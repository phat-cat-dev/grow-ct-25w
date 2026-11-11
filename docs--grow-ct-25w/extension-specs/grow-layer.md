# adapt-grow-layer — GROW Layer

Extension specification for the GROW management layer: the shared runtime host
that every GROW "chrome"/overlay tool mounts onto. Written as a spec for another
agent to read before building on top of, or alongside, this mechanism.

**Grounded in:** `src/extensions/adapt-grow-layer/` (the defining extension) and
its five current consumers: `adapt-grow-pagenotes`, `adapt-grow-pagenav`,
`adapt-grow-mode`, `adapt-grow-studio`, `adapt-grow-journal-extension`.

---

## 1. What it is (and is not)

`adapt-grow-layer` is a **runtime, DOM-level Adapt extension**. It is not:

- a CSS/LESS theme-overlay system (that is `grow-ct-theme-packs`, a separate,
  unrelated LESS-variable theme-selector — see §6),
- a JSON content overlay (nothing to do with context packs / `merge-context.js`),
- a component (nothing is placed in `blocks.json`/`components.json` — it is pure
  JS infrastructure, included course-wide).

It provides **one persistent host region**, `#grow-layer`, appended to `<body>`
once, which other GROW extensions/components use instead of each hand-rolling
their own fixed-position overlay or nav-injection code.

```
#grow-layer                  the region, appended to <body> ONCE (survives page re-render)
├─ .grow-layer__overlay      fixed, full-viewport, click-through stage — overlay tools append here
└─ .grow-layer__dock         fixed bottom zone for toolbar tools — reserves --grow-dock-h
```

Plus a **nav coordinator** (`navMount`) that re-injects nav-bar chrome into
`.nav__inner` on every page/menu view, because Adapt re-renders that element on
every page and a plain one-time DOM append would be wiped out.

---

## 2. Build-time injection (how it gets into the bundle at all)

No course ever references `adapt-grow-layer` directly. It is included by Grunt's
RequireJS plugin auto-discovery, which globs every extension's `bower.json`:

**File:** `grunt/config/javascript.js` (two targets, `dev` and `compile`, identical
pattern — the `compile` target is what `grunt build` / `package-scorm.js` runs):

```js
plugins: [
  '<%= sourcedir %>components/*/bower.json',
  '<%= sourcedir %>extensions/*/bower.json',
  '<%= sourcedir %>menu/<%= menu %>/bower.json',
  '<%= sourcedir %>theme/<%= theme %>/bower.json'
],
pluginsPath: '<%= sourcedir %>/plugins.js',
pluginsModule: 'plugins',
pluginsFilter: function(filepath) {
  return grunt.config('helpers').includedFilter(filepath);
}
```

Every directory under `src/extensions/*` with a `bower.json` is a candidate. The
`"extension"` / `"targetAttribute"` keys in `adapt-grow-layer/bower.json` register
it with Adapt's plugin system:

```json
"extension": "growLayer",
"targetAttribute": "_growLayer",
```

Because it has **no required config key** gating inclusion and `_growLayer._isEnabled`
defaults to `true` with no course needing to set it, `adapt-grow-layer` is present
in every SCORM package built from this repo — it costs nothing until a tool calls
`overlay()`/`dock()` (the LESS sets `--grow-dock-h: 0rem` by default).

This happens identically for every tier/context build via `package-scorm.js` →
`grunt build` → `javascript:compile` → the glob above.

---

## 3. Runtime injection (how the DOM region actually appears)

**File:** `src/extensions/adapt-grow-layer/js/adapt-grow-layer.js` (full file, this
is the entire mechanism — 119 lines):

