# Typography

## 1.0 Heading schemes

<section id="headings">
    <h2 class="sec" data-css-index="7">5 · Heading schemes <code>.scheme</code><button type="button" class="sendcss">⧉ Send to CSS</button></h2>
    <div class="card-doc">
    <div class="panel headings scheme hsc-diagonal hdec-none hbul-none hsz-graded" id="headWrap">
      <div><h1>Depth from a single hue</h1><small>h1</small></div>
      <div><h2>The grey equivalent of that blue</h2><small>h2</small></div>
      <div><h3>Shading gives the sense of layers</h3><small>h3</small></div>
      <div><h4>Quiet enough to recede</h4><small>h4</small></div>
      <div><h5>A supporting detail line</h5><small>h5</small></div>
      <div><h6>Faint section label</h6><small>h6</small></div>
    </div>
    <div class="hovmodes" id="headCaps" role="group" aria-label="Uppercase by heading level">
      <label><input type="checkbox" aria-label="H1 CAPS"> H1 CAPS</label>
      <label><input type="checkbox" aria-label="H2 CAPS"> H2 CAPS</label>
      <label><input type="checkbox" aria-label="H3 CAPS"> H3 CAPS</label>
      <label><input type="checkbox" aria-label="H4 CAPS"> H4 CAPS</label>
      <label><input type="checkbox" aria-label="H5 CAPS"> H5 CAPS</label>
      <label><input type="checkbox" aria-label="H6 CAPS" checked> H6 CAPS</label>
    </div>
    <p class="note">CAPS by heading level: use our suggested defaults or choose your own. Off preserves the original text casing. These choices stay independent of colour, size and reverse settings, and are saved and exported with your theme.</p>
