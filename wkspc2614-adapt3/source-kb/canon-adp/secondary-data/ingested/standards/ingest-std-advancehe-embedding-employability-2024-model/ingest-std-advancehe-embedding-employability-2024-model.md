---
id: std:doc:advancehe-embedding-employability-2024-model
title: "Framework for embedding employability"
profile: standards/model
profileVersion: none yet   # the variant's profile part is to write
issuer: Advance HE
kind: model
modelKind: condition-model
series: advancehe-student-success-frameworks-2024
axes: { perspectives: 3, facets: 0, groups: 0, segments: 20, openSegments: 0, labelsNotInText: 0 }
jurisdiction: [UK]   # not stated; Advance HE is UK-based and its frameworks are used internationally (inferred)
subjectScope: universal
subjects: []
edition: "digital edition, 2024"
published: 2024   # no date printed; from the PDF metadata (Part E)
revised: "none-stated"   # a later file date, if any (Part E)
status: current   # as at the held text; not checked against Advance HE's site (D3)
supersedes: "none-stated"
heldText: { method: sha256-bytes, raw: 33c85c6a9d63e51e5909a5d76882facd60137cafd219aa3c2cb9300af8003041, normalised: d41c791aee20c4b1453bd17d18dd52c95b88749beae7a7491e1819ebf7a6b51a }
original: { method: sha256-bytes, pdf: d363dbd73f9ea3ed9e02b3bba922785af125eccc56b2bee7e40611230f42dccc, held: "library pdf/advance-he-2024-framework-embedding-employability-standard.pdf" }
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
# Framework for embedding employability

> The issuer's text is held beside this document in the library (`txt/advance-he-2024-framework-embedding-employability-standard.norm.txt`). Each M2 `label` (where the text layer holds it), each `explainedBy` and M4 `source` and each S4 `source` is exactly its span's text, held for language analysis (D-std-0014); private, never published. Every other field is ours, and agents phrase from ours.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
A practice model from Advance HE's Student Success Frameworks: twenty components of embedded employability, seen from the institution, educators and students, each held here as a practice theme that can qualify the context of a lesson or a piece of material. Reach for it to set or check the conditions under which students prepare for work, enterprise and further study. It sets no levels and no outcomes: pair it with a framework or benchmark for what students achieve.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Advance HE (2024) treats employability as giving every student the knowledge, skills and experience to succeed after study, in work, enterprise, further study or elsewhere, and holds that it works only when built into the whole of education and the culture of the institution. It draws three dials: six segments for the institution, eight for educators and related staff (Educators+) and six for students, with no open segment. Framing lines oblige embedding and partnership, and a short list of uses is given for each perspective. It names nine of the fifteen Professional Standards Framework 2023 dimensions and invites its use as Fellowship evidence. It binds no one: it is an enhancement model, not an assurance standard.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: Advance HE
title: "Framework for embedding employability"
series: "Advance HE Student Success Frameworks"
edition: "digital edition, 2024"
dates:
  published: 2024   # not printed; PDF metadata
  other: ["PDF created 3 January 2024", "PDF modified 28 April 2025"]
kind: model
jurisdiction: [UK]
authority: advisory
licence: "none stated in the file (D1)"
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the conditions for embedding employability across an institution, its teaching and its students' development (D1, pp. 2-3)"
appliesTo:
  awards: [none-stated]
  levels: [none]
  providers: ["higher education providers (as stated: \"all higher education providers and systems\")"]
whoMustUse: "no one must; offered to those developing and implementing employability policy and practice, curriculum design, student support and learning and teaching, and to programme teams (D1, p. 3)"
howUsed: ["design", "review", "other: strategy, staff development, Fellowship evidence"]
doesNot: "none-stated"
beneficiary: the student
statedScope: "The framework has been designed to engage and support a diverse range of audiences including those involved in developing and implementing employability policy and practice, curriculum design, student support and learning and teaching."
statedScopeLocator: "D1, p. 3"
statedScopeSpan: { start: 982, end: 1217 }
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "what-is", order: 1, componentType: section, parent: "none", heading: "What is employability?", gloss: "definition: knowledge, skills and experience for life after study; embedding; the 3Es", pages: "2", readFrom: "text layer" }
  - { number: "who-for", order: 2, componentType: section, parent: "none", heading: "Who is the framework for?", gloss: "audiences; the series; partnership; inclusive provision", pages: "3", readFrom: "text layer" }
  - { number: "why", order: 3, componentType: section, parent: "none", heading: "Why is embedding employability important?", gloss: "rationale: outcome data, employers, students, governments", pages: "4", readFrom: "text layer" }
  - { number: "structure", order: 4, componentType: figure, parent: "none", heading: "How is the framework structured?", gloss: "the three perspectives shared by the series", pages: "5", readFrom: "figure image" }
  - { number: "institution", order: 5, componentType: perspective, parent: "none", heading: "Institution", gloss: "framing prose for the institution", pages: "6", readFrom: "text layer" }
  - { number: "institution.dial", order: 6, componentType: figure, parent: "institution", heading: "(dial)", gloss: "six segments, none open", pages: "7", readFrom: "figure image" }
  - { number: "educators", order: 7, componentType: perspective, parent: "none", heading: "Educators+", gloss: "framing prose for educators and course teams", pages: "8", readFrom: "text layer" }
  - { number: "educators.dial", order: 8, componentType: figure, parent: "educators", heading: "(dial)", gloss: "eight segments, none open", pages: "9", readFrom: "figure image" }
  - { number: "students", order: 9, componentType: perspective, parent: "none", heading: "Students", gloss: "framing prose for students", pages: "10", readFrom: "text layer" }
  - { number: "students.dial", order: 10, componentType: figure, parent: "students", heading: "(dial)", gloss: "six segments, none open", pages: "11", readFrom: "figure image" }
  - { number: "use", order: 11, componentType: use-list, parent: "none", heading: "How can you use the framework?", gloss: "purpose; three uses for each perspective", pages: "12-13", readFrom: "figure image" }
  - { number: "psf", order: 12, componentType: section, parent: "none", heading: "How does this framework align with the Professional Standards Framework (PSF) 2023?", gloss: "the PSF table (nine dimensions) and the Fellowship invitation", pages: "14", readFrom: "figure image" }
