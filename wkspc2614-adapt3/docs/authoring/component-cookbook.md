# Component cookbook

One build-tested working instance of every interactive component lives in
`courses/_component-gallery/` (16 components, **one component per page** so each
can be viewed and tested in isolation from the boxMenu). That course is the
**canonical reference**: to add an activity to a lesson, copy the matching
component object from `courses/_component-gallery/en/components.json`, re-id it
(`_id`/`_parentId`), and adapt its content. Every config there compiles under
`grunt build` and renders without console error (verified 2026-10-23).

Known polish items (grow-ct theme styling pass, TODO d): the `modal` trigger
button is unstyled because its `.cm.btn` styling lives in `adapt-ab-theme`, which
the grow-ct build excludes; the `ab-carousel` prev/next controls slightly overlap
slide text. Both are theme-CSS, not component-logic, issues.

The leading underscore is deliberate: it is build/reference infrastructure, not
a learner-facing course, so `tools/verify-all-courses.js` (the A80 build gate)
skips it — the same leading-underscore exclusion it uses for `_generated` — and
the gate stays green even though the gallery has no pedagogical gate manifest.

Build-test the gallery any time by pointing the `src/course` junction at
`courses/_component-gallery` and running the Adapt build chain **without**
`verify-all-courses` (it is a technical harness, not a pedagogical course, so it
has no gate manifest):

```
npx grunt check-json check-plugins clean:output build-config tracking-insert \
  copy scripts:adaptpostcopy schema-defaults language-data-manifests handlebars \
  javascript:compile clean:dist less:compile replace scripts:adaptpostbuild \
  clean:temp minify
```

## Palette → activity fit

Each component has its own page in `_component-gallery` (open it from the
boxMenu). Copy the matching object from `en/components.json` by its `_component`.

| `_component` | kind | Use as the main activity for… |
|---|---|---|
| `ab-card` | present | a small set of parallel practices/points (static cards) |
| `flipcard` | interact | front prompt / back answer; `_items[].front.title`, `.back.body` |
| `ab-carousel` | present | a walk-through of sequential items |
| `gowTimeline` | present | change over time / a process in stages — set `_reveal: true` to make each step click-to-reveal |
| `callout` | present | a single short aside (tip/note/definition) |
| `keyTerm` | present | one term — set `_reveal: true` for flashcard mode (reveal definition → example → related on each click) |
| `quoteBlock` | present | a sourced quotation with context |
| `statBlock` | present | 2–4 headline figures |
| `annotate` | interact | mark up a passage (reader-as-editor) |
| `scrollScenes` | present | a scroll-driven narrative/stepped reveal |
| `glossary` | present | a set of terms to browse |
| `modal` | interact | reveal detail behind triggers |
| `textTagging` | question | classify words/phrases in a passage; per-span `feedback` + `_feedback` for right/wrong |
| `matching` | question | pair items across two sets; each option needs `_isCorrect` |
| `sortable` | question | order items correctly |
| `slider` | question | judge a value on a scale |
| `branching` | interact | choose-your-path scenario (single consequence per choice; multi-step not yet supported) |

`accordion`/`ab-accordion`, `tabs`, `mcq`, `confidence`, `checklist`,
`opentext`, `references`, `text` remain available and are already proven in the
gate-authored courses.

**Reveal flags:** `gowTimeline` and `keyTerm` default to showing everything at
once; set `_reveal: true` (schema-documented) to turn them into click-to-reveal
interactions, as the gallery does.

## Gotchas discovered building the gallery (all fixed on base)

- **Every component must call `setReadyStatus()` itself.** `ComponentView.postRender()`
  is a no-op and `AdaptView` does not auto-signal ready for leaf components, so a
  component that never calls `this.setReadyStatus()` leaves its page model
  `_isReady: false` forever — `contentObjectView:ready` never fires and the
  loading curtain never lifts (Adapt force-readies after a 10s timeout with a
  console error, so the symptom is a 10-second blank-grey load). All six
  `adapt-gow-*` components shipped without the call; now fixed (display ones get
  `postRender() { this.setReadyStatus(); this.setupInviewCompletion('.component__inner'); }`,
  `textTagging` calls it in `onQuestionRendered()`).
- **A component's template file must be named after its registered `_component`.**
  `adapt-gow-timeline` registers as `gowTimeline` but shipped `timeline.hbs`, so
  `Handlebars.templates['gowTimeline']` was undefined → `template is not a function`.
  Renamed to `gowTimeline.hbs`.
- **`.hbs` question components mount buttons via `<div class="btn__container"></div>`,
  not `{{> buttons}}`.** `QuestionView.addButtonsView()` renders `ButtonsView` into
  `.btn__container`; feedback shows via the notify popup, not a template partial.
  `textTagging.hbs` used `{{> buttons}}`/`{{> feedback}}` (unregistered partials)
  → "The partial buttons could not be found". The official question components use
  `.jsx` templates with a `btn__container` div.

See [grow-course-authoring-recipe](../../../memory) notes for the full pipeline.
