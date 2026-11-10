# Runbook - build a course end to end

The commands, in order. Conceptual background is in `docs/PIPELINE.md`; the
component map is in `docs/ARCHITECTURE.md`.

Two rules that are not optional:
- Confirm `pwd` is the repo root before any command.
- Never run raw `adapt install`. Use `npm run adapt-install` (it installs, then
  reapplies the `patches/` vendor fixes). Raw `adapt install` silently wipes them.

## 0. One-time setup

```
git submodule update --init --recursive  # pull the 13 pathway repos + context-cmet
npm ci                 # install node deps against the committed lockfile
npm run adapt-install  # install core/menu/theme + adapt-contrib-* and reapply patches
```

Each of the 13 single-tier pathways (`courses/<pathway>/`) is its own repo on
`modules-branch`, wired in as a submodule - a fresh clone has empty pathway
directories until `git submodule update --init` runs. `presenting-v2`/
`referencing-v2` are not submodules; they are archived in-tree at
`courses/_archive/v2/`.

`npm run adapt-install` is what populates `src/core`, `src/menu`, `src/theme` and
the contrib plugins listed in `adapt.json`. They are not vendored in git.

## Stage A - consult & specify (produces the manifest)

Work the six phases in order. `/gate` opens a gate read-only (plan mode); `/land`
writes the confirmed answer (execute mode). Each git add/commit/push is its own
confirmed step; nothing is committed silently.

1. **ONB.** Open and answer `onb-01`..`onb-04` with `/gate`. Then run once:
   ```
   /new-course <slug>
   ```
   This creates the manifest from the four answers and auto-states the reserved
   CXS gates. Where it lands depends on `onb-03_pitch`: a single-tier pitch
   writes `courses/<pathway>/shell/generic/<slug>/course-design_<slug>.json`
   (`<pathway>` is `<slug>` with its tier suffix stripped); pitch `"all"`
   writes three sibling manifests at
   `courses/<theme>/shell/generic/<theme>-<tier>/course-design_<theme>-<tier>.json`
   (`profile: "pathway-distillation"`). See `courses/README.md`.
2. **CXS.** All six gates auto-pass for now; `/new-course` has already stated
   them. Nothing to do unless a CXS gate is being wired for real.
3. **CRS.** `/gate` then `/land` for `crs-01`..`crs-05` in order. crs-02 proposes
   scope + thematic strands; crs-03 the outcomes; crs-04 the lesson map; crs-05
   assembles the course spec (auto-stands).

When every ONB and CRS gate reads `closed` or `skipped`:
```
node tools/gate-order.js --closure-set=ONB
node tools/gate-order.js --closure-set=CRS
```

## Stage A to B - scaffold the shell

```
/scaffold <slug>
```
Fuses the manifest with the archetypes and writes `config.json` + the five
`en/*.json` files, one page per lesson, with interior/activity slots emitted as
**deferred blocks** (empty `_id`s) for LES/WRA to fill.

Expected afterwards (a fresh shell is intentionally not yet buildable):
```
node tools/manifest-completeness.js --course=<slug>   # clause 4 (scaffold) PASSES;
                                                       # clauses 1/2/6 FAIL (no content yet) - correct
```

## Stage B - author content, then compile

4. **LES.** For each lesson in the lesson map: `/gate` then `/land` for
   `les-01_lesson-proposal`. The agent proposes pedagogy-led slot content; you
   confirm or amend; `/land` writes it and records an instantiation.
5. **WRA.** `/land` `wra-01_wrapper-open`, `wra-02_wrapper-close`,
   `wra-03_summative`, `wra-04_confidence`.
6. **CXP (optional, per subject).** `/cxp-open <slug>` once, then
   `/new-context` to author a pack. `merge-context.js` slots the pack into the
   shell's coupled components.

