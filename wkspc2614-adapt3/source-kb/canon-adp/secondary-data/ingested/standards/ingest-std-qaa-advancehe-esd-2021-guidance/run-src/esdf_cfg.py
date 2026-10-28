S = '/home/claude/wkspc2601-library/ingested/standards/ingest-std-qaa-advancehe-esd-2021-guidance/run-src'
JUDGE = S + '/esdf_j.py'
SLUG = 'qaa-advancehe-esd-2021-guidance'
PREFIX = 'qaa-advancehe/esd-2021'
GU6ROWS = open(S + '/gu6_rows.md').read()
import collections as _c
_ns = {}; exec(open(JUDGE).read(), _ns); _R = _ns['R']; _COMP = _ns['COMP']
_BAND = {}
for v in 'identify understand understands recognise describe appreciate access'.split(): _BAND[v] = 'L4'
for v in 'use apply analyse consider link connect communicate present listen work engage draw combine practise undertake assist learn debate collaborate'.split(): _BAND[v] = 'L5'
for v in 'evaluate assess differentiate generate develop demonstrate reflect question take integrate clarify create think address utilise'.split(): _BAND[v] = 'L6'
for v in 'negotiate facilitate employ implement tackle'.split(): _BAND[v] = 'L7'
for v in 'be deal imagine empathise maintain'.split(): _BAND[v] = 'disposition'
def _band(r): return _BAND.get(r['verbs'][0] if r['verbs'] else 'be', '?')
def _profile():
    rows = []
    O = [r for r in _R if r['fam'] == 'outcome']
    for c, name in _COMP.items():
        for col, lab in (('k', 'Knowledge'), ('s', 'Skills'), ('a', 'Attributes and values')):
            rs = [r for r in O if r['id'].split('.')[1] == c and r['id'].split('.')[2][0] == col]
            cnt = _c.Counter(_band(r) for r in rs)
            rows.append(f"| {name} | {lab} | {len(rs)} | " + ' | '.join(str(cnt.get(b, 0)) for b in ('L4', 'L5', 'L6', 'L7', 'disposition')) + ' |')
    tot = _c.Counter((r['id'].split('.')[2][0], _band(r)) for r in O)
    for col, lab in (('k', 'Knowledge'), ('s', 'Skills'), ('a', 'Attributes and values')):
        n = sum(v for (cc, b), v in tot.items() if cc == col)
        rows.append(f"| **all** | **{lab}** | **{n}** | " + ' | '.join(f"**{tot.get((col, b), 0)}**" for b in ('L4', 'L5', 'L6', 'L7', 'disposition')) + ' |')
    return '\n'.join(rows)

FRONT = '''---
id: std:doc:qaa-advancehe-esd-2021-guidance
title: "Education for Sustainable Development Guidance"
profile: standards/guidance   # proposed variant (D-std-0011, P5b); not yet in the profile
profileVersion: 0.1.6-draft
issuer: The Quality Assurance Agency for Higher Education (QAA) and Advance HE
kind: guidance
theme: theme:esd
jurisdiction: [England, Wales, Scotland, Northern Ireland]
subjectScope: universal
subjects: []
edition: March 2021 (second edition)
published: 2021-03
status: current   # as at the held text; not checked against either issuer's site (Part E)
supersedes: "QAA and HEA, Education for Sustainable Development: Guidance for UK Higher Education Providers (2014)"
heldText: {{ method: sha256-bytes, raw: {raw}, normalised: {norm} }}
original: {{ method: sha256-bytes, pdf: 9463b40b98309b37fca334cda8ad2c755f857bdafe8e6c8c17e9d2aa0fcff3d2, held: no }}
licence: none read yet
parts:
  S: "full: 207 statements in thirteen families, 128 of them Table 2's learning outcomes"
  GU: "guidance analysis: families, progression and a verb-level profile of the outcomes, employability, framework and criteria links, pathways, the benchmark web, the crosswalk to the enterprise guidance, pedagogy handed on"
  B: "the guidance's defined terms"
  C: "none"
pins: {{ structure: 0.13.0-draft, template: "guidance 0.1.0-draft (proposed)", runFrame: 0.1.1-draft, runLayer: 0.5.0-draft }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0063
passes:
  P1: "2026-10-03, std (claude.ai, META Project): read direct from Abbott's PDF of the full guidance (06:46); built 06:57"
  P2: "skipped: read direct from the issuers' PDF"
  P3: open
version: 0.1.1
---
'''

