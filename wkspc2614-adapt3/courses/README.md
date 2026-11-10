# courses/

Course directories: manifest (`course-design_<slug>.json`) plus the Adapt
content model (`en/*.json`) once scaffolded/authored.

## Layout

```
courses/
  <pathway>/                  one directory per pathway (13 single-tier +
                               presenting-v2, referencing-v2)
    shell/generic/<slug>/     the per-tier course (course-design_<slug>.json,
                               en/*.json once scaffolded/authored)
    context/<taxonomy>/<slug>/ per-tier context pack (relocated, see below)
  _archive/                   frozen pre-realignment pilots, read-only
  _component-gallery/         a static gallery/demo course, not part of the taxonomy
  _generated/                 build output: merged <tier>-<context> pairs, gitignored
```

## Pathway grouping

Reorganised 10 Nov 2026 (pathway/shell reorg): every pathway is its own
directory holding its tiers under `shell/generic/` rather than courses
sitting flat, or split by a v1/v2 vintage flag. `presenting-v2` and
`referencing-v2` are pathway groups in exactly the same shape as the
13 original pathways - "v2" is part of the pathway name now, not a separate
root. See `docs/curriculum/referencing-presenting-v1-v2-comparison.md` for
the worked side-by-side comparison of the two designs that motivated keeping
them distinct (referencing, presenting).

The distinction is reliably detectable from the manifest itself: a
single-tier manifest carries no `profile` field; a pathway-distillation
manifest (the `-v2` pathways) carries `profile: "pathway-distillation"`.
`tools/new-course.js` uses exactly this rule to decide a new course's
manifest path: a single-tier `onb-03_pitch` answer writes to
`courses/<pathway>/shell/generic/<slug>` where `<pathway>` is `<slug>` with
its tier suffix stripped; pitch `"all"` (three sibling tiers at once) writes
the same shape under the theme's own pathway group.

## Resolving a course slug in code

Do not assume `courses/<slug>/` - a slug usually lives at
`courses/<pathway>/shell/generic/<slug>/`, or (for a merged build) at
`courses/_generated/<slug>/`. Use `tools/lib/course-resolve.js`'s
`resolveCourse(slug, roots)`: the `'courses'` root tries flat
`courses/<slug>` (legacy, kept for callers that pre-date the reorg) then
`courses/<pathway>/shell/generic/<slug>`, so callers do not need to know
which pathway a slug belongs to.

## The other directories

- **`_archive/`** - frozen, pre-realignment course pilots. Not gated against,
  not reviewed, not repaired, not retrofitted (RBD-1). See its own README.
- **`_component-gallery/`** - a static demo/reference course exercising the
  component palette, not part of the 13-pathway x 3-tier taxonomy.
- **`_generated/`** - build output only, never committed by hand: each
  subdirectory is a merged `<tier>-<context>` pair produced by
  `merge-context.js` from a pathway's course plus a subject context pack.
  Gitignored; rebuilt, not edited.
