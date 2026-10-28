---
id: ing:doc:pathway-researching-research-methods
title: Researching and Research Methods (academic skills pathway)
aliases: [researching, research methods, research skills, path:researching-research-methods]
subjectKind: framework
practices: [education]
primaryPractice: education
streams: [education/academic-skills]
extensions: [education]
parts:
  A: "partial: the capabilities are proposed, not yet confirmed; no theory of research method is ingested yet to link to"
  B: "partial: concepts and terms named by the model; associated vocabulary held as candidates"
  C: "full (recommended)"
pins: { structure: 0.11.0-draft, template: 0.10.0-draft, pathwayTemplate: 0.3.0-draft, theory: 0.3.0-draft, terminology: 0.3.0-draft, process: 0.3.0-draft }
status: drafted
researchedBy: INGEST research prompt 0.1.10-draft, with the pathway block of META's `mta-nts-td-pathway-ingest.md` 0.1.1-draft (sections 2 and 2a)
passes:
  P1: 2 October 2026
  P2: not run; triggers 4 and 5 hold (Part E, item 1)
  P3: open
version: 0.1.16
---

<!-- from INGEST wpk-0016-ingest-pd-ingestion-document-template.md 0.10.0-draft; the specification is wpk-0016-ingest-pd-ingestion-document-structure.md -->
# Researching and Research Methods (academic skills pathway)

> **The core document.** Generic: it names no project that uses the pathway. Who made the model and where each claim comes from is in Part D. Companions, never ingested with it: **source maps**, one per guide (the first, for *Excelling at University*, held by `path`, draft), and **integrations**, one per consuming project (`integrations/<project>/`). Rules applied from the first pathway: a capability's level is `unknown` until a source sets it (D-ing-0001 (a)). Fill note from the template kept until P3.

## Part 0 Summary

### 0.1 Agent definition
<!-- brief: Two or three sentences for an agent: what this is and when to reach for it, and one thing it is not for. Write last, from the finished document. -->
<!-- label: editorial; status: drafted; basis: secondary -->
Researching and Research Methods is one of thirteen academic skills pathways: doing a research project, from framing a question to the proposal, the literature review and the report, to running research with rigour and ethics, as in a dissertation. Reach for it to place, sequence or assess a research capability, or to translate one into its workplace form. It is not about finding and evaluating sources, which belongs to the pathway on finding and using sources, nor a theory of research method.

### 0.2 Summary
<!-- brief: One paragraph: who proposed it, when, what it is, its main use and its main dispute. Write last. -->
<!-- label: both; status: drafted; basis: secondary -->
The academic skills pathways model (2026) gathers into one pathway the research material a study skills guide scatters across several chapters: the research proposal, literature review and report, research ethics and data handling, and the dissertation as the culminating integration of every literacy. It climbs in three tiers: what research is and how a project is shaped (from a broad topic to a researchable question, with rationale, aims and objectives); the research-document genres (proposal, literature review as critique, report); and running research with rigour and ethics (methodology, ethics and data, the dissertation). Its tiers sit higher than most pathways': its first tier already assumes a capable student. Its open questions are about coverage: no capability yet covers methodology or the proposal as a document (Part E).

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
- Three tiers, Introductory, Intermediate and Advanced, each with a focus, content, a progression logic and links to other pathways (D:PTM, Pathway 9).
- Research is a structured project, distinct from an essay; the research-document genres are taught here, not in academic writing, because they are the outputs of doing research (D:PTM, Pathways 6 and 9).
- Tiers are anchored to experience of the practice, not to year of study (D:TSPEC, section 2); this pathway's entry point already assumes a capable student, so all three tiers sit one step higher than most pathways' (D:PTM, Pathway 9, notes; D:TSPEC, section 3).
- It was new when the model grew from nine pathways to thirteen (D:PTM, changes, v2).

### A2 Core principles
<!-- brief: One item per claim the theory rests on, each cited to the authors. Claims only, not uses or benefits. -->
<!-- label: source; status: drafted; basis: primary -->
- A research question moves from the general (a topic) to the specific (a title or question that states the angle taken) (D:EAU, p. 151).
- Research need not be wholly original; much research applies or reassesses existing knowledge (D:EAU, p. 151).
- A project must justify its existence: its rationale says why the research should be done and what it adds (D:EAU, p. 152).
- Aims and objectives follow from background reading in the field's discourse (D:EAU, p. 152).
- The methodology says how the aims will be met and what data will be used and analysed; expectations vary by discipline (D:EAU, p. 153).
- A literature review critiques the discourse (analysing, evaluating and synthesising it) to make the value of the research clear; it does not describe it (D:EAU, p. 157).
- Research with people carries legal and ethical duties: confidentiality of data not in the public domain, and informed consent (D:EAU, p. 187).
- Sound research rests on stated principles of benefit, respect, voluntary informed participation, integrity, accountability and independence (D:EAU, p. 188, after D:ESRC).
- The dissertation draws on every academic literacy, on a larger scale (D:EAU, p. 66).

