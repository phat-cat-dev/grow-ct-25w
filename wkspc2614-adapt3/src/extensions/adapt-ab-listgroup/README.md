# adapt-ab-listgroup

A Bootstrap-5 list group (`.ab.list-group` > `.list-group-item`) as a
**style-only** extension — authorable inline in any component's body. No JS, no
config; styled on `--ab-base-listgroup-*` tokens.

## Use

```html
<ul class="ab list-group">
  <li class="list-group-item">An item</li>
  <li class="list-group-item active" aria-current="true">Current item</li>
  <li class="list-group-item disabled" aria-disabled="true">Disabled item</li>
  <li class="list-group-item success">A positive item</li>
</ul>
```

Action rows (links/buttons get hover + focus):

```html
<div class="ab list-group flush">
  <a class="list-group-item list-group-item-action" href="#/">A link row</a>
  <button type="button" class="list-group-item list-group-item-action">A button row</button>
</div>
```

### Modifiers

| Class | Effect |
|---|---|
| `.active` (item) | accent fill (set `aria-current="true"`) |
| `.disabled` (item) | dimmed, non-interactive (set `aria-disabled="true"`) |
| `.list-group-item-action` / `<a>` / `<button>` | hover + focus affordance |
| `.success` `.danger` `.warning` `.info` (item) | tinted contextual background |
| `.flush` (on `.ab.list-group`) | drop the outer border/radius (for nesting) |

## Tokens (level 3)

`--ab-base-listgroup-bg` / `-color` / `-border` / `-border-width` / `-radius` /
`-padding-y` / `-padding-x` / `-active-bg` / `-active-color` / `-hover-bg`, each
defaulting to the base spine. Move a token to reskin; no palette here.

## Accessibility

Use the right element: `<ul>`/`<li>` for a static list, `<a>`/`<button>` rows
for interactive ones. Mark the current row `aria-current="true"` and disabled
rows `aria-disabled="true"`.
