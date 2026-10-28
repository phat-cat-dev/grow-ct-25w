# Course export bundle

`tools/course-export.js` renders a built course into a human-readable, multi-format
bundle — a "course script" (screenplay), a full Adapt-id structure, a course-pack
of gated decisions, a YAML twin, the real component templates, and the source
JSON. One-way export (the edit → rebuild round-trip is a separate import tool,
still to come).

## Run

```
npm run course-export -- \
  --course <content-dir> \
  --short-slug <slug> \
  [--manifest <course-design.json>] \
  [--packs <context-pack-dir>] \
  [--out exports]
```

- **base bundle:** `--course courses/<slug> --short-slug undlaf-intro`
- **subject bundle:** `--course courses/_generated/<slug>-<subject> --short-slug undlaf-intro-psycho`
  (run `merge-context.js` first so coupled slots and tokens are resolved)

Output: `exports/<short-slug>_<ISO-timestamp>/`. `exports/` bundles are
version-controlled (a deliverable, not a throwaway build artifact) — see the
note in `.gitignore`.

This is the **full, on-request** output. Routine `grunt build` runs does *not*
call this — see "Build integration" below.

## What's in a bundle

```
<short-slug>_<timestamp>/
  html/
    <slug>.full.html        every _id / _component / _classes / _layout /
                            _trackingId / _skeletonKey, CXP slot markers,
                            feedback/modal text — maximum metadata
    <slug>.structural.html  clean presentational DOM (article>block>component>p)
  templates/
    lesson.annotated.html   one lesson as produced, annotated with ids, section
                            classes, CXP slot markers and skeleton keys
    src/                    the real component templates (modern Adapt renders
                            components with React JSX, templates/*.jsx; copied
                            from src/ — contrib ones present after `adapt install`)
  md/
    <slug>.script.md        the screenplay: all prose + every activity + every
                            feedback/modal line, reading order, W-OPEN → W-CLOSE,
                            with <!-- id --> anchors for the future round-trip
    <slug>.course-pack.md   gated DECISIONS (not content): course-level gates,
                            each lesson's crs-04 + les-01 decisions, W-OPEN first
                            and W-CLOSE last
    <slug>.edit.md          round-trip SOURCE: every editable field in a fenced
                            block tagged <!-- edit:ID:PATH -->, value verbatim
                            (HTML/tokens/classes preserved) — edit this, re-import
  yaml/<slug>.yaml          structured data twin (ids + fields + metadata)
  json/
    course-design.json      the gated AI decisions (the design-level AI output)
    packs/<page>.json       the AI-generated content packs (generatedProse /
                            generatedItems / _prompts)
```

## Short slug

Set at `onb-04_naming` as `<theme(6)>-<tier|level>-<context(6)>`, e.g.
`undlaf-intro` (base) and `undlaf-intro-psycho` (psychology build). The folder and
file names use it.

## Templates: JSX, not Handlebars

Adapt Framework ≥ 5.19 renders components with **React JSX** templates
(`templates/*.jsx`), not Handlebars. Our custom `adapt-abbott-*` components are
JSX; contrib components the same. Handlebars survives only in some core/menu
places. The bundle captures whatever template files are present.

## Round-trip (edit → rebuild)

`md/<slug>.edit.md` is the faithful, field-anchored source. Edit the content
inside each fenced block (keep the `<!-- edit:ID:PATH -->` markers and fences),
then re-import:

```
node tools/course-script-import.js --edit <slug>.edit.md --course courses/<base-slug> [--dry-run]
```

The import writes each **changed** field back into the base course's
`en/components.json`, then runs `verify-course`. If verification fails (e.g. a
voice violation), the file is **restored** and nothing lands. It makes no commit
— review the diff and stage as usual.

v1 round-trips the flat prose fields (`body`, `displayTitle`, `instruction`) and
the feedback/modal strings. Item/option arrays and per-subject pack content are
read-only for now (edit those in the JSON / packs). Edit the **base** course;
the `script.md` (screenplay) is for reading, `edit.md` is for editing.

## Build integration

`grunt build` runs `tools/course-css-export.js` as its final task
(`course-css-export`). It copies the build's compiled stylesheet,
`build/adapt.css`, into `exports/<short-slug>-<YYMMDDHHMMSS>.css` (no new
sub-folder per build, just one more flat file) — a visual-regression
reference for the course's actually-compiled theme CSS.

Each run also bumps a content-version record, `exports/<short-slug>.version.json`
(`{ shortSlug, version, history: [...] }`, via `tools/lib/content-version.js`).
The first export for a course starts at `1.00`; every export or edit-import
after that increments the minor digit (`1.01`, `1.02`, ...). `tools/
course-script-import.js` bumps the same record on a successful `--edit` or
`--script` round-trip, so the next export's version reflects edits that were
sent back for a rebuild.

The `.script.md` screenplay export (`tools/course-script-md.js`) no longer
runs automatically as part of `grunt build`; run it on request with
`npm run course-script-md -- --course <dir> [...]` or `npx grunt
course-script-md` (discovering `--course` from `src/course` and writing to
`exports/`), the same way as before.

The full multi-format bundle (html/templates/yaml/json/packs) described above
stays on-request too: run `npm run course-export -- --course <dir> [...]`
directly, or `npx grunt course-script` to run it the same way.
