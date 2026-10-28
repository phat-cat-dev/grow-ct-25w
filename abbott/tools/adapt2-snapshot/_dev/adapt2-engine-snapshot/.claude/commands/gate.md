---
description: Open one design gate in the proposal grammar (ONB/CXS/CRS/LES/WRA/CXP). Read-only. Use in plan mode.
argument-hint: <course-slug> <gate-id e.g. crs-02_thematic-scope> [lesson-key e.g. L04]
allowed-tools: Read, Grep, Glob, Bash(node tools/session-audit.js:*), Bash(git log:*), Bash(git status:*)
---

## Working rules (backlog 5.138)

These rules bind every session that runs this command. The same block stands in `gate.md`, `land.md`, `scaffold.md`, `phase-draft.md` and `reopen.md`; change all five together.

1. No `sed` of any kind. Edit a file with the Edit tool or a short Python script whose replacements are string-asserted (`assert text.count(old) == 1`), and check the file's size after every write.
2. One command per Bash call. Never separate two commands with a newline inside one call; where two must run together, join them with `&&` or `;`. Read an exit code with `echo "EXIT: $?"` straight after a single command, never after a pipeline.
3. `/gate` and its arguments stand on a line of their own, with any instructions on the lines below. A session that finds instructions on the command line itself stops and asks which words are arguments.
4. A gate session writes its full proposal and its draft record to its plan file before showing them, prints the plan file's path, and re-reads that file after any compaction or clear before going on (GDP-1).
5. The self-check. Before staging any write, and once more over anything the session reports, run each pattern below once with `grep -cE` (`-ciE` where marked) and once with `grep -oE` (`-oiE` where marked), never `-n`, and paste both commands and their output. Explain any hit that is a count rather than a position.
   - `[A-Za-z0-9_-]*\.[A-Za-z0-9_-]+:[0-9]+`
   - `\b(line|lines)\b[^a-zA-Z]{0,3}[0-9]+` (case-insensitive)
   - `[0-9]+[^a-zA-Z]{0,3}\b(line|lines)\b` (case-insensitive)
   - `^@@ -[0-9]` (a raw diff only)
   - `@@ -[0-9]`
   - `Ruling [0-9]`
   - `\bruling [0-9]` (case-insensitive; commit messages and added lines only)
6. Cite the course's own gate records under the store `course-design` (`courses/<slug>/course-design_<slug>.json`), never under `design-kb`, which names the shared stores only.
7. Compare a log or a register by row id, never by line.

You are opening ONE gate for course `$1`, gate `$2`, lesson `$3` (the
lesson key applies only to a per-lesson LES gate, `les-01`; leave it
empty for every course-level gate). This command runs in plan mode: it
writes nothing to the repository, only to this session's plan file
(GDP-1). Each gate opens in a fresh session; after any compaction or
clear, the session re-reads its plan file before continuing. Its output
is a proposal the human answers; the write happens later via /land.

The six phases are `ONB → CXS → CRS → LES → WRA → CXP`; gate ids carry
the phase prefix (`onb- | cxs- | crs- | les- | wra- | cxp-`). A gate
whose store entry is `reserved` (every `cxs-*` now, plus
`cxp-03_exemplar-programmes`; all `defaultType: "none"`, advisory) is
an auto-pass placeholder for a future process, not an interactive
proposal: do not open it. It needs no record to be absent — a course
validates with no record for a reserved gate (the criticality build
proved this) — and `--skip` does not apply, since that path is for a
gate whose `reachabilityFacet` was not met and a reserved gate carries
none. How a reserved gate's eventual auto-pass record gets written is a
pending mechanics decision; say so rather than writing one here.

Do this in order and show the evidence for each step before the
proposal, not after.

