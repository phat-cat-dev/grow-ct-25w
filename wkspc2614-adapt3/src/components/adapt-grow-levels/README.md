# adapt-grow-levels (GROW)

Tiered levels introduced one at a time. Level 1 opens on load; opening a level
shows it in full, highlights it, and unlocks the next. Each open level offers an
on-demand **"In practice"** advice pop-out for students. The component completes
once every level has been opened (so it satisfies a trickle step).

Built for the AI pathway's "three categories of AI use" (Cardiff Met), but generic:
any set of tiered levels works.

## Authoring

```json
{
  "_component": "growLevels",
  "displayTitle": "The three categories of AI use",
  "body": "<p>Open each level to see what it allows.</p>",
  "instruction": "Select a level to open it, then open the next.",
  "_setCompletionOn": "allOpened",
  "_items": [
    { "_tone": "restricted", "title": "Category 1: No AI expected", "body": "…", "advice": "In practice: …" },
    { "_tone": "guarded",    "title": "Category 2: AI acknowledged", "body": "…", "advice": "In practice: …" },
    { "_tone": "open",       "title": "Category 3: AI embedded", "body": "…", "advice": "In practice: …" }
  ]
}
```

- `_tone`: `restricted` (red), `guarded` (amber), `open` (green), `neutral` (brand blue).
- `advice`: optional; shows an "In practice" pop-out on the open level.

Like the other GROW components, the view calls `setReadyStatus()` itself.
