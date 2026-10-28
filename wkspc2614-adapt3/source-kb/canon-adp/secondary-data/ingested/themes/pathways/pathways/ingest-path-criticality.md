---
id: ing:doc:pathway-criticality
title: Criticality (academic skills pathway)
aliases: [critical thinking, critical thought, being critical, critical engagement, critical edge, path:criticality]
subjectKind: framework
practices: [education]
primaryPractice: education
streams: [education/academic-skills]
extensions: [education]
parts:
  A: "partial: the capabilities are proposed, not yet confirmed; the theory links are ingested (Barnett, the Delphi report, Bloom revised)"
  B: "partial: concepts and terms named by the model; associated vocabulary held as candidates"
  C: "loose: the guide gives an order through a worked example but warns against treating criticality as steps"
pins: { structure: 0.11.0-draft, template: 0.10.0-draft, pathwayTemplate: 0.3.0-draft, theory: 0.3.0-draft, terminology: 0.3.0-draft, process: 0.3.0-draft }
status: drafted
researchedBy: INGEST research prompt 0.1.10-draft, with the pathway block of META's `mta-nts-td-pathway-ingest.md` 0.1.1-draft (sections 2 and 2a)
passes:
  P1: 2 October 2026
  P2: not run; triggers 4 and 5 hold (Part E, item 1)
  P3: "in part: Part E items 3 to 6 settled"
version: 0.1.13
---

<!-- from INGEST wpk-0016-ingest-pd-ingestion-document-template.md 0.10.0-draft; the specification is wpk-0016-ingest-pd-ingestion-document-structure.md -->

# Criticality (academic skills pathway)

> **The core document.** Generic: it names no project that uses the pathway. Who made the model and where each claim comes from is in Part D. Companions, never ingested with it: **source maps**, one per guide (the first, for *Excelling at University*, held by `path`, draft), and **integrations**, one per consuming project (`integrations/<project>/`). A capability's level is `unknown` until a source sets it (D-ing-0001 (a)). Fill note from the template kept until P3.

## Part 0 Summary

### 0.1 Agent definition
<!-- brief: Two or three sentences for an agent: what this is and when to reach for it, and one thing it is not for. Write last, from the finished document. -->
<!-- label: editorial; status: drafted; basis: secondary -->
Criticality is one of thirteen academic skills pathways: engaging critically with a discipline's discourse, from treating "being critical" as a habit of mind and mapping the discourse, through analysing and evaluating interpretations and reading journal articles strategically, to forming judgements and writing with a critical edge. Reach for it to place, sequence or assess a critical thinking capability, or to translate one into its workplace form. It is not about finding sources, which belongs to Finding and Using Sources, nor about the genres and conventions of academic writing, which belong to Academic Writing, though its Advanced tier shares ground with the latter.

### 0.2 Summary
<!-- brief: One paragraph: who proposed it, when, what it is, its main use and its main dispute. Write last. -->
<!-- label: both; status: drafted; basis: secondary -->
The academic skills pathways model (2026) sets Criticality as one of thirteen pathways, drawn from a study skills guide's chapter on critical thought. Its first move is a reframe: being critical is a mindset that runs through research, planning and writing, not a set of skills switched on for an assessment. It climbs in three tiers: criticality as a mindset (critical choices in research, mapping the discourse, the link to marking criteria); the critical skills in action (analysis, evaluation, evaluative question steers, strategic reading of journal articles, active against passive engagement); and articulating criticality (judgements, synthesis, the language of criticality, discipline-specific vocabulary, the critical edge). It sits beside the established accounts of critical thinking, which mostly list skills and dispositions. Its open questions are coverage at Introductory and Advanced, and where its Advanced tier ends and Academic Writing begins (Part E).

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
- Three tiers, Introductory, Intermediate and Advanced, each with a focus, content, a progression logic and links to other pathways (D:PTM, Pathway 5).
- Progression runs from criticality as mindset, to analysing and evaluating, to articulating judgement and synthesis (D:PTM, Pathway 5).
- The pathway is discrete but overlaps Academic Writing by design; the "writing critically" material is shared between the two (D:PTM, Pathway 5).
- Tiers are anchored to experience of the practice, not to year of study (D:TSPEC, section 2).

### A2 Core principles
<!-- brief: One item per claim the theory rests on, each cited to the authors. Claims only, not uses or benefits. -->
<!-- label: source; status: drafted; basis: primary -->
- Criticality concerns how a student uses the sources found: how far they engage critically with their content while forming their own interpretation (D:EAU, p. 113).
- Being critical is a mindset, part of the approach of a self-regulating student, and more than the skills involved (D:EAU, pp. 114-115).
- Skills-only guidance can reduce critical thought to three or four techniques, suggest it can be learnt like a library tool and suggest it is switched on for an assessment and off afterwards (D:EAU, pp. 114-115).
- Critical thought underpins every main area of generic marking criteria: knowledge and understanding, communication, handling research outcomes, engagement with the discourse and argument (D:EAU, p. 115).
- Critical thought starts at the research stage, in the choice of search terms, filters and sources (D:EAU, pp. 116-117).
- Research should open up the discourse: its scope, key works, influential authors, themes and contentious areas; answering these questions maps it (D:EAU, p. 117).
- Knowledge is built progressively, from foundational sources such as textbooks towards the specific debate (D:EAU, p. 117).
- Analysis breaks an interpretation, body of evidence or data set open by close examination, looking below the surface (D:EAU, p. 119).
- Evaluation assesses the relative value of one factor against others (D:EAU, p. 120).
- Journal articles sit at the cutting edge of research; a lack of them points to a lack of engagement with the discourse (D:EAU, p. 121).
- An argument should be planned before writing: what one will argue, how, and where it sits in the discourse (D:EAU, p. 123).
- In the active approach the writer's point comes first and interpretations are used to support and develop it; in the passive approach interpretations are listed and the point is lost (D:EAU, pp. 124-127).
- A judgement states that one factor matters more than another and says why (D:EAU, pp. 127-128).
- Synthesis draws interpretations and evidence together under the writer's control in the service of their own argument (D:EAU, p. 128).
- The critical edge is subtle: it lies in how interpretations are presented, through the language of criticality and discipline-specific vocabulary (D:EAU, pp. 127, 129-132).

