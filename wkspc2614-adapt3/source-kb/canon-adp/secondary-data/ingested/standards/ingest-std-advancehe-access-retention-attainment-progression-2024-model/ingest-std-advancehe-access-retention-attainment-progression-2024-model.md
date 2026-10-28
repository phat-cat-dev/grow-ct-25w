---
id: std:doc:advancehe-access-retention-attainment-progression-2024-model
title: "Framework for student access, retention, attainment and progression"
profile: standards/model
profileVersion: none yet   # the variant's profile part is to write
issuer: Advance HE
kind: model
modelKind: condition-model
series: advancehe-student-success-frameworks-2024
axes: { perspectives: 3, facets: 0, groups: 4, segments: 49, openSegments: 0, labelsNotInText: 49 }
jurisdiction: [UK]   # not stated; Advance HE is UK-based and its frameworks are used internationally (inferred)
subjectScope: universal
subjects: []
edition: "digital edition, 2024"
published: 2024   # no date printed; from the PDF metadata (Part E)
revised: "none-stated"   # a later file date, if any (Part E)
status: current   # as at the held text; not checked against Advance HE's site (D3)
supersedes: "none-stated"
heldText: { method: sha256-bytes, raw: 55261cb1e3e0c4f1366f3cc770cea89efd283a649be1d3d109ca7ea2a9e382e4, normalised: 95425e1d70f7c65ea4bdd153ebb9bfc79e9946cd8a0298dd1e74af69223c67e1 }
original: { method: sha256-bytes, pdf: 408c18e01e829e47781602fda4f44a4738818bfa2740fd6d15022a5cc731e3dc, held: "library pdf/advance-he-2024-framework-student-access-retention-attainment-progression-standard.pdf" }
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
# Framework for student access, retention, attainment and progression

> The issuer's text is held beside this document in the library (`txt/advance-he-2024-framework-student-access-retention-attainment-progression-standard.norm.txt`). Each M2 `label` (where the text layer holds it), each `explainedBy` and M4 `source` and each S4 `source` is exactly its span's text, held for language analysis (D-std-0014); private, never published. Every other field is ours, and agents phrase from ours.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
A practice model from Advance HE's Student Success Frameworks: forty-nine components across the four stages of a student's route (getting in, staying on, achieving and moving on), seen from the institution, its staff and its students, each held here as a practice theme that can qualify the context of a lesson or a piece of material. Reach for it to set or check the conditions for students' entry, continuation, success and progression. It sets no levels and no outcomes: pair it with a framework or benchmark for what students achieve.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Advance HE (2024) treats access, retention, attainment and progression as four linked stages of a successful student journey, each resting on belonging and engagement, and holds senior leaders, staff and students jointly responsible for them. It draws three dials, for the institution, for staff (Educators+) and for students, each with an inner ring of the four stages and sixteen, sixteen and seventeen named segments, none left blank. A short list of four uses is given for each perspective. It names ten Professional Standards Framework 2023 dimensions as particularly relevant and invites its use as Fellowship evidence. It binds no one: it is an enhancement model, not an assurance standard.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: Advance HE
title: "Framework for student access, retention, attainment and progression"
series: "Advance HE Student Success Frameworks"
edition: "digital edition, 2024"
dates:
  published: 2024   # not printed; PDF metadata
  other: ["PDF created 7 May 2024", "PDF modified 28 April 2025"]
kind: model
jurisdiction: [UK]
authority: advisory
licence: "none stated in the file (D1)"
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the conditions for students' access, retention, attainment and progression across an institution, its staff and its students (D1, pp. 2-3)"
appliesTo:
  awards: [none-stated]
  levels: [none]
  providers: ["HE providers (as stated, p. 4)", "HE institutions (p. 4)"]
whoMustUse: "no one must; designed for all staff with a remit to support students, with responsibility shared by senior leaders, academic and professional services staff and students (D1, p. 3)"
howUsed: ["design", "review", "other: strategy, staff development, Fellowship evidence"]
doesNot: "none-stated"
beneficiary: the student
statedScope: "The framework is therefore designed for all staff with a remit to support students to achieve their potential."
statedScopeLocator: "D1, p. 3"
statedScopeSpan: { start: 503, end: 613 }
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "what-is", order: 1, componentType: section, parent: "none", heading: "What is student access, retention, attainment and progression?", gloss: "the four elements, each defined, and their shared basis in belonging", pages: "2", readFrom: "text layer" }
  - { number: "stages", order: 2, componentType: stage, parent: "what-is", heading: "(the four elements)", gloss: "Access, Retention, Attainment, Progression: one-line definitions", pages: "2", readFrom: "text layer" }
  - { number: "who-for", order: 3, componentType: section, parent: "none", heading: "Who is the framework for?", gloss: "shared responsibility; all staff with a remit to support students; partnership", pages: "3", readFrom: "text layer" }
  - { number: "why", order: 4, componentType: section, parent: "none", heading: "Why is access, retention, attainment and progression important?", gloss: "the providers' responsibility; what each stage depends on; awarding gaps and missions", pages: "4", readFrom: "text layer" }
  - { number: "structure", order: 5, componentType: figure, parent: "none", heading: "How is the framework structured?", gloss: "the three perspectives shared by the series", pages: "5", readFrom: "figure image" }
  - { number: "institution", order: 6, componentType: perspective, parent: "none", heading: "Institution", gloss: "framing prose: vision, strategy, analytics, spaces", pages: "6", readFrom: "text layer" }
  - { number: "institution.dial", order: 7, componentType: figure, parent: "institution", heading: "(dial)", gloss: "inner ring of four stages; sixteen segments", pages: "7", readFrom: "figure image" }
  - { number: "educators", order: 8, componentType: perspective, parent: "none", heading: "Educators+", gloss: "framing prose: staff roles, communities, curricula, assessment", pages: "8", readFrom: "text layer" }
  - { number: "educators.dial", order: 9, componentType: figure, parent: "educators", heading: "(dial)", gloss: "inner ring of four stages; sixteen segments", pages: "9", readFrom: "figure image" }
  - { number: "students", order: 10, componentType: perspective, parent: "none", heading: "Students", gloss: "framing prose: transition, practical support, belonging, participation", pages: "10", readFrom: "text layer" }
  - { number: "students.dial", order: 11, componentType: figure, parent: "students", heading: "(dial)", gloss: "inner ring of four stages; seventeen segments", pages: "11", readFrom: "figure image" }
  - { number: "use", order: 12, componentType: use-list, parent: "none", heading: "How can you use the framework?", gloss: "purpose; sibling frameworks named; four uses for each perspective", pages: "12-13", readFrom: "text layer" }
  - { number: "psf", order: 13, componentType: section, parent: "none", heading: "How does this framework align with the Professional Standards Framework (PSF) 2023?", gloss: "the PSF table (ten dimensions) and the Fellowship invitation", pages: "14", readFrom: "figure image" }
