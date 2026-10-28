---
id: ing:doc:pathway-work-based-experiential-learning
title: Work-Based and Experiential Learning (academic skills pathway)
aliases: [work-based learning, practice-based learning, experiential learning, placement learning, path:work-based-experiential-learning]
subjectKind: framework
practices: [education]
primaryPractice: education
streams: [education/academic-skills]
extensions: [education]
parts:
  A: "partial: the capabilities are proposed, not yet confirmed"
  B: "partial: concepts and terms named by the model; associated vocabulary held as candidates"
  C: "full (loose)"
pins: { structure: 0.11.0-draft, template: 0.10.0-draft, pathwayTemplate: 0.3.0-draft, theory: 0.3.0-draft, terminology: 0.3.0-draft, process: 0.3.0-draft }
status: drafted
researchedBy: INGEST research prompt 0.1.10-draft, with the pathway block of META's `mta-nts-td-pathway-ingest.md` 0.1.1-draft (sections 2 and 2a)
passes:
  P1: 2 October 2026
  P2: not run; triggers 4 and 5 hold (Part E, item 1)
  P3: open
version: 0.1.11
---

<!-- from INGEST wpk-0016-ingest-pd-ingestion-document-template.md 0.10.0-draft; the specification is wpk-0016-ingest-pd-ingestion-document-structure.md -->
# Work-Based and Experiential Learning (academic skills pathway)

> **The core document.** Generic: it names no project that uses the pathway. Who made the model and where each claim comes from is in Part D. Companions, never ingested with it: **source maps**, one per guide (the first, for *Excelling at University*, held by `path`, draft), and **integrations**, one per consuming project (`integrations/<project>/`). A capability's level is `unknown` until a source sets it (D-ing-0001 (a)). Fill note from the template kept until P3.

## Part 0 Summary

### 0.1 Agent definition
<!-- brief: Two or three sentences for an agent: what this is and when to reach for it, and one thing it is not for. Write last, from the finished document. -->
<!-- label: editorial; status: drafted; basis: secondary -->
Work-Based and Experiential Learning is one of thirteen academic skills pathways: learning through practice settings such as placements, laboratories, studios, field work, simulation and apprenticeships, from knowing what these are, to working well in them, to learning from them by structured reflection and professional judgement. Reach for it to place, sequence or assess a capability for learning in or from practice, or to translate one into its workplace form. It is not the reflective method itself, which belongs to the Reflective Practice pathway it draws on.

### 0.2 Summary
<!-- brief: One paragraph: who proposed it, when, what it is, its main use and its main dispute. Write last. -->
<!-- label: both; status: drafted; basis: secondary -->
The academic skills pathways model (2026) sets Work-Based and Experiential Learning as one of thirteen pathways, drawn from a study skills guide's chapter on learning by doing. It climbs in three tiers: what practice- and work-based learning is and why it matters; making the most of it (immersion, conducting oneself as a professional, the mentor relationship, testing theory in practice); and learning from experience to a professional standard (Kolb's experiential learning cycle, reflective assessment of practice, professional judgement and decision-making). Its method is reflective practice, by cross-reference rather than merger. Its key theory is situated learning (Lave and Wenger): learning by taking part in a community of practice, from its edge towards full membership, which is what a placement and its mentor provide; Schön's reflection in and on action and Kolb's cycle sit beside it. Its open questions are about coverage: no proposed capability yet covers professional conduct or testing theory in practice (Part E).

## Part A Theory

### A1 Overview
<!-- brief: Authors, year, key publications (the original first), model type, and the defining characteristics as the authors give them. Name what it revised or replaced, if anything. -->
<!-- label: source; status: drafted; basis: primary -->
```yaml
authors: [see Part D]
year: 2026
keyPublications:
  - { key: PTM }
  - { key: TSPEC }
  - { key: EAU }
modelType: framework
audience: both
```
- Three tiers, Introductory, Intermediate and Advanced, each with a focus, content, a progression logic and links to other pathways (D:PTM, Pathway 11).
- It uses the Reflective Practice pathway as its method: a dependency handled by cross-reference, not a merger (D:PTM, Pathway 11).
- Tiers are anchored to experience of the practice, not to year of study (D:TSPEC, section 2).
- It became a pathway of its own when the model grew from nine to thirteen pathways (D:PTM, changes, v2).

### A2 Core principles
<!-- brief: One item per claim the theory rests on, each cited to the authors. Claims only, not uses or benefits. -->
<!-- label: source; status: drafted; basis: primary -->
- Practice- and work-based learning centres on professional practice: applying theory and knowledge in real or simulated work settings (D:EAU, p. 221).
- Its guiding principle is learning through experience; experience, in the sense of the actions one takes, is the currency of learning (D:EAU, pp. 223, 225).
- Simulated and workplace settings count equally as real-world learning (D:EAU, p. 223).
- The learning is structured and supported, and the mentor relationship can decide whether it succeeds (D:EAU, p. 224).
- Workplaces are complex, dynamic and unpredictable, so assessment moves beyond breaking practice into discrete skills and values judgement, decision-making and the reasons behind them (D:EAU, pp. 224-225).
- Assessment usually rests on reflective practice, usually built on Kolb's experiential learning cycle (D:EAU, p. 225).
- The progression is: understand the mode, engage professionally, then reflect on and learn from practice (D:PTM, Pathway 11).

