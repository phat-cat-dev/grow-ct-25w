# adapt-grow-wizard (GROW)

A **step wizard**: a guided multi-step flow with a progress bar. A progress bar
fills to track the current step, a row of step labels highlights the one you are
on, the content panel fades in per step, and Back and Next move you through the
steps (clamped at the first and last).

The steps are authorable: an ordered array, each step with a short label and a
panel body (HTML). Progress and the active label are computed from the current
step.

Matured from the "Step wizard" gallery pattern
(`abbott/assets/gallery/patterns-3.html`).

## Register name

- `_component`: `growWizard`
- Component scope class in the DOM / LESS: `.wiz`

## Authoring

```json
{
  "_component": "growWizard",
  "displayTitle": "How to plan an essay",
  "body": "<p>Work through each step in order. The progress bar fills as you go.</p>",
  "instruction": "Move through the steps with the Back and Next buttons.",
  "_isCompletionBearing": true,
  "_steps": [
    { "label": "Intro",    "body": "<p>What this guide covers and why it helps.</p>" },
    { "label": "Explore",  "body": "<p>A worked example.</p>" },
    { "label": "Practise", "body": "<p>A short activity to apply it.</p>" },
    { "label": "Review",   "body": "<p>Recap the key points.</p>" }
  ]
}
```

### Properties

- `_steps` (array, required): the ordered steps. Each step has a `label` (short,
  one or two words, shown in the progress track) and a `body` (HTML shown in the
  panel when the step is active).
- `_isCompletionBearing` (boolean, default `false`): see Completion below.
- `instruction` (string, optional): guidance shown above the wizard.
- Standard component fields (`displayTitle`, `body`, `_classes`, `_layout`) work
  as usual.

### Globals (learner-facing strings)

All fixed learner-facing strings live in the schema `globals`, so they are
translatable and set once per course:

- `backButton` ("Back"), `nextButton` ("Next")
- `regionLabel` ("Step-by-step guide") and `progressLabel`
  ("Progress through the steps") name the widget and the progress bar
- `progressValueText` ("Step {{current}} of {{total}}") is the spoken progress
  value
- `stepAnnouncement` ("Step {{current}} of {{total}}: {{label}}") is the polite
  announcement made when you move to another step

## Completion and tracking

Formative only. The model extends `ComponentModel` (not `QuestionModel`), so the
component is entirely outside the scoring machinery: no interactions, no marking,
no score, and no SCORM interaction is ever written.

- `_isCompletionBearing: true` — the component marks itself complete once you
  reach the final step.
- `_isCompletionBearing: false` (default) — the component is presentational and
  completes on view, so it never blocks page or trickle completion.

Completion is sticky: a hard reset on revisit does not silently wipe it (mirrors
the opentext pattern).

## Accessibility

- The progress bar is a `role="progressbar"` with `aria-valuemin`/`-valuemax`/
  `-valuenow` and an `aria-valuetext` reading "Step X of Y".
- The active step label carries `aria-current="step"`.
- Only the current panel is visible and in the accessibility tree and tab order;
  the others are `hidden`.
- Step changes are announced politely via a live region.
- Back and Next are disabled at the ends; focus moves to the still-enabled button
  so keyboard focus is never stranded on a disabled control.
- The progress-width and panel-fade transitions are disabled under
  `prefers-reduced-motion: reduce`.

## Theming

No hardcoded brand colours. The study CSS variables (`--accent`, `--surface-1`,
`--line`, `--ink`, `--ink-soft`, `--fs-*`, `--font-mono`) are mapped to the
component's own `--wiz-*` custom properties with grow/ab fallbacks, for example
`var(--grow-accent, var(--accent, #365f80))`. The component retints with the live
GROW hue and flips for dark mode without a rebuild.

## Notes

- Like the other GROW components, the view calls `setReadyStatus()` itself
  (`ComponentView.postRender()` is a no-op in this fork).
- The JSX renders a static shell; step changes are applied imperatively by the
  view, so the authored panel markup is never discarded by a React re-render.
