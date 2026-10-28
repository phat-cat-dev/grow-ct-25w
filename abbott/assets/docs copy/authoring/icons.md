# Icons — CM academic-practice symbols (Google Material Symbols)

Icons are Google **Material Symbols** (Apache-2.0). The academic-practice set is
ported from the authoritative CM source (`cm-global.css`,
`/public/css/cm-utility-icons.css`) into
`src/extensions/adapt-ab-theme/less/cm-icons.less`. A generic ligature helper
(`.cmet-icon`) also lives in `cmet-icons.less`.

## Two mechanisms, same glyphs

Every named icon ships in two forms:

- **SVG** — `.cm icon-<name>-svg`. A self-contained `mask-image` data-URI,
  coloured by `currentColor`, infinitely scalable, **needs no font**. **Prefer
  this for shipped SCORM**: it works fully offline and adds only a few bytes.
- **Font** — `.cm icon-<name>`. A ligature glyph from the self-hosted Material
  Symbols Outlined woff2 (see below).

```html
<span class="cm icon-learning-svg" aria-hidden="true"></span>   <!-- SVG, offline-safe -->
<span class="cm icon-learning" aria-hidden="true"></span>        <!-- font ligature -->
<span class="cm icon-assessment-svg" role="img" aria-label="Assessment"></span> <!-- meaningful -->
```

Decorative icons take `aria-hidden="true"`; a meaningful icon takes an
`aria-label` (and `role="img"`) instead.

## Colour and size

Colour **either** kind by setting `color` — the SVG mask uses `currentColor`, the
font glyph is the text colour. Ready modifier classes (on the brand palette
tokens) come from a loop in `cm-icons.less`:

```html
<span class="cm icon-feedback-svg dark-blue"></span>
<span class="cm icon-wellbeing-svg teal"></span>
```

Sizes: `icon-sm` (1rem), `icon-md` (1.5rem), `icon-lg` (2rem), `icon-xl` (3rem) —
one class sizes both the font (font-size) and the SVG (width/height).

## The named set

21 icons have **both** font + SVG: starting, progressing, graduating, wellbeing,
learning, assessment, feedback, integrity, finding, studying, referencing,
researching, writing, presenting, reflecting, revising-exams, criticality,
creativity, international, ai-technology, signpost. A further ~12 resource/library
icons are **SVG-only**: book, bookchapter, bookmark, digital-learning-activity,
homepage, panopto, podcast, video, worksheet, workshop, workshop-learning-activity,
youtube.

## The font pack (offline-safe, self-hosted)

The font is **self-hosted**, not loaded from Google at runtime:
`fonts/material-symbols-academic.woff2` (~188KB). It was produced from the full
variable woff2 (~3.9MB) by:

1. **Instancing** the variable font to a static cut:
   `fonttools varLib.instancer <full>.woff2 FILL=0 wght=400 GRAD=0 opsz=24`.
2. **Subsetting** to exactly the 21 ligatures used:
   `pyftsubset <static>.woff2 --text="article bolt co_present collections_bookmark
   feature_search feedback frame_inspect globe_asia lightbulb local_library memory
   palette policy rocket_launch school signpost spa stairs_2 sync target timer"
   --layout-features='liga,dlig,rlig,calt,ccmp' --flavor=woff2
   --output-file=fonts/material-symbols-academic.woff2`.

`@font-face` (in `cm-icons.less`, `url("../fonts/material-symbols-academic.woff2")`)
is used rather than `@import` because Adapt compiles one concatenated `adapt.css`
and `@import` only works at the very top of a stylesheet. The build copies the
font via `copy:extensionFonts` to `build/course/fonts/`.

**Adding a font icon later:** add its `.cm icon-<name>::before { content: "<lig>" }`
rule, add the ligature to the `--text` list, and re-run the instance+subset above.
Or — simplest — add only the SVG variant (no font change needed).

## Seeding more icons from the CM source

More icon definitions (and the colour/size/transform/animation modifiers) exist in
`cm-global.css`'s `cm-utility-icons.css` section. Port additional ones the same
way: copy the `.cm.icon-<name>` font + `-svg` rules across; the colour loop and
sizes already cover them.
