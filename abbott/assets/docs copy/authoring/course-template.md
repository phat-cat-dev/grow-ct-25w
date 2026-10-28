# Course-Level Template

> **DRAFT v1** — based on Academic Writing: Introductory Stage instance only
> (28 July 2026). This is the only course built so far; patterns are extracted
> from a single instance, not compared across multiple. See `template-v2-scope.md`
> for items queued for a v2 pass. **Needs validation against a second course
> before being treated as authoritative.**
>
> **SKS-1 note (20 September 2026):** Per SKS-1 (`open-decisions.md`), the
> skeletons store (`design-kb/design-kb.skeletons.json`) is the single
> source of truth for structure; this template is an authoring guide
> pointing at it, not an independent source. Prompt 134's nesting audit
> (Task 5) named 2 disagreements between this template and the
> store/mapping doc, not yet resolved here: the Folder Structure section's
> page order omits C-PRE/C-POST, present in the store's fixed page set;
> and the Course Slug Convention's tier-naming formula uses a "Stage"
> suffix never used in `pathway-tier-mapping.md`. Where this template and
> the store disagree, the store is authoritative.

Reference template for course-level structure — what makes up a complete
pathway-tier at the assembly level, distinct from individual page content.

See also:
- `wrapper-open-template.md` — W-OPEN page structure
- `summative-template.md` — SUMM page structure
- `wrapper-close-template.md` — W-CLOSE page structure
- `lesson-structure-template.md` — content lesson structure
- `course-creation-workflow.md` — the workflow that uses these templates
- `docs/testing/p8-moodle-walkthrough-checklist.md` — Moodle deployment testing

---

## Overview

A **course** is one pathway-tier (per DM-1a). It contains:

| Element | Count | Description |
|---------|-------|-------------|
| W-OPEN | 1 | Wrapper Open — introduces the tier |
| Content lessons | 4-8 typical | Teaching units (L02, L03, etc.) |
| SUMM | 1 | Summative Assessment |
| W-CLOSE | 1 | Wrapper Close — wraps up the tier |

**Page sequence:** W-OPEN → L02 → L03 → ... → L0N → SUMM → W-CLOSE

---

## Folder Structure

```
courses/
└── <course-slug>/              # e.g., academic-writing-introductory
    ├── config.json             # technical config (spoor, theme, completion)
    └── en/                     # language folder
        ├── course.json         # course metadata (title, description, buttons)
        ├── contentObjects.json # pages (W-OPEN, lessons, SUMM, W-CLOSE)
        ├── articles.json       # articles within pages
        ├── blocks.json         # blocks within articles
        └── components.json     # components within blocks
```

**Classification:** Fixed structure — every course uses this layout

---

## Course Slug Convention

| Field | Rule | Example |
|-------|------|---------|
| Pathway name | From `pathway-tier-mapping.md` | "Academic Writing" |
| Tier naming | `<Pathway>: <Tier> Stage` | "Academic Writing: Introductory Stage" |
| Slug | Kebab-case, pathway + tier | `academic-writing-introductory` |

**Classification:** Fixed convention, tier-specific values

Per course-creation-workflow.md §1.1-1.2: Confirm the vocabulary check before
creating any files. Getting the name wrong after files exist is expensive.

---

## Lesson Count and Sequence

**What decides the lesson count?**

Per course-creation-workflow.md §1.4, lesson count is content-driven:

1. **Start from the book's own structure** — chapter subheadings are usually
   a real pedagogical sequence
2. **Test each candidate against the six-part flow** — a candidate earns its
   own lesson only if it can support a full worked-example-plus-analysis
3. **Watch for skills the book embeds** — some topics deserve separation even
   if the source doesn't isolate them
4. **Rough range: 4-8 per tier** — thin enough to stay focused, full enough to
   justify a course

**Classification:** Variable — lesson count is decided at Phase 1.4, per
pathway-tier

---

## config.json (Technical Configuration)

**Classification:** Fixed/boilerplate — copy from existing course, minimal changes

