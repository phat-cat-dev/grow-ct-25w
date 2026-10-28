---
id: std:doc:qaa-fqheis-2024-framework
title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies: the FQHEIS"
profile: standards/framework
profileVersion: 0.1.6-draft
issuer: The Quality Assurance Agency for Higher Education (QAA)
kind: qualification-framework
jurisdiction: [Scotland]
subjectScope: universal
subjects: []
edition: 2nd edition, updated February 2024
published: 2024-02-21
status: current   # as at the held text (Part E)
supersedes: "the first edition (2014)"
heldText: { method: sha256-bytes, raw: 229532f8f0adf1a3c72ee782316cdc85c3d2250217bb6f065a807e69c0d2ca72, normalised: b37faa2a285c74257df9fa5b46f29ba7b7ec2f11a7bafcd214789f35b325f1b5 }   # the same held text as std:doc:qaa-fheq-2024-framework
original: { method: sha256-bytes, pdf: 249d3637cc31612e25748b02513f912d5e0c9712851809c3e7bd9552fbd64621, held: no }
frameworkKind: qualification
nations: [Scotland]
levels: [fqheis:7, fqheis:8, fqheis:9, fqheis:10, fqheis:11, fqheis:12]   # SCQF numbering; 11 and 12 share the FHEQ's descriptors (S5)
awards: [CertHE, DipHE, bachelor's non-honours, bachelor's with honours, master's, doctorate]
credit: "see std:doc:qaa-fheq-2024-framework (Annex C, Scotland column)"
licence: none read yet
parts:
  S: "full for the FQHEIS's own descriptors; the shared descriptors and the common material are in std:doc:qaa-fheq-2024-framework"
  B: "see std:doc:qaa-fheq-2024-framework"
  C: "see std:doc:qaa-fheq-2024-framework"
pins: { structure: 0.13.0-draft, template: 0.6.1-draft, runFrame: 0.1.1-draft, runLayer: 0.5.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0047
passes:
  P1: "2026-10-03, std (claude.ai, META Project): read with the FHEQ at 04:35; split into its own document at 05:24 (D-std-0010)"
  P2: "skipped: read direct from the issuer's PDF"
  P3: open
version: 0.2.1
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the standards/framework variant (profile 0.1.6-draft), with the level-language section SL -->
# The Frameworks for Higher Education Qualifications (QAA, 2024): the FQHEIS

> Run 0047, P1 by std. **One document per framework** (Abbott, 05:20; D-std-0010). This document holds the Framework for Qualifications of Higher Education Institutions in Scotland: its four own descriptors (4.11, 4.13, 4.14, 4.16) and its level language. QAA publishes it in one document with the FHEQ. The master's and doctoral descriptors (4.17, 4.18) are common to both frameworks and are held once in `std:doc:qaa-fheq-2024-framework`, as is the material common to both (sections 2 to 6, Annexes B to D, Table 1, Annex C, the Definitions); this document points to them. The issuer's words are held in the source library repo only (`wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.norm.txt`); every statement points into them by character span.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The FQHEIS: QAA's framework for higher education qualifications awarded in Scotland, SCQF Levels 7 to 12, part of the Scottish Credit and Qualifications Framework. Reach for it to say what a holder of a Scottish higher education qualification has shown at the threshold and what a typical holder can also do, level by level, including the two steps the FHEQ does not have: the DipHE and the non-honours bachelor's degree.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Six levels, numbered on the SCQF (7 to 12): CertHE (7), DipHE (8), bachelor's non-honours (9), bachelor's with honours (10), master's (11) and doctorate (12). The first four have descriptors of their own, here; master's and doctorate share the FHEQ's text. Each descriptor has the two parts the Frameworks use everywhere: outcomes demonstrated for the award (the threshold) and the abilities a typical holder will have. Below honours the Scottish descriptors are fuller than the FHEQ's: they name materials and techniques, ICT and the handling of data, and they set the context in which skills are applied (clearly defined, generally well defined, then professional). The honours descriptor asks more than the FHEQ's: the subject as a whole and its links, emerging issues at the forefront, how knowledge is developed, and "some originality and creativity".

## Part S Standard

### S1 Identity
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies (the FQHEIS within it)"
edition: 2nd edition, updated February 2024
dates: { published: 2024-02-21, other: ["first edition 2014"] }
kind: qualification-framework
jurisdiction: [Scotland]
authority: reference   # degree-awarding bodies in Scotland award in accordance with it (2.2); it is part of the SCQF (2.23)
licence: none read yet
copyrightNotice: "© The Quality Assurance Agency for Higher Education 2024"
```

### S2 Purpose and scope
```yaml
governs: the levels of higher education qualifications in Scotland and the generic outcomes of the main qualification at each
appliesTo: { awards: [CertHE, DipHE, bachelor's non-honours, bachelor's with honours, master's, doctorate], levels: [fqheis:7, fqheis:8, fqheis:9, fqheis:10, fqheis:11, fqheis:12], providers: degree-awarding bodies in Scotland }
whoMustUse: "degree-awarding bodies in Scotland (2.2; How the Frameworks are used); the provider rules are in std:doc:qaa-fheq-2024-framework"
howUsed: [positioning, designing, approving, assessing, awarding, titling, reviewing]
doesNot: "specific subjects (4.1)"
beneficiary: the student
statedScope: "generic: the full range of disciplines (4.1)"
statedSubjects: none-stated
```

### S3 Structure
```yaml
components:
  - { number: "4.11", componentType: descriptor, heading: "4.11 Descriptor for a higher education qualification at SCQF Level 7 on the FQHEIS Certificate of Higher Education", level: fqheis:7 }
  - { number: "4.13", componentType: descriptor, heading: "4.13 Descriptor for a higher education qualification at SCQF Level 8 on the FQHEIS Diploma of Higher Education", level: fqheis:8 }
  - { number: "4.14", componentType: descriptor, heading: "4.14 Descriptor for a higher education qualification at SCQF Level 9 on the FQHEIS Bachelor's (non-honours) degree in Scotland", level: fqheis:9 }
  - { number: "4.16", componentType: descriptor, heading: "4.16 Descriptor for a higher education qualification at SCQF Level 10 on the FQHEIS Bachelor's degree with honours in Scotland", level: fqheis:10 }
  - { number: "4.16.b9", componentType: stem, parent: "4.16", heading: "applying skills in professional contexts that require (three items)" }
  - { number: "4.17", componentType: shared-descriptor, heading: "4.17 master's (SCQF 11; shared)", level: fqheis:11, heldIn: "std:doc:qaa-fheq-2024-framework, statements qaa/fheq-2024/4.17.*" }
  - { number: "4.18", componentType: shared-descriptor, heading: "4.18 doctorate (SCQF 12; shared)", level: fqheis:12, heldIn: "std:doc:qaa-fheq-2024-framework, statements qaa/fheq-2024/4.18.*" }
excluded:
  - { number: "4.10, 4.12, 4.15", heading: "the FHEQ's own descriptors", kind: "other: std:doc:qaa-fheq-2024-framework" }
  - { number: "1 to 3, 4.1 to 4.9, 5, 6, Annexes A to D", heading: "the material common to both frameworks", kind: "other: held once in std:doc:qaa-fheq-2024-framework" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. 35 records, the FQHEIS's own descriptors. Force: `threshold` for outcomes demonstrated for the award (4.2); `will` for typical holders (4.3). -->
```yaml
- id: qaa/fqheis-2024/4.11.b1
  locator: { number: "4.11.b1", headingPath: ["4.11 CertHE (SCQF 7)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 43329, end: 43488 }
  source: "an outline knowledge of the scope and main areas of the subject(s) and its links with related subjects, and a more extensive knowledge of some of the key areas"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:7
  dimension: threshold-outcomes
  award: "a Certificate of Higher Education in Scotland"
  appliesTo: "the award of a Certificate of Higher Education in Scotland"
  addressee: student
  verbs: []
  about: "outline of the subject, some areas in more depth"
  themes: [none]
  paraphrase: "Knows the scope and main areas of the subject in outline, how it links to related subjects, and some key areas more fully."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.11.b2
  locator: { number: "4.11.b2", headingPath: ["4.11 CertHE (SCQF 7)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 43493, end: 43556 }
  source: "an understanding of the major theories, principles and concepts"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:7
  dimension: threshold-outcomes
  award: "a Certificate of Higher Education in Scotland"
  appliesTo: "the award of a Certificate of Higher Education in Scotland"
  addressee: student
  verbs: []
  about: "major theories and concepts"
  themes: [none]
  paraphrase: "Understands the subject's major theories, principles and concepts."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.11.b3
  locator: { number: "4.11.b3", headingPath: ["4.11 CertHE (SCQF 7)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 43561, end: 43648 }
  source: "familiarity with some of the routine materials, techniques and practices of the subject"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:7
  dimension: threshold-outcomes
  award: "a Certificate of Higher Education in Scotland"
  appliesTo: "the award of a Certificate of Higher Education in Scotland"
  addressee: student
  verbs: []
  about: "familiarity with routine materials and practices"
  themes: [none]
  paraphrase: "Is familiar with some of the subject's routine materials, techniques and practices."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.11.b4
  locator: { number: "4.11.b4", headingPath: ["4.11 CertHE (SCQF 7)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 43653, end: 43931 }
  source: "skills for the gathering, basic analysis, and presentation of routine information, ideas, concepts and quantitative and qualitative data within a clearly defined context; this will include the use of information and communications technology (ICT) as appropriate to the subject."
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:7
  dimension: threshold-outcomes
  award: "a Certificate of Higher Education in Scotland"
  appliesTo: "the award of a Certificate of Higher Education in Scotland"
  addressee: student
  verbs: [include]
  about: "gathering and presenting routine information"
  themes: [none]
  paraphrase: "Has the skills to gather, analyse at a basic level and present routine information, ideas and data within a clearly set context, using ICT where it suits the subject."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.11.b5
  locator: { number: "4.11.b5", headingPath: ["4.11 CertHE (SCQF 7)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 44011, end: 44188 }
  source: "use their knowledge of the subject and its techniques in a routine manner to evaluate and formulate a range of arguments and solutions to problems and issues of a routine nature"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:7
  dimension: wider-abilities
  award: "a Certificate of Higher Education in Scotland"
  appliesTo: "the award of a Certificate of Higher Education in Scotland"
  addressee: holder
  verbs: [use, evaluate, formulate]
  about: "routine use of knowledge on routine problems"
  themes: [none]
  paraphrase: "Uses subject knowledge and technique routinely to weigh and build arguments and answers to routine problems."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.11.b6
  locator: { number: "4.11.b6", headingPath: ["4.11 CertHE (SCQF 7)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 44193, end: 44316 }
  source: "communicate the results of their study and other work accurately and reliably, and within structured and coherent arguments"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:7
  dimension: wider-abilities
  award: "a Certificate of Higher Education in Scotland"
  appliesTo: "the award of a Certificate of Higher Education in Scotland"
  addressee: holder
  verbs: [communicate]
  about: "communicating results soundly"
  themes: [none]
  paraphrase: "Reports the results of study and other work accurately and reliably, in structured, coherent argument."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.11.b7
  locator: { number: "4.11.b7", headingPath: ["4.11 CertHE (SCQF 7)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 44321, end: 44391 }
  source: "undertake further learning within a structured and managed environment"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:7
  dimension: wider-abilities
  award: "a Certificate of Higher Education in Scotland"
  appliesTo: "the award of a Certificate of Higher Education in Scotland"
  addressee: holder
  verbs: [undertake]
  about: "further learning in a managed setting"
  themes: [none]
  paraphrase: "Goes on learning where the setting is structured and managed."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.11.b8
  locator: { number: "4.11.b8", headingPath: ["4.11 CertHE (SCQF 7)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 44396, end: 44599 }
  source: "apply their subject-related and transferable skills in contexts where individuals may have some limited personal responsibility, but the criteria for decisions and the scope of the task are well defined."
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:7
  dimension: wider-abilities
  award: "a Certificate of Higher Education in Scotland"
  appliesTo: "the award of a Certificate of Higher Education in Scotland"
  addressee: holder
  verbs: [apply]
  about: "skills where decisions are well defined"
  themes: [none]
  paraphrase: "Applies subject and transferable skills where personal responsibility is limited and the task and its decision criteria are clearly set."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.13.b1
  locator: { number: "4.13.b1", headingPath: ["4.13 DipHE (SCQF 8)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 47913, end: 48149 }
  source: "a knowledge and understanding of the scope and main areas of the subject(s) and its interactions with related subjects; detailed knowledge of some key areas which may include some knowledge of current issues in limited specialised areas"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:8
  dimension: threshold-outcomes
  award: "a Diploma of Higher Education in Scotland"
  appliesTo: "the award of a Diploma of Higher Education in Scotland"
  addressee: student
  verbs: [include]
  about: "scope of the subject, detail in key areas, current issues"
  themes: [none]
  paraphrase: "Knows and understands the subject's scope and main areas and its links to others, with detail in some key areas, possibly including current issues in a few specialised ones."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.13.b2
  locator: { number: "4.13.b2", headingPath: ["4.13 DipHE (SCQF 8)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 48154, end: 48313 }
  source: "familiarity and understanding of a range of the essential theories, principles and concepts and an awareness of major issues at the forefront of the subject(s)"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:8
  dimension: threshold-outcomes
  award: "a Diploma of Higher Education in Scotland"
  appliesTo: "the award of a Diploma of Higher Education in Scotland"
  addressee: student
  verbs: []
  about: "essential theories and issues at the forefront"
  themes: [none]
  paraphrase: "Is familiar with and understands a range of essential theories, principles and concepts, and is aware of major issues at the subject's forefront."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.13.b3
  locator: { number: "4.13.b3", headingPath: ["4.13 DipHE (SCQF 8)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 48318, end: 48429 }
  source: "familiarity and effective deployment of essential/routine materials, techniques and practices of the subject(s)"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:8
  dimension: threshold-outcomes
  award: "a Diploma of Higher Education in Scotland"
  appliesTo: "the award of a Diploma of Higher Education in Scotland"
  addressee: student
  verbs: []
  about: "effective use of essential materials and practices"
  themes: [none]
  paraphrase: "Is familiar with the subject's essential and routine materials, techniques and practices and uses them effectively."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.13.b4
  locator: { number: "4.13.b4", headingPath: ["4.13 DipHE (SCQF 8)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 48434, end: 48666 }
  source: "skills for the gathering, critical analysis and presentation of information, ideas, concepts and/or quantitative and qualitative data that is core to the subject(s); this will include the use of ICT as appropriate to the subject(s)."
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:8
  dimension: threshold-outcomes
  award: "a Diploma of Higher Education in Scotland"
  appliesTo: "the award of a Diploma of Higher Education in Scotland"
  addressee: student
  verbs: [include]
  about: "critical gathering and presentation of core information"
  themes: [none]
  paraphrase: "Has skills to gather, analyse critically and present the information, ideas and data at the subject's core, using ICT as suits it."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.13.b5
  locator: { number: "4.13.b5", headingPath: ["4.13 DipHE (SCQF 8)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 48728, end: 48916 }
  source: "use their knowledge, understanding and skills to critically evaluate and formulate evidence-based arguments and identify solutions to clearly-defined problems of a generally routine nature"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:8
  dimension: wider-abilities
  award: "a Diploma of Higher Education in Scotland"
  appliesTo: "the award of a Diploma of Higher Education in Scotland"
  addressee: holder
  verbs: [use, evaluate, formulate, identify]
  about: "evidence-based argument on defined problems"
  themes: [none]
  paraphrase: "Uses knowledge, understanding and skills to judge critically and build evidence-based arguments, and to find solutions to defined, mostly routine problems."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.13.b6
  locator: { number: "4.13.b6", headingPath: ["4.13 DipHE (SCQF 8)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 48921, end: 49037 }
  source: "communicate the results of their study and other work accurately and reliably using a range of specialist techniques"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:8
  dimension: wider-abilities
  award: "a Diploma of Higher Education in Scotland"
  appliesTo: "the award of a Diploma of Higher Education in Scotland"
  addressee: holder
  verbs: [communicate, using]
  about: "communicating with specialist techniques"
  themes: [none]
  paraphrase: "Reports what study and other work found, accurately and dependably, drawing on several specialist techniques."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.13.b7
  locator: { number: "4.13.b7", headingPath: ["4.13 DipHE (SCQF 8)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 49042, end: 49171 }
  source: "identify and address their own major learning needs within defined contexts and to undertake guided further learning in new areas"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:8
  dimension: wider-abilities
  award: "a Diploma of Higher Education in Scotland"
  appliesTo: "the award of a Diploma of Higher Education in Scotland"
  addressee: holder
  verbs: [identify, address, undertake]
  about: "own learning needs and guided learning"
  themes: [none]
  paraphrase: "Recognises and meets their own main learning needs in defined settings, and takes guided further learning in new areas."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.13.b8
  locator: { number: "4.13.b8", headingPath: ["4.13 DipHE (SCQF 8)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 49176, end: 49393 }
  source: "apply their subject-related and transferable skills in contexts where the scope of the task and the criteria for decisions are generally well defined, but where some personal responsibility and initiative is required."
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:8
  dimension: wider-abilities
  award: "a Diploma of Higher Education in Scotland"
  appliesTo: "the award of a Diploma of Higher Education in Scotland"
  addressee: holder
  verbs: [apply]
  about: "skills with some responsibility and initiative"
  themes: [none]
  paraphrase: "Applies subject and transferable skills where the task and its decision criteria are largely clear but some personal responsibility and initiative is needed."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.14.b1
  locator: { number: "4.14.b1", headingPath: ["4.14 bachelor's non-honours (SCQF 9)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 50511, end: 50877 }
  source: "a broad and comparative knowledge of the general scope of the subject, its different areas and applications, and its interactions with related subjects; a detailed knowledge of a defined subject or a more limited coverage of a specialist area balanced by a wider range of study; in each case, specialised study will be informed by current developments in the subject"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:9
  dimension: threshold-outcomes
  award: "a bachelor's degree without honours in Scotland"
  appliesTo: "the award of a bachelor's degree without honours in Scotland"
  addressee: student
  verbs: [informed]
  about: "broad and comparative knowledge, with depth"
  themes: [none]
  paraphrase: "Knows the subject broadly and comparatively, its areas, uses and links, with detailed knowledge of a defined subject or a narrower specialism balanced by breadth, informed by current developments."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.14.b2
  locator: { number: "4.14.b2", headingPath: ["4.14 bachelor's non-honours (SCQF 9)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 50882, end: 51124 }
  source: "a critical understanding of the essential theories, principles and concepts of the subject(s) and of the ways in which these are developed through the main methods of enquiry in the subject; an awareness of the provisional nature of knowledge"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:9
  dimension: threshold-outcomes
  award: "a bachelor's degree without honours in Scotland"
  appliesTo: "the award of a bachelor's degree without honours in Scotland"
  addressee: student
  verbs: [developed]
  about: "critical understanding of theories and how knowledge develops"
  themes: [none]
  paraphrase: "Understands critically the essential theories, principles and concepts and how the main methods of enquiry develop them, aware that knowledge is provisional."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.14.b3
  locator: { number: "4.14.b3", headingPath: ["4.14 bachelor's non-honours (SCQF 9)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 51129, end: 51271 }
  source: "familiarity and competence in the use of routine materials, practices and skills, and of a few that are more specialised, advanced and complex"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:9
  dimension: threshold-outcomes
  award: "a bachelor's degree without honours in Scotland"
  appliesTo: "the award of a bachelor's degree without honours in Scotland"
  addressee: student
  verbs: []
  about: "competence in routine and some advanced practices"
  themes: [none]
  paraphrase: "Is familiar and competent with routine materials, practices and skills and with a few more specialised, advanced and complex ones."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.14.b4
  locator: { number: "4.14.b4", headingPath: ["4.14 bachelor's non-honours (SCQF 9)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 51276, end: 51539 }
  source: "well-developed skills for the gathering, evaluation, analysis and presentation of information, ideas, concepts and quantitative and/or qualitative data, drawing on a wide range of current sources; this will include the use of ICT as appropriate to the subject(s)."
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:9
  dimension: threshold-outcomes
  award: "a bachelor's degree without honours in Scotland"
  appliesTo: "the award of a bachelor's degree without honours in Scotland"
  addressee: student
  verbs: [drawing, include]
  about: "well-developed skills with a wide range of sources"
  themes: [none]
  paraphrase: "Has well-developed skills to gather, evaluate, analyse and present information and data from a wide range of current sources, using ICT as suits the subject."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.14.b5
  locator: { number: "4.14.b5", headingPath: ["4.14 bachelor's non-honours (SCQF 9)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 51601, end: 51784 }
  source: "use their knowledge, understanding and skills, in both identifying and analysing problems and issues and in formulating, evaluating and applying evidence-based solutions and arguments"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:9
  dimension: wider-abilities
  award: "a bachelor's degree without honours in Scotland"
  appliesTo: "the award of a bachelor's degree without honours in Scotland"
  addressee: holder
  verbs: [use, identifying, analysing, formulating, evaluating, applying]
  about: "identifying problems and evidence-based solutions"
  themes: [none]
  paraphrase: "Uses knowledge, understanding and skills both to find and analyse problems and to build, test and apply evidence-based solutions and arguments."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.14.b6
  locator: { number: "4.14.b6", headingPath: ["4.14 bachelor's non-honours (SCQF 9)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 51789, end: 51981 }
  source: "communicate the results of their studies and other work accurately and reliably in a range of different contexts using the main specialist concepts, constructs and techniques of the subject(s)"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:9
  dimension: wider-abilities
  award: "a bachelor's degree without honours in Scotland"
  appliesTo: "the award of a bachelor's degree without honours in Scotland"
  addressee: holder
  verbs: [communicate, using]
  about: "communicating across contexts with the subject's concepts"
  themes: [none]
  paraphrase: "Reports results accurately and reliably in a range of contexts, using the subject's main specialist concepts and techniques."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.14.b7
  locator: { number: "4.14.b7", headingPath: ["4.14 bachelor's non-honours (SCQF 9)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 51986, end: 52132 }
  source: "identify and address their own learning needs, including being able to draw on a range of current research, development and professional materials"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:9
  dimension: wider-abilities
  award: "a bachelor's degree without honours in Scotland"
  appliesTo: "the award of a bachelor's degree without honours in Scotland"
  addressee: holder
  verbs: [identify, address, draw]
  about: "own learning needs, drawing on current research"
  themes: [none]
  paraphrase: "Recognises and meets their own learning needs, drawing on current research, development and professional materials."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.14.b8
  locator: { number: "4.14.b8", headingPath: ["4.14 bachelor's non-honours (SCQF 9)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 52137, end: 52359 }
  source: "apply their subject-related and transferable skills to contexts where criteria for decisions and the scope of the task may be well defined but where personal responsibility, initiative and decision-making is also required."
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:9
  dimension: wider-abilities
  award: "a bachelor's degree without honours in Scotland"
  appliesTo: "the award of a bachelor's degree without honours in Scotland"
  addressee: holder
  verbs: [apply]
  about: "skills with responsibility, initiative and decisions"
  themes: [none]
  paraphrase: "Applies subject and transferable skills where task and criteria may be clear but responsibility, initiative and decision-making are also needed."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b1
  locator: { number: "4.16.b1", headingPath: ["4.16 honours degree (SCQF 10)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 57015, end: 57275 }
  source: "a systematic, extensive and comparative knowledge and understanding of the subject(s) as a whole and its links to related subject(s); a detailed knowledge of a few specialisms and developments, some of which are at, or informed by, the forefront of the subject"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:10
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: student
  verbs: [informed]
  about: "systematic, extensive, comparative knowledge; specialisms at the forefront"
  themes: [none]
  paraphrase: "Knows and understands the subject as a whole systematically, extensively and comparatively, with its links, and a few specialisms in detail, some at or informed by the forefront."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b2
  locator: { number: "4.16.b2", headingPath: ["4.16 honours degree (SCQF 10)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 57280, end: 57441 }
  source: "a critical understanding of the established theories, principles and concepts, and of a number of advanced and emerging issues at the forefront of the subject(s)"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:10
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: student
  verbs: []
  about: "critical understanding of theory and emerging issues"
  themes: [none]
  paraphrase: "Understands critically the established theories, principles and concepts, and several advanced and emerging forefront issues."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b3
  locator: { number: "4.16.b3", headingPath: ["4.16 honours degree (SCQF 10)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 57446, end: 57629 }
  source: "a critical understanding of the uncertainty and limits of knowledge and how it is developed, and an ability to deploy established techniques of analysis and enquiry within the subject"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:10
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: student
  verbs: [developed, deploy]
  about: "limits of knowledge; established techniques"
  themes: [none]
  paraphrase: "Understands critically how uncertain and limited knowledge is and how it develops, and can use established techniques of analysis and enquiry."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b4
  locator: { number: "4.16.b4", headingPath: ["4.16 honours degree (SCQF 10)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 57634, end: 57783 }
  source: "a comprehensive knowledge and familiarity with essential and advanced materials, techniques and skills including some at the forefront of the subject"
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:10
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: student
  verbs: []
  about: "comprehensive command of essential and advanced techniques"
  themes: [none]
  paraphrase: "Knows comprehensively, and is familiar with, essential and advanced materials, techniques and skills, some at the forefront."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b5
  locator: { number: "4.16.b5", headingPath: ["4.16 honours degree (SCQF 10)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 57788, end: 58064 }
  source: "skills in identifying information needs, and in the systematic gathering, analysis and interpretation of ideas, concepts, qualitative and quantitative data, and information from a range of evaluated sources including current research, scholarly and/or professional literature."
  stem: none
  statementType: descriptor
  force: threshold
  level: fqheis:10
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: student
  verbs: [identifying]
  about: "identifying information needs and systematic gathering"
  themes: [none]
  paraphrase: "Can identify information needs and systematically gather, analyse and interpret ideas and data from varied sources they have evaluated, current research among them."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b6
  locator: { number: "4.16.b6", headingPath: ["4.16 honours degree (SCQF 10)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 58127, end: 58476 }
  source: "use their knowledge, understanding and skills in the systematic and critical assessment of a wide range of concepts, ideas and data (that may be incomplete), and in both identifying and analysing complex problems and issues; demonstrating some originality and creativity in formulating, evaluating and applying evidence-based solutions and arguments"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:10
  dimension: wider-abilities
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: holder
  verbs: [use, identifying, analysing, demonstrating, formulating, evaluating, applying]
  about: "systematic critical assessment with some originality"
  themes: [none]
  paraphrase: "Uses knowledge and skills to assess concepts, ideas and possibly incomplete data systematically and critically, to find and analyse complex problems, showing some originality and creativity in building, testing and applying evidence-based solutions."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b7
  locator: { number: "4.16.b7", headingPath: ["4.16 honours degree (SCQF 10)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 58481, end: 58643 }
  source: "communicate the results of their study and other work accurately and reliably using the full repertoire of the principal concepts and constructs of the subject(s)"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:10
  dimension: wider-abilities
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: holder
  verbs: [communicate, using]
  about: "communicating with the full repertoire of the subject"
  themes: [none]
  paraphrase: "Reports results accurately and reliably, using the full range of the subject's principal concepts and constructs."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b8
  locator: { number: "4.16.b8", headingPath: ["4.16 honours degree (SCQF 10)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 58648, end: 58875 }
  source: "systematically identify and address their own learning needs both in current and new areas, making use of research, development and professional materials as appropriate, including those related to the forefront of developments"
  stem: none
  statementType: descriptor
  force: will
  level: fqheis:10
  dimension: wider-abilities
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: holder
  verbs: [identify, address, making]
  about: "systematically meeting learning needs at the forefront"
  themes: [none]
  paraphrase: "Recognises and meets their own learning needs systematically, in current and new areas, using research, development and professional materials, including those at the forefront."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b9.1
  locator: { number: "4.16.b9.1", headingPath: ["4.16 honours degree (SCQF 10)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 59019, end: 59073 }
  source: "the exercise of personal responsibility and initiative"
  stem: qaa/fqheis-2024/4.16.b9
  statementType: descriptor
  force: will
  level: fqheis:10
  dimension: wider-abilities
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: holder
  verbs: []
  about: "personal responsibility and initiative"
  themes: [none]
  paraphrase: "Skills applied where personal responsibility and initiative are required."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b9.2
  locator: { number: "4.16.b9.2", headingPath: ["4.16 honours degree (SCQF 10)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 59076, end: 59129 }
  source: "decision-making in complex and unpredictable contexts"
  stem: qaa/fqheis-2024/4.16.b9
  statementType: descriptor
  force: will
  level: fqheis:10
  dimension: wider-abilities
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: holder
  verbs: []
  about: "decisions in complex, unpredictable contexts"
  themes: [none]
  paraphrase: "Skills applied where decisions are needed in complex and unpredictable contexts."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fqheis-2024/4.16.b9.3
  locator: { number: "4.16.b9.3", headingPath: ["4.16 honours degree (SCQF 10)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 59132, end: 59217 }
  source: "the ability to undertake further developments of a professional or equivalent nature."
  stem: qaa/fqheis-2024/4.16.b9
  statementType: descriptor
  force: will
  level: fqheis:10
  dimension: wider-abilities
  award: "a bachelor's degree with honours in Scotland"
  appliesTo: "the award of a bachelor's degree with honours in Scotland"
  addressee: holder
  verbs: [undertake]
  about: "further professional development"
  themes: [none]
  paraphrase: "Skills applied where further professional or equivalent development must be undertaken."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. The student versions name the qualification, never the framework or the issuer. -->
```yaml
- statement: qaa/fqheis-2024/4.11.b1
  forPractitioner: { text: "Scottish CertHE holders have shown outline knowledge of the subject's scope, main areas and neighbours, with fuller knowledge of some key areas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a Certificate of Higher Education in Scotland, you will have shown that you know the outline of your subject and its neighbours, and some key areas in more depth.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.11.b2
  forPractitioner: { text: "Scottish CertHE holders have shown understanding of the major theories, principles and concepts.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a Certificate of Higher Education in Scotland, you will have shown that you understand the main theories and ideas of your subject.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.11.b3
  forPractitioner: { text: "Scottish CertHE holders have shown familiarity with some routine materials, techniques and practices of the subject.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a Certificate of Higher Education in Scotland, you will have shown that you know your way round some of the subject's everyday materials and methods.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.11.b4
  forPractitioner: { text: "Scottish CertHE holders have shown skills in gathering, basic analysis and presenting routine information and data in a clearly defined context, ICT included as the subject needs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a Certificate of Higher Education in Scotland, you will have shown that you can gather, sort and present routine information and data, using digital tools where they fit.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.11.b5
  forPractitioner: { text: "Typical Scottish CertHE holders will be able to use subject knowledge and techniques routinely to evaluate and build arguments and solutions to routine problems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Certificate of Higher Education in Scotland, you will usually be able to use what you know to weigh up and answer everyday problems in your subject.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.11.b6
  forPractitioner: { text: "Typical Scottish CertHE holders will be able to report results accurately and reliably, in structured, coherent argument.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Certificate of Higher Education in Scotland, you will usually be able to report what you found accurately and in a clear order.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.11.b7
  forPractitioner: { text: "Typical Scottish CertHE holders will be able to continue learning in a structured, managed setting.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Certificate of Higher Education in Scotland, you will usually be able to keep learning where the setting is well organised.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.11.b8
  forPractitioner: { text: "Typical Scottish CertHE holders will be able to apply subject and transferable skills where responsibility is limited and the task's scope and decision criteria are well defined.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Certificate of Higher Education in Scotland, you will usually be able to use your skills on tasks that are clearly set out, carrying a little responsibility yourself.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.13.b1
  forPractitioner: { text: "Scottish DipHE holders have shown knowledge of the subject's scope and main areas and links, detail in key areas and some awareness of current issues in specialised areas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a Diploma of Higher Education in Scotland, you will have shown that you know the shape of your subject, some key areas in detail and something of current debates.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.13.b2
  forPractitioner: { text: "Scottish DipHE holders have shown understanding of a range of essential theories and concepts and awareness of major issues at the forefront.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a Diploma of Higher Education in Scotland, you will have shown that you understand the essential theories of your subject and know the big questions at its leading edge.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.13.b3
  forPractitioner: { text: "Scottish DipHE holders have shown familiarity with essential and routine materials, techniques and practices and use them effectively.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a Diploma of Higher Education in Scotland, you will have shown that you use your subject's essential materials and methods well.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.13.b4
  forPractitioner: { text: "Scottish DipHE holders have shown skills in gathering, critically analysing and presenting core information and data, using ICT as appropriate.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a Diploma of Higher Education in Scotland, you will have shown that you can gather, critically analyse and present your subject's core information and data.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.13.b5
  forPractitioner: { text: "Typical Scottish DipHE holders will be able to evaluate critically and build evidence-based arguments and find solutions to well-defined, mostly routine problems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Diploma of Higher Education in Scotland, you will usually be able to build arguments from evidence and solve clearly defined, mostly routine problems.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.13.b6
  forPractitioner: { text: "Typical Scottish DipHE holders will be able to report results accurately and reliably with a range of specialist techniques.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Diploma of Higher Education in Scotland, you will usually be able to report your results accurately, using your subject's specialist methods.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.13.b7
  forPractitioner: { text: "Typical Scottish DipHE holders will be able to identify and meet their main learning needs in defined contexts and take guided learning in new areas.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Diploma of Higher Education in Scotland, you will usually be able to see what you need to learn, deal with it, and learn new things with guidance.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.13.b8
  forPractitioner: { text: "Typical Scottish DipHE holders will be able to apply their skills where the task is mostly well defined but some responsibility and initiative is needed.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Diploma of Higher Education in Scotland, you will usually be able to use your skills where tasks are mostly clear but you must show some initiative.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.14.b1
  forPractitioner: { text: "Scottish bachelor's (non-honours) holders have shown broad, comparative knowledge of the subject, with detail in a defined area or a balanced specialism, informed by current developments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a bachelor's degree without honours in Scotland, you will have shown broad knowledge of your subject and how its parts compare, with depth in one area and awareness of new developments.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.14.b2
  forPractitioner: { text: "Scottish bachelor's (non-honours) holders have shown critical understanding of essential theories and how enquiry develops them, and awareness that knowledge is provisional.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a bachelor's degree without honours in Scotland, you will have shown that you understand your subject's main theories critically, how research builds them, and that knowledge can change.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.14.b3
  forPractitioner: { text: "Scottish bachelor's (non-honours) holders have shown competence with routine materials and practices and a few specialised, advanced ones.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a bachelor's degree without honours in Scotland, you will have shown that you handle everyday methods well and a few advanced ones too.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.14.b4
  forPractitioner: { text: "Scottish bachelor's (non-honours) holders have shown well-developed skills in gathering, evaluating, analysing and presenting information from many current sources, ICT included.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a bachelor's degree without honours in Scotland, you will have shown strong skills in finding, judging, analysing and presenting information from many current sources.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.14.b5
  forPractitioner: { text: "Typical Scottish bachelor's (non-honours) holders will be able to identify and analyse problems and to formulate, evaluate and apply evidence-based solutions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a bachelor's degree without honours in Scotland, you will usually be able to spot and analyse problems and build and test solutions from evidence.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.14.b6
  forPractitioner: { text: "Typical Scottish bachelor's (non-honours) holders will be able to report results accurately in varied contexts using the main specialist concepts and techniques.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a bachelor's degree without honours in Scotland, you will usually be able to report your results accurately in different settings, using your subject's key ideas and methods.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.14.b7
  forPractitioner: { text: "Typical Scottish bachelor's (non-honours) holders will be able to identify and meet their learning needs, drawing on current research and professional materials.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a bachelor's degree without honours in Scotland, you will usually be able to work out what you need to learn and use current research and professional materials to learn it.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.14.b8
  forPractitioner: { text: "Typical Scottish bachelor's (non-honours) holders will be able to apply their skills where tasks may be well defined but responsibility, initiative and decisions are needed.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a bachelor's degree without honours in Scotland, you will usually be able to use your skills where you must take responsibility, show initiative and make decisions.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.16.b1
  forPractitioner: { text: "Scottish honours graduates have shown systematic, extensive, comparative knowledge of the subject and its links, and detailed knowledge of a few specialisms partly at the forefront.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree in Scotland, you will have shown wide, systematic knowledge of your whole subject and detail in a few specialisms that reach its leading edge.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.16.b2
  forPractitioner: { text: "Scottish honours graduates have shown critical understanding of established theories and of several advanced and emerging issues at the forefront.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree in Scotland, you will have shown critical understanding of your subject's theories and of new questions at its leading edge.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.16.b3
  forPractitioner: { text: "Scottish honours graduates have shown they understand critically that knowledge is uncertain and limited and how it develops, and can use established techniques of analysis and enquiry.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree in Scotland, you will have shown that you understand the limits of knowledge and how it grows, and can use your subject's research methods.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.16.b4
  forPractitioner: { text: "Scottish honours graduates have shown comprehensive knowledge of essential and advanced materials and techniques, some at the forefront.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree in Scotland, you will have shown full command of your subject's essential and advanced methods, some of them the newest.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.16.b5
  forPractitioner: { text: "Scottish honours graduates have shown skill in identifying information needs and systematically gathering and interpreting data from evaluated sources, including current research.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree in Scotland, you will have shown that you work out what information you need, then gather and interpret it systematically from sources you have judged.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fqheis-2024/4.16.b6
  forPractitioner: { text: "Typical Scottish honours graduates will be able to assess concepts and incomplete data systematically and critically, analyse complex problems and show some originality in evidence-based solutions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree in Scotland, you will usually be able to assess ideas and data critically, analyse complex problems and bring some original, creative thinking to solving them.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.16.b7
  forPractitioner: { text: "Typical Scottish honours graduates will be able to report results accurately using the full repertoire of the subject's principal concepts.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree in Scotland, you will usually be able to report your work accurately, using all your subject's main ideas.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.16.b8
  forPractitioner: { text: "Typical Scottish honours graduates will be able to identify and meet their learning needs systematically, in current and new areas, using research and professional materials up to the forefront.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree in Scotland, you will usually be able to plan your own learning, in familiar and new areas, using the latest research and professional materials.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.16.b9.1
  forPractitioner: { text: "Typical Scottish honours graduates will be able to apply their skills in professional settings that require personal responsibility and initiative.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree in Scotland, you will usually be able to use your skills at work where you must take responsibility and show initiative.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.16.b9.2
  forPractitioner: { text: "Typical Scottish honours graduates will be able to apply their skills where decisions are made in complex, unpredictable contexts.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree in Scotland, you will usually be able to use your skills where you must decide in complex, unpredictable situations.", rewrite: full, force: will, status: drafted }
- statement: qaa/fqheis-2024/4.16.b9.3
  forPractitioner: { text: "Typical Scottish honours graduates will be able to apply their skills where further professional development is required.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree in Scotland, you will usually be able to use your skills where you must keep developing professionally.", rewrite: full, force: will, status: drafted }
```

### S5 Levels and alignment
```yaml
levels:
  - { id: fqheis:7, role: defines, locator: "3.4; 4.11", typical: CertHE }
  - { id: fqheis:8, role: defines, locator: "3.4; 4.13", typical: DipHE }
  - { id: fqheis:9, role: defines, locator: "3.4; 4.14", typical: bachelor's non-honours degree }
  - { id: fqheis:10, role: defines, locator: "3.4; 4.16", typical: bachelor's degree with honours }
  - { id: fqheis:11, role: defines, locator: "3.4; 4.17", typical: master's degree, descriptor: "std:doc:qaa-fheq-2024-framework: qaa/fheq-2024/4.17.* (shared)" }
  - { id: fqheis:12, role: defines, locator: "3.4; 4.18", typical: doctoral degree, descriptor: "std:doc:qaa-fheq-2024-framework: qaa/fheq-2024/4.18.* (shared)" }
crosswalks:
  - { from: fqheis:11, to: fheq:7, relation: shared-descriptor, source: "4.8 and the heading of 4.17" }
  - { from: fqheis:12, to: fheq:8, relation: shared-descriptor, source: "3.4; 4.8 and the heading of 4.18" }
  - { from: fqheis, to: scqf, relation: part-of, source: "2.23; the levels are SCQF levels (3.4)" }
  # Table 1's qualification-by-qualification crosswalk (FHEQ, FQHEIS, QF-EHEA cycles) and Annex C's credit are held once in std:doc:qaa-fheq-2024-framework, S5
```

### S6 Themes
`not-applicable-by-design`: the descriptors carry no cross-cutting themes.

### S7 Relations
```yaml
- { rel: siblingOf, target: "std:doc:qaa-fheq-2024-framework", note: "published together; holds the shared master's and doctoral descriptors and the common material" }
- { rel: partOf, target: "SCQF (2.23)" }
- { rel: particularisedBy, target: "QAA Subject Benchmark Statements (4.1)" }
- { rel: alignsWith, target: "QF-EHEA and its Dublin descriptors (Annex B, in std:doc:qaa-fheq-2024-framework)" }
```

### S8 Currency and review
```yaml
published: 2024-02-21
lastReviewed: 2024-02
reviewCycle: none-stated
consultation: none-stated
replacedBy: unknown
```

### S9 Commentary (optional)
`unknown`: not researched.

### SL Level language
<!-- label: both; status: drafted; basis: primary. Our words, with the issuer's verbs and short quoted phrases. SCQF 11 and 12 are read from the shared descriptors, whose statements are in std:doc:qaa-fheq-2024-framework. -->

#### SL1 What defines each level

| Descriptor and level | For the practitioner | For the learner |
|---|---|---|
| 4.11 CertHE (SCQF 7) | Outline knowledge of the subject with some areas in depth; routine techniques applied to routine problems in clearly bounded contexts; limited personal responsibility. | At this first Scottish level, you know your subject in outline and parts of it more fully, and you use standard methods on familiar problems where the task is clearly set. |
| 4.13 DipHE (SCQF 8) | Detailed knowledge of some areas and a first awareness of the forefront; critical analysis of core data; evidence-based argument on clearly bounded problems; naming one's own learning needs. | At this Scottish level, you know some areas in detail, are aware of the big open questions, build arguments from evidence and can say what you still need to learn. |
| 4.14 bachelor's non-honours (SCQF 9) | Broad, comparative knowledge, with a specialism informed by current developments; seeing knowledge as provisional; identifying and analysing problems and applying evidence-based solutions; drawing on current research to meet one's own learning needs. | At this Scottish level, you see your subject broadly and in comparison, know some of it in depth, accept that knowledge can change, and use current research to keep learning. |
| 4.16 honours degree (SCQF 10) | Systematic, extensive and comparative understanding of the whole subject, critical understanding of emerging issues and of how knowledge is made; the first call for some originality and creativity; professional contexts. | At Scottish honours level, you understand your whole subject and how knowledge in it is made, follow its newest questions, and begin to bring some originality and creativity of your own. |
| 4.17 master's (SCQF 11; shared) | Much of one's knowledge at or informed by the forefront; originality in applying it; evaluating research and methodologies critically and proposing hypotheses; sound judgement without complete data; autonomy and self-direction at a professional level. | At master's level, much of what you know is at the leading edge; you apply it with originality, critique research and its methods, judge well without all the facts and work on your own at a professional level. |
| 4.18 doctorate (SCQF 12; shared) | Creating new knowledge of publishable quality through original research; conceiving, designing and adjusting a project at the forefront; continuing to contribute new techniques and ideas; largely autonomous initiative. | At doctoral level, you create new knowledge through your own research, good enough to be published; you design and steer a project at the leading edge and go on contributing new ideas and methods. |

#### SL2 The level table, by part

| Descriptor and level | Threshold outcomes | Wider abilities | Qualities for employment |
|---|---|---|---|
| 4.11 CertHE (SCQF 7) | outline of the subject, some areas in more depth; major theories and concepts; familiarity with routine materials and practices; gathering and presenting routine information | routine use of knowledge on routine problems; communicating results soundly; further learning in a managed setting; skills where decisions are well defined | (none) |
| 4.13 DipHE (SCQF 8) | scope of the subject, detail in key areas, current issues; essential theories and issues at the forefront; effective use of essential materials and practices; critical gathering and presentation of core information | evidence-based argument on defined problems; communicating with specialist techniques; own learning needs and guided learning; skills with some responsibility and initiative | (none) |
| 4.14 bachelor's non-honours (SCQF 9) | broad and comparative knowledge, with depth; critical understanding of theories and how knowledge develops; competence in routine and some advanced practices; well-developed skills with a wide range of sources | identifying problems and evidence-based solutions; communicating across contexts with the subject's concepts; own learning needs, drawing on current research; skills with responsibility, initiative and decisions | (none) |
| 4.16 honours degree (SCQF 10) | systematic, extensive, comparative knowledge; specialisms at the forefront; critical understanding of theory and emerging issues; limits of knowledge; established techniques; comprehensive command of essential and advanced techniques; identifying information needs and systematic gathering | systematic critical assessment with some originality; communicating with the full repertoire of the subject; systematically meeting learning needs at the forefront; personal responsibility and initiative; decisions in complex, unpredictable contexts; further professional development | (none) |
| 4.17 master's (SCQF 11; shared) | systematic understanding; critical awareness at the forefront; comprehensive understanding of research techniques; originality in applying knowledge; how research creates knowledge; critically evaluating current research; critiquing methodologies; proposing hypotheses | complex issues, judgement without complete data; self-direction, originality and autonomy; continuing to advance knowledge and skills | initiative and personal responsibility; decisions in complex, unpredictable situations; independent learning for continuing development |
| 4.18 doctorate (SCQF 12; shared) | creating new knowledge of publishable quality; substantial body of knowledge at the forefront; designing and adjusting research projects; detailed understanding of research techniques | judgements on complex issues; communicating to all audiences; continuing advanced research and development | qualities for autonomous work in complex situations |

#### SL3 Verbs by level

| Descriptor and level | Threshold outcomes | Wider abilities | Qualities for employment |
|---|---|---|---|
| 4.11 CertHE (SCQF 7) | include | use, evaluate, formulate, communicate, undertake, apply |  |
| 4.13 DipHE (SCQF 8) | include | use, evaluate, formulate, identify, communicate, using, address, undertake, apply |  |
| 4.14 bachelor's non-honours (SCQF 9) | informed, developed, drawing, include | use, identifying, analysing, formulating, evaluating, applying, communicate, using, identify, address, draw, apply |  |
| 4.16 honours degree (SCQF 10) | informed, developed, deploy, identifying | use, identifying, analysing, demonstrating, formulating, evaluating, applying, communicate, using, identify, address, making, undertake |  |
| 4.17 master's (SCQF 11; shared) | informed, used, create, interpret, evaluate, develop, propose | deal, make, communicate, demonstrate, tackling, solving, act, planning, implementing, continue, advance, develop | required |
| 4.18 doctorate (SCQF 12; shared) | satisfy, extend, merit, conceptualise, design, implement, adjust | make, communicate, continue, undertake, contributing |  |

#### SL4 How progression is communicated
<!-- Each thread follows one quality up the Scottish levels; the issuer's words in quotation marks, a few at a time. -->

- **The knowledge held:** 4.11: "outline knowledge", and "more extensive knowledge" of "key areas"; 4.13: "detailed knowledge of some key areas"; 4.14: "broad and comparative knowledge"; 4.16: "systematic, extensive and comparative knowledge"; 4.17: "systematic understanding of knowledge"; 4.18: "a substantial body of knowledge", then "the creation and interpretation of new knowledge".
- **Reach towards the forefront:** 4.13: "an awareness of major issues at the forefront"; 4.14: specialised study "informed by current developments"; 4.16: "advanced and emerging issues at the forefront"; 4.17: "much of which" is at or informed by it; 4.18: "extend the forefront of the discipline".
- **The limits of knowledge:** 4.14: "the provisional nature of knowledge"; 4.16: critical understanding of that, and "how it is developed"; 4.17: "critical awareness of current problems".
- **The problem:** 4.11: "of a routine nature"; 4.13: "clearly-defined problems of a generally routine nature"; 4.14: "identifying and analysing problems and issues"; 4.16: "complex problems and issues"; 4.17: "deal with complex issues", "in the absence of complete data"; 4.18: "complex issues in specialist fields".
- **The thinking verbs:** 4.11: "basic analysis"; 4.13: "critically evaluate and formulate"; 4.14: identify, analyse, formulate, evaluate, apply; 4.16: "systematic and critical assessment"; 4.17: "evaluate critically current research", "develop critiques"; 4.18: conceptualise, design, implement, adjust.
- **Research and enquiry:** 4.16: sources "including current research"; 4.17: "evaluate methodologies", "propose new hypotheses"; 4.18: "original research", good enough "to satisfy peer review".
- **Originality:** 4.16: "some originality and creativity"; 4.17: "originality in the application of knowledge"; "self-direction and originality"; 4.18: "new techniques, ideas or approaches".
- **Communication:** 4.13: "using a range of specialist techniques"; 4.14: "in a range of different contexts"; 4.16: "the full repertoire" of the main concepts; 4.17: "clearly"; 4.18: "clearly and effectively".
- **Learning:** 4.13: "guided further learning in new areas"; 4.14: "identify and address their own learning needs"; 4.16: "both in current and new areas"; 4.17: "to develop new skills to a high level"; "independent learning ability"; 4.18: "continue to undertake pure and/or applied research".
- **Responsibility and autonomy:** 4.11: "some limited personal responsibility"; 4.13: "some personal responsibility and initiative"; 4.14: "personal responsibility, initiative and decision-making"; 4.16: "contexts of a professional or equivalent nature"; 4.17: "act autonomously"; 4.18: "largely autonomous initiative".

#### SL5 Observations on the formulation
<!-- label: editorial; status: drafted; basis: primary -->
- **Six steps, not five.** The FQHEIS puts two awards between CertHE and honours that the FHEQ does not have as levels: the DipHE (SCQF 8) and the non-honours bachelor's (SCQF 9). Its ladder is finer below honours, matching a four-year Scottish honours degree (3.3).
- **Context is graded explicitly.** Each of the four own descriptors closes with the setting in which skills are applied: limited responsibility and well-defined decisions (7), generally well defined but with some initiative (8), well defined but with decision-making (9), then professional contexts with complex and unpredictable decisions (10). It is the CQFW's way of grading, inside a qualifications framework.
- **The forefront arrives earlier.** An "awareness of major issues at the forefront" already at SCQF 8; "current developments" informing specialised study at 9; "advanced and emerging issues" at 10. The FHEQ first names the forefront at honours.
- **Knowledge is graded by breadth as well as depth.** Outline (7), scope and main areas (8), broad and comparative (9), "systematic, extensive and comparative", the subject "as a whole" (10).
- **Data handling is a strand of its own.** Gathering, basic analysis and presentation of routine data (7), critical analysis of core data (8), "well-developed skills" from current sources (9), identifying information needs and systematic gathering from evaluated sources (10), with ICT named at 7 to 9.
- **Scottish honours asks for originality.** "Some originality and creativity" (10), which the FHEQ does not ask before master's.
- **The top two levels are the FHEQ's.** At SCQF 11 and 12 the two frameworks share one text; the differences are all below master's (std:doc:qaa-fheq-2024-framework, SL5).

## Part B Terminology
<!-- label: both; status: drafted; basis: primary -->
`see std:doc:qaa-fheq-2024-framework`: the Definitions are common to both frameworks and held there.

## Part C Process
<!-- label: both; status: drafted; basis: primary -->
`see std:doc:qaa-fheq-2024-framework`: the provider responsibilities (section 6) are common to both frameworks and held there.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies
  edition: 2nd edition, updated February 2024
  year: 2024
  url: unknown
  retrieved: "PDF attached by Abbott, 2026-10-03, 03:47"
  licence: none read yet
  tier: primary
  readVia: direct
  held: 229532f8f0adf1a3c72ee782316cdc85c3d2250217bb6f065a807e69c0d2ca72
  heldFiles: [wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.txt, wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.norm.txt, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, S4, S4a, S5, S7, SL]
- { key: D2, ref: "std:doc:qaa-fheq-2024-framework", use: "the shared descriptors (4.17, 4.18) and the common material" }
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "section 4 read whole with the FHEQ (run 0047); the FQHEIS's own descriptors taken into this document at the split (D-std-0010)" }
```

### D3 Wanted sources
```yaml
- { w: W-std-0018, citation: "the SCQF Partnership's level descriptors for SCQF 7 to 12, which the FQHEIS sits within", settles: [S5, SL], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- The split (D-std-0010): the shared master's and doctoral descriptors and the common material are held once, in std:doc:qaa-fheq-2024-framework; this document points to them. If Abbott wants the common material in a document of its own, both documents change their pointers.
- Statement ids changed at the split: `qaa/fheq-2024/4.11.*` and the like are now `qaa/fqheis-2024/4.11.*`; spans unchanged.
- 4.8, the issuer's slip on the shared descriptors' names, is recorded in std:doc:qaa-fheq-2024-framework, Part E.
- The SCQF level descriptors (the SCQF Partnership's own) are not held; the FQHEIS's levels are SCQF levels, so a crosswalk to them would come from that source (D3).
- ST-12: the statements and versions were checked with the FHEQ's in run 0047 (no nine-word copies).

---

## Change notes
- 0.2.1, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.2.0, 3 October 2026, 11:00: every statement record now carries the issuer's statement in full (`source`, taken from its span in the held text) beside our paraphrase and versions, for language analysis; private, never published (Abbott, 10:56 and 10:59; D-std-0014). No paraphrase changed.
- 0.1.1, 3 October 2026, 07:34: provenance lines added to Parts B and C; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.1.0: 2026-10-03, 05:24: split out of the Frameworks 2024 document (D-std-0010, Abbott, 05:20): the FQHEIS's four descriptors (35 statements, one stem), its level records and its level language; std, run 0047 (P1).
