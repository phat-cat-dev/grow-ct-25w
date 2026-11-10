# adapt-grow-hero

A **hero banner** for the Adapt framework — a bold page or lesson opener with an
eyebrow label, a heading, body copy, optional leading icon or media, and a row
of call-to-action buttons. Use it to set up a lesson or page with a confident,
scannable opening.

Part of the **GROW** plugin set, tokenised to the GROW theme. The LESS here is
**structure only** — every visual (fill, layout, media placement, entrance
animation) comes from the theme's `.ab.hero` object system on `--ab-hero-*`
tokens, so the hero repaints with the active theme and gets a dark mode for
free. Call-to-action buttons reuse the theme's `.ab.btn` object.

## Presentation, not a question

The component extends the stock `ComponentModel`/`ComponentView` — no learner
input, no marking. Completion is by **inview** (becoming visible counts toward
page completion). If a front image is present, the view waits for it to load
before marking ready. The optional entrance animation respects
`prefers-reduced-motion`.

## Authoring

| Field | Purpose |
|---|---|
| `_variant` | Background fill: `neutral` (sunken band), `accent` (bold fill), `tinted` (faint accent). |
| `_align` | Text alignment: `left` (default) or `center`. |
| `_animate` | Small self-contained rise-in entrance (reduced-motion aware). |
| `_icon` | Optional leading icon-font class (e.g. `icon-star`); sets the icon-text layout. |
| `eyebrow` | Small label above the heading. |
| `heading` | The hero title. |
| `body` | Body copy below the heading. |
| `_media` | Optional image or video, placed `side` (beside the text) or `background` (behind, under a scrim). |
| `_ctas` | Array of action buttons (`text`, `url`, `_variant`, `_outline`), rendered as `.ab.btn`. |

See `example.json` for a full block.

## Settings

`_component` must be `growHero`; the target attribute is `_growHero`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
