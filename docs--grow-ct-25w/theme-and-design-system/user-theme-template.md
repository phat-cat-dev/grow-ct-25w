# User-theme template (the AB theme-scheme profile)

Models the CM design system in `cm-global.css` (the `--cmet-col-1..6` neutral
ladder + the three accent sets) **with a user-set seed layer behind it**. A user theme
author edits only **Section 1 (neutral seeds)** and **Section 3 (accent-set
bases)**; **Section 2 (the col ladder, light + dark)** proliferates from the
seeds by preset percentage. `--user-*` is instantiated per user theme (`--cm-*`,
`--sa-*`). CM's real `cm-global` values are shown as the worked example.

For CM, the user-set seeds **would have been**: `white-subtle`, `black-subtle`,
`dark-grey`, `dark-color` (navy-blue) + the accent-set base colours. Everything
else in `cm-global` derives from those.

> **Namespace note (important), reconciled to the six-layer model (11 Oct 2026):**
> `--cmet-*` is `cm-global.css`'s OWN prefix — the external CM design *source* we
> are modelling. We do **not** adopt `--cmet-*`. This doc describes the **L6 user
> profile** (and the L5 contract it fills) from `theming-layers-map.md` Part A.
> The `--user-*` tokens below are the generic **authoring placeholder**; per
> user theme they instantiate as the **L6 form `--<xx>-<stub>-*`** (e.g. CM's corporate
> profile → `--cm-corporate-*`, SA's → `--sa-<stub>-*`). The system tokens they
> feed are the six-layer ones: the **L5 theme contract** `--ab-theme-pf-<name>-*`
> and, through its hooks, the **L3 pivot** `--ab-base-*` over the **L4 defaults**
> `--ab-base-pf-<name>-*`. Where a `#hex` from `cm-global` is quoted below it is a
> *source value we model*, not a token we import.

---

## Section 1 — USER-SET layer (the seeds behind the ladder)

```css
:root {
  /* universal defaults — endpoints of EVERY hierarchy, never edited */
  --user-white: #ffffff;
  --user-black: #000000;

  /* the FOUR neutral seeds the user theme sets (CM's cm-global values shown) */
  --user-white-subtle: #f7fcff;   /* softened white — light ink-invert / top surface */
  --user-black-subtle: #1a1a1a;   /* softened black — ink / bottom surface           */
  --user-dark-grey:    #6d6d6d;   /* base dark NEUTRAL grey  (cmet col-4)             */
  --user-dark-color:   #0a2a3d;   /* base dark USER THEME colour  (cmet navy, col-5)       */

  /* + the accent-set bases — Section 3 */
}
```

---

## Section 2 — NEUTRAL SET (the col-1..6 ladder, holistic light + dark)

The ladder is symmetric: the LIGHT half (col-1→3) mirrors the DARK half
(col-6→4). Only the dark seeds are user-set; the light mirrors **derive** by
lightening, and the two subtles + the endpoints are fixed. This is exactly
`cm-global`'s `--cmet-col-*`, re-expressed over the seeds.

```css
:root {
  --user-lighten: 92%;   /* preset: how far a dark seed lifts to its light mirror */

  /* LIGHT half -------------------------------------------------- */
  --user-col-1:        var(--user-white);          /* page            (cmet-white)        DEFAULT */
  --user-col-1-subtle: var(--user-white-subtle);   /* raised surface  (cmet-white-subtle) USER    */
  --user-col-2:        color-mix(in srgb, var(--user-dark-color) 18%, #fff 82%);  /* light user theme (≈cmet light-blue #d0dfe8) DERIVED from dark-color */
  --user-col-3:        color-mix(in srgb, var(--user-dark-grey) calc(100% - var(--user-lighten)), #fff var(--user-lighten));  /* light grey (≈cmet #f3f3f3) DERIVED from dark-grey */

  /* DARK half (reverse) ---------------------------------------- */
  --user-col-4:        var(--user-dark-grey);      /* dark grey       (cmet col-4)  USER    */
  --user-col-5:        var(--user-dark-color);     /* dark user theme      (cmet col-5)  USER    */
  --user-col-6-subtle: var(--user-black-subtle);   /* near-black      (cmet-black-subtle) USER */
  --user-col-6:        var(--user-black);          /* black           (cmet-black)  DEFAULT */

  /* SEMANTIC mapping (as cm-global: body bg + its reverse for dark) ---------- */
  --user-bg-primary:     var(--user-col-1);   --user-bg-secondary:     var(--user-col-2);   --user-bg-tertiary:     var(--user-col-3);   /* LIGHT surfaces */
  --user-bg-rev-primary: var(--user-col-6);   --user-bg-rev-secondary: var(--user-col-5);   --user-bg-rev-tertiary: var(--user-col-4);   /* DARK surfaces  */
  --user-border-primary: var(--user-col-3);   --user-border-secondary: var(--user-col-2);
  --user-ink:            var(--user-col-6-subtle);   /* text on light */
  --user-ink-invert:     var(--user-col-1-subtle);   /* text on dark  */
}
```

**Light↔dark** is then the `cm-global` move: a `[theme=dark]` block swaps the
`bg-*` roles to the `bg-rev-*` set and `ink`↔`ink-invert`. Same ladder, mirrored
— no new colours.

---

## Section 3 — ACCENT layer (sets of bases, as `cm-global`)

`cm-global` carries **three accent sets of four** (set 1: red/teal/khaki/violet;
set 2: yellow/blue/green/purple; set 3: coral/red2/brown/pink). In the template a
user theme declares **as many accent GROUPS as it wants**, each a **user-set base** +
a **derivation profile** that proliferates its states.

```css
:root {
  /* the user-set bases (CM set 1 shown) */
  --user-accent-red:    #6b0f1a;
  --user-accent-teal:   #237b80;
  --user-accent-khaki:  #7c7f65;
  --user-accent-violet: #82667f;
  /* …sets 2 & 3 the same way — add as many as the user theme needs… */
}

/* each base proliferates the SAME state set by its profile (AB runs this): */
/*   -hover / -active / -deep  = shade ramp (toward #000)                    */
/*   -tint / -line             = pale wash / hairline (toward surface)       */
/*   (optional) light/dark variants, mirroring the neutral set              */
```

### How the accent layer works for user theme profiles — PROPOSAL (to confirm)
- An accent group = **`base` + `profile`**. Profiles:
  - **shade** — states by lightness ramp off the base (a solid accent).
  - **companion** — base is a hue offset from another group (complementary/
    analogous/triadic — the AB colour-theory engine) + its own shade states.
  - **mono** — tints/shades only, no hue shift (status chips, neutch accents).
- A user theme lists N groups by name (`red`, `teal`, …); components pick a group by
  name. CM's three sets = twelve `shade` groups.

**Open points (to settle before building the accent layer):**
1. State set per group — is `hover/active/deep/tint/line` enough, or do accents
   also need the light/dark flip the neutrals have?
2. Store a group's base as hex, or as H/S/L channels? (channels are needed for
   the `companion` profile's hue maths.)
3. How a component selects a group — a class, or a slot-level `_classes` hook.

---

## Section 4 — TYPOGRAPHY (user theme fonts)

Fonts are a user theme concern (the user theme picks its faces), so they live in the user theme
template — NOT in AB base, which owns only the fluid type *scale* (ratios +
clamps, rarely changed). Not present in `cm-global`; this is the typical set a
user theme profile needs:

```css
:root {
  /* the user theme's font FAMILIES (the two primaries + mono) */
  --user-font-sans:  system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;  /* sans primary */
  --user-font-serif: Georgia, "Times New Roman", serif;                         /* serif primary */
  --user-font-mono:  ui-monospace, "SF Mono", Menlo, Consolas, monospace;       /* code / data readout */

  /* ROLE assignment — which family headings vs body use (the user theme decides) */
  --user-font-heading: var(--user-font-sans);   /* e.g. a serif user theme sets this to --user-font-serif */
  --user-font-body:    var(--user-font-sans);

  /* optional user theme weight choices (the scale owns sizes, the user theme owns weight) */
  --user-weight-heading: 600;
  --user-weight-body:    400;
}
```

AB's type ladder sizes everything; these dials decide the FACE + weight. A serif
user theme just repoints `--user-font-heading` (and/or `-body`) at `--user-font-serif`.

**Fonts may be named as Google Fonts** — the user theme gives the family name; a BUILD
step fetches + subsets + **self-hosts** it (⚠ SCORM/Moodle ship offline, so fonts
are never runtime-linked to Google — they are extracted into the package).

---

## Section 5 — ICON SETS (Google Material Symbols, modular packs)

The user theme declares named icon **GROUP PACKS** — each is just a group name + a
list of Google Material Symbol names. A build step **extracts a profile** from
each pack: a subsetted symbol **font** PLUS per-icon **SVG** (and any other
output format), **self-hosted** (exactly as today's `cm-icons` self-hosts
Material Symbols → becomes `ab-icons`). Same offline constraint as fonts —
declared by Google name, shipped as self-hosted assets.

Keep packs **individual / modular** so a project pulls only what it needs:

```css
/* the user theme DECLARES packs in its L6 profile (--<xx>-<stub>-iconset-<group>): */
--cm-corporate-iconset-academic-practice: starting progressing graduating writing researching …;  /* google symbol names */
--cm-corporate-iconset-cite-source:       book article language_us web movie podcast …;

/* …and binds each into the L5 theme contract the base reads: */
--ab-theme-pf-default-iconset-academic-practice: var(--cm-corporate-iconset-academic-practice);
--ab-theme-pf-default-iconset-cite-source:       var(--cm-corporate-iconset-cite-source);
```

A pack's icons **pipe in where that content type appears** — e.g. the
`cite-source` pack is used wherever citation source types are presented in a
project, wired through the template/`_classes` layer (the same seam that carries
styling hooks + `agentAuthor`). So an icon pack is a *content-type → icon*
contract, not just decoration.

**Build tooling implied:** an `ab-icon-extract` / `ab-font-fetch` step that turns
the declared Google names into self-hosted font subsets + SVGs at build time.

## How this feeds AB (the six-layer join)
A user theme file (the **L6 user profile** `--<xx>-<stub>-*`, e.g. `--cm-corporate-*`)
is **Sections 1 + 3** (the seeds + the accent-set bases). Section 2 is the shared
proliferation AB runs for every user theme. The profile **binds its outputs into the
L5 theme contract** (`--ab-theme-pf-<name>-*`), which the **L3 pivot** reads over
the **L4 defaults**:
```css
--ab-theme-pf-default-surface: var(--cm-corporate-bg-primary);   /* L6 → L5 */
--ab-theme-pf-default-ink:     var(--cm-corporate-ink);
--ab-theme-pf-default-accent:  var(--cm-corporate-accent-teal);  /* the chosen accent group */
/* L3 then resolves: --ab-base-surface: var(--ab-theme-pf-default-surface, var(--ab-base-pf-default-surface)); */
```
So `--ab-base-surface` ← (L5) `--ab-theme-pf-default-surface` ← (L6) the user theme's
`--<xx>-<stub>-bg-*` per mode; `--ab-base-ink` ← the user theme's `-ink`/`-invert`;
`--ab-base-accent` ← the chosen accent group. Anything the user theme leaves unset
falls through to the L4 `--ab-base-pf-default-*` default.

## SA (placeholders for now)
`sa-user` fills Sections 1 + 3 with SA's own values — same structure, different
numbers. Pending SA's real colours; scaffold carries clearly-marked placeholders.
