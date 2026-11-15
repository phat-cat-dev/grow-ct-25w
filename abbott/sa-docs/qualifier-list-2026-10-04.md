---
document:  the context qualifier list: pedagogical, thematic and professionally oriented qualifiers
owner:     std (META), compiled on Abbott's direction (4 October 2026, 08:15: "compile this list ... send it over to adapt ... that qualifiers table"); for ADAPT to adopt under its own ids
version:   0.2.0-draft, 4 October 2026, 09:27
supersedes: agt's `threads/agt/mta-agt-td-qualifier-list-draft.md` 0.1.1-draft (its `ped:` list is kept here; its `voc:` and `xct:` groups are replaced)
status:    proposed. 0.2.0: the practice themes come from all eight Advance HE Student Success Frameworks models, merged to one set and aligned across them (tools/practice_themes.json, tools/theme_merges.json); the sector themes take in the series' nine areas. Ids and divisions ruled by Abbott (D-std-0020 and its extension; std N-0126, N-0127, N-0129 to N-0131). Definitions and steers are std's and agt's drafts, unchecked against sources except where marked
---

# Context qualifiers

A qualifier is further context a pack carries beyond its subject and level. It changes how the pack is written and which sources it draws on. ADAPT's Phase D asks for qualifiers at gate four (DQ).

## Gate rules (as ruled)

| Rule | Ruling | Where |
|---|---|---|
| Three categories | pedagogical (`ped:`), thematic (`theme:`), professionally oriented (`pro:`) | Abbott, 05:09, 05:10 (D-std-0020) |
| How many | at most three in all, across the categories | Abbott, 3 October, 00:05 (agt N-0073) |
| Default | none | Abbott, 2 October, 23:37 (agt N-0063) |
| Confirmed | a chosen qualifier is confirmed by the person, never left to stand on silence (CFV-1) | Phase D review, P2 |
| First production round | built in, not used | Abbott, 2 October, 23:37 |
| Overlap | allowed: a qualifier may cross over with another category (employability, enterprise); each points to the other | Abbott, 05:27 |
| Not a qualifier | a direct link to a named assessment task belongs to the institutional path, as a workflow of its own (parked) | Abbott, 05:11 (std N-0128) |

## How to read an entry

Every entry has an id, a label, a one-line definition and a **steer**. The steer is the sentence an author prompt uses as it stands when the qualifier is chosen. **Source** names where the entry comes from, or what to check it against. **Links** name the entries it crosses over with.

Standards measure (quality assurance). Themes and pedagogies move practice forward (quality enhancement) (Abbott, 05:09). The qualifiers are the enhancement side.

## 1. Pedagogical qualifiers (`ped:`)

For teachers who want a pack shaped by a teaching approach. These are from agt's draft, unchanged and still unverified.

| Id | Label | Definition | Steer | Source or check |
|---|---|---|---|---|
| `ped:reflective-practice` | Reflective practice | learning by examining one's own experience and actions to change future practice | Ask the learner to look back on their own practice and draw a next step from it. | INGEST reflective practice runs (Schön, Gibbs, Johns); links `pro:reflexivity` |
| `ped:problem-based` | Problem-based learning | learning driven by open, realistic problems, usually in groups, before formal instruction | Start from a problem the learner must work through before any explanation. | a PBL source (to choose) |
| `ped:enquiry-based` | Enquiry-based learning | learning led by the student's own questions and investigation | Model forming a question and finding out, and let the learner's question lead. | an enquiry-based learning source |
| `ped:project-based` | Project-based learning | learning organised around an extended project with a product at the end | Set each task inside a longer piece of work with a product at the end. | a project-based learning source |
| `ped:case-based` | Case-based learning | learning through analysis of real or realistic cases | Use short cases with a decision in them. | a case-based learning source |
| `ped:experiential` | Experiential learning | learning through a cycle of doing, reflecting, generalising and trying again | Follow the cycle: do, reflect, generalise, try again. | Kolb (INGEST run 0008) |
| `ped:collaborative` | Collaborative learning | shared work with peers towards a common outcome | Build in tasks that need others to complete. | a collaborative learning source |
| `ped:research-informed` | Research-informed teaching | learning that draws on and practises the discipline's research methods | Use real studies and ask the learner to work as a researcher would. | a research-teaching nexus source |
| `ped:flipped` | Flipped learning | content studied before class; class time used for application | Assume prior study and spend the activity on applying it. | a flipped learning source |
| `ped:active` | Active learning | learning by doing tasks in the session rather than listening | Include short tasks the learner does during the session. | an active learning source |

