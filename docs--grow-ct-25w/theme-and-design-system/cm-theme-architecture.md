# CM theme architecture — tokenised, fluid, variable-driven

> **SUPERSEDED for naming + layer structure (11 Oct 2026).** The target
> architecture is now the **six-layer model** in `theming-layers-map.md` Part A
> and `ab-system-architecture.md` (renderer → `--ab-base-if-<renderer>-*` adapter
> → `--ab-base-*` pivot → `--ab-base-pf-<name>-*` base profile →
> `--ab-theme-pf-<name>-*` theme profile → `--<xx>-<stub>-*` user profile). This
> doc is retained for its still-valid **principles** — tokenise all the way down,
> stay fluid, HSL-derive colour, vanilla-as-default — not for its layer count or
> its `--cm-*` names (which are the current-code naming, Part B). Its **`brand`**
> terminology (and the `--cm-brand-*` / `brand-h/s/l` seed names below) is also
> superseded: the user-set top layer is now the **user theme**, its seeds
> `--ab-...-user-*` — see the authoritative docs. Read the two docs above for the
> authoritative cascade; read this for the reasoning behind it.

The target architecture (Abbott, 11 Oct 2026). Supersedes the `html.cm-theme`
opt-in gate (which made brand depend on a per-config class that could be lost —
the "vanilla again" failure). Here **vanilla is the DEFAULT, not a switch**: the
interface tokens default to Adapt's own original values, and the CM theme only
*overrides those values*. Lose the top and you degrade to vanilla, never break.

Principle, stated once: **tokenise all the way down, and stay fluid.** Every
colour, size, space and breakpoint is a variable; type and layout scale by
`clamp()`; colour is built in HSL so a whole theme derives from a few base
variables. A new theme = new base variables at the bottom. Nothing hard-codes a
hex or a px up top.

---

## The layers (bottom = Adapt, top = themes)

```
┌─ (4) VARIABLE THEMES ───────────────────────────────────────────────────────┐
│     A theme = a small set of BASE variables, mostly HSL:                     │
│       --cm-brand-h/s/l, --cm-neutral-h/s, --cm-accent-h …                    │
│     Everything below derives from these. Switch theme = swap these few vars  │
│     (a class like .cm-theme-<name> on <html>, or the default set on :root).  │
│     Light/dark = another base-variable set, not a separate stylesheet.       │
├─ (3) CM THEME TOKENS  (the "CM theme business") ─────────────────────────────┤
│     The brand design system, all derived from layer 4's base vars:           │
│       • COLOUR  — hsl(h s l) scales; tints/shades via calc() on L, not new   │
│                   hexes. Role tokens: --cm-surface/-ink/-accent/… in HSL.    │
│       • TYPE    — fluid clamp() scale --cm-step-* (h1…h6, body); one ratio.   │
│       • SPACE   — fluid clamp() scale --cm-space-*.                           │
│       • LAYOUT  — fluid clamp() --cm-measure/-gutter/-pad; breakpoint tokens. │
│     This layer OVERRIDES the interface tokens (layer 2) with CM values, and  │
│     styles our own .cm-* / adapt-abbott-* components.                        │
├─ (2) ADAPT INTERFACE  (the "interface to Adapt" — the seam) ─────────────────┤
│     ONE token per Adapt surface-role, each DEFAULTING to Adapt's original    │
│     literal (the kept copy of vanilla). e.g.                                 │
│       --ai-accent:        #117F93;   /* vanilla @item-color (teal)        */  │
│       --ai-accent-hover:  #0c5865;   /* darken 10%                        */  │
│       --ai-accent-visited:#09444e;   /* darken 15%                        */  │
│       --ai-accent-open:   #063038;   /* darken 20% (selected/open)        */  │
│       --ai-chrome:        #4D4D4D;   /* vanilla @greyDark buttons/drawer  */  │
│       --ai-text:          #4D4D4D;   /* vanilla running text              */  │
│       --ai-surface-sunken:#f9f9f9;   /* vanilla @greyLight                */  │
│       --ai-hairline:      #e6e6e6;   --ai-disabled: #DDDDDD;                  │
│       --ai-success:       #065f28;   --ai-error: #dd0000;                     │
│     PLUS the sweep: point every Adapt compiled selector at its --ai-* token  │
│     (this is today's vanilla-overrides.less, refined to role-separated       │
│     tokens so the defaults reproduce vanilla EXACTLY — teal, grey and text   │
│     each keep their own token, never collapsed onto one).                    │
│     With ONLY layers 0–2 present, the site is pixel-vanilla.                  │
├─ (1) ADAPT COMPONENTS / CORE (adapt-contrib-*) ──────────────────────────────┤
│     Vanilla's compiled CSS with its baked literals. Untouched.               │
├─ (0) ADAPT FRAMEWORK + the kept original ────────────────────────────────────┤
│     adapt-contrib-vanilla as shipped. We keep a reference snapshot of its    │
│     compiled output (exports/adapt-vanilla.reference.css) so "the original"  │
│     is always on hand to diff against.                                       │
└──────────────────────────────────────────────────────────────────────────────┘
```