1. RECON. Check whether `courses/$1/course-design_$1.json` exists
   before reading it. If it does not:
   - Gate `$2` is one of the four ONB gates (`onb-01_theme-preset`,
     `onb-02_course-theme`, `onb-03_pitch`, `onb-04_naming`): proceed.
     State "no manifest yet — this will be one of $1's first gate
     records, written by /new-course once the four ONB gates are
     answered" and skip the upstream-`decidedValue` reads below (there
     is no manifest to read them from). Where this ONB gate has a
     `dependsOn` edge (onb-02 on onb-01; onb-04 on onb-02/onb-03), the
     upstream answer lives in the preceding /gate session's plan file
     and the human's confirmation, not a manifest — state it from
     there. Continue to step 6's PROPOSAL as normal.
   - Gate `$2` is anything else: STOP — "no manifest exists for $1:
     answer the four ONB gates first, each via this command, then run
     /new-course $1 before opening any other gate." Do not proceed to
     step 2.

   If the manifest exists, read it. State the current
   record for this gate (seq, state, provenance) or "no record". Read
   `design-kb/design-kb.gates.json` and print this gate's entry:
   kind, hardness, every `dependsOn` edge with its dependencyClass.
   For each upstream gate, print its current decidedValue from the
   manifest. If any upstream hard-stop is not closed, STOP and say so.
   The facet set now lives in `manifest.facetSet` (`pathway` from
   onb-02, `tier` from onb-03), written by /new-course — read it there,
   not from any gate's `decidedValue`. No gate in the current store
   carries a `reachabilityFacet`, so there is no facet-reachability
   STOP to apply here; if a future gate entry adds one, test whether
   that facet is a key of `manifest.facetSet` and, if absent, STOP,
   name the missing facet, and say the gate should be closed via
   `/land $1 $2 --skip`, not opened with an ask.

   LAYER-1 PATHWAY GROUNDING. Read this course's pathway record from
   `design-kb/design-kb.pathways.json`, keyed by
   `manifest.facetSet.pathway`. This is the consolidated generic
   grounding for the content gates (`crs-02_thematic-scope`,
   `crs-03_course-outcomes`, `crs-04_lesson-map`,
   `les-01_lesson-proposal`, the `wra-*` gates): it carries the book
   `chapters` in scope, the book-map chunk ids tagged to this pathway
   (`bookChunks.primary` = sole-tagged to this pathway;
   `bookChunks.shared` = co-tagged, each with its co-pathways named),
   and the per-tier `focus` and `voiceBand` for
   `manifest.facetSet.tier`. Cite chunk ids from this record; read each
   chunk's text in place from the book map it points at
   (`machinery.bookMap`), which stays the single source of truth for
   chunk text. This is Layer 1 (pathway/theme), subject-agnostic. The
   Layer-2 subject grounding below (SOURCE CONSULTATION) is separate and
   fires only where a gate carries a `sourceConsultation` block and a
   subject facet is set.

2. SOURCE CONSULTATION (SSC-1, only where this gate's entry in
   `design-kb/design-kb.gates.json` carries a `sourceConsultation`
   block — currently `crs-02_thematic-scope`, `les-01_lesson-proposal`
   and `cxp-04_context-generation`). Print the
   block's `triggeringFacets` and `authorityLevels`. Intersect
   `triggeringFacets` against the manifest's own facet set
   (`manifest.facetSet` — `pathway` and `tier` — plus any module,
   institution, faculty, school or activity facets recorded since); a
   facet the manifest does not carry does not trigger. For each
   triggered facet, read every
   `source-kb` record (and, once populated, `institutional-kb`) whose
   `authorityLevel` is in this gate's `authorityLevels` list and whose
   `facets` match: subject by CAH walk-up, most specific first; level
   by non-empty intersection. Read each matching record's source map
   under `source-kb/source-maps/` where one exists (SM-1); where none
   exists, say so plainly rather than falling back to the record's own
   PDF or to general knowledge. A benchmark-kind map's chunks carry no
   text of their own (BM-1 AMENDMENT, 21 September 2026, Prompt 148):
   where a chunk's own text is needed, read it in place from
   QAAVector's `mapped/<slug>/<slug>.chunks.json`, never copied into
   this repo. Cite only a chunk whose `status` is `confirmed`; a
   `proposed` chunk may be read but not cited as grounding. Print, for
   each record consulted: its id, whether a map existed, and either
   the map chunk id(s) actually used or the words "grounding gap"
   with the reason. Carry this into step 6's Grounding line; a
   triggered facet with no matching record, no map, or no confirmed
   chunk for the need is a grounding gap stated in the proposal, never
   silently dropped. No `sourceConsultation` block on this gate's
   entry: state that plainly and skip to step 3.

