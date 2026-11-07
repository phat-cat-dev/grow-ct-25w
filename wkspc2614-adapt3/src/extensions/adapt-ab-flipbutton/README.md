# adapt-ab-flipbutton

An auto-width, two-face toggle button as an extension, usable from any text
field. Dependency-free (no Bootstrap JS/jQuery), accessible, respects
reduced-motion.

## Enable

Zero-config: enabled unless disabled. In `course.json`:

```json
"_abFlipbutton": { "_isEnabled": true }
```

## Use

```html
<button type="button" class="ab btn flipbutton" data-ab-flipbutton
  aria-pressed="false" aria-label="Toggle example">
  <span class="flipbutton__face flipbutton__face--front" aria-hidden="true">Explore</span>
  <span class="flipbutton__face flipbutton__face--back" aria-hidden="true">See what is possible</span>
</button>
```

`btn` is the shared `.ab.btn` object (`adapt-ab-base/less/ab-base-button.less`)
— it supplies colour, padding, and hover/active/focus/disabled states, the
same as any other `.ab.btn` trigger (e.g. `adapt-ab-collapse`). `flipbutton`
is required alongside it; it supplies the two-face grid-stack mechanics, not
a standalone look.

Both face spans sit in the same grid cell and contribute their natural width
and height, so the button auto-sizes to the larger face with no JS
measurement; each face is centred (both axes) within that cell, so the two
labels sit in the same visual spot regardless of which is shorter. Faces can
wrap on narrow screens. No card or external container is needed.

Hover and keyboard focus preview the back face; this preview is separate from
the pressed state — removing hover/focus returns to the front face unless the
button has been pressed. Click/tap/Enter/Space toggles `aria-pressed` and
`data-flipped`.

Use a stable, meaningful `aria-label` for the action — the face spans are
decorative (`aria-hidden`), so changing the visible face never alters the
accessible name.

For an ordinary action button (not a toggle), remove `data-ab-flipbutton` and
`aria-pressed`, give it an action-specific `aria-label`, and wire your own
click handler; the hover/focus face-preview CSS still applies without the
extension's JS. Use a real link, not a button, for navigation.

## Accessibility

Use a real `<button>`; non-button triggers are made keyboard-operable
(`role="button"`, `tabindex="0"`, Enter/Space). `aria-pressed` is kept in sync
on toggle. The face swap respects `prefers-reduced-motion` (instant, no
transition).

## Styling

`less/ab-flipbutton.less` adds only the grid-stack mechanics and face
centring on top of `.ab.btn` — colour, padding and states come from
`.ab.btn` itself (`--ab-accent`/`--ab-base-*` tokens), not from this file.
The one component-specific token is `--ab-flipbutton-duration` (face-swap
transition length). No palette is defined here; the button follows the
active theme the same way any other `.ab.btn` does.

## Events

```js
import Adapt from 'core/js/adapt';
Adapt.on('abFlipbutton:changed', (triggerEl, isFlipped) => { /* … */ });
```

## Notes

Pure state-transition logic is unit-tested (`flipbuttonLogic`, `node --test`);
the hover/focus/pressed CSS is validated in a running course. No palette —
the extension is mechanics only.