**How re-skinning works:** layer 3 sets `--ai-accent: hsl(var(--cm-brand-h) …)`.
The sweep already points `.mcq-item__label { background: var(--ai-accent) }`, so
the component follows the brand with no new selector. Change the brand hue at
layer 4 → every `--ai-*` the CM layer re-points follows → the whole UI reskins.

**How vanilla works (optionality, done right):** don't apply layer 3's value
overrides. The `--ai-*` tokens fall back to their layer-2 defaults = Adapt's
originals = pixel-vanilla. Optionality is "are the CM values applied?", and the
failure mode of *not* applying them is clean vanilla, never a broken half-state.
(If we still want an explicit switch, it toggles only layer-3's value block —
a few `--ai-*`/`--cm-*` reassignments — not 350 selectors.)

---

## Colour: HSL base variables → derived scales

```less
:root {
  /* layer 4 — base variables (the only thing a new theme changes) */
  --cm-brand-h: 203; --cm-brand-s: 72%; --cm-brand-l: 22%;   /* dark-blue */
  --cm-neutral-h: 0; --cm-neutral-s: 0%;

  /* layer 3 — derived, no new hexes; shades move L, tints raise L */
  --cm-accent:        hsl(var(--cm-brand-h) var(--cm-brand-s) var(--cm-brand-l));
  --cm-accent-hover:  hsl(var(--cm-brand-h) var(--cm-brand-s) calc(var(--cm-brand-l) - 6%));
  --cm-accent-tint:   hsl(var(--cm-brand-h) var(--cm-brand-s) 94%);
  --cm-ink:           hsl(var(--cm-neutral-h) var(--cm-neutral-s) 10%);
  --cm-surface:       hsl(var(--cm-neutral-h) var(--cm-neutral-s) 100%);
}
```
A second theme is `--cm-brand-h: 150` (green) and nothing else. Dark mode is a
base-variable set that raises the neutral L and lifts the accent L.

## Typography & breakpoints: clamp(), fluid

```less
--cm-step-0: clamp(1rem, calc(0.95rem + 0.25vw), 1.125rem);         /* body  */
--cm-step-1: clamp(1.25rem, calc(1.1rem + 0.6vw), 1.6rem);          /* h-ish */
/* one ratio generates the ladder; each step a clamp, so type is fluid        */
--cm-measure: clamp(17.5rem, 94vw, 98.75rem);  /* content column, fluid       */
--cm-gutter:  clamp(1rem, 4vw, 2rem);
```
Breakpoint *tokens* stay for the few genuine step-changes (nav/grid), but the
default is fluid clamps so most of the UI never needs a media query.

---

## What we keep from the current work
- **Palette hexes** → become the seed for the HSL base variables (convert once).
- **vanilla-overrides.less** → becomes the layer-2 sweep, re-pointed from
  `--cm-*` to role-separated `--ai-*` tokens (its selector coverage is the hard
  part and is already done and verified).
- **The fluid clamps** already in theme.less / cm-breakpoints → fold into the
  layer-3 scales.
- **Our components** (adapt-abbott-*) → unchanged; they read layer-3 tokens.
- **DROP**: the `html.cm-theme` opt-in gate (replaced by default-value model).

## Build order (each step buildable; Abbott grunt-builds to verify)
1. **Capture the original**: snapshot vanilla's compiled CSS to
   `exports/adapt-vanilla.reference.css` (the kept copy).
2. **Layer 2 — Adapt Interface**: define the `--ai-*` tokens defaulting to
   vanilla's literals; re-point the sweep onto them. Build → pixel-vanilla with
   no CM theme. (This is the stable floor; "vanilla" is now correct-by-default.)
