---
id: ing:doc:pathway-ai-technology
title: AI and Technology (academic skills pathway)
aliases: [AI literacy, generative AI in study, GenAI, digital literacy, critical AI literacy, path:ai-technology]
subjectKind: framework
practices: [education]
primaryPractice: education
streams: [education/academic-skills]
extensions: [education]
parts:
  A: "partial: an authored pathway (the guide teaches no chapter on it); the capabilities are proposed, not yet confirmed; no Introductory card and one card unplaced; key theory proposed, not ruled"
  B: "partial: concepts and terms named by the model; associated vocabulary held as candidates"
  C: "full (recommended): the model sets a five-stage critical-use workflow, after institutional guidance"
pins: { structure: 0.11.0-draft, template: 0.10.0-draft, pathwayTemplate: 0.3.0-draft, theory: 0.3.0-draft, terminology: 0.3.0-draft, process: 0.3.0-draft }
status: drafted
researchedBy: INGEST research prompt 0.1.10-draft, with the pathway block of META's `mta-nts-td-pathway-ingest.md` 0.1.1-draft (sections 2 and 2a) and META's pathway template 0.3.0-draft (A11)
passes:
  P1: 4 October 2026
  P2: not run; triggers 4 and 5 hold (Part E, item 1)
  P3: open
version: 0.1.0
---

<!-- from INGEST wpk-0016-ingest-pd-ingestion-document-template.md 0.10.0-draft; the specification is wpk-0016-ingest-pd-ingestion-document-structure.md -->

# AI and Technology (academic skills pathway)

> **The core document.** Generic: it names no project that uses the pathway. Who made the model and where each claim comes from is in Part D. Companions, never ingested with it: **source maps**, one per guide (`source-maps/excelling-at-university/ingest-path-ai-technology-eau.md`), **integrations**, one per consuming project (`integrations/<project>/`), and the card integration (`integrations/cards/`, D-ing-0055). A capability's level is `unknown` until a source sets it (D-ing-0001 (a)). This is the fastest-moving pathway: tools, policy and sector guidance change quickly, and every claim here is dated to its source. Fill note from the template kept until P3.

## Part 0 Summary

### 0.1 Agent definition
<!-- brief: Two or three sentences for an agent: what this is and when to reach for it, and one thing it is not for. Write last, from the finished document. -->
<!-- label: editorial; status: drafted; basis: secondary -->
AI and Technology is one of thirteen academic skills pathways: AI literacy for study, from understanding what generative AI is and cannot be trusted to do (how it works at a high level, its limits, the first rule of checking assessment guidance, never citing its output), through using it critically and selectively on study tasks (a five-stage critical-use workflow, evaluating output, weighing costs, informed restraint), to evaluating and acting ethically around it (integrity in full, permitted support against unfair advantage, wider harms, AI in professional life). Reach for it to place, sequence or assess a capability in the use of AI or digital tools in study. It is not about academic integrity in general (Referencing) or about evaluating sources in general (Finding and Using Sources), which it extends.

