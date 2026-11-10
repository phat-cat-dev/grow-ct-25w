# adapt-grow-references

A **read-only references list** for the Adapt framework — a tidy, numbered-free
list of the books and external resources behind a lesson. Each entry is a link
the learner can follow, with an optional second link to the same resource in a
university library catalogue.

Part of the **GROW** plugin set.

## Presentation, not a question

There is no learner input and no scoring. The component uses the stock
`ComponentModel`; the view sets itself ready and uses core's standard
`setupInviewCompletion` so the block completes when it scrolls into view —
otherwise, having nothing to interact with, it would stay incomplete and block
page/trickle completion.

## What the learner sees

- An optional **instruction** line above the list.
- A bulleted list of references. Each **title** is a link (`href`) that opens in
  a new tab (`target="_blank"`, `rel="noopener"`).
- Where an entry has a **permalink**, a small `(permalink)` link follows it,
  pointing at the library-catalogue copy of the same resource.

## Authoring

Fill `_items` — each entry is an object:

| Field | Purpose |
|---|---|
| `title` | Display text for the reference (the link label). Required. |
| `href` | Clickable URL to the resource. Always a populated value. Required. |
| `_hrefStatus` | `placeholder` or `confirmed` — whether `href` is a real, confirmed link or still a placeholder awaiting the real one. Required. |
| `type` | Free-text category, e.g. `book` or `external` (not a locked enum). |
| `permalink` | Optional library-catalogue permalink for the same resource. Independent of `href`, not a fallback. |

See `example.json` for a full block.

## Settings

`_component` must be `growReferences`; the target attribute is `_growReferences`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
