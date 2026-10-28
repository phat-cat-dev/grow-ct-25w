# AB Theme Studio

The Educational animations area provides 18 reusable SVG drawing demos: a
mix-and-match line/box sequence (three variants of each), circle and triangle
cycles split into one through four consecutive parts with separate arrowheads,
and standalone nodes, lines, arrows and an exclamation mark. A shared CSS clock
uses `--edu-duration` (4s fallback), `--edu-speed` (1), `--edu-local-speed` (1)
and `--edu-iterations` (1). Draw/replay, pause/resume, repeat, arrow visibility
and copyable standalone SVG/CSS are available. Playback is opt-in; reduced
motion shows finished drawings. Research links and embedding instructions live
in `public/site/fragments/12_educational_animations.md`.

A tiny Node studio for the **AB single-hue HSL design system**. Pick one colour
and a colour-theory harmony preset, preview it live, and build a ready-to-ship
`theme.css` — in **keep-dynamic** mode, so nothing is ever flattened to hex and
the whole system re-derives from a handful of ingredients via `var()`.

## Run

```bash
npm install
npm start          # → http://localhost:5173
```

- `/` — the **HSL tuner** (your editor / live preview)
- `/site/` — the **ordered site**: Index, Color tuning, Typography, Icons,
  Spacing, Motion, objects. One HTML page with nested sections matching the numbered
  Markdown outlines in `public/site/`, styled with the shared tuner assets.
- `/cheatsheet.html` — the **class-vocabulary cheat-sheet**
- `/cheatsheet%20copy.html` — the **integrated studio and reference**, with live
  controls and demos inside each reference section (no embedded tuner)
- `/theme.css` — the **live design system**

### Learning page template

Open [`public/site/section/page-template.html`](public/site/section/page-template.html)
directly in a browser, or visit `/site/section/page-template.html` with the server
running. This static template reuses the shared tuner and Adapt specimen styles;
it does not require JavaScript or implement Adapt learner tracking.

Replace the example copy and graphic, duplicate articles for sections and blocks
for rows, and keep components inside each block's `component__container`. Use
`is-left` / `is-right` for paired components or `is-full` for a full-width component.
Keep every `id` and `data-adapt-id` unique and update matching anchor links.
The `bg-tint` article and `is-raised` component demonstrate optional modifiers.

Build a saved theme to disk:

```bash
npm run build navy   # → dist/navy/theme.css  +  dist/navy/tokens.json
npm run build        # builds every themes/*.json
```

## Theme manager component workshop

Open `/site/components/tools/theme-manager/` while the studio server is running.
This isolated floating header leaves the original studio header unchanged and
connects to the existing scheme list/load/save/build APIs. It includes a scoped
live preview, source-colour lock/shuffle, JSON import/export and build downloads.
The [component workshop guide](public/site/components/tools/theme-manager/README.md)
documents its mounting API and a gradual JSX/React conversion exercise.

## The idea

A theme is ~8 numbers (see `themes/navy.json`):

| field       | meaning                                             |
|-------------|-----------------------------------------------------|
| `brandH`    | the one knob — hue 0–360                             |
| `brandS`    | saturation of the colourful brand scale             |
| `greyS`     | saturation of the blue-grey neutrals (never 0)      |
| `harmony`   | preset: `complementary` `analogous` `triadic` `split` `tetradic` `square` `monochrome` |
| `semanticS` | saturation of the semantic colours                  |
| `overrides` | free-form `{ "--token": "value" }` pins             |

`src/harmony.js` is the single source of truth for the preset → angle-offset
tables. Everything else — scales, accents, semantics, shadows, harmony siblings,
light/dark — lives in `theme.css` and computes from the ingredients.

## Keep-dynamic build

`build.mjs` emits `theme.css` **verbatim** plus a trailing, unlayered `:root`
block that sets only the ingredients. Unlayered declarations beat the `@layer`
defaults, so these win and the rest of the system recomputes from them — in
light *and* dark. No colour is flattened.

