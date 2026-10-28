# Header asset

For nine more independent hero variants, see
[the hero collection](./heros/README.md) and its
[preview gallery](./heros/index.html).

This directory contains the extracted design-studio hero as a portable header:

- `header.html` is a copy-ready HTML example.
- `header.jsx` is a React component accepting `eyebrow`, `titleLines`,
  `description`, and `meta` props.
- `header.css` styles both versions without changing global element styles.

Include `header.css` and either the HTML or JSX markup. The styles are scoped to
`.ab-header` and its BEM elements. Component tokens can be overridden on the
header, for example:

```css
.ab-header {
  --header-accent: var(--accent);
  --header-ink: var(--ink);
  --header-ink-soft: var(--ink-soft);
  --header-font-heading: var(--font-heading);
  --header-font-body: var(--font-body);
  --header-space-before: 3rem;
  --header-space-after: 2rem;
}
```

When the corresponding GROW/theme tokens are present, the default values
connect to `--accent`, `--ink`, `--ink-soft`, `--font-heading`, and
`--font-body`; fallback values keep the component usable without them.

## Lesson page header

`page-header.html` and `page-header.jsx` provide the second, lesson-page pattern:
a kicker, depth badge, title, introduction and faint decorative tool glyph.
Use either template with `page-header.css`. The JSX props are `kicker`, `depth`,
`title` and `intro`.

These styles are scoped to `.asset-page-header`, avoiding collisions with
Adapt's `.page__header`. Colours, spacing and fonts follow the existing theme
tokens, with `--page-header-*` overrides. The inline SVG works offline without
an icon-font dependency. The title is H2 to fit the gallery page's H1; adjust the
heading level to suit the destination document's outline.