```json
{
  "_type": "config",
  "_defaultLanguage": "en",
  "_theme": "adapt-contrib-vanilla",
  "_menu": "adapt-contrib-boxMenu",
  "_accessibility": { "_isEnabled": true, ... },
  "_completionCriteria": {
    "_requireContentCompleted": false,
    "_requireAssessmentCompleted": true,
    "_submitOnEveryAssessmentAttempt": true,
    "_shouldSubmitScore": true
  },
  "_spoor": {
    "_isEnabled": true,
    "_tracking": {
      "_shouldStoreResponses": true,
      "_shouldRecordInteractions": true,
      "_shouldRecordObjectives": true
    },
    "_reporting": {
      "_onTrackingCriteriaMet": "completed",
      "_onAssessmentFailure": "incomplete"
    }
  },
  "_bookmarking": { "_isEnabled": true, "_level": "component" }
}
```

**Key settings:**
- `_completionCriteria._requireAssessmentCompleted: true` — course completes
  when assessment passes (per S-4)
- `_spoor._reporting._onTrackingCriteriaMet: "completed"` — SCORM status on pass
- `_spoor._reporting._onAssessmentFailure: "incomplete"` — SCORM status on fail

---

## course.json (Course Metadata)

**Classification:** Mixed — some fields are boilerplate, some are tier-specific

### Tier-specific fields (MUST update per course)

| Field | Description |
|-------|-------------|
| `title` | Full course title: "{{Pathway}}: {{Tier}} Stage" |
| `displayTitle` | Same as title |
| `description` | Course description for menu/manifest |
| `body` | Welcome message |
| `_latestTrackingId` | Dense from 0, in block-write order; carries the highest `_trackingId` actually assigned across `blocks.json` (TID-1, `docs/project/open-decisions.md`) |

### Fixed/boilerplate fields

| Field | Description |
|-------|-------------|
| `_id` | Always `"course"` |
| `_buttons` | Submit/Reset/ShowCorrectAnswer labels |
| `_globals` | Accessibility labels, component ARIA text |
| `_pageLevelProgress` | Enabled |
| `_bookmarking` | Enabled, component-level |
| `_navigation` | Standard settings |

### Assessment defaults

```json
"_assessment": {
  "_isPercentageBased": true,
  "_scoreToPass": 70,
  "_correctToPass": 70
}
```

**Note:** These are defaults; the article-level `_assessment` on SUMM-a-01
overrides them. Per Adapt's precedence rules, article-level settings take
priority over course-level defaults.

> **KNOWN-FIXED (28 July 2026):** Academic Writing: Introductory Stage had
> course.json set to 75% while SUMM-a-01 used 70%. All testing was against
> the article-level 70% (which was authoritative). Fixed by aligning
> course.json to 70%. **For future courses:** ensure course.json and SUMM
> article use the same pass mark, or consciously rely on the article-level
> override.

### Resources drawer

```json
"_resources": {
  "_isEnabled": true,
  "_resourcesItems": [ ... ]
}
```

> **KNOWN ISSUE (28 July 2026):** Academic Writing: Introductory Stage still
> contains Adapt Learning demo placeholder links (YouTube, project site,
> Gitter). Either populate with real resources or set `_isEnabled: false`.
> Logged in project-backlog.md.

---

## lesson-registry.json

Records lessons and their metadata for tooling (merge-context.js, etc.).

**Current format:**
```json
{
  "_latestKey": 7,
  "lessons": {
    "L01": { "title": "...", "pathway": "...", "tier": "...", "status": "retired" },
    "L02": { "title": "Understanding the task", "pathway": "academic-writing", "tier": "introductory" },
    ...
  }
}
```

**Lesson key convention:** `L02`, `L03`, etc. — L01 is reserved/retired; new
lessons start at L02.

**Block ID convention within lessons:** Gapped-5s numbering (`L03-b-05`,
`L03-b-10`, `L03-b-15`, ...) to allow insertions.

