# incoming-components/ — staging space for new Adapt plugins

Drop raw HTML, CSS, JS (prototypes, exports from somewhere else, hand-built
demos — whatever form they're in) in here when you want something turned into
a real Adapt component or extension. Everything in this folder except this
README is gitignored — nothing here is ever committed as-is. It's a staging
area, not the destination.

## Before you drop anything in

Check `docs/authoring/component-candidates-register.md` first. It tracks
every component this programme has ever evaluated — adopted, built-own,
rejected (with reason), or still just an idea. If what you want already has
an entry there, that decision (and the reason) already exists; don't
re-litigate it here. If it's genuinely new, it belongs as a new row in that
register once evaluated, following the register's own adoption ladder: core
Adapt component first, then a compatible community plugin, build-own only
when nothing fits and the need actually recurs.

## What to drop in

Anything that shows the interaction you want: a static HTML mockup, a CodePen
export, a JS prototype, a screenshot plus a description — no fixed format.
One subfolder per candidate component keeps multiple drops from colliding,
e.g.:

```
incoming-components/
  word-count-meter/
    mockup.html
    behaviour.js
    notes.md
  peer-review-widget/
    ...
```

## What happens next (conversion path)

A real Adapt component is not a copy-paste of the HTML/JS — it's a rebuild
into this repo's plugin shape. The canonical structural model already in
this repo is `src/components/adapt-abbott-flipcard/`:

```
src/components/adapt-<prefix>-<name>/
  bower.json          # name, component/extension id, targetAttribute,
                       # displayName, framework version, main entry
  properties.schema    # JSON Schema (draft-04) of authorable fields —
                       # drives the authoring UI and validation
  js/
    <Name>Model.js
    <Name>View.js
    <name>Logic.js     # pure logic, independently unit-testable
    adapt-<prefix>-<name>.js   # registers the component with Adapt
  templates/
    <name>.jsx          # React template — must be named after the
                         # registered component id exactly (see gotcha below)
  less/
    <name>.less
  test/
```

Before building, read:

- `docs/authoring/component-cookbook.md` — the three gotchas every custom
  component here has hit: every component must call `setReadyStatus()`
  itself; the template filename must match the registered `_component`
  name exactly (`gowTimeline.hbs`, not `timeline.hbs`); `.hbs`-based question
  components mount their buttons via a `btn__container` div, not a
  `{{> buttons}}` partial.
- `docs/authoring/component-candidates-register.md` — the adoption workflow
  and the compatibility/schema/pedagogical-fit gate every candidate must
  pass, in that order, before it's built.
- An existing component close to what you want, as a worked model — e.g.
  `adapt-abbott-checklist` for a tick-list interaction, `adapt-abbott-modal`
  for an on-demand disclosure, `adapt-abbott-branching` for a decision/
  consequence interaction.

Once built: run it through `courses/_component-gallery` (the one-component-
per-page reference course used to build-test every custom component so far),
record the outcome in `component-candidates-register.md`, and only then is
it "installed" in the sense the rest of this repo's tooling
(`tools/component-map.js`, `design-kb/design-kb.palette.json`) expects.

## What this is not

Not a place for finished plugins — those live in `src/components/` or
`src/extensions/` and are tracked in git. Not a way to skip the register's
compatibility/schema/pedagogical-fit gate. Not a build input — nothing here
is read by `grunt build` or `tools/check-build-target.js`.
