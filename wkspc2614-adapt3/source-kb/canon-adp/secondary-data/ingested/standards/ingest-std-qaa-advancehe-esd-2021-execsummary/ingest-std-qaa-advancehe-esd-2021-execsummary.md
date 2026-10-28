---
id: std:doc:qaa-advancehe-esd-2021-execsummary
title: "Education for Sustainable Development Guidance: Executive Summary"
profile: standards/execsummary   # proposed variant (Abbott, 06:46; D-std-0012); not yet in the profile
profileVersion: 0.1.6-draft
issuer: The Quality Assurance Agency for Higher Education (QAA) and Advance HE
kind: execsummary
theme: theme:esd
jurisdiction: [England, Wales, Scotland, Northern Ireland]
subjectScope: universal
subjects: []
edition: March 2021 (executive summary of the full guidance)
published: 2021-03-29
status: current   # as at the held text; not checked against either issuer's site (Part E)
supersedes: "QAA and HEA, Education for Sustainable Development: Guidance for UK Higher Education Providers (2014)"
heldText: { method: sha256-bytes, raw: 0dda656cc85f29a1bad2861e91ee7cfece5a21ce55d6d6a292b34771e53cdbe8, normalised: b35e640f2d4514fa07fd3ed2c9a27173512b405c94e6663369d86af2ea1ed070 }
original: { method: sha256-bytes, pdf: 1634c4cc3b0454d02b1e1ab3eaa4ffee27c437c514d307c29e5a6d6a62831b60, held: no }
licence: none read yet
parts:
  S: "the executive summary's 20 statements; the full guidance is std:doc:qaa-advancehe-esd-2021-guidance (S7)"
  GU: "guidance analysis: families, progression, employability, framework and criteria links, pathways, the benchmark web, a crosswalk to the enterprise guidance, pedagogy handed on"
  B: "the two defined terms"
  C: "none"
pins: { structure: 0.13.0-draft, template: "execsummary 0.1.0-draft (proposed)", runFrame: 0.1.1-draft, runLayer: 0.5.0-draft }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0057
passes:
  P1: "2026-10-03, std (claude.ai, META Project): read direct from Abbott's PDF of the executive summary (05:40); built 05:52"
  P2: "not needed: the full guidance is its own document (std:doc:qaa-advancehe-esd-2021-guidance, run 0063)"
  P3: open
version: 0.3.1
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the proposed standards/execsummary variant (template wpk-0016-ingest-pd-template-standards-execsummary.md 0.1.0-draft), with the guidance analysis Part GU -->
# Education for Sustainable Development Guidance (QAA and Advance HE, 2021): executive summary

> Run 0057, P1 by std; renamed from `-guidance` to `-execsummary` at 06:49 (Abbott, 06:46: "we will use execsummary as another standards profile"). The full guidance is now its own document, std:doc:qaa-advancehe-esd-2021-guidance (run 0063), which supersedes this one's analysis wherever the two differ. **A summary, read for what it holds.** The executive summary describes the full guidance rather than reproducing it: its standards content is the guidance's aim for students, five conditions under which ESD is best achieved, the roles of employers and academics, and the names of the eight key competencies for sustainability. The competencies' definitions and the learning outcomes the full guidance aligns with them are not in the summary; this document names them only and asks for the full text (D3). The teaching ideas go to theory ingest (GU7). Every link is our reading and marked `inferred`.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA and Advance HE's 2021 guidance on education for sustainable development, in its six-page public summary: a cross-cutting theme for every subject. Reach for it to say what sustainability education asks of a student (knowledge, understanding, skills and values to act for sustainable futures), which eight competencies it is built on, what an institution does when ESD is embedded, and how it reaches the subject benchmarks (GU6). For the competencies' content and learning outcomes, the full guidance is needed.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Sustainable development is defined as an ongoing, aspirational process of addressing social, environmental and economic concerns together; ESD as building curriculum structures and subject content that support it. The guidance takes the UN's seventeen Sustainable Development Goals as a starting point, moves ESD beyond environmental issues to the links between economy, society and environment, and frames learning as a transformative journey through ways of thinking, practising and being. Its eight key competencies (after UNESCO) are systems thinking, anticipatory thinking, normative, strategic thinking, collaborative, critical thinking, self-awareness, and integrated problem-solving.

## Part S Standard