### A3 Structure
<!-- brief: The spine: every component (level, dimension, stage, category) with its order, parent, the authors' definition (paraphrased, cited), our gloss, key language and an example of our own. Take most care here; other stores link to these components. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
structure: [ladder, set]
components:
  - { slug: introductory, componentType: level, order: 1, parent: none, name: "Introductory: criticality as a mindset", authorsDefinition: "being critical as a mindset, not a switch or a tidy skill set; critical thought beginning at the research stage, in the choices a student makes; mapping the discourse (scope, key works, influential authors, themes, contentious areas); the link to marking criteria (D:PTM, Pathway 5)", gloss: "see being critical as a habit of mind that starts with research", keyLanguage: [mindset, discourse, mapping the discourse, marking criteria], examples: ["listing the key authors and the points of disagreement on a topic before deciding what to read in depth"], audience: both, beneficiaryGloss: "learn that being critical is a way of thinking, starting with how you research", readingLevel: "plain English for a student entering higher education" }
  - { slug: intermediate, componentType: level, order: 2, parent: none, name: "Intermediate: the critical skills in action", authorsDefinition: "analysis (breaking an interpretation open); evaluation (assessing the relative value of factors) and recognising evaluative steers; engaging with journal articles strategically through their structure and non-linear reading; active against passive engagement (D:PTM, Pathway 5)", gloss: "analyse and evaluate sources critically", keyLanguage: [analysis, evaluation, "to what extent", journal article, active engagement], examples: ["reading an article's abstract, discussion and conclusion first, then its method only if the findings matter to the essay"], audience: both, beneficiaryGloss: "take sources apart, weigh them against each other and read articles efficiently", readingLevel: "plain English for a student entering higher education" }
  - { slug: advanced, componentType: level, order: 3, parent: none, name: "Advanced: articulating criticality", authorsDefinition: "forming judgements; synthesis (controlling and drawing interpretations together in service of one's argument); the language of criticality; discipline-specific vocabulary; developing the critical edge (D:PTM, Pathway 5)", gloss: "express critical thought with authority", keyLanguage: [judgement, synthesis, language of criticality, critical edge, discipline-specific vocabulary], examples: ["ending a paragraph with 'X therefore matters more than Y, because...' after drawing three studies together"], audience: both, beneficiaryGloss: "make your own judgements clear in writing and use sources to back them", readingLevel: "plain English for a student entering higher education" }
  - { slug: criticality-02, componentType: element, order: 1.1, parent: introductory, name: "Map and question the scholarly discourse around a topic", authorsDefinition: "proposed capability, tier note introduced (D:CARDS)", gloss: "find out what has been said on a topic and where the arguments are", keyLanguage: [discourse, key works, themes, contentious areas], examples: [], audience: both, beneficiaryGloss: "work out who has written what on a topic and where they disagree", readingLevel: "plain English for a student entering higher education" }
  - { slug: criticality-c1, componentType: element, order: 1.2, parent: introductory, name: "Apply critical thought to the choices made when searching, reading and planning", authorsDefinition: "proposed capability, tier note introduced (D-ing-0016 (a), from D:PTM, Pathway 5 and D:EAU, pp. 115-117)", gloss: "be critical from the first search, not only when writing", keyLanguage: [mindset, choices, research stage], examples: [], audience: both, beneficiaryGloss: "think critically about what you search for, read and plan, from the start", readingLevel: "plain English for a student entering higher education" }
  - { slug: criticality-01, componentType: element, order: 2.1, parent: intermediate, name: "Recognise critical thinking skills of analysis and evaluation", authorsDefinition: "proposed capability, tier note developed (D:CARDS)", gloss: "tell analysis and evaluation apart and know when a task asks for each", keyLanguage: [analysis, evaluation, evaluative steer], examples: [], audience: both, beneficiaryGloss: "know what analysis and evaluation mean and spot when a question asks for them", readingLevel: "plain English for a student entering higher education" }
  - { slug: criticality-03, componentType: element, order: 2.2, parent: intermediate, name: "Analyse and evaluate a scholarly interpretation critically", authorsDefinition: "proposed capability, tier note developed (D:CARDS)", gloss: "take an argument apart and weigh it against others", keyLanguage: [analysis, evaluation, interpretation], examples: [], audience: both, beneficiaryGloss: "look below the surface of an argument and judge how much it matters", readingLevel: "plain English for a student entering higher education" }
  - { slug: criticality-04, componentType: element, order: 2.3, parent: intermediate, name: "Critically engage with a journal article's structure and methodology", authorsDefinition: "proposed capability, tier note developed (D:CARDS)", gloss: "read an article strategically, section by section", keyLanguage: [abstract, methodology, results, discussion], examples: [], audience: both, beneficiaryGloss: "use the parts of a journal article to read it quickly and critically", readingLevel: "plain English for a student entering higher education" }
  - { slug: criticality-05, componentType: element, order: 3.1, parent: advanced, name: "Write critically, synthesising sources using discipline-specific vocabulary", authorsDefinition: "proposed capability, tier note extended (D:CARDS)", gloss: "write so that one's own argument leads and sources support it", keyLanguage: [synthesis, language of criticality, discipline-specific vocabulary], examples: [], audience: both, beneficiaryGloss: "draw sources together behind your own point, in your subject's language", readingLevel: "plain English for a student entering higher education" }
  - { slug: criticality-c2, componentType: element, order: 3.2, parent: advanced, name: "Form and justify judgements on the relative importance of factors", authorsDefinition: "proposed capability, tier note extended (D-ing-0016 (a), from D:PTM, Pathway 5 and D:EAU, pp. 127-128)", gloss: "say which factor matters more and why", keyLanguage: [judgement, therefore, because], examples: [], audience: both, beneficiaryGloss: "state clearly what matters most and give your reason", readingLevel: "plain English for a student entering higher education" }
