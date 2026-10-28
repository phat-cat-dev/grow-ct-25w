# Worked-example +/- cue convention

Established 9 October 2026 (Abbott ruling, this sitting). Records the authoring
convention that drives the worked-example visual cue added to the committed
theme extension `adapt-ab-theme`.

## What it is

Every worked example follows the "weaker example first" structure: it contrasts
a **weaker** approach with a **stronger** one (typically `{{learner-a}}` taking
the surface approach, then `{{learner-b}}` taking the deeper one). The theme
renders this contrast visually — a coloured left accent border plus a small
corner glyph:

- **weaker** paragraph: muted red left border, red minus glyph;
- **stronger** paragraph: muted green left border, green plus glyph.

Kept subtle (thin border, ~5% background tint, small glyph), not loud.

## The authoring rule

In each worked-example text component body, add the class `we-weaker` to the
`<p>` that carries the weaker approach, and `we-stronger` to the `<p>` that
carries the stronger approach:

```html
<p class="we-weaker">{{learner-a}} reads the chapter once and highlights ...</p>
<p class="we-stronger">{{learner-b}} reads the same chapter and keeps asking why ...</p>
```

No other paragraph is marked. The framing paragraph and the closing point stay
unclassed. The classes add **no student-facing words** — they are a presentation
hook only, so the copy is unchanged and needs no voice re-check on account of
the cue.

## Why a markup hook, not positional CSS

CSS alone cannot tell the weaker paragraph from the stronger one: in the authored
bodies both are plain `<p>` tags. Targeting them by position (`:nth-of-type`)
would be brittle — a worked example with a different paragraph count would land
the cue on the wrong paragraph silently, which is exactly the position-targeting
this project forbids. The explicit class makes the intent carry in the data, so
the cue is always on the paragraph the author meant.

## Where the CSS lives

`src/extensions/adapt-ab-theme/less/theme.less`. The extension is the
committed CSS home: its LESS compiles into `build/adapt.css` on every build
(`grunt less:compile` globs `extensions/*/less/**`), surviving `adapt-install`,
with `adapt-contrib-vanilla` as the base theme. The colours are LESS variables
(`@abbott-weaker-colour`, `@abbott-stronger-colour`) for easy adjustment.

## Applied

Applied across all five lessons of
`understanding-learning-assessment-feedback-introductory` (components
`L01-c-30` .. `L05-c-30`) at establishment. Future worked examples follow the
same convention.
