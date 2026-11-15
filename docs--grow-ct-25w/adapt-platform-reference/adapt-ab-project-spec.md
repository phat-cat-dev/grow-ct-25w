# adapt-ab project spec

Purpose and ground rules for this repo. Read this before adding or changing
anything under `src/components/adapt-ab-*` or `src/extensions/adapt-ab-*`.

Companion docs: `docs/fresh-adapt-ab-dev-setup.prompt.md` (how this sandbox was
stood up), `docs/adapt-extensibility-map.md` (what the framework actually lets
you extend and where), `docs/adapt-ab-components-sketch.md` (component design
notes), `docs/adapt-dom-map.html` (rendered DOM reference).

---

## 1. Aim

This repo is a **vanilla Adapt Framework install** (`adapt_framework` 5.56.3,
default `adapt-contrib-vanilla` theme, stock `adapt-contrib-core`) used as a
**dev sandbox** for building a family of `adapt-ab-*` components and
extensions in isolation, so they can later be dropped into real production
Adapt courses with minimal friction.

The two things that must both stay true at all times:

1. **The framework install stays vanilla.** Default course, default theme,
   default core, default contrib plugins — untouched except for the minimal
   test-page wiring needed to exercise our own plugins.
2. **Everything we build lives in self-contained, portable `adapt-ab-*`
   folders** that can be lifted out of this sandbox and copied straight into
   another project's `src/components/` / `src/extensions/` with no further
   editing.

If a change would blur that line — e.g. editing `adapt-contrib-vanilla`,
editing `src/core`, or hardcoding something in a shared file that only our
plugins need — it's the wrong change. Isolate it inside an `adapt-ab-*`
plugin instead.

---

## 2. Why "modular mode"

The end goal is **portability**, not just a working sandbox. Every
`adapt-ab-*` component/extension must be dropped into a different Adapt
project and work (or render with sane neutral defaults) without:

- editing any file outside its own plugin folder,
- depending on anything from this course's `src/course/en/*.json`,
- depending on `adapt-contrib-vanilla` or any other theme being present,
- requiring a specific brand/theme to be installed.

This is why Step 3 of the dev-setup prompt (`adapt-ab-base`) exists: it is a
**style-only token foundation**, not a theme. It ships neutral defaults for
every `--ab-*` custom property our plugins reference, so a bare install with
just `adapt-ab-base` + one of our plugins renders correctly, unstyled-but-not-
broken. A real brand theme then overrides the same tokens — it never has to
touch plugin files, and plugin files never have to know a theme exists.

```
building blocks   adapt-ab-card / -accordion / -carousel / -sandbox / ...
                   (structure + behaviour; consume --ab-* tokens with fallbacks)
  ---------------- contract: class hooks + --ab-* custom properties ----------------
base tokens        adapt-ab-base
                   (neutral :root defaults for every --ab-* token the plugins need)
  ---------------- same contract, loaded after base, wins by cascade order --------
theme (future)     adapt-ab-theme  <-- not yet imported, see §6
                   (brand palette, typography, the "real" --ab-* values)
vanilla            adapt-contrib-vanilla  (untouched, ships with the framework)
```

Neither layer edits another layer's files. The seam is entirely CSS custom
properties plus class-name conventions — see
`docs/adapt-extensibility-map.md` §6–8 for the full framework-level reasoning
behind this contract.

---

## 3. Rules

### 3.1 Keep the base install vanilla

- Do not modify `adapt-contrib-vanilla`, `src/core`, `Gruntfile.js`,
  `grunt/`, or framework config beyond what's strictly needed to register a
  plugin (`bower.json` discovery) or wire the test page.
- Default course content (`src/course/en/*.json`) may only gain the minimal
  additions needed to place an instance of our own component/extension for
  manual testing — never bulk rewrites of the stock course.
- `src/core` is a submodule pinned to a released `adapt-contrib-core` version.
  Never hand-edit it; bump the pin via the normal framework upgrade path if a
  newer core is genuinely needed.

### 3.2 Everything custom lives under the `adapt-ab-*` namespace

- Folder: `src/components/adapt-ab-<name>/` or `src/extensions/adapt-ab-<name>/`.
- Registered type name: `ab-<name>` (e.g. `"_component": "ab-card"`).
- `bower.json` `targetAttribute`: `_ab<Name>` (PascalCase, e.g. `_abCard`,
  `_abModal`).