<div class="hovmodes" id="headScheme" role="radiogroup" aria-label="Scheme">
      <label><input type="radio" name="hsc" value="diagonal" checked=""> Diagonal</label>
      <label><input type="radio" name="hsc" value="grey"> Colour-grey</label>
      <label><input type="radio" name="hsc" value="gray"> Pure grey</label>
      <label><input type="radio" name="hsc" value="mono"> Mono</label>
      <label><input type="radio" name="hsc" value="twotone"> Two-tone</label>
      <label><input type="radio" name="hsc" value="accent"> Accent-top</label>
      <label><input type="radio" name="hsc" value="muted"> Muted</label>
      <label><input type="radio" name="hsc" value="analogous"> Analogous</label>
      <label><input type="radio" name="hsc" value="complementary"> Complementary</label>
      <label><input type="radio" name="hsc" value="triadic"> Triadic</label>
      <label><input type="radio" name="hsc" value="split"> Split-complementary</label>
      <label><input type="radio" name="hsc" value="square"> Square</label>
      <label><input type="radio" name="hsc" value="spectrum"> Spectrum</label>
      <label><input type="radio" name="hsc" value="golden-angle"> Golden angle</label>
    </div>
    <p class="note">Heading colour formulas follow your active main hue. Muted uses 45% of its saturation. Analogous offsets H1–H6 by 0°, +15°, +30°, −15°, −30°, +45°; Complementary uses the base for H1–H3 and its opposite for H4–H6; Triadic cycles 0°/120°/240°; Split cycles 0°/150°/210°; Square cycles 0°/90°/180°/270°; Spectrum steps by 60°; Golden angle steps by approximately 137.508°. Reverse reverses hue and brightness order for these harmony schemes, not heading sizes. They style headings only; the separate colour harmony palette is unchanged. Set downstream to apply across the page. Saved/exported as typography settings, not baseline <code>.hsc-*</code> classes.</p>
    <div class="hovmodes" id="headDec" role="radiogroup" aria-label="Decoration">
      <label><input type="radio" name="hdec" value="none" checked=""> No line</label>
      <label><input type="radio" name="hdec" value="underline"> Underline</label>
      <label><input type="radio" name="hdec" value="dashed"> Dashed</label>
      <label><input type="radio" name="hdec" value="dotted"> Dotted</label>
      <label><input type="radio" name="hdec" value="leftborder"> Left border</label>
    </div>
    <div class="connector-controls">
      <label>Underline thickness <input id="underlineWidth" type="range" min="0.01" max="0.3" step="0.01" value="0.06"><output id="underlineWidth-val">0.06 em</output></label>
      <label>Left-border width <input id="borderWidth" type="range" min="0.01" max="0.5" step="0.01" value="0.18"><output id="borderWidth-val">0.18 rem</output></label>
    </div>
    <div class="hovmodes" id="headBul" role="radiogroup" aria-label="Bullet">
      <label><input type="radio" name="hbul" value="none" checked=""> No bullet</label>
      <label><input type="radio" name="hbul" value="chevron"> › Chevron</label>
      <label><input type="radio" name="hbul" value="dot"> • Dot</label>
      <label><input type="radio" name="hbul" value="arrow"> → Arrow</label>
      <label><input type="radio" name="hbul" value="circle"> ○ Circle</label>
      <label><input type="radio" name="hbul" value="square"> ▪ Square</label>
      <label><input type="radio" name="hbul" value="diamond"> ◆ Diamond</label>
      <label><input type="radio" name="hbul" value="star"> ★ Star</label>
      <label><input type="radio" name="hbul" value="check"> ✓ Check</label>
      <label><input type="radio" name="hbul" value="plus"> + Plus</label>
      <label><input type="radio" name="hbul" value="dash"> – Dash</label>
      <label><input type="radio" name="hbul" value="doublechevron"> » Double chevron</label>
    </div>
    <p class="note">Academic practice bullets</p>
    <div class="hovmodes academic-bullets" id="academicBul" role="radiogroup" aria-label="Academic practice bullet">
      <label><input type="radio" name="hbul" value="academic-starting"><svg aria-hidden="true"><use href="#ic-starting"></use></svg> Starting</label>
      <label><input type="radio" name="hbul" value="academic-assessment"><svg aria-hidden="true"><use href="#ic-assessment"></use></svg> Assessment</label>
      <label><input type="radio" name="hbul" value="academic-feedback"><svg aria-hidden="true"><use href="#ic-feedback"></use></svg> Feedback</label>
      <label><input type="radio" name="hbul" value="academic-researching"><svg aria-hidden="true"><use href="#ic-researching"></use></svg> Researching</label>
      <label><input type="radio" name="hbul" value="academic-progressing"><svg aria-hidden="true"><use href="#ic-progressing"></use></svg> Progressing</label>
      <label><input type="radio" name="hbul" value="academic-writing"><svg aria-hidden="true"><use href="#ic-writing"></use></svg> Writing</label>
      <label><input type="radio" name="hbul" value="academic-reflecting"><svg aria-hidden="true"><use href="#ic-reflecting"></use></svg> Reflecting</label>
      <label><input type="radio" name="hbul" value="academic-criticality"><svg aria-hidden="true"><use href="#ic-criticality"></use></svg> Criticality</label>
      <div class="academic-extra-row">
        <label><input type="radio" name="hbul" value="academic-learning"><svg aria-hidden="true"><use href="#ic-learning"></use></svg> Learning</label>
        <label><input type="radio" name="hbul" value="academic-studying"><svg aria-hidden="true"><use href="#ic-studying"></use></svg> Studying</label>
        <label><input type="radio" name="hbul" value="academic-referencing"><svg aria-hidden="true"><use href="#ic-referencing"></use></svg> Referencing</label>
        <label><input type="radio" name="hbul" value="academic-presenting"><svg aria-hidden="true"><use href="#ic-presenting"></use></svg> Presenting</label>
      </div>
    </div>
    <label>Heading icon size <input id="iconSize" type="range" min="0.3" max="2" step="0.01" value="0.72"><output id="iconSize-val">0.72 em</output></label>
    <p class="note">Choose from 12 Academic practice icons. Resize them independently of heading text, from 0.3 to 2 times the heading font size. Icons stay vertically centred beside the text, including collapsible headings. Saved and exported with your typography settings.</p>
    <div class="hovmodes" id="headSize" role="radiogroup" aria-label="Size">
      <label><input type="radio" name="hsz" value="graded" checked=""> Graded sizes</label>
      <label><input type="radio" name="hsz" value="uniform"> Uniform size</label>
      <label><input type="radio" name="hsz" value="minor-second"> Minor second · 1.067</label>
      <label><input type="radio" name="hsz" value="major-second"> Major second · 1.125</label>
      <label><input type="radio" name="hsz" value="minor-third"> Minor third · 1.200</label>
      <label><input type="radio" name="hsz" value="major-third"> Major third · 1.250</label>
      <label><input type="radio" name="hsz" value="perfect-fourth"> Perfect fourth · 1.333</label>
      <label><input type="radio" name="hsz" value="augmented-fourth"> Augmented fourth · 1.414</label>
      <label><input type="checkbox" id="headRev"> Reverse</label>
      <label style="border:none;background:none;gap:8px;">Scale <input type="range" id="headScale" min="0.8" max="1.8" step="0.01" value="1" style="width:110px;vertical-align:middle;"> <b id="headScale-val" style="font-family:var(--font-mono);font-size:.78rem;color:var(--ink);">1.35×</b></label>
    </div>
    <p class="note" id="heading-size-formula" aria-live="polite"></p>
    <p class="note">The six modular scales grade the size difference between heading levels: H6 starts at 0.875rem, then each level multiplies by the chosen ratio up to H1. They scale fluidly from 85% to 100% between 20rem and 80rem viewports, keeping the ratio consistent. Scale multiplies all six sizes; Reverse affects colour order only. These are heading-size formulas, not changes to the separate Spacing tool.</p>
    <div class="btnrow" style="margin:14px 0 0;align-items:center;">
      <button class="ab btn primary btn-sm" id="setDownstream">Set downstream — apply to whole page ↓</button>
      <span style="color:var(--ink-soft);font-size:.8rem;">stamps this scheme onto every heading on the page</span>
    </div>
    <div class="panel headings" id="downstream" style="margin-top:12px;">
      <h2>Downstream heading</h2>
      <p style="color:var(--ink-soft);margin:.3rem 0 1rem;font-size:.9rem;">Body copy under the applied scheme. Tune the controls above, then press “Set downstream” to push the colouring here.</p>
      <h3>A subsection</h3>
      <p style="color:var(--ink-soft);margin:.3rem 0 1rem;font-size:.9rem;">Shows the ramp in a real reading context rather than a label list.</p>
      <h4>A minor point</h4>
    </div>
