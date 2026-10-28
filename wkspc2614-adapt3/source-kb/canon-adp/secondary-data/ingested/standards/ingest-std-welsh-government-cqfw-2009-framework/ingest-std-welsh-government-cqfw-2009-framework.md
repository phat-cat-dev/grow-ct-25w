---
id: std:doc:welsh-government-cqfw-2009-framework
title: Level Descriptors
profile: standards/framework
profileVersion: 0.1.5-draft
issuer: Welsh Government (CQFW), as Abbott identifies it; the document itself names no issuer
kind: qualification-framework
jurisdiction: [Wales]
subjectScope: universal
subjects: []
edition: January 2009
published: 2009-01
status: unknown
supersedes: none
heldText: { method: sha256-bytes, raw: 3eda4e2cec5e9c8b11d5238db7885f013de6a0013daaada1b87d85cd402ee94d, normalised: e75269782dddfa64858be95d49a6a00e70a676162665980c6d9e641b80752c16 }
original: { method: sha256-bytes, pdf: 98e069d687e31ea74e8916aa2f3dfe9fa2436e1928638e595bcb76ba998a0a31, held: no }   # supplied files stay out of UNI (nts N-1020)
frameworkKind: level-descriptors
nations: [Wales]
levels: [cqfw:entry-1, cqfw:entry-2, cqfw:entry-3, cqfw:1, cqfw:2, cqfw:3, cqfw:4, cqfw:5, cqfw:6, cqfw:7, cqfw:8]   # no cross-framework equivalents stated in this document
awards: none-stated
credit: none-stated
licence: none stated in the document (Part E)
parts:
  S: full
  B: "not-applicable: the document defines no terms"
  C: "not-applicable: the document sets out levels, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.5.0-draft, runFrame: 0.1.1-draft, runLayer: 0.5.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0045
passes:
  P1: 2026-10-03, std (claude.ai, META Project)
  P2: "skipped: the text was read direct from the PDF; the issuer's identity rests on Abbott's word (Part E)"
  P3: open
version: 0.2.1
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.5.0-draft under the standards/framework variant (profile 0.1.5-draft; its template is to write), with the level-language section SL proposed for it (Abbott, 04:03; std N-0057) -->
# CQFW Level Descriptors (January 2009)

> Run 0045, P1 by std. The issuer's words are held in the source library repo only (`wkspc2601-library/txt/welsh-government-2009-cqfw-level-descriptors-standard.norm.txt`, extracted from the PDF table by table cell); every statement points into them by character span. Everything else is our words; in the level-language section, words in quotation marks are the issuer's, a few at a time. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The Credit and Qualifications Framework for Wales' generic level descriptors, from Entry 1 to Level 8, each described for knowledge and understanding, application and action, and autonomy and accountability. Reach for it to say what achievement at a level looks like in any subject or setting, or to write level-based progression. It is not a subject standard, a qualification descriptor or a credit specification.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
A short table, dated January 2009, describing eleven levels of achievement (Entry 1 to 3, then Levels 1 to 8) in a summary and three strands: knowledge and understanding; application and action; autonomy and accountability. Each strand is a few short imperative sentences ("Use...", "Address...", "Take responsibility..."). The levels climb by changing a small set of qualifiers: how defined and complex the problem is, what kind of knowledge is drawn on, what is done with it, how methods are chosen, how far enquiry and evaluation reach, and how much responsibility and autonomy the learner holds. The document names no issuer; Abbott identifies it as CQFW's.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: "unknown in the document; Abbott: CQFW's (Credit and Qualifications Framework for Wales, managed by the Welsh Government, as the Frameworks 2024 says at 2.23); PDF metadata author: Evans, Emma-Jane (DfES - QLD)"
title: Level Descriptors
edition: January 2009
dates:
  published: 2009-01
  other: []
kind: qualification-framework
jurisdiction: [Wales]
authority: reference   # the document states none; inferred from its use as CQFW's level descriptors (Part E)
licence: none stated
copyrightNotice: none-stated
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: generic descriptions of achievement at eleven levels, Entry 1 to Level 8, in a summary and three strands (D1, the table)
appliesTo:
  awards: none-stated
  levels: [cqfw:entry-1, cqfw:entry-2, cqfw:entry-3, cqfw:1, cqfw:2, cqfw:3, cqfw:4, cqfw:5, cqfw:6, cqfw:7, cqfw:8]
  providers: none-stated
