# Shared engine, small theme packs

The GROW/Abbott token engine and Adapt compatibility styles exist **once** in
[`grow-ct/less/`](../grow-ct/less/), not inside each theme pack.

## The build route

1. [`grow-ct/less/theme.less`](../grow-ct/less/theme.less) imports
   [`current-theme.less`](current-theme.less).
2. `@grow-theme-current` selects exactly one theme file.
3. That file imports the common
   [`default_theme_template.less`](themes-templates/default_theme_template/default_theme_template.less).
4. The template supplies fallback dials and imports
   [`interface.less`](../grow-ct/less/interface.less).
5. The interface imports [`00-foundation.less`](../grow-ct/less/00-foundation.less)
   first, then shared compatibility/default, shell, plugin and structural rules,
   followed by the corrected foundation application rules.
6. The selected theme supplies its values and final overrides. LESS resolves its
   variables lazily, so those values feed the shared engine's calculations.

Only one theme is selected; GROW and CMET do not import each other.

## Selecting a theme

Edit **only** `@grow-theme-current` in
[`current-theme.less`](current-theme.less). Its path is relative to the import
site, `grow-ct/less/theme.less`. Available selections:

- [GROW red](grow-themes/grow-theme-red/grow-red-theme.less) (active, reusable red settings pack).
- [GROW default](grow-themes/grow-theme-default/grow-default-theme.less).
- [CMET default](cmet-themes/cmet-theme-default/cmet-default-them.less).
- [Common baseline](themes-templates/default_theme_template/default_theme_template.less).

`@grow-theme-current` is a **build-time LESS import path**.
The engine also emits CSS `--grow-theme-current` as the selected theme's name
for inspection. A runtime CSS variable cannot load or select LESS files.

## Editing or creating a pack

Copy the [red settings pack](grow-themes/grow-theme-red/grow-red-theme.less),
or a small GROW or CMET theme file, keep its import of the common template
(adjust the relative path if moved), and change its dials. Do **not** copy any
`styles/` trees.

Both theme files explicitly list their typography and spacing settings:
font families, weights, line heights, tracking, readable measures, all twelve
fluid type steps, all nine fluid spacing steps, semantic padding/gap roles,
content widths and gutters. Edit those settings in the selected theme, not
the shared foundation. Their initial values preserve the existing appearance.
The repeated **settings** are intentional per-theme configuration; the engine
and selector rules are still shared once. Omitting a setting uses its fallback.

The red pack is a reusable starting point, not a standalone copy of the engine.
It inherits surfaces, light/dark behaviour, radius and elevation from the common
template. Its default accent is `hsl(0, 72%, 42%)`; semantic success/error colours
remain separate from the brand. Rename `@grow-theme-name` when copying it.

The separate Theme Manager workshop currently builds studio CSS and token JSON,
not this Adapt LESS format. A future exporter must map its source hue/saturation
and neutral saturation to `@grow-h`, `@grow-s` and `@grow-gs`, and its typography
and spacing settings to the ramps below. Source lightness, harmony selection,
preview modes and button appearances are not automatically transferred by those
three colour dials. The red pack is selected here at build time; it is not yet
controlled live by that workshop.

`@grow-type-scale` and `@grow-space-scale` multiply the respective ramps;
the `--fs-*` and `--space-*` settings change the curves themselves.
Preserve `var(--space-scale)` in spacing expressions to keep the density dial.
Heading sizes use `--fs-4xl` (h1/page), `--fs-3xl` (h2/article),
`--fs-2xl` (h3/block), `--fs-xl` (h4/component), `--fs-lg` (h5) and `--fs-sm` (h6).
Settings named `--layout-wide`, `--layout-narrow` and `--pad-control` are available
tokens, not a guarantee that every compatibility/plugin rule consumes them.