<p class="note">Put <code>.scheme</code> on any container (a section or <code>&lt;body&gt;</code>) and headings inside follow it. Stamp a full scheme as a class string:</p>
    <pre>&lt;main class="scheme hsc-twotone hdec-dotted hbul-chevron hsz-graded"&gt;…&lt;/main&gt;</pre>
    <p class="note">Schemes</p>
    <div class="classlist"><span>hsc-diagonal</span><span>hsc-grey</span><span>hsc-gray</span><span>hsc-mono</span><span>hsc-twotone</span><span>hsc-accent</span></div>
    <p class="note">Decoration · bullets · size · reverse · scale</p>
    <div class="classlist"><span>hdec-underline/dashed/dotted/leftborder</span><span>hbul-chevron/dot/arrow</span><span>hsz-graded/uniform</span><span>hrev</span><span>--hscale</span></div>
    </div>
  </section>

## 2.0 Body text
<div class="card-doc" data-typography-live>
<div class="connector-controls">
<label>Body size ceiling <input id="bodySize" type="range" min="12" max="24" step="1" value="16"><output id="bodySize-val">16 px</output></label>
<label>Line height <input id="lineHeight" type="range" min="1.2" max="2.2" step="0.05" value="1.55"><output id="lineHeight-val">1.55</output></label>
<label>Reading width <input id="readingWidth" type="range" min="40" max="100" step="1" value="70"><output id="readingWidth-val">70 ch</output></label>
</div>
<p>Good typography adapts to the space it has. Body text and headings scale smoothly between narrow and wide screens, while relative units preserve browser zoom and reader preferences. This paragraph is a live reading specimen: adjust its size ceiling, leading and measure to find a comfortable rhythm.</p>
<p class="note">Fluid sizes grow between 20rem and 80rem viewports. The body minimum is 87.5% of its ceiling (at least .75rem); heading minima vary by level. Reading width is a maximum, never a fixed column width.</p>
</div>


## 4.0 Web fonts
CHOICE of OOGLE FONTS

## 5.0 Typography scheme
<div class="card-doc" data-typography-live>
<p id="type-status" role="status"></p>
<button type="button" class="ab btn secondary" id="type-reset">Reset typography</button>
<pre id="type-css"></pre>
</div>

<h2 class="sec" data-css-index="7">5 · Heading scheme layer <code>.scheme</code><button type="button" class="sendcss">⧉ Send to CSS</button></h2>
<div class="card-doc">
  <p class="note">Put <code>.scheme</code> on any container (a section or <code>&lt;body&gt;</code>) and headings inside follow it. Stamp a full scheme as a class string:</p>
  <pre>&lt;main class="scheme hsc-twotone hdec-dotted hbul-chevron hsz-graded"&gt;…&lt;/main&gt;</pre>
  <p class="note">Schemes</p>
  <div class="classlist"><span>hsc-diagonal</span><span>hsc-grey</span><span>hsc-gray</span><span>hsc-mono</span><span>hsc-twotone</span><span>hsc-accent</span></div>
  <p class="note">Decoration · bullets · size · reverse · scale</p>
  <div class="classlist"><span>hdec-underline/dashed/dotted/leftborder</span><span>hbul-chevron/dot/arrow</span><span>hsz-graded/uniform</span><span>hrev</span><span>--hscale</span></div>
</div>
<p class="note">Put <code>.scheme</code> on any container (a section or <code>&lt;body&gt;</code>) and headings inside follow it. Stamp a full scheme as a class string:</p>
<div class="panel headings" id="downstream" style="margin-top:12px;">
      <h2>Downstream heading</h2>
      <p style="color:var(--ink-soft);margin:.3rem 0 1rem;font-size:.9rem;">Body copy under the applied scheme. Tune the controls above, then press “Set downstream” to push the colouring here.</p>
      <h3>A subsection</h3>
      <p style="color:var(--ink-soft);margin:.3rem 0 1rem;font-size:.9rem;">Shows the ramp in a real reading context rather than a label list.</p>
      <h4>A minor point</h4>
    </div>
    <p class="note">Put <code>.scheme</code> on any container (a section or <code>&lt;body&gt;</code>) and headings inside follow it. Stamp a full scheme as a class string:</p>
    <div class="classlist"><span>hsc-diagonal</span><span>hsc-grey</span><span>hsc-gray</span><span>hsc-mono</span><span>hsc-twotone</span><span>hsc-accent</span></div>