# Scroll scenes: style and transition structure

How the component is built, read two ways.

- **Meta** is the rule: which token or mechanism controls a thing and where it lives.
- **Value** is what that rule gives today.

Change the meta layer (tokens and attributes) and every value follows. The
files mentioned here are `scroll-scenes.css`, `scroll-scenes.js` (both
unchanged), `scroll-scenes.backgrounds.css` (new) and
`scene-content.template.yaml` (new).

---

## 1. Anatomy

```
main.scroll-scenes                        host. Tokens live here. mount() target.
├─ nav.scene-nav                          flex row, wraps
│  ├─ button[data-scroll-to="i"]          one per scene. aria-current="step" on the active one
│  ├─ progress[data-scroll-progress]      pushed to the right edge by auto margin
│  └─ span.scene-status                   "Scene 2 of 4", aria-live polite
└─ div[data-scroll-viewport]              THE SCROLLER. tabindex 0, role region
   └─ section[data-scroll-scene]          one per scene. Holds the background
      ├─ ::before                         colour field        (z-index -1)
      ├─ ::after                          pattern layer       (z-index -1, above ::before)
      └─ div[data-scene-content]          the animated block. JS writes its inline style
         ├─ p.scene-number                eyebrow, "01 / OBSERVE"
         ├─ h2                            heading, lines split by <br>
         └─ p.scene-copy                  body
```

Your component has no cards. `[data-scene-content]` is the card: it is the one
element the JavaScript fades, scales, blurs and slides, so every card
transition below targets it.

Each part of the YAML template lands on one of these hooks. `field_map` in
`scene-content.template.yaml` lists the exact mapping.

---

## 2. Typography

| Role | Meta (rule) | Value now | Where set |
|---|---|---|---|
| Base family | `--font-ui`, falling back to `system-ui, sans-serif` | system UI font | `.scroll-scenes` |
| Base size and leading | `font: 1rem/1.6` | 16px, line height 1.6 | `.scroll-scenes` |
| Nav buttons | inherit from host | 1rem, normal weight | `.scroll-scenes button` |
| Active nav button | `--scene-accent`, weight 700, underline offset | accent colour, bold, `.4em` offset | `button[aria-current="step"]` |
| Eyebrow | monospace, tracked, accent colour | `.85rem ui-monospace`, `letter-spacing .15em` | `.scene-number` |
| Heading | fluid size, tight leading, tight tracking | `clamp(2rem, 6vw, 5rem)`, line height 1.06, `letter-spacing -.045em` | `.scroll-scenes h2` |
| Body | fluid size, capped measure | `clamp(1rem, 2vw, 1.25rem)`, `max-inline-size 46ch` | `.scene-copy` |
| Status text | small | `.8rem` | `.scene-status` |

Notes

- The heading sets no `font-family` or weight. It inherits the host family and
  uses the browser's default bold. To change the heading face for one theme,
  set `--font-ui` on an ancestor.
- Tracking is in `em`, so it scales with the fluid size.
- Heading lines in the YAML template are capped at 20 characters. At the
  largest size (5rem) the heading sits in the 48rem content width, and 20
  characters is about the most that fits on one line.

---

## 3. Spacing and alignment

| What | Meta | Value now |
|---|---|---|
| Scene padding | fluid, all four sides | `clamp(1.5rem, 5vw, 5rem)` |
| Scene height | fills the viewport | `min-block-size: 100%`, grows with content |
| Viewport height | fraction of the screen with floor and ceiling | `min(72svh, 48rem)`, never below `20rem` |
| Vertical alignment | grid, centred | `display: grid; align-items: center` |
| Horizontal alignment | content block pinned left | `max-inline-size: 48rem`, `transform-origin: left center` |
| Heading spacing | block margins | `margin-block: 1rem` |
| Nav spacing | flex gap and padding | gap `.5rem`, padding `.75rem 1rem`, buttons `.5rem .8rem` |
| Progress bar | fixed size, pushed right | `6rem` by `.4rem`, `margin-inline: auto .5rem` |
| Snap | start of each scene, soft | `scroll-snap-type: y proximity` |

