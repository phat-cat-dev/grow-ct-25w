Trial build — pathway-proliferation, "presenting" — sdef-05 shell context definition statement
Produced by walking the design-status gate chain in pathway-proliferation-proposal.md (ONB > CXS > SDEF) as a trial, acting as the gate's agent role. Status: proposed throughout — nothing here is a human-confirmed gate record, since the gates it is built from (sdef-01..05) are not wired into design-kb/design-kb.gates.json. Treat this file as what sdef-05 would hand off, not a closed decision.

Section 1: Header
Pathway:        presenting (pathway 7, "Presenting", catalogue/pathways.json)
Route:          pathway-proliferation
Tier scope:     all three (introductory, intermediate, advanced)
Course name(s): "Presenting: the essentials" (introductory) | "Presenting: across formats" (intermediate) | "Presenting: with authority" (advanced) — proposed at onb-06, not yet confirmed; drawn from design-kb.pathways.json tiers.presenting.focus strings, rephrased as titles
Subject:        none (baseline shell, chosen at onboarding for this trial)
Qualifiers:     none
Status:         proposed
Generated:      4 Nov 2026, revision 1

Section 2: Source register
ref	group	source	file	field or selector	version or date	status	used for
T1	Theme: pack	Pathway pack	catalogue/pathways.json	pathways[id=presenting]	pathwaysVersion 1.0.0	live	pathway, chapters
T2	Theme: pathway	Pathway reference	catalogue/context/pathway/presenting.json	capabilities[] (i1-e3), bookGrounding	no date recorded; status "drafted"	drafted	the 9
T3	Theme: tiers	Tier progression	same file	tierProgression (levels, tierStatements, masteryNote, ladderReadings)	no date recorded	drafted	tiers, journey
T4	Theme: outcomes	The 18 evidence examples, plus a drafted genericOutcomes pair per capability	catalogue/context/pathway-evidence/presenting.json	evidence[], genericOutcomes[]	no date recorded; status "drafted"	drafted	the outcomes (both the evidence set and, unusually for this pathway, an already-drafted flat-outcome candidate per row — see note below)
T5	Theme: book	Book source map, chapter 11	source-kb/source-maps/book-excelling-at-university-2026.json	chunks ch11/* (11 real teaching sections, 3 framing)	kbVersion 0.1.1	confirmed (per-chunk boundaryNote, Abbott 8 Oct 2026)	book grounding
T7	Theme: index (pathway-local)	Ladder readings	catalogue/context/pathway/presenting.json	tierProgression.ladderReadings (rowId F, i1-e3: practice/knowledge/identity)	no date recorded	drafted	identity readings for the journey review, used in place of the lens.json index (see limit L4 below)
F1	Framework	Frameworks	catalogue/context/shared/cross-cutting.json	frameworks.FHEQ	crossCuttingVersion 1.0.0	live	level grounding
D1	Design	Pathway build status	design-kb/design-kb.pathways.json	pathways[id=presenting].tiers	no date recorded	drafted	course names, voice bands, and a discrepancy flagged at L5 below

Note on T4: unlike the generation formula described in pathway-proliferation-proposal.md (which treats the 18 as evidence examples only, with no separate flat-outcome formula), pathway-evidence/presenting.json already carries a second, parallel "genericOutcomes" pair per capability (origin: "from-benchmark"), each one already phrased as a candidate learning outcome with its own grounding. This trial used genericOutcomes directly as the Layer-2 benchmark-fill material in sdef-04 below, rather than drafting fresh fill outcomes from the capability statement. Whether this genericOutcomes field is itself the "finished 18" the proposal's F6/1.8 describe as still being worked on elsewhere, or a separate in-repo draft, is not resolved by this trial — flagged at L2 below.

Section 3: Understanding and intent
Presenting (chapter 11) is one of the less writing-centric of the 13 pathways, and the only one where the self-system (confidence, nerves, identity as a presenter) is present from the introductory tier rather than entering only at the top. The chapter's own content is unevenly spread across the three tiers: three of its eleven real sections ground the introductory tier, three ground the intermediate tier one-for-one against its three capabilities, and four ground a single advanced capability (group work), leaving the other two advanced capabilities (professional formats; defending an argument under questioning) with thin, named-only book coverage. This pathway-proliferation trial builds all three tiers together specifically so that imbalance is visible and can be weighed across the whole pathway, rather than tier by tier. No subject or qualifier context was taken for this trial (chosen as a baseline run of the new gate); the shell is generic and would need cxp-01/02 to add one later. Group work's standing as "could become a pathway of its own" (per the pathway's own identity statement) is noted but not acted on here — this trial treats it as advanced-tier content within presenting, as the pathway file currently has it.

Section 4: Tier definitions
tier	levels	definition	what changes in this tier	source
Introductory	L3-L5 (i1=L3, i2=L4, i3=L5)	Reading a presentation brief for what it tests and building a straightforward, individually delivered presentation through a set five-step method, then checking it against the clock.	Declarative knowledge of what a presentation is and what it is for, put to work for the first time through a fixed recipe; a first, basic check of one's own performance in rehearsal.	T3
Intermediate	L4-L6 (d1=L4, d2=L5, d3=L6)	Designing and delivering presentations that work for a real audience: accessible visual aids, delivery adapted to the occasion's format, and managing one's own nerves rather than being managed by them.	Procedural knowledge becomes conditional (which approach fits which format) and the self-system enters directly: the learner starts regulating their own state, not just their content.	T3
Advanced	L5-L7 (e1=L5, e2=L6, e3=L7)	Presenting with professional and academic authority: in the formats a pitch, a poster or a viva-style interview require; as a leader and mediator inside a group; and as someone who can assert and defend their own argument under live questioning.	Fully metacognitive: the learner presents as someone with standing (in a team, in a discipline, in a professional setting), not only as someone completing a set task.	T3

Section 5: The definitive 9 benchmarks
row	tier	level	pathway benchmark (original)	definitive benchmark	change	why	sources
i1	Introductory	L3	Explain what a presentation tests and read its brief	unchanged	unchanged	No context to blend against (baseline shell); capability already book-grounded.	T2
i2	Introductory	L4	Build a presentation to a brief through the five steps	unchanged	unchanged	—	T2, T5:ch11/planning-structuring-and-designing-your-presentation
i3	Introductory	L5	Practise to time and fix what does not work	unchanged	unchanged	Thin book grounding (no bookGrounding record), but the statement itself is clear and the evidence pair is strong; no rewrite needed.	T2, T4
d1	Intermediate	L4	Design effective, accessible visual aids ("less is more")	unchanged	unchanged	—	T2, T5:ch11/designing-visual-aids
d2	Intermediate	L5	Adapt delivery to different presentation formats	unchanged	unchanged	—	T2, T5:ch11/types-of-presentations-used-for-assessment
d3	Intermediate	L6	Open engagingly and manage own nerves	unchanged	unchanged	—	T2, T5:ch11/common-presentation-errors
e1	Advanced	L5	Present in professional formats (pitch, conference poster, viva-style interview)	unchanged	unchanged	Fuzzy top (level 5, shared with i3 and d2) — see Section 7. Kept at Advanced on knowledge kind, not level.	T2
e2	Advanced	L6	Work in a group, leading and resolving conflict	unchanged	unchanged	—	T2, T5:ch11/working-in-groups, ch11/what-tutors-look-for-in-group-work, ch11/personality-types-and-conflict-resolution, ch11/optimising-your-performance-in-group-work
e3	Advanced	L7	Present and defend an argument with an academic voice under questioning	unchanged	unchanged	—	T2, T4

None of the 9 needed rewriting: this trial carried no subject or qualifier context to blend against (sdef-03 was skipped), so sdef-04 had nothing to merge in. A context-bearing run would very likely propose changes here.

Section 6: The definitive learning outcomes, by tier

Introductory: 5 outcomes (floor met; 3 from the book, 2 benchmark fill for i3, which has no book section of its own)

id	outcome	benchmark row	kind	level	source wording	change	sources
presenting-i-01	Explain how a presentation brief sets out its intended audience, required form and the ideas it is meant to make clear, and what skills the task carries into work	i1	conceptual	L3	book: "you're expected to articulate an argument... communicate clearly"; "a highly valued competency"	book-grounded, as original	T5:ch11/defining-the-presentation, ch11/presentations-and-transferable-skills
presenting-i-02	Build an individual presentation to a given brief through the five steps, producing a hook, a main body of clear points, and a conclusion that returns to the brief's objectives	i2	procedural	L4	book: Natalie's worked example; "refer back to the objectives you set"	book-grounded, folds in the "tips on structure" section (pp.209-210) as the same skill at finer grain, not a separate outcome	T5:ch11/planning-structuring-and-designing-your-presentation, ch11/tips-on-structure
presenting-i-03	Explain how timing a rehearsal and naming the specific moment it went wrong supports improving a presentation before delivery	i3	conceptual	L5	evidence genericOutcome, Kolb's experiential learning cycle	benchmark fill (i3 has no book section; evidence/genericOutcomes used instead)	T4 (genericOutcomes, i1/i3 capability block), unattributed benchmark
presenting-i-04	Time a rehearsal of a presentation, identify one specific problem it reveals and make a targeted change before the next attempt	i3	applied	L5	evidence genericOutcome, applied	benchmark fill, as above	T4, unattributed benchmark
presenting-i-05	Identify the audience and form a presentation brief requires, and use that to guide what is planned before any content is drafted	i1	applied	L3	evidence genericOutcome, applied, qaa-universal/threshold/oral-or-other-communication-to-audiences	benchmark fill, added to give i1 an applied partner to presenting-i-01's conceptual framing	T4, universal-reference.json

Intermediate: 6 outcomes (one book outcome and one benchmark-fill outcome per capability)

id	outcome	benchmark row	kind	level	source wording	change	sources
presenting-d-01	Analyse how reducing visual clutter and applying accessibility standards (contrast, text size, captions) improves an audience's ability to follow a presentation	d1	conceptual	L4	book: "less is more"; design principle	book-grounded	T5:ch11/designing-visual-aids
presenting-d-02	Redesign a set of visual aids to cut unnecessary content and meet accessibility standards, checking each change against how real viewers respond	d1	applied	L4	evidence genericOutcome, applied	benchmark fill	T4, qaa-universal/threshold/oral-or-other-communication-to-audiences
presenting-d-03	Analyse how the demands of a presentation format (talk, poster, group, professional, interview, technology-based) shape the pacing, detail and structure a speaker should choose	d2	conceptual	L5	book: the six assessment types	book-grounded	T5:ch11/types-of-presentations-used-for-assessment
presenting-d-04	Adapt the same content for a different presentation format, rebuilding its pacing, detail and structure rather than simply shortening the original	d2	applied	L5	evidence genericOutcome, applied	benchmark fill	T4, qaa-universal/threshold/oral-or-other-communication-to-audiences
presenting-d-05	Explain how a deliberately designed opening and a managed level of arousal help a speaker engage an audience from the first moment, and name the classic errors that lose one	d3	conceptual	L6	book: the hook; "classic presentation errors"; Nasser's worked example	book-grounded	T5:ch11/tips-on-structure, ch11/common-presentation-errors
presenting-d-06	Open a presentation engagingly and stay composed when faced with an unplanned challenge from the audience, without losing the talk's structure	d3	applied	L6	evidence genericOutcome, applied	benchmark fill	T4, qaa-universal/threshold/oral-or-other-communication-to-audiences

Advanced: 5 outcomes (floor met; 3 from the book, all under e2, which the chapter over-represents; 1 benchmark fill each for e1 and e3, which the book under-represents)

id	outcome	benchmark row	kind	level	source wording	change	sources
presenting-e-01	Explain the personality traits and behaviours tutors and employers look for in group participation (communication, collaborating, flexibility, resilience, leadership, accountability, innovative thinking, organisation)	e2	conceptual	L6	book: the eight traits list	book-grounded, folds in the short "working in groups" framing paragraphs (pp.212-213) as context for this classification rather than a separate outcome	T5:ch11/working-in-groups, ch11/what-tutors-look-for-in-group-work
presenting-e-02	Use a personality model (OCEAN) and a stage-of-development model to diagnose a team's state and lead or mediate a conflict within it	e2	procedural	L6	book: OCEAN model; Ross/David/Sandra/Lucia conflict worked example	book-grounded	T5:ch11/personality-types-and-conflict-resolution
presenting-e-03	Apply the chapter's own recommendations (communication, mediation, and the other named practices) to optimise one's own performance in group work	e2	procedural	L6	book: the six numbered recommendations	book-grounded	T5:ch11/optimising-your-performance-in-group-work
presenting-e-04	Construct an argument for a professional pitch using claim, evidence, warrant and rebuttal, so every step of its reasoning is explicit	e1	conceptual	L5	evidence genericOutcome, Toulmin's model of argument	benchmark fill (e1's book grounding is "types only; no in-depth teaching")	T4, qaa-universal/threshold/oral-or-other-communication-to-audiences
presenting-e-05	Critique the stance taken in a recorded argument, judging where language overclaimed or hedged relative to the strength of the evidence	e3	conceptual	L7	evidence genericOutcome, Hyland's (2005) stance model	benchmark fill (e3's book grounding is "named, not taught with a worked example")	T4, qaa-universal/threshold/oral-or-other-communication-to-audiences

Section 7: Fuzzy-top rulings
boundary	outcome	could sit in	placed in	reason	signposted from
Introductory/Intermediate/Advanced, L5 (three-way)	i3 (practise to time), d2 (adapt delivery to formats), e1 (professional formats)	i3 could sit in Intermediate; e1 could sit in Introductory or Intermediate by level alone	i3 stays Introductory, d2 stays Intermediate, e1 stays Advanced	Placed by knowledge kind, not shared level: i3 is beginning metacognition (checking one's own rehearsal), d2 is conditional procedural skill (choosing by format), e1 is professional-form procedural knowledge with no beginner equivalent elsewhere in the pathway. This is the same "level ≠ tier" point the proposal's own masteryNote makes.	i3 signposts forward to d3 (both self-regulation of nerves/performance, d3 at a more developed level)

Section 8: The learning journey
tier	the learner arrives able to	the learner leaves able to	identity shift (from ladderReadings)	main book sections	feeds into
Introductory	give a talk from notes if told what to say	read a brief for what it tests and build an individual presentation to it through a fixed five-step method, checking it against the clock	from "a learner who presents because it is assessed" to "a student beginning to see themself as a presenter who checks own performance"	defining-the-presentation; transferable-skills; planning-structuring-and-designing; tips-on-structure (folded)	Intermediate (the self-check habit from i3 is assumed, though not recorded in design-kb.pathways.json's assumesFromPrevious field — see L5)
Intermediate	build a presentation from a fixed recipe	design accessible visual aids, adapt delivery across formats, and manage their own nerves rather than being managed by them	from "a participant learning the community's ways" to "a self-regulating presenter whose self-knowledge begins to steer delivery"	designing-visual-aids; types-of-presentations; tips-on-structure + common-presentation-errors	Advanced
Advanced	deliver competently across formats, alone	present with professional and academic authority, lead and mediate a group, and defend an argument under live questioning	from "a presenter with a voice of their own" to "a presenting collaborator whose leadership... expresses own values"	working-in-groups; what-tutors-look-for; personality-types-and-conflict-resolution; optimising-performance	—

Narrative: the journey holds together on Anderson and Krathwohl's continuum exactly as masteryNote describes — declarative/procedural, then procedural-plus-self-system, then fully metacognitive — and the metacognition.stance progression (compliance → purpose → investment → ownership) tracks it. Coverage is complete: all 9 capabilities carry at least one outcome, and 9 of the 11 real book sections are used directly (the other 2 are folded into neighbouring outcomes rather than dropped). Balance (conceptual/applied per tier) holds in Introductory and Intermediate; Advanced leans procedural/book-heavy for e2 and theory-heavy for its two benchmark fills, with no applied-professional outcome of its own for e1 or e3 — flagged at L3 below. No outcome repeats; the academic-voice theme named at presenting-i-01 and embodied at presenting-e-05 is a deliberate revisit at depth, not a duplicate.

Section 9: Context alignments
No subject or qualifier context — this trial ran as a baseline shell. sdef-03 was skipped.

Section 10: Pitch review
From onb-05 (pathway-proliferation: agent reviews the pitch across all three tiers, proposed, not yet put to a human): Presenting is one of the less writing-centric pathways and the only one carrying the self-system from its first tier. Its chapter shape is uneven for a three-tier build — thin at the introductory tier beyond the five-step method, and lopsided at the advanced tier, where group work absorbs four times the book material that either professional-format presenting or defending an argument under questioning gets. Building all three tiers together, as pathway-proliferation does, makes that imbalance visible in one pass rather than discovering it tier by tier; it does not fix the imbalance, which Section 11 below records as a limit for the user to weigh.

Section 11: Gaps and limits
limit	what to record
L1 — Unconfirmed mappings	All benchmark attributions (direct/indirect/unattributed) and the universal-reference.json statement "qaa-universal/threshold/oral-or-other-communication-to-audiences" are taken as given; none were independently re-verified against the raw QAA benchmark text in this trial.
L2 — Status of the genericOutcomes field	pathway-evidence/presenting.json's genericOutcomes pairs were used directly as Layer-2 fill material. Whether this field is the "finished 18" that proposal §1.8/F6 describe as still being built elsewhere, a separate draft, or something in between, is not resolved here — it should be checked before this trial's outcome wording is treated as more than a draft.
L3 — Thin/no book grounding	i3, e1 and e3 have thin or no book grounding (i3: quotes only, no bookGrounding record; e1 and e3: both explicitly marked "described/named... no in-depth teaching" in their own bookGrounding.notes). All three outcomes drawn from them rest on benchmark evidence fill, not the book. Advanced in particular has no applied-professional outcome for e1 or e3, only conceptual/theory ones.
L4 — No subject readings, and no lens.json	Not applicable in the same form as the criticality worked trace (that gap is about subject-benchmark readings by row, which this baseline run never reached since sdef-03 was skipped). Separately: grow-generator-component/lens.json, which the proposal's journey-review check for "learner identity" expects, does not exist on this machine. This trial substituted the pathway's own tierProgression.ladderReadings (identical purpose, pathway-local) for that check; a context-bearing run would hit the same lens.json absence the proposal's own F5 and explore findings already flag.
L5 — A stale build-status field	design-kb/design-kb.pathways.json records presenting's three tiers as status:"planned", courseSlug:null, but courses/presenting-introductory, presenting-intermediate and presenting-advanced already exist under the live built-course-shape profile, and the proposal's own Part A text lists "presenting" among the courses checked against built-course-shape on 29 Oct 2026. This field is out of date and should not be trusted for build status without checking courses/ directly.
L6 — Fuzzy tops decided on kind, not independently checked	The Section 7 ruling leans on the capability's own knowledgeKind field as the deciding factor. That field is authored prose, not a separate, independently checked measure, so the ruling is only as sound as that authoring.

Section 12: Hand-off
reader	reads	for
crs-02_thematic-scope	sections 3, 4 and 8	scope (not run in this trial)
crs-03_course-outcomes	section 6	course outcomes and courseOutcomeBanks, for each tier's course (not run in this trial)
crs-04_lesson-map	sections 6 and 9	proposed lessons and their grounding (not run in this trial)
progression-signposting	sections 6, 7 and 8	signposts between tiers (not run in this trial)
les-01, wra-01 to wra-04	sections 3, 6 and 9	authoring (not run in this trial)
cxp-04	sections 2 and 9	context generation (not run in this trial; this trial has no context to generate from)

1.6 Review and storage (as specified)
Review: confirm, amend, or regenerate with new instructions — none of this has happened; this is the agent's first proposal, unreviewed.
Storage: for a real gate run this would go in the gate record's decidedValue. For this trial it is only this file.