HEAD = '''<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the proposed standards/guidance variant (template wpk-0016-ingest-pd-template-standards-guidance.md 0.1.0-draft), with the guidance analysis Part GU -->
# Education for Sustainable Development Guidance (QAA and Advance HE, 2021)

> Run 0063, P1 by std. **The full guidance** (Abbott, 06:46), read for its standards statements: what a student with each sustainability competency can do, know and value, and what the guidance asks of educators and providers so that students can. Its executive summary is a separate document, std:doc:qaa-advancehe-esd-2021-execsummary (variant `execsummary`). Teaching practices and the assessment model go to theory ingest (GU7). Every link to a framework statement, criterion, benchmark or pathway is our reading and marked `inferred`.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA and Advance HE's 2021 guidance on education for sustainable development, second edition: a cross-cutting theme for every subject. Reach for it to say what a student with each of the eight sustainability competencies can do (Table 1's short statements and Table 2's 128 learning outcomes, sorted into knowledge, skills and attributes and values), how learning outcomes for ESD should be written, what an institution, its academics and its services do to embed ESD, and how sustainability reaches the subject benchmarks (GU6). It sets no levels: it tells course designers to adapt its outcomes to the level and credit of each module.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Sustainable development is defined as a continuing process, aspirational in aim, that tackles social, environmental and economic concerns together; ESD as creating curriculum structures and subject content that support and enact it. The guidance takes the SDGs as the policy frame and UNESCO's eight key competencies as the core of learning, grouped as ways of thinking (systems, anticipatory, critical), ways of practising (strategic, collaborative, integrated problem-solving) and ways of being (self-awareness, normative). Table 2 gives indicative outcomes for each competency in three columns. Section 2 sets out who to involve (students, employers, academics, professional services, communities) with guidance for each; Section 3 adds learning environments, teaching practices and an assessment model (for, as and of learning).

## Part S Standard

### S1 Identity
```yaml
issuer: [The Quality Assurance Agency for Higher Education, Advance HE]
title: "Education for Sustainable Development Guidance"
edition: March 2021, second edition
dates: { published: 2021-03, other: ["first edition 2014 (QAA and HEA)", "executive summary: std:doc:qaa-advancehe-esd-2021-execsummary"] }
kind: guidance
chairs: "the ESD Advisory Group's co-chairs (named in the foreword)"
heldText: wkspc2601-library/txt/qaa-and-advance-he-2021-education-sustainable-development-guidance-standard.norm.txt
```

### S2 Purpose and scope
<!-- label: both; status: drafted; basis: primary -->
Mainly for staff who design, manage and teach courses; also for senior managers, quality staff, those directing teaching and staff running extracurricular activity. A reference point for designing, delivering and reviewing curricula, to be read beside the subject benchmark statements and QAA's Quality Code advice and guidance themes; also an advocacy aid. It has no regulatory function: following it does not by itself show compliance with any UK code or framework. It is deliberately not prescriptive about delivery.

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
Chairs' foreword; QAA and Advance HE preface; definitions of terms; introduction (context, audience, purpose, support). Section 1 (what ESD is; the role of higher education; the SDGs). Section 2 (getting started: institutional commitment and the five conditions; curriculum framing and Figure 2's strategic intersections; consulting key players: students, employers and enterprise, academics, professional services and governance, communities; each with guidance points and examples from practice). Section 3 (key competencies: Table 1; the competencies described by ways of thinking, practising and being; course and module learning outcomes; Table 2; learning environments; teaching and assessment guidance; Figure 3, assessment for, as and of learning; Table 3, teaching practices). Section 4 (annotated references and resources). Annex (the advisory group). Statements are cut from the aims, the five conditions, Tables 1 and 2, the competency descriptions, the outcome-design paragraphs, the guidance points and the learning-environment list. Tables are held linearised (D1).
'''