## 2. Thematic qualifiers (`theme:`)

One id space for every cross-cutting theme (Abbott, 05:09: "we will call them themes ... not just QAA themes"). There are two tiers. A sector theme is an agenda named across the sector. A practice theme is a condition for student success, taken from the Advance HE Student Success Frameworks. The tier records where a theme comes from; at the gate the two tiers are offered alike.

### 2a. Sector themes

| Id | Label | Definition | Steer | Source | Links |
|---|---|---|---|---|---|
| `theme:edi` | Equality, diversity and inclusion | treating difference fairly and making learning open to all | Reflect a range of people and voices, and make no assumptions about the learner. | QAA cross-cutting theme; carried in 47 benchmarks; series area (inclusive learning and teaching); Advance HE inclusive model | practice themes below |
| `theme:accessibility` | Accessibility and the needs of disabled students | learning designed so disabled students take part on equal terms | Avoid barriers in tasks and materials, and name alternatives. | QAA cross-cutting theme; 39 benchmarks (no QAA guidance text held) | `theme:anticipating-difference` |
| `theme:esd` | Education for sustainable development | understanding and acting on environmental, social and economic sustainability | Connect the skill to a sustainability question in the subject. | QAA and Advance HE ESD guidance 2021 (ingested); 57 benchmarks | |
| `theme:enterprise` | Enterprise and entrepreneurship | generating ideas and acting on them to create value, in business or elsewhere | Include spotting an opportunity and acting on it. | QAA guidance 2018 (ingested); 52 benchmarks | `pro:` (crossover, Abbott 05:27) |
| `theme:generative-ai` | Generative AI | using, judging and acknowledging generative AI tools in study and practice | Show where AI tools help, where they mislead, and how their use is acknowledged. | 22 benchmarks; not a QAA theme. `theme:genai` (17 records) merges into this id | `theme:digital` |
| `theme:internationalisation` | Internationalisation and global citizenship | learning that draws on more than one culture and on global questions | Draw on more than one country or culture, and on a global question in the subject. | Advance HE internationalising model (held); 10 benchmark mentions | `theme:intercultural-engagement` |
| `theme:employability` | Employability | the skills and awareness that help a graduate gain and succeed in work | Connect the skill to work and to how the learner can show it. | Advance HE access model (progression); 2 benchmark mentions | `pro:` (crossover, Abbott 05:27) |
| `theme:access-retention-attainment-progression` | Access, retention, attainment and progression | the stages of a student's journey into, through and beyond study | Say where in the journey the learner is, and what support fits that stage. | series area; Advance HE access model (ingested) | `theme:transition` |
| `theme:assessment` | Assessment and feedback | assessment designed and used so that students learn and are judged fairly | Say how the task will be judged and how feedback will help the learner improve. | series area; Advance HE assessment model (ingested) | `theme:assessment-literacy`, `theme:feedback-dialogue` |
| `theme:student-partnership` | Student engagement through partnership | open, continuing dialogue and shared work between students, staff and students' unions | Invite the learner to shape part of the task or its criteria, and say how their input will be used. | series area; model not held (wanted) | `theme:student-voice-partnership` |
| `theme:flexible-learning` | Flexible learning | technologies, spaces and policies that let students choose how, what, when and where they learn | Offer a choice of route, pace or format, and say what stays fixed. | series area; model not held (wanted) | `theme:flexibility` |
| `theme:digital` | Digital capability | the confident, critical and safe use of digital tools and information | Use digital tools and ask the learner to judge digital information. | Jisc digital capability framework (to check) | `theme:generative-ai` |
| `theme:decolonising` | Decolonising the curriculum | examining whose knowledge a subject centres, and widening it | Widen examples and sources beyond the usual canon, and ask whose view is missing. | a decolonising source (to choose); 1 benchmark mention | `theme:student-voice-partnership` |
| `theme:welsh` | Welsh language and bilingual learning | learning through or alongside Welsh | Respect bilingual study, and give key terms in both languages where useful. | Coleg Cymraeg Cenedlaethol guidance (to check); CQFW | |
| `theme:wellbeing` | Wellbeing and mental health | conditions that support students' mental and physical health in study | Set a manageable pace, and point to support without making it the subject. | Advance HE access model (retention) | `theme:psychological-safety` |