### A3 Structure
<!-- brief: The spine: every component (level, dimension, stage, category) with its order, parent, the authors' definition (paraphrased, cited), our gloss, key language and an example of our own. Take most care here; other stores link to these components. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
structure: [ladder, set]
components:
  # the three tiers (ladder)
  - { slug: introductory, componentType: level, order: 1, parent: none, name: "Introductory: what research is and how a project is shaped", authorsDefinition: "research as a structured project distinct from an essay; moving from a broad topic to a specific research question; the rationale; aims and objectives (D:PTM, Pathway 9)", gloss: "learn what makes something research and frame a question worth asking", keyLanguage: [research question, topic, rationale, aims, objectives], examples: ["turning an interest in social media marketing into a question about one platform's value to small firms"], audience: both, beneficiaryGloss: "find out what a research project is and turn a topic into a clear question", readingLevel: "plain English for a student entering higher education" }
  - { slug: intermediate, componentType: level, order: 2, parent: none, name: "Intermediate: the research-document genres", authorsDefinition: "the research proposal (title, rationale, aims, methodology, organisation, indicative bibliography); the literature review as critique; the report structure and its variants (D:PTM, Pathway 9)", gloss: "write the documents that plan and report a project", keyLanguage: [research proposal, literature review, report, critique, synthesis], examples: ["a proposal for a final-year project with an indicative bibliography"], audience: both, beneficiaryGloss: "learn to write a research proposal, a literature review and a report", readingLevel: "plain English for a student entering higher education" }
  - { slug: advanced, componentType: level, order: 3, parent: none, name: "Advanced: running research with rigour and ethics", authorsDefinition: "methodology and approach (data, analysis, theoretical lenses); research ethics and data handling (principles, consent, anonymisation, the ethics form); the dissertation as the culminating integration of every literacy (D:PTM, Pathway 9)", gloss: "carry out a project properly and ethically, to a dissertation", keyLanguage: [methodology, data, analysis, ethics, consent, anonymisation, dissertation], examples: ["designing interviews, getting ethical approval and anonymising transcripts for a dissertation"], audience: both, beneficiaryGloss: "do your own research properly and safely, from method to ethics", readingLevel: "plain English for a student entering higher education" }
  # the capabilities (set; proposed, not yet confirmed)
  - { slug: researching-research-methods-01, componentType: element, order: 1.1, parent: introductory, name: "Formulate a research question, rationale, and aims for a research proposal", authorsDefinition: "proposed capability, tier note introduced, from the Introductory tier's question, rationale and aims (D:CARDS)", gloss: "say what you will ask, why it matters and what you aim to do", keyLanguage: [research question, rationale, aims], examples: ["the general-to-specific table of topics and questions (D:EAU, p. 151)"], audience: both, beneficiaryGloss: "write a clear question, say why it is worth asking, and set your aims", readingLevel: "plain English for a student entering higher education" }
  - { slug: researching-research-methods-02, componentType: element, order: 2.1, parent: intermediate, name: "Structure and write a literature review and a research report", authorsDefinition: "proposed capability, tier note developed, from the Intermediate tier's literature review and report (D:CARDS)", gloss: "review what is known critically, and report what you found", keyLanguage: [literature review, report, critique], examples: ["a literature review that leads to the gap the project fills (D:EAU, pp. 157-160)"], audience: both, beneficiaryGloss: "write a review of the research on your topic and a report of your own", readingLevel: "plain English for a student entering higher education" }
  - { slug: researching-research-methods-c1, componentType: element, order: 2.2, parent: intermediate, name: "Write a research proposal that answers each of its questions", authorsDefinition: "capability added by the model's author from the Intermediate tier's research proposal (D:PTM, Pathway 9; D-ing-0007)", gloss: "plan your project in the proposal's set form", keyLanguage: [research proposal, rationale, methodology, indicative bibliography], examples: ["the history proposal on French ultranationalism (D:EAU, pp. 154-156)"], audience: both, beneficiaryGloss: "write a plan for your research by answering each of the proposal's questions", readingLevel: "plain English for a student entering higher education" }
  - { slug: researching-research-methods-03, componentType: element, order: 3.1, parent: advanced, name: "Apply research ethics principles including informed consent and anonymisation", authorsDefinition: "proposed capability, tier note extended, from the Advanced tier's ethics and data handling (D:CARDS)", gloss: "keep participants and their data safe", keyLanguage: [ethics, informed consent, anonymisation, confidentiality], examples: ["an ethics form for an interview study"], audience: both, beneficiaryGloss: "protect the people in your research and their information", readingLevel: "plain English for a student entering higher education" }
  - { slug: researching-research-methods-04, componentType: element, order: 3.2, parent: advanced, name: "Plan and scope an extended dissertation-length research project", authorsDefinition: "proposed capability, tier note extended, from the Advanced tier's dissertation (D:CARDS)", gloss: "plan a long project you can finish", keyLanguage: [dissertation, scope, plan], examples: ["a timeline for a 10,000-word dissertation"], audience: both, beneficiaryGloss: "plan a big project so you can finish it well", readingLevel: "plain English for a student entering higher education" }
  - { slug: researching-research-methods-c2, componentType: element, order: 3.3, parent: advanced, name: "Choose and justify a methodology and methods of data collection and analysis for a research question", authorsDefinition: "capability added by the model's author from the Advanced tier's methodology and approach (D:PTM, Pathway 9; D-ing-0007)", gloss: "pick how you will answer the question, and say why", keyLanguage: [methodology, methods, data collection, data analysis, theoretical lens], examples: ["choosing semi-structured interviews and thematic analysis for a question about student experience, and saying why not a survey"], audience: both, beneficiaryGloss: "decide how you will collect and analyse your data, and explain why that fits your question", readingLevel: "plain English for a student entering higher education" }
