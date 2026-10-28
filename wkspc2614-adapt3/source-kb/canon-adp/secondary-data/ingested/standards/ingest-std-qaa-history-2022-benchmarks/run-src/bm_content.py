# Judgement for run 0110, QAA History 2022 (std run agent). Keys are S4 ids under qaa/history-2022/.
# Built by tools/bm_build.py history-2022 --check. Our words throughout, except `find` texts, which are cut
# from the held text so that each span is exact.
_NORM = open('/home/claude/wkspc2601-library/txt/qaa-2022-history-subject-benchmark-statement-standard.norm.txt', encoding='utf-8').read()
def cut(a, b):
    i = _NORM.find(a); j = _NORM.find(b, i) + len(b)
    return _NORM[i:j]

HON = "bachelor's with honours"
CITE = 'QAA (2022) History Subject Benchmark Statement'

META = dict(
    run='0110', p1='2026-10-03 17:29',
    title='Subject Benchmark Statement History',
    heading='Subject Benchmark Statement: History (QAA, March 2022)',
    edition='March 2022 (fifth edition)', published='2022-03',
    status='current', supersedes='the fourth edition (2019), as the back matter states (D1, back matter: Membership of the Advisory Groups)',
    subjects=[dict(scheme='hecos', code='100302', label='history', basis='stated'),
              dict(scheme='cah', code='CAH20-01-01', label='history', basis='stated')],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, fifth edition for History (March 2022), with the cross-cutting themes',
    partsB="partial: no glossary; the statement sends readers to QAA's Glossary and defines a few terms in passing",
    authority='reference: a sector reference point; in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the quality requirements in Northern Ireland (D1, front matter: Relationship to legislation and regulation)',
    agentDefinition=("QAA's UK reference point for what a History graduate should know, understand and be able to do at the end of a single "
                     "honours bachelor's degree (FHEQ level 6, FQHEIS level 10), also relevant to History in joint, combined and interdisciplinary "
                     "courses. Reach for it when designing, reviewing or describing a History course, its outcomes or its assessment. It states one "
                     "rung only, the minimum threshold, and leaves the classes above it to Annex D of the Frameworks; it is not a curriculum and not "
                     "a regulatory requirement in England."),
    summary=("Published by QAA in March 2022 as the fifth edition, the statement describes the purposes and character of a History degree, "
             "six distinctive design features, teaching, learning and assessment, and benchmark standards at the threshold only: 12 "
             "subject-specific items (4.5) and 17 generic skills (4.6), both threshold by 2.5, with a fuller form of the subject list among "
             "the degree's purposes (1.7). It adds the cross-cutting themes of equality, diversity and inclusion, accessibility, "
             "sustainability and enterprise, points to Annex D of the Frameworks for Higher Education Qualifications for the honours "
             "classifications, and names no professional, statutory or regulatory body in its body text. The 59 statements also hold "
             "provider expectations on course design and assessment (2.1, 2.4, 2.11, 3.7, 3.9 to 3.11, 4.2)."))

S2 = dict(
    governs="what a History graduate can be expected to know, do and understand at the end of a single honours bachelor's degree, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 1.1; 4.1)",
    awards=["bachelor's degrees with honours, single honours in History", "History in joint, combined and interdisciplinary courses (relevant, D1, 1.1; 2.6)"],
    levels=['fheq:6', 'fqheis:10'],
    statedScope='"This Subject Benchmark Statement is focused on single honours bachelor’s courses leading to a named award in History." (D1, 1.1)',
    statedSubjects=[
        dict(name='History', locator='(D1, title; 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100302', label='history'), dict(scheme='cah', code='CAH20-01-01', label='history')]),
        dict(name='History modules offered in joint or combined degrees, or in interdisciplinary courses that include a historical element', locator='(D1, 1.1; 2.6)', kind='programme title', codes=[dict(scheme='hecos', code='100302', label='history')]),
        dict(name='Environmental history', locator='(D1, 1.16; 1.17)', kind='specialism', codes=[dict(scheme='hecos', code='100670', label='environmental history')]),
        dict(name='Public history', locator='(D1, 1.16; 1.17)', kind='specialism', codes=[]),
        dict(name='Economic history', locator='(D1, 1.16; 2.1)', kind='specialism', codes=[dict(scheme='hecos', code='100301', label='economic history')]),
        dict(name='Cultural history', locator='(D1, 1.16; 2.1)', kind='specialism', codes=[]),
        dict(name='Social history', locator='(D1, 2.1)', kind='specialism', codes=[dict(scheme='hecos', code='100312', label='social history')]),
        dict(name='Political history', locator='(D1, 2.1)', kind='specialism', codes=[]),
        dict(name='Gender history', locator='(D1, 2.1)', kind='specialism', codes=[]),
    ])

SECTIONS = {'1': 'Context and purposes of a History degree', '2': 'Distinctive features of a History degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.3', 'Context'), ('1.4', '1.8', 'Purposes of a History degree'), ('1.9', '1.11', 'Characteristics of a History degree'),
       ('1.12', '1.15', 'Equality, diversity and inclusion'), ('1.16', '1.18', 'Sustainability'),
       ('1.19', '1.21', 'Entrepreneurship and enterprise education'), ('2.1', '2.1', 'Design'), ('2.2', '2.2', 'Accessibility'),
       ('2.3', '2.7', 'Progression'), ('2.8', '2.8', 'Flexibility'), ('2.9', '2.9', 'Partnership'), ('2.10', '2.12', 'Monitoring and review'),
       ('3.1', '3.1', 'Content'), ('3.2', '3.8', 'Teaching and learning'), ('3.9', '3.11', 'Assessment'), ('4.1', '4.4', 'Introduction'),
       ('4.5', '4.5', 'Minimum threshold standards'), ('4.6', '4.6', 'Generic skills')]

G = {
    '1.1': 'scope: single honours History, also relevant to joint, combined and interdisciplinary courses',
    '1.2': 'the focus is honours; the criteria hold at every stage towards it',
    '1.3': 'how the subject is organised; the term departments or subject groups',
    '1.4': 'what the subject studies: the whole human past, change and continuity',
    '1.5': 'capabilities shared with the humanities and social sciences (18 items, restated in 4.6)',
    '1.6': 'the distinctive education the subject gives',
    '1.7': 'outcomes on graduating with honours (12 items, restated more briefly in 4.5)',
    '1.8': 'interdisciplinarity and optional experiences such as fieldwork and mobility',
    '1.9': 'independent engagement; no required core of knowledge',
    '1.10': 'variety of teaching; each course sets its own outcomes',
    '1.11': 'clear assessment policies; formative and summative assessment',
    '1.12': 'diversity of past experience; a multi-perspectival discipline',
    '1.13': 'contingent knowledge; uncomfortable pasts; marginalised cultures',
    '1.14': 'an inclusive community: participation, inclusive curricula, decolonising',
    '1.15': "graduates' breadth of skills and contribution to society",
    '1.16': 'sustainability in content and method; the SDGs; environmental history',
    '1.17': 'heritage, conservation and public history',
    '1.18': 'a critical mindset for sustainability challenges',
    '1.19': 'enterprise education and employability',
    '1.20': 'employability skills built in; why employers value History graduates',
    '1.21': 'recognising skills; graduate careers; outcome data',
    '2.1': 'six central features of a History degree, a) to f)',
    '2.2': 'accessible design and attention to students facing practical barriers',
    '2.3': 'cumulative, non-mechanical progression across an honours degree',
    '2.4': 'no fixed order of modules; departments explain progression',
    '2.5': 'yearly attainment towards the threshold; readiness for postgraduate study',
    '2.6': 'joint honours students reach part of the skills',
    '2.7': 'exit awards; four-year Scottish honours',
    '2.8': 'flexible delivery; part-time and mature students',
    '2.9': 'placements and work-related projects',
    '2.10': 'monitoring and periodic review',
    '2.11': 'external reviewers in periodic review',
    '2.12': 'external examiners and threshold standards',
    '3.1': 'breadth and depth of content',
    '3.2': 'student-centred, blended teaching in many settings',
    '3.3': 'lectures in their many formats',
    '3.4': 'seminars and workshops in small groups',
    '3.5': 'independent study as the main mode',
    '3.6': 'critical and constructive comment on progress',
    '3.7': 'teaching methods vary and are reviewed; inclusion and sustainability',
    '3.8': 'module documentation for students',
    '3.9': 'why assessment has to be diverse',
    '3.10': 'six kinds of assessment a course should include, a) to f)',
    '3.11': "each department's assessment mix; every outcome assessed",
    '4.1': 'the lists are the minimum threshold for honours',
    '4.2': 'providers set evidence of achievement with Annex D',
    '4.3': 'templates for different assessment modes',
    '4.4': 'published criteria; positive marking; feedback',
    '4.5': 'threshold subject standards (12 items)',
    '4.6': 'threshold generic skills (17 items)',
}
CTYPE = {'2.1': 'area', '3.1': 'area', '2.9': 'practice', '3.2': 'practice', '3.3': 'practice', '3.4': 'practice', '3.5': 'practice',
         '3.6': 'practice', '3.9': 'practice', '3.11': 'practice'}
EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points', kind='other: front matter, read for S1, S2, S6 and SB6'),
    dict(number='none', heading='section heading lines 1 to 4', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for SB6'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for History', kind='other: back matter, read for the edition history (S8, supersedes)'),
]

P = {}
def s(i, **k): P[i] = k
def you(t):
    return (t.replace('setting their own', 'setting your own').replace('change their view', 'change your view')
             .replace('their own work', 'your own work').replace('express themselves', 'express yourself')
             .replace('to their work', 'to your work').replace('on their own while', 'on your own while').replace('how they are progressing', 'how you are progressing'))

# ---------------------------------------------------------------- the outcome list (1.7) and the threshold subject list (4.5)
# The two lists run item for item in the same order; 4.5 restates 1.7 in shorter form. k: (about, verbs1.7, verbs4.5, domain, g, x7, fw, ad, when, q)
O = {
 1: ('framing historical questions', ['ask'], ['ask'], 'subject-skill',
     'frame pertinent, well-reasoned and tightly focused questions about the past', '',
     'qaa/fheq-2024/4.15.b7', 'qaa/fheq-2024/annex-d/knowledge/r3/3rd',
     'a student is choosing a topic or planning an essay or dissertation', "'What exactly is your question, and why does it matter?'"),
 2: ('finding reliable historical knowledge', ['know', 'access'], ['know', 'access'], 'knowledge',
     'find out where trustworthy, exact knowledge about the past is held and how to reach it', '',
     'qaa/fheq-2024/4.15.b5', 'qaa/fheq-2024/annex-d/cognitive/r1/3rd',
     'a student is unsure where to start researching or which sources to trust', "'Where would you look first, and how would you judge whether it is reliable?'"),
 3: ('structured enquiry with large bodies of evidence', ['conduct'], ['conduct'], 'subject-skill',
     'plan and carry out a structured enquiry, from setting their own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence', '',
     'qaa/fheq-2024/4.15.b6 and 4.15.b2', 'qaa/fheq-2024/annex-d/knowledge/r3/3rd',
     'a student is planning a project, a long essay or a dissertation', "'How will you gather and sort your evidence, and how will you know you have enough?'"),
 4: ('using sound evidence and argument', ['use'], ['use'], 'subject-skill',
     'draw on sound, pertinent evidence and argument', '',
     'qaa/fheq-2024/4.15.b3.1', 'qaa/fheq-2024/annex-d/cognitive/r2/3rd',
     'a student is building or revising an argument', "'Which piece of evidence carries most weight here, and why?'"),
 5: ('bibliographic skills', ['employ'], ['employ'], 'subject-skill',
     'handle references, reading lists and bibliographies well', '',
     'qaa/fheq-2024/4.15.b5', 'qaa/fheq-2024/annex-d/cognitive/r1/3rd',
     'a student asks about referencing or building a reading list', "'How do you keep track of what you read and cite it consistently?'"),
 6: ('analysing claims of differing validity', ['display'], ['display'], 'subject-skill',
     'analyse claims, recognising that some statements are better founded than others',
     ', and that historians test claims by rules of evidence which are themselves open to critique and which belong to intellectual integrity more widely',
     'qaa/fheq-2024/4.15.b7', 'qaa/fheq-2024/annex-d/cognitive/r1/3rd',
     'a student treats every source or claim as equally reliable', "'How would you test whether this claim holds up?'"),
 7: ('critical and empathetic analysis of primary sources', ['analyse', 'addressing'], ['analyse', 'addressing'], 'subject-skill',
     'analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose',
     ', taking primary sources to mean any textual, visual, material or oral evidence from the past that is being examined',
     'qaa/fheq-2024/4.15.b5', 'qaa/fheq-2024/annex-d/cognitive/r1/3rd',
     'a student is working with a document, image, object or oral account', "'Who made this, for whom and why, and how does that shape what it tells you?'"),
 8: ('the problems of the historical record', ['understand'], ['understand'], 'understanding',
     'grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads',
     ', a grasp that also helps them test historical claims made in public life',
     'qaa/fheq-2024/4.15.b4', 'qaa/fheq-2024/annex-d/knowledge/r2/3rd',
     'a student finds sources that conflict or leave gaps', "'What can this evidence not tell you, and how does that limit your conclusion?'"),
 9: ('complexity and diversity of the past', ['appreciate'], ['appreciate'], 'understanding',
     'appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is',
     ', seeing history as a subject that resists reduction and builds intellectual maturity',
     'qaa/fheq-2024/4.15.b4', 'qaa/fheq-2024/annex-d/knowledge/r1/3rd',
     "a student's account flattens a period into one simple story", "'Whose experience of this period is missing from your account?'"),
 10: ('understanding the past on its own terms', ['understand'], ['understand'], 'understanding',
      'understand how people lived, acted and thought in past settings that always differ from our own',
      ', meeting the strangeness of the past, coming to understand unfamiliar structures, cultures and beliefs, and so gaining empathy and respect for difference',
      'qaa/fheq-2024/4.15.b1', 'qaa/fheq-2024/annex-d/knowledge/r2/3rd',
      'a student judges past people by present-day assumptions', "'How did people at the time understand what they were doing?'"),
 11: ('sustaining and revising an argument in debate', ['sustain', 'listen', 'engage', 'amend'], ['sustain', 'listen', 'engage', 'amend'], 'subject-skill',
      'hold to a reasoned argument when others disagree, listen, debate at length and change their view where evidence and argument call for it', '',
      'qaa/fheq-2024/4.15.b3.1 and 4.15.b8', 'qaa/fheq-2024/annex-d/cognitive/r2/3rd',
      'a student is preparing for a seminar debate or answering critical feedback', "'What evidence would make you change your mind?'"),
 12: ('arguing about the past with a bearing on present and future', ['marshal'], ['marshal'], 'subject-skill',
      'build an argument around questions about the past that matter, and that also bear on the present and future', '',
      'qaa/fheq-2024/4.15.b3.1', 'qaa/fheq-2024/annex-d/cognitive/r2/3rd',
      'a student asks why history matters beyond the past itself', "'What does your question tell us about the present?'"),
}
for k, (about, v7, v5, dom, g, x7, fw, ad, when, q) in O.items():
    s('1.7.b%d' % k, type='outcome', rung='none', force='should', level='fheq:6', appliesTo='graduates with honours in History',
      addressee='learner', verbs=v7, about=about, domain=dom, award=HON,
      para='Should be able to ' + g + x7 + '.',
      prac='Graduates with honours in History should be able to ' + g + x7 + '.',
      ben='By the end of your degree, you should be able to ' + you(g + x7) + '.',
      aaw=('Treat this as an outcome a History honours graduate should reach, set out in the account of the degree\'s purposes at FHEQ level 6 '
           '(FQHEIS level 10): to ' + g + '. Cite it as ' + CITE + ', para 1.7, item %d, and note that its shorter form at para 4.5 (4.5.b%d) is the '
           'threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside %s, spine:6 and the third-class '
           'description %s.') % (k, k, fw, ad),
      aad=('Use it when ' + when + ', since it explains why the subject asks for this ability. Tell a student in plain words that by the end of '
           'the degree you should be able to ' + you(g) + ', then ask ' + q + ' Do not recite the full item or treat its added detail as a separate '
           'requirement.'))
    s('4.5.b%d' % k, type='threshold', rung='threshold', force='should', level='fheq:6', appliesTo='graduates with honours in History, at the minimum',
      addressee='learner', verbs=v5, about=about, domain=dom, award=HON,
      para='At threshold, should be able to ' + g + '.',
      prac='At the minimum standard, graduates should be able to ' + g + '.',
      ben='To reach the minimum standard for your degree, you should be able to ' + you(g) + '.',
      aaw=('Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to '
           + g + '. Cite it as ' + CITE + ', para 4.5, item %d, and do not call it a regulatory rule or a sign of a high classification. '
           'Set it beside its fuller form 1.7.b%d, the honours descriptor %s with spine:6, and the third-class floor %s.') % (k, k, fw, ad),
      aad=('Bring it up when ' + when + '. With a student, say in plain words that to graduate you should be able to ' + you(g) + ', and ask '
           + q + ' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award.'))

