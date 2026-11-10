# adapt-grow-flipcard

A **grid of two-sided flip cards** for the Adapt framework. Each card shows a
front face (a prompt, image or term); selecting it turns the card over to reveal
the back. Use it for predict-then-check, term/definition, or claim/verdict pairs.

Part of the **GROW** plugin set. Its surfaces, accent and verdict colours come
from the theme's `--ab-*` tokens, so it repaints with the active theme and has a
dark mode for free.

## Behaviour

- **Select to flip.** A card toggles between its front and back face on click.
- **Flip behaviour** (`_flipBehaviour`): `independent` lets cards flip and stay
  flipped on their own; `single` closes any other open card when one is turned.
- **Optional randomised order** (`_isRandomised`) shuffles the cards each time
  the component is shown.
- **Verdict tone** (`_variant` per card): `positive` shows a green tick on the
  back, `negative` a red cross, `neutral` (default) neither.
- **Completes on view** — marked complete when the component scrolls into view,
  so it passes the trickle without every card being turned.

## Accessibility

- Each card is a native `<button>` with `aria-expanded` reflecting the flip
  state; its accessible name is the **front title** (stable — it does not swap on
  flip).
- Both faces are always in the DOM; the hidden face is `aria-hidden`. Focus does
  not move on flip, and operation is plain native-button keyboard semantics
  (Tab / Enter / Space).

## Authoring

| Field | Purpose |
|---|---|
| `instruction` | Instruction text shown below the body. |
| `_flipBehaviour` | `independent` or `single`. |
| `_isRandomised` | Shuffle the card order on each view. |
| `_items` | The cards. Each has a `front` (at least one of `title`, `body`, `_graphic`), a `back` (at least one of `title`, `body`), an optional `_variant` tone and an optional `_id`. |

See `example.json` for a full block.

## Settings

`_component` must be `growFlipcard`; the target attribute is `_growFlipcard`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
