# SVG scribble

Eight original path-based marks: box + hatch, zigzag, loops, double underline,
circle, arrow, crosshatch and spiral. `scribble.html` is a runnable component
example. No build or font download is required.

Load `scribble.css` and `scribble.js`, then call
`Scribble.mountScribble(host)`. The controls independently change speed
(.25-3x), size (.5-1.5x) and angle (-45 to 45 degrees). Changes show the finished
mark; Replay draws once with staggered strokes, then leaves it visible.
The overlay ignores pointer input, so underlying HTML stays selectable.

The mount returns `get()`, `load({ mark, speed, size, angle })`, `replay()`,
`svg()` and `destroy()`. Invalid settings throw without changing the last valid
state. `scribble:change` carries current settings.

`svg()` returns the current SVG markup, including its token overrides and path
data. Include `scribble.css` when reusing it. Remove `is-playing` for a static
mark; add it to draw on mount. Every path uses `pathLength="1"`.

Tokens: `--scribble-colour` (defaults to `--accent`),
`--scribble-duration`, `--scribble-size`, `--scribble-angle`,
`--scribble-stroke`, and per-path `--scribble-delay`. Size/angle affect the
mark, not the underlying HTML. Strokes use non-scaling widths.
System reduced motion and `.no-motion` / `data-tm-no-motion="true"` render the
completed mark immediately. No infinite animations or SVG filter IDs.

See the [combined preview](../../backgrounds/textured/index.html).
