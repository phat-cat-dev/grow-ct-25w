S = '/home/claude/wkspc2601-library/ingested/standards/ingest-std-qaa-advancehe-esd-2021-execsummary/run-src'
JUDGE = S + '/esd_j.py'
SLUG = 'qaa-advancehe-esd-2021-summary'
PREFIX = 'qaa-advancehe/esd-2021-execsummary'
GU6ROWS = open(S + '/gu6_rows.md').read()

FRONT = '''---
id: std:doc:qaa-advancehe-esd-2021-execsummary
title: "Education for Sustainable Development Guidance: Executive Summary"
profile: standards/execsummary   # proposed variant (Abbott, 06:46; D-std-0012); not yet in the profile
profileVersion: 0.1.6-draft
issuer: The Quality Assurance Agency for Higher Education (QAA) and Advance HE
kind: execsummary
theme: theme:esd
jurisdiction: [England, Wales, Scotland, Northern Ireland]
subjectScope: universal
subjects: []
edition: March 2021 (executive summary of the full guidance)
published: 2021-03-29
status: current   # as at the held text; not checked against either issuer's site (Part E)
supersedes: "QAA and HEA, Education for Sustainable Development: Guidance for UK Higher Education Providers (2014)"
heldText: {{ method: sha256-bytes, raw: {raw}, normalised: {norm} }}
original: {{ method: sha256-bytes, pdf: 1634c4cc3b0454d02b1e1ab3eaa4ffee27c437c514d307c29e5a6d6a62831b60, held: no }}
licence: none read yet
parts:
  S: "the executive summary's 20 statements; the full guidance is std:doc:qaa-advancehe-esd-2021-guidance (S7)"
  GU: "guidance analysis: families, progression, employability, framework and criteria links, pathways, the benchmark web, a crosswalk to the enterprise guidance, pedagogy handed on"
  B: "the two defined terms"
  C: "none"
pins: {{ structure: 0.13.0-draft, template: "execsummary 0.1.0-draft (proposed)", runFrame: 0.1.1-draft, runLayer: 0.5.0-draft }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0057
passes:
  P1: "2026-10-03, std (claude.ai, META Project): read direct from Abbott's PDF of the executive summary (05:40); built 05:52"
  P2: "not needed: the full guidance is its own document (std:doc:qaa-advancehe-esd-2021-guidance, run 0063)"
  P3: open
version: 0.2.1
---
'''

