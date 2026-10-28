# adapt-ab-navigation

An **interface/adapter** over the whole core **navigation bar** (the
`role="navigation"` `.nav` region and its `.nav__inner`). It is an **extension**,
not a component — the nav bar is a core shell region rendered once for the course,
so a content-tree component can't be it. This overlays the core-generated bar on
every view. Pairs with `adapt-ab-navbtn` (per-button hook + click events).

## Enable

Zero-config: enabled unless disabled. In `course.json`:

```json
"_abNavigation": { "_isEnabled": true }
```

## 1. Restyle seam

Stamps a stable **`.ab.navigation`** compound hook on `.nav`; `ab-navigation.less`
styles the bar + layout under that hook, from level-3 tokens:

| Token | Default |
|---|---|
| `--ab-base-navigation-bg` | `var(--ab-accent)` |
| `--ab-base-navigation-color` | `var(--ab-on-accent)` |
| `--ab-base-navigation-min-height` | `3.5rem` |
| `--ab-base-navigation-padding-x` | `var(--ab-space-100)` |
| `--ab-base-navigation-gap` | `var(--ab-space-050)` |
| `--ab-base-navigation-max-width` | `100%` |

## 2. Data layer

- Mirrors the responsive label mode onto **`data-ab-nav-labels`** on `.nav`.
- Emits **`abNavigation:ready`** `(navEl, { buttons, labelMode })`, where
  `buttons` is the inventory `{ event, name, label, order }` of every `.nav__btn`.

```js
import Adapt from 'core/js/adapt';
Adapt.on('abNavigation:ready', (nav, info) => {
  // info.buttons, info.labelMode
});
```

## 3. Add layers (custom nav items)

Inject your own nav items into `.nav__inner`, ordered by `data-order`:

```json
"_abNavigation": {
  "_isEnabled": true,
  "_items": [
    { "label": "Glossary", "_icon": "icon-search", "_order": 95, "_abModal": "glossary" },
    { "label": "Home", "_icon": "icon-home", "_order": 85, "_url": "#/" },
    { "label": "Help", "_icon": "icon-help", "_order": 96, "_event": "myCustomEvent" }
  ]
}
```

Each item renders as `<button class="btn-icon nav__btn ab-navitem">` (or `<a>` for
a `_url`) and can:

- **open an adapt-ab-modal** via `_abModal` (emits `data-ab-modal`),
- **fire a core `data-event`** via `_event` (only acts if a handler exists),
- **link** via `_url`.

Items are inserted by `_order` among the existing nav buttons (skip `-100`,
back `0`, progress `90`, drawer `100`), and re-injected if core re-renders the bar.

## Theme division

Baseline + data/injection interface. With the brand theme present, its nav
styling takes precedence for the look — see issue #6. On a pristine install this
governs the bar.

## Verify

`navigationLogic` (item normalisation + ordering) is unit-tested (`node --test`);
the DOM/injection glue is validated in a running course (dev server).
