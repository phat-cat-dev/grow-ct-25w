# adapt-ab-progress

A Bootstrap-5 progress bar (`.ab.progress` > `.progress-bar`) as an extension,
usable anywhere — authored inline, or embedded in an interactive component /
modal and driven by its state. Dependency-free, accessible, on `--ab-*` tokens.

## Enable

Zero-config: enabled unless explicitly disabled. In `course.json`:

```json
"_abProgress": { "_isEnabled": true }
```

## Declarative (static bar)

Author the container; the extension builds the fill + ARIA from its `data-*`:

```html
<div class="ab progress"
  data-ab-progress
  data-ab-progress-value="40"
  data-ab-progress-max="100"
  data-ab-progress-show-label="true"></div>
```

### Options (`data-ab-progress-*` / event fields)

| Key | Meaning |
|---|---|
| `value` | current value (default 0) |
| `max` | maximum (default 100) |
| `label` | explicit label text (overrides the percentage) |
| `show-label` / `showLabel` | `true` shows the `%` inside the bar |
| `variant` | `success` \| `danger` \| `warning` \| `info` (moves the fill colour) |
| `striped` | `true` adds diagonal stripes |
| `animated` | `true` animates the stripes (respects reduced-motion) |
| `sm` / `lg` | add the class to the container for a thinner/thicker track |

## Programmatic (driven by a component or modal)

Render the container in your component template or modal body, then update it as
state changes. Pass an element or a selector as `target`; only the keys you pass
change, the rest are read from the element's current `data-*`:

```js
import Adapt from 'core/js/adapt';

// in a view, after rendering <div class="ab progress" data-ab-progress ...>
const el = this.$('.ab.progress')[0];
Adapt.trigger('abProgress:set', { target: el, value: 7, max: 10 });
Adapt.trigger('abProgress:set', { target: el, value: 10, variant: 'success', label: 'Done' });

// listen back
Adapt.on('abProgress:changed', (el, spec) => { /* spec.percent, spec.value… */ });
```

A selector works too: `Adapt.trigger('abProgress:set', { target: '#load', value: 100 })`.

## Accessibility

The fill is `role="progressbar"` with `aria-valuemin`/`-valuenow`/`-valuemax`;
an explicit `label` also sets `aria-valuetext`. Stripe animation and width
easing respect `prefers-reduced-motion`.

## Styling

`.ab.progress` exposes local vars (`--ab-progress-track`, `--ab-progress-bar`,
`--ab-progress-on-bar`, `--ab-progress-height`) defaulting to the base spine, so
variants/themes reskin by moving one variable. No palette defined here.
