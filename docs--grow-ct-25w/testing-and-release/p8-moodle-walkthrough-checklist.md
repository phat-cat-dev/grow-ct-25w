# P8 Moodle Walkthrough Checklist

> **Status:** completed test record, 28-29 July 2026, Academic Writing Introductory only (then slugged WR-I). Retained for its findings. The live procedure for the September 2026 pass is `docs/project/moodle-verification-2026-09.md`.

**Package being tested:** Academic Writing: Introductory Stage (WR-I)
**Moodle course:** Development/test instance
**Date:** 28-29 July 2026
**Tester:** Human tester + Claude Code (automated scans)
**Browser/device tested:** Desktop (Chromium via Playwright), manual browser testing

---

## Part A — Technical / Moodle-specific

### Upload & Launch

- [x] SCORM package uploads without error
  Notes: Confirmed working.

- [x] Activity appears in course with correct title
  Notes: Confirmed working.

- [x] Course launches from Moodle's activity page (no blank screen, no JS errors)
  Notes: Confirmed working.

- [x] Content renders correctly inside Moodle's SCORM player iframe
  Notes: Confirmed working.

### Gradebook & Completion (Pass Run)

- [x] Complete assessment with score ≥70% (pass)
  Actual score achieved: 75%
  Notes: Correctly recorded and reported.

- [x] Gradebook shows the correct score
  Notes: Interactions report confirms full per-question response-level tracking works (confidence PRE/POST, L03-L07 checks, SUMM items, reflective textInputs all captured with real values).

- [x] Activity marked as "Complete" in Moodle (check activity completion, course completion if configured)
  Notes: Working after root-cause fix (see W-CLOSE completion notes below).

### Gradebook & Completion (Fail Run)

- [x] Complete assessment with score <70% (fail)
  Actual score achieved: 25%
  Notes: Correctly recorded with correct timestamps.

- [x] Gradebook shows the correct score
  Notes: Confirmed working.

- [x] Activity marked as "Incomplete" (not "Complete") in Moodle
  Notes: Confirmed working.

### Suspend/Resume

- [x] Exit course partway through (after confidence PRE, before assessment)
  Notes: Confirmed working.

- [x] Return to course later — does it restore position correctly?
  Notes: Confirmed working for general case.

- [x] Confidence PRE ratings preserved for POST comparison after resume?
  Notes: Confirmed working.

- [ ] After a fail attempt: exit, return, retry — does retry work correctly from resumed state?
  Notes: **CRITICAL BUG, OPEN.** Fail → reach results (fail message + "Try again" shown) → exit → return: assessment silently resets to a blank attempt, no fail state, no "Try again" button, as if the attempt never happened. Likely cause: `SUMM-a-01`'s `_isResetOnRevisit: true` firing on resumed revisit and colliding with SCORM resume state. Needs investigation: (1) does the gradebook score survive despite the UI reset (untested); (2) intended behaviour — should reset-on-revisit exclude resumed sessions; (3) check Adapt's own `_isResetOnRevisit` documentation/behaviour.

### Additional Technical Findings

**Reflective Prompt Storage:**
- [x] Reflective textInput responses stored correctly in SCORM interactions report
  Notes: Formally tested 29 July. Distinctive marked test strings entered in two separate lessons both appeared correctly in the interactions report. Storage fully verified, not incidental.

**Reflective Prompt Display/Masking:**
- [ ] Reflective textInput content displays readably after submission
  Notes: **BUG, OPEN.** Confirmed consistent across multiple lessons (not one-off). Content displays starred-out/masked and locked (uneditable) after submission. Fix direction: at minimum display readably; ideally stay editable/appendable.

**Possible ID Collision:**
- [ ] All component IDs unique in interactions report
  Notes: **NEEDS INVESTIGATION.** L06-c-45, L02-c-30, L03-c-45 each appear twice in the interactions report with different response values. Unclear if legitimate (resubmit logged separately) or a genuine tracking-ID collision. Needs a check against the course JSON for each ID's uniqueness.

**W-CLOSE Completion:**
- [x] W-CLOSE page completion triggers course completion
  Notes: **RESOLVED, root cause confirmed and fixed 28 July.** Root cause: Moodle course-level "Completion tracking" was set to No — confirmed by total absence of an "Activity completion" section on the activity's own settings page. Not a package/code bug. Fix: course-level tracking enabled, activity's completion condition set to "Completed" only (deliberately not "Passed" or "Receive a grade" — reasoning: package never sends "passed" status, and score submits on every attempt including fails). Retested and confirmed working end-to-end, pass and fail branches both correct.