- `.gitignore` already carries the exception that makes this namespace
  trackable against the framework's own `src/components/*` /
  `src/extensions/*` ignore rules:
  ```
  src/components/*
  !src/components/adapt-ab-*/
  src/extensions/*
  !src/extensions/adapt-ab-*/
  ```
  Any new plugin folder must match the `adapt-ab-*` glob to be tracked at all.

### 3.3 A plugin folder is the unit of portability

A component/extension folder must be **complete and self-contained**:

- its own `bower.json` (version, `framework` range, `main`, `keywords:
  ["adapt-plugin", "adapt-component"|"adapt-extension"]`, `license`,
  `private: true`),
- its own `js/`, `less/`, `templates/` (components), `properties.schema` /
  `schema/component.schema.json`,
- its own `test/` (unit tests for any pure logic extracted into a
  `*Logic.js` module — see `accordionLogic.test.js`, `carouselLogic.test.js`,
  `modalLogic.test.js` for the pattern),
- a short `README.md` for extensions (see `adapt-ab-base/README.md`,
  `adapt-ab-modal/README.md`) documenting what it provides, how to enable/
  configure it, and its styling contract.

Nothing inside the folder may reference a path outside itself except
framework core modules (`core/js/...`) and `react` / standard deps already
available in any Adapt install. No plugin may `import` from a sibling
`adapt-ab-*` plugin's internals — share behaviour via a `*Logic.js` module
copied into each, or via the token/CSS contract, not via cross-plugin JS
imports.

### 3.4 Styling: tokens only, always with fallbacks

- Component/extension LESS **consumes** `--ab-*` / `--ab-base-*` custom
  properties. It never defines a palette, never hardcodes a hex value for
  anything a theme might reasonably want to override.
- Every `var(--ab-*)` reference should carry a sane fallback
  (`var(--ab-base-surface, #fff)`) so the plugin still renders if loaded
  without `adapt-ab-base` or any theme at all.
- `adapt-ab-base` is the only place that *defines* the token defaults
  (`:root { --ab-base-ink: ...; }`). Nothing else defines tokens; everything
  else reads them.
- A theme overrides by **redefining the same custom properties**, globally or
  under a scope class (`.ab-theme-x { --ab-accent: ...; }`). It does this in
  its own files, never by editing `adapt-ab-base` or any `adapt-ab-*` plugin.

### 3.5 Component contract (non-negotiable per `adapt-extensibility-map.md` §8)

Every `adapt-ab-*` component must, regardless of what it renders inside
`.component__inner`:

- honour the completion signal — `setupInviewCompletion(...)` for
  presentational components, or visitation-based completion
  (`_isVisited` on all items) for interactive ones;