excluded:
  - { number: "photo", heading: "(full-page photograph)", kind: "other: illustration, no text", pages: "15" }
  - { number: "back-cover", heading: "We help higher education organisations be the best they can be ...", kind: "other: the issuer's promotional back cover", pages: "16 (unnumbered)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only obliging framing lines, requirement lists and use lists are statements (model template rule 3). -->
```yaml
- id: advancehe/employability-2024/frame.what-is
  locator: { number: "frame.what-is", heading: "What is employability?", page: 2 }
  span: { start: 535, end: 668 }
  source: "To be effective, employability should be embedded into all aspects of education, from the curriculum to the wider student experience."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # D-std-0016: "should"
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["embedded"]
  about: "embedding employability everywhere"
  themes: ["none"]
  paraphrase: "Employability should be built into every part of education, from the curriculum to life outside it."
  audience: both
  subjects: inherited
- id: advancehe/employability-2024/frame.who-for
  locator: { number: "frame.who-for", heading: "Who is the framework for?", page: 3 }
  span: { start: 1460, end: 1547 }
  source: "Embedding employability requires partnership between internal and external stakeholders"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "requires" read as must
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["requires"]
  about: "partnership inside and outside"
  themes: ["none"]
  paraphrase: "Embedding employability requires internal and external stakeholders to work in partnership."
  audience: practitioner
  subjects: inherited
- id: advancehe/employability-2024/frame.institution
  locator: { number: "frame.institution", heading: "Institution", page: 6 }
  span: { start: 3126, end: 3252 }
  source: "From an institutional perspective the strategy, policies and practices of the provider should support embedding employability."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # D-std-0016: "should"
  level: none
  perspective: perspective:institution
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["support", "embedding"]
  about: "strategy and policy behind employability"
  themes: ["none"]
  paraphrase: "The institution's strategy, policy and practice should back the embedding of employability."
  audience: practitioner
  subjects: inherited
- id: advancehe/employability-2024/frame.educators.1
  locator: { number: "frame.educators.1", heading: "Educators+", page: 8 }
  span: { start: 4165, end: 4322 }
  source: "Wherever possible, students should have opportunities to gain work experience, participate in extracurricular activities, and engage with career development."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # D-std-0016: "should"; qualified by "Wherever possible"
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["have", "gain", "participate", "engage"]
  about: "work experience and career development for students"
  themes: ["none"]
  paraphrase: "Where it can be done, students should get chances at work experience, activities beyond the curriculum and career development."
  audience: both
  subjects: inherited
- id: advancehe/employability-2024/frame.educators.2
  locator: { number: "frame.educators.2", heading: "Educators+", page: 8 }
  span: { start: 4475, end: 4681 }
  source: "These areas do not sit in isolation, but are critically important, and individual educators and course teams should consider how they connect to both the needs of the student and the institutional strategy."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # D-std-0016: "should"
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["sit", "consider", "connect"]
  about: "connecting the areas to students and strategy"
  themes: ["none"]
  paraphrase: "Staff and course teams should work out how these connected areas relate to student needs and to institutional strategy."
  audience: practitioner
  subjects: inherited
- id: advancehe/employability-2024/frame.students.1
  locator: { number: "frame.students.1", heading: "Students", page: 10 }
  span: { start: 4980, end: 5113 }
  source: "It identifies the attributes and competencies a student should have the opportunity to develop and practice to enhance their success."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # D-std-0016: "should"
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["identifies", "have", "develop", "practice", "enhance"]
  about: "chances to develop attributes"
  themes: ["none"]
  paraphrase: "Students should have the chance to develop and practise the attributes and competencies named on their dial."
  audience: both
  subjects: inherited
- id: advancehe/employability-2024/frame.students.2
  locator: { number: "frame.students.2", heading: "Students", page: 10 }
  span: { start: 5114, end: 5195 }
  source: "To reach all students and to maximise impact, employability needs to be embedded."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "needs to" read as must
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["reach", "maximise", "needs", "embedded"]
  about: "embedding to reach everyone"
  themes: ["none"]
  paraphrase: "Employability must be embedded if it is to reach every student and have the most effect."
  audience: practitioner
  subjects: inherited
- id: advancehe/employability-2024/frame.students.3
  locator: { number: "frame.students.3", heading: "Students", page: 10 }
  span: { start: 5196, end: 5439 }
  source: "Students should be afforded the opportunity to develop the skills and knowledge that are relevant to the range of trajectories they might pursue, therefore understanding how these can be interchangeable in a range of different contexts is key."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # D-std-0016: "should"; "is key" read as part of the same sentence, not a separate force
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: both
  verbs: ["afforded", "develop", "pursue", "understanding"]
  about: "skills for many routes and settings"
  themes: ["none"]
  paraphrase: "Students should be able to develop skills and knowledge for the different routes they may take, and to see how these carry across settings."
  audience: both
  subjects: inherited
- id: advancehe/employability-2024/use.institution.1
  locator: { number: "use.institution.1", heading: "How can you use the framework?", page: 12 }
  span: { start: 6313, end: 6413 }
  source: "Develop strategic priorities and enhance culture through shared ownership of policies and processes."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["Develop", "enhance"]
  about: "shared ownership of policy"
  themes: ["none"]
  paraphrase: "Institutions should use the model to set strategic priorities and build culture by sharing ownership of policy and process."
  audience: practitioner
  subjects: inherited
- id: advancehe/employability-2024/use.institution.2
  locator: { number: "use.institution.2", heading: "How can you use the framework?", page: 12 }
  span: { start: 6428, end: 6510 }
  source: "Encourage a shared vision and values; providing creative and innovative practices."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["Encourage", "providing"]
  about: "shared vision and creative practice"
  themes: ["none"]
  paraphrase: "Institutions should foster a common vision and values for employability and support new and creative practice."
  audience: practitioner
  subjects: inherited
- id: advancehe/employability-2024/use.institution.3
  locator: { number: "use.institution.3", heading: "How can you use the framework?", page: 12 }
  span: { start: 6511, end: 6613 }
  source: "Foster and develop the relationship between institutions, and both external and internal stakeholders."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["Foster", "develop"]
  about: "relationships with stakeholders"
  themes: ["none"]
  paraphrase: "Institutions should build their relationships with stakeholders inside and outside the institution."
  audience: practitioner
  subjects: inherited
- id: advancehe/employability-2024/use.educators.1
  locator: { number: "use.educators.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 6128, end: 6196 }
  source: "Acts as a benchmark to map against and/or consider current practice."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # a function line: states what the model does, without obliging
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["Acts", "map", "consider"]
  about: "a reference to review practice against"
  themes: ["none"]
  paraphrase: "The model serves as a reference against which staff can map and review what they do now."
  audience: practitioner
  subjects: inherited
- id: advancehe/employability-2024/use.educators.2
  locator: { number: "use.educators.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 6619, end: 6754 }
  source: "Develops collaborative engagement across professional services, within disciplinary teams and for multi and interdisciplinary activity."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # a function line: states what the model does, without obliging
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["Develops"]
  about: "collaboration across services and disciplines"
  themes: ["none"]
  paraphrase: "The model helps build collaboration across services, within subject teams and between disciplines."
  audience: practitioner
  subjects: inherited
- id: advancehe/employability-2024/use.educators.3
  locator: { number: "use.educators.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 6210, end: 6311 }
  source: "Provides a resource that can identify and recognise professional development, needs and requirements."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # a function line: states what the model does, without obliging
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: provider
  verbs: ["Provides", "identify", "recognise"]
  about: "staff development needs"
  themes: ["none"]
  paraphrase: "The model helps staff identify and recognise their own development needs and requirements."
  audience: practitioner
  subjects: inherited
- id: advancehe/employability-2024/use.students.1
  locator: { number: "use.students.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 6756, end: 6857 }
  source: "Offers a structure for identifying key elements that can positively impact on a learner’s experience."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # a function line: states what the model does, without obliging
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: both
  verbs: ["Offers", "identifying", "impact"]
  about: "naming what improves the learner's experience"
  themes: ["none"]
  paraphrase: "The model offers a way to pick out what can improve a learner's experience."
  audience: both
  subjects: inherited
- id: advancehe/employability-2024/use.students.2
  locator: { number: "use.students.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 6869, end: 6963 }
  source: "Identifies core components to help develop a shared and common understanding of employability."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # a function line: states what the model does, without obliging
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: both
  verbs: ["Identifies", "help", "develop"]
  about: "a common language for employability"
  themes: ["none"]
  paraphrase: "The model names core components so that people can share a common understanding of employability."
  audience: both
  subjects: inherited
- id: advancehe/employability-2024/use.students.3
  locator: { number: "use.students.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 6964, end: 7115 }
  source: "Allows for contextual understanding and recognises that areas will be under varying degrees of focus through different learning experiences and stages."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # a function line: states what the model does, without obliging
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for embedding employability"
  addressee: both
  verbs: ["Allows", "recognises"]
  about: "different emphasis at different stages"
  themes: ["none"]
  paraphrase: "The model allows for context and accepts that the areas will be emphasised differently at different stages and in different experiences."
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- statement: advancehe/employability-2024/frame.what-is
  forPractitioner: { text: "Build employability into the whole of education, curriculum and wider experience alike, not into one module or service.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "Preparing for your future should be part of every part of your studies, not kept apart.", rewrite: full, force: should, status: drafted }
  author-agent-written: "The model's core expectation, force should. Keep \"embedded\": the point is integration, not addition. Link it to institutional culture."
  author-agent-dialogue: "Raise it when employability is a single module or an optional extra. Ask: \"Where else in the course does this belong?\""
- statement: advancehe/employability-2024/frame.who-for
  forPractitioner: { text: "Treat partnership with colleagues and outside partners as a requirement of embedding employability, not a bonus.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on institutions and their partners", rewrite: full, force: must, status: drafted }
  author-agent-written: "Force must, from \"requires\". Note the source runs on with a comma into a separate clause; the statement ends before it. Link to external stakeholder engagement and professional services."
  author-agent-dialogue: "Raise it when one team tries to embed employability alone. Ask: \"Who else, inside or outside, needs to be part of this?\""
- statement: advancehe/employability-2024/frame.institution
  forPractitioner: { text: "Check that strategy, policy and practice all back employability; remove any that work against it.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "The framing expectation of the institution perspective, force should. Link it to institutional culture and the institution's uses."
  author-agent-dialogue: "Raise it in strategy or policy review. Ask: \"Does this policy help or hinder embedding employability?\""
- statement: advancehe/employability-2024/frame.educators.1
  forPractitioner: { text: "Where you can, give students chances to gain work experience, take part in wider activities and develop their careers.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "Where it can be arranged, you should get chances to gain work experience, take part in activities beyond your course and plan your career.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should, softened by \"Wherever possible\": record both. Link to work integrated learning and career development learning."
  author-agent-dialogue: "Raise it when a student has had no work experience. Ask: \"What chances to gain experience have you had, or could you seek?\""
- statement: advancehe/employability-2024/frame.educators.2
  forPractitioner: { text: "Treat the eight areas as connected, and check how each one meets your students' needs and the institution's strategy.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff and course teams", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should. Stress that the areas are connected, not a checklist. Link the educators' segments to the institution's strategy."
  author-agent-dialogue: "Raise it when one area is treated alone. Ask: \"How does this connect to what students need and to the wider strategy?\""
- statement: advancehe/employability-2024/frame.students.1
  forPractitioner: { text: "Give every student the chance to develop and practise the six attributes on the students' dial.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "You should have the chance to develop and practise the qualities and abilities that help you succeed.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should; the obligation is on providing the opportunity, not on students reaching a level. Link to the six student segments."
  author-agent-dialogue: "Raise it when a student asks what they should be developing. Ask: \"Which of these have you had a chance to practise?\""
- statement: advancehe/employability-2024/frame.students.2
  forPractitioner: { text: "Embed employability in the curriculum so that it reaches every student, not only those who seek it out.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on course design", rewrite: full, force: must, status: drafted }
  author-agent-written: "Force must, from \"needs to\". Note the reason given: reach and impact. Link to inclusive opportunities."
  author-agent-dialogue: "Raise it when employability relies on opt-in activity. Ask: \"Which students never take part, and how would embedding reach them?\""
- statement: advancehe/employability-2024/frame.students.3
  forPractitioner: { text: "Prepare students for more than one route, and help them see how their skills and knowledge carry from one setting to another.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "You should get the chance to build skills for the different paths you might take, and see how they carry across settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should. Note the two parts: range of routes, and transfer between settings. Link to situational knowledge and confidence and adaptability."
  author-agent-dialogue: "Raise it when a student fears their skills only fit one job. Ask: \"Where else could what you have learned be used?\""
- statement: advancehe/employability-2024/use.institution.1
  forPractitioner: { text: "Use the model to set priorities and build culture, sharing ownership of policy and process across the institution.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "One of three institutional uses; force should (imperative, our reading). Link to institutional culture."
  author-agent-dialogue: "Raise it with leaders. Ask: \"Who owns employability policy here, and who should share it?\""
- statement: advancehe/employability-2024/use.institution.2
  forPractitioner: { text: "Foster a common vision and values for employability, and back staff who try creative and new approaches.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). The second clause is a gerund joined by a semicolon; record it as given. Link to institutional culture."
  author-agent-dialogue: "Raise it when practice is uneven across departments. Ask: \"What shared view of employability could people sign up to?\""
- statement: advancehe/employability-2024/use.institution.3
  forPractitioner: { text: "Build and maintain relationships with partners inside and outside the institution.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Link to external stakeholder engagement and partnership working."
  author-agent-dialogue: "Raise it in partnership planning. Ask: \"Which relationships need attention, inside and out?\""
- statement: advancehe/employability-2024/use.educators.1
  forPractitioner: { text: "Map your current employability practice against the eight areas to see what is covered and what is missing.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use of the model by staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A description of a use, force describes. Placed under Educators+ in the image; the text layer puts it before the label. Do not call it a requirement."
  author-agent-dialogue: "Raise it in course review. Ask: \"Which of the eight areas does your course already cover?\""
- statement: advancehe/employability-2024/use.educators.2
  forPractitioner: { text: "Use the model to bring services and subject teams together, and to plan work across disciplines.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use of the model by staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes. Under Educators+ in the image; the text layer places it later. Link to professional services and interdisciplinarity."
  author-agent-dialogue: "Raise it when teams work apart. Ask: \"Who outside your team could you plan this with?\""
- statement: advancehe/employability-2024/use.educators.3
  forPractitioner: { text: "Use the areas to find and record your own development needs in employability teaching.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use of the model by staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes. Link to the PSF crosswalk and the Fellowship invitation."
  author-agent-dialogue: "Raise it in appraisal or development planning. Ask: \"Which area would you most like to develop in?\""
- statement: advancehe/employability-2024/use.students.1
  forPractitioner: { text: "Use the students' dial to pick out what can improve each learner's experience of preparing for the future.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can use the six areas to see what could make your experience of preparing for the future better.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes. Placed under Students in the image; the text layer misplaces it."
  author-agent-dialogue: "Raise it in a tutorial. Ask: \"Which of these would make the most difference to you now?\""
- statement: advancehe/employability-2024/use.students.2
  forPractitioner: { text: "Use the components as a shared language for employability with students and colleagues.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can use these areas as a shared way to talk about getting ready for life after study.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes. Link to institutional culture and shared vision."
  author-agent-dialogue: "Raise it when people mean different things by employability. Ask: \"What do you mean by employability here?\""
- statement: advancehe/employability-2024/use.students.3
  forPractitioner: { text: "Expect the emphasis to shift between areas across stages and settings, and plan accordingly rather than covering everything at once.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Different areas will matter more at different points in your studies; you do not need to work on them all at once.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Force describes. Note that the model does not expect every area at every stage. Link to situational knowledge."
  author-agent-dialogue: "Raise it when a student feels they must develop everything now. Ask: \"Which area matters most at this stage for you?\""
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
- { id: theme:employability, role: carries, carriedIn: ["what-is", "who-for", "why", "institution", "educators", "students", "use", "psf"], basis: "stated: employability is the model's subject throughout" }
- { id: theme:enterprise, role: carries, carriedIn: ["what-is"], basis: "stated: \"enterprise creation\" and the 3Es of Employability, Enterprise and Entrepreneurship (p. 2); carried by no component" }
- { id: theme:wellbeing, role: carries, carriedIn: ["institution.dial"], basis: "stated: the segment \"Student and Staff Wellbeing\" (p. 7)" }
- { id: theme:assessment, role: carries, carriedIn: ["educators.dial"], basis: "stated: the segment \"Authentic Assessment\" (p. 9)" }
- { id: theme:student-partnership, role: carries, carriedIn: ["who-for", "educators.dial"], basis: "stated: \"co-operation and co-creation\" (p. 3) and the segment \"Co-Creation\" (p. 9)" }
- { id: theme:edi, role: carries, carriedIn: ["who-for", "educators.dial"], basis: "inferred: \"an inclusive provision\" (p. 3) and the segment \"Inclusive Opportunities\" (p. 9); EDI is not named outside the excluded back cover (Part E)" }
- { id: theme:esd, role: carries, carriedIn: ["educators.dial"], basis: "inferred: the bare segment \"Sustainability\" (p. 9); ESD is not named (Part E)" }
- { id: theme:access-retention-attainment-progression, role: carries, carriedIn: ["why", "institution.dial"], basis: "inferred: graduate outcome data and the segment \"Employment Outcome Data\" bear on progression (Part E)" }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: partOf, target: "advancehe-student-success-frameworks-2024", note: "Advance HE Student Success Frameworks; the three-perspective structure is shared by the series (D1, p. 5)" }
- { rel: partOf, target: "std:doc:advancehe-enhancing-student-success-2024-model", note: "the series overview names employability as one of its areas" }
- { rel: alignsWith, target: "std:doc:advancehe-psf-dimensions-2023-framework", note: "stated: particularly relevant to nine PSF 2023 dimensions (M5)" }
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
  - { id: perspective:educators, label: "Educators+", page: 9, segments: 8, openSegments: 0, note: "labelled \"Educators+\" in the structure figure (p. 5), on p. 8 and in the use list (p. 13)" }
  - { id: perspective:students, label: "Students", page: 11, segments: 6, openSegments: 0 }
groups: none
use: "to put the student experience at the centre, encourage fitting pedagogy and set the institution's strategic role in employability; the three perspectives can be used apart or together to find where institutional policy and practice meet; each perspective has three uses (S4 use.*) (D1, pp. 12-13)"
```

### M2 Components
<!-- label: both; status: drafted; basis: primary. In the figure's order (Part E). -->
```yaml
- id: advancehe/employability-2024/institution.employment-outcome-data
  label: "Employment Outcome Data"
  span: { start: 3598, end: 3621 }
  position: { axis: perspective:institution, group: none, order: 1, page: 7 }
  explainedBy:
    - { span: { start: 2010, end: 2104 }, source: "Graduate outcome data is often used within league tables as a proxy for student employability.", link: stated, page: 4 }
    - { span: { start: 3253, end: 3365 }, source: "Excellence in employability provision enhances graduate outcomes, institutional reputation and global standings.", link: inferred, page: 6 }
  conditionType: process
  actor: institution
  about: "using graduate outcome data"
  paraphrase: "The institution gathers and reads data on what its graduates go on to do, and uses it to judge and improve its employability provision."
  themes: ["theme:evidence-informed-enhancement", "theme:employability", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/employability-2024/institution.interdisciplinarity
  label: "Interdisciplinarity"
  span: { start: 3623, end: 3642 }
  position: { axis: perspective:institution, group: none, order: 2, page: 7 }
  explainedBy:
    - { span: { start: 6619, end: 6754 }, source: "Develops collaborative engagement across professional services, within disciplinary teams and for multi and interdisciplinary activity.", link: stated, page: 13 }
  conditionType: structure
  actor: institution
  about: "work across disciplines"
  paraphrase: "The institution makes it possible for students and staff to learn and work across subject boundaries, as most workplaces require."
  themes: ["theme:collaboration", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/institution.institutional-culture
  label: "Institutional Culture"
  span: { start: 3846, end: 3867 }
  position: { axis: perspective:institution, group: none, order: 3, page: 7 }
  explainedBy:
    - { span: { start: 2600, end: 2785 }, source: "Embedding employability can meet these needs and enhance student success significantly through embedding employability into the curriculum and into the culture of the whole institution.", link: stated, page: 4 }
    - { span: { start: 3433, end: 3540 }, source: "By helping shape strategic priorities a shared vision is developed, further enhancing culture and practice.", link: stated, page: 6 }
  conditionType: culture
  actor: institution
  about: "employability owned across the institution"
  paraphrase: "Employability is part of how the whole institution thinks and works, with a shared vision, rather than a task left to a careers service."
  themes: ["theme:whole-institution", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/institution.wellbeing
  label: "Student and Staff Wellbeing"
  span: { start: 3814, end: 3841 }
  position: { axis: perspective:institution, group: none, order: 4, page: 7 }
  explainedBy:
    - { span: { start: 3644, end: 3812 }, source: "Strategic direction and institutional support across these areas will provide optimum support to educators and professional service colleagues to best support students.", link: inferred, page: 6 }
  conditionType: service
  actor: institution
  about: "wellbeing of students and staff"
  paraphrase: "The institution looks after the wellbeing of students and staff alike, since both shape how well students prepare for life after study."
  themes: ["theme:compassion", "theme:employability", "theme:wellbeing"]
  sameLabelAs: none
- id: advancehe/employability-2024/institution.professional-services
  label: "Professional Services"
  span: { start: 3575, end: 3596 }
  position: { axis: perspective:institution, group: none, order: 5, page: 7 }
  explainedBy:
    - { span: { start: 3644, end: 3812 }, source: "Strategic direction and institutional support across these areas will provide optimum support to educators and professional service colleagues to best support students.", link: stated, page: 6 }
    - { span: { start: 6619, end: 6754 }, source: "Develops collaborative engagement across professional services, within disciplinary teams and for multi and interdisciplinary activity.", link: stated, page: 13 }
  conditionType: service
  actor: institution
  about: "professional services working with academics"
  paraphrase: "Careers, placement, skills and other professional services work alongside academic staff, and are given the direction and support to do so."
  themes: ["theme:collaboration", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/institution.external-stakeholder-engagement
  label: "External Stakeholder Engagement"
  span: { start: 3542, end: 3573 }
  position: { axis: perspective:institution, group: none, order: 6, page: 7 }
  explainedBy:
    - { span: { start: 1460, end: 1547 }, source: "Embedding employability requires partnership between internal and external stakeholders", link: stated, page: 3 }
    - { span: { start: 6511, end: 6613 }, source: "Foster and develop the relationship between institutions, and both external and internal stakeholders.", link: stated, page: 12 }
    - { span: { start: 3366, end: 3432 }, source: "This influences student recruitment and engagement with employers.", link: inferred, page: 6 }
  conditionType: relationship
  actor: institution
  about: "working with employers and outside partners"
  paraphrase: "The institution builds lasting working relationships with employers, professional bodies and community partners, who help shape and deliver learning."
  themes: ["theme:collaboration", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/educators.work-integrated-learning
  label: "Work Integrated Learning"
  span: { start: 4708, end: 4732 }
  position: { axis: perspective:educators, group: none, order: 1, page: 9 }
  explainedBy:
    - { span: { start: 4165, end: 4322 }, source: "Wherever possible, students should have opportunities to gain work experience, participate in extracurricular activities, and engage with career development.", link: stated, page: 8 }
    - { span: { start: 4323, end: 4474 }, source: "These experiences will help them to develop the skills and knowledge they need to enhance their immediate employment prospects and longer-term success.", link: inferred, page: 8 }
  conditionType: practice
  actor: educator
  about: "learning through and about work"
  paraphrase: "Course teams build experience of work into the curriculum, through placements, live projects and simulated practice, and link it to what students are learning."
  themes: ["theme:real-world-learning", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/educators.co-creation
  label: "Co-Creation"
  span: { start: 4751, end: 4762 }
  position: { axis: perspective:educators, group: none, order: 2, page: 9 }
  explainedBy:
    - { span: { start: 1715, end: 1885 }, source: "The framework is aimed at those who wish to promote an inclusive provision with a focus on collectively enacting vision and strategy through co-operation and co-creation.", link: stated, page: 3 }
  conditionType: relationship
  actor: all
  about: "students and partners shaping learning together"
  paraphrase: "Staff, students and partners design and shape learning together, so that employability work reflects what students need and want."
  themes: ["theme:student-voice-partnership", "theme:employability", "theme:student-partnership"]
  sameLabelAs: none
- id: advancehe/employability-2024/educators.inclusive-opportunities
  label: "Inclusive Opportunities"
  span: { start: 4786, end: 4809 }
  position: { axis: perspective:educators, group: none, order: 3, page: 9 }
  explainedBy:
    - { span: { start: 451, end: 534 }, source: "It is relevant to all students, regardless of their chosen field of study or level.", link: inferred, page: 2 }
    - { span: { start: 830, end: 918 }, source: "we can help ensure that all students have the skills and knowledge they need to succeed.", link: inferred, page: 2 }
  conditionType: practice
  actor: educator
  about: "employability open to every student"
  paraphrase: "Employability opportunities are designed so that every student can take part, whatever their background, commitments or circumstances."
  themes: ["theme:anticipating-difference", "theme:hidden-curriculum", "theme:employability", "theme:edi"]
  sameLabelAs: none
- id: advancehe/employability-2024/educators.sustainability
  label: "Sustainability"
  span: { start: 4840, end: 4854 }
  position: { axis: perspective:educators, group: none, order: 4, page: 9 }
  explainedBy:
    - { span: { start: 2336, end: 2435 }, source: "Governments expect graduates to make a significant positive contribution to the economy and beyond.", link: inferred, page: 4 }
    - { span: { start: 919, end: 977 }, source: "This will benefit them, the economy and their communities.", link: inferred, page: 2 }
  conditionType: practice
  actor: educator
  about: "sustainability in employability learning"
  paraphrase: "Course teams connect employability to sustainability, so that students see how work affects the environment, society and the economy over time."
  themes: ["theme:systems-futures-thinking", "theme:employability", "theme:esd"]
  sameLabelAs: none
- id: advancehe/employability-2024/educators.career-development-learning
  label: "Career Development Learning"
  span: { start: 4811, end: 4838 }
  position: { axis: perspective:educators, group: none, order: 5, page: 9 }
  explainedBy:
    - { span: { start: 4165, end: 4322 }, source: "Wherever possible, students should have opportunities to gain work experience, participate in extracurricular activities, and engage with career development.", link: stated, page: 8 }
    - { span: { start: 2273, end: 2335 }, source: "Students often undertake HE study to enhance career prospects.", link: inferred, page: 4 }
  conditionType: practice
  actor: educator
  about: "learning to manage one's own career"
  paraphrase: "Students learn, within their course, how to explore options, make career decisions and manage transitions, rather than only receiving careers advice."
  themes: ["theme:career-development", "theme:agency-self-actualisation", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/educators.authentic-assessment
  label: "Authentic Assessment"
  span: { start: 4764, end: 4784 }
  position: { axis: perspective:educators, group: none, order: 6, page: 9 }
  explainedBy:
    - { span: { start: 2168, end: 2272 }, source: "employers expect graduates with the necessary competencies to ensure a positive impact upon recruitment.", link: inferred, page: 4 }
    - { span: { start: 3961, end: 4164 }, source: "The framework identifies areas of focus for course or programme teams to ensure they can take a holistic approach to employability, connecting it with pedagogic practice within and across the curriculum.", link: inferred, page: 8 }
  conditionType: practice
  actor: educator
  about: "assessment that mirrors real tasks"
  paraphrase: "Assessment asks students to do the kind of task, for the kind of audience, that they will meet in work or further study."
  themes: ["theme:real-world-learning", "theme:employability", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/employability-2024/educators.active-learning
  label: "Active Learning"
  span: { start: 4734, end: 4749 }
  position: { axis: perspective:educators, group: none, order: 7, page: 9 }
  explainedBy:
    - { span: { start: 3961, end: 4164 }, source: "The framework identifies areas of focus for course or programme teams to ensure they can take a holistic approach to employability, connecting it with pedagogic practice within and across the curriculum.", link: inferred, page: 8 }
    - { span: { start: 5780, end: 5855 }, source: "this framework encourages the adoption of appropriate pedagogical practices", link: inferred, page: 12 }
  conditionType: practice
  actor: educator
  about: "learning by doing"
  paraphrase: "Students learn by doing (solving problems, discussing, making and deciding) rather than only by listening, which builds the skills work calls for."
  themes: ["theme:agency-self-actualisation", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/educators.learning-environment
  label: "Learning Environment"
  span: { start: 4686, end: 4706 }
  position: { axis: perspective:educators, group: none, order: 8, page: 9 }
  explainedBy:
    - { span: { start: 535, end: 668 }, source: "To be effective, employability should be embedded into all aspects of education, from the curriculum to the wider student experience.", link: inferred, page: 2 }
  conditionType: environment
  actor: educator
  about: "settings that support employability"
  paraphrase: "The physical, digital and social settings in which students learn are shaped to support employability, including spaces and tools like those of the workplace."
  themes: ["theme:real-world-learning", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/students.professional-identity-networks
  label: "Professional Identity and Networks"
  span: { start: 5531, end: 5565 }
  position: { axis: perspective:students, group: none, order: 1, page: 11 }
  explainedBy:
    - { span: { start: 4323, end: 4474 }, source: "These experiences will help them to develop the skills and knowledge they need to enhance their immediate employment prospects and longer-term success.", link: inferred, page: 8 }
    - { span: { start: 3366, end: 3432 }, source: "This influences student recruitment and engagement with employers.", link: inferred, page: 6 }
  conditionType: disposition
  actor: student
  about: "seeing oneself as a professional and building contacts"
  paraphrase: "Students develop a sense of themselves as members of a profession or field, and build the contacts that help them enter and grow in it."
  themes: ["theme:career-development", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/students.emotional-intelligence
  label: "Emotional Intelligence"
  span: { start: 5567, end: 5589 }
  position: { axis: perspective:students, group: none, order: 2, page: 11 }
  explainedBy:
    - { span: { start: 4980, end: 5113 }, source: "It identifies the attributes and competencies a student should have the opportunity to develop and practice to enhance their success.", link: inferred, page: 10 }
  conditionType: disposition
  actor: student
  about: "understanding and managing emotions"
  paraphrase: "Students develop the ability to recognise and manage their own emotions and to read and respond to those of others, at work and beyond."
  themes: ["theme:graduate-attributes", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/students.agency-self-awareness
  label: "Agency and Self Awareness"
  span: { start: 5591, end: 5616 }
  position: { axis: perspective:students, group: none, order: 3, page: 11 }
  explainedBy:
    - { span: { start: 5196, end: 5340 }, source: "Students should be afforded the opportunity to develop the skills and knowledge that are relevant to the range of trajectories they might pursue", link: inferred, page: 10 }
  conditionType: disposition
  actor: student
  about: "knowing oneself and acting on it"
  paraphrase: "Students know their strengths, values and interests, and take action to shape their own path."
  themes: ["theme:agency-self-actualisation", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/students.confidence-adaptability
  label: "Confidence and Adaptability"
  span: { start: 5498, end: 5525 }
  position: { axis: perspective:students, group: none, order: 4, page: 11 }
  explainedBy:
    - { span: { start: 5342, end: 5439 }, source: "therefore understanding how these can be interchangeable in a range of different contexts is key.", link: inferred, page: 10 }
    - { span: { start: 370, end: 450 }, source: "whether that be within employment, enterprise creation, further study or beyond.", link: inferred, page: 2 }
  conditionType: disposition
  actor: student
  about: "confidence to adjust to new settings"
  paraphrase: "Students build the confidence to take on unfamiliar situations and to adjust as work, study and circumstances change."
  themes: ["theme:agency-self-actualisation", "theme:transition", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/students.situational-knowledge
  label: "Situational Knowledge"
  span: { start: 5475, end: 5496 }
  position: { axis: perspective:students, group: none, order: 5, page: 11 }
  explainedBy:
    - { span: { start: 5342, end: 5439 }, source: "therefore understanding how these can be interchangeable in a range of different contexts is key.", link: inferred, page: 10 }
    - { span: { start: 6964, end: 7115 }, source: "Allows for contextual understanding and recognises that areas will be under varying degrees of focus through different learning experiences and stages.", link: inferred, page: 13 }
  conditionType: disposition
  actor: student
  about: "knowing how to apply learning in different settings"
  paraphrase: "Students understand how the norms of different settings vary and how to apply what they know in each."
  themes: ["theme:graduate-attributes", "theme:employability"]
  sameLabelAs: none
- id: advancehe/employability-2024/students.behaviours-qualities-values
  label: "Behaviours, Qualities and Values"
  span: { start: 5441, end: 5473 }
  position: { axis: perspective:students, group: none, order: 6, page: 11 }
  explainedBy:
    - { span: { start: 4980, end: 5113 }, source: "It identifies the attributes and competencies a student should have the opportunity to develop and practice to enhance their success.", link: inferred, page: 10 }
  conditionType: disposition
  actor: student
  about: "personal conduct, qualities and values"
  paraphrase: "Students develop the conduct, personal qualities and values that work and civic life call for, and can show them."
  themes: ["theme:graduate-attributes", "theme:employability"]
  sameLabelAs: none
```

### M2a Component audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- component: advancehe/employability-2024/institution.employment-outcome-data
  forPractitioner: { text: "Read graduate destination data by course and by student group, share it with course teams, and use it to decide where provision needs to change; treat it as one signal, not the whole picture.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "What earlier students went on to do is tracked, and you can ask what that record shows about your course and how it is being used to improve things for you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the institution using evidence of what graduates do next to steer its practice. Do not equate employability with outcome figures alone: the source notes that league tables use the data as a proxy. Set it beside the progression stage of the access, retention, attainment and progression model."
  author-agent-dialogue: "Raise it when someone judges a course only by its employment rate, or ignores destination data entirely. Ask: \"What does the outcome data show for different groups on this course?\" and \"What would you change if you trusted it?\" Avoid treating one year's figures as a verdict."
- component: advancehe/employability-2024/institution.interdisciplinarity
  forPractitioner: { text: "Remove the timetable, credit and budget barriers that stop students and staff working across subjects, and create shared projects that need more than one discipline.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will get chances to work with people from other subjects, as you will in most jobs.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an institutional condition: structures that let disciplines meet. Do not reduce it to optional modules from other subjects; the point is joint work on shared problems. Link it to collaborative engagement in the educators' uses."
  author-agent-dialogue: "Raise it when a course is planned as if its graduates will only ever work with people from the same subject. Ask: \"Where in this course does a student work with someone from another discipline?\" Avoid implying that depth in one subject matters less."
- component: advancehe/employability-2024/institution.institutional-culture
  forPractitioner: { text: "Build a shared view of what employability means here, write it into strategy and policy, and make every area see its part in it, not only the careers team.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Preparing for life after study is part of everything around you here, not something kept in one office.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the whole institution owning employability: vision, strategy and everyday practice. Do not present it as a careers service function. Set it beside the institution's use items on shared ownership and shared vision."
  author-agent-dialogue: "Raise it when employability is described as someone else's job. Ask: \"Who here thinks employability is their business, and who does not?\" and \"What would a shared view of it look like?\" Avoid blaming any one department."
- component: advancehe/employability-2024/institution.wellbeing
  forPractitioner: { text: "Treat staff and student wellbeing as conditions of good employability work: plan placements, deadlines and workloads with both in mind, and make support easy to find.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your wellbeing matters while you prepare for work, and support is there when placements, job searching or deadlines get hard.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present wellbeing as a condition of employability for students and staff together, as the segment names both. Do not reduce it to a counselling service. The source gives no further prose on it: say so rather than inventing detail."
  author-agent-dialogue: "Raise it when work experience, applications or deadlines are piling pressure on a student or a colleague. Ask: \"What support do you know of, and what would make it easier to use?\" Avoid diagnosing or giving clinical advice."
- component: advancehe/employability-2024/institution.professional-services
  forPractitioner: { text: "Bring careers, placement and skills staff into course design and delivery as partners, and give them the time and remit to work with academic teams.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Careers, placement and skills staff are part of your course, and you can reach them through it, not only by finding them yourself.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present professional services as partners in embedding employability, not as a separate add-on. Do not imply the source names particular services; it does not. Link it to partnership working and institutional culture."
  author-agent-dialogue: "Raise it when a course team plans employability alone, or a student does not know who could help. Ask: \"Which services could work on this with you?\" Avoid assuming every institution has the same services."
- component: advancehe/employability-2024/institution.external-stakeholder-engagement
  forPractitioner: { text: "Build lasting relationships with employers, professional bodies and community partners; involve them in course design, live projects and placements, and listen to what they need.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "People from outside the university, such as employers and community groups, help shape what and how you learn.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as partnership with people outside the institution, which the source says embedding employability requires. Do not limit stakeholders to large employers: include professional bodies, community and voluntary partners. Set it beside work integrated learning and professional networks."
  author-agent-dialogue: "Raise it when a course is designed without outside input, or a student wants contact with a field. Ask: \"Who outside the university should have a say in this, or could open a door?\" Avoid promising contacts or placements that do not exist."
- component: advancehe/employability-2024/educators.work-integrated-learning
  forPractitioner: { text: "Design work experience into the course (placements, live briefs, simulations, work-based projects) and help students connect it to their subject learning through reflection.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will learn through real or realistic work as part of your course, and be helped to connect it to what you study.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as work experience built into and linked to the curriculum, not an optional extra. Do not assume a placement year: include live briefs, simulations and part-time work reflected on. It crosses over with the qualifier pro:work-based; name that qualifier, not a theme."
  author-agent-dialogue: "Raise it when a student sees no link between study and work, or a course has no contact with practice. Ask: \"Where in this course do students do real or realistic work?\" and \"How do they connect it back to the subject?\" Avoid implying unpaid work is the only route."
- component: advancehe/employability-2024/educators.co-creation
  forPractitioner: { text: "Design employability activity with students and partners rather than for them: invite them into planning, act on what they say, and share decisions.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can help shape how you prepare for life after study, and what you say can change what is offered.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe co-creation as shared design of learning between staff, students and partners. Do not reduce it to consultation or feedback surveys. Link it to student partnership as a sector theme and to the inclusive model's diversity of voice."
  author-agent-dialogue: "Raise it when employability activity is planned without students. Ask: \"Which students helped design this, and what changed because of them?\" Avoid tokenism, such as one representative speaking for all."
- component: advancehe/employability-2024/educators.inclusive-opportunities
  forPractitioner: { text: "Check who takes up placements, events and extracurricular chances and who does not; remove cost, time and contact barriers, and make the unwritten rules of getting work explicit.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Chances to gain experience and contacts should be open to you whatever your background, money or other commitments.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as access to employability opportunities for all, not only to those with money, time or contacts. Name the hidden rules of recruitment and networking that some students already know. Link it to the inclusive learning and teaching model's anticipating difference."
  author-agent-dialogue: "Raise it when take-up of placements or events is uneven. Ask: \"Who is not taking part, and what stands in their way?\" and \"What does a student need to know that no one says?\" Avoid treating low take-up as lack of interest."
- component: advancehe/employability-2024/educators.sustainability
  forPractitioner: { text: "Link employability learning to sustainability: ask what the work students prepare for does to people and the planet, and build the knowledge to act on it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will think about how the work you prepare for affects people, places and the planet, now and in future.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "The segment is a bare label; the source gives no prose on it. Read it as education for sustainable development applied to employability, and say that this reading is ours. Do not invent claims about green jobs. Set it beside the QAA and Advance HE ESD guidance."
  author-agent-dialogue: "Raise it when a student weighs career choices or a module discusses professional practice. Ask: \"What effect does this kind of work have beyond the employer?\" Avoid moralising about anyone's career choice."
- component: advancehe/employability-2024/educators.career-development-learning
  forPractitioner: { text: "Build career learning into modules: exploring options, reflecting on strengths, making decisions and presenting oneself; link it to each stage of the course.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will learn how to explore options, make decisions about your future and present yourself well, as part of your course.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as learning (taught, staged and reflected on), not as a careers appointment. Do not assume a single career path; the source names employment, enterprise creation and further study. Link it to agency and self awareness on the students' dial."
  author-agent-dialogue: "Raise it when a student says they do not know what they want to do. Ask: \"What have you enjoyed or done well so far?\" and \"What could you try to find out more?\" Avoid steering towards one path."
- component: advancehe/employability-2024/educators.authentic-assessment
  forPractitioner: { text: "Set assessments that mirror real tasks: a report for a client, a pitch, a professional judgement, a product; make the audience and standards those of the field.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your assessments will ask you to do the kind of task people in your field really do.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe authentic assessment as tasks modelled on real practice, with real or realistic audiences and standards. Do not confuse it with the inclusive model's authentic learners, a different idea, though the two meet in M5. It crosses over with the qualifier pro:work-based."
  author-agent-dialogue: "Raise it when an assessment is purely an exam or essay with no link to practice. Ask: \"Who in the field would produce something like this, and for whom?\" Avoid implying traditional forms are never valid."
- component: advancehe/employability-2024/educators.active-learning
  forPractitioner: { text: "Plan sessions in which students solve problems, discuss, make and decide, and name the employability skills those activities build.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will learn by doing, solving problems and working with others, and you will see which skills that builds.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present active learning as a teaching approach that builds employability skills through doing. Do not equate it with group work alone. The source gives no prose on this segment: say so."
  author-agent-dialogue: "Raise it when a session is planned as delivery only. Ask: \"What will the students do in this session, and what skill does that practise?\" Avoid dismissing lectures outright."
- component: advancehe/employability-2024/educators.learning-environment
  forPractitioner: { text: "Shape learning spaces, tools and routines so that they resemble practice in the field and support the skills students will need.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Where and how you learn, including the tools you use, helps you get ready for the places you may work.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "The segment is a bare label; read it as the settings, spaces and tools of learning, and say that the reading is ours. Do not narrow it to buildings. Link it to work integrated learning."
  author-agent-dialogue: "Raise it when students meet professional tools or settings only after they graduate. Ask: \"Which tools or settings of the field do students use while they study?\" Avoid assuming expensive facilities are needed."
- component: advancehe/employability-2024/students.professional-identity-networks
  forPractitioner: { text: "Help students see themselves as practitioners of their field: introduce them to its people, norms and communities, and help them build and keep contacts.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will start to see yourself as part of your field and build contacts who can help you along the way.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as identity and connection together: who the student is becoming in their field, and who they know. It crosses over with the qualifier pro:professional-identity; name that qualifier, not a theme. Note the inferred link to authenticity in M5. Do not assume every student has a defined profession."
  author-agent-dialogue: "Raise it when a student cannot picture themselves in their field or knows no one in it. Ask: \"Who do you know who does work like this?\" and \"What would help you feel part of the field?\" Avoid pushing networking as self-promotion only."
- component: advancehe/employability-2024/students.emotional-intelligence
  forPractitioner: { text: "Give students chances to work with others under pressure and to reflect on how emotions shaped what happened; give feedback on teamwork and communication.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will build your ability to understand and manage your feelings and to work well with other people's.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "The segment is a bare label; gloss it as recognising and managing one's own and others' emotions, and say the source does not define it or cite a model. Do not attribute it to Goleman or any author."
  author-agent-dialogue: "Raise it when a student reflects on a difficult team or client situation. Ask: \"How were you feeling, and how did it affect what you did?\" and \"What do you think the others were feeling?\" Avoid any hint of therapy."
- component: advancehe/employability-2024/students.agency-self-awareness
  forPractitioner: { text: "Help students review their strengths, values and interests, and expect them to make and act on choices about their learning and next steps.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will come to know your strengths, values and interests and use them to shape your own path.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present agency and self awareness together: knowing oneself is the basis for acting on one's own behalf. Link it to career development learning and to the inclusive model's self-actualisation. Do not present it as a fixed trait."
  author-agent-dialogue: "Raise it when a student waits to be told what to do next. Ask: \"What do you know you are good at?\" and \"What is one step you could take this week?\" Avoid making the choice for them."
- component: advancehe/employability-2024/students.confidence-adaptability
  forPractitioner: { text: "Give students graded experience of the unfamiliar (new teams, new settings, changing briefs) and help them reflect on how they adjusted.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will build the confidence to handle new and changing situations, and the habit of adjusting when things shift.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present confidence and adaptability as linked: confidence grows from adapting successfully. Link it to transition between study, work and further study. Do not treat confidence as a fixed personality trait."
  author-agent-dialogue: "Raise it when a student is anxious about a new setting or change. Ask: \"When have you adjusted to something new before, and what helped?\" Avoid empty reassurance."
- component: advancehe/employability-2024/students.situational-knowledge
  forPractitioner: { text: "Help students compare how the same knowledge and skills are used in different settings, and practise reading a new setting's expectations.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will learn how to read a new setting and apply what you know in the way it calls for.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "The segment is a bare label; gloss it as knowing how settings differ and how to apply learning in each, and say the gloss is ours. Link it to transferable learning and to the hidden curriculum of workplaces."
  author-agent-dialogue: "Raise it when a student assumes what worked in one setting will work in another. Ask: \"What is different about this setting, and what does it expect?\" Avoid suggesting there is one right way to behave everywhere."
- component: advancehe/employability-2024/students.behaviours-qualities-values
  forPractitioner: { text: "Make expected conduct and values explicit, give students chances to practise and show them, and help them articulate them to others.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will develop and show the conduct, qualities and values that matter in work and in life, and learn to talk about them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as conduct, character and values developed and shown. It crosses over with the qualifier pro:professional-values; name that qualifier, not a theme. Do not prescribe particular values the source does not name."
  author-agent-dialogue: "Raise it when a student is preparing an application or reflecting on conduct. Ask: \"What values guide how you work?\" and \"Where have you shown them?\" Avoid imposing values."
```

### M3 Conditions
<!-- label: editorial; status: drafted; basis: discussion. Ours, every field. -->
```yaml
- component: advancehe/employability-2024/institution.employment-outcome-data
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Graduate destination data is analysed by course and student group, reaches the people who design teaching, and leads to recorded changes."
  signs: ["course reviews cite destination data broken down by student group", "course teams can say what their outcome data shows", "changes to provision name the data that prompted them"]
  absentWhen: "Outcome data is collected for returns and league tables, but no one who teaches sees or acts on it."
  contextSteer: "Where it helps, show the learner where people from this subject have gone next, and treat that as a picture of options, not a limit."
  basis: ours
- component: advancehe/employability-2024/institution.interdisciplinarity
  theme: theme:collaboration
  holdsWhen: "Students and staff take part in learning or projects that bring disciplines together, and institutional rules allow it without special effort."
  signs: ["modules or projects are shared between subject areas", "credit and timetabling rules allow cross-subject work", "students can describe work done with people from other subjects"]
  absentWhen: "Each subject runs alone, and work across disciplines happens only where an individual pushes it through."
  contextSteer: "Where the topic allows, show how another discipline would approach the same problem, and ask the learner what it adds."
  basis: ours
- component: advancehe/employability-2024/institution.institutional-culture
  theme: theme:whole-institution
  holdsWhen: "Staff across academic and service areas describe employability in compatible terms and can say what their own part in it is."
  signs: ["strategy and policy documents state a shared account of employability", "academic and service staff describe their own part in it", "employability appears in routine course and service planning"]
  absentWhen: "Employability is left to the careers service, and academic staff see it as outside their role."
  contextSteer: "Present preparation for work and further study as part of the subject itself, not as an add-on at the end."
  basis: ours
- component: advancehe/employability-2024/institution.wellbeing
  theme: theme:compassion
  holdsWhen: "Workloads, placements and deadlines are planned with the wellbeing of students and staff in mind, and support is easy to reach."
  signs: ["placement and assessment schedules are checked for clashes and peaks", "students and staff know where to find support", "staff workloads for employability activity are recognised"]
  absentWhen: "Employability demands are added on top of everything else, and strain on students and staff goes unnoticed."
  contextSteer: "Acknowledge that preparing for work can be demanding, and point the learner to support as a normal step, not a last resort."
  basis: ours
- component: advancehe/employability-2024/institution.professional-services
  theme: theme:collaboration
  holdsWhen: "Professional services staff take part in course planning and teaching, and students meet them through the course."
  signs: ["careers or placement staff are named in course plans", "service staff contribute to sessions within modules", "students can name the services that support their next steps"]
  absentWhen: "Services wait for students to find them, and academic and service staff rarely plan together."
  contextSteer: "Where it fits, name the services that can help the learner take the next step, and show how to reach them."
  basis: ours
- component: advancehe/employability-2024/institution.external-stakeholder-engagement
  theme: theme:collaboration
  holdsWhen: "External partners contribute to course design and delivery in a regular, recorded way, and the relationships outlast individual staff."
  signs: ["employers or partners sit on course advisory groups", "live briefs, guest input or placements come through partner relationships", "partner feedback is recorded and acted on"]
  absentWhen: "Contact with employers depends on individual staff, and courses are designed without outside input."
  contextSteer: "Where it helps, bring in a real organisation's problem or voice, and show the learner who outside the university uses this knowledge."
  basis: ours
- component: advancehe/employability-2024/educators.work-integrated-learning
  theme: theme:real-world-learning
  holdsWhen: "Every student meets real or realistic work within the curriculum and reflects on how it connects to their learning."
  signs: ["modules include placements, live briefs or simulations", "assessment asks students to reflect on work experience", "students with jobs are helped to draw learning from them"]
  absentWhen: "Work experience is left to students to find on their own, and is not linked to what they study."
  contextSteer: "Set the task in a real or realistic work situation, and ask the learner what it shows about the subject."
  basis: ours
- component: advancehe/employability-2024/educators.co-creation
  theme: theme:student-voice-partnership
  holdsWhen: "Students and partners take part in designing employability activity and can point to changes they made."
  signs: ["students sit on design groups for modules or employability activity", "records show changes made at students' suggestion", "partners and students work on shared projects"]
  absentWhen: "Staff design everything and students are asked for views only afterwards."
  contextSteer: "Give the learner a real say in how the task is shaped, and show how their input changed it."
  basis: ours
- component: advancehe/employability-2024/educators.inclusive-opportunities
  theme: theme:anticipating-difference
  holdsWhen: "Take-up of employability opportunities is monitored by student group, and barriers of cost, time and know-how are reduced."
  signs: ["take-up data is broken down by student group", "opportunities offer paid, flexible or remote options", "recruitment conventions are explained in the course"]
  absentWhen: "Opportunities go to those who already have the money, time and contacts to take them."
  contextSteer: "Assume the learner may lack contacts, money or time, and spell out the unwritten steps to getting work."
  basis: ours
- component: advancehe/employability-2024/educators.sustainability
  theme: theme:systems-futures-thinking
  holdsWhen: "Employability learning includes the social, environmental and economic effects of work, and students practise weighing them."
  signs: ["tasks ask about the wider effects of professional decisions", "sustainability appears in employability outcomes", "students can discuss the sustainability of their chosen field"]
  absentWhen: "Work is presented only as earning and progression, with no thought to its wider effects."
  contextSteer: "Ask the learner to weigh the wider social and environmental effects of the work or decision in hand."
  basis: ours
- component: advancehe/employability-2024/educators.career-development-learning
  theme: theme:career-development
  holdsWhen: "Career learning is taught in the curriculum at each stage, and students reflect on and plan their next steps."
  signs: ["career learning outcomes appear in modules at each level", "students keep and revisit a plan or reflective record", "students can describe more than one possible route"]
  absentWhen: "Career thinking is left to the final year and to students who seek out advice."
  contextSteer: "Invite the learner to connect the topic to options they might pursue, and to plan a next step."
  basis: ours
- component: advancehe/employability-2024/educators.authentic-assessment
  theme: theme:real-world-learning
  holdsWhen: "Assessment tasks resemble real tasks in the field, with realistic audiences, constraints and standards."
  signs: ["briefs name a real or realistic audience or client", "criteria reflect professional standards", "students can say where they would do such a task again"]
  absentWhen: "Assessment tests recall in forms that students will never use again."
  contextSteer: "Frame the task as one a practitioner would do, with a real audience and the standards of the field."
  basis: ours
- component: advancehe/employability-2024/educators.active-learning
  theme: theme:agency-self-actualisation
  holdsWhen: "Students spend much of their learning time doing tasks that ask them to apply, decide or make, and know which skills that practises."
  signs: ["sessions include problem-solving, discussion or making", "students are told which skills an activity builds", "students take decisions within tasks"]
  absentWhen: "Students listen and take notes, and skills for work are left to chance."
  contextSteer: "Give the learner something to do, solve or decide, and name the skill it practises."
  basis: ours
- component: advancehe/employability-2024/educators.learning-environment
  theme: theme:real-world-learning
  holdsWhen: "Students learn in physical and digital settings, and with tools, that resemble those used in their field."
  signs: ["students use the software or equipment of their field", "learning spaces allow team and project work", "routines mirror professional ones, such as briefings or reviews"]
  absentWhen: "The learning setting bears no relation to where students will work, and professional tools are first met after study."
  contextSteer: "Set the learning in a context and with tools like those the learner would meet in practice."
  basis: ours
- component: advancehe/employability-2024/students.professional-identity-networks
  theme: theme:career-development
  holdsWhen: "Students describe themselves in terms of their field and have contacts within it whom they can approach."
  signs: ["students meet practitioners through the course", "students use professional networks or societies", "students talk about their field as one they belong to"]
  absentWhen: "Students see study as separate from any field and graduate without contacts in it."
  contextSteer: "Address the learner as someone joining a field, and point to the people and communities in it."
  basis: ours
- component: advancehe/employability-2024/students.emotional-intelligence
  theme: theme:graduate-attributes
  holdsWhen: "Students reflect on how emotions shaped their work with others and adjust how they act."
  signs: ["reflections mention own and others' emotions", "feedback covers teamwork and communication", "students handle disagreement constructively"]
  absentWhen: "Emotions at work are never discussed, and students meet conflict without having practised it."
  contextSteer: "Invite the learner to notice how they and others feel in the situation and how that shapes what happens."
  basis: ours
- component: advancehe/employability-2024/students.agency-self-awareness
  theme: theme:agency-self-actualisation
  holdsWhen: "Students can describe their strengths and interests and take steps of their own towards goals they have set."
  signs: ["students set and review their own goals", "reflections name strengths and areas to build", "students act on opportunities without being directed"]
  absentWhen: "Students cannot say what they offer and wait for direction."
  contextSteer: "Ask the learner what they bring and what they want, and leave them a real choice about the next step."
  basis: ours
- component: advancehe/employability-2024/students.confidence-adaptability
  theme: theme:agency-self-actualisation
  holdsWhen: "Students meet unfamiliar or changing tasks within their course and can describe how they adjusted."
  signs: ["tasks change partway or involve new settings", "students reflect on how they handled change", "students volunteer for unfamiliar roles"]
  absentWhen: "The course stays predictable, and students meet change for the first time after they leave."
  contextSteer: "Include an element of change or the unfamiliar, and ask the learner how they would adjust."
  basis: ours
- component: advancehe/employability-2024/students.situational-knowledge
  theme: theme:graduate-attributes
  holdsWhen: "Students can explain how expectations differ between settings and adapt how they apply their knowledge."
  signs: ["tasks set the same skill in contrasting settings", "students describe the norms of a workplace or field", "students adjust their writing or conduct to the setting"]
  absentWhen: "Students learn skills in one setting only and struggle to apply them elsewhere."
  contextSteer: "Ask the learner how the knowledge would be used differently in another setting."
  basis: ours
- component: advancehe/employability-2024/students.behaviours-qualities-values
  theme: theme:graduate-attributes
  holdsWhen: "Expected conduct and values are explicit, practised and discussed, and students can give examples of their own."
  signs: ["courses state expected professional conduct", "students reflect on values in practice", "students give examples of qualities in applications"]
  absentWhen: "Conduct and values are assumed and only raised when something goes wrong."
  contextSteer: "Make the expected conduct and values explicit, and ask the learner to give an example of their own."
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
  lead: { span: { start: 7532, end: 7588 }, source: "It is particularly relevant to the following dimensions:", page: 14 }
  codes:
    - { to: advancehe/psf-dimensions-2023/V1, code: V1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V2, code: V2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V4, code: V4, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A1, code: A1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A2, code: A2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A4, code: A4, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K1, code: K1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K2, code: K2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K5, code: K5, page: 14, note: "named in the PSF table" }
  fellowship: { span: { start: 7673, end: 7887 }, source: "Advance HE invites all those teaching or supporting learning to evidence their use of this or other Student Success Frameworks in applying for Fellowship in recognition of their commitment to professional practice.", page: 14, note: "an invitation, not an obligation: not an S4 statement" }
inferred:
  - { from: "model", to: "theme:employability", rel: related, basis: inferred, note: "employability is the model's whole subject" }
  - { from: "advancehe/employability-2024/students.professional-identity-networks", to: "theme:authenticity", rel: related, basis: inferred, note: "becoming oneself in a field meets the inclusive model's authentic learners; crosses pro:professional-identity" }
  - { from: "advancehe/employability-2024/educators.authentic-assessment", to: "theme:authenticity", rel: related, basis: inferred, note: "a different sense of \"authentic\" (real-world tasks); linked so agents keep the two apart" }
  - { from: "advancehe/employability-2024/educators.inclusive-opportunities", to: "advancehe/inclusive-2024/educators.anticipating-difference", rel: related, basis: inferred, note: "designing opportunities for the range of students" }
  - { from: "advancehe/employability-2024/educators.co-creation", to: "advancehe/inclusive-2024/institution.diversity-of-voice", rel: related, basis: inferred, note: "shared design draws on many voices" }
  - { from: "advancehe/employability-2024/students.agency-self-awareness", to: "advancehe/inclusive-2024/students.self-actualisation", rel: related, basis: inferred, note: "knowing and trusting oneself" }
  - { from: "advancehe/employability-2024/educators.sustainability", to: "theme:esd", rel: related, basis: inferred, note: "a bare label read as ESD applied to employability" }
  - { from: "advancehe/employability-2024/institution.employment-outcome-data", to: "theme:access-retention-attainment-progression", rel: related, basis: inferred, note: "graduate outcomes are the progression stage" }
  - { from: "model", to: "theme:enterprise", rel: related, basis: inferred, note: "the 3Es tie employability to enterprise and entrepreneurship (p. 2)" }
```

### M6 Practice themes carried
<!-- label: both; status: drafted; basis: discussion -->
```yaml
- { id: theme:evidence-informed-enhancement, tier: practice, working: "practice is mapped, its effects are evaluated and it is improved on that evidence", carriedBy: ["advancehe/employability-2024/institution.employment-outcome-data"], status: provisional }
- { id: theme:collaboration, tier: practice, working: "learning and problem-solving are done with others, across subjects, professions and sectors", carriedBy: ["advancehe/employability-2024/institution.interdisciplinarity", "advancehe/employability-2024/institution.professional-services", "advancehe/employability-2024/institution.external-stakeholder-engagement"], status: provisional }
- { id: theme:whole-institution, tier: practice, working: "the institution's strategy, quality processes, estate and staff pull together towards one aim", carriedBy: ["advancehe/employability-2024/institution.institutional-culture"], status: provisional }
- { id: theme:compassion, tier: practice, working: "decisions and teaching shaped by care for the person affected", carriedBy: ["advancehe/employability-2024/institution.wellbeing"], status: provisional }
- { id: theme:real-world-learning, tier: practice, working: "learning, assessment and settings are modelled on real practice", carriedBy: ["advancehe/employability-2024/educators.work-integrated-learning", "advancehe/employability-2024/educators.authentic-assessment", "advancehe/employability-2024/educators.learning-environment"], status: provisional }
- { id: theme:student-voice-partnership, tier: practice, working: "a range of voices, students' included, shapes decisions and is answered", carriedBy: ["advancehe/employability-2024/educators.co-creation"], status: provisional }
- { id: theme:anticipating-difference, tier: practice, working: "teaching is designed in advance for the range of students", carriedBy: ["advancehe/employability-2024/educators.inclusive-opportunities"], status: provisional }
- { id: theme:hidden-curriculum, tier: practice, working: "the unwritten rules of study are made explicit", carriedBy: ["advancehe/employability-2024/educators.inclusive-opportunities"], status: provisional }
- { id: theme:systems-futures-thinking, tier: practice, working: "problems are seen as connected systems and judged against possible futures", carriedBy: ["advancehe/employability-2024/educators.sustainability"], status: provisional }
- { id: theme:career-development, tier: practice, working: "students learn to explore, decide and manage their own paths and professional identity", carriedBy: ["advancehe/employability-2024/educators.career-development-learning", "advancehe/employability-2024/students.professional-identity-networks"], status: provisional }
- { id: theme:agency-self-actualisation, tier: practice, working: "people grow into, use and trust their own judgement", carriedBy: ["advancehe/employability-2024/educators.career-development-learning", "advancehe/employability-2024/educators.active-learning", "advancehe/employability-2024/students.agency-self-awareness", "advancehe/employability-2024/students.confidence-adaptability"], status: provisional }
- { id: theme:graduate-attributes, tier: practice, working: "personal qualities, values and interpersonal abilities are developed, shown and carried across settings", carriedBy: ["advancehe/employability-2024/students.emotional-intelligence", "advancehe/employability-2024/students.situational-knowledge", "advancehe/employability-2024/students.behaviours-qualities-values"], status: provisional }
- { id: theme:transition, tier: practice, working: "students are prepared and supported as they move into, through and on from study", carriedBy: ["advancehe/employability-2024/students.confidence-adaptability"], status: provisional }
```

## Part B Terminology

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: employability, definition: "having the knowledge, skills and experience to succeed after study, in work, enterprise, further study or elsewhere", scopeNote: "the source calls it multifaceted and relevant to every student, field and level", category: concept, practices: [learning-and-teaching] }
- { slug: embedding-employability, definition: "building preparation for life after study into the curriculum, the wider experience and the culture of the institution, rather than adding it on", scopeNote: "the model's core claim; reached through all three perspectives", category: approach, practices: [learning-and-teaching] }
- { slug: three-es, definition: "employability, enterprise and entrepreneurship taken together", scopeNote: "named once (p. 2); links the model to the enterprise sector theme", category: concept, practices: [learning-and-teaching] }
- { slug: work-integrated-learning, definition: "learning through real or realistic work built into and linked to the curriculum", scopeNote: "an educators' segment; the source gives no prose on it beyond work experience (p. 8)", category: practice, practices: [learning-and-teaching] }
- { slug: career-development-learning, definition: "taught learning that helps students explore options, decide and manage their own careers", scopeNote: "an educators' segment", category: practice, practices: [learning-and-teaching] }
- { slug: authentic-assessment, definition: "assessment modelled on tasks, audiences and standards met in real practice", scopeNote: "an educators' segment; distinct from the inclusive model's authentic learners", category: practice, practices: [learning-and-teaching] }
- { slug: graduate-outcome-data, definition: "records of what graduates go on to do after study", scopeNote: "the source notes its use in league tables as a proxy for employability", category: concept, practices: [learning-and-teaching] }
```

### B2a Terms as the issuer uses them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: employability, form: "employability", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: embedding-employability, form: "embedding employability", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: three-es, form: "3Es", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: work-integrated-learning, form: "Work Integrated Learning", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: career-development-learning, form: "Career Development Learning", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: authentic-assessment, form: "Authentic Assessment", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: graduate-outcome-data, form: "Graduate outcome data", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the model names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term takes a meaning of its own in one component.

### B4 Relations
```yaml
- { rel: related, from: embedding-employability, to: employability, note: "embedding is how the model says employability is achieved" }
- { rel: related, from: three-es, to: employability, note: "employability is one of the 3Es" }
- { rel: related, from: work-integrated-learning, to: authentic-assessment, note: "both model learning on real practice" }
- { rel: related, from: graduate-outcome-data, to: employability, note: "used as a proxy for it" }
```

### B5 Rules
- employability: keep it broader than getting a job; the source includes enterprise creation, further study and beyond.
- authentic assessment: keep it distinct from the inclusive model's authentic learners, because "authentic" means real-world tasks here and bringing oneself there.

## Part C Process

### C0 Formality
`not-applicable`: the model sets conditions and uses, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE
  title: "Framework for embedding employability"
  edition: "digital edition, 2024"
  year: 2024
  url: "https://www.advance-he.ac.uk (the series page not reached; D3)"
  retrieved: "PDF supplied by Abbott, 4 October 2026"
  licence: "none stated; held by permission (D-std-0019)"
  tier: primary
  readVia: direct
  held: 33c85c6a9d63e51e5909a5d76882facd60137cafd219aa3c2cb9300af8003041
  heldFiles: ["txt/advance-he-2024-framework-embedding-employability-standard.txt", "txt/advance-he-2024-framework-embedding-employability-standard.norm.txt", "records/advance-he-2024-framework-embedding-employability-standard.held.json", "pdf/advance-he-2024-framework-embedding-employability-standard.pdf"]
  citedIn: [0.2, S1, S2, S3, S4, M1, M2, M4, M5, B1]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: "2026-10-04", pass: P1, outcome: "used for every section; figure pages read as images (figure image)" }
```

### D3 Wanted sources
```yaml
- { citation: "Advance HE, Student Success Frameworks (series web page), current", settles: ["S8", "S7", "S1"], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- Front matter, S1: no year or copyright notice is printed in the file; 2024 is taken from the PDF's creation date (3 January 2024; modified 28 April 2025). The later modification date may mean a revised file; not checked against Advance HE's site (D3). `copyrightNotice: none-stated`.
- Held text: held by Abbott's permission (4 October 2026, 05:03: "Yes full permission"; D-std-0019, as D-std-0013); private, never published.
- M2 order: clockwise from the top of each dial, read from the page images (pp. 7, 9, 11), starting with the segment to the right of the top divider; the text layer gives the labels in another order. Every label is held verbatim in the text layer as its own paragraph, so MD-2 holds and no label is read from the image alone.
- M2: no dial has an open segment and the text names none; M4 is [].
- M2 explainedBy: links marked `inferred` are std's reading; the source has almost no prose on its segments, so most links are inferred. Sustainability, Learning Environment, Active Learning, Emotional Intelligence and Situational Knowledge are bare labels: our paraphrases of them are readings, said so in each aaw.
- S4 use list: the text layer puts the perspective labels in the wrong places (Educators+ after "Acts as a benchmark", Institution after "Develop strategic priorities"); the page image (p. 12-13) places Develop, Encourage and Foster under Institution, Acts, Develops and Provides under Educators+, and Offers, Identifies and Allows under Students. Two pairs (Encourage/Foster, Identifies/Allows) share one paragraph in the text layer and are cut at the sentence.
- S4 force: the institution use items are imperatives read as `should` (proposed); the educators' and students' items are function lines (the model "acts", "offers") read as `describes`. For Abbott: rule whether imperatives read as should.
- S4 frame.who-for: the source sentence runs on with a comma splice ("..., the framework may be particularly useful ..."); the statement stops at the obliging clause, and the "may" clause is a possibility, not a permission, so it is not recorded.
- S4: "Staff may wish to consider ..." (p. 14) is an invitation, not an obligation, and is not a statement; nor is the Fellowship invitation.
- M1: the Educators+ axis is `perspective:educators` (shared series id); its label is "Educators+" throughout this framework.
- M5 PSF: the table names V1, V2, V4, A1, A2, A4, K1, K2, K5 (read from the image, p. 14; the text layer agrees).
- M6: proposed practice themes, new in this model: theme:evidence-informed-enhancement, theme:collaboration, theme:whole-institution, theme:real-world-learning, theme:systems-futures-thinking, theme:career-development, theme:graduate-attributes, theme:graduate-attributes. Each is provisional until the shared theme register exists (Abbott, 05:09).
- M6 reuse doubts: Student and Staff Wellbeing carries theme:compassion (nearest practice theme; wellbeing itself is a sector theme); Active Learning carries theme:agency-self-actualisation rather than a new active-learning theme; Learning Environment carries theme:real-world-learning, which is our reading of a bare label.
- Qualifier crossovers (Abbott's professionally oriented qualifiers, named in aaw, not as themes): Work Integrated Learning and Authentic Assessment with pro:work-based; Professional Identity and Networks with pro:professional-identity; Behaviours, Qualities and Values with pro:professional-values. Career Development Learning may also cross a pro: qualifier; no id is assumed.
- S6: theme:employability is stated throughout. theme:enterprise is stated once ("enterprise creation", the 3Es, p. 2) and carried by no component. theme:wellbeing and theme:assessment are stated in segment labels; theme:student-partnership is stated ("co-creation", p. 3); theme:edi is inferred from "inclusive provision" (p. 3) and the Inclusive Opportunities label; theme:esd is inferred from the bare Sustainability label; theme:access-retention-attainment-progression is inferred for Employment Outcome Data.
- S7 siblingOf: the text names "the complete Student Success Framework Series" (p. 3) but no single sibling; no siblingOf or pointsTo is recorded. The inclusive learning and teaching model is linked by inferred M5 relations only.
- D3: Advance HE's web page for the series (current status, date, revision history) not reached; wanted.

---

## Change notes
- 0.1.1, 2026-10-04 09:26: practice themes aligned across the series by std (17 id(s) renamed by tools/theme_merges.json; the old ids are aliases in the shared theme register); rebuilt on builder 0.2.1. Model template 0.3.0-draft, builder 0.2.1: 20 components, 0 open segments, 17 statements, 13 practice themes.
- 0.1.0, 2026-10-04 09:19: first built (Abbott, 09:08: "Use your template model and refine as you go"; D-std-0018). Model template 0.2.0-draft, builder 0.2.0: 20 components, 0 open segments, 17 statements, 14 practice themes.
