# adapt-grow-scenario

A **branching scenario** component for Adapt. The page shows a title, an intro and a
launch button; the scenario plays card by card in Adapt's `notify` popup. The student
makes decisions, sees the consequences, can recover from a weak start, and reaches a pass
or fail ending that explains why. Independent of Trickle and Branching.

- Component: `growScenario` · targetAttribute `_growScenario`.
- Uses the v6 React/JSX component API; compiles on adapt_framework ≥ 5.19 (verified on the
  5.56.3 harness, which ships React).

## This is the presentation half only

Scenarios are **authored and compiled** by the toolchain at
[`../../adapt-tools/scenario-builder`](../../adapt-tools/scenario-builder/). This plugin
only *plays* a compiled scenario (the `_scenario` object on the component). The engine,
player and card layouts in `js/` are **copies synced from that toolchain** by its `build`
command — do not hand-edit `js/engine.js`, `js/player.js`, `js/card-layouts.js` or
`less/grow-scenario-player.less`.

## Settings

| Property | Default | Notes |
| --- | --- | --- |
| `_completionOn` | `"ending"` | or `"pass"` (completes only on a pass ending) |
| `_launch.{startText,resumeText,reviewText}` | Start / Return to / Review the scenario | launch button label by state |
| `_scenario` | required | the compiled scenario; produced by the toolchain |

See `example.json` for a working component. Full notes, caveats (Spoor saving, private
notes, completion trap) and the authoring flow:
[`adapt-docs/adapt_abbdev/components/adapt-grow-scenario`](../../adapt-docs/adapt_abbdev/components/adapt-grow-scenario/adapt-grow-scenario.md).

## Styling

The player reads `--grow-scenario-*` custom properties and ships literal fallbacks, so it
is legible with no theme work. Map the tokens to your theme in `less/grow-scenario.less`.
