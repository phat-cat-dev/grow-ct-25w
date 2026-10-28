---
id: ing:doc:pathway-reflective-practice
title: Reflective Practice (academic skills pathway)
aliases: [reflective practice, path:reflective-practice, reflection as a professional discipline]
subjectKind: framework
practices: [education]
primaryPractice: education
streams: [education/academic-skills]
extensions: [education]
parts:
  A: "partial: the capabilities are proposed, not yet confirmed; no evidence yet of learners' experience of the pathway"
  B: "partial: concepts and terms named by the model; associated vocabulary held as candidates"
  C: "full (recommended)"
pins: { structure: 0.11.0-draft, template: 0.10.0-draft, pathwayTemplate: 0.3.0-draft, theory: 0.3.0-draft, terminology: 0.3.0-draft, process: 0.3.0-draft }
status: drafted
researchedBy: INGEST research prompt 0.1.10-draft, with the pathway block of META's `mta-nts-td-pathway-ingest.md` 0.1.1-draft (sections 2 and 2a)
passes:
  P1: 2 October 2026
  P2: not run; triggers 4 and 5 hold (Part E, item 1)
  P3: open
version: 0.2.21
---

<!-- from INGEST wpk-0016-ingest-pd-ingestion-document-template.md 0.10.0-draft; the specification is wpk-0016-ingest-pd-ingestion-document-structure.md -->
# Reflective Practice (academic skills pathway)

> **The core document.** Generic: it names no project that uses the pathway (ing N-0012). Who made the model and where each claim comes from is in Part D. Two kinds of companion document sit beside it and are never ingested with it: **source maps**, one per guide, recording which parts of a guide teach each capability (the first is the guide map for *Excelling at University*, held by `path`, draft); and **integrations**, one per consuming project, recording how that project uses the pathway (`integrations/<project>/`). Fill note from the template kept until P3.

## Part 0 Summary

### 0.1 Agent definition
<!-- brief: Two or three sentences for an agent: what this is and when to reach for it, and one thing it is not for. Write last, from the finished document. -->
<!-- label: editorial; status: drafted; basis: secondary -->
Reflective Practice is one of thirteen academic skills pathways: reflection taught as a discipline a student can do on purpose, from a three-stage cycle to the fuller models used in assessed vocational reflection and continuing professional development. Reach for it to place, sequence or assess a reflective capability, or to translate one into its workplace form. It is not a theory of reflection: Gibbs, Schön, Johns and Kolb have their own documents, and reflection on one's own learning process belongs to the pathway on learning, assessment and feedback.

### 0.2 Summary
<!-- brief: One paragraph: who proposed it, when, what it is, its main use and its main dispute. Write last. -->
<!-- label: both; status: drafted; basis: secondary -->
The academic skills pathways model (2026) sets Reflective Practice as one of thirteen pathways, drawn from the treatment of reflection in a study skills guide for undergraduates and from the reflective models used in the professions. It climbs in three tiers: what reflection is and why it matters (a three-stage cycle; honest, balanced reflection); structured, critical reflection turned into action; and reflection as professional practice, using fuller models such as Gibbs, Kolb and Johns, assessed in nursing, teaching and social work, with reflexivity (examining how one's personal identity, values, assumptions and social position shape one's reflections, judgements and actions), and as continuing professional development (CPD). Its main use is as the method under other pathways: feedback, reflective writing, group work and work-based learning. Its open questions are about coverage, not a scholarly dispute: the proposed capabilities cover the tiers unevenly, and the three-stage cycle's first stage is named two ways (Part E).

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
- A pathway is defined by three tiers, Introductory, Intermediate and Advanced, each with a focus, its content, a progression logic and links to other pathways (D:PTM, Pathway 10).
- Reflection is treated as a professional discipline, formal, assessed and career-long, and kept apart from the self-regulation of learning, which another pathway holds (D:PTM, Pathway 10).
- Tiers are anchored to experience of the practice, not to year or level of study: a student may be advanced in one practice and introductory in another (D:TSPEC, section 2).
- It replaced nothing: it became a pathway of its own when the model grew from nine pathways to thirteen (D:PTM, changes, v2).

### A2 Core principles
<!-- brief: One item per claim the theory rests on, each cited to the authors. Claims only, not uses or benefits. -->
<!-- label: source; status: drafted; basis: primary -->
- A learner's development, and in the end their development into a graduate, is driven by self-reflection (D:EAU, p. 53).
- A simple three-stage cycle (describe, reflect, take action) is enough to start; assessed reflection may require a fuller model such as Kolb's or Gibbs's (D:EAU, p. 53).
- Reflection should begin with what went well and is never wholly positive or negative; starting from the positives sets a balanced tone (D:EAU, p. 54).
- The action stage turns reflection into practical steps and is the stage students most often neglect (D:EAU, p. 54).
- Reflective writing must still be critical: describing an experience without critiquing one's own actions is the common fault (D:EAU, p. 161).
- Reflective writing is a genre of its own: less formal, in the first person, focused on experience and the self rather than the discourse, so it usually needs no academic references; it is structured by a reflective cycle and ends in action (D:EAU, pp. 161-163). This pathway teaches it; Academic Writing refers to it (D-ing-0022 (b)). It also teaches the professional-practice reflective report: reflection written in report format, under headings, moving from description to analysis of what worked and what was challenging to an action plan (D-ing-0044; editorial, after Gibbs, 1988).
- Constructive reflection on performance is central to CPD and lifelong learning in professional life (D:EAU, pp. 54-55).
- In practice- and work-based learning, reflective practice is the most common form of assessment (D:EAU, p. 225).
- The pathway's progression is: what reflection is, then structured critical reflection, then professional reflective practice (D:PTM, Pathway 10).

