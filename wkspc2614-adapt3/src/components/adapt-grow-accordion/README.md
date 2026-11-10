# adapt-grow-accordion

A **vertical accordion** for the Adapt framework — a stack of headed panels where
the learner selects a heading to reveal its body and hide the others. Use it to
chunk reference material, worked examples or FAQ-style content into expandable
sections.

Part of the **GROW** plugin set and tokenised to the GROW theme: its colour and
surfaces come from the theme's `--ab-*` tokens (accent, sunken surface, ink,
hairline, spacing), so it repaints with the active pack and gets a dark mode for
free. The LESS defines no palette of its own.

## Behaviour

- Headings are native `<button>`s following the ARIA accordion pattern:
  `aria-expanded` + `aria-controls` on the header, and each panel is a
  `role="region"` labelled by its header.
- By default opening one panel closes the others. Set `_isMultiSelect` to allow
  several open at once.
- `_shouldExpandFirst` opens the first panel on load (and on a reset revisit).
- Open/close is a `max-height`/`opacity` transition; the open panel picks up the
  accent in its label and an inset left bar. Toggling does not move focus.

Optional presentation classes on `_classes` move the accent (`accent`, `success`,
`danger`, `warning`, `info`), drop the outer frame (`flush`), or give a compact
borderless accordion for running prose (`intext`).

## Authoring

| Field | Purpose |
|---|---|
| `instruction` | Instruction text shown below the component body. |
| `_isMultiSelect` | Allow several panels open at once (default `false`). |
| `_shouldExpandFirst` | Open the first panel on load (default `false`). |
| `_items[]` | The panels. Each has `_id` (optional, for analytics), `title` (the header button label and accessible name) and `body` (HTML). |

See `example.json` for a full block.

## Settings

`_component` must be `growAccordion`; the target attribute is `_growAccordion`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