whoMustUse: none-stated
howUsed: [other: none stated in the document]
doesNot: none-stated
beneficiary: the learner
statedScope: none-stated   # the document is the table alone, with no introduction
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary. The issuer's own structure: levels in rows, the summary and three strands in columns; no numbering beyond the level names. Statement ids are level/strand.sentence in the issuer's order. -->
```yaml
components:
  - { number: "entry-1/summary", componentType: level, parent: "entry-1", heading: "Entry 1, Summary" }
  - { number: "entry-2/summary", componentType: level, parent: "entry-2", heading: "Entry 2, Summary" }
  - { number: "entry-2/knowledge", componentType: descriptor, parent: "entry-2", heading: "Entry 2, Knowledge and understanding" }
  - { number: "entry-2/application", componentType: descriptor, parent: "entry-2", heading: "Entry 2, Application and action" }
  - { number: "entry-2/autonomy", componentType: descriptor, parent: "entry-2", heading: "Entry 2, Autonomy and accountability" }
  - { number: "entry-3/summary", componentType: level, parent: "entry-3", heading: "Entry 3, Summary" }
  - { number: "entry-3/knowledge", componentType: descriptor, parent: "entry-3", heading: "Entry 3, Knowledge and understanding" }
  - { number: "entry-3/application", componentType: descriptor, parent: "entry-3", heading: "Entry 3, Application and action" }
  - { number: "entry-3/autonomy", componentType: descriptor, parent: "entry-3", heading: "Entry 3, Autonomy and accountability" }
  - { number: "l1/summary", componentType: level, parent: "l1", heading: "Level 1, Summary" }
  - { number: "l1/knowledge", componentType: descriptor, parent: "l1", heading: "Level 1, Knowledge and understanding" }
  - { number: "l1/application", componentType: descriptor, parent: "l1", heading: "Level 1, Application and action" }
  - { number: "l1/autonomy", componentType: descriptor, parent: "l1", heading: "Level 1, Autonomy and accountability" }
  - { number: "l2/summary", componentType: level, parent: "l2", heading: "Level 2, Summary" }
  - { number: "l2/knowledge", componentType: descriptor, parent: "l2", heading: "Level 2, Knowledge and understanding" }
  - { number: "l2/application", componentType: descriptor, parent: "l2", heading: "Level 2, Application and action" }
  - { number: "l2/autonomy", componentType: descriptor, parent: "l2", heading: "Level 2, Autonomy and accountability" }
  - { number: "l3/summary", componentType: level, parent: "l3", heading: "Level 3, Summary" }
  - { number: "l3/knowledge", componentType: descriptor, parent: "l3", heading: "Level 3, Knowledge and understanding" }
  - { number: "l3/application", componentType: descriptor, parent: "l3", heading: "Level 3, Application and action" }
  - { number: "l3/autonomy", componentType: descriptor, parent: "l3", heading: "Level 3, Autonomy and accountability" }
  - { number: "l4/summary", componentType: level, parent: "l4", heading: "Level 4, Summary" }
  - { number: "l4/knowledge", componentType: descriptor, parent: "l4", heading: "Level 4, Knowledge and understanding" }
  - { number: "l4/application", componentType: descriptor, parent: "l4", heading: "Level 4, Application and action" }
  - { number: "l4/autonomy", componentType: descriptor, parent: "l4", heading: "Level 4, Autonomy and accountability" }
  - { number: "l5/summary", componentType: level, parent: "l5", heading: "Level 5, Summary" }
  - { number: "l5/knowledge", componentType: descriptor, parent: "l5", heading: "Level 5, Knowledge and understanding" }
  - { number: "l5/application", componentType: descriptor, parent: "l5", heading: "Level 5, Application and action" }
  - { number: "l5/autonomy", componentType: descriptor, parent: "l5", heading: "Level 5, Autonomy and accountability" }
  - { number: "l6/summary", componentType: level, parent: "l6", heading: "Level 6, Summary" }
  - { number: "l6/knowledge", componentType: descriptor, parent: "l6", heading: "Level 6, Knowledge and understanding" }
  - { number: "l6/application", componentType: descriptor, parent: "l6", heading: "Level 6, Application and action" }
  - { number: "l6/autonomy", componentType: descriptor, parent: "l6", heading: "Level 6, Autonomy and accountability" }
  - { number: "l7/summary", componentType: level, parent: "l7", heading: "Level 7, Summary" }
  - { number: "l7/knowledge", componentType: descriptor, parent: "l7", heading: "Level 7, Knowledge and understanding" }
  - { number: "l7/application", componentType: descriptor, parent: "l7", heading: "Level 7, Application and action" }
  - { number: "l7/autonomy", componentType: descriptor, parent: "l7", heading: "Level 7, Autonomy and accountability" }
  - { number: "l8/summary", componentType: level, parent: "l8", heading: "Level 8, Summary" }
  - { number: "l8/knowledge", componentType: descriptor, parent: "l8", heading: "Level 8, Knowledge and understanding" }
  - { number: "l8/application", componentType: descriptor, parent: "l8", heading: "Level 8, Application and action" }
  - { number: "l8/autonomy", componentType: descriptor, parent: "l8", heading: "Level 8, Autonomy and accountability" }
excluded:
  - { number: none, heading: "the repeated table header on each page", kind: "other: page furniture" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. 94 descriptor sentences, one record each; the level summaries are in SL1. Force `describes`: level descriptors state what achievement at a level reflects, without obliging. -->
```yaml
- id: welsh-government/cqfw-2009/entry-2/knowledge.1
  locator: { number: "entry-2/knowledge.1", headingPath: ["Entry 2", "Knowledge and understanding"] }
  span: { start: 461, end: 533 }
  source: "Use knowledge or understanding to carry out simple, familiar activities."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-2
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Entry 2"
  addressee: learner
  verbs: [Use, carry]
  about: "using what one knows on simple tasks"
  themes: [none]
  paraphrase: "Apply what is known or understood to simple, familiar activities."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-2/knowledge.2
  locator: { number: "entry-2/knowledge.2", headingPath: ["Entry 2", "Knowledge and understanding"] }
  span: { start: 534, end: 586 }
  source: "Know the steps needed to complete simple activities."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-2
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Entry 2"
  addressee: learner
  verbs: [Know, complete]
  about: "knowing the steps"
  themes: [none]
  paraphrase: "Know the sequence of steps a simple activity needs."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-2/application.1
  locator: { number: "entry-2/application.1", headingPath: ["Entry 2", "Application and action"] }
  span: { start: 610, end: 658 }
  source: "Carry out simple, familiar tasks and activities."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-2
  dimension: application-and-action
  appliesTo: "achievement at Entry 2"
  addressee: learner
  verbs: [Carry]
  about: "doing simple, familiar tasks"
  themes: [none]
  paraphrase: "Do simple tasks and activities that are already familiar."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-2/application.2
  locator: { number: "entry-2/application.2", headingPath: ["Entry 2", "Application and action"] }
  span: { start: 659, end: 735 }
  source: "Follow instructions or use rehearsed steps to complete tasks and activities."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-2
  dimension: application-and-action
  appliesTo: "achievement at Entry 2"
  addressee: learner
  verbs: [Follow, use, complete]
  about: "following instructions and practised steps"
  themes: [none]
  paraphrase: "Complete tasks by following instructions or steps already practised."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-2/autonomy.1
  locator: { number: "entry-2/autonomy.1", headingPath: ["Entry 2", "Autonomy and accountability"] }
  span: { start: 764, end: 862 }
  source: "With appropriate guidance begin to take some responsibility for the outcomes of simple activities."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-2
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Entry 2"
  addressee: learner
  verbs: [begin, take]
  about: "first responsibility, with guidance"
  themes: [none]
  paraphrase: "With suitable guidance, start to take some responsibility for how simple activities turn out."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-2/autonomy.2
  locator: { number: "entry-2/autonomy.2", headingPath: ["Entry 2", "Autonomy and accountability"] }
  span: { start: 863, end: 918 }
  source: "Actively participate in simple and familiar activities."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-2
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Entry 2"
  addressee: learner
  verbs: [participate]
  about: "active participation"
  themes: [none]
  paraphrase: "Take an active part in simple, familiar activities."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-3/knowledge.1
  locator: { number: "entry-3/knowledge.1", headingPath: ["Entry 3", "Knowledge and understanding"] }
  span: { start: 1184, end: 1281 }
  source: "Use knowledge or understanding to carry out structured tasks and activities in familiar contexts."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-3
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Entry 3"
  addressee: learner
  verbs: [Use, carry]
  about: "using what one knows on structured tasks in familiar settings"
  themes: [none]
  paraphrase: "Apply what is known or understood to structured tasks and activities in familiar settings."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-3/knowledge.2
  locator: { number: "entry-3/knowledge.2", headingPath: ["Entry 3", "Knowledge and understanding"] }
  span: { start: 1282, end: 1384 }
  source: "Know and understand the steps needed to complete structured tasks and activities in familiar contexts."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-3
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Entry 3"
  addressee: learner
  verbs: [Know, understand, complete]
  about: "knowing and understanding the steps"
  themes: [none]
  paraphrase: "Know and understand the steps that structured tasks in familiar settings need."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-3/application.1
  locator: { number: "entry-3/application.1", headingPath: ["Entry 3", "Application and action"] }
  span: { start: 1408, end: 1471 }
  source: "Carry out structured tasks and activities in familiar contexts."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-3
  dimension: application-and-action
  appliesTo: "achievement at Entry 3"
  addressee: learner
  verbs: [Carry]
  about: "doing structured tasks in familiar settings"
  themes: [none]
  paraphrase: "Do structured tasks and activities in familiar settings."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-3/application.2
  locator: { number: "entry-3/application.2", headingPath: ["Entry 3", "Application and action"] }
  span: { start: 1472, end: 1532 }
  source: "Be aware of the consequences of actions for self and others."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-3
  dimension: application-and-action
  appliesTo: "achievement at Entry 3"
  addressee: learner
  verbs: [Be]
  about: "awareness of consequences"
  themes: [none]
  paraphrase: "Know that actions have consequences for oneself and others."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-3/autonomy.1
  locator: { number: "entry-3/autonomy.1", headingPath: ["Entry 3", "Autonomy and accountability"] }
  span: { start: 1561, end: 1649 }
  source: "With appropriate guidance take responsibility for the outcomes of structured activities."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-3
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Entry 3"
  addressee: learner
  verbs: [take]
  about: "responsibility for outcomes, with guidance"
  themes: [none]
  paraphrase: "With suitable guidance, take responsibility for how structured activities turn out."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/entry-3/autonomy.2
  locator: { number: "entry-3/autonomy.2", headingPath: ["Entry 3", "Autonomy and accountability"] }
  span: { start: 1650, end: 1706 }
  source: "Actively participate in activities in familiar contexts."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:entry-3
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Entry 3"
  addressee: learner
  verbs: [participate]
  about: "active participation in familiar settings"
  themes: [none]
  paraphrase: "Take an active part in activities in familiar settings."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l1/knowledge.1
  locator: { number: "l1/knowledge.1", headingPath: ["Level 1", "Knowledge and understanding"] }
  span: { start: 1969, end: 2054 }
  source: "Use knowledge of facts, procedures and ideas to complete well-defined, routine tasks."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:1
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 1"
  addressee: learner
  verbs: [Use, complete]
  about: "facts, procedures and ideas for routine tasks"
  themes: [none]
  paraphrase: "Draw on facts, procedures and ideas to finish routine, clearly set tasks."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l1/knowledge.2
  locator: { number: "l1/knowledge.2", headingPath: ["Level 1", "Knowledge and understanding"] }
  span: { start: 2055, end: 2117 }
  source: "Be aware of information relevant to the area of study or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:1
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 1"
  addressee: learner
  verbs: [Be]
  about: "awareness of relevant information"
  themes: [none]
  paraphrase: "Know which information bears on the area of study or work."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l1/application.1
  locator: { number: "l1/application.1", headingPath: ["Level 1", "Application and action"] }
  span: { start: 2141, end: 2178 }
  source: "Complete well defined, routine tasks."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:1
  dimension: application-and-action
  appliesTo: "achievement at Level 1"
  addressee: learner
  verbs: [Complete]
  about: "completing routine tasks"
  themes: [none]
  paraphrase: "Finish routine tasks that are clearly defined."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l1/application.2
  locator: { number: "l1/application.2", headingPath: ["Level 1", "Application and action"] }
  span: { start: 2179, end: 2214 }
  source: "Use relevant skills and procedures."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:1
  dimension: application-and-action
  appliesTo: "achievement at Level 1"
  addressee: learner
  verbs: [Use]
  about: "using relevant skills and procedures"
  themes: [none]
  paraphrase: "Apply the skills and procedures that fit the task."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l1/application.3
  locator: { number: "l1/application.3", headingPath: ["Level 1", "Application and action"] }
  span: { start: 2215, end: 2251 }
  source: "Select and use relevant information."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:1
  dimension: application-and-action
  appliesTo: "achievement at Level 1"
  addressee: learner
  verbs: [Select, use]
  about: "choosing and using information"
  themes: [none]
  paraphrase: "Choose and use information that fits the task."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l1/application.4
  locator: { number: "l1/application.4", headingPath: ["Level 1", "Application and action"] }
  span: { start: 2252, end: 2297 }
  source: "Identify whether actions have been effective."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:1
  dimension: application-and-action
  appliesTo: "achievement at Level 1"
  addressee: learner
  verbs: [Identify]
  about: "checking whether actions worked"
  themes: [none]
  paraphrase: "Tell whether actions have worked."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l1/autonomy.1
  locator: { number: "l1/autonomy.1", headingPath: ["Level 1", "Autonomy and accountability"] }
  span: { start: 2326, end: 2425 }
  source: "Take responsibility for completing tasks and procedures subject to direction or guidance as needed."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:1
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 1"
  addressee: learner
  verbs: [Take, completing]
  about: "responsibility under direction"
  themes: [none]
  paraphrase: "Take responsibility for finishing tasks and procedures, under direction or guidance where needed."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l2/knowledge.1
  locator: { number: "l2/knowledge.1", headingPath: ["Level 2", "Knowledge and understanding"] }
  span: { start: 2801, end: 2919 }
  source: "Use understanding of facts, procedures and ideas to complete well- defined tasks and address straightforward problems."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:2
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 2"
  addressee: learner
  verbs: [Use, complete, address]
  about: "understanding for defined tasks and simple problems"
  themes: [none]
  paraphrase: "Draw on an understanding of facts, procedures and ideas to finish defined tasks and deal with straightforward problems."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l2/knowledge.2
  locator: { number: "l2/knowledge.2", headingPath: ["Level 2", "Knowledge and understanding"] }
  span: { start: 2920, end: 2961 }
  source: "Interpret relevant information and ideas."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:2
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 2"
  addressee: learner
  verbs: [Interpret]
  about: "interpreting information and ideas"
  themes: [none]
  paraphrase: "Make sense of the information and ideas that bear on the task."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l2/knowledge.3
  locator: { number: "l2/knowledge.3", headingPath: ["Level 2", "Knowledge and understanding"] }
  span: { start: 2962, end: 3046 }
  source: "Be aware of the types of information that are relevant to the area of study or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:2
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 2"
  addressee: learner
  verbs: [Be]
  about: "awareness of kinds of relevant information"
  themes: [none]
  paraphrase: "Know what kinds of information bear on the area of study or work."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l2/application.1
  locator: { number: "l2/application.1", headingPath: ["Level 2", "Application and action"] }
  span: { start: 3070, end: 3154 }
  source: "Complete well-defined, generally routine tasks and address straightforward problems."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:2
  dimension: application-and-action
  appliesTo: "achievement at Level 2"
  addressee: learner
  verbs: [Complete, address]
  about: "mostly routine tasks and straightforward problems"
  themes: [none]
  paraphrase: "Finish defined tasks that are mostly routine and deal with straightforward problems."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l2/application.2
  locator: { number: "l2/application.2", headingPath: ["Level 2", "Application and action"] }
  span: { start: 3155, end: 3201 }
  source: "Select and use relevant skills and procedures."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:2
  dimension: application-and-action
  appliesTo: "achievement at Level 2"
  addressee: learner
  verbs: [Select, use]
  about: "choosing skills and procedures"
  themes: [none]
  paraphrase: "Choose and use the skills and procedures that fit."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l2/application.3
  locator: { number: "l2/application.3", headingPath: ["Level 2", "Application and action"] }
  span: { start: 3202, end: 3266 }
  source: "Identify, gather and use relevant information to inform actions."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:2
  dimension: application-and-action
  appliesTo: "achievement at Level 2"
  addressee: learner
  verbs: [Identify, gather, use, inform]
  about: "gathering information to guide action"
  themes: [none]
  paraphrase: "Find, collect and use relevant information to guide what is done."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l2/application.4
  locator: { number: "l2/application.4", headingPath: ["Level 2", "Application and action"] }
  span: { start: 3267, end: 3308 }
  source: "Identify how effective actions have been."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:2
  dimension: application-and-action
  appliesTo: "achievement at Level 2"
  addressee: learner
  verbs: [Identify]
  about: "judging how well actions worked"
  themes: [none]
  paraphrase: "Judge how well actions have worked."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l2/autonomy.1
  locator: { number: "l2/autonomy.1", headingPath: ["Level 2", "Autonomy and accountability"] }
  span: { start: 3337, end: 3393 }
  source: "Take responsibility for completing tasks and procedures."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:2
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 2"
  addressee: learner
  verbs: [Take, completing]
  about: "responsibility for completing tasks"
  themes: [none]
  paraphrase: "Take responsibility for finishing tasks and procedures."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l2/autonomy.2
  locator: { number: "l2/autonomy.2", headingPath: ["Level 2", "Autonomy and accountability"] }
  span: { start: 3394, end: 3467 }
  source: "Exercise autonomy and judgement subject to overall direction or guidance."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:2
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 2"
  addressee: learner
  verbs: [Exercise]
  about: "some autonomy under overall direction"
  themes: [none]
  paraphrase: "Use some independence and judgement within overall direction or guidance."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l3/knowledge.1
  locator: { number: "l3/knowledge.1", headingPath: ["Level 3", "Knowledge and understanding"] }
  span: { start: 3972, end: 4121 }
  source: "Use factual, procedural and theoretical understanding to complete tasks and address problems that, while well defined may be complex and non-routine."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:3
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 3"
  addressee: learner
  verbs: [Use, complete, address]
  about: "theoretical understanding for complex, non-routine problems"
  themes: [none]
  paraphrase: "Draw on factual, procedural and theoretical understanding to finish tasks and deal with problems that are defined but may be complex and non-routine."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l3/knowledge.2
  locator: { number: "l3/knowledge.2", headingPath: ["Level 3", "Knowledge and understanding"] }
  span: { start: 4122, end: 4176 }
  source: "Interpret and evaluate relevant information and ideas."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:3
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 3"
  addressee: learner
  verbs: [Interpret, evaluate]
  about: "interpreting and evaluating"
  themes: [none]
  paraphrase: "Make sense of and weigh up relevant information and ideas."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l3/knowledge.3
  locator: { number: "l3/knowledge.3", headingPath: ["Level 3", "Knowledge and understanding"] }
  span: { start: 4177, end: 4229 }
  source: "Be aware of the nature of the area of study or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:3
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 3"
  addressee: learner
  verbs: [Be]
  about: "awareness of the nature of the field"
  themes: [none]
  paraphrase: "Know what kind of area the study or work is."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l3/knowledge.4
  locator: { number: "l3/knowledge.4", headingPath: ["Level 3", "Knowledge and understanding"] }
  span: { start: 4230, end: 4318 }
  source: "Have awareness of different perspectives or approaches within the area of study or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:3
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 3"
  addressee: learner
  verbs: [Have]
  about: "awareness of perspectives"
  themes: [none]
  paraphrase: "Know that the area holds different perspectives or approaches."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l3/application.1
  locator: { number: "l3/application.1", headingPath: ["Level 3", "Application and action"] }
  span: { start: 4342, end: 4417 }
  source: "Address problems that, while well-defined, may be complex and non- routine."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:3
  dimension: application-and-action
  appliesTo: "achievement at Level 3"
  addressee: learner
  verbs: [Address]
  about: "defined but complex, non-routine problems"
  themes: [none]
  paraphrase: "Deal with problems that are defined but may be complex and non-routine."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l3/application.2
  locator: { number: "l3/application.2", headingPath: ["Level 3", "Application and action"] }
  span: { start: 4418, end: 4486 }
  source: "Identify, select and use appropriate skills, methods and procedures."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:3
  dimension: application-and-action
  appliesTo: "achievement at Level 3"
  addressee: learner
  verbs: [Identify, select, use]
  about: "choosing skills, methods and procedures"
  themes: [none]
  paraphrase: "Find, choose and use suitable skills, methods and procedures."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l3/application.3
  locator: { number: "l3/application.3", headingPath: ["Level 3", "Application and action"] }
  span: { start: 4487, end: 4535 }
  source: "Use appropriate investigation to inform actions."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:3
  dimension: application-and-action
  appliesTo: "achievement at Level 3"
  addressee: learner
  verbs: [Use, inform]
  about: "investigation to guide action"
  themes: [none]
  paraphrase: "Use suitable investigation to guide action."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l3/application.4
  locator: { number: "l3/application.4", headingPath: ["Level 3", "Application and action"] }
  span: { start: 4536, end: 4587 }
  source: "Review how effective methods and actions have been."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:3
  dimension: application-and-action
  appliesTo: "achievement at Level 3"
  addressee: learner
  verbs: [Review]
  about: "reviewing methods and actions"
  themes: [none]
  paraphrase: "Look back on how well methods and actions have worked."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l3/autonomy.1
  locator: { number: "l3/autonomy.1", headingPath: ["Level 3", "Autonomy and accountability"] }
  span: { start: 4616, end: 4763 }
  source: "Take responsibility for initiating and completing tasks and procedures, including where relevant, responsibility for supervising or guiding others."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:3
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 3"
  addressee: learner
  verbs: [Take, initiating, completing]
  about: "starting tasks; supervising others where relevant"
  themes: [none]
  paraphrase: "Take responsibility for starting and finishing tasks and procedures, including, where relevant, supervising or guiding others."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l3/autonomy.2
  locator: { number: "l3/autonomy.2", headingPath: ["Level 3", "Autonomy and accountability"] }
  span: { start: 4764, end: 4822 }
  source: "Exercise autonomy and judgement within limited parameters."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:3
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 3"
  addressee: learner
  verbs: [Exercise]
  about: "autonomy within limited parameters"
  themes: [none]
  paraphrase: "Use independence and judgement within limited bounds."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l4/knowledge.1
  locator: { number: "l4/knowledge.1", headingPath: ["Level 4", "Knowledge and understanding"] }
  span: { start: 5284, end: 5408 }
  source: "Use practical, theoretical or technical understanding to address problems that are well-defined but complex and non-routine."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:4
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 4"
  addressee: learner
  verbs: [Use, address]
  about: "practical, theoretical or technical understanding for complex problems"
  themes: [none]
  paraphrase: "Draw on practical, theoretical or technical understanding to deal with problems that are defined but complex and non-routine."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l4/knowledge.2
  locator: { number: "l4/knowledge.2", headingPath: ["Level 4", "Knowledge and understanding"] }
  span: { start: 5409, end: 5472 }
  source: "Analyse, interpret and evaluate relevant information and ideas."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:4
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 4"
  addressee: learner
  verbs: [Analyse, interpret, evaluate]
  about: "analysing, interpreting and evaluating"
  themes: [none]
  paraphrase: "Analyse, make sense of and weigh up relevant information and ideas."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l4/knowledge.3
  locator: { number: "l4/knowledge.3", headingPath: ["Level 4", "Knowledge and understanding"] }
  span: { start: 5473, end: 5547 }
  source: "Be aware of the nature and approximate scope of the area of study or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:4
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 4"
  addressee: learner
  verbs: [Be]
  about: "awareness of nature and rough scope"
  themes: [none]
  paraphrase: "Know the nature of the area and roughly how far it extends."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l4/knowledge.4
  locator: { number: "l4/knowledge.4", headingPath: ["Level 4", "Knowledge and understanding"] }
  span: { start: 5548, end: 5648 }
  source: "Have an informed awareness of different perspectives or approaches within the area of study or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:4
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 4"
  addressee: learner
  verbs: [Have]
  about: "informed awareness of perspectives"
  themes: [none]
  paraphrase: "Have an informed awareness of the different perspectives or approaches in the area."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l4/application.1
  locator: { number: "l4/application.1", headingPath: ["Level 4", "Application and action"] }
  span: { start: 5672, end: 5758 }
  source: "Address problems that are complex and non- routine while normally fairly well-defined."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:4
  dimension: application-and-action
  appliesTo: "achievement at Level 4"
  addressee: learner
  verbs: [Address]
  about: "complex, non-routine but fairly defined problems"
  themes: [none]
  paraphrase: "Deal with problems that are complex and non-routine though usually fairly well defined."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l4/application.2
  locator: { number: "l4/application.2", headingPath: ["Level 4", "Application and action"] }
  span: { start: 5759, end: 5814 }
  source: "Identify, adapt and use appropriate methods and skills."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:4
  dimension: application-and-action
  appliesTo: "achievement at Level 4"
  addressee: learner
  verbs: [Identify, adapt, use]
  about: "adapting methods and skills"
  themes: [none]
  paraphrase: "Find, adapt and use suitable methods and skills."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l4/application.3
  locator: { number: "l4/application.3", headingPath: ["Level 4", "Application and action"] }
  span: { start: 5815, end: 5876 }
  source: "Initiate and use appropriate investigation to inform actions."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:4
  dimension: application-and-action
  appliesTo: "achievement at Level 4"
  addressee: learner
  verbs: [Initiate, use, inform]
  about: "starting investigation to guide action"
  themes: [none]
  paraphrase: "Start and use suitable investigation to guide action."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l4/application.4
  locator: { number: "l4/application.4", headingPath: ["Level 4", "Application and action"] }
  span: { start: 5877, end: 5954 }
  source: "Review the effectiveness and appropriateness of methods, actions and results."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:4
  dimension: application-and-action
  appliesTo: "achievement at Level 4"
  addressee: learner
  verbs: [Review]
  about: "reviewing effectiveness and fit"
  themes: [none]
  paraphrase: "Look back on how effective and fitting methods, actions and results have been."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l4/autonomy.1
  locator: { number: "l4/autonomy.1", headingPath: ["Level 4", "Autonomy and accountability"] }
  span: { start: 5983, end: 6089 }
  source: "Take responsibility for courses of action, including where relevant responsibility for the work of others."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:4
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 4"
  addressee: learner
  verbs: [Take]
  about: "responsibility for courses of action and others' work"
  themes: [none]
  paraphrase: "Be accountable for courses of action, and for others' work where relevant."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l4/autonomy.2
  locator: { number: "l4/autonomy.2", headingPath: ["Level 4", "Autonomy and accountability"] }
  span: { start: 6090, end: 6173 }
  source: "Exercise autonomy and judgement within broad but generally well-defined parameters."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:4
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 4"
  addressee: learner
  verbs: [Exercise]
  about: "autonomy within broad, generally defined parameters"
  themes: [none]
  paraphrase: "Use independence and judgement within bounds that are broad but generally well defined."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l5/knowledge.1
  locator: { number: "l5/knowledge.1", headingPath: ["Level 5", "Knowledge and understanding"] }
  span: { start: 6645, end: 6761 }
  source: "Use practical, theoretical or technological understanding to find ways forward in broadly-defined, complex contexts."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:5
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 5"
  addressee: learner
  verbs: [Use, find]
  about: "understanding to find ways forward in complex contexts"
  themes: [none]
  paraphrase: "Draw on practical, theoretical or technological understanding so as to find a way forward in complex situations defined only broadly."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l5/knowledge.2
  locator: { number: "l5/knowledge.2", headingPath: ["Level 5", "Knowledge and understanding"] }
  span: { start: 6762, end: 6835 }
  source: "Analyse, interpret and evaluate relevant information, concepts and ideas."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:5
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 5"
  addressee: learner
  verbs: [Analyse, interpret, evaluate]
  about: "analysing information, concepts and ideas"
  themes: [none]
  paraphrase: "Analyse, make sense of and weigh up relevant information, concepts and ideas."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l5/knowledge.3
  locator: { number: "l5/knowledge.3", headingPath: ["Level 5", "Knowledge and understanding"] }
  span: { start: 6836, end: 6898 }
  source: "Be aware of the nature and scope of the area of study or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:5
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 5"
  addressee: learner
  verbs: [Be]
  about: "awareness of nature and scope"
  themes: [none]
  paraphrase: "Know the nature and the scope of the area."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l5/knowledge.4
  locator: { number: "l5/knowledge.4", headingPath: ["Level 5", "Knowledge and understanding"] }
  span: { start: 6899, end: 6997 }
  source: "Understand different perspectives, approaches or schools of thought and the reasoning behind them."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:5
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 5"
  addressee: learner
  verbs: [Understand]
  about: "understanding schools of thought and their reasoning"
  themes: [none]
  paraphrase: "Understand the area's schools of thought, perspectives or approaches and why they hold."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l5/application.1
  locator: { number: "l5/application.1", headingPath: ["Level 5", "Application and action"] }
  span: { start: 7021, end: 7063 }
  source: "Address broadly-defined, complex problems."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:5
  dimension: application-and-action
  appliesTo: "achievement at Level 5"
  addressee: learner
  verbs: [Address]
  about: "broadly defined, complex problems"
  themes: [none]
  paraphrase: "Deal with complex problems that are only broadly defined."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l5/application.2
  locator: { number: "l5/application.2", headingPath: ["Level 5", "Application and action"] }
  span: { start: 7064, end: 7120 }
  source: "Determine, adapt and use appropriate methods and skills."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:5
  dimension: application-and-action
  appliesTo: "achievement at Level 5"
  addressee: learner
  verbs: [Determine, adapt, use]
  about: "deciding on and adapting methods"
  themes: [none]
  paraphrase: "Decide on, adapt and use suitable methods and skills."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l5/application.3
  locator: { number: "l5/application.3", headingPath: ["Level 5", "Application and action"] }
  span: { start: 7121, end: 7176 }
  source: "Use relevant research or development to inform actions."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:5
  dimension: application-and-action
  appliesTo: "achievement at Level 5"
  addressee: learner
  verbs: [Use, inform]
  about: "research or development to guide action"
  themes: [none]
  paraphrase: "Use relevant research or development to guide action."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l5/application.4
  locator: { number: "l5/application.4", headingPath: ["Level 5", "Application and action"] }
  span: { start: 7177, end: 7215 }
  source: "Evaluate actions, methods and results."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:5
  dimension: application-and-action
  appliesTo: "achievement at Level 5"
  addressee: learner
  verbs: [Evaluate]
  about: "evaluating actions, methods and results"
  themes: [none]
  paraphrase: "Weigh up actions, methods and results."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l5/autonomy.1
  locator: { number: "l5/autonomy.1", headingPath: ["Level 5", "Autonomy and accountability"] }
  span: { start: 7244, end: 7375 }
  source: "Take responsibility for planning and developing courses of action, including where relevant, responsibility for the work of others."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:5
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 5"
  addressee: learner
  verbs: [Take, planning, developing]
  about: "planning and developing courses of action"
  themes: [none]
  paraphrase: "Be accountable for planning and shaping courses of action, including, where relevant, the work of others."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l5/autonomy.2
  locator: { number: "l5/autonomy.2", headingPath: ["Level 5", "Autonomy and accountability"] }
  span: { start: 7376, end: 7432 }
  source: "Exercise autonomy and judgement within broad parameters."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:5
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 5"
  addressee: learner
  verbs: [Exercise]
  about: "autonomy within broad parameters"
  themes: [none]
  paraphrase: "Use independence and judgement within broad bounds."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/knowledge.1
  locator: { number: "l6/knowledge.1", headingPath: ["Level 6", "Knowledge and understanding"] }
  span: { start: 7965, end: 8109 }
  source: "Refine and use practical, conceptual or technological understanding to create ways forward in contexts where there are many interacting factors."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Refine, use, create]
  about: "refining understanding to create ways forward"
  themes: [none]
  paraphrase: "Refine practical, conceptual or technological understanding and use it to create ways forward where many factors interact."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/knowledge.2
  locator: { number: "l6/knowledge.2", headingPath: ["Level 6", "Knowledge and understanding"] }
  span: { start: 8110, end: 8193 }
  source: "Critically analyse, interpret and evaluate complex information, concepts and ideas."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [analyse, interpret, evaluate]
  about: "critical analysis of complex information"
  themes: [none]
  paraphrase: "Analyse, make sense of and weigh up complex information, concepts and ideas critically."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/knowledge.3
  locator: { number: "l6/knowledge.3", headingPath: ["Level 6", "Knowledge and understanding"] }
  span: { start: 8194, end: 8263 }
  source: "Understand the context in which the area of study or work is located."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Understand]
  about: "the context of the field"
  themes: [none]
  paraphrase: "Understand the setting in which the area sits."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/knowledge.4
  locator: { number: "l6/knowledge.4", headingPath: ["Level 6", "Knowledge and understanding"] }
  span: { start: 8264, end: 8326 }
  source: "Be aware of current developments in the area of study or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Be]
  about: "awareness of current developments"
  themes: [none]
  paraphrase: "Know what is currently developing in the area."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/knowledge.5
  locator: { number: "l6/knowledge.5", headingPath: ["Level 6", "Knowledge and understanding"] }
  span: { start: 8327, end: 8431 }
  source: "Understand different perspectives, approaches or schools of thought and the theories that underpin them."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Understand]
  about: "schools of thought and their theories"
  themes: [none]
  paraphrase: "Understand the area's schools of thought, perspectives or approaches in the area and the theories beneath them."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/application.1
  locator: { number: "l6/application.1", headingPath: ["Level 6", "Application and action"] }
  span: { start: 8455, end: 8538 }
  source: "Address problems that have limited definition and involve many interacting factors."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: application-and-action
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Address]
  about: "problems of limited definition, many interacting factors"
  themes: [none]
  paraphrase: "Deal with problems that are only loosely defined and involve many interacting factors."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/application.2
  locator: { number: "l6/application.2", headingPath: ["Level 6", "Application and action"] }
  span: { start: 8539, end: 8603 }
  source: "Determine, refine, adapt and use appropriate methods and skills."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: application-and-action
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Determine, refine, adapt, use]
  about: "deciding on, refining and adapting methods"
  themes: [none]
  paraphrase: "Decide on, refine, adapt and use suitable methods and skills."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/application.3
  locator: { number: "l6/application.3", headingPath: ["Level 6", "Application and action"] }
  span: { start: 8604, end: 8689 }
  source: "Use and where appropriate design relevant research and development to inform actions."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: application-and-action
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Use, design, inform]
  about: "using and designing research"
  themes: [none]
  paraphrase: "Use relevant research and development, designing it where appropriate, to guide action."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/application.4
  locator: { number: "l6/application.4", headingPath: ["Level 6", "Application and action"] }
  span: { start: 8690, end: 8751 }
  source: "Evaluate actions, methods and results and their implications."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: application-and-action
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Evaluate]
  about: "evaluating results and their implications"
  themes: [none]
  paraphrase: "Weigh up actions, methods and results and what follows from them."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/autonomy.1
  locator: { number: "l6/autonomy.1", headingPath: ["Level 6", "Autonomy and accountability"] }
  span: { start: 8780, end: 8915 }
  source: "Take responsibility for planning and developing courses of action that are capable of underpinning substantial changes or developments."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Take, planning, developing, underpinning]
  about: "courses of action underpinning substantial change"
  themes: [none]
  paraphrase: "Be accountable for planning and shaping courses of action that can underpin substantial change or development."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/autonomy.2
  locator: { number: "l6/autonomy.2", headingPath: ["Level 6", "Autonomy and accountability"] }
  span: { start: 8916, end: 9027 }
  source: "Initiate and lead tasks and processes, taking responsibility, where relevant, for the work and roles of others."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Initiate, lead, taking]
  about: "initiating and leading, responsible for others"
  themes: [none]
  paraphrase: "Start and lead tasks and processes and, where relevant, answer for others' work and roles."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l6/autonomy.3
  locator: { number: "l6/autonomy.3", headingPath: ["Level 6", "Autonomy and accountability"] }
  span: { start: 9028, end: 9066 }
  source: "Exercise broad autonomy and judgement."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:6
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 6"
  addressee: learner
  verbs: [Exercise]
  about: "broad autonomy and judgement"
  themes: [none]
  paraphrase: "Use broad independence and judgement."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/knowledge.1
  locator: { number: "l7/knowledge.1", headingPath: ["Level 7", "Knowledge and understanding"] }
  span: { start: 9637, end: 9786 }
  source: "Reformulate and use practical, conceptual or technological understanding to create ways forward in contexts where there are many interacting factors."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [Reformulate, use, create]
  about: "reformulating understanding to create ways forward"
  themes: [none]
  paraphrase: "Reformulate practical, conceptual or technological understanding and use it to create ways forward where many factors interact."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/knowledge.2
  locator: { number: "l7/knowledge.2", headingPath: ["Level 7", "Knowledge and understanding"] }
  span: { start: 9787, end: 9905 }
  source: "Critically analyse, interpret and evaluate complex information, concepts and theories to produce modified conceptions."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [analyse, interpret, evaluate, produce]
  about: "critical analysis producing modified conceptions"
  themes: [none]
  paraphrase: "Analyse, make sense of and weigh up complex information, concepts and theories critically, so as to arrive at modified conceptions."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/knowledge.3
  locator: { number: "l7/knowledge.3", headingPath: ["Level 7", "Knowledge and understanding"] }
  span: { start: 9906, end: 9982 }
  source: "Understand the wider contexts in which the area of study or work is located."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [Understand]
  about: "the wider contexts of the field"
  themes: [none]
  paraphrase: "Understand the wider settings in which the area sits."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/knowledge.4
  locator: { number: "l7/knowledge.4", headingPath: ["Level 7", "Knowledge and understanding"] }
  span: { start: 9983, end: 10044 }
  source: "Understand current developments in the area of study or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [Understand]
  about: "understanding current developments"
  themes: [none]
  paraphrase: "Understand what is currently developing in the area."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/knowledge.5
  locator: { number: "l7/knowledge.5", headingPath: ["Level 7", "Knowledge and understanding"] }
  span: { start: 10045, end: 10156 }
  source: "Understand different theoretical and methodological perspectives and how they affect the area of study or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [Understand, affect]
  about: "theoretical and methodological perspectives"
  themes: [none]
  paraphrase: "Understand the area's different theoretical and methodological perspectives and how they shape it."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/application.1
  locator: { number: "l7/application.1", headingPath: ["Level 7", "Application and action"] }
  span: { start: 10180, end: 10267 }
  source: "Conceptualise and address problematic situations that involve many interacting factors."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: application-and-action
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [Conceptualise, address]
  about: "conceptualising problematic situations"
  themes: [none]
  paraphrase: "Frame and deal with problematic situations involving many interacting factors."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/application.2
  locator: { number: "l7/application.2", headingPath: ["Level 7", "Application and action"] }
  span: { start: 10268, end: 10327 }
  source: "Determine and use appropriate methodologies and approaches."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: application-and-action
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [Determine, use]
  about: "deciding on methodologies"
  themes: [none]
  paraphrase: "Decide on and use suitable methodologies and approaches."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/application.3
  locator: { number: "l7/application.3", headingPath: ["Level 7", "Application and action"] }
  span: { start: 10328, end: 10480 }
  source: "Design and undertake research, development or strategic activities to inform the area of work or study or produce organisational or professional change."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: application-and-action
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [Design, undertake, inform, produce]
  about: "designing research or strategic activity"
  themes: [none]
  paraphrase: "Design and carry out research, development or strategic work that informs the area or brings organisational or professional change."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/application.4
  locator: { number: "l7/application.4", headingPath: ["Level 7", "Application and action"] }
  span: { start: 10481, end: 10573 }
  source: "Critically evaluate actions, methods and results and their short and long term implications."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: application-and-action
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [evaluate]
  about: "critical evaluation of short and long term implications"
  themes: [none]
  paraphrase: "Critically weigh up actions, methods and results and what follows from them in the short and long term."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/autonomy.1
  locator: { number: "l7/autonomy.1", headingPath: ["Level 7", "Autonomy and accountability"] }
  span: { start: 10602, end: 10730 }
  source: "Take responsibility for planning and developing courses of action that initiate or underpin substantial changes or developments."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [Take, planning, developing, initiate, underpin]
  about: "courses of action initiating or underpinning substantial change"
  themes: [none]
  paraphrase: "Be accountable for planning and shaping courses of action that start or underpin substantial change or development."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/autonomy.2
  locator: { number: "l7/autonomy.2", headingPath: ["Level 7", "Autonomy and accountability"] }
  span: { start: 10731, end: 10812 }
  source: "Exercise broad autonomy and judgement across a significant area of work or study."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [Exercise]
  about: "broad autonomy across a significant area"
  themes: [none]
  paraphrase: "Use broad independence and judgement over a significant area of study or work."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l7/autonomy.3
  locator: { number: "l7/autonomy.3", headingPath: ["Level 7", "Autonomy and accountability"] }
  span: { start: 10813, end: 10932 }
  source: "Initiate and lead complex tasks and processes, taking responsibility, where relevant, for the work and roles of others."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:7
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 7"
  addressee: learner
  verbs: [Initiate, lead, taking]
  about: "initiating and leading complex tasks"
  themes: [none]
  paraphrase: "Start and lead complex tasks and processes and, where relevant, answer for others' work and roles."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/knowledge.1
  locator: { number: "l8/knowledge.1", headingPath: ["Level 8", "Knowledge and understanding"] }
  span: { start: 11672, end: 11852 }
  source: "Develop original practical, conceptual or technological understanding to create ways forward in contexts that lack definition and where there are many complex, interacting factors."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [Develop, create]
  about: "original understanding in undefined contexts"
  themes: [none]
  paraphrase: "Develop original understanding, practical, conceptual or technological, to create ways forward where things lack definition and many complex factors interact."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/knowledge.2
  locator: { number: "l8/knowledge.2", headingPath: ["Level 8", "Knowledge and understanding"] }
  span: { start: 11853, end: 11977 }
  source: "Critically analyse, interpret and evaluate complex information, concepts and theories to produce new knowledge and theories."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [analyse, interpret, evaluate, produce]
  about: "critical analysis producing new knowledge and theory"
  themes: [none]
  paraphrase: "Analyse, make sense of and weigh up complex information, concepts and theories critically, so as to produce new knowledge and theories."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/knowledge.3
  locator: { number: "l8/knowledge.3", headingPath: ["Level 8", "Knowledge and understanding"] }
  span: { start: 11978, end: 12079 }
  source: "Understand and reconceptualise the wider contexts in which the field of knowledge or work is located."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [Understand, reconceptualise]
  about: "reconceptualising the wider contexts"
  themes: [none]
  paraphrase: "Understand, and reframe, the wider settings in which the field sits."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/knowledge.4
  locator: { number: "l8/knowledge.4", headingPath: ["Level 8", "Knowledge and understanding"] }
  span: { start: 12080, end: 12164 }
  source: "Extend a field of knowledge or work by contributing original knowledge and thinking."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [Extend, contributing]
  about: "extending the field with original contributions"
  themes: [none]
  paraphrase: "Extend a field of knowledge or work through original knowledge and thinking."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/knowledge.5
  locator: { number: "l8/knowledge.5", headingPath: ["Level 8", "Knowledge and understanding"] }
  span: { start: 12165, end: 12305 }
  source: "Exercise critical understanding of different theoretical and methodological perspectives and how they affect the field of knowledge or work."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: knowledge-and-understanding
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [Exercise, affect]
  about: "critical understanding of perspectives"
  themes: [none]
  paraphrase: "Bring critical understanding to the field's different theoretical and methodological perspectives and how they shape it."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/application.1
  locator: { number: "l8/application.1", headingPath: ["Level 8", "Application and action"] }
  span: { start: 12329, end: 12424 }
  source: "Conceptualise and address problematic situations that involve many complex interacting factors."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: application-and-action
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [Conceptualise, address]
  about: "conceptualising highly complex situations"
  themes: [none]
  paraphrase: "Frame and deal with problematic situations involving many complex interacting factors."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/application.2
  locator: { number: "l8/application.2", headingPath: ["Level 8", "Application and action"] }
  span: { start: 12425, end: 12484 }
  source: "Formulate and use appropriate methodologies and approaches."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: application-and-action
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [Formulate, use]
  about: "formulating methodologies"
  themes: [none]
  paraphrase: "Formulate and use suitable methodologies and approaches."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/application.3
  locator: { number: "l8/application.3", headingPath: ["Level 8", "Application and action"] }
  span: { start: 12485, end: 12668 }
  source: "Initiate, design and undertake research, development or strategic activities that extend the field of work or knowledge or result in significant organisational or professional change."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: application-and-action
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [Initiate, design, undertake, extend, result]
  about: "research that extends the field or brings change"
  themes: [none]
  paraphrase: "Start, design and carry out research, development or strategic work that extends the field or brings significant organisational or professional change."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/application.4
  locator: { number: "l8/application.4", headingPath: ["Level 8", "Application and action"] }
  span: { start: 12669, end: 12818 }
  source: "Critically evaluate actions, methods and results and their short and long term implications for the field of work or knowledge and its wider context."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: application-and-action
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [evaluate]
  about: "critical evaluation of implications for the field"
  themes: [none]
  paraphrase: "Critically weigh up actions, methods and results and what follows from them, now and later, for the field and its wider setting."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/autonomy.1
  locator: { number: "l8/autonomy.1", headingPath: ["Level 8", "Autonomy and accountability"] }
  span: { start: 12847, end: 13042 }
  source: "Take responsibility for planning and developing courses of action that have a significant impact on the field of work or knowledge, or result in substantial organisational or professional change."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [Take, planning, developing, have, result]
  about: "courses of action with significant impact on the field"
  themes: [none]
  paraphrase: "Be accountable for planning and shaping courses of action whose impact on the field is significant or bring substantial organisational or professional change."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/autonomy.2
  locator: { number: "l8/autonomy.2", headingPath: ["Level 8", "Autonomy and accountability"] }
  span: { start: 13043, end: 13263 }
  source: "Exercise broad autonomy, judgement and leadership as a leading practitioner or scholar sharing responsibility for the development of a field of work or knowledge, or for substantial organisational or professional change."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [Exercise, sharing]
  about: "leadership as a leading practitioner or scholar"
  themes: [none]
  paraphrase: "Use broad independence and judgement, and lead from the front of the field as practitioner or scholar, sharing responsibility for developing a field or for substantial change."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: welsh-government/cqfw-2009/l8/autonomy.3
  locator: { number: "l8/autonomy.3", headingPath: ["Level 8", "Autonomy and accountability"] }
  span: { start: 13264, end: 13329 }
  source: "Take responsibility for the advancement of professional practice."
  stem: none
  statementType: descriptor
  force: describes
  level: cqfw:8
  dimension: autonomy-and-accountability
  appliesTo: "achievement at Level 8"
  addressee: learner
  verbs: [Take]
  about: "advancing professional practice"
  themes: [none]
  paraphrase: "Take responsibility for advancing professional practice."
  quote: full   # the issuer statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