```
Capability ids keep the model's numbering, which does not follow tier order here (02 is Introductory, 01 Intermediate).

### A4 Concepts used
<!-- brief: The ideas the theory rests on that other theories share; each will become or match a TERMINOLOGY-DAT concept. -->
<!-- label: both; status: drafted; basis: primary -->
- discourse: the academic debate found in a discipline's books, edited collections and above all journal articles (D:EAU, p. 115).
- critical-thought: engaging critically with the discourse and communicating that engagement; the guide also calls it "being critical" (D:EAU, pp. 113-115).
- self-regulated-learning: the approach of a learner who plans, monitors and reflects to improve; criticality is part of it (D:EAU, p. 115).
- building-knowledge: building understanding progressively and logically, from foundational sources to the specific debate (D:EAU, p. 117).
- analysis: breaking an interpretation, evidence or data open by close examination (D:EAU, p. 119).
- evaluation: assessing the relative value of a factor against others (D:EAU, p. 120).
- judgement: an evaluative statement that one factor matters more than another, with the reason (D:EAU, p. 128).
- synthesis: drawing interpretations or evidence together in forming and expressing one's own argument (D:EAU, p. 128).
- peer-review: editorial checking of an article's content by other academics in the discipline (D:EAU, p. 121).
- argument: the point a writer makes and supports through the discourse (D:EAU, pp. 123, 128).
- authorial-voice: the writer's own view made visible in the text (D:EAU, p. 125).
- discourse-community: academics joined by a shared discipline who together create and develop its discourse (D:EAU, glossary, pp. x-xiii).
- active-engagement: writing in which the writer's own point comes first and the discourse is used to support and test it (D:EAU, pp. 124-127).
- passive-engagement: writing that lists interpretations from the discourse without the writer's own point leading (D:EAU, pp. 123-127).
- discipline-specific-vocabulary: the terms a discipline uses, one of the ways writing gains its critical edge (D:EAU, pp. 131-132).
- flow: the sense of progression and connection between sentences and paragraphs that makes writing easy to follow (D:EAU, p. 130).
- foundational-knowledge: the overview of a subject, often from textbooks, that a learner needs before engaging with the discourse (D:EAU, p. 117).
- journal-article: a peer-reviewed article reporting research, at the cutting edge of the discourse (D:EAU, pp. 30, 121).
- mapping-the-discourse: identifying a topic's scope, key works, influential authors, themes and contentious areas (D:EAU, p. 117).

Concepts above from `active-engagement` on were added on 4 October 2026, 10:37: terms named in B2a or B4 that had no definition here (D-ing-0057).

### A5a How practitioners apply it
<!-- brief: From the practitioner's side: the steps they take, the tools and artefacts they use, a worked example, and the decisions they make along the way. Separate what the authors prescribe (source) from how it is done in practice (reported, with sources) and what follows from it (editorial). -->
<!-- label: both; status: drafted; basis: primary -->
Practitioners here are tutors, academic skills staff, librarians and authors of learning material.

**What the authors prescribe** (source):
- Show criticality through marking criteria, which make visible what tutors look for (D:EAU, p. 115).
- Follow one student's research from search to plan to show critical choices at each step (D:EAU, pp. 116-123).
- Contrast two writing exemplars on the same topic and the same sources, one passive and one active, and ask learners what differs (D:EAU, pp. 124-127).
- Give learners an extract and ask them to find how its critical edge is made (D:EAU, pp. 132-133).

**How it is done in practice** (reported):
- Guidance on critical thinking, in handbooks and workshops, often focuses on the skills alone (D:EAU, p. 114; evidence: reported).
- Tutors across the disciplines tell students in feedback to "be more critical" (D:EAU, p. 113; evidence: reported).

**Worked example**:
At Introductory, the learner maps the discourse for an essay question: key works, authors, themes and where they disagree. At Intermediate, they analyse two competing interpretations and decide which factor matters more for the question, reading the relevant articles strategically. At Advanced, they write a paragraph that opens with their point, synthesises the interpretations behind it and closes on a judgement, flagged by the language of criticality (editorial).

### A5b How beneficiaries meet it
<!-- brief: From the beneficiary's side (learner, client, project team, stakeholder): what it asks of them, what they see or do, and any version made for them to use directly. Search for this separately. -->
<!-- label: both; status: drafted; basis: primary -->
- Criticality is the literacy students ask about most, because feedback tells them to be more critical without saying what that means (D:EAU, p. 113; evidence: claimed).
- New or less experienced students tend to report every interpretation they have found before, or instead of, their own view (D:EAU, p. 125; evidence: claimed).
- Students who struggle to synthesise are often less confident about the discourse and their own argument (D:EAU, p. 128; evidence: claimed).
- Learners are asked to review their own recent writing for places where a judgement would have made the argument clearer (D:EAU, p. 128; evidence: claimed).

### A5c Contexts and adaptations
<!-- brief: Where it is used (levels, sectors, practices, settings, modes such as online), and how it has been adapted for them, each with its source. -->
<!-- label: both; status: drafted; basis: secondary -->
- Any discipline; journal articles look different by discipline: in the humanities the literature is reviewed throughout, elsewhere in a section of its own (D:EAU, p. 121).
- Most assessment asks for critical thought in writing, though not all assessment is written (D:EAU, p. 113).
- Educational objectives: Bloom's revised taxonomy (2001) names analyse, evaluate and create as cognitive processes, with evaluating defined as judging against criteria and standards (D:BLOOM; read by summary; META's run 0001).
- Critical thinking as expert consensus: the Delphi report (1990) names interpretation, analysis, evaluation, inference, explanation and self-regulation, with dispositions such as open-mindedness and fair-mindedness (D:DELPHI, through META's run 0036, read direct there).
- Higher education as critical being: Barnett (1997) sets criticality across three domains, knowledge, the self and the world, as critical reason, critical self-reflection and critical action (D:BARNETT, through META's run 0035, read direct there; four levels: critical skills, reflexivity, refashioning of traditions, transformatory critique).
- Beyond education: ESCO groups thinking skills into clusters including analysing or processing information and addressing problems (D:ESCO; read by summary).

### A5d Misapplications
<!-- brief: Common ways it is misused or misread, the evidence for each, and how to avoid it. -->
<!-- label: both; status: drafted; basis: primary -->
- Treating critical thought as three or four skills that, once applied, make one critical (D:EAU, p. 114; evidence: claimed); avoid by teaching it as a mindset across research, planning and writing.
- Switching criticality on for an assessment and off afterwards (D:EAU, p. 115; evidence: claimed).
- Describing a source rather than analysing it, "describing the car" rather than lifting the bonnet (D:EAU, p. 119; evidence: claimed).
- Writing before the argument is planned, which produces unfocused, muddled work (D:EAU, p. 123; evidence: claimed); plan first, write second.
- Listing interpretations without using them, the passive approach (D:EAU, pp. 124-125; evidence: claimed).
- Reading every article from start to finish under deadline pressure (D:EAU, pp. 122-123; evidence: claimed); read strategically by section.

### A6a Benefits to practitioners
<!-- brief: What those who apply it gain. Mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
- A shared account of what "be more critical" means, tied to marking criteria, for feedback and teaching (D:EAU, pp. 113, 115; evidence: claimed).
- Paired exemplars that make the critical edge visible and teachable (D:EAU, pp. 124-127; evidence: claimed).

### A6b Benefits to beneficiaries
<!-- brief: Name the beneficiaries, then what reaches them and how it reaches them through the practitioner. Search for this separately; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students; later, employers and the people their decisions serve.
- Work that meets the marking criteria for understanding, engagement and argument (D:EAU, p. 115; evidence: claimed).
- Writing with clearer flow and greater impact on the reader (D:EAU, p. 130; evidence: claimed).
- Strategic reading that saves time under deadlines (D:EAU, pp. 122-123; evidence: claimed).

### A7a Criticisms of the theory and its application
<!-- brief: Criticisms of the theory itself and of how practitioners apply it, with the evidence for each, marked measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: secondary -->
- none-stated: no published criticism of this pathway exists.
- (editorial) The pathway's own reframe is a criticism of skills-only teaching (A5d); its capabilities are nonetheless written as skills, so the mindset the Introductory tier names has no capability of its own (Part E, item 3).
- (editorial) Criticality here works on the discourse of a discipline; the wider accounts (Barnett's self and world, the Delphi dispositions) reach further than this pathway's tiers.

### A7b Effects on beneficiaries
<!-- brief: Name the beneficiaries, then the harms, costs or limits that reach them through the practitioner's use. Search for this separately, as for A6b; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students.
- The critical edge is subtle and nuanced, so learners may not see it without guided comparison (D:EAU, pp. 127, 129; evidence: claimed).
- unknown: no evidence yet of how learners fare in the pathway.

### A8 Selection
<!-- brief: When to choose it over named alternatives, and what it suits badly. Our reading (editorial). -->
<!-- label: editorial; status: drafted; basis: secondary -->
Choose this pathway when the aim is to engage critically with a discipline's discourse and show it. For finding the sources in the first place, choose `path:finding-using-sources`, whose evaluation of sources is the bridge into this one; for the genres, structure and conventions of academic writing, `path:academic-writing`, which shares this pathway's Advanced material; for reflection on one's own learning, `path:reflective-practice`, which the guide calls an extension of critical engagement. It suits badly a learner who needs reasoning in everyday or professional argument outside a discipline's literature.

### A9 Relations
<!-- brief: Other theories it revises, extends, derives from, contrasts with or competes with, each with a target id and a one-line note. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: related, target: ing:doc:critical-lenses-brookfield-1995, note: "Brookfield (1995), the four critical lenses; critical reflection on assumptions; META INGEST run, SHA-256 prefix 742211547d46" }
- { rel: alternativeTo, target: ing:doc:bloom-anderson-krathwohl-2001, note: "names analyse, evaluate and create as cognitive processes; the pathway's Intermediate and Advanced tiers use the same words (Part E, item 4)" }
- { rel: derivedFrom, target: ing:doc:critical-being-barnett-1997, note: "the key theory: Barnett (1997), criticality as critical being across knowledge, the self and the world; the closest account to the pathway's mindset reframe; META INGEST run 0035 (Part E, item 4)" }
- { rel: derivedFrom, target: ing:doc:delphi-report-facione-1990, note: "the Delphi report (Facione, 1990): expert consensus on critical thinking skills and dispositions; the dispositions give the mindset content, the skills match the Intermediate tier; META INGEST run 0036 (Part E, item 4)" }
```

