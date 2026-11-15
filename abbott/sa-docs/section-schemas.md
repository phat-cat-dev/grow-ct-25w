# Section schemas — the single source behind L4, L5 and the templates

Abbott, 11 Oct 2026. Specifies the *section schema* format and the tool that folds
it, for the theme surface defined in `ab-system-architecture.md` ("Section schemas
+ theme-profile templates") and `theming-layers-map.md` Part A. Companion to
`user-theme-template.md` (the worked **colour** section).

**Status: the schemas are AUTHORED, the fold tool is NOT yet built.** The six
generic section schemas and the Adapt adapter schema exist under
`design-kb/section-schemas/` (index at the end). They describe the TARGET
(`--ab-base-*`) token system and are the source the fold tool will consume after
the phased rename — not live LESS yet.

## Why schemas exist (the one principle)
A themeable **section** (`colour`, `typography`, `spacing`, `icons`, `motion`, …)
is defined **once**, in a schema, and that single definition **projects into
three places** so the section stays consistent everywhere:

```
            ┌─────────────────────────────────────────────┐
            │          section schema (ONE source)         │
            │       colour · typography · spacing · …       │
            └───────────────┬─────────────────────────────┘
          folds into …      │
   ┌──────────────────┬─────┴───────────┬───────────────────────┐
   ▼                  ▼                 ▼                        ▼
L4 defaults       L5 contract        L3 hooks              templates
--ab-base-pf-     --ab-theme-pf-     --ab-base-X:          --ab-theme-pf-
default-X: <val>  <name>-X           var(theme, default)   <name>-tmp-<t>-X
```

So you define `accent` once; the tool emits its L4 default value, its L5 contract
token, the L3 hook that composes them, and (if authorable) its field in the
templates. No hand-sync between layers.

## Two schema tiers (generic vs per-project adapter) — Abbott, 11 Oct 2026
Schemas split along the **portability line**, mirroring the six layers:

- **GENERIC section schemas — L3 → L6.** The portable, renderer-agnostic
  definitions: each section's L3 pivot tokens, their L4 defaults, L5 contract and
  L6 template fields. Written ONCE and reused across every project and every
  renderer, because everything from `--ab-base-*` down knows nothing about Adapt
  or JSX. This is what the rest of this doc specifies.
- **PER-PROJECT adapter schema — L1 → L2.** Renderer/project-specific: it names
  the renderer's own vocabulary (vanilla's `@item-color`, `@item-padding`,
  selectors like `.mcq-item__label`, breakpoints) and declares **how L2 plugs into
  L3** — i.e. the alias map `--ab-base-if-<renderer>-item-color: var(--ab-base-accent)`
  and which renderer vars/selectors the adapter owns. A new renderer (Adapt → JSX)
  is a new per-project adapter schema; the generic schemas do not change.

```
   PER-PROJECT adapter schema  ── L1 renderer vars/selectors + L2 adapter, "how 2 plugs into 3"
   ═══ portability line ═══
   GENERIC section schemas     ── L3 pivot → L4 defaults → L5 contract → L6 templates
```

The current `cm-vanilla-compat.less` (box-model/breakpoint vanilla `@vars`) is the
**proto per-project adapter schema**: it provides the renderer's L1 vars until the
phased rename builds the real L2 `--ab-base-if-<renderer>-*` adapter, into which it
folds. The two tiers meet only at the **alias join** (seam 1): the adapter schema
maps the renderer's names onto the generic L3 pivot, and nothing else crosses.

## Schema file format (JSON, house store style)
One file per section under `design-kb/section-schemas/`. A schema has **two
blocks** — `seeds` (the authorable dials) and `tokens` (the roles derived from
them) — matching the real system (`user-theme-template.md`: a user theme sets the hue,
the ladder derives the rest). Worked extract from `colour.json`:

```json
{
  "section": "colour",
  "schemaVersion": "0.1.0",
  "seeds": {
    "user-h":   { "kind": "number",  "default": 202,            "themeable": true,  "template": { "label": "Theme hue", "input": "number", "min": 0, "max": 360, "presets": ["basic","standard","full"] } },
    "accent-l":  { "kind": "percent", "default": "var(user-l)", "modes": { "dark": "62%" }, "themeable": true, "template": null },
    "l-surface": { "kind": "percent", "default": "100%",         "modes": { "dark": "14%" }, "themeable": true, "template": { "label": "Page background lightness", "input": "percent", "presets": ["full"] } }
  },
  "tokens": {
    "accent":       { "pivot": "--ab-base-accent",       "kind": "hsl",    "channels": ["user-h","user-s","accent-l"], "themeable": true,  "template": { "label": "Accent colour", "input": "color", "presets": ["basic","standard","full"] } },
    "accent-hover": { "pivot": "--ab-base-accent-hover", "kind": "derive", "expr": "hsl(user-h user-s calc(accent-l - 2%))", "themeable": false, "template": null },
    "surface":      { "pivot": "--ab-base-surface",      "kind": "hsl",    "channels": ["neutral-h","neutral-s","l-surface"], "themeable": true, "template": { "label": "Page background", "input": "color", "presets": ["standard","full"] } }
  }
}
```

