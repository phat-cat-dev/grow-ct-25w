# Journal card

One self-contained card combines the sketchbook heading, ruled textarea,
reflection prompts and completion/save action.

Include `journal-card.css`, copy `journal-card.html`, load `journal-card.js`,
then mount it:

```html
<script>
  JournalCard.mountJournalCard(document.querySelector('[data-journal-card]'));
</script>
```

No build, icon font, server or framework is required. Give each card a stable,
unique `data-journal-card` ID. Storage is namespaced by the page path and that
ID. `storageKey: null` disables browser saving; export remains available.
Changes are drafts until the learner presses Save. Storage failures are
reported without discarding the draft. JSON export includes the current text,
last-save timestamp and export timestamp; exporting does not save the draft.

Listen for `journal-card:change` (includes `dirty`) and `journal-card:save` to
integrate with a host. The mount returns `get()` and `destroy()`.

The `--journal-*` tokens inherit the existing surface, ink, accent, spacing and
font tokens, with standalone fallbacks. Textarea rules follow its line-height
and scroll with its content.

Browser saving is not encrypted, account-backed, or synced. Other scripts on
the same origin may access it. Do not use it for sensitive learner records.
It is not an LMS submission or a graded assessment.

Preview the card in the [textured asset gallery](../../backgrounds/textured/index.html)
or the [original lesson preview](../../../.dev/assets/gallery/preview.html).
