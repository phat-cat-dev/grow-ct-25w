# Theming layers map — how our tokens sit on top of Adapt

A map of the CSS layers a build assembles, from the **renderer (Adapt vanilla) at
the bottom** to **our user-theme skin at the top**, and how our tokens map onto the
literals the renderer bakes in.

This doc carries **two pictures**:

- **Part A — TARGET (post-rename AB cascade).** The six-layer model worked out
  with Abbott (11 Oct 2026), the shape after the `--cm-*` → `--ab-*` rename
  (`ab-cm-rename-spec.md`). Its spine is **two seams and a pivot**: a renderer
  adapter (seam 1), the portable `--ab-base-*` token API (the pivot), and a theme
  interface (seam 2) that a user-theme profile fills. **Not yet in code** — AB is
  blueprint only (0 `--ab-*` refs today; the code is still `--cm-*`). Consistent
  with `ab-system-architecture.md`.
- **Part B — CURRENT (`--cm-` / `html.cm-theme` gate).** What is actually in the
  LESS right now, after the `html.cm-theme` gate landed (11 Oct 2026). The
  truthful live-code reference, and the thing the build-test validates before the
  rename runs.

Read Part A for where we are going; read Part B for what compiles today. The
rename is the bridge between them and is **gated on the build-test** — nothing in
Part A is executed until Part B is confirmed to render.

Companion docs: `ab-system-architecture.md` (the master blueprint),
`ab-cm-rename-spec.md` (the rename that turns B into A),
`user-theme-template.md` (the user-theme seed/colour model),
`cm-theme-architecture.md`, `cmet-design-system-source.md` (the palette origin),
`colour-schemes.md`.

---

## 0. The one counter-intuitive fact (true in BOTH pictures): vanilla compiles LAST

Adapt's Grunt build (`grunt/config/less.js`) globs LESS in this order and
concatenates it into one `adapt.css`:

```
1. src/components/*/less     ← adapt-contrib-* AND our adapt-abbott-* components
2. src/extensions/*/less     ← adapt-contrib extensions AND our theme extension (all the *.less)
3. src/theme/*/less          ← adapt-contrib-vanilla  ← COMPILED LAST
```

Within a folder the order is alphanumeric. **Last-compiled wins any tie on equal
specificity** — so **vanilla overrides our extension** whenever specificity is
equal. That is the whole reason our adapter rules need either **higher
specificity** (the gate prefix) or **`!important`**, or both. It is not
decoration; it is structural. (Source: the header of `vanilla-overrides.less`.)

So "source order" and "who wins" run opposite ways:

```
SOURCE ORDER (what the file concatenates)        CASCADE OUTCOME (who wins a tie)
  components  (first)                              vanilla      (wins — compiled last)
  extensions  (… our theme .less here …)           our adapter only wins via
  vanilla     (last)                               !important / gate specificity
```

This fact is why the **adapter layer** (Part A's seam 1, Part B's gated sweep)
exists at all: to out-specify the renderer and re-point its baked-in literals at
our portable tokens. It is renderer-specific — a different renderer (a JSX build)
would not have this compile-order quirk and its adapter would look different, but
the layers below the adapter would be identical.

---

# PART A — TARGET: the AB cascade (post-rename, blueprint)

