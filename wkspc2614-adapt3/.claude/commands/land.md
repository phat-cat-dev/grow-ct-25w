---
description: Write one confirmed gate record and, for content gates (les-01 and the wrappers), its Adapt content. Execute mode only.
argument-hint: <course-slug> <gate-id> [lesson-key] [--skip]
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

Write moment for course `$1`, gate `$2`, lesson `$3`. The human has
answered the /gate ask. Paste of that answer follows this command.
Do not re-derive, re-propose or second-guess the decision.

1. RECON FIRST. Before anything else, read the draft record from
   the plan file whose path the pasted answer names (GDP-1). If no
   path is given, stop and say so. If the named file does not exist,
   stop and name the path. Confirm the manifest's current record for
   this gate matches what /gate printed (seq, state). If it moved,
   stop.
2. Provenance: hard-stop records may only be `human-confirmed`,
   `human-specified` or `human-amended`; if the human's word is not in
   the pasted answer, refuse to write `human-confirmed`. Soft gates
   with no answer stand on this gate's own `defaultType`
   (`design-kb/design-kb.gates.json`), read fresh for this gate rather
   than assumed from a remembered gate id: `defaultType: "fixed-value"`
   stands as `ai-default-stood`; `defaultType: "ai-proposal-stands"`
   stands as `ai-proposal-stood` (GI-2, `docs/project/open-decisions.md`,
   27 Aug 2026 — `schemas/common.schema.json`'s `provenance` enum
   description states the distinction directly: "ai-proposal-stood: for
   gates with defaultType ai-proposal-stands where the AI's proposal
   stood on silence, distinct from ai-default-stood which is for
   fixed-value defaultType gates"). Any other `defaultType` on a soft
   gate: stop and report the value and the gate rather than choosing a
   word for it.
2a. Validate the draft record before appending it. Check
   `tools/validate-gate-record.py`'s own usage line first and use its
   real arguments. Write the draft record, with the human's answer
   applied, to a temp file. Run `python3 tools/validate-gate-record.py
   <path>` as its own Bash call, then `echo "EXIT: $?"` as its own
   call. Any failure refuses the write.
3. Append the record (append-only; new seq; never edit an earlier
   record). String-asserted edit against the manifest. ALT-1: write
   `originalProposal` only when provenance is `human-amended` (the
   schema itself requires it exactly there and nowhere else); keep
   `alternativesConsidered` whenever /gate's proposal set out
   alternatives, regardless of provenance — the two fields' presence
   does not move together.
4. Gates with content author directly into the Adapt JSON, each
   per its own gate (DR-1, `docs/project/open-decisions.md`,
   20 September 2026).
   **Consult `agentAuthor` before authoring a slot** (the agent-direction
   pattern, `docs/authoring/agent-author-metadata.md`). For any slot whose
   skeleton block (`design-kb/design-kb.skeletons.json`) carries an
   `agentAuthor` block, resolve its effective instruction for this course
   before writing the component:
   `node tools/resolve-agent-author.js --archetype=skeletons/<pageType>
   --slot=<key> --manifest=courses/$1/course-design_$1.json --mode=written`.
   The tool reads the course's tier from the manifest `facetSet` and applies
   only the steers whose facet is active (the activation rule): `byTier`
   always, the reserved `bySubject` / `byQualifier` / `byInstitution` only once
   their phase has set a matching key. Follow the returned `content` and
   `relation` as the brief, self-check against every `warnings` entry before
   emitting, treat `bestPractice` and the active-mode `modeNotes` as guidance,
   and use the returned `displayTitle` where one is given. `omit: true` (a tier
   whose steer sets `applies:false`, e.g. advanced `where-next`) means do not
   author that block at all. A slot with no `agentAuthor` is authored as before;
   this adds a brief, it never overrides a closed gate's decided content.
   **Published-course edit-mode (`docs/authoring/field-locks-and-edit-mode.md`):**
   on a course whose `status` is `production`, re-author content ONLY for the
   fields this landing's reopen unlocked; every other component is preserved
   verbatim (do not regenerate settled content). On an in-development course,
   author freely as below.
   In the six-phase model the content-authoring
   gates are the per-lesson `les-01_lesson-proposal` and the two
   wrapper gates `wra-01_wrapper-open` / `wra-02_wrapper-close`. No
   bullet below writes `config.json` (backlog 5.139's residual,
   checked against every bullet):

   - **les-01_lesson-proposal** (per lesson): author this lesson's
     interior and activities into the Adapt JSON — the concept and
     interior-teaching components (`conceptTitle` / `interiorPattern`),
     the worked example (`workedExample`), the formative `check`, the
     `reflectivePrompt`, the general MCQ set (`generalMcqSet`), the
     context-question slot (`contextQuestionSlot`) and the chosen
     component from `activityProposals` — then add or update the page's
     `instantiations` entry in the manifest with `notes` for any
     deviation from the skeleton.
     **v2 concept blocks (8 October 2026):** `interiorPattern` /
     `activityProposals` author the `concept-intro` block, which is the
     interactive concept ACTIVITY. The concept prose is two separate
     blocks: author `concept-definition` (a generic definition of the
     lesson topic, why-before-how — it frames the topic and says why it
     matters and must NOT summarise or spoil what the activity reveals),
     and leave `concept-context` EMPTY (whole-prose coupled; the context
     pack fills it at CXP). `summary` is now a structured-fields coupled
     slot: author its generic recap frame here, the pack fills the
     subject fields at CXP. `workedExample` authors the `interior`
     (worked-example) block as a structured-fields frame using the
     character-token cast (the weaker or less-developed version first,
     then the stronger one; the topic is the lesson's own, not a fixed
     surface/deep framing). The standing per-slot context prompts for
     these coupled slots live in the store and are applied at CXP, not
     re-authored here.
     **Activity-mode question components (8 October 2026):** when the
     chosen `concept-intro` activity is a manipulation question component
     (palette/matching, sortable, hotspot, slider — learn-by-doing, not a
     reveal), author it in ACTIVITY MODE, not as a check: `_attempts: -1`
     (unlimited tries); `_feedback._incorrect.notFinal` explains the error
     and points toward the answer (no `final` — unreachable under -1);
     `_feedback.correct` reiterates and explains the concept/structure the
     learner has just completed (never a bare verdict); `_isPartOfAssessment:
     false`. Its coupling in `coupledSlots` stays as les-01 recorded it
     (shell-coupled unless the activity itself is subject-specific).
     The lesson's `learning-outcomes`,
     `orientation` and `summary` components, and its
     `lesson-references` ("Lesson Sources") component, are authored
     from this lesson's entry in the closed `crs-04_lesson-map` record
     (its outcomes, title/topic/description and bound source
     section(s)): outcomes are set at crs-04, not at les-01 (A6.2),
     so there is no per-lesson outcomes gate to read (BW-1/LF-1 carried
     forward to crs-04). Each Lesson Sources entry follows LSP-1's
     pointer form (`docs/project/open-decisions.md`, Prompt 173): a
     footnote-style pointer such as "See pages x to y of Chapter n of
     *Title* by Authors", not a formatted reference, citing at least
     the chapter and page range (PLR-1 AMENDMENT); its coupling stays
     `shell-coupled`.
     **MK-1** (`docs/project/open-decisions.md`, 21 September 2026,
     AMENDMENT 22 September 2026, Prompt 157): les-01 now carries its
     own per-slot coupling marking in `coupledSlots` (A6.2 folded the
     old separate context-coupling-plan gate into this one). Before
     writing a component, find the entry in this lesson's closed les-01
     `coupledSlots` whose `slot` equals the slotType this component
     fills. If that entry's coupling is anything other than
     `shell-coupled`, write that slot's own marker,
     `slot__<page>__<slotType>` (LK-1's double-underscore form), into
     the component's `_classes` field — the same field and form
     `tools/generate-course-shell.js` writes for the slots it creates
     directly. When a slot needs more than one component tailored to
     the subject, give each its own short kebab-case part name and
     write `slot__<page>__<slotType>__<part>` (MP-1); use the part-less
     form when the slot has one such component; never reuse a part
     within a page and slot; the pack must carry a key of the same
     name, `<slotType>__<part>`. If the coupling is `shell-coupled`, or
     les-01 has not closed yet, write `_classes: ''`: no marker.
     This `coupledSlots` rule governs the SO-1 component-choice slots
     (`concept-intro`, `worked-example`, `practical-guidance`, `check`).
     The v2 `concept-context` and `summary` slots are NOT in
     `coupledSlots` and are NOT marked here: they are single-realisation
     always-coupled slots the generator creates and marks directly at
     scaffold (`slot__<page>__concept-context`, `slot__<page>__summary`),
     so leave those two components' generator-written `_classes` as they
     are.
     The formative `check` additionally records `tests` on each item (AL-6,
     `docs/project/open-decisions.md`, Prompt 173), naming the lesson
     outcome id from this lesson's crs-04 entry the item tests.
   - **wra-01_wrapper-open / wra-02_wrapper-close:** the drafted
     overview (WO-1) authors W-OPEN's `overview` block; the drafted
     course summary authors W-CLOSE's `summary` block; the where-next
     content authors W-CLOSE's `where-next` block; each wrapper's
     practice-connection content authors its `practice-connection`
     block. All are `palette/text` components in `en/components.json`
     (`skeletons/wrapper-open` and `skeletons/wrapper-close`). The
     wrapper-page coupling degree is set at these gates (A6.3); apply
     the same MK-1 marker rule as above, reading each wrapper gate's
     own coupling marking. AL-5 (`docs/project/open-decisions.md`,
     Prompt 173): W-OPEN states the course outcomes and why they
     matter; W-CLOSE's summary tells the student what they can now do,
     outcome by outcome, and refers to the confidence shift seen on
     C-POST. Add or update each wrapper page's `instantiations` entry
     as for any other authored gate, with `notes` for any deviation
     from the skeleton.
   - **wra-03_summative:** author SUMM's `assessment-items` block in
     `en/components.json` (`design-kb/design-kb.skeletons.json`'s
     `skeletons/summative` archetype), one component per item,
     `palette/mcq` or `palette/sortable` per the SM-2 split. The item
     stems come from this gate's own closed `decidedValue.items` (the
     agent turned crs-03's 3 mcqSet specs per outcome into real stems
     at proposal time, Abbott confirmed); do not re-derive them from
     crs-03 here. AL-3 (`docs/project/open-decisions.md`, Prompt 173):
     exactly two summative questions per course outcome. Each item's
     `tests` (AL-6) names the course outcome id from `crs-03` it tests.
     The `results` block furniture (`palette/assessmentresults` with
     its `palette/resultsdebrief` and `palette/passreveal` extensions)
     is structural, not separately authored. An item whose coupling is
     not `shell-coupled` carries its MK-1 slot marker (as in les-01
     above) for `cxp-04` to fill per subject. Add or update SUMM's
     `instantiations` entry with `notes` for any deviation.
   - **wra-04_confidence:** author C-PRE's `confidence-pre` block and
     C-POST's `confidence-post` block (`palette/confidence` component)
     in `en/components.json`. The statements come from this gate's own
     closed `decidedValue.statements`, each placed against the outcome
     its `rates` (AL-4) names; every course outcome carries at least
     one. The same statement set fills both pages (C-PRE before
     lessons, C-POST at close). The `reflectiveBridge` on/off decision
     is structural and read by `generate-course-shell.js`; this gate
     covers only the confidence items' content. Add or update the
     C-PRE and C-POST `instantiations` entries with `notes` for any
     deviation.

   The resources drawer (`course.json`'s `_resources` block) is NOT
   authored here: Abbott ruled it (8 Oct 2026) a reserved gate,
   `cxs-06_resources`, which writes nothing while reserved — this
   command never authors a reserved gate. The shell ships
   adapt-contrib-resources at its own default until a future process
   fills that gate. (The summative/confidence authoring location,
   formerly PENDING here, is likewise RESOLVED: Abbott ruled it to
   wra-03_summative and wra-04_confidence, 8 Oct 2026 — the two bullets
   just above.)
5. Run the validator at every landing, not only during the carve-out
   below: `python3 tools/validate-design-schemas.py --course-design
   courses/$1/course-design_$1.json; echo "exit: $?"`. Paste the
   summary AND the exit line verbatim; require exit 0. This run's own
   named checks (RJ-0060: read from the tool's own output, not this
   list) include SHP-1 (decidedValueShape), the OC-1/CO-1 and LK-1
   cross-checks, CPL-1's page/slot/depth and wrapper checks, and GI-2
   (R18: a closed record's provenance word matches its own gate's
   hardness and defaultType, read fresh each run).

   Once the manifest's `instantiations` array is not empty (checked
   directly, not assumed — read the manifest), ALSO run `node
   tools/verify-course.js --course=$1; echo "exit: $?"` and paste its
   summary table and exit line too; require exit 0 from that as well.
   This widens the existing mechanism rather than replacing it: while
   `instantiations` is empty, `verify-course.js` cannot resolve or
   has nothing to check and does not run — the validator alone
   stands as the gate. State plainly in your response that the
   carve-out applied and why (`instantiations` is empty), when it
   does. The moment any B-gate writes the first `instantiations`
   entry, the carve-out ends: from the first B-gate onward, both
   checks run together, neither substituting for the other. If you
   are unsure which side of that line a course is on, run
   `verify-course.js` and report what it says — do not assume the
   carve-out applies.

   LES-phase carve-out (8 October 2026): landing ONE lesson cannot make
   `verify-course.js` exit 0 on its own, because `manifest-completeness`
   clause 1 (a les-01 record for every lesson in `crs-04_lesson-map`)
   and clause 2 (an `instantiations` entry for every built page) check
   the WHOLE course and stay red until the last lesson and the wrappers
   land. During the LES phase, read those cross-lesson clauses the way
   the fresh-shell carve-out reads clauses 1/2/3/6: expected-incomplete,
   not this landing's failure. What this landing must still prove, and
   what still refuses it, is any failure attributable to the lesson just
   written: the `--course-design` validator must exit 0 (SHP-1, OC-1,
   CO-1, LK-1, CPL-1, GI-2 are this write's own), and within
   `verify-course.js` voice-lint must PASS, validate-design-schemas must
   PASS, and this lesson's OWN rows must be clean — its `instantiations`
   match, its MK-1 markers (NOT YET REACHABLE on other lessons is fine,
   a FAIL on this lesson's markers is not), its CK-1/AL/PSR-1/LPG-1 rows,
   and conformance-lint clause 1 for this lesson's own blocks. Name the
   lessons still pending in your response. The full `verify-course.js`
   exit-0 gate is the LES-phase-close (build-readiness) gate, reached
   once every lesson and wrapper has landed, not a per-lesson gate.

   A missing exit line on any check that should have run means that
   check is unproven. A FAIL or non-zero exit attributable to the lesson
   just written — as distinct from the LES-phase cross-lesson
   incompleteness carved out above — refuses the landing, leaves the
   file as it was before the write, and names the gate and the failing
   field (5.98: a dropped failure reached a commit at 8e7ad02).
6. SHOW-DIFF-STOP. Full `git diff`, then wait. Explicit staging of the
   touched files only. One commit per gate, per "Venue model, write
   cadence and provenance words (8 Sep 2026)"
   (`docs/project/open-decisions.md`), which supersedes
   `course-creation-workflow.md` §7's one-write-per-phase. The
   six-phase model has no multi-gate batch per lesson:
   `les-01_lesson-proposal` is one consolidated gate (A6.2), so a
   lesson lands in a single les-01 invocation and a single commit. The
   old seven-invocation B1-B7 deferral (LD-1,
   `docs/project/open-decisions.md`, 18 September 2026) is retired with
   the per-lesson B-gates it batched; a `/phase-draft` + PHASE BATCH
   PATH run (RJ-0061) still lands a whole phase's soft/advisory gates
   in one commit, per that path below.

   No push. The four built courses' own commit practice is reference
   material under "RBD-1 — Rebuild supersedes retrofit as the audit's
   fix strategy (13 September 2026)" (`docs/project/open-decisions.md`),
   on the same footing as their gate decisions, not binding precedent.

---

SKIP PATH (invoked explicitly as `/land $1 $2 --skip`; never inferred
from silence or from steps 1-6 above). For a gate whose
`reachabilityFacet` (`design-kb/design-kb.gates.json`) was never met by
this course's declared facets, so the gate was never reached, not
decided against (`schemas/common.schema.json`'s `gateState` description).
NOTE: no gate in the current store carries a `reachabilityFacet`, so
this path has no live target now; it is retained for a future gate that
adds one. It is NOT the mechanism for a `reserved` gate (every `cxs-*`,
`cxp-03`) — a reserved gate is reachable but deliberately `none`, needs
no record to be absent, and S1 below correctly refuses it.

S1. Read this gate's entry in `design-kb/design-kb.gates.json`. Refuse —
    "gate $2 carries no reachabilityFacet: not skippable" — if it has
    none.
S2. Read the same manifest step 1 reads (`course-design_$1.json`). Read
    its `facetSet` (written by /new-course: `pathway` from onb-02,
    `tier` from onb-03). Refuse — "manifest carries no facetSet: cannot
    test reachability" — if it is absent.
S3. Shape-check `facetSet` before testing presence.
    Allowed keys: the `reachabilityFacet` enum (`subject`, `level`,
    `institution`, `faculty`, `school`, `module`, `activity`) plus the
    non-facet keys the manifest's facetSet carries (`pathway`, `tier`).
    Refuse — "manifest facetSet is not an object: cannot test
    reachability" — if it is not a JSON object. Refuse — "manifest
    facetSet carries unrecognised key <key>: not in {subject, level,
    institution, faculty, school, module, activity, pathway, tier}" — if
    any key falls outside that union, naming the offending key. An
    object of recognised shape carrying none of the facet keys is a
    valid empty facet set, not a refusal.
    Only once the shape is recognised: test whether the
    `reachabilityFacet` value (e.g. `school`) is a key of `facetSet`.
    Present means reached: refuse — "<facet> is present in the facet
    set: gate $2 is reached, use the ordinary path, not --skip". Absent
    means unmet: proceed.
S4. Append the record: `seq` (next in sequence), `state: "skipped"`,
    `timestamp`. Nothing else — no `provenance`, no `decidedValue`; the
    schema requires none of either for this state. Append-only, new seq,
    string-asserted edit against the manifest, exactly as step 3 above
    requires of every other record.
S5. Run step 5 above exactly as written, against this record like any
    other. Do not exempt it.
S6. Run step 6 above exactly as written.

---

PHASE BATCH PATH (invoked explicitly as `/land $1 --phase-batch=$2
--draft=<path>`; never inferred from silence or from steps 1-6 or the
SKIP PATH above). Lands every soft and advisory gate `/phase-draft`
drafted for phase `$2` (RJ-0061) in one run, instead of one gate at a
time. Holds no gate logic of its own: all of it is
`tools/phase-confirm.js`, which this path only invokes and reports.
**Must run before `/scaffold`, when `$2` is a pre-scaffold phase (ONB
or CRS)**: `phase-draft.md` states this too. The old per-lesson B7
batch boundary is retired with the B-gates; the LES and WRA soft gates
batch per their own phase, after /scaffold.

P1. Confirm `<path>` exists (the draft `/phase-draft` wrote, GDP-1). If
    not, stop and name the path.
P2. Run:

        node tools/phase-confirm.js --course-design=courses/$1/course-design_$1.json --draft=<path> --phase=$2
        echo "EXIT: $?"

    Paste both lines verbatim. The tool itself refuses (named error,
    non-zero exit, manifest left untouched) when the draft is
    missing an answer the phase requires, or when phase `$2` has no
    soft or advisory gate to batch; do not re-derive either check
    here; report the tool's own message. A zero exit means the
    manifest is already written (the tool writes directly, matching
    this command's own append-only edits elsewhere).
P3. Log the amend rate the tool's own output just printed
    (`amendRate`, `gateIds`) as a dated line in
    `docs/project/design-phase-logs/$1.md`: this command's own job,
    not the tool's; do not recount it.
P4. Run step 5 above exactly as written, against the batch's new
    records like any other write this command makes.
P5. SHOW-DIFF-STOP as step 6 above. One commit for the whole phase
    batch (one commit per logical unit, matching the "one commit per
    gate group" cadence above, generalised here to one phase's batch
    rather than one gate). No push.
