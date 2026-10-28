---
id: ing:doc:pathway-finding-using-sources
title: Finding and Using Sources (academic skills pathway)
aliases: [finding sources, searching, search strategy, information literacy, path:finding-using-sources]
subjectKind: framework
practices: [education]
primaryPractice: education
streams: [education/academic-skills]
extensions: [education]
parts:
  A: "partial: the capabilities are proposed, not yet confirmed; the key theory (Kuhlthau) is queued for ingestion, no document yet"
  B: "partial: concepts and terms named by the model; associated vocabulary held as candidates"
  C: "full (recommended)"
pins: { structure: 0.11.0-draft, template: 0.10.0-draft, pathwayTemplate: 0.3.0-draft, theory: 0.3.0-draft, terminology: 0.3.0-draft, process: 0.3.0-draft }
status: drafted
researchedBy: INGEST research prompt 0.1.10-draft, with the pathway block of META's `mta-nts-td-pathway-ingest.md` 0.1.1-draft (sections 2 and 2a)
passes:
  P1: 2 October 2026
  P2: not run; triggers 4 and 5 hold (Part E, item 1)
  P3: "in part: Part E items 3 to 6 settled"
version: 0.1.11
---

<!-- from INGEST wpk-0016-ingest-pd-ingestion-document-template.md 0.10.0-draft; the specification is wpk-0016-ingest-pd-ingestion-document-structure.md -->
# Finding and Using Sources (academic skills pathway)

> **The core document.** Generic: it names no project that uses the pathway. Who made the model and where each claim comes from is in Part D. Companions, never ingested with it: **source maps**, one per guide (the first, for *Excelling at University*, held by `path`, draft), and **integrations**, one per consuming project (`integrations/<project>/`). A capability's level is `unknown` until a source sets it (D-ing-0001 (a)). Fill note from the template kept until P3.

## Part 0 Summary

### 0.1 Agent definition
<!-- brief: Two or three sentences for an agent: what this is and when to reach for it, and one thing it is not for. Write last, from the finished document. -->
<!-- label: editorial; status: drafted; basis: secondary -->
Finding and Using Sources is one of thirteen academic skills pathways: searching for and evaluating academic sources, from using a library's discovery service, through planned searches with keywords, Boolean operators and limiters, to discerning evaluation and comprehensive searching beyond the library. Reach for it to place, sequence or assess a searching or source-evaluation capability, or to translate one into its workplace form. It is not about shaping a research project, which belongs to Researching and Research Methods, nor about citing sources, which belongs to Referencing.

### 0.2 Summary
<!-- brief: One paragraph: who proposed it, when, what it is, its main use and its main dispute. Write last. -->
<!-- label: both; status: drafted; basis: secondary -->
The academic skills pathways model (2026) sets Finding and Using Sources as one of thirteen pathways, drawn from a study skills guide's chapter on search strategies. Its first move is a reframe: academic searching is exploratory, effortful and iterative, not the looking-up of trivia. It climbs in three tiers: searching as a discipline (the library discovery service, the reading list, a five-stage shape of plan, keywords, discovery service, evaluate, extend); search craft (planning from what one already knows, keywords and synonyms, Boolean operators, limiters, iterative narrowing); and extending and evaluating deeply (source-type expectations, currency, authority and above all relevance; subject databases and citation searching for a dissertation). It is the information literacy pathway of the model and sits beside the established information literacy frameworks. Its open question is coverage at Introductory (Part E).

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
- Three tiers, Introductory, Intermediate and Advanced, each with a focus, content, a progression logic and links to other pathways (D:PTM, Pathway 3).
- It covers searching for and evaluating sources, distinct from conceiving a research project (D:PTM, Pathway 3).
- Tiers are anchored to experience of the practice, not to year of study (D:TSPEC, section 2).

### A2 Core principles
<!-- brief: One item per claim the theory rests on, each cited to the authors. Claims only, not uses or benefits. -->
<!-- label: source; status: drafted; basis: primary -->
- Academic searching differs from everyday searching: it is exploratory, effortful and has no exact answer; it is closer to a science (D:EAU, pp. 96-97).
- Searching in an academic context means finding sources relevant to the discipline's discourse and the topic, and engaging critically with them as one sifts them (D:EAU, p. 97).
- Searching tests a learner's self-regulation: it calls for planning, decisions and reflection (D:EAU, p. 97).
- Effective searching has five stages: plan, identify keywords, use the discovery service, evaluate sources, extend the search (D:EAU, p. 101).
- Planning starts from what one already knows, so that searches target the gaps (D:EAU, pp. 101-103).
- Keywords must be specific enough to narrow results; synonyms widen them (D:EAU, pp. 103-104).
- Less experienced students should use the library discovery service before any other tool (D:EAU, p. 105).
- The first criterion of evaluation is knowing what to expect of each source type; then currency, authority and relevance to one's own knowledge-building (D:EAU, pp. 108-109).
- Extending a search beyond the library is not compulsory; if the discovery service finds what is needed, stop there (D:EAU, p. 112).

