# Adapt Framework — Official Reference Links

*Compiled 28 July 2026 for the Cardiff Met theme fork and general course-tweaking work. These are official adaptlearning GitHub wiki/repo pages, not third-party guides. Cross-reference from here rather than duplicating content — these pages get updated upstream.*

---

## Theming (primary references for the Cardiff Met theme fork)

**[Styling your course](https://github.com/adaptlearning/adapt_framework/wiki/Styling-your-course)** — the main framework theming guide. Key facts worth remembering:
- Themes are written in **LESS**, organised into four folders: `_defaults/` (variables — start here), `core/` (built-in UI elements: nav, drawer, notify, pages, blocks), `plugins/` (per-plugin overrides), `project/` (course-level customisation).
- **Official responsive breakpoint variables already exist**: `@device-width-small`, `@device-width-medium`, `@device-width-large`, `@device-width-xlarge`. Use these directly in media queries — this is the concrete mechanism for the "extend Adapt's native breakpoint system" decision already made (see `template-v2-scope.md` Group 2, item 13). Do not invent new breakpoint variables.
- Spacing and fonts are each split across two `_defaults/` files: `_spacing-config.less` / `_spacing-containers.less`, `_font-config.less` / `_font-mixins.less`.
- `@validation-error` / `@validation-success` control correct/incorrect answer feedback colours — relevant to the sortable colour-contrast bug logged in the P8 walkthrough notes.
- Templates now use **JSX** (recommended since Framework v5.12.0); older components may still use Handlebars. A theme overrides any template by placing a same-named file in `adapt-themeName/templates/`. This is the actual mechanism for the "block off comparison pairs / worked examples with background + rounded corners" idea — likely a `project/` LESS override, possibly paired with a template override if structural markup needs to change, not just colour.
- Icons are defined in **framework core**, not the theme (`src/core/less/_defaults/icons.less`), each mapped to a class (e.g. `.icon-tick`). Relevant if the "completed activity" chrome/indicator feature ends up wanting a checkmark icon.

**[Vanilla theme wiki](https://github.com/adaptlearning/adapt-contrib-vanilla/wiki)** — documentation for the theme this project currently forks from. Sub-pages:
- **Custom Classes** — the full list of custom CSS classes Vanilla supports out of the box (e.g. `fade-in`, `is-divider-block`) — check this before inventing new classes; some of what's wanted (visual blocking, dividers) may already exist as a standard class.
- **Structure** — breakdown of the theme's file/folder structure.
- **Icons** — the theme's custom icon font set.
- **Semantic HTML** — how Vanilla structures its markup semantically (relevant to the accessibility backlog item).
- **JSON Config and Authoring Tool Options** — configurable attributes exposed per page/article/block for background images and supporting styles.

**[Modifying the Vanilla Theme](https://github.com/adaptlearning/adapt_authoring/wiki/Modifying-the-Vanilla-Theme)** — step-by-step guide for forking Vanilla into a new theme. This is close to a direct how-to for the Cardiff Met fork:
- Copy `adapt-contrib-vanilla` to a new folder, rename it.
- Edit `bower.json`: `name` (unique identifier, e.g. `adapt-cardiffMet`), `version`, `displayName` (shown in authoring tool), `theme` (last segment of `name`).
- **Style your templates using Vanilla's existing `.less` class names** so that other plugins' styling (including the three custom `adapt-abbott-*` components) inherits correctly rather than breaking.
- Adapt uses LESS; `.less` files compile to `.css` on `grunt build`.
- Zip structure note for manual packaging: zip from the root of the theme folder.

---

## Configuration (course.json / config.json)

**[Configure your project with config.json](https://github.com/adaptlearning/adapt_framework/wiki/Configure-your-project-with-config.json)** — config.json lives outside the language folder (`/src/course/config.json`) and governs **how the project functions**: build settings, plugin includes/excludes, theme selection, tracking (spoor) config. The `build.excludes`/`build.includes` arrays let you explicitly control which plugins ship in a build.

**Content starts with course.json** (linked from the same wiki, not yet separately fetched this session) — course.json lives inside the language folder (`/src/course/en/course.json`) and governs **content reused throughout the course** — title, description, learning outcomes text, etc. Confirms the split already used to resolve the pass-mark mismatch fix (28 July): config.json settings are project-wide defaults; course.json / article-level settings are content-specific and can override them.

**Key distinction to remember** (directly relevant to two bugs found today): settings that are **language-dependent belong in course.json**, not config.json. This is why the `_resources` demo-placeholder content and the title/description placeholder bug (22 July) both lived in course.json — it's the correct location for that content, it just hadn't been filled in with real values.

---

## Accessibility

**[Accessibility](https://github.com/adaptlearning/adapt_framework/wiki/Accessibility)** and **[Accessibility: worked example](https://github.com/adaptlearning/adapt_framework/wiki/Accessibility:-worked-example)** — framework-level accessibility guidance and a worked example. Relevant to Strategic backlog item #1 (screen-reader/keyboard-only audit) — worth reading before that audit happens, rather than working from general WCAG knowledge alone, since Adapt has framework-specific patterns (e.g. its own focus-management system, which the earlier `BrowserFocus._onBlur` recursion bug lived inside).

**[ARIA Roles and Labels](https://github.com/adaptlearning/adapt_framework/wiki/ARIA-Roles-and-Labels)** and **[Globals and ARIA Labels](https://github.com/adaptlearning/adapt_framework/wiki/Globals-and-ARIA-Labels)** — how Adapt's accessibility labelling system works, relevant to any custom component work (the three `adapt-abbott-*` components).

---

## Component reference (per-plugin wikis)

Each core Adapt component has its own wiki with configurable properties. Useful when deciding "is there a consistent Adapt component alternative" (per VO-1, the open hotgraphic-workflow question) or when authoring new lesson content:

- [Accordion](https://github.com/adaptlearning/adapt-contrib-accordion/wiki)
- [Assessment](https://github.com/adaptlearning/adapt-contrib-assessment/wiki)
- [Assessment Results](https://github.com/adaptlearning/adapt-contrib-assessmentResults/wiki) — relevant to the pending per-question correct/incorrect breakdown feature request
- [Graphic](https://github.com/adaptlearning/adapt-contrib-graphic/wiki) — displays device-width-optimised images; a possible alternative to hotgraphic for pathways without a cyclical/staged visual model
- [Graphical Multiple Choice Question (gmcq)](https://github.com/adaptlearning/adapt-contrib-gmcq/wiki)
- [Hot Graphic](https://github.com/adaptlearning/adapt-contrib-hotgraphic/wiki)
- [Matching](https://github.com/adaptlearning/adapt-contrib-matching/wiki)
- [Media](https://github.com/adaptlearning/adapt-contrib-media/wiki)
- [Multiple Choice Question (mcq)](https://github.com/adaptlearning/adapt-contrib-mcq/wiki)
- [Narrative](https://github.com/adaptlearning/adapt-contrib-narrative/wiki)
- [Resources](https://github.com/adaptlearning/adapt-contrib-resources/wiki) — relevant to fixing the course.json `_resources` placeholder-content bug
- [Slider](https://github.com/adaptlearning/adapt-contrib-slider/wiki)
- [Spoor](https://github.com/adaptlearning/adapt-contrib-spoor/wiki) — SCORM tracking, relevant to everything in `moodle-upload-instructions.md`
- [Text](https://github.com/adaptlearning/adapt-contrib-text/wiki)
- [Text Input](https://github.com/adaptlearning/adapt-contrib-textInput/wiki) — relevant to the reflective-content masking/lock bug
- [Trickle](https://github.com/adaptlearning/adapt-contrib-trickle/wiki)
- [Tutor](https://github.com/adaptlearning/adapt-contrib-tutor/wiki) — inline feedback popups

All components accept a `_classes` property for applying theme-defined custom LESS classes — the same mechanism referenced in "Styling your course" above.

---

## How this should be used going forward

- **Before the Cardiff Met theme fork begins**, read "Styling your course" and "Modifying the Vanilla Theme" in full (not just this summary) — they're short enough to read directly rather than working from secondhand notes.
- **When deciding on VO-1** (hotgraphic vs. alternative components), check the Graphic, Narrative, and Accordion wikis for what each actually supports before assuming hotgraphic is the only visual option.
- **Before the accessibility audit** (Strategic item #1), read the Accessibility and ARIA wiki pages — Adapt's focus-management system has framework-specific behaviour (as the earlier `BrowserFocus._onBlur` bug demonstrated), so generic WCAG knowledge alone isn't sufficient.
- Add further pages here as they become relevant, rather than re-discovering them each time.

---

*Note: some of these pages are wiki content and may be edited/reorganised upstream over time. If a link breaks, search `adaptlearning/adapt_framework wiki <topic>` or `adaptlearning/adapt-contrib-vanilla wiki <topic>` to find the current location.*
