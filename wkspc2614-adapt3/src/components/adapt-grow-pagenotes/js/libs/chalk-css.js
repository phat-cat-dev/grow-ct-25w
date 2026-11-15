// Vendored chalk-patterns stylesheet (chalk-theme.css + chalk-labels.css),
// bundled as a string so the overlay can inject it once at runtime (the Adapt
// LESS build only globs *.less). Do not hand-edit; regenerate from the source.
export default `/* chalk-theme.css + tokenised/chalk-labels.css */
/* chalk-theme.css - connects chalk pattern SVGs to the host theme's colours.

   Load once on any page with inline chalk SVGs, including the original files in
   this folder. It needs no markup changes. Each colour resolves in this order:
   per-diagram override -> AB theme token -> older asset token -> fallback, so the
   drawings follow theme switches and light/dark mode automatically.

   Override on any ancestor or on the svg itself:
     --chalk-color         strokes
     --chalk-arrow-color   arrowheads (defaults to the stroke colour)
     --chalk-label-color   label text
     --chalk-label-bg      label chip fill
     --chalk-label-border  label chip border
     --chalk-label-font    label typeface
     --chalk-stage-strength  how much of each accent stage colours keep (default 72%)

   Attributes:
     data-chalk-tone="accent|accent-2|accent-3|accent-4|ink|muted|positive|negative|neutral|info|comment"
     data-chalk-palette="harmony"   gives each cycle stage its own theme accent
     data-chalk-label-tone="match"  colours label text to match its stage or tone
     data-chalk-label-style="chip"  gives HTML labels a visible box
     data-chalk-font="hand"         uses a handwritten system font for labels

   An SVG loaded through <img> cannot read the page's CSS variables, so it uses
   the fallbacks below (which still follow the viewer's light/dark setting). */

:where(svg.edu-svg, .chalk-stage) {
  --chalk-fb-accent: #247c78;
  --chalk-fb-accent-2: #8a5a13;
  --chalk-fb-accent-3: #7a4aa8;
  --chalk-fb-accent-4: #b0405f;
  --chalk-fb-ink: #23353c;
  --chalk-fb-muted: #52666d;
  --chalk-fb-surface: #fff;
  --chalk-fb-line: #bbd3cf;
  --chalk-fb-positive: #2c7a54;
  --chalk-fb-negative: #a8392c;
  --chalk-fb-neutral: #8a5a13;
  --chalk-fb-info: #2b6c96;
  --chalk-fb-comment: #6a44a0;

  --chalk-stroke: var(--chalk-color, var(--accent, var(--chalk-fb-accent)));
  --chalk-arrow: var(--chalk-arrow-color, var(--chalk-stroke));
  --chalk-ink: var(--chalk-label-color, var(--text, var(--ink, var(--chalk-fb-ink))));
  --chalk-box-bg: var(--chalk-label-bg, var(--surface-1, var(--chalk-fb-surface)));
  --chalk-box-border: var(--chalk-label-border, var(--border-strong, var(--line, var(--chalk-fb-line))));

  /* Theme accents vary a lot in contrast, so stage colours lean towards the text
     colour. That raises contrast in both light and dark. Set --chalk-stage-strength
     to 100% to use the raw accents. */
  --chalk-stage-1: color-mix(in srgb, var(--accent, var(--chalk-fb-accent)) var(--chalk-stage-strength, 72%), var(--chalk-ink));
  --chalk-stage-2: color-mix(in srgb, var(--accent-2, var(--chalk-fb-accent-2)) var(--chalk-stage-strength, 72%), var(--chalk-ink));
  --chalk-stage-3: color-mix(in srgb, var(--accent-3, var(--chalk-fb-accent-3)) var(--chalk-stage-strength, 72%), var(--chalk-ink));
  --chalk-stage-4: color-mix(in srgb, var(--accent-4, var(--chalk-fb-accent-4)) var(--chalk-stage-strength, 72%), var(--chalk-ink));
  --chalk-stage-5: color-mix(in srgb, var(--comment, var(--chalk-fb-comment)) var(--chalk-stage-strength, 72%), var(--chalk-ink));
}
@media (prefers-color-scheme: dark) {
  :where(svg.edu-svg, .chalk-stage) {
    --chalk-fb-accent: #8bddcf;
    --chalk-fb-accent-2: #e5b567;
    --chalk-fb-accent-3: #c5a3ea;
    --chalk-fb-accent-4: #f0a0b8;
    --chalk-fb-ink: #e3f0ee;
    --chalk-fb-muted: #a9bdbb;
    --chalk-fb-surface: #1d3034;
    --chalk-fb-line: #496a6e;
    --chalk-fb-positive: #7fd6a6;
    --chalk-fb-negative: #f0a097;
    --chalk-fb-neutral: #e5b567;
    --chalk-fb-info: #8cc5ea;
    --chalk-fb-comment: #c5a3ea;
  }
}

/* The svg. prefix outranks the .edu-svg rule embedded in each SVG file. Strokes
   paint in currentColor, so setting color also recolours the chalk drop shadow. */
svg.edu-svg { color: var(--chalk-stroke); }
svg.edu-svg :where(.edu-stroke.edu-arrow) { color: var(--chalk-arrow); }

[data-chalk-tone="accent"]   { --chalk-color: var(--accent, var(--chalk-fb-accent)); }
[data-chalk-tone="accent-2"] { --chalk-color: var(--accent-2, var(--chalk-fb-accent-2)); }
[data-chalk-tone="accent-3"] { --chalk-color: var(--accent-3, var(--chalk-fb-accent-3)); }
[data-chalk-tone="accent-4"] { --chalk-color: var(--accent-4, var(--chalk-fb-accent-4)); }
[data-chalk-tone="ink"]      { --chalk-color: var(--text, var(--ink, var(--chalk-fb-ink))); }
[data-chalk-tone="muted"]    { --chalk-color: var(--text-soft, var(--chalk-fb-muted)); }
[data-chalk-tone="positive"] { --chalk-color: var(--positive, var(--chalk-fb-positive)); }
[data-chalk-tone="negative"] { --chalk-color: var(--negative, var(--chalk-fb-negative)); }
[data-chalk-tone="neutral"]  { --chalk-color: var(--neutral, var(--chalk-fb-neutral)); }
[data-chalk-tone="info"]     { --chalk-color: var(--info, var(--chalk-fb-info)); }
[data-chalk-tone="comment"]  { --chalk-color: var(--comment, var(--chalk-fb-comment)); }

[data-chalk-palette="harmony"] .edu-stroke[data-chalk-stage="1"] { color: var(--chalk-stage-1); }
[data-chalk-palette="harmony"] .edu-stroke[data-chalk-stage="2"] { color: var(--chalk-stage-2); }
[data-chalk-palette="harmony"] .edu-stroke[data-chalk-stage="3"] { color: var(--chalk-stage-3); }
[data-chalk-palette="harmony"] .edu-stroke[data-chalk-stage="4"] { color: var(--chalk-stage-4); }
[data-chalk-palette="harmony"] .edu-stroke[data-chalk-stage="5"] { color: var(--chalk-stage-5); }


/* Generated by build-tokenised.cjs. Edit LABEL_CSS there, not this file.
   Contains the chalk stroke animation, label layout and write-on timing.
   Load it with ../chalk-theme.css. */
.edu-svg{width:100%;height:auto;display:block;color:var(--accent,#65d5ca);overflow:visible}
.edu-stroke{fill:none;stroke:currentColor;stroke-width:2.7;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1;stroke-dashoffset:0}
.edu-stroke.edu-arrow{stroke-width:2}
.edu-running .edu-stroke{animation-name:var(--edu-animation);animation-duration:calc(var(--edu-duration,4s) / var(--edu-speed,1) / var(--edu-local-speed,1));animation-timing-function:linear;animation-fill-mode:both;animation-iteration-count:var(--edu-iterations,1)}
.edu-paused .edu-stroke{animation-play-state:paused}
.edu-no-arrows .edu-arrow{display:none}
.edu-chalk .edu-stroke{stroke-width:3.2;filter:drop-shadow(.5px .3px 0 currentColor)}
@keyframes edu-draw-1-0{0%,0%{stroke-dashoffset:1}100%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-2-0{0%,0%{stroke-dashoffset:1}50%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-2-1{0%,50%{stroke-dashoffset:1}100%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-3-0{0%,0%{stroke-dashoffset:1}33.333333333333336%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-3-1{0%,33.333333333333336%{stroke-dashoffset:1}66.66666666666667%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-3-2{0%,66.66666666666667%{stroke-dashoffset:1}100%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-4-0{0%,0%{stroke-dashoffset:1}25%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-4-1{0%,25%{stroke-dashoffset:1}50%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-4-2{0%,50%{stroke-dashoffset:1}75%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-4-3{0%,75%{stroke-dashoffset:1}100%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-6-0{0%,0%{stroke-dashoffset:1}16.666666666666668%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-6-1{0%,16.666666666666668%{stroke-dashoffset:1}33.333333333333336%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-6-2{0%,33.333333333333336%{stroke-dashoffset:1}50%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-6-3{0%,50%{stroke-dashoffset:1}66.66666666666667%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-6-4{0%,66.66666666666667%{stroke-dashoffset:1}83.33333333333333%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-6-5{0%,83.33333333333333%{stroke-dashoffset:1}100%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-8-0{0%,0%{stroke-dashoffset:1}12.5%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-8-1{0%,12.5%{stroke-dashoffset:1}25%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-8-2{0%,25%{stroke-dashoffset:1}37.5%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-8-3{0%,37.5%{stroke-dashoffset:1}50%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-8-4{0%,50%{stroke-dashoffset:1}62.5%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-8-5{0%,62.5%{stroke-dashoffset:1}75%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-8-6{0%,75%{stroke-dashoffset:1}87.5%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-8-7{0%,87.5%{stroke-dashoffset:1}100%,100%{stroke-dashoffset:0}}
@media(prefers-reduced-motion:reduce){.edu-running .edu-stroke{animation:none!important;stroke-dashoffset:0}}
.chalk-stage{display:block;margin:0;color:var(--chalk-ink)}
.chalk-canvas{position:relative;display:block;container-type:inline-size}
.chalk-details{display:grid;gap:.35rem;margin:.6rem 0 0;padding:0;list-style:none;font-family:var(--chalk-label-font,var(--font-ui,var(--font-sans,system-ui,-apple-system,"Segoe UI",sans-serif)));font-size:.9rem;line-height:1.35}
.chalk-details:not(:has(.chalk-detail-text:not(:empty))){display:none}
.chalk-detail:has(.chalk-detail-text:empty){display:none}
.chalk-detail{padding-inline-start:.5rem;border-inline-start:3px solid var(--chalk-label-stage,var(--chalk-stroke))}
.chalk-detail-term{font-weight:600}
.chalk-label{font-family:var(--chalk-label-font,var(--font-ui,var(--font-sans,system-ui,-apple-system,"Segoe UI",sans-serif)));font-weight:600}
[data-chalk-font="hand"] .chalk-label{--chalk-label-font:"Segoe Print","Bradley Hand","Chalkboard SE","Comic Sans MS",cursive}
text.chalk-label{fill:var(--chalk-ink);font-size:12px;stroke:none}
div.chalk-label{position:absolute;left:calc(var(--x) / 300 * 100%);top:calc(var(--y) / 160 * 100%);width:max-content;max-width:calc(var(--w) / 300 * 100%);box-sizing:border-box;color:var(--chalk-ink);font-size:clamp(.72rem,4cqi,1.15rem);line-height:1.15;overflow-wrap:break-word;transform:translate(var(--tx,0),var(--ty,0))}
div.chalk-label:empty{display:none}
div.chalk-label[data-align="start"]{text-align:start}
div.chalk-label[data-align="middle"]{--tx:-50%;text-align:center}
div.chalk-label[data-align="end"]{--tx:-100%;text-align:end}
div.chalk-label[data-valign="middle"]{--ty:-50%}
div.chalk-label[data-valign="bottom"]{--ty:-100%}
[data-chalk-label-style="chip"] div.chalk-label{padding:.15em .45em;background:var(--chalk-box-bg);border:1px solid var(--chalk-box-border);border-radius:.4em}
[data-chalk-palette="harmony"] :is(.chalk-label,.chalk-detail)[data-chalk-stage="1"]{--chalk-label-stage:var(--chalk-stage-1)}[data-chalk-palette="harmony"] :is(.chalk-label,.chalk-detail)[data-chalk-stage="2"]{--chalk-label-stage:var(--chalk-stage-2)}[data-chalk-palette="harmony"] :is(.chalk-label,.chalk-detail)[data-chalk-stage="3"]{--chalk-label-stage:var(--chalk-stage-3)}[data-chalk-palette="harmony"] :is(.chalk-label,.chalk-detail)[data-chalk-stage="4"]{--chalk-label-stage:var(--chalk-stage-4)}[data-chalk-palette="harmony"] :is(.chalk-label,.chalk-detail)[data-chalk-stage="5"]{--chalk-label-stage:var(--chalk-stage-5)}
[data-chalk-label-tone="match"] text.chalk-label{fill:color-mix(in srgb,var(--chalk-label-stage,var(--chalk-stroke)) 60%,var(--chalk-ink))}
[data-chalk-label-tone="match"] div.chalk-label{color:color-mix(in srgb,var(--chalk-label-stage,var(--chalk-stroke)) 60%,var(--chalk-ink))}
[data-chalk-label-style="chip"] div.chalk-label[data-chalk-stage]{border-color:var(--chalk-label-stage,var(--chalk-box-border))}
.edu-running :is(.chalk-label,.chalk-detail){animation-name:var(--chalk-write);animation-duration:calc(var(--edu-duration,4s) / var(--edu-speed,1) / var(--edu-local-speed,1));animation-timing-function:linear;animation-fill-mode:both;animation-iteration-count:var(--edu-iterations,1)}
.edu-paused :is(.chalk-label,.chalk-detail){animation-play-state:paused}
@media(prefers-reduced-motion:reduce){.edu-running :is(.chalk-label,.chalk-detail){animation:none!important}}
:is(.no-motion,[data-tm-no-motion="true"]) .edu-running :is(.edu-stroke,.chalk-label,.chalk-detail){animation:none!important}
@keyframes edu-draw-10-0{0%,0%{stroke-dashoffset:1}10%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-10-1{0%,10%{stroke-dashoffset:1}20%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-10-2{0%,20%{stroke-dashoffset:1}30%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-10-3{0%,30%{stroke-dashoffset:1}40%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-10-4{0%,40%{stroke-dashoffset:1}50%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-10-5{0%,50%{stroke-dashoffset:1}60%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-10-6{0%,60%{stroke-dashoffset:1}70%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-10-7{0%,70%{stroke-dashoffset:1}80%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-10-8{0%,80%{stroke-dashoffset:1}90%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-10-9{0%,90%{stroke-dashoffset:1}100%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-7-0{0%,0%{stroke-dashoffset:1}14.29%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-7-1{0%,14.29%{stroke-dashoffset:1}28.57%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-7-2{0%,28.57%{stroke-dashoffset:1}42.86%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-7-3{0%,42.86%{stroke-dashoffset:1}57.14%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-7-4{0%,57.14%{stroke-dashoffset:1}71.43%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-7-5{0%,71.43%{stroke-dashoffset:1}85.71%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-7-6{0%,85.71%{stroke-dashoffset:1}100%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-0{0%,0%{stroke-dashoffset:1}7.69%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-1{0%,7.69%{stroke-dashoffset:1}15.38%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-2{0%,15.38%{stroke-dashoffset:1}23.08%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-3{0%,23.08%{stroke-dashoffset:1}30.77%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-4{0%,30.77%{stroke-dashoffset:1}38.46%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-5{0%,38.46%{stroke-dashoffset:1}46.15%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-6{0%,46.15%{stroke-dashoffset:1}53.85%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-7{0%,53.85%{stroke-dashoffset:1}61.54%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-8{0%,61.54%{stroke-dashoffset:1}69.23%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-9{0%,69.23%{stroke-dashoffset:1}76.92%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-10{0%,76.92%{stroke-dashoffset:1}84.62%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-11{0%,84.62%{stroke-dashoffset:1}92.31%,100%{stroke-dashoffset:0}}
@keyframes edu-draw-13-12{0%,92.31%{stroke-dashoffset:1}100%,100%{stroke-dashoffset:0}}
@keyframes chalk-write-0-1000{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}10%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-1167{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}11.67%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-1250{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}12.5%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-1400{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}14%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-1429{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}14.29%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-1500{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}15%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-1667{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}16.67%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-1750{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}17.5%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-2000{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}20%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-2500{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}25%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-750{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}7.5%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-0-769{0%,0%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}7.69%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-1000-4000{0%,10%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}40%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-1167-2167{0%,11.67%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}21.67%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-1167-2333{0%,11.67%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}23.33%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-1400-2800{0%,14%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}28%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-1750-2500{0%,17.5%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}25%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-1750-3250{0%,17.5%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}32.5%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-1750-3500{0%,17.5%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}35%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-2000-3000{0%,20%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}30%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-2000-4000{0%,20%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}40%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-2308-3077{0%,23.08%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}30.77%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-2333-3333{0%,23.33%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}33.33%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-2333-3500{0%,23.33%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}35%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-2500-3500{0%,25%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}35%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-2500-3750{0%,25%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}37.5%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-2800-4200{0%,28%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}42%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-3000-4000{0%,30%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}40%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-3000-7000{0%,30%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}70%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-3250-5000{0%,32.5%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}50%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-3333-5000{0%,33.33%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}50%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-3500-4667{0%,35%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}46.67%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-3500-5000{0%,35%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}50%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-3500-5250{0%,35%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}52.5%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-4000-5000{0%,40%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}50%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-4000-6000{0%,40%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}60%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-4200-5600{0%,42%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}56%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-4286-5714{0%,42.86%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}57.14%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-4615-5385{0%,46.15%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}53.85%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-4667-5833{0%,46.67%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}58.33%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-5000-10000{0%,50%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}100%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-5000-5833{0%,50%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}58.33%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-5000-6250{0%,50%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}62.5%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-5000-7500{0%,50%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}75%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-5250-7000{0%,52.5%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}70%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-5600-7000{0%,56%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}70%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-5833-6667{0%,58.33%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}66.67%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-5833-7000{0%,58.33%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}70%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-6000-7000{0%,60%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}70%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-6000-7500{0%,60%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}75%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-6667-8333{0%,66.67%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}83.33%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-6750-7500{0%,67.5%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}75%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-6923-7692{0%,69.23%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}76.92%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-7000-10000{0%,70%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}100%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-7500-10000{0%,75%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}100%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-7500-8750{0%,75%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}87.5%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-8000-9000{0%,80%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}90%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-8333-10000{0%,83.33%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}100%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-8333-9167{0%,83.33%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}91.67%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-8500-10000{0%,85%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}100%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-8571-10000{0%,85.71%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}100%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-8750-10000{0%,87.5%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}100%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-9000-10000{0%,90%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}100%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-9167-10000{0%,91.67%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}100%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
@keyframes chalk-write-9231-10000{0%,92.31%{opacity:0;clip-path:inset(-20% 100% -20% -20%)}100%,100%{opacity:1;clip-path:inset(-20% -20% -20% -20%)}}
`;
