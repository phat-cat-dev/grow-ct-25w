---
id: ing:doc:pathway-revising-exams
title: Revising and Exams (academic skills pathway)
aliases: [revision, exams, examinations, exam technique, exam preparation, revision strategy, path:revising-exams]
subjectKind: framework
practices: [education]
primaryPractice: education
streams: [education/academic-skills]
extensions: [education]
parts:
  A: "partial: the capabilities are proposed, not yet confirmed; no Intermediate card; the guide cites no theory; key theory proposed, not ruled"
  B: "partial: concepts and terms named by the model and the guide; associated vocabulary held as candidates"
  C: "full (recommended): the guide gives a five-stage revision strategy and six points of exam strategy"
pins: { structure: 0.11.0-draft, template: 0.10.0-draft, pathwayTemplate: 0.3.0-draft, theory: 0.3.0-draft, terminology: 0.3.0-draft, process: 0.3.0-draft }
status: drafted
researchedBy: INGEST research prompt 0.1.10-draft, with the pathway block of META's `mta-nts-td-pathway-ingest.md` 0.1.1-draft (sections 2 and 2a) and META's pathway template 0.3.0-draft (A11)
passes:
  P1: 4 October 2026
  P2: not run; triggers 4 and 5 hold (Part E, item 1)
  P3: open
version: 0.1.1
---

<!-- from INGEST wpk-0016-ingest-pd-ingestion-document-template.md 0.10.0-draft; the specification is wpk-0016-ingest-pd-ingestion-document-structure.md -->

# Revising and Exams (academic skills pathway)