### A3 Structure
<!-- brief: The spine: every component (level, dimension, stage, category) with its order, parent, the authors' definition (paraphrased, cited), our gloss, key language and an example of our own. Take most care here; other stores link to these components. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
structure: [ladder, set]
components:
  - { slug: introductory, componentType: level, order: 1, parent: none, name: "Introductory: searching as a discipline", authorsDefinition: "academic searching as exploratory, iterative and effortful; why research matters; the library discovery service as first port of call; the module reading list; the five-stage shape (plan, keywords, discovery service, evaluate, extend) (D:PTM, Pathway 3)", gloss: "learn that academic searching is a skill and find sources reliably", keyLanguage: [discovery service, reading list, search, five stages], examples: ["starting from the reading list and then searching the library catalogue for one more book on the topic"], audience: both, beneficiaryGloss: "learn how searching for university sources works and find them reliably", readingLevel: "plain English for a student entering higher education" }
  - { slug: intermediate, componentType: level, order: 2, parent: none, name: "Intermediate: search craft", authorsDefinition: "planning from what you already know; keywords and synonyms; Boolean operators; limiters (date, subject, source type, availability); iterative narrowing (D:PTM, Pathway 3)", gloss: "build targeted searches that return the right results", keyLanguage: [keywords, synonyms, Boolean operators, limiters, narrowing], examples: ["(marketing OR advertising) AND \"social media\" AND sme, limited to journal articles from the last five years"], audience: both, beneficiaryGloss: "plan your keywords and use search tools to get the right results", readingLevel: "plain English for a student entering higher education" }
  - { slug: advanced, componentType: level, order: 3, parent: none, name: "Advanced: extending and evaluating deeply", authorsDefinition: "evaluating with discernment (source-type expectations; currency, authority and above all relevance to your own knowledge-building); extending beyond the discovery service (subject databases, citation searching, scholarly search engines); comprehensive searching for a dissertation (D:PTM, Pathway 3)", gloss: "search comprehensively and judge what you find", keyLanguage: [evaluation, currency, authority, relevance, database, citation searching], examples: ["following the 'cited by' trail from a key article to find newer work that answers it"], audience: both, beneficiaryGloss: "search beyond the library and judge which sources really matter for your work", readingLevel: "plain English for a student entering higher education" }
  - { slug: finding-using-sources-02, componentType: element, order: 1.1, parent: introductory, name: "Use library and discovery services effectively to locate scholarly sources", authorsDefinition: "proposed capability, tier note introduced (D:CARDS)", gloss: "find scholarly sources with the library's tools", keyLanguage: [discovery service, library], examples: [], audience: both, beneficiaryGloss: "use the library search to find academic sources", readingLevel: "plain English for a student entering higher education" }
  - { slug: finding-using-sources-01, componentType: element, order: 2.1, parent: intermediate, name: "Plan a search strategy using keywords and Boolean operators", authorsDefinition: "proposed capability, tier note developed (D:CARDS)", gloss: "plan keywords and combine them to search", keyLanguage: [search strategy, keywords, Boolean operators], examples: [], audience: both, beneficiaryGloss: "plan your search words and how to combine them", readingLevel: "plain English for a student entering higher education" }
  - { slug: finding-using-sources-03, componentType: element, order: 3.1, parent: advanced, name: "Evaluate sources against currency, authority and relevance criteria", authorsDefinition: "proposed capability, tier note extended (D:CARDS)", gloss: "judge sources by date, author and fit", keyLanguage: [currency, authority, relevance], examples: [], audience: both, beneficiaryGloss: "check how recent, how trustworthy and how useful a source is", readingLevel: "plain English for a student entering higher education" }
  - { slug: finding-using-sources-04, componentType: element, order: 3.2, parent: advanced, name: "Extend a search via citation searching and supplementary scholarly tools", authorsDefinition: "proposed capability, tier note extended (D:CARDS)", gloss: "go beyond the library search when the work needs it", keyLanguage: [citation searching, databases, scholarly search engines], examples: [], audience: both, beneficiaryGloss: "follow citations and use specialist databases to find more", readingLevel: "plain English for a student entering higher education" }