3. **Layer 4+3 colour**: HSL base vars + derived role tokens; map CM values onto
   the `--ai-*` tokens. Build → brand returns, now driven by a few base vars.
4. **Type + space + layout** as fluid clamp scales.
5. **Second theme + dark** as proof: a new base-variable set only.
6. Regenerate exports, update the layers-map doc.

---

## Layer model — structure, styling and metadata ride the same build layers

The token cascade above is the STYLING column of a wider model (Abbott, 11 Oct
2026). Three concerns cascade through the same Adapt build layers and meet at one
seam, the **template layer**:

| Build layer | Structure / JSX | Styling / CSS | Metadata |
|---|---|---|---|
| L0 Adapt core + vendor | vendor `adapt-contrib-*` JSX; Adapt render | vanilla CSS + the Adapt-interface tokens (default = vanilla) | — |
| L1 Our components | `adapt-abbott-*` JSX (bespoke markup) | each component's LESS, reading tokens | component spec |
| **L2 Our templates (skeletons)** | slot + archetype structure; the `_classes` it emits | **system tokens + the theme-hook classes the template declares** | **`agentAuthor`** |
| L3 Course instance (JSON) | the real page/block/component tree | instance `_classes` + per-slot coupling markers | course / CXP / qualifier metadata |
| L4 Theme set (`cm-base` dials) | — | the values that COMPLETE the cascade (hues, fonts) | — |

**The seam (L2).** A skeleton slot declares, together: its structure, its styling
hook, and its `agentAuthor`. The styling hook and the metadata are the same kind
of thing — a *contract the template declares that a lower layer fulfils*: the
theme set fulfils the class (via the token cascade), the authoring agent fulfils
the `agentAuthor`.

**How the styling hook attaches (decided 11 Oct 2026): `_classes`, not forked
JSX.** The skeleton declares a theme class per slot/archetype; the generator
(`generate-course-shell.js`) writes it into that element's Adapt-native
`_classes` field (it already does this for `article--lesson-*` and the
`slot__<page>__<slotType>` coupling markers). The CSS theme layer targets those
classes. No second JSX tree is forked over vanilla's; a bespoke `adapt-abbott-*`
component is added only where a slot needs markup vanilla cannot express. So the
"second layer" is a layer of agreed CLASS NAMES (and metadata), not of JSX.

**Consequence for authoring:** extend the skeleton slot shape so a slot can carry
a `themeClasses` (or reuse `classes`) field beside its `agentAuthor` — one place
declares structure + style-hook + authoring contract, and the generator emits the
`_classes` and the metadata together.

---

## Decisions & build status (11 Oct 2026)

**Two profile layers, both off the single `--cm-brand-h`:**
- BASE theme profiles (`cm-colour-profiles`) — one hue → colour-theory palette
  (complementary/analogous/triadic/split); lightweight, standalone-capable.
- CM theme profile (`cm-schemes`) — curated neutrals + accents + light/dark.

**Theme = neutrals + accents; light/dark = a lightness-dial flip.** Role tokens
derive from (neutral hue/sat) + per-role `--cm-l-*` stops; light is the default
L-set, dark (`.cm-dark-tokens`) overrides only the L-stops + `--cm-accent-l`.

**Fluid model (DECIDED): single clamp is the default; breakpoint bands are an
OPTIONAL profile.** Each property is one `clamp()` across `--cm-vw-min→max`
(smooth, no steps). The breakpoint system (sm/md/lg/xl/xxl) stays available as a
switch-on base profile that can override/tune specific bands (e.g. an xl/xxl
boost). This holds for BOTH typography and layout/spacing.

**The 4th base domain — layout/spacing** (to build next): horizontal (gutter +
padding) and vertical (page/container spacing + padding), as single fluid clamps
from `cm-base` dials via the shared `.cm-fluid` mixin, same as the type ladder.

**Status:** ✅ colour (neutrals+accents, HSL) · ✅ typography (fluid ladder) ·
✅ light/dark (L-flip) · ✅ base theme profiles (colour theory) ·
⬜ layout/spacing domain · ⬜ semantic colours → `cm-base` hues ·
⬜ Adapt interface + retire the `html.cm-theme` gate.

**UNVERIFIED-IN-BROWSER:** everything from the HSL/token rebuild onward is
`lessc`-verified only; none has been through a real `grunt` build yet (the
build-test clone wasn't up). A build-test is due before the layout refactor,
which touches deliberate gutter/spacing decisions.
