# objects

## 1.0 Cards
<h2 class="sec" data-css-index="4">7 · Cards <code>.ab.card</code><button type="button" class="sendcss">⧉ Send to CSS</button></h2>
<div class="card-doc">
    <div class="swrow">
      <div class="ab card info"><div class="card-header">Header</div><div class="card-body"><div class="card-title">Info card</div><p class="card-text">Accent tints border + header.</p></div></div>
      <div class="ab card positive invert"><div class="card-body"><div class="card-title">Invert</div><p class="card-text">Solid accent fill.</p></div></div>
      <div class="ab card negative"><div class="card-body"><div class="card-title">Negative</div><p class="card-text">One accent var drives it all.</p></div></div>
    </div>
    <p class="note">Slots</p>
    <div class="classlist"><span>card-header</span><span>card-body</span><span>card-footer</span><span>card-title</span><span>card-subtitle</span><span>card-text</span><span>card-link</span><span>card-img-top/-bottom/-overlay</span></div>
    <p class="note">Modifiers</p>
    <div class="classlist"><span>primary/secondary/positive/negative/comment/info</span><span>fam-* + sh-*</span><span>invert</span><span>soft</span><span>flat</span><span>raised</span><span>square</span><span>with-icon</span><span>hover-animate</span><span>elevated</span></div>
  </div>
<section>
    <h2 class="sec">Cards — one accent var drives border, header &amp; icon</h2>
    <div class="cardgrid">
      <div class="ab card">
        <div class="card-header">Neutral</div>
        <div class="card-body">
          <h3 class="card-title">Plain card</h3>
          <p class="card-text">No variant — border and header sit at the neutral line colour.</p>
        </div>
      </div>
      <div class="ab card primary">
        <div class="card-header">Primary</div>
        <div class="card-body">
          <h3 class="card-title">Brand accent</h3>
          <p class="card-text">The accent follows the hue slider; border and header tint with it.</p>
        </div>
        <div class="card-footer">Footer</div>
      </div>
      <div class="ab card positive">
        <div class="card-header">Positive</div>
        <div class="card-body">
          <h3 class="card-title">Confirmed</h3>
          <p class="card-text">Semantic variants sit on fixed hues so green always reads as green.</p>
        </div>
      </div>
      <div class="ab card negative">
        <div class="card-header">Negative</div>
        <div class="card-body">
          <h3 class="card-title">Something failed</h3>
          <p class="card-text">One line sets the accent; everything else is shared.</p>
        </div>
      </div>
      <div class="ab card comment">
        <div class="card-header">Comment</div>
        <div class="card-body">
          <h3 class="card-title">A note</h3>
          <p class="card-text">Violet accent, same template.</p>
        </div>
      </div>
      <div class="ab card info">
        <div class="card-header">Info</div>
        <div class="card-body">
          <h3 class="card-title">Good to know</h3>
          <p class="card-text">Header tint is a color-mix of the accent over the surface.</p>
        </div>
      </div>
    </div>
  </section>
<div class="card-doc">
<div class="cardgrid">
      <div class="ab card">
        <div class="card-header">Neutral</div>
        <div class="card-body">
          <h3 class="card-title">Plain card</h3>
          <p class="card-text">No variant — border and header sit at the neutral line colour.</p>
        </div>
      </div>
      <div class="ab card primary">
        <div class="card-header">Primary</div>
        <div class="card-body">
          <h3 class="card-title">Brand accent</h3>
          <p class="card-text">The accent follows the hue slider; border and header tint with it.</p>
        </div>
        <div class="card-footer">Footer</div>
      </div>
      <div class="ab card positive">
        <div class="card-header">Positive</div>
        <div class="card-body">
          <h3 class="card-title">Confirmed</h3>
          <p class="card-text">Semantic variants sit on fixed hues so green always reads as green.</p>
        </div>
      </div>
      <div class="ab card negative">
        <div class="card-header">Negative</div>
        <div class="card-body">
          <h3 class="card-title">Something failed</h3>
          <p class="card-text">One line sets the accent; everything else is shared.</p>
        </div>
      </div>
      <div class="ab card comment">
        <div class="card-header">Comment</div>
        <div class="card-body">
          <h3 class="card-title">A note</h3>
          <p class="card-text">Violet accent, same template.</p>
        </div>
      </div>
      <div class="ab card info">
        <div class="card-header">Info</div>
        <div class="card-body">
          <h3 class="card-title">Good to know</h3>
          <p class="card-text">Header tint is a color-mix of the accent over the surface.</p>
        </div>
      </div>
    </div>