# ---------------------------------------------------------------- the threshold generic skills (4.6); threshold by 2.5
GS = {
 1: ('independent work with supervision', ['work', 'engaging'], 'work on their own while making good use of supervision and guidance',
     'qaa/fheq-2024/4.15.b9.1', 'qaa/fheq-2024/annex-d/transferable/r3/3rd', '4.6.b12 and 3.10 d)',
     'a student is starting a dissertation or other self-directed work', "'What will you bring to your next supervision, and what will you decide yourself?'"),
 2: ('teamwork', ['work'], 'collaborate well as a member of a team',
     'qaa/fheq-2024/4.15.b9.1', 'qaa/fheq-2024/annex-d/transferable/r2/3rd', '3.10 e)',
     'a student is about to start group work or a group presentation', "'What role do you usually take in a group, and how could you widen it?'"),
 3: ('formulating and pursuing enquiries', ['formulate', 'pursue'], 'devise and follow up clearly framed questions and lines of enquiry',
     'qaa/fheq-2024/4.15.b7', 'qaa/fheq-2024/annex-d/knowledge/r3/3rd', '4.5.b1 and 4.5.b3',
     'a student is turning a broad interest into a researchable question', "'Can you state your question in one sentence?'"),
 4: ('information retrieval and handling', ['demonstrate'], 'identify, locate, retrieve, sort and share information by suitable means',
     'qaa/fheq-2024/4.15.b5', 'qaa/fheq-2024/annex-d/practical/r4/3rd', '4.5.b2 and 4.5.b5',
     'a student struggles to find or manage material for an assignment', "'How do you search, and how do you keep what you find in order?'"),
 5: ('gathering and deploying evidence and data', ['gather', 'organise', 'deploy'], 'collect, arrange and put to use evidence, data and information',
     'qaa/fheq-2024/4.15.b6', 'qaa/fheq-2024/annex-d/practical/r4/3rd', '4.5.b3 and 4.5.b4',
     'a student has plenty of material but no clear way to use it', "'Which of your sources does the most work in your argument?'"),
 6: ('analysing sources', ['undertake'], 'carry out close analysis of sources',
     'qaa/fheq-2024/4.15.b7', 'qaa/fheq-2024/annex-d/cognitive/r1/3rd', '4.5.b7',
     'a student describes sources instead of analysing them', "'What does this source show that its author may not have intended?'"),
 7: ("judging others' arguments", ['recognise'], "see what is strong and what is weak in other people's arguments",
     'qaa/fheq-2024/4.15.b7', 'qaa/fheq-2024/annex-d/cognitive/r2/3rd', '4.5.b6 and 4.5.b11',
     'a student is reviewing scholarship or responding to peers', "'Where is this historian's argument least convincing, and why?'"),
 8: ('analysis and problem-solving', ['show', 'consider', 'solve'], 'think analytically and tackle problems, including ones with no single answer',
     'qaa/fheq-2024/4.15.b7', 'qaa/fheq-2024/annex-d/cognitive/r3/3rd', '4.5.b6',
     'a student is stuck on a problem with several possible answers', "'What are the possible answers here, and how would you choose between them?'"),
 9: ('conceptual grasp and shaping arguments', ['demonstrate', 'shape'], 'grasp concepts and use them to give shape to arguments',
     'qaa/fheq-2024/4.15.b3.1', 'qaa/fheq-2024/annex-d/knowledge/r2/3rd', '4.5.b4 and 4.5.b12',
     'a student uses concepts such as class, gender or empire loosely', "'How are you defining this concept, and how does it shape your argument?'"),
 10: ('intellectual integrity, maturity and independence', ['show'], 'act with integrity, maturity and independence of mind',
      'qaa/fheq-2024/4.15.b9.1', 'qaa/fheq-2024/annex-d/transferable/r4/3rd', '4.6.b14',
      "a student faces a choice about how to use others' work or how far to lean on a tutor", "'Which judgements in this work are genuinely yours?'"),
 11: ('imagination and creativity', ['exhibit'], 'bring imagination, insight and creativity to their work',
      'qaa/fheq-2024/4.15.b6', 'qaa/fheq-2024/annex-d/cognitive/r4/3rd', '4.5.b12',
      'a student wants to try an unusual approach or format', "'What fresh angle could you take on this topic?'"),
 12: ('self-discipline and self-direction', ['demonstrate'], 'discipline and direct their own work',
      'qaa/fheq-2024/4.15.b5', 'qaa/fheq-2024/annex-d/transferable/r3/3rd', '4.6.b1',
      'a student is managing deadlines or long stretches of independent study', "'How do you plan a week of independent study?'"),
 13: ('initiative and questioning habits', ['show'], 'take the initiative and make a habit of asking questions',
      'qaa/fheq-2024/4.15.b9.1', 'qaa/fheq-2024/annex-d/transferable/r4/3rd', '4.6.b3',
      'a student waits to be told what to read or do', "'What question would you like to pursue that nobody has set you?'"),
 14: ('academic integrity and research ethics', ['show'], "understand academic integrity and the ethical duties raised by research and by drawing on other people's work",
      'qaa/fheq-2024/4.15.b2', 'qaa/fheq-2024/annex-d/knowledge/r3/3rd', '2.1 d) (2.1.b4)',
      'a student asks about referencing, plagiarism, generative tools or research ethics approval', "'How do you show which ideas are yours and which you have drawn from others?'"),
 15: ('oral, written and digital communication', ['exhibit'], 'express themselves with structure, coherence and clarity in speech and writing, and use digital tools with confidence',
      'qaa/fheq-2024/4.15.b8', 'qaa/fheq-2024/annex-d/transferable/r1/3rd', '4.5.b11 and 3.10 a)',
      'a student is preparing a presentation, essay or digital output', "'Could a reader follow your argument from your paragraph openings alone?'"),
 16: ('reflection and use of feedback', ['make'], 'reflect on how they are progressing and act on feedback',
      'qaa/fheq-2024/4.15.b5', 'qaa/fheq-2024/annex-d/transferable/r5/3rd', '4.4 on feedback',
      'a student receives marked work or asks how to improve', "'What one change from your last feedback will you make in your next piece?'"),
 17: ('sustainability debates and global perspectives', ['appreciate', 'engage'], 'take part in current debates on global sustainability and on global perspectives',
      'qaa/fheq-2024/4.15.b8', 'qaa/fheq-2024/annex-d/summary/r1/3rd', '1.16 to 1.18 and std:doc:qaa-advancehe-esd-2021-guidance',
      'a student links a topic to climate, environment or global inequality', "'How does the history you are studying bear on a present global challenge?'"),
}
for k, (about, verbs, g, fw, ad, nb, when, q) in GS.items():
    s('4.6.b%d' % k, type='threshold', rung='threshold', force='should', level='fheq:6', appliesTo='graduates with honours in History, at the minimum',
      addressee='learner', verbs=verbs, about=about, domain='generic-skill', award=HON,
      para='At threshold, as a generic skill, should be able to ' + g + '.',
      prac='As a minimum generic skill, graduates should be able to ' + g + '.',
      ben='To reach the minimum standard for your degree, you should be able to ' + you(g) + '.',
      aaw=('Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the '
           'minimum (para 2.5) and refines the FHEQ level 6 descriptor %s (spine:6; FQHEIS level 10). Graduates should be able to ' + g + '. '
           'Cite it as ' + CITE + ', para 4.6, item %d; do not claim it holds at another level or is a legal requirement, and set it beside %s '
           'and the third-class description %s.') % (fw, k, nb, ad),
      aad=('Raise it when ' + when + '. Put it to a student as a skill you should be able to show by graduation, to ' + you(g) + ', and ask ' + q +
           ' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud.'))

