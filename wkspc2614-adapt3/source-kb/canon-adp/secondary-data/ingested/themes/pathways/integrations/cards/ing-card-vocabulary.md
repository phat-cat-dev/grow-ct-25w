---
document:  ing: capability card vocabulary
owner:     adp ing
version:   0.1.2, 4 October 2026, 10:53, D-ing-0058 note (ing N-0120); 0.1.1, 4 October 2026, 08:51, moved to `integrations/cards/` (ing N-0111); 0.1.0, 4 October 2026, 08:48 (ing N-0110)
status:    working draft; an integration: the cards speak to the library ingestion documents (the pathway cores) and are not part of them (Abbott, 08:51); feeds the card enrichment (ing N-0106) and the practice searcher (J-ing-0003)
sources:   the 62 draft cards and draft book map of `mta-nts-ho-adp-nts-0007` (adp-0212), with their benchmark evidence; the 26 cards added by the model's author in the ing cores (A10); tier notes from the cores, and for the three undrafted pathways from `adp-relay/threads/prm/reviews/adp-0213-tier-notes.json`
data:      `ing-card-vocabulary.json` beside this file
---

# Capability card vocabulary

> [4 October 2026, 10:53, D-ing-0058] Every verb here is captured with its statement: the card's own statement for these verbs; benchmark and other statements, with their subject and relation, go in `verbs-in-context.json`.

For each card: its **verbs** (what the learner does), its **measures** (the words that say how well, how or under what condition), and its **keywords** (the statement's terms, then the guide's own topic terms under the card, merged). Extraction by ing from the statement text, not by script; keywords from the book are adp-0212's draft book map, not re-checked. Benchmark hits are adp-0212's counts (passages / texts, of 54), found by a phrase search that runs loose on common words; cards added since have none.

## Coverage

88 cards across all 13 pathways: 62 drafted by adp-0212, 26 added by the model's author since. Every pathway has cards. By tier:

| Pathway | Cards | Intro | Inter | Adv | Gap |
|---|---|---|---|---|---|
| Starting, Progressing and Succeeding | 7 | 2 | 3 | 2 | - |
| Understanding Learning, Assessment and Feedback | 9 | 3 | 3 | 3 | - |
| Finding and Using Sources | 5 | 2 | 1 | 2 | - |
| Referencing | 7 | 3 | 2 | 2 | - |
| Criticality | 7 | 2 | 3 | 2 | - |
| Academic Writing | 8 | 3 | 4 | 1 | - |
| Presenting | 7 | 1 | 4 | 2 | - |
| Revising and Exams | 4 | 1 | 0 | 3 | Inter |
| Researching and Research Methods | 6 | 1 | 2 | 3 | - |
| Reflective Practice | 9 | 2 | 4 | 3 | - |
| Work-Based and Experiential Learning | 6 | 1 | 3 | 2 | - |
| AI and Technology | 6 | 0 | 3 | 2 | Intro, 1 unplaced |
| Creativity | 7 | 2 | 4 | 1 | - |

Two tier gaps: Revising and Exams has no Intermediate card; AI and Technology has no Introductory card, and its `/04` describes the pathway's design, not a skill. Both are undrafted pathways (queue rows 11 and 12); their cards are adp-0212's drafts only.

## Tally

**Verbs** (cards using each):

use 13, apply 12, reflect 5, recognise 4, distinguish 4, plan 4, write 4, justify 4, exercise 4, manage 3, follow 3, structure 3, build 2, sustain 2, interpret 2, engage 2, turn 2, adapt 2, evaluate 2, construct 2, avoid 2, uphold 2, identify 2, present 2, choose 2, treat 2, adopt 1, set 1, articulate 1, develop 1, own 1, direct 1, understand 1, differentiate 1, assess 1, locate 1, extend 1, explain 1, record 1, organise 1, show 1, map 1, question 1, analyse 1, synthesise 1, form 1, vary 1, correct 1, complete 1, integrate 1, put 1, design 1, open 1, work 1, resolve 1, defend 1, prepare 1, convert 1, deepen 1, formulate 1, scope 1, answer 1, describe 1, take action 1, balance 1, support 1, amend 1, examine 1, shape 1, make use 1, conduct oneself 1, test 1, decide 1, cite 1, progress 1, weigh 1, relate 1, overcome 1, draw on 1

