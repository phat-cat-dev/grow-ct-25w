# Textured learning assets

Each surface has its own HTML fragment and CSS file: lined, handwriting, quad,
dotgrid, graph, spiral, legalpad, indexcard, whiteboard, chalkboard, corkboard,
sticky-note and highlight. Include `tokens.css` plus your chosen stylesheet.
Spiral is a modifier: pair it with `lined.css`. Corkboard's example uses
`sticky-note.css`. Or include `textured.css` for all the static surfaces.

Open [index.html](./index.html) for the combined live preview, including the
[journal card](../../components/journal-card/README.md),
[scribble controls](../../components/scribble/README.md) and
[page header](../../header/README.md).
All components work on `file:` URLs or HTTP without a build.

## Surface tokens

Add `.textured` alongside the surface class. Neutral papers follow
`--surface-1`, `--ink`, `--line`, `--accent`, `--space-sm/md`, and font tokens,
with standalone fallbacks. Override `--texture-paper`, `--texture-ink`,
`--texture-rule`, `--texture-accent`, `--texture-pad`, `--texture-gap`,
`--texture-rule-gap` and `--texture-dot-gap` per component.
Material surfaces retain their own readable ink: `--texture-cork*`,
`--texture-sticky*`, `--texture-legal-*`, `--texture-index-*`,
`--texture-whiteboard-*`, and `--texture-chalk` / `--texture-slate`.
They do not force a global light/dark mode or import a font.

## Interactive notes board

Include `notes-board.css` and `notes-board.js`. The latter exposes
`TexturedNotes.mountNotesBoard(host, options)`. [notes-board.html](./notes-board.html)
is a runnable authoring example.

An activity defines an ID, title, labelled `groups` and authored `notes`.
Each note has `id`, `text`, `group`, optional `answer` and `colour`
(`yellow|pink|blue|brand`). For checking, specify `expectedGroup` and optionally
`expectedOrder` (1-based and contiguous within each target group).

- Authored notes cannot be edited/deleted; learner notes can be created, edited,
  coloured and deleted and are never scored.
- Move notes by dragging the Move handle, or use the labelled group menu with
  mouse, touch or keyboard. Earlier/Later buttons change order without dragging.
- Reveal answers in Learning mode. Testing mode requires an arrangement check
  before answers can be revealed. Changing arrangement closes answers and clears
  previous feedback.
- Remember toggles mark notes for review. “Things to remember” filters the view,
  not the scoring set. Creating a note clears the filter so the new note is visible.
- Checking scores authored notes by group and relative order of scored notes;
  unscored personal notes do not change the order score.
- Pin/move and flip use short, one-shot animations. Reduced motion and host
  `.no-motion` / `data-tm-no-motion="true"` skip them.

The mount returns `get()`, `load(progress)`, `check()` and `destroy()`.
`load` validates the entire progress record before replacing state.
Events: `notes-board:change`, `notes-board:check` (score/total/per-note results).
Pass `onChange(progress)` to integrate another store.

Browser storage defaults to `grow-notes:<page path>:<activity ID>`.
Use a distinct activity ID when changing content; use `storageKey: null` to
disable saving. Storage failures are visible and keep current notes usable.
JSON export is a portable progress record; authored answer text and scoring
criteria are not included. Use `load(JSON.parse(fileText))` in a host importer.
Authored note text always comes from current activity configuration on restore.

This is client-side practice, **not secure assessment**: authored answers and
criteria are inspectable in source. Nothing is submitted to an LMS. Browser
storage is neither encrypted nor synced and other same-origin scripts may read
it. Do not store sensitive records; exported reflections may be personal.
No learner data is sent anywhere by these scripts.

## Sequential dots and typing chat

`sequential-dots.html/css` contains exactly three circles, appearing in order,
once. No writing paths. `--dot-step` sets delay spacing, `--dot-colour` the ink;
add/re-add `is-playing` to replay. Reduced motion shows all three immediately.

`typing-chat.html` demonstrates `TexturedChat.mountTypingChat(host, { messages })`.
Messages are `{ speaker: 'guide'|'learner', text }`. The UI explicitly labels this
as a **scripted** conversation, not a live agent. Next reveals a three-dot
indicator then typed text; Show full message finishes immediately; Replay
resets. Nothing auto-plays or loops. The text is announced as a complete message,
not character by character. Reduced motion reveals complete text immediately.
The mount returns `next()` and `destroy()` and emits `typing-chat:message`.
No model, network or remote chat service is connected.
