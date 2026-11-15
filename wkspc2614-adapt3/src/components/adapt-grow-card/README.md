# adapt-grow-card

**Information cards** for the Adapt framework — one or more self-contained cards,
each with an optional image, header, title, subtitle, body text, link and footer,
laid out as a responsive group. Use them for do/don't pairs, summary tiles,
linked resources or any set of short, parallel chunks.

Part of the **GROW** plugin set and tokenised to the GROW theme. This component
supplies structure only; all card visuals (background, border, cap, radius and
the per-variant styling) come from the theme's `.ab.card` system on `--ab-card-*`
tokens, and the group wrapper consumes `--ab-*` spacing tokens.

## Behaviour

- Purely presentational — no interaction handlers. The view waits for any card
  images to load before marking ready, then registers inview completion so a
  visible card counts toward page completion.
- A single card stacks; two or more (or `_isGroup`) render as an auto-fit grid
  (`minmax(16rem, 1fr)`). A group of exactly four is capped at two columns (2×2)
  via a `:has()` rule, so it never spreads to three or four across.
- `_hoverAnimate` lets cards lift on hover; `_tinted` washes the surface and cap
  with a faint tint from the variant accent.
- Each card's variant is its own `_variant`, falling back to the component
  `_variant`, then `neutral`.

## Authoring

| Field | Purpose |
|---|---|
| `instruction` | Instruction text shown below the component body. |
| `_variant` | Default card variant: `neutral`, `accent`, `do`, `dont`, `advice`, `action`, `starting`, `feedback-pos`, `feedback-neg`. |
| `_isGroup` | Force the `.card-group` layout even with a single card. |
| `_hoverAnimate` | Lift cards on hover. |
| `_tinted` | Tint the card surface and cap from the variant accent. |
| `_items[]` | The cards. Each may carry `_id`, `_variant` override, `_withIcon` + `_icon`, `header`, `title`, `subtitle`, `text` (HTML), `footer`, a top `_graphic` (`src` + `alt`) and a `_link` (`text` + `url`). A card should carry at least a title or text. |

See `example.json` for a full block.

## Settings

`_component` must be `growCard`; the target attribute is `_growCard`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
