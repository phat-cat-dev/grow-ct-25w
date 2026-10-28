---
id: std:doc:advancehe-enterprise-entrepreneurship-2024-model
title: "Framework for enterprise and entrepreneurship"
profile: standards/model
profileVersion: none yet   # the variant's profile part is to write
issuer: Advance HE
kind: model
modelKind: condition-model
series: advancehe-student-success-frameworks-2024
axes: { perspectives: 3, facets: 0, groups: 0, segments: 19, openSegments: 0, labelsNotInText: 0 }
jurisdiction: [UK]   # not stated; Advance HE is UK-based and its frameworks are used internationally (inferred)
subjectScope: universal
subjects: []
edition: "digital edition, 2024"
published: 2024   # no date printed; from the PDF metadata (Part E)
revised: "none-stated"   # a later file date, if any (Part E)
status: current   # as at the held text; not checked against Advance HE's site (D3)
supersedes: "none-stated"
heldText: { method: sha256-bytes, raw: 2e9f1d0a8c186ab5debd1e7a5d1708bc6fadf00577ae723d9138baae2ead99ca, normalised: d3efdba94d554b0aa9397c550619fe71c0458f692a9d8dab3cbfd625773063de }
original: { method: sha256-bytes, pdf: 7682a34d025f7b7f105691b207f11b8e085b1bee01e34ba8224d1c191f638403, held: "library pdf/advance-he-2024-framework-enterprise-entrepreneurship-standard.pdf" }
licence: "no licence or copyright notice printed; © Advance HE assumed. Held by Abbott's permission (4 October 2026, 05:03; D-std-0019)"
agentUse: source-and-rephrased   # `label` and `source` are the issuer's words for language analysis; private, never published (D-std-0014); agents phrase from our fields
parts:
  S: full
  M: full
  B: full
  C: "not-applicable: the model sets conditions, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, model: 0.3.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; model template 0.3.0-draft; std (Claude Code, META Project); builder model_build.py 0.2.1
passes:
  P1: "2026-10-04, std"
  P2: "skipped: read direct from the issuer's PDF; the series page is wanted (D3)"
  P3: open
version: 0.1.1
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards-model.md 0.3.0-draft on wpk-0016-ingest-pd-template-standards.md 0.8.0-draft; built by model_build.py 0.2.1 from run-src/model_content.py -->
# Framework for enterprise and entrepreneurship

> The issuer's text is held beside this document in the library (`txt/advance-he-2024-framework-enterprise-entrepreneurship-standard.norm.txt`). Each M2 `label` (where the text layer holds it), each `explainedBy` and M4 `source` and each S4 `source` is exactly its span's text, held for language analysis (D-std-0014); private, never published. Every other field is ours, and agents phrase from ours.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
A practice model from Advance HE's Student Success Frameworks: nineteen components of enterprise and entrepreneurship education, seen from the institution, educators and students, each held here as a practice theme that can qualify the context of a lesson or a piece of material. Reach for it to set or check the conditions for enterprise learning and the capabilities students build. It sets no levels and no outcomes: pair it with QAA's 2018 enterprise guidance for what students achieve.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Advance HE (2024) sets out how enterprise and entrepreneurship education adds value to a learner's journey, whether the learner goes on to found a venture or to act enterprisingly in someone else's organisation. It keeps enterprise and entrepreneurship distinct, quoting QAA's 2018 definitions, and places both beside employability as the 3Es. Three dials carry six institutional, five staff and eight student segments; none is left blank. Short framing lines and a list of uses for each perspective direct the reader, and staff are said to need four capabilities. It names eight PSF 2023 dimensions and invites its use as Fellowship evidence. It binds no one: it is an enhancement model, not an assurance standard.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: Advance HE
title: "Framework for enterprise and entrepreneurship"
series: "Advance HE Student Success Frameworks"
edition: "digital edition, 2024"
dates:
  published: 2024   # not printed; PDF metadata
  other: ["PDF created 26 March 2024", "PDF modified 28 April 2025"]
kind: model
jurisdiction: [UK]
authority: advisory
licence: "none stated in the file (D1)"
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the conditions for enterprise and entrepreneurship education across an institution, its teaching and its students' learning journey (D1, pp. 2-4)"
appliesTo:
  awards: [none-stated]
  levels: [none]
  providers: ["higher education institutions (as stated: \"the institution\")"]
whoMustUse: "no one must; designed for educators who teach enterprise and entrepreneurship in or beyond the curriculum, and of use to senior managers with responsibility for enterprise, employability and external engagement and to staff supporting businesses and social enterprises (D1, p. 3)"
howUsed: ["design", "review", "other: staff development, evaluation of impact, Fellowship evidence"]
doesNot: "none-stated"
beneficiary: the student
statedScope: "This framework is designed to inform and support the activities of educators who interact with students through the delivery of enterprise and entrepreneurship within the curriculum and/or extracurricular activity."
statedScopeLocator: "D1, p. 3"
statedScopeSpan: { start: 600, end: 814 }
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "what-is", order: 1, componentType: section, parent: "none", heading: "What is enterprise and entrepreneurship education?", gloss: "the distinction between enterprise and entrepreneurship; the 3Es; QAA 2018 definitions quoted", pages: "2", readFrom: "text layer" }
  - { number: "who-for", order: 2, componentType: section, parent: "none", heading: "Who is the framework for?", gloss: "audiences: educators in and beyond the curriculum, senior managers, staff supporting businesses and social enterprises", pages: "2-3", readFrom: "text layer" }
  - { number: "why", order: 3, componentType: section, parent: "none", heading: "Why is the framework important?", gloss: "rationale: value to the learner's journey, employability, graduates joining small firms", pages: "4", readFrom: "text layer" }
  - { number: "structure", order: 4, componentType: figure, parent: "none", heading: "How is the framework structured?", gloss: "the three perspectives shared by the series", pages: "5", readFrom: "figure image" }
  - { number: "institution", order: 5, componentType: perspective, parent: "none", heading: "Institution", gloss: "framing line and six key elements of the institutional environment", pages: "6", readFrom: "text layer" }
  - { number: "institution.dial", order: 6, componentType: figure, parent: "institution", heading: "(dial)", gloss: "six segments", pages: "7", readFrom: "figure image" }
  - { number: "educators", order: 7, componentType: perspective, parent: "none", heading: "Educators+", gloss: "framing prose for educators and the lead-in to four capabilities", pages: "8", readFrom: "text layer" }
  - { number: "through", order: 8, componentType: stem, parent: "educators", heading: "As recognised within national professional standards, educators need to be able to deliver ... through:", gloss: "the lead-in to the four capabilities", pages: "8", readFrom: "text layer" }
  - { number: "educators.dial", order: 9, componentType: figure, parent: "educators", heading: "(dial)", gloss: "five segments", pages: "9", readFrom: "figure image" }
  - { number: "students", order: 10, componentType: perspective, parent: "none", heading: "Students", gloss: "the learner journey: four stages; learning about, for and through", pages: "10", readFrom: "text layer" }
  - { number: "students.dial", order: 11, componentType: figure, parent: "students", heading: "(dial)", gloss: "eight segments", pages: "11", readFrom: "figure image" }
  - { number: "use", order: 12, componentType: use-list, parent: "none", heading: "How can you use the framework?", gloss: "purpose and three uses for each perspective", pages: "12-13", readFrom: "figure image" }
  - { number: "psf", order: 13, componentType: section, parent: "none", heading: "How does this framework align with the Professional Standards Framework (PSF) 2023?", gloss: "the PSF crosswalk table (eight dimensions) and the Fellowship invitation", pages: "14", readFrom: "text layer" }
