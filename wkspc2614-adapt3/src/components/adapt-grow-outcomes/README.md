# adapt-grow-outcomes

**Learning Outcomes (GROW)** — presents a lesson's learning outcomes and reveals
them one at a time. Nothing is shown to begin with; each press of the reveal
button shows the next outcome. When the final outcome is revealed the button is
removed and the component calls `setCompletionStatus()` — which lets the trickle
Continue button appear and unlock the next section.

Because the component only completes once every outcome has been shown, it is
designed to sit under a **trickle step** on its block: the lesson-overview
section stays locked until the learner has clicked through all of its outcomes.

## Attributes

| Attribute | Type | Default | Notes |
|---|---|---|---|
| `_component` | string | `growOutcomes` | |
| `body` | string | `""` | Lead-in sentence, e.g. "By the end of this lesson, you will be able to:". |
| `instruction` | string | `""` | Optional helper line. |
| `_revealButtonText` | string | `Reveal next outcome` | Button label. |
| `_items[]` | array | — | `{ "text": "…" }` per outcome, revealed in order. |

## Trickle gate (authoring)

Put trickle on the component's **block** so the section completes only when the
outcomes are all revealed:

```json
"_trickle": {
  "_isEnabled": true,
  "_scrollDuration": 500,
  "_completionAttribute": "_isComplete",
  "_stepLocking": { "_isEnabled": true, "_isCompletionRequired": true, "_isLockedOnRevisit": false },
  "_button": { "_isEnabled": true, "_isFullWidth": false, "_styleBeforeCompletion": "hidden", "_styleAfterClick": "hidden", "text": "Continue" }
}
```

## Notes

- `ComponentView.postRender()` is a no-op, so the view calls `setReadyStatus()`
  itself. It deliberately does **not** use `setupInviewCompletion` — completion
  is the reveal interaction, not scrolling into view.
- On revisit a completed component restores fully revealed (no re-lock, given
  `_isLockedOnRevisit: false`).
