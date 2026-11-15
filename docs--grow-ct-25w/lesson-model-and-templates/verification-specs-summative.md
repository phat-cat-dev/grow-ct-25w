# A56 — SUMM verification specification

Written 15 September 2026 against Phase 4 cluster 6's four rulings (all recorded on A21's own
row, `docs/project/audit-2026-09/audit-actions-arising.md`). This document rules nothing. It
specifies what a future check would test, once built and wired (A80). Where a cluster 6 ruling
left something open, the corresponding item here is recorded as blocked or not mechanically
checkable, not filled in.

**Scope.** Per RBD-1 (`open-decisions.md`), the four built courses (AWI, AWM, AWA, PRI) are
reference material, not the target of this check. This specifies a check for Phase 6's builds —
courses designed anew through the gate process, against the rulings below. It is not run against
the four existing courses as an acceptance test.

**Authorship note.** A56's original proposal (SUMM sheet I6, its own row) predates every cluster 6
ruling below by up to a month. Section 1 tests each of its ten original items against what is now
ruled, since the checklist itself has drifted and the drift is not uniform: some items are
confirmed unchanged, some are sharpened by a ruling into something more concrete, one is narrowed
by scope, one is reversed, and one is blocked.

---

## 1. Drift: the original ten items against cluster 6's rulings

A56's original checklist, verbatim, is ten items: (1) 5 to 7 items; (2) outcome mapping with no
contradiction of lessons; (3) tier-row pitch; (4) attempts and feedback consistent with purpose;
(5) no positional references on shuffled options; (6) pass mark and introduction present; (7)
debrief items for the fail path; (8) learner-facing titles; (9) labels matching stems; (10) page
completion against pass.

| # | Original item | Drift | What replaces it |
|---|---|---|---|
| 1 | 5 to 7 items | **Contradicted.** Item count is tier-scoped (Attempts/Item-count ruling, Paper 2 Q4b, Option 2), settled at each tier's own design time; SM-2's 7–8 mix is not a programme default. Served counts already exceed the ceiling: AWI 8, PRI 8 (AWM 5, AWA 4). The `design-kb.skeletons.json` `role: summative` entry cites this same contradiction directly against AUD-PRI-SUMM-3. **The fixed range is replaced with no fixed number at all, not with a different number.** A reader looking for the figure that superseded "5 to 7" will find none, because the ruling settles the question as tier-scoped rather than choosing a new programme-wide count — absence of a replacement number is the ruling working as intended, not a gap in this record. | §2 item A: count is checked against the tier's own recorded design decision, not a fixed range. |
| 2 | outcome mapping with no contradiction of lessons | **Sharpened.** Results content ruling (Paper 4 Q4b, Option A) gives "outcome mapping" a concrete definition: `_resultsDebrief` covers every assessable question in the targeted assessment. "No contradiction of lessons" is not itself a clause of that ruling. | §2 item E checks coverage mechanically. The contradiction-of-lessons half is not mechanically checkable — see §4. |
| 3 | tier-row pitch | **Unchanged.** No cluster 6 paper rules on whether a tier's SUMM items are pitched at that tier's level; Item count/type's "settled at each tier's own design time" (Option 2) establishes that each tier designs its own SUMM, but not a rule for judging the pitch. | §4 (not mechanically checkable — human review against the tier's own design decision). |
| 4 | attempts and feedback consistent with purpose | **Confirmed and split into two concrete rulings.** Attempts: Paper 2 Q4a, Option 3 (per-item `_attempts: -1` within a sitting; assessment-level attempts bounded, number unruled). Feedback: Paper 3 Q4a, Option A (`notFinal` + `correct` pairing, not `notFinal` + `final`, since `final` is structurally unreachable under `_attempts: -1`; §15.5 applies). | §2 items B, C, D. |
| 5 | no positional references on shuffled options | **Unchanged in substance, sharpened in stakes.** The Attempts ruling makes `_randomisation._isEnabled: true` a load-bearing dependency of the ruled retake mechanism (currently `false` on all four built courses). A positional reference was always wrong; under this ruling it is wrong on a component the ruling now requires to shuffle. | §2 item F. |
| 6 | pass mark and introduction present | **Split.** "Introduction present" is unchanged, still checkable. "Pass mark present" cannot be checked as a presence requirement while `_passReveal`'s own disposition is deferred, not ruled (Paper 4 Q4c) — the ruling points toward retiring it, pending the retake number (Phase 6). | §2 item G (introduction only); §3 (pass mark, blocked). |
| 7 | debrief items for the fail path | **Narrowed scope, contradicted as written.** Results content (Paper 4 Q4b, Option A) requires `_resultsDebrief` to cover every assessable question, not only the fail path. "For the fail path" is too narrow a reading of the ruling that now governs this. | §2 item E replaces this item; it is not "fail-path debrief" plus something else. |
| 8 | learner-facing titles | **Unchanged.** No cluster 6 paper addresses component titling; standing voice-spec convention. | §2 item H. |
| 9 | labels matching stems | **Unchanged.** No cluster 6 paper addresses ARIA labelling; standing structural convention (radiogroup `aria-label` against the visible stem, the same pattern already captured for evidence in `pri-auto-evidence-spec.md` §3). | §2 item I. |
| 10 | page completion against pass | **Reversed, not merely sharpened.** The original framing implies completion should track pass/fail. The `role: summative` skeleton's own landed `namedDependencies` clause rules the opposite: "Completion state is never rendered as a pass verdict. Completion means attempted, not passed" (citing AUD-PRI-SUMM-1 as the defect shape — a menu card reading "Completed" while the block's own progress bar reads incomplete). The pass-mark half is additionally blocked, as in item 6. | §2 item J checks the two signals stay decoupled; §3 covers the pass-mark half. |

