# Chalk drawing patterns

Open [the gallery](index.html). It contains 36 independent examples:

- A line/box mixer: straight, elbow or curved line with rectangle, rounded or sketch box.
- Circle cycles split into 1–4 sequential parts.
- Triangle cycles split into 1–4 sequential parts.
- Rectangle, square, circle, triangle, straight line, three arrows and exclamation mark.
- Seven more arrows/connectors: double-headed, return, S-curve, rounded elbow,
  fork, merge and loop-back.
- Five more nodes: decision diamond, oval, rounded rectangle, hexagon and speech bubble.
- Six emphasis marks: check, cross, star, paired brackets, grouping brace and double underline.

Each example has an individual HTML page and a default self-contained SVG.
All nine line/box combinations also have separate SVG files. See the filenames
in this folder; a cycle's part count divides one closed outline, not multiple shapes.

Play draws once and holds the result. Replay restarts; pause resumes at the same
position. Repeat is optional. Master and local speed multiply together. Arrows
are separate paths and can be hidden; their timing slots remain short pauses.
Reduced motion always shows finished artwork.

Use Copy reusable code or Download current SVG for an SVG containing its own
styles plus current speed/repeat/arrow settings. Clipboard failures display an
error and select the code for manual copying. Default SVG downloads draw once
automatically when opened; the HTML previews wait for Play.

SVGs use `--accent` with a teal fallback and `currentColor` strokes.
Speed tokens: `--edu-duration` (default 4s), `--edu-speed`,
`--edu-local-speed`, `--edu-iterations`. There are no external dependencies.
Inlining SVGs allows host token inheritance; `<img>` SVGs cannot inherit host CSS.
When combining examples, include the common animation stylesheet only once.

To regenerate from the existing studio drawing library:

```powershell
node .\assets\interactive\chalk-patterns\build-patterns.cjs
```

Source artwork is preserved. The 18 additional patterns are defined in the
generator and reuse the same card, stroke timing and playback controls.
Multi-stroke marks draw in order; connector arrowheads are separate, optional
paths. The original studio is not modified.