### 0.2 Summary
<!-- brief: One paragraph: who proposed it, when, what it is, its main use and its main dispute. Write last. -->
<!-- label: both; status: drafted; basis: secondary -->
The academic skills pathways model (2026) sets AI and Technology as one of thirteen pathways, authored from institutional and sector sources rather than drawn from the study skills guide, which uses generative AI only as the topic of a worked essay example. Its spine is AI literacy, defined as the ability to understand, use, critically evaluate and act responsibly with AI, measured by how well the learner decides rather than how fluently they operate a tool: informed restraint is a valid outcome. It climbs in three tiers after the UNESCO framework's understand, apply and create: understand AI and its limits; use it critically and selectively through a five-stage workflow; evaluate, create with and act ethically around it. Academic integrity threads through all three tiers. The model asks for subject expert sign-off before authoring and expects local policy to replace the institutional examples. Its open questions are an Introductory tier with no capability, a card that describes the pathway's design rather than a skill, and which framework to make key (Part E).

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
modelType: framework
audience: both
```
- Three tiers, Introductory, Intermediate and Advanced, each with a focus, content and a goal (D:PTM, Pathway 12).
- An authored pathway: the guide does not teach the topic, so content is authored from institutional and sector sources, recorded for sign-off; the mapping needs subject expert approval before authoring (D:PTM, Pathway 12).
- The tiering backbone is understand, apply, create, after UNESCO's framework and Ng and others' AI literacy model; ethics and integrity are cross-cutting (D:PTM, Pathway 12, sources and framing).
- The fastest-moving pathway: content is to be built to be updated (D:PTM, Pathway 12, notes).
- Tiers are anchored to experience of the practice, not to year of study (D:TSPEC, section 2).

### A2 Core principles
<!-- brief: One item per claim the theory rests on, each cited to the authors. Claims only, not uses or benefits. -->
<!-- label: source; status: drafted; basis: primary -->
- AI literacy is the ability to understand, use, critically evaluate and act responsibly with AI, not fluency with prompts (D:PTM, Pathway 12, framing).
- AI literacy is measured by how well one decides; informed restraint and refusal are valid outcomes (D:PTM, Pathway 12, framing).
- Academic integrity is not a final-tier addition; it threads through every tier, as ethics is cross-cutting in UNESCO's framework (D:PTM, Pathway 12, framing; D:UNESCO, by summary).
- Generative AI has significant limits, inaccuracy, fabrication, bias, privacy and data risks and non-reproducibility, and is not a solution to everything (D:PTM, Pathway 12, Introductory).
- The first rule is to check the module and assessment guidance and ask the tutor if unsure; generative AI output is never cited as a source (D:PTM, Pathway 12, Introductory, after D:SHEFFIELD).
- Used well, AI is a critical friend that augments one's own thinking rather than replacing it, through a five-stage workflow ending in disclosure (D:PTM, Pathway 12, Intermediate, after D:SHEFFIELD).
- Over-reliance can erode one's own voice, creativity and language development (D:PTM, Pathway 12, Intermediate).
- Whether AI is the right tool is weighed per task, including its environmental cost (D:PTM, Pathway 12, Intermediate).
- Universities are to support students to become AI-literate and to uphold rigour and integrity (D:RUSSELL, read direct on the announcement page).

### A3 Structure
<!-- brief: The spine: every component (level, dimension, stage, category) with its order, parent, the authors' definition (paraphrased, cited), our gloss, key language and an example of our own. Take most care here; other stores link to these components. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
structure: [ladder, set]
components:
  - { slug: introductory, componentType: level, order: 1, parent: none, name: "Introductory: understand AI (AI literacy foundations)", authorsDefinition: "what generative AI is and is not; how it works at a high level (large datasets, pattern generation); its limits (inaccuracy, fabrication, bias, privacy and data risks, non-reproducibility); the golden rule of checking guidance; never citing its output (D:PTM, Pathway 12)", gloss: "know what AI is, what it cannot be trusted to do, and the first rule of using it in study", keyLanguage: [generative AI, large language model, hallucination, fabrication, bias, golden rule], examples: ["checking a module handbook's AI statement before using a chatbot to plan an essay"], audience: both, beneficiaryGloss: "understand what AI tools are and where they go wrong", readingLevel: "plain English for a student entering higher education" }
  - { slug: intermediate, componentType: level, order: 2, parent: none, name: "Intermediate: use AI critically (apply it to study tasks)", authorsDefinition: "AI as a critical friend; the critical-use workflow (background thinking, initial prompting, dialogic prompting, critical analysis and fact-checking, acknowledge, describe, evidence); applied to essays and reports, revision and reading; evaluating output; weighing pros and cons including environmental cost; informed restraint (D:PTM, Pathway 12)", gloss: "use AI on your own thinking, check everything it gives you, and know when not to use it", keyLanguage: [critical friend, critical-use workflow, prompting, fact-checking, disclosure, informed restraint], examples: ["asking a chatbot for counter-arguments to one's own plan, then checking each against sources"], audience: both, beneficiaryGloss: "use AI carefully and selectively, and check what it produces", readingLevel: "plain English for a student entering higher education" }
  - { slug: advanced, componentType: level, order: 3, parent: none, name: "Advanced: evaluate, create with, and act ethically around AI", authorsDefinition: "deep AI literacy: evaluating AI systems and outputs against academic standards; bias, equity of access, environmental impact, a human-centred mindset; integrity in full (five misconduct risks, disclosure, permitted support against unfair advantage); responsible use in complex creative and research work; AI and graduate identity (D:PTM, Pathway 12)", gloss: "judge AI against academic standards and use it to a professional, ethical standard", keyLanguage: [misconduct risks, unfair advantage, disclosure, equity of access, human-centred, responsible use], examples: ["writing a methods note that discloses and justifies AI use in a research project"], audience: both, beneficiaryGloss: "use AI responsibly at a professional standard", readingLevel: "plain English for a student entering higher education" }
  - { slug: ai-technology-01, componentType: element, order: 2.1, parent: intermediate, name: "Exercise AI literacy through informed, justified decisions about when, and when not, to use AI", authorsDefinition: "proposed capability, tier note developed (D:CARDS)", gloss: "decide well whether to use AI at all", keyLanguage: [AI literacy, informed restraint, decision], examples: [], audience: both, beneficiaryGloss: "decide when AI helps and when it does not", readingLevel: "plain English for a student entering higher education" }
  - { slug: ai-technology-03, componentType: element, order: 2.2, parent: intermediate, name: "Apply a critical-use workflow treating AI as a critical friend, not a replacement for independent thought", authorsDefinition: "proposed capability, tier note developed (D:CARDS)", gloss: "work with AI in stages, keeping your own thinking first", keyLanguage: [critical-use workflow, critical friend, independent thought], examples: [], audience: both, beneficiaryGloss: "use AI step by step without letting it think for you", readingLevel: "plain English for a student entering higher education" }
  - { slug: ai-technology-05, componentType: element, order: 2.3, parent: intermediate, name: "Weigh the costs of AI/technology use, including environmental and professional impact, against its benefits", authorsDefinition: "proposed capability, tier note developed (D:CARDS)", gloss: "weigh what AI costs against what it gives", keyLanguage: [costs, benefits, environmental impact, professional impact], examples: [], audience: both, beneficiaryGloss: "think about the downsides of AI as well as the upsides", readingLevel: "plain English for a student entering higher education" }
  - { slug: ai-technology-02, componentType: element, order: 3.1, parent: advanced, name: "Avoid GenAI misconduct risks and never cite GenAI outputs as a source", authorsDefinition: "proposed capability, tier note extended; the never-cite rule is first stated at Introductory (D:CARDS)", gloss: "stay clear of the ways AI use becomes misconduct", keyLanguage: [misconduct risks, plagiarism, fabrication, collusion, never cite], examples: [], audience: both, beneficiaryGloss: "avoid using AI in ways that break the rules", readingLevel: "plain English for a student entering higher education" }
  - { slug: ai-technology-06, componentType: element, order: 3.2, parent: advanced, name: "Distinguish permitted technological support from an unfair academic advantage", authorsDefinition: "proposed capability, tier note extended (D:CARDS)", gloss: "tell allowed help from unfair advantage", keyLanguage: [permitted support, unfair advantage], examples: [], audience: both, beneficiaryGloss: "know which help is allowed and which is not", readingLevel: "plain English for a student entering higher education" }
  - { slug: ai-technology-04, componentType: element, order: 9.1, parent: none, name: "Progress through tiers of digital/AI capability while treating ethics as cross-cutting", authorsDefinition: "proposed capability, unplaced: it describes the pathway's cross-tier design, not a skill at one tier (D:CARDS, tier notes)", gloss: "the pathway's own design: ethics in every tier", keyLanguage: [cross-cutting ethics, progression], examples: [], audience: practitioner, beneficiaryGloss: "ethics comes up at every stage", readingLevel: "plain English for a student entering higher education" }
```
No card sits at Introductory, which holds understanding AI and its limits and the first rule; `/04` describes the pathway's design (Part E, item 3).

