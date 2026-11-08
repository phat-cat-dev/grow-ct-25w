# courses/v1/

39 courses: the 13 academic-practice pathways (`docs/curriculum/
pathway-tier-mapping.md`) at 3 tiers each (introductory/intermediate/
advanced), built one tier at a time via `tools/new-course.js`'s single-tier
path. No `profile` field in any manifest here - this IS the identifying
mark of a v1 course (verified empirically, no exceptions across all 39).

## Design shape

4 course outcomes -> 4 lessons: one lesson per outcome (L01-L03), plus a
closing **L04** that integrates all three strands into "one practice"
(`crs-03_course-outcomes`, `crs-04_lesson-map`). See
`docs/curriculum/referencing-presenting-v1-v2-comparison.md` for a worked
example of this structure against v2's, on the same two subjects.

## Shape per course directory

```
<slug>/
  course-design_<slug>.json   the manifest: gates, decided values, grounding
  en/                         Adapt content model, once scaffolded/authored
    config.json
    course.json
    contentObjects.json
    articles.json
    blocks.json
    components.json
```

## Pathways (13)

academic-writing, ai-technology, creativity, criticality,
finding-using-sources, presenting, referencing, reflective-practice,
researching-research-methods, revising-exams,
starting-progressing-succeeding, understanding-learning-assessment-feedback,
work-based-experiential-learning - each as `<pathway>-introductory`,
`<pathway>-intermediate`, `<pathway>-advanced`.

## Resolving a slug

Use `tools/lib/course-resolve.js`'s `resolveCourse(slug, ['courses', ...])` -
do not hardcode `courses/v1/<slug>` in a tool; the shared resolver already
checks here (and `courses/v2/`) so a caller does not need to know which
vintage a given slug is.
