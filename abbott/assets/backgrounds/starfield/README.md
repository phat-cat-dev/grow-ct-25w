# Layered starfield

[Open the offline demo](index.html). An original canvas implementation of
three star-depth layers drifting at different speeds, inspired by the general
visual idea in [Sarazond's CSS parallax star background](https://codepen.io/sarazond/pen/LYGbwj).
No CodePen source, assets or text were copied. This version uses canvas rather
than Sass-generated box shadows; no dependencies or network access are needed.

Include `starfield.css`, paste [the fragment](section.template.html), then:

```html
<script src="starfield.js"></script>
<script>
  const stars = Starfield.mount(document.querySelector('.starfield'), {
    density: 180, speed: 1, paused: false
  });
</script>
```

API: `stars.set({density:250, speed:0.5})`, `stars.set({paused:true})`,
`stars.shuffle()`, `stars.get()`, `stars.destroy()`.
Density is an integer from 20–500; speed is 0.1–3; paused is boolean.
Invalid options throw explicit errors. Each host has independent stars.
Destroy cancels the frame loop and removes observers, listeners and canvas.

Provide a pause button wherever this looping decorative asset is embedded;
the demo includes one. System reduced motion, ancestor `.no-motion` and
`data-tm-no-motion="true"` keep stars static. Hidden tabs and offscreen hosts
stop rendering; resume has no time jump. Resizing preserves relative star
positions. Pixel ratio is capped at 2.

Canvas is decorative, ignores pointer input and is hidden from assistive
technology. Text remains regular HTML and stays available without JavaScript.
No twinkling/flashing is used. This is an ambient drifting background, not a
scroll-linked effect or pointer-tracking parallax.

Tokens: `--star-colour` (use a CSS hex/rgb/hsl colour), `--star-ink`,
`--star-sky`; content uses `--font-ui` when available. Keep text/background
contrast appropriate when changing these. Star colour is decorative and does
not replace the independent text colour.
