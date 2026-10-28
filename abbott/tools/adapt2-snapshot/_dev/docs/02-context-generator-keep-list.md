# grow-context extraction — keep-list & sweep sheet

> **Written for:** Stuart, as the "sweep" checkpoint before anything is split out.
> This proposes what the isolated engine — package name **`grow-context`** (phase-1: gated
> proposal grammar → manifest → Adapt-populating JSON) — should contain, and what stays behind
> with the hard-forked Adapt build side. Nothing has been moved — this is a proposal to review.
>
> **Decisions locked (2026-10-19, final):** lands in **this repo** at `tools/grow-context`
> (not a standalone repo) · name `grow-context` · the adapt2 lesson was built/served for styling ·
> landed as a **verbatim reference snapshot** at [`../adapt2-engine-snapshot/`](../adapt2-engine-snapshot/)
> (see its README for provenance + the adapt2→GROW mapping).
> **Theme/token system is OUT** — `design-kb/section-schemas/` and `tools/adapt-ab/` are NOT brought
> (grow-ct owns structure, not look; they belong to the theme-builder). Only `theme-mapping`'s
> structural **spine** (`adapt-template-classes.*`) is kept, as read-only reference.
> *(This supersedes the earlier "KEEP section-schemas + adapt-ab" note; the KEEP table below predates the
> reversal — the snapshot README is authoritative.)*
>
> Legend: **KEEP** = goes into the isolated engine · **EXCLUDE** = stays with the Adapt
> fork · **DECIDE** = genuine judgement call, flagged for you.

---

## What the engine *is* (the thing we're isolating)

The first phase: six gated phases (ONB → CXS → CRS → LES → WRA → CXP), 24 gates, defined in
`design-kb/design-kb.gates.json`. Decisions are recorded in an append-only manifest; the
`/scaffold` step emits the six Adapt JSON files; `/land` fills deferred slots; `merge-context.js`
slots subject packs in. It operates **purely on JSON + stores** — no `src/`, `build/`, `grunt`, or
`node_modules/adapt` dependency. That clean separation is what makes the extraction viable.

---

## KEEP — the engine

| Path | What it is |
|---|---|
| `.claude/commands/*.md` | The 10 skills: gate, land, new-course, scaffold, new-context, cxp-open, ledger, phase-draft, reopen, publish |
| `.claude/agents/reviewer.md` | Read-only second reader invoked after `/land` |
| `design-kb/*.json` | The stores the grammar reasons from: gates, skeletons, palette, activity-patterns, content-shapes, content-conventions, tier-bands, pathways |
| `schemas/*` | Schemas governing stores + manifest (`course-design.schema.json` = the manifest, `common.schema.json`, all `design-kb.*`, `catalogue.*`, `source-kb`, `source-map`, `institutional-kb`, `hecos-kb`, `vocab-kb`) |
| `reference/*` | `excelling-at-university.md` (606 KB source book), `excelling-voice-specification.md` (voice contract), `excelling-linguistic-audit.md` |
| `source-kb/source-maps/*` | Chunked/tagged book map — single source of truth for chunk text |
| `catalogue/*` | 13-pathway registry (`pathways.json`, `pathways/*`) + `context/` correspondence data |
| `integrations/mapper/` | Subject ↔ HESA ↔ pathway profiles (feeds subject/pathway resolvers) |
| `tools/` **engine subset** | `new-course.js, gate-order.js, phase-confirm.js, render-course-spec.js (+fields json), resolve-agent-author.js (+test), validate-gate-record.py, cxp-open.js, publish.js, reopen.js, generate-course-shell.js, verify-course.js, verify-all-courses.js, manifest-completeness.js, validate-design-schemas.py, conformance-lint.js, session-audit.js, component-map.js, template-field-map.js, merge-health.js` |
| `tools/lib/` | `course-resolve.js, phase-gate.js, page-match.js, content-version.js, script-sync.js` |
| `tools/subject/`, `tools/pathways/` | Subject/benchmark + pathway resolution data (CAH/HECOS vocab) |
| `tools/doc-templates/` | `course-pack.*`, `lesson-plan.*` templates |
| `tools/test/`, `tools/test-fixtures/` | Engine unit tests |
| `merge-context.js` (root) | CXP merge — slots subject prose into coupled components |
| `voice-lint.js` (root) | Copy vs voice spec |
| `docs/PIPELINE.md`, `docs/ARCHITECTURE.md`, `docs/RUNBOOK.md`, `docs/authoring/` | The prose the gate grammar's `prosePointer`/`specPointer` fields reference |
| `CLAUDE.md` (adapted) | Working rules — will need trimming to the engine's scope |
| **`design-kb/section-schemas/`** | Design-token definitions (colour, typography, spacing, icons, breakpoints, motion, semantics, box-model, container-queries, accent-spectrum + adapters) — token reference for grow-context's own page templates |
| **`tools/theme-mapping/`** | Generates the structural "spine" selector map (`adapt-template-classes.json/.less`) — the page-structure reference you'll template against |
| **`tools/adapt-ab/`** | The CSS/token computation engine that folds section-schemas and computes CSS (`ab-fold-section-schemas.js`, `ab-theme-css.js`, `ab-theme-computed.js`, `ab-component-reference.js`). Brought because it operationalises the section-schemas. Confirm its npm-script deps (`less`) travel with it |