<h3 class="sub">Family and fill style</h3>
<div class="panel">
      <div class="hovmodes" id="cFam" role="radiogroup" aria-label="Family">
        <label><input type="radio" name="cfam" value="brand" checked=""> Brand</label>
        <label><input type="radio" name="cfam" value="grey"> Colour-grey</label>
        <label><input type="radio" name="cfam" value="gray"> Pure grey</label>
      </div>
      <div class="hovmodes" id="cStyle" role="radiogroup" aria-label="Fill style">
        <label><input type="radio" name="cstyle" value="tinted" checked=""> Tinted</label>
        <label><input type="radio" name="cstyle" value="invert"> Invert</label>
        <label><input type="radio" name="cstyle" value="soft"> Soft</label>
      </div>
      <div class="cardgrid cfm-brand cst-tinted" id="cardWrap">
        <div class="ab card">
          <div class="card-header">Header</div>
          <div class="card-body"><h3 class="card-title">Themed card</h3><p class="card-text">The accent follows the family; the fill style switches the whole look.</p></div>
          <div class="card-footer">Footer</div>
        </div>
        <div class="ab card">
          <div class="card-body"><h3 class="card-title">No header</h3><p class="card-text">Border and tint both come from the one accent var.</p><a class="card-link" href="#" onclick="return false">Action</a></div>
        </div>
        <div class="ab card">
          <div class="card-header">Status</div>
          <div class="card-body"><h3 class="card-title">Try invert</h3><p class="card-text">Invert fills the card solid; tinted and soft stay light.</p></div>
        </div>
      </div>
    </div>
<p class="note">Slots</p>
    <div class="classlist"><span>card-header</span><span>card-body</span><span>card-footer</span><span>card-title</span><span>card-subtitle</span><span>card-text</span><span>card-link</span><span>card-img-top/-bottom/-overlay</span></div>
    <p class="note">Modifiers</p>
    <div class="classlist"><span>primary/secondary/positive/negative/comment/info</span><span>fam-* + sh-*</span><span>invert</span><span>soft</span><span>flat</span><span>raised</span><span>square</span><span>with-icon</span><span>hover-animate</span><span>elevated</span></div>
    </div>

### 1.1 Card layers
<section>
    <h2 class="sec">Depth — six card layers, each a lighter rung + deeper shadow</h2>
    <div class="hovmodes" id="depthFam" role="radiogroup" aria-label="Family" style="margin-bottom:10px;">
      <label><input type="radio" name="dfam" value="grey" checked=""> Colour-grey</label>
      <label><input type="radio" name="dfam" value="brand"> Brand</label>
      <label><input type="radio" name="dfam" value="gray"> Pure grey</label>
    </div>
    <div class="hovmodes" style="margin-bottom:14px;">
      <label><input type="checkbox" id="depthInvert"> Invert (reverse light ↔ dark)</label>
    </div>
    <div class="depth dfm-grey" id="depthBox">
      <p class="eyebrow">Base surface</p>
      <div class="ab card el1"><div class="card-body">
        <span class="eyebrow">Layer 1</span>
        <div class="ab card el2"><div class="card-body">
          <span class="eyebrow">Layer 2</span>
          <div class="ab card el3"><div class="card-body">
            <span class="eyebrow">Layer 3</span>
            <div class="ab card el4"><div class="card-body">
              <span class="eyebrow">Layer 4</span>
              <div class="ab card el5"><div class="card-body">
                <span class="eyebrow">Layer 5</span>
                <div class="ab card el6"><div class="card-body">
                  <span class="eyebrow">Layer 6</span>
                  <p>Lightness and shadow together read as height.</p>
                  <button class="ab btn primary btn-sm">Top action</button>
                </div></div>
              </div></div>
            </div></div>
          </div></div>
        </div></div>
      </div></div>
    </div>
  </section>