HEAD = '''<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the proposed standards/execsummary variant (template wpk-0016-ingest-pd-template-standards-execsummary.md 0.1.0-draft), with the guidance analysis Part GU -->
# Education for Sustainable Development Guidance (QAA and Advance HE, 2021): executive summary

> Run 0057, P1 by std; renamed from `-guidance` to `-execsummary` at 06:49 (Abbott, 06:46: "we will use execsummary as another standards profile"). The full guidance is now its own document, std:doc:qaa-advancehe-esd-2021-guidance (run 0063), which supersedes this one's analysis wherever the two differ. **A summary, read for what it holds.** The executive summary describes the full guidance rather than reproducing it: its standards content is the guidance's aim for students, five conditions under which ESD is best achieved, the roles of employers and academics, and the names of the eight key competencies for sustainability. The competencies' definitions and the learning outcomes the full guidance aligns with them are not in the summary; this document names them only and asks for the full text (D3). The teaching ideas go to theory ingest (GU7). Every link is our reading and marked `inferred`.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA and Advance HE's 2021 guidance on education for sustainable development, in its six-page public summary: a cross-cutting theme for every subject. Reach for it to say what sustainability education asks of a student (knowledge, understanding, skills and values to act for sustainable futures), which eight competencies it is built on, what an institution does when ESD is embedded, and how it reaches the subject benchmarks (GU6). For the competencies' content and learning outcomes, the full guidance is needed.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Sustainable development is defined as an ongoing, aspirational process of addressing social, environmental and economic concerns together; ESD as building curriculum structures and subject content that support it. The guidance takes the UN's seventeen Sustainable Development Goals as a starting point, moves ESD beyond environmental issues to the links between economy, society and environment, and frames learning as a transformative journey through ways of thinking, practising and being. Its eight key competencies (after UNESCO) are systems thinking, anticipatory thinking, normative, strategic thinking, collaborative, critical thinking, self-awareness, and integrated problem-solving.

## Part S Standard

### S1 Identity
```yaml
issuer: [The Quality Assurance Agency for Higher Education, Advance HE]
title: "Education for Sustainable Development Guidance: Executive Summary"
edition: March 2021
dates: { published: 2021-03-29, other: ["full guidance 2021: std:doc:qaa-advancehe-esd-2021-guidance", "first edition 2014 (QAA and HEA)"] }
kind: execsummary
form: executive summary
heldText: wkspc2601-library/txt/qaa-and-advance-he-2021-education-sustainable-development-guidance-executive-summary-standard.norm.txt
```

### S2 Purpose and scope
<!-- label: both; status: drafted; basis: primary -->
For staff who design, manage and teach courses, and for senior managers, quality staff and those leading teaching. It supports curriculum design and suggests approaches to teaching, learning and assessment, for readers new to the topic. It can serve as a reference point for course design and as an aid to advocacy. Advisory, like all QAA guidance: it sets no level and no threshold.

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
The summary describes the full guidance: an introduction (global and UK context, student expectations), Section 1 (defining SD and ESD), Section 2 (getting started; strategic commitment; involving students, employers, academics, professional services, governance and communities; the five conditions), Section 3 (teaching, learning and assessment: the key competencies, learning outcomes for courses and modules, learning environments), Section 4 (references and resources). Statements are cut from the aims, the five conditions, the roles and the list of competencies.
'''

MID = '''
### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary for the absence of levels; inferred for the alignment -->
No levels. The competencies and the transformative journey are level-free in the summary; the full guidance does not level its learning outcomes either (std:doc:qaa-advancehe-esd-2021-guidance, S5).

### S6 Themes
`theme:esd` (this document is the theme's reference text); `theme:enterprise` (the enterprise guidance ties green and social entrepreneurship to sustainability education, GU2 crosswalk); employability (one direct statement: competencies that speed change once graduates are at work).

### S7 Relations
```yaml
- { type: themeReference, target: theme:esd }
- { type: supersedes, target: "QAA and HEA ESD guidance 2014 (not held)" }
- { type: summaryOf, target: std:doc:qaa-advancehe-esd-2021-guidance, basis: primary }
- { type: citedBy, target: "49 of the 54 subject benchmark statements held cite ESD guidance by title (GU6)", basis: primary }
- { type: citedBy, target: std:doc:qaa-enterprise-2018-guidance, note: "cites the 2014 edition", basis: primary }
- { type: mapsTo, target: std:doc:qaa-fheq-2024-framework, basis: inferred }
- { type: mapsTo, target: std:doc:bristol-generic-2024-assesscriteria, basis: inferred }
- { type: handsTo, target: "theory ingest (ing): the pedagogy in GU7" }
```

### S8 Currency and review
<!-- label: both; status: drafted; basis: primary -->
Published 29 March 2021, replacing the 2014 guidance. The issuers promised workshops and further support; any later revision is unchecked (E2).

### S9 Commentary (optional)
<!-- label: practitioner; status: drafted; basis: inferred -->
Thin as a standards source, rich as a hub. The summary states one aim for students and names eight competencies, but its weight lies in where it is cited: nearly every benchmark has a sustainability paragraph and 37 carry sustainability into their standards, more than enterprise or employability (GU6). The benchmarks, not this summary, are where ESD becomes a subject standard.
'''

