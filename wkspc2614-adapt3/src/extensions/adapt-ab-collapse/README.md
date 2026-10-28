# adapt-ab-collapse

A Bootstrap-5 collapse (show/hide with height animation) as an extension, usable
from any text field. Dependency-free (no Bootstrap JS/jQuery), accessible,
respects reduced-motion.

## Enable

Zero-config: enabled unless disabled. In `course.json`:

```json
"_abCollapse": { "_isEnabled": true }
```

## Use

A trigger targets a collapsible element by selector:

```html
<button type="button" class="ab btn" data-ab-collapse="#more">Show more</button>

<div class="ab collapse" id="more">
  <p>Hidden until the trigger is activated.</p>
</div>
```

- Start **open** by adding `show`: `<div class="ab collapse show" id="more">`.
- Multiple triggers can point at the same target (all stay in sync).
- A trigger's selector may match several targets (all toggle together).

### Accordion style (one open at a time)

```html
<div id="faq">
  <button data-ab-collapse="#p1" data-ab-collapse-parent="#faq">Q1</button>
  <div class="ab collapse" id="p1">A1</div>
  <button data-ab-collapse="#p2" data-ab-collapse-parent="#faq">Q2</button>
  <div class="ab collapse" id="p2">A2</div>
</div>
```

Opening one closes the other open collapses within the `data-ab-collapse-parent`
ancestor. (For a full question-style accordion component, use `adapt-ab-accordion`.)

## Accessibility

Triggers get `aria-expanded` + `aria-controls` (auto-added, kept in sync). Use a
real `<button>`; non-button triggers are made keyboard-operable (`role="button"`,
`tabindex="0"`, Enter/Space). The height animation respects
`prefers-reduced-motion`.

## Events

```js
import Adapt from 'core/js/adapt';
Adapt.on('abCollapse:shown', (targetEl) => { /* … */ });
Adapt.on('abCollapse:hidden', (targetEl) => { /* … */ });
```

## Notes

Pure config parsing is unit-tested (`collapseLogic`, `node --test`); the
height/transition glue is validated in a running course. No palette — the
extension is mechanics only; the collapsed content keeps its own styling.