```js
import Adapt from 'core/js/adapt';

class GrowLayer {
  constructor() {
    this._root = null;
    this._overlay = null;
    this._dock = null;
    this._navInjectors = [];
    this._runNav = this._runNav.bind(this);
    Adapt.on('app:dataReady', () => this.getRoot());
    Adapt.on('pageView:ready menuView:ready', this._runNav);
  }

  getRoot() {
    if (this._root && this._root.isConnected) return this._root;
    const root = document.createElement('div');
    root.id = 'grow-layer';
    root.className = 'grow-layer';
    root.setAttribute('role', 'region');
    root.setAttribute('aria-label', 'GROW layer');
    document.body.appendChild(root);
    this._root = root;
    return root;
  }

  overlay() {
    if (this._overlay && this._overlay.isConnected) return this._overlay;
    const el = document.createElement('div');
    el.className = 'grow-layer__overlay';
    this.getRoot().appendChild(el);
    this._overlay = el;
    return el;
  }

  dock() {
    if (this._dock && this._dock.isConnected) return this._dock;
    const el = document.createElement('div');
    el.className = 'grow-layer__dock';
    this.getRoot().appendChild(el);
    this._dock = el;
    document.documentElement.classList.add('grow-has-dock');
    return el;
  }

  navMount(id, inject) {
    this._navInjectors = this._navInjectors.filter(n => n.id !== id);
    this._navInjectors.push({ id, inject });
    this._runNav();
    return () => { this._navInjectors = this._navInjectors.filter(n => n.id !== id); };
  }

  _runNav() {
    const nav = document.querySelector('.nav__inner');
    if (!nav) return;
    for (const { inject } of this._navInjectors) {
      try { inject(nav); } catch (e) { /* one tool must not break the others */ }
    }
  }
}

const growLayer = new GrowLayer();
Adapt.growLayer = growLayer;
export default growLayer;
```

(Field/implementation detail may differ slightly in on-disk formatting; the
contract above — `getRoot/overlay/dock/navMount`, the two Adapt event hooks, the
idempotent `isConnected` guards — is exact and is what any new consumer must rely
on.)

**Key behavioural points for anything that will consume this:**

- `getRoot()` creates `#grow-layer` **the first time it is called**, triggered
  once on `app:dataReady` by the layer's own constructor — so it exists before
  any consumer's own `app:dataReady`/`adapt:start` handler needs it, provided
  module load order doesn't matter (ES module imports are resolved before any
  handler runs).
- `overlay()` and `dock()` are **lazy and idempotent** — call them as many times
  as you like from as many tools as you like; the same element is returned and
  only created once.
- `overlay()` returns a `position: fixed; inset: 0; pointer-events: none` stage
  (z-index 1000). Everything you append into it is click-through by default —
  **you must set `pointer-events: auto` on your own interactive children** (the
  pattern every current consumer follows: `> * { pointer-events: auto; }` style
  rule, or set it directly on the button/panel element).
- `dock()` returns a fixed bottom-zone element and flips `grow-has-dock` on
  `<html>`, which reserves `--grow-dock-h` (6rem) as body padding — so a dock
  tool doesn't have its content obscured by other page chrome, and vice versa.
