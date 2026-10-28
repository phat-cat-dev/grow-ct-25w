# Phase 0/1 Fix Re-Verification Checklist

**Purpose:** Confirm the four hash-tagged SCORM packages (built from commit `cba0a2e`, 29 July 2026) correctly reflect every fix from Phase 0 and Phase 1, when re-uploaded to Moodle. This is a **targeted** re-check — only the things that actually changed — not a repeat of the full P8 walkthrough (which remains valid for everything not touched since).

**Packages tested:**
- `academic-writing-introductory-baseline_cba0a2e_2026-07-29.zip`
- `academic-writing-introductory-criminology_cba0a2e_2026-07-29.zip`
- `academic-writing-introductory-psychology_cba0a2e_2026-07-29.zip`
- `academic-writing-introductory-sports-journalism_cba0a2e_2026-07-29.zip`

*Note: These packages use the pre-30 July naming format. Packages built from 30 July 2026 onward use the new format: `{tier}_{context}_{YYYYMMDD}_{HHMMSS}_{commitHash}.zip` (see `courses/README.md`).*

**Verification date:** 30 July 2026

---

## Setup

- [x] Upload `academic-writing-introductory-baseline_cba0a2e_2026-07-29.zip` as a new SCORM activity (or replace the existing one — your call, but if replacing, note that existing attempt history may be affected).
- [x] Confirm upload succeeds without error, activity launches, no blank screen/JS errors.

**Result:** Confirmed — upload/launch clean, console reviewed (only Moodle-generic noise, nothing from adapt/spoor/custom components).

---

## Check 1 — SRF-1: Fail → Resume → Retry (highest priority)

This is the most important check — the fix changed `_isResetOnRevisit` from `true` to `false`, so behaviour should now differ from the original P8 walkthrough finding.

- [x] Go into SUMM, answer to get a **fail** score (<70%).
- [x] Confirm you reach the results page showing the fail message and a **"Try again"** button.
- [x] **Exit the course** (close tab/navigate away) without clicking "Try again."
- [x] **Return to the course** (resume).
- [x] **Expected (this is the fix):** the fail message and "Try again" button are **still shown** — not silently reset to a blank attempt as before.
- [x] Click "Try again" — confirm a fresh attempt starts (trickle resets, no carried-over answers).
- [x] Complete this retry attempt with a **pass** score (≥70%).
- [x] Confirm the pass message displays correctly, and confirm the activity/course marks as **complete** in Moodle (per the completion-tracking setup from the original P8 walkthrough).

**Result:** **FULLY CONFIRMED WORKING** end-to-end — fail state persists across resume, Try Again resets correctly, retry-to-pass completes and marks activity complete in Moodle.

---

## Check 2 — Reflective content no longer masked

- [x] Enter a reflective prompt in any lesson (something identifiable, e.g. "RETEST-[today's date]").
- [x] Submit / move on.
- [x] Re-enter that same lesson/block.
- [x] **Expected (this is the fix):** your text displays **readably**, not starred-out/masked.
- [x] Note whether the field is still locked/read-only (expected — the fix was "display readably," not "make always-editable," per the documented scope) or if it happens to be editable too (bonus, not required).

**Result:** **PARTIALLY FIXED.**

- **Scenario A (in-session navigation):** Leave lesson, return within same SCORM session — **CONFIRMED FIXED**, text displays readably.
- **Scenario B (genuine SCORM suspend/resume):** Close package entirely, reopen — **NOT FIXED**. Text is not restored/displayed at all on reload (not masked, just absent), even though the underlying data is confirmed safe in Moodle's interactions report.

This is a **distinct bug** from what Phase 1 patched — the original fix addressed display/masking logic for same-session state, but never touched the restore-from-SCORM-resume code path (reading cmi.suspend_data back into the field on initialisation). **See open-decisions.md #35 (RTR-1).**

---

## Check 3 — Sortable component visuals

- [x] Go to L07 (Common errors) or SUMM's sortable items.
- [x] Visually check: does the text on sortable items read clearly against its background in all states — default, and if you grab/drag an item, the grabbed/dragging state too?
- [x] No specific contrast issue should be visible now (this was a WCAG 1.4.3 fix).

**Result:** **CONFIRMED FIXED.**

---

## Check 4 — Sortable keyboard accessibility (ARIA changes)

The ARIA roles changed (`role="listbox"`/`"option"` → `role="group"` with explicit `aria-label`s) to fix `nested-interactive` and `aria-input-field-name` violations. This shouldn't change how it *feels* to use, but worth confirming:

- [x] Tab to a sortable component, use Enter/arrows/Enter to reorder an item (same as the original P8 keyboard test) — confirm it still works exactly as before. This was an ARIA/semantic fix, not a behavioural one, so nothing should feel different — just confirming no regression.

**Result:** **CONFIRMED**, no regression.

---

## Check 5 — Confidence component row layout

- [x] View a confidence check (W-OPEN PRE or W-CLOSE POST) at a normal desktop/laptop browser width.
- [x] Confirm the 5-option rating row stays in **one row**, not wrapping/overflowing.
- [x] If you can resize the browser window narrower (or check on a phone/tablet), confirm it switches to a stacked layout at a genuinely small width, not before.

**Result (initial 30 July test):** **NOT FIXED.** 4 options fit on first row, 5th wrapped.

**Fix applied:** CRO-1 fix committed (4658a41, 30 July 2026). After iterative design review (520px → 640px → three-tier), implemented three-tier responsive layout with breakpoints at 720px and 560px.