### A3 Structure
<!-- brief: The spine: every component (level, dimension, stage, category) with its order, parent, the authors' definition (paraphrased, cited), our gloss, key language and an example of our own. Take most care here; other stores link to these components. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
structure: [ladder, set]
components:
  # the three tiers (ladder)
  - { slug: introductory, componentType: level, order: 1, parent: none, name: "Introductory: what reflection is and why it matters", authorsDefinition: "reflection as both a learner's tool and a professional practice; the simple ERA cycle; reflecting honestly, positives first, never wholly positive or negative (D:PTM, Pathway 10)", gloss: "learn what reflection is and do it once, simply and honestly", keyLanguage: [ERA cycle, experience, reflect, take action, honest reflection], examples: ["after a first seminar, writing three short paragraphs: what happened, what went well and why, what to do next time"], audience: both, beneficiaryGloss: "find out what reflecting means and try a simple three-step way of doing it", readingLevel: "plain English for a student entering higher education" }
  - { slug: intermediate, componentType: level, order: 2, parent: none, name: "Intermediate: structured reflection turned into action", authorsDefinition: "reflecting on real experiences (feedback, tasks, group work); reflecting critically on one's own performance rather than describing it; turning reflection into concrete action plans (D:PTM, Pathway 10)", gloss: "reflect on real work, critically, and end with a plan", keyLanguage: [critical reflection, pure description, action plan], examples: ["reflecting on tutor feedback on an essay and setting three dated actions for the next one"], audience: both, beneficiaryGloss: "look hard at how you did on real work and turn it into a plan", readingLevel: "plain English for a student entering higher education" }
  - { slug: advanced, componentType: level, order: 3, parent: none, name: "Advanced: reflection as professional practice", authorsDefinition: "fuller models such as Gibbs, Kolb and Johns used in assessed reflection in vocational fields such as nursing, teaching and social work; reflexivity, examining how one's personal identity, values, assumptions and social position shape one's reflections, judgements and actions; reflection as CPD; reflection as part of graduate identity (D:PTM, Pathway 10; Johns and reflexivity added by the model's author, 2 October 2026)", gloss: "reflect the way a profession requires, and keep doing it", keyLanguage: [Gibbs, Kolb, Johns, assessed reflection, reflexivity, CPD, graduate identity], examples: ["a placement reflection written to Gibbs's six stages for a nursing module"], audience: both, beneficiaryGloss: "use the reflection models your profession uses, and make reflection a habit", readingLevel: "plain English for a student entering higher education" }
  # the capabilities (set; proposed, not yet confirmed)
  - { slug: reflective-practice-01, componentType: element, order: 1.1, parent: introductory, name: "Apply a structured reflective cycle (describe, reflect, take action) to a learning experience", authorsDefinition: "proposed capability, tier note introduced, from the Introductory tier's ERA cycle (D:CARDS)", gloss: "work through the three stages on something you did", keyLanguage: [reflective cycle, describe, reflect, take action], examples: ["a student's reflection on preparing for a tutorial (D:EAU, p. 54)"], audience: both, beneficiaryGloss: "use the three steps to think back over something you did", readingLevel: "plain English for a student entering higher education" }
  - { slug: reflective-practice-02, componentType: element, order: 1.2, parent: introductory, name: "Balance positive and negative observations when reflecting on performance", authorsDefinition: "proposed capability, tier note introduced, from the Introductory tier's honest reflection (D:CARDS)", gloss: "say what went well before what did not", keyLanguage: [positives first, balanced], examples: [], audience: both, beneficiaryGloss: "be fair to yourself: start with what went well", readingLevel: "plain English for a student entering higher education" }
  - { slug: reflective-practice-04, componentType: element, order: 2.1, parent: intermediate, name: "Reflect on motivation and amend learning strategies that are not working", authorsDefinition: "proposed capability, tier note developed, placed from the learning, assessment and feedback pathway's Intermediate tier (monitoring and adapting strategy); it crosses pathways (D:CARDS)", gloss: "notice when a way of working fails and change it", keyLanguage: [motivation, strategy, adapt], examples: ["a student changing how she reads journal articles mid-task (D:EAU, pp. 51-52)"], audience: both, beneficiaryGloss: "if the way you are studying isn't working, notice it and try another way", readingLevel: "plain English for a student entering higher education" }
  - { slug: reflective-practice-c1, componentType: element, order: 2.2, parent: intermediate, name: "Reflect critically on own performance rather than describing it", authorsDefinition: "capability added by the model's author from the Intermediate tier's critical reflection (D:PTM, Pathway 10; D-ing-0004)", gloss: "judge what you did, not just report it", keyLanguage: [critical reflection, description], examples: ["asking why a group task stalled and what part you played, not only what happened"], audience: both, beneficiaryGloss: "don't just say what happened: ask why, and what your part in it was", readingLevel: "plain English for a student entering higher education" }
  - { slug: reflective-practice-c2, componentType: element, order: 2.3, parent: intermediate, name: "Turn reflection into a dated action plan", authorsDefinition: "capability added by the model's author from the Intermediate tier's action planning (D:PTM, Pathway 10; D-ing-0004)", gloss: "end with steps you will take, and when", keyLanguage: [action plan, take action], examples: ["three actions for the next essay, each with a date"], audience: both, beneficiaryGloss: "finish with a short list of things you will do, and by when", readingLevel: "plain English for a student entering higher education" }
  - { slug: reflective-practice-c5, componentType: element, order: 2.4, parent: intermediate, name: "Write a professional-practice reflective report in report format", authorsDefinition: "capability added by the model's author: reflection written as a report under headings, from description through evaluation and analysis to an action plan (D-ing-0044, D-ing-0045)", gloss: "write up a reflection as a report with headings", keyLanguage: [reflective report, description, evaluation, analysis, action plan], examples: ["a placement reflection under the headings introduction, description, evaluation, analysis, conclusion and action plan"], audience: both, beneficiaryGloss: "set out your reflection as a report: what happened, what worked, what was hard, why, and what you will do next", readingLevel: "plain English for a student entering higher education" }
  - { slug: reflective-practice-03, componentType: element, order: 3.1, parent: advanced, name: "Use reflective writing to support continuing professional development and lifelong learning", authorsDefinition: "proposed capability, tier note extended, from the Advanced tier's CPD and graduate identity (D:CARDS)", gloss: "keep reflecting in writing after the course is over", keyLanguage: [reflective writing, CPD, lifelong learning], examples: [], audience: both, beneficiaryGloss: "keep writing reflections to keep learning in your career", readingLevel: "plain English for a student entering higher education" }
  - { slug: reflective-practice-c3, componentType: element, order: 3.2, parent: advanced, name: "Choose and apply a fuller reflective model (Gibbs, Kolb, Johns) to an assessed reflection", authorsDefinition: "capability added by the model's author from the Advanced tier's fuller models (D:PTM, Pathway 10; D-ing-0003, D-ing-0004)", gloss: "pick the model the task or profession needs and use it well", keyLanguage: [Gibbs, Kolb, Johns, assessed reflection], examples: ["a placement reflection to Gibbs's six stages, saying why Gibbs fits"], audience: both, beneficiaryGloss: "choose the reflection model your course or profession expects and follow it", readingLevel: "plain English for a student entering higher education" }
  - { slug: reflective-practice-c4, componentType: element, order: 3.3, parent: advanced, name: "Examine how own personal identity, values, assumptions and social position shape own reflections, judgements and actions (reflexivity)", authorsDefinition: "capability added by the model's author, Advanced only: examining how one's personal identity, values, assumptions and social position shape one's reflections, judgements and actions (D-ing-0004, D-ing-0006)", gloss: "question your own reflection: what shaped how you saw it", keyLanguage: [reflexivity, identity, values, assumptions, social position, positionality], examples: ["noticing that a reflection on a difficult placement blames a mentor and asking what in one's own background led to that reading"], audience: both, beneficiaryGloss: "look again at your reflection and ask how who you are, what you value and what you take for granted shaped it", readingLevel: "plain English for a student entering higher education" }
