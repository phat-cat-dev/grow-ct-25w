---
id: std:doc:advancehe-enhancing-student-success-2024-model
title: "Enhancing student success in higher education"
profile: standards/model
profileVersion: none yet   # the variant's profile part is to write
issuer: Advance HE
kind: model
modelKind: series-overview
series: advancehe-student-success-frameworks-2024
axes: { perspectives: 0, facets: 4, groups: 0, segments: 24, openSegments: 0, labelsNotInText: 0 }
jurisdiction: [UK]   # not stated; Advance HE is UK-based and its frameworks are used internationally (inferred)
subjectScope: universal
subjects: []
edition: "digital edition, 2024"
published: 2024   # no date printed; from the PDF metadata (Part E)
revised: "none-stated"   # a later file date, if any (Part E)
status: current   # as at the held text; not checked against Advance HE's site (D3)
supersedes: "none-stated"
heldText: { method: sha256-bytes, raw: 50e634264e6dbfa1ee0ca297a9e20e6c1dfaf2e4805f3b87bc6c18a7a2794be2, normalised: eccf7457393da848958c2d41a6a5fff645a4b1e92a82d845f844ce14ed8494fc }
original: { method: sha256-bytes, pdf: a1e31bba4dca762b1a4a6e27360175308b0f616a4f7e8cc4dabbbb64ed888444, held: "library pdf/advance-he-2024-enhancing-student-success-higher-education-standard.pdf" }
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
# Enhancing student success in higher education

> The issuer's text is held beside this document in the library (`txt/advance-he-2024-enhancing-student-success-higher-education-standard.norm.txt`). Each M2 `label` (where the text layer holds it), each `explainedBy` and M4 `source` and each S4 `source` is exactly its span's text, held for language analysis (D-std-0014); private, never published. Every other field is ours, and agents phrase from ours.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The overview of Advance HE's Student Success Frameworks: a model of models that names the nine areas the series covers and the five principles, six operational commitments and four impacts they share, each held here as a component with a practice theme. Reach for it to place one of the series' models in the whole, or to check the shared conditions behind any of them. It sets no levels and no outcomes, and holds none of the detail of the area models: go to those (S7) for that.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Advance HE (2024) introduces its series on student success, which it treats as wider than grades: achievement, moving on, deeper engagement with a subject, personal growth and activity outside the course. It says what the series offers institutions, staff and Students' Unions, then names nine areas, each the subject of its own model, and the principles, commitments and impacts the areas share, drawn as rings of one wheel. Two lines oblige: embedding the areas needs a shared institutional basis, and student success needs critique, evaluation and a positive culture. It invites use of the series as Fellowship evidence but prints no PSF table. It binds no one: it is an enhancement overview, not an assurance standard.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: Advance HE
title: "Enhancing student success in higher education"
series: "Advance HE Student Success Frameworks"
edition: "digital edition, 2024"
dates:
  published: 2024   # not printed; PDF metadata
  other: ["PDF created 2 July 2024", "PDF modified 3 July 2024"]
kind: model
jurisdiction: [UK]
authority: advisory
licence: "none stated in the file (D1)"
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the series as a whole: what student success is, whom the series serves, its nine areas and the principles, commitments and impacts they share (D1, pp. 2-19)"
appliesTo:
  awards: [none-stated]
  levels: [none]
  providers: ["higher education institutions and related sector agencies (as stated)"]
whoMustUse: "no one must; offered to all stakeholders in higher education, with what it offers institutions, academic and professional services staff, and Students' Unions listed (D1, pp. 5-9)"
howUsed: ["review", "design", "other: benchmarking, planning and approval, stakeholder engagement, Fellowship evidence"]
doesNot: "none-stated"
beneficiary: the student
statedScope: "Student success is the primary objective of higher education, making the framework series relevant to all stakeholders involved in, and associated with, higher education."
statedScopeLocator: "D1, p. 5"
statedScopeSpan: { start: 933, end: 1103 }
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "what-is", order: 1, componentType: section, parent: "none", heading: "What is student success?", gloss: "definition of student success as achievement, transition, engagement, skills and growth", pages: "2-3", readFrom: "text layer" }
  - { number: "wheel", order: 2, componentType: figure, parent: "none", heading: "(series wheel)", gloss: "nine areas in a middle ring; principles, commitments (with BELONGING and MATTERING) and impacts as rings; a hub of Institution, Educators+ and Students; repeated on pp. 11, 12, 14, 16 and 18 with one ring highlighted", pages: "3", readFrom: "figure image" }
  - { number: "who-for", order: 3, componentType: section, parent: "none", heading: "Who is the series for?", gloss: "all stakeholders; the three perspectives each model takes; the functions it reaches", pages: "5", readFrom: "text layer" }
  - { number: "why", order: 4, componentType: section, parent: "none", heading: "Why is the series important?", gloss: "evidence base and sector voice; what the series offers three audiences", pages: "6-9", readFrom: "text layer" }
  - { number: "why.institutions", order: 5, componentType: use-list, parent: "why", heading: "For institutions and related sector agencies, the series:", gloss: "six function lines", pages: "6-7", readFrom: "text layer" }
  - { number: "why.staff", order: 6, componentType: use-list, parent: "why", heading: "For academic and professional services staff, the series:", gloss: "four function lines", pages: "8", readFrom: "text layer" }
  - { number: "why.unions", order: 7, componentType: use-list, parent: "why", heading: "For Students’ Unions, associations and guilds, the series:", gloss: "three function lines", pages: "9", readFrom: "text layer" }
  - { number: "areas", order: 8, componentType: section, parent: "none", heading: "Areas of focus", gloss: "nine areas, a note on metrics, and the line that embedding them requires a shared basis", pages: "10-13", readFrom: "text layer and page images" }
  - { number: "principles", order: 9, componentType: section, parent: "none", heading: "Principles", gloss: "five guiding principles of practice", pages: "14-15", readFrom: "text layer" }
  - { number: "commitments", order: 10, componentType: section, parent: "none", heading: "Operational commitments", gloss: "framing line and six commitments", pages: "16-17", readFrom: "text layer" }
  - { number: "impacts", order: 11, componentType: section, parent: "none", heading: "Impacts", gloss: "four places the series has its effect", pages: "18-19", readFrom: "text layer" }
  - { number: "psf", order: 12, componentType: section, parent: "none", heading: "How does this series align with the Professional Standards Framework (PSF) 2023?", gloss: "an alignment paragraph and the Fellowship invitation; no table", pages: "20", readFrom: "text layer" }
