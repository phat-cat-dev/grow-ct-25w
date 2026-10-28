---
id: std:doc:advancehe-inclusive-learning-teaching-2024-model
title: "Inclusive learning and teaching framework"
profile: standards/model
profileVersion: none yet   # the variant's profile part is to write
issuer: Advance HE
kind: model
modelKind: condition-model
series: advancehe-student-success-frameworks-2024
axes: { perspectives: 3, facets: 0, groups: 0, segments: 14, openSegments: 3, labelsNotInText: 0 }
jurisdiction: [UK]   # not stated; Advance HE is UK-based and its frameworks are used internationally (inferred)
subjectScope: universal
subjects: []
edition: "digital edition, 2024"
published: 2024   # no date printed; from the PDF metadata (Part E)
revised: "none-stated"   # a later file date, if any (Part E)
status: current   # as at the held text; not checked against Advance HE's site (D3)
supersedes: "none-stated"
heldText: { method: sha256-bytes, raw: 5c9b382f3d546b495c8c8ed714068b7173a8d019a783163ab431d294ee494845, normalised: 133761bde238c1141e2a3f93f8b2031d07700d6e742a84a96ee66565258df494 }
original: { method: sha256-bytes, pdf: d4f6264fdcdc88431b9f2e8d9d892c88bfd6073b8452712e57ebc300c57fff18, held: "library pdf/advance-he-2024-inclusive-learning-teaching-framework-standard.pdf" }
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
# Inclusive learning and teaching framework

> The issuer's text is held beside this document in the library (`txt/advance-he-2024-inclusive-learning-teaching-framework-standard.norm.txt`). Each M2 `label` (where the text layer holds it), each `explainedBy` and M4 `source` and each S4 `source` is exactly its span's text, held for language analysis (D-std-0014); private, never published. Every other field is ours, and agents phrase from ours.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
A practice model from Advance HE's Student Success Frameworks: fourteen components of inclusive learning and teaching, seen from the institution, educators and students, each held here as a practice theme that can qualify the context of a lesson or a piece of material. Reach for it to set or check the conditions under which students learn. It sets no levels and no outcomes: pair it with a framework or benchmark for what students achieve.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Advance HE (2024) sets out inclusive learning and teaching as the deliberate shaping of approaches so that every student can thrive, and as the foundation of quality rather than a competing priority. It draws three dials, one for each of the institution, educators and related staff, and students, with five, five and four named segments and one segment in each left blank for what is not yet known. Four requirements frame it, and a short list of uses is given for each perspective. It states that it bears on every dimension of the Professional Standards Framework 2023 and invites its use as Fellowship evidence. It binds no one: it is an enhancement model, not an assurance standard.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: Advance HE
title: "Inclusive learning and teaching framework"
series: "Advance HE Student Success Frameworks"
edition: "digital edition, 2024"
dates:
  published: 2024   # not printed; PDF metadata
  other: ["PDF created 25 June 2024", "PDF modified 8 July 2024"]
kind: model
jurisdiction: [UK]
authority: advisory
licence: "none stated in the file (D1)"
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the conditions for inclusive learning and teaching across an institution, its teaching and its students' experience (D1, pp. 2-3)"
appliesTo:
  awards: [none-stated]
  levels: [none]
  providers: ["higher education institutions (as stated: \"our institutions\")"]
whoMustUse: "no one must; offered to anyone with input into student learning, outcomes or experience, and named as particularly useful to academic developers, module and course leaders, facilitators, decision makers and students' unions (D1, pp. 2-3)"
howUsed: ["design", "review", "other: strategy, staff development, Fellowship evidence"]
doesNot: "none-stated"
beneficiary: the student
statedScope: "This framework is relevant to anyone, in any role, that has input into student learning, student outcomes, and/or the student experience in any shape or form."
statedScopeLocator: "D1, p. 3"
statedScopeSpan: { start: 1877, end: 2035 }
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "what-is", order: 1, componentType: section, parent: "none", heading: "What is inclusive learning and teaching in higher education?", gloss: "definition, the mindset and the four requirements", pages: "2-3", readFrom: "text layer" }
  - { number: "requires", order: 2, componentType: stem, parent: "what-is", heading: "Inclusive learning and teaching requires:", gloss: "the lead-in to the four requirements", pages: "3", readFrom: "text layer" }
  - { number: "who-for", order: 3, componentType: section, parent: "none", heading: "Who is the framework for?", gloss: "audiences: academic developers, module and course leaders, facilitators, decision makers, students' unions", pages: "2-3", readFrom: "text layer" }
  - { number: "why", order: 4, componentType: section, parent: "none", heading: "Why is inclusive learning and teaching important?", gloss: "rationale: rethinking practice; psychological safety and lived experience", pages: "4", readFrom: "text layer" }
  - { number: "structure", order: 5, componentType: figure, parent: "none", heading: "How is the framework structured?", gloss: "the three perspectives shared by the series", pages: "5", readFrom: "figure image" }
  - { number: "institution", order: 6, componentType: perspective, parent: "none", heading: "Institution", gloss: "framing prose for the institution", pages: "6", readFrom: "text layer" }
  - { number: "institution.dial", order: 7, componentType: figure, parent: "institution", heading: "(dial)", gloss: "five segments and one open segment", pages: "7", readFrom: "figure image" }
  - { number: "educators", order: 8, componentType: perspective, parent: "none", heading: "Educators and related staff", gloss: "framing prose for educators; the hidden curriculum", pages: "8-9", readFrom: "text layer" }
  - { number: "educators.dial", order: 9, componentType: figure, parent: "educators", heading: "(dial)", gloss: "five segments and one open segment", pages: "9", readFrom: "figure image" }
  - { number: "students", order: 10, componentType: perspective, parent: "none", heading: "Students", gloss: "framing prose for students: mattering, psychological safety", pages: "10-11", readFrom: "text layer" }
  - { number: "students.dial", order: 11, componentType: figure, parent: "students", heading: "(dial)", gloss: "four segments and one open segment", pages: "11", readFrom: "figure image" }
  - { number: "use", order: 12, componentType: use-list, parent: "none", heading: "How can you use the framework?", gloss: "purpose, the open segments, three uses for each perspective", pages: "12-13", readFrom: "figure image" }
  - { number: "psf", order: 13, componentType: section, parent: "none", heading: "How does this framework align with the Professional Standards Framework (PSF) 2023?", gloss: "the PSF crosswalk table and the Fellowship invitation", pages: "14", readFrom: "text layer" }