**Measures** (cards using each):

professional 6, scholarly 4, critically 4, effective 4, active 3, critical 3, passive 2, independent 2, different 2, effectively 2, structured 2, creative 2, under academic pressure 1, mastery-oriented 1, personal 1, within its conventions 1, independently 1, constructivist 1, intended 1, aligned 1, formative 1, summative 1, varied 1, self-regulated 1, for improvement 1, against marking criteria 1, diagnostically 1, in dialogue 1, across a degree 1, against criteria 1, supplementary 1, staged 1, accurate 1, consistent 1, correctly 1, as they are found 1, traceable 1, discipline-specific 1, relative importance 1, by discipline 1, clear 1, before writing 1, common 1, first 1, actively 1, one's own point first 1, accessible 1, engagingly 1, to a brief 1, under questioning 1, organised 1, visual 1, kinaesthetic 1, time-managed 1, targeted 1, across question formats 1, extended 1, dissertation-length 1, each of its questions 1, for a research question 1, positive 1, negative 1, continuing 1, lifelong 1, not working 1, rather than describing 1, dated 1, fuller 1, assessed 1, own 1, in report format 1, experiential 1, in a work-based setting 1, in a practice setting 1, informed 1, justified 1, when, and when not 1, never 1, cross-cutting 1, environmental 1, permitted 1, unfair 1, developable 1, cross-disciplinary 1, at the right stage 1, when a strategy is not working 1, entrepreneurial 1, established 1

**Keywords:** 351 distinct, 25 on more than one card, 9 shared across pathways:

sources (Academic Writing, Criticality, Finding and Using Sources, Referencing), academic voice (Presenting, Starting, Progressing and Succeeding), practice (Starting, Progressing and Succeeding, Work-Based and Experiential Learning), discipline (Academic Writing, Understanding Learning, Assessment and Feedback), action plan (Reflective Practice, Understanding Learning, Assessment and Feedback), keywords (Academic Writing, Finding and Using Sources), critical thinking (Creativity, Criticality), methodology (Criticality, Researching and Research Methods), methods (Creativity, Researching and Research Methods)

The vocabulary is almost wholly pathway-specific: few keywords recur, and those that cross pathways mark the joins (sources, academic voice, action plan, critical thinking, methodology).

## Starting, Progressing and Succeeding

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Intro | Adopt a growth mindset towards academic challenge | adopt | - | growth mindset; academic challenge; fixed mindset | 87 / 38 |
| `02` | Inter | Build self-efficacy and manage stress or anxiety under academic pressure | build, manage | under academic pressure | self-efficacy; stress; anxiety; managing stress and anxiety | 9 / 6 |
| `03` | Inter | Set and sustain mastery-oriented academic goals | set, sustain | mastery-oriented | academic goals; mastery; mastery goals; performance goals; achievable goal-setting | 54 / 36 |
| `04` | Adv | Articulate personal graduate capital for the transition from student to graduate | articulate | personal | graduate capital; transition; student to graduate; graduate identity; graduate capital framework; human capital; social capital; cultural capital; identity capital; psychological capital; transition from student to graduate | 229 / 53 |
| `c1` | Intro | Recognise and follow the conventions of academic practice. | recognise, follow | - | conventions of academic practice; academic practice | (added; not searched) |
| `c2` | Inter | Develop an academic voice, and the confidence and sense of capability to own one's practice within its conventions. | develop, own | within its conventions | academic voice; confidence; sense of capability; practice; conventions | (added; not searched) |
| `c3` | Adv | Direct one's own academic practice, learning and development independently, as a lifelong learner. | direct | independently | academic practice; learning and development; lifelong learner | (added; not searched) |

