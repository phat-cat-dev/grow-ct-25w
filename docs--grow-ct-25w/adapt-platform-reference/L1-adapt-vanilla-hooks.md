# L1 adapt-vanilla hooks — the full override map

Exhaustive, human-readable sibling of
`design-kb/section-schemas/adapters/L1-adapt-vanilla-hooks.json`. Where
`theming-layers-map.md` (table B2) and `adapters/adapt.json` (`aliasMap`)
condense the override into **families**, this doc lists **every individual
selector** vanilla's own compiled CSS carries a literal on, the property it
carries it on, and the `--ab-base-if-adapt-*` token the L2 adapter repaints it
with.

Source of truth: `src/extensions/adapt-ab-theme/less/ab-vanilla-overrides.less`
(the 8 numbered sections). If that file's selector lists change, this doc is
stale until re-synced by hand — it is documentation, not generated output.

## The mechanism (why every rule below needs `!important` + a gate)

```
grunt/config/less.js glob order:
  1. components/*/less   (ours + adapt-contrib-*)
  2. extensions/*/less    (ours + adapt-contrib extensions)  ← ab-vanilla-overrides.less lives here
  3. theme/*/less         (adapt-contrib-vanilla)             ← compiles LAST
```

Last-compiled wins any tie on equal specificity → **vanilla beats our
extension** unless we out-rank it. Every selector below is therefore:

1. prefixed with the gate class — `html.ab-theme .selector` (or
   `html.ab-theme:not(...)` where the selector already began `html:not(...)`)
2. and carries `!important`

Gate absent from `<html>` (`config.json _htmlClasses`) → zero rules match →
vanilla's own literals render untouched = pure vanilla. The theme is opt-in.

## Seam 1 — the alias map (`:root`, top of the file)

| Adapter token (`--ab-base-if-adapt-*`) | Resolves to (today) |
|---|---|
| `item-color` | `var(--ab-base-accent)` |
| `item-color-hover` | `var(--ab-base-accent-hover)` |
| `item-color-visited` | `var(--ab-base-accent-active)` |
| `item-color-selected` | `var(--ab-base-accent-deep)` |
| `item-color-inverted` | `var(--ab-white)` |
| `font-color` | `var(--ab-dark-grey)` |
| `font-color-strong` | `var(--ab-base-ink)` |
| `font-color-muted` | `var(--ab-base-ink-muted)` |
| `greyDark` | `var(--ab-primary)` |
| `greyDark-hover` | `var(--ab-primary-hover)` |
| `greyLight` | `var(--ab-base-surface-sunken)` |
| `disabled` | `var(--ab-light)` |
| `hairline` | `var(--ab-base-hairline)` |
| `validation-success` | `var(--ab-success)` |
| `validation-error` | `var(--ab-danger)` |

> **Caveat:** `greyDark` / `greyDark-hover` / `disabled` / `font-color` alias
> to the live semantic + palette tokens the sweep actually used today, **not
> yet** the design-target pivot names in `adapt.json`'s condensed `aliasMap`
> (e.g. `@greyDark → --ab-base-ink-muted`). That re-point waits on deferred
> semantic-family reconciliation — doing it now would change the render.

## Section 1 — Accent base

**L1 literal:** `@item-color` / `@heading-color` (`#117F93`)

| Property | Selectors | → Token |
|---|---|---|
| `color` | `.boxmenu__title`, `.boxmenu__subtitle`, `.page__title`, `.page__subtitle` | `item-color` |
| `border-color` | `.boxmenu-item__inner`, `.aside-pull-quote` | `item-color` |
| `background-color` | `.accordion-item__btn`, `.boxmenu-item__button`, `.confidenceslider .slider__item-input-fill-linked`, `.gmcq-item__option`, `.hotgraphic__pin:not(.has-pin-image)`, `.mcq-item__label`, `.media__transcript-btn`, `.narrative__controls`, `.narrative__progress`, `.narrative__strapline-btn`, `.slider__number-selection`, `.slider__number-model-answer`, `.slider__item-input-fill`, `.trickle__btn` | `item-color` |

Split into three property groups because the compiled CSS puts this colour on
three *different* properties depending on the component (checked against
`build/adapt.css`, not assumed) — text-colour headings, border-only chrome
with its own unrelated body text, and solid-fill buttons/badges whose vendor
text is already white.

## Section 2 — Accent hover + focus-visible

