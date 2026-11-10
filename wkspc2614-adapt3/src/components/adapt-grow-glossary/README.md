# adapt-grow-glossary

An **inline-glossary passage** for the Adapt framework — a short piece of teaching
prose with certain terms marked. Selecting a marked term reveals its definition in
a single region beneath the passage. The reading stays continuous; the definitions
are there when the learner wants them.

Part of the **GROW** plugin set, tokenised against the theme (accent and surface
tokens), so it repaints with the active theme and has a dark mode for free.

## Behaviour

- **Prose with marked terms.** The passage is authored as an ordered run of
  segments; the ones carrying a `_term` render as inline marker buttons.
- **One definition at a time.** Selecting a term opens its definition in a shared
  region below; selecting another term swaps it; a **Back to passage** control
  closes it.
- **Mark 2–8 terms** per passage (first use only); a console warning appears if
  that range is exceeded.
- **Completes when every marked term has been opened** — visitation is one-way,
  so opening each term once marks the component complete.

## Accessibility

- Markers are native `<button>`s with `aria-expanded` and `aria-controls` onto
  the definition region, each with a visually-hidden "Definition of: …" label.
- On expansion, focus moves to the definition region (an `aria-live="polite"`
  region); the Back control returns focus to the marker it came from. Reduced
  motion is honoured.

## Authoring

| Field | Purpose |
|---|---|
| `instruction` | Instruction text for the passage. |
| `_passage` | The passage as an ordered array of segments. A plain segment has only `text`; a term segment adds `_term` with a `term` (the headword) and its `definition`. |

See `example.json` for a full block.

## Settings

`_component` must be `growGlossary`; the target attribute is `_growGlossary`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
