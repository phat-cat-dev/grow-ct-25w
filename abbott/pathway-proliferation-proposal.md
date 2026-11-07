Pathway-proliferation gating — full lookup survey
Companion to original-pathway-gating-lookups.md (the live system). This file covers the design-status redesign held in design-kb/design-kb.gate-profiles.json (kbVersion 0.1.1) — the profile the user's shorthand "multiplies the old one by three" refers to (pathway-distillation: all three tiers built together, from the pathway's own benchmarks rather than free thematic strands) — plus the single-course profile it shares its machinery with, and the built-course-shape profile, which is status: "live" and documents, for comparison, what the current 4-gate original-pathway-gating-lookups.md flow actually produces.

None of this is wired into design-kb/design-kb.gates.json. Both single-course and pathway-distillation are status: "design". Treat every lookup below as a documented intention, not a running gate, unless stated otherwise.

Contents: the underlying data and generation formula, then Part A (the 3 gate profiles), Part B (the query-layer chain), Part C (open blockers) and Part D (the per-gate lookup table, including the reworked ONB gates onb-01 to onb-06 and the new SDEF gates sdef-01 to sdef-05), Part E (the complete routing), Part F (query paths and data bridges) and Appendix 1 (the sdef-04 and sdef-05 specification).

Gate ids: Part D renumbers ONB, so onb-01 to onb-04 mean different gates there. Parts A to C use the live ids; the "replaces" column in Part D maps old to new.

The underlying data: the 9 capabilities and the 18 evidence statements
Before any gate-profile step runs, two generated catalogue files ground the whole redesign:

The 9 — catalogue/context/pathway/<pathway>.json, capabilities[]. 3 per tier (i1-i3 introductory, d1-d3 intermediate, e1-e3 advanced). Each entry carries rowId, capabilityId, tier, fheqLevel, statement, knowledgeKind, qf, book, competency, vocabulary, bookGrounding. Correction to a common assumption: these are not uniformly pitched at FHEQ L5/L6. Verified directly on criticality.json: i1=L3, i2=L4, i3=L5, d1=L4, d2=L5, d3=L6, e1=L5, e2=L6, e3=L7 — a spread of L3 to L7, FHEQ levels are indicative and cross-cutting (a tier can span several levels and a level several tiers), not a bucket. Only 4 of the 9 (i3, d2, e1, e2 — plus d3/e1 depending on how the L5/L6 band is drawn) actually sit at L5/L6. The file also carries a benchmarkKeys block (note, sources, byTier, attribution, built by tools/key-benchmark-tiers.py) and a source block recording the off-repo ingest files it was built from (core, plan, wide, vocab, eau, adapt, all under a path beginning /home/user/wkspc2614-adapt — confirmed absent on this machine; the raw ingest cannot currently be re-derived or audited from this repo, only the already-built capabilities[] output can).

The 18 — catalogue/context/pathway-evidence/<pathway>.json. Exactly 2 evidence examples per capability (one conceptual, one applied) × 9 capabilities = 18, 6 per tier. Each pair: {kind, title, example, artefact, grounding[]}. Validated by tools/check-pathway-evidence.py — rules taken directly from its docstring: exactly 1 conceptual + 1 applied per capability; conceptual grounding must cite the capability's own ingested theory id or "model: <name>"; word-count bounds (title ≤12, example 35-90, artefact 8-30); no em dash; never the phrase "academic skills". Directly re-run: all 13 pathways pass, not just criticality (files are marked "status": "drafted", i.e. authored and validated but not yet gate-closed anywhere).

An .md export of the 9+18 already exists. tools/ render-pathway-benchmarks-md.py writes gate-experiment/ pathway-capabilities-and-benchmark-keys.md (242,505 bytes, 1,307 lines, re-run directly, exit 0) — one file covering all 13 pathways' capabilities and benchmark keys in one place. A separate, related tool, tools/build-prompt-sets.py, generates RTCF student-facing chat-prompt starters from the same benchmark keys into src/components/adapt-grow-promptbuilder/libraries/ academic-practice-prompts.json — not a generation formula for the 18 itself, but downstream of it.

The generation "formula"
Two distinct things answer "what was the 18 generated from":

Generating the 18 itself — governed by check-pathway-evidence.py's validation rules above. There is no separate, reusable prompt string recorded in the repo for this step; the rules are the closest thing to a formula.

Distilling the 18 into learning outcomes — the book-first, two-layer method, settled 2 Nov 2026, documented in full in gate-experiment/crs-redesign.md. Layer 1 (primary): one LO per real section of the pathway's own book chapter (source-kb/source-maps/book-excelling-at-university-2026.json), book cross-references and definitions taking precedence over external theory. Layer 2 (secondary, fill-to-minimum only): where Layer 1 falls short of 5 LOs, fill using (a) the pathway's own applied/professional benchmark evidence, and/or (b) at most one named theory lesson per tier (each tier is its own Adapt course, so each tier carries its own theory budget), anchored inside an existing book-grounded lesson's context, never freestanding.

This explicitly supersedes an earlier "merge rule" (merge two adjacent benchmark statements into one outcome where they cluster), which was hand-tested against all 9 capabilities of two real pathways (criticality, referencing) and never fired once — 6/6/6 in both, because every pathway-evidence pair is deliberately authored as one theory-grounded example plus one distinct professional-practice example, so the two members of a pair almost never cluster.

