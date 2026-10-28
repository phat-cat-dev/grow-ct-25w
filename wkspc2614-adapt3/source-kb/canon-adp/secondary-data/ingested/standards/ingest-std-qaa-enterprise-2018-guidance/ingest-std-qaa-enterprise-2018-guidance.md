---
id: std:doc:qaa-enterprise-2018-guidance
title: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers"
profile: standards/guidance   # proposed variant (D-std-0011, P5b); not yet in the profile
profileVersion: 0.1.6-draft
issuer: The Quality Assurance Agency for Higher Education (QAA)
kind: guidance
theme: theme:enterprise
jurisdiction: [England, Wales, Scotland, Northern Ireland]
subjectScope: universal
subjects: []
edition: January 2018 (QAA2042)
published: 2018-01
status: current   # as at the held text; not checked against QAA's site (Part E)
supersedes: "Enterprise and entrepreneurship education: Guidance for UK higher education providers (QAA, 2012)"
heldText: { method: sha256-bytes, raw: 2d964955da861fd468e8eb3fbb1a03c7863e99fbf245c32fdb5c5d0cd8f0aeec, normalised: 59673311692ed68412ad9227c271461eed7be4376ebf310ea1247bfffbeafb4e }
original: { method: sha256-bytes, pdf: c11bde8113a7d57d84ba8f8400aab80306027f6de167777ac5217e4356b3d3ff, held: no }
licence: none read yet
parts:
  S: "full: 103 statements in eleven families"
  GU: "guidance analysis: families, progression, employability, framework and criteria links, pathways, the benchmark web, pedagogy handed on"
  B: "the guidance's defined terms"
  C: "none (the guidance sets no process standards bodies must follow)"
pins: { structure: 0.13.0-draft, template: "guidance 0.1.0-draft (proposed)", runFrame: 0.1.1-draft, runLayer: 0.5.0-draft }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0056
passes:
  P1: "2026-10-03, std (claude.ai, META Project): read direct from Abbott's PDF (05:40); built 05:52"
  P2: "skipped: read direct from the issuer's PDF"
  P3: open
version: 0.2.1
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the proposed standards/guidance variant (template wpk-0016-ingest-pd-template-standards-guidance.md 0.1.0-draft), with the guidance analysis Part GU -->
# Enterprise and Entrepreneurship Education (QAA, 2018)

