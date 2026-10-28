# adapt-ab-theme

A portable, layered CSS **token cascade**. One anchor colour and a few seeds
drive the whole visual system — palette, type scale, spacing, breakpoint
clamps, container-query edges and icon rosters — all resolved at runtime in the
browser. It is plain CSS: no LESS, no build step, no framework. Drop it in and
reference the `--ab-base-*` tokens from your own component styles.

This package collates only the **token layers** of the wider AB theming work.
It deliberately does **not** include the Adapt components, the vanilla-renderer
selector sweep, or the icon font files — those are renderer-specific. What ships
here plugs straight into any project that can load a stylesheet.

## Use

```html
<link rel="stylesheet" href="adapt-ab-theme/ab-theme.css">
```

Then, in your own CSS:

```css
.card        { background: var(--ab-base-surface); color: var(--ab-base-ink); }
.card__title { color: var(--ab-base-h1-color); font-size: var(--ab-base-h1-font-size); }
.btn         { background: var(--ab-base-accent); color: var(--ab-base-on-accent); }
.btn:hover   { background: var(--ab-base-accent-hover); }
.stack > * + * { margin-block-start: var(--ab-base-space-100); }
```

`ab-theme.css` ships the **pink** user pack (anchor `hsl(329 78% 31%)`, the
nominal brand `#8e1152`). Dark mode is built in — set `data-theme="dark"` or
class `ab-dark` on `<html>` and every token re-derives.

## The six layers

Loaded by `ab-theme.css` in this order (resolution is lazy, so the order is for
reading; no two layers set the same custom property):

| Layer | Namespace | File | Role |
|------|-----------|------|------|
| **L2** adapter | `--ab-base-if-adapt-*` | `layers/L2-adapter.css` | Renderer role seam. A renderer's component CSS reads these; rewire this one file to port to a different renderer. |
| **L3** pivot | `--ab-base-*` | `layers/L3-pivot.css` | The generic surface everything reads. Themeable pivots read L5-else-L4; fixed pivots read L4. |
| **L4** defaults | `--ab-base-pf-default-*` | `layers/L4-defaults.css` | Shipped defaults. Seeds first, derived tokens after. Each is overridable by its L5 twin. |
| **L5** template | `--ab-theme-pf-default-*` | `layers/L5-template.css` | The authorable theme contract — every token a theme may retarget, and nothing else. Ships empty (commented), so L4 stands. |
| **L6** user pack | `--ab-thm-*` | `layers/L6-thm-pink.css` | Brand values in their own published namespace, bound into L5. Swap this file to recolour everything. |

(L1 is the renderer/browser itself — out of scope for a stylesheet.)

### How an override flows

Every L4 default is written `var(--ab-theme-pf-default-X, <default>)`, and the
themeable L3 pivots are written `var(--ab-theme-pf-default-X, var(--ab-base-pf-default-X))`.
So defining `--ab-theme-pf-default-X` anywhere (an L5 edit, or an L6 pack
binding into it) retargets X without touching the default. The L6 pink pack
sets three colour seeds; the accent, every accent state, the heading colours
and (if you tint the spine) the greys all re-derive from them.

### Theming

Two ways:

1. **Edit L5 directly** — uncomment and change lines in `layers/L5-template.css`.
2. **Swap the L6 pack** — copy `layers/L6-thm-pink.css`, change the `--ab-thm-*`
   seed values (keep them in your own `--ab-thm-<brand>-*` namespace), and point
   the last `@import` in `ab-theme.css` at it. A ready-made **blue** pack ships
   alongside pink (`layers/L6-thm-blue.css`, the stock dark-blue anchor
   `hsl(202 72% 14%)` ≈ `#0a2a3d`) — point the import at it, or drop the L6
   import entirely to fall through to the identical L4 default. A third,
   **cmab-dual** pack ships with its own entry point, `cmab-theme-pack.css`
   (`layers/L6-thm-cmab-dual.css`): the same dark-blue anchor plus a dark-grey
   (`#6d6d6d`) pinned as the `h2` tier — two seeds, not one.

Retarget **seeds**, not outputs: set `--ab-theme-pf-default-user-h/-s/-l` (the
colour anchor) and `--ab-theme-pf-default-type-ratio`, not the individual
`accent`/`h2-font-size` outputs they derive. Buttons follow the same rule —
seven knobs (`-btn-radius`, `-btn-padding-y/-x`, `-btn-border-width`,
`-btn-focus-shadow-rgb`, `-btn-active-shade`, `-btn-hover-surface`) are
themeable via L5; sizes and semantic variants are derived outputs, not part
of the contract.

### Namespace grammar

