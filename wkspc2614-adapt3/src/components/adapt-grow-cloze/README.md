# adapt-grow-cloze (GROW)

Fill the blanks (cloze). The learner chooses a word from a dropdown for each
inline blank in a sentence, then selects **Check**. Every blank is marked correct
or incorrect and an overall feedback message is announced. Generalised to any
number of blanks.

Matured from the "Fill the blanks" gallery pattern
(`abbott/assets/gallery/patterns-3.html`).

## Formative, not assessed

This is a formative **check**, not a question. The model extends
`ComponentModel` (not `QuestionModel`): it records **no** `cmi.interactions`,
produces **no** score, and sets no result status. Feedback is informational only.
Set `_isCompletionBearing: true` to let it complete the first time the learner
selects Check (that completion is informational, never a score or a SCORM
interaction); leave it `false` and the component never blocks completion.

## Authoring

Write the sentence in `text` as plain text with a placeholder for each blank:
`[[1]]`, `[[2]]`, and so on. Each number maps 1-based to the matching entry in
`_blanks`. Each blank is a set of `_options` plus the `_answer` (which must match
one of its options exactly).

```json
{
  "_id": "c-05",
  "_parentId": "b-05",
  "_type": "component",
  "_component": "growCloze",
  "_layout": "full",
  "displayTitle": "Fill the blanks",
  "instruction": "Choose a word for each blank to complete the sentence, then select Check.",
  "text": "A paragraph usually opens with a [[1]] sentence and ends with a [[2]] that links to the next idea.",
  "_blanks": [
    { "_options": ["topic", "concluding"], "_answer": "topic" },
    { "_options": ["transition", "quotation"], "_answer": "transition" }
  ],
  "_isCompletionBearing": true
}
```

Notes:

- `text` is plain text; HTML is not compiled inside it. A placeholder with no
  matching `_blanks` entry is left as literal text and a warning is logged.
- `_options` needs at least two choices. The first option shown in each dropdown
  is the unselected prompt (`blankPlaceholder`); an unanswered blank counts as
  incorrect on Check.
- All learner-facing strings (the Check label, the per-blank status words, and
  both feedback messages) live in the schema `globals` and are translatable.

## Accessibility

- The sentence is a `role="group"` with an accessible name (`ariaRegion`).
- Each dropdown has an `aria-label` ("Blank n of total").
- State is conveyed **non-visually as well as by colour**: a tick/cross glyph,
  `aria-invalid` on wrong blanks, and a visually-hidden status word per blank
  ("Correct"/"Incorrect") referenced by the dropdown via `aria-describedby`.
- The overall feedback is written to a polite, atomic `aria-live` region.
- Motion is disabled under `prefers-reduced-motion: reduce`.

## Theming

Study CSS variables are mapped to component-owned custom properties with
`--grow-*` / bare grow / `ab` fallbacks, e.g.
`var(--grow-accent, var(--accent, #365f80))`. The feedback colours fall back to
the study's own semantic positive/negative values (not brand colours); the weak
backgrounds fall back to a surface-aware `color-mix` so they stay legible when a
theme supplies no "weak" token (for example in dark mode). Colours flip for dark
mode through the live GROW tokens with no rebuild.

Like the other GROW components, the view calls `setReadyStatus()` itself.
