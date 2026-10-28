---
id: std:doc:advancehe-enhancing-assessment-2024-model
title: "Framework for enhancing assessment"
profile: standards/model
profileVersion: none yet   # the variant's profile part is to write
issuer: Advance HE
kind: model
modelKind: condition-model
series: advancehe-student-success-frameworks-2024
axes: { perspectives: 3, facets: 0, groups: 4, segments: 27, openSegments: 0, labelsNotInText: 16 }
jurisdiction: [UK]   # not stated; Advance HE is UK-based and its frameworks are used internationally (inferred)
subjectScope: universal
subjects: []
edition: "digital edition, 2024 (file revised April 2025)"
published: 2024   # no date printed; from the PDF metadata (Part E)
revised: "none-stated"   # a later file date, if any (Part E)
status: current   # as at the held text; not checked against Advance HE's site (D3)
supersedes: "none-stated"
heldText: { method: sha256-bytes, raw: d66604a96910bea7bcb2ecb3d625673e2723d9d4c4ae6d1de87e7ee8466f83f0, normalised: e05bdc27ffced7a0117705a74455c3c7d4f848e64af024e7c2e9bef8d797bf89 }
original: { method: sha256-bytes, pdf: 30c52c874c1081da5aa2c0fecc7e8b2c43ead3d0676ea3829e3774adf496bc3c, held: "library pdf/advance-he-2024-framework-enhancing-assessment-standard.pdf" }
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
# Framework for enhancing assessment

> The issuer's text is held beside this document in the library (`txt/advance-he-2024-framework-enhancing-assessment-standard.norm.txt`). Each M2 `label` (where the text layer holds it), each `explainedBy` and M4 `source` and each S4 `source` is exactly its span's text, held for language analysis (D-std-0014); private, never published. Every other field is ours, and agents phrase from ours.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
A practice model from Advance HE's Student Success Frameworks: twenty-seven components of assessment and feedback practice, seen from the institution, educators and students and grouped in four areas of focus, each held here as a practice theme that can qualify the context of a lesson, a task or a piece of material. Reach for it to set or check the conditions under which students are assessed and given feedback. It sets no levels and no outcomes: pair it with a framework or benchmark for what students achieve.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Advance HE (2024; the file was revised in April 2025) treats assessment as both judgement, which must be valid and reliable, and a driver of learning. It names four areas of focus: embedding in the curriculum; systems, processes and policy; innovative assessment; and staff development. The institution dial sets sixteen segments in those four areas, the educators dial shows the four areas themselves, and the students dial has seven segments. Framing lines tie clear criteria and feedback to closing awarding gaps, and short lists of uses are given for each perspective. It links six dimensions of the Professional Standards Framework 2023 and invites its use as Fellowship evidence. It binds no one: it is an enhancement model, not an assurance standard.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: Advance HE
title: "Framework for enhancing assessment"
series: "Advance HE Student Success Frameworks"
edition: "digital edition, 2024 (file revised April 2025)"
dates:
  published: 2024   # not printed; PDF metadata
  other: ["PDF created 5 February 2024", "PDF modified 28 April 2025"]
kind: model
jurisdiction: [UK]
authority: advisory
licence: "none stated in the file (D1)"
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the conditions for valid, reliable and learning-centred assessment and feedback across an institution, its course teams and its students' experience (D1, pp. 2-3)"
appliesTo:
  awards: [none-stated]
  levels: [none]
  providers: ["higher education institutions (as stated: \"institution-wide\")"]
whoMustUse: "no one must; offered to all stakeholders: educators, those in charge of policy, quality assurance and quality enhancement, and education leaders from pro vice-chancellors to programme leaders (D1, p. 3)"
howUsed: ["design", "review", "other: strategy, staff development, Fellowship evidence"]
doesNot: "none-stated"
beneficiary: the student
statedScope: "This framework is designed for all stakeholders; for educators, those in charge of policy, quality assurance and quality enhancement, and those responsible for leading education at all levels from pro vice-chancellors to programme leaders."
statedScopeLocator: "D1, p. 3"
statedScopeSpan: { start: 1316, end: 1555 }
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "what-is", order: 1, componentType: section, parent: "none", heading: "What is assessment?", gloss: "assessment as judgement and as learning; the sector context and the enhancement cycle", pages: "2", readFrom: "text layer" }
  - { number: "who-for", order: 2, componentType: section, parent: "none", heading: "Who is the framework for?", gloss: "audiences; widening access, awarding gaps and the call for clarity", pages: "3", readFrom: "text layer" }
  - { number: "why", order: 3, componentType: section, parent: "none", heading: "Why is enhancing assessment important?", gloss: "rationale: learning, satisfaction; authenticity, sustainability and inclusivity", pages: "4", readFrom: "text layer" }
  - { number: "structure", order: 4, componentType: figure, parent: "none", heading: "How is the framework structured?", gloss: "the three perspectives shared by the series", pages: "5", readFrom: "figure image" }
  - { number: "institution", order: 5, componentType: perspective, parent: "none", heading: "Institution", gloss: "framing prose for the institution: policy, technology, innovation and staff development", pages: "6", readFrom: "text layer" }
  - { number: "institution.dial", order: 6, componentType: figure, parent: "institution", heading: "(dial)", gloss: "sixteen segments in four quadrants; each quadrant's area of focus is named on the outer ring", pages: "7", readFrom: "figure image" }
  - { number: "educators", order: 7, componentType: perspective, parent: "none", heading: "Educators+", gloss: "framing prose for course teams: the four areas of focus, progression of unfamiliar tasks, varied methods", pages: "8", readFrom: "text layer" }
  - { number: "educators.dial", order: 8, componentType: figure, parent: "educators", heading: "(dial)", gloss: "four segments: the four areas of focus", pages: "9", readFrom: "figure image" }
  - { number: "students", order: 9, componentType: perspective, parent: "none", heading: "Students", gloss: "framing prose for students: assessment design, academic literacy, authentic tasks", pages: "10", readFrom: "text layer" }
  - { number: "students.dial", order: 10, componentType: figure, parent: "students", heading: "(dial)", gloss: "seven segments", pages: "11", readFrom: "figure image" }
  - { number: "use", order: 11, componentType: use-list, parent: "none", heading: "How can you use the framework?", gloss: "purpose and three uses for each perspective", pages: "12-13", readFrom: "figure image" }
  - { number: "psf", order: 12, componentType: section, parent: "none", heading: "How does this framework align with the Professional Standards Framework (PSF) 2023?", gloss: "the PSF table (six dimensions) and the Fellowship invitation", pages: "14", readFrom: "text layer" }