### A10 Extension fields
<!-- brief: The practice extension fields for each practice in the front matter, and no others. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
education:
  domain: "cognitive (D:EAU, pp. 113-133)"
  verbs: [analyse, evaluate, synthesise, judge]
  learnerLevel: "higher education, any year; tiers anchored to experience of engaging with the discourse (D:TSPEC, section 2)"
pathway:
  id: path:criticality
  title: Criticality
  definition: "Engaging critically with a discipline's discourse as a habit of mind: mapping the discourse, analysing and evaluating its interpretations, reading journal articles strategically, and articulating judgement and synthesis in one's own argument with a critical edge."
  terms:
    direct: [critical, critique, evaluation, analysis, appraisal, synthesis]
    associated: [discourse, mapping the discourse, judgement, language of criticality, critical edge, active engagement, discipline-specific vocabulary, peer review]
    source: "direct: the pathway term list v1.0 (D:TERMS; its 7 patterns written as words, analyse and analyze as one); associated: candidates from D:EAU and D:PTM (B2b); it holds critical*, analys*, evaluat* as provisional, matching more than a tenth of benchmark chunks; associated widened from the guide's glossary and the model's tier text (D-ing-0050)"
  competencies:
    - id: criticality/02
      tierNote: introduced
      statement: Map and question the scholarly discourse around a topic.
      level: unknown
      verbs: [map, question]
      theory: [ing:doc:critical-being-barnett-1997, ing:doc:delphi-report-facione-1990]
      process: [critical-engagement]
      professional:
        - statement: Scans a field, market or policy area to find its key players, positions and open questions before acting.
          equivalence: partial
          gap: "the professional scan serves a decision and includes grey literature and people; the academic one maps a scholarly discourse for an assignment"
          frameworks: ["ESCO thinking skills: acquiring and managing information"]
    - id: criticality/c1   # proposed; the model assigns the number
      tierNote: introduced
      statement: Apply critical thought to the choices made when searching, reading and planning.
      level: unknown
      verbs: [apply]
      theory: [ing:doc:critical-being-barnett-1997, ing:doc:delphi-report-facione-1990]
      process: [critical-engagement]
      professional:
        - statement: Questions the sources, scope and assumptions of a piece of work from the start, not only at review.
          equivalence: partial
          gap: "the academic choices are search terms, filters and which sources to read; the professional ones are which evidence, advisers and options to consider"
          frameworks: ["Delphi report (1990): dispositions (inquisitive, open-minded, diligent in seeking relevant information)", "Barnett (1997): critical being"]
    - id: criticality/01
      tierNote: developed
      statement: Recognise critical thinking skills of analysis and evaluation.
      level: unknown
      verbs: [recognise]
      theory: [ing:doc:bloom-anderson-krathwohl-2001, ing:doc:critical-being-barnett-1997, ing:doc:delphi-report-facione-1990]
      process: [critical-engagement]
      professional:
        - statement: Recognises when a brief asks for analysis, for a judgement between options, or for both.
          equivalence: partial
          gap: "workplace briefs rarely use the academic steers ('to what extent', 'assess'); the demand is read from the decision at stake"
          frameworks: ["Revised Bloom's taxonomy: Analyse, Evaluate", "Delphi report (1990): analysis, evaluation"]
    - id: criticality/03
      tierNote: developed
      statement: Analyse and evaluate a scholarly interpretation critically.
      level: unknown
      verbs: [analyse, evaluate]
      theory: [ing:doc:bloom-anderson-krathwohl-2001, ing:doc:critical-being-barnett-1997, ing:doc:delphi-report-facione-1990]
      process: [critical-engagement]
      professional:
        - statement: Analyses an argument, report or proposal and weighs it against the alternatives.
          equivalence: partial
          gap: "the academic object is a scholarly interpretation within a discourse; the professional one is a proposal, report or claim weighed for a decision"
          frameworks: ["Revised Bloom's taxonomy: Analyse, Evaluate", "Delphi report (1990): analysis, evaluation, inference", "ESCO thinking skills: analysing or processing information"]
    - id: criticality/04
      tierNote: developed
      statement: Critically engage with a journal article's structure and methodology.
      level: unknown
      verbs: [engage]
      theory: [ing:doc:critical-being-barnett-1997, ing:doc:delphi-report-facione-1990]
      process: [critical-engagement]
      professional:
        - statement: Reads research and technical reports selectively and checks their method before relying on their findings.
          equivalence: narrower
          gap: "evidence-based professions read research articles directly; most workplaces meet research through reports and summaries"
          frameworks: ["Delphi report (1990): interpretation, evaluation"]
    - id: criticality/05
      tierNote: extended
      statement: Write critically, synthesising sources using discipline-specific vocabulary.
      level: unknown
      verbs: [write, synthesise, use]
      theory: [ing:doc:bloom-anderson-krathwohl-2001, ing:doc:critical-being-barnett-1997, ing:doc:delphi-report-facione-1990]
      process: [critical-engagement]
      professional:
        - statement: Writes a recommendation that draws the evidence together and reaches a justified conclusion in the field's own terms.
          equivalence: partial
          gap: "the professional form leads with the conclusion for a reader who must act; the academic one builds an argument within a discourse for a marker"
          frameworks: ["Revised Bloom's taxonomy: Create", "Delphi report (1990): explanation"]
    - id: criticality/c2   # proposed; the model assigns the number
      tierNote: extended
      statement: Form and justify judgements on the relative importance of factors.
      level: unknown
      verbs: [form, justify]
      theory: [ing:doc:bloom-anderson-krathwohl-2001, ing:doc:critical-being-barnett-1997, ing:doc:delphi-report-facione-1990]
      process: [critical-engagement]
      professional:
        - statement: Recommends one option over others and states why, so that a decision can be taken on it.
          equivalence: partial
          gap: "the academic judgement weighs interpretations within a discourse for a marker; the professional one weighs options for a decision and its consequences"
          frameworks: ["Revised Bloom's taxonomy: Evaluate", "Delphi report (1990): evaluation, explanation"]
  external:
    - { framework: "Bloom's taxonomy revised (Anderson and Krathwohl, 2001)", match: [Analyse, Evaluate, Create], equivalence: broader }
    - { framework: "Delphi report: critical thinking expert consensus (Facione, 1990)", match: [interpretation, analysis, evaluation, inference, explanation, self-regulation], equivalence: broader }
    - { framework: "Barnett (1997): critical being", match: [knowledge domain, critical reason], equivalence: broader }
    - { framework: "ESCO transversal skills: thinking skills and competences", match: [acquiring and managing information, analysing or processing information], equivalence: broader }
  processes: [critical-engagement]
  templates: ["discourse map (proposed)", "article reading map (proposed)", "argument analysis (proposed)", "argument plan (proposed)", "judgement frame (proposed)"]
