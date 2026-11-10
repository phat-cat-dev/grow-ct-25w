# adapt-grow-scroll-scenes

A scroll-linked sequence of full-height **scenes**. Each scene fades, zooms,
blurs or slides as it reaches the centre of a native-scrolling viewport.
Scrolling back reverses the effect, because every value comes from scroll
position, not from a timer.

This is the matured Adapt component built from the `scroll-scenes` study in
`abbott/assets/interactive/scroll-scenes`. The engine, the look (11 backgrounds,
5 transition models, colour schemes) and the accessibility story are the
study's; this package repackages them as a GROW component.

- **Original engine** — no external libraries, fonts or network access.
- **Design is authored, not shown.** The learner sees only the scroll. Effect,
  background, transition and scheme are chosen once at authoring time via a
  preset plus optional overrides — there is no on-screen settings toolbar.
- **Accessible by default** — native scrolling works without JavaScript and
  without the effect; reduced motion, forced colours and print are all handled;
  nothing is hidden from assistive technology.

## Files

```
adapt-grow-scroll-scenes/
├─ bower.json                     Adapt plugin manifest (component "scrollScenes", _scrollScenes)
├─ properties.schema              Authoring fields (the content + design pipe)
├─ example.json                   A ready component block to drop into a course
├─ js/
│  ├─ adapt-grow-scroll-scenes.js registration
│  ├─ ScrollScenesModel.js        ItemsComponentModel subclass (presentational)
│  ├─ ScrollScenesView.js         ComponentView: mounts the engine, inview completion
│  ├─ scrollScenesDriver.js       the scroll engine (ESM port of the study)
│  ├─ scrollScenesLogic.js        pure maths + the preset/override resolver (tested)
│  └─ package.json                {"type":"module"} — so `node --test` treats js/ as ESM
├─ templates/scrollScenes.jsx     learner-facing markup (just the scroll)
├─ less/scrollScenes.less         ported CSS; reads GROW tokens, falls back to study values
└─ test/scrollScenesLogic.test.js unit tests (node:test)
```

## How the design options work (preset + overrides)

Pick a **preset**, then optionally override any single dial. An empty override
means "use the preset". An unknown value falls back to the preset (authoring
input degrades, it never breaks the page).

| `_preset` | scheme | background | transition | effect |
|---|---|---|---|---|
| `original` | default | lines | none | zoom |
| `calm` | default | wash | none | zoom |
| `technical` | default | grid | drift | fade |
| `editorial` | warm | spotlight | stagger | fade |
| `atlas` | dusk | contour | tilt | fade |
| `horizon-rise` | default | horizon | rise | fade |
| `night-study` | night | aurora | none | blur |
| `custom` | default | lines | none | zoom (then override every dial yourself) |

Overrides: `_scheme` (default/night/warm/dusk), `_background` (lines, aurora,
mesh, dots, grid, contour, horizon, spotlight, weave, wash, plain),
`_transition` (none, rise, drift, tilt, wipe, stagger), `_effect` (zoom, blur,
fade, slide, none). Plus `_snap`, and `_showNav` / `_showProgress` /
`_showStatus` for the optional navigation row.

A single scene can override the background (`_background`) and force a colour
slot (`_colourSlot` 1–4; 0 = automatic). See `properties.schema` for the full,
documented field set, and [STYLE-STRUCTURE.md](../../assets/interactive/scroll-scenes/STYLE-STRUCTURE.md)
in the study for how the backgrounds and transition models are constructed.

## Authoring a scene

Each item in `_items` is one scene:

- `stageLabel` — short eyebrow, e.g. "Observe" (also the scene-button label; the
  number is added automatically).
- `heading` — the large heading; use `<br>` for deliberate line breaks.
- `body` — the supporting copy.
- optional `_extras` — teaching prompts shown beneath the body, matching the
  retired `scenes.py` output: `questionPrompt` ("Ask yourself: …"),
  `microTask` `{minutes, instruction}` ("Try this (N min): …"), `evidenceCue`
  ("You will know it worked when: …"), `reflectionNote` ("In your notes: …")
  and `transitionCue` (a short italic hand-off to the next scene).

`example.json` is a complete four-scene block you can paste into a course's
`components.json`.

## Theming

The LESS reads the GROW runtime tokens first — `--accent`, `--ink`,
`--surface-1`, `--font-ui` on `:root` — and falls back to the study's own
values, so the component picks up the active theme and dark mode automatically.
The `night` / `warm` / `dusk` schemes remain available as explicit,
author-chosen overrides.

## What changed from the study

- The demo workshop chrome (the effect/snap dropdowns, download links) is gone.
  Those dials are now **authoring settings**, not a learner-facing toolbar.
- The `scene-content` **YAML schema + `scenes.py`** content pipeline is retired:
  its job — piping authored content and a chosen look into a finished render —
  is now done natively by `properties.schema` + the Adapt build. The scenes, the
  presentation and the optional extras all map onto authoring fields.
- The two-line transition-model patch from the study (STYLE-STRUCTURE.md §5.4)
  is **folded into the engine**: the driver writes `--scene-offset` and
  `--scene-distance` every frame, so `rise`/`drift`/`tilt`/`wipe`/`stagger`
  work with no external bridge.

## Developing

Run the logic tests:

```bash
cd adapt-grow-scroll-scenes
node --test test/scrollScenesLogic.test.js
```

The LESS compiles under the build's Less 3.x. Two study idioms were adjusted for
that compiler: `:is(a, b)` groupings are written as plain comma selector lists,
and the one CSS `min()` is escaped (`~"min(…)"`) so Less does not treat it as its
own `min()` function. The output is identical.

## Installing into the GROW build

This component is staged in the `abbott/components` workbench. To use it in the
Adapt build, copy the folder to
`wkspc2614-adapt3/src/components/adapt-grow-scroll-scenes/`, add the component to
the relevant block's `components.json` (see `example.json`), then
`npx grunt build`. The component attribute is `_scrollScenes` and the component
type is `scrollScenes`.

## Authoring contract (for agents)

Fill ONLY the content; let the preset own the look. The minimal, stable shape
(see `example.json`) is:

```jsonc
{
  "_component": "scrollScenes",
  "_preset": "editorial",          // tone → preset: calm · technical · editorial · atlas · horizon-rise · night-study · original
  "_items": [                      // 3–6 scenes, in scroll order
    { "stageLabel": "Observe",     // REQUIRED. one word; the scene number is added automatically
      "heading": "Start with<br>what you notice.",  // REQUIRED. <br> controls line breaks; ~20 chars/line
      "body": "One or two sentences of supporting copy." }
  ]
}
```

Rules:
- Write `stageLabel` + `heading` + `body` for every scene; nothing else is needed.
- Do NOT set `_scheme`, `_background`, `_transition`, `_effect` or the per-scene
  `_background` / `_colourSlot` — the preset drives all of them. Touch those only
  for a deliberate one-off, never as routine authoring.
- Pick the preset by tone, not by colour; the active theme supplies the palette.
- `_extras` (question prompt, micro task, evidence cue, reflection note,
  transition cue) are optional teaching add-ons, not part of the core fill.
