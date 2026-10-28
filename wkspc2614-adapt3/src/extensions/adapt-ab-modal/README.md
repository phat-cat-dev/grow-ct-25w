# adapt-ab-modal

A single, globally-triggerable Bootstrap-5-shaped modal (`.ab.modal`) for Adapt.
Dependency-free (no Bootstrap JS, Popper or jQuery), accessible, and usable from
any element in any text field.

## Enable

Zero-config: enabled unless explicitly disabled. In `course.json`:

```json
"_abModal": { "_isEnabled": true }
```

## Configure reusable modals

```json
"_abModal": {
  "_isEnabled": true,
  "_modals": [
    {
      "_id": "refs",
      "title": "References",
      "body": "<p>Harvard, Cite Them Right…</p>",
      "_size": "lg",            // "", "sm", "lg" or "xl"
      "_isStatic": false,        // true = no Escape / backdrop close
      "_isCentered": false,
      "_isScrollable": false
    }
  ]
}
```

## Trigger from anywhere

By configured id (recommended — use a real `<button>`):

```html
<button type="button" data-ab-modal="refs">References</button>
```

Ad-hoc, no config needed:

```html
<button type="button"
  data-ab-modal
  data-ab-modal-title="Quick note"
  data-ab-modal-body="&lt;p&gt;Any HTML.&lt;/p&gt;"
  data-ab-modal-size="sm">More</button>
```

Inline `data-ab-modal-*` attributes override a matched configured modal, so one
configured modal can be reused and tweaked per trigger. Non-`<button>` triggers
are made keyboard-operable automatically (`role="button"`, `tabindex="0"`,
Enter/Space activation).

## Programmatic API

```js
import Adapt from 'core/js/adapt';
Adapt.trigger('abModal:open', 'refs');                 // configured modal by id
Adapt.trigger('abModal:open', { title, body, size });  // ad-hoc
Adapt.trigger('abModal:close');
// emitted: 'abModal:opened' (id|null), 'abModal:closed'
```

## Accessibility

`role="dialog"` + `aria-modal="true"`, labelled by the title (and described by
the body when present). Focus moves into the dialog on open and is trapped
(Tab/Shift+Tab wrap); Escape and backdrop-click close unless `_isStatic`; focus
returns to the trigger on close; background scroll is locked while open; the
modal closes on route change.

## Styling

`less/ab-modal.less` consumes `--ab-*` theme tokens only (surface, ink, hairline,
radius, spacing, accent) — no palette is defined here, so the modal inherits the
active theme / base defaults.

## Notes

Content set via `data-ab-modal-body` / `_modals[].body` is authored HTML and is
injected as-is; treat it as trusted course content.