MID = '''
### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary for the absence of levels; inferred for the alignment -->
No levels. The guidance says its Table 2 outcomes are indicative, not a checklist, and that educators should select and adapt them to the discipline, context, level and credit of each module (`design.2`). So the guidance hands levelling to the course designer. GU2 gives a verb-level profile of the outcomes and a suggested ladder; GU4 lists the framework statements records most resemble.

### S6 Themes
`theme:esd` (this document is the theme's reference text); `theme:enterprise` (the employers section names enterprise competencies as a catalyst for sustainable change and cites the enterprise guidance, std:doc:qaa-enterprise-2018-guidance); `theme:edi` (Figure 2 places equality, diversity and inclusion, with decolonisation, among the priorities ESD intersects; collaborative outcomes ask for equitable collaboration); employability (strategic competency is said to include core employability skills; GU3).

### S7 Relations
```yaml
- { type: themeReference, target: theme:esd }
- { type: supersedes, target: "QAA and HEA ESD guidance 2014 (not held)" }
- { type: summarisedBy, target: std:doc:qaa-advancehe-esd-2021-execsummary, basis: primary }
- { type: cites, target: std:doc:qaa-enterprise-2018-guidance, note: "employers and enterprise section; Section 4 resources", basis: primary }
- { type: readWith, target: "the QAA subject benchmark statements (S2)", basis: primary }
- { type: citedBy, target: "49 of the 54 subject benchmark statements held cite ESD guidance by title (GU6)", basis: primary }
- { type: mapsTo, target: std:doc:qaa-fheq-2024-framework, basis: inferred, note: "39 records linked (GU4)" }
- { type: mapsTo, target: std:doc:bristol-generic-2024-assesscriteria, basis: inferred }
- { type: mapsTo, target: std:doc:cardiffmet-generic-2020-assesscriteria, basis: inferred }
- { type: overlaps, target: std:doc:qaa-enterprise-2018-guidance, basis: inferred, note: "GU2 crosswalk" }
- { type: handsTo, target: "theory ingest (ing): the pedagogy in GU7" }
```

### S8 Currency and review
<!-- label: both; status: drafted; basis: primary -->
Second edition, March 2021, after sector consultation from November 2020 to January 2021; replaces the 2014 guidance. Any later revision is unchecked (E1).

### S9 Commentary (optional)
<!-- label: practitioner; status: drafted; basis: inferred -->
This is the richest student-facing standards source we hold outside the frameworks: 128 outcomes, each a plain "a student can" statement, already sorted into knowledge, skills and attributes and values. That three-way split is one the frameworks only half have (knowledge and skills; no values). Its weakness as a standard is that it is level-free and, by its own words, indicative. Its strength is that it is ready to use as learning-outcome text, and that it says how: adapt to level and credit, assess process over product.
'''

GU2 = '''
### GU2 Progression
<!-- label: both; status: drafted; basis: primary for the three ways; inferred for the verb profile and levels -->
The guidance's model of growth is a transformative journey through three ways: thinking (systems, anticipatory, critical), practising (strategic, collaborative, integrated problem-solving) and being (self-awareness, normative), all resting on subject knowledge and knowledge of the SDGs (Table 1's frame). It names no stages and no levels.

**Verb-level profile of Table 2** (ours). Each outcome's first verb placed on the FHEQ document's verb ladder (std:doc:qaa-fheq-2024-framework, SL3): L4 know and describe (identify, recognise, understand, describe, appreciate); L5 apply and analyse (use, apply, analyse, consider, communicate, engage); L6 evaluate and judge (evaluate, assess, develop, demonstrate, reflect, take a position); L7 lead and negotiate under uncertainty (negotiate, facilitate, mediate, implement, lead); disposition (be, deal with, imagine, empathise, maintain).

| Competency | Column | Outcomes | L4 | L5 | L6 | L7 | Disposition |
|---|---|---|---|---|---|---|---|
''' + _profile() + '''

**Reading.** The knowledge column sits mostly at L4 ("identify" alone opens 26 outcomes across the table); the skills column runs mostly at L5 and L6, with five at L7; the attributes and values column mixes judgement with dispositions. So each competency's three columns already form a rough ladder, knowledge first, then skills, then values. But within a column the levels are mixed, and nothing tells a designer which outcome suits which year. The frameworks' level language (independence, complexity, uncertainty) is what is missing.

**Suggestion: a levelled ladder for three competencies** (ours, `suggested`), built from Table 2's own outcomes:

| Competency | L4 | L5 | L6 | L7 |
|---|---|---|---|---|
| systems thinking | describe how environmental, social and economic systems relate (`outcome.systems.k1`) | analyse a complex system in your subject (`s2`, `s3`) | combine varied data into a range of solutions and judge them (`s4`) | identify the levers with most potential for change and act on them under uncertainty (`a4`, `a2`) |
| critical thinking | identify the case for behaviour change (`k2`) | critically analyse a sustainability issue in your subject (`s4`) | reach and test reasoned conclusions; take an evidenced position (`s5`, `a4`) | build a personal ethical code on independent, evidence-based thinking (`a1`) |
| collaborative | recognise group strategies and communication (`k3`, `k4`) | communicate clearly and listen critically (`s1`, `s6`) | work across disciplines towards creative solutions (`s2`) | facilitate and mediate stakeholder conflict; lead (`s5`, `s9`) |

**Crosswalk to the enterprise guidance** (std:doc:qaa-enterprise-2018-guidance; ours). With the full text the overlap is clearer than the summary showed:

| ESD competency | Enterprise outcome theme | Shared ground (record ids) |
|---|---|---|
| systems thinking | decision | analysing and synthesising complex information (`outcome.systems.s4`; enterprise `outcome.decision.b3`) |
| anticipatory thinking | communication; opportunity | visualising futures; reviewing solutions under uncertainty and risk (`outcome.anticipatory.s1`, `s8`, `s9`) |
| critical thinking | decision | evaluating information and building arguments (`outcome.critical.s5`) |
| strategic thinking | implementation; decision | planning and resource management; "core employability skills" (`narrative.strategic.1`) |
| collaborative | communication; implementation | stakeholders, trust, negotiation, leadership (`outcome.collaborative.s5`, `s9`) |
| integrated problem-solving | creativity; opportunity | several solutions for real problems (`outcome.problem.s2` to `s4`) |
| self-awareness | reflection; the mindset family | own competences and learning needs; motivation (`outcome.selfaware.k1`, `s3`) |
| normative | (none) | the enterprise guidance names ethics but has no values competency |

Seven of the eight have an enterprise counterpart; only normative competency is ESD's own (the summary's reading had two). The ESD guidance makes the link itself: enterprise education, it says, can build qualities such as creativity, spotting opportunities, self-determination and adaptability that speed sustainable change.
'''