```
Capability ids keep the model's numbering, which does not follow tier order here (02 is Introductory, 01 Intermediate).

### A4 Concepts used
<!-- brief: The ideas the theory rests on that other theories share; each will become or match a TERMINOLOGY-DAT concept. -->
<!-- label: both; status: drafted; basis: primary -->
- search-strategy: a structured, planned approach to searching (D:EAU, p. 112).
- discovery-service: the library's search tool across the resources it holds or subscribes to (D:EAU, p. 105).
- keyword: a word or short phrase that drives a search (D:EAU, p. 104).
- boolean-operator: AND, OR, NOT, phrase marks, brackets and truncation that combine or limit keywords (D:EAU, pp. 105-106).
- limiter: a filter on results by date, subject, source type, availability or language (D:EAU, pp. 106-107).
- source-type: the kind of source (article, book, chapter, review, thesis, conference paper) and what to expect of it (D:EAU, pp. 108-109).
- citation-searching: finding later work that cites a given source (D:EAU, p. 111).
- information-literacy: the wider field this pathway belongs to (D:CILIP; read by summary).
- discourse: the conversation of a discipline that sources belong to (D:EAU, p. 97).
- add-on-provision: optional extra-curricular sessions, such as library search workshops, that sit beside the formal learning framework (D:EAU, glossary, pp. x-xiii).
- peer-review: checked by other academics in the discipline before journal publication (D:EAU, glossary, pp. x-xiii).
- reading-list: recommended sources for a module or assessment, usually indicative rather than compulsory (D:EAU, glossary, pp. x-xiii).
- systematic-review: a structured search and review of all existing research on a defined topic (D:EAU, glossary, pp. x-xiii).
- currency: how recent a source is, which matters more in some disciplines than others (D:EAU, pp. 108-109).
- authority: who wrote a source and how established they are in the discipline (D:EAU, p. 109).
- relevance: how far a source serves one's own knowledge-building for the task, the most important criterion (D:EAU, p. 109).
- database: a subject collection of sources searched beyond the discovery service, often found through a librarian (D:EAU, p. 110).
- synonym: a word that means the same as another word; used in searching to enhance search results (D:EAU, glossary, pp. x-xiii; pp. 103-104).
- truncation: a search symbol that finds every word beginning with a stem, also called a wildcard search (D:EAU, p. 106).
- academic-searching: exploratory, iterative and effortful searching for scholarly sources, not a lookup (D:EAU, pp. 96-97).
- everyday-searching: looking things up on a general search engine such as Google (D:EAU, pp. 96-97, 105).

Concepts above from `currency` on were added on 4 October 2026, 10:37: terms named in B2a or B4 that had no definition here (D-ing-0057).

### A5a How practitioners apply it
<!-- brief: From the practitioner's side: the steps they take, the tools and artefacts they use, a worked example, and the decisions they make along the way. Separate what the authors prescribe (source) from how it is done in practice (reported, with sources) and what follows from it (editorial). -->
<!-- label: both; status: drafted; basis: primary -->
Practitioners here are librarians, academic skills staff, tutors and authors of learning material.

**What the authors prescribe** (source):
- Teach the five stages through a contrast of a disorganised and a self-regulating student searching for the same essay (D:EAU, pp. 97-101).
- Use guided tasks in the learner's own discovery service: Boolean operators, then limiters, then sorting (D:EAU, pp. 105-108).
- Send learners to a librarian to find the databases for their discipline (D:EAU, p. 110).

**How it is done in practice** (reported):
- Librarians encourage synonyms for keywords, as in a workshop for social work students (D:EAU, p. 104; evidence: reported).

**Worked example**:
At Introductory, the learner finds two journal articles on a reading-list topic in the discovery service; at Intermediate, they build and refine a Boolean search with limiters and record each version; at Advanced, they extend a dissertation search through a subject database and citation searching and justify which sources they keep (editorial).

### A5b How beneficiaries meet it
<!-- brief: From the beneficiary's side (learner, client, project team, stakeholder): what it asks of them, what they see or do, and any version made for them to use directly. Search for this separately. -->
<!-- label: both; status: drafted; basis: primary -->
- Learners often treat academic searching like looking up trivia and find too much or the wrong things (D:EAU, pp. 96-99; evidence: claimed).
- A first search can return many thousands of results; keywords and limiters bring it down (D:EAU, pp. 106-108; evidence: claimed).
- Learners are asked to reflect on their own searching against the five stages (D:EAU, p. 102; evidence: claimed).

### A5c Contexts and adaptations
<!-- brief: Where it is used (levels, sectors, practices, settings, modes such as online), and how it has been adapted for them, each with its source. -->
<!-- label: both; status: drafted; basis: secondary -->
- Any discipline; currency matters more in fast-moving fields (social media marketing) than in history (D:EAU, pp. 107, 109).
- Extended searching is mainly for final-year and postgraduate dissertations and theses (D:EAU, p. 110).
- UK higher education libraries: SCONUL's Seven Pillars of Information Literacy (2011), seven areas in no fixed order: Identify, Scope, Plan, Gather, Evaluate, Manage, Present (D:SCONUL; read by summary).
- North American higher education: the ACRL Framework for Information Literacy (filed 2015, adopted 2016), six frames, among them Searching as Strategic Exploration and Authority Is Constructed and Contextual (D:ACRL; read by summary).
- Beyond education: CILIP's 2018 definition sets information literacy in everyday life, citizenship, education, the workplace and health (D:CILIP; read by summary).

### A5d Misapplications
<!-- brief: Common ways it is misused or misread, the evidence for each, and how to avoid it. -->
<!-- label: both; status: drafted; basis: primary -->
- Searching without a plan or the question in hand, too late, with keywords copied from the title (D:EAU, pp. 98-99; evidence: claimed); avoid by planning from what one already knows.
- Keywords too broad to narrow results (D:EAU, p. 104; evidence: claimed); avoid by combining specific terms and synonyms.
- Taking any source that looks relevant (D:EAU, p. 108; evidence: claimed); avoid by evaluating source type, currency, authority and relevance.
- Going straight to a web search engine before the library (D:EAU, p. 105; evidence: claimed).

### A6a Benefits to practitioners
<!-- brief: What those who apply it gain. Mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
- A shared five-stage shape for teaching and diagnosing searching (D:EAU, pp. 101-102; evidence: claimed).

### A6b Benefits to beneficiaries
<!-- brief: Name the beneficiaries, then what reaches them and how it reaches them through the practitioner. Search for this separately; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students; later, employers and the people their decisions serve.
- Time saved and better sources found (D:EAU, pp. 101, 103; evidence: claimed).
- Comprehensive, discerning engagement with the discourse for longer work (D:PTM, Pathway 3; evidence: claimed).

### A7a Criticisms of the theory and its application
<!-- brief: Criticisms of the theory itself and of how practitioners apply it, with the evidence for each, marked measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: secondary -->
- none-stated: no published criticism of this pathway exists.
- (editorial) The pathway covers searching and evaluating; managing found information (one of SCONUL's pillars) is not in its tiers and may sit with Referencing.

### A7b Effects on beneficiaries
<!-- brief: Name the beneficiaries, then the harms, costs or limits that reach them through the practitioner's use. Search for this separately, as for A6b; mark each item measured, reported or claimed. -->
<!-- label: both; status: drafted; basis: primary -->
Beneficiaries: students.
- Discovery services differ between institutions, so tool-specific teaching may not transfer (D:EAU, p. 105; evidence: claimed).
- unknown: no evidence yet of how learners fare in the pathway.

### A8 Selection
<!-- brief: When to choose it over named alternatives, and what it suits badly. Our reading (editorial). -->
<!-- label: editorial; status: drafted; basis: secondary -->
Choose this pathway when the aim is to find and judge sources. For shaping a research project, choose `path:researching-research-methods`, whose search phase builds on this one; for engaging critically with a source once found, `path:criticality`; for citing it, `path:referencing`. It suits badly a learner who already searches comprehensively and needs help with argument.

### A9 Relations
<!-- brief: Other theories it revises, extends, derives from, contrasts with or competes with, each with a target id and a one-line note. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: derivedFrom, target: ing:doc:information-search-process-kuhlthau-1991, note: "the key theory: Kuhlthau's Information Search Process (1991), searching as a sequence of stages, each with its feelings, from uncertainty to confidence; explains why academic searching is exploratory and effortful; META INGEST run 0034 (Part E, item 4)" }
- { rel: alternativeTo, target: unknown, note: "SCONUL Seven Pillars of Information Literacy (2011): a UK model of the same ground; no ingestion document yet (Part E, item 4)" }
- { rel: alternativeTo, target: unknown, note: "ACRL Framework for Information Literacy for Higher Education (2015): threshold concepts for the same ground; no ingestion document yet (Part E, item 4)" }
```

### A10 Extension fields
<!-- brief: The practice extension fields for each practice in the front matter, and no others. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
education:
  domain: "cognitive (D:EAU, pp. 96-112)"
  verbs: none-stated
  learnerLevel: "higher education, any year; tiers anchored to experience of searching (D:TSPEC, section 2)"