```
`equivalence` says how the professional form relates to the capability (META D-0175's scale), and in `external` how the framework relates to the pathway. Every item here is editorial. Bloom's revised taxonomy (run 0001), Barnett (run 0035) and the Delphi report (run 0036) are META INGEST runs, linked by id; ESCO was read by summary only and has no ingestion document (Part E, item 1).

### A11 Progression by level
<!-- brief: How the practice develops across qualification levels 3 to 8, deconstructed at each level into skills, competencies, understandings and literacies (after Lea and Street); level 8 in full; each entry says what changes from the level below; grounded in level descriptors and the key theory. From META's pathway template 0.3.0-draft. -->
<!-- label: both; status: drafted; basis: secondary -->
Each level also carries a metacognitive statement (D-ing-0038, D-ing-0039): what the learner understands about the practice in general and its application, and their stance towards it, on a ladder from applying it because they must (compliance), through knowing why (purpose), investment, ownership and confidence (ownership), to adapting it to personal goals (adaptation) and practising it fluently, applied and communicated as a mode of doing and expression in the service of the disciplinary community (flow). The practice described is critical engagement with a discipline's discourse, never the pathway's tiers. Each level's understandings end with what the practice means for the learner's own development (D-ing-0036). The descriptors were read by summary only (Part E). The climb follows Barnett's levels of criticality (1997, META run 0035): critical skills, reflexivity, refashioning of traditions and transformatory critique, across knowledge, the self and the world; the Delphi report's skills and dispositions (META run 0036) give the content at the lower levels.
```yaml
progression:
  levelFramework: "qualification levels 3 to 8: CQFW and RQF numbering; FHEQ levels 4 to 8"
  levels:
    - level: 3
      context: "a learner entering higher education: level 3 study, access and foundation years"
      skills: ["tell fact from opinion", "give reasons for a view", "spot a weak argument"]
      competencies: ["questions a source when prompted"]
      understandings: ["a claim needs evidence", "for own development: questioning what one reads is a habit one can choose"]
      literacies: ["a short argued answer with reasons"]
      metacognition: { stance: compliance, statement: "Questions a source when asked to; sees being critical as finding fault." }
      changesFromBelow: not-applicable-by-design
      sources: [CQFW, DELPHI]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 4
      context: "the first year of higher education"
      skills: ["map the discourse on a topic", "interpret data and arguments using basic theories", "recognise when a question asks for analysis or evaluation"]
      competencies: ["applies critical skills within a discipline's discourse (Barnett: critical skills)"]
      understandings: ["being critical is a mindset from the first search, not a switch for assessment", "for own development: critical thought is what tutors mean by 'be more critical', and it can be practised"]
      literacies: ["notes and essays that report interpretations and begin to weigh them"]
      metacognition: { stance: purpose, statement: "Knows why critical thought is valued and what 'be more critical' means; applies critical skills when the task signals them." }
      changesFromBelow: "from reasons for one's own view to engaging with a discourse"
      sources: [FHEQ, BARNETT, DELPHI]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 5
      context: "developing practice, depending on the student: the second year"
      skills: ["analyse and evaluate interpretations against each other", "read journal articles strategically", "use sources actively in support of one's own point"]
      competencies: ["evaluates the appropriateness of different approaches and judges their relative value"]
      understandings: ["interpretations are contested and situated", "for own development: one's own assumptions shape how one reads, and can be examined (Barnett: reflexivity begins)"]
      literacies: ["essays in the active approach: one's point first, sources behind it"]
      metacognition: { stance: investment, statement: "Invests in their own point of view, using sources to support it; begins to see critical thought as a way of thinking rather than a technique." }
      changesFromBelow: "from engaging with a discourse to evaluating it and using it to support one's own argument"
      sources: [FHEQ, BARNETT, BLOOM]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 6
      context: "independent practice: the final undergraduate year"
      skills: ["form and justify judgements", "synthesise interpretations under one's own argument", "use the language of criticality and discipline vocabulary"]
      competencies: ["devises and sustains arguments using ideas at the forefront of the discipline (Barnett: reflexivity)"]
      understandings: ["one's own position is part of the argument", "for own development: an authorial voice is part of the graduate one is becoming"]
      literacies: ["a dissertation or extended essay with a critical edge"]
      metacognition: { stance: ownership, statement: "Owns an authorial voice and position, confident in judgement and synthesis; critical thought is a habit across research, planning and writing." }
      changesFromBelow: "from evaluating to judging and synthesising, with one's own voice and position in view"
      sources: [FHEQ, BARNETT]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 7
      context: "advanced practice: master's study, professional practice"
      skills: ["critique methodologies and the frameworks of a field", "propose alternatives to established interpretations"]
      competencies: ["refashions the traditions of a field in one's own work (Barnett: refashioning of traditions)"]
      understandings: ["a field's frameworks can be questioned, not only used", "for own development: critical being extends to professional action, not only to texts"]
      literacies: ["a master's dissertation that critiques and reframes"]
      metacognition: { stance: adaptation, statement: "Adapts critique to fields, frameworks and professional problems, questioning frames as well as claims; communicates critique so others can use it." }
      changesFromBelow: "from judging within a field to questioning and reframing the field's own frameworks"
      sources: [FHEQ, QAAMSC, BARNETT]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 8
      context: "doctoral practice: an original contribution to knowledge, the researcher's identity and independence"
      skills: ["generate new frameworks or understandings", "defend an original position against peers"]
      competencies: ["acts as a critical being in knowledge, the self and the world: transformatory critique"]
      understandings: ["critique can make new knowledge and change practice", "for own development: the researcher's critical identity is formed through the contribution and its defence"]
      literacies: ["the thesis and its defence; peer review given and received"]
      metacognition: { stance: flow, statement: "Critical being is a mode of doing and expression, fluent and in the flow; critique becomes transformatory, communicated to make new knowledge in the service of their disciplinary community." }
      changesFromBelow: "a different kind, not more of level 7: critique becomes transformatory, making knowledge rather than appraising it"
      sources: [QAADOC, BARNETT, VITAE]
      provenance: { label: both, status: drafted, basis: secondary }
```

## Part B Terminology

### B1 Concepts
<!-- brief: One concept per idea that has a name in this theory (each A3 component, each A4 concept): plain definition, scope note, category, practices. -->
<!-- label: both; status: drafted; basis: primary -->
By rule: one concept per A3 tier and per A4 concept, definition as A3's gloss or A4's line. The exceptions:
```yaml
- slug: critical-edge
  definition: the quality of writing that makes the writer's understanding of the discourse and critical engagement with it visible to the reader
  beneficiaryDefinition: "the part of your writing that shows you are thinking about your sources, not just reporting them"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "made by presentation: an active approach, the language of criticality and discipline-specific vocabulary (D:EAU, pp. 127, 129-132)"
  category: quality
  practices: [education]
- slug: language-of-criticality
  definition: words and phrases, often at the start of a sentence, that show the relationship between interpretations and so flag critical engagement (however, therefore, although, moreover, furthermore)
  beneficiaryDefinition: "linking words that show how sources relate and what you think of them"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "the guide's own term; also improves flow (D:EAU, pp. 129-130)"
  category: technique
  practices: [education]
- slug: evaluative-steer
  definition: an assessment question's opening that asks for evaluation, such as "To what extent", "How far" or "Assess"
  scopeNote: "'Assess' is less explicit than the other two (D:EAU, p. 120)"
  category: technique
  practices: [education]
