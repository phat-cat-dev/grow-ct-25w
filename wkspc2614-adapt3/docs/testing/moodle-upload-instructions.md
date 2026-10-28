# Moodle Upload & Configuration Instructions

*Reference document for uploading Academic Writing (and future pathway-tier) SCORM packages to Moodle. Covers both Moodle course-level settings and individual SCORM activity-level settings. Compiled from the P8 walkthrough (28 July 2026), which surfaced the course-level completion-tracking requirement below the hard way.*

---

## Terminology note

- **Moodle course** = the container in Moodle (e.g. a sandbox or module course) that holds one or more SCORM activities.
- **Adapt course / pathway-tier** = the project's own unit (e.g. "Academic Writing: Introductory Stage") — packaged as a single SCORM zip and uploaded *into* a Moodle course as one activity.

Do not confuse the two. Settings described as "course-level" below refer to the **Moodle course**, not the Adapt tier.

---

## Part A — Moodle Course-Level Settings (set once per Moodle course)

These apply to the whole Moodle course and affect every activity inside it, including the SCORM package.

### A1. Completion tracking — REQUIRED

**Location:** Moodle course → Settings (gear icon) → find "Completion tracking" section (may appear under a "Student progress" heading depending on theme).

**Setting:** "Enable completion tracking" → **Yes**.

**Why this matters:** if this is set to **No**, Moodle will never show *any* activity in the course as complete, regardless of how correctly the SCORM package itself is built or configured. Symptom if missed: the SCORM activity's own settings page will have **no "Activity completion" section at all** — Moodle only renders that section once course-level tracking is enabled. This was discovered during the P8 walkthrough (28 July 2026) as the root cause of an apparent "W-CLOSE won't mark complete" bug, which turned out to be this setting, not a package fault.

**Check this FIRST** whenever completion status looks wrong in a new Moodle course — it is more likely than a package bug.

---

## Part B — SCORM Activity-Level Settings (set once per uploaded package)

These apply to the individual SCORM activity (i.e. per pathway-tier/context package uploaded). Go to the activity's own Settings (Edit settings) to configure.

### B1. Package file

Upload the SCORM zip under the **Package** section. Confirm the file shows as an Archive (ZIP) and that no error appears on save (a common failure is `imsmanifest.xml` not sitting at the zip's root — verify this before upload if a new build ever fails here).

### B2. Grading method

**Location:** Grade section → "Grading method."

Options: Learning objects / Highest grade / Average grade / Sum grade. **Recommended: Highest grade** (records the best-scoring attempt) unless there's a specific reason to average or sum across multiple attempts.

**Maximum grade:** typically 100.

### B3. Attempts management

- **Number of attempts:** Unlimited, unless the pathway design specifically wants to cap retries.
- **Attempts grading:** "Highest attempt" is the sensible default if multiple attempts are allowed — records the best result in the gradebook regardless of which attempt it came from.
- **Force new attempt:** "No" is the safest default — lets a learner resume an in-progress attempt rather than being forced into a fresh one. As of 29 July 2026 (SRF-1 fix), the assessment's `_isResetOnRevisit` is set to `false`, so a resumed session correctly preserves fail state and requires an explicit "Try again" click rather than auto-resetting — confirm this still pairs sensibly with whatever "Force new attempt" is set to here.

### B4. Activity completion — REQUIRED

**Location:** the activity's own settings → "Activity completion" section. **This section will not appear at all unless Part A1 (course-level completion tracking) is enabled first.**

**Completion conditions to select:** click "Add requirements," then tick **only "Completed."**

**Do NOT tick:**
- **"Passed"** — the package's spoor configuration deliberately reports SCORM status as `"completed"` on a pass and `"incomplete"` on a fail; it never reports a `"passed"` status. Ticking this condition means the activity would never show as Moodle-complete, even on a genuine pass.
- **"Receive a grade"** — the package submits a score on every attempt, including failed ones (`_shouldSubmitScore: true`). Ticking this would cause even failed attempts to mark the activity complete, contradicting the intended pass/fail distinction.
- **"Require minimum score"** — this would duplicate the 70% pass threshold already enforced inside the package itself, risking two thresholds disagreeing with each other if they're ever set to different values.

Optional, harmless to add alongside "Completed": **"View the activity."**

**Why "Completed" alone is correct:** it aligns exactly with the package's own reporting logic — `_onTrackingCriteriaMet: "completed"` fires on pass, `_onAssessmentFailure: "incomplete"` fires on fail — so Moodle's completion tick will only appear when the package itself reports genuine completion, correctly reflecting pass/fail without needing a second, potentially conflicting condition.

### B5. Display settings

- **Display package:** "New window" (keeps the SCORM player separate from Moodle's own chrome).
- **Display content structure in player:** "Disabled" (the Adapt course has its own internal menu/navigation; Moodle's SCORM table-of-contents overlay isn't needed).
- **Disable preview mode:** "Yes" recommended for production use, so students can't browse the content without it counting as a genuine attempt (adjust if preview access is specifically wanted for staff/QA).

### B6. Compatibility settings

- **Force completed:** No (let the package's own status reporting drive completion, don't override it).
- **Mastery score overrides status:** review case-by-case; generally leave as configured by default unless a specific reason to change it.

---

## Part C — Post-Upload Verification Checklist

After configuring both course-level and activity-level settings, verify before considering the upload "done":

- [ ] Package uploads and launches without error.
- [ ] Complete one **pass** attempt (≥70%) — confirm the activity shows as **complete** in the course.
- [ ] Complete one **fail** attempt (<70%) — confirm the activity shows as **incomplete** (not complete) in the course.
- [ ] Confirm the gradebook records the correct score for each attempt.
- [ ] Confirm suspend/resume works (exit partway, return, position restored).
- [ ] Confirm resume also works correctly after a **failed** attempt specifically (retry path), not just after a pass — as of the SRF-1 fix (29 July 2026), the fail state and "Try again" button should now persist correctly across a resume.

---

## Known gotchas (from the 28-29 July P8 walkthrough, updated 29 July with fixes applied)

1. **Missing "Activity completion" section** on the activity settings page = course-level completion tracking is off (Part A1). Not a package bug — check this first.
2. ~~**References component links open inside the SCORM iframe** rather than a new tab~~ — **FIXED 29 July 2026**: template confirmed correct with `target="_blank"` and `rel="noopener"`.
3. ~~**Reflective text input content displays masked/read-only after results**~~ — **FIXED 29 July 2026**: patched via `patches/adapt-contrib-textInput+reflective-answer-restore.patch`; content now displays readably after submission (still read-only, not editable — that's a separate, smaller enhancement not yet done).
4. ~~**Suspend/resume after a failed attempt silently resets the assessment**~~ — **FIXED 29 July 2026** (SRF-1, `open-decisions.md` #33): `_isResetOnRevisit` changed to `false` on SUMM's assessment config. Fail state and "Try again" now correctly persist across a resumed session.

---

*This document should be kept up to date as new gotchas or settings requirements are discovered during future uploads (new pathways, new tiers, or new Moodle instances).*
