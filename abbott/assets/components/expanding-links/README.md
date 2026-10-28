# Expanding icon links

## Learning sequences

[Open the learning-step demo](learning.html): inquiry (4 steps), guided practice
(5) and reflection/transfer (3). Plain numbered buttons expand their label on
hover/focus and for the current step. No surrounding cards or content boxes.
Only the current activity is shown after mounting; without JavaScript all
authored activities remain visible.

The workshop's **Number of steps** control supports 1–10. Extra steps use
placeholder prompts for your own activities. Reducing the count keeps removed
steps' notes and completion in memory; increasing it restores them. Each preset
keeps its own count and progress until reload. Add up to ten sections to the
reusable HTML fragment to author a full ten-step sequence.

Include `expanding-links.css`, `learning-sequence.css` and
`learning-sequence.js`, paste [learning.template.html](learning.template.html),
then call `LearningSequence.mount(element)`.
Add/remove labelled `data-learning-step` sections; step buttons are generated
from `data-label`. Keep labels short. Mount after authoring the step count.

Back/Next only navigate. Completion is an explicit learner action, not a score
or assessed result. Every step is freely accessible. Revisiting keeps content
and input values. The workshop also retains each preset's notes and completion
in memory when switching; reload clears everything. No storage, LMS reporting,
timers or locking are involved.

API: `player.go(index, focusHeading)`, `player.get()`, `player.reset()`,
`player.destroy()`. Indices are zero-based. Reset clears completion and returns
to step 1 but preserves form values. `learning-sequence:change` and
`learning-sequence:progress` bubble with `{index,total,completed}`; completed
contains indices. Destroy restores originally hidden/visible activities and
original nav children. Use normal mounting again to start fresh.

Step buttons keep focus when clicked; Back/Next focus the new activity heading.
All buttons are in normal Tab order. Current step uses `aria-current="step"`;
completed buttons include an accessible completion label and a visible check.
Reduced-motion and mobile label behaviour are shared with the icon-link demo.

## Icon-link component

[Open the demo](index.html) or paste [the nav fragment](nav.template.html)
alongside `expanding-links.css`. No JavaScript is needed for the component.
Original CSS and simple SVG line artwork, inspired by the general expanding
navigation idea in [Jhey's grid-template links](https://codepen.io/jh3y/pen/MWBmmxb).
No reference code or artwork was copied.

Each link shows an icon at rest. Its visual label expands on hover or keyboard
focus, and also for `aria-current="page"`. Touch/coarse-pointer and narrow
screens show all labels. Set `data-labels="always"` on the nav to always show
them on desktop too. The demo's small script only operates preview controls.

Replace fragment destinations with real page URLs or existing section IDs.
Use links for navigation, not fake action buttons. A stable `aria-label` names
each link; the decorative SVG and visual label are hidden from screen readers
to avoid duplication. Update both the accessible and visible labels together.
The fragment's destination sections must be supplied by the consuming page.

Tokens: `--expand-accent`, `--expand-ink`, `--expand-duration` (300 ms default).
Focus outlines remain visible, navigation wraps, and system/host reduced-motion
preferences disable transitions. No panel, tile background or border surrounds
the links. Labels use intrinsic widths; keep them reasonably short.