The content block is left aligned and the default background puts its bright
spot at 85% across and 25% down. That places visual weight on the right to
balance the text on the left. The pattern backgrounds reuse the same focus
point through `--bg-focus-x` and `--bg-focus-y`, so they balance the layout in
the same way. Move the focus point and the whole composition shifts.

Everything uses `rem`, `ch`, `svh` and `clamp()`. Nothing is fixed in pixels
except the progress bar thickness (in `rem`) and hairline widths in the
patterns.

---

## 4. How backgrounds are made

### 4.1 The layer stack

```
[data-scroll-viewport]   background: var(--scene-paper)       the paper
 section                  position relative, isolation isolate  keeps z-index -1 inside the scene
  ::before                the colour field: gradients, opacity
  ::after                 the pattern: lines, dots, rings, masked
  [data-scene-content]    text, above both
```

`isolation: isolate` on the section is what lets the two pseudo elements sit
at `z-index: -1` without dropping behind the viewport paper.

### 4.2 The original recipe, step by step

`scroll-scenes.css` builds each background from two gradients on `::before`,
at 22% opacity:

1. **Glow.** `radial-gradient(ellipse at 85% 25%, colour, transparent 60%)`. An
   ellipse of the scene colour that fades out at 60% of its radius.
2. **Hairlines.** `repeating-linear-gradient(135deg, ...)`. One line of the
   scene colour, `.08rem` thick, every `8rem`, drawn at 135 degrees.
3. **Opacity.** The whole layer sits at `.22`, so the colour never fights the
   text.

The colour is `--scene-colour`, which changes per scene:

| Scene position | Slot | Value now |
|---|---|---|
| 1, 5, 9 ... | `--scene-colour-1` | `#44a8ba` (teal) |
| 2, 6, 10 ... | `--scene-colour-2` | `#dbaa45` (gold) |
| 3, 7, 11 ... | `--scene-colour-3` | `#ba7dbb` (purple) |
| 4, 8, 12 ... | `--scene-colour-4` | `#52a783` (green) |

The original file only coloured scenes 1 to 4. The new file cycles the four
slots, so a model with 5 to 7 stages keeps working. A single scene can pick a
slot with `data-scene-colour="3"`.

### 4.3 The colour formula

Every background reads these tokens. They are derived per scene, so you never
type a colour into a background.

| Token | Formula | Used for |
|---|---|---|
| `--bg-tint` | 16% scene colour in paper | soft washes |
| `--bg-tint-strong` | 34% scene colour in paper | corners, bands |
| `--bg-shade` | 14% accent in paper | counter tone, so a scene is never one colour |
| `--bg-line` | 60% scene colour, rest transparent | hairlines, dots, rings |
| `--bg-glow` | 50% scene colour, rest transparent | glows |
| `--bg-vignette` | 10% ink, rest transparent (30% black in `night`) | edge darkening |

All mixes use `color-mix(in oklch, ...)`. OKLCH keeps lightness steady when
you swap the hue, so a new scheme gets the same visual weight without
retuning.

> Assumption to check: I derived this formula from the tokens already in
> `scroll-scenes.css` (accent, ink, paper and the four scene colours). If the
> Cardiff Met colour formula uses different steps, change the six percentages
> in section 2 of `scroll-scenes.backgrounds.css`. Nothing else needs to move.

### 4.4 The library

Set `data-scene-bg` on the host for every scene, or on one section for that
scene alone. A scene value beats the host value. With no attribute you get the
original look.

| `data-scene-bg` | Layers | Character | Use when |
|---|---|---|---|
| `lines` | glow, diagonal hairlines | the original, rebuilt from tokens (pixel identical) | you want the house look |
| `aurora` | three overlapping glows, one in the accent | soft, atmospheric | opening and closing scenes |
| `mesh` | four corner washes | smooth, even | long copy |
| `dots` | diagonal wash, fading dot grid | light, technical | steps and procedures |
| `grid` | wash, squared-paper grid | precise | methods, checklists |
| `contour` | wash, concentric rings from the focus point | map-like, directional | exploring, comparing |
| `horizon` | tinted bands low in the scene, small low sun | calm, grounded | reflection and review |
| `spotlight` | pool of colour behind the text, edge vignette | focused | one strong statement |
| `weave` | wash, faint checker fading in from the left | textured | practice and drills |
| `wash` | one diagonal gradient from tint to shade | calmest | dense text |
| `plain` | nothing | none | page already visually busy |

