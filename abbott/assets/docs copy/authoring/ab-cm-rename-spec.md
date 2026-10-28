# AB / CM split — rename & restructure spec (BLUEPRINT, not yet executed)

Abbott, 11 Oct 2026. Separates the generic theming SYSTEM (**AB**) from the
dark-blue user theme built on it (**CM** = a user profile, an instance of an AB theme
profile). Nothing here is applied yet — the blueprint to execute AFTER a
build-test confirms the current colour/type/light-dark/profile stack renders.

> **Reconciled to the six-layer model (11 Oct 2026).** The target is no longer a
> flat `--cm-*` → `--ab-*` swap. It is the six-layer cascade defined in
> `theming-layers-map.md` Part A and `ab-system-architecture.md`:
> `renderer → --ab-base-if-<renderer>-* (adapter) → --ab-base-* (pivot) →
> --ab-base-pf-<name>-* (base profile) → --ab-theme-pf-<name>-* (theme profile)
> → --<xx>-<stub>-* (user profile)`. Reaching it is **more than a rename** — see
> "What the restructure adds" below — so this doc covers both the mechanical
> namespace move and the structural split, landed in **phases** (strategy (ii),
> chosen 11 Oct 2026; see "Migration strategy" and the phased execution plan).

## Principle
- **AB** = the engine: the renderer adapter (seam 1), the portable `--ab-base-*`
  token API (the pivot), the base profile defaults (L4), the fluid type/space
  ladders, breakpoints, colour-theory profiles, the role/scheme + light/dark
  mechanism, and the **theme-profile contract** (seam 2, L5) a user theme fills.
- **CM** = one user profile (`--cm-<stub>-*`, L6) = a thin file that fills the L5
  theme contract with CM's values (dark-blue), plus CM's presentational brand
  bits. "CM is an instance of an AB theme profile."
- **SA** = a SECOND user profile (`--sa-<stub>-*`), another instance of the same
  L5 contract. Proves the architecture: a new user theme is a new L6 dial-set, nothing
  in AB changes. A user theme is selected per build (its class/values in the course
  `_htmlClasses`), so CM and SA coexist in AB and a package picks one.

## Token mapping (by family → six-layer home) — SUPERSEDES the old blanket rule
The old rule ("every `--cm-*` → `--ab-*`") is retired: the six layers give each
`--cm-*` family a different home and infix. Map by what the token *is*:

| Current `--cm-*` family (Part B) | → six-layer home | New form |
|---|---|---|
| role spine + accent chain (`--cm-accent`/-hover/-active/-deep, `--cm-surface`/-subtle/-sunken, `--cm-ink`/-muted, `--cm-hairline`, `--cm-on-accent`) | **L3 pivot** | `--ab-base-<role>` (e.g. `--ab-base-accent`) |
| semantic (`--cm-primary/-info/-success/-danger`), headings (`--cm-h1..h6-color`), type scale (`--cm-*-font-size`, steps), layout (`--cm-page-max/-gutter/-pad-y`) | **L3 pivot** | `--ab-base-<role>` |
| HSL seeds + dials in cm-base (`--cm-brand-h/-s/-l`, `--cm-neutral-h/-s`, the `--cm-l-*` lightness stops, `--cm-accent-l`, ratios, `--cm-radius`, `--cm-border-width`, `--cm-measure-max`) | **L4 base profile** (the default VALUES the pivot resolves to) | `--ab-base-pf-default-*` |
| raw palette hex (cm-palette: `--cm-white`, `--cm-dark-blue`, …) | L4 default seeds **and** L6 user-theme values | `--ab-base-pf-default-*` / `--cm-<stub>-*` |
| per-pack values (cm-theme-packs) + per-profile accents (cm-colour-profiles) | **L5 theme profile** / colour-theory | `--ab-theme-pf-<name>-*` |
| the CM dark-blue user-theme values themselves (hue 202, tint, L-stops, font) | **L6 user profile** | `--cm-<stub>-*` (e.g. `--cm-corporate-*`) |

