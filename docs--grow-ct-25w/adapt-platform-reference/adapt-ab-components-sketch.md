# adapt-ab-* component sketches - card, accordion, carousel, badge

Illustrative scaffolds for four Bootstrap-5-shaped building blocks, authored on
this theme's `--ab-*` tokens (no Bootstrap / `--bs-*` dependency). **Sketches to
review, not build-wired** - none are registered in `adapt.json` or installed yet.

Naming: the **new `adapt-ab-*` prefix** (component type `ab-card` etc.), per the
decision to migrate off `adapt-abbott-*` later. Patterns mirror the existing
`adapt-abbott-tabs` / `-flipcard` (ItemsComponentModel, `setupInviewCompletion`,
roving-tabindex ARIA, pure logic in a `*Logic.js`, JSX templates via
`core/js/reactHelpers`). Companion to `docs/adapt-extensibility-map.md` (§8 the
component contract) and `docs/adapt-dom-map.html`.

## Component or extension?

| Block | Verdict | Why |
|---|---|---|
| **card** | **Component** (`adapt-ab-card`) | block-level, its own content model (items), reuses the existing `.cm.card` LESS |
| **accordion** | **Component** (`adapt-ab-accordion`) | block-level, interactive, per-item visitation + completion |
| **carousel** | **Component** (`adapt-ab-carousel`) | block-level, interactive, per-slide visitation + completion |
| **badge** | **Style-only** (theme LESS) | inline, no content model, no completion - belongs *inside* prose, not as a block. Optional tiny extension only if you want auto-injection |

**The shared contract every component keeps** (from §8): the `.component` root +
state classes are core-owned; honour the completion signal
(`setupInviewCompletion` or all-items-visited), the a11y model, and
`trackable()`/`suspend_data`; namespace hooks (`ab-card__*`) and consume `--ab-*`
tokens. Everything below `.component__inner` is yours.

---

## 1. `adapt-ab-card` (component)

Reuses the existing `.cm.card` system (`ab-cards.less`). Presentational: renders
one or more cards; completion by inview (visible = done). One or many cards via
`_items`; wrapped in `.card-group` when more than one.

```
src/components/adapt-ab-card/
  bower.json
  properties.schema
  js/adapt-ab-card.js        # register
  js/CardModel.js            # ComponentModel (presentational)
  js/CardView.js             # ComponentView (inview completion)
  templates/card.jsx         # emits .cm.card markup
  less/ab-card.less          # thin: layout only; visuals come from .cm.card
```

**js/adapt-ab-card.js**
```js
import components from 'core/js/components';
import CardView from './CardView';
import CardModel from './CardModel';

export default components.register('ab-card', { view: CardView, model: CardModel });
```

**js/CardModel.js**
```js
import ComponentModel from 'core/js/models/componentModel';

export default class CardModel extends ComponentModel {
  defaults() {
    return { ...super.defaults(), _variant: 'neutral', _isGroup: false };
  }
  hasAnyGraphics() {
    return (this.get('_items') || []).some(i => i._graphic && i._graphic.src);
  }
}
```

**js/CardView.js**
```js
import ComponentView from 'core/js/views/componentView';

class CardView extends ComponentView {
  postRender() {
    if (this.model.hasAnyGraphics()) {
      this.$('.ab-card__group').imageready(this.setReadyStatus.bind(this));
    } else {
      this.setReadyStatus();
    }
    this.setupInviewCompletion('.component__widget'); // presentational: inview = complete
  }
}
CardView.template = 'card.jsx';
export default CardView;
```

