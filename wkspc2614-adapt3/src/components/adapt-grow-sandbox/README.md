# adapt-grow-sandbox

A **minimal placeholder component** for the Adapt framework — it exists purely to
prove the GROW component build pipeline renders end to end. The learner sees a
standard header and a single boxed line reading "Sandbox component rendered."

Part of the **GROW** plugin set, and tokenised to the GROW theme: the box reads
its surface, ink, hairline, radius and spacing from the theme's custom
properties (`--ab-base-surface-sunken`, `--ab-base-ink`, `--ab-base-hairline`,
`--ab-border-radius`, `--ab-space-100`), each with a literal fallback, so it
repaints with the active theme.

> Note: this component is currently **excluded from the comps build**. It is a
> development/testing harness, not lesson content.

## Behaviour

There is no learner input and no scoring. The component uses the stock
`ComponentModel`; the view sets itself ready and uses core's standard
`setupInviewCompletion`, so it completes when it scrolls into view.

## Authoring

It takes only the standard component fields:

| Field | Purpose |
|---|---|
| `displayTitle` | Title shown on the page (default "GROW Sandbox"). |
| `body` | Body text under the title. |
| `instruction` | Optional instruction line. |
| `_supportedLayout` | `full-width`, `half-width` or `both` (default `both`). |

See `example.json` for a full block. The schema is `schema/component.schema.json`.

## Settings

`_component` must be `growSandbox`; the target attribute is `_growSandbox`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