> **Dark-mode note:** only props that are identical in light and dark are forced
> globally (hue, saturations, harmony angles, semantic saturation). The
> theme-flipped *lightness* tokens (`--sem-l`, `--acc-l`, surfaces) stay in
> `theme.css` so dark mode keeps working. Pin those via `theme.css`, not
> `overrides`, unless you add a matching dark value.

## Files

```
ab-theme-studio/
├─ theme.css              # the design system (the "bundle") — served + used as the build template
├─ public/
│  ├─ index.html          # HSL tuner (editor UI)
│  ├─ cheatsheet.html     # class-vocabulary reference
│  ├─ cheatsheet copy.html # integrated studio and reference
│  ├─ tuner.css          # shared tuner/demo styling
│  ├─ tuner.js           # shared live controls and Save/Load/Build
│  ├─ reference.css      # reference layout and icon gallery
│  ├─ reference.js       # section CSS copying and icon packs
│  └─ icons.svg           # the 33-symbol sprite
├─ src/
│  ├─ harmony.js          # preset → [h2,h3,h4] angle offsets  (shared truth)
│  ├─ tokens.js           # config → ingredient overrides
│  ├─ emit-css.js         # theme.css + ingredient override  (keep-dynamic)
│  └─ emit-json.js        # portable theme record
├─ themes/navy.json       # a saved theme config
├─ build.mjs              # CLI build
└─ server.mjs             # dev server + JSON API
```

## JSON API

| method | route                 | does                                  |
|--------|-----------------------|---------------------------------------|
| GET    | `/api/themes`         | list saved theme names                |
| GET    | `/api/themes/:name`   | load one config                       |
| POST   | `/api/themes/:name`   | save a config (JSON body)             |
| POST   | `/api/build/:name`    | build → `dist/:name/`                 |

## Using the studio

### Ordered site

`public/site/index.html` is generated from ten ordered Markdown sources.
Section 8, Layout, is authored in `public/site/07_layout.md`:

The Cards subsection of Objects is generated from
`public/site/fragments/cards.html` (replacing the legacy pasted card examples in
`06_obects.md`). It presents themed cards, semantic cards including amber
caution, a live project-wide card styler, nested layers and responsive joined
sets. The styler controls default family/fill, padding, border, tint, elevation,
icon size and set spacing. Explicit card modifiers override defaults; semantic
accents stay tied to their live meaning tokens. Layout remains responsible for
corners. The `cards` settings persist through save/load and JSON export and are
included in browser, CLI and API CSS exports. Old schemes without `cards` keep
their previous CLI output and use default settings in the workbench.

Layout includes a live 0–48 px corner-radius slider, reset and card/button
previews. It controls shared radius tokens and workbench cards, containers and
buttons, including the padlock. Explicit square/circle icon frames stay
independent. Layout settings persist in saved/JSON themes and browser, CLI and
API CSS exports. Older themes use the default 16 px radius.

The sticky rail shows the active main source as a larger rectangular colour chip
with an editable HSL value inside, using a contrasting foreground. Paste a hex
(with or without `#`), RGB, HSL, named colour or another browser-supported absolute
CSS colour, then press Enter or leave the field to apply it. Escape cancels.
Opaque colours only; invalid values show an inline error without changing the
theme. Pasting activates Brand and preserves the exact converted HSL lightness
as a custom selection in saved themes and exports. It follows exact
shade selections, main-system changes and light/dark mode.
“Set as base theme” captures the selected colour as a fixed HSL foundation.
All colour controls remain editable: Harmony and Semantics derive from that
foundation, while swatch clicks and other controls preview candidates without
replacing it. Only another explicit “Set as base theme” changes the foundation.
The fixed base is saved with the theme and retained in CSS exports.
The padlock beside the floating HSL chip makes that state explicit: open means
colour selections update the live theme; closed means the base is fixed.
Click it to pin the current colour or release the base. Releasing immediately
applies the current selection. The rail colour input is disabled while locked;
the other colour editing controls remain available for candidate previews.
The shuffle button on the other side of the HSL chip generates a new source
hue, saturation, neutral saturation, tonal remix, harmony preset and colour count
on each click. Semantic adjustments reset to follow the new foundation. Included
layers are retained (Brand is activated); typography, cards and layout are
unchanged. Shuffle is disabled while a fixed base colour is set.
In whole-palette Harmony mode it identifies the selected
source colour, not the separate action/link colour assigned by role mapping.

