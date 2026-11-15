# Course Creation Prompts

*Copy-paste prompts for Claude Code, one per phase/write moment of
`docs/authoring/course-creation-workflow.md`. REWRITTEN 27 August 2026
(away-week Session 3) against the S3-D1–D9 decision set. Every prompt
here writes what a claude.ai design conversation has already decided
and closed — none makes a design decision. Each assumes the workflow
document exists and is current; none restates its content beyond what
a Claude Code session needs pasted directly into it. Not yet tested
against a real course build under this model.*

---

## Prompt 1: Phase A close — folder, manifest scaffold, gate records

*Run once, after Phase A's gates (§1 of the workflow) have all closed
in the design conversation and the phase-close ledger has been swept.*

```
Confirm pwd ends in wkspc2614-ADAPT (per CLAUDE.md's own
check); cd there first if not.

This is a Phase A close-write task per
docs/authoring/course-creation-workflow.md §1 and §7. The design
conversation has already closed every Phase A gate (CTX, A1-A7); I am
pasting the confirmed ledger below. Do not re-open, re-derive, or
second-guess any of it — this task only writes what's already decided.

CONFIRMED LEDGER:
[paste the full Phase A ledger from the design conversation: pathway,
tier, slug; the CTX facet set with each value marked
declared/derived-with-citation/defaulted plus its grounding; A2 source
type and scope; A3 lesson breakdown; A4 visual-overview
pattern/realisation/coupling triple; A5 coupling plan; A6 confidence
items + bridge ruling; A7 resources ruling; any groundingGaps recorded
this phase]

Do this, in order:

1. RECON FIRST. Check whether courses/<slug>/ already exists. If it
   does, stop and tell me — do not overwrite.
2. Create courses/<slug>/ per §2's folder discipline (permanent name
   from day one, no sandbox).
3. Write course-design_<slug>.json (the manifest, per S1-D5): facet
   set, gate records for CTX and A1-A7 with provenance and grounding
   exactly as given above, no invented fields. Follow
   course-design_amended_schema.json.
4. If any groundingGaps were recorded, confirm they're present in the
   manifest as groundingGaps entries (schema amendment A5), not lost
   in the write.
5. SHOW-DIFF-STOP. Show me the full diff before staging anything.
   Explicit staging only (never git add -A).

Do not proceed to course shape scaffolding (Prompt 2) in this session.
```

---

## Prompt 2: Course shape scaffold — fixed pages, registry entry

*Run once, immediately after Prompt 1's diff is confirmed and staged.
Assumes courses/<slug>/ and course-design_<slug>.json already exist.*

```
Confirm pwd ends in wkspc2614-ADAPT; cd there first if
not.

This is a course-shape scaffold task per
docs/authoring/course-creation-workflow.md §2. courses/<slug>/ and
course-design_<slug>.json already exist from the prior task — RECON
FIRST: read the manifest, confirm the facet set and A3 lesson
breakdown, and confirm the folder is empty of page content so far.

Lesson breakdown (from the manifest's A3 record): [paste the
confirmed lesson list, order, and slugs]

Do this, in order:

1. Scaffold the fixed-page sequence per §2's standing shape:
   W-OPEN -> C-PRE -> [lessons, in the order above] -> SUMM -> C-POST
   -> W-CLOSE. Use the archetype/skeleton definitions in
   design-kb/design-kb.skeletons.json where populated; where a
   skeleton isn't yet populated, use the current authoring templates
   (wrapper-open-template.md, c-pre-template.md,
   lesson-structure-template.md, summative-template.md,
   c-post-template.md, wrapper-close-template.md) as the reference
   shape, and note in the manifest's instantiation notes that this
   page was built from template, not skeleton, pending population.
2. Create contentObjects.json / articles.json / blocks.json /
   components.json entries for structural shell ONLY — page and
   article scaffolding, no lesson content yet (that's Prompt 3, per
   lesson). Also create config.json, copied from the nearest tier
   sibling (5.85) — it holds framework settings only (theme, menu,
   accessibility, SCORM tracking behaviour), never course content.
   Every block scaffolded here carries `_skeletonKey`, set to the
   blockSequence key it fulfils in the archetype used for that page
   (design-kb/design-kb.skeletons.json) — e.g. a lesson's orientation
   block gets `"_skeletonKey": "orientation"`. Where a page is built
   from template rather than skeleton (step 1's fallback), leave
   `_skeletonKey` unset and say so in the manifest's instantiation
   notes, same as the template-vs-skeleton note itself (5.39 option B;
   see project-backlog.md 5.39).
3. Write content/shells/lesson-registry.json entries for this course
   as a generated view per S1-D6/§2 — do not hand-edit an existing
   registry entry for a different course; only add this course's
   entries.
4. SHOW-DIFF-STOP. Show me the full diff before staging. Explicit
   staging only.

Do not encode lesson interiors, SUMM, or wrapper content in this
session.
```

---

## Prompt 3: Lesson build — write one closed lesson

*Run once per lesson, after that lesson's Phase B session (§3 of the
workflow) has closed both movements in the design conversation.*