**L1 literal:** `darken(@item-color, 10%)` (`#0c5865` / `#0e6b7c`)

All `background-color: var(--ab-base-if-adapt-item-color-hover)`, as hover/
focus-visible pairs:

- `.accordion-item__btn` (`:not(.is-selected):hover` / `:focus-visible`)
- `.boxmenu-item__button` (`:not(.is-disabled):not(.is-locked):hover` / `:focus-visible`)
- `.gmcq-item__label .gmcq-item__option` (hover) / `.gmcq-item__input:focus-visible + .gmcq-item__label .gmcq-item__option`
- `.hotgraphic__pin:not(.has-pin-image)` (hover/focus, disabled+locked excluded)
- `.mcq-item__label` (hover) / `.mcq-item__input:focus-visible + .mcq-item__label`
- `.media__transcript-btn:not([aria-expanded="true"])` (hover/focus)
- `.narrative__controls`, `.narrative__strapline-btn`, `.trickle__btn` (hover/focus, disabled+locked excluded)

All hover variants are scoped `.no-touch`; all focus variants are scoped
`:not(.a11y-disable-focusoutline)` and use `:focus-visible`.

## Section 3 — Accent visited

**L1 literal:** `darken(@item-color, 15%)` / `@visited` (`#09444e`)

`background-color: var(--ab-base-if-adapt-item-color-visited)` on:

`.accordion-item__btn.is-visited`, `.hotgraphic__pin:not(.has-pin-image).is-visited`,
`.hotgraphic__pin.has-pin-image .hotgraphic__pin-number`,
`.hotgraphic__pin.has-pin-image.is-visited .icon`,
`.hotgraphic__tile.is-visited .icon`, `.media.is-complete .media__transcript-btn`,
`.narrative__progress.is-visited`, `.narrative__strapline-btn.is-visited`

> `.narrative__progress` keeps its own **white** `border-color` at this step
> in vanilla's compiled CSS (the "visited ring" design) — deliberately left
> alone here. Contrast Section 4, where the border genuinely does turn teal.

## Section 4 — Accent selected / open

**L1 literal:** `darken(@item-color, 20%)` / `@item-color-selected` (`#063038`)

| Property | Selectors | → Token |
|---|---|---|
| `background-color` | `.accordion-item__btn.is-selected`, `.gmcq-item__label.is-selected .gmcq-item__option`, `.mcq-item__label.is-selected`, `.media__transcript-btn[aria-expanded="true"]`, `.narrative__progress.is-selected` | `item-color-selected` |
| `border-color` (extra) | `.narrative__progress.is-selected` | `item-color-selected` |

`.narrative__progress.is-selected` is the one selector where vendor's own
`border-color` *also* turns teal at this step (confirmed in compiled CSS, not
white) — hence the extra declaration.

## Section 5 — Grey-button family

**L1 literal:** `@greyDark` (`#4D4D4D`) base / `darken(10%)` (`#333`) hover /
`@disabled` (`#DDDDDD`)

Refines `theme.less`'s own blanket button `!important` (which flattens
vanilla's hover/focus/disabled states); this file loads after `theme.less`
(`v` > `t` alphanumerically) so it wins the tie and restores them.

**5a. Hover + focus-visible** — `background-color` + `border-color: var(--ab-base-if-adapt-greyDark-hover)`:

`.btn-text`, `.btn-icon`, `.btn__action`, `.btn__feedback`, `.nav__btn`,
`.drawer__btn`, `.notify__btn`, `.notify__btn-icon`, `.notify-push__close-btn`,
`.assessmentresults__retry-btn`, `.hotgraphic-popup__controls`,
`.hotgraphic-popup__close`, `.languagepicker__language-btn`, `.tutor__btn-icon`,
`.tutor-type-overlay .tutor__btn`, `.tutor-type-overlay .tutor__btn-icon`
(hover scoped `.no-touch` + state guards; focus scoped `:not(.a11y-disable-focusoutline)` + `:focus-visible`)

**5b. Disabled / locked** — `background-color` + `border-color: var(--ab-base-if-adapt-disabled)`, `color: var(--ab-base-if-adapt-font-color)`:

