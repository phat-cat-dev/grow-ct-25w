# adapt-grow-journal

A **lined "notebook" journal** for the Adapt framework — a ruled, paper-like
text field where a learner writes freely. It has **no correct answer**: use it
for reflective prompts, a running set of notes, or any "write what you think"
moment.

Part of the **GROW** plugin set. It is the GROW-styled sibling of an open-text
input — same component structure as a reflective text component, dressed as a
ruled journal page and fully tokenised against the GROW theme, so it repaints
with the active theme and spacing profile and has a dark mode for free.

## Not a question

Like its open-text sibling, the journal extends `ComponentModel`, **not**
`QuestionModel` — it stays entirely outside the scoring machinery. Writing is
persisted via `offlineStorage` custom keys into **`cmi.suspend_data`**, not
`cmi.interactions`, which avoids the 250-character truncation and the false
`result: incorrect` you'd get from routing prose through an interaction.

## What the learner sees

- A ruled textarea that looks like a notebook page. **Each line of writing lands
  on a printed rule** — the rule spacing *is* the line-height.
- The field **auto-grows** as they type, up to `_maxRows`, then scrolls; the
  ruled lines scroll with the text.
- A corner **expand/collapse** button to pre-open the page before writing.
- A character (or word) **counter** that appears only as they approach the limit,
  and a polite warning if they go over.
- Writing **saves automatically** (debounced, and on blur); a status line
  confirms it, or warns assertively if a save ever fails.
- Optional **Mark as complete** button for the reflection variant.

## The one block that is *not* tokenised

Everything is tokenised to GROW custom properties **except** the coupled
line-height and ruled background in `.grow-journal__textarea`. The rule spacing
(`--rule-gap`) is the textarea's `line-height`, and the `repeating-linear-gradient`
draws the rules at that same gap. They are a matched pair — splitting them, or
swapping the line-height for a unitless theme value, would drift the writing off
the lines — so they stay joined, and the top padding is kept equal to the
background offset. This is called out in a comment in `less/grow-journal.less`.

## Accessibility

- The textarea has an accessible name via `aria-labelledby` (body → instruction →
  title → region fallback) and `aria-describedby` to the status line.
- The counter is `aria-hidden` (never announced on keystrokes); thresholds and
  completion go through a polite live region; save failures through an alert.
- Real `<button>` controls with visible focus rings.

## Variants

| `_variant` | Use | Completion |
|---|---|---|
| `reflection` (default) | reflective prompts | may be completion-bearing (`_isCompletionBearing`) |
| `notes` | general note-taking | never completion-bearing |

## Settings

`_component` must be `growJournal`; the target attribute is `_growJournal`.
See `example.json` for a full block. Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
