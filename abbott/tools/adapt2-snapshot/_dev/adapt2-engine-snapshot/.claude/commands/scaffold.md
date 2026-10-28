---
description: Generate a course's structural shell (config.json + five en/*.json files) from a course whose ONB and CRS gates have closed. Runs once per course, after CRS closes and before LES opens.
argument-hint: <course-slug>
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

Cold-start for course `$1`'s content model. This runs ONCE per course
(SG-1, `docs/project/open-decisions.md`, 18 September 2026), after the
ONB and CRS gates have closed (every gate `node tools/gate-order.js
--closure-set=ONB` and `node tools/gate-order.js --closure-set=CRS`
report is either `closed` or, where reachability was never met,
`skipped`; RJ-0059: read from the store, not this list) and before the
first LES gate opens. It writes only the Adapt content-model files
(`config.json`, `en/course.json`, `en/contentObjects.json`,
`en/articles.json`, `en/blocks.json`, `en/components.json`); it never
touches the manifest (`courses/$1/course-design_$1.json`), which is
`/new-course`'s territory alone. It is not run per lesson: every
lesson's page, articles and blocks are written in this one pass, from
`crs-04_lesson-map`'s lesson list.

Do not use this command if `courses/$1/config.json` or
`courses/$1/en/course.json` already exists — this tool does not
overwrite (see step 1(b)). Do not use it if the ONB and CRS gates have
not closed — running it early is a failed generator call, not a
graceful check (step 1(a) catches this first, before the generator is
invoked).

1. RECON FIRST.
   (a) Read `courses/$1/course-design_$1.json`. For every gate id
       `node tools/gate-order.js --closure-set=ONB` and `node
       tools/gate-order.js --closure-set=CRS` report (RJ-0059: read
       from the store, not this list), find the last record and
       confirm its `state` is `closed` or `skipped`. If any is missing,
       or its last record's
       `state` is anything else, STOP — name the gate and the state
       found (or "no record") — the ONB/CRS gates are not closed, and
       the generator's own refusal (`requireGate`) will not tell you
       which gate is the problem, only the first one it happens to
       check (`onb-04_naming`, then `crs-04_lesson-map` — see
       `tools/generate-course-shell.js`'s `requireGate` calls).
   (b) Confirm `courses/$1/config.json` does not exist AND
       `courses/$1/en/course.json` does not exist. If either does,
       STOP and quote what is there — do not delete anything. (This
       mirrors the generator's own `requireCleanOutput`, checked here
       first so the stop is a plan-time finding, not a `REFUSED:`
       exit.)

2. RUN THE GENERATOR.

       node tools/generate-course-shell.js --manifest=courses/$1/course-design_$1.json --out=courses/$1

   `--out` is `courses/$1`, matching where the manifest already lives
   — `manifest-completeness.js`'s `resolveCourse()` (`tools/lib/
   course-resolve.js`) checks the `courses` root before
   `courses/_generated`, and only finds a course's shell and its
   manifest together when both sit in the same directory. Paste the
   full console output, including the four printed lines (`Wrote
   shell to...`, the `Pages/Articles/Blocks/Components` counts,
   `_latestTrackingId`, and the deferred-blocks count). A non-zero
   exit or a `REFUSED:` line stops here; do not work around it.

3. CHECK: `manifest-completeness.js` clause 4 is this command's own
   proof of write; clauses 1, 2, 3 and 6 are NOT.

       node tools/manifest-completeness.js --course=$1
       echo "EXIT: $?"

   Paste the full output. Read clause 4 ("Scaffold outputs") as the
   check this command answers for: it must PASS, with `config.json`
   and all four `en/*.json` files `FOUND`. Clauses 1, 2, 3 and 6 are
   EXPECTED to FAIL on a fresh shell, for reasons this command does
   not own and does not fix — none of the four reads or writes
   anything `generate-course-shell.js` touches (it writes only
   `config.json` and `en/*.json`; it never touches the manifest's
   `gates` or `instantiations`, and never touches
   `content/context-packs/`):
   - Clause 1 (gate coverage) fails because none of this course's
     lessons yet has any `les-01` gate record — that is the LES
     phase's job, one lesson at a time via `/gate` and `/land`.
   - Clause 2 (instantiations) fails because `instantiations[]` is
     still empty while `en/contentObjects.json` now has real pages —
     the same LES work adds an `instantiations` entry per lesson with
     content (`land.md` step 4).
   - Clause 3 (context packs imply cxp-04) fails if any subject already
     has lesson-level context-pack files for this course under
     `content/context-packs/<subject>/$1/` (WF-B/`new-context.md` can
     run before LES, against a course whose ONB/CRS gates have closed)
     while `cxp-04_context-generation` has no record yet — the cxp-04
     gate is decided via `/gate` and `/land` like any other, and this
     command never opens or writes a gate.
   - Clause 6 (slotKey resolution) fails because it iterates
     `instantiations[]` and finds zero entries to check ("0 items
     checked" is `manifest-completeness.js`'s own `clause()` wrapper
     forcing a FAIL, not this command's doing).

   The overall run printing `manifest-completeness: FAILED` with
   exactly clauses 1, 2, 3 (if this course already has context packs)
   and 6 failing, and clause 4 (and 5) passing, is the expected,
   correct result of a fresh shell — state this plainly rather than
   reading these failures as the scaffold having failed. Any OTHER
   clause-4 failure, or a clause-4 pass alongside a different failing
   clause not on this list, is a real finding: stop and report it
   rather than proceeding to commit.

4. SHOW-DIFF-STOP. Full `git diff` / `git status` for the six written
   files. Explicit staging of exactly `courses/$1/config.json`,
   `courses/$1/en/course.json`, `courses/$1/en/contentObjects.json`,
   `courses/$1/en/articles.json`, `courses/$1/en/blocks.json` and
   `courses/$1/en/components.json` — never `git add -A`. One commit,
   message `scaffold: $1 shell (<n> pages, <m> deferred blocks)` using
   the generator's own printed counts from step 2, not a recalculation.
   No push.
