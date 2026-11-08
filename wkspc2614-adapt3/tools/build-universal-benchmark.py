#!/usr/bin/env python3
"""build-universal-benchmark.py - the baseline (universal) sibling dataset.

Reads every per-subject benchmark in catalogue/context/subject/benchmarks/*.json
and distils the shared core across them into one universal-reference.json in the
same folder: what an honours graduate is expected to know, do and be, whatever
the subject. It is the catalogue sibling of the per-subject files and the
grounding a baseline / unscoped context is authored against.

Method (same basis the prose reference ingest-std-qaa-universal-reference-benchmark
flags as `inferred`): a 20-concept / 5-strand keyword rule (reused verbatim from
that reference's run-src/rb_concepts.py) is matched against each statement's
about + paraphrase + verbs + themes. A subject "carries" a concept at a rung when
it has at least one matching statement at that rung. sharedBy counts subjects out
of the whole set (54), per rung and across any rung. The graduate/student wording
(forPractitioner / forBeneficiary) is reused from rb_build.py; no issuer text is
copied.

Run from the repo root (writes JSON + Markdown by default):
    python tools/build-universal-benchmark.py               # JSON + Markdown
    python tools/build-universal-benchmark.py --format yaml  # YAML only
    python tools/build-universal-benchmark.py --format all   # JSON + Markdown + YAML

The JSON is the machine-readable form the resolver and the context-pack flow
consume; the Markdown (universal-reference.md) and YAML siblings are the same
content laid out for a human or an authoring agent to read. Each statement
carries four audience registers: forPractitioner (the graduate standard) with a
nested forEducator (teacher-to-teacher pedagogical guidance), and forBeneficiary
(the student) with a nested forLearnerGuidance (student-facing advice /
clarification). All siblings are written to the same folder.
"""
import argparse, json, glob, os, re, collections, datetime
import pathway_tiers

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_GLOB = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks', '*.json')
OUT = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks', 'universal-reference.json')
OUT_MD = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks', 'universal-reference.md')
OUT_YAML = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks', 'universal-reference.yaml')
VOICE_SPEC = os.path.join(REPO_ROOT, 'reference', 'excelling-voice-specification.md')

# concept: (strand-letter, regex) - reused verbatim from the reference's rb_concepts.py
C = {
 'subject knowledge and understanding': ('K', r'knowledge|understand'),
 'theories, concepts and debates': ('K', r'theor|concept|debate|paradigm'),
 'history, context and currency of the field': ('K', r'histor|context|contemporary|current'),
 'critical evaluation of evidence and arguments': ('C', r'critical|evaluat|assess (the|evidence|argument)|argument'),
 'analysis and problem-solving': ('C', r'analys|problem'),
 'research and enquiry methods': ('A', r'research|enquiry|inquiry|investigat|method'),
 'data, numbers and quantitative reasoning': ('A', r'\bdata\b|quantitative|numer|statistic'),
 'applying knowledge to practice or problems': ('A', r'\bappl(y|ication)|practi(c|s)e|practical'),
 'information and sources': ('A', r'source|literature|information|retriev'),
 'digital skills': ('A', r'digital|software|technolog|computational'),
 'written communication': ('M', r'writ|written|report|essay'),
 'oral or other communication to audiences': ('M', r'communicat|present|audience|oral'),
 'teamwork and collaboration': ('M', r'team|collaborat|group work|others'),
 'independent and self-directed learning': ('R', r'independen|self-direct|autonom|own learning'),
 'reflection and personal development': ('R', r'reflect|personal development|self-aware'),
 'ethics, integrity and values': ('R', r'ethic|integrity|values|responsib'),
 'professional practice and employability': ('R', r'professional|employab|career|workplace|vocational'),
 'equality, diversity and inclusion': ('R', r'diversity|inclusi|equalit|equity'),
 'sustainability': ('R', r'sustainab|environmental'),
 'enterprise and creativity': ('A', r'enterpris|entrepreneur|creativ|innovat'),
}
SN = {'K': 'strand:knowledge', 'C': 'strand:thinking', 'A': 'strand:application',
      'M': 'strand:communication', 'R': 'strand:autonomy'}
# strand -> benchmark domain vocabulary (as used in the per-subject statements[])
DOMAIN = {'K': 'knowledge', 'C': 'generic-skill', 'A': 'generic-skill',
          'M': 'generic-skill', 'R': 'generic-skill'}
# concept: (forPractitioner, forBeneficiary) - reused from rb_build.py
EXP = {
 'subject knowledge and understanding': ("Graduates show broad and well-founded knowledge of the subject's core content.", "You know the core content of your subject well and can show it."),
 'theories, concepts and debates': ("Graduates understand the subject's main theories and concepts and the debates between them.", "You understand the main ideas and theories in your subject and where people disagree about them."),
 'history, context and currency of the field': ("Graduates place the subject in its history and context and know where it currently stands.", "You know how your subject developed, the settings it works in and what is current in it."),
 'critical evaluation of evidence and arguments': ("Graduates evaluate evidence and arguments critically and reach reasoned judgements.", "You weigh up evidence and arguments critically and come to reasoned conclusions."),
 'analysis and problem-solving': ("Graduates analyse problems and work towards solutions using the subject's approaches.", "You break problems down and work out solutions using your subject's methods."),
 'research and enquiry methods': ("Graduates understand and use the subject's methods of research and enquiry.", "You know how research is done in your subject and can carry out an enquiry yourself."),
 'data, numbers and quantitative reasoning': ("Graduates handle data and numbers appropriately for the subject.", "You can work with data and numbers in the way your subject needs."),
 'applying knowledge to practice or problems': ("Graduates apply subject knowledge to practical situations and problems.", "You can use what you know on real problems and in practical settings."),
 'information and sources': ("Graduates find, select and use information and sources appropriate to the subject.", "You can find, choose and use the right sources and information for your subject."),
 'digital skills': ("Graduates use the digital tools and technologies the subject relies on.", "You can use the digital tools your subject depends on."),
 'written communication': ("Graduates write in the forms the subject requires.", "You can write in the forms your subject needs."),
 'oral or other communication to audiences': ("Graduates communicate the subject clearly to different audiences and in different forms.", "You can explain your subject clearly to different audiences, in more than one form."),
 'teamwork and collaboration': ("Graduates work effectively with others.", "You can work well with other people."),
 'independent and self-directed learning': ("Graduates manage their own learning and work independently.", "You can manage your own learning and work on your own."),
 'reflection and personal development': ("Graduates reflect on their learning and practice and plan their development.", "You can reflect on how you learn and work, and plan how to improve."),
 'ethics, integrity and values': ("Graduates recognise and act on the ethical issues and responsibilities of the subject.", "You recognise the ethical questions in your subject and act responsibly."),
 'professional practice and employability': ("Graduates understand the subject's professional settings and are prepared for work.", "You understand how your subject is used at work and are ready for it."),
 'equality, diversity and inclusion': ("Graduates recognise diversity and inclusion as they bear on the subject.", "You understand how diversity and inclusion matter in your subject."),
 'sustainability': ("Graduates understand the subject's bearing on sustainability and the environment.", "You understand how your subject affects sustainability and the environment."),
 'enterprise and creativity': ("Graduates show creativity and enterprise in applying the subject.", "You can be creative and enterprising in how you use your subject."),
}
# concept: agentInstruction - how to realise this expectation in a baseline
# (subject-neutral) pack. Parallels the per-statement agentInstruction psychology
# carries in pathwayMapping. Our words; authoring guidance, not student copy.
EXPINSTR = {
 'subject knowledge and understanding': "Realise as the learner showing well-founded knowledge of their own field's core content. Keep subject-neutral (use 'your subject'); a worked example may use the Student A / Student B cast.",
 'theories, concepts and debates': "Have the learner handle the main ideas, theories and the debates between them, and show that disagreement is normal in a field. Do not import a specific discipline's theories at baseline.",
 'history, context and currency of the field': "Frame as placing the subject in its history and knowing what is current in it. Keep examples generic; do not date-stamp a particular discipline.",
 'critical evaluation of evidence and arguments': "Frame as weighing evidence and arguments to a reasoned judgement. This strand climbs most across tiers: at advanced, push to sustained criticality throughout.",
 'analysis and problem-solving': "Realise as breaking a problem down and working to a solution with the field's methods. Pair with a worked example that shows the steps.",
 'research and enquiry methods': "Frame as knowing how enquiry is done in the field and being able to carry one out: supervised at intermediate, designed and critiqued by the learner at advanced.",
 'data, numbers and quantitative reasoning': "Have the learner work with data and numbers in the way the subject needs; pitch the amount to the pathway, as some carry little quantitative content.",
 'applying knowledge to practice or problems': "Frame as using knowledge on real problems and in practical settings. A good anchor for authentic tasks and reflective prompts.",
 'information and sources': "Realise as finding, choosing and using the right sources and information. Natural fit for the finding-using-sources and referencing pathways.",
 'digital skills': "Frame as using the digital tools the subject relies on. Keep tool-agnostic at baseline; name no specific software.",
 'written communication': "Have the learner write in the forms their work needs. Shared by fewer subjects (threshold 33/54), so treat as supporting unless the pathway is writing-led.",
 'oral or other communication to audiences': "Frame as explaining the subject clearly to different audiences and in more than one form. Core to presenting; supports most pathways.",
 'teamwork and collaboration': "Realise as working well with others. Use lightly unless the pathway is collaboration-led; do not force group work into solo-study topics.",
 'independent and self-directed learning': "Frame as managing one's own learning and working independently. A tier-climb marker: more independence at higher tiers.",
 'reflection and personal development': "Natural anchor for the six-part flow's reflective prompt: reflecting on how one learns and works and planning to improve. Keep questions genuine, with no single right answer.",
 'ethics, integrity and values': "Frame as recognising the ethical questions in the field and acting responsibly. This sits at the threshold (baseline), not as a mark of excellence.",
 'professional practice and employability': "Frame as understanding how the subject is used at work and being ready for it. Keep settings generic at baseline.",
 'equality, diversity and inclusion': "Carry as a cross-cutting value woven through, not a bolt-on topic: how diversity and inclusion bear on the subject. Present inclusively.",
 'sustainability': "Frame as how the subject affects sustainability and the environment. Cross-cutting; weave in rather than teach as a separate unit.",
 'enterprise and creativity': "Frame as being creative and enterprising in applying the subject. Shared by fewer at threshold (23/54); use where the pathway invites it.",
}
# The second layer, student side: concise advice / clarification addressed to the
# learner ("you"), nested under forBeneficiary. Voice Specification register; our
# wording, status drafted, pending SME approval. Clarifies what the expectation
# means in practice and how to tell you are meeting it.
STUDENT_ADVICE = {
 'subject knowledge and understanding': "Knowing your subject is more than recalling facts: you can explain the main ideas in your own words and show how they fit together. A good check is whether you could teach a topic to someone on a different course without reading from your notes.",
 'theories, concepts and debates': "Theories are the tools your subject uses to explain things, and experts often disagree about which tool fits. You are handling this well when you can set out more than one position on a question and say what each gets right, rather than treating the first explanation you meet as the only one.",
 'history, context and currency of the field': "Ideas in your subject came from somewhere and are still changing, so it helps to know how a topic developed and what is current now. You are on track when you can say why a method became standard and point to something recent that is shifting it.",
 'critical evaluation of evidence and arguments': "Do not just report what a source says: ask how it knows it, what it leaves out, and whether the conclusion really follows. You are doing this well when your writing weighs one piece of evidence against another and says which you find stronger and why, instead of listing them all as equally true.",
 'analysis and problem-solving': "Analysis means breaking a problem into parts you can actually work on, then choosing a method and following it through. You can see it working when you show your steps and reasoning, not only the final answer.",
 'research and enquiry methods': "Every subject has its own ways of finding things out, and you are expected to know how yours works and to run a small enquiry yourself. You are doing well when you can say why you chose a method and what its limits are, not just what you found.",
 'data, numbers and quantitative reasoning': "Most subjects ask you to handle some numbers or data, even where yours is not a maths-heavy one. You are on track when you can read a figure or dataset, say what it does and does not show, and use it to support a point rather than decorate one.",
 'applying knowledge to practice or problems': "What you learn is meant to be used, so expect to take ideas from class onto real problems and settings. You can tell it is working when you choose which part of your knowledge a new situation needs, rather than reciting everything you know.",
 'information and sources': "You are expected to find the right sources, judge how good they are, and use them properly. A good sign is that you choose a few strong, relevant sources and show why they are trustworthy, instead of grabbing whatever comes up first.",
 'digital skills': "Your subject relies on particular digital tools, and you are expected to use the ones it depends on competently. You are doing well when you pick the right tool for a task and use it to produce something that meets the subject's standards, not just operate it.",
 'written communication': "You are expected to write in the forms your subject uses, whether that is an essay, a report or something else. You can see it working when your structure and style fit the form and a reader can follow your point without effort.",
 'oral or other communication to audiences': "You are expected to explain your subject clearly to different people and in more than one way, not only in writing. You are on track when you adjust how you present something for the audience in front of you and still keep it accurate.",
 'teamwork and collaboration': "Much of what you will do depends on working well with other people. You can tell it is going well when the group shares the work fairly, handles disagreement openly, and produces something better than any of you would alone.",
 'independent and self-directed learning': "You are expected to manage your own learning: plan your time, find what you need, and keep going without being told each step. A good sign is that you set your own next task and follow it through before a deadline forces you to.",
 'reflection and personal development': "Reflection means looking honestly at how you learn and work so you can plan what to improve. It is working when your reflection names something specific you will do differently, rather than just saying how a task went.",
 'ethics, integrity and values': "Every subject carries ethical questions and expects you to act with integrity. You are meeting this when you can spot the ethical issue in a situation and act responsibly, including being honest about your own work and sources.",
 'professional practice and employability': "Your subject is used in workplaces, and you are expected to understand those settings and be ready for them. You are on track when you can connect what you study to how it is used at work and act in the way the setting expects.",
 'equality, diversity and inclusion': "Diversity and inclusion matter in how your subject is practised and who it serves. You are doing well when you consider whose perspectives are present or missing in your work and present your material inclusively.",
 'sustainability': "Your subject connects to sustainability and the environment in some way, and you are expected to understand how. You are on track when you can point to where your field affects, or is affected by, environmental and social sustainability.",
 'enterprise and creativity': "You are expected to be creative and enterprising in how you use your subject: finding new angles, spotting opportunities and making ideas work. You can see it when you try an original approach and see it through, not just when you have the idea.",
}
# The second layer, tutor side: teacher-to-teacher guidance on the expectation
# itself, nested under forPractitioner. Distinct from agentInstruction (which
# briefs the authoring agent): this explains the pedagogy to another educator -
# the common misconception, how to scaffold, how it climbs. Our wording, drafted.
TUTOR_ADVICE = {
 'subject knowledge and understanding': "Early on, learners equate knowledge with coverage and recall, so they revise lists rather than connections. Build understanding by asking them to link new content to what they already know and to restate ideas in their own words; across the levels the expectation moves from knowing the core to seeing how the parts relate and where the field is unsettled.",
 'theories, concepts and debates': "Students tend to want the 'correct' theory and find open disagreement unsettling, so normalise it: present a live debate and show that reasoned people hold different views. Scaffold with paired contrasts before asking for a judgement, and expect the move from naming theories to weighing them as learners progress.",
 'history, context and currency of the field': "Learners often treat the textbook as timeless and miss that knowledge is dated and contested. Anchor topics to their origins and to a current development or controversy; the expectation deepens from placing ideas in context to tracking where the field currently stands and why.",
 'critical evaluation of evidence and arguments': "Students often hear 'critical' as 'negative', or meet it by summarising more sources. The shift to teach is from description to judgement, so scaffold a visible claim, evidence, so-what move and model your own reasoning aloud before asking for theirs; this strand climbs the most across levels, from tentative judgement to sustained, independent critique.",
 'analysis and problem-solving': "Novices jump to an answer and skip the breakdown, so their errors are hard to locate. Teach a repeatable decomposition (what is given, what is asked, what method fits) and insist on visible working; the expectation grows from applying a given method to selecting and defending one.",
 'research and enquiry methods': "Students often see method as a hoop rather than the thing that makes a claim trustworthy. Teach method alongside the questions it answers, start with supervised enquiry and release responsibility gradually; by the top of the range learners design and critique enquiry, not just carry it out.",
 'data, numbers and quantitative reasoning': "Confidence varies widely and anxiety blocks many capable students, so pitch to the quantitative load your subject actually carries and make the purpose of each technique clear. Scaffold interpretation before calculation; the expectation ranges from reading and using data appropriately to reasoning with it under uncertainty.",
 'applying knowledge to practice or problems': "Transfer is the hard part: students who perform well on set exercises often stall on an unfamiliar real case. Use authentic, slightly messy tasks and ask learners to justify why a given idea applies; the expectation moves from applying knowledge in familiar settings to doing so in current and complex ones.",
 'information and sources': "Students equate searching with a quick web lookup and rarely question authority or relevance. Teach selection and evaluation, not just retrieval, and connect it to referencing and integrity; the expectation deepens from finding suitable sources to using them discerningly within the field's conventions.",
 'digital skills': "Keep this tool-agnostic at baseline and focus on judgement over button-clicking, since specific software dates quickly. Build from guided use to independent choice of tools, and tie digital practice to the subject's real outputs rather than teaching it as a separate skill.",
 'written communication': "Students often transfer one default essay shape to every task, so name the forms your subject actually requires and model each. Give feedback on structure and audience, not only content; this matters most where the pathway is writing-led, and the expectation grows from meeting the form to using it fluently.",
 'oral or other communication to audiences': "Learners tend to present for the marker rather than the audience, and read slides aloud. Give them real audiences and formats and coach adaptation and clarity; the expectation climbs from communicating clearly to tailoring the message and the medium to who is listening.",
 'teamwork and collaboration': "Group work often rewards the willing few and hides free-riding, which sours students on collaboration. Design interdependent roles and assess process as well as product; use this lightly unless the pathway is collaboration-led, and avoid forcing group work onto genuinely solo tasks.",
 'independent and self-directed learning': "Independence has to be taught, not assumed; dropping support too fast leaves weaker students stranded. Release responsibility gradually and make planning and self-monitoring visible; this is a clear tier marker, with more autonomy expected at each level.",
 'reflection and personal development': "Reflection easily becomes description or box-ticking, so students report events instead of learning from them. Prompt with genuine, open questions and value honesty about difficulty; this is the natural anchor for the six-part flow's reflective prompt and should keep questions that have no single right answer.",
 'ethics, integrity and values': "Treat this as threshold, not a mark of excellence: it is the floor every graduate stands on, not a distinction. Use real dilemmas from the field rather than abstract rules, and connect academic integrity to professional conduct so it reads as practice, not policing.",
 'professional practice and employability': "Keep settings generic at baseline and avoid narrowing to one career too early. Bring in authentic professional tasks and norms and let learners rehearse them; the expectation moves from understanding professional settings to operating confidently within them.",
 'equality, diversity and inclusion': "Carry this as a value woven through the subject, not a bolt-on unit, and present it inclusively yourself. Draw out how diversity and inclusion bear on the field's own content and practice; model inclusive examples rather than teaching the topic in isolation.",
 'sustainability': "Like EDI, weave this in rather than teaching it as a separate module, and tie it to the subject's own decisions and impacts. Keep it concrete to the discipline so it reads as relevant, not bolted on; it is cross-cutting across the statements.",
 'enterprise and creativity': "Fewer subjects foreground this at threshold, so use it where the pathway invites it rather than forcing it everywhere. Create space for divergent ideas before converging and reward sensible risk-taking; it pairs naturally with application and professional practice.",
}
# Second-layer advice for the two above-threshold climb statements.
CLIMB_ADVICE = {
 'typical': {
  'learner': "Reaching the typical standard is not about doing extra tasks: it is the same work with more of it critical and independent, and your knowledge wider and more current. Aim to show judgement and initiative across a whole piece, not only in one strong paragraph.",
  'educator': "Frame the step up to typical as more of the same qualities, not new content, so students are not chasing extra coverage. Point feedback at where criticality and independence appear and where they lapse; pitch this to the intermediate tier reading.",
 },
 'excellent': {
  'learner': "At the excellent standard your work is critical and independent throughout and shows some original thinking, so it stands out. Look for the places where you can push a judgement further or bring an idea of your own, rather than playing safe.",
  'educator': "Reserve 'exceptional' framing for sustained criticality and independence with genuine originality, carried across the whole piece rather than in flashes. Help strong students take defensible risks and own their judgements; pitch to the advanced tier reading.",
 },
}