excluded:
  - { number: "photo", heading: "(photograph, no text)", kind: "other: a full-page photograph", pages: "15" }
  - { number: "back-cover", heading: "We help higher education organisations be the best they can be ...", kind: "other: the issuer's promotional back cover", pages: "16 (unnumbered)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only obliging framing lines, requirement lists and use lists are statements (model template rule 3). -->
```yaml
- id: advancehe/arap-2024/frame.responsibility
  locator: { number: "frame.responsibility", heading: "Who is the framework for?", page: 3 }
  span: { start: 360, end: 502 }
  source: "Access, retention, attainment and progression are the responsibility of senior leaders, academic and professional services staff and students."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "responsibility" read as must
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: both
  verbs: ["are"]
  about: "who holds responsibility for student success"
  themes: ["none"]
  paraphrase: "Responsibility for access, staying on, achievement and moving on lies with leaders, staff and students together."
  audience: both
  subjects: inherited
- id: advancehe/arap-2024/frame.providers
  locator: { number: "frame.providers", heading: "Why is access, retention, attainment and progression important?", page: 4 }
  span: { start: 1691, end: 1904 }
  source: "HE providers have a legal, ethical and economic responsibility to ensure they widen access to all who may benefit from higher education and to put support in place for all students to achieve their full potential."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "responsibility" read as must
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["have", "ensure", "widen", "benefit", "put", "achieve"]
  about: "the duty to widen access and support success"
  themes: ["none"]
  paraphrase: "Higher education institutions are bound, legally, ethically and economically, to open entry to all who could benefit and to support every student to do their best."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/frame.institution
  locator: { number: "frame.institution", heading: "Institution", page: 6 }
  span: { start: 4717, end: 4872 }
  source: "Vision needs to be aligned with a coherent set of strategies and policies that skilled academic and professional services staff are supported to implement."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "needs to" read as must
  level: none
  perspective: perspective:institution
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["needs", "aligned", "supported", "implement"]
  about: "vision aligned with strategy and policy"
  themes: ["none"]
  paraphrase: "The institution's vision must line up with consistent strategy and policy, which staff are equipped to carry out."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/frame.students
  locator: { number: "frame.students", heading: "Students", page: 10 }
  span: { start: 7748, end: 7933 }
  source: "Securing retention and attainment for all students requires a combination of practical support, including financial assistance and resource accessibility, academic and pastoral support."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "requires" read as must; a condition of success rather than a duty on a named party (Part E)
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Securing", "requires"]
  about: "the practical and personal support retention needs"
  themes: ["none"]
  paraphrase: "Keeping students on and helping them achieve depends on combining practical help, including money and accessible resources, with academic and pastoral support."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/use.institution.1
  locator: { number: "use.institution.1", heading: "How can you use the framework?", page: 12 }
  span: { start: 9560, end: 9646 }
  source: "Articulating a clear vision and mission aligned with coherent strategies and policies."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:institution
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Articulating", "aligned"]
  about: "a clear vision tied to strategy"
  themes: ["none"]
  paraphrase: "The institution uses the model to set out a clear vision and mission that fit its strategies and policies."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/use.institution.2
  locator: { number: "use.institution.2", heading: "How can you use the framework?", page: 12 }
  span: { start: 9661, end: 9741 }
  source: "Creating learning spaces that encourage collaboration and informal interactions."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:institution
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Creating", "encourage"]
  about: "spaces for collaboration and informal contact"
  themes: ["none"]
  paraphrase: "The institution creates spaces that invite students to work together and meet informally."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/use.institution.3
  locator: { number: "use.institution.3", heading: "How can you use the framework?", page: 12 }
  span: { start: 9742, end: 9823 }
  source: "Using data and technology effectively to prompt intervention to support students."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:institution
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Using", "prompt", "support"]
  about: "data that triggers support"
  themes: ["none"]
  paraphrase: "The institution uses data and technology well to prompt timely help for students."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/use.institution.4
  locator: { number: "use.institution.4", heading: "How can you use the framework?", page: 12 }
  span: { start: 9824, end: 9937 }
  source: "Focusing skilled academic and professional services staff on student achievement, wellbeing and career readiness."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:institution
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Focusing"]
  about: "staff focus on achievement, wellbeing and careers"
  themes: ["none"]
  paraphrase: "The institution directs its skilled staff towards student achievement, wellbeing and readiness for work."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/use.educators.1
  locator: { number: "use.educators.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 8791, end: 8909 }
  source: "Supporting students through outreach, admissions, academic/pastoral support, mental health services and career advice."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Supporting"]
  about: "the range of support staff give"
  themes: ["none"]
  paraphrase: "Staff support students across outreach, admissions, academic and personal support, mental health and careers."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/use.educators.2
  locator: { number: "use.educators.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 9943, end: 10056 }
  source: "Fostering belonging through pre-entry learning communities, staff-student collaboration and peer learning groups."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Fostering"]
  about: "building belonging through learning communities"
  themes: ["none"]
  paraphrase: "Staff build belonging through communities that form before entry, between staff and students and among peers."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/use.educators.3
  locator: { number: "use.educators.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 10057, end: 10178 }
  source: "Developing inclusive curricula and materials reflecting diverse experiences which promote positive engagement and debate."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Developing", "reflecting", "promote"]
  about: "inclusive curricula that open debate"
  themes: ["none"]
  paraphrase: "Staff develop inclusive curricula and materials that reflect diverse experience and invite debate."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/use.educators.4
  locator: { number: "use.educators.4", heading: "How can you use the framework?", page: 13 }
  span: { start: 10179, end: 10286 }
  source: "Offering diverse assessments with student choice and constructive feedback to enable all students to excel."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Offering", "enable", "excel"]
  about: "varied assessment with choice and feedback"
  themes: ["none"]
  paraphrase: "Staff offer varied assessment with student choice and useful feedback so that every student can do well."
  audience: practitioner
  subjects: inherited
- id: advancehe/arap-2024/use.students.1
  locator: { number: "use.students.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 10288, end: 10387 }
  source: "Providing practical support and inclusive learning environments for successful student transitions."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:students
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Providing"]
  about: "support for transitions"
  themes: ["none"]
  paraphrase: "Staff and the institution give practical support and inclusive settings that help students through each transition."
  audience: both
  subjects: inherited
- id: advancehe/arap-2024/use.students.2
  locator: { number: "use.students.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 10399, end: 10496 }
  source: "Delivering outreach activities promoting early engagement with the institution, course and peers."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:students
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Delivering", "promoting"]
  about: "outreach that starts engagement early"
  themes: ["none"]
  paraphrase: "Outreach is run to start students' engagement with the institution, course and peers early."
  audience: both
  subjects: inherited
- id: advancehe/arap-2024/use.students.3
  locator: { number: "use.students.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 10497, end: 10582 }
  source: "Providing financial assistance, resource accessibility and academic/pastoral support."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:students
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Providing"]
  about: "financial, resource and personal support"
  themes: ["none"]
  paraphrase: "Students are given money help, accessible resources and academic and personal support."
  audience: both
  subjects: inherited
- id: advancehe/arap-2024/use.students.4
  locator: { number: "use.students.4", heading: "How can you use the framework?", page: 13 }
  span: { start: 10583, end: 10707 }
  source: "Delivering inclusive teaching practices and fostering belonging through active participation with and beyond the curriculum."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # gerund: names an activity without a modal; describes (model template S4 mood)
  level: none
  perspective: perspective:students
  mood: gerund
  readFrom: "text layer"
  appliesTo: "framework for student access, retention, attainment and progression"
  addressee: provider
  verbs: ["Delivering", "fostering"]
  about: "inclusive teaching and belonging through participation"
  themes: ["none"]
  paraphrase: "Teaching is inclusive, and belonging grows from active taking part in and around the course."
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- statement: advancehe/arap-2024/frame.responsibility
  forPractitioner: { text: "Treat student success as your responsibility too, whatever your role, and work with others who share it.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "You share responsibility for your own success, alongside the staff and leaders who support you.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as shared responsibility across roles, force must from \"responsibility\". Note that students are named among those responsible. Do not single out one group."
  author-agent-dialogue: "Raise it when success is treated as one team's job. Ask: \"What part of this is yours to do?\""
- statement: advancehe/arap-2024/frame.providers
  forPractitioner: { text: "Open entry to everyone who could benefit, and give every student the help they need to do their best.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty laid on institutions", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the framing duty of the model, force must. Note its three grounds: legal, ethical and economic. Do not state particular laws."
  author-agent-dialogue: "Raise it when access is treated as optional. Ask: \"What does this institution owe applicants who could benefit?\""
- statement: advancehe/arap-2024/frame.institution
  forPractitioner: { text: "Align strategy and policy with the institution's vision, and support staff with the skills and time to carry them out.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present as the institution perspective's framing line, force must from \"needs to\". Link it to strategic approaches to teaching excellence and staff recruitment and development."
  author-agent-dialogue: "Raise it in strategy work. Ask: \"Does this policy follow from the vision, and can staff deliver it?\""
- statement: advancehe/arap-2024/frame.students
  forPractitioner: { text: "Combine practical help, such as money and accessible resources, with academic and personal support; none of these alone is enough.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition met by the institution and its staff", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a requirement for retention and attainment, force must from \"requires\". Note it names a combination, not any single service."
  author-agent-dialogue: "Raise it when one form of support is expected to do everything. Ask: \"Which kinds of support does this student have, and which are missing?\""
- statement: advancehe/arap-2024/use.institution.1
  forPractitioner: { text: "Use the model to set out a clear vision and mission and to check that strategies and policies follow from them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "One of four institution uses; force describes (gerund). Link to frame.institution."
  author-agent-dialogue: "Raise it with leaders. Ask: \"Can staff state the vision, and do policies match it?\""
- statement: advancehe/arap-2024/use.institution.2
  forPractitioner: { text: "Use the model to plan spaces that invite group work and informal contact.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). Link to the learning spaces component."
  author-agent-dialogue: "Raise it in estates or timetabling discussions. Ask: \"Where can students work together here?\""
- statement: advancehe/arap-2024/use.institution.3
  forPractitioner: { text: "Use data and technology to spot students who need help and to prompt staff to act.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). Link to learning analytics and early intervention."
  author-agent-dialogue: "Raise it in discussion of data. Ask: \"What does a flag lead to, and how fast?\""
- statement: advancehe/arap-2024/use.institution.4
  forPractitioner: { text: "Direct staff effort and development towards student achievement, wellbeing and readiness for work.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). Note the three foci; link to staff recruitment and development, mental health and wellbeing, and career services."
  author-agent-dialogue: "Raise it in workload or development planning. Ask: \"Where does staff time go, and does it reach these three aims?\""
- statement: advancehe/arap-2024/use.educators.1
  forPractitioner: { text: "Map your role against outreach, admissions, academic and personal support, mental health and careers, and see where you contribute.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). It summarises the Educators+ remit given on p. 8."
  author-agent-dialogue: "Raise it when staff ask where they fit. Ask: \"Which of these areas does your role touch?\""
- statement: advancehe/arap-2024/use.educators.2
  forPractitioner: { text: "Build belonging through pre-arrival groups, working with students and peer learning.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). Link to pre-entry learning communities and peer/learning communities."
  author-agent-dialogue: "Raise it in induction planning. Ask: \"Where do students first meet each other and staff?\""
- statement: advancehe/arap-2024/use.educators.3
  forPractitioner: { text: "Develop curricula and materials that reflect diverse experience and use them to open discussion.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). Link to the inclusive curriculum component."
  author-agent-dialogue: "Raise it in curriculum review. Ask: \"Whose experience does this material reflect?\""
- statement: advancehe/arap-2024/use.educators.4
  forPractitioner: { text: "Offer varied assessment with choice and forward-looking feedback.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). Link to student choice, constructive feedback and diverse and inclusive assessment."
  author-agent-dialogue: "Raise it in assessment design. Ask: \"Where is the choice, and when is feedback used?\""
- statement: advancehe/arap-2024/use.students.1
  forPractitioner: { text: "Provide practical help and inclusive settings at each move: into study, through it and beyond it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect practical help and a welcoming setting as you start, move through and finish your studies.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). Listed under Students but voiced as provision for them. Link to the transition theme."
  author-agent-dialogue: "Raise it at points of change. Ask: \"What will help you through this next move?\""
- statement: advancehe/arap-2024/use.students.2
  forPractitioner: { text: "Run outreach that connects prospective students with the institution, course and future peers.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect chances to connect with your university, course and future classmates before you start.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). Link to outreach activities and early engagement."
  author-agent-dialogue: "Raise it in outreach planning. Ask: \"Who will prospective students meet?\""
- statement: advancehe/arap-2024/use.students.3
  forPractitioner: { text: "Provide money help, accessible resources and academic and personal support together.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect money help, resources you can use and academic and personal support.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). It restates frame.students in list form."
  author-agent-dialogue: "Raise it when support seems patchy. Ask: \"Which kind of help do you need most?\""
- statement: advancehe/arap-2024/use.students.4
  forPractitioner: { text: "Teach inclusively and build belonging by inviting students to take part in and beyond the course.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect inclusive teaching and chances to take part in and beyond your course.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes (gerund). Link to sense of belonging."
  author-agent-dialogue: "Raise it when students feel outside the course. Ask: \"Where could you take part beyond class?\""
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
- { id: theme:access-retention-attainment-progression, role: carries, carriedIn: ["what-is", "stages", "who-for", "why", "institution", "educators", "students", "use"], basis: "stated: the model's whole subject (title; D1, p. 2)" }
- { id: theme:wellbeing, role: carries, carriedIn: ["what-is", "educators", "institution.dial", "use"], basis: "stated: \"overall wellbeing\" (p. 2), \"mental health and wellbeing support\" (p. 8), a segment label (p. 7)" }
- { id: theme:employability, role: carries, carriedIn: ["stages", "why", "institution.dial", "educators.dial", "students.dial", "use"], basis: "stated: progression to \"further study or employment\" (p. 2), professional skills and competencies (p. 4), \"career readiness\" (p. 12), the employability framework named (p. 12)" }
- { id: theme:assessment, role: carries, carriedIn: ["educators", "educators.dial", "use"], basis: "stated: diverse assessments, student choice and feedback (p. 8), segment labels (p. 9)" }
- { id: theme:student-partnership, role: carries, carriedIn: ["who-for", "students.dial"], basis: "stated: \"the engagement of students as partners\" (p. 3); segment Co-creation and Partnership (p. 11)" }
- { id: theme:accessibility, role: carries, carriedIn: ["institution", "students", "students.dial"], basis: "stated: \"assistive technologies\" (p. 6), \"resource accessibility\" (p. 10), segment Accessible Information (p. 11)" }
- { id: theme:digital, role: carries, carriedIn: ["institution", "institution.dial", "students.dial", "use"], basis: "stated: learning analytics, \"access to devices\" (p. 6), \"data and technology\" (p. 12), segment Access to Digital Tools and Devices (p. 11)" }
- { id: theme:flexible-learning, role: carries, carriedIn: ["institution.dial"], basis: "stated: segment Flexible Learning Models (p. 7)" }
- { id: theme:edi, role: carries, carriedIn: ["why", "institution.dial", "educators.dial", "students.dial"], basis: "inferred: widening participation, social mobility and awarding gaps (p. 4) and contextual admissions; EDI is not named outside the back cover (Part E)" }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: partOf, target: "advancehe-student-success-frameworks-2024", note: "Advance HE Student Success Frameworks; the three-perspective structure is shared by the series (D1, p. 5)" }
- { rel: partOf, target: "std:doc:advancehe-enhancing-student-success-2024-model", note: "the series overview names access, retention, attainment and progression as one of its areas" }
- { rel: modelledAs, target: "ing:doc:access-retention-attainment-progression-framework-advance-he-2024", note: "the same source run as theory with a dialogue layer (ing run 0139); read for consistency, not used as a source" }
- { rel: alignsWith, target: "std:doc:advancehe-psf-dimensions-2023-framework", note: "stated: ten PSF 2023 dimensions named as particularly relevant (M5)" }
- { rel: pointsTo, target: "std:doc:advancehe-enhancing-assessment-2024-model", note: "named on p. 12 (\"Enhancing Assessment\"); proposed id, not yet ingested" }
- { rel: pointsTo, target: "std:doc:advancehe-embedding-employability-2024-model", note: "named on p. 12 (\"Employability\"); proposed id, not yet ingested" }
- { rel: pointsTo, target: "std:doc:advancehe-inclusive-learning-teaching-2024-model", note: "p. 12 names \"Inclusive Curriculum\"; the nearest held title (Part E)" }
- { rel: siblingOf, target: "std:doc:advancehe-internationalising-higher-education-2024-model", note: "reserved id; held, not yet ingested" }
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
  - { id: perspective:institution, label: "Institution", page: 7, segments: 16, openSegments: 0 }
  - { id: perspective:educators, label: "Educators+", page: 9, segments: 16, openSegments: 0, note: "labelled \"Educators+\" throughout (pp. 5, 8, 12); the prose glosses it as academics and professional services staff (p. 8)" }
  - { id: perspective:students, label: "Students", page: 11, segments: 17, openSegments: 0 }
groups:
  - { id: stage:access, kind: stage, label: "Access", axis: all, ring: inner, segments: 12, perAxis: {"perspective:institution": 4, "perspective:educators": 4, "perspective:students": 4}, readFrom: "figure image" }
  - { id: stage:retention, kind: stage, label: "Retention", axis: all, ring: inner, segments: 13, perAxis: {"perspective:institution": 4, "perspective:educators": 4, "perspective:students": 5}, readFrom: "figure image" }
  - { id: stage:attainment, kind: stage, label: "Attainment", axis: all, ring: inner, segments: 13, perAxis: {"perspective:institution": 4, "perspective:educators": 5, "perspective:students": 4}, readFrom: "figure image" }
  - { id: stage:progression, kind: stage, label: "Progression", axis: all, ring: inner, segments: 11, perAxis: {"perspective:institution": 4, "perspective:educators": 3, "perspective:students": 4}, readFrom: "figure image" }
use: "as a prompt for all staff involved in the student experience, connecting what learners need to the support in place, and to be read beside the series' assessment, employability and inclusive curriculum frameworks; each perspective has four uses (S4 use.*) (D1, p. 12)"
```

### M2 Components
<!-- label: both; status: drafted; basis: primary. In the figure's order (Part E). -->
```yaml
- id: advancehe/arap-2024/institution.financial-support
  label: "Financial Support"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:access, order: 1, page: 7 }
  explainedBy:
    - { span: { start: 822, end: 898 }, source: "Access: Ensuring everyone who could benefit from higher education can do so.", link: inferred, page: 2 }
    - { span: { start: 7748, end: 7933 }, source: "Securing retention and attainment for all students requires a combination of practical support, including financial assistance and resource accessibility, academic and pastoral support.", link: inferred, page: 10 }
  conditionType: service
  actor: institution
  about: "money help so cost is no barrier to entry"
  paraphrase: "The institution offers financial help so that the cost of study does not stop people who could benefit from coming in."
  themes: ["theme:targeted-support", "theme:access-retention-attainment-progression", "theme:edi"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.targeted-outreach
  label: "Targeted Outreach Activities"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:access, order: 2, page: 7 }
  explainedBy:
    - { span: { start: 2212, end: 2350 }, source: "Access encompasses targeted outreach activity, personalised pre-entry information and engagement as well as efficient admission processes.", link: stated, page: 4 }
  conditionType: practice
  actor: institution
  about: "outreach aimed at under-represented groups"
  paraphrase: "The institution reaches out to groups who are less likely to enter higher education, aiming its effort where it is most needed."
  themes: ["theme:transition", "theme:access-retention-attainment-progression", "theme:edi"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.contextual-admissions
  label: "Contextual Admissions"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:access, order: 3, page: 7 }
  explainedBy:
    - { span: { start: 2212, end: 2350 }, source: "Access encompasses targeted outreach activity, personalised pre-entry information and engagement as well as efficient admission processes.", link: inferred, page: 4 }
    - { span: { start: 3442, end: 3603 }, source: "Typically, institutions have broader missions including social mobility, widening participation, closing awarding gaps and alignment with governmental priorities", link: inferred, page: 4 }
  conditionType: process
  actor: institution
  about: "admissions that weigh the applicant's circumstances"
  paraphrase: "Admission decisions take account of the circumstances in which an applicant achieved their results, not the grades alone."
  themes: ["theme:contextual-adaptation", "theme:access-retention-attainment-progression", "theme:edi"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.application-admission
  label: "Application and Admission Processes"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:access, order: 4, page: 7 }
  explainedBy:
    - { span: { start: 2212, end: 2350 }, source: "Access encompasses targeted outreach activity, personalised pre-entry information and engagement as well as efficient admission processes.", link: stated, page: 4 }
  conditionType: process
  actor: institution
  about: "clear and efficient application and entry"
  paraphrase: "Applying and being admitted is clear and efficient, so that the process itself does not put people off."
  themes: ["theme:transition", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.learning-analytics
  label: "Learning Analytics"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:retention, order: 5, page: 7 }
  explainedBy:
    - { span: { start: 4873, end: 5050 }, source: "Attendance systems and learning analytics allow timely and targeted interventions, including academic or pastoral support, providing assistive technologies or access to devices.", link: stated, page: 6 }
    - { span: { start: 9742, end: 9823 }, source: "Using data and technology effectively to prompt intervention to support students.", link: stated, page: 12 }
  conditionType: structure
  actor: institution
  about: "using data to spot students who need help"
  paraphrase: "The institution uses data on attendance and engagement to notice early when a student may be struggling, so that someone can act."
  themes: ["theme:targeted-support", "theme:access-retention-attainment-progression", "theme:digital"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.peer-learning-systems
  label: "Peer Learning Systems"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:retention, order: 6, page: 7 }
  explainedBy:
    - { span: { start: 1220, end: 1412 }, source: "They each depend on fostering a sense of belonging and actively engaging students with their programme and the wider institution, enabling students to thrive throughout their higher education.", link: inferred, page: 2 }
    - { span: { start: 5857, end: 6040 }, source: "Outreach programmes and the development of pre-entry learning communities initiate the sense of belonging, which can be built upon through staff-student and peer learning communities.", link: inferred, page: 8 }
  conditionType: structure
  actor: institution
  about: "structured schemes for students learning together"
  paraphrase: "The institution sets up and sustains schemes in which students learn with and from each other."
  themes: ["theme:belonging-mattering", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.mental-health-wellbeing
  label: "Student Mental Health and Wellbeing"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:retention, order: 7, page: 7 }
  explainedBy:
    - { span: { start: 1413, end: 1548 }, source: "This holistic approach not only focuses on academic success but also on the overall wellbeing and personal development of the students.", link: inferred, page: 2 }
    - { span: { start: 9824, end: 9937 }, source: "Focusing skilled academic and professional services staff on student achievement, wellbeing and career readiness.", link: stated, page: 12 }
    - { span: { start: 6551, end: 6784 }, source: "Depending on the structure and size of the institution, specific roles and responsibilities will be shared, but can include outreach, admissions, academic and pastoral support, mental health and wellbeing support, and careers advice.", link: stated, page: 8 }
  conditionType: service
  actor: institution
  about: "services for students' mental health and wellbeing"
  paraphrase: "The institution provides and resources mental health and wellbeing support so that students can stay on and do well."
  themes: ["theme:compassion", "theme:access-retention-attainment-progression", "theme:wellbeing"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.learning-spaces
  label: "Learning Spaces"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:retention, order: 8, page: 7 }
  explainedBy:
    - { span: { start: 5051, end: 5232 }, source: "Inclusive learning spaces, welcome activities and fostering a strong sense of belonging further contribute to an environment where students can thrive and achieve their aspirations.", link: stated, page: 6 }
    - { span: { start: 9661, end: 9741 }, source: "Creating learning spaces that encourage collaboration and informal interactions.", link: stated, page: 12 }
  conditionType: environment
  actor: institution
  about: "physical and shared spaces that welcome students"
  paraphrase: "Learning spaces are inclusive and designed for students to work together and meet informally."
  themes: ["theme:belonging-mattering", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.commitment-full-potential
  label: "Commitment to All Students to Reach Their Full Potential"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:attainment, order: 9, page: 7 }
  explainedBy:
    - { span: { start: 1691, end: 1904 }, source: "HE providers have a legal, ethical and economic responsibility to ensure they widen access to all who may benefit from higher education and to put support in place for all students to achieve their full potential.", link: stated, page: 4 }
    - { span: { start: 4560, end: 4716 }, source: "The institution plays a leading role in creating the vision, mission and culture of shared responsibility that ensures successful outcomes for all students.", link: inferred, page: 6 }
    - { span: { start: 2760, end: 2857 }, source: "These elements, often overlooked in outcome measurements, are critical for closing awarding gaps.", link: inferred, page: 4 }
  conditionType: culture
  actor: institution
  about: "expecting and enabling every student to do their best"
  paraphrase: "The institution commits to every student achieving all they can, and organises itself around that commitment rather than accepting gaps between groups."
  themes: ["theme:whole-institution", "theme:access-retention-attainment-progression", "theme:edi"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.flexible-learning-models
  label: "Flexible Learning Models"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:attainment, order: 10, page: 7 }
  explainedBy:
    - { span: { start: 2618, end: 2759 }, source: "on various factors, including their individual experience, engagement level, sense of belonging and opportunities to cultivate self-efficacy.", link: inferred, page: 4 }
  conditionType: structure
  actor: institution
  about: "study patterns that fit students' lives"
  paraphrase: "The institution offers ways of studying, in time, place and pace, that fit the lives of the students it admits."
  themes: ["theme:contextual-adaptation", "theme:access-retention-attainment-progression", "theme:flexible-learning"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.staff-recruitment-development
  label: "Staff Recruitment and Development"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:attainment, order: 11, page: 7 }
  explainedBy:
    - { span: { start: 4717, end: 4872 }, source: "Vision needs to be aligned with a coherent set of strategies and policies that skilled academic and professional services staff are supported to implement.", link: inferred, page: 6 }
    - { span: { start: 9824, end: 9937 }, source: "Focusing skilled academic and professional services staff on student achievement, wellbeing and career readiness.", link: inferred, page: 12 }
  conditionType: structure
  actor: institution
  about: "hiring and developing skilled staff"
  paraphrase: "The institution recruits, develops and supports staff with the skills to help students succeed."
  themes: ["theme:whole-institution", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.teaching-excellence
  label: "Strategic Approaches to Teaching Excellence"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:attainment, order: 12, page: 7 }
  explainedBy:
    - { span: { start: 4717, end: 4872 }, source: "Vision needs to be aligned with a coherent set of strategies and policies that skilled academic and professional services staff are supported to implement.", link: inferred, page: 6 }
    - { span: { start: 9560, end: 9646 }, source: "Articulating a clear vision and mission aligned with coherent strategies and policies.", link: inferred, page: 12 }
  conditionType: structure
  actor: institution
  about: "strategy that raises the quality of teaching"
  paraphrase: "The institution has a coherent strategy for good teaching, tied to its vision and backed by policy."
  themes: ["theme:whole-institution", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.lifelong-learning
  label: "Facilitate Lifelong Learning"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:progression, order: 13, page: 7 }
  explainedBy:
    - { span: { start: 1064, end: 1144 }, source: "Progression: Supporting students as they move on to further study or employment.", link: inferred, page: 2 }
  conditionType: structure
  actor: institution
  about: "routes back into learning after graduation"
  paraphrase: "The institution makes it possible for people to keep learning after their first award, including by returning to study."
  themes: ["theme:transition", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.contextual-pg-admissions
  label: "Contextual Postgraduate Admissions"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:progression, order: 14, page: 7 }
  explainedBy:
    - { span: { start: 1064, end: 1144 }, source: "Progression: Supporting students as they move on to further study or employment.", link: inferred, page: 2 }
    - { span: { start: 3442, end: 3603 }, source: "Typically, institutions have broader missions including social mobility, widening participation, closing awarding gaps and alignment with governmental priorities", link: inferred, page: 4 }
  conditionType: process
  actor: institution
  about: "postgraduate entry that weighs circumstance"
  paraphrase: "Admission to postgraduate study takes account of the circumstances in which applicants achieved their first degree."
  themes: ["theme:contextual-adaptation", "theme:transition", "theme:access-retention-attainment-progression", "theme:edi"]
  sameLabelAs: none
- id: advancehe/arap-2024/institution.employer-engagement
  label: "Employer Engagement"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:progression, order: 15, page: 7 }
  explainedBy:
    - { span: { start: 2858, end: 3036 }, source: "Progression and positive exit paths are dependent on the development of professional skills and competencies within the curriculum and through extra and co-curricular activities.", link: inferred, page: 4 }
    - { span: { start: 9824, end: 9937 }, source: "Focusing skilled academic and professional services staff on student achievement, wellbeing and career readiness.", link: inferred, page: 12 }
  conditionType: relationship
  actor: institution
  about: "working relationships with employers"
  paraphrase: "The institution builds relationships with employers so that students can meet them, learn from them and move into work."
  themes: ["theme:career-development", "theme:access-retention-attainment-progression", "theme:employability"]
  sameLabelAs: advancehe/arap-2024/educators.employer-engagement
- id: advancehe/arap-2024/institution.career-services
  label: "Career Services"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: stage:progression, order: 16, page: 7 }
  explainedBy:
    - { span: { start: 6551, end: 6784 }, source: "Depending on the structure and size of the institution, specific roles and responsibilities will be shared, but can include outreach, admissions, academic and pastoral support, mental health and wellbeing support, and careers advice.", link: stated, page: 8 }
    - { span: { start: 9824, end: 9937 }, source: "Focusing skilled academic and professional services staff on student achievement, wellbeing and career readiness.", link: inferred, page: 12 }
  conditionType: service
  actor: institution
  about: "careers advice and support"
  paraphrase: "The institution provides careers services that help students plan and make their next step."
  themes: ["theme:career-development", "theme:access-retention-attainment-progression", "theme:employability"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.bridging-programmes
  label: "Bridging Programmes"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:access, order: 1, page: 9 }
  explainedBy:
    - { span: { start: 5857, end: 6040 }, source: "Outreach programmes and the development of pre-entry learning communities initiate the sense of belonging, which can be built upon through staff-student and peer learning communities.", link: inferred, page: 8 }
    - { span: { start: 822, end: 898 }, source: "Access: Ensuring everyone who could benefit from higher education can do so.", link: inferred, page: 2 }
  conditionType: practice
  actor: educator
  about: "preparatory courses before entry"
  paraphrase: "Staff run preparatory programmes that help people get ready for study and close gaps before they start."
  themes: ["theme:transition", "theme:access-retention-attainment-progression", "theme:edi"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.outreach-activities
  label: "Outreach Activities"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:access, order: 2, page: 9 }
  explainedBy:
    - { span: { start: 5857, end: 6040 }, source: "Outreach programmes and the development of pre-entry learning communities initiate the sense of belonging, which can be built upon through staff-student and peer learning communities.", link: stated, page: 8 }
    - { span: { start: 8791, end: 8909 }, source: "Supporting students through outreach, admissions, academic/pastoral support, mental health services and career advice.", link: stated, page: 13 }
  conditionType: practice
  actor: educator
  about: "staff taking part in outreach"
  paraphrase: "Staff take part in outreach that introduces higher education and their subject to people who might not otherwise consider it."
  themes: ["theme:transition", "theme:access-retention-attainment-progression"]
  sameLabelAs: advancehe/arap-2024/students.outreach-activities
- id: advancehe/arap-2024/educators.engagement-applicants
  label: "Engagement with Applicants"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:access, order: 3, page: 9 }
  explainedBy:
    - { span: { start: 2212, end: 2350 }, source: "Access encompasses targeted outreach activity, personalised pre-entry information and engagement as well as efficient admission processes.", link: inferred, page: 4 }
    - { span: { start: 8791, end: 8909 }, source: "Supporting students through outreach, admissions, academic/pastoral support, mental health services and career advice.", link: inferred, page: 13 }
  conditionType: relationship
  actor: educator
  about: "keeping in touch with applicants"
  paraphrase: "Staff keep in contact with applicants between offer and arrival, so that they feel expected and know what to do."
  themes: ["theme:transition", "theme:belonging-mattering", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.pre-entry-communities
  label: "Pre-entry Learning Communities"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:access, order: 4, page: 9 }
  explainedBy:
    - { span: { start: 5857, end: 6040 }, source: "Outreach programmes and the development of pre-entry learning communities initiate the sense of belonging, which can be built upon through staff-student and peer learning communities.", link: stated, page: 8 }
    - { span: { start: 9943, end: 10056 }, source: "Fostering belonging through pre-entry learning communities, staff-student collaboration and peer learning groups.", link: stated, page: 13 }
  conditionType: relationship
  actor: educator
  about: "learning groups formed before arrival"
  paraphrase: "Staff set up learning communities before students arrive, so that belonging starts before the first day."
  themes: ["theme:belonging-mattering", "theme:transition", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.inclusive-curriculum
  label: "Inclusive Curriculum"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:retention, order: 5, page: 9 }
  explainedBy:
    - { span: { start: 6041, end: 6209 }, source: "Inclusive curricula and course materials that reflect diverse experiences validate student identities and provide a space for positive challenge, debate and engagement.", link: stated, page: 8 }
    - { span: { start: 10057, end: 10178 }, source: "Developing inclusive curricula and materials reflecting diverse experiences which promote positive engagement and debate.", link: stated, page: 13 }
  conditionType: practice
  actor: educator
  about: "curriculum and materials that reflect diverse experience"
  paraphrase: "Staff design curricula and materials that reflect diverse experiences, so that students see themselves in what they study and can engage critically."
  themes: ["theme:anticipating-difference", "theme:authenticity", "theme:access-retention-attainment-progression", "theme:edi"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.peer-learning-communities
  label: "Peer/Learning Communities"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:retention, order: 6, page: 9 }
  explainedBy:
    - { span: { start: 5857, end: 6040 }, source: "Outreach programmes and the development of pre-entry learning communities initiate the sense of belonging, which can be built upon through staff-student and peer learning communities.", link: stated, page: 8 }
    - { span: { start: 9943, end: 10056 }, source: "Fostering belonging through pre-entry learning communities, staff-student collaboration and peer learning groups.", link: stated, page: 13 }
  conditionType: relationship
  actor: educator
  about: "communities of staff and students learning together"
  paraphrase: "Staff build learning communities among students and between students and staff, so that belonging keeps growing."
  themes: ["theme:belonging-mattering", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.student-centred-pedagogy
  label: "Student-centred Pedagogy"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:retention, order: 7, page: 9 }
  explainedBy:
    - { span: { start: 8419, end: 8597 }, source: "This student-centred framework identifies the practical support and learning environment necessary for students’ successful transition into, through, and beyond higher education.", link: inferred, page: 10 }
    - { span: { start: 1220, end: 1412 }, source: "They each depend on fostering a sense of belonging and actively engaging students with their programme and the wider institution, enabling students to thrive throughout their higher education.", link: inferred, page: 2 }
  conditionType: practice
  actor: educator
  about: "teaching built around students' needs and activity"
  paraphrase: "Staff teach in ways that start from students' needs and put students' own activity at the centre."
  themes: ["theme:anticipating-difference", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.early-intervention
  label: "Early Intervention"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:retention, order: 8, page: 9 }
  explainedBy:
    - { span: { start: 4873, end: 5050 }, source: "Attendance systems and learning analytics allow timely and targeted interventions, including academic or pastoral support, providing assistive technologies or access to devices.", link: inferred, page: 6 }
    - { span: { start: 9742, end: 9823 }, source: "Using data and technology effectively to prompt intervention to support students.", link: inferred, page: 12 }
  conditionType: practice
  actor: educator
  about: "acting early when a student struggles"
  paraphrase: "Staff notice early signs that a student is struggling and act before problems become serious."
  themes: ["theme:targeted-support", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.authentic-assessment
  label: "Authentic Assessment"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:attainment, order: 9, page: 9 }
  explainedBy:
    - { span: { start: 6210, end: 6339 }, source: "Providing diverse assessments that incorporate student choice and constructive feedback will help enable all students to succeed.", link: inferred, page: 8 }
  conditionType: practice
  actor: educator
  about: "assessment that mirrors real tasks"
  paraphrase: "Staff set assessments that resemble the tasks people do in the subject or at work, so that students see their point."
  themes: ["theme:authenticity", "theme:access-retention-attainment-progression", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.graduate-attributes
  label: "Develop Graduate Attributes"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:attainment, order: 10, page: 9 }
  explainedBy:
    - { span: { start: 2858, end: 3036 }, source: "Progression and positive exit paths are dependent on the development of professional skills and competencies within the curriculum and through extra and co-curricular activities.", link: inferred, page: 4 }
  conditionType: practice
  actor: educator
  about: "building broad graduate capabilities"
  paraphrase: "Staff build the broad capabilities graduates need, such as communication and teamwork, into the course."
  themes: ["theme:career-development", "theme:access-retention-attainment-progression", "theme:employability"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.student-choice
  label: "Student Choice"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:attainment, order: 11, page: 9 }
  explainedBy:
    - { span: { start: 6210, end: 6339 }, source: "Providing diverse assessments that incorporate student choice and constructive feedback will help enable all students to succeed.", link: stated, page: 8 }
    - { span: { start: 10179, end: 10286 }, source: "Offering diverse assessments with student choice and constructive feedback to enable all students to excel.", link: stated, page: 13 }
  conditionType: practice
  actor: educator
  about: "choice in how students are assessed"
  paraphrase: "Staff give students meaningful choices, above all in assessment, so that each can show what they know in a way that suits them."
  themes: ["theme:agency-self-actualisation", "theme:access-retention-attainment-progression", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.constructive-feedback
  label: "Constructive Feedback"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:attainment, order: 12, page: 9 }
  explainedBy:
    - { span: { start: 6210, end: 6339 }, source: "Providing diverse assessments that incorporate student choice and constructive feedback will help enable all students to succeed.", link: stated, page: 8 }
    - { span: { start: 10179, end: 10286 }, source: "Offering diverse assessments with student choice and constructive feedback to enable all students to excel.", link: stated, page: 13 }
  conditionType: practice
  actor: educator
  about: "feedback that helps students improve"
  paraphrase: "Staff give feedback that tells students how to improve, in time for them to use it."
  themes: ["theme:agency-self-actualisation", "theme:access-retention-attainment-progression", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.diverse-inclusive-assessment
  label: "Diverse and Inclusive Assessment"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:attainment, order: 13, page: 9 }
  explainedBy:
    - { span: { start: 6210, end: 6339 }, source: "Providing diverse assessments that incorporate student choice and constructive feedback will help enable all students to succeed.", link: stated, page: 8 }
    - { span: { start: 10179, end: 10286 }, source: "Offering diverse assessments with student choice and constructive feedback to enable all students to excel.", link: stated, page: 13 }
  conditionType: practice
  actor: educator
  about: "a range of assessment that fairly suits all students"
  paraphrase: "Staff use a range of assessment types designed so that every student has a fair chance to show what they can do."
  themes: ["theme:anticipating-difference", "theme:access-retention-attainment-progression", "theme:assessment", "theme:edi"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.professional-competencies
  label: "Professional Competencies"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:progression, order: 14, page: 9 }
  explainedBy:
    - { span: { start: 2858, end: 3036 }, source: "Progression and positive exit paths are dependent on the development of professional skills and competencies within the curriculum and through extra and co-curricular activities.", link: stated, page: 4 }
  conditionType: practice
  actor: educator
  about: "skills for professional practice in the curriculum"
  paraphrase: "Staff build the skills and competencies of professional practice into the curriculum."
  themes: ["theme:career-development", "theme:access-retention-attainment-progression", "theme:employability"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.professional-experiences
  label: "Professional Experiences"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:progression, order: 15, page: 9 }
  explainedBy:
    - { span: { start: 2858, end: 3036 }, source: "Progression and positive exit paths are dependent on the development of professional skills and competencies within the curriculum and through extra and co-curricular activities.", link: inferred, page: 4 }
  conditionType: practice
  actor: educator
  about: "placements and practice experience"
  paraphrase: "Staff arrange experiences of professional practice, such as placements and live projects, for students."
  themes: ["theme:career-development", "theme:authenticity", "theme:access-retention-attainment-progression", "theme:employability"]
  sameLabelAs: none
- id: advancehe/arap-2024/educators.employer-engagement
  label: "Employer Engagement"
  span: none   # figure image, p. 9
  position: { axis: perspective:educators, group: stage:progression, order: 16, page: 9 }
  explainedBy:
    - { span: { start: 2858, end: 3036 }, source: "Progression and positive exit paths are dependent on the development of professional skills and competencies within the curriculum and through extra and co-curricular activities.", link: inferred, page: 4 }
    - { span: { start: 1064, end: 1144 }, source: "Progression: Supporting students as they move on to further study or employment.", link: inferred, page: 2 }
  conditionType: relationship
  actor: educator
  about: "employers involved in teaching"
  paraphrase: "Staff involve employers in teaching and course design, so that students meet the world of work through their course."
  themes: ["theme:career-development", "theme:access-retention-attainment-progression", "theme:employability"]
  sameLabelAs: advancehe/arap-2024/institution.employer-engagement
- id: advancehe/arap-2024/students.information-advice
  label: "Information, Advice and Guidance"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:access, order: 1, page: 11 }
  explainedBy:
    - { span: { start: 2212, end: 2350 }, source: "Access encompasses targeted outreach activity, personalised pre-entry information and engagement as well as efficient admission processes.", link: inferred, page: 4 }
    - { span: { start: 8419, end: 8597 }, source: "This student-centred framework identifies the practical support and learning environment necessary for students’ successful transition into, through, and beyond higher education.", link: inferred, page: 10 }
  conditionType: service
  actor: institution
  about: "clear information and advice before entry"
  paraphrase: "Prospective students get clear, personal information and advice to choose and prepare for study."
  themes: ["theme:transition", "theme:hidden-curriculum", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.outreach-activities
  label: "Outreach Activities"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:access, order: 2, page: 11 }
  explainedBy:
    - { span: { start: 7578, end: 7747 }, source: "Access is supported through outreach activities that encourage applications and support early engagement with the institution, their course and their prospective cohort.", link: stated, page: 10 }
    - { span: { start: 10399, end: 10496 }, source: "Delivering outreach activities promoting early engagement with the institution, course and peers.", link: stated, page: 13 }
  conditionType: practice
  actor: institution
  about: "outreach as students meet it"
  paraphrase: "Prospective students take part in outreach that encourages them to apply and starts their engagement early."
  themes: ["theme:transition", "theme:access-retention-attainment-progression"]
  sameLabelAs: advancehe/arap-2024/educators.outreach-activities
- id: advancehe/arap-2024/students.early-engagement
  label: "Early Engagement with Cohort and Institution"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:access, order: 3, page: 11 }
  explainedBy:
    - { span: { start: 7578, end: 7747 }, source: "Access is supported through outreach activities that encourage applications and support early engagement with the institution, their course and their prospective cohort.", link: stated, page: 10 }
    - { span: { start: 2351, end: 2517 }, source: "Establishing students’ sense of belonging and mattering early in their engagement with the institution will enhance the likelihood of them completing their programme.", link: inferred, page: 4 }
  conditionType: relationship
  actor: all
  about: "connecting with peers and the institution early"
  paraphrase: "Students connect with their future peers, course and institution before and soon after they arrive."
  themes: ["theme:transition", "theme:belonging-mattering", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.access-financial-support
  label: "Access to Financial Support"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:access, order: 4, page: 11 }
  explainedBy:
    - { span: { start: 7748, end: 7933 }, source: "Securing retention and attainment for all students requires a combination of practical support, including financial assistance and resource accessibility, academic and pastoral support.", link: stated, page: 10 }
    - { span: { start: 10497, end: 10582 }, source: "Providing financial assistance, resource accessibility and academic/pastoral support.", link: stated, page: 13 }
  conditionType: service
  actor: institution
  about: "students reaching the money help they need"
  paraphrase: "Students can find and obtain the financial support they need to start and stay in study."
  themes: ["theme:targeted-support", "theme:access-retention-attainment-progression", "theme:edi"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.remedial-support
  label: "Remedial Support"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:retention, order: 5, page: 11 }
  explainedBy:
    - { span: { start: 7748, end: 7933 }, source: "Securing retention and attainment for all students requires a combination of practical support, including financial assistance and resource accessibility, academic and pastoral support.", link: inferred, page: 10 }
    - { span: { start: 903, end: 986 }, source: "Retention: Supporting all students to successfully complete their chosen programme.", link: inferred, page: 2 }
  conditionType: service
  actor: all
  about: "help to catch up"
  paraphrase: "Students who fall behind or lack a skill can get help to catch up."
  themes: ["theme:targeted-support", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.pastoral-support
  label: "Pastoral Support"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:retention, order: 6, page: 11 }
  explainedBy:
    - { span: { start: 7748, end: 7933 }, source: "Securing retention and attainment for all students requires a combination of practical support, including financial assistance and resource accessibility, academic and pastoral support.", link: stated, page: 10 }
    - { span: { start: 10497, end: 10582 }, source: "Providing financial assistance, resource accessibility and academic/pastoral support.", link: stated, page: 13 }
  conditionType: service
  actor: all
  about: "personal support beyond the academic"
  paraphrase: "Students can get personal support with matters outside their studies that affect them."
  themes: ["theme:compassion", "theme:access-retention-attainment-progression", "theme:wellbeing"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.sense-of-belonging
  label: "Sense of Belonging"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:retention, order: 7, page: 11 }
  explainedBy:
    - { span: { start: 7934, end: 8089 }, source: "Inclusive teaching and learning practices ensure all students feel valued and included and engenders a sense of belonging within the educational community.", link: stated, page: 10 }
    - { span: { start: 2351, end: 2517 }, source: "Establishing students’ sense of belonging and mattering early in their engagement with the institution will enhance the likelihood of them completing their programme.", link: stated, page: 4 }
    - { span: { start: 1220, end: 1412 }, source: "They each depend on fostering a sense of belonging and actively engaging students with their programme and the wider institution, enabling students to thrive throughout their higher education.", link: stated, page: 2 }
  conditionType: relationship
  actor: all
  about: "feeling part of the learning community"
  paraphrase: "Students feel valued, included and part of their learning community."
  themes: ["theme:belonging-mattering", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.accessible-information
  label: "Accessible Information"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:retention, order: 8, page: 11 }
  explainedBy:
    - { span: { start: 7748, end: 7933 }, source: "Securing retention and attainment for all students requires a combination of practical support, including financial assistance and resource accessibility, academic and pastoral support.", link: inferred, page: 10 }
    - { span: { start: 10497, end: 10582 }, source: "Providing financial assistance, resource accessibility and academic/pastoral support.", link: inferred, page: 13 }
  conditionType: environment
  actor: institution
  about: "information every student can use"
  paraphrase: "Information and resources are in forms every student can find, open and use."
  themes: ["theme:anticipating-difference", "theme:access-retention-attainment-progression", "theme:accessibility"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.digital-tools-devices
  label: "Access to Digital Tools and Devices"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:retention, order: 9, page: 11 }
  explainedBy:
    - { span: { start: 4873, end: 5050 }, source: "Attendance systems and learning analytics allow timely and targeted interventions, including academic or pastoral support, providing assistive technologies or access to devices.", link: stated, page: 6 }
  conditionType: service
  actor: institution
  about: "students having the technology to study"
  paraphrase: "Students have the devices, connection and software they need to study, including assistive technology."
  themes: ["theme:targeted-support", "theme:access-retention-attainment-progression", "theme:digital", "theme:accessibility"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.graduate-attributes-competencies
  label: "Graduate Attributes and Competencies"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:attainment, order: 10, page: 11 }
  explainedBy:
    - { span: { start: 2858, end: 3036 }, source: "Progression and positive exit paths are dependent on the development of professional skills and competencies within the curriculum and through extra and co-curricular activities.", link: inferred, page: 4 }
  conditionType: disposition
  actor: student
  about: "students building graduate capabilities"
  paraphrase: "Students develop the broad attributes and competencies they will need after graduation."
  themes: ["theme:career-development", "theme:access-retention-attainment-progression", "theme:employability"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.recognition-achievements
  label: "Recognition of Achievements"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:attainment, order: 11, page: 11 }
  explainedBy:
    - { span: { start: 991, end: 1059 }, source: "Attainment: Recognising and validating the achievements of students.", link: stated, page: 2 }
  conditionType: practice
  actor: all
  about: "students' achievements recognised and valued"
  paraphrase: "Students' achievements, in and beyond their studies, are recognised and valued."
  themes: ["theme:belonging-mattering", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.co-creation-partnership
  label: "Co-creation and Partnership"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:attainment, order: 12, page: 11 }
  explainedBy:
    - { span: { start: 614, end: 817 }, source: "Consideration of the impact of policies, practices and support services from the student perspective, institution-wide collaboration and the engagement of students as partners are key to student success.", link: stated, page: 3 }
    - { span: { start: 8090, end: 8238 }, source: "This can be enhanced through active participation in academic activities, involvement in campus life, and contribution to decision-making processes.", link: inferred, page: 10 }
  conditionType: relationship
  actor: all
  about: "students as partners in their education"
  paraphrase: "Students work with staff as partners, shaping their learning and the decisions that affect it."
  themes: ["theme:student-voice-partnership", "theme:access-retention-attainment-progression", "theme:student-partnership"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.personal-tutoring
  label: "Personal Tutoring"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:attainment, order: 13, page: 11 }
  explainedBy:
    - { span: { start: 7748, end: 7933 }, source: "Securing retention and attainment for all students requires a combination of practical support, including financial assistance and resource accessibility, academic and pastoral support.", link: inferred, page: 10 }
  conditionType: relationship
  actor: educator
  about: "a named tutor who knows the student"
  paraphrase: "Each student has a personal tutor who knows them and supports their academic and personal progress."
  themes: ["theme:belonging-mattering", "theme:compassion", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.agency-self-confidence
  label: "Agency, Self-confidence and Personal Insight"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:progression, order: 14, page: 11 }
  explainedBy:
    - { span: { start: 8239, end: 8406 }, source: "All of which enhance the students’ learning experience and empowers them to take ownership of their education and successfully progress to further study or employment.", link: inferred, page: 10 }
    - { span: { start: 2618, end: 2759 }, source: "on various factors, including their individual experience, engagement level, sense of belonging and opportunities to cultivate self-efficacy.", link: inferred, page: 4 }
  conditionType: disposition
  actor: student
  about: "students owning their learning and next steps"
  paraphrase: "Students gain the agency, confidence and self-knowledge to take charge of their education and next steps."
  themes: ["theme:agency-self-actualisation", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.experiential-work-based
  label: "Experiential, Authentic and Work-based Experiences"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:progression, order: 15, page: 11 }
  explainedBy:
    - { span: { start: 2858, end: 3036 }, source: "Progression and positive exit paths are dependent on the development of professional skills and competencies within the curriculum and through extra and co-curricular activities.", link: inferred, page: 4 }
  conditionType: practice
  actor: all
  about: "learning through real and work-based experience"
  paraphrase: "Students learn through real experiences, including work-based ones, inside and outside the curriculum."
  themes: ["theme:authenticity", "theme:career-development", "theme:access-retention-attainment-progression", "theme:employability"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.networks
  label: "Networks"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:progression, order: 16, page: 11 }
  explainedBy:
    - { span: { start: 8090, end: 8238 }, source: "This can be enhanced through active participation in academic activities, involvement in campus life, and contribution to decision-making processes.", link: inferred, page: 10 }
  conditionType: relationship
  actor: student
  about: "students building useful contacts"
  paraphrase: "Students build networks of peers, staff, alumni and employers that help them move on."
  themes: ["theme:career-development", "theme:access-retention-attainment-progression", "theme:employability"]
  sameLabelAs: none
- id: advancehe/arap-2024/students.progression-paths
  label: "Information on Progression Paths"
  span: none   # figure image, p. 11
  position: { axis: perspective:students, group: stage:progression, order: 17, page: 11 }
  explainedBy:
    - { span: { start: 1064, end: 1144 }, source: "Progression: Supporting students as they move on to further study or employment.", link: inferred, page: 2 }
    - { span: { start: 8239, end: 8406 }, source: "All of which enhance the students’ learning experience and empowers them to take ownership of their education and successfully progress to further study or employment.", link: inferred, page: 10 }
  conditionType: service
  actor: institution
  about: "knowing the routes after study"
  paraphrase: "Students can find clear information about the routes open to them after their course."
  themes: ["theme:transition", "theme:hidden-curriculum", "theme:access-retention-attainment-progression", "theme:employability"]
  sameLabelAs: none
```

### M2a Component audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- component: advancehe/arap-2024/institution.financial-support
  forPractitioner: { text: "Fund bursaries, hardship schemes and cost-of-study help, and make sure applicants hear about them before they decide whether to apply.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If money is a worry, you can expect help to be on offer and to hear about it before you decide whether to apply.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an institutional service at the access stage, set beside the students' own access to financial support. Do not name schemes or amounts; the model gives none. Link it to widening participation."
  author-agent-dialogue: "Raise it when cost comes up as a reason not to apply or to leave. Ask: \"Do you know what financial help is on offer here?\" and \"Who could tell you whether you qualify?\" Avoid giving eligibility advice."
- component: advancehe/arap-2024/institution.targeted-outreach
  forPractitioner: { text: "Aim outreach at communities and schools where entry rates are low, plan it with them and check whom it actually reaches.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If no one around you has been to university, you can expect it to come and meet you, not wait for you to find it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the institution choosing where to spend outreach effort. Do not imply targeting means excluding others. Set it beside the outreach activities that staff and students meet in practice."
  author-agent-dialogue: "Raise it in widening participation planning. Ask: \"Who is this outreach meant to reach, and how do you know it does?\" Avoid labelling groups as deficient."
- component: advancehe/arap-2024/institution.contextual-admissions
  forPractitioner: { text: "Use context, such as school, area or care experience, when reading applications, and make clear how it changes offers.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "When you apply, the circumstances in which you studied can count alongside your grades.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as reading achievement in context. Do not state particular criteria or lowered grades; the model gives none. Link it to the postgraduate form on the same dial."
  author-agent-dialogue: "Raise it when an applicant thinks their grades rule them out. Ask: \"Has anything about where or how you studied made results harder to get?\" Avoid promising an offer."
- component: advancehe/arap-2024/institution.application-admission
  forPractitioner: { text: "Make each step of applying and enrolling clear, quick and well explained, and remove steps that add delay without purpose.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect applying and enrolling to be clear, with each step explained and decisions made in good time.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as process quality at the access stage. Do not describe a particular admissions system. Set it beside contextual admissions, which is about how decisions are made rather than how smoothly."
  author-agent-dialogue: "Raise it when an applicant is confused by forms or deadlines. Ask: \"Which step is unclear, and who could explain it?\" Avoid guessing at deadlines."
- component: advancehe/arap-2024/institution.learning-analytics
  forPractitioner: { text: "Use engagement and attendance data to flag students who may need help, and make sure each flag leads to a timely human contact.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If your engagement drops, you can expect someone to notice and get in touch to offer help.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe analytics as a trigger for human support, as the source does, not as surveillance or prediction of failure. Link it to early intervention on the educators' dial."
  author-agent-dialogue: "Raise it when data is discussed. Ask: \"What happens after a student is flagged, and how quickly?\" Avoid implying that data alone helps anyone."
- component: advancehe/arap-2024/institution.peer-learning-systems
  forPractitioner: { text: "Fund and organise peer learning schemes, such as peer mentoring or study groups, train the peer leaders and keep the schemes running year on year.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect chances to learn with other students, including those a year or two ahead of you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the institution's structure behind peer learning; the educators' dial holds the communities that form within it. Do not claim a specific scheme model."
  author-agent-dialogue: "Raise it when a student studies alone and struggles. Ask: \"Is there a peer group or mentor scheme on your course?\" Avoid presenting peers as a substitute for staff."
- component: advancehe/arap-2024/institution.mental-health-wellbeing
  forPractitioner: { text: "Resource mental health and wellbeing services well enough to respond in time, and connect them with teaching staff so that concerns are passed on.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you are struggling with your mental health or wellbeing, you can expect support to exist and to be reachable without a long wait.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an institutional service and a condition of staying on. Do not offer clinical advice or name conditions. Link it to pastoral support on the students' dial."
  author-agent-dialogue: "Raise it gently when a student mentions stress affecting study. Ask: \"Do you know where to get support here?\" Avoid diagnosing or counselling; point to services."
- component: advancehe/arap-2024/institution.learning-spaces
  forPractitioner: { text: "Design and equip spaces where students can work together and meet informally, and make sure every student can use them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect places on campus where you can work with others or just spend time, and where you feel welcome.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present spaces as a condition of belonging and collaboration, as the source does. Do not reduce it to estate standards."
  author-agent-dialogue: "Raise it when students say they have nowhere to go between classes. Ask: \"Where do students on your course meet and work together?\""
- component: advancehe/arap-2024/institution.commitment-full-potential
  forPractitioner: { text: "State the commitment, measure progress towards it, including awarding gaps between groups, and act where some students fall behind.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect high hopes for what you can achieve, and support aimed at helping you get there.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the institution's stated commitment and culture. Do not claim results; the model describes intent. Link it to closing awarding gaps, which the source names."
  author-agent-dialogue: "Raise it when low expectations of a group surface. Ask: \"What would it take for every student here to reach their best?\" Avoid blaming students for gaps."
- component: advancehe/arap-2024/institution.flexible-learning-models
  forPractitioner: { text: "Offer study patterns, such as part-time, blended or step-off routes, that let students with other commitments keep going and do well.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If work, care or other commitments limit when you can study, you can expect more than one way to fit study around them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a structural condition of attainment. Do not name modes the model does not name. Link it to the series' flexible learning theme."
  author-agent-dialogue: "Raise it when a student's circumstances clash with the timetable. Ask: \"Is there another pattern of study open to you?\" Avoid promising options that may not exist."
- component: advancehe/arap-2024/institution.staff-recruitment-development
  forPractitioner: { text: "Recruit for and develop the skills that support student success, including inclusive teaching and support skills, and give staff time to use them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the people who teach and support you to be skilled and kept up to date.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the staffing condition behind attainment. Do not equate it with any one qualification. Link it to strategic approaches to teaching excellence."
  author-agent-dialogue: "Raise it in staff development planning. Ask: \"What skills do staff here need to support every student, and how are they built?\""
- component: advancehe/arap-2024/institution.teaching-excellence
  forPractitioner: { text: "Set a teaching strategy that ties to the institution's vision, back it with policy and resources, and review its effect on student outcomes.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect good teaching to be planned for across your university, not left to chance.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as strategy, not individual brilliance. Do not equate excellence with metrics alone. Link it to the vision and policy framing line (frame.institution)."
  author-agent-dialogue: "Raise it in strategy work. Ask: \"How does the teaching strategy reach the classroom, and how would you know?\""
- component: advancehe/arap-2024/institution.lifelong-learning
  forPractitioner: { text: "Offer short courses, further study routes and ways back in, and tell students about them before they leave.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "When you finish, you can expect ways to keep learning and to come back for more study later.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as progression beyond the first award. Do not name particular provision. Link it to contextual postgraduate admissions."
  author-agent-dialogue: "Raise it when a student assumes learning ends at graduation. Ask: \"What might you want to learn next, and when?\""
- component: advancehe/arap-2024/institution.contextual-pg-admissions
  forPractitioner: { text: "Apply contextual criteria to postgraduate applications too, so that progression to further study is open to those who faced barriers.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you apply for further study, the circumstances of your earlier study can count alongside your results.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the progression-stage counterpart of contextual admissions. Do not state criteria. Note that the model places it under progression."
  author-agent-dialogue: "Raise it when a graduate doubts they could go on to postgraduate study. Ask: \"Has anything in your circumstances affected your results?\" Avoid promising admission."
- component: advancehe/arap-2024/institution.employer-engagement
  forPractitioner: { text: "Build lasting ties with employers that open placements, projects, talks and jobs to all students, not only the best connected.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect chances to meet employers and learn what they look for while you study.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the institution's side of employer relationships; the educators' dial has the same label for the course-level side. Do not name employers."
  author-agent-dialogue: "Raise it in curriculum or careers planning. Ask: \"Which employers do students meet on this course, and how?\""
- component: advancehe/arap-2024/institution.career-services
  forPractitioner: { text: "Provide careers advice from the first year, link it to courses, and reach students who do not seek it out.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can get help to plan your next step after study, from early on and not only in your final year.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a service condition of progression. Do not give careers advice in its name. Link it to information on progression paths on the students' dial."
  author-agent-dialogue: "Raise it when a student is unsure what comes next. Ask: \"Have you talked to the careers service yet?\" Avoid steering towards a particular career."
- component: advancehe/arap-2024/educators.bridging-programmes
  forPractitioner: { text: "Design and teach preparatory courses that build the skills and confidence new students need, and link them to the course they lead into.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Before you start, you can take part in a course that helps you get ready for study.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as pre-entry teaching. Do not describe it as remedial or as a lesser route. Link it to pre-entry learning communities."
  author-agent-dialogue: "Raise it with prospective students who feel underprepared. Ask: \"Is there a preparation course you could join before starting?\""
- component: advancehe/arap-2024/educators.outreach-activities
  forPractitioner: { text: "Take part in outreach: talk about your subject, run taster sessions and show prospective students what study is like.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Before you apply, you can meet the people who teach and try out what studying a subject is like.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the staff part in outreach; the same label on the students' dial is outreach as students meet it. Do not describe a particular programme."
  author-agent-dialogue: "Raise it when staff ask how they can help access. Ask: \"What could you show a prospective student about your subject?\""
- component: advancehe/arap-2024/educators.engagement-applicants
  forPractitioner: { text: "Contact applicants before they arrive with welcome messages, course information and chances to ask questions.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "After you get an offer, you can expect to hear from your course and to be able to ask questions before you arrive.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the gap between offer and arrival. Do not imply a set contact schedule. Link it to early engagement on the students' dial."
  author-agent-dialogue: "Raise it in planning for new intakes. Ask: \"What does an applicant hear from the course before they arrive?\""
- component: advancehe/arap-2024/educators.pre-entry-communities
  forPractitioner: { text: "Set up a space, online or in person, where incoming students meet each other and staff and begin some learning together before term.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Before term starts, you can meet others joining your course and begin learning with them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the start of belonging, as the source does. Do not equate it with induction alone. Link it to peer learning communities."
  author-agent-dialogue: "Raise it in planning for new students. Ask: \"Where can new students meet each other before they arrive?\""
- component: advancehe/arap-2024/educators.inclusive-curriculum
  forPractitioner: { text: "Choose content, examples and sources that reflect a range of backgrounds and views, and use them to open debate.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to see people and experiences like yours in what you study, alongside others different from you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as curriculum content and design. Do not reduce it to adding names to a reading list. Link it to the series' inclusive curriculum framework, which the use page names."
  author-agent-dialogue: "Raise it when material draws on one perspective. Ask: \"Whose experience does this material reflect, and whose is missing?\" Avoid tokenism."
- component: advancehe/arap-2024/educators.peer-learning-communities
  forPractitioner: { text: "Organise teaching so that students learn in stable groups, with each other and with staff, and keep those groups going.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to learn in groups where you know others and they know you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Keep the printed label with its slash; it reads as peer and learning communities. Present it as the course-level form of the institution's peer learning systems."
  author-agent-dialogue: "Raise it when students feel isolated on a large course. Ask: \"Which group do you learn with regularly?\""
- component: advancehe/arap-2024/educators.student-centred-pedagogy
  forPractitioner: { text: "Plan teaching around what students need and do, with active tasks, and adjust to the group in front of you.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to be active in your learning, with teaching shaped around what you and your group need.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an approach to teaching. Do not set it against all lecturing; it is about where the focus lies. Link it to student choice and to co-creation."
  author-agent-dialogue: "Raise it when teaching is mostly transmission. Ask: \"What will students do in this session, and how does it fit their needs?\""
- component: advancehe/arap-2024/educators.early-intervention
  forPractitioner: { text: "Watch for early signs, such as missed sessions or late work, and contact the student promptly with an offer of help.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you start to fall behind, you can expect someone to notice early and offer help.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as staff action, the human side of the institution's learning analytics. Do not frame it as discipline."
  author-agent-dialogue: "Raise it when staff wait until a fail. Ask: \"What early sign would tell you this student needs help, and who acts on it?\""
- component: advancehe/arap-2024/educators.authentic-assessment
  forPractitioner: { text: "Set assessments based on real tasks and audiences in the field, and explain how they connect to work beyond the course.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect assessments that look like real tasks you might do later, not only exams for their own sake.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as assessment design; the model does not define it further. Do not confuse it with the inclusive model's authentic learners. Link to the series' assessment framework."
  author-agent-dialogue: "Raise it in assessment design. Ask: \"Where would someone in the field do a task like this?\""
- component: advancehe/arap-2024/educators.graduate-attributes
  forPractitioner: { text: "Build the institution's graduate attributes into teaching and assessment, and make them visible to students as they develop.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your course to help you build wider skills, such as working with others, and to show you when you are building them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the educators' part in graduate attributes; the students' dial has graduate attributes and competencies. Do not list attributes the model does not."
  author-agent-dialogue: "Raise it in course design. Ask: \"Which wider skills does this module build, and do students know it?\""
- component: advancehe/arap-2024/educators.student-choice
  forPractitioner: { text: "Offer choice of topic, format or timing in assessment where the learning outcome allows, and help students choose well.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect some choice in how you show what you have learned.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present choice as tied to assessment, as the source does. Do not imply every element is optional. Link it to diverse and inclusive assessment."
  author-agent-dialogue: "Raise it in assessment design. Ask: \"Which parts of this task could students choose without losing the outcome?\""
- component: advancehe/arap-2024/educators.constructive-feedback
  forPractitioner: { text: "Give feedback that points forward, arrives in time to use, and is followed by a chance to act on it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect feedback that shows you how to improve and comes in time to use it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as feedback for improvement. Do not equate it with marks or praise. Link to the series' assessment framework."
  author-agent-dialogue: "Raise it when students ignore feedback. Ask: \"When do students get to use this feedback, and how?\""
- component: advancehe/arap-2024/educators.diverse-inclusive-assessment
  forPractitioner: { text: "Use a mix of assessment types across a course, check them for hidden barriers, and design them for the range of students you teach.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect a mix of assessment types, designed so that you have a fair chance to show what you can do.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as variety plus fairness. Do not imply lower standards. Link it to student choice and to the series' assessment framework."
  author-agent-dialogue: "Raise it when one assessment type dominates. Ask: \"Which students might this format disadvantage for reasons unrelated to the outcome?\""
- component: advancehe/arap-2024/educators.professional-competencies
  forPractitioner: { text: "Identify the competencies of the field your students are heading for, and teach and assess them in the course.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your course to build the practical skills you will need in professional life.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as curriculum content for progression. Do not equate it with accreditation. Link it to professional experiences."
  author-agent-dialogue: "Raise it in course design. Ask: \"What will graduates of this course need to be able to do at work, and where do they learn it?\""
- component: advancehe/arap-2024/educators.professional-experiences
  forPractitioner: { text: "Arrange placements, live projects or practice visits that every student can take up, and help students reflect on them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect chances to try out professional work during your course.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the educators' side of experiential learning; the students' dial has experiential, authentic and work-based experiences. Do not imply all courses include placements."
  author-agent-dialogue: "Raise it when students lack contact with practice. Ask: \"Where in this course does a student try out professional work?\""
- component: advancehe/arap-2024/educators.employer-engagement
  forPractitioner: { text: "Bring employers into teaching through talks, projects and course review, and help students make contacts.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect employers to be part of your course, through talks, projects or feedback on your work.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "The same label appears on the institution's dial; here it is the course-level side. Link to the series' employability framework."
  author-agent-dialogue: "Raise it in course design. Ask: \"Where do employers appear in this course?\""
- component: advancehe/arap-2024/students.information-advice
  forPractitioner: { text: "Give prospective students clear information and personal advice about courses, costs, support and what study will be like.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Before you apply, you can get clear information and personal advice about courses, costs and what study is really like.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as what students receive at the access stage. Note the source calls pre-entry information personalised. Do not give admissions advice in its name."
  author-agent-dialogue: "Raise it when a prospective student is unsure. Ask: \"What do you still need to know to decide?\" Avoid giving firm answers on entry."
- component: advancehe/arap-2024/students.outreach-activities
  forPractitioner: { text: "Run outreach that lets prospective students experience the course and meet staff and current students.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Before you apply, you can join activities that let you see what study is like and meet people on the course.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as outreach from the student's side; the educators' dial has the same label. Do not describe a particular programme."
  author-agent-dialogue: "Raise it with prospective students. Ask: \"Have you been to a taster or open event?\""
- component: advancehe/arap-2024/students.early-engagement
  forPractitioner: { text: "Help incoming students connect early with their cohort, course and institution through events and shared spaces.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can start getting to know your course, your university and others in your year before or soon after you arrive.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as early belonging, which the source ties to completing the course. Link it to engagement with applicants on the educators' dial."
  author-agent-dialogue: "Raise it with new students. Ask: \"Who have you met on your course so far?\""
- component: advancehe/arap-2024/students.access-financial-support
  forPractitioner: { text: "Make financial support easy to find and claim, and tell students about it at the points they need it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you need money help, you can expect to find out what exists and to apply without a struggle.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as access to support from the student's side; the institution's dial has financial support. Do not give eligibility advice."
  author-agent-dialogue: "Raise it when money worries surface. Ask: \"Do you know how to apply for financial help here?\""
- component: advancehe/arap-2024/students.remedial-support
  forPractitioner: { text: "Offer catch-up support, such as skills sessions or study help, without stigma, and point students to it early.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you fall behind or find a skill hard, you can get help to catch up without feeling judged.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Keep the issuer's word but gloss it as catch-up help; avoid any tone of deficit. Link it to early intervention."
  author-agent-dialogue: "Raise it when a student is behind. Ask: \"What would help you catch up, and have you seen the study skills support?\""
- component: advancehe/arap-2024/students.pastoral-support
  forPractitioner: { text: "Make personal support easy to reach and connect it with academic staff, so that a student's whole situation is considered.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If life outside your studies gets difficult, you can find someone to talk to and get support.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as support for the whole person. Do not give personal advice in its name. Link it to the institution's mental health and wellbeing services."
  author-agent-dialogue: "Raise it gently when personal matters affect study. Ask: \"Is there someone here you could talk to about this?\""
- component: advancehe/arap-2024/students.sense-of-belonging
  forPractitioner: { text: "Make students feel valued and included through how you teach, who you notice and how they take part in academic and campus life.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You belong here: you can expect to feel valued and part of the community you study in.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present belonging as the thread the source runs through all four stages. Link it to mattering. Do not reduce it to social events."
  author-agent-dialogue: "Raise it when a student feels out of place. Ask: \"Where on your course do you feel most at home, and where least?\""
- component: advancehe/arap-2024/students.accessible-information
  forPractitioner: { text: "Publish information and materials in accessible formats, in plain language and in places students already look.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect information and materials in forms you can find, open and use.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as accessibility of information and resources, which the source calls resource accessibility. Link it to the series' accessibility theme."
  author-agent-dialogue: "Raise it when a student cannot use materials. Ask: \"What format would work for you?\""
- component: advancehe/arap-2024/students.digital-tools-devices
  forPractitioner: { text: "Lend devices, provide software and assistive technology, and check that no student is held back by lack of technology.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you lack a device, software or a connection, you can expect help to get what you need to study.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a practical condition of staying on. Link it to assistive technology, which the source names. Do not name products."
  author-agent-dialogue: "Raise it when a student cannot get online or use a tool. Ask: \"What technology would you need, and do you know about loan schemes?\""
- component: advancehe/arap-2024/students.graduate-attributes-competencies
  forPractitioner: { text: "Help students recognise and record the attributes and competencies they are building, and how to show them to others.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You build wider skills and abilities as you study, and can learn to recognise and describe them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as what students develop and can show. The educators' dial has develop graduate attributes. Note the model places it under attainment, not progression."
  author-agent-dialogue: "Raise it in reflection. Ask: \"Which skills have you built this year, and how could you show them?\""
- component: advancehe/arap-2024/students.recognition-achievements
  forPractitioner: { text: "Recognise what students achieve, including outside assessed work, and make it visible to them and others.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "What you achieve, in your studies and beyond them, is noticed and valued.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the source's own definition of attainment: recognising and validating achievement. Do not equate it with marks alone."
  author-agent-dialogue: "Raise it when a student discounts their progress. Ask: \"What have you achieved this term that you are proud of?\""
- component: advancehe/arap-2024/students.co-creation-partnership
  forPractitioner: { text: "Work with students as partners in designing learning and in decisions, and show what changed because of them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can help shape your course and the decisions that affect it, working alongside staff.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present partnership as key to success, as the source states. Do not equate it with surveys. Link it to the series' student partnership theme."
  author-agent-dialogue: "Raise it when decisions are made for students. Ask: \"Where could students help design this?\""
- component: advancehe/arap-2024/students.personal-tutoring
  forPractitioner: { text: "Meet tutees regularly, know their progress and circumstances, and refer them to support when needed.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect a personal tutor who knows you and helps you with your progress.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present tutoring as a relationship. Note the model places it under attainment. Do not describe a particular tutoring model."
  author-agent-dialogue: "Raise it when a student has no one to turn to. Ask: \"Have you met your personal tutor this term?\""
- component: advancehe/arap-2024/students.agency-self-confidence
  forPractitioner: { text: "Give students decisions to make, reflection to do and support to build confidence, so they can plan their own next step.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can grow in confidence, know your strengths and take charge of your learning and your next step.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a progression condition: owning one's education leads to moving on. Link it to self-efficacy, which the source names under attainment."
  author-agent-dialogue: "Raise it when a student waits to be told. Ask: \"What do you want to do next, and what do you need to get there?\""
- component: advancehe/arap-2024/students.experiential-work-based
  forPractitioner: { text: "Offer and recognise experiential and work-based learning, in the course and in extra-curricular activity, open to every student.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can learn by doing real tasks, including in workplaces, and have that experience count.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the students' side of professional experiences. Note the source names extra and co-curricular activity. Do not imply placements are guaranteed."
  author-agent-dialogue: "Raise it when learning feels abstract. Ask: \"Where could you try this out for real?\""
- component: advancehe/arap-2024/students.networks
  forPractitioner: { text: "Help students meet alumni, employers and professionals, and teach them how to build and use contacts.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can build contacts with others in your field who can help you take your next step.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present networks as something the course helps every student build. The model gives no detail. Do not assume students arrive with contacts."
  author-agent-dialogue: "Raise it in career planning. Ask: \"Who do you know in the field you want to enter, and how could you meet more?\""
- component: advancehe/arap-2024/students.progression-paths
  forPractitioner: { text: "Show students the routes into further study and work open to them, early in the course and again near its end.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can find out what routes into work or further study are open to you, and how to take them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as information at the progression stage, the counterpart of pre-entry information. Link it to career services."
  author-agent-dialogue: "Raise it when a student is unsure what comes next. Ask: \"What routes are open from your course, and where could you find out?\""
```

### M3 Conditions
<!-- label: editorial; status: drafted; basis: discussion. Ours, every field. -->
```yaml
- component: advancehe/arap-2024/institution.financial-support
  theme: theme:targeted-support
  holdsWhen: "Financial help exists for students who need it, is publicised to applicants and is simple to claim."
  signs: ["bursary and hardship details appear in pre-application material", "staff can point a worried applicant to the right office", "claim processes are short and decided quickly"]
  absentWhen: "Help exists only on paper or is found too late, and cost quietly filters out applicants."
  contextSteer: "Where cost may matter to the learner, say plainly that financial help exists and where to ask about it."
  basis: ours
- component: advancehe/arap-2024/institution.targeted-outreach
  theme: theme:transition
  holdsWhen: "Outreach is directed at groups with low entry rates and its reach is checked against that aim."
  signs: ["outreach plans name the groups they aim at", "activity records show who took part", "partner schools or communities help shape the programme"]
  absentWhen: "Outreach goes to whoever already turns up, and the gap in who enters stays the same."
  contextSteer: "Write for a reader who may be the first in their circle to consider university, and explain what others take for granted."
  basis: ours
- component: advancehe/arap-2024/institution.contextual-admissions
  theme: theme:contextual-adaptation
  holdsWhen: "Admissions take account of the setting in which an applicant studied, by published criteria."
  signs: ["the admissions policy names the contextual factors it uses", "offers vary with context in a stated way", "applicants can find out whether they qualify"]
  absentWhen: "Grades are read as if every applicant had the same chances to earn them."
  contextSteer: "Treat the learner's prior results as shaped by circumstance, and avoid implying that grades alone show potential."
  basis: ours
- component: advancehe/arap-2024/institution.application-admission
  theme: theme:transition
  holdsWhen: "Applicants can see each step, know what is needed and receive timely decisions."
  signs: ["steps and deadlines are set out in one place", "applicants get prompt replies to queries", "drop-out between offer and enrolment is tracked"]
  absentWhen: "Applicants are lost in unclear steps, and some give up before enrolment."
  contextSteer: "Set out any process the learner must follow as clear numbered steps with what each one needs."
  basis: ours
- component: advancehe/arap-2024/institution.learning-analytics
  theme: theme:targeted-support
  holdsWhen: "Engagement data is reviewed regularly and a flag leads to a supportive contact within a set time."
  signs: ["a named person acts on each flag", "students are contacted soon after engagement falls", "students are told what data is used and why"]
  absentWhen: "Data is gathered but nobody acts on it, or students learn of concern only when they fail."
  contextSteer: "Encourage the learner to notice their own engagement patterns and to treat a check-in from staff as help, not blame."
  basis: ours
- component: advancehe/arap-2024/institution.peer-learning-systems
  theme: theme:belonging-mattering
  holdsWhen: "Peer learning schemes are available to every student, staffed by trained peers and sustained over time."
  signs: ["each course has a peer scheme students know about", "peer leaders are trained and supported", "participation is tracked and reviewed"]
  absentWhen: "Students who already have friends benefit, and others study alone."
  contextSteer: "Build in a point where the learner works with or learns from a peer."
  basis: ours
- component: advancehe/arap-2024/institution.mental-health-wellbeing
  theme: theme:compassion
  holdsWhen: "Wellbeing and mental health support is resourced, known to students and reachable in good time."
  signs: ["waiting times are short and published", "staff know how to refer a student", "students can name where to go for support"]
  absentWhen: "Support is hard to find or slow, and students leave rather than ask."
  contextSteer: "Acknowledge that study can be stressful and say where support can be found, without giving clinical advice."
  basis: ours
- component: advancehe/arap-2024/institution.learning-spaces
  theme: theme:belonging-mattering
  holdsWhen: "Students have accessible spaces for group work and informal contact, and use them."
  signs: ["spaces for group work are easy to book or find", "students gather in them between classes", "the spaces suit a range of needs"]
  absentWhen: "Students arrive for classes and leave, with nowhere to meet or work together."
  contextSteer: "Suggest settings, physical or online, where the learner can work with others or meet informally."
  basis: ours
- component: advancehe/arap-2024/institution.commitment-full-potential
  theme: theme:whole-institution
  holdsWhen: "The institution sets an aim for every student, tracks gaps between groups and acts to close them."
  signs: ["strategies name gaps between groups and targets to close them", "progress is reported openly", "actions follow when gaps persist"]
  absentWhen: "Differences in results between groups are treated as natural and left alone."
  contextSteer: "Write with high expectations of every learner and avoid any hint that some are less capable."
  basis: ours
- component: advancehe/arap-2024/institution.flexible-learning-models
  theme: theme:contextual-adaptation
  holdsWhen: "Students can choose or change patterns of study to fit their circumstances without losing progress."
  signs: ["part-time or blended routes exist for the course", "students can pause and return with credit kept", "materials are available outside class times"]
  absentWhen: "One fixed pattern of study suits some students, and those with other commitments fall behind or leave."
  contextSteer: "Make the material usable at the learner's own pace and time, and avoid assuming full-time attendance."
  basis: ours
- component: advancehe/arap-2024/institution.staff-recruitment-development
  theme: theme:whole-institution
  holdsWhen: "Staff are recruited and developed for the skills student success needs, and have time to use them."
  signs: ["job descriptions name student support and inclusive teaching", "development is offered and taken up", "staff report having time to apply what they learn"]
  absentWhen: "Staff are left to learn alone, and support depends on who a student happens to meet."
  contextSteer: "Write for staff readers as skilled professionals who are still developing, and point to where their practice can grow."
  basis: ours
- component: advancehe/arap-2024/institution.teaching-excellence
  theme: theme:whole-institution
  holdsWhen: "A teaching strategy exists, is linked to the institution's vision, and shapes what happens in courses."
  signs: ["course reviews refer to the teaching strategy", "resources follow strategic priorities", "the strategy's effects on students are reported"]
  absentWhen: "Teaching quality varies by person and course, with no shared direction."
  contextSteer: "Align a lesson's approach with stated strategic priorities where they are known, and make good teaching practice visible."
  basis: ours
- component: advancehe/arap-2024/institution.lifelong-learning
  theme: theme:transition
  holdsWhen: "Graduates and others can find and take further learning routes at the institution."
  signs: ["further study options are shown to final-year students", "returning learners have a clear way in", "short courses are open to alumni"]
  absentWhen: "The relationship ends at graduation and further learning must be found elsewhere."
  contextSteer: "Point the learner towards where the topic could lead in later study or work."
  basis: ours
- component: advancehe/arap-2024/institution.contextual-pg-admissions
  theme: theme:contextual-adaptation
  holdsWhen: "Postgraduate admissions read results in context by published criteria."
  signs: ["postgraduate entry criteria mention context", "graduates from under-represented groups progress at similar rates", "applicants can see how context is used"]
  absentWhen: "Barriers met at undergraduate level carry over unchecked into postgraduate entry."
  contextSteer: "Avoid implying that the learner's earlier results fix what further study is open to them."
  basis: ours
- component: advancehe/arap-2024/institution.employer-engagement
  theme: theme:career-development
  holdsWhen: "Employers are involved in ways that every student can reach, such as placements, projects or talks."
  signs: ["employer contacts are listed and active", "students from all backgrounds meet employers", "employer input shapes some course content"]
  absentWhen: "Contact with employers depends on students' own networks."
  contextSteer: "Bring in a real workplace view or example that shows how the topic is used at work."
  basis: ours
- component: advancehe/arap-2024/institution.career-services
  theme: theme:career-development
  holdsWhen: "Careers support is available throughout study and reaches students who would not ask for it."
  signs: ["careers sessions are built into courses", "first-year students know the service", "uptake is tracked across student groups"]
  absentWhen: "Careers help is left until the end and used mostly by students who are already confident."
  contextSteer: "Connect the topic to possible next steps and suggest talking to careers advisers where relevant."
  basis: ours
- component: advancehe/arap-2024/educators.bridging-programmes
  theme: theme:transition
  holdsWhen: "Preparation programmes exist for those who need them and lead into the main course."
  signs: ["bridging courses are offered before term", "participants progress into the course", "content links to first-year modules"]
  absentWhen: "Students start without preparation and the gap shows in the first weeks."
  contextSteer: "Begin from what a newcomer may not yet know, and build the basics before moving on."
  basis: ours
- component: advancehe/arap-2024/educators.outreach-activities
  theme: theme:transition
  holdsWhen: "Staff take part in outreach and prospective students meet them."
  signs: ["staff run taster sessions or school visits", "outreach shows real teaching", "participants go on to apply"]
  absentWhen: "Outreach is left to a central team, and prospective students never meet teaching staff."
  contextSteer: "Show the learner what studying the subject is really like, with a concrete taste of it."
  basis: ours
- component: advancehe/arap-2024/educators.engagement-applicants
  theme: theme:transition
  holdsWhen: "Applicants hear from course staff before arrival and can ask questions."
  signs: ["welcome messages go out from course staff", "applicants can join an online space or event", "queries from applicants are answered promptly"]
  absentWhen: "Applicants hear nothing between offer and arrival, and some do not turn up."
  contextSteer: "Welcome the learner as already part of the course and tell them what to expect."
  basis: ours
- component: advancehe/arap-2024/educators.pre-entry-communities
  theme: theme:belonging-mattering
  holdsWhen: "Incoming students join a learning group with peers and staff before the course starts."
  signs: ["a pre-entry space exists and is used", "new students know some peers on arrival", "staff take part before term"]
  absentWhen: "Students arrive as strangers to each other and to staff."
  contextSteer: "Include a way for the learner to connect with others starting at the same time."
  basis: ours
- component: advancehe/arap-2024/educators.inclusive-curriculum
  theme: theme:anticipating-difference
  holdsWhen: "Course content and materials draw on diverse experiences and students engage with them in discussion."
  signs: ["reading lists and examples draw on a range of voices", "students say the content relates to them", "debate about different views is part of teaching"]
  absentWhen: "Content reflects one experience, and some students find nothing of themselves in it."
  contextSteer: "Use examples and sources that reflect a range of backgrounds and perspectives."
  basis: ours
- component: advancehe/arap-2024/educators.peer-learning-communities
  theme: theme:belonging-mattering
  holdsWhen: "Students learn in groups that last, with peers and staff they know."
  signs: ["students work in the same groups over time", "staff and students know each other by name", "students help one another outside class"]
  absentWhen: "Students sit in large classes with no group to belong to."
  contextSteer: "Design the activity for small groups and encourage the learner to build on what others say."
  basis: ours
- component: advancehe/arap-2024/educators.student-centred-pedagogy
  theme: theme:anticipating-difference
  holdsWhen: "Students spend much of their learning time active, and teaching changes in response to them."
  signs: ["sessions include tasks for students", "staff adjust plans after checking understanding", "students are asked what helps them learn"]
  absentWhen: "Students listen while staff talk, and teaching is the same whoever is in the room."
  contextSteer: "Give the learner something to do, not only something to read, and connect it to their needs."
  basis: ours
- component: advancehe/arap-2024/educators.early-intervention
  theme: theme:targeted-support
  holdsWhen: "Early signs of difficulty prompt a supportive contact from staff within days."
  signs: ["staff follow up missed sessions quickly", "early low-stakes tasks show who needs help", "contacts offer help rather than warnings"]
  absentWhen: "Difficulties surface only at the exam, when it is too late to help."
  contextSteer: "Include an early check of understanding and say where help can be found if it is shaky."
  basis: ours
- component: advancehe/arap-2024/educators.authentic-assessment
  theme: theme:authenticity
  holdsWhen: "Assessments are modelled on tasks and audiences found in the subject or workplace."
  signs: ["assessment briefs name a real audience or purpose", "students can say how a task relates to work", "employers or practitioners help shape tasks"]
  absentWhen: "Assessment tests recall in forms that students never meet again."
  contextSteer: "Frame any task the learner does around a real purpose and audience."
  basis: ours
- component: advancehe/arap-2024/educators.graduate-attributes
  theme: theme:career-development
  holdsWhen: "Graduate attributes are taught and assessed explicitly and students can say which they are building."
  signs: ["module outlines name the attributes they develop", "students reflect on their progress in them", "assessments include them"]
  absentWhen: "Wider skills are assumed to develop by themselves and students cannot name them."
  contextSteer: "Name the wider skill the learner is practising and how it will help them later."
  basis: ours
- component: advancehe/arap-2024/educators.student-choice
  theme: theme:agency-self-actualisation
  holdsWhen: "Students choose among real options in assessment and are helped to choose."
  signs: ["assessment briefs offer options", "students explain why they chose", "outcomes are met across options"]
  absentWhen: "Every student must show learning in one way, which suits some far better than others."
  contextSteer: "Offer the learner a choice of route or format where the aim allows."
  basis: ours
- component: advancehe/arap-2024/educators.constructive-feedback
  theme: theme:agency-self-actualisation
  holdsWhen: "Feedback arrives before the next task and students act on it."
  signs: ["feedback names next steps", "students use it in a following task", "feedback returns within a stated time"]
  absentWhen: "Feedback arrives late, justifies a mark and is never used."
  contextSteer: "Tell the learner what to do next to improve, not only how well they did."
  basis: ours
- component: advancehe/arap-2024/educators.diverse-inclusive-assessment
  theme: theme:anticipating-difference
  holdsWhen: "A course assesses in several forms, each checked for barriers that do not relate to what is assessed."
  signs: ["several assessment types appear across a course", "formats are reviewed for barriers", "results are compared across student groups"]
  absentWhen: "One format dominates and some groups do worse for reasons unrelated to their learning."
  contextSteer: "Avoid relying on one way for the learner to show understanding."
  basis: ours
- component: advancehe/arap-2024/educators.professional-competencies
  theme: theme:career-development
  holdsWhen: "The curriculum teaches and assesses the competencies of the field students will enter."
  signs: ["competencies are mapped to modules", "practitioners review the curriculum", "students can name the skills they have built"]
  absentWhen: "Students graduate with subject knowledge but unsure how to practise."
  contextSteer: "Show how the topic is applied in professional practice."
  basis: ours
- component: advancehe/arap-2024/educators.professional-experiences
  theme: theme:career-development
  holdsWhen: "Students have experiences of professional practice within the course, open to all."
  signs: ["placements or live projects exist", "take-up is similar across student groups", "students reflect on what they learned from them"]
  absentWhen: "Practice experience goes to students who can arrange it for themselves."
  contextSteer: "Link the task to a real professional setting the learner could experience."
  basis: ours
- component: advancehe/arap-2024/educators.employer-engagement
  theme: theme:career-development
  holdsWhen: "Employers take part in teaching or course design and students meet them."
  signs: ["employer talks or projects run in modules", "employers comment on course design", "students make employer contacts through the course"]
  absentWhen: "Employers are absent from teaching and students meet them only at the end."
  contextSteer: "Include an employer's perspective or a task framed by one."
  basis: ours
- component: advancehe/arap-2024/students.information-advice
  theme: theme:transition
  holdsWhen: "Prospective students can get accurate information and personal advice suited to their situation."
  signs: ["information covers costs, support and study life", "advice is available one to one", "applicants say they knew what to expect"]
  absentWhen: "Applicants rely on hearsay, and those without contacts make choices blind."
  contextSteer: "Explain the practical facts the learner needs to decide, without assuming prior knowledge of how higher education works."
  basis: ours
- component: advancehe/arap-2024/students.outreach-activities
  theme: theme:transition
  holdsWhen: "Prospective students take part in outreach and go on to apply."
  signs: ["prospective students attend tasters", "they meet current students", "they go on to apply"]
  absentWhen: "Prospective students never experience the course before choosing."
  contextSteer: "Give the learner a taste of the subject and the people in it."
  basis: ours
- component: advancehe/arap-2024/students.early-engagement
  theme: theme:transition
  holdsWhen: "New students have met peers and staff and know the institution before teaching begins."
  signs: ["students join cohort events early", "they know where to go for help", "they report knowing some peers"]
  absentWhen: "Students arrive knowing no one and nothing of how the place works."
  contextSteer: "Make the learner feel part of a group from the start."
  basis: ours
- component: advancehe/arap-2024/students.access-financial-support
  theme: theme:targeted-support
  holdsWhen: "Students who need financial help know about it and receive it in time."
  signs: ["students can find financial help without asking around", "claims are decided quickly", "take-up matches need across groups"]
  absentWhen: "Help exists but students do not know of it or give up on claiming."
  contextSteer: "Mention where money help can be found if cost bears on the topic."
  basis: ours
- component: advancehe/arap-2024/students.remedial-support
  theme: theme:targeted-support
  holdsWhen: "Catch-up help is available, known and used without stigma."
  signs: ["study skills sessions are open to all", "staff refer students without blame", "students who use help go on to pass"]
  absentWhen: "Students who fall behind stay behind, or avoid help for fear of being labelled."
  contextSteer: "Offer the learner a way back to any basics they may have missed, without singling them out."
  basis: ours
- component: advancehe/arap-2024/students.pastoral-support
  theme: theme:compassion
  holdsWhen: "Students can reach personal support easily, and academic and pastoral staff work together."
  signs: ["students know who to approach", "referrals between academic and pastoral staff work", "support is offered before a crisis"]
  absentWhen: "Personal problems are left to the student, and some leave without telling anyone."
  contextSteer: "Acknowledge that life beyond study affects learning, and say where support is."
  basis: ours
- component: advancehe/arap-2024/students.sense-of-belonging
  theme: theme:belonging-mattering
  holdsWhen: "Students say they feel valued and included, and take part in academic and community life."
  signs: ["students take part in class and campus life", "students say staff know them", "belonging is surveyed and acted on"]
  absentWhen: "Students feel like outsiders and drift away."
  contextSteer: "Address the learner as a valued member of the learning community."
  basis: ours
- component: advancehe/arap-2024/students.accessible-information
  theme: theme:anticipating-difference
  holdsWhen: "Information and materials meet accessibility standards and students can find them."
  signs: ["materials are in accessible formats", "information is in plain language", "students find what they need in one place"]
  absentWhen: "Information is scattered or inaccessible, and some students miss what others find."
  contextSteer: "Write in plain language with clear structure, and give alternatives for any non-text content."
  basis: ours
- component: advancehe/arap-2024/students.digital-tools-devices
  theme: theme:targeted-support
  holdsWhen: "Every student has the technology needed for their course, with loans and assistive tools available."
  signs: ["device loan schemes exist", "assistive technology is offered", "courses check students' access before relying on a tool"]
  absentWhen: "Students without devices or connections fall behind quietly."
  contextSteer: "Avoid assuming the learner has particular devices or software; offer low-tech alternatives."
  basis: ours
- component: advancehe/arap-2024/students.graduate-attributes-competencies
  theme: theme:career-development
  holdsWhen: "Students can name the attributes and competencies they have built and give evidence of them."
  signs: ["students keep a record of skills", "they can describe skills with examples", "they use them in applications"]
  absentWhen: "Students cannot say what they can do beyond their subject."
  contextSteer: "Ask the learner to name a skill they used and where they could use it again."
  basis: ours
- component: advancehe/arap-2024/students.recognition-achievements
  theme: theme:belonging-mattering
  holdsWhen: "Student achievements of many kinds are acknowledged and recorded."
  signs: ["achievements beyond marks are celebrated", "records capture wider activity", "students hear their progress named"]
  absentWhen: "Only grades count, and other achievements go unseen."
  contextSteer: "Acknowledge what the learner has already achieved before moving on."
  basis: ours
- component: advancehe/arap-2024/students.co-creation-partnership
  theme: theme:student-voice-partnership
  holdsWhen: "Students take part in designing learning and in decisions, and see the results."
  signs: ["students sit on course committees", "some teaching is co-designed", "changes are credited to student input"]
  absentWhen: "Students are consulted after decisions are made, if at all."
  contextSteer: "Invite the learner to shape part of the task or its outcome."
  basis: ours
- component: advancehe/arap-2024/students.personal-tutoring
  theme: theme:belonging-mattering
  holdsWhen: "Every student has a tutor they meet regularly and who knows their progress."
  signs: ["tutorials happen on a schedule", "tutors refer students to services", "students know their tutor by name"]
  absentWhen: "Tutors exist in name only and students do not know who to approach."
  contextSteer: "Encourage the learner to talk through their progress with someone who knows them."
  basis: ours
- component: advancehe/arap-2024/students.agency-self-confidence
  theme: theme:agency-self-actualisation
  holdsWhen: "Students make decisions about their learning and future and can explain their strengths."
  signs: ["students set their own goals", "they reflect on strengths and gaps", "they make plans for their next step"]
  absentWhen: "Students drift, unsure what they can do or want."
  contextSteer: "Ask the learner to reflect on their strengths and decide a next step."
  basis: ours
- component: advancehe/arap-2024/students.experiential-work-based
  theme: theme:authenticity
  holdsWhen: "Students take part in real or work-based learning and it is recognised."
  signs: ["students complete placements or projects", "extra-curricular experience is recorded", "take-up is fair across groups"]
  absentWhen: "Learning stays in the classroom and only some students gain real experience."
  contextSteer: "Ground the task in a real or work-based situation."
  basis: ours
- component: advancehe/arap-2024/students.networks
  theme: theme:career-development
  holdsWhen: "Students have contacts beyond their course that help them progress."
  signs: ["students meet alumni and professionals", "they use professional networking", "contacts lead to opportunities"]
  absentWhen: "Only students with family contacts have networks to draw on."
  contextSteer: "Suggest who the learner could connect with to take the topic further."
  basis: ours
- component: advancehe/arap-2024/students.progression-paths
  theme: theme:transition
  holdsWhen: "Students know the main routes after their course and how to pursue them."
  signs: ["routes are set out for each course", "final-year students can name options", "information covers study as well as work"]
  absentWhen: "Students learn of routes by chance, and some never hear of them."
  contextSteer: "Make clear where this learning can lead and what the next steps involve."
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
  lead: { span: { start: 11176, end: 11232 }, source: "It is particularly relevant to the following dimensions:", page: 14 }
  codes:
    - { to: advancehe/psf-dimensions-2023/V1, code: V1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V2, code: V2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V3, code: V3, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V4, code: V4, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A1, code: A1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A2, code: A2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A4, code: A4, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K2, code: K2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K3, code: K3, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K4, code: K4, page: 14, note: "named in the PSF table" }
  fellowship: { span: { start: 11321, end: 11535 }, source: "Advance HE invites all those teaching or supporting learning to evidence their use of this or other Student Success Frameworks in applying for Fellowship in recognition of their commitment to professional practice.", page: 14, note: "an invitation, not an obligation: not an S4 statement" }
inferred:
  - { from: "model", to: "theme:edi", rel: related, basis: inferred, note: "widening participation and closing awarding gaps run through the model" }
  - { from: "advancehe/arap-2024/educators.diverse-inclusive-assessment", to: "std:doc:advancehe-inclusive-learning-teaching-2024-model", rel: related, basis: inferred, note: "inclusive assessment design sits beside the inclusive model's anticipating difference" }
  - { from: "advancehe/arap-2024/students.sense-of-belonging", to: "advancehe/inclusive-2024/students.mattering", rel: related, basis: inferred, note: "the source pairs belonging and mattering (p. 4); the inclusive model holds mattering" }
  - { from: "advancehe/arap-2024/students.co-creation-partnership", to: "theme:student-partnership", rel: related, basis: inferred, note: "partnership is named as key to success (p. 3)" }
```

### M6 Practice themes carried
<!-- label: both; status: drafted; basis: discussion -->
```yaml
- { id: theme:transition, tier: practice, working: "students are prepared and supported as they move into, through and on from study", carriedBy: ["advancehe/arap-2024/institution.targeted-outreach", "advancehe/arap-2024/institution.application-admission", "advancehe/arap-2024/institution.lifelong-learning", "advancehe/arap-2024/institution.contextual-pg-admissions", "advancehe/arap-2024/educators.bridging-programmes", "advancehe/arap-2024/educators.outreach-activities", "advancehe/arap-2024/educators.engagement-applicants", "advancehe/arap-2024/educators.pre-entry-communities", "advancehe/arap-2024/students.information-advice", "advancehe/arap-2024/students.outreach-activities", "advancehe/arap-2024/students.early-engagement", "advancehe/arap-2024/students.progression-paths"], status: provisional }
- { id: theme:belonging-mattering, tier: practice, working: "students see that their experience and needs count", carriedBy: ["advancehe/arap-2024/institution.peer-learning-systems", "advancehe/arap-2024/institution.learning-spaces", "advancehe/arap-2024/educators.engagement-applicants", "advancehe/arap-2024/educators.pre-entry-communities", "advancehe/arap-2024/educators.peer-learning-communities", "advancehe/arap-2024/students.early-engagement", "advancehe/arap-2024/students.sense-of-belonging", "advancehe/arap-2024/students.recognition-achievements", "advancehe/arap-2024/students.personal-tutoring"], status: provisional }
- { id: theme:targeted-support, tier: practice, working: "help reaches the students who need it, early and before difficulty grows", carriedBy: ["advancehe/arap-2024/institution.financial-support", "advancehe/arap-2024/institution.learning-analytics", "advancehe/arap-2024/educators.early-intervention", "advancehe/arap-2024/students.access-financial-support", "advancehe/arap-2024/students.remedial-support", "advancehe/arap-2024/students.digital-tools-devices"], status: provisional }
- { id: theme:contextual-adaptation, tier: practice, working: "practice adapts to the setting and its students, not the reverse", carriedBy: ["advancehe/arap-2024/institution.contextual-admissions", "advancehe/arap-2024/institution.flexible-learning-models", "advancehe/arap-2024/institution.contextual-pg-admissions"], status: provisional }
- { id: theme:compassion, tier: practice, working: "decisions and teaching shaped by care for the person affected", carriedBy: ["advancehe/arap-2024/institution.mental-health-wellbeing", "advancehe/arap-2024/students.pastoral-support", "advancehe/arap-2024/students.personal-tutoring"], status: provisional }
- { id: theme:whole-institution, tier: practice, working: "the institution's strategy, quality processes, estate and staff pull together towards one aim", carriedBy: ["advancehe/arap-2024/institution.commitment-full-potential", "advancehe/arap-2024/institution.staff-recruitment-development", "advancehe/arap-2024/institution.teaching-excellence"], status: provisional }
- { id: theme:career-development, tier: practice, working: "students learn to explore, decide and manage their own paths and professional identity", carriedBy: ["advancehe/arap-2024/institution.employer-engagement", "advancehe/arap-2024/institution.career-services", "advancehe/arap-2024/educators.graduate-attributes", "advancehe/arap-2024/educators.professional-competencies", "advancehe/arap-2024/educators.professional-experiences", "advancehe/arap-2024/educators.employer-engagement", "advancehe/arap-2024/students.graduate-attributes-competencies", "advancehe/arap-2024/students.experiential-work-based", "advancehe/arap-2024/students.networks"], status: provisional }
- { id: theme:anticipating-difference, tier: practice, working: "teaching is designed in advance for the range of students", carriedBy: ["advancehe/arap-2024/educators.inclusive-curriculum", "advancehe/arap-2024/educators.student-centred-pedagogy", "advancehe/arap-2024/educators.diverse-inclusive-assessment", "advancehe/arap-2024/students.accessible-information"], status: provisional }
- { id: theme:authenticity, tier: practice, working: "learners bring who they are, and that is treated as an asset", carriedBy: ["advancehe/arap-2024/educators.inclusive-curriculum", "advancehe/arap-2024/educators.authentic-assessment", "advancehe/arap-2024/educators.professional-experiences", "advancehe/arap-2024/students.experiential-work-based"], status: provisional }
- { id: theme:agency-self-actualisation, tier: practice, working: "people grow into, use and trust their own judgement", carriedBy: ["advancehe/arap-2024/educators.student-choice", "advancehe/arap-2024/educators.constructive-feedback", "advancehe/arap-2024/students.agency-self-confidence"], status: provisional }
- { id: theme:student-voice-partnership, tier: practice, working: "a range of voices, students' included, shapes decisions and is answered", carriedBy: ["advancehe/arap-2024/students.co-creation-partnership"], status: provisional }
- { id: theme:hidden-curriculum, tier: practice, working: "the unwritten rules of study are made explicit", carriedBy: ["advancehe/arap-2024/students.information-advice", "advancehe/arap-2024/students.progression-paths"], status: provisional }
```

## Part B Terminology

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: access, definition: "making entry to higher education open to everyone who could gain from it", scopeNote: "the first stage; covers outreach, pre-entry information and admissions", category: concept, practices: [learning-and-teaching] }
- { slug: retention, definition: "students staying on and completing the course they chose", scopeNote: "the second stage", category: concept, practices: [learning-and-teaching] }
- { slug: attainment, definition: "what students achieve, recognised and valued", scopeNote: "the third stage; the source ties it to awarding gaps", category: concept, practices: [learning-and-teaching] }
- { slug: progression, definition: "students moving on to further study or work after their course", scopeNote: "the fourth stage", category: concept, practices: [learning-and-teaching] }
- { slug: sense-of-belonging, definition: "a student's feeling of being valued and included in their learning community", scopeNote: "the source runs it through all four stages; also a student segment", category: concept, practices: [learning-and-teaching] }
- { slug: mattering, definition: "a student's sense that they count to the institution", scopeNote: "named once beside belonging (p. 4); not a segment here", category: concept, practices: [learning-and-teaching] }
- { slug: awarding-gaps, definition: "differences in the degree results awarded to different groups of students", scopeNote: "named as a reason for attention to attainment and as an institutional mission", category: concept, practices: [learning-and-teaching] }
- { slug: learning-analytics, definition: "use of data on student activity to spot need and prompt support", scopeNote: "an institution segment and a framing line", category: practice, practices: [learning-and-teaching] }
- { slug: educators-plus, definition: "academic and professional services staff together", scopeNote: "the series' staff perspective; the + marks the inclusion of professional services", category: concept, practices: [learning-and-teaching] }
```

### B2a Terms as the issuer uses them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: access, form: "access", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: retention, form: "retention", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: attainment, form: "attainment", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: progression, form: "progression", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: sense-of-belonging, form: "sense of belonging", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: mattering, form: "mattering", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: awarding-gaps, form: "awarding gaps", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: learning-analytics, form: "learning analytics", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: educators-plus, form: "Educators+", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the model names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term takes a meaning of its own in one component.

### B4 Relations
```yaml
- { rel: related, from: sense-of-belonging, to: mattering, note: "named together on p. 4 as early conditions of completion" }
- { rel: related, from: attainment, to: awarding-gaps, note: "attainment factors are critical for closing awarding gaps (p. 4)" }
- { rel: related, from: access, to: progression, note: "the first and last of four linked stages" }
- { rel: related, from: learning-analytics, to: retention, note: "analytics allow timely intervention (p. 6)" }
```

### B5 Rules
- Educators+: write it as printed, and gloss it on first use as academic and professional services staff together.
- attainment: keep it distinct from awarding gaps; the source defines attainment as recognising achievement, and treats gaps as what attention to it should close.
- Remedial Support: keep the issuer's label in quotation but phrase our fields as catch-up help, to avoid a deficit tone.

## Part C Process

### C0 Formality
`not-applicable`: the model sets conditions and uses, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE
  title: "Framework for student access, retention, attainment and progression"
  edition: "digital edition, 2024"
  year: 2024
  url: "https://www.advance-he.ac.uk (the series page not reached; D3)"
  retrieved: "PDF supplied by Abbott, 4 October 2026"
  licence: "none stated; held by permission (D-std-0019)"
  tier: primary
  readVia: direct
  held: 55261cb1e3e0c4f1366f3cc770cea89efd283a649be1d3d109ca7ea2a9e382e4
  heldFiles: ["txt/advance-he-2024-framework-student-access-retention-attainment-progression-standard.txt", "txt/advance-he-2024-framework-student-access-retention-attainment-progression-standard.norm.txt", "records/advance-he-2024-framework-student-access-retention-attainment-progression-standard.held.json", "pdf/advance-he-2024-framework-student-access-retention-attainment-progression-standard.pdf"]
  citedIn: [0.2, S1, S2, S3, S4, M1, M2, M4, M5, B1]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: "2026-10-04", pass: P1, outcome: "used for every section; figure pages read as images (figure image)" }
- { ref: "ing:doc:access-retention-attainment-progression-framework-advance-he-2024", tier: primary, consulted: "2026-10-04", pass: P1, outcome: "read for consistency of component names; not cited" }
```

### D3 Wanted sources
```yaml
- { citation: "Advance HE, Student Success Frameworks (series web page), current", settles: ["S8", "S7"], asked: not yet, state: wanted }
- { citation: "Advance HE, the April 2025 revision of this PDF, if any (change notes)", settles: ["S1", "S8"], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- Front matter, S1: no year or copyright notice is printed; 2024 is taken from the series and the PDF's creation date (7 May 2024; modified 28 April 2025). `copyrightNotice: none-stated`. The 2025 modification date may mean a revised file; not checked (D3).
- Held text: held by Abbott's permission (4 October 2026, 05:03: "Yes full permission"; D-std-0019, as D-std-0013); private, never published.
- M2 labels: all 49 segment labels are curved text that the text layer scrambles (e.g. "Ta Ac rget tiv ed itie O s ut"); each was read from the page images (pp. 7, 9, 11), checked against the scrambled fragments, and written as printed, including capitals. "Peer/Learning Communities" keeps its slash as printed.
- M2 order: clockwise from the top of each dial, starting with the first segment right of the vertical, which is in the Access sector; stages run Access, Retention, Attainment, Progression clockwise.
- M2 groups: segments per stage are uneven. Institution 4/4/4/4; Educators+ 4/4/5/3 (Diverse and Inclusive Assessment sits below the horizontal, in Attainment); Students 4/5/4/4 (Access to Digital Tools and Devices in Retention). Read from the sector boundaries in the images; a doubt for Abbott on the two boundary segments.
- M2 sameLabelAs: "Employer Engagement" (institution, educators) and "Outreach Activities" (educators, students) recur with identical labels and are linked both ways.
- M2 explainedBy: links marked `inferred` are std's reading; the source never ties its prose to individual segments. Several segments (Flexible Learning Models, Networks, Remedial Support, Personal Tutoring) have no prose that names them; their links are inferred only.
- S4 force: four framing lines carry "responsibility", "needs to" or "requires" and read as must (D-std-0016). frame.students ("Securing retention and attainment ... requires ...") states a condition of success rather than laying a duty on a named party; read as must, for Abbott to confirm.
- S4 use lists: all twelve items are gerunds ("Supporting ...", "Articulating ..."), mood gerund, force describes. The Students list is voiced as provision for students, not by them; addressee provider.
- M6: three practice themes are proposed, none in the shared list: theme:targeted-support, theme:whole-institution, theme:career-development. theme:transition (provisional in the shared list) is confirmed here: it is the model's central idea (D1, p. 10, "transition into, through, and beyond"). theme:authenticity's working line is widened to cover tasks that mirror real practice; for Abbott to rule whether that is one theme or two.
- S6: theme:edi is inferred: the text names widening participation, social mobility and awarding gaps but not EDI (EDI appears only in the excluded back cover). theme:wellbeing, theme:employability, theme:assessment, theme:student-partnership, theme:accessibility, theme:digital and theme:flexible-learning are stated in segment labels or prose.
- S7 pointsTo: the use page names "Enhancing Assessment, Employability and Inclusive Curriculum" in the series. The assessment and employability ids are proposed (not yet ingested). "Inclusive Curriculum" has no matching title in the held series; it is pointed at the inclusive learning and teaching model as the nearest, for Abbott to confirm.
- M2: the theory run (ing 0139) reads the same 49 segments in the same order; names agree. Read for consistency only.
- M5 PSF: the table shows V1-V4, A1, A2, A4, K2, K3, K4 (read from the image, p. 14); the text layer carries the same codes, with V4 displaced after K4.
- D3: Advance HE's web page for the series (current status, date, the 2025 file revision) not reached; wanted.
- M2: 49 label(s) not held in the text layer (read from the page image; `span: none`); MD-2 cannot check them by script.

---

## Change notes
- 0.1.1, 2026-10-04 09:26: practice themes aligned across the series by std (16 id(s) renamed by tools/theme_merges.json; the old ids are aliases in the shared theme register); rebuilt on builder 0.2.1. Model template 0.3.0-draft, builder 0.2.1: 49 components, 0 open segments, 16 statements, 12 practice themes.
- 0.1.0, 2026-10-04 09:23: first built (Abbott, 09:08: "Use your template model and refine as you go"; D-std-0018). Model template 0.2.0-draft, builder 0.2.0: 49 components, 0 open segments, 16 statements, 12 practice themes.
