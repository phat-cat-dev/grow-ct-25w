# adapt-grow-phasenotes — GROW Phase notes

Extension specification for the trickle-phase note overlay: hand-drawn
annotation "notes" authored per article, drawn onto the shared GROW overlay,
revealed in step with `adapt-contrib-trickle` via a mirror continue button,
with a top-nav button + popup menu to hide/show notes and switch between
per-article sets.

**Grounded in:** `src/extensions/adapt-grow-phasenotes/` (the defining
extension); consumes `adapt-grow-layer` (host region) and
`adapt-contrib-trickle` (the button it mirrors); imports its drawing engines
directly from `src/components/adapt-grow-pagenotes/js/libs/`, which it does
**not** modify.

---

## 1. What it is

A **runtime, DOM-level Adapt extension** (`extension: "growPhaseNotes"`,
`targetAttribute: "_growPhaseNotes"`). Authoring is article-level
(`_growPhaseNotes._notes[]`); there is no `templates/` and nothing is placed
in `blocks.json`/`components.json` — DOM-only, like every other `grow-*`
extension.

A **set** is one authored article: its `_id` is the set id, its (optional)
`label` or its own title is the set label shown in the nav menu's switcher.
Nothing hard-codes a count of sets per page or steps per set.

A page with no `_growPhaseNotes` authored on any article is a complete
no-op — no nav button, no overlay nodes, trickle untouched.

---

## 2. Authoring model

```jsonc
// articles.json
{
  "_id": "L01-a-02",
  "_growPhaseNotes": {
    "_isEnabled": true,
    "label": "",                 // optional; defaults to the article's own title
    "_notes": [
      { "_type": "mark", "_markId": "circle", "text": "the claim",
        "_color": "accent", "x": 30, "y": 22, "step": 0 },
      { "_type": "chalk", "_pattern": "curved-arrow", "_targetId": "L01-b-30",
        "_color": "comment", "x": 68, "y": 55, "step": 1,
        "data": { "source": { "label": "claim" } } }
    ]
  }
}
```

Per-note `_targetId` (optional) pins a note to a block/component `_id`
within the article rather than the whole article; `set.mount()`
(`notesLayer.js`) resolves it via `articleEl.querySelector('[data-adapt-id="…"]')`
and groups notes by resolved target into separate **regions**, each with its
own position-tracking root. A blank `_targetId` groups under the
whole-article region.

Config-level settings (`config.json` → `_growPhaseNotes`):

| Key | Default | Purpose |
|---|---|---|
| `_isEnabled` | `true` | Master switch. `false` disables harvesting, the mirror scan and the nav button entirely. |
| `_icon` | `ink_pen` | Material Symbols Outlined name for the top-nav toggle button. |
| `_revealText` | `Reveal notes` | Mirror button label while the article it sits over still has steps to reveal. |
| `_continueText` | `Continue` | Mirror button label on the final step, matching the real trickle button's own text. |

A course-level aria label for each note region is read from
`_globals._extensions._growPhaseNotes.ariaRegion` (the authoring-tool
convention for extension-contributed globals — confirmed against
`adapt-contrib-trickle`'s own `incompleteContent`/`additionalContentLoaded`,
both declared as bare keys in `properties.schema` and read at runtime nested
under `_extensions._trickle`), falling back to a hardcoded string
(`adapt-grow-phasenotes.js` — `DEFAULT_ARIA_REGION`) if absent.

Rejected: harvesting `growPageNotes` component instances (couples two
plugins, and it is authored in zero courses — nothing to harvest);
config.json-level notes (cannot address per-article sets).

---

## 3. Trickle-phase binding — `view:childAdded`

Trickled-away children are **genuinely absent from the DOM**, not hidden:
`TrickleController.onAddChildView` calls `event.stop()`
(`adapt-contrib-trickle/js/controller.js:95`), so
`src/core/js/views/adaptView.js:253-258` breaks before `new ChildView` at
`:271`. There is no element to observe, so MutationObserver and
`change:_isHidden` are both categorically wrong.

Verified signal: `Adapt.trigger('${type}View:childAdded view:childAdded', this, childView)`
at `adaptView.js:315`, fired immediately after `this.$el.append(childView.$el)`
(`:307`).

```js
Adapt.on('contentObjectView:preRender', this.reset);
Adapt.on('view:childAdded', this.onChildAdded);          // adaptView.js:315
Adapt.on('trickle:finished trickle:killed', this.sync);  // catch-all
Adapt.on('pageView:ready menuView:ready', this.onPageReady);
```