- declare `trackable()` correctly so only state that should survive a
  revisit enters `suspend_data` (transient UI state like "is currently open"
  is excluded unless it's genuinely part of the SCORM contract);
- keep accessibility intact — correct heading levels, native control
  semantics (real `<button>`s), ARIA roles/states matching the UI pattern
  (accordion, carousel, dialog, etc.), keyboard operability;
- namespace its own BEM classes (`ab-card__*`, `ab-accordion__*`, ...) so
  they never collide with core or theme classes;
- extend the core-owned `.component` root and state classes (`is-complete`,
  `is-visited`, ...) rather than stripping or replacing them.

### 3.6 Naming / shape consistency

New plugins should mirror the file layout already established by
`adapt-ab-card`, `adapt-ab-accordion`, `adapt-ab-carousel`, `adapt-ab-modal`,
`adapt-ab-sandbox`:

```
src/components/adapt-ab-<name>/
  bower.json
  properties.schema                 (or schema/component.schema.json)
  js/adapt-ab-<name>.js              # components.register(...)
  js/<Name>Model.js                  # ComponentModel / ItemsComponentModel subclass
  js/<Name>View.js                   # ComponentView subclass
  js/<name>Logic.js                  # pure logic, unit-testable, no DOM/Backbone
  templates/<name>.jsx               # core/js/reactHelpers
  less/ab-<name>.less                # tokens only, with fallbacks
  test/<name>Logic.test.js
  test/package.json
```

```
src/extensions/adapt-ab-<name>/
  README.md
  bower.json                         # extension name "ab<Name>", targetAttribute "_ab<Name>"
  js/adapt-ab-<name>.js
  js/<name>Logic.js                  # if there's non-trivial runtime behaviour
  less/ab-<name>.less
  test/<name>Logic.test.js
  test/package.json
```

---

## 4. Current inventory

Components (`src/components/`):
- `adapt-ab-card` — presentational card group, inview completion
- `adapt-ab-accordion` — visitation completion, Bootstrap-accordion ARIA shape
- `adapt-ab-carousel` — visitation completion, Bootstrap-carousel ARIA shape
- `adapt-ab-hotgraphic` — inlined-SVG hotspot diagram, visitation completion,
  per-diagram paint via theme-level token blocks (no new code per diagram)
- `adapt-ab-sandbox` — minimal proof-of-pipeline component, base tokens only

Extensions (`src/extensions/`):
- `adapt-ab-base` — the neutral `--ab-*` token foundation (§2); no runtime
  behaviour
- `adapt-ab-modal` — dependency-free, accessible global modal, triggerable
  from any `data-ab-modal` element in authored content

All of the above must keep rendering correctly with only `adapt-ab-base`
installed and no theme present — that's the contract this whole repo exists
to prove.

---

## 5. Verification expectations

Before calling a plugin done:

- `npx grunt build` passes.
- It renders correctly on the sandbox test page with only `adapt-ab-base`
  active (no theme) — proving the token-fallback contract.
- If a theme-scope class is toggled (see the `ab-theme-demo` seam in the
  dev-setup prompt, Step 4), the plugin visibly re-skins with no code change.
- Pure logic extracted to `*Logic.js` has unit tests under `test/`.
- Completion and accessibility behave per §3.5 — spot-check interactive
  components (accordion/carousel/modal) with keyboard only.

---

## 6. Upcoming: importing the real `ab-theme`

`adapt-ab-base` is a **placeholder/neutral foundation**, not the final
theme. Once the real `adapt-ab-theme` extension/framework (brand palette,
type scale, the full `--ab-base-if-adapt-*` adapter layer referenced in
`docs/adapt-extensibility-map.md` §6) is ready on its own branch, it will be
imported into this install as an **additional, later-loaded layer** —
following the same seam already proven here:

- `adapt-ab-theme` redefines the same `--ab-*` / `--ab-base-*` custom
  properties that `adapt-ab-base` defines and our components already
  consume — it does not edit `adapt-ab-base` or any `adapt-ab-*` component
  file.
- Load order stays: vanilla → `adapt-ab-base` (neutral defaults) →
  `adapt-ab-theme` (brand values win by cascade/later-load, exactly like the
  `ab-theme-demo` proof in the dev-setup prompt).
- No component or extension built so far should need to change when that
  import happens. If one does, that's a sign it broke the token-only rule in
  §3.4 and needs fixing now, before the theme lands.
- At that point `adapt-ab-base`'s neutral defaults become the fallback layer
  under the real theme, not something to delete — keeps every plugin
  theme-optional for other projects that import them without `ab-theme`.

Until then: **do not pre-empt the theme.** No brand colours, no
Cardiff-Met-specific (or any other brand-specific) styling anywhere in
`adapt-ab-base` or any component/extension LESS — that is explicitly
out of scope for this sandbox (see the dev-setup prompt's "DO NOT" list) and
is the real theme's job alone.

---

## 7. Porting a plugin out of this repo

To move an `adapt-ab-*` plugin into a production project:

1. Copy the whole `src/components/adapt-ab-<name>/` (or `extensions/...`)
   folder across, unmodified.
2. Ensure the target project has `adapt-ab-base` (or its own equivalent
   token set / the real `adapt-ab-theme` once available) installed, so the
   `--ab-*` tokens the plugin consumes resolve to something sensible.
3. Run the target project's install step (`npm run adapt-install` or
   equivalent) so the plugin is picked up by the build.
4. Register an instance in course JSON (`"_component": "ab-<name>"` /
   enable the extension via its documented config key).
5. No other file in the target project should need editing. If it does, the
   plugin broke §3.3 (self-containment) and should be fixed at the source
   here, not patched per-consumer.