Controls (set on the host, a scene or any ancestor; all optional):

| Token | Default | Effect |
|---|---|---|
| `--bg-opacity` | varies per background | strength of the colour field |
| `--bg-angle` | varies | direction of washes and hairlines |
| `--bg-gap` | `8rem` | spacing of `lines` |
| `--bg-gap-sm` | varies | cell size of `dots`, `grid`, `weave` and ring spacing in `contour` |
| `--bg-line-width` | `.08rem` | thickness of `lines` |
| `--bg-dot` | `1.5px` | dot radius in `dots` |
| `--bg-focus-x`, `--bg-focus-y` | `85%`, `25%` | where glows and fades centre |

### 4.5 Safety

- Forced colours mode hides both pseudo elements.
- Print hides the pattern layer. The colour field stays.
- Text always sits on paper plus at most a 34% tint, so contrast stays high
  (see section 8).

---

## 5. How transitions work

### 5.1 The driver

The JavaScript is scroll linked. There is no timer, duration or easing curve.
On every scroll it runs one `requestAnimationFrame` update:

1. Find the vertical centre of the viewport.
2. For each scene find `offset = (scene centre - viewport centre) / viewport height`.
   It is negative above the centre, positive below and 0 when centred.
3. Set `distance = min(1, |offset|)`.
4. Write inline styles on `[data-scene-content]` from `distance` and `offset`.

Scrolling back reverses everything, because the values come from position and
not from time.

### 5.2 The five built in effects

| Effect | Opacity | Scale | Blur | Slide |
|---|---|---|---|---|
| `zoom` | `1 - 0.65 d` | `1 - 0.12 d` | none | none |
| `blur` | `1 - 0.65 d` | `1 - 0.12 d` | `7px * d` | none |
| `fade` | `1 - 0.65 d` | none | none | none |
| `slide` | `1 - 0.65 d` | none | none | `offset * 45px` on x |
| `none` | 1 | none | none | none |

`d` is `distance`. Opacity never drops below 0.35, so adjacent scenes stay
legible while they scroll past.

Related behaviour

- **Nav buttons** call `scrollTo` with smooth behaviour (instant when motion is
  reduced).
- **Snap** is `proximity`, so tall scenes stay scrollable.
- **Reduced motion** (system setting, an ancestor `.no-motion`, or
  `data-tm-no-motion="true"`) sets opacity to 1 and removes every other
  effect.
- **Print** forces everything visible.

### 5.3 CSS transition models (new, optional)

The JavaScript writes `opacity`, `translate`, `scale` and `filter`. It never
touches `transform` or `clip-path`. The new models use those two, so they
combine with the JavaScript effects without a clash.

Set `data-scene-transition` on the host:

| Model | Motion | Maths |
|---|---|---|
| `rise` | scene moves further than the scroll, like parallax | `translateY(offset * 3.5rem)` |
| `drift` | sideways glide opposite to the scroll | `translateX(offset * -5rem)` |
| `tilt` | tips back like a card on a shelf | `perspective(70rem) rotateX(offset * -16deg)` |
| `wipe` | text is cropped from the right as it leaves | `clip-path: inset(0 (distance * 45%) 0 0)` |
| `stagger` | eyebrow, heading and body move at different rates | translateY at `1rem`, `2.5rem`, `4rem` times `offset` |

`stagger` is the writing transition: the three text parts drift apart as the
scene leaves and close up as it arrives.

Pair a model with the `fade` or `none` effect. A model together with `zoom` or
`blur` works but moves more than most pages need.

### 5.4 The two lines that switch the models on

