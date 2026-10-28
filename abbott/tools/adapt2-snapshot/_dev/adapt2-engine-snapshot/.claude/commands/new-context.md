---
description: WF-B. Author a new context pack for an EXISTING closed course. No shell edits.
argument-hint: <course-slug> <context-slug e.g. nursing> <character-name>
---

Existing-course, new-context workflow for `$1`, context `$2`,
character `$3`. The manifest is closed and READ-ONLY for this
workflow: if any step needs a shell edit or a gate change, stop and
say "this is a reopen, not a new context" and hand back.

Phase 1 (plan mode, read-only):
1. RECON. Read `courses/$1/course-design_$1.json`. Print the coupling
   plan from its `instantiations[]`: per page (`pageKey`), every
   `slotChoices` entry carrying `contextCoupling`, with its `coupled`
   flag and `variationType`. A slot with `coupled:false` (or no
   `contextCoupling`) needs no pack content; say so. This is the same
   plan `merge-context.js` reads (`requireCouplingPlan`), gathered from
   where les-01, the wrapper gates (wra-01/02) and wra-03 deposit
   per-slot coupling via /land — not the retired
   les-03_context-coupling-plan.
2. GROUND IN THE SUBJECTS CATALOGUE. Resolve the subject `$2` to its
   benchmark reference and read it as the grounding for this pack:

       node tools/resolve-subject-benchmark.js $2 --load

   Paste the JSON result and the reference path it prints. If the
   result carries a `gap` (no benchmark for this subject, or the
   subject resolved `universal`), say so plainly and proceed
   ungrounded — the pack then rests on the agent's general knowledge,
   and that is flagged in the plan at step 6. Otherwise READ the
   reference file named in `benchmark.file` and use it as the source
   for every coupled slot's discipline realisation: the subject's
   `tierReadings` (the practice/knowledge/identity triad at each tier)
   for pitch; its `pathwayMapping` entry for this course's pathway for
   how the subject's standards bear on the topic (honour each mapped
   statement's `agentInstruction`, and never invent content for a
   pathway the map records as empty); its `digest` and `statements`
   (with their beneficiary rewrites) for discipline detail. Carry the
   resolved `code` and `label` into the `cxp-01` record at step 9.
3. Read the baseline pack for every coupled page at
   `content/context-packs/baseline/$1/<page>.json` and print its
   shape (keys, array lengths, segment counts for `_passage[]`). The
   new pack must match that shape exactly; the shell supplies title,
   displayTitle and instruction, the pack supplies bodies (CP-1c).
4. **LK-1 note (22 September 2026; six-phase migration 8 October 2026):**
   `merge-context.js` reads `$1`'s own `instantiations[]` directly
   (`requireCouplingPlan`) and fills exactly the coupled pages/slots it
   names, by `pageKey` (a crs-04 lesson key, or a wrapper/summative page
   key). The coupling plan already printed in step 1 is what it will
   read; nothing further to check here.
5. Check FCI-1: the pack may vary discipline realisation only; every
   format the shell fixes stays fixed.
6. Print the plan: file list to create, character placement per
   CP-1f at `content/context-packs/$2/$1/context.json`, word-count
   targets copied from baseline, and the subject-benchmark grounding
   from step 2 (or a stated note that the pack is ungrounded, if step 2
   returned a gap). Ask for confirm.

Phase 2 (execute, after confirm):
7. Write `context.json` and one pack file per coupled page, British
   English, Voice Specification register, grounded in the subject
   benchmark reference from step 2. No stated counts in note
   bodies unless the contrast is the teaching point (5.66).
8. Run `node tools/merge-health.js` and `node voice-lint.js
   --course=$1` (confirm voice-lint reads pack content; if it does
   not, say so per 5.71). Grep the merged output for `$3` and for any
   unresolved `{{` token. Paste real output.
9. Append this context pack's CXP gate records. The CXP per-pack gates
   (`cxp-01`, `cxp-02`, `cxp-04`) carry `repeatsPer: context-pack`, so each
   pack's records are keyed by a **composite gate id** `$1-$2-<nn>` — the
   base course slug, the subject slug, and the gate's short id (gate-redesign
   -2026-10-06.md, D1, 8 October 2026; the course-design gateId pattern
   admits this composite form). Write, in order:
   - **`$1-$2-cxp-01`** (subject): human-specified, `decidedValue`
     `{ "subject": { "scheme": <hecos|cah>, "code": <code>, "label": <label> } }`
     taken from step 2's resolver result (`resolved.code`, `resolved.label`,
     and `resolved.level` as the scheme), not re-derived by hand. The
     `cxp-01_subject` decidedValueShape forbids any other key under `subject`,
     so record the resolved `benchmark.id` and matched code in the record's
     `grounding` (a pointer to the catalogue entry), never in `decidedValue`.
     If step 2 returned a gap, record the subject as named with
     `scheme`/`code` null and note the gap in `grounding`. Hard-stop.
   - **`$1-$2-cxp-02`** (qualifiers): human-specified, `decidedValue`
     `{ "qualifiers": [...] }` — up to three, the empty array `[]` when the
     pack carries none (the gate is hard-stop, so the record is always
     written, even empty). Hard-stop.
   - **`$1-$2-cxp-04`** (context-generation, old D1): provenance from the
     human's confirm, sessionRef "claude-code: $1 cxp-04 $2 <date>".
   The reserved gate `cxp-03_exemplar-programmes` is subject-independent and
   opened ONCE per course by `/cxp-open` (not per pack); it is never written
   here.
10. SHOW-DIFF-STOP. Explicit staging. One commit. No push.
