# Browser Test Checklist: Academic Writing: Introductory Stage

**Server:** `http://localhost:9000/` (currently running via plain `grunt
server`). Note: full SCORM completion/suspend-resume behaviour needs
`grunt server-scorm` specifically, flagged separately below where it
matters, don't assume the plain server covers it.

**Before starting:** confirm `src/course` actually points to
`courses/academic-writing-introductory/` (today's migration renamed the
folder; `ls -la src/course` should show the new path) before running
`grunt server`, given how many mix-ups this exact kind of symlink
caused earlier today.

**Before starting:** open the browser console and leave it open
throughout. Every page/action below should be checked against "any new
console errors?" as a standing background check, not just the specific
items listed.

---

## 0. Menu / navigation

- [ ] Exactly 11 pages appear, in this order, with no demo/test pages
      visible: **Academic Writing: Introductory Stage** (W-OPEN) ->
      **Before you start** (C-PRE) -> **Understanding the task** (L02) ->
      **Planning** (L03) -> **Drafting** (L04) -> **Editing** (L05) ->
      **Proofreading** (L06) -> **Common errors** (L07) ->
      **Bringing it together** (SUMM) -> **How far you've come** (C-POST) ->
      **Wrap-up** (W-CLOSE)
- [ ] No console errors on initial load

*Note: Page count and structure updated 13 August 2026 per CC-1 (C-PRE/C-POST pages added). The automated `test-browser-checklist.mjs` was updated in commit ceb7967.*

---

## 1. Wrapper Open ("Academic Writing: Introductory Stage")

- [ ] **Learning outcomes render FIRST** (14 Aug reorder, supersedes WR-1b):
  - [ ] Heading "Learning outcomes" is the first visible content block
  - [ ] Intro line reads "By the end of this **course**" (not "topic")
  - [ ] 3 bullet items render
- [ ] Overview & justification text renders cleanly (no raw HTML tags
      visible, no broken entities) — now second block
- [ ] Signpost text renders (before and after the diagram) — now third block
- [ ] **Hotgraphic diagram**: all 5 pins visible and clickable
  - [ ] Pin 1: "Understand the task": popup text correct
  - [ ] Pin 2: "Plan": popup text correct
  - [ ] Pin 3: "Draft": popup text correct
  - [ ] Pin 4: "Edit": popup text correct
  - [ ] Pin 5: "Proofread": popup text correct
  - [ ] All 5 pins visited registers completion (`_setCompletionOn:
        allItems`)
- [ ] **No confidence component on this page** (moved to C-PRE per CC-1)

---

## 1.5. Before you start (C-PRE): confidence pre-check

