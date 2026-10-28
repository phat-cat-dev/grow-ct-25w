# Self-contained SVG motion

Open [the gallery](index.html) for 22 icon/typography animations and six transition
studies from the studio Motion section. Each `.svg` embeds its own animation CSS,
vector artwork, accessible title and reduced-motion rule. No scripts, external
fonts, image files or network access are needed by an SVG.

The icon drawings are original vector interpretations of the source motifs, not
Google Material Symbols outlines. Typography remains editable SVG text using a
system font; its exact letter shapes therefore vary between platforms.
Gradient text and shadow effects use SVG clipping/duplicated text rather than
HTML background-clip or text-shadow.

## Embed

```html
<img src="spin.svg" width="160" height="65" alt="Activity in progress">
```

Use inline SVG to inherit host CSS tokens:

- `--motion-accent` (default blue), `--motion-ink`
- `--motion-line`, `--motion-muted` (shadow colours)
- `--motion-speed` (positive multiplier, default `1`)

Set `data-paused` on the SVG root to pause, or remove it to resume. A standalone
SVG or an SVG in an image starts automatically; image contents cannot inherit
host CSS variables or be paused by the host. Use inline SVG when control is
needed. Namespace IDs if embedding the same SVG more than once.

The gallery starts paused and offers play/pause, replay, speed, size and angle.
Downloads are the original self-contained files, not the adjusted preview.
Reduced-motion preferences always disable animations and leave readable artwork.
Transition files repeat a forward/hold/return demonstration; for one-time UI
state transitions, use the original studio transition controls instead.

Regenerate with `node .\assets\motion\build-motion.cjs`. Edit the generator, not
generated SVGs. The original Motion section is not modified.
