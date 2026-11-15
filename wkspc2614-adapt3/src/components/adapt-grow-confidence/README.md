# adapt-grow-confidence

A **pre/post self-efficacy check** for the Adapt framework. The learner rates how
confident they feel against a short set of lesson outcomes — once before the
lesson and once after — and the post version shows how each rating moved, with
metacognitive feedback. It is a self-report, **not graded**.

Part of the **GROW** plugin set, tokenised against the theme (surface, ink,
hairline and accent tokens, plus `--confidence-before`/`--confidence-after` for
the chart), so it repaints with the active theme and has a dark mode for free.

## Behaviour

- **Two modes, paired by id.** A `pre` block and a `post` block share a
  `_selfAssessmentGroupId`. The pre carries the items and the rating scale; the
  post finds its pre by that id and inherits the same items and scale, so the two
  are identical.
- **Rate, then submit.** Each statement is a radio scale (five points by
  default, low to high). Submit is disabled until every statement is rated.
- **Pre** shows a confirmation message after submit. **Post** compares each
  statement's before and after rating, shows the movement (▲/▼/—) and a per-item
  feedback line chosen from the movement pattern, plus a summary and a forward
  hand-off, then a Chart.js before/after bar chart that echoes the list.
- **Standalone post.** If no pre ratings exist, the post shows a single-reading
  framing with no delta.
- Completes on submit. With `_recordInteraction` on (default) each rating is
  written to `cmi.interactions` as a likert self-report for cohort extraction.

## Accessibility

- Each statement is a `role="radiogroup"` labelled by its text; ratings carry an
  explicit `aria-label` ("…: label, N of M").
- On post submit, focus moves to the feedback region (a live region); the chart
  is `role="img"` with a label and is never the sole carrier of meaning — the
  exact numbers live in the per-item list. The chart degrades to nothing if
  Chart.js is unavailable, and honours reduced-motion.

## Authoring

| Field | Purpose |
|---|---|
| `_mode` | `pre` or `post`. |
| `_selfAssessmentGroupId` | Identical on the pre and post of a pair; the post keys off it. |
| `_items` | Authored on the **pre** only — each a can-do confidence statement with a stable `_id`. The post leaves this empty. |
| `_scale._labels` | Scale points, low to high (five by default); the stored value is the 1-based index. |
| `_feedback` | **Post** only. Five movement-pattern templates (`rose`, `stayedHigh`, `stayedLow`, `noMovement`, `dropped`), three `_summary` variants, a `_standalone` text and a `_forward` hand-off. `{{item}}` is available. |
| `_hasSummativeFollowing` | **Post** only. Picks the forward hand-off (assessment ahead vs. apply next). |
| `_preConfirmation` | **Pre** only. Shown after the pre is submitted. |
| `_itemFeedbackOverrides` | Optional per-item pattern wording, keyed by item `_id`. |
| `_recordInteraction` | Record ratings to `cmi.interactions` (default on). |

See `example.json` for a full pre block.

## Settings

`_component` must be `growConfidence`; the target attribute is `_growConfidence`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
