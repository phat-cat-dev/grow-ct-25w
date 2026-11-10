# adapt-grow-branching

A **branching decision scenario** for the Adapt framework — a short interactive
case the learner walks one choice at a time. Each node is either a *decision*
(read the situation, pick a response) or an *outcome* (an ending). After a choice,
its consequence is shown before the learner continues, so the move's wisdom is
revealed by what happens next rather than by labelling the options.

Part of the **GROW** plugin set and partly tokenised to the GROW theme: the
selected, continue/restart and focus-ring states draw on the theme's accent
tokens (`--ab-base-accent`, `--ab-base-accent-ring`). The neutral choice greys
and the good/poor outcome colours are deliberately kept literal.

## Behaviour

The template renders only the model's **current node** in one of three states:

- **decision** — the node body plus its choices as buttons.
- **consequence** — after a choice, "You chose: …", the consequence text, and a
  **Continue** button.
- **outcome** — an ending's body, styled `good` / `poor` / `neutral`, with a
  **Start over** button.

A step counter is shown on decision/consequence nodes. On each state change focus
moves to the newly revealed consequence or outcome region (a `role="status"`), so
keyboard and screen-reader users land on the new content. The choice reveal
animation is dropped under `prefers-reduced-motion: reduce`.

## Authoring

A scenario is a `_start` node id plus a `_nodes` map. A node has a `body` and
**either** `_choices` (a decision) **or** `_outcome` (an ending).

| Field | Purpose |
|---|---|
| `instruction` | Instruction shown above the scenario. |
| `_scenario._start` | The id (a key in `_nodes`) to begin at. |
| `_scenario._nodes` | Map of node id → node. |
| node `body` | The situation (decision) or ending text (outcome). |
| node `_outcome` | `good` / `poor` / `neutral` — makes the node an ending. |
| node `_choices[]` | 2–4 choices, each with `text`, a `consequence` and a `_goto` (next node id). |

See `example.json` for a full block.

## Settings

`_component` must be `growBranching`; the target attribute is `_growBranching`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
