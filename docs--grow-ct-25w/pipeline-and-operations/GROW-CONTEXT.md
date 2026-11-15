# GROW-CONTEXT — the gate→manifest authoring engine

**What it is:** the tooling that turns design *decisions* into course *source*,
with no Adapt build involved. Decisions are captured through "gates", written into
a manifest, scaffolded into an Adapt content shell, and optionally overlaid with
subject context. Pure JSON + Node + Python + markdown.

## The pipeline
Phases of gates: **`ONB → CXS → CRS → LES → WRA → CXP`**. A gate = one decision.
1. **Gate → manifest** — gate skills record decisions into `courses/<slug>/course-design_<slug>.json`.
2. **Manifest → shell** — `tools/generate-course-shell.js --manifest=… --out=courses/<slug>` emits `config.json` + `en/*.json` (one page per lesson, deferred slots for later gates).
3. **Shell + context → variant** — `merge-context.js --context=<subject> --tier=<slug>` overlays authored prose → `courses/_generated/<tier>-<context>/`.

## Gate skills (`.claude/commands/`)
`gate` (open one gate, read-only) · `land` (write a confirmed gate record) ·
`new-course` (create the manifest, once) · `scaffold` (manifest→shell) ·
`new-context` (author a context pack) · `cxp-open` · `ledger` · `phase-draft` ·
`reopen` · `publish`.

## Data stores (pure JSON)
- `design-kb/` — design knowledge base: gates grammar, skeletons, palette, pathways, activity-patterns, content shapes/conventions, tier-bands, `section-schemas/`.
- `schemas/` — JSON Schemas validating the KB + manifests (`course-design.schema.json`, …).
- `catalogue/` — cross-course pathways + context correspondences.
- `source-kb/` — provenance / source maps.
- `content/context-packs/<subject>/<slug>/` — authored prose packs `merge-context.js` consumes.

## Engine code
- `tools/*.js` — `new-course`, `generate-course-shell`, `gate-order`, `phase-confirm`, `manifest-completeness`, `render-course-spec`, verify/lint, course import/export.
- `tools/*.py` — `validate-design-schemas.py`, `validate-gate-record.py`, KB builders.
- `tools/lib/` — shared libs (`course-resolve`, `phase-gate`, `page-match`, …).
- `merge-context.js` (repo root).

## Standalone
Everything above is pure JSON + Node + Python + markdown and could be lifted out to
its own repo **without `src/` or `grunt/`** (deps: Node builtins + `fs-extra`;
Python + `jsonschema`). The only bridges back into the build are `package-scorm.js`
(runs `grunt build`) and the theme-token / LESS tools (`tools/adapt-ab/*`,
`tools/lib/adapt-less-layers.js`, `course-css-export.js`) that read `src/` theme LESS.
`grow-ct/tools/manifest-generator/` was an early, partial extraction of this engine.

## Known issue
The generated `en/course.json` uses `_remainingAttemptsText` / `_remainingAttemptText`
(underscore-prefixed). The correct Adapt mcq-globals form is **without** the
underscore (confirmed by the grow-ct fix, commit `5594e60`). Fix at the
shell-generation source so output stops needing hand-patching downstream.
