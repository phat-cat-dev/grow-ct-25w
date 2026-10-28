# L2 — adapt-core-less

What `src/core/less` contributes to the compiled `adapt.css`, and exactly where
it hooks onto the L1 structural spine
(`tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.less`).

Generate: `node tools/theme-mapping/layers/l2-adapt-core-less/l2-adapt-core-less-generator.js`
Reads: L1's `adapt-template-classes.json`/`.less` (for the spine + line numbers) and
`src/core/less/**/*.less` (compiled for real via `lessc`).
Writes: `l2-adapt-core-less.less`, `l2-adapt-core-less.json` (this directory).

## The grunt compile sequence (how core becomes part of `adapt.css`)

Confirmed by reading the actual task implementation, not just its config:
`grunt/config/less.js` (options) and `grunt/tasks/less.js` (the custom
`grunt.registerMultiTask('less', ...)` that consumes them — this is **not**
stock `grunt-contrib-less`).

The task builds one string of plain `@import 'path';` lines and hands it to
`less.render()` **once**. There is no per-layer compile step — one LESS
compilation, one `adapt.css` + `adapt.css.map`.

```
Stage 0  screenSize (config.json, falls back to src/core/schema/config.schema.json:174-202
         defaults: small:0 medium:720 large:960 xlarge:1280, px->em) injected as
         @adapt-device-* variables + a :root{} CSS-var block.
         grunt/tasks/less.js:19-51

Stage 1  options.mandatory  ->  src/core/less/**/*.less          ALWAYS, unconditional
         grunt/tasks/less.js:53-66        (this layer, L2)

Stage 2  options.src, in this literal array order (grunt/config/less.js:17-22):
           2a  src/components/*/less/**/*.less    only installed components (filter: includedFilter)
           2b  src/extensions/*/less/**/*.less    AB theme's L2-L6 token cascade lives here
           2c  src/menu/<menu>/**/*.less          whichever menu plugin config.json names
           2d  src/theme/<theme>/**/*.less        adapt-contrib-vanilla — LAST            (this is L3)
         grunt/tasks/less.js:68-82
```

Within each glob, `sortLESSFilePaths`/`compareFilePaths` (`grunt/config/less.js:7-18`)
orders files alphanumerically per-directory, with a length-tiebreak when one
filename is a prefix of another in the same folder (this generator reimplements
that same function, cited inline, so L2's file order matches the real build).

**Core compiles first, vanilla compiles last, unconditionally, by hard-coded
stage order** — not a cascade trick, a literal two-loop sequence in
`grunt/tasks/less.js:53-82` (mandatory loop runs to completion before the src
loop even starts).

## Correction to an earlier claim: core does NOT depend on the theme

I previously assumed core's `page.less`/`block.less` (`@max-page-width`,
`@max-content-width`) were only defined by the vanilla theme and core would
fail to compile alone. **Checked directly — this is wrong.** Confirmed by
running `lessc` against `src/core/less/**/*.less` alone (no theme, no
extensions, nothing but the Stage-0 device variables):

```
25 files, 66125 bytes bundled, lessc exit 0, 2400 lines of real CSS.
```

`src/core/less/_defaults/_variables.less:30-33,73-80` defines its **own**
defaults for every variable `core/*.less` consumes:
`@max-content-width`, `@max-page-width`, `@block-padding-ver`,
`@block-padding-hoz`, `@component-padding-hoz`. Core is self-sufficient.

What actually happens at Stage 2d is that
`src/theme/adapt-contrib-vanilla/less/_defaults/_spacing-containers.less`
**redefines the same variable names** with the theme's own values (e.g.
`@block-padding-ver: 4rem` — same name, different/final value, because LESS
resolves variables against the single merged import tree and the *last*
definition in that tree wins, regardless of which stage declared it first).
Core's variables are therefore defaults that the theme is free to, and does,
override by colliding on the same name — not a dependency running the other
way.

## What core actually puts on each L1 spine selector

Confirmed by compiling the real bundle and reading the matching CSS block.
Core only ever sets **position/layout/behaviour**, never colour, spacing-scale,
or typography, on the spine:

| L1 spine selector | real core rule (compiled) | core source |
|---|---|---|
| `.page` | `margin: 0 auto; max-width: 90rem;` | `core/page.less:2` |
| `.page__header-inner` (not itself a spine rung — a header-family descendant of `.page`) | `margin: 0 auto; max-width: 60rem;` | `core/page.less:5` |
| `.article` | *(no own rule — `&__header-inner` only)* | — |
| `.article__inner` | *(none)* | — |
| `.block` | `position: relative;` | `core/accessibility.less` |
| `.block__inner` | `margin: 0 auto; max-width: 60rem;` | `core/block.less:3` |
| `.component` | `position: relative;` + `width: 100%;` (two separate rule blocks, two files) | `core/accessibility.less`, `core/component.less:1` |
| `.component__container` | `display:flex; flex-direction:column; flex-wrap:wrap; align-items:flex-start;` (+ `row` at `min-width:45rem`) | `core/component.less:4-13` |
| `.component__inner.<name>__inner` | not a core class at all (per-component `.jsx`) | — |
| `.component__widget` | not a core class at all (per-component `.jsx`) | — |

`core/global.less` adds one Firefox fix shared across `.page/.article/.block/.component.__title-inner`
(and `.menu`/`.menu-item`, outside L1's scope).

The full, exact, per-selector compiled-CSS mapping — generated, not hand-typed,
and self-updating if L1 regenerates — is in `l2-adapt-core-less.less`, with every
block commented to cite the matching line in
`tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.less`.

## Why this matters for the AB extension (flagged, not yet acted on)

The AB theme's token cascade sits at **Stage 2b** — compiled *before* menu and
*before* vanilla (Stage 2d). In raw import order that is the opposite of
"layered over vanilla": a plain selector override in the extension would lose
to a same-specificity vanilla rule declared later. The AB cascade works around
this by dealing in `--ab-*` custom-property tokens rather than literal selector
overrides — tokens don't collide with vanilla's declarations, they just sit
there until something reads them via `var()`.

## Layer boundaries

- **L2 (this layer)**: `src/core/less/**/*.less` only. No per-component
  styling exists here — `src/core/less` has no plugin/component directory.
  Per-component LESS lives in `src/components/*/less/**/*.less` (Stage 2a,
  outside L2) and is styled for real in `src/theme/adapt-contrib-vanilla/less/plugins/*`
  (Stage 2d, L3).
- **L3 (next)**: `adapt-contrib-vanilla` — where colour, the spacing scale,
  and typography actually land on these same selectors, and where every
  per-component section exists.