# ---------------------------------------------------------------- statements in the descriptive sections
s('1.20', find=cut('The practice of working across', 'variety of audiences.'),
  type='expectation', rung='none', force='must', level='fheq:6', appliesTo='students of History', addressee='learner',
  verbs=['summarise', 'form', 'communicate'], about='handling information and arguing for audiences, for employability', domain='generic-skill', award=HON,
  para=('Because the subject works across a wide range of sources, History students must become skilled at finding, choosing, interpreting, '
        'analysing and combining information from large analogue and digital datasets, and at condensing complex knowledge into clear, reasoned arguments for varied audiences.'),
  prac=('Because historical work spans many kinds of source, students must become adept at retrieving, selecting, interpreting, analysing and '
        'combining information from large paper and digital collections, and at turning complex knowledge into clear, reasoned arguments for different audiences.'),
  ben=('Because history draws on so many kinds of source, you must become skilled at finding, sorting, interpreting and combining information '
       'from large paper and digital collections, and at turning complex material into clear, reasoned arguments for different audiences.'),
  aaw=('Treat this as an expected outcome stated in the enterprise and employability part of the statement: what the subject\'s work with sources '
       'requires of History students at honours level (FHEQ level 6). Cite it as ' + CITE + ', para 1.20, and record its force as must only with '
       "the note that the issuer writes 'requires', not 'must'. Set it beside the threshold items 4.5.b3 and 4.6.b4, the FHEQ descriptors "
       'qaa/fheq-2024/4.15.b5 and 4.15.b8, and spine:6.'),
  aad=('Raise it when a student or programme team asks how historical study builds skills employers value. Put it to a student as the information '
       "and communication skills you must build by working with many sources, and ask: 'Which large set of sources have you handled, and how did you "
       "turn it into an argument for a particular audience?' Avoid presenting it as a separate employability requirement or reading the passage aloud."))

s('2.1.b2', find=cut('Where a single country', 'should be multiperspectival.'),
  type='expectation', rung='none', force='should', level='none', appliesTo='History courses focused mainly on one country', addressee='provider',
  verbs=['incorporates'], about='comparison in courses centred on one country', domain='none', award=HON,
  para='A course centred mainly on one country brings in sustained, serious comparison with other places and should take several perspectives.',
  prac='Where one country dominates a course, build in serious, sustained comparison with others: the course should take more than one perspective.',
  ben=('n/a', 'a duty on course design; the student meets its effect'),
  aaw=('Treat this as a provider expectation, worded with should, on the design of History honours courses whose focus is mainly one country; it '
       'concerns course structure, not a student outcome. Cite it as ' + CITE + ', para 2.1 b) (geographical range), and do not present it as a '
       'requirement on every module. Set it beside the outcome items 1.7.b9 and 4.5.b9 on the variety of the past, and the comparative knowledge '
       'in the Scottish honours descriptor qaa/fqheis-2024/4.16.b1.'),
  aad=('Raise it with a programme team reviewing a course built around one nation\'s history. Ask how and where the course compares that country '
       'with others, and whether more than one perspective runs through it. Do not put this to a student as something they must do: it is the course\'s duty.'))

s('2.1.b3', find=cut('opportunity for close work', 'is essential.'),
  type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='History honours courses and their students', addressee='both',
  verbs=[], about='close work on primary sources from the period', domain='subject-skill', award=HON,
  para='Close study of material produced in the period being studied is indispensable to the degree.',
  prac='Give every student the chance to study closely source material from the period being taught; the statement calls this essential.',
  ben='You will get the chance to work closely with sources created in the period you are studying, a central part of learning history.',
  aaw=('Treat this as a defining feature of a History honours course rather than a graded outcome: the issuer calls the opportunity for close '
       "source work 'essential', a word outside the five modals, so its force is recorded as describes and flagged. Cite it as " + CITE + ', para 2.1 c) '
       '(primary sources), and do not turn it into a claim that every module must be source-based. Set it beside 1.7.b7 and 4.5.b7 on analysing '
       'primary sources and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5.'),
  aad=('Raise it when a student or team asks what makes a History course distinctive or how much source work to expect. For a student, say plainly '
       "that working closely with material from the period is central to the subject, and ask: 'Which sources from your period have you worked with "
       "directly so far?' For staff, ask where each year offers this, without implying it belongs only in a research module."))

s('2.1.b4', find=cut('History students are expected to demonstrate', 'in their own work.'),
  type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='students of History', addressee='learner',
  verbs=['demonstrate', 'receive'], about='historiographical, methodological and ethical awareness across modules', domain='understanding', award=HON,
  para=("Students are expected to show awareness and understanding of historiography and method in every module and in long independent work, "
        "to receive guidance in research ethics and show they apply it, and to know the subject's conventions for quoting and reproducing others' work."),
  prac=("Expect students to show historiographical and methodological awareness in all modules and in extended independent work; give them guidance "
        "in research ethics that they can show they apply, including institutional and archive codes, and teach the conventions for quoting and reproducing others' work."),
  ben=("You are expected to show that you understand how historians have written about your topics and the methods they use, in every module and in "
       "longer independent work, to apply research ethics, including any archive or university codes, and to follow the subject's rules on quoting others."),
  aaw=("Treat this as an expectation on History honours students (the issuer says 'expected to', outside the five modals, so its force is recorded "
       'as describes and flagged), covering historiographical and methodological awareness, research ethics and the conventions of quotation. Cite it as '
       + CITE + ', para 2.1 d) (critical awareness), and do not claim it requires a dedicated historiography module, since the text allows the awareness '
       'to be shown across modules. Set it beside 4.6.b14 on academic integrity, 4.5.b8 on the historical record, and the FHEQ level 6 descriptors '
       'qaa/fheq-2024/4.15.b4 and 4.15.b2.'),
  aad=("Raise it when a student asks why essays are marked on engagement with historians' debates, or before archive or oral history work that needs "
       "ethical approval. Explain in plain words that you are expected to show awareness of how history is written and researched in every module, and "
       "ask: 'Whose interpretations are you arguing with here?' and 'Do you need ethical approval or archive permission for this?' Avoid reading out the "
       'paragraph or treating ethical approval as optional.'))