- [ ] **Confidence PRE**:
  - [ ] Component renders with **no console error**
  - [ ] All 9 statements appear
  - [ ] Each statement has a 5-point radio-group scale, all 5 options
        visible and labelled (not just numbers)
  - [ ] Try keyboard navigation on one radio group (Tab between items,
        arrow keys within one item's options)
  - [ ] Submit button is disabled until all 9 are rated, then enables
  - [ ] After submit: confirmation text appears ("Thank you. You'll rate
        these again at the end of the course...")

---

## 2. Understanding the task (L02): pre-existing pilot content

- [ ] Loads without errors (sanity check only; this predates today's
      work, shouldn't have changed, but worth confirming nothing broke)

---

## 3-7. Planning, Drafting, Editing, Proofreading, Common errors

For **each** of the five lessons:

- [ ] All text sections render cleanly, no raw HTML/markdown showing
- [ ] Worked example renders in the blockquote style (visually
      distinguished from regular text)
- [ ] **Check Your Understanding** component:
  - [ ] Renders correctly (mcq for Planning/Drafting/Editing/
        Proofreading; sortable for Common errors)
  - [ ] Selecting an answer and submitting **does show feedback** (these
        are formative, feedback should NOT be suppressed here, unlike
        SUMM)
  - [ ] Feedback text matches what was authored (spot-check one or two)
- [ ] **Common errors specifically**: sortable component:
  - [ ] Drag-and-drop reordering works
  - [ ] Keyboard reordering works (Enter to grab, arrow keys to move,
        Enter to drop)
- [ ] Reflective prompt (textinput):
  - [ ] Optional: doesn't block page completion if left blank
  - [ ] No marking/feedback UI shown (this is correct; it's unscored)
- [ ] **No confidence component appears on any of these five pages**
      (correctly absent; confidence lives only at wrapper level now)

---

## 8. Bringing it together (SUMM): the assessment

- [ ] Orientation text renders
- [ ] **Trickle gating**: items appear one at a time behind a
      "Continue" button, not all 8 at once
- [ ] All 8 items appear in order:
  - [ ] Item 1 (mcq, steer identification)
  - [ ] Item 2 (mcq, hidden steer)
  - [ ] Item 3 (sortable, writing-cycle sequence, reused from the old
        L01)
  - [ ] Item 4 (sortable, planning steps)
  - [ ] Item 5 (mcq, comma splice)
  - [ ] Item 6 (mcq, apostrophe misuse)
  - [ ] Item 7 (mcq, semicolon/colon confusion)
  - [ ] Item 8 (mcq, overlong sentences: check both Version A and
        Version B display correctly)
- [ ] **Critical: no per-item feedback appears** after answering each
      question (feedback is deliberately suppressed during the
      assessment; this is intentional, not a bug, but worth confirming
      it's actually suppressed and not accidentally showing)
- [ ] After all 8 items: a "Show results" gate appears (inverted-colour
      block), separate from the results themselves
- [ ] Clicking "Show results" reveals the assessmentResults component
- [ ] Score and pass/fail band feedback display correctly
- [ ] **Test the pass mark**: if feasible, try once to fail (score below
      70%) and once to pass (70%+), since attempts are unlimited,
      confirm the right band feedback shows for each
- [ ] Retry button reads "Try again" (not the default "Retry Assessment")

---

## 9. How far you've come (C-POST): confidence post-check

- [ ] **Confidence POST**:
  - [ ] Renders with no console error
  - [ ] Same 9 statements as PRE
  - [ ] Rate them (try varying the ratings vs. what you gave at PRE, to
        actually exercise the rose/dropped/stayedHigh/stayedLow/
        noMovement patterns, not just resubmit identical values)
  - [ ] Submit, and confirm per-item feedback appears, distinct per
        pattern (not the same generic text for everything)
  - [ ] Confirm a summary line appears too (predominantlyUp / mixed /
        flatOrLow, depending on the overall pattern of your answers)

---

## 10. Wrap-up (W-CLOSE)

- [ ] **Four blocks render in order** (per WC-1, CC-1e verification):
  - [ ] Block 1 (c-10): Course summary renders (text now reads
        "introductory stage" per terminology sweep)
  - [ ] Block 2 (c-20): Practice connection — "Everything this course
        has covered..."
  - [ ] Block 3 (c-25): Where this goes next — "The intermediate stage
        builds..."
  - [ ] Block 4 (c-15): References component
- [ ] **No confidence component on this page** (moved to C-POST per CC-1)
- [ ] **References component**:
  - [ ] The one entry ("Excelling at University, Chapter 8: Writing
        critically, 'The language of criticality'") displays as a link
  - [ ] Clicking it doesn't error (href="#" is a placeholder, so it
        won't navigate anywhere meaningful, that's expected, just
        confirm no JS error)
  - [ ] No permalink shown (none was provided; confirm it degrades
        cleanly, not showing an empty/broken permalink link)

---

## 11. Cross-cutting

- [ ] No console errors anywhere across all 11 pages, start to finish
- [ ] No broken images (hotgraphic diagram, page thumbnails)
- [ ] Resize the browser to a mobile width at least once; check the
      hotgraphic's narrative-on-mobile fallback (`_isNarrativeOnMobile:
      true`) actually kicks in
- [ ] **Not tested here, needs `grunt server-scorm` specifically**:
      SCORM completion status, suspend/resume behaviour (does revisiting
      W-CLOSE after closing the browser correctly restore the PRE
      ratings for POST to compare against?). Flag as separate follow-up
      testing, not covered by the plain server.

---

## What to report back

For anything that doesn't check out: the exact page, what you expected
vs. what happened, and the console error text if there is one. I'll
recon the actual cause before proposing any fix, same as every other
issue today.