---

## Part B — Human Eyeballing (things Playwright approximated)

*Note: Part B functional-adjacent items (hotgraphic popup close, trickle reliability, clipped/overlapping elements) were verified 29 July. Remaining Part B items (blockquote styling, confidence feedback readability, font rendering, general width/scrollbar impressions) are purely presentational and are deliberately deferred to the Cardiff Met theme pass — not outstanding walkthrough gaps.*

### Visual Distinction

- [ ] Blockquote/worked-example styling: visually distinct from body text?
  Notes: Not formally checked.

- [ ] Confidence PRE/POST feedback: readable, clear which pattern applies to each item?
  Notes: Not formally checked.

### Interaction Feel

- [x] Hotgraphic pins: feel responsive, popup appears smoothly, close works?
  Notes: Confirmed working 29 July. Popup close functions correctly. **Incidental finding (separate issue):** Hotgraphic container div (W-OPEN) not centred — CSS fix needed, check if the same pattern recurs elsewhere hotgraphic is used.

- [x] Trickle "Continue" buttons: responsive, no lag or double-tap needed?
  Notes: Confirmed working 29 July (SUMM). Single-click activates, no lag, correctly gated on answer submission.

### Moodle-specific Layout

- [ ] Any cramped width issues inside SCORM player iframe?
  Notes: **Incidental finding: Confidence component 5-option rating row overflows** instead of staying in one row at desktop/tablet widths; should only stack at genuine mobile breakpoints. Markup confirmed correct (`confidence__scale`, `role="radiogroup"`, `confidence__option` × 5) — this is a CSS/flex-wrap issue in the component's `.less`, not markup.

- [ ] Any unexpected scrollbars (horizontal or nested vertical)?
  Notes: Not formally checked.

- [ ] Font rendering acceptable? (no fallback fonts, no odd sizing)
  Notes: Not formally checked.

- [x] Any components clipped or overlapping at Moodle's default iframe width?
  Notes: Confirmed 29 July — none found. All components render within bounds.

### Additional Visual Findings (Incidental)

**Sortable Component Contrast:**
- [ ] Sortable text/background colour contrast acceptable
  Notes: **Colour contrast clash identified.** State/location not yet pinned down — needs follow-up to specify which state: default/dragged/selected/submitted. Independently confirmed by axe-core scan (WCAG 1.4.3 violation, SERIOUS severity).

**References Component Links:**
- [x] External links open in new tab
  Notes: **Confirmed working 29 July.** Template already has `target="_blank"` and `rel="noopener"` on both link types — no fix needed. Original report was incorrect.

---

## Part C — Accessibility Spot-check

*This is a sanity pass, not a full audit. Note anything broken plainly. Full screen-reader/keyboard audit tracked separately as Strategic item #1.*

### Confidence Component (Keyboard-only)

*Completed 29 July.*

- [x] Tab through confidence rating items using only keyboard (no mouse)
  Notes: Confirmed working. Tab/arrow-key navigation between rating items and options works correctly.

- [x] Focus order makes sense? (moves through items in logical sequence)
  Notes: Confirmed working.

- [x] Can select a rating option using keyboard? (arrow keys within a group, or spacebar/enter)
  Notes: **Space bar: confirmed working**, visual state updates correctly and immediately. **Enter does not select** an option — this is correct standard radio-group behaviour, not a bug. An initial report of "delayed visual feedback" and "difficulty selecting the first option" was traced to using Enter instead of Space (user-key confusion). Recommend one final clean re-test using Space consistently across all 9 items before fully closing this out.

- [x] Can submit using keyboard? (tab to submit button, enter to activate)
  Notes: Confirmed working once all 9 items have a selection.

### Sortable Component (Keyboard-only)

*Completed 29 July.*

- [x] Find the sortable component on Common errors (L07) or SUMM
  Notes: Sortable component located and tested.

- [x] Enter to grab an item — does it enter "grabbed" mode with visual feedback?
  Notes: Confirmed working. Enter key grabs item, visual feedback shows grabbed state.

- [x] Arrow keys to move the item up/down in the list?
  Notes: Confirmed working. Arrow keys move grabbed item through the list.

