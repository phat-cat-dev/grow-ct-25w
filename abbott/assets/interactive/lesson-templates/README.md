# Lesson interactivities

Open [the gallery](index.html), or use any of the six HTML pages individually.
No server, fonts, frameworks or network requests are required.

- **Journey:** progressively reveals three stages, completion meter and restart.
- **Maker:** independent station checklists.
- **Studio:** live hue control and colour swatches.
- **Notebook:** selectable thinking prompts that never overwrite notes.
- **Board:** ordered reveal of water-cycle explanations, with reset.
- **Editorial:** selectable reading lenses.

Every page reuses the [journal card](../../components/journal-card/README.md)
for explicit browser-only Save, restore and JSON export. Notes are not encrypted.
Storage errors are displayed on the card. Controls and completion progress are
session-only and reset on reload; only explicitly saved notes persist.
Completion is self-reported, not automatically graded.

## Reuse

Use a page directly or in an iframe for complete style isolation. To embed markup,
copy its `[data-lesson]` wrapper and include the three stylesheets and two classic
scripts shown in the page, adjusting relative paths. `template-layout.css` includes
global foundation styles, so iframe embedding is preferred on an existing site.
Load scripts after markup. Give each journal a unique `data-journal-card` ID when
placing multiple copies on the same page.

The layouts use the existing theme tokens, including `--h`, `--s`, `--accent`,
`--ink`, `--surface-1`, `--space-scale` and `--type-scale`. Override them on the
lesson wrapper. Set `data-theme="light"` or `"dark"` on the document element;
otherwise the operating-system preference applies.

Run `node .\assets\interactive\lesson-templates\build-templates.cjs` from the
workspace root to regenerate pages and the layout stylesheet from the archived
template gallery. Edit the generator rather than generated HTML. The original
gallery is left unchanged.