```

### A4 Concepts used
<!-- brief: The ideas the theory rests on that other theories share; each will become or match a TERMINOLOGY-DAT concept. -->
<!-- label: both; status: drafted; basis: primary -->
- research-question: the specific question a project answers (D:EAU, p. 151).
- rationale: why the research should exist (D:EAU, p. 152).
- aims-and-objectives: what the project sets out to achieve, from broad to particular (D:EAU, p. 152).
- methodology: how the aims will be met, with what data and analysis (D:EAU, p. 153).
- literature-review: a critique of the discourse that frames the research (D:EAU, p. 157).
- discourse-community: the scholars of a discipline who make its discourse together (D:EAU, Glossary).
- research-ethics: the principles and duties governing research with people and their data (D:EAU, pp. 187-188).
- informed-consent: voluntary, informed agreement to take part (D:EAU, pp. 187-188).
- dissertation: an extended research project drawing on every literacy (D:EAU, p. 66).
- epistemology: the study of the nature and foundations of knowledge: how something is known (D:EAU, glossary, pp. x-xiii).
- peer-review: checked by other academics in the discipline before journal publication (D:EAU, glossary, pp. x-xiii).
- systematic-review: a structured search and review of all existing research on a defined topic (D:EAU, glossary, pp. x-xiii).
- anonymisation: removing participants' names and identifying details from data, for example by calling them Participant A (D:EAU, p. 187).
- indicative-bibliography: the proposal's list of sources read and to be read (D:EAU, p. 153).
- research-project: a structured inquiry, such as a dissertation, of which the proposal is the plan (D:EAU, p. 150).
- essay: a continuous written response to a set question, distinct from a research project (D:PTM, Pathway 9; D:EAU, p. 145).

Concepts above from `anonymisation` on were added on 4 October 2026, 10:37: terms named in B2a or B4 that had no definition here (D-ing-0057).

### A5a How practitioners apply it
<!-- brief: From the practitioner's side: the steps they take, the tools and artefacts they use, a worked example, and the decisions they make along the way. Separate what the authors prescribe (source) from how it is done in practice (reported, with sources) and what follows from it (editorial). -->
<!-- label: both; status: drafted; basis: primary -->
Practitioners here are those who teach and supervise research: tutors, supervisors, academic skills staff and authors of learning material.

**What the authors prescribe** (source):
- Pitch a lesson to the whole tier at once (D:TSPEC, section 5), remembering that this pathway's tiers sit one step higher (D:TSPEC, section 3).
- Teach the proposal through its questions: title, rationale, aims and objectives, methodology, organisation, indicative bibliography (D:EAU, pp. 150-153).
- Model before asking: a history proposal on French ultranationalism and a literature review on student stress and plagiarism are worked examples (D:EAU, pp. 154-159).
- Point students to the six principles behind any research ethics form (D:EAU, p. 188).

**How it is done in practice** (reported):
- Some institutions split the dissertation into smaller assessed tasks, such as a dissertation proposal in the second year (D:EAU, p. 66; evidence: reported).

**Worked example**:
At Introductory, the learner moves three topics to questions using a general-to-specific table; at Intermediate, they draft a proposal's rationale and aims with a prompt; at Advanced, they choose a method for their own question, justify it and complete an ethics form (editorial).

### A5b How beneficiaries meet it
<!-- brief: From the beneficiary's side (learner, client, project team, stakeholder): what it asks of them, what they see or do, and any version made for them to use directly. Search for this separately. -->
<!-- label: both; status: drafted; basis: primary -->
- Most students meet the literature review in a dissertation or other long research-based work, at undergraduate or postgraduate level (D:EAU, p. 157; evidence: claimed).
- Science students write reports of practical work structured like research articles; business reports add parts such as an executive summary (D:EAU, p. 160; evidence: claimed).
- Students often meet research ethics first as an ethics form to complete (D:EAU, p. 187; evidence: claimed).
- Many believe a dissertation must be original research; it need not be (D:EAU, p. 151; evidence: claimed).

### A5c Contexts and adaptations
<!-- brief: Where it is used (levels, sectors, practices, settings, modes such as online), and how it has been adapted for them, each with its source. -->
<!-- label: both; status: drafted; basis: secondary -->
- Heavily final-year and postgraduate (D:PTM, Pathway 9, notes). A learner with no research experience, such as a first-year student, begins with `path:finding-using-sources` and `path:criticality`, which this pathway builds on (D:PTM, Pathway 9, cross-links; D-ing-0009).
- Disciplines differ: history may not separate the literature review; the social sciences weigh methodology more; sciences and business differ in report structure (D:EAU, pp. 153, 157, 160).
- Doctoral and research careers: the Vitae Researcher Development Framework sets researcher capabilities in four domains (D:RDF; read by summary).
- Government and policy research: the Government Social Research technical framework sets research skills for social researchers (D:GSR; read by summary).
- Research integrity in UK institutions: the Concordat to Support Research Integrity, refreshed in April 2025 (D:UKRIO; read by summary).

### A5d Misapplications
<!-- brief: Common ways it is misused or misread, the evidence for each, and how to avoid it. -->
<!-- label: both; status: drafted; basis: primary -->
- A literature review that describes the literature instead of critiquing it (D:EAU, p. 157; evidence: claimed); avoid by putting one's own view first and using sources to support it (D:EAU, p. 160).
- Starting reading in the middle of the field, at a narrow article, without the broad picture (D:EAU, p. 157; evidence: claimed); avoid by reading in a planned order.
- Treating originality as compulsory (D:EAU, p. 151; evidence: claimed); avoid by framing the contribution honestly.
- Treating ethics as a form to fill rather than principles to apply (editorial).

### A6a Benefits to practitioners
<!-- brief: What those who apply it gain. Mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
- The proposal's questions show a tutor how deeply a student understands the field (D:EAU, p. 150; evidence: claimed).
- One pathway holds the research genres, so they are taught once (D:PTM, Pathways 6 and 9; evidence: claimed).

### A6b Benefits to beneficiaries
<!-- brief: Name the beneficiaries, then what reaches them and how it reaches them through the practitioner. Search for this separately; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students; later, the people and organisations their research serves; research participants.
- A plan that makes a long project manageable (D:EAU, pp. 66, 153; evidence: claimed).
- Participants protected by consent and confidentiality (D:EAU, pp. 187-188; evidence: claimed).

### A7a Criticisms of the theory and its application
<!-- brief: Criticisms of the theory itself and of how practitioners apply it, with the evidence for each, marked measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: secondary -->
- none-stated: no published criticism of this pathway exists.
- (editorial) The capabilities first proposed left out methodology and the proposal as a whole document; two added in P3 fill the gaps (Part E, item 3).

### A7b Effects on beneficiaries
<!-- brief: Name the beneficiaries, then the harms, costs or limits that reach them through the practitioner's use. Search for this separately, as for A6b; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students.
- Pitched one step higher than most pathways, the Introductory tier may be too demanding for a learner with no research experience early in a degree (editorial, from D:PTM, Pathway 9, notes).
- unknown: no evidence yet of how learners fare in the pathway.

### A8 Selection
<!-- brief: When to choose it over named alternatives, and what it suits badly. Our reading (editorial). -->
<!-- label: editorial; status: drafted; basis: secondary -->
Choose this pathway when the aim is to conceive, plan, run or write up a research project; critical research writing (the proposal, the literature review, the research report) is taught here, and Academic Writing signposts to it (D-ing-0023). For searching and evaluating sources, choose `path:finding-using-sources`; for the values of academic integrity and plagiarism, `path:referencing`, which shares ethics with this pathway by cross-reference (integrity covers values and plagiarism; this pathway covers ethics in the field). It suits badly a learner who needs one research method explained in depth: that is a method's own document. A learner new to research, such as a first-year student, starts with Finding and Using Sources and Criticality first.

### A9 Relations
<!-- brief: Other theories it revises, extends, derives from, contrasts with or competes with, each with a target id and a one-line note. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: derivedFrom, target: ing:doc:research-skill-development-willison-2007, note: "META INGEST run, SHA-256 prefix 3690e703821b; the key theory (D-ing-0040): Willison and O'Regan's Research Skill Development framework (2007): six facets of research across five levels of student autonomy, prescribed to open; the scale A11 climbs; queued at META's ing (W-0036)" }
- { rel: derivedFrom, target: unknown, note: "beside the key theory (D-ing-0040): Saunders, Lewis and Thornhill's research onion: queued at INGEST, no document yet; the structure for c2 (Part E, item 4)" }
- { rel: derivedFrom, target: unknown, note: "beside the key theory (D-ing-0040): Hart, Doing a Literature Review: queued at INGEST, no document yet; the model for capability 02 (Part E, item 4)" }
```

### A10 Extension fields
<!-- brief: The practice extension fields for each practice in the front matter, and no others. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
education:
  domain: "cognitive (D:EAU, pp. 150-160) and ethical (D:EAU, pp. 187-188)"
  verbs: none-stated
  learnerLevel: "higher education, mainly final year and postgraduate; tiers anchored to experience of research, not to study level (D:TSPEC, section 2; D:PTM, Pathway 9)"