`onChildAdded` filters on `_type` in `{article, block}`, dedupes by `_id`
(renderTo and `trickle:kill` can re-enter), then awaits
`childView.whenReady()` (`adaptView.js:365`) before measuring, so the box is
final before a region is built against it.

This needs zero knowledge of trickle and therefore needs no separate
fallback: the same event fires on non-trickled pages, on forced `renderTo`
renders, and after `trickle:kill`. A set with no mirror button reveals all
its steps on eligibility (`onArticleEligible` → `set.revealAll()`), so notes
on a page with no trickle gate simply appear with the content.

Rejected, one line each:

- `change:_isLocked` — `applyLocks()` runs *before* `addChildren()`
  (`controller.js:117-118`), a pre-reveal signal; also a cooperative lock
  *count* (`lockingModel.js:96-102`) another plugin's lock can silently
  suppress.
- `change:_isRendered` — set at `adaptView.js:262`, before the view is
  constructed and attached.
- `view:addChild` (`adaptView.js:409`) — fires before the view exists and is
  cancellable; trickle itself cancels it.
- `trickle:started` (`controller.js:82`) — once per page, no per-phase
  information, never fires on a page without trickle.
- `pageView:ready` alone — guarded by `_isTriggeredReady`
  (`contentObjectView.js:111-112`), fires at most once and is **not**
  re-fired after a continue. Used here only for the bulk harvest + sweep of
  content already in the DOM before `view:childAdded` attached.

---

## 4. The mirror button

Created **only** where a real, visible trickle button exists for an article
*and* that article has unrevealed steps.

| Pattern | Real button | Mirror | Notes revealed by |
|---|---|---|---|
| Block-level trickle gate, button shown | yes | yes | mirror click, then proxy |
| Article `_onChildren` gate, no visible button (`_button._isEnabled:false`) | no | no | article eligibility, all steps at once |
| Article `_onChildren` gate, button shown | yes, per block | yes | mirror click, then proxy |
| No trickle at all (wrapper pages) | no | no | article eligibility, all steps at once |

**Locate**: `document.querySelectorAll('.trickle .js-trickle-btn')`
(`mirrorButton.js` → `scan()`), filtered through `isRealButtonUsable()` —
container not carrying `u-display-none` (`TrickleButtonView.js:132`), button
not carrying `aria-disabled="true"` or `is-disabled`
(`a11y.js:toggleEnabled`). Owner article via
`btn.closest('.article[data-adapt-id]')` — `data-adapt-id` is set on every
content view by `AdaptView.attributes()` (`adaptView.js:48-53`).

**Owner article semantics**: the mirror drives the *same* article the real
button lives in — its own `_growPhaseNotes` set, not a different article the
button happens to gate. This only produces a visible step-by-step rhythm
when an article's own `_trickle` block gates its own later content (pattern
row 1 and row 3 above); authoring additional `_trickle` gates to get that
rhythm on a page that currently has only one gate is a course-data change,
out of this extension's scope.

**Stay in sync**: `TrickleButtonView.render()` runs once, in
`initialize()` (`:40`); later state changes go through
`updateButtonState()` (`:129-153`), and `a11y.toggleEnabled` touches only
`aria-disabled`/`is-disabled` (`a11y.js:496-506`) — so this extension's own
suppression attributes (`tabindex="-1"`, `aria-hidden="true"`, class
`is-grow-mirrored`) survive. Belt and braces anyway
(`mirrorButton.js` → `trackRect()`): `ResizeObserver` on the real button, a
`MutationObserver` on the `.trickle` root, rAF-coalesced `window`
resize/scroll in capture phase.