3. VARIETY VIEW, where `node tools/gate-order.js --flags=<this gate's id>`
   reports `procedureFlags.varietyView` true (RJ-0059: read from the
   store, not this list). From the manifest, list every
   pattern id and realisation already recorded at the same gate for
   every other lesson in this course. The proposal must name what it
   is avoiding repeating, or say why repetition is right here.

4. CANDIDATES, where the same tool call reports `procedureFlags.candidates`
   true (RJ-0059: read from the store, not this list; activity-gate
   slot choices — currently `les-01_lesson-proposal`,
   `wra-01_wrapper-open`, `wra-02_wrapper-close` and
   `wra-03_summative`). The signpost slot
   on `wra-01_wrapper-open` uses the skeletons store's furniture
   selection model instead (FSM-1). SHAPE FIRST (SF-1):
   before selecting any pattern, name
   the content shape or shapes for this slot from
   `design-kb/design-kb.content-shapes.json`, quoting the book
   passage that shows each shape, read via this pathway's `bookChunks`
   (`design-kb/design-kb.pathways.json`) through the book map; for a
   lesson, narrow to the chunks for the book section recorded at
   `crs-04_lesson-map`.
   From
   `design-kb/design-kb.activity-patterns.json` select every pattern
   where: `servesShapes` includes the named shape, `intent` admits
   the gate's intent, the course tier appears in `tierCalibration`
   with fit strong or adequate, and the slot type is in `slotTypes`
   (a slotTypes miss is reported, not silently argued past; see
   backlog 5.76). Rank by `contextAffinity` against the manifest's
   facetSet. Print the ranked list with ids, and the shape id and
   quoted passage beside it. Zero survivors is stated plainly and
   noted as pattern-store population evidence. Alternatives (step 6)
   are drawn from this list in shape order: first, other patterns
   from this same ranked list serving the named shape; then, only if
   the content shows a second shape, a pattern serving that second
   shape, run through the same slotTypes/tierCalibration/intent
   filters above. Each alternative is subject to the same slot, tier
   and intent filters as the lead.

5. PRE-FLIGHT (S3-D6). For the lead realisation, read the palette
   entry in `design-kb/design-kb.palette.json` and open the file at
   its `specPointer.doc`. Print the constraints that bind this shape
   (item caps, required children, feedback structure). If the shape
   fails, take the next realisation in the pattern's list. Never utter
   a shape you have not checked against the spec.
   Pre-flight checks the component's own structural and config validity
   against its spec, NOT whether an asset already exists (BK-5): an
   asset-needing component (e.g. `palette/hotgraphic` with no image yet)
   is a valid proposal, since there is never an asset until the option
   is chosen. Record the asset as a `visualAssets` placeholder and
   supply it later if the option is selected; do not fail pre-flight for
   a missing asset.