s('2.4', find=cut('However, it is the responsibility', 'period of study.'),
  type='expectation', rung='none', force='describes', level='none', appliesTo='History departments', addressee='provider',
  verbs=['articulate', 'facilitates'], about='explaining progression in a non-sequential subject', domain='none', award=HON,
  para='History has no fixed order of modules, so departments carry the responsibility to explain clearly how each course supports progression across its years.',
  prac="Because the subject is not sequential, set out clearly in course documents how the course builds progression year on year; the statement makes this the department's responsibility.",
  ben=('n/a', "a responsibility of the department in course design; the student sees its effect in course documents"),
  aaw=("Treat this as a duty on departments (the issuer says 'responsibility', outside the five modals, so its force is recorded as describes and "
       'flagged), set against the view that History has no fixed order of modules. Cite it as ' + CITE + ', para 2.4, and do not claim it prescribes a '
       "sequence of modules or a syllabus for each year. Set it beside 2.3 and 2.5 on progression and the FHEQ's own account of rising levels "
       '(std:doc:qaa-fheq-2024-framework, SL4), with fheq:4 to fheq:6 as the steps.'),
  aad=('Raise it with a programme team writing or reviewing a course specification. Ask how the course shows that demands rise from year to year '
       'when modules can be taken in any order, and where that is written down. Do not present it to students as their task; it belongs to the department.'))

s('2.5', type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='students and graduates of History honours courses', addressee='learner',
  verbs=['builds', 'achieved', 'undertaking'], about='yearly attainment towards the threshold; readiness for postgraduate study', domain='none', award=HON,
  para=("Each year is expected to bring knowledge, expertise and experience that build towards meeting every threshold subject and generic skill in "
        "the statement; a graduate with a second-class degree or better is expected to be ready for postgraduate study in History or a related field."),
  prac=("Plan each year so that attainment builds towards all the threshold subject-specific and generic skills by graduation; a graduate with at "
        "least a second-class degree is expected to be ready and able to take on postgraduate study."),
  ben=("Each year of your degree is meant to build your knowledge and skills towards the full set of minimum outcomes; if you graduate with a "
       "second-class degree or higher, you are expected to be ready for postgraduate study in history or a related subject."),
  aaw=("Treat this as the statement's expectation (worded 'it is expected', outside the five modals, so recorded as describes) that each year builds "
       'towards all the threshold skills of paras 4.5 and 4.6, and that a second-class degree or better prepares a graduate for postgraduate study. '
       'Cite it as ' + CITE + ', para 2.5, and do not claim it sets thresholds for each year or guarantees entry to a master\'s course. Set it beside the '
       'threshold lists 4.5 and 4.6, the honours descriptor qaa/fheq-2024/4.15.b9.3 on learning for further training, and the Annex D summary '
       'qaa/fheq-2024/annex-d/summary/r1/2.2.'),
  aad=('Raise it when a student asks whether they are on track, or whether their likely classification is enough for a master\'s course. Say in plain '
       "words that each year should move you closer to the full set of minimum outcomes, and ask: 'Which of the outcomes do you feel least sure of now, "
       "and how will this year help?' Avoid promising postgraduate admission or treating the expectation as a guarantee."))

s('2.6', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='joint honours undergraduates', addressee='learner',
  verbs=['achieve', 'add'], about='joint honours: part of the subject and generic skills', domain='none', award=HON,
  para="Joint honours students will reach some of the subject's specific and generic skills and will gain others from the other subjects they study.",
  prac="In joint honours, graduates will meet some of History's subject-specific and generic skills and will add others from the partner subjects; design the History part with that in mind.",
  ben='If you study History jointly with another subject, you will develop some of the history skills and add others from your other subject.',
  aaw=('Treat this as an expected outcome (will) for joint honours students at FHEQ level 6: they meet part of History\'s subject and generic skills, '
       'not necessarily all. Cite it as ' + CITE + ', para 2.6, and do not claim that joint honours graduates must meet every item in 4.5 and 4.6, or '
       'that the statement says which items. Set it beside 1.1 on joint and combined courses, the threshold lists 4.5 and 4.6, the honours descriptor '
       'qaa/fheq-2024/4.15.b1 and spine:6.'),
  aad=('Raise it when a joint honours student, or a team designing a joint course, asks which History outcomes apply. Explain that you will build '
       "some of the history skills and gain others from your other subject, and ask: 'Which history skills does your course develop, and which come "
       "from your other subject?' Avoid telling a joint student they fall short for not covering every History item."))

s('2.11', type='expectation', rung='none', force='will', level='none', appliesTo='higher education providers in periodic review', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award=HON,
  para='Providers will bring external reviewers into periodic review for an outside view of proposed changes and to make sure threshold standards are met and content suits the subject.',
  prac='Periodic review will draw on external reviewers for an outside perspective on proposed changes, to confirm that threshold standards are achieved and that content fits the subject.',
  ben=('n/a', "a duty on the provider's quality assurance"),
  aaw=('Treat this as a statement, in will, about provider practice in quality assurance: external reviewers take part in the periodic review of '
       'History courses. Cite it as ' + CITE + ', para 2.11, and do not present it as a student outcome or as a regulatory requirement set by this '
       'statement. Set it beside 2.10 and 2.12 on monitoring and external examining, and the threshold lists 4.5 and 4.6 that reviewers check against.'),
  aad=('Raise it with a programme team preparing for periodic review. Ask who the external reviewers will be and how their view on threshold '
       'standards and subject content will be recorded and acted on. Do not bring it to a student as something they need to do.'))

s('3.7', find=cut('Teaching and learning methods should', 'Sustainable Development.'),
  type='expectation', rung='none', force='should', level='none', appliesTo='History departments and teaching staff', addressee='provider',
  verbs=['reflect', 'provide'], about='inclusive and sustainable teaching methods', domain='none', award=HON,
  para='Teaching and learning methods should also show the need for an inclusive environment and serve the aims of education for sustainable development.',
  prac='Choose teaching methods that should create an inclusive environment for learning and serve the aims of education for sustainable development.',
  ben=('n/a', 'a duty on teaching design; the student meets its effect'),
  aaw=('Treat this as a provider expectation (should) on teaching and learning methods in History courses, carrying both the equality, diversity '
       'and inclusion theme and education for sustainable development. Cite it as ' + CITE + ', para 3.7, and do not claim it prescribes particular '
       'methods, since the same paragraph leaves methods to each department. Set it beside 1.12 to 1.14 on inclusion, 1.16 to 1.18 on sustainability, '
       'and the guidance std:doc:qaa-advancehe-esd-2021-guidance.'),
  aad=("Raise it with staff reviewing a module's teaching or a course's learning and teaching strategy. Ask how the current methods include every "
       'student and where they connect with sustainability, and what evidence, such as evaluations or peer review, shows it. Do not present it to a student as their duty.'))

s('3.9', type='expectation', rung='none', force='should', level='none', appliesTo='History courses', addressee='provider',
  verbs=['provide', 'show'], about='diverse assessment so every student can show their abilities', domain='none', award=HON,
  para=("Assessment needs variety, because no single mode reveals all of a student's abilities and students arrive with different backgrounds; "
        'courses should give everyone chances to demonstrate their knowledge, understanding and skills, rewarding strengths while building weaker areas.'),
  prac=('Use a variety of assessment modes: no one mode shows the full range of ability, and students arrive with different qualifications, so the '
        'course should give all of them chances to demonstrate their knowledge, understanding and abilities.'),
  ben=('n/a', "a duty on the course's assessment design"),
  aaw=('Treat this as a provider expectation (should) that History courses assess through varied modes so every student can demonstrate what they '
       'have learned. Cite it as ' + CITE + ', para 3.9, and do not claim it fixes a list of modes; the kinds are in 3.10. Set it beside 3.10 a) to f) '
       'and 3.11, and the Annex D descriptions (std:doc:qaa-fheq-2024-framework, SL6) that classification draws on.'),
  aad=("Raise it with a team designing or reviewing a course's assessment pattern. Ask whether any group of students could be disadvantaged by relying "
       'on one mode, and where students can play to their strengths. Do not present it to a student as a requirement on them.'))