GU2 = '''
### GU2 Progression
<!-- label: both; status: drafted; basis: primary for the three ways; inferred for the rest -->
The summary's model of growth is a transformative journey in three ways: of thinking, of practising, of being. It names no stages and no levels. Read against the frameworks:

| Way | Competencies it most draws on (our reading) | Nearest framework strand | Note |
|---|---|---|---|
| thinking | systems, anticipatory, critical thinking | FHEQ Annex D cognitive skills | levels well: the FHEQ's analyse, evaluate, synthesise ladder applies |
| practising | strategic thinking, collaborative, integrated problem-solving | Annex D practical and transferable skills; the "wider abilities" | levels by autonomy and complexity, as in the FHEQ |
| being | normative, self-awareness | none | the frameworks state no values; this is the guidance's addition, and the one hardest to assess by grade |

**Suggestion.** Level the competencies the way the frameworks level cognitive skills: at L4 recognise and describe (the systems a subject touches; the SDGs it bears on); at L5 apply and analyse (trace interactions; compare futures); at L6 evaluate and judge (weigh trade-offs between social, environmental and economic aims; argue a normative position); at L7 act and lead (design and lead an intervention under uncertainty, with stakeholders). Hold "being" outcomes to reflective evidence rather than graded performance.

**Crosswalk to the enterprise guidance** (std:doc:qaa-enterprise-2018-guidance; ours):

| Key competency | Enterprise outcome theme | Note |
|---|---|---|
| systems thinking | decision (analysis and synthesis) | enterprise has no systems view; ESD adds it |
| anticipatory thinking | communication (visualising the future) | both ask for futures thinking |
| normative competency | (none) | enterprise mentions ethics but states no values competency |
| strategic thinking | implementation; decision | planning action to a goal |
| collaborative competency | communication; implementation (teams, relationships) | shared |
| critical thinking | decision; opportunity (evaluating solutions) | shared |
| self-awareness | reflection; the mindset family | shared |
| integrated problem-solving | creativity; opportunity | shared |

Six of the eight have an enterprise counterpart; systems thinking and the normative competency are ESD's own. A pathway or module drawing on both guidance documents can treat the shared six as one competency set with two contexts (venture and sustainability).
'''

GU3 = '''
**Reading.** One statement is direct (graduates' competencies speeding sustainable change at work); most are bridges, because the competencies serve study and work alike. The summary says employers' priorities are shifting towards sustainability, but states no employability outcome. The full guidance involves employers among its key players; its statements on them are wanted (D3).

**Suggestion.** Tag the eight competencies `bridge` and record, in each benchmark ingested, whether its sustainability paragraph names a professional duty (for example a code of conduct or an accrediting body's requirement); where it does, the competency becomes `direct` for that subject.
'''

GU4 = '''
**Reading.** Only two records sit close to an FHEQ statement (critical thinking with the honours descriptor's evaluation of arguments; integrated problem-solving with the master's descriptor's decisions in complex situations). The frameworks name no sustainability outcome; the link runs through the benchmarks. Against the marking criteria, Bristol's problem-solving, decision-making, critical-approach, teamwork and insight rows take the competencies.

**Suggestions for learning outcomes and assessment.**
1. The full guidance aligns learning outcomes with each competency; they are ingested in std:doc:qaa-advancehe-esd-2021-guidance (S4, Table 2) and levelled there (GU2).
2. Until then, a module can name its SDGs and one or two competencies, and write the outcome as the subject task that exercises them, assessed on the matching criterion row.
3. The normative competency and self-awareness need an assessment form neither generic grid has: reflective or position writing judged on how well values are made explicit and reasoned, not on which values are held.
'''

GU5 = '''
**Reading.** Criticality dominates (systems, anticipatory, normative and critical thinking all fall there), then creativity (envisioning better worlds), work-based and experiential learning (strategic and collaborative competencies) and reflective practice (self-awareness). The summary says nothing about writing, sources or referencing.

**Suggestions for pathways.**
1. Criticality: add the systems and normative competencies as a strand (weighing interconnected social, environmental and economic aims), which the frameworks' cognitive skills do not name.
2. Reflective practice: self-awareness here means one's values and part in change, a wider object than reflection on learning; a reflective-practice pathway can carry it as its "being" strand.
3. Creativity: anticipatory thinking and envisioning futures pair with the enterprise guidance's creativity theme.
'''