Applies in the theme LESS, the `adapt-abbott-*` component LESS (their `--cm-*`
reads become the L3 pivot `--ab-base-*`), and the extension JS.

## What the restructure ADDS beyond renaming (new structure, no `--cm-*` source)
These do not exist in Part B and are *built*, not renamed:
1. **The L2 adapter** (`--ab-base-if-adapt-*`): tokens mirroring vanilla's named
   vars 1:1, plus the seam rules. Today the sweep points vanilla selectors
   straight at `--cm-accent`; the restructure inserts the adapter indirection
   (`--ab-base-if-adapt-item-color: var(--ab-base-accent)`).
2. **The L3 hook**: each pivot token becomes
   `--ab-base-accent: var(--ab-theme-pf-default-accent, var(--ab-base-pf-default-accent))`
   — composing L5-over-L4. Today `--cm-accent` holds a value directly.
3. **The L4/L5 split**: today seeds and role tokens live together in
   cm-base/cm-schemes; the restructure separates the base-profile VALUES (L4)
   from the theme CONTRACT (L5, pure interface).
4. **L6 user profiles** with lineage metadata (`--cm-<stub>-reflects:`,
   `--ab-theme-pf-default-overrides:`).

## File mapping
| Current | → New | Six-layer role |
|---|---|---|
| cm-base.less | **ab-base.less** (+ extract CM VALUES to **the L6 cm profile**) | L4 base-profile defaults |
| cm-schemes.less | **ab-schemes.less** | L3 pivot + its hooks + light/dark |
| cm-type.less | **ab-type.less** | L3 type steps + L4 clamp ladder |
| cm-breakpoints.less | **ab-breakpoints.less** | L3 band tokens + L4 bands |
| cm-colour-profiles.less | **ab-colour-profiles.less** | colour-theory feeding L5 |
| cm-palette.less | **ab-palette.less** | L4 default seeds / raw values |
| cm-font-themes.less | **ab-font-themes.less** | L3 heading tokens + L4 values |
| vanilla-overrides.less | **ab-vanilla-overrides.less** | **L2 adapter** (seam rules + `--ab-base-if-adapt-*`) |
| theme.less | **ab-core.less** | L2 app-rules + L3 pivot core |
| cm-notify / -buttons / -cards / -callouts / -icons / -links / -dropdown | **ab-** each | component systems (read L3) |
| cmet-content.less / cmet-icons.less | **ab-content.less / ab-icons-ext.less** | component systems |
| cm-themes.less | **stays cm-themes.less** | CM presentational brand look |
| cm-theme-packs.less | **stays cm-theme-packs.less** | CM dark-blue/grey packs (L5/L6-style) |
| — | **NEW `cm-<stub>.less`** (the L6 user profile) | fills the L5 theme contract with CM values |

## Class mapping
**AB (rename `cm-` → `ab-`):** cm-theme (the gate), cm-force-light, cm-dark(-tokens),
cm-fluid, cm-font-dark-tokens, cm-popup-dark-tokens, cm-container, cm-link,
cm-has-title-icon, cm-scheme-/cm-scheme-loop, **cm-profile-*** (dusk/ember/fern/
harbour/orchid/studio — colour theory = AB), and the mixins cm-btn-colour-loop,
cm-btn-outline-loop, cm-callout-colour-loop, cm-callout-named, cm-card-colour-loop,
cm-card-functional, cm-icon-colour-loop.

**CM (stay `cm-`):** cm-theme-dark-blue, cm-theme-dark-grey, cm-theme-dark-blue-grey,
cm-pack-dark-* (all pack mixins), cm-tile-accent, cm-tile-soft,
cm-tile-icon-assessment.

