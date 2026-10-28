---
id: std:doc:qaa-fheq-2024-framework
title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies: the FHEQ, and the material common to both frameworks"
profile: standards/framework
profileVersion: 0.1.6-draft
issuer: The Quality Assurance Agency for Higher Education (QAA)
kind: qualification-framework
jurisdiction: [England, Wales, Northern Ireland]   # the common material (Annexes B to D, sections 2 to 6) also applies in Scotland
subjectScope: universal
subjects: []
edition: 2nd edition, updated February 2024
published: 2024-02-21
status: current   # as at the held text; not checked against QAA's site (Part E)
supersedes: "the first edition (2014), as the document's 'About this edition' says"
heldText: { method: sha256-bytes, raw: 229532f8f0adf1a3c72ee782316cdc85c3d2250217bb6f065a807e69c0d2ca72, normalised: b37faa2a285c74257df9fa5b46f29ba7b7ec2f11a7bafcd214789f35b325f1b5 }
original: { method: sha256-bytes, pdf: 249d3637cc31612e25748b02513f912d5e0c9712851809c3e7bd9552fbd64621, held: no }   # supplied files stay out of UNI (nts N-1020)
frameworkKind: qualification
nations: [England, Wales, Northern Ireland]
levels: [fheq:4, fheq:5, fheq:6, fheq:7, fheq:8]   # equivalents stated by the document: S5; the FQHEIS levels are std:doc:qaa-fqheis-2024-framework
awards: [CertHE, foundation degree, bachelor's with honours, master's, doctorate]
credit: "illustrative: Annex C, typical minimum credit per qualification and nation (S5 credit)"
licence: none read yet (Part E)
parts:
  S: full   # Annex A (the 2014 advisory group) excluded
  B: full
  C: described