### 2b. Practice themes

The conditions for student success, from the eight Advance HE Student Success Frameworks models (`std:doc:advancehe-*-2024-model`, 189 components). The ids are merged across the series: the old ids in the last column are aliases (`designs/ingest/standards/tools/theme_merges.json`), and the definitions are the shared register's (`tools/practice_themes.json` 0.1.0), which every model's M6 now uses. Each steer is an example, written for one model's component and named for that model's topic; a generic steer for each theme is still to write (Open, 1). "Carried by" counts components per model.

| Id | Label | Definition | Example steer (from a model) | Carried by | Aliases |
|---|---|---|---|---|---|
| `theme:transition` | Transition | students are prepared and supported as they move into, through and on from study | Write for a reader who may be the first in their circle to consider university, and explain what others take for granted. | internationalising 2, access 12, employability 1, assessment 1, overview 1 |  |
| `theme:evidence-informed-enhancement` | Evidence-informed enhancement | practice is mapped, its effects are evaluated and it is improved on that evidence | Say which sustainability competency the activity builds, so that it can be placed on a course map. | internationalising 2, ESD 3, employability 1, enterprise 6, overview 4 | `theme:evidence-informed-practice`, `theme:data-informed-practice`, `theme:review-and-improvement`, `theme:informed-practice` |
| `theme:agency-self-actualisation` | Agency and self-actualisation | people grow into, use and trust their own judgement | Ask the learner to make and justify a judgement of their own, and treat a reasoned answer as valuable even where others are possible. | inclusive 2, access 3, ESD 1, employability 4, assessment 1, enterprise 1, overview 2 |  |
| `theme:whole-institution` | Whole-institution approach | the institution's strategy, quality processes, estate and staff pull together towards one aim | State plainly where sustainability sits in the course's aims and outcomes, so the material can be traced to them. | internationalising 5, access 3, ESD 2, employability 1, overview 3 | `theme:whole-institution-approach`, `theme:shared-commitment`, `theme:shared-responsibility`, `theme:strategic-leadership` |
| `theme:collaboration` | Collaboration | learning and problem-solving are done with others, across subjects, professions and sectors | Bring in at least one perspective from another subject or profession and show how it changes the problem. | ESD 5, employability 3, assessment 3, enterprise 3 | `theme:collaborative-engagement`, `theme:partnership-working`, `theme:collaborative-learning` |
| `theme:belonging-mattering` | Belonging and mattering | students see that their experience and needs count | Address the learner as someone whose experience counts, and invite them to bring it into the task. | inclusive 1, internationalising 2, access 9, overview 1 |  |
| `theme:career-development` | Career development | students learn to explore, decide and manage their own paths and professional identity | Invite the learner to connect the topic to options they might pursue, and to plan a next step. | access 9, employability 2 | `theme:career-readiness` |
| `theme:anticipating-difference` | Anticipating difference | teaching is designed in advance for the range of students | Make unspoken expectations explicit, offer more than one way in, and avoid assuming what the learner already knows. | inclusive 1, internationalising 1, access 4, employability 1, assessment 2, overview 1 |  |
| `theme:student-voice-partnership` | Student voice and partnership | a range of voices, students' included, shapes decisions and is answered | Bring in more than one perspective on the topic, including views from outside the mainstream, and ask the learner whose view is missing. | inclusive 1, access 1, ESD 1, employability 1, assessment 2, overview 2 |  |
| `theme:feedback-dialogue` | Feedback dialogue | feedback is timely, usable, two-way and acted on | Before asking the learner to review a peer's work, give them the criteria, an example and a frame for their comments. | assessment 8 |  |
| `theme:authenticity` | Authenticity | learners bring who they are, and that is treated as an asset | Invite the learner to draw on their own experience and ways of working, and value what they bring. | inclusive 1, internationalising 1, access 4, ESD 1 |  |
| `theme:interconnectivity` | Interconnectivity | work in one area, discipline or place is linked to others | Point out where the topic links to another subject or area, and invite the learner to make the connection. | internationalising 4, ESD 1, overview 2 | `theme:global-connectedness`, `theme:connected-curriculum` |
| `theme:real-world-learning` | Real-world learning | learning, assessment and settings are modelled on real practice | Set the task in a real or realistic work situation, and ask the learner what it shows about the subject. | employability 3, assessment 4 | `theme:authentic-assessment` |
| `theme:enterprising-capability` | Enterprising capability | learners build and practise the skills of turning ideas into value | Ask the learner to find a real need or opening and to judge whether it is worth pursuing, with reasons. | enterprise 7 |  |
| `theme:compassion` | Compassion | decisions and teaching shaped by care for the person affected | Write with warmth and without blame: acknowledge that circumstances differ, and show where help or discretion can be sought. | inclusive 2, access 3, employability 1 |  |
| `theme:contextual-adaptation` | Contextual adaptation | practice adapts to the setting and its students, not the reverse | Offer more than one way to reach the same aim, and make clear which parts are fixed and which can change. | inclusive 1, access 3, assessment 1, overview 1 |  |
| `theme:hidden-curriculum` | Hidden curriculum | the unwritten rules of study are made explicit | Make explicit what the learner is expected to learn beyond the content itself, including how to go about it. | inclusive 1, internationalising 1, access 2, employability 1, overview 1 |  |
| `theme:targeted-support` | Targeted support | help reaches the students who need it, early and before difficulty grows | Where cost may matter to the learner, say plainly that financial help exists and where to ask about it. | access 6 |  |
| `theme:assessment-literacy` | Assessment literacy | staff and students share an understanding of criteria, standards and how work is judged | State the criteria for the task plainly at the start and show what meeting each one looks like. | assessment 6 |  |
| `theme:critical-thinking` | Critical thinking | questioning and evaluating are practised and valued | Include at least one point where the learner questions a claim, weighs evidence and states a reasoned view. | inclusive 2, ESD 1, enterprise 2 |  |
| `theme:intercultural-engagement` | Intercultural engagement | people from different cultures meet, work together and learn from each other | Build in a point where the learner seeks out and uses a perspective from a culture other than their own. | internationalising 3, ESD 1, overview 1 |  |
| `theme:consistent-judgement` | Consistent judgement | assessment judgements are consistent, calibrated and fair across markers, modules and groups | Use the same standard throughout the material and say plainly what each level of work looks like. | assessment 5 |  |
| `theme:programmatic-assessment` | Programmatic assessment | assessment is planned across a whole programme so that tasks connect, balance and build | Connect the criteria here to those the learner has met before and to what comes next. | assessment 5 |  |
| `theme:structural-challenge` | Structural challenge | structures that exclude can be questioned and are changed | Invite the learner to ask why a convention exists and whom it serves, and treat that question as part of the learning. | inclusive 2, internationalising 1 |  |
| `theme:global-citizenship` | Global citizenship | learners prepare to act responsibly on shared global challenges | Connect the topic to a global challenge and ask the learner what a responsible response would be. | internationalising 1, overview 2 | `theme:social-responsibility` |
| `theme:professional-learning` | Professional learning | staff are given time, support and recognition to develop their practice | Give worked examples from the subject so that a reader new to sustainability can see how it applies. | ESD 1, assessment 2 | `theme:professional-development` |
| `theme:systems-futures-thinking` | Systems and futures thinking | problems are seen as connected systems and judged against possible futures | Include a perspective from another part of the world and ask the learner how the issue may change over time. | ESD 2, employability 1 | `theme:sustainable-futures` |
| `theme:graduate-attributes` | Graduate attributes | personal qualities, values and interpersonal abilities are developed, shown and carried across settings | Invite the learner to notice how they and others feel in the situation and how that shapes what happens. | employability 3 | `theme:transferable-learning` |
| `theme:entrepreneurial-mindset` | Entrepreneurial mindset | learners come to see themselves as able to act on ideas, and learn from setbacks | Use examples the learner can relate to, and frame being enterprising as open to them. | enterprise 2, overview 1 | `theme:enterprising-mindset` |
| `theme:equitable-participation` | Equitable participation | every student, and member of staff, can take part fully and on fair terms | Assume no shared starting point: explain what others may take for granted and show the way through each stage. | overview 3 |  |
| `theme:psychological-safety` | Psychological safety | speaking, asking, disagreeing and erring carry no penalty | Frame mistakes and questions as expected, invite the learner's own experience, and allow for disagreement. | inclusive 1, assessment 1 |  |
| `theme:community-engagement` | Community engagement | learning connects with communities, employers and partners beyond the institution | Set the task in a real setting with a named kind of partner and their constraints, rather than in the abstract. | ESD 2 |  |
| `theme:action-competence` | Action competence | learners turn understanding into action and judge its effects | Close with a concrete action the learner could take, and ask how they would know it had worked. | ESD 2 |  |
| `theme:flexibility` | Flexibility | learners choose how, what, when and where they learn, with tools, spaces and rules that allow it | Offer the learner a choice of route, pace or format, and make clear what stays fixed. | overview 2 |  |
| `theme:embedded-practice` | Embedded practice | an aim is built into curriculum, teaching and assessment, not added on | Make the international dimension part of what the learner does and is judged on, not a side example. | internationalising 1 |  |
| `theme:values-reflection` | Values reflection | learners examine how their values and experiences shape their judgements and actions | Ask the learner what values or experiences lead them to their view, without judging the answer. | ESD 1 |  |
| `theme:shared-language` | Shared language | key terms are defined, agreed and used the same way by everyone involved | Say which of the two you mean, enterprise or entrepreneurship, and keep to that meaning throughout the material. | enterprise 1 |  |
| `theme:entrepreneurial-pedagogy` | Entrepreneurial pedagogy | teaching methods and assessment match whether learners study, prepare for or do enterprise | Make clear whether the learner is studying enterprise, preparing for it or doing it, and match the task to that. | enterprise 1 |  |
| `theme:assessment-for-learning` | Assessment for learning | assessment and its feedback are designed so that students learn through them | Build in a chance to practise and get feedback before anything is judged, and say how the task helps the learner learn. | overview 1 |  |