> Run 0056, P1 by std. **A guidance document read for its standards statements** (Abbott, 05:40): what it says a student or graduate should be able to do, be or show, and what it asks educators and providers to offer so that students can. The teaching ideas it carries (learning about, for and through enterprise; experiential learning; EntreComp; Venture Creation Programmes) go to theory ingest and are only named here (GU7). Every link to a framework statement, a marking criterion, a benchmark or a pathway is our reading and marked `inferred`.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's 2018 guidance on enterprise and entrepreneurship in UK higher education: a cross-cutting theme, written for any subject. Reach for it to say what an enterprising graduate can do (23 outcomes in seven themes), how that capability grows (four stages from awareness to effectiveness), what teaching should give students the chance to do, how such learning can be assessed, and how enterprise sits beside employability. It sets no levels and no thresholds: its statements are level-free and lean on the frameworks and the benchmarks for both.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
The guidance defines enterprise (generating ideas and applying them in practical settings) and entrepreneurship (applying enterprise to create cultural, social or economic value, sometimes through a new venture), and keeps both apart from employability, for which it takes Knight and Yorke's (2003) definition. Its standards content falls into eleven families: a principle of opportunity for every student, aims, a vocabulary of behaviours, attributes and competencies, assessment goals, a four-stage learning journey, the qualities of an entrepreneurial mindset, 23 graduate outcomes, 33 delivery opportunities, nine assessment considerations, the educator's role (after SFEDI's occupational standards) and five marks of an entrepreneurial institution. Most statements are bridges: capabilities that serve both study and work (GU3).

## Part S Standard

### S1 Identity
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers"
edition: January 2018
dates: { published: 2018-01, other: ["first edition 2012"] }
kind: guidance
code: QAA2042
partners: "named in the guidance's Appendix 3 (enterprise educator and entrepreneurship education bodies)"
heldText: wkspc2601-library/txt/qaa-2018-enterprise-entrepreneurship-education-guidance-standard.norm.txt
```

### S2 Purpose and scope
<!-- label: both; status: drafted; basis: primary -->
Written for educators in any subject and for the providers that support them, the guidance aims to help embed enterprise and entrepreneurship in curricular, co-curricular and extracurricular learning. It states its principle at the start: every student should be able to take part, in a form that fits their subject. It is advisory. Unlike a framework or a benchmark it carries no expectation that providers meet it, and it sets no level; its "should" statements say what good provision looks like.

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
Foreword; introduction and context (the value, the aims and vision, policy context in the UK and abroad); definitions and distinctions (enterprise, entrepreneurship, employability, enterprise education, entrepreneurship education, entrepreneurial education, and how employability, enterprise and entrepreneurship relate); delivering enterprise and entrepreneurship education (the educator's role, delivery, assessment, the gateway triangle, EntreComp, the four-stage journey); graduate outcomes in seven themes, each with its delivery opportunities; evaluation and impact; the supporting institution; Venture Creation Programmes; three appendices (resources, the 2018 advisory group, partner organisations). The standards statements are cut from the definitions, the journey, the outcomes and delivery lists, the assessment list, the educator list and the institution list (GU1).

### S4 Statements
<!-- label: both; status: drafted; basis: primary. One record per statement, cut at the issuer's own list items and sentences. Extra fields (guidance variant, proposed): `family` (GU1), `employability` (direct: names work, careers or ventures; bridge: a transferable capability employers value; academic: within study), `category` (behaviour, attribute, competency, literacy, awareness, mindset, capability, effectiveness, opportunity, assessment, educator, institution, aim, principle), `maps` (our reading: related framework statements, assessment criteria and academic practice pathways; all `inferred`). -->
```yaml
- id: qaa/enterprise-2018/principle.1
  family: principle
  locator: { heading: "Principle: every student has the opportunity" }
  span: { start: 6862, end: 6998 }
  source: "all students should have an opportunity to engage with Enterprise and Entrepreneurship, and to align it with their subject(s) of choice."
  statementType: principle
  force: should
  addressee: provider
  employability: bridge
  verbs: [engage, align]
  maps: { pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/principle.2
  family: principle
  locator: { heading: "Principle: every student has the opportunity" }
  span: { start: 6999, end: 7148 }
  source: "This will enable them to identify and seek out new opportunities; have higher aspirations in their careers; be resilient; and better adapt to change."
  statementType: attribute
  force: describes
  addressee: student
  employability: direct
  verbs: [identify, seek, adapt]
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/aim.enterprise
  family: aim
  locator: { heading: "Aims of Enterprise and of Entrepreneurship Education" }
  span: { start: 25855, end: 26171 }
  source: "The aim of Enterprise Education is to produce graduates with an awareness, mindset and capability to generate original ideas in response to identified needs, opportunities and shortfalls, and the ability to act on them, even if circumstances are changing and ambiguous; in short, having an idea and making it happen."
  statementType: competency
  force: describes
  addressee: graduate
  employability: bridge
  verbs: [generate, act]
  maps: { framework: [qaa/fheq-2024/4.17.b6], criteria: [bristol/generic-2024: problem-solving], pathways: [creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/aim.entrepreneurship
  family: aim
  locator: { heading: "Aims of Enterprise and of Entrepreneurship Education" }
  span: { start: 26853, end: 27331 }
  source: "Entrepreneurship Education aims to build upon the enterprising competencies of students who are capable of identifying opportunities and developing ventures, through becoming self-employed, setting up new businesses or developing and growing part of an existing venture. It focuses on the application of enterprising competencies and extends the learning environment into realistic risk environments that may include legal issues, funding issues, start-up and growth strategies."
  statementType: competency
  force: describes
  addressee: student
  employability: direct
  verbs: [build, identifying, developing, focuses, extends]
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/aim.realisation
  family: aim
  locator: { heading: "Aims of Enterprise and of Entrepreneurship Education" }
  span: { start: 27579, end: 27802 }
  source: "Entrepreneurship Education is the realisation of ideas, through an enhanced understanding and application of business processes within the legal and ethical constraints that are found in the context of their chosen venture."
  statementType: literacy
  force: describes
  addressee: student
  employability: direct
  verbs: [realisation]
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/aim.respond
  family: aim
  locator: { heading: "Aims of Enterprise and of Entrepreneurship Education" }
  span: { start: 30963, end: 31147 }
  source: "Students should be able to identify and respond to opportunities using their ideas, knowledge, skills and confidence to create interventions that will address the challenges they meet."
  statementType: competency
  force: should
  addressee: student
  employability: bridge
  verbs: [identify, respond, create, address]
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [bristol/generic-2024: problem-solving, cardiffmet/generic-2020: analysis], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/vocab.behaviours
  family: vocab
  locator: { heading: "What enterprise behaviours, attributes and competencies can include" }
  span: { start: 26176, end: 26402 }
  source: "Enterprise behaviours can include: taking the initiative, making things happen, reflecting, communicating, pivoting and adapting, storytelling, taking responsibility, networking, personal effectiveness and managed risk taking."
  statementType: behaviour
  force: describes
  addressee: student
  employability: bridge
  verbs: [taking, making, reflecting, communicating, adapting]
  maps: { framework: [qaa/fheq-2024/4.15.b9.1], criteria: [bristol/generic-2024: self-management, bristol/generic-2024: communication, bristol/generic-2024: insight], pathways: [reflective-practice, presenting, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/vocab.attributes
  family: vocab
  locator: { heading: "What enterprise behaviours, attributes and competencies can include" }
  span: { start: 26408, end: 26555 }
  source: "Enterprise attributes can include: open mindedness, proactivity, curiosity, self-efficacy, flexibility, adaptability, determination and resilience."
  statementType: attribute
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: insight], pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/vocab.competencies
  family: vocab
  locator: { heading: "What enterprise behaviours, attributes and competencies can include" }
  span: { start: 26561, end: 26824 }
  source: "Enterprise competencies can include: intuitive decision making, identifying opportunities, creative problem solving, innovating, strategic thinking, design thinking, negotiation, communicating, influencing, leadership and financial, business and digital literacy."
  statementType: competency
  force: describes
  addressee: student
  employability: direct
  verbs: [identifying, innovating, thinking, negotiation, influencing]
  maps: { framework: [qaa/fheq-2024/4.15.b9.2], criteria: [bristol/generic-2024: problem-solving, bristol/generic-2024: decision-making, bristol/generic-2024: teamwork], pathways: [creativity, criticality, presenting], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/goal.enterprise
  family: goal
  locator: { heading: "Assessment goals for Enterprise and for Entrepreneurship Education" }
  span: { start: 31310, end: 31653 }
  source: "Enterprise Education develops students’ capabilities as enquiring, critical thinking, future orientated thinkers, who are equipped to face the challenges of their careers along with awareness of civic and social responsibility. The predominant assessment strategy asks ‘are they being innovative, challenging norms and seeing new ways forward?"
  statementType: competency
  force: describes
  addressee: student
  employability: bridge
  verbs: [develops]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [criticality, creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/goal.entrepreneurship
  family: goal
  locator: { heading: "Assessment goals for Enterprise and for Entrepreneurship Education" }
  span: { start: 31655, end: 32089 }
  source: "Entrepreneurship Education focuses enterprising competencies in the context of new venture creation and business environments, developing entrepreneurial graduates and citizens who are able to undertake autonomous learning and self-evaluation in more risky contexts that include legal, financial and ethical considerations. The predominant assessment strategy is ‘can they apply and implement their ideas within practical constraints?"
  statementType: competency
  force: describes
  addressee: student
  employability: direct
  verbs: [undertake, apply, implement]
  maps: { criteria: [bristol/generic-2024: decision-making, bristol/generic-2024: self-management], pathways: [work-based-and-experiential-learning, reflective-practice], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/goal.value
  family: goal
  locator: { heading: "Assessment goals for Enterprise and for Entrepreneurship Education" }
  span: { start: 36152, end: 36449 }
  source: "Delivery of Entrepreneurial Education should enable students to express the notion of their value propositions both within their studies, and in relation to external stakeholder perspectives. These could be financial, social or related to sustainability, and should include ethical considerations."
  statementType: competency
  force: should
  addressee: educator
  employability: direct
  verbs: [express]
  maps: { framework: [qaa/fheq-2024/4.15.b8], criteria: [bristol/generic-2024: communication], pathways: [presenting], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/journey.awareness.1
  family: journey
  locator: { heading: "The learning journey: awareness, mindset, capability, effectiveness" }
  span: { start: 51926, end: 52053 }
  source: "Students acquire enterprise awareness by developing knowledge and understanding of enterprising and entrepreneurial activities."
  statementType: awareness
  force: describes
  addressee: student
  employability: bridge
  verbs: [acquire, developing]
  maps: { pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/journey.awareness.2
  family: journey
  locator: { heading: "The learning journey: awareness, mindset, capability, effectiveness" }
  span: { start: 52054, end: 52216 }
  source: "They will understand the professional significance of Enterprise and Entrepreneurship in the wider world, as well as its meaning and relevance to them personally."
  statementType: awareness
  force: will
  addressee: student
  employability: direct
  verbs: [understand]
  maps: { pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/journey.awareness.3
  family: journey
  locator: { heading: "The learning journey: awareness, mindset, capability, effectiveness" }
  span: { start: 53667, end: 53826 }
  source: "Enterprise and Entrepreneurship Education should encourage students to be critically aware of the influence of media stereotypes in Entrepreneurship Education."
  statementType: awareness
  force: should
  addressee: educator
  employability: academic
  verbs: [encourage]
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/journey.mindset.0
  family: journey
  locator: { heading: "The learning journey: awareness, mindset, capability, effectiveness" }
  span: { start: 53869, end: 54104 }
  source: "Students should be encouraged to develop self-awareness of their own enterprising and entrepreneurial capabilities, as well as the motivation and self-discipline to apply these flexibly in different contexts to achieve desired results."
  statementType: mindset
  force: should
  addressee: student
  employability: bridge
  verbs: [develop, apply]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/journey.capability.1
  family: journey
  locator: { heading: "The learning journey: awareness, mindset, capability, effectiveness" }
  span: { start: 56738, end: 56945 }
  source: "This might be demonstrated when a student designs a new service or product to meet an identified need, or identifies an opportunity and visualises potential actions together with their prospects for success."
  statementType: capability
  force: describes
  addressee: student
  employability: direct
  verbs: [designs, identifies, visualises]
  maps: { framework: [qaa/fheq-2024/4.15.b6], criteria: [bristol/generic-2024: problem-solving], pathways: [creativity, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/journey.capability.2
  family: journey
  locator: { heading: "The learning journey: awareness, mindset, capability, effectiveness" }
  span: { start: 56946, end: 57162 }
  source: "Through gaining practical insights, learning experiences will increasingly develop entrepreneurial capabilities, enabling students to take the lead and demonstrate autonomy, either individually or as part of a group."
  statementType: capability
  force: will
  addressee: student
  employability: bridge
  verbs: [develop, enabling, take, demonstrate]
  maps: { framework: [qaa/fheq-2024/4.17.b6], criteria: [bristol/generic-2024: teamwork, bristol/generic-2024: self-management], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/journey.capability.3
  family: journey
  locator: { heading: "The learning journey: awareness, mindset, capability, effectiveness" }
  span: { start: 57318, end: 57453 }
  source: "Students will be encouraged to recognise that team-based performance is an essential feature of both employed and entrepreneurial work."
  statementType: capability
  force: will
  addressee: student
  employability: direct
  verbs: [recognise]
  maps: { criteria: [bristol/generic-2024: teamwork, cardiffmet/generic-2020: analysis], pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/journey.effectiveness.1
  family: journey
  locator: { heading: "The learning journey: awareness, mindset, capability, effectiveness" }
  span: { start: 58356, end: 58565 }
  source: "Entrepreneurial effectiveness is likely to be achieved as the student moves toward completion of their current study and prepares for the transition into work, self-employment, further study, or other options."
  statementType: effectiveness
  force: describes
  addressee: student
  employability: direct
  verbs: [achieved, moves, prepares]
  maps: { pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/journey.effectiveness.2
  family: journey
  locator: { heading: "The learning journey: awareness, mindset, capability, effectiveness" }
  span: { start: 58739, end: 58862 }
  source: "By this stage, students’ learning becomes increasingly self-directed, pursuing both academic and broader career-life goals."
  statementType: effectiveness
  force: describes
  addressee: student
  employability: bridge
  verbs: [becomes, pursuing]
  maps: { framework: [qaa/fheq-2024/4.15.b5], criteria: [bristol/generic-2024: self-management], pathways: [starting-progressing-and-succeeding, reflective-practice], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/mindset.b1
  family: mindset
  locator: { heading: "Developing an entrepreneurial mindset is becoming:" }
  span: { start: 54373, end: 54418 }
  source: "self-aware of personality and social identity"
  statementType: attribute
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/mindset.b2
  family: mindset
  locator: { heading: "Developing an entrepreneurial mindset is becoming:" }
  span: { start: 54424, end: 54473 }
  source: "motivated to achieve personal ambitions and goals"
  statementType: attribute
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: insight], pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/mindset.b3
  family: mindset
  locator: { heading: "Developing an entrepreneurial mindset is becoming:" }
  span: { start: 54479, end: 54517 }
  source: "self-organised, flexible and resilient"
  statementType: attribute
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: self-management], pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/mindset.b4
  family: mindset
  locator: { heading: "Developing an entrepreneurial mindset is becoming:" }
  span: { start: 54523, end: 54575 }
  source: "curious towards new possibilities for creating value"
  statementType: attribute
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { pathways: [creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/mindset.b5
  family: mindset
  locator: { heading: "Developing an entrepreneurial mindset is becoming:" }
  span: { start: 54581, end: 54647 }
  source: "responsive to problems and opportunities by making new connections"
  statementType: attribute
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/mindset.b6
  family: mindset
  locator: { heading: "Developing an entrepreneurial mindset is becoming:" }
  span: { start: 54653, end: 54712 }
  source: "able to go beyond perceived limitations and achieve results"
  statementType: attribute
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/mindset.b7
  family: mindset
  locator: { heading: "Developing an entrepreneurial mindset is becoming:" }
  span: { start: 54718, end: 54771 }
  source: "tolerant of uncertainty, ambiguity, risk, and failure"
  statementType: attribute
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { criteria: [bristol/generic-2024: decision-making], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/mindset.b8
  family: mindset
  locator: { heading: "Developing an entrepreneurial mindset is becoming:" }
  span: { start: 54777, end: 54870 }
  source: "sensitive to personal values, such as ethical, social, diversity and environmental awareness."
  statementType: attribute
  force: describes
  addressee: student
  employability: bridge
  verbs: []
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.creativity.b1
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Creativity and innovation" }
  span: { start: 64341, end: 64463 }
  source: "generate multiple ideas, concepts, proposals, solutions, or arguments in response to identified problems and opportunities"
  statementType: competency
  force: should
  addressee: graduate
  employability: bridge
  verbs: [generate]
  maps: { framework: [qaa/fheq-2024/annex-d/cognitive/r4/2.1], criteria: [bristol/generic-2024: problem-solving, cardiffmet/generic-2020: analysis], pathways: [creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.creativity.b2
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Creativity and innovation" }
  span: { start: 64469, end: 64576 }
  source: "think speculatively, employing both convergent and divergent approaches to arrive at appropriate solutions."
  statementType: competency
  force: should
  addressee: graduate
  employability: bridge
  verbs: [think, employing, arrive]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.opportunity.b1
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Opportunity recognition, creation and evaluation" }
  span: { start: 65120, end: 65175 }
  source: "identify, analyse and respond to relevant opportunities"
  statementType: competency
  force: should
  addressee: graduate
  employability: direct
  verbs: [identify, analyse, respond]
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [bristol/generic-2024: problem-solving], pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.opportunity.b2
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Opportunity recognition, creation and evaluation" }
  span: { start: 65181, end: 65308 }
  source: "develop and produce multiple solutions to enhance existing provisions, and identify problems, shortfalls and similar challenges"
  statementType: competency
  force: should
  addressee: graduate
  employability: direct
  verbs: [develop, produce, identify]
  maps: { criteria: [bristol/generic-2024: problem-solving], pathways: [creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.opportunity.b3
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Opportunity recognition, creation and evaluation" }
  span: { start: 65314, end: 65407 }
  source: "be flexible and adaptable, seeing alternative perspectives and offering a choice of solutions"
  statementType: attribute
  force: should
  addressee: graduate
  employability: direct
  verbs: [seeing, offering]
  maps: { framework: [qaa/fheq-2024/annex-d/cognitive/r2/3rd], criteria: [bristol/generic-2024: logical-argument-and-evaluation-of-perspectives], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.opportunity.b4
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Opportunity recognition, creation and evaluation" }
  span: { start: 65413, end: 65559 }
  source: "review and evaluate multiple solutions in contexts that anticipate and accommodate change and contain elements of ambiguity, uncertainty and risk."
  statementType: competency
  force: should
  addressee: graduate
  employability: direct
  verbs: [review, evaluate]
  maps: { framework: [qaa/fheq-2024/4.17.b5], criteria: [bristol/generic-2024: problem-solving, cardiffmet/generic-2020: argument], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.decision.b1
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Decision making supported by critical analysis, synthesis and judgement" }
  span: { start: 66506, end: 66561 }
  source: "source and retrieve relevant contextualised information"
  statementType: competency
  force: should
  addressee: graduate
  employability: bridge
  verbs: [source, retrieve]
  maps: { framework: [qaa/fheq-2024/4.15.b5], criteria: [bristol/generic-2024: research, cardiffmet/generic-2020: research], pathways: [finding-and-using-sources, researching-and-research-methods], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.decision.b2
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Decision making supported by critical analysis, synthesis and judgement" }
  span: { start: 66567, end: 66644 }
  source: "evaluate information and formulate arguments, independently and within a team"
  statementType: competency
  force: should
  addressee: graduate
  employability: bridge
  verbs: [evaluate, formulate]
  maps: { framework: [qaa/fheq-2024/4.15.b7], criteria: [bristol/generic-2024: use-of-evidence-and-sources, cardiffmet/generic-2020: argument], pathways: [criticality, academic-writing], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.decision.b3
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Decision making supported by critical analysis, synthesis and judgement" }
  span: { start: 66650, end: 66789 }
  source: "combine analysis with synthesis, intuition and intuitive decision making, drawn from subject expertise and evaluation of critical incidents"
  statementType: competency
  force: should
  addressee: graduate
  employability: bridge
  verbs: [combine]
  maps: { framework: [qaa/fheq-2024/4.17.b5], criteria: [bristol/generic-2024: decision-making], pathways: [criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.decision.b4
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Decision making supported by critical analysis, synthesis and judgement" }
  span: { start: 66795, end: 66859 }
  source: "be resilient and flexible when faced with change or uncertainty."
  statementType: attribute
  force: should
  addressee: graduate
  employability: bridge
  verbs: []
  maps: { framework: [qaa/fheq-2024/4.15.b9.2], criteria: [bristol/generic-2024: decision-making], pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.implementation.b1
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Implementation of ideas through leadership and management" }
  span: { start: 67425, end: 67549 }
  source: "manage resources in response to a problem or need, demonstrating an enthusiasm for enquiry and the motivation to sustain it."
  statementType: competency
  force: should
  addressee: graduate
  employability: direct
  verbs: [manage, demonstrating, sustain]
  maps: { framework: [qaa/fheq-2024/4.17.b6], criteria: [bristol/generic-2024: self-management, bristol/generic-2024: teamwork], pathways: [work-based-and-experiential-learning, researching-and-research-methods], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.reflection.b1
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Action and reflection" }
  span: { start: 68312, end: 68389 }
  source: "critically reflect upon, review and evaluate the solutions they have explored"
  statementType: competency
  force: should
  addressee: graduate
  employability: bridge
  verbs: [reflect, review, evaluate]
  maps: { framework: [qaa/fheq-2024/annex-d/transferable/r5/2.1], criteria: [bristol/generic-2024: insight, cardiffmet/generic-2020: argument], pathways: [reflective-practice, criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.reflection.b2
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Action and reflection" }
  span: { start: 68395, end: 68488 }
  source: "identify personal development needs and other changing factors through the reflective process"
  statementType: competency
  force: should
  addressee: graduate
  employability: bridge
  verbs: [identify]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.reflection.b3
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Action and reflection" }
  span: { start: 68494, end: 68604 }
  source: "evaluate their own learning and respond to identified shortfalls (competencies, attributes and behaviour gaps)"
  statementType: competency
  force: should
  addressee: graduate
  employability: bridge
  verbs: [evaluate, respond]
  maps: { framework: [qaa/fheq-2024/4.15.b5], criteria: [bristol/generic-2024: insight, cardiffmet/generic-2020: argument], pathways: [reflective-practice, understanding-learning-assessment-and-feedback], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.reflection.b4
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Action and reflection" }
  span: { start: 68610, end: 68724 }
  source: "demonstrate resourcefulness in seeking development guidance or mentoring from both external and internal contacts."
  statementType: behaviour
  force: should
  addressee: graduate
  employability: bridge
  verbs: [demonstrate, seeking]
  maps: { criteria: [bristol/generic-2024: insight], pathways: [reflective-practice, starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.communication.b1
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Communication and strategy skills" }
  span: { start: 69596, end: 69637 }
  source: "identify and respond to stakeholder needs"
  statementType: competency
  force: should
  addressee: graduate
  employability: direct
  verbs: [identify, respond]
  maps: { criteria: [bristol/generic-2024: communication], pathways: [presenting, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.communication.b2
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Communication and strategy skills" }
  span: { start: 69643, end: 69720 }
  source: "communicate enthusiasm and passion to ‘sell’ new ideas, concepts or solutions"
  statementType: behaviour
  force: should
  addressee: graduate
  employability: direct
  verbs: [communicate]
  maps: { criteria: [bristol/generic-2024: communication, cardiffmet/generic-2020: presentation], pathways: [presenting], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.communication.b3
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Communication and strategy skills" }
  span: { start: 69726, end: 69890 }
  source: "employ visualisation and flexible planning skills to interact effectively with others, articulate ideas, build trust and present information or outputs to audiences"
  statementType: competency
  force: should
  addressee: graduate
  employability: direct
  verbs: [employ, interact, articulate, build, present]
  maps: { framework: [qaa/fheq-2024/4.15.b8], criteria: [bristol/generic-2024: communication, cardiffmet/generic-2020: presentation], pathways: [presenting], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.communication.b4
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Communication and strategy skills" }
  span: { start: 69896, end: 69978 }
  source: "draw on the views of others to inform the development or enhancement of their work"
  statementType: behaviour
  force: should
  addressee: graduate
  employability: direct
  verbs: [draw, inform]
  maps: { criteria: [bristol/generic-2024: teamwork, bristol/generic-2024: logical-argument-and-evaluation-of-perspectives], pathways: [criticality, understanding-learning-assessment-and-feedback], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.communication.b5
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Communication and strategy skills" }
  span: { start: 69984, end: 70154 }
  source: "provide research and other evidence to suggest how ideas can be taken forward over time, taking changing environments and emerging technologies and concepts into account."
  statementType: competency
  force: should
  addressee: graduate
  employability: direct
  verbs: [provide, suggest, taking]
  maps: { criteria: [bristol/generic-2024: research, cardiffmet/generic-2020: research], pathways: [researching-and-research-methods, finding-and-using-sources], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.digital.b1
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Digital and Data Skills" }
  span: { start: 70876, end: 70954 }
  source: "perceive the importance of digital technologies and the impact on productivity"
  statementType: literacy
  force: should
  addressee: graduate
  employability: direct
  verbs: [perceive]
  maps: { criteria: [bristol/generic-2024: communication], pathways: [ai-and-technology], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.digital.b2
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Digital and Data Skills" }
  span: { start: 70960, end: 71043 }
  source: "understand technological advances and ability for different technologies to connect"
  statementType: literacy
  force: should
  addressee: graduate
  employability: direct
  verbs: [understand]
  maps: { pathways: [ai-and-technology], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/outcome.digital.b3
  family: outcome
  locator: { heading: "Graduate outcomes: graduates should be able to: Digital and Data Skills" }
  span: { start: 71049, end: 71140 }
  source: "explore technological advances in application to venture creation and effective management."
  statementType: literacy
  force: should
  addressee: graduate
  employability: direct
  verbs: [explore]
  maps: { pathways: [ai-and-technology], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.creativity.b1
  family: delivery
  locator: { heading: "Delivery should include opportunities: Creativity and innovation" }
  span: { start: 64629, end: 64646 }
  source: "creative thinking"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.creativity.b2
  family: delivery
  locator: { heading: "Delivery should include opportunities: Creativity and innovation" }
  span: { start: 64652, end: 64669 }
  source: "conceptualisation"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.creativity.b3
  family: delivery
  locator: { heading: "Delivery should include opportunities: Creativity and innovation" }
  span: { start: 64675, end: 64685 }
  source: "innovation"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.creativity.b4
  family: delivery
  locator: { heading: "Delivery should include opportunities: Creativity and innovation" }
  span: { start: 64691, end: 64706 }
  source: "problem solving"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [creativity, criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.creativity.b5
  family: delivery
  locator: { heading: "Delivery should include opportunities: Creativity and innovation" }
  span: { start: 64712, end: 64760 }
  source: "understanding the value of intellectual property"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [referencing], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.creativity.b6
  family: delivery
  locator: { heading: "Delivery should include opportunities: Creativity and innovation" }
  span: { start: 64766, end: 64804 }
  source: "value creation from different markets."
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.opportunity.b1
  family: delivery
  locator: { heading: "Delivery should include opportunities: Opportunity recognition, creation and evaluation" }
  span: { start: 65607, end: 65685 }
  source: "recognise or create multiple opportunities through actively making connections"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.opportunity.b2
  family: delivery
  locator: { heading: "Delivery should include opportunities: Opportunity recognition, creation and evaluation" }
  span: { start: 65691, end: 65770 }
  source: "make connections as a result of problem solving, evaluating and assessing ideas"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.opportunity.b3
  family: delivery
  locator: { heading: "Delivery should include opportunities: Opportunity recognition, creation and evaluation" }
  span: { start: 65776, end: 66080 }
  source: "develop relevant subject expertise and awareness of contemporary issues, both of which should be evidenced in any strategies for recognising opportunity - as Enterprise and Entrepreneurship are led by ideas, it is important for students to develop awareness of how to manage Intellectual Property issues."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [criticality, referencing], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.decision.b1
  family: delivery
  locator: { heading: "Delivery should include opportunities: Decision making supported by critical analysis, synthesis and judgement" }
  span: { start: 66911, end: 66940 }
  source: "research and collect evidence"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [researching-and-research-methods, finding-and-using-sources], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.decision.b2
  family: delivery
  locator: { heading: "Delivery should include opportunities: Decision making supported by critical analysis, synthesis and judgement" }
  span: { start: 66946, end: 66983 }
  source: "critically analyse evidence collected"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.decision.b3
  family: delivery
  locator: { heading: "Delivery should include opportunities: Decision making supported by critical analysis, synthesis and judgement" }
  span: { start: 66989, end: 67033 }
  source: "intuitively make decisions under uncertainty"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.decision.b4
  family: delivery
  locator: { heading: "Delivery should include opportunities: Decision making supported by critical analysis, synthesis and judgement" }
  span: { start: 67039, end: 67077 }
  source: "use judgement to take calculated risks"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.decision.b5
  family: delivery
  locator: { heading: "Delivery should include opportunities: Decision making supported by critical analysis, synthesis and judgement" }
  span: { start: 67083, end: 67127 }
  source: "take the initiative to take or change action"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.decision.b6
  family: delivery
  locator: { heading: "Delivery should include opportunities: Decision making supported by critical analysis, synthesis and judgement" }
  span: { start: 67133, end: 67197 }
  source: "demonstrate financial literacy in the context of their learning."
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.implementation.b1
  family: delivery
  locator: { heading: "Delivery should include opportunities: Implementation of ideas through leadership and management" }
  span: { start: 67598, end: 67644 }
  source: "leadership and team management within projects"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.implementation.b2
  family: delivery
  locator: { heading: "Delivery should include opportunities: Implementation of ideas through leadership and management" }
  span: { start: 67650, end: 67762 }
  source: "productively linking intention, context and process with outcome and dissemination, within management structures"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.implementation.b3
  family: delivery
  locator: { heading: "Delivery should include opportunities: Implementation of ideas through leadership and management" }
  span: { start: 67768, end: 67936 }
  source: "development and maintenance of effective relationships with audiences, clients, markets, users, and consumers, as well as with participants, co-workers, and co-creators"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [presenting, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.implementation.b4
  family: delivery
  locator: { heading: "Delivery should include opportunities: Implementation of ideas through leadership and management" }
  span: { start: 67942, end: 68033 }
  source: "evaluation of resilience and adaptability, using effectiveness in relationships as a gauge."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.reflection.b1
  family: delivery
  locator: { heading: "Delivery should include opportunities: Action and reflection" }
  span: { start: 68773, end: 68837 }
  source: "audits and evaluations before and after entrepreneurial activity"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.reflection.b2
  family: delivery
  locator: { heading: "Delivery should include opportunities: Action and reflection" }
  span: { start: 68843, end: 68884 }
  source: "developing critical reflection techniques"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.reflection.b3
  family: delivery
  locator: { heading: "Delivery should include opportunities: Action and reflection" }
  span: { start: 68890, end: 68948 }
  source: "action planning for self-development with SMART objectives"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [reflective-practice, starting-progressing-and-succeeding], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.reflection.b4
  family: delivery
  locator: { heading: "Delivery should include opportunities: Action and reflection" }
  span: { start: 68954, end: 68972 }
  source: "reviewing networks"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.reflection.b5
  family: delivery
  locator: { heading: "Delivery should include opportunities: Action and reflection" }
  span: { start: 68978, end: 69063 }
  source: "use of iterative, discovery and learning processes that include learning from failure"
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [reflective-practice], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.reflection.b6
  family: delivery
  locator: { heading: "Delivery should include opportunities: Action and reflection" }
  span: { start: 69069, end: 69196 }
  source: "reflection on generating novel and associative solutions in response to perceived problems, rather than just the final outcome."
  statementType: opportunity
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [reflective-practice, creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.communication.b1
  family: delivery
  locator: { heading: "Delivery should include opportunities: Communication and strategy skills" }
  span: { start: 70203, end: 70338 }
  source: "thinking about and visualising the future, scanning the environment, planning, communicating, influencing, directing, and rationalising"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [presenting, creativity], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.communication.b2
  family: delivery
  locator: { heading: "Delivery should include opportunities: Communication and strategy skills" }
  span: { start: 70344, end: 70443 }
  source: "building relationships, building trust, influencing, networking, negotiating and reviewing progress"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [presenting, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.communication.b3
  family: delivery
  locator: { heading: "Delivery should include opportunities: Communication and strategy skills" }
  span: { start: 70449, end: 70555 }
  source: "multiple forms of communication for a range of audiences including stakeholders and new media technologies"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [presenting, ai-and-technology], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.communication.b4
  family: delivery
  locator: { heading: "Delivery should include opportunities: Communication and strategy skills" }
  span: { start: 70561, end: 70650 }
  source: "learning how intellectual property and issues of confidentiality impact on communication."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [referencing], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.digital.b1
  family: delivery
  locator: { heading: "Delivery should include opportunities: Digital and Data Skills" }
  span: { start: 71188, end: 71234 }
  source: "explore digital advances and their application"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [ai-and-technology], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.digital.b2
  family: delivery
  locator: { heading: "Delivery should include opportunities: Digital and Data Skills" }
  span: { start: 71240, end: 71321 }
  source: "critically review the advantages and disadvantages of data-driven decision making"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [ai-and-technology, criticality], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.digital.b3
  family: delivery
  locator: { heading: "Delivery should include opportunities: Digital and Data Skills" }
  span: { start: 71327, end: 71376 }
  source: "engage with industry experts and big data sources"
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [ai-and-technology, work-based-and-experiential-learning], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/delivery.digital.b4
  family: delivery
  locator: { heading: "Delivery should include opportunities: Digital and Data Skills" }
  span: { start: 71382, end: 71476 }
  source: "review innovation, problem solving and resilience in the context of data-driven opportunities."
  statementType: opportunity
  force: should
  addressee: educator
  employability: direct
  verbs: []
  maps: { pathways: [ai-and-technology], basis: inferred }
  audience: both
- id: qaa/enterprise-2018/assessment.b1
  family: assessment
  locator: { heading: "Assessment: what educators should consider" }
  span: { start: 42788, end: 42938 }
  source: "learning ‘about’ entrepreneurship is normally evaluated through analytical texts such as essays and knowledge retention exercises such as examinations"
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [revising-and-exams, academic-writing], basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/assessment.b2
  family: assessment
  locator: { heading: "Assessment: what educators should consider" }
  span: { start: 42944, end: 43050 }
  source: "learning ‘for’ entrepreneurship requires practical activities where students demonstrate their development"
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning], basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/assessment.b3
  family: assessment
  locator: { heading: "Assessment: what educators should consider" }
  span: { start: 43056, end: 43237 }
  source: "learning ‘through’ entrepreneurship is primarily a reflective process, where a student engages in entrepreneurial activities and maps their own learning and (supported) progression."
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [reflective-practice], basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/assessment.b4
  family: assessment
  locator: { heading: "Assessment: what educators should consider" }
  span: { start: 43308, end: 43456 }
  source: "knowledge retention and knowledge harvesting are different - the latter takes the learning journey further, from critical analysis towards synthesis"
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [criticality], basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/assessment.b5
  family: assessment
  locator: { heading: "Assessment: what educators should consider" }
  span: { start: 43462, end: 43690 }
  source: "teamwork is an essential component of employability and entrepreneurship, and peer review can be used to inform assessment, for example, through contribution audits that clarify and support individual team members’ contributions"
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [work-based-and-experiential-learning, understanding-learning-assessment-and-feedback], basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/assessment.b6
  family: assessment
  locator: { heading: "Assessment: what educators should consider" }
  span: { start: 43696, end: 43992 }
  source: "assessment that measures against known outcomes differs from assessment that develops new perceptions and new opportunities, particularly when these are situated in ever changing contexts and environments - this requires process-driven assessment that maps against demonstrated stages of learning"
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [understanding-learning-assessment-and-feedback], basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/assessment.b7
  family: assessment
  locator: { heading: "Assessment: what educators should consider" }
  span: { start: 43998, end: 44134 }
  source: "temporary failure can inform progress and increase resilience - realisation of failure through reflection can inform positive assessment"
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [reflective-practice], basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/assessment.b8
  family: assessment
  locator: { heading: "Assessment: what educators should consider" }
  span: { start: 44140, end: 44433 }
  source: "assessment that utilises start-up ‘pitches’ and business modelling within a scenario or context related to the student’s aspirations are effective - not only in terms of becoming entrepreneurial, but can also provide valuable insights into business operation and potential career opportunities"
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [presenting], basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/assessment.b9
  family: assessment
  locator: { heading: "Assessment: what educators should consider" }
  span: { start: 44998, end: 45191 }
  source: "assessment should relate to evidence provided by the student or learning team, and this requires portfolio styles of collated work that demonstrates progression through reflection and guidance."
  statementType: assessment
  force: should
  addressee: educator
  employability: bridge
  verbs: []
  maps: { pathways: [reflective-practice, understanding-learning-assessment-and-feedback], basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/educator.role.b1
  family: educator
  locator: { heading: "The entrepreneurial educator: role, attributes and tasks" }
  span: { start: 32328, end: 32396 }
  source: "plan and deliver effective Enterprise and Entrepreneurship curricula"
  statementType: educator
  force: describes
  addressee: educator
  employability: bridge
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/educator.role.b2
  family: educator
  locator: { heading: "The entrepreneurial educator: role, attributes and tasks" }
  span: { start: 32402, end: 32483 }
  source: "build collaborative relationships with students, educators and other stakeholders"
  statementType: educator
  force: describes
  addressee: educator
  employability: bridge
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/educator.role.b3
  family: educator
  locator: { heading: "The entrepreneurial educator: role, attributes and tasks" }
  span: { start: 32489, end: 32602 }
  source: "motivate and inspire students to develop enterprising and entrepreneurial behaviours attributes, and competencies"
  statementType: educator
  force: describes
  addressee: educator
  employability: bridge
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/educator.role.b4
  family: educator
  locator: { heading: "The entrepreneurial educator: role, attributes and tasks" }
  span: { start: 32608, end: 32663 }
  source: "reflect on own practice as an entrepreneurial educator."
  statementType: educator
  force: describes
  addressee: educator
  employability: bridge
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/institution.b1
  family: institution
  locator: { heading: "An entrepreneurial institution will:" }
  span: { start: 71813, end: 72015 }
  source: "encourage improved student engagement and entrepreneurial outcomes in the learning process, for example, being able to map them against the enterprise and/or entrepreneurship definitions provided by QAA"
  statementType: institution
  force: will
  addressee: provider
  employability: direct
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/institution.b2
  family: institution
  locator: { heading: "An entrepreneurial institution will:" }
  span: { start: 72021, end: 72153 }
  source: "drive graduate success through intrapreneurship, self-employment and the creation of new businesses and value creation opportunities"
  statementType: institution
  force: will
  addressee: provider
  employability: direct
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/institution.b3
  family: institution
  locator: { heading: "An entrepreneurial institution will:" }
  span: { start: 72159, end: 72319 }
  source: "map and articulate institutional development that responds to policy drivers, economic development and social wellbeing, on regional, national and global levels"
  statementType: institution
  force: will
  addressee: provider
  employability: direct
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/institution.b4
  family: institution
  locator: { heading: "An entrepreneurial institution will:" }
  span: { start: 72325, end: 72646 }
  source: "employ learning evaluation metrics that respond to identified entrepreneurial needs - for example, projects that require change and adaptation can enhance competencies related to flexibility and adaptability, and outcomes that require multiple solutions (that can be compared and contrasted) can enhance creative capacity"
  statementType: institution
  force: will
  addressee: provider
  employability: direct
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
- id: qaa/enterprise-2018/institution.b5
  family: institution
  locator: { heading: "An entrepreneurial institution will:" }
  span: { start: 72652, end: 72950 }
  source: "strengthen links/relationships with businesses, social enterprises, alumni and relevant organisations by inviting entrepreneurs to be guest speakers and/or visiting lecturers. Understanding the distinctive differences between what larger business and smaller business can offer is integral to this."
  statementType: institution
  force: will
  addressee: provider
  employability: direct
  verbs: []
  maps: { basis: inferred }
  audience: practitioner
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. Student versions in the second person, naming no issuer; force kept. -->
```yaml
- statement: qaa/enterprise-2018/principle.1
  forPractitioner: { text: "Every student should be able to take part in enterprise and entrepreneurship, aligned with their own subject.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should have the chance to learn enterprise and entrepreneurship in a way that fits your subject.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/principle.2
  forPractitioner: { text: "Engagement is meant to help students spot and pursue opportunities, aim higher in their careers, be resilient and adapt to change.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "This helps you spot and go after opportunities, aim higher in your career, bounce back and adapt to change.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/aim.enterprise
  forPractitioner: { text: "Enterprise Education aims for graduates aware of, disposed to and able to generate original ideas for identified needs and opportunities and act on them, even in changing, ambiguous circumstances.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Enterprise learning aims to help you come up with original ideas for real needs and put them into action, even when things are uncertain.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/aim.entrepreneurship
  forPractitioner: { text: "Entrepreneurship Education builds on enterprise competencies towards creating or growing ventures, applying them in realistic risk settings with legal, funding and growth issues.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Entrepreneurship learning builds on your enterprise skills so you can start or grow a venture, working with real risks such as law, funding and growth.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/aim.realisation
  forPractitioner: { text: "Ideas are realised through understanding and applying business processes within the legal and ethical limits of the venture.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to turn ideas into reality by using business processes within the law and ethics of your venture.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/aim.respond
  forPractitioner: { text: "Students should identify and respond to opportunities, using ideas, knowledge, skills and confidence to devise interventions for the challenges they meet.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to spot opportunities and respond, using your ideas, knowledge, skills and confidence to tackle the challenges you face.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/vocab.behaviours
  forPractitioner: { text: "The behaviours listed run from initiative and making things happen, through reflection, communication, pivoting and storytelling, to owning responsibility, building networks, working effectively and taking managed risks.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Being enterprising means you take the lead, make things happen, reflect, communicate, change course, tell a story, take responsibility, network and take sensible risks.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/vocab.attributes
  forPractitioner: { text: "The attributes listed are curiosity, an open mind, proactivity, belief in their own ability (self-efficacy), flexibility and adaptability, determination and resilience.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Enterprising qualities include being open-minded, proactive, curious, confident in your ability, flexible, determined and resilient.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/vocab.competencies
  forPractitioner: { text: "Enterprise competencies include intuitive decisions, spotting opportunities, creative problem-solving, innovating, strategic and design thinking, negotiating, communicating, influencing, leading, and financial, business and digital literacy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "As an enterprising person you build skills in making quick decisions, spotting opportunities, solving problems creatively, innovating, planning, negotiating, persuading, leading, and understanding money, business and digital tools.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/goal.enterprise
  forPractitioner: { text: "Enterprise Education develops enquiring, critical, future-oriented thinkers with civic and social awareness; it is assessed by whether students innovate, challenge norms and see new ways forward.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Enterprise learning develops you as a curious, critical thinker looking ahead; you are judged on whether you innovate, question the usual way and find new routes.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/goal.entrepreneurship
  forPractitioner: { text: "Entrepreneurship Education develops graduates who learn autonomously and evaluate themselves in riskier settings with legal, financial and ethical demands; it is assessed by whether they can apply and implement ideas within practical limits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Entrepreneurship learning helps you learn on your own and judge your own progress in riskier settings; you are judged on whether you can make your ideas work in practice.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/goal.value
  forPractitioner: { text: "Delivery should let students express their value propositions within their studies and to external stakeholders, financially, socially or for sustainability, with ethical considerations.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should get to explain the value your ideas create, financial, social or environmental, to people inside and outside your course, including the ethics.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/journey.awareness.1
  forPractitioner: { text: "Awareness: students gain knowledge and understanding of enterprising and entrepreneurial activity.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "First, you learn what enterprise and entrepreneurship involve.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/journey.awareness.2
  forPractitioner: { text: "Students will understand why enterprise matters professionally and what it means for them personally.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will see why enterprise matters at work and what it means for you.", rewrite: full, force: will, status: drafted }
- statement: qaa/enterprise-2018/journey.awareness.3
  forPractitioner: { text: "Students should be encouraged to be critically aware of media stereotypes of entrepreneurs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should learn to question the way the media portray entrepreneurs.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/journey.mindset.0
  forPractitioner: { text: "Mindset: students should develop awareness of their own enterprising capability and the motivation and self-discipline to apply it flexibly in different settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Next, you build awareness of your own enterprising strengths and the drive and discipline to use them in different settings.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/journey.capability.1
  forPractitioner: { text: "Capability: shown when a student designs a product or service for an identified need, or spots an opportunity and plans actions and their chances.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Then you show capability: designing a product or service for a real need, or spotting an opportunity and planning how to act on it.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/journey.capability.2
  forPractitioner: { text: "Practical experience increasingly develops capability, so that students lead and act autonomously, alone or in a group.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With practical experience, you increasingly take the lead and work independently, alone or in a team.", rewrite: full, force: will, status: drafted }
- statement: qaa/enterprise-2018/journey.capability.3
  forPractitioner: { text: "Students are encouraged to see team performance as essential to employed and entrepreneurial work alike.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You learn that working well in a team is essential, whether you are employed or running a venture.", rewrite: full, force: will, status: drafted }
- statement: qaa/enterprise-2018/journey.effectiveness.1
  forPractitioner: { text: "Effectiveness: likely reached towards the end of study, as the student prepares for work, self-employment or further study.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Finally, as you near the end of your course and prepare for work, self-employment or further study, you become effective at enterprise.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/journey.effectiveness.2
  forPractitioner: { text: "Learning becomes increasingly self-directed, pursuing academic and wider career goals.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By then you direct your own learning, towards both academic and career goals.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/mindset.b1
  forPractitioner: { text: "Self-aware of personality and social identity.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know your own personality and social identity.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/mindset.b2
  forPractitioner: { text: "Driven to reach personal ambitions and goals.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are driven to reach your own ambitions and goals.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/mindset.b3
  forPractitioner: { text: "Organised, flexible and resilient.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You organise yourself, stay flexible and bounce back.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/mindset.b4
  forPractitioner: { text: "Curious about new ways of creating value.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are curious about new ways to create value.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/mindset.b5
  forPractitioner: { text: "Responds to problems and opportunities by connecting things in new ways.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You respond to problems and opportunities by connecting ideas in new ways.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/mindset.b6
  forPractitioner: { text: "Gets past perceived limits to achieve results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You push past the limits you think you have and get results.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/mindset.b7
  forPractitioner: { text: "Copes with uncertainty, ambiguity, risk and failure.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can live with uncertainty, risk and failure.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/mindset.b8
  forPractitioner: { text: "Sensitive to values: ethical, social, diversity and environmental.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You are alert to values such as ethics, fairness, diversity and the environment.", rewrite: full, force: describes, status: drafted }
- statement: qaa/enterprise-2018/outcome.creativity.b1
  forPractitioner: { text: "Generates several ideas, proposals, solutions or arguments for identified problems and opportunities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You come up with several ideas, proposals or solutions for a problem or opportunity.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.creativity.b2
  forPractitioner: { text: "Thinks speculatively, narrowing and widening in turn, to reach fitting solutions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You think freely, opening up and narrowing down ideas, to reach a good solution.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.opportunity.b1
  forPractitioner: { text: "Identifies, analyses and responds to relevant opportunities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You spot, analyse and respond to relevant opportunities.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.opportunity.b2
  forPractitioner: { text: "Develops several solutions that improve what exists, and identifies problems and shortfalls.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You produce several ways to improve what exists and point out problems and gaps.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.opportunity.b3
  forPractitioner: { text: "Flexible and adaptable: sees other perspectives and offers a choice of solutions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You stay flexible, see things from other angles and offer a choice of solutions.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.opportunity.b4
  forPractitioner: { text: "Reviews and weighs several solutions in settings that expect change, ambiguity, uncertainty and risk.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You weigh up several solutions where things may change and the outcome is uncertain.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.decision.b1
  forPractitioner: { text: "Finds and retrieves relevant information in context.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You find the information that matters for the situation.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.decision.b2
  forPractitioner: { text: "Weighs information and builds arguments, alone and in a team.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You weigh up information and build arguments, on your own and with others.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.decision.b3
  forPractitioner: { text: "Joins analysis with synthesis and intuition in deciding, drawing on subject expertise and critical incidents.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You combine analysis with instinct when deciding, using what you know of your subject and past events.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.decision.b4
  forPractitioner: { text: "Resilient and flexible under change or uncertainty.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You stay resilient and flexible when things change or are unclear.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.implementation.b1
  forPractitioner: { text: "Manages resources to meet a problem or need, with enthusiasm for enquiry and the drive to keep it up.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You manage resources to meet a need, with a real interest in finding out and the drive to keep going.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.reflection.b1
  forPractitioner: { text: "Reflects critically on, reviews and evaluates the solutions explored.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You reflect critically on the solutions you tried and judge how well they worked.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.reflection.b2
  forPractitioner: { text: "Identifies personal development needs and changing factors through reflection.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Through reflection, you work out what you need to develop and what is changing.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.reflection.b3
  forPractitioner: { text: "Evaluates own learning and acts on gaps in competencies, attributes and behaviour.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You judge your own learning and act on the gaps you find.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.reflection.b4
  forPractitioner: { text: "Seeks development guidance or mentoring resourcefully, from inside and outside the institution.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You look for advice and mentoring, from inside and outside your university.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.communication.b1
  forPractitioner: { text: "Identifies and responds to stakeholders' needs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You find out what the people involved need and respond to it.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.communication.b2
  forPractitioner: { text: "Conveys enthusiasm to \"sell\" new ideas, concepts or solutions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You show enthusiasm to win support for new ideas.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.communication.b3
  forPractitioner: { text: "Uses visualisation and flexible planning to work with others, put ideas across, build trust and present outputs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You use visuals and flexible plans to work with others, explain ideas, build trust and present your work.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.communication.b4
  forPractitioner: { text: "Uses others' views to develop or improve own work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You use other people's views to improve your work.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.communication.b5
  forPractitioner: { text: "Gives research and other evidence for how ideas can develop over time, allowing for changing environments and technologies.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You use research and evidence to show how ideas could develop, allowing for change and new technology.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.digital.b1
  forPractitioner: { text: "Sees the importance of digital technologies and their effect on productivity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You understand how much digital technology matters for getting things done.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.digital.b2
  forPractitioner: { text: "Understands technological advances and how technologies connect.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You understand new technology and how different technologies link up.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/outcome.digital.b3
  forPractitioner: { text: "Explores how new technology applies to starting and managing ventures.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You explore how new technology can help start and run a venture.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.creativity.b1
  forPractitioner: { text: "Opportunities for creative thinking.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to think creatively.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.creativity.b2
  forPractitioner: { text: "Opportunities to conceptualise.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to form and shape concepts.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.creativity.b3
  forPractitioner: { text: "Opportunities to innovate.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to innovate.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.creativity.b4
  forPractitioner: { text: "Opportunities for problem-solving.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to solve problems.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.creativity.b5
  forPractitioner: { text: "Opportunities to understand the value of intellectual property.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You learn why intellectual property is valuable.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.creativity.b6
  forPractitioner: { text: "Opportunities to create value for different markets.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to create value for different markets.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.opportunity.b1
  forPractitioner: { text: "Opportunities to recognise or create several opportunities by making connections.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You practise finding and creating opportunities by connecting things.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.opportunity.b2
  forPractitioner: { text: "Opportunities to make connections through solving problems and weighing ideas.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You practise connecting ideas as you solve problems and weigh them up.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.opportunity.b3
  forPractitioner: { text: "Opportunities to build subject expertise and awareness of current issues, including managing intellectual property.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You build expertise in your subject and awareness of current issues, including who owns ideas.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.decision.b1
  forPractitioner: { text: "Opportunities to research and collect evidence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to research and gather evidence.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.decision.b2
  forPractitioner: { text: "Opportunities to analyse the evidence critically.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You practise analysing the evidence you gather critically.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.decision.b3
  forPractitioner: { text: "Opportunities to decide intuitively under uncertainty.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You practise making decisions by instinct when things are uncertain.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.decision.b4
  forPractitioner: { text: "Opportunities to judge and take calculated risks.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You practise taking calculated risks.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.decision.b5
  forPractitioner: { text: "Opportunities to take the initiative to act or change course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to take the lead in acting or changing course.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.decision.b6
  forPractitioner: { text: "Opportunities to show financial literacy in context.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to show you understand money in your subject.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.implementation.b1
  forPractitioner: { text: "Opportunities for leadership and team management in projects.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to lead and manage teams in projects.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.implementation.b2
  forPractitioner: { text: "Opportunities to link aims, context and process to outcomes and their sharing.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You practise linking what you aim for, how you work and what you produce.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.implementation.b3
  forPractitioner: { text: "Opportunities to build and keep working relationships with audiences, clients, users and collaborators.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You practise building good working relationships with clients, users and co-workers.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.implementation.b4
  forPractitioner: { text: "Opportunities to evaluate resilience and adaptability, judged by how well relationships work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You get chances to judge your own resilience and adaptability through your working relationships.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.reflection.b1
  forPractitioner: { text: "Opportunities for audits and evaluations before and after enterprise activity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You check your skills before and after an enterprise activity.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.reflection.b2
  forPractitioner: { text: "Opportunities to develop critical reflection techniques.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You learn techniques for reflecting critically.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.reflection.b3
  forPractitioner: { text: "Opportunities for self-development action planning with SMART objectives.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You plan your development with clear, measurable goals.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.reflection.b4
  forPractitioner: { text: "Opportunities to review networks.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You review your networks.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.reflection.b5
  forPractitioner: { text: "Opportunities to work iteratively and learn from failure.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You work in cycles and learn from what fails.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.reflection.b6
  forPractitioner: { text: "Opportunities to reflect on how new solutions were generated, not only on the result.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You reflect on how you came up with new solutions, not only on the result.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.communication.b1
  forPractitioner: { text: "Opportunities to envision the future, scan the environment, plan, communicate, influence and direct.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You practise picturing the future, scanning your surroundings, planning and persuading.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.communication.b2
  forPractitioner: { text: "Opportunities to build relationships and trust, influence, network, negotiate and review progress.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You practise building trust, networking, negotiating and reviewing progress.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.communication.b3
  forPractitioner: { text: "Opportunities to communicate in several forms for varied audiences and new media.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You communicate in different forms for different audiences, new media included.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.communication.b4
  forPractitioner: { text: "Opportunities to learn how intellectual property and confidentiality affect communication.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You learn how ownership of ideas and confidentiality affect what you can share.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.digital.b1
  forPractitioner: { text: "Opportunities to explore digital advances and their uses.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You explore new digital tools and how to use them.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.digital.b2
  forPractitioner: { text: "Opportunities to review the pros and cons of data-driven decisions critically.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You weigh up the pros and cons of decisions driven by data.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.digital.b3
  forPractitioner: { text: "Opportunities to work with industry experts and large data sources.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You work with industry experts and large data sets.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/delivery.digital.b4
  forPractitioner: { text: "Opportunities to review innovation, problem-solving and resilience where data drive opportunities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You review innovation and problem-solving where data open up opportunities.", rewrite: full, force: should, status: drafted }
- statement: qaa/enterprise-2018/assessment.b1
  forPractitioner: { text: "Learning \"about\" is usually assessed by analytical writing and recall, such as essays and exams.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/assessment.b2
  forPractitioner: { text: "Learning \"for\" needs practical activities in which students show their development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/assessment.b3
  forPractitioner: { text: "Learning \"through\" is assessed mainly by reflection: students map their own supported progress in real activity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/assessment.b4
  forPractitioner: { text: "Retaining knowledge differs from harvesting it, which moves from critical analysis to synthesis.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/assessment.b5
  forPractitioner: { text: "Teamwork is essential; peer review and contribution audits can inform individual marks.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/assessment.b6
  forPractitioner: { text: "Assessing against known outcomes differs from assessing new perceptions; changing contexts need process-driven assessment mapped to stages of learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/assessment.b7
  forPractitioner: { text: "Temporary failure, realised through reflection, can inform positive assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/assessment.b8
  forPractitioner: { text: "Pitches and business modelling set in the student's own aspirations are effective assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/assessment.b9
  forPractitioner: { text: "Assessment rests on the student's or team's evidence, usually a portfolio showing progress through reflection and guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/educator.role.b1
  forPractitioner: { text: "Plans and delivers effective enterprise curricula.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/educator.role.b2
  forPractitioner: { text: "Builds collaborative relationships with students, colleagues and stakeholders.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/educator.role.b3
  forPractitioner: { text: "Motivates and inspires students to develop enterprising behaviours, attributes and competencies.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/educator.role.b4
  forPractitioner: { text: "Reflects on own practice as an enterprise educator.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: addressed to educators alone"
- statement: qaa/enterprise-2018/institution.b1
  forPractitioner: { text: "Encourages student engagement and entrepreneurial outcomes, mapped against QAA's definitions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/enterprise-2018/institution.b2
  forPractitioner: { text: "Drives graduate success through intrapreneurship, self-employment and new ventures.", rewrite: light, force: will, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/enterprise-2018/institution.b3
  forPractitioner: { text: "Maps its development against policy, economic development and social wellbeing at every scale.", rewrite: light, force: will, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/enterprise-2018/institution.b4
  forPractitioner: { text: "Uses learning metrics fitted to entrepreneurial needs, such as change projects for adaptability and multiple-solution outcomes for creativity.", rewrite: light, force: will, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/enterprise-2018/institution.b5
  forPractitioner: { text: "Strengthens links with businesses, social enterprises, alumni and other organisations, inviting entrepreneurs to teach.", rewrite: light, force: will, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary for the absence of levels; inferred for the alignment -->
The guidance names no FHEQ, FQHEIS or CQFW level. Its outcomes describe a graduate at the end of study and its four stages describe growth across a course. GU2 reads the stages against the frameworks' levels; GU4 lists the framework statements each record most resembles. Neither is the issuer's.

### S6 Themes
`theme:enterprise` (this document is the theme's reference text); `theme:esd` (the definitions tie green and social entrepreneurship to sustainability education and cite QAA and HEA's 2014 ESD guidance, now replaced by std:doc:qaa-advancehe-esd-2021-guidance); employability (defined, kept separate, GU3).

### S7 Relations
```yaml
- { type: themeReference, target: theme:enterprise }
- { type: supersedes, target: "QAA enterprise and entrepreneurship guidance 2012 (not held)" }
- { type: cites, target: "QAA and HEA, Education for Sustainable Development (2014); replaced by std:doc:qaa-advancehe-esd-2021-guidance", basis: primary }
- { type: citedBy, target: "36 of the 54 subject benchmark statements held (GU6)", basis: primary }
- { type: citedBy, target: std:doc:qaa-advancehe-esd-2021-guidance, note: "its employers and enterprise section and resources", basis: primary }
- { type: mapsTo, target: std:doc:qaa-fheq-2024-framework, basis: inferred, note: "20 records linked (GU4)" }
- { type: mapsTo, target: std:doc:bristol-generic-2024-assesscriteria, basis: inferred }
- { type: mapsTo, target: std:doc:cardiffmet-generic-2020-assesscriteria, basis: inferred }
- { type: handsTo, target: "theory ingest (ing): the pedagogy in GU7" }
- { type: relatedTo, target: "ing:doc for Advance HE's PSF 2023 (run 0053): staff standards beside this guidance's educator family", basis: inferred }
```

### S8 Currency and review
<!-- label: both; status: drafted; basis: primary -->
January 2018, replacing the 2012 edition. Whether QAA has revised it since has not been checked (Part E, E1).

### S9 Commentary (optional)
<!-- label: practitioner; status: drafted; basis: inferred -->
The guidance writes in three voices. To students and graduates it says what they will become ("should be able to"); to educators it lists the chances teaching should give; to institutions it lists commitments. Only the first is a standard in the sense the frameworks use. The other two are conditions for meeting it, and we keep them because they say what a student can expect to be offered (student versions in S4a where that holds).

## Part GU Guidance analysis

### GU1 Statement families
<!-- The kinds of standards assertion the guidance makes, by family: who it addresses, its usual force, and how many records. -->

| Family | Heading | Records | Addressee | Force | Student versions |
|---|---|---|---|---|---|
| principle | Principle: every student has the opportunity | 2 | provider, student | describes, should | 2 |
| aim | Aims of Enterprise and of Entrepreneurship Education | 4 | graduate, student | describes, should | 4 |
| vocab | What enterprise behaviours, attributes and competencies can include | 3 | student | describes | 3 |
| goal | Assessment goals for Enterprise and for Entrepreneurship Education | 3 | educator, student | describes, should | 3 |
| journey | The learning journey: awareness, mindset, capability, effectiveness | 9 | educator, student | describes, should, will | 9 |
| mindset | Developing an entrepreneurial mindset is becoming: | 8 | student | describes | 8 |
| outcome | Graduate outcomes: graduates should be able to | 23 | graduate | should | 23 |
| delivery | Delivery should include opportunities | 33 | educator | should | 33 |
| assessment | Assessment: what educators should consider | 9 | educator | should | 0 |
| educator | The entrepreneurial educator: role, attributes and tasks | 4 | educator | describes | 0 |
| institution | An entrepreneurial institution will: | 5 | provider | will | 0 |

### GU2 Progression
<!-- label: both; status: drafted; basis: primary for the stages; inferred for the levels -->
The guidance's progression model has four stages, each named and described, with a teaching mode for each (education about, for and through enterprise; the model itself goes to theory ingest, GU7). It does not tie a stage to a level or a year; it says only that effectiveness comes near the end of study. Read against the frameworks, the stages fall like this:

| Stage | Name | What it means for the student (our gloss) | Level (our reading) | FHEQ descriptors |
|---|---|---|---|---|
| awareness | Enterprise awareness | first year: knowing what enterprise is and why it matters to you | L4 | 4.10 (CertHE) |
| mindset | Entrepreneurial mindset | seeing yourself as enterprising; motivation and resilience | L4 to L5 | 4.10, 4.12 |
| capability | Entrepreneurial capability | doing it: designing, spotting and acting on opportunities in guided projects | L5 to L6 | 4.12, 4.15 |
| effectiveness | Entrepreneurial effectiveness | self-directed, with external clients, at the transition to work, venture or further study | L6 to L7 | 4.15, 4.17 |

**What changes from stage to stage.** Three things move together, and they are the same three the FHEQ's descriptors move: *autonomy* (taught, then guided, then self-directed), *context* (the classroom, then simulations and projects, then live clients and ventures) and *uncertainty* (the outcomes ask graduates to work where change, ambiguity and risk are expected, which is the master's descriptor's "complex and unpredictable situations"). The guidance adds a fourth that the frameworks lack: *identity* (the mindset stage is about seeing yourself as enterprising).

**Suggestion: a levelled outcome ladder.** The 23 outcomes are level-free. To use one as a module learning outcome, keep its object and change its verb and context by stage. Three examples, ours (`suggested`):

| Theme | Awareness (L4) | Capability (L5 to L6) | Effectiveness (L6 to L7) |
|---|---|---|---|
| opportunity | describe how opportunities arise in your subject | identify and analyse an opportunity and plan a response | evaluate competing responses to an opportunity under uncertainty and lead one |
| reflection | describe your own enterprising strengths | review a project you took part in and set development goals | evaluate your own development across a live project and act on the gaps |
| communication | explain an idea to peers | present a proposal to a stakeholder and respond to questions | persuade external stakeholders of an idea's value, financial, social or environmental |

The verbs follow the FHEQ document's verb ladder (std:doc:qaa-fheq-2024-framework, SL3): describe and explain at L4, apply and analyse at L5, evaluate and critically review at L6, lead and act autonomously in unpredictable contexts at L7.


### GU3 Employability
<!-- Each record tagged: `direct` names work, careers, employers or ventures; `bridge` is a capability that study and work share; `academic` stays within study. Our reading. -->

| Tag | Records | Categories |
|---|---|---|
| direct | 43 | opportunity 15, competency 11, institution 5, literacy 4, attribute 2, capability 2, behaviour 2, awareness 1, effectiveness 1 |
| bridge | 59 | opportunity 18, competency 11, attribute 10, assessment 9, educator 4, behaviour 2, principle 1, awareness 1, mindset 1, capability 1, effectiveness 1 |
| academic | 1 | awareness 1 |

**Direct statements:** `principle.2`; `aim.entrepreneurship`; `aim.realisation`; `vocab.competencies`; `goal.entrepreneurship`; `goal.value`; `journey.awareness.2`; `journey.capability.1`; `journey.capability.3`; `journey.effectiveness.1`; `outcome.opportunity.b1`; `outcome.opportunity.b2`; `outcome.opportunity.b3`; `outcome.opportunity.b4`; `outcome.implementation.b1`; `outcome.communication.b1`; `outcome.communication.b2`; `outcome.communication.b3`; `outcome.communication.b4`; `outcome.communication.b5`; `outcome.digital.b1`; `outcome.digital.b2`; `outcome.digital.b3`; `delivery.opportunity.b1`; `delivery.opportunity.b2`; `delivery.opportunity.b3`; `delivery.implementation.b1`; `delivery.implementation.b2`; `delivery.implementation.b3`; `delivery.implementation.b4`; `delivery.communication.b1`; `delivery.communication.b2`; `delivery.communication.b3`; `delivery.communication.b4`; `delivery.digital.b1`; `delivery.digital.b2`; `delivery.digital.b3`; `delivery.digital.b4`; `institution.b1`; `institution.b2`; `institution.b3`; `institution.b4`; `institution.b5`.

**Reading.** The guidance is an employability document that declines the word: it keeps employability (Knight and Yorke's achievements that make employment more likely) separate from enterprise (a way of acting) and entrepreneurship (creating value), and its figure on the three shows them overlapping. In its statements, 43 name work, ventures, markets or stakeholders outright (`direct`) and 59 describe capabilities that hold as well in study as at work (`bridge`): creativity, decision-making, reflection, resilience. Only one stays within study. Direct statements cluster in the opportunity, implementation, communication and digital themes, and in the institution family (intrapreneurship, alumni, business links).

**Suggestions.**
1. Treat the `bridge` statements as the link between academic outcomes and professional competence: each one has an academic face (an assessed criterion, GU4) and a work face (an employer's competency). A module outcome built from a bridge statement can name both.
2. Treat the `direct` statements as the guidance's professional competencies. They are the ones a benchmark's employability paragraph most often echoes (GU6) and the ones a placement, live brief or venture module would assess.
3. In the standards profile, record `employability` on every guidance statement (direct, bridge, academic) and, later, on benchmark statements too, so that a query for "what professional competence does this subject's standard build" can run across documents.


### GU4 Links to framework levels and assessment criteria
<!-- Counts of records linked, our reading (`inferred`). Framework statements are std:doc:qaa-fheq-2024-framework's; criteria are Bristol's (b:) and Cardiff Met's (c:) generic marking criteria. -->

| Framework statement | Records |
|---|---|
| qaa/fheq-2024/4.17.b6 | 3 |
| qaa/fheq-2024/4.15.b7 | 3 |
| qaa/fheq-2024/4.15.b5 | 3 |
| qaa/fheq-2024/4.15.b9.2 | 2 |
| qaa/fheq-2024/4.15.b8 | 2 |
| qaa/fheq-2024/4.17.b5 | 2 |
| qaa/fheq-2024/4.15.b9.1 | 1 |
| qaa/fheq-2024/4.15.b6 | 1 |
| qaa/fheq-2024/annex-d/cognitive/r4/2.1 | 1 |
| qaa/fheq-2024/annex-d/cognitive/r2/3rd | 1 |
| qaa/fheq-2024/annex-d/transferable/r5/2.1 | 1 |

| Assessment criterion | Records |
|---|---|
| Bristol: problem-solving | 11 |
| Bristol: insight | 9 |
| Bristol: decision-making | 6 |
| Bristol: self-management | 6 |
| Bristol: communication | 6 |
| Bristol: teamwork | 5 |
| Cardiff Met: argument | 4 |
| Cardiff Met: analysis | 3 |
| Bristol: logical-argument-and-evaluation-of-perspectives | 2 |
| Bristol: research | 2 |
| Cardiff Met: research | 2 |
| Cardiff Met: presentation | 2 |
| Bristol: use-of-evidence-and-sources | 1 |

**Reading.** Twenty records sit close to an FHEQ statement, almost all at Level 6 (4.15: dealing with complex issues, communicating to specialist and non-specialist audiences, the qualities for employment) or Level 7 (4.17: deciding in complex and unpredictable situations, independent learning, initiative and personal responsibility). The guidance's outcomes are, in effect, the FHEQ's "wider abilities of typical holders" rewritten for enterprise. Against the marking criteria, Bristol's skills criteria (problem-solving, insight, decision-making, self-management, communication, teamwork) take most links, because Bristol writes criteria for practical and professional abilities that Cardiff Met's generic grid folds into argument, analysis, research and presentation.

**Suggestions for assessment.**
1. The guidance's three assessment modes line up with three assessment forms: learning *about* enterprise with essays and examinations (Cardiff Met's argument and analysis rows), learning *for* it with practical tasks and pitches (Bristol's problem-solving and communication rows), learning *through* it with reflective portfolios (Bristol's insight and self-management rows). A module can say which mode it assesses and borrow the matching criterion rows, banded on the UK marking scale (std:doc:bristol-generic-2024-assesscriteria AC3).
2. Two of its considerations need a criterion neither grid has: crediting temporary failure that is reflected on, and judging process where the outcome cannot be known in advance. A guidance-derived criterion row ("learning from setbacks", banded from description of what went wrong at the pass band to evaluated change of approach at 70 and above) would fill that.
3. Teamwork with individual marks (peer review, contribution audits) fits Bristol's teamwork criterion; the guidance's point is that the individual's share be evidenced, not assumed.


### GU5 Academic practice pathways
<!-- Records per pathway (ACPRAC-DAT's thirteen, used loosely as categories), our reading. -->

| Pathway | Records | Families |
|---|---|---|
| reflective-practice | 19 | delivery 6, outcome 4, assessment 3, journey 2, mindset 2, vocab 1, goal 1 |
| researching-and-research-methods | 4 | outcome 3, delivery 1 |
| work-based-and-experiential-learning | 21 | delivery 10, journey 3, aim 2, outcome 2, assessment 2, vocab 1, goal 1 |
| finding-and-using-sources | 3 | outcome 2, delivery 1 |
| criticality | 20 | outcome 8, delivery 5, mindset 2, aim 1, vocab 1, goal 1, journey 1, assessment 1 |
| academic-writing | 2 | outcome 1, assessment 1 |
| referencing | 3 | delivery 3 |
| understanding-learning-assessment-and-feedback | 5 | assessment 3, outcome 2 |
| starting-progressing-and-succeeding | 14 | journey 4, mindset 3, principle 2, outcome 2, delivery 2, vocab 1 |
| presenting | 11 | delivery 4, outcome 3, vocab 2, goal 1, assessment 1 |
| revising-and-exams | 1 | assessment 1 |
| ai-and-technology | 8 | delivery 5, outcome 3 |
| creativity | 18 | delivery 7, outcome 4, aim 2, mindset 2, vocab 1, goal 1, journey 1 |

**Reading.** The guidance spreads across nine of the thirteen pathways but leans on five: work-based and experiential learning, criticality, reflective practice, creativity, and starting, progressing and succeeding. It is the strongest source we hold for the **creativity** pathway (no framework names creativity as a capability; this guidance makes it the first outcome theme) and for **work-based and experiential learning** (live projects, placements, ventures). Reflection runs through every stage and has an outcome theme of its own. Writing, referencing, revision and exams are thin: the guidance links them only through intellectual property (referencing, loosely) and learning "about" assessment (essays and exams).

**Suggestions for pathways.**
1. Creativity: take the creativity and opportunity outcomes as the pathway's first standards statements, with the ladder in GU2 for levels.
2. Reflective practice: the reflection theme gives five outcomes and six delivery opportunities, including before-and-after skills audits and SMART action planning, which a reflective-practice pathway can use as its practice tasks.
3. Starting, progressing and succeeding: the mindset family (self-aware, motivated, resilient, tolerant of ambiguity, reflecting on failure) is a ready description of the dispositions that pathway builds.
4. AI and technology: the digital theme (digital advances, data-driven decisions, connecting technologies) is 2018's view and predates generative AI; use it for the data-literacy strand and look elsewhere for AI.


### GU6 The benchmark web
<!-- label: practitioner; status: drafted; basis: primary for the paragraph and citation counts (a scan of the 54 benchmark texts held in stan); inferred for the reading -->
How this theme reaches the subject benchmark statements. Columns: paragraphs on enterprise or entrepreneurship, on sustainability, and on employability anywhere in the statement; whether it cites this guidance and the ESD guidance by title; and the paragraphs of its benchmark standards (the threshold, typical and excellent statements) that use theme words. References and reading lists excluded. Paragraph numbers are the statement's own.

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


**Reading.** The benchmarks revised from 2019 on carry a short section on each cross-cutting theme (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship): 52 of the 54 held have enterprise paragraphs, and 36 cite this guidance by title. But the theme stays mostly in the context sections: only 12 benchmarks carry enterprise words into their standards, against 37 for sustainability and 23 for employability. Where they do, the strongest is a three-rung ladder in communication, media, film and cultural studies (applying entrepreneurial skills at threshold, at a high level for typical, at an exceptional level for excellent); creative writing, English, housing, librarianship, physics, public policy, agriculture and art and design carry one or two statements each.

So the web has three strands, in falling strength: **cites** (the benchmark names the guidance), **theme paragraph** (the benchmark says what enterprise means in its subject, outside its standards), and **theme in standards** (a benchmark standard asks for enterprise). Only the third binds a subject's threshold. The relations index (wkspc2601-library/ingested/standards/ingest-std-relations-index.md) holds these as edges.

**Suggestion.** When a benchmark is ingested (S-02), tag its theme paragraphs with `theme:enterprise` and link each to the guidance families it echoes (most often the outcome themes); tag its standards that use theme words with the same theme and a `mapsTo` to the outcome. Then a subject's enterprise standard can be read as "this guidance outcome, at this benchmark's level".

### GU7 Pedagogy handed to theory ingest
<!-- label: practitioner; status: drafted; basis: primary -->
Named here, not ingested; for ing to judge as theory items:
- learning about, for and through enterprise (the guidance's three modes, after the wider literature);
- the four-stage model of enterprise learning (awareness, mindset, capability, effectiveness) and its figure;
- the gateway triangle for assessing enterprise and entrepreneurship (the guidance's figure 3);
- EntreComp, the European Commission's entrepreneurship competence framework (three areas: ideas and opportunities, resources, into action);
- Venture Creation Programmes;
- SFEDI's National Occupational Standards for Enterprise Educators (2016), the source of the educator family;
- Knight and Yorke's (2003) definition of employability;
- experiential learning, business simulations and live projects as delivery methods;
- the "optimum strategic employment spot" figure (location, skills gaps, established businesses).

EntreComp and SFEDI's standards are themselves standards documents; if Abbott supplies them they belong in this profile (Part D, D3).

## Part B Terminology
<!-- label: both; status: drafted; basis: primary; paraphrased -->
```yaml
- { term: enterprise, gloss: "Generating ideas and applying them in practical settings during a project or undertaking; generic to all education and work." }
- { term: entrepreneurship, gloss: "Applying enterprise behaviours, attributes and competencies to create cultural, social or economic value, which may but need not mean a new venture; in any sector." }
- { term: entrepreneurial, gloss: "The guidance's word for enterprise and entrepreneurship together." }
- { term: enterprise education, gloss: "Education aimed at graduates able to generate original ideas for needs and opportunities and act on them, in uncertain conditions." }
- { term: entrepreneurship education, gloss: "Education building on enterprise competencies towards creating or growing a venture, in settings with real risk." }
- { term: employability, gloss: "Achievements (skills, understandings, personal attributes) that make employment and success in an occupation more likely (Knight and Yorke, 2003, as quoted)." }
- { term: intrapreneurship, gloss: "Enterprise exercised inside an existing organisation of any size or sector." }
- { term: social entrepreneurship, gloss: "Ventures driven by social or cultural problems rather than profit." }
- { term: green entrepreneurship, gloss: "Ventures aiming at a net benefit to the natural environment by sustainable means." }
- { term: digital entrepreneurship, gloss: "Ventures whose products or services are created, sold and supported online." }
- { term: enterprise behaviours, gloss: "Ways of acting (S4 vocab.behaviours)." }
- { term: enterprise attributes, gloss: "Personal qualities (S4 vocab.attributes)." }
- { term: enterprise competencies, gloss: "Capabilities that combine knowledge and skill (S4 vocab.competencies)." }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->
None: the guidance sets no process that providers must follow.

## Part D Sources

### D1 Held text
The PDF Abbott supplied (36 pages, sha256-bytes c11bde81…), converted with pdftotext and normalised (normalise.js 1.0); the PDF is not held in UNI. The figures' text survives only as fragments and is not cut into statements.

### D2 Research log
- 2026-10-03 05:40 to 05:52, std: read direct; 103 statements in eleven families; benchmark scan over the 54 held texts.

### D3 Wanted sources
- W-std-0013: EntreComp (Bacigalupo and others, 2016), the competence framework the guidance cites: a standards document for this profile.
- W-std-0014: SFEDI, National Occupational Standards for Enterprise Educators (2016): staff standards behind the educator family.
- W-std-0015: QAA's 2012 edition, for the change record.
- W-std-0016: Any QAA revision after 2018.

## Part E Gaps and questions
- E1 Currency: not checked against QAA's site.
- E2 The educator and institution families are standards for staff and providers, not students. Kept (Abbott's scope is what a student should be able to do "in some form"; these say what students can expect), with no student version where the statement says nothing a student can use.
- E3 The level reading (GU2) and every map (GU4, GU5, GU6) are ours.

---

## Change notes
- 0.2.1, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.2.0, 3 October 2026, 11:00: every statement record now carries the issuer's statement in full (`source`, taken from its span in the held text) beside our paraphrase and versions, for language analysis; private, never published (Abbott, 10:56 and 10:59; D-std-0014). No paraphrase changed.
- 0.1.2, 3 October 2026, 07:34: provenance lines added to Parts B and C; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.1.1, 3 October 2026, 06:59: S7 records that the full ESD guidance 2021 (run 0063) cites this guidance.
- 0.1.0, 3 October 2026, 05:52: first build, run 0056 (std; Abbott, 05:40).

