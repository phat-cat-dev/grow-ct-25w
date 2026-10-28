# adapt-ab-close

A Bootstrap-5 close button (`.btn-close`) plus a generic **dismiss** behaviour,
usable from any text field. Dependency-free (no Bootstrap JS/jQuery), accessible,
styled on `--ab-*` tokens.

## Enable

Zero-config: enabled unless explicitly disabled. In `course.json`:

```json
"_abClose": { "_isEnabled": true }
```

## Use

Put a close button inside anything you want dismissible:

```html
<div class="ab alert" data-ab-dismissible>
  <button type="button" class="btn-close" data-ab-dismiss aria-label="Close"></button>
  <p>A dismissible notice.</p>
</div>
```

Clicking it dismisses the nearest ancestor marked `data-ab-dismissible`
(or `.ab.alert` / `.ab.card`).

### Target a specific element

```html
<button type="button" class="btn-close" data-ab-dismiss="#notice-1" aria-label="Close"></button>
```

### Options (data-* on the button)

| Attribute | Effect |
|---|---|
| `data-ab-dismiss` | empty / `true` = nearest dismissible ancestor; a value = target selector |
| `data-ab-dismiss-remove="false"` | hide (`hidden`) instead of removing from the DOM |
| `data-ab-dismiss-fade="0"` | disable the fade-out (ms; default 200) |

### Variant

`btn-close-white` inverts the glyph for dark backgrounds.

## Accessibility

Use a real `<button>` with `aria-label="Close"` (auto-added if missing).
Non-`<button>` triggers are made keyboard-operable (`role="button"`,
`tabindex="0"`, Enter/Space). On dismiss, focus moves to the element after the
dismissed one (else before it, else its parent); the fade respects
`prefers-reduced-motion`.

## Events

```js
Adapt.on('abClose:dismissed', (targetEl) => { /* … */ });
```

## Notes

Does not collide with `adapt-ab-modal`, which closes via `data-ab-modal-dismiss`.
Styling consumes `--ab-*` tokens only (ink, surface, accent) — no palette.
