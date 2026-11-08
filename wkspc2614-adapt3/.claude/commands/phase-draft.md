---
description: Draft every soft and advisory gate in one phase in a single sitting, for a single /land phase-batch run. Read-only. Use in plan mode.
argument-hint: <course-slug> <phase-id e.g. CRS, LES-L04, WRA, CXP>
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
6. Cite the course's own gate records under the store `course-design` (`courses/v1/<slug>/course-design_<slug>.json` or `courses/v2/<slug>/...`), never under `design-kb`, which names the shared stores only.
7. Compare a log or a register by row id, never by line.

You are drafting every soft and advisory gate in phase `$2` for course
`$1`, in one sitting, for one `/land $1 --phase-batch=$2` run (RJ-0061).
This command runs in plan mode: it writes nothing to the repository,
only to this session's plan file (GDP-1). It holds no gate logic of
its own: for each gate's proposal it runs exactly `gate.md`'s own
steps 2 through 6 (source consultation, variety view, candidates,
pre-flight, PROPOSAL), the same grammar `/gate` uses for a single
gate. The only thing this command adds is collecting many gates'
proposals into one draft file and recording, per gate, whether Abbott
marked it.

Which gates this phase batches: every gate in phase `$2` whose
`hardness` is `soft` or `advisory`, read via `node
tools/gate-order.js --order` and this gate's own entry in
`design-kb/design-kb.gates.json` (RJ-0059: read from the store, not
a list in this file). Never hardcoded here; `tools/phase-confirm.js`'s
own `getPhaseBatchGates` computes the identical list independently
and will refuse (named error) if this draft's answers do not cover
it exactly. A hard-stop gate in the same phase (e.g. `crs-01_sources`
through `crs-04_lesson-map` in CRS) is not part of this batch; it is
answered one at a time via the existing `/gate` and `/land` path. A
`reserved` gate (every `cxs-*`, `cxp-03`) is likewise not batched — it
is an auto-pass placeholder, not opened at all. So in practice the
batchable soft/advisory gates are `crs-05_course-spec` (CRS, advisory),
`les-01_lesson-proposal` (LES, soft, per lesson), `wra-01_wrapper-open`,
`wra-02_wrapper-close`, `wra-03_summative` and `wra-04_confidence` (WRA,
soft) and `cxp-04_context-generation` (CXP, soft) — but always computed
from the store, never hardcoded
(RULINGS 5, adp-0216: a phase's soft gate is not special-cased out of
its batch list).

1. RECON. List phase `$2`'s batch gates in sequence order (as above).
   For each, read its current record in
   `courses/$1/course-design_$1.json` if one exists; a gate already
   `closed` in this phase is a finding, not silently skipped: state
   it and ask whether this run should still include it (it would
   append a second record, which the manifest's append-only
   invariant allows but a phase batch should not do by accident).

2. PER-GATE PROPOSAL. For each batch gate, in sequence order, run
   `gate.md` steps 2 to 6 for that gate exactly as `/gate` would run
   them for a single gate (source consultation, variety view,
   candidates, pre-flight, the PROPOSAL block including its Ask
   line). Soft gates print "standing unless you object"; advisory
   gates print "stated, no response sought": `/gate`'s own Ask
   wording, unchanged.

3. DRAFT FILE (GDP-1). Write the whole phase's draft to this
   session's plan file before showing any proposal, print the path,
   and re-read it after any compaction or clear. Shape, matching
   `tools/phase-confirm.js`'s own documented input exactly:

   ```json
   { "answers": [
       { "gateId": "wra-01_wrapper-open", "decidedValue": {"...": "..."}, "marked": false },
       { "gateId": "wra-02_wrapper-close", "decidedValue": {"...": "..."}, "marked": true,
         "originalProposal": {"...": "..."} }
   ] }
   ```

   Every batch gate's `decidedValue` starts as this gate's own
   proposal from step 2, `marked: false`. Nothing is marked by this
   command itself.

4. SHOW AND ASK. Show every gate's proposal block from step 2 in
   sequence order. Ask once, naming the whole phase: "mark any gate
   above whose decided value should differ from its proposal; every
   other gate in this batch stands on its own default (soft) or is
   stated with no response sought (advisory)." For any gate Abbott
   marks: set that gate's `marked: true`, set `decidedValue` to the
   amended value, and set `originalProposal` to the value step 2
   proposed before amendment (REQUIRED exactly here: the schema's
   own `human-amended` conditional, confirmed directly in
   `tools/validate-design-schemas.py`, and `phase-confirm.js`'s own
   refusal when it is missing). Re-write the plan file with the
   updated answers before handing off.

5. HAND-OFF. This command never writes `course-design_$1.json`. Once
   the draft file is complete, the write happens via `/land $1
   --phase-batch=$2 --draft=<plan file path>` (land.md's PHASE BATCH
   PATH, RJ-0061), which runs `tools/phase-confirm.js` against this
   draft. **That run must happen before `/scaffold` runs, when `$2`
   is a pre-scaffold phase (ONB or CRS)**: both land.md's PHASE BATCH
   PATH and this command state this. (The old per-lesson B7 batch
   boundary is retired with the B-gates; the post-scaffold LES, WRA
   and CXP soft gates batch per their own phase.) Print the hand-off
   command with `$1` and `$2`
   filled in, and the draft file's own path, so the next invocation
   needs no re-derivation.

6. AMEND RATE. `tools/phase-confirm.js` prints `marked`/`total` and
   which gate ids were marked; this command does not recompute it.
   The calling session logs that rate, once the confirm run has
   produced it, as a dated line in
   `docs/project/design-phase-logs/<slug>.md`: logged by the
   session, not written by the tool.

   VALIDATE BEFORE READ-BACK (RJ-0102). The same confirm run checks
   the record it just wrote against `tools/validate-design-
   schemas.py --course-design` before it renders anything. A record
   the validator refuses stops there: the validator's own named
   errors are printed and no read-back is rendered. The phase batch
   write itself still stands either way (report-failed-state, not
   rollback: the manifest is append-only by `tools/phase-confirm.js`'s
   own design, so this command does not retry or unwind it); a
   session seeing this refusal re-runs `/phase-draft` for the same
   phase to produce a corrected draft, rather than editing
   `course-design_$1.json` by hand.

   READ-BACK (RJ-0080). Once the record passes that check, the same
   confirm run renders the course design specification from it and
   writes it beside that record, never changing the record a second
   time. The tool's printed `readBack.specPath` names where it
   landed; `readBack.notReadyCount` is the render's own "Not ready"
   count at this point in the course. A render failure at this stage
   is named on stderr and does not undo the phase batch write that
   already stands; this command does not retry it.

7. FLAGGED TENSION (not resolved here, RULINGS 5 vs.
   `schemas/common.schema.json`'s provenance-enum description): see
   `tools/phase-confirm.js`'s own code comment for the full statement.
   In short, `confirmedAt` is stamped here on `ai-default-stood`,
   `ai-proposal-stood` and `advisory-stated` records (every record
   that stood on silence), never on `human-confirmed`, which this
   two-branch model has no path to produce.

Do not batch more than one phase into a single draft file. Do not
proceed to another phase in this invocation.