# 3.10 a) to f): lead-in "These should include:"
AS = {
 1: ('a', cut('assessments that show a student', 'digital history projects'), ['show', 'communicate'], 'communication assessments in varied forms',
     'tasks in which students communicate information and argument to suit the task, in written forms of differing kinds, lengths and audiences, and in forms beyond prose such as talks, videos, websites, databases and digital history projects',
     'assessments of communicating information and argument in written and non-written forms', '',
     '3.10 b) to f), 3.9 and the generic skill 4.6.b15', 'qaa/fheq-2024/annex-d/transferable/r1/3rd',
     'tasks for different audiences and in non-written forms', 'the range goes beyond the essay'),
 2: ('b', cut('assessments that demonstrate an ability to work with', 'or commentaries'), ['demonstrate', 'work'], 'work with historical evidence',
     'tasks that test handling varied kinds of historical evidence, for example gobbet exercises, source exercises or commentaries',
     'assessments of working with historical evidence', '',
     '4.5.b7 on primary sources and 3.10 a) to f)', 'qaa/fheq-2024/annex-d/cognitive/r1/3rd',
     'source-based tasks such as gobbets or commentaries', 'every year includes some'),
 3: ('c', cut('assessments that demonstrate a student', 'hours or days'), ['demonstrate', 'work', 'think'], 'time-pressured assessment',
     'tasks that test working against the clock and quick thinking, whether a timed exam, a take-home paper or a task over hours or days',
     'assessments of working under time pressure and thinking quickly', ', since the text allows exams, take-home papers or tasks over days',
     '3.9 and 3.10 a) to f)', 'qaa/fheq-2024/annex-d/cognitive/r3/3rd',
     'time-limited tasks', 'they suit students who need adjustments'),
 4: ('d', cut('assessments that demonstrate an ability to work independently', 'under supervision'), ['demonstrate', 'work'], 'supervised independent work',
     'tasks that test independent work carried out under supervision',
     'assessments of independent work under supervision', '',
     '4.6.b1 and 3.10 f)', 'qaa/fheq-2024/annex-d/transferable/r3/3rd',
     'supervised independent tasks', 'supervision is set up before the final year'),
 5: ('e', cut('assessments that show an ability to collaborate', 'or projects'), ['show', 'collaborate', 'work'], 'collaboration and group work',
     'tasks that test collaboration and effective group work, such as group presentations or projects',
     'assessments of collaboration and group work', '',
     '4.6.b2', 'qaa/fheq-2024/annex-d/transferable/r2/3rd',
     'assessed group work', 'individual contributions are fairly recognised'),
 6: ('f', cut('at least one major assignment', 'different audiences.'), ['assessed', 'address', 'pursue', 'sustaining', 'developing'], 'a major staged historical enquiry',
     'at least one major assignment testing the ability to tackle historical problems in depth through structured enquiry pursued over several stages, often a dissertation or final year project at least twice the usual essay length, though other forms, including authentic tasks for different audiences, are possible',
     'at least one major assignment testing structured historical enquiry in depth over several stages', ', since the text allows forms other than a dissertation',
     '2.1 f) on the extended piece of work, 4.5.b3 and 4.6.b3', 'qaa/fheq-2024/annex-d/knowledge/r3/3rd and the honours descriptor qaa/fheq-2024/4.15.b6',
     'a major staged enquiry', 'students set their own tasks within it'),
}
for k, (letter, text, verbs, about, body, thing, extra, nb, ad, thing2, q) in AS.items():
    s('3.10.b%d' % k, find=text, type='expectation', rung='none', force='should', level='none', appliesTo='the assessment of History courses',
      addressee='provider', verbs=verbs, about=about, domain='none', award=HON,
      para='Assessments should include ' + body + '.',
      prac='The course should include ' + body + '.',
      ben=('n/a', "a requirement on the course's assessment design; the student meets it as the tasks set"),
      aaw=('Treat this as a provider expectation (should) on the mix of assessment in a History honours course: the course should include '
           + thing + '. Cite it as ' + CITE + ', para 3.10 ' + letter + '), and do not claim it requires one particular format' + extra +
           '. Set it beside ' + nb + ', and the Annex D descriptions it helps to evidence, such as ' + ad + '.'),
      aad=('Raise it with a team mapping assessment across a course, or a module leader choosing a task type. Ask where in the course students meet '
           + thing2 + ', and whether ' + q + '. Do not put it to a student as a demand on them; for a student, simply explain that the course includes such tasks.'))

s('3.11', find=cut('In any case, however', 'on their assessments.'),
  type='requirement', rung='none', force='must', level='none', appliesTo='the assessment of History courses', addressee='provider',
  verbs=['enable', 'demonstrate'], about='assessment covering every outcome, with information and feedback', domain='none', award=HON,
  para=('Whatever the mix, the assessments as a whole must let students show every learning outcome of their course, with clear and timely '
        'information on how they will be assessed and constructive feedback.'),
  prac=('Taken together, the course\'s assessments must allow students to demonstrate every intended learning outcome; give students clear, timely '
        'information about how they are assessed and constructive feedback on their work.'),
  ben=('n/a', "a requirement on the course's assessment design"),
  aaw=('Treat this as the one must in the account of assessment: across a History course, the combined assessments must allow students to '
       'demonstrate all its learning outcomes, with clear information and constructive feedback. Cite it as ' + CITE + ', para 3.11, and do not claim '
       'that each single assessment must cover every outcome. Set it beside 3.9 and 3.10 a) to f), the threshold lists 4.5 and 4.6, and the FHEQ '
       'level 6 descriptor qaa/fheq-2024/4.15.b5.'),
  aad=("Raise it with a team building an assessment map or a module leader writing assessment briefs. Ask: 'Which assessment shows each learning "
       "outcome, and is any outcome never assessed?', and how students learn in good time how they will be assessed. Do not present it to a student "
       'as their obligation; to a student, explain only that every outcome is assessed somewhere and that feedback is due.'))

s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['refer', 'operate', 'publish'], about='evidence of achievement and Annex D', domain='none', award=HON,
  para=("Each provider sets its own way of judging what counts as evidence of achievement and should consult Annex D's classification descriptions "
        'for honours degrees at FHEQ level 6 and FQHEIS level 10; providers run and publish their own descriptors, perhaps as assessment criteria.'),
  prac=("Decide how the course will evidence achievement of the standards; the course team should consult Annex D's descriptions of the four honours "
        'classes (1st, 2:1, 2:2, 3rd) and publish its own descriptors for students, for example as assessment criteria.'),
  ben=('n/a', 'a duty on the provider in setting its own descriptors'),
  aaw=('Treat this as a provider expectation (should) that links the History threshold standards to the generic classification descriptions in '
       'Annex D of the Frameworks for Higher Education Qualifications. Cite it as ' + CITE + ', para 4.2, and do not claim that the History statement '
       'defines the classes itself or that Annex D is subject-specific. Set it beside 4.1 and the threshold lists 4.5 and 4.6, and point to '
       'std:doc:qaa-fheq-2024-framework, Annex D (SL6), with third-class cells such as qaa/fheq-2024/annex-d/summary/r1/3rd as the threshold.'),
  aad=("Raise it with staff writing marking criteria or grade descriptors for a History course. Ask how the course's descriptors relate to Annex D's "
       'four classes and where students can read them. With a student, explain only that the classification bands come from published descriptors, '
       'and avoid reading Annex D aloud.'))

