# courses/

Course directories: manifest (`course-design_<slug>.json`) plus the Adapt
content model (`en/*.json`) once scaffolded/authored.

## Layout

```
courses/
  v1/                     39 single-tier courses - the original design
  v2/                     6 pathway-distillation courses (2 themes x 3 tiers)
  _archive/               frozen pre-realignment pilots, read-only
  _component-gallery/     a static gallery/demo course, not part of the taxonomy
  _generated/             build output: merged <tier>-<context> pairs, gitignored
  sandbox-les01-hardstop/ a standalone sandbox course, not part of the taxonomy
```

## v1/ vs v2/

Split 8 Nov 2026 to keep two different course designs - built at different
times, to different specs - from sitting flat side by side. See
`v1/README.md` and `v2/README.md`, and
`docs/curriculum/referencing-presenting-v1-v2-comparison.md` for a worked
side-by-side comparison of the two designs on the same subjects
(referencing, presenting).

The split is reliably detectable from the manifest itself: every `v1/`
manifest carries no `profile` field; every `v2/` manifest carries
`profile: "pathway-distillation"`. `tools/new-course.js` uses exactly this
rule to decide where a new course's manifest is written: a single-tier
`onb-03_pitch` answer writes to `v1/`, pitch `"all"` (three sibling tiers at
once) writes to `v2/`.

## Resolving a course slug in code

Do not assume `courses/<slug>/` - a slug may live at `courses/v1/<slug>/`,
`courses/v2/<slug>/`, or (for a merged build) `courses/_generated/<slug>/`.
Use `tools/lib/course-resolve.js`'s `resolveCourse(slug, roots)`: the
`'courses'` root itself tries all of flat `courses/<slug>` (legacy, kept for
callers that pre-date the split), `courses/v1/<slug>` and `courses/v2/<slug>`
in that order, so callers do not need to know which vintage a slug is in.

## The other directories

- **`_archive/`** - frozen, pre-realignment course pilots. Not gated against,
  not reviewed, not repaired, not retrofitted (RBD-1). See its own README.
- **`_component-gallery/`** - a static demo/reference course exercising the
  component palette, not part of the 13-pathway x 3-tier taxonomy.
- **`_generated/`** - build output only, never committed by hand: each
  subdirectory is a merged `<tier>-<context>` pair produced by
  `merge-context.js` from a `v1/` or `v2/` course plus a subject context pack.
  Gitignored; rebuilt, not edited.
- **`sandbox-les01-hardstop/`** - a standalone sandbox course for exercising
  the `les-01` gate/hard-stop machinery, not part of the taxonomy.
