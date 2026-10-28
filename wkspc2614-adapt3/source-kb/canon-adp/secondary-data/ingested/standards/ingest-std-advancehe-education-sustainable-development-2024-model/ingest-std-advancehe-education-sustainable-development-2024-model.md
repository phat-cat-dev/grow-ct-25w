---
id: std:doc:advancehe-education-sustainable-development-2024-model
title: "Education for sustainable development framework"
profile: standards/model
profileVersion: none yet   # the variant's profile part is to write
issuer: Advance HE
kind: model
modelKind: condition-model
series: advancehe-student-success-frameworks-2024
axes: { perspectives: 3, facets: 0, groups: 0, segments: 18, openSegments: 0, labelsNotInText: 0 }
jurisdiction: [UK]   # not stated; Advance HE is UK-based and its frameworks are used internationally (inferred)
subjectScope: universal
subjects: []
edition: "digital edition, 2024"
published: 2024   # no date printed; from the PDF metadata (Part E)
revised: "none-stated"   # a later file date, if any (Part E)
status: current   # as at the held text; not checked against Advance HE's site (D3)
supersedes: "none-stated"
heldText: { method: sha256-bytes, raw: e8c1801550ab5404236ec1a207a5faf102e880881d97a2d22e70ef37d7f30f88, normalised: df449ad7a2a7398ac3e898e9d4843b8f7f6e214166e8d466f8b786dea04574f8 }
original: { method: sha256-bytes, pdf: 574061a6370d464670747420d81375f89ca7ffe15fc35090c182a62dbce87a83, held: "library pdf/advance-he-2024-education-sustainable-development-framework-standard.pdf" }
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
# Education for sustainable development framework

> The issuer's text is held beside this document in the library (`txt/advance-he-2024-education-sustainable-development-framework-standard.norm.txt`). Each M2 `label` (where the text layer holds it), each `explainedBy` and M4 `source` and each S4 `source` is exactly its span's text, held for language analysis (D-std-0014); private, never published. Every other field is ours, and agents phrase from ours.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
A practice model from Advance HE's Student Success Frameworks: eighteen components of education for sustainable development, six each for the institution, educators and students, each held here as a practice theme that can qualify the context of a lesson or a piece of material. The student dial names sustainability competencies; the other two name what staff and institutions do so that students can build them. Reach for it to set or check the conditions for sustainability learning. It sets no levels and no outcomes: pair it with the QAA and Advance HE ESD guidance (2021) for what students achieve.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Advance HE (2024) presents education for sustainable development as giving students the knowledge, abilities and values to act on linked economic, social and environmental problems, and as a driver of wider student success. It works best, it says, when the whole institution takes it up. It draws three dials, for the institution, educators and students, each with six named segments and none left blank. Its few obliging lines say higher education has to prepare graduates to act, and that quality processes and cross-subject work should support this; a short list of uses is given for each perspective. It links itself to all PSF 2023 values and activities and to three of the five core knowledge dimensions, and invites its use as Fellowship evidence. It binds no one: it is an enhancement model.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: Advance HE
title: "Education for sustainable development framework"
series: "Advance HE Student Success Frameworks"
edition: "digital edition, 2024"
dates:
  published: 2024   # not printed; PDF metadata
  other: ["PDF created 4 March 2024", "PDF modified 28 April 2025"]
kind: model
jurisdiction: [UK]
authority: advisory
licence: "none stated in the file (D1)"
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the conditions for education for sustainable development across an institution, its teaching and its students' competencies (D1, pp. 2-3)"
appliesTo:
  awards: [none-stated]
  levels: [none]
  providers: ["higher education institutions (as stated: \"our institutions\")"]
whoMustUse: "no one must; offered to a broad audience and named as useful to course teams, students and institutions; the source says ESD works best when the whole institution takes it up (D1, p. 3)"
howUsed: ["design", "review", "other: strategy, quality assurance, staff development, Fellowship evidence"]
doesNot: "none-stated"
beneficiary: the student
statedScope: "The framework is designed to be of value to a broad audience and can be particularly beneficial in:"
statedScopeLocator: "D1, p. 3"
statedScopeSpan: { start: 627, end: 726 }
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "what-is", order: 1, componentType: section, parent: "none", heading: "What is education for sustainable development?", gloss: "definition and ESD as a driver of student success", pages: "2", readFrom: "text layer" }
  - { number: "who-for", order: 2, componentType: section, parent: "none", heading: "Who is the framework for?", gloss: "the whole-institution condition and four uses", pages: "3", readFrom: "text layer" }
  - { number: "beneficial", order: 3, componentType: stem, parent: "who-for", heading: "The framework is designed to be of value to a broad audience and can be particularly beneficial in:", gloss: "the lead-in to the four uses", pages: "3", readFrom: "text layer" }
  - { number: "why", order: 4, componentType: section, parent: "none", heading: "Why is education for sustainable development important?", gloss: "rationale: graduates' role and demand for sustainability skills", pages: "4", readFrom: "text layer" }
  - { number: "structure", order: 5, componentType: figure, parent: "none", heading: "How is the education for sustainable development framework structured?", gloss: "the three perspectives shared by the series", pages: "5", readFrom: "figure image" }
  - { number: "institution", order: 6, componentType: perspective, parent: "none", heading: "Institution", gloss: "framing prose: whole-institution approach, quality assurance, interdisciplinary work", pages: "6", readFrom: "text layer" }
  - { number: "institution.dial", order: 7, componentType: figure, parent: "institution", heading: "(dial)", gloss: "six segments", pages: "7", readFrom: "figure image" }
  - { number: "educators", order: 8, componentType: perspective, parent: "none", heading: "Educators+", gloss: "framing prose: problem- and project-based learning on real challenges", pages: "8", readFrom: "text layer" }
  - { number: "educators.dial", order: 9, componentType: figure, parent: "educators", heading: "(dial)", gloss: "six segments", pages: "9", readFrom: "figure image" }
  - { number: "students", order: 10, componentType: perspective, parent: "none", heading: "Students", gloss: "framing prose: sustainability competencies as ways of thinking, practising and being", pages: "10", readFrom: "text layer" }
  - { number: "students.dial", order: 11, componentType: figure, parent: "students", heading: "(dial)", gloss: "six segments", pages: "11", readFrom: "figure image" }
  - { number: "use", order: 12, componentType: use-list, parent: "none", heading: "How can you use the framework?", gloss: "purpose and three uses for each perspective", pages: "12-13", readFrom: "figure image" }
  - { number: "psf", order: 13, componentType: section, parent: "none", heading: "How does this framework align with the Professional Standards Framework (PSF) 2023?", gloss: "the PSF crosswalk table and the Fellowship invitation", pages: "14", readFrom: "text layer" }