```bash
npm run build:site
```

The Motion area is authored in `public/site/05_motion.md`. Its thirteen icon and
nine typography previews start paused; click a tile (or use Enter/Space) to
toggle playback. Each tile exposes its pressed state and a visible playing label,
and respect `prefers-reduced-motion`. Changing that preference or hiding the
browser tab pauses previews. Motion styles are scoped to the preview specimens;
the rest of the workbench keeps its stationary hover behaviour. These are site
demonstrations, not automatically included in exported theme CSS.
Source controls and accordion specimens are maintained under
`public/site/fragments/` rather than extracted from the editable cheat sheet.
H3 outline headings independently collapse their section content using native
buttons (Enter/Space), with expanded sections by default. Direct section links
open the enclosing area and any collapsed H3 section before scrolling.
The heading-styled accordion examples are live: H2 brand, H3 Color-grey,
H4 reverse grey and H5 reverse brand retain their distinct open/closed fills.
Native buttons toggle independently with Enter/Space, expose expanded state and
control labelled panels that are hidden when collapsed. The H6 inline example
is a minimal text disclosure. Global typography decorations and bullets exclude
accordion headers so they do not interfere with the component.

Edit those sources to change the outline, then regenerate. Their heading text,
numbering and order are preserved, including numbering gaps. Index remains
a placeholder. Existing tuner controls and accordion examples fill the
matching HSL Tuner and Accordions sections; pasted demo headings are captions,
not extra outline headings. The original tuner and cheat-sheet pages are unchanged.
Each main H2 contains a keyboard-accessible dropdown trigger. Areas start
collapsed and can open independently; navigation and direct section links open
the target area automatically. Without JavaScript, the content remains visible.

Colour and typography controls are wired to the active main palette.
Light/Dark/System works in the top rail.
Google Fonts and Google Material Symbols are live connectors in Web fonts and
Icons. Choose separate heading/body fonts, or Outlined/Rounded/Sharp symbols with
weight, fill and size controls. The searchable symbol preview provides selectable,
copyable markup while retaining the existing SVG packs. Connections use Google's
public CSS API (internet access required); load failures appear beside the previews.
Material Symbols choices are compact, framed icon-only buttons. Names remain
available as accessible labels and hover titles; selection and keyboard focus
are visibly indicated, and search still matches the symbol names.
Their frames, padding, border thickness and corner radius scale proportionally
with the symbol-size slider; the grid reflows at the resulting button size.
The existing SVG packs also use icon-only framed tiles, retaining hover names,
accessible labels and click/Enter/Space-to-copy. Their separate size slider scales
glyphs, frames and borders together; the Circular frames switch toggles between
square and round frames. These gallery display controls are preview-only.
No API key is needed. Font requests send the chosen family names to Google.
The duplicated pasted SVG pack is shown once; all 33 icons remain copyable by
mouse or keyboard. Original Markdown examples are kept intact.
Open **CSS / scheme tools** for the working CSS editor:

- **Inject CSS** applies the editor CSS to this page; **Remove injection**
  restores the preview. Editing or loading CSS does not apply it automatically.
- **Copy CSS** and **Export CSS** include the full design-system bundle, selected
  colour layers, typography, spacing, Google imports, connector rules and editor CSS.
  **Export scheme JSON** includes the complete configuration for re-editing.
  Imports are placed first so exported and built CSS loads correctly.
- Over HTTP, **Save scheme** persists the configuration and editor CSS;
  **Load** restores them. **Save & build scheme** saves the current editor first,
  then generates the full design system plus its custom CSS, with download links.
- Existing ingredient values and overrides survive loading and saving. Custom
  CSS also survives a subsequent save in the original tuner. Colour and
  typography settings are stored in the saved configuration.

