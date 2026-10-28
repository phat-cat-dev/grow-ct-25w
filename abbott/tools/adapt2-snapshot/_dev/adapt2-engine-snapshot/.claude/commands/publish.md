---
description: Publish a course (status -> production) and lock it. After this, a reopen may change only the fields it unlocks.
argument-hint: <course-slug>
---

Publish course `$1`: set its manifest `status` to `production` and stamp
`publishedAt`. This is the lock milestone (`docs/authoring/field-locks-and-edit-mode.md`):
once published, every gate field is locked. A later change goes through
`/reopen $1 <gate>` naming the decidedValue path(s) it unlocks; `tools/reopen.js`
and the lint refuse any change outside the unlocked set. Records written before
`publishedAt` (the initial-authoring history) are grandfathered.

Run `/publish` only when the human says the course is finished and ready to
lock, never on your own initiative. A course still being authored or refined
stays `in-development` (edits are free there).

1. RECON. Confirm `courses/$1/course-design_$1.json` exists and read its
   current `status`. If it is already `production`, say so and stop (the tool
   is a no-op there). Confirm with the human that `$1` is ready to lock before
   running the tool.

2. Run the tool (idempotent; keeps an existing publishedAt):

       node tools/publish.js --course=$1

   Paste its output.

3. Validate and show it still passes with the course now published:

       python3 tools/validate-design-schemas.py --course-design courses/$1/course-design_$1.json; echo "EXIT: $?"

   The `UNLOCK-SCOPE` line should report the post-publish superseding records
   checked (0 immediately after publishing, since all existing reopens predate
   `publishedAt`). Require exit 0.

4. SHOW-DIFF-STOP. Full `git diff` for the manifest only. Explicit staging of
   `courses/$1/course-design_$1.json`. One commit. No push.