### A3 Structure
<!-- brief: The spine: every component (level, dimension, stage, category) with its order, parent, the authors' definition (paraphrased, cited), our gloss, key language and an example of our own. Take most care here; other stores link to these components. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
structure: [ladder, set]
components:
  - { slug: introductory, componentType: level, order: 1, parent: none, name: "Introductory: what practice- and work-based learning is", authorsDefinition: "its value to personal development; the range of activities (placements, laboratory work, studios, field work, simulation, project-based learning, internships, apprenticeships) (D:PTM, Pathway 11)", gloss: "know the kinds of learning by doing and why they matter", keyLanguage: [placement, laboratory, studio, field work, simulation, internship, apprenticeship], examples: ["sorting a list of a course's activities into lab work, simulation and placement"], audience: both, beneficiaryGloss: "find out the different ways you learn by doing, and what you get from them", readingLevel: "plain English for a student entering higher education" }
  - { slug: intermediate, componentType: level, order: 2, parent: none, name: "Intermediate: making the most of it", authorsDefinition: "immersing yourself; conducting yourself as a professional; the mentor relationship; testing theory in practice (D:PTM, Pathway 11)", gloss: "work well in the setting and learn from the people in it", keyLanguage: [immersion, professional conduct, mentor, theory into practice], examples: ["agreeing goals with a placement mentor in the first week"], audience: both, beneficiaryGloss: "get stuck in, behave like a professional and use your mentor well", readingLevel: "plain English for a student entering higher education" }
  - { slug: advanced, componentType: level, order: 3, parent: none, name: "Advanced: reflecting on experience", authorsDefinition: "Kolb's experiential learning cycle applied; reflective assessment of practice; professional judgement and decision-making (D:PTM, Pathway 11)", gloss: "learn from what happened, to a professional standard", keyLanguage: [experiential learning cycle, reflective assessment, professional judgement, decision-making], examples: ["a reflection on a taught lesson on placement, structured by Kolb's four stages (D:EAU, pp. 226-228)"], audience: both, beneficiaryGloss: "use a reflection cycle to learn from your placement and explain your decisions", readingLevel: "plain English for a student entering higher education" }
  - { slug: work-based-experiential-learning-01, componentType: element, order: 1.1, parent: introductory, name: "Distinguish types of practice- and work-based learning", authorsDefinition: "proposed capability, tier note introduced (D:CARDS)", gloss: "tell the kinds of learning by doing apart", keyLanguage: [types, placement, simulation, apprenticeship], examples: [], audience: both, beneficiaryGloss: "know which kind of learning by doing you are in", readingLevel: "plain English for a student entering higher education" }
  - { slug: work-based-experiential-learning-02, componentType: element, order: 2.1, parent: intermediate, name: "Make effective use of a mentoring relationship while on placement", authorsDefinition: "proposed capability, tier note developed (D:CARDS)", gloss: "use your mentor's guidance to shape what you do", keyLanguage: [mentor, guidance], examples: [], audience: both, beneficiaryGloss: "ask your mentor for help and act on it", readingLevel: "plain English for a student entering higher education" }
  - { slug: work-based-experiential-learning-c1, componentType: element, order: 2.2, parent: intermediate, name: "Conduct oneself as a professional in a practice setting", authorsDefinition: "capability added by the model's author from the Intermediate tier's professional conduct (D:PTM, Pathway 11; D:EAU, p. 229; D-ing-0010)", gloss: "behave as someone already qualified would", keyLanguage: [professional conduct, conduct, professionalism], examples: ["a student teacher planning, teaching and following school policy as a qualified teacher would (D:EAU, p. 229)"], audience: both, beneficiaryGloss: "act the way a qualified person in that job would", readingLevel: "plain English for a student entering higher education" }
  - { slug: work-based-experiential-learning-c2, componentType: element, order: 2.3, parent: intermediate, name: "Test theoretical knowledge by applying it in practice and reflecting on the result", authorsDefinition: "capability added by the model's author from the Intermediate tier's testing theory in practice (D:PTM, Pathway 11; D:EAU, p. 229; D-ing-0010)", gloss: "try out what you learned and see what happens", keyLanguage: [theory, practice, application, test], examples: ["trying a questioning technique from a module in a lesson, then noting how pupils responded"], audience: both, beneficiaryGloss: "use an idea from your course for real and notice how it works", readingLevel: "plain English for a student entering higher education" }
  - { slug: work-based-experiential-learning-03, componentType: element, order: 3.1, parent: advanced, name: "Apply an experiential learning cycle to work-based learning", authorsDefinition: "proposed capability, tier note extended (D:CARDS)", gloss: "structure your learning from experience with a cycle", keyLanguage: [experiential learning cycle, Kolb], examples: [], audience: both, beneficiaryGloss: "use a learning cycle to make sense of what happened at work", readingLevel: "plain English for a student entering higher education" }
  - { slug: work-based-experiential-learning-04, componentType: element, order: 3.2, parent: advanced, name: "Exercise professional judgement and justify decision-making in a work-based setting", authorsDefinition: "proposed capability, tier note extended (D:CARDS)", gloss: "make good calls at work and say why", keyLanguage: [professional judgement, decision-making, rationale], examples: [], audience: both, beneficiaryGloss: "decide what to do at work and explain your reasons", readingLevel: "plain English for a student entering higher education" }
