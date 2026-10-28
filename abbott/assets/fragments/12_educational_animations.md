# Educational drawing animations

## 1.0 Chalk drawing library

<p class="note">Mix line and box variants, build whole cycles from one, two, three or four sequential parts, or reuse individual nodes and arrows. Strokes use the active theme accent; arrows are separate paths, not baked into the outline. Each cycle closes into one complete shape.</p>

EDUCATIONAL_ANIMATIONS

## 2.0 The master clock and reusable code

<div class="card-doc">
<p>Copy any example for a self-contained SVG, wrapper and animation stylesheet. No animation library is needed. Place these variables on a common ancestor to control every drawing together:</p>
<pre>:root {
  --edu-duration: 4s;    /* total time for one sequence */
  --edu-speed: 1;        /* master multiplier: 2 = twice as fast */
  --edu-local-speed: 1;  /* override on one drawing if needed */
  --edu-iterations: 1;   /* use infinite to repeat */
}
/* Example local override: */
.my-fast-drawing { --edu-local-speed: 2; }</pre>
<p>Add <code>edu-running</code> to the SVG wrapper to draw it. Add <code>edu-paused</code> to pause, or <code>edu-no-arrows</code> to hide arrow strokes. Remove and re-add <code>edu-running</code> with a layout flush to replay. Separate examples share the same keyframe names, so include the common stylesheet only once when combining them. With arrows hidden, their time slots remain as short pauses; the master cycle stays the same length.</p>
<p>Line and box paths can be swapped independently. Every path uses <code>pathLength="1"</code>; normalized dash offsets draw straight and curved strokes with the same timing system. Segment count changes how the single complete outline is divided, not how many circles or triangles appear. Colour converts to the host theme's <code>--accent</code>, with a teal fallback outside the workbench.</p>
<p>The board is a theme-tinted teaching surface, not a fixed black colour. SVG strokes stay sharp at any size. A light chalk-like shadow and rounded caps suggest a hand-drawn stroke without flashing, random jitter or heavy noise filters.</p>
<p>Research: <a href="https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/pathLength" target="_blank" rel="noreferrer">MDN: pathLength</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-dashoffset" target="_blank" rel="noreferrer">stroke-dashoffset</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration" target="_blank" rel="noreferrer">animation-duration</a>, and <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion" target="_blank" rel="noreferrer">prefers-reduced-motion</a>. Reduced motion always shows the completed shape; playback is opt-in.</p>
</div>