```

### B2a Terms named by the authors
<!-- brief: Every name the authors give a concept: preferred and admitted forms, their alternative names and spelling variants, in full (no compact rule); part of speech, register, extension fields. -->
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: critical-thought, form: critical thought, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: critical-thought, form: being critical, lang: en, partOfSpeech: verb-phrase, termStatus: admitted, register: general }
- { concept: critical-thought, form: critical thinking, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: critical-thought, form: criticality, lang: en, partOfSpeech: noun, termStatus: admitted, register: discipline-specific }
- { concept: discourse, form: discourse, lang: en, partOfSpeech: noun, termStatus: preferred, register: discipline-specific }
- { concept: discourse, form: academic discourse, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: discipline-specific }
- { concept: mapping-the-discourse, form: mapping the discourse, lang: en, partOfSpeech: verb-phrase, termStatus: preferred, register: discipline-specific }
- { concept: mapping-the-discourse, form: opening up the discourse, lang: en, partOfSpeech: verb-phrase, termStatus: admitted, register: discipline-specific }
- { concept: building-knowledge, form: building knowledge, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: foundational-knowledge, form: foundational knowledge, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: analysis, form: analysis, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: evaluation, form: evaluation, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: evaluative-steer, form: question steer, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: journal-article, form: journal article, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: journal-article, form: research article, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: peer-review, form: peer-reviewed, lang: en, partOfSpeech: adjective, termStatus: preferred, register: discipline-specific }
- { concept: active-engagement, form: active approach, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: passive-engagement, form: passive approach, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: judgement, form: judgement, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: synthesis, form: synthesis, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: language-of-criticality, form: language of criticality, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: critical-edge, form: critical edge, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: discipline-specific-vocabulary, form: discipline-specific vocabulary, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: authorial-voice, form: authorial voice, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: flow, form: flow, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: discourse-community, form: discourse community, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

Glossary terms placed in this pathway (D:EAU, glossary, pp. x-xiii; D-ing-0050): analysis, criticality, discourse, discourse community, evaluation, language of criticality, synthesis; added here: discourse community.
`usableIn` and `bannedIn`: none-stated. Education extension: `sourceType` is `book` for every term from D:EAU; the rest unknown.

### B2b Associated vocabulary
<!-- brief: The wider vocabulary practitioners reach for (for Bloom, the verb lists), from at least two named secondary sources, with a scholarly analysis of such lists where one exists. Where none exists, list the words as candidates and put the glossary wanted in D3. One membership per component a word is placed in, with its sources and agreement weight; record where sources disagree with the authors. Never store similarity between words: it is computed from embeddings at query time. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
- { concept: critique, form: critique, frameworkBlocks: [{ component: intermediate, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: appraisal, form: appraisal, frameworkBlocks: [{ component: intermediate, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: inference, form: inference, frameworkBlocks: [{ component: intermediate, sources: [DELPHI], weight: 1/1 }], status: candidate }
- { concept: create, form: create, frameworkBlocks: [{ component: advanced, sources: [BLOOM], weight: 1/1 }], status: candidate }
- { concept: critical-being, form: critical being, frameworkBlocks: [{ component: introductory, sources: [BARNETT], weight: 1/1 }], status: candidate }
- { concept: disposition, form: critical thinking disposition, frameworkBlocks: [{ component: introductory, sources: [DELPHI], weight: 1/1 }], status: candidate }
- { concept: evaluative-steer, form: evaluative steer, frameworkBlocks: [{ component: intermediate, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: structural-map, form: structural map, frameworkBlocks: [{ component: intermediate, sources: [PTM], weight: 1/1 }], status: candidate }
```
The verbs of Bloom's revised taxonomy are held in META's run 0001; no glossary of critical thinking vocabulary was consulted, and one is wanted (D3).

### B3 Framework blocks
<!-- brief: For each concept this theory defines its own way: the A3 component, this theory's definition (cited) and its use here. -->
<!-- label: source; status: drafted; basis: primary -->
By rule: each tier concept's framework block is its A3 component and definition. The exceptions:
```yaml
- { concept: evaluation, component: intermediate, definitionHere: "assessing the relative value of a factor against others (D:EAU, p. 120)", useHere: "narrower than Bloom's 'judge against criteria and standards': here it is always comparative" }
- { concept: judgement, component: advanced, definitionHere: "X is more important than Y because ... (D:EAU, p. 128)", useHere: "the Advanced statement of understanding and the signpost of an argument" }
```

### B4 Relations
<!-- brief: Broader, narrower, related, contrasts-with and the order within this theory, between the B1 concepts. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: higher-level-than, from: intermediate, to: introductory, note: "tier order" }
- { rel: higher-level-than, from: advanced, to: intermediate, note: "tier order" }
- { rel: related, from: evaluation, to: judgement, note: "evaluation is closely linked to judgement (D:EAU, p. 120)" }
- { rel: contrasts-with, from: active-engagement, to: passive-engagement, note: "the writer's point first against interpretations listed (D:EAU, pp. 124-127)" }
- { rel: narrower, from: language-of-criticality, to: critical-edge, note: "one of the ways the edge is made (D:EAU, pp. 129-130)" }
- { rel: narrower, from: discipline-specific-vocabulary, to: critical-edge, note: "another (D:EAU, pp. 131-132)" }
- { rel: related, from: critical-thought, to: self-regulated-learning, note: "reflection on learning is an extension of critical engagement with sources (D:EAU, p. 115)" }
```

### B5 Rules
<!-- brief: Our rules on using the terms (such as a verb banned in outcomes), each with its reason. Editorial. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- understand, know, appreciate, be aware of: not used in learning outcomes at any tier, because they name no observable operation (D:TSPEC, section 6).
- "be critical" or "be more critical": not used in an outcome without saying which operation (analyse, evaluate, judge, synthesise) is meant, because the guide shows learners cannot act on it unexplained (D:EAU, p. 113).

## Part C Process

### C0 Formality
<!-- brief: Decide first: prescribed, recommended, loose, implied or not applicable, with one sentence on why. If not applicable, stop Part C. -->
<!-- label: both; status: drafted; basis: primary -->
`loose`: the guide follows one student from mapping the discourse to writing in an order that can be read as stages, but it says criticality is a mindset that runs through all of them, not a sequence of skills (D:EAU, pp. 114-117, 123).

### C1 Process models
<!-- brief: Each process the theory lends itself to: what it achieves, shape, scale, what starts it and what counts as done. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: critical-engagement
  summary: engage critically with a discourse and articulate one's own position within it
  shape: iterative
  scale: [task]
  scaleNote: "one assessment; the same engagement runs through longer work (D:EAU, pp. 116-133)"
  groundedIn: [ing:doc:pathway-criticality]
  entry: an assessment question and the sources found for it
  exit: writing that states and supports a position within the discourse
```

### C2 Stages
<!-- brief: Each stage in order: purpose, inputs, activities, outputs, roles, the gate that ends it. Mark our arrangement editorial where the authors give no stages, and every activity the sources do not name `inferred: true`. -->
<!-- label: both; status: drafted; basis: primary -->
The arrangement into stages is editorial, from the guide's worked example.
```yaml
- { model: critical-engagement, order: 1, name: Map the discourse, purpose: "find its scope, key works, authors, themes and contentious areas, building from foundational sources (D:EAU, pp. 117-118)", inputs: [], activities: [review own knowledge, read foundational sources, note themes and key authors], outputs: [discourse-map], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: critical-engagement, order: 2, name: Analyse interpretations, purpose: "break each interpretation open and place it in the discourse (D:EAU, pp. 119-120)", inputs: [discourse-map], activities: [trace the argument through key points, read the discussion closely], outputs: [analysis-notes], roles: [student], endsAt: none, repeat: "for each interpretation", audience: both }
- { model: critical-engagement, order: 3, name: Engage with journal articles, purpose: "read articles strategically by section (D:EAU, pp. 121-123)", inputs: [discourse-map], activities: [read abstract, introduction, results, discussion; return to method if needed], outputs: [analysis-notes], roles: [student], endsAt: none, repeat: "for each article", audience: both }
- { model: critical-engagement, order: 4, name: Evaluate and judge, purpose: "weigh factors against each other and reach a judgement (D:EAU, pp. 120, 127-128)", inputs: [analysis-notes], activities: [compare the relative value of factors, state which matters more and why], outputs: [argument-plan], roles: [student], endsAt: argument-clear, repeat: none, audience: both }
- { model: critical-engagement, order: 5, name: Write critically, purpose: "articulate the argument actively, with synthesis and a critical edge (D:EAU, pp. 123-132)", inputs: [argument-plan], activities: [lead with the point, synthesise interpretations, use the language of criticality and discipline vocabulary, end on judgements], outputs: [critical-writing], roles: [student], endsAt: none, repeat: none, audience: both }
```