```

### A4 Concepts used
<!-- brief: The ideas the theory rests on that other theories share; each will become or match a TERMINOLOGY-DAT concept. -->
<!-- label: both; status: drafted; basis: primary -->
- practice-based-learning: learning by applying knowledge in practice settings (D:EAU, p. 221).
- work-based-learning: learning in or for a workplace (D:EAU, p. 221).
- experiential-learning: learning through experience (D:EAU, p. 225).
- mentor: the experienced practitioner who guides a learner in the setting (D:EAU, p. 224).
- professional-judgement: deciding well in complex, uncertain practice, with reasons (D:EAU, pp. 224-225).
- reflective-practice: the method by which practice learning is assessed (D:EAU, p. 225).
- authentic-learning: real-world experience, simulated or in the workplace (D:EAU, p. 223).
- professional-network: contacts made in practice that help towards employment (D:EAU, p. 224).
- transferable-skills: skills or competencies that carry across professional contexts (D:EAU, glossary, pp. x-xiii).
- placement: a period working in a professional setting as part of a programme, also called an industry placement (D:EAU, pp. 220, 222).
- internship: a period working directly in a professional environment to gain hands-on experience (D:EAU, p. 222).
- field-work: working off site in real-world settings, as on a dig or in a habitat (D:EAU, p. 222).
- simulation-based-training: working within scenarios that replicate real-world situations, as student nurses do (D:EAU, p. 222).
- workplace-observation: observing professionals at work to gain insight into tasks, dynamics and practices (D:EAU, p. 223).
- apprenticeship: a programme combining paid on-the-job learning with formal education and mentorship (D:EAU, p. 223).

Concepts above from `placement` on were added on 4 October 2026, 10:37: terms named in B2a or B4 that had no definition here (D-ing-0057).

### A5a How practitioners apply it
<!-- brief: From the practitioner's side: the steps they take, the tools and artefacts they use, a worked example, and the decisions they make along the way. Separate what the authors prescribe (source) from how it is done in practice (reported, with sources) and what follows from it (editorial). -->
<!-- label: both; status: drafted; basis: primary -->
Practitioners here are tutors, placement organisers, mentors, technicians and authors of learning material.

**What the authors prescribe** (source):
- Pitch a lesson to the whole tier at once (D:TSPEC, section 5).
- Assess judgement, decisions and their rationale rather than discrete skills (D:EAU, pp. 224-225).
- Structure reflection on practice with Kolb's cycle; a student teacher's placement reflection is the worked example (D:EAU, pp. 225-228).

**How it is done in practice** (reported):
- Mentors and supervisors who assess are often unpaid volunteers with high turnover, which makes recruiting and training them hard (D:EAU, p. 224; evidence: reported).
- Some practice learning includes an observed practical element, as in teacher training (D:EAU, p. 225; evidence: reported).
- UK guidance sets nine principles for work-based learning, including formal agreements between provider, employer and student, workplace supervision and partnership in design and review (D:QAAWBL; read by summary; evidence: claimed).

**Worked example**:
At Introductory, the learner sorts a list of activities into types; at Intermediate, they plan the first week of a placement with their mentor; at Advanced, they reflect on a decision they made on placement with Kolb's cycle and justify it (editorial).

### A5b How beneficiaries meet it
<!-- brief: From the beneficiary's side (learner, client, project team, stakeholder): what it asks of them, what they see or do, and any version made for them to use directly. Search for this separately. -->
<!-- label: both; status: drafted; basis: primary -->
- Five pieces of advice to the learner: immerse yourself; act as a professional; use those around you, especially your mentor; test theory in practice; keep a reflective mindset (D:EAU, p. 229; evidence: claimed).
- Learners may find it daunting at first (D:EAU, p. 229; evidence: claimed).
- Apprenticeships let learners earn while they study and often lead to employment (D:EAU, p. 223; evidence: claimed).

### A5c Contexts and adaptations
<!-- brief: Where it is used (levels, sectors, practices, settings, modes such as online), and how it has been adapted for them, each with its source. -->
<!-- label: both; status: drafted; basis: secondary -->
- STEM laboratory work; art and design studios; field work; simulation, as in nursing; project-based learning; industry placements and internships; professional practice courses designed with industry; workplace observation; apprenticeships (D:EAU, pp. 221-223).
- Vocational fields (nursing, teaching, social work) lean on it heavily and need discipline-aware examples beyond a general guide (D:PTM, cross-cutting notes).
- UK higher education: QAA advice and guidance on work-based learning, 2018 (D:QAAWBL; read by summary).
- Apprenticeships in England are built on occupational standards that set the knowledge, skills and behaviours for a role, now published by Skills England (D:SKE; read by summary).

### A5d Misapplications
<!-- brief: Common ways it is misused or misread, the evidence for each, and how to avoid it. -->
<!-- label: both; status: drafted; basis: primary -->
- Assessing practice as a checklist of separate skills, missing judgement in complex settings (D:EAU, p. 224; evidence: claimed); avoid by assessing decisions and their rationale.
- Treating the experience as enough without reflection (editorial, from D:EAU, p. 229); avoid by keeping a reflective mindset throughout.
- Undervaluing simulated or unusual experiences (D:EAU, pp. 223, 230; evidence: claimed); avoid by treating them as real-world learning.

### A6a Benefits to practitioners
<!-- brief: What those who apply it gain. Mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
- Links between courses and industry and professional practice (D:EAU, p. 229; evidence: claimed).

### A6b Benefits to beneficiaries
<!-- brief: Name the beneficiaries, then what reaches them and how it reaches them through the practitioner. Search for this separately; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students; later, employers and the people their practice serves.
- A feel for the workplace and evidence for a CV and job selection (D:EAU, p. 223; evidence: claimed).
- Theory made real by applying it; literacies such as communication and critical thought developed in context; better decision-making (D:EAU, pp. 223-224; evidence: claimed).
- Professional networks and progress towards professional recognition (D:EAU, p. 224; evidence: claimed).

### A7a Criticisms of the theory and its application
<!-- brief: Criticisms of the theory itself and of how practitioners apply it, with the evidence for each, marked measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: secondary -->
- none-stated: no published criticism of this pathway exists. Criticisms of Kolb's cycle are in its own document (META run 0008).
- (editorial) Two Intermediate topics had no capability; two added in P3 fill the gaps (Part E, item 3).

### A7b Effects on beneficiaries
<!-- brief: Name the beneficiaries, then the harms, costs or limits that reach them through the practitioner's use. Search for this separately, as for A6b; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students.
- Variable mentoring: a less conscientious or untrained mentor can weaken the experience (D:EAU, p. 224; evidence: claimed).
- Each workplace's culture makes standard assessment hard, so judgements of students can vary (D:EAU, p. 224; evidence: claimed).

### A8 Selection
<!-- brief: When to choose it over named alternatives, and what it suits badly. Our reading (editorial). -->
<!-- label: editorial; status: drafted; basis: secondary -->
Choose this pathway when the learning happens in or from a practice setting. For reflection as a discipline in its own right, choose `path:reflective-practice`, which this pathway uses as its method; for graduate identity and the move into work, `path:starting-progressing-succeeding`. It suits badly a learner with no practice setting to learn in.

### A9 Relations
<!-- brief: Other theories it revises, extends, derives from, contrasts with or competes with, each with a target id and a one-line note. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: derivedFrom, target: ing:doc:experiential-learning-kolb-1984, note: "Kolb's cycle is the Advanced tier's model (D:PTM, Pathway 11; D:EAU, pp. 225-228)" }
- { rel: derivedFrom, target: ing:doc:pathway-reflective-practice, note: "the pathway's method, by cross-reference (D:PTM, Pathway 11)" }
- { rel: derivedFrom, target: ing:doc:situated-learning-lave-wenger-1991, note: "the key theory: Lave and Wenger (1991), situated learning and legitimate peripheral participation in a community of practice; explains the mentor, immersion and the move to full participation; META INGEST run 0033 (Part E, item 4)" }
- { rel: derivedFrom, target: ing:doc:reflective-practitioner-schon-1983, note: "reflection in and on action in professional practice; a theory the pathway rests on beside situated learning" }
```

### A10 Extension fields
<!-- brief: The practice extension fields for each practice in the front matter, and no others. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
education:
  domain: "cognitive, affective and psychomotor (practical and professional settings) (D:EAU, pp. 221-225)"
  verbs: none-stated
  learnerLevel: "higher education, any year; tiers anchored to experience of practice learning (D:TSPEC, section 2)"
