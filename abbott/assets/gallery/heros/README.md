# Individual hero assets

Nine copy-ready hero fragments: `aurora.html`, `mesh.html`, `gradient.html`,
`dots.html`, `waves.html`, `night.html`, `editorial.html`, `blueprint.html`,
`split.html`. Open [index.html](./index.html) for the light/dark/hue preview.

The first six reinterpret the existing hero gallery as namespaced assets.
Editorial, Blueprint and Split add quieter static alternatives. Use one H1
hero per real page; the preview intentionally displays several for comparison.

Include `heros.css` and your chosen fragment. The optional `heros.js` wires
Play/Pause buttons on elements present when loaded. Without it the artwork stays
still. No build step, network, icon font or framework is needed at runtime.
Set real Start/Outline destinations in the fragment before shipping; the gallery
provides working in-page example destinations.

The CSS only targets `.asset-hero`. Tokens inherit the host's surface, ink,
accent, hue, saturation, fonts and spacing. Override `--hero-paper`,
`--hero-raised`, `--hero-ink`, `--hero-muted`, `--hero-accent`, `--hero-hue`,
`--hero-saturation` and `--hero-pad` per hero.
Night owns a fixed dark surface and matching light ink in either theme.

Motion is paused by default. Setting `data-hero-playing="true"` opts in.
The supplied button can stop it; reduced-motion preferences and host
`.no-motion` / `data-tm-no-motion="true"` stop animations regardless of the button.
Legibility scrims sit behind the text, not over it; decorative layers are hidden
from assistive technology and do not intercept interaction.

The Dots variant has no outer border, with stronger dots visible farther left.
Its background is a 7% accent tint over `--hero-host` (default `--surface-1`), so
it sits very close to the host page colour, and the dots fade vertically into
`--hero-host` at the bottom. Hosts set `--hero-host` to their page background;
the lesson preview maps it to the Theme Manager's live `--tm-bg`.
It owns a light canvas with dark text in either host theme so the white fade
does not compromise text contrast.
With `heros.js`, its artwork fades out over 1.8 seconds during pointer movement,
clicks/taps, keyboard use, scrolling or input anywhere on the page, and starts
fading back after 3 seconds without those events. Play motion (or
`data-hero-playing="true"` without a button, as the lesson page does) enables a gentle
18-second looping swirl, like a slow water current, rather than diagonal drift.
Text and links stay still and visible. Reduced-motion
and host no-motion settings remove the fade transition; Play/Pause still
controls only the decorative animation. Without JavaScript, the dots stay visible.

`build-heros.cjs` generates the fragments and gallery from their content records.
After editing records, run:

```powershell
node .\assets\header\heros\build-heros.cjs
```