```

### A4 Concepts used
<!-- brief: The ideas the theory rests on that other theories share; each will become or match a TERMINOLOGY-DAT concept. -->
<!-- label: both; status: drafted; basis: primary -->
- reflection: the core act, looking back on an experience to find its meaning (D:EAU, p. 54).
- reflective-cycle: a model that orders reflection into stages (D:EAU, p. 53).
- critical-reflection: reflection that critiques one's own actions rather than describing them (D:EAU, p. 161).
- action-plan: the practical steps that close a reflection (D:EAU, p. 54).
- continuing-professional-development: the professional frame reflection serves (D:EAU, pp. 54-55).
- lifelong-learning: the disposition reflection sustains (D:EAU, p. 55).
- reflective-writing: the genre in which reflection is assessed (D:EAU, p. 161).
- experiential-learning: learning through experience, the frame of Kolb's cycle (D:EAU, p. 225).
- self-regulated-learning: its evaluation phase holds reflective practice (D:EAU, p. 53).
- graduate-identity: an identity defined by the competencies and capabilities of being a graduate (D:EAU, glossary, pp. x-xiii).
- era-experience: the describe stage of the ERA cycle: an account of what actually happened, without explanation (D:EAU, p. 53).
- reflective-journal: a running written record of reflection, often used as formative assessment (D:EAU, p. 53).
- description: an account of what happened without critique of one's own part, the common fault in reflective writing (D:EAU, pp. 53, 161).

Concepts above from `era-experience` on were added on 4 October 2026, 10:37: terms named in B2a or B4 that had no definition here (D-ing-0057).

### A5a How practitioners apply it
<!-- brief: From the practitioner's side: the steps they take, the tools and artefacts they use, a worked example, and the decisions they make along the way. Separate what the authors prescribe (source) from how it is done in practice (reported, with sources) and what follows from it (editorial). -->
<!-- label: both; status: drafted; basis: primary -->
Practitioners here are those who teach the pathway: tutors, academic skills staff and authors of learning material.

**What the authors prescribe** (source):
- Pitch a lesson to the whole tier at once: assumed experience, cognitive demand, task complexity and learner autonomy together, never one of them alone (D:TSPEC, section 5).
- Teach the three-stage cycle first; bring in the fuller models only at Advanced (D:PTM, Pathway 10).
- Model a reflection before asking for one: an ERA reflection on a group task and a Kolb account of a school placement are worked examples (D:EAU, pp. 162-163, 226-228).

**How it is done in practice** (reported):
- unknown: no report of the pathway taught as a whole yet.

**Worked example**:
At Introductory, a lesson shows a student's three-stage reflection on a tutorial, then asks the learner to sort statements into experience, reflect and take action; at Intermediate, the learner reflects on their own feedback and writes an action plan with a prompt but no model; at Advanced, the learner chooses Gibbs or Kolb for a placement reflection and justifies the choice (editorial, after D:TSPEC, section 9).

**What it implies** (editorial):
- Feedback climbs with the tier: at Introductory it states the answer and why, at Intermediate it points to where the answer lies, at Advanced it asks a question that leads the learner to it (D:TSPEC, section 5).

### A5b How beneficiaries meet it
<!-- brief: From the beneficiary's side (learner, client, project team, stakeholder): what it asks of them, what they see or do, and any version made for them to use directly. Search for this separately. -->
<!-- label: both; status: drafted; basis: primary -->
- Learners meet reflection first as formative assessment or a reflective journal, often before university (D:EAU, p. 53; evidence: claimed).
- They are asked to write in the first person and less formally, without academic references, but still critically (D:EAU, p. 161; evidence: claimed).
- On placements they are assessed mainly through reflection, usually built on Kolb's cycle (D:EAU, p. 225; evidence: claimed).
- They use it after group tasks to judge their own contribution (D:EAU, p. 217; evidence: claimed).

### A5c Contexts and adaptations
<!-- brief: Where it is used (levels, sectors, practices, settings, modes such as online), and how it has been adapted for them, each with its source. -->
<!-- label: both; status: drafted; basis: secondary -->
- Any higher education setting and mode; a learner enters at the tier that matches their experience of reflection, whatever their year (D:TSPEC, section 2).
- Vocational fields (nursing, teaching, social work): Advanced, with the model set by the profession (D:PTM, Pathway 10); these need discipline-aware examples beyond a general guide (D:PTM, cross-cutting notes).
- Art and design: reflective journals as part of the course (D:EAU, p. 53).
- Professional regulation (editorial, read by summary): nurses and midwives write reflective accounts for revalidation and discuss them with another registrant (D:NMC); HCPC's standards of proficiency hold a standard on reflecting on and reviewing practice (D:HCPC); Social Work England's standards ask social workers to reflect critically and record their reflection (D:SWE).

### A5d Misapplications
<!-- brief: Common ways it is misused or misread, the evidence for each, and how to avoid it. -->
<!-- label: both; status: drafted; basis: primary -->
- Describing instead of reflecting: the common fault in reflective writing (D:EAU, p. 161; evidence: claimed); avoid by keeping description to the first stage and questioning one's own actions after it.
- Over-critical reflection that dwells on the negatives (D:EAU, p. 54; evidence: claimed); avoid by starting with what went well.
- Skipping the action stage (D:EAU, p. 54; evidence: claimed); avoid by ending every reflection with dated, practical steps.
- Mis-tiered teaching: asking for critique while holding the learner's hand through it (D:TSPEC, section 5; evidence: claimed); avoid by pitching the whole tier at once.

### A6a Benefits to practitioners
<!-- brief: What those who apply it gain. Mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
- Reflective writing shows a tutor whether a student can take responsibility for their development and regulate their own performance (D:EAU, p. 161; evidence: claimed).
- One pathway that others draw on, so reflection is taught once and cross-referenced (D:PTM, Pathway 10; evidence: claimed).

### A6b Benefits to beneficiaries
<!-- brief: Name the beneficiaries, then what reaches them and how it reaches them through the practitioner. Search for this separately; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students; later, the people their professional practice serves.
- Insight into their own performance, and better performance next time (D:EAU, pp. 54, 161; evidence: claimed).
- A habit that carries into CPD and professional life (D:EAU, pp. 54-55; evidence: claimed).
- Self-knowledge and a sense of their ability to work in professional settings (D:EAU, p. 230; evidence: claimed).

### A7a Criticisms of the theory and its application
<!-- brief: Criticisms of the theory itself and of how practitioners apply it, with the evidence for each, marked measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: secondary -->
- none-stated: no published criticism of this pathway exists. Criticisms of the models it uses are in their own documents (A9).
- (editorial) The capabilities first proposed covered the tiers unevenly; four added in P3 fill the gaps (Part E, item 3).

### A7b Effects on beneficiaries
<!-- brief: Name the beneficiaries, then the harms, costs or limits that reach them through the practitioner's use. Search for this separately, as for A6b; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students.
- A student taught one simple cycle may meet a module that requires a fuller model, and must be told so (D:EAU, p. 53; evidence: claimed).
- unknown: no evidence yet of how learners fare in the pathway.

### A8 Selection
<!-- brief: When to choose it over named alternatives, and what it suits badly. Our reading (editorial). -->
<!-- label: editorial; status: drafted; basis: secondary -->
Choose this pathway when the aim is reflection as a deliberate, assessable practice. For reflection on one's own learning process, choose `path:understanding-learning-assessment-feedback`; for learning from placements, `path:work-based-experiential-learning`, which uses this pathway as its method. It suits badly a learner who needs one theory explained in depth: use that theory's document.

### A9 Relations
<!-- brief: Other theories it revises, extends, derives from, contrasts with or competes with, each with a target id and a one-line note. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: derivedFrom, target: ing:doc:experiential-learning-kolb-1984, note: "Kolb's cycle is taught at Advanced (D:PTM, Pathway 10; D:EAU, pp. 225-228)" }
- { rel: derivedFrom, target: ing:doc:reflective-cycle-gibbs-1988, note: "Gibbs's cycle is taught at Advanced (D:PTM, Pathway 10; D:EAU, p. 53)" }
- { rel: alternativeTo, target: ing:doc:reflective-practitioner-schon-1983, note: "the theory of reflection in and on action behind reflective practice; a link only, not a model taught in a tier (Part E, item 7)" }
- { rel: derivedFrom, target: ing:doc:structured-reflection-johns-1995, note: "Johns's model is taught at Advanced, a fuller model used in nursing" }
- { rel: derivedFrom, target: unknown, note: "the ERA cycle (Jasper, 2013): the Introductory model; no ingestion document yet (Part E, item 4)" }
- { rel: related, target: ing:doc:variants-of-reflexivity-finlay-2002, note: "Finlay (2002), variants of reflexivity; the Advanced tier's reflexivity; META INGEST run, SHA-256 prefix cc81a1375fdd; a model the tiers may teach, not ruled" }
- { rel: related, target: ing:doc:reflexive-learning-rolfe-2001, note: "Rolfe (2001), what, so what, now what; META INGEST run, SHA-256 prefix 515e06ab478e; a model the tiers may teach, not ruled" }
- { rel: related, target: ing:doc:what-model-driscoll-1994, note: "Driscoll (1994), the what model; META INGEST run, SHA-256 prefix 75724b6fe1ba; a model the tiers may teach, not ruled" }
- { rel: related, target: ing:doc:reflective-processes-atkins-murphy-1993, note: "Atkins and Murphy (1993), the reflective processes; META INGEST run, SHA-256 prefix 3823e4faf628; a model the tiers may teach, not ruled" }
- { rel: related, target: ing:doc:reflection-boud-keogh-walker-1985, note: "Boud, Keogh and Walker (1985), reflection: turning experience into learning; META INGEST run, SHA-256 prefix bbc63e980d66; a model the tiers may teach, not ruled" }
- { rel: related, target: ing:doc:critical-lenses-brookfield-1995, note: "Brookfield (1995), the four critical lenses; META INGEST run, SHA-256 prefix 742211547d46; a model the tiers may teach, not ruled" }
- { rel: derivedFrom, target: unknown, note: "the key theory (D-ing-0037): Moon (2004), reflection and reflective writing at increasing depth (descriptive writing, descriptive reflection, dialogic reflection, critical reflection, after Hatton and Smith, 1995); the scale A11 climbs; queued at META's ing (W-0035)" }
- { rel: derivedFrom, target: unknown, note: "beside the key theory (D-ing-0037): Bolton (with Delderfield), reflective practice as writing and professional development, with reflexivity; the upper levels; queued at META's ing (W-0003)" }
```

### A10 Extension fields
<!-- brief: The practice extension fields for each practice in the front matter, and no others. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
education:
  domain: "cognitive and affective (D:EAU, p. 54: judging performance, positives and negatives)"
  verbs: none-stated
  learnerLevel: "higher education, any year; tiers are anchored to experience of reflection, not to study level (D:TSPEC, section 2)"
