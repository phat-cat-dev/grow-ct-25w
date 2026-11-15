# Backlog

Deferred pipeline improvements. Living list; add items as they surface, strike them when done.

## BK-1 — Onboarding recorder (durable pre-manifest ONB record)

The four ONB answers (`onb-01`..`onb-04`) are held only in scratchpad plan files
and the conversation until `/new-course` writes them into the manifest. The
manifest is not born until `onb-04`, so there is no repo-durable record of ONB
while it is in progress: a dropped session mid-ONB loses the answers.

**Build:** a pending-onboarding file in the repo, e.g.
`courses/_onboarding/<working-name>.json`, created at `onb-01` and appended as
each ONB gate confirms (committed per gate, like a mini-`/land`). `/new-course`
reads that instead of a throwaway scratch file, then archives/removes it once the
real manifest exists. Working-name = the theme once `onb-02` sets it (a timestamp
before). Makes ONB durable, resumable and auditable.

Does not block authoring an existing course. Raised 8 Oct 2026.

## BK-2 — Strands/scope must be generated against the tier specs (do BOTH)

`crs-02_thematic-scope` must define its scope and 5-10 strands against the tier,
consulting both the generic tier model (`docs/curriculum/tier-specification.md`)
and this pathway's per-tier content assignment
(`docs/curriculum/pathway-tier-mapping.md`). This session proved the need: the
first crs-02 scope/strands were pitched too broad for introductory (they pulled in
marking criteria, the feedback cycle and constructivism, which the mapping
reserves for intermediate/advanced) and had to be narrowed by a reopen after
cross-referencing the mapping.

**Do both (confirmed 8 Oct 2026):**
1. **Instruction** — add the tier cross-reference to `gate.md`'s generation step
   for `crs-02` and to the gate store's `crs-02` `generation.parameters`: the
   agent must read the generic tier spec and the pathway's mapping section and
   pitch scope + strands to the pitch's tier before proposing.
2. **Enrich the store** — extend `design-kb/design-kb.pathways.json` so each
   tier carries its content breakdown (what that pathway assigns to
   introductory vs intermediate vs advanced), extracted from
   `pathway-tier-mapping.md`. Then the per-tier content is in the one Layer-1
   store and the agent reads it there rather than parsing the markdown doc.
   Update `design-kb.pathways.schema.json` and the builder accordingly.

## BK-3 — Auto-render the course spec at CRS close

`crs-05_course-spec` auto-stands and "produces the course spec / user-facing
course pack (render-doc)", but landing it does not currently run the renderer —
`render-course-spec.js` was run manually this session. Make the spec md a
guaranteed artifact of closing CRS: wire `render-course-spec.js` into the
`crs-05` landing in `land.md` so it always generates, every course, not
optionally. Raised 8 Oct 2026.

## BK-4 — les-01 "three activity proposals" are shape x component alternatives (choose-one)

The three `activityProposals` at `les-01` are **three alternative ways to present
the lesson's core content, each in a different Adapt component, from which the
human selects one**. They are chosen on two bases: (a) the **shape** of the
information/content, and (b) how that shape **works with the available
components** (`design-kb.palette.json`). They are NOT a mix of lesson furniture.
The **checklist** (practical-guidance) and the **MCQ knowledge-check** (check) are
defaults/givens, always present, never among the three proposals. Fix `gate.md`'s
`les-01` step 4/6 wording to state this explicitly: propose 3 distinct components
that each present the same content, ranked by shape-fit, for the human to choose
one. Raised 8 Oct 2026.

## BK-5 — pre-flight must not fail an asset-needing component for a missing asset

`gate.md` step 5 (pre-flight) treated a component that needs an image (e.g.
`palette/hotgraphic`) as failing when no image asset exists yet. That is wrong:
there is never an image until the component is chosen. An asset-needing component
is a valid proposal; the asset is recorded as a `visualAssets` placeholder and
supplied later if the option is selected. Pre-flight should check the component's
own structural/config validity against its spec, not require assets to pre-exist.
Fix `gate.md` step 5 accordingly. Raised 8 Oct 2026.

## BK-6 — implement the v2 lesson-page model in the skeletons store (+ schema) — DONE (8 Oct 2026)

Done: schema `standingContextPrompt` field (commit 0de8dfe), store restructure
(commit c6a5682), template alignment (commit 5e8505c). The change was more
contained than first scoped: the former `concept-intro` slot IS the v2 interactive
activity and the `interior` block (slotType `worked-example`) IS the v2 worked
example, so no slotTypes were renamed — `concept-context` and `summary` are
additive coupled slots, and `activity-patterns` needed no change. Original note
retained below for reference.

