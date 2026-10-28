---
description: Show the standing ledger for a course from the manifest. Read-only.
argument-hint: <course-slug>
allowed-tools: Read, Bash(node tools/session-audit.js:*), Bash(node tools/verify-course.js:*)
---

Standing command "show me the ledger" for course `$1`. Derive
everything from `courses/$1/course-design_$1.json` and
`design-kb/design-kb.gates.json`. Do not use memory of earlier turns.

Print, in order:

1. Every gate id in gates.json, for this course's phase set (A, B per
   lesson in the A3 breakdown, S, W, D), with: state (open, closed,
   deferred, absent), latest seq, provenance, sessionRef.
2. Hard-stops still open, listed separately.
3. Assumptions tally: every soft gate that stood on silence, by
   `defaultType` — `fixed-value` as `ai-default-stood`,
   `ai-proposal-stands` as `ai-proposal-stood` (GI-2,
   `docs/project/open-decisions.md`, 27 Aug 2026;
   `schemas/common.schema.json`'s `provenance` enum description states
   the distinction directly).
4. Open `sweepEvents` with unconfirmed invalidates or flags.
5. `groundingGaps` across all records.
6. Instantiations: count, and which scaffolded pages in
   `courses/$1/en/contentObjects.json` have NO instantiation (a page
   without one is invisible to conformance-lint clause 1).
7. Run `node tools/session-audit.js --course=$1` and paste its final
   report verbatim.

End with one line: "Ledger derived from manifest at <git short hash>".
