---
description: Reopen a closed gate. Preview its dependents by class, gather Abbott's dispositions, then write the new record and the sweep event in one run. Finding F5.
argument-hint: <course-slug> <gate-id e.g. crs-03_course-outcomes>
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

You are reopening gate `$2` for course `$1` (RJ-0062, adp-0216). This
closes finding F5: reopening (scope preview, then a sweep) was designed
in the gate model (`docs/design/gate-conversation-model-draft-v1.md`
5) and in the record schema's `sweepEvents` array, but no command ran
it. Steps 1 to 4 run in plan mode and write nothing but this session's
plan file (GDP-1). Step 5 is the one write this command makes, and it
runs `tools/reopen.js` directly; there is no `/land` path for a reopen
(RJ-0062 did not touch `land.md`).

Out of scope here: `gates/$2` carrying `propagationScope: "universal"`
(gate-conversation-model-draft-v1.md 5.4). A universal-scope gate's
sweep runs the change-kind tracer rule over every gate, not this
tool's static `dependsOn` net; `tools/reopen.js` refuses it (reading
the store entry generically, not by a hardcoded id) rather than
reporting an empty dependents list. NOTE: no gate in the current store
carries `propagationScope: "universal"`, so this carve-out has no live
target now; it is retained for a future gate that adds one, which would
need that tracer rule built first.

1. RECON. Confirm `courses/$1/course-design_$1.json` exists and carries
   at least one record for `gates/$2`; state its current seq, state and
   provenance. State why `gates/$2` is being reopened in one sentence
   (what moved) before going on.

2. PREVIEW. Run:

       node tools/reopen.js --preview --gate=$2 --course-design=courses/$1/course-design_$1.json
       echo "EXIT: $?"

   Paste both lines verbatim. The tool's own output is the scope
   preview (`gate-conversation-model-draft-v1.md` 5.5, beat one):
   `gates/$2`'s current seq and every other gate whose own `dependsOn`
   array names it, each with its `dependencyClass`. Print each
   dependent's class-level default verdict beside it (constitutive ->
   invalidate, substantive -> flag-for-review, nominal ->
   stand-with-warning, `design-kb.gates.schema.json`'s own `dependsOn`
   description; `gate-conversation-model-draft-v1.md` 5.2-5.3): the
   edge class is the default, Abbott disposes next, not this command.
   A non-zero exit here (not in the store; no record to reopen;
   universal scope) stops the run; do not proceed to step 3.

3. NEW DECISION.
   **Published-course edit-mode (`docs/authoring/field-locks-and-edit-mode.md`).**
   If the manifest's `status` is `production` (published), this reopen is a
   PATCH, not a regeneration: carry the superseded record's `decidedValue`
   forward verbatim and change ONLY the field(s) this reopen targets. Name
   those paths in the draft's `unlocked` array (dot-paths into decidedValue,
   e.g. `["check.items"]`). `tools/reopen.js` refuses any change outside the
   unlocked set, and the lint refuses it at every landing. Do NOT re-propose
   or regenerate locked (untargeted) fields; that is exactly the regeneration
   this guards against. A full re-proposal is reserved for an explicit,
   deliberate redesign in which every changed path is unlocked.

   If the course is still `in-development` (not yet published): run `gate.md`'s
   own steps 2 to 6 for `gates/$2` as `/gate` would, producing its new proposal
   (nothing is locked yet; no unlock needed). This command holds no gate logic
   of its own for the reopened gate itself.

   Either way, record the `changeKind`: `amended` (same decision, refined),
   `replaced` (a different decision entirely) or `re-deferred` (reopened back
   into `deferred`). One sentence naming the change, for the sweep event's
   `trigger.note`.

4. DISPOSITIONS. For each dependent the preview named, show its class
   and default verdict from step 2 and ask Abbott once, as a labelled
   set (`gate-conversation-model-draft-v1.md` 5.5: "flag-for-review
   defaults are bulk-confirmable as a labelled set"), whether each
   stands on its default or is amended to a different verdict.
   Invalidate defaults are individually named, each needing Abbott's
   own explicit word (5.5: "individually named"), never bulk-confirmed
   alongside the others. For every dependent: `mode` is `confirmed`
   (the default verdict stands as given), `amended` (a different
   verdict, `note` required by the schema exactly there) or `stood`
   (silence; only open to a stand-with-warning or flag-for-review
   default, never to invalidate, which the 5.5 individually-named rule
   above already rules out). `resolution: {status: "open"}` on every
   `invalidate` and `flag-for-review` disposition; no `resolution` on
   `stand-with-warning`.

5. DRAFT FILE (GDP-1). Write the whole draft to this session's plan
   file before showing it, print the path, and re-read it after any
   compaction or clear. Shape, matching `tools/reopen.js`'s own
   documented input exactly:

   ```json
   { "changeKind": "amended", "note": "one sentence from step 3",
     "provenance": "human-specified", "decidedValue": {"...": "..."},
     "unlocked": ["check.items"],
     "dispositions": [
       { "gate": "crs-03_course-outcomes", "verdict": "invalidate", "mode": "confirmed",
         "resolution": { "status": "open" } }
   ] }
   ```

6. APPLY. Print the exact command, with `$1`, `$2` and the plan file's
   path filled in, and run it:

       node tools/reopen.js --course-design=courses/$1/course-design_$1.json --draft=<plan file path> --gate=$2
       echo "EXIT: $?"

   This is the one write this command makes: the tool itself appends
   `gates/$2`'s new record (`supersedes` citing the record it
   replaces) and the sweep event, in the shape
   `schemas/course-design.schema.json`'s own `sweepEvents` item defines
   (quoted in full in `tools/reopen.js`'s own header comment). A
   non-zero exit (a dependent with no disposition; a disposition
   missing its schema-required `note` or `resolution`) refuses the
   write; the manifest is left untouched. SHOW-DIFF-STOP as `land.md`'s
   own step 6: show the diff, run the self-check, then one commit for
   the whole reopen (new record plus sweep event together, one logical
   unit). No push.

7. AFTERMATH (`gate-conversation-model-draft-v1.md` 5.5). A confirmed
   `invalidate` reopens its own gate into the normal conversation under
   its own hardness: run this same `/reopen` command again (or `/gate`,
   if the dependent itself has no dependents of its own to sweep) for
   each invalidated dependent, naming it from this run's sweep event. A
   `flag-for-review` persists in the event and blocks that course's
   build-readiness (the 5.13 lint refuses on an unresolved event) until
   it is re-affirmed, escalated or demoted; name the open flags left
   behind. A `stand-with-warning` needs nothing further. State all
   three buckets plainly before ending the run; do not resolve a flag
   silently inside this same invocation.

Do not batch more than one gate's reopen into a single draft file. Do
not proceed to another gate in this invocation.
