# courses/v2/

6 courses: 2 themes (referencing, presenting) x 3 tiers, written atomically
as three sibling manifests by `tools/new-course.js`'s multi-tier path
(`onb-03_pitch.decidedValue.pitch === "all"`). Every manifest here carries
`profile: "pathway-distillation"` - the identifying mark of a v2 course
(verified empirically, no exceptions across all 6).

## Design shape

6 flat course outcomes -> 6 lessons: one lesson per outcome, **no**
integrating final lesson (unlike v1's L04). See
`docs/curriculum/referencing-presenting-v1-v2-comparison.md` for the full
side-by-side against v1 on these same two subjects, including the advanced-
tier subject-matter shift: v1's `referencing-advanced` stays on
referencing-as-scholarly-practice; `referencing-v2-advanced` moves to
broader research-ethics judgement scenarios (a weak result, an unnoticed
error, a fairness issue, an unacknowledged contributor) - referencing
mechanics are no longer the subject there; ethical judgement is.

As of 8 Nov 2026, `presenting-v2-*` has progressed only through
`crs-06_pathway-statements` (onboarding/context/sourcing); it has no course
outcomes, lesson map or lessons yet. `referencing-v2-*` is further along -
see the comparison doc's coverage note for the exact gate-by-gate state of
each.

## Shape per course directory

Same as `v1/` (manifest + `en/*.json` once scaffolded/authored), plus the
`profile` field:

```
<slug>/
  course-design_<slug>.json   profile: "pathway-distillation", facetSet.tier set
  en/                         Adapt content model, once scaffolded/authored
```

## Slugs (6)

presenting-v2-introductory, presenting-v2-intermediate, presenting-v2-advanced,
referencing-v2-introductory, referencing-v2-intermediate, referencing-v2-advanced

## Resolving a slug

Use `tools/lib/course-resolve.js`'s `resolveCourse(slug, ['courses', ...])` -
do not hardcode `courses/v2/<slug>` in a tool; the shared resolver already
checks here (and `courses/v1/`) so a caller does not need to know which
vintage a given slug is.