### A4 Concepts used
<!-- brief: The ideas the theory rests on that other theories share; each will become or match a TERMINOLOGY-DAT concept. -->
<!-- label: both; status: drafted; basis: primary -->
- ai-literacy: the ability to understand, use, critically evaluate and act responsibly with AI (D:PTM, Pathway 12; after D:UNESCO and D:NG).
- generative-ai: AI tools that generate text, images or other content from patterns in large datasets (D:PTM, Pathway 12, Introductory).
- fabrication: AI output that presents invented content, such as references, as fact; also called hallucination (D:PTM, Pathway 12).
- critical-friend: the stance of using AI to question and augment one's own thinking (D:PTM, Pathway 12, after D:SHEFFIELD).
- critical-use-workflow: five stages for using AI on a study task, ending in disclosure (D:PTM, Pathway 12, after D:SHEFFIELD).
- informed-restraint: deciding not to use AI where it does not serve the task or one's development (D:PTM, Pathway 12).
- disclosure: acknowledging, describing and evidencing how AI was used (D:PTM, Pathway 12, after D:SHEFFIELD).
- misconduct-risk: a way AI use becomes academic misconduct: plagiarism, buying or commissioning, coursework sites, fabrication, collusion (D:PTM, Pathway 12, after D:SHEFFIELD).
- academic-integrity: honest, responsible conduct in academic work (shared with `path:referencing`).
- human-centred-mindset: keeping agency, judgement and responsibility with the person using AI (D:UNESCO, by summary).

### A5a How practitioners apply it
<!-- brief: From the practitioner's side: the steps they take, the tools and artefacts they use, a worked example, and the decisions they make along the way. Separate what the authors prescribe (source) from how it is done in practice (reported, with sources) and what follows from it (editorial). -->
<!-- label: both; status: drafted; basis: primary -->
Practitioners here are tutors, academic skills staff, librarians and authors of learning material.

**What the authors prescribe** (source):
- Teach the critical-use workflow on real study tasks: essays and reports, revision and reading (D:PTM, Pathway 12, Intermediate).
- Thread integrity through every tier rather than leaving it to the end (D:PTM, Pathway 12, framing).
- Replace institutional examples with local policy, approved tools and disclosure process, supplied by a subject expert (D:PTM, Pathway 12, sources and notes).
- Coordinate with the referencing and integrity pathway so the two reinforce rather than repeat (D:PTM, Pathway 12, notes).

**How it is done in practice** (reported):
- Universities publish AI guidance hubs with integrity rules and critical-use advice (D:SHEFFIELD, via D:PTM; evidence: reported).
- Sector principles commit universities to AI literacy and to adapting teaching and assessment for ethical use (D:RUSSELL; evidence: reported).

**Worked example**:
At Introductory, the learner checks the assessment's AI rules, asks a tool a factual question and finds a fabricated reference in the answer. At Intermediate, they plan an essay themselves, use AI for counter-arguments, fact-check each against sources and disclose the use. At Advanced, they judge whether AI use in a project gives an unfair advantage, weigh its costs and write a justified disclosure (editorial).

### A5b How beneficiaries meet it
<!-- brief: From the beneficiary's side (learner, client, project team, stakeholder): what it asks of them, what they see or do, and any version made for them to use directly. Search for this separately. -->
<!-- label: both; status: drafted; basis: primary -->
- Many students are considering how to use generative AI in their studies, which raises the stakes of referencing and integrity (D:EAU, p. 6; evidence: claimed).
- Concern in universities centres on students using generative AI to cheat (D:EAU, pp. 145-146, an example essay; evidence: claimed).
- unknown: no source here reports students' own experience of AI literacy teaching.

