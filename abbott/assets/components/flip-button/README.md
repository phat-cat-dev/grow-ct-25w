# Auto-width flip button

[Open the demo](index.html). Original implementation of the general two-face
flip idea referenced by [Alex Moore's CodePen](https://codepen.io/MoorLex/pen/NBwNZa).
No source, fonts or assets copied; works offline.

Include `flip-button.css`, paste [the button fragment](button.template.html),
and include `flip-button.js` once for the optional toggle behaviour.
Both face spans occupy the same grid cell and contribute their natural width
and height. They can wrap on narrow screens. No card or external container is needed.

Hover (on hover-capable devices) and keyboard focus show the back face.
Click/tap/Enter/Space toggles `data-flipped` and `aria-pressed`. Pointer or focus
preview is separate from the pressed state: removing hover/focus returns to the
front unless pressed. A bubbling `flip-button:change` event carries
`detail.flipped`. Disabled buttons neither flip nor toggle.

Use a stable, meaningful `aria-label` for the action/toggle. Decorative face
labels are `aria-hidden`, so changing the visible face does not confuse the
accessible name. Replace the demo's generic labels in real use.

For an ordinary action button, remove `data-flip-toggle` and `aria-pressed`,
give it an action-specific accessible name and connect your own click handler.
CSS hover/focus preview still works without the script. Navigation should use
an actual link instead of pretending a toggle button navigates.

Tokens: `--flip-accent`, `--flip-paper`, `--flip-ink`, `--flip-duration`,
`--flip-radius`, with page-theme fallbacks. Default duration 450 ms.
Reduced motion and ancestor `.no-motion` / `data-tm-no-motion="true"` make the
face change instant. Focus outlines remain visible. Choose contrasting theme
colours; this component does not automatically calculate contrast.
