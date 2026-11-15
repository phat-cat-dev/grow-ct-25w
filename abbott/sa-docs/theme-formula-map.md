# Default formula map (theme / sub-theme / semantic sets)

The AB rule: **a theme, sub-theme or semantic set exposes only a few authorable
seeds; the default formulas below proliferate everything else.** Those formulas
become the **L4 base-profile defaults** (`--ab-base-pf-default-*`); the authorable
seeds are surfaced in the **L5 template**; an **L6 user profile / sub-theme** sets
or overrides them. Every derived token is a pivot hook `--ab-base-X:
var(--ab-theme-pf-default-X, var(--ab-base-pf-default-X))`, so an explicit L5/L6
value always wins over the formula.

HSL is the engine throughout (verified live in `ab-schemes.less` /
`ab-colour-profiles.less`); values below are the current live defaults.

---

## 1. The authorable seeds (the only hand-set values)

**Theme** (e.g. CM corporate — the fixed foundation):
- `neutral-h`, `neutral-s` — the grey spine's tint (today `202 / 0%` = pure grey).
- the neutral endpoints: `white`, `black`, `white-subtle` `#fafafa`, `black-subtle` `#1a1a1a`.
- the lightness ladder `l-*` (rarely touched).
- the accent **palette** — named colours a sub-theme may promote.

**Sub-theme** (e.g. corporate / midnight — one dial does the work):
- `primary-h`, `primary-s` — the chosen primary's hue + saturation (a hex is read into these).
- `spine` — `brand-tinted` (greys carry the hue) or `neutral` (pure grey).
- (optional) any explicit override of a derived token.

**Semantic sets** (positive / negative / neutral):
- per-category `*-hue` dial — `positive 145`, `negative 5`, `neutral 38`.
- shared `semantic-s`, `semantic-l`.
- per set + sub-category `*-icon` (a Material Symbol name).

**Accent spectrum** (the 12-family named palette — one dial does the work):
- the **dark-neutrals**: `black-subtle`, `dark-grey` (achromatic, stay constant),
  `dark-color-1` (mandatory — the primary dark-neutral), `dark-color-2`,
  `dark-color-3` (optional).
- that is the whole authorable surface: `dark-color-1`'s hue, saturation and
  shade-depth seed all 12 families (see §2.8). The greys are not families.

Everything below is **derived** from these.

---

## 2. Default formulas

