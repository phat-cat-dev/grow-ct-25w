# Individual flow diagrams

| Diagram | HTML component | Standalone SVG |
| --- | --- | --- |
| Circle | [circle.html](./circle.html) | [circle.svg](./circle.svg) |
| Triangle | [triangle.html](./triangle.html) | [triangle.svg](./triangle.svg) |
| Square | [square.html](./square.html) | [square.svg](./square.svg) |
| Vertical | [vertical.html](./vertical.html) | [vertical.svg](./vertical.svg) |
| Horizontal | [horizontal.html](./horizontal.html) | [horizontal.svg](./horizontal.svg) |

Open [index.html](./index.html) to compare them. Each HTML component works
directly from disk, with shared `diagrams.css` and optional playback in
`diagrams.js`. Copy the article and its inline SVG into your page to reuse it.
The script automatically mounts `[data-flow-card]` elements present on load;
use `FlowDiagrams.mount(host)` for dynamically inserted cards. The mount returns
`play()`, `setNodeCount(count)` and `destroy()`.

Each card has a Nodes selector (2 through 12). Circle nodes follow the circular
arc; Triangle and Square nodes are equally spaced along their perimeters,
including any corners between them. Vertical/Horizontal nodes are distributed
along the sequence. Node radii shrink when necessary to avoid overlap.
Changing count preserves playback, pause, speed and runner layer settings.
The accessible diagram label updates to match. Invalid API counts throw an
explicit `RangeError` rather than silently clamping.

“Download current” exports the configured diagram, including its colours and
numbering, as a self-contained **static** SVG (no runner). Without JavaScript
the link downloads the original default SVG. Changes are local to the card;
they are not saved to browser storage or written over the supplied source SVGs.

Standalone SVG files embed their diagram styles and require no scripts or
network assets. They are static by default. Inline them to inherit your theme
tokens; an `<img>` cannot inherit the containing page's CSS custom properties.
Add `is-playing` to the SVG for opt-in playback, `is-paused` to pause it.
The runner loops only while playback is enabled; the HTML includes Pause.
System reduced motion and `.no-motion` / `data-tm-no-motion="true"` render static
diagrams with no travelling runner.

Tokens: `--flow-accent` -> `--accent`, `--flow-paper` -> `--surface-1`,
`--flow-ink` -> `--ink`, `--font-ui`, `--flow-height`, and `--flow-rate`.
Speed changes the edge draw durations, delays and runner speed together.
Runner Over/Behind changes SVG paint order without changing the route.
The original view boxes, paths, node numbering and accessible labels are retained.

## Regeneration

The assets are extracted from the five known SVGs in the existing
[flow gallery](../../.dev/assets/gallery/flows.html). After changing that source
or the shared CSS, regenerate:

```powershell
node .\assets\diagrams\build-diagrams.cjs
```

The generator checks for each named source diagram and fails explicitly if one
is missing. Generated HTML/SVG files are deliverables and do not depend on the
archived gallery at runtime. `diagrams.css` and `diagrams.js` are hand-maintained.
