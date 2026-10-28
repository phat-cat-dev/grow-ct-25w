# Lesson record template

A pure Handlebars template for the whole lesson front matter data group, with a
plain grey skin laid over it and an optional markup inspector.

| File | Role |
|---|---|
| `lesson-record.hbs` | The template. Semantic HTML, no JavaScript, no inline styles. Reads as a plain document with no CSS. |
| `lesson-record.skin.css` | The skin: white page and header (no borders), very light grey cards, white inner layer, 1px borders, 3px corners. Greyscale only. |
| `lesson-record.inspect.css` and `.js` | Optional data layer view (see below). |
| `lesson-record.sample.json` | Sample lesson record and course record in the spec section 3 shape. |
| `build.js` | Builds the view model and renders `lesson-record.example.html`. `npm install handlebars` then `node build.js`. |
| `lesson-record.example.html` | Rendered example. Open it directly. |

## Structure

```
article.lr
  header.lr__header          white, no border
  div.lr__bar                card: key and tools slot
  ol.lr__groups
    li.lr__item > details.lr-group             every group is an accordion
                                               (01-09, 12 open; 10, 11 closed)
      summary.lr-group__summary
      div.lr-group__body
        p.lr-note                              callout
        div.lr-panel                           inner layer
          li.lr-item#CO1 / #LO1 / #ACT1        id blocks, one card each
```

Course outcomes (05), lesson outcomes (06) and activities (07) are three
separate cards at the same level. They link to each other with plain anchors
and `:target` highlights the block you land on.

## Data layer view

Press **Markup** in the bar. Every element is outlined by nesting depth and a
panel opens with:

- the hovered or pinned element: its ancestor path and every attribute (class, id, role, aria-*, data-*, href and so on)
- the whole tree beside it, with tag, classes, id, ARIA and data attributes in separate colours
- filters for **All**, **ARIA and roles** and **Classes**

Click pins an element, clicking a tree line scrolls to it and opens any closed
accordion around it, Escape closes.

## View model

The template expects the lesson record fields as they are, plus `course`
(`language`, `learner_pitch`, `voice_specification`, `referencing_style`,
`rights`, `outcomes[]` each with `aligned`), `position` and `summaries.*`.
`build.js` shows how to derive them. Treat the output as a display view of the
authoritative metadata, not a second source of truth (spec section 5).