pathway:
  id: path:finding-using-sources
  title: Finding and Using Sources
  definition: "Searching for and judging academic sources as a planned, iterative practice: using the library's discovery service, building searches with keywords, Boolean operators and limiters, evaluating sources by type, currency, authority and relevance, and extending a search through databases and citations when the work needs it."
  terms:
    direct: [literature, literature review, source, search, retrieval, database, information literacy, reading]
    associated: [discovery service, keyword, Boolean operator, limiter, search strategy, citation searching, currency, authority, relevance]
    source: "direct: the pathway term list v1.0 (D:TERMS; its 8 patterns written as words); associated: candidates from D:EAU and D:PTM (B2b); associated widened from the guide's glossary and the model's tier text (D-ing-0050)"
  competencies:
    - id: finding-using-sources/02
      tierNote: introduced
      statement: Use library and discovery services effectively to locate scholarly sources.
      level: unknown
      verbs: [use, locate]
      theory: [ing:doc:information-search-process-kuhlthau-1991]
      process: [search-strategy]
      professional:
        - statement: Finds reliable information quickly with an organisation's knowledge systems and subscription services.
          equivalence: partial
          gap: "workplace tools are intranets, commercial databases and colleagues; the academic one is the library catalogue and its licensed content"
          frameworks: ["SCONUL Seven Pillars: Gather", "CILIP (2018): information literacy in the workplace"]
    - id: finding-using-sources/c1   # proposed; the model assigns the number
      tierNote: introduced
      statement: Follow a staged search strategy, starting from the reading list and what one already knows.
      level: unknown
      verbs: [follow]
      theory: [ing:doc:information-search-process-kuhlthau-1991]
      process: [search-strategy]
      professional:
        - statement: Starts a search from what the organisation and its people already hold before looking further.
          equivalence: partial
          gap: "the academic starting point is a module reading list set by a tutor; the professional one is internal knowledge, colleagues and past work"
          frameworks: ["SCONUL Seven Pillars: Identify, Scope", "ACRL Framework: Searching as Strategic Exploration"]
    - id: finding-using-sources/01
      tierNote: developed
      statement: Plan a search strategy using keywords and Boolean operators.
      level: unknown
      verbs: [plan]
      theory: [ing:doc:information-search-process-kuhlthau-1991]
      process: [search-strategy]
      professional:
        - statement: Plans and documents searches for evidence, policy, competitors or prior art.
          equivalence: partial
          gap: "professional searches answer a decision under time pressure and may need to be reproducible (systematic or patent searching); the academic one supports an assignment"
          frameworks: ["SCONUL Seven Pillars: Plan", "ACRL Framework: Searching as Strategic Exploration"]
    - id: finding-using-sources/03
      tierNote: extended
      statement: Evaluate sources against currency, authority and relevance criteria.
      level: unknown
      verbs: [evaluate]
      theory: [ing:doc:information-search-process-kuhlthau-1991]
      process: [search-strategy]
      professional:
        - statement: Judges whether information is reliable and relevant enough to base a decision on.
          equivalence: partial
          gap: "the academic form adds scholarly norms (peer review, citation); the professional form adds time pressure and commercial or legal risk"
          frameworks: ["SCONUL Seven Pillars: Evaluate", "ACRL Framework: Authority Is Constructed and Contextual", "CILIP (2018): critical thinking and balanced judgement"]
    - id: finding-using-sources/04
      tierNote: extended
      statement: Extend a search via citation searching and supplementary scholarly tools.
      level: unknown
      verbs: [extend]
      theory: [ing:doc:information-search-process-kuhlthau-1991]
      process: [search-strategy]
      professional:
        - statement: Searches beyond the first tool to cover the evidence comprehensively.
          equivalence: partial
          gap: "the professional form weighs cost and time against completeness; the academic one aims at a comprehensive review"
          frameworks: ["SCONUL Seven Pillars: Scope, Gather", "ACRL Framework: Scholarship as Conversation"]
  external:
    - { framework: "SCONUL Seven Pillars of Information Literacy (2011)", match: [Identify, Scope, Plan, Gather, Evaluate], equivalence: broader }
    - { framework: "ACRL Framework for Information Literacy for Higher Education (2015)", match: ["Searching as Strategic Exploration", "Authority Is Constructed and Contextual", "Scholarship as Conversation"], equivalence: broader }
    - { framework: "CILIP definition of information literacy (2018)", match: [education, workplace], equivalence: broader }
    - { framework: "ESCO", match: [unknown], equivalence: unknown }
  processes: [search-strategy]
  templates: ["search log (proposed)", "search plan (proposed)"]
