# Cards — the CM card system

`src/extensions/adapt-ab-theme/less/cm-cards.less`

A Bootstrap-5.3-shaped card object
([structure reference](https://getbootstrap.com/docs/5.3/components/card/))
rebuilt on this theme's `--cm-*` tokens — no Bootstrap / `--bs-*` dependency.
CSS-only: authors write card markup inside any text/graphic component, the same
way `.cm.btn` works.

## Namespace + structure

Root is the compound class **`.cm.card`** (element carries both `cm` and
`card`), matching the `.cm.btn` convention. Familiar Bootstrap part classes are
scoped under it:

```html
<div class="cm card do">
  <div class="card-header">Do</div>
  <div class="card-body">
    <h3 class="card-title">Lead with the claim</h3>
    <p class="card-text">State the point first, then the evidence …</p>
  </div>
</div>
```

Parts: `card-header`, `card-body`, `card-footer`, `card-title`, `card-subtitle`,
`card-text`, `card-link`, `card-img-top` / `card-img` / `card-img-bottom`,
`card-img-overlay`. Group cards with `<div class="cm card-group">`.

## Variants

- **Colour** — `.cm.card.<colour>` for any palette colour (teal, coral, …):
  coloured border + a 10% header wash; the body stays neutral so colour reads as
  an edge accent, not a fill.
- **Scheme accent** — `.cm.card.accent` follows the series' `--cm-accent`, so a
  card re-themes with its pathway.
- **Pedagogy-functional** (semantic meaning + faint 5% body tint):
  | class | meaning | colour |
  |---|---|---|
  | `do` / `advice` / `feedback-pos` | good practice, affirmation | success (green) |
  | `dont` / `feedback-neg` | poor practice, caution | danger (red) |
  | `starting` | getting-started / warning | warning (sienna) |
  | `action` | do-this-now | info (teal) |

  These line up with the worked-example red/green scheme.

## Options

- `.with-icon` on the card + `<span class="card-icon cmet-icon">…</span>` in the
  title for a leading icon (coloured to the card accent).
- `.hover-animate` — opt-in subtle lift on hover/focus (honours reduced-motion).

## Accessibility

Focus within a card draws an accent ring; `forced-colors` falls back to system
colours; motion is disabled under `prefers-reduced-motion`. Keep card headers as
real headings where they title content, and don't rely on colour alone — the
do/dont header text ("Do" / "Don't") carries the meaning too.
