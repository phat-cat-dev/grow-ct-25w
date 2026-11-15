# System overview — grow-ct-25w, as it stands

**Written:** 2026-11-10, directly from source inspection, before the documentation
reorg that produced this tree. Every figure below carries the command to
re-derive it — re-run those commands before trusting a number here that is more
than a few weeks old.

---

## 1. What this is, in five sentences

This is an academic-skills e-learning programme — **Academic Practice
eLearning** — built on the [Adapt Framework](https://www.adaptlearning.org/)
(v5.56.2), packaged as SCORM and delivered through Moodle. Content is a matrix
of 13 academic-practice **pathways** at 3 tiered **pitches**
(introductory/intermediate/advanced), sourced from *Excelling at University*
(Dennis & Abbott, 2026) plus new material authored to the same voice. It is
not one pipeline but **two cooperating systems**: **GROW-CONTEXT** (a guided
gate conversation that turns pathway+pitch into a JSON manifest — pure
Node/Python, no browser) and **GROW-BUILD** (the Adapt fork that turns a
manifest-driven course shell into a playable, then SCORM-packaged, course).
The hinge between them is the **manifest** — an append-only JSON record of
every authoring decision, read by the builder to scaffold, fill, compile and
package.

## 2. The pipeline, end to end

```
ONB → CXS → CRS → LES → WRA → CXP          (6 phases, the gate conversation)
  │
  ▼
course-design_<slug>.json                   (the manifest — GROW-CONTEXT's output)
  │
  ▼
generate-course-shell.js                     (fuses manifest + design-kb archetypes)
  │
  ▼
courses/<pathway>/shell/generic/<slug>/      (authored JSON: config/course/
  en/{config,course,contentObjects,           contentObjects/articles/blocks/
      articles,blocks,components}.json        components .json)
  │
  ▼
merge-context.js                             (fills in subject context pack)
  │
  ▼
grunt build  (src/course → build/, via the symlinked shell)
  │
  ▼
package-scorm.js  →  scorm-packages/*.zip    (imsmanifest.xml at zip top level)
```

**The manifest path is nested, not flat:**
```
courses/<pathway>/shell/generic/<slug>/course-design_<slug>.json
```
(e.g. `courses/criticality/shell/generic/criticality-introductory/course-design_criticality-introductory.json`).
Several existing docs (`ARCHITECTURE.md`, `GROW-CONTEXT.md`) wrote this flat as
`courses/<slug>/course-design_<slug>.json` — that form **does not exist on
disk**; corrected copies are in `pipeline-and-operations/`.

Two course layouts coexist:
- **13 pathway submodules** at `courses/<pathway>/`, one Git submodule each (see
  `.gitmodules`) — the live, maintained set.
- **`courses/_archive/`** — `v2/` (presenting-v2, referencing-v2, in-tree, not
  submodules) and `courses-2026-09/` (flat pre-reorg layout, pre-dates the
  `shell/generic/` nesting).

Re-derive the manifest count:
```bash
find wkspc2614-adapt3/courses -name 'course-design_*.json' | wc -l
```

## 3. Verified plugin inventory

Every existing doc's plugin-count table was wrong in some way. This is the
corrected table, dated 2026-11-10:

| | Total | `adapt-contrib-*` (upstream) | `adapt-grow-*` (custom) | `adapt-abbott-*` (custom, legacy name) |
|---|---|---|---|---|
| `src/components/` | 58 | 14 | 44 | 1 (`adapt-abbott-timeline`) |
| `src/extensions/` | 16 | 9 | 7 | 0 |

The 7 custom extensions: `adapt-grow-layer`, `adapt-grow-mode`,
`adapt-grow-pagenav`, `adapt-grow-phasenotes`, `adapt-grow-studio`,
`adapt-grow-journal-extension`, `adapt-grow-trickle-button`.

Both `adapt-abbott-timeline` and `adapt-grow-timeline` exist side by side —
not a duplicate, two different components (see
`component-specs/timeline.md` vs `component-specs/grow-timeline.md`).

Re-derive:
```bash
ls -d wkspc2614-adapt3/src/components/*/  | xargs -n1 basename | sort
ls -d wkspc2614-adapt3/src/extensions/*/  | xargs -n1 basename | sort
```

## 4. Documentation coverage, honestly stated

| Surface | Documented | Undocumented |
|---|---|---|
| Components (44 `adapt-grow-*` + 1 `adapt-abbott-*`) | 38 specs (1 of which, `hotspot.md`, documents a component that doesn't exist) | 19: `adapt-grow-{animations,annotate,cloze,corkboard,expanding-links,guided-chat,journal,levels,memory,outcomes,pagenotes,promptbuilder,reflection-module,sandbox,scenario,scroll-scenes,show_working,tutor,wizard}` |
| Extensions (7 `adapt-grow-*`) | 2 specs (`grow-layer.md`, `grow-phasenotes.md`) | 5: `mode`, `pagenav`, `studio`, `journal-extension`, `trickle-button` |

Re-derive:
```bash
ls wkspc2614-adapt3/docs--grow-ct-25w/component-specs/*.md | wc -l   # after this reorg
ls -d wkspc2614-adapt3/src/components/adapt-grow-*/ | wc -l
```

## 5. Naming reality

Code was renamed `adapt-abbott-*` → `adapt-grow-*` at some point; the rename
did not reach every spec heading. 22 component-spec files still open with an
`adapt-abbott-*` plugin id in their title even though the only surviving
`adapt-abbott-*` component is `adapt-abbott-timeline`. This consolidation
**flags** every affected file (status table, each folder README) but does
**not** bulk-rename them — that is a deliberately deferred, separately-scoped
job, because 22 simultaneous content edits are hard to review as a batch and
easy to get subtly wrong (e.g. `gowtimeline.md` turned out not to be a dead
file but a second, real component).

## 6. Theme state

The active theme is `_grow` (vanilla's successor); `adapt-contrib-vanilla` is
excluded from the build. Inside the theme:

- **Live today:** the `--cm-*` token layer (Cardiff Met-specific) and the
  single-hue + type/space-scale token engine described in
  `theme-and-design-system/grow-base-architecture.md` §1-3.
- **Target, not yet built:** the six-layer `--ab-*` cascade and the
  `00-interface/ 10-profiles/ 20-core-bridge.less 30-paint/` LESS restructure
  described in `grow-base-architecture.md` §4 — its own §6 labels this a
  migration plan, not a current-state map. Actual LESS layout today is
  `_defaults/ core/ plugins/ project/`.
- **Authored but not wired:** the `section-schemas.md` token-shape spec — the
  fold tool that would consume it has not been built.

## 7. Known gaps and debt

This section is why this document exists — it names what every prior doc
assumed was fine.

- **The decision record doesn't exist.** `docs/project/open-decisions.md` is
  cited **136 times** across this codebase, including 9 times by
  `.claude/commands/land.md` as the authority for live decisions (GI-2, DR-1,
  MK-1, AL-3, AL-5, Prompt 173), and by 6 `schemas/*.json` files. It is not on
  disk, not in this repo's git history, and not in the sibling
  `wkspc2615-grow-course` workspace. Same situation for `project-backlog.md`
  (23 refs), `audit-2026-09/audit-actions-arising.md` (21),
  `design/gate-conversation-model-draft-v1.md` (6), `away-week-log.md` (3),
  `pedagogy-log.md` (2). `gating-and-manifest/open-decisions.md` and
  `project-backlog.md` in this tree are **seeded reconstructions** from
  `BACKLOG.md` and the gate store, clearly banner-marked — not the original
  record.
- **Dead plugin, live config.** `adapt-abbott-pass-reveal` no longer exists in
  `src/extensions/`, but `_passReveal` config is still emitted by
  `tools/generate-course-shell.js`, three `design-kb/design-kb.*.json` stores,
  matching `schemas/*.schema.json`, `.claude/commands/land.md`, and 6 archived
  course JSON files.
- **Cross-workspace fragility.** `abbott/sa-docs/{gating,querying}/` held 6
  symlinks resolving to absolute paths in a *different* sibling workspace
  (`wkspc2615-grow-course`), not this one. All 6 targets have local
  equivalents; the symlinks were dropped rather than carried forward.
- **`abbott/sa-docs/*.md` was untracked.** 37 files, mostly duplicates of
  `docs/authoring/`, sitting outside version control. The one genuinely
  unique file (`database-link-logic.md`) is now in `institutional-context/`.

## 8. How to re-derive every number above

```bash
# Plugin inventory (§3)
ls -d wkspc2614-adapt3/src/components/*/ | xargs -n1 basename | sort
ls -d wkspc2614-adapt3/src/extensions/*/ | xargs -n1 basename | sort

# Manifest count and path shape (§2)
find wkspc2614-adapt3/courses -name 'course-design_*.json'

# Doc coverage gaps (§4) — components with no spec
comm -23 \
  <(ls -d wkspc2614-adapt3/src/components/adapt-grow-*/ | sed 's#.*/##;s#/$##' | sort) \
  <(ls wkspc2614-adapt3/docs--grow-ct-25w/component-specs/*.md | xargs -n1 basename | sed 's/\.md$//' | sort)

# Phantom doc reference counts (§7)
grep -rc 'open-decisions' --include=*.md --include=*.json --include=*.js \
  --exclude-dir=node_modules --exclude-dir=build wkspc2614-adapt3 | \
  awk -F: '{s+=$2} END {print s}'

# _passReveal live-debt surface (§7)
grep -rl '_passReveal' --include=*.json --include=*.js wkspc2614-adapt3 \
  --exclude-dir=node_modules
```

## 9. Map to this docs tree

| Folder | What it answers |
|---|---|
| `pipeline-and-operations/` | How does a course get built, end to end, and what are the operating rules? |
| `curriculum-and-pathways/` | What are the 13 pathways × 3 tiers, and how do they map to the source book? |
| `gating-and-manifest/` | How does the gate conversation produce and structure the manifest? |
| `authoring-method/` | How should an agent/author write content so it fits the system and voice? |
| `lesson-model-and-templates/` | What shape does a lesson/wrapper/page take, concretely? |
| `component-specs/` | What does each Adapt component do and how is it authored? |
| `extension-specs/` | What do the custom runtime extensions do? |
| `theme-and-design-system/` | How does the GROW token/theme engine work? |
| `adapt-platform-reference/` | What does vanilla Adapt provide, and where does GROW extend it? |
| `testing-and-release/` | How is a build verified and packaged for Moodle? |
| `institutional-context/` | What Cardiff Met-specific data (courses, schools, citation links) feeds the content? |
| `proposals-and-open-decisions/` | What is proposed but not landed, or genuinely unresolved? |
| `archive/recovered-from-git/` | What was deleted from history and worth keeping? |