### A5c Contexts and adaptations
<!-- brief: Where it is used (levels, sectors, practices, settings, modes such as online), and how it has been adapted for them, each with its source. -->
<!-- label: both; status: drafted; basis: secondary -->
- Any discipline; policy varies by institution, module and assessment (D:PTM, Pathway 12).
- Schools to higher education: UNESCO's framework for students sets four dimensions (a human-centred mindset, ethics of AI, AI techniques and applications, AI system design) across three levels (understand, apply, create) (D:UNESCO, by summary).
- AI literacy research: Ng and others (2021) propose four aspects, know and understand, use and apply, evaluate and create, and ethical issues (D:NG, by catalogue record and the model's summary); Long and Magerko (2020) set out competencies and design considerations for AI literacy (D:LONG, by summary).
- Digital capability more widely: Jisc's framework of individual digital capabilities (D:JISC, by catalogue record).

### A5d Misapplications
<!-- brief: Common ways it is misused or misread, the evidence for each, and how to avoid it. -->
<!-- label: both; status: drafted; basis: primary -->
- Pasting in the essay title without one's own thinking first (D:PTM, Pathway 12; evidence: claimed); start with background thinking.
- Copying and pasting output into assessed work (D:PTM, Pathway 12; evidence: claimed); use output only to inform one's own work.
- Citing AI output as a source (D:PTM, Pathway 12; evidence: claimed); find and cite the underlying source.
- Treating AI literacy as prompt fluency (D:PTM, Pathway 12, framing; evidence: claimed).

### A6a Benefits to practitioners
<!-- brief: What those who apply it gain. Mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
- A shared workflow and vocabulary for discussing AI use with students (editorial).

### A6b Benefits to beneficiaries
<!-- brief: Name the beneficiaries, then what reaches them and how it reaches them through the practitioner. Search for this separately; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students; later, employers.
- Safer, more effective use of AI in study, with integrity kept (D:PTM, Pathway 12; evidence: claimed).
- A discerning, responsible stance towards AI carried into professional life (D:PTM, Pathway 12, Advanced, after D:RUSSELL; evidence: claimed).

### A7a Criticisms of the theory and its application
<!-- brief: Criticisms of the theory itself and of how practitioners apply it, with the evidence for each, marked measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: secondary -->
- none-stated: no published criticism of this pathway exists.
- (editorial) The workflow and disclosure model are one university's; other institutions' rules differ, and the model expects them replaced locally (D:PTM, Pathway 12, notes).
- (editorial) The field changes faster than any pathway can be revised; claims about tools and policy date quickly.
- (editorial) The guide's only extended treatment of AI is an example essay arguing a position on AI in higher education (pp. 145-148); it is an example of argument, not teaching about AI.

### A7b Effects on beneficiaries
<!-- brief: Name the beneficiaries, then the harms, costs or limits that reach them through the practitioner's use. Search for this separately, as for A6b; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students.
- unknown: no evidence yet of how learners fare in the pathway.
- (editorial) Unequal access to paid tools may advantage some students; equity of access is named at Advanced but not resolved.

### A8 Selection
<!-- brief: When to choose it over named alternatives, and what it suits badly. Our reading (editorial). -->
<!-- label: editorial; status: drafted; basis: secondary -->
Choose this pathway when the aim is deciding on, using or judging AI and digital tools in study. For integrity and plagiarism in general, choose `path:referencing`; for evaluating sources in general, `path:finding-using-sources`; for critical thinking in general, `path:criticality`. It suits badly a need for training in a particular tool.

### A9 Relations
<!-- brief: Other theories it revises, extends, derives from, contrasts with or competes with, each with a target id and a one-line note. -->
<!-- label: both; status: drafted; basis: primary -->
The model names its sources; none is ingested at META. No key theory is ruled (Part E, item 4).
```yaml
- { rel: derivedFrom, target: unknown, note: "the tiering backbone, proposed lead: UNESCO (2024) AI Competency Framework for Students (Miao and Shiohira): four dimensions across understand, apply and create; read by summary; W-0087" }
- { rel: derivedFrom, target: unknown, note: "the definition: Ng, Leung, Chu and Qiao (2021), Conceptualizing AI literacy: an exploratory review, Computers and Education: Artificial Intelligence 2; know and understand, use and apply, evaluate and create, ethics; from catalogue records; W-0088" }
- { rel: related, target: unknown, note: "Long and Magerko (2020), What is AI literacy? Competencies and design considerations, CHI 2020; read by summary; W-0089" }
- { rel: derivedFrom, target: unknown, note: "the workflow and integrity rules: University of Sheffield, Using Generative AI guidance (the five misconduct risks, the golden rule, never cite, the critical-use workflow, acknowledge, describe, evidence); named by the model, not read here; W-0090" }
- { rel: related, target: unknown, note: "sector principles: Russell Group (2023) Principles on the use of generative AI tools in education, five principles; read direct on the announcement page; W-0091" }
- { rel: related, target: unknown, note: "digital capability: Jisc, the digital capabilities framework, individual digital capabilities; from catalogue records; W-0092" }
- { rel: related, target: ing:doc:subject-benchmark-statements-qaa-2022, note: "generative AI becomes a cross-cutting theme of the benchmark statements from the 2026 editions; META INGEST run, SHA-256 prefix fb603834406f, read there" }
- { rel: extends, target: ing:doc:pathway-referencing, note: "the AI-specific extension of integrity, values and plagiarism; cross-reference, not duplicate (model, cross-links)" }
- { rel: related, target: ing:doc:pathway-criticality, note: "evaluating AI output is applied criticality (model, cross-links)" }
- { rel: related, target: ing:doc:pathway-finding-using-sources, note: "using AI to find information, and why its output is not a citable source (model, cross-links)" }
- { rel: related, target: ing:doc:pathway-academic-writing, note: "essays and reports: AI for scoping, planning and proofreading (model, cross-links)" }
- { rel: related, target: ing:doc:pathway-revising-exams, note: "AI as a self-testing aid, not a replacement for retrieval practice (model, cross-links)" }
```

### A10 Extension fields
<!-- brief: The practice extension fields for each practice in the front matter, and no others. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
education:
  domain: "cognitive and ethical (D:PTM, Pathway 12)"
  verbs: [exercise, decide, apply, weigh, avoid, distinguish]
  learnerLevel: "higher education, any year; tiers anchored to experience of the practice (D:TSPEC, section 2)"
pathway:
  id: path:ai-technology
  title: AI and Technology
  definition: "AI literacy for study: understanding what generative AI is and cannot be trusted to do, using it critically and selectively through a staged workflow that keeps one's own thinking first, evaluating its output, deciding when not to use it, and acting with integrity: disclosing use, avoiding misconduct and telling permitted support from unfair advantage."
  terms:
    direct: [artificial intelligence, AI, GenAI, generative AI, technology, digital skills, digital literacy, digital tools]
    associated: [AI literacy, critical AI literacy, large language model, chatbot, prompt, prompting, hallucination, fabrication, bias, critical friend, critical-use workflow, fact-checking, disclosure, acknowledgement, informed restraint, misconduct, unfair advantage, environmental impact, human-centred, data privacy]
    source: "direct: the pathway term list v1.0 (D:TERMS; its 8 patterns written as words); associated: candidates from D:PTM and the sector sources (B2b) (D-ing-0050)"
  competencies:
    - id: ai-technology/01
      tierNote: developed
      statement: Exercise AI literacy through informed, justified decisions about when, and when not, to use AI.
      level: unknown
      verbs: [exercise, decide, use]
      theory: [{unknown: "UNESCO (2024), not yet ingested; W-0087"}, {unknown: "Ng and others (2021), not yet ingested; W-0088"}]
      process: [critical-use-workflow]
      professional:
        - statement: Decides whether and how to use AI tools in work, within the organisation's policy, and can justify the decision.
          equivalence: close
          gap: "workplace policy and liability set the limits; academic ones the assessment rules"
          frameworks: ["Jisc digital capabilities: digital learning and development"]
    - id: ai-technology/03
      tierNote: developed
      statement: Apply a critical-use workflow treating AI as a critical friend, not a replacement for independent thought.
      level: unknown
      verbs: [apply, treat]
      theory: [{unknown: "University of Sheffield guidance, not yet ingested; W-0090"}]
      process: [critical-use-workflow]
      professional:
        - statement: Uses AI to draft, question and check work while keeping professional judgement and verifying output.
          equivalence: close
          gap: "professional output carries organisational accountability; academic output is assessed as the student's own"
          frameworks: []
    - id: ai-technology/05
      tierNote: developed
      statement: Weigh the costs of AI/technology use, including environmental and professional impact, against its benefits.
      level: unknown
      verbs: [weigh]
      theory: [{unknown: "UNESCO (2024), not yet ingested; W-0087"}]
      process: [critical-use-workflow]
      professional:
        - statement: Assesses the costs, risks and sustainability of adopting a technology against its benefits.
          equivalence: partial
          gap: "organisations weigh adoption at scale; a student weighs one task"
          frameworks: []
    - id: ai-technology/02
      tierNote: extended
      statement: Avoid GenAI misconduct risks and never cite GenAI outputs as a source.
      level: unknown
      verbs: [avoid, cite]
      theory: [{unknown: "University of Sheffield guidance, not yet ingested; W-0090"}]
      process: [critical-use-workflow]
      professional:
        - statement: Uses AI within professional and legal rules on authorship, confidentiality and attribution.
          equivalence: partial
          gap: "professional rules concern liability and confidentiality; academic ones authorship and assessment"
          frameworks: []
    - id: ai-technology/06
      tierNote: extended
      statement: Distinguish permitted technological support from an unfair academic advantage.
      level: unknown
      verbs: [distinguish]
      theory: [{unknown: "Russell Group (2023), not yet ingested; W-0091"}]
      process: [{none: "an understanding, applied at the critical-use workflow's disclosure stage"}]
      professional:
        - statement: Judges whether a tool or aid is fair and permitted in a regulated assessment or practice.
          equivalence: partial
          gap: "professional fairness concerns clients and regulators; academic fairness other students"
          frameworks: []
    - id: ai-technology/04
      tierNote: unknown   # unplaced: describes the pathway's design, not a skill at one tier (tier notes)
      statement: Progress through tiers of digital/AI capability while treating ethics as cross-cutting.
      level: unknown
      verbs: [progress, treat]
      theory: [{unknown: "UNESCO (2024), not yet ingested; W-0087"}]
      process: [{none: "a design note for the pathway, not a capability (Part E, item 3)"}]
      professional: []
  external:
    - { framework: "UNESCO AI Competency Framework for Students (2024)", match: ["human-centred mindset", "ethics of AI", "AI techniques and applications"], equivalence: broader }
    - { framework: "Jisc digital capabilities framework", match: ["information, data and media literacies", "digital learning and development"], equivalence: broader }
  processes: [critical-use-workflow]
  templates: ["AI use decision checklist (proposed)", "AI use disclosure statement (proposed)", "AI output fact-check log (proposed)"]
```
`equivalence` says how the professional form relates to the capability (META D-0175's scale), and in `external` how the framework relates to the pathway. Every item here is editorial. UNESCO and Jisc were read by summary or catalogue record only (Part E, item 1).

### A11 Progression by level
<!-- brief: How the practice develops across qualification levels 3 to 8, deconstructed at each level into skills, competencies, understandings and literacies (after Lea and Street); level 8 in full; each entry says what changes from the level below; grounded in level descriptors and the key theory. From META's pathway template 0.3.0-draft. -->
<!-- label: both; status: drafted; basis: secondary -->
Each level also carries a metacognitive statement (D-ing-0038, D-ing-0039) on the ladder from compliance, through purpose, investment and ownership, to adaptation and flow. The practice described is using and judging AI in study and practice, never the pathway's tiers. Each level's understandings end with what the practice means for the learner's own development (D-ing-0036). The descriptors were read by summary only (Part E, item 9). No key theory is ruled (Part E, item 4).
```yaml
progression:
  levelFramework: "qualification levels 3 to 8: CQFW and RQF numbering; FHEQ levels 4 to 8"
  levels:
    - level: 3
      context: "a learner entering higher education: level 3 study, access and foundation years"
      skills: ["use an AI tool for a simple, permitted task", "notice when an answer looks wrong", "follow a stated rule on AI use"]
      competencies: ["uses AI tools within stated rules with guidance"]
      understandings: ["AI tools can be wrong", "for own development: one's own work must stay one's own"]
      literacies: ["a chatbot exchange; a stated rule"]
      metacognition: { stance: compliance, statement: "Uses or avoids AI because the rules say so; follows instructions on it." }
      changesFromBelow: not-applicable-by-design
      sources: [CQFW, PTM]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 4
      context: "the first year of higher education"
      skills: ["explain how generative AI produces text and why it fabricates", "check the assessment's AI guidance", "never cite AI output"]
      competencies: ["understands AI's limits and the first rules of using it in study"]
      understandings: ["AI is pattern generation, not knowledge", "for own development: AI literacy is judgement, not fluency"]
      literacies: ["module AI statements; a fabricated reference spotted"]
      metacognition: { stance: purpose, statement: "Knows why AI rules exist and what AI cannot do; uses it cautiously when allowed." }
      changesFromBelow: "from following a rule to understanding why it exists"
      sources: [FHEQ, PTM, UNESCO]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 5
      context: "developing practice, depending on the student: the second year"
      skills: ["run the critical-use workflow on a study task", "fact-check output and detect bias", "disclose use", "decide not to use AI where it does not serve the task"]
      competencies: ["uses AI critically and selectively and discloses it"]
      understandings: ["AI augments thinking only when one's own thinking comes first", "for own development: over-reliance erodes one's voice"]
      literacies: ["a disclosure statement; a fact-check log"]
      metacognition: { stance: investment, statement: "Invests in using AI well: develops their own critical workflow and chooses when to refrain." }
      changesFromBelow: "from understanding limits to using AI critically on real tasks"
      sources: [FHEQ, PTM, NG]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 6
      context: "independent practice: the final undergraduate year"
      skills: ["evaluate AI output against academic standards", "distinguish permitted support from unfair advantage", "weigh costs including environmental impact"]
      competencies: ["evaluates and uses AI to an ethical, academic standard"]
      understandings: ["integrity in AI use is a matter of judgement as well as rules", "for own development: being a discerning AI user is part of graduate identity"]
      literacies: ["a justified AI use in a dissertation; an evaluation of a tool"]
      metacognition: { stance: ownership, statement: "Owns their AI practice: judges, discloses and defends their use with confidence." }
      changesFromBelow: "from using critically to evaluating and acting ethically"
      sources: [FHEQ, PTM, UNESCO]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 7
      context: "advanced practice: master's study, professional development"
      skills: ["use AI responsibly in research and professional work", "assess a tool's fitness, bias and risk for a context", "advise others on AI use"]
      competencies: ["integrates AI into specialist practice responsibly and advises others"]
      understandings: ["AI shapes the practices of the field and its ethics", "for own development: one's AI practice is adapted to each professional purpose"]
      literacies: ["AI use statements in research; tool evaluations; guidance for colleagues"]
      metacognition: { stance: adaptation, statement: "Adapts AI use to personal and professional aims; coaches others in responsible use." }
      changesFromBelow: "from ethical use in study to responsible use and advice in professional and research settings"
      sources: [FHEQ, QAAMSC, VITAE, UNESCO]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 8
      context: "doctoral practice: an original contribution to knowledge, the researcher's identity and independence"
      skills: ["design and justify AI use in original research", "contribute to the field's norms on AI", "examine others' AI use"]
      competencies: ["shapes responsible AI practice in the research community"]
      understandings: ["a field's norms on AI are made by its researchers", "for own development: the researcher stands responsible for every tool they use"]
      literacies: ["methodological statements on AI; contributions to guidance"]
      metacognition: { stance: flow, statement: "Responsible AI use is fluent and tacit, a mode of doing and expression in the flow, in the service of their disciplinary community." }
      changesFromBelow: "a different kind, not more of level 7: from using AI responsibly to setting the field's norms for it"
      sources: [QAADOC, VITAE, FHEQ]
      provenance: { label: both, status: drafted, basis: secondary }
```

## Part B Terminology

### B1 Concepts
<!-- brief: One concept per idea that has a name in this theory (each A3 component, each A4 concept): plain definition, scope note, category, practices. -->
<!-- label: both; status: drafted; basis: primary -->
By rule: one concept per A3 tier and per A4 concept, definition as A3's gloss or A4's line. The exceptions:
```yaml
- slug: golden-rule
  definition: "always check the module and assessment guidance on AI, and ask the tutor if unsure"
  beneficiaryDefinition: "check the rules before you use AI"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "the model's first rule, after institutional guidance (D:PTM, Pathway 12)"
  category: rule
  practices: [education]
- slug: acknowledge-describe-evidence
  definition: "the disclosure stage: acknowledge that AI was used, describe how, and evidence it"
  beneficiaryDefinition: "say that you used AI, how, and show it"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "the workflow's fifth stage, after institutional guidance (D:PTM, Pathway 12)"
  category: technique
  practices: [education]
```

### B2a Terms named by the authors
<!-- brief: Every name the authors give a concept: preferred and admitted forms, their alternative names and spelling variants, in full (no compact rule); part of speech, register, extension fields. -->
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: ai-literacy, form: AI literacy, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: generative-ai, form: generative AI, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: generative-ai, form: GenAI, lang: en, partOfSpeech: abbreviation, termStatus: admitted, register: general }
- { concept: fabrication, form: fabrication, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: fabrication, form: hallucination, lang: en, partOfSpeech: noun, termStatus: admitted, register: general }
- { concept: critical-friend, form: critical friend, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: critical-use-workflow, form: critical-use workflow, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: informed-restraint, form: informed restraint, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: disclosure, form: disclosure, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: misconduct-risk, form: misconduct risks, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: golden-rule, form: golden rule, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: human-centred-mindset, form: human-centred mindset, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```
Glossary terms placed in this pathway (D:EAU, glossary, pp. x-xiii; D-ing-0050): none; the guide's glossary has no AI terms. The model's terms are the source here.
`usableIn` and `bannedIn`: none-stated.

### B2b Associated vocabulary
<!-- brief: The wider vocabulary practitioners reach for (for Bloom, the verb lists), from at least two named secondary sources, with a scholarly analysis of such lists where one exists. Where none exists, list the words as candidates and put the glossary wanted in D3. One membership per component a word is placed in, with its sources and agreement weight; record where sources disagree with the authors. Never store similarity between words: it is computed from embeddings at query time. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
- { concept: large-language-model, form: large language model, frameworkBlocks: [{ component: introductory, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: prompting, form: prompting, frameworkBlocks: [{ component: intermediate, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: dialogic-prompting, form: dialogic prompting, frameworkBlocks: [{ component: intermediate, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: fact-checking, form: fact-checking, frameworkBlocks: [{ component: intermediate, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: ai-speak, form: AI speak, frameworkBlocks: [{ component: intermediate, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: unfair-advantage, form: unfair advantage, frameworkBlocks: [{ component: advanced, sources: [PTM, CARDS], weight: 2/2 }], status: candidate }
- { concept: equity-of-access, form: equity of access, frameworkBlocks: [{ component: advanced, sources: [PTM, RUSSELL], weight: 2/2 }], status: candidate }
- { concept: digital-capability, form: digital capability, frameworkBlocks: [{ component: introductory, sources: [JISC], weight: 1/1 }], status: candidate }
- { concept: critical-ai-literacy, form: critical AI literacy, frameworkBlocks: [{ component: advanced, sources: [PTM], weight: 1/1 }], status: candidate }
```
No glossary of AI literacy vocabulary was consulted; one is wanted (D3).

### B3 Framework blocks
<!-- brief: For each concept this theory defines its own way: the A3 component, this theory's definition (cited) and its use here. -->
<!-- label: source; status: drafted; basis: primary -->
By rule: each tier concept's framework block is its A3 component and definition. The exceptions:
```yaml
- { concept: ai-literacy, component: intermediate, definitionHere: "measured by how well one decides, not how fluently one operates a tool (D:PTM, Pathway 12, framing)", useHere: "the spine of every tier; informed restraint counts as literacy" }
```

### B4 Relations
<!-- brief: Broader, narrower, related, contrasts-with and the order within this theory, between the B1 concepts. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: higher-level-than, from: intermediate, to: introductory, note: "tier order" }
- { rel: higher-level-than, from: advanced, to: intermediate, note: "tier order" }
- { rel: narrower, from: fabrication, to: misconduct-risk, note: "one of the five risks (D:PTM, Pathway 12)" }
- { rel: part-of, from: acknowledge-describe-evidence, to: critical-use-workflow, note: "the fifth stage" }
- { rel: related, from: informed-restraint, to: ai-literacy, note: "a valid literacy outcome (D:PTM, Pathway 12)" }
- { rel: related, from: misconduct-risk, to: academic-integrity, note: "shared with path:referencing" }
```

### B5 Rules
<!-- brief: Our rules on using the terms (such as a verb banned in outcomes), each with its reason. Editorial. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- understand, know, appreciate, be aware of: not used in learning outcomes at any tier, because they name no observable operation (D:TSPEC, section 6).
- Institution-specific rules (approved tools, disclosure process) are not stated as general facts; they belong to each institution's own context (D:PTM, Pathway 12, notes).

## Part C Process

### C0 Formality
<!-- brief: Decide first: prescribed, recommended, loose, implied or not applicable, with one sentence on why. If not applicable, stop Part C. -->
<!-- label: both; status: drafted; basis: primary -->
`recommended`: the model sets a five-stage critical-use workflow, after one institution's guidance, and a first rule (D:PTM, Pathway 12).

### C1 Process models
<!-- brief: Each process the theory lends itself to: what it achieves, shape, scale, what starts it and what counts as done. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: critical-use-workflow
  summary: use AI on a study task critically, keeping one's own thinking first, and disclose the use
  shape: linear
  scale: [task]
  scaleNote: "one study task; the decision whether to use AI at all comes first"
  groundedIn: [ing:doc:pathway-ai-technology]
  entry: a study task and its assessment guidance
  exit: one's own work, informed and checked, with the AI use disclosed
```

### C2 Stages
<!-- brief: Each stage in order: purpose, inputs, activities, outputs, roles, the gate that ends it. Mark our arrangement editorial where the authors give no stages, and every activity the sources do not name `inferred: true`. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { model: critical-use-workflow, order: 0, name: Check the guidance and decide, purpose: "check the assessment's AI rules and weigh whether AI is the right tool (D:PTM, Pathway 12, golden rule and weighing habit)", inputs: [], activities: [read the guidance, weigh pros and cons], outputs: [], roles: [student], endsAt: use-ai, repeat: none, audience: both }
- { model: critical-use-workflow, order: 1, name: Background thinking, purpose: "establish what one already knows and thinks first (D:PTM, Pathway 12)", inputs: [], activities: [note own ideas and plan], outputs: [], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: critical-use-workflow, order: 2, name: Initial prompting, purpose: "build a prompt with a role, a function and limitations (D:PTM, Pathway 12)", inputs: [], activities: [write the prompt], outputs: [], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: critical-use-workflow, order: 3, name: Dialogic prompting, purpose: "push for counter-arguments and depth through dialogue (D:PTM, Pathway 12)", inputs: [], activities: [question the output, ask for counter-arguments], outputs: [], roles: [student], endsAt: none, repeat: "as needed", audience: both }
- { model: critical-use-workflow, order: 4, name: Critical analysis and fact-checking, purpose: "verify everything against reliable sources, checking for fabrication and bias (D:PTM, Pathway 12)", inputs: [], activities: [check claims and references against sources], outputs: [fact-check-log], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: critical-use-workflow, order: 5, name: Acknowledge, describe, evidence, purpose: "disclose how AI was used (D:PTM, Pathway 12)", inputs: [fact-check-log], activities: [write the disclosure], outputs: [disclosure-statement], roles: [student], endsAt: none, repeat: none, audience: both }
```
Stage 0 is our arrangement of the model's golden rule and weighing habit before its five stages (editorial).

### C3 Gates
<!-- brief: Each decision point with criteria that can pass or fail, and what it decides. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: use-ai
  criteria: ["the assessment permits it", "it serves the task and one's own development", "its costs are worth its benefits"]
  decides: "use AI | do not use AI"
  variationPoint: yes
```

### C4 Outputs
<!-- brief: Each product a stage makes: purpose, parts, and what a template for it needs to know. Mark every output the sources do not name `inferred: true`. Where the method names its own document types, record every one complete (purpose, composition, derivation, quality criteria) from its product descriptions; our templates are drafted from those parts, never the method's text copied. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: fact-check-log, purpose: "a record of what was checked and against which source", parts: [claim or reference, source checked, result], producedBy: [critical-use-workflow 4], usedBy: [critical-use-workflow 5], templateHint: "the AI output fact-check log", audience: beneficiary, inferred: true }
- { slug: disclosure-statement, purpose: "acknowledge, describe and evidence AI use", parts: [acknowledgement, description of use, evidence], producedBy: [critical-use-workflow 5], usedBy: [], templateHint: "the AI use disclosure statement, to the institution's format", audience: beneficiary, inferred: false }
```

### C5 Roles
<!-- brief: Who does each stage, from both sides: practitioner roles and beneficiary roles. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: student, responsibilities: [decide, use AI critically, check, disclose], stagesInvolved: [all] }
- { slug: tutor, responsibilities: [set the AI rules for an assessment, answer questions on them], stagesInvolved: [critical-use-workflow 0] }
```

### C6 Variation points
<!-- brief: Where the process can be tailored or branch, by gate. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- The decision gate may end the workflow: not using AI is a valid outcome.
- The disclosure format follows the institution's rules (D:PTM, Pathway 12, notes).

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
- { key: PTM, author: "Abbott, S.", title: "Academic skills pathways model: pathway tier mapping, Draft v3 (v3.1)", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [0.2, A1, A2, A3, A4, A5a, A5d, A10, B1, B2b, B3, C0, C2] }
- { key: TSPEC, author: "Abbott, S.", title: "Academic skills pathways model: tier specification v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A1, A10, B5] }
- { key: CARDS, author: "Abbott, S.", title: "Academic skills pathways model: capability cards with tier notes, proposed", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A3, A10] }
- { key: TERMS, author: "Abbott, S.", title: "Academic skills pathways model: pathway term list v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A10] }
- { key: EAU, author: "Dennis, C. and Abbott, S.", title: "Excelling at University: Academic Literacies and the Development of Graduate Identity", edition: 1st, year: 2026, publisher: Routledge, licence: copyright, tier: primary, readVia: direct, held: not held, citedIn: [A5b, A7a] }
- { key: UNESCO, author: "Miao, F. and Shiohira, K. (UNESCO)", title: "AI Competency Framework for Students", year: 2024, tier: professional, readVia: summary, held: not held, citedIn: [A2, A4, A5c, A9, A11] }
- { key: RUSSELL, author: Russell Group, title: "Principles on the use of generative AI tools in education (announced 4 July 2023)", year: 2023, tier: professional, readVia: direct, held: not held, citedIn: [A2, A5a, A6b, A9, B2b] }
- { key: LONG, author: "Long, D. and Magerko, B.", title: "What is AI literacy? Competencies and design considerations", journal: "Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI 2020)", year: 2020, tier: secondary, readVia: summary, held: not held, citedIn: [A5c, A9] }
- { key: FHEQ, author: Quality Assurance Agency for Higher Education, title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies, 2nd edn (level descriptors unchanged from 2014)", year: 2024, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:qaa-fheq-2024-framework, META, SHA-256 prefix 97c52675225e" }
- { key: CQFW, author: Welsh Government, title: "Credit and Qualifications Framework for Wales: level descriptors", year: 2009, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:welsh-government-cqfw-2009-framework, META, SHA-256 prefix 682642ca28c8" }
- { key: QAAMSC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Master's Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: QAADOC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Doctoral Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: VITAE, author: Vitae, title: "Researcher Development Framework", year: 2010, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
```
Not in D1 until read: Ng and others (2021), the University of Sheffield guidance and Jisc's framework, found as catalogue records or named by the model only (D2; D3, W-0088, W-0090, W-0092). The keys NG, SHEFFIELD and JISC name those rows.

### D2 Research log
<!-- brief: Every source opened, used or not, as you open it. -->
```yaml
- { ref: PTM, tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: Pathway 12 in full, with its sources, framing, cross-links and notes" }
- { ref: TSPEC, tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: anchoring and outcome verbs" }
- { ref: CARDS, tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: six capabilities; tier notes three developed, two extended, one unplaced, none introduced" }
- { ref: TERMS, tier: primary, consulted: 2026-10-04, pass: P1, outcome: "used: 8 patterns" }
- { ref: EAU, tier: primary, consulted: 2026-10-04, pass: P1, outcome: "searched for AI: an example essay on generative AI in higher education (pp. 145-148), the referencing context (p. 6) and the integrity chapter's opening; no teaching on AI" }
- { ref: "META INGEST runs (UNI library, theory)", tier: primary, consulted: 2026-10-04, pass: P1, outcome: "none found for AI literacy or digital capability (a listing of the folder)" }
- { ref: "UNESCO (2024), via https://gcedclearinghouse.org/en/node/146445", tier: web, consulted: 2026-10-04, pass: P1, outcome: "used, by summary: authors, four dimensions, three levels" }
- { ref: "Russell Group (2023), via https://russellgroup.ac.uk/news/new-principles-on-use-of-ai-in-education/", tier: web, consulted: 2026-10-04, pass: P1, outcome: "used, read direct: the five principles and the date" }
- { ref: "Long and Magerko (2020), via https://circlcenter.org/what-is-ai-literacy-competencies-and-design-considerations/", tier: web, consulted: 2026-10-04, pass: P1, outcome: "used, by summary: citation and shape; the numbers of competencies not on the page" }
- { ref: "Ng and others (2021), via https://doaj.org/article/232df6b413cb475daaa3d8d7b664a7e6", tier: web, consulted: 2026-10-04, pass: P1, outcome: "catalogue record only; its four aspects are the model's summary" }
- { ref: "Jisc digital capabilities, via https://digitalcapability.jisc.ac.uk/what-is-digital-capability/individual-digital-capabilities/", tier: web, consulted: 2026-10-04, pass: P1, outcome: "catalogue record only; content not read" }
- { ref: "University of Sheffield, Using Generative AI", tier: web, consulted: 2026-10-04, pass: P1, outcome: "not opened; named and summarised by the model (W-0090)" }
- { ref: "FHEQ, CQFW, QAA characteristics statements, Vitae RDF", tier: web, consulted: 2026-10-04, pass: P1, outcome: "used, by summary, as for Reflective Practice's A11" }
```

### D3 Wanted sources
<!-- brief: Every source needed and not reached, with what it would settle; ask Abbott when one blocks a section. -->
```yaml
- { id: W-0087, citation: "Miao, F. and Shiohira, K. (2024) AI Competency Framework for Students, UNESCO, read direct", settles: [A3, A9, A11], asked: not yet, state: wanted }
- { id: W-0088, citation: "Ng, D. T. K., Leung, J. K. L., Chu, S. K. W. and Qiao, M. S. (2021) Conceptualizing AI literacy: an exploratory review, Computers and Education: Artificial Intelligence 2, read direct", settles: [A4, A9], asked: not yet, state: wanted }
- { id: W-0089, citation: "Long, D. and Magerko, B. (2020) What is AI literacy? Competencies and design considerations, CHI 2020, read direct", settles: [A5c, A9], asked: not yet, state: wanted }
- { id: W-0090, citation: "University of Sheffield, Using Generative AI guidance pages (academic integrity; using GenAI critically; for essays and reports; for revision), read direct and dated", settles: [A2, A9, C2], asked: not yet, state: wanted }
- { id: W-0091, citation: "Russell Group (2023) Principles on the use of generative AI tools in education, the full statement, read direct", settles: [A2, A9], asked: not yet, state: wanted }
- { id: W-0092, citation: "Jisc, digital capabilities framework, the individual capabilities, read direct", settles: [A5c, A10], asked: not yet, state: wanted }
- { id: W-0093, citation: "a glossary of AI literacy vocabulary", settles: [B2b], asked: not yet, state: wanted }
- { id: W-0033, citation: "QAA (2020) Characteristics Statements: Master's and Doctoral Degree, read direct", settles: [A11], asked: not yet, state: wanted }
- { id: W-0034, citation: "Vitae (2010) Researcher Development Framework, read direct", settles: [A11], asked: not yet, state: wanted }
```

## Part E Gaps and questions
<!-- brief: Every unknown, conflict and point for Abbott, as it arises. -->
1. **P2 triggers:** 4 and 5: UNESCO, Long and Magerko and the level descriptors were read by summary; Ng and others, Sheffield's guidance and Jisc by catalogue record or the model's own summary only (W-0087 to W-0092). The crosswalk is editorial.
2. **Levels:** `unknown` for every capability (D-ing-0001 (a)).
3. **Capability coverage:** no card sits at Introductory, which holds understanding AI and its limits, the golden rule and never citing output; `/04` describes the pathway's cross-tier design, not a skill. Candidate for the model's author, temporary id: c1 (Introductory) "Explain what generative AI is, what it cannot be trusted to do and the first rule of using it in study". And `/04` to become a design note rather than a card. Open.
4. **Key theory:** open. Candidates: UNESCO (2024) as the tiering backbone, the model's own choice, with Ng and others (2021) for the definition; Sheffield's guidance for the workflow, to be replaced by local policy.
5. **Subject expert sign-off:** the model requires it before authoring, and the institution's own tools, policy and disclosure process to replace the examples.
6. **Currency:** the fastest-moving pathway; every source is to be re-dated at each revision.
7. **Templates:** proposed: an AI use decision checklist, a disclosure statement and a fact-check log.
8. **Integrity coordination:** the model asks that this pathway and Referencing reinforce rather than repeat each other; the split is not yet drawn.
9. **Progression by level (A11):** drafted with the document (J-ing-0001; META D-0205; D-ing-0035, D-ing-0036, D-ing-0038, D-ing-0039). Every level was read by summary only.
10. **Source map:** the guide does not teach this pathway; its source map records where it touches AI.
11. **Vocabulary (D-ing-0050):** built in from the start: no glossary term in the guide; candidates from the model and the sector sources in B2b; A10's direct terms as the term list v1.0 patterns. The search patterns themselves are kept with each consuming project.

---

## Change notes
- 0.1.0: 4 October 2026, 10:06: researched by INGEST research prompt 0.1.10-draft with META's pathway block 0.1.1-draft and META's pathway template 0.3.0-draft (A11); an authored pathway; generic core with A11, metacognition, the D-ing-0050 vocabulary shape and the D-ing-0056 card fields from the start (ing N-0114).