```
Confirm pwd ends in wkspc2614-ADAPT; cd there first if
not.

This is a lesson-write task per
docs/authoring/course-creation-workflow.md §3 and §7. The design
conversation has already closed this lesson's substance movement
(B1-B3) and interaction movement (B4-B7); I am pasting the confirmed
gate records below. Do not re-derive, re-propose, or second-guess any
of it — every proposal already went through the S3-D4/D5/D6 grammar
in the design conversation. This task writes what's decided and
authors the prose that expresses it.

Course: [pathway]: [tier] Stage (slug: [slug]).
Lesson: [lesson name/key, e.g. "Planning"], position [N] of [total].

CONFIRMED LESSON RECORD:
[paste every closed B-gate for this lesson: B1 outcomes; B2 pattern/
realisation/coupling triple + interior reasoning; B3 worked-example
triple; B4 check triple; B5 reflective prompt; B6 trickle/pacing
ruling (note explicitly if page-block order deviates from B2's
default, per the S3-D8 order-vs-pacing clarification); B7 visual
asset ruling; any groundingGaps]

Do this, in order:

1. RECON FIRST. Confirm this lesson isn't already built. Read the
   scaffolded shell from Prompt 2.
2. Author the lesson content per book-to-adapt-mapping-workflow.md's
   established method, using ONLY the confirmed record above for
   teaching-move-to-component decisions — do not choose a different
   component or pattern than what's recorded, even if a different
   choice looks better in the moment. If something in the record
   looks wrong once you're working with the actual source content,
   STOP and flag it back to me rather than silently deviating.
3. Encode as Adapt JSON: page/article/block/component structure,
   _latestTrackingId discipline, lesson-level mcq defaults
   (_attempts:2, _isRandom:true, _shouldDisplayAttempts:true unless
   the record says otherwise).
4. Tag context-coupled content per the coupling triple's variation
   type (token-substitution / structured-fields / whole-prose).
   Generate the baseline context pack and its generation template
   together, per the established two-tier rule (full slot replacement
   for prose, tokens for connective text).
5. Run the mechanical voice-lint if it exists (check
   project-backlog.md for current status); if it doesn't exist yet,
   say so explicitly and tell me this lesson still needs manual
   voice/register review before I treat it as done.
6. Write this lesson's gate records into course-design_<slug>.json,
   provenance and grounding exactly as given above.
7. SHOW-DIFF-STOP. Show me the full diff before staging. Explicit
   staging only.

Do not proceed to the next lesson or to SUMM/wrapper build in this
session.
```

---

## Prompt 4: SUMM & wrapper build

*Run once, after every lesson is built and Phase B is fully closed,
and after S1/W1 have closed in the design conversation.*

```
Confirm pwd ends in wkspc2614-ADAPT; cd there first if
not.

This is a SUMM-and-wrapper write task per
docs/authoring/course-creation-workflow.md §4. Every lesson is built.
The design conversation has closed S1 (summative design) and W1
(wrapper content). I am pasting both confirmed records below.

Do NOT consult summative-template.md for marking, feedback, or
furniture specifics (F7 — it predates the 14 August SUMM changes and
is actively misleading). Use only the record below and the standard
furniture specs (docs/authoring/extension-specs/passreveal.md;
resultsdebrief has no separate spec — cite the backlog record given
below in its place, per F1's policy).

CONFIRMED S1 RECORD (SUMM):
[paste: item list + item-to-lesson mapping; marking config
(_suppressMarking, _canShowFeedback/_canShowMarking); remediation
pointer strings per item; pass mark; retry policy (unlimited, per
S3-D9.7 — do not add an attempts cap unless the record explicitly
says the grinding lever has been pulled); furniture list
(resultsdebrief + passreveal, both standard)]

CONFIRMED W1 RECORD (wrappers):
[paste: W-OPEN block order and content — learning outcomes first,
then overview, then signpost, per the 14 August reorder; W-CLOSE's
four blocks in render order; confirm A6's confidence/bridge ruling is
NOT re-litigated here, only referenced]

Do this, in order:

1. RECON FIRST. Confirm SUMM and both wrapper pages are still
   shell-only from Prompt 2.
2. Build SUMM: items, marking config, remediation feedback strings,
   both furniture extensions configured exactly per the record
   (assessment ID match, guard chains as documented in each
   extension's own spec).
3. Build W-OPEN and W-CLOSE content per the W1 record. Confirm C-PRE/
   C-POST are NOT touched here (they were scaffolded from A6's record
   in an earlier task) — do not move confidence content back onto the
   wrappers.
4. Write the S1 and W1 gate records into course-design_<slug>.json.
5. SHOW-DIFF-STOP. Show me the full diff before staging. Explicit
   staging only.

Do not run the build-readiness lint or package the course in this
session — that's a separate task (Prompt 6), after this diff is
reviewed.
```

---

## Prompt 5: Sweep write

*Run only when a reopen sweep resolves in the design conversation
(§5). Not part of the standard build sequence — fires irregularly,
whenever a dependency-driven reopen closes.*

