# adapt-grow-marks

An **extension** that draws hand-drawn ink marks on content in *any* component,
using the shared [grow-marks](../grow-marks/) engine. It's the cross-component
companion to the self-contained [adapt-grow-annotate](../adapt-grow-annotate/)
component.

An extension (unlike a component) isn't placed on the page — it switches on
globally and reaches into existing content. This one does two things:

### 1. Author-tagged words draw on (zero-config)

Mark words in *any* text field with a `data-gm-mark` span; they draw on when
scrolled into view:

```html
A landscape needs a <span data-gm-mark="underline" data-gm-color="accent">foreground</span>
and a <span data-gm-mark="oval">backdrop</span>, and depth is a
<span data-gm-mark="highlight" data-gm-color="neutral">choice</span>.
```

Attributes (from the grow-marks dataset convention): `data-gm-mark` (required —
any catalogue id: `oval`, `underline`, `box`, `highlight`, `tick`, `star`, …),
`data-gm-color` (`accent | positive | negative | neutral | comment | soft`),
`data-gm-speed`, `data-gm-hold`. On wherever such a span appears; nothing to
configure.

### 2. Question right / wrong (opt-in)

When a question is answered, play a mark on it — a tick for correct, a cross for
wrong by default. Opt-in per question so it never fights the question's own
feedback:

```json
"_growMarks": {
  "_feedback": {
    "_isEnabled": true,
    "_correct":   { "_mark": "tick",  "_color": "positive" },
    "_incorrect": { "_mark": "cross", "_color": "negative" },
    "_target": ""
  }
}
```

By default the mark lands on a `[data-gm-feedback]` element if present, else the
question title. Set `_target` to a CSS selector inside the component (e.g. an
author-tagged word) to put it somewhere specific.

## Enable / disable

On by default. Turn off for a whole course in `course.json`:

```json
"_growMarks": { "_isEnabled": false }
```

Or per component with the same attribute (`"_growMarks": { "_isEnabled": false }`).

## Scope (deliberate)

It marks **author-tagged targets** and **reacts to question state**. It does
*not* try to pick an arbitrary word inside a foreign component at runtime — that
is fragile and breaks when components change. Tag the word, or target it with a
selector. (This is the "80%" boundary agreed during design; the fully-dynamic
word-picking idea was set aside.)

## How it works

- `js/marksExtensionLogic.js` — pure: global/feedback enablement and the
  correct/incorrect mark resolution. **8 unit tests, all passing.**
- `js/adapt-grow-marks.js` — the extension. On `pageView:ready` it collects
  `[data-gm-mark]` spans and plays each via an `IntersectionObserver` when it
  enters the viewport (draws immediately under reduced motion / no observer).
  On `questionView:showFeedback` it plays the resolved feedback mark. It tidies
  up on `router:location`.
- `schema/course.schema.json`, `schema/component.schema.json` — authoring.
- `less/grow-marks.less` (vendored) + `less/marks-ext.less`.
- `js/libs/` — the vendored grow-marks core.

Accessibility: marks are decorative (`aria-hidden`), so they add nothing a
screen reader must read; question feedback meaning still comes from the
question's own tutor text. Reduced motion shows finished marks without
animation.

## Vendored library

`js/libs/` and `less/grow-marks.less` are copied from
`abbott/components/grow-marks` (Adapt plugins are self-contained). Re-sync with:

```bash
cp ../grow-marks/src/*.js       js/libs/
cp ../grow-marks/grow-marks.css less/grow-marks.less
```

If adapt-grow-annotate is also installed, both vendor the same `.gm-*` CSS —
harmless duplicate rules; a later consolidation could let one own it.

## Developing

```bash
node --test test/marksExtensionLogic.test.js
```

## Installing into the GROW build

Copy to `wkspc2614-adapt3/src/extensions/adapt-grow-marks/`, run
`npm run adapt-install` (so the framework registers the extension), then
`npx grunt build`. Add `_growMarks` where you want it (see `example.json`);
author `data-gm-mark` spans directly in text fields.
