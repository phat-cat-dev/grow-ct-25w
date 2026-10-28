# Adapt course template field map

_Generated 2026-10-10T12:46:08.132Z from `design-kb/design-kb.skeletons.json` (kbVersion 0.1.24). This is a read-only rendering — the skeletons file is the source of truth; edit that, not this report._

## Legend
- **kind**: `fixed` (same shell content/shape in every course) or `variable` (a slot whose filler is chosen per course/lesson).
- **role**: pedagogical role, also used to key `completionRules`/`iconRules` elsewhere in the skeletons file.
- **content coupling**: how the slot's content reaches the learner — `shell-coupled` (written once, generic), `token-substitution` (shell text carrying a `{{token}}`), `structured-fields` (shell frame + named fields filled per subject), `whole-prose` (empty in the shell, written per subject).
- **authoring prompt**: direct instruction for whoever writes this slot's content (shell author or an agent).
- **standing context prompt**: a layout-level instruction a context-pack (CXP) agent applies when filling a coupled slot for a specific subject, on top of the shell's own prose.

## Page order
1. W-OPEN — `skeletons/wrapper-open`
2. C-PRE ("Before you start") — `skeletons/c-pre`
3. LESSON (repeats, one per lesson) — `skeletons/lesson`
4. SUMM — `skeletons/summative`
5. C-POST ("Looking back") — `skeletons/c-post`
6. W-CLOSE — `skeletons/wrapper-close`

## W-OPEN  <!-- skeletons/wrapper-open -->
_pageType: `wrapper-open` · archetype version 0.1.0 · source: docs/authoring/wrapper-open-template.md (Structure Summary)_

### 1. `overview` — "Overview and justification"
- kind: **fixed** · role: **orientation** · required: **true**
- displayTitle (visible heading): _(none — no visible heading)_
- component: `palette/text`

### 2. `learning-outcomes` — "Learning outcomes"
- kind: **fixed** · role: **learning-outcomes** · required: **true**
- displayTitle (visible heading): "Course learning outcomes"
- component: `palette/text`

### 3. `practice-connection` — "In real academic practice"
- kind: **variable** · role: **practical-guidance** · required: **true**
- displayTitle (visible heading): "In real academic practice"
- slotType: `practice-connection`
- component options: `palette/text`
- content coupling: `whole-prose`
- selection model: single-realisation: only palette/text fills this slot. No routing decision; no activity-pattern names this slotType.
- **standing context prompt (CXP agent, filling this slot for a subject):**
  > Recast the generic 'In real academic practice' section in the learner's own subject: show how this topic applies in their actual academic work, with the academic framing first and any professional connection kept brief, as a natural follow-on from the generic version above.

### 4. `signpost` — "Signpost"
- kind: **variable** · role: **furniture** · required: **true** · interactionMode: **passive**
- displayTitle (visible heading): "What's ahead"
- slotType: `visual-overview`
- component options: `palette/hotgraphic`, `palette/narrative`, `palette/text`, `palette/timeline`, `palette/flipcard`
- content coupling: `shell-coupled`
- selection model: furniture: signpost component selected once per pathway at A4 gate. Choice based on visual suitability — hotgraphic for spatial models, narrative for staged tours, timeline for linear/staged sequences, flipcard for a playful reveal of a small item set, text for prose-only. Deliberately excluded from activity-pattern layer (furniture class).
- authoring advice: _(none recorded for this slot — furniture, or a routing-only slot)_

### 5. `course-instructions` — "Course instructions"
- kind: **fixed** · role: **furniture** · required: **true** · interactionMode: **passive**
- displayTitle (visible heading): "How you'll work through this course"
- component: `palette/text`
- **fixed shell text** (identical in every course, not authored per course):
  > Start and finish with a confidence check. Before the lessons, you'll rate how confident you feel about each part of this topic. You'll rate the same statements again at the end, so you can see what has changed. Your ratings are yours: they aren't marked and no one else sees them.The activities in the lessons are for practice. Questions, examples and reflective prompts are there to help you think, and they don't count towards passing. Reflective prompts are private and optional.The test at the end is the one that counts. To complete the course you need to take the final test and score at least {{passMark}}. You can retake it.

