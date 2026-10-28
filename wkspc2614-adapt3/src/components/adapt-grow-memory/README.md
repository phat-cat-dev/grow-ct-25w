# adapt-grow-memory (GROW)

Memory match: a tile-flip pairs game. The component builds a deck of two of each
authored pair, shuffles it on every load, and lays the tiles out in a responsive
grid. Turn two tiles over: a match stays revealed, a mismatch turns both back
over after a short pause so you can try again. The game is won when every pair
has been found.

It is formative only. It extends `ComponentModel` (not a question component), so
there is no score, no marking and no SCORM interaction. Completion is optional
and author-toggled.

## Authoring

```json
{
  "_component": "growMemory",
  "displayTitle": "Match the pairs",
  "body": "Turn the tiles over two at a time to find the matching pairs.",
  "instruction": "Select a tile to turn it over, then find its pair.",
  "_isCompletionBearing": true,
  "_columns": 0,
  "_items": [
    { "icon": "lightbulb", "alt": "Idea" },
    { "icon": "psychology", "alt": "Thinking" },
    { "text": "Why?", "alt": "Question" },
    { "icon": "done_all", "text": "Check", "alt": "Review" }
  ]
}
```

### Pairs (`_items`)

Each entry is **one pair** (it becomes two matching tiles). Give it:

- `icon` - a [Material Symbols Outlined](https://fonts.google.com/icons) name,
  for example `bolt`, `cloud`, `water_drop`. The GROW theme self-hosts this font,
  so icons render offline in the SCORM package.
- `text` - short text shown on the tile. Keep it brief so it fits.
- `alt` - what a screen reader reads for the tile when it is turned over. Falls
  back to `text`, then `icon`. **Set this on icon-only tiles.**

Provide an `icon`, a `text`, or both. Four to eight pairs grid well.

### Options

- `_isCompletionBearing` (default `true`): when `true`, finding all pairs marks
  the component complete. When `false`, the game is purely formative: the win
  message still shows, but completion is satisfied on view instead (so it never
  gates the page). If a non-bearing game still must not count, also set
  `_isOptional: true` on the component.
- `_columns` (default `0`): `0` lays the tiles out responsively; a positive value
  fixes the column count.

### Learner-facing strings

All learner-facing copy (the ARIA region intro, tile labels, reveal / match /
no-match announcements, the matched-state suffix and the win message) lives in
the schema `globals`, so it is editable and translatable in one place. British
English, addresses the learner as "you", no em dashes.

## Accessibility

- Tiles are native `<button>`s: Tab to move, Enter / Space to turn over.
- Every turn is announced through a polite live region (the tile content on
  reveal, the outcome on the second tile, and the win message).
- A tile's accessible name tracks its state (face down / content / matched).
- Reduced motion is honoured: the scale-in reveal and colour fades are dropped
  while the state swaps still apply.

Like the other GROW components, the view calls `setReadyStatus()` itself.
