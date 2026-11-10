# adapt-grow-expanding-links

Expanding Links (GROW) is a formative learning-sequence stepper whose step
buttons **are** expanding icon-links. Each step button shows an icon at rest and
expands its short label on hover, keyboard focus and for the current step. Only
the current step's activity is shown; **Back** and **Next** navigate. Completion,
when enabled, is an explicit learner action, never a score and never a SCORM
interaction.

Matured from the self-contained study at
`abbott/assets/components/expanding-links/` (the expanding-label grid technique,
the learning-sequence player, keyboard, ARIA and reduced-motion behaviour), ported
into the Adapt View lifecycle.

- **Registered name / `_component`:** `growExpandingLinks`
- **Model:** extends `ComponentModel` (not `QuestionModel`) and stays entirely
  outside the scoring machinery (no interactions, no marking).

## Attributes

Standard component attributes (`_id`, `_parentId`, `_type`, `_component`,
`_classes`, `_layout`, `displayTitle`, `body`, `instruction`, `_isOptional`, ...)
apply as usual. Component-specific attributes:

| Attribute | Type | Default | Notes |
| --- | --- | --- | --- |
| `_isCompletionBearing` | Boolean | `false` | `false`: formative only, completes on inview (seen = done). `true`: completion becomes an explicit learner action governed by `_completionCriteria`. |
| `_completionCriteria` | String | `allStepsComplete` | Only when `_isCompletionBearing` is `true`. `allStepsComplete`: every step must be marked complete. `finalStep`: completes on reaching the final step. |
| `_labelDisplay` | String | `expandOnActive` | `expandOnActive`: labels expand on hover, focus and for the current step (touch and narrow screens always show them). `always`: labels stay expanded on all pointer types. |
| `_steps` | Array | `[]` (min 1) | Ordered steps. Each step has `_icon`, `label`, `body`. |

### A step

| Field | Type | Notes |
| --- | --- | --- |
| `_icon` | String | Either a **Material Symbols** icon name (for example `explore`, `edit`, `lightbulb`) **or** an **inline SVG** snippet beginning with `<svg`. Inline SVG needs no font and inherits the current colour (via `stroke`). Material Symbols require the Material Symbols font to be present in the course. |
| `label` | String | Short label. Hidden at rest; expands when the step is current or on hover and keyboard focus. Keep it short. |
| `body` | String (HTML) | The step's activity or explanation. Shown only when this step is the current step. |

## Learner-facing strings (globals)

Every fixed interface string lives in the schema `globals` block, keyed to this
component (`_globals._components._growExpandingLinks`), so it is translatable and
editable without touching code. Defaults are British English, address the learner
as "you", and contain no em dashes:

`navAriaLabel`, `stepLabel` (`{{number}}`, `{{label}}`), `stepLabelCompleted`,
`statusText` (`{{current}}`, `{{total}}`, `{{completed}}`), `sequenceCompleteText`,
`backButton`, `nextButton`, `markStepButton`, `stepCompletedButton`.

Per-step `label` and `body` are authored content (translatable), not fixed strings.

## Behaviour

- Only the current step's activity is shown after mount. Without JavaScript every
  authored activity stays visible (progressive enhancement); the view hides the
  non-current panels and is also overridden for print.
- Step buttons keep focus when clicked. **Back** / **Next** move focus to the new
  step panel (`tabindex="-1"`, named from the step label) without scrolling.
- The current step uses `aria-current="step"`, which also expands its label.
- **Mark step complete** records a formative, non-scored completion for that step
  and shows a tick. The polite `role="status"` line reports progress and announces
  when every step is complete.
- `growExpandingLinks:change` and `growExpandingLinks:progress` bubble as DOM
  `CustomEvent`s on the component element with `{ index, total, completed }`
  (`completed` is the sorted list of completed indices), preserving the study's
  event API.

## Completion and tracking (formative)

- `_isCompletionBearing: false` completes the component on inview via the standard
  `ComponentView` mechanism (seen = done) so it never silently blocks page
  completion. This is not a score.
- `_isCompletionBearing: true` sets completion only on the explicit learner action
  defined by `_completionCriteria` (`allStepsComplete` or `finalStep`), via
  `setCompletionStatus()`.
- Completion is sticky across revisits (protected in `reset()`), mirroring the
  opentext pattern. Step progress itself (the current index and the marked set) is
  ephemeral per the study and is not persisted. Nothing writes `cmi.interactions`
  or a score.

## Theming / tokens

The study's own custom properties are kept as the component contract and mapped to
the GROW runtime tokens with literal fallbacks (no brand colours are hardcoded):

```less
--expand-accent: var(--grow-accent, var(--accent, #365f80));
--expand-ink:    var(--grow-ink, var(--ink, #172e3a));
--expand-line:   var(--grow-line, var(--line, #afc0ca));
--expand-duration: 300ms;
```

Type uses the GROW fluid tokens (`--fs-base`, `--fs-sm`, `--fs-xs`) and
`--font-ui`. Reduced motion disables the label transition via
`prefers-reduced-motion`, and the host opt-out classes `.no-motion` /
`[data-tm-no-motion="true"]` are honoured, as in the study.

## Example

See `example.json` in this folder for a complete three-step component. A minimal
snippet:

```json
{
  "_id": "c-05",
  "_parentId": "b-05",
  "_type": "component",
  "_component": "growExpandingLinks",
  "_isCompletionBearing": true,
  "_completionCriteria": "allStepsComplete",
  "_steps": [
    { "_icon": "explore", "label": "Explore", "body": "<p>Read the scenario.</p>" },
    { "_icon": "edit", "label": "Try", "body": "<p>Attempt the task.</p>" },
    { "_icon": "lightbulb", "label": "Reflect", "body": "<p>How would you apply this?</p>" }
  ]
}
```
