# Adapt extensibility map - page to component

What each layer of the Adapt content tree is made of, the DOM and the hooks it
exposes, and exactly how far we can bend it: (a) our own style classes, (b) our
own metadata, (c) an `.<container>.abbott` view layer of our own.

Companion to `docs/ARCHITECTURE.md` (what lives where in *this* repo) and
`docs/PIPELINE.md` (the authoring flow). This file is about the **framework**
underneath, not our pipeline.

## Provenance of the claims below

Two confidence levels are flagged throughout, because they come from two places:

- **[repo]** - confirmed by reading our own code in `src/components/adapt-abbott-*`
  and `src/extensions/adapt-abbott-*`. These are certain.
- **[core]** - the standard `adapt-contrib-core` API. The core submodule
  (`src/core`, pinned to `adapt-contrib-core` **v6.77.1**) is **not checked out**
  in this workspace, so these are reconstructed from the stable core API and
  should be re-verified against `src/core/js` once the submodule is initialised.
  They mostly concern the block/article/page layers, which we do not currently
  subtype.

Framework: `adapt_framework` 5.56.2. Our components declare `"framework": ">=5.19.1"`. [repo]

---

## 1. The tree, layer by layer

Course > Content Object (menu/page) > Article > Block > Component. Authored as
JSON under `courses/<slug>/en/`; each element has a unique `_id` and a
`_parentId` into the layer above.

| Layer | JSON source | Core model base [core] | Core view base [core] | DOM element (standard) [core] |
|---|---|---|---|---|
| Course | `course.json` | `CourseModel` | `AdaptView` (root) | `#wrapper` |
| Content Object: **menu** | `contentObjects.json` (`_type:"menu"`) | `MenuModel` | `MenuView` (pluggable) | `.menu` |
| Content Object: **page** | `contentObjects.json` (`_type:"page"`) | `PageModel` | `PageView` | `.page` |
| Article | `articles.json` | `ArticleModel` | `ArticleView` | `.article` |
| Block | `blocks.json` | `BlockModel` | `BlockView` | `.block` |
| Component | `components.json` | `ComponentModel` (and subclasses) | `ComponentView` | `.component` |

The asymmetry that governs everything in section 4: **only the component layer
has a type discriminator.** A component says `"_component": "flipcard"` and core
looks up whatever was registered under that name. A block is just a block; an
article is just an article. There is no `"_block": "..."` selector in stock
core. [core]

---

## 2. What each element emits into the DOM (the class/id surface)

Two kinds of class land on every element's wrapper:

1. **Core-emitted, automatic** [core] - the element type (`component`,
   `block`, `article`...), the component type as a class (e.g. `flipcard`), the
   model `_id` as the element `id`, `data-adapt-id` / `data-component`
   attributes, and **state classes** toggled at runtime (`is-complete`,
   `is-visited`, `is-locked`, `is-disabled`, `is-optional`, `is-hidden`...).
2. **Author-supplied, from JSON** - whatever we put in the `_classes` string on
   that element. Core appends it verbatim to the wrapper. This is the primary,
   zero-code styling hook and it exists at **every** layer. [core]

Inside the component, the template emits its own **BEM** classes, and these are
fully ours to define. Confirmed from `templates/flipcard.jsx` [repo]:

- Structural classes the theme expects: `component__inner`, `component__widget`.
- Our own namespace: `flipcard__inner`, `flipcard__cards`, `flipcard__card`,
  `flipcard__face--front`, `flipcard__title--back`, etc.
- Conditional state classes via the `classes([...])` helper from
  `core/js/reactHelpers`:
  `classes(['flipcard__card-container', isFlipped && 'is-flipped', isVisited && 'is-visited'])`.

Course-wide, `_htmlClasses` in `config.json` puts classes on `<html>` (we
already gate the dev theme switcher behind one: `cm-theme-switch`). [repo]

---

## 3. The lifecycle hooks each layer gives us

All views are Backbone views, so every layer exposes `events()`, `initialize`,
`listenTo`, `render`, `remove`, and the Adapt render lifecycle. Confirmed from
`FlipcardView.js` and `FlipcardModel.js` [repo]; the same surface exists on the
block/article/page views in core [core].

**View hooks** (what we override in `*View.js`):

| Hook | When | We use it for |
|---|---|---|
| `events()` | binding | delegated DOM events, e.g. `'click .flipcard__card': 'onCardClick'` [repo] |
| `preRender()` | before template | wire `listenTo` on child models before first paint [repo] |
| `postRender()` | after template in DOM | image-ready waits, `setupInviewCompletion('.component__widget')`, `setReadyStatus()` [repo] |
| `changed()` | re-render | re-render the React template when model state changes [repo] |
| `setCompletionStatus()` / inview | completion | mark the element complete (feeds tracking) [core] |

