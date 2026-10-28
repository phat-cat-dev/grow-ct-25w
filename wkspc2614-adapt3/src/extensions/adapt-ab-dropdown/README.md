# adapt-ab-dropdown

An **interface/adapter** over the **Adapt matching-component dropdown**
(`adapt-contrib-matching`'s `matchingDropDown`: the `.dropdown` root with
`.dropdown__btn` / `.dropdown__list` / `.dropdown-item`). That widget ships a
hard-coded palette from vanilla; this adapter re-themes it from `--ab-*` tokens
and exposes a selection event. It renders no widget of its own.

> "Is there an Adapt dropdown to style?" — yes, this one. It is **not** a generic
> Bootstrap dropdown menu; it's the matching question's select.

## Enable

Zero-config: enabled unless disabled. In `course.json`:

```json
"_abDropdown": { "_isEnabled": true }
```

## 1. Restyle seam

Stamps a stable **`.ab-dropdown`** class on each `.dropdown` widget;
`ab-dropdown.less` restyles the trigger / list / items under that hook, from
level-3 tokens:

| Token | Default |
|---|---|
| `--ab-base-dropdown-bg` | `var(--ab-accent)` |
| `--ab-base-dropdown-color` | `var(--ab-on-accent)` |
| `--ab-base-dropdown-bg-hover` | `color-mix(... bg, #000)` |
| `--ab-base-dropdown-bg-active` | `color-mix(... bg, #000)` |
| `--ab-base-dropdown-radius` | `0` |
| `--ab-base-dropdown-item-padding` | `var(--ab-space-100)` |

`!important` is used to beat vanilla's hard-coded dropdown styling (same reason
the brand theme's old `ab-dropdown.less` did), kept contained by the `.ab-dropdown`
scope. Hover/active shades derive from the fill via `color-mix`, so no theme-only
tokens are needed.

## 2. Data layer

Observes item selection and emits an event — **observe-only**, never
`preventDefault`, so the matching component's own open/close/select still runs:

```js
import Adapt from 'core/js/adapt';
Adapt.on('abDropdown:change', (dropdownEl, { text, value }) => { /* … */ });
```

## Theme division / supersedes

This replaces the brand theme's `ab-dropdown.less` (which re-themed the same
widget under `html.ab-theme`). On a pristine install this governs the dropdown;
when the brand theme is present the two overlap — retire the theme's file in
favour of this adapter (see issue #6).

## Verify

DOM/event glue is validated in a running course (a matching component with
`_isDropdownEnabled` / dropdown layout), not by unit tests.