## Understanding Learning, Assessment and Feedback

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Intro | Understand how academic learning operates within a discipline's discourse community | understand | - | academic learning; discipline; discourse community | 4 / 4 |
| `02` | Intro | Distinguish active, constructivist learning from passive reception of knowledge | distinguish | active, constructivist, passive | constructivist learning; passive reception; knowledge; active learning; passive learning | 24 / 19 |
| `03` | Inter | Interpret intended learning outcomes and how learning activities are aligned to them | interpret | intended, aligned | intended learning outcomes; learning activities; constructive alignment | 244 / 51 |
| `04` | Intro | Differentiate formative from summative assessment and engage with varied assessment forms | differentiate, engage | formative, summative, varied | formative assessment; summative assessment; assessment forms; marking criteria; self and peer assessment | 86 / 43 |
| `05` | Inter | Apply self-regulated learning cycles to independent study | apply | self-regulated, independent | self-regulated learning cycle; independent study; self-regulated learning; forethought phase; evaluation phase | 53 / 36 |
| `06` | Inter | Use reflective practice to turn feedback into an action plan for improvement | use, turn | for improvement | reflective practice; feedback; action plan; feedback cycle; action plan from reflection | 1 / 1 |
| `c1` | Adv | Assess one's own and peers' work against marking criteria. | assess | against marking criteria | own work; peers' work; marking criteria; self-assessment; peer assessment | (added; not searched) |
| `c2` | Adv | Use feedback diagnostically and in dialogue with tutors to sustain development across a degree. | use, sustain | diagnostically, in dialogue, across a degree | feedback; dialogue with tutors; development | (added; not searched) |
| `c3` | Adv | Adapt to the demands of different types of assessment. | adapt | different | types of assessment; assessment demands | (added; not searched) |

## Finding and Using Sources

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Inter | Plan a search strategy using keywords and Boolean operators | plan | - | search strategy; keywords; Boolean operators; keyword selection; search limiters | 16 / 12 |
| `02` | Intro | Use library and discovery services effectively to locate scholarly sources | use, locate | effectively, scholarly | library; discovery service; scholarly sources; library discovery service | 78 / 23 |
| `03` | Adv | Evaluate sources against currency, authority and relevance criteria | evaluate | against criteria | sources; currency; authority; relevance; evaluation criteria; evaluative criteria for sources; currency of a source; authority of a source; relevance of a source | 20 / 15 |
| `04` | Adv | Extend a search via citation searching and supplementary scholarly tools | extend | supplementary, scholarly | search; citation searching; scholarly tools; extending searches via google scholar | 6 / 3 |
| `c1` | Intro | Follow a staged search strategy, starting from the reading list and what one already knows. | follow | staged | search strategy; reading list; prior knowledge | (added; not searched) |

## Referencing

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Intro | Construct accurate in-text citations and a references list in a consistent style | construct | accurate, consistent | in-text citation; references list; referencing style; in-text references; author-date/harvard referencing style | 1 / 1 |
| `02` | Inter | Avoid plagiarism by distinguishing and correctly using quotation and paraphrase | avoid, distinguish, use | correctly | plagiarism; quotation; paraphrase | 8 / 8 |
| `03` | Adv | Uphold honesty and trust in academic work | uphold | - | honesty; trust; academic work; academic integrity | 38 / 24 |
| `04` | Adv | Uphold fairness, respect, responsibility and courage in academic conduct | uphold | - | fairness; respect; responsibility; courage; academic conduct | 3 / 3 |
| `c1` | Intro | Explain why academic work acknowledges the sources of its knowledge. | explain | - | academic work; acknowledgement; sources of knowledge | (added; not searched) |
| `c2` | Intro | Record and organise sources as they are found, so that every citation can be traced. | record, organise | as they are found, traceable | sources; citation; source management | (added; not searched) |
| `c3` | Inter | Use citation to show the scope of research and engagement with the discourse. | use, show | - | citation; scope of research; engagement with the discourse | (added; not searched) |