### 6. `course-conventions` — "How this course works"
- kind: **fixed** · role: **furniture** · required: **true** · interactionMode: **passive**
- displayTitle (visible heading): "How this course works"
- component: `palette/text`
- **fixed shell text** (identical in every course, not authored per course):
  > The examples and activities in this course use invented people, authors and sources to show how things work. Unless we say otherwise, any name, citation or reference you meet in an example is fictional.Where a lesson draws on real work, you'll find it listed under Lesson Sources at the bottom of that page. Every real source used in the course is gathered under Course Sources at the end.

## C-PRE ("Before you start")  <!-- skeletons/c-pre -->
_pageType: `c-pre` · archetype version 0.1.0 · source: docs/authoring/c-pre-template.md (Structure Summary)_

### 1. `confidence-pre` — "Confidence check"
- kind: **fixed** · role: **furniture** · required: **true** · interactionMode: **interactive**
- displayTitle (visible heading): "How confident do you feel?"
- component: `palette/confidence`

## LESSON (repeats, one per lesson)  <!-- skeletons/lesson -->
_pageType: `lesson` · archetype version 0.2.0 · source: docs/authoring/lesson-structure-template.md (Block order)_

### 1. `orientation` — "Orientation"
- kind: **fixed** · role: **orientation** · required: **true**
- displayTitle (visible heading): _(none — no visible heading)_
- component: `palette/text`

### 2. `orientation-tier` — "Orientation: at this level"
- kind: **fixed** · role: **orientation-tier** · required: **true**
- displayTitle (visible heading): _(none — no visible heading)_
- component: `palette/text`

### 3. `learning-outcomes` — "Learning outcomes"
- kind: **fixed** · role: **learning-outcomes** · required: **true**
- displayTitle (visible heading): _(none — no visible heading)_
- component: `palette/text`

### 4. `concept-definition` — "Concept: definition"
- kind: **fixed** · role: **concept** · required: **true**
- displayTitle (visible heading): _(none — no visible heading)_
- component: `palette/text`

### 5. `concept-context` — "Concept: in practice"
- kind: **variable** · role: **concept** · required: **true** · **gate immediately after this block**
- displayTitle (visible heading): _(none — no visible heading)_
- slotType: `concept-context`
- component options: `palette/text`
- content coupling: `whole-prose`
- selection model: single-realisation: palette/text. A coupled follow-on to the generic concept-definition above it; empty in the shell, filled by the context pack as natural prose. No routing decision.
- **standing context prompt (CXP agent, filling this slot for a subject):**
  > What does this look like in practice within the given context? Write a short follow-on from the generic definition above, in the learner's own subject or discipline.

