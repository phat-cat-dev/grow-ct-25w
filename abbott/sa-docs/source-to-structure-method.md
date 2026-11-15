# Source to structure: how the agent reads a source and proposes outcomes and lessons

Ruled 25-26 September 2026 [corrected 26 September 2026, adp-0184: SSM-1's own heading and provenance in `docs/project/open-decisions.md` give "25-26 September 2026, Prompt 180"; this document as supplied said "26 September 2026"] (SSM-1, `docs/project/open-decisions.md`). It replaces `course-template.md`'s "Lesson Count and Sequence" section, `course-creation-workflow.md`'s "4–8 typical" line and the "six-part flow" lesson test, and it governs gates A2 and A3.

## What this is for

The agent reads a source and proposes a structure a teacher can confirm: outcomes first, then the units that teach them. The method does not depend on the source being *Excelling at University*. It works for any book, chapter, article, guide or institutional document, supplied as Markdown that keeps its headings and page markers. It also works at any scale: one activity, a lesson, a course, a module or a programme.

## The steps

**1. Map the source.** Break the source along its own structure: chapter, heading, subheading, then paragraph groups where a section is long. For each chunk, record:
- an id, the heading path and the pages;
- whether it is framing (openings, objectives, summaries) or teaching;
- the content shapes it holds, named from the content-shapes store, each with a short quoted passage as evidence;
- its key concepts, in the source's own terms;
- its pathway and tier tags.

The teacher confirms the map once; after that every gate cites chunks by id. A source that is already mapped is reused, never re-chunked.

**2. Set the scope.** Choose the chunks in scope for this course and tier, each with a reason, and list the chunks left out and why. (Gate A2.)

**3. Propose the course outcomes.** Three to five, three by default, with a stated reason for four or five. Each outcome is one idea (one verb from the tier's verb band, one object) and names the chunks it rests on. (Gate A3.)

**4. Propose candidate lessons.** Group in-scope chunks into candidate lessons by conceptual unit, not by counting sections. Test each candidate:
- Can it carry two to four one-idea outcomes, each testable by a question?
- Do its chunks' shapes fill the lesson's teaching blocks: a concept, a worked example with analysis, and practical guidance?
Merge a candidate that fails the test into its neighbour; split one that needs more than four outcomes.

**5. Set the lesson count.**
- **Core lessons.** Every course outcome has one core lesson that mainly serves it: most of that lesson's outcomes serve that course outcome. So the count starts at the number of course outcomes.
- **Additional lessons.** More lessons are added only where the source's breakdown into candidate topics needs them, or where the teacher asks for one. Content is always the primary driver. A lesson the teacher asks for must still pass the step 4 test on its own content.
- **Mixed lessons.** An additional lesson may serve more than one course outcome, as long as it stays coherent around a single topic.
- **Ceiling.** At most twice as many lessons as course outcomes.

**6. Present and record.** Show the teacher:
- the source map in brief;
- the proposed outcomes;
- the lesson list, with each lesson's chunks, shapes and the course outcome it mainly serves (or "mixed");
- the alternatives considered (a merge or a split), each with its reason.

Then ask. Record what the teacher decides, with provenance.

## How the agent conducts itself

- Quote the source for every claim about what it contains. Never invent coverage.
- Say which in-scope chunks no lesson uses, and why.
- Name gaps plainly. A missing source is a grounding gap, not a guess.
- Never set a count by formula when the content says otherwise. The bounds limit the count; the content decides it.
- Ask one decision at a time. Offer a blank or skip option where a question does not apply.

## What tools check, not the agent

- Outcome counts and the one-idea form.
- Lesson count within its bounds.
- A lesson that mainly serves each course outcome.
- Every cited chunk id exists in the source map.
- Every named content shape exists in the store.

## Scale

- **Activity:** one outcome and one source passage; no lessons.
- **Lesson:** two to four outcomes from a chapter section.
- **Course:** as above.
- **Module or programme:** outcomes at the higher level, with courses in place of lessons; the same bounds and main-focus rule apply one level up.

The general form of this method belongs to the ALIGN project, which is being built for outcome generation at every scale. ADAPT uses it now for courses. The two should converge on one method. [checked 26 September 2026, adp-0184: this claim could not be verified against repo sources this sitting. SSM-1's own grounds in `docs/project/open-decisions.md` already record a zero-hit search for the phrase "ALIGN project" across the Prompt 176-178 reports and a zero-hit repo-wide search for "ALIGN", and state that this clause rests on Abbott's own knowledge, not a survey finding. This sitting did not repeat that search; it defers to SSM-1's own record of it.]