## Criticality

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Inter | Recognise critical thinking skills of analysis and evaluation | recognise | critical | critical thinking; analysis; evaluation | 866 / 54 |
| `02` | Intro | Map and question the scholarly discourse around a topic | map, question | scholarly | scholarly discourse; topic; mapping the discourse | 3 / 3 |
| `03` | Inter | Analyse and evaluate a scholarly interpretation critically | analyse, evaluate | critically, scholarly | scholarly interpretation; evaluative question steers | 121 / 47 |
| `04` | Inter | Critically engage with a journal article's structure and methodology | engage | critically | journal article; structure; methodology; journal article structure | 9 / 8 |
| `05` | Adv | Write critically, synthesising sources using discipline-specific vocabulary | write, synthesise, use | critically, discipline-specific | synthesis; sources; discipline-specific vocabulary; language of criticality; critical edge; active and passive engagement with discourse | 137 / 49 |
| `c1` | Intro | Apply critical thought to the choices made when searching, reading and planning. | apply | critical | critical thought; searching; reading; planning | (added; not searched) |
| `c2` | Adv | Form and justify judgements on the relative importance of factors. | form, justify | relative importance | judgement; factors | (added; not searched) |

## Academic Writing

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Adv | Recognise how writing conventions vary by discipline | recognise, vary | by discipline | writing conventions; discipline; discipline writing exemplars | 1 / 1 |
| `02` | Inter | Identify and structure the genres of academic writing | identify, structure | - | genres of academic writing; academic writing; reflective writing as a genre | 5 / 5 |
| `03` | Inter | Apply the pillars of effective writing to structure paragraphs and essays | apply, structure | effective | pillars of effective writing; paragraphs; essays; topic sentence; four pillars of effective writing; essay structure as paragraph microcosm | 10 / 7 |
| `04` | Inter | Construct clear sentences using active voice and effective sentence structure | construct, use | clear, active, effective | sentences; active voice; sentence structure; svo model for sentence structure; active versus passive voice | 2 / 2 |
| `05` | Intro | Interpret an assessment question's steer and keywords before writing | interpret | before writing | assessment question; steer; keywords; writing cycle; the steer and keywords | 21 / 17 |
| `06` | Intro | Identify and correct common writing errors through proofreading and editing | identify, correct | common | writing errors; proofreading; editing; comma splice; proofreading versus editing | 2 / 2 |
| `c1` | Intro | Follow the writing cycle to plan and complete a first draft. | follow, plan, complete | first | writing cycle; first draft | (added; not searched) |
| `c2` | Inter | Integrate sources actively, putting one's own point first and using sources to support it. | integrate, put, use | actively, one's own point first | sources; own point; support | (added; not searched) |

## Presenting

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Inter | Plan and design an effective, accessible presentation using visual aids | plan, design, use | effective, accessible | presentation; visual aids; accessibility; 'less is more' visual aid design; accessibility of presented content | 13 / 12 |
| `02` | Inter | Open a presentation engagingly and manage presentation nerves | open, manage | engagingly | presentation; presentation nerves; hook; presentation hook; managing presentation nerves | none found |
| `03` | Inter | Adapt presentation delivery to different assessment formats | adapt | different | presentation delivery; assessment formats; poster presentations; professional/practice-based presentations; interview-based presentations; technology-based presentations | 35 / 26 |
| `04` | Adv | Work effectively in a group, exercising leadership and resolving conflict | work, exercise, resolve | effectively | group work; leadership; conflict; ocean personality model; leadership in group work; conflict resolution in group work | 494 / 54 |
| `c1` | Intro | Build a presentation to a brief through the five steps, with a hook, a main body and a conclusion. | build | to a brief | presentation; brief; five steps; hook; main body; conclusion | (added; not searched) |
| `c2` | Inter | Present and defend an argument with an academic voice under questioning. | present, defend | under questioning | argument; academic voice; questioning | (added; not searched) |
| `c3` | Adv | Present in professional formats: the pitch, the conference poster and the viva-style interview. | present | professional | professional formats; pitch; conference poster; viva-style interview | (added; not searched) |

