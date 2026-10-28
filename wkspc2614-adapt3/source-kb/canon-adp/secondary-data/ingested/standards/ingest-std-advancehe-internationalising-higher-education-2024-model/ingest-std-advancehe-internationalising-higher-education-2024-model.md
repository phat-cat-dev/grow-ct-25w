---
id: std:doc:advancehe-internationalising-higher-education-2024-model
title: "Framework for internationalising higher education"
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
heldText: { method: sha256-bytes, raw: 70b5ae7cf29e51dca9464be3ec05b4317b4a6794ec4deac172d2b5071d620930, normalised: cfc85cd00633bee718f136d5a440f952686d83a7bd421d8861b8751fd930b090 }
original: { method: sha256-bytes, pdf: d17af02ec64e281857e3f6a1af14c707e952fe38a2a7d078fe0a769fde88550b, held: "library pdf/advance-he-2024-framework-internationalising-higher-education-standard.pdf" }
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
# Framework for internationalising higher education

> The issuer's text is held beside this document in the library (`txt/advance-he-2024-framework-internationalising-higher-education-standard.norm.txt`). Each M2 `label` (where the text layer holds it), each `explainedBy` and M4 `source` and each S4 `source` is exactly its span's text, held for language analysis (D-std-0014); private, never published. Every other field is ours, and agents phrase from ours.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
A practice model from Advance HE's Student Success Frameworks: twenty components of internationalisation, seen from the institution, educators and students, each held here as a practice theme that can qualify the context of a lesson or a piece of material. Reach for it to set or check the conditions under which a course becomes international and intercultural. It sets no levels and no outcomes: pair it with a framework or benchmark for what students achieve.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Advance HE (2024) treats internationalisation as a continuing commitment across the whole institution to a learning setting that is globally aware and inclusive, for every student wherever and however they study. It draws three dials, for the institution, educators and students, with six, seven and seven segments and no blank segment. Two framing lines oblige: the responsibility is everyone's, and the work calls for new thinking and collaboration across cultures and borders. Three uses are given for each perspective. It names eight Professional Standards Framework 2023 dimensions as particularly relevant and invites its use as Fellowship evidence. It binds no one: it is an enhancement model, not an assurance standard.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: Advance HE
title: "Framework for internationalising higher education"
series: "Advance HE Student Success Frameworks"
edition: "digital edition, 2024"
dates:
  published: 2024   # not printed; PDF metadata
  other: ["PDF created 9 February 2024", "PDF modified 9 February 2024"]
kind: model
jurisdiction: [UK]
authority: advisory
licence: "none stated in the file (D1)"
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the conditions for internationalising higher education across an institution, its teaching and its students' experience (D1, pp. 2-3)"
appliesTo:
  awards: [none-stated]
  levels: [none]
  providers: ["higher education institutions and providers (as stated: \"HE institutions\", \"HE providers\")"]
whoMustUse: "no one must; offered to all those within higher education and beyond, with organisations (providers, agencies, bodies, employers) and individuals (staff, students, employees) as its principal audiences (D1, p. 3)"
howUsed: ["design", "review", "other: strategy, stakeholder relationships, shared vocabulary, Fellowship evidence"]
doesNot: "none-stated"
beneficiary: the student
statedScope: "This framework is intended for all those within HE and beyond, including those who contribute to and can benefit from an internationalised sector."
statedScopeLocator: "D1, p. 3"
statedScopeSpan: { start: 577, end: 723 }
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "what-is", order: 1, componentType: section, parent: "none", heading: "What is internationalising higher education?", gloss: "definition, shared responsibility and the two framing lines", pages: "2", readFrom: "text layer" }
  - { number: "who-for", order: 2, componentType: section, parent: "none", heading: "Who is the framework for?", gloss: "audiences (organisations and individuals) and the whole-institution approach", pages: "3", readFrom: "text layer" }
  - { number: "why", order: 3, componentType: section, parent: "none", heading: "Why is internationalising higher education important?", gloss: "benefits for institutions, individuals and programmes", pages: "4", readFrom: "text layer" }
  - { number: "structure", order: 4, componentType: figure, parent: "none", heading: "How is the internationalising higher education framework structured?", gloss: "the three perspectives shared by the series", pages: "5", readFrom: "figure image" }
  - { number: "institution", order: 5, componentType: perspective, parent: "none", heading: "Institution", gloss: "framing prose for the institution: standing, partnerships, evidence", pages: "6", readFrom: "text layer" }
  - { number: "institution.dial", order: 6, componentType: figure, parent: "institution", heading: "(dial)", gloss: "six segments, no open segment", pages: "7", readFrom: "figure image" }
  - { number: "educators", order: 7, componentType: perspective, parent: "none", heading: "Educators", gloss: "framing prose for educators: the internationalised curriculum", pages: "8", readFrom: "text layer" }
  - { number: "educators.dial", order: 8, componentType: figure, parent: "educators", heading: "(dial)", gloss: "seven segments, no open segment", pages: "9", readFrom: "figure image" }
  - { number: "students", order: 9, componentType: perspective, parent: "none", heading: "Students", gloss: "framing prose for students: horizons, belonging, employability", pages: "10", readFrom: "text layer" }
  - { number: "students.dial", order: 10, componentType: figure, parent: "students", heading: "(dial)", gloss: "seven segments, no open segment", pages: "11", readFrom: "figure image" }
  - { number: "use", order: 11, componentType: use-list, parent: "none", heading: "How can you use the framework?", gloss: "purpose and three uses for each perspective", pages: "12-13", readFrom: "figure image" }
  - { number: "psf", order: 12, componentType: section, parent: "none", heading: "How does this framework align with the Professional Standards Framework (PSF) 2023?", gloss: "the PSF table (V1-V4, A1, A2, A4, K2) and the Fellowship invitation", pages: "14", readFrom: "figure image" }