excluded:
  - { number: "photo", heading: "(photograph)", kind: "other: a full-page photograph with no text", pages: "15" }
  - { number: "back-cover", heading: "We help higher education organisations be the best they can be ...", kind: "other: the issuer's promotional back cover", pages: "16" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only obliging framing lines, requirement lists and use lists are statements (model template rule 3). -->
```yaml
- id: advancehe/assessment-2024/frame.valid-reliable
  locator: { number: "frame.valid-reliable", heading: "What is assessment?", page: 2 }
  span: { start: 213, end: 280 }
  source: "Assessment provides judgement so it needs to be valid and reliable."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "needs to" read as must
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["provides", "needs", "be"]
  about: "valid and reliable judgement"
  themes: ["none"]
  paraphrase: "Because assessment passes judgement, it has to measure what it claims to and do so dependably."
  audience: both
  subjects: inherited
- id: advancehe/assessment-2024/frame.designed-for-learning
  locator: { number: "frame.designed-for-learning", heading: "What is assessment?", page: 2 }
  span: { start: 281, end: 489 }
  source: "It also supports student learning and feedback, so it should be designed to promote desirable learning behaviours, develop subject-specific and professional competencies, as well as other graduate attributes."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # modal "should"
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["supports", "designed", "promote", "develop"]
  about: "assessment designed to drive learning"
  themes: ["none"]
  paraphrase: "Because assessment also drives learning, it should be designed to encourage good study habits and to build subject, professional and wider graduate capabilities."
  audience: both
  subjects: inherited
- id: advancehe/assessment-2024/frame.dialogue
  locator: { number: "frame.dialogue", heading: "What is assessment?", page: 2 }
  span: { start: 1051, end: 1189 }
  source: "It requires dialogue between academic and professional services staff, students and employers to inform curriculum review and development."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "requires" read as must; the subject is the process of enhancing assessment
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["requires", "inform"]
  about: "dialogue among staff, students and employers"
  themes: ["none"]
  paraphrase: "Improving assessment requires academic staff, professional services staff, students and employers to talk to each other to inform curriculum review."
  audience: practitioner
  subjects: inherited
- id: advancehe/assessment-2024/frame.clarity-gaps
  locator: { number: "frame.clarity-gaps", heading: "Who is the framework for?", page: 3 }
  span: { start: 1834, end: 1973 }
  source: "Clear learning outcomes, assessment criteria and constructive feedback are essential to address these gaps and promote inclusive education."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "essential" read as must
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["are", "address", "promote"]
  about: "clarity to close awarding gaps"
  themes: ["none"]
  paraphrase: "Clear outcomes, clear criteria and constructive feedback are required if awarding gaps are to close and education is to be inclusive."
  audience: both
  subjects: inherited
- id: advancehe/assessment-2024/frame.institution
  locator: { number: "frame.institution", heading: "Institution", page: 6 }
  span: { start: 3847, end: 4008 }
  source: "The strategies, policies and practices of the provider should actively support and enhance assessment practices and facilitate curriculum review and development."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: expectation
  force: should   # modal "should"
  level: none
  perspective: perspective:institution
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["support", "enhance", "facilitate"]
  about: "institutional support for assessment"
  themes: ["none"]
  paraphrase: "The institution's strategy, policy and practice should actively back better assessment and make curriculum review easier."
  audience: practitioner
  subjects: inherited
- id: advancehe/assessment-2024/frame.educators.policy
  locator: { number: "frame.educators.policy", heading: "Educators+", page: 8 }
  span: { start: 4395, end: 4507 }
  source: "Educators need to work within the institutional systems, processes and policies and apply them to their context."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "need to" read as must
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["need", "work", "apply"]
  about: "working within and applying policy"
  themes: ["none"]
  paraphrase: "Educators have to work inside the institution's rules, systems and processes and fit them to their own setting."
  audience: practitioner
  subjects: inherited
- id: advancehe/assessment-2024/frame.educators.progress
  locator: { number: "frame.educators.progress", heading: "Educators+", page: 8 }
  span: { start: 4508, end: 4721 }
  source: "Activities such as self- and peerassessment, formative assessment and learning from feedback may not be familiar to all students, so it is essential to integrate and progress them throughout a programme or course."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "essential" read as must
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["integrate", "progress"]
  about: "introducing unfamiliar assessment over a course"
  themes: ["none"]
  paraphrase: "Because self and peer assessment, formative tasks and using feedback may be new to students, they must be built in and developed across a course."
  audience: both
  subjects: inherited
- id: advancehe/assessment-2024/frame.educators.support
  locator: { number: "frame.educators.support", heading: "Educators+", page: 8 }
  span: { start: 4962, end: 5053 }
  source: "Educators require subject-specific developmental support to stay current in this landscape."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "require" read as must; it states a need of educators that falls on whoever develops them
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["require", "stay"]
  about: "subject-specific support for staff"
  themes: ["none"]
  paraphrase: "Educators need development support specific to their subject in order to keep up with changing assessment practice."
  audience: practitioner
  subjects: inherited
- id: advancehe/assessment-2024/use.institution.1
  locator: { number: "use.institution.1", heading: "How can you use the framework?", page: 12 }
  span: { start: 6540, end: 6640 }
  source: "Develop strategic priorities and enhance culture through shared ownership of policies and processes."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["Develop", "enhance"]
  about: "strategy and shared ownership"
  themes: ["none"]
  paraphrase: "Institutions should use the model to set strategic priorities and build a culture in which policies and processes are owned by many."
  audience: practitioner
  subjects: inherited
- id: advancehe/assessment-2024/use.institution.2
  locator: { number: "use.institution.2", heading: "How can you use the framework?", page: 12 }
  span: { start: 6655, end: 6748 }
  source: "Encourage a shared vision and values; providing creative and innovative assessment practices."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["Encourage", "providing"]
  about: "shared vision and innovative practice"
  themes: ["none"]
  paraphrase: "Institutions should foster a common vision and values for assessment and make room for creative, innovative practice."
  audience: practitioner
  subjects: inherited
- id: advancehe/assessment-2024/use.institution.3
  locator: { number: "use.institution.3", heading: "How can you use the framework?", page: 12 }
  span: { start: 6749, end: 6842 }
  source: "Foster and develop the relationship between institutions, external and internal stakeholders."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: should   # imperative read as should (proposed; Part E)
  level: none
  perspective: perspective:institution
  mood: imperative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["Foster", "develop"]
  about: "relationships with stakeholders"
  themes: ["none"]
  paraphrase: "Institutions should build relationships with stakeholders inside and outside the institution."
  audience: practitioner
  subjects: inherited
- id: advancehe/assessment-2024/use.educators.1
  locator: { number: "use.educators.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 6355, end: 6423 }
  source: "Acts as a benchmark to map against and/or consider current practice."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # function line: says what the model does for educators, without obliging
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["Acts", "map", "consider"]
  about: "a reference to map practice against"
  themes: ["none"]
  paraphrase: "For educators, the model serves as a reference point for mapping and reviewing current practice."
  audience: practitioner
  subjects: inherited
- id: advancehe/assessment-2024/use.educators.2
  locator: { number: "use.educators.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 6848, end: 6982 }
  source: "Develops collaborative engagement and can be used to develop inter- and intra-disciplinary working, and/or with external stakeholders."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # function line: says what the model does for educators, without obliging; "can" is possibility
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["Develops", "used", "develop"]
  about: "collaboration within and across disciplines"
  themes: ["none"]
  paraphrase: "For educators, the model supports collaboration within and across disciplines and with external partners."
  audience: practitioner
  subjects: inherited
- id: advancehe/assessment-2024/use.educators.3
  locator: { number: "use.educators.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 6437, end: 6538 }
  source: "Provides a resource that can identify and recognise professional development, needs and requirements."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # function line: says what the model does for educators, without obliging
  level: none
  perspective: perspective:educators
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: provider
  verbs: ["Provides", "identify", "recognise"]
  about: "identifying development needs"
  themes: ["none"]
  paraphrase: "For educators, the model helps identify and recognise development needs and requirements."
  audience: practitioner
  subjects: inherited
- id: advancehe/assessment-2024/use.students.1
  locator: { number: "use.students.1", heading: "How can you use the framework?", page: 13 }
  span: { start: 6984, end: 7100 }
  source: "Offers a structure for identifying key elements that can positively impact on a learner’s experience and attainment."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # function line: says what the model offers on the students' side, without obliging
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: both
  verbs: ["Offers", "identifying", "impact"]
  about: "elements that affect experience and attainment"
  themes: ["none"]
  paraphrase: "On the students' side, the model gives a structure for finding what most improves a learner's experience and results."
  audience: both
  subjects: inherited
- id: advancehe/assessment-2024/use.students.2
  locator: { number: "use.students.2", heading: "How can you use the framework?", page: 13 }
  span: { start: 7112, end: 7228 }
  source: "Identifies core components to help develop a shared and common understanding of assessment practices and literacies."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # function line: says what the model offers on the students' side, without obliging
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: both
  verbs: ["Identifies", "help", "develop"]
  about: "shared understanding of assessment"
  themes: ["none"]
  paraphrase: "On the students' side, the model names core parts that help staff and students reach a common understanding of assessment."
  audience: both
  subjects: inherited
- id: advancehe/assessment-2024/use.students.3
  locator: { number: "use.students.3", heading: "How can you use the framework?", page: 13 }
  span: { start: 7229, end: 7380 }
  source: "Allows for contextual understanding and recognises that areas will be under varying degrees of focus through different learning experiences and stages."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: guidance
  force: describes   # function line: says what the model allows, without obliging; "will" is prediction
  level: none
  perspective: perspective:students
  mood: declarative
  readFrom: "text layer"
  appliesTo: "framework for enhancing assessment"
  addressee: both
  verbs: ["Allows", "recognises"]
  about: "focus varies by stage and context"
  themes: ["none"]
  paraphrase: "On the students' side, the model allows for context and accepts that different elements matter more at different stages."
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- statement: advancehe/assessment-2024/frame.valid-reliable
  forPractitioner: { text: "Check that each task measures the outcome it claims to and that its marking would come out the same in other hands.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "You should be able to trust that a task tests what it says it tests, and that your mark would be the same from another marker.", rewrite: full, force: must, status: drafted }
  author-agent-written: "The framing requirement on assessment as judgement, force must from \"needs to\". Set it beside consistent standards and calibration on the Institution dial."
  author-agent-dialogue: "Raise it when a task's purpose is unclear. Ask: \"What does this task actually measure?\" and \"Would another marker reach the same mark?\" Avoid technical psychometric language unless asked."
- statement: advancehe/assessment-2024/frame.designed-for-learning
  forPractitioner: { text: "Design each task so that preparing for it builds the habits and capabilities you want students to leave with.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "Your assessments should help you build good study habits and the abilities you will need in your field and beyond.", rewrite: full, force: should, status: drafted }
  author-agent-written: "The framing expectation on assessment for learning, force should. Link it to showcasing competencies and to authentic challenges."
  author-agent-dialogue: "Raise it when a task rewards cramming or recall. Ask: \"What does preparing for this task teach students to do?\" Avoid dismissing exams as such."
- statement: advancehe/assessment-2024/frame.dialogue
  forPractitioner: { text: "Bring academic and professional services colleagues, students and employers into the review of assessment, and let what they say shape the curriculum.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on how the institution reviews assessment, though students take part", rewrite: full, force: must, status: drafted }
  author-agent-written: "A framing requirement on the enhancement process, force must from \"requires\". Link it to co-creation of criteria and to students contributing to assessment design."
  author-agent-dialogue: "Raise it in curriculum review. Ask: \"Who has been part of this review, and who is missing?\" Avoid implying employers set academic standards."
- statement: advancehe/assessment-2024/frame.clarity-gaps
  forPractitioner: { text: "Make outcomes, criteria and feedback clear to every student, as a direct means of narrowing awarding gaps.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "You should be told clearly what you are meant to learn, how it will be judged and how to improve.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Force must from \"essential\". The source ties clarity to awarding gaps arising from a more diverse student body; keep that reason. Link it to rubrics and criteria and to understanding criteria."
  author-agent-dialogue: "Raise it when gaps in attainment between groups are discussed. Ask: \"How clear are the outcomes, criteria and feedback to students who are new to these conventions?\" Avoid treating gaps as deficits in students."
- statement: advancehe/assessment-2024/frame.institution
  forPractitioner: { text: "Check that strategy, policy and regulations actively support better assessment and curriculum review, including room for new technology.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to the institution", rewrite: full, force: should, status: drafted }
  author-agent-written: "The framing expectation of the institution perspective, force should. The next sentence names adapting regulations and using technology; link to the anonymous-feedback and timely-feedback segments."
  author-agent-dialogue: "Raise it when a regulation blocks a better assessment practice. Ask: \"Which policy stands in the way, and who can change it?\" Avoid assuming policy can change quickly."
- statement: advancehe/assessment-2024/frame.educators.policy
  forPractitioner: { text: "Work within the institution's assessment rules and systems, and interpret them for your subject and students.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to staff", rewrite: full, force: must, status: drafted }
  author-agent-written: "Force must from \"need to\". Note it pairs compliance with application to context. Link it to the Systems, Processes and Policy area."
  author-agent-dialogue: "Raise it when a teacher plans a change without checking policy. Ask: \"What does policy allow here?\" Avoid presenting policy as a reason to do nothing."
- statement: advancehe/assessment-2024/frame.educators.progress
  forPractitioner: { text: "Introduce self and peer assessment, formative tasks and the use of feedback early, and develop them through the course.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "You should be introduced gradually to unfamiliar kinds of assessment, such as judging your own work, rather than meeting them cold.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Force must from \"essential\". Keep the reason: unfamiliarity. Link it to scaffolding, peer-assessment support and acting on feedback."
  author-agent-dialogue: "Raise it when students struggle with self or peer assessment. Ask: \"Where were students first taught to do this?\" Avoid assuming prior experience."
- statement: advancehe/assessment-2024/frame.educators.support
  forPractitioner: { text: "Provide, and seek, development on assessment that is specific to the subject, not only general.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: concerns staff development", rewrite: full, force: must, status: drafted }
  author-agent-written: "Force must from \"require\", our reading: the line states a need, and the duty falls on the institution. Link it to the Staff Development area."
  author-agent-dialogue: "Raise it when staff are asked to adopt new methods without support. Ask: \"What development in your subject would help?\" Avoid implying staff are at fault."
- statement: advancehe/assessment-2024/use.institution.1
  forPractitioner: { text: "Use the model in strategy work, and share ownership of assessment policy and process across staff and students.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "One of three institutional uses; force should (imperative, our reading)."
  author-agent-dialogue: "Raise it in strategy planning. Ask: \"Who owns our assessment policies, and who should share that ownership?\""
- statement: advancehe/assessment-2024/use.institution.2
  forPractitioner: { text: "Agree a shared vision for assessment and back staff who try creative and innovative methods.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). The issuer's grammar mixes an imperative and a gerund; recorded as imperative. Link it to the Innovative Assessment area."
  author-agent-dialogue: "Raise it when innovation lacks institutional backing. Ask: \"What vision of assessment do we share, and does it allow new methods?\""
- statement: advancehe/assessment-2024/use.institution.3
  forPractitioner: { text: "Build working relationships on assessment with students, colleagues across services and external partners such as employers.", rewrite: full, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: addressed to institutions", rewrite: full, force: should, status: drafted }
  author-agent-written: "Force should (imperative, our reading). Link it to the requirement for dialogue with staff, students and employers."
  author-agent-dialogue: "Raise it when assessment review is internal only. Ask: \"Which outside stakeholders could inform this?\""
- statement: advancehe/assessment-2024/use.educators.1
  forPractitioner: { text: "Map your current assessment practice against the model's segments to see what is in place and what is missing.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use for staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line; force describes. The issuer calls it a benchmark, but the model sets no level: do not present it as a threshold."
  author-agent-dialogue: "Raise it at course review. Ask: \"Which segments does our current practice cover, and which not?\""
- statement: advancehe/assessment-2024/use.educators.2
  forPractitioner: { text: "Use the model as common ground when working on assessment with colleagues in and beyond your discipline and with external partners.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use for staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line; force describes. Link it to the team-based approach the source names."
  author-agent-dialogue: "Raise it when a team plans assessment alone. Ask: \"Who else could you work with on this?\""
- statement: advancehe/assessment-2024/use.educators.3
  forPractitioner: { text: "Use the model to identify what development you need in assessment, and to recognise development you have done.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a use for staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line; force describes. Link it to the Staff Development area and to the PSF crosswalk."
  author-agent-dialogue: "Raise it in appraisal or Fellowship planning. Ask: \"Which segment is your next area for development?\""
- statement: advancehe/assessment-2024/use.students.1
  forPractitioner: { text: "Use the students' segments to identify which elements most affect your students' experience and attainment.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can use these elements to see what most helps your own experience and results in assessment.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line; force describes. Keep attainment and experience together, as the source does."
  author-agent-dialogue: "Raise it in tutorials. Ask: \"Which of these elements would make the biggest difference to you?\""
- statement: advancehe/assessment-2024/use.students.2
  forPractitioner: { text: "Use the students' segments to build a shared language about assessment with your students.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can use these elements to build a shared understanding of assessment with the people who teach you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line; force describes. Link it to assessment literacy and to understanding criteria."
  author-agent-dialogue: "Raise it when staff and students talk past each other about assessment. Ask: \"What do we each mean by this term?\""
- statement: advancehe/assessment-2024/use.students.3
  forPractitioner: { text: "Expect different segments to matter more at different stages, and adjust emphasis accordingly.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Different parts of assessment will matter more to you at different stages of your course, and that is expected.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line; force describes. Do not suggest every segment must be in focus at once."
  author-agent-dialogue: "Raise it when someone treats the segments as a checklist. Ask: \"Which of these matters most at this stage?\""
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
- { id: theme:assessment, role: carries, carriedIn: ["what-is", "who-for", "why", "institution", "educators", "students", "use", "psf"], basis: "stated: assessment and feedback are the model's whole subject" }
- { id: theme:edi, role: carries, carriedIn: ["who-for", "why", "educators"], basis: "inferred: the text names inclusive education, inclusivity and awarding gaps but not EDI as such (Part E)" }
- { id: theme:access-retention-attainment-progression, role: carries, carriedIn: ["who-for", "use"], basis: "inferred: the text names widening access, awarding gaps and attainment (Part E)" }
- { id: theme:digital, role: carries, carriedIn: ["institution", "institution.dial"], basis: "inferred: the text names new technologies and technology for the assessment cycle and feedback (Part E)" }
- { id: theme:employability, role: carries, carriedIn: ["what-is", "students.dial"], basis: "inferred: the text names employers, professional competencies and graduate attributes (Part E)" }
- { id: theme:student-partnership, role: carries, carriedIn: ["what-is", "institution.dial", "students.dial"], basis: "inferred: the text calls for dialogue with students; the figures name co-creation and student contribution to design (Part E)" }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: partOf, target: "advancehe-student-success-frameworks-2024", note: "Advance HE Student Success Frameworks; the three-perspective structure is shared by the series (D1, p. 5)" }
- { rel: alignsWith, target: "std:doc:advancehe-psf-dimensions-2023-framework", note: "stated: particularly relevant to V1, V3, A1, A3, K2 and K5 of the PSF 2023 (M5)" }
- { rel: partOf, target: "std:doc:advancehe-enhancing-student-success-2024-model", note: "the series overview names assessment as one of its areas" }
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
  - { id: perspective:educators, label: "Educators+", page: 9, segments: 4, openSegments: 0, note: "labelled \"Educators+\" in the structure figure (p. 5), on p. 8 and in the use list (p. 13)" }
  - { id: perspective:students, label: "Students", page: 11, segments: 7, openSegments: 0 }
groups:
  - { id: category:embedded-in-the-curriculum, kind: category, label: "Embedded in the Curriculum", axis: all, ring: inner, segments: 5, perAxis: {"perspective:institution": 4, "perspective:educators": 1}, readFrom: "text layer (p. 9); outer-ring arc label on the figure image (p. 7)" }
  - { id: category:systems-processes-and-policy, kind: category, label: "Systems, Processes and Policy", axis: all, ring: inner, segments: 5, perAxis: {"perspective:institution": 4, "perspective:educators": 1}, readFrom: "text layer (p. 9); outer-ring arc label on the figure image (p. 7)" }
  - { id: category:innovative-assessment, kind: category, label: "Innovative Assessment", axis: all, ring: inner, segments: 5, perAxis: {"perspective:institution": 4, "perspective:educators": 1}, readFrom: "text layer (p. 9); outer-ring arc label on the figure image (p. 7)" }
  - { id: category:staff-development, kind: category, label: "Staff Development", axis: all, ring: inner, segments: 5, perAxis: {"perspective:institution": 4, "perspective:educators": 1}, readFrom: "text layer (p. 9); outer-ring arc label on the figure image (p. 7)" }
use: "to keep the student experience, fitting pedagogy and a strategic view of assessment in focus, using the three perspectives alone or together to find where institutional policy and practice meet; each perspective has three uses (S4 use.*) (D1, pp. 12-13)"
```

### M2 Components
<!-- label: both; status: drafted; basis: primary. In the figure's order (Part E). -->
```yaml
- id: advancehe/assessment-2024/institution.co-creation-of-criteria
  label: "Co-creation of Criteria"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:embedded-in-the-curriculum, order: 1, page: 7 }
  explainedBy:
    - { span: { start: 1834, end: 1973 }, source: "Clear learning outcomes, assessment criteria and constructive feedback are essential to address these gaps and promote inclusive education.", link: inferred, page: 3 }
    - { span: { start: 1051, end: 1189 }, source: "It requires dialogue between academic and professional services staff, students and employers to inform curriculum review and development.", link: inferred, page: 2 }
  conditionType: practice
  actor: all
  about: "students helping to write criteria"
  paraphrase: "Students and staff draw up assessment criteria together, so that students share ownership of the standard they are judged by."
  themes: ["theme:student-voice-partnership", "theme:assessment-literacy", "theme:assessment", "theme:student-partnership"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.peer-assessment-training
  label: "Support and Training for Peer Assessment and Feedback"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:embedded-in-the-curriculum, order: 2, page: 7 }
  explainedBy:
    - { span: { start: 4508, end: 4721 }, source: "Activities such as self- and peerassessment, formative assessment and learning from feedback may not be familiar to all students, so it is essential to integrate and progress them throughout a programme or course.", link: stated, page: 8 }
  conditionType: service
  actor: institution
  about: "preparing students to judge peers' work"
  paraphrase: "Students are taught and supported to assess one another's work and to give useful feedback, rather than being left to do it unprepared."
  themes: ["theme:feedback-dialogue", "theme:assessment-literacy", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.rubrics-and-criteria
  label: "Rubrics and Assessment Criteria"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:embedded-in-the-curriculum, order: 3, page: 7 }
  explainedBy:
    - { span: { start: 1834, end: 1973 }, source: "Clear learning outcomes, assessment criteria and constructive feedback are essential to address these gaps and promote inclusive education.", link: stated, page: 3 }
  conditionType: practice
  actor: educator
  about: "clear rubrics and criteria for tasks"
  paraphrase: "Each task has clear criteria, set out in a rubric where useful, so that students can see what is being judged and how."
  themes: ["theme:assessment-literacy", "theme:assessment", "theme:edi"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.anonymous-feedback-technology
  label: "Technology to Support Anonymous Feedback"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:embedded-in-the-curriculum, order: 4, page: 7 }
  explainedBy:
    - { span: { start: 4009, end: 4175 }, source: "This includes adapting regulations to accommodate new technologies, utilise technology for managing the assessment cycle and delivering timely, constructive feedback.", link: stated, page: 6 }
  conditionType: structure
  actor: institution
  about: "tools that let feedback be anonymous"
  paraphrase: "The institution provides digital tools that let students give feedback, on peers' work or on teaching, without being named."
  themes: ["theme:feedback-dialogue", "theme:psychological-safety", "theme:assessment", "theme:digital"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.consistent-standards
  label: "Consistent Standards and Assessment Criteria"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:systems-processes-and-policy, order: 5, page: 7 }
  explainedBy:
    - { span: { start: 213, end: 280 }, source: "Assessment provides judgement so it needs to be valid and reliable.", link: inferred, page: 2 }
    - { span: { start: 1190, end: 1314 }, source: "Continuous enhancement of assessment positively impacts student learning, satisfaction and confidence in academic standards.", link: inferred, page: 2 }
  conditionType: structure
  actor: institution
  about: "the same standards applied across courses"
  paraphrase: "Standards and criteria are applied in the same way across modules and markers, so that a grade means the same wherever it is earned."
  themes: ["theme:consistent-judgement", "theme:assessment-literacy", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.program-level-rubrics
  label: "Program Level Rubrics"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:systems-processes-and-policy, order: 6, page: 7 }
  explainedBy:
    - { span: { start: 1556, end: 1641 }, source: "It’s most effective when implemented institution-wide and integrated into programmes.", link: inferred, page: 3 }
  conditionType: structure
  actor: institution
  about: "rubrics shared across a programme"
  paraphrase: "A programme uses rubrics that run across its modules, so that criteria build from one stage to the next."
  themes: ["theme:programmatic-assessment", "theme:consistent-judgement", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.equitable-group-work
  label: "Equitable Assessment Processes for Group Work"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:systems-processes-and-policy, order: 7, page: 7 }
  explainedBy:
    - { span: { start: 967, end: 1050 }, source: "This has implications for the institution’s infrastructure, policies and practices.", link: inferred, page: 2 }
  conditionType: process
  actor: institution
  about: "fair marking of group work"
  paraphrase: "Group work is assessed through processes that treat each member fairly and recognise individual contribution."
  themes: ["theme:consistent-judgement", "theme:collaboration", "theme:assessment", "theme:edi"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.calibration-academic-standards
  label: "Calibration of Academic Standards"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:systems-processes-and-policy, order: 8, page: 7 }
  explainedBy:
    - { span: { start: 1190, end: 1314 }, source: "Continuous enhancement of assessment positively impacts student learning, satisfaction and confidence in academic standards.", link: stated, page: 2 }
  conditionType: process
  actor: educator
  about: "markers aligning their judgements"
  paraphrase: "Markers compare their judgements on shared work and adjust them, so that academic standards hold across people and over time."
  themes: ["theme:consistent-judgement", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.inclusive-assessment-range
  label: "Diverse Range of Inclusive Assessment Instruments"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:innovative-assessment, order: 9, page: 7 }
  explainedBy:
    - { span: { start: 4722, end: 4805 }, source: "The framework encourages the adoption of diverse and innovative assessment methods.", link: stated, page: 8 }
    - { span: { start: 4806, end: 4961 }, source: "A team-based approach ensures students experience a broad range of assessment methods, enhancing the validity, authenticity and inclusivity of assessments.", link: stated, page: 8 }
  conditionType: practice
  actor: educator
  about: "varied and inclusive assessment methods"
  paraphrase: "Courses use a varied set of assessment methods designed so that students with different strengths and needs can show what they have learned."
  themes: ["theme:anticipating-difference", "theme:real-world-learning", "theme:assessment", "theme:edi", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.scaffolding-complexity
  label: "Scaffolding Complexity of Assessment Tasks"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:innovative-assessment, order: 10, page: 7 }
  explainedBy:
    - { span: { start: 4508, end: 4721 }, source: "Activities such as self- and peerassessment, formative assessment and learning from feedback may not be familiar to all students, so it is essential to integrate and progress them throughout a programme or course.", link: inferred, page: 8 }
  conditionType: practice
  actor: educator
  about: "building task difficulty step by step"
  paraphrase: "Assessment tasks grow in complexity in planned steps, with support that is reduced as students gain competence."
  themes: ["theme:programmatic-assessment", "theme:transition", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.formative-summative-balance
  label: "Balance of Formative and Summative Assessment"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:innovative-assessment, order: 11, page: 7 }
  explainedBy:
    - { span: { start: 5348, end: 5493 }, source: "This includes peerand self-assessment, and formative and summative assessments, all of which foster academic literacy and good academic practice.", link: stated, page: 10 }
  conditionType: practice
  actor: educator
  about: "enough practice before marks count"
  paraphrase: "Courses give students enough formative assessment, with feedback, alongside summative tasks that count towards their marks."
  themes: ["theme:programmatic-assessment", "theme:feedback-dialogue", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.holistic-programmatic-approach
  label: "Holistic Programmatic Approach to Assessment"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:innovative-assessment, order: 12, page: 7 }
  explainedBy:
    - { span: { start: 4304, end: 4394 }, source: "The framework promotes a holistic approach by course teams across the four areas of focus.", link: stated, page: 8 }
    - { span: { start: 1556, end: 1641 }, source: "It’s most effective when implemented institution-wide and integrated into programmes.", link: inferred, page: 3 }
  conditionType: structure
  actor: educator
  about: "assessment planned across a whole programme"
  paraphrase: "Assessment is planned across the whole programme by its team, not module by module, so that tasks connect and build."
  themes: ["theme:programmatic-assessment", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.dialogic-feedback
  label: "Ongoing Dialogic Feedback & Feedforward Processes"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:staff-development, order: 13, page: 7 }
  explainedBy:
    - { span: { start: 281, end: 489 }, source: "It also supports student learning and feedback, so it should be designed to promote desirable learning behaviours, develop subject-specific and professional competencies, as well as other graduate attributes.", link: inferred, page: 2 }
    - { span: { start: 5494, end: 5682 }, source: "These interconnected factors not only enhance students’ understanding and trust in assessment, but also involve them in authentic tasks that improve both assessment and feedback practices.", link: inferred, page: 10 }
  conditionType: process
  actor: educator
  about: "feedback as two-way, forward-looking talk"
  paraphrase: "Feedback is an ongoing exchange between staff and students that looks ahead to the next piece of work, not a one-off verdict on the last."
  themes: ["theme:feedback-dialogue", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.aligned-to-criteria
  label: "Aligned to Criteria and Standards"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:staff-development, order: 14, page: 7 }
  explainedBy:
    - { span: { start: 1834, end: 1973 }, source: "Clear learning outcomes, assessment criteria and constructive feedback are essential to address these gaps and promote inclusive education.", link: inferred, page: 3 }
  conditionType: practice
  actor: educator
  about: "feedback tied to the criteria"
  paraphrase: "Feedback refers to the published criteria and standards, so that students can see how their work was judged."
  themes: ["theme:assessment-literacy", "theme:feedback-dialogue", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.timely-actionable-feedback
  label: "Timely and Actionable Feedback"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:staff-development, order: 15, page: 7 }
  explainedBy:
    - { span: { start: 4009, end: 4175 }, source: "This includes adapting regulations to accommodate new technologies, utilise technology for managing the assessment cycle and delivering timely, constructive feedback.", link: stated, page: 6 }
  conditionType: practice
  actor: educator
  about: "feedback in time to use"
  paraphrase: "Feedback comes back while it can still be used and says what to do, not only what was wrong."
  themes: ["theme:feedback-dialogue", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/institution.range-of-places-and-formats
  label: "Available in a Range of Places and Formats"
  span: none   # figure image, p. 7
  position: { axis: perspective:institution, group: category:staff-development, order: 16, page: 7 }
  explainedBy:
    - { span: { start: 3644, end: 3837 }, source: "The institution plays a crucial role in promoting and disseminating innovative assessment practices, while ensuring that appropriate staff development opportunities are available for all staff.", link: inferred, page: 6 }
  conditionType: service
  actor: institution
  about: "development offered in varied forms"
  paraphrase: "Development for staff on assessment is offered in a range of places and formats, so that every member of staff can take part."
  themes: ["theme:professional-learning", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/educators.embedded-in-the-curriculum
  label: "Embedded in the Curriculum"
  span: { start: 5077, end: 5103 }
  position: { axis: perspective:educators, group: category:embedded-in-the-curriculum, order: 1, page: 9 }
  explainedBy:
    - { span: { start: 4508, end: 4721 }, source: "Activities such as self- and peerassessment, formative assessment and learning from feedback may not be familiar to all students, so it is essential to integrate and progress them throughout a programme or course.", link: inferred, page: 8 }
    - { span: { start: 4304, end: 4394 }, source: "The framework promotes a holistic approach by course teams across the four areas of focus.", link: inferred, page: 8 }
  conditionType: practice
  actor: educator
  about: "assessment built into course design"
  paraphrase: "Assessment practices are part of how a course is designed and taught, introduced and developed through it, not added at the end."
  themes: ["theme:programmatic-assessment", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/educators.systems-processes-and-policy
  label: "Systems, Processes and Policy"
  span: { start: 5128, end: 5157 }
  position: { axis: perspective:educators, group: category:systems-processes-and-policy, order: 2, page: 9 }
  explainedBy:
    - { span: { start: 4395, end: 4507 }, source: "Educators need to work within the institutional systems, processes and policies and apply them to their context.", link: stated, page: 8 }
    - { span: { start: 3847, end: 4008 }, source: "The strategies, policies and practices of the provider should actively support and enhance assessment practices and facilitate curriculum review and development.", link: inferred, page: 6 }
  conditionType: structure
  actor: all
  about: "working within institutional rules"
  paraphrase: "Course teams work within the institution's assessment systems, processes and policies and apply them sensibly to their own setting."
  themes: ["theme:contextual-adaptation", "theme:consistent-judgement", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/educators.innovative-assessment
  label: "Innovative Assessment"
  span: { start: 5105, end: 5126 }
  position: { axis: perspective:educators, group: category:innovative-assessment, order: 3, page: 9 }
  explainedBy:
    - { span: { start: 4722, end: 4805 }, source: "The framework encourages the adoption of diverse and innovative assessment methods.", link: stated, page: 8 }
    - { span: { start: 3644, end: 3837 }, source: "The institution plays a crucial role in promoting and disseminating innovative assessment practices, while ensuring that appropriate staff development opportunities are available for all staff.", link: stated, page: 6 }
  conditionType: practice
  actor: educator
  about: "trying new assessment methods"
  paraphrase: "Course teams adopt new and varied assessment methods where they improve validity, authenticity or inclusivity."
  themes: ["theme:real-world-learning", "theme:anticipating-difference", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/educators.staff-development
  label: "Staff Development"
  span: { start: 5058, end: 5075 }
  position: { axis: perspective:educators, group: category:staff-development, order: 4, page: 9 }
  explainedBy:
    - { span: { start: 3644, end: 3837 }, source: "The institution plays a crucial role in promoting and disseminating innovative assessment practices, while ensuring that appropriate staff development opportunities are available for all staff.", link: stated, page: 6 }
    - { span: { start: 4962, end: 5053 }, source: "Educators require subject-specific developmental support to stay current in this landscape.", link: stated, page: 8 }
  conditionType: service
  actor: institution
  about: "keeping staff current on assessment"
  paraphrase: "Staff receive subject-specific development that keeps their assessment and feedback practice current."
  themes: ["theme:professional-learning", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/students.showcase-competencies
  label: "Showcase Competencies"
  span: { start: 5717, end: 5738 }
  position: { axis: perspective:students, group: none, order: 1, page: 11 }
  explainedBy:
    - { span: { start: 281, end: 489 }, source: "It also supports student learning and feedback, so it should be designed to promote desirable learning behaviours, develop subject-specific and professional competencies, as well as other graduate attributes.", link: stated, page: 2 }
  conditionType: practice
  actor: student
  about: "showing what one can do"
  paraphrase: "Students have the chance, through assessment, to show the subject and professional competencies they have built."
  themes: ["theme:real-world-learning", "theme:assessment", "theme:employability"]
  sameLabelAs: none
- id: advancehe/assessment-2024/students.understand-assessment-criteria
  label: "Understand Assessment Criteria"
  span: { start: 5771, end: 5801 }
  position: { axis: perspective:students, group: none, order: 2, page: 11 }
  explainedBy:
    - { span: { start: 5494, end: 5682 }, source: "These interconnected factors not only enhance students’ understanding and trust in assessment, but also involve them in authentic tasks that improve both assessment and feedback practices.", link: inferred, page: 10 }
    - { span: { start: 1834, end: 1973 }, source: "Clear learning outcomes, assessment criteria and constructive feedback are essential to address these gaps and promote inclusive education.", link: inferred, page: 3 }
  conditionType: disposition
  actor: student
  about: "students grasping the criteria"
  paraphrase: "Students understand the criteria their work is judged by, and so can aim at them and trust the result."
  themes: ["theme:assessment-literacy", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/students.give-and-receive-feedback
  label: "Give and Receive Feedback"
  span: { start: 5843, end: 5868 }
  position: { axis: perspective:students, group: none, order: 3, page: 11 }
  explainedBy:
    - { span: { start: 5348, end: 5493 }, source: "This includes peerand self-assessment, and formative and summative assessments, all of which foster academic literacy and good academic practice.", link: inferred, page: 10 }
    - { span: { start: 4508, end: 4721 }, source: "Activities such as self- and peerassessment, formative assessment and learning from feedback may not be familiar to all students, so it is essential to integrate and progress them throughout a programme or course.", link: inferred, page: 8 }
  conditionType: practice
  actor: student
  about: "students as givers and receivers of feedback"
  paraphrase: "Students both give feedback to others and receive it, learning from each side of the exchange."
  themes: ["theme:feedback-dialogue", "theme:collaboration", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/students.contribution-to-group-work
  label: "Contribution to Group Work"
  span: { start: 5870, end: 5896 }
  position: { axis: perspective:students, group: none, order: 4, page: 11 }
  explainedBy:
    - { span: { start: 5494, end: 5682 }, source: "These interconnected factors not only enhance students’ understanding and trust in assessment, but also involve them in authentic tasks that improve both assessment and feedback practices.", link: inferred, page: 10 }
  conditionType: practice
  actor: student
  about: "each student's part in group work"
  paraphrase: "Students take an active and recognised part in group tasks and learn to work with others."
  themes: ["theme:collaboration", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/students.complex-authentic-challenges
  label: "Thrive on Complex Authentic Challenges"
  span: { start: 5803, end: 5841 }
  position: { axis: perspective:students, group: none, order: 5, page: 11 }
  explainedBy:
    - { span: { start: 5494, end: 5682 }, source: "These interconnected factors not only enhance students’ understanding and trust in assessment, but also involve them in authentic tasks that improve both assessment and feedback practices.", link: stated, page: 10 }
    - { span: { start: 2290, end: 2389 }, source: "It also facilitates the adoption of requirements like authenticity, sustainability and inclusivity.", link: inferred, page: 4 }
  conditionType: disposition
  actor: student
  about: "students taking on real, complex tasks"
  paraphrase: "Students take on demanding tasks that resemble real problems in their subject or profession and grow through them."
  themes: ["theme:real-world-learning", "theme:assessment", "theme:employability"]
  sameLabelAs: none
- id: advancehe/assessment-2024/students.act-on-feedback
  label: "Recognise and Act on Feedback"
  span: { start: 5740, end: 5769 }
  position: { axis: perspective:students, group: none, order: 6, page: 11 }
  explainedBy:
    - { span: { start: 4508, end: 4721 }, source: "Activities such as self- and peerassessment, formative assessment and learning from feedback may not be familiar to all students, so it is essential to integrate and progress them throughout a programme or course.", link: stated, page: 8 }
    - { span: { start: 5494, end: 5682 }, source: "These interconnected factors not only enhance students’ understanding and trust in assessment, but also involve them in authentic tasks that improve both assessment and feedback practices.", link: inferred, page: 10 }
  conditionType: disposition
  actor: student
  about: "students using the feedback they get"
  paraphrase: "Students recognise feedback in its many forms and act on it in their later work."
  themes: ["theme:feedback-dialogue", "theme:agency-self-actualisation", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/assessment-2024/students.contribute-to-assessment-design
  label: "Contribute to Assessment Design"
  span: { start: 5684, end: 5715 }
  position: { axis: perspective:students, group: none, order: 7, page: 11 }
  explainedBy:
    - { span: { start: 5246, end: 5347 }, source: "This student-centred framework aims to enhance learning potential through improved assessment design.", link: inferred, page: 10 }
    - { span: { start: 1051, end: 1189 }, source: "It requires dialogue between academic and professional services staff, students and employers to inform curriculum review and development.", link: inferred, page: 2 }
  conditionType: relationship
  actor: student
  about: "students shaping how they are assessed"
  paraphrase: "Students help design how they are assessed, and their views shape the tasks they take."
  themes: ["theme:student-voice-partnership", "theme:assessment", "theme:student-partnership"]
  sameLabelAs: none
```

### M2a Component audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- component: advancehe/assessment-2024/institution.co-creation-of-criteria
  forPractitioner: { text: "Work out the criteria for a task with your students, explain what each one rewards, and keep the parts that the subject fixes.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can help shape the criteria your work is marked against, so you know what they mean and why they matter.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a partnership practice in assessment design, read from the figure (the prose never names it). Do not imply students set their own grades or that every criterion is negotiable. Set it beside the students' segment on contributing to assessment design."
  author-agent-dialogue: "Raise it when criteria are handed down without explanation. Ask: \"Which of these criteria could students help word?\" and \"What would they understand better if they had?\" Avoid promising students control over standards."
- component: advancehe/assessment-2024/institution.peer-assessment-training
  forPractitioner: { text: "Teach students how to read work against criteria and how to word feedback, practise it with low stakes first, and support them as they do it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will be shown how to judge a classmate's work fairly and how to give feedback they can use, with practice before it counts.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as preparation for peer assessment, not peer assessment itself. Note that the source says such activities may be unfamiliar to students. Link it to the students' segment on giving and receiving feedback."
  author-agent-dialogue: "Raise it when peer review is set with no preparation. Ask: \"How will students learn to judge each other's work?\" and \"Where can they practise first?\" Avoid treating peer marking as a way to save staff time."
- component: advancehe/assessment-2024/institution.rubrics-and-criteria
  forPractitioner: { text: "Publish criteria and, where they help, rubrics with each task; write them plainly and use them in teaching, not only in marking.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can see the criteria for each task before you start, set out plainly, so you know what good work looks like.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present rubrics and criteria as tools for learning as well as judgement; the source ties clear criteria to closing awarding gaps and to inclusive education. Do not imply a rubric alone guarantees fair marking."
  author-agent-dialogue: "Raise it when students say they do not know what is wanted. Ask: \"Where are the criteria for this, and have you worked through them with an example?\" Avoid suggesting that more detail always helps; clarity matters more."
- component: advancehe/assessment-2024/institution.anonymous-feedback-technology
  forPractitioner: { text: "Provide and support tools that allow anonymous feedback where naming people would hold back honest comment, and show staff how to use them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can give honest feedback through tools that do not show your name, so you can say what you think without worry.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Read from the figure; the prose speaks of using technology across the assessment cycle and for feedback, not of anonymity. Present anonymity as a means to candour, not as a default for every exchange."
  author-agent-dialogue: "Raise it when students hold back in peer or course feedback. Ask: \"Would students say more if their names were not attached?\" Avoid suggesting anonymity replaces open dialogue."
- component: advancehe/assessment-2024/institution.consistent-standards
  forPractitioner: { text: "Set shared standards and criteria at institution or programme level, and check that markers and modules apply them alike.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect a grade to mean the same thing whichever module or marker gives it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present consistency as a condition of valid and reliable judgement, which the source names. Do not equate consistency with identical tasks; criteria can be shared while tasks differ."
  author-agent-dialogue: "Raise it when students report that marking varies from module to module. Ask: \"Which shared standard do these modules mark against?\" Avoid blaming individual markers before checking the system."
- component: advancehe/assessment-2024/institution.program-level-rubrics
  forPractitioner: { text: "Agree rubrics at programme level that modules adapt rather than replace, so that students meet familiar criteria that grow more demanding.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You meet the same kinds of criteria across your course, and they grow more demanding as you progress.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "The figure prints \"Program\" in US spelling; write \"programme\" in our prose. Present it as programme design, not as one rubric for every task."
  author-agent-dialogue: "Raise it in programme review. Ask: \"Do students see the same criteria grow across the years, or new ones in every module?\" Avoid imposing one rubric where tasks differ in kind."
- component: advancehe/assessment-2024/institution.equitable-group-work
  forPractitioner: { text: "Set rules for assessing group work that recognise individual contribution, deal with uneven effort and are applied the same way across modules.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "When you work in a group, you can expect your own contribution to be recognised and the marking to be fair to everyone.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Read from the figure; the prose does not discuss group work. Present equity here as fair process and recognition of contribution, not as equal marks for all. Set it beside the students' group-work segment."
  author-agent-dialogue: "Raise it when students fear being marked down by a group. Ask: \"How is each person's contribution recognised?\" and \"What happens if someone does not take part?\" Avoid suggesting group work should be avoided."
- component: advancehe/assessment-2024/institution.calibration-academic-standards
  forPractitioner: { text: "Hold regular calibration where markers grade the same samples, discuss differences and agree what each standard looks like.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can trust that the people marking your work have compared their judgements and agree on the standard.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present calibration as an ongoing shared practice among markers, distinct from moderation after the event. The source ties enhanced assessment to confidence in academic standards; keep that link."
  author-agent-dialogue: "Raise it when markers disagree or grades drift. Ask: \"When did the team last mark the same scripts and compare?\" Avoid treating one marker's view as the standard."
- component: advancehe/assessment-2024/institution.inclusive-assessment-range
  forPractitioner: { text: "Plan a mix of assessment methods across a course, and design each so that it tests the outcome rather than an unrelated skill or circumstance.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You will meet a range of assessment types, designed so that you can show what you know in more than one way.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present variety and inclusivity together, as the source does: a broad range is said to strengthen validity, authenticity and inclusivity. Do not present variety as novelty for its own sake. Set it beside the inclusive learning and teaching model."
  author-agent-dialogue: "Raise it when one method dominates a course. Ask: \"Which students does this method suit, and which does it disadvantage for reasons unrelated to the outcome?\" Avoid listing student groups as problems."
- component: advancehe/assessment-2024/institution.scaffolding-complexity
  forPractitioner: { text: "Sequence tasks so that each builds on the last, offer support early and withdraw it as students become able to work alone.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your assessments build step by step, with more support at the start and more independence as you go.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Read from the figure; the prose speaks of integrating and progressing unfamiliar activities through a course. Present scaffolding as planned progression with fading support, not as making tasks easier."
  author-agent-dialogue: "Raise it when a first-year task asks for skills not yet taught. Ask: \"What earlier task prepares students for this one?\" Avoid lowering the end standard."
- component: advancehe/assessment-2024/institution.formative-summative-balance
  forPractitioner: { text: "Plan formative opportunities before each summative task and make sure their feedback can be used in time.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You get chances to practise and receive feedback before the assessments that count towards your marks.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present the balance as a design choice across a course. Do not treat formative work as optional extra; the source names both kinds as fostering academic literacy."
  author-agent-dialogue: "Raise it when students meet a task for the first time when it counts. Ask: \"Where do students practise this before it is graded?\" Avoid adding formative tasks with no feedback."
- component: advancehe/assessment-2024/institution.holistic-programmatic-approach
  forPractitioner: { text: "Plan assessment as a programme team: map every task, remove clutter and overlap, and connect tasks so that they build towards the programme outcomes.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your assessments are planned as a whole across your course, so each one connects to what comes before and after.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as programme-level design by course teams, which the source names as its holistic approach. Do not present it as removing module autonomy entirely."
  author-agent-dialogue: "Raise it when students report bunched deadlines or repeated tasks. Ask: \"Has the team mapped assessment across the whole programme?\" Avoid recommending a full redesign where a map would show the gaps."
- component: advancehe/assessment-2024/institution.dialogic-feedback
  forPractitioner: { text: "Make feedback a conversation: invite students to respond and ask, and point each comment towards what to do next time.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Feedback on your work is a conversation you can join, and it tells you what to do next time as well as how you did.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Read from the figure, in the Staff Development quadrant; this reads it as feedback practice that staff are developed to offer (Part E). Present feedforward as advice for future work. Do not equate dialogue with more written comments."
  author-agent-dialogue: "Raise it when feedback is described as one-way. Ask: \"How do students respond to feedback, and what do they do with it next?\" Avoid implying staff must hold individual meetings with every student."
- component: advancehe/assessment-2024/institution.aligned-to-criteria
  forPractitioner: { text: "Write feedback that names the criteria and the standard reached, so that comments and marks clearly agree.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Feedback on your work tells you how it measured up against the criteria, so the comments and the mark make sense together.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Read from the figure; the label is a phrase, not a noun, and sits in the Staff Development quadrant beside two feedback segments, so it is read here as a quality of feedback (Part E). Say so if you rely on that reading."
  author-agent-dialogue: "Raise it when students cannot see why they got a mark. Ask: \"Which criteria does this comment speak to?\" Avoid reducing feedback to ticking rubric cells."
- component: advancehe/assessment-2024/institution.timely-actionable-feedback
  forPractitioner: { text: "Return feedback before the next related task and phrase it as actions the student can take.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You get feedback in time to use it, and it tells you what to do differently.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present timeliness relative to the next task, not a fixed number of days. The source names timely feedback under the institution's use of technology; link the two."
  author-agent-dialogue: "Raise it when feedback arrives after the next submission. Ask: \"When does feedback come back compared with the next task?\" and \"What can the student act on?\" Avoid promising turnaround times the institution has not set."
- component: advancehe/assessment-2024/institution.range-of-places-and-formats
  forPractitioner: { text: "Offer development on assessment in several formats and settings (online, in person, within teams, on demand) so that no group of staff is left out.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: concerns how staff development is offered; it bears on students only through better-prepared staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Read from the figure; the label has no noun. It sits in the Staff Development quadrant and is read here as describing staff development provision, which the prose says must be available to all staff (Part E). It may instead describe feedback; say so if the reading matters."
  author-agent-dialogue: "Raise it when development is offered in one form only. Ask: \"Which staff cannot reach this format, and what else could reach them?\" Avoid assuming online provision suits everyone."
- component: advancehe/assessment-2024/educators.embedded-in-the-curriculum
  forPractitioner: { text: "Build assessment and feedback activities into teaching from the start, and introduce unfamiliar ones gradually across the course.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Assessment is part of how your course is taught, and new kinds of task are introduced to you step by step.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the four areas of focus; on the Institution dial it heads co-creation, peer-assessment support, rubrics and anonymous-feedback technology. Do not treat it as a single practice."
  author-agent-dialogue: "Raise it when assessment is planned separately from teaching. Ask: \"Where in the teaching do students prepare for this task?\" Avoid prescribing a single design."
- component: advancehe/assessment-2024/educators.systems-processes-and-policy
  forPractitioner: { text: "Know the assessment regulations and systems that apply to you, and interpret them for your subject and students; raise those that do not fit.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect the rules about assessment to be applied in the same way to everyone and explained to you clearly.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "One of the four areas of focus; on the Institution dial it heads consistent standards, programme rubrics, equitable group-work processes and calibration. Present the educator's role as applying policy to context, not just complying."
  author-agent-dialogue: "Raise it when staff are unsure what policy allows. Ask: \"What does the regulation require here, and how does it apply to this course?\" Avoid giving legal or regulatory rulings."
- component: advancehe/assessment-2024/educators.innovative-assessment
  forPractitioner: { text: "Try new assessment methods where the current ones fall short, evaluate them, and share what works with colleagues.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You may meet new kinds of assessment designed to test what matters in your subject more fairly and realistically.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "One of the four areas of focus; on the Institution dial it heads inclusive variety, scaffolding, formative-summative balance and the programmatic approach. Present innovation as serving validity and inclusivity, not novelty."
  author-agent-dialogue: "Raise it when a method no longer fits its purpose. Ask: \"What would test this outcome more directly?\" and \"How will you know the new method works?\" Avoid recommending change for its own sake."
- component: advancehe/assessment-2024/educators.staff-development
  forPractitioner: { text: "Take part in development on assessment that fits your subject, and ask for it where it is missing.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: concerns the development of staff; it bears on students only through better-prepared staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "One of the four areas of focus; on the Institution dial it heads dialogic feedback, criteria-aligned feedback, timely feedback and availability in a range of formats. The source says educators need subject-specific support; keep that qualifier."
  author-agent-dialogue: "Raise it when staff feel unprepared for a new method. Ask: \"What development would help you assess this well in your subject?\" Avoid suggesting generic training is enough."
- component: advancehe/assessment-2024/students.showcase-competencies
  forPractitioner: { text: "Design tasks that let students show what they can do, in forms that others, including employers, would recognise.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your assessments let you show what you can do, in ways that people outside your course would recognise.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Link this to the source's aim that assessment develops subject-specific and professional competencies and graduate attributes. Do not reduce it to building a portfolio."
  author-agent-dialogue: "Raise it when a student cannot say what an assessment shows about them. Ask: \"What could you show someone outside the course from this task?\" Avoid promising employment outcomes."
- component: advancehe/assessment-2024/students.understand-assessment-criteria
  forPractitioner: { text: "Work through criteria with students, using examples, until they can apply them to their own and others' work.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the criteria your work is judged against, so you can aim at them and see why you got your mark.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present understanding of criteria as part of assessment literacy, which the source names. Do not assume that publishing criteria means students understand them."
  author-agent-dialogue: "Raise it when a student is surprised by a mark. Ask: \"Which criterion do you think this mark reflects?\" and \"What would meeting it look like?\" Avoid re-marking in dialogue."
- component: advancehe/assessment-2024/students.give-and-receive-feedback
  forPractitioner: { text: "Give students regular, structured chances to comment on each other's work as well as to receive comments.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You both give feedback to others and receive it, and you learn from doing each.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present giving feedback as learning in its own right, not only as help for peers; the source names peer and self-assessment. Link it to the institution's support for peer assessment."
  author-agent-dialogue: "Raise it when a student only waits for staff feedback. Ask: \"What did you learn from commenting on someone else's work?\" Avoid treating peer comments as a substitute for staff feedback."
- component: advancehe/assessment-2024/students.contribution-to-group-work
  forPractitioner: { text: "Design group tasks so that each member has a real role, and make individual contribution visible.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "In group work you have a real part to play, and what you contribute is noticed.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Read from the figure; the prose does not discuss group work. Set it beside the institution's equitable processes for group work. Do not present group work as only an employability skill."
  author-agent-dialogue: "Raise it when a student describes doing all the work, or none. Ask: \"What is your role in the group, and how is it recognised?\" Avoid taking sides in group disputes."
- component: advancehe/assessment-2024/students.complex-authentic-challenges
  forPractitioner: { text: "Set tasks that mirror real problems in the subject or profession, with enough support for students to succeed at them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You take on tasks that are like real problems in your field, and you can grow by meeting them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present authenticity in the sense of authentic assessment (realistic tasks), which the source names; do not confuse it with the inclusive model's authentic learners. \"Thrive\" implies support as well as challenge."
  author-agent-dialogue: "Raise it when tasks feel artificial to students. Ask: \"Where would someone in this field meet a problem like this?\" Avoid making tasks complex without support."
- component: advancehe/assessment-2024/students.act-on-feedback
  forPractitioner: { text: "Show students the many forms feedback takes and build in moments where they plan and show how they will use it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to spot feedback in all its forms and to use it to improve your next piece of work.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a learned capability: the source says learning from feedback may be unfamiliar to students. Note that feedback includes comments in class and from peers, not only on scripts."
  author-agent-dialogue: "Raise it when a student says they get no feedback. Ask: \"What comments have you had, in class or from peers, and what did you change because of them?\" Avoid blaming students for not using feedback they were never taught to use."
- component: advancehe/assessment-2024/students.contribute-to-assessment-design
  forPractitioner: { text: "Involve students in designing or reviewing assessment, and tell them what changed as a result.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can help shape how you are assessed, and your views can change the tasks.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as partnership, linked to the institution's co-creation of criteria and to the dialogue with students the source calls for. Do not imply students decide standards alone."
  author-agent-dialogue: "Raise it in course review or when students criticise a task. Ask: \"How could students help redesign this task?\" Avoid promising changes that need approval."
```

### M3 Conditions
<!-- label: editorial; status: drafted; basis: discussion. Ours, every field. -->
```yaml
- component: advancehe/assessment-2024/institution.co-creation-of-criteria
  theme: theme:student-voice-partnership
  holdsWhen: "Students take part in drafting or rewording the criteria for at least some tasks, and their contribution is visible in the final version."
  signs: ["a session where students discuss and draft criteria", "criteria written in language students proposed", "students can say why a criterion is there"]
  absentWhen: "Criteria arrive finished, and students meet them for the first time when they get a mark."
  contextSteer: "Show the learner how the criteria were reached and invite them to restate one in their own words."
  basis: ours
- component: advancehe/assessment-2024/institution.peer-assessment-training
  theme: theme:feedback-dialogue
  holdsWhen: "Before peer assessment counts, students have practised it with guidance and have criteria and examples to work from."
  signs: ["a practice round of peer review before an assessed one", "worked examples of useful and unhelpful feedback", "students refer to the criteria when commenting on peers"]
  absentWhen: "Students are asked to mark or comment on each other's work with no preparation, and the feedback is vague or harsh."
  contextSteer: "Before asking the learner to review a peer's work, give them the criteria, an example and a frame for their comments."
  basis: ours
- component: advancehe/assessment-2024/institution.rubrics-and-criteria
  theme: theme:assessment-literacy
  holdsWhen: "Every assessed task has published criteria in plain language, and students use them while preparing their work."
  signs: ["criteria are given out with the task, not after marking", "teaching sessions use the rubric with sample work", "feedback refers to the criteria by name"]
  absentWhen: "Criteria are missing, vague or kept for markers, and students guess what is wanted."
  contextSteer: "State the criteria for the task plainly at the start and show what meeting each one looks like."
  basis: ours
- component: advancehe/assessment-2024/institution.anonymous-feedback-technology
  theme: theme:feedback-dialogue
  holdsWhen: "Students have a supported digital route to give feedback without being identified, and use it."
  signs: ["peer review or course surveys can be completed anonymously", "staff know how to set up anonymous feedback", "anonymous comments are candid and acted on"]
  absentWhen: "Every comment carries a name, so students soften or withhold what they think."
  contextSteer: "Where the learner is asked to comment on others, offer a way to do so without being named."
  basis: ours
- component: advancehe/assessment-2024/institution.consistent-standards
  theme: theme:consistent-judgement
  holdsWhen: "Modules and markers judge work against shared standards, and checks show their grades agree within an accepted range."
  signs: ["shared grade descriptors are used across modules", "moderation records show few large disagreements", "students describe marking as predictable"]
  absentWhen: "Each module sets its own standard, and similar work gets different grades."
  contextSteer: "Use the same standard throughout the material and say plainly what each level of work looks like."
  basis: ours
- component: advancehe/assessment-2024/institution.program-level-rubrics
  theme: theme:programmatic-assessment
  holdsWhen: "Modules in a programme share rubrics or a common set of criteria that progress across its stages."
  signs: ["a programme rubric is referenced in module handbooks", "criteria wording recurs from year to year with higher expectations", "programme teams agree rubric changes together"]
  absentWhen: "Each module invents its own rubric, and students relearn what counts every time."
  contextSteer: "Connect the criteria here to those the learner has met before and to what comes next."
  basis: ours
- component: advancehe/assessment-2024/institution.equitable-group-work
  theme: theme:consistent-judgement
  holdsWhen: "Group assessments have stated rules for recognising individual contribution and for handling disputes, and they are applied consistently."
  signs: ["peer contribution ratings or individual components in group marks", "a published route for raising group problems", "students say group marks were fair"]
  absentWhen: "Everyone in a group gets one mark regardless of effort, and disputes have no route to resolution."
  contextSteer: "When setting group work, say how individual contribution will be recognised and where problems can be raised."
  basis: ours
- component: advancehe/assessment-2024/institution.calibration-academic-standards
  theme: theme:consistent-judgement
  holdsWhen: "Markers regularly grade common samples together, discuss differences and agree reference points for each standard."
  signs: ["calibration meetings before marking periods", "annotated exemplars agreed by the team", "smaller gaps between first and second markers over time"]
  absentWhen: "Markers work alone, and standards drift between people and from year to year."
  contextSteer: "Anchor any judgement of quality to agreed examples, and show the learner what each standard looks like."
  basis: ours
- component: advancehe/assessment-2024/institution.inclusive-assessment-range
  theme: theme:anticipating-difference
  holdsWhen: "A course assesses through several methods, and each has been checked for barriers unrelated to what it measures."
  signs: ["a programme map shows a spread of assessment types", "task design records an inclusivity check", "attainment gaps between groups are reviewed by method"]
  absentWhen: "One or two methods dominate, and the same students are disadvantaged each time."
  contextSteer: "Offer more than one way to show the learning where the outcome allows it, and remove barriers that are not part of what is tested."
  basis: ours
- component: advancehe/assessment-2024/institution.scaffolding-complexity
  theme: theme:programmatic-assessment
  holdsWhen: "Tasks across a module or course are sequenced so that each builds on skills practised in the one before, with support that decreases."
  signs: ["a task sequence that names the skills each step builds", "early tasks with templates or guided stages", "later tasks that leave more choices to students"]
  absentWhen: "Students meet complex tasks without earlier practice, and support is the same at every stage."
  contextSteer: "Break the task into stages that build on each other, and say which supports will fall away later."
  basis: ours
- component: advancehe/assessment-2024/institution.formative-summative-balance
  theme: theme:programmatic-assessment
  holdsWhen: "Each summative task is preceded by at least one formative opportunity whose feedback students can act on before submission."
  signs: ["formative tasks appear in module schedules ahead of summative ones", "feedback on formative work is returned in time to use", "students take part in formative tasks"]
  absentWhen: "Assessment is almost all summative, and students first learn what is expected when they are marked."
  contextSteer: "Give the learner a low-stakes attempt with feedback before anything that counts."
  basis: ours
- component: advancehe/assessment-2024/institution.holistic-programmatic-approach
  theme: theme:programmatic-assessment
  holdsWhen: "The programme team holds a map of all assessment, uses it to plan, and changes tasks to fit the whole."
  signs: ["a programme assessment map exists and is current", "deadlines are spread by agreement across modules", "tasks refer to earlier and later ones"]
  absentWhen: "Each module plans its own assessment, and students face bunching, repetition and gaps."
  contextSteer: "Place the task within the wider course: say what it builds on and what it prepares for."
  basis: ours
- component: advancehe/assessment-2024/institution.dialogic-feedback
  theme: theme:feedback-dialogue
  holdsWhen: "Students regularly respond to and discuss feedback, and comments name what to do in the next task."
  signs: ["feedback sessions or replies where students ask questions", "comments that say what to change next time", "students refer to earlier feedback in new work"]
  absentWhen: "Feedback is a one-off judgement that students read once and file away."
  contextSteer: "Frame feedback as advice for the next attempt and invite the learner to reply or ask."
  basis: ours
- component: advancehe/assessment-2024/institution.aligned-to-criteria
  theme: theme:assessment-literacy
  holdsWhen: "Feedback names the criteria and the standard reached, and students can link comments to their mark."
  signs: ["comments cite criteria by name", "marks and comments agree", "students can explain their grade using the criteria"]
  absentWhen: "Feedback is general or personal, and students cannot connect it to the mark."
  contextSteer: "When commenting on work, tie each point to a criterion and the standard it reached."
  basis: ours
- component: advancehe/assessment-2024/institution.timely-actionable-feedback
  theme: theme:feedback-dialogue
  holdsWhen: "Feedback reaches students before the next related task and includes at least one action they can take."
  signs: ["return dates are set before the next deadline", "comments include specific next steps", "students act on feedback in their following work"]
  absentWhen: "Feedback arrives too late to use, or says what was wrong without saying what to do."
  contextSteer: "Give feedback the learner can act on straight away, phrased as next steps."
  basis: ours
- component: advancehe/assessment-2024/institution.range-of-places-and-formats
  theme: theme:professional-learning
  holdsWhen: "Development on assessment is offered in several formats and places, and staff in every role take part."
  signs: ["the same development offered online and in person", "part-time and professional services staff take part", "resources are available on demand"]
  absentWhen: "Development runs in one format at one time, and many staff never attend."
  contextSteer: "Not applicable to lesson context: it shapes staff provision, not a learner's setting."
  basis: ours
- component: advancehe/assessment-2024/educators.embedded-in-the-curriculum
  theme: theme:programmatic-assessment
  holdsWhen: "Assessment tasks and the skills they need are planned into teaching sessions, and unfamiliar forms are introduced in stages."
  signs: ["teaching plans name the assessment skills each session builds", "new assessment types are introduced with practice", "students see links between classes and tasks"]
  absentWhen: "Assessment is bolted on after teaching is planned, and students meet unfamiliar forms cold."
  contextSteer: "Link the activity directly to how the learner will later be assessed."
  basis: ours
- component: advancehe/assessment-2024/educators.systems-processes-and-policy
  theme: theme:contextual-adaptation
  holdsWhen: "Staff know the relevant assessment policies, apply them consistently and adapt their application to the course within what the policy allows."
  signs: ["staff cite the relevant regulation when setting tasks", "policy questions are answered by a named person", "local practice is consistent across a team"]
  absentWhen: "Staff are unaware of or ignore policy, or apply it rigidly where it does not fit."
  contextSteer: "Make any rule that governs the task explicit, and explain how it applies here."
  basis: ours
- component: advancehe/assessment-2024/educators.innovative-assessment
  theme: theme:real-world-learning
  holdsWhen: "Course teams introduce and evaluate new assessment methods, and keep those that improve validity or inclusivity."
  signs: ["new methods are piloted with evaluation", "innovations are shared at team or institution level", "reasons for a change of method are recorded"]
  absentWhen: "Methods stay unchanged by habit, even where they no longer fit the outcomes."
  contextSteer: "Where a conventional task would test the wrong thing, choose a format that tests the outcome directly."
  basis: ours
- component: advancehe/assessment-2024/educators.staff-development
  theme: theme:professional-learning
  holdsWhen: "Staff have access to subject-specific development on assessment and feedback and take it up."
  signs: ["development sessions tailored to disciplines", "staff cite recent development when changing practice", "new staff are inducted into assessment practice"]
  absentWhen: "Development is generic or absent, and practice depends on what each person already knows."
  contextSteer: "Not applicable to lesson context: it concerns staff preparation, not a learner's setting."
  basis: ours
- component: advancehe/assessment-2024/students.showcase-competencies
  theme: theme:real-world-learning
  holdsWhen: "Assessment tasks produce work that shows students' competencies in forms they can use beyond the course."
  signs: ["tasks produce outputs students can share", "students can name the competencies a task shows", "professional formats are used where they fit"]
  absentWhen: "Assessment shows only a mark, and students cannot point to what they can do."
  contextSteer: "Ask the learner to produce something that shows a real competence, and say who would value it."
  basis: ours
- component: advancehe/assessment-2024/students.understand-assessment-criteria
  theme: theme:assessment-literacy
  holdsWhen: "Students can explain the criteria for a task in their own words and use them to judge a piece of work."
  signs: ["students paraphrase criteria accurately", "students self-assess against criteria before submitting", "fewer queries about what is wanted"]
  absentWhen: "Students treat the criteria as opaque and see marks as arbitrary."
  contextSteer: "Check that the learner can restate the criteria and apply them to an example before they begin."
  basis: ours
- component: advancehe/assessment-2024/students.give-and-receive-feedback
  theme: theme:feedback-dialogue
  holdsWhen: "Students regularly give structured feedback to peers and receive it, and can say what they learned from both."
  signs: ["peer feedback is built into tasks", "students use criteria when commenting", "students change their work after peer comments"]
  absentWhen: "Feedback flows only from staff to students, and students never judge work themselves."
  contextSteer: "Include a step where the learner gives feedback on another piece of work against the criteria."
  basis: ours
- component: advancehe/assessment-2024/students.contribution-to-group-work
  theme: theme:collaboration
  holdsWhen: "Each member of a group has a defined role, contributes, and has that contribution recognised."
  signs: ["roles are agreed and recorded", "individual contributions are visible in the output or the marks", "students reflect on how the group worked"]
  absentWhen: "A few students carry the group, and contribution goes unseen."
  contextSteer: "When the task is collaborative, give the learner a defined role and a way to show their contribution."
  basis: ours
- component: advancehe/assessment-2024/students.complex-authentic-challenges
  theme: theme:real-world-learning
  holdsWhen: "Students regularly meet tasks that resemble real problems in their field and succeed at them with support."
  signs: ["tasks use real cases, data or clients", "tasks have more than one acceptable answer", "students say the work felt meaningful"]
  absentWhen: "Tasks are artificial exercises with one right answer and little link to the field."
  contextSteer: "Set the task in a realistic situation from the field and allow more than one sound answer."
  basis: ours
- component: advancehe/assessment-2024/students.act-on-feedback
  theme: theme:feedback-dialogue
  holdsWhen: "Students identify feedback from different sources and can show changes in their work made in response."
  signs: ["students keep a record of feedback and actions", "later work shows earlier comments addressed", "students name in-class comments as feedback"]
  absentWhen: "Students read only the mark, and the same comments recur from task to task."
  contextSteer: "Ask the learner to name a piece of earlier feedback and show how they will use it here."
  basis: ours
- component: advancehe/assessment-2024/students.contribute-to-assessment-design
  theme: theme:student-voice-partnership
  holdsWhen: "Students take part in designing or reviewing assessment, and some tasks change as a result."
  signs: ["student representatives sit on assessment design or review", "tasks offer students choices that they helped define", "students are told what changed after their input"]
  absentWhen: "Assessment is designed without students, and their views on it are not sought."
  contextSteer: "Give the learner a say in how the task is shaped, and show what difference their choice makes."
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
  lead: { span: { start: 7792, end: 7848 }, source: "It is particularly relevant to the following dimensions:", page: 14 }
  codes:
    - { to: advancehe/psf-dimensions-2023/V1, code: V1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/V3, code: V3, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A1, code: A1, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/A3, code: A3, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K2, code: K2, page: 14, note: "named in the PSF table" }
    - { to: advancehe/psf-dimensions-2023/K5, code: K5, page: 14, note: "named in the PSF table" }
  fellowship: { span: { start: 7921, end: 8135 }, source: "Advance HE invites all those teaching or supporting learning to evidence their use of this or other Student Success Frameworks in applying for Fellowship in recognition of their commitment to professional practice.", page: 14, note: "an invitation, not an obligation: not an S4 statement" }
inferred:
  - { from: "model", to: "theme:assessment", rel: related, basis: inferred, note: "assessment and feedback are the model's whole subject" }
  - { from: "advancehe/assessment-2024/institution.inclusive-assessment-range", to: "std:doc:advancehe-inclusive-learning-teaching-2024-model", rel: related, basis: inferred, note: "inclusive assessment design meets the inclusive model's anticipating-difference component" }
  - { from: "advancehe/assessment-2024/students.showcase-competencies", to: "theme:employability", rel: related, basis: inferred, note: "the source names professional competencies and employers; the model does not name employability" }
  - { from: "advancehe/assessment-2024/institution.anonymous-feedback-technology", to: "theme:digital", rel: related, basis: inferred, note: "technology for feedback; the source names new technologies on p. 6" }
```

### M6 Practice themes carried
<!-- label: both; status: drafted; basis: discussion -->
```yaml
- { id: theme:student-voice-partnership, tier: practice, working: "a range of voices, students' included, shapes decisions and is answered", carriedBy: ["advancehe/assessment-2024/institution.co-creation-of-criteria", "advancehe/assessment-2024/students.contribute-to-assessment-design"], status: provisional }
- { id: theme:assessment-literacy, tier: practice, working: "staff and students share an understanding of criteria, standards and how work is judged", carriedBy: ["advancehe/assessment-2024/institution.co-creation-of-criteria", "advancehe/assessment-2024/institution.peer-assessment-training", "advancehe/assessment-2024/institution.rubrics-and-criteria", "advancehe/assessment-2024/institution.consistent-standards", "advancehe/assessment-2024/institution.aligned-to-criteria", "advancehe/assessment-2024/students.understand-assessment-criteria"], status: provisional }
- { id: theme:feedback-dialogue, tier: practice, working: "feedback is timely, usable, two-way and acted on", carriedBy: ["advancehe/assessment-2024/institution.peer-assessment-training", "advancehe/assessment-2024/institution.anonymous-feedback-technology", "advancehe/assessment-2024/institution.formative-summative-balance", "advancehe/assessment-2024/institution.dialogic-feedback", "advancehe/assessment-2024/institution.aligned-to-criteria", "advancehe/assessment-2024/institution.timely-actionable-feedback", "advancehe/assessment-2024/students.give-and-receive-feedback", "advancehe/assessment-2024/students.act-on-feedback"], status: provisional }
- { id: theme:psychological-safety, tier: practice, working: "speaking, asking, disagreeing and erring carry no penalty", carriedBy: ["advancehe/assessment-2024/institution.anonymous-feedback-technology"], status: provisional }
- { id: theme:consistent-judgement, tier: practice, working: "assessment judgements are consistent, calibrated and fair across markers, modules and groups", carriedBy: ["advancehe/assessment-2024/institution.consistent-standards", "advancehe/assessment-2024/institution.program-level-rubrics", "advancehe/assessment-2024/institution.equitable-group-work", "advancehe/assessment-2024/institution.calibration-academic-standards", "advancehe/assessment-2024/educators.systems-processes-and-policy"], status: provisional }
- { id: theme:programmatic-assessment, tier: practice, working: "assessment is planned across a whole programme so that tasks connect, balance and build", carriedBy: ["advancehe/assessment-2024/institution.program-level-rubrics", "advancehe/assessment-2024/institution.scaffolding-complexity", "advancehe/assessment-2024/institution.formative-summative-balance", "advancehe/assessment-2024/institution.holistic-programmatic-approach", "advancehe/assessment-2024/educators.embedded-in-the-curriculum"], status: provisional }
- { id: theme:collaboration, tier: practice, working: "learning and problem-solving are done with others, across subjects, professions and sectors", carriedBy: ["advancehe/assessment-2024/institution.equitable-group-work", "advancehe/assessment-2024/students.give-and-receive-feedback", "advancehe/assessment-2024/students.contribution-to-group-work"], status: provisional }
- { id: theme:anticipating-difference, tier: practice, working: "teaching is designed in advance for the range of students", carriedBy: ["advancehe/assessment-2024/institution.inclusive-assessment-range", "advancehe/assessment-2024/educators.innovative-assessment"], status: provisional }
- { id: theme:real-world-learning, tier: practice, working: "learning, assessment and settings are modelled on real practice", carriedBy: ["advancehe/assessment-2024/institution.inclusive-assessment-range", "advancehe/assessment-2024/educators.innovative-assessment", "advancehe/assessment-2024/students.showcase-competencies", "advancehe/assessment-2024/students.complex-authentic-challenges"], status: provisional }
- { id: theme:transition, tier: practice, working: "students are prepared and supported as they move into, through and on from study", carriedBy: ["advancehe/assessment-2024/institution.scaffolding-complexity"], status: provisional }
- { id: theme:professional-learning, tier: practice, working: "staff are given time, support and recognition to develop their practice", carriedBy: ["advancehe/assessment-2024/institution.range-of-places-and-formats", "advancehe/assessment-2024/educators.staff-development"], status: provisional }
- { id: theme:contextual-adaptation, tier: practice, working: "practice adapts to the setting and its students, not the reverse", carriedBy: ["advancehe/assessment-2024/educators.systems-processes-and-policy"], status: provisional }
- { id: theme:agency-self-actualisation, tier: practice, working: "people grow into, use and trust their own judgement", carriedBy: ["advancehe/assessment-2024/students.act-on-feedback"], status: provisional }
```

## Part B Terminology

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: areas-of-focus, definition: "the four categories that organise the model: curriculum, systems and policy, innovation, and staff development", scopeNote: "the quadrants of the institution dial and the segments of the educators dial; held as groups in M1", category: concept, practices: [learning-and-teaching] }
- { slug: academic-literacy, definition: "a student's grasp of how academic work is done and judged in their subject", scopeNote: "the source says assessment practices foster it; the practice theme theme:assessment-literacy is wider, covering staff too", category: concept, practices: [learning-and-teaching] }
- { slug: awarding-gaps, definition: "differences in the grades or degree classes awarded to different groups of students", scopeNote: "the source attributes them to a more diverse intake and calls clear outcomes, criteria and feedback essential to closing them", category: concept, practices: [learning-and-teaching] }
- { slug: formative-assessment, definition: "assessment set mainly to help learning through feedback, with little or nothing riding on the mark", scopeNote: "named with summative assessment; their balance is an institution segment", category: concept, practices: [learning-and-teaching] }
- { slug: self-assessment, definition: "a student judging their own work against the criteria", scopeNote: "named with peer assessment as unfamiliar to many students", category: approach, practices: [learning-and-teaching] }
- { slug: academic-standards, definition: "the levels of achievement an institution holds its awards to", scopeNote: "the source links enhanced assessment to confidence in them; their calibration is an institution segment", category: concept, practices: [learning-and-teaching] }
```

### B2a Terms as the issuer uses them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: areas-of-focus, form: "areas of focus", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: academic-literacy, form: "academic literacy", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: awarding-gaps, form: "awarding gaps", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: formative-assessment, form: "formative assessment", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: self-assessment, form: "self-assessment", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: academic-standards, form: "academic standards", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the model names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term takes a meaning of its own in one component.

### B4 Relations
```yaml
- { rel: related, from: formative-assessment, to: self-assessment, note: "both named as unfamiliar activities to be built in and progressed (p. 8)" }
- { rel: related, from: academic-literacy, to: awarding-gaps, note: "clear criteria and feedback, which build literacy, are named as essential to closing gaps" }
- { rel: related, from: academic-standards, to: areas-of-focus, note: "calibration and consistent standards sit in the Systems, Processes and Policy area" }
```

### B5 Rules
- areas of focus: name them as the issuer does (four), but note the use page speaks of "three areas of focus" meaning the perspectives; say which is meant.
- authentic: in this model it means realistic tasks (authentic assessment), not the inclusive model's "authentic learners"; keep the senses apart.

## Part C Process

### C0 Formality
`not-applicable`: the model sets conditions and uses, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE
  title: "Framework for enhancing assessment"
  edition: "digital edition, 2024 (file revised April 2025)"
  year: 2024
  url: "https://www.advance-he.ac.uk (the series page not reached; D3)"
  retrieved: "PDF supplied by Abbott, 4 October 2026"
  licence: "none stated; held by permission (D-std-0019)"
  tier: primary
  readVia: direct
  held: d66604a96910bea7bcb2ecb3d625673e2723d9d4c4ae6d1de87e7ee8466f83f0
  heldFiles: ["txt/advance-he-2024-framework-enhancing-assessment-standard.txt", "txt/advance-he-2024-framework-enhancing-assessment-standard.norm.txt", "records/advance-he-2024-framework-enhancing-assessment-standard.held.json", "pdf/advance-he-2024-framework-enhancing-assessment-standard.pdf"]
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
- Front matter, S1: no year or copyright notice is printed in the file. The PDF was created on 5 February 2024 and modified on 28 April 2025; the assignment calls it the 2024 framework, revised April 2025. `published: 2024` (the builder's fixed field) and `edition` records the revision. For Abbott: is the 2025 file a new edition or a corrected issue?
- Held text: held by Abbott's permission (4 October 2026, 05:03: "Yes full permission"; D-std-0019, as D-std-0013); private, never published.
- M2 Institution: the dial (p. 7) is two-ring in the sense the brief warned of, but the ring of categories is the OUTER arc (labels on the rim), not an inner ring: sixteen segments in four quadrants of four. All sixteen labels are curved and scrambled in the text layer, so all were read from a 300 dpi render of the page and recorded as printed (`span: none`). Clockwise from twelve o'clock: Embedded in the Curriculum, then Systems, Processes and Policy, then Innovative Assessment, then Staff Development.
- M2 Institution: "Program Level Rubrics" is printed in US spelling; recorded as printed, glossed "programme" in our fields.
- M2 Institution, Staff Development quadrant: its four labels ("Ongoing Dialogic Feedback & Feedforward Processes", "Aligned to Criteria and Standards", "Timely and Actionable Feedback", "Available in a Range of Places and Formats") read as qualities of feedback more than of staff development. Two have no noun. We read the first three as feedback practice staff are developed to give, and the fourth as staff development provision (linked, inferred, to the p. 6 line that staff development be available for all staff). For Abbott: the issuer may mean all four as qualities of feedback.
- M2 Educators+: the dial (p. 9) is single-ring; its four segments are the four areas of focus, whose labels are clean in the text layer. They are recorded both as GROUPS (axis all: they group the institution segments) and as the four educators components, each in its own group. The model template has no way to say a perspective's segments ARE the groups.
- M2 Students: the dial (p. 11) has seven segments and an unlabelled segmented outer rim; the text layer gives the labels in row order, not clockwise. Order here is clockwise from twelve o'clock, read from the image.
- M2 explainedBy: links marked `inferred` are std's reading; the source does not tie its prose to its segments, and several segments (group work, anonymous feedback, programme rubrics) have no prose that names them.
- S4 force: the institution use items are imperatives read as `should` (proposed). The educators and students use items are third-person function lines ("Acts as ...", "Offers ...") read as `describes`. "Educators require ..." is read as must from "require", our reading, since it states a need rather than a duty. For Abbott: rule whether these read as given.
- S4: "It requires dialogue ..." (p. 2) has the enhancement process as its subject; read as must from "requires" like the inclusive model's lead-in.
- S4 use.institution.2: the issuer's grammar mixes an imperative and a gerund ("Encourage ...; providing ..."); recorded as imperative. In the text layer it shares a paragraph with use.institution.3, which is a separate item on the page.
- Use page (p. 12): the issuer speaks of "three areas of focus" for the perspectives, while p. 8 speaks of "four areas of focus" for the categories; B5 asks writers to say which is meant.
- S6: the text names inclusivity, inclusive education, awarding gaps, widening access, new technologies, employers and professional competencies, but not EDI, digital, employability or partnership as such; those sector themes are inferred. Sustainability is named once (p. 4) as a requirement assessment helps adopt; no component carries it, so theme:esd is not carried.
- M6: proposed practice theme theme:assessment-literacy (staff and students share an understanding of criteria, standards and how work is judged).
- M6: proposed practice theme theme:feedback-dialogue (feedback is timely, usable, two-way and acted on).
- M6: proposed practice theme theme:consistent-judgement (assessment judgements are consistent, calibrated and fair across markers, modules and groups).
- M6: proposed practice theme theme:programmatic-assessment (assessment is planned across a whole programme so that tasks connect, balance and build).
- M6: proposed practice theme theme:collaboration (students learn and are assessed through fair, recognised work with peers).
- M6: proposed practice theme theme:real-world-learning (tasks resemble real problems in the field and let students show what they can do); kept apart from theme:authenticity, which is the inclusive model's sense.
- M6: proposed practice theme theme:professional-learning (staff are kept current through development they can reach and that fits their subject).
- M6: every practice theme is provisional until the shared theme register exists (Abbott, 05:09: "we will call them themes").
- M2a: two components (Staff Development, Available in a Range of Places and Formats) have `not-applicable` beneficiary versions and context steers that say they do not qualify a lesson's context.
- S7: the text names no sibling model, only "other Student Success Frameworks"; no siblingOf is recorded. No theory run of this source is known (THEORY none).
- D3: Advance HE's web page for the series (current status, date, revision history) not reached; wanted.
- M2: 16 label(s) not held in the text layer (read from the page image; `span: none`); MD-2 cannot check them by script.

---

## Change notes
- 0.1.1, 2026-10-04 09:26: practice themes aligned across the series by std (15 id(s) renamed by tools/theme_merges.json; the old ids are aliases in the shared theme register); rebuilt on builder 0.2.1. Model template 0.3.0-draft, builder 0.2.1: 27 components, 0 open segments, 17 statements, 13 practice themes.
- 0.1.0, 2026-10-04 09:21: first built (Abbott, 09:08: "Use your template model and refine as you go"; D-std-0018). Model template 0.2.0-draft, builder 0.2.0: 27 components, 0 open segments, 17 statements, 13 practice themes.
