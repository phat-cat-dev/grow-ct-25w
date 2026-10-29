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

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_GLOB = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks', '*.json')
OUT = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks', 'universal-reference.json')
OUT_MD = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks', 'universal-reference.md')
OUT_YAML = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks', 'universal-reference.yaml')

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
            stmts.append({
                'chunkId': 'qaa-universal/threshold/' + slugify(k),
                'tag': 'adapt-' + p['id'],
                'strength': 'direct' if k in direct else 'indirect',
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
    def _gc_title(a):
        a = (a or '').strip()
        return (a[:1].upper() + a[1:]) if a else a
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
            'statementId': _s['id'],
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
                'pathwayMappingBasis': 'Authored, not averaged: each pathway in design-kb/design-kb.pathways.json is mapped to the shared-core expectations it realises, by its name + tier focus. Generic and subject-neutral; only one of the subject benchmarks carries a real pathway map, so this cannot be averaged.',
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
                    'identity': 'Works honestly and responsibly, follows guidance on ethical and academic conduct, and begins to reflect on their own learning.',
                    'groundingIds': [],
                    'pitchNote': 'Pedagogical down-pitch toward the shared core for an introductory (FHEQ level 4) audience. QAA benchmarks define only the honours graduate at level 6, so this reading is ours, not an issuer standard.',
                },
                {
                    'rowId': 'u-int', 'tier': 'intermediate', 'fheqLevel': 6,
                    'practice': "Applies the subject's methods to questions and problems, carries out supervised research and enquiry, works with data and sources, and communicates findings to different audiences.",
                    'knowledge': 'Knows the core content, main theories and debates of the subject, and how the field developed and where it currently stands.',
                    'identity': 'Works ethically and increasingly independently, reflects on their own learning, and recognises how diversity, sustainability and professional practice bear on the subject.',
                    'groundingIds': [],
                },
                {
                    'rowId': 'u-adv', 'tier': 'advanced', 'fheqLevel': 6,
                    'practice': 'Designs and critiques enquiry across methods, evaluates evidence and arguments critically throughout, and applies knowledge to current and complex problems with some originality.',
                    'knowledge': 'Commands the breadth and depth of the subject, its theoretical foundations and their bearing on current thinking, and sees where understanding runs out.',
                    'identity': 'A reflective, ethical and independent practitioner who weighs what findings mean for wider debate and helps varied audiences act on them.',
                    'groundingIds': [],
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
        'pathwayMapping': build_pathway_mapping(order),
        'mapAgentInstructions': [
            'Universal baseline reference: pathwayMapping here is generic and subject-neutral (authored from design-kb.pathways.json), not a real per-subject map. Build a baseline pack from the pathway\'s mapped shared-core expectations plus tierReadings, honouring each expectation\'s agentInstruction.',
            'Select, do not cram: pick the expectations whose strand fits the pathway being built (e.g. criticality -> strand:thinking; finding-using-sources -> information and sources; presenting -> communication). Core expectations (sharedBy at least half of the set) carry the framing; low-count ones support.',
            'Pitch by tier using tierReadings (intermediate vs advanced practice/knowledge/identity) and the pathway\'s own tier voiceBand / teachingProsePointer in catalogue/pathways/<pathway>.json. Benchmarks speak at the honours-graduate end, so lean on these for intermediate/advanced and pitch down for introductory.',
            'Invent no subject-specific content at baseline: keep examples neutral (use "your subject" and the Student A / Student B cast). A real subject benchmark, where one exists for the subject, overrides this baseline.',
            'The rungs climb by qualifiers, not new verbs: realise typical/excellent (statements qaa-universal/typical|excellent/climb) as more critical, more independent and some originality, not as different tasks.',
        ],
    }
    return doc


def _strand_label(s):
    """'strand:knowledge' -> 'Knowledge'; 'strand:all' -> 'All'."""
    return (s or '').replace('strand:', '').replace('-', ' ').strip().capitalize() or '-'


def _cell(s):
    """A table cell: no raw pipes, no line breaks."""
    return str(s or '').replace('|', '\\|').replace('\n', ' ').strip()


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