pathway:
  id: path:researching-research-methods
  title: Researching and Research Methods
  definition: "Doing research as a structured project: framing a researchable question with its rationale and aims, writing the documents that plan and report it, and carrying it out with a sound method and ethical care, up to a dissertation."
  terms:
    direct: [research methods, research design, research ethics, research skills, research project, research question, methods of enquiry, methods of inquiry, empirical, data analysis, data collection, qualitative, quantitative, hypothesis, dissertation]
    associated: [research proposal, literature review, methodology, rationale, aims and objectives, informed consent, anonymisation, research integrity, research report, lab report, report writing]
    source: "direct: the pathway term list v1.0 (D:TERMS; its 15 patterns written as words); associated: candidates from D:EAU and D:PTM, no list places them yet (B2b); research report, lab report and report writing proposed from Academic Writing's list (D-ing-0021 (a)); associated widened from the guide's glossary and the model's tier text (D-ing-0050)"
  competencies:
    - id: researching-research-methods/01
      tierNote: introduced
      statement: Formulate a research question, rationale, and aims for a research proposal.
      level: unknown
      verbs: [formulate]
      theory: [ing:doc:research-skill-development-willison-2007]
      process: [research-proposal]
      professional:
        - statement: Defines a research or evaluation question for a client or policy need, with its purpose and scope.
          equivalence: partial
          gap: "the professional question starts from a client's or policy need and a budget; the academic one from a gap in the discourse"
          frameworks: ["GSR technical framework: identifying research needs, designing and specifying research", "Vitae RDF C2 Research management: research strategy"]
    - id: researching-research-methods/02
      tierNote: developed
      statement: Structure and write a literature review and a research report.
      level: unknown
      verbs: [structure, write]
      theory: [ing:doc:research-skill-development-willison-2007]
      process: [literature-review, research-report]
      professional:
        - statement: Reviews existing evidence and reports findings for decision-makers.
          equivalence: partial
          gap: "the professional review is often rapid and for action, with an executive summary; the academic one is comprehensive and argues for the project's value"
          frameworks: ["GSR technical framework: analysis and interpretation; leading, communicating and championing social research", "Vitae RDF A2 Cognitive abilities: synthesising"]
    - id: researching-research-methods/03
      tierNote: extended
      statement: Apply research ethics principles including informed consent and anonymisation.
      level: unknown
      verbs: [apply]
      theory: [ing:doc:research-skill-development-willison-2007]
      process: [ethics-approval]
      professional:
        - statement: Conducts research within an employer's or funder's ethics and data protection requirements.
          equivalence: partial
          gap: "the professional form adds data protection law, commercial confidentiality and organisational governance; the academic form is approved by a university ethics panel"
          frameworks: ["Vitae RDF C1 Professional conduct: ethics, principles and sustainability; legal requirements", "Concordat to Support Research Integrity (2025)", "ESRC/UKRI research ethics principles"]
    - id: researching-research-methods/04
      tierNote: extended
      statement: Plan and scope an extended dissertation-length research project.
      level: unknown
      verbs: [plan, scope]
      theory: [ing:doc:research-skill-development-willison-2007]
      process: [dissertation]
      professional:
        - statement: Plans and manages a research project to time, scope and budget.
          equivalence: partial
          gap: "the professional project adds budget, commissioning and stakeholders; the dissertation is individual and assessed"
          frameworks: ["Vitae RDF C2 Research management: project planning and delivery; risk management", "GSR technical framework: managing and commissioning social research"]
    - id: researching-research-methods/c1   # proposed; the model assigns the number
      tierNote: developed
      statement: Write a research proposal that answers each of its questions.
      level: unknown
      verbs: [write, answer]
      theory: [ing:doc:research-skill-development-willison-2007]
      process: [research-proposal]
      professional:
        - statement: Writes a research specification or bid that sets out the question, method, outputs and plan.
          equivalence: partial
          gap: "the professional document adds costs, timescales and deliverables for a commissioner or funder; the academic one is assessed by a tutor"
          frameworks: ["GSR technical framework: identifying research needs, designing and specifying research", "Vitae RDF C2 Research management: research strategy"]
    - id: researching-research-methods/c2   # proposed; the model assigns the number
      tierNote: extended
      statement: Choose and justify a methodology and methods of data collection and analysis for a research question.
      level: unknown
      verbs: [choose, justify]
      theory: [ing:doc:research-skill-development-willison-2007]
      process: [research-proposal, dissertation]
      professional:
        - statement: Selects and defends research methods that fit the question, the evidence needed and the constraints.
          equivalence: partial
          gap: "the professional choice weighs cost, time and the decision the evidence serves; the academic one weighs the discipline's expectations"
          frameworks: ["GSR technical framework: knowledge of research methods; identifying research needs, designing and specifying research", "Vitae RDF A1 Knowledge base: research methods, theoretical knowledge and practical application"]
  external:
    - { framework: "Vitae Researcher Development Framework", match: ["A1 Knowledge base: research methods, theoretical knowledge and practical application", "A2 Cognitive abilities", "C1 Professional conduct", "C2 Research management"], equivalence: broader }
    - { framework: "Government Social Research technical framework v4", match: ["technical skills 1 to 4"], equivalence: broader }
    - { framework: "Concordat to Support Research Integrity (2025)", match: [unknown], equivalence: partial }
    - { framework: "ESCO", match: [unknown], equivalence: unknown }
  processes: [research-proposal, literature-review, research-report, ethics-approval, dissertation]
  templates: ["research proposal (proposed)", "literature review (proposed)", "research report (proposed)", "research ethics application (proposed)"]
