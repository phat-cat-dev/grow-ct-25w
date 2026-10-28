# SVG icon collections

Open [all collections](index.html), or an individual collection:

- [Academic practice areas](academic-practice.html): 20 icons.
- [Resources](resources.html): 12 icons.
- [Library](library.html): 1 icon.

These are the existing studio SVGs, presented consistently as plain buttons with
counts, icon-only buttons, search, selected-markup preview and keyboard-accessible
copy buttons. There are no surrounding pack/control panels or inner icon boxes.
Visible sprite-ID labels and their toggle are removed. Accessible button names
and hover titles remain. Size and optional rounded-button controls sit below the preview packs.
Borders default to 0 px; choose 0–8 px and solid, dashed, dotted, double or none.
The optional border is on the button itself, not a nested frame.
Entrance options are none (default), fade, rise and gentle pop, with duration
100–2000 ms and stagger 0–300 ms. Choose an effect or press Replay entrance.
Search cancels playback; replay includes only visible results. Keyboard focus
on an icon reveals all buttons immediately. System reduced motion skips effects.
Search covers these 33 local icons, not Google's catalogue.

Click an icon to select and copy **self-contained SVG markup**. Clipboard failures
are reported and the markup is selected for manual copying. Download links work
without clipboard permission. Every icon is also an individual `.svg` file.
Collection `.sprite.svg` files preserve the original `ic-*` symbol IDs for users
who prefer sprites. No network requests or external fonts are required.

```html
<img src="ic-starting.svg" width="32" height="32" alt="Starting">
<!-- For sprites, place the symbols inline in your page, then: -->
<svg width="32" height="32" role="img" aria-label="Starting">
  <use href="#ic-starting"></use>
</svg>
```

Inline icons inherit `currentColor`; an SVG loaded through `<img>` cannot inherit
the surrounding document's text colour. Copied markup contains paths and a
viewBox rather than a reference to a sprite on another page.

The gallery consumes existing `--ink`, `--ink-soft`, `--surface-1`, `--surface-2`,
`--line`, `--accent`, `--radius`, `--font-ui` and `--font-mono` tokens, with standalone
system light/dark fallbacks. The preview size and frames are gallery-only settings;
copied markup and downloads stay independent of them.

Regenerate pages, sprites and individual SVGs from the source studio with:

```powershell
node .\assets\icons\build-icons.cjs
```

Existing artwork and IDs are retained, not redrawn. Keep the upstream artwork's
licensing/attribution requirements when redistributing it. The source studio's
Google connector is linked as a separate companion, not loaded or duplicated.