excluded:
  - { number: "back-cover", heading: "We help higher education organisations be the best they can be ...", kind: "other: the issuer's promotional back cover", pages: "16" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only obliging framing lines, requirement lists and use lists are statements (model template rule 3). -->
```yaml
- id: advancehe/internationalising-2024/frame.responsibility
  locator: { number: "frame.responsibility", heading: "What is internationalising higher education?", page: 2 }
  span: { start: 1003, end: 1147 }
  source: "The responsibility for internationalising HE resides with everyone, from individual faculty members to professional services and senior leaders."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "responsibility" read as must
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: provider
  verbs: ["resides"]
  about: "shared responsibility for internationalisation"
  themes: ["none"]
  paraphrase: "Everyone in the institution, from academic staff to services and leaders, carries responsibility for internationalisation."
  audience: practitioner
  subjects: inherited
- id: advancehe/internationalising-2024/frame.requires
  locator: { number: "frame.requires", heading: "What is internationalising higher education?", page: 2 }
  span: { start: 1487, end: 1634 }
  source: "It requires new and imaginative ways of thinking and collaboration in a global context within and across academic cultures and national boundaries."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "requires" read as must
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: provider
  verbs: ["requires"]
  about: "new thinking and collaboration across cultures and borders"
  themes: ["none"]
  paraphrase: "Internationalisation demands fresh thinking and collaboration across academic cultures and national borders."
  audience: practitioner
  subjects: inherited
- id: advancehe/internationalising-2024/use.institution.1
  locator: { number: "use.institution.1", heading: "How can you use the framework?", page: 12 }
  span: { start: 5711, end: 5821 }
  source: "Inform and enhance strategic priorities, contributing to the impact of organisations in internationalising HE."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: provider
  verbs: ["Inform", "enhance", "contributing"]
  about: "using the model in strategy"
  themes: ["none"]
  paraphrase: "Institutions should use the model to shape and improve strategic priorities for internationalisation."
  audience: practitioner
  subjects: inherited
- id: advancehe/internationalising-2024/use.institution.2
  locator: { number: "use.institution.2", heading: "How can you use the framework?", page: 12 }
  span: { start: 5836, end: 5929 }
  source: "Foster and develop the relationship between institutions, external and internal stakeholders."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: provider
  verbs: ["Foster", "develop"]
  about: "relationships with stakeholders"
  themes: ["none"]
  paraphrase: "Institutions should build and strengthen relationships with internal and external stakeholders."
  audience: practitioner
  subjects: inherited
- id: advancehe/internationalising-2024/use.institution.3
  locator: { number: "use.institution.3", heading: "How can you use the framework?", page: 12 }
  span: { start: 5930, end: 6059 }
  source: "Stimulate reciprocal exploration and enhance the communal elements of both design and delivery, including policies and processes."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: provider
  verbs: ["Stimulate", "enhance", "including"]
  about: "shared, two-way work on design and delivery"
  themes: ["none"]
  paraphrase: "Institutions should encourage two-way exploration and strengthen what is shared in how courses, policies and processes are designed and run."
  audience: practitioner
  subjects: inherited
- id: advancehe/internationalising-2024/use.educators.1
  locator: { number: "use.educators.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 5471, end: 5539 }
  source: "Acts as a benchmark to map against and/or consider current practice."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # a function line: says what the model does; no obligation
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: provider
  verbs: ["Acts", "map", "consider"]
  about: "the model as a reference point for practice"
  themes: ["none"]
  paraphrase: "The model serves as a reference point against which staff can map or review what they currently do."
  audience: practitioner
  subjects: inherited
- id: advancehe/internationalising-2024/use.educators.2
  locator: { number: "use.educators.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 6065, end: 6131 }
  source: "A shared communication tool to convey ways of working with others."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # a verbless function line: says what the model is; no obligation
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: provider
  verbs: ["convey", "working"]
  about: "the model as a common language"
  themes: ["none"]
  paraphrase: "The model gives staff a common language for describing how they work with others."
  audience: practitioner
  subjects: inherited
- id: advancehe/internationalising-2024/use.educators.3
  locator: { number: "use.educators.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 5552, end: 5709 }
  source: "Assess, evaluate, and improve the extent to which a module, programme or co-curriculum activity promotes internationalisation or contributes to this process."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:educators
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: provider
  verbs: ["Assess", "evaluate", "improve", "promotes", "contributes"]
  about: "reviewing and improving modules and activities"
  themes: ["none"]
  paraphrase: "Staff should judge how far a module, course or co-curricular activity advances internationalisation, and improve it."
  audience: practitioner
  subjects: inherited
- id: advancehe/internationalising-2024/use.students.1
  locator: { number: "use.students.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 6133, end: 6272 }
  source: "Reflect, evaluate, and adapt attitudes, knowledge, values and practices as needed to augment the contribution and influence of individuals."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:students
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: learner
  verbs: ["Reflect", "evaluate", "adapt", "augment"]
  about: "reflecting on and adapting one's own outlook"
  themes: ["none"]
  paraphrase: "Students should reflect on and adjust their attitudes, knowledge, values and practices so that they can contribute and influence more."
  audience: both
  subjects: inherited
- id: advancehe/internationalising-2024/use.students.2
  locator: { number: "use.students.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 6284, end: 6338 }
  source: "Promote intercultural engagement for a global society."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:students
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: learner
  verbs: ["Promote"]
  about: "encouraging contact across cultures"
  themes: ["none"]
  paraphrase: "Students should encourage engagement across cultures, with a global society in view."
  audience: both
  subjects: inherited
- id: advancehe/internationalising-2024/use.students.3
  locator: { number: "use.students.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 6339, end: 6462 }
  source: "Enhance knowledge creation and exchange, embedding social responsibility through openness, reciprocity and ethical enquiry."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:students
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for internationalising higher education"
  addressee: learner
  verbs: ["Enhance", "embedding"]
  about: "responsible creation and sharing of knowledge"
  themes: ["none"]
  paraphrase: "Students should help create and share knowledge, and do so openly, reciprocally and ethically."
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- statement: advancehe/internationalising-2024/frame.responsibility
  forPractitioner: { text: "Take internationalisation as part of your own responsibility, whatever your role; it does not belong to one office.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff and leaders", rewrite: full, force: must, status: drafted }
  author-agent-written: "State this as the framing obligation of the model, force must from \"responsibility\" (D-std-0016). Link it to the working in the internationalisation space component. Do not name one office as the owner."
  author-agent-dialogue: "Raise it when a person says internationalisation is not their job. Ask: \"Which part of it touches your role?\" Avoid adding duties without asking what support exists."
- statement: advancehe/internationalising-2024/frame.requires
  forPractitioner: { text: "Expect to change how you think and work: collaborate across academic cultures and countries rather than adding international content to existing habits.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on how staff and institutions work", rewrite: full, force: must, status: drafted }
  author-agent-written: "State this as the second framing obligation, force must from \"requires\". Its subject is internationalisation itself. Link it to the cross disciplinary and embedded practices components."
  author-agent-dialogue: "Raise it when internationalisation is reduced to adding examples. Ask: \"What would you do differently, not just add?\" Avoid dismissing small first steps."
- statement: advancehe/internationalising-2024/use.institution.1
  forPractitioner: { text: "Use the model when setting and reviewing strategic priorities, so that internationalisation has a clear place in them.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "One of three institutional uses; force should (imperative, our reading). Link it to the purposeful approaches component."
  author-agent-dialogue: "Raise it in strategy work. Ask: \"Where does internationalisation sit in your priorities, and what is it for?\" Avoid assuming a strategy exists."
- statement: advancehe/internationalising-2024/use.institution.2
  forPractitioner: { text: "Use the model to build and strengthen working relationships with partners and stakeholders, inside and outside the institution.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Link it to the interconnectivity component. In the text layer this item and the next run together; they are two items on the page (Part E)."
  author-agent-dialogue: "Raise it when partnerships are discussed. Ask: \"Which stakeholders matter most here, and how is the relationship kept up?\""
- statement: advancehe/internationalising-2024/use.institution.3
  forPractitioner: { text: "Encourage two-way learning with partners and stakeholders, and strengthen the shared parts of how courses, policies and processes are designed and run.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Note \"reciprocal\": learning flows both ways. Link it to cohesive approaches."
  author-agent-dialogue: "Raise it in course or policy design. Ask: \"Who else shapes this, and what do you learn from them?\""
- statement: advancehe/internationalising-2024/use.educators.1
  forPractitioner: { text: "Map your current practice against the model's segments to see what is in place and what is missing.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: describes a use for staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes: it says what the model does and obliges no one. Its subject is the model. Do not present it as an audit requirement."
  author-agent-dialogue: "Raise it when a teacher wants to review a module. Ask: \"Which segments does your module already address, and which not yet?\""
- statement: advancehe/internationalising-2024/use.educators.2
  forPractitioner: { text: "Use the model's terms when describing your practice to colleagues and partners, so you share a vocabulary.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: describes a use for staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line with no main verb, force describes. Present the model as a common vocabulary. Do not overstate it as a communication plan."
  author-agent-dialogue: "Raise it when colleagues talk past each other. Ask: \"Could the model's segments give you a shared way to name what you each do?\""
- statement: advancehe/internationalising-2024/use.educators.3
  forPractitioner: { text: "Review how far your module, course or co-curricular activity advances internationalisation, and act on what you find.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Link it to the evidence informed practice component. Note it covers co-curricular activity as well as modules."
  author-agent-dialogue: "Raise it in module review. Ask: \"How would you tell whether this module advances internationalisation?\""
- statement: advancehe/internationalising-2024/use.students.1
  forPractitioner: { text: "Give students structured chances to reflect on their attitudes, knowledge, values and habits and to adapt them as they meet other cultures.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "Reflect on your attitudes, knowledge, values and habits, and adapt them where that helps you contribute more.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Addressed to students. Link it to effective intercultural relations."
  author-agent-dialogue: "Raise it after an intercultural experience. Ask: \"What did that change in how you see things?\""
- statement: advancehe/internationalising-2024/use.students.2
  forPractitioner: { text: "Invite students to lead and encourage intercultural activity among their peers.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "Encourage contact and shared work across cultures, among your peers and beyond.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). It is the students' counterpart of the educators' intercultural engagement component."
  author-agent-dialogue: "Raise it when a student is in a mixed group. Ask: \"How could you help the group draw on everyone's background?\""
- statement: advancehe/internationalising-2024/use.students.3
  forPractitioner: { text: "Give students roles in creating and sharing knowledge, and set clear expectations of openness, reciprocity and ethics.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "You can help create and share knowledge; do it openly, fairly in both directions and ethically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Link it to the social responsibility and research-informed pedagogy components."
  author-agent-dialogue: "Raise it in project work. Ask: \"Who benefits from what you are making, and how will you share it?\""
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
- { id: theme:internationalisation, role: carries, carriedIn: ["what-is", "who-for", "why", "institution", "educators", "students", "use", "psf"], basis: "stated: internationalisation is the model's subject throughout" }
- { id: theme:edi, role: carries, carriedIn: ["what-is", "educators.dial"], basis: "inferred: \"inclusive learning environment\" (p. 2) and the intersectionality and structural inequality segment; EDI is not named (Part E)" }
- { id: theme:employability, role: carries, carriedIn: ["students"], basis: "stated: \"enhanced employability prospects\" (p. 10)" }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: partOf, target: "advancehe-student-success-frameworks-2024", note: "Advance HE Student Success Frameworks; the three-perspective structure is shared by the series (D1, p. 5)" }
- { rel: modelledAs, target: "ing:doc:internationalising-higher-education-framework-advance-he-2024", note: "the same source run as theory with a dialogue layer (ing run 0138); read for consistency of names, not used as a source" }
- { rel: alignsWith, target: "std:doc:advancehe-psf-dimensions-2023-framework", note: "stated: particularly relevant to V1-V4, A1, A2, A4 and K2 (M5)" }
- { rel: partOf, target: "std:doc:advancehe-enhancing-student-success-2024-model", note: "the series overview names internationalising higher education as one of its areas" }
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
  - { id: perspective:educators, label: "Educators", page: 9, segments: 7, openSegments: 0, note: "labelled \"Educators\" in the structure figure (p. 5), on p. 8 and in the use list (p. 13)" }
  - { id: perspective:students, label: "Students", page: 11, segments: 7, openSegments: 0 }
groups: none
use: "as a guide to keep attention on the student experience, choose fitting pedagogy and treat internationalisation as a strategic matter; the three perspectives can be used apart or together to find where institutional policy and practice meet; each perspective has three uses (S4 use.*) (D1, pp. 12-13)"
```

### M2 Components
<!-- label: both; status: drafted; basis: primary. In the figure's order (Part E). -->
```yaml
- id: advancehe/internationalising-2024/institution.training-support-mechanisms
  label: "Training and Support Mechanisms"
  span: { start: 3641, end: 3672 }
  position: { axis: perspective:institution, group: none, order: 1, page: 7 }
  explainedBy:
    - { span: { start: 1722, end: 1821 }, source: "fostering a supportive environment for internationalisation initiatives throughout the organisation", link: inferred, page: 3 }
  conditionType: service
  actor: institution
  about: "staff development and support for the work"
  paraphrase: "The institution gives the people who carry out internationalisation the training and day-to-day help they need to do it well."
  themes: ["theme:whole-institution", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/institution.resourced
  label: "Resourced"
  span: { start: 3674, end: 3683 }
  position: { axis: perspective:institution, group: none, order: 2, page: 7 }
  explainedBy:
    - { span: { start: 200, end: 349 }, source: "Internationalising higher education (HE) is an ongoing, institution-wide commitment to fostering a globally aware and inclusive learning environment.", link: inferred, page: 2 }
  conditionType: structure
  actor: institution
  about: "time, money and people behind the work"
  paraphrase: "Internationalisation has the time, budget and staffing it needs, so that it does not depend on goodwill alone."
  themes: ["theme:whole-institution", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/institution.cohesive-approaches
  label: "Cohesive Approaches"
  span: { start: 3685, end: 3704 }
  position: { axis: perspective:institution, group: none, order: 3, page: 7 }
  explainedBy:
    - { span: { start: 1823, end: 1908 }, source: "This whole institutional approach will influence culture and drive relevant practices", link: inferred, page: 3 }
    - { span: { start: 1148, end: 1321 }, source: "By working together, we can create a learning environment that reflects the rich mix of cultures, languages and perspectives that exist within the global academic community.", link: inferred, page: 2 }
  conditionType: process
  actor: institution
  about: "joined-up work across the institution"
  paraphrase: "Different parts of the institution pull in the same direction on internationalisation, so that policy, services and teaching fit together."
  themes: ["theme:whole-institution", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/institution.interconnectivity
  label: "Interconnectivity"
  span: { start: 3619, end: 3636 }
  position: { axis: perspective:institution, group: none, order: 4, page: 7 }
  explainedBy:
    - { span: { start: 873, end: 1002 }, source: "By promoting a diverse and inclusive learning experience, HE institutions prepare graduates to thrive in an interconnected world.", link: inferred, page: 2 }
    - { span: { start: 5836, end: 5929 }, source: "Foster and develop the relationship between institutions, external and internal stakeholders.", link: inferred, page: 12 }
  conditionType: relationship
  actor: institution
  about: "links with stakeholders inside and outside"
  paraphrase: "The institution builds and keeps up links with internal and external stakeholders, here and abroad, so that its work is part of a wider network."
  themes: ["theme:interconnectivity", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/institution.cross-disciplinary
  label: "Cross Disciplinary"
  span: { start: 3599, end: 3617 }
  position: { axis: perspective:institution, group: none, order: 5, page: 7 }
  explainedBy:
    - { span: { start: 1487, end: 1634 }, source: "It requires new and imaginative ways of thinking and collaboration in a global context within and across academic cultures and national boundaries.", link: inferred, page: 2 }
    - { span: { start: 457, end: 575 }, source: "Internationalisation benefits all HE students, regardless of their location, background, discipline, or mode of study.", link: inferred, page: 2 }
  conditionType: practice
  actor: institution
  about: "internationalisation across all subjects"
  paraphrase: "Internationalisation reaches every subject and draws on collaboration between disciplines, rather than sitting in a few departments."
  themes: ["theme:interconnectivity", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/institution.purposeful-approaches
  label: "Purposeful Approaches"
  span: { start: 3576, end: 3597 }
  position: { axis: perspective:institution, group: none, order: 6, page: 7 }
  explainedBy:
    - { span: { start: 5711, end: 5821 }, source: "Inform and enhance strategic priorities, contributing to the impact of organisations in internationalising HE.", link: inferred, page: 12 }
    - { span: { start: 5233, end: 5287 }, source: "considering internationalising HE at a strategic level", link: inferred, page: 12 }
  conditionType: process
  actor: institution
  about: "internationalisation with clear aims"
  paraphrase: "Internationalisation is planned with clear aims tied to the institution's strategy, not a set of unrelated activities."
  themes: ["theme:whole-institution", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/educators.positive-narratives
  label: "Positive Narratives"
  span: { start: 4154, end: 4173 }
  position: { axis: perspective:educators, group: none, order: 1, page: 9 }
  explainedBy:
    - { span: { start: 2209, end: 2257 }, source: "Internationalisation offers a range of benefits.", link: inferred, page: 4 }
    - { span: { start: 3809, end: 3997 }, source: "An internationalised curriculum adds vibrancy and relevance into course design and delivery by incorporating a broader range of perspectives, beliefs, values, connections and partnerships.", link: inferred, page: 8 }
  conditionType: culture
  actor: educator
  about: "talking about difference as a gain"
  paraphrase: "Staff speak about internationalisation and about students from many backgrounds as a gain for everyone, not as a problem to manage."
  themes: ["theme:authenticity", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/educators.embedded-practices
  label: "Embedded Practices (Pedagogy and Curricula)"
  span: { start: 4220, end: 4263 }
  position: { axis: perspective:educators, group: none, order: 2, page: 9 }
  explainedBy:
    - { span: { start: 1910, end: 2060 }, source: "whilst embedding the framework within programmes ensures the incorporation of internationalisation principles into the individual learning experience.", link: stated, page: 3 }
    - { span: { start: 1407, end: 1486 }, source: "It is much more than the inclusion of international examples in the curriculum.", link: inferred, page: 2 }
  conditionType: practice
  actor: educator
  about: "internationalisation built into teaching and curriculum"
  paraphrase: "An international and intercultural dimension is built into how courses are designed and taught, not added as stray examples."
  themes: ["theme:embedded-practice", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/educators.intercultural-engagement
  label: "Intercultural Engagement"
  span: { start: 4265, end: 4289 }
  position: { axis: perspective:educators, group: none, order: 3, page: 9 }
  explainedBy:
    - { span: { start: 6284, end: 6338 }, source: "Promote intercultural engagement for a global society.", link: stated, page: 13 }
  conditionType: practice
  actor: educator
  about: "real contact across cultures in learning"
  paraphrase: "Staff design learning in which students from different cultures meet, work together and learn from each other."
  themes: ["theme:intercultural-engagement", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/educators.evidence-informed-practice
  label: "Evidence Informed Practice"
  span: { start: 4318, end: 4344 }
  position: { axis: perspective:educators, group: none, order: 4, page: 9 }
  explainedBy:
    - { span: { start: 5552, end: 5709 }, source: "Assess, evaluate, and improve the extent to which a module, programme or co-curriculum activity promotes internationalisation or contributes to this process.", link: inferred, page: 13 }
    - { span: { start: 5471, end: 5539 }, source: "Acts as a benchmark to map against and/or consider current practice.", link: inferred, page: 13 }
  conditionType: practice
  actor: educator
  about: "choices based on evidence, effects checked"
  paraphrase: "Staff base their internationalisation choices on evidence and check whether those choices work."
  themes: ["theme:evidence-informed-enhancement", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/educators.global-academic-community
  label: "Global Academic Community"
  span: { start: 4291, end: 4316 }
  position: { axis: perspective:educators, group: none, order: 5, page: 9 }
  explainedBy:
    - { span: { start: 1185, end: 1321 }, source: "learning environment that reflects the rich mix of cultures, languages and perspectives that exist within the global academic community.", link: stated, page: 2 }
  conditionType: culture
  actor: educator
  about: "belonging to scholarship worldwide"
  paraphrase: "Staff place their teaching and their students within a worldwide community of scholars, drawing on knowledge from many places and languages."
  themes: ["theme:interconnectivity", "theme:belonging-mattering", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/educators.intersectionality-structural-inequality
  label: "Intersectionality and Structural Inequality"
  span: { start: 4175, end: 4218 }
  position: { axis: perspective:educators, group: none, order: 6, page: 9 }
  explainedBy:
    - { span: { start: 457, end: 575 }, source: "Internationalisation benefits all HE students, regardless of their location, background, discipline, or mode of study.", link: inferred, page: 2 }
    - { span: { start: 287, end: 348 }, source: "fostering a globally aware and inclusive learning environment", link: inferred, page: 2 }
  conditionType: disposition
  actor: educator
  about: "overlapping identities and unequal structures"
  paraphrase: "Staff recognise that students' identities overlap and that structures create unequal chances, and they take both into account in internationalisation."
  themes: ["theme:structural-challenge", "theme:anticipating-difference", "theme:internationalisation", "theme:edi"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/educators.working-internationalisation-space
  label: "Working in the Internationalisation Space"
  span: { start: 4111, end: 4152 }
  position: { axis: perspective:educators, group: none, order: 7, page: 9 }
  explainedBy:
    - { span: { start: 1003, end: 1147 }, source: "The responsibility for internationalising HE resides with everyone, from individual faculty members to professional services and senior leaders.", link: inferred, page: 2 }
    - { span: { start: 350, end: 456 }, source: "This process encompasses all aspects of HE, from teaching and learning to research and knowledge exchange.", link: inferred, page: 2 }
  conditionType: disposition
  actor: educator
  about: "internationalisation as part of one's own role"
  paraphrase: "Staff see internationalisation as part of their own work and take an active part in it, rather than leaving it to specialists."
  themes: ["theme:whole-institution", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/students.research-informed-pedagogy
  label: "Research-Informed Pedagogy"
  span: { start: 4784, end: 4810 }
  position: { axis: perspective:students, group: none, order: 1, page: 11 }
  explainedBy:
    - { span: { start: 350, end: 456 }, source: "This process encompasses all aspects of HE, from teaching and learning to research and knowledge exchange.", link: inferred, page: 2 }
    - { span: { start: 6339, end: 6462 }, source: "Enhance knowledge creation and exchange, embedding social responsibility through openness, reciprocity and ethical enquiry.", link: inferred, page: 13 }
  conditionType: practice
  actor: all
  about: "teaching drawing on research from many places"
  paraphrase: "Students learn through teaching that draws on research, including research from many countries, and they take part in making knowledge."
  themes: ["theme:evidence-informed-enhancement", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/students.social-opportunities
  label: "Social Opportunities"
  span: { start: 4812, end: 4832 }
  position: { axis: perspective:students, group: none, order: 2, page: 11 }
  explainedBy:
    - { span: { start: 4601, end: 4773 }, source: "Engaging in international activities expands horizons, networks, and opportunities, leading to enhanced learning, a sense of belonging and enhanced employability prospects.", link: inferred, page: 10 }
  conditionType: environment
  actor: all
  about: "chances to meet and mix across cultures"
  paraphrase: "Students have chances to meet, mix and make connections across cultures beyond the classroom."
  themes: ["theme:belonging-mattering", "theme:intercultural-engagement", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/students.international-global-partnerships
  label: "International Partnerships/ Global Partnerships"
  span: { start: 4890, end: 4937 }
  position: { axis: perspective:students, group: none, order: 3, page: 11 }
  explainedBy:
    - { span: { start: 3405, end: 3574 }, source: "Furthermore, international collaborations and partnerships contribute to credibility, currency and the provision of evidence supporting teaching and research excellence.", link: stated, page: 6 }
    - { span: { start: 2309, end: 2364 }, source: "enhance research relevance through broader partnerships", link: inferred, page: 4 }
  conditionType: relationship
  actor: all
  about: "links abroad that students can use"
  paraphrase: "Students can take part in partnerships with universities and organisations in other countries, through exchange, joint projects or shared study."
  themes: ["theme:interconnectivity", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/students.social-responsibility
  label: "Social Responsibility"
  span: { start: 4939, end: 4960 }
  position: { axis: perspective:students, group: none, order: 4, page: 11 }
  explainedBy:
    - { span: { start: 6339, end: 6462 }, source: "Enhance knowledge creation and exchange, embedding social responsibility through openness, reciprocity and ethical enquiry.", link: stated, page: 13 }
  conditionType: disposition
  actor: student
  about: "using learning openly, fairly and ethically"
  paraphrase: "Students take responsibility for how their learning and knowledge affect others, acting with openness, fairness and ethical care."
  themes: ["theme:global-citizenship", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/students.effective-intercultural-relations
  label: "Effective Intercultural Relations"
  span: { start: 4855, end: 4888 }
  position: { axis: perspective:students, group: none, order: 5, page: 11 }
  explainedBy:
    - { span: { start: 2516, end: 2602 }, source: "enabling students and staff to work with people from diverse backgrounds and cultures.", link: inferred, page: 4 }
    - { span: { start: 6284, end: 6338 }, source: "Promote intercultural engagement for a global society.", link: inferred, page: 13 }
  conditionType: relationship
  actor: student
  about: "working well across cultures"
  paraphrase: "Students build the skills and attitudes to get on and work well with people from other cultures."
  themes: ["theme:intercultural-engagement", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/students.scaffolded-learning
  label: "Scaffolded Learning"
  span: { start: 4834, end: 4853 }
  position: { axis: perspective:students, group: none, order: 6, page: 11 }
  explainedBy:
    - { span: { start: 4451, end: 4600 }, source: "Internationalisation fosters a diverse and enriching learning environment, encompassing a rich mix of knowledge, experiences, languages and cultures.", link: inferred, page: 10 }
  conditionType: practice
  actor: all
  about: "stepped support into new ways of learning"
  paraphrase: "Students are led step by step into unfamiliar ways of learning, with support that eases as they gain confidence."
  themes: ["theme:transition", "theme:hidden-curriculum", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/internationalising-2024/students.support
  label: "Support"
  span: { start: 4775, end: 4782 }
  position: { axis: perspective:students, group: none, order: 7, page: 11 }
  explainedBy:
    - { span: { start: 1722, end: 1821 }, source: "fostering a supportive environment for internationalisation initiatives throughout the organisation", link: inferred, page: 3 }
    - { span: { start: 457, end: 575 }, source: "Internationalisation benefits all HE students, regardless of their location, background, discipline, or mode of study.", link: inferred, page: 2 }
  conditionType: service
  actor: all
  about: "help that lets every student take part"
  paraphrase: "Students have the academic, language, practical and personal support they need to take full part in an international learning setting."
  themes: ["theme:transition", "theme:internationalisation"]
  sameLabelAs: none
```

### M2a Component audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- component: advancehe/internationalising-2024/institution.training-support-mechanisms
  forPractitioner: { text: "Offer staff development on international and intercultural teaching, and name where staff can turn for help when they take on this work.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the staff who teach and support you to have been helped to work well with students from many countries and cultures.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the institution equipping its staff, not as training for students. The source names the segment but does not define it; do not invent a programme it does not describe. Set it beside the resourced component, since training needs time and money."
  author-agent-dialogue: "Raise it when a member of staff says they were never prepared for an international cohort. Ask: \"What training or help have you been offered for this?\" and \"Who could you ask for it?\" Avoid implying that staff are at fault for gaps the institution left."
- component: advancehe/internationalising-2024/institution.resourced
  forPractitioner: { text: "Put real time, budget and staff behind internationalisation plans, and stop counting on unpaid goodwill to deliver them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the international parts of your course, such as exchanges, partners and support, to be properly funded and staffed.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a structural condition: the work has resources. The source says nothing more about resources; do not state amounts or models. Link it to training and support, and to purposeful approaches, since a plan without resources is a statement of hope."
  author-agent-dialogue: "Raise it when an initiative is described as running on enthusiasm. Ask: \"Whose time pays for this, and is it in their workload?\" Avoid promising resources the person cannot secure."
- component: advancehe/internationalising-2024/institution.cohesive-approaches
  forPractitioner: { text: "Join up the work of academic departments, professional services and leaders on internationalisation, so that each knows what the others do and plans fit together.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the different offices and teams you deal with to give you a consistent picture, not contradictory advice.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as coherence across units, the opposite of scattered projects. Do not equate it with central control. Set it beside cross disciplinary and interconnectivity, which are about links; this one is about consistency."
  author-agent-dialogue: "Raise it when a person describes teams working on the same aim without knowing of each other. Ask: \"Who else here is working on this, and do your plans fit?\" Avoid blaming any one team for a lack of joined-up work."
- component: advancehe/internationalising-2024/institution.interconnectivity
  forPractitioner: { text: "Build and keep up working relationships with partners, employers, agencies and internal stakeholders, and use them in teaching and research.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your studies to connect you with people and organisations beyond your own university, including in other countries.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a network of relationships the institution maintains. The source gives the segment no definition; read it with the uses about stakeholders. Do not reduce it to technology or online links."
  author-agent-dialogue: "Raise it when a course seems sealed off from the world outside. Ask: \"Which outside partners does this course work with, and how do students meet them?\" Avoid listing partnerships the person has not confirmed."
- component: advancehe/internationalising-2024/institution.cross-disciplinary
  forPractitioner: { text: "Treat internationalisation as work for every discipline, and bring subjects together where a shared international question benefits from more than one lens.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Whatever your subject, you can expect it to connect to the wider world, and sometimes to other subjects too.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as internationalisation that crosses subject lines, in two senses: every subject takes part, and subjects work together. The source does not define it; keep the reading modest. Link it to the source's point about crossing academic cultures."
  author-agent-dialogue: "Raise it when a person assumes internationalisation belongs to languages or business only. Ask: \"What would an international angle look like in your subject?\" and \"Which other subject could help?\" Avoid suggesting one model fits all disciplines."
- component: advancehe/internationalising-2024/institution.purposeful-approaches
  forPractitioner: { text: "Set out what internationalisation is for in your institution, link it to strategy, and judge each activity by whether it serves those aims.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the international parts of your course to have a clear purpose that someone can explain to you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as intent: aims set in advance and tied to strategy. The source does not define it; read it with the strategic uses on p. 12. Do not treat recruitment targets as the only purpose."
  author-agent-dialogue: "Raise it when activities are listed without a reason. Ask: \"What is this activity for, and how would you know it worked?\" Avoid assuming the institution has a written strategy."
- component: advancehe/internationalising-2024/educators.positive-narratives
  forPractitioner: { text: "Talk about international students, other cultures and other languages as assets to the learning of the whole group, and challenge deficit talk when you hear it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "The mix of backgrounds in your group is something everyone learns from, and what you bring is valued.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as how staff frame internationalisation and diversity: as gain, not deficit. The source does not define the segment; read it with the benefits it lists. Do not turn it into marketing language or deny real difficulties."
  author-agent-dialogue: "Raise it when a person describes international students mainly as a challenge. Ask: \"What does this group gain from having these students in it?\" Avoid dismissing real pressures the person describes."
- component: advancehe/internationalising-2024/educators.embedded-practices
  forPractitioner: { text: "Build international and intercultural aims into learning outcomes, activities and assessment, so the dimension runs through the course rather than appearing as the odd example.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "The international side of your course is part of what you learn and are assessed on, not an optional extra.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as design that runs through the curriculum and the teaching method; the source warns that it is far more than adding international examples. Link it to the internationalised curriculum named on p. 8."
  author-agent-dialogue: "Raise it during course design or review. Ask: \"Where does the international dimension appear in the outcomes and assessment, not only the examples?\" Avoid suggesting a whole redesign when one change would start the work."
- component: advancehe/internationalising-2024/educators.intercultural-engagement
  forPractitioner: { text: "Design tasks that need students from different cultures to work together and draw on each other's perspectives, and support them through the friction this can bring.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will work with people whose cultures differ from yours, and learn from them as they learn from you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as engagement designed by staff, not left to chance. It pairs with the students' effective intercultural relations component. Do not assume that a mixed group engages on its own."
  author-agent-dialogue: "Raise it when a teacher reports that students stay in same-culture groups. Ask: \"What in the task would make working across cultures worth it to them?\" Avoid forcing grouping without preparation."
- component: advancehe/internationalising-2024/educators.evidence-informed-practice
  forPractitioner: { text: "Use research and your own evaluation data to decide what to change, and check the effect of each change on students.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "The way you are taught has been chosen with good reason, and your experience is part of how it gets checked.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as using evidence to choose and to evaluate practice. The source does not define the segment; read it with the educators' uses on p. 13. Set it beside the students' research-informed pedagogy component."
  author-agent-dialogue: "Raise it when a practice is kept or dropped on habit. Ask: \"What evidence do you have that this helps students?\" and \"How could you find out?\" Avoid treating only published research as evidence."
- component: advancehe/internationalising-2024/educators.global-academic-community
  forPractitioner: { text: "Draw on scholarship from many countries, languages and traditions, and show students that they are joining a community of learning that spans the world.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your subject is studied and argued over all around the world, and you are joining that community.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a sense of membership in scholarship worldwide, and as reading lists and examples that reflect it. Do not imply that English-language or Western scholarship is the default."
  author-agent-dialogue: "Raise it when reading lists come from one country or tradition. Ask: \"Whose scholarship is missing from this list?\" Avoid a token addition that changes nothing."
- component: advancehe/internationalising-2024/educators.intersectionality-structural-inequality
  forPractitioner: { text: "Consider how nationality, language, race, class, gender and other identities combine in your students, and look for the structures that make internationalisation easier for some than others.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Who you are is more than one label, and you can expect the barriers some students face because of how things are set up to be noticed and addressed.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Use the terms as the field uses them: intersectionality for overlapping identities, structural inequality for unequal chances built into systems. The source names the segment without defining it. Do not treat international students as one group."
  author-agent-dialogue: "Raise it when \"international students\" are discussed as one group. Ask: \"Which of these students face more than one barrier at once?\" and \"What in the system creates that?\" Avoid assigning identities to anyone."
- component: advancehe/internationalising-2024/educators.working-internationalisation-space
  forPractitioner: { text: "Treat internationalisation as part of your own role, whatever your job, and look for the part of it you can take forward.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "The staff you meet, in teaching and in services, see helping you learn in a global setting as part of their job.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as staff owning a part of internationalisation in their own role. The source does not define the segment; read it with the line that responsibility lies with everyone. Do not imply it belongs to an international office."
  author-agent-dialogue: "Raise it when a member of staff says internationalisation is someone else's job. Ask: \"What part of it touches your own work?\" Avoid piling on duties without support."
- component: advancehe/internationalising-2024/students.research-informed-pedagogy
  forPractitioner: { text: "Bring current research from many countries into teaching, and give students chances to take part in creating and sharing knowledge.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "What you learn draws on research from around the world, and you can help create new knowledge yourself.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this from the students' side: they meet research in their learning and take part in making knowledge. The source does not define the segment. Set it beside the educators' evidence informed practice component."
  author-agent-dialogue: "Raise it when a student sees research as something only staff do. Ask: \"Where in your course could you add to what is known?\" Avoid overstating what an undergraduate project can contribute."
- component: advancehe/internationalising-2024/students.social-opportunities
  forPractitioner: { text: "Create and promote social and co-curricular activities that bring students from different backgrounds together, and remove barriers such as cost or timing that keep some away.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You have chances to meet and mix with people from other cultures outside class, and that can help you feel you belong.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the social side of internationalisation, linked by the source to networks and belonging. Do not assume students will mix without opportunities designed for it. Note the link to employability through networks."
  author-agent-dialogue: "Raise it when a student feels isolated or mixes only with people like them. Ask: \"What chances have you had to meet people from other backgrounds here?\" Avoid pressing someone into social settings they find hard."
- component: advancehe/internationalising-2024/students.international-global-partnerships
  forPractitioner: { text: "Open the institution's international partnerships to students, through exchanges, joint projects, virtual collaboration or shared modules, and make access fair.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can take part in links with universities and organisations in other countries, in person or online.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Use both of the issuer's names; the segment is printed as one label with two forms. Present partnerships here as something students take part in, not only institutional agreements. Do not assume travel is required."
  author-agent-dialogue: "Raise it when a student thinks international experience means a year abroad only. Ask: \"Which links with other countries could you take part in from here?\" Avoid naming partners the institution has not confirmed."
- component: advancehe/internationalising-2024/students.social-responsibility
  forPractitioner: { text: "Ask students to weigh the effects of knowledge on others, to share it openly and fairly, and to approach enquiry ethically.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "What you learn and create affects other people, and you are expected to use it openly, fairly and with care.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Tie social responsibility to the source's three terms on p. 13: openness, reciprocity and ethical enquiry. Do not reduce it to volunteering or charity."
  author-agent-dialogue: "Raise it when a student's work affects people elsewhere. Ask: \"Who is affected by this, and have they had a say?\" Avoid moralising."
- component: advancehe/internationalising-2024/students.effective-intercultural-relations
  forPractitioner: { text: "Help students develop the skills to communicate and work across cultures, and give them feedback on how they do it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You build the skills to get on and work well with people whose cultures differ from yours.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a capability students develop, which the educators' intercultural engagement component makes possible. Do not present any culture as the norm others adjust to."
  author-agent-dialogue: "Raise it when a student reports friction in a mixed group. Ask: \"What did each of you expect from the group, and where did that differ?\" Avoid stereotyping any culture."
- component: advancehe/internationalising-2024/students.scaffolded-learning
  forPractitioner: { text: "Break unfamiliar academic tasks into steps, model each one, and reduce the support as students gain confidence, remembering that conventions differ between education systems.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "New ways of learning are introduced to you step by step, with support that steps back as you gain confidence.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe scaffolding as support that is planned to fade. The source names the segment without defining it; in this model it applies to all students meeting unfamiliar academic conventions, which differ across countries. Do not imply that any student lacks ability."
  author-agent-dialogue: "Raise it when a student is unsure what a task expects. Ask: \"Which part of this is new to you, compared with how you studied before?\" Avoid assuming what any student's past education was like."
- component: advancehe/internationalising-2024/students.support
  forPractitioner: { text: "Make academic, language, practical and wellbeing support easy to find and fitted to students from different systems and countries, and check who is not using it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can get help with study, language and everyday life when you need it, and it is easy to find.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe support broadly, as the source gives the segment no definition: academic, language, practical and personal help. Do not limit it to international students; all students meet an international setting."
  author-agent-dialogue: "Raise it when a student is struggling alone. Ask: \"Do you know where to get help with this, and has anything stopped you asking?\" Avoid assuming the student's need from their nationality."
```

### M3 Conditions
<!-- label: editorial; status: drafted; basis: discussion. Ours, every field. -->
```yaml
- component: advancehe/internationalising-2024/institution.training-support-mechanisms
  theme: theme:whole-institution
  holdsWhen: "Staff who take on international or intercultural work have had relevant development and know where to get help."
  signs: ["staff development lists sessions on teaching across cultures", "new staff are told who supports internationalisation work", "staff can name a person or team they would ask"]
  absentWhen: "Staff meet international cohorts and partners with no preparation and solve problems alone."
  contextSteer: "Assume the reader may be new to teaching across cultures, and point to where further help can be found."
  basis: ours
- component: advancehe/internationalising-2024/institution.resourced
  theme: theme:whole-institution
  holdsWhen: "Internationalisation activity has named budget, staff time in workload and the facilities it needs."
  signs: ["workload models count internationalisation tasks", "plans name a budget line", "activities continue when one keen person leaves"]
  absentWhen: "International activity depends on a few volunteers and stops when they move on."
  contextSteer: "Suggest activities that a teacher can run within ordinary time and means, and say plainly where more would be needed."
  basis: ours
- component: advancehe/internationalising-2024/institution.cohesive-approaches
  theme: theme:whole-institution
  holdsWhen: "Units that touch internationalisation share aims, know each other's work and make plans that fit together."
  signs: ["a single plan or group links academic and service work", "students get consistent information from different offices", "projects refer to each other rather than repeat each other"]
  absentWhen: "Separate teams run their own international projects, with gaps, overlaps and mixed messages."
  contextSteer: "Link the activity to related work elsewhere in the course or institution, so the learner sees one coherent picture."
  basis: ours
- component: advancehe/internationalising-2024/institution.interconnectivity
  theme: theme:interconnectivity
  holdsWhen: "The institution keeps active relationships with internal and external stakeholders, and these reach into teaching and research."
  signs: ["partners appear in teaching, projects or placements", "stakeholder relationships have a named owner", "links are reviewed and renewed rather than left to lapse"]
  absentWhen: "The institution works in isolation, and outside links exist on paper only."
  contextSteer: "Connect the topic to people, organisations or practice beyond the learner's own institution and country."
  basis: ours
- component: advancehe/internationalising-2024/institution.cross-disciplinary
  theme: theme:interconnectivity
  holdsWhen: "Every discipline has an international dimension in its teaching, and some work brings disciplines together on shared global questions."
  signs: ["programmes in many subjects name an international aim", "joint activities involve staff or students from different disciplines", "examples come from more than one academic tradition"]
  absentWhen: "Internationalisation is seen as the business of a few departments, and other subjects opt out."
  contextSteer: "Draw on more than one discipline or academic tradition when the topic has a global dimension."
  basis: ours
- component: advancehe/internationalising-2024/institution.purposeful-approaches
  theme: theme:whole-institution
  holdsWhen: "Internationalisation activities have stated aims that link to the institution's strategy and are reviewed against them."
  signs: ["a strategy names aims for internationalisation beyond recruitment", "activities state which aim they serve", "reviews ask whether aims were met"]
  absentWhen: "Activities happen because they always have, or because someone is keen, with no shared aim."
  contextSteer: "State the purpose of the international element plainly, so the learner knows why it is there."
  basis: ours
- component: advancehe/internationalising-2024/educators.positive-narratives
  theme: theme:authenticity
  holdsWhen: "Staff and materials present cultural and linguistic diversity as a gain for the whole group, and deficit framing is challenged."
  signs: ["staff describe what international students add to learning", "materials avoid treating any group as a problem", "deficit remarks are questioned when made"]
  absentWhen: "International students are discussed mainly as a language or integration problem."
  contextSteer: "Present the variety of backgrounds in the group as a source of learning, and avoid any framing of difference as deficit."
  basis: ours
- component: advancehe/internationalising-2024/educators.embedded-practices
  theme: theme:embedded-practice
  holdsWhen: "International and intercultural aims appear in outcomes, teaching activities and assessment, not only in examples."
  signs: ["learning outcomes name an international or intercultural aim", "assessment asks students to use more than one cultural context", "teaching methods draw on the group's own range of experience"]
  absentWhen: "Internationalisation means adding a foreign case study while the course design stays the same."
  contextSteer: "Make the international dimension part of what the learner does and is judged on, not a side example."
  basis: ours
- component: advancehe/internationalising-2024/educators.intercultural-engagement
  theme: theme:intercultural-engagement
  holdsWhen: "Learning activities require students from different cultures to work together and use each other's perspectives, with support."
  signs: ["group tasks mix students across cultures by design", "tasks ask for perspectives from more than one culture", "staff prepare students for intercultural group work"]
  absentWhen: "Students sit in same-culture groups and the mix in the room adds nothing to learning."
  contextSteer: "Build in a point where the learner seeks out and uses a perspective from a culture other than their own."
  basis: ours
- component: advancehe/internationalising-2024/educators.evidence-informed-practice
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Changes to internationalisation practice cite evidence, and their effect on students is evaluated."
  signs: ["course reviews include evaluation of international elements", "staff refer to research when choosing approaches", "student feedback on intercultural work is gathered and used"]
  absentWhen: "Practice rests on habit or anecdote, and no one checks whether it works."
  contextSteer: "Ground suggestions in evidence where it exists, and suggest how the learner or teacher could check the effect."
  basis: ours
- component: advancehe/internationalising-2024/educators.global-academic-community
  theme: theme:interconnectivity
  holdsWhen: "Teaching draws on scholarship from many countries and traditions, and students see themselves as members of a worldwide academic community."
  signs: ["reading lists include work from several regions and traditions", "staff refer to debates in other countries", "students take part in international academic events or exchanges"]
  absentWhen: "The subject is presented as if it were made in one country and one language."
  contextSteer: "Include voices and evidence from more than one country or scholarly tradition, and place the learner within that wider community."
  basis: ours
- component: advancehe/internationalising-2024/educators.intersectionality-structural-inequality
  theme: theme:structural-challenge
  holdsWhen: "Staff consider overlapping identities in their students and identify and act on structures that give some students fewer chances."
  signs: ["staff avoid treating international students as one group", "access to international opportunities is checked across student groups", "structural barriers such as cost or visa rules are named and addressed"]
  absentWhen: "Students are sorted into broad labels, and unequal access to international opportunity goes unseen."
  contextSteer: "Avoid treating any group as uniform, and name structural barriers where they shape who can take part."
  basis: ours
- component: advancehe/internationalising-2024/educators.working-internationalisation-space
  theme: theme:whole-institution
  holdsWhen: "Staff in many roles can say what part of internationalisation they contribute to and act on it."
  signs: ["staff in academic and service roles describe their part in internationalisation", "internationalisation appears in role descriptions or plans", "initiatives come from many parts of the institution"]
  absentWhen: "Internationalisation is left to an international office, and other staff see it as outside their work."
  contextSteer: "Show the reader a part of internationalisation they can take forward within their own role."
  basis: ours
- component: advancehe/internationalising-2024/students.research-informed-pedagogy
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Teaching draws on current research from varied places, and students take part in research or enquiry."
  signs: ["teaching refers to recent research from more than one country", "students carry out enquiry or research tasks", "students share findings with others"]
  absentWhen: "Students receive settled content and never see how knowledge is made or where it comes from."
  contextSteer: "Show the learner where the knowledge comes from, including research from other countries, and invite them to enquire for themselves."
  basis: ours
- component: advancehe/internationalising-2024/students.social-opportunities
  theme: theme:belonging-mattering
  holdsWhen: "Students from different backgrounds have regular, accessible chances to meet and build relationships outside formal teaching."
  signs: ["social and co-curricular events draw a mixed group", "events run at times and costs most students can manage", "students name friends from other cultures"]
  absentWhen: "Students socialise only within their own national or cultural groups, and some have no social contact at all."
  contextSteer: "Suggest ways for the learner to connect with peers from other backgrounds, inside and beyond the task."
  basis: ours
- component: advancehe/internationalising-2024/students.international-global-partnerships
  theme: theme:interconnectivity
  holdsWhen: "Students can join activities with partners in other countries, and access does not depend on wealth or ability to travel."
  signs: ["exchanges or virtual collaborations are open to students", "joint projects with overseas partners appear in modules", "support or funding widens access to partner activity"]
  absentWhen: "Partnerships exist between institutions but students never meet or work with the partners."
  contextSteer: "Point the learner to ways of working with partners in other countries, including options that need no travel."
  basis: ours
- component: advancehe/internationalising-2024/students.social-responsibility
  theme: theme:global-citizenship
  holdsWhen: "Students consider the effect of their work on others, share knowledge reciprocally and follow ethical practice in enquiry."
  signs: ["tasks ask students to consider who is affected by their work", "students credit and share knowledge from others fairly", "ethics is discussed as part of enquiry"]
  absentWhen: "Knowledge is treated as private gain, and its effects on others go unconsidered."
  contextSteer: "Ask the learner to consider who is affected by the knowledge in play and how to share it fairly."
  basis: ours
- component: advancehe/internationalising-2024/students.effective-intercultural-relations
  theme: theme:intercultural-engagement
  holdsWhen: "Students communicate and work productively with peers from other cultures and can reflect on how they do it."
  signs: ["mixed groups complete work with shared contribution", "students can describe what they learned from cultural difference", "misunderstandings are discussed and resolved"]
  absentWhen: "Intercultural contact leads to friction or withdrawal, and students avoid it where they can."
  contextSteer: "Prepare the learner to work across cultures, naming that expectations can differ and how to talk about it."
  basis: ours
- component: advancehe/internationalising-2024/students.scaffolded-learning
  theme: theme:transition
  holdsWhen: "Unfamiliar tasks are introduced in steps with modelling and support, and the support is reduced as students gain confidence."
  signs: ["tasks come with worked examples or models", "early tasks are lower in stakes than later ones", "academic conventions are explained, not assumed"]
  absentWhen: "Students are expected to know academic conventions from the start, and those from other systems fall behind."
  contextSteer: "Introduce unfamiliar conventions one step at a time, with an example, and say plainly what is expected."
  basis: ours
- component: advancehe/internationalising-2024/students.support
  theme: theme:transition
  holdsWhen: "Students can find and use academic, language, practical and personal support suited to them, and gaps in use are noticed."
  signs: ["support is signposted at the points students need it", "services adapt to students from different education systems", "use of support is monitored across student groups"]
  absentWhen: "Support exists but is hard to find or assumes one kind of student, and some never use it."
  contextSteer: "Say where help is available and normalise asking for it."
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
  lead: { span: { start: 6888, end: 6944 }, source: "It is particularly relevant to the following dimensions:", page: 14 }
  codes:
    - { to: advancehe/psf-dimensions-2023/V1, code: V1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V2, code: V2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V3, code: V3, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V4, code: V4, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A1, code: A1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A2, code: A2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A4, code: A4, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K2, code: K2, page: 14, note: "named in the PSF table" }
  fellowship: { span: { start: 7025, end: 7239 }, source: "Advance HE invites all those teaching or supporting learning to evidence their use of this or other Student Success Frameworks in applying for Fellowship in recognition of their commitment to professional practice.", page: 14, note: "an invitation, not an obligation: not an S4 statement" }
inferred:
  - { from: "model", to: "theme:internationalisation", rel: related, basis: inferred, note: "internationalisation is the model's whole subject" }
  - { from: "advancehe/internationalising-2024/educators.intersectionality-structural-inequality", to: "theme:edi", rel: related, basis: inferred, note: "overlapping identities and structural inequality are EDI concerns; the model does not name EDI" }
  - { from: "advancehe/internationalising-2024/students.social-opportunities", to: "theme:employability", rel: related, basis: inferred, note: "networks and opportunities lead to employability prospects (D1, p. 10)" }
  - { from: "advancehe/internationalising-2024/students.effective-intercultural-relations", to: "advancehe/inclusive-2024/students.psychological-safety", rel: related, basis: inferred, note: "the inclusive model ties psychological safety to working with people from diverse backgrounds" }
  - { from: "advancehe/internationalising-2024/educators.intersectionality-structural-inequality", to: "advancehe/inclusive-2024/institution.challenge-structures", rel: related, basis: inferred, note: "both ask that excluding structures be named and changed" }
```

### M6 Practice themes carried
<!-- label: both; status: drafted; basis: discussion -->
```yaml
- { id: theme:whole-institution, tier: practice, working: "the institution's strategy, quality processes, estate and staff pull together towards one aim", carriedBy: ["advancehe/internationalising-2024/institution.training-support-mechanisms", "advancehe/internationalising-2024/institution.resourced", "advancehe/internationalising-2024/institution.cohesive-approaches", "advancehe/internationalising-2024/institution.purposeful-approaches", "advancehe/internationalising-2024/educators.working-internationalisation-space"], status: provisional }
- { id: theme:interconnectivity, tier: practice, working: "work in one area, discipline or place is linked to others", carriedBy: ["advancehe/internationalising-2024/institution.interconnectivity", "advancehe/internationalising-2024/institution.cross-disciplinary", "advancehe/internationalising-2024/educators.global-academic-community", "advancehe/internationalising-2024/students.international-global-partnerships"], status: provisional }
- { id: theme:authenticity, tier: practice, working: "learners bring who they are, and that is treated as an asset", carriedBy: ["advancehe/internationalising-2024/educators.positive-narratives"], status: provisional }
- { id: theme:embedded-practice, tier: practice, working: "an aim is built into curriculum, teaching and assessment, not added on", carriedBy: ["advancehe/internationalising-2024/educators.embedded-practices"], status: provisional }
- { id: theme:intercultural-engagement, tier: practice, working: "people from different cultures meet, work together and learn from each other", carriedBy: ["advancehe/internationalising-2024/educators.intercultural-engagement", "advancehe/internationalising-2024/students.social-opportunities", "advancehe/internationalising-2024/students.effective-intercultural-relations"], status: provisional }
- { id: theme:evidence-informed-enhancement, tier: practice, working: "practice is mapped, its effects are evaluated and it is improved on that evidence", carriedBy: ["advancehe/internationalising-2024/educators.evidence-informed-practice", "advancehe/internationalising-2024/students.research-informed-pedagogy"], status: provisional }
- { id: theme:belonging-mattering, tier: practice, working: "students see that their experience and needs count", carriedBy: ["advancehe/internationalising-2024/educators.global-academic-community", "advancehe/internationalising-2024/students.social-opportunities"], status: provisional }
- { id: theme:structural-challenge, tier: practice, working: "structures that exclude can be questioned and are changed", carriedBy: ["advancehe/internationalising-2024/educators.intersectionality-structural-inequality"], status: provisional }
- { id: theme:anticipating-difference, tier: practice, working: "teaching is designed in advance for the range of students", carriedBy: ["advancehe/internationalising-2024/educators.intersectionality-structural-inequality"], status: provisional }
- { id: theme:global-citizenship, tier: practice, working: "learners prepare to act responsibly on shared global challenges", carriedBy: ["advancehe/internationalising-2024/students.social-responsibility"], status: provisional }
- { id: theme:transition, tier: practice, working: "students are prepared and supported as they move into, through and on from study", carriedBy: ["advancehe/internationalising-2024/students.scaffolded-learning", "advancehe/internationalising-2024/students.support"], status: provisional }
- { id: theme:hidden-curriculum, tier: practice, working: "the unwritten rules of study are made explicit", carriedBy: ["advancehe/internationalising-2024/students.scaffolded-learning"], status: provisional }
```

## Part B Terminology

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: internationalising-higher-education, definition: "a continuing commitment across a whole institution to a learning setting that is globally aware and inclusive, reaching teaching, research and knowledge exchange", scopeNote: "the model's subject; the source stresses it is more than adding international examples", category: approach, practices: [learning-and-teaching] }
- { slug: internationalised-curriculum, definition: "a curriculum whose design and delivery draw on a wider range of perspectives, values, connections and partnerships", scopeNote: "named under educators (p. 8); see the embedded practices component", category: concept, practices: [learning-and-teaching] }
- { slug: intercultural-engagement, definition: "learning in which people from different cultures meet, work together and learn from each other", scopeNote: "an educators' segment and a students' use; the practice theme theme:intercultural-engagement", category: concept, practices: [learning-and-teaching] }
- { slug: global-academic-community, definition: "the worldwide community of scholars and learners whose cultures, languages and views a course can draw on", scopeNote: "an educators' segment; also in the definition on p. 2", category: concept, practices: [learning-and-teaching] }
- { slug: whole-institutional-approach, definition: "putting the model into effect across the entire institution so that it shapes culture and practice, not in isolated pockets", scopeNote: "p. 3; read with cohesive approaches and the shared commitment theme", category: approach, practices: [learning-and-teaching] }
- { slug: social-responsibility, definition: "making and using knowledge with regard for its effects on others, openly, reciprocally and ethically", scopeNote: "a students' segment and a students' use", category: concept, practices: [learning-and-teaching] }
- { slug: intersectionality, definition: "the way several identities in one person combine to shape their experience and the barriers they meet", scopeNote: "named only in an educators' segment label; the source does not define it", category: concept, practices: [learning-and-teaching] }
- { slug: scaffolded-learning, definition: "learning introduced in steps with support that is withdrawn as the learner gains confidence", scopeNote: "named only in a students' segment label; the source does not define it", category: concept, practices: [learning-and-teaching] }
```

### B2a Terms as the issuer uses them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: internationalising-higher-education, form: "internationalising higher education", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: internationalised-curriculum, form: "internationalised curriculum", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: intercultural-engagement, form: "intercultural engagement", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: global-academic-community, form: "global academic community", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: whole-institutional-approach, form: "whole institutional approach", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: social-responsibility, form: "social responsibility", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: intersectionality, form: "intersectionality", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: scaffolded-learning, form: "scaffolded learning", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the model names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term takes a meaning of its own in one component.

### B4 Relations
```yaml
- { rel: related, from: internationalised-curriculum, to: internationalising-higher-education, note: "the curriculum is the educators' share of the whole" }
- { rel: related, from: whole-institutional-approach, to: internationalising-higher-education, note: "the source says the model works best institution-wide" }
- { rel: related, from: intercultural-engagement, to: global-academic-community, note: "both concern contact beyond one culture" }
- { rel: related, from: social-responsibility, to: intercultural-engagement, note: "paired in the students' uses on p. 13" }
```

### B5 Rules
- internationalisation: do not reduce it to recruiting international students or adding foreign examples; the source says it reaches the whole institution and every student.
- intersectionality and scaffolded learning: gloss them on first use, because the source names them in segment labels without defining them.
- International Partnerships/ Global Partnerships: treat as one segment with two names, not two components.

## Part C Process

### C0 Formality
`not-applicable`: the model sets conditions and uses, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE
  title: "Framework for internationalising higher education"
  edition: "digital edition, 2024"
  year: 2024
  url: "https://www.advance-he.ac.uk (the series page not reached; D3)"
  retrieved: "PDF supplied by Abbott, 4 October 2026"
  licence: "none stated; held by permission (D-std-0019)"
  tier: primary
  readVia: direct
  held: 70b5ae7cf29e51dca9464be3ec05b4317b4a6794ec4deac172d2b5071d620930
  heldFiles: ["txt/advance-he-2024-framework-internationalising-higher-education-standard.txt", "txt/advance-he-2024-framework-internationalising-higher-education-standard.norm.txt", "records/advance-he-2024-framework-internationalising-higher-education-standard.held.json", "pdf/advance-he-2024-framework-internationalising-higher-education-standard.pdf"]
  citedIn: [0.2, S1, S2, S3, S4, M1, M2, M4, M5, B1]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: "2026-10-04", pass: P1, outcome: "used for every section; figure pages read as images (figure image)" }
- { ref: "ing:doc:internationalising-higher-education-framework-advance-he-2024", tier: primary, consulted: "2026-10-04", pass: P1, outcome: "read for consistency of component names; not cited" }
```

### D3 Wanted sources
```yaml
- { citation: "Advance HE, Student Success Frameworks (series web page), current", settles: ["S8", "S7"], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- Front matter, S1: no year or copyright notice is printed in the file; 2024 is taken from the PDF's creation date (9 February 2024; modified the same day). `copyrightNotice: none-stated`.
- Held text: held by Abbott's permission (4 October 2026, 05:03: "Yes full permission"; D-std-0019, as D-std-0013); private, never published.
- M2 order: clockwise from the top of each dial, read from the page images (pp. 7, 9, 11). Each dial has a divider at 12 o'clock, so the first segment is the one to its right (Training and Support Mechanisms; Positive Narratives; Research-Informed Pedagogy), as the worked example starts top right. The text layer and ing run 0138 start top left (Purposeful Approaches; Working in the Internationalisation Space; Support); the components are the same. For Abbott: confirm the start point for dials with a divider at the top.
- M2 labels: every label is found verbatim in the text layer, so MD-2 holds; "Support" occurs inside "Training and Support Mechanisms" first, so its span is anchored after the students' framing prose. "International Partnerships/ Global Partnerships" keeps the issuer's space after the slash; it is one segment with two names.
- M4: no segment is left blank in any dial, and the text says nothing of open segments; `[]`. Unlike the inclusive model, the dials have six and seven segments.
- M2 explainedBy: links marked `inferred` are std's reading; the source names its segments without defining any of them, and ties almost no prose to them.
- M6: the provisional practice theme theme:intercultural-engagement is confirmed by this model: it is the main theme of the educators' intercultural engagement and the students' effective intercultural relations components, and a second theme of social opportunities.
- M6 proposed practice theme: theme:whole-institution (a purpose is pursued on purpose, resourced, supported and joined up, and everyone owns a part of it); carried by purposeful approaches, training and support, resourced, cohesive approaches and working in the internationalisation space.
- M6 proposed practice theme: theme:interconnectivity (learning and work connect across disciplines, institutions and countries through active links); carried by interconnectivity, cross disciplinary, global academic community and the partnerships segment.
- M6 proposed practice theme: theme:embedded-practice (an aim is built into curriculum, teaching and assessment, not added on); carried by embedded practices.
- M6 proposed practice theme: theme:evidence-informed-enhancement (practice rests on evidence and its effects are checked); carried by evidence informed practice and research-informed pedagogy.
- M6 proposed practice theme: theme:global-citizenship (knowledge is made and used openly, reciprocally and ethically, with regard for others); carried by social responsibility.
- M6 doubt: positive narratives takes theme:authenticity (learners bring who they are, treated as an asset) as the nearest shared theme for framing difference as gain; an asset-framing theme of its own may be better. Support and scaffolded learning take theme:transition on our reading only: the source does not define either. For Abbott.
- S4 force: the two framing lines read as must ("responsibility" and "requires", D-std-0016). The imperative use items are read as `should`, marked on each force line; for Abbott: rule whether these read as should. "Staff may wish to consider" (p. 14) is permissive and not a statement.
- S4 use list: the text layer misplaces the institution's first use ("Inform and enhance ...") under the "Educators" heading and runs two pairs of items into one paragraph each. Perspective and order are read from the page image (pp. 12-13): institution, then educators, then students, three each.
- S4 use.educators.1 and use.educators.2 are function lines (what the model is or does), mood declarative, force describes; use.educators.2 has no main verb.
- S6: theme:internationalisation is carried, stated (the subject throughout). theme:edi is inferred from "inclusive learning environment" (p. 2) and the intersectionality segment; EDI is named only in the excluded back cover. theme:employability is stated once (p. 10).
- S7 siblingOf: the text names "other Student Success Frameworks" (p. 14) but no sibling by name, so no siblingOf or pointsTo relation is recorded.
- M5: the PSF table names V1, V2, V3, V4, A1, A2, A4 and K2, read from the page image and matching the text layer (where V4 is displaced after K2).
- D3: Advance HE's web page for the series (current status, date, the full list of frameworks in the series) not reached; wanted.

---

## Change notes
- 0.1.1, 2026-10-04 09:26: practice themes aligned across the series by std (20 id(s) renamed by tools/theme_merges.json; the old ids are aliases in the shared theme register); rebuilt on builder 0.2.1. Model template 0.3.0-draft, builder 0.2.1: 20 components, 0 open segments, 11 statements, 12 practice themes.
- 0.1.0, 2026-10-04 09:19: first built (Abbott, 09:08: "Use your template model and refine as you go"; D-std-0018). Model template 0.2.0-draft, builder 0.2.0: 20 components, 0 open segments, 11 statements, 12 practice themes.