```
`equivalence` says how the professional form relates to the capability (META D-0175's scale). Every crosswalk item is editorial: its frameworks were read by summary only (Part E, item 1).

### A11 Progression by level
<!-- brief: How the practice develops across qualification levels 3 to 8, deconstructed at each level into skills, competencies, understandings and literacies (after Lea and Street); level 8 in full; each entry says what changes from the level below; grounded in level descriptors and the key theory. From META's pathway template 0.3.0-draft. -->
<!-- label: both; status: drafted; basis: secondary -->
Each level's understandings end with what the practice means for the learner's own development (D-ing-0036). Each level also carries a metacognitive statement (D-ing-0038, D-ing-0039): what the learner understands about the practice in general and its application, and their stance towards it, on a ladder from applying it because they must (compliance), through knowing why (purpose), investment, ownership and confidence (ownership), to adapting it to personal goals (adaptation) and practising it fluently, applied and communicated as a mode of doing and expression in the service of the disciplinary community (flow). The practice described is academic research, never the pathway's tiers. The descriptors were read by summary only (Part E, item 9). Autonomy at each level follows the five levels of student autonomy in Willison and O'Regan's Research Skill Development framework (2007): prescribed, bounded, scaffolded, student-initiated and open research; its six facets (embark and clarify, find and generate, evaluate and reflect, organise and manage, analyse and synthesise, communicate and apply) are recall.
```yaml
progression:
  levelFramework: "qualification levels 3 to 8: CQFW and RQF numbering; FHEQ levels 4 to 8"
  levels:
    - level: 3
      context: "a learner entering higher education: level 3 study, access and foundation years, an extended project"
      skills: ["ask a question that can be investigated", "follow given steps to collect information from set sources", "record and report what was found"]
      competencies: ["completes a small, well-defined investigation set by a tutor (prescribed research)"]
      understandings: ["research answers a question with evidence, unlike an opinion piece", "for own development: a small investigation shows one can find things out for oneself"]
      literacies: ["a short project report in set headings"]
      metacognition: { stance: compliance, statement: "Investigates because the task requires it; sees research as following steps to an answer someone else expects." }
      changesFromBelow: not-applicable-by-design
      sources: [CQFW, RSD]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 4
      context: "the first year of higher education"
      skills: ["narrow a broad topic to a focused question", "write a rationale, an aim and objectives", "collect and interpret simple qualitative or quantitative data within set methods"]
      competencies: ["carries out a small study within limits a tutor sets (bounded research)"]
      understandings: ["a research project differs from an essay: it is designed, and its design is judged", "data must be interpreted, not only reported", "for own development: research moves one from receiving knowledge to finding it"]
      literacies: ["a short research report or project plan in a discipline's standard structure"]
      metacognition: { stance: purpose, statement: "Knows why research is asked of them and how it differs from an essay; still relies on the tutor to set the limits." }
      changesFromBelow: "from following given steps to shaping a question and choosing within set limits"
      sources: [FHEQ, RSD, CQFW]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 5
      context: "developing practice, depending on the student: the second year, research methods modules"
      skills: ["write a research proposal answering its standard questions", "review literature critically to place a question", "compare methods and justify a choice"]
      competencies: ["designs a study with supports a tutor places (scaffolded research)", "knows the main methods of enquiry in the subject and their limits"]
      understandings: ["different methods suit different questions; each has limits", "research is governed by ethics", "for own development: learning research methods sharpens one's judgement of evidence across all one's study"]
      literacies: ["the proposal, the literature review and the research report as genres with their conventions"]
      metacognition: { stance: investment, statement: "Starts to care about questions of their own and invests in designing a study; sees methods as choices that shape what can be found." }
      changesFromBelow: "from a study inside set limits to designing one, with the literature and methods chosen and justified"
      sources: [FHEQ, RSD, ESRC]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 6
      context: "independent practice: the final undergraduate year, the dissertation"
      skills: ["choose and justify a methodology and methods of data collection and analysis", "apply ethics principles: informed consent, anonymisation, data handling", "plan and complete an extended project", "use theoretical lenses to interpret findings"]
      competencies: ["initiates and directs own research with a supervisor's mentoring (student-initiated research)", "manages own learning using scholarly sources at the forefront of the discipline"]
      understandings: ["methodology rests on assumptions about knowledge", "research has obligations to participants and to integrity", "for own development: running one's own project builds the independence and confidence of an emerging researcher"]
      literacies: ["the dissertation: an extended argument from question to conclusion, in the discipline's conventions"]
      metacognition: { stance: ownership, statement: "Owns a project from question to conclusion, confident in justifying methodology and ethics; knows research as a practice they can direct." }
      changesFromBelow: "from designing a study with support to initiating and running one independently, with methodology justified and ethics applied"
      sources: [FHEQ, RSD, ESRC, UKRIO]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 7
      context: "advanced practice: master's study, professional research"
      skills: ["critically evaluate research and critique methodologies", "apply knowledge in original ways and propose new hypotheses", "use a range of techniques and methods for advanced scholarship"]
      competencies: ["conducts research within a discipline's norms with little supervision (open research)", "applies research and critical perspectives to professional situations"]
      understandings: ["the current problems and forefront insights of the field", "professional responsibility, integrity and ethics in research", "for own development: research capability becomes part of one's professional identity and employability"]
      literacies: ["a master's dissertation or research project, often with a critical review of existing literature"]
      metacognition: { stance: adaptation, statement: "Adapts methods and designs to new problems and professional purposes; communicates research to different audiences and helps others to do it." }
      changesFromBelow: "from independent research to research at the forefront, with methodologies critiqued, not only chosen"
      sources: [FHEQ, QAAMSC, RSD]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 8
      context: "doctoral practice: an original contribution to knowledge, the researcher's identity and independence"
      skills: ["conceptualise, design and carry out a project that generates new knowledge", "adjust the design when problems arise", "manage research governance, resources and funding", "disseminate to academic and wider audiences"]
      competencies: ["creates original research of a quality to satisfy peer review", "acts as an independent researcher across knowledge, personal effectiveness, research governance and engagement"]
      understandings: ["the forefront of the discipline and how one's work extends it", "the researcher's own position, responsibilities and career", "for own development: one's identity, career and standing as a researcher grow through the work and its dissemination"]
      literacies: ["the thesis and the viva; peer-reviewed publication; communication of research beyond the academy"]
      metacognition: { stance: flow, statement: "Research is a mode of doing and expression: questions, methods and writing come fluently, in the flow; they make and communicate original knowledge in the service of their disciplinary community, as an expression of their commitment to it." }
      changesFromBelow: "a different kind, not more of level 7: the researcher makes an original contribution and takes on the identity and independence of a researcher"
      sources: [FHEQ, QAADOC, RDF]
      provenance: { label: both, status: drafted, basis: secondary }
```

## Part B Terminology

### B1 Concepts
<!-- brief: One concept per idea that has a name in this theory (each A3 component, each A4 concept): plain definition, scope note, category, practices. -->
<!-- label: both; status: drafted; basis: primary -->
By rule: one concept per A3 tier and per A4 concept, definition as A3's gloss or A4's line. The exceptions, written out:
```yaml
- slug: research-proposal
  definition: a document that plans a research project through a set of questions (title, rationale, aims and objectives, methodology, organisation, indicative bibliography)
  beneficiaryDefinition: "a plan for your research, written as answers to set questions"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "the Intermediate genre; often assessed before a dissertation"
  category: framework
  practices: [education]
- slug: literature-review
  definition: a critique of the discourse relevant to a project, setting out key works, themes, debates and gaps to show the project's value
  beneficiaryDefinition: "a critical look at what has already been written on your topic"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "a discrete section in most disciplines, woven through in some (history)"
  category: technique
  practices: [education]
- slug: methodology
  definition: how a project will meet its aims, with what data and what analysis
  scopeNote: "the Advanced tier's core; expectations vary by discipline"
  category: approach
  practices: [education]
```

### B2a Terms named by the authors
<!-- brief: Every name the authors give a concept: preferred and admitted forms, their alternative names and spelling variants, in full (no compact rule); part of speech, register, extension fields. -->
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: research-question, form: research question, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: research-question, form: RQ, lang: en, partOfSpeech: noun, termStatus: admitted, register: discipline-specific }
- { concept: rationale, form: rationale, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: aims-and-objectives, form: aims and objectives, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: methodology, form: methodology, lang: en, partOfSpeech: noun, termStatus: preferred, register: discipline-specific }
- { concept: methodology, form: approach, lang: en, partOfSpeech: noun, termStatus: admitted, register: general }
- { concept: research-proposal, form: research proposal, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: research-proposal, form: dissertation proposal, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: literature-review, form: literature review, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: indicative-bibliography, form: indicative bibliography, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: research-ethics, form: research ethics, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: informed-consent, form: informed consent, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: anonymisation, form: anonymisation, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: dissertation, form: dissertation, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: discourse-community, form: discourse community, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: epistemology, form: epistemology, lang: en, partOfSpeech: noun, termStatus: preferred, register: discipline-specific }
- { concept: peer-review, form: peer-reviewed, lang: en, partOfSpeech: adjective, termStatus: preferred, register: discipline-specific }
- { concept: systematic-review, form: systematic review, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

Glossary terms placed in this pathway (D:EAU, glossary, pp. x-xiii; D-ing-0050): epistemology, peer-reviewed, rationale, systematic review; added here: epistemology, peer-reviewed, systematic review.
`usableIn` and `bannedIn`: none-stated. Education extension: `sourceType` is `book` for every term from D:EAU; the rest unknown.

### B2b Associated vocabulary
<!-- brief: The wider vocabulary practitioners reach for (for Bloom, the verb lists), from at least two named secondary sources, with a scholarly analysis of such lists where one exists. Where none exists, list the words as candidates and put the glossary wanted in D3. One membership per component a word is placed in, with its sources and agreement weight; record where sources disagree with the authors. Never store similarity between words: it is computed from embeddings at query time. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
- { concept: qualitative-research, form: qualitative, frameworkBlocks: [{ component: advanced, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: quantitative-research, form: quantitative, frameworkBlocks: [{ component: advanced, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: hypothesis, form: hypothesis, frameworkBlocks: [{ component: introductory, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: empirical-research, form: empirical, frameworkBlocks: [{ component: advanced, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: research-integrity, form: research integrity, frameworkBlocks: [{ component: advanced, sources: [UKRIO], weight: 1/1 }], status: candidate }
```
No glossary of research methods vocabulary was consulted; one is wanted (D3).

