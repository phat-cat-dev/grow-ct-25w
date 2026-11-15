# AB system architecture (master blueprint)

The complete picture (Abbott, 11 Oct 2026). **AB** is the reusable system; a
**user theme** (CM, SA) is an instance. Ties together the sub-docs:
`ab-cm-rename-spec.md` (the `--cm-*`→`--ab-*` rename), `user-theme-template.md`
(the colour/seed model), `theming-layers-map.md`, `cm-theme-architecture.md`.
Source for everything below is `cm-global.css` (the concatenation of the
`/public/css/cm-utility-*`, `cm-object-*`, `cm-content-*`, `cm-layout` files —
each marked `/* ===== …css ===== */` inside it).

**The canonical six-layer cascade — names, seams and worked examples — lives in
`theming-layers-map.md` Part A.** This doc states it in brief and then covers
what that map does not: the cm-global intake tables and the component systems.

## The layer stack (six layers, two seams, one pivot)

Top (renderer) → bottom (the user's own values). The spine is two seams meeting
at the layer-3 pivot (full detail: `theming-layers-map.md` Part A).

```
LAYER 1  RENDERER                    instance: adapt-vanilla (a JSX lib later)
                                     bakes its own literals in its own vocabulary
   ⇅ SEAM 1 — the ADAPTER (renderer-specific; one active per build)
LAYER 2  --ab-base-if-<renderer>-*      renderer-named tokens + the seam rules, mirroring
                                     the renderer's NAMED vars 1:1 (--ab-base-if-adapt-item-color
                                     ← @item-color). Alias → L3.
══ portability line — everything below is framework-agnostic ══
LAYER 3  --ab-base-*                 THE PIVOT: the portable token API, by role. Holds no
                                     literal — each is a hook composing L5-over-L4:
                                       --ab-base-accent:
                                         var(--ab-theme-pf-default-accent,
                                             var(--ab-base-pf-default-accent));
LAYER 4  --ab-base-pf-<base-profile-name>-*   BASE PROFILE — the fallback floor (renders with no
                                     theme). The token embeds the PROFILE NAME (self-labelling);
                                     the shipped default is "default" → --ab-base-pf-default-*.
                                     Two-tier with L3: the active profile fills these names (a
                                     second profile is --ab-base-pf-<name>-*, e.g. --ab-base-pf-compact-*,
                                     and L3's names don't move). Fluid clamp scales (space/type),
                                     ratios, radius, shadows, motion, default icon sets.
   ⇅ SEAM 2 — the THEME INTERFACE
LAYER 5  --ab-theme-pf-<theme-profile-name>-*   the theme CONTRACT: the complete themeable
                                     vocabulary, each token bound 1:1 to an L3 hook. PURE
                                     INTERFACE — no values of its own; unset → L4 defaults
                                     render; when a user theme populates it, L3 resolves to it =
                                     overrides L4 for only what is set. Token embeds the theme-
                                     profile name; default is "default" → --ab-theme-pf-default-*.
                                     METADATA: declares the L4 profile it overrides, so the
                                     override is traceable — --ab-theme-pf-default-overrides: ab-base-pf-default;
LAYER 6  --<xx>-<stub>-*             the USER profile: filled from an L5-sublayer
                                     TEMPLATE (--ab-theme-pf-<name>-tmp-<template-name>-*,
                                     a pick-n-mix of section schemas) — the customer fills —
                                     neutral seeds + accent-set bases + FONTS (heading/body,
                                     serif/sans/mono, may be Google Fonts) + ICON SET packs
                                     (named Google Material Symbol groups: academic-practice-
                                     type, cite-source-type…) [user-theme-template.md §1,3,4,5].
                                     ALWAYS an instance of a specific L5 template and reflects
                                     it; METADATA stamps the lineage —
                                     --cm-corporate-reflects: ab-theme-pf-default; — so a
                                     user build traces up to its base. Feeds L5; nothing above
                                     knows its name. cm-user / sa-user are instances. A BUILD
                                     step self-hosts fonts + icon assets (SCORM ships offline;
                                     never runtime-linked to Google). Base owns only the fluid
                                     type SCALE; faces + icon packs are user theme concerns.

AB COMPONENT SYSTEMS (ab-base-component-*, in an ab.<obj>.* class space) read the
L3 pivot ONLY — the same portable tokens the adapter reads — so one theme-agnostic
structure re-skins per user theme through seam 2. cm.btn → ab.btn is the exemplar.
element _classes are declared at the template layer and point down the same
cascade.
```
Key: **seam 1 lets the renderer change (Adapt → JSX) with only the adapter
moving; seam 2 lets the theme system evolve with only L5 + its L3 hooks moving.
The AB component systems are `--ab-base-*`-level systems for components** —
generic, consuming the L3 pivot, re-skinned only through seam 2.

## Section schemas + theme-profile templates (the pick-n-mix authoring surface)
(Abbott, 11 Oct 2026.) How the user-facing templates are built, and where they sit.

**SECTION SCHEMAS** — one per themeable section (`colour`, `typography`,
`spacing`, `icons`, `motion`, …). A section schema is the **single authoritative
definition** of that section's token set and shape. Each schema **projects into
three places**, so a section is defined once and stays consistent everywhere:
1. **L4 `--ab-base-pf-*`** — the section's DEFAULT values.
2. **L5 `--ab-theme-pf-*`** — the section's CONTRACT (the themeable tokens + their
   L3 hooks).