excluded:
  - { number: "back-cover", heading: "We help higher education organisations be the best they can be ...", kind: "other: the issuer's back cover (promotion, acknowledgements, partners)", pages: "back cover, unnumbered" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only obliging framing lines, requirement lists and use lists are statements (model template rule 3). -->
```yaml
- id: advancehe/enterprise-2024/frame.three-es
  locator: { number: "frame.three-es", heading: "What is enterprise and entrepreneurship education?", page: 2 }
  span: { start: 1631, end: 1776 }
  source: "It is also important to recognise both these terms alongside employability, creating the ‘3Es’ of employability, enterprise and entrepreneurship."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # "it is important to" read as should: not in D-std-0016's list; proposed (Part E)
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["recognise", "creating"]
  about: "enterprise and entrepreneurship beside employability"
  themes: ["none"]
  paraphrase: "Enterprise and entrepreneurship should be recognised alongside employability, the three together forming the 3Es."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/frame.institution
  locator: { number: "frame.institution", heading: "Institution", page: 6 }
  span: { start: 4220, end: 4421 }
  source: "It is important to have the elements of an institutional environment that support enterprise and entrepreneurship educators to deliver an effective experience and responds to the needs of all learners."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # "it is important to" read as should: not in D-std-0016's list; proposed (Part E)
  level: none
  perspective: perspective:institution
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["have", "support", "deliver", "responds"]
  about: "an institutional environment that supports enterprise teaching"
  themes: ["none"]
  paraphrase: "Institutions should provide an environment that supports staff teaching enterprise and entrepreneurship and meets the needs of every learner."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/through.b1
  locator: { number: "through.b1", heading: "Educators+", page: 8 }
  span: { start: 5745, end: 5857 }
  source: "motivating and inspiring learners in developing enterprising and entrepreneurial mindsets, behaviours and skills"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: through
  statementType: requirement
  force: must   # D-std-0016: "need to" (lead-in) read as must
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["motivating", "inspiring", "developing"]
  about: "motivating learners towards an enterprising outlook"
  themes: ["none"]
  paraphrase: "Staff must be able to motivate and inspire learners to develop enterprising ways of thinking, behaving and working."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/through.b2
  locator: { number: "through.b2", heading: "Educators+", page: 8 }
  span: { start: 5862, end: 5941 }
  source: "designing, developing and delivering enterprise and entrepreneurship curriculum"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: through
  statementType: requirement
  force: must   # D-std-0016: "need to" (lead-in) read as must
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["designing", "developing", "delivering"]
  about: "designing and teaching the curriculum"
  themes: ["none"]
  paraphrase: "Staff must be able to design, develop and teach enterprise and entrepreneurship curriculum."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/through.b3
  locator: { number: "through.b3", heading: "Educators+", page: 8 }
  span: { start: 5946, end: 6038 }
  source: "building collaborative relationships with others both within and external to the institution"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: through
  statementType: requirement
  force: must   # D-std-0016: "need to" (lead-in) read as must
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["building"]
  about: "working with others inside and outside"
  themes: ["none"]
  paraphrase: "Staff must be able to build working relationships with others inside and outside the institution."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/through.b4
  locator: { number: "through.b4", heading: "Educators+", page: 8 }
  span: { start: 6043, end: 6189 }
  source: "reflecting on your own practice as an enterprise and entrepreneurship educator in order to identify what you do well and what you could do better."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: through
  statementType: requirement
  force: must   # D-std-0016: "need to" (lead-in) read as must
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["reflecting", "identify", "do"]
  about: "reviewing one's own teaching"
  themes: ["none"]
  paraphrase: "Staff must be able to review their own enterprise teaching to find its strengths and what to improve."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/frame.students
  locator: { number: "frame.students", heading: "Students", page: 10 }
  span: { start: 7451, end: 7697 }
  source: "In addition, different approaches to teaching and learning are required at each stage of the journey, particularly in terms of the focus on understanding, skills and experience and progressive ownership of the education experience by the learner."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "required" read as must
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["required"]
  about: "different teaching for each stage of the journey"
  themes: ["none"]
  paraphrase: "Each stage of the learner's journey needs its own approach to teaching, shifting the focus across understanding, skills and experience and handing the learner more ownership."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/use.institution.1
  locator: { number: "use.institution.1", heading: "How can you use the framework?", page: 12 }
  span: { start: 9147, end: 9258 }
  source: "Reflecting on the impact of what you do with others, including learners, other staff and external stakeholders."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names a use of the model; does not oblige
  level: none
  perspective: perspective:institution
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["Reflecting", "do"]
  about: "reviewing impact with others"
  themes: ["none"]
  paraphrase: "The model helps the institution review the effect of its work with learners, staff and outside partners."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/use.institution.2
  locator: { number: "use.institution.2", heading: "How can you use the framework?", page: 12 }
  span: { start: 9273, end: 9476 }
  source: "Identifying the key ways associated with the design, delivery and documenting of different approaches to enterprise and entrepreneurship education, both in the curriculum and as extracurricular activity."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names a use of the model; does not oblige
  level: none
  perspective: perspective:institution
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["Identifying", "associated"]
  about: "ways to design, deliver and record provision"
  themes: ["none"]
  paraphrase: "The model helps the institution identify how to design, deliver and record its approaches, in and beyond the curriculum."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/use.institution.3
  locator: { number: "use.institution.3", heading: "How can you use the framework?", page: 12 }
  span: { start: 9477, end: 9587 }
  source: "Identifying how to create learning environments and resources that add value to the experience of the learner."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names a use of the model; does not oblige
  level: none
  perspective: perspective:institution
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["Identifying", "create", "add"]
  about: "environments and resources that help learners"
  themes: ["none"]
  paraphrase: "The model helps the institution work out how to create settings and resources that improve the learner's experience."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/use.educators.1
  locator: { number: "use.educators.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 8853, end: 8980 }
  source: "Recognising the value of engagement with external stakeholders in the co-creation of enterprise and entrepreneurship education."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names a use of the model; does not oblige
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["Recognising"]
  about: "co-creating with outside partners"
  themes: ["none"]
  paraphrase: "The model helps staff see the value of creating enterprise learning together with outside partners."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/use.educators.2
  locator: { number: "use.educators.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 9593, end: 9743 }
  source: "Identifying the difference between enterprise and entrepreneurship education and supporting the development of a shared language in this area of work."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names a use of the model; does not oblige
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["Identifying", "supporting"]
  about: "telling the terms apart and sharing a vocabulary"
  themes: ["none"]
  paraphrase: "The model helps staff tell enterprise education from entrepreneurship education and build a common vocabulary."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/use.educators.3
  locator: { number: "use.educators.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 8994, end: 9145 }
  source: "Providing a resource to reflect on professional development needs and requirements, acting as a benchmark to reflect on current practice and provision."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names a use of the model; does not oblige
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: provider
  verbs: ["Providing", "reflect", "acting"]
  about: "a reference point for professional development"
  themes: ["none"]
  paraphrase: "The model gives staff a reference point for reviewing their development needs and their current practice."
  audience: practitioner
  subjects: inherited
- id: advancehe/enterprise-2024/use.students.1
  locator: { number: "use.students.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 9745, end: 9812 }
  source: "Understanding what it means to be enterprising and entrepreneurial."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names a use of the model; does not oblige
  level: none
  perspective: perspective:students
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: learner
  verbs: ["Understanding", "means", "be"]
  about: "knowing what being enterprising involves"
  themes: ["none"]
  paraphrase: "The model helps students understand what being enterprising and entrepreneurial involves."
  audience: both
  subjects: inherited
- id: advancehe/enterprise-2024/use.students.2
  locator: { number: "use.students.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 9824, end: 9943 }
  source: "Identify and understanding how they can add value in different contexts through being enterprising and entrepreneurial."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund ("understanding") with an imperative "Identify" joined to it; read as naming a use; does not oblige (Part E)
  level: none
  perspective: perspective:students
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: learner
  verbs: ["Identify", "understanding", "add", "being"]
  about: "seeing how one can add value in different settings"
  themes: ["none"]
  paraphrase: "The model helps students see how they can add value in different settings by being enterprising."
  audience: both
  subjects: inherited
- id: advancehe/enterprise-2024/use.students.3
  locator: { number: "use.students.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 9944, end: 10031 }
  source: "Encouraging reciprocal and collaborative ways of working within and across disciplines."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names a use of the model; does not oblige
  level: none
  perspective: perspective:students
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for enterprise and entrepreneurship"
  addressee: both
  verbs: ["Encouraging", "working"]
  about: "collaboration within and across subjects"
  themes: ["none"]
  paraphrase: "The model encourages students to work together, giving and gaining, within and across subjects."
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- statement: advancehe/enterprise-2024/frame.three-es
  forPractitioner: { text: "Treat enterprise and entrepreneurship as linked to employability, and plan them together rather than as separate agendas.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a framing for staff and institutions on how to group the terms", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as the issuer's framing of the 3Es, force should (our reading of \"it is important to\"). The definitions that follow it are quoted from QAA 2018, not the issuer's own; attribute them to QAA."
  author-agent-dialogue: "Raise it when enterprise is discussed as unrelated to careers. Ask: \"How does this connect to students' employability?\" Avoid collapsing the three terms into one."
- statement: advancehe/enterprise-2024/frame.institution
  forPractitioner: { text: "Put in place the environment staff need to teach enterprise well, and check that it serves every learner, not only those already inclined to it.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present as the framing expectation of the institution perspective, force should (our reading). The six \"key elements\" listed after it are explanations of the dial, not separate statements (Part E)."
  author-agent-dialogue: "Raise it when staff lack support to teach enterprise. Ask: \"What in the institution would need to change for this to work?\" Avoid detail the institution has not stated."
- statement: advancehe/enterprise-2024/through.b1
  forPractitioner: { text: "Be able to motivate and inspire students to build an enterprising outlook as well as skills; this is one of the means the issuer requires.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a capability required of staff", rewrite: full, force: must, status: drafted }
  author-agent-written: "State as one of four means through which staff must be able to teach enterprise well; must force comes from \"need to\" in the lead-in, which the issuer ties to national professional standards. Link to the motivational leadership component."
  author-agent-dialogue: "Raise it in staff development. Ask: \"How do you help students see enterprise as open to them?\" Avoid treating inspiration as a personality trait."
- statement: advancehe/enterprise-2024/through.b2
  forPractitioner: { text: "Be able to design, build and teach enterprise and entrepreneurship learning; the lead-in makes this a requirement.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a capability required of staff", rewrite: full, force: must, status: drafted }
  author-agent-written: "Must force from the lead-in. Link to the planning and delivery component."
  author-agent-dialogue: "Raise it in curriculum design. Ask: \"Who designs the enterprise learning here, and with what support?\""
- statement: advancehe/enterprise-2024/through.b3
  forPractitioner: { text: "Build working relationships with colleagues and outside partners as part of teaching enterprise; the lead-in makes this required.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a capability required of staff", rewrite: full, force: must, status: drafted }
  author-agent-written: "Must force from the lead-in. Link to the building collaborative relationships component."
  author-agent-dialogue: "Raise it when a teacher works in isolation. Ask: \"Who could you partner with on this?\""
- statement: advancehe/enterprise-2024/through.b4
  forPractitioner: { text: "Review your own enterprise teaching to find what works and what to improve; the lead-in makes this required.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a capability required of staff", rewrite: full, force: must, status: drafted }
  author-agent-written: "Must force from the lead-in. Note the shift to second person (\"your own practice\") inside a list about educators. Link to the reflecting on own practice component."
  author-agent-dialogue: "Raise it in appraisal or review. Ask: \"What do you do well, and what would you change?\""
- statement: advancehe/enterprise-2024/frame.students
  forPractitioner: { text: "Match teaching to the stage the learner has reached, and hand over more ownership of the learning as they progress.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to those who design teaching", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present as the one obliging line in the students section, must force from \"required\". Link it to the three approaches (about, for, through) the source names next. Do not imply learners move through the stages in a fixed order; the source says they may enter and leave at different points."
  author-agent-dialogue: "Raise it when one method is used for every group. Ask: \"Where are these learners in their journey, and does the method fit?\" Avoid labelling learners by stage without asking them."
- statement: advancehe/enterprise-2024/use.institution.1
  forPractitioner: { text: "Use the model to review what your enterprise work achieves with learners, colleagues and outside partners.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use for the institution", rewrite: full, force: describes, status: drafted }
  author-agent-written: "One of three uses printed beside the Institution roundel (p. 12, read from the image; the text layer places it elsewhere). It describes a use; it does not oblige. Link to define and measure impact."
  author-agent-dialogue: "Raise it in institutional review. Ask: \"What has your enterprise work changed for learners and partners?\""
- statement: advancehe/enterprise-2024/use.institution.2
  forPractitioner: { text: "Use the model to set out how enterprise learning is designed, delivered and recorded, in the curriculum and outside it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use for the institution", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describes a use; does not oblige. Note \"documenting\": the institution keeps a record of its approaches. Link to understand what others do."
  author-agent-dialogue: "Raise it in planning. Ask: \"Where is your enterprise provision recorded, in and out of the curriculum?\""
- statement: advancehe/enterprise-2024/use.institution.3
  forPractitioner: { text: "Use the model to decide which learning spaces and resources would add most to students' enterprise experience.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use for the institution", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describes a use; does not oblige. Link to prioritise action."
  author-agent-dialogue: "Raise it in resource planning. Ask: \"What space or resource would most help students act on ideas?\""
- statement: advancehe/enterprise-2024/use.educators.1
  forPractitioner: { text: "Use the model to plan how outside partners can help create the learning, not only appear in it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use for staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describes a use; does not oblige. Printed beside the Educators+ roundel (p. 13, read from the image). Link to engage with external stakeholders and building collaborative relationships."
  author-agent-dialogue: "Raise it when partners are only guest speakers. Ask: \"How could a partner help shape this from the start?\""
- statement: advancehe/enterprise-2024/use.educators.2
  forPractitioner: { text: "Use the model to keep enterprise and entrepreneurship education distinct and to agree a common vocabulary with colleagues.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use for staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describes a use; does not oblige. Link to apply definitions."
  author-agent-dialogue: "Raise it when terms are confused. Ask: \"Are you teaching enterprise, entrepreneurship, or both?\""
- statement: advancehe/enterprise-2024/use.educators.3
  forPractitioner: { text: "Use the dial as a reference point to review your development needs and your current teaching.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use for staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describes a use (the model as a reference point); does not oblige. Link to reflecting on own practice and to the PSF alignment."
  author-agent-dialogue: "Raise it in development planning. Ask: \"Which segment of the dial would you most like to develop?\""
- statement: advancehe/enterprise-2024/use.students.1
  forPractitioner: { text: "Use the model with students to explore what being enterprising and entrepreneurial involves for them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can use it to work out what being enterprising, and starting ventures, could mean for you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describes a use for students; does not oblige. Link to the students' dial as a whole."
  author-agent-dialogue: "Raise it with students new to the idea. Ask: \"What do you think being enterprising looks like in your subject?\""
- statement: advancehe/enterprise-2024/use.students.2
  forPractitioner: { text: "Use the model to help students see where their enterprising skills add value, in work for others as well as in their own ventures.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can use it to see how being enterprising lets you add value in different settings, including when working for others.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describes a use; does not oblige. The issuer's grammar mixes \"Identify\" with \"understanding\"; recorded as given. Link to starting and developing a business, which sets venture creation beside working for others."
  author-agent-dialogue: "Raise it when a student thinks enterprise is only for founders. Ask: \"Where could you add value in a job or a community group?\""
- statement: advancehe/enterprise-2024/use.students.3
  forPractitioner: { text: "Use the model to set up collaborative work between students within and across subjects.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You are encouraged to work with others, in your own subject and beyond it, so that everyone gains.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describes a use; does not oblige. Link to interpersonal skills."
  author-agent-dialogue: "Raise it when a student works only within their subject. Ask: \"Who in another subject could you work with on this?\""
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels: []   # the model defines and cites no level
crosswalks: []   # its stated link to the PSF 2023, if any, is in M5
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary. Sector themes; the practice themes are in M6. -->
```yaml
- { id: theme:enterprise, role: carries, carriedIn: ["what-is", "who-for", "why", "institution", "educators", "students", "use"], basis: "stated: enterprise and entrepreneurship education is the model's subject" }
- { id: theme:employability, role: carries, carriedIn: ["what-is", "why", "use"], basis: "stated: the 3Es of employability, enterprise and entrepreneurship (D1, p. 2); enhancing employability (D1, p. 4)" }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: partOf, target: "advancehe-student-success-frameworks-2024", note: "Advance HE Student Success Frameworks; the three-perspective structure is shared by the series (D1, p. 5)" }
- { rel: partOf, target: "std:doc:advancehe-enhancing-student-success-2024-model", note: "the series overview names enterprise and entrepreneurship education as one of its areas" }
- { rel: alignsWith, target: "std:doc:advancehe-psf-dimensions-2023-framework", note: "stated: eight PSF 2023 dimensions named (M5)" }
- { rel: refersTo, target: "std:doc:qaa-enterprise-2018-guidance", note: "stated: quotes QAA 2018 (p. 7) for its definitions and draws the student journey from its model of entrepreneurial effectiveness (D1, pp. 2, 10)" }
- { rel: siblingOf, target: "std:doc:advancehe-embedding-employability-2024-model", note: "stated on the back cover: this model complements the employability model; reserved id, not yet ingested under this variant" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: 2024
lastReviewed: none-stated
reviewCycle: none-stated
consultation: none-stated
replacedBy: none
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched (Part E).

## Part M Model

### M1 Model shape
<!-- label: source; status: drafted; basis: primary -->
```yaml
figure: { form: dial, pages: [7, 9, 11], readFrom: "figure image" }
axes:
  - { id: perspective:institution, label: "Institution", page: 7, segments: 6, openSegments: 0 }
  - { id: perspective:educators, label: "Educators+", page: 9, segments: 5, openSegments: 0, note: "labelled \"Educators+\" in the structure figure (p. 5), the section heading (p. 8) and the use list (p. 13)" }
  - { id: perspective:students, label: "Students", page: 11, segments: 8, openSegments: 0 }
groups: none
use: "to connect the learner's journey to the educator's role and to the institution's environment, and to find points of intervention, guide implementation and evaluate impact; three uses are given for each perspective (S4 use.*) (D1, pp. 4, 12-13)"
```

### M2 Components
<!-- label: both; status: drafted; basis: primary. In the figure's order (Part E). -->
```yaml
- id: advancehe/enterprise-2024/institution.apply-definitions
  label: "Apply Definitions"
  span: { start: 5158, end: 5175 }
  position: { axis: perspective:institution, group: none, order: 1, page: 7 }
  explainedBy:
    - { span: { start: 4637, end: 4709 }, source: "identifying and applying a definition of enterprise and entrepreneurship", link: stated, page: 6 }
    - { span: { start: 1318, end: 1446 }, source: "Clarity of the definitions supports educators, institutions, students and external stakeholders through a clear shared language.", link: inferred, page: 2 }
  conditionType: structure
  actor: institution
  about: "an agreed definition put to use"
  paraphrase: "The institution settles on what it means by enterprise and by entrepreneurship, and uses those meanings consistently across its work."
  themes: ["theme:shared-language", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/institution.understand-what-others-do
  label: "Understand What Others Do"
  span: { start: 5177, end: 5202 }
  position: { axis: perspective:institution, group: none, order: 2, page: 7 }
  explainedBy:
    - { span: { start: 4714, end: 4776 }, source: "mapping and reviewing activities undertaken in the institution", link: inferred, page: 6 }
  conditionType: process
  actor: institution
  about: "knowing the activity already under way"
  paraphrase: "The institution finds out what enterprise and entrepreneurship activity already happens, in its own departments and elsewhere, before deciding what to do."
  themes: ["theme:evidence-informed-enhancement", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/institution.prioritise-action
  label: "Prioritise Action"
  span: { start: 5204, end: 5221 }
  position: { axis: perspective:institution, group: none, order: 3, page: 7 }
  explainedBy:
    - { span: { start: 4781, end: 4825 }, source: "prioritising the activities to be undertaken", link: stated, page: 6 }
    - { span: { start: 4830, end: 4895 }, source: "the resources required and the implications for staff development", link: inferred, page: 6 }
  conditionType: process
  actor: institution
  about: "choosing what to do first and resourcing it"
  paraphrase: "The institution decides which activities matter most, and plans the resources and staff development they need."
  themes: ["theme:evidence-informed-enhancement", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/institution.define-measure-impact
  label: "Define and Measure Impact"
  span: { start: 5131, end: 5156 }
  position: { axis: perspective:institution, group: none, order: 4, page: 7 }
  explainedBy:
    - { span: { start: 4900, end: 5016 }, source: "defining and measuring the impact of enterprise and entrepreneurship education on internal and external stakeholders", link: stated, page: 6 }
  conditionType: process
  actor: institution
  about: "setting and measuring intended effects"
  paraphrase: "The institution says what effect its enterprise and entrepreneurship education should have, on people inside and outside it, and measures that effect."
  themes: ["theme:evidence-informed-enhancement", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/institution.engage-external-stakeholders
  label: "Engage with External Stakeholders"
  span: { start: 5096, end: 5129 }
  position: { axis: perspective:institution, group: none, order: 5, page: 7 }
  explainedBy:
    - { span: { start: 8853, end: 8980 }, source: "Recognising the value of engagement with external stakeholders in the co-creation of enterprise and entrepreneurship education.", link: stated, page: 13 }
    - { span: { start: 3904, end: 4044 }, source: "This in turn enables leaders to empower entrepreneurship educators to deliver an effective experience to internal and external stakeholders.", link: inferred, page: 4 }
  conditionType: relationship
  actor: institution
  about: "working with partners outside the institution"
  paraphrase: "The institution works with businesses, community bodies and other partners outside it, including in shaping its enterprise and entrepreneurship education."
  themes: ["theme:collaboration", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/institution.adapt-and-change
  label: "Adapt and Change"
  span: { start: 5078, end: 5094 }
  position: { axis: perspective:institution, group: none, order: 6, page: 7 }
  explainedBy:
    - { span: { start: 5021, end: 5076 }, source: "identifying what works well and what could work better.", link: inferred, page: 6 }
  conditionType: culture
  actor: institution
  about: "changing course on the evidence"
  paraphrase: "The institution acts on what it learns about what works, and changes its approach where something could work better."
  themes: ["theme:evidence-informed-enhancement", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/educators.planning-and-delivery
  label: "Planning and Delivery"
  span: { start: 6278, end: 6299 }
  position: { axis: perspective:educators, group: none, order: 1, page: 9 }
  explainedBy:
    - { span: { start: 5862, end: 5941 }, source: "designing, developing and delivering enterprise and entrepreneurship curriculum", link: stated, page: 8 }
    - { span: { start: 7855, end: 7986 }, source: "Each of these three approaches is associated with different pedagogies, teaching and learning activities and assessment strategies.", link: inferred, page: 10 }
  conditionType: practice
  actor: educator
  about: "designing and teaching enterprise learning"
  paraphrase: "Staff design, develop and teach enterprise and entrepreneurship learning, in the curriculum or outside it, choosing methods to suit the aim."
  themes: ["theme:entrepreneurial-pedagogy", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/educators.building-collaborative-relationships
  label: "Building Collaborative Relationships"
  span: { start: 6301, end: 6337 }
  position: { axis: perspective:educators, group: none, order: 2, page: 9 }
  explainedBy:
    - { span: { start: 5946, end: 6038 }, source: "building collaborative relationships with others both within and external to the institution", link: stated, page: 8 }
  conditionType: relationship
  actor: educator
  about: "working with colleagues and outside partners"
  paraphrase: "Staff build working relationships with colleagues and with partners outside the institution to strengthen enterprise and entrepreneurship learning."
  themes: ["theme:collaboration", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/educators.reflecting-on-own-practice
  label: "Reflecting on Own Practice"
  span: { start: 6339, end: 6365 }
  position: { axis: perspective:educators, group: none, order: 3, page: 9 }
  explainedBy:
    - { span: { start: 6043, end: 6189 }, source: "reflecting on your own practice as an enterprise and entrepreneurship educator in order to identify what you do well and what you could do better.", link: stated, page: 8 }
    - { span: { start: 8994, end: 9145 }, source: "Providing a resource to reflect on professional development needs and requirements, acting as a benchmark to reflect on current practice and provision.", link: inferred, page: 13 }
  conditionType: practice
  actor: educator
  about: "teachers reviewing their own teaching"
  paraphrase: "Staff look critically at their own enterprise and entrepreneurship teaching to see what works and what to improve."
  themes: ["theme:evidence-informed-enhancement", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/educators.awareness-research-policy-practice
  label: "Awareness of Research, Policy and Practice"
  span: { start: 6234, end: 6276 }
  position: { axis: perspective:educators, group: none, order: 4, page: 9 }
  explainedBy:
    - { span: { start: 1450, end: 1630 }, source: "In 2018, the QAA worked with several organisations, including the partners that developed this framework, to provide clearly defined terms for both enterprise and entrepreneurship.", link: inferred, page: 2 }
    - { span: { start: 3148, end: 3221 }, source: "Evidence shows the value of developing entrepreneurial skills in learners", link: inferred, page: 4 }
  conditionType: disposition
  actor: educator
  about: "keeping up with the field"
  paraphrase: "Staff keep up with research, national policy and current practice in enterprise and entrepreneurship education and let it inform their teaching."
  themes: ["theme:evidence-informed-enhancement", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/educators.motivational-inspirational-leadership
  label: "Motivational and Inspirational Leadership"
  span: { start: 6191, end: 6232 }
  position: { axis: perspective:educators, group: none, order: 5, page: 9 }
  explainedBy:
    - { span: { start: 5745, end: 5857 }, source: "motivating and inspiring learners in developing enterprising and entrepreneurial mindsets, behaviours and skills", link: stated, page: 8 }
  conditionType: relationship
  actor: educator
  about: "teachers inspiring an enterprising outlook"
  paraphrase: "Staff motivate and inspire students to develop enterprising and entrepreneurial ways of thinking, behaving and working."
  themes: ["theme:entrepreneurial-mindset", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/students.opportunity-recognition-evaluation
  label: "Opportunity Recognition and Evaluation"
  span: { start: 8015, end: 8053 }
  position: { axis: perspective:students, group: none, order: 1, page: 11 }
  explainedBy:
    - { span: { start: 7368, end: 7449 }, source: "the perceived opportunities recognised from their experiences in higher education", link: inferred, page: 10 }
  conditionType: practice
  actor: student
  about: "spotting and judging opportunities"
  paraphrase: "Students learn to notice opportunities and to judge which are worth pursuing."
  themes: ["theme:enterprising-capability", "theme:critical-thinking", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/students.decision-making-uncertainty
  label: "Decision Making under Uncertainty"
  span: { start: 8091, end: 8124 }
  position: { axis: perspective:students, group: none, order: 2, page: 11 }
  explainedBy:
    - { span: { start: 6882, end: 6977 }, source: "Developing their skills and competencies associated with being enterprising and entrepreneurial", link: inferred, page: 10 }
  conditionType: practice
  actor: student
  about: "deciding without full information"
  paraphrase: "Students learn to make reasoned decisions when information is incomplete and outcomes are uncertain."
  themes: ["theme:enterprising-capability", "theme:critical-thinking", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/students.implementation-of-ideas
  label: "Implementation of Ideas"
  span: { start: 8149, end: 8172 }
  position: { axis: perspective:students, group: none, order: 3, page: 11 }
  explainedBy:
    - { span: { start: 403, end: 598 }, source: "the enhancement of appropriate skills, knowledge, attributes and behaviours necessary for transforming creative ideas into actions are of ever-increasing importance across all disciplinary areas.", link: inferred, page: 2 }
  conditionType: practice
  actor: student
  about: "turning ideas into action"
  paraphrase: "Students learn to turn an idea into action: to plan it, organise people and resources, and carry it through."
  themes: ["theme:enterprising-capability", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/students.communication-strategy-skills
  label: "Communication and Strategy Skills"
  span: { start: 8196, end: 8229 }
  position: { axis: perspective:students, group: none, order: 4, page: 11 }
  explainedBy:
    - { span: { start: 6882, end: 6977 }, source: "Developing their skills and competencies associated with being enterprising and entrepreneurial", link: inferred, page: 10 }
  conditionType: practice
  actor: student
  about: "communicating ideas and planning a strategy"
  paraphrase: "Students learn to communicate their ideas to different audiences and to plan a strategy for achieving them."
  themes: ["theme:enterprising-capability", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/students.interpersonal-skills
  label: "Interpersonal Skills"
  span: { start: 8174, end: 8194 }
  position: { axis: perspective:students, group: none, order: 5, page: 11 }
  explainedBy:
    - { span: { start: 9944, end: 10031 }, source: "Encouraging reciprocal and collaborative ways of working within and across disciplines.", link: inferred, page: 13 }
  conditionType: practice
  actor: student
  about: "working well with other people"
  paraphrase: "Students learn to work with others: to build relationships, collaborate across disciplines and handle differences."
  themes: ["theme:enterprising-capability", "theme:collaboration", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/students.reflection-and-action
  label: "Reflection and Action"
  span: { start: 8126, end: 8147 }
  position: { axis: perspective:students, group: none, order: 6, page: 11 }
  explainedBy:
    - { span: { start: 6790, end: 6877 }, source: "Developing the learner’s mindset associated with being enterprising and entrepreneurial", link: inferred, page: 10 }
  conditionType: disposition
  actor: student
  about: "reflecting and then acting on it"
  paraphrase: "Students reflect on their experience, including setbacks, and use what they learn to act differently next time."
  themes: ["theme:entrepreneurial-mindset", "theme:agency-self-actualisation", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/students.starting-developing-business
  label: "Starting and Developing a Business"
  span: { start: 8055, end: 8089 }
  position: { axis: perspective:students, group: none, order: 7, page: 11 }
  explainedBy:
    - { span: { start: 6982, end: 7207 }, source: "Generating the learner’s understanding of the outcomes from the enterprise and entrepreneurship process – e.g. starting a business or adding value through innovation and creativity when working for or supporting someone else.", link: stated, page: 10 }
    - { span: { start: 3223, end: 3370 }, source: "not only in terms of facilitating the creation of new ventures whilst in education, and upon graduation, but also in enhancing their employability.", link: inferred, page: 4 }
  conditionType: practice
  actor: student
  about: "creating and growing a venture"
  paraphrase: "Students learn what it takes to start and grow a business or other venture, as one possible outcome of being enterprising."
  themes: ["theme:enterprising-capability", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/enterprise-2024/students.creativity-innovation
  label: "Creativity and Innovation"
  span: { start: 7988, end: 8013 }
  position: { axis: perspective:students, group: none, order: 8, page: 11 }
  explainedBy:
    - { span: { start: 7116, end: 7206 }, source: "adding value through innovation and creativity when working for or supporting someone else", link: inferred, page: 10 }
    - { span: { start: 493, end: 533 }, source: "transforming creative ideas into actions", link: inferred, page: 2 }
  conditionType: disposition
  actor: student
  about: "generating new ideas and approaches"
  paraphrase: "Students learn to generate original ideas and new ways of doing things, and to use them to add value."
  themes: ["theme:enterprising-capability", "theme:enterprise"]
  sameLabelAs: none
```

### M2a Component audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- component: advancehe/enterprise-2024/institution.apply-definitions
  forPractitioner: { text: "Agree working definitions of enterprise and of entrepreneurship, publish them, and use them in strategy, course approval and reporting so that everyone means the same thing.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the people around your study to mean the same thing when they talk about being enterprising or starting a venture, so you know what is being asked of you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an institutional choice of definitions, kept distinct: enterprise is the broader capacity to act on ideas, entrepreneurship its application to create value. Do not merge the two terms or swap in employability. Set it beside the shared-language use for educators."
  author-agent-dialogue: "Raise it when people in one conversation use enterprise and entrepreneurship as if they were the same. Ask: \"Which of the two do you mean here?\" and \"Does your institution have a definition you can point to?\" Avoid insisting on one wording when the institution has its own."
- component: advancehe/enterprise-2024/institution.understand-what-others-do
  forPractitioner: { text: "Map the enterprise and entrepreneurship activity already running across departments and services, and look at what comparable institutions do, before planning new work.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your university to know what chances to be enterprising already exist across it, so it can point you to them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as mapping and learning from existing activity, inside and outside the institution. The label says \"others\"; the prose speaks of mapping activity in the institution, so do not claim the source asks for sector benchmarking in so many words."
  author-agent-dialogue: "Raise it when someone plans a new enterprise initiative. Ask: \"What already happens elsewhere in the institution that this overlaps with?\" and \"Who else has tried this?\" Avoid implying that the existing activity is necessarily good."
- component: advancehe/enterprise-2024/institution.prioritise-action
  forPractitioner: { text: "Decide which activities come first on the evidence of the mapping, and cost them, including the staff development they will need.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the chances on offer to you to be planned and funded, not left to chance.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a planning step that follows mapping: choose, then resource, including staff development. Do not present it as a list of fixed priorities; the source names none."
  author-agent-dialogue: "Raise it when a plan lists many actions with no order. Ask: \"Which of these comes first, and why?\" and \"What staff time or training does it need?\" Avoid choosing priorities for the institution."
- component: advancehe/enterprise-2024/institution.define-measure-impact
  forPractitioner: { text: "State the intended effects of the provision, on students, staff and partners outside the institution, and collect evidence of whether they happen.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your university to check whether what it offers really helps you, and to change it if it does not.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe impact as defined before it is measured, and as reaching both internal and external stakeholders. Do not equate impact only with business start-ups; the source also counts adding value when working for others."
  author-agent-dialogue: "Raise it when an activity is judged by attendance alone. Ask: \"What difference was this meant to make, and for whom?\" and \"How would you know?\" Avoid treating one measure as enough."
- component: advancehe/enterprise-2024/institution.engage-external-stakeholders
  forPractitioner: { text: "Build lasting links with employers, entrepreneurs and community organisations, and involve them in designing and delivering learning, not only as guest speakers.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to meet and work with people from businesses and community groups during your studies, not only your teaching staff.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present external partners as co-creators of the learning, as the use lists do, not as an audience. Do not limit stakeholders to private business; the source names public, voluntary and community settings too."
  author-agent-dialogue: "Raise it when a course is designed without anyone from outside. Ask: \"Who outside the institution could help shape this?\" and \"What would they gain?\" Avoid presenting partners only as funders."
- component: advancehe/enterprise-2024/institution.adapt-and-change
  forPractitioner: { text: "Act on evaluation: keep what works, change what does not, and say what changed and why.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your university to change how it supports you when what it has been doing does not work well.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the step that closes the loop after measuring impact. Do not claim the source sets a review cycle; it names none."
  author-agent-dialogue: "Raise it when evaluation results sit unused. Ask: \"What did you learn, and what will you change because of it?\" Avoid suggesting change for its own sake."
- component: advancehe/enterprise-2024/educators.planning-and-delivery
  forPractitioner: { text: "Plan enterprise and entrepreneurship learning deliberately: decide whether students learn about it, for it or through it, and match activities and assessment to that choice.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect learning about being enterprising to be planned, with activities and assessment that fit what you are meant to gain.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as curriculum design and teaching, in the curriculum or outside it. Link it to the source's three approaches (learning about, for and through) and say they need different methods and assessment. Do not assume enterprise learning sits only in business subjects."
  author-agent-dialogue: "Raise it when someone plans an enterprise activity. Ask: \"Is this learning about enterprise, for it, or through doing it?\" and \"Does the assessment match that?\" Avoid prescribing one method."
- component: advancehe/enterprise-2024/educators.building-collaborative-relationships
  forPractitioner: { text: "Work with colleagues in other subjects and services, and with partners outside the institution, so that students meet varied people and settings.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the people who teach you to bring in colleagues and outside contacts who widen what you can learn and do.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe relationships both inside and outside the institution. Set it beside the institution's engagement with external stakeholders, which it serves at the level of the teacher."
  author-agent-dialogue: "Raise it when a teacher works alone on enterprise teaching. Ask: \"Who inside or outside the institution could you work with on this?\" Avoid assuming the teacher has spare time to build networks."
- component: advancehe/enterprise-2024/educators.reflecting-on-own-practice
  forPractitioner: { text: "Review your own enterprise teaching regularly, using student work, feedback and the dial, and plan the development you need.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your teachers to review and improve how they teach you, and to ask what helped.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the teacher's own review of practice, linked to professional development. Do not present it as appraisal by others."
  author-agent-dialogue: "Raise it when a teacher asks how to improve an enterprise module. Ask: \"What went well last time, and what would you change?\" and \"What development would help?\" Avoid judging the teacher's practice yourself."
- component: advancehe/enterprise-2024/educators.awareness-research-policy-practice
  forPractitioner: { text: "Keep up with research, sector guidance and policy on enterprise and entrepreneurship education, and use it to shape what and how you teach.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your teachers to know current thinking on enterprise and bring it into what you learn.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as staying current with research, policy and practice. The prose does not explain this segment directly; links to the QAA definitions and to the evidence claim are our reading. Do not cite specific studies the source does not name."
  author-agent-dialogue: "Raise it when teaching relies on old or anecdotal ideas about entrepreneurs. Ask: \"What does current research or sector policy say about this?\" Avoid overwhelming the teacher with reading lists."
- component: advancehe/enterprise-2024/educators.motivational-inspirational-leadership
  forPractitioner: { text: "Motivate students by example and encouragement: show what being enterprising looks like, and help them see it as open to them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your teachers to encourage you to see yourself as someone who can act on ideas.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as leadership by teachers in the learning, aimed at mindset as well as skills. Do not reduce it to charisma or to celebrating famous entrepreneurs."
  author-agent-dialogue: "Raise it when students seem unmotivated by enterprise content. Ask: \"What would make this feel possible for these students?\" and \"Who could they see doing it?\" Avoid assuming every student wants to start a business."
- component: advancehe/enterprise-2024/students.opportunity-recognition-evaluation
  forPractitioner: { text: "Give students real situations in which to spot needs or openings, and teach them to test which are worth pursuing.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will practise spotting opportunities around you and weighing up which are worth your effort.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as two linked skills: noticing an opportunity and evaluating it. Do not limit opportunities to business ideas; they include social and cultural value."
  author-agent-dialogue: "Raise it when a student has an idea and is unsure of it. Ask: \"What need does this meet, and for whom?\" and \"What would tell you it is worth pursuing?\" Avoid judging the idea for them."
- component: advancehe/enterprise-2024/students.decision-making-uncertainty
  forPractitioner: { text: "Set tasks where the information is incomplete and the outcome unknown, and ask students to decide, justify and then review their decision.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will practise making decisions when you cannot know everything, and explaining why you chose as you did.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as reasoned judgement where data are partial and outcomes unknown. The prose does not explain this segment; the link to skills and competencies is our reading. Do not equate uncertainty with recklessness."
  author-agent-dialogue: "Raise it when a student waits for certainty before acting. Ask: \"What do you know now, and what is the smallest step you could take?\" Avoid pressing a student to take risks they cannot afford."
- component: advancehe/enterprise-2024/students.implementation-of-ideas
  forPractitioner: { text: "Let students carry an idea through to action, with real constraints of time, people and resources, rather than stopping at the plan.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will get the chance to carry an idea through to something real, not just write about it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as acting on ideas, the step after generating them. The source treats turning ideas into action as important in every subject; do not confine it to business courses."
  author-agent-dialogue: "Raise it when a student's work stops at the proposal. Ask: \"What would the first real step be, and what do you need to take it?\" Avoid pushing implementation where the task is meant to be exploratory."
- component: advancehe/enterprise-2024/students.communication-strategy-skills
  forPractitioner: { text: "Have students pitch, present and write for real audiences, and plan how they would get an idea adopted.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will practise explaining your ideas to different people and planning how to make them happen.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as two linked skills: communicating to varied audiences and planning a route to the goal. The prose does not explain the segment; the link is our reading."
  author-agent-dialogue: "Raise it when a student's idea is sound but poorly explained. Ask: \"Who needs to be persuaded, and what matters to them?\" Avoid coaching style over substance."
- component: advancehe/enterprise-2024/students.interpersonal-skills
  forPractitioner: { text: "Set work in teams, including teams across subjects, and teach students how to build relationships and resolve differences.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will work with other people, sometimes from other subjects, and learn to build good working relationships.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as relationship and teamwork skills. Link it to the students' use item on collaborative working across disciplines. Do not reduce it to presentation skills."
  author-agent-dialogue: "Raise it when a student struggles in a team. Ask: \"What does each person bring, and how are you sharing the work?\" Avoid taking sides in a team dispute."
- component: advancehe/enterprise-2024/students.reflection-and-action
  forPractitioner: { text: "Build reflection into enterprise tasks, and require students to say what they will do differently and then do it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will look back on what you tried, including what went wrong, and use it to decide your next step.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present reflection as leading to action, not as an end in itself. Treat setbacks as material for learning. The link to the mindset stage is our reading."
  author-agent-dialogue: "Raise it after a task or setback. Ask: \"What happened, what did you learn, and what will you do next?\" Avoid dwelling on failure without moving to action."
- component: advancehe/enterprise-2024/students.starting-developing-business
  forPractitioner: { text: "Give students who want it a route to start or grow a venture while studying, and show all students how ventures are created, whether or not they will found one.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can learn how a business or other venture is started and grown, and try it if you want to, while you study or afterwards.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present venture creation as one outcome among others; the source sets it beside adding value when working for someone else. Do not imply every student should start a business."
  author-agent-dialogue: "Raise it when a student has a venture idea. Ask: \"What would you need to test this on a small scale?\" and \"What support exists here?\" Avoid financial or legal advice."
- component: advancehe/enterprise-2024/students.creativity-innovation
  forPractitioner: { text: "Create space for students to generate and test original ideas, and value new approaches even when they do not fully succeed.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will be encouraged to come up with new ideas and fresh ways of doing things, and to try them out.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present creativity and innovation as generating ideas and putting new approaches to use. Do not confine creativity to the arts or innovation to technology."
  author-agent-dialogue: "Raise it when a student copies a model answer. Ask: \"What could be done differently here?\" and \"What would a fresh approach look like?\" Avoid dismissing unusual ideas too quickly."
```

### M3 Conditions
<!-- label: editorial; status: drafted; basis: discussion. Ours, every field. -->
```yaml
- component: advancehe/enterprise-2024/institution.apply-definitions
  theme: theme:shared-language
  holdsWhen: "The institution has a written definition of each term, and its documents and staff use the terms in line with it."
  signs: ["a definition of each term appears in strategy or curriculum documents", "course descriptions use the terms consistently", "staff from different areas give similar answers when asked what the terms mean"]
  absentWhen: "The terms are used loosely and interchangeably, so plans and reports cannot be compared."
  contextSteer: "Say which of the two you mean, enterprise or entrepreneurship, and keep to that meaning throughout the material."
  basis: ours
- component: advancehe/enterprise-2024/institution.understand-what-others-do
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Someone holds a current map of enterprise and entrepreneurship activity across the institution, and planning starts from it."
  signs: ["a current list or map of activity exists and is shared", "new proposals cite related activity elsewhere", "staff in different units know of one another's work"]
  absentWhen: "Units start initiatives in isolation, duplicating or missing work done elsewhere."
  contextSteer: "Point the learner to related opportunities that already exist beyond the immediate course."
  basis: ours
- component: advancehe/enterprise-2024/institution.prioritise-action
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Enterprise and entrepreneurship activity has stated priorities, each with resources and any staff development it needs."
  signs: ["a plan ranks activities and gives reasons", "budgets or staff time are attached to the priorities", "staff development is planned alongside new activity"]
  absentWhen: "Activity grows by accident, without resources or the staff training it needs."
  contextSteer: "Focus the material on a few things that matter most, and say what the learner needs in order to do them."
  basis: ours
- component: advancehe/enterprise-2024/institution.define-measure-impact
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Intended effects are written down before activity starts, and evidence of the actual effects on students and partners is collected and reported."
  signs: ["objectives name the effect sought, not only the activity", "evaluation reaches external partners as well as students", "reports compare results with the intended effects"]
  absentWhen: "Success is reported as numbers taking part, and no one knows what changed as a result."
  contextSteer: "State what the learner should be able to do differently afterwards, so the effect can be seen."
  basis: ours
- component: advancehe/enterprise-2024/institution.engage-external-stakeholders
  theme: theme:collaboration
  holdsWhen: "External partners take part in designing, delivering or judging enterprise and entrepreneurship learning, and the relationship lasts beyond one event."
  signs: ["partners help set briefs or projects", "the same partners return year on year", "partners from public and voluntary settings take part as well as businesses"]
  absentWhen: "Contact with the outside world is occasional and one-way, such as a single talk."
  contextSteer: "Set the task in a real external setting, with a partner, client or community need the learner can work with."
  basis: ours
- component: advancehe/enterprise-2024/institution.adapt-and-change
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Evaluation findings lead to recorded changes in provision, and those who gave evidence hear what changed."
  signs: ["reviews end with named changes", "provision differs from year to year for stated reasons", "students and partners are told what changed"]
  absentWhen: "Provision stays the same year after year whatever the evaluation shows."
  contextSteer: "Invite the learner to revise an idea after feedback, and treat the revision as part of the task."
  basis: ours
- component: advancehe/enterprise-2024/educators.planning-and-delivery
  theme: theme:entrepreneurial-pedagogy
  holdsWhen: "Enterprise and entrepreneurship learning is planned with a stated approach, and its activities and assessment fit that approach."
  signs: ["module plans state whether learning is about, for or through enterprise", "assessment tasks match the approach chosen", "extracurricular activity is planned with the same care as taught modules"]
  absentWhen: "Enterprise activity is added ad hoc, and its assessment does not match what students did."
  contextSteer: "Make clear whether the learner is studying enterprise, preparing for it or doing it, and match the task to that."
  basis: ours
- component: advancehe/enterprise-2024/educators.building-collaborative-relationships
  theme: theme:collaboration
  holdsWhen: "Staff teaching enterprise and entrepreneurship work regularly with colleagues elsewhere in the institution and with outside partners."
  signs: ["teaching involves colleagues from other subjects or services", "outside partners contribute to sessions or projects", "staff can name the partners they work with"]
  absentWhen: "Enterprise teaching rests on one person working alone within one subject."
  contextSteer: "Bring in perspectives from other subjects or from outside partners, so the learner meets more than one viewpoint."
  basis: ours
- component: advancehe/enterprise-2024/educators.reflecting-on-own-practice
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Staff review their enterprise teaching against evidence, name strengths and changes, and act on them."
  signs: ["staff keep notes or records of what worked", "changes to teaching cite feedback or results", "staff seek development linked to what they found"]
  absentWhen: "Teaching is repeated unchanged, and development is not linked to any review."
  contextSteer: "Build in a point where the learner reviews what worked in their own approach and what they would change."
  basis: ours
- component: advancehe/enterprise-2024/educators.awareness-research-policy-practice
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Staff can name current research, policy or practice that informs their enterprise teaching, and their materials reflect it."
  signs: ["reading lists or materials include recent sources", "staff refer to sector definitions and policy", "staff attend or contribute to networks in the field"]
  absentWhen: "Teaching rests on personal experience or outdated ideas alone."
  contextSteer: "Ground the material in current thinking on enterprise, and show the learner where it comes from."
  basis: ours
- component: advancehe/enterprise-2024/educators.motivational-inspirational-leadership
  theme: theme:entrepreneurial-mindset
  holdsWhen: "Students describe staff as encouraging them to act on ideas, and more students take up enterprise activity as a result."
  signs: ["staff share examples relevant to their students' own settings", "students say they feel able to try ideas", "take-up of optional enterprise activity rises"]
  absentWhen: "Enterprise is presented as for a few, and most students see it as not for them."
  contextSteer: "Use examples the learner can relate to, and frame being enterprising as open to them."
  basis: ours
- component: advancehe/enterprise-2024/students.opportunity-recognition-evaluation
  theme: theme:enterprising-capability
  holdsWhen: "Students identify opportunities in real settings and give reasons for pursuing some and not others."
  signs: ["students propose ideas drawn from needs they observed", "students compare options using stated criteria", "students drop weak ideas for reasons they can give"]
  absentWhen: "Students are handed ready-made ideas and never judge whether an opening is worth pursuing."
  contextSteer: "Ask the learner to find a real need or opening and to judge whether it is worth pursuing, with reasons."
  basis: ours
- component: advancehe/enterprise-2024/students.decision-making-uncertainty
  theme: theme:enterprising-capability
  holdsWhen: "Students make and justify decisions with incomplete information, and review them as results come in."
  signs: ["tasks include incomplete or changing information", "students state the assumptions behind a decision", "students revise decisions when new information arrives"]
  absentWhen: "Tasks always have one right answer and full information."
  contextSteer: "Leave some information uncertain, and ask the learner to decide, state their assumptions and say what would change their mind."
  basis: ours
- component: advancehe/enterprise-2024/students.implementation-of-ideas
  theme: theme:enterprising-capability
  holdsWhen: "Students take ideas beyond planning into action, organising what is needed and seeing them through."
  signs: ["projects produce a working output, event or prototype", "students manage time, people or budgets", "students report what happened when they acted"]
  absentWhen: "Ideas stay on paper and students never test them in action."
  contextSteer: "Ask the learner to take an idea to a first real step and to report what happened."
  basis: ours
- component: advancehe/enterprise-2024/students.communication-strategy-skills
  theme: theme:enterprising-capability
  holdsWhen: "Students present ideas to audiences beyond their tutors and set out a plan for reaching their aim."
  signs: ["students pitch or present to external audiences", "students adapt the message to the audience", "work includes a plan with steps and choices"]
  absentWhen: "Students communicate only to tutors, in one format, with no plan for action."
  contextSteer: "Name a real audience for the learner's idea and ask them to shape both message and plan for it."
  basis: ours
- component: advancehe/enterprise-2024/students.interpersonal-skills
  theme: theme:enterprising-capability
  holdsWhen: "Students work in teams, including across disciplines, and manage relationships and disagreements well."
  signs: ["tasks require teamwork with shared outcomes", "teams include students from other subjects", "students reflect on how the team worked"]
  absentWhen: "Students work alone, or teams form without support and fall apart."
  contextSteer: "Make the task depend on working with others, and ask the learner to reflect on how they worked together."
  basis: ours
- component: advancehe/enterprise-2024/students.reflection-and-action
  theme: theme:entrepreneurial-mindset
  holdsWhen: "Students reflect on their experience and setbacks and can show how that reflection changed what they did next."
  signs: ["reflections end with a planned action", "later work shows the planned change", "setbacks are discussed openly as learning"]
  absentWhen: "Reflection is written for marks and never changes what students do."
  contextSteer: "After any attempt, ask the learner what they learned and what they will do next."
  basis: ours
- component: advancehe/enterprise-2024/students.starting-developing-business
  theme: theme:enterprising-capability
  holdsWhen: "Students can learn about, and if they wish try, starting or growing a venture with support during their studies."
  signs: ["start-up support is available to students", "students run or test ventures as part of learning", "students can explain how a venture is set up and grown"]
  absentWhen: "Venture creation is talked about but never practised, or presented as the only aim."
  contextSteer: "Treat starting a venture as one option, and show the learner how the same skills add value when working for others."
  basis: ours
- component: advancehe/enterprise-2024/students.creativity-innovation
  theme: theme:enterprising-capability
  holdsWhen: "Students generate original ideas or approaches and test them, and novelty is valued in assessment."
  signs: ["tasks reward original approaches", "students produce several ideas before choosing one", "unusual ideas are discussed seriously"]
  absentWhen: "Tasks reward reproducing a set approach, and new ideas are seen as risky."
  contextSteer: "Ask the learner for more than one idea, and value an original approach even if it is imperfect."
  basis: ours
```

### M4 Open segments
<!-- label: both; status: drafted; basis: primary -->
```yaml
[]   # the figure leaves no segment blank on purpose
```

### M5 Crosswalks
<!-- label: both; status: drafted; basis: primary -->
```yaml
stated:
  lead: { span: { start: 10454, end: 10510 }, source: "It is particularly relevant to the following dimensions:", page: 14 }
  codes:
    - { to: advancehe/psf-dimensions-2023/V1, code: V1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V2, code: V2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V4, code: V4, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A1, code: A1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A2, code: A2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A4, code: A4, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K2, code: K2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K3, code: K3, page: 14, note: "named in the PSF table" }
  fellowship: { span: { start: 10591, end: 10805 }, source: "Advance HE invites all those teaching or supporting learning to evidence their use of this or other Student Success Frameworks in applying for Fellowship in recognition of their commitment to professional practice.", page: 14, note: "an invitation, not an obligation: not an S4 statement" }
inferred:
  - { from: "model", to: "theme:employability", rel: related, basis: inferred, note: "the 3Es and the rationale tie the model to employability" }
  - { from: "advancehe/enterprise-2024/students.creativity-innovation", to: "qaa/enterprise-2018/outcome.creativity.b1", rel: related, basis: inferred, note: "QAA 2018's 'Creativity and innovation' outcome theme" }
  - { from: "advancehe/enterprise-2024/students.opportunity-recognition-evaluation", to: "qaa/enterprise-2018/outcome.opportunity.b1", rel: related, basis: inferred, note: "QAA 2018's 'Opportunity recognition, creation and evaluation' outcome theme" }
  - { from: "advancehe/enterprise-2024/students.decision-making-uncertainty", to: "qaa/enterprise-2018/outcome.decision.b1", rel: related, basis: inferred, note: "QAA 2018's decision-making outcome theme, which stresses uncertainty" }
  - { from: "advancehe/enterprise-2024/students.implementation-of-ideas", to: "qaa/enterprise-2018/outcome.implementation.b1", rel: related, basis: inferred, note: "QAA 2018's 'Implementation of ideas through leadership and management' outcome theme" }
  - { from: "advancehe/enterprise-2024/students.reflection-and-action", to: "qaa/enterprise-2018/outcome.reflection.b1", rel: related, basis: inferred, note: "QAA 2018's reflection into action outcome theme" }
  - { from: "advancehe/enterprise-2024/students.communication-strategy-skills", to: "qaa/enterprise-2018/outcome.communication.b1", rel: related, basis: inferred, note: "QAA 2018's 'Communication and strategy skills' outcome theme, which also covers interpersonal skills" }
```

### M6 Practice themes carried
<!-- label: both; status: drafted; basis: discussion -->
```yaml
- { id: theme:shared-language, tier: practice, working: "key terms are defined, agreed and used the same way by everyone involved", carriedBy: ["advancehe/enterprise-2024/institution.apply-definitions"], status: provisional }
- { id: theme:evidence-informed-enhancement, tier: practice, working: "practice is mapped, its effects are evaluated and it is improved on that evidence", carriedBy: ["advancehe/enterprise-2024/institution.understand-what-others-do", "advancehe/enterprise-2024/institution.prioritise-action", "advancehe/enterprise-2024/institution.define-measure-impact", "advancehe/enterprise-2024/institution.adapt-and-change", "advancehe/enterprise-2024/educators.reflecting-on-own-practice", "advancehe/enterprise-2024/educators.awareness-research-policy-practice"], status: provisional }
- { id: theme:collaboration, tier: practice, working: "learning and problem-solving are done with others, across subjects, professions and sectors", carriedBy: ["advancehe/enterprise-2024/institution.engage-external-stakeholders", "advancehe/enterprise-2024/educators.building-collaborative-relationships", "advancehe/enterprise-2024/students.interpersonal-skills"], status: provisional }
- { id: theme:entrepreneurial-pedagogy, tier: practice, working: "teaching methods and assessment match whether learners study, prepare for or do enterprise", carriedBy: ["advancehe/enterprise-2024/educators.planning-and-delivery"], status: provisional }
- { id: theme:entrepreneurial-mindset, tier: practice, working: "learners come to see themselves as able to act on ideas, and learn from setbacks", carriedBy: ["advancehe/enterprise-2024/educators.motivational-inspirational-leadership", "advancehe/enterprise-2024/students.reflection-and-action"], status: provisional }
- { id: theme:enterprising-capability, tier: practice, working: "learners build and practise the skills of turning ideas into value", carriedBy: ["advancehe/enterprise-2024/students.opportunity-recognition-evaluation", "advancehe/enterprise-2024/students.decision-making-uncertainty", "advancehe/enterprise-2024/students.implementation-of-ideas", "advancehe/enterprise-2024/students.communication-strategy-skills", "advancehe/enterprise-2024/students.interpersonal-skills", "advancehe/enterprise-2024/students.starting-developing-business", "advancehe/enterprise-2024/students.creativity-innovation"], status: provisional }
- { id: theme:critical-thinking, tier: practice, working: "questioning and evaluating are practised and valued", carriedBy: ["advancehe/enterprise-2024/students.opportunity-recognition-evaluation", "advancehe/enterprise-2024/students.decision-making-uncertainty"], status: provisional }
- { id: theme:agency-self-actualisation, tier: practice, working: "people grow into, use and trust their own judgement", carriedBy: ["advancehe/enterprise-2024/students.reflection-and-action"], status: provisional }
```

## Part B Terminology

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: enterprise, definition: "generating ideas and putting them into practice in real situations, drawing on creativity, initiative and problem solving", scopeNote: "the source quotes QAA 2018 for its definition; kept distinct from entrepreneurship", category: concept, practices: [learning-and-teaching] }
- { slug: entrepreneurship, definition: "using enterprising behaviours and competencies to create cultural, social or economic value, which may or may not mean founding a venture", scopeNote: "the source quotes QAA 2018 for its definition", category: concept, practices: [learning-and-teaching] }
- { slug: entrepreneurial-education, definition: "the collective name for enterprise education and entrepreneurship education together", scopeNote: "the source says the distinction between the two underpins the model", category: approach, practices: [learning-and-teaching] }
- { slug: three-es, definition: "employability, enterprise and entrepreneurship, recognised together", scopeNote: "the source frames enterprise and entrepreneurship beside employability", category: concept, practices: [learning-and-teaching] }
- { slug: learner-journey, definition: "the path a learner takes from awareness through mindset and skills to understanding outcomes, entered and left at different points", scopeNote: "four stages named in prose (p. 10); they are not drawn on the dial and are not groups here", category: concept, practices: [learning-and-teaching] }
- { slug: about-for-through, definition: "three approaches to enterprise teaching: studying it, preparing for it and learning by doing it", scopeNote: "each needs its own methods and assessment; drawn from QAA 2018", category: approach, practices: [learning-and-teaching] }
- { slug: entrepreneurial-effectiveness, definition: "the model of the learner's development towards acting enterprisingly, which the student journey draws on", scopeNote: "attributed to QAA 2018; not defined in this source", category: concept, practices: [learning-and-teaching] }
```

### B2a Terms as the issuer uses them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: enterprise, form: "enterprise", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: entrepreneurship, form: "entrepreneurship", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: entrepreneurial-education, form: "entrepreneurial education", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: three-es, form: "3Es", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: learner-journey, form: "journey of the learner", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: about-for-through, form: "learning ‘about’, learning ‘for’ and learning ‘through’", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: entrepreneurial-effectiveness, form: "entrepreneurial effectiveness", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the model names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term takes a meaning of its own in one component.

### B4 Relations
```yaml
- { rel: related, from: enterprise, to: entrepreneurship, note: "kept distinct; entrepreneurship applies enterprise to create value" }
- { rel: related, from: entrepreneurial-education, to: enterprise, note: "the collective term for the two" }
- { rel: related, from: learner-journey, to: entrepreneurial-effectiveness, note: "the journey draws on QAA's model" }
- { rel: related, from: about-for-through, to: learner-journey, note: "different approaches are required at each stage" }
```

### B5 Rules
- enterprise and entrepreneurship: never use them as synonyms; the source rests on the distinction.
- the QAA definitions: attribute them to QAA 2018, not to Advance HE, when quoting or paraphrasing.
- venture creation: present it as one outcome among others, beside adding value when working for someone else.

## Part C Process

### C0 Formality
`not-applicable`: the model sets conditions and uses, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE
  title: "Framework for enterprise and entrepreneurship"
  edition: "digital edition, 2024"
  year: 2024
  url: "https://www.advance-he.ac.uk (the series page not reached; D3)"
  retrieved: "PDF supplied by Abbott, 4 October 2026"
  licence: "none stated; held by permission (D-std-0019)"
  tier: primary
  readVia: direct
  held: 2e9f1d0a8c186ab5debd1e7a5d1708bc6fadf00577ae723d9138baae2ead99ca
  heldFiles: ["txt/advance-he-2024-framework-enterprise-entrepreneurship-standard.txt", "txt/advance-he-2024-framework-enterprise-entrepreneurship-standard.norm.txt", "records/advance-he-2024-framework-enterprise-entrepreneurship-standard.held.json", "pdf/advance-he-2024-framework-enterprise-entrepreneurship-standard.pdf"]
  citedIn: [0.2, S1, S2, S3, S4, M1, M2, M4, M5, B1]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: "2026-10-04", pass: P1, outcome: "used for every section; figure pages read as images (figure image)" }
```

### D3 Wanted sources
```yaml
- { citation: "Advance HE, Student Success Frameworks (series web page), current", settles: ["S8", "S7"], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- Front matter, S1: no year or copyright notice is printed in the file; 2024 is taken from the PDF's creation date (26 March 2024; modified 28 April 2025). The back cover calls it an "updated framework"; the original was jointly developed with EEUK, IOEE, ISBE, SFEDI and the QAA, and the dial was first shared at a 2018 symposium. No earlier edition is identified, so `supersedes: none-stated`. `copyrightNotice: none-stated`.
- Held text: held by Abbott's permission (4 October 2026, 05:03: "Yes full permission"; D-std-0019, as D-std-0013); private, never published.
- M2 order: clockwise from the top of each dial, read from the page images (pp. 7, 9, 11); each dial has a vertical divider at the top, and the first segment is the one to its right. The text layer gives the labels in a different order. Each label is found verbatim in the held text as its own paragraph, so MD-2 holds.
- M2 explainedBy: links marked `inferred` are std's reading; the source does not tie its prose to its segments. Several student segments (decision making, communication and strategy, interpersonal skills) and the educators' awareness segment have no prose that names them; their links are thin and inferred.
- Quotations: the definitions of enterprise and entrepreneurship (p. 2) are QAA 2018 (p. 7) quoted by the issuer. They are not statements of this model and are not used as explainedBy spans; B1 paraphrases them and names QAA as the source. The student journey is said to draw on QAA's model of entrepreneurial effectiveness (S7 refersTo).
- Institution bullets (p. 6): the six items after "Key elements here include:" are read as explanations of the dial (elements of the environment), not as directing statements; four of them name a dial segment in nearly the same words and are explainedBy spans. Only the framing line before them is an S4 record. For Abbott: confirm.
- Educators+ bullets (p. 8): the four items after "educators need to be able to deliver ... through:" are S4 statements under that lead-in (stem `through`), force must from "need to"; the issuer attributes the requirement to "national professional standards" (the PSF, inferred). They also explain dial segments.
- S4 force: "it is important to" (frame.three-es, frame.institution) is read as `should`, as "it is important that" is in the worked example; neither form is in D-std-0016. "required" (frame.students) reads as must. The use-list items are all gerunds or function lines and read as `describes`. For Abbott: rule whether "it is important to" reads as should.
- S4 use list: the text layer misplaces the items (it puts "Recognising the value of engagement ..." before the Educators+ heading and "Reflecting on the impact ..." before the Institution heading). The perspective of each item is read from the page image (pp. 12-13): Institution has "Reflecting on the impact ...", "Identifying the key ways ..." and "Identifying how to create ..."; Educators+ has "Recognising the value ...", "Identifying the difference ..." and "Providing a resource ..."; Students has "Understanding ...", "Identify and understanding ..." and "Encouraging ...". "Reflecting on the impact of what you do" reads like a staff use but sits beside the Institution roundel; recorded as printed.
- S4 use.students.2: the issuer's grammar mixes "Identify" with "understanding"; recorded as given, `mood: gerund`, force describes.
- Students (p. 10): "The journey of the learner is critical" is descriptive, not obliging ("critical" is not in D-std-0016). The four stages of the journey (awareness, mindset, skills and competencies, outcomes) are prose only; the dial has no inner ring, so GROUPS is empty and the stages are held as B1 learner-journey.
- M2 conditionType: the student segments are competencies; the template has no `competency` type, so skills are `practice` and outlooks (creativity, reflection) `disposition`.
- M6: proposed practice themes, provisional until the shared theme register exists: theme:shared-language, theme:evidence-informed-enhancement, theme:evidence-informed-enhancement, theme:collaboration, theme:entrepreneurial-pedagogy, theme:entrepreneurial-mindset, theme:enterprising-capability. theme:critical-thinking and theme:agency-self-actualisation are reused from the shared list.
- S6: theme:enterprise is the model's subject (stated). theme:employability is carried, stated: the 3Es and the rationale name it, and the back cover says the model complements the employability model. theme:edi is not carried: "the needs of all learners" (p. 6) is the only nod, and EDI is named only on the excluded back cover.
- S7 siblingOf: the employability model is named on the back cover (excluded from S3 but read); its id std:doc:advancehe-embedding-employability-2024-model is reserved here and must match whatever its own run uses.
- M5 inferred: the student segments are matched to the QAA 2018 outcome themes by their names; "Interpersonal Skills" and "Starting and Developing a Business" have no QAA outcome theme of their own (QAA folds interpersonal skills into communication and strategy).
- D3: Advance HE's web page for the series (current status, date, the full list of frameworks in the series) not reached; wanted.

---

## Change notes
- 0.1.1, 2026-10-04 09:26: practice themes aligned across the series by std (15 id(s) renamed by tools/theme_merges.json; the old ids are aliases in the shared theme register); rebuilt on builder 0.2.1. Model template 0.3.0-draft, builder 0.2.1: 19 components, 0 open segments, 16 statements, 8 practice themes.
- 0.1.0, 2026-10-04 09:20: first built (Abbott, 09:08: "Use your template model and refine as you go"; D-std-0018). Model template 0.2.0-draft, builder 0.2.0: 19 components, 0 open segments, 16 statements, 9 practice themes.