TAIL = '''
### GU6 The benchmark web
<!-- label: practitioner; status: drafted; basis: primary for the paragraph and citation counts (a scan of the 54 benchmark texts held in stan); inferred for the reading -->
The same scan as std:doc:qaa-enterprise-2018-guidance GU6, read here for sustainability. Columns as there.

| Benchmark (held text) | Enterprise ¶ | ESD ¶ | Employability ¶ | Cites EEE 2018 | Cites ESD | Enterprise in standards | ESD in standards | Employability in standards |
|---|---|---|---|---|---|---|---|---|
''' + GU6ROWS + '''

**Reading.** Sustainability is the cross-cutting theme that has gone furthest into subject standards: all 54 held benchmarks have sustainability paragraphs, 49 cite ESD guidance by title (either edition; the scan does not separate them), and 37 use sustainability words inside their benchmark standards, against 12 for enterprise. In the standards we sampled, the theme mostly appears as one clause in a list of contexts a graduate weighs (social, economic, environmental, ethical) rather than as a competency of its own; some subjects give it more than one standard (accounting, agriculture and related sciences, architectural technology, for example). A full reading waits on the benchmark runs (S-02).

**Suggestion.** In each benchmark ingested, mark the statements that use sustainability words with `theme:esd` and map them to the key competency they exercise (most often systems or normative thinking). That gives every subject a line from this guidance's competencies to its own threshold.

### GU7 Pedagogy handed to theory ingest
<!-- label: practitioner; status: drafted; basis: primary -->
Named here, not ingested:
- UNESCO's key competencies for sustainability (UNESCO, 2017) and their learning objectives;
- the UN Sustainable Development Goals as a curriculum frame;
- ways of thinking, practising and being as a transformative journey;
- the whole-institution approach;
- co-creation of learning with students;
- learning environments for ESD.

## Part B Terminology
<!-- label: both; status: drafted; basis: primary; paraphrased -->
```yaml
- { term: sustainable development, gloss: "An ongoing process, aspirational in aim, of tackling social, environmental and economic concerns together for a better world." }
- { term: education for sustainable development, gloss: "Building curriculum structures and subject content that support sustainable development." }
- { term: key competencies for sustainability, gloss: "Eight competencies (after UNESCO) that the guidance's learning outcomes are aligned with (S4 competency.b1 to b8)." }
- { term: whole-institution approach, gloss: "Embedding ESD across strategy, curricula, quality processes and staff development, not in single modules." }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->
None.

## Part D Sources

### D1 Held text
The executive summary Abbott supplied (6 pages, sha256-bytes 1634c4cc…), converted with pdftotext and normalised; the PDF is not held in UNI. Figure 1 (the SDGs) is not cut into statements.

### D2 Research log
- 2026-10-03 05:40 to 05:52, std: read direct; 20 statements in four families; crosswalk to the enterprise guidance; benchmark scan shared with run 0056.

### D3 Wanted sources
- W-std-0009: UNESCO (2017), Education for Sustainable Development Goals: Learning Objectives: the source of the competencies.
- W-std-0010: The 2014 QAA and HEA guidance, for the change record.
- W-std-0020: (The full 2021 guidance was supplied by Abbott at 06:46 and is run 0063.)

## Part E Gaps and questions
- E1 A summary: the competencies are named here, not defined (records carry `basis: name only`); their definitions and outcomes are in std:doc:qaa-advancehe-esd-2021-guidance.
- E2 Currency unchecked.
- E3 Every map is ours.

---

## Change notes
- 0.2.1, 3 October 2026, 07:34: provenance lines added to Parts B and C; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.2.0, 3 October 2026, 06:49: renamed `ingest-std-qaa-advancehe-esd-2021-execsummary`, id `std:doc:qaa-advancehe-esd-2021-execsummary`, statement ids `qaa-advancehe/esd-2021-execsummary/...`, variant `standards/execsummary` (Abbott, 06:46; D-std-0012); points to the full guidance, run 0063.
- 0.1.0, 3 October 2026, 05:52: first build, run 0057 (std; Abbott, 05:40).
'''
