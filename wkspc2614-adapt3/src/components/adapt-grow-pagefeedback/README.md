# adapt-grow-pagefeedback

An **end-of-page self-report** component for the Adapt framework — a two-choice
"was this page helpful?" response (a positive and a negative button) plus an
optional free-text note. Use it at the foot of a page to gather a quick,
low-friction signal on how the page landed.

Part of the **GROW** plugin set, tokenised to the GROW theme (it uses
`--ab-base-accent`, `--ab-base-on-accent`, `--ab-base-hairline`,
`--ab-success` tokens, so it repaints with the active theme and has a dark mode
for free).

## Not a question

The component extends `ComponentModel`/`ComponentView`, **not** `QuestionModel`
— there is no array of items and no correct answer. The response and note are
persisted via `offlineStorage` custom keys into **`cmi.suspend_data`**, not
`cmi.interactions`, which avoids the 250-character truncation and the false
`result: incorrect`.

## Behaviour and accessibility

- A **"choose, then act" flow**: the note field and Save/Clear buttons stay
  hidden until a response is chosen.
- The two choices are an `aria-pressed` pair inside a `role="group"` labelled by
  `choicesGroupLabel`; only one is active at a time.
- A `role="status"` line reports each step (prompt → chosen → saved / failed /
  cleared). The note textarea is uncontrolled, so typing never fights a
  re-render.
- When `_isCompletionBearing` is on, **saving a response completes the
  component** (there is no separate complete button) and shows a thank-you chip;
  completion is sticky — never revoked by a later clear.
- All learner-facing strings are translatable schema globals.

## Authoring

| Field | Purpose |
|---|---|
| `_variant` | Visual treatment only (illustration/accent): `conversation`, `growth`, or `fieldnote`. Does not change data or behaviour. |
| `_choicePositiveLabel` | Label for the helpful response; blank uses a variant default (e.g. "Yes, it helped"). |
| `_choiceNegativeLabel` | Label for the not-helpful response; blank uses a variant default (e.g. "Not quite"). |
| `_isCompletionBearing` | When true, saving a response contributes to lesson completion (sticky). |

See `example.json` for a full block.

## Settings

`_component` must be `growPagefeedback`; the target attribute is
`_growPagefeedback`. Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
