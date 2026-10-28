# adapt2 engine — verbatim reference snapshot

**What this is.** A frozen, read-only copy of the *context-consultation engine* (the "first
phase") from the adapt2 repo, lifted here to refactor `grow-context` from. It is reference
material, not the live tool — the real GROW-targeted tool is built in `../../tool/`.

- **Source:** `adapt3/wkspc2614-adapt3` @ commit `7cc387c` (branch `adab-styles-mapper`), 2026-10-19.
- **Not a running package.** Paths mirror the source repo so it reads like a mini-repo. Don't wire
  anything to it; copy/adapt pieces out of it into `tool/`.
- **Specs that go with it:** [`../docs/01-page-structure-and-components-spec.md`](../docs/01-page-structure-and-components-spec.md)
  (page structure, fields, components) and [`../docs/02-context-generator-keep-list.md`](../docs/02-context-generator-keep-list.md)
  (what was kept/dropped and why).

## The engine in one paragraph

Six gated phases — **ONB → CXS → CRS → LES → WRA → CXP**, 24 gates (`design-kb/design-kb.gates.json`).
Decisions are recorded in an append-only manifest; a scaffold step emits the Adapt JSON; `/land` fills
deferred slots; `merge-context.js` slots subject packs in. It reasons purely over JSON stores — no
build, grunt or SCORM dependency. The valuable, portable part is the **decision logic**: shape → activity
pattern → component routing, tier/subject grounding, and the `agentAuthor` briefs that map the AI to the
right context.

## What's here

| Dir | What |
|---|---|
| `design-kb/*.json` | The 8 stores the grammar reasons from: gates, skeletons, palette, activity-patterns, content-shapes, content-conventions, tier-bands, pathways |
| `schemas/` | JSON schemas for the stores + the manifest (`course-design.schema.json`) |
| `.claude/commands/` | The 10 skills (gate, land, new-course, scaffold, new-context, cxp-open, ledger, phase-draft, reopen, publish) + `agents/reviewer.md` |
| `tools/` | Engine scripts: `generate-course-shell.js` (the emitter), `gate-order.js`, `phase-confirm.js`, `resolve-agent-author.js`, `verify-course.js`, `conformance-lint.js`, `manifest-completeness.js`, `validate-design-schemas.py`, resolvers + `lib/`, `subject/`, `pathways/`, `doc-templates/`, `test/` |
| `reference/` | `excelling-at-university.md` (source book) + voice spec + linguistic audit |
| `source-kb/` | The chunked/tagged book map (single source of truth for chunk text) |
| `catalogue/` | 13-pathway registry + context correspondence data (the heavy grounding corpora) |
| `integrations/mapper/` | Subject ↔ HESA ↔ pathway profiles |
| `docs/` | PIPELINE, ARCHITECTURE, RUNBOOK + `authoring/`, `curriculum/`, `contexts/` |
| `example-adapt2-output/` | The one real course the engine emitted — concrete example of the current (adapt2-shaped) output |
| `reference-structural-spine/` | `adapt-template-classes.{json,less}` + `layer.md` — the structural selector "spine" (the only theme-mapping artefact kept; structure, not look) |
| `merge-context.js`, `voice-lint.js` | Root engine scripts |

## What was deliberately left out

- **Theme / token system** — `design-kb/section-schemas/`, `tools/adapt-ab/`, `tools/theme-mapping/`
  (except the spine above), the `adapt-ab-theme` extension. grow-ct owns *structure + function, not
  look*; the look is the theme-builder's job and GROW already has its own token engine. The structural
  spine is kept as a read-only reference only.
- **Build / SCORM harness** — `Gruntfile`, `grunt/`, `src/`, `adapt.json`, `patches/`,
  `package-scorm.js`, the `build-*`/`course-css-export`/`check-build-target` tools.
- **Course content** — only one course is kept, under `example-adapt2-output/`, as an example of the
  emitter's output (not as live content).

## The refactor's core job: adapt2 → GROW content model

The decision logic ports as-is. The **emitter and the field/role vocabulary do not** — adapt2 and
GROW describe structure differently. This is the main design work for the real `grow-context` tool.

**adapt2 (what the snapshot emits)**
- Hierarchy: `course → contentObject(page) → article → block → component` (4 levels).
- Role is carried on blocks as **`_skeletonKey`** (e.g. `concept-definition`, `worked-example`, `check`,
  `reflective-prompt`); phase is a CSS class on articles (`article--lesson-open/-concept/-formative/
  -reflection/-close`); provenance is a class on components (`slot__<pageKey>__<skeletonKey>`); SCORM
  stability via `_trackingId`.

**GROW (what the tool must emit — see `grow/schema/grow-structure.schema.json` in the repo root)**
- Depth model: `lesson → phase → section → learning-step → item` (5 levels), stamped as a universal
  **`_grow._frontmatter`** object at page/article/block/component, with `_role` (BEM modifier) and
  `_type` (semantic function), plus `eyebrow/body/_outcomes/_fields/_objectives`, surfaced as
  `data-grow-*` / `data-fm-*`.

**Approximate correspondence (to be nailed down — the two depths don't line up 1:1):**

| adapt2 | GROW `_role` | note |
|---|---|---|
| page (lesson) | `lesson` | lesson pages |
| article (phase class) | `phase` | `_type` = the phase (open/concept/formative/reflection/close) |
| block (`_skeletonKey`) | `section` *or* `learning-step` | GROW splits into two levels adapt2 doesn't have — the main open question |
| component (`slot__…`) | `item` | `_type` = the semantic role (ex-`_skeletonKey`) |

So the adapt2 **`_skeletonKey` taxonomy becomes GROW `_type` values**, and the extra GROW levels
(`section`, `learning-step`) need a deliberate mapping decision. `generate-course-shell.js` is the file
to re-aim: today it writes adapt2 JSON; the GROW version writes `_grow`-shaped JSON.

## If you run any engine tool on Windows

Two env workarounds carry over (recorded during the adapt2 build): `python3` may be the dead MS-Store
alias (use real `python`/a `python3.exe` shim for `validate-design-schemas.py`), and Node 18 needs
`NODE_OPTIONS=--experimental-global-webcrypto`. The validator passes under real Python.

## Suggested next steps

1. Decide the adapt2→GROW level mapping (the table above) against `grow/schema/grow-structure.schema.json`.
2. Build `../../tool/` as the GROW-targeted engine: reuse the stores + routing + resolvers verbatim;
   rewrite only the emitter and the skeleton/field vocabulary to `_grow`.
3. Reconcile with the existing `../../../context-packs/` tool (the CXP/subject-recast concept already
   has a home there — don't duplicate it).