## 3. Professionally oriented qualifiers (`pro:`)

For professional and disciplinary practice (Abbott, 05:10 to 05:32). This covers work-based learning, apprenticeships, vocational courses, professional practitioners, professional values, identity and reflexivity, and the settings where a discipline is practised. It crosses over with `theme:employability` and `theme:enterprise`; each entry points to the other (Abbott, 05:27).

| Id | Label | Definition | Steer | Source or check | Links |
|---|---|---|---|---|---|
| `pro:work-based` | Work-based learning | learning that takes place in, or is designed around, the student's workplace | Set examples in the learner's workplace and use its tasks. | QAA, Advance HE work-based learning (to check) | `theme:employability` |
| `pro:degree-apprenticeship` | Degree apprenticeship | a degree studied while employed, learning in work and at university | Tie academic work to the employer's setting and the apprenticeship standard. | Skills England apprenticeship standards | `pro:work-based` |
| `pro:placement` | Placement learning | a period of supervised work as part of the course | Refer to the placement and to how the learner records learning from it. | QAA placement learning (to check) | `theme:employability` |
| `pro:vocational` | Vocational course | a course preparing students for a named occupation | Use the occupation's tasks, tools and language. | to check | `pro:professional-practice` |
| `pro:psrb-accredited` | Accredited by a professional body | the course meets a professional, statutory or regulatory body's requirements | Stay within the body's requirements and name them where they apply. | the body's own requirements | `pro:professional-values` |
| `pro:cpd` | Continuing professional development | learning by people already in practice, to keep or extend their competence | Assume practising learners, and draw on their own work. | the relevant body's CPD framework; PSF 2023 for teaching staff | `pro:reflexivity` |
| `pro:professional-practice` | Professional practice | the conduct and work of a profession the course leads to | Use the profession's settings, language and expectations. | the relevant professional body | `theme:employability` |
| `pro:professional-values` | Professional values | the values and conduct a profession expects of its members | Name the value at stake and ask how a practitioner would act on it. | professional codes; PSF 2023 V1 to V5 for teaching staff | `pro:professional-identity` |
| `pro:professional-identity` | Professional identity | who a person becomes as a practitioner | Ask the learner how the task shapes them as a practitioner. | Shulman (2005), wanted (W-std-0109) | equivalent: `pro:reflexivity`; `pro:disciplinary-identity` |
| `pro:disciplinary-identity` | Disciplinary identity | learning to think and work as a member of the discipline does (a chemist, a historian, a designer) | Model how someone in the discipline would approach the task, and ask the learner to try it. | Shulman (2005), wanted (W-std-0109) | `pro:professional-identity` |
| `pro:reflexivity` | Reflexivity | examining one's own position, values and assumptions as a practitioner | Ask the learner what they bring to the situation and how it shapes their judgement. | Finlay (2002), ing run 0054 | equivalent: `pro:professional-identity`; `ped:reflective-practice` |
| `pro:lab` | Laboratory setting | practice in a laboratory | Frame tasks around method, safety and recording results. | Shulman (2005), signature pedagogies (wanted) | `pro:disciplinary-identity` |
| `pro:studio` | Studio setting | practice in a studio, through making and critique | Frame tasks around making, iterating and critique. | as above | `pro:disciplinary-identity` |
| `pro:fieldwork` | Fieldwork setting | practice in the field, away from the institution | Frame tasks around planning, observation, safety and records made on site. | as above | `pro:disciplinary-identity` |
| `pro:clinical` | Clinical setting | practice with patients or service users, under supervision | Frame tasks around safe, supervised practice, consent and professional conduct. | as above; the relevant regulator | `pro:professional-values` |
| `pro:workshop` | Workshop setting | practice with tools, equipment and materials | Frame tasks around correct use of tools, safety and quality of the product. | as above | `pro:vocational` |