**`seeds`** — the raw dials a user theme actually authors (`user-h`, the `l-*` stops,
font faces). Keys: `kind` (value type), `default`, optional `modes` (a second value
per mode — `dark` for the lightness stops; tokens re-derive from the active mode's
seeds), `themeable`, `template`.

**`tokens`** — the roles the fold tool emits, keyed by:
- **`pivot`** — the L3 token (`--ab-base-*`), the stable name everything reads.
- **`kind`** + its payload — how the value is produced: `hsl` (+`channels`: seed
  names), `derive` (+`expr`: a calc/hsl expression over seeds), `clamp` (+`power`:
  a fluid ladder step), `ref` (+`ref`: another token in this section), `ref-seed`
  (+`ref`: a seed), `literal` (+`value`), `symbol-list` (icon packs).
- **`themeable`** — `true` → gets an **L5 contract** entry + the L3 **hook**
  (`var(--ab-theme-pf-<name>-X, <L4 default>)`); `false` → derived-only, not
  user-overridable (e.g. hover is always a ramp off accent).
- **`template`** — `null`, or a field spec: `label`, `input` (`color`/`percent`/
  `number`/`length`/`font`/`select`/`time`/`iconset`), optional constraints, and
  **`presets`** (which extent presets expose it).

Mostly a user theme authors **seeds** (the hue, the faces), not individual derived
tokens — so a `template` sits on the seed (e.g. `user-h`) more often than the
token (`accent`), though a token may also be directly authorable (`surface`).

## The three projections (what the folding tool emits)
For each section schema the tool generates:

1. **L4 default** — for every token: `--ab-base-pf-default-<token>: <value from "default">;`
2. **L5 contract + L3 hook** — for every `themeable` token:
   - contract token declared (empty): `--ab-theme-pf-<name>-<token>` (per theme profile)
   - the pivot rewired as a hook:
     `--ab-base-<token>: var(--ab-theme-pf-<name>-<token>, var(--ab-base-pf-default-<token>));`
3. **Template fields** — for every token whose `template` is set, a field in each
   template whose name is in the token's `presets` (basic ⊂ standard ⊂ full), rendered
   with its `label`/`input`. A **bespoke** template is an explicit list of sections
   (and optionally tokens) to include — the pick-n-mix.

A completed template writes the L6 user profile `--<xx>-<stub>-<token>` and binds
it into the L5 contract (`--ab-theme-pf-<name>-<token>: var(--<xx>-<stub>-<token>)`).

## Extent presets + pick-n-mix
- **basic / standard / full** = cumulative extent presets; a token's `presets` key
  lists which it appears in. basic = the few essentials (accent, page bg, heading
  font); full = everything themeable.
- **bespoke** = a template manifest naming the sections (and optional token subset)
  to include, e.g. `{ "template": "cardiffmet-theme", "sections": ["colour", "icons"] }`
  — colour + icons authored, typography/spacing/motion fall through to L4 defaults.

## The folding tool (BUILT — emits to exports/ab-fold/)
`tools/adapt-ab/ab-fold-section-schemas.js` reads `design-kb/section-schemas/*.json` and emits:
- `exports/ab-fold/ab-base-pf-default.less` — L4 defaults (seeds + token values) +
  the dark-mode seed-override block;
- `exports/ab-fold/ab-base-pivot.less` — the L3 pivot hooks + the L5 contract list;
- `exports/ab-fold/ab-templates.json` — the authorable fields per extent preset.

It is the single generator that keeps the layers in sync; edit a section schema,
re-fold — never hand-edit the generated files. Verified: the generated L4+L3 LESS
compiles clean, HSL/derive values carry `~"…"` escapes, and the fluid clamps match
cm-type.less exactly. **Not yet wired into the live build** — output lands in
`exports/` (reviewable) because the live `--ab-*` LESS does not exist until the
phased rename; at rename Phase 3 these generated files become the real L4/L3 LESS.
The template-RENDERING surface (how a user fills the fields) is still open (below).

## Resolved while authoring (11 Oct 2026) — correctable
1. **Location / format** — `design-kb/section-schemas/*.json` (generic) +
   `design-kb/section-schemas/adapters/*.json` (per-project), JSON in the house
   store style. ✅
2. **`kind` set** — `hsl`, `derive`, `clamp`, `ref`, `ref-seed`, `literal`,
   `symbol-list` (+ seed kinds `number`/`percent`/`length`/`time`/`fontstack`/
   `ref-seed`/`symbol-list`). ✅ Extend if a section needs more.