**templates/card.jsx**
```jsx
import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

export default function Card(props) {
  const items = props._items || [];
  const isGroup = items.length > 1 || props._isGroup;
  return (
    <div className="component__inner ab-card__inner">
      <templates.header {...props} />
      <div className="component__widget ab-card__widget">
        <div className={classes(['ab-card__group', isGroup && 'card-group'])}>
          {items.map((item, i) => <AbCard key={item._id || i} item={item} />)}
        </div>
      </div>
    </div>
  );
}

function AbCard({ item }) {
  const g = item._graphic || {};
  const link = item._link || {};
  return (
    <div className={classes(['cm', 'card', item._variant, item._withIcon && 'with-icon'])}>
      {g.src && <img className="card-img-top" src={g.src} alt={g.alt || ''} />}
      {item.header && <div className="card-header">{item.header}</div>}
      <div className="card-body">
        {item.title && <h3 className="card-title">{item.title}</h3>}
        {item.subtitle && <div className="card-subtitle">{item.subtitle}</div>}
        {item.text && <div className="card-text" dangerouslySetInnerHTML={{ __html: compile(item.text) }} />}
        {link.url && <a className="card-link" href={link.url}>{link.text || link.url}</a>}
      </div>
      {item.footer && <div className="card-footer">{item.footer}</div>}
    </div>
  );
}
```

**properties.schema** (key fields)
```jsonc
{
  "type": "object",
  "$schema": "http://json-schema.org/draft-04/schema",
  "id": "http://jsonschema.net",
  "$ref": "http://localhost/plugins/content/component/model.schema",
  "globals": {
    "ariaRegion": { "type": "string", "required": true,
      "default": "Information cards.", "inputType": "Text", "translatable": true }
  },
  "properties": {
    "_variant": { "type": "string", "default": "neutral",
      "enum": ["neutral","accent","do","dont","advice","action","starting","feedback-pos","feedback-neg"],
      "title": "Card variant", "inputType": { "type": "Select",
      "options": ["neutral","accent","do","dont","advice","action","starting","feedback-pos","feedback-neg"] } },
    "_items": { "type": "array", "required": true, "title": "Cards",
      "items": { "type": "object", "properties": {
        "_id":      { "type": "string", "default": "" },
        "_variant": { "type": "string", "default": "", "help": "Per-card override of the component variant." },
        "header":   { "type": "string", "default": "", "translatable": true },
        "title":    { "type": "string", "default": "", "translatable": true },
        "subtitle": { "type": "string", "default": "", "translatable": true },
        "text":     { "type": "string", "default": "", "inputType": "TextArea", "translatable": true },
        "footer":   { "type": "string", "default": "", "translatable": true },
        "_withIcon":{ "type": "boolean", "default": false },
        "_graphic": { "type": "object", "properties": {
          "src": { "type": "string", "inputType": "Asset:image" },
          "alt": { "type": "string", "translatable": true } } },
        "_link":    { "type": "object", "properties": {
          "text": { "type": "string", "translatable": true },
          "url":  { "type": "string" } } }
      } } }
  }
}
```

**Emitted DOM:** `.component.ab-card > .component__inner.ab-card__inner > header +
.component__widget.ab-card__widget > .ab-card__group(.card-group) > .cm.card.<variant>`
then the `.card-*` parts. Visuals entirely from `ab-cards.less`; `ab-card.less`
only handles group layout.

**Contract:** presentational -> `setupInviewCompletion`; no interaction tracking
needed. `.cm.card` already consumes `--ab-card-*` tokens.

---

## 2. `adapt-ab-accordion` (component)

Bootstrap-accordion-shaped. Interactive: panels expand/collapse; **completion when
every panel has been opened** (visitation, like `flipcard`/`tabs`). Single-open
(`data-bs-parent` behaviour) or multi-open.

```
src/components/adapt-ab-accordion/
  bower.json  properties.schema
  js/adapt-ab-accordion.js  js/AccordionModel.js  js/AccordionView.js
  js/accordionLogic.js      templates/accordion.jsx  less/ab-accordion.less
```

