# adapt-grow-reflection-module

A **composed reflection activity** for the Adapt framework. Two things side by
side:

- a lined **sketchbook journal** — "develop your thought" — where the learner
  writes freely, and
- a **"change the lens"** panel of short reframing prompts that push them to see
  the thought differently.

On narrow screens the two columns stack, with the lens falling below the journal.
Part of the **GROW** plugin set, fully tokenised against the GROW theme (it
repaints with the active theme and spacing profile and has a dark mode for free).

## Built on the GROW journal

The writing half *is* the `adapt-grow-journal` field — same proven behaviour:
extends `ComponentModel` (not `QuestionModel`, so it stays outside scoring),
auto-grows, shows a character/word counter only near the limit, and **saves
automatically** (debounced + on blur) to `cmi.suspend_data`, not
`cmi.interactions`. Optionally completion-bearing in the `reflection` variant.
The lens prompts are static authored content with no state. This module adds the
sketchbook framing, the kicker, the caption and the lens panel around that field.

## The two blocks that are *not* tokenised

Everything is tokenised to GROW custom properties **except** two ruled "paper"
backgrounds — the sketchbook surface and the journal textarea. In each, the rule
spacing (`--rule-gap`) is the `line-height` the writing sits on, and the
`repeating-linear-gradient` draws the rules at that same gap; the sketchbook also
carries a vertical margin rule whose left padding is sized to clear it. They are
matched sets — splitting them, or swapping the gap for a unitless theme value,
would drift text off the lines — so each stays joined, as flagged in
`less/grow-reflection-module.less`.

## Accessibility

- The writing area is named via `aria-labelledby` (journal label → instruction →
  title → region fallback) and described by the status line.
- The counter is `aria-hidden`; thresholds and completion go through a polite
  live region, save failures through an alert.
- The lens is a labelled `group` containing a real list; the expand/complete
  controls are real `<button>`s with visible focus rings.

## Authoring

Add a `growReflectionModule` component. Key fields:

| Field | Purpose |
|---|---|
| `_kicker` | Small uppercase label above the sketchbook (blank = hidden). |
| `_journal.title` / `.icon` / `.label` | Heading, Material Symbol and field label for the writing card. |
| `_caption` | Optional note below the journal. |
| `_lens.title` / `.icon` / `._prompts[]` | The reframing panel. **Empty `_prompts` hides the aside** and the journal spans full width. |
| `_variant`, `_isCompletionBearing`, `_minCharacters`, `_maxCharacters`, `_rows`, `_maxRows`, `placeholder` | The journal's writing behaviour (see adapt-grow-journal). |

See `example.json` for a complete block, and
`adapt-content-templates/adapt-grow-reflection-module/` for ready-made modules.
To author one, use the `adapt-grow-reflection-module-agent` skill.

## Settings

`_component` must be `growReflectionModule`; the target attribute is
`_growReflectionModule`. Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