All four colour sections can be the main theme. Their **Use as main system**
buttons are exclusive; **Export theme CSS** exports the current complete
selection, not only that section. Harmony retains its whole-palette role mapping.
Click an HSL/brand ramp step (including Color-grey and Pure grey), or a semantic
strong/weak button, to use that exact HSL shade as the main accent in both modes.
Semantic Tuning includes colour presets (Default, Muted, Vivid, Pastel and High
contrast) and appearance modifiers (Original, Solid, Soft, Outline/border and
Inverted). Presets keep meaning hues fixed and transform saturation/lightness
relative to the active foundation before slider offsets. Selecting a preset
resets offsets in both modes and releases an exact semantic selection, but never
changes a locked base. Appearance applies to semantic buttons and badges across
the project, not cards; explicit `.outline`, `.soft` and `.link` styles are kept.
Original preserves solid buttons and soft badges. Both settings are stored in
`colorSystem` and exported when Semantics is included. High contrast is palette
separation, not an accessibility certification.
Heading bullets and left-border decorations are left-aligned. Left-border
thickness and the inset use root-relative units so their left edges do not drift
with heading font size; Academic icon sizes remain heading-relative.
Heading size choices also include six modular scales: Minor second (16/15),
Major second (9/8), Minor third (6/5), Major third (5/4), Perfect fourth (4/3)
and Augmented fourth (sqrt(2)). H6 is 0.875rem times Scale; each level toward H1
multiplies by the ratio. Modular sizes interpolate from 85% to 100% between
20rem and 80rem viewports, preserving adjacent ratios. Original Graded and
Uniform outputs remain unchanged. The live formula readout shows all six maxima.
These settings save/export as `typography.size`; they do not alter spacing tokens.
The H1–H6 preview sits directly beneath the section title, before all modifiers.
The rail's CSS / scheme tools button shares the theme-mode button geometry and
interaction styling; its expanded state uses the same selected appearance.

`public/site/08_structure.md` is the ninth generated area, Adapt structure.
It includes a scoped menu/page/article/block/component specimen based on the
local `adapt-theming-kit`, including container and dual-BEM hooks, wrapping
left/right components and full-width content. Colours, fonts, fluid spacing and
corners follow the active studio theme. It is not an Adapt runtime or a
pixel-perfect Vanilla theme. The section records reference inconsistencies and
proposes a token/type/fluid/structure/component/author import mapping.
No Adapt-specific package exporter is implemented: existing CSS/JSON exports are
unchanged. Verify the installed Adapt version and import pipeline before using
the proposed LESS bridge, and avoid loading both starter layout systems.

`public/site/fragments/10_adapt experiments.md` supplies six collapsible lesson
experiments in the tenth area. `src/lesson-experiments.mjs` renders the maintained
compositions: Guided field notes, Workshop canvas, Story chapters, Case
investigation, Milestone journey and Reflective studio. Each workbench H3 is the
d1 surround; a visible H4 inside is the d2 lesson page title (conceptual lesson
H1). Articles use H5/d3, blocks H6/d4, and component titles use
`role="heading" aria-level="7"`/d5, preserving the workbench heading hierarchy.
Depth labels sit at the bottom-right of their card or section header, outside
heading flow, with a reserved inset to keep them clear of content.
The compositions differ beyond column ratios: editorial marginalia and a side
brief, a model/assembly/comparison bench, cinematic scenes and a branching-scenario
placeholder, an expandable evidence dossier, a checkpoint route, and an
inspiration/sketchbook/gallery studio. Each stage has different content geometry.
Abstract CSS artwork represents future media components; evidence disclosure and
journal inputs work locally. All palettes use theme tokens and layouts stack on
small screens. Lesson paragraphs fill their containers; reading measure is
limited explicitly on hero introductions rather than every lesson paragraph.
Navigation and action controls use the shared `.ab.btn` schema, varying existing
solid/outline/soft/link, pill/square, size and semantic-family modifiers by lesson
and stage. Completion labels describe the local activity rather than repeating
the same generic next-stage button.

