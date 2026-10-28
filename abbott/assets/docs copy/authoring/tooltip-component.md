# Tooltips — `adapt-abbott-tooltip`

Inline vocabulary tooltips that work on **any text, in any component**. Built as
an Adapt **extension** (not a block component) so it enriches inline markup
wherever it appears, dependency-free (no Popper / Bootstrap JS / jQuery).

`src/extensions/adapt-abbott-tooltip/`

## Why an extension, not a component

A block component occupies the component slot; it can't sit inside a sentence. A
tooltip on a word is *inline*, so the behaviour loads globally and wires up any
marked term in any text field (text, narrative, accordion, …).

## Authoring — mark a term

In any HTML text field:

```html
<span class="cm-tooltip" data-cm-tip="A self-contained one-sentence definition.">
  epistemology
</span>
```

- The term gets a dashed underline (accent colour) and a help cursor.
- The definition shows on **hover**, on **keyboard focus** (the term is
  focusable), and on **tap** (touch).
- Keep the definition a self-contained sentence (voice spec 18): no contractions,
  no "it is when…".

## Behaviour

- One shared bubble (`role="tooltip"`), positioned by JS: above the term, flips
  below if there's no room, clamped inside the viewport (logic in
  `tooltipLogic.js`, unit-tested).
- Hover shows/hides; focus shows/hides; **click/tap toggles a pinned state** so
  touch users can open it and it stays open to read; **Escape** or an outside
  click closes it and returns focus to the term.
- Repositions on scroll/resize while open. Honours `prefers-reduced-motion`.
- a11y: focusable trigger + `aria-describedby` to the bubble while shown.

## Enable / disable

Enabled by default (zero-config). To turn off for a course, in `course.json`:

```json
"_abbottTooltip": { "_isEnabled": false }
```

## Styling

`less/tooltip.less` — trigger dashed underline (`--cm-accent`), dark-grey bubble
with white text (`--cm-dark-grey` / `--cm-white`), themed with the `--cm-*`
tokens so it follows the scheme system.

## Tests

`node --test src/extensions/adapt-abbott-tooltip/test/tooltipLogic.test.js`
covers placement: above/below flip, left/right clamp, wider-than-viewport, and
bottom-overflow clamp.
