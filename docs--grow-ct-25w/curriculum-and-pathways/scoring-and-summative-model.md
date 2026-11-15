# Scoring, Pass/Fail & the Formative → Summative Model

*A design note for when delivery tiers are built. The pilot is deliberately formative-only (it proved the pipeline, not grading). This records how to enable scoring and pass/fail, the formative→summative pattern, and the design questions to answer BEFORE switching anything on. Nothing here changes the pilot; it's a reference for tier design.*

**Status:** design reference. Scoring is NOT enabled in the pilot and shouldn't be until a delivery tier's design calls for it.

---

## 1. The mechanism (how scoring / pass-fail is enabled)

All supported by components you already have; this is configuration, not new building. Three layers move together:

- **Component level** — a question component (mcq, matching, `adapt-abbott-sortable`) becomes scored by setting `_isPartOfAssessment: true` and a `_questionWeight`. Left `false` (the pilot default) it's formative: it teaches and gives feedback but contributes no score.
- **Assessment level** — the `assessment` extension (already installed) groups scored questions into an assessment, sets a **pass mark** (e.g. 60%), and controls attempts, randomisation, and question banking. This is where pass/fail actually lives.
- **Reporting level (spoor)** — spoor's `_reporting` decides what goes to SCORM/Moodle: `_onTrackingCriteriaMet` / `_onAssessmentFailure` and whether to report on completion, pass/fail, or both. Change this and Moodle's Score column and completion status reflect real marks (the pilot reports completion-only, which is why Moodle showed score 0 — correct for formative).

**Moodle side must agree:** once you report a score and pass/fail, set the Moodle SCORM activity's grading method to use the score and its completion condition to "require passing grade." The two sides must match or Moodle will look broken when it isn't. (Proven: the pilot's completion-only reporting tracked correctly once Moodle was set to status-based completion.)

---

## 2. The formative → summative pattern

The natural shape for a pathway-tier: **a series of formative component lessons that teach and let the learner practise without stakes, then a summative assessment at the end that counts.**

- **Formative lessons** stay as the pilot lessons are: `_isPartOfAssessment: false`. Low-stakes checks (the sortable, the teaching-style mcq feedback) build the skill. No score, no gate.
- **Summative assessment** at the end: one or more `_isPartOfAssessment: true` questions grouped by the assessment extension, with a pass mark, reported to Moodle.

Both modes coexist in one package without conflict — formative components simply don't contribute to the score; the assessment extension counts only what's marked summative. No need to separate them into different courses.

### Two design choices to make deliberately

1. **Where the summative assessment sits structurally.** Preferred: a **dedicated end-of-tier assessment page** after the lesson pages (reads clearly as "the graded bit," easy to set a pass mark on, keeps the formative/summative line visible), rather than woven into the last lesson.
2. **What the summative questions test.** Make the end assessment test **synthesis across the parts**, not a re-ask of each part's formative check. The formative checks test each stage; the summative should confirm they've come together. That's the difference between "did the lessons" and "learned the thing" — and it's what earns the assessment its summative status.

---

## 3. Parity is a TIER property, not a context property

Important framing, because it's easy to get backwards.

Each context is a **separate course** (criminology-introductory is its own package; sports-journalism-introductory is another). Summative questions in different contexts are therefore **not** competing in one gradebook and do **not** need to be interchangeable. So parity is NOT "these two context questions must be equivalent within one assessment."

Instead, **summative equivalence is calibrated per tier.** Whatever context it sits in:
- an **introductory** summative assessment should sit at the introductory tier's level of demand;
- an **intermediate** one at its (higher) level; and so on.

What's held constant across contexts is the **complexity and phrasing of the questions, calibrated to the tier** — not the surface content. Criminology-introductory and sports-journalism-introductory summative questions can be entirely different in subject matter, but should be **equivalently demanding** because both are "introductory." The context varies *what* the question is about; the tier governs *how hard and how it's phrased*.

**This ties to existing authority:** the tier is already the unit of difficulty (introductory/intermediate/advanced defined by complexity and prior experience). The Voice Specification's tier calibration (§16 and the tier language/cognitive-demand guidance) is what carries summative parity across contexts. So when authoring a summative assessment for a new context, calibrate it to the *tier's* established complexity and phrasing — do not try to match another context's specific questions.

### Consequence for the context-overlay tooling

When summative content sits in a context slot, the generation/authoring of that slot must respect **tier calibration** as the equivalence standard. A summative context slot is authored to the tier's demand level (via the Voice Specification), not matched question-for-question to a sibling context. Formative slots are forgiving of variation; summative slots must hold the tier's demand level consistently.

---

## 4. When to decide this

Per pathway-tier, at design time — as part of "what is this lesson/tier for": what's practice, what counts, what does the graded bit test, and what's the pass mark. The mechanism is trivial to implement once decided; the decision deserves the same deliberateness as the rest of the design (pressure-test the teaching first, then build). Keep the pilot and any early tiers formative until a tier's purpose genuinely calls for summative assessment.

---

## 5. Resolved: Academic Writing introductory tier

Resolved 16 July 2026, at the pre-C2 scoring-design gate. Scoped to Academic Writing introductory only — §4's general per-tier gate remains open for every other pathway-tier's own design time.

**(S-1) Structural placement: dedicated end-of-tier assessment page.** Adopted per §2's stated preference. Also adopted as the programme default going forward, so future tiers don't re-litigate this unless a tier has a specific reason to deviate.

**(S-2) What the summative tests: recognition-level, not produced-writing quality.** The installed scoreable components (mcq, matching, textInput exact-match, adapt-abbott-sortable) cannot assess whether a piece of prose is well-argued or well-structured — there is no component that grades writing quality. AW introductory's summative therefore tests recognition and application of the writing-cycle process, synthesised across the introductory lessons: identifying the steer/keywords in a new essay question, sequencing the writing-cycle stages for a given scenario, and spotting/fixing a flaw in a short flawed extract. Recognition-level, matching the tier-specification's D2 introductory cognitive-demand row (see tier-specification.md §5). **Explicitly out of scope:** authentic assessment of produced student writing — that would need a human-marked channel outside Adapt/SCORM entirely, and is a separate decision if ever wanted, not assumed by this one.

**(S-3) Pass mark: 70%.**

**(S-4) Attempts: unlimited.** Not attempt-limited.

**(S-5) Confidence-component interaction (mechanical, not a new decision).** Once this assessment page exists, AW introductory's confidence post-instance `_hasSummativeFollowing` (AR-5, open-decisions.md #19) is set `true` at assembly, selecting the "tested by the assessment ahead" feedback phrasing over the application/practice default.