3. **`input` vocabulary** — `color`, `percent`, `number`, `length`, `font`,
   `select`, `time`, `iconset`. ✅ Constraints per input still loose (min/max shown
   for number/percent).

## Still open (Abbott's call)
4. **Where the templates render** — a form UI, a generated LESS stub the user edits,
   or a JSON the user fills? Decides how `template`/`input` are consumed. The
   `iconset` input in particular is undefined.
5. **Build order vs the phased rename** — schemas describe the TARGET `--ab-base-*`
   LESS, which the fold tool emits; so the fold tool + templates are built AFTER the
   phased restructure (rename Phase 4), not before. The schemas themselves (data)
   are authored now. Confirm the surface sits at the end of the sequence.
6. **Spacing fluid scale + border fixed-vs-fluid** — `spacing.json` marks the fluid
   `--ab-base-space-*` ladder `toBuild`; `box-model.json` leaves border fixed-vs-fluid
   open (value 0.2rem settled). Both wait on the fluid engine.

## Authored schemas (index)
Generic (L3→L6, renderer-agnostic), under `design-kb/section-schemas/`:
- `colour.json` — seeds (user/neutral hue+sat, L-stops with light/dark modes,
  semantic h/s/l) + tokens (accent chain, surface/ink/hairline spine, semantic,
  h1–h6 colour).
- `typography.json` — seeds (ratio, base size, vw range, font faces + roles +
  weights) + tokens (the clamp type steps, power −1…6) + the clamp rule.
- `spacing.json` — layout tokens (page-max, gutter, pad-y, measure-max, item
  pad/gap); fluid `--ab-base-space-*` scale marked `toBuild`.
- `box-model.json` — radius (0.32rem) + border-width (0.2rem, resolved).
- `icons.json` — modular Google-Symbol packs (academic-practice, cite-source),
  self-hosted at build.
- `motion.json` — durations + easings + the reduced-motion guard.

Per-project adapter (L1→L2, renderer-specific), under `.../adapters/`:
- `adapt.json` — the Adapt renderer: the vanilla `@vars` the adapter provides, the
  seam-1 alias map (vanilla literal → L3 pivot), the sweep selectors, and the dead
  vanilla vars the migration has absorbed.

The **fold tool** (`tools/adapt-ab/ab-fold-section-schemas.js`) is built and emits to
`exports/ab-fold/`; what remains is wiring its output into the live build (rename
Phase 3) and the template-rendering surface (open item 4).

## Round-trip proof (L4 → L5 → L6), verified 11 Oct 2026
`tools/adapt-ab/ab-resolve-tokens.js` resolves the `--ab-base-*` pivot through the fold
output (optionally with an L6 user theme profile), doing the var() cascade lessc can't.
A worked L6 example, `exports/ab-fold/example-cm-corporate.l6.less` (the CM
"corporate" user theme setting ONLY `accent`), resolves as:

| token | no user theme (L4 default) | CM corporate |
|---|---|---|
| `--ab-base-accent` | `hsl(202 72% 14%)` | **`#7a1540`** (override) |
| `--ab-base-surface` | `hsl(202 0% 100%)` | `hsl(202 0% 100%)` (inherited) |
| `--ab-base-h1-color` | `hsl(202 72% 14%)` | **`#7a1540`** (follows accent — it is `ref: accent`) |

So a user theme overrides exactly what it sets, inherits the rest from the L4 default,
and `ref` tokens track the override. Reproduce with
`node tools/adapt-ab/ab-resolve-tokens.js exports/ab-fold/example-cm-corporate.l6.less`.

**Seed-level L5 hooks (built, verified 11 Oct 2026):** themeable role TOKENS carry
L5 hooks, and so now do themeable SEEDS — so a user theme can re-hue the whole
palette by setting ONE seed hook (`--ab-theme-pf-default-user-h`) rather than
overriding each final role. The fold tool emits, for a themeable seed,
`--ab-base-pf-default-user-h: var(--ab-theme-pf-default-user-h, 202)`. Proven with
a profile that sets only `--ab-theme-pf-default-user-h: 150`: every accent token
(`accent`, `-hover`, `-active`, `-deep`, `-tint`, `-line`, `-ring`) swings to the
new hue, while neutral-driven tokens (`on-accent`) stay put. A themeable seed that
ALSO has a dark value (`l-surface`, `accent-l`) exposes a SEPARATE dark hook
`--ab-theme-pf-default-<name>-dark`, so a theme sets its light and dark values
independently; each falls back to the base default for its own mode (verified:
`--ab-theme-pf-default-l-surface-dark: 8%` sets the dark page background without
touching the light one).