**js/AccordionModel.js** (mirrors TabsModel: ItemsComponentModel + visitation)
```js
import ItemsComponentModel from 'core/js/models/itemsComponentModel';

export default class AccordionModel extends ItemsComponentModel {
  defaults() {
    return { ...super.defaults(), _isMultiSelect: false, _shouldExpandFirst: false };
  }
  init() {
    super.init();
    if (this.get('_shouldExpandFirst')) this.toggleItem(0, true);
  }
  toggleItem(index, forceOpen) {
    const item = this.getItem(index);
    if (!item) return;
    const open = (typeof forceOpen === 'boolean') ? forceOpen : !item.get('_isOpen');
    if (!this.get('_isMultiSelect') && open) {
      this.getChildren().forEach(c => c.set('_isOpen', false)); // single-open
    }
    item.set('_isOpen', open);
    if (open && !item.get('_isVisited')) item.set('_isVisited', true); // completion feed
  }
}
```

**js/AccordionView.js**
```js
import ComponentView from 'core/js/views/componentView';

class AccordionView extends ComponentView {
  events() { return { 'click .ab-accordion__header-btn': 'onHeaderClick' }; }
  preRender() { this.listenTo(this.model.getChildren(), 'change:_isOpen', this.changed); }
  postRender() { this.setReadyStatus(); this.setupInviewCompletion('.component__widget'); }
  onHeaderClick(e) {
    const index = this.$(e.currentTarget).data('index');
    if (typeof index === 'number') this.model.toggleItem(index);
  }
}
AccordionView.template = 'accordion.jsx';
export default AccordionView;
```

**templates/accordion.jsx** (Bootstrap accordion ARIA: button + aria-expanded +
aria-controls; region aria-labelledby)
```jsx
import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

export default function Accordion(props) {
  const items = props._items || [];
  const cid = props._id;
  return (
    <div className="component__inner ab-accordion__inner">
      <templates.header {...props} />
      <div className="component__widget ab-accordion__widget">
        <div className="cm accordion">
          {items.map((item, i) => {
            const hid = `${cid}-h-${i}`, pid = `${cid}-p-${i}`, open = !!item._isOpen;
            return (
              <div className="accordion-item" key={item._id || i}>
                <h3 className="accordion-header" id={hid}>
                  <button type="button"
                    className={classes(['accordion-button', 'ab-accordion__header-btn', !open && 'collapsed'])}
                    data-index={i} aria-expanded={open.toString()} aria-controls={pid}>
                    {item.title}
                  </button>
                </h3>
                <div id={pid} role="region" aria-labelledby={hid}
                  className={classes(['accordion-collapse', open ? 'show' : 'collapse'])}>
                  <div className="accordion-body"
                    dangerouslySetInnerHTML={{ __html: compile(item.body) }} />
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
```

**properties.schema** (key fields): `_isMultiSelect` (bool), `_shouldExpandFirst`
(bool), `_items[]` of `{ _id, title (Text, translatable), body (TextArea,
translatable) }`, plus the `ariaRegion` global.

**Emitted DOM:** `.cm.accordion > .accordion-item > (.accordion-header >
button.accordion-button[.collapsed]) + (.accordion-collapse.show|collapse >
.accordion-body)`.

**Contract:** completion when all panels opened (visitation via `_isVisited`);
ARIA accordion pattern (button `aria-expanded`/`aria-controls`, panel
`role="region"` + `aria-labelledby`); no auto-collapse that moves focus.
`ab-accordion.less` consumes `--ab-*` (reuse `--ab-card-cap-bg`, `--ab-base-*`).

---

## 3. `adapt-ab-carousel` (component)

Bootstrap-carousel-shaped. Interactive: prev/next + indicators; **completion when
every slide has been viewed**. Auto-rotate **off by default** (accessibility +
completion reliability).

```
src/components/adapt-ab-carousel/
  bower.json  properties.schema
  js/adapt-ab-carousel.js  js/CarouselModel.js  js/CarouselView.js
  js/carouselLogic.js      templates/carousel.jsx  less/ab-carousel.less
```