**Re-verification (30 July 2026): VERIFIED FIXED — three-tier layout.**
- **Method:** Compiled CSS confirmed (720px + 560px breakpoints); live rendering verified via Playwright against local SCORM harness (`grunt server-scorm`).
- **Three-tier scheme:**
  - WIDE (above 720px): Radio inline beside label, 5 tiles on one row
  - MIDDLE (720px–561px): Radio above label (centred), 5 tiles still on one row
  - STACKED (560px and below): Tiles stack in column, radio inline beside label
- **Viewports tested (12 total):**
  - WIDE: 1280px, 1024px, 768px, 740px
  - MIDDLE: 720px, 700px, 640px, 600px, 580px
  - STACKED: 560px, 540px, 375px
- **Screenshots:** `docs/testing/cro1-verification-screenshots/`

Moodle-side visual confirmation will occur incidentally at the next package upload (RTR-1 testing). See open-decisions.md CRO-1 for full resolution details.

---

## Check 6 — L02 lesson order

- [x] Go through L02 (Understanding the task).
- [x] Confirm the order is now **Practical guidance → Check your understanding** (matching L03–L06), not the reverse.

**Result:** **Tentatively confirmed** via visual inspection only (not block-name-verified) — judged low-priority given the upcoming V2 rewrite of this lesson.

---

## Sanity checks — other three packages (criminology, psychology, sports-journalism)

For each of the remaining three:

- [x] Upload succeeds, activity launches without error.
- [x] Spot-check that the context-specific content (character names, scenario details) looks correct for that context — not showing baseline content by mistake.

**Result:** One additional package tested clean, judged sufficient given the fixes are shared code, not context-specific.

---

## Summary

**Overall result:** [x] Issues found (see below)

**Issues found:**
1. **Reflective content not restored on genuine SCORM resume** — see open-decisions.md RTR-1

**Confirmed working:**
- SRF-1 (fail → resume → retry) — **fully working**
- Sortable contrast fix — **working**
- Sortable ARIA/keyboard — **working, no regression**
- L02 block order — **tentatively confirmed**
- Reflective masking (in-session only) — **working**
- CRO-1 (confidence row overflow) — **verified fixed** (30 July 2026, local SCORM harness)

---

## After this checklist

- [x] Investigate and resolve RTR-1 (reflective text restore on SCORM resume) — **IMPLEMENTED** (30 July 2026):
  - [x] Original `cmi.interactions` approach disproven (250-char SPM truncation)
  - [x] `adapt-abbott-interactions-restore` extension removed (was actively harmful)
  - [x] New `adapt-abbott-reflective-store` extension implemented (suspend_data approach)
- [x] CRO-1 (confidence row overflow) — **VERIFIED FIXED** (commit 4658a41, verified 30 July 2026)
- [x] Regenerate SCORM packages after RTR-1 fix — built `academic-writing-introductory_baseline_20260730_204837_954f8eb.zip`
- [x] **RTR-1 Moodle verification — RESTORE PATH VERIFIED** (30 July 2026):
  - [x] Deploy package with `adapt-abbott-reflective-store` extension (capacity probe removed)
  - [x] Resume course from prior session
  - [x] **VERIFIED:** Full text restored — console evidence:
    ```
    [reflective-store] Restored L02-c-40: "Lorem ipsum dolor sit amet, consectetur adipiscing..." (2013 chars)
    [reflective-store] Restore complete: 1 component(s) restored from suspend_data
    ```
  - [x] 2,013 chars restored intact (vs 250 under disproven interactions route)
  - [x] No error 406; `cmi.location` writes succeeded normally
  - **Caveat:** Moodle attempt contained leftover `probe:1800`/`probe:5000` payloads from earlier probe build; restored text was written in prior session. Restore verified; write path verified locally but not yet in Moodle with clean suspend_data.
- [x] **RTR-1 clean write path verification — VERIFIED** (31 July 2026):
  - [x] Delete existing Moodle attempt (clear suspend_data)
  - [x] Fresh reflection → submit → close browser
  - [x] Resume → confirm full text restored
  - [x] **Write evidence:**
    ```
    [reflective-store] Storing L02-c-40: 2029 chars
    [reflective-store] L02-c-40: stored successfully
    ```
  - [x] **Restore evidence:**
    ```
    [reflective-store] Restored L02-c-40: "Lorem ipsum dolor sit amet, consectetur adipiscing..." (2029 chars)
    [reflective-store] Restore complete: 1 component(s) restored from suspend_data
    ```
  - [x] Moodle track details confirmed `rtr:L02-c-40` in `cmi.suspend_data` with complete 2,029-char reflection
  - [x] Corroboration: `cmi.interactions.1.learner_response` truncated at 250 chars (confirms why interactions route was abandoned)
  - [x] **RTR-1 FULLY VERIFIED**
- [x] Move verified packages to `scorm-packages/verified/` per RC-1c convention — `academic-writing-introductory_baseline_20260730_204837_954f8eb.zip` moved 31 July 2026
- [x] **CB-1 Moodle verification — COMMIT BEHAVIOUR VERIFIED** (31 July 2026):
  - [x] Fresh attempt, answered several L02 questions (no lesson completion, no status boundary crossed)
  - [x] Closed browser tab directly (no exit navigation)
  - [x] Relaunched: all MCQ answers and activity state restored correctly
  - [x] Direct counterpart of CB-1b failure scenario — with `_commitOnAnyChange: true`, progress now persists
  - [x] Diagnostic extension (`adapt-abbott-cb-diag`) removed after findings captured