Lesson experiments also include Sideways workspaces: four exclusive horizontal
accordion panels, each containing multiple cards or media/widget placeholders.
One workspace stays open. Shared button modifiers style the rails; arrow keys,
Home and End move between triggers, and Enter/Space opens the focused panel.
Closed regions are hidden and inert. Mobile uses stacked rails, and reduced
motion disables sliding/fading. Notes remain local and unsaved.
Native details keep aims/frontmatter and revealed
blocks independently collapsible. Stage 1 starts open; completing each simulated
widget reveals/opens the next block, announces progress and focuses its summary
without forcing a scroll. Reveal is opacity-only and disabled for reduced motion.
Restart clears practice notes and completion, hides later stages and reopens aims
and stage 1. No real Adapt runtime or completion events are installed, and notes/
progress are not stored or exported. Layouts use studio cards, semantic/harmony
accents, font connectors, fluid type/spacing and Layout corners; the preview CSS
and interaction code are workbench-only, not part of generated theme exports.
Heading colour schemes include eight further choices: Muted (45% of active
saturation), Analogous, Complementary (base/opposite grouped by three levels),
Triadic, Split-complementary, Square, Spectrum (60-degree steps), and Golden
angle. The seven harmony schemes derive H1–H6 hues from the active main hue and
override whole-palette heading hue mapping without altering that palette.
Reverse reverses their hue and brightness order; size, decoration and CAPS
remain independent. Choices persist as `typography.scheme` and work in scoped
previews, downstream styling and CSS exports. Existing six schemes are retained.

Harmony now has 23 choices, including Tight/Wide analogous, Wide split,
45-degree Rectangle, Pentadic (72-degree steps), Hexadic (60-degree steps),
Spectrum (360 degrees divided by count), and Golden angle
(180 * (3 - sqrt(5)) degrees per colour). Fixed-anchor formulas repeat with
lightness variations when count exceeds anchor count. Spectrum and Golden angle
generate a distinct hue for every entry. All support 3–10 colours, exact shade
selection, fixed-base locks, shuffle, JSON persistence and CSS exports.
The rethemed harmony card preview appears before the preset/count modifiers.
The selected shade has a pressed state, persists as `colorSystem.mainShade`, and
is emitted identically by preview, CSS exports and API/CLI builds. Primary button
foreground uses whichever of black/white provides the higher WCAG contrast.
Choosing a system again returns to its automatic palette; generating a new seed
or remix clears the pinned shade. Fixed semantic hue identities remain intact.

Harmony swatches behave like semantic buttons: clicking one captures its exact
displayed HSL colour as the main accent, including repeated-hue lightness variants.
This selection persists in JSON and CSS builds and stays fixed across light/dark
mode changes. The Harmony main-colour selector selects the same swatches.
The section's **Use as main system** button restores whole-palette role mapping;
changing the harmony preset or count also clears the pinned harmony shade.
Harmony specimens keep their independent lightness instead of repeatedly shifting
when an already selected swatch is clicked.

Six extra one-hue presets sit beside original Monochrome: **Tints** (42–90%
lightness), **Shades** (68–10%), **Muted** (constant 48% lightness with decreasing
saturation), **Pastel** (72–90% lightness with softening saturation), **High
contrast** (alternating dark/light), and **Ink and wash** (20% ink plus pale,
muted supporting tones). All interpolate over 3–10 colours, retain the brand hue,
and export per-slot `--theme-harmony-s-N` and `--theme-harmony-l-N` tokens.
These six use fixed lightness values in either mode; the original Monochrome
keeps its existing accent-relative tones. High contrast is a palette description,
not a guarantee of accessible text contrast. Exact swatch selection captures
the slot's saturation as well as lightness; settings persist in scheme JSON.

**Save complete theme** in any colour section opens the naming/save tools.
On the local `file:` page, **Save scheme** and **Load** use browser localStorage;
over HTTP they continue using the server's theme files. Both retain colour
pipelines and the exact main shade, included layers, fonts/symbols, typography,
spacing, custom CSS and Light/Dark/System mode. Load restores custom CSS as well.
Local saves are specific to this browser and file location and can be removed by
clearing browser data. **Export scheme JSON** provides a portable backup;
**Import theme JSON** restores either that file or a built tokens JSON record.
Only full bundle builds still require the server.

#### Fluid spacing