### 6. `concept-intro` — "Explore the concept"
- kind: **variable** · role: **concept** · required: **true**
- displayTitle (visible heading): _(none — no visible heading)_
- slotType: `concept-intro`
- component options: `palette/text`, `palette/accordion`, `palette/flipcard`, `palette/tabs`, `palette/hotgraphic`, `palette/narrative`, `palette/timeline`, `palette/annotated`, `palette/graphic`, `palette/media`, `palette/matching`, `palette/sortable`, `palette/hotspot`, `palette/slider`
- content coupling: `shell-coupled`
- selection model: pattern-derived: identify content shape → match pattern recognition → take realisation. Presentational patterns: explore-model (hotgraphic, narrative, timeline, flipcard, accordion, graphic, media), survey-alternatives (tabs, accordion), recall-reveal (flipcard, accordion), inline-commentary (annotated). Plus palette/text for plain prose. ACTIVITY-MODE question patterns (8 Oct 2026, Abbott): a manipulation question component may be the activity (learn by doing) - sort-into-groups (matching), build-from-parts (sortable), label-a-structure (hotspot), place-on-a-scale (slider); when one fills this slot it runs in activity mode, not as a check (see this archetype's notes). v2 (8 Oct 2026): this is the lesson's interactive concept activity (the "interior / activity"), authored generically; the subject-specific concept prose lives in the concept-context block above it, not here.
- **authoring prompt (direct — shell author / agent writing this slot):**
  > Activity mode — the task itself teaches the concept. For a manipulation question (matching/sortable/hotspot/slider): plausible, unambiguous options/pairs/targets; incorrect feedback (notFinal) explains and points toward the answer; correct feedback restates the concept, not a bare verdict. Balance any selected options per docs/authoring/mcq-authoring-guidance.md.

### 7. `worked-example` — "Worked example"
- kind: **variable** · role: **worked-example** · required: **true**
- displayTitle (visible heading): "Worked example"
- slotType: `worked-example`
- component options: `palette/text`, `palette/accordion`, `palette/narrative`, `palette/hotgraphic`, `palette/timeline`, `palette/flipcard`, `palette/annotated`, `palette/branching`, `palette/graphic`, `palette/media`
- content coupling: `structured-fields`, `token-substitution`
- selection model: pattern-derived: identify content shape → match pattern recognition → take realisation. Patterns: sequential-process (accordion, narrative, media), explore-model (hotgraphic, narrative, timeline, flipcard, accordion, graphic, media), evaluate-versions (annotated, accordion, text), recall-reveal (flipcard, accordion), decision-scenario (branching). Plus palette/text for plain prose. Block count (1–4 blocks depending on content shape) is recorded in instantiation, not governed by this slot; see backlog 5.45 follow-on (a). v2 (8 Oct 2026): contextCoupling is structured-fields + token-substitution (the character cast); the shell authors a generic surface-vs-deep frame and the context pack fills subject fields and the cast names.
- **authoring prompt (direct — shell author / agent writing this slot):**
  > Worked example — third person: a weaker/less-developed version first, then a stronger version reached by better practice; make explicit what the stronger one does differently.
- **standing context prompt (CXP agent, filling this slot for a subject):**
  > Give a subject-specific worked example of this lesson's concept: a weaker or less-developed version first, then a stronger version reached by better practice, using the context cast (character tokens) consistently.

### 8. `practical-guidance` — "Practical guidance"
- kind: **variable** · role: **practical-guidance** · required: **true** · **gate immediately after this block**
- displayTitle (visible heading): "How to do it"
- slotType: `practical-guidance`
- component options: `palette/text`, `palette/accordion`, `palette/tabs`, `palette/branching`, `palette/checklist`, `palette/annotated`, `palette/matching`, `palette/sortable`, `palette/slider`, `palette/hotspot`
- content coupling: `shell-coupled`, `token-substitution`
- selection model: pattern-derived: identify content shape → match pattern recognition → take realisation. Patterns: survey-alternatives (tabs, accordion), decision-scenario (branching), action-checklist (checklist), inline-commentary (annotated), sort-into-groups (matching), build-from-parts (sortable), place-on-a-scale (slider), label-a-structure (hotspot). Plus palette/text for plain prose. Note: decision-scenario names this slotType but records first homes as Presenting, Reflective Practice, Work-Based Learning. Branching included because the archetype serves all thirteen pathways. v2 (8 Oct 2026): contextCoupling is shell-coupled + token-substitution — broadly generic guidance that may name the context via {{context}}.
- **authoring prompt (direct — shell author / agent writing this slot):**
  > Practical, do-this-now guidance the learner can act on this week; why-before-how; concrete steps, not restated theory.

### 9. `check` — "Check your understanding"
- kind: **variable** · role: **knowledge-check** · required: **true**
- displayTitle (visible heading): "Check your understanding"
- slotType: `check`
- component options: `palette/mcq`, `palette/sortable`, `palette/matching`, `palette/gmcq`, `palette/hotspot`, `palette/slider`
- content coupling: `shell-coupled`, `token-substitution`, `structured-fields`, `whole-prose`
- band: 3–3 blocks — Every check carries exactly three questions, one per lesson outcome: item 1 general/shell-coupled (o1), item 2 context-specific body (o2), item 3 token-substitution carrying {{context}} (o3). Three-outcome model, 9 Oct 2026; see docs/authoring/token-substitution-coupling-and-three-outcome-model.md (CK-1).
- selection model: pattern-derived: identify content shape → match pattern recognition → take realisation. Patterns: retrieval-practice (mcq, sortable), match-pairs (matching), spot-the-error (mcq, gmcq, hotspot), sort-into-groups (matching), build-from-parts (sortable), place-on-a-scale (slider), label-a-structure (hotspot).
- **authoring prompt (direct — shell author / agent writing this slot):**
  > Author MCQ options balanced per docs/authoring/mcq-authoring-guidance.md: all options the same length and specificity so the correct answer is never the longest or most qualified; distractors are plausible misconceptions, not filler; keep hedging and absolutes even across options; feedback gives the reason, never a bare verdict.
- **standing context prompt (CXP agent, filling this slot for a subject):**
  > Write the subject's own version of this lesson's check question(s), testing the same outcome in the learner's own discipline.
- authoring venue: Item 1 (position 1, shell-coupled) is authored in the shell. A context-specific body item (whole-prose / structured-fields) is authored in context packs; an uncoupled lesson authors it in the shell instead. A token-substitution item is authored in the shell carrying {{context}}, filled at merge per its tokenMode (generic -> 'your subject'; cxp-fillable -> context.label, floor 'your subject'). Derived from the lesson's coupling, not declared independently.
- position rules:
  - position 1: coupling shell-coupled — General question, the same for every subject (CK-1)
  - position rest: coupling token-substitution, structured-fields, whole-prose — Context-specific (CK-1)
- **agentAuthor**:
  - content: A question testing one lesson outcome, with teaching feedback - never a bare right/wrong.
  - context.all: The CXP subject/pack recasts the stem and options into the learner's own discipline (three-outcome model: item 1 general/shell-coupled, the rest context-specific); keep the correctness pattern and item count, reword for the subject.
  - context.introductory: Test recognition and recall of the basic concept; distractors are common everyday misconceptions.
  - context.intermediate: Test application of the concept to a typical task in the subject; distractors are partial or misapplied versions, not obvious errors.
  - context.advanced: Test evaluation, judgement and transfer; distractors are defensible-but-weaker positions a capable student might pick, not clear mistakes.
  - relation: Tests the concept defined earlier in the page; do not introduce new ideas here.
  - warning: Keep distractors parallel in length and structure to the correct answer. If the key is a longer, two-clause definitional sentence and the distractors are short one-liners, length alone flags the answer - match their shape and rough length so only the content distinguishes the right option.
  - bestPractice: Every distractor defensibly wrong, and the feedback says why (teach, do not bark).
  - agentAuthorWritten.notes: Apply the Voice Spec section 18 register check before treating copy as done.
  - agentAuthorDialogue.notes: Pose the question conversationally; probe the learner's reasoning before revealing the key.

### 10. `reflective-prompt` — "Reflective prompt"
- kind: **variable** · role: **reflective** · required: **true**
- displayTitle (visible heading): "Your thoughts"
- slotType: `reflective-prompt`
- component options: `palette/opentext`
- content coupling: `shell-coupled`
- selection model: pattern-derived: served by activity-patterns/write-own-thinking, realised as palette/opentext (replacing the legacy palette/textinput).
- **authoring prompt (direct — shell author / agent writing this slot):**
  > 1-3 genuine open questions with no right answers; private, unmarked tone; invite the learner's own view, never quiz.

### 11. `summary` — "Summary"
- kind: **variable** · role: **summary** · required: **true**
- displayTitle (visible heading): "Summary"
- slotType: `summary`
- component options: `palette/text`
- content coupling: `structured-fields`
- selection model: single-realisation: palette/text. A generic recap frame authored in the shell; the context pack fills it with what the learner can now do in their own subject. No routing decision.
- **authoring prompt (direct — shell author / agent writing this slot):**
  > Recap what the learner can now do, outcome by outcome, and why it matters next; affirm progress; introduce no new content.
- **standing context prompt (CXP agent, filling this slot for a subject):**
  > Recap what the learner can now do, in terms of their own subject or context.

### 12. `lesson-references` — "Lesson Sources"
- kind: **variable** · role: **references** · required: **true**
- displayTitle (visible heading): "Lesson Sources"
- slotType: `lesson-references`
- component options: `palette/references`
- content coupling: `shell-coupled`
- selection model: single-realisation: only palette/references fills this slot. No routing decision; no activity-pattern names this slotType.
- **authoring prompt (direct — shell author / agent writing this slot):**
  > Footnote-style pointer(s) only — 'See pages x-y of Chapter n of Title by Authors'; chapter + page range; real sources only (LSP-1).

## SUMM  <!-- skeletons/summative -->
_pageType: `summative` · archetype version 0.1.0 · source: docs/project/project-backlog.md (2026-08-14 resultsdebrief/pass-reveal verification)_

### 1. `introduction` — "Assessment introduction"
- kind: **fixed** · role: **furniture** · required: **true** · interactionMode: **passive**
- displayTitle (visible heading): _(none — no visible heading)_
- component: `palette/text`
- **fixed shell text** (identical in every course, not authored per course):
  > This is the test for the whole course. It covers everything you've studied in the lessons, with a set of questions to work through.To pass, you need to score at least {{passMark}}. You can retake the test if you don't pass first time.

### 2. `assessment-items` — "Assessment items"
- kind: **variable** · role: **summative** · required: **true**
- displayTitle (visible heading): _(none — no visible heading)_
- slotType: `summative-item`
- component options: `palette/mcq`, `palette/sortable`
- content coupling: `shell-coupled`
- selection model: pattern-derived: identify content shape → match pattern recognition → take realisation. Pattern: summative-mixed (mcq, sortable).
- **authoring prompt (direct — shell author / agent writing this slot):**
  > Author MCQ options balanced per docs/authoring/mcq-authoring-guidance.md: all options the same length and specificity so the correct answer is never the longest or most qualified; distractors are plausible misconceptions, not filler; keep hedging and absolutes even across options; feedback gives the reason, never a bare verdict.
- **agentAuthor**:
  - content: Summative questions testing the course outcomes, two per outcome (AL-3), each with teaching feedback - never a bare right/wrong.
  - context.all: Summative items are NOT tailored to a subject context (SQ-1): keep them general, using 'your subject' in generic phrasing where suitable; do not recast per CXP pack.
  - context.introductory: Recognition and recall of the course's core concepts.
  - context.intermediate: Application of the concepts across the course's typical tasks.
  - context.advanced: Evaluation, judgement and transfer across the course's material.
  - relation: Tests the course outcomes set at crs-03 (each item names via `tests` the one outcome it tests); covers what the lessons taught - introduce no new material.
  - warning: Keep distractors parallel in length and structure to the correct answer; length or specificity must not flag the key (mcq-authoring-guidance.md).
  - warning: Do not tailor items to a subject context (SQ-1) - summative coupling is none.
  - bestPractice: Every distractor defensibly wrong, and the feedback says why (teach, do not bark).
  - bestPractice: Spread the two items per outcome across different facets of that outcome.
  - agentAuthorWritten.notes: Apply the Voice Spec section 18 register check before treating copy as done.
  - agentAuthorDialogue.notes: Pose each question conversationally; probe the learner's reasoning before revealing the key.

### 3. `results` — "Results"
- kind: **fixed** · role: **furniture** · required: **true** · interactionMode: **passive**
- displayTitle (visible heading): _(none — no visible heading)_
- component: `palette/assessmentresults` + extensions: `palette/resultsdebrief`, `palette/passreveal`

## C-POST ("Looking back")  <!-- skeletons/c-post -->
_pageType: `c-post` · archetype version 0.1.0 · source: docs/authoring/c-post-template.md (Structure Summary)_

### 1. `confidence-post` — "Confidence check"
- kind: **fixed** · role: **furniture** · required: **true** · interactionMode: **interactive**
- displayTitle (visible heading): "How confident do you feel now?"
- component: `palette/confidence`

### 2. `reflective-bridge` — "Your reflection"
- kind: **variable** · role: **reflective** · required: **false**
- displayTitle (visible heading): _(none — no visible heading)_
- slotType: `reflective-bridge`
- component options: `palette/opentext`
- content coupling: `shell-coupled`
- selection model: furniture: optional bridge after C-POST, off by default per CC-1c. Deliberately excluded from activity-pattern layer (furniture class). Realised as palette/opentext, matching reflective-prompt's realisation elsewhere in this store.
- authoring advice: _(none recorded for this slot — furniture, or a routing-only slot)_

## W-CLOSE  <!-- skeletons/wrapper-close -->
_pageType: `wrapper-close` · archetype version 0.1.0 · source: docs/authoring/wrapper-close-template.md (Structure Summary)_

### 1. `summary` — "Course summary"
- kind: **fixed** · role: **summary** · required: **true**
- displayTitle (visible heading): "Summary"
- component: `palette/text`

### 2. `practice-connection` — "In real academic practice"
- kind: **variable** · role: **practical-guidance** · required: **true**
- displayTitle (visible heading): "In real academic practice"
- slotType: `practice-connection`
- component options: `palette/text`
- content coupling: `whole-prose`
- selection model: single-realisation: only palette/text fills this slot. No routing decision; no activity-pattern names this slotType.
- **standing context prompt (CXP agent, filling this slot for a subject):**
  > Recast the generic 'In real academic practice' section in the learner's own subject: show how this topic applies in their actual academic work, with the academic framing first and any professional connection kept brief, as a natural follow-on from the generic version above.
- **agentAuthor**:
  - content: Show the learner how this practice applies in real academic work: concrete ways to use it in their current study, academic framing first and any professional connection kept brief.
  - context: The CXP subject/pack recasts this into the learner's own discipline (the slot.standingContextPrompt axis): name the subject's real tasks and evidence, not a generic 'academic work'.
  - relation: Practical-guidance role; follows the course summary. Apply the practice the course taught - do not introduce new ideas, and do not restate the summary.
  - warning: Keep it actionable, not a recap of the summary.
  - warning: Scale the sideways (pathway) reach to the tier (see byTier); do not over-reach at introductory.
  - bestPractice: Give first concrete actions the learner can take now.
  - bestPractice: Draw pathway links from the relationship table, not invented ones.
  - byTier.introductory: displayTitle: "In real academic practice"
    > How to start applying this practice in the learner's current study; first concrete actions. Light sideways reach.
    - sideways: "Name at most one strongly-related pathway, as 'you will also use this when you...'."
  - byTier.intermediate: displayTitle: "In real academic practice"
    > Applying the practice across modules and tasks; begins to connect it to neighbouring practices.
    - sideways: "Draw the two or three strongest pathway links from the relationship table and show the transfer."
  - byTier.advanced: displayTitle: "Into your own practice"
    > Self-directed extension, cross-pathway transfer and contribution, not how to apply the basics. Carries the outward move that where-next no longer does at this tier.
    - sideways: "Full sideways map: how this practice integrates with the others in independent work."
  - agentAuthorWritten.notes: Apply the Voice Spec section 18 register check before treating copy as done; British English, address the learner as 'you', and give the reason behind each action.
  - agentAuthorDialogue.notes: Ask where the learner could apply this next, then tailor the example to their answer rather than listing uses.

### 3. `where-next` — "Where this goes next"
- kind: **fixed** · role: **furniture** · required: **false** · interactionMode: **passive**
- displayTitle (visible heading): "Where this goes next"
- component: `palette/text`
- **agentAuthor**:
  - content: Point the learner to where this course leads next in the programme: outline the topics the neighbouring courses cover so they can see the shape of the series.
  - context: Resolve against the courses that actually exist in the programme at build time; an unbuilt course resolves to a safe placeholder, never a dead link.
  - relation: Terminal block of the close wrapper; follows practice-connection. Look outward to the series - do not restate this course's own content.
  - warning: Do not hard-code course names or links that may not exist yet; reference siblings through series link tokens.
  - warning: Keep it tier-appropriate (see byTier): introductory points forward only; intermediate points forward and back; advanced omits the block.
  - bestPractice: Give a short outline of each linked course's topics, not just a title, so the learner can judge where to go.
  - byTier.introductory: displayTitle: "Where this goes next"
    > Forward only: name the next tier of this pathway as the deliberate next step and outline what it adds. No look-back (nothing sits below introductory). Encouraging and concrete.
    - forwardBack: "Point up to the next tier only; there is nothing below to look back to."
  - byTier.intermediate: displayTitle: "Building on this"
    > Forward and back: briefly connect to the introductory groundwork this tier assumes, then point up to the advanced tier and what it extends into.
    - forwardBack: "Up to the advanced tier and back to the introductory groundwork it builds on."
  - byTier.advanced: applies: false — Terminal tier: there is no next tier up, so omit this block. The outward move collapses into practice-connection (sideways). This is why where-next is required:false in the skeleton.
  - agentAuthorWritten.notes: Resolve series link tokens to the courses that exist at build time; outline their topics in prose.
  - agentAuthorDialogue.notes: Offer next steps as a short menu and ask which direction interests the learner, rather than listing every course.

### 4. `course-references` — "Course Sources"
- kind: **variable** · role: **references** · required: **true**
- displayTitle (visible heading): "Course Sources"
- slotType: `course-references`
- component options: `palette/references`
- content coupling: `shell-coupled`
- selection model: single-realisation: only palette/references fills this slot. No routing decision; no activity-pattern names this slotType.
- **authoring prompt (direct — shell author / agent writing this slot):**
  > Aggregate the real sources cited across the lessons, same pointer form; every lesson source present and nothing here uncited (consistency rule).