pathway:
  id: path:reflective-practice
  title: Reflective Practice
  definition: "Reflection taught as a deliberate discipline: looking back on an experience in stages, judging one's own part in it honestly and critically, and turning what is found into action; first as a learner's tool, then as the assessed and career-long practice of the professions, examined reflexively."
  terms:
    direct: [reflective practice, reflection, reflective, reflect on, self-reflection, reflexivity, CPD, continuing professional development]
    associated: [reflective cycle, reflective writing, reflective journal, reflective account, reflective report, action plan, critical reflection, lifelong learning]
    source: "direct: the pathway term list v1.0 (D:TERMS; its 7 patterns written as words); associated: candidates from D:EAU and D:PTM, no list places them yet (B2b); reflective report proposed from Academic Writing's list, where reflective also stood (D-ing-0022 (b)); associated widened from the guide's glossary and the model's tier text (D-ing-0050)"
  competencies:
    - id: reflective-practice/01
      tierNote: introduced
      statement: Apply a structured reflective cycle (describe, reflect, take action) to a learning experience.
      level: unknown
      verbs: [apply, describe, reflect, take action]
      theory: [unknown: the ERA cycle has no document]
      process: [era-reflective-cycle]
      professional:
        - statement: Writes a structured reflective account of a practice event, ending in actions.
          equivalence: partial
          gap: "the professional account is tied to a code or standard, to a set count and cycle, and is discussed with or audited by a peer or regulator; the academic one reflects on a learning task"
          frameworks: ["NMC revalidation: written reflective accounts", "HCPC standards of proficiency: reflect on and review practice", "Social Work England professional standards 4.7"]
    - id: reflective-practice/02
      tierNote: introduced
      statement: Balance positive and negative observations when reflecting on performance.
      level: unknown
      verbs: [balance, reflect]
      theory: [{unknown: "Jasper (2013), the ERA cycle, not yet ingested; W-0001"}]
      process: [era-reflective-cycle]
      professional:
        - statement: Reviews own practice critically and fairly, and considers other ways of working.
          equivalence: broader
          gap: "the professional form asks for critical review and alternatives; balance is one part of it"
          frameworks: ["HCPC standards of proficiency: reflect critically and consider alternative approaches"]
    - id: reflective-practice/04
      tierNote: developed
      statement: Reflect on motivation and amend learning strategies that are not working.
      level: unknown
      verbs: [reflect, amend]
      theory: [{unknown: "Zimmerman (2002), self-regulated learning, not yet ingested; W-0037"}]
      process: [{needed: "a process for monitoring and amending strategies; the self-regulated learning cycle of Understanding Learning, Assessment and Feedback may serve"}]
      professional:
        - statement: Uses feedback and supervision to find learning needs and change how one works.
          equivalence: partial
          gap: "the professional form runs through supervision and feedback from others; the academic one is self-monitored and about study strategy"
          frameworks: ["Social Work England professional standards 4.2", "Vitae RDF B1 Personal qualities: self-reflection"]
    - id: reflective-practice/03
      tierNote: extended
      statement: Use reflective writing to support continuing professional development and lifelong learning.
      level: unknown
      verbs: [use, support]
      theory: [ing:doc:reflective-cycle-gibbs-1988, ing:doc:experiential-learning-kolb-1984]
      process: [structured-debriefing, experiential-learning-cycle]
      professional:
        - statement: Records reflection on learning and practice as CPD evidence, to a regulator's or employer's standard.
          equivalence: partial
          gap: "the professional form is mandated, recorded to a format and audited; the academic one is the habit before the mandate"
          frameworks: ["NMC revalidation", "Social Work England professional standards 4.6 and 4.7", "Advance HE PSF 2023 A5", "Wales professional standards for teaching: professional learning (revised; consultation)"]
    - id: reflective-practice/c1   # proposed; the model assigns the number
      tierNote: developed
      statement: Reflect critically on own performance rather than describing it.
      level: unknown
      verbs: [reflect]
      theory: [{unknown: "Moon (2004), not yet ingested; W-0035"}]
      process: [era-reflective-cycle]
      professional:
        - statement: Reflects critically on own practice and considers alternative approaches.
          equivalence: partial
          gap: "the professional form judges practice against standards and a duty to others; the academic one judges a learning task"
          frameworks: ["HCPC standards of proficiency: reflect critically and consider alternative approaches", "Social Work England professional standards 4.2"]
    - id: reflective-practice/c2   # proposed; the model assigns the number
      tierNote: developed
      statement: Turn reflection into a dated action plan.
      level: unknown
      verbs: [turn]
      theory: [{unknown: "Jasper (2013), the ERA cycle, not yet ingested; W-0001"}]
      process: [era-reflective-cycle]
      professional:
        - statement: Plans and records development actions from reflection on practice.
          equivalence: partial
          gap: "the professional plan is tied to CPD requirements and reviewed by others; the academic one is the student's own"
          frameworks: ["NMC revalidation", "Social Work England professional standards 4.6"]
    - id: reflective-practice/c5   # proposed; the model assigns the number
      tierNote: developed
      statement: Write a professional-practice reflective report in report format.
      level: unknown
      verbs: [write]
      theory: [ing:doc:reflective-cycle-gibbs-1988]
      process: [structured-debriefing, era-reflective-cycle]
      professional:
        - statement: Writes reflective accounts or reports on practice for a supervisor, assessor or regulator.
          equivalence: partial
          gap: "the professional account often follows a form the profession sets; the academic report sets its own headings and is assessed as writing"
          frameworks: ["NMC revalidation: written reflective accounts"]
    - id: reflective-practice/c3   # proposed; the model assigns the number
      tierNote: extended
      statement: Choose and apply a fuller reflective model (Gibbs, Kolb, Johns) to an assessed reflection.
      level: unknown
      verbs: [choose, apply]
      theory: [ing:doc:reflective-cycle-gibbs-1988, ing:doc:experiential-learning-kolb-1984, ing:doc:structured-reflection-johns-1995]
      process: [structured-debriefing, experiential-learning-cycle, structured-reflection]
      professional:
        - statement: Uses the reflective model the profession or employer expects, and justifies the choice.
          equivalence: partial
          gap: "a profession often fixes the model or the form; the academic form includes choosing"
          frameworks: ["NMC revalidation: written reflective accounts", "HCPC standards of proficiency: reflect on and review practice"]
    - id: reflective-practice/c4   # proposed; the model assigns the number
      tierNote: extended
      statement: Examine how own personal identity, values, assumptions and social position shape own reflections, judgements and actions (reflexivity).
      level: unknown
      verbs: [examine, shape]
      theory: [ing:doc:variants-of-reflexivity-finlay-2002, {unknown: "Bolton, not yet ingested; W-0003"}]
      process: [{none: "a disposition (reflexivity), not a process"}]
      professional:
        - statement: Reflects on own values and challenges their effect on practice.
          equivalence: partial
          gap: "close in kind: both examine one's own values; the professional form also challenges their effect on practice and the people served, the academic form their effect on the learner's reading of their own experience"
          frameworks: ["Social Work England professional standards 4.8"]
  external:
    - { framework: "Vitae Researcher Development Framework", match: ["B1 Personal qualities: self-reflection", "B3 Professional and career development"], equivalence: broader }
    - { framework: "Advance HE Professional Standards Framework 2023", match: [A5], equivalence: partial }
    - { framework: "ESCO", match: [unknown], equivalence: unknown }
  processes: [era-reflective-cycle, structured-debriefing, experiential-learning-cycle, structured-reflection]
  templates: [GD-edu-12 Reflective account, "an action plan (proposed)", "a reflective journal entry (proposed)"]
```
`equivalence` says how the professional form relates to the capability (META D-0175's scale). Every crosswalk item is editorial: its frameworks were read by summary only (Part E, item 1).

### A11 Progression by level
<!-- brief: How the practice develops across qualification levels 3 to 8, deconstructed at each level into skills, competencies, understandings and literacies (after Lea and Street); level 8 in full; each entry says what changes from the level below; grounded in level descriptors and the key theory. From META's pathway template 0.3.0-draft. -->
<!-- label: both; status: drafted; basis: secondary -->
Each level's understandings end with what the practice means for the learner's own development (D-ing-0036). Each level also carries a metacognitive statement (D-ing-0038, D-ing-0039): what the learner understands about the practice in general and its application, and their stance towards it, on a ladder from applying it because they must (compliance), through knowing why (purpose), investment, ownership and confidence (ownership), to adapting it to personal goals (adaptation) and practising it fluently, applied and communicated as a mode of doing and expression in the service of the disciplinary community (flow). The practice described is reflection on one's own learning and practice, never the pathway's tiers. The descriptors were read by summary only (Part E, item 11). The depth of reflection at each level follows the four types of reflective writing that Moon (2004) adopts from Hatton and Smith (1995): descriptive writing, descriptive reflection, dialogic reflection and critical reflection.
```yaml
progression:
  levelFramework: "qualification levels 3 to 8: CQFW and RQF numbering; FHEQ levels 4 to 8"
  levels:
    - level: 3
      context: "a learner entering higher education: level 3 study, access and foundation years"
      skills: ["describe an experience, what happened and how one felt", "say what went well and what did not", "set a simple next step"]
      competencies: ["completes a short reflection on a well-defined task with guidance"]
      understandings: ["reflection is learning from experience, not only recounting it", "for own development: noticing how one learns is the first step in taking charge of it"]
      literacies: ["a short first-person account, mostly descriptive writing"]
      metacognition: { stance: compliance, statement: "Reflects because the task asks for it; sees reflection as something to complete, and is not yet aware of how they learn." }
      changesFromBelow: not-applicable-by-design
      sources: [CQFW, MOON, HATTONSMITH]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 4
      context: "the first year of higher education"
      skills: ["use a simple cycle (experience, reflect, act) on own learning and feedback", "give reasons for what happened", "balance strengths and weaknesses honestly"]
      competencies: ["reflects on assessed work and feedback with some guidance and acts on it"]
      understandings: ["reflection is part of self-regulated learning: the evaluation that feeds the next plan", "for own development: reflection closes the loop from feedback to the next piece of work, so the learner steers their own improvement"]
      literacies: ["a reflective journal or learning log; descriptive reflection, with reasons in plain language"]
      metacognition: { stance: purpose, statement: "Knows why reflection is asked for and begins to notice their own learning habits; still reflects mainly when prompted." }
      changesFromBelow: "from recounting to giving reasons and planning the next step, applied to one's own study"
      sources: [FHEQ, MOON, HATTONSMITH]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 5
      context: "developing practice, depending on the student: the second year, work placements"
      skills: ["reflect critically on own performance in real tasks such as group work and feedback, rather than describe it", "use a recognised model such as Gibbs's cycle", "turn reflection into an action plan with measurable steps"]
      competencies: ["identifies own learning needs and acts on them without prompting"]
      understandings: ["the same event can be read from more than one point of view", "theory and literature can explain one's experience", "reflective practice can evolve a practitioner identity, the move towards reflection as professional practice at level 6 (Abbott, D-ing-0035)", "for own development: reflection over time makes one's growth visible and plannable across a whole course"]
      literacies: ["a structured reflective essay or report linking experience to literature; dialogic reflection: stepping back, weighing alternatives"]
      metacognition: { stance: investment, statement: "Invests in reflection, beginning to choose when and how to reflect, aware that reflection shapes who they are becoming as a practitioner; can say what the practice does for them." }
      changesFromBelow: "from one's own reasons to alternatives, other perspectives and the literature; from a next step to a plan; the first sense of reflection shaping who one is becoming as a practitioner"
      sources: [FHEQ, MOON, HATTONSMITH]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 6
      context: "independent practice: the final undergraduate year, professional placements"
      skills: ["choose and justify a reflective model for the purpose (Kolb, Gibbs, Johns)", "reflect in and on action in practice settings", "examine how one's own values and assumptions shape judgement (reflexivity begins)"]
      competencies: ["reflects routinely as professional practice and records it as continuing professional development against a profession's standards"]
      understandings: ["reflection is a professional duty in many fields, assessed against standards", "personal position affects what one notices and how one judges", "for own development: reflection records and directs one's continuing professional development and readiness for practice"]
      literacies: ["an assessed reflective account in a vocational genre (nursing, teaching, social work); a CPD record; critical reflection placing practice in its wider context"]
      metacognition: { stance: ownership, statement: "Has made reflection their own: reflects habitually and with confidence, judges which model fits, and knows how their own position colours what they notice." }
      changesFromBelow: "from structured reflection on study to reflection as professional practice, judged against standards, with reflexivity"
      sources: [FHEQ, MOON, HATTONSMITH, NMC, SWE]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 7
      context: "advanced practice: master's study, professional development and recognition"
      skills: ["critically evaluate own and others' practice against theory and evidence", "frame and reframe practice problems", "lead reflective discussion with colleagues"]
      competencies: ["sustains reflexivity across a body of work; reflects on own progress as a learner and on professional responsibility, integrity and ethics"]
      understandings: ["reflective practice is itself contested: its models, frames and power relations can be critiqued", "for own development: reflecting on one's progress as a learner and practitioner sustains lifelong development and professional recognition"]
      literacies: ["a reflective commentary within practice-based research; a portfolio for professional recognition"]
      metacognition: { stance: adaptation, statement: "Moulds reflection to personal and professional goals and settings, combining or inventing approaches; communicates their reflection to colleagues and uses it to develop others." }
      changesFromBelow: "from reflecting on practice to critiquing practice and the frames used to reflect on it"
      sources: [FHEQ, QAAMSC, PSF, MOON]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 8
      context: "doctoral practice: an original contribution to knowledge, the researcher's identity and independence"
      skills: ["write a reflexive account of one's position in relation to the research", "reflect on the research process and its decisions as it unfolds", "plan one's development as a researcher"]
      competencies: ["uses reflexivity as part of research method, so that the account of the knowledge made includes the maker", "manages own development and career as a researcher"]
      understandings: ["the researcher's identity, values and position shape what counts as knowledge in the study", "reflection here concerns the production of knowledge, not only the improvement of practice", "for own development: reflexivity shapes one's identity, independence and career as a researcher"]
      literacies: ["a positionality statement and a reflexive methodology section in a thesis; a development record against a researcher framework"]
      metacognition: { stance: flow, statement: "Reflection has become a mode of doing and expression, fluent and largely tacit, like an athlete in the flow; reflexivity is how they make and communicate knowledge in the service of their disciplinary community, and an expression of their commitment to it." }
      changesFromBelow: "a different kind, not more of level 7: reflection turns on the making of original knowledge and on the researcher's own identity and independence"
      sources: [QAADOC, RDF, FHEQ]
      provenance: { label: both, status: drafted, basis: secondary }