*Ids are generated per ID-1; ids shown here are illustrative.*

> **DOC/REALITY GAP:** course-creation-workflow.md §1.6 describes a `courses`
> nesting structure that's not yet implemented. See template-v2-scope.md for
> resolution path.

---

## Context-Pack Structure

Context packs provide discipline-specific content for context-coupled lessons.

```
content/context-packs/
├── baseline/
│   └── <course-slug>/
│       ├── understanding-the-task.json
│       ├── planning.json
│       └── ...
├── <context>/                   # e.g., criminology, psychology
│   └── <course-slug>/
│       └── (same lesson files)
└── _template/
    └── (per-lesson generation templates)
```

**LK-1 note (22 September 2026):** The pattern below is superseded. A
lesson pack file is `<subject>/<base-course-slug>/<key>.json`, where
`<key>` is the lesson's A3 key (the same key A5's plan and that lesson's
`slot__<key>__<slotType>` markers use). See `open-decisions.md` LK-1.

**Pattern:** `<context>/<course-slug>/<lesson-slug>.json`

**Baseline:** The default context (was called "book" in early development).
Always built for every context-coupled lesson.

**Classification:** Fixed structure, tier-specific content

---

## Confidence PRE/POST Pairing

The confidence component in W-OPEN (PRE) and W-CLOSE (POST) are linked by
`_selfAssessmentGroupId`.

| Page | Mode | Setting |
|------|------|---------|
| W-OPEN Block 4 | `_mode: "pre"` | `_selfAssessmentGroupId: "{{course-slug}}-confidence"` |
| W-CLOSE Block 1 | `_mode: "post"` | `_selfAssessmentGroupId: "{{course-slug}}-confidence"` |

**Both must use the same group ID** for the pre/post comparison to work.

**Items:** Curated mix of tier + lesson outcomes, max 10 items (per WR-2a).
Same items appear in both PRE and POST.

**Classification:** Fixed mechanism, tier-specific items and group ID

---

## Build and Deploy

See `docs/testing/p8-moodle-walkthrough-checklist.md` for the full deployment
testing checklist. Summary:

1. **Build:** `grunt build` — produces `build/` with imsmanifest.xml
2. **Package:** Zip contents of `build/` so imsmanifest.xml is at zip root
3. **Upload:** Add as SCORM package activity in Moodle
4. **Test:** Pass and fail paths, gradebook, suspend/resume

**Classification:** Fixed process

---

## Classification Summary

| Element | Classification |
|---------|----------------|
| Folder structure | **Fixed** |
| Course slug | **Tier-specific** (follows convention) |
| Lesson count | **Variable** (4-8 typical, content-driven per §1.4) |
| config.json | **Fixed/boilerplate** |
| course.json title/description | **Tier-specific** |
| course.json _assessment | **Fixed** (70% pass mark) |
| course.json _resources | **OPEN** (currently contains placeholders) |
| lesson-registry.json | **Fixed convention** (format evolving) |
| Context-pack structure | **Fixed structure**, tier-specific content |
| Confidence groupId | **Tier-specific** |
| Build/deploy process | **Fixed** |

---

## Checklist: Creating a New Course

- [ ] Vocabulary check (pathway name, tier naming, slug) — §1.1-1.2
- [ ] Confirm curriculum scope and source — §1.3
- [ ] Propose lesson breakdown — §1.4
- [ ] STOP for review — §1.5
- [ ] Create course folder: `courses/<course-slug>/`
- [ ] Copy config.json from existing course (minimal changes)
- [ ] Create course.json with tier-specific title/description
- [ ] Update `_latestTrackingId` as content is added
- [ ] Add to lesson-registry.json
- [ ] Build page content (W-OPEN, lessons, SUMM, W-CLOSE)
- [ ] Create baseline context packs for context-coupled lessons
- [ ] Build and test (`grunt build`, `grunt server-scorm`)
- [ ] Moodle walkthrough (per p8-moodle-walkthrough-checklist.md)