---



`docs/authoring/lesson-structure-template.md` v2 (8 Oct 2026) defines the agreed
lesson-page model; the skeletons store (`design-kb/design-kb.skeletons.json`,
authoritative per SKS-1) still carries the older structure. Bring the store into
line, and update `design-kb.skeletons.schema.json`:
- **Concept = two components**: a generic `concept-definition` (shell) and a
  coupled `concept-context` (whole-prose, marker part). 
- **Worked example** = structured-fields coupling + character tokens; keep it a
  distinct block after the interior/activity.
- **Summary** = structured-fields coupling (was shell).
- **Practical guidance** = token-substitution (`{{context}}`); **orientation** =
  shell + optional `{{context}}`.
- Add, per coupled slot, a **standing context prompt** field (layout-level
  instruction the CXP agent applies), e.g. concept-context "what does this look
  like in practice within the given context?"; worked-example "subject-specific
  surface example + a prominent theory showing deep learning -> conceptual
  understanding; use the cast"; summary "recap what the learner can now do in
  their context".
- Register the token system: `{{context}}` (the context definition label) and
  character tokens (`{{learner-a}}` ...), resolved at CXP.
Until this lands, template v2 is ahead of the store; the store is authoritative on
conflict (SKS-1), so treat v2 as the target.

## BK-7 — generator + merge-context for the v2 model — GENERATOR DONE (8 Oct 2026); merge-context PENDING (CXP phase)

Generator done: `tools/generate-course-shell.js` emits the v2 structure with no
code change for the block layout (it is data-driven: it iterates the archetype's
blockSequence and parents by `roleToSection`, both already covering the new
concept blocks). The one generator change needed was marker-writing (commit
5e1847f): single-realisation always-coupled slots the generator creates directly
(the wrapper practice-connection slots, and the lesson concept-context and summary
slots) now carry `slot__<page>__<slotType>` from the generator — this also fixed a
pre-existing gap where the wrapper practice-connection markers MK-1 Part 2 requires
were never written. ULAF-introductory re-scaffolded (commit 0ec39e3);
manifest-completeness clause 4 and MK-1 PASS, voice-lint and
validate-design-schemas PASS, the remaining clause fails are the documented
empty-instantiations forced-fails.

**Still PENDING (CXP phase, with BK-8's cxp-05):** `merge-context.js` must resolve
the new token types (`{{context}}` label; character tokens from the context pack's
cast) and fill the structured fields and whole-prose follow-ons from the pack,
driven by the standing per-slot prompts. Not exercised until a context pack is
built, so deferred to the CXP phase.

## BK-8 — cxp-05_characters gate + les-01 gate guidance

Two parts. **(a) les-01 guidance (needed NOW, to author L01 under v2).** Update
`gate.md` and `land.md` for the v2 lesson model:
- `gate.md` SO-1 slots object (component choices) is UNCHANGED in shape —
  `concept-intro` (now the interactive activity), `interior` (worked-example) and
  `practical-guidance`, plus `check` (AL-3). What changes is the framing: the
  concept is a definition that does NOT spoil the activity; `concept-intro` is the
  interactive exploration proposed as 3 shape x component alternatives (BK-4);
  record the standing per-slot context prompts; apply the BK-5 pre-flight fix (an
  asset-needing component is a valid proposal).
- `land.md` les-01 authoring adds the two new generic blocks: `concept-definition`
  (author the generic definition of the lesson topic, why-before-how, no spoiler)
  and `concept-context` (left EMPTY in the shell — the generator already wrote its
  `slot__<page>__concept-context` marker; CXP fills it). `summary` is now a
  structured-fields coupled slot (generator wrote `slot__<page>__summary`); author
  the generic recap frame at land, CXP fills subject fields. `worked-example` is
  structured-fields + character-token cast. The concept-context/summary markers are
  generator-written (not from les-01 coupledSlots); the concept-intro/
  worked-example/check-context markers are still written at land from coupledSlots
  (MK-1 Part 1, unchanged).

**(b) cxp-05_characters (CXP phase).** Add `cxp-05_characters` to the gate store:
`agent+human`, the agent proposes a small diverse cast
(Welsh/British/Indian/African/Chinese names), the human confirms; runs before
`cxp-04_context-generation` so the names exist when pack content is generated;
stored in the context pack; reused for that context across all pathways and tiers.
