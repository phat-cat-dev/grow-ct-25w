# courses/_archive/

Reference-only historical course material, imported into this repo (28 Oct
2026) from a predecessor project's git backup
(`~/git-backup/wkspc2614-ADAPT.git`). Not active courses: not built, not
gated, not reviewed, not retrofitted.

## Why it lives under `courses/_archive/`, not `archive/`

The predecessor repo kept its archive at the top level, sibling to
`courses/`. Here it was placed inside `courses/` on explicit instruction.
Two things keep that safe:

- **Underscore prefix.** `tools/verify-all-courses.js`'s `discoverCourses()`
  already skips any direct `courses/` entry starting with `_` (the existing
  convention for `courses/_generated/` and `courses/_component-gallery/`).
  Naming this `_archive` rather than `archive` means it is excluded from
  course-gating (`voice-lint`, `conformance-lint`, `validate-design-schemas`)
  automatically, the same way the others are.
- **Explicit build-target refusal.** `tools/check-build-target.js` refuses a
  build outright if `src/course` ever resolves into `courses/_archive/`,
  regardless of the underscore prefix, closing the same failure mode that
  tool was originally written to catch (`src/course` once pointed into the
  predecessor repo's `archive/`).

## Contents

- **`courses-2026-09/`** — the four courses archived together for the
  Manual Course Audit 2026-09 (16-17 Sep 2026): `academic-writing-introductory`,
  `academic-writing-intermediate`, `academic-writing-advanced`,
  `presenting-introductory`. This is the version where the five-stage
  *writing cycle* (understand the task, plan, draft, edit, proofread) was
  the literal lesson-by-lesson backbone of the academic-writing course
  (`L02` Understanding the task through `L07` Common errors).
- **`courses-2026-09-rebuild/`** — a later, separate retirement: a Phase 6
  rebuild attempt at `presenting-introductory`, closed at Phase A (no
  B-gates) and retired without being built on 19 Sep 2026. Distinct from
  the batch above.
- **`v2/`** — the retired `presenting-v2` and `referencing-v2`
  pathway-distillation pathways (`profile: "pathway-distillation"` on their
  manifests), each with its three tiers under `shell/generic/`. Moved here
  from `courses/presenting-v2/` and `courses/referencing-v2/` on 10 Nov 2026.

Each subdirectory keeps its own original README with full provenance, except
`v2/`, which has none - it was moved straight from the live pathway tree, not
imported from the predecessor repo.

## What was deliberately not imported

The predecessor repo's `archive/courses-2026-09/_generated-snapshot/`
directory (dozens of subject-contextualised regenerations of the same four
courses — banking-and-finance, criminology, project-management, psychology,
sports-journalism variants) was not brought across. It is a copy of
generated output for the same courses already captured here, not a
distinct previous course; importing it was judged excessive for
reference-only purposes. If a specific subject variant is needed later, it
can be extracted the same way these were, from
`~/git-backup/wkspc2614-ADAPT.git` at commit `b152c3a`.

No other retired/archived course directories were found across the
predecessor repo's full history beyond the two archiving events above (one
unrelated hit, `dummy-pipeline-test-introductory`, deleted 29 Aug 2026, was
a pipeline smoke-test course, not real content, and was not imported).
