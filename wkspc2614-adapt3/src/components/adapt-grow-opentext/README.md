# adapt-grow-opentext

A **general-purpose open-text input** for the Adapt framework — a plain text
area where a learner writes freely in response to a prompt or jots notes. It has
**no correct answer**: use it for reflections, running notes, or any "write what
you think" moment.

Part of the **GROW** plugin set, tokenised to the GROW theme (it uses
`--ab-base-accent`, `--ab-base-ink-muted`, `--ab-danger`/`--ab-success` tokens,
so it repaints with the active theme and has a dark mode for free). This is the
unstyled base sibling of `adapt-grow-journal`, which is the same component
dressed as a ruled notebook page.

## Not a question

The component extends `ComponentModel`, **not** `QuestionModel` — it stays
entirely outside the scoring machinery. Writing is persisted via
`offlineStorage` custom keys into **`cmi.suspend_data`**, not `cmi.interactions`,
which avoids the 250-character truncation and the false `result: incorrect` you
would get from routing prose through an interaction.

## What the learner sees

- A text area that **auto-grows** from `_rows` up to `_maxRows`, then scrolls.
- A corner **expand/collapse** button to pre-open the area before writing.
- A **counter** that works in characters or, when `_maxWords` is set, in words;
  it appears as the learner approaches the limit, with a polite over-limit
  warning.
- Writing **saves automatically**; a status line confirms it, or warns
  assertively (via an `alert` region) if a save ever fails.
- An optional **Mark as complete** button (reflection variant only).

## Accessibility

The text area is named via `aria-labelledby` (to the rendered body/instruction)
and `aria-describedby` to the status line. The counter is `aria-hidden` (never
announced on keystrokes); thresholds and completion go through a polite live
region, and save failures through an `role="alert"`. Controls are real
`<button>`s. All learner-facing strings are translatable schema globals.

## Authoring

| Field | Purpose |
|---|---|
| `instruction` | Optional guidance above the text area. |
| `_variant` | `reflection` (may be completion-bearing) or `notes` (never completion-bearing). |
| `placeholder` | Empty-state text; falls back to a variant default. |
| `_maxCharacters` | Soft character limit (default 4000); also the suspend_data backstop. |
| `_minCharacters` | Minimum characters before completion is allowed. |
| `_maxWords` / `_minWords` | Switch the counter and gate to **words** instead of characters. |
| `_isCompletionBearing` | Reflection only: shows "Mark as complete" and contributes to lesson completion. |
| `_rows` / `_maxRows` | Initial and maximum height (in rows) before internal scroll. |

See `example.json` for a full block.

## Settings

`_component` must be `growOpentext`; the target attribute is `_growOpentext`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
