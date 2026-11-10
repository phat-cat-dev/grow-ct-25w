# adapt-grow-guided-chat

A **scripted learning conversation** for the Adapt framework. A short dialogue
between a *guide* and a *learner* is revealed one message at a time with a
gentle typing effect — like watching a tutorial conversation replay itself.

There is no live agent and no AI at runtime: the conversation is **authored
content**. Use it to model a line of thinking — a worked reflection, a
Socratic question-and-answer, a "here's how an expert talks through this"
moment — where seeing the exchange unfold beats reading it as a block of prose.

Part of the **GROW** plugin set. Its styling is fully tokenised against the
GROW theme (`--surface-1`, `--line`, `--accent`, `--ink`, `--space-*`), so it
repaints with the active theme and spacing profile and has a dark mode for
free.

## What the learner sees

- Guide and learner messages as alternating bubbles (learner indented, tinted
  with the theme accent).
- Each message **types itself out**, then waits.
- **Next message** reveals the following line; **Show full message** skips the
  typing on the current one; **Replay conversation** restarts from the top.
- A polite live region announces each full message, so the pace never hides
  content from assistive tech.

## Accessibility

- The **full text of every message is always in the DOM** for screen readers
  (a visually-hidden `__sr` span); the typing animation is purely visual and
  `aria-hidden`.
- Honours `prefers-reduced-motion` and the GROW `no-motion` flag: each message
  appears **in full at once**, with no caret, and the controls still work.
- Controls are real `<button>`s with a ≥2.75rem touch target and a visible
  focus ring.

## Authoring

Add a `growGuidedChat` component and fill `_chat._messages` — an ordered list of
`{ _speaker: "guide" | "learner", name?, text }`. See `example.json`.

| Field | Purpose |
|---|---|
| `_chat._messages` | The conversation, in order. |
| `_chat.guideName` / `learnerName` | Default speaker names. |
| `_chat._typeSpeed` | Milliseconds per character (lower = faster). |
| `_chat._autoAdvance` | Play straight through instead of waiting for *Next*. |
| `_chat._labels` | Override the three control labels. |

Ready-made conversations live in
`adapt-content-templates/adapt-grow-guided-chat/`. To **write** one, see the
`adapt-grow-guided-chat-agent` skill in
`adapt-grow-agents/adapt-grow-guided-chat/`.

## Settings

`_component` must be `growGuidedChat`; the target attribute is
`_growGuidedChat`. Requires Adapt framework `>=5.19.1` (React templates).

## License

GPL-3.0, consistent with the Adapt framework.