Template layers use the long form
`--<xx>-theme-pf-<theme>-tmp-<subtheme>-<n>-<formula>-<token>`; on publish to a
user scheme it shortens to `--<xx>-thm-<theme>-<subtheme>-<n>-<formula>-<token>`
(drop `-pf-` and `-tmp-`). The pink pack is `xx=ab`, `theme=pink`,
`subtheme=dark-neutral`, single anchor `n=1`; the anchor seed carries no
colour-theory formula, so `<formula>` is omitted for it (structural and type
tokens omit `<n>-<formula>` the same way).

## Accent spectrum

Beyond the single accent, the module ships a full **named-colour spectrum**:
12 families (`red orange amber lime green emerald teal azure blue indigo violet
rose`) × `dark`/`light` × 9 bands (`10`–`90`), reachable directly:

```css
.tag      { background: var(--ab-base-accent-azure-light-10); color: var(--ab-base-accent-azure-dark-80); }
.callout  { border-inline-start: 3px solid var(--ab-base-accent-amber-dark-50); }
```

Band labels are fixed and identical across families (the A-v2 ladder); a band's
true mix depth = `label + shade-offset`, where the offset is derived from the
pack anchor's lightness, so the labels stay clean while values ride true to the
chosen colour. The whole spectrum is **runtime-reactive**: it derives from the
same anchor as the rest of the cascade (shared chroma = `accent-s`, offset via
CSS `round()`), so swapping the pack re-derives all of it — no regeneration.

**Colour-theory sets.** Seven rotations ship alongside the plain (`mono`) set —
`complementary split-a split-b triad-a triad-b analogous-lo analogous-hi` — each
a full 12-family ladder with the family hues rotated by the colour-theory angle:

```css
.chip { background: var(--ab-base-complementary-accent-blue-dark-40); }
```

A rotation rotates every family's hue, so under a rotation a **family name
denotes the slot, not the rendered hue** — `complementary-accent-blue-*` is
blue + 180° (an amber). Seven `--ab-base-companion-*` single colours (the §2.5
companions off the primary) ship too.

Generated from `design-kb/section-schemas/accent-spectrum.json` by
`tools/adapt-ab/ab-gen-accent-spectrum.js`. Requires `color-mix()` and CSS
`round()` (modern browsers).

## Semantic cue sets

Three HSL-derived cue categories for callouts, feedback and notices:

```css
.callout--positive { background: var(--ab-base-positive-bg); border-color: var(--ab-base-positive-border); color: var(--ab-base-positive-ink); }
.callout--positive .icon::before { content: var(--ab-base-positive-icon); }     /* "check_circle" */
```

- `positive` (green, hue 145) — sub-icons `correct`, `advise`
- `negative` (red, hue 5) — sub-icons `incorrect`, `warn`
- `neutral-cue` (amber, hue 38) — sub-icon `observe`

Each exposes `-bg` (pale wash), `-border`, `-ink` (AA-dark text on the wash),
`-icon-colour` and `-icon` (a ligature); each sub-category adds its own
`-<sub>-icon`. Category hues are fixed (semantic meaning should not drift with
the brand), but the shared `semantic-s`/`semantic-l` dials and the hues are
themeable via L5. The amber category is named **`neutral-cue`**, not `neutral`,
so it does not collide with the neutral *spine* (`--ab-base-...-neutral-h/-s`).
Schema: `design-kb/section-schemas/semantics.json` (§2.6).

## Breakpoints and `@media`

The breakpoint values (`--ab-base-bp-*`) and the fluid clamps ship as tokens and
resolve at runtime. The `@media` **rules** that would switch layout at those
breakpoints cannot be expressed as custom properties (a media query needs a
compile-time length), so they are **not** part of this token array — they belong
in a renderer's own layout stylesheet, which can read the `--ab-base-bp-*`
values for its query edges. Within a breakpoint, the fluid scales already adapt
continuously, so most components need no media query at all. Container queries
are the same: the band edges (`--ab-base-cq-medium/-wide`) ship as tokens; the
`@container` rules that consume them live in component CSS.

## Provenance

The L3 and L4 files are the compiled fold of the repository's section schemas
(`tools/adapt-ab/ab-fold-section-schemas.js`), lifted to standalone CSS. Two
edits were made against the raw fold, both to make the package self-contained:

- `--ab-base-pf-default-gutter` is `var(--ab-theme-pf-default-gutter, 1rem)`
  here; the live extension points it at a renderer layout variable plus an
  `@media` override (out of scope for a token array, per above).
- `--ab-base-pf-default-font-heading` / `-font-body` reference the real
  `--ab-base-pf-default-font-display` / `-font-sans` tokens; the raw fold
  emitted bare `font-display` / `font-sans` keywords, which are not valid
  font-family values.

Verified by resolving the whole cascade in Chromium: the pink anchor computes to
`rgb(141 17 81)` at `--ab-base-accent` and through the L2 seam at
`--ab-base-if-adapt-item-color`, with surfaces, ink, accent-state offsets, the
fluid spacing/type clamps and the icon ligatures all resolving.