**Replace, do not sit alongside**: suppress with `visibility: hidden`,
never `display: none` (`display: none` would collapse the rect the mirror
positions against). Click handling
(`mirrorButton.js` → `buildMirror()`'s `onClick`):

```js
function onClick() {
  if (set.advance()) {                 // reveal next step, stay put
    growPhaseNotes.sync();
    relabel(mirror, set);              // last step -> config._continueText
    return;
  }
  teardown({ restore: true });         // restore BEFORE the click
  realBtn.click();                     // core trickle continues and scrolls
}
```

`pointer-events: auto` is mandatory — `growLayer.overlay()` is
`pointer-events: none`. Focus is not stolen mid-read: the mirror only takes
focus on build if `document.activeElement === realBtn`, and only hands focus
back on the final click if it was on the mirror. Reveals are announced via a
polite live region (`growPhaseNotes.announce()`).

**Scan timing**: `Adapt.on('pageView:ready', scan)` is registered
**synchronously**, not rAF-deferred. This deliberately wins a race against
the controller's own eligibility decision — `onArticleEligible()` defers its
"reveal everything unless mirrored" check by one animation frame
specifically so this scan, which runs synchronously within the same
`pageView:ready` dispatch, gets first claim via `claimMirror()`.

**Known limitation**: the mirror lives in `#grow-layer`, at the end of
`<body>`, so there is still exactly one tab stop in the trickle gate's place
but it falls at the end of the document tab order rather than inline.
Documented rather than fixed — the escape hatch, if a11y testing rejects it,
is a capture-phase click interceptor on the real button instead.

---

## 5. Note rendering (`notesLayer.js`)

Imports the pagenotes drawing engines **in place**, via a single re-export
(`js/engines.js`), rather than duplicating ~960 lines of mark/chalk
rendering logic:

```js
export { instanceMarkup, baseCss, INK_FILTER_SVG } from 'components/adapt-grow-pagenotes/js/libs/engine';
export { default as ChalkLabels } from 'components/adapt-grow-pagenotes/js/libs/chalk-labels';
export { default as chalkCss } from 'components/adapt-grow-pagenotes/js/libs/chalk-css';
```

Legal and precedented: the RequireJS/rollup resolver resolves any bare
specifier against `baseUrl` (= `src/`); `adapt-contrib-gmcq/js/GmcqView.js`
already imports `components/adapt-contrib-mcq/js/McqView`, and
`adapt-grow-pagenotes/js/overlay.js` already imports the `adapt-grow-layer`
extension the other direction. Verified bundled: `grunt build` then
`grep -o "grow-phasenotes[A-Za-z_:-]*" build/adapt/js/adapt.min.js | sort -u`
returns strings sourced from this extension's own modules, confirming the
cross-plugin import resolved rather than silently failing.

**Shared asset guards**: `injectAssetsOnce()` reuses the *same* DOM ids
`overlay.js` uses (`grow-pagenotes-marks-css`, `grow-pagenotes-chalk-css`,
`am-ink`) rather than inventing new ones — a second, differently-id'd
injection would duplicate the unscoped `.am-*` stylesheet and the `am-ink`
SVG filter, making `filter: url(#am-ink)` resolve by document order instead
of correctly.

**State model** (one `Set` per authored article, from `createSet()`):

```
Set
  articleId, label, steps[]       // sorted unique authored step values
  revealedUpTo  = -1              // index into steps
  eligible      = false
  regions: Map<targetId, { targetEl, root, notes[], ro }>
```

One `applyVisibility()` pass per set:

```
isRevealed = set.eligible && set.steps.indexOf(note.step) <= set.revealedUpTo
isVisible  = isRevealed && globalVisible
             && (activeSetId === 'all' || activeSetId === set.articleId)
```

- Notes are **built once and stay in the DOM**; visibility toggles
  `is-visible`/`[hidden]`, never destroy-and-rebuild.
- `revealedUpTo` is **never lowered** by the hide toggle, so "show notes"
  restores exactly what trickle had revealed and nothing more.
- Draw animation plays only on the `false → true` transition, gated by a
  per-note `hasPlayed` flag — `instanceMarkup(note, { play: false })` builds
  static markup; `classList.add('am-run')` (marks) or `ChalkLabels.play()`
  (chalk) runs once, on first reveal.
- `revealedUpTo` is runtime-only per page; it does not attempt to track
  `_isLockedOnRevisit` — that is trickle's own re-lock behaviour and the two
  would fight if this extension tried to persist it.

---

## 6. Nav button and menu (`navMenu.js`)

`growLayer.navMount('phasenotes', mount)` — id free among existing
consumers (`mode`, `pagenav`, `journal`, `grow-studio`). `data-order="93"`,
consumed by `navigationView.js`'s nav-chrome sort — free among existing
orders (`-100`, `0`, `94` journal, `95` mode, `100` drawer).

One `menuitemcheckbox` for Show/Hide, not two items — "Hide all" and "Show
all revealed" are the two states of one binary, matching grow-mode's
Animations/Backgrounds idiom: the label stays constant; `aria-checked` and
an `is-off` class carry the state.

**Rebuild per page, not mount-once**: unlike `adapt-grow-mode`'s
`mount()`, which early-returns if its own marker is already present, this
extension's set list is page-specific, so `mount()` unconditionally removes
any existing `.grow-phasenotes` wrapper and rebuilds — returning early
**without appending** when the page has no authored notes, so the button is
simply absent rather than disabled.

**Ordering fix (explicit call, not reliance on `navMount`'s own rerun)**:
`adapt-grow-layer`'s own `Adapt.on('pageView:ready menuView:ready', this._runNav)`
is registered at `GrowLayer`'s construction time — ahead of this
extension's own `pageView:ready` handler, which is registered inside its
`Adapt.once('app:dataReady', …)` callback. On the very first page, growLayer's
rerun would otherwise fire `navMenu.mount()` *before* this extension's
`harvest()` has populated `this.sets`, so the nav button would silently fail
to appear even on a page with authored notes. Fixed by having the
controller's own `onPageReady()` call `navMenu.mount()` directly, straight
after `harvest()`, rather than relying on `navMount`'s registration-time/
rerun timing for this correctness-critical path. `growLayer.navMount()` is
still registered, both for its idempotent-lookup boilerplate and because its
timing is harmless on `menuView:ready` (menu pages have no articles to
harvest, so an empty set list is always correct there).

a11y: `aria-expanded` maintained on the toggle; `aria-checked` kept in sync
by `reflect()` (the grow-mode idiom); outside-click closes the panel;
**Escape closes and returns focus to the toggle** (grow-mode omits the
focus-return, fixed here); Up/Down gives roving focus across the menu's
items.

---

## 7. Persistence

Only the global Show/Hide toggle, the grow-studio-family convention:

```js
const LS_VISIBLE = 'grow-phasenotes:visible';   // 'on' | 'off', default on
```

Every localStorage access is try/catch wrapped. Not persisted:
`activeSetId` (an article id is meaningless on the next page, resets to
`'all'` on every `contentObjectView:preRender`) and `revealedUpTo` (§5 —
runtime-only, trickle owns revisit-lock behaviour).

---

## 8. Motion and accessibility

`prefersReducedMotion()` (`notesLayer.js`) checks `matchMedia`,
`html.no-motion`/`[data-tm-no-motion]` and `html[data-motion="off"]` — the
last of these is what `adapt-grow-mode`'s Animations toggle actually sets
(`adapt-grow-mode.js:130`).

Under reduced motion: notes are shown fully drawn and static — no
`am-run`, no `ChalkLabels.play()` — never suppressed. Both engines hold the
finished artwork regardless of the running state, so the annotation is
always fully present.

Note regions carry `role="group"` and an `aria-label` (from
`ariaRegionLabel`, §2); they are not modals (annotations over live content,
not a focus trap).

---

## 9. File manifest

| File | Purpose |
|---|---|
| `bower.json` | Plugin registration + dependency declaration (`adapt-grow-layer`, `adapt-contrib-trickle`) |
| `package.json` | npm mirror |
| `properties.schema` | Authoring UI schema — `config._growPhaseNotes`, `article._growPhaseNotes`, `globals.ariaRegion` |
| `example.json` | A worked three-note set on one article |
| `js/adapt-grow-phasenotes.js` | Entry + controller: harvest, §3 bindings, state, public API |
| `js/engines.js` | Single re-export of the three pagenotes drawing libs |
| `js/notesLayer.js` | Asset injection, note/region build, the `Set` state model (§5) |
| `js/mirrorButton.js` | The trickle coupling (§4) |
| `js/navMenu.js` | Nav button + popup menu (§6) |
| `less/grow-phasenotes.less` | Menu, region/note, mirror button styling |
| `README.md` | Human-facing version of this spec |

No `templates/` — DOM-only, like every other `grow-*` extension.

**Build wiring**: nothing to register beyond a valid `bower.json` — the
`compile` target's RequireJS plugin-discovery glob
(`grunt/config/javascript.js`) and the LESS glob
(`grunt/config/less.js`) both pick up `src/extensions/*` automatically.

---

## 10. Known limitations

- **Mirror tab-order** (§4): the mirror's single tab stop falls at the end
  of the document tab order, not inline where the real button sits.
- **Mid-page target resolution** (`adapt-grow-phasenotes.js` →
  `onChildAdded`): a note's `_targetId` pointing at a block that arrives
  *after* its owning article is already mounted (per-block trickle within
  one article) resolves correctly from that point on, but the region it was
  built against keeps the article-wide fallback box it was given at mount
  time — the region itself is not rebuilt once an article has mounted.
- **`_growLayer._isEnabled: false` is not read**: like every other
  `navMount`/`overlay()` consumer, this extension assumes `adapt-grow-layer`
  is present and enabled; it has no standalone fallback path (contrast
  `adapt-grow-studio`, which does).

---

## 11. History

| Date | Change |
|------|--------|
| 2026-11-10 | Initial build: notesLayer/engines, controller, mirror button, nav menu, LESS. |
