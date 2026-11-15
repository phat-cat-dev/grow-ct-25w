# adapt-grow-worked-example

A **collapsible worked example** for the Adapt framework — the title is a toggle
that opens a single panel of worked-through prose, typically a weaker version of
something set against a stronger one so the learner can see the move to copy. It
sits collapsed until opened.

Part of the **GROW** plugin set, and tokenised to the GROW theme (the toggle and
region read `--accent`, `--surface-2`, `--ink` and `--line`, with literal
fallbacks), so it repaints with the active theme.

## Presentation, not a question

There is no learner input and no scoring. It uses the stock `ComponentModel`.
Completion is the **first open**: the view calls `setCompletionStatus()` the
first time the accordion is opened, which passes the trickle — opening is the
whole gate, since there is nothing to tick.

The weaker/stronger paragraph cue classes (`we-weaker` / `we-stronger`) are baked
into the body prose upstream and themed separately in `adapt-ab-theme`; this
component only owns the accordion shell.

## Accessibility

- The toggle is a real `<button>` with `aria-expanded` and `aria-controls`; the
  revealed region is `role="region"` labelled by the heading (and by the
  authorable `ariaRegion` global).
- The chevron icon is `aria-hidden`.
- Honours `prefers-reduced-motion` (the icon's rotation transition is dropped).

## Authoring

The schema is deliberately minimal — the component takes only the standard
component fields:

| Field | Purpose |
|---|---|
| `displayTitle` | The toggle label (falls back to "Worked example"). |
| `body` | The worked-example prose revealed when opened. |
| `_supportedLayout` | `full-width`, `half-width` or `both` (default `full-width`). |

See `example.json` for a full block.

> CSS note: the root class is `.growworkedexample` (no hyphens). Adapt's
> `ComponentView` lowercases `_component` (`growWorkedExample`) without inserting
> a hyphen, so the LESS block name matches that live root class — this is
> intentional, not a typo.

## Settings

`_component` must be `growWorkedExample`; the target attribute is
`_growWorkedExample`. Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