```
`equivalence` says how the professional form relates to the capability (META D-0175's scale), and in `external` how the framework relates to the pathway. Every item here is editorial: its frameworks were read by summary only (Part E, item 1).

### A11 Progression by level
<!-- brief: How the practice develops across qualification levels 3 to 8, deconstructed at each level into skills, competencies, understandings and literacies (after Lea and Street); level 8 in full; each entry says what changes from the level below; grounded in level descriptors and the key theory. From META's pathway template 0.3.0-draft. -->
<!-- label: both; status: drafted; basis: secondary -->
Each level also carries a metacognitive statement (D-ing-0038, D-ing-0039): what the learner understands about the practice in general and its application, and their stance towards it, on a ladder from applying it because they must (compliance), through knowing why (purpose), investment, ownership and confidence (ownership), to adapting it to personal goals (adaptation) and practising it fluently, applied and communicated as a mode of doing and expression in the service of the disciplinary community (flow). The practice described is finding and evaluating information and sources, never the pathway's tiers. Each level's understandings end with what the practice means for the learner's own development (D-ing-0036). The descriptors were read by summary only (Part E). The feelings and thinking that go with searching follow Kuhlthau's Information Search Process (1991, META run 0034): uncertainty falling as a focus forms; the information literacy models (SCONUL, ACRL) frame the practice from novice to expert.
```yaml
progression:
  levelFramework: "qualification levels 3 to 8: CQFW and RQF numbering; FHEQ levels 4 to 8"
  levels:
    - level: 3
      context: "a learner entering higher education: level 3 study, access and foundation years"
      skills: ["search the web and a library catalogue with simple keywords", "tell an information source from an opinion"]
      competencies: ["finds information for a set task from sources a tutor names"]
      understandings: ["not all information is equally reliable", "for own development: knowing where to look is a skill one can learn"]
      literacies: ["a short list of sources found; notes from them"]
      metacognition: { stance: compliance, statement: "Searches because the task asks for sources; takes the first results that look relevant." }
      changesFromBelow: not-applicable-by-design
      sources: [CQFW, SCONUL]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 4
      context: "the first year of higher education"
      skills: ["use the library discovery service and the reading list", "plan a search: keywords, synonyms, Boolean operators, limiters", "judge relevance, currency and authority"]
      competencies: ["searches iteratively for an assignment and narrows results to what is relevant"]
      understandings: ["academic searching is exploratory and effortful, and uncertainty early on is normal", "for own development: knowing that confusion at the start of a search is a stage, not a failure, sustains persistence"]
      literacies: ["a search plan; a keyword list; a working bibliography"]
      metacognition: { stance: purpose, statement: "Knows why academic searching is planned and iterative, and that early uncertainty is normal; still follows a set method." }
      changesFromBelow: "from finding something to planning a search and judging what is found"
      sources: [FHEQ, KUHLTHAU, SCONUL]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 5
      context: "developing practice, depending on the student: the second year"
      skills: ["search subject databases and use citation searching", "evaluate sources against the expectations of each source type", "form a focus that guides further searching"]
      competencies: ["builds a body of sources that maps a topic's discourse"]
      understandings: ["information is produced in a discourse, and authority is constructed and contextual", "for own development: one's own knowledge decides what is relevant, so searching and learning grow together"]
      literacies: ["an annotated bibliography; a search log"]
      metacognition: { stance: investment, statement: "Invests in building a picture of a field, choosing tools and sources with purpose; sees searching and learning growing together." }
      changesFromBelow: "from searching the discovery service to extending into databases and citation chains, guided by a focus"
      sources: [FHEQ, KUHLTHAU, ACRL]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 6
      context: "independent practice: the final undergraduate year, the dissertation"
      skills: ["design a comprehensive search for an extended project", "manage and update searches over months", "evaluate with discernment, including grey literature"]
      competencies: ["searches independently at the forefront of a field"]
      understandings: ["a systematic search can be defended and repeated", "for own development: confident searching underpins independence as a learner"]
      literacies: ["a documented search strategy for a dissertation's literature review"]
      metacognition: { stance: ownership, statement: "Owns their search strategy, confident to defend it; evaluates with discernment as a habit." }
      changesFromBelow: "from focused searching for an assignment to a defensible, sustained search for an extended project"
      sources: [FHEQ, SCONUL, KUHLTHAU]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 7
      context: "advanced practice: master's study, professional practice"
      skills: ["run structured or systematic searches with documented protocols", "critically appraise evidence, including research methods", "use information to inform professional decisions"]
      competencies: ["applies information expertise to professional problems with little guidance"]
      understandings: ["evidence bases have gaps and biases that shape what can be known", "for own development: keeping up with a field is part of professional responsibility"]
      literacies: ["a systematic or scoping review protocol; an evidence summary for practice"]
      metacognition: { stance: adaptation, statement: "Adapts searching to new questions, settings and professional needs; shares sources and search expertise with others." }
      changesFromBelow: "from a defensible search to systematic searching and critical appraisal for advanced scholarship and practice"
      sources: [FHEQ, QAAMSC, ACRL]
      provenance: { label: both, status: drafted, basis: secondary }
    - level: 8
      context: "doctoral practice: an original contribution to knowledge, the researcher's identity and independence"
      skills: ["establish the full state of knowledge to show where a contribution lies", "track a field continuously as it moves", "manage information and data across a long project"]
      competencies: ["knows the forefront of the discipline well enough to show what is new"]
      understandings: ["the gap one fills is defined by what the search shows does not yet exist", "for own development: one's own work becomes part of the information landscape others search"]
      literacies: ["the thesis's literature review establishing originality; data management plans"]
      metacognition: { stance: flow, statement: "Searching and evaluating are fluent and tacit, in the flow; they keep the state of knowledge in view and communicate it, so their own work extends the record in the service of their disciplinary community." }
      changesFromBelow: "a different kind, not more of level 7: searching establishes where an original contribution sits, and one's work joins the record"
      sources: [QAADOC, VITAE, FHEQ]
      provenance: { label: both, status: drafted, basis: secondary }
```

## Part B Terminology

### B1 Concepts
<!-- brief: One concept per idea that has a name in this theory (each A3 component, each A4 concept): plain definition, scope note, category, practices. -->
<!-- label: both; status: drafted; basis: primary -->
By rule: one concept per A3 tier and per A4 concept, definition as A3's gloss or A4's line. The exceptions:
```yaml
- slug: search-strategy
  definition: a planned, staged approach to searching, from objectives and keywords to evaluation and extension
  beneficiaryDefinition: "a plan for how you will search, step by step"
  readingLevel: "plain English for a student entering higher education"
  scopeNote: "the guide's five stages; distinct from a research project's design"
  category: process
  practices: [education]
- slug: boolean-operator
  definition: a word or symbol that combines, excludes or groups keywords in a search (AND, OR, NOT, phrase marks, brackets, truncation)
  scopeNote: "truncation and wildcards are grouped here as the guide groups them"
  category: technique
  practices: [education]
```

### B2a Terms named by the authors
<!-- brief: Every name the authors give a concept: preferred and admitted forms, their alternative names and spelling variants, in full (no compact rule); part of speech, register, extension fields. -->
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: search-strategy, form: search strategy, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: discovery-service, form: discovery service, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: discovery-service, form: library discovery service, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: keyword, form: keyword, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: synonym, form: synonym, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: boolean-operator, form: Boolean operator, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: truncation, form: truncation, lang: en, partOfSpeech: noun, termStatus: preferred, register: discipline-specific }
- { concept: truncation, form: wildcard search, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: discipline-specific }
- { concept: limiter, form: limiter, lang: en, partOfSpeech: noun, termStatus: preferred, register: discipline-specific }
- { concept: source-type, form: source type, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: source-type, form: resource type, lang: en, partOfSpeech: noun-phrase, termStatus: admitted, register: general }
- { concept: currency, form: currency, lang: en, partOfSpeech: noun, termStatus: preferred, register: discipline-specific }
- { concept: authority, form: authority, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: relevance, form: relevance, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: database, form: database, lang: en, partOfSpeech: noun, termStatus: preferred, register: general }
- { concept: citation-searching, form: citation searching, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: reading-list, form: module reading list, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: add-on-provision, form: add-on provision, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
- { concept: peer-review, form: peer-reviewed, lang: en, partOfSpeech: adjective, termStatus: preferred, register: discipline-specific }
- { concept: reading-list, form: reading list, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: general }
- { concept: systematic-review, form: systematic review, lang: en, partOfSpeech: noun-phrase, termStatus: preferred, register: discipline-specific }
```