<section>
    <h2 class="sec">Card modifiers — family &amp; fill style (invert, soft, tinted)</h2>
    <div class="panel">
      <div class="hovmodes" id="cFam" role="radiogroup" aria-label="Family">
        <label><input type="radio" name="cfam" value="brand" checked=""> Brand</label>
        <label><input type="radio" name="cfam" value="grey"> Colour-grey</label>
        <label><input type="radio" name="cfam" value="gray"> Pure grey</label>
      </div>
      <div class="hovmodes" id="cStyle" role="radiogroup" aria-label="Fill style">
        <label><input type="radio" name="cstyle" value="tinted" checked=""> Tinted</label>
        <label><input type="radio" name="cstyle" value="invert"> Invert</label>
        <label><input type="radio" name="cstyle" value="soft"> Soft</label>
      </div>
      <div class="cardgrid cfm-gray cst-tinted" id="cardWrap">
        <div class="ab card">
          <div class="card-header">Header</div>
          <div class="card-body"><h3 class="card-title">Themed card</h3><p class="card-text">The accent follows the family; the fill style switches the whole look.</p></div>
          <div class="card-footer">Footer</div>
        </div>
        <div class="ab card">
          <div class="card-body"><h3 class="card-title">No header</h3><p class="card-text">Border and tint both come from the one accent var.</p><a class="card-link" href="#" onclick="return false">Action</a></div>
        </div>
        <div class="ab card">
          <div class="card-header">Status</div>
          <div class="card-body"><h3 class="card-title">Try invert</h3><p class="card-text">Invert fills the card solid; tinted and soft stay light.</p></div>
        </div>
      </div>
    </div>
  </section>



<div class="card-doc">
    <div class="swrow">
      <div class="ab card info"><div class="card-header">Header</div><div class="card-body"><div class="card-title">Info card</div><p class="card-text">Accent tints border + header.</p></div></div>
      <div class="ab card positive invert"><div class="card-body"><div class="card-title">Invert</div><p class="card-text">Solid accent fill.</p></div></div>
      <div class="ab card negative"><div class="card-body"><div class="card-title">Negative</div><p class="card-text">One accent var drives it all.</p></div></div>
    </div>
    <p class="note">Slots</p>
    <div class="classlist"><span>card-header</span><span>card-body</span><span>card-footer</span><span>card-title</span><span>card-subtitle</span><span>card-text</span><span>card-link</span><span>card-img-top/-bottom/-overlay</span></div>
    <p class="note">Modifiers</p>
    <div class="classlist"><span>primary/secondary/positive/negative/comment/info</span><span>fam-* + sh-*</span><span>invert</span><span>soft</span><span>flat</span><span>raised</span><span>square</span><span>with-icon</span><span>hover-animate</span><span>elevated</span></div>
  </div>
## 2.0 Buttons

<section id="buttons">
    <h2 class="sec" data-css-index="3">7 · Buttons <code>.ab.btn</code><button type="button" class="sendcss">⧉ Send to CSS</button></h2>
    <div class="card-doc">
<div class="panel">
      <div class="btnrow">
        <button class="ab btn primary">Primary</button>
        <button class="ab btn secondary">Secondary</button>
        <button class="ab btn positive">Positive</button>
        <button class="ab btn negative">Negative</button>
        <button class="ab btn comment">Comment</button>
        <button class="ab btn info">Info</button>
      </div>
      <div class="btnrow">
        <button class="ab btn primary outline">Primary</button>
        <button class="ab btn secondary outline">Secondary</button>
        <button class="ab btn positive outline">Positive</button>
        <button class="ab btn negative outline">Negative</button>
        <button class="ab btn comment outline">Comment</button>
        <button class="ab btn info outline">Info</button>
      </div>
      <div class="btnrow">
        <button class="ab btn primary btn-sm">Small</button>
        <button class="ab btn primary">Default</button>
        <button class="ab btn primary btn-lg">Large</button>
        <button class="ab btn link">Link</button>
        <button class="ab btn primary" disabled="">Disabled</button>
      </div>
    </div>