## Revising and Exams

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Intro | Manage exam anxiety and prepare for exams in an organised way | manage, prepare | organised | exam anxiety; exams; exam preparation | 2 / 1 |
| `02` | Adv | Convert passive revision into active visual revision techniques | convert | passive, active, visual | revision; revision techniques; visual revision; passive-to-active revision; mind mapping; flashcards; visual mnemonics | 2 / 2 |
| `03` | Adv | Use kinaesthetic and role-play revision techniques to deepen engagement with content | use, deepen | kinaesthetic | role-play; revision techniques; engagement with content; kinaesthetic revision techniques; role-playing as a revision technique | 21 / 18 |
| `04` | Adv | Apply time-managed, targeted revision and exam strategy across question formats | apply | time-managed, targeted, across question formats | revision; exam strategy; question formats; multiple-choice question exams; time management under exam conditions; targeted revision | 23 / 20 |

## Researching and Research Methods

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Intro | Formulate a research question, rationale, and aims for a research proposal | formulate | - | research question; rationale; aims; research proposal; research rationale; aims and objectives; indicative bibliography | 31 / 21 |
| `02` | Inter | Structure and write a literature review and a research report | structure, write | - | literature review; research report; report structure | 9 / 7 |
| `03` | Adv | Apply research ethics principles including informed consent and anonymisation | apply | - | research ethics; informed consent; anonymisation; esrc research ethics principles; participant consent; anonymising participants | 8 / 6 |
| `04` | Adv | Plan and scope an extended dissertation-length research project | plan, scope | extended, dissertation-length | research project; dissertation; dissertation as extended research project | 84 / 46 |
| `c1` | Inter | Write a research proposal that answers each of its questions. | write, answer | each of its questions | research proposal | (added; not searched) |
| `c2` | Adv | Choose and justify a methodology and methods of data collection and analysis for a research question. | choose, justify | for a research question | methodology; methods; data collection; data analysis; research question | (added; not searched) |

## Reflective Practice

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Intro | Apply a structured reflective cycle (describe, reflect, take action) to a learning experience | apply, describe, reflect, take action | structured | reflective cycle; learning experience; three-stage reflective cycle; the describe stage; the reflect stage; the take-action stage | 56 / 31 |
| `02` | Intro | Balance positive and negative observations when reflecting on performance | balance, reflect | positive, negative | observations; performance; positives-before-negatives principle | 3 / 3 |
| `03` | Adv | Use reflective writing to support continuing professional development and lifelong learning | use, support | continuing, lifelong | reflective writing; continuing professional development; lifelong learning; lifelong learner identity; reflective journals as formative assessment | 90 / 42 |
| `04` | Inter | Reflect on motivation and amend learning strategies that are not working | reflect, amend | not working | motivation; learning strategies; reflecting on motivation; monitoring and amending strategies | none found |
| `c1` | Inter | Reflect critically on own performance rather than describing it. | reflect | critically, rather than describing | critical reflection; own performance; description | (added; not searched) |
| `c2` | Inter | Turn reflection into a dated action plan. | turn | dated | reflection; action plan | (added; not searched) |
| `c3` | Adv | Choose and apply a fuller reflective model (Gibbs, Kolb, Johns) to an assessed reflection. | choose, apply | fuller, assessed | reflective model; Gibbs; Kolb; Johns; assessed reflection | (added; not searched) |
| `c4` | Adv | Examine how own personal identity, values, assumptions and social position shape own reflections, judgements and actions (reflexivity). | examine, shape | own | personal identity; values; assumptions; social position; judgements; reflexivity | (added; not searched) |
| `c5` | Inter | Write a professional-practice reflective report in report format. | write | professional, in report format | professional practice; reflective report; report format | (added; not searched) |

## Work-Based and Experiential Learning

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Intro | Distinguish types of practice- and work-based learning | distinguish | - | practice-based learning; work-based learning; defining practice- and work-based learning; laboratory work; simulation-based training; industry placements and internships; apprenticeships | 364 / 54 |
| `02` | Inter | Make effective use of a mentoring relationship while on placement | make use | effective | mentoring relationship; placement; the student-mentor relationship | 30 / 19 |
| `03` | Adv | Apply an experiential learning cycle to work-based learning | apply | experiential | experiential learning cycle; work-based learning; kolb's experiential learning cycle; the experiencing stage; the reflecting stage; the thinking stage; the acting stage | 57 / 31 |
| `04` | Adv | Exercise professional judgement and justify decision-making in a work-based setting | exercise, justify | professional, in a work-based setting | professional judgement; decision-making; professional judgement and decision-making | 4 / 4 |
| `c1` | Inter | Conduct oneself as a professional in a practice setting. | conduct oneself | professional, in a practice setting | professionalism; practice setting | (added; not searched) |
| `c2` | Inter | Test theoretical knowledge by applying it in practice and reflecting on the result. | test, apply, reflect | - | theoretical knowledge; practice; theory and practice | (added; not searched) |