```

## Part B Terminology

### B1 Concepts
<!-- brief: One concept per idea that has a name in this theory (each A3 component, each A4 concept): plain definition, scope note, category, practices. -->
<!-- label: both; status: drafted; basis: primary -->
By rule: one concept per A3 tier and per A4 concept, definition as A3's gloss or A4's line. The exceptions, written out:
```yaml
- slug: reflective-practice
  definition: reflection done on purpose, in stages, as a habit of learning and of professional work
  beneficiaryDefinition: "thinking back over what you did, step by step, so you do better next time"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: covers the pathway's practice; excludes reflection on one's own learning process, held by self-regulated learning
  category: approach
  practices: [education]
- slug: era-reflective-cycle
  definition: "a three-stage cycle: experience (describe what happened), reflect, take action"
  beneficiaryDefinition: "three steps: say what happened, think about why, decide what to do next"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: the pathway's first model; credited to Jasper (2013) and close to Driscoll (2007) in D:EAU
  category: process
  practices: [education]
- slug: critical-reflection
  definition: reflection that judges one's own actions and decisions rather than describing them
  scopeNote: the Intermediate step; contrasts with description
  category: construct
  practices: [education]
- slug: reflexivity
  definition: "examining how one's personal identity, values, assumptions and social position shape one's reflections, judgements and actions"
  beneficiaryDefinition: "asking how who you are, what you value and what you take for granted shaped your reflection"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "Advanced only; goes beyond reflection, which looks back at an event, by examining the self that reflects; includes positionality and the limits of what one can know from where one stands"
  category: construct
  practices: [education]
- slug: action-plan
  definition: the practical steps a reflection ends with
  scopeNote: the output of the take-action stage
  category: technique
  practices: [education]
```

### B2a Terms named by the authors
<!-- brief: Every name the authors give a concept: preferred and admitted forms, their alternative names and spelling variants, in full (no compact rule); part of speech, register, extension fields. -->
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: reflective-practice, form: reflective practice, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: reflection, form: reflection, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: reflection, form: self-reflection, lang: en, partOfSpeech: noun, termStatus: admitted, register: general }
- { concept: era-reflective-cycle, form: ERA cycle, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: era-reflective-cycle, form: three-stage reflective cycle, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: era-reflective-cycle, form: "Experience, Reflect, Take action", lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: era-reflective-cycle, form: "describe, reflect, take action", lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: era-experience, form: Experience, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: era-experience, form: describe, lang: en, partOfSpeech: verb, termStatus: admitted, register: general }
- { concept: critical-reflection, form: reflecting critically, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: action-plan, form: action plan, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: continuing-professional-development, form: continuing professional development, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: continuing-professional-development, form: CPD, lang: en, partOfSpeech: noun, termStatus: admitted, register: general }
- { concept: lifelong-learning, form: lifelong learner, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: reflective-writing, form: reflective writing, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: reflective-journal, form: reflective journal, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: reflexivity, form: reflexivity, lang: en, partOfSpeech: noun, termStatus: preferred, register: discipline-specific }
- { concept: reflexivity, form: reflexive, lang: en, partOfSpeech: adjective, termStatus: admitted, register: discipline-specific }
- { concept: graduate-identity, form: graduate identity, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
```

Glossary terms placed in this pathway (D:EAU, glossary, pp. x-xiii; D-ing-0050): graduate identity, lifelong learner, reflective practice; added here: graduate identity.
`usableIn` and `bannedIn`: none-stated. Education extension (`qualificationLevel`, `domain`, `sourceType`): `sourceType` is `book` for every term from D:EAU; the rest unknown.