### S1 Identity
```yaml
issuer: [The Quality Assurance Agency for Higher Education, Advance HE]
title: "Education for Sustainable Development Guidance: Executive Summary"
edition: March 2021
dates: { published: 2021-03-29, other: ["full guidance 2021: std:doc:qaa-advancehe-esd-2021-guidance", "first edition 2014 (QAA and HEA)"] }
kind: execsummary
form: executive summary
heldText: wkspc2601-library/txt/qaa-and-advance-he-2021-education-sustainable-development-guidance-executive-summary-standard.norm.txt
```

### S2 Purpose and scope
<!-- label: both; status: drafted; basis: primary -->
For staff who design, manage and teach courses, and for senior managers, quality staff and those leading teaching. It supports curriculum design and suggests approaches to teaching, learning and assessment, for readers new to the topic. It can serve as a reference point for course design and as an aid to advocacy. Advisory, like all QAA guidance: it sets no level and no threshold.

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
The summary describes the full guidance: an introduction (global and UK context, student expectations), Section 1 (defining SD and ESD), Section 2 (getting started; strategic commitment; involving students, employers, academics, professional services, governance and communities; the five conditions), Section 3 (teaching, learning and assessment: the key competencies, learning outcomes for courses and modules, learning environments), Section 4 (references and resources). Statements are cut from the aims, the five conditions, the roles and the list of competencies.

