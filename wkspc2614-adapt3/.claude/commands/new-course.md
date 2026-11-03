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

MULTI-TIER MODE (pathway-distillation, 2 Nov 2026): if `onb-03_pitch`'s
closed `decidedValue.pitch` is `"all"` rather than a single tier,
`new-course.js` takes a different, atomic path — it derives
`$1-introductory`, `$1-intermediate` and `$1-advanced` and writes all
three manifests together, each carrying a concrete `facetSet.tier` and
`profile: "pathway-distillation"`, with the same four ONB answers and six
auto-stated CXS records replicated into each (CXS runs once, conceptually
shared across the three tiers, but is still recorded per manifest since
each tier is its own Adapt course). This is all-or-nothing: if any of the
three target directories already exists, or any of the three manifests
fails `validate-design-schemas.py`, NONE are written (every partial write
in that invocation is rolled back). Steps 1, 3 and 5 below apply
per-manifest in this mode; steps 4, 6 and 7 differ as noted inline. `$1`
in this mode names the shared base slug (e.g. `zztest`), not a slug with
a tier suffix already on it — `new-course.js` refuses if `$1` does not
match `onb-04_naming`'s own slug.

1. RECON FIRST. Confirm `courses/$1/` does not exist, or exists with no
   `course-design_*.json` inside it. If a manifest is already there,
   stop — this is not a reopen, and `/new-course` never overwrites. In
   MULTI-TIER MODE, confirm all three of `courses/$1-introductory/`,
   `courses/$1-intermediate/` and `courses/$1-advanced/` are absent (or
   contain no `course-design_*.json`); any one of the three existing
   already is enough to stop, since the write is atomic across all
   three.

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
   codes. In MULTI-TIER MODE the same single invocation (pitch `"all"`
   read from the answers file, not a separate flag) writes and validates
   all three manifests; paste all three validate results.

5. If it refused, the refusal names exactly what to fix; do not work
   around it. In MULTI-TIER MODE a refusal at any point rolls back every
   manifest written in that invocation — re-run from a clean state, do
   not try to salvage one or two of the three.

6. SHOW-DIFF-STOP. Full `git diff` / `git status` for the new file.
   Explicit staging of `courses/$1/course-design_$1.json` only. One
   commit. No push. In MULTI-TIER MODE, stage and commit all three new
   manifests (`courses/$1-introductory/`, `-intermediate/`, `-advanced/`)
   together as one commit — they were written atomically and belong
   together.

7. Continue with `/gate $1 crs-01_sources`. In MULTI-TIER MODE, continue
   with `/gate $1-introductory crs-01_sources`, then the same for
   `-intermediate` and `-advanced` — crs-01_sources is a once-per-course
   gate like any other; there is no shared-source shortcut across the
   three tiers at this gate (CXS, not CRS, is what the profile shares
   conceptually — see MULTI-TIER MODE above).

8. Once the ONB and CRS gates close (every gate `node
   tools/gate-order.js --closure-set=ONB` and `--closure-set=CRS` report
   is `closed` or `skipped`; read from the store, not this list), run
   `/scaffold $1` before opening any LES gate. /scaffold builds the page
   skeleton from `crs-04_lesson-map`; the per-lesson content (`les-01`),
   wrappers (`wra-*`) and context packs (`cxp-*`) come after it.