### B3 Framework blocks
<!-- brief: For each concept this theory defines its own way: the A3 component, this theory's definition (cited) and its use here. -->
<!-- label: source; status: drafted; basis: primary -->
By rule: each tier concept's framework block is its A3 component and definition. The exceptions:
```yaml
- { concept: literature-review, component: intermediate, definitionHere: "a critique, not a description, of the discourse (D:EAU, p. 157)", useHere: "the Intermediate genre that leads to the project's gap" }
- { concept: research-question, component: introductory, definitionHere: "the specific end of a move from general topic to specific question (D:EAU, p. 151)", useHere: "the Introductory task" }
```

### B4 Relations
<!-- brief: Broader, narrower, related, contrasts-with and the order within this theory, between the B1 concepts. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: higher-level-than, from: intermediate, to: introductory, note: "tier order" }
- { rel: higher-level-than, from: advanced, to: intermediate, note: "tier order" }
- { rel: narrower, from: research-question, to: research-proposal, note: "the question is the proposal's first part" }
- { rel: related, from: literature-review, to: discourse-community, note: "the review maps the community's discourse" }
- { rel: related, from: research-ethics, to: informed-consent, note: "consent is one of the six principles (D:EAU, p. 188)" }
- { rel: contrasts-with, from: research-project, to: essay, note: "research is a structured project distinct from an essay (D:PTM, Pathway 9)" }
```

### B5 Rules
<!-- brief: Our rules on using the terms (such as a verb banned in outcomes), each with its reason. Editorial. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- understand, know, appreciate, be aware of: not used in learning outcomes at any tier, because they name no observable operation (D:TSPEC, section 6).

## Part C Process

### C0 Formality
<!-- brief: Decide first: prescribed, recommended, loose, implied or not applicable, with one sentence on why. If not applicable, stop Part C. -->
<!-- label: both; status: drafted; basis: primary -->
`recommended`: the proposal's parts and the report's structure are set out as recommended practice, with variation by discipline and institution (D:EAU, pp. 150-160).

### C1 Process models
<!-- brief: Each process the theory lends itself to: what it achieves, shape, scale, what starts it and what counts as done. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: research-proposal
  summary: plan a project by answering the proposal's questions
  shape: linear
  scale: [task]
  scaleNote: "one proposal (D:EAU, pp. 150-156)"
  groundedIn: [ing:doc:pathway-researching-research-methods]
  entry: a topic of interest
  exit: an approved proposal
- slug: literature-review
  summary: read the discourse in a planned order and write a critique that shows the project's value
  shape: iterative
  scale: [task]
  scaleNote: "one review (D:EAU, pp. 157-160)"
  groundedIn: [ing:doc:pathway-researching-research-methods]
  entry: a research question
  exit: a written review that identifies the gap
- slug: ethics-approval
  summary: show how the research meets ethical principles and gain approval before collecting data
  shape: staged-with-gates
  scale: [project]
  scaleNote: "every project with participants or non-public data (D:EAU, pp. 187-188)"
  groundedIn: [ing:doc:pathway-researching-research-methods]
  entry: a planned method involving people or their data
  exit: ethics approval
- slug: research-report
  summary: report a piece of research in the field's structure
  shape: linear
  scale: [task]
  scaleNote: "one report (D:EAU, p. 160)"
  groundedIn: [ing:doc:pathway-researching-research-methods]
  entry: results to report
  exit: a report
- slug: dissertation
  summary: carry an extended project from proposal to submission
  shape: staged-with-gates
  scale: [project]
  scaleNote: "about 10,000 words, often split into assessed parts (D:EAU, p. 66)"
  groundedIn: [ing:doc:pathway-researching-research-methods]
  entry: an approved proposal
  exit: a submitted dissertation
  inferred: true
```

### C2 Stages
<!-- brief: Each stage in order: purpose, inputs, activities, outputs, roles, the gate that ends it. Mark our arrangement editorial where the authors give no stages, and every activity the sources do not name `inferred: true`. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { model: research-proposal, order: 1, name: Title or research question, purpose: "move from a general topic to a specific question (D:EAU, p. 151)", inputs: [], activities: [read around the topic, narrow it], outputs: [research-question], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: research-proposal, order: 2, name: Rationale, purpose: "say why the research should exist (D:EAU, p. 152)", inputs: [research-question], activities: [state interest, approach and contribution], outputs: [rationale], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: research-proposal, order: 3, name: Aims and objectives, purpose: "set what the project will achieve (D:EAU, p. 152)", inputs: [research-question], activities: [derive aims from reading], outputs: [aims], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: research-proposal, order: 4, name: Approach or methodology, purpose: "say how the aims will be met, with what data and analysis (D:EAU, p. 153)", inputs: [aims], activities: [choose data and method], outputs: [method-statement], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: research-proposal, order: 5, name: Organisation, purpose: "outline the chapters and their flow (D:EAU, p. 153)", inputs: [aims], activities: [plan chapters], outputs: [outline], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: research-proposal, order: 6, name: Indicative bibliography, purpose: "show command of the field's literature (D:EAU, p. 153)", inputs: [], activities: [list sources read and to read], outputs: [bibliography], roles: [student], endsAt: proposal-approval, repeat: none, audience: both }
- { model: ethics-approval, order: 1, name: Apply the principles, purpose: "check the plan against the six principles (D:EAU, p. 188)", inputs: [method-statement], activities: [plan consent, confidentiality and data handling], outputs: [ethics-application], roles: [student, supervisor], endsAt: ethics-panel, repeat: "if the panel asks for changes", audience: both }
```

### C3 Gates
<!-- brief: Each decision point with criteria that can pass or fail, and what it decides. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
- slug: proposal-approval
  criteria: ["each proposal question answered", "the question is specific and researchable"]
  decides: go
  variationPoint: yes
  inferred: true
- slug: ethics-panel
  criteria: ["consent, confidentiality and data handling meet the principles (D:EAU, pp. 187-188)"]
  decides: "go | loop back"
  variationPoint: no
```