### S4 Statements
<!-- label: both; status: drafted; basis: primary. One record per statement, cut at the issuer's own list items and sentences. Extra fields (guidance variant, proposed): `family` (GU1), `employability` (direct: names work, careers or ventures; bridge: a transferable capability employers value; academic: within study), `category` (behaviour, attribute, competency, literacy, awareness, mindset, capability, effectiveness, opportunity, assessment, educator, institution, aim, principle), `maps` (our reading: related framework statements, assessment criteria and academic practice pathways; all `inferred`). -->
```yaml
- id: qaa-advancehe/esd-2021-execsummary/aim.1
  family: aim
  locator: { heading: "Aims of the guidance" }
  span: { start: 437, end: 623 }
  source: "supporting students from any discipline to acquire the knowledge, understanding and skills necessary to develop values and take actions to transition society towards sustainable futures."
  statementType: aim
  force: describes
  addressee: student
  employability: bridge
  verbs: [supporting, acquire, develop, take]
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021-execsummary/aim.2
  family: aim
  locator: { heading: "Aims of the guidance" }
  span: { start: 4125, end: 4320 }
  source: "ESD is part of an educational change agenda allowing us to look critically at how the world is and to envision how it might be, supporting learners to create and pursue visions of a better world."
  statementType: aim
  force: describes
  addressee: student
  employability: bridge
  verbs: [look, envision, create, pursue]
  maps: { pathways: [criticality, creativity], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021-execsummary/aim.3
  family: aim
  locator: { heading: "Aims of the guidance" }
  span: { start: 4321, end: 4490 }
  source: "It outlines the role of higher education in supporting the knowledge, skills and competencies that students and staff develop to contribute to a more sustainable future,"
  statementType: aim
  force: describes
  addressee: student
  employability: bridge
  verbs: [supporting, develop, contribute]
  maps: { basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021-execsummary/principle.b1
  family: principle
  locator: { heading: "ESD is best achieved when:" }
  span: { start: 5278, end: 5401 }
  source: "ESD objectives, targets and KPIs are part of the institution’s strategic priorities and subsequent strategies and policies."
  statementType: institution
  force: should
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021-execsummary/principle.b2
  family: principle
  locator: { heading: "ESD is best achieved when:" }
  span: { start: 5405, end: 5530 }
  source: "The framing of ESD within the curriculum is included in the validation of new courses and ongoing review of existing courses."
  statementType: institution
  force: should
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021-execsummary/principle.b3
  family: principle
  locator: { heading: "ESD is best achieved when:" }
  span: { start: 5534, end: 5646 }
  source: "ESD is central to the staff and student induction process, as well as staff appraisal and/or promotion criteria."
  statementType: institution
  force: should
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021-execsummary/principle.b4
  family: principle
  locator: { heading: "ESD is best achieved when:" }
  span: { start: 5650, end: 5720 }
  source: "ESD is articulated within quality assurance and enhancement processes."
  statementType: institution
  force: should
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021-execsummary/principle.b5
  family: principle
  locator: { heading: "ESD is best achieved when:" }
  span: { start: 5724, end: 5801 }
  source: "Staff development to enable ESD is fully supported at an institutional level."
  statementType: institution
  force: should
  addressee: provider
  employability: academic
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021-execsummary/role.employers
  family: role
  locator: { heading: "Roles: employers, academics, staff" }
  span: { start: 5861, end: 5960 }
  source: "we stress how ESD competencies can accelerate sustainable change once students enter the workplace."
  statementType: competency
  force: describes
  addressee: graduate
  employability: direct
  verbs: [accelerate]
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021-execsummary/role.academics
  family: role
  locator: { heading: "Roles: employers, academics, staff" }
  span: { start: 6018, end: 6146 }
  source: "their approaches to curriculum design, teaching and assessment provide learners with opportunities to gain the key competencies."
  statementType: opportunity
  force: describes
  addressee: educator
  employability: bridge
  verbs: [provide, gain]
  maps: { pathways: [understanding-learning-assessment-and-feedback], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021-execsummary/role.reflect
  family: role
  locator: { heading: "Roles: employers, academics, staff" }
  span: { start: 6147, end: 6234 }
  source: "It is crucial that academic staff reflect critically on their own knowledge and skills."
  statementType: educator
  force: must
  addressee: educator
  employability: academic
  verbs: [reflect]
  maps: { pathways: [reflective-practice], basis: inferred }
  audience: practitioner
- id: qaa-advancehe/esd-2021-execsummary/role.outcomes
  family: role
  locator: { heading: "Roles: employers, academics, staff" }
  span: { start: 7159, end: 7250 }
  source: "interconnecting subject-specific learning outcomes with the UN’s SDGs and ESD competencies."
  statementType: outcome-design
  force: describes
  addressee: educator
  employability: academic
  verbs: [interconnecting]
  maps: { pathways: [understanding-learning-assessment-and-feedback], basis: inferred }
  audience: both
- id: qaa-advancehe/esd-2021-execsummary/competency.b1
  family: competency
  locator: { heading: "Key competencies for sustainability (UNESCO), named" }
  span: { start: 6921, end: 6937 }
  source: "systems thinking"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [criticality], basis: inferred }
  audience: both
  basis: "name only: our gloss of the competency name; its definition and outcomes are in the full guidance (D3)"
- id: qaa-advancehe/esd-2021-execsummary/competency.b2
  family: competency
  locator: { heading: "Key competencies for sustainability (UNESCO), named" }
  span: { start: 6941, end: 6962 }
  source: "anticipatory thinking"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [creativity, criticality], basis: inferred }
  audience: both
  basis: "name only: our gloss of the competency name; its definition and outcomes are in the full guidance (D3)"
- id: qaa-advancehe/esd-2021-execsummary/competency.b3
  family: competency
  locator: { heading: "Key competencies for sustainability (UNESCO), named" }
  span: { start: 6966, end: 6986 }
  source: "normative competency"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: critical-approach], pathways: [criticality], basis: inferred }
  audience: both
  basis: "name only: our gloss of the competency name; its definition and outcomes are in the full guidance (D3)"
- id: qaa-advancehe/esd-2021-execsummary/competency.b4
  family: competency
  locator: { heading: "Key competencies for sustainability (UNESCO), named" }
  span: { start: 6990, end: 7008 }
  source: "strategic thinking"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
  basis: "name only: our gloss of the competency name; its definition and outcomes are in the full guidance (D3)"
- id: qaa-advancehe/esd-2021-execsummary/competency.b5
  family: competency
  locator: { heading: "Key competencies for sustainability (UNESCO), named" }
  span: { start: 7012, end: 7036 }
  source: "collaborative competency"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
  basis: "name only: our gloss of the competency name; its definition and outcomes are in the full guidance (D3)"
- id: qaa-advancehe/esd-2021-execsummary/competency.b6
  family: competency
  locator: { heading: "Key competencies for sustainability (UNESCO), named" }
  span: { start: 7040, end: 7057 }
  source: "critical thinking"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [bristol/generic-2024: critical-approach, cardiffmet/generic-2020: argument], pathways: [criticality], basis: inferred }
  audience: both
  basis: "name only: our gloss of the competency name; its definition and outcomes are in the full guidance (D3)"
- id: qaa-advancehe/esd-2021-execsummary/competency.b7
  family: competency
  locator: { heading: "Key competencies for sustainability (UNESCO), named" }
  span: { start: 7061, end: 7075 }
  source: "self-awareness"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
  basis: "name only: our gloss of the competency name; its definition and outcomes are in the full guidance (D3)"
- id: qaa-advancehe/esd-2021-execsummary/competency.b8
  family: competency
  locator: { heading: "Key competencies for sustainability (UNESCO), named" }
  span: { start: 7079, end: 7116 }
  source: "integrated problem-solving competency"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { framework: [qaa/fheq-2024/4.17.b5], criteria: [bristol/generic-2024: problem-solving, cardiffmet/generic-2020: analysis], pathways: [criticality, creativity], basis: inferred }
  audience: both
  basis: "name only: our gloss of the competency name; its definition and outcomes are in the full guidance (D3)"
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. Student versions in the second person, naming no issuer; force kept. -->
```yaml
- statement: qaa-advancehe/esd-2021-execsummary/aim.1
  forPractitioner: { text: "The guidance aims to help students of any discipline gain the knowledge, understanding and skills to form values and act towards sustainable futures.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Whatever your subject, you should gain the knowledge and skills to form your own values and act for a sustainable future.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/aim.2
  forPractitioner: { text: "ESD lets learners look critically at the world as it is, imagine how it might be, and create and pursue visions of a better one.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You look critically at how the world is, imagine how it could be, and work towards a better version.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/aim.3
  forPractitioner: { text: "Higher education has a part in building the knowledge, skills and competencies by which students and staff help make the future more sustainable.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your university helps you build the knowledge and skills to contribute to a more sustainable future.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/principle.b1
  forPractitioner: { text: "ESD objectives, targets and KPIs sit in the institution's strategic priorities, strategies and policies.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa-advancehe/esd-2021-execsummary/principle.b2
  forPractitioner: { text: "Course validation and review consider how the curriculum frames ESD.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You can expect sustainability to be built into how your course is designed, reviewed and taught.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/principle.b3
  forPractitioner: { text: "ESD is central to staff and student induction and to staff appraisal or promotion criteria.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You can expect sustainability to be built into how your course is designed, reviewed and taught.", rewrite: full, force: should, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/principle.b4
  forPractitioner: { text: "Quality assurance and enhancement processes set out ESD.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa-advancehe/esd-2021-execsummary/principle.b5
  forPractitioner: { text: "The institution fully supports staff development for ESD.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa-advancehe/esd-2021-execsummary/role.employers
  forPractitioner: { text: "Graduates' ESD competencies can speed up sustainable change at work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "The sustainability skills you gain can help speed up change in the workplace.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/role.academics
  forPractitioner: { text: "Curriculum design, teaching and assessment give learners the chance to gain the key competencies.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your course design, teaching and assessment give you chances to gain these competencies.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/role.reflect
  forPractitioner: { text: "Academic staff must reflect critically on their own sustainability knowledge and skills.", rewrite: light, force: must, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa-advancehe/esd-2021-execsummary/role.outcomes
  forPractitioner: { text: "Subject learning outcomes are to be linked with the SDGs and the ESD competencies (the full guidance discusses how).", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your subject's learning outcomes can be linked to the global sustainability goals.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/competency.b1
  forPractitioner: { text: "Systems thinking. One of eight UNESCO key competencies; the summary names it, and the full guidance gives its learning outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to see how parts of a system connect and affect one another.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/competency.b2
  forPractitioner: { text: "Anticipatory thinking. One of eight UNESCO key competencies; the summary names it, and the full guidance gives its learning outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to think ahead about possible futures.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/competency.b3
  forPractitioner: { text: "Normative competency. One of eight UNESCO key competencies; the summary names it, and the full guidance gives its learning outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to work with the values and norms behind decisions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/competency.b4
  forPractitioner: { text: "Strategic thinking. One of eight UNESCO key competencies; the summary names it, and the full guidance gives its learning outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to plan action towards a goal.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/competency.b5
  forPractitioner: { text: "Collaborative competency. One of eight UNESCO key competencies; the summary names it, and the full guidance gives its learning outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to work with others towards shared aims.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/competency.b6
  forPractitioner: { text: "Critical thinking. One of eight UNESCO key competencies; the summary names it, and the full guidance gives its learning outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to question assumptions and evidence.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/competency.b7
  forPractitioner: { text: "Self-awareness. One of eight UNESCO key competencies; the summary names it, and the full guidance gives its learning outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to reflect on your own values, role and actions.", rewrite: full, force: describes, status: drafted }
- statement: qaa-advancehe/esd-2021-execsummary/competency.b8
  forPractitioner: { text: "Integrated problem-solving competency. One of eight UNESCO key competencies; the summary names it, and the full guidance gives its learning outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to bring these competencies together to solve complex problems.", rewrite: full, force: describes, status: drafted }
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary for the absence of levels; inferred for the alignment -->
No levels. The competencies and the transformative journey are level-free in the summary; the full guidance does not level its learning outcomes either (std:doc:qaa-advancehe-esd-2021-guidance, S5).

### S6 Themes
`theme:esd` (this document is the theme's reference text); `theme:enterprise` (the enterprise guidance ties green and social entrepreneurship to sustainability education, GU2 crosswalk); employability (one direct statement: competencies that speed change once graduates are at work).

### S7 Relations
```yaml
- { type: themeReference, target: theme:esd }
- { type: supersedes, target: "QAA and HEA ESD guidance 2014 (not held)" }
- { type: summaryOf, target: std:doc:qaa-advancehe-esd-2021-guidance, basis: primary }
- { type: citedBy, target: "49 of the 54 subject benchmark statements held cite ESD guidance by title (GU6)", basis: primary }
- { type: citedBy, target: std:doc:qaa-enterprise-2018-guidance, note: "cites the 2014 edition", basis: primary }
- { type: mapsTo, target: std:doc:qaa-fheq-2024-framework, basis: inferred }
- { type: mapsTo, target: std:doc:bristol-generic-2024-assesscriteria, basis: inferred }
- { type: handsTo, target: "theory ingest (ing): the pedagogy in GU7" }
```

### S8 Currency and review
<!-- label: both; status: drafted; basis: primary -->
Published 29 March 2021, replacing the 2014 guidance. The issuers promised workshops and further support; any later revision is unchecked (E2).

### S9 Commentary (optional)
<!-- label: practitioner; status: drafted; basis: inferred -->
Thin as a standards source, rich as a hub. The summary states one aim for students and names eight competencies, but its weight lies in where it is cited: nearly every benchmark has a sustainability paragraph and 37 carry sustainability into their standards, more than enterprise or employability (GU6). The benchmarks, not this summary, are where ESD becomes a subject standard.

## Part GU Guidance analysis

### GU1 Statement families
<!-- The kinds of standards assertion the guidance makes, by family: who it addresses, its usual force, and how many records. -->

| Family | Heading | Records | Addressee | Force | Student versions |
|---|---|---|---|---|---|
| aim | Aims of the guidance | 3 | student | describes | 3 |
| principle | ESD is best achieved when: | 5 | provider | should | 2 |
| competency | Key competencies for sustainability (UNESCO), named | 8 | student | describes | 8 |
| role | Roles: employers, academics, staff | 4 | educator, graduate | describes, must | 3 |

### GU2 Progression
<!-- label: both; status: drafted; basis: primary for the three ways; inferred for the rest -->
The summary's model of growth is a transformative journey in three ways: of thinking, of practising, of being. It names no stages and no levels. Read against the frameworks:

| Way | Competencies it most draws on (our reading) | Nearest framework strand | Note |
|---|---|---|---|
| thinking | systems, anticipatory, critical thinking | FHEQ Annex D cognitive skills | levels well: the FHEQ's analyse, evaluate, synthesise ladder applies |
| practising | strategic thinking, collaborative, integrated problem-solving | Annex D practical and transferable skills; the "wider abilities" | levels by autonomy and complexity, as in the FHEQ |
| being | normative, self-awareness | none | the frameworks state no values; this is the guidance's addition, and the one hardest to assess by grade |

**Suggestion.** Level the competencies the way the frameworks level cognitive skills: at L4 recognise and describe (the systems a subject touches; the SDGs it bears on); at L5 apply and analyse (trace interactions; compare futures); at L6 evaluate and judge (weigh trade-offs between social, environmental and economic aims; argue a normative position); at L7 act and lead (design and lead an intervention under uncertainty, with stakeholders). Hold "being" outcomes to reflective evidence rather than graded performance.

**Crosswalk to the enterprise guidance** (std:doc:qaa-enterprise-2018-guidance; ours):

| Key competency | Enterprise outcome theme | Note |
|---|---|---|
| systems thinking | decision (analysis and synthesis) | enterprise has no systems view; ESD adds it |
| anticipatory thinking | communication (visualising the future) | both ask for futures thinking |
| normative competency | (none) | enterprise mentions ethics but states no values competency |
| strategic thinking | implementation; decision | planning action to a goal |
| collaborative competency | communication; implementation (teams, relationships) | shared |
| critical thinking | decision; opportunity (evaluating solutions) | shared |
| self-awareness | reflection; the mindset family | shared |
| integrated problem-solving | creativity; opportunity | shared |

Six of the eight have an enterprise counterpart; systems thinking and the normative competency are ESD's own. A pathway or module drawing on both guidance documents can treat the shared six as one competency set with two contexts (venture and sustainability).


### GU3 Employability
<!-- Each record tagged: `direct` names work, careers, employers or ventures; `bridge` is a capability that study and work share; `academic` stays within study. Our reading. -->

| Tag | Records | Categories |
|---|---|---|
| direct | 1 | competency 1 |
| bridge | 12 | competency 8, aim 3, opportunity 1 |
| academic | 7 | institution 5, educator 1, outcome-design 1 |

**Direct statements:** `role.employers`.

**Reading.** One statement is direct (graduates' competencies speeding sustainable change at work); most are bridges, because the competencies serve study and work alike. The summary says employers' priorities are shifting towards sustainability, but states no employability outcome. The full guidance involves employers among its key players; its statements on them are wanted (D3).

**Suggestion.** Tag the eight competencies `bridge` and record, in each benchmark ingested, whether its sustainability paragraph names a professional duty (for example a code of conduct or an accrediting body's requirement); where it does, the competency becomes `direct` for that subject.


### GU4 Links to framework levels and assessment criteria
<!-- Counts of records linked, our reading (`inferred`). Framework statements are std:doc:qaa-fheq-2024-framework's; criteria are Bristol's (b:) and Cardiff Met's (c:) generic marking criteria. -->

| Framework statement | Records |
|---|---|
| qaa/fheq-2024/4.15.b7 | 1 |
| qaa/fheq-2024/4.17.b5 | 1 |

| Assessment criterion | Records |
|---|---|
| Bristol: problem-solving | 2 |
| Bristol: decision-making | 2 |
| Bristol: critical-approach | 2 |
| Bristol: teamwork | 1 |
| Cardiff Met: argument | 1 |
| Bristol: insight | 1 |
| Cardiff Met: analysis | 1 |

**Reading.** Only two records sit close to an FHEQ statement (critical thinking with the honours descriptor's evaluation of arguments; integrated problem-solving with the master's descriptor's decisions in complex situations). The frameworks name no sustainability outcome; the link runs through the benchmarks. Against the marking criteria, Bristol's problem-solving, decision-making, critical-approach, teamwork and insight rows take the competencies.

**Suggestions for learning outcomes and assessment.**
1. The full guidance aligns learning outcomes with each competency; they are ingested in std:doc:qaa-advancehe-esd-2021-guidance (S4, Table 2) and levelled there (GU2).
2. Until then, a module can name its SDGs and one or two competencies, and write the outcome as the subject task that exercises them, assessed on the matching criterion row.
3. The normative competency and self-awareness need an assessment form neither generic grid has: reflective or position writing judged on how well values are made explicit and reasoned, not on which values are held.


### GU5 Academic practice pathways
<!-- Records per pathway (ACPRAC-DAT's thirteen, used loosely as categories), our reading. -->

| Pathway | Records | Families |
|---|---|---|
| reflective-practice | 2 | role 1, competency 1 |
| researching-and-research-methods | 0 | (none) |
| work-based-and-experiential-learning | 3 | competency 2, role 1 |
| finding-and-using-sources | 0 | (none) |
| criticality | 7 | competency 5, aim 2 |
| academic-writing | 0 | (none) |
| referencing | 0 | (none) |
| understanding-learning-assessment-and-feedback | 2 | role 2 |
| starting-progressing-and-succeeding | 0 | (none) |
| presenting | 0 | (none) |
| revising-and-exams | 0 | (none) |
| ai-and-technology | 0 | (none) |
| creativity | 3 | competency 2, aim 1 |

**Reading.** Criticality dominates (systems, anticipatory, normative and critical thinking all fall there), then creativity (envisioning better worlds), work-based and experiential learning (strategic and collaborative competencies) and reflective practice (self-awareness). The summary says nothing about writing, sources or referencing.

**Suggestions for pathways.**
1. Criticality: add the systems and normative competencies as a strand (weighing interconnected social, environmental and economic aims), which the frameworks' cognitive skills do not name.
2. Reflective practice: self-awareness here means one's values and part in change, a wider object than reflection on learning; a reflective-practice pathway can carry it as its "being" strand.
3. Creativity: anticipatory thinking and envisioning futures pair with the enterprise guidance's creativity theme.


### GU6 The benchmark web
<!-- label: practitioner; status: drafted; basis: primary for the paragraph and citation counts (a scan of the 54 benchmark texts held in stan); inferred for the reading -->
The same scan as std:doc:qaa-enterprise-2018-guidance GU6, read here for sustainability. Columns as there.

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


**Reading.** Sustainability is the cross-cutting theme that has gone furthest into subject standards: all 54 held benchmarks have sustainability paragraphs, 49 cite ESD guidance by title (either edition; the scan does not separate them), and 37 use sustainability words inside their benchmark standards, against 12 for enterprise. In the standards we sampled, the theme mostly appears as one clause in a list of contexts a graduate weighs (social, economic, environmental, ethical) rather than as a competency of its own; some subjects give it more than one standard (accounting, agriculture and related sciences, architectural technology, for example). A full reading waits on the benchmark runs (S-02).

**Suggestion.** In each benchmark ingested, mark the statements that use sustainability words with `theme:esd` and map them to the key competency they exercise (most often systems or normative thinking). That gives every subject a line from this guidance's competencies to its own threshold.

### GU7 Pedagogy handed to theory ingest
<!-- label: practitioner; status: drafted; basis: primary -->
Named here, not ingested:
- UNESCO's key competencies for sustainability (UNESCO, 2017) and their learning objectives;
- the UN Sustainable Development Goals as a curriculum frame;
- ways of thinking, practising and being as a transformative journey;
- the whole-institution approach;
- co-creation of learning with students;
- learning environments for ESD.

## Part B Terminology
<!-- label: both; status: drafted; basis: primary; paraphrased -->
```yaml
- { term: sustainable development, gloss: "An ongoing process, aspirational in aim, of tackling social, environmental and economic concerns together for a better world." }
- { term: education for sustainable development, gloss: "Building curriculum structures and subject content that support sustainable development." }
- { term: key competencies for sustainability, gloss: "Eight competencies (after UNESCO) that the guidance's learning outcomes are aligned with (S4 competency.b1 to b8)." }
- { term: whole-institution approach, gloss: "Embedding ESD across strategy, curricula, quality processes and staff development, not in single modules." }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->
None.

## Part D Sources

### D1 Held text
The executive summary Abbott supplied (6 pages, sha256-bytes 1634c4cc…), converted with pdftotext and normalised; the PDF is not held in UNI. Figure 1 (the SDGs) is not cut into statements.

### D2 Research log
- 2026-10-03 05:40 to 05:52, std: read direct; 20 statements in four families; crosswalk to the enterprise guidance; benchmark scan shared with run 0056.

### D3 Wanted sources
- W-std-0009: UNESCO (2017), Education for Sustainable Development Goals: Learning Objectives: the source of the competencies.
- W-std-0010: The 2014 QAA and HEA guidance, for the change record.
- W-std-0020: (The full 2021 guidance was supplied by Abbott at 06:46 and is run 0063.)

## Part E Gaps and questions
- E1 A summary: the competencies are named here, not defined (records carry `basis: name only`); their definitions and outcomes are in std:doc:qaa-advancehe-esd-2021-guidance.
- E2 Currency unchecked.
- E3 Every map is ours.

---

## Change notes
- 0.3.1, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.3.0, 3 October 2026, 11:00: every statement record now carries the issuer's statement in full (`source`, taken from its span in the held text) beside our paraphrase and versions, for language analysis; private, never published (Abbott, 10:56 and 10:59; D-std-0014). No paraphrase changed.
- 0.2.1, 3 October 2026, 07:34: provenance lines added to Parts B and C; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.2.0, 3 October 2026, 06:49: renamed `ingest-std-qaa-advancehe-esd-2021-execsummary`, id `std:doc:qaa-advancehe-esd-2021-execsummary`, statement ids `qaa-advancehe/esd-2021-execsummary/...`, variant `standards/execsummary` (Abbott, 06:46; D-std-0012); points to the full guidance, run 0063.
- 0.1.0, 3 October 2026, 05:52: first build, run 0057 (std; Abbott, 05:40).