def verb_bands():
    """Section 16 of the voice specification: band name -> outcome verbs.
    Mirrors tools/build-prompt-sets.py's verb_bands() verbatim (the six-line
    regex parser is duplicated by design; the data it reads is not - section
    16 is the one authoritative verb list, per docs/curriculum/
    tier-specification.md section 6, which forbids holding a second one
    here). Read live every build, so drift in section 16 shows up here too."""
    bands = {}
    for line in open(VOICE_SPEC, encoding='utf-8'):
        m = re.match(r'\|\s*\*\*(\w+)\*\*\s*\|.*Outcome verbs:\s*([^|]+?)\.?\s*\|\s*$', line)
        if m:
            bands[m.group(1)] = [v.strip() for v in m.group(2).split(',') if v.strip()]
    return bands


BANDS = verb_bands()
# Default tier -> section 16 band anchor (tier-specification.md section 6).
TIER_BAND_ANCHOR = {'introductory': 'Beginner', 'intermediate': 'Intermediate', 'advanced': 'Advanced'}
BANNED_VAGUE_VERBS = {'understand', 'know', 'appreciate', 'be aware of'}


def _vslot(band, fill, key='verb'):
    """Build a verb-role slot: options are a live subset of BANDS[band] (section
    16), never a hand-typed list. `key` lets a multi-verb statement formula
    give each verb slot its own key (verb_1, verb_2, ...)."""
    return {'key': key, 'role': 'verb', 'fill': fill, 'options': list(BANDS[band]),
            'subjectSupplied': False, 'verbBand': band,
            'verbBandPointer': {'doc': 'reference/excelling-voice-specification.md',
                                 'ref': 'section 16 ' + band + ' band'}}


# Shared grammar for the tokenised formula layer added to tierReadings.rows[]
# and graduate_competency.items[]. Written once at the document's top level
# (`statementFormulas`), read by any agent consuming a formula rather than
# re-deriving the convention per formula. See docs/authoring/
# token-substitution-coupling-and-three-outcome-model.md for the marker
# convention this follows ({single} authoring-time, {{double}} runtime,
# [square] human-visible-unfilled).
STATEMENT_FORMULAS_GRAMMAR = {
    'definition': "A statement formula templates one generic statement so that filling its sourceFill reproduces the live statement byte-for-byte; an outcome formula templates one rule-AL-2-compliant atomic learning outcome (one verb, one object, one condition) generated from inside that statement.",
    'markerConvention': "Single braces {slot} mark an authoring-time fillable slot, machine-filled by template.format(**fill). {{double braces}} are reserved for the runtime merge-context layer and never appear inside a formula template. [square brackets] mark a human-visible unfilled placeholder in rendered prose, not a machine slot.",
    'roles': [
        {'role': 'verb', 'required': True, 'meaning': 'the measurable operation; options drawn live from the section 16 band'},
        {'role': 'object', 'required': True, 'meaning': 'the one thing acted on (rule AL-2: one verb, one object)'},
        {'role': 'condition', 'required': True, 'meaning': 'support, autonomy or context; tier-defining'},
        {'role': 'field_content', 'required': False, 'subjectSupplied': True, 'floor': 'your subject',
         'meaning': "the subject's own matter; the only genuinely subject-specific slot"},
        {'role': 'scope', 'required': False, 'meaning': 'breadth or range of the task'},
        {'role': 'qualifier', 'required': False, 'meaning': 'the rung climb (critical, independent, original)'},
        {'role': 'audience', 'required': False, 'meaning': 'who the output is for'},
        {'role': 'stance', 'required': False, 'meaning': 'identity statements only: the value, ethical or reflexive quality'},
    ],
    'verbBandAnchor': {
        'source': {'doc': 'reference/excelling-voice-specification.md', 'ref': 'section 16'},
        'rule': "Verb options are read live from section 16 at build time, never a second hand-typed list (docs/curriculum/tier-specification.md section 6 forbids holding one here).",
        'defaultAnchor': TIER_BAND_ANCHOR,
    },
    'al2': "Rule AL-2: each outcome formula states one verb, one object and one condition; no 'and' joins two tasks in an outcome template's own fixed text.",
    'bannedVagueVerbs': sorted(BANNED_VAGUE_VERBS),
    'instructions': [
        "Fill subjectSupplied slots (field_content) with the subject itself; every other slot fills from its own options list, never free text.",
        "A statement formula must reproduce its live statement exactly when sourceFill is applied; an outcome formula has no sourceFill and is generated fresh by choosing one option per slot.",
        "Verb slot options are a subset of the section 16 band the formula names; never substitute a verb outside that band, and never use a section 15.8 banned-vague verb (understand, know, appreciate, be aware of) when generating new content.",
        "Reproduce every outcome formula under a statement together when illustrating that statement; dropping one usually understates the tier the statement establishes.",
    ],
}