pathway:
  id: path:work-based-experiential-learning
  title: Work-Based and Experiential Learning
  definition: "Learning in and from practice settings (placements, laboratories, studios, field work, simulation, projects and apprenticeships): knowing these modes, working well in them with a mentor's guidance, and learning from experience through structured reflection and professional judgement."
  terms:
    direct: [placement, field work, fieldwork, lab work, laboratory, work-based, experiential, work experience, practicum, internship, live project, apprenticeship, practice-based, real world, in practice, applied practice, practice setting, professional practice, in the workplace]
    associated: [simulation, studio, mentor, workplace observation, professional judgement, experiential learning cycle]
    source: "direct: the pathway term list v1.0 (D:TERMS; its 20 patterns written as words, one listed twice); associated: candidates from D:EAU and D:PTM (B2b); the term list's ruled second version, not yet in force, drops practicum; associated widened from the guide's glossary and the model's tier text (D-ing-0050)"
  competencies:
    - id: work-based-experiential-learning/01
      tierNote: introduced
      statement: Distinguish types of practice- and work-based learning.
      level: unknown
      verbs: [distinguish]
      theory: [ing:doc:situated-learning-lave-wenger-1991]
      process: [{none: "an understanding, not a process"}]
      professional:
        - statement: Recognises the forms of learning at work (on-the-job training, shadowing, apprenticeship, continuing development) and uses them.
          equivalence: partial
          gap: "the professional form is about finding learning within a job; the academic one about the modes a course offers"
          frameworks: ["Skills England occupational standards (knowledge, skills and behaviours)"]
    - id: work-based-experiential-learning/02
      tierNote: developed
      statement: Make effective use of a mentoring relationship while on placement.
      level: unknown
      verbs: [make use, use]
      theory: [ing:doc:situated-learning-lave-wenger-1991]
      process: [{needed: "a process for working with a mentor on placement"}]
      professional:
        - statement: Uses supervision and mentoring to develop in a role.
          equivalence: partial
          gap: "the professional relationship runs over years and may be line management; the placement one is short and partly assessed"
          frameworks: ["QAA work-based learning guidance (2018): roles, responsibilities and support", "Social Work England professional standards 4.2"]
    - id: work-based-experiential-learning/c1   # proposed; the model assigns the number
      tierNote: developed
      statement: Conduct oneself as a professional in a practice setting.
      level: unknown
      verbs: [conduct oneself, conduct]
      theory: [ing:doc:situated-learning-lave-wenger-1991]
      process: [placement-cycle]
      professional:
        - statement: Meets the conduct, values and standards expected in the role.
          equivalence: partial
          gap: "the professional form is bound by a code and carries sanctions; the academic one is practised under supervision"
          frameworks: ["QAA work-based learning guidance (2018): applying knowledge, skills and professional behaviours", "Skills England occupational standards: behaviours"]
    - id: work-based-experiential-learning/c2   # proposed; the model assigns the number
      tierNote: developed
      statement: Test theoretical knowledge by applying it in practice and reflecting on the result.
      level: unknown
      verbs: [test, apply, reflect]
      theory: [ing:doc:experiential-learning-kolb-1984]
      process: [placement-cycle, experiential-learning-cycle]
      professional:
        - statement: Applies evidence and theory to practice and reviews what works.
          equivalence: partial
          gap: "the professional form answers to outcomes for others and to evidence-based practice; the academic one to a learning task"
          frameworks: ["QAA work-based learning guidance (2018): applying knowledge", "HCPC standards of proficiency: reflect on and review practice"]
    - id: work-based-experiential-learning/03
      tierNote: extended
      statement: Apply an experiential learning cycle to work-based learning.
      level: unknown
      verbs: [apply]
      theory: [ing:doc:experiential-learning-kolb-1984]
      process: [experiential-learning-cycle]
      professional:
        - statement: Learns from work experience through structured reflection and records it as development.
          equivalence: partial
          gap: "the professional form is often required and recorded for a regulator; the academic one is assessed on a placement"
          frameworks: ["NMC revalidation", "HCPC standards of proficiency: reflect on and review practice"]
    - id: work-based-experiential-learning/04
      tierNote: extended
      statement: Exercise professional judgement and justify decision-making in a work-based setting.
      level: unknown
      verbs: [exercise, justify]
      theory: [ing:doc:situated-learning-lave-wenger-1991]
      process: [{needed: "a process for professional decision-making"}]
      professional:
        - statement: Makes and justifies decisions within the scope of a role and its standards.
          equivalence: partial
          gap: "the professional form carries accountability and consequences for others; the academic one is supervised and assessed"
          frameworks: ["QAA work-based learning guidance (2018): applying knowledge, skills and professional behaviours", "Skills England occupational standards: behaviours"]
  external:
    - { framework: "QAA Advice and Guidance: Work-based Learning (2018)", match: ["guiding principles 1 to 9"], equivalence: broader }
    - { framework: "Skills England occupational standards", match: ["knowledge, skills and behaviours"], equivalence: broader }
    - { framework: "Advance HE Embedding Employability framework", match: [unknown], equivalence: unknown }
    - { framework: "ESCO", match: [unknown], equivalence: unknown }
  processes: [experiential-learning-cycle, placement-cycle]
  templates: [GD-edu-12 Reflective account, "placement learning agreement (proposed)", "placement log (proposed)"]
