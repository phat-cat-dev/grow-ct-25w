---
description: Open the CXP (context-pack) phase for an existing course by auto-stating its one reserved gate, cxp-03_exemplar-programmes. Execute mode. Runs once per course.
argument-hint: <course-slug>
---

Open the CXP phase for course `$1`. This writes the single reserved CXP
gate, `cxp-03_exemplar-programmes`, which is advisory, `defaultType:
none`, and subject-independent ("exemplar programmes: none" whatever the
subject) — so it is auto-stated ONCE per course, here, not per context
pack (Abbott, 8 October 2026: "wire cxp-03 record-writing into the CXP
flow"). The live CXP gates (`cxp-01_subject`, `cxp-02_qualifiers`,
`cxp-04_context-generation`) are decided per context pack via the
ordinary `/gate` + `/land` path and are NOT written here.

It mirrors the reserved CXS records `/new-course` writes: `state:
closed`, `provenance: advisory-stated` (GI-2's word for an advisory gate
stated at the moment it applies, never opened), `grounding: []`,
`decidedValue: {value:"none", reserved:true}`.

1. RECON. Confirm `courses/$1/course-design_$1.json` exists (this runs
   on an existing course, after /new-course). If it does not, stop and
   name the path.

2. Run the tool, which is idempotent (a no-op if `cxp-03` already
   carries a record):

       node tools/cxp-open.js --course=$1

   Paste its output in full, including the record it wrote and the
   validate result with its exit code. A non-zero exit or a `REFUSED:`
   line stops here; the tool reverts the manifest to its prior content
   on a validation failure, so do not work around it.

3. SHOW-DIFF-STOP. Full `git diff` / `git status` for
   `courses/$1/course-design_$1.json` only. Explicit staging of that
   one file. One commit. No push. (If step 2 reported the idempotent
   no-op, there is nothing to stage — say so and stop.)

Note: the per-context authoring flow (`/new-context`) is a separate,
still-old-model workflow; its realignment to the six-phase CXP gates is
pending, and when done it should assume this gate is already open (run
`/cxp-open $1` first if not).
