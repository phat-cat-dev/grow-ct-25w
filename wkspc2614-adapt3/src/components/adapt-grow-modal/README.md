# adapt-grow-modal

A **modal launcher** for the Adapt framework — a trigger button (with an
optional on-page teaser) that foregrounds authored content in a focused,
dimmed-backdrop popup. Use it to pull an activity, worked example, definition or
"try this" panel out of the page flow and into a dedicated overlay.

Part of the **GROW** plugin set, tokenised to the GROW theme. The on-page
trigger is a `.cm.btn`; the popup itself is the stock Adapt notify popup —
the same modal the hotgraphic hotspots and question feedback use — themed
light/dark by the theme's `cm-notify.less` on `--ab-popup-*` tokens. The LESS
here only lays out the trigger.

## Presentation, not a question

The component extends the stock `ComponentModel`/`ComponentView` — no marking,
no interaction recording. The popup body is authored HTML. On click it opens via
`Adapt.notify.popup`, which traps focus until dismissed. By default completion
fires on **open** (engagement); it can be set to on-**view** or **none**.

## Authoring

| Field | Purpose |
|---|---|
| `body` | Optional teaser shown on the page, above the trigger button. |
| `_completion` | When it completes: `trigger` (on open, default), `view` (scrolls into view), or `none`. |
| `_trigger.text` | Trigger button text (required). |
| `_trigger.ariaLabel` | Accessible label for the trigger; falls back to the button text. |
| `_trigger._icon` | Optional `cm` icon name (e.g. `learning`) shown on the button. |
| `_popup.title` | Popup heading. |
| `_popup.body` | The foregrounded content, HTML allowed (required). |
| `_popup._classes` | Extra CSS classes on the popup (`cm-notify cm-modal` always applied). |
| `_popup._isCancellable` | Whether the learner can dismiss with the close control / Esc (default `true`). |

See `example.json` for a full block.

## Settings

`_component` must be `growModal`; the target attribute is `_growModal`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
