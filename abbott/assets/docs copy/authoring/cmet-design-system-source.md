# CMET design system — source capture (Abbott's upstream system)

Status: **capture only**. This records the Cardiff Met design system Abbott
supplied (pasted from the live library-site CSS, 9–10 Oct 2026) so the Adapt
theme port builds from the authoritative source rather than a reconstruction.
Nothing here is applied to the live theme yet; the live theme tokens are in
`src/extensions/adapt-abbott-theme/less/` and are documented in
`theming-tokens.md`.

Every line below is tagged:
- **[SRC]** — copied verbatim from Abbott's pasted CSS (authoritative fact).
- **[INF]** — my inference from comparing sources; NOT yet confirmed by Abbott.
- **[RULING]** — a decision Abbott has stated.

**[RULING] (10 Oct 2026):** the full colour system — the complete extended
`--cm-*` palette plus the `--cmet-col-*` semantic/mode layer (§4) — is now the
**default/canonical** colour architecture for the theme, superseding the
smaller hand-built token set the live theme was built from. Abbott will supply
a **reference copy of the full CSS** to work from; the palette correction and
the architecture adoption happen against that copy, in one pass, not piecemeal.

**[RULING] (10 Oct 2026):** porting is accepted as a real LESS-adaptation job
(not a drop-in paste). **Cards and heroes are parked for now** — Abbott will
bring the full CSS as a reference to call on when that work starts.

**[RULING] (10 Oct 2026):** the live theme's custom-property **prefix is now
`--cm-*`** (was `--cmet-*`), matching the upstream base layer. The rename is
done across the live theme files and token docs. NB the subtlety: the upstream
system uses `--cm-*` for the base (palette, buttons, cards, spacing, type) and a
separate `--cmet-*` namespace for the semantic/mode layer (`--cmet-col-*`,
`--cmet-s-first..sixth`, `[cmet-lg-theme=…]`, §4). The `[SRC]` quotes below keep
that `--cmet-*` verbatim because it is Abbott's actual source. When the full
system is adopted from the reference copy, we settle whether that semantic/mode
layer keeps `--cmet-*` or also folds to `--cm-*`; our base tokens are `--cm-*`
from now.

The upstream system targets **Bootstrap 5 markup** (`.card`, `.row`,
`.container`, `.cm.btn`, `--bs-*`). Adapt renders React/JSX components, not
Bootstrap markup, so none of it ports wholesale — it is a design + token source,
and the component objects (cards, heroes, summary, callouts, practical-steps)
need Adapt-native rebuilds. See "Port plan" at the end.

---

## 1. Base colour palette (authoritative `--cm-*` block)

**[SRC]** The upstream base palette defines each colour as hex + rgb + hsl.
Captured values (this paste was **truncated** at sienna — "Show all properties
(200 more)" — so colours past sienna are NOT yet captured and must not be
invented):

| name | hex | rgb |
|---|---|---|
| white | `#ffffff` | 255 255 255 |
| white-subtle | `#fafafa` | 250 250 250 |
| light-blue | `#d0dfe8` | 208 223 232 |
| light-grey | `#f3f3f3` | 243 243 243 |
| dark-grey | `#6d6d6d` | 109 109 109 |
| dark-blue | `#0a2a3d` | 10 42 61 |
| black-subtle | `#1a1a1a` | 26 26 26 |
| black | `#000000` | 0 0 0 |
| red | `#6b0f1a` | 107 15 26 |
| jasper | `#ae362c` | 174 54 44 |
| tomato | `#f55d3e` | 245 93 62 |
| coral | `#f98948` | 249 137 72 |
| sienna | `#ab6621` | 171 102 33 *(rgb derived from hex; rgb line was truncated)* |

**[RESOLVED 10 Oct 2026]** The complete palette is now in the repo at
`cm-global.css` (root), "CM CORE COLORS" + accent blocks. Full authoritative set
(hex): jasper `#ae362c`, tomato `#f55d3e`, coral `#f98948`, sienna `#ab6621`,
khaki `#7c7f65`, bronze `#86775c`, brown `#8e6e53`, olive `#546857`, green
`#29524a`, teal `#237b80`, ocean `#2a6d7d`, aquamarine `#2e607a`, midnight
`#305276`, blue `#304573`, purple `#2a1f2d`, amethyst `#544154`, violet
`#82667f`, blossom `#aa7184`, pink `#d17b88`, greys-middle `#808080` (+ a
color-mix tint/shade grey scale 10–90). NB there is no distinct `orange`/`yellow`
in the base palette — `#ab6621` is **sienna** (what the warning semantic uses);
the earlier mention of orange/yellow was mine, not confirmed by the source.