After each `/land`, verify the result before moving on:
```
node tools/verify-course.js --course=<slug>
python3 tools/validate-design-schemas.py --course-design courses/<pathway>/shell/generic/<slug>/course-design_<slug>.json
node tools/conformance-lint.js --course=<slug>
node voice-lint.js --course=<slug>
```
(`<pathway>` is `<slug>` with its tier suffix stripped; `verify-course.js`,
`conformance-lint.js` and `voice-lint.js` resolve the slug themselves via
`tools/lib/course-resolve.js`, which checks both the flat and nested locations)

7. **Build.** Point the build at the course and compile. A course builds cleanly
   only once **fully** authored (every deferred block filled); `check-json`
   aborts while any deferred block still has an empty `_id`.
   ```
   ls -l src/course                                                    # note the current symlink target
   ln -sfn ../courses/<pathway>/shell/generic/<slug> src/course         # <pathway> = <slug> minus its tier suffix
   npx grunt build                                                     # a fully authored course builds clean
   ```
   On a partly authored shell, `grunt build` aborts at `check-json` (exit 3) -
   that is expected, not a fault. `npx grunt build --force` will build a shell by
   suppressing that check (dev convenience only).

   A real pass leaves a FRESH `build/imsmanifest.xml` AND compiled `build/*.css`.
   `build/` is gitignored and can hold a stale manifest from an earlier run; do
   not accept an old manifest as proof.

8. **Preview (optional).**
   ```
   npx grunt server-scorm        # serves build/ with a dummy SCORM harness
   ```
   Note: `server-scorm` serves `build/`, it does not build it. Run `grunt build`
   first and confirm the served course title matches. Default port is `9000`.

   To preview a tier's build alongside the others instead of replacing
   whatever is currently linked at `src/course`, stage it into its own
   reserved, locked-port server (`grunt/tier-servers.js`):
   ```
   npx grunt stage-tier:introductory     # copies build/ -> build-introductory/
   npx grunt server-introductory         # plain preview, locked to :9001
   npx grunt server-introductory-scorm   # SCORM harness, same build, locked to :9011
   ```
   `intermediate`/`advanced` work the same way, on `:9002`/`:9012` and
   `:9003`/`:9013`. Use the plain preview port for day-to-day review after
   each rebuild + restage; reach for the `-scorm` port only to check
   tracking behaviour before a Moodle upload. Each pair is printed on its
   own hostname (`introductory.localhost`, etc.), not plain `localhost` -
   SCORM state lives in a single `_spoor` cookie scoped by host, not port,
   so three *tiers* sharing `localhost` would overwrite each other's
   tracking (the preview/SCORM pair within one tier sharing a hostname is
   fine - same course, same tracking). `stage-tier` refuses a stale or
   missing `build/`; pass `--force` to stage anyway.

## Stage C - verify, package, hand off

```
node tools/verify-all-courses.js
node --test tools/test/*.test.js
```

Package the build (commit first; package names embed the HEAD commit hash, and
`build-all-packages.js` refuses a dirty tree):
```
node package-scorm.js --context=<subject> --tier=<slug>    # single pair
# or
node tools/build-all-packages.js                           # all pairs → scorm-packages/
```

Then the manual steps (no Moodle access from here):
- Upload the zip to Moodle as a SCORM activity (`docs/testing/moodle-upload-instructions.md`).
- Walk the Moodle checklist (`docs/testing/p8-moodle-walkthrough-checklist.md`).

Automated browser checks against a local server, before Moodle:
```
node test-browser-checklist.mjs
node test-accessibility-scan.mjs
node test-focus-sequence-scan.mjs
```

## Quick reference

| You want to | Do |
|---|---|
| start a new course | `/gate` ONB gates, then `/new-course <slug>` |
| see a course's state | `/ledger <slug>` |
| build the shell | `/scaffold <slug>` (after ONB+CRS close) |
| author a lesson | `/gate` + `/land` `les-01` (per lesson) |
| add a subject version | `/cxp-open <slug>` then `/new-context` |
| compile to SCORM | `grunt build` then `package-scorm.js` |
| reopen a decision | `/reopen` |
