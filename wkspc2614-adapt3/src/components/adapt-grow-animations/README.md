# adapt-grow-animations

Hand-drawn **note-taking marks** for Adapt — 58 re-colourable, re-animatable marks that
**draw themselves on** when the component appears. Underlines, highlighters, ticks, arrows,
ovals and handwritten notes, each a self-contained SVG/CSS unit whose colour is a **theme
role** (never a fixed hue) and whose speed follows the theme's motion dial.

Derived from the Abbott **animation-manager** authoring tool; this is its runtime as an
Adapt component. The tool stays the way you *pick and tune* a mark; this component is how a
built course *renders* one.

## The 58 marks (6 families)

- **emphasis** (8) — `underline` `double-underline` `wavy-underline` `circle` `box` `brackets` `strike` `scribble`
- **highlighter** (1) — `highlight` (band height / position / length controllable)
- **standalone** (5) — `tick` `cross` `star` `caret` `big-tick`
- **shapes** (26) — arrows (`arrow-right/-left/-up/-down/-curved/-double/-return/-zigzag/-hook/-bold/-thin/-dotted/-sweep`), `circle-shape` `dot` `target` `square` `rounded` `check-box` `exclaim(-circled)` `question(-circled)` `line-dotted/-dashed/-dotted-arrow`
- **ovals & rectangles** (11) — `oval-phrase` `oval-long` `oval-double-ring` `oval-left` `oval-triple` `rectangle` `rectangle-stacked` `boxes-row` `bar-stretch` `circles-row` `rules`
- **handwritten notes** (7) — `hand` `hnote` `margin-note` `teacher-mark` `correction` `sticky` `checklist-item`

Full data (ids, keywords, categories, SVG) is in
[`adapt-content-templates/adapt-grow-animations/animations.json`](../../adapt-content-templates/adapt-grow-animations/animations.json).

## Authoring

```json
{
  "_component": "growAnimations",
  "_markLayout": "inline",
  "_marks": [
    { "_id": "highlight", "text": "key idea", "_color": "neutral" },
    { "_id": "circle",    "text": "this one", "_color": "negative", "_repeats": 2 },
    { "_id": "tick",      "_color": "positive", "_scale": 1.2 },
    { "_id": "margin-note","text": "see here", "_color": "pen", "_rotation": -4 }
  ]
}
```

| Field | Meaning |
|---|---|
| `_id` | one of the 58 catalogue ids |
| `text` | the word/phrase a wrap/highlight/note mark carries (ignored by standalone marks) |
| `over` | `correction` only — the replacement word written above the strike |
| `_color` | a **role**: `accent` `positive` `negative` `neutral` `comment` `pen` `ink` |
| `_speed` | 0.4–2.5 draw speed (overrides `--flow-rate` for this mark) |
| `_scale` | 0.3–3 size · `_rotation` -45–45° · `_repeats` 1–10 passes · `_jitter` 0–10° |
| `_markLayout` | `inline` (flow together) or `stack` (one per row) |

## How it aligns with the GROW theme (tokenisation)

The marks are driven by theme tokens, so they reskin with the course:

| Concern | Token |
|---|---|
| **Colour** | `_color` → `--accent` / `--c-positive` / `--c-negative` / `--c-neutral` / `--c-comment` / `--pen` / `--ink` (each with a self-contained fallback) |
| **Speed** | draw timings are `calc(… / var(--am-rate, var(--flow-rate, 1)))` — a per-mark `_speed` wins, else the theme's `--flow-rate`, else 1 |
| **Wobble** | the hand-drawn jitter uses the shared `#ink` SVG filter — the same one the GROW/Abbott theme injects; the component adds a fallback `#ink` only if the page has none |

Per-instance geometry (`--am-scale`, `--am-rot`, `--am-d` stroke delays, `--am-turn-*`
jitter) stays on the mark as inline custom properties — those are authored per mark, not
theme-level.

## Behaviour

- Marks **draw on** when the component renders (`.am-run`). At rest a mark is fully drawn,
  so it still reads if motion never plays.
- **Reduced motion** (`prefers-reduced-motion`, `.no-motion`, `[data-tm-no-motion]`) stops
  the draw-on and shows the finished mark.
- **Offline / SCORM-safe:** marks are self-contained SVG + CSS. The handwriting faces
  (`Caveat`, `Kalam`) are *not* loaded from Google here — they fall back to a system cursive;
  self-host a subset if you need the exact faces offline.

## Layout

```
less/grow-animations.less   the base marks stylesheet (generated from the engine, tokenised)
js/animation-catalog.js     the 58 marks (pure data)
js/engine.js                markup + CSS generation (shared with the standalone tool)
js/AnimationsView.js        the component view (renders authored marks, injects #ink)
templates/growAnimations.jsx
properties.schema  example.json  bower.json
```

## Context packs

The same marks power **context packs** — stepped, animated *process* walkthroughs (marking &
feedback, source evaluation, referencing, critical analysis…). A pack is data: a `statement`,
a `stage` marked up one move at a time, ordered `steps`, and `feedForward`. The 25 finished
packs live as content in
[`adapt-grow-content/adapt-grow-animations/`](../../adapt-grow-content/adapt-grow-animations/);
the schema, the authoring **SKILL** and a blank template per stage type live in
[`adapt-content-templates/adapt-grow-animations/context-packs/`](../../adapt-content-templates/adapt-grow-animations/context-packs/).
A stepped **pack-player** view (like the scenario player) is the planned way to render them;
the marks already come from this component's engine.

GPL-3.0. Lineage: `inbox/abbott-tools/{animation-manager, context-packs}`; source of record
(tool CSS, engine, the context-pack renderer + authoring prompt) preserved in
`adapt-docs/adapt_abbdev/components/adapt-grow-animations/source/`.