GU3 = '''
**Reading.** Of 207 records, 39 are direct and 110 bridges. The guidance is more explicit about work than its summary suggested: strategic competency "includes core employability skills" (goal setting, time and resource management, planning and evaluating action); graduates are expected to communicate professionally across disciplines, cultures and borders; careers services should report employers' social and environmental performance; students should be supported to build enterprise skills towards ventures; and competencies can be evidenced on CVs, online profiles, digital badges and the HEAR. In Table 2, the direct outcomes cluster in the skills columns of anticipatory (precaution, risk, scenarios, backcasting, forecasting), strategic (planning tools, stakeholder strategy) and collaborative competency (group management, mediation, leadership, equitable collaboration).

**Suggestions.**
1. Read the anticipatory and strategic skills outcomes as professional competencies: risk evaluation, scenario planning, backcasting and forecasting are workplace methods and can be assessed as such (live briefs, consultancy projects).
2. Use the guidance's evidencing routes (badges, HEAR, CV, PDP) as the bridge to employability records: a competency met in an extracurricular activity is still a standard met.
3. Pair ESD's strategic and collaborative outcomes with the enterprise guidance's implementation and communication outcomes in one employability strand.
'''

GU4 = '''
**Reading.** Thirty-nine records sit close to an FHEQ statement, spread across Levels 4 to 7 because Table 2 spans them: knowledge outcomes near the CertHE's knowledge of concepts (4.10), analysis near the foundation degree's critical analysis (4.12), evaluation and evidence near the honours descriptor (4.15: evaluating arguments, managing own learning, the uncertainty of knowledge, decisions in complex contexts), and negotiation and leadership near the master's (4.17). Bristol's skills criteria take most criterion links (teamwork, problem-solving, decision-making, critical approach, insight, self-management), Cardiff Met's analysis and argument rows the knowledge and critical outcomes. Values and dispositions (empathy, wellbeing, intergenerational fairness) have no criterion in either grid.

**Suggestions for learning outcomes and assessment.**
1. **Writing outcomes.** The guidance's own rule (`design.1`): join subject knowledge and skills, a sustainability competency and the SDGs in each course or module outcome. Pattern: verb at the module's level + subject object + competency context + SDG. Example (ours): "Evaluate the trade-offs between two flood-defence options for a coastal town, weighing social, economic and environmental effects (systems thinking; SDGs 11 and 13)."
2. **Process over product.** The guidance asks for criteria that reward how a student reached a viable solution above the solution (`assessment.b5`). The enterprise guidance asks the same for process-driven assessment. A shared criterion row, "approach to the problem", banded from a described approach at the pass band to an evaluated, adapted approach at 70 and above, would serve both.
3. **For, as and of learning** (Figure 3, adapted from the National Forum): assessment *of* learning shows achievement (self-assessment against holistic criteria, synoptic tasks linking subject to the SDGs); assessment *as* learning builds self-regulation (self-review, peer review, portfolios recording competencies, co-created criteria); assessment *for* learning gives feedback on teaching (scaffolded tasks, real-life scenarios, dialogue). Map each module's assessment to one of the three and to the competency it develops.
4. **Values.** Assess attributes and values through reflection and position-taking, judged on how explicit and well reasoned the values are, never on which values are held.
5. **Synoptic assessment.** The guidance asks for policies that allow it; it is the natural home for systems and integrated problem-solving outcomes at L6 and L7.
'''

