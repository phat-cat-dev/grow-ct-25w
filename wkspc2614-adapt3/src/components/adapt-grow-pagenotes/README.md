# adapt-grow-pagenotes

A button that opens a **transparent, full-page overlay of hand-drawn animated notes**
over an article, block or component. The content stays visible beneath; the notes
**draw themselves on** at authored positions. Author-authored presentation (not graded).

Two note vocabularies, both reusing the existing GROW draw-on engines:

- **ink marks** — the 58 marks of [`adapt-grow-animations`](../adapt-grow-animations/)
  (`_type: "mark"`, `_markId`), via the bundled `engine.instanceMarkup`.
- **chalk diagrams** — the [`chalk-patterns`](../../adapt-content-templates/adapt-grow-animations/chalk-patterns/)
  library (`_type: "chalk"`, `_pattern` + slot `data`), via the bundled `ChalkLabels.render`.

## Authoring

```json
{
  "_component": "growPageNotes",
  "_launch": { "_icon": "edit_note", "text": "Show the notes" },
  "_overlay": { "_reveal": "stepped", "_scrim": "faint" },
  "_notes": [
    { "_type": "mark", "_markId": "underline", "text": "the central claim", "_color": "accent", "x": 24, "y": 20, "step": 1 },
    { "_type": "mark", "_markId": "circle", "text": "no source", "_color": "negative", "_repeats": 2, "x": 70, "y": 30, "step": 2 },
    { "_type": "chalk", "_pattern": "fork-connector", "_color": "neutral", "x": 40, "y": 64, "step": 3,
      "data": { "source": { "label": "one study" }, "branch1": { "label": "measured output" }, "branch2": { "label": "self-report" } } }
  ]
}
```

- `x` / `y` are **percentages of the target region's box** (resilient to resize).
- `step` groups the sequential reveal (`_overlay._reveal: "stepped"`); `"all"` draws them together.
- `_targetId` picks the region to cover (an `_id`); blank = the component's own article.
- `_color` is a theme **role** (`accent/positive/negative/neutral/comment/pen/ink`), never a hue.
- `_launch._icon` is a Material Symbols Outlined name; the launch button is a bordered GROW
  icon-button on the `--ib-*` token contract (icon-manager-ready).

## Behaviour & accessibility

The overlay is a `position: fixed` transparent layer matched to the target's box; it is
click-through (`pointer-events: none`) except the notes and the Next/Close controls, so the
page stays usable (`role="group"`, `aria-modal="false"` — an overlay, not a modal). Focus
moves to a control on open, **Escape** closes, focus returns to the launch button. It
repositions on resize/scroll. Under `prefers-reduced-motion` the notes show finished, with no
draw-on.

## Notes

- The ink-mark CSS (`am-*`) and the chalk CSS (`edu-*`/`chalk-*`) are injected once at runtime
  by `js/overlay.js` (the Adapt LESS build only globs `*.less`); the raw source is kept in
  `_vendor-css/` for reference.
- The marks engine (`js/libs/engine.js` + `animation-catalog.js`) and the chalk runtime
  (`js/libs/chalk-labels.js` + `chalk-pattern-data.js`, converted from UMD to ES modules) are
  **vendored copies**. A shared `adapt-grow-marks` engine and icon consolidation are deferred.

GPL-3.0.