**Model hooks** (what we override in `*Model.js`):

| Hook | Purpose |
|---|---|
| `defaults()` | default field values, e.g. `_flipBehaviour: 'independent'` [repo] |
| `init()` / `setUpItems()` | derive runtime state from JSON [core] |
| `trackable()` | **declares which fields enter `suspend_data`** - the SCORM persistence contract. `_isFlipped` is deliberately excluded so transient UI state never serialises [repo] |
| `checkIfResetOnRevisit()` | reset behaviour on page revisit [repo] |
| `getChildren()` / `getItem()` | child model access [repo] |

**Registration** - one line, from `core/js/components` [repo]:

```js
import components from 'core/js/components';
export default components.register('flipcard', { view: FlipcardView, model: FlipcardModel });
```

Template is bound on the view class: `FlipcardView.template = 'flipcard.jsx'` [repo].
Extensions register differently - see `adapt-abbott-theme/js/adapt-abbott-theme.js`,
which is a style-only extension that ships committed LESS and an optional,
flag-gated runtime switcher [repo].

---

## 4. The three questions, answered

### (a) Can we add our own style classes? - YES, fully, no caveats

Three independent routes, all already available:

1. **`_classes` on any element** (course / menu / page / article / block /
   component) - appended to that element's wrapper by core. No code. [core]
2. **BEM classes inside our component templates** - entirely ours; we already
   run a `flipcard__*` / `is-*` namespace. [repo]
3. **Theme LESS** - `adapt-abbott-theme` ships programme-wide styling
   (`cm-palette`, `cm-schemes`, `cm-cards`, `cm-font-themes`...) that compiles
   with every build while vanilla stays the base theme. [repo]

Verdict: this is the framework working as designed. Nothing to build.

### (b) Can we add our own metadata structures? - YES, with one distinction

Any key we add to an element's JSON is set on its Backbone model and readable
via `model.get('...')`. Core ignores keys it does not recognise, so **arbitrary
metadata rides along for free** at every layer. What the `properties.schema`
buys us on top (confirmed from `flipcard/properties.schema` [repo]):

- **Validation + authoring-tool UI** - `inputType`, `title`, `help`,
  `validators`, `enum`, `default`, `translatable`, `editorOnly`.
- **`globals`** (e.g. `ariaRegion`) and `$ref` to the core
  `component/model.schema` so our fields extend the base contract rather than
  replace it.
- **`targetAttribute`** in `bower.json` (`"_flipcard"`) namespaces the
  component's config block. [repo]

The distinction: metadata that only *we* read (our tooling, `verify-course.js`,
analytics) needs **no schema** - just put it on the JSON. Metadata that must be
**validated**, **authored in a GUI**, or **round-tripped by the Adapt Authoring
Tool** needs a schema entry. For our pipeline (JSON authored by agents, validated
by our own tools) we can define whatever metadata structures we like; the schema
is optional rigour, not a gate.

Caveat: keep custom keys from colliding with reserved core keys (`_id`,
`_parentId`, `_type`, `_component`, `_classes`, `_isOptional`, ...). Namespace
ours (e.g. `_abbott` or our `targetAttribute`) to stay clear.

### (c) Can we create an `.<container>.abbott` view layer? - YES for components and menus; NOT as types for blocks/articles

First, separate two senses of "`.abbott`":

- **The registered *type* name** - the functional identity core routes on
  (`'flipcard'`). This is what makes a new view selectable per-instance.
- **The `.abbott` *CSS/package namespace*** - presentational, carried by the
  package name (`adapt-abbott-flipcard`), the `_classes`, and the theme LESS.

Our existing `.abbott` layer today is already: 12 custom **components**
(`adapt-abbott-annotated/branching/checklist/confidence/flipcard/glossary/
modal/opentext/references/sortable/tabs/timeline`) + 5 **extensions**
(`pass-reveal`, `reflective-store`, `resultsdebrief`, `theme`, `tooltip`). [repo]

How far the "own view layer" idea reaches per layer:

| Layer | Own selectable `.abbott` view? | Mechanism |
|---|---|---|
| **Component** | **Yes, unlimited** | `components.register('abbott-x', {view, model})`; selected per instance via `_component`. This is our real adaptation surface. [repo] |
| **Menu** | **Yes** | menu plugins register a named view; selected via `_menu` in config/CO. [core] |
| **Page (content object)** | **Yes, in practice** | custom content-object view via an extension/menu-style plugin. [core] |
| **Article** | **No type registry** | one `ArticleView` globally. Vary by `_classes` + theme, or replace the global view wholesale from an extension. [core] |
| **Block** | **No type registry** | same as article. [core] |

So a true `.block.abbott` / `.article.abbott` **type** does not exist in stock
core - there is no `_block`/`_article` selector to hang it on. The three
sanctioned ways to get "Abbott-flavoured" structure at those layers:

1. **Push the custom rendering down into a component.** The component is the
   open registry; a block/article is just its frame. This is the idiomatic
   answer and what we already do.
2. **`_classes` + theme LESS** to restyle the stock block/article frame per
   instance (zero code).
3. **Override the global `BlockView`/`ArticleView`** from an extension (like how
   core extensions augment views). This changes *every* block/article, not a
   selectable subtype, and needs verification against `src/core` v6.77.1 before
   relying on it. [core]

---

## 5. Bottom line

- **Styling (a):** unlimited, three routes, already in use.
- **Metadata (b):** unlimited on the model; schema only where we want validation
  or GUI authoring.
- **View layer (c):** unlimited at the **component** layer (our real surface) and
  available at the **menu/page** layer; the **block/article** layers are framed,
  not subtyped - adapt them via components, classes/theme, or a global view
  override, not via a `.abbott` block *type*.

The practical shape of an "Abbott view layer" is therefore: **custom components +
custom menu/page views + the theme extension + `_classes`/metadata conventions**
- which is largely what `src/components/adapt-abbott-*` and
`src/extensions/adapt-abbott-*` already are. The ceiling we would hit trying to
go further is the block/article type registry that core simply does not provide.

---

## 6. The styling stack and where the `--ab-*` theme plugs in

Styling is a separate axis from the view/type question above. The theme
(`adapt-abbott-theme`, the `--ab-*` system) and the building blocks (our
components) are two layers joined by one contract.

### The layer stack (bottom to top)

```
building blocks  (adapt-abbott-* components)        <- structure + behaviour
     owns: BEM boxes (flipcard__face), layout, state styling (is-flipped)
     consumes: --ab-* tokens for every visual value
  -------------------- the contract: class hooks + --ab-* tokens --------------------
theme            (adapt-abbott-theme, html.ab-theme) <- skin
     owns: palette -> semantic family -> --ab-base-<role> -> --ab-base-if-adapt-*,
           type scale, hierarchy-tied spacing, schemes, light/dark, vanilla overrides
vanilla          (adapt-contrib-vanilla)             <- base, untouched
```

Confirmed on the theming branch (`claude/laughing-gates-ylnn7z`): the token
system is fully `--ab-*` (0 `--cm-*` variables remain; ~400 `--ab-*` tokens),
with an **`--ab-base-if-adapt-*` adapter layer** (the seam that maps our tokens
onto Adapt's own internals, e.g. `--ab-base-if-adapt-item-color-selected`,
`-validation-error`, `-hairline`). The theme scopes its rules under
`html.ab-theme`. [repo]

### The contract (identical at every tier)

Three things combine to style any element, and they are the same from course to
component:

1. **Core structural class** (automatic): `.article`, `.article__title`,
   `.block`, `.component`, `.component__title`, `.component__body`. [core]
2. **Author `_classes` modifier** (per instance, from JSON): e.g.
   `article--abbott-x`. Appended to the wrapper by core. [core]
3. **Theme selector consuming tokens**:
   `html.ab-theme .article--abbott-x { ... var(--ab-...) }`. [repo]

So the plug-in point is the same at every layer: **structural class + `_classes`
modifier -> themed selector reading `--ab-*`**. Building blocks *emit* the hooks;
the theme *paints* them; neither side edits the other's files. The division of
labour is **structure (blocks) vs skin (theme)**, and the contract between them
is **class names + the `--ab-*` token vocabulary**.

### How theming plugs into each layer

| Layer | Class hooks it emits | Theme plugs in via |
|---|---|---|
| Page | `.page`, `.page__title`, `.page__inner` + `_htmlClasses` root (`ab-theme`) | root scope + page selectors |
| Article | `.article`, `.article__title`, `.article__inner` + `_classes` | `html.ab-theme .article--x` |
| Block | `.block`, `.block__title`, `.block__inner` + `_classes` | `html.ab-theme .block--x` |
| Component | `.component`, `.component__title`, `.component__body` + the component's own BEM classes | component LESS reading `--ab-*`; theme for shared surfaces |

