# Adapt framework shape: models, views, templates

You were right about the shape: there's a **model layer** (flat data + hierarchy logic), a **view layer** (DOM creation + two different template engines), and a **registry** that wires the two together. There is no `pageModel.json`/`page.schema.json` template — page/menu share `contentobject.schema.json`, and the "nesting" you're picturing from the JSON files isn't real nesting at all. That's the first thing to straighten out.

---

## 1. The data isn't a tree — it's a flat list joined by `_parentId`

`courses/<slug>/en/{contentObjects,articles,blocks,components}.json` are **flat arrays**. Every model type (`page`, `article`, `block`, `component`) carries `_parentId` (defined once, generically, in `content.schema.json:15-19` — the shared base schema article/block/component/contentobject all extend). Nothing in the schema or JSON expresses "children"; hierarchy is reconstructed at runtime by `AdaptModel.getChildren()`:

```js
// src/core/js/models/adaptModel.js:629-657
getChildren() {
  ...
  const id = this.get('_id');
  const children = data.filter(model => model.get('_parentId') === id); // ← the whole tree comes from this
  childrenCollection = new Backbone.Collection(children);
  ...
}
```

So "Content Object > Article > Block > Component" is a *lookup pattern*, not a data structure. `getParent()` (adaptModel.js:671-686) does the same thing in reverse via `data.findById(parentId)`.

## 2. The model class chain (what `_type`/`_component` resolves to)

```
LockingModel → AdaptModel  (adaptModel.js)      — generic tree/completion/locking logic, shared by everything
                 ├─ ContentObjectModel  (contentObjectModel.js)  → getTypeGroup() = 'contentobject'
                 │    └─ PageModel  (pageModel.js)  → getTypeGroup() = 'page'   [MenuModel is the sibling for menus]
                 ├─ ArticleModel   (articleModel.js)
                 ├─ BlockModel     (blockModel.js)
                 └─ ComponentModel (componentModel.js)  → hasManagedChildren = false (leaf)
                      └─ ItemsComponentModel (itemsComponentModel.js)  — for item-based components (mcq, matching...)
                           └─ (plugin's own Model, e.g. McqModel)

LockingModel → ItemModel (itemModel.js) — the _items[] inside an item-based component (not a real child model)
```

Each of page/article/block/component self-registers at the bottom of its file:

```js
// articleModel.js:32
components.register('article', { model: ArticleModel });
```

That line is the only place the string `'article'` gets tied to a class. `src/core/js/components.js` (the registry) stores it in `this._register['article'].model`.

`ItemsComponentModel.setUpItems()` (itemsComponentModel.js:37-42) is worth flagging separately: for components like MCQ, the `_items` array *is* genuinely nested JSON (not `_parentId`-joined), and gets wrapped into its own private `Backbone.Collection` of `ItemModel`s, parallel to but structurally different from the page/article/block/component mechanism.

## 3. Schemas mirror the model chain, additively

```
content.schema.json        — shared base (title, body, instruction, _classes, _isOptional, _onScreen, ...)
  contentobject.schema.json  — + page/menu-only fields
  article.schema.json        — + article-only fields
  block.schema.json          — + block-only fields
  component.schema.json      — + component-only fields (_component, _layout, _items, ...)
```

`verify-course.js` validates authored JSON against these — this is the thing checking that your `_parentId`s resolve and your fields are legal, before any of the runtime code below ever runs.

## 4. The view class chain — and this is where "classes/data-attributes" gets answered

```
Backbone.View → AdaptView (adaptView.js)
                  ├─ ContentObjectView (contentObjectView.js)
                  │    └─ PageView (pageView.js)        [childContainer: '.article__container']
                  ├─ ArticleView   (articleView.js)      [childContainer: '.block__container']
                  ├─ BlockView     (blockView.js)        [childContainer: '.component__container']
                  └─ ComponentView (componentView.js)     — leaf, no childContainer
```

**Classes and data-attributes are injected before any template runs at all**, by Backbone's own view-construction contract. Each class defines `className()` and `attributes()` as functions; Backbone calls `_.result(this, 'className')`/`attributes` when it creates `this.el`, *inside `new ChildView({model})`*, before `initialize()` even starts rendering.

```js
// componentView.js:16-28
className() {
  return [
    'component',
    this.model.get('_component').toLowerCase(),   // ← e.g. 'mcq'
    this.model.get('_id'),                          // ← e.g. 'c-05'
    this.model.get('_classes'),                      // ← author-set custom classes from JSON
    this.setVisibility(),                              // → 'u-visibility-hidden' or ''
    this.setHidden(),
    'is-' + this.model.get('_layout'),
    (this.model.get('_isComplete') ? 'is-complete' : ''),
    (this.model.get('_isOptional') ? 'is-optional' : '')
  ].join(' ');
}
```

```js
// adaptView.js:13-18 (base — every view gets this unless overridden)
attributes() {
  return {
    'data-adapt-id': this.model.get('_id'),   // ← the data-attribute
    role: 'presentation'
  };
}
```

`componentView.js:6-14` overrides `attributes()` further to add `aria-labelledby`/`role="region"` when `_isA11yRegionEnabled`. So: **wrapper element identity (tag, class list, ARIA/data attrs) = Backbone view construction. Inner HTML = template.** Two separate mechanisms, two separate moments.