The Spacing area uses the three supplied LESS sources in
`public/site/fragments/04_spacing/`. `npm run build:site` compiles them with LESS
into the persistent `public/site/fluid-core.js` bundle, embedded in the generated
page so it also works from disk. Rebuild after editing the LESS sources.
Layer 0 settings feed independent text, space and layout clamps; semantic
multipliers and the original legacy token aliases are preserved.

Theme-accented sliders with live rem readouts adjust minimum/maximum bases and
viewport bounds. Paired slider limits prevent reversed ranges; reset uses the
standard secondary button model. Invalid or
reversed ranges show an error and retain the last valid settings. The default
pack grows from 0.75rem to 1rem between 20rem and 45rem. Compact and Roomy provide
denser and more generous spacing; fixed scoped comparisons, a live card container,
seven text sizes and measured pixel readouts demonstrate the differences.
Card SVG icons have a separate fluid min/max size range (default 1.5–2.5rem,
allowed 0.5–6rem) using `--ab-icon-size`. Text size, card padding and icon padding
are unaffected by icon-size edits. Icon settings persist in the spacing record
and CSS exports/builds; older themes receive the defaults.
Resize the browser to see the clamps grow and saturate. Every `data-ab-profile`
scope recomputes its own engine tokens instead of inheriting resolved root values.
Tokens are available globally, but specimens opt in explicitly: existing page
typography remains under the Typography controls. Colours follow the main theme.
The `spacing` record travels with scheme save/load and JSON; CSS copy/export,
API builds and CLI builds include the compiled engine and current settings.
Schemes without this record keep their previous build output.

#### Colour pipeline

Typography heading schemes, decoration, bullets, sizing, reverse and scale are
live in the Typography area. **Set downstream** activates the current heading
scheme across the page; subsequent changes remain live. **Reset typography**
also restores underline thickness (0.06em) and left-border width (0.18rem).
These independent controls use heading-relative units and are saved/exported.
Heading bullets include chevron, dot, arrow, circle, square, diamond, star, check,
plus, dash and double chevron, as well as no bullet. Each follows the heading's
colour and size, and persists in saved themes and CSS builds.
An additional compact Academic practice row offers Starting, Assessment,
Feedback and Researching icons, plus Progressing, Writing, Reflecting and
Criticality. Heading markers are .72em and use embedded SVG
masks, so exported typography works without the page's SVG sprite.
Reset
restores defaults and returns headings to preview-only. Body size ceiling,
unitless line height and maximum reading width apply immediately. Heading and
body sizes use continuous `clamp()` curves between 20rem and 80rem viewports,
with rem-based limits for zoom support. Colours reference the active main
palette, and Google font pairing continues to apply. The `typography` record is
saved/loaded and emitted in CSS exports and API/CLI builds before custom CSS.
Older themes without that record retain their previous build output.

1. **HSL Tuner** accepts an opaque hex, RGB or HSL seed and generates the source
   brand/grey ramps. Its sliders regenerate the source and reset stage 2.
   **Set as new base** copies the current hue/saturation into the seed field and
   chip at 50% lightness, keeps grey saturation, and resets stage 2 to match.
2. **Brand tuner** offers one **Remix colours** button instead of duplicate
   sliders. Every click starts from stage 1, preserves its hue and varies brand/
   Color-grey saturation and the lightness curve. Consecutive results differ.
   The saved result (including its tone) feeds harmony and semantics; regenerating
   stage 1 clears the remix. Exports retain the remixed ramps, and choosing brand
   as main also applies its tonal curve to the standard design-system ramps.
3. **Color theory** applies any of nine harmony patterns to stage 2, including
   accented analogous and double complementary. Choose 3–10 colours including the
   base (default four). Extra colours reuse the preset's hue anchors at varied
   lightness; monochrome varies lightness only. The count persists in saved
   themes and controls previews, main-colour options and exported tokens/classes.
   Older saved themes without a count retain four colours. Reducing the count
   moves an out-of-range main-colour choice to the last remaining colour.
   The preset radio buttons above the single preview stay synchronized with
   the sibling swatches and saved theme.