### C3 Gates
<!-- brief: Each decision point with criteria that can pass or fail, and what it decides. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: argument-clear
  criteria: ["the writer knows what they will argue, how, and where it sits in the discourse (D:EAU, p. 123)"]
  decides: "write | return to stages 1 to 3"
  variationPoint: no
```

### C4 Outputs
<!-- brief: Each product a stage makes: purpose, parts, and what a template for it needs to know. Mark every output the sources do not name `inferred: true`. Where the method names its own document types, record every one complete (purpose, composition, derivation, quality criteria) from its product descriptions; our templates are drafted from those parts, never the method's text copied. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: discourse-map, purpose: "a picture of the discourse on a topic", parts: [scope, key works, influential authors, themes, contentious areas, gaps in own knowledge], producedBy: [1], usedBy: [2, 3], templateHint: "a page or note-making app; the guide's own questions as headings (D:EAU, p. 117)", audience: beneficiary, inferred: false }
- { slug: analysis-notes, purpose: "each interpretation broken open", parts: [source, argument, key points, place in the discourse], producedBy: [2, 3], usedBy: [4], templateHint: "one block per source; for articles, a row per section read", audience: beneficiary, inferred: true }
- { slug: argument-analysis, purpose: "break down another writer's argument", parts: [claim, reasons, evidence, assumptions, counter-arguments, place in the discourse], producedBy: [2, 3], usedBy: [4], templateHint: "one per interpretation; deconstructing others' arguments, the counterpart of the argument plan (D-ing-0026)", audience: beneficiary, inferred: true }
- { slug: argument-plan, purpose: "formulate one's own argument before writing", parts: [point, judgements, interpretations that support or qualify each], producedBy: [4], usedBy: [5], templateHint: "the judgement frame: X matters more than Y because; cross-referenced from Academic Writing's essay plan (D-ing-0026)", audience: beneficiary, inferred: true }
- { slug: critical-writing, purpose: "the assessed text", parts: [point first, synthesised interpretations, judgements], producedBy: [5], usedBy: [], templateHint: "not a template; checked against the active approach", audience: beneficiary, inferred: true }
```

### C5 Roles
<!-- brief: Who does each stage, from both sides: practitioner roles and beneficiary roles. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: student, responsibilities: [map, analyse, read, evaluate, judge, write], stagesInvolved: [1, 2, 3, 4, 5] }
- { slug: tutor, responsibilities: [set the question, give feedback against the marking criteria], stagesInvolved: [5] }
```

### C6 Variation points
<!-- brief: Where the process can be tailored or branch, by gate. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- Stages 1 to 4 loop: analysis or an article can reopen the map, and a judgement can send the learner back to the sources.
- Every tier: the discipline changes the shape of journal articles, the vocabulary and the weight of each source type, never the demand.

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
- { key: PTM, author: "Abbott, S.", title: "Academic skills pathways model: pathway tier mapping, Draft v3 (v3.1)", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [0.2, A1, A3, B3] }
- { key: TSPEC, author: "Abbott, S.", title: "Academic skills pathways model: tier specification v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A1, A10, B5] }
- { key: CARDS, author: "Abbott, S.", title: "Academic skills pathways model: capability cards with tier notes, proposed", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A3, A10] }
- { key: TERMS, author: "Abbott, S.", title: "Academic skills pathways model: pathway term list v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A10, B2b] }
- { key: EAU, author: "Dennis, C. and Abbott, S.", title: "Excelling at University: Academic Literacies and the Development of Graduate Identity", edition: 1st, year: 2026, publisher: Routledge, licence: copyright, tier: primary, readVia: direct, held: not held, citedIn: [A2, A4, A5a, A5b, A5c, A5d, A6a, A6b, A7b, B1, B3, B4, B5, C0, C1, C2, C3, C4] }
- { key: BLOOM, author: "Anderson, L. W. and Krathwohl, D. R. (eds)", title: "A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives", year: 2001, publisher: Longman, tier: secondary, readVia: summary, held: not held, citedIn: [A5c, A9, A10, B2b, B3] }
- { key: DELPHI, author: "Facione, P. A.", title: "Critical Thinking: A Statement of Expert Consensus for Purposes of Educational Assessment and Instruction (the Delphi Report)", year: 1990, publisher: American Philosophical Association, tier: secondary, readVia: inherited, held: not held, citedIn: [A5c, A9, A10, B2b] }
- { key: BARNETT, author: "Barnett, R.", title: "Higher Education: A Critical Business", year: 1997, publisher: "SRHE and Open University Press", tier: secondary, readVia: inherited, held: not held, citedIn: [A5c, A7a, A9, A10, B2b] }
- { key: ESCO, author: European Commission, title: "A terminology on transversal skills and competences and its integration in ESCO, v1.1", year: 2021, tier: professional, readVia: summary, held: not held, citedIn: [A5c, A10] }
- { key: FHEQ, author: Quality Assurance Agency for Higher Education, title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies, 2nd edn (level descriptors unchanged from 2014)", year: 2024, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:qaa-fheq-2024-framework, META, SHA-256 prefix 97c52675225e" }
- { key: CQFW, author: Welsh Government, title: "Credit and Qualifications Framework for Wales: level descriptors", year: 2009, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:welsh-government-cqfw-2009-framework, META, SHA-256 prefix 682642ca28c8" }
- { key: QAAMSC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Master's Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: QAADOC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Doctoral Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: VITAE, author: Vitae, title: "Researcher Development Framework", year: 2010, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
```

### D2 Research log
<!-- brief: Every source opened, used or not, as you open it. -->
```yaml
- { ref: PTM, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: Pathway 5" }
- { ref: TSPEC, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: anchoring and outcome verbs" }
- { ref: CARDS, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: five capabilities with tier notes" }
- { ref: TERMS, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: 7 patterns" }
- { ref: EAU, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: Ch 8 pp. 113-133" }
- { ref: "Revised Bloom's taxonomy, via https://www.celt.iastate.edu/teaching/effective-practice/revised-blooms-taxonomy/", tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: the six processes; analyse and evaluate defined" }
- { ref: "Delphi report, via https://sacscoc.shsu.edu/Support Docs/8.2.b/56 - Critical Thinking Sub-committee Report.pdf", tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: the skills and the dispositions" }
- { ref: "Barnett (1997), via https://srhe.ac.uk/arc/conference2010/abstracts/0088.pdf", tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: three domains and three forms; the levels not given there" }
- { ref: ESCO, tier: professional, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: the thinking skills clusters; no single 'think critically' concept found in the summary" }
- { ref: "META INGEST runs 0035 and 0036", tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: ing:doc:critical-being-barnett-1997 0.1.1 (SHA-256 prefix cd3264781b01) and ing:doc:delphi-report-facione-1990 0.1.0 (458621896a2d), at UNI 47f1f4f; recalled levels, skills and dispositions matched" }
- { ref: "META INGEST run queue", tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: Bloom revised is run 0001 (`ing:doc:bloom-anderson-krathwohl-2001`); no run for Barnett or the Delphi report" }
- { ref: "FHEQ, CQFW, QAA characteristics statements, Vitae RDF", tier: web, consulted: 2026-10-03, pass: P1, outcome: "used, by summary, as for Reflective Practice's A11 (its D2 lists the pages)" }
```