The models read `--scene-offset` and `--scene-distance` from each
`[data-scene-content]`. `scroll-scenes.js` does not write them yet, so the
models do nothing (every value falls back to 0). To switch them on, add two
lines inside the `scenes.forEach` loop in `render()`, straight after
`const content = contents[index];`:

```js
content.style.setProperty('--scene-offset', offset.toFixed(4));
content.style.setProperty('--scene-distance', distance.toFixed(4));
```

`destroy()` already restores each content element's original `style`
attribute, so cleanup needs no change. Reduced motion and print are handled in
the CSS with `!important` rules.

I have not made this change. `backgrounds-preview.html` carries a small bridge
script that does the same job from outside, so you can try every model first.
Say the word and I will patch the JavaScript and remove the bridge.

### 5.5 Adding a new model

A model is one CSS rule that reads the two variables:

```css
.scroll-scenes[data-scene-transition="lift"] [data-scene-content] {
  transform: translateY(calc(var(--scene-distance, 0) * -2rem)) scale(calc(1 - var(--scene-distance, 0) * .04));
}
```

Add `lift` to the allowed values in `field_map` and a preset if it earns one.

---

## 6. Presets: style and transition together

A preset bundles a scheme, a background, a transition model and an effect that
suit each other. They live in `style_presets` in the YAML.

| Preset | Scheme | Background | Model | Effect |
|---|---|---|---|---|
| `original` | default | `lines` | none | `zoom` |
| `calm` | default | `wash` | none | `zoom` |
| `technical` | default | `grid` | `drift` | `fade` |
| `editorial` | warm | `spotlight` | `stagger` | `fade` |
| `atlas` | dusk | `contour` | `tilt` | `fade` |
| `horizon-rise` | default | `horizon` | `rise` | `fade` |
| `night-study` | night | `aurora` | none | `blur` |

---

## 7. Colour schemes

A scheme only sets tokens, so the template stays token driven. Set these on
`.scroll-scenes` or an ancestor:

```
--scene-paper  --scene-ink  --scene-accent
--scene-colour-1  --scene-colour-2  --scene-colour-3  --scene-colour-4
```

The component already reads the design system tokens `--surface-1`, `--ink`,
`--accent` and `--font-ui` first, then falls back to its own values. A page
that sets those four tokens re-colours the component with no scheme at all.
The `data-scheme` examples (`night`, `warm`, `dusk`) exist so you can see how
far the same backgrounds stretch.

---

## 8. Checks run

- `scene-content.template.yaml` parses. The four OQEA scenes and the five
  scene illustration for a custom model pass the template's own length limits.
- `lines` renders pixel identical to the original `scroll-scenes.css`
  background in all four scenes.
- A fifth scene takes colour slot 1 again.
- No console errors or warnings in the preview page.
- The `stagger` model produces the expected transform at the sampled scroll
  position (`-0.549 * 2.5rem` on the heading, about `-22px`).
- Contrast, measured on rendered pixels under the real eyebrow, heading and
  body boxes. Every background, every scheme, every scene, at 1300px and 390px
  wide. The worst pixel in each case:

  | Scheme | Heading and body (worst case) | Eyebrow (worst case) |
  |---|---|---|
  | default | 9.0:1 | 4.5:1 |
  | night | 6.4:1 | 4.6:1 |
  | warm | 8.2:1 | 5.1:1 |
  | dusk | 8.5:1 | 5.4:1 |

  The default scheme's 4.5:1 comes from your original `lines` background, which
  I left unchanged. The other backgrounds darken the eyebrow slightly
  (`--scene-eyebrow`, 75% accent and 25% ink) because `aurora` and `contour`
  fell to about 4.0:1 without it. The measure is the lowest single pixel, so it
  is stricter than a typical reading of the text.

---

## 9. Open points

1. The colour formula in section 4.3 is my derivation from the component
   tokens. Replace the six percentages if the house formula differs.
2. Models with more than four stages reuse the four colour slots. Add
   `--scene-colour-5` and beyond if you want a distinct colour per stage.
3. The JavaScript patch in section 5.4 is ready but not applied.
4. Welsh content sits in `i18n.cy` in the YAML and stays empty until a
   professional translation is supplied.
