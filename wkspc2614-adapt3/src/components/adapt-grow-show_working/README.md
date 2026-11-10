# adapt-grow-show_working

**"Show your working"** for the Adapt framework — a worked solution revealed one
line at a time. Each step rises in with the move explained in a hand-written
margin note, and the final answer is checked by substitution with a tick that
draws on.

Part of the **GROW** plugin set, fully tokenised against the GROW theme (it
repaints with the active theme, paces off the theme motion knob `--flow-rate`,
and has a dark mode for free). Maths is the obvious use, but any ordered
derivation — a proof, a method, a chain of reasoning — fits.

## Presentation, not a question

There is no learner input and no scoring. The component uses the stock
`ComponentModel`; the view plays the reveal when the component scrolls into view
and marks it complete as seen. A **Replay** button re-runs it.

## Behaviour

- **Readable at rest.** Every line is present and in order before, during and
  after any animation — the reveal is decoration over an ordered list.
- **Staggered reveal.** Lines arrive in turn, `_working._stagger` seconds apart,
  the whole thing paced by the theme's `--flow-rate`.
- **The tick draws on** on a check line (a `stroke-dasharray` draw keyed to
  `pathLength="1"`).
- **Quiet under reduced motion.** With `prefers-reduced-motion: reduce` nothing
  animates, the working simply sits there, and the Replay button is hidden.

## The block that is *not* tokenised

Everything is tokenised to GROW custom properties **except** the animation
mechanism — the reveal paced by `--flow-rate` and staggered by each line's `--d`,
and the check-mark draw, which depends on a `stroke-dasharray`/`stroke-dashoffset`
pair normalised by `pathLength="1"` on the path. Those move together, so they are
kept as a coupled set, flagged in `less/grow-show_working.less`.

## Authoring

Add a `growShowWorking` component and fill `_working._steps` — an ordered list of
`{ eq, ann?, _isCheck? }`:

| Field | Purpose |
|---|---|
| `eq` | The line. Wrap a substituted value in `<mark>` to highlight it, e.g. `2(<mark>4</mark>) + 6 = 14`. |
| `ann` | The move explained, in the hand-written style (optional). |
| `_isCheck` | Draws the verification tick — use on the final line. |
| `_working._stagger` | Seconds between lines (default 0.3). |
| `_kicker` | The small mono label above the title. |

See `example.json` for a full block, and
`adapt-content-templates/adapt-grow-show_working/` for ready-made workings. To
author one, use the `adapt-grow-show_working-agent` skill.

## Accessibility

The steps are an ordered list that reads correctly at rest; the tick SVG is
`aria-hidden` and a visually-hidden phrase ("this checks out") carries the
verification to screen readers. The Replay control is a real `<button>` with a
visible focus ring.

## Settings

`_component` must be `growShowWorking`; the target attribute is `_growShowWorking`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