Glossary terms placed in this pathway (D:EAU, glossary, pp. x-xiii; D-ing-0050): add-on provision, citation searching, databases, discovery service, keywords, limiters, peer-reviewed, reading list, search strategy, synonym, systematic review; added here: add-on provision, peer-reviewed, reading list, systematic review.
`usableIn` and `bannedIn`: none-stated. Education extension: `sourceType` is `book` for every term from D:EAU; the rest unknown.

### B2b Associated vocabulary
<!-- brief: The wider vocabulary practitioners reach for (for Bloom, the verb lists), from at least two named secondary sources, with a scholarly analysis of such lists where one exists. Where none exists, list the words as candidates and put the glossary wanted in D3. One membership per component a word is placed in, with its sources and agreement weight; record where sources disagree with the authors. Never store similarity between words: it is computed from embeddings at query time. -->
<!-- label: both; status: drafted; basis: secondary -->
```yaml
- { concept: information-literacy, form: information literacy, frameworkBlocks: [{ component: introductory, sources: [TERMS, CILIP], weight: 2/2 }], status: candidate }
- { concept: retrieval, form: retrieval, frameworkBlocks: [{ component: intermediate, sources: [TERMS], weight: 1/1 }], status: candidate }
- { concept: scholarship-as-conversation, form: scholarship as conversation, frameworkBlocks: [{ component: advanced, sources: [ACRL], weight: 1/1 }], status: candidate }
- { concept: boolean-operators, form: Boolean operators, frameworkBlocks: [{ component: intermediate, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: subject-database, form: subject database, frameworkBlocks: [{ component: advanced, sources: [PTM], weight: 1/1 }], status: candidate }
- { concept: google-scholar, form: Google Scholar, frameworkBlocks: [{ component: advanced, sources: [PTM], weight: 1/1 }], status: candidate }
```
No glossary of information literacy vocabulary was consulted; one is wanted (D3).

### B3 Framework blocks
<!-- brief: For each concept this theory defines its own way: the A3 component, this theory's definition (cited) and its use here. -->
<!-- label: source; status: drafted; basis: primary -->
By rule: each tier concept's framework block is its A3 component and definition. The exception:
```yaml
- { concept: relevance, component: advanced, definitionHere: "the most important evaluation criterion: relevance to one's own knowledge-building (D:PTM, Pathway 3; D:EAU, p. 109)", useHere: "the Advanced evaluation" }
```

### B4 Relations
<!-- brief: Broader, narrower, related, contrasts-with and the order within this theory, between the B1 concepts. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: higher-level-than, from: intermediate, to: introductory, note: "tier order" }
- { rel: higher-level-than, from: advanced, to: intermediate, note: "tier order" }
- { rel: narrower, from: search-strategy, to: information-literacy, note: "searching is one part of information literacy" }
- { rel: related, from: keyword, to: synonym, note: "synonyms widen a keyword (D:EAU, p. 104)" }
- { rel: contrasts-with, from: academic-searching, to: everyday-searching, note: "exploratory, not a lookup (D:EAU, pp. 96-97)" }
```

### B5 Rules
<!-- brief: Our rules on using the terms (such as a verb banned in outcomes), each with its reason. Editorial. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- understand, know, appreciate, be aware of: not used in learning outcomes at any tier, because they name no observable operation (D:TSPEC, section 6).

## Part C Process

### C0 Formality
<!-- brief: Decide first: prescribed, recommended, loose, implied or not applicable, with one sentence on why. If not applicable, stop Part C. -->
<!-- label: both; status: drafted; basis: primary -->
`recommended`: the guide sets out five stages of effective searching and the order to take them, with the last stage optional (D:EAU, pp. 101, 112).

### C1 Process models
<!-- brief: Each process the theory lends itself to: what it achieves, shape, scale, what starts it and what counts as done. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: search-strategy
  summary: find and choose the right sources for a task in five stages
  shape: iterative
  scale: [task]
  scaleNote: "one assessment or tutorial; extended for a dissertation (D:EAU, pp. 101, 110)"
  groundedIn: [ing:doc:pathway-finding-using-sources]
  entry: a task, question or topic
  exit: a set of evaluated sources
```

### C2 Stages
<!-- brief: Each stage in order: purpose, inputs, activities, outputs, roles, the gate that ends it. Mark our arrangement editorial where the authors give no stages, and every activity the sources do not name `inferred: true`. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { model: search-strategy, order: 1, name: Plan, purpose: "review what you know and set the search's objectives (D:EAU, pp. 101-103)", inputs: [], activities: [review existing knowledge, set objectives, decide source types and dates], outputs: [search-plan], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: search-strategy, order: 2, name: Identify keywords, purpose: "choose specific keywords and their synonyms (D:EAU, pp. 103-104)", inputs: [search-plan], activities: [list keywords, add synonyms], outputs: [keyword-list], roles: [student], endsAt: none, repeat: none, audience: both }
- { model: search-strategy, order: 3, name: Use the discovery service, purpose: "search with Boolean operators, limiters and sorting (D:EAU, pp. 104-108)", inputs: [keyword-list], activities: [combine keywords, apply limiters, sort, refine], outputs: [results], roles: [student], endsAt: none, repeat: "refine until results are manageable", audience: both }
- { model: search-strategy, order: 4, name: Evaluate sources, purpose: "choose sources by type, currency, authority and relevance (D:EAU, pp. 108-109)", inputs: [results], activities: [check source type, date, author, fit], outputs: [selected-sources], roles: [student], endsAt: enough-found, repeat: none, audience: both }
- { model: search-strategy, order: 5, name: Extend the search, purpose: "go beyond the library where the work needs it (D:EAU, pp. 109-112)", inputs: [selected-sources], activities: [search subject databases, citation searching, scholarly search engines], outputs: [selected-sources], roles: [student, librarian], endsAt: none, repeat: none, audience: both }
```

### C3 Gates
<!-- brief: Each decision point with criteria that can pass or fail, and what it decides. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- slug: enough-found
  criteria: ["the discovery service has found what the task needs (D:EAU, p. 112)"]
  decides: "stop | branch to stage 5"
  variationPoint: yes
```