GRADE = {}   # one rung only: no gradeOf links
TH = {'1.20': 'theme:enterprise', '3.7': 'theme:edi, theme:esd', '4.6.b17': 'theme:esd'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.3; 4.2'), dict(id='fqheis:10', role='cites', locator='D1, 2.3; 4.2')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent',
                           basis='stated (D1, 2.3: a degree with honours at FHEQ Level 6 and FQHEIS Level 10; 4.2: Annex D for both); matches std:doc:qaa-fheq-2024-framework S5, Table 1')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.12', '1.13', '1.14', '3.7', '3.11']),
      dict(id='theme:accessibility', role='carries', carriedIn=['2.2', '2.8']),
      dict(id='theme:esd', role='carries', carriedIn=['1.5', '1.16', '1.17', '1.18', '3.7', '3.11', '4.6']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.19', '1.20', '1.21'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-history-2019-benchmarks (not ingested)', note='the fourth edition, 2019; this is the fifth (D1, back matter)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='cited at 4.2 as Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees; now part of the Frameworks 2024'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='fheq:6 (2.3, 4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='fqheis:10 (2.3, 4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='cited at 1.16 and in the list of references'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance (not yet ingested)', note='front matter'),
      dict(rel='refersTo', target="QAA Glossary (not ingested)", note='front matter')]

SB1 = ['The study of the whole human past, from human origins to recent events, tracing change and continuity across society, politics, economics, culture, ideas and environments (D1, 1.4).',
       'Allied to the humanities, arts and social sciences, yet distinct in its sense of the past, its respect for context and its rigorous handling of evidence (D1, 1.5, 1.6).',
       'No fixed canon: historians recognise no required body of knowledge or core, so courses legitimately differ in content, teaching and assessment (D1, 1.9 to 1.11).',
       'Six central features: depth of time; geographical range and comparison; close work on primary sources; critical, historiographical and ethical awareness; varied specialisms; an extended independent piece of work (D1, 2.1).',
       'A non-sequential subject: progression is cumulative and qualitative rather than a fixed order of modules (D1, 2.3, 2.4).',
       'Multi-perspectival and, by its own account, uncomfortable, attending to non-dominant and marginalised cultures (D1, 1.12, 1.13).']
SB2 = [dict(theme='theme:edi', inThisSubject='the subject recovers the diversity of past experience and is multi-perspectival; it faces uncomfortable pasts, attends to marginalised cultures and commits its community to widening participation, inclusive curricula and decolonising the curriculum (D1, 1.12 to 1.14); teaching methods should be inclusive (D1, 3.7)', statements=['3.7']),
       dict(theme='theme:accessibility', inThisSubject='courses aim to be highly accessible through varied teaching and assessment, digital resources and attention to students facing practical barriers: disability, health conditions, caring, commuting, low income and religious observance (D1, 2.2); flexible and part-time delivery follow (D1, 2.8)', statements=[]),
       dict(theme='theme:esd', inThisSubject='headed Sustainability: content and method serve the UN goals, with environmental, public, economic and cultural history to the fore, links to heritage and conservation, and a mindset of change, continuity and causation (D1, 1.16 to 1.18); a generic skill and teaching methods carry it (D1, 4.6, 3.7)', statements=['3.7', '4.6.b17']),
       dict(theme='theme:enterprise', inThisSubject='headed Entrepreneurship and enterprise education: employability built into modules through real-world tasks such as policy papers, group work and presentations; career resilience; a wide spread of graduate careers (D1, 1.19 to 1.21)', statements=['1.20'])]
SB3 = dict(areas=[dict(component='2.1', gloss='six central features of course design: time depth, geographical range, primary sources, critical awareness, varied specialisms, extended work'),
                  dict(component='3.1', gloss='breadth and depth vary by department and module choice, resting on sections 1 and 2')],
           practices=[dict(component='3.2', kind='teaching', gloss='student-centred, blended, in classrooms, libraries, online and at museums, galleries and heritage sites'),
                      dict(component='3.3', kind='teaching', gloss='lectures in many formats, including online and flipped'),
                      dict(component='3.4', kind='learning', gloss='seminars and workshops in small groups, with preparatory tasks'),
                      dict(component='3.5', kind='learning', gloss='independent study as the main mode, guided by reading lists'),
                      dict(component='3.6', kind='learning', gloss='regular critical and constructive comment from staff'),
                      dict(component='2.9', kind='learning', gloss='work placements and work-related projects, history-related or not'),
                      dict(component='3.9', kind='assessment', gloss='varied modes so every student can show their abilities'),
                      dict(component='3.10', kind='assessment', gloss='six kinds of assessment, including one major staged enquiry'),
                      dict(component='3.11', kind='assessment', gloss="each department's own mix, covering every outcome, with information and feedback")])
SB4 = dict(rungs=[dict(rung='threshold', leadIn='4.5', award=HON, items=29)],
           rungBases=("4.1 calls section 4 the minimum threshold standards for an honours degree. 4.5, headed Minimum threshold standards, holds the 12 "
                      "subject-specific items; 4.6, headed Generic skills, holds 17 more under the same lead-in, threshold by 2.5 ('threshold-level "
                      "subject-specific and generic skills'). No typical or excellent rung: 4.2 sends providers to Annex D for the classes above threshold."),
           outcomeLists=[dict(leadIn='1.7', gloss='outcomes on graduating with honours, in the account of the purposes; restated more briefly as the 4.5 threshold items, item for item', items=12, award=['honours'])],
           outcomes=[])
SB4A_FULL = []
SB5 = []
SB6 = dict(themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.12', '1.13', '1.14', '3.7', '3.11'], statements=['3.7']),
                   dict(id='theme:accessibility', named='Accessibility', carriedIn=['2.2', '2.8'], statements=[]),
                   dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development; 3.7: Education for Sustainable Development)', carriedIn=['1.5', '1.16', '1.17', '1.18', '3.7', '3.11', '4.6'], statements=['3.7', '4.6.b17']),
                   dict(id='theme:enterprise', named='Entrepreneurship and enterprise education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.19', '1.20', '1.21'], statements=['1.20'])],
           frameworks=[dict(framework='fheq', levels=['fheq:6'], citedIn=['2.3', '4.2']),
                       dict(framework='scqf', levels=['fqheis:10'], citedIn=['2.3', '4.2'])],
           bodies=[],
           sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='descriptions of the four honours classes (1st, 2:1, 2:2, 3rd); the only account of standards above threshold'),
                            dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='QAA and Advance HE, Education for Sustainable Development Guidance', citedIn=['1.16', 'section 5'], role='frame for the sustainability theme'),
                            dict(document='UN Sustainable Development Goals (external)', named='UN Sustainable Development Goals', citedIn=['1.16'], role='what the subject can contribute to'),
                            dict(document='Prospects and HESA graduate outcomes data (external)', named='Prospects and HESA', citedIn=['1.21', 'section 5'], role='data on graduate careers'),
                            dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
                            dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
                            dict(document="OfS regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland) (not ingested)", named="Office for Students' regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework", citedIn=['front matter'], role="the statement's standing in each nation")])