### B2b Associated vocabulary
<!-- brief: The wider vocabulary practitioners reach for (for Bloom, the verb lists), from at least two named secondary sources, with a scholarly analysis of such lists where one exists. Where none exists, list the words as candidates and put the glossary wanted in D3. One membership per component a word is placed in, with its sources and agreement weight; record where sources disagree with the authors. Never store similarity between words: it is computed from embeddings at query time. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
- { concept: reflective-account, form: reflective account, frameworkBlocks: [{ component: advanced, sources: [NMC], weight: 1/1 }], status: candidate }
- { concept: debrief, form: debriefing, frameworkBlocks: [{ component: advanced, sources: [], weight: 0/0 }], status: candidate }
- { concept: supervision, form: reflective supervision, frameworkBlocks: [{ component: advanced, sources: [SWE], weight: 1/1 }], status: candidate }
- { concept: critical-reflection, form: critical reflection, frameworkBlocks: [{ component: intermediate, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: reflective-model, form: reflective model, frameworkBlocks: [{ component: advanced, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: reflective-report, form: reflective report, frameworkBlocks: [{ component: intermediate, sources: [PTM], weight: 1/1 }], status: candidate }
```
No glossary of reflective practice vocabulary was consulted; one is wanted (D3).

### B3 Framework blocks
<!-- brief: For each concept this theory defines its own way: the A3 component, this theory's definition (cited) and its use here. -->
<!-- label: source; status: drafted; basis: primary -->
By rule: each tier concept's framework block is its A3 component and definition. The exceptions:
```yaml
- { concept: era-reflective-cycle, component: introductory, definitionHere: "a simple three-stage model for structuring reflection, offered as enough to start (D:EAU, p. 53)", useHere: "the Introductory model and the structure of reflective writing" }
- { concept: critical-reflection, component: intermediate, definitionHere: "reflecting critically on one's own performance, avoiding pure description (D:PTM, Pathway 10)", useHere: "the Intermediate step" }
```

### B4 Relations
<!-- brief: Broader, narrower, related, contrasts-with and the order within this theory, between the B1 concepts. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: higher-level-than, from: intermediate, to: introductory, note: "tier order" }
- { rel: higher-level-than, from: advanced, to: intermediate, note: "tier order" }
- { rel: broader, from: reflexivity, to: critical-reflection, note: "reflexivity examines the reflecting self as well as the act; Advanced only" }
- { rel: narrower, from: era-reflective-cycle, to: reflective-cycle, note: "one cycle among many" }
- { rel: contrasts-with, from: critical-reflection, to: description, note: "the fault D:EAU names (p. 161)" }
- { rel: related, from: reflective-practice, to: continuing-professional-development, note: "reflection is at the heart of CPD (D:EAU, p. 55)" }
- { rel: related, from: reflective-practice, to: self-regulated-learning, note: "reflection is the evaluation phase of SRL (D:EAU, p. 53)" }
```

### B5 Rules
<!-- brief: Our rules on using the terms (such as a verb banned in outcomes), each with its reason. Editorial. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- understand, know, appreciate, be aware of: not used in learning outcomes at any tier, because they name no observable operation (D:TSPEC, section 6).

## Part C Process

### C0 Formality
<!-- brief: Decide first: prescribed, recommended, loose, implied or not applicable, with one sentence on why. If not applicable, stop Part C. -->
<!-- label: both; status: drafted; basis: primary -->
`recommended`: the three-stage cycle is recommended and each stage set out, while other models exist and some assessments require them (D:EAU, pp. 53-54).

### C1 Process models
<!-- brief: Each process the theory lends itself to: what it achieves, shape, scale, what starts it and what counts as done. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: era-reflective-cycle
  summary: reflect on one experience in three stages and leave with actions
  shape: cyclic
  scale: [task]
  scaleNote: "one tutorial, one group task (D:EAU, pp. 54, 162-163)"
  groundedIn: [ing:doc:pathway-reflective-practice]
  entry: an experience worth learning from
  exit: an action plan
- slug: pathway-progression
  summary: move a learner from a first simple reflection to professional reflective practice
  shape: staged-with-gates
  scale: [course, programme]
  scaleNote: "three tiers (D:PTM, Pathway 10)"
  groundedIn: [ing:doc:pathway-reflective-practice]
  entry: no prior deliberate reflection
  exit: reflection used as CPD
  inferred: true
```
The fuller models are processes in their own documents: `structured-debriefing` (Gibbs), `experiential-learning-cycle` (Kolb), `structured-reflection` and `guided-reflection` (Johns), `reflective-practice-cycle` (Schön).

### C2 Stages
<!-- brief: Each stage in order: purpose, inputs, activities, outputs, roles, the gate that ends it. Mark our arrangement editorial where the authors give no stages, and every activity the sources do not name `inferred: true`. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { model: era-reflective-cycle, order: 1, name: Experience, purpose: "describe what happened, nothing more (D:EAU, pp. 53, 161)", inputs: [], activities: [write an account of the experience], outputs: [account], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: era-reflective-cycle, order: 2, name: Reflect, purpose: "explore why it went as it did, positives first (D:EAU, p. 54)", inputs: [account], activities: [ask what went well and why, ask what did not and why], outputs: [insights], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: era-reflective-cycle, order: 3, name: Take action, purpose: "turn reflections into practical steps (D:EAU, p. 54)", inputs: [insights], activities: [write an action plan], outputs: [action-plan], roles: [student], endsAt: none, repeat: "the next similar experience", audience: both }
- { model: pathway-progression, order: 1, name: Introductory, purpose: "what reflection is and why it matters", inputs: [], activities: [learn and apply the three-stage cycle], outputs: [], roles: [student, tutor], endsAt: tier-assessment, repeat: none, audience: both, inferred: true }
- { model: pathway-progression, order: 2, name: Intermediate, purpose: "structured reflection turned into action", inputs: [], activities: [reflect critically on real experience, write action plans], outputs: [action-plan], roles: [student, tutor], endsAt: tier-assessment, repeat: none, audience: both, inferred: true }
- { model: pathway-progression, order: 3, name: Advanced, purpose: "reflection as professional practice", inputs: [], activities: [use a fuller model in assessed reflection, reflect for CPD], outputs: [reflective-account], roles: [student, tutor], endsAt: tier-assessment, repeat: none, audience: both, inferred: true }
```

### C3 Gates
<!-- brief: Each decision point with criteria that can pass or fail, and what it decides. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
- slug: tier-assessment
  criteria: ["an end-of-tier assessment is passed at the tier's demand (D:TSPEC, section 7)"]
  decides: go
  variationPoint: no
```

### C4 Outputs
<!-- brief: Each product a stage makes: purpose, parts, and what a template for it needs to know. Mark every output the sources do not name `inferred: true`. Where the method names its own document types, record every one complete (purpose, composition, derivation, quality criteria) from its product descriptions; our templates are drafted from those parts, never the method's text copied. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: account, purpose: "the plain record of what happened", parts: [what happened], producedBy: [1], usedBy: [2], templateHint: "no judgement in this part", audience: beneficiary }
- { slug: insights, purpose: "what went well and why; what did not and why", parts: [positives, negatives, reasons], producedBy: [2], usedBy: [3], templateHint: "positives first", audience: beneficiary }
- { slug: action-plan, purpose: "practical steps to improve next time", parts: [actions], producedBy: [3], usedBy: [], templateHint: "a short list of concrete actions (D:EAU, p. 163)", audience: beneficiary }
- { slug: reflective-account, purpose: "an assessed reflective piece written to a named model", parts: [the model's stages], producedBy: [Advanced], usedBy: [], templateHint: "COMPOSE GD-edu-12", audience: both, inferred: true }
```

### C5 Roles
<!-- brief: Who does each stage, from both sides: practitioner roles and beneficiary roles. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: student, responsibilities: [reflect, write, act], stagesInvolved: [1, 2, 3] }
- { slug: tutor, responsibilities: [model reflection, assess it], stagesInvolved: [Introductory, Intermediate, Advanced] }
- { slug: mentor, responsibilities: [discuss reflection on placement], stagesInvolved: [Advanced], inferred: true }
```

### C6 Variation points
<!-- brief: Where the process can be tailored or branch, by gate. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- Advanced: the model is chosen by the profession or the module (Gibbs, Kolb, Johns); the pathway does not fix it.
- Every tier: the learner's subject changes the experiences reflected on, never the demand.

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
- { key: PTM, author: "Abbott, S.", title: "Academic skills pathways model: pathway tier mapping, Draft v3 (v3.1)", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [0.2, A1, A2, A3, A5a, A5c, A6a, A8, A9, B3, C1] }
- { key: TSPEC, author: "Abbott, S.", title: "Academic skills pathways model: tier specification v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A1, A5a, A5c, A5d, A10, B5, C3] }
- { key: CARDS, author: "Abbott, S.", title: "Academic skills pathways model: capability cards with tier notes, proposed", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A3, A10] }
- { key: TERMS, author: "Abbott, S.", title: "Academic skills pathways model: pathway term list v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A10, B2b] }
- { key: EAU, author: "Dennis, C. and Abbott, S.", title: "Excelling at University: Academic Literacies and the Development of Graduate Identity", edition: 1st, year: 2026, publisher: Routledge, licence: "copyright", tier: primary, readVia: direct, held: not held, citedIn: [A2, A3, A4, A5a, A5b, A5c, A5d, A6a, A6b, A7b, A10, B1, B3, B4, C0, C1, C2, C4] }
- { key: NMC, author: Nursing and Midwifery Council, title: "Revalidation: reflective discussion", year: unknown, publisher: NMC, tier: web, readVia: summary, held: not held, citedIn: [A5c, A10, B2b] }
- { key: HCPC, author: Association of Educational Psychologists, title: "Reflective practice guidance, HCPC and AEP", year: 2026, tier: professional, readVia: summary, held: not held, citedIn: [A5c, A10] }
- { key: SWE, author: Social Work England, title: "The CPD standard", year: unknown, tier: web, readVia: summary, held: not held, citedIn: [A5c, A10, B2b] }
- { key: PSF, author: Advance HE, title: "Professional Standards Framework 2023", year: 2023, tier: professional, readVia: summary, held: not held, citedIn: [A10], run: "ing:doc:professional-standards-framework-advance-he-2023, META, SHA-256 prefix d567e4bc041e" }
- { key: RDF, author: "University of Edinburgh, School of Social and Political Science", title: "Researcher Development Framework (Vitae) page", year: unknown, tier: web, readVia: summary, held: not held, citedIn: [A10, A11] }
- { key: WPS, author: Welsh Government, title: "Revised professional standards for assisting teaching, teaching and leadership (consultation)", year: 2025, tier: web, readVia: summary, held: not held, citedIn: [A10] }
- { key: FHEQ, author: Quality Assurance Agency for Higher Education, title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies, 2nd edn (level descriptors unchanged from 2014)", year: 2024, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:qaa-fheq-2024-framework, META, SHA-256 prefix 97c52675225e" }
- { key: CQFW, author: Welsh Government, title: "Credit and Qualifications Framework for Wales: level descriptors", year: 2009, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:welsh-government-cqfw-2009-framework, META, SHA-256 prefix 682642ca28c8" }
- { key: QAAMSC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Master's Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: QAADOC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Doctoral Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: MOON, author: "Moon, J. A.", title: "A Handbook of Reflective and Experiential Learning: Theory and Practice", year: 2004, publisher: RoutledgeFalmer, tier: secondary, readVia: summary, held: not held, citedIn: [A11] }
- { key: HATTONSMITH, author: "Hatton, N. and Smith, D.", title: "Reflection in teacher education: towards definition and implementation", journal: "Teaching and Teacher Education 11(1), 33-49 (recall)", year: 1995, tier: secondary, readVia: summary, held: not held, citedIn: [A11] }
```

### D2 Research log
<!-- brief: Every source opened, used or not, as you open it. -->
```yaml
- { ref: PTM, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: tiers, links between pathways" }
- { ref: TSPEC, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: tier dimensions, outcome verbs, end-of-tier assessment" }
- { ref: CARDS, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: four capabilities with tier notes" }
- { ref: TERMS, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: 7 patterns" }
- { ref: EAU, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: Ch 4 pp. 51-55, Ch 9 pp. 161-163, Ch 11 p. 217, Ch 12 pp. 225-230" }
- { ref: "INGEST runs 0008, 0025, 0031, 0032 (front matter, C0, C1)", tier: scholarly, consulted: 2026-10-02, pass: P1, outcome: "used: ids and process slugs only" }
- { ref: "COMPOSE catalogue 0.2.5-draft, GD-edu-12 and GD-edu-06", tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: templates" }
- { ref: NMC, tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: reflective accounts, reflective discussion" }
- { ref: HCPC, tier: professional, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: the standard on reflection, numbered 10, and its four parts" }
- { ref: "https://www.aep.org.uk/resources/hcpc-standards-proficiency-practitioner-psychologists", tier: web, consulted: 2026-10-02, pass: P1, outcome: "set aside: gives the standard as 11, conflicting (Part E, item 5)" }
- { ref: SWE, tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: standards 4.2, 4.6, 4.7, 4.8" }
- { ref: PSF, tier: professional, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: A5" }
- { ref: RDF, tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: B1 self-reflection, B3" }
- { ref: WPS, tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: the professional learning standard; consultation, launch September 2026" }
- { ref: "ESCO transversal skills terminology v1.1 (search result only)", tier: web, consulted: 2026-10-02, pass: P1, outcome: "set aside: not opened; no ESCO skill id found" }
- { ref: "FHEQ, via https://www.qaa.ac.uk/news-events/news/updated-edition-of-the-frameworks-for-higher-education-qualifications-of-uk-degree-awarding-bodies-published and https://www.ucl.ac.uk/study/current-students/academic-manual/chapters/chapter-7-course-and-module-approval-and-amendment-framework/section-5-level-descriptors", tier: web, consulted: 2026-10-03, pass: P1, outcome: "used, by summary: 2nd edn February 2024, descriptors unchanged; levels 4 to 8 as a university restates them" }
- { ref: "CQFW, via https://connectingcredentials.org/wp-content/uploads/2015/02/Wales-Fan-Diagram-and-Level-Descriptors.pdf", tier: web, consulted: 2026-10-03, pass: P1, outcome: "used, by summary: January 2009; level 3 under its three headings" }
- { ref: "QAA characteristics statements, via https://www.qaa.ac.uk/docs/qaa/quality-code/master's-degree-characteristics-statement.pdf and https://www.qaa.ac.uk/the-quality-code/characteristics-statements/characteristics-statement-doctoral-degrees", tier: professional, consulted: 2026-10-03, pass: P1, outcome: "used, by summary: master's, reflection on own progress and professional responsibility; doctoral, original contribution" }
- { ref: "Vitae RDF, via https://www.casrai.org/guides/vitae-researcher-development-framework", tier: web, consulted: 2026-10-03, pass: P1, outcome: "used, by summary: 2010; four domains, twelve sub-domains" }
- { ref: "Moon (2004) after Hatton and Smith (1995), via https://repository.londonmet.ac.uk/248/1/InvestigationsInUniversityTeachingAndLearning%20v4n2%20p33-41.pdf", tier: web, consulted: 2026-10-03, pass: P1, outcome: "used, by summary: the four types of reflective writing, quoted there from Moon (2004, p. 75)" }
- { ref: "University of Edinburgh, Reflection Toolkit: Gibbs' reflective cycle, via https://reflection.ed.ac.uk/reflectors-toolkit/reflecting-on-experience/gibbs-reflective-cycle", tier: web, consulted: 2026-10-03, pass: P3, outcome: "used, by summary: the six stages (description, feelings, evaluation, analysis, conclusion, action plan) with guiding questions, used as headings for written reflection; the example for the reflective report (D-ing-0044)" }
- { ref: "University of York, Skills Guides: Reflective practice: employability skills, via https://subjectguides.york.ac.uk/skills/reflective-practice", tier: web, consulted: 2026-10-03, pass: P3, outcome: "used, by summary: Gibbs's six stages for reflecting on work experience, with a worked student example separating description from evaluation, conclusion and action plan" }
```

### D3 Wanted sources
<!-- brief: Every source needed and not reached, with what it would settle; ask Abbott when one blocks a section. -->
```yaml
- { id: W-0001, citation: "Jasper, M. (2013) Beginning Reflective Practice. 2nd edn. Cengage", settles: [A9, B1, C1], asked: not yet, state: wanted }
- { id: W-0002, citation: "HCPC (2023) Standards of proficiency (one profession's document, read direct)", settles: [A5c, A10], asked: not yet, state: wanted }
- { id: W-0003, citation: "a glossary of reflective practice vocabulary (for example Bolton and Delderfield, Reflective Practice, latest edition); now also the theory beside the key one (D-ing-0037)", settles: [B2b, A9], asked: META ing, 3 October 2026, state: wanted }
- { id: W-0004, citation: "ESCO: the skill concept for reflecting on one's own practice, with its URI", settles: [A10], asked: not yet, state: wanted }
- { id: W-0005, citation: "NMC (2019) How to revalidate with the NMC, read direct", settles: [A5c, A10], asked: not yet, state: wanted }
- { id: W-0031, citation: "QAA (2024) The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies, 2nd edn, read direct (the level descriptors)", settles: [A11], asked: not yet, state: received (META std:doc:qaa-fheq-2024-framework, 3 October 2026) }
- { id: W-0032, citation: "Welsh Government, CQFW level descriptors, current edition, read direct", settles: [A11], asked: not yet, state: received (META std:doc:welsh-government-cqfw-2009-framework, 3 October 2026) }
- { id: W-0033, citation: "QAA (2020) Characteristics Statements: Master's Degree and Doctoral Degree, read direct", settles: [A11], asked: not yet, state: wanted }
- { id: W-0034, citation: "Vitae (2010) Researcher Development Framework, read direct (the descriptors and phases)", settles: [A11], asked: not yet, state: wanted }
- { id: W-0035, citation: "Moon, J. A. (2004) A Handbook of Reflective and Experiential Learning, RoutledgeFalmer, read direct; with Hatton and Smith (1995); the key theory (D-ing-0037)", settles: [A11, A9], asked: META ing, 3 October 2026, state: wanted }
- { id: W-0053, citation: "Williams, K., Woolliams, M. and Spiro, J. (2020) Reflective Writing. 2nd edn. Red Globe Press (Pocket Study Skills), read direct", settles: [Part E item 12], asked: not yet, state: wanted }
```

## Part E Gaps and questions
<!-- brief: Every unknown, conflict and point for Abbott, as it arises. -->
1. **P2 triggers:** 4 (the external frameworks rest on web and professional sources only) and 5 (all of them read by summary). The A10 crosswalk is editorial and quotes nothing until each is read direct.
2. **Levels:** every capability's `level` is `unknown`. The model ties tiers to experience, not to level, and no source sets an FHEQ level per capability. Settled for every pathway document: `unknown`, with this reason, until a source sets a level (D-ing-0001 (a), Abbott, 21:13).
3. **Capability coverage:** settled. Four capabilities added by the model's author (D-ing-0004 (a), amended, Abbott, 21:29): two Intermediate (critical reflection; a dated action plan) and two Advanced (choosing a fuller model; reflexivity, Advanced only). They are proposed here with temporary ids (c1 to c4) until the model numbers them; the model's own capability list and tier text do not yet show them. [Added 06:37, D-ing-0045: a fifth, c5, Intermediate: the professional-practice reflective report.]
4. **The ERA cycle** has no ingestion document; D:EAU credits it to Jasper (2013) and calls it close to Driscoll (2007) (W-0001).
5. **Conflict:** the HCPC standard on reflection is numbered 10 in one source (AEP guidance, 2026) and 11 in another (AEP resource page, undated, likely the 2015 standards). Both recorded; not settled (W-0002).
6. **The first stage is named two ways:** "describe" (D:EAU, p. 53) and "Experience" (D:EAU, p. 161), the second following Jasper's ERA. Settled: Experience is preferred, describe admitted, so the ERA name holds (D-ing-0002 (a), Abbott, 21:18). The proposed capability reflective-practice/01 still says "describe"; its wording is the model's to change.
7. **Schön and Johns:** settled. The Advanced tier names its fuller models as such as Gibbs, Kolb and Johns; Schön stays a link only, as the theory behind reflective practice rather than a model a student applies (D-ing-0003 (a), Abbott, 21:26). The model's own tier text still names Gibbs and Kolb only; its wording is the model's to change.
8. **Slug:** the id is `ing:doc:pathway-reflective-practice`, not author and year, because the subject is a pathway, not a published work.
9. **Templates:** COMPOSE's GD-edu-12 (reflective account) fits Advanced; an action plan and a reflective journal entry are proposed, not in COMPOSE's catalogue.
10. **Source map:** what *Excelling at University* teaches for each capability, with pages and extracts, belongs in its guide map (held by `path`, draft), not here; the page citations here are only the provenance of claims.
11. **Progression by level (A11):** drafted 02:27 (J-ing-0001; META D-0205). Every level was read by summary only (W-0031 to W-0035); the entries are editorial readings of the descriptors and of Moon's four types of reflective writing. Moon and Bolton are recommended by META's nts as the key theory (Moon key, Bolton beside); not yet ruled, and A9 does not link them. [Ruled 02:43, D-ing-0037 (a): Moon key, Bolton beside, both in A9 and queued at META's ing; Kolb, Gibbs, Johns and Schön stay as the models the tiers teach.] Level 3 uses CQFW's numbering (RQF in England).
12. **The reflective report:** settled (D-ing-0044, Abbott, 06:19): this pathway teaches the professional-practice reflective report, reflection written in typical report format, so report writing is taught here as well as in Researching and Research Methods (research and laboratory report) and Work-Based and Experiential Learning (a context-defined lesson); Academic Writing refers to all three. The example structure (editorial, after Gibbs, 1988, as headings in the Edinburgh Reflection Toolkit and York's Skills Guides): 1 Introduction (the setting, the role and the report's purpose); 2 Description (what happened, factually); 3 Evaluation (what worked and what was challenging, positives first, following the guide's advice at p. 54); 4 Analysis (why, drawing on theory and literature); 5 Conclusion (what was learned, what skills to develop); 6 Action plan (what will be done differently, how and by when); references. Gibbs's feelings stage is folded into description and evaluation. It maps to the ERA cycle: Experience is the description, Reflect the evaluation, analysis and conclusion, Take action the action plan. The guide teaches reflective writing in essay form (pp. 161-163), not in report form. Capability: `reflective-practice/c5`, Intermediate, "Write a professional-practice reflective report in report format" (D-ing-0045, Abbott, 06:37) [was owed, 06:19 to 06:37]. A published study-skills treatment to read direct: W-0053.
13. **Vocabulary (D-ing-0050, Abbott, 11:10):** swept. The guide's glossary terms for this pathway are in B2a (and A4 where new); candidates from the model's tier text are in B2b; A10's direct terms are the term list v1.0 patterns as words, with the ruled second version's changes noted. The search patterns themselves are kept with each consuming project, not here. No published glossary of this pathway's vocabulary has yet been read; B2b stays candidates.

---

## Change notes
- 0.2.21: 4 October 2026, 10:37: A4 gains 3 definitions for terms named in B2a or B4 without one, found by compiling the terminology database (D-ing-0057; ing N-0119).
- 0.2.20: 4 October 2026, 10:03: A10 cards corrected (D-ing-0056): verbs matched to each statement, theory filled from the ruled A9 theory, cards with no process marked as needing one or as not a process (ing N-0113).
- 0.2.19: 3 October 2026, 11:10: vocabulary sweep: 1 glossary terms added to B2a (1 new concepts in A4), 3 candidates to B2b, A10 source note, Part E item 13 (D-ing-0050; ing N-0100).
- 0.2.18: 3 October 2026, 06:37: capability c5 added at Intermediate, the professional-practice reflective report (A3, A10, Part E items 3 and 12) (D-ing-0045; ing N-0094).
- 0.2.17: 3 October 2026, 06:19: the professional-practice reflective report taught here (A2; Part E item 12); Edinburgh and York read for the example (D2); W-0053 (D-ing-0044; ing N-0093).
- 0.2.16: 3 October 2026, 05:52: META runs linked: FHEQ and CQFW linked to META's standards runs; W-0031 and W-0032 received; six META reflection runs linked as related (Finlay, Rolfe, Driscoll, Atkins and Murphy, Boud, Keogh and Walker, Brookfield); PSF linked to its run (J-ing-0002; ing N-0089).
- 0.2.15: 3 October 2026, 04:41: file renamed to `ingest-path-reflective-practice.md`; the id is unchanged (ing N-0083).
- 0.2.14: 3 October 2026, 02:49: level 5's stance renamed investment (D-ing-0039; ing N-0081).
- 0.2.13: 3 October 2026, 02:46: A11: each level gains a metacognitive statement and stance, compliance to flow (D-ing-0038; ing N-0080; G-ing-0144).
- 0.2.12: 3 October 2026, 02:43: key theory Moon (2004), Bolton beside, in A9 and queued at META's ing (D-ing-0037 (a); ing N-0079; G-ing-0142).
- 0.2.11: 3 October 2026, 02:33: A11: each level's understandings gain the learner's understanding of the practice applied to their own development (D-ing-0036; ing N-0077; G-ing-0133).
- 0.2.10: 3 October 2026, 02:32: A11 level 5 gains the understanding that reflective practice can evolve a practitioner identity (D-ing-0035; ing N-0075; G-ing-0129).
- 0.2.9: 3 October 2026, 02:27: A11 progression by level, levels 3 to 8, from META's pathway template 0.3.0-draft; level descriptors and Moon read by summary; W-0031 to W-0035; Part E item 11 (J-ing-0001; META D-0205; ing N-0074; G-ing-0127).
- 0.2.8: 2 October 2026, 23:53: reflective writing as a genre taught here, Academic Writing referring to it; reflective report proposed for the term list (D-ing-0022 (b); ing N-0055; G-ing-0074).
- 0.2.7: 2 October 2026, 21:45: front matter `parts` values quoted so the front matter parses as YAML; no content change (ing N-0024; G-ing-0015).
- 0.2.6: 2 October 2026, 21:37: reflexivity reworded after a quick reading of the wider literature (Bolton; Finlay 2002; qualitative research on positionality; D'Cruz and others 2007, recall): examining how personal identity, values, assumptions and social position shape reflections, judgements and actions (D-ing-0006 (b); ing N-0021, N-0022; G-ing-0012): 0.2, A3, A10, B1.
- 0.2.5: 2 October 2026, 21:32: reflexivity worded as personal identity, values and assumptions, after Social Work England 4.8 (D-ing-0005; ing N-0019, N-0020; G-ing-0011): 0.2, A3, A10, B1.
- 0.2.4: 2 October 2026, 21:29: four capabilities added, c1 to c4, including reflexivity at Advanced only (D-ing-0004 (a), amended; ing N-0018; G-ing-0010): 0.2, A3, A7a, A10, B1, B2a, B2b, B4 and Part E item 3. Also: B1 made valid YAML (`readingLevel` as its own key; one definition quoted); every YAML block now parses.
- 0.2.3: 2 October 2026, 21:26: the Advanced tier names its fuller models as such as Gibbs, Kolb and Johns; Schön a link only (D-ing-0003 (a); ing N-0017; G-ing-0009): 0.2, A3, A9 and Part E item 7.
- 0.2.2: 2 October 2026, 21:18: the first stage is Experience, describe admitted (D-ing-0002 (a); ing N-0016; G-ing-0008): A3, A5a, B1, B2a, C2 and Part E item 6.
- 0.2.1: 2 October 2026, 21:13: Part E item 2 settled, D-ing-0001 (a) (ing N-0015; G-ing-0007).
- 0.2.0: 2 October 2026, 21:00: made generic (ing N-0012; Abbott, 20:52 to 20:56): every reference to a consuming project moved to that project's integration document; the model's authorship kept in Part D only; the model's documents cited as the author's, not by a project's repo path; the head note names the two companion kinds (source maps, integrations); B5's tier-verb rule moved out (it comes from a consumer's voice bands); Part E item 10 replaced by the source map pointer (G-ing-0005).
- 0.1.0: 2 October 2026: researched by INGEST research prompt 0.1.10-draft with META's pathway block 0.1.1-draft (ing N-0004; G-ing-0003).