Worked trace (criticality, settled 2 Nov 2026). Book chapter 8 splits 3 introductory / 3 intermediate / 5 advanced sections (not the even 3/3/3 the capability model assumed — advanced under-represents the book: capability /05 alone maps to 4 of the 5 advanced sections, and #e3 has no book section at all, a pure Hyland-theory import). Applying the method settles criticality at 5 / 5 / 6 lessons (introductory/intermediate/advanced), within the 5-floor/6-ceiling per tier:

Tier	#	LO source	Traces to
Intro	1	Book: defining critical thought	ch8/defining-critical-thought, #i3
Intro	2	Book: thinking critically about academic sources	ch8/thinking-critically-about-academic-sources, c1
Intro	3	Book: opening up the discourse in practice	ch8/opening-up-the-discourse-in-practice, /02
Intro	4	Theory — Bloom's full taxonomy ladder, orienting preview	Anderson & Krathwohl 2001
Intro	5	Benchmark fill — stakeholder mapping (food bank)	/02 applied evidence
Inter	1	Book: analysing an interpretation	ch8/analysing-an-interpretation, /01
Inter	2	Book: evaluating interpretations	ch8/evaluating-interpretations, /03
Inter	3	Book: engaging with journal articles (Table 8.1)	ch8/engaging-with-journal-articles, /04
Inter	4	Benchmark fill — recognising analysis/evaluation without steer words	/01 applied
Inter	5	Benchmark fill — method-check/briefing (software internship)	/04 applied
Adv	1	Book: active vs passive approaches	ch8/active-and-passive-approaches
Adv	2	Book: forming judgements	ch8/forming-judgements, c2
Adv	3	Book: applying synthesis	ch8/applying-synthesis
Adv	4	Book: the language of criticality	ch8/language-of-criticality, /05
Adv	5	Book: discipline-specific vocabulary	ch8/discipline-specific-vocabulary, /05
Adv	6	Theory — Hyland's 2005 stance model, built on LO3	Hyland 2005, restores #e3
Status: agreed with human gate 2 Nov 2026; not yet run on a second or third pathway, so it is open whether 5/5/6 is typical or specific to criticality's own chapter shape.

Part A — the 3 gate profiles, step by step
single-course (status: design) — one tier, query-layer build
step id	gates	decider	inputs	produces
theme	onb-01, onb-02	agent+human	catalogue/pathways.json	the pathway
tier	onb-03	agent+human	design-kb.tier-bands.json	intro|inter|advanced|none
levels (planned)	—	agent+human	tier-bands, pathway/<p>.json tierProgression.levels	one or adjacent levels
ctx-shell (CXS, pre)	cxs-01..04, cxs-06	auto	reserved placeholders, all auto-pass	the context shell, in place before authoring starts
fork01-frameworks	cxs-05	human (change: was auto)	catalogue/context/shared/cross-cutting.json frameworks (FHEQ, CQFW, FQHEIS/SCQF, QF-EHEA)	chosen framework(s)
fork01-benchmarks (planned)	—	human	pathway/<p>.json capabilities+benchmarkKeys, universal-reference.json	0-9 of the pathway's 9 benchmarks selected
ao-01 (planned)	—	agent+human	chosen frameworks+benchmarks, pathway-evidence/<p>.json (the 18), the tier	the tier's flat LOs, typically 4-6, straight from its 6 benchmark statements — no further distillation
ao-04 (planned)	—	agent+human	AO-01, tools/voice-lint.js	the ONB shell context statement (voice-linted)
lessons	crs-04	agent+human	AO-04's flat LOs, design-kb.content-shapes.json	up to 6 lessons, one LO each
fork02-shell	cxp-01	agent+human	baseline (universal-reference.json) | group (CAH1/2 via tools/resolve-subject-benchmark.js, docs/contexts/cmet/cardiff_met_school_hesa_shortlist.json) | specific (HECoS/CAH3)	the shell's subject grounding
fork03-qualifiers	cxp-02	human	docs/authoring/qualifier-list-2026-10-04.md, universal-reference.json graduate_competency, Advance HE ingests	up to 6 qualifiers, 4 categories
ao-02	cxp-04	agent+human	fork02-shell's resolved benchmark, AO-01	context-specific competency attributes + worked examples, merged via merge-context.js
ao-03 (planned)	—	agent+human	each chosen qualifier's ingest	qualifier-specific competency attributes added to the context pack
continuesWith: crs-05_course-spec, les-01_lesson-proposal, wra-01..04.

pathway-distillation (status: design) — all three tiers at once
Same theme and ctx-shell steps as single-course (CXS runs once, shared across tiers). Then diverges:

step id	gates	decider	inputs	produces
pathway-statements (planned)	—	auto	pathway/<p>.json capabilities(9)+benchmarkKeys, pathway-evidence/<p>.json (the 18)	the 18 statements, 6/tier, with capability+attribution+key
tiered-outcomes (planned)	—	agent+human	source-kb/source-maps/book-excelling-at-university-2026.json, the tier's 6 statements, tierReadings, tier-keyed benchmarks	the tier's flat LOs, book-first two-layer method (see above)
lessons	crs-04	agent+human	the tier's flat LOs (5-6), content shapes	5-6 lessons per tier (hard floor 5, ceiling 6), one LO each
progression-signposting (planned, no generator yet)	—	agent+human	all three tiers' LOs + lesson maps together	forward/backward signposts between tiers — annotation, not new gate content
fork02-shell	cxp-01	agent+human	same as single-course, run once, shared	subject grounding shared across all 3 tiers
fork03-qualifiers	cxp-02	human	same as single-course	up to 6 qualifiers, shared
ao-02	cxp-04	agent+human	fork02-shell's resolved benchmark, each tier's LOs	context-specific attributes, generated once, merged into all 3 tiers' shells
ao-03 (planned)	—	agent+human	qualifier ingests	qualifier-specific attributes, shared across all 3 tiers
continuesWith: les-01_lesson-proposal, wra-01..04 (no crs-05 listed for this profile).

built-course-shape (status: live) — what actually ran
Kept in gate-profiles.json as its own named profile specifically so the two redesigns above can be compared against, or fallen back to, what is really live. Matches original-pathway-gating-lookups.md Part A exactly for onb-01..03, crs-02..04: free thematic strands (5-10, human-authored) are the structural source, not pathway benchmarks; no query layers (TIER/LEVEL(S)/FORK01-03/AO-01-04) exist; 4 course outcomes (gate allows 3-5, built courses all chose 4); 4 parallel lessons, one course outcome + 3 lesson outcomes each (12 total), no synthesis lesson. Checked against the real built courses (criticality, ai-technology, academic-writing, presenting) on 29 Oct 2026.

Part B — the query-layer chain (onboarding side, single-course/pathway-distillation shared)
From gate-experiment/query-layers-and-generation.md (status: design scope, branch gates/tri-tier):

1  TIER          intro | inter | advanced | none                    (optional)
2  LEVEL(S)      auto from tier bands | human: single or grouped | none
     FORK01  GENERIC STATEMENTS
       1  qualification frameworks (user selects)
       2  universal / pathway benchmarks (0-9 of the pathway's 9)
          -> AO-01  GENERIC COMPETENCY ATTRIBUTES CONTEXT: 6 generic benchmarks
     FORK02  SHELL vs CONTEXT SLOT
       1  baseline shell | 2  group context shell | 3  specific context shell
          -> AO-02  CONTEXT SPECIFIC COMPETENCY ATTRIBUTES CONTEXT
     FORK03  QUALIFIERS (up to 6, four categories)
          -> AO-03  QUALIFIER SPECIFIC COMPETENCY ATTRIBUTES CONTEXT
4  AO-04  ONB SHELL CONTEXT STATEMENT (academic prose, voice-linted)
5  flat tiered learning outcomes (settled 2 Nov 2026 — see "flat 6" below), then the lesson map

Layer → gate-today → data-it-reads → status table (reproduced from the source doc, all verified against the live store):

Layer	Gate today	Data it reads	Status
THEME	onb-01, onb-02	catalogue/pathways.json	exists
1 TIER	onb-03	design-kb.tier-bands.json	exists, none option to add
2 LEVEL(S)	none	tier bands; pathway/<p>.json tierProgression.levels (L3-L8)	gap: tier bands list L3-L7 only, no L8
FORK01.1 frameworks	cxs-05 (auto, reserved)	cross-cutting.json frameworks	data exists, needs human-select change
FORK01.2 benchmarks	none	capabilities + benchmarkKeys + pathway-evidence (18) + universal-reference.json	data exists, gate to build
AO-01	none	the above	to build
FORK02 shell	cxp-01 (+ baseline routing)	baseline: universal-reference.json; group: CAH1/2 via tools/subject/core/vocab/cah.json; specific: HECoS/CAH via tools/resolve-subject-benchmark.js	gap: group identity (School→HESA subjects) needs the CMET course data tree
AO-02	cxp-04	subject benchmark corpus, pathway mappings	partial
FORK03 qualifiers	cxp-02 (max 3/3 today), cxs-03 (reserved)	qualifier-list-2026-10-04.md, graduate_competency (20, in universal), Advance HE ingests	gap: no qualifier JSON mapping each qualifier to its ingest yet
AO-03	none	qualifier ingests	to build
AO-04	none	AO-01 to AO-03, tools/voice-lint.js	to build
5 outcomes	crs-04	AO-04	exists (crs-04); crs-03 has no job left under flat-6
"Flat 6" ruling (settled 2 Nov 2026, supersedes a 29 Oct 2026 "3 course + 6 lesson outcomes" draft): AO-01's generic benchmarks (contextualised by AO-02+AO-03 into AO-04) ARE the tier's final learning outcomes, flat — not distilled to 3 and proliferated back to 6. They map one-to-one onto up to 6 lessons (single-course) or 5-6 (pathway-distillation), each ~4-6 pages.

Amended 3 Nov 2026: the upper tiers can hold more than 6 outcomes, and the lesson count normally rises with them. One lesson per outcome is the default rather than a strict rule, and 5 lessons is the minimum. The user signs off the final lesson structure and outcome mapping at crs-04_lesson-map (see CRS in Part D and Appendix 1).

Part C — open structural blockers (none of this is wired live)
crs-02_thematic-scope and crs-03_course-outcomes stay (decided 3 Nov 2026), with sdef-05_shell-definition feeding them. crs-03 keeps courseOutcomeBanks, which wra-03_summative and wra-04_confidence read, so their rules and the tooling that checks them can stay as they are. The "flat 6" ruling in Part B gave crs-03 no job; D5 in Part E settles this, with one course outcome for each agreed outcome.
The 9 capabilities' own off-repo ingest sources are inaccessible from this workspace (/home/user/wkspc2614-adapt, confirmed absent) — the generated capabilities[]/benchmarkKeys output can be read and used, but not re-derived or audited against its raw ingest from here.
L8 is not yet in the tier bands (only L3-L7), despite tierProgression.levels elsewhere documenting it as cross-cutting alongside L7.
The CMET course-data tree now exists but is unconfirmed. grow-generator-component/context-sources/cardiff_met_course_map.json supplies FORK02's "group" shell identity (School to HESA subjects) for 239 courses, proposed from course titles. cardiff_met_school_context.json links subject groups to benchmarks, but 45 of its 78 groups have no core benchmark link, including sport and exercise sciences (27 courses), so those need a person to judge them.
No qualifier JSON yet mapping each of the (proposed) 6 qualifiers across 4 categories to its own ingest.
The book-first two-layer LO method has been run on exactly one pathway (criticality). It is not yet known whether its 5/5/6 lesson split is typical or specific to that pathway's chapter shape.
Phase-order note, same as doc 1: neither design profile introduces a CONF, SUMM, or GLOS phase. Both profiles tag steps with a stage field (pre / course-body / post) instead — pre = CXS before authoring starts, course-body = the tier/LO/lesson build, post = CXP after the lessons exist. This is a different organising axis from an 8-phase list, not a renamed version of it.
Part D — per-gate lookup table (30 gates: reworked ONB, new SDEF and the live gates)
This table starts from the live store table in original-pathway-gating-lookups.md, which holds 24 gates. It differs in four ways: the old ONB gates and crs-01_sources are merged into a reworked ONB, a new SDEF group follows CXS, every reference below uses the new ids, and crs-02 and crs-03 now read from sdef-05 (see CRS). The other gates are as they are in the live store, though all seq numbers have moved.

Columns: deps = dependsOn; generation.sources = the gate's own (pre-existing) generation.sources field, often descriptive prose rather than a literal path; pointers = agentContext.authoringReview.pointers (tightened to explicit file/field references on exactly 4 gates — crs-02, crs-03, crs-04, crs-05 — during the 0.10.2-0.10.5 agentContext build; every other gate's pointers is original and loosely mirrors generation.sources, not independently re-verified beyond what is reproduced here); checks = agentContext.validation.checks ids (declared, see Part C of original-pathway-gating-lookups.md for enforcement status); sourceConsultation = the gate's sourceConsultation object, where set.

ONB — onboarding (reworked, design status, not in the live store)
ONB decides what is being built and which pathway it is built from. The gates are the same on both routes. The route changes what onb-05_pitch does, how much SDEF covers and what follows SDEF.

Routes from onb-01_mode:

single-course          ONB (onb-01 to onb-06) > CXS > SDEF (sdef-01 if tier > sdef-02 > sdef-03 if context > sdef-04 > sdef-05) > course gates from crs-02
pathway-proliferation  ONB (onb-01 to onb-06) > CXS > SDEF (sdef-01 > sdef-02 > sdef-03 if context > sdef-04 > sdef-05) > course gates from crs-02, once per tier

seq	gate id	phase	hardness	kind	deps	generation.sources / pointers	checks	sourceConsultation
0	onb-01_mode	ONB	hard-stop	human	—	none, this is a routing choice. Options: single-course | pathway-proliferation	—	—
1	onb-02_sources	ONB	hard-stop	human	onb-01	—	—	—
2	onb-03_thematic-pack	ONB	hard-stop	human	onb-02 (order only)	catalogue/pathways.json (the pathways pack, selected by default). Other packs, such as a module or programme pack, could be offered here	—	—
3	onb-04_thematic-pathway	ONB	hard-stop	agent+human	onb-03, onb-02	sources: the pack loaded at onb-03 (catalogue/pathways.json) | onb-02 source set: pathway core Part A + source-map (prose) | user-uploaded sources and context from onb-02, which alone supply the theme on the no-preset path. pointers: onb-02_sources ;; design-kb.pathways.json (pathways[].chapters, bookChunks.primary/shared, tiers.<tier>.voiceBand)	SCP-1, STR-1, TW-1 (shared with crs-02, to review)	{triggeringFacets:["level"], authorityLevels:["sector"]}
4	onb-05_pitch	ONB	hard-stop	agent+human	onb-04	design-kb/design-kb.tier-bands.json (tier↔FHEQ relation, cognitive-demand notes) | catalogue/context/pathway/<pathway>.json (both axes independently: tierProgression.levels L3-L8, tierProgression.tierStatements, masteryNote, capabilities[] each with tier+fheqLevel) | same file's bookGrounding | catalogue/context/subject/benchmarks/universal-reference.json (tierReadings.rows, pathwayMapping['adapt-<pathway>'])	—	—
5	onb-06_naming	ONB	hard-stop	agent+human	onb-04, onb-05	—	—	—
What each gate does:

gate	replaces	what happens	produces
onb-01_mode	new	The user chooses between one Adapt course, with a specific tier in mind or none, and a three-tiered course built all at once (the pathway-distillation profile in gate-profiles.json).	the route
onb-02_sources	crs-01_sources	The user uploads sources and context, on either route.	the source set
onb-03_thematic-pack	onb-01_theme-preset	The user selects the pack to work from, with pathways as the default. The gate only loads the pack, so it does not use the onb-02 outcome.	the active pack
onb-04_thematic-pathway	onb-02_course-theme	The user selects one theme from the pack, which in the pathways pack means one academic practice. The agent reads up on that pathway's book material and tier information so that all tiers can be considered together, and takes the onb-02 sources into account.	the chosen pathway, with its book and tier read-up
onb-05_pitch	onb-03_pitch	On single-course, sets the tier, which can be none. On pathway-proliferation, the user has already chosen all three tiers, so the agent reviews the pitch across them and carries that review into sdef-05_shell-definition.	the tier, or the all-tier pitch review
onb-06_naming	onb-04_naming	Unchanged in purpose.	the course name
CXS — context shell
Any subject, qualifier or other shell context is optional and is defined here, not in ONB. The rows below are still the live auto-pass placeholders (see the open decisions under SDEF).

seq	gate id	phase	hardness	kind	deps	generation.sources / pointers	checks	sourceConsultation
6	cxs-01_institutional-context	CXS	advisory	auto	—	—	—	—
7	cxs-02_subject-context	CXS	advisory	auto	—	—	—	—
8	cxs-03_qualifiers	CXS	advisory	auto	—	—	—	—
9	cxs-04_referencing-style	CXS	advisory	auto	—	—	—	—
10	cxs-05_external-standards	CXS	advisory	auto	—	—	—	—
11	cxs-06_resources	CXS	advisory	auto	—	—	—	—
SDEF — Shell Definition (new, design status, not in the live store)
SDEF runs after CXS because it depends on whatever context CXS holds. The agent looks up the tier definitions and benchmarks, blends them with any context, agrees the definitive set with the user, and writes the statement of shell context that it will refer to when authoring. All five gates are C/A/R: the agent proposes, and the user confirms, amends or asks it to regenerate with new instructions.

SDEF runs on both routes. pathway-proliferation covers all three tiers, so the full 9 benchmarks and 18 outcomes. single-course covers its own tier, so that tier's 3 benchmarks and 6 outcomes. If its tier is none, it skips sdef-01 and works from the full 9 and 18. The 18 is the starting set rather than a fixed total, so the number agreed at sdef-04 can differ.

seq	gate id	phase	hardness	kind	deps	generation.sources / pointers	checks	sourceConsultation
12	sdef-01_tier-definitions	SDEF	hard-stop when it runs	agent+human	onb-04, onb-05, CXS closed (skipped on single-course with tier none)	design-kb/design-kb.tier-bands.json | catalogue/context/pathway/<pathway>.json (tierProgression.levels, tierProgression.tierStatements, masteryNote) | catalogue/context/subject/benchmarks/universal-reference.json (tierReadings.rows) | design-kb.pathways.json (tiers.<tier>.voiceBand)	—	—
13	sdef-02_thematic-benchmarks	SDEF	hard-stop	agent+human	onb-05, CXS closed, sdef-01 if it ran	catalogue/context/pathway/<pathway>.json (capabilities[], the 9) | catalogue/context/pathway-evidence/<pathway>.json (the 18)	—	—
14	sdef-03_context-benchmarks	SDEF	hard-stop when it runs	agent+human	sdef-02, cxs-02, cxs-03 (skipped if CXS holds no subject or qualifier context)	In grow-generator-component/context-sources/ (see Part F): benchmark ids held in CXS, from schools/<school>/courses/<slug>.json (benchmarks.links[]) or subject-contexts.json | benchmark-maps/<id>.map.json, or <id>.pilot-map.json for the 3 pilots (pathways['adapt-<pathway>']: benchmark statements to pathway). Universal set: catalogue/context/subject/benchmarks/universal-reference.json (pathwayMapping['adapt-<pathway>'], location to confirm) | standing standards registry | onb-02 source set	—	—
15	sdef-04_definitive-set	SDEF	hard-stop	agent+human	sdef-02, sdef-01 and sdef-03 if they ran	the closed records of sdef-01, sdef-02 and sdef-03 | catalogue/context/pathway/<pathway>.json (tierProgression.tierStatements, masteryNote) | grow-generator-component/context-sources/lens.json (pathways[<pathway>].rows, for identity)	—	—
16	sdef-05_shell-definition	SDEF	hard-stop	agent+human	sdef-04, onb-05	the closed records of onb-02, onb-03, onb-04, onb-05, CXS and the SDEF gates that ran	—	—
What each gate does:

gate	what happens	produces
sdef-01_tier-definitions	On pathway-proliferation, the agent looks up the definitions of all three tiers. The course presents a full learning pathway from introductory to advanced and raises the learner through those levels, so every tier is key context. On single-course, it looks up the chosen tier only.	the agreed tier definitions
sdef-02_thematic-benchmarks	The agent looks up the pathway's benchmarks and learning outcomes for the route's scope and presents them grouped loosely into level bands: L4 (few if any), L5, L6 and L7. The user deals with any that are unsuitable or need changing.	the agreed pathway benchmarks and outcomes
sdef-03_context-benchmarks	Runs only if CXS holds subject or qualifier context. The course's HECoS mapping points to the benchmarks of its subject or grouping, which are already broken down and mapped to the pathways and to the universal benchmark set. The agent pulls these together with any standards groupings and other defined content sources, and presents the matches against the pathway benchmarks, showing where a subject makes clear the importance of a benchmark or of the pathway. It then proposes any merging or rewriting that blends the benchmarks and outcomes with that context.	recorded alignments, signposted for later gates, and the proposed blended benchmarks and outcomes
sdef-04_definitive-set	The agent proposes, and discusses with the user, the definitive 9 benchmarks and the definitive learning outcomes in their tier groupings. It rules on the fuzzy tops and reviews the learning journey that results. See Appendix 1, 1.3.	the definitive 9 and outcomes, tier groupings, fuzzy-top rulings and journey review
sdef-05_shell-definition	The agent writes the shell context definition statement, which it refers to when authoring. It records what sdef-04 agreed and makes no new decisions. See Appendix 1, 1.5, for its contents.	the shell context definition statement
Open decisions on ONB, CXS and SDEF:

Connecting the subject context (in progress). cxs-02_subject-context and cxs-03_qualifiers are still advisory, auto-pass placeholders. The data is on its way in grow-generator-component/context-sources/: HECoS mappings link courses to the benchmarks of a subject or grouping, and all 54 benchmarks are mapped to the 13 pathways. What remains is pulling these together, so that CXS records the subject for sdef-03 to use. Three limits apply:
The 239 course assignments are proposed from course titles (192 clear, 40 weak, 7 unassigned), not taken from the university's HESA returns.
A benchmark link shows a shared code, not that the benchmark governs the course. 45 of the 78 school subject groups have no core benchmark link and need a person to judge them.
Every statement in the benchmark maps is still proposed.
Later subject choices. cxp-01_subject and cxp-02_qualifiers also choose a subject and qualifiers after the lessons, so they need to reuse anything set in CXS rather than ask again.
What the 18 are. The table points to pathway-evidence/<pathway>.json, which holds 18 evidence examples per pathway (6 per tier). If the 18 learning outcomes are a new set, they need their own source. The total no longer has to reach 18, so the settled 5/5/6 criticality split (16 outcomes under "flat 6") is allowed.
Level bands. The bands start at L4, but capabilities can sit at L3 (i1 in criticality.json).
Overlap with the design profiles. SDEF covers much of fork01-benchmarks, ao-02, fork02-shell and ao-04. Part A has not been updated to say which steps it replaces.
CRS — course
Both routes enter CRS at crs-02_thematic-scope. sdef-05_shell-definition feeds crs-02 and crs-03, and through crs-03 the courseOutcomeBanks that wra-03 and wra-04 read. The pathway choice itself has moved to onb-04.

crs-04_lesson-map is where the user signs off the final lesson structure and outcome mapping, once per tier on pathway-proliferation. The agent proposes, and the user confirms or amends, on these rules:

Minimum: 5 lessons, on both routes.
Default: one lesson per outcome. This is the first layer of alignment, so a tier with more outcomes normally gets more lessons.
Starting point: the agent starts with more lessons rather than fewer, because it is easier to come down from more at review.
Content shape: decides the final structure, as it always has (design-kb.content-shapes.json).
Flexibility: a lesson can support more than one outcome where that makes pedagogical sense, and the agent records why. It is not strict that every outcome has a lesson. Coverage is reviewed as part of the CRS stage.
The user can also change the outcomes here. They can reword, merge, regenerate or remove any outcome, and this is their decision. It does not reopen sdef-04. Instead:

The crs-03 banks follow: a changed outcome's bank is regenerated, and a removed outcome's bank is removed.
The change is recorded in the sdef-05 statement as a new revision, with the reason. The statement does not go back for review.
Later gates use the outcomes as they stand when crs-04 closes.
On pathway-proliferation, progression-signposting re-checks the learning journey after all three lesson maps, using the journey checks in Appendix 1, 1.3. It flags any gap or jump for the user to decide.
Build notes from tools/manifest-completeness.js (local copy, which may be older):

CO-1 needs relaxing. It fails if any course outcome is served by no lesson, which conflicts with not requiring a lesson for every outcome. It should accept an outcome with no lesson if the user's decision is recorded.
Changes at crs-04 must be written back to the crs-03 record. CO-1, AL-3b and AL-4 all read the course outcomes from crs-03, so they would otherwise check the old set.
Flexibility needs no new data shape. A lesson holds a list of outcomes, each with its own serves, so one lesson can already support several course outcomes.
seq	gate id	phase	hardness	kind	deps	generation.sources / pointers	checks	sourceConsultation
17	crs-02_thematic-scope	CRS	hard-stop	agent+human	sdef-05	sources: the sdef-05 statement | onb-02 source set: pathway core Part A + source-map (prose). pointers (tightened): sdef-05_shell-definition ;; onb-02_sources ;; design-kb.pathways.json (pathways[].chapters, bookChunks.primary/shared, tiers.<tier>.voiceBand)	SCP-1, STR-1, TW-1	{triggeringFacets:["level"], authorityLevels:["sector"]}
18	crs-03_course-outcomes	CRS	hard-stop	agent+human	crs-02, sdef-05	sources: the outcomes agreed at sdef-04 and recorded in the sdef-05 statement, one course outcome and bank for each (D5 in Part E) | thematic scope | pathway core A10 capabilities (prose). pointers (tightened): sdef-05_shell-definition ;; crs-02_thematic-scope ;; catalogue/context/pathway/<pathway-id>.json (capabilities[].capabilityId, the A10 core-capability crosswalk)	AL-2, AL-4	—
19	crs-04_lesson-map	CRS	hard-stop	agent+human	crs-03, crs-02	sources: course outcomes | thematic strands | source search (prose, not paths) | design-kb.content-shapes.json. pointers (tightened): onb-02_sources ;; crs-02_thematic-scope ;; crs-03_course-outcomes	AL-1, AL-2	—
20	crs-05_course-spec	CRS	advisory	agent+human	crs-04	sources: all closed ONB+SDEF+CRS records (prose). pointers (tightened): onb-03_thematic-pack ;; onb-04_thematic-pathway ;; onb-05_pitch ;; onb-06_naming ;; cxs-04_referencing-style ;; onb-02_sources ;; sdef-05_shell-definition ;; crs-02_thematic-scope ;; crs-03_course-outcomes ;; crs-04_lesson-map	AL-1, AL-2	—
LES — lesson
seq	gate id	phase	hardness	kind	deps	generation.sources / pointers	checks	sourceConsultation
21	les-01_lesson-proposal	LES	soft	agent+human	crs-04, crs-02	pathway core A10 templates + Part C process | onb-02 source set	—	{triggeringFacets:["activity"], authorityLevels:["institutional"]}
WRA — wrappers
seq	gate id	phase	hardness	kind	deps	generation.sources / pointers	checks	sourceConsultation
22	wra-01_wrapper-open	WRA	soft	agent+human	crs-03, crs-04	onb-02 source set | pathway core A10 professional equivalences	—	—
23	wra-02_wrapper-close	WRA	soft	agent+human	crs-03, crs-04	onb-02 source set | pathway core A9 Relations + adapt-integration overlap | catalogue/pathways.json (tier ladder)	—	—
24	wra-03_summative	WRA	soft	agent+human	crs-03, crs-04	crs-03 courseOutcomeBanks (the 3 mcqSet specs per outcome) | onb-02 source set | pathway core	—	—
25	wra-04_confidence	WRA	soft	agent+human	crs-03	crs-03 courseOutcomeBanks (confidenceStatement per outcome)	—	—
CXP — context pack
seq	gate id	phase	hardness	kind	deps	generation.sources / pointers	checks	sourceConsultation
26	cxp-01_subject	CXP	hard-stop	human	—	—	—	—
27	cxp-02_qualifiers	CXP	hard-stop	human	—	—	—	—
28	cxp-03_exemplar-programmes	CXP	advisory	auto	—	—	—	—
29	cxp-04_context-generation	CXP	soft	agent+human	cxp-01, les-01, wra-01, wra-02, wra-03	subject benchmark corpus (adapt-integration benchmark search patterns) | baseline subject (cxp-01=baseline): catalogue/context/subject/benchmarks/universal-reference.json | standing standards registry | cxs-04 referencing | onb-02 source set	—	{triggeringFacets:["level","institution","faculty","activity"], authorityLevels:["sector","institutional"]}
Part E — complete routing (proposed for build)
The status column shows what has been agreed and what is still a proposal. The decisions below the table record what has been settled.

Run state the routing reads: route, pack, pathway, tier, subject (optional), qualifiers (optional).

order	gate	single-course	pathway-proliferation	skip or branch	status
1	onb-01_mode	sets route	sets route	—	agreed
2	onb-02_sources	runs	runs	—	agreed
3	onb-03_thematic-pack	runs	runs	—	agreed
4	onb-04_thematic-pathway	runs	runs	—	agreed
5	onb-05_pitch	sets tier, which can be none	agent reviews the pitch across all tiers	—	agreed
6	onb-06_naming	one course name	one name for each tier's course	—	proposed
7	cxs-01 to cxs-06	runs once	runs once, shared across tiers	sets optional subject and qualifiers	agreed, not built
8	sdef-01_tier-definitions	chosen tier	all three tiers	skip if tier is none	agreed
9	sdef-02_thematic-benchmarks	that tier's 3 and 6, or all 9 and 18 if tier is none	all 9 and 18	—	agreed
10	sdef-03_context-benchmarks	runs for the same scope	runs for the same scope	skip if no subject and no qualifiers	agreed
11	sdef-04_definitive-set	that tier's benchmarks and outcomes, or the full set with no tier grouping if tier is none	all 9 and the definitive outcomes, with fuzzy tops and journey review	—	agreed
12	sdef-05_shell-definition	runs	runs	—	agreed
13	crs-02, crs-03	once	once per tier	fed by sdef-05; crs-03 holds courseOutcomeBanks	agreed; shape in D5
14	crs-04_lesson-map	once, at least 5 lessons, one per outcome by default	once per tier, at least 5 lessons, one per outcome by default	reads crs-02 and crs-03, as in the live flow; content shape decides the final structure, and the user signs off the lessons and outcome mapping	agreed
15	progression-signposting	skip	once, after all three lesson maps	planned, no generator yet; re-checks the journey against the outcomes as changed at crs-04 and flags gaps for the user	Part A profile; re-check agreed
16	crs-05_course-spec	runs	skip	as listed in Part A	Part A profile
17	les-01_lesson-proposal	once per lesson	once per lesson, per tier	—	Part A profile
18	wra-01 to wra-04	once	once per tier	read crs-03 banks, as in the live flow	agreed
19	cxp-01 to cxp-04	once	once, merged into all three tiers	cxp-01 and cxp-02 reuse CXS, and ask only if nothing was set	agreed
The main addition to Part D is the fan-out at steps 13 to 18: after one shared definition, pathway-proliferation runs the course gates once for each tier, because each tier is its own Adapt course.

Decided (3 November 2026):

D1: crs-02 and crs-03 stay, fed by sdef-05. Both routes go from sdef-05 to crs-02. This reverses a brief decision the same day to drop them.
D2: wra-03_summative keeps its live rule of two questions per course outcome, reading courseOutcomeBanks on crs-03.
D3: cxp-01 and cxp-02 reuse anything set in CXS, and ask only if nothing was set.
D4: a subject with no linked benchmark. Benchmarks for the remaining subjects are coming. Until then the flow behaves as the original does, and as a further fallback the user will supply the subject's .md benchmark.
D5 (4 November 2026): each agreed outcome becomes one course outcome on crs-03, with its own bank. The outcomes stay flat, as the "flat 6" ruling says, rather than being distilled. The live limit of 3 to 5 course outcomes gives way to the number agreed at sdef-04, because D7 lets a tier exceed 6. At two questions per course outcome, a tier of 5 or 6 has 10 to 12 summative questions, and more above that.
D6: the new gate is sdef-04_definitive-set, and the statement becomes sdef-05_shell-definition.
D7: 18 is the starting set, not a fixed total. Each tier on pathway-proliferation needs at least 5 outcomes, and the upper tiers can go above 6 with a recorded reason.
D8: lesson structure. The minimum is 5 lessons, on both routes. The default is one lesson per outcome, as the first layer of alignment, so more outcomes normally mean more lessons. The agent starts with more lessons rather than fewer, because it is easier to come down at review. Content shape decides the final structure, and a lesson can support more than one outcome where that makes pedagogical sense. Not every outcome has to have a lesson: coverage is reviewed in CRS, and the user signs off the lessons and outcome mapping at crs-04_lesson-map.
D9 (4 November 2026): the outcomes stay open at crs-04_lesson-map. The user can reword, merge, regenerate or remove them there, without reopening sdef-04. The crs-03 banks follow, and the sdef-05 statement records the change as a new revision. On pathway-proliferation, progression-signposting then re-checks the journey and flags gaps for the user to decide.
Part F — query paths and data bridges
Measured on 3 November 2026 from grow-generator-component/context-sources (G: below) and wkspc2614-adapt3 (A: below).

The whole chain:

course ──> HECoS/CAH ──> benchmark id ──> benchmark map ──> pathway statements
                              │                                    │
                              └── readings by row ──> row <── pathway capabilities
                                                       │
                                  phrase families <────┘

F1. The keys that bridge the data
Most of the confusion comes from the same thing having different ids in different files. Each id below is the form to convert to before joining.

thing	canonical key	other forms	how to convert
Pathway	criticality	adapt-criticality (maps)	add or strip adapt-
Row (tier and level position)	i1-i3, d1-d3, e1-e3	also F and L8 in the lens	same in all files
Capability or card	rowId plus pathway	criticality/02 (capabilityId, cardId)	look up by row, because this id can be null
Benchmark	accounting-2025	qaa/accounting-2025 (maps)	add or strip qaa/
Benchmark passage	qaa/accounting-2025/1.9	—	chunkId in a map statement
Course	csad/animation-ba-hons-degree	course title	id in the course file
Subject	HECoS 100057	CAH3, CAH2, CAH1 codes	G:hesa-hecos-cah.json
Phrase family	function/hedge-a-claim	—	lens.json families key
The row is the most useful bridge. It is the one key shared by the pathway capabilities, pathway readings, benchmark readings and phrase families.

F2. One source for each question
question	use	do not use	why
What benchmarks does this course have?	G:schools/<school>/courses/<slug>.json (benchmarks)	tools/resolve-subject-benchmark.js, when a course is known	the resolver walks up CAH ancestors and differs (see F4)
What benchmark fits this subject, with no course?	A:tools/resolve-subject-benchmark.js, shown as a proposal	—	the only route from a free subject name
What contexts does this school have?	G:subject-contexts.json (60 graded contexts)	G:cardiff_met_school_context.json, except for rankings	it groups subjects for choosing and grades them
How does a benchmark map to a pathway?	G:benchmark-maps/<id>.map.json (pathways['adapt-<pathway>'])	pathwayMapping in A:catalogue/context/subject/benchmarks/<id>.json	that field is empty in 53 of 54 files, and the Psychology one is superseded
What does a subject mean at a given row?	A:catalogue/context/subject/benchmarks/<id>.json (tierReadings.rows)	—	the source of those readings
What are the pathway's benchmarks?	A:catalogue/context/pathway/<pathway>.json (capabilities[])	—	the source of those statements
What are the 18?	catalogue/context/pathway-evidence/<pathway>.json	—	not on this machine
What are the tier and level definitions?	A:catalogue/context/pathway/<pathway>.json (tierProgression)	—	specific to the pathway
What does the book say?	A:source-kb/source-maps/book-excelling-at-university-2026.json (chunks), with chapters from A:catalogue/pathways.json	—	the source map
G:lens.json is an index, not a source. It already joins pathway readings, benchmark readings, contexts and phrase families by row, which makes it the fastest first read. The agent should use it to find what matters, then cite the underlying file. Its own note calls it a working join of drafts.

F3. Query path for each gate
gate	input	path	output
onb-03	—	A:catalogue/pathways.json	the pack's 13 pathways
onb-04	pathway	A:catalogue/pathways.json (chapters, file) > A:catalogue/context/pathway/<pathway>.json (identity, bookGrounding, tierProgression) > book chunks	pathway and book read-up
onb-05	pathway, tier	tierProgression (tierStatements, levels, masteryNote) > A:catalogue/context/shared/cross-cutting.json (tierModel, genericLadder)	pitch, or all-tier review
CXS: by course	course	G:schools/<school>/courses/<slug>.json (hesa, benchmarks.links[])	subject, benchmark ids, core or specialism
CXS: by school	school	G:subject-contexts.json (schools[].contexts[], with grade, benchmarks, courseIds)	subject, benchmark ids, grade
CXS: by subject	name or HECoS	A:tools/resolve-subject-benchmark.js	a proposed benchmark, or a recorded gap
sdef-01	pathway, route, tier	tierProgression > G:lens.json (rows, for row to tier and level)	tier definitions
sdef-02	pathway, scope	capabilities[] by rowId > G:lens.json (pathways[<pathway>].rows: practice, knowledge, identity) > pathway evidence (the 18)	benchmarks and outcomes in level bands
sdef-03	benchmark ids, pathway	G:lens.json (benchmarks[<id>].pathways[<pathway>]: coverage, summary) > the map's statements (chunkId, extract, strength, agentInstruction) > tierReadings.rows by row	alignments with their evidence, and the proposed blend
sdef-04	closed records of sdef-01 to sdef-03	the proposed 9 and outcomes > rows for row to tier and level (the fuzzy tops) > tierStatements, masteryNote and lens identity (the journey)	the definitive set, tier groupings, rulings and journey review
sdef-05	closed records	the records of the gates that ran	the shell statement, with a pointer to each source
crs-02, crs-03	sdef-05	the statement's pointers > its agreed outcomes	scope, course outcomes and courseOutcomeBanks
crs-04, les-01	crs-03, sdef-05	the statement's pointers > book chunks > map statements for the pathway	lessons grounded in the agreed outcomes
Authoring (optional)	pathway, row	G:lens.json (families, whose serves lists pathway and row) > G:packs/	phrasing suited to the row
F4. Traps found while testing the joins
The two course-to-benchmark routes disagree. Over all 239 courses, comparing the course files with the resolver:

result	courses
share at least one benchmark	146
neither finds one	29
resolver finds one, course file has none	47
no benchmark in common	14
course file has one, resolver finds none	3
For example, the course file for Criminal Justice and Security links social-policy-2026, and the resolver returns public-policy-and-public-administration-2025.

Subject readings stop at honours level. Across the 54 benchmarks, readings exist for d3 (52), e2 (52), e3 (39) and d2 (1), and for no other row. A join by row therefore gives the introductory tier and d1 no subject reading. Blends at those rows need to use the map's statements, which are tagged by pathway and not by row.

capabilityId is often null. In the lens, e3 has no card id in 9 of 14 pathways, and i1 and i3 have none in 7. This is why joins should use the row. The null has a meaning: the id is the card's old id in G:cards/plans/<pathway>.yaml, and the 40 of 126 cards without one are new, so null does not mean missing data.

13 or 14 pathways. The lens and the card files include self-development, but catalogue/pathways.json has 13. Its term list is marked candidate, so routing should offer the 13 until it is promoted.

Benchmark maps do not all hold every pathway. All 54 maps list 14 pathways in coverage, but pathways leaves out any marked none (45 cases). A lookup should read coverage first, and treat none as a finding that the benchmark says nothing on that pathway.

Benchmark coverage is partial. Of the 239 course files, 94 have a core benchmark, 69 a specialism and 76 none. Subject contexts are graded 26 solid, 24 usable and 10 needing a benchmark.

G:schools/index.json is invalid JSON. It has a syntax error at line 23, so a build that reads it will fail. Nothing in these paths needs it.

F5. Named in this document but not found on this machine
design-kb/ (including gates.json, gate-profiles.json, pathways.json and tier-bands.json), catalogue/context/pathway-evidence/ (the 18), catalogue/context/subject/benchmarks/universal-reference.json, benchmarkKeys in the pathway files, and gate-experiment/. wkspc2614-adapt3 here is not a git checkout, and its pathway files predate some of this work, so the paths above need rechecking against the current copy before they are built on.

F6. Interim sources (4 November 2026)
The finished pathway data is being worked on elsewhere and is not wired up yet. Until it is, SDEF reads from grow-generator-component. Each gate keeps the same job, so wiring up the finished data only changes where it reads from. Paths are under G: as above, except analysis/, which sits beside context-sources.

gate	use for now	what it gives	stands in for
sdef-01	G:cards/ing-cards-<pathway>.md, sections 3a and 4a	tier statements with knowledge type, process and what changes; mastery note; the tier map	tierProgression
sdef-02, the 9	G:cards/ing-cards-<pathway>.md, section 1	card statement by row, verbs, measures, keywords, book topics with pages, pedagogy, frameworks	capabilities[]
sdef-02, the outcomes	Drafted by the agent, row by row, from section 1 and G:cards/wide/pathway-readings.yaml (practice, knowledge, identity). Marked interim	a working set to review at sdef-04	the finished 18
sdef-03	G:schools/<school>/courses/<slug>.json > G:benchmark-maps/<id>.map.json > G:cards/wide/benchmarks/<id>.yaml (rows)	the subject link, statements by pathway, subject readings by row	as F2, with the readings read from their source
sdef-03, by row	the card's Benchmark evidence row	a row-level benchmark link, which the maps do not give. 65 of the 126 cards say "not searched"	—
sdef-04, the journey	section 3a and the identity readings	the checks in Appendix 1, 1.3	tierStatements, lens identity
Traps in these sources:

The 9 have two wordings, on purpose. Each card has a full statement, in ing-cards-<pathway>.md, and a short form, in G:cards/plans/<pathway>.yaml. capabilities[] and lens.json use the short form, which matches capabilities[] on all 117 rows of the 13 pathways. Only 20 of the 117 full statements match it exactly. For now the full statement is the benchmark, and the short form is its label, always joined on the row. A few differ in meaning and need checking at sdef-02: criticality/d3 is "Critically engage with a journal article's structure and methodology" in full and "Read a journal article strategically by its structure and method" in short.
The cards are drafts. Each says "working draft; not ingested", and each has a "For review" section listing cards that are still proposed.
The cards do not hold outcomes. Interim outcomes therefore have no agreed source, and the source register must show them as interim.
The ready-made lookup is scripts/build_lens.mjs. Most of the sdef-03 join already exists:

node scripts/build_lens.mjs "<context>" <pathway> <row> [school]

Run from grow-generator-component, this prints the card, the pathway readings, the subject readings, what QAA says on that pathway with its coverage, and the phrase families. For "Law" criticality d3 csm it returns all of these. Three limits apply: it takes a subject context title from subject-contexts.json, not a course, it reads the short form of the card, and it needs ../wkspc2614-adapt3/catalogue/context/correspondences.json to run.

script	use
build_lens.mjs (no arguments), or npm run build-lens to include the page	rebuilds lens.json from the cards, readings, maps and contexts. Rebuild after any of them change
subject_contexts.mjs	recounts and grades the contexts in subject-contexts.yaml
school_context.mjs, map_courses.py	build the school context and the course to HESA map
lens_trial.mjs <trial>	builds a worked trial like LENS-TRIAL-LAW-CRITICALITY.md
check_family_lens.mjs	checks that the phrase family map points to real pathways and rows
The other scripts build and check the phrase generator, and SDEF does not need them.

G:../analysis/ is for reference, not for lookups. These are generated reports, and some are marked internal only.

file	use
LENS-TRIAL-LAW-CRITICALITY.md	a worked example of a row-by-row lookup for one subject and pathway
SUBJECT-CONTEXTS.md, SCHOOL-CONTEXT.md, COURSE-HESA-MAP.md	readable views of the context data, for checking a CXS choice
CONTEXT-EXAMPLES-DEMO.md, HESA-OUTCOMES.md, HESA-OUTCOMES-STRUCTURAL.md	phrasing examples for authoring. Their "outcomes" are worked sentences, not learning outcomes
Appendix 1 — sdef-04_definitive-set and sdef-05_shell-definition specification (draft for review)
1.1 Purpose
sdef-05 produces the shell definition statement: the one document that records what the agent has been given, what has been agreed and what it intends to build. The agent refers to it when authoring, and the course gates read from it.

It records decisions and does not make them. The definitive benchmarks, outcomes and tier groupings are agreed at the gate before it (1.3).

1.2 Where it sits
sdef-01 tier definitions > sdef-02 pathway benchmarks > sdef-03 context benchmarks (if context)
    > sdef-04 definitive set (1.3) > sdef-05 shell definition > crs-02 > crs-03 banks > crs-04 sign-off

route	scope of the statement
pathway-proliferation	all three tiers, the full 9 and the definitive outcomes, the fuzzy tops and the whole learning journey
single-course with a tier	that tier's 3 benchmarks and its outcomes, plus what comes before and after it in the pathway
single-course with tier none	the full 9 and the outcomes as a reference set, with no tier grouping or journey review
1.3 The gate before it: sdef-04_definitive-set
The gate runs on both routes and is never skipped. The agent proposes, the user and agent discuss it, and the user confirms, amends or asks the agent to regenerate with new instructions.

agreed here	how
The definitive 9	each benchmark is the pathway's own, or the blended version proposed at sdef-03
The definitive outcomes	starting from the 18, each outcome is the original, reworked for the subject context, or added. 18 is not a fixed total
Tier groupings	outcomes are grouped by tier, normally 5 or 6 per tier, with more allowed in the upper tiers
Fuzzy tops	every outcome near a tier boundary is placed by a recorded ruling (see below)
The learning journey	the agent shows the journey that results, and the user reviews it (see below)
Fuzzy tops. The tiers overlap in level by design. All 13 pathway files use this pattern:

level	introductory	intermediate	advanced
L3	i1		
L4	i2	d1	
L5	i3	d2	e1
L6		d3	e2
L7			e3
So the top of one tier sits at the same level as the middle or base of the next. An outcome near that overlap could reasonably sit on either side. For each boundary, the agent:

Lists the outcomes that could sit on either side.
Recommends a tier for each, with its reason, such as the kind of knowledge or the demand it makes on the learner.
Records the user's ruling. An outcome can be placed in one tier and signposted from another.
Journey review. The agent lays the outcomes out in order and checks:

check	what it looks for
Rising demand	the weight moves along the tierStatements type and process values and matches masteryNote
Continuity	each tier builds on the one before, with no jumps, and nothing depends on a later outcome
No repeats	an outcome appearing twice is either merged or deliberately revisited at greater depth
Balance	conceptual and applied outcomes are both present in each tier
Coverage	the pathway's book sections and any subject alignments are represented
Learner identity	the identity readings in lens.json form a believable progression
The gate fails to close if: any of the 9 is missing, a tier has fewer than 5 outcomes (pathway-proliferation only), a fuzzy top has no ruling, or a journey check is left unresolved. A tier above 6 outcomes needs a recorded reason. This relaxes the 6-lesson ceiling in Part A, and it applies to the upper tiers only. Extra outcomes are added, not taken from a lower tier, though a fuzzy-top ruling can still move one across a boundary if the tier keeps at least 5. The final lesson structure and outcome mapping are signed off later, at crs-04_lesson-map, where the user can still reword, merge, regenerate or remove outcomes.

1.4 Inputs
from	what it supplies
onb-02 to onb-06	sources, pack, pathway, pitch review, course name
CXS	optional subject and qualifiers, frameworks, referencing style
sdef-01	tier definitions
sdef-02	pathway benchmarks and outcomes
sdef-03, if it ran	alignments, signposts and proposed blends
sdef-04	the definitive 9 and outcomes, tier groupings, fuzzy-top rulings, journey review
1.5 Contents of the statement
Sections are always present and in this order. A section with nothing to record says so.

Section 1: Header
Pathway:        <pathway id and name>
Route:          single-course | pathway-proliferation
Tier scope:     <tier> | none | all three
Course name(s): <one per tier's course>
Subject:        <benchmark ids, HECoS code, core | specialism> | none
Qualifiers:     <list> | none
Status:         proposed | confirmed
Generated:      <date>, revision <n>

Section 2: Source register
Every source the agent drew on, listed by type. Each row is one file or field actually used. Anything cited later in the statement must have a row here.

ref	group	source	file	field or selector	version or date	status	used for
T1	Theme: pack	Pathway pack	catalogue/pathways.json	pathways[id=<pathway>]	pathwaysVersion	live	pathway, chapters
T2	Theme: pathway	Pathway reference	catalogue/context/pathway/<pathway>.json	capabilities[], bookGrounding	<date>	<status>	the 9
T3	Theme: tiers	Tier progression	same file	tierProgression	<date>	<status>	tiers, journey
T4	Theme: outcomes	The 18, or interim outcomes until they are wired up (F6)	catalogue/context/pathway-evidence/<pathway>.json, or the agent's draft from context-sources/cards/	all	<date>	drafted or interim	the outcomes
T5	Theme: book	Book source map	source-kb/source-maps/book-excelling-at-university-2026.json	chunks[<ids>]	kbVersion	<status>	book grounding
T6	Theme: index	Lens	context-sources/lens.json	pathways[<pathway>].rows	<date>	working draft	readings by row
C1	Context: course	Course file	context-sources/schools/<school>/courses/<slug>.json	hesa, benchmarks	<date>	proposed	subject link
C2	Context: school	Subject context	context-sources/subject-contexts.json	schools[].contexts[]	<date>	draft, <grade>	subject link
S1	Subject: mapping	Benchmark map	context-sources/benchmark-maps/<id>.map.json	pathways['adapt-<pathway>'].statements	mapVersion	proposed	alignments
S2	Subject: readings	Benchmark reference	catalogue/context/subject/benchmarks/<id>.json	tierReadings.rows, digest	edition	<status>	subject readings
S3	Subject: universal	Universal set	catalogue/context/subject/benchmarks/universal-reference.json	pathwayMapping['adapt-<pathway>']	<date>	<status>	generic set
Q1	Qualifier	Qualifier source	<ingest file>	<selector>	<date>	<status>	qualifier context
F1	Framework	Frameworks	catalogue/context/shared/cross-cutting.json	frameworks	crossCuttingVersion	live	level grounding
U1	User	Uploaded source	<name>	<section>	<date>	user-supplied	<purpose>
The S rows also cover a user-supplied .md benchmark, recorded as user-supplied. Until the finished data is wired up, T2 and T3 read from context-sources/cards/ing-cards-<pathway>.md, and S2 from context-sources/cards/wide/benchmarks/<id>.yaml (Part F, F6).

Section 3: Understanding and intent
Prose, voice-linted with voice-lint.js. It covers what this context means for the shell, who the learner is, whether the full journey is being built in one, and what is out of scope.

Section 4: Tier definitions
tier	levels	definition	what changes in this tier	source
Introductory	<range>	<definition>	<movement from masteryNote>	T3
Intermediate	<range>	<definition>	<movement>	T3
Advanced	<range>	<definition>	<movement>	T3
Section 5: The definitive 9 benchmarks
row	tier	level	pathway benchmark (original)	definitive benchmark	change	why	sources
i1	Introductory	L3	<statement from capabilities[]>	<wording>	unchanged, aligned or rewritten	<reason, or none>	T2, S1:<chunkId>
There is one row for each of i1 to e3, joined on the row, because capabilityId can be null.

Section 6: The definitive learning outcomes, by tier
One table per tier, with a count in the heading:

Introductory: <n> outcomes

id	outcome	benchmark row	kind	level	source wording	change	sources
<pathway>-i-01	<wording>	i1	conceptual or applied	L3	<original, or none if added>	unchanged, reworked for <context>, or added because <reason>	T4, T5:<chunk>, S1:<chunkId>
Section 7: Fuzzy-top rulings
boundary	outcome	could sit in	placed in	reason	signposted from
Introductory to Intermediate	<id>	both	<tier>	<reason>	<tier or none>
Intermediate to Advanced	<id>	both	<tier>	<reason>	<tier or none>
Section 8: The learning journey
tier	the learner arrives able to	the learner leaves able to	identity shift	main book sections	feeds into
Introductory	<arrives>	<leaves>	<from lens identity>	<sections>	Intermediate
A short narrative follows, plus the results of the journey checks in 1.3.

Section 9: Context alignments
Empty, with the words "no subject or qualifier context", if sdef-03 was skipped.

benchmark row	subject benchmark	strength	passage	what it means for authoring	where to use it
d3	<id>	direct or indirect	<chunkId>, <extract>	<from agentInstruction>	<outcome ids>
Section 10: Pitch review
From onb-05_pitch: the agent's review across all tiers, or the chosen tier's pitch.

Section 11: Gaps and limits
The agent states what the statement rests on and what is thin. It always covers:

limit	what to record
Unconfirmed mappings	that map statements are still proposed, and which were used
Weak subject links	core, specialism or none, and any weak course match
No subject readings	the rows with none, normally everything below d3, and how those were handled
Missing sources	anything expected but not available, and the fallback used
Section 12: Hand-off
reader	reads	for
crs-02_thematic-scope	sections 3, 4 and 8	scope
crs-03_course-outcomes	section 6	course outcomes and courseOutcomeBanks, for each tier's course
crs-04_lesson-map	sections 6 and 9	proposed lessons and their grounding, for the user's sign-off
progression-signposting	sections 6, 7 and 8, at their latest revision	signposts between tiers, and the journey re-check after crs-04
les-01, wra-01 to wra-04	sections 3, 6 and 9	authoring
cxp-04	sections 2 and 9	context generation
1.6 Review and storage
Review: confirm, amend, or regenerate with new instructions. Each regeneration records its instruction and raises the revision number.
Storage: the structured sections go in the gate record's decidedValue, so later gates can read them by id. The readable document is rendered from that record.
Going stale: if an earlier gate reopens, or a registered source's version changes, the statement is marked stale and goes back for review.
Changes at crs-04: these do not make the statement stale. Section 6 takes the change and its reason as a new revision, and keeps the wording agreed at sdef-04.
1.7 Checks before it can close
check	fails if
Sources	anything cited has no row in the source register, or a registered file can't be found
Complete	a section is missing, or the 9 or the outcomes differ from sdef-04
Traceable	a changed benchmark or outcome lacks its original wording or reason, or an added outcome lacks its reason
Honest	a source's status is shown as firmer than it is, or section 11 omits a required limit
Voice	section 3 fails voice-lint.js
Ready to hand off	an outcome has no id, or no tier on pathway-proliferation
1.8 Open questions
Where the finished 18 will live. They are being worked on elsewhere, and SDEF uses the interim sources in Part F, F6, until then. T4 and section 6 point to the new location once they are wired up.