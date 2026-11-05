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
<button type="button" class="ab flipbutton" data-ab-flipbutton
  aria-pressed="false" aria-label="Toggle example">
  <span class="flipbutton__face flipbutton__face--front" aria-hidden="true">Explore</span>
  <span class="flipbutton__face flipbutton__face--back" aria-hidden="true">See what is possible</span>
</button>
```

Both face spans sit in the same grid cell and contribute their natural width
and height, so the button auto-sizes to the larger face with no JS
measurement. Faces can wrap on narrow screens. No card or external container
is needed.

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

`less/ab-flipbutton.less` consumes `--ab-base-*` theme tokens only (surface,
ink, hairline, radius, spacing, accent) plus one component-specific
`--ab-flipbutton-duration` override — no palette is defined here, so the
button inherits the active theme / base defaults. Choose contrasting theme
colours; this extension does not calculate contrast automatically.

## Events

```js
import Adapt from 'core/js/adapt';
Adapt.on('abFlipbutton:changed', (triggerEl, isFlipped) => { /* … */ });
```

## Notes

Pure state-transition logic is unit-tested (`flipbuttonLogic`, `node --test`);
the hover/focus/pressed CSS is validated in a running course. No palette —
the extension is mechanics only.