### C4 Outputs
<!-- brief: Each product a stage makes: purpose, parts, and what a template for it needs to know. Mark every output the sources do not name `inferred: true`. Where the method names its own document types, record every one complete (purpose, composition, derivation, quality criteria) from its product descriptions; our templates are drafted from those parts, never the method's text copied. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: search-plan, purpose: "set what the search is for", parts: [what I know, gaps, objectives, source types, date range], producedBy: [1], usedBy: [2], templateHint: "short; written before searching", audience: beneficiary, inferred: true }
- { slug: keyword-list, purpose: "the words that drive the search", parts: [keywords, synonyms, combinations], producedBy: [2], usedBy: [3], templateHint: "a table of concepts and their synonyms", audience: beneficiary, inferred: true }
- { slug: search-log, purpose: "record searches so they can be repeated and refined", parts: [date, tool, search string, limiters, number of results, notes], producedBy: [3, 5], usedBy: [4], templateHint: "one row per search", audience: beneficiary, inferred: true }
- { slug: selected-sources, purpose: "the sources kept, with why", parts: [reference, source type, currency, authority, relevance], producedBy: [4, 5], usedBy: [], templateHint: "the evaluation criteria as columns", audience: beneficiary, inferred: true }
```

### C5 Roles
<!-- brief: Who does each stage, from both sides: practitioner roles and beneficiary roles. -->
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: student, responsibilities: [plan, search, evaluate, extend], stagesInvolved: [1, 2, 3, 4, 5] }
- { slug: librarian, responsibilities: [advise on keywords and databases], stagesInvolved: [2, 5] }
- { slug: tutor, responsibilities: [set the reading list and the task], stagesInvolved: [1] }
```

