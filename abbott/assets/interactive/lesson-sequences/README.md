# Sequential lesson templates

Six spatial compositions extracted from the studio lesson experiments:
guided field notes, workshop canvas, story scenes, casebook, expedition route
and reflective studio.

Open [the template index](index.html) or the dedicated
[sequential reveal playground](sequential.html).
Each composition has a standalone page and a `.template.html` fragment.
Media and Adapt-plugin placeholders remain labelled; they are authoring slots,
not implemented learning activities. Replace demonstration text with your lesson.

## Reveal behaviour

- **On completion:** first stage starts open; completing a stage fades in and
  opens the next. Earlier stages remain collapsible and available.
- **Timed trickle:** press Start to reveal one stage every 0.5–8 seconds.
  Pause/resume never clears content. Timers do not award completion, steal focus
  or hide existing stages. Completion buttons must still be used in order.
- Changing mode preserves revealed stages and completion.
- Restart resets progress and visibility, **not notes**.
- Switching compositions pauses inactive timers and preserves drafts in the
  current page. A backgrounded page pauses trickle until resumed manually.
- Reduced motion reveals immediately without fading; timing remains unchanged.
- Completion is self-reported practice unless an integrated activity supplies
  its own completion signal. This is not secure assessment or LMS tracking.

## Reuse and activity integration

Load `sequence.css`, `lesson-layouts.css`, the journal card stylesheet, then
`journal-card.js` and `sequence.js` after your fragment. Adjust the relative paths
shown in each standalone page. The foundation stylesheet includes document-wide
rules; use an iframe for isolation within an existing application.

Page/article/block/component classes are retained. Standalone headings are
promoted to H1/H2/H3 and component heading level 4, rather than workbench H4–H7.
There are no external fonts or network requests.

`sequence.js` auto-mounts `[data-lesson-template]`. Dynamically inserted fragments
can use `LessonSequence.mount(element)`. Use unique DOM IDs and journal IDs when
embedding multiple copies of the same composition.

```js
const lesson = document.querySelector('[data-lesson-template]');
// Dispatch only when the corresponding activity genuinely finishes.
lesson.dispatchEvent(new CustomEvent('lesson:complete', {
  detail: { step: 0 } // zero-based, in-order, revealed stage
}));
const sequence = LessonSequence.get(lesson);
sequence.get();       // completed, revealed, total, mode, running
sequence.pause();
sequence.restart();   // preserves notes
// sequence.complete(0); // throws for invalid or out-of-order completion
// sequence.destroy();   // cancels timer/listeners and unmounts journals
```

Invalid event completions display an explicit error. Duplicate completion of an
already completed stage is harmless. Events `lesson-sequence:reveal` and
`lesson-sequence:progress` bubble with current progress details.

Theme tokens include `--accent`, `--ink`, `--surface-1`, `--surface-2`, `--line`,
`--ab-space-item-margin`, `--ab-space-item-padding` and
`--lesson-fade-duration`. System light/dark mode applies by default.
The existing journal card handles explicit browser Save, restore and JSON export;
notes are not encrypted. Only saved notes persist after reload, not progress.

Regenerate layout CSS, pages and fragments with:

```powershell
node .\assets\interactive\lesson-sequences\build-lessons.cjs
```

Edit the generator rather than generated HTML. The original studio is unchanged.