```
`equivalence` says how the professional form relates to the capability (META D-0175's scale). Every crosswalk item is editorial: its frameworks were read by summary only (Part E, item 1).

### A11 Progression by level
<!-- brief: How the practice develops across qualification levels 3 to 8, deconstructed at each level into skills, competencies, understandings and literacies (after Lea and Street); level 8 in full; each entry says what changes from the level below; grounded in level descriptors and the key theory. From META's pathway template 0.3.0-draft. -->
<!-- label: both; status: drafted; basis: secondary -->
Each level also carries a metacognitive statement (D-ing-0038, D-ing-0039): what the learner understands about the practice in general and its application, and their stance towards it, on a ladder from applying it because they must (compliance), through knowing why (purpose), investment, ownership and confidence (ownership), to adapting it to personal goals (adaptation) and practising it fluently, applied and communicated as a mode of doing and expression in the service of the disciplinary community (flow). The practice described is learning in and through practice and work, never the pathway's tiers. Each level's understandings end with what the practice means for the learner's own development (D-ing-0036). The descriptors were read by summary only (Part E). Movement from the edge of a community of practice towards full participation follows Lave and Wenger's legitimate peripheral participation (1991, META run 0033); learning from experience follows Kolb's cycle (META run 0008).
```yaml
progression:
  levelFramework: "qualification levels 3 to 8: CQFW and RQF numbering; FHEQ levels 4 to 8"
  levels:
    - level: 3
      context: "a learner entering higher education: level 3 vocational study, work experience, a first placement"
      skills: ["follow workplace instructions and routines", "describe the tasks one did and what one learnt"]
      competencies: ["completes well-defined tasks in a setting under close supervision"]
      understandings: ["learning happens in the doing, not only in the classroom", "for own development: a placement shows what one can already do and what one cannot yet"]
      literacies: ["a placement diary or log of tasks"]
      metacognition: { stance: compliance, statement: "Takes part because the course requires it; sees the placement as tasks to get through." }
      changesFromBelow: not-applicable-by-design
      sources: [CQFW, LAVEWENGER]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 4
      context: "the first year of higher education"
      skills: ["identify the kind of practice-based learning on offer (placement, lab, studio, field work, simulation)", "conduct oneself professionally: punctuality, communication, confidentiality", "ask a mentor for guidance and feedback"]
      competencies: ["takes part in real but limited tasks at the edge of the practice (peripheral participation)"]
      understandings: ["a setting has its own community, norms and ways of talking", "for own development: practice-based learning builds skills and confidence that study alone does not"]
      literacies: ["a learning log; a short reflective account of the experience"]
      metacognition: { stance: purpose, statement: "Knows why practice-based learning matters and begins to notice what they learn from people and tasks; still waits to be told what to do." }
      changesFromBelow: "from following instructions to taking part, with professional conduct and a mentor relationship"
      sources: [FHEQ, LAVEWENGER, QAAWBL]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 5
      context: "developing practice, depending on the student: the second year, a sandwich year, a longer placement"
      skills: ["immerse oneself and take initiative within a role", "test theory against practice", "use Kolb's cycle to learn from an experience"]
      competencies: ["carries growing responsibility for tasks with supervision; works with colleagues as a member of a team"]
      understandings: ["theory and practice inform and challenge each other", "for own development: the placement is where one begins to see oneself as a practitioner, not only a student"]
      literacies: ["a placement learning agreement; a reflective report linking practice to theory"]
      metacognition: { stance: investment, statement: "Invests in the setting, taking initiative and testing theory; begins to see themselves as a practitioner in the making." }
      changesFromBelow: "from taking part to taking initiative and testing theory, with experience turned into learning through a cycle"
      sources: [FHEQ, KOLB, LAVEWENGER]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 6
      context: "independent practice: the final undergraduate year, final placements, apprenticeships at degree level"
      skills: ["make professional judgements and decisions in context", "reflect on practice to a professional standard", "evaluate one's own performance against a profession's standards"]
      competencies: ["works with limited supervision and is accountable for decisions within a role (fuller participation)"]
      understandings: ["professional judgement rests on knowledge, values and experience together", "for own development: one's readiness for professional practice and its standards can be judged and evidenced"]
      literacies: ["a reflective assessment of practice; a portfolio of evidence against professional standards"]
      metacognition: { stance: ownership, statement: "Owns their professional conduct and judgement, confident to decide and to account for decisions; learns from experience as a matter of course." }
      changesFromBelow: "from supervised initiative to accountable professional judgement, assessed against standards"
      sources: [FHEQ, SCHON, LAVEWENGER]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 7
      context: "advanced practice: master's study, professional and practice master's, work-based projects"
      skills: ["apply research and critical perspectives to professional situations", "lead or improve practice within an organisation", "design a work-based project"]
      competencies: ["acts as a full participant who shapes the practice and supports newcomers"]
      understandings: ["practice and its knowledge can be researched and changed", "for own development: one's practice becomes a site of inquiry for career-long development"]
      literacies: ["a work-based project report; a practice-based dissertation"]
      metacognition: { stance: adaptation, statement: "Adapts practice to new settings and personal goals, changes how things are done, and communicates practice knowledge to colleagues and newcomers." }
      changesFromBelow: "from accountable practice to changing practice, using research and critique"
      sources: [FHEQ, QAAMSC, LAVEWENGER]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 8
      context: "doctoral practice: an original contribution to knowledge, the researcher's identity and independence; professional doctorates"
      skills: ["research one's own professional practice to make an original contribution", "bring new knowledge back into the practice and the community"]
      competencies: ["makes original knowledge from and for practice, as a researcher and a practitioner at once"]
      understandings: ["practice-based doctorates unite original research with professional development", "for own development: the researcher-practitioner identity is itself developed and examined in the work"]
      literacies: ["a professional doctorate thesis or portfolio; publication to practitioner and academic audiences"]
      metacognition: { stance: flow, statement: "Practice is a mode of doing and expression, fluent and in the flow; they research and change it, communicating what they learn in the service of their professional and disciplinary community." }
      changesFromBelow: "a different kind, not more of level 7: the practitioner makes original knowledge, and the community's practice changes because of it"
      sources: [QAADOC, VITAE, FHEQ]
      provenance: { label: both, status: drafted, basis: secondary }
```

## Part B Terminology

### B1 Concepts
<!-- brief: One concept per idea that has a name in this theory (each A3 component, each A4 concept): plain definition, scope note, category, practices. -->
<!-- label: both; status: drafted; basis: primary -->
By rule: one concept per A3 tier and per A4 concept, definition as A3's gloss or A4's line. The exceptions:
```yaml
- slug: practice-based-learning
  definition: learning by applying knowledge in real or simulated practice settings
  beneficiaryDefinition: "learning by doing the work, for real or in a realistic setting"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "covers laboratories, studios, field work, simulation and projects; work-based learning is its workplace form"
  category: approach
  practices: [education]
- slug: mentor
  definition: an experienced practitioner who guides, supports and often assesses a learner in a practice setting
  scopeNote: "may be a supervisor, technician or qualified professional"
  category: role
  practices: [education]
```

### B2a Terms named by the authors
<!-- brief: Every name the authors give a concept: preferred and admitted forms, their alternative names and spelling variants, in full (no compact rule); part of speech, register, extension fields. -->
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: practice-based-learning, form: practice-based learning, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: work-based-learning, form: work-based learning, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: experiential-learning, form: experiential learning, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: experiential-learning, form: learning by doing, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: placement, form: placement, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: placement, form: industry placement, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: internship, form: internship, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: field-work, form: field work, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: field-work, form: fieldwork, lang: en, partOfSpeech: noun, termStatus: admitted, register: general }
- { concept: simulation-based-training, form: simulation-based training, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: apprenticeship, form: apprenticeship, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: workplace-observation, form: workplace observation, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: mentor, form: mentor, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: professional-judgement, form: professional judgement, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: transferable-skills, form: transferable skills, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
```

