# Theming tokens (`--cm-*`)

Theme values live as CSS custom properties, split across two files in
`src/extensions/adapt-ab-theme/less/`:

- **`cm-palette.less`** — the Cardiff Met **brand palette** (colours + paired
  `-rgb` triplets) and the **opacity scale**, brought in verbatim. The full
  palette (dark-blue, red, jasper, tomato, coral, sienna, khaki, bronze, brown,
  olive, green, teal, ocean, aquamarine, midnight, blue, purple, amethyst,
  violet, blossom, pink + neutrals) is present so pathways can later be themed
  with distinct accents. Values and names are the authoritative set from
  `cm-global.css`; see `cmet-design-system-source.md`.
- **`theme.less`** — the **semantic tokens** (what colours are used for), the
  **type scale**, the **spacing scale**, and the rules.

Every rule references a token, never a raw hex, so a palette change is one edit
and the incoming brand values map onto tokens rather than rewriting rules.

## Why plain CSS, not LESS

The brand file is plain CSS custom properties; LESS passes `:root{--x:…}` and
`var()` through untouched, so the blocks compile as-is into `build/adapt.css`.

## Adapt has no `h1`–`h6` — the type scale maps to title *classes*

Adapt renders divs with classes + `aria-level`, not heading elements. The
semantic heading level is the aria-level (set in `_accessibility._ariaLevels`:
page 1, article 2, block 3, component 4); the **visual** scale is applied to the
title classes:

| aria level | Adapt class | type token |
|---|---|---|
| 1 | `.page__title` | `--cm-h1-font-size` |
| 2 | `.article__title` | `--cm-h2-font-size` |
| 3 | `.block__title` | `--cm-h3-font-size` |
| 4 | `.component__title` | `--cm-h4-font-size` |
| (4, secondary) | `.knowledge-check-question .component__title` | `--cm-h5-font-size` |

Type sizes are the authoritative **Cardiff Met brand scale** from
`cm-global.css` (fluid `clamp(min, min + Nvw, max)`, so each size scales subtly
with the viewport): h1 2→3rem, h2 1.5→2.116rem, h3 1.3→1.75rem, h4 1.275→1.66rem,
h5 1.25→1.5rem, h6 1→1.166rem; weight 500; line-height 1.2. Tune via the
`--cm-h*-font-size` tokens.

## Spacing follows the hierarchy

The oversized gaps are vanilla's defaults. Four tokens set a rhythm that tracks
the structure (gap after a section > between blocks > between components >
within):

| token | applied to | default |
|---|---|---|
| `--cm-space-article` | `.article` margin-bottom + section-title top | 2.5rem |
| `--cm-space-block` | `.block` margin-bottom | 1.25rem |
| `--cm-space-component` | `.component` margin-bottom | 0.75rem |
| `--cm-space-within` | within-component | 0.5rem |

Tune the four tokens; the rules only reference them. These overrides are a
first pass — confirm against a build and adjust the values.

## Semantic + cue tokens

| token | value | use |
|---|---|---|
| `--cm-primary` | → `--cm-dark-blue` | links, buttons, focus, section rule |
| `--cm-weaker` / `-tint` | = `--cm-danger` (brand red) / 8% | worked-example weaker cue |
| `--cm-stronger` / `-tint` | = `--cm-success` (brand green) / 8% | worked-example stronger cue |
| `--cm-rule` | dark-blue @ 20% | section-header underline |

## Buttons and content styling

- **`cm-buttons.less`** — the canonical **`.cm.btn`** button object, ported from
  `cm-global.css` onto `--cm-*` tokens (replaces the retired `.btn-cmet`). The
  selector is the compound class `.cm.btn` (element carries both `cm` and `btn`),
  a namespace Adapt's own markup never emits. Variants: semantic `.primary` /
  `.secondary` / `.link`, Bootstrap-style `.btn-outline-<semantic>` (looped over
  primary/secondary/success/danger/warning/info/light/dark), a colour class per
  palette colour (`.cm.btn.dark-blue`, `.cm.btn.teal`, …) with the brand
  solid-fill → outline-on-hover behaviour, and sizes `.cm.btn-lg` / `.cm.btn-sm`.
  Full a11y (reduced-motion, high-contrast, forced-colors, 44px touch targets).
  Usage: `<a class="cm btn dark-blue" ...>`, `<a class="cm btn primary btn-lg" ...>`.
  The semantic colour layer it consumes (`--cm-primary/secondary/success/danger/
  warning/info/light/dark` + `-contrast/-hover/-active`) lives in `theme.less`.