**[SRC]** `white-subtle` upstream is `#fafafa` (250,250,250). The live theme
currently has `white-subtle: #f7fcff` (247,252,255) — a discrepancy to resolve
when the palette is corrected.

## 2. Corrections to the live palette — **APPLIED 10 Oct 2026**

`cm-palette.less` has been rebuilt from `cm-global.css`'s authoritative
palette (full extended set, comma-triplet `-rgb` form for `rgba()` consumption).
The corrections below are now live; the button dark-loop list
(`cmet-buttons.less`) was updated to the full accent set in the same pass.
The live `cm-palette.less` had been built from Abbott's **older** `--cmet-*`
block, which carried a bug and two misnamings against the authoritative set:

- **[SRC] coral bug.** Live palette has `--cmet-coral: #f55d3e` with
  `--cmet-coral-rgb: 249,137,72`. The hex and rgb disagree. Authoritative:
  coral is `#f98948` / 249,137,72. → fix the hex to `#f98948`.
- **[INF] `red2` is really `tomato`.** Live `--cmet-red2: #f55d3e` /
  `245,93,62` matches the authoritative **tomato** exactly. → rename
  `red2` → `tomato`.
- **[INF] `yellow` is really `sienna`.** Live `--cmet-yellow: #ab6621` /
  `171,102,33` matches the authoritative **sienna**. The upstream system has a
  *separate* `yellow` (and `orange`) among the uncaptured colours, so keeping
  `#ab6621` labelled "yellow" is a name collision. → rename `yellow` → `sienna`;
  add the real `yellow`/`orange` once their hexes arrive.
- **[SRC] jasper missing.** Add `jasper: #ae362c` / `174,54,44`.

These touch live token names used in `cmet-buttons.less` (the dark-colour loop
lists `yellow`, `red2`) and anywhere else — do the rename **once**, against the
complete palette, not piecemeal.

## 3. Semantic mappings (authoritative `:root`)

**[SRC]** From the practical-steps `:root`:

```
--cm-primary: var(--cm-dark-blue, #0a2a3d);
--cm-success: var(--cm-green,     #29524a);
--cm-warning: var(--cm-sienna,    #ab6621);
--cm-danger:  var(--cm-red,       #6b0f1a);
--cm-info:    var(--cm-teal,      #237b80);
```

These align with the live theme's `--cmet-primary → dark-blue`. The live theme
has no success/warning/danger/info aliases yet; these are the authoritative
values to add.

## 4. A parallel `--cmet-*` semantic/mode layer exists upstream

**[SRC]** Beyond the base palette, Abbott's system has a semantic + light/dark
mode layer already on the `--cmet-` prefix (not Bootstrap-coupled):

- `--cmet-col-1..6` (+ `-subtle`) mapping the 8 neutrals to a numbered scale:
  col-1 white, col-2 light-blue, col-3 light-grey, col-4 dark-grey,
  col-5 dark-blue (**[SRC]** still named `navy-blue` in this layer upstream —
  our rename to `dark-blue` must be carried here too if this layer is adopted),
  col-6 black.
- `--cmet-body-bg/text/border/outline-color-{primary,secondary,tertiary}` +
  `-rev-` reversed variants, all built from `--cmet-col-*`.
- `--cmet-s-first..sixth-{bg,text,border}-color` — six content "schemes".
- `[cmet-lg-theme=light]` scoping + `--cm-mode-color01..08` / `--cm-thm01..08`
  → a full light/dark + 8-theme mode system.
- Type scale `--cmet-h1-fs..h6-fs` (fluid `clamp()`), `--cmet-body-font-size:
  var(--cmet-font-size-fluid)` = `clamp(1rem, 1rem + 0.0625vw, 1.166rem)`.
- Spacing scale `--cm-space-025..600` (fluid clamps) + `--cm-gutter-x/y`.
- `--cmet-border-radius: 0.32rem` (matches the live foundation token).