### 2.1 Primary / accent chain — from `primary-h`/`primary-s` + a lightness ladder
`accent-l` = `user-l` (14%) light · `62%` dark.
```
accent        = hsl(primary-h  primary-s  accent-l)
accent-hover  = hsl(primary-h  primary-s  calc(accent-l - 2%))
accent-active = hsl(primary-h  primary-s  calc(accent-l - 4%))
accent-deep   = hsl(primary-h  primary-s  calc(accent-l - 6%))
accent-tint   = hsl(primary-h  calc(primary-s * 0.5)  95%)        // pale wash
accent-line   = hsl(primary-h  primary-s  accent-l / 0.2)          // translucent hairline
accent-ring   = hsl(primary-h  primary-s  55%)                     // focus ring
```
(`primary-h/s` ARE the theme's `user-h/s`; a sub-theme just resets them.)

### 2.2 Neutral spine + grey ramp — from `neutral-h`/`neutral-s` + `l-*` stops
`l-*` light/dark: surface `100/14` · subtle `98/18` · sunken `95/9` · hairline `88/32` · ink-muted `43/62` · ink `10/92` · on-accent `100`.
```
surface | surface-subtle | surface-sunken | ink | ink-muted | hairline | on-accent
              = hsl(neutral-h  neutral-s  l-<role>)
greys-light-N = color-mix(neutral-base,  #fff, N%)      // neutral-base = hsl(neutral-h neutral-s 50%)
greys-dark-N  = color-mix(neutral-base,  #000, N%)
```

### 2.3 Brand-tinted dark anchor — NEW (how a sub-theme "replaces the dark-blue")
The deep end of the neutral ladder (`dark-colour` / `col-5`, navy today) is the
**primary at brand-dark lightness**, so promoting a new primary re-tints it:
```
theme-dark = hsl(primary-h  primary-s  L_brand_dark)     // L_brand_dark = 14% (= user-l)
```
`spine` switch:
- `brand-tinted` → `neutral-h = primary-h`, `neutral-s ≈ 6%` (greys lean to the hue).
- `neutral` (today's default) → `neutral-s = 0%` (pure grey); `theme-dark` still exists as a distinct token for chrome that wants the deep brand.

### 2.4 Heading tiers — a rule, not a per-pack list
```
h1-color = accent (the primary)
h2-color = ink-muted            // the "blue-grey" look = h1 primary + h2 neutral, derived
h3..h6-color = ink
```

### 2.5 Companions (colour-theory profiles) — `primary-h` rotated
At shared `companion-s 55%`, `companion-l 45%`:
```
complementary = hsl(calc(primary-h + 180) companion-s companion-l)
split-a/-b    = hsl(calc(primary-h + 150 | + 210) …)
analogous ±   = hsl(calc(primary-h ± 30) …)
triadic a/b   = hsl(calc(primary-h + 120 | + 240) …)
```

### 2.6 Semantic sets — NEW. Per-category hue × shared sat/light, icon per set/sub-category
`semantic-s` default = `companion-s` (nudged by `neutral-s`); `semantic-l ≈ 42%`.
For each category `X` in {positive 145, negative 5, neutral 38}:
```
X-base        = hsl(X-hue  semantic-s  semantic-l)              // border / accent / icon-colour
X-bg          = hsl(X-hue  calc(semantic-s * 0.5)  94%)         // pale card wash
X-ink         = hsl(X-hue  semantic-s  28%)                     // AA-dark text on the wash
X-icon-colour = X-base
X-icon        = <placeholder symbol>                            // positive check_circle · negative cancel · neutral info
```
A **sub-category** reuses its parent's colour tokens and sets only its own icon + name:
```
positive-correct  → X=positive, icon check_circle
positive-advise   → X=positive, icon lightbulb
negative-incorrect→ X=negative, icon cancel
negative-warn     → X=negative, icon warning
neutral-observe   → X=neutral,  icon visibility
```
The format class (`.ab-positive-advise`, …) is a first-party card that reads these
tokens and auto-injects the icon via the self-hosted Material Symbols font —
no vanilla adapter needed (it consumes L3 directly).

### 2.7 Dark mode — a seed flip, nothing re-authored
Dark overrides only the lightness dials (`l-*`, `accent-l`); every role and the
accent chain re-derive, so the whole spine recomputes for dark with no rule changes.

### 2.8 Accent spectrum — NEW. 12 named families, all cascading off `dark-color-1`
Schema: `design-kb/section-schemas/accent-spectrum.json`. This is the full named
palette an author reaches for (`accent-blue-dark-80`, …), distinct from §2.1's
UI primary chain. The **only** hand-set values are the dark-neutrals (§1); the
whole spectrum spins out of **`dark-color-1`**.

**Seed read (once, from `dark-color-1`):**
```
primary-h    = hue(dark-color-1)          // also §2.1 user-h and the §2.3 brand-dark hue
accent-s     = sat(dark-color-1)          // shared chroma for every family
anchor-shade = shadeDepth(dark-color-1)   // % mix toward black that reproduces its L, e.g. 84
anchor-band  = round10(anchor-shade)      // e.g. 80 — the label the anchor snaps to
offset       = anchor-shade - anchor-band // e.g. +4
```

**The 12 families** (fixed, absolute hues — not brand-rotated). Blue is the 9th:
```
red 0 · orange 30 · amber 55 · lime 90 · green 130 · emerald 160 · teal 185
· azure 205 · blue 225 · indigo 265 · violet 295 · rose 330
```

**The ladder (A-v2, ruled 12 Oct 2026).** Band labels are the fixed round set
`10..90`; a band's true mix-% = `label + offset`, so labels stay clean and
identical across families while values ride true to the chosen colour. Per
family `F` (hue `Hf`), base `= hsl(Hf accent-s 50%)`:
```
accent-F-dark-L  = color-mix(in srgb, base, black  (L + offset)%)   // toward black
accent-F-light-L = color-mix(in srgb, base, white  (L + offset)%)   // the mirror, toward white
```
The family `dark-color-1` names (nearest `Hf`) carries it at the anchor rung:
```
accent-<familyOf(primary-h)>-dark-<anchor-band> = dark-color-1
```
So picking a dark-blue at 84 gives `accent-blue-dark-80` (= the colour itself,
value 84), the full blue ladder around it, and the other 11 families at their
fixed hues sharing `accent-s` and `offset` — one choice, the whole spectrum.
`dark-color-2`/`-3` optionally pin a second/third family (colour-theory rotation
off `dark-color-1`, or a manual hex).

**Named overrides.** The 20 CM curated colours (`ab-palette.less`) pin specific
family rungs where the house palette differs from this formula default (e.g.
`--ab-theme-pf-default-tmp-default-1-mono-accent-blue-dark-80: var(--cm-corporate-navy)`).
An unoverridden rung keeps its derived value.

**Tokens** (full grammar §4): L5 authorable
`--ab-theme-pf-<theme>-tmp-<subtheme>-<n>-<formula>-accent-<family>-<dark|light>-<NN>`, L4 default
`--ab-base-pf-default-accent-…`, L3 pivot `--ab-base-accent-…` = `var(L5, L4)`.

### 2.9 Neutral endpoints + grey scale — `white-subtle` source, grey mode (ruled 12 Oct 2026)
The always-set darks are `black-subtle`, `dark-grey`, `dark-color-1` (§1). Two
neutral behaviours are **end-user choices** surfaced in the L5 template, each with
a safe default:

**`white-subtle`** — the near-white endpoint (light-mode surface) is DERIVED, not
hand-set, with a `source` choice and a manual `nudge`:
- `source: mirror` (default) — the lightness invert of `black-subtle`.
- `source: primary` — a faint theme tint (the invert/pale of `dark-color-1`): a
  warm or cool off-white cohesive with the palette.
- both start at the plain invert of their source; `nudge: ±N%` (default `0%`)
  shifts it a little lighter or darker from there.

**Grey scale** — the grey ladder is built off `dark-grey` with the A-v2 band
mechanics (round labels `10..90`, offset on the grey's own depth): a first-class
laddered family, used heavily in dark mode. `mode`:
- `pure` (default) — zero saturation, true neutral grey.
- `neutral-tinted` — ~4–6% of the set neutral hue, so the greys read as part of
  the palette (the §2.3 `spine` switch, generalised to the whole ladder).

---

## 3. Presentation (L5) and definition (L6)

- Each block above is a **section schema** (`design-kb/section-schemas/*.json`):
  colour (live), semantics (new), accent-spectrum (new), sub-theme/primary (new). The fold tool projects
  each into the L4 defaults, the L3 hooks, and the **L5 template** — the authorable
  seeds (the few in §1), presented as named fields.
- A **sub-theme** is an L6 instance: it sets `primary-h/s` (+ `spine`, + any icon or
  explicit override) under `--<xx>-theme-<name>-<subtheme>-*` and binds them into the
  L5 contract; the formulas above fill the rest.
- A **semantic override** is the same: a user theme nudges `positive-hue`, swaps
  `positive-advise-icon`, or slams an explicit `positive-bg` at L5/L6.

So authoring a sub-theme = name it + pick a primary (two dials); authoring a
semantic palette = three hues + a couple of shared dials + icon names. The map
above is what turns those into the full token set.

---

## 4. Namespace grammar — template vs published

Every theme-profile colour token carries its full role in the TEMPLATE layers
(L4 defaults, L5 theme template) and a shortened, role-marker-free form once
PUBLISHED to a locked user scheme (L6). Ruled 12 Oct 2026.

```
Template  (L4 / L5):  --<xx>-theme-pf-<theme>-tmp-<subtheme>-<n>-<formula>-<token-path>
Published (L6 locked): --<xx>-thm-<theme>-<subtheme>-<n>-<formula>-<token-path>
```

**Slots:**
- `<xx>` — vendor stub (`ab`).
- `<theme>` — user theme name (`default`, `cm-corporate`, …).
- `<subtheme>` — sub-theme name (`default`, `midnight`, …). Structural roles
  (`neutral-dark`, `dark-grey`, `black-subtle`, `white-subtle`, `accent-*`) are
  NOT sub-theme names — they live in `<token-path>`.
- `<n>` — colour-count mode: `1` | `2` | `3` (how many neutral-dark anchors set).
- `<formula>` — colour-theory set: `mono` (the base, un-rotated cascade) +
  `complementary` | `split-a` | `split-b` | `triad-a` | `triad-b` |
  `analogous-lo` | `analogous-hi`.
- `<token-path>` — the role (`accent-blue-dark-80`, `neutral-dark-grey-40`,
  `white-subtle`, `surface`, `ink`, …).

**Publish transform** (template → published): `theme-pf-<theme>-tmp-<subtheme>`
→ `thm-<theme>-<subtheme>`, i.e. `theme-pf` → `thm` and `tmp` dropped. The
`-pf-`/`-tmp-` markers define role in the authoring layers only; a locked scheme
needs neither, so the publish step strips them.

**`<formula>` sets are OPTIONAL engine output** (R2): every set is generated as
an L4 default and hooked at L3 (the base engine), so it rides the cascade whether
or not a theme touches it — a token names its set only to pick which generated
palette it belongs to; a sub-theme overrides a token only to deviate from the
engine default. No per-sub-theme authoring is needed to get the rotation sets.

**Count modes:** `1` is defined (§2.8 — one anchor cascades secondary neutrals +
accents via each formula set). `2` and `3` (two / three neutral-dark anchors, for
2–3 primary foreground colours) are named stubs — only wanted for multi-primary
themes, designed when one appears. The key open question when designing them: **how
2–3 darks split the neutral spine** — one drives surfaces, another ink/borders, or
they alternate down the grey ladder? Starting proposal (12 Oct 2026): anchor-1
still drives the grey spine + the 12-family rotation (as `n=1`); anchors 2/3 become
additional PINNED primaries (their families pinned, optionally promoted to a
`secondary-accent` role), with accent auto-derivation off them opt-in.

**Scope of `<n>-<formula>`** (ruled 12 Oct 2026 — omit for structural): these two
slots belong to the colour cascade (accents, colour-theory families, the
neutral-colour spine) only. Structural / typographic tokens (radius, fonts,
motion) have no count or rotation dimension and carry only
`theme-pf-<theme>-tmp-<subtheme>-<token>` — two clean grammar shapes, each varying
on only what it actually varies on.

**Live migration is phased, not a quiet edit.** The existing live namespace is
`--ab-theme-pf-default-*` across `ab-schemes.less`, `ab-semantics.less`, the
packs, the fold tool's `THEME` constant and the L5 template. Moving it onto this
full grammar is a phased, build-tested rename (as the AB/CM rename was), separate
from recording the grammar here. The accent spectrum (§2.8) is greenfield and is
authored in the new grammar directly.

---

## 5. Greyscale transform — design + delivery mode (stub, ruled luminance-corrected)

A transform that renders a whole theme (or sub-theme) in greys — every accent,
family and role collapsed to its grey equivalent. Two uses: a **delivery mode**
(monochrome variant for accessibility, print, low-distraction, or a deliberately
mono aesthetic) and a **design mode** (author in greyscale so value / shading /
layering carry the hierarchy, then reintroduce colour — grey layering is powerful,
especially in dark mode).

**Desaturation is luminance-corrected** (ruled 12 Oct 2026), not a plain `S→0`:
HSL lightness is not perceived brightness (a yellow and a blue at equal `L` look
identical desaturated yet read very differently), so each token maps to its
*perceptual* grey. Pure `S→0` is the cheap approximation; luminance-correction is
the chosen target — build-test may stage pure first and correct if the flats read
wrong.

**Shape (stub):** a theme-level `greyscale` mode that routes every colour token
through the desaturation, AND optionally `formula=greyscale` as a named set so a
single element can be greyed within a colour theme. Exact mechanics (which
luminance weights; whether it runs at L3 engine or publish time) are to be
designed when built.