## Counts

| Category | Entries | Status |
|---|---|---|
| `ped:` | 10 | agt's draft, unverified |
| `theme:` sector | 15 | the QAA four checked against the benchmarks; the series' nine areas from the overview model; the rest proposed |
| `theme:` practice | 39 | from the eight ingested models, merged from 59 |
| `pro:` | 16 | proposed; ruled as a category |
| **All** | **80** | |

## Open

1. **Steers are drafts.** Each still needs checking against its source. The practice steers are examples from the models' M3; a generic steer per practice theme is to write before the gate uses them.
2. **Tagging our documents** with `theme:` ids (Abbott, 05:09: "tag all our various documents with them") is next for std. It starts with the shared theme register (this list's `theme:` rows, with definitions) and the merge of `theme:genai` into `theme:generative-ai`.
3. **The Advance HE series** has nine areas (the overview model). Eight models are held and ingested; Student Engagement through Partnership and Flexible Learning in HE are wanted. Each adds practice themes.
4. **The direct assessment context workflow** is parked for the institutional path (std N-0128).

## Change notes
- 0.2.0-draft, 4 October 2026, 09:27: practice themes from all eight series models (39, merged from 59, with aliases), definitions from the shared register; sector themes add the series' nine areas (`theme:assessment`, `theme:student-partnership`, `theme:flexible-learning`; `theme:student-success` becomes `theme:access-retention-attainment-progression`); 80 qualifiers (Abbott, 09:08).
- 0.1.0-draft, 4 October 2026, 08:16: first compiled from Abbott's rulings of 05:02 to 05:32 (D-std-0020; std N-0124 to N-0131), agt's draft 0.1.1 (`ped:` kept) and the inclusive model 0.1.0 (practice steers); for ADAPT (Abbott, 08:15).
