# adapt-grow-tutor

A lesson-guide **course tutor** for Adapt. It lists the page's sections, tracks where the
learner is as they scroll, and **speaks** — publishing guidance to the shared GROW
**notification bar**. Derived from the Abbott `course-agent` prototype; wired to the
standalone `notifications` service so the tutor's output appears as live, dismissible messages.

> Prototype guide — no AI service is connected. Hints are authored, not generated.

## The notifications link

This is the point of the component: the tutor **outputs to the notification service**.

```
TutorView.say(message)  →  notifications.publish({ message, source: tutorName, level })
                        →  the mounted notification bar shows it (info / success / error),
                           with history (back / forward) and a 10s auto-hide.
```

- The `notifications` module (`js/notifications/`) is the **shared singleton** —
  `Symbol.for('grow.notification-service')`. Any other GROW tool on the page (spacing
  manager, theme manager, …) publishes to and reads from the **same** bar, so the tutor's
  voice and tool messages share one display.
- The bar is mounted once per component into `.grow-tutor__bar`, sized to the tutor **rail**.

## When the tutor speaks

- **On appear** — the `greeting` (as a `success` message).
- **As you scroll** — each section's hint from `_messages` (article id → text), spoken once
  when that section reaches the middle of the screen.
- Programmatically — `view.say('…', 'info' | 'success' | 'error')`.

## Authoring

```json
{
  "_component": "growTutor",
  "_tutor": {
    "name": "Ada",
    "intro": "I'll point you to each part of this lesson.",
    "greeting": "Welcome. Start with the overview, then work down.",
    "_showGuide": true,
    "_messages": {
      "a-05": "This section sets up the problem — read it first.",
      "a-10": "Here's where it gets practical. Try the activity."
    }
  }
}
```

| Field | Meaning |
|---|---|
| `name` | tutor name — the rail label and the **source** of each notification |
| `intro` | a short line under the rail |
| `greeting` | published to the bar when the component appears |
| `_showGuide` | list the page's sections as links that highlight on scroll |
| `_messages` | map of **article id → hint**, spoken once as that section reaches centre |
| `_sections` | fallback section list (id + title) when the page has no articles to read |

The section list is read from the real page DOM (`.article[id]` + `.article__title`); links
scroll to the section. Current section tracking uses an `IntersectionObserver`.

## Theme alignment (tokenisation)

The panel + bar CSS was tokenised from the tool's `--tm-*` set onto GROW tokens:
`--tm-ink → --ink`, `--tm-line → --line`, `--tm-surface → --surface-1`,
`--tm-raised`/`--tm-source → --surface-2`. So the tutor reskins with the course.

- The bar's nav buttons use Material Symbols ligatures (`arrow_back`/`arrow_forward`); with
  no symbol font loaded they fall back to short text labels (SCORM-offline — no Google Fonts).

## Layout

```
js/adapt-grow-tutor.js   registration
js/TutorView.js          the view — builds the guide, mounts the bar, publishes
js/notifications/        the vendored shared service (service · bar · history)
less/grow-tutor.less     panel + bar, tokenised
templates/growTutor.jsx  properties.schema  example.json  bower.json
```

GPL-3.0. Lineage: `inbox/abbott-tools/{course-agent, notifications}`; source of record in
`adapt-docs/adapt_abbdev/components/adapt-grow-tutor/source/`.
