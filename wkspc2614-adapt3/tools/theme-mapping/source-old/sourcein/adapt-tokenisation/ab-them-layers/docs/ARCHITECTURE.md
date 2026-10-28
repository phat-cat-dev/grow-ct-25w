# adapt-ab-theme — architecture

The module is a **token cascade**: one anchor colour plus a handful of seeds, and
every visual value (palette, type scale, spacing, breakpoint clamps,
container-query edges, icon rosters) derives from them at runtime. This doc is
the mental model. For install and usage see `../README.md`; for the machine
description see `../package.json` (the `ab` block).

This is a distilled, module-local account. The authoritative, fuller treatment
lives in the parent repository and is cited inline below — nothing here claims to
replace it.

## The six layers

```
L1  renderer / browser          literals in the renderer's own vocabulary   (out of scope)
L2  adapter    --ab-base-if-adapt-*    renderer role seam         layers/L2-adapter.css
───────────────────────────── portability line (everything below is framework-agnostic)
L3  pivot      --ab-base-*             the generic read surface   layers/L3-pivot.css
L4  defaults   --ab-base-pf-default-*  shipped default values     layers/L4-defaults.css
L5  template   --ab-theme-pf-default-* the authorable contract    layers/L5-template.css
L6  user pack  --ab-thm-*              brand values, bound into L5 layers/L6-thm-pink.css
```

- **L2 adapter** is the only layer that speaks a specific renderer's vocabulary.
  It aliases each renderer role (`item-color`, `greyDark`, validation, …) to an
  L3 pivot. Porting to another renderer means rewriting only this file. The
  renderer-specific *selector sweep* that paints the renderer's component classes
  with these tokens is **not** in this module — it stays in the host extension.
- **L3 pivot** is the stable public surface. Component CSS references `--ab-base-*`
  and nothing else. Themeable pivots read L5-else-L4; fixed pivots read L4.
- **L4 defaults** hold the shipped values: HSL seeds + the tokens derived from
  them. The package renders on L4 alone, with no theme present.
- **L5 template** is pure interface — the complete set of tokens a theme may
  retarget, and nothing else. It ships empty (every line commented), so L4 stands
  until something populates it.
- **L6 user pack** keeps the brand's values in its own published `--ab-thm-*`
  namespace and binds them into L5. Swap the pack, recolour everything; nothing
  above L5 knows the pack's name.

(Source: `docs/authoring/theming-layers-map.md` Part A, the canonical cascade.
That doc's Part A was "not yet in code" when written on 11 Oct 2026; this branch
has since realised the `--ab-*` cascade it specifies.)

## How an override flows (the accent, end to end)

```
L6  --ab-thm-pink-dark-neutral-1-h: 329;  -s: 78%;  -l: 31%;     the brand value
    --ab-theme-pf-default-user-h: var(--ab-thm-pink-dark-neutral-1-h);   bind → L5
L5  --ab-theme-pf-default-user-h   (set by L6; otherwise unset)
L4  --ab-base-pf-default-user-h: var(--ab-theme-pf-default-user-h, 202);   L5-else-default
    --ab-base-pf-default-accent: hsl(var(--…-user-h) var(--…-user-s) var(--…-accent-l));
L3  --ab-base-accent: var(--ab-theme-pf-default-accent, var(--ab-base-pf-default-accent));
L2  --ab-base-if-adapt-item-color: var(--ab-base-accent);
```

Read it bottom-up: L6 sets a seed → binds it into L5's contract → L4's default
resolves to it → L3's pivot exposes it → L2 hands it to the renderer. With no
pack, L5 is unset, L4's literal default stands, and the module renders unthemed.

Every L4 default is written `var(--ab-theme-pf-default-X, <default>)` and every
themeable L3 pivot `var(--ab-theme-pf-default-X, var(--ab-base-pf-default-X))`, so
defining `--ab-theme-pf-default-X` anywhere wins — composed at the hook, never by
writing into the base namespace. (Source: `docs/authoring/theme-formula-map.md`;
the hook-not-overwrite decision is `theming-layers-map.md` A5.)

## Seeds vs derived — retarget seeds, not outputs

A theme sets a few **seeds**; the **formulas** proliferate everything else:

- **Colour.** One HSL anchor (`user-h/-s/-l`) → accent + its hover/active/deep/
  tint/line/ring via `calc()` lightness offsets; a neutral spine (`neutral-h/-s`
  + lightness stops) → surfaces, ink, hairline. Dark mode flips the lightness
  stops only; every colour re-derives.
- **Type.** A base size + a ratio → a fluid `clamp()` ladder (step-small … h1).
- **Spacing.** A fluid `clamp()` ladder keyed to the viewport range.
- **Breakpoints / container queries.** Named edges ship as tokens (see the
  caveat below).

So `--ab-theme-pf-default-user-h` and `--ab-theme-pf-default-type-ratio` are the
dials; `accent-hover` and `h2-font-size` are outputs — do not set them directly.
(Source: `docs/authoring/theme-formula-map.md`, the "few seeds, formulas
proliferate the rest" rule; `docs/authoring/user-theme-template.md` for the
seed/colour model.)

## Namespace grammar

Template layers use the long form
`--<xx>-theme-pf-<theme>-tmp-<subtheme>-<n>-<formula>-<token>`. On publish to a
user scheme it shortens to `--<xx>-thm-<theme>-<subtheme>-<n>-<formula>-<token>`
(drop `-pf-` and `-tmp-`). The `-if-` infix marks the renderer *interface* (L2);
`-pf-` marks a *profile* (L4/L5); bare `--ab-base-*` is the L3 pivot. The pink
pack is `xx=ab`, `theme=pink`, `subtheme=dark-neutral`, single anchor `n=1`; the
anchor seed carries no colour-theory formula, so `<formula>` is omitted for it
(structural and type tokens omit `<n>-<formula>` the same way). (Source:
`theme-formula-map.md` §4; infixes in `theming-layers-map.md` A2.)

## Where the token values come from

L3 and L4 are the compiled **fold** of the repository's section schemas —
`accent-spectrum`, `box-model`, `breakpoints`, `colour`, `container-queries`,
`icons`, `motion`, `semantics`, `spacing`, `typography` under
`design-kb/section-schemas/` — via `tools/adapt-ab/ab-fold-section-schemas.js`,
lifted here to standalone CSS. Two edits against the raw fold make the module
self-contained (both in `../README.md`, Provenance): `--…-gutter` and the
`font-heading`/`font-body` references.

## Breakpoints and `@media` — the one portability caveat

Breakpoint values and the fluid clamps ship as tokens and resolve at runtime. The
`@media` and `@container` **rules** that switch layout at those edges cannot be
custom properties (a query needs a compile-time length), so they are **not** part
of this token array — they belong in a renderer's own layout CSS, which can read
`--ab-base-bp-*` / `--ab-base-cq-*` for its query edges. Within a band the fluid
scales already adapt continuously, so most components need no query at all.