---

## 2. Checkable items

Each item states what it checks as an applicable rule, the artefact it reads (per A94) and why,
its trigger scope (per CTS-1 as amended — see the note on scope count below), what would run it,
and whether it reports or blocks.

**LK-1 flag (22 September 2026, not a correction):** the paragraph below rests on
`CONTEXT_COUPLED_LESSONS` being a fixed list, the same for every tier, that never named SUMM.
That list no longer exists in `merge-context.js` (Prompt 154, LK-1). `design-kb.skeletons.json`'s
`skeletons/summative` archetype gives its `summative-item` slot `contextCoupling:
["token-substitution", "structured-fields"]` — not `["none"]` — so the skeleton itself does not
rule out SUMM items being context-coupled. **Corrected 22 September 2026 (Prompt 155):** the
paragraph as first written concluded from this that "a course's own A5 record can couple SUMM's
items" — that conclusion is wrong. CPL-1 (`open-decisions.md`) restricts gate A5's `page` field to
either an A3 lesson's own `pageKey`, or the literal string `wrapper-open` or `wrapper-close`; SUMM
is none of these, so CPL-1 provides no way to plan coupling for SUMM at all, whatever the
skeleton's own `contextCoupling` array allows. **Settled 22 September 2026 (SQ-1, Prompt 156):** the question above is closed, not open. Summative
questions are not tailored to context at all — CPL-1 does not need extending to let a course plan
coupling for SUMM, because SUMM items are never context-coupled. `design-kb.skeletons.json`'s
`skeletons/summative` archetype now gives its `summative-item` slot `contextCoupling: ["none"]`,
matching this. Re-deriving §2's artefact choice for items A-I is a separate question from
documenting the marker and pack-naming change.