**Status: not yet in code.** The six-layer model, worked out with Abbott (11 Oct
2026). Top (the renderer) → bottom (the user's own values). The spine is **two
seams meeting at one pivot**:

- **SEAM 1** — renderer ⇄ portable API — the **adapter** (layer 2). Swap the
  renderer (Adapt → JSX), only this moves.
- **THE PIVOT** — layer 3, `--ab-base-*` — the stable token API both sides meet
  at. Adapters point *up* into it; it reaches *down* for its values. Its *names*
  never move.
- **SEAM 2** — base ⇄ theme — the **theme interface** (layer 5). Evolve the theme
  system, only this (and its hooks) move.

## A1. The six layers

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 1   RENDERER                 instance: adapt-vanilla (a JSX lib later)       │
│   Stock Adapt: bakes LITERALS (@item-color #117F93, @greyDark, @validation-*,      │
│   fixed radius/spacing/sizes) in its OWN vocabulary. Not ours; never edited.       │
│   Compiles LAST → wins equal-specificity ties.                                     │
│                              ▲ seam rules paint the renderer's selectors            │
├─────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 2   ADAPTER  (seam 1)        tokens: --ab-base-if-<renderer>-*                   │
│   The ONE layer that speaks the renderer's vocabulary — renderer-specific, one      │
│   active per build. Holds the seam RULES + renderer-named tokens mirroring the      │
│   renderer's NAMED vars 1:1:                                                       │
│     --ab-base-if-adapt-item-color    ← @item-color                                    │
│     --ab-base-if-adapt-heading-color ← @heading-color     --ab-base-if-adapt-greydark …  │
│   Rule:  html .mcq-item__label { background: var(--ab-base-if-adapt-item-color) !important }│
│                              │ SEAM 1 (ALIAS):  --ab-base-if-adapt-item-color: var(--ab-base-accent);│
│══ PORTABILITY LINE — everything below is framework-agnostic ══════════════════════│
│ LAYER 3   PORTABLE API — THE PIVOT         tokens: --ab-base-*                      │
│   The ab-base system's public surface, by ROLE, in our vocabulary — knows nothing  │
│   of any renderer or theme. Every adapter points up into it; components read it.   │
│     --ab-base-accent /-hover/-active/-deep   --ab-base-surface /-subtle/-sunken     │
│     --ab-base-ink /-muted  --ab-base-hairline  --ab-base-on-accent                  │
│     --ab-base-success/-danger/-info  --ab-base-h1..h6-color                         │
│     --ab-base-space-*  --ab-base-step-*  --ab-base-radius  --ab-base-page-max …      │
│   Each holds NO literal — it is a hook: theme-if-present, else base default:        │
│     --ab-base-accent: var(--ab-theme-pf-default-accent, var(--ab-base-pf-default-accent));│
│                              │ SEAM 2 hook ↑ theme (L5)      │ fallback ↓ default (L4)│
├─────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 4   BASE PROFILE             tokens: --ab-base-pf-<base-profile-name>-*          │
│   The default VALUES for everything in ab-base — the fallback FLOOR (renders when   │
│   no theme is active). The token embeds the PROFILE NAME, so it is self-labelling;  │
│   the shipped default profile is "default" → --ab-base-pf-default-*.                   │
│     --ab-base-pf-default-accent: hsl(…);   --ab-base-pf-default-space-3: clamp(…);        │
│   Holds HSL seeds + ramps, fluid clamp ladders, ratios, radius, shadows, motion,    │
│   default icon sets. SWAPPABLE: a second profile is --ab-base-pf-<name>-* (e.g.        │
│   --ab-base-pf-compact-*) — a new name, nothing above moves.                           │
├─────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 5   THEME PROFILE  (seam 2)      tokens: --ab-theme-pf-<theme-profile-name>-*     │
│   The theme-side CONTRACT: the complete, named set of themeable tokens, each bound   │
│   1:1 to a layer-3 hook. PURE INTERFACE — holds no values of its own; stays unset    │
│   (→ layer-4 defaults render) until a layer-6 profile populates it. When populated,  │
│   layer 3 resolves to it = overrides layer 4, only for what the theme sets. Token    │
│   embeds the THEME-PROFILE NAME; the default theme profile is "default":             │
│     --ab-theme-pf-default-accent  -neutral-1..6  -surface  -font-heading                │
│     --ab-theme-pf-default-iconset-<group>                                               │
│   METADATA — it DECLARES the layer-4 base profile it overrides, so the override is   │
│   traceable:   --ab-theme-pf-default-overrides: ab-base-pf-default;                        │
│   A second theme profile is --ab-theme-pf-<name>-* and can sit beside it.               │
│                              ▲ populated by the active layer-6 profile               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 6   USER PROFILE             tokens: --<xx>-<stub>-*                     │
│   The customer-facing layer, filled from an L5-sublayer TEMPLATE                     │
│   (--ab-theme-pf-<name>-tmp-<template-name>-*, e.g. -tmp-basic/-standard/-full), a    │
│   pick-n-mix of section schemas (colour/typo/spacing/icons/motion — see              │
│   ab-system-architecture.md). The customer fills values → becomes their profile       │
│   --<xx>-<stub>-* (xx = 2-letter customer slug, e.g. cardiffmet → cm;           │
│   stub = their theme-profile name, e.g. corporate → --cm-corporate-*).           │
│     --cm-corporate-accent: #0a2a3d;                        (the customer's value)│
│     --ab-theme-pf-default-accent: var(--cm-corporate-accent);          (bind → L5) │
│   METADATA — it REFERENCES the layer-5 template it was cut from, so the lineage is   │
│   traceable:   --cm-corporate-reflects: ab-theme-pf-default;   (value = ab-theme-pf-<L5 name>)│
│   One profile active per build (via _htmlClasses / file inclusion).                  │
└─────────────────────────────────────────────────────────────────────────────────┘

  AB COMPONENT SYSTEMS (ab-base-component-*, ab.<obj>.* class space) read LAYER 3
  only — the same portable pivot the adapter reads — so one agnostic structure
  re-skins per user theme through seam 2. cm.btn → ab.btn is the exemplar.
```

## A2. The naming scheme (one segment per layer)

| Layer | Role | Token form | Example |
|---|---|---|---|
| 1 | renderer | the renderer's own vars | `@item-color` |
| 2 | adapter (seam 1) | `--ab-base-if-<renderer>-*` | `--ab-base-if-adapt-item-color` |
| 3 | portable API (pivot) | `--ab-base-*` | `--ab-base-accent` |
| 4 | base profile | `--ab-base-pf-<base-profile-name>-*` | `--ab-base-pf-default-accent` |
| 5 | theme profile (seam 2) | `--ab-theme-pf-<theme-profile-name>-*` | `--ab-theme-pf-default-accent` |
| 6 | user profile | `--<xx>-<stub>-*` | `--cm-corporate-accent` |

**Disambiguating infixes (why `-if-` and `-pf-`).** The two interface/profile
roles under the `--ab-base-` / `--ab-theme-` roots are told apart by a one-word
infix, not by convention:
- **`-if-`** = *interface* (the renderer adapter), layer 2: `--ab-base-if-<renderer>-*`.
- **`-pf-`** = *profile* (a base or theme profile), layers 4 and 5:
  `--ab-base-pf-<base-profile-name>-*`, `--ab-theme-pf-<theme-profile-name>-*`.

So the adapter (`--ab-base-if-adapt-*`) and a base profile (`--ab-base-pf-default-*`)
never share a shape — the `-if-` marks interface function, the `-pf-` marks a
profile. The bare `--ab-base-*` (no infix) is the layer-3 pivot. (Abbott,
11 Oct 2026.)

**Traceability (the metadata chain).** Each profile stamps its lineage, so any
user build is traceable up to its base:
```
--cm-corporate-reflects: ab-theme-pf-default;    (L6 → names its L5 template)
--ab-theme-pf-default-overrides:  ab-base-pf-default;      (L5 → names the L4 base profile it overrides)
```
Read them together: user profile `cm-corporate` → reflects theme profile
`ab-theme-pf-default` → overrides base profile `ab-base-pf-default`. You always know
what a user's theme definitions are reflecting, and the base they sit on.

## A3. The two seams + the override, worked end-to-end (the accent)

```
L1  .mcq-item__label                                   renderer's own selector (literal was #117F93)
L2  html .mcq-item__label {                            the ADAPTER's rule…
      background-color: var(--ab-base-if-adapt-item-color) !important; }
    --ab-base-if-adapt-item-color: var(--ab-base-accent); ◄ SEAM 1 (renderer name → pivot)
── portability line ────────────────────────────────────────────────────────────────────────
L3  --ab-base-accent:                                  the PIVOT — a hook, not a value
      var(--ab-theme-pf-default-accent,                   ◄ SEAM 2: theme if present…
          var(--ab-base-pf-default-accent));              …else the base default
L4  --ab-base-pf-default-accent: hsl(…);                  BASE PROFILE "default" (renders with no theme)
L5  --ab-theme-pf-default-accent: var(--cm-corporate-accent);   THEME PROFILE "default" (fed by L6)
    --ab-theme-pf-default-overrides: ab-base-pf-default;     ◄ metadata: names the L4 profile it overrides
L6  --cm-corporate-accent: #0a2a3d;              USER value
    --cm-corporate-reflects: ab-theme-pf-default;   ◄ metadata: names the L5 template it reflects
```

Read the override bottom-up: L6 sets its own value → binds it into L5's contract →
L3's hook therefore resolves to it instead of L4 → the adapter paints L1 with it.
No theme present → L5 is unset → L3 falls through to L4 → unthemed render.

## A4. What each layer lets you change independently (the point of the seams)

| Change this… | …and ONLY this moves | because |
|---|---|---|
| the renderer (Adapt → JSX) | layer 2 (a new adapter) | seam 1 confines renderer vocabulary + specificity to the adapter |
| the base defaults (e.g. tighter spacing) | layer 4 (a new `--ab-base-pf-<name>-*` profile) | layer 3 names are stable; the profile is swappable |
| the theme system (new themeable aspect) | layer 5 (+ its layer-3 hook) | seam 2 is a distinct namespace from base |
| the user theme (new customer) | layer 6 (a new profile from a template) | the profile only feeds layer 5; nothing above knows its name; its `-reflects` stamp keeps it traceable |

**Partial themes fall out for free:** a layer-6 profile sets only the tokens it
cares about (accent, neutrals, fonts); every token it leaves unset has an unset
layer-5 hook, so layer 3 falls through to the layer-4 default. A user theme never has
to specify the whole system.

## A5. Why the hook (option a), not overwriting the base (option b)

The theme is a **separate namespace** (`--ab-theme-pf-<name>-*`) composed with the
base at layer 3's hook — it never writes into the base namespace
(`--ab-base-pf-<name>-*`). That is what keeps base and theme two systems with a real
interface between them: the theme can grow, reorganise or add a second theme
profile and the base defaults, the pivot, the adapter and the renderer are all
untouched. The visible *outcome* ("a theme overrides the base default") is
identical to overwriting the base token — but composing at the hook keeps
specificity out of the token layer (it stays sealed in the adapter) and lets the
two systems version independently. (Decision with Abbott, 11 Oct 2026: option a.)

## A6. File → AB layer index (post-rename targets, from `ab-cm-rename-spec.md`)

| TARGET file (`ab-*`)                | AB layer (Part A)                               |
|-------------------------------------|-------------------------------------------------|
| `ab-vanilla-overrides.less`         | L2 adapter — the seam rules + `--ab-base-if-adapt-*` |
| `ab-core.less`                      | L2 adapter app-rules **+** some L3 pivot tokens  |
| `ab-schemes.less`                   | L3 pivot role spine **+** L4 default values + light/dark |
| `ab-base.less`                      | L4 base-profile dials (+ user-theme VALUES → `cm-user.less`) |
| `ab-breakpoints.less`               | L3 band tokens **+** L4 bands                    |
| `ab-type.less`                      | L3 `--ab-base-step-*` **+** L4 fluid clamp ladder |
| `ab-colour-profiles.less`           | L4 colour-theory profiles (feed the values)      |
| `ab-palette.less`                   | L4 raw values feeding the profiles               |
| `ab-font-themes.less`               | L3 heading-colour tokens **+** L4 values         |
| `ab-notify/-buttons/-cards/-callouts/-icons/-links/-dropdown` | AB component systems (`ab.<obj>.*`, read L3) |
| `ab-content.less / ab-icons-ext.less` | AB component systems (our own objects)         |
| **NEW** `cm-user.less`             | L6 user profile → fills the L5 contract          |
| **NEW** `sa-user.less`             | L6 user profile → fills the L5 contract          |
| *stays* `cm-themes.less`            | CM presentational brand look (menu/tile)         |
| *stays* `cm-theme-packs.less`       | CM dark-blue/grey packs (L6-style overrides)     |

(The rename is whole-token / longest-first — `cm-theme` → `ab-theme` must not
corrupt `cm-theme-dark-blue-grey`, which stays CM. See `ab-cm-rename-spec.md`
"Collision".)

---

# PART B — CURRENT: the `--cm-` / `html.cm-theme` gate (live in code today)

What the LESS actually compiles right now, after the `html.cm-theme` gate landed
(11 Oct 2026). The build-test validates THIS before the rename to Part A runs.

## B1. The layer stack (bottom = Adapt, top = ours)

Read bottom-up. Each layer above only *overrides* what it needs from the layer
below; everything it doesn't touch falls through to vanilla.

```
┌───────────────────────────────────────────────────────────────────────────┐
│  (5) THE GATE  —  html.cm-theme                                             │
│      One class on <html> (config.json _htmlClasses). Wraps layers 3–4 so    │
│      the whole user-theme skin is OPTIONAL. Remove it → layers 3–4 stop matching │
│      → you fall straight back to layer 1 (pure vanilla).                    │
│      (TARGET: this gate class becomes ab-theme; the skin stops being        │
│       "optional-via-gate" and becomes "user-theme-selected" — see Part A.)       │
│                                                                             │
│  (4) APPLICATION  —  rules that paint vanilla's components with our tokens  │
│        • vanilla-overrides.less  (the sweep: vanilla's teal/grey → --cm-*)  │
│        • theme.less app-rules    (headings, links, nav, gutters, spacing)   │
│        • cm-links / cm-notify / cm-themes / cm-dropdown / cm-breakpoints    │
│      ALL of this is gated under (5).   (TARGET: this IS the L2 adapter.)    │
│                                                                             │
│  (3) SEMANTIC / ROLE TOKENS  —  what the user theme "means"  (defined on :root)  │
│        • role spine   --cm-surface/-ink/-hairline/-on-accent  (cm-schemes)  │
│        • accent chain --cm-accent /-hover/-active/-deep/-ring (cm-schemes)  │
│        • semantic     --cm-primary --cm-info --cm-success --cm-danger (theme)│
│        • headings     --cm-h1-color … --cm-h6-color           (cm-font-…)   │
│        • type scale   --cm-h1-font-size … --cm-body-font-size  (cm-type)    │
│        • layout       --cm-page-max --cm-gutter --cm-pad-y     (theme/bp)   │
│        • fluid dials  --cm-brand-h/-s/-l, --cm-l-* stops, ratios (cm-base)  │
│        • packs/profiles re-point these per series (cm-theme-packs,          │
│          cm-colour-profiles)                                                │
│      Tokens are DEFINITIONS — they sit on :root, NOT under the gate, and    │
│      are harmless when the skin is off (nothing consumes them then).        │
│      (TARGET: the L3 pivot + L4/L5/L6 profile stack, see Part A.)           │
│                                                                             │
│  (2) SEEDS / DERIVATION  —  HSL dials + derived ramps  (cm-base/cm-schemes) │
│        A single user-theme hue + neutral tint + lightness stops; roles derive    │
│        via ~"hsl(var(--cm-*) …)" and color-mix(). Dark = L-stop flip.       │
│        (TARGET: these become the L4 base-profile + L6 user-theme seeds.)         │
│                                                                             │
│  (1) ADAPT — adapt-contrib-vanilla + core + each contrib component          │
│        Vanilla bakes LITERALS into compiled CSS: @item-color #117F93 (teal),│
│        @greyDark #4D4D4D, @validation-* , fixed radius/spacing. This is     │
│        "stock Adapt" — what you see with the gate OFF.                      │
└───────────────────────────────────────────────────────────────────────────┘
```

Our own components (`adapt-abbott-confidence`, `-flipcard`, `-sortable`, …) are a
separate story: they live in layer (1)'s *source* slot (components/) but have no
vanilla equivalent, so they are **not** gated — they style their own BEM markup
and simply read the layer-3 tokens. (TARGET: these keep their own files; their
`--cm-*` reads become `--ab-base-*`.)

## B2. How our tokens map onto Adapt's literals

Vanilla hard-codes colours per component. The **sweep** (`vanilla-overrides.less`)
re-points vanilla's selectors at our tokens; the token then resolves through
layers 3 → 2. So the flow for any one colour is:

```
vanilla selector  ──(sweep, gated)──►  --cm-* semantic token  ──►  HSL-derived value
.mcq-item__label                       --cm-accent                 hsl(brand-h brand-s accent-l)
```

| Vanilla literal (layer 1)                     | Our token (layer 3)        | Resolves to (layer 2)                    | Applied by |
|-----------------------------------------------|----------------------------|------------------------------------------|------------|
| `@item-color` / `@heading-color` `#117F93` teal | `--cm-accent`, `--cm-primary` | `hsl(brand-h brand-s accent-l)`        | sweep §1, theme.less |
| `darken(@item-color,10%)` `#0c5865` (hover)   | `--cm-accent-hover`        | `calc(accent-l - N%)`                    | sweep §2 |
| `darken(@item-color,15%)` `#09444e` (visited) | `--cm-accent-active`       | `calc(accent-l - N%)`                    | sweep §3 |
| `darken(@item-color,20%)` `#063038` (selected)| `--cm-accent-deep`         | `calc(accent-l - N%)`                    | sweep §4 |
| `@greyDark` `#4D4D4D` (buttons, chrome)       | `--cm-primary` (recoloured) | user-theme spine                             | sweep §5 |
| `@font-color` / `@greyDark` (running text)    | `--cm-ink` / `-ink-muted`  | neutral spine                            | sweep §6 |
| `@greyLight` `#f9f9f9` / `#e6e6e6` (surfaces) | `--cm-surface-sunken`, `--cm-hairline` | neutral spine               | sweep §7 |
| `@disabled` `#DDDDDD`                          | `--cm-hairline`            | neutral spine                            | sweep §5/§7 |
| `@validation-success` `#065f28`               | `--cm-success`             | semantic token                           | sweep §8 |
| `@validation-error` `#dd0000`                 | `--cm-danger`              | semantic token                           | sweep §8 |
| fixed heading sizes (per breakpoint)          | `--cm-h1-font-size` …      | fluid `clamp()` in cm-type               | theme.less headings |
| fixed content width / gutters                 | `--cm-page-max`, `--cm-gutter`, `--cm-pad-y` | layout tokens              | theme.less, cm-breakpoints |

**Why a token and not the hex directly:** change `--cm-accent` (or the user-theme hue
it derives from) in ONE place — a pack, a profile, a `.cm-scheme-<colour>`
wrapper, or dark mode — and every vanilla surface the sweep re-pointed follows.
One variable re-themes a whole series, while the neutral spine stays constant.

## B3. The optional switch (layer 5) in one line

```less
html.cm-theme .mcq-item__label { background-color: var(--cm-accent) !important; }
│    │          │                                  │
│    │          │                                  └ layer 3 token → layer 2 HSL value
│    │          └ vanilla's own selector (layer 1)
│    └ THE GATE: present only when _htmlClasses has "cm-theme"
└ wins the cascade over vanilla (compiled-last) via specificity + !important
```

- **Gate on**  → the rule matches → user theme.
- **Gate off** → the rule does not match → vanilla's own `#117F93` shows → pure vanilla.

The one special case: a selector that targets `<html>` itself (the pack class
`cm-theme-dark-blue-grey`) concatenates — `html.cm-theme.cm-theme-dark-blue-grey`
— rather than becoming a descendant.

## B4. File → layer index (current)

| File (`src/extensions/adapt-ab-theme/less/`) | Layer | Gated? |
|--------------------------------------------------|-------|--------|
| `cm-base.less`               | 2 seeds/dials + 3 emitted tokens           | no (definitions) |
| `cm-schemes.less`            | 2 derivation + 3 role spine/accent chain   | no (defs); its one `body` rule is gated |
| `cm-type.less`               | 3 fluid type ladder (clamp)                | no (definitions) |
| `cm-font-themes.less`        | 3 heading-colour tiers                     | no (definitions) |
| `theme.less`                 | 3 semantic/layout tokens **+** 4 app-rules | `:root` no; app-rules **yes** |
| `cm-breakpoints.less`        | 3 layout-band tokens **+** 4               | tokens no; `.page__inner`/hotgraphic **yes** |
| `cm-theme-packs.less`        | 3 per-pack token values                    | no (values keyed by pack class) |
| `cm-colour-profiles.less`    | 3 per-profile accent values                | no (definitions) |
| `vanilla-overrides.less`     | 4 the vendor sweep (teal/grey → tokens)    | **yes** (every selector) |
| `cm-links.less`              | 4 prose links (`:root` tokens + app)       | tokens no; links **yes** |
| `cm-notify.less`             | 4 notify/hotgraphic popups                 | tokens no; popup rules **yes** |
| `cm-themes.less`             | 4 menu/tile presentational theme           | **yes** |
| `cm-dropdown.less`           | 4 matching dropdown                        | **yes** (kept as its own file) |
| `cm-buttons.less` `cm-cards.less` `cm-callouts.less` `cm-icons.less` `cmet-*` | our own `.cm.*`/`.cmet-*` objects | no (no vanilla equivalent) |

**Rule of thumb for adding new styling (current):**
- A new **colour** → add/point a `--cm-*` token (layers 2–3); don't hard-code a hex.
- Overriding a **vanilla** surface → put the rule under `html.cm-theme` (layer 4/5).
- Styling **our own** component/object → no gate needed; read the tokens.

---

## The bridge: how B becomes A

`ab-cm-rename-spec.md` is the scripted, atomic pass that turns Part B into Part A:
every `--cm-*` custom property → `--ab-*`, the AB class list renamed
(`cm-theme` → `ab-theme`, `cm-profile-*` → `ab-profile-*`, …) while the CM-brand
classes (`cm-theme-dark-blue-grey`, `cm-pack-*`, `cm-tile-*`) stay, the AB files
`git mv`-d to `ab-*`, and CM's dial VALUES extracted into a new `cm-user.less`.
**It is gated on the build-test** (`ab-system-architecture.md` sequencing step a):
Part B must be confirmed to render — colour, fluid type, light/dark, profiles —
before the rename runs, or the port lands in the wrong namespace.

The rename also draws the layers Part A names but Part B has not yet separated:
the gated sweep splits into the **adapter** (L2, seam 1) and the portable
**`--ab-base-*`** pivot (L3); the seeds/derivation (B's layer 2) and the
pack/profile values become the **base-profile defaults** (L4) and the **theme
interface + user profiles** (L5/L6, seam 2). Only after that split does a second
adapter (a JSX build) become possible without touching the user-theme layer.