---

## EXCLUDE — stays with the Adapt build fork

| Path | Why it stays behind |
|---|---|
| `src/components/*`, `src/extensions/*`, `src/core|menu|theme` | The Adapt plugin source — the fork builds + styles these |
| `adapt.json`, `.bowerrc`, `.browserslistrc`, `babel.config.js` | Adapt install / build config |
| `Gruntfile.js`, `grunt/`, `GRUNT.md` | Build harness |
| `patches/`, `scripts/apply-vendor-patches.js` | Vendor patch machinery |
| `package-scorm.js`, `tools/build-all-packages.js`, `tools/build-course-pack.js` | SCORM packaging (these *do* call `grunt build`) |
| `courses/<slug>/` | Produced course content (output, not engine) — though keep one as a golden fixture (see below) |
| `content/context-packs/baseline/`, `content/context-packs/psychology/` | Per-subject CXP *output* |
| `cm-design.css`, `cm-global.css`, `exports/`, `undlaf-intro_261012-235924/` | Generated CSS + export snapshots |
| `_workspace/`, `catalogue.json`, `inbox/`, `.github/`, `.mcp.json` | Project scaffolding / workspace tooling |
| `jest.config.js`, `cypress.config.js`, `test*.mjs`, `test.js`, `test/`, `test-fixtures/` (root) | Browser/a11y tests that target a running Adapt server |

---

## DECIDE — genuine judgement calls

1. **Theme / design-token system — RESOLVED (2026-10-19).** `design-kb/section-schemas/` +
   `tools/theme-mapping/` + `tools/adapt-ab/` come **into grow-context** as token/structure
   references (grow-context generates page structure from its own templates). The `adapt-ab-theme`
   extension under `src/` is NOT needed and stays with the Adapt fork.
   - *Still to confirm during extraction:* whether `tools/export-adapt-less-layers.js`,
     `tools/build-ab-token-*.js`, `tools/build-abbott-*.js` are wanted (they read `src/core/less` /
     `src/theme/.../less`, so they have a build-side dependency that section-schemas/theme-mapping do not).
   - *Verified:* `section-schemas` is referenced only by theme/styling code, never by `.claude/commands/*.md`
     or the core engine tools — so nothing in the gate grammar breaks by moving it.

2. **A golden course fixture.** The engine's tests + `verify-course.js` are more useful with one
   real course to validate against. *Recommendation:* keep a **copy** of
   `courses/understanding-learning-assessment-feedback-introductory/` as a read-only fixture in the
   engine repo (not as live content).

3. **Subject-benchmark grounding (Layer-3).** Already soft/stubbed — `tools/resolve-subject-benchmark.js`
   degrades to "gap" when no benchmark exists; PIPELINE.md says the QAA/vector-DB step is deferred.
   KEEP the resolver; no action needed, just noting it's a partial capability.

---

## Dependency surface (verified 2026-10-19 — informs grow-context's package.json)

The engine's JS is remarkably light. A scan of every `require()` across `tools/` (incl. `tools/lib/`,
`tools/adapt-ab/`, `tools/subject/`, `tools/pathways/`) and the root scripts shows **only Node
builtins** (`fs`, `path`, `child_process`, `os`, `node:test`, `node:assert`, `node:crypto`) **plus a
single external npm package: `fs-extra`** (used by `manifest-completeness.js`, `conformance-lint.js`,
`voice-lint.js`, `merge-context.js`).

- **JS runtime dep:** `fs-extra` only. Tests use Node's built-in test runner — no jest needed.
- **`less`:** the theme-css computation (`tools/adapt-ab/ab-theme-css.js`) shells out to `less` via
  `child_process`, so keep `less` as a dep *if* you want to run theme-css/theme-computed in grow-context.
- **Python:** `tools/validate-design-schemas.py` + the `*.py` resolvers use `jsonschema` (add a
  `requirements.txt`).

So grow-context's `package.json` dependencies are essentially `{ "fs-extra": "^8", "less": "^3.9" }`,
Node ≥18, plus a Python requirement for the schema validator. Clean.

## Fixups needed during extraction (don't carry bugs across)

- **Dangling `src/course`** — a plain-file symlink pointing at a missing
  `courses/_generated/…-psychology`. Irrelevant to the engine (it's a build artifact), but repoint
  it in the Adapt fork before any build.
- **Stale doc pointers** — command `.md` files cite three docs absent from disk
  (`docs/project/open-decisions.md`, `docs/design/gate-conversation-model-draft-v1.md`,
  `docs/authoring/gate-master-table-2026-10-07.md`). Either create stubs or scrub the references so
  they don't dangle in the standalone module.

---

## Packaging — DECIDED

**New standalone git repo**, package name **`grow-context`**. Cleanest isolation; becomes a real
package the Adapt fork and your other tools can depend on. Plan: fresh sibling dir, `git init`, copy
the KEEP set, add a root `package.json` (name `grow-context`) declaring the real deps (`ajv` for schema
validation, `less` for the theme tools), scrub the dangling doc pointers, and keep one course as a
read-only golden fixture.

Open sub-questions for the build step: the destination path for the new repo (proposed sibling
`../grow-context`), and whether to `git init` fresh (no history) or `git subtree`/filter to carry the
relevant history across.