`.btn-text.is-disabled`, `.btn-text.is-locked`, `.btn-icon.is-disabled`,
`.btn-icon.is-locked`, `.btn__action.is-disabled`, `.btn__feedback.is-disabled`,
`.drawer__item-btn.is-locked`, `.drawer__item-btn.is-disabled`,
`.notify__btn.is-disabled`, `.assessmentresults__retry-btn.is-disabled`,
`.boxmenu-item__button.is-locked`, `.gmcq-item__label.is-disabled .gmcq-item__option`,
`.hotgraphic-popup__controls.is-disabled`, `.hotgraphic-popup__close.is-disabled`,
`.languagepicker__language-btn.is-disabled`, `.dropdown__btn.is-disabled`,
`.mcq-item__label.is-disabled`, `.narrative__controls.is-disabled`,
`.textinput__widget.is-disabled .textinput-item__textbox`,
`.trickle__btn.is-disabled`, `.trickle__btn.is-locked`

**5c. Non-button chrome** sharing the same family — `background-color` +
`border-color: var(--ab-base-if-adapt-greyDark)`, `color: var(--ab-base-if-adapt-item-color-inverted)`:

`.drawer`, `.drawer__btn`, `.drawer__item-btn`, `.notify__popup`, `.notify__title`,
`.notify__btn`, `.notify__btn-icon`, `.notify-push`, `.notify-push__close-btn`,
`.boxmenu-item__inner`, `.resources__filter-btn`, `.tutor__btn-icon`,
`.tutor-type-overlay .tutor__inner`, `.tutor-type-overlay .tutor__btn`,
`.tutor-type-overlay .tutor__btn-icon`

**5d. Selected / current** — `background-color` + `border-color: var(--ab-base-if-adapt-item-color-selected)`:

`.drawer__item-btn[aria-current="true"]`, `.drawer__item-btn.is-selected`,
`.resources__filter-btn.is-selected`

## Section 6 — Ink + muted text

**L1 literal:** `@font-color` / `@greyDark` (`#4D4D4D`) running text;
`lighten(@font-color, 25%)` (`#8d8d8d`) muted text.

> Links are **not** handled here — `theme.less`'s own `a, a:visited` rule
> covers them (fixed alongside this file so it now wins its own specificity
> fight). Duplicating ~30 selectors here would just point at the same token.

**6a. Running text** — `color: var(--ab-base-if-adapt-font-color)`:

`body`, `.page__body`, `.page__instruction`, `.boxmenu__body`, `.boxmenu__instruction`,
`.boxmenu-group__body`, `.boxmenu-group__instruction`, `.hotgraphic-popup__controls`,
`.hotgraphic-popup__close`, `.glossary__checkbox-label`, `.glossary__index-link`,
`.glossary__item-not-found`

> **Deliberate exception to the ink role token:** this is a literal swap, not
> a role-split — `#4D4D4D → var(--ab-dark-grey)` (`#6d6d6d`), not the
> near-black `--ab-base-ink` (`#1a1a1a`) used elsewhere. Contrast on white
> drops from **4.69:1 → 3.54:1**, below WCAG AA for normal-size text —
> accepted knowingly (Abbott, 10 Oct 2026), not an oversight.

**6b. Muted text** — `color: var(--ab-base-if-adapt-font-color-muted)`:
`.glossary__item-description`, `.glossary__items-group-header`

**6c. Progress indicator fill** — `background-color: var(--ab-base-if-adapt-item-color)`:

`.pagelevelprogress__indicator`, `.pagelevelprogress__indicator-bar`,
`.menu-item__progress .pagelevelprogress__indicator`,
`.menu-item__progress .pagelevelprogress__indicator-bar`,
`.pagelevelprogress__nav-btn .pagelevelprogress__indicator-inner`,
`.pagelevelprogress__item-btn:not(.is-disabled) .pagelevelprogress__indicator`,
`.pagelevelprogress__item-btn:not(.is-disabled) .pagelevelprogress__indicator-bar`,
`.header-color.transparent-light.menu .menu__header .pagelevelprogress__indicator`,
`.header-color.header-transparent-light.menu .menu__header .pagelevelprogress__indicator`,
`.header-color.transparent-light.menu .menu__header .pagelevelprogress__indicator-bar`,
`.header-color.header-transparent-light.menu .menu__header .pagelevelprogress__indicator-bar`,
`.comp-header-bg-color.transparent-light .pagelevelprogress__indicator`,
`.comp-header-bg-color.transparent-light .pagelevelprogress__indicator-bar`

**6d. Progress hover** — `background-color: var(--ab-base-if-adapt-item-color-hover)`:

`.no-touch .pagelevelprogress__nav-btn:hover .pagelevelprogress__indicator-inner`,
`.no-touch .pagelevelprogress__item-btn:not(.is-disabled):hover .pagelevelprogress__indicator`,
`.no-touch .pagelevelprogress__item-btn:not(.is-disabled):hover .pagelevelprogress__indicator-bar`

**6e. Progress disabled** — `background-color: var(--ab-base-if-adapt-disabled)`:
`.pagelevelprogress__item-btn.is-disabled .pagelevelprogress__indicator-inner`

**6f. Header title text (transparent-light header)** — `color: var(--ab-base-if-adapt-font-color-strong)`:

`.header-color.transparent-light.menu .menu__title`,
`.header-color.header-transparent-light.menu .menu__title`,
`.comp-header-bg-color.transparent-light .component__header`,
`.comp-header-bg-color.transparent-light .component__title`,
`.comp-header-bg-color.transparent-light .component__body a`,
`.comp-header-bg-color.transparent-light .component__instruction a`

## Section 7 — Surfaces + hairlines

**L1 literal:** `@greyLight` (`#f9f9f9`), `darken(@grey,5%)` (`#e6e6e6`),
`@grey` / `@disabled` (`#DDDDDD`)

**7a. Surface fill** — `background-color: var(--ab-base-if-adapt-greyLight)`:

`.drawer__toolbar`, `.resources__header-inner`, `.glossary__search-container`,
`.glossary__index-container`, `.glossary__items-group-header`,
`.glossary__item-description`, `.glossary__item-not-found`

**7b. Hairline border** — `border-color: var(--ab-base-if-adapt-hairline)`:
`.drawer__item-btn.is-locked`, `.drawer__item-btn.is-disabled`

> No `#f9f9f9` "surface-subtle" bucket here — every selector that used to
> carry it is a first-party `adapt-abbott-*` component, fixed at source
> instead (no vendor rule competes at its own BEM selector, so no
> `!important` is needed there).

## Section 8 — Validation

**L1 literal:** `@validation-success` (`#065f28`) / `@validation-error` (`#dd0000`)

Reuses `theme.less`'s existing semantic tokens (the authoritative
`cm-global.css` map); no new tokens needed.

| Property | Selectors | → Token |
|---|---|---|
| `color`, `border-color` | `.btn__marking.is-correct`, `.slider__widget.show-user-answer.is-correct .slider__number-selection`, `.slider__widget.show-user-answer.is-correct .slider__item-input-fill`, `.slider__widget.show-correct-answer.is-correct .slider__item-input-fill`, `.slider__widget.show-correct-answer.is-correct .slider__number-model-answer` | `validation-success` |
| `color`, `border-color` | `.btn__marking.is-incorrect`, `.narrative__instruction.has-error`, `.matching__widget:not(.is-complete) .matching-item__select-container.has-error .dropdown__btn`, `.slider__widget.show-user-answer.is-incorrect .slider__number-selection`, `.slider__widget.show-user-answer.is-incorrect .slider__item-input-fill`, `.slider__widget.show-correct-answer.is-incorrect .slider__item-input-fill`, `.slider__widget.show-correct-answer.is-incorrect .slider__number-model-answer` | `validation-error` |

## Explicitly excluded (by design)

Not swept — either intentional vendor literals or already fixed elsewhere:

- `.bg-color.*` / `.header-color.*` / `.comp-header-bg-color.*` black-white
  a11y utilities
- high-contrast blocks, `#a11y-focuser`
- MediaElement (`.mejs__*`) chrome
- anything already a plain `--ab-primary` via `theme.less`

## Adding a new selector

The eight families mirror vanilla's own state model (base / hover+focus /
visited / selected / disabled), so a new selector almost always slots into
an existing group. If any teal or vanilla grey survives a build: grep the
built `adapt.css` for the hex, find its selector, and add it to the matching
family above **and** in `ab-vanilla-overrides.less` and the JSON sibling.

## See also

- `src/extensions/adapt-ab-theme/less/ab-vanilla-overrides.less` — the live rules (source of truth)
- `src/extensions/adapt-ab-theme/less/L1-adapt-vanilla-hooks.less` — comment-only reference co-located with the LESS
- `design-kb/section-schemas/adapters/L1-adapt-vanilla-hooks.json` — machine-readable sibling of this doc
- `design-kb/section-schemas/adapters/adapt.json` — condensed family-level aliasMap
- `docs/authoring/theming-layers-map.md` — the six-layer model this sits inside (table B2 / section A3)
