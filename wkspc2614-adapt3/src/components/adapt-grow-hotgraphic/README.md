# adapt-grow-hotgraphic

A **hotgraphic** for the Adapt framework — an authored SVG diagram with
selectable **hotspots**. The learner selects a marked point on the diagram to
open more about that stage, as a modal popup or an inline reveal beneath the
diagram. It inlines the SVG and binds each content item to a node inside it, so
any future diagram can be painted by the theme without new component code.

Part of the **GROW** plugin set, tokenised to the GROW theme (it uses
`--ab-base-accent`, `--ab-base-ink`, `--ab-base-surface-*` and the
`--ab-hotgraphic-wedge-*` tokens, so it repaints with the active theme and has a
dark mode for free).

## Needs an authored SVG asset

**This component ships no `example.json`** — its example is parked at
`example.needs-asset.json` because it needs a **course SVG with hotspot nodes**
that does not exist yet. That parked example models a four-stage "reflective
learning cycle": a `_diagram.src` of `course/en/images/placeholder-reflective-cycle.svg`
and four `_items` (Experience, Reflect, Make sense, Apply) whose `_hotspot._id`
values (`experience`, `reflect`, `learn`, `apply`) each resolve to a node in
that SVG. To use it, author the SVG under `course/`, give each hotspot a
`data-ab-hotspot` attribute or matching element id, and drop the parked block
into your content. The source must be a relative path under `course/`.

## Behaviour and accessibility

- The view fetches and **inlines** the SVG, namespaces its ids (so two diagrams
  on one page never collide), and sanitises design-tool accidents (`script`,
  `foreignObject`, `on*` handlers, external `href`s).
- Interactive hotspots become `role="button"`, `tabindex="0"` controls with an
  accessible label (title plus a "visited" word once seen); Enter/Space
  activate them. Decorative hotspots (`_action: "none"`) are painted but never
  focusable, and excluded from completion.
- A **narrow-band fallback** — a plain, always-correct `<ol>` of native buttons
  in `_items` order — is shown instead of the SVG when the diagram is too narrow
  for its own text, so it stays fully usable.
- The SVG is `role="group"` (not `role="img"`, which would prune the controls)
  with `aria-labelledby`/`describedby` onto its own `<title>`/`<desc>`.

## Authoring

| Field | Purpose |
|---|---|
| `_diagram.src` | Relative path under `course/` to the SVG file (required). |
| `_diagram.title` | Accessible label for the narrow-band fallback list (required). |
| `_diagram._slug` | Advanced: overrides the generated theme class hook; defaults to the SVG filename. |
| `_items[].title` | Hotspot accessible label and popup/reveal heading (required). |
| `_items[].body` | Content shown for `popup` / `inlineReveal`; unused for `none`. |
| `_items[]._hotspot._id` | Matches a `data-ab-hotspot` attribute or element id in the SVG. |
| `_items[]._hotspot._selector` | Advanced: explicit CSS selector into the SVG (tried first). |
| `_items[]._hotspot._action` | `popup`, `inlineReveal`, or `none` (decorative). |
| `_setCompletionOn` | `allItems` (visit every required hotspot) or `inview`. |

See `example.needs-asset.json` for a full block.

## Settings

`_component` must be `growHotgraphic`; the target attribute is `_growHotgraphic`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