### C4 Outputs
<!-- brief: Each product a stage makes: purpose, parts, and what a template for it needs to know. Mark every output the sources do not name `inferred: true`. Where the method names its own document types, record every one complete (purpose, composition, derivation, quality criteria) from its product descriptions; our templates are drafted from those parts, never the method's text copied. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: research-proposal-document, purpose: "plan a project for approval", parts: [title or research question, rationale, aims and objectives, approach or methodology, organisation, indicative bibliography], producedBy: [research-proposal], usedBy: [proposal-approval], templateHint: "one heading per question; the history example is a model (D:EAU, pp. 154-156)", audience: both }
- { slug: literature-review-text, purpose: "critique the discourse and show the gap", parts: [key works and authors, themes, debates, gaps], producedBy: [literature-review], usedBy: [dissertation], templateHint: "own view first, sources in support; linked paragraphs (D:EAU, pp. 157-160)", audience: both }
- { slug: research-report-document, purpose: "report a piece of research", parts: [title, abstract, introduction, methodology, results, discussion, conclusion, references], producedBy: [research-report], usedBy: [], templateHint: "sciences as listed; business adds an executive summary and recommendations (D:EAU, p. 160)", audience: both }
- { slug: ethics-application, purpose: "gain ethical approval", parts: [unknown], producedBy: [ethics-approval], usedBy: [ethics-panel], templateHint: "institutional form; its parts vary (D:EAU, p. 187)", audience: both }
```

### C5 Roles
<!-- brief: Who does each stage, from both sides: practitioner roles and beneficiary roles. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: student, responsibilities: [frame, plan, research, write], stagesInvolved: [all] }
- { slug: supervisor, responsibilities: [ask why, guide, approve], stagesInvolved: [research-proposal, ethics-approval, dissertation] }
- { slug: ethics-panel, responsibilities: [approve research with people or their data], stagesInvolved: [ethics-approval], inferred: true }
- { slug: participant, responsibilities: [consent or decline], stagesInvolved: [ethics-approval], inferred: true }
```