- `navMount(id, inject)` is the **only** sanctioned way to put a button in the
  top nav bar as a GROW tool. `inject(nav)` is called immediately, and again on
  every subsequent `pageView:ready`/`menuView:ready` (Adapt tears down and
  rebuilds `.nav__inner` on every page navigation — a one-off `appendChild` would
  be lost on the very next page). **Your `inject` function must be idempotent**:
  check `nav.querySelector(...)` for your own marker and return early if already
  present. One tool throwing inside `inject` is caught and does not break the
  others (`_runNav`'s try/catch). `navMount` returns an unmount function if you
  ever need to deregister.

**LESS (the only visual contract the layer itself owns):**

**File:** `src/extensions/adapt-grow-layer/less/grow-layer.less`

```less
:root { --grow-dock-h: 0rem; }
html.grow-has-dock { --grow-dock-h: 6rem; }
html.grow-has-dock #wrapper { padding-bottom: var(--grow-dock-h); }
html.grow-has-dock { scroll-padding-bottom: var(--grow-dock-h); }

.grow-layer {
  &__overlay {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 1000;
  }
  &__dock {
    position: fixed;
    left: 0; right: 0; bottom: 0;
    z-index: 900;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem;
    pointer-events: none;
    > * { pointer-events: auto; }
  }
}

html.no-motion .grow-layer,
html[data-motion="off"] .grow-layer {
  * { animation: none !important; transition: none !important; }
}
```

The layer owns **no visible styling** beyond this stage/dock positioning — every
mounted tool brings its own look (its own LESS file, its own z-index ABOVE 1000
if it needs to sit over the overlay stage, e.g. `adapt-grow-studio`'s drawer at
`z-index: 1100`).

---

## 4. Consumers (reference patterns for a new tool)

| Extension/component | Uses | Pattern |
|---|---|---|
| `adapt-grow-pagenotes` (component) | `overlay()` | Appends a position-matched note overlay into the shared stage; tracks a target element's `getBoundingClientRect()` on scroll/resize. |
| `adapt-grow-pagenav` | `navMount('pagenav', …)` | Injects prev/next page buttons flanking the nav back button; re-run every nav render. |
| `adapt-grow-mode` | `navMount('mode', …)` | Injects a single toggle button + popup `<div role="menu">` panel built from a template string, wired with `addEventListener` inside `mount()`. The reference pattern for "nav button + its own menu overlay". |
| `adapt-grow-studio` | `navMount('grow-studio', …)` + `getRoot()` | Nav button via `navMount`; a separate fixed drawer panel appended once to `getRoot()` (not `overlay()`, since it needs full pointer-events and a higher z-index), mounted lazily on first open. Has an explicit **fallback** path if `growLayer` is absent (floats its own button, appends drawer to `<body>`). |
| `adapt-grow-journal-extension` | `navMount('journal', …)` + `overlay()` | Nav button via `navMount`; the notebook panel itself is appended into `overlay()` (not `getRoot()` directly), relying on the panel setting its own `pointer-events: auto`. |

Every nav-mounted tool uses a **unique `navMount` id** (`'mode'`, `'pagenav'`,
`'grow-studio'`, `'journal'`) — `navMount` replaces any existing injector with the
same id before pushing, so reusing an id registered by another tool would
silently steal its slot. **Any new tool must pick its own unique id.**

Every tool guards its own injected markup with a CSS-class/selector check at the
top of its `inject`/`mount` function (`if (nav.querySelector('.grow-mode')) return;`)
— this is the idempotency contract `navMount` requires of its callers.

---

## 5. Settings

Config key: `_growLayer` (config.json). Extension id: `growLayer`. Requires Adapt
framework `>=5.19.1`. Single property:

```json
"_growLayer": { "_isEnabled": true }
```

`_isEnabled: false` is not currently read by the JS (the constructor runs
unconditionally) — the schema advertises the switch but the extension does not
yet act on it. Treat it as advisory/future-proofing, not a verified kill switch.

---

## 6. Do not confuse with: `grow-ct-theme-packs`

`src/theme/grow-ct-theme-packs/` is a **separate, unrelated** LESS-variable
theme-selector system (picks a theme file via `current-theme.less`), excluded
per-course via `config.json`'s `build.excludes` array. It shares the "GROW"
naming prefix and nothing else — no shared code, no shared DOM, no shared
events. Do not route new runtime-overlay work through it, and do not assume
`grow-layer` has any theming responsibility (it has none beyond honouring
`data-motion`/`no-motion` for its own children's animations).

---

## 7. File manifest (defining + consuming files)

**Defines the extension:**

- `src/extensions/adapt-grow-layer/js/adapt-grow-layer.js` — the entire mechanism (§3)
- `src/extensions/adapt-grow-layer/less/grow-layer.less` — stage/dock positioning only
- `src/extensions/adapt-grow-layer/bower.json` — Adapt plugin registration + build-time glob target
- `src/extensions/adapt-grow-layer/package.json` — npm metadata (no runtime effect)
- `src/extensions/adapt-grow-layer/properties.schema` — authoring UI schema for `_growLayer`
- `src/extensions/adapt-grow-layer/README.md` — human-facing version of this spec

**Build-time inclusion mechanism:**

- `grunt/config/javascript.js` — RequireJS plugin-discovery glob (`extensions/*/bower.json`) that pulls every extension, including this one, into `adapt.min.js` with no course-level reference

**Consumes the extension (reference implementations for a new tool):**

- `src/components/adapt-grow-pagenotes/js/overlay.js` — `overlay()` consumer, position-tracking overlay
- `src/extensions/adapt-grow-pagenav/js/adapt-grow-pagenav.js` — `navMount()` consumer, simple nav buttons
- `src/extensions/adapt-grow-mode/js/adapt-grow-mode.js` — `navMount()` consumer, button + popup menu (the pattern to copy for "its own menu overlay like grow-mode")
- `src/extensions/adapt-grow-studio/js/adapt-grow-studio.js` + `less/grow-studio.less` + `bower.json` + `README.md` — `navMount()` + `getRoot()` consumer, button + full drawer panel, with a documented no-grow-layer fallback
- `src/extensions/adapt-grow-journal-extension/js/adapt-grow-journal-extension.js` + `bower.json` + `README.md` — `navMount()` + `overlay()` consumer, button + non-blocking panel

---

## 8. History

| Date | Change |
|------|--------|
| 2026-11-10 | Initial spec, written from direct source inspection for use as another agent's reference before extending the GROW layer (trickle-phase-end reveal tool). |