**js/CarouselModel.js**
```js
import ItemsComponentModel from 'core/js/models/itemsComponentModel';

export default class CarouselModel extends ItemsComponentModel {
  defaults() {
    return { ...super.defaults(), _activeIndex: 0, _shouldAutoScroll: false, _canCycle: true };
  }
  init() {
    super.init();
    const first = this.getItem(0);
    if (first && !first.get('_isVisited')) first.set('_isVisited', true);
  }
  goTo(index) {
    const n = this.getChildren().length;
    const i = this.get('_canCycle') ? ((index % n) + n) % n : Math.max(0, Math.min(n - 1, index));
    this.set('_activeIndex', i);
    const item = this.getItem(i);
    if (item && !item.get('_isVisited')) item.set('_isVisited', true);
  }
  next() { this.goTo(this.get('_activeIndex') + 1); }
  prev() { this.goTo(this.get('_activeIndex') - 1); }
}
```

**js/CarouselView.js**
```js
import ComponentView from 'core/js/views/componentView';

class CarouselView extends ComponentView {
  events() {
    return {
      'click .ab-carousel__prev': 'onPrev',
      'click .ab-carousel__next': 'onNext',
      'click .ab-carousel__indicator': 'onIndicator'
    };
  }
  preRender() { this.listenTo(this.model, 'change:_activeIndex', this.changed); }
  postRender() {
    if (this.model.hasAnyGraphics?.()) this.$('.carousel-inner').imageready(this.setReadyStatus.bind(this));
    else this.setReadyStatus();
    this.setupInviewCompletion('.component__widget');
  }
  onPrev() { this.model.prev(); }
  onNext() { this.model.next(); }
  onIndicator(e) { this.model.goTo(this.$(e.currentTarget).data('index')); }
}
CarouselView.template = 'carousel.jsx';
export default CarouselView;
```

**templates/carousel.jsx** (carousel ARIA: `aria-roledescription="carousel"`,
slides `role="group" aria-roledescription="slide"`, controls are real buttons,
non-current slides `aria-hidden`)
```jsx
import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

export default function Carousel(props) {
  const items = props._items || [];
  const active = props._activeIndex || 0;
  return (
    <div className="component__inner ab-carousel__inner">
      <templates.header {...props} />
      <div className="component__widget ab-carousel__widget">
        <div className="cm carousel" aria-roledescription="carousel" aria-label={props.ariaRegion}>
          <div className="carousel-inner" aria-live={props._shouldAutoScroll ? 'off' : 'polite'}>
            {items.map((item, i) => {
              const g = item._graphic || {};
              const isActive = i === active;
              return (
                <div key={item._id || i} role="group" aria-roledescription="slide"
                  aria-label={`${i + 1} of ${items.length}`} aria-hidden={(!isActive).toString()}
                  className={classes(['carousel-item', isActive && 'active'])}>
                  {g.src && <img className="d-block w-100" src={g.src} alt={g.alt || ''} />}
                  {(item.title || item.caption) && (
                    <div className="carousel-caption">
                      {item.title && <h3>{item.title}</h3>}
                      {item.caption && <div dangerouslySetInnerHTML={{ __html: compile(item.caption) }} />}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
          <button type="button" className="carousel-control-prev ab-carousel__prev">
            <span className="carousel-control-prev-icon" aria-hidden="true" />
            <span className="visually-hidden">Previous</span>
          </button>
          <button type="button" className="carousel-control-next ab-carousel__next">
            <span className="carousel-control-next-icon" aria-hidden="true" />
            <span className="visually-hidden">Next</span>
          </button>
          <div className="carousel-indicators">
            {items.map((item, i) => (
              <button key={i} type="button" data-index={i}
                className={classes(['ab-carousel__indicator', i === active && 'active'])}
                aria-current={(i === active).toString()} aria-label={`Slide ${i + 1}`} />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
```