Glossary terms placed in this pathway (D:EAU, glossary, pp. x-xiii; D-ing-0050): transferable skills; added here: transferable skills.
`usableIn` and `bannedIn`: none-stated. Education extension: `sourceType` is `book` for every term from D:EAU; the rest unknown.

### B2b Associated vocabulary
<!-- brief: The wider vocabulary practitioners reach for (for Bloom, the verb lists), from at least two named secondary sources, with a scholarly analysis of such lists where one exists. Where none exists, list the words as candidates and put the glossary wanted in D3. One membership per component a word is placed in, with its sources and agreement weight; record where sources disagree with the authors. Never store similarity between words: it is computed from embeddings at query time. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
- { concept: practicum, form: practicum, frameworkBlocks: [{ component: introductory, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: live-project, form: live project, frameworkBlocks: [{ component: introductory, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: work-experience, form: work experience, frameworkBlocks: [{ component: introductory, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: knowledge-skills-behaviours, form: knowledge, skills and behaviours, frameworkBlocks: [{ component: advanced, sources: [SKE], weight: 1/1 }], status: candidate }
- { concept: simulation, form: simulation, frameworkBlocks: [{ component: introductory, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: studio, form: studio, frameworkBlocks: [{ component: introductory, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: project-based-learning, form: project-based learning, frameworkBlocks: [{ component: introductory, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: experiential-learning-cycle, form: experiential learning cycle, frameworkBlocks: [{ component: advanced, sources: [PTM], weight: 1/1 }], status: candidate }
```
No glossary of work-based learning vocabulary was consulted; one is wanted (D3).

### B3 Framework blocks
<!-- brief: For each concept this theory defines its own way: the A3 component, this theory's definition (cited) and its use here. -->
<!-- label: source; status: drafted; basis: primary -->
By rule: each tier concept's framework block is its A3 component and definition. The exception:
```yaml
- { concept: professional-judgement, component: advanced, definitionHere: "what tutors value in practice assessment, with the reasons behind it (D:EAU, pp. 224-225)", useHere: "the Advanced tier's assessed capability" }
```

### B4 Relations
<!-- brief: Broader, narrower, related, contrasts-with and the order within this theory, between the B1 concepts. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: higher-level-than, from: intermediate, to: introductory, note: "tier order" }
- { rel: higher-level-than, from: advanced, to: intermediate, note: "tier order" }
- { rel: broader, from: practice-based-learning, to: work-based-learning, note: "work-based learning is the workplace form" }
- { rel: broader, from: experiential-learning, to: practice-based-learning, note: "experiential learning embraces both (D:EAU, p. 225)" }
- { rel: narrower, from: placement, to: work-based-learning, note: "one mode" }
- { rel: narrower, from: apprenticeship, to: work-based-learning, note: "one mode" }
```

### B5 Rules
<!-- brief: Our rules on using the terms (such as a verb banned in outcomes), each with its reason. Editorial. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- understand, know, appreciate, be aware of: not used in learning outcomes at any tier, because they name no observable operation (D:TSPEC, section 6).

## Part C Process

### C0 Formality
<!-- brief: Decide first: prescribed, recommended, loose, implied or not applicable, with one sentence on why. If not applicable, stop Part C. -->
<!-- label: both; status: drafted; basis: primary -->
`loose`: the guide gives advice for getting the most out of practice learning and recommends Kolb's cycle for reflecting on it, but sets no fixed procedure for a placement (D:EAU, pp. 225-229).

### C1 Process models
<!-- brief: Each process the theory lends itself to: what it achieves, shape, scale, what starts it and what counts as done. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: placement-cycle
  summary: prepare for, take part in and learn from a period of practice learning
  shape: cyclic
  scale: [task, course]
  scaleNote: "a placement or internship for a set period (D:EAU, p. 222)"
  groundedIn: [ing:doc:pathway-work-based-experiential-learning]
  entry: a placement, project or practice period begins
  exit: a reflective account and actions for the next experience
  inferred: true
```
Reflection on the experience follows `experiential-learning-cycle` (Kolb, META run 0008).

### C2 Stages
<!-- brief: Each stage in order: purpose, inputs, activities, outputs, roles, the gate that ends it. Mark our arrangement editorial where the authors give no stages, and every activity the sources do not name `inferred: true`. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { model: placement-cycle, order: 1, name: Prepare, purpose: "know the setting and agree what to learn", inputs: [], activities: [read about the setting, agree goals with the mentor], outputs: [placement-agreement], roles: [student, mentor, tutor], endsAt: none, repeat: none, audience: both, inferred: true }
- { model: placement-cycle, order: 2, name: Engage, purpose: "immerse, act as a professional, test theory in practice (D:EAU, p. 229)", inputs: [placement-agreement], activities: [immerse yourself, act as a professional, use the mentor, test theory], outputs: [placement-log], roles: [student, mentor], endsAt: none, repeat: none, audience: both }
- { model: placement-cycle, order: 3, name: Reflect, purpose: "draw meaning from the experience with Kolb's cycle (D:EAU, pp. 225-228)", inputs: [placement-log], activities: [experiencing, reflecting, thinking, acting], outputs: [reflective-account], roles: [student], endsAt: practice-assessment, repeat: "the next placement or experience", audience: both }
```

### C3 Gates
<!-- brief: Each decision point with criteria that can pass or fail, and what it decides. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
- slug: practice-assessment
  criteria: ["judgement and decisions shown, with their rationale (D:EAU, pp. 224-225)", "reflection on performance with actions (D:EAU, p. 225)"]
  decides: go
  variationPoint: yes
```

### C4 Outputs
<!-- brief: Each product a stage makes: purpose, parts, and what a template for it needs to know. Mark every output the sources do not name `inferred: true`. Where the method names its own document types, record every one complete (purpose, composition, derivation, quality criteria) from its product descriptions; our templates are drafted from those parts, never the method's text copied. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: placement-agreement, purpose: "agree roles, goals and support", parts: [goals, roles, support, practicalities], producedBy: [1], usedBy: [2], templateHint: "UK guidance expects formal agreements between provider, employer and student (D:QAAWBL)", audience: both, inferred: true }
- { slug: placement-log, purpose: "record experiences to reflect on later", parts: [date, what happened, notes], producedBy: [2], usedBy: [3], templateHint: "brief, regular entries", audience: beneficiary, inferred: true }
- { slug: reflective-account, purpose: "an assessed reflection on practice", parts: [experiencing, reflecting, thinking, acting], producedBy: [3], usedBy: [practice-assessment], templateHint: "COMPOSE GD-edu-12; John's account is a model (D:EAU, pp. 226-228)", audience: both }
```

### C5 Roles
<!-- brief: Who does each stage, from both sides: practitioner roles and beneficiary roles. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: student, responsibilities: [take part, act professionally, reflect], stagesInvolved: [1, 2, 3] }
- { slug: mentor, responsibilities: [guide, support, often assess], stagesInvolved: [1, 2, practice-assessment] }
- { slug: tutor, responsibilities: [prepare, assess reflection, observe where practical], stagesInvolved: [1, practice-assessment] }
- { slug: employer, responsibilities: [host, agree the placement], stagesInvolved: [1], inferred: true }
```

### C6 Variation points
<!-- brief: Where the process can be tailored or branch, by gate. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- practice-assessment: some settings add an observed practical element, as in teaching; the reflective model may be set by the profession.
- Every tier: the setting (lab, studio, field, ward, school, firm) changes the experiences, never the demand.

### C7 Extension fields
<!-- brief: The practice extension fields for each practice in the front matter, and no others. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
education:
  alignmentRole: [activity, assessment]
```

## Part D Sources
<!-- brief: Every cited source with full citation, tier, licence and how it was read (`readVia`). Original works first. -->
```yaml
- { key: PTM, author: "Abbott, S.", title: "Academic skills pathways model: pathway tier mapping, Draft v3 (v3.1)", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [0.2, A1, A2, A3, A5c, A8, A9] }
- { key: TSPEC, author: "Abbott, S.", title: "Academic skills pathways model: tier specification v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A1, A5a, A10, B5] }
- { key: CARDS, author: "Abbott, S.", title: "Academic skills pathways model: capability cards with tier notes, proposed", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A3, A10] }
- { key: TERMS, author: "Abbott, S.", title: "Academic skills pathways model: pathway term list v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A10, B2b] }
- { key: EAU, author: "Dennis, C. and Abbott, S.", title: "Excelling at University: Academic Literacies and the Development of Graduate Identity", edition: 1st, year: 2026, publisher: Routledge, licence: copyright, tier: primary, readVia: direct, held: not held, citedIn: [A2, A3, A4, A5a, A5b, A5c, A5d, A6a, A6b, A7b, A10, B3, B4, C0, C1, C2, C3, C4] }
- { key: QAAWBL, author: QAA, title: "UK Quality Code, Advice and Guidance: Work-based Learning", year: 2018, publisher: QAA, tier: professional, readVia: summary, held: not held, citedIn: [A5a, A5c, A10, C4] }
- { key: SKE, author: Skills England, title: "Developing an occupational standard (guidance)", year: unknown, publisher: UK Government, tier: web, readVia: summary, held: not held, citedIn: [A5c, A10, B2b] }
- { key: FHEQ, author: Quality Assurance Agency for Higher Education, title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies, 2nd edn (level descriptors unchanged from 2014)", year: 2024, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:qaa-fheq-2024-framework, META, SHA-256 prefix 97c52675225e" }
- { key: CQFW, author: Welsh Government, title: "Credit and Qualifications Framework for Wales: level descriptors", year: 2009, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:welsh-government-cqfw-2009-framework, META, SHA-256 prefix 682642ca28c8" }
- { key: QAAMSC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Master's Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: QAADOC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Doctoral Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: VITAE, author: Vitae, title: "Researcher Development Framework", year: 2010, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: LAVEWENGER, author: "Lave, J. and Wenger, E.", title: "Situated Learning: Legitimate Peripheral Participation", year: 1991, publisher: Cambridge University Press, tier: secondary, readVia: inherited, held: not held, citedIn: [A9, A11] }
- { key: KOLB, author: "Kolb, D. A.", title: "Experiential Learning: Experience as the Source of Learning and Development", year: 1984, publisher: Prentice Hall, tier: secondary, readVia: inherited, held: not held, citedIn: [A11] }
- { key: SCHON, author: "Schön, D. A.", title: "The Reflective Practitioner: How Professionals Think in Action", year: 1983, publisher: Basic Books, tier: secondary, readVia: inherited, held: not held, citedIn: [A11] }
```

### D2 Research log
<!-- brief: Every source opened, used or not, as you open it. -->
```yaml
- { ref: PTM, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: Pathway 11" }
- { ref: TSPEC, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: anchoring" }
- { ref: CARDS, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: four capabilities with tier notes" }
- { ref: TERMS, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: 20 patterns, one duplicated" }
- { ref: EAU, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: Ch 12 pp. 220-230" }
- { ref: QAAWBL, tier: professional, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: definition and nine principles" }
- { ref: SKE, tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: occupational standards as knowledge, skills and behaviours; Skills England publishes them" }
- { ref: "https://www.gla.ac.uk/myglasgow/learningandteaching/studentskills/abouttheframework", tier: web, consulted: 2026-10-02, pass: P1, outcome: "set aside: Glasgow's own framework, not Advance HE's" }
- { ref: "META run 0008 (front matter, C1)", tier: scholarly, consulted: 2026-10-02, pass: P1, outcome: "used: id and process slug" }
- { ref: "FHEQ, CQFW, QAA characteristics statements, Vitae RDF", tier: web, consulted: 2026-10-03, pass: P1, outcome: "used, by summary, as for Reflective Practice's A11 (its D2 lists the pages)" }
```

### D3 Wanted sources
<!-- brief: Every source needed and not reached, with what it would settle; ask Abbott when one blocks a section. -->
```yaml
- { id: W-0013, citation: "QAA (2018) UK Quality Code, Advice and Guidance: Work-based Learning, read direct", settles: [A5a, A5c, A10], asked: not yet, state: wanted }
- { id: W-0014, citation: "Advance HE (2019) Embedding Employability in Higher Education framework, read direct", settles: [A10], asked: not yet, state: wanted }
- { id: W-0015, citation: "Lave, J. and Wenger, E. (1991) Situated Learning: Legitimate Peripheral Participation. Cambridge University Press", settles: [A9, B2b], asked: not yet, state: received (META run 0033, 3 October 2026) }
- { id: W-0031, citation: "QAA (2024) FHEQ, 2nd edn, read direct (the level descriptors)", settles: [A11], asked: not yet, state: received (META std:doc:qaa-fheq-2024-framework, 3 October 2026) }
- { id: W-0032, citation: "CQFW level descriptors, current edition, read direct", settles: [A11], asked: not yet, state: received (META std:doc:welsh-government-cqfw-2009-framework, 3 October 2026) }
- { id: W-0033, citation: "QAA (2020) Characteristics Statements: Master's and Doctoral Degree, read direct", settles: [A11], asked: not yet, state: wanted }
- { id: W-0034, citation: "Vitae (2010) Researcher Development Framework, read direct", settles: [A11], asked: not yet, state: wanted }
```

## Part E Gaps and questions
<!-- brief: Every unknown, conflict and point for Abbott, as it arises. -->
1. **P2 triggers:** 4 and 5: the external frameworks were read by summary only (W-0013, W-0014). The crosswalk is editorial.
2. **Levels:** `unknown` for every capability (D-ing-0001 (a)).
3. **Capability coverage:** settled. Two capabilities added by the model's author (D-ing-0010 (a), Abbott, 22:14): c1 "Conduct oneself as a professional in a practice setting" and c2 "Test theoretical knowledge by applying it in practice and reflecting on the result" (both Intermediate), with temporary ids until the model numbers them.
4. **Theory links:** settled (D-ing-0011, Abbott, 22:24): Lave and Wenger's situated learning (1991) is the key theory, queued at META's ing; Schön (run 0031) and Kolb (run 0008) are linked beside it. Whether the model's tier text should name situated learning is for the model (W-0015).
5. **Term list:** one pattern (`real world`) is listed twice; harmless here, a fault in the list for its holder.
6. **Templates:** a placement learning agreement and a placement log are proposed, not in COMPOSE's catalogue.
7. **Source map:** what *Excelling at University* teaches for each capability belongs in its guide map (held by `path`, draft), not here.
8. **Progression by level (A11):** drafted 02:36 (J-ing-0001; META D-0205; shape D-ing-0035, D-ing-0036). Every level was read by summary only (W-0031 to W-0034); the entries are editorial readings of the descriptors and the pathway's theory. Lave and Wenger's run 0033 is now linked in A9 (the key theory, D-ing-0011).
9. **Report writing:** settled (D-ing-0024, amended by D-ing-0044, Abbott, 06:19): this pathway has one lesson on report writing somewhere in its series: a brief outer shell of the characteristics of a report, with the context defining the report it teaches, general or subject-specific. How the lesson is built belongs to each consumer, not to this document. The research and laboratory report are taught in Researching and Research Methods, the professional-practice reflective report in Reflective Practice; Academic Writing refers to all three. The guide treats the science and business report (pp. 160-161), which a context may use. [Was, 06:04 to 06:19: settled (D-ing-0024 (a), Abbott, 06:04): this pathway teaches the business report (executive summary, findings, recommendations, for a reader who must act) and the incident report (what happened, when, who was involved, what was done, factual and timely); the research and laboratory report go to Researching and Research Methods; Academic Writing signposts both. No capability names them yet; a candidate for the model's author: "Write a business or incident report for a workplace audience" (Intermediate or Advanced). The guide treats the business report (pp. 160-161); the incident report is not in the guide.]
10. **Vocabulary (D-ing-0050, Abbott, 11:10):** swept. The guide's glossary terms for this pathway are in B2a (and A4 where new); candidates from the model's tier text are in B2b; A10's direct terms are the term list v1.0 patterns as words, with the ruled second version's changes noted. The search patterns themselves are kept with each consuming project, not here. No published glossary of this pathway's vocabulary has yet been read; B2b stays candidates.

---

## Change notes
- 0.1.11: 4 October 2026, 10:37: A4 gains 6 definitions for terms named in B2a or B4 without one, found by compiling the terminology database (D-ing-0057; ing N-0119).
- 0.1.10: 4 October 2026, 10:03: A10 cards corrected (D-ing-0056): verbs matched to each statement, theory filled from the ruled A9 theory, cards with no process marked as needing one or as not a process (ing N-0113).
- 0.1.9: 3 October 2026, 11:10: vocabulary sweep: 1 glossary terms added to B2a (1 new concepts in A4), 4 candidates to B2b, A10 source note, Part E item 10 (D-ing-0050; ing N-0100).
- 0.1.8: 3 October 2026, 06:19: Part E item 9: a context-defined report writing lesson replaces the business and incident report; the capability candidate withdrawn (D-ing-0044; ing N-0093).
- 0.1.7: 3 October 2026, 06:04: Part E item 9: the business and incident report taught here; a capability candidate (D-ing-0024 (a); ing N-0091).
- 0.1.6: 3 October 2026, 05:52: META runs linked: FHEQ and CQFW linked to META's standards runs; W-0031 and W-0032 received (J-ing-0002; ing N-0089).
- 0.1.5: 3 October 2026, 04:41: file renamed to `ingest-path-work-based-experiential-learning.md`; the id is unchanged (ing N-0083).
- 0.1.4: 3 October 2026, 02:49: A11: each level gains a metacognitive statement and stance, compliance to flow (D-ing-0038, D-ing-0039; ing N-0081).
- 0.1.3: 3 October 2026, 02:36: A11 progression by level, levels 3 to 8, with own-development understandings; level descriptors by summary; W-0031 to W-0034; Part E item 8; key theory run linked in A9 and `theory:` (J-ing-0001; META D-0205; D-ing-0035; D-ing-0036; ing N-0078).
- 0.1.2: 2 October 2026, 22:24: theory links: Lave and Wenger key, Schön and Kolb beside (D-ing-0011; ing N-0032; G-ing-0027): 0.2, A9, D3 and Part E item 4.
- 0.1.1: 2 October 2026, 22:14: two capabilities added, c1 and c2 (D-ing-0010 (a); ing N-0031; G-ing-0025): A3, A7a, A10 and Part E item 3.
- 0.1.0: 2 October 2026, 22:12: researched by INGEST research prompt 0.1.10-draft with META's pathway block 0.1.1-draft; generic core from the start (ing N-0029; G-ing-0022).