```less
@import "../../themes-templates/default_theme_template/default_theme_template.less";

@grow-theme-name: "my-theme";
@grow-h: 330;
@grow-s: 65%;
@grow-gs: 12%;
@grow-type-scale: 1.1;
@grow-space-scale: .95;
@grow-font-ui: system-ui, sans-serif;
@grow-font-heading: var(--font-ui);

:root {
  --radius-md: 8px;
  --l-h1: 35%;
}
```

Then select the new file in `current-theme.less` and rebuild. LESS hue/saturation
dials also drive the real colour palette used by Adapt plugin `darken()` and
`fade()` calculations. Changing CSS `--h` at runtime retints foundation/content,
but does not recalculate baked shell colours.

Use runtime token overrides after the template import for other visual choices,
or final selectors when necessary. Fonts, sizes, spacing, colours and state rules
remain overridable; shared rules are not a second selected brand theme.
System dark mode and root `data-theme="dark"`/`"light"` remain supported.

## Shared rule ownership

| Surface | Single shared owner in `grow-ct/less/` |
| --- | --- |
| Colour/type/space token engine, light/dark ladders | `00-foundation.less` |
| Adapt colour roles and button-state aliases | `_defaults/_colors.less` |
| Type roles and mixins | `_defaults/_font-config.less`, `_font-mixins.less` |
| Button rendering and states | `_defaults/_buttonMixins/` |
| Compatibility spacing | `_defaults/_spacing*.less` |
| Navigation, drawer, page and shell painting | `core/` |
| Component, extension and menu painting | `plugins/` |
| Frontmatter, phases and columns | `grow-lesson.less`, `grow-structure.less` |
| Import order and final foundation application | `interface.less` |

The common template owns the fallback dial values and basic radius/elevation
defaults. Adapt's own CSS still compiles for mechanics and accessibility.
Plugin theme styles remain active to preserve component states and drawer
buttons; they are no longer copied per theme.

## Optional layers: disabled in the basic build

The restored Abbott layers `15-surfaces`, `16-paper`, `25-motion`, `35-diagrams`,
`40-cycle-timeline`, `45-scribbles`, `50-marks`, `55-bullets`, `60-backgrounds`,
`65-washes` and `70-heroes` live once in `grow-ct/less/`, but are **not imported**.
They must not enter the build merely because their files exist.

Before explicitly importing one from a selected theme, review its markup and
assets. Marks/bullets refer to an inline SVG `#ink` filter; washes include a
self-contained SVG noise texture, not a missing image file. The earlier GROW
decoration variants are preserved under
[`_dev/_quarantine/grow-decoration-variants/`](../_dev/_quarantine/grow-decoration-variants/).
Nothing under `_dev` is imported.

The original Abbott foundation is retained in quarantine as reference. The active
port preserves its token contract while retaining the fixes for escaped fluid
maths, live heading colours, actual Adapt component containers and reduced-motion
completion events. Do not overwrite it with the older version.

The legacy `zzz-fluid-baseline.less` and `zzz-overrides.less` are also references,
not imports: their fixed/fluid values conflict and their old container assumption
does not match Adapt.

`grow-ct/less/90-interface-red.less` is also an inactive test file. The selected
red pack supplies red via `@grow-h: 0`, so both compiled shell colours and live
foundation tokens receive it, rather than applying a runtime-only override.

## Build and validation

Run `docker compose up --build` from the repository root. Staging exposes **only**
the loader to Adapt's automatic theme LESS glob; the real source tree is imported
explicitly. Pack, engine and selector changes are watched. Copying this entire
LESS directory straight into the framework's automatic glob would bypass that
ordering and activate optional layers: use `docker/prepare-theme.cjs`.

```sh
docker compose exec -T -w /work/framework adapt npx grunt less:dev --theme=grow-ct
docker compose exec -T -w /work/framework adapt node /repo/docker/test-theme-packs.cjs /work/framework /repo
```

The test compiles all selections through the actual loader, checks the token
contract, shared imports, absence of decoration/quarantine imports, dial
propagation, theme identity and missing-theme failure. Missing imports fail
explicitly; there is no fallback to vanilla.