5b. AGENT-DIRECTION CONSULT. Where this gate authors a slot whose skeleton
    block (`design-kb/design-kb.skeletons.json`) carries an `agentAuthor`
    block, resolve its effective instruction before shaping the proposal:
    `node tools/resolve-agent-author.js --archetype=skeletons/<pageType>
    --slot=<key> --manifest=courses/$1/course-design_$1.json --mode=written`
    (agent-direction pattern, `docs/authoring/agent-author-metadata.md`). It
    applies only the steers whose facet is active (the activation rule):
    `byTier` from the course's tier always; the reserved `bySubject` /
    `byQualifier` / `byInstitution` only once their phase has set a matching
    key. Fold the returned `content` and `relation` into the proposal's
    rationale, carry each `warnings` entry as a do-not to respect, treat
    `bestPractice` as guidance, and use the returned `displayTitle` where one
    is given. `omit: true` (a tier whose steer sets `applies:false`, e.g.
    advanced `where-next`) means the slot is not proposed at this tier at all.
    A slot with no `agentAuthor` is proposed as before.

6. PROPOSAL, in exactly this shape. At `les-01_lesson-proposal` only
   (SO-1, `docs/project/open-decisions.md`, 19 September 2026): this is
   not one triple but a `slots` object with one entry for each of
   `concept-intro`, `worked-example` and `practical-guidance` (the
   worked-example slot was keyed `interior` before the v2 rename, 8 Oct
   2026; block-key is now its slotType), each entry in
   the pattern/realisation/coupling shape below plus its own rationale.
   (les-01 is the single consolidated lesson gate — interior design
   plus activities plus per-slot coupling marking; see the master table,
   `docs/authoring/gate-master-table-2026-10-07.md`.)
   v2 lesson model (8 October 2026, `design-kb/design-kb.skeletons.json`
   lesson archetype; `docs/authoring/lesson-structure-template.md`): the
   `concept-intro` slot is the lesson's **interactive concept activity**
   ("now see it"), not the concept prose. The concept prose is two
   separate blocks that are NOT gate decisions and carry no entry in
   this `slots` object: `concept-definition` (a generic definition of the
   lesson topic, why-before-how, authored at /land — it frames the topic
   and says why it matters and must NOT summarise or spoil what the
   activity reveals) and `concept-context` (whole-prose coupled, left
   empty in the shell for the context pack to fill at CXP). So the
   `concept-intro` entry here proposes the **activity**: offer it as
   three shape x component alternatives (BK-4) from which the human
   chooses one — three distinct components that each present the same
   content, ranked by content-shape fit (steps 4-5), never a mix of
   lesson furniture (the practical-guidance checklist and the check MCQ
   are givens, not among the three). The activity may be a manipulation
   question component in ACTIVITY MODE (palette/matching, sortable,
   hotspot, slider, via sort-into-groups / build-from-parts /
   label-a-structure / place-on-a-scale, which now serve concept-intro)
   - learn-by-doing, not a reveal; authored at /land with `_attempts:
   -1`, a teaching `notFinal` and a concept-reiterating `correct`,
   `_isPartOfAssessment: false` (see the skeletons lesson archetype
   notes). mcq/gmcq stay check-only. Each coupled slot's standing
   context prompt is layout-level and lives in the store
   (`slot.standingContextPrompt`), not decided here; cite it in the
   entry's grounding rather than re-authoring it.
   **Plain prose is always weighed at every entry, and may lead
   (RT-1, 20 September 2026).** Weighing it is not optional even where
   a pattern realisation is proposed: the rationale states that plain
   prose was considered and says why it did or did not lead. Where it
   leads, the entry records `pattern: null` under SO-1. The wrapper slot
   choices (`wra-01_wrapper-open`, `wra-02_wrapper-close`) still write
   the single triple as before.

   Alignment guidance, by gate (constructive alignment runs every
   downstream decision back from the course-outcomes gate
   `crs-03_course-outcomes` and the lesson outcomes set at
   `crs-04_lesson-map`):
   - **crs-04_lesson-map** (per-lesson outcomes): AL-1
     (`docs/project/open-decisions.md`, Prompt 173) — each lesson
     outcome serves exactly one course outcome from
     `crs-03_course-outcomes`. AL-2 (same) — each outcome states one
     verb and one object, no "and" joining two tasks; the count is
     never derived from how many source sections the lesson has, and
     the outcome stays inside `crs-02_thematic-scope`'s recorded scope.
   - **les-01_lesson-proposal** (formative check): AL-3 (same,
     three-outcome model 9 Oct 2026; see
     docs/authoring/token-substitution-coupling-and-three-outcome-model.md)
     — exactly three check items, one per lesson outcome: item 1 general
     and shell-coupled, item 2 context-specific, item 3 token-substitution
     (shell body carrying {{context}}, its tokenMode set at this gate). Each
     names via `tests` the one lesson outcome it tests; the three `tests`
     are distinct and cover all three outcomes.
   - **crs-03_course-outcomes** (course outcomes + the per-outcome banks
     they seed): AL-2 (same) — each course outcome, and each confidence
     statement in its bank, states one thing (the one-idea rule). crs-03
     DECIDES the MCQ-set specs and confidence-statement text; the
     authoring of the SUMM items and the C-PRE/C-POST components is done
     downstream at wra-03/wra-04 (post-scaffold), where AL-3/AL-6 and
     AL-4 below bind.
   - **wra-03_summative** (summative authoring, post-scaffold): AL-3
     (same) — every course outcome is tested by exactly two summative
     questions, the real stems drafted from crs-03's per-outcome MCQ-set
     specs into the SUMM page, each naming via `tests` (AL-6) the one
     course outcome it tests.
   - **wra-04_confidence** (confidence placement, post-scaffold): AL-4
     (same) — each confidence statement names via `rates` the course
     outcome it rates, and every course outcome carries at least one;
     the same statement set fills C-PRE and C-POST.
   - **wra-01_wrapper-open / wra-02_wrapper-close**: AL-5 (same) —
     W-OPEN (wra-01) states the course outcomes and why they matter for
     the student's own studies; W-CLOSE's (wra-02) summary tells the
     student what they can now do, outcome by outcome, connects each to
     their studies, and refers to the confidence shift seen on C-POST.

   **Gate $2 (<plain name>) for $1 $3. Hardness: <from gates.json>.**
   Proposal: <pattern id> realised as <palette id>, coupling
   <variationType> drawing on <kb entry or "generic">.
   Grounding: <the citations, ids and doc refs as they will be
   written into the record — shape (SF-1), pattern, realisation and
   coupling from steps 4-5 where this gate is an activity gate; the
   source-kb record ids, source-map chunk ids or stated grounding gaps
   carried from step 2 where this gate's entry carries a
   sourceConsultation block (SSC-1); every id printed in step 2, 4 or
   5>.
   Consequence: <downstream constraint, or omit>.
   Alternatives (pattern-level sketches, one line each, field-grounded
   why-not): <1 to 3, or "none survive filter">.
   Ask: hard-stop -> "confirm / amend / replace / defer" on its own
   line, nothing else on that line. Soft -> "standing unless you
   object". Advisory -> "stated, no response sought".

7. Write the full proposal and the draft record JSON into this
   session's plan file (GDP-1), and print the plan file's path
   alongside the proposal (I47). Validation against the schema
   happens at /land, not here (I39): plan mode writes nothing to the
   repository, so `tools/validate-gate-record.py` cannot run against
   a file this session has saved. Print the draft record JSON exactly
   as /land will write it: `originalProposal` only when provenance is
   `human-amended` (ALT-1; the schema's own description already
   requires it exactly there and nowhere else — "REQUIRED when
   provenance=human-amended"), `alternativesConsidered` (array of
   `{pattern, whyNot}`, ALT-1: kept whenever this proposal set out
   alternatives, regardless of provenance — the two fields' presence
   does not move together) and `sessionRef` as an object (SRF-1:
   object form only) — `{"venue": "claude-code-plan", "description":
   "<course> <gate> <date>"}`.

Do not batch more than one hard-stop into a single ask. Do not
proceed to another gate in this invocation.
