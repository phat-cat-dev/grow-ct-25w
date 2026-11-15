# adapt-grow-tabs

A **tabbed content** component for the Adapt framework — two to four tabs across
the top, each revealing its own panel of title, body text and an optional image.
The learner clicks or arrow-keys between them; only the active panel is shown.

Part of the **GROW** plugin set, and tokenised to the GROW theme (the tab rule,
active indicator, hover and label colours read from theme custom properties such
as `--ab-base-accent`, `--ab-base-accent-deep` and `--ab-dark-grey`), so it
repaints with the active theme.

## Presentation, not a question

There is no scoring. It extends `ItemsComponentModel` for per-tab visitation
tracking; the first tab is active and marked visited on render, and the view
uses core's standard `setupInviewCompletion`, so the block completes when it
scrolls into view. On revisit (`_isResetOnRevisit`) it returns to the first tab.

## Accessibility

Full WAI-ARIA tabs pattern:

- `role="tablist"` / `role="tab"` / `role="tabpanel"`, with `aria-selected`,
  `aria-controls` and `aria-labelledby` wired up.
- **Roving tabindex**: the active tab is the one tab stop; **Left/Right** (and
  **Up/Down**) move between tabs with wraparound, **Home/End** jump to the ends,
  with automatic activation on focus.
- `aria-orientation` switches `horizontal` → `vertical` at the narrow-viewport
  breakpoint (`60rem`), matching the stacked LESS layout.
- Honours `prefers-reduced-motion`.

## Authoring

Fill `_items` — **2 to 4** tabs, each an object:

| Field | Purpose |
|---|---|
| `tabTitle` | Short label on the tab button (1-3 words). Required. |
| `title` | Optional heading shown inside the panel. |
| `body` | The panel's main content. Required. |
| `_graphic.src` / `_graphic.alt` | Optional panel image and its alt text (blank alt = decorative). |

`instruction` sets the instruction line; `ariaRegion` is an authorable global.
See `example.json` for a full block.

## Settings

`_component` must be `growTabs`; the target attribute is `_growTabs`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
