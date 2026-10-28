# Page templates

[`page-templates.json`](./page-templates.json) is the initial, data-only catalog
of the six Adapt page archetypes in the portable specification. It records page
order, article phases, block-role slots, and the lesson-specific gating and
assessment markers.

[`lesson-page.html`](./lesson-page.html) is a standalone, ordinary HTML starter
for the lesson archetype. It shows the five-article lesson spine, Adapt-style
page/article/block/component hooks, example objective metadata, and placeholder
content for the core lesson slots. It is intended for authoring and review before
the structure is expressed as JSX.
Its `.frontmatter` role classes and `data-grow-role` hooks follow the existing
Adapt markup and GROW selectors in [`grow/templates/`](../../../grow/templates/)
and [`grow/less/grow-lesson.less`](../../../grow/less/grow-lesson.less).

This catalog is a generator input, not an importable Adapt course. A renderer
still needs to materialize unique `_id` and `_parentId` values, assign
course-wide `_trackingId` values, and populate content and component fields.
Component routing remains a separate step; the catalog does not select or
author components. The HTML file is a static starter rather than an Adapt
runtime template; its sample component markup must be replaced with actual
component output when it is generated into a course.

## Lesson navigation preview

The HTML lesson starter now mounts [lesson-nav.js](./lesson-nav.js) using the
shared [nav fragment](./nav-template.html) and [navigation styles](./lesson-nav.css).
Serve the repository root over HTTP, for example:

```powershell
python -m http.server 8767 --bind 127.0.0.1 --directory E:\workspace-26ux-25\gro\grow-ct-main
```

Open <http://127.0.0.1:8767/tools/grow-context/templates/lesson-page.html>.
The content-only JSX and Handlebars lesson templates remain usable without the
preview shell. Their host can call `mountLessonNav(host, { lesson, authoring })`
after rendering, and call the returned controller's `destroy()` on unmount.
The matching nav YAML/JSX describe the same button groups and status keys.

The page header uses the shared borderless Dots hero, not an inner card. It is
a full-width band whose background sits very close to the host page colour and
fades into it at the bottom. With the Theme Manager mounted, the hero reads the
live `--tm-bg`, `--tm-ink`, `--tm-muted` and `--tm-accent` values, so it follows
colour and light/dark changes. Front matter
remains inside the existing page body. The HTML starter includes the hero CSS
and behaviour. The lesson hero has no Play/Pause button: it is marked
`data-hero-playing="true"`, so the swirl runs unless reduced motion or the
host no-motion setting is on. JSX/Handlebars hosts must also include those shared
assets and load `heros.js` after rendering; Adapt runtime wiring is separate.

- The bordered, tinted screen is geometrically centred on wide screens. On
  narrower screens it occupies a centred second row. The screen holds only the
  readout: Previous/Next section keys flank it, with the Alerts key on the
  right (Google Material Symbols). The location view is the default and has no
  key; pressing the active Alerts key again returns to it. Pressed state
  identifies the selected view. Symbols require the Google font
  connection; buttons retain accessible labels and title tooltips.
- Location defaults to `Lesson title > Lesson Overview` and follows the current
  article as the page scrolls. It does not claim tracked SCORM completion.
  Page sections opens links to the overview and each article. Previous/Next
  move between sections in this standalone preview, not browser history;
  they disable at the first and last section. There is no separate Back
  button. Resources
  links to the lesson's references.
- Short notifications temporarily replace the display for seven seconds.
  Messages longer than 100 characters, including their source prefix, use the
  separate reusable notification bar with its existing ten-second expiry and
  history. Selecting a status key restores that view immediately.
- Theme Manager and [Course Agent](../../course-agent/course-agent.js) mount
  independently in separate panels. Escape/Close returns focus to the trigger;
  opening another tool closes the previous panel. Course Agent currently
  provides location and section navigation only: no AI backend, conversation
  persistence or external transmission is implemented.
- Theme Manager uses existing studio colour helpers. The lesson preview is
  local-only: modes, colour/harmony editing and JSON import/export work;
  server save/load/build controls are explicitly disabled rather than making
  requests to an unavailable studio API.

`authoring` defaults to `false` in the mount API. The standalone HTML explicitly
opts in with `data-authoring="true"`. For production, omit that opt-in or set it
to `false`: no Theme Manager button/panel, colour-status keys, theme-manager
JavaScript, studio adapter or theme-manager CSS is loaded. Course Agent and
learner navigation remain separate. `?mode=production` previews this exclusion;
it is not an export/build pipeline or a substitute for production configuration.

The copied references in [`../_dev/docs/`](../_dev/docs/) are the source for
this first pass. The original skeleton store and schema cited by those
references are not present in this checkout, so details not stated there—such
as concrete component properties and completion-rule definitions—are
intentionally left to the generator/store integration rather than guessed here.