4. **Semantic Tuning** follows the active main palette's saturation and tonal
   character, with fixed hues: red 0, green 145, amber 42, purple 270, blue 210.
   All roles share the red's saturation/brightness settings. Sliders store
   saturation and lightness offsets, preserved when the main palette changes.
   Strong brightness starts from the page accent (42% light / 64% dark), adjusted
   by the source's tonal curve and selected harmony tone; weak starts at 92%/18%.
   Values are bounded to 0–100%. Semantics-as-main follows section 2's remix to
   avoid circular dependencies. Light/dark adjustments are independent and
   persist through Save/Load and builds. Older saved absolute semantic settings
   are preserved until adjusted, then converted to relative offsets.
   Fixed hue identity is **not a contrast/accessibility guarantee**.
5. **Color theme** previews the selected layer CSS. Choose one main system and
   optional extra systems, either at the top or beside stages 1–4. The main
   system is always included. Harmony mains can pick a sibling; semantic mains
   can pick a meaning. Previewing an excluded layer does not include it in export.
   Click a harmony swatch to select that sibling and activate harmony as main
   directly. The base swatch intentionally keeps the original hue. Harmony
   specimens retain their source colours without pinning the section's controls
   or captions to the source palette.
   When Harmony is main, the whole palette is applied by role: the base hue
   colours surfaces, sibling 2 colours headings, sibling 3 colours links and
   primary/secondary buttons, and sibling 4 colours borders (sibling 3 for a
   three-colour palette). Colours 5–7 cycle through heading levels h2–h6.
   Typography schemes respect those heading hues; semantic hues remain locked.
   Only one **Use as main system** button is active at a time, indicated by
   **Main system active** and its pressed state. Buttons and the main selector
   stay synchronized, including after loading. The main palette applies across
   the page; source, remix, harmony and semantic specimens keep their own palettes.

The main system supplies standard `--brand-h`, `--brand-s` and `--grey-s`.
Optional generated/refined ramps use `--theme-hsl-*` and `--theme-brand-*`;
harmony uses `--theme-harmony-*` plus standard sibling tokens; semantics uses
the standard meaning tokens and compatible `--c-*` aliases. Harmony and
semantic sources remain stage 2 even when another system is selected as main.
The full design-system build retains its baseline component defaults; excluding
a layer omits that layer's **custom additions**, not the baseline CSS.

`colorSystem` in saved/exported JSON stores both palettes, pattern, main
selection, included layers and mode-specific semantics. Copy/export, API builds
and CLI builds share the same colour generator. Optional custom editor CSS is
last and may intentionally override generated rules; no default editor rule
silently pins the generated colours.
Edit layered colour themes in `/site/`. The older single-palette tuner reports
this explicitly rather than loading a layered theme and silently saving changes
that its pipeline would ignore. Existing single-palette themes remain compatible.

The optional `connectors` record persists heading/body family and symbol settings.
Both API and CLI builds include its Google imports and styling. Schemes without
this field retain their previous output. The optional `customCss` string is appended after the
generated ingredient overrides in both API and CLI builds. Schemes without this
field produce the same output as before. Opening `/site/index.html` as a local
file supports previews, injection, CSS/JSON exports, JSON imports and browser-local
Save/Load. Full bundle builds need the Node server.

Run colour/connector/export regression tests with
`node --test src/color-system.test.mjs src/emit-css.test.mjs`.

### Earlier studio pages

Both studio pages share the same styling and interactive controls. In the
integrated reference, Light/Dark/System stays in the top rail, ingredient
controls sit in Tokens, and the harmony selector sits in Colour harmony.
Heading, depth, button, card, callout, accordion and icon demos update in place.
Section CSS-copy buttons and the icon gallery remain available.

Enter a theme name and **Save** the ingredient values. Select a saved theme
to load it, or use **Load**. **Build** builds the saved configuration, so save
again after changing ingredients. Download links serve the resulting CSS and
JSON from `/dist/<name>/`. Loaded override tokens are retained when saving.
Other demo modifiers and semantic lightness controls are preview-only; lightness
otherwise follows the selected light/dark mode.

Opening the HTML directly with `file://` supports local previews and exports,
but Save/Load/Build requires `npm start` and the HTTP page. These API controls
are disabled with an explanatory message when opened as a local file.
