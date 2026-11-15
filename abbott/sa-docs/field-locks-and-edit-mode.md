# Field locks and edit-mode reopen (published = locked)

Status: agreed with Abbott, 9 October 2026. Design of record; read from disk
before each write (durability rule). Supersedes the earlier per-field-marker
draft: locking is now a course STATE, not scattered markers.

## The model (Abbott, 9 Oct)

- When a course is **first published, everything is locked.** No field of any
  gate record, and no authored content, may change.
- To change something, you **reopen a gate and unlock the specific field(s)**
  you intend to change. Only unlocked fields may differ; everything else is
  carried forward verbatim. This is "edit mode": a reopen is a bounded patch,
  never a regeneration.

This collapses locking and edit-mode into one rule and needs nothing remembered:
the default on a published course is locked; the agent can only touch what a
reopen explicitly unlocks.

## Problem it fixes

A reopen used to re-propose the whole gate (`reopen.md` step 3: "run gate.md
steps 2-6 producing its new proposal"), so a reopen aimed at one field could
silently regenerate settled, hand-refined content (the L01 flipcard). Under this
model a reopen that unlocks only `outcomes` cannot touch the interior at all.

## A. Publish state

- The manifest carries `published` (boolean) and `publishedAt` (date-time),
  set by an explicit `/publish <course>` action (Abbott's deliberate milestone;
  recommended over auto-locking at first package, so locking is a decision, not
  a side effect).
- **Before** publish: open authoring; reopens behave as now (no unlock needed).
- **After** publish: locked; every reopen must declare its unlocks.

## B. Reopen = patch + explicit unlock (on a published course)

    /reopen <course> <gate> --unlock <decidedValue-path> [--unlock <path> ...]

- Paths are dot-paths into the record's `decidedValue` (e.g. `outcomes`,
  `check.items`, `workedExample`, `conceptTitle`).
- The new (superseding) record starts as the superseded record's `decidedValue`
  carried forward verbatim; the reopen may change ONLY the unlocked paths.
- The new record stores the set it was permitted to change:
  `"unlocked": ["check.items"]`.
- Content re-authoring (`/land`) on a published course is scoped the same way:
  only content owned by an unlocked gate field is re-authored; every other
  component is preserved untouched.
- Full regeneration is not a shortcut around this: on a published course it is
  refused unless every path it would change is unlocked.

## C. Enforcement (checked, not trusted)

- `tools/reopen.js` refuses a draft whose new `decidedValue` differs from the
  superseded record at any path NOT in `unlocked` (names the offending path).
- A lint in the gating set re-checks at every landing: for a published course,
  each superseding record's diff against the record it supersedes must be a
  subset of that record's `unlocked`. Any stray change -> FAIL, naming gate and
  path. This makes the lock a verified guarantee.

## D. Granularity

Per-field, via the unlock paths: unlock `outcomes` while `check.items`,
`workedExample`, `conceptTitle` stay locked; unlock `check.items` while the
outcomes stay locked. No whole-record all-or-nothing.

## E. Content layer

Authored content (`components.json` etc.) is derived from gate decisions, so it
is protected by B/C: a reopen/land only re-authors content for unlocked gate
fields. A deliberate, human-directed content edit outside the gate flow (as with
the flipcard copy fix) remains possible and is git-visible; a future `/edit`
path can bind such edits to an unlock too, but v1 relies on the reopen/land
discipline plus the lint on the manifest. The per-component `_locked` marker
from the earlier draft is therefore not needed in v1 (locking is the course
state, not a marker); it is retained only as a possible future content-guard.

## F. Implementation touch-points

- `schemas/course-design.schema.json`: add `published` (bool) + `publishedAt`
  (date-time) at manifest top level; add optional `unlocked` (array of strings)
  to the gate-record properties.
- `tools/publish.js` + `/publish` command: set `published: true` + `publishedAt`;
  idempotent; one commit.
- `tools/reopen.js`: accept `--unlock`; carry the superseded `decidedValue`
  forward and apply only unlocked-path changes; refuse any out-of-scope change
  on a published course; write `unlocked` onto the new record.
- `reopen.md`: rewrite step 3 to patch + explicit unlock; `--regenerate` only
  with full unlocks; `--unlock` grammar; pre/post-publish behaviour.
- `land.md`: re-author scoped to unlocked fields on a published course.
- `gate.md`: note the lock model (a published gate's locked fields are not
  re-proposed).
- A lint (validate-design-schemas or conformance-lint): the subset check in C.
- Record the convention in the schema-conventions doc (task #2).

## G. The pilot

`understanding-learning-assessment-feedback-introductory` has been packaged, so
it is "published": run `/publish` on it once the mechanism exists, after which
its gates are locked and further edits go through `--unlock`.