<h3 class="sub">Themed buttons</h3>
<div class="panel">
      <div class="hovmodes" id="hovmodes" role="radiogroup" aria-label="Hover mode">
        <label><input type="radio" name="hovmode" value="flip" checked=""> Inverse flip</label>
        <label><input type="radio" name="hovmode" value="shade"> Shaded</label>
        <label><input type="radio" name="hovmode" value="outline"> Outline</label>
        <label><input type="radio" name="hovmode" value="ghost"> Ghost</label>
      </div>
      <div id="themeWrap" class="hv-flip">
      <p style="margin:0 0 9px;color:var(--ink-soft);font-size:.82rem;font-weight:600;">Brand — saturation fixed (hover to preview the mode)</p>
      <div class="btnrow">
        <button class="ab btn btn-sm fam-brand sh-200">200</button>
        <button class="ab btn btn-sm fam-brand sh-300">300</button>
        <button class="ab btn btn-sm fam-brand sh-400">400</button>
        <button class="ab btn btn-sm fam-brand sh-500">500</button>
        <button class="ab btn btn-sm fam-brand sh-600">600</button>
        <button class="ab btn btn-sm fam-brand sh-700">700</button>
        <button class="ab btn btn-sm fam-brand sh-800">800</button>
        <button class="ab btn btn-sm fam-brand sh-900">900</button>
      </div>
      <p style="margin:16px 0 9px;color:var(--ink-soft);font-size:.82rem;font-weight:600;">Blue-grey — saturation dialled almost out</p>
      <div class="btnrow">
        <button class="ab btn btn-sm fam-grey sh-200">200</button>
        <button class="ab btn btn-sm fam-grey sh-300">300</button>
        <button class="ab btn btn-sm fam-grey sh-400">400</button>
        <button class="ab btn btn-sm fam-grey sh-500">500</button>
        <button class="ab btn btn-sm fam-grey sh-600">600</button>
        <button class="ab btn btn-sm fam-grey sh-700">700</button>
        <button class="ab btn btn-sm fam-grey sh-800">800</button>
        <button class="ab btn btn-sm fam-grey sh-900">900</button>
      </div>
      <p style="margin:16px 0 9px;color:var(--ink-soft);font-size:.82rem;font-weight:600;">Pure grey — true neutral (0% saturation)</p>
      <div class="btnrow">
        <button class="ab btn btn-sm fam-gray sh-200">200</button>
        <button class="ab btn btn-sm fam-gray sh-300">300</button>
        <button class="ab btn btn-sm fam-gray sh-400">400</button>
        <button class="ab btn btn-sm fam-gray sh-500">500</button>
        <button class="ab btn btn-sm fam-gray sh-600">600</button>
        <button class="ab btn btn-sm fam-gray sh-700">700</button>
        <button class="ab btn btn-sm fam-gray sh-800">800</button>
        <button class="ab btn btn-sm fam-gray sh-900">900</button>
      </div>
      </div>
    </div>