**Artefact, all items A–I (pre-LK-1 text, unresolved by the flag above):** the **shell**
(`src/course/en/*.json` for the course under design). SUMM's items are not context-coupled
lessons under CPL-1 (see the corrected flag above). **Corrected 22 September 2026 (Prompt 155):**
the claim that `merge-context.js`'s now-removed `CONTEXT_COUPLED_LESSONS` object "confirmed only
the C-PRE/C-POST confidence lessons sat in it, for every tier" is wrong. The actual object (`git
show 30cd660 -- merge-context.js`) held four courses' own lesson slugs — academic-writing-introductory
(understanding-the-task, planning, drafting, editing, proofreading, common-errors),
academic-writing-intermediate (clarity-precision, structuring-argument, integrating-sources,
four-pillars, genre-awareness), academic-writing-advanced (conventions-in-practice, critical-edge),
and presenting-introductory (reading-the-brief, research-and-planning, structuring-your-argument) —
and never named C-PRE, C-POST or SUMM at all. So a SUMM authoring defect survives unchanged into
any generated variant, and the shell is both sufficient and the correct place to fix it, per A94's
per-check-type guidance (authored-content conformance reads the shell). Item J is the one exception
— see its own row.

**Trigger scope, all items A–I:** **course-scoped, fixed artefact**, in CTS-1's own four-scope
terms (`open-decisions.md`, the "these four" summary line) — recomputed per authored course
because SUMM's item count, attempts and debrief mapping are each authored per tier, not shared
across the programme. Not decision-scoped: the check reads authored course content, not only the
decisions register. Item J differs — see its own row.

| Item | What it checks | What would run it | Reports or blocks |
|---|---|---|---|
| **A. Item count** | The authored SUMM's item count matches the count recorded in that tier's own design decision (not a fixed 5–7 range). | No existing tool cross-reads authored `components.json` against a tier's own recorded design decision. Nearest existing pattern: `validate-design-schemas.py`, already design-kb-aware (reads `design-kb.gates.json`); this would be a new check in the same family, not an extension of an unrelated tool. Name and location not proposed here, following A98's own precedent for saying so plainly rather than inventing a home. | Blocks. A count that does not match the tier's own decision is a build defect, not a warning. |
| **B. Per-item attempts** | Each SUMM question's `_attempts` is `-1` (unlimited within the sitting), per Paper 2 Q4a Option 3. | Same new-validator family as A. | Blocks. |
| **C. Assessment-level attempts bounded** | The assessment-level attempts figure is a small fixed number, not unlimited. **Checkable in form only** — see §3, the number itself is unruled. | Same new-validator family as A. | Reports only until the number is ruled (Phase 6); blocks once it is. |
| **D. Feedback pairing** | Authored `_feedback._incorrect.notFinal` and `_feedback.correct` are both present and non-empty; `_feedback._incorrect.final` is not required (per Paper 3 Q4a, `final` is structurally unreachable under `_attempts: -1` and is not a target for this role). Voice: §15.5 (never a bare verdict) applies to both fields present, per `mcq.md` §4's mapping (already landed, not new). | `voice-lint.js` for the §15.5 clause (existing tool, existing pattern — same clause class as knowledge-check feedback); the presence/absence-of-`final`-as-non-target clause is new, same family as A. | Voice clause: reports (voice-lint's existing convention for its non-order-violation clauses, per A80). Presence clause: blocks. |
| **E. Results debrief coverage** | Where `_resultsDebrief` is enabled, its mapping covers every assessable question in the targeted assessment (Paper 4 Q4b, Option A). Cross-referenced with A100, which is this ruling's own instance of a gap (AWA's empty `_items`). | Same new-validator family as A; natural extension point once A100's own check exists, since both read the same `_resultsDebrief` structure. | Blocks. A gap in coverage is the AWA/A100 defect class directly. |
| **F. Randomisation on shuffled options** | Where a SUMM mcq/gmcq presents options in a randomised order, `_randomisation._isEnabled: true` is set on the article (now load-bearing per the Attempts ruling, not merely good practice), and no authored option text or feedback string contains a positional reference ("the first option", "as above", etc.). | The positional-reference half is `voice-lint.js`'s existing territory (a text-pattern check); the `_randomisation._isEnabled` presence half is structural, same new-validator family as A. Two different tools for one checklist item — recorded as such, not merged into one false single check. | Positional-reference half: blocks (a positional reference on a shuffled option is a defect, not a style note). `_randomisation` presence: blocks, since the Attempts ruling makes it load-bearing. |
| **G. Introduction present** | The SUMM article/page carries an authored introduction (the "introduction present" half of the original item 6; "pass mark present" is severed — see §3). | Same new-validator family as A, or `conformance-lint.js` if introduction presence is expressed as a block-order/structural clause rather than a content-presence clause — either is defensible; not decided here. | Blocks. |
| **H. Learner-facing titles** | Component `displayTitle`/title fields read as learner-facing copy, not internal ids or placeholder text. | Voice convention; `voice-lint.js` territory by pattern, though no existing clause is confirmed to cover this specifically — recorded as an extension, not confirmed already covered. | Reports (consistent with voice-lint's existing non-order-violation clause convention). |
| **I. Labels matching stems** | Question components' `aria-label` (or equivalent) matches the visible stem text. | No canonical tool currently reads rendered ARIA output; this is presently an evidence-capture item (`pri-auto-evidence-spec.md` §3 already records it for PRI, manually assembled) rather than a lint-time check, since it requires a served DOM, not just authored JSON. | Reports, and only as a built-course check (see item J's artefact note) — not a shell-JSON check like A–H. |
| **J. Completion decoupled from pass** | The page's completion state is never rendered as a pass/fail verdict (completion means attempted, per the landed `role: summative` skeleton `namedDependencies` clause). **Artefact: whichever artefact `src/course` resolves to when the check runs**, per A94's A91 guidance — this is a property of a built, served course, not a static JSON read. **Trigger scope: course-scoped, resolution-dependent artefact** (CTS-1's third named scope), not fixed-artefact like items A–I. | Nearest existing check is A91 itself (completability), or a new clause on it — not proposed as a separate tool, since A91 already owns "whichever artefact is live" as its defining trait. | Blocks. A completion signal that reads as a pass verdict is the AUD-PRI-SUMM-1 defect class directly. |

**Note on CTS-1's scope count.** The relay prompt for this task describes CTS-1 as carrying "four
scopes and two qualifiers." Reading CTS-1's own text fresh for this specification, its body
(`open-decisions.md`) contains a passage calling the A91 resolution-dependent-artefact addition "a
qualifier on the existing course-scoped value, not a fourth named scope," and a second passage two
paragraphs later, in the same decision code, giving a four-item summary ("component-scoped,
course-independent; course-scoped, fixed artefact; course-scoped, resolution-dependent artefact;
decision-scoped, course-independent") captioned "No scope beyond these four is named." These two
passages do not agree with each other on whether the count is three scopes plus one qualifier, or
four scopes outright. This specification uses CTS-1's own four-item summary line, since CTS-1
itself designates that line as the authoritative count ("no scope beyond these four"), but the
inconsistency is CTS-1's own and is unresolved by this document. See the close report.

---

## 3. Blocked items

These are checkable in form but not in value: the rule for what to check is settled, but the
value to check against is not yet chosen.

- **Assessment-level attempts, the number itself.** Ruled bounded (Paper 2, Option 3); the figure
  is explicitly Phase 6's to choose, not fixed by cluster 6. §2 item C checks the form (a small
  fixed number is set, not `-1`) but cannot check a specific value until Phase 6 rules one.
- **Pass mark.** Blocked on two separate open items, not one: `_passReveal`'s own disposition is
  deferred (Paper 4 Q4c, pointing toward retirement but not settled, itself dependent on the
  retake number); and, separately, what a pass mark means for Moodle's gradebook sits behind
  A73's Moodle-blocked rows (whether Moodle's grading method reads `scaled` or normalises `raw`
  under SCORM 2004) — a question A21's own closure notes "no recon on `grunt server` can answer."
  Nothing in this specification substitutes a guess for either.

---

## 4. Not mechanically checkable

- **Item character: synthesis across lessons, not recall within one.** This is the standing
  design requirement behind the Purpose ruling (Paper 1: "the summative is a teaching instrument
  ... teach[ing] the synthesis the separate lessons do not individually teach, using the
  assessment format as the vehicle rather than as a check of prior knowledge"). Whether a given
  item tests synthesis or recall is a judgement about what the item is actually asking, not a
  structural property any tool here can read off JSON. **What a human review would need to look
  at instead:** each item's stem and correct-answer rationale against the specific lesson content
  it draws on, asking whether answering it requires combining more than one lesson's content or
  only reproducing one lesson's stated fact. No proxy (item length, number of lessons cited in the
  stem, keyword overlap with lesson text) is proposed here as a stand-in for this judgement; each
  would be gameable or wrong in ways that misrepresent the ruling as satisfied.
- **Tier-row pitch** (original item 3). No cluster 6 paper rules a mechanism for judging whether a
  tier's SUMM sits at that tier's level. Human review against the tier's own design decision,
  alongside the item-character review above, since both turn on reading item content against
  intent rather than structure.
- **"No contradiction of lessons"** (the second half of original item 2). Coverage is mechanically
  checkable (§2 item E); whether the debrief text itself contradicts what a lesson taught is a
  content-accuracy judgement, not a structural one.

---

## 5. Where this specification lives

**Ruled, 15 September 2026 (Abbott, against this document's own §5 proposal as first written).**
Verification specifications scheduled out of a cluster paper under CVS-1 — a complete specification
with no open judgement call left in it — live in `docs/authoring/verification-specs/`, one file per
specification. This one is `docs/authoring/verification-specs/summative.md`. Reasoning recorded at
the ruling: A56, A80 and A24 were all scheduled out of cluster papers under CVS-1 as complete
specifications, and none of the three had anywhere to live; settling the location once for all
three beats settling it three times, since the pattern repeats for every future CVS-1 exit. A80 and
A24 are not yet written, so this document was moved into the location first.

This document originally proposed `docs/project/audit-2026-09/`, alongside `pri-auto-evidence-spec.md`
— the one precedent then found for a named, committed specification document in this repo, though a
different genre (capture instructions rather than pass/fail rules). That proposal is superseded by
the ruling above, recorded here rather than silently erased. A56's own row carries a short pointer
to this file rather than the specification's own content, since the content here is far longer than
fits a row without repeating the oversized-row problem already found on A21's.