TIER_READING_FORMULAS = {
 'u-intro': {
  'practice': {
   'template': "Begins to {verb_1} the subject's {object_1} to {scope_1} tasks {condition_1}, {verb_2} with {object_2}, and {verb_3} {object_3} {qualifier_1}.",
   'sourceFill': {'verb_1': 'apply', 'object_1': 'basic methods', 'scope_1': 'familiar, well-defined',
                  'condition_1': 'with guidance', 'verb_2': 'works', 'object_2': 'sources and data they are given',
                  'verb_3': 'communicates', 'object_3': 'straightforward findings', 'qualifier_1': 'clearly'},
   'slots': [
    _vslot('Beginner', 'the operation of using a basic method on a bounded task', key='verb_1'),
    {'key': 'object_1', 'role': 'object', 'fill': 'the method being used',
     'options': ['basic methods', 'foundational techniques', 'set procedures'], 'subjectSupplied': False},
    {'key': 'scope_1', 'role': 'scope', 'fill': 'how bounded the task is at introductory tier',
     'options': ['familiar, well-defined', 'clearly set out', 'straightforward'], 'subjectSupplied': False},
    {'key': 'condition_1', 'role': 'condition', 'fill': 'the support available at introductory tier',
     'options': ['with guidance', 'with a worked model to follow', 'with step-by-step support'], 'subjectSupplied': False},
    _vslot('Beginner', 'the operation of using material already supplied', key='verb_2'),
    {'key': 'object_2', 'role': 'object', 'fill': 'the material worked with',
     'options': ['sources and data they are given', 'material provided to them', 'the sources set for them'], 'subjectSupplied': False},
    _vslot('Beginner', 'the operation of reporting findings', key='verb_3'),
    {'key': 'object_3', 'role': 'object', 'fill': 'what is communicated',
     'options': ['straightforward findings', 'simple results', 'basic conclusions'], 'subjectSupplied': False},
    {'key': 'qualifier_1', 'role': 'qualifier', 'fill': 'the manner of communication expected',
     'options': ['clearly', 'in plain terms', 'so a reader can follow without effort'], 'subjectSupplied': False},
   ],
   'agentInstruction': 'The introductory practice triad: use a basic method on a bounded task with support, work with material already supplied, then report plainly. Keep every verb in the Beginner band; only the connecting structure is fixed. Reproduce all three moves, since dropping one loses the guided, bounded character of this tier.',
   'outcomes': [
    {'id': 'u-intro/practice/o1', 'template': '{verb} the {object} suited to a {scope} task in {field_content}, {condition}.',
     'slots': [
      _vslot('Beginner', 'a Beginner-band verb for naming or recognising the right method, not performing it unsupervised'),
      {'key': 'object', 'role': 'object', 'fill': 'the method being selected',
       'options': ['basic method', 'set procedure', 'introductory technique'], 'subjectSupplied': False},
      {'key': 'scope', 'role': 'scope', 'fill': 'how bounded the task is',
       'options': ['familiar, well-defined', 'clearly set out', 'straightforward'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain",
       'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'the support available at this tier',
       'options': ['with guidance', 'with a worked model to follow', 'with step-by-step support'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself and keep the verb in the Beginner band naming or recognising the method, not performing it unsupervised. The condition slot carries the guided character of this tier, so do not drop it or imply the learner works alone.'},
    {'id': 'u-intro/practice/o2', 'template': '{verb} the {object} you have been given in {field_content}, {condition}.',
     'slots': [
      _vslot('Beginner', 'a Beginner-band verb for recognising or describing material already provided'),
      {'key': 'object', 'role': 'object', 'fill': 'the material worked with',
       'options': ['sources and data', 'material provided', 'given evidence'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain",
       'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'the support available at this tier',
       'options': ['with guidance', 'when prompted', 'with support'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. The verb must denote recognising or describing material already given, not collecting or generating it, since that independence belongs to a later tier. Keep the condition slot to signal the guidance still expected here.'},
    {'id': 'u-intro/practice/o3', 'template': '{verb} {object} about {field_content} {qualifier}, {condition}.',
     'slots': [
      _vslot('Beginner', 'a Beginner-band verb for stating or setting out findings plainly'),
      {'key': 'object', 'role': 'object', 'fill': 'what is communicated',
       'options': ['straightforward findings', 'simple results', 'basic conclusions'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain",
       'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'qualifier', 'role': 'qualifier', 'fill': 'the manner of communication expected',
       'options': ['clearly', 'in plain terms', 'so a reader can follow without effort'], 'subjectSupplied': False},
      {'key': 'condition', 'role': 'condition', 'fill': 'the support available at this tier',
       'options': ['with guidance', 'with feedback on structure', 'when prompted to check clarity'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. Keep the verb plain and Beginner-band: stating or setting out findings, not interpreting them. The qualifier slot carries the plainness this tier expects; do not let it drift into a more technical register.'},
   ],
  },
  'knowledge': {
   'template': "{verb_1} the {object_1} that introduce the subject, and can {verb_2} them in the {scope_1} field.",
   'sourceFill': {'verb_1': 'Knows', 'object_1': 'core terms, ideas and principles', 'verb_2': 'place', 'scope_1': 'wider'},
   'slots': [
    {'key': 'verb_1', 'role': 'verb', 'fill': 'the operation of holding core terms (sourceFill keeps the live, vague verb; options stay clean)',
     'options': list(BANDS['Beginner']), 'subjectSupplied': False, 'verbBand': 'Beginner',
     'verbBandPointer': {'doc': 'reference/excelling-voice-specification.md', 'ref': 'section 16 Beginner band'}},
    {'key': 'object_1', 'role': 'object', 'fill': 'the core terms, ideas and principles',
     'options': ['core terms, ideas and principles', 'key definitions and principles', 'foundational terms and ideas'], 'subjectSupplied': False},
    _vslot('Beginner', 'the operation of connecting a term to its wider context', key='verb_2'),
    {'key': 'scope_1', 'role': 'scope', 'fill': 'how wide the field being connected to is',
     'options': ['wider', 'broader', 'surrounding'], 'subjectSupplied': False},
   ],
   'agentInstruction': 'The introductory knowledge pair names the core terms, then places them in context. sourceFill preserves the live statement\'s "Knows", a banned §15.8 verb, but the slot options stay clean Beginner-band verbs: nothing generated from this formula should repeat that vagueness.',
   'outcomes': [
    {'id': 'u-intro/knowledge/o1', 'template': '{verb} the {object} that introduce {field_content}, {condition}.',
     'slots': [
      _vslot('Beginner', 'a Beginner-band verb for naming or defining core terms, not merely knowing them'),
      {'key': 'object', 'role': 'object', 'fill': 'the core terms, ideas and principles',
       'options': ['core terms, ideas and principles', 'key definitions and principles', 'foundational terms and ideas'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain",
       'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'how independently the terms are stated',
       'options': ['in your own words', 'with guidance', 'when asked to explain them'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. Keep the verb a Beginner-band naming or defining operation, never the live statement\'s "knows". The condition slot should reward restating in the learner\'s own words, not verbatim recall.'},
    {'id': 'u-intro/knowledge/o2', 'template': '{verb} how {object} relates to the {scope} field, {condition}.',
     'slots': [
      _vslot('Beginner', 'a Beginner-band verb for connecting a term to its wider context'),
      {'key': 'object', 'role': 'object', 'fill': 'a single core idea being connected outward',
       'options': ['a core idea', 'a key principle', 'a basic concept'], 'subjectSupplied': False},
      {'key': 'scope', 'role': 'scope', 'fill': 'how wide the connection reaches',
       'options': ['wider', 'broader', 'surrounding'], 'subjectSupplied': False},
      {'key': 'condition', 'role': 'condition', 'fill': 'the support available for making the connection',
       'options': ['with guidance', 'using a simple example', 'when prompted'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Keep object singular so it agrees with "relates"; field_content is not needed here since the object itself already names the subject-neutral idea. The verb must connect the idea outward, not merely restate it in isolation.'},
   ],
  },
  'identity': {
   'template': "Begins to {verb_1} {object_1} for the first time, following {condition_1} on {object_2} as an early sense of the kind of {audience_1} they are becoming.",
   'sourceFill': {'verb_1': 'connect', 'object_1': 'practice, theory and reflection', 'condition_1': 'guidance',
                  'object_2': 'ethical and academic conduct', 'audience_1': 'practitioner'},
   'slots': [
    _vslot('Beginner', 'the operation of linking practice, theory and reflection together', key='verb_1'),
    {'key': 'object_1', 'role': 'object', 'fill': 'what is being linked for the first time',
     'options': ['practice, theory and reflection', 'what you do, what you are taught, and how you reflect on it', 'practical work and course theory'], 'subjectSupplied': False},
    {'key': 'condition_1', 'role': 'condition', 'fill': 'the support given for ethical/academic conduct',
     'options': ['guidance', 'a set of rules to follow', 'a tutor\'s steer'], 'subjectSupplied': False},
    {'key': 'object_2', 'role': 'object', 'fill': 'the conduct being guided',
     'options': ['ethical and academic conduct', 'academic integrity', 'professional conduct'], 'subjectSupplied': False},
    {'key': 'audience_1', 'role': 'audience', 'fill': 'the identity being formed',
     'options': ['practitioner', 'professional', 'graduate in the subject'], 'subjectSupplied': False},
   ],
   'agentInstruction': 'The introductory identity statement links practice, theory and reflection for the first time under guidance on conduct. Two object slots are deliberate (the thing linked, and the conduct guided); keep both, since dropping either loses either the triad or the ethical framing.',
   'outcomes': [
    {'id': 'u-intro/identity/o1', 'template': '{verb} {object} for the first time, {condition}.',
     'slots': [
      _vslot('Beginner', 'a Beginner-band verb for linking practice, theory and reflection together'),
      {'key': 'object', 'role': 'object', 'fill': 'what is being linked',
       'options': ['practice, theory and reflection', 'what you do and what you are taught', 'practical work and course theory'], 'subjectSupplied': False},
      {'key': 'condition', 'role': 'condition', 'fill': 'the support given for making the link',
       'options': ['with guidance', 'following a set structure', 'with a model to follow'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Keep the verb a Beginner-band connecting operation: the point is linking elements the learner has not yet connected, not recalling any one of them alone. No field_content slot is needed, since the link itself is the generic content.'},
    {'id': 'u-intro/identity/o2', 'template': '{verb} {object} as an early sense of the kind of {audience} you are becoming, {condition}.',
     'slots': [
      _vslot('Beginner', 'a Beginner-band verb for recognising or following expected conduct'),
      {'key': 'object', 'role': 'object', 'fill': 'the conduct expected',
       'options': ['the conduct expected of you', 'guidance on ethical and academic conduct', 'basic ethical and academic expectations'], 'subjectSupplied': False},
      {'key': 'audience', 'role': 'audience', 'fill': 'the identity being formed',
       'options': ['practitioner', 'professional', 'graduate in your subject'], 'subjectSupplied': False},
      {'key': 'condition', 'role': 'condition', 'fill': 'the support given',
       'options': ['with guidance', 'when advised by a tutor', 'following the rules you are given'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Keep the verb Beginner-band and about recognising or following, not internalising unsupervised: that independence belongs to later tiers. The audience slot names the identity still forming, so do not harden it into a fixed professional label.'},
   ],
  },
 },
 'u-int': {
  'practice': {
   'template': "{verb_1} the subject's {object_1} to {object_2}, {verb_2} {condition_1} {object_3}, {verb_3} with {object_4}, and {verb_4} {object_5} to {audience_1}.",
   'sourceFill': {'verb_1': 'Applies', 'object_1': 'methods', 'object_2': 'questions and problems',
                  'verb_2': 'carries out', 'condition_1': 'supervised', 'object_3': 'research and enquiry',
                  'verb_3': 'works', 'object_4': 'data and sources', 'verb_4': 'communicates',
                  'object_5': 'findings', 'audience_1': 'different audiences'},
   'slots': [
    _vslot('Intermediate', 'the operation of using a method on a new question', key='verb_1'),
    {'key': 'object_1', 'role': 'object', 'fill': "the subject's methods", 'options': ['methods', 'approaches', 'techniques'], 'subjectSupplied': False},
    {'key': 'object_2', 'role': 'object', 'fill': 'what the methods are used on', 'options': ['questions and problems', 'new problems', 'unfamiliar questions'], 'subjectSupplied': False},
    _vslot('Intermediate', 'the operation of carrying out an enquiry', key='verb_2'),
    {'key': 'condition_1', 'role': 'condition', 'fill': 'the level of supervision', 'options': ['supervised', 'tutor-checked', 'guided'], 'subjectSupplied': False},
    {'key': 'object_3', 'role': 'object', 'fill': 'the enquiry carried out', 'options': ['research and enquiry', 'a small investigation', 'an enquiry into a question'], 'subjectSupplied': False},
    _vslot('Intermediate', 'the operation of examining data and sources', key='verb_3'),
    {'key': 'object_4', 'role': 'object', 'fill': 'what is examined', 'options': ['data and sources', 'evidence and sources', 'a dataset and its sources'], 'subjectSupplied': False},
    _vslot('Intermediate', 'the operation of adapting findings to an audience', key='verb_4'),
    {'key': 'object_5', 'role': 'object', 'fill': 'what is communicated', 'options': ['findings', 'results', 'conclusions'], 'subjectSupplied': False},
    {'key': 'audience_1', 'role': 'audience', 'fill': 'who findings are adapted for', 'options': ['different audiences', 'more than one audience', 'an audience outside the subject'], 'subjectSupplied': False},
   ],
   'agentInstruction': 'The intermediate practice quartet: apply methods to new problems, run a supervised enquiry, examine data and sources, then adapt findings outward. Keep all four verbs Intermediate-band. Reproduce all four moves together, since any one alone understates the tier\'s range.',
   'outcomes': [
    {'id': 'u-int/practice/o1', 'template': '{verb} {object} to address {scope} in {field_content}, {condition}.',
     'slots': [
      _vslot('Intermediate', 'an Intermediate-band verb for using a method on a new question or problem'),
      {'key': 'object', 'role': 'object', 'fill': 'the method chosen', 'options': ["the subject's methods", 'an appropriate method', 'a chosen technique'], 'subjectSupplied': False},
      {'key': 'scope', 'role': 'scope', 'fill': 'the kind of problem addressed', 'options': ['a question or problem', 'an unfamiliar problem', 'a new question'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'the autonomy expected at this tier', 'options': ['independently', 'with reduced support', 'without being told which method to use'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. Keep the verb Intermediate-band and the condition genuinely independent, since reduced scaffolding is what separates this tier from introductory. The object names the method, not the problem.'},
    {'id': 'u-int/practice/o2', 'template': '{verb} the design of {object} in {field_content}, {condition}.',
     'slots': [
      _vslot('Intermediate', 'an Intermediate-band verb for examining the design of an enquiry'),
      {'key': 'object', 'role': 'object', 'fill': 'the enquiry being examined', 'options': ['a small research enquiry', 'a piece of research', 'an investigation into a question'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'the level of supervision at this tier', 'options': ['under supervision', 'with a tutor checking your design', 'following an agreed method'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. Supervised is the point at this tier, unlike the unsupervised design expected later, so keep the condition slot explicitly supervised rather than independent.'},
    {'id': 'u-int/practice/o3', 'template': '{verb} the {object} in {field_content}, {condition}.',
     'slots': [
      _vslot('Intermediate', 'an Intermediate-band verb for examining data and sources, not just collecting them'),
      {'key': 'object', 'role': 'object', 'fill': 'what is examined', 'options': ['data and sources you work with', 'evidence available to you', 'a dataset or set of sources'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'the autonomy expected', 'options': ['independently', 'with some supervision', 'once sources are identified'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. The verb must denote examining the material, not merely gathering it; gathering sits at introductory. Keep exactly one condition slot carrying the tier\'s autonomy.'},
    {'id': 'u-int/practice/o4', 'template': '{verb} {object} for {audience}, {condition}.',
     'slots': [
      _vslot('Intermediate', 'an Intermediate-band verb for adapting findings to a specific audience'),
      {'key': 'object', 'role': 'object', 'fill': 'what is communicated', 'options': ['your findings', 'what you have found', 'your results'], 'subjectSupplied': False},
      {'key': 'audience', 'role': 'audience', 'fill': 'who the communication is adapted for', 'options': ['a different audience', 'more than one kind of audience', 'an audience outside your subject'], 'subjectSupplied': False},
      {'key': 'condition', 'role': 'condition', 'fill': 'how the adaptation is carried out', 'options': ['adjusting the level of detail', 'without changing the substance', 'in more than one format'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'The object is the findings, the audience slot is who they are adapted for; keep both distinct roles rather than collapsing them. The condition slot should protect accuracy while varying form, not loosen the claim itself.'},
   ],
  },
  'knowledge': {
   'template': "{verb_1} the {object_1} of the subject, and how the field {verb_2} and where it currently {verb_3}.",
   'sourceFill': {'verb_1': 'Knows', 'object_1': 'core content, main theories and debates', 'verb_2': 'developed', 'verb_3': 'stands'},
   'slots': [
    {'key': 'verb_1', 'role': 'verb', 'fill': 'the operation of holding core content (sourceFill keeps the live, vague verb; options stay clean)',
     'options': list(BANDS['Intermediate']), 'subjectSupplied': False, 'verbBand': 'Intermediate',
     'verbBandPointer': {'doc': 'reference/excelling-voice-specification.md', 'ref': 'section 16 Intermediate band'}},
    {'key': 'object_1', 'role': 'object', 'fill': 'the main content, theories and debates',
     'options': ['core content, main theories and debates', 'main theories and the debates between them', 'theories and the debates between them'], 'subjectSupplied': False},
    _vslot('Intermediate', 'the operation of tracing how the field developed', key='verb_2'),
    _vslot('Intermediate', 'the operation of locating where the field currently stands', key='verb_3'),
   ],
   'agentInstruction': 'The intermediate knowledge triple states the content, then its history, then its current standing. sourceFill preserves the live "Knows"; the clean verb options must never repeat it, so anything generated stays §15.8-compliant.',
   'outcomes': [
    {'id': 'u-int/knowledge/o1', 'template': '{verb} the {object} of {field_content}, {condition}.',
     'slots': [
      _vslot('Intermediate', 'an Intermediate-band verb for weighing core theories and debates, not just knowing them'),
      {'key': 'object', 'role': 'object', 'fill': 'the theories and debates', 'options': ['main theories and debates', 'core content and main theories', 'theories and the debates between them'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'how the comparison is carried out', 'options': ['comparing more than one position', 'with reference to current debate', 'without relying on one single source'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. Keep the verb Intermediate-band and genuinely comparative: the point is weighing positions against each other, not reciting one theory at a time.'},
    {'id': 'u-int/knowledge/o2', 'template': "{verb} {field_content}'s {object}, {condition}.",
     'slots': [
      _vslot('Intermediate', 'an Intermediate-band verb for tracing development and current standing as one bundled object'),
      {'key': 'object', 'role': 'object', 'fill': 'the development and current standing of the field, as a single bundled object',
       'options': ['development and current standing', 'history and present state', 'trajectory and current position'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'the evidence base for the claim', 'options': ['drawing on more than one source', 'with reference to a recent development', "using evidence of its history"], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. Keep development and current standing bundled as one object rather than as two coordinate clauses joined by "and", since splitting them back into separate verb-bearing halves reintroduces the AL-2 violation this design avoids.'},
   ],
  },
  'identity': {
   'template': "{verb_1} {qualifier_1} and increasingly {condition_1}, treating {audience_1} identity as still {qualifier_2} rather than fixed, shaped by {object_1} on their own learning and by how {object_2} bear on the subject.",
   'sourceFill': {'verb_1': 'Works', 'qualifier_1': 'ethically', 'condition_1': 'independently',
                  'audience_1': 'practitioner', 'qualifier_2': 'forming', 'object_1': 'reflection',
                  'object_2': 'diversity, sustainability and professional practice'},
   'slots': [
    _vslot('Intermediate', 'the operation of conducting oneself', key='verb_1'),
    {'key': 'qualifier_1', 'role': 'qualifier', 'fill': 'the ethical manner of working', 'options': ['ethically', 'responsibly', 'with integrity'], 'subjectSupplied': False},
    {'key': 'condition_1', 'role': 'condition', 'fill': 'the autonomy expected', 'options': ['independently', 'with reduced support', 'managing their own time'], 'subjectSupplied': False},
    {'key': 'audience_1', 'role': 'audience', 'fill': 'whose identity is still forming', 'options': ['practitioner', 'professional', 'graduate'], 'subjectSupplied': False},
    {'key': 'qualifier_2', 'role': 'qualifier', 'fill': 'the state of that identity', 'options': ['forming', 'taking shape', 'not yet settled'], 'subjectSupplied': False},
    {'key': 'object_1', 'role': 'object', 'fill': 'what shapes the identity from within', 'options': ['reflection', 'reflection on their own learning', 'their own self-assessment'], 'subjectSupplied': False},
    {'key': 'object_2', 'role': 'object', 'fill': 'what shapes the identity from the cross-cutting themes', 'options': ['diversity, sustainability and professional practice', 'equality, diversity and sustainability', 'professional practice, diversity and sustainability'], 'subjectSupplied': False},
   ],
   'agentInstruction': 'The intermediate identity statement holds three forces at once: ethical, increasingly independent conduct; identity as still forming; and the cross-cutting themes bearing on it. Keep all three in any reproduction, since dropping the cross-cutting clause loses the EDI/sustainability link entirely.',
   'outcomes': [
    {'id': 'u-int/identity/o1', 'template': '{verb} the {object} that arise in {field_content}, {condition}.',
     'slots': [
      _vslot('Intermediate', 'an Intermediate-band verb for examining ethical questions as they arise'),
      {'key': 'object', 'role': 'object', 'fill': 'the ethical questions encountered', 'options': ['the ethical questions that arise', 'the ethical implications of a choice', 'the ethical issues you meet'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'the autonomy expected', 'options': ['with increasing independence', 'without being told each step', 'managing your own time'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. The verb must denote examining the ethical question, not just recognising that one exists, since recognition alone belongs to the introductory tier.'},
    {'id': 'u-int/identity/o2', 'template': '{verb} your own {object} as {qualifier} rather than fixed, {condition}.',
     'slots': [
      _vslot('Intermediate', 'an Intermediate-band verb for examining a developing sense of practitioner identity'),
      {'key': 'object', 'role': 'object', 'fill': 'the identity being examined', 'options': ['sense of practitioner identity', 'developing identity as a practitioner', 'emerging professional identity'], 'subjectSupplied': False},
      {'key': 'qualifier', 'role': 'qualifier', 'fill': 'the open state of that identity', 'options': ['still forming', 'still taking shape', 'not yet settled'], 'subjectSupplied': False},
      {'key': 'condition', 'role': 'condition', 'fill': 'what drives the change', 'options': ['through reflection on your own learning', 'as you gain more experience', 'in light of feedback you receive'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Keep the qualifier open rather than settled; this outcome exists to stop a learner treating their professional identity as already fixed. The condition slot should name what is driving the change, not just assert that it is happening.'},
    {'id': 'u-int/identity/o3', 'template': '{verb} how {object} bear on {field_content}, {condition}.',
     'slots': [
      _vslot('Intermediate', 'an Intermediate-band verb for examining how cross-cutting themes bear on the subject'),
      {'key': 'object', 'role': 'object', 'fill': 'the cross-cutting themes', 'options': ['diversity, sustainability and professional practice', 'equality, diversity and sustainability', 'professional practice, diversity and sustainability'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'how concretely the claim is grounded', 'options': ['drawing on a specific example', 'with reference to your own practice', 'as part of your reflection'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. Keep all three named themes together in the object rather than splitting into separate outcomes, since the live statement treats them as one bundle bearing on the subject.'},
   ],
  },
 },
 'u-adv': {
  'practice': {
   'template': "{verb_1} and {verb_2} {object_1} across {scope_1}, {verb_3} {object_2} {qualifier_1} throughout, and {verb_4} knowledge to {qualifier_2} problems with some {qualifier_3}.",
   'sourceFill': {'verb_1': 'Designs', 'verb_2': 'critiques', 'object_1': 'enquiry', 'scope_1': 'methods',
                  'verb_3': 'evaluates', 'object_2': 'evidence and arguments', 'qualifier_1': 'critically',
                  'verb_4': 'applies', 'qualifier_2': 'current and complex', 'qualifier_3': 'originality'},
   'slots': [
    _vslot('Advanced', 'the operation of designing an enquiry', key='verb_1'),
    _vslot('Advanced', 'the operation of critiquing that same enquiry', key='verb_2'),
    {'key': 'object_1', 'role': 'object', 'fill': 'what is designed and critiqued', 'options': ['enquiry', 'a piece of research', 'an investigation'], 'subjectSupplied': False},
    {'key': 'scope_1', 'role': 'scope', 'fill': 'the range of methods in play', 'options': ['methods', 'competing methods', 'more than one method'], 'subjectSupplied': False},
    _vslot('Advanced', 'the operation of weighing evidence and arguments', key='verb_3'),
    {'key': 'object_2', 'role': 'object', 'fill': 'what is weighed', 'options': ['evidence and arguments', 'competing claims', 'the evidence available'], 'subjectSupplied': False},
    {'key': 'qualifier_1', 'role': 'qualifier', 'fill': 'the manner of the weighing', 'options': ['critically', 'rigorously', 'without default agreement'], 'subjectSupplied': False},
    _vslot('Advanced', 'the operation of applying knowledge to a complex problem', key='verb_4'),
    {'key': 'qualifier_2', 'role': 'qualifier', 'fill': 'the kind of problem addressed', 'options': ['current and complex', 'novel and complex', 'unfamiliar and open-ended'], 'subjectSupplied': False},
    {'key': 'qualifier_3', 'role': 'qualifier', 'fill': 'the originality expected', 'options': ['originality', 'independent thinking', 'a genuinely own idea'], 'subjectSupplied': False},
   ],
   'agentInstruction': 'The advanced practice triad: design and critique enquiry across methods, evaluate evidence throughout, apply knowledge with originality. All four verbs are Advanced-band. Reproduce the full triad, since any one move alone understates sustained criticality.',
   'outcomes': [
    {'id': 'u-adv/practice/o1', 'template': '{verb} {object} across {scope}, {condition}.',
     'slots': [
      _vslot('Advanced', 'an Advanced-band verb for critically examining the choice of method itself'),
      {'key': 'object', 'role': 'object', 'fill': 'the enquiry being designed', 'options': ['the design of an enquiry', 'your choice of method', 'the enquiry you design'], 'subjectSupplied': False},
      {'key': 'scope', 'role': 'scope', 'fill': 'the range of methods considered', 'options': ['more than one method', 'competing methods', 'the methods available to you'], 'subjectSupplied': False},
      {'key': 'condition', 'role': 'condition', 'fill': 'the justification expected', 'options': ['justifying the choice you make', 'without being told which to use', 'before you carry it out'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Keep the verb Advanced-band and aimed at the choice of method itself, not just its execution. The condition slot should require explicit justification, since unexamined method choice is the introductory-tier failure mode this outcome rules out.'},
    {'id': 'u-adv/practice/o2', 'template': '{verb} {object} {qualifier} throughout {field_content}, {condition}.',
     'slots': [
      _vslot('Advanced', 'an Advanced-band verb for weighing evidence and arguments to a judgement'),
      {'key': 'object', 'role': 'object', 'fill': 'what is weighed', 'options': ['evidence and arguments', 'the evidence you encounter', 'competing arguments'], 'subjectSupplied': False},
      {'key': 'qualifier', 'role': 'qualifier', 'fill': 'the sustained manner of the weighing', 'options': ['with sustained rigour', 'consistently', 'without lapsing into summary'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'the outcome of the weighing', 'options': ['reaching a reasoned judgement', 'without default agreement', 'sustained through a whole piece of work'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. The qualifier must mark sustained criticality throughout a whole piece of work, not a single strong paragraph, which is the specific advanced-tier demand this outcome encodes.'},
    {'id': 'u-adv/practice/o3', 'template': '{verb} how {object} applies to {qualifier} problems in {field_content}, {condition}.',
     'slots': [
      _vslot('Advanced', 'an Advanced-band verb for building an original response to a complex problem'),
      {'key': 'object', 'role': 'object', 'fill': 'what is applied', 'options': ['your knowledge', 'what you know', 'your understanding'], 'subjectSupplied': False},
      {'key': 'qualifier', 'role': 'qualifier', 'fill': 'the kind of problem addressed', 'options': ['current and complex', 'novel and complex', 'unfamiliar and open-ended'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'the originality expected', 'options': ['with some originality', 'bringing an idea of your own', 'without a settled procedure to follow'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. The condition slot carries the originality this tier expects; do not soften it to mere competent application, which belongs to the intermediate tier.'},
   ],
  },
  'knowledge': {
   'template': "{verb_1} the {object_1} of the subject, its {object_2} and their bearing on {object_3}, and {verb_2} where {object_4} runs out.",
   'sourceFill': {'verb_1': 'Commands', 'object_1': 'breadth and depth', 'object_2': 'theoretical foundations',
                  'object_3': 'current thinking', 'verb_2': 'sees', 'object_4': 'understanding'},
   'slots': [
    {'key': 'verb_1', 'role': 'verb', 'fill': 'the operation of holding the breadth and depth of the subject (sourceFill keeps the live, vague verb; options stay clean)',
     'options': list(BANDS['Advanced']), 'subjectSupplied': False, 'verbBand': 'Advanced',
     'verbBandPointer': {'doc': 'reference/excelling-voice-specification.md', 'ref': 'section 16 Advanced band'}},
    {'key': 'object_1', 'role': 'object', 'fill': 'the breadth and depth held', 'options': ['breadth and depth', 'the full range and depth', 'scope and depth'], 'subjectSupplied': False},
    {'key': 'object_2', 'role': 'object', 'fill': 'the theoretical foundations', 'options': ['theoretical foundations', 'theoretical base', "foundational theory"], 'subjectSupplied': False},
    {'key': 'object_3', 'role': 'object', 'fill': 'what the foundations bear on', 'options': ['current thinking', 'contemporary debate', 'where the field is heading'], 'subjectSupplied': False},
    _vslot('Advanced', 'the operation of locating the limits of understanding', key='verb_2'),
    {'key': 'object_4', 'role': 'object', 'fill': 'what runs out', 'options': ['understanding', 'established theory', "the field's current knowledge"], 'subjectSupplied': False},
   ],
   'agentInstruction': 'The advanced knowledge pair holds command of the field together with knowing its limits. sourceFill preserves the live "Commands"; the clean verb options stay Advanced-band and never repeat that vagueness, so anything generated is observable, not a claim of mastery.',
   'outcomes': [
    {'id': 'u-adv/knowledge/o1', 'template': '{verb} how {object} bears on {scope}, {condition}.',
     'slots': [
      _vslot('Advanced', 'an Advanced-band verb for weighing the bearing of theoretical foundations on current thinking'),
      {'key': 'object', 'role': 'object', 'fill': "the subject's theoretical base", 'options': ['the breadth and depth of your subject', "your subject's theoretical foundations", 'the foundations of your field'], 'subjectSupplied': False},
      {'key': 'scope', 'role': 'scope', 'fill': 'what the foundations bear on', 'options': ['current thinking', 'contemporary debate', 'where the field is heading'], 'subjectSupplied': False},
      {'key': 'condition', 'role': 'condition', 'fill': 'how the limits of the claim are handled', 'options': ['identifying where understanding runs out', 'without overstating certainty', 'pointing to open questions'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'The object already names the subject, so no separate field_content slot is needed. Keep the condition slot explicit about the limits of understanding; this outcome fails if it reads as unqualified mastery.'},
    {'id': 'u-adv/knowledge/o2', 'template': '{verb} where {object} in {field_content} runs out, {condition}.',
     'slots': [
      _vslot('Advanced', 'an Advanced-band verb for locating the limits of current understanding'),
      {'key': 'object', 'role': 'object', 'fill': 'what is examined for its limits', 'options': ['current understanding', 'established theory', "the field's current knowledge"], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'how the limit is framed', 'options': ['without overstating what is known', 'pointing to what remains open', 'distinguishing it from what is well established'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject itself. This outcome is the direct AL-2 atom of "sees where understanding runs out": keep it distinct from o1, which is about the bearing on current thinking, not the limit itself.'},
   ],
  },
  'identity': {
   'template': "A {stance} practitioner who {verb_1} how their own {object_1} shape their {object_2}, {verb_2} what this means for {audience_1} and for {audience_2} acting on it, and {verb_3} their {object_3} as still {qualifier} through that scrutiny.",
   'sourceFill': {'stance': 'reflexive', 'verb_1': 'examines', 'object_1': 'position, assumptions and values',
                  'object_2': 'judgements', 'verb_2': 'weighs', 'audience_1': 'wider debate',
                  'audience_2': 'audiences', 'verb_3': 'treats', 'object_3': 'professional identity',
                  'qualifier': 'evolving'},
   'slots': [
    {'key': 'stance', 'role': 'stance', 'fill': 'the reflexive, ethical quality of the practitioner', 'options': ['reflexive', 'self-critical', 'self-aware'], 'subjectSupplied': False},
    _vslot('Advanced', 'the operation of self-examination', key='verb_1'),
    {'key': 'object_1', 'role': 'object', 'fill': 'what is examined in oneself', 'options': ['position, assumptions and values', 'standpoint and commitments', 'frame of reference', 'prior beliefs'], 'subjectSupplied': False},
    {'key': 'object_2', 'role': 'object', 'fill': 'what the examined position shapes', 'options': ['judgements', 'conclusions', 'interpretations'], 'subjectSupplied': False},
    _vslot('Advanced', 'the operation of judging outward implications', key='verb_2'),
    {'key': 'audience_1', 'role': 'audience', 'fill': 'the first outward audience', 'options': ['wider debate', 'wider debate in the field', 'the field as a whole'], 'subjectSupplied': False},
    {'key': 'audience_2', 'role': 'audience', 'fill': 'the second outward audience', 'options': ['audiences', 'other practitioners', 'those who act on the conclusions'], 'subjectSupplied': False},
    _vslot('Advanced', 'the operation of holding identity open to revision', key='verb_3'),
    {'key': 'object_3', 'role': 'object', 'fill': 'the identity held open', 'options': ['professional identity', 'sense of practice', 'standpoint as a practitioner'], 'subjectSupplied': False},
    {'key': 'qualifier', 'role': 'qualifier', 'fill': 'the open, unsettled state of that identity', 'options': ['evolving', 'still open', 'unsettled'], 'subjectSupplied': False},
   ],
   'agentInstruction': 'The advanced identity triad: examine your own position, weigh what it means outward, then hold identity open. Fill stance and qualifier from the options to keep the reflexive register; only field_content-bearing outcomes take subject context. Reproduce all three outcomes or none, since dropping the third collapses identity back into reflection.',
   'outcomes': [
    {'id': 'u-adv/identity/o1', 'template': '{verb} how your own {object} shape the judgements you make in {field_content}, {condition}.',
     'slots': [
      _vslot('Advanced', 'an Advanced-band verb denoting active self-examination, not passive awareness'),
      {'key': 'object', 'role': 'object', 'fill': 'what is being examined in oneself', 'options': ['position, assumptions and values', 'standpoint and commitments', 'frame of reference', 'prior beliefs'], 'subjectSupplied': False},
      {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain of judgement", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
      {'key': 'condition', 'role': 'condition', 'fill': 'the autonomy expected at advanced tier', 'options': ['without prompting', 'across a sustained piece of work', 'independently'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Fill field_content with the subject\'s own domain of judgement and keep the verb in the Advanced band. Do not weaken the reflexive claim: the verb must denote active self-examination, not noticing or being aware. The condition slot carries the tier, so do not soften it when the subject is vocational.'},
    {'id': 'u-adv/identity/o2', 'template': '{verb} what your {object} mean for {audience}, {condition}.',
     'slots': [
      _vslot('Advanced', 'an Advanced-band verb for judging the outward implications of your own position'),
      {'key': 'object', 'role': 'object', 'fill': 'the plural output of one\'s own judgement', 'options': ['judgements', 'conclusions', 'interpretations'], 'subjectSupplied': False},
      {'key': 'audience', 'role': 'audience', 'fill': 'who the implications reach', 'options': ['wider debate in your subject', 'other practitioners', 'those who act on your conclusions'], 'subjectSupplied': False},
      {'key': 'condition', 'role': 'condition', 'fill': 'the autonomy expected', 'options': ['without prompting', 'across a sustained piece of work', 'independently'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'Keep object plural to agree with "mean". This outcome is distinct from o1: o1 looks inward at what shapes judgement, o2 looks outward at what that judgement means for others acting on it. Keep both if reproducing the triad.'},
    {'id': 'u-adv/identity/o3', 'template': '{verb} your {object} as still open to revision through that scrutiny, {condition}.',
     'slots': [
      _vslot('Advanced', 'an Advanced-band verb for holding your own identity open rather than fixed'),
      {'key': 'object', 'role': 'object', 'fill': 'the identity held open', 'options': ['professional identity', 'sense of practice', 'standpoint as a practitioner'], 'subjectSupplied': False},
      {'key': 'condition', 'role': 'condition', 'fill': 'the autonomy expected', 'options': ['without prompting', 'across a sustained piece of work', 'independently'], 'subjectSupplied': False},
     ],
     'agentInstruction': 'No field_content or audience slot here; the point is purely reflexive. Keep the verb denoting holding identity open to revision, not closing it down into a settled professional label, which would contradict the whole triad.'},
   ],
  },
 },
}
# graduate_competency formulas: the 20 QAA-style threshold items, each in both
# registers (forPractitioner / forBeneficiary), authored against the Advanced
# section 16 band (the full honours-graduate standard FHEQ level 6 the
# competency items describe, matching TIER_BAND_ANCHOR['advanced']). Authored
# in four groups of five items; merged here into one lookup by item id.

GROUP_A = {
 'subject-knowledge-and-understanding': {
    'forPractitioner': {
        'template': "Graduates {verb} {qualifier} knowledge of the subject's {object}.",
        'sourceFill': {'verb': 'show', 'qualifier': 'broad and well-founded', 'object': 'core content'},
        'slots': [
            _vslot('Advanced', 'an Advanced-band verb for demonstrating command of core subject content', key='verb'),
            {'key': 'qualifier', 'role': 'qualifier', 'fill': 'how broad and solid the knowledge is',
             'options': ['broad and well-founded', 'wide-ranging and robust', 'extensive and well grounded'], 'subjectSupplied': False},
            {'key': 'object', 'role': 'object', 'fill': 'the part of the subject the knowledge covers',
             'options': ['core content', 'core subject matter', 'core content and key topics'], 'subjectSupplied': False},
        ],
        'agentInstruction': 'Reuse by keeping the "knowledge of the subject\'s X" frame intact; vary qualifier for breadth/soundness and verb for how the knowledge is demonstrated, while object names the content area being claimed.',
        'outcomes': [
            {'id': 'subject-knowledge-and-understanding/o1', 'template': "{verb} {object} of {field_content}, {condition}.",
             'slots': [
                _vslot('Advanced', 'an Advanced-band verb for demonstrating depth of command over core content, not merely knowing it'),
                {'key': 'object', 'role': 'object', 'fill': 'the content area being demonstrated',
                 'options': ['core content', 'core subject matter', 'key content areas'], 'subjectSupplied': False},
                {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain",
                 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                {'key': 'condition', 'role': 'condition', 'fill': 'how the command of content is evidenced',
                 'options': ['with reference to primary sources', 'without relying on lecture notes alone', 'linking it to current scholarship'], 'subjectSupplied': False},
             ],
             'agentInstruction': 'Fill field_content with the subject itself. Choose a verb that shows active command of content rather than passive familiarity, and let condition specify the evidence that demonstrates breadth and soundness.'},
        ],
    },
    'forBeneficiary': {
        'template': "You {verb_1} the core content of your subject well and can {verb_2} it.",
        'sourceFill': {'verb_1': 'know', 'verb_2': 'show'},
        'slots': [
            _vslot('Advanced', 'an Advanced-band verb standing in for the live, banned "know" (sourceFill keeps the live wording; options stay clean)', key='verb_1'),
            _vslot('Advanced', 'an Advanced-band verb for demonstrating the knowledge once held', key='verb_2'),
        ],
        'agentInstruction': 'sourceFill preserves the live statement\'s banned verb "know" exactly, but both verb slots offer clean Advanced-band options for anything newly generated: pair a command-of-content verb with a demonstration verb.',
        'outcomes': [],
    },
 },
 'analysis-and-problem-solving': {
    'forPractitioner': {
        'template': "Graduates {verb_1} {object_1} and {verb_2} towards {object_2} using the subject's {object_3}.",
        'sourceFill': {'verb_1': 'analyse', 'object_1': 'problems', 'verb_2': 'work', 'object_2': 'solutions', 'object_3': 'approaches'},
        'slots': [
            _vslot('Advanced', 'an Advanced-band verb for breaking a problem into its component parts', key='verb_1'),
            {'key': 'object_1', 'role': 'object', 'fill': 'what is being analysed',
             'options': ['problems', 'complex problems', 'ill-structured problems'], 'subjectSupplied': False},
            _vslot('Advanced', 'an Advanced-band verb for building towards a solution', key='verb_2'),
            {'key': 'object_2', 'role': 'object', 'fill': 'what is being worked towards',
             'options': ['solutions', 'workable solutions', 'practical solutions'], 'subjectSupplied': False},
            {'key': 'object_3', 'role': 'object', 'fill': "the subject's own methods used to get there",
             'options': ['approaches', 'methods and approaches', 'disciplinary approaches'], 'subjectSupplied': False},
        ],
        'agentInstruction': 'Keep the two-clause frame: a breakdown verb acting on a problem, then a solution-building verb acting on a solution, both anchored by the subject\'s own approaches. Vary each object independently to fit context.',
        'outcomes': [
            {'id': 'analysis-and-problem-solving/o1', 'template': "{verb} {object}, {condition}.",
             'slots': [
                _vslot('Advanced', 'an Advanced-band verb for critically breaking a problem into its parts'),
                {'key': 'object', 'role': 'object', 'fill': 'the problem being broken down',
                 'options': ['complex problems', 'ill-defined problems', 'multi-part problems'], 'subjectSupplied': False},
                {'key': 'condition', 'role': 'condition', 'fill': 'the rigour behind the breakdown', 'options': ['using evidence to support each step', 'separating relevant from irrelevant information', 'justifying each stage of the breakdown'], 'subjectSupplied': False},
             ],
             'agentInstruction': 'Use for the analysis half of the competency only. The verb must denote genuine decomposition of a problem, not description of it; condition should require evidence or justification for how the breakdown was carried out.'},
            {'id': 'analysis-and-problem-solving/o2', 'template': "{verb} {object} using {field_content}'s approaches, {condition}.",
             'slots': [
                _vslot('Advanced', 'an Advanced-band verb for building a solution from a disciplinary approach'),
                {'key': 'object', 'role': 'object', 'fill': 'the solution produced',
                 'options': ['workable solutions', 'practical solutions', 'a solution'], 'subjectSupplied': False},
                {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain",
                 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                {'key': 'condition', 'role': 'condition', 'fill': 'how the approach was chosen or tested', 'options': ['selecting the approach best suited to the problem', 'testing the solution against the original problem', 'adapting a standard approach to a new case'], 'subjectSupplied': False},
             ],
             'agentInstruction': 'Use for the solution-building half of the competency. Fill field_content with the subject itself so the solution is explicitly grounded in disciplinary approaches rather than generic problem solving.'},
        ],
    },
    'forBeneficiary': {
        'template': "You {verb_1} {object_1} down and {verb_2} out {object_2} using your subject's {object_3}.",
        'sourceFill': {'verb_1': 'break', 'object_1': 'problems', 'verb_2': 'work', 'object_2': 'solutions', 'object_3': 'methods'},
        'slots': [
            _vslot('Advanced', 'an Advanced-band verb for breaking a problem into parts, phrased for the student register', key='verb_1'),
            {'key': 'object_1', 'role': 'object', 'fill': 'what is being broken down',
             'options': ['problems', 'complex problems', 'tricky problems'], 'subjectSupplied': False},
            _vslot('Advanced', 'an Advanced-band verb for working out a solution', key='verb_2'),
            {'key': 'object_2', 'role': 'object', 'fill': 'what is being worked out',
             'options': ['solutions', 'workable solutions', 'answers'], 'subjectSupplied': False},
            {'key': 'object_3', 'role': 'object', 'fill': "the subject's own methods used",
             'options': ['methods', 'methods and techniques', 'tools and methods'], 'subjectSupplied': False},
        ],
        'agentInstruction': 'Mirrors the practitioner formula in plainer, second-person phrasing: a breakdown verb on a problem, then a solving verb on a solution, both grounded in the subject\'s own methods. Vary objects to suit the context.',
        'outcomes': [],
    },
 },
 'applying-knowledge-to-practice-or-problems': {
    'forPractitioner': {
        'template': "Graduates {verb} {object} to {object_2}.",
        'sourceFill': {'verb': 'apply', 'object': 'subject knowledge', 'object_2': 'practical situations and problems'},
        'slots': [
            _vslot('Advanced', 'an Advanced-band verb for putting subject knowledge to practical use', key='verb'),
            {'key': 'object', 'role': 'object', 'fill': 'the knowledge being applied',
             'options': ['subject knowledge', 'knowledge of the subject', 'subject-specific knowledge'], 'subjectSupplied': False},
            {'key': 'object_2', 'role': 'object', 'fill': 'the practical situations and problems knowledge is applied to',
             'options': ['practical situations and problems', 'real-world situations and problems', 'practice-based situations and problems'], 'subjectSupplied': False},
        ],
        'agentInstruction': 'Keep the single-clause "apply X to Y" frame: vary the verb for the manner of application, the first object for the knowledge drawn on, and the second object for the practical situations or problems it meets.',
        'outcomes': [
            {'id': 'applying-knowledge-to-practice-or-problems/o1', 'template': "{verb} {field_content} knowledge to {object}, {condition}.",
             'slots': [
                _vslot('Advanced', 'an Advanced-band verb for putting knowledge to use on a practical case'),
                {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain",
                 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                {'key': 'object', 'role': 'object', 'fill': 'the practical situation or problem knowledge is applied to',
                 'options': ['a practical situation', 'a real-world problem', 'a practice-based scenario'], 'subjectSupplied': False},
                {'key': 'condition', 'role': 'condition', 'fill': 'what grounds the application in the subject', 'options': ['drawing on established subject principles', 'applying methods learned within the subject', 'using evidence-based practice from the subject'], 'subjectSupplied': False},
             ],
             'agentInstruction': 'Fill field_content with the subject itself. Choose a verb that denotes active application to a case, not recall of theory, and let condition specify which subject principles or methods ground that application.'},
        ],
    },
    'forBeneficiary': {
        'template': "You can {verb} what you know on {object_1} and in {object_2}.",
        'sourceFill': {'verb': 'use', 'object_1': 'real problems', 'object_2': 'practical settings'},
        'slots': [
            _vslot('Advanced', 'an Advanced-band verb for putting knowledge to use, phrased for the student register', key='verb'),
            {'key': 'object_1', 'role': 'object', 'fill': 'the problems knowledge is used on',
             'options': ['real problems', 'genuine problems', 'real-world problems'], 'subjectSupplied': False},
            {'key': 'object_2', 'role': 'object', 'fill': 'the settings knowledge is used in',
             'options': ['practical settings', 'practice-based settings', 'hands-on settings'], 'subjectSupplied': False},
        ],
        'agentInstruction': 'Keeps the fixed phrase "what you know" intact and only varies the verb plus the two destination objects: the kind of real problem and the kind of practical setting knowledge gets used in.',
        'outcomes': [],
    },
 },
 'critical-evaluation-of-evidence-and-arguments': {
    'forPractitioner': {
        'template': "Graduates {verb_1} {object_1} {qualifier} and {verb_2} {object_2}.",
        'sourceFill': {'verb_1': 'evaluate', 'object_1': 'evidence and arguments', 'qualifier': 'critically', 'verb_2': 'reach', 'object_2': 'reasoned judgements'},
        'slots': [
            _vslot('Advanced', 'an Advanced-band verb for critically weighing evidence and arguments', key='verb_1'),
            {'key': 'object_1', 'role': 'object', 'fill': 'the evidence and arguments weighed, bundled as one object',
             'options': ['evidence and arguments', 'the evidence and the arguments for it', 'competing evidence and arguments'], 'subjectSupplied': False},
            {'key': 'qualifier', 'role': 'qualifier', 'fill': 'the manner of the evaluation',
             'options': ['critically', 'rigorously', 'with a critical eye'], 'subjectSupplied': False},
            _vslot('Advanced', 'an Advanced-band verb for arriving at a reasoned judgement', key='verb_2'),
            {'key': 'object_2', 'role': 'object', 'fill': 'the judgement arrived at',
             'options': ['reasoned judgements', 'justified judgements', 'defensible judgements'], 'subjectSupplied': False},
        ],
        'agentInstruction': 'Keep the two-clause frame: a critical-weighing verb acting on bundled evidence-and-arguments, then a judgement verb acting on the resulting judgement. Qualifier controls how critical the weighing is; vary both objects independently.',
        'outcomes': [
            {'id': 'critical-evaluation-of-evidence-and-arguments/o1', 'template': "{verb} {object}, {condition}.",
             'slots': [
                _vslot('Advanced', 'an Advanced-band verb for critically weighing evidence and arguments'),
                {'key': 'object', 'role': 'object', 'fill': 'evidence and arguments, bundled as one object',
                 'options': ['evidence and arguments', 'the evidence and the arguments for it', 'competing evidence and arguments'], 'subjectSupplied': False},
                {'key': 'condition', 'role': 'condition', 'fill': 'how the critical weighing is demonstrated', 'options': ['identifying strengths and weaknesses in each source', 'comparing the credibility of competing claims', 'testing claims against counter-evidence'], 'subjectSupplied': False},
             ],
             'agentInstruction': 'Use for the evaluative half only. Bundle evidence and arguments into a single object phrase rather than splitting them with a coordinating "and", which would reintroduce the AL-2 violation this design avoids.'},
            {'id': 'critical-evaluation-of-evidence-and-arguments/o2', 'template': "{verb} {object}, {condition}.",
             'slots': [
                _vslot('Advanced', 'an Advanced-band verb for forming a reasoned judgement from an evaluation'),
                {'key': 'object', 'role': 'object', 'fill': 'the judgement reached',
                 'options': ['a reasoned judgement', 'a justified conclusion', 'a defensible judgement'], 'subjectSupplied': False},
                {'key': 'condition', 'role': 'condition', 'fill': 'the basis for the judgement', 'options': ['based on the weight of the evidence', 'after weighing competing arguments', 'having ruled out weaker alternatives'], 'subjectSupplied': False},
             ],
             'agentInstruction': 'Use for the judgement half only, after an evaluation has taken place. The verb must denote arriving at a conclusion, and condition should name the evidential basis that makes the judgement defensible.'},
        ],
    },
    'forBeneficiary': {
        'template': "You {verb_1} up {object_1} {qualifier} and {verb_2} to {object_2}.",
        'sourceFill': {'verb_1': 'weigh', 'object_1': 'evidence and arguments', 'qualifier': 'critically', 'verb_2': 'come', 'object_2': 'reasoned conclusions'},
        'slots': [
            _vslot('Advanced', 'an Advanced-band verb standing in for "weigh" in the student register', key='verb_1'),
            {'key': 'object_1', 'role': 'object', 'fill': 'the evidence and arguments weighed, bundled as one object',
             'options': ['evidence and arguments', 'the evidence and the arguments for it', 'competing evidence and arguments'], 'subjectSupplied': False},
            {'key': 'qualifier', 'role': 'qualifier', 'fill': 'the manner of the weighing',
             'options': ['critically', 'rigorously', 'with a critical eye'], 'subjectSupplied': False},
            _vslot('Advanced', 'an Advanced-band verb standing in for "come" in the student register', key='verb_2'),
            {'key': 'object_2', 'role': 'object', 'fill': 'the conclusion arrived at',
             'options': ['reasoned conclusions', 'justified conclusions', 'defensible conclusions'], 'subjectSupplied': False},
        ],
        'agentInstruction': 'Mirrors the practitioner formula with the fixed idiom "weigh up ... and come to ...": vary the verbs, the bundled evidence-and-arguments object, the qualifier, and the conclusion object while keeping the two-clause shape.',
        'outcomes': [],
    },
 },
 'oral-or-other-communication-to-audiences': {
    'forPractitioner': {
        'template': "Graduates {verb} the subject {qualifier} to {audience} and in {scope}.",
        'sourceFill': {'verb': 'communicate', 'qualifier': 'clearly', 'audience': 'different audiences', 'scope': 'different forms'},
        'slots': [
            _vslot('Advanced', 'an Advanced-band verb for communicating subject content to an audience', key='verb'),
            {'key': 'qualifier', 'role': 'qualifier', 'fill': 'how clear the communication is',
             'options': ['clearly', 'accessibly', 'in plain language'], 'subjectSupplied': False},
            {'key': 'audience', 'role': 'audience', 'fill': 'who the communication reaches',
             'options': ['different audiences', 'varied audiences', 'a range of audiences'], 'subjectSupplied': False},
            {'key': 'scope', 'role': 'scope', 'fill': 'the range of forms the communication takes',
             'options': ['different forms', 'a range of forms', 'varied formats'], 'subjectSupplied': False},
        ],
        'agentInstruction': 'Keep the "communicate X to audience in forms" frame: vary the verb for the mode of communicating, qualifier for clarity, audience for who is addressed, and scope for the range of forms used.',
        'outcomes': [
            {'id': 'oral-or-other-communication-to-audiences/o1', 'template': "{verb} {object} {qualifier} to {audience}, {condition}.",
             'slots': [
                _vslot('Advanced', 'an Advanced-band verb for making subject content understandable to an audience'),
                {'key': 'object', 'role': 'object', 'fill': 'the subject matter communicated',
                 'options': ['the subject', 'key ideas in the subject', 'core subject content'], 'subjectSupplied': False},
                {'key': 'qualifier', 'role': 'qualifier', 'fill': 'how clear the communication is',
                 'options': ['clearly', 'accessibly', 'in plain language'], 'subjectSupplied': False},
                {'key': 'audience', 'role': 'audience', 'fill': 'who is being addressed',
                 'options': ['a non-specialist audience', 'an audience unfamiliar with the subject', 'a mixed audience'], 'subjectSupplied': False},
                {'key': 'condition', 'role': 'condition', 'fill': 'what form or medium carries the communication', 'options': ['using a form suited to that audience', 'adapting the format to the audience', 'choosing a form the audience can engage with'], 'subjectSupplied': False},
             ],
             'agentInstruction': 'Fill audience with a concrete type of listener or reader and let condition name the form or medium chosen for them. The verb should denote active, audience-shaped communication rather than mere delivery of content.'},
        ],
    },
    'forBeneficiary': {
        'template': "You can {verb} your subject {qualifier} to {audience}, in {scope}.",
        'sourceFill': {'verb': 'explain', 'qualifier': 'clearly', 'audience': 'different audiences', 'scope': 'more than one form'},
        'slots': [
            _vslot('Advanced', 'an Advanced-band verb for explaining subject content to an audience, in the student register', key='verb'),
            {'key': 'qualifier', 'role': 'qualifier', 'fill': 'how clear the explanation is',
             'options': ['clearly', 'accessibly', 'in plain language'], 'subjectSupplied': False},
            {'key': 'audience', 'role': 'audience', 'fill': 'who the explanation reaches',
             'options': ['different audiences', 'varied audiences', 'a range of audiences'], 'subjectSupplied': False},
            {'key': 'scope', 'role': 'scope', 'fill': 'the range of forms the explanation takes',
             'options': ['more than one form', 'several different forms', 'a range of forms'], 'subjectSupplied': False},
        ],
        'agentInstruction': 'Mirrors the practitioner formula in second-person phrasing: vary the verb for how the explaining is done, qualifier for clarity, audience for who is addressed, and scope for how many forms are covered.',
        'outcomes': [],
    },
 },
}

GROUP_B = {
    'research-and-enquiry-methods': {
        'forPractitioner': {
            'template': "Graduates {verb_1} and {verb_2} the subject's methods of research and enquiry.",
            'sourceFill': {'verb_1': 'understand', 'verb_2': 'use'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb for critically engaging with the subject's research methods, replacing the live statement's banned verb 'understand'", key='verb_1'),
                _vslot('Advanced', "an Advanced-band verb for actively applying the subject's methods of research and enquiry", key='verb_2'),
            ],
            'agentInstruction': "Reuse wherever a graduate outcome pairs critical command of a subject's research methods with actively using them. verb_1's options stay clean Advanced-band verbs even though sourceFill preserves the live statement's banned 'understand'; verb_2 covers the active-use clause, and the fixed object text should stay unchanged.",
            'outcomes': [
                {'id': 'research-and-enquiry-methods/o1', 'template': "{verb} the {object} of {field_content}, {condition}.",
                 'slots': [
                    _vslot('Advanced', "an Advanced-band verb for critically assessing research methods rather than merely understanding them"),
                    {'key': 'object', 'role': 'object', 'fill': 'the methods of research and enquiry used in the field',
                     'options': ['methods of research and enquiry', 'research methods and approaches to enquiry', 'established research and enquiry techniques'], 'subjectSupplied': False},
                    {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                    {'key': 'condition', 'role': 'condition', 'fill': 'the basis on which the methods are judged',
                     'options': ['against alternative approaches', 'with reference to their limitations', 'before applying them to a new research question'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Fill field_content with the subject itself. Keep the verb a genuinely evaluative operation that weighs methods critically rather than passively understanding them, and choose a condition that names the comparison basis used to judge the methods."},
                {'id': 'research-and-enquiry-methods/o2', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', "an Advanced-band verb for constructing or carrying out an original piece of research"),
                    {'key': 'object', 'role': 'object', 'fill': 'an independent research enquiry designed by the learner',
                     'options': ['an original research enquiry', 'an independent investigation of their own design', "a research project using the subject's recognised methods"], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'the standard the enquiry is expected to meet',
                     'options': ["following the subject's recognised methods", 'applying accepted standards of rigour', 'addressing a question they have framed themselves'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Use this to assess active use of research methods rather than merely describing them. The object should name a genuine piece of independent research; the condition should specify the methodological standard expected, keeping verb, object and condition each singular and unjoined."},
            ],
        },
        'forBeneficiary': {
            'template': "You {verb_1} how research is done in {field_content} and can {verb_2} an enquiry yourself.",
            'sourceFill': {'verb_1': 'know', 'field_content': 'your subject', 'verb_2': 'carry out'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb for engaging critically with how research is done in the subject, replacing the live text's banned verb 'know'", key='verb_1'),
                {'key': 'field_content', 'role': 'field_content', 'fill': "the learner's own subject", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                _vslot('Advanced', 'an Advanced-band verb for carrying out an original enquiry independently', key='verb_2'),
            ],
            'agentInstruction': "Reuse for the student-facing research-methods competency. field_content should be filled with the learner's own subject; verb_1's options stay clean Advanced-band verbs even though sourceFill preserves the live text's banned 'know', and verb_2 covers independently carrying out an enquiry.",
            'outcomes': [],
        },
    },
    'theories': {
        'forPractitioner': {
            'template': "Graduates {verb} the subject's {object}.",
            'sourceFill': {'verb': 'understand', 'object': 'main theories and concepts and the debates between them'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb for critically weighing a subject's main theories, concepts and the debates between them, replacing the live statement's banned verb 'understand'", key='verb'),
                {'key': 'object', 'role': 'object', 'fill': 'the bundled main theories, concepts and debates between them',
                 'options': ['main theories and concepts and the debates between them', 'core theories, concepts and the debates surrounding them', 'main theoretical concepts and the arguments between them'], 'subjectSupplied': False},
            ],
            'agentInstruction': "Reuse wherever a graduate outcome asserts command of a subject's core theoretical landscape. object bundles theories, concepts and debates as one noun phrase so later outcomes avoid an AL-2 'and' violation; verb's options stay clean Advanced-band verbs despite sourceFill preserving the banned 'understand'.",
            'outcomes': [
                {'id': 'theories/o1', 'template': "{verb} {field_content}'s {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', "an Advanced-band verb for weighing a subject's theories, concepts and debates against each other"),
                    {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                    {'key': 'object', 'role': 'object', 'fill': 'theories, concepts and the debates between them bundled as one object',
                     'options': ['main theories and concepts and the debates between them', 'core theories, concepts and the debates surrounding them', 'theoretical positions and the disagreements between them'], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'the basis on which the debates are weighed',
                     'options': ['comparing more than one position', 'with reference to ongoing disagreement', 'without relying on a single source'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Fill field_content with the subject itself. Keep theories, concepts and debates bundled as one object rather than splitting them with 'and' in the template's own wording, since separating them would reintroduce the AL-2 violation this bundling avoids."},
            ],
        },
        'forBeneficiary': {
            'template': "You {verb} the main ideas and theories in {field_content} and where people disagree about them.",
            'sourceFill': {'verb': 'understand', 'field_content': 'your subject'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb for critically engaging with a subject's main ideas, theories and the disagreements between them, replacing the live text's banned verb 'understand'", key='verb'),
                {'key': 'field_content', 'role': 'field_content', 'fill': "the learner's own subject", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
            ],
            'agentInstruction': "Reuse for the student-facing version of the theories competency. field_content takes the learner's own subject; verb's options remain clean Advanced-band verbs even though sourceFill keeps the live text's banned 'understand' to preserve the original statement exactly.",
            'outcomes': [],
        },
    },
    'ethics': {
        'forPractitioner': {
            'template': "Graduates {verb_1} and {verb_2} the ethical issues and responsibilities of the subject.",
            'sourceFill': {'verb_1': 'recognise', 'verb_2': 'act on'},
            'slots': [
                _vslot('Advanced', 'an Advanced-band verb for critically identifying the ethical issues and responsibilities of the subject', key='verb_1'),
                _vslot('Advanced', 'an Advanced-band verb for justifying action taken in response to ethical issues and responsibilities', key='verb_2'),
            ],
            'agentInstruction': "Reuse wherever a graduate outcome pairs identifying ethical issues with acting on them. verb_1 covers the recognition clause and verb_2 the action clause; both should draw from clean Advanced-band verbs, and the fixed object phrase naming ethical issues and responsibilities should stay unchanged.",
            'outcomes': [
                {'id': 'ethics/o1', 'template': "{verb} the {object} of {field_content}, {condition}.",
                 'slots': [
                    _vslot('Advanced', 'an Advanced-band verb for critically identifying ethical issues and responsibilities'),
                    {'key': 'object', 'role': 'object', 'fill': 'the ethical issues and responsibilities bundled as one object',
                     'options': ['ethical issues and responsibilities', 'ethical risks and obligations', 'ethical concerns and duties'], 'subjectSupplied': False},
                    {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                    {'key': 'condition', 'role': 'condition', 'fill': 'the situation in which the issues are identified',
                     'options': ['in a given scenario', 'before beginning a piece of work', 'when reviewing a case study'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Fill field_content with the subject itself. Keep ethical issues and responsibilities bundled as a single object rather than two coordinate nouns joined by 'and' in the template's own wording, and specify a concrete situation in condition."},
                {'id': 'ethics/o2', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', 'an Advanced-band verb for justifying a course of action taken in response to an ethical issue'),
                    {'key': 'object', 'role': 'object', 'fill': 'a concrete response or course of action on an ethical matter',
                     'options': ['a response to an identified ethical issue', 'a course of action addressing an ethical responsibility', 'a justified response to an ethical dilemma'], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'the manner in which responsibility for the action is shown',
                     'options': ['with reference to professional standards', 'taking responsibility for the outcome', 'before any harm can occur'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Use this to assess acting on ethical issues, not merely spotting them. The object should name a concrete response or course of action; condition should specify accountability or timing, keeping the three roles singular so the outcome isn't two linked tasks."},
            ],
        },
        'forBeneficiary': {
            'template': "You {verb_1} the ethical questions in {field_content} and {verb_2} responsibly.",
            'sourceFill': {'verb_1': 'recognise', 'field_content': 'your subject', 'verb_2': 'act'},
            'slots': [
                _vslot('Advanced', 'an Advanced-band verb for critically identifying the ethical questions in the subject', key='verb_1'),
                {'key': 'field_content', 'role': 'field_content', 'fill': "the learner's own subject", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                _vslot('Advanced', 'an Advanced-band verb for justifying responsible action taken on an ethical question', key='verb_2'),
            ],
            'agentInstruction': "Reuse for the student-facing ethics competency. field_content takes the learner's own subject; verb_1 covers recognising ethical questions and verb_2 the responsible-action clause, both drawn from clean Advanced-band verbs rather than vague alternatives.",
            'outcomes': [],
        },
    },
    'history': {
        'forPractitioner': {
            'template': "Graduates {verb_1} the subject in its history and context and {verb_2} where it currently stands.",
            'sourceFill': {'verb_1': 'place', 'verb_2': 'know'},
            'slots': [
                _vslot('Advanced', 'an Advanced-band verb for critically situating the subject within its history and context', key='verb_1'),
                _vslot('Advanced', "an Advanced-band verb for evaluating where the subject currently stands, replacing the live statement's banned verb 'know'", key='verb_2'),
            ],
            'agentInstruction': "Reuse wherever a graduate outcome pairs historical situating of a subject with judgement of its current standing. verb_1 covers the placing clause and verb_2 the current-standing clause; verb_2's options stay clean Advanced-band verbs despite sourceFill preserving the live statement's banned 'know'.",
            'outcomes': [
                {'id': 'history/o1', 'template': "{verb} {field_content} within {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', "an Advanced-band verb for critically situating a subject within its history and context"),
                    {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                    {'key': 'object', 'role': 'object', 'fill': 'the history and context bundled as one object',
                     'options': ['its history and context', 'its historical development and setting', 'its origins and current context'], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'the evidence used to situate the subject',
                     'options': ['drawing on more than one historical source', 'with reference to a specific period', 'using evidence of how it has changed'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Fill field_content with the subject itself. Keep history and context bundled as one object rather than two nouns joined by 'and' in the template's own wording, and specify the evidence base used to situate the subject in condition."},
                {'id': 'history/o2', 'template': "{verb} the {object} of where {field_content} currently stands, {condition}.",
                 'slots': [
                    _vslot('Advanced', "an Advanced-band verb for evaluating where a subject currently stands, replacing the banned verb 'know'"),
                    {'key': 'object', 'role': 'object', 'fill': 'the current standing or position of the subject',
                     'options': ['current standing', 'present position', 'current state of development'], 'subjectSupplied': False},
                    {'key': 'field_content', 'role': 'field_content', 'fill': "the subject's own domain", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                    {'key': 'condition', 'role': 'condition', 'fill': 'the evidential basis for the judgement',
                     'options': ['with reference to recent developments', 'comparing it with where it stood previously', 'using more than one source of evidence'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Fill field_content with the subject itself. This targets judgement of current disciplinary standing rather than simply knowing it; keep the verb genuinely evaluative and use condition to specify the evidential basis for the judgement being made."},
            ],
        },
        'forBeneficiary': {
            'template': "You {verb} how {field_content} developed, the settings it works in and what is current in it.",
            'sourceFill': {'verb': 'know', 'field_content': 'your subject'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb for critically tracing how a subject developed, the settings it works in and what is current in it, replacing the live text's banned verb 'know'"),
                {'key': 'field_content', 'role': 'field_content', 'fill': "the learner's own subject", 'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
            ],
            'agentInstruction': "Reuse for the student-facing history competency. field_content takes the learner's own subject; verb's options stay clean Advanced-band verbs even though sourceFill preserves the live text's banned 'know' so the original statement is kept exact.",
            'outcomes': [],
        },
    },
    'teamwork-and-collaboration': {
        'forPractitioner': {
            'template': "Graduates {verb} {qualifier} with {object}.",
            'sourceFill': {'verb': 'work', 'qualifier': 'effectively', 'object': 'others'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb for collaborating with others, replacing the live statement's plain verb 'work'"),
                {'key': 'qualifier', 'role': 'qualifier', 'fill': 'how effectively the collaboration is carried out',
                 'options': ['effectively', 'productively', 'constructively'], 'subjectSupplied': False},
                {'key': 'object', 'role': 'object', 'fill': 'the people worked with',
                 'options': ['others', 'fellow team members', 'colleagues from different backgrounds'], 'subjectSupplied': False},
            ],
            'agentInstruction': "Reuse this compact formula wherever a graduate outcome asserts effective teamwork. verb replaces the live text's plain 'work' with a richer Advanced-band collaborative verb; qualifier and object can vary the manner and the people collaborated with while keeping the sentence simple.",
            'outcomes': [
                {'id': 'teamwork-and-collaboration/o1', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', 'an Advanced-band verb for constructing or justifying effective collaborative work with others'),
                    {'key': 'object', 'role': 'object', 'fill': 'the shared output produced through collaboration',
                     'options': ['a shared team outcome', 'a joint piece of work with others', 'a collaborative solution to a shared task'], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'the manner in which the collaboration succeeds',
                     'options': ['taking account of differing viewpoints', 'meeting agreed deadlines as a group', 'resolving disagreement constructively'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Use this single outcome to evidence effective teamwork. Fill object with a genuine shared output rather than a solo task, and use condition to specify what makes the collaboration effective, such as handling disagreement or differing viewpoints."},
            ],
        },
        'forBeneficiary': {
            'template': "You can {verb} {qualifier} with {object}.",
            'sourceFill': {'verb': 'work', 'qualifier': 'well', 'object': 'other people'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb for collaborating with other people, replacing the live text's plain verb 'work'"),
                {'key': 'qualifier', 'role': 'qualifier', 'fill': 'how well the collaboration is carried out',
                 'options': ['well', 'effectively', 'productively'], 'subjectSupplied': False},
                {'key': 'object', 'role': 'object', 'fill': 'the people worked with',
                 'options': ['other people', 'fellow students', 'people from different backgrounds'], 'subjectSupplied': False},
            ],
            'agentInstruction': "Reuse for the student-facing teamwork competency. verb replaces the live text's plain 'work' with a richer Advanced-band collaborative verb; qualifier and object can vary the manner and who is collaborated with while preserving the simple sentence structure.",
            'outcomes': [],
        },
    },
}

GROUP_C = {
    'independent-and-self-directed-learning': {
        'forPractitioner': {
            'template': "Graduates {verb_1} their own learning and {verb_2} independently.",
            'sourceFill': {'verb_1': 'manage', 'verb_2': 'work'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'manage', covering how graduates direct their own learning", key='verb_1'),
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'work', covering unsupervised task completion", key='verb_2'),
            ],
            'agentInstruction': "Reuse by keeping the two-clause shape: a learning-management verb followed by an independent-working verb. sourceFill preserves the exact live words; when generating new text, swap only the slot options, both drawn from the Advanced band, never the literal 'manage'/'work' pairing.",
            'outcomes': [
                {'id': 'independent-and-self-directed-learning/o1', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                     _vslot('Advanced', 'an Advanced-band verb for critically directing or organising own learning', key='verb'),
                     {'key': 'object', 'role': 'object', 'fill': 'the learning being self-managed',
                      'options': ['own learning and development', 'personal study programme', 'independent learning plan'], 'subjectSupplied': False},
                     {'key': 'condition', 'role': 'condition', 'fill': 'how unsupervised the self-management is',
                      'options': ['without routine supervision', 'in unfamiliar contexts', 'when goals are self-set'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Use this for the self-management half of the pair. Fill verb with an Advanced-band directing/organising operation, object with a bundled learning noun phrase, and condition with the degree of autonomy expected, avoiding any supervised or guided phrasing."},
                {'id': 'independent-and-self-directed-learning/o2', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                     _vslot('Advanced', 'an Advanced-band verb for critically organising independent working practice', key='verb'),
                     {'key': 'object', 'role': 'object', 'fill': 'the tasks or schedule being worked through independently',
                      'options': ['working practices and schedule', 'tasks and study plan', 'assigned work and deadlines'], 'subjectSupplied': False},
                     {'key': 'condition', 'role': 'condition', 'fill': 'the absence of direct oversight',
                      'options': ['without direct supervision', 'while managing competing deadlines', 'in self-directed study contexts'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Use this for the independent-working half of the pair. The object should bundle tasks/schedule into one noun phrase; the condition must signal lack of direct supervision, distinguishing this outcome from the learning-management outcome above."},
            ],
        },
        'forBeneficiary': {
            'template': "You can {verb_1} your own learning and {verb_2} on your own.",
            'sourceFill': {'verb_1': 'manage', 'verb_2': 'work'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'manage', covering how the learner directs their own learning", key='verb_1'),
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'work', covering unsupervised task completion", key='verb_2'),
            ],
            'agentInstruction': "Mirror the practitioner formula but keep second-person phrasing ('You can...on your own'). sourceFill holds the exact live verbs; any regenerated text must still slot in two Advanced-band verbs around the fixed 'your own learning and...on your own' frame.",
            'outcomes': [],
        },
    },
    'information-and-sources': {
        'forPractitioner': {
            'template': "Graduates {verb_1}, {verb_2} and {verb_3} information and sources appropriate to the subject.",
            'sourceFill': {'verb_1': 'find', 'verb_2': 'select', 'verb_3': 'use'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'find', covering locating relevant sources", key='verb_1'),
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'select', covering critically choosing between sources", key='verb_2'),
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'use', covering applying sources appropriately", key='verb_3'),
            ],
            'agentInstruction': "Keep the three-verb sequence (locate, choose, apply) fixed around the bundled object 'information and sources appropriate to the subject'. Fill each verb slot from the Advanced band; do not collapse or reorder the three verbs when reproducing the live sentence.",
            'outcomes': [
                {'id': 'information-and-sources/o1', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                     _vslot('Advanced', 'an Advanced-band verb bundling the find/select/use sequence into one critical information-handling operation', key='verb'),
                     {'key': 'object', 'role': 'object', 'fill': 'the information and sources being handled',
                      'options': ['information and sources appropriate to the subject', 'relevant sources and data', 'appropriate information and materials'], 'subjectSupplied': False},
                     {'key': 'condition', 'role': 'condition', 'fill': 'how the subject-appropriateness is judged',
                      'options': ["for the subject's specific requirements", 'to support subject-specific enquiry', 'according to disciplinary conventions'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Bundles the live text's three verbs (find, select, use) into a single Advanced-band verb, since generating three separate outcomes would be excessive. Keep the object as one noun phrase covering both information and sources, and anchor condition to subject-appropriateness."},
            ],
        },
        'forBeneficiary': {
            'template': "You can {verb_1}, {verb_2} and {verb_3} the right sources and information for your subject.",
            'sourceFill': {'verb_1': 'find', 'verb_2': 'choose', 'verb_3': 'use'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'find', covering locating relevant sources", key='verb_1'),
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'choose', covering critically choosing between sources", key='verb_2'),
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'use', covering applying sources appropriately", key='verb_3'),
            ],
            'agentInstruction': "Mirror the practitioner formula's three-verb sequence but keep second-person 'You can...for your subject' phrasing. sourceFill records the exact live verbs ('find, choose, use'); fill regenerated versions from the Advanced band in the same order.",
            'outcomes': [],
        },
    },
    'data': {
        'forPractitioner': {
            'template': "Graduates {verb} data and numbers appropriately for the subject.",
            'sourceFill': {'verb': 'handle'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'handle', covering working rigorously with quantitative material", key='verb'),
            ],
            'agentInstruction': "Keep the single-verb shape with the fixed bundled object 'data and numbers' and the fixed 'appropriately for the subject' qualifier. Replace only the verb, drawing from the Advanced band, when generating new statements from this formula.",
            'outcomes': [
                {'id': 'data/o1', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                     _vslot('Advanced', 'an Advanced-band verb for critically working with quantitative data', key='verb'),
                     {'key': 'object', 'role': 'object', 'fill': 'the data or numbers being worked with',
                      'options': ['data and numbers', 'quantitative data and figures', 'numerical data and statistics'], 'subjectSupplied': False},
                     {'key': 'condition', 'role': 'condition', 'fill': 'the standard of subject-appropriateness required',
                      'options': ['in ways appropriate to the subject', 'using subject-appropriate methods', 'to standards expected in the discipline'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Fill verb with an Advanced-band quantitative operation, keep object as one bundled data/numbers noun phrase, and use condition to tie the handling back to subject-specific standards rather than generic numeracy."},
            ],
        },
        'forBeneficiary': {
            'template': "You can {verb} data and numbers in the way your subject needs.",
            'sourceFill': {'verb': 'work with'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'work with', covering engaging rigorously with quantitative material", key='verb'),
            ],
            'agentInstruction': "Mirror the practitioner formula in second person. sourceFill preserves the exact live phrase 'work with'; keep the fixed 'data and numbers in the way your subject needs' wording and only vary the verb slot when regenerating.",
            'outcomes': [],
        },
    },
    'digital-skills': {
        'forPractitioner': {
            'template': "Graduates {verb} the digital tools and technologies the subject relies on.",
            'sourceFill': {'verb': 'use'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'use', covering critically deploying digital tools", key='verb'),
            ],
            'agentInstruction': "Keep the fixed object 'the digital tools and technologies the subject relies on' untouched; only substitute the verb slot with an Advanced-band option when producing a new version of this statement from the formula.",
            'outcomes': [
                {'id': 'digital-skills/o1', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                     _vslot('Advanced', 'an Advanced-band verb for critically deploying digital tools and technologies', key='verb'),
                     {'key': 'object', 'role': 'object', 'fill': 'the digital tools or technologies being deployed',
                      'options': ['digital tools and technologies', 'software and digital platforms', 'digital tools and systems'], 'subjectSupplied': False},
                     {'key': 'condition', 'role': 'condition', 'fill': 'the standard the tool use must meet',
                      'options': ['that the subject relies on', 'appropriate to disciplinary practice', 'to professional standards in the field'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Fill verb with an Advanced-band deployment operation and object with a bundled tools/technologies phrase. Use condition to anchor the tool use to subject reliance or professional standards, not generic digital literacy."},
            ],
        },
        'forBeneficiary': {
            'template': "You can {verb} the digital tools your subject depends on.",
            'sourceFill': {'verb': 'use'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb standing in for the live text's 'use', covering critically deploying digital tools", key='verb'),
            ],
            'agentInstruction': "Mirror the practitioner formula in second person, keeping the fixed phrase 'the digital tools your subject depends on'. Only the verb slot should vary, filled from the Advanced band, when regenerating this statement.",
            'outcomes': [],
        },
    },
    'sustainability': {
        'forPractitioner': {
            'template': "Graduates {verb} the subject's bearing on sustainability and the environment.",
            'sourceFill': {'verb': 'understand'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb replacing the live text's banned 'understand', covering critical evaluation of sustainability impact", key='verb'),
            ],
            'agentInstruction': "sourceFill deliberately preserves the live text's banned verb 'understand' to keep fidelity exact, but the verb slot's own options must stay clean Advanced-band alternatives. Keep the fixed object clause untouched when regenerating.",
            'outcomes': [
                {'id': 'sustainability/o1', 'template': "{verb} {field_content}'s {object}, {condition}.",
                 'slots': [
                     _vslot('Advanced', 'an Advanced-band verb for critically evaluating sustainability impact, never the banned live verb', key='verb'),
                     {'key': 'field_content', 'role': 'field_content', 'fill': "the subject whose sustainability bearing is assessed",
                      'options': ['your subject'], 'subjectSupplied': True, 'floor': 'your subject'},
                     {'key': 'object', 'role': 'object', 'fill': 'the bearing on sustainability and the environment',
                      'options': ['bearing on sustainability and the environment', 'impact on sustainability and the environment', 'relationship to sustainability and environmental concerns'], 'subjectSupplied': False},
                     {'key': 'condition', 'role': 'condition', 'fill': 'the evidence base used to assess the bearing',
                      'options': ['using evidence from current debates', 'with reference to recognised sustainability frameworks', 'when considering long-term environmental impact'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Fill field_content with 'your subject' and verb with a clean Advanced-band evaluative operation, never the live text's banned 'understand'. Keep object bundled as one sustainability-and-environment phrase, and ground condition in evidence or frameworks."},
            ],
        },
        'forBeneficiary': {
            'template': "You {verb} how your subject affects sustainability and the environment.",
            'sourceFill': {'verb': 'understand'},
            'slots': [
                _vslot('Advanced', "an Advanced-band verb replacing the live text's banned 'understand', covering critical evaluation of sustainability impact", key='verb'),
            ],
            'agentInstruction': "Mirror the practitioner formula in second person, preserving 'understand' only in sourceFill for exact fidelity. The verb slot's options must remain clean Advanced-band verbs; keep the fixed sustainability-and-environment clause unchanged.",
            'outcomes': [],
        },
    },
}

GROUP_D = {
    'professional-practice-and-employability': {
        'forPractitioner': {
            'template': "Graduates {verb_1} the subject's professional settings and are prepared for work.",
            'sourceFill': {'verb_1': 'understand'},
            'slots': [
                _vslot('Advanced', "the operation of critically engaging with the subject's professional settings, though the live text uses the banned verb 'understand'", key='verb_1'),
            ],
            'agentInstruction': "This formula reproduces the live professional-practice-and-employability statement exactly. Reuse it by keeping the fixed wording unchanged and substituting verb_1 from a clean Advanced-band verb list; sourceFill retains the live banned verb 'understand' solely so the template still matches the original text.",
            'outcomes': [
                {'id': 'professional-practice-and-employability/o1', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', 'an Advanced-band verb for critically examining professional settings and readiness for work'),
                    {'key': 'object', 'role': 'object', 'fill': "the subject's professional settings and work-readiness requirements",
                     'options': ["the subject's professional settings and work-readiness requirements", "professional contexts and employability expectations for the subject", "workplace settings and preparation needs within the subject"], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'how readiness for professional work is demonstrated',
                     'options': ['to demonstrate readiness for professional work', 'in preparing to enter the workplace', 'when assessing fitness for employment in the field'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': 'Use this to generate an outcome assessing understanding of professional context and work-readiness. Choose an Advanced verb that critically examines settings rather than passively knowing them; pair with a condition specifying how readiness is evidenced, such as through preparation or workplace expectations.'},
            ],
        },
        'forBeneficiary': {
            'template': "You {verb_1} how your subject is used at work and are ready for it.",
            'sourceFill': {'verb_1': 'understand'},
            'slots': [
                _vslot('Advanced', 'the operation of critically engaging with how the subject is used at work, though the live text uses the banned verb \'understand\'', key='verb_1'),
            ],
            'agentInstruction': "This formula reproduces the live student-facing version of the professional-practice statement exactly. Reuse it by keeping the fixed wording unchanged and substituting verb_1 from a clean Advanced-band verb list; sourceFill retains the live banned verb 'understand' only to match the original text.",
            'outcomes': [],
        },
    },
    'written-communication': {
        'forPractitioner': {
            'template': "Graduates {verb_1} in the {object_1} the subject requires.",
            'sourceFill': {'verb_1': 'write', 'object_1': 'forms'},
            'slots': [
                _vslot('Advanced', 'the operation of producing text in the forms the subject requires', key='verb_1'),
                {'key': 'object_1', 'role': 'object', 'fill': 'the forms or formats of writing required',
                 'options': ['forms', 'formats', 'genres'], 'subjectSupplied': False},
            ],
            'agentInstruction': "This formula reproduces the live written-communication statement exactly. Reuse it by keeping the fixed wording unchanged and substituting verb_1 and object_1 from their clean Advanced-band and noun-phrase option lists; sourceFill holds the live words 'write' and 'forms' for exact text reproduction.",
            'outcomes': [
                {'id': 'written-communication/o1', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', 'an Advanced-band verb for producing or constructing the written forms the subject requires'),
                    {'key': 'object', 'role': 'object', 'fill': 'the forms, formats or genres of writing required by the subject',
                     'options': ['the forms, formats and genres of writing required by the subject', 'the written forms and conventions the subject demands', 'the formats and styles of writing the subject requires'], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'how the writing meets disciplinary expectations',
                     'options': ['to meet the conventions of the field', 'in line with the standards the subject demands', 'to communicate effectively within the discipline'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Use this to generate an outcome on disciplinary writing. Select an Advanced verb for actively constructing text rather than merely producing it; the object should name the specific forms or genres involved, and the condition should tie the writing to the subject's own standards or conventions."},
            ],
        },
        'forBeneficiary': {
            'template': "You can {verb_1} in the {object_1} your subject needs.",
            'sourceFill': {'verb_1': 'write', 'object_1': 'forms'},
            'slots': [
                _vslot('Advanced', 'the operation of producing text in the forms your subject needs', key='verb_1'),
                {'key': 'object_1', 'role': 'object', 'fill': 'the forms or formats of writing needed',
                 'options': ['forms', 'formats', 'genres'], 'subjectSupplied': False},
            ],
            'agentInstruction': "This formula reproduces the live student-facing version of the written-communication statement exactly. Reuse it by keeping the fixed wording unchanged while substituting verb_1 and object_1 from their option lists; sourceFill holds the live words 'write' and 'forms' only to match the original text.",
            'outcomes': [],
        },
    },
    'reflection-and-personal-development': {
        'forPractitioner': {
            'template': "Graduates {verb_1} on their {object_1} and {verb_2} their development.",
            'sourceFill': {'verb_1': 'reflect', 'object_1': 'learning and practice', 'verb_2': 'plan'},
            'slots': [
                _vslot('Advanced', 'the operation of reflecting on their own learning and practice', key='verb_1'),
                {'key': 'object_1', 'role': 'object', 'fill': 'the learning and practice being reflected on',
                 'options': ['learning and practice', 'learning, practice and reflection', 'study and professional practice'], 'subjectSupplied': False},
                _vslot('Advanced', 'the operation of planning their own future development', key='verb_2'),
            ],
            'agentInstruction': "This formula reproduces the live reflection-and-personal-development statement exactly. Reuse it by keeping the fixed wording unchanged and substituting verb_1, object_1 and verb_2 from their clean option lists; sourceFill holds the live words 'reflect', 'learning and practice' and 'plan' for exact reproduction.",
            'outcomes': [
                {'id': 'reflection-and-personal-development/o1', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', "an Advanced-band verb for critically examining one's own learning and practice"),
                    {'key': 'object', 'role': 'object', 'fill': 'their own learning and practice',
                     'options': ['their own learning and practice', 'how they learn and work', 'their learning processes and professional practice'], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'what the reflection is measured against',
                     'options': ['to identify areas for growth', 'drawing on specific evidence from practice', 'against recognised standards in the field'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Use this to generate an outcome on reflective self-evaluation. Choose an Advanced verb for critically examining one's own learning and practice rather than merely describing it; the condition should specify what evidence or standard the reflection draws on."},
                {'id': 'reflection-and-personal-development/o2', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', 'an Advanced-band verb for constructing a plan for future development'),
                    {'key': 'object', 'role': 'object', 'fill': 'a plan for their own future development',
                     'options': ['a plan for their own development', 'a personal development plan', 'a plan for future learning and practice'], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'what the plan is grounded in',
                     'options': ['based on their own reflection', 'in response to identified learning needs', 'to guide their future practice'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Use this to generate an outcome on development planning. Choose an Advanced verb for actively constructing a plan rather than simply having one; the condition should tie the plan to prior reflection or identified learning needs guiding future practice."},
            ],
        },
        'forBeneficiary': {
            'template': "You can {verb_1} on how you {object_1}, and {verb_2} how to improve.",
            'sourceFill': {'verb_1': 'reflect', 'object_1': 'learn and work', 'verb_2': 'plan'},
            'slots': [
                _vslot('Advanced', 'the operation of reflecting on how they learn and work', key='verb_1'),
                {'key': 'object_1', 'role': 'object', 'fill': 'how they learn and work',
                 'options': ['learn and work', 'study and work', 'learn and practice'], 'subjectSupplied': False},
                _vslot('Advanced', 'the operation of planning how to improve', key='verb_2'),
            ],
            'agentInstruction': "This formula reproduces the live student-facing version of the reflection statement exactly. Reuse it by keeping the fixed wording unchanged and substituting verb_1, object_1 and verb_2 from their clean option lists; sourceFill holds the live words 'reflect', 'learn and work' and 'plan' for exact reproduction.",
            'outcomes': [],
        },
    },
    'equality': {
        'forPractitioner': {
            'template': "Graduates {verb_1} {object_1} as they bear on the subject.",
            'sourceFill': {'verb_1': 'recognise', 'object_1': 'diversity and inclusion'},
            'slots': [
                _vslot('Advanced', 'the operation of recognising diversity and inclusion as they bear on the subject', key='verb_1'),
                {'key': 'object_1', 'role': 'object', 'fill': 'diversity and inclusion as a bundled concept',
                 'options': ['diversity and inclusion', 'equality and inclusion', 'diverse and inclusive practice'], 'subjectSupplied': False},
            ],
            'agentInstruction': "This formula reproduces the live equality statement exactly. Reuse it by keeping the fixed wording unchanged and substituting verb_1 and object_1 from their clean option lists; sourceFill holds the live words 'recognise' and 'diversity and inclusion' for exact text reproduction.",
            'outcomes': [
                {'id': 'equality/o1', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', 'an Advanced-band verb for critically evaluating diversity and inclusion issues within the subject'),
                    {'key': 'object', 'role': 'object', 'fill': 'diversity and inclusion as they relate to the subject',
                     'options': ['diversity and inclusion', 'equality and inclusion issues', 'diverse perspectives and inclusive practice'], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'how the issues are situated in the subject',
                     'options': ['as they bear on the subject', 'within the context of the field', 'in relation to current practice in the subject'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': "Use this to generate an outcome on equality and inclusion. Choose an Advanced verb for critically evaluating diversity and inclusion issues rather than merely recognising them; the condition should situate the evaluation within the subject's own context or current practice."},
            ],
        },
        'forBeneficiary': {
            'template': "You {verb_1} how {object_1} matter in your subject.",
            'sourceFill': {'verb_1': 'understand', 'object_1': 'diversity and inclusion'},
            'slots': [
                _vslot('Advanced', "the operation of critically engaging with how diversity and inclusion matter in the subject, though the live text uses the banned verb 'understand'", key='verb_1'),
                {'key': 'object_1', 'role': 'object', 'fill': 'diversity and inclusion as a bundled concept',
                 'options': ['diversity and inclusion', 'equality and inclusion', 'diverse and inclusive practice'], 'subjectSupplied': False},
            ],
            'agentInstruction': "This formula reproduces the live student-facing version of the equality statement exactly. Reuse it by keeping the fixed wording unchanged while substituting verb_1 from a clean Advanced-band verb list; sourceFill retains the live banned verb 'understand' only to match the original text.",
            'outcomes': [],
        },
    },
    'enterprise-and-creativity': {
        'forPractitioner': {
            'template': "Graduates {verb_1} {object_1} in applying the subject.",
            'sourceFill': {'verb_1': 'show', 'object_1': 'creativity and enterprise'},
            'slots': [
                _vslot('Advanced', 'the operation of showing creativity and enterprise in applying the subject', key='verb_1'),
                {'key': 'object_1', 'role': 'object', 'fill': 'creativity and enterprise as a bundled concept',
                 'options': ['creativity and enterprise', 'originality and enterprise', 'inventiveness and entrepreneurial flair'], 'subjectSupplied': False},
            ],
            'agentInstruction': "This formula reproduces the live enterprise-and-creativity statement exactly. Reuse it by keeping the fixed wording unchanged and substituting verb_1 and object_1 from their clean option lists; sourceFill holds the live words 'show' and 'creativity and enterprise' for exact text reproduction.",
            'outcomes': [
                {'id': 'enterprise-and-creativity/o1', 'template': "{verb} {object}, {condition}.",
                 'slots': [
                    _vslot('Advanced', 'an Advanced-band verb for constructing original or enterprising responses when applying the subject'),
                    {'key': 'object', 'role': 'object', 'fill': 'creative and enterprising solutions',
                     'options': ['creative and enterprising solutions', 'original and enterprising approaches', 'inventive and entrepreneurial responses'], 'subjectSupplied': False},
                    {'key': 'condition', 'role': 'condition', 'fill': 'the situation the subject is being applied to',
                     'options': ['when applying the subject to new situations', 'in response to real-world challenges in the field', 'to address unfamiliar problems in the subject'], 'subjectSupplied': False},
                 ],
                 'agentInstruction': 'Use this to generate an outcome on enterprise and creativity. Choose an Advanced verb for actively constructing original or enterprising responses rather than merely showing them; the condition should specify the unfamiliar situation or challenge the subject is applied to.'},
            ],
        },
        'forBeneficiary': {
            'template': "You can {verb_1} {object_1} in how you use your subject.",
            'sourceFill': {'verb_1': 'be', 'object_1': 'creative and enterprising'},
            'slots': [
                _vslot('Advanced', 'the operation of being creative and enterprising in how the subject is used', key='verb_1'),
                {'key': 'object_1', 'role': 'object', 'fill': 'being creative and enterprising as a bundled concept',
                 'options': ['creative and enterprising', 'original and enterprising', 'inventive and entrepreneurial'], 'subjectSupplied': False},
            ],
            'agentInstruction': "This formula reproduces the live student-facing version of the enterprise-and-creativity statement exactly. Reuse it by keeping the fixed wording unchanged while substituting verb_1 and object_1 from their clean option lists; sourceFill holds the live words 'be' and 'creative and enterprising' for exact reproduction.",
            'outcomes': [],
        },
    },
}


COMPETENCY_FORMULAS = {}
COMPETENCY_FORMULAS.update(GROUP_A)
COMPETENCY_FORMULAS.update(GROUP_B)
COMPETENCY_FORMULAS.update(GROUP_C)
COMPETENCY_FORMULAS.update(GROUP_D)



# Pathway-concept hints: match a pathway's canonical name + tier focus (the short
# text in design-kb.pathways.json) to the shared-core concepts it most directly
# realises. Distinct from the statement-level rule C above; tuned for the pathway
# vocabulary. Used to author a generic, subject-neutral pathwayMapping so the
# baseline matches a subject benchmark's shape.
PATHWAY_MATCH = {
 'subject knowledge and understanding': r'knowledge|understand|learning',
 'theories, concepts and debates': r'theor|concept|debate',
 'history, context and currency of the field': r'histor|context|contemporary|current',
 'critical evaluation of evidence and arguments': r'critical|evaluat|argument|judg|apprais',
 'analysis and problem-solving': r'analys|problem|reason',
 'research and enquiry methods': r'research|enquiry|inquiry|investigat|\bmethod',
 'data, numbers and quantitative reasoning': r'\bdata\b|quantitative|numer|statistic',
 'applying knowledge to practice or problems': r'\bappl|practi(c|s)e|practical|work-based|experient',
 'information and sources': r'source|literature|informatio|referenc|\bcit',
 'digital skills': r'digital|software|technolog|\bai\b|comput',
 'written communication': r'\bwrit|essay|\breport',
 'oral or other communication to audiences': r'present|audience|oral|speak|communicat',
 'teamwork and collaboration': r'team|collaborat|group',
 'independent and self-directed learning': r'independen|self-direct|autonom|manag|succeed|progress|start',
 'reflection and personal development': r'reflect|personal development|self-aware|revis',
 'ethics, integrity and values': r'ethic|integrity|values|responsib',
 'professional practice and employability': r'professional|employab|career|workplace|work-based',
 'equality, diversity and inclusion': r'diversity|inclusi|equalit|equity',
 'sustainability': r'sustainab|environmental',
 'enterprise and creativity': r'enterpris|entrepreneur|creativ|innovat',
}
# Shared-core expectations that apply to any university learning: carried by every
# pathway as `indirect` where not already a direct match (a sensible floor).
ALWAYS_INDIRECT = [
 'subject knowledge and understanding',
 'critical evaluation of evidence and arguments',
 'independent and self-directed learning',
 'ethics, integrity and values',
 'oral or other communication to audiences',
]
# Expectations whose realisation leans professional rather than academic.
PRO_ORIENT = {
 'applying knowledge to practice or problems',
 'professional practice and employability',
 'enterprise and creativity',
}
RUNGS = ('threshold', 'typical', 'excellent')


def slugify(concept):
    return concept.split(',')[0].replace(' ', '-')


def build_pathway_mapping(order):
    """Author a generic pathwayMapping: each of the 13 pathways -> the shared-core
    expectations it realises, mirroring a subject benchmark's shape but staying
    subject-neutral. Grounded in design-kb/design-kb.pathways.json (names + tier
    focuses); not averaged from the 54 (only one subject carries a real map)."""
    path = os.path.join(REPO_ROOT, 'design-kb', 'design-kb.pathways.json')
    pd = json.load(open(path, encoding='utf-8'))
    mapping = {}
    for p in pd.get('pathways', []):
        tiers = p.get('tiers')
        foci = []
        if isinstance(tiers, dict):
            foci = [t.get('focus', '') for t in tiers.values() if isinstance(t, dict)]
        elif isinstance(tiers, list):
            foci = [t.get('focus', '') for t in tiers if isinstance(t, dict)]
        text = (p.get('name', '') + ' ' + ' '.join(foci)).lower()
        direct = [k for k in order if re.search(PATHWAY_MATCH[k], text)]
        indirect = [k for k in ALWAYS_INDIRECT if k not in direct]
        stmts = []
        for k in direct + indirect:
            strength = 'direct' if k in direct else 'indirect'
            tiers, basis = pathway_tiers.key_tiers('adapt-' + p['id'], strength,
                                                   pattern=PATHWAY_MATCH[k])
            stmts.append({
                'chunkId': 'qaa-universal/threshold/' + slugify(k),
                'tag': 'adapt-' + p['id'],
                'strength': strength,
                'tiers': tiers,
                'tierBasis': basis,
                'extract': EXP[k][0],
                'orientation': 'professional' if k in PRO_ORIENT else 'academic',
                'blockType': 'baseline',
                'agentInstruction': EXPINSTR[k],
                'status': 'drafted',
            })
        short = ', '.join(k.split(',')[0] for k in direct) or 'the shared core'
        mapping['adapt-' + p['id']] = {
            'coverage': {'direct': len(direct), 'indirect': len(indirect)},
            'summary': {'text': (
                'At baseline, the ' + p.get('name', '').strip() + ' pathway realises '
                'the shared-core expectations of ' + short + ', pitched to the tier via '
                'tierReadings. Keep examples subject-neutral (the Student A / Student B '
                'cast); a real subject benchmark, where one exists, overrides this '
                'generic mapping.')},
            'statements': stmts,
        }
    return mapping


def aggregate():
    files = sorted(glob.glob(SRC_GLOB))
    files = [f for f in files if os.path.basename(f) != 'universal-reference.json']
    docs = {r: collections.defaultdict(set) for r in RUNGS}
    anyr = collections.defaultdict(set)
    grounds = collections.defaultdict(lambda: collections.defaultdict(list))
    for f in files:
        d = json.load(open(f, encoding='utf-8'))
        slug = d['subjectBenchmarkId']
        for s in d.get('statements') or []:
            rung = s.get('rung')
            text = ' '.join([
                str(s.get('about') or ''), str(s.get('paraphrase') or ''),
                ' '.join(s.get('verbs') or []),
                ' '.join(t for t in (s.get('themes') or []) if t != 'none'),
            ]).lower()
            for k, (st, rx) in C.items():
                if re.search(rx, text):
                    anyr[k].add(slug)
                    if rung in RUNGS:
                        docs[rung][k].add(slug)
                        if len(grounds[k][rung]) < 4:
                            grounds[k][rung].append(slug + ':' + s['id'].split('/')[-1])
    return len(files), docs, anyr, grounds


def build():
    n, docs, anyr, grounds = aggregate()
    order = sorted(C, key=lambda k: (-len(docs['threshold'][k]), -len(anyr[k]), k))

    statements = []
    for k in order:
        t = len(docs['threshold'][k]); ty = len(docs['typical'][k])
        e = len(docs['excellent'][k]); a = len(anyr[k])
        p, s = EXP[k]
        statements.append({
            'id': 'qaa-universal/threshold/' + slugify(k),
            'statementType': 'threshold', 'rung': 'threshold', 'level': 'fheq:6',
            'force': 'will', 'appliesTo': 'graduates at the threshold level',
            'about': k, 'strand': SN[C[k][0]], 'domain': DOMAIN[C[k][0]],
            'paraphrase': p,
            'sharedBy': {'threshold': t, 'typical': ty, 'excellent': e, 'any': a, 'of': n},
            'core': a * 2 >= n, 'basis': 'inferred', 'status': 'drafted',
            'agentInstruction': EXPINSTR[k],
            'audienceVersions': {
                'forPractitioner': {'text': p, 'status': 'drafted',
                                    'forEducator': {'text': TUTOR_ADVICE[k], 'status': 'drafted'}},
                'forBeneficiary': {'text': s, 'status': 'drafted',
                                   'forLearnerGuidance': {'text': STUDENT_ADVICE[k], 'status': 'drafted'}},
            },
            'groundingSample': grounds[k].get('threshold', []),
        })
    # the climb above threshold (the successful student), universal tier
    statements.append({
        'id': 'qaa-universal/typical/climb', 'statementType': 'typical', 'rung': 'typical',
        'level': 'fheq:6', 'about': 'the typical standard (most graduates)',
        'strand': 'strand:all', 'basis': 'inferred', 'status': 'drafted',
        'agentInstruction': 'Realise the typical standard as more of the work being critical and independent and the knowledge wider and more current. It is the same tasks done better, not new tasks; pitch to the intermediate tier reading.',
        'paraphrase': "Typically, more of the graduate's work is critical and independent, and their knowledge is wider and more current.",
        'audienceVersions': {
            'forPractitioner': {'text': "Typically, more of the graduate's work is critical and independent, and their knowledge is wider and more current.", 'status': 'drafted',
                                'forEducator': {'text': CLIMB_ADVICE['typical']['educator'], 'status': 'drafted'}},
            'forBeneficiary': {'text': 'At the typical standard, more of what you do is critical and independent, and you know more of what is current.', 'status': 'drafted',
                               'forLearnerGuidance': {'text': CLIMB_ADVICE['typical']['learner'], 'status': 'drafted'}},
        },
    })
    statements.append({
        'id': 'qaa-universal/excellent/climb', 'statementType': 'excellent', 'rung': 'excellent',
        'level': 'fheq:6', 'about': 'the excellent standard (the successful student)',
        'strand': 'strand:all', 'basis': 'inferred', 'status': 'drafted',
        'agentInstruction': 'Realise excellence as sustained criticality and independence with some originality; reserve "exceptional" framing for the top. Still the same tasks, carried higher; pitch to the advanced tier reading.',
        'paraphrase': 'At excellent, work is critical and independent throughout, shows some originality, and is described as exceptional.',
        'audienceVersions': {
            'forPractitioner': {'text': 'At excellent, work is critical and independent throughout, shows some originality, and is described as exceptional.', 'status': 'drafted',
                                'forEducator': {'text': CLIMB_ADVICE['excellent']['educator'], 'status': 'drafted'}},
            'forBeneficiary': {'text': 'At the excellent standard, you are critical and independent throughout, show some original thinking, and your work stands out.', 'status': 'drafted',
                               'forLearnerGuidance': {'text': CLIMB_ADVICE['excellent']['learner'], 'status': 'drafted'}},
        },
    })

    # Graduate-competency layer: a flat, subject-neutral projection of the
    # threshold shared-core statements, for reuse as baseline context. Onboarding
    # / CXP may offer these (if the user wishes) as an opt-in subset of the
    # qualifier list, default none. House term: graduate competency / graduate
    # skill / graduate attribute / academic practice (never "academic skills").
    pm = build_pathway_mapping(order)
    def _gc_title(a):
        a = (a or '').strip()
        return (a[:1].upper() + a[1:]) if a else a
    def _gc_pathways(stmt_id):
        """Which academic-practice pathways this competency keys into (from pathwayMapping)."""
        out = []
        for _pwk, _pw in pm.items():
            for _st in (_pw.get('statements') or []):
                if _st.get('chunkId') == stmt_id:
                    out.append({'pathway': _pwk, 'strength': _st.get('strength'),
                                'tiers': [t['tier'] for t in _st.get('tiers') or []],
                                'tierBasis': _st.get('tierBasis')})
                    break
        return out
    grad_competencies = []
    for _s in statements:
        if _s.get('rung') != 'threshold':
            continue
        _av = (_s.get('audienceVersions') or {}).get('forBeneficiary') or {}
        _sb = _s.get('sharedBy') or {}
        grad_competencies.append({
            'id': _s['id'].split('/')[-1],
            'label': _gc_title(_s.get('about')),
            'strand': (_s.get('strand') or '').replace('strand:', ''),
            'graduateStatement': _s.get('paraphrase', ''),
            'studentStatement': _av.get('text', ''),
            'sharedBy': {'threshold': _sb.get('threshold', 0), 'of': _sb.get('of', n)},
            'core': bool(_s.get('core')),
            'pathways': _gc_pathways(_s['id']),
            'statementId': _s['id'],
            'formula': {'registers': COMPETENCY_FORMULAS.get(_s['id'].split('/')[-1])},
        })

    doc = {
        'subjectBenchmarkId': 'universal-reference',
        'subject': {
            'name': 'Universal (shared core of the QAA subject benchmark statements)',
            'codes': [],
        },
        'issuer': 'QAA (distilled across the subject benchmark statements)',
        'title': 'Universal reference benchmark: the shared core of the QAA subject benchmark statements',
        'edition': 'derived ' + datetime.date.today().isoformat(),
        'published': datetime.date.today().isoformat(),
        'status': 'draft',
        'levelsCovered': ['fheq:6'],
        'awardsCovered': ["bachelor's with honours"],
        'nations': ['UK'],
        'source': {
            'ingestId': 'std:ref:qaa-universal-benchmark',
            'licence': 'Distillation across the QAA Subject Benchmark Statements; QAA copyright is held, no issuer text is copied; all wording here is our paraphrase or audience rewrite.',
            'ingestDoc': {
                'repo': 'wkspc2614-adapt',
                'path': 'source-kb/canon-adp/secondary-data/ingested/standards/ingest-std-qaa-universal-reference-benchmark/ingest-std-qaa-universal-reference-benchmark.md',
                'note': 'The prose reference this structured sibling is derived from.',
            },
            'derivedFrom': {
                'method': 'Shared-core aggregation across the catalogue per-subject benchmark JSONs; 20-concept / 5-strand keyword rule on each statement about+paraphrase+verbs+themes; sharedBy = subjects with at least one matching statement per rung, out of the whole set.',
                'pathwayMappingBasis': 'Authored, not averaged: each pathway in design-kb/design-kb.pathways.json is mapped to the shared-core expectations it realises, by its name + tier focus. Generic and subject-neutral; only one of the subject benchmarks carries a real pathway map, so this cannot be averaged. Each edge is keyed to pathway + tier by tools/pathway_tiers.py (tierBasis: capability-match | progression | floor).',
                'script': 'tools/build-universal-benchmark.py',
                'generated': datetime.date.today().isoformat(),
                'sourceFiles': n,
            },
        },
        'tierReadings': {
            'rows': [
                {
                    'rowId': 'u-intro', 'tier': 'introductory', 'fheqLevel': 4,
                    'practice': "Begins to apply the subject's basic methods to familiar, well-defined tasks with guidance, works with sources and data they are given, and communicates straightforward findings clearly.",
                    'knowledge': 'Knows the core terms, ideas and principles that introduce the subject, and can place them in the wider field.',
                    'identity': 'Begins to connect practice, theory and reflection for the first time, following guidance on ethical and academic conduct as an early sense of the kind of practitioner they are becoming.',
                    'groundingIds': [],
                    'pitchNote': 'Pedagogical down-pitch toward the shared core for an introductory (FHEQ level 4) audience. QAA benchmarks define only the honours graduate at level 6, so this reading is ours, not an issuer standard.',
                    'formulas': TIER_READING_FORMULAS['u-intro'],
                },
                {
                    'rowId': 'u-int', 'tier': 'intermediate', 'fheqLevel': 6,
                    'practice': "Applies the subject's methods to questions and problems, carries out supervised research and enquiry, works with data and sources, and communicates findings to different audiences.",
                    'knowledge': 'Knows the core content, main theories and debates of the subject, and how the field developed and where it currently stands.',
                    'identity': 'Works ethically and increasingly independently, treating practitioner identity as still forming rather than fixed, shaped by reflection on their own learning and by how diversity, sustainability and professional practice bear on the subject.',
                    'groundingIds': [],
                    'formulas': TIER_READING_FORMULAS['u-int'],
                },
                {
                    'rowId': 'u-adv', 'tier': 'advanced', 'fheqLevel': 6,
                    'practice': 'Designs and critiques enquiry across methods, evaluates evidence and arguments critically throughout, and applies knowledge to current and complex problems with some originality.',
                    'knowledge': 'Commands the breadth and depth of the subject, its theoretical foundations and their bearing on current thinking, and sees where understanding runs out.',
                    'identity': 'A reflexive practitioner who examines how their own position, assumptions and values shape their judgements, weighs what this means for wider debate and for audiences acting on it, and treats their professional identity as still evolving through that scrutiny.',
                    'groundingIds': [],
                    'formulas': TIER_READING_FORMULAS['u-adv'],
                },
            ],
            'note': 'Benchmarks set standards for the honours graduate (FHEQ level 6); the intermediate and advanced rows synthesise that shared core across the statements. The introductory (FHEQ level 4) row is a pedagogical down-pitch toward the same core, marked with its own pitchNote - the benchmarks do not themselves speak at level 4. Our words, no issuer text.',
            'source': {'script': 'tools/build-universal-benchmark.py', 'note': 'Universal synthesis, not a per-subject card.'},
        },
        'themes': [
            {'id': 'theme:accessibility', 'role': 'carries', 'note': 'an accessibility sub-section appears in section 1 of all statements'},
            {'id': 'theme:esd', 'alias': 'sustainability', 'role': 'carries',
             'sharedBy': len(anyr['sustainability']), 'note': 'a sustainability sub-section in all statements; the shared-core sustainability expectation is carried this widely'},
            {'id': 'theme:edi', 'role': 'carries', 'sharedBy': len(anyr['equality, diversity and inclusion']),
             'note': 'an EDI sub-section in most statements'},
            {'id': 'theme:enterprise', 'role': 'carries', 'sharedBy': len(anyr['enterprise and creativity']),
             'note': 'an enterprise sub-heading in a minority of statements; treated without the heading in the rest'},
        ],
        'digest': {
            'definition': 'The shared core of the QAA Subject Benchmark Statements: what an honours graduate is expected to know, do and be on graduating, whatever the subject.',
            'distinctiveFeatures': [
                'Subjects differ in the matter their graduates act on, not in the shape of the expectation: the same verbs and rungs recur across the statements.',
                'At threshold, most subjects ask for the same core: subject knowledge, theories, critical evaluation, analysis, research methods, application, communication, teamwork, independence and ethics.',
                "The rungs climb by qualifiers, not new verbs: 'critical', 'independent' and 'original' mark the typical and excellent standards above threshold.",
                'Ethical, professional and digital expectations sit at the threshold: they are baseline, not marks of excellence.',
            ],
            'standards': {
                'rungs': [
                    {'rung': 'threshold', 'award': "bachelor's with honours", 'note': 'the minimum every honours graduate shows; spine:6'},
                    {'rung': 'typical', 'note': 'what most graduates show'},
                    {'rung': 'excellent', 'note': 'the best performance'},
                ],
                'rungBases': 'Typical and excellent go beyond threshold by depth and breadth of knowledge, engagement in research and independent study, critical insight, and advanced application of theory and method.',
            },
        },
        'statements': statements,
        'graduate_competency': {
            'note': 'Flat, subject-neutral projection of the threshold shared-core statements as graduate competencies, for reuse as baseline context. Onboarding/CXP may offer these (if the user wishes) as an opt-in subset of the qualifier list (design-kb cxp-02_qualifiers), default none. House term: graduate competency / graduate skill / graduate attribute / academic practice - never "academic skills".',
            'terms': ['graduate competency', 'graduate skill', 'graduate attribute', 'academic practice'],
            'qualifierCategory': 'graduate-competency',
            'items': grad_competencies,
        },
        'pathwayMapping': pm,
        'mapAgentInstructions': [
            'Universal baseline reference: pathwayMapping here is generic and subject-neutral (authored from design-kb.pathways.json), not a real per-subject map. Build a baseline pack from the pathway\'s mapped shared-core expectations plus tierReadings, honouring each expectation\'s agentInstruction.',
            'Select, do not cram: pick the expectations whose strand fits the pathway being built (e.g. criticality -> strand:thinking; finding-using-sources -> information and sources; presenting -> communication). Core expectations (sharedBy at least half of the set) carry the framing; low-count ones support.',
            'Pitch by tier using tierReadings (intermediate vs advanced practice/knowledge/identity) and the pathway\'s own tier voiceBand / teachingProsePointer in catalogue/context/pathways/<pathway>.json. Benchmarks speak at the honours-graduate end, so lean on these for intermediate/advanced and pitch down for introductory.',
            'Invent no subject-specific content at baseline: keep examples neutral (use "your subject" and the Student A / Student B cast). A real subject benchmark, where one exists for the subject, overrides this baseline.',
            'The rungs climb by qualifiers, not new verbs: realise typical/excellent (statements qaa-universal/typical|excellent/climb) as more critical, more independent and some originality, not as different tasks.',
        ],
        'statementFormulas': STATEMENT_FORMULAS_GRAMMAR,
    }
    return doc


def _strand_label(s):
    """'strand:knowledge' -> 'Knowledge'; 'strand:all' -> 'All'."""
    return (s or '').replace('strand:', '').replace('-', ' ').strip().capitalize() or '-'


def _cell(s):
    """A table cell: no raw pipes, no line breaks."""
    return str(s or '').replace('|', '\\|').replace('\n', ' ').strip()


def _render_formula_lines(label, formula, indent='  '):
    """One statement formula (template + sourceFill) plus its outcome
    formulas, as a short bullet block. Braces are safe in Markdown, so the
    template renders as-written."""
    if not formula:
        return []
    tmpl = formula.get('template', '')
    fill = ', '.join('%s=%s' % (k, v) for k, v in (formula.get('sourceFill') or {}).items())
    lines = [indent + '- **' + label + ' formula:** `' + tmpl + '` (fill: ' + fill + ')']
    for oc in formula.get('outcomes') or []:
        lines.append(indent + '  - `' + oc.get('id', '') + '`: ' + oc.get('template', ''))
    return lines


def render_markdown(doc):
    """Render the built universal benchmark as a readable Markdown sibling.

    Same content as the JSON, laid out for a person (or an authoring agent) to
    read: the definition, the standard and how it climbs, each shared-core
    expectation with its graduate and student wording, the tier readings, and
    how the 13 pathways draw on it. Provenance sits in a footer. No issuer text;
    our paraphrase and audience rewrites only."""
    src = doc.get('source', {})
    dv = src.get('derivedFrom', {})
    n = dv.get('sourceFiles', '?')
    L = []
    L.append('# ' + doc['title'])
    L.append('')
    L.append('> ' + doc['digest']['definition'])
    L.append('')
    L.append('*' + ' · '.join([
        'Edition: ' + str(doc.get('edition', '')),
        'FHEQ level 6 (honours graduate)',
        'Derived from ' + str(n) + ' subject benchmark statements',
    ]) + '*')
    L.append('')

    feats = doc['digest'].get('distinctiveFeatures') or []
    if feats:
        L.append('## What the shared core is')
        L.append('')
        L.extend('- ' + f for f in feats)
        L.append('')

    std = doc['digest'].get('standards', {})
    rungs = std.get('rungs') or []
    if rungs:
        L.append('## The standard and how it climbs')
        L.append('')
        for r in rungs:
            bits = '; '.join(b for b in (r.get('award'), r.get('note')) if b)
            L.append('- **' + r['rung'] + '**' + (': ' + bits if bits else ''))
        if std.get('rungBases'):
            L.append('')
            L.append(std['rungBases'])
        L.append('')

    expectations = [s for s in doc['statements'] if s.get('statementType') == 'threshold']
    climbs = [s for s in doc['statements'] if s.get('statementType') in ('typical', 'excellent')]
    comp_by_stmt = {it.get('statementId'): it for it in (doc.get('graduate_competency') or {}).get('items') or []}

    L.append('## Shared-core expectations (threshold)')
    L.append('')
    L.append('Each is what an honours graduate is expected to show, whatever the '
             'subject. "Shared by" counts how many of the ' + str(n) + ' subject '
             'benchmarks carry it.')
    L.append('')
    for i, s in enumerate(expectations, 1):
        sb = s.get('sharedBy', {})
        av = s.get('audienceVersions', {})
        L.append('### ' + str(i) + '. ' + (s.get('about') or s['id']).capitalize())
        tags = ['Strand: ' + _strand_label(s.get('strand'))]
        if sb:
            tags.append('Shared by ' + str(sb.get('threshold', '?')) + '/' + str(sb.get('of', '?'))
                        + ' at threshold (' + str(sb.get('any', '?')) + '/' + str(sb.get('of', '?'))
                        + ' at any rung)')
        if s.get('core'):
            tags.append('core')
        L.append('*' + ' · '.join(tags) + '*')
        L.append('')
        pr = av.get('forPractitioner') or {}
        bn = av.get('forBeneficiary') or {}
        gr = pr.get('text') or s.get('paraphrase')
        be = bn.get('text')
        ed = (pr.get('forEducator') or {}).get('text')
        lg = (bn.get('forLearnerGuidance') or {}).get('text')
        if gr:
            L.append('- **Graduate:** ' + gr)
        if ed:
            L.append('- **Tutor advice:** ' + ed)
        if be:
            L.append('- **Student:** ' + be)
        if lg:
            L.append('- **Student advice:** ' + lg)
        if s.get('agentInstruction'):
            L.append('- **Authoring note:** ' + s['agentInstruction'])
        comp_item = comp_by_stmt.get(s['id'])
        regs = ((comp_item or {}).get('formula') or {}).get('registers') or {}
        if regs.get('forPractitioner'):
            L.extend(_render_formula_lines('Graduate', regs['forPractitioner']))
        if regs.get('forBeneficiary'):
            L.extend(_render_formula_lines('Student', regs['forBeneficiary']))
        L.append('')

    if climbs:
        L.append('## Above threshold')
        L.append('')
        for s in climbs:
            av = s.get('audienceVersions', {})
            pr = av.get('forPractitioner') or {}
            bn = av.get('forBeneficiary') or {}
            L.append('### ' + (s.get('about') or s['id']))
            gr = pr.get('text') or s.get('paraphrase')
            be = bn.get('text')
            ed = (pr.get('forEducator') or {}).get('text')
            lg = (bn.get('forLearnerGuidance') or {}).get('text')
            if gr:
                L.append('- **Graduate:** ' + gr)
            if ed:
                L.append('- **Tutor advice:** ' + ed)
            if be:
                L.append('- **Student:** ' + be)
            if lg:
                L.append('- **Student advice:** ' + lg)
            if s.get('agentInstruction'):
                L.append('- **Authoring note:** ' + s['agentInstruction'])
            L.append('')

    tr = doc.get('tierReadings', {})
    rows = tr.get('rows') or []
    if rows:
        L.append('## Tier readings')
        L.append('')
        L.append('| Tier | FHEQ | Practice | Knowledge | Identity |')
        L.append('|---|---|---|---|---|')
        for r in rows:
            L.append('| ' + ' | '.join([
                _cell(r.get('tier')), _cell(r.get('fheqLevel')),
                _cell(r.get('practice')), _cell(r.get('knowledge')), _cell(r.get('identity')),
            ]) + ' |')
        L.append('')
        for r in rows:
            formulas = r.get('formulas') or {}
            if not formulas:
                continue
            L.append('**' + _cell(r.get('rowId') or r.get('tier')) + ' formulas:**')
            L.append('')
            for field in ('practice', 'knowledge', 'identity'):
                L.extend(_render_formula_lines(field, formulas.get(field), indent=''))
            L.append('')
        if tr.get('note'):
            L.append(tr['note'])
            L.append('')

    pm = doc.get('pathwayMapping', {})
    if pm:
        L.append('## How the pathways use the shared core')
        L.append('')
        for key, body in pm.items():
            cov = body.get('coverage', {})
            head = '**' + key.replace('adapt-', '') + '**'
            if cov:
                head += ' (direct ' + str(cov.get('direct', 0)) + ', indirect ' + str(cov.get('indirect', 0)) + ')'
            summ = (body.get('summary') or {}).get('text', '')
            L.append('- ' + head + (': ' + summ if summ else ''))
        L.append('')

    mai = doc.get('mapAgentInstructions') or []
    if mai:
        L.append('## Using this as grounding')
        L.append('')
        L.extend('- ' + m for m in mai)
        L.append('')

    L.append('---')
    L.append('')
    L.append('## Provenance')
    L.append('')
    if dv.get('method'):
        L.append('- **Method:** ' + dv['method'])
    if dv.get('pathwayMappingBasis'):
        L.append('- **Pathway mapping:** ' + dv['pathwayMappingBasis'])
    L.append('- **Built by:** `' + dv.get('script', 'tools/build-universal-benchmark.py')
             + '` on ' + str(dv.get('generated', '')))
    if src.get('licence'):
        L.append('- **Licence:** ' + src['licence'])
    L.append('')
    return '\n'.join(L)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(
        description='Collate the generic (universal) benchmark from the per-subject set.')
    ap.add_argument('--format', choices=('json', 'md', 'yaml', 'both', 'all'), default='both',
                    help="which sibling(s) to write: json, md, yaml, both (json+md, default) or all")
    args = ap.parse_args()

    doc = build()
    wrote = []
    if args.format in ('json', 'both', 'all'):
        with open(OUT, 'w', encoding='utf-8') as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=2)
            fh.write('\n')
        wrote.append(os.path.relpath(OUT, REPO_ROOT))
    if args.format in ('md', 'both', 'all'):
        with open(OUT_MD, 'w', encoding='utf-8') as fh:
            fh.write(render_markdown(doc))
            fh.write('\n')
        wrote.append(os.path.relpath(OUT_MD, REPO_ROOT))
    if args.format in ('yaml', 'all'):
        try:
            import yaml
        except ImportError:
            print('skipped YAML: PyYAML not installed (pip install pyyaml)')
        else:
            with open(OUT_YAML, 'w', encoding='utf-8') as fh:
                yaml.safe_dump(doc, fh, allow_unicode=True, sort_keys=False,
                               default_flow_style=False, width=100)
            wrote.append(os.path.relpath(OUT_YAML, REPO_ROOT))

    for w in wrote:
        print('wrote', w)
    print('statements:', len(doc['statements']), '| sourceFiles:', doc['source']['derivedFrom']['sourceFiles'])
