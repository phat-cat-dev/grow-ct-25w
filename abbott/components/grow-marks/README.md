# grow-marks

A shared, framework-agnostic library of **ink marks**: hand-drawn SVG marks and
bullets that **draw on** (stroke) or **pop in** (fill), on cue, respecting
reduced motion. Built from the studies
`tool-theming/elearning-assets/gallery/marks.html` and `bullets.html` — the
artwork is theirs; this packages it as a reusable engine.

This is the **backbone** for two planned Adapt plugins:

- **adapt-grow-annotate** (a component) — a passage where the learner tags /
  labels / circles words and the mark animates.
- **adapt-grow-marks** (an extension) — author-tagged words draw on as the
  learner reads, and a question's right/wrong plays a mark on a target.

Both import this library rather than re-implementing the marks. It is *not* an
Adapt plugin itself — it is the core they share.

## What's in it

```
grow-marks/
├─ src/
│  ├─ marksCatalogue.js   the mark artwork, as data (42 marks + a badge generator)
│  ├─ marksLogic.js       pure helpers: build SVG markup, resolve colour/speed (tested)
│  └─ growMarks.js        the DOM engine: ensureMarkDefs, drawMark, playMark, playWithin
├─ grow-marks.css         styles + keyframes (plain CSS; port to LESS inside a plugin)
├─ demo/index.html        browser demo — catalogue + the two use-cases
├─ test/marks.test.js     unit tests (node:test) — 24, all passing
└─ package.json           {"type":"module"}
```

## Two primitives, one catalogue

| Kind | Animation | Examples |
|---|---|---|
| `ink` | a stroked outline **draws on** (`stroke-dashoffset`) | underline, oval, box, bracket, strike, tick, cross, arrow, ring, diamond, toggle |
| `pop` | a filled shape **pops in** (scale) | dot, disc, square-fill, play ▸, heart, numbered badges |

Plus `knob` (the toggle's sliding dot) and badge text. Marks fall into
categories — **emphasis** (word-wrappers), **glyph** (ticks/arrows/feedback),
**bullet** (list markers), **state** (radio/checkbox/toggle/pin/tag), and
on-demand **badges** (1–20, A–Z via `makeBadge`).

Each mark also has a `kind` that drives placement: `wrap` (overlay on a word),
`inline` (an em-sized SVG dropped in), or `highlight` (a CSS marker sweep).

## Using it

```js
import { playMark, drawMark, playWithin, makeBadge } from './src/growMarks.js';

// Circle a word in green (plays immediately):
playMark(wordEl, { mark: 'oval', color: 'positive' });

// Insert a bullet without playing yet, then play on cue:
const h = drawMark(liMarkerEl, { mark: 'check-ring', autoplay: false });
h.play();          // h.replay() re-runs it; h.remove() tears it down

// Draw a numbered badge:
playMark(slotEl, { mark: makeBadge('3') });

// Draw every author-tagged word under a root (reads data-gm-* attributes):
playWithin(document.querySelector('.passage'));
//   <span data-gm-mark="underline" data-gm-color="accent">matters</span>
```

Options: `mark` (catalogue id or a definition object), `color`
(`accent | positive | negative | neutral | comment | soft`), `speed`
(0.4–2.5, default 1), `hold` (keep the mark after it draws, default true),
`autoplay` (default true), and `variant` (highlight only).

## Theming

The CSS reads GROW theme tokens first — `--accent`, `--ink-soft`,
`--surface-2`, `--c-positive/-negative/-neutral/-comment` — and falls back to
its own values, so marks retint with the active theme and dark mode. The colour
roles map straight onto those tokens.

The engine injects one shared `#gm-ink` turbulence filter (`ensureMarkDefs()`,
called automatically on first draw). The host loads `grow-marks.css` once; an
Adapt plugin ports it to LESS. Everything is namespaced `gm-*` to avoid
clashing inside a large build.

## Viewing the demo

The demo uses native ES modules, so serve the folder (module imports don't work
over `file://`):

```bash
npx serve abbott/components/grow-marks     # then open /demo/
# or VS Code "Live Server" on demo/index.html
```

It shows the full catalogue, marking a chosen word, and right/wrong feedback.

## Developing

```bash
node --test test/marks.test.js     # pure catalogue + logic
```

The DOM engine (`growMarks.js`) is exercised in the demo. Relative imports use
explicit `.js` extensions so the library runs unbundled in the browser and in
Node, as well as through the Adapt/Rollup bundler.

## Next

When wiring into Adapt, each plugin can **vendor** this `src/` + the LESS port
(Adapt plugins are self-contained), or we keep one copy here and import it at
build time — a decision for when adapt-grow-annotate / adapt-grow-marks are
built. See the component/extension notes in the project memory.
