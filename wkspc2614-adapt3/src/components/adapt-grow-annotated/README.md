# adapt-grow-annotated

An **annotated exemplar** for the Adapt framework — a passage of sample text with
numbered markers on chosen phrases. The learner selects a marker to open an
explanatory note beneath the passage. Use it to show *why* a piece of writing (or
code, or working) is good, phrase by phrase.

Part of the **GROW** plugin set and tokenised to the GROW theme: the marker
colour, note surface and muted text come from the theme's `--ab-*` tokens
(accent, accent-hover, surface, ink-muted, body font size), so it follows the
active pack and mode.

## Behaviour

- The passage is rendered as continuous prose. Annotated segments are underlined
  (never colour alone) and carry an inline superscript marker button labelled
  `[n]`.
- Selecting a marker opens a **single note region** below the passage showing the
  note title, the quoted referent phrase and the note body (HTML allowed). A
  **Back to passage** control closes it.
- Only one note is open at a time; opening another replaces it.

## Accessibility

- Markers are native `<button>`s with `aria-expanded` and `aria-controls`; the
  hidden `Note n` label names each one for screen readers.
- On open, focus moves to the `aria-live="polite"` note region; **Back to
  passage** returns focus to the marker that was clicked.
- Visited markers are dimmed; focus rings are visible; on narrow viewports
  markers grow to a 44px tap target. The reveal transition is dropped under
  `prefers-reduced-motion: reduce`.

## Authoring

The passage is an ordered array of segments; an annotated segment adds a `_note`.

| Field | Purpose |
|---|---|
| `instruction` | Instruction text for the exemplar. |
| `_passage[]` | Ordered segments. Each has `text` (the sentence or phrase). |
| `_passage[]._note` | Optional note on that segment: `title` (short heading) and `body` (the commentary, HTML allowed). |

See `example.json` for a full block.

## Settings

`_component` must be `growAnnotated`; the target attribute is `_growAnnotated`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
