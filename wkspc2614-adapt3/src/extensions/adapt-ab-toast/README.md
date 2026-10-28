# adapt-ab-toast

Bootstrap-5-shaped toasts (`.ab.toast`) — transient notifications stacked in a
corner live region, shown programmatically. Dependency-free; styled on
`--ab-base-toast-*` tokens.

## Enable

Zero-config: enabled unless disabled. In `course.json`:

```json
"_abToast": { "_isEnabled": true }
```

## Show a toast

```js
import Adapt from 'core/js/adapt';

Adapt.trigger('abToast:show', {
  title: 'Saved',
  body: 'Your answer was recorded.',
  variant: 'success',   // accent | success | danger | warning | info
  autohide: true,       // default true
  delay: 5000,          // ms, default 5000
  showClose: true       // default true
});

Adapt.trigger('abToast:hideAll');

Adapt.on('abToast:shown', (el, spec) => { /* … */ });
Adapt.on('abToast:hidden', (el) => { /* … */ });
```

A close button dismisses immediately; `autohide` dismisses after `delay` ms;
toasts clear on navigation (`router:location`).

## Tokens (level 3)

`--ab-base-toast-bg` / `-color` / `-border` / `-accent` / `-radius` / `-width`,
each defaulting to the base spine; variants move `--ab-base-toast-accent`.

## Accessibility

Toasts append to a shared `role="region"` with `aria-live="polite"`, so they are
announced without stealing focus. Polite is the safe default for incidental
feedback; it does not interrupt the learner.

## Verify

`toastLogic` (option normalisation) is unit-tested (`node --test`); the DOM/timer
glue is validated in a running course (dev server).