<h3 class="sub">Modifiers</h3>
<div class="panel">
      <div class="hovmodes" id="modFam" role="radiogroup" aria-label="Family">
        <label><input type="radio" name="modfam" value="brand" checked=""> Brand</label>
        <label><input type="radio" name="modfam" value="grey"> Colour-grey</label>
        <label><input type="radio" name="modfam" value="gray"> Pure grey</label>
      </div>
      <div class="hovmodes" id="modHov" role="radiogroup" aria-label="Hover mode">
        <label><input type="radio" name="modhov" value="flip" checked=""> Inverse flip</label>
        <label><input type="radio" name="modhov" value="shade"> Shaded</label>
        <label><input type="radio" name="modhov" value="outline"> Outline</label>
        <label><input type="radio" name="modhov" value="ghost"> Ghost</label>
      </div>
      <div id="modWrap" class="fm-brand hv-flip">
        <div class="btnrow">
          <button class="ab btn sh-600">Default</button>
          <button class="ab btn sh-600 pill">Pill</button>
          <button class="ab btn sh-600 square">Square</button>
          <button class="ab btn sh-600 icon" aria-label="Star">★</button>
          <button class="ab btn sh-600 lift">Lift</button>
          <button class="ab btn sh-600 loading">Loading</button>
        </div>
        <div class="btnrow" style="margin-top:12px;">
          <button class="ab btn sh-600 block pill">Block (full width)</button>
        </div>
      </div>
    </div>
<p class="note">Variants</p>
    <div class="classlist"><span>primary</span><span>secondary</span><span>positive</span><span>negative</span><span>comment</span><span>info</span></div>
    <p class="note">Hover modes (pick one)</p>
    <div class="classlist"><span>(flip — default)</span><span>shaded-hover</span><span>outline</span><span>ghost</span></div>
    <p class="note">Modifiers</p>
    <div class="classlist"><span>soft</span><span>pill</span><span>square</span><span>block</span><span>icon</span><span>circle</span><span>lift</span><span>loading</span><span>btn-sm</span><span>btn-lg</span><span>link</span></div>
    <p class="note">Themed instead of semantic</p>
    <div class="classlist"><span>fam-brand</span><span>fam-grey</span><span>fam-gray</span><span>sh-50 … sh-950</span></div>
    </div>
  </section>

## 3.0 Callouts

<div class="card-doc">
<div class="panel">
      <div class="hovmodes" id="coFam" role="radiogroup" aria-label="Family">
        <label><input type="radio" name="cofam" value="brand" checked=""> Brand</label>
        <label><input type="radio" name="cofam" value="grey"> Colour-grey</label>
        <label><input type="radio" name="cofam" value="gray"> Pure grey</label>
      </div>
      <div class="hovmodes" id="coStyle" role="radiogroup" aria-label="Fill style">
        <label><input type="radio" name="costyle" value="tinted" checked=""> Tinted</label>
        <label><input type="radio" name="costyle" value="soft"> Soft</label>
        <label><input type="radio" name="costyle" value="invert"> Invert</label>
      </div>
      <div id="calloutWrap" class="cofm-brand cost-tinted" style="display:grid;gap:12px;">
        <div class="ab callout"><div class="callout-header">Themed callout</div><p>Accent comes from the family control; the style switches tinted / soft / invert.</p></div>
        <div class="ab callout with-icon"><span class="callout-icon"><svg class="ic"><use href="#ic-search"></use></svg></span><div class="callout-content"><div class="callout-header">With icon</div><p>The icon tints to match the bar.</p></div></div>
      </div>
    </div>
    <p style="margin:14px 0 8px;color:var(--ink-soft);font-size:.82rem;font-weight:600;">Semantic &amp; functional (follow the semantic formula):</p>
    <div style="display:grid;gap:12px;">
      <div class="ab callout positive"><div class="callout-header">Positive / advice / do</div><p>Green family from the formula.</p></div>
      <div class="ab callout neutral"><div class="callout-header">Neutral — amber</div><p>Neutral is amber now, derived from the same formula.</p></div>
      <div class="ab callout negative"><div class="callout-header">Negative / warning / dont</div><p>Red family.</p></div>
      <div class="ab callout comment soft"><div class="callout-header">Comment (soft)</div><p>Stronger tint via <code>soft</code>.</p></div>
      <div class="ab callout info invert"><div class="callout-header">Info (invert)</div><p>Solid accent fill.</p></div>
    </div>
