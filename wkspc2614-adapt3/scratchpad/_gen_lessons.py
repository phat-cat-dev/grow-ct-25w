import json, os

OUT = "scratchpad"

def go(items):
    return {"_component": "growOutcomes", "_classes": "", "_layout": "full",
            "title": "What you will be able to do", "body": "",
            "instruction": "Press reveal to see each outcome for this lesson.",
            "_items": [{"text": t} for t in items]}

def text(title, body, classes=""):
    return {"_component": "text", "_classes": classes, "_layout": "full",
            "title": title, "body": body, "instruction": ""}

def worked_example(lesson_key, weaker, stronger, setup, closer):
    body = f"<p>{setup}</p><p class=\"we-weaker\">{weaker}</p><p class=\"we-stronger\">{stronger}</p><p>{closer}</p>"
    return {"_component": "text", "_classes": f"slot__{lesson_key}__worked-example", "_layout": "full",
            "title": "Worked example", "displayTitle": "Worked example", "body": body, "instruction": "",
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False}}

def opentext(items):
    return {"_component": "opentext", "_classes": "", "_layout": "full",
            "title": "Your turn", "body": "",
            "instruction": "This is for your own reflection; no right answers are expected.",
            "_items": [{"text": t} for t in items]}

def keyTerm(term, pos, definition, extended, example, related):
    return {"_component": "keyTerm", "_classes": "", "_layout": "full",
            "term": term, "_partOfSpeech": pos, "definition": definition,
            "extendedDefinition": extended, "example": example, "_relatedTerms": related,
            "_reveal": True,
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False}}

def glossary(title, display, instruction, passage):
    return {"_component": "glossary", "_classes": "", "_layout": "full",
            "title": title, "displayTitle": display, "body": "", "instruction": instruction,
            "_passage": passage,
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False}}

def annotated(display, instruction, passage):
    return {"_component": "annotated", "_classes": "", "_layout": "full",
            "title": "", "displayTitle": display, "body": "", "instruction": instruction,
            "_passage": passage,
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False}}

def tabs(display, body, instruction, items):
    return {"_component": "tabs", "_classes": "", "_layout": "full",
            "title": "", "displayTitle": display, "body": body, "instruction": instruction,
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False},
            "_items": items}

def growLevels(display, instruction, items):
    return {"_component": "growLevels", "_classes": "", "_layout": "full",
            "title": "", "displayTitle": display, "body": "", "instruction": instruction,
            "_setCompletionOn": "allOpened",
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False},
            "_items": items}

def branching(display, body, start, nodes):
    return {"_component": "branching", "_classes": "", "_layout": "full",
            "title": "Decision scenario", "displayTitle": display, "body": body,
            "instruction": "Read each situation and choose a response to see what happens next.",
            "ariaRegion": "Decision scenario. Read each situation and choose a response to see what happens next.",
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False},
            "_scenario": {"_start": start, "_nodes": nodes}}

def checklist(title, display, body, items):
    return {"_component": "checklist", "_classes": "", "_layout": "full",
            "title": title, "displayTitle": display, "body": body,
            "instruction": "Tick each item once you have tried it.",
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False},
            "_items": [{"text": t} for t in items]}

def sortable(title, display, body, instruction_extra, items, correct_feedback, incorrect_feedback):
    return {"_component": "sortable", "_classes": "", "_layout": "full",
            "title": title, "displayTitle": display, "body": body,
            "instruction": "Drag items to reorder, or use the keyboard (Enter to grab, arrows to move, Enter to drop). Then select Submit.",
            "ariaQuestion": instruction_extra,
            "_attempts": -1, "_shouldDisplayAttempts": False, "_questionWeight": 1,
            "_canShowModelAnswer": True, "_canShowFeedback": True, "_canShowMarking": True,
            "_recordInteraction": True, "_isPartOfAssessment": False,
            "_items": [{"text": t} for t in items],
            "_feedback": {"title": "", "correct": correct_feedback,
                          "_incorrect": {"notFinal": incorrect_feedback, "final": ""}},
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False}}

def matching(title, display, body, aria, rows):
    return {"_component": "matching", "_classes": "", "_layout": "full",
            "title": title, "displayTitle": display, "body": body,
            "instruction": "Select an option for each item, then select Submit.",
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False},
            "ariaQuestion": aria, "_attempts": 1, "_shouldDisplayAttempts": False,
            "_questionWeight": 1, "_hasItemScoring": False, "_canShowModelAnswer": True,
            "_canShowCorrectness": False, "_canShowFeedback": True, "_canShowMarking": True,
            "_recordInteraction": True, "_shouldResetAllAnswers": True, "_isRandom": False,
            "_isRandomQuestionOrder": False, "_allowOnlyUniqueAnswers": False,
            "placeholder": "Select an option", "_isPartOfAssessment": False,
            "_items": rows}

def mcq(title, display, aria, items):
    return {"_component": "mcq", "_classes": "knowledge-check-question", "_layout": "full",
            "title": title, "displayTitle": display, "body": "",
            "instruction": "Choose one option and select Submit.",
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": True},
            "ariaQuestion": aria, "_selectable": 1, "_items": items}

def slider(display, body, labelStart, labelEnd, scaleStart, scaleEnd, correctBottom, correctTop, correct_fb, incorrect_fb):
    return {"_component": "slider", "_classes": "", "_layout": "full",
            "title": "Slider", "displayTitle": display, "body": body,
            "instruction": "Drag the slider to make your choice, then select Submit.",
            "ariaQuestion": "", "ariaScaleName": f"Scale from {scaleStart} to {scaleEnd}.",
            "_attempts": 1, "_shouldDisplayAttempts": False, "_questionWeight": 1,
            "_canShowModelAnswer": True, "_canShowCorrectness": False, "_canShowFeedback": True,
            "_canShowMarking": True, "_recordInteraction": True,
            "labelStart": labelStart, "labelEnd": labelEnd,
            "_scaleStart": scaleStart, "_scaleEnd": scaleEnd, "_scaleStep": 1,
            "scaleStepPrefix": "", "scaleStepSuffix": "", "_correctAnswer": "",
            "_correctRange": {"_bottom": correctBottom, "_top": correctTop},
            "_showNumber": True, "_showScaleIndicator": True, "_showScale": True, "_showScaleNumbers": True,
            "_feedback": {"title": "Feedback", "altTitle": "", "correct": correct_fb,
                          "_incorrect": {"notFinal": "", "final": incorrect_fb}},
            "_pageLevelProgress": {"_isEnabled": True, "_isCompletionIndicatorEnabled": False}}


def build_lesson(key, lo_list, blocks):
    """blocks: list of component dicts in order. Assigns ids/parentIds sequentially."""
    out = []
    for i, comp in enumerate(blocks, start=1):
        c = dict(comp)
        c["_id"] = f"{key}-c-{i:02d}"
        c["_parentId"] = f"{key}-b-{i:02d}"
        c["_type"] = "component"
        out.append(c)
    return out

