# adapt-grow-checklist

A **self-assessment checklist** for the Adapt framework — a collapsible panel of
tickable items, each a concrete yes/no action the learner can confirm they have
done. There is **no marking**: ticking is a reflective aid, not a scored answer.

Part of the **GROW** plugin set, tokenised against the GROW theme (accent,
surface and ink tokens), so it repaints with the active theme and has a dark mode
for free.

## Behaviour

- **A collapsible accordion.** The title is a toggle button; the list of
  checkboxes is collapsed by default and opens beneath it.
- **Opening is the gate, not ticking.** The first time the learner opens the
  checklist the component is marked complete (so it passes the trickle); which
  items they tick is up to them.
- **Ticks do not persist.** On revisit the boxes reset — the checklist is a
  prompt to think, not a stored response. Only visitation is tracked, never the
  checked state.
- A neutral **"N of M checked"** progress count updates as items are ticked, with
  no evaluative copy.

## Accessibility

- The toggle is a real `<button>` with `aria-expanded` / `aria-controls`; the
  region is labelled by the heading.
- Items are native `<input type="checkbox">` with associated `<label>`s, grouped
  in a `fieldset`/`legend`; the progress count is an `aria-live="polite"` region.
  Checked state is shown by weight and a tick, not colour alone, and focus stays
  on the ticked control.

## Authoring

| Field | Purpose |
|---|---|
| `instruction` | Instruction text for the checklist (used as the fieldset legend). |
| `_items` | The checklist items (4–8). Each has a required `text` — a concrete action phrased as a yes/no check. |

See `example.json` for a full block.

## Settings

`_component` must be `growChecklist`; the target attribute is `_growChecklist`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