excluded:
  - { number: "back-cover", heading: "We help higher education organisations be the best they can be ...", kind: "other: the issuer's promotional back cover", pages: "back cover (PDF p. 12)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only obliging framing lines, requirement lists and use lists are statements (model template rule 3). -->
```yaml
- id: advancehe/student-success-2024/for.institutions.1
  locator: { number: "for.institutions.1", heading: "For institutions and related sector agencies, the series:", page: 6 }
  span: { start: 2295, end: 2405 }
  source: "provides a way of benchmarking or evidencing performance, progress and impact over time, or relative to others"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: institutions
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["provides", "benchmarking", "evidencing"]
  about: "measuring progress"
  themes: ["none"]
  paraphrase: "Gives institutions a means to compare and show their performance and progress, against their own past or against peers."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/for.institutions.2
  locator: { number: "for.institutions.2", heading: "For institutions and related sector agencies, the series:", page: 6 }
  span: { start: 2406, end: 2523 }
  source: "identifies points of interconnectivity across the thematic areas, which help shape and inspire continuous development"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: institutions
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["identifies", "help", "shape", "inspire"]
  about: "links across the areas"
  themes: ["none"]
  paraphrase: "Shows where the series' areas meet, which helps drive continuing improvement."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/for.institutions.3
  locator: { number: "for.institutions.3", heading: "For institutions and related sector agencies, the series:", page: 6 }
  span: { start: 2524, end: 2628 }
  source: "enables consistency of approach while allowing for local contextualisation by programme or service teams"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: institutions
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["enables", "allowing"]
  about: "consistency with local adaptation"
  themes: ["none"]
  paraphrase: "Lets an institution keep one approach while letting teams adapt it to their setting."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/for.institutions.4
  locator: { number: "for.institutions.4", heading: "For institutions and related sector agencies, the series:", page: 7 }
  span: { start: 2633, end: 2717 }
  source: "informs planning, review, validation, accreditation and programme approval processes"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: institutions
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["informs"]
  about: "quality processes"
  themes: ["none"]
  paraphrase: "Feeds into planning, review, approval and accreditation."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/for.institutions.5
  locator: { number: "for.institutions.5", heading: "For institutions and related sector agencies, the series:", page: 7 }
  span: { start: 2718, end: 2854 }
  source: "provides a structure for engaging stakeholder groups, within the sector and beyond, in strategic priorities that impact student outcomes"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: institutions
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["provides", "engaging", "impact"]
  about: "engaging stakeholders in priorities"
  themes: ["none"]
  paraphrase: "Gives a shared structure for drawing stakeholders inside and outside the sector into priorities that affect student outcomes."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/for.institutions.6
  locator: { number: "for.institutions.6", heading: "For institutions and related sector agencies, the series:", page: 7 }
  span: { start: 2855, end: 3019 }
  source: "offers institutions a comprehensive approach for reflecting on and communicating current work, progress, evaluation and impact, both nationally and internationally."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: institutions
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["offers", "reflecting", "communicating"]
  about: "reflecting on and reporting work"
  themes: ["none"]
  paraphrase: "Gives institutions a full way to reflect on their work and to report it at home and abroad."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/for.staff.1
  locator: { number: "for.staff.1", heading: "For academic and professional services staff, the series:", page: 8 }
  span: { start: 3121, end: 3276 }
  source: "offers a structure for enhancing the quality of teaching and learning throughout the academic lifecycle, shaping effective curriculum and assessment design"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: staff
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["offers", "enhancing", "shaping"]
  about: "improving teaching across the lifecycle"
  themes: ["none"]
  paraphrase: "Gives staff a structure for improving teaching and learning at every stage, including curriculum and assessment design."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/for.staff.2
  locator: { number: "for.staff.2", heading: "For academic and professional services staff, the series:", page: 8 }
  span: { start: 3277, end: 3442 }
  source: "provides processes to improve consistency, inclusivity and equity across diverse programmes or courses that positively impact student success within higher education"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: staff
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["provides", "improve", "impact"]
  about: "consistency and fairness across courses"
  themes: ["none"]
  paraphrase: "Gives staff processes that make courses more consistent, inclusive and fair."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/for.staff.3
  locator: { number: "for.staff.3", heading: "For academic and professional services staff, the series:", page: 8 }
  span: { start: 3444, end: 3636 }
  source: "encourages reciprocal and collaborative ways of working (locally, nationally and globally) in the delivery and enhancement of the curriculum, learning and teaching and professional development"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: staff
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["encourages", "working"]
  about: "working together on teaching"
  themes: ["none"]
  paraphrase: "Encourages staff to work with others, near and far, on teaching, the curriculum and their own development."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/for.staff.4
  locator: { number: "for.staff.4", heading: "For academic and professional services staff, the series:", page: 8 }
  span: { start: 3637, end: 3763 }
  source: "gives insight into current research and scholarship to enable programme enhancement, professional development and scholarship."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: staff
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["gives", "enable"]
  about: "access to research"
  themes: ["none"]
  paraphrase: "Points staff to current research to support course improvement, their development and their own scholarship."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/for.unions.1
  locator: { number: "for.unions.1", heading: "For Students’ Unions, associations and guilds, the series:", page: 9 }
  span: { start: 3824, end: 4015 }
  source: "highlights areas across teaching and learning, as well as wider institutional opportunities, where students can engage and have visibility in helping shape and enhance the learning experience"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: unions
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: both
  verbs: ["highlights", "engage", "have", "helping", "shape", "enhance"]
  about: "where students can shape learning"
  themes: ["none"]
  paraphrase: "Shows student bodies where students can take part, and be seen to take part, in shaping their learning experience."
  audience: both
  subjects: inherited
- id: advancehe/student-success-2024/for.unions.2
  locator: { number: "for.unions.2", heading: "For Students’ Unions, associations and guilds, the series:", page: 9 }
  span: { start: 4020, end: 4150 }
  source: "promotes a shared sense of responsibility, engagement and ownership for learning and success across the student journey and beyond"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: unions
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: both
  verbs: ["promotes"]
  about: "shared ownership of learning"
  themes: ["none"]
  paraphrase: "Encourages students and staff to share responsibility for learning and success, during study and after."
  audience: both
  subjects: inherited
- id: advancehe/student-success-2024/for.unions.3
  locator: { number: "for.unions.3", heading: "For Students’ Unions, associations and guilds, the series:", page: 9 }
  span: { start: 4151, end: 4300 }
  source: "identifies skills, knowledge and experiences that foster new ways of thinking and helps shape positive trajectories upon completion of their studies."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: unions
  statementType: characteristic
  force: describes   # a function line: says what the series does, without obliging
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: both
  verbs: ["identifies", "foster", "helps", "shape"]
  about: "skills and experiences for life after study"
  themes: ["none"]
  paraphrase: "Names the skills, knowledge and experiences that open up new thinking and set students on good paths after they finish."
  audience: both
  subjects: inherited
- id: advancehe/student-success-2024/areas.embedding
  locator: { number: "areas.embedding", heading: "Areas of focus", page: 13 }
  span: { start: 6545, end: 6667 }
  source: "Effectively embedding these nine priority areas requires shared principles, processes and outcomes across the institution."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "requires" read as must
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["embedding", "requires"]
  about: "whole-institution basis for the areas"
  themes: ["none"]
  paraphrase: "Embedding the nine areas well needs principles, processes and outcomes that the whole institution shares."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/commitments.frame
  locator: { number: "commitments.frame", heading: "Operational commitments", page: 17 }
  span: { start: 7737, end: 7862 }
  source: "Enabling student success necessitates ongoing critique, evaluation and the development of policy directly linked to practice."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # "necessitates" read as must, beside D-std-0016's "necessary"; not in the list itself; proposed (Part E)
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["Enabling", "necessitates"]
  about: "critique, evaluation and practice-linked policy"
  themes: ["none"]
  paraphrase: "Student success depends on continuing critical review, evaluation and policy that grows out of practice."
  audience: practitioner
  subjects: inherited
- id: advancehe/student-success-2024/commitments.culture
  locator: { number: "commitments.culture", heading: "Operational commitments", page: 17 }
  span: { start: 8076, end: 8154 }
  source: "Student success requires a positive culture that embraces holistic approaches."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  stem: none
  statementType: requirement
  force: must   # D-std-0016: "requires" read as must
  level: none
  perspective: none
  mood: declarative
  readFrom: "text layer"
  appliesTo: "enhancing student success in higher education"
  addressee: provider
  verbs: ["requires", "embraces"]
  about: "a positive whole-person culture"
  themes: ["none"]
  paraphrase: "Student success depends on a positive culture that takes whole-person approaches."
  audience: practitioner
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- statement: advancehe/student-success-2024/for.institutions.1
  forPractitioner: { text: "Use the series to compare your performance with your own past and with peers, and to show the progress you make.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: what the series offers institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line: the issuer says what the series offers; force describes. Do not turn it into a requirement to benchmark."
  author-agent-dialogue: "Raise it in planning or review. Ask: \"Against what will you compare your progress?\""
- statement: advancehe/student-success-2024/for.institutions.2
  forPractitioner: { text: "Use the series to find where its areas overlap, and plan improvements that serve more than one.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: what the series offers institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes. Link it to the interconnectivity principle."
  author-agent-dialogue: "Raise it when areas are planned apart. Ask: \"Where does this area meet another?\""
- statement: advancehe/student-success-2024/for.institutions.3
  forPractitioner: { text: "Use the series to agree a shared approach, and let course and service teams adapt it to their students.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: what the series offers institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes. Note the balance it strikes between consistency and local adaptation."
  author-agent-dialogue: "Raise it when central policy and local need clash. Ask: \"What must be the same everywhere, and what can teams adapt?\""
- statement: advancehe/student-success-2024/for.institutions.4
  forPractitioner: { text: "Draw on the series when planning, reviewing, approving or accrediting courses.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: what the series offers institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes. Do not imply the series is a regulatory requirement in these processes."
  author-agent-dialogue: "Raise it before a course review or approval. Ask: \"Which areas of the series does this course address?\""
- statement: advancehe/student-success-2024/for.institutions.5
  forPractitioner: { text: "Use the series as a common structure when involving partners in priorities that shape student outcomes.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: what the series offers institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes."
  author-agent-dialogue: "Raise it when partners need a shared language. Ask: \"Which priorities do you want partners to help with?\""
- statement: advancehe/student-success-2024/for.institutions.6
  forPractitioner: { text: "Use the series to reflect on current work and to report progress and impact to audiences at home and abroad.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: what the series offers institutions", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes."
  author-agent-dialogue: "Raise it when an institution must report its work. Ask: \"Which areas can you show impact in, and how?\""
- statement: advancehe/student-success-2024/for.staff.1
  forPractitioner: { text: "Use the series to structure improvements to teaching, curriculum and assessment design at each stage of a course.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: what the series offers staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes. Link it to the curriculum and teaching quality impacts."
  author-agent-dialogue: "Raise it in course design. Ask: \"At which stage of the course would this change help most?\""
- statement: advancehe/student-success-2024/for.staff.2
  forPractitioner: { text: "Use the series' processes to make courses more consistent, inclusive and fair for the students taking them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: what the series offers staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes."
  author-agent-dialogue: "Raise it when courses differ in how fairly they treat students. Ask: \"Where do students on different courses get a different deal?\""
- statement: advancehe/student-success-2024/for.staff.3
  forPractitioner: { text: "Work with colleagues locally and further afield on delivering and improving the curriculum and on your own development.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: what the series offers staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes. Link it to the collaboration principle."
  author-agent-dialogue: "Raise it when a teacher works alone on a problem. Ask: \"Who else is working on this, here or elsewhere?\""
- statement: advancehe/student-success-2024/for.staff.4
  forPractitioner: { text: "Use the series to find current research that can inform your course, your development and your own scholarship.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: what the series offers staff", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes. Link it to the scholarship and evidence commitment."
  author-agent-dialogue: "Raise it when a change lacks an evidence base. Ask: \"What does current research say about this?\""
- statement: advancehe/student-success-2024/for.unions.1
  forPractitioner: { text: "Use the series with your Students' Union to find where students can take part in shaping learning and the wider institution.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can find out where you and your Students' Union can have a visible say in how your learning works.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes. Link it to the student partnership area."
  author-agent-dialogue: "Raise it with student representatives. Ask: \"Where could students have more say, and be seen to have it?\""
- statement: advancehe/student-success-2024/for.unions.2
  forPractitioner: { text: "Use the series to build shared responsibility with students for learning and success, through the course and after it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You share in owning your learning and success, with staff, through your studies and after.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes. Link it to the shared responsibility commitment. Note \"responsibility\" here is promoted, not imposed: force describes."
  author-agent-dialogue: "Raise it when a student sees learning as done to them. Ask: \"What part of this is yours to shape?\""
- statement: advancehe/student-success-2024/for.unions.3
  forPractitioner: { text: "Use the series to name the skills, knowledge and experiences that help students think in new ways and move on well.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can see which skills, knowledge and experiences will help you think in new ways and move on well when you finish.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "A function line, force describes. Link it to the employability area."
  author-agent-dialogue: "Raise it with students near the end of their studies. Ask: \"Which experiences here have changed how you think?\""
- statement: advancehe/student-success-2024/areas.embedding
  forPractitioner: { text: "Agree principles, processes and outcomes across the institution before trying to embed the areas; local efforts alone will not do it.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the institution", rewrite: full, force: must, status: drafted }
  author-agent-written: "The overview's one obliging line about the areas, with must force from \"requires\". It introduces the principles, commitments and impacts that follow."
  author-agent-dialogue: "Raise it when one department works on an area alone. Ask: \"What does the rest of the institution share with you on this?\""
- statement: advancehe/student-success-2024/commitments.frame
  forPractitioner: { text: "Keep questioning and evaluating what you do, and make policy from what practice shows.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the institution", rewrite: full, force: must, status: drafted }
  author-agent-written: "The framing line of the operational commitments, force must (our reading of \"necessitates\", marked). The commitments that follow are components, not statements (Part E)."
  author-agent-dialogue: "Raise it when policy is written apart from practice. Ask: \"What in current practice is this policy based on?\""
- statement: advancehe/student-success-2024/commitments.culture
  forPractitioner: { text: "Build a positive culture that attends to the whole person; the series treats this as a condition of success.", rewrite: full, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the institution", rewrite: full, force: must, status: drafted }
  author-agent-written: "The definition of the Culture commitment, which obliges (\"requires\"); held as a statement as well as a component explanation (Part E)."
  author-agent-dialogue: "Raise it when culture is treated as optional. Ask: \"What in the culture here helps or blocks student success?\""
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
- { id: theme:assessment, role: carries, carriedIn: ["areas"], basis: "stated: the overview names Enhancing Assessment in HE as an area" }
- { id: theme:employability, role: carries, carriedIn: ["areas"], basis: "stated: the overview names Embedding Employability in HE as an area" }
- { id: theme:access-retention-attainment-progression, role: carries, carriedIn: ["areas"], basis: "stated: the overview names Student Access, Retention, Attainment and Progression in HE as an area" }
- { id: theme:student-partnership, role: carries, carriedIn: ["areas"], basis: "stated: the overview names Student Engagement through Partnership as an area" }
- { id: theme:internationalisation, role: carries, carriedIn: ["areas"], basis: "stated: the overview names Internationalising HE as an area" }
- { id: theme:flexible-learning, role: carries, carriedIn: ["areas"], basis: "stated: the overview names Flexible Learning in HE as an area" }
- { id: theme:enterprise, role: carries, carriedIn: ["areas"], basis: "stated: the overview names Enterprise and Entrepreneurship as an area" }
- { id: theme:esd, role: carries, carriedIn: ["areas"], basis: "stated: the overview names Education for Sustainable Development as an area" }
- { id: theme:edi, role: carries, carriedIn: ["areas", "principles"], basis: "stated: the overview names Inclusive Learning and Teaching as an area and Inclusivity as a principle" }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: partOf, target: "advancehe-student-success-frameworks-2024", note: "the overview of Advance HE Student Success Frameworks" }
- { rel: overviewOf, target: "std:doc:advancehe-enhancing-assessment-2024-model", note: "the overview names this area and summarises it in one line (Enhancing Assessment in HE, p. 10)" }
- { rel: overviewOf, target: "std:doc:advancehe-embedding-employability-2024-model", note: "the overview names this area and summarises it in one line (Embedding Employability in HE, p. 10)" }
- { rel: overviewOf, target: "std:doc:advancehe-access-retention-attainment-progression-2024-model", note: "the overview names this area and summarises it in one line (Student Access, Retention, Attainment and Progression in HE, p. 10)" }
- { rel: overviewOf, target: "none-held: Student Engagement through Partnership", note: "the overview names this area and summarises it in one line (p. 10); the model is not held (D3)" }
- { rel: overviewOf, target: "std:doc:advancehe-internationalising-higher-education-2024-model", note: "the overview names this area and summarises it in one line (Internationalising HE, p. 10)" }
- { rel: overviewOf, target: "none-held: Flexible Learning in HE", note: "the overview names this area and summarises it in one line (p. 13); the model is not held (D3)" }
- { rel: overviewOf, target: "std:doc:advancehe-education-sustainable-development-2024-model", note: "the overview names this area and summarises it in one line (Education for Sustainable Development, p. 13)" }
- { rel: overviewOf, target: "std:doc:advancehe-inclusive-learning-teaching-2024-model", note: "the overview names this area and summarises it in one line (Inclusive Learning and Teaching, p. 13)" }
- { rel: overviewOf, target: "std:doc:advancehe-enterprise-entrepreneurship-2024-model", note: "the overview names this area and summarises it in one line (Enterprise and Entrepreneurship, p. 13)" }
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
figure: { form: wheel, pages: [3, 11, 12, 14, 16, 18], readFrom: "text layer and page images" }
axes:
  - { id: facet:areas, label: "Areas of focus", page: 10, segments: 9, openSegments: 0, note: "nine areas, printed on pp. 10 and 13 and drawn as the middle ring of the series wheel (pp. 3, 11, 12)" }
  - { id: facet:principles, label: "Principles", page: 15, segments: 5, openSegments: 0, note: "drawn as the dark ring around the areas in the wheel (p. 14)" }
  - { id: facet:commitments, label: "Operational commitments", page: 17, segments: 6, openSegments: 0, note: "drawn as the outer ring of the wheel (p. 16), which also prints BELONGING and MATTERING; the text lists six commitments and neither of those (Part E)" }
  - { id: facet:impacts, label: "Impacts", page: 19, segments: 4, openSegments: 0, note: "drawn as the inner ring of the wheel (p. 18), around a hub of Institution, Educators+ and Students" }
groups: none
use: "to give institutions, academic and professional services staff, and Students' Unions one view of the nine areas the series covers, with the principles, commitments and impacts they share; what the series offers each audience is listed (S4 for.*) (D1, pp. 6-9)"
```

### M2 Components
<!-- label: both; status: drafted; basis: primary. In the figure's order (Part E). -->
```yaml
- id: advancehe/student-success-2024/areas.assessment
  label: "Enhancing Assessment in HE"
  span: { start: 4607, end: 4633 }
  position: { axis: facet:areas, group: none, order: 1, page: 10 }
  explainedBy:
    - { span: { start: 4635, end: 4755 }, source: "Promote desirable learning behaviours and maximise opportunities for student learning throughout the assessment process.", link: stated, page: 10 }
  conditionType: practice
  actor: all
  about: "assessment that drives learning"
  paraphrase: "Assessment is designed so that it encourages good study habits and gives students the most chances to learn at every stage."
  themes: ["theme:assessment-for-learning", "theme:assessment"]
  sameLabelAs: none
- id: advancehe/student-success-2024/areas.employability
  label: "Embedding Employability in HE"
  span: { start: 4756, end: 4785 }
  position: { axis: facet:areas, group: none, order: 2, page: 10 }
  explainedBy:
    - { span: { start: 4787, end: 4926 }, source: "Enable successful transitions and contributions for students throughout HE and beyond, benefitting them, their communities and the economy.", link: stated, page: 10 }
  conditionType: practice
  actor: all
  about: "preparing for life and work after study"
  paraphrase: "Study prepares students to move on well and to contribute, during their course and after it, to their own lives, communities and the economy."
  themes: ["theme:transition", "theme:employability"]
  sameLabelAs: none
- id: advancehe/student-success-2024/areas.access-retention-attainment-progression
  label: "Student Access, Retention, Attainment and Progression in HE"
  span: { start: 4927, end: 4986 }
  position: { axis: facet:areas, group: none, order: 3, page: 10 }
  explainedBy:
    - { span: { start: 4988, end: 5110 }, source: "Foster a culture that promotes and enables the full and equitable participation of all students to, through and beyond HE.", link: stated, page: 10 }
  conditionType: culture
  actor: institution
  about: "fair participation across the student lifecycle"
  paraphrase: "The institution's culture lets every student get in, stay, do well and move on, on equal terms with others."
  themes: ["theme:equitable-participation", "theme:access-retention-attainment-progression"]
  sameLabelAs: none
- id: advancehe/student-success-2024/areas.student-partnership
  label: "Student Engagement through Partnership"
  span: { start: 5116, end: 5154 }
  position: { axis: facet:areas, group: none, order: 4, page: 10 }
  explainedBy:
    - { span: { start: 5156, end: 5340 }, source: "Commit to developing open, constructive and continuous dialogue between students and staff, among students, and between institutions and their Students’ Unions, associations or guilds.", link: stated, page: 10 }
  conditionType: relationship
  actor: all
  about: "ongoing dialogue between students, staff and unions"
  paraphrase: "Students, staff and student bodies keep talking openly and usefully, so that students shape their education as partners."
  themes: ["theme:student-voice-partnership", "theme:student-partnership"]
  sameLabelAs: none
- id: advancehe/student-success-2024/areas.internationalising
  label: "Internationalising HE"
  span: { start: 5341, end: 5362 }
  position: { axis: facet:areas, group: none, order: 5, page: 10 }
  explainedBy:
    - { span: { start: 5364, end: 5457 }, source: "Prepare graduates to live in and contribute responsibly to a globally interconnected society.", link: stated, page: 10 }
  conditionType: practice
  actor: all
  about: "preparing students for a connected world"
  paraphrase: "Study prepares students to live and act responsibly in a world where societies are closely linked."
  themes: ["theme:intercultural-engagement", "theme:global-citizenship", "theme:internationalisation"]
  sameLabelAs: none
- id: advancehe/student-success-2024/areas.flexible-learning
  label: "Flexible Learning in HE"
  span: { start: 5553, end: 5576 }
  position: { axis: facet:areas, group: none, order: 6, page: 13 }
  explainedBy:
    - { span: { start: 5578, end: 5771 }, source: "Employ pedagogically informed technologies, learning spaces and policies to create personalised, engaging learning experiences, allowing students to choose how, what, when and where they learn.", link: stated, page: 13 }
  conditionType: structure
  actor: institution
  about: "student choice over how, when and where to learn"
  paraphrase: "Technology, spaces and policy are used with teaching in mind so that students can choose the manner, content, time and place of their learning."
  themes: ["theme:flexibility", "theme:flexible-learning"]
  sameLabelAs: none
- id: advancehe/student-success-2024/areas.esd
  label: "Education for Sustainable Development"
  span: { start: 5973, end: 6010 }
  position: { axis: facet:areas, group: none, order: 7, page: 13 }
  explainedBy:
    - { span: { start: 6012, end: 6150 }, source: "Equip learners with the knowledge, competencies and values to tackle interconnected global challenges and promote sustainable citizenship.", link: stated, page: 13 }
  conditionType: practice
  actor: all
  about: "learning to act on global challenges sustainably"
  paraphrase: "Students gain what they need, in knowledge, ability and values, to address linked global problems and to act as sustainable citizens."
  themes: ["theme:global-citizenship", "theme:esd"]
  sameLabelAs: none
- id: advancehe/student-success-2024/areas.inclusive
  label: "Inclusive Learning and Teaching"
  span: { start: 6395, end: 6426 }
  position: { axis: facet:areas, group: none, order: 8, page: 13 }
  explainedBy:
    - { span: { start: 6428, end: 6543 }, source: "Promote a universal approach to design for learning to provide equitable access and opportunities for all students.", link: stated, page: 13 }
  conditionType: practice
  actor: all
  about: "learning designed for everyone from the start"
  paraphrase: "Learning is designed from the start for the whole range of students, so that each has fair access and the same chances."
  themes: ["theme:anticipating-difference", "theme:equitable-participation", "theme:edi"]
  sameLabelAs: none
- id: advancehe/student-success-2024/areas.enterprise
  label: "Enterprise and Entrepreneurship"
  span: { start: 5773, end: 5804 }
  position: { axis: facet:areas, group: none, order: 9, page: 13 }
  explainedBy:
    - { span: { start: 5806, end: 5971 }, source: "Inform and support the delivery of enterprise and entrepreneurship education, whether for venture creation or to support the development of entrepreneurial mindsets.", link: stated, page: 13 }
  conditionType: practice
  actor: all
  about: "enterprising thinking and venture creation"
  paraphrase: "Students are helped to think and act in enterprising ways, whether or not they go on to start a venture."
  themes: ["theme:entrepreneurial-mindset", "theme:enterprise"]
  sameLabelAs: none
- id: advancehe/student-success-2024/principles.inclusivity
  label: "Inclusivity"
  span: { start: 6883, end: 6894 }
  position: { axis: facet:principles, group: none, order: 1, page: 15 }
  explainedBy:
    - { span: { start: 6895, end: 7030 }, source: "Enabling the full and equitable participation of all students and staff through proactively developing inclusive approaches and values.", link: stated, page: 15 }
  conditionType: culture
  actor: all
  about: "fair participation for students and staff"
  paraphrase: "Inclusive ways of working and values are built in advance, so that every student and member of staff can take part fully and fairly."
  themes: ["theme:equitable-participation"]
  sameLabelAs: none
- id: advancehe/student-success-2024/principles.student-centred
  label: "Student-centred"
  span: { start: 7032, end: 7047 }
  position: { axis: facet:principles, group: none, order: 2, page: 15 }
  explainedBy:
    - { span: { start: 7048, end: 7171 }, source: "Enabling every student to take ownership of their learning journey and their individual definition of a successful outcome.", link: stated, page: 15 }
    - { span: { start: 654, end: 819 }, source: "enabling every student to attain their unique benchmarks of success, reinforcing their motivations and fulfilling their expectations of studying in higher education.", link: inferred, page: 3 }
  conditionType: disposition
  actor: student
  about: "students owning their path and what success means"
  paraphrase: "Each student shapes their own route through study and decides what a good outcome means for them."
  themes: ["theme:agency-self-actualisation"]
  sameLabelAs: none
- id: advancehe/student-success-2024/principles.agility
  label: "Agility"
  span: { start: 7173, end: 7180 }
  position: { axis: facet:principles, group: none, order: 3, page: 15 }
  explainedBy:
    - { span: { start: 7181, end: 7328 }, source: "Creating structures, systems and approaches that are agile and responsive to changing needs and requirements of students, employers and regulators.", link: stated, page: 15 }
  conditionType: structure
  actor: institution
  about: "structures that respond to change"
  paraphrase: "The institution's structures and ways of working can change quickly as the needs of students, employers and regulators change."
  themes: ["theme:contextual-adaptation"]
  sameLabelAs: none
- id: advancehe/student-success-2024/principles.interconnectivity
  label: "Interconnectivity"
  span: { start: 7330, end: 7347 }
  position: { axis: facet:principles, group: none, order: 4, page: 15 }
  explainedBy:
    - { span: { start: 7348, end: 7482 }, source: "Making connections across thematic areas between people, disciplines and activity locally, regionally, nationally and internationally.", link: stated, page: 15 }
    - { span: { start: 2406, end: 2523 }, source: "identifies points of interconnectivity across the thematic areas, which help shape and inspire continuous development", link: stated, page: 6 }
  conditionType: practice
  actor: all
  about: "linking areas, people and disciplines"
  paraphrase: "Work in one area is linked to the others, and to people and disciplines near and far."
  themes: ["theme:interconnectivity"]
  sameLabelAs: none
- id: advancehe/student-success-2024/principles.collaboration
  label: "Collaboration"
  span: { start: 7484, end: 7497 }
  position: { axis: facet:principles, group: none, order: 5, page: 15 }
  explainedBy:
    - { span: { start: 7498, end: 7617 }, source: "Working in partnership with all stakeholders internally and externally to engender shared ownership and responsibility.", link: stated, page: 15 }
  conditionType: relationship
  actor: all
  about: "partnership with everyone involved"
  paraphrase: "Everyone with a stake, inside and outside the institution, works as a partner, so that all share ownership."
  themes: ["theme:whole-institution", "theme:student-voice-partnership"]
  sameLabelAs: none
- id: advancehe/student-success-2024/commitments.leadership-strategy
  label: "Leadership and strategy for learning and teaching"
  span: { start: 7916, end: 7965 }
  position: { axis: facet:commitments, group: none, order: 1, page: 17 }
  explainedBy:
    - { span: { start: 7966, end: 8066 }, source: "Committing and organising resources towards the achievement of a shared vision for student outcomes.", link: stated, page: 17 }
  conditionType: structure
  actor: institution
  about: "leadership that resources a shared vision"
  paraphrase: "Leaders set a shared aim for student outcomes and put resources behind it in an organised way."
  themes: ["theme:whole-institution"]
  sameLabelAs: none
- id: advancehe/student-success-2024/commitments.culture
  label: "Culture"
  span: { start: 8068, end: 8075 }
  position: { axis: facet:commitments, group: none, order: 2, page: 17 }
  explainedBy:
    - { span: { start: 8076, end: 8154 }, source: "Student success requires a positive culture that embraces holistic approaches.", link: stated, page: 17 }
    - { span: { start: 8155, end: 8229 }, source: "Such an environment empowers educators, related staff, and students alike.", link: stated, page: 17 }
  conditionType: culture
  actor: all
  about: "a positive, whole-person culture"
  paraphrase: "The institution has a positive culture that looks at the whole person and gives staff and students the power to act."
  themes: ["theme:agency-self-actualisation"]
  sameLabelAs: none
- id: advancehe/student-success-2024/commitments.shared-responsibility
  label: "Shared responsibility"
  span: { start: 8231, end: 8252 }
  position: { axis: facet:commitments, group: none, order: 3, page: 17 }
  explainedBy:
    - { span: { start: 8253, end: 8426 }, source: "Providing clearly defined responsibilities for staff and students, given all have a key role to play in learning and teaching and ultimately contributing to student success.", link: stated, page: 17 }
    - { span: { start: 4020, end: 4150 }, source: "promotes a shared sense of responsibility, engagement and ownership for learning and success across the student journey and beyond", link: inferred, page: 9 }
  conditionType: structure
  actor: all
  about: "clear roles for staff and students"
  paraphrase: "Staff and students each know what they are responsible for, because each has a part in learning and in success."
  themes: ["theme:whole-institution"]
  sameLabelAs: none
- id: advancehe/student-success-2024/commitments.scholarship-evidence
  label: "Scholarship and evidence"
  span: { start: 8428, end: 8452 }
  position: { axis: facet:commitments, group: none, order: 4, page: 17 }
  explainedBy:
    - { span: { start: 8453, end: 8529 }, source: "Utilising underpinning pedagogical research and relevant institutional data.", link: stated, page: 17 }
    - { span: { start: 3637, end: 3763 }, source: "gives insight into current research and scholarship to enable programme enhancement, professional development and scholarship.", link: inferred, page: 9 }
  conditionType: practice
  actor: all
  about: "practice based on research and data"
  paraphrase: "Practice draws on research about teaching and on the institution's own data."
  themes: ["theme:evidence-informed-enhancement"]
  sameLabelAs: none
- id: advancehe/student-success-2024/commitments.continual-development
  label: "Continual development"
  span: { start: 8531, end: 8552 }
  position: { axis: facet:commitments, group: none, order: 5, page: 17 }
  explainedBy:
    - { span: { start: 8553, end: 8705 }, source: "Investing in ongoing and collaborative learning processes for staff and students, to facilitate engagement, reflection, planning, action and evaluation.", link: stated, page: 17 }
  conditionType: process
  actor: all
  about: "ongoing learning for staff and students"
  paraphrase: "The institution invests in learning that never stops, for staff and students together, moving through reflection, planning, action and review."
  themes: ["theme:evidence-informed-enhancement"]
  sameLabelAs: none
- id: advancehe/student-success-2024/commitments.evaluation-impact
  label: "Evaluation and impact"
  span: { start: 8711, end: 8732 }
  position: { axis: facet:commitments, group: none, order: 6, page: 17 }
  explainedBy:
    - { span: { start: 8733, end: 8864 }, source: "Identifying and recording a range of metrics, using a variety of methods, to demonstrate the impact of activity on student success.", link: stated, page: 17 }
    - { span: { start: 8865, end: 8995 }, source: "This may include metrics on retention, attainment and graduate outcomes, alongside data regarding access, wellbeing and belonging.", link: stated, page: 17 }
  conditionType: process
  actor: institution
  about: "measuring what difference activity makes"
  paraphrase: "The institution chooses and records several measures, by several methods, to show what difference its work makes to student success."
  themes: ["theme:evidence-informed-enhancement"]
  sameLabelAs: none
- id: advancehe/student-success-2024/impacts.curriculum
  label: "Curriculum"
  span: { start: 9198, end: 9208 }
  position: { axis: facet:impacts, group: none, order: 1, page: 19 }
  explainedBy:
    - { span: { start: 9209, end: 9294 }, source: "The content, design, delivery and assessment of the formal and/or informal curricula.", link: stated, page: 19 }
  conditionType: practice
  actor: educator
  about: "what is taught, how and how it is assessed"
  paraphrase: "The series acts on what is taught, how it is designed and delivered and how it is assessed, in both formal and informal curricula."
  themes: ["theme:hidden-curriculum"]
  sameLabelAs: none
- id: advancehe/student-success-2024/impacts.learning-environments
  label: "Learning environments"
  span: { start: 9295, end: 9316 }
  position: { axis: facet:impacts, group: none, order: 2, page: 19 }
  explainedBy:
    - { span: { start: 9317, end: 9410 }, source: "The design and provision of formal and/or informal learning spaces, technology and resources.", link: stated, page: 19 }
  conditionType: environment
  actor: institution
  about: "spaces, technology and resources for learning"
  paraphrase: "The series acts on the spaces, technology and resources in which students learn, formal and informal alike."
  themes: ["theme:flexibility"]
  sameLabelAs: none
- id: advancehe/student-success-2024/impacts.learning-communities
  label: "Learning communities"
  span: { start: 9416, end: 9436 }
  position: { axis: facet:impacts, group: none, order: 3, page: 19 }
  explainedBy:
    - { span: { start: 9437, end: 9552 }, source: "Engaging staff and students in professional, academic and discipline communities within and beyond the institution.", link: stated, page: 19 }
  conditionType: relationship
  actor: all
  about: "belonging to communities of learning"
  paraphrase: "The series acts by drawing staff and students into professional, academic and subject communities, inside and outside the institution."
  themes: ["theme:belonging-mattering", "theme:interconnectivity"]
  sameLabelAs: none
- id: advancehe/student-success-2024/impacts.teaching-quality
  label: "Teaching quality"
  span: { start: 9553, end: 9569 }
  position: { axis: facet:impacts, group: none, order: 4, page: 19 }
  explainedBy:
    - { span: { start: 9570, end: 9682 }, source: "The quality of design, delivery or evaluation of teaching as core to the enhancement of any theme or discipline.", link: stated, page: 19 }
  conditionType: practice
  actor: educator
  about: "well designed, delivered and evaluated teaching"
  paraphrase: "The series acts on how well teaching is designed, delivered and evaluated, which underpins progress in any area or subject."
  themes: ["theme:evidence-informed-enhancement"]
  sameLabelAs: none
```

### M2a Component audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- component: advancehe/student-success-2024/areas.assessment
  forPractitioner: { text: "Design each assessment so that preparing for it, doing it and getting feedback on it all build learning, and so that it rewards the study habits you want.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your assessments are there to help you learn as well as to measure you, with chances to improve before, during and after each one.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the series' assessment area, which has its own model (S7 overviewOf). Describe it as assessment for learning across the whole process, not as marking. Do not attribute detail from the assessment model to this overview."
  author-agent-dialogue: "Raise it when a task is discussed only as a grade. Ask: \"What does a student learn by preparing for this?\" and \"Where is the feedback, and can it be used?\" Avoid implying fewer assessments always help."
- component: advancehe/student-success-2024/areas.employability
  forPractitioner: { text: "Build preparation for work and further study into the course itself, and link what students learn to the contributions they will make beyond it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your course helps you move on well, into work or further study, and shows how what you learn lets you contribute to your community.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the series' employability area, which has its own model (S7 overviewOf). Note the issuer frames it as transitions and contributions, wider than getting a job. Do not reduce it to careers services."
  author-agent-dialogue: "Raise it when a student asks what a module is for. Ask: \"Where could you use this after your course?\" Avoid treating employability as separate from the subject."
- component: advancehe/student-success-2024/areas.access-retention-attainment-progression
  forPractitioner: { text: "Look at who gets in, who stays, who does well and who moves on, find where some groups fall behind, and change what causes it.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect a fair chance to get in, to stay, to do well and to move on, whatever your background.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the series' access, retention, attainment and progression area, which has its own model (S7 overviewOf). Keep the four stages together as the issuer does. Do not frame gaps as students' deficits."
  author-agent-dialogue: "Raise it when outcomes differ between groups. Ask: \"At which stage do some students fall away, and what about the course causes it?\" Avoid blaming the students affected."
- component: advancehe/student-success-2024/areas.student-partnership
  forPractitioner: { text: "Set up regular, two-way conversations with students and their union, and let what students say change what you do.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can work with staff and your Students' Union as a partner, and talk with them regularly about how your education works.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the series' partnership area; its own model is not held (S7, D3), so draw only on this overview. Stress that dialogue is continuous and runs in three directions."
  author-agent-dialogue: "Raise it when students are consulted once and not again. Ask: \"How do students hear what came of what they said?\" Avoid treating one survey as partnership."
- component: advancehe/student-success-2024/areas.internationalising
  forPractitioner: { text: "Bring global perspectives and intercultural work into the curriculum for all students, not only those who travel.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your course prepares you to live and work well with people across the world and to act responsibly in a connected society.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the series' internationalising area, which has its own model (S7 overviewOf). Note it is framed as preparation for every graduate, not as recruitment of overseas students."
  author-agent-dialogue: "Raise it when a curriculum draws on one national view only. Ask: \"Whose perspectives from elsewhere would change how this topic looks?\" Avoid treating international students as a resource for others."
- component: advancehe/student-success-2024/areas.flexible-learning
  forPractitioner: { text: "Choose technology, spaces and rules for how they support learning, and use them to give students real choices about how and when they study.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can choose how, when and where you learn, and some of what you learn, with tools and spaces that support it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the series' flexible learning area; its own model is not held (S7, D3), so draw only on this overview. Do not equate it with online delivery; the issuer names spaces and policies as well."
  author-agent-dialogue: "Raise it when a student cannot fit study around other demands. Ask: \"Which parts of this could be done at another time or place?\" Avoid promising choices the course does not offer."
- component: advancehe/student-success-2024/areas.esd
  forPractitioner: { text: "Connect your subject to global challenges such as climate and inequality, and build the values and abilities students need to act on them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You learn how your subject bears on big shared problems, like climate, and how you can act on them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the series' sustainable development area, which has its own model (S7 overviewOf), and beside the QAA and Advance HE ESD guidance held in the store. Note it names values as well as knowledge."
  author-agent-dialogue: "Raise it when a subject seems far from sustainability. Ask: \"Which global challenge does this topic touch, and what could you do about it?\" Avoid moralising."
- component: advancehe/student-success-2024/areas.inclusive
  forPractitioner: { text: "Design teaching and materials for the full range of students you will have, so that few need special arrangements.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your course is designed from the start so that you can take part fully, without having to ask for special arrangements.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the series' inclusive learning and teaching area, which has its own model (S7 overviewOf); that model is ingested and holds the detail. Note the overview names a universal approach to design."
  author-agent-dialogue: "Raise it when access is handled case by case. Ask: \"What change to the design would mean no one needs to ask?\" Avoid suggesting formal adjustments are unnecessary."
- component: advancehe/student-success-2024/areas.enterprise
  forPractitioner: { text: "Give students chances to spot opportunities, try ideas and act on them in your subject, for a business or for any other purpose.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You get to spot opportunities, try out ideas and make things happen, whether or not you ever start a business.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the series' enterprise area, which has its own model (S7 overviewOf), and beside the QAA enterprise guidance held in the store. Note the two aims: venture creation and mindset."
  author-agent-dialogue: "Raise it when a student thinks enterprise is only for business students. Ask: \"Where in your subject could you spot a need and act on it?\" Avoid reducing it to starting companies."
- component: advancehe/student-success-2024/principles.inclusivity
  forPractitioner: { text: "Build inclusive approaches before they are needed, and check that staff as well as students can take part on equal terms.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to take part fully and fairly, because the ways things are done are planned with everyone in mind.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a principle the issuer says runs through every model in the series. Note it covers staff as well as students, and stresses acting in advance."
  author-agent-dialogue: "Raise it when inclusion is treated as a response to complaints. Ask: \"What could be put in place before anyone is excluded?\" Avoid narrowing it to one group."
- component: advancehe/student-success-2024/principles.student-centred
  forPractitioner: { text: "Ask students what success means to them, and give them real choices that let them steer their own path.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You decide what success means for you and have a real say in the path you take to get there.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a series principle. Note the issuer lets each student define success, which links to its opening view of student success as individual. Do not reduce it to student satisfaction."
  author-agent-dialogue: "Raise it when success is described by one measure. Ask: \"What would a good outcome look like for you?\" Avoid imposing one picture of success."
- component: advancehe/student-success-2024/principles.agility
  forPractitioner: { text: "Keep structures and processes light enough to change, and review them when the needs of students, employers or regulators shift.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your university to change how it works when your needs, or the world you are heading into, change.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a series principle about responsiveness. Note the issuer names three sources of change: students, employers and regulators. Do not present it as constant change for its own sake."
  author-agent-dialogue: "Raise it when a process lags behind need. Ask: \"What has changed since this was set up, and how quickly could it adapt?\" Avoid assuming every change is possible at once."
- component: advancehe/student-success-2024/principles.interconnectivity
  forPractitioner: { text: "Link work across the areas (assessment with inclusion, employability with sustainability) and connect with colleagues and disciplines beyond your own.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You get to see how your subject links to others and to people and places beyond your university.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a series principle: the areas are not separate projects. When writing about one area, name where it meets another. Do not invent links the series does not draw."
  author-agent-dialogue: "Raise it when an initiative is run in isolation. Ask: \"Which other area does this touch, and who works on that?\" Avoid making every task about every area."
- component: advancehe/student-success-2024/principles.collaboration
  forPractitioner: { text: "Work with students, colleagues, employers and the community as partners, so that the work belongs to all of them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You work as a partner with staff and others, and share in owning how your education works.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a series principle. Note it reaches outside the institution and aims at shared ownership. Link it to the student partnership area and the shared responsibility commitment."
  author-agent-dialogue: "Raise it when one party carries a change alone. Ask: \"Who else has a stake here, and how could they share the work?\" Avoid token involvement."
- component: advancehe/student-success-2024/commitments.leadership-strategy
  forPractitioner: { text: "Agree a shared aim for student outcomes and allocate people, time and money to it, not only words.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your university to put real resources behind the outcomes it says it wants for you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an operational commitment of the series. Stress resourcing as well as vision. Do not present it as a role description for named posts."
  author-agent-dialogue: "Raise it when a goal has no resources. Ask: \"Who owns this aim, and what has been set aside to meet it?\" Avoid criticising named leaders."
- component: advancehe/student-success-2024/commitments.culture
  forPractitioner: { text: "Build a culture that attends to the whole person and gives staff and students the confidence and room to act.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect a positive place to study, where your whole life is taken into account and you are trusted to act.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an operational commitment. Note the issuer uses obliging language here (S4 commitments.culture). Keep \"holistic\" as whole-person, not as a vague positive."
  author-agent-dialogue: "Raise it when people feel they cannot act without permission. Ask: \"What would help you feel able to act on this?\" Avoid treating culture as a slogan."
- component: advancehe/student-success-2024/commitments.shared-responsibility
  forPractitioner: { text: "Make clear what staff and what students are responsible for in learning, and hold both to it fairly.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You know what is yours to do in your learning and what staff will do, and you have a real part in your success.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an operational commitment. Stress that responsibilities are defined for both staff and students. Do not use it to shift blame to students."
  author-agent-dialogue: "Raise it when roles are unclear. Ask: \"What is yours to do here, and what can you expect from staff?\" Avoid implying students are solely responsible for outcomes."
- component: advancehe/student-success-2024/commitments.scholarship-evidence
  forPractitioner: { text: "Base changes on research about teaching and on your own institution's data, and say which evidence you used.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect how you are taught to rest on evidence about what helps students learn.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an operational commitment. Note the two kinds of evidence: published pedagogical research and local data. Do not overstate the strength of evidence for any practice."
  author-agent-dialogue: "Raise it when a change is justified by habit. Ask: \"What evidence suggests this will help, here or elsewhere?\" Avoid dismissing professional judgement."
- component: advancehe/student-success-2024/commitments.continual-development
  forPractitioner: { text: "Give staff and students time and support to learn together in cycles: reflect, plan, act and review.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You keep developing through cycles of reflecting, planning, acting and looking back, alongside staff who do the same.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an operational commitment. Note it covers staff and students and names a cycle. Link it to scholarship and evidence and to evaluation and impact."
  author-agent-dialogue: "Raise it when development is a one-off event. Ask: \"What will you try next, and how will you know it worked?\" Avoid adding workload without time."
- component: advancehe/student-success-2024/commitments.evaluation-impact
  forPractitioner: { text: "Decide at the start how you will show the difference an activity makes, and use more than one measure and method.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect your university to check whether what it does actually helps you, and to change what does not.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an operational commitment. Note the issuer lists wellbeing and belonging beside outcome measures. Do not equate impact with one metric."
  author-agent-dialogue: "Raise it when an activity has no plan for showing its effect. Ask: \"How would you know if this made a difference to students?\" Avoid measuring only what is easy."
- component: advancehe/student-success-2024/impacts.curriculum
  forPractitioner: { text: "Look at the whole curriculum, including what students learn outside formal sessions and from how things are done, when making changes.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "What you learn, and how, includes the formal course and the things you pick up around it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the four places the series has its effect. Note \"informal curricula\": the issuer counts learning outside formal sessions. Link that cautiously to the hidden curriculum; the overview does not use that term."
  author-agent-dialogue: "Raise it when change is confined to content. Ask: \"What do students learn from how this is run, not only from what is taught?\" Avoid treating the informal curriculum as unimportant."
- component: advancehe/student-success-2024/impacts.learning-environments
  forPractitioner: { text: "Design spaces, technology and resources, formal and informal, so that they support the way students actually learn.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect places, tools and resources that make it easier for you to learn, in class and outside it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the four places the series has its effect. Note it covers informal spaces as well as classrooms. Link it to the flexible learning area."
  author-agent-dialogue: "Raise it when a space or tool gets in the way. Ask: \"Where and with what do students actually study, and does it work?\" Avoid assuming more technology is better."
- component: advancehe/student-success-2024/impacts.learning-communities
  forPractitioner: { text: "Bring students and staff into the communities of their subject and profession, inside and beyond the institution.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You become part of communities of people who share your subject or profession, at your university and beyond it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the four places the series has its effect. The overview does not use the word belonging here; the link to belonging is our reading (the wheel prints BELONGING; Part E)."
  author-agent-dialogue: "Raise it when a student feels isolated in their subject. Ask: \"Who else is working on this, and how could you join them?\" Avoid assuming every student wants the same community."
- component: advancehe/student-success-2024/impacts.teaching-quality
  forPractitioner: { text: "Treat the design, delivery and evaluation of teaching as the base for any improvement, and review each of the three.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect teaching that is well planned, well delivered and checked to see that it works for you.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the four places the series has its effect. Note the issuer calls teaching quality core to any theme. Do not equate quality with student satisfaction scores."
  author-agent-dialogue: "Raise it when an initiative ignores teaching itself. Ask: \"How will the teaching change, and how will you know it is better?\" Avoid judging individual teachers."
```

### M3 Conditions
<!-- label: editorial; status: drafted; basis: discussion. Ours, every field. -->
```yaml
- component: advancehe/student-success-2024/areas.assessment
  theme: theme:assessment-for-learning
  holdsWhen: "Assessment tasks, their preparation and their feedback are planned as learning, and students act on feedback before the next task."
  signs: ["feedback arrives in time to be used on a later task", "tasks reward steady work over cramming", "students can say what an assessment taught them"]
  absentWhen: "Assessment arrives at the end, measures without teaching, and feedback comes too late to use."
  contextSteer: "Build in a chance to practise and get feedback before anything is judged, and say how the task helps the learner learn."
  basis: ours
- component: advancehe/student-success-2024/areas.employability
  theme: theme:transition
  holdsWhen: "Students meet the link between their study and life after it within the course, and are prepared for the moves they will make."
  signs: ["modules name where their learning is used beyond the course", "students take part in work-related or community tasks", "students can describe their next step and how the course prepares them"]
  absentWhen: "Life after study is left to an optional service, and students cannot connect their learning to it."
  contextSteer: "Link the topic to a real use beyond study, in work or the community, and to the learner's next step."
  basis: ours
- component: advancehe/student-success-2024/areas.access-retention-attainment-progression
  theme: theme:equitable-participation
  holdsWhen: "Students from every group enter, continue, achieve and progress at similar rates, and gaps that appear are acted on."
  signs: ["data on each stage are reviewed by student group", "actions name a gap and what will change", "students who struggle are noticed early"]
  absentWhen: "Some groups fall away at each stage, and the pattern is accepted as normal."
  contextSteer: "Assume no shared starting point: explain what others may take for granted and show the way through each stage."
  basis: ours
- component: advancehe/student-success-2024/areas.student-partnership
  theme: theme:student-voice-partnership
  holdsWhen: "Students and staff, and the institution and its student body, talk regularly and openly, and these talks lead to changes."
  signs: ["students sit on groups that make decisions", "students hear what changed because of their views", "students talk with each other about their learning in organised ways"]
  absentWhen: "Students are asked for views now and then, and hear nothing back."
  contextSteer: "Invite the learner to say what they think and show how their view could shape what comes next."
  basis: ours
- component: advancehe/student-success-2024/areas.internationalising
  theme: theme:intercultural-engagement
  holdsWhen: "All students meet global perspectives and work across cultures as part of their course."
  signs: ["sources and cases come from more than one country", "students work in culturally mixed groups by design", "tasks ask how an issue plays out elsewhere"]
  absentWhen: "The curriculum assumes one national setting, and intercultural learning happens only by chance."
  contextSteer: "Include a perspective or case from another part of the world and ask how it changes the picture."
  basis: ours
- component: advancehe/student-success-2024/areas.flexible-learning
  theme: theme:flexibility
  holdsWhen: "Students can choose some of the time, place, pace, route or content of their learning, and the tools and rules support that choice."
  signs: ["materials and sessions can be reached at other times", "students pick between routes or topics", "policies allow study in more than one mode"]
  absentWhen: "Learning happens at one time, in one place and in one way, and those who cannot fit it miss out."
  contextSteer: "Offer the learner a choice of route, pace or format, and make clear what stays fixed."
  basis: ours
- component: advancehe/student-success-2024/areas.esd
  theme: theme:global-citizenship
  holdsWhen: "Students meet sustainability issues within their subject and practise acting on them."
  signs: ["tasks link the subject to a global challenge", "students weigh the values at stake, not only facts", "students propose action as part of their work"]
  absentWhen: "Sustainability is absent or left to one optional module, and students cannot link it to their field."
  contextSteer: "Connect the topic to a global challenge and ask the learner what a responsible response would be."
  basis: ours
- component: advancehe/student-success-2024/areas.inclusive
  theme: theme:anticipating-difference
  holdsWhen: "Teaching and materials are designed for the range of students expected, so that access does not depend on asking."
  signs: ["materials come in more than one format by default", "tasks offer more than one way to show learning", "few students need individual arrangements"]
  absentWhen: "The design suits a typical student, and others must ask for exceptions one by one."
  contextSteer: "Design for the whole range of learners from the start: offer more than one way in and do not assume one kind of student."
  basis: ours
- component: advancehe/student-success-2024/areas.enterprise
  theme: theme:entrepreneurial-mindset
  holdsWhen: "Students take initiative on real or realistic opportunities within their course."
  signs: ["tasks ask students to find a need and propose a response", "students try ideas and learn from what fails", "enterprise appears outside business subjects"]
  absentWhen: "Initiative is not asked for, and enterprise is seen as a business-school topic."
  contextSteer: "Ask the learner to spot an opportunity or need in the topic and propose something they could do about it."
  basis: ours
- component: advancehe/student-success-2024/principles.inclusivity
  theme: theme:equitable-participation
  holdsWhen: "Approaches are designed in advance so that every student and member of staff can participate fully, and gaps are acted on."
  signs: ["plans name who might be left out and how that is prevented", "staff and students report taking part on equal terms", "inclusive values are stated and used in decisions"]
  absentWhen: "Inclusion is reactive, and some people are left out until they complain."
  contextSteer: "Plan for every learner to take part fully, and remove barriers before they arise."
  basis: ours
- component: advancehe/student-success-2024/principles.student-centred
  theme: theme:agency-self-actualisation
  holdsWhen: "Students make choices about their study and set their own goals, and the course respects those goals."
  signs: ["students are asked about their own goals", "there are real choices of route or focus", "progress is discussed against the student's goals as well as grades"]
  absentWhen: "One route and one measure of success apply to all, and students follow rather than steer."
  contextSteer: "Ask the learner what they want from the topic and let that shape how they approach it."
  basis: ours
- component: advancehe/student-success-2024/principles.agility
  theme: theme:contextual-adaptation
  holdsWhen: "Structures and processes are changed within a reasonable time when the needs they serve change."
  signs: ["processes are reviewed on a cycle and when needs change", "changes cite the shift that prompted them", "staff can adjust practice without long approval chains"]
  absentWhen: "Structures stay fixed long after needs have moved on."
  contextSteer: "Show how the topic or practice is changing and invite the learner to adapt their approach."
  basis: ours
- component: advancehe/student-success-2024/principles.interconnectivity
  theme: theme:interconnectivity
  holdsWhen: "Work in one area draws on and feeds others, and people across disciplines and places connect over it."
  signs: ["projects name more than one area", "staff from different units work together on them", "students meet links between subjects"]
  absentWhen: "Each area runs separately, and the same problems are solved more than once."
  contextSteer: "Point out where the topic links to another subject or area, and invite the learner to make the connection."
  basis: ours
- component: advancehe/student-success-2024/principles.collaboration
  theme: theme:whole-institution
  holdsWhen: "Stakeholders inside and outside the institution plan and carry out the work together and share its ownership."
  signs: ["partners outside the institution help design activity", "students share in decisions and their delivery", "credit and responsibility are shared"]
  absentWhen: "One group decides and others are informed."
  contextSteer: "Set the task up as shared work in which the learner and others each own a part."
  basis: ours
- component: advancehe/student-success-2024/commitments.leadership-strategy
  theme: theme:whole-institution
  holdsWhen: "A shared aim for student outcomes is stated, owned by leaders and backed with resources."
  signs: ["strategies name student outcomes and their owners", "budgets and workload follow the stated aims", "staff can say what the shared aim is"]
  absentWhen: "Aims are announced without resources, and staff meet them in their spare time."
  contextSteer: "Make the goal of the learning explicit and show what support is in place to reach it."
  basis: ours
- component: advancehe/student-success-2024/commitments.culture
  theme: theme:agency-self-actualisation
  holdsWhen: "Staff and students describe the setting as positive and act on their own initiative, and approaches consider the whole person."
  signs: ["staff and students take initiative without waiting to be told", "support looks at circumstances beyond study", "people describe the setting as positive"]
  absentWhen: "The culture is cautious, and people wait for permission and see only part of each other."
  contextSteer: "Write in a way that encourages the learner, takes account of their wider life and trusts them to act."
  basis: ours
- component: advancehe/student-success-2024/commitments.shared-responsibility
  theme: theme:whole-institution
  holdsWhen: "Staff and students can each state their responsibilities in learning, and both sides meet them."
  signs: ["course documents say what staff and students each do", "students can describe their own role", "missed responsibilities are discussed on both sides"]
  absentWhen: "Roles are vague, and each side blames the other when things go wrong."
  contextSteer: "Say plainly what the learner is expected to do and what support they can expect in return."
  basis: ours
- component: advancehe/student-success-2024/commitments.scholarship-evidence
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Decisions about teaching cite research or institutional data, and staff can name what informed them."
  signs: ["proposals cite research or data", "staff read and discuss teaching research", "local data are shared with those who teach"]
  absentWhen: "Practice rests on habit and anecdote, and data stay with administrators."
  contextSteer: "Ground claims about learning in evidence and show the learner where it comes from."
  basis: ours
- component: advancehe/student-success-2024/commitments.continual-development
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Staff and students take part in repeated cycles of reflection, planning, action and review, with time set aside for them."
  signs: ["development activity recurs and builds", "staff and students reflect together", "reviews lead to a next plan"]
  absentWhen: "Development is occasional and isolated, and lessons are not carried forward."
  contextSteer: "End with a prompt for the learner to reflect on what they did and plan their next step."
  basis: ours
- component: advancehe/student-success-2024/commitments.evaluation-impact
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Activities have a plan for showing their effect on students, using more than one measure and method, and the results are recorded."
  signs: ["evaluation plans exist before activity starts", "measures include belonging or wellbeing as well as outcomes", "results lead to decisions"]
  absentWhen: "Activity is judged by effort or by one figure, and its effect is unknown."
  contextSteer: "Give the learner a way to check whether they have achieved what they set out to do."
  basis: ours
- component: advancehe/student-success-2024/impacts.curriculum
  theme: theme:hidden-curriculum
  holdsWhen: "Changes to content, design, delivery and assessment are made together, and informal learning is considered alongside formal."
  signs: ["course reviews cover design, delivery and assessment together", "informal and extra-curricular learning are named in plans", "unwritten expectations are made explicit"]
  absentWhen: "Only the content list is revised, and what students learn informally is ignored."
  contextSteer: "Make explicit what the learner is expected to learn beyond the content itself, including how to go about it."
  basis: ours
- component: advancehe/student-success-2024/impacts.learning-environments
  theme: theme:flexibility
  holdsWhen: "Spaces, technology and resources, in and out of class, are chosen for how they support learning and are available when students need them."
  signs: ["informal study spaces are available and used", "technology is chosen for a teaching purpose", "students can reach resources when they study"]
  absentWhen: "Spaces and tools are inherited or chosen for cost alone, and students work around them."
  contextSteer: "Name the tools and spaces the learner will need and how to get to them."
  basis: ours
- component: advancehe/student-success-2024/impacts.learning-communities
  theme: theme:belonging-mattering
  holdsWhen: "Students and staff take part in subject and professional communities that reach beyond their own course."
  signs: ["students attend subject or professional events", "staff and students learn together in shared groups", "links with communities outside the institution are used in teaching"]
  absentWhen: "Learning happens course by course, and students do not meet the wider community of their subject."
  contextSteer: "Point the learner to the wider community of the subject and invite them to take part."
  basis: ours
- component: advancehe/student-success-2024/impacts.teaching-quality
  theme: theme:evidence-informed-enhancement
  holdsWhen: "Teaching is planned, delivered and evaluated with care, and evaluation leads to changes."
  signs: ["teaching is reviewed by peers or students and changed as a result", "session plans state their aims", "evaluation covers design and delivery"]
  absentWhen: "Teaching is left to individual habit, and no one checks whether it works."
  contextSteer: "State the aim of the learning clearly, structure it with care and include a way to check it worked."
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
  codes: []   # the table names no dimension
  fellowship: { span: { start: 10029, end: 10262 }, source: "Advance HE invites lecturers, teachers and learning support staff to evidence their use of this, or other Advance HE frameworks in the series, when applying for Fellowship, in recognition of their commitment to professional practice.", page: 20, note: "an invitation, not an obligation: not an S4 statement" }
inferred:
  - { from: "advancehe/student-success-2024/principles.inclusivity", to: "theme:edi", rel: related, basis: inferred, note: "full and equitable participation of students and staff is the series' inclusion principle" }
  - { from: "advancehe/student-success-2024/commitments.evaluation-impact", to: "theme:wellbeing", rel: related, basis: inferred, note: "the issuer lists wellbeing and belonging data among the measures of impact" }
  - { from: "advancehe/student-success-2024/impacts.learning-environments", to: "theme:digital", rel: related, basis: inferred, note: "technology is named among the elements of learning environments" }
  - { from: "advancehe/student-success-2024/impacts.learning-communities", to: "theme:belonging-mattering", rel: related, basis: inferred, note: "the wheel prints BELONGING and MATTERING; the text does not tie them to any item" }
```

### M6 Practice themes carried
<!-- label: both; status: drafted; basis: discussion -->
```yaml
- { id: theme:assessment-for-learning, tier: practice, working: "assessment and its feedback are designed so that students learn through them", carriedBy: ["advancehe/student-success-2024/areas.assessment"], status: provisional }
- { id: theme:transition, tier: practice, working: "students are prepared and supported as they move into, through and on from study", carriedBy: ["advancehe/student-success-2024/areas.employability"], status: provisional }
- { id: theme:equitable-participation, tier: practice, working: "every student, and member of staff, can take part fully and on fair terms", carriedBy: ["advancehe/student-success-2024/areas.access-retention-attainment-progression", "advancehe/student-success-2024/areas.inclusive", "advancehe/student-success-2024/principles.inclusivity"], status: provisional }
- { id: theme:student-voice-partnership, tier: practice, working: "a range of voices, students' included, shapes decisions and is answered", carriedBy: ["advancehe/student-success-2024/areas.student-partnership", "advancehe/student-success-2024/principles.collaboration"], status: provisional }
- { id: theme:intercultural-engagement, tier: practice, working: "people from different cultures meet, work together and learn from each other", carriedBy: ["advancehe/student-success-2024/areas.internationalising"], status: provisional }
- { id: theme:global-citizenship, tier: practice, working: "learners prepare to act responsibly on shared global challenges", carriedBy: ["advancehe/student-success-2024/areas.internationalising", "advancehe/student-success-2024/areas.esd"], status: provisional }
- { id: theme:flexibility, tier: practice, working: "learners choose how, what, when and where they learn, with tools, spaces and rules that allow it", carriedBy: ["advancehe/student-success-2024/areas.flexible-learning", "advancehe/student-success-2024/impacts.learning-environments"], status: provisional }
- { id: theme:anticipating-difference, tier: practice, working: "teaching is designed in advance for the range of students", carriedBy: ["advancehe/student-success-2024/areas.inclusive"], status: provisional }
- { id: theme:entrepreneurial-mindset, tier: practice, working: "learners come to see themselves as able to act on ideas, and learn from setbacks", carriedBy: ["advancehe/student-success-2024/areas.enterprise"], status: provisional }
- { id: theme:agency-self-actualisation, tier: practice, working: "people grow into, use and trust their own judgement", carriedBy: ["advancehe/student-success-2024/principles.student-centred", "advancehe/student-success-2024/commitments.culture"], status: provisional }
- { id: theme:contextual-adaptation, tier: practice, working: "practice adapts to the setting and its students, not the reverse", carriedBy: ["advancehe/student-success-2024/principles.agility"], status: provisional }
- { id: theme:interconnectivity, tier: practice, working: "work in one area, discipline or place is linked to others", carriedBy: ["advancehe/student-success-2024/principles.interconnectivity", "advancehe/student-success-2024/impacts.learning-communities"], status: provisional }
- { id: theme:whole-institution, tier: practice, working: "the institution's strategy, quality processes, estate and staff pull together towards one aim", carriedBy: ["advancehe/student-success-2024/principles.collaboration", "advancehe/student-success-2024/commitments.leadership-strategy", "advancehe/student-success-2024/commitments.shared-responsibility"], status: provisional }
- { id: theme:evidence-informed-enhancement, tier: practice, working: "practice is mapped, its effects are evaluated and it is improved on that evidence", carriedBy: ["advancehe/student-success-2024/commitments.scholarship-evidence", "advancehe/student-success-2024/commitments.continual-development", "advancehe/student-success-2024/commitments.evaluation-impact", "advancehe/student-success-2024/impacts.teaching-quality"], status: provisional }
- { id: theme:hidden-curriculum, tier: practice, working: "the unwritten rules of study are made explicit", carriedBy: ["advancehe/student-success-2024/impacts.curriculum"], status: provisional }
- { id: theme:belonging-mattering, tier: practice, working: "students see that their experience and needs count", carriedBy: ["advancehe/student-success-2024/impacts.learning-communities"], status: provisional }
```

## Part B Terminology

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: student-success, definition: "a many-sided outcome of study: achievement, moving on to work, enterprise or further study, deeper engagement with a subject, skills and personal growth, including activity outside the course", scopeNote: "the series' organising idea; each student's own measure of success counts", category: concept, practices: [learning-and-teaching] }
- { slug: student-journey, definition: "the path a student takes into, through and beyond study, shaped differently for each", scopeNote: "used for the individual route that success factors shape", category: concept, practices: [learning-and-teaching] }
- { slug: educators-and-related-staff, definition: "everyone who contributes to student learning or directly improves student outcomes, not only those who teach", scopeNote: "one of the three perspectives each model in the series takes; perspective:educators", category: role, practices: [learning-and-teaching] }
- { slug: operational-commitments, definition: "the ways of running an institution that the series says student success depends on", scopeNote: "six in the text; the wheel also prints Belonging and Mattering in the same ring", category: concept, practices: [learning-and-teaching] }
- { slug: guiding-principles, definition: "the five values every model in the series supports", scopeNote: "Inclusivity, Student-centred, Agility, Interconnectivity, Collaboration", category: concept, practices: [learning-and-teaching] }
```

### B2a Terms as the issuer uses them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: student-success, form: "student success", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: student-journey, form: "student journey", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: educators-and-related-staff, form: "educators and related staff", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: operational-commitments, form: "Operational commitments", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: guiding-principles, form: "guiding principles of practice", lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the model names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term takes a meaning of its own in one component.

### B4 Relations
```yaml
- { rel: related, from: student-journey, to: student-success, note: "success factors shape each student's journey (p. 3)" }
- { rel: related, from: guiding-principles, to: operational-commitments, note: "both are shared by every model in the series and drawn as rings of one wheel" }
- { rel: related, from: educators-and-related-staff, to: student-success, note: "defined by contribution to learning or outcomes (p. 5)" }
```

### B5 Rules
- student success: use it in the issuer's wide sense (achievement, moving on, engagement, skills, growth, extra-curricular activity), not as grades or continuation alone.
- areas: cite the area's own model for any detail; the overview gives each area one line only.
- Belonging and Mattering: do not list them as commitments; the wheel prints them but the text does not (Part E).

## Part C Process

### C0 Formality
`not-applicable`: the model sets conditions and uses, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE
  title: "Enhancing student success in higher education"
  edition: "digital edition, 2024"
  year: 2024
  url: "https://www.advance-he.ac.uk (the series page not reached; D3)"
  retrieved: "PDF supplied by Abbott, 4 October 2026"
  licence: "none stated; held by permission (D-std-0019)"
  tier: primary
  readVia: direct
  held: 50e634264e6dbfa1ee0ca297a9e20e6c1dfaf2e4805f3b87bc6c18a7a2794be2
  heldFiles: ["txt/advance-he-2024-enhancing-student-success-higher-education-standard.txt", "txt/advance-he-2024-enhancing-student-success-higher-education-standard.norm.txt", "records/advance-he-2024-enhancing-student-success-higher-education-standard.held.json", "pdf/advance-he-2024-enhancing-student-success-higher-education-standard.pdf"]
  citedIn: [0.2, S1, S2, S3, S4, M1, M2, M4, M5, B1]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: "2026-10-04", pass: P1, outcome: "used for every section; figure pages read as images (text layer and page images)" }
```

### D3 Wanted sources
```yaml
- { citation: "Advance HE, Student Success Frameworks (series web page), current", settles: ["S8", "S7"], asked: not yet, state: wanted }
- { citation: "Advance HE (2024) Student Engagement through Partnership (Student Success Frameworks)", settles: ["S7", "M5"], asked: not yet, state: wanted }
- { citation: "Advance HE (2024) Flexible Learning in HE (Student Success Frameworks)", settles: ["S7", "M5"], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- Front matter, S1: no year or copyright notice is printed in the file; 2024 is taken from the PDF's creation date (2 July 2024; modified 3 July 2024). `copyrightNotice: none-stated`.
- Held text: held by Abbott's permission (4 October 2026, 05:03: "Yes full permission"; D-std-0019, as D-std-0013); private, never published.
- M1 figure: the brief asked for `form: list`; the pages show a wheel (pp. 3, 11, 12, 14, 16, 18): the nine areas as a middle ring, the principles as a dark ring around them, the commitments as an outer ring, the impacts as an inner ring around a hub of Institution, Educators+ and Students. Recorded as `form: wheel`; every label is also printed as text, so the components are read from the text layer. For Abbott: confirm wheel or list.
- M2 order: within each facet, the order printed on the text pages (left column top to bottom, then right). The text layer agrees except on p. 13, where it reads Flexible, Enterprise, ESD, the metrics note, Inclusive; the page reads Flexible, ESD, Inclusive (left column), Enterprise (right column). The wheel's clockwise order from the top differs: areas Enterprise and Entrepreneurship, Flexible Learning, Education for Sustainable Development, Access Retention Attainment and Progression, Inclusive Learning and Teaching, Assessment, Internationalising, Student Engagement through Partnership, Employability; principles Inclusivity, Agility, Collaboration, Student-centred, Interconnectivity; commitments Continual development, Shared responsibility, (MATTERING), Evaluation and impact, Scholarship and evidence, Culture, (BELONGING), Leadership and strategy; impacts Curriculum, Learning communities, Learning environment(s), Teaching quality.
- M2 areas: the text says "nine strategic areas"; the area names in the wheel are shorter than the text headings (for example "Assessment" beside "Enhancing Assessment in HE", "Learning environment" beside "Learning environments"); labels are the text headings, as the brief asked.
- M1 commitments: the wheel's outer ring prints BELONGING and MATTERING, in larger type, among the six commitments; the text lists six commitments and names belonging only as a data source under Evaluation and impact. They are not held as components. For Abbott: are Belonging and Mattering commitments, a frame around them, or a design element?
- M2 explainedBy: links marked `inferred` are std's reading; the source does not tie those sentences to the component.
- S4: the three "the series:" lists are function lines (mood declarative, force describes), not uses; their audiences (institutions, staff, Students' Unions) are not axes of this overview, so `perspective: none`, and the audience is in the stem and `heading`.
- S4 "promoting a need for:" (the lead-in to the six commitments): read as descriptive, not obliging. It says what the series promotes; the obligation sits in the sentence before it ("necessitates", S4 commitments.frame). The six commitments are therefore components, not statements.
- S4 commitments.frame: "necessitates" is not in D-std-0016's list; read as must beside "necessary" (proposed). For Abbott: rule.
- S4 commitments.culture: the Culture commitment's first sentence obliges ("requires"); held both as an S4 statement and as the component's explainedBy span.
- M5, S7: the overview has a PSF paragraph and the Fellowship invitation but no table and no named dimension; `codes: []`, and no `alignsWith` to the PSF dimensions document.
- S6: each area carries its sector theme, basis stated (the overview names the area). Inclusive Learning and Teaching carries theme:edi, the series' id for inclusion.
- S7: two area models are not held: Student Engagement through Partnership and Flexible Learning in HE (D3). Their targets are written `none-held: <title>`.
- M6: proposed practice themes (new): theme:assessment-for-learning, theme:equitable-participation, theme:global-citizenship, theme:flexibility, theme:entrepreneurial-mindset, theme:interconnectivity, theme:whole-institution, theme:whole-institution, theme:evidence-informed-enhancement. All themes are provisional until the shared theme register exists (Abbott, 05:09).
- M2 impacts.curriculum: carrying theme:hidden-curriculum rests on the issuer's "informal curricula"; the overview does not use the term. For Abbott: keep, or coin a curriculum theme.
- D3: Advance HE's series web page (current status, the full list of frameworks) not reached; wanted.

---

## Change notes
- 0.1.1, 2026-10-04 09:26: practice themes aligned across the series by std (10 id(s) renamed by tools/theme_merges.json; the old ids are aliases in the shared theme register); rebuilt on builder 0.2.1. Model template 0.3.0-draft, builder 0.2.1: 24 components, 0 open segments, 16 statements, 16 practice themes.
- 0.1.0, 2026-10-04 09:21: first built (Abbott, 09:08: "Use your template model and refine as you go"; D-std-0018). Model template 0.2.0-draft, builder 0.2.0: 24 components, 0 open segments, 16 statements, 17 practice themes.
