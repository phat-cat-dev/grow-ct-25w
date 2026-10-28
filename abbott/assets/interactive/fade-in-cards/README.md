# Sequential fade-in cards

[Open the offline demo](index.html). A clean, reusable interpretation of the
heading, segmented introduction and three-card reveal pattern. No WordPress,
Swiper, GSAP, network dependencies or pasted chat wrappers are required.
Demonstration copy is original placeholder content; replace it with your own.

## Card count, vertical layout and effects

### Hover-flip information backs

Cards now spin horizontally to reveal more information on a dark back. Mouse
hover reveals it; leaving returns to the front. Tap/click or Enter/Space toggles
the face; Escape returns to the front. Keyboard focus alone does not flip.
The whole card is a button target; keep both faces informational, without nested
links or controls. `aria-expanded`, `aria-controls` and the inactive face's
`aria-hidden`/`inert` state follow the visible face.

Include `flip-cards.js` after the section markup (before `workshop.js` in the
demo). Add `<div class="fade-card-back" hidden>…</div>` inside each `.fade-card`.
The script enhances existing cards automatically. For dynamically added cards,
call `FadeFlipCards.enhance(container)`. Without this script the front stays
visible and the optional back stays hidden.

Both faces contribute to card height, so longer back text does not get clipped.
The spin is separate from the outer sequential entrance effect and works in
both layouts and on additional cards. Reduced motion changes faces instantly.
Tokens: `--fade-back-paper`, `--fade-back-ink`, `--fade-flip-duration` (650ms).

The workshop supports 1–12 cards and either a grid or a vertical stack.
Count/layout update immediately and stop the current animation; press Replay
to start again. Reducing the count keeps removed card nodes in memory so their
content returns if you increase it again (until page reload). Additional cards
use editable placeholder copy. The download remains the starter fragment, not
an export of the current workshop settings.

Choose fade only, fade + rise, slide from left, slide from right or gentle zoom.
Transition duration and the gap **after** each card are independent: cards
never overlap when `cardGap` is specified. Intro stagger still controls the
heading/text sequence. The first card starts after the introduction finishes.
Space is reserved for every card; reveals do not collapse the stack, scroll the
page, steal focus or remove content from screen readers.

For your own vertical version, set `data-layout="vertical"` on `.fade-cards`
and add/remove `<li data-fade-item>` elements inside `.fade-grid`:

```js
const player = FadeInCards.mount(document.querySelector('.fade-cards'), {
  duration: 700, stagger: 160, distance: 24,
  effect: 'rise', cardGap: 1200
});
```

`cardGap` accepts 0–10000 ms or `null` (the original overlapping stagger).
The reusable runtime defaults to `null` for backwards compatibility; the
workshop starts at 500 ms. `effect` defaults to `'rise'`; alternatives are
`'fade'`, `'left'`, `'right'`, `'zoom'`. Distance affects rise/slide only.
The player reads the current items on every replay, so newly added cards work
without remounting. The runtime has no card-count limit; 12 is the workshop cap.

## Use

Include [fade-in.css](fade-in.css) and [fade-in.js](fade-in.js), then paste
[section.template.html](section.template.html) into your page:

```html
<link rel="stylesheet" href="fade-in.css">
<!-- Paste the section fragment here. -->
<script src="fade-in.js"></script>
<script>
  const player = FadeInCards.mount(document.querySelector('.fade-cards'), {
    duration: 650, stagger: 160, distance: 18
  });
</script>
```

It plays once on first viewport entry. Every `[data-fade-item]` in DOM order
gets a fade and gentle upward reveal: eyebrow, title, text segments, cards.
Keep spaces between inline text spans. Text is not split automatically, so
links, emphasis, line breaks, selection and screen-reader reading order remain intact.
Use `distance: 0` for opacity-only animation.

For button/completion triggers, mount with `trigger: 'manual'`, then call
`player.play()`. Also available: `player.show()`, `player.set({ stagger: 200 })`
and `player.destroy()`. `play()` returns a promise and the section emits
`fade-in:complete` after an uninterrupted sequence. Cancelling/replaying does
not emit completion for the interrupted run.

Duration is 100–2000 ms, stagger 0–1000 ms, distance 0–60 px. Invalid values
throw explicit errors. The demo reports errors in its status area.

All content remains in the document, visible without JavaScript. Animation
never awards learning completion or locks a card. Keyboard focus inside the
section cancels playback and reveals everything. System reduced motion and
ancestor `.no-motion` / `data-tm-no-motion="true"` skip animations; changing
these preferences during playback reveals all content immediately.

Scoped theme tokens: `--fade-accent`, `--fade-paper`, `--fade-ink`,
`--fade-line`, `--fade-radius`; defaults consume the page's existing theme.
The three columns become a single column on smaller screens.
