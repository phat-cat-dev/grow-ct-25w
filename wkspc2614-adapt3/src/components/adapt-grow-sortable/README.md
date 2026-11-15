# adapt-grow-sortable

An **ordering question** for the Adapt framework — the learner puts a set of
items into the correct sequence, by dragging with a mouse/touch or entirely from
the keyboard, then submits for marking.

Part of the **GROW** plugin set, and tokenised to the GROW theme (items, hover,
grabbed, drop-target and correct/incorrect states all read from theme custom
properties such as `--ab-base-accent`, `--ab-base-ink`, `--ab-success` and
`--ab-danger`), so it repaints with the active theme.

## A real question

It extends `ItemsQuestionModel` / `QuestionView`, so it plugs into the normal
scoring, feedback, attempts and model-answer machinery. Items are **authored in
the correct order** and shuffled (Fisher-Yates) for display. Marking is
**all-or-nothing**: every item must be in its correct position to score. Resets
re-shuffle. Results report to the LMS as a SCORM **`sequencing`** interaction
(unless `_recordInteraction` is off).

## Accessibility

- Each item is focusable; **arrow keys** move focus, **Enter/Space** picks an
  item up and drops it ("grabbed" state), arrows then move it, **Home/End** jump
  it to the ends, **Escape** releases it.
- Explicit **move-up / move-down buttons** on each item for pointer users.
- Standard HTML5 **drag-and-drop** for mouse/touch.
- An **ARIA live region** announces every move ("… moved to position n of m");
  focus follows the moved item. Announcement strings are authorable globals
  (`ariaItemMoved`, `ariaMoveUp`, `ariaMoveDown`, `ariaCorrectAnswer`,
  `ariaUserAnswer`, `ariaRegion`).

## Authoring

| Field | Purpose |
|---|---|
| `_items[].text` | The item text. Author the items **in the correct order**. Required. |
| `instruction` | Instruction text above the list. |
| `_attempts` | How many attempts are allowed (default 1). |
| `_canShowModelAnswer` | Let the learner view the correct order after answering. |
| `_canShowFeedback` / `_canShowMarking` | Show feedback / per-item marking. |
| `_shouldDisplayAttempts` | Show remaining attempts. |
| `_questionWeight` | Score weight (default 1). |
| `_recordInteraction` | Record to `cmi.interactions` (default true). |
| `_feedback` | Correct / incorrect / partly-correct feedback text. |

See `example.json` for a full block.

## Settings

`_component` must be `growSortable`; the target attribute is `_growSortable`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
