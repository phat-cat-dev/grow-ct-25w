---
description: Create a brand-new course's manifest, once, after the four ONB gates are answered. The one exception to /land's append-only invariant.
argument-hint: <course-slug>
---

Cold-start for course `$1`. This runs ONCE per course, after the four
ONB gates — `onb-01_theme-preset`, `onb-02_course-theme`, `onb-03_pitch`
and `onb-04_naming` — have been opened via `/gate` and answered by the
human. It does not decide anything itself — it writes what those four
gates already decided into existence as
`courses/$1/course-design_$1.json`, because no manifest exists yet for
`/land` to append to. (`onb-04_naming` is the gate that mints the slug;
"no files can be created until answered" now attaches to it.)

Do not use this command if `courses/$1/course-design_$1.json` already
exists. Do not use it to answer the ONB gates — `/gate` and the human's
confirm do that; this command only writes the records already agreed.

`new-course.js` ALSO auto-states the six reserved CXS gates at creation
(Abbott, 8 Oct 2026, "reserved-gate record-writing"): CXS is
deterministic and course-level, so `cxs-01`..`cxs-06` are written with
`state: closed`, `provenance: advisory-stated` (GI-2), `cxs-04` carrying
the live `Harvard (Cite Them Right)` referencing default and the other
five a reserved `{value: "none", reserved: true}`. You do not supply
these in the answers file; the tool writes them itself. `cxp-03`
(reserved, CXP) is NOT written here — it is left to the CXP context-pack
flow.

1. RECON FIRST. Confirm `courses/$1/` does not exist, or exists with no
   `course-design_*.json` inside it. If a manifest is already there,
   stop — this is not a reopen, and `/new-course` never overwrites.

2. Collect the four closed ONB answers. Each gate's `decidedValue`,
   `provenance`, `grounding`, `confirmedAt` and `sessionRef`, exactly as
   `/gate` printed them and the human confirmed them — do not
   re-derive, re-propose, or amend any.

3. Write the four records to a scratch file (not committed; your
   scratchpad is fine). A gate record may carry any of `seq`, `state`,
   `provenance`, `decidedValue`, `originalProposal`, `grounding`,
   `groundingGaps`, `confirmedAt`, `deferReason`, `supersedes`,
   `alternativesConsidered`, `timestamp`, `sessionRef`, `reconstruction`
   and `provenanceDisputed` (`schemas/course-design.schema.json`'s
   `gates.records` item properties); copy every field the closed record
   actually carries. The answers object is keyed by the four ONB gate
   ids:
   ```json
   {
     "onb-01_theme-preset": { "state": "closed", "provenance": "...", "decidedValue": { "preset": "..." }, "grounding": [...], "confirmedAt": "gate", "sessionRef": {...} },
     "onb-02_course-theme": { "state": "closed", "provenance": "...", "decidedValue": { "theme": "...", "themeSource": "..." }, "grounding": [...], "confirmedAt": "gate", "sessionRef": {...} },
     "onb-03_pitch":        { "state": "closed", "provenance": "...", "decidedValue": { "pitch": "introductory|intermediate|advanced" }, "grounding": [...], "confirmedAt": "gate", "sessionRef": {...} },
     "onb-04_naming":       { "state": "closed", "provenance": "...", "decidedValue": { "pathwayName": "...", "tierName": "...", "slug": "$1" }, "grounding": [...], "confirmedAt": "gate", "sessionRef": {...} }
   }
   ```

4. Run `node tools/new-course.js --slug=$1 --answers=<scratch-file
   path>`. Paste its output in full, including the facetSet projection
   it prints (theme → `pathway`, pitch → `tier`), the line naming the
   six auto-stated CXS gates, and the validate results with their exit
   codes.

5. If it refused, the refusal names exactly what to fix; do not work
   around it.

6. SHOW-DIFF-STOP. Full `git diff` / `git status` for the new file.
   Explicit staging of `courses/$1/course-design_$1.json` only. One
   commit. No push.

7. Continue with `/gate $1 crs-01_sources`.

8. Once the ONB and CRS gates close (every gate `node
   tools/gate-order.js --closure-set=ONB` and `--closure-set=CRS` report
   is `closed` or `skipped`; read from the store, not this list), run
   `/scaffold $1` before opening any LES gate. /scaffold builds the page
   skeleton from `crs-04_lesson-map`; the per-lesson content (`les-01`),
   wrappers (`wra-*`) and context packs (`cxp-*`) come after it.