3. **the templates below** — the section's user-authorable FIELDS.

Build order: a schema **folds first into L4** (defaults), **then L5** (contract),
**then the templates** (authoring fields).

**THEME-PROFILE TEMPLATES** — the user-facing authoring surface, an **L5 sublayer**,
**named not numbered** (the old `-nnnn` is dropped):
```
--ab-theme-pf-<theme-profile-name>-tmp-<template-name>-*
   e.g.  --ab-theme-pf-default-tmp-basic-*   -tmp-standard-*   -tmp-full-*
```
A template is a **pick-n-mix of section schemas** — it exposes exactly the sections
a user wants to author, at the extent they want:
- **basic / standard / full** = extent presets (fewer → more sections/fields).
- **bespoke** = any chosen combination (e.g. `colour` + `icons`, but not
  `typography`) — because schemas are per-section, a template is just the union of
  the sections it includes.

A user **completes a template** → their choices become the **L6 user profile**
`--<xx>-<stub>-*` (which binds into the L5 contract, per the cascade). Sections a
template does not expose are simply not authored — they **fall through to the L4
defaults**, exactly as any unset theme token does.

**Placement note (resolving "layer 4 or 5?"):** the template lives in the **L5
namespace** (`--ab-theme-pf-…-tmp-…`) — it is the user-facing FACE of the L5 theme
contract, scoped to a named subset. It DERIVES its field structure from the section
schemas (which also define L4), so it "touches" L4, but it is an **L5 sublayer**,
not L4. *(Judgement call on Abbott's "not sure" — confirm.)*

**The section-schema format** (what a `colour`/`typography`/… schema file looks
like, and the `ab-fold-section-schemas` tool that projects it into L4/L5/templates)
is drafted in **`section-schemas.md`** (DRAFT, not yet built). `user-theme-
template.md` is in effect the worked **colour** section (seeds + neutral ladder +
accents) and the template's colour face.

## AB base (system) — the utility intake from cm-global

> Token-name note: the `--ab-space-*`, `--ab-shadow-*`, `--ab-*` names in the
> table below are shorthand for the **L3 pivot** tokens — i.e. `--ab-base-space-*`,
> `--ab-base-shadow-*`, … (`theming-layers-map.md` A2). Their default VALUES live
> in the L4 base profile (`--ab-base-pf-<base-profile-name>-*`, e.g. `--ab-base-pf-default-*`); a user theme overrides via the L5
> contract. The intake mapping itself is unchanged.

| cm-global section (source) | → AB base | Make it… |
|---|---|---|
| SPACING root vars (modular scale `--cmet-spacing-*` from `--cmet-scale-*` ratios) | `ab-space` (`--ab-space-*`) | **fluid** clamp scale from base unit + ratio + fluid range (like the type ladder) |
| UTILITY + COLOUR root vars | `ab-palette` / `ab-tokens` | `--cmet-*` → `--ab-*` |
| cm-utility-typography | `ab-type` | already a fluid ladder; fold in heading weight/line-height/letter-spacing |
| cm-utility-spacing (margin/padding utils) | `ab-space` utilities | see BS5 caution below |
| cm-utility-positioning / -display | `ab-position` / `ab-display` | keep only what Adapt lacks |
| cm-utility-shadows | `ab-shadows` (`--ab-shadow-*`) | tokenised elevation scale |
| cm-utility-animations | `ab-motion` | guard with `prefers-reduced-motion` |
| cm-utility-icons / navicons | `ab-icons` | reconcile with our existing `cm-icons` |
| box model (`--cmet-border-radius/-width/-style/-outline`) | L4 `--ab-base-pf-default-border-*` | ✅ RESOLVED (Abbott, 11 Oct 2026): border-width **0.2rem** (cm-global wins over the current 0.1rem). A token in the L4 base profile; see the fluid-engine note on whether borders are fluid or fixed. |

## AB base — the fluid engine (the L4 default profile's own model)
The L4 base profile (`--ab-base-pf-default-*`) is built as a **fluid engine**, not
a table of fixed numbers (Abbott, 11 Oct 2026):

- **Base-rem anchor.** `1rem = 16px` (the browser root default) is the unit
  everything is expressed in. Change the anchor and the whole system scales.
- **Fluid default (vw-based).** Every size/space token is `clamp(min, <Nrem + Mvw>,
  max)` — continuous scaling with the viewport (the Utopia-style interpolation
  already used for the type ladder), proliferating from the base rem + a ratio + a
  min/max viewport range. This is the default.
- **Breakpoint FALLBACK (stepped, "in case").** A parallel set where media-query
  breakpoints step the same values per band — the **media query acts as the clamp**
  (its boundaries stand in for the clamp's min/max anchors), so the stepped values
  roughly track the fluid curve but degrade gracefully where the continuous
  vw-clamp is unwanted or unavailable. Kept aligned to the fluid curve by
  construction, not maintained as independent numbers.

**One sub-question flagged (Abbott leaning fluid):** **border-width** is the one
box-model dial usually best kept **fixed** (or on a very tight clamp) — a hairline
that grows with the viewport reads heavy on large screens. Recommendation: type
and space are fluid; `--ab-base-pf-default-border-width` is fixed at 0.2rem (or a
tight clamp). Confirm fixed vs fully-fluid for borders. (The default VALUE, 0.2rem,
is settled either way.)

Also still open: whether the breakpoint fallback is a **separate base profile**
(`--ab-base-pf-breakpoint-*`) or baked into `-default` via `@supports`/media
queries. Flagged, not chosen.

## AB component systems — the object intake from cm-global
`cm-object-tooltips / -callouts / -accordions / -buttons / -card / -hero /
-navtiles / -navlists / -navicons / -sitewidenav / -index`, `cm-content-summary /
-practicalsteps`, `cm-layout` → **`ab-base-component-<name>`** each, in an
**`ab.<obj>.*` class space** (`ab.btn.*`, `ab.card.*`, `ab.callout.*`, …).

**The pattern (cm.btn → ab.btn is the exemplar):** a component file sets up the
THEME-AGNOSTIC structure — layout, sizes, states (hover/active/disabled),
variants — reading the **L3 pivot tokens only** (`--ab-base-accent`,
`--ab-base-surface`, `--ab-base-space-*`, `--ab-base-radius`…), with **no user theme
colour baked in**. At build time the active **user theme profile's colour themes
proliferate** it (through seam 2), so the one structure re-skins per user theme (CM vs
SA) through the cascade. This is how *most* AB components are built: base
structure (agnostic) + user theme-driven colour.

**Reconcile with what already exists** — we already have `cm-buttons`,
`cm-cards`, `cm-callouts`, `cm-dropdown`, `cm-icons` in the theme (which become
`ab.btn`/`ab.card`/… under `ab-base-component-*`), plus the `adapt-abbott-*`
components; the port must MERGE into one home per object, never create a second.

## Value resolution (the override order — applies to every component + token)
A component's **actual produced output** resolves through the L3 pivot, which
composes seam 2 over the base default:
```
ab-base-component-*        structure + state + token REFERENCES (reads --ab-base-*)
   the referenced L3 token is a hook:
     --ab-base-X: var(--ab-theme-pf-default-X, var(--ab-base-pf-default-X));
                      │ L5 theme profile (set by the      │ L4 base profile "default"
                      │ active L6 user theme profile) — wins    │ — else this
```
So **by default a component renders from the L4 base-profile defaults; the L5
theme contract (fed by the L6 user theme profile) overwrites only what it sets, and
anything it leaves unset falls through to the base default.** Same precedence for
spacing / type / icons as for colour — one override chain, composed **at the
pivot** (never by writing into the base namespace: option (a), `theming-layers-
map.md` A5), so base and theme stay two systems that version independently.

## Not bringing in yet
BS5-based objects / the Bootstrap utility OVERRIDES (margin/padding/display
grids) — we're recreating some of these; they stay out until explicitly pulled.

## Pro-notes raised for Abbott (your "if there's a better way, flag it")
1. **Fluid, not fixed.** cm-global's spacing + type are fixed modular scales;
   AB makes them `clamp()` fluid off the shared range — same structure, modern
   result. (Already the agreed default.) ✅ recommend.
2. **Don't re-implement Bootstrap.** cm-global carries many BS5 utility
   *overrides*. Adapt already ships a grid/util layer; porting all of them
   duplicates it and bloats the build. Recommend: bring in only AB utilities
   Adapt lacks, and only the object systems we actually use.
3. **One home per object.** The `cm-object-*` ports overlap our existing
   `cm-buttons/-cards/-callouts/-dropdown/-icons` and the `adapt-abbott-*`
   components. Recommend each object resolves to ONE `ab-*` file (merge), never
   two sources — otherwise we re-create the very duplication this cleanup fixes.
4. **Base has a default profile, like user themes do.** `ab-base-profile-default` (L4)
   holds the base's default VALUES (fluid range, ratios, spacing base, radius) so
   a build can swap the base profile (`-defaultversion2`) the same way a user theme
   overrides colour via L5 — one consistent profile mechanism across base and
   user theme. ✅ recommend.
5. **Utilities are opt-in.** Utility classes (`bg-*`, `m-*`, `d-*`) can bloat;
   keep the set lean and AB-namespaced, and prefer tokens over utility classes
   inside components.

## Sequencing
This is a large program. Order: **(a) build-test the current theme stack →
(b) AB/CM rename (establishes the `--ab-base-*` pivot + the seam-1 adapter
namespace everything hangs on) → (c) AB base intake (space/type/box-model/
shadows/motion, fluid) + the L4 `ab-base-profile-default` → (d) the L5 theme
contract + L6 user theme profiles (cm / sa, from a template) → (e) AB component
systems, one object at a time, merging with existing files.** Nothing ports
before the rename, or it ports into the wrong namespace.