B1 = [dict(slug='historiography', definition='the study of how history has been written (D1, 2.1 d)', beneficiaryDefinition='how historians have written about the past and why their accounts differ', scopeNote='expected to show across all modules, not only in a dedicated one', category='unknown', practices=['education']),
      dict(slug='primary-source', definition='any evidence from the past that is under examination, whether textual, visual, material or oral (D1, 1.7; 2.1 c)', beneficiaryDefinition='material made in the period you are studying', scopeNote='close work on it is called essential (2.1 c)', category='unknown', practices=['education']),
      dict(slug='formative-assessment', definition='assessment meant as feedback on progress (D1, 1.11)', beneficiaryDefinition='work that is marked to help you improve, not to count towards your degree', scopeNote='set against summative assessment', category='unknown', practices=['education']),
      dict(slug='summative-assessment', definition='assessment chiefly for awarding and classifying the degree (D1, 1.11)', beneficiaryDefinition='work that counts towards your degree result', scopeNote='set against formative assessment', category='unknown', practices=['education']),
      dict(slug='extended-piece-of-work', definition='an independent extended piece of work under supervision, often called a dissertation or final year project, usually source-based or historiographical (D1, 2.1 f; 3.10 f)', beneficiaryDefinition='your own long project, such as a dissertation', scopeNote='one of the six features (2.1 f) and an assessment the course should include (3.10 f)', category='unknown', practices=['education']),
      dict(slug='flipped-lecture', definition='a lecture students meet online first and then build on in class discussion and reflection (D1, 3.3)', beneficiaryDefinition='a lecture you watch beforehand and then discuss in class', scopeNote='one of several lecture formats', category='unknown', practices=['education']),
      dict(slug='threshold-standard', definition='the minimum a student will have shown on being awarded honours in History (D1, 4.1, 4.5)', beneficiaryDefinition='the minimum you need to show to gain your degree', scopeNote='the only rung stated; classes above it are in Annex D (4.2)', category='unknown', practices=['education']),
      dict(slug='departments-or-history-subject-groups', definition='the statement\'s term for the unit that teaches History, whether a department or part of a wider cluster (D1, 1.3)', beneficiaryDefinition='the staff group that runs your History course', scopeNote='used throughout', category='unknown', practices=['education'])]
B2A = [dict(concept='historiography', form='historiography', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
       dict(concept='primary-source', form='primary sources', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
       dict(concept='formative-assessment', form='formative assessment', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='summative-assessment', form='summative assessment', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='extended-piece-of-work', form='extended piece of work', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='extended-piece-of-work', form='dissertation', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
       dict(concept='extended-piece-of-work', form='final year project', lang='en', partOfSpeech='noun-phrase', termStatus='admitted', register='formal'),
       dict(concept='flipped-lecture', form="'flipped' lectures", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='minimum threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='departments-or-history-subject-groups', form='departments or History subject groups', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = [dict(rel='contrasts-with', **{'from': 'formative-assessment'}, to='summative-assessment', note='1.11')]
B5 = []
D3 = []

E = [
    'SB4, rungs: one rung only, threshold. 4.5 (Minimum threshold standards, 12 subject-specific items) and 4.6 (Generic skills, 17 items) share one lead-in wording; 4.6 is recorded as threshold on 2.5\'s words "threshold-level subject-specific and generic skills" (the skeleton gave 4.6 no rung). No typical or excellent rung; 4.2 leaves the classes above threshold to Annex D. Pattern as Archaeology, unlike Psychology. For P3: confirm 4.6 as threshold.',
    'SB4, force: the threshold lead-ins say "should be able to"; force is recorded as should, the issuer\'s modal, not as threshold, although 4.1 and 4.5\'s heading call the lists the minimum. For Abbott: should a rung list with "should" take force threshold?',
    'SB4, gradeOf: none, since one rung is stated. SB4 outcomes is empty.',
    'S4, 1.7 and 4.5: the outcome list in section 1 (1.7, "should be able to") runs item for item with the 4.5 threshold list, 4.5 being shorter (4.5.b6 to b10 drop 1.7\'s second clauses). Both are recorded, as the template counts every outcome-list item; 1.7 is rung none. For P3: keep 1.7 or treat it as a duplicate of 4.5.',
    'S4, 1.5: its 18 items ("Students of history develop ... the ability to") repeat 4.6 almost word for word (1.5.b6 "evidence", 4.6.b6 "sources"; 1.5 splits digital literacy into its own item). The lead-in is plain present with no modal, so 1.5 is an S3 stem, not statements; 4.6 carries the standard.',
    'S4, 1.20: "requires History students to be proficient" is recorded with force must ("required" is must, batch-1 convention); the sentence describes what the work demands rather than imposing a rule. For Abbott.',
    'S4, obliging words outside the five, recorded as describes: "is essential" (2.1.b3, 2.1 c)), "are expected to" (2.1.b4, 2.1 d)), "it is the responsibility of departments" (2.4), "it is expected that" (2.5). Also "are essential" in 3.6 and "a shared commitment to and responsibility for" in 1.14, not taken (descriptive). For Abbott.',
    'S4, 2.1: the six features a) to f) are run-in letters inside one paragraph; ids 2.1.b2 to 2.1.b4 follow the letters (b = 2, c = 3, d = 4). a), e) and f) state plain-present norms ("Courses introduce students", "Students are introduced", "the student is enabled") and are not statements.',
    'S4, plain-present provider norms not taken as statements (template open point 5): 1.10, 1.11, 2.1 a), e), f), 2.2, 3.5, 3.6, 3.8, 4.4 ("Published criteria and grade descriptors are available"). Predictive or permissive "will" and "may" not taken: 1.3, 2.3 ("a History student will progress"), 2.7, 2.9, 2.12 ("external examiners will be asked"), 4.1, 4.3.',
    'S4, 4.1 is the rung\'s definition ("the minimum threshold standards that student will have demonstrated"), recorded in SB4 rungBases, not as a statement.',
    'S4, 3.10: the skeleton cut only one item (e) and f) run together over the page break); a) to f) are re-cut by find as 3.10.b1 to b6, taking "These should include" as lead-in. 3.10.b6 keeps the extraction\'s broken words ("task-s etti ng", "wri tten", "re quired") in its source.',
    'S4, verbs: 4.6.b16\'s span has "re flect" split by extraction, so only "make" is recorded; 4.6.b17 ("contempora ry", "relati ng", "sustainabilit y") and 4.6.b7 ("arg uments") also carry split words in source. 2.1.b3 has no action verb in its span.',
    'S4, provider statements carry no student version (2.1.b2, 2.4, 2.11, 3.7, 3.9, 3.10.b1 to b6, 3.11, 4.2).',
    'S5: fheq:6 and fqheis:10 are stated together at 2.3 and 4.2. 2.7 names exit awards (CertHE, DipHE) and four-year Scottish honours without levels; by the FHEQ document (S5, Table 1) these would be fheq:4 and fheq:5: inferred, not recorded as cited.',
    'S6 and SB6: theme paragraphs read from what each paragraph says; the skeleton\'s hits on 1.11, 1.15, 2.1 and 1.18 came from section headings that the extraction ran onto the end of those paragraphs, and were dropped. 1.15 ("environmental responsibility", "social justice") is not tagged esd or edi. 2.9 (placements) is linked from 1.19 but does not name enterprise: not tagged.',
    'SB5 and SB6 bodies: no professional, statutory or regulatory body is named in the body text; PSRBs appear generically in the front matter, and the Royal Historical Society, the Historical Association, The National Archives and the Disabled Students\' Commission only in the advisory group back matter (excluded). Prospects and HESA (1.21) are data sources, listed in sharedDocuments.',
    'S2, statedSubjects: no HECoS term for public, cultural, political or gender history; the generic history code covers them.',
    'S7: the fourth edition (2019) is named in the back matter only; std:doc:qaa-history-2019-benchmarks is our id for it, not ingested.',
    'S1, licence: the text gives a copyright notice and no re-use terms (template open point 3).',
    'S9: not researched in P1.',
    'Patterns that differ from Psychology: one rung only (threshold), no typical or excellent; generic skills given as a threshold list of their own (4.6) rather than an outcome list; an outcome list (1.7) duplicating the threshold list; lead-ins in "should be able to"; no PSRB; four themes, all in section 1 under their own headings; Annex D cited at 4.2 as part of the 2024 Frameworks.',
]