### C6 Variation points
<!-- brief: Where the process can be tailored or branch, by gate. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- proposal-approval: the questions asked vary by discipline and institution.
- Every tier: the learner's subject changes the data, methods and report structure, never the demand.

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
- { key: PTM, author: "Abbott, S.", title: "Academic skills pathways model: pathway tier mapping, Draft v3 (v3.1)", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [0.2, A1, A3, A5c, A6a, A7b, A8, A10, B4] }
- { key: TSPEC, author: "Abbott, S.", title: "Academic skills pathways model: tier specification v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A1, A5a, A10, B5] }
- { key: CARDS, author: "Abbott, S.", title: "Academic skills pathways model: capability cards with tier notes, proposed", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A3, A10] }
- { key: TERMS, author: "Abbott, S.", title: "Academic skills pathways model: pathway term list v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A10, B2b] }
- { key: EAU, author: "Dennis, C. and Abbott, S.", title: "Excelling at University: Academic Literacies and the Development of Graduate Identity", edition: 1st, year: 2026, publisher: Routledge, licence: copyright, tier: primary, readVia: direct, held: not held, citedIn: [A2, A3, A4, A5a, A5b, A5c, A5d, A6a, A6b, A10, B3, B4, C0, C1, C2, C3, C4] }
- { key: ESRC, author: UKRI, title: "ESRC Framework for Research Ethics (the six principles, as given in D:EAU)", year: 2021, tier: primary, readVia: inherited, held: not held, citedIn: [A2, A10] }
- { key: RDF, author: "University of Edinburgh, School of Social and Political Science", title: "Researcher Development Framework (Vitae) page", year: unknown, tier: web, readVia: summary, held: not held, citedIn: [A5c, A10] }
- { key: GSR, author: Government Social Research, title: "GSR Technical Framework v4", year: unknown, publisher: UK Government, tier: professional, readVia: summary, held: not held, citedIn: [A5c, A10] }
- { key: UKRIO, author: UK Research Integrity Office, title: "The Concordat to Support Research Integrity (page)", year: 2025, tier: web, readVia: summary, held: not held, citedIn: [A5c, A10, B2b] }
- { key: FHEQ, author: Quality Assurance Agency for Higher Education, title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies, 2nd edn (level descriptors unchanged from 2014)", year: 2024, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:qaa-fheq-2024-framework, META, SHA-256 prefix 97c52675225e" }
- { key: CQFW, author: Welsh Government, title: "Credit and Qualifications Framework for Wales: level descriptors", year: 2009, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:welsh-government-cqfw-2009-framework, META, SHA-256 prefix 682642ca28c8" }
- { key: QAAMSC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Master's Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: QAADOC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Doctoral Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: RSD, author: "Willison, J. W. and O'Regan, K.", title: "Commonly known, commonly not known, totally unknown: a framework for students becoming researchers", journal: "Higher Education Research and Development 26, 393-409", year: 2007, tier: secondary, readVia: summary, held: not held, citedIn: [A11] }
```
`ESRC` is cited through its host, D:EAU, which reproduces the six principles (structure 4b).

### D2 Research log
<!-- brief: Every source opened, used or not, as you open it. -->
```yaml
- { ref: PTM, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: Pathway 9, Pathway 6's hand-off" }
- { ref: TSPEC, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: anchoring, the up-skew" }
- { ref: CARDS, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: four capabilities with tier notes" }
- { ref: TERMS, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: 15 patterns" }
- { ref: EAU, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: Ch 5 p. 66, Ch 9 pp. 150-160, Ch 10 pp. 187-188, Glossary" }
- { ref: "COMPOSE catalogue 0.2.5-draft", tier: primary, consulted: 2026-10-02, pass: P1, outcome: "set aside: no research document templates" }
- { ref: "INGEST runs 0001 to 0032 (names)", tier: scholarly, consulted: 2026-10-02, pass: P1, outcome: "set aside: no theory of research method" }
- { ref: RDF, tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: A1, A2, C1, C2 descriptors" }
- { ref: GSR, tier: professional, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: the technical skills" }
- { ref: UKRIO, tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: refreshed 4 April 2025; commitments not listed on the page" }
- { ref: "FHEQ, CQFW, QAA characteristics statements, Vitae RDF", tier: web, consulted: 2026-10-03, pass: P1, outcome: "used, by summary, as for Reflective Practice's A11 (its D2 lists the pages)" }
- { ref: "RSD, via https://research.uoregon.edu/plan/undergraduate-research/resources/research-skills-development", tier: web, consulted: 2026-10-03, pass: P1, outcome: "used, by summary: the five levels of student autonomy and the citation; the six facets not named there, so recall" }
```

### D3 Wanted sources
<!-- brief: Every source needed and not reached, with what it would settle; ask Abbott when one blocks a section. -->
```yaml
- { id: W-0009, citation: "Vitae (2010) Researcher Development Framework, the full descriptor set, read direct", settles: [A5c, A10], asked: not yet, state: wanted }
- { id: W-0010, citation: "UKRIO and Universities UK (2025) The Concordat to Support Research Integrity, read direct", settles: [A10], asked: not yet, state: wanted }
- { id: W-0011, citation: "UKRI (2021) ESRC Framework for Research Ethics, read direct", settles: [A2, A10], asked: not yet, state: wanted }
- { id: W-0012, citation: "a research methods text for the theory links and vocabulary (for example a standard research design textbook), chosen by Abbott", settles: [A9, B2b], asked: not yet, state: wanted }
- { id: W-0031, citation: "QAA (2024) FHEQ, 2nd edn, read direct (the level descriptors)", settles: [A11], asked: not yet, state: received (META std:doc:qaa-fheq-2024-framework, 3 October 2026) }
- { id: W-0032, citation: "CQFW level descriptors, current edition, read direct", settles: [A11], asked: not yet, state: received (META std:doc:welsh-government-cqfw-2009-framework, 3 October 2026) }
- { id: W-0033, citation: "QAA (2020) Characteristics Statements: Master's and Doctoral Degree, read direct", settles: [A11], asked: not yet, state: wanted }
- { id: W-0036, citation: "Willison, J. W. and O'Regan, K. (2007) Higher Education Research and Development 26, 393-409, read direct, with the RSD framework sheet (the six facets)", settles: [A11, A9], asked: META ing, 3 October 2026, state: received (META run, 3 October 2026) }
```

## Part E Gaps and questions
<!-- brief: Every unknown, conflict and point for Abbott, as it arises. -->
1. **P2 triggers:** 4 and 5: the external frameworks were read by summary only (W-0009 to W-0011). The crosswalk is editorial.
2. **Levels:** `unknown` for every capability (D-ing-0001 (a)).
3. **Capability coverage:** settled. Two capabilities added by the model's author (D-ing-0007 (a), Abbott, 21:51): c1 "Write a research proposal that answers each of its questions" (Intermediate) and c2 "Choose and justify a methodology and methods of data collection and analysis for a research question" (Advanced), with temporary ids until the model numbers them.
4. **Theory links:** settled (D-ing-0008 (a), Abbott, 21:53): Saunders, Lewis and Thornhill's research onion (*Research Methods for Business Students*, latest edition) and Hart's *Doing a Literature Review* (2nd edn, 2018) are to be ingested as theories; Creswell and Creswell's *Research Design* is a source to check them against, not a subject. Both are recall until read; A9's targets fill in when the documents exist (W-0012). [Amended by D-ing-0040, Abbott, 02:56: Willison and O'Regan's Research Skill Development framework (2007) is the key theory, queued at META's ing; the research onion and Hart sit beside it.]
5. **The up-skew:** settled (D-ing-0009 (c), Abbott, 22:07): the pathway keeps its higher start; a learner with no research experience, such as a first-year student, begins with Finding and Using Sources and Criticality, which this pathway builds on (A5c, A8).
6. **Templates:** no research document template exists in COMPOSE; four proposed (A10).
7. **The ethics form's parts** are institutional and unknown here (C4).
8. **Source map:** what *Excelling at University* teaches for each capability belongs in its guide map (held by `path`, draft), not here.
9. **Progression by level (A11):** drafted 02:33 (J-ing-0001; META D-0205; shape D-ing-0035). Every level was read by summary only (W-0031 to W-0033, W-0009, W-0036); the entries are editorial readings of the descriptors and of the RSD framework's autonomy levels. Willison and O'Regan's RSD framework is recommended by META's nts as the key theory, with the research onion and Hart beside it; not yet ruled, and A9 does not link it. [Ruled 02:56, D-ing-0040 (a): A9 links it as the key theory.] The pathway's higher start (item 5) shows here: its own tiers begin where level 4 and 5 practice does.
10. **Report writing:** settled (D-ing-0024 (a), Abbott, 06:04): this pathway teaches the research report and the laboratory report (the science report on practical work: abstract, introduction, methods, results, discussion); the business report and the incident report go to Work-Based and Experiential Learning; Academic Writing signposts both. The term patterns `research report` and `lab report` stay here; `report writing` covers both homes and is for the term list's owner to place. [Amended 06:19, D-ing-0044: Work-Based and Experiential Learning teaches a context-defined report writing lesson in place of the business and incident report; Reflective Practice teaches the professional-practice reflective report; Academic Writing refers to all three.]
11. **Vocabulary (D-ing-0050, Abbott, 11:10):** swept. The guide's glossary terms for this pathway are in B2a (and A4 where new); candidates from the model's tier text are in B2b; A10's direct terms are the term list v1.0 patterns as words, with the ruled second version's changes noted. The search patterns themselves are kept with each consuming project, not here. No published glossary of this pathway's vocabulary has yet been read; B2b stays candidates.

---

## Change notes
- 0.1.16: 4 October 2026, 10:37: A4 gains 4 definitions for terms named in B2a or B4 without one, found by compiling the terminology database (D-ing-0057; ing N-0119).
- 0.1.15: 4 October 2026, 10:03: A10 cards corrected (D-ing-0056): verbs matched to each statement, theory filled from the ruled A9 theory, cards with no process marked as needing one or as not a process (ing N-0113).
- 0.1.14: 3 October 2026, 11:10: vocabulary sweep: 3 glossary terms added to B2a (3 new concepts in A4), 0 candidates to B2b, A10 source note, Part E item 11 (D-ing-0050; ing N-0100).
- 0.1.13: 3 October 2026, 06:19: Part E item 10 amended (D-ing-0044; ing N-0093).
- 0.1.12: 3 October 2026, 06:04: Part E item 10: the research and laboratory report taught here (D-ing-0024 (a); ing N-0091).
- 0.1.11: 3 October 2026, 05:52: META runs linked: FHEQ and CQFW linked to META's standards runs; W-0031 and W-0032 received; RSD linked in A9 and every capability's `theory:`; W-0036 received (J-ing-0002; ing N-0089).
- 0.1.10: 3 October 2026, 04:41: file renamed to `ingest-path-researching-research-methods.md`; the id is unchanged (ing N-0083).
- 0.1.9: 3 October 2026, 02:56: key theory Willison and O'Regan's RSD framework, the research onion and Hart beside it (D-ing-0040 (a); ing N-0082; G-ing-0154).
- 0.1.8: 3 October 2026, 02:49: A11: each level gains a metacognitive statement and stance, compliance to flow (D-ing-0038, D-ing-0039; ing N-0081).
- 0.1.7: 3 October 2026, 02:33: A11: each level's understandings gain the learner's understanding of the practice applied to their own development (D-ing-0036; ing N-0077; G-ing-0134).
- 0.1.6: 3 October 2026, 02:33: A11 progression by level, levels 3 to 8, autonomy after the RSD framework; W-0031 to W-0033 and W-0036; Part E item 9 (J-ing-0001; META D-0205; D-ing-0035; ing N-0076; G-ing-0131).
- 0.1.5: 3 October 2026, 00:02: critical research writing taught here, signposted from Academic Writing (D-ing-0023; ing N-0056; G-ing-0078).
- 0.1.4: 2 October 2026, 23:49: three report terms proposed from Academic Writing (D-ing-0021 (a); ing N-0051; G-ing-0067).
- 0.1.3: 2 October 2026, 22:07: the higher start kept, with an on-ramp through Finding and Using Sources and Criticality (D-ing-0009 (c); ing N-0028; G-ing-0020): A5c, A8 and Part E item 5.
- 0.1.2: 2 October 2026, 21:53: theory links chosen (D-ing-0008 (a); ing N-0027; G-ing-0019): A9 and Part E item 4.
- 0.1.1: 2 October 2026, 21:51: two capabilities added, c1 and c2 (D-ing-0007 (a); ing N-0026; G-ing-0017): A3, A7a, A10 and Part E item 3.
- 0.1.0: 2 October 2026, 21:50: researched by INGEST research prompt 0.1.10-draft with META's pathway block 0.1.1-draft; generic core from the start (ing N-0024; G-ing-0013).