### D3 Wanted sources
<!-- brief: Every source needed and not reached, with what it would settle; ask Abbott when one blocks a section. -->
```yaml
- { id: W-0019, citation: "Barnett, R. (1997) Higher Education: A Critical Business, SRHE and Open University Press, read direct (the levels of criticality are recall: critical skills, reflexivity, refashioning of traditions, transformatory critique)", settles: [A5c, A9, A10], asked: META ing, 2 October 2026, state: received (META run 0035, 2 October 2026) }
- { id: W-0020, citation: "Facione, P. A. (1990) Critical Thinking: A Statement of Expert Consensus for Purposes of Educational Assessment and Instruction, American Philosophical Association, read direct", settles: [A5c, A9, A10], asked: META ing, 2 October 2026, state: received (META run 0036, 2 October 2026) }
- { id: W-0021, citation: "ESCO, the transversal skill concepts for critical thinking, read direct in the ESCO portal", settles: [A10], asked: not yet, state: wanted }
- { id: W-0031, citation: "QAA (2024) FHEQ, 2nd edn, read direct (the level descriptors)", settles: [A11], asked: not yet, state: received (META std:doc:qaa-fheq-2024-framework, 3 October 2026) }
- { id: W-0032, citation: "CQFW level descriptors, current edition, read direct", settles: [A11], asked: not yet, state: received (META std:doc:welsh-government-cqfw-2009-framework, 3 October 2026) }
- { id: W-0033, citation: "QAA (2020) Characteristics Statements: Master's and Doctoral Degree, read direct", settles: [A11], asked: not yet, state: wanted }
- { id: W-0034, citation: "Vitae (2010) Researcher Development Framework, read direct", settles: [A11], asked: not yet, state: wanted }
```

## Part E Gaps and questions
<!-- brief: Every unknown, conflict and point for Abbott, as it arises. -->
1. **P2 triggers:** 4 and 5 now hold for ESCO only (W-0021): Barnett and the Delphi report are read direct in META's runs 0035 and 0036 (W-0019, W-0020 received), and the recalled levels, skills and dispositions matched. The crosswalk is editorial.
2. **Levels:** `unknown` for every capability (D-ing-0001 (a)).
3. **Capability coverage:** settled. Two capabilities added by the model's author (D-ing-0016 (a), Abbott, 23:10): c1 "Apply critical thought to the choices made when searching, reading and planning" (Introductory) and c2 "Form and justify judgements on the relative importance of factors" (Advanced), with temporary ids until the model numbers them.
4. **Theory links:** settled (D-ing-0017 (a), Abbott, 23:14): Barnett's critical being (1997) is the key theory and the Delphi report (Facione, 1990) sits beside it, both queued at META's ing; Bloom's revised taxonomy stays linked (META's run 0001). A9's targets and the capabilities' `theory:` fill in when the documents exist (W-0019, W-0020). Linked 23:51: `ing:doc:critical-being-barnett-1997` (run 0035) and `ing:doc:delphi-report-facione-1990` (run 0036), in A9 and every capability's `theory:`.
5. **Overlap with Academic Writing:** settled (D-ing-0020 (a), Abbott, 23:38): Criticality teaches the critical edge, the language of criticality, synthesis and judgement (`criticality/05` and its judgement capability stay there); Academic Writing's Advanced tier applies them within each discipline's conventions and refers to Criticality, with no capability of its own for the critical edge.
6. **Templates:** settled (D-ing-0018 (a), Abbott, 23:16): the discourse map (the guide's own), the article reading map and the judgement frame (C4) stay here as proposals, not in COMPOSE's catalogue, and are offered to COMPOSE through META's ing when this document reaches `checked`. Added (D-ing-0026, Abbott, 3 October 2026, 00:21): an argument analysis, for breaking down other people's arguments, and an argument plan, for formulating one's own; both belong here and Academic Writing cross-references them where it treats formulating arguments.
7. **Source map:** what *Excelling at University* teaches for each capability belongs in its guide map (held by `path`, draft), not here.
8. **Progression by level (A11):** drafted 02:36 (J-ing-0001; META D-0205; shape D-ing-0035, D-ing-0036). Every level was read by summary only (W-0031 to W-0034); the entries are editorial readings of the descriptors and the pathway's theory.
9. **Vocabulary (D-ing-0050, Abbott, 11:10):** swept. The guide's glossary terms for this pathway are in B2a (and A4 where new); candidates from the model's tier text are in B2b; A10's direct terms are the term list v1.0 patterns as words, with the ruled second version's changes noted. The search patterns themselves are kept with each consuming project, not here. No published glossary of this pathway's vocabulary has yet been read; B2b stays candidates.

---

## Change notes
- 0.1.13: 4 October 2026, 10:37: A4 gains 7 definitions for terms named in B2a or B4 without one, found by compiling the terminology database (D-ing-0057; ing N-0119).
- 0.1.12: 4 October 2026, 10:03: A10 cards corrected (D-ing-0056): verbs matched to each statement, theory filled from the ruled A9 theory, cards with no process marked as needing one or as not a process (ing N-0113).
- 0.1.11: 3 October 2026, 11:10: vocabulary sweep: 1 glossary terms added to B2a (1 new concepts in A4), 2 candidates to B2b, A10 source note, Part E item 9 (D-ing-0050; ing N-0100).
- 0.1.10: 3 October 2026, 05:52: META runs linked: FHEQ and CQFW linked to META's standards runs; W-0031 and W-0032 received; Brookfield's critical lenses linked as related (J-ing-0002; ing N-0089).
- 0.1.9: 3 October 2026, 04:41: file renamed to `ingest-path-criticality.md`; the id is unchanged (ing N-0083).
- 0.1.8: 3 October 2026, 02:49: A11: each level gains a metacognitive statement and stance, compliance to flow (D-ing-0038, D-ing-0039; ing N-0081).
- 0.1.7: 3 October 2026, 02:36: A11 progression by level, levels 3 to 8, with own-development understandings; level descriptors by summary; W-0031 to W-0034; Part E item 8 (J-ing-0001; META D-0205; D-ing-0035; D-ing-0036; ing N-0078).
- 0.1.6: 3 October 2026, 00:21: argument analysis and argument plan templates added, cross-referenced from Academic Writing (D-ing-0026; ing N-0058; G-ing-0084).
- 0.1.5: 2 October 2026, 23:51: Barnett (run 0035) and the Delphi report (run 0036) linked in A9 and every capability; W-0019 and W-0020 received (ing N-0052; G-ing-0070).
- 0.1.4: 2 October 2026, 23:38: Part E item 5 settled: this pathway teaches the critical edge, Academic Writing applies it (D-ing-0020 (a); ing N-0050; G-ing-0061).
- 0.1.3: 2 October 2026, 23:16: Part E item 6 settled, templates offered at `checked` (D-ing-0018 (a); ing N-0045; G-ing-0052).
- 0.1.2: 2 October 2026, 23:14: key theory Barnett and the Delphi report linked in A9; Part E item 4 settled (D-ing-0017 (a); ing N-0044; G-ing-0049).
- 0.1.1: 2 October 2026, 23:10: capabilities c1 (Introductory) and c2 (Advanced) added; Part E item 3 settled (D-ing-0016 (a); ing N-0043; G-ing-0046).
- 0.1.0: 2 October 2026, 23:02: researched by INGEST research prompt 0.1.10-draft with META's pathway block 0.1.1-draft; generic core from the start (ing N-0041; G-ing-0043).