One rule keeps the seam clean: **component LESS consumes `--ab-*` tokens, never
defines a palette or hardcodes a hex.** Where a block needs a value with no
token, add a *semantic* `--ab-*` token in the theme rather than inventing a
colour in component LESS. Unlike the theme-over-vanilla layer (which needs
`!important` to beat vanilla), our component LESS styles our own low-specificity
classes and needs none.

---

## 7. Can we create a whole new `article.abbott` and plug the theme into it?

**Yes - and we already do.** Our courses carry articles classed
`article--lesson-open / -concept / -formative / -reflection / -close`, and the
theme styles them (`[class*="article--lesson-"] .article__title { ...
var(--ab-...) }`). That is a custom article *format* with the theme plugged in,
built entirely from `_classes` + themed selectors, no core changes. [repo]

The rule is **format vs type**:

- **Format (own classes + own styling): YES at every layer.** Author the article
  with `_classes: "article--abbott"`, then theme
  `html.ab-theme .article--abbott { ... var(--ab-...) }`. Full control over
  layout, spacing, rhythm, borders, backgrounds, heading treatment of the article
  and its children. Zero core edits. Same pattern for `block--abbott`.
- **Type (own markup / own template): only at the component (and menu/page)
  layer.** Core gives the article **no swappable per-type template** - the
  `.article > .block > .component` wrapper markup is fixed. [core]

**The one boundary:** if "new structure" means *different HTML inside the article
wrapper*, that does not come from the article - it comes from the **components**
placed inside it (components have their own `.jsx`). A custom `article.abbott` is
therefore **custom `_classes` + theme rules + the components it contains**, not a
custom article template. The only route to bespoke article DOM is overriding the
global `ArticleView`, which affects *every* article - a structural decision, not
a per-variant one, and best avoided. [core]

So: style and lay out a whole new `article.abbott` and wire the `--ab-*` system
into it freely (that is the `article--lesson-*` pattern generalised); put any
genuinely new *markup* one tier down, in a component.

---

## 8. Inside a component: what's unlimited vs the contract you keep

The component is the one layer where core hands you a blank template. Below
`.component__inner` the markup is **entirely yours** - this is why components, not
articles/blocks, are the real extensibility surface.

**Unlimited (inside `.component__inner`):**

- any nested divs, any depth;
- as many class hooks as you like - your own BEM namespace (`mycomp__*`), state
  classes (`is-*`), modifiers;
- any `data-*` attributes, any ARIA;
- you need not use the header partial (`<templates.header>`) at all - render your
  own title/body markup instead;
- sub-components, and any JS mounted in `postRender` (a React subtree, D3, canvas,
  a whole mini-app); any schema fields you define arrive as props. [repo]

**The fixed frame (add to it, don't erase it):** the outer `.component` root is
created by core's `ComponentView` and carries `.component` + the type class +
**state classes** (`is-complete`, `is-visited`, `is-disabled`...) + your
`_classes`. Those state classes are how tracking / inview / completion hook in,
so you extend the root, you don't strip it. Your freedom starts at
`.component__inner`. [core]

**The contract (honour it or SCORM/a11y break):**

- the completion signal (`setReadyStatus`, inview / completion);
- accessibility (the `js-heading` aria-level, focus handling, native control
  semantics);
- `trackable()` / `suspend_data` for any state that must persist across revisits.

**Two styling rules:** namespace your hooks (`mycomp__*`) so they never clash with
core/theme; and component LESS **consumes `--ab-*` tokens, never hardcodes a
palette** (the §6 seam).

A component is still a **leaf**: you can build any world inside it, but you cannot
reshape the article/block frame around it. "Go mad" means *inside the component
boundary* - unlimited markup and hooks there, with the completion + a11y + tracking
contract still satisfied.

See `docs/adapt-dom-map.html` for this drawn out: the same outer frame around two
components - a `text` component (header partial only) and a card component whose
`.component__widget` holds the `.cm.card` object (the token-based Bootstrap-5-shaped
card system in `ab-cards.less`).

---

## To verify next (when `src/core` is checked out)

1. Exact auto-emitted wrapper classes and `data-*` attributes per layer
   (`src/core/js/views/*View.js`).
2. Whether v6.77.1 exposes any per-instance block/article view override beyond
   `_classes` (search `registerView` / view-swap hooks in core).
3. The reserved-key list, to finalise our custom-metadata namespace.
