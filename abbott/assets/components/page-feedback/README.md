# End-of-page feedback cards

Open [the design gallery](index.html). Three original variants:

- [Conversation](conversation.html): overlapping message bubbles and a quiet resource footer.
- [Growth](growth.html): a sprouting illustration and a lesson-focused treatment.
- [Field note](fieldnote.html): a compact notebook illustration for reference pages.

Each has a standalone HTML preview, `.template.html` fragment and original SVG
illustration. These are new designs, not reproductions of MDN's illustration,
branding or footer markup.

## Interaction and privacy

Choose a useful/not-useful response, optionally enter a note, then download a
JSON response. Choices can be changed without losing the note; Clear resets the
whole response. The page does not send feedback, use browser storage or contact
any external service. Reload discards drafts. Download does **not** submit.
Contribution links point to this guide until an author configures real channels.
The displayed date is the template revision, not a claim about your page's update.

## Reuse

Copy a `.template.html` fragment into your article footer and include
`page-feedback.css` and `page-feedback.js` after markup. Give the section and its
heading unique IDs when embedding multiple copies of a variant. Replace the
title, prompts, contribution links and revision details with your real content.
Adjust or remove the local template/illustration download links when embedding.

The component CSS is scoped to `.feedback-card`; `.feedback-demo*` rules style
only the standalone gallery. No fonts, frameworks or network requests are needed.
There is no motion, so no reduced-motion exception is necessary.

Tokens inherit the existing theme:

| Component token | Host token / fallback |
| --- | --- |
| `--feedback-paper` | `--surface-1` / system light-dark surface |
| `--feedback-ink` | `--ink` / readable text |
| `--feedback-muted` | `--ink-soft` / muted text |
| `--feedback-line` | `--line` / border |
| `--feedback-accent` | `--accent` / variant accent |
| `--feedback-radius` | `--radius` / variant corners |
| `--feedback-pad` | `--space-md` / fluid padding |

Inline illustrations inherit the accent and paper colours; standalone SVG files
use currentColor and a white paper fallback. Set `color-scheme: light dark` on
your host if you want the system-aware fallback colours.

`page-feedback:change` and `page-feedback:export` bubble with
`{ version, cardId, page, response, note }`; exports include `exportedAt`.
These events do not submit anything. A production feedback service requires its
own consent, validation, delivery and error handling.
Dynamic content can call `PageFeedback.mount(element)`, returning `get()` and
`destroy()`. Do not mount a card twice.

Regenerate previews, fragments and illustrations with:

```powershell
node .\assets\components\page-feedback\build-feedback.cjs
```

Edit the generator rather than generated HTML/SVG files.