- [x] Enter again to drop the item in new position?
  Notes: Confirmed working. Enter key releases/drops the item in its new position.

- [x] Can submit the sortable using keyboard?
  Notes: Confirmed working. Tab to submit button, Enter to activate — all keyboard-accessible.

### General Keyboard Navigation

*Completed 29 July.*

- [x] Can navigate entire course using Tab/Shift+Tab without getting stuck?
  Notes: Confirmed working. Automated Tab-sequence scan (`test-focus-sequence-scan.mjs`) verified full forward/backward traversal across all pages.

- [x] Any focus traps (places where tab stops working or loops unexpectedly)?
  Notes: **None found.** Automated scan (52 pages) found no focus traps. One forward/reverse asymmetry flagged in the confidence component — investigated and confirmed as a false positive (scan-script artefact from dynamic re-rendering after rating selection, not a real accessibility issue). Confidence backward navigation (Tab/Shift+Tab through rated items to review/correct) works correctly. References links (W-CLOSE) keyboard-reachable via Tab + Enter.

### Automated Accessibility Scan (axe-core)

*Added 29 July. See `test-accessibility-scan.mjs` for the full script.*

**Findings:**

1. **Sortable colour-contrast** (WCAG 2.1 AA, 1.4.3) — SERIOUS
   Independently confirms the manually-identified contrast issue. Affects L07 and SUMM sortable components (14 elements total).

2. **aria-input-field-name** (WCAG 2.1 A, 4.1.2) — SERIOUS
   Sortable `<ol role="listbox">` elements lack accessible names. Custom component (`adapt-abbott-sortable`). 3 elements affected.

3. **nested-interactive** (WCAG 2.1 A, 4.1.2) — SERIOUS
   Sortable `<li role="option">` items contain nested interactive elements. Custom component (`adapt-abbott-sortable`). 5 elements affected.

**Clean pages (zero violations):**
- W-OPEN (all states including confidence interaction)
- L02-L06
- SUMM (initial state)
- W-CLOSE (all states including confidence interaction)

**Note:** axe-core cannot detect layout/CSS issues (overflow, masking) — these require human eyeballing, which the manual pass identified.

**Fix:** The sortable component is `adapt-abbott-sortable` (custom project code) — edit directly in `src/components/adapt-abbott-sortable/`.

---

## Summary

**Overall result:** WALKTHROUGH COMPLETE — ISSUES TO FIX

**Status:** Parts A, B (functional-adjacent), and C are fully complete as of 29 July 2026. Remaining Part B items (presentational styling) deliberately deferred to Cardiff Met theme pass.

**Critical issues (must fix before launch):**

1. **Suspend/Resume after fail:** Assessment silently resets on resumed revisit after a fail attempt. Blocks retry-from-resumed-state functionality. Root cause likely `_isResetOnRevisit` collision with SCORM resume. See `open-decisions.md` #33 / SRF-1.

2. **Reflective textInput masking:** Content displays starred-out and locked after submission. Affects all reflective prompts across all lessons.

**Minor issues (can fix later):**

1. Sortable colour-contrast (confirmed by both manual and automated testing)
2. Confidence rating row overflow at desktop/tablet widths (CSS flex-wrap issue)
3. ~~Hotgraphic container not centred (W-OPEN)~~ — **FIXED 29 July:** changed `_layout` from "right" to "full"
4. ~~References links open in iframe instead of new tab (W-CLOSE)~~ — **Non-issue:** template already correct
5. ~~Possible ID collision in interactions report~~ — **Non-issue:** expected two-attempt logging behaviour

**Accessibility verification completed:**

- Confidence component keyboard-only: PASSED (Space to select, not Enter)
- Sortable component keyboard-only: PASSED (Enter to grab, arrows to move, Enter to drop, Tab+Enter to submit)
- General keyboard navigation: PASSED (no focus traps; forward/reverse asymmetry flag was false positive)
- axe-core identified 2 issues in `adapt-abbott-sortable` (aria-input-field-name, nested-interactive) — custom component, fix directly
- Confidence component and all other custom code: zero axe-core violations

---

## Related Checklists

**Targeted re-verification:** When a batch of fixes is applied and packages regenerated, use `docs/testing/phase-0-1-reverification-checklist.md` for targeted re-checks of only the things that changed — distinct from repeating this full walkthrough. Created 29 July 2026 for the Phase 0/1 fix batch.
