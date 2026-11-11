# Colour schemes — the CM scheme system

`src/extensions/adapt-ab-theme/less/cm-schemes.less`

A modern, subtle, minimal colour architecture: one fixed neutral **spine** plus
**one accent variable** that re-themes a whole series. Swapping the accent shifts
the mood; the spine never moves, so a programme of pathways stays visibly one
family while each series can carry its own colour.

## The idea in one line

> Fixed neutrals (white / white-subtle / greys / black) + dark-blue as the
> default accent. Change `--cm-accent` and a series re-themes; everything else
> holds still.

Accent is used **sparingly** — section rules, focus rings, small fills, a faint
8% tint — never as large flat fills of brand colour. That restraint is what keeps
it modern and minimal rather than loud, and it is why swapping the accent never
destabilises a page: most of what you see is the neutral spine.

## Four layers

1. **Greyscale ramp** — `--cm-greys-light-10…90` and `--cm-greys-dark-10…90`,
   mixed from `--cm-greys-middle` toward white / black. The neutral stops for
   hairlines, dividers, muted text and sunken surfaces.
2. **Role tokens (the spine)** — semantic names, not colours, so rules reference
   intent:
   | token | light default | use |
   |---|---|---|
   | `--cm-surface` | white | page background |
   | `--cm-surface-subtle` | white-subtle | cards / raised panels |
   | `--cm-surface-sunken` | light-grey | wells / inset areas |
   | `--cm-ink` | black-subtle | primary text |
   | `--cm-ink-muted` | dark-grey | secondary text |
   | `--cm-hairline` | greys-light-80 | 1px borders / dividers |
   | `--cm-on-accent` | white | text on an accent fill |
3. **Accent** — `--cm-accent` (default dark-blue) with derived
   `--cm-accent-hover` / `-active` (darker), `--cm-accent-tint` (8% wash on the
   surface) and `--cm-accent-line` (20% hairline). A series overrides just
   `--cm-accent` (+ `-rgb`); everything derived follows.
4. **Dark mode (DRAFT)** — `[data-theme="dark"]` (and the OS preference, unless
   `data-theme="light"` is set) flips the spine to a dark surface / light ink and
   lifts the accent toward white so it stays legible. First cut to look at;
   per-series dark accents still need contrast tuning.

## Using it — per-series theming

Put a scheme class on a page/menu wrapper (or `<body>`) and that subtree
re-themes:

```html
<div class="cm-scheme-teal">   <!-- this pathway reads teal -->
  … lessons, components … 
</div>
```

Available: `.cm-scheme-<colour>` for every accent
(`dark-blue, midnight, blue, ocean, teal, aquamarine, green, olive, khaki,
bronze, brown, sienna, coral, tomato, jasper, red, purple, amethyst, violet,
blossom, pink`). The default (no class) is dark-blue.

What currently responds to the accent: **section-header rules** (`--cm-rule`)
and **focus outlines**. These are wired in `theme.less`. More touches (small
fills, accented callouts) can be pointed at `--cm-accent*` as components are
built — deliberately kept few so the look stays restrained.

## Consistency vs. variation — the deliberate split

- **Constant across the whole programme:** the neutral spine, body type, spacing
  rhythm, layout. This is what makes 39 pathway-tiers feel like one product.
- **Varies per series:** the accent only. Enough to give a pathway identity,
  never enough to fork the design.

## Notes / open tuning

- `color-mix()` is used throughout (hover/active/tint, greyscale, dark surfaces).
  Supported in current Chromium — fine for Moodle SCORM; verify on the target
  Moodle's browser baseline when the pilot is packaged.
- Links keep their own blue (`cm-links.less`) rather than following the accent —
  a consistency choice; say if you'd rather links re-theme per series.
- Dark mode is a draft; it is opt-in and does not affect the default light
  appearance.