```
Confirm pwd ends in wkspc2614-ADAPT; cd there first if
not.

This is a sweep-write task per
docs/authoring/course-creation-workflow.md §5. A reopen sweep has
resolved in the design conversation: [name the trigger gate and
changeKind — amended/replaced/re-deferred].

CONFIRMED SWEEP EVENT:
[paste: sweep id; trigger gate + changeKind; every swept gate's
disposition (invalidate/flag-for-review/stand-with-warning) with its
edge, one-line why, and the record evidence cited as grounding;
which invalidates were confirmed and re-closed with what new values
(or confirmed unchanged); any cascade sweeps this one triggered, each
with its own id]

Do this, in order:

1. RECON FIRST. Read the current course-design_<slug>.json's
   sweepEvents array; confirm this event's id doesn't already exist.
2. Append this sweep event (and any cascade events) to the top-level
   sweepEvents array, append-only — never edit a prior entry.
3. For every gate that was re-closed with a genuinely new value,
   update that gate's record as a new, superseding entry (never
   overwrite the superseded one) with provenance human-confirmed and
   changeKind recorded per the paste above.
4. For flags confirmed as stand-with-warning, record the disposition
   on the sweep event; do not touch the underlying gate record.
5. SHOW-DIFF-STOP. Show me the full diff before staging. Explicit
   staging only.

This write happens now, not deferred to a phase close (§5's stated
exception) — that's why this is its own prompt rather than folded
into Prompt 1 or Prompt 3.
```

---

## Prompt 6: Lint & build-readiness check

*Run before any SCORM package is generated — after every build task
above, and again immediately before the Moodle proof run.*

```
Confirm pwd ends in wkspc2614-ADAPT; cd there first if
not.

This is a build-readiness check per
docs/authoring/course-creation-workflow.md §6. Run the 5.13 lint
against courses/<slug>/ and course-design_<slug>.json (check
project-backlog.md for the lint's current implementation status if
you're unsure it exists yet — if it doesn't, say so plainly and don't
improvise a substitute check).

Confirm all three clauses fire, and report each separately:

1. Consumes instantiation notes — any recorded archetype deviation is
   read and NOT flagged as a surprise.
2. Refuses on unresolved sweepEvents — any invalidate or flag without
   a confirmed disposition blocks the build; report which, if any.
3. Reports groundingGaps informationally — lists them, does NOT
   refuse the build on their account.

Report PASS/BLOCKED per clause, not a single overall verdict. If
BLOCKED on clause 2, stop — do not proceed to packaging. If clean or
only clause-3 gaps are present, packaging may proceed as a separate
task.
```

---

## Prompt 7: Records landing

*Run at any phase close that produced groundingGaps, or when a
hardness-regrade question (S3-D1's escape valve) has been raised and
settled.*

```
Confirm pwd ends in wkspc2614-ADAPT; cd there first if
not.

This is a records-landing task per
docs/authoring/course-creation-workflow.md §7.

[Select what applies:]

GROUNDING GAPS: paste the groundingGaps entries recorded this phase
close, from course-design_<slug>.json. Add each to the sourcing list
(docs/project/sourcing-list.md or wherever S1-D6's generated-view
tooling currently writes it — confirm the current location if
unsure) in the established format: store, lookup, what a hit would
have grounded, course/gate it came from.

HARDNESS REGRADE: paste the settled regrade question and its
resolution. Add a new entry to open-decisions.md following the GI-1e
precedent format (question raised, ruling, provenance, grounds).
Update design-kb/design-kb.gates.json's hardness field for the
affected gate if the ruling changes it.

Do this, in order:

1. RECON FIRST. Read the current state of whichever file(s) you're
   landing to.
2. Make the addition(s) via targeted string-asserted replacement, not
   a full overwrite.
3. SHOW-DIFF-STOP. Show me the full diff before staging. Explicit
   staging only.
```

---

## Notes on using these

- **Prompts 1, 2, 6 run once per course** (6 twice: after each build
  phase and again before Moodle proof). **Prompt 3 repeats once per
  lesson**, in teaching order. **Prompt 4 runs once**, after every
  lesson is built. **Prompts 5 and 7 are event-triggered** — they run
  whenever their trigger condition occurs, not on a fixed schedule.
- **Every prompt assumes its design-conversation gate already closed
  in claude.ai.** No prompt here makes a design decision; each writes
  what was already decided. If a prompt surfaces something that looks
  like an undecided question, STOP and take it back to the design
  conversation — don't resolve it in the Claude Code session.
- **CLAUDE.md's working-directory check applies to every prompt**,
  not restated as a caveat each time beyond the first line.
- **Untested against a real second course build** under this rewritten
  model. The prior step-numbered workflow and its prompts were
  exercised once, on the pilot, under a different (undifferentiated
  claude.ai/Claude-Code) division of labour; this sequence has not yet
  been proven end-to-end. Expect friction on first use — flag it back
  into the design conversation rather than silently patching the
  prompt.