excluded:
  - { number: "back-cover", heading: "We help higher education organisations be the best they can be ...", kind: "other: the issuer's promotional back cover", pages: "15" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only obliging framing lines, requirement lists and use lists are statements (model template rule 3). -->
```yaml
- id: advancehe/inclusive-2024/requires.b1
  locator: { number: "requires.b1", heading: "Inclusive learning and teaching requires:", page: 3 }
  span: { start: 1211, end: 1273 }
  source: "understanding that the status quo is not a level playing field"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: requires
  statementType: requirement
  force: must   # D-std-0016: "requires" (lead-in) read as must
  level: none
  perspective: none
  mood: gerund
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["understanding"]
  about: "unequal starting points"
  themes: ["none"]
  paraphrase: "Requires recognising that existing arrangements do not give every student an equal start."
  audience: practitioner
  subjects: inherited
- id: advancehe/inclusive-2024/requires.b2
  locator: { number: "requires.b2", heading: "Inclusive learning and teaching requires:", page: 3 }
  span: { start: 1274, end: 1351 }
  source: "actively seeking to know the unexpected impacts we might have on our students"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: requires
  statementType: requirement
  force: must   # D-std-0016: "requires" (lead-in) read as must
  level: none
  perspective: none
  mood: gerund
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["seeking", "know", "have"]
  about: "finding out unintended effects on students"
  themes: ["none"]
  paraphrase: "Requires going out of one's way to discover the effects one has on students that were not intended."
  audience: practitioner
  subjects: inherited
- id: advancehe/inclusive-2024/requires.b3
  locator: { number: "requires.b3", heading: "Inclusive learning and teaching requires:", page: 3 }
  span: { start: 1352, end: 1440 }
  source: "welcome different ways of working for all students without needing “evidence” or “proof”"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: requires
  statementType: requirement
  force: must   # D-std-0016: "requires" (lead-in) read as must
  level: none
  perspective: none
  mood: infinitive
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["welcome", "working", "needing"]
  about: "accepting other ways of working without demanding proof"
  themes: ["none"]
  paraphrase: "Requires accepting that students may work in different ways without asking them to justify or prove why."
  audience: both
  subjects: inherited
- id: advancehe/inclusive-2024/requires.b4
  locator: { number: "requires.b4", heading: "Inclusive learning and teaching requires:", page: 3 }
  span: { start: 1441, end: 1581 }
  source: "reviewing our practices, processes and curricula by critically examining what is truly “non-negotiable”, and designing flexibly around this."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: requires
  statementType: requirement
  force: must   # D-std-0016: "requires" (lead-in) read as must
  level: none
  perspective: none
  mood: gerund
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["reviewing", "examining", "designing"]
  about: "separating the fixed from the flexible in design"
  themes: ["none"]
  paraphrase: "Requires reviewing practice, process and curriculum to find what genuinely cannot change, and building flexibility around it."
  audience: practitioner
  subjects: inherited
- id: advancehe/inclusive-2024/frame.institution
  locator: { number: "frame.institution", heading: "Institution", page: 6 }
  span: { start: 4597, end: 4762 }
  source: "It is important that institutions consider and implement policies and practices which are culturally aligned yet able to recognise the fluidity of evolving contexts."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # "it is important that" read as should: not in D-std-0016's list; proposed (Part E)
  level: none
  perspective: perspective:institution
  mood: declarative
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["consider", "implement", "recognise"]
  about: "policy that fits culture and adapts to change"
  themes: ["none"]
  paraphrase: "Institutions should adopt policies and practices that fit their culture while staying able to respond as circumstances change."
  audience: practitioner
  subjects: inherited
- id: advancehe/inclusive-2024/frame.educators
  locator: { number: "frame.educators", heading: "Educators and related staff", page: 9 }
  span: { start: 6498, end: 6705 }
  source: "It is important that staff continually seek to change practices which are within their personal sphere of control, and actively use successes as leverage for challenging existing structures when appropriate."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # "it is important that" read as should: not in D-std-0016's list; proposed (Part E)
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["seek", "change", "use", "challenging"]
  about: "changing what is in one's control, then structures"
  themes: ["none"]
  paraphrase: "Staff should keep changing the practices they control, and use what works as grounds to question wider structures where that is right."
  audience: practitioner
  subjects: inherited
- id: advancehe/inclusive-2024/use.institution.1
  locator: { number: "use.institution.1", heading: "How can you use the framework?", page: 12 }
  span: { start: 9547, end: 9642 }
  source: "Develop leadership and structures to prioritise cultures of inclusion in learning and teaching."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["Develop", "prioritise"]
  about: "leadership and structures for inclusion"
  themes: ["none"]
  paraphrase: "Institutions should build leadership and structures that put inclusive cultures of learning and teaching first."
  audience: practitioner
  subjects: inherited
- id: advancehe/inclusive-2024/use.institution.2
  locator: { number: "use.institution.2", heading: "How can you use the framework?", page: 12 }
  span: { start: 8890, end: 9004 }
  source: "Inform and enhance strategic priorities, mapping how inclusive learning and teaching aligns with these priorities."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["Inform", "enhance", "mapping", "aligns"]
  about: "linking inclusion to strategy"
  themes: ["none"]
  paraphrase: "Institutions should use the model to shape strategy and show where inclusive learning and teaching fits it."
  audience: practitioner
  subjects: inherited
- id: advancehe/inclusive-2024/use.institution.3
  locator: { number: "use.institution.3", heading: "How can you use the framework?", page: 12 }
  span: { start: 10064, end: 10194 }
  source: "Welcome diverse perspectives, and be accountable for ensuring critical, divergent, or marginalised perspectives are not dismissed."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["Welcome", "ensuring", "dismissed"]
  about: "accountability for unheard views"
  themes: ["none"]
  paraphrase: "Institutions should seek a range of views and answer for making sure that critical and marginalised ones are not brushed aside."
  audience: practitioner
  subjects: inherited
- id: advancehe/inclusive-2024/use.educators.1
  locator: { number: "use.educators.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 9644, end: 9788 }
  source: "Notice how your practices might impact students, and question your assumptions around what excellence and appropriate behaviour might look like."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:educators
  mood: imperative
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["Notice", "impact", "question", "look"]
  about: "checking one's assumptions about excellence"
  themes: ["none"]
  paraphrase: "Staff should watch for the effects of their practice on students and test their assumptions about what excellent work and proper conduct are."
  audience: practitioner
  subjects: inherited
- id: advancehe/inclusive-2024/use.educators.2
  locator: { number: "use.educators.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 9006, end: 9157 }
  source: "Make decisions in your own context with compassion, understanding that policies, processes and notions of evidence may reinforce barriers to inclusion."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E); "may" here is possibility, not permission
  level: none
  perspective: perspective:educators
  mood: imperative
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: provider
  verbs: ["Make", "understanding", "reinforce"]
  about: "compassionate local decisions"
  themes: ["none"]
  paraphrase: "Staff should decide with compassion in their own setting, aware that rules, processes and evidence demands can themselves create barriers."
  audience: practitioner
  subjects: inherited
- id: advancehe/inclusive-2024/use.educators.3
  locator: { number: "use.educators.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 9158, end: 9281 }
  source: "Be empowered – and empower students – to explore what enables them to thrive, and support them in trusting their judgement."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:educators
  mood: imperative
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: both
  verbs: ["empowered", "empower", "explore", "enables", "thrive", "support", "trusting"]
  about: "mutual empowerment and trust in judgement"
  themes: ["none"]
  paraphrase: "Staff should take up their own agency, extend it to students, help them find what lets them thrive and back their judgement."
  audience: both
  subjects: inherited
- id: advancehe/inclusive-2024/use.students.1
  locator: { number: "use.students.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 9790, end: 9902 }
  source: "Be supported to develop in authentic, meaningful ways, rather than expected to fit into unsuitable environments."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # entitlement read as should (proposed; Part E)
  level: none
  perspective: perspective:students
  mood: entitlement
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: learner
  verbs: ["supported", "develop", "expected", "fit"]
  about: "developing as oneself, not fitting in"
  themes: ["none"]
  paraphrase: "Students should be helped to develop in ways that are genuine and meaningful to them, not made to fit settings that do not suit them."
  audience: both
  subjects: inherited
- id: advancehe/inclusive-2024/use.students.2
  locator: { number: "use.students.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 9914, end: 9963 }
  source: "Be treated like they matter, and with compassion."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # entitlement read as should (proposed; Part E)
  level: none
  perspective: perspective:students
  mood: entitlement
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: learner
  verbs: ["treated", "matter"]
  about: "being treated as mattering"
  themes: ["none"]
  paraphrase: "Students should be treated as people who count, and with compassion."
  audience: both
  subjects: inherited
- id: advancehe/inclusive-2024/use.students.3
  locator: { number: "use.students.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 9964, end: 10062 }
  source: "Be empowered to explore what enables them to thrive, and support them in trusting their judgement."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # entitlement read as should (proposed; Part E)
  level: none
  perspective: perspective:students
  mood: entitlement
  readFrom: "text layer"
  appliesTo: "inclusive learning and teaching framework"
  addressee: learner
  verbs: ["empowered", "explore", "enables", "thrive", "support", "trusting"]
  about: "finding what helps one thrive"
  themes: ["none"]
  paraphrase: "Students should be enabled to find out what helps them thrive and be supported to trust their own judgement."
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- statement: advancehe/inclusive-2024/requires.b1
  forPractitioner: { text: "Start from the recognition that current arrangements do not put all students on equal terms; this is required, not optional.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a stance required of staff and the institution, not of the student", rewrite: full, force: must, status: drafted }
  author-agent-written: "State this as the first requirement the issuer sets for inclusive learning and teaching, with must force from \"requires\". Do not restate it as a claim about any one group."
  author-agent-dialogue: "Raise it when someone assumes fairness means treating everyone identically. Ask: \"Does everyone start this from the same place?\" Avoid lecturing."
- statement: advancehe/inclusive-2024/requires.b2
  forPractitioner: { text: "Find out, actively, how your practice affects students in ways you did not intend; waiting for complaints does not meet this requirement.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on staff and the institution", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an active duty to look for unintended effects, with must force. Link it to the hidden curriculum and to the anticipating-difference component."
  author-agent-dialogue: "Raise it when a practice is defended because no one has complained. Ask: \"How would you know if this affected some students badly?\" Avoid implying bad intent."
- statement: advancehe/inclusive-2024/requires.b3
  forPractitioner: { text: "Accept different ways of working from any student without first asking for documentation or proof of need.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "You should not have to prove a need before you are allowed to work in a way that suits you.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Note the issuer puts \"evidence\" and \"proof\" in quotation marks, signalling a critique of evidence demands; keep that nuance. The force is must, from the lead-in. Do not present it as removing formal adjustment processes."
  author-agent-dialogue: "Raise it when a student is asked to justify a reasonable preference. Ask: \"What would it cost to allow this for anyone who asks?\" Avoid contradicting formal disability processes; this is about everyday flexibility."
- statement: advancehe/inclusive-2024/requires.b4
  forPractitioner: { text: "Review your course to separate what genuinely cannot change from what is habit, then design flexibly around the fixed core.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on course design, met by staff", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a design method: identify the truly fixed requirements, then flex the rest. Keep the quotation marks' implication that much called fixed is not."
  author-agent-dialogue: "Raise it during course design or review. Ask: \"Which of these requirements would the subject itself fail without, and which are habit?\" Avoid treating every requirement as negotiable."
- statement: advancehe/inclusive-2024/frame.institution
  forPractitioner: { text: "Set policies that fit the institution's culture and still respond to changing circumstances; review them for both.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present as the framing expectation of the institution perspective, force should (our reading of \"it is important that\"). Link it to the contextual adaptation component."
  author-agent-dialogue: "Raise it in discussion of policy review. Ask: \"Does this policy still fit the students we now have?\" Avoid detail the institution has not stated."
- statement: advancehe/inclusive-2024/frame.educators
  forPractitioner: { text: "Change what is within your own control first and keep doing so; then use what worked as evidence to argue for wider structural change.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present as the framing expectation of the educators' perspective, force should (our reading). Note its two steps: local change, then leverage. Link it to the challenge-structures component."
  author-agent-dialogue: "Raise it when a teacher feels powerless. Ask: \"What here is within your control?\" and later \"What has worked that you could use to argue for more?\" Avoid urging confrontation."
- statement: advancehe/inclusive-2024/use.institution.1
  forPractitioner: { text: "Use the model to shape leadership roles and structures so that inclusion in learning and teaching is a priority, not an add-on.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "One of three uses the issuer gives for institutions; force should (imperative, our reading). Link to the reconfigure-structures component."
  author-agent-dialogue: "Raise it with leaders. Ask: \"Who owns inclusion in learning and teaching here, and with what authority?\" Avoid assuming a structure exists."
- statement: advancehe/inclusive-2024/use.institution.2
  forPractitioner: { text: "Map inclusive learning and teaching against the institution's strategic priorities and use the model to improve them.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "A use of the model for strategy; force should (our reading). Do not overstate it as a requirement."
  author-agent-dialogue: "Raise it in strategy work. Ask: \"Where does inclusive teaching appear in our priorities, and where is it missing?\""
- statement: advancehe/inclusive-2024/use.institution.3
  forPractitioner: { text: "Seek a range of views, and be answerable for making sure that critical, minority and marginalised views are acted on rather than brushed aside.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Stress accountability, which goes beyond welcoming. Link to the diversity-of-voice component."
  author-agent-dialogue: "Raise it when consultation is described. Ask: \"Which critical views were heard, and what happened to them?\""
- statement: advancehe/inclusive-2024/use.educators.1
  forPractitioner: { text: "Watch for how your practice affects different students, and test your own picture of what excellent work and proper conduct look like.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Note the reflexive turn: the assumptions examined are the educator's own. Link to anticipating difference and the hidden curriculum."
  author-agent-dialogue: "Raise it in reflection on marking or conduct expectations. Ask: \"Where did your idea of excellent work come from, and who does it suit?\""
- statement: advancehe/inclusive-2024/use.educators.2
  forPractitioner: { text: "Decide with compassion in your own setting, aware that rules, procedures and demands for evidence can themselves be barriers.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Note the claim that notions of evidence can be a barrier, which links to requirement b3. Link to the compassionate pedagogies component."
  author-agent-dialogue: "Raise it when a decision is being made by the book. Ask: \"Could the rule itself be the barrier here?\""
- statement: advancehe/inclusive-2024/use.educators.3
  forPractitioner: { text: "Take up your own agency and extend it to students: help them find out what lets them thrive, and back their judgement.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "You are encouraged to find out what helps you thrive and to trust your own judgement.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). It addresses staff and students at once. Link to both self-actualisation components."
  author-agent-dialogue: "Raise it when a student defers to staff on how they learn best. Ask: \"What have you found works for you?\""
- statement: advancehe/inclusive-2024/use.students.1
  forPractitioner: { text: "Support students to develop in ways that are genuine and meaningful to them, and change unsuitable settings rather than asking students to fit them.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "You should be helped to grow in ways that are real and meaningful to you, not expected to squeeze into a setting that does not suit you.", rewrite: full, force: should, status: drafted }
  author-agent-written: "An entitlement: what students should receive; force should (our reading). Link to the authentic-learners component."
  author-agent-dialogue: "Raise it when a student is struggling to fit a format. Ask: \"What would let you do this in a way that works for you?\""
- statement: advancehe/inclusive-2024/use.students.2
  forPractitioner: { text: "Treat every student as someone who counts, and with compassion, in every contact.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "You should be treated as someone who counts, and with compassion.", rewrite: full, force: should, status: drafted }
  author-agent-written: "An entitlement; force should (our reading). Link to the mattering component."
  author-agent-dialogue: "Raise it when a student reports being dismissed. Ask: \"What happened, and who could you raise it with?\""
- statement: advancehe/inclusive-2024/use.students.3
  forPractitioner: { text: "Enable students to find out what helps them thrive, and support them to trust their own judgement.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "You should have the chance to find out what helps you thrive and support to trust your own judgement.", rewrite: full, force: should, status: drafted }
  author-agent-written: "An entitlement; force should (our reading). Note the second clause shifts to the supporter (\"support them\"). Link to the students' self-actualisation component."
  author-agent-dialogue: "Raise it in tutorials on study approaches. Ask: \"What conditions help you do your best work?\""
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
- { id: theme:edi, role: carries, carriedIn: ["what-is", "why", "institution", "educators", "students", "use"], basis: "inferred: the document is about inclusion throughout but never names EDI (Part E)" }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: partOf, target: "advancehe-student-success-frameworks-2024", note: "Advance HE Student Success Frameworks; the three-perspective structure is shared by the series (D1, p. 5)" }
- { rel: modelledAs, target: "ing:doc:inclusive-learning-teaching-framework-advance-he-2024", note: "the same source run as theory with a dialogue layer (ing run 0137); read for consistency, not used as a source" }
- { rel: alignsWith, target: "std:doc:advancehe-psf-dimensions-2023-framework", note: "stated: relevant to every PSF 2023 dimension (M5)" }
- { rel: partOf, target: "std:doc:advancehe-enhancing-student-success-2024-model", note: "the series overview names inclusive learning and teaching as one of its nine areas" }
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
  - { id: perspective:institution, label: "Institution", page: 7, segments: 5, openSegments: 1 }
  - { id: perspective:educators, label: "Educators and related staff", page: 9, segments: 5, openSegments: 1, note: "labelled \"Educators\" in the structure figure (p. 5) and \"Educators and related staff\" on pp. 8 and 12" }
  - { id: perspective:students, label: "Students", page: 11, segments: 4, openSegments: 1 }
groups: none
use: "to place inclusion at the core of learning and teaching and to move from fixed rules to compassion in everyday choices; each perspective has three uses (S4 use.*) (D1, p. 12)"
```

### M2 Components
<!-- label: both; status: drafted; basis: primary. In the figure's order (Part E). -->
```yaml
- id: advancehe/inclusive-2024/institution.kindness
  label: "Fostering a culture of kindness"
  span: { start: 5053, end: 5084 }
  position: { axis: perspective:institution, group: none, order: 1, page: 7 }
  explainedBy:
    - { span: { start: 8676, end: 8875 }, source: "It empowers readers to take a dynamic approach that moves away from static rules, processes and policies to those of compassion and kindness, acknowledging the impact of the everyday choices we make.", link: stated, page: 12 }
  conditionType: culture
  actor: institution
  about: "kindness as the institution's culture"
  paraphrase: "The institution builds a culture in which care for people shapes everyday decisions, ahead of fixed rules and procedure."
  themes: ["theme:compassion", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/institution.contextual-adaptation
  label: "Creating conditions for contextual adaptation"
  span: { start: 5194, end: 5239 }
  position: { axis: perspective:institution, group: none, order: 2, page: 7 }
  explainedBy:
    - { span: { start: 1003, end: 1168 }, source: "Rather than expecting students to adapt to unsuitable environments, inclusive cultures of learning and teaching anticipate difference and adapt based on the context.", link: stated, page: 3 }
    - { span: { start: 4597, end: 4762 }, source: "It is important that institutions consider and implement policies and practices which are culturally aligned yet able to recognise the fluidity of evolving contexts.", link: stated, page: 6 }
  conditionType: structure
  actor: institution
  about: "room to adapt practice to the setting"
  paraphrase: "Policy and practice leave room for staff to adjust to the setting and the students present, so that the environment changes rather than the student."
  themes: ["theme:contextual-adaptation", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/institution.challenge-structures
  label: "Empowering all to challenge the legitimacy of existing structures"
  span: { start: 5241, end: 5306 }
  position: { axis: perspective:institution, group: none, order: 3, page: 7 }
  explainedBy:
    - { span: { start: 601, end: 707 }, source: "Inclusion is often unintentionally gatekept by those upholding existing policies, practices and processes.", link: inferred, page: 2 }
    - { span: { start: 4763, end: 4884 }, source: "The biggest opportunities for meaningful inclusion and organisational success come from understanding what isn’t working.", link: inferred, page: 6 }
  conditionType: culture
  actor: all
  about: "permission to question existing structures"
  paraphrase: "Staff and students are able, and encouraged, to ask whether existing policies and processes are justified, above all where they keep some students out."
  themes: ["theme:structural-challenge", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/institution.reconfigure-structures
  label: "Being prepared to reconfigure institutional structures"
  span: { start: 5138, end: 5192 }
  position: { axis: perspective:institution, group: none, order: 4, page: 7 }
  explainedBy:
    - { span: { start: 9547, end: 9642 }, source: "Develop leadership and structures to prioritise cultures of inclusion in learning and teaching.", link: stated, page: 12 }
    - { span: { start: 4885, end: 5048 }, source: "Institutional leaders that deliberately seek out heterogeneous views are equipped to drive effective cohesion between inclusive practices, leadership and policies.", link: inferred, page: 6 }
  conditionType: structure
  actor: institution
  about: "willingness to change institutional structures"
  paraphrase: "Leaders are ready to change how the institution is organised when its structures stand in the way of inclusion."
  themes: ["theme:structural-challenge", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/institution.diversity-of-voice
  label: "Fostering diversity of voice to centre inclusivity"
  span: { start: 5086, end: 5136 }
  position: { axis: perspective:institution, group: none, order: 5, page: 7 }
  explainedBy:
    - { span: { start: 10064, end: 10194 }, source: "Welcome diverse perspectives, and be accountable for ensuring critical, divergent, or marginalised perspectives are not dismissed.", link: stated, page: 12 }
    - { span: { start: 4885, end: 4953 }, source: "Institutional leaders that deliberately seek out heterogeneous views", link: stated, page: 6 }
  conditionType: practice
  actor: institution
  about: "many voices heard in decisions"
  paraphrase: "Decisions draw on a wide range of voices, and dissenting or marginalised views are sought out and acted on rather than set aside."
  themes: ["theme:student-voice-partnership", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/educators.compassionate-relational
  label: "Compassionate, relational pedagogies"
  span: { start: 6707, end: 6743 }
  position: { axis: perspective:educators, group: none, order: 1, page: 9 }
  explainedBy:
    - { span: { start: 9006, end: 9157 }, source: "Make decisions in your own context with compassion, understanding that policies, processes and notions of evidence may reinforce barriers to inclusion.", link: stated, page: 13 }
    - { span: { start: 2449, end: 2592 }, source: "the framework gives principles to support facilitators of learning and teaching to both anticipate and respond compassionately to student need.", link: stated, page: 3 }
  conditionType: relationship
  actor: educator
  about: "teaching built on care and relationship"
  paraphrase: "Teaching rests on relationships of care: staff respond to what students need with compassion and judge each case in its setting."
  themes: ["theme:compassion", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/educators.self-actualisation
  label: "Self-actualisation"
  span: { start: 6842, end: 6860 }
  position: { axis: perspective:educators, group: none, order: 2, page: 9 }
  explainedBy:
    - { span: { start: 717, end: 838 }, source: "this framework positions the facilitation of student and staff self-actualisation as key to promoting inclusive cultures.", link: stated, page: 2 }
    - { span: { start: 839, end: 934 }, source: "We can do this by supporting staff and students to develop and believe in their own judgements.", link: stated, page: 2 }
  conditionType: disposition
  actor: all
  about: "staff and students growing into their own judgement"
  paraphrase: "Staff and students are helped to develop, and to trust, their own judgement, as the way to an inclusive culture."
  themes: ["theme:agency-self-actualisation", "theme:edi"]
  sameLabelAs: advancehe/inclusive-2024/students.self-actualisation
- id: advancehe/inclusive-2024/educators.critical-thinkers
  label: "Empowering students to be critical thinkers"
  span: { start: 6862, end: 6905 }
  position: { axis: perspective:educators, group: none, order: 3, page: 9 }
  explainedBy:
    - { span: { start: 7887, end: 7999 }, source: "This includes using all learning episodes to promote students’ critical thinking, agency and power to influence.", link: stated, page: 11 }
    - { span: { start: 491, end: 600 }, source: "Rather than an end goal, inclusion is a mindset which promotes critical thinking and cultural transformation.", link: stated, page: 2 }
  conditionType: practice
  actor: educator
  about: "developing students' critical thinking"
  paraphrase: "Staff use every learning activity to build students' critical thinking and their sense that they can influence what happens."
  themes: ["theme:critical-thinking", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/educators.authentic-learners
  label: "Recognising students and selves as authentic learners"
  span: { start: 6787, end: 6840 }
  position: { axis: perspective:educators, group: none, order: 4, page: 9 }
  explainedBy:
    - { span: { start: 962, end: 1002 }, source: "work in ways that are authentic to them.", link: stated, page: 3 }
    - { span: { start: 9790, end: 9902 }, source: "Be supported to develop in authentic, meaningful ways, rather than expected to fit into unsuitable environments.", link: stated, page: 13 }
  conditionType: disposition
  actor: educator
  about: "learning as one's genuine self"
  paraphrase: "Staff treat students, and themselves, as learners who bring who they are to their study, rather than people who must fit one mould."
  themes: ["theme:authenticity", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/educators.anticipating-difference
  label: "Anticipating difference without judgment"
  span: { start: 6745, end: 6785 }
  position: { axis: perspective:educators, group: none, order: 5, page: 9 }
  explainedBy:
    - { span: { start: 1071, end: 1168 }, source: "inclusive cultures of learning and teaching anticipate difference and adapt based on the context.", link: stated, page: 3 }
    - { span: { start: 9644, end: 9788 }, source: "Notice how your practices might impact students, and question your assumptions around what excellence and appropriate behaviour might look like.", link: inferred, page: 13 }
    - { span: { start: 5915, end: 6050 }, source: "One aspect of this may be the hidden curriculum, namely the unspoken rules we have around what it means to succeed in higher education.", link: inferred, page: 8 }
  conditionType: practice
  actor: educator
  about: "planning for difference in advance"
  paraphrase: "Staff expect students to differ, plan for that from the start, and do not measure students against an assumed typical student."
  themes: ["theme:anticipating-difference", "theme:hidden-curriculum", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/students.mattering
  label: "Mattering"
  span: { start: 8286, end: 8295 }
  position: { axis: perspective:students, group: none, order: 1, page: 11 }
  explainedBy:
    - { span: { start: 7001, end: 7135 }, source: "Treating students like they matter means seeing their experiences and needs as legitimate, and an important factor in decision-making.", link: stated, page: 10 }
    - { span: { start: 7233, end: 7334 }, source: "it is the process and mindset we use to make decisions in which we show students whether they matter.", link: stated, page: 10 }
  conditionType: relationship
  actor: all
  about: "students knowing they count"
  paraphrase: "Students' experiences and needs are taken as legitimate and weigh in decisions, so that each student can see they count."
  themes: ["theme:belonging-mattering", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/students.self-actualisation
  label: "Self-actualisation"
  span: { start: 8332, end: 8350 }
  position: { axis: perspective:students, group: none, order: 2, page: 11 }
  explainedBy:
    - { span: { start: 7642, end: 7748 }, source: "highlights that all students matter, if they are to build confidence and enhance their self-actualisation.", link: stated, page: 11 }
    - { span: { start: 9964, end: 10062 }, source: "Be empowered to explore what enables them to thrive, and support them in trusting their judgement.", link: stated, page: 13 }
  conditionType: disposition
  actor: student
  about: "students growing into their own judgement"
  paraphrase: "Students build the confidence to work out what helps them thrive and to trust their own judgement."
  themes: ["theme:agency-self-actualisation", "theme:edi"]
  sameLabelAs: advancehe/inclusive-2024/educators.self-actualisation
- id: advancehe/inclusive-2024/students.critical-thinking
  label: "Recognising the value of critical thinking"
  span: { start: 8352, end: 8394 }
  position: { axis: perspective:students, group: none, order: 3, page: 11 }
  explainedBy:
    - { span: { start: 7887, end: 7999 }, source: "This includes using all learning episodes to promote students’ critical thinking, agency and power to influence.", link: stated, page: 11 }
  conditionType: disposition
  actor: student
  about: "students valuing critical thinking"
  paraphrase: "Students come to see critical thinking as worth doing and as a way to have a say in their learning."
  themes: ["theme:critical-thinking", "theme:edi"]
  sameLabelAs: none
- id: advancehe/inclusive-2024/students.psychological-safety
  label: "Psychologically safe environments"
  span: { start: 8297, end: 8330 }
  position: { axis: perspective:students, group: none, order: 4, page: 11 }
  explainedBy:
    - { span: { start: 7335, end: 7482 }, source: "Through everyday actions we can create psychological safety by listening receptively, valuing feelings and understanding the importance of context.", link: stated, page: 10 }
    - { span: { start: 8142, end: 8284 }, source: "Creating psychologically safe environments enables students to work effectively and safely with people from different and diverse backgrounds.", link: stated, page: 11 }
    - { span: { start: 4115, end: 4260 }, source: "This enables psychologically safe environments that allow truly dialogic conversations that embed lived experience as a crucial form of evidence.", link: stated, page: 5 }
  conditionType: environment
  actor: all
  about: "safety to speak and to err"
  paraphrase: "Students and staff can speak up, ask, disagree and get things wrong without fear of being judged or penalised."
  themes: ["theme:psychological-safety", "theme:edi"]
  sameLabelAs: none
```

### M2a Component audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- component: advancehe/inclusive-2024/institution.kindness
  forPractitioner: { text: "Make kindness part of how the institution runs: in policy, in how decisions are explained and in how staff are treated, so that care is the norm and not a favour.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the people and systems around your study to treat you with care, and to explain decisions that affect you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a cultural condition set by the institution, not a teaching technique. Do not present kindness as softness or lowered expectations; present it as how rules are applied. Set it beside the compassionate, relational pedagogies component, which is its classroom form."
  author-agent-dialogue: "Raise it when a person describes a rule applied without regard to circumstance. Ask: \"Where does a rule here get in the way of treating someone fairly?\" and \"Who could you ask to apply it with more discretion?\" Avoid moralising about individual staff."
- component: advancehe/inclusive-2024/institution.contextual-adaptation
  forPractitioner: { text: "Write policies that set a purpose and leave staff room to adapt how it is met, and review them as the student body and setting change.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your course to adjust how things are done when the usual way does not work for the people taking it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the institutional permission that makes local adaptation possible. Do not imply that any adaptation is allowed: the purpose of a policy stays; the means can flex. Link it to anticipating difference, which is what staff do with that permission."
  author-agent-dialogue: "Raise it when staff say \"the system will not let me\". Ask: \"What is the purpose of this rule, and is there more than one way to meet it?\" Avoid promising flexibility the institution has not granted."
- component: advancehe/inclusive-2024/institution.challenge-structures
  forPractitioner: { text: "Make it safe and expected for anyone to ask why a process exists and whom it excludes, and act on what the questions reveal.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You are entitled to ask why things are done the way they are, especially if a rule seems to work against some students.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as legitimate questioning, not as rule-breaking. Do not encourage ignoring requirements; encourage asking whether they are justified and raising it through a route that can change them."
  author-agent-dialogue: "Raise it when a person accepts an excluding practice as fixed. Ask: \"Who does this arrangement suit, and who does it leave out?\" and \"Where could you raise that?\" Avoid turning it into blame of named people."
- component: advancehe/inclusive-2024/institution.reconfigure-structures
  forPractitioner: { text: "Treat structures (committees, timetables, assessment regulations, roles) as open to redesign when evidence shows they exclude, and give leaders the remit to redesign them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your university to change how it is organised, not only to ask you to cope, when the way it works shuts some students out.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the institution's side of the bargain: questioning (the challenge component) leads somewhere only if structures can change. Do not overstate it as a promise of any particular change."
  author-agent-dialogue: "Raise it when a fix is being sought from individuals for a structural problem. Ask: \"Is this a problem one tutor can solve, or one the structure creates?\" Avoid suggesting that staff alone should absorb structural failings."
- component: advancehe/inclusive-2024/institution.diversity-of-voice
  forPractitioner: { text: "Seek out views that differ from the majority, students' included, before deciding; record how they shaped the decision, and answer for any that were set aside.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your view counts, including when it differs from most people's, and you can expect to hear what was done with it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe voice as something sought and answered for, not merely allowed. Do not equate it with surveys alone. Link it to partnership and co-creation with students."
  author-agent-dialogue: "Raise it when a decision is described with no mention of who was consulted. Ask: \"Whose view is missing here?\" and \"How would they hear what happened to their input?\" Avoid tokenism, such as one student speaking for all."
- component: advancehe/inclusive-2024/educators.compassionate-relational
  forPractitioner: { text: "Build working relationships with students, learn enough about their circumstances to respond well, and use your discretion with care where a rule or a habit would harm.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the people who teach you to know you as a person and to respond to what you need with care.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a pedagogy (how teaching is done), grounded in relationship. Do not reduce it to pastoral support or to being nice; it includes holding high expectations with care."
  author-agent-dialogue: "Raise it when a teacher describes a student only by performance. Ask: \"What do you know about what is going on for this student?\" and \"What would a caring response look like that still keeps the standard?\" Avoid implying staff must solve every personal difficulty."
- component: advancehe/inclusive-2024/educators.self-actualisation
  forPractitioner: { text: "Give staff and students the room and the support to make judgements of their own, and back them when they do.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You are supported to grow into your own judgement and to trust it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Use the issuer's term, self-actualisation, and gloss it as growing into and trusting one's own judgement; note that it applies to staff as well as students here. Do not attribute the term to Maslow without saying the source does not."
  author-agent-dialogue: "Raise it when a person defers every judgement to a rule or an authority. Ask: \"What do you think is right here, and why?\" Avoid pushing confidence where the person needs information first."
- component: advancehe/inclusive-2024/educators.critical-thinkers
  forPractitioner: { text: "Design each activity so students question claims, weigh evidence and form a view, and show them that their reasoning can change things.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will be asked to question, weigh evidence and form your own view, and that view can make a difference.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Tie critical thinking to agency, as the source does: thinking critically includes the power to act on it. Do not present it only as an academic skill."
  author-agent-dialogue: "Raise it when a task asks only for recall. Ask: \"Where in this task does the student question or judge something?\" Avoid treating criticism as negativity."
- component: advancehe/inclusive-2024/educators.authentic-learners
  forPractitioner: { text: "Recognise the experience, identity and ways of working that students and colleagues bring, and let them show in how learning is done.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can bring who you are and what you know to your learning; you do not have to become someone else to succeed.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Note that the component names staff too (\"selves\"): educators are learners. Do not confuse it with authentic assessment, which is a different idea; link to it only as a related practice."
  author-agent-dialogue: "Raise it when a person feels they must hide their background or way of working to fit in. Ask: \"What do you bring that this task could use?\" Avoid assuming what anyone's identity is."
- component: advancehe/inclusive-2024/educators.anticipating-difference
  forPractitioner: { text: "Design for the range of students you will have, not for an imagined typical one; make unwritten expectations explicit, and check your own assumptions about what good looks like.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your course to be designed with different students in mind, and the unwritten rules of study to be explained.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as design in advance, not reaction after a problem. Link it to the hidden curriculum, which the source raises in the same section. Do not equate difference with deficit."
  author-agent-dialogue: "Raise it when a teacher plans for \"the average student\". Ask: \"Who might find this harder for reasons that have nothing to do with ability?\" and \"What unwritten rule does this task rely on?\" Avoid listing groups as problems."
- component: advancehe/inclusive-2024/students.mattering
  forPractitioner: { text: "Treat what students tell you about their experience as evidence, let it weigh in decisions, and show them that it did.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You matter: your experience and needs are taken seriously and count when decisions are made.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present mattering as shown through how decisions are made, as the source does, not as a feeling staff should induce. Link it to belonging, which it underpins."
  author-agent-dialogue: "Raise it when a student doubts they are noticed. Ask: \"When did someone here act on something you told them?\" Avoid reassurance with no evidence behind it."
- component: advancehe/inclusive-2024/students.self-actualisation
  forPractitioner: { text: "Help students find out what helps them learn and thrive, and build their confidence to act on their own judgement.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You are supported to find out what helps you thrive and to trust your own judgement.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Gloss the issuer's term as growing in confidence and trusting one's own judgement; note the source ties it to mattering. Do not present it as an endpoint students reach."
  author-agent-dialogue: "Raise it when a student asks to be told the right way. Ask: \"What has worked for you before?\" and \"What would you choose, and why?\" Avoid withholding guidance the student needs."
- component: advancehe/inclusive-2024/students.critical-thinking
  forPractitioner: { text: "Show students what critical thinking achieves, in their subject and beyond it, so they value it rather than seeing it as an exercise.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Questioning and weighing things up is worth your effort: it is how you have a say in what you learn and what happens around you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Distinguish this from the educators' component: here the condition is that students value critical thinking, not only that staff promote it."
  author-agent-dialogue: "Raise it when a student sees critical work as box-ticking. Ask: \"Where has questioning something made a difference for you?\" Avoid lecturing on its importance."
- component: advancehe/inclusive-2024/students.psychological-safety
  forPractitioner: { text: "Listen properly, take feelings seriously and respond to mistakes as part of learning, so that students can speak, ask and disagree without risk.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can ask questions, disagree and make mistakes without being judged for it; that is part of how you learn.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Use the term as the source does: an environment for open dialogue in which lived experience counts as evidence. Do not confuse safety with comfort or with avoiding challenge."
  author-agent-dialogue: "Raise it when a student is reluctant to speak or ask. Ask: \"What would make it easier to say that in the group?\" Avoid promising that nothing will ever feel uncomfortable."
```

### M3 Conditions
<!-- label: editorial; status: drafted; basis: discussion. Ours, every field. -->
```yaml
- component: advancehe/inclusive-2024/institution.kindness
  theme: theme:compassion
  holdsWhen: "Decisions about students are made and explained with regard to the person affected, and discretion is used where a rule would cause needless harm."
  signs: ["policies include a route for exceptions and say who decides", "decisions are explained in plain terms to the student affected", "staff speak of students' circumstances without blame"]
  absentWhen: "Rules are applied the same way regardless of circumstance, and students learn to expect refusal."
  contextSteer: "Write with warmth and without blame: acknowledge that circumstances differ, and show where help or discretion can be sought."
  basis: ours
- component: advancehe/inclusive-2024/institution.contextual-adaptation
  theme: theme:contextual-adaptation
  holdsWhen: "Staff can change how a requirement is met for a group or a person without seeking exceptional approval, provided its purpose is kept."
  signs: ["course teams change formats or timings within a term without escalation", "policies state their purpose as well as their procedure", "reviews ask whether a rule still fits the current students"]
  absentWhen: "Every variation needs special approval, so practice stays fixed and students are asked to fit it."
  contextSteer: "Offer more than one way to reach the same aim, and make clear which parts are fixed and which can change."
  basis: ours
- component: advancehe/inclusive-2024/institution.challenge-structures
  theme: theme:structural-challenge
  holdsWhen: "Questions about whether a policy or practice is fair are raised openly, answered, and sometimes lead to change."
  signs: ["students and staff raise concerns about processes in open forums", "responses give reasons and say what will change", "some policies change because of such questions"]
  absentWhen: "Existing arrangements are treated as given, and questioning them is seen as disloyal or naive."
  contextSteer: "Invite the learner to ask why a convention exists and whom it serves, and treat that question as part of the learning."
  basis: ours
- component: advancehe/inclusive-2024/institution.reconfigure-structures
  theme: theme:structural-challenge
  holdsWhen: "When a structure is shown to exclude, someone with authority owns its redesign and the change is made within a stated time."
  signs: ["reviews of regulations name inclusion as a test", "structural changes cite the evidence that prompted them", "leaders report on changes made, not only on plans"]
  absentWhen: "Structural problems are handed back to individual staff and students to work around."
  contextSteer: "Where a barrier is structural, say so plainly rather than presenting it as the learner's problem to solve."
  basis: ours
- component: advancehe/inclusive-2024/institution.diversity-of-voice
  theme: theme:student-voice-partnership
  holdsWhen: "Decisions record whose views were sought, include views from groups usually unheard, and report back what was done with them."
  signs: ["consultation reaches beyond the usual representatives", "minority or critical views appear in decision records", "people who gave views are told the outcome"]
  absentWhen: "The same few voices shape decisions, and critical or minority views are thanked and ignored."
  contextSteer: "Bring in more than one perspective on the topic, including views from outside the mainstream, and ask the learner whose view is missing."
  basis: ours
- component: advancehe/inclusive-2024/educators.compassionate-relational
  theme: theme:compassion
  holdsWhen: "Staff know their students well enough to notice need, and respond to it with care while keeping expectations clear."
  signs: ["staff use students' names and refer to what they know of them", "responses to difficulty open with a question, not a sanction", "students say they would approach staff with a problem"]
  absentWhen: "Contact is transactional, and students meet procedure before they meet a person."
  contextSteer: "Address the learner directly and warmly, acknowledge that circumstances differ, and keep the standard clear."
  basis: ours
- component: advancehe/inclusive-2024/educators.self-actualisation
  theme: theme:agency-self-actualisation
  holdsWhen: "Staff and students make and defend their own judgements, and are supported rather than overruled when they do so reasonably."
  signs: ["staff adapt practice on their own judgement and explain why", "students are asked for their reasoning, not only their answer", "reasonable judgements are backed even when another choice was possible"]
  absentWhen: "People wait to be told, and judgement is exercised only by those with authority."
  contextSteer: "Ask the learner to make and justify a judgement of their own, and treat a reasoned answer as valuable even where others are possible."
  basis: ours
- component: advancehe/inclusive-2024/educators.critical-thinkers
  theme: theme:critical-thinking
  holdsWhen: "Learning activities regularly require students to question, evaluate and decide, and their conclusions are taken seriously."
  signs: ["tasks ask for a judgement with reasons", "students challenge sources or the tutor without penalty", "student conclusions lead to changes in the session or course"]
  absentWhen: "Students receive and reproduce content, and questioning is reserved for later study."
  contextSteer: "Include at least one point where the learner questions a claim, weighs evidence and states a reasoned view."
  basis: ours
- component: advancehe/inclusive-2024/educators.authentic-learners
  theme: theme:authenticity
  holdsWhen: "Students and staff can draw on their own experience and ways of working in learning, and these are treated as assets."
  signs: ["tasks invite students to draw on their own experience", "more than one way of working is accepted", "staff talk about their own learning"]
  absentWhen: "One way of being a student is rewarded, and others are corrected."
  contextSteer: "Invite the learner to draw on their own experience and ways of working, and value what they bring."
  basis: ours
- component: advancehe/inclusive-2024/educators.anticipating-difference
  theme: theme:anticipating-difference
  holdsWhen: "Teaching is planned for the range of students expected, and the unwritten expectations of study are made explicit."
  signs: ["materials and tasks offer more than one route in", "expectations such as how to use feedback or office hours are spelled out", "staff check assumptions about what excellent work looks like"]
  absentWhen: "Teaching assumes one kind of student, and those who differ discover the rules by failing them."
  contextSteer: "Make unspoken expectations explicit, offer more than one way in, and avoid assuming what the learner already knows."
  basis: ours
- component: advancehe/inclusive-2024/students.mattering
  theme: theme:belonging-mattering
  holdsWhen: "Students' accounts of their experience are taken as legitimate, affect decisions, and students are shown that they did."
  signs: ["students are asked about their experience and told what changed", "individual students are noticed when absent or struggling", "students say staff know who they are"]
  absentWhen: "Students feel anonymous, and their accounts are discounted as anecdote."
  contextSteer: "Address the learner as someone whose experience counts, and invite them to bring it into the task."
  basis: ours
- component: advancehe/inclusive-2024/students.self-actualisation
  theme: theme:agency-self-actualisation
  holdsWhen: "Students choose how to approach their learning, reflect on what works for them, and act on their own judgement with support."
  signs: ["students make choices about how they learn or are assessed", "reflection asks what helped and why", "students explain their own decisions"]
  absentWhen: "Students wait to be told what to do and doubt their own judgement."
  contextSteer: "Give the learner a real choice and ask them to explain it, building confidence in their own judgement."
  basis: ours
- component: advancehe/inclusive-2024/students.critical-thinking
  theme: theme:critical-thinking
  holdsWhen: "Students choose to question and evaluate without being prompted, and can say why it matters to them."
  signs: ["students raise questions unprompted", "students can say what critical thinking changed in their work", "students apply it outside set tasks"]
  absentWhen: "Students treat critical thinking as a requirement to satisfy rather than a habit worth having."
  contextSteer: "Show the learner what questioning achieves in a real case before asking them to do it."
  basis: ours
- component: advancehe/inclusive-2024/students.psychological-safety
  theme: theme:psychological-safety
  holdsWhen: "Students speak, ask, disagree and admit mistakes in learning settings, and doing so carries no penalty."
  signs: ["students ask questions that reveal what they do not know", "disagreement with peers or staff is heard respectfully", "mistakes are discussed openly as part of learning"]
  absentWhen: "Students stay silent to avoid judgement, and mistakes are hidden."
  contextSteer: "Frame mistakes and questions as expected, invite the learner's own experience, and allow for disagreement."
  basis: ours
```

### M4 Open segments
<!-- label: both; status: drafted; basis: primary -->
```yaml
- id: advancehe/inclusive-2024/institution.open
  position: { axis: perspective:institution, page: 7 }
  reason: { span: { start: 9283, end: 9545 }, source: "One segment in each dial is left intentionally blank to represent the many unknown unknowns – complex factors that we may not realise we are missing – and the importance of not assuming we know enough to make judgements about a student’s needs and circumstances.", page: 12 }
  agentInstruction: "Do not fill this segment. When the institution's side is in play, ask what else in this institution bears on inclusion that the five named components miss, and hold the answer as context, not as part of the model."
- id: advancehe/inclusive-2024/educators.open
  position: { axis: perspective:educators, page: 9 }
  reason: { span: { start: 9283, end: 9545 }, source: "One segment in each dial is left intentionally blank to represent the many unknown unknowns – complex factors that we may not realise we are missing – and the importance of not assuming we know enough to make judgements about a student’s needs and circumstances.", page: 12 }
  agentInstruction: "Do not fill this segment. When the educators' side is in play, ask what else in this teaching setting bears on these students that the five named components miss, and hold the answer as context."
- id: advancehe/inclusive-2024/students.open
  position: { axis: perspective:students, page: 11 }
  reason: { span: { start: 9283, end: 9545 }, source: "One segment in each dial is left intentionally blank to represent the many unknown unknowns – complex factors that we may not realise we are missing – and the importance of not assuming we know enough to make judgements about a student’s needs and circumstances.", page: 12 }
  agentInstruction: "Do not fill this segment. When the students' side is in play, ask the person what else matters for these students that the four named components miss, and do not assume you know their needs."
```

### M5 Crosswalks
<!-- label: both; status: drafted; basis: primary -->
```yaml
stated:
  lead: { span: { start: 10626, end: 10709 }, source: "Inclusive learning and teaching can be relevant to all dimensions of the framework:", page: 14 }
  codes:
    - { to: advancehe/psf-dimensions-2023/V1, code: V1, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/V2, code: V2, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/V3, code: V3, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/V4, code: V4, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/V5, code: V5, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/A1, code: A1, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/A2, code: A2, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/A3, code: A3, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/A4, code: A4, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/A5, code: A5, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/K1, code: K1, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/K2, code: K2, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/K3, code: K3, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/K4, code: K4, page: 14, note: "relevant, as stated for every dimension" }
    - { to: advancehe/psf-dimensions-2023/K5, code: K5, page: 14, note: "relevant, as stated for every dimension" }
  fellowship: { span: { start: 10818, end: 11032 }, source: "Advance HE invites all those teaching or supporting learning to evidence their use of this or other Student Success Frameworks in applying for Fellowship in recognition of their commitment to professional practice.", page: 14, note: "an invitation, not an obligation: not an S4 statement" }
inferred:
  - { from: "model", to: "theme:edi", rel: related, basis: inferred, note: "inclusion is the model's whole subject" }
  - { from: "advancehe/inclusive-2024/educators.anticipating-difference", to: "theme:accessibility", rel: related, basis: inferred, note: "designing in advance for difference includes disabled students; the model does not name disability" }
  - { from: "advancehe/inclusive-2024/students.psychological-safety", to: "theme:internationalisation", rel: related, basis: inferred, note: "safe work with people from diverse backgrounds (D1, p. 11) links to the internationalising model's intercultural components" }
```

### M6 Practice themes carried
<!-- label: both; status: drafted; basis: discussion -->
```yaml
- { id: theme:compassion, tier: practice, working: "decisions and teaching shaped by care for the person affected", carriedBy: ["advancehe/inclusive-2024/institution.kindness", "advancehe/inclusive-2024/educators.compassionate-relational"], status: provisional }
- { id: theme:contextual-adaptation, tier: practice, working: "practice adapts to the setting and its students, not the reverse", carriedBy: ["advancehe/inclusive-2024/institution.contextual-adaptation"], status: provisional }
- { id: theme:structural-challenge, tier: practice, working: "structures that exclude can be questioned and are changed", carriedBy: ["advancehe/inclusive-2024/institution.challenge-structures", "advancehe/inclusive-2024/institution.reconfigure-structures"], status: provisional }
- { id: theme:student-voice-partnership, tier: practice, working: "a range of voices, students' included, shapes decisions and is answered", carriedBy: ["advancehe/inclusive-2024/institution.diversity-of-voice"], status: provisional }
- { id: theme:agency-self-actualisation, tier: practice, working: "people grow into, use and trust their own judgement", carriedBy: ["advancehe/inclusive-2024/educators.self-actualisation", "advancehe/inclusive-2024/students.self-actualisation"], status: provisional }
- { id: theme:critical-thinking, tier: practice, working: "questioning and evaluating are practised and valued", carriedBy: ["advancehe/inclusive-2024/educators.critical-thinkers", "advancehe/inclusive-2024/students.critical-thinking"], status: provisional }
- { id: theme:authenticity, tier: practice, working: "learners bring who they are, and that is treated as an asset", carriedBy: ["advancehe/inclusive-2024/educators.authentic-learners"], status: provisional }
- { id: theme:anticipating-difference, tier: practice, working: "teaching is designed in advance for the range of students", carriedBy: ["advancehe/inclusive-2024/educators.anticipating-difference"], status: provisional }
- { id: theme:hidden-curriculum, tier: practice, working: "the unwritten rules of study are made explicit", carriedBy: ["advancehe/inclusive-2024/educators.anticipating-difference"], status: provisional }
- { id: theme:belonging-mattering, tier: practice, working: "students see that their experience and needs count", carriedBy: ["advancehe/inclusive-2024/students.mattering"], status: provisional }
- { id: theme:psychological-safety, tier: practice, working: "speaking, asking, disagreeing and erring carry no penalty", carriedBy: ["advancehe/inclusive-2024/students.psychological-safety"], status: provisional }
```

## Part B Terminology

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: inclusive-learning-and-teaching, definition: "deliberately shaping teaching and its setting so that every student can thrive, treated as the basis of quality", scopeNote: "covers culture, policy and practice as well as the curriculum; not limited to any protected group", category: approach, practices: [learning-and-teaching] }
- { slug: hidden-curriculum, definition: "the unwritten expectations about how to succeed in study that students must pick up without being told", scopeNote: "the source raises it under educators; the practice theme theme:hidden-curriculum", category: concept, practices: [learning-and-teaching] }
- { slug: mattering, definition: "a student's sense, borne out by how decisions are made, that their experience and needs count", scopeNote: "named a student segment; linked to belonging", category: concept, practices: [learning-and-teaching] }
- { slug: psychological-safety, definition: "a setting in which people can speak, ask, disagree and make mistakes without fear of judgement or penalty", scopeNote: "named a student segment; the source links it to dialogue and lived experience as evidence", category: concept, practices: [learning-and-teaching] }
- { slug: self-actualisation, definition: "growing into and trusting one's own judgement; here applied to staff and students alike", scopeNote: "the source does not cite Maslow or define the term further", category: concept, practices: [learning-and-teaching] }
- { slug: unknown-unknowns, definition: "factors that bear on a student which those designing or teaching have not recognised", scopeNote: "represented by the open segment in each dial", category: concept, practices: [learning-and-teaching] }
```

### B2a Terms as the issuer uses them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: inclusive-learning-and-teaching, form: "inclusive learning and teaching", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: hidden-curriculum, form: "hidden curriculum", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: mattering, form: "mattering", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: psychological-safety, form: "psychological safety", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: self-actualisation, form: "self-actualisation", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: unknown-unknowns, form: "unknown unknowns", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the model names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term takes a meaning of its own in one component.

### B4 Relations
```yaml
- { rel: related, from: mattering, to: psychological-safety, note: "both under students; the source links mattering to confidence and safety" }
- { rel: related, from: hidden-curriculum, to: inclusive-learning-and-teaching, note: "noticing it is named as a key opportunity" }
- { rel: related, from: unknown-unknowns, to: inclusive-learning-and-teaching, note: "the open segments" }
```

### B5 Rules
- self-actualisation: gloss it on first use as growing into and trusting one's own judgement, because the source uses it without definition and readers may assume Maslow's sense.
- mattering: keep it distinct from belonging, because the source treats it as shown through decisions, not as a feeling.

## Part C Process

### C0 Formality
`not-applicable`: the model sets conditions and uses, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE
  title: "Inclusive learning and teaching framework"
  edition: "digital edition, 2024"
  year: 2024
  url: "https://www.advance-he.ac.uk (the series page not reached; D3)"
  retrieved: "PDF supplied by Abbott, 4 October 2026"
  licence: "none stated; held by permission (D-std-0019)"
  tier: primary
  readVia: direct
  held: 5c9b382f3d546b495c8c8ed714068b7173a8d019a783163ab431d294ee494845
  heldFiles: ["txt/advance-he-2024-inclusive-learning-teaching-framework-standard.txt", "txt/advance-he-2024-inclusive-learning-teaching-framework-standard.norm.txt", "records/advance-he-2024-inclusive-learning-teaching-framework-standard.held.json", "pdf/advance-he-2024-inclusive-learning-teaching-framework-standard.pdf"]
  citedIn: [0.2, S1, S2, S3, S4, M1, M2, M4, M5, B1]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: "2026-10-04", pass: P1, outcome: "used for every section; figure pages read as images (figure image)" }
- { ref: "ing:doc:inclusive-learning-teaching-framework-advance-he-2024", tier: primary, consulted: "2026-10-04", pass: P1, outcome: "read for consistency of component names; not cited" }
```

### D3 Wanted sources
```yaml
- { citation: "Advance HE, Student Success Frameworks (series web page), current", settles: ["S8", "S7"], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- Front matter, S1: no year or copyright notice is printed in the file; 2024 is taken from the PDF's creation date (25 June 2024; modified 8 July 2024), as ing's run 0137 does. `copyrightNotice: none-stated`.
- Held text: held by Abbott's permission (4 October 2026, 05:03: "Yes full permission"; D-std-0019, as D-std-0013); private, never published.
- M2 order: clockwise from the top of each dial, read from the page images (pp. 7, 9, 11); the text layer gives the labels in a different order. Each label is still found verbatim in the held text, so MD-2 holds.
- M2 explainedBy: links marked `inferred` are std's reading; the source does not tie its prose to its segments.
- S4 force: "it is important that" (frame.institution, frame.educators) and the imperative and entitlement use items are read as `should`, marked on each force line. Neither form is in D-std-0016. For Abbott: rule whether these read as should.
- S4 requires.b3: the issuer's grammar breaks the list ("welcome" after three gerunds); recorded as given, `mood: infinitive`.
- S6: the document never names EDI or accessibility as such (EDI appears only in the excluded back cover); theme:edi is carried, inferred.
- M6: every practice theme is provisional until the shared theme register exists (Abbott, 05:09: "we will call them themes").
- S7 siblingOf: the internationalising and access, retention, attainment and progression models are held (library) but not yet ingested under this variant; their ids are reserved.
- D3: Advance HE's web page for the series (current status, date, the full list of frameworks in the series) not reached; wanted.

---

## Change notes
- 0.1.1, 2026-10-04 09:26: rebuilt on the generic builder; position.perspective becomes position.axis; S7 adds the series overview. Model template 0.3.0-draft, builder 0.2.1: 14 components, 3 open segments, 15 statements, 11 practice themes.
- 0.1.0, 2026-10-04 05:15: first built (Abbott, 05:02 and 05:03; D-std-0018, D-std-0019), the worked example of the model template 0.1.0-draft: 14 components, 3 open segments, 15 statements, 11 practice themes (Abbott, 05:09: conditions are themes).