- **`cm-links.less`** — the CM link system: a dotted blue underline that becomes
  a solid dark-blue underline on hover, from `cm-global.css`'s `--cm-link-*`
  tokens. Auto-applied to Adapt prose links (`.component__body a:not(.btn)`),
  plus an explicit `.cm-link` class for links elsewhere. Single class `.cm-link`
  (not `.cm.link`, which would clash with the `.cm.btn.link` button variant);
  buttons (`<a class="cm btn">`) are excluded via `:not(.btn)`.
- **`cm-cards.less`** — the CM card system: Bootstrap-5.3-shaped cards on the
  compound `.cm.card` class with part classes (`.card-header/-body/-footer/
  -title/-text/-img*`), colour variants (`.cm.card.<colour>`), scheme-accent
  (`.cm.card.accent`), and pedagogy-functional variants (do/dont/advice/action/
  starting/feedback-pos/feedback-neg). No Bootstrap dependency. See
  `card-system.md`.
- **`cm-callouts.less`** — the CM callout system: a left-border highlight box on
  `.cm.callout` with optional `.with-icon` (+ `.callout-icon` / `.callout-content`)
  and a `.callout-header`. Variants: pedagogy-named (`tip`=green, `note`/`info`=teal,
  `warning`=sienna, `important`=danger), every palette colour, and `.accent`
  (follows the series accent). Border + header take the variant colour; the body
  sits on a faint 6% tint. e.g.
  `<div class="cm callout warning"><p class="callout-header">Watch out</p><p>…</p></div>`
- **`cmet-content.less`** — panel styling: composable `.content_bg_<c>` /
  `.content_fg_<c>` / `.content_bdr_<c>` modifiers + `.content_style_<c>--white`
  (filled) and `.content_style_white--<c>-border` (outline) presets, generated
  via LESS over the blue/grey scheme (the brand paste set tokens it never
  applied; this applies real properties). Contrast caveat: a filled light
  colour + white text is decorative only, not for reading text.

## Not brought in (from the brand CSS)

- The gradient/modes blocks — deferred (dark mode is a later layer).
- The brand file's upstream `--cmet-*` semantic/mode layer references undefined
  tokens out of context; the base colours are brought in and we standardise on
  `--cm-*` and define our own type/spacing rather than import the placeholders.

## Colour schemes (`cm-schemes.less`)

The scheme system: a fixed neutral spine (surface/ink/hairline role tokens + a
greyscale ramp `--cm-greys-light/dark-10…90`) plus one `--cm-accent` variable
(default dark-blue) that re-themes a series via `.cm-scheme-<colour>` on a
wrapper. Section rules and focus outlines follow the accent. Includes a draft
`[data-theme="dark"]` mode. Full rationale + usage in `colour-schemes.md`.

## Responsive system (`cm-breakpoints.less`)

The breakpoint + fluid-spacing foundation from `cm-global.css`, brought in for
explicit device-design control (SCORM box). **Additive and removable** — it does
NOT override Adapt's own `.container`/`.row` grid, so deleting the file rolls it
back.

- **Breakpoints** (min-width): sm 576, md 768, lg 992, xl 1200, xxl 1400,
  **xxxl 1600**. As LESS vars `@cm-bp-*` (for `@media` in theme LESS) and mirrored
  custom properties `--cm-bp-*`.
- **Fluid spacing scale** `--cm-space-025 … --cm-space-600` (`clamp()` with `vi`
  units, so spacing scales with the viewport) + `--cm-gutter-x/y`.
- **`.cm-container`** — a namespaced centred container capping width per
  breakpoint (540/720/960/1140/1320/1580). Use on an author wrapper; never
  collides with Adapt's `.container`.
- **`.d-xxxl-*`** display utilities for the 1600px breakpoint Adapt/Bootstrap
  lack.

The full Bootstrap-style `.row`/`.col` grid is left in `cm-global.css` (not
ported) — Adapt has its own layout; bring it in only if that proves insufficient.

## Icons

Google Material Symbols, via `cmet-icons.less` (CDN prototype; self-host a subset
for production). See `docs/authoring/icons.md`.

## Still to do

- Brand **font families** (type sizes are in; fonts still to add as tokens).
- Tune the spacing tokens against a build.
- Complete the vanilla teal → dark-blue sweep (nav, progress, selected states).
- Icons: self-host a subset for offline SCORM; build the local pack (SVG + font
  subset) from the icons in use.
- Optional later: a dark-mode `modes` layer, per-pathway accent theming.
