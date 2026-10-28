# adapt-ab-base

The **base token layer** for the `adapt-ab-*` family. A style-only extension that
ships neutral `--ab-*` default values (and a minimal `.ab.card` base object) so
the components/extensions render correctly with **no brand theme present**.

## What it provides

- `less/ab-base.less` — `:root` defaults for the token spine:
  - ink/surface: `--ab-base-ink`, `--ab-base-ink-muted`, `--ab-base-surface`,
    `--ab-base-surface-sunken`, `--ab-base-hairline`, `--ab-base-border-width`
  - accent: `--ab-accent`, `--ab-accent-rgb`, `--ab-on-accent`
  - semantic: `--ab-success(-rgb)`, `--ab-danger(-rgb)`, `--ab-warning(-rgb)`, `--ab-info(-rgb)`
  - shape/type: `--ab-border-radius`, `--ab-h4-font-size`
  - spacing: `--ab-space-050 / -075 / -100 / -125 / -200`
- `less/ab-base-card.less` — a compact, token-based `.ab.card` (so `adapt-ab-card`
  renders without the brand `ab-cards.less`).

## The base-vs-theme seam

- **Components consume** these tokens with fallbacks (`var(--ab-base-surface, #fff)`)
  and never hardcode a palette.
- **A theme overrides** by redefining the same custom properties — globally, or
  under a scope class (e.g. `.ab-theme-x { --ab-accent: … }`). It does not edit
  component or base files.

Load order: this base loads first (defaults); a theme loaded after wins. If the
full brand theme (`adapt-abbott-theme`) is present, its richer `ab-cards.less`
and token definitions supersede this minimal layer.

## Covers these plugins

Every `--ab-*` token referenced by `adapt-ab-card`, `adapt-ab-accordion`,
`adapt-ab-carousel` and `adapt-ab-modal` is defined here, so a pristine install
with just those plugins + this base renders styled with zero theme.

No runtime behaviour; no configuration.