GU5 = '''
**Reading.** Criticality dominates (89 records: systems, anticipatory, critical and normative thinking), then work-based and experiential learning (49: strategic and collaborative practice, live problems, communities), reflective practice (32: self-awareness, values, reflection on action), creativity (26: futures, visions, solutions) and starting, progressing and succeeding (15: adaptability, lifelong learning, careers). Finding and using sources, research methods and presenting appear through the critical and problem-solving outcomes (evidence, research methods from other disciplines, communicating complex issues). Referencing, revision and exams are absent; AI and technology appears once (authentic digital assessment), though the guidance's definition of 4IR technologies and its resources on new technologies would support it.

**Suggestions for pathways.**
1. **Criticality:** Table 2's critical thinking skills (`outcome.critical.s1` to `s6`) are a ready outcome set for the pathway's evidence and argument strand; systems and normative thinking add a strand the frameworks lack.
2. **Reflective practice:** self-awareness and normative outcomes give the pathway its "being" strand: values, emotions, wellbeing, own role (`outcome.selfaware.a1` to `a3`, `outcome.normative.a2`).
3. **Work-based and experiential learning:** collaborative and strategic skills (mediation, stakeholder strategy, planning tools, leadership) are the pathway's practice outcomes; the employers guidance (`employers.b1` to `b3`) says what students should be offered.
4. **Creativity:** anticipatory thinking (visions, backcasting, scenarios) pairs with the enterprise guidance's creativity theme.
5. **Finding and using sources:** `outcome.critical.k1`, `s3`, `s6` and `outcome.problem.s5` (evidence across disciplines; telling evidence from opinion) and `environment.b7` (diverse voices in reading lists).
'''