<p class="note">Slots &amp; modifiers</p>
    <div class="classlist"><span>callout-header(.h2–.h6)</span><span>callout-content</span><span>callout-icon</span><span>with-icon</span><span>primary/positive/negative/comment/info</span><span>advice/action/do/dont/warning/starting/feedback-*</span><span>fam-*+sh-*</span><span>soft</span><span>invert</span></div>
    </div>
<section id="callouts">
    <h2 class="sec" data-css-index="5">9 · Callouts <code>.ab.callout</code><button type="button" class="sendcss">⧉ Send to CSS</button></h2>
    <div class="card-doc">
<div class="panel">
      <div class="hovmodes" id="coFam" role="radiogroup" aria-label="Family">
        <label><input type="radio" name="cofam" value="brand" checked=""> Brand</label>
        <label><input type="radio" name="cofam" value="grey"> Colour-grey</label>
        <label><input type="radio" name="cofam" value="gray"> Pure grey</label>
      </div>
      <div class="hovmodes" id="coStyle" role="radiogroup" aria-label="Fill style">
        <label><input type="radio" name="costyle" value="tinted" checked=""> Tinted</label>
        <label><input type="radio" name="costyle" value="soft"> Soft</label>
        <label><input type="radio" name="costyle" value="invert"> Invert</label>
      </div>
      <div id="calloutWrap" class="cofm-brand cost-tinted" style="display:grid;gap:12px;">
        <div class="ab callout"><div class="callout-header">Themed callout</div><p>Accent comes from the family control; the style switches tinted / soft / invert.</p></div>
        <div class="ab callout with-icon"><span class="callout-icon"><svg class="ic"><use href="#ic-search"></use></svg></span><div class="callout-content"><div class="callout-header">With icon</div><p>The icon tints to match the bar.</p></div></div>
      </div>
    </div>
    <p style="margin:14px 0 8px;color:var(--ink-soft);font-size:.82rem;font-weight:600;">Semantic &amp; functional (follow the semantic formula):</p>
    <div style="display:grid;gap:12px;">
      <div class="ab callout positive"><div class="callout-header">Positive / advice / do</div><p>Green family from the formula.</p></div>
      <div class="ab callout neutral"><div class="callout-header">Neutral — amber</div><p>Neutral is amber now, derived from the same formula.</p></div>
      <div class="ab callout negative"><div class="callout-header">Negative / warning / dont</div><p>Red family.</p></div>
      <div class="ab callout comment soft"><div class="callout-header">Comment (soft)</div><p>Stronger tint via <code>soft</code>.</p></div>
      <div class="ab callout info invert"><div class="callout-header">Info (invert)</div><p>Solid accent fill.</p></div>
    </div>
<p class="note">Slots &amp; modifiers</p>
    <div class="classlist"><span>callout-header(.h2–.h6)</span><span>callout-content</span><span>callout-icon</span><span>with-icon</span><span>primary/positive/negative/comment/info</span><span>advice/action/do/dont/warning/starting/feedback-*</span><span>fam-*+sh-*</span><span>soft</span><span>invert</span></div>
    </div>
  </section>

<div class="card-doc">
    <div style="display:grid;gap:10px">
      <div class="ab callout info with-icon"><span class="callout-icon"><svg class="ic"><use href="#ic-criticality"></use></svg></span><div class="callout-content"><div class="callout-header">Info</div><p>Left bar, tint, header &amp; icon from one accent.</p></div></div>
      <div class="ab callout neutral"><div class="callout-header">Neutral — amber</div><p>Derived from the Start colour.</p></div>
      <div class="ab callout positive"><div class="callout-header">Positive / advice / do</div><p>Functional aliases map to the semantics.</p></div>
    </div>
    <p class="note">Slots &amp; modifiers</p>
    <div class="classlist"><span>callout-header(.h2–.h6)</span><span>callout-content</span><span>callout-icon</span><span>with-icon</span><span>primary/positive/negative/comment/info</span><span>advice/action/do/dont/warning/starting/feedback-*</span><span>fam-*+sh-*</span><span>soft</span><span>invert</span></div>
  </div>

## 4.0 Accordions