### C6 Variation points
<!-- brief: Where the process can be tailored or branch, by gate. -->
<!-- label: editorial; status: drafted; basis: secondary -->
- enough-found: stop at stage 4 for most tasks; go on to stage 5 for a dissertation or thesis.
- Every tier: the discipline changes the databases, the weight on currency and the source types, never the demand.

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
- { key: PTM, author: "Abbott, S.", title: "Academic skills pathways model: pathway tier mapping, Draft v3 (v3.1)", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [0.2, A1, A3, A6b, B3] }
- { key: TSPEC, author: "Abbott, S.", title: "Academic skills pathways model: tier specification v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A1, A10, B5] }
- { key: CARDS, author: "Abbott, S.", title: "Academic skills pathways model: capability cards with tier notes, proposed", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A3, A10] }
- { key: TERMS, author: "Abbott, S.", title: "Academic skills pathways model: pathway term list v1.0", year: 2026, publisher: unpublished, licence: "author's document", tier: primary, readVia: direct, held: not held, citedIn: [A10, B2b] }
- { key: EAU, author: "Dennis, C. and Abbott, S.", title: "Excelling at University: Academic Literacies and the Development of Graduate Identity", edition: 1st, year: 2026, publisher: Routledge, licence: copyright, tier: primary, readVia: direct, held: not held, citedIn: [A2, A4, A5a, A5b, A5c, A5d, A6a, A6b, A7b, A10, B3, B4, C0, C1, C2, C3] }
- { key: SCONUL, author: SCONUL, title: "The SCONUL Seven Pillars of Information Literacy: core model", year: 2011, tier: professional, readVia: summary, held: not held, citedIn: [A5c, A9, A10] }
- { key: ACRL, author: Association of College and Research Libraries, title: "Framework for Information Literacy for Higher Education", year: 2015, publisher: ALA, tier: professional, readVia: summary, held: not held, citedIn: [A5c, A9, A10, B2b] }
- { key: CILIP, author: CILIP, title: "CILIP Definition of Information Literacy 2018", year: 2018, tier: professional, readVia: summary, held: not held, citedIn: [A4, A5c, A10, B2b] }
- { key: FHEQ, author: Quality Assurance Agency for Higher Education, title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies, 2nd edn (level descriptors unchanged from 2014)", year: 2024, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:qaa-fheq-2024-framework, META, SHA-256 prefix 97c52675225e" }
- { key: CQFW, author: Welsh Government, title: "Credit and Qualifications Framework for Wales: level descriptors", year: 2009, tier: professional, readVia: summary, held: not held, citedIn: [A11], run: "std:doc:welsh-government-cqfw-2009-framework, META, SHA-256 prefix 682642ca28c8" }
- { key: QAAMSC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Master's Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: QAADOC, author: Quality Assurance Agency for Higher Education, title: "Characteristics Statement: Doctoral Degree, 3rd edn", year: 2020, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: VITAE, author: Vitae, title: "Researcher Development Framework", year: 2010, tier: professional, readVia: summary, held: not held, citedIn: [A11] }
- { key: KUHLTHAU, author: "Kuhlthau, C. C.", title: "Inside the search process: information seeking from the user's perspective", year: 1991, tier: secondary, readVia: inherited, held: not held, citedIn: [A9, A11] }
```

### D2 Research log
<!-- brief: Every source opened, used or not, as you open it. -->
```yaml
- { ref: PTM, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: Pathway 3" }
- { ref: TSPEC, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: anchoring" }
- { ref: CARDS, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: four capabilities with tier notes" }
- { ref: TERMS, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: 8 patterns" }
- { ref: EAU, tier: primary, consulted: 2026-10-02, pass: P1, outcome: "used: Ch 7 pp. 94-112" }
- { ref: "https://access.sconul.ac.uk/sites/default/files/documents/coremodel.pdf", tier: professional, consulted: 2026-10-02, pass: P1, outcome: "set aside: returned 404" }
- { ref: "SCONUL Seven Pillars, via https://scalar.usc.edu/works/information-literacy-frameworks/media/seven-pillars-of-information-literacy.2", tier: web, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: the seven pillar names, in no fixed order" }
- { ref: ACRL, tier: professional, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: the six frames; filed February 2015, adopted January 2016" }
- { ref: CILIP, tier: professional, consulted: 2026-10-02, pass: P1, outcome: "used, by summary: definition and five contexts" }
- { ref: "FHEQ, CQFW, QAA characteristics statements, Vitae RDF", tier: web, consulted: 2026-10-03, pass: P1, outcome: "used, by summary, as for Reflective Practice's A11 (its D2 lists the pages)" }
```

### D3 Wanted sources
<!-- brief: Every source needed and not reached, with what it would settle; ask Abbott when one blocks a section. -->
```yaml
- { id: W-0016, citation: "SCONUL (2011) The SCONUL Seven Pillars of Information Literacy: Core Model for Higher Education, read direct", settles: [A5c, A9, A10], asked: not yet, state: wanted }
- { id: W-0017, citation: "ACRL (2015) Framework for Information Literacy for Higher Education, read direct", settles: [A5c, A9, A10], asked: not yet, state: wanted }
- { id: W-0018, citation: "Kuhlthau, C. C. (1991) 'Inside the search process: information seeking from the user's perspective', Journal of the American Society for Information Science, 42(5) (recall)", settles: [A9], asked: META ing, 2 October 2026, state: received (META run 0034, 3 October 2026) }
- { id: W-0031, citation: "QAA (2024) FHEQ, 2nd edn, read direct (the level descriptors)", settles: [A11], asked: not yet, state: received (META std:doc:qaa-fheq-2024-framework, 3 October 2026) }
- { id: W-0032, citation: "CQFW level descriptors, current edition, read direct", settles: [A11], asked: not yet, state: received (META std:doc:welsh-government-cqfw-2009-framework, 3 October 2026) }
- { id: W-0033, citation: "QAA (2020) Characteristics Statements: Master's and Doctoral Degree, read direct", settles: [A11], asked: not yet, state: wanted }
- { id: W-0034, citation: "Vitae (2010) Researcher Development Framework, read direct", settles: [A11], asked: not yet, state: wanted }
```

## Part E Gaps and questions
<!-- brief: Every unknown, conflict and point for Abbott, as it arises. -->
1. **P2 triggers:** 4 and 5: the external frameworks were read by summary only, and SCONUL's own page returned an error (W-0016, W-0017). The crosswalk is editorial.
2. **Levels:** `unknown` for every capability (D-ing-0001 (a)).
3. **Capability coverage:** settled. One capability added by the model's author (D-ing-0012 (a), Abbott, 22:42): c1 "Follow a staged search strategy, starting from the reading list and what one already knows" (Introductory), with a temporary id until the model numbers it.
4. **Theory links:** settled (D-ing-0013 (a), Abbott, 22:44): Kuhlthau's Information Search Process (1991) is the key theory, queued at META's ing; SCONUL's Seven Pillars and the ACRL Framework stay as external frameworks for the crosswalk (A10), not theories. Kuhlthau's details are recall until read; A9's target and the capabilities' `theory:` fill in when the document exists (W-0018).
5. **Managing information:** settled (D-ing-0014 (a), Abbott, 22:48): SCONUL's Manage pillar (organising and storing what is found, reference management) stays out of this pathway and is carried to the Referencing pathway (`path:referencing`), where recording a source belongs with citing it. The crosswalk in A10 matches no capability here to Manage.
6. **Templates:** settled (D-ing-0015 (a), Abbott, 22:50): the search plan and the search log (C3) stay here as proposals, not in COMPOSE's catalogue, and are offered to COMPOSE through META's ing when this document reaches `checked`. The log matters most at Advanced, where a comprehensive search must be repeatable.
7. **Source map:** what *Excelling at University* teaches for each capability belongs in its guide map (held by `path`, draft), not here.
8. **Progression by level (A11):** drafted 02:36 (J-ing-0001; META D-0205; shape D-ing-0035, D-ing-0036). Every level was read by summary only (W-0031 to W-0034); the entries are editorial readings of the descriptors and the pathway's theory. Kuhlthau's run 0034 is now linked in A9 and in every capability's `theory:` (the key theory, D-ing-0013 (a)).
9. **Vocabulary (D-ing-0050, Abbott, 11:10):** swept. The guide's glossary terms for this pathway are in B2a (and A4 where new); candidates from the model's tier text are in B2b; A10's direct terms are the term list v1.0 patterns as words, with the ruled second version's changes noted. The search patterns themselves are kept with each consuming project, not here. No published glossary of this pathway's vocabulary has yet been read; B2b stays candidates.

---

## Change notes
- 0.1.11: 4 October 2026, 10:37: A4 gains 8 definitions for terms named in B2a or B4 without one, found by compiling the terminology database (D-ing-0057; ing N-0119).
- 0.1.10: 4 October 2026, 10:03: A10 cards corrected (D-ing-0056): verbs matched to each statement, theory filled from the ruled A9 theory, cards with no process marked as needing one or as not a process (ing N-0113).
- 0.1.9: 3 October 2026, 11:10: vocabulary sweep: 4 glossary terms added to B2a (4 new concepts in A4), 3 candidates to B2b, A10 source note, Part E item 9 (D-ing-0050; ing N-0100).
- 0.1.8: 3 October 2026, 05:52: META runs linked: FHEQ and CQFW linked to META's standards runs; W-0031 and W-0032 received (J-ing-0002; ing N-0089).
- 0.1.7: 3 October 2026, 04:41: file renamed to `ingest-path-finding-using-sources.md`; the id is unchanged (ing N-0083).
- 0.1.6: 3 October 2026, 02:49: A11: each level gains a metacognitive statement and stance, compliance to flow (D-ing-0038, D-ing-0039; ing N-0081).
- 0.1.5: 3 October 2026, 02:36: A11 progression by level, levels 3 to 8, with own-development understandings; level descriptors by summary; W-0031 to W-0034; Part E item 8; key theory run linked in A9 and `theory:` (J-ing-0001; META D-0205; D-ing-0035; D-ing-0036; ing N-0078).
- 0.1.4: 2 October 2026, 22:50: Part E item 6 settled, templates offered at `checked` (D-ing-0015 (a); ing N-0039; G-ing-0040).
- 0.1.3: 2 October 2026, 22:48: Part E item 5 settled, Manage carried to Referencing (D-ing-0014 (a); ing N-0038; G-ing-0037).
- 0.1.2: 2 October 2026, 22:44: key theory Kuhlthau linked in A9; Part E item 4 settled (D-ing-0013 (a); ing N-0037; G-ing-0034).
- 0.1.1: 2 October 2026, 22:42: capability c1 added at Introductory; Part E item 3 settled (D-ing-0012 (a); ing N-0036; G-ing-0031).
- 0.1.0: 2 October 2026, 22:36: researched by INGEST research prompt 0.1.10-draft with META's pathway block 0.1.1-draft; generic core from the start (ing N-0034; G-ing-0028).