def write_lesson(filename, key, lo_list, parts):
    comps = [go(lo_list)] + parts
    data = build_lesson(key, lo_list, comps)
    path = os.path.join(OUT, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print("wrote", path, len(data), "components")

# ======================================================================
# INTRODUCTORY
# ======================================================================

write_lesson(
    "draft-lesson_criticality-intro-L02.json", "crit-intro-L02",
    ["Apply critical thought to the choices you make when searching, reading and planning, not only when writing."],
    [
        text("Being critical before you write a word",
             "<p>Being critical is usually framed as something you do to a finished source: you read it, then judge it. But the habit starts earlier than that, in the choices you make while deciding what to search for, what to read, and what to trust before you have written anything at all.</p>"),
        text("Opening up the discourse",
             "<p>Dennis and Abbott (2026, pp.117-118) put the goal plainly: 'When beginning your research, therefore, your goal should be to open up the relevant discourse.' That means your first search should deliberately widen what you see, not just confirm what you already expected to find.</p>"),
        worked_example("L02",
            "{{learner-a}} searches a topic, keeps the first three results because they are easy to find, and starts writing from those alone.",
            "{{learner-b}} searches the same topic, but deliberately varies the search terms to surface more than one position, and only then decides which sources to trust.",
            "Consider two students starting the same piece of coursework.",
            "Both searched. Only {{learner-b}} opened up the discourse before settling on a view."),
        text("Why this counts as being critical",
             "<p>Nothing here is about reading more. It is about noticing that the first search result is one voice in a discourse, not the whole of it, and choosing to look for the other voices before you decide what you think.</p>"),
        checklist("Search choices checklist", "Before you start searching",
                  "Use these questions before you commit to a set of sources.",
                  ["Did I write down the scope of the question before searching?",
                   "Did I note which sources I will trust, and why?",
                   "Did I vary my search terms rather than using the first ones I thought of?",
                   "Did I flag any assumption built into how the question was framed?"]),
        sortable("Order the search steps", "Put the search steps in order",
                 "These four steps describe a critical approach to starting a search, but they are out of sequence.",
                 "Put the four search steps in order, from first to last.",
                 ["Scope the question before searching anything.",
                  "Note which sources you will trust and why.",
                  "Search with deliberately varied terms.",
                  "Flag any assumptions built into what you find."],
                 "That is the right order. Scoping and noting trusted sources come before you search, varied terms open up the discourse, and flagging assumptions comes once you have something to question.",
                 "Not quite. Think about what has to be decided before you search, and what can only happen once you have results to look at."),
        text("Doing this in practice",
             "<p>Before you collect anything, write down the scope of your question, the sources you expect to trust, and any assumption you can already see in how the question is framed. This takes minutes, and it changes what you end up reading.</p>"),
        opentext(["Think of a recent piece of work. Did your search open up the discourse, or did it confirm what you already expected?",
                  "What is one search term you could add next time to deliberately surface a different position?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-intro-L03.json", "crit-intro-L03",
    ["Map and question the scholarly discourse around a topic, starting from wherever you are."],
    [
        text("Starting from a textbook is not a weakness",
             "<p>It is tempting to think that a 'proper' discourse map has to start with journal articles. It does not. Starting from a textbook, as a less experienced reader, is a sensible first step, provided you then use it to open up the wider discourse rather than stopping there.</p>"),
        text("The book's own example",
             "<p>Dennis and Abbott (2026, pp.118-119) illustrate this with a worked example. 'As a less experienced learner, and with the principle of \u2018building knowledge\u2019 in mind, John begins by looking at the textbook he found, Creativity in Primary Education, edited by Anthony Wilson (3rd ed., 2015).' John's starting point is ordinary. What matters is what he does with it next: using it to find the wider positions in the field, not treating it as the final word.</p>"),
        worked_example("L03",
            "{{learner-a}} finds three sources on a topic and lists them in the essay, one after another, with no sense of how they relate.",
            "{{learner-b}} finds the same three sources, but groups them by the position each one takes, and writes one question against each group: what is this group assuming, and who does its claim affect?",
            "Consider two students who have each gathered a small set of sources on the same topic.",
            "Both had the sources. Only {{learner-b}} had mapped the discourse, rather than just listing it."),
        text("Why grouping and tagging counts as mapping",
             "<p>A list of sources is not a map. A map groups positions together and asks a question of each group. That is what turns 'I found some sources' into 'I have mapped and questioned the discourse around this topic', which is the skill this lesson is building.</p>"),
        tabs("Three ways to start opening up a discourse",
             "Different starting points all lead to the same destination: a mapped, questioned discourse.",
             "Select each tab to see how that starting point leads on to mapping the wider discourse.",
             [
                 {"tabTitle": "From a textbook", "title": "From a textbook",
                  "body": "A textbook gives you the settled, well-established version of a topic. Use its references and signposting to find the live debates it is built on, then go looking for the positions on either side."},
                 {"tabTitle": "From a review article", "title": "From a review article",
                  "body": "A review article has already grouped positions for you. Use its groupings as a starting map, then check whether more recent work has shifted the picture it describes."},
                 {"tabTitle": "From a recent paper", "title": "From a recent journal paper",
                  "body": "A recent paper usually opens by placing itself against existing positions. Use its own framing of the debate as a starting map, then check who it has left out."},
             ]),
        annotated("A short discourse map, annotated",
                  "Select a highlighted phrase to see why it matters.",
                  [
                      {"text": "Three positions on this topic can be grouped as follows: ", "_note": ""},
                      {"text": "Group A argues the effect is strong", "_note": "Naming the position, not just the authors, is what makes this a map rather than a list."},
                      {"text": ", ", "_note": ""},
                      {"text": "Group B argues it is weak once other factors are controlled for", "_note": "A genuine discourse map needs the disagreement stated, not smoothed over."},
                      {"text": ", and ", "_note": ""},
                      {"text": "Group C questions whether the effect can be measured at all", "_note": "The question a group leaves open is often more useful than its headline claim."},
                      {"text": ".", "_note": ""},
                  ]),
        text("Building your own map",
             "<p>Start wherever you are, even a textbook. List the positions you find, group them, and write one question against each group: what is it assuming, and who does it affect. That one-page map is the mapping and questioning this lesson is about.</p>"),
        opentext(["Pick a topic from your own course. What is the first, most accessible source you would start from?",
                  "What question would you ask of the position that source takes?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-intro-L04.json", "crit-intro-L04",
    ["Use Bloom's taxonomy as a map of where 'being critical' sits, from remembering to creating."],
    [
        text("A ladder, not a single step",
             "<p>So far this lesson has talked about 'being critical' as one habit. It is worth seeing where that habit actually sits on a wider ladder of thinking, so you can notice when you are only at the bottom of it.</p>"),
        text("Six rungs",
             "<p>Anderson and Krathwohl's (2001) revised taxonomy sets out six levels of thinking: remember, understand, apply, analyse, evaluate, and create. Being critical mostly lives in the top three: breaking a claim down (analyse), judging it against others (evaluate), and building something new from what you have judged (create). This is a preview of the ladder, not a test of it; you will practise analyse and evaluate properly in later lessons.</p>"),
        worked_example("L04",
            "{{learner-a}} reads a source and can recite its main claim back accurately. That is remembering and understanding, useful, but it stops there.",
            "{{learner-b}} reads the same source, then breaks its claim into the evidence it rests on and checks that evidence against another source. That is moving up the ladder into analysis and evaluation.",
            "Consider two students who have each just read the same journal article.",
            "Both understood the article. Only {{learner-b}} had moved up the ladder."),
        text("Why the ladder matters for a habit of mind",
             "<p>A habit of mind is not a one-off climb. The point is to notice, every time, which rung you are actually on, and to make moving up it automatic rather than something you only do when a task tells you to.</p>"),
        keyTerm("Analyse", "verb",
                "To break a claim, source or data set down into its parts in order to examine how it works or what it rests on.",
                "In Anderson and Krathwohl's (2001) revised taxonomy, 'analyse' sits above 'understand' and below 'evaluate': you are expected to take something apart, not just restate it.",
                "Analysing a claim means asking what evidence it is built on, not just what the claim itself says.",
                ["Evaluate", "Bloom's taxonomy", "Critical thought"]),
        sortable("Order the six levels", "Put Bloom's six levels in order",
                 "These six levels of thinking, from Anderson and Krathwohl (2001), are listed out of order.",
                 "Put the six levels of the revised taxonomy in order, from the most basic to the most demanding.",
                 ["Remember", "Understand", "Apply", "Analyse", "Evaluate", "Create"],
                 "That is the correct order, from remembering a fact up to creating something new from your own judgement of it.",
                 "Not quite. Think about which level has to come before another: you cannot evaluate something you have not yet analysed."),
        text("Noticing your own rung",
             "<p>Next time you read something for a task, pause and ask which rung you are actually on. If you can only restate the claim, you are not critical about it yet, whatever else the task required.</p>"),
        opentext(["Think of something you read this week. Which rung of the ladder were you actually on, honestly?",
                  "What would it take to move one rung higher next time, without it taking much longer?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-intro-L05.json", "crit-intro-L05",
    ["Map the voices on a real issue, note where they agree and disagree, and write down the questions they leave open."],
    [
        text("Discourse mapping outside a reading list",
             "<p>Mapping a discourse is not only an academic exercise done on a reading list. The same skill applies whenever several sources say different things about a real issue and someone needs to make sense of them.</p>"),
        text("A real example",
             "<p>Imagine volunteering with a local food bank, where the coordinator wants to know what is being said about food insecurity among students. You would map the main voices, such as university reports, a charity briefing, and research articles, note where they agree and disagree, and write down the questions they leave open, for example whether the published figures include part-time and commuting students.</p>"),
        worked_example("L05",
            "{{learner-a}} finds three sources that mention food insecurity and lists them in a note for the coordinator, without saying how they relate.",
            "{{learner-b}} finds the same three sources, maps who says what, marks where they agree and disagree, and writes down the question that none of them answer: do the figures include part-time and commuting students?",
            "Consider two volunteers asked to brief the same coordinator.",
            "Both read the same sources. Only {{learner-b}} had mapped them, and found the gap nobody had filled."),
        text("Why this still counts as being critical",
             "<p>Nobody marked this task. The coordinator did not ask for a discourse map by name. But mapping who says what, and noticing what none of them say, is exactly the same critical habit this lesson has been building, now running in a setting with no deadline attached.</p>"),
        matching("Match the source to its strength", "What is each kind of source good for?",
                 "Different sources are strong in different ways. Match each source type to what it is best placed to tell you.",
                 "Match each source type to the kind of claim it is best placed to support.",
                 [
                     {"text": "A university report", "_options": [
                         {"text": "Official statistics at scale", "_isCorrect": True, "_score": 1},
                         {"text": "Frontline, day-to-day experience", "_isCorrect": False, "_score": 0}]},
                     {"text": "A charity briefing", "_options": [
                         {"text": "Frontline, day-to-day experience", "_isCorrect": True, "_score": 1},
                         {"text": "Official statistics at scale", "_isCorrect": False, "_score": 0}]},
                     {"text": "A peer-reviewed research article", "_options": [
                         {"text": "Analysis checked by other researchers", "_isCorrect": True, "_score": 1},
                         {"text": "A single organisation's own figures", "_isCorrect": False, "_score": 0}]},
                 ]),
        branching("Briefing the coordinator",
                  "The food bank coordinator asks you to check whether the published figures on student food insecurity are reliable before she uses them in a funding bid.",
                  "s1",
                  {
                      "s1": {"body": "The coordinator asks you to check whether the published figures are reliable before she uses them in a funding bid. What do you do first?",
                             "_choices": [
                                 {"text": "Pass the figures on as they are; they were published, so they should be fine.", "consequence": "The figures go into a funding bid unchecked, which is a risk if they turn out to be incomplete.", "_goto": "poor"},
                                 {"text": "Check what population the figures actually cover.", "consequence": "A sound first move: a published figure is only as good as what it was measured on.", "_goto": "s2"},
                             ]},
                      "s2": {"body": "You find the figures do not mention part-time or commuting students. What now?",
                             "_choices": [
                                 {"text": "Use the figures as they are, since no better ones exist.", "consequence": "Workable, but the gap needs to be stated, not left implicit.", "_goto": "neutral"},
                                 {"text": "Flag the gap clearly to the coordinator alongside the figures.", "consequence": "The coordinator can now use the figures honestly, aware of their limits.", "_goto": "good"},
                             ]},
                      "good": {"body": "The coordinator uses the figures with the gap stated plainly. The bid is stronger for being honest about what the data does not cover.", "_outcome": "good"},
                      "neutral": {"body": "The figures go into the bid without the gap being mentioned. They may still hold up, but an assessor who spots the gap themselves will trust the bid less.", "_outcome": "neutral"},
                      "poor": {"body": "An unchecked figure ends up in a funding bid. If it turns out to be incomplete, the bid's credibility is what suffers.", "_outcome": "poor"},
                  }),
        text("Building your own briefing note",
             "<p>Map the main voices on the issue, note where they agree and disagree, and write down one open question that none of them answer. That short note is the same skill as an academic discourse map, built for someone who needs an answer, not a grade.</p>"),
        opentext(["Think of an issue outside your course where you could map 'who is saying what'. Who are the voices?",
                  "What question would you write down as still open, once you had mapped them?"]),
    ]
)

print("Introductory lessons I-2..I-5 written.")

# ======================================================================
# INTERMEDIATE
# ======================================================================

write_lesson(
    "draft-lesson_criticality-inter-L01.json", "crit-inter-L01",
    ["Recognise analysis as breaking an interpretation, body of evidence or data set down through close examination."],
    [
        text("Analysis is not summary",
             "<p>At intermediate level, 'critical thinking' stops being one word for everything and splits into skills you can name and practise separately. The first of these is analysis.</p>"),
        text("What analysis actually means",
             "<p>Dennis and Abbott (2026, pp.119-120) define it directly: 'Analysis refers to the breaking down or opening up of an interpretation, a body of evidence, or a data set through close examination.' Analysis is not describing what a source says. It is taking that claim apart to see what it is built on.</p>"),
        worked_example("L01",
            "{{learner-a}} reads a scholar's interpretation and summarises it accurately in their own words.",
            "{{learner-b}} reads the same interpretation and breaks it into its claim, the evidence offered for it, and the assumption it rests on.",
            "Consider two students reading the same journal article.",
            "Both could restate the interpretation. Only {{learner-b}} had analysed it."),
        text("Why this is a distinct skill",
             "<p>A good summary can still leave an interpretation untouched. Analysis means opening it up: separating the claim from the evidence from the assumption, so each part can be checked on its own.</p>"),
        keyTerm("Analysis", "noun",
                "The breaking down or opening up of an interpretation, a body of evidence, or a data set through close examination (Dennis and Abbott, 2026, p.119).",
                "Analysis is the skill this lesson isolates from the wider idea of 'being critical': it is one specific move, not the whole habit.",
                "Analysing an argument means separating its claim from the evidence it rests on, rather than simply repeating the claim.",
                ["Evaluation", "Interpretation", "Evidence"]),
        sortable("Order the steps of analysis", "Put the steps of analysing an interpretation in order",
                 "These four steps describe how to analyse an interpretation, but they are out of sequence.",
                 "Put the four steps of analysis in order, from first to last.",
                 ["Identify the claim being made.",
                  "Identify the evidence offered for it.",
                  "Identify the assumption it rests on.",
                  "Decide what the claim actually depends on."],
                 "That is the right order. You need the claim and its evidence before you can see the assumption underneath, and only then can you say what it depends on.",
                 "Not quite. Think about what you need to see before you can spot the assumption underneath a claim."),
        text("Practising analysis on your own reading",
             "<p>Next time you read an interpretation for a seminar, try writing its claim, its evidence, and its assumption as three separate lines. If you cannot fill in all three, you have found where the interpretation is thin.</p>"),
        opentext(["Pick a claim from something you read this week. What was its evidence, and what assumption sat underneath it?",
                  "Was there a claim you accepted without being able to state its evidence? What made you accept it anyway?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-inter-L02.json", "crit-inter-L02",
    ["Analyse and evaluate a scholarly interpretation by weighing it against alternatives."],
    [
        text("From analysis to evaluation",
             "<p>Analysis opens an interpretation up. Evaluation is the next move: deciding how much weight that interpretation actually deserves, once it is sitting next to the alternatives.</p>"),
        text("What evaluation actually means",
             "<p>Dennis and Abbott (2026, pp.120-121) define evaluation as 'the practice of assessing the relative value of a factor against that of other factors.' The key word is relative: evaluation only means something once you have more than one interpretation to weigh against each other.</p>"),
        worked_example("L02",
            "{{learner-a}} reads two interpretations of the same event and treats them as equally convincing, since both are published.",
            "{{learner-b}} reads the same two interpretations and weighs them against each other using stated criteria: which uses stronger evidence, and which accounts for more of what is known.",
            "Consider two students who have each read the same two interpretations.",
            "Both had read the interpretations. Only {{learner-b}} had evaluated them."),
        text("Why relative weighing matters",
             "<p>Calling an interpretation 'wrong' is rarely useful. Saying which of two interpretations is better supported, and why, is what evaluation actually asks you to do, and it is a more defensible judgement besides.</p>"),
        annotated("Weighing two interpretations, annotated",
                  "Select a highlighted phrase to see why it matters.",
                  [
                      {"text": "Interpretation A rests on a single case study", "_note": "A single case is suggestive, but it is a narrower evidence base than a wider sample."},
                      {"text": ", while Interpretation B draws on a larger, more varied sample", "_note": "A wider sample does not automatically win, but it does carry more weight unless there is a reason to distrust it."},
                      {"text": ". On the evidence offered, B currently carries more weight, though a reason to distrust the sample would change that.", "_note": "Stating the criterion (evidence base) and keeping the judgement open to revision is what makes this an evaluation rather than a preference."},
                  ]),
        slider("How confident are you in weighing interpretations?",
               "Rate how confident you feel about weighing one interpretation against another using stated criteria.",
               "Not confident", "Very confident", 1, 5, 4, 5,
               "Good. Try applying this to a real pair of interpretations from your own reading this week.",
               "Try the annotated example above again, and notice exactly which criterion made one interpretation stronger."),
        text("Doing this with your own reading",
             "<p>When you meet two interpretations that disagree, name one criterion before you decide between them: strength of evidence, size of sample, or how much of the picture it accounts for. State the criterion, then say which interpretation wins on it.</p>"),
        opentext(["Think of two sources you have read that disagreed. What criterion would you use to weigh them against each other?",
                  "Did you ever treat two sources as equally convincing just because both were published? What would change that now?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-inter-L03.json", "crit-inter-L03",
    ["Read a journal article strategically by its structure, rather than reading it start to finish."],
    [
        text("Reading an article is not reading a story",
             "<p>A journal article is not written to be read from the first word to the last. It has a structure, and knowing that structure lets you decide what to read first, and what you can skip.</p>"),
        text("The book's own structure",
             "<p>Dennis and Abbott (2026, pp.121-123) set out the sections of a journal article in the order a reader meets them, in their Table 8.1, and then apply that structure to a worked example. The sections generally run from abstract through introduction, method, results, and discussion to conclusion, but the order you should read them in is not the order they are printed in.</p>"),
        worked_example("L03",
            "{{learner-a}} starts at the introduction and reads straight through to the conclusion, in print order.",
            "{{learner-b}} reads the abstract and conclusion first, then the method, and only turns to the introduction if they still need the background.",
            "Consider two students who have each been given the same journal article to use.",
            "Both finished the article. Only {{learner-b}} had decided how to read it, rather than simply starting at the top."),
        text("Why method-first is a critical choice",
             "<p>Reading the method before the discussion means you judge the findings on how they were produced, not just on how convincingly they are described afterwards. That order is a critical decision, not a shortcut.</p>"),
        tabs("Four things worth checking in a method section",
             "The method section is where a study's claim is actually tested.",
             "Select each tab to see what to check for.",
             [
                 {"tabTitle": "Sample", "title": "Sample",
                  "body": "Who or what was studied, and how many. A claim about a wide population needs a sample that could support it."},
                 {"tabTitle": "Design", "title": "Design",
                  "body": "How the study was set up. A comparison needs something to compare against, not just a single group observed once."},
                 {"tabTitle": "Measures", "title": "Measures",
                  "body": "What was actually measured, and whether that measure really captures the thing the claim is about."},
                 {"tabTitle": "Limits", "title": "Limitations",
                  "body": "What the authors themselves admit the study cannot show. This is often the most honest part of the method section."},
             ]),
        checklist("Reading route checklist", "Before you trust a finding",
                  "Use this order when you next read a journal article for a task.",
                  ["Did I read the abstract and conclusion before anything else?",
                   "Did I check the method before reading the discussion?",
                   "Did I note the sample size and design before judging the finding?",
                   "Did I only read the introduction once I knew I needed the background?"]),
        text("Making this your default",
             "<p>Try this reading order on the next article you are given, even if nobody asks you to. Abstract and conclusion first, then method, then decide if you need the introduction. It takes the same time overall, but you judge the claim rather than just absorbing it.</p>"),
        opentext(["Think of an article you read recently start to finish. What would you have noticed sooner by reading the method first?",
                  "Is there a habit from this lesson you could apply to the very next article you are given?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-inter-L04.json", "crit-inter-L04",
    ["Recognise when a task is asking for analysis or evaluation, even when it does not use those words."],
    [
        text("Real tasks rarely say 'analyse'",
             "<p>Assessment briefs often use the words 'analyse' and 'evaluate' directly. Real requests, from a manager, a client, or a placement supervisor, usually do not. The skill is recognising the same demand underneath different wording.</p>"),
        text("A placement example",
             "<p>On an engineering placement, a supervisor might hand over three requests without using either word: one asking how a system works and why it fails, one asking you to choose between two options, and one asking for both. Reading the brief correctly here is itself a critical skill, confirmed with the supervisor rather than assumed.</p>"),
        worked_example("L04",
            "{{learner-a}} waits for a brief to literally say 'analyse' or 'evaluate' before treating a task as either.",
            "{{learner-b}} reads a request like 'can you look into why this keeps failing' and recognises it as a request for analysis, even though neither word appears.",
            "Consider two placement students handed the same informal request.",
            "Both received the request. Only {{learner-b}} had recognised what it was actually asking for."),
        text("Why this recognition matters",
             "<p>Treating every request as a plain instruction, rather than reading what thinking skill it actually calls for, means you can complete a task technically while missing what was really being asked.</p>"),
        matching("Match the request to the skill it is asking for", "What is this request really asking for?",
                 "Workplace requests rarely use the words 'analyse' or 'evaluate' directly. Match each request to what it is really asking for.",
                 "Match each informal request to the thinking skill it is really asking for.",
                 [
                     {"text": "'Can you look into why this keeps failing?'", "_options": [
                         {"text": "Analysis", "_isCorrect": True, "_score": 1},
                         {"text": "Judgement between options", "_isCorrect": False, "_score": 0}]},
                     {"text": "'Which of these two suppliers should we go with?'", "_options": [
                         {"text": "Judgement between options", "_isCorrect": True, "_score": 1},
                         {"text": "Analysis", "_isCorrect": False, "_score": 0}]},
                     {"text": "'Work out what's going wrong, then tell us which fix to use.'", "_options": [
                         {"text": "Both analysis and judgement", "_isCorrect": True, "_score": 1},
                         {"text": "Neither; just report back", "_isCorrect": False, "_score": 0}]},
                 ]),
        branching("An informal request",
                  "A supervisor sends a message: 'Customers are complaining about the checkout page, can you take a look?'",
                  "s1",
                  {
                      "s1": {"body": "A supervisor messages: 'Customers are complaining about the checkout page, can you take a look?' How do you read this request?",
                             "_choices": [
                                 {"text": "Treat it as a simple instruction to check the page loads.", "consequence": "A narrower reading than the supervisor likely meant, and it may miss the actual problem.", "_goto": "poor"},
                                 {"text": "Read it as a request to work out why customers are complaining.", "consequence": "A reading that matches what is actually being asked, even though the word 'analyse' never appears.", "_goto": "s2"},
                             ]},
                      "s2": {"body": "You find two possible causes. What now?",
                             "_choices": [
                                 {"text": "Report both causes and stop there.", "consequence": "Useful, but the supervisor still has to decide what to do next.", "_goto": "neutral"},
                                 {"text": "Report both causes and recommend which to fix first, with your reasoning.", "consequence": "This answers both the analysis and the judgement the request was quietly asking for.", "_goto": "good"},
                             ]},
                      "good": {"body": "The supervisor gets a clear cause and a reasoned recommendation, exactly what the informal request was actually asking for.", "_outcome": "good"},
                      "neutral": {"body": "The supervisor now has to ask a follow-up question to get the recommendation the original message was really after.", "_outcome": "neutral"},
                      "poor": {"body": "The checkout page 'works', but the actual complaint goes unaddressed, since the real request was never recognised.", "_outcome": "poor"},
                  }),
        text("Reading requests for what they actually ask",
             "<p>Before you act on an informal request, pause and ask yourself whether it is really asking for analysis, judgement, or both, whatever words it happens to use. Confirming your reading with whoever asked is a critical move in itself, not a sign of uncertainty.</p>"),
        opentext(["Think of an informal request you have received, at work, in a club, or at home. What was it really asking for?",
                  "Did you ever answer the literal words of a request and miss what it was actually asking? What would you do differently now?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-inter-L05.json", "crit-inter-L05",
    ["Check a study's method before trusting its claim, especially when a decision rests on it."],
    [
        text("A claim is only as good as its method",
             "<p>A published study's headline claim is easy to accept, especially when it supports what you were already planning to do. Checking the method before trusting the claim is where critical thought actually earns its keep.</p>"),
        text("A workplace example",
             "<p>During a software internship, a team might be asked whether a published study supports adopting a new testing tool. Going straight to the method and results, checking how the tool was actually tested and on what kind of code, matters more than reading the study's own summary of itself.</p>"),
        worked_example("L05",
            "{{learner-a}} reads a study's abstract, sees it supports adopting the new tool, and recommends adopting it.",
            "{{learner-b}} reads the same abstract, then checks the method: the tool was tested on a handful of small open-source projects, quite unlike the team's own large commercial codebase.",
            "Consider two team members asked the same question about the same study.",
            "Both read the study. Only {{learner-b}} had checked whether its method actually supported the team's decision."),
        text("Why this check changes the decision",
             "<p>A study can be entirely honest and still not apply to your situation. Checking the method is not about catching dishonesty; it is about checking whether the evidence actually transfers to the decision you are about to make.</p>"),
        checklist("Method-check checklist", "Before you trust a claim for a decision",
                  "Use these questions before a published claim is allowed to influence a real decision.",
                  ["Did I check what was tested, not just what the abstract concludes?",
                   "Did I check how closely the tested case matches my own situation?",
                   "Did I check the sample size before trusting the result?",
                   "Did I check what the authors themselves say the study cannot show?"]),
        mcq("Formative check: when a study doesn't transfer",
            "A study on a small open-source project claims a new tool improves testing speed. Your team works on a large commercial codebase. What should you do?",
            "What should you do when a study's method does not closely match your own situation?",
            [
                {"text": "Treat the method mismatch as a reason for caution, not an automatic rejection.", "_shouldBeSelected": True,
                 "feedback": "Yes. A mismatch is a reason to weigh the claim carefully, not to dismiss or accept it outright."},
                {"text": "Reject the study outright, since it was not tested on your kind of codebase.", "_shouldBeSelected": False,
                 "feedback": "That overcorrects. The study may still be informative; the mismatch is a reason for caution, not automatic rejection."},
                {"text": "Adopt the tool anyway, since the study's overall conclusion was positive.", "_shouldBeSelected": False,
                 "feedback": "This ignores exactly the mismatch that matters: the tested case and your own situation are not alike."},
            ]),
        text("Making the check routine",
             "<p>Before a published claim gets to influence a real decision, ask what was actually tested and how closely it matches your own situation. That one check is often the difference between evidence that transfers and evidence that merely sounds convincing.</p>"),
        opentext(["Think of a claim you have relied on recently. Did you check what it was actually tested on?",
                  "Is there a decision coming up where a method check like this one would be worth doing first?"]),
    ]
)

print("Intermediate lessons M-1..M-5 written.")

# ======================================================================
# ADVANCED
# ======================================================================

write_lesson(
    "draft-lesson_criticality-adv-L01.json", "crit-adv-L01",
    ["Write with an active approach, using sources to build your own argument rather than only reporting them."],
    [
        text("Two ways to use the same sources",
             "<p>Two students can read exactly the same sources and still write very differently. The difference is not how much they read. It is whether they report what others found, or use it to build a position of their own.</p>"),
        text("The passive approach, named",
             "<p>Dennis and Abbott (2026, pp.123-127) describe one exemplar this way: 'This exemplar illustrates what we call the passive approach to engaging with discourse. Susie has done what many new or less experienced students do when writing: she's prioritised reporting to the reader all the different interpretations she's found ahead of presenting her own view.' Reporting is not the same as arguing.</p>"),
        worked_example("L01",
            "{{learner-a}} writes a paragraph that reports what three sources each say, one after another, and ends without stating a view.",
            "{{learner-b}} writes a paragraph on the same three sources, but opens with the position they are building toward, and uses each source to support or complicate that position.",
            "Consider two draft paragraphs on the same topic, built from the same three sources.",
            "Both paragraphs cited the same sources. Only {{learner-b}}'s paragraph was actually arguing something."),
        text("Why reporting is not enough",
             "<p>A passive paragraph can be accurate, well-referenced, and still say nothing of its own. An active paragraph uses the same sources in service of a position the reader can agree or disagree with.</p>"),
        tabs("Signals of a passive or active paragraph",
             "The same sources can be used two different ways. These signals show which way a paragraph is leaning.",
             "Select each tab to see what to look for.",
             [
                 {"tabTitle": "Reporting", "title": "Reporting language",
                  "body": "Phrases like 'Smith found that...' or 'according to Jones...' repeated across a paragraph, with no sentence that states what you think."},
                 {"tabTitle": "Ordering", "title": "Source-led ordering",
                  "body": "Paragraphs that move source by source, in the order you read them, rather than by the point being made."},
                 {"tabTitle": "Positioning", "title": "Positioning language",
                  "body": "Phrases like 'this suggests...' or 'taken together, these indicate...' that use sources to build toward your own claim."},
             ]),
        annotated("A passive sentence, annotated",
                  "Select a highlighted phrase to see what it signals.",
                  [
                      {"text": "Smith (2019) found X, and Jones (2020) found Y", "_note": "Two findings reported one after another, with nothing yet said about how they relate to the writer's own view."},
                      {"text": ", while Patel (2021) disagreed with both", "_note": "A third finding added to the list; still no position of the writer's own."},
                      {"text": ". Taken together, these three studies suggest that the effect depends on context more than either Smith or Jones allowed for", "_note": "This is the move that turns reporting into positioning: a claim the writer is making, built from, not instead of, the sources."},
                  ]),
        text("Writing actively from here",
             "<p>Before you write a paragraph, decide the position it is building toward. Then bring each source in to support, complicate, or challenge that position, rather than listing what each one separately found.</p>"),
        opentext(["Find a paragraph you have written recently. Was it reporting sources, or using them to argue something of your own?",
                  "What is one sentence you could add to turn a reporting paragraph into a positioning one?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-adv-L02.json", "crit-adv-L02",
    ["Form and justify a judgement on the relative importance of competing factors."],
    [
        text("A judgement needs a reason",
             "<p>Saying one factor matters more than another is easy. Saying why, in a way someone else could check, is the actual skill this lesson is building.</p>"),
        text("The book's own formula",
             "<p>Dennis and Abbott (2026, pp.127-128) give the shape a justified judgement takes, set out as its own formula: 'X is more important (or significant or valuable) than Y because ....' Notice that the formula does not work without the 'because'.</p>"),
        worked_example("L02",
            "{{learner-a}} writes that cost matters more than quality, and moves on without saying why.",
            "{{learner-b}} writes that cost matters more than quality in this case, because the client's stated budget rules out every option that would improve quality.",
            "Consider two drafts reaching the same conclusion about the same two factors.",
            "Both drafts favoured cost over quality. Only {{learner-b}}'s judgement could actually be checked."),
        text("Why stating a criterion first helps",
             "<p>Naming your criterion, such as strength of evidence, size of effect, or fit with a stated constraint, before you rank anything means your judgement can be examined and challenged on that criterion, rather than taken on trust.</p>"),
        checklist("Criteria-stating checklist", "Before you rank anything",
                  "Use these questions before you commit to a judgement about which factor matters most.",
                  ["Did I name my criterion before ranking the factors?",
                   "Did I complete the 'because' in my own judgement?",
                   "Did I say what evidence would change my ranking?",
                   "Did I check my criterion against at least one alternative criterion?"]),
        growLevels("Forming a judgement, move by move",
                   "Open each move to read it. You can keep more than one open at once.",
                   [
                       {"_tone": "neutral", "title": "Move 1: Name the factors",
                        "body": "<p>List the factors actually competing for importance, not just the one you already favour.</p>",
                        "advice": "In practice: write every factor down before ranking any of them, even the ones you expect to dismiss."},
                       {"_tone": "neutral", "title": "Move 2: State your criterion",
                        "body": "<p>Decide what 'important' means here: strength of evidence, size of effect, or fit with a constraint.</p>",
                        "advice": "In practice: name the criterion in one sentence before you rank anything against it."},
                       {"_tone": "neutral", "title": "Move 3: Rank and justify",
                        "body": "<p>Complete the formula: X is more important than Y because ....</p>",
                        "advice": "In practice: if you cannot finish the sentence, your judgement is not ready yet."},
                       {"_tone": "neutral", "title": "Move 4: Say what would change it",
                        "body": "<p>State the evidence that would move your ranking, even if you do not expect to find it.</p>",
                        "advice": "In practice: this is what separates a justified judgement from a fixed opinion."},
                   ]),
        text("Applying this to your own writing",
             "<p>Next time you rank factors in an assignment, write the criterion down first, then complete the formula properly. A judgement with its 'because' attached is one a marker, or a reader, can actually engage with.</p>"),
        opentext(["Think of a judgement you have made recently, academic or otherwise. What was your criterion, even if you did not state it at the time?",
                  "What evidence would have to appear to change that judgement?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-adv-L03.json", "crit-adv-L03",
    ["Apply synthesis in your own writing, drawing sources together to form and express your own argument."],
    [
        text("Beyond analysis and evaluation",
             "<p>Analysis takes an interpretation apart. Evaluation weighs it against alternatives. Synthesis is the move that comes after both: putting pieces back together into something that is now your own.</p>"),
        text("What synthesis actually means",
             "<p>Dennis and Abbott (2026, pp.128-129) define it as 'the ability to draw together different interpretations or evidence in the formation and expression of your own argument.' Synthesis is not summarising several sources. It is building something new from them.</p>"),
        worked_example("L03",
            "{{learner-a}} writes a section source by source: first what Smith argues, then what Jones argues, then what Patel argues.",
            "{{learner-b}} redrafts the same section by grouping the sources around the point each one actually supports, and writes the section around those points, with their own position carrying it.",
            "Consider two drafts covering the same three sources on the same topic.",
            "Both drafts covered the same material. Only {{learner-b}}'s draft was synthesis rather than summary."),
        text("Why grouping by point changes the writing",
             "<p>Once sources are grouped by the point they support, rather than listed in the order you found them, the paragraph has to be organised around your argument instead of around the sources. That reordering is what synthesis actually looks like on the page.</p>"),
        sortable("Order the stages of synthesis", "Put the stages of turning summary into synthesis in order",
                 "These four stages describe redrafting a section from summary into synthesis, but they are out of sequence.",
                 "Put the four stages in order, from first to last.",
                 ["List the sources you currently have, source by source.",
                  "Group the sources by the point each one actually supports.",
                  "Draft the section organised around those points, not the sources.",
                  "Check that your own position is what carries the section."],
                 "That is the right order. You need the sources listed and grouped before you can draft around the points, and the final check confirms the position is actually yours.",
                 "Not quite. Think about what has to happen before you can draft around points rather than sources."),
        tabs("Two ways to open a synthesis paragraph",
             "How you open a paragraph signals whether it will summarise or synthesise.",
             "Select each tab to compare the two openings.",
             [
                 {"tabTitle": "Source-led", "title": "A source-led opening",
                  "body": "'Smith (2019) argues that...' This opening commits the paragraph to following Smith's structure, not yours."},
                 {"tabTitle": "Point-led", "title": "A point-led opening",
                  "body": "'The evidence on this point is mixed.' This opening commits the paragraph to your point, with sources brought in to support it."},
             ]),
        text("Redrafting your own work",
             "<p>Pick one section you have already written source by source. Group its sources by the point each one makes, then redraft the section around those points. The content barely changes; the argument becomes yours.</p>"),
        opentext(["Find a section of your own writing organised source by source. What point could each source be regrouped around?",
                  "What would the opening sentence become if the paragraph led with your point instead of a source?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-adv-L04.json", "crit-adv-L04",
    ["Use the language of criticality, choosing words that show how your ideas relate rather than just listing them."],
    [
        text("Words that do more than connect",
             "<p>Some words in academic writing only join sentences together. Others show the reader exactly how two ideas relate, contrast, build, or follow from each other. That second group is the language of criticality.</p>"),
        text("The book's own examples",
             "<p>Dennis and Abbott (2026, pp.129-131) point to words such as 'although', 'in addition', and 'therefore' as signals of this kind, noting that further examples are set out in the book's own Table 8.2. Each of these words commits you to a specific relationship between two ideas, not just their presence together.</p>"),
        worked_example("L04",
            "{{learner-a}} strings two findings together with 'and': 'Smith found X, and Jones found Y.'",
            "{{learner-b}} writes the same two findings with 'although': 'Although Smith found X, Jones found Y', signalling a contrast the reader is meant to notice.",
            "Consider two sentences reporting the same two findings.",
            "Both sentences were accurate. Only {{learner-b}}'s sentence told the reader how the findings related."),
        text("Why the choice of word is a critical choice",
             "<p>Choosing 'although' over 'and' is not a style preference. It is a claim about how two ideas relate, and getting it wrong misrepresents the relationship between your sources just as much as getting a fact wrong would.</p>"),
        glossary("Three connecting words, defined", "Three connecting words, defined",
                 "Select each highlighted word to see the relationship it signals.",
                 [
                     {"text": "Three words carry particular weight in critical writing: "},
                     {"text": "although", "_term": {"term": "although", "definition": "Signals a contrast: the idea that follows runs against what the reader might expect from the idea before it."}},
                     {"text": ", "},
                     {"text": "in addition", "_term": {"term": "in addition", "definition": "Signals that a further, separate point is being added, not a conclusion drawn from what came before."}},
                     {"text": ", and "},
                     {"text": "therefore", "_term": {"term": "therefore", "definition": "Signals a conclusion: the idea that follows is being drawn as a consequence of what came before, not simply added to it."}},
                     {"text": ". Choosing between them is choosing what relationship you are claiming between two ideas."},
                 ]),
        matching("Match the word to the relationship", "What relationship does each word signal?",
                 "Each connecting word commits you to a specific relationship between two ideas. Match each word to what it signals.",
                 "Match each connecting word to the relationship it signals.",
                 [
                     {"text": "although", "_options": [
                         {"text": "Contrast", "_isCorrect": True, "_score": 1},
                         {"text": "Addition", "_isCorrect": False, "_score": 0}]},
                     {"text": "in addition", "_options": [
                         {"text": "Addition", "_isCorrect": True, "_score": 1},
                         {"text": "Consequence", "_isCorrect": False, "_score": 0}]},
                     {"text": "therefore", "_options": [
                         {"text": "Consequence", "_isCorrect": True, "_score": 1},
                         {"text": "Contrast", "_isCorrect": False, "_score": 0}]},
                 ]),
        text("Choosing deliberately",
             "<p>Before you join two sentences with 'and', ask what relationship actually holds between them. If it is a contrast, a consequence, or an addition, say so. The book's Table 8.2 is worth keeping open while you redraft a section this way.</p>"),
        opentext(["Find a sentence in your own writing joined with 'and'. What relationship was actually there: contrast, addition, or consequence?",
                  "Which connecting word would make that relationship explicit?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-adv-L05.json", "crit-adv-L05",
    ["Use discipline-specific vocabulary precisely, signalling fluency in your field's own discourse."],
    [
        text("Vocabulary that marks who you are writing for",
             "<p>Every discipline has words that carry a specific, settled meaning inside it, a meaning a general reader would not necessarily guess. Using these words precisely signals that you are writing inside the discipline, not about it from outside.</p>"),
        text("What counts as discipline-specific vocabulary",
             "<p>Dennis and Abbott (2026, pp.131-133) frame the question directly: 'What constitutes discipline-specific vocabulary? Included here are individual words or terms that carry meaning within the disciplinary discourse.' The book follows this with a task extract for you to analyse in the same way, if you have the text to hand.</p>"),
        worked_example("L05",
            "{{learner-a}} avoids a field's own terms entirely, explaining everything in general language, which reads as unfamiliar with the discipline.",
            "{{learner-b}} uses the field's own terms precisely and in the right place, signalling fluency without having to announce it.",
            "Consider two drafts written for the same discipline-specific audience.",
            "Both drafts were accurate. Only {{learner-b}}'s draft read as written by someone inside the field."),
        text("Why precision matters more than volume",
             "<p>Using a discipline's vocabulary does not mean using more jargon. It means using the right term, correctly, exactly where the field itself would use it, and no term where the field would not.</p>"),
        keyTerm("Discipline-specific vocabulary", "noun phrase",
                "Individual words or terms that carry meaning within a disciplinary discourse (Dennis and Abbott, 2026, p.131).",
                "A term can be ordinary outside a field and carry a precise, technical meaning inside it; using it correctly signals membership in that field's discourse.",
                "A term used loosely by a general reader but precisely by a specialist is an example of discipline-specific vocabulary.",
                ["Discourse", "Register", "Criticality"]),
        annotated("A passage, marked for discipline-specific terms",
                  "Select a highlighted term to see why it counts as discipline-specific.",
                  [
                      {"text": "The study's ", "_note": ""},
                      {"text": "construct validity", "_note": "A precise, technical term inside this field; a general reader might read 'validity' alone and miss the specific claim being made."},
                      {"text": " was tested using a ", "_note": ""},
                      {"text": "convergent design", "_note": "A term that names a specific method choice, not just 'the way the study was done'."},
                      {"text": ", which the authors report in detail.", "_note": ""},
                  ]),
        text("Building your own vocabulary",
             "<p>Keep a short list of your own discipline's terms as you meet them, each with the precise meaning it carries inside your field. Try the book's own task extract on pages 132-133 if you have it to hand, checking your reading against it.</p>"),
        opentext(["Name one term from your own discipline that means something different, or more precise, than it does in general use.",
                  "Is there a term you have been using loosely that your discipline actually defines precisely?"]),
    ]
)

write_lesson(
    "draft-lesson_criticality-adv-L06.json", "crit-adv-L06",
    ["Write with authority, aware of how your own stance shapes the argument you are making."],
    [
        text("Authority is not the same as hiding",
             "<p>Many students assume that writing with authority means sounding neutral and keeping themselves out of the text entirely. The opposite is closer to the truth: authority comes from knowing your own stance, not concealing it.</p>"),
        text("Hyland's model of stance",
             "<p>Hyland's (2005) model names four devices writers use to show their stance: hedges (such as 'may suggest'), boosters (such as 'clearly shows'), attitude markers (showing surprise, importance, or agreement), and self-mention (naming yourself as the one making the claim). Marking your stance deliberately, through these four devices, is what turns a flat report into an authoritative argument, building on the synthesis work from earlier in this tier.</p>"),
        worked_example("L06",
            "{{learner-a}} writes a chapter with no hedges, no boosters, and no self-mention, reporting findings as though no judgement went into selecting or weighing them.",
            "{{learner-b}} writes the same chapter, marking a hedge where the evidence is thin, a booster where it is strong, and a sentence naming their own reading explicitly.",
            "Consider two drafts of the same dissertation chapter.",
            "Both drafts covered the same findings. Only {{learner-b}}'s draft showed a stance the reader could actually see."),
        text("Why visible stance reads as more authoritative",
             "<p>A reader who can see where you hedge and where you push a claim harder trusts the places you push harder, precisely because you did not push everywhere equally. Authority comes from that visible, deliberate unevenness, not from a flat tone throughout.</p>"),
        tabs("Hyland's four stance devices",
             "Each device marks your stance in a different way. Select each tab to see an example.",
             "Select each tab to see what each device does.",
             [
                 {"tabTitle": "Hedges", "title": "Hedges",
                  "body": "Words like 'may suggest' or 'appears to' that mark where your claim is less certain. Example: 'This may suggest a wider pattern, though the sample is small.'"},
                 {"tabTitle": "Boosters", "title": "Boosters",
                  "body": "Words like 'clearly' or 'demonstrates' that mark where your claim is strongly supported. Example: 'The results clearly demonstrate a consistent effect.'"},
                 {"tabTitle": "Attitude markers", "title": "Attitude markers",
                  "body": "Words showing surprise, importance, or agreement. Example: 'Surprisingly, none of the three studies controlled for this factor.'"},
                 {"tabTitle": "Self-mention", "title": "Self-mention",
                  "body": "Naming yourself as the one making the claim. Example: 'I read this gap as significant, given what the other three studies found.'"},
             ]),
        checklist("Stance self-check", "Before you submit a chapter or section",
                  "Use these questions to check your stance is visible, not hidden.",
                  ["Did I hedge at least once, where the evidence is genuinely thin?",
                   "Did I boost at least once, where the evidence is genuinely strong?",
                   "Did I mark my own reading explicitly, rather than only reporting findings?",
                   "Would a reader be able to tell which claims I am most confident about?"]),
        text("Carrying this into your synthesis work",
             "<p>Go back to a section you have already synthesised from several sources. Mark one hedge, one booster, and one place for self-mention. The argument does not change; what changes is how visibly it is yours.</p>"),
        opentext(["Find a sentence in your own writing with no hedge, booster, or self-mention at all. Which device would fit it best?",
                  "Is there a claim you have made that deserved a stronger booster than you gave it, or a hedge you left out?"]),
    ]
)

print("Advanced lessons A-1..A-6 written.")
print("All 15 lessons generated.")