## 5. Two template engines, split cleanly by level

`AdaptView.initialize()` (adaptView.js:20-52) decides which engine per-view:

```js
this.isJSX = (this.template || this.constructor.template || '').includes('.jsx');
```

- **page / article / block / menu** → `template: 'page'|'article'|'block'` (no `.jsx`) → **Handlebars**, precompiled from `src/core/templates/*.hbs` into the global `Handlebars.templates` map at build time:

  ```js
  // adaptView.js:60-71 (render())
  const data = this.model.toJSON();
  data.view = this;
  const template = Handlebars.templates[this.constructor.template];
  this.$el.html(template(data));
  ```

- **components** → `template: '<name>.jsx'` → **React**, via `changed()` (adaptView.js:90-109):

  ```js
  const Template = templates[(this.template || this.constructor.template).replace('.jsx', '')];
  ReactDOM.render(<Template {...props} />, this.el);
  ```

  `templates` here is the `export const templates = {}` registry in `src/core/js/reactHelpers.js:52`, populated at build time by `babel-plugin-transform-react-templates` calling `register(name, component)` (reactHelpers.js:9-24) for every `.jsx` file — the React equivalent of `components.register`.

**`html-react-parser`'s role**: Handlebars templates use `{{{compile body}}}` (triple-stash → raw HTML injection, see `page.hbs:43-46`, `article.hbs:30`, `block.hbs:30`, and `compile()` in `reactHelpers.js:70-73`, which literally runs `Handlebars.compile(template)(...)` from inside a JSX file to borrow Handlebars' helpers). React has no triple-stash equivalent, so JSX component templates that need to inject author-authored HTML strings (`body`, `instruction`, item text, etc.) parse them with `html-react-parser` (vendored at `src/core/libraries/html-react-parser.min.js`, the standard `remarkablemark/html-react-parser` package — it walks the HTML string into a DOM via `document.implementation.createHTMLDocument`/`DOMParser` and rebuilds it as real `React.createElement` nodes). It's excluded from the RequireJS/AMD bundle (`grunt/config/javascript.js:51`, mapped to `'empty:'`) because it ships through the separate React/Babel build path instead — that's why a direct `import ... from 'html-react-parser'` search in `src/` comes back empty in this checkout; it's consumed implicitly wherever a `.jsx` template needs raw-HTML-to-React, and mocked in `test/unit/__mocks__/html-react-parser.js` for tests.

## 6. How nesting actually becomes HTML: `childContainer` + `addChildren`

Each parent template leaves one **empty container div** for its children — that's the entire "injection point" contract between template and code:

```
page.hbs   → <div class="article__container">   (comment: "Articles render here")
article.hbs→ <div class="block__container">      (comment: "Blocks render here")
block.hbs  → <div class="component__container">   (comment: "Components render here")
```

And each view class declares which selector that is:

```js
Object.assign(PageView,    { childContainer: '.article__container',   type: 'page',    template: 'page'    });
Object.assign(ArticleView, { childContainer: '.block__container',     type: 'article', template: 'article' });
Object.assign(BlockView,   { childContainer: '.component__container', type: 'block',    template: 'block'   });
```

`AdaptView.addChildren()` (adaptView.js:156-215) is the recursive engine:

1. reads `model.getAvailableChildModels()` — i.e. the `_parentId` filter from step 1
2. resolves the correct view class via `components.getViewClass(model)` (components.js:102-114, which reads `_component` or `_type` off the model's JSON, components.js:65-95)
3. `new ChildView({ model })` → this synchronously runs *that child's own* `initialize → className/attributes → preRender → render → (deferred) postRender → addChildren` (the exact same cycle, one level down)
4. `addChildView()` (adaptView.js:225-245) appends the new child's `$el` into `this.$(this.constructor.childContainer)`

So "the page is built" is really: **PageView renders its own chrome around an empty `.article__container` → deferred tick → for each article model, build an ArticleView and drop it into that container → each ArticleView does the same into `.block__container` → down to ComponentView, which has no container and is a leaf.** Nothing waits for the whole tree before painting; each level defers its children by one `_.defer` tick, which is also why `ContentObjectView.isReady()` (contentObjectView.js:63-97) exists as a separate, later signal — it fires only once `_isReady` has bubbled true from the leaves back up (`AdaptModel.checkReadyStatus()`, adaptModel.js:269-285), which is the actual "fully built, fade in, hide loader" moment.

---

## One-paragraph summary

Flat JSON (validated against `content.schema.json` + per-level schema) is loaded into a flat `data` collection of model instances whose class is chosen by `components.getModelClass()` reading `_type`/`_component`; parent/child is a runtime filter on `_parentId`, not real nesting. Rendering walks that same relationship: Backbone assigns each view's wrapper element its classes/ARIA/data-attributes from `className()`/`attributes()` *before* any template runs; the wrapper's inner HTML then comes either from a precompiled Handlebars `.hbs` (page/article/block — static chrome plus `{{{compile body}}}` raw-HTML injection) or from a React `.jsx` template (components — using `html-react-parser` where it needs the Handlebars-style raw-HTML trick); and the actual page/article/block/component tree you see in the DOM is produced by each view recursively finding its `_parentId`-children, building the right child view via the `components` registry, and appending it into the single named `childContainer` div its own template left empty for that purpose.
