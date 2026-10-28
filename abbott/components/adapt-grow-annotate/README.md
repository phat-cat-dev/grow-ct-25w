# adapt-grow-annotate

A passage the learner **marks up with hand-drawn ink** — circle the key idea,
underline evidence, flag what they're unsure of. Reflective, not graded. Built
on the shared [grow-marks](../grow-marks/) engine.

The author chooses which words are annotatable and offers a small palette of
annotation "tools"; the learner picks a tool and clicks words to mark them, and
each mark draws on. This is the self-contained version of the idea — the
companion **adapt-grow-marks extension** handles marking across other
components (author-tagged spans + question right/wrong).

## How authoring works

The passage is plain text with annotatable words wrapped in double brackets:

```
"A landscape needs a [[foreground]], a [[middle ground]] and a [[backdrop|bd]]."
```

`[[word]]` becomes a clickable target; add a stable key with a pipe
(`[[word|bd]]`) if you reuse a word or want a fixed id. Surrounding text may
contain inline HTML.

Tools are the palette (`_tools`): each is a label + an ink mark + a colour.

```json
"_tools": [
  { "_id": "idea",     "label": "Main idea", "_mark": "oval",      "_color": "accent" },
  { "_id": "evidence", "label": "Evidence",  "_mark": "underline", "_color": "positive" },
  { "_id": "doubt",    "label": "Not sure",  "_mark": "question",  "_color": "neutral" }
]
```

With a single tool the component is a simple circle-the-word toggle (and if you
provide none, a default "Circle" tool is used). `example.json` is a complete
component block.

Other settings: `_minAnnotations` (how many marks before it counts complete; 0
= complete on view), `_showLabels` (label chip next to marked words),
`_allowReset` (a clear button).

Marks available to `_mark`: the word-wrappers `oval`, `box`, `bracket`,
`underline`, `double`, `wavy`, `strike`, `scribble`, `highlight`, and the
beside-the-word glyphs `tick`, `cross`, `star`, `caret`, `checkbox`,
`question`, `exclaim`. Colours: `accent`, `positive`, `negative`, `neutral`,
`comment`, `soft` (mapped to the theme).

## How it works

- `js/annotateLogic.js` — pure: parses the passage into segments, holds the
  `targetKey -> toolId` state (apply/toggle), completion predicate, and
  (de)serialisation. **19 unit tests, all passing.**
- `js/AnnotateModel.js` — `ComponentModel` subclass; parses the passage in
  `init`, records annotations, completes at `_minAnnotations`.
- `js/AnnotateView.js` — renders the JSX shell once, then wires the palette and
  targets **imperatively** and drives grow-marks. There is no React re-render
  after mount, so the appended mark SVGs are never discarded (same discipline
  as scroll-scenes).
- `templates/annotate.jsx` — the static shell (palette + passage + footer).
- `less/annotate.less` + `less/grow-marks.less` — component styles plus the
  vendored mark styles.
- `js/libs/` — the vendored grow-marks core (`growMarks.js`, `marksLogic.js`,
  `marksCatalogue.js`).

### Accessibility
Each target is a real `<button>` with `aria-pressed`; the palette is a
`role="toolbar"`; changes are announced through a polite live region; marks
respect reduced motion (shown complete, no animation). Native scrolling/reading
is unaffected.

## Vendored library

`js/libs/` and `less/grow-marks.less` are copied from
`abbott/components/grow-marks` so this plugin is self-contained (Adapt plugins
can't import across plugin folders). If the library changes, re-copy:

```bash
cp ../grow-marks/src/*.js            js/libs/
cp ../grow-marks/grow-marks.css      less/grow-marks.less
```

## Known limitation (v1)

Completion persists through Adapt's normal state (it's a trackable). The
**annotations themselves** are written to `_userAnswer` and restored on
re-render, but persisting them into LMS suspend data across a full reload needs
them wired into the model's serialised state / `offlineStorage` — a small
follow-up. The interaction, marks, labels, completion and reset all work now.

## Developing

```bash
node --test test/annotateLogic.test.js
```

The view/engine are exercised visually once built. To preview the look of the
marks without a build, open the grow-marks demo (`../grow-marks/demo/`).

## Installing into the GROW build

Copy the folder to `wkspc2614-adapt3/src/components/adapt-grow-annotate/`, add a
component block (see `example.json`) to a block's `components.json`, then
`npx grunt build`. Component type `annotate`, attribute `_annotate`.
