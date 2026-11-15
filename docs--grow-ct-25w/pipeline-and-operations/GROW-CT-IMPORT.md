# GROW-CT-IMPORT — bringing the grow-ct styling / components into this build

**Status (updated 2026-10-21): IN PROGRESS on branch `adopt-grow-theme` — `grunt build` is green.** **Decision: Option A** — adopt the `_grow` theme as grow-course's active theme; `adapt-ab-theme` retired as active styling, wanted bits hand-ported into `_grow`. The 32-component / 23-extension library is otherwise unaffected.

### Progress
- [x] `_grow` theme tracked + active, vanilla excluded; **build compiles clean** (`0b4c894`, `2d657c6`).
- [x] Build/python portability fixed (`25286d5`, `b84b1f8`): real python resolved via `where`, preferring one that has `jsonschema`. **Build env: Node 18 needs `--experimental-global-webcrypto`; or use Node 20+.** Command: `NODE_OPTIONS=--experimental-global-webcrypto npx grunt build`.
- [x] Imported `adapt-grow-pagenav` — top nav prev/next (`6076f87`). **Dropped `adapt-grow-layer`** (`77d108b`): it only hosts the runtime theme-manager/typography studio, which we don't ship (chosen values are baked into `_grow-tokens.less`).
- [x] Adopted grow-ct's `confidence` (incl. Chart.js before/after) + `hotgraphic` (`a66416a`).
- [x] Loaded **Material Symbols Outlined** (`afb061b`) — nav home/prev/next glyphs + menu-card marks render.
- [x] **Verified in-browser** (Playwright): content-page top nav = centred home + prev/next icon-buttons; grow theme + confidence render. (Menu nav is intentionally minimal — pagenav hides there.)
- [ ] Salvage wanted ab-theme bits into `_grow` (cards/callouts/buttons/type, CM colour packs, light/dark theme-switcher) — iterative, visual.
- [ ] Minor cleanup: `grow-chrome.less` still reserves `--grow-dock-h` bottom space for the removed dock — trim when convenient.
- [ ] `src/course` is a per-machine junction (relink per environment; not committed).

**Source:** the sibling repo `adapt-forks/grow-ct` (a containerised GROW
theme/content project). We decided to build in **grow-course**, so grow-ct's
distinctive work should be imported here rather than maintained in two places.
grow-course already has the larger library (32 components, 23 extensions);
grow-ct's value is its **theme**, **two extensions**, and **recent fixes**.

## What's worth importing
1. **The `_grow` theme** (`grow-ct/grow-ct/`, theme `grow-base`, `targetAttribute _grow`) — a *full replacement* theme forked from vanilla, driven by the `@grow-*/--grow-*` token system (`less/_defaults/_grow-tokens.less` is the single source of truth), with its own Backbone view overrides, `templates/`, and a theme-pack selector under `themes/`. **This is the look you built and want.**
2. **Two new extensions** — `adapt-grow-layer` (`_growLayer`) and `adapt-grow-pagenav` (`_growPageNav`). Not in grow-course — clean adds.
3. **Reconcile two drifted components** — `adapt-abbott-confidence` (now with before/after Chart.js + a vendored `js/` dir) and `adapt-ab-hotgraphic` differ from grow-course's copies. The other 5 shared components are byte-identical.
4. **Recent grow-ct commits** `7f9e26f…5594e60` — frontmatter-leak fix, summative fix, confidence chart, pagenav, nav / page-layout / stage-card styling, mcq attempts-text fix.

## The one real decision: theming strategy
Adapt allows **one active theme**, and the two repos are incompatible:
- **grow-course now:** vanilla (active) + `adapt-ab-theme` *extension* + a `--ab-*` token pipeline from `cm-global.css`, driven by `_htmlClasses`.
- **grow-ct:** the `_grow` *full theme* replaces vanilla + a `@grow-*/--grow-*` token system.

You cannot run both.

- **Option A — CHOSEN: adopt `_grow` as grow-course's theme.** Makes grow-course look like grow-ct (the goal / "latest version"). `_grow` replaces vanilla as the active theme; `adapt-ab-theme` is retired as active styling, its wanted pieces hand-ported into `_grow` (see "Salvaging from the old ab-theme"). The component/extension library is untouched — only the theme changes. A migration, done on a branch with build tests.
- **Option B:** keep vanilla + `adapt-ab-theme`, import only the 2 extensions. Lower churn, older look. *Not chosen.*

## Salvaging from the old ab-theme
`_grow` becomes the one active theme, so `adapt-ab-theme` can't stay active alongside it — but port its wanted work into `_grow`'s LESS, translating `--ab-*`/CM tokens into the `@grow-*`/`--grow-*` system:
- **Salvage candidates:** specific component styling (cards, callouts, buttons, type scale), the CM brand colour packs (`cm-global.css` / `cm-theme-*`), the light/dark + profile **theme-switcher** (`ab-theme-switcher.js`), and any `ab-*` layer `_grow` has no equivalent for.
- **Skip:** anything `_grow` already covers via its token layer / decoration layers (`themes/adapt-abbott/`).
- **Method:** diff each ab-theme layer against its `_grow` equivalent; bring across only what's missing or better, as a `_grow` LESS addition; visual-review each.

## Mechanical recipe for Option A (adapted from grow-ct `docker/entrypoint.sh`)
1. Copy `grow-ct/grow-ct` → `src/theme/grow-ct`.
2. **LESS wiring:** move `src/theme/grow-ct/themes` out to a sibling `src/theme/grow-ct-theme-packs` (so Adapt's recursive LESS scan compiles only the *selected* pack), and rewrite the two `@import` paths — in `_grow-tokens.less` and in `current-theme.less`.
3. Generate `src/theme/grow-ct/less/zz-adapt-abbott.less` importing `themes/adapt-abbott/less/*.less` (the `zz-` prefix sorts the decoration layers last).
4. **Config:** set `_theme: grow-ct`, add every other theme to `build.excludes`, and reconcile `_htmlClasses` (the `ab-*`/`cm-*` classes mean nothing to `_grow`).
5. Copy the 2 grow extensions into `src/extensions/`.
6. **Reconcile** `adapt-abbott-confidence` + `adapt-ab-hotgraphic` deliberately — do **not** blind-overwrite (same `1.0.0`, different content).
7. `npm run adapt-install` (reapply `patches/`) → `npx grunt build` → preview → SCORM.

## Conflict map (from the mapping pass)
| grow-ct piece | type / target | in grow-course? | action |
|---|---|---|---|
| `grow-ct` theme | theme `grow-base` / `_grow` | no (`_grow` absent) | Option A/B decision |
| `adapt-grow-layer` | ext `_growLayer` | no | clean add |
| `adapt-grow-pagenav` | ext `_growPageNav` | no | clean add |
| `adapt-abbott-confidence` | comp `_confidence` | yes | **merge** (drift: +Chart.js, vendored js) |
| `adapt-ab-hotgraphic` | comp `_abHotgraphic` | yes | **merge** (drift: `ab-hotgraphic.less`) |
| checklist, flipcard, opentext, references, sortable | comps | yes | identical — no action |

Menu: grow-ct ships none — `src/menu/adapt-contrib-boxMenu` untouched.