TAIL = '''
### GU6 The benchmark web
<!-- label: practitioner; status: drafted; basis: primary for the paragraph and citation counts (a scan of the 54 benchmark texts held in stan); inferred for the reading -->
The scan shared with std:doc:qaa-enterprise-2018-guidance GU6, read for sustainability. Columns as there.

| Benchmark (held text) | Enterprise ¶ | ESD ¶ | Employability ¶ | Cites EEE 2018 | Cites ESD | Enterprise in standards | ESD in standards | Employability in standards |
|---|---|---|---|---|---|---|---|---|
''' + GU6ROWS + '''

**Reading.** The link runs both ways. The guidance tells readers to use it beside the subject benchmark statements (S2); the benchmarks cite it back (49 of 54 by title, either edition), all 54 have sustainability paragraphs, and 37 carry sustainability words into their benchmark standards, against 12 for enterprise. In the standards we sampled, the theme mostly appears as one clause in a list of contexts a graduate weighs (social, economic, environmental, ethical); some subjects give it more than one standard (accounting, agriculture and related sciences, architectural technology, for example). With the full guidance held, each such benchmark standard can now be mapped to a Table 2 outcome, not just a competency name.

**Suggestion.** When a benchmark is ingested (S-02), tag its sustainability statements `theme:esd` and give each a `mapsTo` to the Table 2 outcome it most resembles (most often systems `k1`, `s5`, critical `s4` or normative `k3`). Then "what does sustainability mean at the threshold in my subject" is a query, not a reading exercise.

### GU7 Pedagogy handed to theory ingest
<!-- label: practitioner; status: drafted; basis: primary -->
Named here, not ingested:
- UNESCO's key competencies for sustainability and its learning objectives for the SDGs (UNESCO, 2017); ESD for 2030 (UNESCO, 2019);
- ways of thinking, practising and being; transformative learning; critical pedagogy;
- the whole-institution approach; ESD as curriculum framing (Figure 2's intersections with employability, enterprise, internationalisation, EDI and decolonisation, health and wellbeing, civic engagement, students as partners, research and knowledge exchange);
- assessment for, as and of learning for SD (Figure 3, after Ireland's National Forum for teaching and learning enhancement); synoptic assessment;
- Table 3's teaching practices: collaborative learning, enquiry-based learning, play-based learning (game-based learning, gamification, simulation), learning through storytelling, problem-based learning;
- triggers and authentic artefacts; the Iceberg Model for systems thinking; the campus as a living laboratory;
- Advance HE's Future Fit Framework (2012); Giangrande and others (2019) on ESD competencies in higher education; the ESDG guidelines (2014);
- UNECE's competences in ESD for educators (2012): a staff competence framework, a standards candidate for this profile (D3).

## Part B Terminology
<!-- label: both; status: drafted; basis: primary; paraphrased -->
```yaml
- { term: sustainable development, gloss: "An ongoing process, aspirational in aim, of tackling social, environmental and economic concerns together for a better world." }
- { term: education for sustainable development, gloss: "Creating curriculum structures, subject content and pedagogy that support and put into practice sustainable development." }
- { term: key competencies for sustainability, gloss: "UNESCO's eight competencies (S4 competency.*), grouped as ways of thinking, practising and being; the base of Table 2's outcomes." }
- { term: learning outcomes, gloss: "What a learner is expected to know, understand or be able to show after a period of learning." }
- { term: synoptic assessment, gloss: "Assessment of a learner's ability to connect different parts of a programme; suited to ESD." }
- { term: wicked problem, gloss: "A problem with no single definition or solution, whose parts are interdependent and keep changing." }
- { term: complex system, gloss: "A system of many interacting parts, such as the climate, an organism or a city." }
- { term: transformative learning, gloss: "Learning that changes how learners see themselves and the world, beyond gaining knowledge and skills." }
- { term: critical pedagogy, gloss: "Teaching that questions inequality and dominant power structures and assumptions." }
- { term: precautionary principle, gloss: "Caution, pause and review before innovations that may cause harm where scientific knowledge is lacking." }
- { term: 4IR technology, gloss: "Technologies linking the physical and digital, such as AI, robotics, 3D printing, VR and AR, cloud computing, big data and the Internet of Things." }
- { term: HEAR, gloss: "The Higher Education Achievement Report: an electronic record of a student's achievement during study." }
- { term: PSRBs, gloss: "Professional, statutory and regulatory bodies." }
- { term: SDGs, gloss: "The UN's 17 Sustainable Development Goals (2015), with 169 targets, for 2030." }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->
None: the guidance sets no process that providers must follow.

## Part D Sources

### D1 Held text
The PDF Abbott supplied (51 pages, sha256-bytes 9463b40b…), not held in UNI. Text by pdftotext page by page, except the pages holding ruled tables (Tables 1, 2 and 3), where each table is linearised row by row and cell by cell with pdfplumber so that each column's items stay together; the vertical labels set in mirror image ("Ways of thinking" and the like) are restored; bullet glyphs are written as bullets. Normalised with stan's normalise.js 1.0 (words equal). Figures 1 to 3 are not cut into statements; Figure 3 is described in our words (GU4) from the page.

### D2 Research log
- 2026-10-03 06:46 to 06:57, std: held and normalised; 207 statements in thirteen families; verb profile; crosswalk; benchmark scan shared with run 0056.

### D3 Wanted sources
- W-std-0009: UNESCO (2017), Education for Sustainable Development Goals: Learning Objectives: the competencies' source, with outcomes for each SDG.
- W-std-0011: UNECE (2012), Learning for the future: competences in ESD: staff competences, a standards document.
- W-std-0012: Advance HE (2019), Framework for Enterprise and Entrepreneurship Education, cited here beside QAA's enterprise guidance.
- W-std-0010: The 2014 QAA and HEA guidance, for the change record.

## Part E Gaps and questions
- E1 Currency unchecked.
- E2 Table 2 is indicative by the guidance's own words; its outcomes are standards statements of what a student can do, not thresholds.
- E3 Some outcomes repeat across competencies (conflict mediation in collaborative and self-awareness; power structures in systems and self-awareness; the range of cultures in self-awareness and normative): kept as separate records, as the guidance places them; a `sameAs` link is a P3 job.
- E4 The verb profile (GU2) and every map are ours.

---

## Change notes
- 0.1.1, 3 October 2026, 07:34: provenance lines added to Parts B and C; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.1.0, 3 October 2026, 06:57: first build, run 0063 (std; Abbott, 06:46: "I do have the full esd. can you redo using this").
'''