## AI and Technology

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Inter | Exercise AI literacy through informed, justified decisions about when, and when not, to use AI | exercise, decide, use | informed, justified, when, and when not | AI literacy; decisions; AI use; the "golden rule"; informed restraint | 165 / 45 |
| `02` | Adv | Avoid GenAI misconduct risks and never cite GenAI outputs as a source | avoid, cite | never | GenAI; misconduct risks; GenAI outputs; source; never-cite-genai rule; the five genai misconduct risks | 118 / 22 |
| `03` | Inter | Apply a critical-use workflow treating AI as a critical friend, not a replacement for independent thought | apply, treat | critical, independent | critical-use workflow; critical friend; independent thought; ai as a "critical friend" | 14 / 12 |
| `04` | unplaced | Progress through tiers of digital/AI capability while treating ethics as cross-cutting | progress, treat | cross-cutting | digital capability; AI capability; ethics; understand, apply, create tiering backbone; ai ethics as cross-cutting | 29 / 23 |
| `05` | Inter | Weigh the costs of AI/technology use, including environmental and professional impact, against its benefits | weigh | environmental, professional | costs; benefits; AI use; technology use; environmental impact; environmental cost of ai use; ai and graduate identity | 46 / 28 |
| `06` | Adv | Distinguish permitted technological support from an unfair academic advantage | distinguish | permitted, unfair | technological support; academic advantage; the distinction between permitted support and unfair advantage | 3 / 3 |

## Creativity

| Card | Tier | Statement | Verbs | Measures | Keywords | Benchmark hits |
|---|---|---|---|---|---|---|
| `01` | Intro | Recognise creativity as a developable, cross-disciplinary academic skill related to critical thinking | recognise, relate | developable, cross-disciplinary | creativity; academic skill; critical thinking; creativity as a developable, cross-disciplinary academic skill; the creativity-critical-thinking relationship | 457 / 53 |
| `02` | Inter | Apply divergent and convergent thinking at the right stage of a task | apply | at the right stage | divergent thinking; convergent thinking; task; divergent versus convergent thinking | 13 / 11 |
| `03` | Intro | Overcome creative barriers such as fear of failure and perfectionism | overcome | - | creative barriers; fear of failure; perfectionism; overcoming creative barriers | 5 / 4 |
| `04` | Inter | Use structured creative problem-solving methods | use | structured, creative | creative problem-solving; methods; combinatorial creativity and the "adjacent possible"; divergent-thinking methods | 170 / 51 |
| `05` | Inter | Exercise cognitive flexibility and learning agility when a strategy is not working | exercise | when a strategy is not working | cognitive flexibility; learning agility; strategy; cognitive flexibility and learning agility | 5 / 2 |
| `06` | Adv | Apply creativity and enterprise thinking to professional and entrepreneurial contexts | apply | professional, entrepreneurial | creativity; enterprise thinking; entrepreneurship; enterprise awareness, mindset, capability, effectiveness pipeline; the "about / for / through" distinction; creativity as a graduate/professional attribute | 428 / 54 |
| `07` | Inter | Draw on established creativity theory to justify a creative approach | draw on, justify | established, creative | creativity theory; creative approach; de bono's lateral thinking and bloom's taxonomy | 3 / 3 |

---

## Change notes
- 0.1.2: 4 October 2026, 10:53: note on D-ing-0058 (ing N-0120).
- 0.1.1: 4 October 2026, 08:51: moved from `sandboxes/ing/cards/` to `sandboxes/ing/integrations/cards/`: the cards are an integration, not part of the library documents (Abbott, 08:51; ing N-0111).
- 0.1.0: 4 October 2026, 08:48: created (Abbott, 08:46; ing N-0110).