**[INF]** This is a more complete semantic/mode architecture than the live
theme's hand-built tokens. Adopting it would mean replacing the live ad-hoc
semantic tokens with this numbered-scale + mode layer — a deliberate
architecture choice, not a drop-in. Flagged for Abbott; not assumed.

## 5. Component objects supplied (for Adapt-native rebuild, not paste)

All Bootstrap-markup; recorded as design intent for the component work (#13/#14):

- **Buttons** `.cm.btn` — full token-driven button object (primary/secondary/…
  colour variants, sizes sm/lg, link, focus/active/disabled states). Confirmed
  by Abbott as the canonical button set to adopt (supersedes the live
  `.btn-cmet`). Base `--cm-btn-*` tokens captured; port onto `--cmet-` + Adapt
  button markup.
- **Cards** `.cm.card` — Bootstrap card with colour variants (every palette
  colour), semantic variants (primary/success/…), functional variants
  (advice/action/starting/do/dont/feedback-pos/feedback-neg), icon support,
  hover-animate, full a11y (forced-colors, reduced-motion, touch targets).
- **Heroes** `.cm.hero` (`.svg-text`, `.icon-text`, `.video`) — colour
  modifiers, SVG bounce-in + colour-ripple animations, responsive float layout,
  Material Symbols icon support, dark-mode ripple.
- **Summary** `.cm.summary` — gradient panel, badge, gradient-text title,
  section-icon wrappers (colour gradients), definition/strategy/key-point/
  comparison/process-flow cards. Relevant to our lesson "Lesson summary" article.
- **Callout** `--cm-callout-*` — left-border callout with icon + header.
- **Tooltip** `.cm.tooltip` — dashed-underline help trigger (relates to our
  glossary tooltips).
- **Practical steps** — tabbed assessment/step cards with completion state.
- **Layout** — Bootstrap grid extended with an `xxxl` (1600px) breakpoint.

## 6. Port plan (proposed; Abbott rules)

1. **Palette first, once.** On the complete untruncated palette: fix coral,
   rename red2→tomato and yellow→sienna, add jasper + the rest, reconcile
   white-subtle. Carry the `navy-blue→dark-blue` rename into the `--cmet-col-5`
   layer if that layer is adopted.
2. **Semantic aliases.** Add success/warning/danger/info from §3.
3. **Buttons.** ~~Port `.cm.btn`.~~ **DONE 10 Oct 2026** — `cm-buttons.less`
   ports the full `.cm.btn` object (base, `.primary`/`.secondary`/`.link`,
   `.btn-outline-<semantic>`, a colour class per palette colour with the
   solid→outline hover, sizes, a11y) onto `--cm-*`; `.btn-cmet` retired
   (`cmet-buttons.less` removed). Semantic layer added to `theme.less`.
   NB (Abbott, 10 Oct): the semantic `success`/`danger` (brand green/red) suit
   the worked-example poor/good-practice scheme — the worked-example cues
   currently use their own brighter muted red/green; aliasing them to
   `--cm-danger`/`--cm-success` is a pending decision (brand red is a dark
   burgundy, less obviously "warning" at tint strength).
4. **Content objects.** Cards + callouts: **DONE 10 Oct 2026** — `cm-cards.less`
   (`.cm.card`, see `card-system.md`) and `cm-callouts.less` (`.cm.callout`:
   left-border box, named tip/note/warning/important + colour + accent variants)
   ported onto `--cm-*`. Still to do: summary and hero as Adapt-native
   (author-HTML patterns) under #13/#14.
5. **Mode/type/spacing layer.** Decide whether to adopt the upstream
   `--cmet-col-*`/mode architecture wholesale or keep the hand-built tokens.

## Open questions for Abbott

1. ~~The complete `--cm-*` palette.~~ **RESOLVED** — in `cm-global.css`; palette
   rebuilt (§2 applied).
2. ~~Adopt the upstream architecture, or keep hand-built tokens?~~ **RULED** —
   the full colour system is the default; `--cm-*` is our prefix. What remains is
   the *mechanics* of adopting the `--cmet-col-*`/mode/type/spacing layer and the
   component objects (cards/heroes/summary/callout), to be done against
   `cm-global.css` when that work starts (cards/heroes parked for now).
3. Still open: the brand **font family** (type sizes are in; `cm-global.css` uses
   a system-font stack — confirm whether a licensed brand face is wanted).
