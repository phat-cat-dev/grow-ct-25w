Trial build — pathway-proliferation, "presenting" — CRS gates (crs-02, crs-03, crs-04)
Continues trial-build-presenting-sdef-05.md into the CRS phase, acting as the gate's agent role for crs-02_thematic-scope, crs-03_course-outcomes and crs-04_lesson-map (design-kb/design-kb.gates.json). Status: proposed throughout — nothing here is a human-confirmed gate record. Section numbering continues from sdef-05 (which ended at Section 12).

Section 13: A note before the gate output — AL-2 corrections made at this gate
Per crs-03's own authoringReview ("this gate is where AL-2's one-idea rule... is PRODUCED"), sdef-05 Section 6 was re-checked against AL-2 before use. Six of the sixteen outcomes failed it (two verbs/ideas joined by "and"). All six are reworded below to single-idea form; none are dropped, and no capability loses its outcome. This is drafting discipline expected at this gate, not a change to sdef-05 itself.

id	sdef-05 wording	AL-2 fault	corrected wording (used from here on)
presenting-i-01	"...and what skills the task carries into work"	two ideas (what the brief sets out AND transferable skills)	"Explain how a presentation brief sets out its intended audience, required form and the ideas it is meant to make clear." (transferable-skills idea moves to lesson grounding only, not the outcome)
presenting-i-04	"Time a rehearsal..., identify one specific problem... and make a targeted change..."	three verbs	"Identify, from a timed rehearsal of a presentation, the one specific problem it reveals."
presenting-i-05	"Identify the audience and form..., and use that to guide what is planned..."	two verbs	"Identify the audience and form a presentation brief requires."
presenting-d-05	"Explain...and name the classic errors that lose one"	two verbs	"Explain how a deliberately designed opening engages an audience from the first moment."
presenting-d-06	"Open a presentation engagingly and stay composed..."	two verbs	"Respond to an unplanned challenge from the audience without losing the talk's structure." (the "classic errors" idea moves to this lesson's grounding instead, via ch11/common-presentation-errors)
presenting-e-02	"...diagnose a team's state and lead or mediate a conflict"	two verbs	"Mediate a conflict within a team, reading its state through a personality model and a stage-of-development model." (one main verb; the model-reading is a method clause, not a second action)

All other ten outcomes were checked and pass AL-2 as drafted (compound-noun objects such as "audience and form" or "pacing, detail and structure" are permitted by the rule; a single finite verb with a participial or purpose clause is one idea, not two).

Section 14: crs-02_thematic-scope (one per tier)

Introductory
field	value
sourceType	book-derived
chapter	"11 (primary); scoped by the pathway's own i1/i2/i3 capability rows (catalogue/context/pathway/presenting.json), not by chapter-section partition alone — see Section 17 for how this differs from the built-course-shape record for this same tier"
sectionsInScope	ch11/opening; ch11/learning-objectives-and-keywords; ch11/defining-the-presentation; ch11/presentations-and-transferable-skills (context for i1 only, not independently outcome-bearing — see Section 13); ch11/planning-structuring-and-designing-your-presentation; ch11/tips-on-structure; ch11/summary
sectionsOutOfScope	ch11/designing-visual-aids, ch11/common-presentation-errors (d1/d3: INTERMEDIATE); ch11/working-in-groups, ch11/what-tutors-look-for-in-group-work, ch11/personality-types-and-conflict-resolution, ch11/optimising-your-performance-in-group-work (e1/e2/e3: ADVANCED)
tierWindow.goal	Read a presentation brief for what it tests and build an individual presentation to it through a fixed five-step method, then check it against a timed rehearsal.
tierWindow.cognitiveDemand	Recognition, recall, description and a first, guided self-check (understand, build, identify).
tierWindow.taskComplexity	Well-defined, one idea at a time; a fixed method applied to a single, individually-owned brief.
tierWindow.autonomy	High scaffolding; worked examples (Natalie); feedback confirms and explains.
tierWindow.voiceBand	Section 16 Beginner (bands 2-4)
tierWindow.outcomeVerbs	explain, identify, build, apply, time
priorExperienceAnchor	No prior experience of preparing an academic presentation is assumed; the learner has not yet given a graded presentation.
subThemes	(1) presentation-as-assessment — what a brief sets out (audience/form/content); (2) brief-guided-planning — identifying what a brief requires before planning; (3) five-step-method — building a presentation through the five steps; (4) rehearsal-and-feedback-theory — why timing and naming a specific problem supports improvement; (5) timed-rehearsal-practice — running a timed rehearsal to surface and act on one problem

Intermediate
field	value
sourceType	book-derived
chapter	"11 (primary); scoped by d1/d2/d3"
sectionsInScope	ch11/designing-visual-aids; ch11/types-of-presentations-used-for-assessment; ch11/tips-on-structure; ch11/common-presentation-errors
sectionsOutOfScope	chapter framing (INTRODUCTORY); ch11/defining-the-presentation, ch11/presentations-and-transferable-skills (i1: INTRODUCTORY); group-work/personality chunks (e1/e2/e3: ADVANCED)
tierWindow.goal	Design accessible visual aids, adapt delivery across the formats used for assessment, open engagingly and recover composure when challenged.
tierWindow.cognitiveDemand	Application and analysis: judge, adapt, redesign, compare.
tierWindow.taskComplexity	Realistic tasks with several moving parts (format + structure + visual aids + a live audience) managed together.
tierWindow.autonomy	Moderate scaffolding; worked examples (Nasser) model the moves, then the learner applies them.
tierWindow.voiceBand	Section 16 Intermediate (bands 2-4)
tierWindow.outcomeVerbs	explain, analyse, design, redesign, adapt, respond
priorExperienceAnchor	The learner already knows what a presentation is and can build one to a brief (the introductory tier, or equivalent); this tier is about making it land for a real audience across formats.
subThemes	(1) reducing-visual-clutter; (2) accessible-visual-aids-in-practice; (3) format-demands; (4) adapting-content-across-formats; (5) designed-openings; (6) responding-to-audience-challenge

Advanced
field	value
sourceType	book-derived, supplemented by benchmark-evidence fill for e1 and e3 (both have thin/no book grounding — carried over from sdef-05 L3)
chapter	"11 (primary); scoped by e1/e2/e3"
sectionsInScope	ch11/working-in-groups; ch11/what-tutors-look-for-in-group-work; ch11/personality-types-and-conflict-resolution; ch11/optimising-your-performance-in-group-work
sectionsOutOfScope	everything owned by introductory/intermediate above. e1 (professional formats) and e3 (defending an argument under questioning) have no book section of their own in scope — their grounding is T4 (evidence genericOutcomes: Toulmin's model; Hyland's (2005) stance model), carried in from sdef-05 and not re-derived here.
tierWindow.goal	Present with professional and academic authority, lead and mediate group work, and defend an argument under live questioning.
tierWindow.cognitiveDemand	Justification, evaluation and mediation: construct, defend, judge, mediate.
tierWindow.taskComplexity	Ill-defined and contested: a hostile question, a team in conflict, no single settled right answer.
tierWindow.autonomy	Low scaffolding; the learner directs and justifies; feedback probes reasoning.
tierWindow.voiceBand	Section 16 Advanced (bands 2-4)
tierWindow.outcomeVerbs	construct, identify, use, mediate, apply, evaluate, explain, judge
priorExperienceAnchor	The learner can already deliver a presentation across common formats (the intermediate tier, or equivalent); this tier moves to standing as a presenter and a collaborator, not only completing the task.
subThemes	(1) professional-argument-construction; (2) group-work-behaviours-tutors-value; (3) personality-and-conflict-mediation; (4) optimising-own-group-performance; (5) critiquing-stance-in-argument

crs-02 self-check (SCP-1, STR-1, TW-1): SCP-1 — no section appears in both in-scope and out-of-scope lists in any tier, checked by inspection. STR-1 — every tier carries 5 or 6 subThemes (within the 5-10 band). TW-1 — all three voiceBand values are copied verbatim from the pathway's own real built-course-shape crs-02 records for presenting (confirmed identical wording), so they agree by construction.

Section 15: crs-03_course-outcomes (3 per tier, default count, no courseOutcomeCountReason needed)

Introductory
id	text	confidence statement	serves (sdef-05 rows)
co1	Read a presentation brief for the audience, form and content it requires.	I can read a presentation brief for the audience, form and content it requires.	i1 (presenting-i-01, i-05)
co2	Build an individual presentation to a brief through a structured five-step method.	I can build an individual presentation to a brief through the five-step method.	i2 (presenting-i-02)
co3	Improve a presentation by identifying a specific weakness surfaced in a timed rehearsal.	I can improve a presentation by identifying a specific weakness surfaced in a timed rehearsal.	i3 (presenting-i-03, i-04)

Intermediate
id	text	confidence statement	serves
co1	Design visual aids that reduce clutter and meet accessibility standards for a presentation audience.	I can design visual aids that reduce clutter and meet accessibility standards.	d1 (presenting-d-01, d-02)
co2	Adapt a presentation's pacing, detail and structure to the demands of its assessed format.	I can adapt a presentation's pacing, detail and structure to its assessed format.	d2 (presenting-d-03, d-04)
co3	Sustain audience engagement from a presentation's opening through to an unplanned challenge from the floor.	I can sustain audience engagement from a presentation's opening through to an unplanned challenge.	d3 (presenting-d-05, d-06, corrected)

Advanced
id	text	confidence statement	serves
co1	Construct a professionally formatted argument, such as a pitch, that makes its reasoning explicit.	I can construct a professionally formatted argument that makes its reasoning explicit.	e1 (presenting-e-04)
co2	Collaborate effectively in group work, drawing on an awareness of personality, team development and the practices tutors value.	I can collaborate effectively in group work, drawing on an awareness of personality, team development and the practices tutors value.	e2 (presenting-e-01, e-02 corrected, e-03)
co3	Defend an argument with an academic voice under live questioning, judging where a stance over-claims or hedges against the evidence.	I can defend an argument with an academic voice under live questioning.	e3 (presenting-e-05)

courseOutcomeBanks (all three tiers): each co above gets exactly 3 mcqSets, each {"coupling": "shell-coupled", "crossLessonApplication": true, "feedbackOnEveryAnswer": true, "status": "drafted"} — this convention is copied directly from the real, closed built-course-shape courseOutcomeBanks for presenting's three tiers (verified identical across all three), since crs-03's own validation.scopeNote treats AL-4 as "ALSO already a live automated check" and nothing in the proposal suggests the mcqSet-spec convention should change under pathway-proliferation.

crs-03 self-check (AL-2, AL-4): AL-2 — all nine courseOutcomes texts and nine confidenceStatement texts carry one verb/one object each (checked by the same method as Section 13 above; none joins two actions with "and"). AL-4 — every courseOutcomes[].id (co1-co3 in all three tiers) appears exactly once as a courseOutcomeBanks[].outcomeId, and no bank names an id outside its own tier's three; both directions hold.

Section 16: crs-04_lesson-map (one per tier; lesson count meets the 2 Nov 2026 minimum-5 ruling in every tier)

Introductory — 5 lessons, progression: "Reading a brief (L01-L02) is assumed before building to it (L03); building is assumed before rehearsing and improving against it (L04-L05)."
key	mainCourseOutcome	title	sourceSections (chunkId, pages)	outcomes (serves co, each id Lxx-oY)
L01	co1	Reading a presentation brief	ch11/defining-the-presentation (201-202)	o1 Explain what a presentation brief tells you about its intended audience. / o2 Explain what a presentation brief tells you about its required form. / o3 Identify the central idea a presentation brief is meant to make clear.
L02	co1	Using the brief to guide planning	ch11/defining-the-presentation (201-202, reused)	o1 Identify the audience and form a presentation brief requires. / o2 Give an example of a planning decision a presentation brief should guide. / o3 Recognise when a planned presentation has drifted from its brief.
L03	co2	Building a presentation through the five steps	ch11/planning-structuring-and-designing-your-presentation (205-208); ch11/tips-on-structure (209-210)	o1 Describe the five steps for building a presentation from a brief. / o2 Apply the five-step method to produce a hook, a main body of clear points and a conclusion, using Natalie's worked example as a model. / o3 Check a draft conclusion against the objectives set out in the original brief.
L04	co3	Why a timed rehearsal helps	(no book chunk; T4 evidence genericOutcome, Kolb's experiential learning cycle — see sdef-05 L3)	o1 Explain Kolb's experiential learning cycle as a reason for rehearsing to a timer. / o2 Explain why naming one specific moment that went wrong is more useful than a general sense a rehearsal "didn't go well". / o3 Recognise the difference between a vague rehearsal note and a specific, actionable one.
L05	co3	Running a timed rehearsal	(no book chunk; T4, as above)	o1 Time a rehearsal of a presentation against the slot it has been given. / o2 Identify, from a timed rehearsal, the one specific problem it reveals. / o3 Choose a targeted change to make before the next rehearsal attempt.

Intermediate — 6 lessons, progression: "Designing accessible aids (L01-L02) and adapting to format (L03-L04) are both delivery-preparation moves; opening well and recovering from challenge (L05-L06) are the live-delivery moves that depend on having something well-prepared to deliver."
key	mainCourseOutcome	title	sourceSections	outcomes
L01	co1	Why clutter and accessibility matter	ch11/designing-visual-aids (208-209)	o1 Explain how visual clutter makes a slide harder for an audience to follow. / o2 Explain what an accessibility standard (contrast, text size, captions) requires of a slide. / o3 Apply the "less is more" principle to judge whether a slide needs trimming.
L02	co1	Redesigning visual aids	ch11/designing-visual-aids (reused)	o1 Redesign a cluttered slide to cut unnecessary content. / o2 Check a redesigned slide against an accessibility standard. / o3 Predict how a real viewer would respond to a redesigned slide, compared with the original.
L03	co2	What a presentation format demands	ch11/types-of-presentations-used-for-assessment (203-205)	o1 Identify the demands a given presentation format places on a speaker. / o2 Analyse how a talk, a poster, a group presentation and an interview-style format each call for a different pace. / o3 Explain why the same content needs a different level of detail in two different formats.
L04	co2	Adapting content for a new format	ch11/types-of-presentations-used-for-assessment (reused)	o1 Adapt a presentation's pacing to a new format. / o2 Rebuild a presentation's level of detail and structure for a new format, rather than simply shortening the original. / o3 Compare an adapted presentation against the original for fit with the new format.
L05	co3	A deliberately designed opening	ch11/tips-on-structure (209-210)	o1 Explain how a deliberately designed opening engages an audience from the first moment. / o2 Identify the hook Nasser uses in the chapter's worked example. / o3 Draft an opening for a presentation of your own that is more than a restated title slide.
L06	co3	Responding to an unplanned challenge	ch11/common-presentation-errors (210-212)	o1 Recognise a classic presentation error named in the chapter. / o2 Respond to an unplanned challenge or question from the audience without losing the talk's structure. / o3 Explain why staying composed under an unplanned challenge matters more than having a perfect script.

Advanced — 5 lessons, progression: "Constructing a professional argument (L01) and the three group-work lessons (L02-L04) are independent threads built on the intermediate delivery skills; defending an argument under questioning (L05) draws on both the academic-voice material in L01 and the composure-under-challenge groundwork from intermediate L06."
key	mainCourseOutcome	title	sourceSections	outcomes
L01	co1	Constructing a professional argument	(no book chunk; T4, Toulmin's model — e1's book grounding is types-only, per sdef-05 L3)	o1 Identify claim, evidence, warrant and rebuttal in a worked argument, using Toulmin's model. / o2 Construct an argument for a professional pitch using claim, evidence, warrant and rebuttal. / o3 Check a constructed argument for a step where the reasoning is left implicit.
L02	co2	Behaviours tutors and employers value	ch11/working-in-groups (212-213); ch11/what-tutors-look-for-in-group-work (213-215)	o1 Explain why tutors assess the process of group work, not only its product. / o2 Identify one of the eight named traits in a described group member. / o3 Recognise which of the eight traits a given group-work situation is calling for.
L03	co2	Mediating a team conflict	ch11/personality-types-and-conflict-resolution (215-218)	o1 Use the OCEAN personality model to describe a team member's likely behaviour in conflict. / o2 Use a stage-of-development model to read where a team currently sits. / o3 Mediate a conflict within a team, drawing on the chapter's worked example.
L04	co2	Optimising your own performance	ch11/optimising-your-performance-in-group-work (218)	o1 Identify one of the chapter's six numbered recommendations for group-work performance. / o2 Apply a named recommendation to a group-work situation in your own study. / o3 Evaluate your own last piece of group work against one of the six recommendations.
L05	co3	Critiquing stance in a recorded argument	(no book chunk; T4, Hyland's (2005) stance model — e3's book grounding is named-only, per sdef-05 L3)	o1 Explain Hyland's distinction between overclaiming and hedging in academic argument. / o2 Identify a moment of overclaiming or hedging in a recorded argument. / o3 Judge whether a speaker's stance in a recorded argument matches the strength of their evidence.

crs-04 self-check (AL-1, AL-2, MCO-1): AL-1 — every outcomes[].serves names a real co1/co2/co3 id in its own tier; none dangles. AL-2 — every lesson-outcome text carries one verb/one object (checked individually; none joins two actions with "and" — the same method as Section 13). Lesson subject matter stays within each tier's sectionsInScope (Section 14); the four lessons with no book chunk (Introductory L04-L05, Advanced L01 and L05) are grounded in T4 instead, which is in scope by sdef-05's own Section 2 source register, not an out-of-scope addition. MCO-1 — within every lesson, all three outcomes[].serves share one value, and that value equals the lesson's own mainCourseOutcome; checked for all 16 lessons.

Section 17: Comparison against the real built-course-shape records for presenting
Real, closed crs-02/03/04 records for presenting-introductory, presenting-intermediate and presenting-advanced already exist (courses/presenting-*/course-design_presenting-*.json, human-confirmed, dated 23 Oct 2026, built under the live built-course-shape profile — see sdef-05 L5 on the stale design-kb.pathways.json field that claims otherwise). Comparing them against this trial's output is itself one of the trial's findings.

1. Different starting point, by design. built-course-shape's crs-02 authoringReview points only to crs-01 and design-kb.pathways.json's bookChunks/voiceBand — it never points to catalogue/context/pathway/presenting.json's nine capabilities. This trial's crs-02, by contrast, is scoped capability-first (one tier per i/d/e row), because that is what the sdef chain it is built from (sdef-01..05) is grounded in. The two scopes genuinely differ as a result — this is not an error in either, it is the structural difference the pathway-proliferation proposal is trialing.
2. Section reuse across tiers. The real records reuse the same book chunk across tiers for different purposes (e.g. ch11/types-of-presentations-used-for-assessment and ch11/designing-visual-aids both appear in the real introductory AND intermediate sectionsInScope). This trial's scope assigns each chunk to one tier only via its owning capability, with one deliberate exception (ch11/tips-on-structure, reused in Introductory L03 and Intermediate L05, matching the real records' own precedent for that chunk).
3. e1 and e3 are not taught at all in the real advanced course. The real presenting-advanced record has no lesson on professional presentation formats (pitch, poster, viva-style interview) and no lesson that asks a learner to construct or defend an argument with claim/evidence/warrant/rebuttal or Hyland's stance model — its one authority-related lesson ("Presenting with authority") stays at the level of "own your material" and "choose an authoritative response", with no named framework. This trial's e1/e3 lessons (L01, L05 above) use exactly the Toulmin and Hyland material that catalogue/context/pathway-evidence/presenting.json's genericOutcomes field already carries. The simplest explanation: that evidence file (and the capabilities file it pairs with) was authored after, or independently of, the 23 Oct 2026 build, and the old pipeline never had a reason to consult it. This is the clearest empirical case this trial has found for what the new capability-grounded sdef chain adds over the old one.
4. Course-outcome count and an inconsistency worth flagging (not this trial's to fix). All three real records set courseOutcomeCountReason to "Three, matching the three ... sub-themes" — but then list four courseOutcomes (co1-co4), with co4 an explicit integrative outcome the reason text's own wording ("No integrative fourth outcome...") denies exists. This is a genuine inconsistency inside already-closed, human-confirmed production data, found incidentally while building the comparison above. It sits outside this trial's scope to correct (these are closed records under a different profile), but it is worth a maintainer's attention: either the reason text or the fourth outcome is wrong, consistently across all three tiers. This trial's own crs-03 avoids the pattern by choosing a straight count of three with no integrative fourth, and no capstone lesson to match.
5. Lesson-count floor. The real records have exactly 4 lessons per tier; this trial's have 5, 6 and 5. The real records predate the "minimum 5 lessons" ruling (dated 2 Nov 2026 in design-kb.gates.json's crs-04 scopeNote) by about ten days — this is a timeline artifact, not a defect in the real records.
6. profiles gap, restated at CRS. crs-02_thematic-scope and crs-03_course-outcomes both carry a profiles array in design-kb.gates.json listing only ["built-course-shape", "single-course"]; pathway-proliferation/pathway-distillation is not in either list (crs-04 carries no profiles array at all in the copy read for this trial). sdef-05 already flagged this gap for the SDEF gates; it holds just as much at CRS, and matters more here because CRS output looks, superficially, exactly like a real gate record.

Section 18: Gaps and limits (continuing sdef-05's L1-L6)
limit	what to record
L7 — CRS profiles gap	As Section 17 point 6: crs-02 and crs-03's profiles arrays do not list pathway-proliferation; crs-04 carries no profiles array at all in the copy read. This trial's CRS output, like sdef-05's SDEF output, is not a record any currently-wired gate would accept without that array being extended first.
L8 — Fine-grained lesson outcomes are this trial's invention, not sourced text	The 48 lesson-level outcomes in Section 16 decompose each of the sixteen (corrected) sdef-05 outcomes into three finer-grained angles (typically: explain/describe the idea, apply it to a worked example or evidence example, then a transfer/judgement task), following the same decomposition pattern visible in the real built-course-shape records. The three-way split itself, for each lesson, is this trial's own editorial judgement about how to teach the single underlying idea, not something drawn from an additional source. None of the three invents a new fact; each stays inside the single capability's own grounding (book quote, worked example name, or named evidence/genericOutcome). But the specific three-way cut is a judgement call, consistent with crs-04's own validation.checks AL-2 note that "the outcome count for a lesson is a judgement call".
L9 — Closed-record inconsistency found incidentally	Section 17 point 4 (the courseOutcomeCountReason text vs. the actual four-outcome courseOutcomes array, repeated identically across all three closed presenting records). Flagged for a maintainer; out of scope for this trial to fix, since these are human-confirmed records under a different profile.
L10 — mcqSets coupling convention copied, not independently derived	This trial's courseOutcomeBanks reuse the real records' "shell-coupled" convention for every mcqSet rather than deriving it fresh, on the reasoning that crs-03's validation.scopeNote treats AL-4 as already live-checked elsewhere and nothing in the proposal suggests this convention should change under pathway-proliferation. That reasoning was not independently verified against docs/authoring/gate-redesign-2026-10-06.md's A-round text.

Section 19: Hand-off
reader	reads	for
crs-05_course-spec	Sections 14-16 (not run in this trial; its own job is a mechanical rollup, not new authoring)	auto-stands rollup into the course pack
progression-signposting	Section 16's three progression statements, plus sdef-05 Section 7-8	cross-tier signposting (not run in this trial)
les-01, wra-01 to wra-04	Section 16 (lesson outcomes, source sections)	authoring (not run in this trial)
a future maintainer review	Section 17 points 3-4 and Section 18 L7-L10	deciding whether to (a) extend the CRS gates' profiles arrays, (b) reconcile the genericOutcomes-vs-built-course-shape gap for presenting's advanced tier specifically, and (c) fix the real courseOutcomeCountReason inconsistency

Review and storage (as specified): unreviewed; this is the agent's first proposal for CRS, same status as sdef-05. For a real gate run this would go in each gate's own decidedValue; for this trial it is only this file.