excluded:
  - { number: "back-cover", heading: "We help higher education organisations be the best they can be ...", kind: "other: the issuer's promotional back cover", pages: "back cover (PDF p. 9)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only obliging framing lines, requirement lists and use lists are statements (model template rule 3). -->
```yaml
- id: advancehe/esd-2024/frame.whole-institution
  locator: { number: "frame.whole-institution", heading: "Who is the framework for?", page: 3 }
  span: { start: 520, end: 626 }
  source: "This requires collaboration among educators, professional services, estates, decision-makers and students."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "requires" read as must; conditional on the preceding sentence (ESD works best when the whole institution takes it up)
  level: none
  perspective: perspective:institution
  mood: declarative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["requires"]
  about: "collaboration across the institution"
  themes: ["none"]
  paraphrase: "A whole-institution approach needs teachers, professional services, estates staff, leaders and students to work together."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/frame.why
  locator: { number: "frame.why", heading: "Why is education for sustainable development important?", page: 4 }
  span: { start: 2189, end: 2347 }
  source: "Higher education must therefore equip them with the skills and agency required to have a positive impact on social, economic and environmental sustainability."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "must"
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["must", "equip", "required", "have"]
  about: "the sector's duty to prepare graduates"
  themes: ["none"]
  paraphrase: "Higher education has to give students the skills and agency to make a positive difference to sustainability."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/frame.institution.qa
  locator: { number: "frame.institution.qa", heading: "Institution", page: 6 }
  span: { start: 3632, end: 3797 }
  source: "Quality assurance processes should ensure the integration of ESD into curriculum design, development, approval and review, following national and subject guidelines."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # D-std-0016: "should"
  level: none
  perspective: perspective:institution
  mood: declarative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["should", "ensure", "following"]
  about: "sustainability in quality processes"
  themes: ["none"]
  paraphrase: "Quality processes should make sure sustainability is built into how courses are designed, approved and reviewed, in line with national and subject expectations."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/frame.institution.interdisciplinary
  locator: { number: "frame.institution.interdisciplinary", heading: "Institution", page: 6 }
  span: { start: 3877, end: 4013 }
  source: "Interdisciplinary and multidisciplinary approaches should be encouraged and resourced and teams supported to overcome internal barriers."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # D-std-0016: "should"
  level: none
  perspective: perspective:institution
  mood: declarative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["should", "encouraged", "resourced", "supported", "overcome"]
  about: "resourcing work across disciplines"
  themes: ["none"]
  paraphrase: "The institution should encourage and fund work across disciplines and help teams get past internal obstacles."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/frame.psf
  locator: { number: "frame.psf", heading: "How does this framework align with the Professional Standards Framework (PSF) 2023?", page: 14 }
  span: { start: 8290, end: 8443 }
  source: "It requires consideration on how students learn both within their discipline and beyond and challenges traditional approaches to teaching and assessment."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "requires" read as must; the line says what engaging with ESD involves, so it may be descriptive (Part E)
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["requires", "learn", "challenges"]
  about: "rethinking teaching and assessment for ESD"
  themes: ["none"]
  paraphrase: "Taking up ESD means thinking about how students learn inside and outside their subject, and it questions familiar ways of teaching and assessing."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/beneficial.1
  locator: { number: "beneficial.1", heading: "Who is the framework for?", page: 3 }
  span: { start: 1323, end: 1504 }
  source: "supporting course teams to understand ESD and adopt a consistent approach to integrating it across programmes, including supporting co-curricular and interdisciplinary opportunities"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: beneficial
  statementType: guidance
  force: describes   # states without obliging
  level: none
  perspective: perspective:educators
  mood: gerund
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["supporting", "understand", "adopt", "integrating"]
  about: "a consistent course-wide approach"
  themes: ["none"]
  paraphrase: "One use of the model is helping course teams understand ESD and take a consistent approach to it across their courses, inside and outside the curriculum."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/beneficial.2
  locator: { number: "beneficial.2", heading: "Who is the framework for?", page: 3 }
  span: { start: 1507, end: 1633 }
  source: "helping students identify the necessary competencies for sustainable citizenship and fostering agency for a sustainable future"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: beneficial
  statementType: guidance
  force: describes   # states without obliging
  level: none
  perspective: perspective:students
  mood: gerund
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: both
  verbs: ["helping", "identify", "fostering"]
  about: "students finding the competencies they need"
  themes: ["none"]
  paraphrase: "Another use is helping students see which competencies sustainable citizenship needs and building their sense that they can act."
  audience: both
  subjects: inherited
- id: advancehe/esd-2024/beneficial.3
  locator: { number: "beneficial.3", heading: "Who is the framework for?", page: 3 }
  span: { start: 1637, end: 1808 }
  source: "supporting institutions to develop comprehensive approaches that encompass policy frameworks, interdisciplinary learning, engagement with community groups and stakeholders"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: beneficial
  statementType: guidance
  force: describes   # states without obliging
  level: none
  perspective: perspective:institution
  mood: gerund
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["supporting", "develop", "encompass"]
  about: "a comprehensive institutional approach"
  themes: ["none"]
  paraphrase: "A third use is helping institutions build broad approaches that cover policy, learning across disciplines and work with communities and partners."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/beneficial.4
  locator: { number: "beneficial.4", heading: "Who is the framework for?", page: 3 }
  span: { start: 1811, end: 1874 }
  source: "aligning strategy to create a sustainable learning environment."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: beneficial
  statementType: guidance
  force: describes   # states without obliging
  level: none
  perspective: perspective:institution
  mood: gerund
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["aligning", "create"]
  about: "strategy for a sustainable setting"
  themes: ["none"]
  paraphrase: "A fourth use is lining up strategy so that the place of learning is itself sustainable."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/use.institution.1
  locator: { number: "use.institution.1", heading: "How can you use the framework?", page: 12 }
  span: { start: 6901, end: 7072 }
  source: "Develop leadership and structures to prioritise a whole-institution approach to ESD across education, research, knowledge exchange, civic engagement and estate management."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["Develop", "prioritise"]
  about: "leadership for a whole-institution approach"
  themes: ["none"]
  paraphrase: "Institutions should build leadership and structures that put a whole-institution approach to ESD first, across teaching, research, knowledge exchange, civic work and estate."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/use.institution.2
  locator: { number: "use.institution.2", heading: "How can you use the framework?", page: 12 }
  span: { start: 7073, end: 7219 }
  source: "Map, evaluate and enhance the extent to which staff and students can engage with ESD, and develop and embed meaningful quality assurance measures."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["Map", "evaluate", "enhance", "engage", "develop", "embed"]
  about: "measuring and assuring engagement with ESD"
  themes: ["none"]
  paraphrase: "Institutions should map, evaluate and improve how far staff and students can take part in ESD, and build real quality measures for it."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/use.institution.3
  locator: { number: "use.institution.3", heading: "How can you use the framework?", page: 12 }
  span: { start: 7220, end: 7353 }
  source: "Encourage staff development, recognise and celebrate good practice and reward sustainability initiatives from across the institution."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["Encourage", "recognise", "celebrate", "reward"]
  about: "developing and rewarding staff"
  themes: ["none"]
  paraphrase: "Institutions should encourage staff learning and recognise and reward sustainability work wherever it happens."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/use.educators.1
  locator: { number: "use.educators.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 6307, end: 6447 }
  source: "Map, evaluate and enhance the extent to which a module or course provides opportunities for students to develop sustainability competencies."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:educators
  mood: imperative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["Map", "evaluate", "enhance", "provides", "develop"]
  about: "mapping competency opportunities"
  themes: ["none"]
  paraphrase: "Staff should map, evaluate and improve how far a module or course lets students build sustainability competencies."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/use.educators.2
  locator: { number: "use.educators.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 7359, end: 7470 }
  source: "Take interdisciplinary approaches to exploring local and global challenges with internal and external partners."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:educators
  mood: imperative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["Take", "exploring"]
  about: "cross-subject work with partners"
  themes: ["none"]
  paraphrase: "Staff should explore local and global problems across disciplines and with partners inside and outside the institution."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/use.educators.3
  locator: { number: "use.educators.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 7471, end: 7668 }
  source: "Consider how sustainability competencies can connect with and reinforce other strategic priorities such as employability, enterprise, entrepreneurship, inclusive curricula and internationalisation."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:educators
  mood: imperative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: provider
  verbs: ["Consider", "connect", "reinforce"]
  about: "linking competencies to other priorities"
  themes: ["none"]
  paraphrase: "Staff should look at how sustainability competencies tie in with and strengthen priorities such as employability, enterprise, inclusion and internationalisation."
  audience: practitioner
  subjects: inherited
- id: advancehe/esd-2024/use.students.1
  locator: { number: "use.students.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 7670, end: 7804 }
  source: "Develop the knowledge, competencies, attributes and agency to make informed decisions that contribute to a sustainable future for all."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:students
  mood: imperative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: learner
  verbs: ["Develop", "make", "contribute"]
  about: "building the capacity for informed decisions"
  themes: ["none"]
  paraphrase: "Students should build the knowledge, abilities and agency to make well-founded choices that help create a sustainable future for everyone."
  audience: both
  subjects: inherited
- id: advancehe/esd-2024/use.students.2
  locator: { number: "use.students.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 7816, end: 7911 }
  source: "Collaborate with others to develop fair and equitable solutions to local and global challenges."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:students
  mood: imperative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: learner
  verbs: ["Collaborate", "develop"]
  about: "working with others on fair solutions"
  themes: ["none"]
  paraphrase: "Students should work with others to find fair answers to local and global problems."
  audience: both
  subjects: inherited
- id: advancehe/esd-2024/use.students.3
  locator: { number: "use.students.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 7912, end: 8015 }
  source: "Reflect on how their personal experiences, beliefs and values impact their decision making and actions."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E); "their" shows the list describes students in the third person
  level: none
  perspective: perspective:students
  mood: imperative
  readFrom: "text layer"
  appliesTo: "education for sustainable development framework"
  addressee: learner
  verbs: ["Reflect", "impact"]
  about: "reflecting on values and choices"
  themes: ["none"]
  paraphrase: "Students should think about how their experiences, beliefs and values shape their decisions and actions."
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- statement: advancehe/esd-2024/frame.whole-institution
  forPractitioner: { text: "Bring teaching staff, professional services, estates, leaders and students into the same planning for sustainability.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to the institution as a whole", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present as the condition for a whole-institution approach, with must force from \"requires\". Note that students are named among the collaborators. Link to strategic alignment."
  author-agent-dialogue: "Raise it when sustainability planning involves only academics. Ask: \"Who from estates, services or the student body is part of this?\" Avoid implying any group is to blame."
- statement: advancehe/esd-2024/frame.why
  forPractitioner: { text: "Treat preparing students to act on sustainability as a core duty of the course, not an option.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to higher education as a sector", rewrite: full, force: must, status: drafted }
  author-agent-written: "The strongest obliging line in the model, addressed to higher education generally; force must. Do not attribute it to any regulator."
  author-agent-dialogue: "Raise it when a course team asks whether sustainability is their business. Ask: \"What skills will your graduates need to act on these challenges?\" Avoid moralising."
- statement: advancehe/esd-2024/frame.institution.qa
  forPractitioner: { text: "Add sustainability to course design, approval and review criteria, using national and subject expectations as the reference.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to the institution", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should. Link to the quality assurance component and to the 2021 ESD guidance and subject benchmarks, which are the likely national and subject references (our reading)."
  author-agent-dialogue: "Raise it in course approval. Ask: \"Which approval question would catch a course with no sustainability content?\""
- statement: advancehe/esd-2024/frame.institution.interdisciplinary
  forPractitioner: { text: "Fund and encourage teaching across disciplines, and help teams remove the internal obstacles that stop it.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to the institution", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should. Link to the interdisciplinary and interprofessional learning component."
  author-agent-dialogue: "Raise it when joint teaching stalls. Ask: \"What internal barrier is in the way, and who can lift it?\""
- statement: advancehe/esd-2024/frame.psf
  forPractitioner: { text: "Expect ESD to change how you teach and assess: plan for learning beyond your subject and question habits in your assessment design.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to teaching staff", rewrite: full, force: must, status: drafted }
  author-agent-written: "Force must from \"requires\", though the line reads partly as description (Part E). Link to the PSF 2023 crosswalk in M5."
  author-agent-dialogue: "Raise it when ESD is treated as content only. Ask: \"What would have to change in how you assess for this to count?\""
- statement: advancehe/esd-2024/beneficial.1
  forPractitioner: { text: "Use the model to agree one approach to sustainability across your course team, including extra-curricular and cross-subject opportunities.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: describes a use for course teams", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A use the issuer names, force describes. Link to the map opportunities component."
  author-agent-dialogue: "Raise it when modules handle sustainability inconsistently. Ask: \"Does the team share one approach?\""
- statement: advancehe/esd-2024/beneficial.2
  forPractitioner: { text: "Use the student dial to help students name the competencies they need and build their confidence to act.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can use this to work out which abilities you need to act for a sustainable future, and to grow your confidence that you can.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A use the issuer names, force describes. Link to the six student components."
  author-agent-dialogue: "Raise it in personal tutoring. Ask: \"Which of these abilities do you already have, and which would you like to build?\""
- statement: advancehe/esd-2024/beneficial.3
  forPractitioner: { text: "Use the institution dial to check that policy, cross-subject learning and community partnerships are all in your plan.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: describes a use for institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A use the issuer names, force describes. Link to the interdisciplinary, stakeholder and civic components."
  author-agent-dialogue: "Raise it in institutional planning. Ask: \"Which of these three does the current plan leave out?\""
- statement: advancehe/esd-2024/beneficial.4
  forPractitioner: { text: "Use the model to line up strategy so that the learning environment practises sustainability.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: describes a use for institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A use the issuer names, force describes. Link to the strategic alignment component."
  author-agent-dialogue: "Raise it in strategy work. Ask: \"Does the campus show students what we teach them?\""
- statement: advancehe/esd-2024/use.institution.1
  forPractitioner: { text: "Give someone the authority and structures to lead sustainability across teaching, research, knowledge exchange, civic work and estate together.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Note the five areas named. Link to the strategic alignment and civic university components."
  author-agent-dialogue: "Raise it with leaders. Ask: \"Who is responsible for sustainability across all five areas, not just one?\""
- statement: advancehe/esd-2024/use.institution.2
  forPractitioner: { text: "Find out how far staff and students can take part in sustainability learning, improve it, and build quality measures that mean something.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Link to the quality assurance component."
  author-agent-dialogue: "Raise it in quality review. Ask: \"How would we know whether students can engage with ESD here?\""
- statement: advancehe/esd-2024/use.institution.3
  forPractitioner: { text: "Support staff learning on sustainability, and recognise and reward the work people do on it in every part of the institution.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Link to the staff development component."
  author-agent-dialogue: "Raise it when staff effort goes unnoticed. Ask: \"How is sustainability work recognised here?\""
- statement: advancehe/esd-2024/use.educators.1
  forPractitioner: { text: "Map where your module or course lets students build sustainability competencies, judge how well, and improve it.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Link to the map opportunities and evaluate impact components."
  author-agent-dialogue: "Raise it at module review. Ask: \"Which competency does this module build, and how well?\""
- statement: advancehe/esd-2024/use.educators.2
  forPractitioner: { text: "Explore local and global problems with colleagues from other subjects and with outside partners.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Link to the model collaborative approaches and stakeholder engagement components."
  author-agent-dialogue: "Raise it in planning. Ask: \"Who outside your subject could help students see this problem whole?\""
- statement: advancehe/esd-2024/use.educators.3
  forPractitioner: { text: "Look for where sustainability competencies also serve employability, enterprise, inclusion and internationalisation, and design for both.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Link to the connect ESD component and to sibling models in the series."
  author-agent-dialogue: "Raise it when priorities compete for time. Ask: \"Which other aim could this task serve at the same time?\""
- statement: advancehe/esd-2024/use.students.1
  forPractitioner: { text: "Help students build the knowledge, abilities and confidence to make well-founded choices for a sustainable future.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "You should build the knowledge, abilities and confidence to make well-founded choices that help create a sustainable future for everyone.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading), addressed to students. Link to the action focused and critical thinker components."
  author-agent-dialogue: "Raise it in tutoring. Ask: \"What would you need to know to make a good choice on this?\""
- statement: advancehe/esd-2024/use.students.2
  forPractitioner: { text: "Set team tasks in which students seek fair answers to local and global problems.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "You should work with others to find fair answers to problems close to home and across the world.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Note \"fair and equitable\": fairness is part of the aim. Link to the collaborative and strategic practitioner component."
  author-agent-dialogue: "Raise it in group work. Ask: \"Who would gain and who would lose from your solution?\""
- statement: advancehe/esd-2024/use.students.3
  forPractitioner: { text: "Build in reflection on how students' experiences, beliefs and values shape what they decide and do.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "You should think about how your own experiences, beliefs and values shape what you decide and do.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Note the shift to \"their\": the item describes students rather than addressing them. Link to the self-aware and reflective component."
  author-agent-dialogue: "Raise it after a decision. Ask: \"What in your own background shaped that choice?\""
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
- { id: theme:esd, role: carries, carriedIn: ["what-is", "who-for", "why", "institution", "educators", "students", "use", "psf"], basis: "stated: education for sustainable development is the model's subject" }
- { id: theme:employability, role: carries, carriedIn: ["what-is", "educators.dial", "students", "use"], basis: "stated: named on pp. 2, 9, 10 and 13" }
- { id: theme:enterprise, role: carries, carriedIn: ["what-is", "students", "use"], basis: "stated: enterprise and entrepreneurship named on pp. 2, 10 and 13" }
- { id: theme:edi, role: carries, carriedIn: ["what-is", "why", "educators.dial", "use"], basis: "stated: EDI named in an educators segment (p. 9); inclusivity on p. 2" }
- { id: theme:internationalisation, role: carries, carriedIn: ["what-is", "use"], basis: "stated: named on pp. 2 and 13" }
- { id: theme:wellbeing, role: carries, carriedIn: ["what-is"], basis: "stated: mental health and wellbeing named once (p. 2); no component carries it" }
- { id: theme:student-partnership, role: carries, carriedIn: ["educators.dial"], basis: "inferred: our reading of the co-creation segment (Part E)" }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: partOf, target: "advancehe-student-success-frameworks-2024", note: "Advance HE Student Success Frameworks; the three-perspective structure is shared by the series (D1, p. 5)" }
- { rel: partOf, target: "std:doc:advancehe-enhancing-student-success-2024-model", note: "the series overview names education for sustainable development as one of its areas" }
- { rel: alignsWith, target: "std:doc:advancehe-psf-dimensions-2023-framework", note: "stated: the PSF table names V1-V5, A1-A5 and K1-K3 (M5)" }
- { rel: refersTo, target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "our link, inferred: the model names no source; its \"national and subject guidelines\" (p. 6) and its student competencies point to this guidance (Part E)" }
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
  - { id: perspective:educators, label: "Educators+", page: 9, segments: 6, openSegments: 0, note: "labelled \"Educators+\" throughout (pp. 5, 8, 12); the series axis that other models label \"Educators and related staff\"" }
  - { id: perspective:students, label: "Students", page: 11, segments: 6, openSegments: 0 }
groups: none
use: "to help readers see how students build sustainability competencies and where staff and institutions can act on the learning experience; the three perspectives can be used apart or together, to trace institutional policy into course practice and its effect on students; each perspective has three uses (S4 use.*) (D1, pp. 12-13)"
```

### M2 Components
<!-- label: both; status: drafted; basis: primary. In the figure's order (Part E). -->
```yaml
- id: advancehe/esd-2024/institution.quality-assurance
  label: "Quality Assurance"
  span: { start: 4110, end: 4127 }
  position: { axis: perspective:institution, group: none, order: 1, page: 7 }
  explainedBy:
    - { span: { start: 3632, end: 3797 }, source: "Quality assurance processes should ensure the integration of ESD into curriculum design, development, approval and review, following national and subject guidelines.", link: stated, page: 6 }
    - { span: { start: 7073, end: 7219 }, source: "Map, evaluate and enhance the extent to which staff and students can engage with ESD, and develop and embed meaningful quality assurance measures.", link: stated, page: 12 }
  conditionType: process
  actor: institution
  about: "sustainability built into quality processes"
  paraphrase: "The institution uses its course design, approval and review processes to check that sustainability is part of every curriculum, in line with national and subject expectations."
  themes: ["theme:whole-institution", "theme:evidence-informed-enhancement", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/institution.staff-development
  label: "Staff Development"
  span: { start: 4129, end: 4146 }
  position: { axis: perspective:institution, group: none, order: 2, page: 7 }
  explainedBy:
    - { span: { start: 3798, end: 3876 }, source: "This might require staff development and mechanisms for sharing best practice.", link: stated, page: 6 }
    - { span: { start: 7220, end: 7353 }, source: "Encourage staff development, recognise and celebrate good practice and reward sustainability initiatives from across the institution.", link: stated, page: 12 }
  conditionType: structure
  actor: institution
  about: "developing and rewarding staff for sustainability work"
  paraphrase: "The institution helps staff learn how sustainability applies to their work, shares what works and rewards those who lead change."
  themes: ["theme:professional-learning", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/institution.strategic-alignment
  label: "Strategic Alignment for a Sustainable University"
  span: { start: 4148, end: 4196 }
  position: { axis: perspective:institution, group: none, order: 3, page: 7 }
  explainedBy:
    - { span: { start: 3250, end: 3482 }, source: "Aligning all initiatives and strategies towards a shared vision of a sustainable institution and fostering internal collaboration can identify synergies, address challenges and model interdisciplinary and interprofessional learning.", link: stated, page: 6 }
    - { span: { start: 1811, end: 1874 }, source: "aligning strategy to create a sustainable learning environment.", link: stated, page: 3 }
    - { span: { start: 3483, end: 3631 }, source: "This ensures students learn within a sustainable university environment, reinforcing sustainability principles throughout their learning experience.", link: inferred, page: 6 }
  conditionType: structure
  actor: institution
  about: "one sustainability aim across the whole institution"
  paraphrase: "The institution points all its strategies, including estate and operations, at a shared aim of being sustainable, so that students learn in a place that practises what it teaches."
  themes: ["theme:whole-institution", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/institution.interdisciplinary-learning
  label: "Interdisciplinary and Interprofessional Learning"
  span: { start: 4060, end: 4108 }
  position: { axis: perspective:institution, group: none, order: 4, page: 7 }
  explainedBy:
    - { span: { start: 3877, end: 4013 }, source: "Interdisciplinary and multidisciplinary approaches should be encouraged and resourced and teams supported to overcome internal barriers.", link: stated, page: 6 }
    - { span: { start: 7359, end: 7470 }, source: "Take interdisciplinary approaches to exploring local and global challenges with internal and external partners.", link: inferred, page: 13 }
  conditionType: structure
  actor: institution
  about: "learning across subjects and professions"
  paraphrase: "The institution funds and enables learning that crosses subject and professional boundaries, and removes the internal obstacles that stop teams working together."
  themes: ["theme:collaboration", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/institution.stakeholder-engagement
  label: "Stakeholder Engagement"
  span: { start: 4036, end: 4058 }
  position: { axis: perspective:institution, group: none, order: 5, page: 7 }
  explainedBy:
    - { span: { start: 1759, end: 1808 }, source: "engagement with community groups and stakeholders", link: stated, page: 3 }
    - { span: { start: 4541, end: 4728 }, source: "Real-world challenges designed in partnership with external stakeholders such as employers and community groups or internal departments require learners to collaborate across disciplines.", link: inferred, page: 8 }
  conditionType: relationship
  actor: institution
  about: "working with partners beyond the institution"
  paraphrase: "The institution builds lasting relationships with employers, community groups and other partners who help shape and take part in sustainability learning."
  themes: ["theme:community-engagement", "theme:collaboration", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/institution.civic-university
  label: "Civic University"
  span: { start: 4018, end: 4034 }
  position: { axis: perspective:institution, group: none, order: 6, page: 7 }
  explainedBy:
    - { span: { start: 6901, end: 7072 }, source: "Develop leadership and structures to prioritise a whole-institution approach to ESD across education, research, knowledge exchange, civic engagement and estate management.", link: inferred, page: 12 }
    - { span: { start: 1248, end: 1316 }, source: "ESD is therefore beneficial both within and beyond our institutions.", link: inferred, page: 2 }
  conditionType: culture
  actor: institution
  about: "the institution serving its place"
  paraphrase: "The institution sees itself as part of its locality and puts its teaching, research and estate to work on the sustainability of the place around it."
  themes: ["theme:community-engagement", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/educators.globally-inclusive-curricula
  label: "Globally Inclusive and Future-focused Curricula"
  span: { start: 5039, end: 5086 }
  position: { axis: perspective:educators, group: none, order: 1, page: 9 }
  explainedBy:
    - { span: { start: 202, end: 450 }, source: "Education for sustainable development (ESD) in higher education equips learners with the knowledge, competencies and values to tackle interconnected global challenges, and have a positive impact on economic, social and environmental sustainability.", link: inferred, page: 2 }
    - { span: { start: 2023, end: 2188 }, source: "Graduates will have a critical role in developing viable, inclusive and equitable solutions to the economic, social and environmental challenges the world is facing.", link: inferred, page: 4 }
  conditionType: practice
  actor: educator
  about: "curricula with global reach and a view of the future"
  paraphrase: "Staff design curricula that draw on knowledge and voices from across the world and that look ahead to the problems students will face."
  themes: ["theme:systems-futures-thinking", "theme:intercultural-engagement", "theme:esd", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/esd-2024/educators.map-opportunities
  label: "Map Opportunities for ESD and Identify Gaps"
  span: { start: 5088, end: 5131 }
  position: { axis: perspective:educators, group: none, order: 2, page: 9 }
  explainedBy:
    - { span: { start: 6307, end: 6447 }, source: "Map, evaluate and enhance the extent to which a module or course provides opportunities for students to develop sustainability competencies.", link: stated, page: 13 }
    - { span: { start: 1323, end: 1504 }, source: "supporting course teams to understand ESD and adopt a consistent approach to integrating it across programmes, including supporting co-curricular and interdisciplinary opportunities", link: inferred, page: 3 }
  conditionType: process
  actor: educator
  about: "finding where sustainability is and is not taught"
  paraphrase: "Staff check where a module or course already gives students the chance to build sustainability competencies, and where it does not."
  themes: ["theme:evidence-informed-enhancement", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/educators.co-create
  label: "Co-create with Students to Identify Problems and Solutions"
  span: { start: 5133, end: 5191 }
  position: { axis: perspective:educators, group: none, order: 3, page: 9 }
  explainedBy:
    - { span: { start: 4541, end: 4728 }, source: "Real-world challenges designed in partnership with external stakeholders such as employers and community groups or internal departments require learners to collaborate across disciplines.", link: inferred, page: 8 }
    - { span: { start: 1507, end: 1633 }, source: "helping students identify the necessary competencies for sustainable citizenship and fostering agency for a sustainable future", link: inferred, page: 3 }
  conditionType: relationship
  actor: all
  about: "students as partners in framing problems"
  paraphrase: "Staff work with students as partners to choose which sustainability problems to tackle and to work out possible answers together."
  themes: ["theme:student-voice-partnership", "theme:esd", "theme:student-partnership"]
  sameLabelAs: none
- id: advancehe/esd-2024/educators.model-collaborative
  label: "Model Collaborative Approaches"
  span: { start: 5007, end: 5037 }
  position: { axis: perspective:educators, group: none, order: 4, page: 9 }
  explainedBy:
    - { span: { start: 3250, end: 3482 }, source: "Aligning all initiatives and strategies towards a shared vision of a sustainable institution and fostering internal collaboration can identify synergies, address challenges and model interdisciplinary and interprofessional learning.", link: inferred, page: 6 }
    - { span: { start: 7359, end: 7470 }, source: "Take interdisciplinary approaches to exploring local and global challenges with internal and external partners.", link: inferred, page: 13 }
  conditionType: practice
  actor: educator
  about: "staff showing collaboration in their own work"
  paraphrase: "Staff work together across subjects and with partners in ways students can see, so that students learn collaboration by example as well as by instruction."
  themes: ["theme:collaboration", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/educators.evaluate-impact
  label: "Evaluate Impact of ESD"
  span: { start: 4983, end: 5005 }
  position: { axis: perspective:educators, group: none, order: 5, page: 9 }
  explainedBy:
    - { span: { start: 6307, end: 6447 }, source: "Map, evaluate and enhance the extent to which a module or course provides opportunities for students to develop sustainability competencies.", link: stated, page: 13 }
    - { span: { start: 7073, end: 7219 }, source: "Map, evaluate and enhance the extent to which staff and students can engage with ESD, and develop and embed meaningful quality assurance measures.", link: inferred, page: 12 }
  conditionType: process
  actor: educator
  about: "finding out what sustainability teaching achieves"
  paraphrase: "Staff gather evidence of what their sustainability teaching achieves for students and use it to improve."
  themes: ["theme:evidence-informed-enhancement", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/educators.connect-esd
  label: "Connect ESD to Employability, Global Citizenship, Civic Responsibility and EDI"
  span: { start: 4903, end: 4981 }
  position: { axis: perspective:educators, group: none, order: 6, page: 9 }
  explainedBy:
    - { span: { start: 7471, end: 7668 }, source: "Consider how sustainability competencies can connect with and reinforce other strategic priorities such as employability, enterprise, entrepreneurship, inclusive curricula and internationalisation.", link: stated, page: 13 }
    - { span: { start: 1067, end: 1247 }, source: "ESD is a powerful driver of student success, enhancing internationalisation, employability and entrepreneurship, community engagement, inclusivity, and mental health and wellbeing.", link: stated, page: 2 }
  conditionType: practice
  actor: educator
  about: "linking sustainability to other priorities"
  paraphrase: "Staff show how sustainability learning connects with employability, global citizenship, civic responsibility and equality, diversity and inclusion, so that each strengthens the others."
  themes: ["theme:interconnectivity", "theme:esd", "theme:employability", "theme:edi"]
  sameLabelAs: none
- id: advancehe/esd-2024/students.action-focused
  label: "Action Focused"
  span: { start: 6113, end: 6127 }
  position: { axis: perspective:students, group: none, order: 1, page: 11 }
  explainedBy:
    - { span: { start: 5293, end: 5456 }, source: "ESD provides students with the opportunity to develop and practice the attributes and competencies required to act for the benefit of others now and in the future.", link: inferred, page: 10 }
    - { span: { start: 728, end: 867 }, source: "It enables learners to make informed decisions and take both individual and collective actions to transform society and protect the planet.", link: inferred, page: 2 }
  conditionType: disposition
  actor: student
  about: "moving from knowing to doing"
  paraphrase: "Students turn what they learn into action, alone and with others, for the good of people and the planet."
  themes: ["theme:action-competence", "theme:agency-self-actualisation", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/students.integrated-problem-solver
  label: "Integrated Problem Solver"
  span: { start: 6129, end: 6154 }
  position: { axis: perspective:students, group: none, order: 2, page: 11 }
  explainedBy:
    - { span: { start: 4729, end: 4898 }, source: "This fosters integrated problem-solving skills and self-awareness, enabling the development of solutions that will have a positive impact on society and the environment.", link: stated, page: 8 }
    - { span: { start: 4355, end: 4540 }, source: "What is evident, is that problem- or project-based learning, centred on authentic sustainability challenges, emerge as effective pedagogical methods regardless of the educational model.", link: inferred, page: 8 }
  conditionType: disposition
  actor: student
  about: "solving complex problems by combining approaches"
  paraphrase: "Students tackle complex sustainability problems by drawing together different kinds of knowledge and methods into workable solutions."
  themes: ["theme:collaboration", "theme:authenticity", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/students.self-aware-reflective
  label: "Self-aware and Reflective"
  span: { start: 6156, end: 6181 }
  position: { axis: perspective:students, group: none, order: 3, page: 11 }
  explainedBy:
    - { span: { start: 5457, end: 5652 }, source: "Sustainability competencies encompass ways of thinking, practicing and being, that enable learners to reflect on their values and appreciate how their beliefs and experiences shape their actions.", link: stated, page: 10 }
    - { span: { start: 7912, end: 8015 }, source: "Reflect on how their personal experiences, beliefs and values impact their decision making and actions.", link: stated, page: 13 }
  conditionType: disposition
  actor: student
  about: "knowing one's own values and their effects"
  paraphrase: "Students examine their own values, beliefs and experiences and see how these shape the choices they make."
  themes: ["theme:values-reflection", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/students.critical-thinker
  label: "Critical Thinker"
  span: { start: 6095, end: 6111 }
  position: { axis: perspective:students, group: none, order: 4, page: 11 }
  explainedBy:
    - { span: { start: 5457, end: 5652 }, source: "Sustainability competencies encompass ways of thinking, practicing and being, that enable learners to reflect on their values and appreciate how their beliefs and experiences shape their actions.", link: inferred, page: 10 }
    - { span: { start: 7670, end: 7804 }, source: "Develop the knowledge, competencies, attributes and agency to make informed decisions that contribute to a sustainable future for all.", link: inferred, page: 13 }
  conditionType: disposition
  actor: student
  about: "questioning claims about sustainability"
  paraphrase: "Students question claims, norms and practices about sustainability and reach their own reasoned positions."
  themes: ["theme:critical-thinking", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/students.systems-future-thinker
  label: "Systems and Future Thinker"
  span: { start: 6067, end: 6093 }
  position: { axis: perspective:students, group: none, order: 5, page: 11 }
  explainedBy:
    - { span: { start: 202, end: 450 }, source: "Education for sustainable development (ESD) in higher education equips learners with the knowledge, competencies and values to tackle interconnected global challenges, and have a positive impact on economic, social and environmental sustainability.", link: inferred, page: 2 }
    - { span: { start: 5792, end: 6019 }, source: "Guiding students towards recognising their role and influence in shaping a sustainable future demands cultivation of self-awareness and negotiation skills that will enable them to navigate conflicts of interest and uncertainty.", link: inferred, page: 10 }
  conditionType: disposition
  actor: student
  about: "seeing connections and possible futures"
  paraphrase: "Students see how parts of a problem connect across economy, society and environment, and think through possible futures and their consequences."
  themes: ["theme:systems-futures-thinking", "theme:esd"]
  sameLabelAs: none
- id: advancehe/esd-2024/students.collaborative-strategic-practitioner
  label: "Collaborative and Strategic Practitioner"
  span: { start: 6025, end: 6065 }
  position: { axis: perspective:students, group: none, order: 6, page: 11 }
  explainedBy:
    - { span: { start: 7816, end: 7911 }, source: "Collaborate with others to develop fair and equitable solutions to local and global challenges.", link: stated, page: 13 }
    - { span: { start: 5792, end: 6019 }, source: "Guiding students towards recognising their role and influence in shaping a sustainable future demands cultivation of self-awareness and negotiation skills that will enable them to navigate conflicts of interest and uncertainty.", link: inferred, page: 10 }
    - { span: { start: 5653, end: 5791 }, source: "Many of these competencies are critical attributes for wider aspects of success, including employability, enterprise and entrepreneurship.", link: inferred, page: 10 }
  conditionType: disposition
  actor: student
  about: "working with others to plan change"
  paraphrase: "Students work with others, negotiate between interests and plan steps that move a sustainability aim forward."
  themes: ["theme:collaboration", "theme:action-competence", "theme:esd", "theme:employability", "theme:enterprise"]
  sameLabelAs: none
```

### M2a Component audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- component: advancehe/esd-2024/institution.quality-assurance
  forPractitioner: { text: "Add sustainability to the questions asked when a course is designed, approved and reviewed, and use the answers to plan improvement rather than to tick a box.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your course to have been checked for how it prepares you to deal with sustainability, as part of the normal review of its quality.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a quality process that embeds sustainability, not a separate audit. Do not claim any national rule makes it compulsory; the source points to national and subject guidance. Set it beside the QAA and Advance HE ESD guidance (2021) and the relevant subject benchmark."
  author-agent-dialogue: "Raise it when a course is being designed or reviewed. Ask: \"Where in approval or review would anyone notice if sustainability were missing?\" and \"Which subject expectations apply here?\" Avoid presenting it as compliance alone."
- component: advancehe/esd-2024/institution.staff-development
  forPractitioner: { text: "Offer staff time and support to learn how sustainability bears on their subject or service, create ways to share practice, and recognise the people who move it forward.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the people who teach and support you to be learning, too, about how sustainability connects to what they do.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an institutional condition: staff learning is supported, shared and rewarded. Do not imply that staff lack commitment; the gap is usually time and confidence. Link it to the PSF 2023 and Fellowship, which the source names."
  author-agent-dialogue: "Raise it when a teacher says they do not know how sustainability fits their subject. Ask: \"What support or examples would help you see the connection?\" and \"Who in your area already does this well?\" Avoid suggesting every academic must become a sustainability expert."
- component: advancehe/esd-2024/institution.strategic-alignment
  forPractitioner: { text: "Join up the institution's plans for teaching, research, estate and operations behind one sustainability aim, and show students how the campus itself reflects it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the place where you study to practise sustainability in how it runs, not only to teach it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as the whole-institution approach the source puts first: teaching, estate and strategy pulling the same way. Do not claim the institution is sustainable; describe alignment as an aim. Link it to the civic university component."
  author-agent-dialogue: "Raise it when teaching about sustainability is contradicted by how the institution runs. Ask: \"Where does what students see on campus support or undercut what they are taught?\" Avoid accusing the institution of hypocrisy."
- component: advancehe/esd-2024/institution.interdisciplinary-learning
  forPractitioner: { text: "Fund and timetable shared modules and projects across departments and professions, and remove the regulatory and budget obstacles that keep teams apart.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect chances to work with students and staff from other subjects and professions on problems that no single subject can solve.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an institutional enabler: structures and resources that let teaching cross boundaries. Do not imply disciplines matter less; the point is combining them. Link it to the integrated problem solver and model collaborative approaches components."
  author-agent-dialogue: "Raise it when a course team wants to work with another department and meets obstacles. Ask: \"What stops this joint work: money, timetables or rules?\" and \"Who could remove that obstacle?\" Avoid underplaying real administrative limits."
- component: advancehe/esd-2024/institution.stakeholder-engagement
  forPractitioner: { text: "Build ongoing partnerships with employers, community groups and public bodies who can bring real sustainability problems and take part in teaching.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to meet and work with people outside the university who face sustainability problems in their work and communities.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe stakeholders as partners in learning, not only as audiences or funders. Do not invent particular partners. Link it to the civic university component and to the educators' co-creation segment."
  author-agent-dialogue: "Raise it when a course uses only invented case studies. Ask: \"Which local organisation faces this problem, and could they work with your students?\" Avoid assuming partners have time to give for free."
- component: advancehe/esd-2024/institution.civic-university
  forPractitioner: { text: "Treat the local area as a partner and a place to serve: direct teaching, research and estate decisions at the sustainability problems your community faces.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your studies to connect with the town or region around you, and to give you chances to make a difference there.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Use \"civic university\" for an institution that acts on its role in its place; the source names civic engagement in its uses but does not define the term. Do not overstate a local role the institution has not claimed. Link it to stakeholder engagement."
  author-agent-dialogue: "Raise it when sustainability is discussed only in global terms. Ask: \"What does this challenge look like in the place where you study?\" Avoid presuming the learner lives locally."
- component: advancehe/esd-2024/educators.globally-inclusive-curricula
  forPractitioner: { text: "Draw content, cases and voices from many parts of the world, including those most affected by environmental and social harm, and design tasks that look forward to future conditions.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will study problems as they affect people across the world, and think about what the future could look like and how to shape it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe \"globally inclusive\" as breadth of perspective and source, and \"future-focused\" as attention to what may come. The source does not define either term: say so if pressed. Link it to the systems and future thinker component and to internationalisation."
  author-agent-dialogue: "Raise it when a reading list or case set comes from one region. Ask: \"Whose experience of this problem is missing?\" and \"What might this look like in twenty years?\" Avoid tokenistic additions."
- component: advancehe/esd-2024/educators.map-opportunities
  forPractitioner: { text: "Go through each module and its assessments to find where students already meet sustainability, and plan to fill the gaps across the course as a whole.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a design task for course teams; students meet only its results", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present mapping as the first, diagnostic step: it finds existing coverage before adding more. Do not treat a mention of sustainability as evidence that students build a competency. Set it beside the eight competencies in the QAA and Advance HE ESD guidance (2021)."
  author-agent-dialogue: "Raise it at course design or review. Ask: \"Where in this course does a student practise this competency, and where is it only mentioned?\" Avoid implying every module must cover everything."
- component: advancehe/esd-2024/educators.co-create
  forPractitioner: { text: "Invite students to propose and frame the problems the course will address, and develop answers with them rather than handing them a set brief.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can help decide which problems to work on and shape the answers with your tutors, rather than only following a set brief.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe co-creation as shared framing of problems and answers, not consultation after the fact. The source's prose does not expand on this segment: say so if pressed. Link it to student partnership as a sector theme."
  author-agent-dialogue: "Raise it when a project brief is fully fixed before students arrive. Ask: \"Which part of this problem could students choose or define?\" Avoid handing students all the responsibility without support."
- component: advancehe/esd-2024/educators.model-collaborative
  forPractitioner: { text: "Teach with colleagues from other subjects or with partners, and let students see how you negotiate and share the work.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will see the people who teach you working together across subjects and with outside partners, and learn from how they do it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Stress \"model\": the staff practice is itself the lesson. Do not reduce it to setting group work for students. Link it to the collaborative and strategic practitioner component, which is the student side."
  author-agent-dialogue: "Raise it when a module asks students to collaborate but staff teach alone. Ask: \"Where could students see you working with someone from another field?\" Avoid implying solo teaching is poor."
- component: advancehe/esd-2024/educators.evaluate-impact
  forPractitioner: { text: "Collect evidence of what students can do after your sustainability teaching (in their work, reflections and choices) and change the teaching in light of it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You may be asked what difference this learning has made to how you think and act, and your answer can change how it is taught.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present evaluation as judging effect on students, not counting activities. Do not claim measured impact the source does not report. Pair it with the mapping component: mapping finds where; evaluation asks how well."
  author-agent-dialogue: "Raise it when a course reports only how much sustainability content it has. Ask: \"What can students now do that they could not before, and how do you know?\" Avoid demanding heavy measurement for small changes."
- component: advancehe/esd-2024/educators.connect-esd
  forPractitioner: { text: "Make the links explicit: show students how sustainability skills count in work, citizenship, civic life and equality, and design tasks that serve more than one of these at once.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "The sustainability skills you build also count for your career, your part in society and fairness for others; you will be shown how.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as connection, not competition between priorities. Name the four the segment lists. Do not claim the source shows evidence of the links; it asserts them. Link to the employability and inclusive learning and teaching models in the series."
  author-agent-dialogue: "Raise it when sustainability is treated as one more add-on. Ask: \"Which of your existing aims, such as employability or inclusion, could this task also serve?\" Avoid forcing a link that is not there."
- component: advancehe/esd-2024/students.action-focused
  forPractitioner: { text: "Give students real chances to act on what they learn, and to judge the effects of their actions, not only to analyse problems.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will be expected to act on what you learn, on your own and with others, and to see what difference it makes.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the step from understanding to action. Do not prescribe particular actions or political positions; describe the capacity to act. The 2021 ESD guidance has no matching competency; it is closest to strategic competency."
  author-agent-dialogue: "Raise it when a learner can describe a problem but sees no part for themselves. Ask: \"What is one thing you could do about this, and with whom?\" Avoid pressing anyone into activism."
- component: advancehe/esd-2024/students.integrated-problem-solver
  forPractitioner: { text: "Set real, open problems that cannot be solved from one subject alone, and help students combine methods into a workable answer.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will work on real problems with no single right answer and learn to combine different kinds of knowledge to find one that works.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Use \"integrated\" in the source's sense: problem-solving that combines disciplines and perspectives. Link it to problem- and project-based learning, which the source names as effective, and to the integrated problem-solving competency in the 2021 ESD guidance."
  author-agent-dialogue: "Raise it when a learner seeks the one correct answer. Ask: \"What would someone from another field add to this solution?\" Avoid suggesting any answer is as good as another."
- component: advancehe/esd-2024/students.self-aware-reflective
  forPractitioner: { text: "Build in regular reflection on how students' values and backgrounds shape their judgements on sustainability questions, and treat differences as material for learning.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will look at your own values and experiences and how they shape your choices, and learn from the ways others see things differently.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present reflection here as about values and their effect on action, as the source frames it. Do not prescribe which values are right. Link it to the self-awareness and normative competencies in the 2021 ESD guidance."
  author-agent-dialogue: "Raise it when a learner states a strong view on a sustainability question. Ask: \"What in your own experience leads you to that view?\" Avoid judging the learner's values."
- component: advancehe/esd-2024/students.critical-thinker
  forPractitioner: { text: "Ask students to test sustainability claims, including popular and commercial ones, against evidence and to question the assumptions behind current practice.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will learn to question claims about sustainability, including popular ones, and reach your own reasoned view.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "The source names this segment but its prose does not discuss critical thinking: draw on the critical thinking competency in the 2021 ESD guidance and say it is the link. Do not equate it with scepticism about climate science."
  author-agent-dialogue: "Raise it when a learner accepts a green claim at face value. Ask: \"What evidence would show this claim is true, and who benefits from it?\" Avoid encouraging cynicism."
- component: advancehe/esd-2024/students.systems-future-thinker
  forPractitioner: { text: "Ask students to trace links between the economic, social and environmental sides of a problem and to compare possible futures and their risks.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will learn to see how things connect, how a change in one place affects another, and to think about different possible futures.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Name both halves: systems thinking (connections) and futures thinking (what may come). The source does not explain the segment; link it to the systems and anticipatory competencies in the 2021 ESD guidance."
  author-agent-dialogue: "Raise it when a learner proposes a fix to one part of a problem. Ask: \"What else would this change affect?\" and \"How might this look in thirty years?\" Avoid overwhelming the learner with complexity."
- component: advancehe/esd-2024/students.collaborative-strategic-practitioner
  forPractitioner: { text: "Set team tasks in which students must negotiate between competing interests and plan realistic steps towards a shared sustainability aim.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will learn to work with people whose interests differ from yours and to plan practical steps towards a fair result.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Name both parts: collaboration (working with others, negotiating) and strategy (planning steps to an aim). Link it to the collaboration and strategic competencies in the 2021 ESD guidance and to employability and enterprise, which the source names."
  author-agent-dialogue: "Raise it when a group is stuck between competing views. Ask: \"What does each side need, and what first step could they all accept?\" Avoid presenting compromise as always right."
```

### M3 Conditions
<!-- label: editorial; status: drafted; basis: discussion. Ours, every field. -->
```yaml
- component: advancehe/esd-2024/institution.quality-assurance
  theme: theme:whole-institution
  holdsWhen: "Course design, approval and periodic review each include a question about sustainability, and the answers lead to recorded changes."
  signs: ["approval templates ask how the course addresses sustainability", "review reports record sustainability actions and follow them up", "panels cite subject or national expectations on sustainability"]
  absentWhen: "Sustainability is left to the interest of individual staff, and quality processes never ask about it."
  contextSteer: "State plainly where sustainability sits in the course's aims and outcomes, so the material can be traced to them."
  basis: ours
- component: advancehe/esd-2024/institution.staff-development
  theme: theme:professional-learning
  holdsWhen: "Staff have funded time and routes to learn about sustainability in their own field, and good practice is shared and recognised."
  signs: ["development sessions link sustainability to particular subjects or services", "staff share examples through a network or event", "awards or promotion criteria mention sustainability work"]
  absentWhen: "Staff are expected to embed sustainability with no time, examples or recognition, so few try."
  contextSteer: "Give worked examples from the subject so that a reader new to sustainability can see how it applies."
  basis: ours
- component: advancehe/esd-2024/institution.strategic-alignment
  theme: theme:whole-institution
  holdsWhen: "Strategies for education, research, estate and operations share a stated sustainability aim, and students can see it in their surroundings."
  signs: ["the strategy names sustainability across education, research and estate", "campus projects are used as teaching examples", "one group or person coordinates sustainability across departments"]
  absentWhen: "Each part of the institution pursues its own plan, and students meet sustainability in lectures but not in the place itself."
  contextSteer: "Use the learner's own institution or setting as a live example where it practises, or fails to practise, sustainability."
  basis: ours
- component: advancehe/esd-2024/institution.interdisciplinary-learning
  theme: theme:collaboration
  holdsWhen: "Students can take part in learning shared with other subjects or professions, and staff who run it are resourced and not blocked by internal rules."
  signs: ["modules or projects are shared across departments", "budgets or workload models credit joint teaching", "students work in mixed-discipline teams on a common problem"]
  absentWhen: "Each department teaches alone, and staff who try joint work meet budget or timetable walls."
  contextSteer: "Bring in at least one perspective from another subject or profession and show how it changes the problem."
  basis: ours
- component: advancehe/esd-2024/institution.stakeholder-engagement
  theme: theme:community-engagement
  holdsWhen: "External partners contribute to the design or delivery of learning, and the relationships last beyond a single project."
  signs: ["partners help set briefs or assess projects", "the same partners return across years", "students present work to the organisations that posed the problem"]
  absentWhen: "Learning stays inside the institution, and sustainability is studied only through published cases."
  contextSteer: "Set the task in a real setting with a named kind of partner and their constraints, rather than in the abstract."
  basis: ours
- component: advancehe/esd-2024/institution.civic-university
  theme: theme:community-engagement
  holdsWhen: "The institution names its local area as a focus, and students and staff work on that area's sustainability problems with local people."
  signs: ["projects address problems named by local bodies", "the institution reports its local sustainability work", "community members take part in events or teaching"]
  absentWhen: "The institution treats its locality as a backdrop, and sustainability learning has no local reference."
  contextSteer: "Tie the global issue to a local case the learner could visit or act on."
  basis: ours
- component: advancehe/esd-2024/educators.globally-inclusive-curricula
  theme: theme:systems-futures-thinking
  holdsWhen: "The curriculum draws on sources and cases from many regions and asks students to consider future scenarios, not only the present."
  signs: ["reading lists include authors from several world regions", "tasks ask students to project or compare future scenarios", "cases show how one problem differs across places"]
  absentWhen: "Content comes from one national or cultural frame and treats today's conditions as fixed."
  contextSteer: "Include a perspective from another part of the world and ask the learner how the issue may change over time."
  basis: ours
- component: advancehe/esd-2024/educators.map-opportunities
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Course teams hold a current map of where each sustainability competency is taught and assessed, and act on the gaps it shows."
  signs: ["a course map lists competencies against modules", "gaps found in the map lead to named changes", "teams revisit the map at each review"]
  absentWhen: "No one knows where sustainability appears in the course, so it is repeated in places and missing in others."
  contextSteer: "Say which sustainability competency the activity builds, so that it can be placed on a course map."
  basis: ours
- component: advancehe/esd-2024/educators.co-create
  theme: theme:student-voice-partnership
  holdsWhen: "Students take part in choosing or framing the problems they work on, and their ideas shape the solutions that are pursued."
  signs: ["students propose or refine project topics", "staff and students develop solutions in the same sessions", "student ideas change the brief"]
  absentWhen: "Problems and acceptable answers are set by staff in advance, and students carry them out."
  contextSteer: "Leave part of the problem for the learner to define, and invite them to propose their own route to a solution."
  basis: ours
- component: advancehe/esd-2024/educators.model-collaborative
  theme: theme:collaboration
  holdsWhen: "Students see staff from different subjects or organisations planning, teaching or solving problems together."
  signs: ["sessions are co-taught across subjects or with partners", "staff talk openly about how they reached a shared view", "students are shown how a joint decision was made"]
  absentWhen: "Staff ask students to collaborate while working alone themselves."
  contextSteer: "Show how people from different backgrounds would combine their views on the problem, not only what each would say."
  basis: ours
- component: advancehe/esd-2024/educators.evaluate-impact
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Teams collect evidence of students' sustainability learning and record the changes they make in response."
  signs: ["assessment shows students applying a sustainability competency", "student reflections are gathered and reviewed", "module reports note changes made after evaluation"]
  absentWhen: "Sustainability teaching is counted by hours or topics, and no one knows whether it changed anything."
  contextSteer: "End with a way for the learner to show, or reflect on, what they can now do differently."
  basis: ours
- component: advancehe/esd-2024/educators.connect-esd
  theme: theme:interconnectivity
  holdsWhen: "Tasks and course documents show how sustainability learning serves employability, citizenship, civic duty and inclusion as well."
  signs: ["learning outcomes name more than one of these aims", "careers or civic examples appear in sustainability tasks", "students can say how the learning helps them beyond the module"]
  absentWhen: "Sustainability sits apart from other priorities and competes with them for time."
  contextSteer: "Show the learner how the same skill matters for their working life and their part in society."
  basis: ours
- component: advancehe/esd-2024/students.action-focused
  theme: theme:action-competence
  holdsWhen: "Students carry out actions arising from their learning and reflect on what those actions achieved."
  signs: ["tasks end in an action, not only a report", "students describe something they changed", "students judge the effect of an action they took"]
  absentWhen: "Students analyse problems in depth but never act on them."
  contextSteer: "Close with a concrete action the learner could take, and ask how they would know it had worked."
  basis: ours
- component: advancehe/esd-2024/students.integrated-problem-solver
  theme: theme:collaboration
  holdsWhen: "Students produce solutions to open problems that combine more than one discipline or method and weigh their side effects."
  signs: ["solutions draw on more than one subject", "students explain trade-offs in their solution", "briefs come from real settings"]
  absentWhen: "Problems are closed and single-subject, with one expected answer."
  contextSteer: "Pose an open problem that needs more than one kind of knowledge, and ask the learner to weigh the trade-offs in their answer."
  basis: ours
- component: advancehe/esd-2024/students.self-aware-reflective
  theme: theme:values-reflection
  holdsWhen: "Students regularly reflect, with evidence, on how their values and experiences shaped a decision they made."
  signs: ["reflective tasks ask about values, not only process", "students name how their background shaped a judgement", "students revise a view after hearing others"]
  absentWhen: "Reflection is a summary of what was done, and values stay unexamined."
  contextSteer: "Ask the learner what values or experiences lead them to their view, without judging the answer."
  basis: ours
- component: advancehe/esd-2024/students.critical-thinker
  theme: theme:critical-thinking
  holdsWhen: "Students test sustainability claims against evidence and can explain the assumptions behind a practice or policy."
  signs: ["students check claims against sources", "students identify assumptions in a policy or product claim", "students defend a position with reasons"]
  absentWhen: "Students repeat claims about sustainability without asking how they are known."
  contextSteer: "Include a claim for the learner to test against evidence, and ask what assumptions lie behind it."
  basis: ours
- component: advancehe/esd-2024/students.systems-future-thinker
  theme: theme:systems-futures-thinking
  holdsWhen: "Students map connections within a problem and reason about more than one future outcome."
  signs: ["students draw or describe links between parts of a system", "students compare scenarios", "students spot unintended effects of a proposal"]
  absentWhen: "Problems are treated in isolation and only the present is considered."
  contextSteer: "Ask the learner to trace what else a change would affect and how the outcome might differ over time."
  basis: ours
- component: advancehe/esd-2024/students.collaborative-strategic-practitioner
  theme: theme:collaboration
  holdsWhen: "Students work in teams across differing interests and produce plans with realistic steps towards a shared aim."
  signs: ["teams record how they settled disagreements", "plans include stages, roles and risks", "students take account of interests other than their own"]
  absentWhen: "Group work divides tasks without negotiation, and plans stop at aims."
  contextSteer: "Set the task so that the learner must account for other people's interests and plan the first realistic steps."
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
  lead: { span: { start: 8193, end: 8289 }, source: "Engagement with ESD is closely aligned with the Professional Values articulated in the PSF 2023.", page: 14 }
  codes:
    - { to: advancehe/psf-dimensions-2023/V1, code: V1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V2, code: V2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V3, code: V3, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V4, code: V4, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V5, code: V5, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A1, code: A1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A2, code: A2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A3, code: A3, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A4, code: A4, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A5, code: A5, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K1, code: K1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K2, code: K2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K3, code: K3, page: 14, note: "named in the PSF table" }
  fellowship: { span: { start: 8713, end: 8927 }, source: "Advance HE invites all those teaching or supporting learning to evidence their use of this or other Student Success Frameworks in applying for Fellowship in recognition of their commitment to professional practice.", page: 14, note: "an invitation, not an obligation: not an S4 statement" }
inferred:
  - { from: "model", to: "theme:esd", rel: related, basis: inferred, note: "education for sustainable development is the model's whole subject" }
  - { from: "model", to: "std:doc:qaa-advancehe-esd-2021-guidance", rel: related, basis: inferred, note: "our link: the sector guidance on ESD from QAA and Advance HE; the model does not cite it" }
  - { from: "advancehe/esd-2024/institution.quality-assurance", to: "std:doc:qaa-advancehe-esd-2021-guidance", rel: related, basis: inferred, note: "\"national and subject guidelines\" (p. 6) read as this guidance and the subject benchmarks" }
  - { from: "advancehe/esd-2024/students.systems-future-thinker", to: "qaa-advancehe/esd-2021/competency.systems.b1", rel: related, basis: inferred, note: "systems thinking competency (2021 guidance, Table 1)" }
  - { from: "advancehe/esd-2024/students.systems-future-thinker", to: "qaa-advancehe/esd-2021/competency.anticipatory.b1", rel: related, basis: inferred, note: "anticipatory competency: the future half of the segment" }
  - { from: "advancehe/esd-2024/students.critical-thinker", to: "qaa-advancehe/esd-2021/competency.critical.b1", rel: related, basis: inferred, note: "critical thinking competency" }
  - { from: "advancehe/esd-2024/students.integrated-problem-solver", to: "qaa-advancehe/esd-2021/competency.problem.b1", rel: related, basis: inferred, note: "integrated problem-solving competency" }
  - { from: "advancehe/esd-2024/students.self-aware-reflective", to: "qaa-advancehe/esd-2021/competency.selfaware.b1", rel: related, basis: inferred, note: "self-awareness competency" }
  - { from: "advancehe/esd-2024/students.self-aware-reflective", to: "qaa-advancehe/esd-2021/competency.normative.b1", rel: related, basis: inferred, note: "normative competency: reflecting on values" }
  - { from: "advancehe/esd-2024/students.collaborative-strategic-practitioner", to: "qaa-advancehe/esd-2021/competency.collaborative.b1", rel: related, basis: inferred, note: "collaboration competency" }
  - { from: "advancehe/esd-2024/students.collaborative-strategic-practitioner", to: "qaa-advancehe/esd-2021/competency.strategic.b1", rel: related, basis: inferred, note: "strategic competency" }
  - { from: "advancehe/esd-2024/educators.connect-esd", to: "theme:employability", rel: related, basis: inferred, note: "named in the segment label" }
  - { from: "advancehe/esd-2024/educators.globally-inclusive-curricula", to: "theme:internationalisation", rel: related, basis: inferred, note: "global breadth of curriculum; the use list names internationalisation (p. 13)" }
```

### M6 Practice themes carried
<!-- label: both; status: drafted; basis: discussion -->
```yaml
- { id: theme:whole-institution, tier: practice, working: "the institution's strategy, quality processes, estate and staff pull together towards one aim", carriedBy: ["advancehe/esd-2024/institution.quality-assurance", "advancehe/esd-2024/institution.strategic-alignment"], status: provisional }
- { id: theme:evidence-informed-enhancement, tier: practice, working: "practice is mapped, its effects are evaluated and it is improved on that evidence", carriedBy: ["advancehe/esd-2024/institution.quality-assurance", "advancehe/esd-2024/educators.map-opportunities", "advancehe/esd-2024/educators.evaluate-impact"], status: provisional }
- { id: theme:professional-learning, tier: practice, working: "staff are given time, support and recognition to develop their practice", carriedBy: ["advancehe/esd-2024/institution.staff-development"], status: provisional }
- { id: theme:collaboration, tier: practice, working: "learning and problem-solving are done with others, across subjects, professions and sectors", carriedBy: ["advancehe/esd-2024/institution.interdisciplinary-learning", "advancehe/esd-2024/institution.stakeholder-engagement", "advancehe/esd-2024/educators.model-collaborative", "advancehe/esd-2024/students.integrated-problem-solver", "advancehe/esd-2024/students.collaborative-strategic-practitioner"], status: provisional }
- { id: theme:community-engagement, tier: practice, working: "learning connects with communities, employers and partners beyond the institution", carriedBy: ["advancehe/esd-2024/institution.stakeholder-engagement", "advancehe/esd-2024/institution.civic-university"], status: provisional }
- { id: theme:systems-futures-thinking, tier: practice, working: "problems are seen as connected systems and judged against possible futures", carriedBy: ["advancehe/esd-2024/educators.globally-inclusive-curricula", "advancehe/esd-2024/students.systems-future-thinker"], status: provisional }
- { id: theme:intercultural-engagement, tier: practice, working: "people from different cultures meet, work together and learn from each other", carriedBy: ["advancehe/esd-2024/educators.globally-inclusive-curricula"], status: provisional }
- { id: theme:student-voice-partnership, tier: practice, working: "a range of voices, students' included, shapes decisions and is answered", carriedBy: ["advancehe/esd-2024/educators.co-create"], status: provisional }
- { id: theme:interconnectivity, tier: practice, working: "work in one area, discipline or place is linked to others", carriedBy: ["advancehe/esd-2024/educators.connect-esd"], status: provisional }
- { id: theme:action-competence, tier: practice, working: "learners turn understanding into action and judge its effects", carriedBy: ["advancehe/esd-2024/students.action-focused", "advancehe/esd-2024/students.collaborative-strategic-practitioner"], status: provisional }
- { id: theme:agency-self-actualisation, tier: practice, working: "people grow into, use and trust their own judgement", carriedBy: ["advancehe/esd-2024/students.action-focused"], status: provisional }
- { id: theme:authenticity, tier: practice, working: "learners bring who they are, and that is treated as an asset", carriedBy: ["advancehe/esd-2024/students.integrated-problem-solver"], status: provisional }
- { id: theme:values-reflection, tier: practice, working: "learners examine how their values and experiences shape their judgements and actions", carriedBy: ["advancehe/esd-2024/students.self-aware-reflective"], status: provisional }
- { id: theme:critical-thinking, tier: practice, working: "questioning and evaluating are practised and valued", carriedBy: ["advancehe/esd-2024/students.critical-thinker"], status: provisional }
```

## Part B Terminology

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: education-for-sustainable-development, definition: "education that gives learners the knowledge, abilities and values to act on linked economic, social and environmental problems", scopeNote: "abbreviated ESD throughout; covers content, teaching methods and the learning environment", category: approach, practices: [learning-and-teaching] }
- { slug: whole-institution-approach, definition: "sustainability taken up across teaching, research, operations and estate rather than left to the curriculum alone", scopeNote: "the source puts it first under the institution; practice theme theme:whole-institution", category: approach, practices: [learning-and-teaching] }
- { slug: sustainability-competencies, definition: "the abilities, values and dispositions a person needs to act for sustainability", scopeNote: "the student dial names six; the 2021 ESD guidance names eight (UNESCO); the source does not cite either", category: concept, practices: [learning-and-teaching] }
- { slug: civic-university, definition: "an institution that acts on its role in and responsibility to its locality", scopeNote: "an institution segment; not defined in the source", category: concept, practices: [learning-and-teaching] }
- { slug: interprofessional-learning, definition: "learning in which students or staff from different professions learn with and from each other", scopeNote: "paired with interdisciplinary learning in an institution segment", category: concept, practices: [learning-and-teaching] }
- { slug: sustainable-citizenship, definition: "taking part in society in ways that support a sustainable future", scopeNote: "named once, in the uses on p. 3", category: concept, practices: [learning-and-teaching] }
```

### B2a Terms as the issuer uses them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: education-for-sustainable-development, form: "education for sustainable development", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: whole-institution-approach, form: "whole-institution approach", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: sustainability-competencies, form: "sustainability competencies", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: civic-university, form: "Civic University", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: interprofessional-learning, form: "interprofessional learning", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: sustainable-citizenship, form: "sustainable citizenship", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the model names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term takes a meaning of its own in one component.

### B4 Relations
```yaml
- { rel: related, from: whole-institution-approach, to: education-for-sustainable-development, note: "the source says ESD works best when the whole institution takes it up" }
- { rel: related, from: sustainability-competencies, to: education-for-sustainable-development, note: "what ESD develops in students; named on the student dial" }
- { rel: related, from: civic-university, to: whole-institution-approach, note: "civic engagement is one of the five areas of the whole-institution approach (p. 12)" }
- { rel: related, from: interprofessional-learning, to: whole-institution-approach, note: "modelled by internal collaboration (p. 6)" }
```

### B5 Rules
- education for sustainable development: write it out on first use and then use ESD, as the source does.
- sustainability competencies: when naming them, say whether you mean the six on the student dial or the eight in the 2021 ESD guidance, because the two lists differ.
- Civic University: gloss it on first use, because the source does not define it.

## Part C Process

### C0 Formality
`not-applicable`: the model sets conditions and uses, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE
  title: "Education for sustainable development framework"
  edition: "digital edition, 2024"
  year: 2024
  url: "https://www.advance-he.ac.uk (the series page not reached; D3)"
  retrieved: "PDF supplied by Abbott, 4 October 2026"
  licence: "none stated; held by permission (D-std-0019)"
  tier: primary
  readVia: direct
  held: e8c1801550ab5404236ec1a207a5faf102e880881d97a2d22e70ef37d7f30f88
  heldFiles: ["txt/advance-he-2024-education-sustainable-development-framework-standard.txt", "txt/advance-he-2024-education-sustainable-development-framework-standard.norm.txt", "records/advance-he-2024-education-sustainable-development-framework-standard.held.json", "pdf/advance-he-2024-education-sustainable-development-framework-standard.pdf"]
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
- Front matter, S1: no year or copyright notice is printed in the file; 2024 is taken from the PDF's creation date (4 March 2024; modified 28 April 2025). `copyrightNotice: none-stated`.
- Held text: held by Abbott's permission (4 October 2026, 05:03: "Yes full permission"; D-std-0019, as D-std-0013); private, never published.
- M2 order: clockwise from the top of each dial, read from the page images (pp. 7, 9, 11); each dial has a divider at the top, so the first segment is the one to its right. The text layer gives the labels in a different order. Every label is found verbatim in the held text as its own paragraph, so MD-2 holds.
- M1, M4: each dial has six segments and none is left blank; the source says nothing of open segments, so M4 is [].
- M2 explainedBy: links marked `inferred` are std's reading; the source does not tie its prose to its segments. Three segments have no prose that names them: Critical Thinker, Civic University and Co-create with Students to Identify Problems and Solutions; their explainedBy spans are all inferred.
- M5 inferred: the student dial's six segments fold UNESCO's eight key sustainability competencies, as the QAA and Advance HE ESD guidance (2021) lists them (systems and anticipatory into Systems and Future Thinker; collaboration and strategic into Collaborative and Strategic Practitioner; self-awareness and normative into Self-aware and Reflective). Action Focused has no counterpart there. This mapping is std's reading; the model cites neither UNESCO nor the 2021 guidance.
- S4 force: the imperative use items are read as `should`, marked on each force line; imperatives are not in D-std-0016. For Abbott: rule whether these read as should.
- S4 frame.psf: "It requires consideration on how students learn ..." is read as must from "requires", but it reads as what ESD involves more than as an obligation. For Abbott: keep as must, or treat as description.
- S4 not cut: "This might require staff development ..." (p. 6, possibility), "Real-world challenges ... require learners to collaborate" (p. 8, describes the method) and "... demands cultivation of self-awareness and negotiation skills ..." (p. 10, "demands" is not in D-std-0016) are read as descriptive prose and held as explainedBy spans.
- S4 beneficial.1-4: the four uses under "Who is the framework for?" are gerunds and recorded with force describes; the issuer lists them as uses, not audiences.
- S4 use.students.3: the item says "their" where the other student items are bare imperatives; the student list may be third-person description with "Students" as its implied subject. Recorded as imperative; for Abbott.
- M5 stated: the PSF table (p. 14, read from the image) shows V1 to V5, A1 to A5 and K1 to K3; K4 and K5 are not shown. The lead sentence names only the Professional Values, while the table shows Activity and Core Knowledge codes as well.
- S6: theme:esd is the model's subject (stated). Employability, enterprise, EDI, internationalisation and wellbeing are named in the text (stated); student partnership is our reading of the co-creation segment (inferred).
- M6: proposed practice themes, new in this model: theme:whole-institution, theme:evidence-informed-enhancement, theme:professional-learning, theme:collaboration, theme:community-engagement, theme:systems-futures-thinking, theme:interconnectivity, theme:action-competence, theme:values-reflection. Every practice theme is provisional until the shared theme register exists (Abbott, 05:09: "we will call them themes").
- S7 refersTo std:doc:qaa-advancehe-esd-2021-guidance: our link, inferred; the model names no source. Its "national and subject guidelines" (p. 6) most likely means that guidance and the subject benchmarks.
- D3: Advance HE's web page for the series (current status, date, the full list of frameworks in the series) not reached; wanted.

---

## Change notes
- 0.1.1, 2026-10-04 09:26: practice themes aligned across the series by std (3 id(s) renamed by tools/theme_merges.json; the old ids are aliases in the shared theme register); rebuilt on builder 0.2.1. Model template 0.3.0-draft, builder 0.2.1: 18 components, 0 open segments, 18 statements, 14 practice themes.
- 0.1.0, 2026-10-04 09:20: first built (Abbott, 09:08: "Use your template model and refine as you go"; D-std-0018). Model template 0.2.0-draft, builder 0.2.0: 18 components, 0 open segments, 18 statements, 14 practice themes.
