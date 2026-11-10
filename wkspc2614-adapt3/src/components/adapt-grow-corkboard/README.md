# adapt-grow-corkboard

A **cork-board of sticky notes** for Adapt. Two board types:

- **display** — static notes you author (text), pinned at a gentle angle. Good for a
  brainstorm, reflection prompts or lesson takeaways.
- **brainstorm** — each note shows a **title you set** and the **learner types their own
  answer** into it (a term, a definition, a question, an example). Entries are **saved**
  (offline storage / suspend data) and the component **completes** once enough notes are
  filled.

Notes are **square**, laid out as a balanced, centred grid. Colour is a **role**, not
decoration. Componentised from the Abbott `cork-board` surface.

## Authoring

```json
{
  "_component": "growCorkboard",
  "_mode": "brainstorm",
  "_count": 4,
  "_minComplete": 0,
  "_notes": [
    { "title": "Key term",        "_placeholder": "A term you met…",       "_color": "default", "_rotation": -2 },
    { "title": "A definition",    "_placeholder": "In your own words…",    "_color": "blue",    "_rotation": 1.5 },
    { "title": "A question",      "_placeholder": "What do you still ask?","_color": "pink",    "_rotation": -1 },
    { "title": "An example",      "_placeholder": "A concrete example…",   "_color": "green",   "_rotation": 2 }
  ]
}
```

| Field | Meaning |
|---|---|
| `_mode` | `display` (static `text` notes) or `brainstorm` (learner fills titled notes) |
| `_count` | notes shown: `1 2 3 4 6 8`, as a centred grid (4 = 2×2, 6 = 3×2, 8 = 4×2). First N of `_notes`. |
| `_minComplete` | brainstorm only: notes the learner must fill to complete (`0` = all shown) |
| `text` | **display**: the note — short, one idea, simple inline HTML allowed |
| `title` | **brainstorm**: the heading the learner answers under |
| `_placeholder` | **brainstorm**: faint hint in the empty input |
| `_color` | a role: `default` (a thought) · `pink` (a question) · `blue` (a next step) · `green` (done/agreed) · `amber` (caution) · `brand` (emphasis — soft purple) |
| `_rotation` | a tilt in degrees (≈ -3…3). Omit for an automatic small jitter. |

Ready-to-paste fragments: `adapt-content-templates/adapt-grow-corkboard/`; authoring skill
`adapt-grow-corkboard-agent`.

## Persistence (brainstorm)

Learner entries save via `offlineStorage` into `cmi.suspend_data` (keyed by component id),
restored at `adapt:start` — the same mechanism as `adapt-grow-opentext` (outside the scoring
machinery; no `cmi.interactions`). Without an LMS the notes are editable in-session but do not
persist across sessions. Completion is sticky.

## Theme alignment

Padding rides `--space-*`; the fixed sticky hues (pink/blue/green/amber + the soft purple
brand) and the cork texture are intentional constants. Hover/focus gently straightens a note
(reduced-motion safe); a note being typed into is not scaled.
