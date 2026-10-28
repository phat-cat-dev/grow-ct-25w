# Background washes

Fifteen independent background assets extracted from the existing washes gallery:
top, bottom, corner, centre, diagonal, dual, vignette, band, dots, hairlines,
crosshatch, microgrid, grain, paper and washgrain.

Open [index.html](./index.html) to compare intensity, hue and light/dark modes.
Each variant has an individual HTML fragment and CSS file. Include
`wash-base.css` plus the chosen variant, or use `washes.css` for all of them:

```html
<link rel="stylesheet" href="./wash-base.css">
<link rel="stylesheet" href="./corner.css">
<section class="wash-bg wash-bg--corner">
  <h2>Your heading</h2>
  <p>Normal selectable and interactive content.</p>
</section>
```

These are backgrounds, not interactive widgets. They are static, do not download
fonts, and need no JavaScript at runtime. The gallery's controls are preview-only.
The decorative pseudo-element sits behind content in an isolated stacking context
and ignores pointer events. It uses `::before`; avoid applying it to an element
that already uses that pseudo-element for something else.

Tokens: `--wash-intensity` (recommended .3-2.2, default 1), `--wash-accent`,
`--wash-ink-soft`, `--wash-hue`, `--wash-saturation`, `--wash-noise`.
Theme fallbacks use `--surface-1`, `--ink`, `--accent`, `--ink-soft`, `--h`, `--s`.
No root theme settings are imposed. Grain uses an embedded SVG noise image.

After changing source gradients, regenerate the individual assets:

```powershell
node .\assets\backgrounds\washes\build-washes.cjs
```

The generator checks every named rule in
[the source gallery](../../../.dev/assets/gallery/washes.html) before writing
files. The generated assets do not depend on the gallery at runtime.