⚠ **Collision:** `cm-theme` (gate → `ab-theme`) is a prefix of
`cm-theme-dark-blue-grey` (stays). The rename MUST match whole tokens /
longest-first, never a blind substring replace, or it corrupts the pack classes.
(The same whole-token discipline applies to the token families above: map by
family, never by a blind `--cm-` → `--ab-` substring pass, or role tokens and
seeds collapse into one namespace.)

## Config `_htmlClasses`
`"cm-theme cm-profile-ember cm-theme-dark-blue-grey cm-force-light"`
→ `"ab-theme ab-profile-ember cm-theme-dark-blue-grey ab-force-light"`
(gate + colour-theory profile + force-light become AB; the brand pack stays CM.)

## Also touched (don't miss)
- `adapt-abbott-*` component LESS — all `--cm-*` reads → the L3 pivot `--ab-base-*`.
- Extension JS (`adapt-abbott-theme.js`, `cm-theme-switcher.js`) — class names it
  toggles (`cm-theme`, `cm-force-light`, `data-theme`) → the AB names.
- Course JSON `_classes` / skeletons — any AB class referenced (e.g. the gate,
  profiles); brand classes (cm-theme-dark-blue-grey, cm-tile-*) unchanged.
- `bower.json` extension name/displayName if desired (optional).
- Docs under docs/authoring/ (cm-theme-architecture.md) — update prose to AB/CM;
  theming-layers-map.md + ab-system-architecture.md already carry the target.

## Migration strategy — PHASED (ii), chosen (Abbott, 11 Oct 2026)
The restructure is bigger than the original "one atomic pass," so it lands in
verifiable phases, each of which **renders and bisects** (matching
`ab-system-architecture.md` sequencing). The alternative — one atomic restructure
— was rejected: a single large diff is hard to bisect if the build-test then
fails. Every phase ends with `lessc` passing on every file AND a build-test
confirming the course still renders, before the next phase starts.

## Execution plan (phased)
**Phase 0 — build-test the CURRENT `--cm-` stack renders.** The gate on everything
below (colour, fluid type, light/dark, profiles). Nothing starts until this passes.

**Phase 1 — namespace move + file `git mv` (keep today's structure).** Map
`--cm-*` by family (never a blind substring pass): role/semantic/heading/type/
layout tokens → the L3 pivot `--ab-base-*` (still holding values directly, as
today — no hook yet); the cm-base seeds/dials → `--ab-base-pf-default-*`. `git mv`
the AB files to `ab-*`. Rename classes whole-token / longest-first per the AB list,
leaving the CM-stays list untouched. Update config `_htmlClasses` + JS/JSON class
refs. `lessc` all (incl. the cross-file ladder). The look is byte-for-byte
unchanged — only names move. Commit, build-test.

**Phase 2 — insert the L2 adapter (seam 1).** Add `--ab-base-if-adapt-*` tokens
mirroring vanilla's named vars; repoint the sweep rules (now `ab-vanilla-overrides`)
to read those adapter tokens; alias each adapter token to its L3 pivot token
(`--ab-base-if-adapt-item-color: var(--ab-base-accent)`). Behaviour identical —
this only adds the indirection. Commit, build-test.

**Phase 3 — split L4/L5 + wire the L3 hook (seam 2).** Turn each pivot token into a
hook — `--ab-base-accent: var(--ab-theme-pf-default-accent, var(--ab-base-pf-default-accent))`
— moving its current value down into the L4 `--ab-base-pf-default-*` and leaving the
L5 `--ab-theme-pf-default-*` contract empty (declared, unset). With no theme active,
L3 falls through to L4 = the same render. Commit, build-test.

**Phase 4 — extract L6 user profiles.** Pull CM's dark-blue user-theme values out into
the L6 `--cm-<stub>-*` profile and bind them into the L5 contract; add the SA
placeholder profile. With the CM profile active the look is unchanged; swapping to
SA proves the architecture. Commit, build-test.

Each phase is its own commit (or small set); a phase that fails its build-test is
fixed or reverted before the next. **Phase 0 gates all of it.**