**properties.schema** (key fields): `_shouldAutoScroll` (bool, default false),
`_canCycle` (bool, default true), `_items[]` of `{ _id, title, caption
(TextArea), _graphic { src (Asset:image), alt } }`, plus `ariaRegion`.

**Emitted DOM:** `.cm.carousel[aria-roledescription] > .carousel-inner >
.carousel-item(.active) > img + .carousel-caption`, then `.carousel-control-prev/next`
and `.carousel-indicators > button`.

**Contract:** completion when all slides visited; auto-rotate default off (if on,
needs pause control + `aria-live="off"`); controls are buttons; non-current slides
`aria-hidden`. `ab-carousel.less` consumes `--ab-*`.

---

## 4. `badge` - style-only (theme LESS), not a component

A badge is **inline** - it sits inside a heading or sentence (`<span class="cm badge">`).
It has no content model and no completion, so a block-level component is the wrong
shape. Make it a **theme partial** (`ab-badge.less`), authored inline in any rich-text
`body` field - exactly how `.cm.card` / `.cm.btn` already work.

**Class contract** (Bootstrap-5-shaped, on `--ab-*` tokens):
```
.cm.badge                          /* base: inline pill/label */
.cm.badge.<palette>                /* colour variants: teal, amethyst … */
.cm.badge.accent                   /* scheme accent */
.cm.badge.do / .dont / .advice …   /* functional, matching the card/callout set */
.cm.badge.rounded-pill             /* pill shape */
.cm.badge.soft                     /* tinted (bg = colour @ low alpha), like we-*-tint */
```

**Authored inline:**
```html
<p>Referencing style <span class="cm badge accent">Harvard</span></p>
<h3 class="block__title">Assessment <span class="cm badge rounded-pill advice">formative</span></h3>
```

**LESS sketch** (reuses the spine tokens; add to the theme, not a component):
```less
.cm.badge {
  --ab-badge-bg: var(--ab-base-surface-sunken, #eee);
  --ab-badge-color: var(--ab-base-ink, #1a1a1a);
  display: inline-block; padding: 0.25em 0.6em; font-size: 0.78em; font-weight: 600;
  line-height: 1; border-radius: var(--ab-border-radius, 0.375rem);
  background: var(--ab-badge-bg); color: var(--ab-badge-color); vertical-align: baseline;
}
.cm.badge.rounded-pill { border-radius: 10rem; }
.cm.badge.accent { --ab-badge-bg: var(--ab-accent); --ab-badge-color: var(--ab-on-accent, #fff); }
.cm.badge.soft.accent { --ab-badge-bg: rgba(var(--ab-accent-rgb), 0.12); --ab-badge-color: var(--ab-accent); }
/* do/dont/advice… map to the same semantic colours as .cm.card variants */
```

**When a tiny extension *would* earn its place:** only if you want authoring
sugar - e.g. an extension that rewrites a token like `[[badge:Harvard|accent]]`
in body text into the markup, or auto-appends a status badge to blocks carrying a
`_classes` flag. That is a `tooltip`-style post-processor, not core to the badge
itself. Default recommendation: **ship the LESS, author inline, skip the extension.**

---

## Next steps if you want these real (not just sketched)

1. Create the dirs above, add each `bower.json` (`"component": "ab-card"`,
   `"targetAttribute": "_abCard"`, `"framework": ">=5.19.1"`).
2. `npm run adapt-install` (never raw `adapt install`) so vendor patches reapply.
3. Add `ab-badge.less` to the theme (coordinate with the theming agent - theme
   files are their branch).
4. Verify completion + a11y empirically: `grunt server-scorm` for completion
   behaviour, the a11y scan (`test-accessibility-scan.mjs`) for the ARIA patterns.
5. Register in `design-kb/design-kb.palette.json` so `/gate` can route to them.