pins: { structure: 0.13.0-draft, template: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.5.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0047
passes:
  P1: "2026-10-03, std (claude.ai, META Project): stage 1 at 04:35, stage 2 at 04:53; split from the FQHEIS at 05:24 (D-std-0010)"
  P2: "skipped: read direct from the issuer's PDF"
  P3: open
version: 0.4.1
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.0-draft under the standards/framework variant (profile 0.1.6-draft; its template is to write), with the level-language section SL as in the CQFW run (std N-0057) -->
# The Frameworks for Higher Education Qualifications (QAA, 2024): the FHEQ

> Run 0047, P1 by std, in two stages: (1) the FHEQ's five qualification descriptors (4.10, 4.12, 4.15, 4.17, 4.18) and their level language; (2) Annex D (the honours classification descriptions), Annex B (the Dublin descriptors), Table 1 and Annex C (read from the page images), the Definitions, and the provider statements of sections 2, 4, 5 and 6. The issuer's words are held in the source library repo only (`wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.norm.txt`); every statement points into them by character span. Everything else is our words; in the level-language section, words in quotation marks are the issuer's, a few at a time. Doubts are in Part E.

> **One document per framework** (Abbott, 05:20; D-std-0010). This document holds the FHEQ (England, Wales, Northern Ireland). The FQHEIS (Scotland) is `std:doc:qaa-fqheis-2024-framework`: its four own descriptors (4.11, 4.13, 4.14, 4.16) and its level language. The master's and doctoral descriptors (4.17, 4.18) are common to both frameworks and are held here once; the FQHEIS document's SCQF 11 and 12 records point to them. The material common to both frameworks (sections 2 to 6, Annexes B to D, Table 1, the Definitions) is also held here once.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The FHEQ: QAA's framework for higher education qualifications in England, Wales and Northern Ireland, Levels 4 to 8, with the material QAA's Frameworks document gives both UK frameworks (award and title rules, the Dublin descriptors, the credit table and the honours classification descriptions). Reach for it to say what a holder of an FHEQ qualification has shown at the threshold, what a typical holder can also do, and how the levels compare with Scotland's and Europe's. It is generic across subjects; subject benchmarks particularise it.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Five qualification descriptors, one for the main qualification at each FHEQ level: CertHE (Level 4), foundation degree (Level 5), honours degree (Level 6), master's (Level 7) and doctorate (Level 8); the last two are shared with the FQHEIS as SCQF 11 and 12. Each has two parts (4.2, 4.3): the outcomes a student has demonstrated for the award, which the document calls the national threshold academic standard, and the wider abilities a typical holder will have, including the qualities employment asks for. The descriptors are noun phrases hung on a lead ("awarded to students who have demonstrated:"), not imperatives as in the CQFW; progression is carried by the qualifiers of knowledge (outline, detailed, systematic, at the forefront, new), of problem (routine, clearly defined, complex, incomplete data), and of independence. Around them the document sets the rules for awarding and titling qualifications (sections 2, 4, 5, 6), relates the levels to the European cycles (Table 1, the Dublin descriptors in Annex B), gives typical credit by nation (Annex C), and describes the four honours classes and failure across five strands (Annex D).

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies
edition: 2nd edition, updated February 2024
dates:
  published: 2024-02-21
  other: ["first edition 2014 (About this edition)"]
kind: qualification-framework
jurisdiction: [England, Wales, Northern Ireland, Scotland]
authority: reference   # degree-awarding bodies use it as a reference point; England's providers also refer to the OfS sector-recognised standards (4.9)
licence: none read yet
copyrightNotice: "© The Quality Assurance Agency for Higher Education 2024"
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: the levels of UK higher education qualifications and the generic outcomes of the main qualification at each (section 4)
appliesTo:
  awards: [CertHE, foundation degree, bachelor's with honours, master's, doctorate]
  levels: [fheq:4, fheq:5, fheq:6, fheq:7, fheq:8]
  providers: UK degree-awarding bodies
whoMustUse: "degree-awarding bodies and their delivery partners; in Scotland, Wales and Northern Ireland the full framework, in England through the OfS sector-recognised standards (How the Frameworks are used; 2.2)"
howUsed: [positioning, designing, approving, assessing, awarding, classifying, titling, reviewing]   # 1.1, 2.4, 4.2, section 6
doesNot: "specific subjects: Subject Benchmark Statements fulfil that purpose (4.1)"
beneficiary: the student
statedScope: "generic: the descriptors cover the full range of disciplines (4.1)"
statedSubjects: none-stated
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary. The issuer's structure: nine descriptors, each a heading (4.10 to 4.18), of which the FHEQ's five are here, a lead and up to three lists; list items numbered by us in order (b1, b2, ...), sub-items b<n>.<m>. Stems (list leads ending in a colon) are components, not statements; their sub-items carry them. -->
```yaml
components:
  - { number: "4.10", componentType: descriptor, heading: "4.10 Descriptor for a higher education qualification at Level 4 on the FHEQ Certificate of Higher Education", level: fheq:4 }
  - { number: "4.12", componentType: descriptor, heading: "4.12 Descriptor for a higher education qualification at Level 5 on the FHEQ Foundation degree", level: fheq:5 }
  - { number: "4.15", componentType: descriptor, heading: "4.15 Descriptor for a higher education qualification at Level 6 on the FHEQ Bachelor's degree with honours", level: fheq:6 }
  - { number: "4.17", componentType: descriptor, heading: "4.17 Descriptor for a higher education qualification at Level 7 on the FHEQ and SCQF Level 11 on the FQHEIS Master's degree", level: [fheq:7, fqheis:11] }
  - { number: "4.18", componentType: descriptor, heading: "4.18 Descriptor for a higher education qualification at Level 8 on the FHEQ and SCQF Level 12 on the FQHEIS Doctoral degree", level: [fheq:8, fqheis:12] }
  - { number: "4.15.b3", componentType: stem, parent: "4.15", heading: "conceptual understanding that enables the student to (two items)" }
  - { number: "4.15.b9", componentType: stem, parent: "4.15", heading: "qualities and skills for employment that requires (three items)" }
  - { number: "4.17.b4", componentType: stem, parent: "4.17", heading: "conceptual understanding that enables the student to (two items)" }
  - { number: "4.17.b8", componentType: stem, parent: "4.17", heading: "qualities and skills for employment that requires (three items)" }
  - { number: "annex-d/summary/lead/ns", componentType: stem, parent: "annex-d/summary", heading: "the lead of the Not successful column: course outcomes not achieved" }
  - { number: "annex-d/summary/lead/3rd", componentType: stem, parent: "annex-d/summary", heading: "the lead of the Third-class honours (3rd, pass or threshold) column: all course outcomes achieved, and" }
  - { number: "annex-d/summary/lead/2.2", componentType: stem, parent: "annex-d/summary", heading: "the lead of the Lower second-class honours (2.2) column: all course outcomes achieved, and" }
  - { number: "annex-d/summary/lead/2.1", componentType: stem, parent: "annex-d/summary", heading: "the lead of the Upper second-class honours (2.1) column: all course outcomes achieved, and" }
  - { number: "annex-d/summary/lead/1st", componentType: stem, parent: "annex-d/summary", heading: "the lead of the First-class honours (1st) column: all course outcomes achieved, and" }
  - { number: "annex-d/knowledge", componentType: strand, parent: "Annex D", heading: "Knowledge and understanding", gloss: "Knowledge and understanding: systematic, comparative understanding of the field, some of it at or informed by the forefront" }
  - { number: "annex-d/cognitive", componentType: strand, parent: "Annex D", heading: "Cognitive skills", gloss: "Cognitive skills: the conceptual understanding needed to argue, solve problems and comment on research, aware of the limits of knowledge" }
  - { number: "annex-d/practical", componentType: strand, parent: "Annex D", heading: "Practical skills", gloss: "Practical skills: managing one's own learning and using the discipline's established techniques accurately" }
  - { number: "annex-d/transferable", componentType: strand, parent: "Annex D", heading: "Transferable skills", gloss: "Transferable skills: communicating to any audience, initiative, responsibility and decisions in complex situations" }
  - { number: "annex-d/professional", componentType: strand, parent: "Annex D", heading: "Professional competences", gloss: "Professional competences: the requirements and learning ability for further professional training, where course outcomes express them; a PSRB-accredited award is not made without them" }
  - { number: "annex-d/summary", componentType: strand, parent: "Annex D", heading: "Summary table (four rows)", gloss: "The summary: four strands of achievement read across the five outcomes, after all course learning outcomes are met" }
  - { number: "annex-b/short", componentType: stem, parent: "Annex B", heading: "the short cycle: qualifications marking its completion are awarded to students who (list)", level: qfehea:short }
  - { number: "annex-b/1", componentType: stem, parent: "Annex B", heading: "the first cycle: qualifications marking its completion are awarded to students who (list)", level: qfehea:1 }
  - { number: "annex-b/2", componentType: stem, parent: "Annex B", heading: "the second cycle: qualifications marking its completion are awarded to students who (list)", level: qfehea:2 }
  - { number: "annex-b/3", componentType: stem, parent: "Annex B", heading: "the third cycle: qualifications marking its completion are awarded to students who (list)", level: qfehea:3 }
  - { number: "6.3", componentType: stem, parent: "6.3", heading: "what course design and review weigh (stem)" }
  - { number: "6.7", componentType: stem, parent: "6.7", heading: "conditions of award (stem)" }
  - { number: "6.14", componentType: stem, parent: "6.14", heading: "degree titles only in full (stem)" }
excluded:
  - { number: "4.11, 4.13, 4.14, 4.16", heading: "the FQHEIS's own descriptors", kind: "other: std:doc:qaa-fqheis-2024-framework (D-std-0010)" }
  - { number: "4.10 to 4.18, the paragraphs after each list", heading: "which qualifications meet the descriptor in full or in part", kind: "other: stage 2" }
  - { number: "Annex A", heading: "Advisory group (for 2014 version)", kind: "other: names, out of scope" }
  - { number: "1, 2, 3, 4.1 to 4.9, 5, 6 (descriptive paragraphs)", heading: "context and explanation", kind: "other: read for S1, S2, S5, S7, Part C; only obliging sentences are S4 records (D-std-0002 (a))" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. The FHEQ's descriptor records, then the common material. Force: `threshold` for the outcomes demonstrated for the award (4.2: "the national threshold academic standard"); `will` for the typical holder's wider abilities and qualities (4.3), which the issuer frames as expectations, not conditions of award. -->
```yaml
- id: qaa/fheq-2024/4.10.b1
  locator: { number: "4.10.b1", headingPath: ["4.10 CertHE (FHEQ 4)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 41289, end: 41468 }
  source: "knowledge of the underlying concepts and principles associated with their area(s) of study, and an ability to evaluate and interpret these within the context of that area of study"
  stem: none
  statementType: descriptor
  force: threshold
  level: fheq:4
  dimension: threshold-outcomes
  award: "a Certificate of Higher Education"
  appliesTo: "the award of a Certificate of Higher Education"
  addressee: student
  verbs: [evaluate, interpret]
  about: "underlying concepts and their interpretation"
  themes: [none]
  paraphrase: "Knows the concepts and principles beneath their area of study and can judge and read them within it."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.10.b2
  locator: { number: "4.10.b2", headingPath: ["4.10 CertHE (FHEQ 4)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 41473, end: 41694 }
  source: "an ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study."
  stem: none
  statementType: descriptor
  force: threshold
  level: fheq:4
  dimension: threshold-outcomes
  award: "a Certificate of Higher Education"
  appliesTo: "the award of a Certificate of Higher Education"
  addressee: student
  verbs: [present, evaluate, interpret, develop, make]
  about: "handling data to argue and judge"
  themes: [none]
  paraphrase: "Can present and weigh qualitative and quantitative data to build arguments and reach sound judgements grounded in the subject's basic theories."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.10.b3
  locator: { number: "4.10.b3", headingPath: ["4.10 CertHE (FHEQ 4)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 41756, end: 41874 }
  source: "evaluate the appropriateness of different approaches to solving problems related to their area(s) of study and/or work"
  stem: none
  statementType: descriptor
  force: will
  level: fheq:4
  dimension: wider-abilities
  award: "a Certificate of Higher Education"
  appliesTo: "the award of a Certificate of Higher Education"
  addressee: holder
  verbs: [evaluate]
  about: "judging approaches to problems"
  themes: [none]
  paraphrase: "Weighs how well different approaches suit problems in their study or work."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.10.b4
  locator: { number: "4.10.b4", headingPath: ["4.10 CertHE (FHEQ 4)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 41879, end: 41990 }
  source: "communicate the results of their study/work accurately and reliably, and with structured and coherent arguments"
  stem: none
  statementType: descriptor
  force: will
  level: fheq:4
  dimension: wider-abilities
  award: "a Certificate of Higher Education"
  appliesTo: "the award of a Certificate of Higher Education"
  addressee: holder
  verbs: [communicate]
  about: "communicating results soundly"
  themes: [none]
  paraphrase: "Reports what their study or work found, accurately, reliably and in a structured, coherent way."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.10.b5
  locator: { number: "4.10.b5", headingPath: ["4.10 CertHE (FHEQ 4)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 41995, end: 42089 }
  source: "undertake further training and develop new skills within a structured and managed environment."
  stem: none
  statementType: descriptor
  force: will
  level: fheq:4
  dimension: wider-abilities
  award: "a Certificate of Higher Education"
  appliesTo: "the award of a Certificate of Higher Education"
  addressee: holder
  verbs: [undertake, develop]
  about: "further training in a managed setting"
  themes: [none]
  paraphrase: "Takes on more training and new skills where the setting is structured and managed."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.10.b6
  locator: { number: "4.10.b6", headingPath: ["4.10 CertHE (FHEQ 4)", "Qualities and transferable skills of holders (4.3)"] }
  span: { start: 42117, end: 42235 }
  source: "the qualities and transferable skills necessary for employment requiring the exercise of some personal responsibility."
  stem: none
  statementType: descriptor
  force: will
  level: fheq:4
  dimension: employment-qualities
  award: "a Certificate of Higher Education"
  appliesTo: "the award of a Certificate of Higher Education"
  addressee: holder
  verbs: []
  about: "qualities for work with some personal responsibility"
  themes: [none]
  paraphrase: "Has the qualities and transferable skills for jobs that call for some personal responsibility."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.12.b1
  locator: { number: "4.12.b1", headingPath: ["4.12 foundation degree (FHEQ 5)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 45077, end: 45231 }
  source: "knowledge and critical understanding of the well-established principles of their area(s) of study, and of the way in which those principles have developed"
  stem: none
  statementType: descriptor
  force: threshold
  level: fheq:5
  dimension: threshold-outcomes
  award: "a foundation degree"
  appliesTo: "the award of a foundation degree"
  addressee: student
  verbs: []
  about: "critical understanding of established principles"
  themes: [none]
  paraphrase: "Knows and critically understands the field's well-established principles and how they came about."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.12.b2
  locator: { number: "4.12.b2", headingPath: ["4.12 foundation degree (FHEQ 5)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 45236, end: 45432 }
  source: "ability to apply underlying concepts and principles outside the context in which they were first studied, including, where appropriate, the application of those principles in an employment context"
  stem: none
  statementType: descriptor
  force: threshold
  level: fheq:5
  dimension: threshold-outcomes
  award: "a foundation degree"
  appliesTo: "the award of a foundation degree"
  addressee: student
  verbs: [apply]
  about: "applying principles beyond their first context"
  themes: [none]
  paraphrase: "Can apply core concepts and principles outside the setting where they were learned, at work where that fits."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.12.b3
  locator: { number: "4.12.b3", headingPath: ["4.12 foundation degree (FHEQ 5)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 45437, end: 45645 }
  source: "knowledge of the main methods of enquiry in the subject(s) relevant to the named award, and ability to evaluate critically the appropriateness of different approaches to solving problems in the field of study"
  stem: none
  statementType: descriptor
  force: threshold
  level: fheq:5
  dimension: threshold-outcomes
  award: "a foundation degree"
  appliesTo: "the award of a foundation degree"
  addressee: student
  verbs: [evaluate, solving]
  about: "methods of enquiry and judging approaches"
  themes: [none]
  paraphrase: "Knows the subject's main methods of enquiry and can judge critically how well different approaches suit its problems."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.12.b4
  locator: { number: "4.12.b4", headingPath: ["4.12 foundation degree (FHEQ 5)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 45650, end: 45778 }
  source: "an understanding of the limits of their knowledge, and how this influences analyses and interpretations based on that knowledge."
  stem: none
  statementType: descriptor
  force: threshold
  level: fheq:5
  dimension: threshold-outcomes
  award: "a foundation degree"
  appliesTo: "the award of a foundation degree"
  addressee: student
  verbs: [influences]
  about: "the limits of one's own knowledge"
  themes: [none]
  paraphrase: "Understands where their knowledge stops and how that shapes analysis and interpretation built on it."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.12.b5
  locator: { number: "4.12.b5", headingPath: ["4.12 foundation degree (FHEQ 5)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 45840, end: 46001 }
  source: "use a range of established techniques to initiate and undertake critical analysis of information, and to propose solutions to problems arising from that analysis"
  stem: none
  statementType: descriptor
  force: will
  level: fheq:5
  dimension: wider-abilities
  award: "a foundation degree"
  appliesTo: "the award of a foundation degree"
  addressee: holder
  verbs: [use, initiate, undertake, propose]
  about: "critical analysis and proposing solutions"
  themes: [none]
  paraphrase: "Uses a range of established techniques to start and carry out critical analysis of information and to propose answers to the problems it shows."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.12.b6
  locator: { number: "4.12.b6", headingPath: ["4.12 foundation degree (FHEQ 5)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 46006, end: 46186 }
  source: "effectively communicate information, arguments and analysis in a variety of forms to specialist and non-specialist audiences and deploy key techniques of the discipline effectively"
  stem: none
  statementType: descriptor
  force: will
  level: fheq:5
  dimension: wider-abilities
  award: "a foundation degree"
  appliesTo: "the award of a foundation degree"
  addressee: holder
  verbs: [communicate, deploy]
  about: "communicating to specialist and general audiences"
  themes: [none]
  paraphrase: "Communicates information, argument and analysis in several forms to specialist and general audiences, and uses the discipline's key techniques well."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.12.b7
  locator: { number: "4.12.b7", headingPath: ["4.12 foundation degree (FHEQ 5)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 46191, end: 46351 }
  source: "undertake further training, develop existing skills and acquire new competences that will enable them to assume significant responsibility within organisations."
  stem: none
  statementType: descriptor
  force: will
  level: fheq:5
  dimension: wider-abilities
  award: "a foundation degree"
  appliesTo: "the award of a foundation degree"
  addressee: holder
  verbs: [undertake, develop, acquire, enable, assume]
  about: "further training towards significant responsibility"
  themes: [none]
  paraphrase: "Undertakes further training, builds on existing skills and gains new competences that equip them for significant responsibility in organisations."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.12.b8
  locator: { number: "4.12.b8", headingPath: ["4.12 foundation degree (FHEQ 5)", "Qualities and transferable skills of holders (4.3)"] }
  span: { start: 46379, end: 46512 }
  source: "the qualities and transferable skills necessary for employment requiring the exercise of personal responsibility and decision-making."
  stem: none
  statementType: descriptor
  force: will
  level: fheq:5
  dimension: employment-qualities
  award: "a foundation degree"
  appliesTo: "the award of a foundation degree"
  addressee: holder
  verbs: []
  about: "qualities for work with responsibility and decisions"
  themes: [none]
  paraphrase: "Has the qualities and transferable skills for jobs that call for personal responsibility and decision-making."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b1
  locator: { number: "4.15.b1", headingPath: ["4.15 honours degree (FHEQ 6)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 52861, end: 53080 }
  source: "a systematic understanding of key aspects of their field of study, including acquisition of coherent and detailed knowledge, at least some of which is at, or informed by, the forefront of defined aspects of a discipline"
  stem: none
  statementType: descriptor
  force: threshold
  level: fheq:6
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: student
  verbs: [informed]
  about: "systematic understanding reaching the forefront"
  themes: [none]
  paraphrase: "Understands key aspects of the field systematically, with coherent, detailed knowledge, some of it at or informed by the forefront of the discipline."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b2
  locator: { number: "4.15.b2", headingPath: ["4.15 honours degree (FHEQ 6)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 53085, end: 53183 }
  source: "an ability to deploy accurately established techniques of analysis and enquiry within a discipline"
  stem: none
  statementType: descriptor
  force: threshold
  level: fheq:6
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: student
  verbs: [deploy]
  about: "accurate use of established techniques"
  themes: [none]
  paraphrase: "Uses the discipline's established techniques of analysis and enquiry accurately."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b3.1
  locator: { number: "4.15.b3.1", headingPath: ["4.15 honours degree (FHEQ 6)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 53242, end: 53379 }
  source: "to devise and sustain arguments, and/or to solve problems, using ideas and techniques, some of which are at the forefront of a discipline"
  stem: qaa/fheq-2024/4.15.b3
  statementType: descriptor
  force: threshold
  level: fheq:6
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: student
  verbs: [devise, sustain, solve, using]
  about: "arguing and solving problems with forefront ideas"
  themes: [none]
  paraphrase: "Builds and keeps up arguments, or solves problems, drawing partly on forefront ideas and techniques."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b3.2
  locator: { number: "4.15.b3.2", headingPath: ["4.15 honours degree (FHEQ 6)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 53384, end: 53506 }
  source: "to describe and comment upon particular aspects of current research, or equivalent advanced scholarship, in the discipline"
  stem: qaa/fheq-2024/4.15.b3
  statementType: descriptor
  force: threshold
  level: fheq:6
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: student
  verbs: [describe, comment]
  about: "commenting on current research"
  themes: [none]
  paraphrase: "Describes and comments on aspects of current research or advanced scholarship in the discipline."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b4
  locator: { number: "4.15.b4", headingPath: ["4.15 honours degree (FHEQ 6)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 53511, end: 53580 }
  source: "an appreciation of the uncertainty, ambiguity and limits of knowledge"
  stem: none
  statementType: descriptor
  force: threshold
  level: fheq:6
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: student
  verbs: []
  about: "appreciating uncertainty and limits of knowledge"
  themes: [none]
  paraphrase: "Appreciates that knowledge is uncertain, ambiguous and limited."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b5
  locator: { number: "4.15.b5", headingPath: ["4.15 honours degree (FHEQ 6)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 53585, end: 53782 }
  source: "the ability to manage their own learning, and to make use of scholarly reviews and primary sources (for example, refereed research articles and/or original materials appropriate to the discipline)."
  stem: none
  statementType: descriptor
  force: threshold
  level: fheq:6
  dimension: threshold-outcomes
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: student
  verbs: [manage, make]
  about: "managing own learning with scholarly and primary sources"
  themes: [none]
  paraphrase: "Manages their own learning and uses scholarly reviews and primary sources, such as refereed articles or original materials."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b6
  locator: { number: "4.15.b6", headingPath: ["4.15 honours degree (FHEQ 6)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 53844, end: 54014 }
  source: "apply the methods and techniques that they have learned to review, consolidate, extend and apply their knowledge and understanding, and to initiate and carry out projects"
  stem: none
  statementType: descriptor
  force: will
  level: fheq:6
  dimension: wider-abilities
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: holder
  verbs: [apply, learned, review, consolidate, extend, initiate, carry]
  about: "applying methods to extend knowledge; projects"
  themes: [none]
  paraphrase: "Applies learned methods and techniques to review, consolidate, extend and apply knowledge, and to start and carry out projects."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b7
  locator: { number: "4.15.b7", headingPath: ["4.15 honours degree (FHEQ 6)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 54019, end: 54242 }
  source: "critically evaluate arguments, assumptions, abstract concepts and data (that may be incomplete), to make judgements, and to frame appropriate questions to achieve a solution - or identify a range of solutions - to a problem"
  stem: none
  statementType: descriptor
  force: will
  level: fheq:6
  dimension: wider-abilities
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: holder
  verbs: [evaluate, make, frame, achieve, identify]
  about: "critical evaluation and framing questions"
  themes: [none]
  paraphrase: "Evaluates arguments, assumptions, abstract ideas and possibly incomplete data critically, judges, and frames questions that lead to one or several solutions."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b8
  locator: { number: "4.15.b8", headingPath: ["4.15 honours degree (FHEQ 6)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 54247, end: 54350 }
  source: "communicate information, ideas, problems and solutions to both specialist and non-specialist audiences."
  stem: none
  statementType: descriptor
  force: will
  level: fheq:6
  dimension: wider-abilities
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: holder
  verbs: [communicate]
  about: "communicating to specialist and general audiences"
  themes: [none]
  paraphrase: "Communicates information, ideas, problems and solutions to specialists and non-specialists."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b9.1
  locator: { number: "4.15.b9.1", headingPath: ["4.15 honours degree (FHEQ 6)", "Qualities and transferable skills of holders (4.3)"] }
  span: { start: 54456, end: 54510 }
  source: "the exercise of initiative and personal responsibility"
  stem: qaa/fheq-2024/4.15.b9
  statementType: descriptor
  force: will
  level: fheq:6
  dimension: employment-qualities
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: holder
  verbs: []
  about: "initiative and personal responsibility"
  themes: [none]
  paraphrase: "Employment needing initiative and personal responsibility."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b9.2
  locator: { number: "4.15.b9.2", headingPath: ["4.15 honours degree (FHEQ 6)", "Qualities and transferable skills of holders (4.3)"] }
  span: { start: 54515, end: 54568 }
  source: "decision-making in complex and unpredictable contexts"
  stem: qaa/fheq-2024/4.15.b9
  statementType: descriptor
  force: will
  level: fheq:6
  dimension: employment-qualities
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: holder
  verbs: []
  about: "decisions in complex, unpredictable contexts"
  themes: [none]
  paraphrase: "Employment needing decisions in complex and unpredictable contexts."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.b9.3
  locator: { number: "4.15.b9.3", headingPath: ["4.15 honours degree (FHEQ 6)", "Qualities and transferable skills of holders (4.3)"] }
  span: { start: 54573, end: 54682 }
  source: "the learning ability needed to undertake appropriate further training of a professional or equivalent nature."
  stem: qaa/fheq-2024/4.15.b9
  statementType: descriptor
  force: will
  level: fheq:6
  dimension: employment-qualities
  award: "a bachelor's degree with honours"
  appliesTo: "the award of a bachelor's degree with honours"
  addressee: holder
  verbs: [needed, undertake]
  about: "learning ability for professional training"
  themes: [none]
  paraphrase: "Employment needing the learning ability for further professional or equivalent training."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b1
  locator: { number: "4.17.b1", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 59751, end: 59986 }
  source: "a systematic understanding of knowledge, and a critical awareness of current problems and/or new insights, much of which is at, or informed by, the forefront of their academic discipline, field of study or area of professional practice"
  stem: none
  statementType: descriptor
  force: threshold
  level: [fheq:7, fqheis:11]
  dimension: threshold-outcomes
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: student
  verbs: [informed]
  about: "systematic understanding; critical awareness at the forefront"
  themes: [none]
  paraphrase: "Understands knowledge systematically and is critically aware of current problems or new insights, much of it at or informed by the forefront of the discipline or practice."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b2
  locator: { number: "4.17.b2", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 59991, end: 60091 }
  source: "a comprehensive understanding of techniques applicable to their own research or advanced scholarship"
  stem: none
  statementType: descriptor
  force: threshold
  level: [fheq:7, fqheis:11]
  dimension: threshold-outcomes
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: student
  verbs: []
  about: "comprehensive understanding of research techniques"
  themes: [none]
  paraphrase: "Understands comprehensively the techniques that apply to their own research or advanced scholarship."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b3
  locator: { number: "4.17.b3", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 60096, end: 60295 }
  source: "originality in the application of knowledge, together with a practical understanding of how established techniques of research and enquiry are used to create and interpret knowledge in the discipline"
  stem: none
  statementType: descriptor
  force: threshold
  level: [fheq:7, fqheis:11]
  dimension: threshold-outcomes
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: student
  verbs: [used, create, interpret]
  about: "originality in applying knowledge; how research creates knowledge"
  themes: [none]
  paraphrase: "Applies knowledge with originality and understands in practice how established research techniques create and interpret knowledge."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b4.1
  locator: { number: "4.17.b4.1", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 60353, end: 60435 }
  source: "to evaluate critically current research and advanced scholarship in the discipline"
  stem: qaa/fheq-2024/4.17.b4
  statementType: descriptor
  force: threshold
  level: [fheq:7, fqheis:11]
  dimension: threshold-outcomes
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: student
  verbs: [evaluate]
  about: "critically evaluating current research"
  themes: [none]
  paraphrase: "Evaluates current research and advanced scholarship critically."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b4.2
  locator: { number: "4.17.b4.2", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 60438, end: 60544 }
  source: "to evaluate methodologies and develop critiques of them and, where appropriate, to propose new hypotheses."
  stem: qaa/fheq-2024/4.17.b4
  statementType: descriptor
  force: threshold
  level: [fheq:7, fqheis:11]
  dimension: threshold-outcomes
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: student
  verbs: [evaluate, develop, propose]
  about: "critiquing methodologies; proposing hypotheses"
  themes: [none]
  paraphrase: "Evaluates and critiques methodologies and, where fitting, proposes new hypotheses."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b5
  locator: { number: "4.17.b5", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 60606, end: 60808 }
  source: "deal with complex issues - both systematically and creatively, make sound judgements in the absence of complete data, and communicate their conclusions clearly to specialist and non-specialist audiences"
  stem: none
  statementType: descriptor
  force: will
  level: [fheq:7, fqheis:11]
  dimension: wider-abilities
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: holder
  verbs: [deal, make, communicate]
  about: "complex issues, judgement without complete data"
  themes: [none]
  paraphrase: "Deals with complex issues systematically and creatively, judges soundly without complete data, and communicates conclusions clearly to specialists and non-specialists."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b6
  locator: { number: "4.17.b6", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 60813, end: 60983 }
  source: "demonstrate self-direction and originality in tackling and solving problems, and act autonomously in planning and implementing tasks at a professional or equivalent level"
  stem: none
  statementType: descriptor
  force: will
  level: [fheq:7, fqheis:11]
  dimension: wider-abilities
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: holder
  verbs: [demonstrate, tackling, solving, act, planning, implementing]
  about: "self-direction, originality and autonomy"
  themes: [none]
  paraphrase: "Shows self-direction and originality in solving problems, and acts autonomously in planning and carrying out tasks at a professional level."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b7
  locator: { number: "4.17.b7", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 60988, end: 61085 }
  source: "continue to advance their knowledge and understanding, and to develop new skills to a high level."
  stem: none
  statementType: descriptor
  force: will
  level: [fheq:7, fqheis:11]
  dimension: wider-abilities
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: holder
  verbs: [continue, advance, develop]
  about: "continuing to advance knowledge and skills"
  themes: [none]
  paraphrase: "Keeps advancing knowledge and understanding and develops new skills to a high level."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b8.1
  locator: { number: "4.17.b8.1", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Qualities and transferable skills of holders (4.3)"] }
  span: { start: 61189, end: 61243 }
  source: "the exercise of initiative and personal responsibility"
  stem: qaa/fheq-2024/4.17.b8
  statementType: descriptor
  force: will
  level: [fheq:7, fqheis:11]
  dimension: employment-qualities
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: holder
  verbs: []
  about: "initiative and personal responsibility"
  themes: [none]
  paraphrase: "Employment needing initiative and personal responsibility."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b8.2
  locator: { number: "4.17.b8.2", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Qualities and transferable skills of holders (4.3)"] }
  span: { start: 61246, end: 61301 }
  source: "decision-making in complex and unpredictable situations"
  stem: qaa/fheq-2024/4.17.b8
  statementType: descriptor
  force: will
  level: [fheq:7, fqheis:11]
  dimension: employment-qualities
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: holder
  verbs: []
  about: "decisions in complex, unpredictable situations"
  themes: [none]
  paraphrase: "Employment needing decisions in complex and unpredictable situations."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.b8.3
  locator: { number: "4.17.b8.3", headingPath: ["4.17 master's (FHEQ 7, SCQF 11)", "Qualities and transferable skills of holders (4.3)"] }
  span: { start: 61304, end: 61386 }
  source: "the independent learning ability required for continuing professional development."
  stem: qaa/fheq-2024/4.17.b8
  statementType: descriptor
  force: will
  level: [fheq:7, fqheis:11]
  dimension: employment-qualities
  award: "a master's degree"
  appliesTo: "the award of a master's degree"
  addressee: holder
  verbs: [required]
  about: "independent learning for continuing development"
  themes: [none]
  paraphrase: "Employment needing the independent learning ability that continuing professional development requires."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.18.b1
  locator: { number: "4.18.b1", headingPath: ["4.18 doctorate (FHEQ 8, SCQF 12)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 66282, end: 66487 }
  source: "the creation and interpretation of new knowledge, through original research or other advanced scholarship, of a quality to satisfy peer review, extend the forefront of the discipline, and merit publication"
  stem: none
  statementType: descriptor
  force: threshold
  level: [fheq:8, fqheis:12]
  dimension: threshold-outcomes
  award: "a doctorate"
  appliesTo: "the award of a doctorate"
  addressee: student
  verbs: [satisfy, extend, merit]
  about: "creating new knowledge of publishable quality"
  themes: [none]
  paraphrase: "Creates and interprets new knowledge, by original research or other advanced scholarship, good enough to pass peer review, extend the discipline's forefront and merit publication."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.18.b2
  locator: { number: "4.18.b2", headingPath: ["4.18 doctorate (FHEQ 8, SCQF 12)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 66492, end: 66654 }
  source: "a systematic acquisition and understanding of a substantial body of knowledge which is at the forefront of an academic discipline or area of professional practice"
  stem: none
  statementType: descriptor
  force: threshold
  level: [fheq:8, fqheis:12]
  dimension: threshold-outcomes
  award: "a doctorate"
  appliesTo: "the award of a doctorate"
  addressee: student
  verbs: []
  about: "substantial body of knowledge at the forefront"
  themes: [none]
  paraphrase: "Has acquired and understands systematically a substantial body of knowledge at the forefront of the discipline or professional practice."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.18.b3
  locator: { number: "4.18.b3", headingPath: ["4.18 doctorate (FHEQ 8, SCQF 12)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 66659, end: 66899 }
  source: "the general ability to conceptualise, design and implement a project for the generation of new knowledge, applications or understanding at the forefront of the discipline, and to adjust the project design in the light of unforeseen problems"
  stem: none
  statementType: descriptor
  force: threshold
  level: [fheq:8, fqheis:12]
  dimension: threshold-outcomes
  award: "a doctorate"
  appliesTo: "the award of a doctorate"
  addressee: student
  verbs: [conceptualise, design, implement, adjust]
  about: "designing and adjusting research projects"
  themes: [none]
  paraphrase: "Can conceive, design and carry out a project that generates new knowledge, applications or understanding at the forefront, and adjust its design when unforeseen problems arise."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.18.b4
  locator: { number: "4.18.b4", headingPath: ["4.18 doctorate (FHEQ 8, SCQF 12)", "Outcomes demonstrated for the award (the threshold, 4.2)"] }
  span: { start: 66904, end: 66997 }
  source: "a detailed understanding of applicable techniques for research and advanced academic enquiry."
  stem: none
  statementType: descriptor
  force: threshold
  level: [fheq:8, fqheis:12]
  dimension: threshold-outcomes
  award: "a doctorate"
  appliesTo: "the award of a doctorate"
  addressee: student
  verbs: []
  about: "detailed understanding of research techniques"
  themes: [none]
  paraphrase: "Understands in detail the techniques for research and advanced academic enquiry that apply."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.18.b5
  locator: { number: "4.18.b5", headingPath: ["4.18 doctorate (FHEQ 8, SCQF 12)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 67059, end: 67284 }
  source: "make informed judgements on complex issues in specialist fields, often in the absence of complete data, and be able to communicate their ideas and conclusions clearly and effectively to specialist and non-specialist audiences"
  stem: none
  statementType: descriptor
  force: will
  level: [fheq:8, fqheis:12]
  dimension: wider-abilities
  award: "a doctorate"
  appliesTo: "the award of a doctorate"
  addressee: holder
  verbs: [make, communicate]
  about: "judgements on complex issues; communicating to all audiences"
  themes: [none]
  paraphrase: "Makes informed judgements on complex specialist issues, often without complete data, and communicates ideas and conclusions clearly and effectively to specialists and non-specialists."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.18.b6
  locator: { number: "4.18.b6", headingPath: ["4.18 doctorate (FHEQ 8, SCQF 12)", "Wider abilities of typical holders (4.3)"] }
  span: { start: 67289, end: 67463 }
  source: "continue to undertake pure and/or applied research and development at an advanced level, contributing substantially to the development of new techniques, ideas or approaches."
  stem: none
  statementType: descriptor
  force: will
  level: [fheq:8, fqheis:12]
  dimension: wider-abilities
  award: "a doctorate"
  appliesTo: "the award of a doctorate"
  addressee: holder
  verbs: [continue, undertake, contributing]
  about: "continuing advanced research and development"
  themes: [none]
  paraphrase: "Continues to carry out advanced pure or applied research and development, contributing substantially to new techniques, ideas or approaches."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.18.b7
  locator: { number: "4.18.b7", headingPath: ["4.18 doctorate (FHEQ 8, SCQF 12)", "Qualities and transferable skills of holders (4.3)"] }
  span: { start: 67491, end: 67722 }
  source: "the qualities and transferable skills necessary for employment requiring the exercise of personal responsibility and largely autonomous initiative in complex and unpredictable situations, in professional or equivalent environments."
  stem: none
  statementType: descriptor
  force: will
  level: [fheq:8, fqheis:12]
  dimension: employment-qualities
  award: "a doctorate"
  appliesTo: "the award of a doctorate"
  addressee: holder
  verbs: []
  about: "qualities for autonomous work in complex situations"
  themes: [none]
  paraphrase: "Has the qualities and transferable skills for work needing personal responsibility and largely autonomous initiative in complex, unpredictable professional settings."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/use.1
  locator: { number: "use.1", headingPath: ["How the Frameworks are used"] }
  span: { start: 8564, end: 8688 }
  source: "Providers in Scotland, Wales and Northern Ireland are required to adhere to the full framework that applies to their nation."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "provider"
  verbs: [required, adhere]
  about: "full adherence outside England"
  themes: [none]
  paraphrase: "Providers in Scotland, Wales and Northern Ireland must follow the whole framework for their nation."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/use.2
  locator: { number: "use.2", headingPath: ["How the Frameworks are used"] }
  span: { start: 8774, end: 8969 }
  source: "These form part of the regulatory requirements that providers registered with the Office for Students (OfS) must adhere to in England through compliance with ongoing condition of registration B5."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "provider (England, OfS-registered)"
  verbs: [adhere]
  about: "England: sector-recognised standards under B5"
  themes: [none]
  paraphrase: "In England, parts of the framework are sector-recognised standards that OfS-registered providers must meet under condition B5."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/use.3
  locator: { number: "use.3", headingPath: ["How the Frameworks are used"] }
  span: { start: 8970, end: 9090 }
  source: "Providers registered in England should refer to the OfS regulatory framework, including the sector-recognised standards."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "provider (England)"
  verbs: [refer]
  about: "England: refer to the OfS framework"
  themes: [none]
  paraphrase: "Providers registered in England should consult the OfS regulatory framework and its sector-recognised standards."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/2.2.a
  locator: { number: "2.2.a", headingPath: ["2.2"] }
  span: { start: 14224, end: 14378 }
  source: "All degree-awarding bodies in Northern Ireland, Scotland and Wales ensure that their qualifications are awarded in accordance with the relevant framework."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [ensure, awarded]
  about: "awarding by the framework"
  themes: [none]
  paraphrase: "In Northern Ireland, Scotland and Wales, every degree-awarding body awards its qualifications by the relevant framework."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/2.2.b
  locator: { number: "2.2.b", headingPath: ["2.2"] }
  span: { start: 14379, end: 14598 }
  source: "In England, providers may also make use of the Frameworks but providers registered with the OfS are required to comply with the OfS ongoing condition of registration B5 that sets out the OfS sector-recognised standards."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "provider (England, OfS-registered)"
  verbs: [required, comply]
  about: "England: comply with B5"
  themes: [none]
  paraphrase: "In England, OfS-registered providers must comply with condition B5 and its sector-recognised standards."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/2.3
  locator: { number: "2.3", headingPath: ["2.3"] }
  span: { start: 14678, end: 14904 }
  source: "Education providers are entitled to claim that their qualifications are assigned to a level of the UK frameworks for higher education qualifications only if those qualifications are awarded by an approved degree-awarding body."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "provider"
  verbs: [claim, awarded]
  about: "claiming a framework level"
  themes: [none]
  paraphrase: "A provider may claim a framework level for a qualification only when a recognised degree-awarding body awards it."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/2.9.a
  locator: { number: "2.9.a", headingPath: ["2.9"] }
  span: { start: 16954, end: 17170 }
  source: "Individual courses of study have course learning outcomes which specify the intended outcomes from that course which must be achieved for the award of a specific qualification from an individual degree-awarding body."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [specify, achieved]
  about: "course outcomes required for award"
  themes: [none]
  paraphrase: "Each course has learning outcomes that must be met for its qualification to be awarded."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/2.9.b
  locator: { number: "2.9.b", headingPath: ["2.9"] }
  span: { start: 17171, end: 17266 }
  source: "The course learning outcomes are required to align with the relevant qualification descriptors."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [required, align]
  about: "outcomes aligned to descriptors"
  themes: [none]
  paraphrase: "Course learning outcomes must line up with the relevant qualification descriptor."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/2.12
  locator: { number: "2.12", headingPath: ["2.12"] }
  span: { start: 18263, end: 18416 }
  source: "The Quality Code asks providers to ensure that the academic standards of courses meet the requirements of the relevant national qualifications framework."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "provider"
  verbs: [asks, ensure, meet]
  about: "standards meet the framework"
  themes: [none]
  paraphrase: "Providers are asked to make sure their courses' academic standards meet the national framework's requirements."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/2.13
  locator: { number: "2.13", headingPath: ["2.13"] }
  span: { start: 18657, end: 18843 }
  source: "However, they need to\n\n7\n\nunderstand how threshold academic standards are both set and maintained, and are responsible for maintaining the academic standards of the degree-awarding body."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "delivery partner"
  verbs: [need, understand, maintaining]
  about: "partners maintain the awarding body's standards"
  themes: [none]
  paraphrase: "Providers that teach for a degree-awarding body must understand how threshold standards are set and kept, and keep that body's standards."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/4.10.i1
  locator: { number: "4.10.i1", headingPath: ["4.10"] }
  span: { start: 40990, end: 41075 }
  source: "is for any Certificate of Higher Education, which should meet the descriptor in full."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [meet]
  about: "CertHE meets the descriptor in full"
  themes: [none]
  paraphrase: "Every Certificate of Higher Education should meet the Level 4 descriptor in full."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.10.i2
  locator: { number: "4.10.i2", headingPath: ["4.10"] }
  span: { start: 41076, end: 41205 }
  source: "This qualification descriptor should also be used as a reference point for other qualifications aligned with Level 4 of the FHEQ."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "reference point for other Level 4 awards"
  themes: [none]
  paraphrase: "The Level 4 descriptor should also serve as the reference point for other Level 4 qualifications."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/4.12.i1
  locator: { number: "4.12.i1", headingPath: ["4.12"] }
  span: { start: 44750, end: 44820 }
  source: "is for any foundation degree which should meet the descriptor in full."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [meet]
  about: "foundation degree meets the descriptor in full"
  themes: [none]
  paraphrase: "Every foundation degree should meet the Level 5 descriptor in full."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.12.i2
  locator: { number: "4.12.i2", headingPath: ["4.12"] }
  span: { start: 44821, end: 45007 }
  source: "This qualification descriptor should also be used as a reference point for other qualifications at Level 5 of the FHEQ, such as Diplomas of Higher Education and Higher National Diplomas."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "reference point for DipHE, HND and others"
  themes: [none]
  paraphrase: "The Level 5 descriptor should also be the reference point for other Level 5 qualifications, such as DipHEs and HNDs."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/4.15.i1
  locator: { number: "4.15.i1", headingPath: ["4.15"] }
  span: { start: 52523, end: 52606 }
  source: "is for any bachelor's degree with honours which should meet the descriptor in full."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [meet]
  about: "honours degree meets the descriptor in full"
  themes: [none]
  paraphrase: "Every honours degree should meet the Level 6 descriptor in full."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.15.i2
  locator: { number: "4.15.i2", headingPath: ["4.15"] }
  span: { start: 52607, end: 52778 }
  source: "This qualification descriptor should also be used as a reference point for other qualifications at Level 6 of the FHEQ, including bachelor's degrees and graduate diplomas."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "reference point for ordinary degrees and graduate diplomas"
  themes: [none]
  paraphrase: "The Level 6 descriptor should also be the reference point for other Level 6 qualifications, ordinary bachelor's degrees and graduate diplomas among them."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/4.17.i1
  locator: { number: "4.17.i1", headingPath: ["4.17"] }
  span: { start: 59404, end: 59472 }
  source: "is for any master's degree which should meet the descriptor in full."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [meet]
  about: "master's meets the descriptor in full"
  themes: [none]
  paraphrase: "Every master's degree should meet the Level 7 (SCQF 11) descriptor in full."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.17.i2
  locator: { number: "4.17.i2", headingPath: ["4.17"] }
  span: { start: 59473, end: 59683 }
  source: "This qualification descriptor should also be used as a reference point for other qualifications at Level 7 on the FHEQ/SCQF Level 11 on the FQHEIS, including postgraduate certificates and postgraduate diplomas."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "reference point for PG certificates and diplomas"
  themes: [none]
  paraphrase: "The Level 7 descriptor should also be the reference point for other Level 7 qualifications, including postgraduate certificates and diplomas."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/4.18.i1
  locator: { number: "4.18.i1", headingPath: ["4.18"] }
  span: { start: 66032, end: 66100 }
  source: "is for any doctoral degree which should meet the descriptor in full."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [meet]
  about: "doctorate meets the descriptor in full"
  themes: [none]
  paraphrase: "Every doctoral degree should meet the Level 8 (SCQF 12) descriptor in full."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.18.i2
  locator: { number: "4.18.i2", headingPath: ["4.18"] }
  span: { start: 66101, end: 66214 }
  source: "This qualification descriptor should also be used as a reference point for other Level 8/Level 12 qualifications."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "reference point for other Level 8 awards"
  themes: [none]
  paraphrase: "The doctoral descriptor should also be the reference point for other Level 8 (SCQF 12) qualifications."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/4.5
  locator: { number: "4.5", headingPath: ["4.5"] }
  span: { start: 38469, end: 38713 }
  source: "Where a qualification type other than the main qualification has a smaller volume of learning, the qualification descriptor for the degree is used as a reference point and the sub-degree qualification is expected to meet the descriptor in part."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used, expected, meet]
  about: "smaller awards meet the descriptor in part"
  themes: [none]
  paraphrase: "A smaller qualification at a level takes the main qualification's descriptor as its reference and is expected to meet part of it."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/4.9
  locator: { number: "4.9", headingPath: ["4.9"] }
  span: { start: 40696, end: 40837 }
  source: "Providers in England should also refer to the OfS sector-recognised standards which align with the content of the descriptors appearing here."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "provider (England)"
  verbs: [refer]
  about: "England: refer to the OfS standards"
  themes: [none]
  paraphrase: "Providers in England should also consult the OfS sector-recognised standards, which match the descriptors."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/5.5
  locator: { number: "5.5", headingPath: ["5.5"] }
  span: { start: 71725, end: 72016 }
  source: "Degree-awarding bodies (and their delivering partners) are responsible for ensuring that individual course learning outcomes (or award criteria in the case of research degrees) align with the appropriate qualification descriptor in the relevant framework for higher education qualifications."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body and partners"
  verbs: [ensuring, align]
  about: "aligning course outcomes"
  themes: [none]
  paraphrase: "Degree-awarding bodies and their partners must make sure course learning outcomes, or research award criteria, align with the right qualification descriptor."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.1.a
  locator: { number: "6.1.a", headingPath: ["6.1"] }
  span: { start: 73181, end: 73335 }
  source: "degree-awarding bodies are responsible for demonstrating that each of their qualifications is assigned the appropriate level of the relevant UK framework."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [demonstrating, assigned]
  about: "showing each qualification's level"
  themes: [none]
  paraphrase: "Each degree-awarding body must show that every qualification it awards sits at the right framework level."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/6.1.b
  locator: { number: "6.1.b", headingPath: ["6.1"] }
  span: { start: 73336, end: 73839 }
  source: "Degree-awarding bodies consider the framework level with which the majority of course outcomes most closely correspond (using the qualification descriptor as a reference point). For example, a course leading to a graduate certificate or graduate diploma might have some outcomes at Level 7 on the FHEQ/SCQF Level 11 on the FQHEIS, but positioning it at this level and the use of the 'postgraduate' title for the award would be justified only if most or all of the outcomes were assessed at those levels."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [consider, justified]
  about: "level set by most outcomes"
  themes: [none]
  paraphrase: "A qualification's level is the one most of its outcomes match; a postgraduate level and title are justified only if most or all outcomes are assessed there."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.3.b1
  locator: { number: "6.3.b1", headingPath: ["6.3"] }
  span: { start: 74472, end: 74637 }
  source: "the alignment between the intended learning outcomes of the course and the qualification descriptors of the relevant UK framework for higher education qualifications"
  stem: qaa/fheq-2024/6.3
  statementType: provider-requirement
  force: should
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: []
  about: "alignment with descriptors"
  themes: [none]
  paraphrase: "How well the course's intended outcomes align with the framework's descriptors."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.3.b2
  locator: { number: "6.3.b2", headingPath: ["6.3"] }
  span: { start: 74642, end: 74764 }
  source: "whether there is a sufficient volume of assessed study that will demonstrate that the learning outcomes have been achieved"
  stem: qaa/fheq-2024/6.3
  statementType: provider-requirement
  force: should
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [demonstrate]
  about: "enough assessed study"
  themes: [none]
  paraphrase: "Whether there is enough assessed study to show the outcomes have been met."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.3.b3
  locator: { number: "6.3.b3", headingPath: ["6.3"] }
  span: { start: 74769, end: 74938 }
  source: "whether the design of the curriculum and assessments is such that all students following the course have the opportunity to achieve and demonstrate the intended outcomes"
  stem: qaa/fheq-2024/6.3
  statementType: provider-requirement
  force: should
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [achieve, demonstrate]
  about: "opportunity for every student"
  themes: [none]
  paraphrase: "Whether curriculum and assessment give every student the chance to achieve and show the intended outcomes."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.3.b4
  locator: { number: "6.3.b4", headingPath: ["6.3"] }
  span: { start: 74943, end: 75065 }
  source: "the regulatory and other requirements of any PSRBs which recognise or accredit specific courses for professional purposes."
  stem: qaa/fheq-2024/6.3
  statementType: provider-requirement
  force: should
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [recognise, accredit]
  about: "professional body requirements"
  themes: [none]
  paraphrase: "The requirements of any professional, statutory or regulatory body that recognises or accredits the course."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.4
  locator: { number: "6.4", headingPath: ["6.4"] }
  span: { start: 75503, end: 75691 }
  source: "However, a 'degree', for example, can only be awarded when the course learning outcomes, which should have been aligned to the relevant qualification descriptor, have been met or exceeded."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [awarded, aligned, met, exceeded]
  about: "award only on meeting outcomes"
  themes: [none]
  paraphrase: "A degree can be awarded only when its course outcomes, aligned to the descriptor, are met or exceeded."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.5
  locator: { number: "6.5", headingPath: ["6.5"] }
  span: { start: 75975, end: 76169 }
  source: "Degreeawarding bodies judge student performance against the standards set and ensure that\n\n30\n\nqualifications are awarded only where the relevant learning outcomes have been achieved in this way"
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [judge, ensure, awarded]
  about: "award only on assessed achievement"
  themes: [none]
  paraphrase: "Degree-awarding bodies judge performance against the set standards and award qualifications only where assessment shows the outcomes achieved."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.6
  locator: { number: "6.6", headingPath: ["6.6"] }
  span: { start: 76263, end: 76646 }
  source: "A student who has failed to achieve the required course learning outcomes for a qualification at a specific level may be considered for the award of a qualification at a lower level. However, the lower qualification is awarded only if the student has demonstrated the course learning outcomes required (or award criteria in the case of research degrees) for that lower qualification."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [considered, awarded, demonstrated]
  about: "lower awards only on their own outcomes"
  themes: [none]
  paraphrase: "A student who misses one qualification's outcomes may be considered for a lower one, but gets it only by having shown that lower qualification's outcomes."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.6.b1
  locator: { number: "6.6.b1", headingPath: ["6.6"] }
  span: { start: 76663, end: 76906 }
  source: "a student who has failed to achieve the required outcomes for a bachelor's degree may only be awarded a DipHE if the student has demonstrated the outcomes specified for a DipHE (at Level 5 on the FHEQ/SCQF Level 8 on the FQHEIS) on that course"
  stem: qaa/fheq-2024/6.6
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [awarded, demonstrated]
  about: "example: DipHE after a bachelor's"
  themes: [none]
  paraphrase: "For example, a student who misses a bachelor's gets a DipHE only by having shown the DipHE outcomes on that course."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.6.b2
  locator: { number: "6.6.b2", headingPath: ["6.6"] }
  span: { start: 76911, end: 77227 }
  source: "a student who has failed to achieve the required outcomes for a doctoral degree (at Level 8 on the FHEQ/SCQF Level 12 on the FQHEIS) may only be awarded an MPhil if the student has demonstrated the outcomes and satisfied the award criteria specified for an MPhil (at Level 7 on the FHEQ/SCQF Level 11 on the FQHEIS)."
  stem: qaa/fheq-2024/6.6
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [awarded, demonstrated, satisfied]
  about: "example: MPhil after a doctorate"
  themes: [none]
  paraphrase: "For example, a student who misses a doctorate gets an MPhil only by having shown its outcomes and met its award criteria."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.7.b1
  locator: { number: "6.7.b1", headingPath: ["6.7"] }
  span: { start: 77274, end: 77467 }
  source: "the course learning outcomes/award criteria required for each of their courses and qualifications are specified clearly (including those for any intermediate or exit qualifications within them)"
  stem: qaa/fheq-2024/6.7
  statementType: provider-requirement
  force: must
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [required, specified]
  about: "outcomes specified clearly"
  themes: [none]
  paraphrase: "The outcomes or criteria required for each course and qualification, exit awards included, are clearly specified."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.7.b2
  locator: { number: "6.7.b2", headingPath: ["6.7"] }
  span: { start: 77472, end: 77592 }
  source: "achievement of the relevant course learning outcomes/research criteria is demonstrated before a qualification is awarded"
  stem: qaa/fheq-2024/6.7
  statementType: provider-requirement
  force: must
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [demonstrated, awarded]
  about: "achievement shown before award"
  themes: [none]
  paraphrase: "Achievement of the course outcomes or research criteria is shown before any award."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.7.b3
  locator: { number: "6.7.b3", headingPath: ["6.7"] }
  span: { start: 77597, end: 77812 }
  source: "assessment procedures that permit compensation or condonement are not applied in a way that might allow a qualification to be awarded without achievement, in full, of the course learning outcomes being demonstrated."
  stem: qaa/fheq-2024/6.7
  statementType: provider-requirement
  force: must
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [permit, applied, awarded]
  about: "compensation and condonement limited"
  themes: [none]
  paraphrase: "Compensation or condonement is never applied so that a qualification is awarded without the course outcomes shown in full."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.9
  locator: { number: "6.9", headingPath: ["6.9"] }
  span: { start: 78101, end: 78272 }
  source: "The title of any qualification accurately and appropriately reflects the level of achievements, the nature, volume and field(s) of study undertaken, and is not misleading."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [reflects]
  about: "titles reflect level, nature and volume"
  themes: [none]
  paraphrase: "A qualification's title reflects its level, nature, volume and field of study accurately and does not mislead."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.10.b1
  locator: { number: "6.10.b1", headingPath: ["6.10"] }
  span: { start: 78401, end: 78806 }
  source: "the titles 'honours' (for example, bachelor's degree with honours), 'master' (for example, Master of Arts) and 'doctor' (for example, Doctor of Philosophy) are used only for qualifications that meet, in full, the expectations of the qualification descriptors at Level 6, 7 and 8 on the FHEQ/SCQF Level 10, 11 and 12 on the FQHEIS respectively (but see note to the master's degree qualification descriptor)"
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used, meet]
  about: "honours, master, doctor titles"
  themes: [none]
  paraphrase: "The titles \"honours\", \"master\" and \"doctor\" are used only for qualifications that meet the Level 6, 7 or 8 (SCQF 10, 11, 12) descriptor in full."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.10.b2
  locator: { number: "6.10.b2", headingPath: ["6.10"] }
  span: { start: 78811, end: 79136 }
  source: "titles with the stem 'graduate' (for example, 'graduate diploma') are used for qualifications from courses of study that typically require graduate entry, or its\n\n31\n\nequivalent, and have learning outcomes that match relevant parts of the descriptor for a qualification at Level 6 on the FHEQ/SCQF Level 9 or 10 on the FQHEIS"
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used, require, match]
  about: "graduate titles"
  themes: [none]
  paraphrase: "\"Graduate\" titles are for courses that typically need graduate entry and have outcomes matching parts of the Level 6 (SCQF 9 or 10) descriptor."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.10.b3
  locator: { number: "6.10.b3", headingPath: ["6.10"] }
  span: { start: 79140, end: 79418 }
  source: "titles with the stem 'postgraduate' (for example, 'postgraduate diploma') are restricted to qualifications where the learning outcomes of the course of study match or exceed relevant parts of the descriptor for a qualification at Level 7 on the FHEQ/SCQF Level 11 on the FQHEIS."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [restricted, match, exceed]
  about: "postgraduate titles"
  themes: [none]
  paraphrase: "\"Postgraduate\" titles are restricted to qualifications whose outcomes match or exceed parts of the Level 7 (SCQF 11) descriptor."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.11.a
  locator: { number: "6.11.a", headingPath: ["6.11"] }
  span: { start: 79455, end: 79637 }
  source: "the title Postgraduate Certificate in Education is reserved for those PGCE qualifications that are set at Level 7 of the FHEQ and align with the qualification descriptor for Level 7."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [reserved, set, align]
  about: "PGCE at Level 7"
  themes: [none]
  paraphrase: "Only PGCEs set at FHEQ Level 7 and aligned with its descriptor carry the title Postgraduate Certificate in Education."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.11.b
  locator: { number: "6.11.b", headingPath: ["6.11"] }
  span: { start: 79638, end: 79868 }
  source: "The title Professional Graduate Certificate in Education is used for those PGCE qualifications in England, Wales and Northern Ireland that are set at Level 6 of the FHEQ and align with the FHEQ qualification descriptor at Level 6."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used, set, align]
  about: "Professional Graduate PGCE at Level 6"
  themes: [none]
  paraphrase: "PGCEs in England, Wales and Northern Ireland set at FHEQ Level 6 carry the title Professional Graduate Certificate in Education."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.13.b2
  locator: { number: "6.13.b2", headingPath: ["6.13"] }
  span: { start: 81035, end: 81601 }
  source: "Graduate diplomas and certificates are at the same level (Level 6 on the FHEQ/SCQF Level 10 on the FQHEIS) but are differentiated from each other by volume of study and learning outcomes. The title 'certificate' normally signifies learning outcomes which would imply study equivalent to at least one-third of a full-time academic year, and the title 'diploma' normally signifies study equivalent to at least two-thirds of a full-time academic year at the relevant level (and, where credit is awarded, the volume of credit specified by the relevant credit framework)."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [differentiated, signifies]
  about: "graduate certificate and diploma volumes"
  themes: [none]
  paraphrase: "Graduate certificates and diplomas share a level and differ by volume: a certificate normally means at least a third of a full-time year's study, a diploma at least two-thirds."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.13.b3
  locator: { number: "6.13.b3", headingPath: ["6.13"] }
  span: { start: 81606, end: 82176 }
  source: "Postgraduate diplomas and certificates are at the same level (Level 7 on the FHEQ/SCQF Level 11 on the FQHEIS) but are differentiated from each other by volume of study and learning outcomes. The title 'certificate' normally signifies learning outcomes which would imply study equivalent to at least one-third of a full-time academic year, and the title 'diploma' normally signifies study equivalent to at least two-thirds of a full-time academic year at the relevant level (and, where credit is awarded, the volume of credit specified by the relevant credit framework)."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [differentiated, signifies]
  about: "postgraduate certificate and diploma volumes"
  themes: [none]
  paraphrase: "Postgraduate certificates and diplomas share a level and differ by volume: a certificate normally means at least a third of a full-time year, a diploma at least two-thirds."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.14.b1
  locator: { number: "6.14.b1", headingPath: ["6.14"] }
  span: { start: 82560, end: 82644 }
  source: "'foundation degree' is used only in respect of qualifications at Level 5 on the FHEQ"
  stem: qaa/fheq-2024/6.14
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "foundation degree at Level 5"
  themes: [none]
  paraphrase: "\"Foundation degree\" is used only for FHEQ Level 5 qualifications."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.14.b2
  locator: { number: "6.14.b2", headingPath: ["6.14"] }
  span: { start: 82649, end: 82766 }
  source: "'bachelor's (non-honours) degree in Scotland' is used only in respect of qualifications at SCQF Level 9 on the FQHEIS"
  stem: qaa/fheq-2024/6.14
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "Scottish non-honours at SCQF 9"
  themes: [none]
  paraphrase: "\"Bachelor's (non-honours) degree in Scotland\" is used only for SCQF Level 9 qualifications."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.14.b3
  locator: { number: "6.14.b3", headingPath: ["6.14"] }
  span: { start: 82771, end: 82896 }
  source: "'bachelor's degree with honours' is used only in respect of qualifications at Level 6 on the FHEQ/SCQF Level 10 on the FQHEIS"
  stem: qaa/fheq-2024/6.14
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "honours at FHEQ 6 / SCQF 10"
  themes: [none]
  paraphrase: "\"Bachelor's degree with honours\" is used only for FHEQ Level 6 or SCQF Level 10 qualifications."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.14.b4
  locator: { number: "6.14.b4", headingPath: ["6.14"] }
  span: { start: 82901, end: 83011 }
  source: "'master's degree' is used only in respect of qualifications at Level 7 on the FHEQ/SCQF Level 11 on the FQHEIS"
  stem: qaa/fheq-2024/6.14
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "master's at FHEQ 7 / SCQF 11"
  themes: [none]
  paraphrase: "\"Master's degree\" is used only for FHEQ Level 7 or SCQF Level 11 qualifications."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.14.b5
  locator: { number: "6.14.b5", headingPath: ["6.14"] }
  span: { start: 83016, end: 83127 }
  source: "'doctoral degree' is used only in respect of qualifications at Level 8 on the FHEQ/SCQF Level 12 on the FQHEIS."
  stem: qaa/fheq-2024/6.14
  statementType: provider-requirement
  force: must
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "doctorate at FHEQ 8 / SCQF 12"
  themes: [none]
  paraphrase: "\"Doctoral degree\" is used only for FHEQ Level 8 or SCQF Level 12 qualifications."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.15
  locator: { number: "6.15", headingPath: ["6.15"] }
  span: { start: 83252, end: 83503 }
  source: "The abbreviated titles PhD and DPhil are used for qualifications where assessment is solely by a final thesis or published work; or by artefact, composition or performance that is accompanied by a written commentary placing it in its academic context."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "PhD and DPhil titles"
  themes: [none]
  paraphrase: "PhD and DPhil are used where assessment is by thesis or published work alone, or by artefact, composition or performance with a written commentary."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.16
  locator: { number: "6.16", headingPath: ["6.16"] }
  span: { start: 83509, end: 83697 }
  source: "The abbreviated title MPhil is generally used for qualifications awarded following extended master's courses that typically involve a substantial element of research or equivalent enquiry."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [used]
  about: "MPhil title"
  themes: [none]
  paraphrase: "MPhil is generally used for extended master's courses with a substantial research element."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.17
  locator: { number: "6.17", headingPath: ["6.17"] }
  span: { start: 83719, end: 83923 }
  source: "Titles used for doctoral qualifications awarded after courses that include a substantial taught element normally include the name of the discipline in the title (for example, EdD for Doctor of Education)."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [include]
  about: "professional doctorate titles name the discipline"
  themes: [none]
  paraphrase: "Doctorates with a substantial taught element normally name the discipline in their title."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.18.b1
  locator: { number: "6.18.b1", headingPath: ["6.18"] }
  span: { start: 84102, end: 84181 }
  source: "'A and B', where there is an approximately equal balance between two components"
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: []
  about: "A and B titles"
  themes: [none]
  paraphrase: "\"A and B\" where two subjects are about equal."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.18.b2
  locator: { number: "6.18.b2", headingPath: ["6.18"] }
  span: { start: 84186, end: 84297 }
  source: "'A with B' for a major/minor combination where the minor subject accounts for at least a quarter of the course."
  stem: none
  statementType: provider-requirement
  force: must
  forceBasis: inferred
  level: none
  addressee: "degree-awarding body"
  verbs: []
  about: "A with B titles"
  themes: [none]
  paraphrase: "\"A with B\" for a major and minor, the minor at least a quarter of the course."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/6.19
  locator: { number: "6.19", headingPath: ["6.19"] }
  span: { start: 84304, end: 84485 }
  source: "Qualification titles do not normally reflect more than three subject components. Where there are more than three significant components, the title 'Combined Studies' is appropriate."
  stem: none
  statementType: provider-requirement
  force: should
  forceBasis: stated
  level: none
  addressee: "degree-awarding body"
  verbs: [reflect]
  about: "no more than three subjects in a title"
  themes: [none]
  paraphrase: "Titles do not normally name more than three subjects; with more significant components, \"Combined Studies\" fits."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/short/b1
  locator: { number: "annex-b/short/b1", headingPath: ["Annex B: Dublin descriptors", "short cycle"] }
  span: { start: 89299, end: 89619 }
  source: "have demonstrated knowledge and understanding in a field of study that builds upon their general secondary education4 and is typically at a level supported by advanced textbooks; such knowledge provides an underpinning for a field of work or vocation, personal development and further studies to complete the first cycle"
  stem: qaa/fheq-2024/annex-b/short
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:short
  dimension: knowledge-and-understanding
  addressee: student
  verbs: [demonstrated, builds, provides]
  about: "knowledge at advanced-textbook level"
  themes: [none]
  paraphrase: "Knowledge and understanding of a field built on secondary schooling, at the level of advanced textbooks, enough to underpin work, personal growth and study to the end of the first cycle."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/short/b2
  locator: { number: "annex-b/short/b2", headingPath: ["Annex B: Dublin descriptors", "short cycle"] }
  span: { start: 89624, end: 89692 }
  source: "can apply their knowledge and understanding in occupational contexts"
  stem: qaa/fheq-2024/annex-b/short
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:short
  dimension: applying-knowledge
  addressee: student
  verbs: [apply]
  about: "applying knowledge at work"
  themes: [none]
  paraphrase: "Applies knowledge and understanding in occupational settings."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/short/b3
  locator: { number: "annex-b/short/b3", headingPath: ["Annex B: Dublin descriptors", "short cycle"] }
  span: { start: 89697, end: 89808 }
  source: "have the ability to identify and use data to formulate responses to well-defined concrete and abstract problems"
  stem: qaa/fheq-2024/annex-b/short
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:short
  dimension: making-judgements
  addressee: student
  verbs: [identify, use, formulate]
  about: "data for well-defined problems"
  themes: [none]
  paraphrase: "Finds and uses data to answer well-defined problems, concrete and abstract."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/short/b4
  locator: { number: "annex-b/short/b4", headingPath: ["Annex B: Dublin descriptors", "short cycle"] }
  span: { start: 89813, end: 89914 }
  source: "can communicate about their understanding, skills and activities, with peers, supervisors and clients"
  stem: qaa/fheq-2024/annex-b/short
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:short
  dimension: communication
  addressee: student
  verbs: [communicate]
  about: "communicating with peers, supervisors, clients"
  themes: [none]
  paraphrase: "Communicates what they understand and do with peers, supervisors and clients."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/short/b5
  locator: { number: "annex-b/short/b5", headingPath: ["Annex B: Dublin descriptors", "short cycle"] }
  span: { start: 90100, end: 90173 }
  source: "have the learning skills to undertake further studies with some autonomy."
  stem: qaa/fheq-2024/annex-b/short
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:short
  dimension: learning-skills
  addressee: student
  verbs: [undertake]
  about: "further study with some autonomy"
  themes: [none]
  paraphrase: "Has the learning skills to study further with some autonomy."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/1/b1
  locator: { number: "annex-b/1/b1", headingPath: ["Annex B: Dublin descriptors", "first cycle"] }
  span: { start: 90265, end: 90553 }
  source: "have demonstrated knowledge and understanding in a field of study that builds upon their general secondary education, and is typically at a level that, while supported by advanced textbooks, includes some aspects that will be informed by knowledge of the forefront of their field of study"
  stem: qaa/fheq-2024/annex-b/1
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:1
  dimension: knowledge-and-understanding
  addressee: student
  verbs: [demonstrated, builds, includes]
  about: "advanced-textbook knowledge touching the forefront"
  themes: [none]
  paraphrase: "Knowledge and understanding built on secondary schooling, at advanced-textbook level, with some aspects informed by the forefront of the field."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/1/b2
  locator: { number: "annex-b/1/b2", headingPath: ["Annex B: Dublin descriptors", "first cycle"] }
  span: { start: 90558, end: 90816 }
  source: "can apply their knowledge and understanding in a manner that indicates a professional5 approach to their work or vocation, and have competences6 typically demonstrated through devising and sustaining arguments and solving problems within their field of study"
  stem: qaa/fheq-2024/annex-b/1
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:1
  dimension: applying-knowledge
  addressee: student
  verbs: [apply, indicates, demonstrated, devising, sustaining, solving]
  about: "professional approach; arguing and solving problems"
  themes: [none]
  paraphrase: "Applies knowledge in a way that shows a professional approach, with competences shown by building arguments and solving problems in the field."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/1/b3
  locator: { number: "annex-b/1/b3", headingPath: ["Annex B: Dublin descriptors", "first cycle"] }
  span: { start: 90821, end: 91007 }
  source: "have the ability to gather and interpret relevant data (usually within their field of study) to inform judgements that include reflection on relevant social, scientific or ethical issues"
  stem: qaa/fheq-2024/annex-b/1
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:1
  dimension: making-judgements
  addressee: student
  verbs: [gather, interpret, inform]
  about: "data to inform judgements, with reflection"
  themes: [none]
  paraphrase: "Gathers and interprets relevant data to inform judgements that reflect on social, scientific or ethical issues."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/1/b4
  locator: { number: "annex-b/1/b4", headingPath: ["Annex B: Dublin descriptors", "first cycle"] }
  span: { start: 91012, end: 91118 }
  source: "can communicate information, ideas, problems and solutions to both specialist and non-specialist audiences"
  stem: qaa/fheq-2024/annex-b/1
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:1
  dimension: communication
  addressee: student
  verbs: [communicate]
  about: "communicating to any audience"
  themes: [none]
  paraphrase: "Communicates information, ideas, problems and solutions to specialists and non-specialists."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/1/b5
  locator: { number: "annex-b/1/b5", headingPath: ["Annex B: Dublin descriptors", "first cycle"] }
  span: { start: 91123, end: 91258 }
  source: "have developed those learning skills that are necessary for them to continue to undertake further study with a high degree of autonomy."
  stem: qaa/fheq-2024/annex-b/1
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:1
  dimension: learning-skills
  addressee: student
  verbs: [developed, continue, undertake]
  about: "further study with high autonomy"
  themes: [none]
  paraphrase: "Has the learning skills to go on studying with a high degree of autonomy."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/2/b1
  locator: { number: "annex-b/2/b1", headingPath: ["Annex B: Dublin descriptors", "second cycle"] }
  span: { start: 91351, end: 91620 }
  source: "have demonstrated knowledge and understanding that is founded upon and extends and/or enhances that typically associated with the first cycle, and that provides a basis or opportunity for originality in developing and/or applying ideas, often within a research7 context"
  stem: qaa/fheq-2024/annex-b/2
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:2
  dimension: knowledge-and-understanding
  addressee: student
  verbs: [demonstrated, founded, extends, enhances, provides]
  about: "knowledge extending the first cycle; basis for originality"
  themes: [none]
  paraphrase: "Knowledge and understanding that build on and extend the first cycle and ground original development or application of ideas, often through research."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/2/b2
  locator: { number: "annex-b/2/b2", headingPath: ["Annex B: Dublin descriptors", "second cycle"] }
  span: { start: 91625, end: 91812 }
  source: "can apply their knowledge and understanding, and problem-solving abilities in new or unfamiliar environments within broader (or multidisciplinary) contexts related to their field of study"
  stem: qaa/fheq-2024/annex-b/2
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:2
  dimension: applying-knowledge
  addressee: student
  verbs: [apply]
  about: "problem-solving in new, broader contexts"
  themes: [none]
  paraphrase: "Applies knowledge and problem-solving in new or unfamiliar settings within broader or multidisciplinary contexts."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/2/b3
  locator: { number: "annex-b/2/b3", headingPath: ["Annex B: Dublin descriptors", "second cycle"] }
  span: { start: 91817, end: 92071 }
  source: "have the ability to integrate knowledge and handle complexity, and formulate judgements with incomplete or limited information, but that include reflecting on social and ethical responsibilities linked to the application of their knowledge and judgements"
  stem: qaa/fheq-2024/annex-b/2
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:2
  dimension: making-judgements
  addressee: student
  verbs: [integrate, handle, formulate, reflecting]
  about: "integrating knowledge; judging on limited information"
  themes: [none]
  paraphrase: "Integrates knowledge, handles complexity and forms judgements on incomplete information while reflecting on the social and ethical responsibilities involved."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/2/b4
  locator: { number: "annex-b/2/b4", headingPath: ["Annex B: Dublin descriptors", "second cycle"] }
  span: { start: 92076, end: 92231 }
  source: "can communicate their conclusions, and the knowledge and rationale underpinning these, to specialist and non-specialist audiences clearly and unambiguously"
  stem: qaa/fheq-2024/annex-b/2
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:2
  dimension: communication
  addressee: student
  verbs: [communicate]
  about: "communicating conclusions and their basis"
  themes: [none]
  paraphrase: "Communicates conclusions and the knowledge and reasoning behind them clearly and unambiguously to specialists and non-specialists."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/2/b5
  locator: { number: "annex-b/2/b5", headingPath: ["Annex B: Dublin descriptors", "second cycle"] }
  span: { start: 92236, end: 92356 }
  source: "have the learning skills to allow them to continue to study in a manner that may be largely self-directed or autonomous."
  stem: qaa/fheq-2024/annex-b/2
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:2
  dimension: learning-skills
  addressee: student
  verbs: [allow, continue]
  about: "largely self-directed study"
  themes: [none]
  paraphrase: "Has the learning skills to go on studying in a largely self-directed or autonomous way."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/3/b1
  locator: { number: "annex-b/3/b1", headingPath: ["Annex B: Dublin descriptors", "third cycle"] }
  span: { start: 93685, end: 93826 }
  source: "have demonstrated a systematic understanding of a field of study and mastery of the skills and methods of research associated with that field"
  stem: qaa/fheq-2024/annex-b/3
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:3
  dimension: knowledge-and-understanding
  addressee: student
  verbs: [demonstrated]
  about: "systematic understanding; mastery of research methods"
  themes: [none]
  paraphrase: "Systematic understanding of a field and mastery of its research skills and methods."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/3/b2
  locator: { number: "annex-b/3/b2", headingPath: ["Annex B: Dublin descriptors", "third cycle"] }
  span: { start: 93831, end: 93960 }
  source: "have demonstrated the ability to conceive, design, implement and adapt a substantial process of research with scholarly integrity"
  stem: qaa/fheq-2024/annex-b/3
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:3
  dimension: applying-knowledge
  addressee: student
  verbs: [demonstrated, conceive, design, implement, adapt]
  about: "running a substantial research process with integrity"
  themes: [none]
  paraphrase: "Can conceive, design, carry out and adapt a substantial research process with scholarly integrity."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/3/b3
  locator: { number: "annex-b/3/b3", headingPath: ["Annex B: Dublin descriptors", "third cycle"] }
  span: { start: 93965, end: 94164 }
  source: "have made a contribution through original research that extends the frontier of knowledge by developing a substantial body of work, some of which merits national or international refereed publication"
  stem: qaa/fheq-2024/annex-b/3
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:3
  dimension: making-judgements
  addressee: student
  verbs: [made, extends, developing, merits]
  about: "original contribution; publishable work"
  themes: [none]
  paraphrase: "Has contributed original research that extends the frontier of knowledge through a substantial body of work, part of it worth refereed publication."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/3/b4
  locator: { number: "annex-b/3/b4", headingPath: ["Annex B: Dublin descriptors", "third cycle"] }
  span: { start: 94169, end: 94252 }
  source: "are capable of critical analysis, evaluation and synthesis of new and complex ideas"
  stem: qaa/fheq-2024/annex-b/3
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:3
  dimension: communication
  addressee: student
  verbs: []
  about: "critical analysis and synthesis of new ideas"
  themes: [none]
  paraphrase: "Analyses, evaluates and synthesises new and complex ideas critically."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/3/b5
  locator: { number: "annex-b/3/b5", headingPath: ["Annex B: Dublin descriptors", "third cycle"] }
  span: { start: 94257, end: 94380 }
  source: "can communicate with their peers, the larger scholarly community and with society in general about their areas of expertise"
  stem: qaa/fheq-2024/annex-b/3
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:3
  dimension: learning-skills
  addressee: student
  verbs: [communicate]
  about: "communicating with peers, scholars and society"
  themes: [none]
  paraphrase: "Communicates about their expertise with peers, the wider scholarly community and society."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-b/3/b6
  locator: { number: "annex-b/3/b6", headingPath: ["Annex B: Dublin descriptors", "third cycle"] }
  span: { start: 94385, end: 94542 }
  source: "can be expected to be able to promote, within academic and professional contexts, technological, social or cultural advancement in a knowledge-based society."
  stem: qaa/fheq-2024/annex-b/3
  statementType: descriptor
  force: describes   # the annex: "not meant to be prescriptive", not thresholds
  level: qfehea:3
  dimension: wider-contribution
  addressee: student
  verbs: [promote]
  about: "advancing society through knowledge"
  themes: [none]
  paraphrase: "Can be expected to promote technological, social or cultural advancement in academic and professional settings."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r1/ns
  locator: { number: "annex-d/summary/r1/ns", headingPath: ["Annex D", "Summary table", "Not successful"] }
  span: { start: 107022, end: 107139 }
  source: "did not consistently demonstrate sufficient knowledge and understanding, cognitive, practical and transferable skills"
  stem: qaa/fheq-2024/annex-d/summary/lead/ns
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrate]
  about: "insufficient knowledge and skills, inconsistently"
  themes: [none]
  paraphrase: "Did not show enough knowledge, understanding and cognitive, practical and transferable skill, consistently."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r1/3rd
  locator: { number: "annex-d/summary/r1/3rd", headingPath: ["Annex D", "Summary table", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 107141, end: 107227 }
  source: "demonstrated knowledge and understanding, cognitive, practical and transferable skills"
  stem: qaa/fheq-2024/annex-d/summary/lead/3rd
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "knowledge and skills shown"
  themes: [none]
  paraphrase: "Showed knowledge and understanding and the cognitive, practical and transferable skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r1/2.2
  locator: { number: "annex-d/summary/r1/2.2", headingPath: ["Annex D", "Summary table", "Lower second-class honours (2.2)"] }
  span: { start: 107229, end: 107322 }
  source: "demonstrated strong knowledge and understanding, cognitive, practical and transferable skills"
  stem: qaa/fheq-2024/annex-d/summary/lead/2.2
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "strong knowledge and skills"
  themes: [none]
  paraphrase: "Showed strong knowledge and understanding and strong cognitive, practical and transferable skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r1/2.1
  locator: { number: "annex-d/summary/r1/2.1", headingPath: ["Annex D", "Summary table", "Upper second-class honours (2.1)"] }
  span: { start: 107324, end: 107419 }
  source: "demonstrated thorough knowledge and understanding, cognitive, practical and transferable skills"
  stem: qaa/fheq-2024/annex-d/summary/lead/2.1
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "thorough knowledge and skills"
  themes: [none]
  paraphrase: "Showed thorough knowledge and understanding and thorough cognitive, practical and transferable skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r1/1st
  locator: { number: "annex-d/summary/r1/1st", headingPath: ["Annex D", "Summary table", "First-class honours (1st)"] }
  span: { start: 107421, end: 107529 }
  source: "consistently demonstrated advanced knowledge and understanding, cognitive, practical and transferable skills"
  stem: qaa/fheq-2024/annex-d/summary/lead/1st
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "advanced knowledge and skills, consistently"
  themes: [none]
  paraphrase: "Showed advanced knowledge and understanding and advanced cognitive, practical and transferable skills, throughout."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r2/ns
  locator: { number: "annex-d/summary/r2/ns", headingPath: ["Annex D", "Summary table", "Not successful"] }
  span: { start: 107531, end: 107611 }
  source: "did not consistently demonstrate adequate initiative and personal responsibility"
  stem: qaa/fheq-2024/annex-d/summary/lead/ns
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrate]
  about: "inadequate initiative and responsibility"
  themes: [none]
  paraphrase: "Did not consistently show enough initiative or take enough personal responsibility."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r2/3rd
  locator: { number: "annex-d/summary/r2/3rd", headingPath: ["Annex D", "Summary table", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 107613, end: 107674 }
  source: "demonstrated initiative and exercised personal responsibility"
  stem: qaa/fheq-2024/annex-d/summary/lead/3rd
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, exercised]
  about: "initiative and responsibility shown"
  themes: [none]
  paraphrase: "Showed initiative and took personal responsibility."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r2/2.2
  locator: { number: "annex-d/summary/r2/2.2", headingPath: ["Annex D", "Summary table", "Lower second-class honours (2.2)"] }
  span: { start: 107676, end: 107727 }
  source: "demonstrated initiative and personal responsibility"
  stem: qaa/fheq-2024/annex-d/summary/lead/2.2
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "initiative and responsibility"
  themes: [none]
  paraphrase: "Showed initiative and personal responsibility."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r2/2.1
  locator: { number: "annex-d/summary/r2/2.1", headingPath: ["Annex D", "Summary table", "Upper second-class honours (2.1)"] }
  span: { start: 107729, end: 107785 }
  source: "demonstrated good initiative and personal responsibility"
  stem: qaa/fheq-2024/annex-d/summary/lead/2.1
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "good initiative and responsibility"
  themes: [none]
  paraphrase: "Showed good initiative and personal responsibility."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r2/1st
  locator: { number: "annex-d/summary/r2/1st", headingPath: ["Annex D", "Summary table", "First-class honours (1st)"] }
  span: { start: 107787, end: 107863 }
  source: "consistently demonstrated exceptional initiative and personal responsibility"
  stem: qaa/fheq-2024/annex-d/summary/lead/1st
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "exceptional initiative and responsibility, consistently"
  themes: [none]
  paraphrase: "Showed exceptional initiative and personal responsibility, throughout."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r3/ns
  locator: { number: "annex-d/summary/r3/ns", headingPath: ["Annex D", "Summary table", "Not successful"] }
  span: { start: 107865, end: 107930 }
  source: "did not consistently demonstrate ability to reflect on their work"
  stem: qaa/fheq-2024/annex-d/summary/lead/ns
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrate, reflect]
  about: "reflection not shown consistently"
  themes: [none]
  paraphrase: "Did not consistently show they could reflect on their own work."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r3/3rd
  locator: { number: "annex-d/summary/r3/3rd", headingPath: ["Annex D", "Summary table", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 107932, end: 107982 }
  source: "demonstrated some ability to reflect on their work"
  stem: qaa/fheq-2024/annex-d/summary/lead/3rd
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, reflect]
  about: "some reflection"
  themes: [none]
  paraphrase: "Showed some ability to reflect on their own work."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r3/2.2
  locator: { number: "annex-d/summary/r3/2.2", headingPath: ["Annex D", "Summary table", "Lower second-class honours (2.2)"] }
  span: { start: 107984, end: 108032 }
  source: "demonstrated an ability to reflect on their work"
  stem: qaa/fheq-2024/annex-d/summary/lead/2.2
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, reflect]
  about: "reflection"
  themes: [none]
  paraphrase: "Showed they can reflect on their own work."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r3/2.1
  locator: { number: "annex-d/summary/r3/2.1", headingPath: ["Annex D", "Summary table", "Upper second-class honours (2.1)"] }
  span: { start: 108034, end: 108093 }
  source: "demonstrated an ability to reflect critically on their work"
  stem: qaa/fheq-2024/annex-d/summary/lead/2.1
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, reflect]
  about: "critical reflection"
  themes: [none]
  paraphrase: "Showed they can reflect critically on their own work."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r3/1st
  locator: { number: "annex-d/summary/r3/1st", headingPath: ["Annex D", "Summary table", "First-class honours (1st)"] }
  span: { start: 108095, end: 108182 }
  source: "consistently demonstrated ability to reflect critically and independently on their work"
  stem: qaa/fheq-2024/annex-d/summary/lead/1st
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, reflect]
  about: "critical, independent reflection, consistently"
  themes: [none]
  paraphrase: "Showed throughout that they can reflect on their work critically and independently."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r4/ns
  locator: { number: "annex-d/summary/r4/ns", headingPath: ["Annex D", "Summary table", "Not successful"] }
  span: { start: 108184, end: 108239 }
  source: "did not consistently demonstrate problem-solving skills"
  stem: qaa/fheq-2024/annex-d/summary/lead/ns
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrate]
  about: "problem-solving not shown consistently"
  themes: [none]
  paraphrase: "Did not consistently show problem-solving skill."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r4/3rd
  locator: { number: "annex-d/summary/r4/3rd", headingPath: ["Annex D", "Summary table", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 108241, end: 108276 }
  source: "demonstrated problem-solving skills"
  stem: qaa/fheq-2024/annex-d/summary/lead/3rd
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "problem-solving shown"
  themes: [none]
  paraphrase: "Showed problem-solving skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r4/2.2
  locator: { number: "annex-d/summary/r4/2.2", headingPath: ["Annex D", "Summary table", "Lower second-class honours (2.2)"] }
  span: { start: 108278, end: 108319 }
  source: "demonstrated strong problemsolving skills"
  stem: qaa/fheq-2024/annex-d/summary/lead/2.2
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "strong problem-solving"
  themes: [none]
  paraphrase: "Showed strong problem-solving skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r4/2.1
  locator: { number: "annex-d/summary/r4/2.1", headingPath: ["Annex D", "Summary table", "Upper second-class honours (2.1)"] }
  span: { start: 108321, end: 108364 }
  source: "demonstrated thorough problemsolving skills"
  stem: qaa/fheq-2024/annex-d/summary/lead/2.1
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "thorough problem-solving"
  themes: [none]
  paraphrase: "Showed thorough problem-solving skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/summary/r4/1st
  locator: { number: "annex-d/summary/r4/1st", headingPath: ["Annex D", "Summary table", "First-class honours (1st)"] }
  span: { start: 108366, end: 108426 }
  source: "consistently demonstrated exceptional problem-solving skills"
  stem: qaa/fheq-2024/annex-d/summary/lead/1st
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: summary
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "exceptional problem-solving, consistently"
  themes: [none]
  paraphrase: "Showed exceptional problem-solving skills throughout."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r1/ns
  locator: { number: "annex-d/knowledge/r1/ns", headingPath: ["Annex D", "Knowledge and understanding", "Not successful"] }
  span: { start: 111249, end: 111391 }
  source: "The student's knowledge and understanding of the subject is inadequate, without the required breadth or depth, with deficiencies in key areas."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: []
  about: "inadequate breadth and depth"
  themes: [none]
  paraphrase: "Subject knowledge and understanding fall short in breadth or depth, with gaps in key areas."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r1/3rd
  locator: { number: "annex-d/knowledge/r1/3rd", headingPath: ["Annex D", "Knowledge and understanding", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 111393, end: 111557 }
  source: "The student has demonstrated a depth of knowledge and understanding in key aspects of their field of study, sufficient to deal with terminology, facts and concepts."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, deal]
  about: "enough depth to handle terms, facts, concepts"
  themes: [none]
  paraphrase: "Has shown knowledge and understanding of key aspects deep enough to handle the field's terms, facts and concepts."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r1/2.2
  locator: { number: "annex-d/knowledge/r1/2.2", headingPath: ["Annex D", "Knowledge and understanding", "Lower second-class honours (2.2)"] }
  span: { start: 111559, end: 111739 }
  source: "The student has demonstrated a sound breadth and depth of subject knowledge and understanding, if sometimes balanced towards the descriptive rather than the critical or analytical."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "sound breadth and depth, sometimes descriptive"
  themes: [none]
  paraphrase: "Has shown sound breadth and depth of subject knowledge, though at times more descriptive than critical or analytical."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r1/2.1
  locator: { number: "annex-d/knowledge/r1/2.1", headingPath: ["Annex D", "Knowledge and understanding", "Upper second-class honours (2.1)"] }
  span: { start: 111741, end: 111868 }
  source: "The student has demonstrated sophisticated breadth and depth of knowledge and understanding, showing a clear, critical insight."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, showing]
  about: "sophisticated breadth and depth, critical insight"
  themes: [none]
  paraphrase: "Has shown sophisticated breadth and depth of knowledge with clear critical insight."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r1/1st
  locator: { number: "annex-d/knowledge/r1/1st", headingPath: ["Annex D", "Knowledge and understanding", "First-class honours (1st)"] }
  span: { start: 111870, end: 112040 }
  source: "The student has shown exceptional knowledge and understanding, significantly beyond the threshold expectation of a graduate at this level and beyond what has been taught."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [shown]
  about: "exceptional, beyond the threshold and the taught"
  themes: [none]
  paraphrase: "Has shown exceptional knowledge and understanding, well past the threshold for a graduate and past what was taught."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r2/ns
  locator: { number: "annex-d/knowledge/r2/ns", headingPath: ["Annex D", "Knowledge and understanding", "Not successful"] }
  span: { start: 112042, end: 112206 }
  source: "The student has demonstrated inadequate understanding of subject-specific theories, paradigms, concepts and principles, including their limitations and ambiguities."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "inadequate grasp of theory and its limits"
  themes: [none]
  paraphrase: "Has shown inadequate understanding of the subject's theories, paradigms, concepts and principles, and of their limits and ambiguities."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r2/3rd
  locator: { number: "annex-d/knowledge/r2/3rd", headingPath: ["Annex D", "Knowledge and understanding", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 112208, end: 112319 }
  source: "The student has demonstrated an understanding of subject-specific theories, paradigms, concepts and principles."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "understanding of theories and concepts"
  themes: [none]
  paraphrase: "Has shown understanding of the subject's theories, paradigms, concepts and principles."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r2/2.2
  locator: { number: "annex-d/knowledge/r2/2.2", headingPath: ["Annex D", "Knowledge and understanding", "Lower second-class honours (2.2)"] }
  span: { start: 112321, end: 112478 }
  source: "The student has consistently demonstrated an understanding of subjectspecific theories, paradigms, concepts and principles as well as more specialised areas."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "consistent understanding, some specialised areas"
  themes: [none]
  paraphrase: "Has consistently understood the subject's theories and principles and some more specialised areas."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r2/2.1
  locator: { number: "annex-d/knowledge/r2/2.1", headingPath: ["Annex D", "Knowledge and understanding", "Upper second-class honours (2.1)"] }
  span: { start: 112480, end: 112652 }
  source: "The student has demonstrated a thorough understanding of subject-specific theories, paradigms, concepts and principles, and a sound understanding of more specialised areas."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "thorough theory, sound specialised knowledge"
  themes: [none]
  paraphrase: "Has shown thorough understanding of the subject's theories and principles and sound understanding of specialised areas."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r2/1st
  locator: { number: "annex-d/knowledge/r2/1st", headingPath: ["Annex D", "Knowledge and understanding", "First-class honours (1st)"] }
  span: { start: 112654, end: 112850 }
  source: "The student has demonstrated an exceptional understanding of subject-specific theories, paradigms, concepts and principles, and in-depth knowledge, if not mastery, of a range of specialised areas."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "exceptional theory, in-depth specialised knowledge"
  themes: [none]
  paraphrase: "Has shown exceptional understanding of the subject's theories and principles, with in-depth knowledge, near mastery, of several specialised areas."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r3/ns
  locator: { number: "annex-d/knowledge/r3/ns", headingPath: ["Annex D", "Knowledge and understanding", "Not successful"] }
  span: { start: 112852, end: 112971 }
  source: "The student has not produced sufficient evidence of background investigation, analysis, research, enquiry and/or study."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [produced]
  about: "insufficient background investigation"
  themes: [none]
  paraphrase: "Has not produced enough evidence of background investigation, research or study."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r3/3rd
  locator: { number: "annex-d/knowledge/r3/3rd", headingPath: ["Annex D", "Knowledge and understanding", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 112973, end: 113148 }
  source: "The student has conducted general background investigation, analysis, research, enquiry and/or study using established techniques, with the ability to extract relevant points."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [conducted, using, extract]
  about: "general investigation, picking out relevant points"
  themes: [none]
  paraphrase: "Has done general background research with established techniques and can pick out the relevant points."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r3/2.2
  locator: { number: "annex-d/knowledge/r3/2.2", headingPath: ["Annex D", "Knowledge and understanding", "Lower second-class honours (2.2)"] }
  span: { start: 113150, end: 113329 }
  source: "The student has conducted background investigation, analysis, research, enquiry and/or study using established techniques accurately, and can critically appraise academic sources."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [conducted, using, appraise]
  about: "accurate investigation, appraising sources"
  themes: [none]
  paraphrase: "Has done background research accurately with established techniques and can appraise academic sources critically."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r3/2.1
  locator: { number: "annex-d/knowledge/r3/2.1", headingPath: ["Annex D", "Knowledge and understanding", "Upper second-class honours (2.1)"] }
  span: { start: 113331, end: 113560 }
  source: "The student has conducted thorough background investigation, analysis, research, enquiry and/or study using established techniques accurately, and possesses a well-developed ability to critically appraise a wide range of sources."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [conducted, using, appraise]
  about: "thorough investigation, well-developed appraisal"
  themes: [none]
  paraphrase: "Has done thorough, accurate background research and has a well-developed ability to appraise many kinds of source critically."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/knowledge/r3/1st
  locator: { number: "annex-d/knowledge/r3/1st", headingPath: ["Annex D", "Knowledge and understanding", "First-class honours (1st)"] }
  span: { start: 113562, end: 113787 }
  source: "The student has conducted independent, extensive and appropriate investigation, analysis, research, enquiry and/or study well beyond the usual range, together with critical evaluation, to advance work and/or direct arguments."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: knowledge
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [conducted, advance, direct]
  about: "independent investigation beyond the usual range"
  themes: [none]
  paraphrase: "Has carried out independent, extensive and fitting research well past the usual range, evaluated critically, to move work forward or steer arguments."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r1/ns
  locator: { number: "annex-d/cognitive/r1/ns", headingPath: ["Annex D", "Cognitive skills", "Not successful"] }
  span: { start: 114115, end: 114264 }
  source: "The student has displayed an overreliance on set sources. They have not demonstrated an adequate ability to select and evaluate reading and research."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [displayed, demonstrated, select, evaluate]
  about: "over-reliance on set sources"
  themes: [none]
  paraphrase: "Leans too heavily on set sources and cannot yet choose and weigh reading and research adequately."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r1/3rd
  locator: { number: "annex-d/cognitive/r1/3rd", headingPath: ["Annex D", "Cognitive skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 114266, end: 114380 }
  source: "The student has demonstrated the ability to select, evaluate and comment on reading, research and primary sources."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, select, evaluate, comment]
  about: "selecting and commenting on sources"
  themes: [none]
  paraphrase: "Has shown they can choose, weigh and comment on reading, research and primary sources."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r1/2.2
  locator: { number: "annex-d/cognitive/r1/2.2", headingPath: ["Annex D", "Cognitive skills", "Lower second-class honours (2.2)"] }
  span: { start: 114382, end: 114505 }
  source: "The student has selected, evaluated and commented on reading, research and primary sources, sometimes beyond the set range."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [selected, evaluated, commented]
  about: "sources, sometimes beyond the set range"
  themes: [none]
  paraphrase: "Has chosen, weighed and commented on reading, research and primary sources, at times going past the set range."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r1/2.1
  locator: { number: "annex-d/cognitive/r1/2.1", headingPath: ["Annex D", "Cognitive skills", "Upper second-class honours (2.1)"] }
  span: { start: 114507, end: 114650 }
  source: "The student has thoroughly selected, critically evaluated and commented on reading, research and primary sources, usually beyond the set range."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [selected, evaluated, commented]
  about: "sources critically, usually beyond the set range"
  themes: [none]
  paraphrase: "Has chosen sources thoroughly, weighed them critically and commented on them, usually going past the set range."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r1/1st
  locator: { number: "annex-d/cognitive/r1/1st", headingPath: ["Annex D", "Cognitive skills", "First-class honours (1st)"] }
  span: { start: 114652, end: 114852 }
  source: "The student has demonstrated an exceptional ability to select, consider, evaluate, comment on and synthesise a broad range of research, primary sources, views and information and integrate references."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, select, consider, evaluate, comment, synthesise, integrate]
  about: "synthesising a broad range of sources"
  themes: [none]
  paraphrase: "Has shown exceptional skill in choosing, weighing and synthesising a broad range of research, sources and views, and integrating references."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r2/ns
  locator: { number: "annex-d/cognitive/r2/ns", headingPath: ["Annex D", "Cognitive skills", "Not successful"] }
  span: { start: 114854, end: 115030 }
  source: "The student's arguments and explanations are weak and/or poorly constructed, and they are not able to critically evaluate the arguments of others or consider alternative views."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [evaluate, consider]
  about: "weak argument, no critical view of others"
  themes: [none]
  paraphrase: "Arguments and explanations are weak or poorly built; cannot yet evaluate others' arguments critically or weigh alternatives."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r2/3rd
  locator: { number: "annex-d/cognitive/r2/3rd", headingPath: ["Annex D", "Cognitive skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 115032, end: 115195 }
  source: "The student has shown the ability to devise and sustain an argument, with some consideration of alternative views, and can explain often complex matters and ideas."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [shown, devise, sustain, explain]
  about: "sustained argument, some alternatives"
  themes: [none]
  paraphrase: "Can build and keep up an argument with some regard to other views and can explain often complex matters."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r2/2.2
  locator: { number: "annex-d/cognitive/r2/2.2", headingPath: ["Annex D", "Cognitive skills", "Lower second-class honours (2.2)"] }
  span: { start: 115197, end: 115420 }
  source: "The student has argued logically, with supporting evidence, and has demonstrated the ability to consider and evaluate a range of views and information. They have clearly and consistently explained complex matters and ideas."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [argued, demonstrated, consider, evaluate, explained]
  about: "logical, evidenced argument; consistent explanation"
  themes: [none]
  paraphrase: "Argues logically with evidence, considers and weighs a range of views, and explains complex matters clearly and consistently."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r2/2.1
  locator: { number: "annex-d/cognitive/r2/2.1", headingPath: ["Annex D", "Cognitive skills", "Upper second-class honours (2.1)"] }
  span: { start: 115422, end: 115716 }
  source: "The student has demonstrated the ability to make coherent, substantiated arguments, as well as the ability to consider, critically evaluate and synthesise a range of views and information. They have demonstrated a thorough, perceptive and thoughtful interpretation of complex matters and ideas."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, make, consider, evaluate, synthesise]
  about: "coherent argument; perceptive interpretation"
  themes: [none]
  paraphrase: "Makes coherent, well-supported arguments, weighs and synthesises views critically, and interprets complex matters thoroughly and perceptively."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r2/1st
  locator: { number: "annex-d/cognitive/r2/1st", headingPath: ["Annex D", "Cognitive skills", "First-class honours (1st)"] }
  span: { start: 115718, end: 116055 }
  source: "The student has made consistent, logical, coherentlydeveloped, and substantiated arguments, and demonstrated the ability to systematically consider, critically evaluate and synthesise a wide range of views and information. They have demonstrated sophisticated perception, critical insight and interpretation of complex matters and ideas."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [made, demonstrated, consider, evaluate, synthesise]
  about: "systematic synthesis; sophisticated insight"
  themes: [none]
  paraphrase: "Makes consistent, logical, well-built and supported arguments, synthesises a wide range of views systematically and critically, and interprets with sophistication and insight."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r3/ns
  locator: { number: "annex-d/cognitive/r3/ns", headingPath: ["Annex D", "Cognitive skills", "Not successful"] }
  span: { start: 116057, end: 116137 }
  source: "The student has shown a limited ability to solve problems and/or make decisions."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [shown, solve, make]
  about: "limited problem-solving and decisions"
  themes: [none]
  paraphrase: "Shows only limited ability to solve problems or make decisions."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r3/3rd
  locator: { number: "annex-d/cognitive/r3/3rd", headingPath: ["Annex D", "Cognitive skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 116139, end: 116313 }
  source: "The student has demonstrated an ability to solve problems, applying a range of methods to do so, and the ability to make decisions in complex and unpredictable circumstances."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, solve, applying, make]
  about: "solving problems; deciding in complex situations"
  themes: [none]
  paraphrase: "Can solve problems with a range of methods and make decisions in complex, unpredictable circumstances."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r3/2.2
  locator: { number: "annex-d/cognitive/r3/2.2", headingPath: ["Annex D", "Cognitive skills", "Lower second-class honours (2.2)"] }
  span: { start: 116315, end: 116490 }
  source: "The student has consistently solved complex problems, selecting and applying a range of appropriate methods, and can make decisions in complex and unpredictable circumstances."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [solved, selecting, applying, make]
  about: "consistently solving complex problems"
  themes: [none]
  paraphrase: "Consistently solves complex problems, choosing and applying fitting methods, and makes decisions in complex, unpredictable circumstances."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r3/2.1
  locator: { number: "annex-d/cognitive/r3/2.1", headingPath: ["Annex D", "Cognitive skills", "Upper second-class honours (2.1)"] }
  span: { start: 116492, end: 116709 }
  source: "The student has demonstrated thorough problem-solving skills, selecting and justifying their use of a wide range of methods, and can make decisions in complex and unpredictable circumstances with a degree of autonomy."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, selecting, justifying, make]
  about: "justifying methods; some autonomy in decisions"
  themes: [none]
  paraphrase: "Solves problems thoroughly, choosing and justifying a wide range of methods, and decides in complex, unpredictable circumstances with some autonomy."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r3/1st
  locator: { number: "annex-d/cognitive/r3/1st", headingPath: ["Annex D", "Cognitive skills", "First-class honours (1st)"] }
  span: { start: 116711, end: 116938 }
  source: "The student has demonstrated a wide range of extremely well-developed problem-solving skills, as well as a strong aptitude for decision-making with a high degree of autonomy, in the most complex and unpredictable circumstances."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "highly developed problem-solving; autonomous decisions"
  themes: [none]
  paraphrase: "Has a wide range of highly developed problem-solving skills and a strong aptitude for highly autonomous decisions in the most complex, unpredictable circumstances."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r4/ns
  locator: { number: "annex-d/cognitive/r4/ns", headingPath: ["Annex D", "Cognitive skills", "Not successful"] }
  span: { start: 116940, end: 116991 }
  source: "The student has shown little or no real creativity."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [shown]
  about: "little or no creativity"
  themes: [none]
  paraphrase: "Shows little or no real creativity."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r4/3rd
  locator: { number: "annex-d/cognitive/r4/3rd", headingPath: ["Annex D", "Cognitive skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 116993, end: 117037 }
  source: "The student has some produced creative work."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [produced]
  about: "some creative work"
  themes: [none]
  paraphrase: "Has produced some creative work."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r4/2.2
  locator: { number: "annex-d/cognitive/r4/2.2", headingPath: ["Annex D", "Cognitive skills", "Lower second-class honours (2.2)"] }
  span: { start: 117039, end: 117092 }
  source: "The student has consistently demonstrated creativity."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "consistent creativity"
  themes: [none]
  paraphrase: "Has shown creativity consistently."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r4/2.1
  locator: { number: "annex-d/cognitive/r4/2.1", headingPath: ["Annex D", "Cognitive skills", "Upper second-class honours (2.1)"] }
  span: { start: 117094, end: 117181 }
  source: "The student has shown a high level of creativity and originality throughout their work."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [shown]
  about: "high creativity and originality"
  themes: [none]
  paraphrase: "Has been highly creative and original throughout."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/cognitive/r4/1st
  locator: { number: "annex-d/cognitive/r4/1st", headingPath: ["Annex D", "Cognitive skills", "First-class honours (1st)"] }
  span: { start: 117183, end: 117255 }
  source: "The student has demonstrated exceptional creative flair and originality."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: cognitive
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "exceptional creative flair"
  themes: [none]
  paraphrase: "Has shown exceptional creative flair and originality."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r1/ns
  locator: { number: "annex-d/practical/r1/ns", headingPath: ["Annex D", "Practical skills", "Not successful"] }
  span: { start: 117509, end: 117619 }
  source: "The student has not demonstrated sufficient evidence of discipline-specific skills development or application."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "insufficient discipline skills"
  themes: [none]
  paraphrase: "Has not shown enough evidence of developing or applying the discipline's skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r1/3rd
  locator: { number: "annex-d/practical/r1/3rd", headingPath: ["Annex D", "Practical skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 117621, end: 117724 }
  source: "The student has demonstrated evidence of developing and applying discipline-specific specialist skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, developing, applying]
  about: "developing and applying specialist skills"
  themes: [none]
  paraphrase: "Has shown evidence of developing and applying the discipline's specialist skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r1/2.2
  locator: { number: "annex-d/practical/r1/2.2", headingPath: ["Annex D", "Practical skills", "Lower second-class honours (2.2)"] }
  span: { start: 117726, end: 117849 }
  source: "The student has consistently demonstrated the development and informed application of disciplinespecific specialist skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "consistent, informed use of specialist skills"
  themes: [none]
  paraphrase: "Has consistently developed and applied the discipline's specialist skills in an informed way."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r1/2.1
  locator: { number: "annex-d/practical/r1/2.1", headingPath: ["Annex D", "Practical skills", "Upper second-class honours (2.1)"] }
  span: { start: 117851, end: 117969 }
  source: "The student has demonstrated capable and effective performance/demonstration of discipline-specific specialist skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "capable, effective specialist skills"
  themes: [none]
  paraphrase: "Has performed the discipline's specialist skills capably and effectively."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r1/1st
  locator: { number: "annex-d/practical/r1/1st", headingPath: ["Annex D", "Practical skills", "First-class honours (1st)"] }
  span: { start: 117971, end: 118083 }
  source: "The student has demonstrated an accomplished and innovative application of disciplinespecific specialist skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "accomplished, innovative specialist skills"
  themes: [none]
  paraphrase: "Has applied the discipline's specialist skills in an accomplished and innovative way."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r2/ns
  locator: { number: "annex-d/practical/r2/ns", headingPath: ["Annex D", "Practical skills", "Not successful"] }
  span: { start: 118085, end: 118252 }
  source: "The student has attempted practical tasks/processes but followed a limited, procedural or mechanistic formula, and they contain errors, with little or no independence."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [attempted, followed]
  about: "mechanical, error-prone, dependent"
  themes: [none]
  paraphrase: "Attempted practical tasks but followed a narrow, mechanical procedure, with errors and little or no independence."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r2/3rd
  locator: { number: "annex-d/practical/r2/3rd", headingPath: ["Annex D", "Practical skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 118254, end: 118358 }
  source: "The student has completed practical tasks and/or processes accurately and with a degree of independence."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [completed]
  about: "accurate tasks, some independence"
  themes: [none]
  paraphrase: "Has completed practical tasks accurately and with some independence."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r2/2.2
  locator: { number: "annex-d/practical/r2/2.2", headingPath: ["Annex D", "Practical skills", "Lower second-class honours (2.2)"] }
  span: { start: 118360, end: 118498 }
  source: "The student has consistently completed practical tasks/processes mainly independently in an accurate, well-coordinated and proficient way."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [completed]
  about: "mainly independent, proficient tasks"
  themes: [none]
  paraphrase: "Has consistently completed practical tasks mainly independently, accurately, with coordination and proficiency."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r2/2.1
  locator: { number: "annex-d/practical/r2/2.1", headingPath: ["Annex D", "Practical skills", "Upper second-class honours (2.1)"] }
  span: { start: 118500, end: 118604 }
  source: "The student has performed practical tasks and/or processes autonomously, with accuracy and coordination."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [performed]
  about: "autonomous, accurate tasks"
  themes: [none]
  paraphrase: "Has carried out practical tasks autonomously, accurately and with coordination."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r2/1st
  locator: { number: "annex-d/practical/r2/1st", headingPath: ["Annex D", "Practical skills", "First-class honours (1st)"] }
  span: { start: 118606, end: 118739 }
  source: "The student has autonomously completed practical tasks and/or processes with a high degree of accuracy, coordination and proficiency."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [completed]
  about: "autonomous, highly accurate tasks"
  themes: [none]
  paraphrase: "Has completed practical tasks autonomously, highly accurately, with coordination and proficiency."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r3/ns
  locator: { number: "annex-d/practical/r3/ns", headingPath: ["Annex D", "Practical skills", "Not successful"] }
  span: { start: 118741, end: 118846 }
  source: "The student has demonstrated a lack of technical, creative and/or artistic skills in most, or key, areas."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "lacking technical or creative skill"
  themes: [none]
  paraphrase: "Shows a lack of technical, creative or artistic skill in most or key areas."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r3/3rd
  locator: { number: "annex-d/practical/r3/3rd", headingPath: ["Annex D", "Practical skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 118848, end: 118920 }
  source: "The student has demonstrated technical, creative and/or artistic skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "technical or creative skill shown"
  themes: [none]
  paraphrase: "Has shown technical, creative or artistic skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r3/2.2
  locator: { number: "annex-d/practical/r3/2.2", headingPath: ["Annex D", "Practical skills", "Lower second-class honours (2.2)"] }
  span: { start: 118922, end: 119022 }
  source: "The student has consistently demonstrated well-developed technical, creative and/or artistic skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "well-developed technical skill, consistently"
  themes: [none]
  paraphrase: "Has consistently shown well-developed technical, creative or artistic skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r3/2.1
  locator: { number: "annex-d/practical/r3/2.1", headingPath: ["Annex D", "Practical skills", "Upper second-class honours (2.1)"] }
  span: { start: 119024, end: 119131 }
  source: "The student has a thorough command of highly-developed relevant technical, creative and/or artistic skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: []
  about: "thorough command of advanced skills"
  themes: [none]
  paraphrase: "Has a thorough command of highly developed technical, creative or artistic skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r3/1st
  locator: { number: "annex-d/practical/r3/1st", headingPath: ["Annex D", "Practical skills", "First-class honours (1st)"] }
  span: { start: 119133, end: 119220 }
  source: "The student has a full range of exceptional technical, creative and/or artistic skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: []
  about: "full range of exceptional skills"
  themes: [none]
  paraphrase: "Has a full range of exceptional technical, creative or artistic skills."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r4/ns
  locator: { number: "annex-d/practical/r4/ns", headingPath: ["Annex D", "Practical skills", "Not successful"] }
  span: { start: 119222, end: 119377 }
  source: "The student has not presented their research findings clearly or effectively, and their gathering, processing and interpretation of data is unsatisfactory."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [presented]
  about: "unclear findings, unsatisfactory data handling"
  themes: [none]
  paraphrase: "Has not presented findings clearly or effectively, and gathered, processed and interpreted data unsatisfactorily."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r4/3rd
  locator: { number: "annex-d/practical/r4/3rd", headingPath: ["Annex D", "Practical skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 119379, end: 119511 }
  source: "The student has presented their research findings, in several formats, and has gathered, processed and interpreted data effectively."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [presented, gathered, processed, interpreted]
  about: "findings in several formats; effective data"
  themes: [none]
  paraphrase: "Has presented findings in several formats and gathered, processed and interpreted data effectively."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r4/2.2
  locator: { number: "annex-d/practical/r4/2.2", headingPath: ["Annex D", "Practical skills", "Lower second-class honours (2.2)"] }
  span: { start: 119513, end: 119700 }
  source: "The student has consistently presented their research findings effectively and appropriately in many formats, and has gathered, processed and interpreted data efficiently and effectively."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [presented, gathered, processed, interpreted]
  about: "consistent presentation; efficient data"
  themes: [none]
  paraphrase: "Has consistently presented findings effectively in many formats and handled data efficiently and effectively."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r4/2.1
  locator: { number: "annex-d/practical/r4/2.1", headingPath: ["Annex D", "Practical skills", "Upper second-class honours (2.1)"] }
  span: { start: 119702, end: 119915 }
  source: "The student has presented thorough research findings perceptively and appropriately in a wide range of formats, and has gathered, processed and interpreted a wide range of complex data efficiently and effectively."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [presented, gathered, processed, interpreted]
  about: "perceptive presentation; complex data"
  themes: [none]
  paraphrase: "Has presented thorough findings perceptively in a wide range of formats and handled a wide range of complex data efficiently."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/practical/r4/1st
  locator: { number: "annex-d/practical/r4/1st", headingPath: ["Annex D", "Practical skills", "First-class honours (1st)"] }
  span: { start: 119917, end: 120135 }
  source: "The student has presented research findings perceptively, convincingly and appropriately in a wide range of formats, and has gathered, processed and interpreted a wide range of complex data efficiently and effectively."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: practical
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [presented, gathered, processed, interpreted]
  about: "convincing presentation; complex data"
  themes: [none]
  paraphrase: "Has presented findings perceptively and convincingly in a wide range of formats and handled a wide range of complex data efficiently."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r1/ns
  locator: { number: "annex-d/transferable/r1/ns", headingPath: ["Annex D", "Transferable skills", "Not successful"] }
  span: { start: 120516, end: 120814 }
  source: "The student is not able to sufficiently express ideas and convey clear meaning verbally, electronically and/or in writing, uses inaccurate terminology, with many errors in spelling, vocabulary and syntax. They have been unable to demonstrate consistently basic numeracy and digital literacy skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [express, convey, uses, demonstrate]
  about: "unclear expression; weak numeracy and digital skill"
  themes: [none]
  paraphrase: "Cannot yet express ideas clearly in speech, digitally or in writing; terminology inaccurate, many errors; basic numeracy and digital literacy not shown consistently."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r1/3rd
  locator: { number: "annex-d/transferable/r1/3rd", headingPath: ["Annex D", "Transferable skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 120816, end: 121026 }
  source: "The student can communicate information, ideas, problems and solutions verbally, electronically and in writing, with clear expression and style. They have also demonstrated numeracy and digital literacy skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [communicate, demonstrated]
  about: "clear communication; numeracy and digital literacy"
  themes: [none]
  paraphrase: "Communicates information, ideas, problems and solutions in speech, digitally and in writing with clear expression; has shown numeracy and digital literacy."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r1/2.2
  locator: { number: "annex-d/transferable/r1/2.2", headingPath: ["Annex D", "Transferable skills", "Lower second-class honours (2.2)"] }
  span: { start: 121028, end: 121324 }
  source: "The student can consistently and confidently communicate information, ideas, problems and solutions verbally, electronically and in writing. They show a clear, coherent, expressive style, with a range of vocabulary. They have consistently demonstrated strong numeracy and digital literacy skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [communicate, show, demonstrated]
  about: "confident communication; strong numeracy"
  themes: [none]
  paraphrase: "Communicates consistently and confidently in all modes, in a clear, coherent and expressive style, with strong numeracy and digital literacy."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r1/2.1
  locator: { number: "annex-d/transferable/r1/2.1", headingPath: ["Annex D", "Transferable skills", "Upper second-class honours (2.1)"] }
  span: { start: 121326, end: 121614 }
  source: "The student can communicate information, ideas, problems and solutions with a high-degree of proficiency verbally, electronically and in writing. They have a clear, fluent and expressive style with appropriate vocabulary. They have a high standard of numeracy and digital literacy skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [communicate]
  about: "proficient communication; high numeracy"
  themes: [none]
  paraphrase: "Communicates with a high degree of proficiency in all modes, in a clear, fluent, expressive style; numeracy and digital literacy of a high standard."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r1/1st
  locator: { number: "annex-d/transferable/r1/1st", headingPath: ["Annex D", "Transferable skills", "First-class honours (1st)"] }
  span: { start: 121616, end: 121873 }
  source: "The student can communicate information, ideas, problems and solutions to an accomplished level verbally, electronically and in writing. They have shown an accurate, fluent, sophisticated style. They possess exceptional numeracy and digital literacy skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [communicate, shown, possess]
  about: "accomplished communication; exceptional numeracy"
  themes: [none]
  paraphrase: "Communicates to an accomplished level in all modes, in an accurate, fluent and sophisticated style; numeracy and digital literacy exceptional."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r2/ns
  locator: { number: "annex-d/transferable/r2/ns", headingPath: ["Annex D", "Transferable skills", "Not successful"] }
  span: { start: 121875, end: 121962 }
  source: "The student has made infrequent contributions to group discussions and/or project work."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [made]
  about: "infrequent contributions to group work"
  themes: [none]
  paraphrase: "Contributed to group discussion or project work only infrequently."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r2/3rd
  locator: { number: "annex-d/transferable/r2/3rd", headingPath: ["Annex D", "Transferable skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 121964, end: 122078 }
  source: "The student has demonstrated a capability of making useful contributions to group discussions and/or project work."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, making]
  about: "useful contributions to group work"
  themes: [none]
  paraphrase: "Can make useful contributions to group discussion and project work."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r2/2.2
  locator: { number: "annex-d/transferable/r2/2.2", headingPath: ["Annex D", "Transferable skills", "Lower second-class honours (2.2)"] }
  span: { start: 122080, end: 122226 }
  source: "The student has consistently demonstrated the capability to make coherent and constructive contributions to group discussions and/or project work."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, make]
  about: "coherent, constructive contributions"
  themes: [none]
  paraphrase: "Consistently makes coherent and constructive contributions to group discussion and project work."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r2/2.1
  locator: { number: "annex-d/transferable/r2/2.1", headingPath: ["Annex D", "Transferable skills", "Upper second-class honours (2.1)"] }
  span: { start: 122228, end: 122404 }
  source: "The student has demonstrated the capability to make strong, valuable contributions to group discussions and/or project work, with an understanding of team and leadership roles."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, make]
  about: "strong contributions; team and leadership roles"
  themes: [none]
  paraphrase: "Makes strong, valuable contributions to group work and understands team and leadership roles."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r2/1st
  locator: { number: "annex-d/transferable/r2/1st", headingPath: ["Annex D", "Transferable skills", "First-class honours (1st)"] }
  span: { start: 122406, end: 122596 }
  source: "The student has demonstrated the capability to make clear, authoritative and valuable contributions to group discussions and/or project work, with exceptional teamwork and leadership skills."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, make]
  about: "authoritative contributions; exceptional teamwork and leadership"
  themes: [none]
  paraphrase: "Makes clear, authoritative and valuable contributions to group work, with exceptional teamwork and leadership."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r3/ns
  locator: { number: "annex-d/transferable/r3/ns", headingPath: ["Annex D", "Transferable skills", "Not successful"] }
  span: { start: 122598, end: 122705 }
  source: "The student has demonstrated little or no ability to manage their learning and/or work without supervision."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, manage]
  about: "little self-management"
  themes: [none]
  paraphrase: "Shows little or no ability to manage learning or work without supervision."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r3/3rd
  locator: { number: "annex-d/transferable/r3/3rd", headingPath: ["Annex D", "Transferable skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 122707, end: 122805 }
  source: "The student has shown an ability to manage their learning and work with minimal or no supervision."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [shown, manage]
  about: "managing learning with minimal supervision"
  themes: [none]
  paraphrase: "Can manage their own learning and work with little or no supervision."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r3/2.2
  locator: { number: "annex-d/transferable/r3/2.2", headingPath: ["Annex D", "Transferable skills", "Lower second-class honours (2.2)"] }
  span: { start: 122807, end: 122923 }
  source: "The student has consistently shown an ability to systematically manage their learning, and work without supervision."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [shown, manage]
  about: "systematic self-management, consistently"
  themes: [none]
  paraphrase: "Consistently manages their learning systematically and works without supervision."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r3/2.1
  locator: { number: "annex-d/transferable/r3/2.1", headingPath: ["Annex D", "Transferable skills", "Upper second-class honours (2.1)"] }
  span: { start: 122925, end: 123034 }
  source: "The student has shown a strong ability to systematically manage their learning, and work without supervision."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [shown, manage]
  about: "strong systematic self-management"
  themes: [none]
  paraphrase: "Shows a strong ability to manage their learning systematically and work without supervision."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r3/1st
  locator: { number: "annex-d/transferable/r3/1st", headingPath: ["Annex D", "Transferable skills", "First-class honours (1st)"] }
  span: { start: 123036, end: 123160 }
  source: "The student has shown an exceptional ability to manage their learning on their own initiative, and work without supervision."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [shown, manage]
  about: "self-directed learning on own initiative"
  themes: [none]
  paraphrase: "Manages learning exceptionally on their own initiative and works unsupervised."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r4/ns
  locator: { number: "annex-d/transferable/r4/ns", headingPath: ["Annex D", "Transferable skills", "Not successful"] }
  span: { start: 123162, end: 123242 }
  source: "The student has not demonstrated adequate initiative or personal responsibility."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "inadequate initiative or responsibility"
  themes: [none]
  paraphrase: "Has not shown adequate initiative or personal responsibility."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r4/3rd
  locator: { number: "annex-d/transferable/r4/3rd", headingPath: ["Annex D", "Transferable skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 123244, end: 123315 }
  source: "The student has demonstrated initiative and/or personal responsibility."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "initiative or responsibility"
  themes: [none]
  paraphrase: "Has shown initiative or personal responsibility."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r4/2.2
  locator: { number: "annex-d/transferable/r4/2.2", headingPath: ["Annex D", "Transferable skills", "Lower second-class honours (2.2)"] }
  span: { start: 123317, end: 123401 }
  source: "The student has consistently demonstrated initiative and/or personal responsibility."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "consistent initiative or responsibility"
  themes: [none]
  paraphrase: "Has consistently shown initiative or personal responsibility."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r4/2.1
  locator: { number: "annex-d/transferable/r4/2.1", headingPath: ["Annex D", "Transferable skills", "Upper second-class honours (2.1)"] }
  span: { start: 123403, end: 123502 }
  source: "The student has consistently demonstrated well-developed initiative and/or personal responsibility."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "well-developed initiative, consistently"
  themes: [none]
  paraphrase: "Has consistently shown well-developed initiative or personal responsibility."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r4/1st
  locator: { number: "annex-d/transferable/r4/1st", headingPath: ["Annex D", "Transferable skills", "First-class honours (1st)"] }
  span: { start: 123504, end: 123587 }
  source: "The student has demonstrated exceptional initiative and/or personal responsibility."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated]
  about: "exceptional initiative or responsibility"
  themes: [none]
  paraphrase: "Has shown exceptional initiative or personal responsibility."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r5/ns
  locator: { number: "annex-d/transferable/r5/ns", headingPath: ["Annex D", "Transferable skills", "Not successful"] }
  span: { start: 123589, end: 123657 }
  source: "The student has shown little or no ability to reflect on their work."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [shown, reflect]
  about: "little or no reflection"
  themes: [none]
  paraphrase: "Shows little or no capacity for reflecting on their work."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r5/3rd
  locator: { number: "annex-d/transferable/r5/3rd", headingPath: ["Annex D", "Transferable skills", "Third-class honours (3rd, pass or threshold)"] }
  span: { start: 123659, end: 123725 }
  source: "The student has demonstrated the ability to reflect on their work."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "3rd"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, reflect]
  about: "reflection shown"
  themes: [none]
  paraphrase: "Has shown they can reflect on their work."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r5/2.2
  locator: { number: "annex-d/transferable/r5/2.2", headingPath: ["Annex D", "Transferable skills", "Lower second-class honours (2.2)"] }
  span: { start: 123727, end: 123819 }
  source: "The student has consistently demonstrated a well-developed ability to reflect on their work."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "2.2"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, reflect]
  about: "well-developed reflection, consistently"
  themes: [none]
  paraphrase: "Has consistently reflected on their work in a well-developed way."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r5/2.1
  locator: { number: "annex-d/transferable/r5/2.1", headingPath: ["Annex D", "Transferable skills", "Upper second-class honours (2.1)"] }
  span: { start: 123821, end: 123898 }
  source: "The student has demonstrated the ability to reflect critically on their work."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "2.1"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, reflect]
  about: "critical reflection"
  themes: [none]
  paraphrase: "Has shown they can reflect critically on their work."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/transferable/r5/1st
  locator: { number: "annex-d/transferable/r5/1st", headingPath: ["Annex D", "Transferable skills", "First-class honours (1st)"] }
  span: { start: 123900, end: 124006 }
  source: "The student has demonstrated an exceptional ability to reflect critically and independently on their work."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: transferable
  band: "1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, reflect]
  about: "exceptional critical, independent reflection"
  themes: [none]
  paraphrase: "Has shown an exceptional ability to reflect on their work critically and independently."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/professional/r1/ns
  locator: { number: "annex-d/professional/r1/ns", headingPath: ["Annex D", "Professional competences", "Not successful"] }
  span: { start: 124464, end: 124630 }
  source: "The student has not demonstrated achievement of professional competence when assessed against the requirements of a professional, statutory or regulatory body (PSRB)."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: professional
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, assessed]
  about: "professional competence not met"
  themes: [none]
  paraphrase: "Has not shown professional competence when assessed against a PSRB's requirements."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/professional/r1/3rd-1st
  locator: { number: "annex-d/professional/r1/3rd-1st", headingPath: ["Annex D", "Professional competences", "3rd to 1st (one cell across all four classifications)"] }
  span: { start: 124632, end: 124749 }
  source: "The student has demonstrated achievement of professional competence when assessed against the requirements of a PSRB."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: professional
  band: "3rd-1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [demonstrated, assessed]
  about: "professional competence met"
  themes: [none]
  paraphrase: "Has shown professional competence when assessed against a PSRB's requirements; the same for every classification."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/fheq-2024/annex-d/professional/r2/ns
  locator: { number: "annex-d/professional/r2/ns", headingPath: ["Annex D", "Professional competences", "Not successful"] }
  span: { start: 124751, end: 124862 }
  source: "The student has failed to adhere to the appropriate rules and/or conventions set by regulators or the industry."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: professional
  band: "ns"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [failed, adhere]
  about: "rules and conventions not kept"
  themes: [none]
  paraphrase: "Has not kept to the rules or conventions set by regulators or the industry."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/fheq-2024/annex-d/professional/r2/3rd-1st
  locator: { number: "annex-d/professional/r2/3rd-1st", headingPath: ["Annex D", "Professional competences", "3rd to 1st (one cell across all four classifications)"] }
  span: { start: 124864, end: 124966 }
  source: "The student has adhered to the appropriate rules and/or conventions set by regulators or the industry."
  stem: none
  statementType: classification-descriptor
  force: describes
  level: [fheq:6, fqheis:10]
  dimension: professional
  band: "3rd-1st"
  gradeOf: "bachelor's degree with honours"
  addressee: student
  verbs: [adhered]
  about: "rules and conventions kept"
  themes: [none]
  paraphrase: "Has kept to the rules and conventions set by regulators or the industry; the same for every classification."   # for grid cells the paraphrase is the practitioner version
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. The student versions name the qualification, never the framework or the issuer; force kept: "you will have shown" for the threshold, "you will usually be able to" or "you will have" for the typical holder. -->
```yaml
- statement: qaa/fheq-2024/4.10.b1
  forPractitioner: { text: "CertHE holders have shown they know the concepts and principles underneath their area and can evaluate and interpret them there.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a Certificate of Higher Education, you will have shown that you know the main ideas and principles behind your subject and can weigh them up within it.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.10.b2
  forPractitioner: { text: "CertHE holders have shown they can present and assess numbers and qualitative data to build arguments and judge soundly from basic subject theory.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a Certificate of Higher Education, you will have shown that you can present and weigh up data, numbers and words alike, to make an argument and a sound judgement.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.10.b3
  forPractitioner: { text: "Typical CertHE holders will be able to judge which approaches suit a problem in their study or work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Certificate of Higher Education, you will usually be able to judge which ways of tackling a problem fit best.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.10.b4
  forPractitioner: { text: "Typical CertHE holders will be able to report their results accurately and reliably, in structured, coherent argument.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Certificate of Higher Education, you will usually be able to report what you found accurately, in a clear and well-ordered argument.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.10.b5
  forPractitioner: { text: "Typical CertHE holders will be able to take further training and learn new skills in a structured, managed setting.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Certificate of Higher Education, you will usually be able to go on training and learning new skills where the setting is well organised.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.10.b6
  forPractitioner: { text: "CertHE holders will have the qualities and transferable skills for work that asks for some personal responsibility.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a Certificate of Higher Education, you will have the qualities and skills for work where you carry some responsibility yourself.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.12.b1
  forPractitioner: { text: "Foundation degree holders have shown knowledge and critical understanding of the field's established principles and how they developed.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a foundation degree, you will have shown that you know and can think critically about your field's established principles and where they came from.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.12.b2
  forPractitioner: { text: "Foundation degree holders have shown they can apply core concepts and principles beyond where they first met them, including at work where relevant.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a foundation degree, you will have shown that you can use core ideas in new settings, including at work where it fits.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.12.b3
  forPractitioner: { text: "Foundation degree holders have shown knowledge of the main methods of enquiry and can evaluate critically which approaches suit the field's problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a foundation degree, you will have shown that you know your subject's main research methods and can judge which approach suits a problem.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.12.b4
  forPractitioner: { text: "Foundation degree holders have shown they understand the limits of their knowledge and how these shape their analysis and interpretation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a foundation degree, you will have shown that you know where your knowledge ends and how that affects your conclusions.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.12.b5
  forPractitioner: { text: "Typical foundation degree holders will be able to use established techniques to begin and carry out critical analysis and propose solutions from it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a foundation degree, you will usually be able to use proven techniques to analyse information critically and suggest solutions to the problems you find.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.12.b6
  forPractitioner: { text: "Typical foundation degree holders will be able to communicate information, arguments and analysis in varied forms to specialists and non-specialists, and use key discipline techniques well.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a foundation degree, you will usually be able to explain information and arguments in different forms to experts and non-experts, and use your subject's key techniques well.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.12.b7
  forPractitioner: { text: "Typical foundation degree holders will be able to take further training, build skills and gain new competences that prepare them for significant responsibility at work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a foundation degree, you will usually be able to keep training and build new skills that prepare you for real responsibility in an organisation.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.12.b8
  forPractitioner: { text: "Foundation degree holders will have the qualities and transferable skills for work needing personal responsibility and decision-making.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a foundation degree, you will have the qualities and skills for work where you take responsibility and make decisions.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.15.b1
  forPractitioner: { text: "Honours graduates have shown systematic understanding of key aspects of the field and coherent, detailed knowledge, part of it at or near the discipline's forefront.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree, you will have shown a systematic understanding of the key parts of your subject, with detailed knowledge that reaches its leading edge in places.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.15.b2
  forPractitioner: { text: "Honours graduates have shown they can use the discipline's established techniques of analysis and enquiry accurately.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree, you will have shown that you use your subject's standard methods of analysis and research accurately.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.15.b3.1
  forPractitioner: { text: "Honours graduates' conceptual understanding lets them build and sustain arguments or solve problems with ideas and techniques partly at the forefront.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree, you will have shown that you can build and hold an argument, or solve a problem, using some of the newest ideas and methods.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.15.b3.2
  forPractitioner: { text: "Honours graduates' conceptual understanding lets them describe and comment on aspects of current research or advanced scholarship.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree, you will have shown that you can describe and comment on current research in your subject.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.15.b4
  forPractitioner: { text: "Honours graduates have shown they appreciate that knowledge is uncertain, ambiguous and limited.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree, you will have shown that you understand knowledge is uncertain, open to more than one reading and limited.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.15.b5
  forPractitioner: { text: "Honours graduates have shown they can manage their own learning and use scholarly reviews and primary sources, such as refereed articles or original materials.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded an honours degree, you will have shown that you manage your own learning and use research reviews and original sources.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.15.b6
  forPractitioner: { text: "Typical honours graduates will be able to use the methods they learned to review, consolidate, extend and apply knowledge, and to start and run projects.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree, you will usually be able to use the methods you have learned to deepen and extend what you know, and to start and run projects.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.15.b7
  forPractitioner: { text: "Typical honours graduates will be able to critically evaluate arguments, assumptions, abstract concepts and incomplete data, judge, and frame questions that reach one or several solutions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree, you will usually be able to judge arguments, assumptions and patchy data critically, and ask the questions that lead to a solution or several.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.15.b8
  forPractitioner: { text: "Typical honours graduates will be able to communicate information, ideas, problems and solutions to specialist and non-specialist audiences.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree, you will usually be able to explain ideas, problems and solutions to experts and non-experts.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.15.b9.1
  forPractitioner: { text: "Honours graduates will have the qualities and skills for work needing initiative and personal responsibility.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree, you will have the qualities for work where you show initiative and take responsibility.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.15.b9.2
  forPractitioner: { text: "Honours graduates will have the qualities and skills for work needing decisions in complex, unpredictable contexts.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree, you will have the qualities for work where you make decisions in complex, unpredictable situations.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.15.b9.3
  forPractitioner: { text: "Honours graduates will have the learning ability to take further professional or equivalent training.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With an honours degree, you will have the ability to go on to professional training.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.17.b1
  forPractitioner: { text: "Master's graduates have shown systematic understanding and critical awareness of current problems or new insights, much of it at or near the forefront.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a master's degree, you will have shown systematic understanding and a critical grasp of current problems and new insights, much of it at the leading edge.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.17.b2
  forPractitioner: { text: "Master's graduates have shown comprehensive understanding of the techniques for their own research or advanced scholarship.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a master's degree, you will have shown full understanding of the methods your own research needs.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.17.b3
  forPractitioner: { text: "Master's graduates have shown originality in applying knowledge and a practical grasp of how research techniques create and interpret knowledge.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a master's degree, you will have shown originality in using what you know and a practical grasp of how research makes new knowledge.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.17.b4.1
  forPractitioner: { text: "Master's graduates' conceptual understanding lets them critically evaluate current research and advanced scholarship.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a master's degree, you will have shown that you can critically evaluate current research.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.17.b4.2
  forPractitioner: { text: "Master's graduates' conceptual understanding lets them critique methodologies and, where relevant, propose new hypotheses.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a master's degree, you will have shown that you can critique research methods and, where it fits, put forward new hypotheses.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.17.b5
  forPractitioner: { text: "Typical master's graduates will be able to handle complex issues systematically and creatively, judge soundly on incomplete data and state conclusions clearly to any audience.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's degree, you will usually be able to handle complex issues systematically and creatively, judge well without all the facts and explain your conclusions clearly.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.17.b6
  forPractitioner: { text: "Typical master's graduates will be able to show self-direction and originality in solving problems and work autonomously in planning and doing professional tasks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's degree, you will usually be able to direct yourself, solve problems in original ways and plan and carry out professional work on your own.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.17.b7
  forPractitioner: { text: "Typical master's graduates will be able to keep advancing their knowledge and develop new skills to a high level.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's degree, you will usually be able to keep growing your knowledge and build new skills to a high level.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.17.b8.1
  forPractitioner: { text: "Master's graduates will have the qualities and skills for work needing initiative and personal responsibility.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's degree, you will have the qualities for work where you show initiative and take responsibility.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.17.b8.2
  forPractitioner: { text: "Master's graduates will have the qualities and skills for work needing decisions in complex, unpredictable situations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's degree, you will have the qualities for work where you decide in complex, unpredictable situations.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.17.b8.3
  forPractitioner: { text: "Master's graduates will have the independent learning ability that continuing professional development requires.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a master's degree, you will have the ability to keep learning independently throughout your career.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.18.b1
  forPractitioner: { text: "Doctoral graduates have shown they create and interpret new knowledge, by original research or advanced scholarship, good enough for peer review and publication and extending the forefront.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a doctorate, you will have shown that you create new knowledge through original research, good enough to pass peer review, push your field forward and be published.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.18.b2
  forPractitioner: { text: "Doctoral graduates have shown they have systematically acquired and understood a substantial forefront body of knowledge.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a doctorate, you will have shown that you hold a large, systematic body of knowledge at your field's leading edge.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.18.b3
  forPractitioner: { text: "Doctoral graduates have shown they can generally conceptualise, design and implement a project for new knowledge at the forefront, adjusting it when problems arise.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a doctorate, you will have shown that you can plan, design and carry out a research project that creates new knowledge, and change course when problems arise.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.18.b4
  forPractitioner: { text: "Doctoral graduates have shown detailed understanding of the techniques for research and advanced enquiry.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To be awarded a doctorate, you will have shown detailed understanding of the research methods your work needs.", rewrite: full, force: threshold, status: drafted }
- statement: qaa/fheq-2024/4.18.b5
  forPractitioner: { text: "Typical doctoral graduates will be able to judge complex specialist issues in an informed way, often on incomplete data, and communicate them clearly to any audience.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a doctorate, you will usually be able to judge complex issues in your field, often without all the facts, and explain your ideas clearly to anyone.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.18.b6
  forPractitioner: { text: "Typical doctoral graduates will be able to continue advanced pure or applied research and development, contributing substantially to new techniques, ideas or approaches.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a doctorate, you will usually be able to keep doing advanced research and help create new techniques, ideas and approaches.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/4.18.b7
  forPractitioner: { text: "Doctoral graduates will have the qualities and transferable skills for work needing personal responsibility and largely autonomous initiative in complex, unpredictable settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "With a doctorate, you will have the qualities for work where you take responsibility and act largely on your own initiative in complex, unpredictable situations.", rewrite: full, force: will, status: drafted }
- statement: qaa/fheq-2024/use.1
  forPractitioner: { text: "In Scotland, Wales and Northern Ireland a provider follows its nation's framework in full.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you study in Scotland, Wales or Northern Ireland, your qualification is set against the full national framework.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/use.2
  forPractitioner: { text: "In England, the adopted parts are regulatory: OfS-registered providers meet them through condition B5.", rewrite: light, force: must, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/use.3
  forPractitioner: { text: "English providers consult the OfS framework and its sector-recognised standards alongside this one.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/2.2.a
  forPractitioner: { text: "Outside England, every degree-awarding body awards by the relevant framework.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you study in Northern Ireland, Scotland or Wales, your award is made according to the national framework.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/2.2.b
  forPractitioner: { text: "OfS-registered providers in England comply with condition B5.", rewrite: light, force: must, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/2.3
  forPractitioner: { text: "Only qualifications awarded by an approved degree-awarding body can be placed on a framework level.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your qualification sits on a national level only if a body with the power to award degrees awards it.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/2.9.a
  forPractitioner: { text: "A course's learning outcomes are the conditions of its award.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To get your qualification, you must meet your course's learning outcomes.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/2.9.b
  forPractitioner: { text: "Course outcomes align with the qualification descriptor for their level.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course's learning outcomes are matched to the national description of your qualification.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/2.12
  forPractitioner: { text: "Under the Quality Code, a course's standards meet the national framework.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/2.13
  forPractitioner: { text: "A delivery partner understands how threshold standards work and keeps its awarding body's standards.", rewrite: light, force: must, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/4.10.i1
  forPractitioner: { text: "Every CertHE meets the Level 4 descriptor in full.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "A Certificate of Higher Education should give you everything the national description of that award sets out.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/4.10.i2
  forPractitioner: { text: "Other Level 4 qualifications are referenced to this descriptor.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/4.12.i1
  forPractitioner: { text: "Every foundation degree meets the Level 5 descriptor in full.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "A foundation degree should give you everything the national description of that award sets out.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/4.12.i2
  forPractitioner: { text: "DipHEs, HNDs and other Level 5 awards are referenced to this descriptor.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/4.15.i1
  forPractitioner: { text: "Every honours degree meets the Level 6 descriptor in full.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "An honours degree should give you everything the national description of that award sets out.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/4.15.i2
  forPractitioner: { text: "Ordinary degrees, graduate diplomas and other Level 6 awards are referenced to this descriptor.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/4.17.i1
  forPractitioner: { text: "Every master's degree meets the Level 7 descriptor in full.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "A master's degree should give you everything the national description of that award sets out.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/4.17.i2
  forPractitioner: { text: "Postgraduate certificates, diplomas and other Level 7 awards are referenced to this descriptor.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/4.18.i1
  forPractitioner: { text: "Every doctorate meets the Level 8 descriptor in full.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "A doctorate should give you everything the national description of that award sets out.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/4.18.i2
  forPractitioner: { text: "Other Level 8 awards are referenced to this descriptor.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/4.5
  forPractitioner: { text: "A smaller award at a level meets part of the main descriptor, which is its reference point.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a smaller award, such as a certificate, it covers part of what the full qualification at its level sets out.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/4.9
  forPractitioner: { text: "English providers also consult the OfS sector-recognised standards.", rewrite: light, force: should, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/5.5
  forPractitioner: { text: "Awarding bodies and partners align each course's outcomes, or a research degree's criteria, with its descriptor.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course's outcomes are lined up with the national description of your qualification.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.1.a
  forPractitioner: { text: "An awarding body shows that each of its qualifications sits at the right level.", rewrite: light, force: must, status: drafted }
  forBeneficiary: "not-applicable: addressed to providers alone"
- statement: qaa/fheq-2024/6.1.b
  forPractitioner: { text: "Level follows the majority of outcomes; \"postgraduate\" needs most or all outcomes at Level 7 (SCQF 11).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "A \"postgraduate\" award should mean that most or all of what you are assessed on is at master's level.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.3.b1
  forPractitioner: { text: "Course design and review weigh the fit between the course outcomes and the descriptors.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course is checked against the national description of your award when it is designed and reviewed.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/6.3.b2
  forPractitioner: { text: "Course design and review weigh whether there is enough assessment to show the outcomes are met.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course has enough assessment to show you have met its outcomes.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/6.3.b3
  forPractitioner: { text: "Course design and review weigh whether every student can achieve and show the outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course is designed so that you have a fair chance to achieve and show its outcomes.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/6.3.b4
  forPractitioner: { text: "Course design and review weigh any accrediting body's requirements.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If your course is accredited, it is designed to meet the professional body's requirements.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/6.4
  forPractitioner: { text: "Volume of study or credit alone never earns a degree: the outcomes must be met.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are awarded a degree only when you meet or exceed your course's learning outcomes.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.5
  forPractitioner: { text: "Awards follow only from assessed achievement of the outcomes.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your work is judged against set standards, and you are awarded only when assessment shows you have met the outcomes.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.6
  forPractitioner: { text: "A fall-back award needs its own outcomes demonstrated.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you do not meet the outcomes for your qualification, you may get a lower one, but only if you have shown that award's own outcomes.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.6.b1
  forPractitioner: { text: "Example: a DipHE as fall-back needs the DipHE outcomes shown.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For example, if you miss a bachelor's degree, you can be given a DipHE only if you have shown its outcomes.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.6.b2
  forPractitioner: { text: "Example: an MPhil as fall-back needs the MPhil outcomes and criteria met.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For example, if you miss a doctorate, you can be given an MPhil only if you have met its outcomes and criteria.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.7.b1
  forPractitioner: { text: "Every course states clearly the outcomes needed for each award, exit awards included.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course states clearly what you must achieve for each award, including any you could leave with early.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.7.b2
  forPractitioner: { text: "No award is made before achievement is shown.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must show you have met the outcomes before you are given an award.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.7.b3
  forPractitioner: { text: "Compensation and condonement never stand in for full achievement of the outcomes.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Rules that let a near-miss pass cannot give you a qualification without your meeting all its outcomes.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.9
  forPractitioner: { text: "Titles are accurate about level, nature, volume and field.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "The title of your qualification tells others accurately what level and kind of study you did.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.10.b1
  forPractitioner: { text: "\"Honours\", \"master\" and \"doctor\" are reserved for awards that meet their descriptors in full.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "An \"honours\", \"master\" or \"doctor\" title means your award met its national description in full.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.10.b2
  forPractitioner: { text: "\"Graduate\" titles need graduate entry and Level 6 outcomes.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If your award is called \"graduate\", you usually need a degree to enter it, and it is set at bachelor's level.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.10.b3
  forPractitioner: { text: "\"Postgraduate\" titles need outcomes at Level 7 (SCQF 11).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "A \"postgraduate\" award means your outcomes are at master's level.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.11.a
  forPractitioner: { text: "The postgraduate PGCE is a Level 7 award.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If your PGCE is a Postgraduate Certificate in Education, it is set at master's level.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.11.b
  forPractitioner: { text: "The professional graduate PGCE is a Level 6 award.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If your PGCE is a Professional Graduate Certificate in Education, it is set at bachelor's level.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.13.b2
  forPractitioner: { text: "At Level 6, certificate means at least a third of a year, diploma at least two-thirds.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a graduate certificate, expect at least a third of a full-time year; a graduate diploma, at least two-thirds.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/6.13.b3
  forPractitioner: { text: "At Level 7, certificate means at least a third of a year, diploma at least two-thirds.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a postgraduate certificate, expect at least a third of a full-time year; a postgraduate diploma, at least two-thirds.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/6.14.b1
  forPractitioner: { text: "Foundation degree: FHEQ 5 only.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you take a foundation degree, it is always at Level 5.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.14.b2
  forPractitioner: { text: "Scottish non-honours bachelor's: SCQF 9 only.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you take a non-honours bachelor's degree in Scotland, it is always at Level 9 of the Scottish framework.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.14.b3
  forPractitioner: { text: "Honours degree: FHEQ 6 or SCQF 10 only.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you take an honours degree, it is always at Level 6 (Level 10 in Scotland).", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.14.b4
  forPractitioner: { text: "Master's degree: FHEQ 7 or SCQF 11 only.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you take a master's degree, it is always at Level 7 (Level 11 in Scotland).", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.14.b5
  forPractitioner: { text: "Doctoral degree: FHEQ 8 or SCQF 12 only.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you take a doctorate, it is always at Level 8 (Level 12 in Scotland).", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.15
  forPractitioner: { text: "PhD and DPhil: assessed by thesis, published work, or creative work with commentary.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you take a PhD or DPhil, you are assessed by thesis, published work, or creative work with a written commentary.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.16
  forPractitioner: { text: "MPhil: extended master's with substantial research.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take an MPhil, expect an extended master's with a large research part.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/6.17
  forPractitioner: { text: "Taught doctorates name their discipline (EdD, DClinPsy).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you take a taught doctorate, its title usually names your subject.", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/6.18.b1
  forPractitioner: { text: "\"A and B\": two subjects in roughly equal balance.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "A title \"A and B\" means you studied two subjects about equally.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.18.b2
  forPractitioner: { text: "\"A with B\": major and minor, the minor at least a quarter.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "A title \"A with B\" means B made up at least a quarter of your course.", rewrite: full, force: must, status: drafted }
- statement: qaa/fheq-2024/6.19
  forPractitioner: { text: "At most three subjects in a title; beyond that, \"Combined Studies\".", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your award title normally names no more than three subjects; with more, it is \"Combined Studies\".", rewrite: full, force: should, status: drafted }
- statement: qaa/fheq-2024/annex-b/short/b1
  forPractitioner: { text: "Short-cycle graduates typically know a field at advanced-textbook level, building on school, as a base for work and further study.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a short-cycle course, you usually know your field at the level of advanced textbooks, enough to work in it or to study on.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/short/b2
  forPractitioner: { text: "Short-cycle graduates typically apply what they know in the workplace.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a short-cycle course, you can usually put what you know to use at work.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/short/b3
  forPractitioner: { text: "Short-cycle graduates typically identify and use data to respond to well-defined problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a short-cycle course, you can usually find and use data to answer clearly set problems.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/short/b4
  forPractitioner: { text: "Short-cycle graduates typically talk about their understanding and work with peers, supervisors and clients.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a short-cycle course, you can usually explain your work to colleagues, managers and clients.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/short/b5
  forPractitioner: { text: "Short-cycle graduates typically have the learning skills to go on studying with some independence.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a short-cycle course, you can usually go on studying with some independence.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/1/b1
  forPractitioner: { text: "First-cycle graduates typically know their field at advanced-textbook level, with some of it informed by the forefront.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a bachelor's, you usually know your field at the level of advanced textbooks, with some of it drawn from current research.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/1/b2
  forPractitioner: { text: "First-cycle graduates typically apply knowledge professionally, shown by sustained argument and problem-solving in their field.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a bachelor's, you can usually apply what you know in a professional way, making arguments and solving problems in your field.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/1/b3
  forPractitioner: { text: "First-cycle graduates typically gather and read data to make judgements that weigh social, scientific or ethical issues.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a bachelor's, you can usually gather and read data to make judgements, thinking about their social, scientific or ethical side.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/1/b4
  forPractitioner: { text: "First-cycle graduates typically communicate ideas, problems and solutions to expert and lay audiences.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a bachelor's, you can usually explain ideas, problems and solutions to experts and non-experts.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/1/b5
  forPractitioner: { text: "First-cycle graduates typically have the learning skills for further study with much independence.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a bachelor's, you can usually go on studying largely on your own.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/2/b1
  forPractitioner: { text: "Second-cycle graduates typically hold knowledge beyond the first cycle that lets them be original, often in research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a master's, your knowledge usually goes past a bachelor's and lets you develop or apply ideas in original ways, often through research.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/2/b2
  forPractitioner: { text: "Second-cycle graduates typically apply knowledge and problem-solving in unfamiliar and multidisciplinary settings.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a master's, you can usually use what you know to solve problems in new settings and across subjects.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/2/b3
  forPractitioner: { text: "Second-cycle graduates typically integrate knowledge, handle complexity and judge on limited information, mindful of social and ethical responsibility.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a master's, you can usually bring knowledge together, handle complexity and make judgements without full information, with an eye to their ethics.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/2/b4
  forPractitioner: { text: "Second-cycle graduates typically state their conclusions and reasoning clearly to any audience.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a master's, you can usually explain your conclusions and the reasons for them clearly to anyone.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/2/b5
  forPractitioner: { text: "Second-cycle graduates typically have the learning skills for largely self-directed study.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a master's, you can usually direct your own further study.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/3/b1
  forPractitioner: { text: "Third-cycle graduates typically understand their field systematically and have mastered its research methods.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a doctorate, you usually understand your field systematically and have mastered its research methods.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/3/b2
  forPractitioner: { text: "Third-cycle graduates typically conceive, design, run and adapt substantial research with integrity.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a doctorate, you can usually plan, run and adapt a major research project with integrity.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/3/b3
  forPractitioner: { text: "Third-cycle graduates typically contribute original research that pushes knowledge forward, some of it publishable.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a doctorate, you have usually added original research to your field, some of it good enough for refereed publication.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/3/b4
  forPractitioner: { text: "Third-cycle graduates typically analyse, evaluate and synthesise new, complex ideas critically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a doctorate, you can usually analyse, judge and bring together new and complex ideas.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/3/b5
  forPractitioner: { text: "Third-cycle graduates typically talk about their expertise with peers, scholars and the public.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a doctorate, you can usually talk about your expertise with other researchers and with the public.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-b/3/b6
  forPractitioner: { text: "Third-cycle graduates can typically be expected to drive technological, social or cultural progress in academic and professional settings.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the end of a doctorate, you can usually be expected to help move technology, society or culture forward.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r1/ns
  forPractitioner: { text: "Did not show enough knowledge, understanding and cognitive, practical and transferable skill, consistently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/summary/r1/3rd
  forPractitioner: { text: "Showed knowledge and understanding and the cognitive, practical and transferable skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you show knowledge and understanding, and thinking, practical and transferable skills.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r1/2.2
  forPractitioner: { text: "Showed strong knowledge and understanding and strong cognitive, practical and transferable skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, your knowledge, understanding and skills are strong.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r1/2.1
  forPractitioner: { text: "Showed thorough knowledge and understanding and thorough cognitive, practical and transferable skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, your knowledge, understanding and skills are thorough.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r1/1st
  forPractitioner: { text: "Showed advanced knowledge and understanding and advanced cognitive, practical and transferable skills, throughout.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, your knowledge, understanding and skills are advanced, and you show this throughout.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r2/ns
  forPractitioner: { text: "Did not consistently show enough initiative or take enough personal responsibility.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/summary/r2/3rd
  forPractitioner: { text: "Showed initiative and took personal responsibility.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you show initiative and take responsibility for your work.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r2/2.2
  forPractitioner: { text: "Showed initiative and personal responsibility.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you show initiative and responsibility.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r2/2.1
  forPractitioner: { text: "Showed good initiative and personal responsibility.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you show good initiative and responsibility.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r2/1st
  forPractitioner: { text: "Showed exceptional initiative and personal responsibility, throughout.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, your initiative and responsibility are exceptional, throughout.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r3/ns
  forPractitioner: { text: "Did not consistently show they could reflect on their own work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/summary/r3/3rd
  forPractitioner: { text: "Showed some ability to reflect on their own work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you show some ability to reflect on your work.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r3/2.2
  forPractitioner: { text: "Showed they can reflect on their own work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you show you can reflect on your work.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r3/2.1
  forPractitioner: { text: "Showed they can reflect critically on their own work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you reflect critically on your work.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r3/1st
  forPractitioner: { text: "Showed throughout that they can reflect on their work critically and independently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you reflect on your work critically and on your own, throughout.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r4/ns
  forPractitioner: { text: "Did not consistently show problem-solving skill.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/summary/r4/3rd
  forPractitioner: { text: "Showed problem-solving skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you show you can solve problems.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r4/2.2
  forPractitioner: { text: "Showed strong problem-solving skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you solve problems well.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r4/2.1
  forPractitioner: { text: "Showed thorough problem-solving skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you solve problems thoroughly.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/summary/r4/1st
  forPractitioner: { text: "Showed exceptional problem-solving skills throughout.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, your problem-solving is exceptional, throughout.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r1/ns
  forPractitioner: { text: "Subject knowledge and understanding fall short in breadth or depth, with gaps in key areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/knowledge/r1/3rd
  forPractitioner: { text: "Has shown knowledge and understanding of key aspects deep enough to handle the field's terms, facts and concepts.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you know the key parts of your subject well enough to handle its terms, facts and ideas.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r1/2.2
  forPractitioner: { text: "Has shown sound breadth and depth of subject knowledge, though at times more descriptive than critical or analytical.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, your knowledge is broad and deep enough, though you may sometimes describe more than you analyse.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r1/2.1
  forPractitioner: { text: "Has shown sophisticated breadth and depth of knowledge with clear critical insight.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, your knowledge is broad, deep and sophisticated, and you show clear critical insight.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r1/1st
  forPractitioner: { text: "Has shown exceptional knowledge and understanding, well past the threshold for a graduate and past what was taught.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, your knowledge is exceptional, going well past what a graduate needs and past what you were taught.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r2/ns
  forPractitioner: { text: "Has shown inadequate understanding of the subject's theories, paradigms, concepts and principles, and of their limits and ambiguities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/knowledge/r2/3rd
  forPractitioner: { text: "Has shown understanding of the subject's theories, paradigms, concepts and principles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you understand your subject's theories, ideas and principles.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r2/2.2
  forPractitioner: { text: "Has consistently understood the subject's theories and principles and some more specialised areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you understand your subject's theories consistently, and some of its specialist areas too.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r2/2.1
  forPractitioner: { text: "Has shown thorough understanding of the subject's theories and principles and sound understanding of specialised areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you understand your subject's theories thoroughly and its specialist areas soundly.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r2/1st
  forPractitioner: { text: "Has shown exceptional understanding of the subject's theories and principles, with in-depth knowledge, near mastery, of several specialised areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, your grasp of theory is exceptional and you know several specialist areas in depth, close to mastery.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r3/ns
  forPractitioner: { text: "Has not produced enough evidence of background investigation, research or study.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/knowledge/r3/3rd
  forPractitioner: { text: "Has done general background research with established techniques and can pick out the relevant points.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you research the background with standard methods and pick out what matters.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r3/2.2
  forPractitioner: { text: "Has done background research accurately with established techniques and can appraise academic sources critically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you research accurately with standard methods and judge academic sources critically.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r3/2.1
  forPractitioner: { text: "Has done thorough, accurate background research and has a well-developed ability to appraise many kinds of source critically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, your research is thorough and accurate, and you judge a wide range of sources critically.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/knowledge/r3/1st
  forPractitioner: { text: "Has carried out independent, extensive and fitting research well past the usual range, evaluated critically, to move work forward or steer arguments.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you research independently and widely, well past the usual range, and use what you find to drive your work and arguments.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r1/ns
  forPractitioner: { text: "Leans too heavily on set sources and cannot yet choose and weigh reading and research adequately.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/cognitive/r1/3rd
  forPractitioner: { text: "Has shown they can choose, weigh and comment on reading, research and primary sources.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you choose, weigh up and comment on your reading and sources.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r1/2.2
  forPractitioner: { text: "Has chosen, weighed and commented on reading, research and primary sources, at times going past the set range.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you choose and weigh up sources well, sometimes going past the reading list.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r1/2.1
  forPractitioner: { text: "Has chosen sources thoroughly, weighed them critically and commented on them, usually going past the set range.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you choose sources thoroughly and weigh them critically, usually going past the reading list.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r1/1st
  forPractitioner: { text: "Has shown exceptional skill in choosing, weighing and synthesising a broad range of research, sources and views, and integrating references.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you choose, weigh up and bring together a broad range of research and views exceptionally well.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r2/ns
  forPractitioner: { text: "Arguments and explanations are weak or poorly built; cannot yet evaluate others' arguments critically or weigh alternatives.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/cognitive/r2/3rd
  forPractitioner: { text: "Can build and keep up an argument with some regard to other views and can explain often complex matters.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you build and hold an argument, give some thought to other views and explain complex ideas.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r2/2.2
  forPractitioner: { text: "Argues logically with evidence, considers and weighs a range of views, and explains complex matters clearly and consistently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you argue logically with evidence, weigh up a range of views and explain complex ideas clearly.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r2/2.1
  forPractitioner: { text: "Makes coherent, well-supported arguments, weighs and synthesises views critically, and interprets complex matters thoroughly and perceptively.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, your arguments are coherent and well supported, you bring views together critically and you read complex ideas perceptively.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r2/1st
  forPractitioner: { text: "Makes consistent, logical, well-built and supported arguments, synthesises a wide range of views systematically and critically, and interprets with sophistication and insight.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, your arguments are consistent, logical and well supported, you bring together a wide range of views and your insight is sophisticated.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r3/ns
  forPractitioner: { text: "Shows only limited ability to solve problems or make decisions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/cognitive/r3/3rd
  forPractitioner: { text: "Can solve problems with a range of methods and make decisions in complex, unpredictable circumstances.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you solve problems with a range of methods and make decisions when things are complex and uncertain.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r3/2.2
  forPractitioner: { text: "Consistently solves complex problems, choosing and applying fitting methods, and makes decisions in complex, unpredictable circumstances.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you solve complex problems consistently, choosing methods that fit.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r3/2.1
  forPractitioner: { text: "Solves problems thoroughly, choosing and justifying a wide range of methods, and decides in complex, unpredictable circumstances with some autonomy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you solve problems thoroughly, explain why you chose your methods and make decisions with some independence.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r3/1st
  forPractitioner: { text: "Has a wide range of highly developed problem-solving skills and a strong aptitude for highly autonomous decisions in the most complex, unpredictable circumstances.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, your problem-solving is highly developed and you make decisions independently in the hardest, least predictable situations.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r4/ns
  forPractitioner: { text: "Shows little or no real creativity.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/cognitive/r4/3rd
  forPractitioner: { text: "Has produced some creative work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you produce some creative work.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r4/2.2
  forPractitioner: { text: "Has shown creativity consistently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you are creative consistently.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r4/2.1
  forPractitioner: { text: "Has been highly creative and original throughout.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, your work is highly creative and original throughout.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/cognitive/r4/1st
  forPractitioner: { text: "Has shown exceptional creative flair and originality.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, your creative flair and originality are exceptional.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r1/ns
  forPractitioner: { text: "Has not shown enough evidence of developing or applying the discipline's skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/practical/r1/3rd
  forPractitioner: { text: "Has shown evidence of developing and applying the discipline's specialist skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you show you are developing and using your subject's specialist skills.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r1/2.2
  forPractitioner: { text: "Has consistently developed and applied the discipline's specialist skills in an informed way.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you develop and use your subject's specialist skills consistently and knowingly.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r1/2.1
  forPractitioner: { text: "Has performed the discipline's specialist skills capably and effectively.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you use your subject's specialist skills capably and effectively.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r1/1st
  forPractitioner: { text: "Has applied the discipline's specialist skills in an accomplished and innovative way.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you use your subject's specialist skills in an accomplished and inventive way.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r2/ns
  forPractitioner: { text: "Attempted practical tasks but followed a narrow, mechanical procedure, with errors and little or no independence.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/practical/r2/3rd
  forPractitioner: { text: "Has completed practical tasks accurately and with some independence.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you complete practical tasks accurately and with some independence.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r2/2.2
  forPractitioner: { text: "Has consistently completed practical tasks mainly independently, accurately, with coordination and proficiency.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you complete practical tasks mostly on your own, accurately and proficiently.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r2/2.1
  forPractitioner: { text: "Has carried out practical tasks autonomously, accurately and with coordination.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you carry out practical tasks on your own, accurately and smoothly.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r2/1st
  forPractitioner: { text: "Has completed practical tasks autonomously, highly accurately, with coordination and proficiency.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you carry out practical tasks on your own, highly accurately and proficiently.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r3/ns
  forPractitioner: { text: "Shows a lack of technical, creative or artistic skill in most or key areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/practical/r3/3rd
  forPractitioner: { text: "Has shown technical, creative or artistic skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you show technical, creative or artistic skill.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r3/2.2
  forPractitioner: { text: "Has consistently shown well-developed technical, creative or artistic skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, your technical, creative or artistic skills are well developed and consistent.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r3/2.1
  forPractitioner: { text: "Has a thorough command of highly developed technical, creative or artistic skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you command highly developed technical, creative or artistic skills.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r3/1st
  forPractitioner: { text: "Has a full range of exceptional technical, creative or artistic skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you have a full range of exceptional technical, creative or artistic skills.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r4/ns
  forPractitioner: { text: "Has not presented findings clearly or effectively, and gathered, processed and interpreted data unsatisfactorily.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/practical/r4/3rd
  forPractitioner: { text: "Has presented findings in several formats and gathered, processed and interpreted data effectively.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you present your findings in several formats and handle data effectively.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r4/2.2
  forPractitioner: { text: "Has consistently presented findings effectively in many formats and handled data efficiently and effectively.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you present findings well in many formats and handle data efficiently.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r4/2.1
  forPractitioner: { text: "Has presented thorough findings perceptively in a wide range of formats and handled a wide range of complex data efficiently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you present thorough findings perceptively in many formats and handle complex data efficiently.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/practical/r4/1st
  forPractitioner: { text: "Has presented findings perceptively and convincingly in a wide range of formats and handled a wide range of complex data efficiently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you present findings perceptively and convincingly in many formats and handle complex data efficiently.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r1/ns
  forPractitioner: { text: "Cannot yet express ideas clearly in speech, digitally or in writing; terminology inaccurate, many errors; basic numeracy and digital literacy not shown consistently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/transferable/r1/3rd
  forPractitioner: { text: "Communicates information, ideas, problems and solutions in speech, digitally and in writing with clear expression; has shown numeracy and digital literacy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you communicate clearly in speech, writing and online, and show numeracy and digital skills.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r1/2.2
  forPractitioner: { text: "Communicates consistently and confidently in all modes, in a clear, coherent and expressive style, with strong numeracy and digital literacy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you communicate confidently in a clear, coherent style, with strong number and digital skills.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r1/2.1
  forPractitioner: { text: "Communicates with a high degree of proficiency in all modes, in a clear, fluent, expressive style; numeracy and digital literacy of a high standard.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you communicate fluently and proficiently, with a high standard of number and digital skills.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r1/1st
  forPractitioner: { text: "Communicates to an accomplished level in all modes, in an accurate, fluent and sophisticated style; numeracy and digital literacy exceptional.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you communicate in an accurate, fluent and sophisticated way, with exceptional number and digital skills.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r2/ns
  forPractitioner: { text: "Contributed to group discussion or project work only infrequently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/transferable/r2/3rd
  forPractitioner: { text: "Can make useful contributions to group discussion and project work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you make useful contributions to group work.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r2/2.2
  forPractitioner: { text: "Consistently makes coherent and constructive contributions to group discussion and project work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you contribute to group work coherently and constructively.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r2/2.1
  forPractitioner: { text: "Makes strong, valuable contributions to group work and understands team and leadership roles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, your contributions to group work are strong, and you understand team and leadership roles.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r2/1st
  forPractitioner: { text: "Makes clear, authoritative and valuable contributions to group work, with exceptional teamwork and leadership.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you contribute to group work with authority, and your teamwork and leadership are exceptional.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r3/ns
  forPractitioner: { text: "Shows little or no ability to manage learning or work without supervision.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/transferable/r3/3rd
  forPractitioner: { text: "Can manage their own learning and work with little or no supervision.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you manage your learning and work with little or no supervision.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r3/2.2
  forPractitioner: { text: "Consistently manages their learning systematically and works without supervision.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you manage your learning systematically and work unsupervised.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r3/2.1
  forPractitioner: { text: "Shows a strong ability to manage their learning systematically and work without supervision.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you manage your learning strongly and systematically, without supervision.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r3/1st
  forPractitioner: { text: "Manages learning exceptionally on their own initiative and works unsupervised.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you direct your own learning on your own initiative, exceptionally well.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r4/ns
  forPractitioner: { text: "Has not shown adequate initiative or personal responsibility.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/transferable/r4/3rd
  forPractitioner: { text: "Has shown initiative or personal responsibility.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you show initiative or take responsibility.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r4/2.2
  forPractitioner: { text: "Has consistently shown initiative or personal responsibility.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you show initiative or responsibility consistently.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r4/2.1
  forPractitioner: { text: "Has consistently shown well-developed initiative or personal responsibility.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, your initiative and responsibility are well developed and consistent.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r4/1st
  forPractitioner: { text: "Has shown exceptional initiative or personal responsibility.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, your initiative and responsibility are exceptional.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r5/ns
  forPractitioner: { text: "Shows little or no capacity for reflecting on their work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/transferable/r5/3rd
  forPractitioner: { text: "Has shown they can reflect on their work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a third, you show you can reflect on your work.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r5/2.2
  forPractitioner: { text: "Has consistently reflected on their work in a well-developed way.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.2, you reflect on your work in a well-developed way, consistently.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r5/2.1
  forPractitioner: { text: "Has shown they can reflect critically on their work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a 2.1, you reflect critically on your work.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/transferable/r5/1st
  forPractitioner: { text: "Has shown an exceptional ability to reflect on their work critically and independently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For a first, you reflect on your work critically and independently, exceptionally well.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/professional/r1/ns
  forPractitioner: { text: "Has not shown professional competence when assessed against a PSRB's requirements.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/professional/r1/3rd-1st
  forPractitioner: { text: "Has shown professional competence when assessed against a PSRB's requirements; the same for every classification.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For any honours classification on an accredited course, you meet the professional body's requirements for competence.", rewrite: full, force: describes, status: drafted }
- statement: qaa/fheq-2024/annex-d/professional/r2/ns
  forPractitioner: { text: "Has not kept to the rules or conventions set by regulators or the industry.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: "not-applicable: the not-successful column describes failure; a student version is for P3 (Part E)"
- statement: qaa/fheq-2024/annex-d/professional/r2/3rd-1st
  forPractitioner: { text: "Has kept to the rules and conventions set by regulators or the industry; the same for every classification.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "For any honours classification on such a course, you keep to the rules and conventions of regulators and your industry.", rewrite: full, force: describes, status: drafted }
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary. Each level a shared level record; equivalences only as the document states them (framework rule 2). -->
```yaml
levels:
  - { id: fheq:4, role: defines, locator: "3.4; 4.10", typical: CertHE }
  - { id: fheq:5, role: defines, locator: "3.4; 4.12", typical: foundation degree }
  - { id: fheq:6, role: defines, locator: "3.4; 4.15", typical: bachelor's degree with honours }
  - { id: fheq:7, role: defines, locator: "3.4; 4.17", typical: master's degree }
  - { id: fheq:8, role: defines, locator: "3.4; 4.18", typical: doctoral degree }
  - { id: "fqheis:7 to fqheis:12", role: refers, locator: "std:doc:qaa-fqheis-2024-framework (D-std-0010); fqheis:11 and fqheis:12 take this document's 4.17 and 4.18" }
  - { id: qfehea:short, role: refers, locator: "Annex B; Table 1" }
  - { id: qfehea:1, role: refers, locator: "Annex B; Table 1" }
  - { id: qfehea:2, role: refers, locator: "Annex B; Table 1" }
  - { id: qfehea:3, role: refers, locator: "Annex B; Table 1" }
crosswalks:
  - { from: fheq:7, to: fqheis:11, relation: shared-descriptor, source: "4.8 and the heading of 4.17: one descriptor common to both" }
  - { from: fheq:8, to: fqheis:12, relation: shared-descriptor, source: "3.4 (doctoral level 8, in Scotland 12); 4.8 and the heading of 4.18" }
  - { from: "cqfw:4 to cqfw:8", to: "fheq:4 to fheq:8", relation: compares-with, source: "2.24: the CQFW's Levels 4 to 8 'compare with the corresponding levels of the FHEQ'; 2.23: the FHEQ forms part of the CQFW" }
  - { from: "rqf:4 to rqf:8", to: "fheq:4 to fheq:8", relation: compares-with, source: "2.24 (the RQF is separate from the FHEQ)" }
  - { from: fqheis, to: scqf, relation: part-of, source: "2.23: the FQHEIS forms part of the SCQF; its levels are SCQF levels (3.4)" }

  # Table 1 (read from the page image, printed page 12): the qualification-level crosswalk. Equivalence holds per qualification, not per level: FHEQ 6 sits beside SCQF 10 for honours and SCQF 9 for other bachelor's and graduate awards.
  - { qualification: "Doctoral degrees (eg PhD/DPhil, EdD, DBA, DClinPsy)", fheq: 8, fqheis: 12, qfehea: "third cycle (end of cycle)", source: "Table 1" }
  - { qualification: "Master's degrees (eg MPhil, MLitt, MRes, MA, MSc)", fheq: 7, fqheis: 11, qfehea: "second cycle (end of cycle)", source: "Table 1" }
  - { qualification: "Integrated master's degrees (eg MEng, MChem, MPhys, MPharm)", fheq: 7, fqheis: 11, qfehea: "second cycle (end of cycle)", source: "Table 1" }
  - { qualification: "Primary qualifications (or first degrees) in medicine, dentistry and veterinary science", fheq: 7, fqheis: 11, qfehea: "second cycle (end of cycle)", source: "Table 1" }
  - { qualification: "Postgraduate diplomas", fheq: 7, fqheis: 11, qfehea: "none (shaded: short of the cycle's expectations, 3.7)", source: "Table 1" }
  - { qualification: "Postgraduate Certificate in Education (PGCE) / Postgraduate Diploma in Education (PGDE)", fheq: 7, fqheis: 11, qfehea: "none (shaded: short of the cycle's expectations, 3.7)", source: "Table 1" }
  - { qualification: "Postgraduate certificates", fheq: 7, fqheis: 11, qfehea: "none (shaded: short of the cycle's expectations, 3.7)", source: "Table 1" }
  - { qualification: "Bachelor's degrees with honours (eg BA/BSc Hons)", fheq: 6, fqheis: 10, qfehea: "first cycle (end of cycle)", source: "Table 1" }
  - { qualification: "Bachelor's degrees", fheq: 6, fqheis: 9, qfehea: "none (shaded: short of the cycle's expectations, 3.7)", source: "Table 1" }
  - { qualification: "Professional Graduate Certificate in Education (PGCE) in England, Wales and Northern Ireland", fheq: 6, fqheis: 9, qfehea: "none (shaded: short of the cycle's expectations, 3.7)", source: "Table 1" }
  - { qualification: "Graduate diplomas", fheq: 6, fqheis: 9, qfehea: "none (shaded: short of the cycle's expectations, 3.7)", source: "Table 1" }
  - { qualification: "Graduate certificates", fheq: 6, fqheis: 9, qfehea: "none (shaded: short of the cycle's expectations, 3.7)", source: "Table 1" }
  - { qualification: "Foundation degrees (eg FdA, FdSc)", fheq: 5, fqheis: "NA", qfehea: "short cycle (within or linked to the first cycle)", source: "Table 1" }
  - { qualification: "Diplomas of Higher Education (DipHE)", fheq: 5, fqheis: 8, qfehea: "short cycle (within or linked to the first cycle)", source: "Table 1" }
  - { qualification: "Higher National Diplomas (HND) awarded by degree-awarding bodies in England, Wales and Northern Ireland under licence from Pearson", fheq: 5, fqheis: "NA", qfehea: "short cycle (within or linked to the first cycle)", source: "Table 1" }
  - { qualification: "Higher National Certificates (HNC) awarded by degree-awarding bodies in England, Wales and Northern Ireland under licence from Pearson", fheq: 4, fqheis: "NA", qfehea: "none (shaded: short of the cycle's expectations, 3.7)", source: "Table 1" }
  - { qualification: "Certificates of Higher Education (CertHE)", fheq: 4, fqheis: 7, qfehea: "none (shaded: short of the cycle's expectations, 3.7)", source: "Table 1" }
  - { from: "qfehea:3, qfehea:2, qfehea:1, qfehea:short", to: "fheq and fqheis, by qualification as above", relation: corresponds, source: "Table 1; 2.20; Annex B" }
credit:   # Annex C, read from the page images (printed pages 40 to 43); values exactly as printed, typical minimum credit per qualification, with any minimum or maximum at a stated level in brackets; qualification names and values are data, copied exactly
  - { qualification: "PhD/DPhil", fheq: 8, scqf: 12, englandNI: "Not typically credit-rated", scotland: "Not typically credit-rated", wales: "Not typically credit-rated", ects: "Not typically credit-rated" }
  - { qualification: "Professional doctorates (only if credit-based) (EdD, DBA, DClinPsy)", fheq: 8, scqf: 12, englandNI: "540 (360 at FHEQ Level 8)", scotland: "540 (420 at SCQF Level 12)", wales: "540 (360 at FHEQ Level 8 and a max of 30 at FHEQ Level 6)", ects: "Not typically credit-rated" }
  - { qualification: "Research master's degrees (eg MRes, MPhil)", fheq: 7, scqf: 11, englandNI: "Not typically credit-rated", scotland: "Not typically credit-rated", wales: "180 (150 at FHEQ Level 7 and a max of 30 at FHEQ Level 6)", ects: "The minimum requirement is 60 ECTS points; however, a range of 90-100 ECTS points is more typical at second-cycle level" }
  - { qualification: "Taught master's degrees (eg MA, MSc)", fheq: 7, scqf: 11, englandNI: "180 (150 at FHEQ Level 7)", scotland: "180 (150 at SCQF Level 11)", wales: "180 (150 at FHEQ Level 7 and a max of 30 at FHEQ Level 6)", ects: "as above" }
  - { qualification: "Integrated master's degrees (eg MEng, MChem, MPhys, MPharm)", fheq: 7, scqf: 11, englandNI: "480 (120 at FHEQ Level 7)", scotland: "600c (120 at SCQF Level 11)", wales: "480 (120 at FHEQ Level 7 and a max of 30 at CQFW Level 3)", ects: "as above" }
  - { qualification: "Primary qualifications (or first degrees) in medicine, dentistry and veterinary science", fheq: 7, scqf: 11, englandNI: "Not typically credit-rated", scotland: "Not typically credit-rated", wales: "Not typically credit-rated", ects: "as above" }
  - { qualification: "Postgraduate diplomas", fheq: 7, scqf: 11, englandNI: "120 (90 at FHEQ Level 7)", scotland: "120 (90 at SCQF Level 11)", wales: "120 (90 at FHEQ Level 7 and a max of 30 at FHEQ Level 6)", ects: shaded }
  - { qualification: "PGCE in England, Wales and Northern Ireland / PGDE in Scotland", fheq: 7, scqf: 11, englandNI: "60 (40 at FHEQ Level 7)", scotland: "60 (40 at SCQF Level 11)", wales: "120 (40 at FHEQ Level 7 and a max of 80 at FHEQ Level 6)", ects: shaded }
  - { qualification: "Postgraduate certificates", fheq: 7, scqf: 11, englandNI: "60 (40 at FHEQ Level 7)", scotland: "60 (40 at SCQF Level 11)", wales: "60 (40 at FHEQ Level 7 and a max of 20 at FHEQ Level 6)", ects: shaded }
  - { qualification: "Bachelor's degrees with honours (eg BA/BSc Hons)", fheq: 6, scqf: 10, englandNI: "360 (90 at FHEQ Level 6)", scotland: "480d (90 at SCQF Level 10)", wales: "360 (90 at FHEQ Level 6 and a max of 30 at CQFW Level 3)", ects: "180-240 ECTS points" }
  - { qualification: "Bachelor's degrees", fheq: 6, scqf: 9, englandNI: "300 (60 at FHEQ Level 6)", scotland: "360 (60 at SCQF Level 9)", wales: "300 (60 at FHEQ Level 6 and a max of 30 at CQFW Level 3)", ects: "180-240 ECTS points" }
  - { qualification: "Professional Graduate Certificate in Education (PGCE)", fheq: 6, scqf: "NA", englandNI: "60 (40 at FHEQ Level 6)", scotland: "NA", wales: "120 (90 at FHEQ Level 6 and a max of 30 at CQFW Level 3)", ects: shaded }
  - { qualification: "Graduate diplomas", fheq: 6, scqf: 9, englandNI: "80 (80 at FHEQ Level 6)", scotland: "120 (at SCQF Level 9 or above)", wales: "120 (90 at FHEQ Level 6 and a max of 30 at CQFW Level 3)", ects: shaded }
  - { qualification: "Graduate certificates", fheq: 6, scqf: 9, englandNI: "40 (40 at FHEQ Level 6)", scotland: "60 at SCQF Level 9 or above", wales: "60 (40 at FHEQ Level 6 and a max of 20 at CQFW Level 3)", ects: shaded }
  - { qualification: "Foundation degrees (eg FdA, FdSc)", fheq: 5, scqf: 8, englandNI: "240 (90 at FHEQ Level 5)", scotland: "NA", wales: "240 (90 at FHEQ Level 5 and a max of 30 at CQFW Level 3)", ects: "Approximately 120 ECTS points" }
  - { qualification: "Diplomas of Higher Education (DipHE)", fheq: 5, scqf: 8, englandNI: "240 (90 at FHEQ Level 5)", scotland: "240 (90 at SCQF Level 8 or above)", wales: "240 (90 at FHEQ Level 5 and a max of 30 at CQFW Level 3)", ects: "Approximately 120 ECTS points" }
  - { qualification: "Higher National Diplomas (HND) awarded by DABs in England, Wales and Northern Ireland under licence from Pearson", fheq: 5, scqf: "NA", englandNI: "240 (90 at FHEQ Level 5)", scotland: "NA", wales: "240 (90 at FHEQ Level 5 and a max of 30 at CQFW Level 3)", ects: "Approximately 120 ECTS points" }
  - { qualification: "Higher National Certificates (HNC) awarded by DABs in England, Wales and Northern Ireland under licence from Pearson", fheq: 4, scqf: "NA", englandNI: "150 (120 at FHEQ Level 4)", scotland: "NA", wales: "150 (30 at FHEQ Level 5 and a max of 30 at CQFW Level 3)", ects: shaded }
  - { qualification: "Certificates of Higher Education (CertHE)", fheq: 4, scqf: 7, englandNI: "120 (90 at FHEQ Level 4)", scotland: "120 (90 at SCQF Level 7 or above)", wales: "120 (90 at FHEQ Level 4 and a max of 30 at CQFW Level 3)", ects: shaded }
```

### S6 Themes
`not-applicable-by-design`: the document carries no cross-cutting themes.

### S7 Relations
```yaml
- { rel: partOf, target: "CQFW (the FHEQ is part of it, 2.23)", note: "std:doc:welsh-government-cqfw-2009-framework" }
- { rel: partOf, target: "SCQF (the FQHEIS is part of it, 2.23)" }
- { rel: particularisedBy, target: "QAA Subject Benchmark Statements (4.1)", note: "std:doc:qaa-psychology-2023-benchmarks and the 53 others (S-02)" }
- { rel: alignsWith, target: "OfS sector-recognised standards (4.9, England)" }
- { rel: alignsWith, target: "QF-EHEA and its Dublin descriptors (2.16 to 2.20, Annex B)" }
- { rel: alignsWith, target: "EQF, verified compatible (2.21, 2.22; last verified June 2019)" }
- { rel: refersTo, target: "QAA Characteristics Statements (5.4); Higher Education Credit Framework for England (2.27 to 2.29); the Quality Code (2.12)" }
```

### S8 Currency and review
```yaml
published: 2024-02-21
lastReviewed: 2024-02
reviewCycle: none-stated   # 4.7: QAA reviews the need for further or amended descriptors
consultation: none-stated   # Annex D: informed by providers' criteria and consultation with students, providers and PSRBs
replacedBy: unknown
```

### S9 Commentary (optional)
`unknown`: not researched.

### SL Level language
<!-- As in the CQFW document (Abbott, 04:03; std N-0057). label: both; status: drafted; basis: primary. Our words, with the issuer's verbs and short quoted phrases. The FHEQ's five levels; the FQHEIS's are in its own document. -->

#### SL1 What defines each level
<!-- Each level's defining step, in our words, for the practitioner and the learner. -->

| Descriptor and level | For the practitioner | For the learner |
|---|---|---|
| 4.10 CertHE (FHEQ 4) | Knowing the concepts beneath a subject and using basic theory to weigh data and argue soundly; choosing between approaches; learning further where the setting is managed for them. | At this first level, you know the main ideas behind your subject, can use them to weigh up evidence and make a sound case, and keep learning where the course is set out for you. |
| 4.12 foundation degree (FHEQ 5) | Critical understanding of established principles and their history; applying them beyond the setting where they were learned; knowing the limits of one's own knowledge; starting critical analysis oneself. | At this level, you think critically about your field's established ideas, use them in new settings such as work, know where your knowledge stops, and start analysing problems yourself. |
| 4.15 honours degree (FHEQ 6) | Systematic understanding with some knowledge at the forefront; accurate use of established techniques; commenting on current research; appreciating uncertainty and ambiguity; judging with incomplete data and framing the questions that lead to solutions; managing one's own learning from primary sources. | At honours level, you understand your field as a system, with parts of it at the leading edge, use its methods accurately, comment on current research, accept that knowledge is uncertain, and manage your own learning. |
| 4.17 master's (FHEQ 7, SCQF 11) | Much of one's knowledge at or informed by the forefront; originality in applying it; evaluating research and methodologies critically and proposing hypotheses; sound judgement without complete data; autonomy and self-direction at a professional level. | At master's level, much of what you know is at the leading edge; you apply it with originality, critique research and its methods, judge well without all the facts and work on your own at a professional level. |
| 4.18 doctorate (FHEQ 8, SCQF 12) | Creating new knowledge of publishable quality through original research; conceiving, designing and adjusting a project at the forefront; continuing to contribute new techniques and ideas; largely autonomous initiative. | At doctoral level, you create new knowledge through your own research, good enough to be published; you design and steer a project at the leading edge and go on contributing new ideas and methods. |

#### SL2 The level table, by part
<!-- Each cell is our short gloss of the issuer's items at that level and part (the S4 `about` fields). The issuer's strands are its two parts, not knowledge, application and autonomy as in the CQFW. -->

| Descriptor and level | Threshold outcomes | Wider abilities | Qualities for employment |
|---|---|---|---|
| 4.10 CertHE (FHEQ 4) | underlying concepts and their interpretation; handling data to argue and judge | judging approaches to problems; communicating results soundly; further training in a managed setting | qualities for work with some personal responsibility |
| 4.12 foundation degree (FHEQ 5) | critical understanding of established principles; applying principles beyond their first context; methods of enquiry and judging approaches; the limits of one's own knowledge | critical analysis and proposing solutions; communicating to specialist and general audiences; further training towards significant responsibility | qualities for work with responsibility and decisions |
| 4.15 honours degree (FHEQ 6) | systematic understanding reaching the forefront; accurate use of established techniques; arguing and solving problems with forefront ideas; commenting on current research; appreciating uncertainty and limits of knowledge; managing own learning with scholarly and primary sources | applying methods to extend knowledge; projects; critical evaluation and framing questions; communicating to specialist and general audiences | initiative and personal responsibility; decisions in complex, unpredictable contexts; learning ability for professional training |
| 4.17 master's (FHEQ 7, SCQF 11) | systematic understanding; critical awareness at the forefront; comprehensive understanding of research techniques; originality in applying knowledge; how research creates knowledge; critically evaluating current research; critiquing methodologies; proposing hypotheses | complex issues, judgement without complete data; self-direction, originality and autonomy; continuing to advance knowledge and skills | initiative and personal responsibility; decisions in complex, unpredictable situations; independent learning for continuing development |
| 4.18 doctorate (FHEQ 8, SCQF 12) | creating new knowledge of publishable quality; substantial body of knowledge at the forefront; designing and adjusting research projects; detailed understanding of research techniques | judgements on complex issues; communicating to all audiences; continuing advanced research and development | qualities for autonomous work in complex situations |

#### SL3 Verbs by level
<!-- The issuer's own verbs, as given, by part (from the S4 `verbs` fields, first occurrence kept). Threshold outcomes are mostly noun phrases ("knowledge of", "an ability to"), so that column is thin: its progression is in the nouns and qualifiers (SL4). -->

| Descriptor and level | Threshold outcomes | Wider abilities | Qualities for employment |
|---|---|---|---|
| 4.10 CertHE (FHEQ 4) | evaluate, interpret, present, develop, make | evaluate, communicate, undertake, develop |  |
| 4.12 foundation degree (FHEQ 5) | apply, evaluate, solving, influences | use, initiate, undertake, propose, communicate, deploy, develop, acquire, enable, assume |  |
| 4.15 honours degree (FHEQ 6) | informed, deploy, devise, sustain, solve, using, describe, comment, manage, make | apply, learned, review, consolidate, extend, initiate, carry, evaluate, make, frame, achieve, identify, communicate | needed, undertake |
| 4.17 master's (FHEQ 7, SCQF 11) | informed, used, create, interpret, evaluate, develop, propose | deal, make, communicate, demonstrate, tackling, solving, act, planning, implementing, continue, advance, develop | required |
| 4.18 doctorate (FHEQ 8, SCQF 12) | satisfy, extend, merit, conceptualise, design, implement, adjust | make, communicate, continue, undertake, contributing |  |

#### SL4 How progression is communicated
<!-- Each thread follows one quality up the levels: where the wording changes, the level is listed with the new wording (the issuer's words in quotation marks, otherwise our short reading). A level not listed adds nothing new to that thread. -->

- **The knowledge held:** 4.10: "underlying concepts and principles"; 4.12: "knowledge and critical understanding" of "well-established principles"; 4.15: "systematic understanding", "coherent and detailed knowledge"; 4.17: "systematic understanding of knowledge"; 4.18: "a substantial body of knowledge", then "the creation and interpretation of new knowledge".
- **Reach towards the forefront:** 4.15: "at least some" of it at or informed by the forefront; 4.17: "much of which" is at or informed by it; 4.18: "extend the forefront of the discipline".
- **The limits of knowledge:** 4.12: "the limits of their knowledge"; 4.15: "the uncertainty, ambiguity and limits of knowledge"; 4.17: "critical awareness of current problems".
- **The problem:** 4.10: choosing among "different approaches to solving problems"; 4.15: data "(that may be incomplete)"; "frame appropriate questions"; 4.17: "deal with complex issues", "in the absence of complete data"; 4.18: "complex issues in specialist fields".
- **The thinking verbs:** 4.10: evaluate and interpret; 4.12: "evaluate critically", "critical analysis"; 4.15: "critically evaluate arguments, assumptions, abstract concepts and data"; 4.17: "evaluate critically current research", "develop critiques"; 4.18: conceptualise, design, implement, adjust.
- **Research and enquiry:** 4.12: "the main methods of enquiry"; 4.15: "deploy accurately established techniques"; "describe and comment upon" current research; 4.17: "evaluate methodologies", "propose new hypotheses"; 4.18: "original research", good enough "to satisfy peer review".
- **Originality:** 4.17: "originality in the application of knowledge"; "self-direction and originality"; 4.18: "new techniques, ideas or approaches".
- **Communication:** 4.10: "accurately and reliably", in "structured and coherent arguments"; 4.12: "specialist and non-specialist audiences", "in a variety of forms"; 4.17: "clearly"; 4.18: "clearly and effectively".
- **Learning:** 4.10: "within a structured and managed environment"; 4.15: "manage their own learning"; 4.17: "to develop new skills to a high level"; "independent learning ability"; 4.18: "continue to undertake pure and/or applied research".
- **Responsibility and autonomy:** 4.10: "some personal responsibility"; 4.12: "personal responsibility and decision-making"; "significant responsibility within organisations"; 4.15: "decision-making in complex and unpredictable contexts"; 4.17: "act autonomously"; 4.18: "largely autonomous initiative".

#### SL5 Observations on the formulation
<!-- label: editorial; status: drafted; basis: primary -->
- **Two parts, two forces.** Each descriptor separates what must have been shown for the award (the threshold, 4.2) from what a typical holder can also do (4.3). The CQFW has one register for all; here the threshold list is the standard and the second part is expectation. A progression model can borrow the split: what you must show, and what you will usually be able to do.
- **Nouns, not imperatives.** The threshold items are noun phrases ("knowledge of", "an understanding of", "an ability to") completing one lead. The level lives in the noun's qualifier: outline, detailed, broad and comparative, systematic, systematic and extensive, substantial; and in what is done: knowing, understanding critically, appreciating limits, creating.
- **The forefront is the spine.** From honours up, each level states how much of the student's knowledge reaches the forefront: "at least some" (honours), "much" (master's), then extending it (doctorate). It is the one quality the descriptors grade in quantity.
- **Uncertainty is graded.** The limits of one's knowledge (foundation degree), uncertainty and ambiguity (honours), current problems and new insights (master's).
- **Data become incomplete.** Routine information in a clearly defined context at the bottom; data "that may be incomplete" at honours; judgement "in the absence of complete data" at master's and doctorate.
- **Originality arrives late and in stages.** Not asked at Levels 4 to 6; originality in applying knowledge (master's), then new knowledge (doctorate).
- **The employment ladder repeats the CQFW's.** Personal responsibility (some, limited, plain), then initiative and decision-making, then complex and unpredictable contexts, then autonomy. The two frameworks share this strand almost word for word.
- **Against the FQHEIS.** The Scottish framework has six levels to the FHEQ's five, with steps the FHEQ lacks (DipHE, non-honours bachelor's) and fuller wording below honours; at master's and doctorate the two share this document's text (std:doc:qaa-fqheis-2024-framework, SL5).
- **Against the CQFW (first look; the full comparison is the second layer, std N-0058).** The CQFW grades by context (how defined the problem is) and by autonomy; the FHEQ grades by knowledge (how deep, how near the forefront, how certain) and by what the student does with research. A pathway that wants both can take its knowledge rungs from the FHEQ and its context and autonomy rungs from the CQFW.

#### SL6 The classification bands (Annex D)
<!-- How the four classes and the not-successful column are told apart: our reading, with a count of the issuer's degree words per band across all 104 cells (the issuer's single words, counted from the held text). -->

| Band | What marks it | Degree words, counted |
|---|---|---|
| Not successful | Absence and inconsistency: outcomes not achieved; the skill is "not" shown, "little or no", "inadequate", or not "consistently". | not 12, consistently 5, little 4, inadequate 2, limited 2, lack 1, weak 1, critically 1 |
| Third-class honours (3rd, pass or threshold) | Presence: the skill is shown, mostly with no qualifier at all; "some" and "general" where one is used. All course outcomes achieved: the threshold. | some 3, general 1 |
| Lower second-class honours (2.2) | Consistency: the commonest qualifier by far; "strong" and "sound" for quality; at times going past the set range. | consistently 14, strong 3, well-developed 2, sound 1, critical 1, critically 1, independently 1, beyond 1 |
| Upper second-class honours (2.1) | Thoroughness and criticality: "thorough", "critically", "wide"; first autonomy in decisions; going past the set range usually. | thorough 8, critically 5, wide 4, high 3, strong 2, well-developed 2, sound 1, good 1, consistently 1, thoroughly 1, sophisticated 1, critical 1, autonomously 1, autonomy 1, beyond 1, perceptively 1, originality 1 |
| First-class honours (1st) | Exception and independence: "exceptional" dominates; "beyond" the threshold and the taught; independence, autonomy, originality, flair. | exceptional 12, consistently 4, wide 4, critically 3, beyond 3, sophisticated 2, critical 2, independently 2, accomplished 2, high 2, not 1, strong 1, well-developed 1, advanced 1, independent 1, autonomously 1, autonomy 1, perceptively 1, extensive 1, innovative 1, originality 1, flair 1 |

#### SL7 The Dublin step changes (Annex B)
<!-- The annex's own comparison of the cycles, element by element (the Joint Quality Initiative's), in our short reading with the issuer's words in quotation marks a few at a time. -->

- **Knowledge and understanding:** short cycle: at the level of "advanced textbooks"; first: some of it "informed by knowledge at the forefront"; second: a "basis or opportunity for originality", often in research; doctorate: "systematic understanding" and "mastery of the methods of research".
- **Applying knowledge:** short cycle: in "occupational context"; first: by "devising and sustaining arguments"; second: problem-solving in "new or unfamiliar environments"; doctorate: a "substantial process of research" that "extends the frontier of knowledge".
- **Making judgements:** short cycle: data for "well-defined concrete and abstract problems"; first: "gathering and interpreting relevant data"; second: "handle complexity", judging "with incomplete data"; doctorate: "critical analysis, evaluation and synthesis".
- **Communication:** short cycle: with "peers, supervisors and clients"; first: "information, ideas, problems and solutions"; second: conclusions and their rationale to "specialist and non-specialist audiences"; doctorate: with peers, scholars and "society in general".
- **Learning skills:** short cycle: "with some autonomy"; first: "a high level of autonomy"; second: "largely self-directed or autonomous"; doctorate: promoting "technological, social or cultural advancement".

#### SL8 Observations on stage 2
<!-- label: editorial; status: drafted; basis: primary -->
- **Annex D is a marking scale for one level.** It holds the honours threshold (3rd) fixed and grades upwards by a small ladder of qualifiers, the same in every strand: shown, then consistently, then thoroughly and critically, then exceptionally and independently. It is the pattern Bristol's and Cardiff Met's criteria follow within each level (the assessment-criteria variant, next).
- **The third is the threshold.** The annex says so ("3rd (pass or threshold)"), and the 3rd column's wording is the descriptor's wording almost unqualified. A pathway's pass statement and an honours descriptor are the same thing said twice.
- **Failure is described as absence or inconsistency, not as a lower level.** "Did not consistently demonstrate" is the summary's failure form: the same skill, shown unreliably.
- **The Dublin descriptors climb by autonomy and by reach.** Their learning-skills line is the clearest single progression in the document: "some autonomy", "a high level", "largely self-directed", then promoting advancement in society.
- **The provider statements are mostly present-tense rules** ("degree-awarding bodies ensure"), not "must"; their force is inferred as `must` where the sentence states a condition of award or title (`forceBasis: inferred`).

## Part B Terminology
<!-- label: both; status: drafted; basis: primary. The document's Definitions, glossed in our words. -->
```yaml
- { term: "Compensation", gloss: "credit for a module failed by a small margin, usually on the strength of good overall performance", locator: "Definitions", basis: paraphrase }
- { term: "Condonement", gloss: "allowing a student to fail one or more modules, without credit, and still receive the degree", locator: "Definitions", basis: paraphrase }
- { term: "Course (of study)", gloss: "an approved, coherent course that normally leads to a qualification; research programmes included", locator: "Definitions", basis: paraphrase }
- { term: "Course learning outcomes", gloss: "what a learner is expected to know, understand or do on completing a course; holistic, not the sum of module outcomes", locator: "Definitions", basis: paraphrase }
- { term: "Credit", gloss: "a measure of learning, awarded for achieving outcomes at a stated level", locator: "Definitions", basis: paraphrase }
- { term: "Cycles", gloss: "the Bologna process's sequential levels (short, first, second, third) in which European higher education qualifications sit", locator: "Definitions", basis: paraphrase }
- { term: "Degree-awarding body", gloss: "an institution holding degree-awarding powers by one of the routes the definition lists", locator: "Definitions", basis: paraphrase }
- { term: "Exit qualification", gloss: "an award made when a student leaves a longer course part way, not registered for at the outset", locator: "Definitions", basis: paraphrase }
- { term: "Framework levels", gloss: "stages of similar attainment, in sequence, against which institutions place their qualifications", locator: "Definitions", basis: paraphrase }
- { term: "Intermediate qualification", gloss: "a separate award available part way through a longer course, which a student can register for at the outset", locator: "Definitions", basis: paraphrase }
- { term: "Level descriptor", gloss: "a statement of the generic characteristics of learning outcomes at one level of a framework, used as a reference point", locator: "Definitions", basis: paraphrase }
- { term: "Qualification", gloss: "a degree, diploma or certificate that a competent authority awards; here, a degree-awarding body", locator: "Definitions", basis: paraphrase }
- { term: "Abbreviations", gloss: "CQFW, EQF, FHEQ, FQHEIS, OfS, PSRBs and QF-EHEA are expanded in the Definitions; recorded in S1, S5 and S7 where used", locator: "Definitions", basis: paraphrase }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`described`: section 6 sets out what degree-awarding bodies do; the steps are its, the order ours.

### C1 Steps
```yaml
- { step: 1, name: position the qualification, does: "set its framework level by the level most of its outcomes match (6.1)", statements: [6.1.a, 6.1.b] }
- { step: 2, name: approve the course, does: "course approval checks the threshold standard and the awarding body's own standards (6.2); design and review weigh alignment, volume, opportunity and PSRB requirements (6.3)", statements: [6.3.b1, 6.3.b2, 6.3.b3, 6.3.b4] }
- { step: 3, name: assess, does: "judge performance against the standards set (6.5)", statements: [6.5] }
- { step: 4, name: award, does: "award only when outcomes are shown in full; fall-back awards only on their own outcomes; compensation and condonement never replace achievement (6.4, 6.6, 6.7)", statements: [6.4, 6.6, 6.6.b1, 6.6.b2, 6.7.b1, 6.7.b2, 6.7.b3] }
- { step: 5, name: classify (honours), does: "place the honours award in a class by Annex D (2.8)", statements: ["annex-d/*"] }
- { step: 6, name: title, does: "title the award by level, volume, nature and field (6.8 to 6.19)", statements: [6.9, 6.10.b1, 6.10.b2, 6.10.b3, 6.11.a, 6.11.b, 6.13.b2, 6.13.b3, 6.14.b1, 6.14.b2, 6.14.b3, 6.14.b4, 6.14.b5, 6.15, 6.16, 6.17, 6.18.b1, 6.18.b2, 6.19] }
- { step: 7, name: record, does: "give the student a record of study: transcript, Diploma Supplement or HEAR (5.7)", statements: [] }
```

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
  citedIn: [S1, S2, S3, S4, S4a, S5, S7, SL, B, C]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "stage 1: section 4 read whole; 2.23 to 2.26, 3.1 to 3.7, 4.1 to 4.9 read for S1, S2, S5 and S7; text by pdftotext, normalised with stan's tool" }
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "stage 2: the whole document read; Annex D cut by table cell from the held text, its row and column order checked against the page images (PDF pages 47, 53); Table 1 and Annex C read from the page images (PDF pages 14, 43 to 45) and checked against pdftotext layout mode; the PDF from Abbott's upload, byte hash matching index.json" }
```

### D3 Wanted sources
```yaml
- { w: W-std-0017, citation: "QAA's web page for this edition: its licence and re-use terms, and whether a later edition exists", settles: [S1, S8], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- Stage 2 read Table 1 and Annex C from the page images; their values are ours to check at P3 against the PDF.
- One document per framework (D-std-0010, Abbott, 05:20): the FQHEIS's four own descriptors moved to std:doc:qaa-fqheis-2024-framework with their statements, now `qaa/fqheis-2024/...`. The shared master's and doctoral descriptors and the common material stay here once, so that nothing is held twice; the FQHEIS document links to them.
- S3, the cut: the descriptors have no knowledge, application and autonomy headings; profile framework rule 3 is applied as one record per list item, the issuer's own unit. Stems (5) are components; their sub-items carry the stem's id.
- S4, force: `threshold` for the outcomes demonstrated (4.2 names them the threshold standard); `will` for the typical holder's abilities and qualities (4.3). The issuer says "Typically, holders ... will be able to", so the force is an expectation of the typical, not a condition.
- 4.8, an issuer slip: it names the shared Level 7/SCQF 11 descriptor as for "bachelor's degrees" and the shared Level 8/SCQF 12 one as for "master's degrees"; the headings of 4.17 and 4.18 show these are the master's and the doctoral descriptors. Recorded by the headings.
- S5, Table 1 and Annex C disagree in three places: foundation degrees are SCQF "NA" in Table 1 but 8 in Annex C; the Professional Graduate PGCE is SCQF 9 in Table 1 but "NA" in Annex C; graduate diplomas and certificates are SCQF 9 in both but SCQF 10 in 6.13. Recorded as each table gives them; for QAA (D3).
- S5, Annex C: the Scottish integrated master's "600c" carries note c (ECTS), probably meant for note d (a year longer); the Welsh HNC row reads "150 (30 at FHEQ Level 5 ...)" where England's reads "120 at FHEQ Level 4". Both recorded as printed.
- S5: equivalence is by qualification, not by level: FHEQ 6 sits beside SCQF 10 (honours) and SCQF 9 (other bachelor's and graduate awards); the short cycle spans FHEQ 5 and SCQF 8. The CQFW and RQF comparison (2.24) is "compare with", and 2.25 warns that the cross-UK guide gives comparisons, "rather than direct equivalences": recorded as `compares-with`, not `equals`.
- S1: the licence is not yet read (the back page gives only the copyright line); status is taken as current from the held text alone (D3).
- ST-12: versions run short and close to the issuer's formulaic wording; 13 nine-word copies were found and reworded in stage 1, 32 checker findings in stage 2 (10 copies, 22 student versions not in the second person or naming a framework), all fixed.
- Annex D, the not-successful column: no student version (24 cells); a "what is missing" version for students may be wanted (P3).
- Annex D: issuer slips kept as held: "The student has some produced creative work" (cognitive, 3rd); "problemsolving", "subjectspecific", "disciplinespecific" (PDF line breaks).
- Annex D, grid cells: the S4 paraphrase is the practitioner version (one wording, not two), the cells being short single judgements.
- Annex B: the short-cycle lead says "(within the first cycle)"; Table 1 says "within or linked to the first cycle".
- Provider statements: present-tense rules ("degree-awarding bodies ensure") carry force `must` or `should` with `forceBasis: inferred`; "must", "required", "only" are `stated`.
- Annex A (the 2014 advisory group) is excluded: names only.

---

## Change notes
- 0.4.1, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.4.0, 3 October 2026, 11:00: every statement record now carries the issuer's statement in full (`source`, taken from its span in the held text) beside our paraphrase and versions, for language analysis; private, never published (Abbott, 10:56 and 10:59; D-std-0014). No paraphrase changed.
- 0.3.1, 3 October 2026, 07:34: provenance lines added to Parts B and C; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.3.0: 2026-10-03, 05:24: the FQHEIS split out (D-std-0010): its descriptors 4.11, 4.13, 4.14 and 4.16 (37 statements) and their level language moved to std:doc:qaa-fqheis-2024-framework; this document is the FHEQ and the material common to both.
- 0.2.0: 2026-10-03: stage 2: 181 records added (56 provider statements, 21 Dublin descriptors, 104 Annex D cells), Table 1 crosswalk and Annex C credit in S5, SL6 to SL8, Part B and Part C; std, run 0047 (P1).
- 0.1.0: 2026-10-03: stage 1 researched by run frame 0.1.1-draft and standards run layer 0.5.0-draft, std, run 0047 (P1).