- statement: welsh-government/cqfw-2009/entry-2/knowledge.1
  forPractitioner: { text: "At Entry 2, learners apply what they know or understand to simple activities they already know.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 2, you use what you know to do simple, familiar things.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-2/knowledge.2
  forPractitioner: { text: "At Entry 2, learners know the steps a simple activity involves.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 2, you know the steps to finish a simple activity.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-2/application.1
  forPractitioner: { text: "At Entry 2, learners carry out simple tasks they are used to.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 2, you can do simple tasks you have done before.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-2/application.2
  forPractitioner: { text: "At Entry 2, learners complete tasks by following instructions or steps they have practised.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 2, you finish tasks by following instructions or steps you have practised.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-2/autonomy.1
  forPractitioner: { text: "At Entry 2, learners start, with guidance, to take some responsibility for the results of simple activities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 2, with help, you start to take some responsibility for how simple activities turn out.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-2/autonomy.2
  forPractitioner: { text: "At Entry 2, learners join in actively with simple, familiar activities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 2, you take an active part in simple activities you know.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-3/knowledge.1
  forPractitioner: { text: "At Entry 3, learners apply what they know to structured tasks in settings they know.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 3, you use what you know on structured tasks in places and situations you know.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-3/knowledge.2
  forPractitioner: { text: "At Entry 3, learners know and understand the steps structured tasks involve in familiar settings.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 3, you know and understand the steps for structured tasks in familiar situations.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-3/application.1
  forPractitioner: { text: "At Entry 3, learners carry out structured tasks in familiar settings.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 3, you can carry out structured tasks in situations you know.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-3/application.2
  forPractitioner: { text: "At Entry 3, learners are aware that what they do affects themselves and other people.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 3, you know that what you do has effects on you and on others.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-3/autonomy.1
  forPractitioner: { text: "At Entry 3, learners take responsibility, with guidance, for the results of structured activities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 3, with help, you take responsibility for how structured activities turn out.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/entry-3/autonomy.2
  forPractitioner: { text: "At Entry 3, learners join in actively in settings they know.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Entry 3, you take an active part in activities in familiar situations.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l1/knowledge.1
  forPractitioner: { text: "At Level 1, learners draw on facts, procedures and ideas to complete routine tasks that are clearly defined.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 1, you use facts, methods and ideas to finish routine tasks with clear instructions.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l1/knowledge.2
  forPractitioner: { text: "At Level 1, learners are aware of the information that matters in their area of study or work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 1, you know what information matters in your study or work.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l1/application.1
  forPractitioner: { text: "At Level 1, learners complete routine, clearly defined tasks.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 1, you finish routine tasks that are clearly set out.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l1/application.2
  forPractitioner: { text: "At Level 1, learners apply the skills and procedures a task needs.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 1, you use the skills and methods the task needs.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l1/application.3
  forPractitioner: { text: "At Level 1, learners choose and use the information that fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 1, you pick out and use the information you need.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l1/application.4
  forPractitioner: { text: "At Level 1, learners can tell whether their actions worked.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 1, you can tell whether what you did worked.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l1/autonomy.1
  forPractitioner: { text: "At Level 1, learners take responsibility for finishing tasks and procedures, with direction or guidance as needed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 1, you take responsibility for finishing tasks, with direction or help when you need it.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l2/knowledge.1
  forPractitioner: { text: "At Level 2, learners draw on their understanding of facts, procedures and ideas to complete defined tasks and solve straightforward problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 2, you use your understanding of facts, methods and ideas to finish set tasks and solve simple problems.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l2/knowledge.2
  forPractitioner: { text: "At Level 2, learners interpret the information and ideas that matter to the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 2, you make sense of the information and ideas that matter.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l2/knowledge.3
  forPractitioner: { text: "At Level 2, learners know which kinds of information are relevant to their area.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 2, you know what kinds of information are useful in your study or work.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l2/application.1
  forPractitioner: { text: "At Level 2, learners complete defined, mostly routine tasks and solve straightforward problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 2, you finish set tasks that are mostly routine and sort out simple problems.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l2/application.2
  forPractitioner: { text: "At Level 2, learners choose and apply the skills and procedures that fit.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 2, you choose and use the right skills and methods.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l2/application.3
  forPractitioner: { text: "At Level 2, learners find, collect and use relevant information to guide their actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 2, you find, collect and use the information that helps you decide what to do.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l2/application.4
  forPractitioner: { text: "At Level 2, learners judge how effective their actions were.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 2, you can judge how well what you did worked.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l2/autonomy.1
  forPractitioner: { text: "At Level 2, learners take responsibility for completing tasks and procedures.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 2, you take responsibility for getting tasks done.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l2/autonomy.2
  forPractitioner: { text: "At Level 2, learners use autonomy and judgement within overall direction or guidance.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 2, you make some of your own decisions, within the direction you are given.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l3/knowledge.1
  forPractitioner: { text: "At Level 3, learners bring factual, procedural and theoretical understanding to tasks and problems that are defined but can be complex and unfamiliar.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 3, you use facts, methods and theory on tasks and problems that are set out but can be complex and new to you.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l3/knowledge.2
  forPractitioner: { text: "At Level 3, learners interpret and evaluate relevant information and ideas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 3, you make sense of information and ideas and judge their worth.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l3/knowledge.3
  forPractitioner: { text: "At Level 3, learners are aware of the nature of their area of study or work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 3, you understand what kind of field you are studying or working in.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l3/knowledge.4
  forPractitioner: { text: "At Level 3, learners are aware that their area holds different perspectives or approaches.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 3, you know that people in your field see things in different ways.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l3/application.1
  forPractitioner: { text: "At Level 3, learners tackle problems that are defined yet may be complex and unfamiliar.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 3, you tackle problems that are set out but can be complex and new to you.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l3/application.2
  forPractitioner: { text: "At Level 3, learners identify, choose and apply suitable skills, methods and procedures.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 3, you work out which skills and methods suit the job, then choose and use them.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l3/application.3
  forPractitioner: { text: "At Level 3, learners use fitting investigation to guide what they do.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 3, you look into things properly before deciding what to do.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l3/application.4
  forPractitioner: { text: "At Level 3, learners review how effective their methods and actions were.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 3, you look back at how well your methods and actions worked.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l3/autonomy.1
  forPractitioner: { text: "At Level 3, learners take responsibility for starting and finishing tasks and, where relevant, for supervising or guiding others.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 3, you take charge of starting and finishing tasks, and sometimes of guiding other people.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l3/autonomy.2
  forPractitioner: { text: "At Level 3, learners use autonomy and judgement within limited parameters.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 3, you make your own decisions within limited bounds.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l4/knowledge.1
  forPractitioner: { text: "At Level 4, learners bring practical, theoretical or technical understanding to defined problems that are complex and non-routine.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 4, you use practical, theoretical or technical understanding on problems that are clear in outline but complex and unfamiliar.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l4/knowledge.2
  forPractitioner: { text: "At Level 4, learners analyse, interpret and evaluate relevant information and ideas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 4, you break information and ideas down, make sense of them and judge their worth.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l4/knowledge.3
  forPractitioner: { text: "At Level 4, learners are aware of the nature and approximate scope of their area.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 4, you know what your field is about and roughly how far it reaches.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l4/knowledge.4
  forPractitioner: { text: "At Level 4, learners have an informed awareness of the area's different perspectives or approaches.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 4, you know enough about the different views in your field to talk about them with some knowledge.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l4/application.1
  forPractitioner: { text: "At Level 4, learners tackle complex, non-routine problems that are usually fairly clearly defined.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 4, you tackle complex, unfamiliar problems that are still fairly clear in outline.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l4/application.2
  forPractitioner: { text: "At Level 4, learners identify, adapt and apply suitable methods and skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 4, you find the right methods and skills and adapt them to fit.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l4/application.3
  forPractitioner: { text: "At Level 4, learners initiate and use fitting investigation to guide their actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 4, you start your own investigations and use them to decide what to do.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l4/application.4
  forPractitioner: { text: "At Level 4, learners review both how effective and how appropriate their methods, actions and results were.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 4, you look back at whether your methods, actions and results worked and were the right choice.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l4/autonomy.1
  forPractitioner: { text: "At Level 4, learners take responsibility for courses of action and, where relevant, for other people's work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 4, you take responsibility for a whole course of action, and sometimes for other people's work.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l4/autonomy.2
  forPractitioner: { text: "At Level 4, learners use their own judgement, with some independence, inside broad but generally clear limits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 4, you make your own decisions within wide but clear bounds.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l5/knowledge.1
  forPractitioner: { text: "At Level 5, learners bring practical, theoretical or technological understanding to complex, broadly defined situations and find a way forward.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 5, you use your understanding to find a way forward in complex situations that are only broadly defined.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l5/knowledge.2
  forPractitioner: { text: "At Level 5, learners analyse and interpret the relevant information, concepts and ideas, and judge them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 5, you break down, make sense of and judge information, concepts and ideas.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l5/knowledge.3
  forPractitioner: { text: "At Level 5, learners are aware of the nature and scope of their area.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 5, you know what your field is about and how far it reaches.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l5/knowledge.4
  forPractitioner: { text: "At Level 5, learners understand the schools of thought, perspectives or approaches in the area and why each holds.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 5, you understand the different schools of thought in your field and the reasons behind them.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l5/application.1
  forPractitioner: { text: "At Level 5, learners tackle complex problems that are only broadly defined.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 5, you tackle complex problems that are only loosely set out.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l5/application.2
  forPractitioner: { text: "At Level 5, learners determine, adapt and apply suitable methods and skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 5, you decide which methods and skills to use and adapt them.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l5/application.3
  forPractitioner: { text: "At Level 5, learners use relevant research or development work to guide their actions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 5, you use research or development work to decide what to do.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l5/application.4
  forPractitioner: { text: "At Level 5, learners evaluate their actions, methods and results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 5, you judge your actions, methods and results.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l5/autonomy.1
  forPractitioner: { text: "At Level 5, learners are accountable for planning and shaping courses of action and, where relevant, for other people's work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 5, you take responsibility for planning and shaping a course of action, and sometimes for other people's work.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l5/autonomy.2
  forPractitioner: { text: "At Level 5, learners use autonomy and judgement within broad parameters.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 5, you make your own decisions within wide bounds.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/knowledge.1
  forPractitioner: { text: "At Level 6, learners refine practical, conceptual or technological understanding and use it to create ways forward where many factors interact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you sharpen your understanding and use it to create a way forward where many things affect one another.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/knowledge.2
  forPractitioner: { text: "At Level 6, learners critically analyse and interpret complex information, concepts and ideas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you critically break down, interpret and judge complex information, concepts and ideas.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/knowledge.3
  forPractitioner: { text: "At Level 6, learners understand the context in which their area is located.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you understand the wider setting your field belongs to.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/knowledge.4
  forPractitioner: { text: "At Level 6, learners are aware of current developments in their area.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you keep up with what is new in your field.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/knowledge.5
  forPractitioner: { text: "At Level 6, learners understand the schools of thought, perspectives or approaches in the area and the theory beneath each.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you understand the different schools of thought in your field and the theories they rest on.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/application.1
  forPractitioner: { text: "At Level 6, learners tackle problems of limited definition in which many factors interact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you tackle problems that are not clearly defined and where many things affect one another.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/application.2
  forPractitioner: { text: "At Level 6, learners determine, refine, adapt and apply suitable methods and skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you decide on methods and skills, then refine and adapt them.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/application.3
  forPractitioner: { text: "At Level 6, learners use relevant research and development to guide action and design it where appropriate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you use research to decide what to do, and design your own research where it fits.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/application.4
  forPractitioner: { text: "At Level 6, learners evaluate their actions, methods and results and the implications of each.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you judge your actions, methods and results and what they lead to.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/autonomy.1
  forPractitioner: { text: "At Level 6, learners are accountable for planning and shaping courses of action able to underpin substantial change or development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you take responsibility for planning actions that can support big changes or developments.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/autonomy.2
  forPractitioner: { text: "At Level 6, learners initiate and lead tasks and processes and, where relevant, take responsibility for others' work and roles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you start and lead tasks, and sometimes take responsibility for other people's work and roles.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l6/autonomy.3
  forPractitioner: { text: "At Level 6, learners exercise broad autonomy and judgement.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 6, you make your own decisions across a wide range.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/knowledge.1
  forPractitioner: { text: "At Level 7, learners reformulate practical, conceptual or technological understanding and use it to create ways forward where many factors interact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you rework your understanding and use it to create a way forward where many things affect one another.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/knowledge.2
  forPractitioner: { text: "At Level 7, learners critically analyse and interpret complex information, concepts and theories to arrive at modified conceptions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you critically examine complex information, concepts and theories and come out with changed ideas of your own.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/knowledge.3
  forPractitioner: { text: "At Level 7, learners understand the wider contexts in which their area is located.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you understand the wider settings your field belongs to.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/knowledge.4
  forPractitioner: { text: "At Level 7, learners understand current developments in their area.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you understand what is new in your field, not only that it is happening.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/knowledge.5
  forPractitioner: { text: "At Level 7, learners understand the different theoretical and methodological perspectives and how each shapes the area.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you understand the theories and research approaches in your field and how they shape it.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/application.1
  forPractitioner: { text: "At Level 7, learners conceptualise and tackle problematic situations in which many factors interact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you work out how to frame difficult situations where many things affect one another, and then tackle them.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/application.2
  forPractitioner: { text: "At Level 7, learners determine and apply suitable methodologies and approaches.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you decide on whole research approaches and use them.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/application.3
  forPractitioner: { text: "At Level 7, learners design and undertake research, development or strategic work to inform the area or bring about organisational or professional change.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you design and carry out research or strategic work that informs your field or changes how an organisation or profession works.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/application.4
  forPractitioner: { text: "At Level 7, learners critically evaluate their own actions, methods and results and the short and long term implications.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you critically judge your actions, methods and results and what they lead to now and later.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/autonomy.1
  forPractitioner: { text: "At Level 7, learners are accountable for planning and shaping courses of action that start, or form the basis of, substantial change or development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you take responsibility for planning actions that start or support big changes or developments.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/autonomy.2
  forPractitioner: { text: "At Level 7, learners exercise broad autonomy and judgement over a significant area of study or work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you make your own decisions across a large area of work or study.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l7/autonomy.3
  forPractitioner: { text: "At Level 7, learners initiate and lead complex tasks and processes and, where relevant, take responsibility for others' work and roles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 7, you start and lead complex tasks, and sometimes take responsibility for other people's work and roles.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/knowledge.1
  forPractitioner: { text: "At Level 8, learners develop practical, conceptual or technological understanding that is original, to create ways forward in undefined contexts where many complex factors interact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you develop understanding of your own to create a way forward where nothing is clearly defined and many complex things interact.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/knowledge.2
  forPractitioner: { text: "At Level 8, learners critically analyse and interpret complex information, concepts and theories, and produce new knowledge and theory from them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you critically examine complex information, concepts and theories and produce new knowledge and theory.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/knowledge.3
  forPractitioner: { text: "At Level 8, learners understand the wider contexts the field sits in, and reconceptualise them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you understand the wider settings of your field and rethink them.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/knowledge.4
  forPractitioner: { text: "At Level 8, learners extend a field of knowledge or work through original knowledge and thinking of their own.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you push your field forward with original knowledge and thinking of your own.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/knowledge.5
  forPractitioner: { text: "At Level 8, learners exercise critical understanding of the different theoretical and methodological perspectives and how each shapes the field.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you critically understand the theories and research approaches in your field and how they shape it.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/application.1
  forPractitioner: { text: "At Level 8, learners conceptualise and tackle problematic situations in which many complex factors interact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you frame and tackle difficult situations where many complex things affect one another.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/application.2
  forPractitioner: { text: "At Level 8, learners formulate and apply suitable methodologies and approaches.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you create research approaches of your own and use them.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/application.3
  forPractitioner: { text: "At Level 8, learners initiate, design and undertake research, development or strategic work that extends the field or results in significant organisational or professional change.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you start, design and carry out research or strategic work that moves your field on or brings major change to an organisation or profession.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/application.4
  forPractitioner: { text: "At Level 8, learners critically evaluate their own actions, methods and results and the short and long term implications for the field and its wider context.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you critically judge your actions, methods and results and what they mean, now and later, for your field and beyond.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/autonomy.1
  forPractitioner: { text: "At Level 8, learners are accountable for planning and shaping courses of action with significant impact on the field or substantial organisational or professional change.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you take responsibility for planning actions that make a real difference to your field or bring big change to an organisation or profession.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/autonomy.2
  forPractitioner: { text: "At Level 8, learners use broad autonomy and judgement and lead as front-rank practitioners or scholars, sharing responsibility for the development of a field or for substantial change.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you lead with independence and judgement, as a leading practitioner or scholar who helps shape your field or bring major change.", rewrite: full, force: describes, status: drafted }
- statement: welsh-government/cqfw-2009/l8/autonomy.3
  forPractitioner: { text: "At Level 8, learners take responsibility for advancing professional practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At Level 8, you take responsibility for moving professional practice forward.", rewrite: full, force: describes, status: drafted }
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: cqfw:entry-1, role: defines, locator: "D1, Entry 1" }
  - { id: cqfw:entry-2, role: defines, locator: "D1, Entry 2" }
  - { id: cqfw:entry-3, role: defines, locator: "D1, Entry 3" }
  - { id: cqfw:1, role: defines, locator: "D1, Level 1" }
  - { id: cqfw:2, role: defines, locator: "D1, Level 2" }
  - { id: cqfw:3, role: defines, locator: "D1, Level 3" }
  - { id: cqfw:4, role: defines, locator: "D1, Level 4" }
  - { id: cqfw:5, role: defines, locator: "D1, Level 5" }
  - { id: cqfw:6, role: defines, locator: "D1, Level 6" }
  - { id: cqfw:7, role: defines, locator: "D1, Level 7" }
  - { id: cqfw:8, role: defines, locator: "D1, Level 8" }
crosswalks: []   # this document states none; framework rule 2: an equivalence is recorded only with its source, never inferred. The Frameworks 2024 (2.23, 2.24) states the FHEQ's place in the CQFW: recorded there, at S-03
```

### S6 Themes
`not-applicable-by-design`: the document carries no cross-cutting themes.

### S7 Relations
```yaml
- { rel: partOf, target: "CQFW (Credit and Qualifications Framework for Wales)", note: "the framework's level descriptors (Abbott)" }
- { rel: alignsWith, target: "std:doc:qaa-fheq-2024-framework (S-03)", note: "the FHEQ is a constituent part of the CQFW (Frameworks 2024, 2.23)" }
```

### S8 Currency and review
```yaml
published: 2009-01
lastReviewed: none-stated
reviewCycle: none-stated
consultation: none-stated
replacedBy: unknown   # whether a later CQFW edition replaces these descriptors is to check (Part E)
```

### S9 Commentary (optional)
`unknown`: not researched.

### SL Level language
<!-- Proposed for the frameworks variant (Abbott, 04:03: "have a section in any um, level based framework, which is really what these are ... breaks down the language of them, looks at the verbs, looks at the um, the way they communicate uh, progression"; std N-0057). label: both; status: drafted; basis: primary. Our words, with the issuer's own verbs and short quoted phrases; the issuer's full wording, cell by cell, is in the held companion `wkspc2601-library/records/welsh-government-2009-cqfw-level-descriptors-standard.levels.held.md` (UNI only, never published). -->

#### SL1 What defines each level
<!-- Each level's defining step, in our words, for the practitioner and the learner. Read down the table to see the progression. -->

| Level | For the practitioner | For the learner |
|---|---|---|
| Entry 1 | Progress at the very start: from the most basic achievement to beginning to use skills and knowledge tied to one's immediate surroundings. | At Entry 1, you are taking first steps: starting to use skills and knowledge in the world right around you. |
| Entry 2 | Simple, familiar tasks done with guidance, by following instructions or practised steps. | At Entry 2, you do simple things you know, with help, by following instructions or steps you have practised. |
| Entry 3 | Structured tasks in familiar settings, with guidance where needed; first awareness that actions have consequences. | At Entry 3, you do structured tasks in situations you know, with help when needed, and you see that what you do affects others. |
| Level 1 | Routine, clearly defined tasks completed using relevant knowledge and procedures, under direction; checking whether actions worked. | At Level 1, you finish routine tasks with clear instructions, using what you know, and check whether it worked. |
| Level 2 | Defined tasks and straightforward problems, with chosen skills and gathered information; some autonomy within overall direction. | At Level 2, you solve simple problems as well as set tasks, choosing your own methods and making some of your own decisions. |
| Level 3 | Defined problems that may be complex and non-routine; theory enters; initiating tasks and guiding others; aware of different perspectives; autonomy within limited parameters. | At Level 3, problems can be complex and new to you; you use theory, start tasks yourself, may guide others and know your field holds different views. |
| Level 4 | Complex, non-routine problems that are still fairly well defined; analysis joins interpretation and evaluation; adapting methods; initiating investigation; responsible for courses of action; informed awareness of perspectives; broad but defined parameters. | At Level 4, you analyse as well as interpret, adapt methods, start your own investigations and take responsibility for a whole course of action. |
| Level 5 | Complex problems that are only broadly defined; finding ways forward; deciding on methods; using research; planning and developing courses of action; understanding schools of thought and their reasoning. | At Level 5, problems are loosely defined; you find a way forward, decide on methods, use research and understand why different schools of thought hold. |
| Level 6 | Problems of limited definition with many interacting factors; refining understanding to create ways forward; critical analysis; designing research; courses of action that can underpin substantial change; broad autonomy. | At Level 6, you work on loosely defined problems where many things interact, think critically, design research and lead work that can support big change. |
| Level 7 | Problematic situations conceptualised; understanding reformulated; modified conceptions produced; methodologies determined; research or strategy designed to change practice; critical evaluation of long-term implications; autonomy across a significant area. | At Level 7, you frame difficult situations yourself, rework ideas into new ones, choose whole research approaches and lead change across a large area. |
| Level 8 | Original understanding where nothing is defined; new knowledge and theory; formulating methodologies; extending the field; leadership as a leading practitioner or scholar; advancing professional practice. | At Level 8, you create new knowledge and research approaches of your own, push your field forward and lead it as a recognised expert. |

#### SL2 The level table, by strand
<!-- Each cell is our short gloss of the issuer's sentences at that level and strand (the S4 `about` fields); the issuer's sentences are the S4 spans. -->

| Level | Knowledge and understanding | Application and action | Autonomy and accountability |
|---|---|---|---|
| Entry 1 | (summary only) | (summary only) | (summary only) |
| Entry 2 | using what one knows on simple tasks; knowing the steps | doing simple, familiar tasks; following instructions and practised steps | first responsibility, with guidance; active participation |
| Entry 3 | using what one knows on structured tasks in familiar settings; knowing and understanding the steps | doing structured tasks in familiar settings; awareness of consequences | responsibility for outcomes, with guidance; active participation in familiar settings |
| Level 1 | facts, procedures and ideas for routine tasks; awareness of relevant information | completing routine tasks; using relevant skills and procedures; choosing and using information; checking whether actions worked | responsibility under direction |
| Level 2 | understanding for defined tasks and simple problems; interpreting information and ideas; awareness of kinds of relevant information | mostly routine tasks and straightforward problems; choosing skills and procedures; gathering information to guide action; judging how well actions worked | responsibility for completing tasks; some autonomy under overall direction |
| Level 3 | theoretical understanding for complex, non-routine problems; interpreting and evaluating; awareness of the nature of the field; awareness of perspectives | defined but complex, non-routine problems; choosing skills, methods and procedures; investigation to guide action; reviewing methods and actions | starting tasks; supervising others where relevant; autonomy within limited parameters |
| Level 4 | practical, theoretical or technical understanding for complex problems; analysing, interpreting and evaluating; awareness of nature and rough scope; informed awareness of perspectives | complex, non-routine but fairly defined problems; adapting methods and skills; starting investigation to guide action; reviewing effectiveness and fit | responsibility for courses of action and others' work; autonomy within broad, generally defined parameters |
| Level 5 | understanding to find ways forward in complex contexts; analysing information, concepts and ideas; awareness of nature and scope; understanding schools of thought and their reasoning | broadly defined, complex problems; deciding on and adapting methods; research or development to guide action; evaluating actions, methods and results | planning and developing courses of action; autonomy within broad parameters |
| Level 6 | refining understanding to create ways forward; critical analysis of complex information; the context of the field; awareness of current developments; schools of thought and their theories | problems of limited definition, many interacting factors; deciding on, refining and adapting methods; using and designing research; evaluating results and their implications | courses of action underpinning substantial change; initiating and leading, responsible for others; broad autonomy and judgement |
| Level 7 | reformulating understanding to create ways forward; critical analysis producing modified conceptions; the wider contexts of the field; understanding current developments; theoretical and methodological perspectives | conceptualising problematic situations; deciding on methodologies; designing research or strategic activity; critical evaluation of short and long term implications | courses of action initiating or underpinning substantial change; broad autonomy across a significant area; initiating and leading complex tasks |
| Level 8 | original understanding in undefined contexts; critical analysis producing new knowledge and theory; reconceptualising the wider contexts; extending the field with original contributions; critical understanding of perspectives | conceptualising highly complex situations; formulating methodologies; research that extends the field or brings change; critical evaluation of implications for the field | courses of action with significant impact on the field; leadership as a leading practitioner or scholar; advancing professional practice |

#### SL3 Verbs by level
<!-- The issuer's own verbs, as given, in each strand at each level (from the S4 `verbs` fields, first occurrence kept). -->

| Level | Knowledge and understanding | Application and action | Autonomy and accountability |
|---|---|---|---|
| Entry 1 |  |  |  |
| Entry 2 | use, carry, know, complete | carry, follow, use, complete | begin, take, participate |
| Entry 3 | use, carry, know, understand, complete | carry, be | take, participate |
| Level 1 | use, complete, be | complete, use, select, identify | take, completing |
| Level 2 | use, complete, address, interpret, be | complete, address, select, use, identify, gather, inform | take, completing, exercise |
| Level 3 | use, complete, address, interpret, evaluate, be, have | address, identify, select, use, inform, review | take, initiating, completing, exercise |
| Level 4 | use, address, analyse, interpret, evaluate, be, have | address, identify, adapt, use, initiate, inform, review | take, exercise |
| Level 5 | use, find, analyse, interpret, evaluate, be, understand | address, determine, adapt, use, inform, evaluate | take, planning, developing, exercise |
| Level 6 | refine, use, create, analyse, interpret, evaluate, understand, be | address, determine, refine, adapt, use, design, inform, evaluate | take, planning, developing, underpinning, initiate, lead, taking, exercise |
| Level 7 | reformulate, use, create, analyse, interpret, evaluate, produce, understand, affect | conceptualise, address, determine, use, design, undertake, inform, produce, evaluate | take, planning, developing, initiate, underpin, exercise, lead, taking |
| Level 8 | develop, create, analyse, interpret, evaluate, produce, understand, reconceptualise, extend, contributing, exercise, affect | conceptualise, address, formulate, use, initiate, design, undertake, extend, result, evaluate | take, planning, developing, have, result, exercise, sharing |

#### SL4 How progression is communicated
<!-- Each thread follows one quality up the levels: where the issuer changes its wording, the level is listed with the new wording (the issuer's words in quotation marks, otherwise our short reading). A level not listed keeps the wording of the level below. -->

- **The problem or context:** Entry 2: "simple, familiar"; Entry 3: "structured", "familiar contexts"; Level 1: "well-defined, routine"; Level 2: "straightforward problems"; Level 3: "well-defined" but "complex and non-routine"; Level 4: "well-defined but complex and non-routine"; Level 5: "broadly-defined, complex"; Level 6: "limited definition", "many interacting factors"; Level 7: "problematic situations"; Level 8: "lack definition", "many complex, interacting factors".
- **The knowledge drawn on:** Entry 2: "knowledge or understanding"; Level 1: "facts, procedures and ideas"; Level 2: "understanding of facts"; Level 3: "factual, procedural and theoretical"; Level 4: "practical, theoretical or technical"; Level 5: "technological"; Level 6: "conceptual"; Level 8: "original".
- **What is done with understanding:** Level 1: use; Level 5: use, to "find ways forward"; Level 6: refine, to "create ways forward"; Level 7: reformulate; Level 8: develop original.
- **The thinking verbs:** Entry 2: know; Level 1: be aware; Level 2: interpret; Level 3: interpret and evaluate; Level 4: analyse, interpret and evaluate; Level 6: critically analyse; Level 7: critically analyse ... to produce modified conceptions; Level 8: ... to produce new knowledge and theories.
- **The field:** Level 1: relevant information; Level 3: its nature; Level 4: its nature and approximate scope; Level 5: its nature and scope; Level 6: its context; current developments; Level 7: its wider contexts; Level 8: reconceptualise its wider contexts; extend it.
- **Perspectives:** Level 3: awareness; Level 4: informed awareness; Level 5: understand, with the reasoning; Level 6: understand, with the theories beneath; Level 7: theoretical and methodological perspectives; Level 8: critical understanding of them.
- **Methods:** Level 1: use relevant skills and procedures; Level 2: select and use; Level 3: identify, select and use; Level 4: identify, adapt and use; Level 5: determine, adapt and use; Level 6: determine, refine, adapt and use; Level 7: determine methodologies and approaches; Level 8: formulate methodologies.
- **Enquiry:** Level 2: gather information; Level 3: appropriate investigation; Level 4: initiate investigation; Level 5: use research or development; Level 6: design research where appropriate; Level 7: design and undertake research or strategy; Level 8: initiate, design and undertake research that extends the field.
- **Evaluation:** Level 1: whether actions worked; Level 2: how effective; Level 3: review effectiveness; Level 4: review effectiveness and appropriateness; Level 5: evaluate; Level 6: evaluate, with implications; Level 7: critically evaluate, short and long term; Level 8: ... for the field and its wider context.
- **Responsibility:** Entry 2: begin to take some, for outcomes; Level 1: completing tasks; Level 3: initiating tasks; supervising others; Level 4: courses of action; others' work; Level 5: planning and developing courses of action; Level 6: underpinning substantial change; leading; Level 7: initiating substantial change; leading complex tasks; Level 8: significant impact on the field; advancing professional practice.
- **Autonomy:** Entry 2: with appropriate guidance; Level 1: subject to direction or guidance; Level 2: some autonomy, under overall direction; Level 3: within limited parameters; Level 4: within broad but well-defined parameters; Level 5: within broad parameters; Level 6: broad autonomy; Level 7: across a significant area; Level 8: with leadership, as a leading practitioner or scholar.

#### SL5 Observations on the formulation
<!-- label: editorial; status: drafted; basis: primary -->
- **The form is fixed.** Every level uses the same three strands and the same sentence shape: an imperative verb, an object, and a qualifier of context or degree. Progression is carried almost wholly by the qualifiers and a few verbs, not by new kinds of sentence.
- **Verbs climb in a small ladder.** Thinking verbs go know, be aware, interpret, evaluate, analyse, critically analyse, then "produce modified conceptions" (Level 7) and "new knowledge and theories" (Level 8). Method verbs go use, select, identify, adapt, determine, refine, then "formulate" (Level 8).
- **Context does the most work.** The problem moves from "simple, familiar" through "well-defined, routine" and "complex and non-routine" to "limited definition", "problematic situations" and finally contexts that "lack definition". Each step loosens how much is given.
- **Responsibility and autonomy rise together but separately.** Responsibility widens in scope (outcomes, tasks, courses of action, change, the field); autonomy widens in limits (guidance, direction, limited, broad, across an area, leadership).
- **Some steps are small.** Levels 4 and 5, and 6 and 7, share most of their wording; the differences sit in one or two qualifiers per strand ("well-defined" to "broadly-defined"; "refine" to "reformulate"). These are the steps a progression model has to make most visible.
- **Higher education levels.** Levels 4 to 8 are the higher education levels the FHEQ shares (Frameworks 2024, 2.24); the comparison of the two sets of wording is the second layer Abbott asks for (std N-0058), after S-03.

## Part B Terminology
<!-- label: both; status: drafted; basis: primary -->
`not-applicable-by-design`: the document defines no terms.

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the document sets out levels, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: "unknown in the document (Abbott: CQFW)"
  title: Level Descriptors
  edition: January 2009
  year: 2009
  url: unknown
  retrieved: "PDF attached by Abbott, 2026-10-03, 03:47"
  licence: none stated
  tier: primary
  readVia: direct
  held: 3eda4e2cec5e9c8b11d5238db7885f013de6a0013daaada1b87d85cd402ee94d
  heldFiles: [wkspc2601-library/txt/welsh-government-2009-cqfw-level-descriptors-standard.txt, wkspc2601-library/txt/welsh-government-2009-cqfw-level-descriptors-standard.norm.txt, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, S4, S4a, S5, SL]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct; extracted by table cell with pdfplumber, normalised with stan's tool (word sequence equal)" }
- { ref: "std:doc:qaa-fheq-2024-framework, 2.23 and 2.24 (held, read for S-03)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "the CQFW's managing body and its relation to the FHEQ, for S1, S5 and S7" }
```

### D3 Wanted sources
```yaml
- { w: W-std-0019, citation: "the CQFW's own publication of these level descriptors, with its issuer, date, status and re-use terms, and any later edition", settles: [S1, S8], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- S1: the document names no issuer, framework or nation; CQFW rests on Abbott's word (03:47 and 04:03) and the PDF's metadata author (DfES - QLD, read as the Welsh Government's education department: inference). Its status (current or superseded), licence and any later edition are unknown (D3).
- S1: the same three strands and Entry 1 to Level 8 were used by England's Qualifications and Credit Framework; this text is taken as CQFW's on Abbott's word, not compared with the QCF's.
- S3, extraction: the PDF is a table; the text was taken cell by cell (pdfplumber), so the held text's line order is ours: level, strand heading, cell. pdftotext's reading order interleaved the columns and was not used.
- S4: statements are cut at sentences, the issuer giving no numbers within a cell; ids are ours (level/strand.n).
- S4: the source writes "well defined" and "well-defined", "non- routine" (a broken hyphen), "broadly- defined"; the held text keeps them as extracted.
- S4, force: `describes` for every descriptor; the imperative form ("Use...", "Take responsibility...") describes what achievement reflects and obliges no one.
- S5: no crosswalk: this document states none, and the framework variant records an equivalence only from its source (profile 0.1.5-draft, P5); the CQFW-FHEQ relation is the Frameworks 2024's to state (S-03).
- S4, the cut: the framework variant says a descriptor is cut "at its own headings" (P5, rule 3); this run cuts one step finer, one record per sentence within each heading, the sentences being separate descriptors and the unit the verb analysis needs. For Abbott (D-std-0005).
- SL: the section is proposed for the frameworks variant; its tables are built from S4 and need P3 like the rest.
- ST-12: versions here run short (7 to 37 words); the formulaic wording of level descriptors made close paraphrase copy nine-word runs (31 found and reworded).

---

## Change notes
- 0.2.1, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.2.0, 3 October 2026, 11:00: every statement record now carries the issuer's statement in full (`source`, taken from its span in the held text) beside our paraphrase and versions, for language analysis; private, never published (Abbott, 10:56 and 10:59; D-std-0014). No paraphrase changed.
- 0.1.1, 3 October 2026, 07:34: provenance lines added to Parts B and C; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.1.0: 2026-10-03: researched by run frame 0.1.1-draft and standards run layer 0.5.0-draft, std, run 0045 (P1).
