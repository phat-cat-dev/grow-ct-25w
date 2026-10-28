# Spacing

## 1.0 Fluid foundations

<div class="card-doc" data-spacing-controls>
<p class="note">Three independent fluid bases: <strong>text</strong>, <strong>space</strong> and <strong>layout</strong>. Each grows smoothly between two viewport widths, then stops at its bounds. Sizes and viewport bounds are in rem (1rem follows the reader's root font size). Resize the browser to see the measured values change.</p>
<div class="connector-controls">
<label>Starting profile <select data-spacing-live><option value="default">Default</option><option value="compact">Compact</option><option value="roomy">Roomy</option><option value="custom" disabled>Custom settings</option></select></label>
<button type="button" class="ab btn secondary" data-spacing-live>Reset fluid settings</button>
</div>
<div class="fluid-settings">
<fieldset><legend>Viewport range (rem)</legend><label>Minimum <output data-spacing-value="viewportMin">20 rem</output><input type="range" min="10" max="120" step="1" value="20" data-spacing-setting="viewportMin" data-spacing-live></label><label>Maximum <output data-spacing-value="viewportMax">45 rem</output><input type="range" min="10" max="120" step="1" value="45" data-spacing-setting="viewportMax" data-spacing-live></label></fieldset>
<fieldset><legend>Text base (rem)</legend><label>Minimum <output data-spacing-value="textMin">0.75 rem</output><input type="range" min=".5" max="3" step=".05" value=".75" data-spacing-setting="textMin" data-spacing-live></label><label>Maximum <output data-spacing-value="textMax">1 rem</output><input type="range" min=".5" max="3" step=".05" value="1" data-spacing-setting="textMax" data-spacing-live></label></fieldset>
<fieldset><legend>Space base (rem)</legend><label>Minimum <output data-spacing-value="spaceMin">0.75 rem</output><input type="range" min=".5" max="3" step=".05" value=".75" data-spacing-setting="spaceMin" data-spacing-live></label><label>Maximum <output data-spacing-value="spaceMax">1 rem</output><input type="range" min=".5" max="3" step=".05" value="1" data-spacing-setting="spaceMax" data-spacing-live></label></fieldset>
<fieldset><legend>Layout base (rem)</legend><label>Minimum <output data-spacing-value="layoutMin">0.75 rem</output><input type="range" min=".5" max="3" step=".05" value=".75" data-spacing-setting="layoutMin" data-spacing-live></label><label>Maximum <output data-spacing-value="layoutMax">1 rem</output><input type="range" min=".5" max="3" step=".05" value="1" data-spacing-setting="layoutMax" data-spacing-live></label></fieldset>
<fieldset><legend>Icon size (rem)</legend><label>Minimum <output data-spacing-value="iconMin">1.5 rem</output><input type="range" min=".5" max="6" step=".05" value="1.5" data-spacing-setting="iconMin" data-spacing-live></label><label>Maximum <output data-spacing-value="iconMax">2.5 rem</output><input type="range" min=".5" max="6" step=".05" value="2.5" data-spacing-setting="iconMax" data-spacing-live></label></fieldset>
</div>
<p id="spacing-status" role="status" aria-live="polite"></p>
</div>

## 2.0 Live container and cards

<div class="fluid-stage" data-ab-profile="custom">
<div class="fluid-container">
<p class="eyebrow">Your live settings</p>
<h3 class="fluid-title">Room for ideas to grow</h3>
<p class="fluid-copy">A container sets the outer rhythm. Cards use item padding, their layout uses item margins, and the text has its own fluid scale. All colours follow your main theme.</p>
<div class="fluid-cards">
<article class="fluid-card"><span class="fluid-marker" aria-hidden="true"><svg class="fluid-icon"><use href="#ic-progressing"></use></svg></span><h4 class="fluid-card-title">Explore a little</h4><p class="fluid-copy">Small screens keep a compact rhythm. Larger viewports give the same content more breathing room.</p><a class="ab btn primary fluid-action" href="#typography">Explore typography</a></article>
<article class="fluid-card"><span class="fluid-marker" aria-hidden="true"><svg class="fluid-icon"><use href="#ic-criticality"></use></svg></span><h4 class="fluid-card-title">Keep it connected</h4><p class="fluid-copy">Independent scales let you open up a layout without making the text larger. Icon size has its own range, separate from text and padding.</p><a class="ab btn secondary fluid-action" href="#color">Explore colours</a></article>
</div>
<output data-spacing-readout></output>
</div>
</div>

## 3.0 Compare scoped profiles

<p class="note">These fixed profiles sit side by side at the same viewport width. Compact keeps the default text but tightens spacing; Roomy stretches spacing and layout over 20–80rem. Each scope recomputes the engine, so its children do not inherit a frozen root clamp.</p>
<div class="fluid-comparisons">
<div class="fluid-stage" data-ab-profile="compact"><div class="fluid-container"><p class="eyebrow">Compact</p><article class="fluid-card"><h4 class="fluid-card-title">Close-knit content</h4><p class="fluid-copy">Useful for dense dashboards, lists and supporting information.</p><a class="fluid-link" href="#spacing">See the rhythm</a></article><output data-spacing-readout></output></div></div>
<div class="fluid-stage" data-ab-profile="default"><div class="fluid-container"><p class="eyebrow">Default</p><article class="fluid-card"><h4 class="fluid-card-title">An everyday rhythm</h4><p class="fluid-copy">The supplied pack: a 0.75–1rem base over a 20–45rem viewport.</p><a class="fluid-link" href="#spacing">See the rhythm</a></article><output data-spacing-readout></output></div></div>
<div class="fluid-stage" data-ab-profile="roomy"><div class="fluid-container"><p class="eyebrow">Roomy</p><article class="fluid-card"><h4 class="fluid-card-title">Space to breathe</h4><p class="fluid-copy">More generous spacing for editorial layouts and feature panels.</p><a class="fluid-link" href="#spacing">See the rhythm</a></article><output data-spacing-readout></output></div></div>
</div>

## 4.0 Fluid type scale

<div class="fluid-type-scale" data-ab-profile="custom">
<p style="font-size:var(--ab-text-2xs)">2xs · An annotation</p>
<p style="font-size:var(--ab-text-xs)">xs · A short supporting sentence</p>
<p style="font-size:var(--ab-text-sm)">sm · A readable introduction</p>
<p style="font-size:var(--ab-text-md)">md · A clear subheading</p>
<p style="font-size:var(--ab-text-lg)">lg · An expressive title</p>
<p style="font-size:var(--ab-text-xl)">xl · Make room</p>
<p style="font-size:var(--ab-text-2xl)">2xl · Ideas grow</p>
</div>

## 5.0 Tokens and portable CSS

<div class="card-doc">
<p class="note">Layer 0: settings. Layer 1: <code>--ab-fluid-text</code>, <code>--ab-fluid-space</code>, <code>--ab-fluid-layout</code>. Layer 2: seven text steps, three layout tokens and four spacing tokens. Existing <code>--ab-core-*-clamp-*-l4</code> aliases remain available. A scoped <code>data-ab-profile</code> recomputes all layers.</p>
<p class="note">The original LESS files remain the source; the site build compiles them to browser-ready CSS. Changes here persist in scheme JSON and CSS exports/builds. These tokens are available page-wide; specimens opt in explicitly so the Typography section retains control of existing page text.</p>
<details><summary>Generated fluid CSS</summary><pre id="spacing-css"></pre></details>
</div>