# adapt-grow-callouts

**Callouts** for the Adapt framework — short, scannable asides that sit beside the
main text: a tip, a note, a do, a don't, a warning. One or more callouts, each
with an optional title, body text and leading icon, laid out as a responsive
group.

Part of the **GROW** plugin set and tokenised to the GROW theme. This component
supplies structure only; all callout visuals (background, border, accent, the
per-variant styling and icon glyph) come from the theme's `.ab.callout` system on
`--ab-callout-*` tokens, and the group wrapper consumes `--ab-*` spacing tokens.

## Behaviour

- Purely presentational — no interaction handlers. The view marks ready
  immediately and registers inview completion, so a visible callout counts toward
  page completion.
- A single callout stacks; two or more (or `_isGroup`) render as an auto-fit grid
  (`minmax(18rem, 1fr)`), so paired callouts sit side by side where there is room
  and collapse to one column on narrow screens.
- Each callout's variant is its own `_variant`, falling back to the component
  `_variant`, then `neutral`.

## Authoring

| Field | Purpose |
|---|---|
| `instruction` | Instruction text shown below the component body. |
| `_variant` | Default variant for every callout: one of `neutral`, `accent`, `note`, `tip`, `info`, `advice`, `do`, `dont`, `warning`, `caution`, `action`, `starting`, `feedback-pos`, `feedback-neg`. |
| `_isGroup` | Force the responsive group layout even with a single callout. |
| `_items[]` | The callouts. Each has `_id` (optional), `_variant` (per-callout override), `_withIcon` + optional `_icon` class, `title` and `text` (HTML). A callout should carry at least a title or text. |

See `example.json` for a full block.

## Settings

`_component` must be `growCallouts`; the target attribute is `_growCallouts`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
