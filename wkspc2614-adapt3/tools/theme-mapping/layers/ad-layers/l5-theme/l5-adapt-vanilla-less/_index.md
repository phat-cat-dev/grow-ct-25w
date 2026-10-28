# L4 — adapt-vanilla-less

What `adapt-contrib-vanilla`'s less contributes on top of L2 core, and exactly
where it hooks onto the same L1 structural spine
(`tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.less`),
cited alongside L2's own hooks
(`tools/theme-mapping/layers/l2-adapt-core-less/l2-adapt-core-less.less`).

Generate: `node tools/theme-mapping/layers/l4-adapt-vanilla-less/l4-adapt-vanilla-less-generator.js`
(requires the L1 and L2 generators to have been run first - it reads their JSON, it does not re-derive L2's hooks)
Reads: L1's `adapt-template-classes.json`/`.less` (spine + line numbers), L2's
`l2-adapt-core-less.json` (core's own hooks, cited not recompiled) and
`src/theme/adapt-contrib-vanilla/less/**/*.less` (compiled for real via `lessc`,
together with `src/core/less` as mixin context - see below).
Writes: `l4-adapt-vanilla-less.less`, `l4-adapt-vanilla-less.json` (this directory).

## Correction to the obvious assumption: vanilla does NOT compile standalone

L2's doc corrected an assumption that core depends on the theme. The reverse
is true for vanilla, and it is not a borrowed assumption this time - checked
directly, the same way:

```
node /tmp/vanilla-standalone-test-gen.js && npx lessc /tmp/vanilla-standalone-test.less
SyntaxError: .l-container-responsive is undefined
  in /tmp/vanilla-standalone-test.less on line 5355
```

Grepping confirms why - vanilla's own `core/*.less` files call mixins they
never define themselves:

```
core/page.less:3     .l-container-padding(@page-padding-ver, @page-padding-hoz);
core/article.less:40 .l-container-padding(@article-header-padding-ver, @article-header-padding-hoz);
core/block.less:17   .l-container-padding(@block-padding-ver, @block-padding-hoz);
core/notify.less:5   .l-container-responsive(@max-notify-width);
core/attribution.less:14 .transform(translate3d(0,0,0));
core/drawer.less:42  .transition(left var(--adapt-drawer-duration) ...);
```

All four mixins (`.l-container-padding`, `.l-container-responsive`,
`.transform`, `.transition`) are defined only in
`src/core/less/_defaults/layout.less` and
`src/core/less/core/{transform,transitions}.less`. So this generator compiles
vanilla's files with **all** of core's less in the bundle as mixin context -
exactly the real grunt sequence, Stage 1 (mandatory) immediately followed by
Stage 2d (`src/theme/<theme>/**/*.less`), nothing else mixed in (Stage
2a/2b/2c - components/extensions/menu - are deliberately omitted; this is a
direct two-layer comparison, not a full build).

One consequence, inherited from L2's variable-precedence finding: because
core's files are compiled *before* vanilla's in this bundle but LESS resolves
variables against the whole merged tree regardless of declaration order,
vanilla's own `_defaults/_spacing-containers.less` redefinitions (e.g.
`@block-padding-ver: 4rem`, overriding core's own default of the same value)
are what core's own mixins pick up had they been scanned here too - they are
not, that attribution is L2's job, not re-done in this layer.

## What L4 actually puts on the L1 spine, over L2

Confirmed by compiling core+vanilla together and reading the matching CSS
block for each spine rung, cross-checked against L2's own JSON (not
re-derived - this layer cites L2, it doesn't recompute it):

| L1 spine selector | L2 (core) already declared | L4 (vanilla) adds | relation |
|---|---|---|---|
| `.page.contentobject` | `margin:0 auto; max-width:90rem` | `position:relative;` + `.l-container-padding(@page-padding-ver,@page-padding-hoz)` -> `padding-top/right/bottom/left` | **additive** - no shared property name |
| `.page__inner` | *(no core rule)* | `position:relative;` | **new** |
| `.article` | *(no own rule - container only)* | `position:relative;` + `has-bg-image` handling | **new** |
| `.article__inner` | *(no core rule)* | `position:relative;` | **new** |
| `.block` | `position: relative;` (core/accessibility.less) | `position:relative;` + `has-bg-image` handling | **redeclare** - shares `position` (same value, harmless, but cascade order means L4's declaration is the one actually in effect) |
| `.block__inner` | `margin:0 auto; max-width:60rem` | `position:relative;` + `.l-container-padding(@block-padding-ver,@block-padding-hoz)` | **additive** - no shared property name |
| `.component__container` | `display:flex; flex-direction:column; flex-wrap:wrap; align-items:flex-start;` (+ `row` at >=medium) | `flex-direction: unset;` + negative `margin-left`/`margin-right` | **redeclare, and the one that matters** - vanilla's `flex-direction: unset` has **no media-query guard**, so in the real cascade (core mandatory first, vanilla/theme compiled last) it wins over core's media-queried `column`/`row` for every screen size, not just a fallback. This is a genuine override, not a harmless duplicate. |
| `.component` | `position:relative;` (accessibility) + `width:100%;` (component.less) | `position:relative;` + `has-bg-image` handling (no own `width`) | **redeclare** on `position` only; `width:100%` from L2 is left uncontested |
| `.component__inner.<name>__inner` | *(not a core/vanilla class)* | *(not a core/vanilla class)* | n/a - component `.jsx` territory, see L1 |
| `.component__widget` | *(not a core/vanilla class)* | *(not a core/vanilla class)* | n/a - component `.jsx` territory, see L1 |

The `relation` column is not asserted by hand - the generator computes it from
the real compiled property-name sets of L2's cited body vs L4's own compiled
body for the same selector (`new` / `additive` / `redeclare: <names>`), and
the full per-rung detail (file:line for every hook, both layers) is in
`l4-adapt-vanilla-less.less`.

## Why `.component__container`'s override matters for the AB extension

L2's doc flagged that the AB extension's token cascade sits at Stage 2b -
compiled *before* vanilla (Stage 2d) - so a plain selector override in the
extension loses to a same-specificity vanilla rule declared later. This
`.component__container` finding is the concrete proof of exactly that
mechanism already happening *inside* the stock pipeline: core's own
responsive `column`/`row` behaviour is unconditionally overwritten by
vanilla's unguarded `flex-direction: unset`, for no other reason than
"compiled later, same specificity, last declaration in the merged tree wins."
Anything layered after vanilla (there is nothing, in Stage 2d's case - vanilla
is already last) would do the same to vanilla. Nothing after Stage 2b can
plain-override anything in Stage 2d by selector collision; only
custom-property tokens survive that ordering, which is why the AB cascade
uses `var()` rather than selector overrides.

## Known limitation (checked, not swept under the rug)

The primary own-rule hook for every spine selector - the one the `relation`
column above is computed from - is verified correct by direct read of the
generated `.less` (e.g. `.block`, `.block__inner`, `.component__container`,
`.component`'s first/exact hooks all show the right compiled body from the
right file:line). Two sources of noise in the secondary hooks, confirmed and
left as-is rather than chased further (out of proportion with what this pass
was scoped to):

1. `project/columns.less`'s grid mixins (`.make-columns(...)  when (@count >=
   @iteration) {...}`) are LESS mixin *definitions* with parametric guards -
   the scanner's selector-text extraction includes the guard clause as part
   of the "selector" string, which is cosmetic noise (these never compile to
   CSS until called, so they correctly show as container-only, just with an
   ugly label).
2. When the identical resolved selector text appears at two different
   declaration sites inside the *same* vanilla file (e.g.
   `.block.align-vert-center .component__container`, once inside a
   comma-group at `block.less:84` sharing a body with `.block__inner`, once
   alone at `block.less:88`), the per-file isolation lookup can attribute the
   wrong site's compiled body to the other site, because lessc keeps
   comma-joined selectors as one combined key while the source-side scanner
   splits comma alternatives individually. This is a narrower version of the
   cross-file duplicate-selector problem L2 solved with the marker technique
   - confined here to within-one-file alignment-modifier noise
   (`align-vert-center`/`align-horz-*`), never the primary declarations.

## Layer boundaries

- **L4 (this layer)**: `src/theme/adapt-contrib-vanilla/less` spine files only
  (`core/*.less` mirroring L1's structural rungs). Scoped to match L2's own
  scope exactly, per instruction.
- **L3** (`tools/theme-mapping/layers/l3-adapt-core-components-less`) covers
  the theme-independent half of the per-component mapping flagged below -
  `src/components/<dir>/less` (Stage 2a, compiles before any theme, 30 of 32
  L1 components). Built as its own layer, not here.
- **L5** (`tools/theme-mapping/layers/l5-adapt-vanilla-components-less`)
  covers the vanilla half - `adapt-contrib-vanilla/less/plugins/*` (Stage 2d,
  per-component, compiles after L3 and can override it on selector
  collision, the same relationship this layer (L4) has to L2 one level up).
  Built as its own layer, not here.
- Checked while scoping this layer, recorded here so the finding isn't lost
  (L3/L5 cite these counts, not re-derive them):
  - `adapt-contrib-vanilla/less/plugins/` has **19** component-named
    subdirectories, but only **11** of them match an L1 component directory
    name exactly (`accordion, assessmentResults, gmcq, graphic, hotgraphic,
    matching, mcq, media, narrative, slider, textInput`). The other 8
    (`boxmenu, confidenceSlider, glossary, languagePicker,
    pageLevelProgress, resources, trickle, tutor`) are menu/extension plugins
    or components not installed under that name in this project (L1 has
    `adapt-abbott-confidence` and `adapt-abbott-glossary` instead - different
    directories entirely).
  - Confirmed via `grunt/helpers.js:317` (`isPathIncluded`) that vanilla's
    `less/plugins/<name>/` files ARE filtered by whether `<name>` is actually
    installed (same `includedFilter` as Stage 2a/2b). `adapt-contrib-
    confidenceSlider` and `adapt-contrib-glossary` are not installed anywhere
    in `src/components`, `src/extensions`, or `src/menu` in this project - so
    those two plugin directories are dead weight in the real compiled
    `adapt.css` here, not just unused by L1's naming.
  - Separately, **30 of 32** L1 components have their own
    `src/components/<dir>/less/` directory (Stage 2a, a different pipeline
    stage from vanilla's plugins entirely). Only `adapt-contrib-
    assessmentResults` and `adapt-contrib-text` do not; `adapt-contrib-text`
    gets no component-specific styling at any stage - it relies purely on
    the generic header-family mixins L1/L2 already describe.
  - Net: 10 components are styled at *both* Stage 2a (their own less) and
    Stage 2d (a vanilla plugin); 1 (`assessmentResults`) only at Stage 2d; 20
    only at Stage 2a with zero vanilla involvement; 1 (`text`) at neither.
    Mapping all 30+ files onto their resolved `_component` names and BEM
    roots (the same naming traps L1 already solved -
    `adapt-contrib-textInput` -> `textinput` etc.) is real work, deliberately
    left for its own layer rather than folded into this one.