> **The core document.** Generic: it names no project that uses the pathway. Who made the model and where each claim comes from is in Part D. Companions, never ingested with it: **source maps**, one per guide (`source-maps/excelling-at-university/ingest-path-revising-exams-eau.md`, candidates for `path`'s guide map), **integrations**, one per consuming project (`integrations/<project>/`), and the card integration (`integrations/cards/`, D-ing-0055). A capability's level is `unknown` until a source sets it (D-ing-0001 (a)). Fill note from the template kept until P3.

## Part 0 Summary

### 0.1 Agent definition
<!-- brief: Two or three sentences for an agent: what this is and when to reach for it, and one thing it is not for. Write last, from the finished document. -->
<!-- label: editorial; status: drafted; basis: secondary -->
Revising and Exams is one of thirteen academic skills pathways: preparing for and sitting examinations, from understanding what exams are for and why anxiety arises (the forms of exam, exams as learning tools, why passive revision fails), through building and running a revision strategy (time, gaps, allocation, techniques, monitoring; active against passive revision; cognitive resilience), to active revision techniques and exam-day performance (retrieval, visual, auditory and kinaesthetic techniques matched to the exam, and an exam strategy that manages time). Reach for it to place, sequence or assess a capability in revision or exam performance. It is not about assessment in general or feedback (Understanding Learning, Assessment and Feedback), nor about writing an essay outside exam conditions (Academic Writing).

### 0.2 Summary
<!-- brief: One paragraph: who proposed it, when, what it is, its main use and its main dispute. Write last. -->
<!-- label: both; status: drafted; basis: secondary -->
The academic skills pathways model (2026) sets Revising and Exams as one of thirteen pathways, drawn from one chapter of a study skills guide on revision and exam strategies. It climbs in three tiers: understanding exams and the need for strategy (exams as learning tools, not obstacles; the five forms of exam; exam anxiety and its causes; why passive revision fails); building a revision strategy (the guide's five stages, active against passive learning, time management, targeted revision and cognitive resilience); and active techniques and exam-day performance (visual, auditory and kinaesthetic techniques matched to the exam type, and an exam strategy of arriving early, reading the instructions, allocating time and writing to time). The guide cites no research; the field's evidence on retrieval practice, spacing and test anxiety is gathered here for the key theory. Its open questions are an Intermediate tier with no capability, the guide's framing of techniques by learning preference, which the learning styles research does not support, and which theory to make key (Part E).

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
- Three tiers, Introductory, Intermediate and Advanced, each with a focus, content and a goal (D:PTM, Pathway 8).
- A discrete pathway with one source chapter (D:PTM, Pathway 8, source).
- Less writing-centric; to be pressure-tested before it is built (D:PTM, Pathway 8, flag).
- Tiers are anchored to experience of the practice, not to year of study (D:TSPEC, section 2).

### A2 Core principles
<!-- brief: One item per claim the theory rests on, each cited to the authors. Claims only, not uses or benefits. -->
<!-- label: source; status: drafted; basis: primary -->
- Exams are learning tools that support academic and personal development, not obstacles to excelling (D:EAU, pp. 231-232, 245).
- Exams test much the same criteria as other assessment, depth of knowledge and understanding, critique of the discourse and clear communication, under set conditions; for the tutor they are a leveller across the cohort (D:EAU, p. 232).
- Exams take different forms, essay, multiple-choice, open book, short answer and technical, each with its own demands, and students need the agility to meet each (D:EAU, pp. 232-234).
- Exam anxiety is common and can paralyse; it is reduced by a revision strategy that gives enough time and targets the gaps in knowledge and understanding (D:EAU, pp. 234-235).
- A revision strategy rests on the use of time and the ability to find gaps, and is built in five stages: the time available, the gaps, the allocation of time, the techniques and the monitoring of effectiveness (D:EAU, pp. 235-237).
- Cognitive resilience is the ability to stay focused on objectives while managing pressures such as exams; monitoring the strategy sustains it (D:EAU, p. 237; glossary).
- Passive revision, such as reading a textbook from the start, builds little understanding; active revision, which makes the learner reproduce or test the knowledge, deepens it and aids recall (D:EAU, pp. 237-238, 245).
- Active revision techniques fall into three categories, visual, auditory and kinaesthetic, and switching between them helps sustain cognitive resilience (D:EAU, pp. 238-242).
- Exam strategy is to arrive early, bring what is needed, read the instructions, allocate time to each part including planning, watch the clock and write to time (D:EAU, pp. 243-245).

### A3 Structure
<!-- brief: The spine: every component (level, dimension, stage, category) with its order, parent, the authors' definition (paraphrased, cited), our gloss, key language and an example of our own. Take most care here; other stores link to these components. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
structure: [ladder, set]
components:
  - { slug: introductory, componentType: level, order: 1, parent: none, name: "Introductory: understanding exams and the need for strategy", authorsDefinition: "exams as learning tools, not obstacles; the forms of exam (essay, multiple-choice, open-book, short-answer, technical) and their demands; exam anxiety and its real causes; why passive revision fails (D:PTM, Pathway 8)", gloss: "know what exams ask of you and why a plan beats cramming", keyLanguage: [exam, learning tool, essay exam, multiple-choice, open book, short answer, technical exam, exam anxiety, passive revision], examples: ["reading a module handbook to find which form of exam is set, and what it rewards"], audience: both, beneficiaryGloss: "understand exams and why you need a revision plan", readingLevel: "plain English for a student entering higher education" }
  - { slug: intermediate, componentType: level, order: 2, parent: none, name: "Intermediate: building a revision strategy", authorsDefinition: "the five-stage strategy (time available, identify gaps, allocate time, choose techniques, monitor); active against passive learning applied to revision; time management; targeted revision; cognitive resilience (D:PTM, Pathway 8)", gloss: "plan revision around your time and your gaps, and keep checking it works", keyLanguage: [revision strategy, time management, targeted revision, gaps, active learning, cognitive resilience, monitoring], examples: ["a two-week revision calendar that gives most time to the topics a past paper shows are weakest"], audience: both, beneficiaryGloss: "design a revision plan that fits your time and fills your gaps", readingLevel: "plain English for a student entering higher education" }
  - { slug: advanced, componentType: level, order: 3, parent: none, name: "Advanced: active techniques and exam-day performance", authorsDefinition: "the active-technique toolkit, visual (mind maps, visual note-taking, flashcards, mnemonics, posters), auditory (reading aloud, recordings, discussion), kinaesthetic (spatial placing, role-play, movement, models); matching techniques to exam type; exam-day strategy (arriving early, reading instructions, allocating and planning time per answer, writing to time) (D:PTM, Pathway 8)", gloss: "test yourself actively, and manage the exam itself", keyLanguage: [active revision techniques, self-testing, flashcards, mind map, exam strategy, writing to time], examples: ["self-testing with flashcards on the weakest topics, then a timed answer plan for a past question"], audience: both, beneficiaryGloss: "use active revision and a plan for the exam itself", readingLevel: "plain English for a student entering higher education" }
  - { slug: revising-exams-01, componentType: element, order: 1.1, parent: introductory, name: "Manage exam anxiety and prepare for exams in an organised way", authorsDefinition: "proposed capability, tier note introduced (D:CARDS)", gloss: "keep exam nerves in check by preparing in good time", keyLanguage: [exam anxiety, preparation, organisation], examples: [], audience: both, beneficiaryGloss: "prepare in an organised way so exams feel less frightening", readingLevel: "plain English for a student entering higher education" }
  - { slug: revising-exams-02, componentType: element, order: 3.1, parent: advanced, name: "Convert passive revision into active visual revision techniques", authorsDefinition: "proposed capability, tier note extended; the active against passive framing is the Intermediate tier's, the visual techniques the Advanced tier's (D:CARDS)", gloss: "turn rereading into making and testing", keyLanguage: [passive revision, active revision, mind map, flashcards, visual notes], examples: [], audience: both, beneficiaryGloss: "swap rereading for revision that makes you work with the material", readingLevel: "plain English for a student entering higher education" }
  - { slug: revising-exams-03, componentType: element, order: 3.2, parent: advanced, name: "Use kinaesthetic and role-play revision techniques to deepen engagement with content", authorsDefinition: "proposed capability, tier note extended (D:CARDS)", gloss: "revise by doing: placing, acting out and handling models", keyLanguage: [kinaesthetic, role-play, spatial placing, models], examples: [], audience: both, beneficiaryGloss: "revise through movement and acting things out", readingLevel: "plain English for a student entering higher education" }
  - { slug: revising-exams-04, componentType: element, order: 3.3, parent: advanced, name: "Apply time-managed, targeted revision and exam strategy across question formats", authorsDefinition: "proposed capability, tier note extended; targeted revision and time management are first named at Intermediate (D:CARDS)", gloss: "spend revision and exam time where it counts, whatever the question type", keyLanguage: [targeted revision, time management, exam strategy, question formats], examples: [], audience: both, beneficiaryGloss: "manage your time in revision and in the exam", readingLevel: "plain English for a student entering higher education" }
```
No card sits at Intermediate, which holds the building of a revision strategy (Part E, item 3).

### A4 Concepts used
<!-- brief: The ideas the theory rests on that other theories share; each will become or match a TERMINOLOGY-DAT concept. -->
<!-- label: both; status: drafted; basis: primary -->
- exam: a timed assessment under set conditions that tests knowledge, understanding and critique (D:EAU, pp. 231-232).
- exam-form: a kind of exam with its own demands: essay question, multiple-choice, open book, short answer, technical (D:EAU, pp. 233-234).
- exam-anxiety: anxiety in the build-up to an exam, at worst paralysing (D:EAU, p. 234).
- revision-strategy: a plan for revision built on the use of time and finding gaps in knowledge and understanding (D:EAU, pp. 235-237).
- targeted-revision: revision focused on the gaps a learner has found (D:EAU, p. 236; chapter keywords).
- time-management: allocating realistic time to revision and to each part of an exam (D:EAU, pp. 235-236, 245; chapter keywords).
- cognitive-resilience: the ability to stay focused on objectives while managing pressures, some academic, such as exams (D:EAU, glossary, pp. x-xiii; p. 237).
- active-learning: learning that makes the learner use, reproduce or test knowledge, against passive reception (D:EAU, pp. 237-238).
- active-revision-technique: a revision technique that makes the learner process and reproduce knowledge: visual, auditory or kinaesthetic (D:EAU, pp. 238-242).
- exam-strategy: the decisions a learner makes on the day to manage anxiety and time (D:EAU, pp. 243-245).
- passive-revision: revision that only rereads or reviews, without reproducing or testing the knowledge (D:EAU, pp. 237-238).

Concepts above from `passive-revision` on were added on 4 October 2026, 10:37: terms named in B2a or B4 that had no definition here (D-ing-0057).

### A5a How practitioners apply it
<!-- brief: From the practitioner's side: the steps they take, the tools and artefacts they use, a worked example, and the decisions they make along the way. Separate what the authors prescribe (source) from how it is done in practice (reported, with sources) and what follows from it (editorial). -->
<!-- label: both; status: drafted; basis: primary -->
Practitioners here are tutors, academic skills staff and authors of learning material.

**What the authors prescribe** (source):
- Contrast a disorganised, passive approach (Natalie) with a planned, active one (Jess), in revision and in the exam hall (D:EAU, pp. 234-238, 243-245).
- Ask learners to build their own revision strategy through the five stages, with a friend (D:EAU, p. 237).
- Ask learners to review a past revision as passive or active and choose techniques to make it active, then test them (D:EAU, pp. 242-243).
- Point learners to the module handbook for the form of exam, and to past papers for likely topics (D:EAU, pp. 234, 236).

**How it is done in practice** (reported):
- Tutors run exam preparation sessions before exams (D:EAU, p. 234; evidence: reported).
- Past exam papers are often held in the library (D:EAU, p. 236; evidence: reported).

**Worked example**:
At Introductory, the learner finds the form of their exam in the handbook and names what it rewards and what makes them anxious. At Intermediate, they plot exams on a calendar, find gaps from past papers, allocate short sessions with objectives and review progress weekly. At Advanced, they replace rereading with self-testing and making, match techniques to the exam form, and plan the exam's timings before they start writing (editorial).

### A5b How beneficiaries meet it
<!-- brief: From the beneficiary's side (learner, client, project team, stakeholder): what it asks of them, what they see or do, and any version made for them to use directly. Search for this separately. -->
<!-- label: both; status: drafted; basis: primary -->
- For many students exams cause a great deal of anxiety (D:EAU, pp. 231, 234; evidence: claimed).
- Students often revise by reading textbooks and reviewing lecture notes, a monotonous and passive approach (D:EAU, p. 238; evidence: claimed).
- Revising within a limited time and writing in exam conditions is challenging for many students (D:EAU, p. 232; evidence: claimed).
- Students commonly underestimate the time revision needs, not least because most have several exams (D:EAU, p. 235; evidence: claimed).

### A5c Contexts and adaptations
<!-- brief: Where it is used (levels, sectors, practices, settings, modes such as online), and how it has been adapted for them, each with its source. -->
<!-- label: both; status: drafted; basis: secondary -->
- Any discipline that sets exams; the form varies by discipline, year and the module's intended learning outcomes (D:EAU, p. 232).
- Practice-based disciplines: kinaesthetic techniques suit process-oriented competencies and procedural knowledge (D:EAU, p. 241).
- Retrieval practice: taking a test on studied material improves long-term retention more than restudying it (D:ROEDIGER, by citation; W-0082).
- Learning techniques rated by evidence: practice testing and distributed practice of high utility; highlighting and rereading of low utility (D:DUNLOSKY, by citation; W-0081).
- Spacing: distributed practice improves recall over massed practice, with the best gap depending on the retention interval (D:CEPEDA, by citation; W-0083).
- Test anxiety: a research field of its own, with a cognitive component (worry) linked to lower performance (D:ZEIDNER, D:CASSADY, by citation; W-0084).

### A5d Misapplications
<!-- brief: Common ways it is misused or misread, the evidence for each, and how to avoid it. -->
<!-- label: both; status: drafted; basis: primary -->
- Too little time, no strategy and no targeting: reading the textbook from page one (D:EAU, pp. 234-235; evidence: claimed); build the five-stage strategy.
- Passive revision, reading without recall or testing (D:EAU, p. 237; evidence: claimed); pair every reading session with a technique that makes you reproduce the knowledge.
- Long unbroken sessions (D:EAU, p. 236; evidence: claimed); use shorter, intensive sessions with objectives and breaks.
- Answering the question one recognises a keyword in by writing all one knows, and overrunning on it (D:EAU, pp. 243-244; evidence: claimed); read the question, plan, and write to time.

### A6a Benefits to practitioners
<!-- brief: What those who apply it gain. Mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
- Exams let tutors review performance across a cohort under the same conditions, alongside insight into each student (D:EAU, p. 232; evidence: claimed).

### A6b Benefits to beneficiaries
<!-- brief: Name the beneficiaries, then what reaches them and how it reaches them through the practitioner. Search for this separately; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students.
- Lower exam anxiety and more confidence from an organised strategy (D:EAU, pp. 235, 238; evidence: claimed).
- Deeper understanding and better recall from active revision (D:EAU, pp. 237, 245; evidence: claimed); retrieval and spacing are among the best-evidenced learning techniques (D:DUNLOSKY, by citation).
- Practice in working to time, a professional capability (D:EAU, p. 232; evidence: claimed).

### A7a Criticisms of the theory and its application
<!-- brief: Criticisms of the theory itself and of how practitioners apply it, with the evidence for each, marked measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: secondary -->
- none-stated: no published criticism of this pathway exists.
- (editorial) The guide sorts active techniques into visual, auditory and kinaesthetic and speaks of "visual learners" and of finding which type of learning appeals (D:EAU, pp. 239, 242). Matching teaching to a learner's preferred style has little evidence behind it (D:PASHLER, by citation; W-0085). The techniques themselves are sound where they make the learner retrieve and test; the preference framing is not. Part E, item 6.
- (editorial) The guide's claim that upward eye movements aid recall (D:EAU, p. 240) has no source; it is not carried into this core's claims.
- (editorial) The guide cites no research; the evidence for retrieval practice and spacing supports its emphasis on active revision and self-testing (A5c).

### A7b Effects on beneficiaries
<!-- brief: Name the beneficiaries, then the harms, costs or limits that reach them through the practitioner's use. Search for this separately, as for A6b; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students.
- unknown: no evidence yet of how learners fare in the pathway.
- (editorial) Severe test anxiety may need support beyond study strategy (wellbeing services, reasonable adjustments); the guide does not discuss it.
- (editorial) Framing techniques by learning type may lead a learner to avoid techniques that would help them.

### A8 Selection
<!-- brief: When to choose it over named alternatives, and what it suits badly. Our reading (editorial). -->
<!-- label: editorial; status: drafted; basis: secondary -->
Choose this pathway when the aim is preparing for or sitting an exam. For assessment, criteria and feedback in general, choose `path:understanding-learning-assessment-feedback`; for the essay outside exam conditions, `path:academic-writing`; for motivation and anxiety more widely, `path:starting-progressing-succeeding`. It suits badly a programme assessed wholly by coursework.

### A9 Relations
<!-- brief: Other theories it revises, extends, derives from, contrasts with or competes with, each with a target id and a one-line note. -->
<!-- label: both; status: drafted; basis: primary -->
The guide cites no theory for this chapter. The relations below come from research for the pathway (D2): the evidence on learning techniques, on test anxiety and on self-regulation. No key theory is ruled (Part E, item 4).
```yaml
- { rel: derivedFrom, target: unknown, note: "techniques, proposed lead: Dunlosky, Rawson, Marsh, Nathan and Willingham (2013), ten learning techniques rated by evidence: practice testing and distributed practice high utility, rereading and highlighting low; from catalogue records only; W-0081" }
- { rel: related, target: unknown, note: "techniques: Roediger and Karpicke (2006), test-enhanced learning: retrieval improves long-term retention more than restudy; from catalogue records only; W-0082" }
- { rel: related, target: unknown, note: "techniques: Cepeda, Pashler, Vul, Wixted and Rohrer (2006), distributed practice, a review and quantitative synthesis; from catalogue records only; W-0083" }
- { rel: contrastsWith, target: unknown, note: "techniques: Pashler, McDaniel, Rohrer and Bjork (2008), learning styles: concepts and evidence; little support for matching teaching to a preferred style; against the guide's framing (Part E, item 6); from catalogue records only; W-0085" }
- { rel: derivedFrom, target: unknown, note: "anxiety, proposed lead: Zeidner (1998), Test Anxiety: The State of the Art; with Cassady and Johnson (2002) on cognitive test anxiety; from catalogue records only; W-0084" }
- { rel: related, target: ing:doc:self-regulated-learning-goal-orientation-pintrich-2000, note: "strategy: the revision strategy's planning, monitoring and amending as self-regulation (forethought, monitoring, control, reflection); META INGEST run, SHA-256 prefix ac21ada4f7fd, read there" }
- { rel: related, target: ing:doc:approaches-to-learning-marton-saljo-1976, note: "active against passive: deep and surface approaches to learning; META INGEST run, SHA-256 prefix 2af04640ba6f, read there" }
- { rel: related, target: ing:doc:pathway-understanding-learning-assessment-feedback, note: "exams as one form of assessment; active learning and self-regulation are that pathway's ground (guide, p. 231)" }
- { rel: related, target: ing:doc:pathway-starting-progressing-succeeding, note: "anxiety, resilience and motivation more widely" }
- { rel: related, target: ing:doc:pathway-academic-writing, note: "essay exams ask for argument and critique under time pressure (guide, p. 233)" }
```

### A10 Extension fields
<!-- brief: The practice extension fields for each practice in the front matter, and no others. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
education:
  domain: "cognitive and affective (D:EAU, pp. 231-245)"
  verbs: [manage, prepare, convert, use, deepen, apply]
  learnerLevel: "higher education, any year; tiers anchored to experience of the practice (D:TSPEC, section 2)"
pathway:
  id: path:revising-exams
  title: Revising and Exams
  definition: "Preparing for and sitting examinations: understanding exams as learning tools and their forms, managing exam anxiety, building a revision strategy on time and gaps, revising actively by testing and making, and managing time and decisions on the day."
  terms:
    direct: [examination, exam, exams, revision, revising for, unseen, timed assessment]
    associated: [revision strategy, targeted revision, time management, active learning, active revision techniques, passive revision, cognitive resilience, exam anxiety, exam strategy, past papers, self-testing, flashcards, mind map, multiple-choice, open book, short answer, retrieval practice, spaced practice, test anxiety]
    source: "direct: the pathway term list v1.0 (D:TERMS; its 7 patterns written as words); associated: candidates from D:EAU (its chapter keywords and glossary) and D:PTM (B2b), with the field's terms for the candidate theories (D-ing-0050)"
  competencies:
    - id: revising-exams/01
      tierNote: introduced
      statement: Manage exam anxiety and prepare for exams in an organised way.
      level: unknown
      verbs: [manage, prepare]
      theory: [{unknown: "Zeidner (1998), not yet ingested; W-0084"}]
      process: [revision-strategy]
      professional:
        - statement: Prepares for high-stakes assessments, licensing or professional exams, and manages the pressure of them.
          equivalence: close
          gap: "professional exams gate entry to practice; academic ones a module mark"
          frameworks: ["Vitae RDF B2: self-management"]
    - id: revising-exams/02
      tierNote: extended
      statement: Convert passive revision into active visual revision techniques.
      level: unknown
      verbs: [convert]
      theory: [{unknown: "Dunlosky and others (2013), not yet ingested; W-0081"}]
      process: [revision-strategy]
      professional:
        - statement: Uses active study methods to learn and retain new professional knowledge.
          equivalence: partial
          gap: "workplace learning is less often tested by recall; academic revision is aimed at an exam"
          frameworks: ["Vitae RDF B3: professional and career development"]
    - id: revising-exams/03
      tierNote: extended
      statement: Use kinaesthetic and role-play revision techniques to deepen engagement with content.
      level: unknown
      verbs: [use, deepen]
      theory: [{unknown: "Dunlosky and others (2013), not yet ingested; W-0081"}]
      process: [revision-strategy]
      professional:
        - statement: Rehearses procedures and scenarios physically, as in simulation training.
          equivalence: partial
          gap: "simulation in practice is assessed as performance; academic role-play is a revision aid"
          frameworks: []
    - id: revising-exams/04
      tierNote: extended
      statement: Apply time-managed, targeted revision and exam strategy across question formats.
      level: unknown
      verbs: [apply]
      theory: [{unknown: "Cepeda and others (2006), not yet ingested; W-0083"}, ing:doc:self-regulated-learning-goal-orientation-pintrich-2000]
      process: [revision-strategy, exam-strategy]
      professional:
        - statement: Plans time against priorities and performs to time under pressure.
          equivalence: partial
          gap: "workplace deadlines are negotiated and longer; exams are fixed and short"
          frameworks: ["Vitae RDF B2: self-management"]
  external:
    - { framework: "Vitae Researcher Development Framework", match: ["B2 Self-management"], equivalence: broader }
  processes: [revision-strategy, exam-strategy]
  templates: ["revision plan (proposed)", "active revision technique chooser (proposed)", "exam-day checklist and timing plan (proposed)"]
```
`equivalence` says how the professional form relates to the capability (META D-0175's scale), and in `external` how the framework relates to the pathway. Every item here is editorial. Vitae was read by summary only (Part E, item 1). Theory is proposed until the key theory is ruled (Part E, item 4).

### A11 Progression by level
<!-- brief: How the practice develops across qualification levels 3 to 8, deconstructed at each level into skills, competencies, understandings and literacies (after Lea and Street); level 8 in full; each entry says what changes from the level below; grounded in level descriptors and the key theory. From META's pathway template 0.3.0-draft. -->
<!-- label: both; status: drafted; basis: secondary -->
Each level also carries a metacognitive statement (D-ing-0038, D-ing-0039): what the learner understands about the practice in general and its application, and their stance towards it, on a ladder from applying it because they must (compliance), through knowing why (purpose), investment, ownership and confidence (ownership), to adapting it to personal goals (adaptation) and practising it fluently, applied and communicated as a mode of doing and expression in the service of the disciplinary community (flow). The practice described is revising and sitting exams, never the pathway's tiers. Each level's understandings end with what the practice means for the learner's own development (D-ing-0036). Exams thin out at the upper levels; there the practice becomes self-testing, preparing for oral examination and keeping knowledge current. The descriptors were read by summary only (Part E, item 9). No key theory is ruled (Part E, item 4).
```yaml
progression:
  levelFramework: "qualification levels 3 to 8: CQFW and RQF numbering; FHEQ levels 4 to 8"
  levels:
    - level: 3
      context: "a learner entering higher education: level 3 study, access and foundation years"
      skills: ["make a revision timetable with guidance", "use notes and simple self-tests", "follow exam-hall instructions"]
      competencies: ["revises set material and sits exams with guidance"]
      understandings: ["exams test what has been learned under set conditions", "for own development: starting early makes exams less frightening"]
      literacies: ["revision notes, flashcards, a revision timetable"]
      metacognition: { stance: compliance, statement: "Revises because the exam is coming; reads and rereads, and aims to get through." }
      changesFromBelow: not-applicable-by-design
      sources: [CQFW, EAU]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 4
      context: "the first year of higher education"
      skills: ["identify the form of an exam and what it rewards", "plan revision time across several exams", "name the causes of one's exam anxiety"]
      competencies: ["prepares for each form of exam in an organised way"]
      understandings: ["exams are learning tools, and each form asks something different", "for own development: exam anxiety eases with a plan"]
      literacies: ["a revision calendar; past papers"]
      metacognition: { stance: purpose, statement: "Knows why exams are set and what each form rewards; prepares in good time, mainly for the mark." }
      changesFromBelow: "from revising material to preparing for a particular form of exam"
      sources: [FHEQ, EAU]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 5
      context: "developing practice, depending on the student: the second year"
      skills: ["find gaps from past papers and target revision on them", "replace rereading with self-testing and making", "space sessions and monitor progress against objectives"]
      competencies: ["designs and runs a revision strategy and adjusts it"]
      understandings: ["active revision deepens understanding and aids recall", "for own development: one's own strategy can be tested and improved"]
      literacies: ["a targeted revision plan; self-tests; visual summaries"]
      metacognition: { stance: investment, statement: "Invests in a strategy of their own: monitors what works and changes what does not." }
      changesFromBelow: "from preparing in good time to designing and monitoring a strategy"
      sources: [FHEQ, EAU, DUNLOSKY]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 6
      context: "independent practice: the final undergraduate year"
      skills: ["match techniques to the exam form", "plan and write to time across sections", "synthesise and apply knowledge under time pressure"]
      competencies: ["performs to their level under exam conditions across forms"]
      understandings: ["exams test synthesis and argument under constraint, not recall alone", "for own development: performing under pressure is a capability one owns"]
      literacies: ["timed essay plans; open-book answers; technical solutions"]
      metacognition: { stance: ownership, statement: "Owns their exam practice: chooses techniques and timings with confidence and stays composed." }
      changesFromBelow: "from running a strategy to performing under exam conditions by design"
      sources: [FHEQ, EAU]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 7
      context: "advanced practice: master's study, professional development"
      skills: ["prepare for professional and licensing exams alongside work", "test and maintain specialist knowledge", "prepare for oral examination of a project"]
      competencies: ["sustains specialist knowledge and performs in high-stakes assessment"]
      understandings: ["professional assessment tests applied judgement", "for own development: one's study methods are adapted to each demand"]
      literacies: ["professional exam preparation; project vivas"]
      metacognition: { stance: adaptation, statement: "Adapts revision and exam practice to professional aims; coaches others in it." }
      changesFromBelow: "from module exams to professional and specialist assessment"
      sources: [FHEQ, QAAMSC, VITAE]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 8
      context: "doctoral practice: an original contribution to knowledge, the researcher's identity and independence"
      skills: ["prepare to defend a thesis in a viva", "keep command of a field's literature", "set and examine others' assessments"]
      competencies: ["holds a field in command for oral examination and examines others"]
      understandings: ["examination at this level is a conversation among peers about a contribution", "for own development: knowing a field is kept, not crammed"]
      literacies: ["the viva; examining and moderating"]
      metacognition: { stance: flow, statement: "Command of the field is fluent and tacit, a mode of doing and expression in the flow; they examine and are examined in the service of their disciplinary community." }
      changesFromBelow: "a different kind, not more of level 7: from being examined to examining, and from recall to command of a field"
      sources: [QAADOC, VITAE, FHEQ]
      provenance: { label: both, status: drafted, basis: secondary }
```

## Part B Terminology

### B1 Concepts
<!-- brief: One concept per idea that has a name in this theory (each A3 component, each A4 concept): plain definition, scope note, category, practices. -->
<!-- label: both; status: drafted; basis: primary -->
By rule: one concept per A3 tier and per A4 concept, definition as A3's gloss or A4's line. The exceptions:
```yaml
- slug: five-stage-revision-strategy
  definition: "the guide's five stages for building a revision strategy: time available, gaps, allocation of time, techniques, monitoring"
  beneficiaryDefinition: "five questions to plan your revision"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "the guide's own model (D:EAU, pp. 235-237)"
  category: technique
  practices: [education]
- slug: writing-to-time
  definition: "finishing each answer within the time allocated to it, even if less developed than wished"
  beneficiaryDefinition: "stick to your planned time for each answer"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "the guide's sixth point of exam strategy (D:EAU, p. 245)"
  category: technique
  practices: [education]
```

### B2a Terms named by the authors
<!-- brief: Every name the authors give a concept: preferred and admitted forms, their alternative names and spelling variants, in full (no compact rule); part of speech, register, extension fields. -->
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: exam, form: exam, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: exam, form: examination, lang: en, partOfSpeech: noun, termStatus: admitted, register: general }
- { concept: exam-form, form: essay question exam, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: exam-form, form: multiple-choice question exam, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: exam-form, form: MCQ, lang: en, partOfSpeech: abbreviation, termStatus: admitted, register: general }
- { concept: exam-form, form: open book exam, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: exam-form, form: short answer exam, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: exam-form, form: technical exam, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: exam-anxiety, form: exam anxiety, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: revision-strategy, form: revision strategy, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: targeted-revision, form: targeted revision, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: time-management, form: time management, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: cognitive-resilience, form: cognitive resilience, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: active-learning, form: active learning, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: active-revision-technique, form: active revision techniques, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: exam-strategy, form: exam strategy, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: active-revision-technique, form: mind mapping, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: active-revision-technique, form: visual note-taking, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: active-revision-technique, form: flashcards, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: active-revision-technique, form: mnemonics, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: active-revision-technique, form: role-playing, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: active-revision-technique, form: spatial placing, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
```
Glossary terms placed in this pathway (D:EAU, glossary, pp. x-xiii; D-ing-0050): cognitive resilience; added here: cognitive resilience (the term waiting in the queue). The chapter's keywords (cognitive resilience, revision strategy, active learning, active revision techniques, time management, targeted revision, exam strategy) are all here.
`usableIn` and `bannedIn`: none-stated. Education extension: `sourceType` is `book` for every term from D:EAU.

### B2b Associated vocabulary
<!-- brief: The wider vocabulary practitioners reach for (for Bloom, the verb lists), from at least two named secondary sources, with a scholarly analysis of such lists where one exists. Where none exists, list the words as candidates and put the glossary wanted in D3. One membership per component a word is placed in, with its sources and agreement weight; record where sources disagree with the authors. Never store similarity between words: it is computed from embeddings at query time. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
- { concept: past-papers, form: past exam papers, frameworkBlocks: [{ component: intermediate, sources: [EAU], weight: 1/1 }], status: candidate }
- { concept: self-testing, form: self-testing, frameworkBlocks: [{ component: advanced, sources: [EAU, DUNLOSKY], weight: 2/2 }], status: candidate }
- { concept: retrieval-practice, form: retrieval practice, frameworkBlocks: [{ component: advanced, sources: [ROEDIGER, DUNLOSKY], weight: 2/2 }], status: candidate }
- { concept: testing-effect, form: testing effect, frameworkBlocks: [{ component: advanced, sources: [ROEDIGER], weight: 1/1 }], status: candidate }
- { concept: spaced-practice, form: distributed practice, frameworkBlocks: [{ component: intermediate, sources: [CEPEDA, DUNLOSKY], weight: 2/2 }], status: candidate }
- { concept: interleaving, form: interleaved practice, frameworkBlocks: [{ component: advanced, sources: [DUNLOSKY], weight: 1/1 }], status: candidate }
- { concept: test-anxiety, form: test anxiety, frameworkBlocks: [{ component: introductory, sources: [ZEIDNER, CASSADY], weight: 2/2 }], status: candidate }
- { concept: learning-styles, form: learning styles, frameworkBlocks: [{ component: advanced, sources: [PASHLER], weight: 1/1 }], status: candidate }
- { concept: unseen-exam, form: unseen exam, frameworkBlocks: [{ component: introductory, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: timed-assessment, form: timed assessment, frameworkBlocks: [{ component: introductory, sources: [TERMS], weight: 1/1 }], status: candidate }
```
`learning-styles` is recorded as a term of the field, not endorsed (A7a). No glossary of revision and exam vocabulary was consulted; one is wanted (D3).

### B3 Framework blocks
<!-- brief: For each concept this theory defines its own way: the A3 component, this theory's definition (cited) and its use here. -->
<!-- label: source; status: drafted; basis: primary -->
By rule: each tier concept's framework block is its A3 component and definition. The exceptions:
```yaml
- { concept: cognitive-resilience, component: intermediate, definitionHere: "the ability to stay focused on objectives while managing pressures such as exams (D:EAU, p. 237; glossary)", useHere: "what monitoring the revision strategy sustains" }
- { concept: active-revision-technique, component: advanced, definitionHere: "visual, auditory or kinaesthetic techniques that make the learner process and reproduce knowledge (D:EAU, pp. 238-242)", useHere: "the Advanced toolkit; the categories are the guide's, the evidence for the techniques rests on retrieval and spacing (A7a)" }
```

### B4 Relations
<!-- brief: Broader, narrower, related, contrasts-with and the order within this theory, between the B1 concepts. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: higher-level-than, from: intermediate, to: introductory, note: "tier order" }
- { rel: higher-level-than, from: advanced, to: intermediate, note: "tier order" }
- { rel: narrower, from: exam-form, to: exam, note: "five forms (D:EAU, pp. 233-234)" }
- { rel: narrower, from: targeted-revision, to: revision-strategy, note: "stage 2 (D:EAU, p. 236)" }
- { rel: related, from: revision-strategy, to: cognitive-resilience, note: "monitoring sustains it (D:EAU, p. 237)" }
- { rel: related, from: revision-strategy, to: exam-anxiety, note: "a strategy alleviates it (D:EAU, p. 235)" }
- { rel: contrasts-with, from: active-learning, to: passive-revision, note: "(D:EAU, pp. 237-238)" }
```

### B5 Rules
<!-- brief: Our rules on using the terms (such as a verb banned in outcomes), each with its reason. Editorial. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- understand, know, appreciate, be aware of: not used in learning outcomes at any tier, because they name no observable operation (D:TSPEC, section 6).
- "visual learner" and similar: not used to label a student, pending a ruling, because matching to a preferred style lacks evidence (Part E, item 6).

## Part C Process

### C0 Formality
<!-- brief: Decide first: prescribed, recommended, loose, implied or not applicable, with one sentence on why. If not applicable, stop Part C. -->
<!-- label: both; status: drafted; basis: primary -->
`recommended`: the guide sets five numbered stages for a revision strategy and six numbered points of exam strategy, with contrasting worked examples (D:EAU, pp. 235-237, 245).

### C1 Process models
<!-- brief: Each process the theory lends itself to: what it achieves, shape, scale, what starts it and what counts as done. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: revision-strategy
  summary: build and run a revision strategy for one or more exams
  shape: cycle
  scale: [task]
  scaleNote: "an exam session; monitoring loops back to allocation and techniques"
  groundedIn: [ing:doc:pathway-revising-exams]
  entry: an exam timetable
  exit: readiness for each exam
- slug: exam-strategy
  summary: perform under exam conditions
  shape: linear
  scale: [task]
  scaleNote: "one exam sitting"
  groundedIn: [ing:doc:pathway-revising-exams]
  entry: the exam day
  exit: every required answer written to time
```

### C2 Stages
<!-- brief: Each stage in order: purpose, inputs, activities, outputs, roles, the gate that ends it. Mark our arrangement editorial where the authors give no stages, and every activity the sources do not name `inferred: true`. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { model: revision-strategy, order: 1, name: How much time is available, purpose: "plot exams and set realistic revision hours (D:EAU, pp. 235-236)", inputs: [], activities: [plot exams in a calendar, estimate realistic hours], outputs: [], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: revision-strategy, order: 2, name: Where are the gaps, purpose: "find the topics one is least confident in, from lecture topics and past papers (D:EAU, p. 236)", inputs: [], activities: [review topics, read past papers], outputs: [], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: revision-strategy, order: 3, name: Allocate time, purpose: "give more time to exams with more gaps or harder topics, in short sessions with objectives (D:EAU, p. 236)", inputs: [], activities: [allocate sessions, set objectives, schedule breaks], outputs: [revision-plan], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: revision-strategy, order: 4, name: Choose techniques, purpose: "choose active techniques that make one reproduce and test the knowledge (D:EAU, p. 236)", inputs: [revision-plan], activities: [choose visual, auditory and kinaesthetic techniques], outputs: [], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: revision-strategy, order: 5, name: Monitor effectiveness, purpose: "test oneself, check time and gaps, and sustain cognitive resilience (D:EAU, p. 237)", inputs: [revision-plan], activities: [self-test, review time and gaps, amend the plan], outputs: [], roles: [student], endsAt: strategy-review, repeat: "to stage 3 while exams remain", audience: both }
- { model: exam-strategy, order: 1, name: Arrive early and prepared, purpose: "avoid adding to anxiety; bring all that is needed (D:EAU, p. 245)", inputs: [], activities: [arrive early, bring pens, water, a watch], outputs: [], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: exam-strategy, order: 2, name: Read the instructions, purpose: "know what must be answered and complete the administration (D:EAU, p. 245)", inputs: [], activities: [read the paper's instructions, fill in details], outputs: [], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: exam-strategy, order: 3, name: Allocate time, purpose: "set timings for each part, with time to plan (D:EAU, p. 245)", inputs: [], activities: [note timings on the paper], outputs: [timing-plan], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: exam-strategy, order: 4, name: Plan and write to time, purpose: "plan each answer briefly, watch the clock and finish each answer within its time (D:EAU, p. 245)", inputs: [timing-plan], activities: [plan, write, watch the clock, conclude], outputs: [], roles: [student], endsAt: none, repeat: "for each answer", audience: both }
```
The exam-strategy stages are our arrangement of the guide's six points (editorial).

### C3 Gates
<!-- brief: Each decision point with criteria that can pass or fail, and what it decides. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: strategy-review
  criteria: ["self-tests show the gaps closing", "the time allocated is enough for what remains", "pressure is being managed"]
  decides: "continue | reallocate time | change techniques"
  variationPoint: yes
```

### C4 Outputs
<!-- brief: Each product a stage makes: purpose, parts, and what a template for it needs to know. Mark every output the sources do not name `inferred: true`. Where the method names its own document types, record every one complete (purpose, composition, derivation, quality criteria) from its product descriptions; our templates are drafted from those parts, never the method's text copied. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: revision-plan, purpose: "the revision strategy written down", parts: [exams and dates, available hours, gaps by exam, sessions with objectives, techniques], producedBy: [revision-strategy 3], usedBy: [revision-strategy 4, revision-strategy 5], templateHint: "the revision plan", audience: beneficiary, inferred: true }
- { slug: timing-plan, purpose: "the timings for each part of the exam", parts: [questions to answer, minutes per answer, planning time, move-on times], producedBy: [exam-strategy 3], usedBy: [exam-strategy 4], templateHint: "the exam-day timing plan", audience: beneficiary, inferred: false }
```
The guide names no written revision plan; it asks learners to develop their strategy with a friend (p. 237), so the plan is inferred.

### C5 Roles
<!-- brief: Who does each stage, from both sides: practitioner roles and beneficiary roles. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: student, responsibilities: [build and run a revision strategy, sit exams], stagesInvolved: [all] }
- { slug: revision-partner, responsibilities: [discuss and review strategy and techniques], stagesInvolved: [revision-strategy 1, revision-strategy 5] }
- { slug: tutor, responsibilities: [set exams, run preparation sessions, give feedback], stagesInvolved: [] }
- { slug: invigilator, responsibilities: [conduct the exam], stagesInvolved: [exam-strategy 2] }
```

### C6 Variation points
<!-- brief: Where the process can be tailored or branch, by gate. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- The strategy review loops back to allocation or techniques as gaps close or remain.
- Techniques and exam timings change with the form of exam: recall for multiple-choice, argument for essays, organised access to sources for open book, procedure for technical exams (D:EAU, pp. 233-234).

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
- { key: PTM, author: "Abbott, S.", title: "Academic skills pathways model: pathway tier mapping, Draft v3 (v3.1)", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [0.2, A1, A3, B2b] }
- { key: TSPEC, author: "Abbott, S.", title: "Academic skills pathways model: tier specification v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A1, A10, B5] }
- { key: CARDS, author: "Abbott, S.", title: "Academic skills pathways model: capability cards with tier notes, proposed", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A3, A10] }
- { key: TERMS, author: "Abbott, S.", title: "Academic skills pathways model: pathway term list v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A10, B2b] }
- { key: EAU, author: "Dennis, C. and Abbott, S.", title: "Excelling at University: Academic Literacies and the Development of Graduate Identity", edition: 1st, year: 2026, publisher: Routledge, licence: copyright, tier: primary, readVia: direct, held: not held, citedIn: [A2, A4, A5a, A5b, A5c, A5d, A6a, A6b, A7a, A11, B1, B2a, B2b, B3, B4, C0, C2, C4] }
- { key: FHEQ, author: Quality Assurance Agency for Higher Education, title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies, 2nd edn (level descriptors unchanged from 2014)", year: 2024, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:qaa-fheq-2024-framework, META, SHA-256 prefix 97c52675225e" }
- { key: CQFW, author: Welsh Government, title: "Credit and Qualifications Framework for Wales: level descriptors", year: 2009, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:welsh-government-cqfw-2009-framework, META, SHA-256 prefix 682642ca28c8" }
- { key: QAAMSC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Master's Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: QAADOC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Doctoral Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: VITAE, author: Vitae, title: "Researcher Development Framework", year: 2010, tier: professional, readVia: summary, held: not held, citedIn: [A10, A11] }
```
Not in D1 until read: Dunlosky and others (2013), Roediger and Karpicke (2006), Cepeda and others (2006), Zeidner (1998), Cassady and Johnson (2002), Pashler and others (2008), found as catalogue records only (D2; D3, W-0081 to W-0085). The keys DUNLOSKY, ROEDIGER, CEPEDA, ZEIDNER, CASSADY and PASHLER name those rows. Pintrich (2000) and Marton and Säljö (1976) are read through their META runs (A9).

### D2 Research log
<!-- brief: Every source opened, used or not, as you open it. -->
```yaml
- { ref: PTM, tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: Pathway 8, with its flag" }
- { ref: TSPEC, tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: anchoring and outcome verbs, as for the other pathways" }
- { ref: CARDS, tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: four capabilities; tier notes one introduced, three extended, none developed" }
- { ref: "CARDS tier notes, with their quotations from PTM", tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: the notes on 02 and 04 spanning two tiers" }
- { ref: TERMS, tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: 7 patterns" }
- { ref: EAU, tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: Chapter 13 (pp. 231-245) in full and the glossary entry for cognitive resilience; the chapter cites no research" }
- { ref: "META INGEST runs (UNI library, theory)", tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: Pintrich (2000) and Marton and Säljö (1976) linked in A9; none found for retrieval practice, spacing, test anxiety or learning styles (a listing of the folder)" }
- { ref: "learning techniques and retrieval, via https://pubmed.ncbi.nlm.nih.gov/16507066/ and https://www.readingrockets.org/resources/resource-library/improving-students-learning-effective-learning-techniques-promising", tier: web, consulted: 2026-10-04, pass: P1, outcome: "catalogue records for Roediger and Karpicke (2006) and Dunlosky and others (2013); content not read" }
- { ref: "spacing, via https://pubmed.ncbi.nlm.nih.gov/16719566/", tier: web, consulted: 2026-10-04, pass: P1, outcome: "catalogue record for Cepeda and others (2006); content not read" }
- { ref: "learning styles, via https://digitalcommons.usf.edu/psy_facpub/1765/", tier: web, consulted: 2026-10-04, pass: P1, outcome: "catalogue record for Pashler and others (2008); content not read" }
- { ref: "test anxiety, via https://link.springer.com/book/10.1007/b109548", tier: web, consulted: 2026-10-04, pass: P1, outcome: "catalogue record for Zeidner (1998); Cassady and Johnson (2002) not found by this search, recall" }
- { ref: "FHEQ, CQFW, QAA characteristics statements, Vitae RDF", tier: web, consulted: 2026-10-04, pass: P1, outcome: "used, by summary, as for Reflective Practice's A11" }
```

### D3 Wanted sources
<!-- brief: Every source needed and not reached, with what it would settle; ask Abbott when one blocks a section. -->
```yaml
- { id: W-0081, citation: "Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J. and Willingham, D. T. (2013) Improving students' learning with effective learning techniques, Psychological Science in the Public Interest 14(1), read direct", settles: [A5c, A9, A10], asked: not yet, state: wanted }
- { id: W-0082, citation: "Roediger, H. L. and Karpicke, J. D. (2006) Test-enhanced learning: taking memory tests improves long-term retention, Psychological Science 17(3), read direct", settles: [A5c, A9], asked: not yet, state: wanted }
- { id: W-0083, citation: "Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T. and Rohrer, D. (2006) Distributed practice in verbal recall tasks: a review and quantitative synthesis, Psychological Bulletin 132(3), read direct", settles: [A5c, A9], asked: not yet, state: wanted }
- { id: W-0084, citation: "Zeidner, M. (1998) Test Anxiety: The State of the Art, Plenum; and Cassady, J. C. and Johnson, R. E. (2002) Cognitive test anxiety and academic performance, Contemporary Educational Psychology 27 (recall), read direct", settles: [A5c, A9], asked: not yet, state: wanted }
- { id: W-0085, citation: "Pashler, H., McDaniel, M., Rohrer, D. and Bjork, R. (2008) Learning styles: concepts and evidence, Psychological Science in the Public Interest 9(3), read direct", settles: [A7a, A9], asked: not yet, state: wanted }
- { id: W-0086, citation: "a glossary or textbook of revision and exam vocabulary", settles: [B2b], asked: not yet, state: wanted }
- { id: W-0033, citation: "QAA (2020) Characteristics Statements: Master's and Doctoral Degree, read direct", settles: [A11], asked: not yet, state: wanted }
- { id: W-0034, citation: "Vitae (2010) Researcher Development Framework, read direct", settles: [A10, A11], asked: not yet, state: wanted }
```

## Part E Gaps and questions
<!-- brief: Every unknown, conflict and point for Abbott, as it arises. -->
1. **P2 triggers:** 4 and 5: the level descriptors and Vitae were read by summary only; the candidate theory by catalogue record only (W-0081 to W-0085). The crosswalk is editorial.
2. **Levels:** `unknown` for every capability (D-ing-0001 (a)).
3. **Capability coverage:** no card sits at Intermediate, which holds the building of a revision strategy (the five stages, targeted revision, cognitive resilience); three of the four cards are Advanced. Candidate for the model's author, temporary id: c1 (Intermediate) "Design, run and monitor a revision strategy that targets the gaps in one's knowledge within the time available". Open.
4. **Key theory:** open. The guide cites none. Candidates: Dunlosky and others (2013) for the techniques, with retrieval (Roediger and Karpicke) and spacing (Cepeda and others) beside; Zeidner (1998) for test anxiety; Pintrich (2000), ingested, for the strategy as self-regulation.
5. **Pressure-test:** the model asks for the pathway to be pressure-tested before it is built, being less writing-centric.
6. **Conflict, learning styles:** the guide frames the active techniques as visual, auditory and kinaesthetic and asks which type of learning appeals to the learner (pp. 239, 242); the research finds little support for matching teaching to a preferred style (Pashler and others, 2008). The techniques stand on retrieval and making, not on preference. Recorded as a conflict; the lessons need a ruling on whether to keep the three categories, and how.
7. **Unsupported claim:** that upward eye movements aid recall (p. 240) has no source and is left out.
8. **Templates:** proposed: a revision plan, an active revision technique chooser and an exam-day checklist with a timing plan.
9. **Progression by level (A11):** drafted with the document (J-ing-0001; META D-0205; D-ing-0035, D-ing-0036, D-ing-0038, D-ing-0039). Every level was read by summary only.
10. **Source map:** what *Excelling at University* teaches for each capability is in its source map, not here.
11. **Vocabulary (D-ing-0050):** built in from the start: the glossary term for this pathway (cognitive resilience) in B2a, candidates from the model's tier text and the candidate theories in B2b, A10's direct terms as the term list v1.0 patterns. The search patterns themselves are kept with each consuming project.

---

## Change notes
- 0.1.1: 4 October 2026, 10:37: A4 gains 1 definitions for terms named in B2a or B4 without one, found by compiling the terminology database (D-ing-0057; ing N-0119).
- 0.1.0: 4 October 2026, 10:06: researched by INGEST research prompt 0.1.10-draft with META's pathway block 0.1.1-draft and META's pathway template 0.3.0-draft (A11); generic core with A11, metacognition, the D-ing-0050 vocabulary shape and the D-ing-0056 card fields from the start (ing N-0114).
