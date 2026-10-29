# Archive: courses-2026-09

> **Provenance note (this repo, 28 Oct 2026):** this directory and its contents
> were imported verbatim from a predecessor project's git history
> (`~/git-backup/wkspc2614-ADAPT.git`, commit `b152c3a`) as reference material,
> at the user's request, after discovering the "writing cycle" structure in
> earlier academic-writing drafts. The rest of this README is the **original**
> note from that history and describes events in that predecessor repo, not
> this one — e.g. "moved here from `courses/`" originally meant the
> predecessor repo's top-level `archive/`, not this repo's `courses/_archive/`.
> The `_generated-snapshot/` subdirectory it describes below was **not**
> imported (dozens of subject-variant regenerations of the same four courses;
> judged excessive for reference-only purposes). See
> `courses/_archive/README.md` for this repo's own archive index.

Four courses — `academic-writing-introductory`, `academic-writing-intermediate`,
`academic-writing-advanced`, `presenting-introductory` — moved here from `courses/` on
17 September 2026. They were the basis of the Manual Course Audit 2026-09
(`docs/project/audit-2026-09/`).

Archived per RBD-1 (`docs/project/open-decisions.md`) and Abbott's 17 September direction:
these are reference material for Phase 6's ground-up redesign, not a retrofit target. They
remain readable but are no longer active courses — not gated against, not reviewed, not
repaired, not retrofitted. They served their purpose as the audit's basis.

## `_generated-snapshot/`

A **copy**, not regenerable output, of `courses/_generated/` as it stood at archive time (21
discipline-merged pairs). Kept because it is the only copy of content several open/landed
audit action rows cite directly, not the shell: A79, A94 and A97 (AWI's criminology-merged
`components.json` — text that exists only there, e.g. the "Priya" character name and the L05
annotated before/after, absent or placeholder-only in the shell); A33 (used to re-verify a
ruling directly against the generated file). `courses/_generated/` itself was gitignored, so
this snapshot is its only committed copy.

It cannot simply be regenerated from the archived shells: `merge-context.js:591` hardcodes
`shellDir` to `courses/<tier>`, not the archive path. Regenerating any of these pairs would
need either the shells restored to `courses/` or that hardcoded path changed.
