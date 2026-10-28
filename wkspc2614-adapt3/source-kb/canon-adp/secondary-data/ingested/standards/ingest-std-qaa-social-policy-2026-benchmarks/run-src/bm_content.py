# bm_content.py: run 0129, QAA Subject Benchmark Statement: Social Policy (April 2026). std.
# Judgement file for tools/bm_build.py (BM-BRIEF 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft).
# Written fresh from the held text alone; no consuming project's files read (benchmark rule 6).
import re as _re

HON = "bachelor's with honours"
MAS = "master's"
CITE = '(QAA, 2026, Social Policy Subject Benchmark Statement, para %s)'

META = dict(
    run='0129', p1='2026-10-03 18:29',
    title='Subject Benchmark Statement: Social Policy',
    heading='Subject Benchmark Statement: Social Policy (QAA, April 2026)',
    edition='April 2026 (fifth edition)', published='2026-04',
    status='current', supersedes='the fourth edition, 2019 (minor update), as the back matter records',
    subjects=[
        dict(scheme='hecos', code='100502', label='social policy', basis='stated'),
        dict(scheme='cah', code='CAH15-01-03', label='social policy', basis='stated'),
    ],
    awards=[HON, MAS], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2026 revision (fifth edition for this subject)',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("QAA's UK reference point for what a Social Policy graduate can be expected to know, understand and do at the end "
                     "of an honours degree, with lists for master's graduates. It holds three-rung tables (threshold, typical, "
                     "excellent, tied to third, second and first-class honours) for knowledge and understanding, subject-specific "
                     "skills, generic intellectual skills and generic transferable skills, a long list of knowledge areas and four "
                     "master's lists. Reach for it when designing, reviewing or describing a Social Policy course, module or its "
                     "outcomes. It is not a curriculum and not a regulatory requirement in England."),
    summary=("Published by QAA in April 2026 as the fifth edition, the statement sets out the context and purposes of the subject "
             "(human welfare, need, social justice and resource distribution, across state, market, voluntary and family "
             "sectors), its distinctive features (design, progression, flexibility, partnership, monitoring), content, teaching "
             "and assessment, and benchmark standards. For the bachelor's degree with honours it gives three rungs, threshold "
             "(third class), typical (second class) and excellent (first class), in four tables; for the master's degree it "
             "gives four lists with no rungs. It carries five cross-cutting themes: equity, diversity and inclusion (with a "
             "strong decolonising strand); accessibility and the needs of disabled students; education for sustainable "
             "development (the UN goals); employability, entrepreneurship and enterprise education; and generative AI. It "
             "points to Annex D of the Frameworks for the four honours classes, cites the FHEQ and the FQHEIS (SCQF) for levels, "
             "and names PSRBs as a class, the Equality and Human Rights Commission and the Disabled Students Commission."),
    authority=('reference: a sector-owned reference point; in England not a sector-recognised standard under the OfS '
               'regulatory framework; part of the current quality arrangements in Scotland, Wales and Northern Ireland '
               '(D1, front matter: Relationship to legislation)'),
)

S2 = dict(
    governs=("what a Social Policy graduate can be expected to know, do and understand at the end of an honours degree, with "
             "standards for the master's degree, and the nature of awards in the subject (D1, front matter: About this "
             "Statement; 1.1; 4.1)"),
    awards=["bachelor's degree with honours", "integrated master's (described, 2.8, 2.12)", "taught master's degree (4.11 to 4.15)",
            "joint and combined honours (1.2, 2.10)", "CertHE and DipHE as exit awards (2.11)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    statedScope=('"This QAA Subject Benchmark Statement for Social Policy defines what can be expected of a graduate in terms '
                 'of what they might know, do, and understand at the end of their studies." (D1, front matter: About this Statement)'),
    doesNot=('it does not prescribe approaches to teaching, learning or assessment; it does not interpret legislation or carry '
             'statutory or regulatory requirements; its threshold standards are not universal competence standards '
             '(D1, front matter; 4.4)'),
    statedSubjects=[
        dict(name='Social Policy', locator='(D1, title; 1.1; 1.3)', kind='subject',
             codes=[dict(scheme='hecos', code='100502', label='social policy'),
                    dict(scheme='cah', code='CAH15-01-03', label='social policy')]),
        dict(name='Social Administration (the subject\'s historical root)', locator='(D1, 1.9)', kind='subject',
             codes=[dict(scheme='hecos', code='100090', label='public administration')]),
        dict(name='wider social science programmes', locator='(D1, 1.2; 3.1)', kind='programme title',
             codes=[dict(scheme='hecos', code='100471', label='social sciences')]),
        dict(name='Sociology, Politics, Criminology and Economics (degrees in which the subject is taught)', locator='(D1, 1.59)',
             kind='programme title',
             codes=[dict(scheme='hecos', code='100505', label='sociology'), dict(scheme='hecos', code='100491', label='politics'),
                    dict(scheme='hecos', code='100484', label='criminology'), dict(scheme='hecos', code='100450', label='economics')]),
        dict(name='Public Policy and Administration (overlapping field)', locator='(D1, 2.6)', kind='subject',
             codes=[dict(scheme='hecos', code='100647', label='public policy'), dict(scheme='hecos', code='100090', label='public administration')]),
        dict(name='combined or joint degree (including major and minor options)', locator='(D1, 1.2; 2.10)', kind='programme title',
             codes=[dict(scheme='cah', code='CAH15-01-03', label='social policy')]),
    ],
)

SECTIONS = {
    '1': 'Context and purposes of a Social Policy degree',
    '2': 'Distinctive features of the Social Policy degree',
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
}
SUB = [
    ('1.1', '1.15', 'Context and purposes of a Social Policy degree'),
    ('1.16', '1.28', 'Purposes and characteristics of a Social Policy degree'),
    ('1.29', '1.39', 'Equity, diversity and inclusion'),
    ('1.40', '1.43', 'Accessibility and the needs of disabled students'),
    ('1.44', '1.53', 'Education for sustainable development'),
    ('1.54', '1.59', 'Employability, entrepreneurship and enterprise education'),
    ('1.60', '1.66', 'Generative artificial intelligence'),
    ('2.1', '2.7', 'Design'),
    ('2.8', '2.11', 'Progression'),
    ('2.12', '2.13', 'Flexibility'),
    ('2.14', '2.14', 'Partnership'),
    ('2.15', '2.18', 'Monitoring and review'),
    ('3.1', '3.3', 'Content'),
    ('3.4', '3.9', 'Teaching and learning'),
    ('3.10', '3.17', 'Assessment'),
    ('4.1', '4.4', 'Introduction'),
    ('4.5', '4.10', 'Undergraduate programmes'),
    ('4.11', '4.15', "Master's programmes"),
]

G = {
    '1.1': 'what the statement sets out, for undergraduate and taught postgraduate study',
    '1.2': 'joint honours and standalone modules',
    '1.3': 'the discipline against the practice of policy',
    '1.4': 'welfare, need and justice; academic and applied',
    '1.5': 'dividing and allocating welfare resources',
    '1.6': 'who gains and loses; social divisions',
    '1.7': 'devolution, local government and subsidiarity',
    '1.8': 'policy in lived experience over the life course',
    '1.9': 'roots in Social Administration',
    '1.10': 'polycrises and resilient welfare',
    '1.11': 'welfare beyond the state',
    '1.12': 'the four sectors of provision',
    '1.13': 'racism and other structural discrimination',
    '1.14': 'environmental sustainability central to welfare',
    '1.15': 'safety net or wide provision',
    '1.16': 'entitlement, rights and citizenship',
    '1.17': 'regimes, governance and policy design',
    '1.18': 'cash, services and public finance',
    '1.19': 'research evidence, power and ideology',
    '1.20': 'a normative subject; values and research',
    '1.21': 'decolonising curricula',
    '1.22': 'UK history, empire and colonisation',
    '1.23': 'empire, Commonwealth and post-war rebuilding',
    '1.24': 'colonial legacies in analysis and funding',
    '1.25': 'blind spots of the canon',
    '1.26': 'global majority understandings',
    '1.27': 'cannot be fully decolonised; diversify teaching',
    '1.28': 'openness to diverse welfare systems',
    '1.29': 'varied starting points on entry',
    '1.30': 'diverse students; equity in teaching',
    '1.31': 'diverse needs and awarding gaps',
    '1.32': 'support and belonging for all',
    '1.33': 'constructive dialogue across views',
    '1.34': 'co-constructing curricula',
    '1.35': 'equity, diversity and inclusion defined',
    '1.36': 'good EDI practice in design',
    '1.37': 'applying EDI critically to policy debate',
    '1.38': 'self-reflection and others\' views',
    '1.39': 'graduates reflecting on inclusion and identity',
    '1.40': 'anticipatory accessibility under equality law',
    '1.41': 'diverse backgrounds as a learning resource',
    '1.42': 'four areas for inclusive, accessible courses',
    '1.43': 'placement support for disabled students',
    '1.44': 'sustainable development in welfare debate',
    '1.45': 'the UN goals described',
    '1.46': 'the subject aligned with the UN goals',
    '1.47': 'the UN goals as a way into eco-social policy',
    '1.48': 'welfare, economy and the environment',
    '1.49': 'goals in programme design; global problems',
    '1.50': 'ESD resources; Inner Development Goals',
    '1.51': 'sustainability across all teaching',
    '1.52': 'critiquing sustainability; climate and privilege',
    '1.53': 'sustainability and lifelong learning',
    '1.54': 'EEE for problem solving and careers',
    '1.55': 'EEE and careers services',
    '1.56': 'EEE through authentic assessment and placements',
    '1.57': 'accessible placements and volunteering',
    '1.58': 'EEE beyond placements',
    '1.59': 'graduate careers; teaching beside other subjects',
    '1.60': 'critical engagement with GenAI',
    '1.61': 'gains from GenAI in learning',
    '1.62': 'risks of GenAI',
    '1.63': 'integrating GenAI into teaching and assessment',
    '1.64': 'employability and responsible GenAI use',
    '1.65': 'institutional GenAI policy; teaching risks',
    '1.66': 'pointer to QAA GenAI resources',
    '2.1': 'core questions for any social problem',
    '2.2': 'five elements of programme design',
    '2.3': 'interdisciplinary knowledge; what students critique',
    '2.4': 'skills for policy analysis and communication',
    '2.5': 'debate, evidence and colonial influence',
    '2.6': 'social administration; reflective practice',
    '2.7': 'student contributions to review',
    '2.8': 'progression through the levels',
    '2.9': 'readiness for postgraduate study',
    '2.10': 'joint and combined degrees',
    '2.11': 'early exit awards',
    '2.12': 'course length and Scottish degrees',
    '2.13': 'modes of study and credit',
    '2.14': 'partnership delivery',
    '2.15': 'monitoring, review and student voice',
    '2.16': 'external reviewers in periodic review',
    '2.17': 'the external examining system',
    '2.18': 'professional accreditation',
    '3.1': 'a dynamic subject; core content without prescription',
    '3.2': 'insights at local to global scale; fields of policy',
    '3.3': 'knowledge areas of graduates, in five groups',
    '3.4': 'aims and methods of teaching',
    '3.5': 'virtual and distance learning',
    '3.6': 'experiences that prepare for work',
    '3.7': 'settings of learning',
    '3.8': 'learning methods students use',
    '3.9': 'mature learners and inclusive design',
    '3.10': 'constructive alignment; varied assessment',
    '3.11': 'authentic assessment recommended',
    '3.12': 'independent competence, GenAI and misconduct',
    '3.13': 'accessible, inclusive assessment principles',
    '3.14': 'indicative assessment types',
    '3.15': 'programme-level assessment diversity',
    '3.16': 'feedback throughout studies',
    '3.17': 'feedback on strengths for work',
    '4.1': 'what the standards cover, by level',
    '4.2': 'the three rungs defined by class',
    '4.3': 'performance above typical; Annex D',
    '4.4': 'not competence standards; EHRC guidance',
    '4.5': 'honours outcomes in line with the Frameworks',
    '4.6': 'not a checklist; rungs cumulative',
    '4.7': 'knowledge and understanding table',
    '4.8': 'subject-specific skills table',
    '4.9': 'generic intellectual skills table',
    '4.10': 'generic transferable skills table',
    '4.11': 'master\'s standards; not a checklist',
    '4.12': 'master\'s knowledge and understanding list',
    '4.13': 'master\'s subject-specific skills list',
    '4.14': 'master\'s generic intellectual skills list',
    '4.15': 'master\'s generic transferable skills list',
}

CTYPE = {
    '3.2': 'area', '3.3': 'area',
    '3.4': 'practice', '3.5': 'practice', '3.6': 'practice', '3.7': 'practice', '3.8': 'practice',
    '3.10': 'practice', '3.11': 'practice', '3.13': 'practice', '3.14': 'practice', '3.15': 'practice', '3.16': 'practice',
}

EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='section headings 1 to 4', heading='the four section heading lines and the lead paragraph of section 3', kind='other: headings, recorded in SECTIONS'),
    dict(number='footnote 1', heading='definition of polycrises (page 4)', kind='other: footnote, read for Part B'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for SB6 and Part E'),
    dict(number='6', heading='Membership of the Advisory Group (2026, 2019, 2016, 2007, 2000)', kind='other: back matter, read for S7 and S8'),
    dict(number='none', heading='Fifth Edition; Published 16 April 2026; copyright notice', kind='other: colophon, read for S1 and S8'),
]

P = {}
GRADE = {}
OUT = []


def s(i, **k):
    P[i] = k


def you(x):
    x = _re.sub(r'\bthemselves\b', 'yourself', x)
    x = _re.sub(r'\btheir\b', 'your', x)
    return _re.sub(r'\bthey\b', 'you', x)


# ================================================================== rung tables 4.7 to 4.10 (honours)
CLASS = {'threshold': 'third-class', 'typical': 'second-class', 'excellent': 'first-class'}


def aaw_cell(n, rung, about, others, fw):
    if rung == 'threshold':
        head = ("Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 "
                "(FQHEIS Level 10): %s." % about)
        tail = 'or apply it to the master\'s award'
    else:
        head = ("Present this as the %s standard, the attainment the statement requires for %s honours in Social Policy at FHEQ "
                "Level 6 (FQHEIS Level 10): %s." % (rung, CLASS[rung], about))
        tail = 'or present it as the minimum to pass'
    return ("%s Cite it as %s, %s column. Do not call it a regulatory requirement %s. Set it beside %s in the same row, %s and "
            "spine:6." % (head, CITE % n, rung, tail, others, fw))


def aad_cell(rung, when, ask):
    if rung == 'threshold':
        put = 'the least you need to show to gain honours at all'
        avoid = 'or suggesting the threshold is what most students aim for'
    elif rung == 'typical':
        put = 'what a second-class result asks of you'
        avoid = 'and never present this typical standard as the minimum for a pass'
    else:
        put = 'what a first-class result asks of you'
        avoid = 'and never present this excellent standard as the minimum or as expected of everyone'
    return ("Raise this when %s. With a student, put it in plain second-person words as %s; with staff, frame it as what "
            "teaching and assessment must give students room to show. Ask: \"%s\" Avoid reading the table aloud %s." % (when, put, ask, avoid))


def cell(i, rung, dom, c, n, others, when):
    x = c['x']
    xb = c.get('xb', you(x))
    if rung == 'threshold':
        para = 'At the threshold for third-class honours, graduates %s.' % x
        prac = 'Every honours route must give students the chance to %s; this is the minimum for third-class honours.' % x
        ben = 'To gain honours at all, you need to be able to %s.' % xb
        force, ty = 'threshold', 'threshold'
    else:
        para = 'At the %s standard, required for %s honours, graduates %s.' % (rung, CLASS[rung], x)
        prac = 'For %s honours the statement requires that students %s; design tasks that let them show it.' % (CLASS[rung], x)
        ben = 'For a %s degree, you need to be able to %s.' % (CLASS[rung], xb)
        force, ty = 'must', rung
    s(i, find=c['find'], type=ty, rung=rung, force=force, forceFrom='4.2', level='fheq:6',
      appliesTo='honours graduates at the %s standard (%s)' % (rung, CLASS[rung]), addressee='learner', verbs=c['verbs'],
      about=c['about'], domain=dom, award=HON, para=para, prac=prac, ben=ben,
      aaw=aaw_cell(n, rung, c['about'], others, c['fw']), aad=aad_cell(rung, when, c['ask']))


def row(n, k, dom, t, y, e, when, out):
    ti, yi, ei = '%s.b%d' % (n, k), '%s.b%d.typical' % (n, k), '%s.b%d.excellent' % (n, k)
    cell(ti, 'threshold', dom, t, n, '%s and %s' % (yi, ei), when)
    cell(yi, 'typical', dom, y, n, '%s and %s' % (ti, ei), when)
    cell(ei, 'excellent', dom, e, n, '%s and %s' % (ti, yi), when)
    GRADE[yi] = ti + '|stated'
    GRADE[ei] = yi + '|stated'
    OUT.append(dict(outcome=out, threshold=ti, typical=yi, excellent=ei, basis='stated', domain=dom, award=HON))


# ---- 4.7 Knowledge and understanding
row('4.7', 1, 'knowledge', dict(
    find='Demonstrate factual knowledge of important historical and contemporary social policy events, issues and policies.',
    verbs=['demonstrate'], about='factual knowledge of past and present policy events',
    x='show they know the facts of significant social policy events, issues and policies, past and present',
    ask='Which major social policy events or reforms, past and recent, could you describe accurately?',
    fw='qaa/fheq-2024/4.15.b1 and Annex D qaa/fheq-2024/annex-d/knowledge/r1/3rd'),
    dict(find=('Demonstrate in-depth knowledge, understanding and critical awareness of key aspects of Social Policy analysis, including, '
               'for example, how social policies operate in local, national and international contexts in developing a sustainable '
               'future, with specific reference to the UN Sustainable Development Goals (SDGs).'),
         verbs=['demonstrate', 'operate'], about='deep, critical knowledge of policy analysis, sustainability included',
         x=('show deep knowledge and critical awareness of central parts of policy analysis, such as how policies at local, '
            'national and international scale bear on a sustainable future and the UN goals'),
         ask='How would you explain the way one policy, at local or national level, helps or hinders progress on a UN goal?',
         fw='qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.15.b3.2 and Annex D qaa/fheq-2024/annex-d/knowledge/r1/2.2 and 2.1'),
    dict(find=('Critique the role and evaluate the effects of policies in the main social policy areas across the UK and internationally, '
               'including new and emerging issues.'),
         verbs=['critique', 'evaluate'], about='critique and evaluation of policy across the main fields',
         x='critique what policies do and weigh their effects across the main policy fields, in the UK and abroad, emerging issues included',
         xb='critique what policies do and weigh their effects across the main policy fields, in the UK and abroad, emerging issues included',
         ask='Pick a policy field: what has a recent policy achieved, what has it missed, and how do you know?',
         fw='qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/knowledge/r1/1st'),
    'a student asks how much policy knowledge they need, or a team plans core policy content', 'knowledge of policies and their effects')
row('4.7', 2, 'understanding', dict(
    find=('Understand and compare how social policies operate across the UK and internationally, with particular emphasis on, but not '
          'limited to, health, education, housing, employment, social protection/income maintenance and social care.'),
    verbs=['understand', 'compare', 'operate'], about='how policies work in the UK and elsewhere',
    x='understand and compare the workings of social policies in the UK and in other countries, notably in health, education, housing, work, income support and care',
    ask='How does one service, say housing or social care, work differently in two countries or UK nations?',
    fw='qaa/fheq-2024/4.15.b1 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/3rd'),
    dict(find='Distinguish, compare and critique welfare systems across different parts of the world.',
         verbs=['distinguish', 'compare', 'critique'], about='comparative critique of welfare systems',
         x='tell welfare systems in different regions of the world apart, compare them and critique them',
         ask='What sets two welfare systems you have studied apart, and which do you find weaker, and why?',
         fw='qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/2.2 and 2.1'),
    dict(find=('Classify and critically evaluate the rationales for, coherence and effects of different types of welfare states and '
               'social policies, including their respective implications for different groups.'),
         verbs=['classify', 'evaluate'], about='typing and judging welfare states and their effects on groups',
         x='sort types of welfare state and policy, and critically judge the reasoning, consistency and effects of each, including what each means for different groups',
         ask='Which welfare regime type fits a country you know, and who gains or loses most under it?',
         fw='qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/1st'),
    'a student is comparing countries or welfare regimes', 'comparing welfare systems')
row('4.7', 3, 'understanding', dict(
    find='Discuss, contrast and apply core theories, concepts, perspectives and methods relevant to Social Policy.',
    verbs=['discuss', 'contrast', 'apply'], about='using the core theories and concepts',
    x='discuss, set against each other and use the main theories, concepts, perspectives and methods of the subject',
    ask='Which two theories of welfare could you compare, and how have you used one in your work?',
    fw='qaa/fheq-2024/4.15.b2 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/3rd'),
    dict(find='Categorise and engage critically with core theories, concepts, perspectives and methods relevant to Social Policy.',
         verbs=['categorise', 'engage'], about='critical engagement with core theory',
         x='group the main theories, concepts, perspectives and methods of the subject and engage with them critically',
         ask='Where does a theory you use fall short, and what would a critic say?',
         fw='qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/2.1'),
    dict(find='Analyse, classify, synthesise and critique core theories, concepts, perspectives and methods relevant to Social Policy.',
         verbs=['analyse', 'classify', 'synthesise', 'critique'], about='synthesis and critique of core theory',
         x='analyse, sort, bring together and critique the main theories, concepts, perspectives and methods of the subject',
         ask='Can you combine two perspectives into an argument of your own, and say where both fall short?',
         fw='qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/1st'),
    'a student is choosing or using theory in an essay', 'core theories and concepts')
row('4.7', 4, 'knowledge', dict(
    find='Demonstrate awareness of the UN SDGs.',
    verbs=['demonstrate'], about='awareness of the UN goals',
    x='show they are aware of the UN Sustainable Development Goals',
    ask='Which of the UN goals touch the policy areas you study?',
    fw='qaa/fheq-2024/4.15.b1'),
    dict(find='Apply their knowledge and understanding of UN SDGs across a wide range of social policy issues.',
         verbs=['apply'], about='applying the UN goals to many issues',
         x='use what they know of the UN goals on many different social policy issues',
         ask='Take two different policy issues: how do the UN goals bear on each?',
         fw='qaa/fheq-2024/4.15.b3.1'),
    dict(find=('Construct analysis of social problems and social policies which integrate the principles of sustainable development, '
               'which embed the UN SDGs.'),
         verbs=['construct', 'integrate', 'embed'], about='analysis built on sustainable development',
         x='build analyses of social problems and policies with sustainable development principles and the UN goals at the core',
         ask='How would your analysis of this problem change if sustainability were built in from the start?',
         fw='qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r4/1st'),
    'sustainability or the UN goals come up, or a team plans sustainability content', 'sustainable development and the UN goals')

# ---- 4.8 Subject-specific skills
row('4.8', 1, 'subject-skill', dict(
    find='Recall key characteristics of different social problems.',
    verbs=['recall'], about='features of social problems',
    x='recall the main features of a range of social problems',
    ask='What marks out two social problems you have studied, such as poverty and homelessness?',
    fw='Annex D qaa/fheq-2024/annex-d/knowledge/r1/3rd'),
    dict(find='Utilise key conceptual frameworks to analyse complex social questions, issues and problems.',
         verbs=['utilise', 'analyse'], about='frameworks used to analyse complex problems',
         x='use central conceptual frameworks to analyse complex social questions and problems',
         ask='Which framework helped you make sense of a complex social problem, and how?',
         fw='qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/practical/r1/2.2'),
    dict(find=('Construct critical analysis of key social problems and policy responses, and evaluate alternative solutions using '
               'relevant analytical tools and research methods.'),
         verbs=['construct', 'evaluate', 'using'], about='critical analysis of problems and alternative solutions',
         x='build critical analyses of major social problems and the policies aimed at them, and weigh other solutions with suitable analytical tools and research methods',
         ask='What alternative to the current policy on this problem would you propose, and what evidence would test it?',
         fw='qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r3/1st'),
    'a student is analysing a social problem', 'analysing social problems')
row('4.8', 2, 'subject-skill', dict(
    find='Summarise and contrast core Social Policy theories, concepts and perspectives.',
    verbs=['summarise', 'contrast'], about='summary and contrast of core theory',
    x="sum up the subject's main theories, concepts and perspectives and show how they differ",
    xb="sum up the subject's main theories, concepts and perspectives and show how they differ",
    ask='Can you sum up two perspectives on welfare and say how they differ?',
    fw='qaa/fheq-2024/4.15.b2'),
    dict(find=('Understand and apply core theories, concepts and perspectives in Social Policy and appreciate their relevance for '
               'other subjects and practitioners.'),
         verbs=['understand', 'apply', 'appreciate'], about='applying core theory, for other fields too',
         x="understand and use the subject's main theories, concepts and perspectives, and see why they matter to other disciplines and to practitioners",
         xb="understand and use the subject's main theories, concepts and perspectives, and see why they matter to other disciplines and to practitioners",
         ask='Why might a practitioner, or a student of another subject, find this theory useful?',
         fw='qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/2.2'),
    dict(find='Critically classify, compare, synthesise and evaluate core Social Policy theories, concepts and perspectives.',
         verbs=['classify', 'compare', 'synthesise', 'evaluate'], about='critical synthesis and evaluation of core theory',
         x="critically sort, compare, combine and judge the subject's main theories, concepts and perspectives",
         ask='Which perspective holds up best against the evidence in your topic, and why?',
         fw='Annex D qaa/fheq-2024/annex-d/knowledge/r2/1st'),
    'a student is working with theory', 'using theory')
row('4.8', 3, 'subject-skill', dict(
    find='Recognise how ideology, values, interests and norms can affect and shape social policies.',
    verbs=['recognise', 'affect', 'shape'], about='ideology and values in policy',
    x='see how ideology, values, interests and norms can influence and form social policies',
    ask='What values or interests lie behind a policy you have studied?',
    fw='qaa/fheq-2024/4.15.b1'),
    dict(find=('Distinguish between normative values and empirical claims, and critically reflect on how values underpin and shape '
               'policy making and relate to empirical evidence.'),
         verbs=['distinguish', 'reflect', 'underpin', 'shape', 'relate'], about='values against evidence in policy making',
         x='tell normative values from empirical claims and reflect critically on how values drive policy making and connect with evidence',
         ask='In this policy debate, which claims are about values and which can be tested with evidence?',
         fw='qaa/fheq-2024/4.15.b7'),
    dict(find='Understand the relevance of and apply different ideological positions, values, and norms to the analysis of social policies.',
         verbs=['understand', 'apply'], about='ideological positions applied in analysis',
         x='understand why different ideological positions, values and norms matter and use them in analysing social policies',
         ask='How would two ideological positions read the same policy differently?',
         fw='qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/1st'),
    'values, ideology or politics in policy come up', 'values and ideology in policy')
row('4.8', 4, 'subject-skill', dict(
    find='Understand and explain the importance of human need and lived experience to social policies.',
    verbs=['understand', 'explain'], about='need and lived experience in policy',
    x='understand and explain why human need and lived experience matter to social policies',
    ask='How does lived experience change our understanding of what a policy does?',
    fw='qaa/fheq-2024/4.15.b1'),
    dict(find=('Demonstrate sensitivity to the values and interests of others to appreciate the diversity of human needs and understand '
               'how they can be addressed through social policy analysis and policy making and implementation processes.'),
         verbs=['demonstrate', 'appreciate', 'understand', 'addressed'], about='sensitivity to others and to diverse needs',
         x="show sensitivity to other people's values and interests, appreciate how varied human needs are and understand how analysis, policy making and implementation can meet them",
         ask='Whose needs does this policy overlook, and how could the process have heard them?',
         fw='qaa/fheq-2024/4.15.b7'),
    dict(find=('Critically evaluate the significance of lived experience to social policy analysis and policies and apply insights '
               'from this where relevant.'),
         verbs=['evaluate', 'apply'], about='lived experience weighed and applied',
         x='critically judge how much lived experience matters to policy analysis and to policies, and use what it shows where it fits',
         ask='Where have you used evidence from lived experience, and how did you weigh it against other evidence?',
         fw='Annex D qaa/fheq-2024/annex-d/cognitive/r1/1st'),
    "a student is working with service users' views or lived experience", 'human need and lived experience')
row('4.8', 5, 'subject-skill', dict(
    find='Assess and undertake Social Policy research using relevant methods.',
    verbs=['assess', 'undertake', 'using'], about='assessing and doing research',
    x='assess research in the subject and carry out their own with suitable methods',
    ask='What method did you choose for your research, and why did it fit the question?',
    fw='qaa/fheq-2024/4.15.b6 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/3rd'),
    dict(find=('Apply knowledge and experience of research methods to provide informed and critical commentary on the quality of '
               'Social Policy research.'),
         verbs=['apply', 'provide'], about='critical comment on research quality',
         x='draw on what they know and have done with research methods to comment critically and knowledgeably on how good research in the subject is',
         ask='How strong was the method in a study you read recently, and what would you have done differently?',
         fw='qaa/fheq-2024/4.15.b3.2 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/2.1'),
    dict(find=('Plan, develop and undertake valid and robust Social Policy research using relevant methods and applying appropriate '
               'ethical standards.'),
         verbs=['plan', 'develop', 'undertake', 'using', 'applying'], about='valid, robust and ethical research',
         x='plan, build and carry out valid, robust research in the subject with suitable methods and proper ethical standards',
         ask='How did you make your research valid and ethical, and what would an examiner question?',
         fw='qaa/fheq-2024/4.15.b6 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/1st'),
    'a student is planning a dissertation or reading research critically', 'research')

# ---- 4.9 Generic intellectual skills
row('4.9', 1, 'generic-skill', dict(
    find=('Reasoned arguments: the ability to construct and develop coherent and logical arguments, discuss issues and propose responses.'),
    verbs=['construct', 'develop', 'discuss', 'propose'], about='coherent, logical argument',
    x='build and develop arguments that hang together logically, talk issues through and suggest responses',
    ask='What is your argument in one sentence, and does each step follow?',
    fw='qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/3rd'),
    dict(find=('Independent reasoning: the ability to construct and develop substantiated, evidence-based arguments, discuss issues and '
               'solve problems using appropriate information and critical judgement.'),
         verbs=['construct', 'develop', 'discuss', 'solve', 'using'], about='independent, evidence-based argument',
         x='reason for themselves, building arguments backed by evidence and using fitting information and critical judgement to discuss issues and solve problems',
         ask='What evidence carries your argument, and where did you rely on your own judgement?',
         fw='qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/2.2 and 2.1'),
    dict(find=('Creative and independent reasoning: the ability to construct and develop a coherent, logical, valid and evidence-based '
               'argument to discuss issues and solve problems.'),
         verbs=['construct', 'develop', 'discuss', 'solve'], about='creative, independent and valid argument',
         x='reason creatively and for themselves, building a coherent, valid argument grounded in evidence to discuss issues and solve problems',
         ask='What in your argument is your own, beyond what the reading says?',
         fw='Annex D qaa/fheq-2024/annex-d/cognitive/r4/1st and qaa/fheq-2024/annex-d/cognitive/r2/1st'),
    'a student asks what makes an argument stronger or why a mark was held back', 'reasoning and argument')
row('4.9', 2, 'generic-skill', dict(
    find='Analytical skills: the ability to read, listen/watch and accurately summarise, restate and assess content.',
    verbs=['read', 'listen', 'watch', 'summarise', 'restate', 'assess'], about='accurate summary and assessment of content',
    x='read, listen to or watch material and summarise, restate and assess it accurately',
    ask='Can you summarise this report accurately in a few lines and say how good it is?',
    fw='Annex D qaa/fheq-2024/annex-d/cognitive/r1/3rd'),
    dict(find=('Evaluative and analytical skills: the ability to critically and thoroughly assess and summarise assumptions, arguments '
               'and evidence from reports, documents and audiovisual sources.'),
         verbs=['assess', 'summarise'], about='thorough evaluation of assumptions and evidence',
         x='assess and summarise, thoroughly and critically, the assumptions, arguments and evidence in reports, documents and audiovisual material',
         ask='What does this report assume without saying so?',
         fw='qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r1/2.1'),
    dict(find=('Critical analytical skills: the ability to read, listen/watch material and critically analyse its strength and '
               'weaknesses, offering evidence-based alternatives where relevant.'),
         verbs=['read', 'listen', 'watch', 'analyse', 'offering'], about='critical analysis with evidenced alternatives',
         x='read, listen to or watch material, analyse its strengths and weaknesses critically and, where it helps, offer alternatives backed by evidence',
         ask='Where is this source weakest, and what better-evidenced view would you put in its place?',
         fw='Annex D qaa/fheq-2024/annex-d/cognitive/r1/1st'),
    'a student is reading or reviewing sources', 'analysing material')
row('4.9', 3, 'generic-skill', dict(
    find='Problem-solving skills: the ability to identify challenging social issues and assess alternative responses.',
    verbs=['identify', 'assess'], about='spotting hard issues and weighing responses',
    x='identify hard social issues and weigh the different responses to them',
    ask='What is a hard social issue you have studied, and which responses to it did you compare?',
    fw='Annex D qaa/fheq-2024/annex-d/cognitive/r3/3rd'),
    dict(find='Problem-solving skills: the ability to critically analyse issues and assess alternative evidence-based solutions.',
         verbs=['analyse', 'assess'], about='critical analysis and evidenced solutions',
         x='analyse issues critically and weigh different solutions that rest on evidence',
         ask='Which solution has the strongest evidence behind it?',
         fw='Annex D qaa/fheq-2024/annex-d/cognitive/r3/2.2 and 2.1'),
    dict(find=('Problem-solving skills: the ability to critically evaluate issues and develop and assess alternative evidence- based '
               'responses.'),
         verbs=['evaluate', 'develop', 'assess'], about='devising and testing evidenced responses',
         x='evaluate issues critically and devise and test different responses grounded in evidence',
         ask='Which response would you design yourself, and how would you test it?',
         fw='Annex D qaa/fheq-2024/annex-d/cognitive/r3/1st'),
    'a student is working on a policy problem or case study', 'problem-solving')
row('4.9', 4, 'generic-skill', dict(
    find=('Data collection and research skills: the ability to devise and undertake a research project, including planning, '
          'collecting and analysing data and writing, with supervisory support.'),
    verbs=['devise', 'undertake', 'planning', 'collecting', 'analysing'], about='a supervised research project',
    x="design and complete a research project, from planning through data collection and analysis to writing, with a supervisor's help",
    ask='Which parts of your project did you plan yourself, and where did your supervisor step in?',
    fw='qaa/fheq-2024/4.15.b6 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/3rd'),
    dict(find=('Data collection and research skills: the ability to work independently to retrieve, record, synthesise and analyse '
               'information gathered from various sources.'),
         verbs=['work', 'retrieve', 'record', 'synthesise', 'analyse'], about='independent gathering and analysis of information',
         x='work on their own to find, record, combine and analyse information from a range of sources',
         ask='How do you find and keep track of your sources without being told where to look?',
         fw='qaa/fheq-2024/4.15.b5 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/2.2'),
    dict(find=('Independent research skills: the ability to independently devise and undertake a research project, including '
               'planning, collecting and analysing data and writing up results.'),
         verbs=['devise', 'undertake', 'planning', 'collecting', 'analysing'], about='an independent research project',
         x='design and complete a research project on their own, from planning and data work to writing up findings',
         ask='Which decisions in your project were wholly yours?',
         fw='qaa/fheq-2024/4.15.b6 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/1st'),
    'a student is planning a dissertation or research project', 'research projects')
# the orphan cell: one cell after the research row, read as excellent (Part E)
cell('4.9.b5.excellent', 'excellent', 'generic-skill', dict(
    find='Synthesis skills: the ability to accurately combine and integrate diverse information sources to develop new knowledge or arguments.',
    verbs=['combine', 'integrate', 'develop'], about='synthesis into new knowledge or argument',
    x='bring varied sources together accurately to build new knowledge or arguments',
    ask='What new argument came out of putting your sources together?',
    fw='Annex D qaa/fheq-2024/annex-d/cognitive/r1/1st'),
    '4.9', '4.9.b4.excellent (the research row; this cell has no threshold or typical partner)',
    'a student is drawing many sources together for a dissertation or long essay')
OUT.append(dict(outcome='synthesis', threshold='none', typical='none', excellent='4.9.b5.excellent', basis='stated',
                domain='generic-skill', award=HON))

# ---- 4.10 Generic transferable skills
row('4.10', 1, 'generic-skill', dict(
    find=('Communication and presentation skills: the ability to communicate and present effectively in writing, verbally/non-verbally '
          'and visually, to different audiences using appropriate technical aids.'),
    verbs=['communicate', 'present', 'using'], about='effective communication to varied audiences',
    x='communicate and present well in writing, in speech and other forms, and visually, to varied audiences with suitable technical aids',
    ask='How did you adapt your last presentation for its audience?',
    fw='qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd'),
    dict(find=('Communication and presentation skills: to communicate effectively with different audiences across a range of formats, '
               'including written, verbal/non-verbal and visual, and to use technical aids where appropriate.'),
         verbs=['communicate', 'use'], about='effective communication across formats',
         x='communicate well with varied audiences in many formats, written, spoken and visual, using technical aids where useful',
         ask='Which formats have you used to share your work, and which suited which audience?',
         fw='Annex D qaa/fheq-2024/annex-d/transferable/r1/2.2 and 2.1'),
    dict(find=('Communication and presentation skills: the ability to articulate a coherent and complex argument and communicate ideas '
               'effectively both verbally/non-verbally and in writing, and, where appropriate, use technical aids to develop and '
               'deliver complex presentations to an audience.'),
         verbs=['articulate', 'communicate', 'use', 'develop', 'deliver'], about='complex argument put across; complex presentations',
         x='put a complex, coherent argument into words, communicate ideas well in speech and writing and, where useful, use technical aids to build and give complex presentations',
         ask='Could you present your most complex argument to a non-specialist audience in ten minutes?',
         fw='Annex D qaa/fheq-2024/annex-d/transferable/r1/1st'),
    'a student prepares a presentation, briefing or written piece', 'communication')
row('4.10', 2, 'generic-skill', dict(
    find='Self-directed learning: the ability to plan, organise and prioritise work to meet deadlines.',
    verbs=['plan', 'organise', 'prioritise', 'meet'], about='planning work to deadlines',
    x='plan, organise and order their work so they meet deadlines',
    ask='How do you plan your week when two deadlines fall together?',
    fw='Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd'),
    dict(find='Self-directed learning: the ability to plan, manage time effectively and work independently.',
         verbs=['plan', 'manage', 'work'], about='time management and independent work',
         x='plan, use their time well and work on their own',
         ask='Where do you work best without guidance, and where do you still need it?',
         fw='Annex D qaa/fheq-2024/annex-d/transferable/r3/2.2 and 2.1'),
    dict(find='Self-directed learning: the ability to design projects, organise resources, locate sources and exercise independent judgement.',
         verbs=['design', 'organise', 'locate', 'exercise'], about='designing projects; independent judgement',
         x='design projects, marshal resources, find sources and use their own judgement',
         ask='Which project have you shaped yourself from the start?',
         fw='qaa/fheq-2024/4.15.b9.1 and Annex D qaa/fheq-2024/annex-d/transferable/r3/1st'),
    'a student is struggling with workload or moving to independent study', 'self-directed learning')
row('4.10', 3, 'generic-skill', dict(
    find='Team and group working: the ability to form, engage and work effectively in groups.',
    verbs=['form', 'engage', 'work'], about='effective group work',
    x='form groups, take part and work well within them',
    ask='What did you contribute to your last group task?',
    fw='Annex D qaa/fheq-2024/annex-d/transferable/r2/3rd'),
    dict(find='Teamwork skills: the ability to initiate, coordinate and contribute effectively to group work and collective projects.',
         verbs=['initiate', 'coordinate', 'contribute'], about='starting and coordinating group work',
         x='start, coordinate and contribute well to group work and shared projects',
         ask='Have you ever set a group task going or kept one on track, and how?',
         fw='Annex D qaa/fheq-2024/annex-d/transferable/r2/2.2 and 2.1'),
    dict(find='Team and group working: the ability to initiate, form, engage constructively and work effectively in groups.',
         verbs=['initiate', 'form', 'engage', 'work'], about='starting groups and engaging constructively',
         x='start and form groups, engage constructively and work well within them',
         ask='How did you handle disagreement in a group you led?',
         fw='Annex D qaa/fheq-2024/annex-d/transferable/r2/1st'),
    'group work is set or a group is not working well', 'teamwork')
row('4.10', 4, 'generic-skill', dict(
    find=('Technology skills: the ability to use existing and new technologies and show awareness of evolving technologies, including '
          'appropriate, specific use of generative artificial intelligence tools.'),
    verbs=['use', 'show'], about='using technologies, generative AI included',
    x='use current and new technologies, know about emerging ones and use generative AI tools fittingly for specific tasks',
    ask='Which digital tools, generative AI included, did you use on your last assignment, and for what?',
    fw='Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd'),
    dict(find=('Technology skills: competent and confident use of a wide range of existing and new technologies to retrieve, analyse '
               'and present information, including appropriate, specific use of generative artificial intelligence tools.'),
         verbs=['retrieve', 'analyse', 'present'], about='confident use of technology to handle information',
         x='use a wide range of current and new technologies competently and confidently to find, analyse and present information, generative AI tools included where fitting',
         ask='How confident are you using software to analyse data, and how do you check what an AI tool gives you?',
         fw='Annex D qaa/fheq-2024/annex-d/transferable/r1/2.2 and 2.1'),
    dict(find=('Technology skills: proficient ability to use existing, new and evolving technologies, including appropriate, specific use '
               'of generative artificial intelligence tools.'),
         verbs=['use'], about='proficient use of evolving technology',
         x='use current, new and emerging technologies proficiently, generative AI tools included where fitting',
         ask='Which new tool have you mastered recently, and where would you not use it?',
         fw='Annex D qaa/fheq-2024/annex-d/transferable/r1/1st'),
    'a student asks about digital tools or generative AI', 'technology')
row('4.10', 5, 'generic-skill', dict(
    find='Evidence and referencing skills: the ability to accurately reference sources to provide evidence for submitted work.',
    verbs=['reference', 'provide'], about='accurate referencing',
    x='reference their sources accurately as evidence for the work they hand in',
    ask='How do you make sure every source in your essay is credited accurately?',
    fw='Annex D qaa/fheq-2024/annex-d/professional/r2/3rd-1st'),
    dict(find='Evidence and referencing skills: understand and correctly apply standard systems for accurate referencing in texts and reference lists.',
         verbs=['understand', 'apply'], about='standard referencing systems',
         x='understand standard referencing systems and apply them correctly in the text and the reference list',
         ask='Which referencing system do you use, and where does it trip you up?',
         fw='Annex D qaa/fheq-2024/annex-d/professional/r2/3rd-1st'),
    dict(find='Evidence and referencing skills: the ability to locate and accurately reference sources in accordance with academic conventions.',
         verbs=['locate', 'reference'], about='finding and referencing sources to convention',
         x='find sources and reference them accurately as academic convention requires',
         ask='How did you find the sources nobody pointed you to, and are they referenced correctly?',
         fw='Annex D qaa/fheq-2024/annex-d/knowledge/r3/1st'),
    'referencing, plagiarism or academic integrity come up', 'evidence and referencing')


# ================================================================== 3.3 knowledge areas (plain present; describes)
GROUP = {
    'A': ('welfare systems', 'a team plans core content on welfare history and systems, or a student asks what they should know of them',
          'qaa/fheq-2024/4.15.b1'),
    'B': ('policy processes', 'policy making, governance or implementation is the topic', 'qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b3.2'),
    'C': ('impacts', 'the effects of policy on people and groups are being studied', 'qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b7'),
    'D': ('concepts and theories', "a student or team is working with the subject's core concepts and theories",
          'qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b2'),
    'E': ('research and policy analysis', 'research methods, evaluation or a dissertation are being planned',
          'qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6'),
}


def k33(b, grp, verbs, about, x, ask, find=None):
    label, when, fw = GROUP[grp]
    i = '3.3.b%d' % b
    k = dict(type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='graduates of Social Policy courses',
             addressee='learner', verbs=verbs, about=about, domain='knowledge', award=HON,
             para='Graduates show knowledge of %s.' % x,
             prac='Teach %s, so that graduates can show knowledge of it.' % x,
             ben='By graduation you have knowledge of %s.' % you(x),
             aaw=("Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present "
                  "with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): %s. Cite it as %s, in the group on %s. "
                  "Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. "
                  "Set it beside the 4.7 knowledge rows, %s and spine:6." % (about, CITE % '3.3', label, fw)),
             aad=("Raise this when %s. With a student, ask in plain second-person words what they already know of it; with staff, ask "
                  "where in the course it is taught. Ask: \"%s\" Avoid presenting the list as a checklist every module must cover." % (when, ask)))
    if find:
        k['find'] = find
    s(i, **k)


k33(1, 'A', ['operate'], 'origins of welfare institutions and their settings',
    'how welfare institutions arose and grew in the UK and elsewhere, and their economic, social, demographic and political settings',
    'How did the welfare institutions you study come about, and what pressures shaped them?')
k33(2, 'A', ['shaped', 'continue'], 'historical roots of discrimination in welfare',
    'the historical forces, colonialism, capitalism and industrialisation among them, behind lasting discrimination, and how their legacy still shapes welfare',
    'Which historical force still shapes who is treated unequally by welfare today?')
k33(3, 'A', [], 'drivers of social change',
    'drivers of social change such as climate change, sustainability, globalisation, the media and social movements',
    'Which force for change, such as globalisation or a social movement, has most altered the policy area you study?')
k33(4, 'A', [], 'main welfare institutions and their work',
    'what the main UK and global welfare institutions do and how they are organised, funded and regulated across security, education, work, health, care and housing',
    'Who funds and regulates the main institution in your policy area, and what does it do day to day?')
k33(5, 'A', ['drawing'], 'shared features and challenges of welfare institutions',
    'common features and shared challenges of welfare institutions worldwide, in efficacy, equity, sustainability and political backing, from comparative study',
    'What challenge do welfare institutions in different countries share, and how do they meet it?')
k33(6, 'A', ['organise', 'determine', 'realise'], 'how countries organise and pursue policy goals',
    'how countries organise their social policies and institutions, set goals politically and how well they meet them',
    'How does one country set its welfare goals, and how well does it reach them?')
k33(7, 'A', [], 'policy in sustainability and the climate crisis',
    'the part policy plays, globally and nationally, in sustainability and the climate crisis, including growth or degrowth, energy and environmental injustice',
    'Who bears the cost of climate change in the communities you study, and what can policy do about it?')
k33(8, 'A', ['driving', 'emerged'], 'ideas and thinkers of the subject in context',
    'the ideas, principles and key thinkers behind the subject, read in the historical settings that produced them',
    'Which thinker shaped the subject most for you, and what in their time shaped them?',
    find=('theoretical and conceptual ideas and principles driving the development of the subject, as well as key thinkers, with a '
          'critical awareness of the specific historical contexts in which they emerged.'))
k33(9, 'B', [], 'framework and financing of policy processes',
    'how policy making and implementation are framed, run and funded, with many stakeholders at several levels of government',
    'Who was involved in making and funding this policy, and at which level of government?')
k33(10, 'B', [], 'subnational and supranational policy; international organisations',
    'policy above and below the nation state and how international organisations frame problems and solutions',
    'How has an international organisation shaped how this problem is defined or solved?')
k33(11, 'B', ['interact'], 'non-state welfare and mixed economies',
    'non-state welfare from informal, voluntary and private sources and how these mix with the state',
    'What part do families, charities or firms play in welfare in your topic?')
k33(12, 'B', ['recognising', 'navigate', 'embed'], 'social administration and the running of institutions',
    'social administration: how welfare institutions are led, managed and run day to day, with reflective and interpersonal skills',
    'What would it take to manage a welfare service well, and what skills would you need?')
k33(13, 'B', [], 'digital technology in policy',
    'digital technology in designing, delivering and administering policy',
    'How has digital technology changed how a service in your area is delivered?')
k33(14, 'B', ['influencing'], 'public attitudes, misinformation and advocacy',
    'public attitudes to welfare, the effect of information and misinformation, and how lobbying, campaigns and advocacy shape policy',
    'How did public opinion or a campaign shape a policy you have studied?',
    find=('public perceptions and attitudes towards social policy and welfare, including the role of information, disinformation and '
          'misinformation and the roles of lobbying, campaigning and advocacy in influencing policy making.'))
k33(15, 'C', ['impacts'], 'how policy improves or fails welfare',
    'how policy affects the welfare of people and groups, both improving conditions and failing to reduce inequality',
    'Where has a policy improved lives, and where has it left inequality untouched?')
k33(16, 'C', [], 'ambivalent effects: control and conditionality',
    'the mixed effects of policy, including control and discipline through conditionality or the reproduction of inequality',
    'Does welfare conditionality in your area support people, discipline them, or both?')
k33(17, 'C', [], 'ways of delivering welfare; eligibility debates',
    'ways of delivering welfare: universal or targeted, conditional or not, means-tested, and debates on eligibility, deservingness, leakage and coverage',
    'Should the benefit you are studying be universal or targeted, and why?')
k33(18, 'C', ['affected'], 'policy and intersecting disadvantage',
    'how policy meets communities, families and people facing intersecting disadvantage of class, ethnicity, gender identity, sex, disability, religion or sexual orientation',
    'Who faces more than one disadvantage under this policy, and how does that change its effect?')
k33(19, 'C', [], 'new technology, generative AI and automation',
    'what new technology, generative AI and automation among them, means for work, education, health, care and welfare administration',
    'How might automation change the area of welfare you study?')
k33(20, 'C', ['shape', 'recognising'], 'policy and environmental debate',
    'how policy and environmental debate shape each other, including climate inequality, resource distribution and long-term wellbeing',
    'How has environmental debate changed a policy you know, or been changed by it?')
k33(21, 'C', ['collect', 'analyse'], 'welfare data sources and research methods',
    'major data sources on welfare and the main quantitative and qualitative research methods',
    'Which data source would you use to measure the problem you study, and what would it miss?',
    find=('significant sources of data about social welfare, and the main quantitative and qualitative social research approaches '
          'and methods used to collect and analyse data.'))
k33(22, 'D', [], 'core concepts of welfare',
    'core concepts: need, wellbeing, welfare, poverty, inequality, exclusion, citizenship, rights, equity, justice, sustainability, difference and intersectionality',
    'How would you define poverty, and how does your definition change the policy you would back?')
k33(23, 'D', [], 'theories and ideologies of welfare',
    'theories, philosophies and ideological debates about welfare and the roles of state, market and other actors',
    'What should the state do for welfare, and what should be left to markets, families or charities?')
k33(24, 'D', [], 'theories of the state and comparison',
    'theories of the state and policy making, and comparative theory and method',
    'Which theory of the state best explains the policy you are studying?')
k33(25, 'D', ['coalescing'], 'interdisciplinary approaches',
    "interdisciplinary approaches, with the social sciences meeting around policy's applied focus",
    'What does another social science add to your view of this problem?')
k33(26, 'D', ['related'], 'political economy of welfare',
    'the political economy of welfare and how values link to political and economic interests',
    'Whose economic interests does this policy serve, and which values justify it?',
    find='the political economy of welfare and how values and principles are related to political and economic interests.')
k33(27, 'E', [], 'ontology and epistemology of research',
    'the ontology and epistemology beneath research designs',
    'What do you assume about what can be known when you choose a research design?')
k33(28, 'E', ['identifying'], 'framing research problems',
    'how to identify researchable problems about welfare',
    'What question about welfare could you actually research, and how would you narrow it?')
k33(29, 'E', [], 'research design principles',
    'the principles of quantitative, qualitative and mixed-method research design',
    'Why might your question need numbers, interviews or both?')
k33(30, 'E', [], 'choosing techniques for data',
    'how to choose techniques for collecting, managing, interpreting and analysing data, secondary data included',
    'Which existing data set could answer part of your question?')
k33(31, 'E', [], 'policy evaluation and analysis',
    'approaches to policy evaluation and analysis',
    'How would you tell whether this policy has worked?')
k33(32, 'E', ['informing'], 'evidence-based policy and research',
    'debates on evidence-based policy and how social science research informs policy making',
    'When does research actually change policy, and when is it ignored?')
k33(33, 'E', [], 'research ethics',
    'research ethics in the social sciences',
    'What ethical risks would your research raise, and how would you handle them?',
    find='ethics of social science research.')


# ================================================================== 4.5 honours outcomes in line with the Frameworks (expected to; describes)
def aaw_45(about, fw):
    return ("Present this as an outcome the statement expects of every Social Policy honours graduate at FHEQ Level 6 (FQHEIS Level 10), "
            "set out in line with the Frameworks: %s. Cite it as %s. It is not one of the rungs and the issuer's word is 'expected', so "
            "state it without must or will, and do not call it a regulatory requirement. Set it beside the matching honours descriptor "
            "%s, the 4.7 to 4.10 tables and spine:6." % (about, CITE % '4.5', fw))


def aad_45(when, ask):
    return ("Raise this when %s. With a student, say in plain second-person words what you are expected to have built by graduation; "
            "with staff, frame it as the shape of the whole honours award. Ask: \"%s\" Avoid reading the list aloud or treating it as "
            "graded by class." % (when, ask))


def k45(b, verbs, dom, about, para, prac, ben, when, ask, fw, th=None):
    s('4.5.b%d' % b, type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='honours graduates', addressee='learner',
      verbs=verbs, about=about, domain=dom, award=HON, para=para, prac=prac, ben=ben, aaw=aaw_45(about, fw), aad=aad_45(when, ask))


k45(1, ['developed'], 'understanding', 'grasp of a complex body of knowledge',
    'In line with the Frameworks, honours graduates are expected to grasp a complex and substantial body of knowledge.',
    'Build the course so that by the end graduates have a grasp of a complex, substantial body of knowledge in the subject.',
    'By graduation you are expected to have a grasp of a complex and substantial body of knowledge.',
    'a student asks what an honours degree adds up to', 'How would you sum up what you now know that you did not know in your first year?',
    'qaa/fheq-2024/4.15.b1')
k45(2, ['developed', 'applied'], 'generic-skill', 'analytical and problem-solving skills for work',
    'Honours graduates are expected to have gained analytical and problem-solving skills they can use in many kinds of work.',
    'Make sure analytical and problem-solving skills are taught and practised in ways students can carry into many kinds of job.',
    'By graduation you are expected to have analytical and problem-solving skills you can use in many kinds of work.',
    'a student asks how the degree helps them get work', 'Which problem-solving skill from your degree would you describe to an employer, and with what example?',
    'qaa/fheq-2024/4.15.b9.2')
k45(3, ['developed', 'working'], 'generic-skill', 'co-creative, sustainable and responsible working',
    'Honours graduates are expected to have learned, through experience, to work with others in ways that are co-creative, sustainable and socially responsible.',
    'Give students experience of working with others co-creatively, sustainably and responsibly, and help them name what they learned.',
    'By graduation you are expected to have learned, through experience, to work with others in co-creative, sustainable and socially responsible ways.',
    'group projects, partnerships or volunteering come up', 'When have you worked with others to create something, and how did you keep it fair and sustainable?',
    'qaa/fheq-2024/4.15.b9.1')
k45(4, ['analyse', 'reach', 'communicate'], 'generic-skill', 'weighing evidence, judging soundly and communicating',
    'Honours graduates are expected to be able to weigh evidence, arguments and assumptions, reach sound conclusions and communicate them well.',
    'Assess, across the course, how well students weigh evidence and assumptions, reach sound conclusions and communicate them.',
    'By graduation you are expected to be able to weigh evidence, arguments and assumptions, reach sound conclusions and explain them well.',
    'a student is writing an argument or policy recommendation', 'What assumption in your argument would a sceptical reader challenge first?',
    'qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/4.15.b8')


# ================================================================== master's lists 4.12 to 4.15 (expected to; describes)
MWHEN = {
    '4.12': "a master's student plans their specialism or a team designs the core of a master's course",
    '4.13': "a master's student is analysing policy or a team designs master's modules",
    '4.14': "a master's student is planning research or a dissertation",
    '4.15': "a master's student reflects on skills for work and further learning",
}


def km(n, b, dom, find, verbs, about, x, ask, fw, after=None):
    k = dict(find=find, type='threshold', rung='threshold', force='describes', level='fheq:7', appliesTo="master's graduates",
             addressee='learner', verbs=verbs, about=about, domain=dom, award=MAS,
             para="Master's graduates are expected to show %s." % x,
             prac="Design the master's course so that graduates can show %s." % x,
             ben="By the end of your master's, you are expected to show %s." % you(x),
             aaw=("Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): %s; the "
                  "issuer's word is 'expected', so state it without must or will. Cite it as %s. Do not apply it to the honours degree, "
                  "call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it "
                  "beside %s and spine:7." % (about, CITE % n, fw)),
             aad=("Raise this when %s. With a master's student, ask in plain second-person words how far they can already show it; with "
                  "staff, frame it as what the master's course is expected to develop. Ask: \"%s\" Avoid treating the list as a checklist, "
                  "which 4.11 says it is not, or reading it aloud." % (MWHEN[n], ask)))
    if after:
        k['after'] = after
    s('%s.b%d.masters' % (n, b), **k)


km('4.12', 1, 'knowledge',
   ('a sound understanding of the broader social policy landscape, alongside in-depth knowledge of at least one major area of Social '
    'Policy, such as, but not limited to, employment, housing, eco-social policies, health, family, pensions, tax, social security, '
    'education, social care, gender and social policy, and international and global policies'),
   [], 'breadth across the field with depth in one area',
   'a sound grasp of the wider policy field with deep knowledge of at least one major area, such as housing, health, pensions, social security or global policy',
   'Which area of policy is your specialism, and how does it fit the wider field?', 'qaa/fheq-2024/4.17.b1')
km('4.12', 2, 'understanding',
   ('a thorough and comprehensive understanding of human needs, social justice, and individual and collective wellbeing in contemporary '
    'societies and their relationship to Social Policy analysis'),
   [], 'need, justice and wellbeing in policy analysis',
   'a thorough, full understanding of human need, social justice and personal and shared wellbeing today, and how they relate to policy analysis',
   'How does your view of social justice shape the policy analysis you do?', 'qaa/fheq-2024/4.17.b1')
km('4.12', 3, 'understanding',
   'the capacity to navigate and apply core concepts and theoretical frameworks in Social Policy to critically evaluate research and scholarships',
   ['navigate', 'apply', 'evaluate'], 'core theory used to judge research',
   "the capacity to work with and apply the subject's core concepts and theories to judge research and scholarship critically",
   'Which theory do you use to judge the studies you read, and why that one?', 'qaa/fheq-2024/4.17.b4.1')
km('4.12', 4, 'understanding',
   ('a sound understanding of a specific dimension or manifestation of social injustices, how they are reproduced, sustained and '
    'addressed, including their particular policy context'),
   ['reproduced', 'sustained', 'addressed'], 'one form of social injustice in depth',
   'a sound understanding of one particular form of social injustice, how it is reproduced, kept in place and tackled, and its policy setting',
   'Which injustice have you studied in depth, and what keeps it in place?', 'qaa/fheq-2024/4.17.b1')
km('4.12', 5, 'understanding',
   ('the ability to recognise and demonstrate the relevance of norms, values and worldviews in defining social injustices, shaping '
    'policy processes and informing policy solutions'),
   ['recognise', 'demonstrate', 'defining', 'shaping', 'informing'], 'norms and worldviews in injustice and policy',
   'the ability to recognise and make plain how norms, values and worldviews define injustice, shape policy processes and inform solutions',
   'Whose worldview defines the problem in the policy you are studying?', 'qaa/fheq-2024/4.17.b4.2')
km('4.12', 6, 'subject-skill',
   ('awareness and appreciation of alternative research methods and the ability to design and undertake an independent dissertation '
    'or research project with appropriate supervision'),
   ['design', 'undertake'], 'research methods and a supervised dissertation',
   'knowledge of a range of research methods and the ability to design and carry out an independent, supervised dissertation or project',
   'Which methods did you consider for your dissertation before choosing one?', 'qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b6')
km('4.13', 1, 'subject-skill',
   ('in-depth understanding of social policy making, practice and impact, including understanding policy in relevant local, national '
    'and international contexts, and significant social and economic differences among jurisdictions, and variations in welfare histories.'),
   [], 'policy making and impact across jurisdictions',
   'deep understanding of how policy is made, practised and felt, at local, national and international scale, across differing jurisdictions and welfare histories',
   'How would this policy play out differently in another jurisdiction with a different welfare history?', 'qaa/fheq-2024/4.17.b1')
km('4.13', 2, 'subject-skill',
   ('awareness of and ability to undertake comparative analyses of differences in political regime types, policy-making styles and '
    'substantive policies'),
   ['undertake'], 'comparative analysis of regimes and policies',
   'the ability to carry out comparative analysis of regime types, policy-making styles and actual policies',
   'Which two regimes would you compare for your topic, and on what basis?', 'qaa/fheq-2024/4.17.b2')
km('4.13', 3, 'subject-skill',
   ('identify and understand the roles, responsibilities and perspectives of key stakeholders in the social policy landscape – including '
    'service users, providers, practitioners,\n\n27\npolicymakers and professionals – and the openness of policy-making structures to '
    'democratic participation and co-production'),
   ['identify', 'understand'], 'stakeholders and democratic participation',
   'the ability to identify and understand what key stakeholders, from service users to policymakers, do and think, and how open policy making is to democratic participation and co-production',
   'Who has a say in this policy, and who is left out?', 'qaa/fheq-2024/4.17.b5')
km('4.13', 4, 'subject-skill',
   ('a critical understanding of how social policy making, development and implementation impact upon and are experienced by service '
    'users, benefit claimants and the broader public'),
   ['impact', 'experienced'], 'how policy is felt by users and the public',
   'critical understanding of how making and delivering policy affects, and is lived by, service users, claimants and the public',
   'How do claimants experience the policy you are studying, and what evidence shows it?', 'qaa/fheq-2024/4.17.b1')
km('4.13', 5, 'subject-skill',
   'a critical understanding and application of equality issues and their intersections to the analysis of social policies',
   [], 'intersecting equality issues in analysis',
   'critical understanding of equality issues and how they intersect, applied to policy analysis',
   'Which intersecting inequalities matter most in your topic?', 'qaa/fheq-2024/4.17.b3')
km('4.13', 6, 'subject-skill',
   ('a critical and reflective understanding of the importance of diversity, equity, inclusion, decolonisation, equality issues and '
    'environmental sustainability across all stages of social policy research and practice, in local, national and global contexts, '
    'and how these operate in different cultures and countries'),
   ['operate'], 'EDI, decolonisation and sustainability in research and practice',
   'critical, reflective understanding of why diversity, equity, inclusion, decolonisation, equality and environmental sustainability matter at every stage of research and practice, locally to globally and across cultures',
   'How have equity and sustainability shaped the design of your own research?', 'qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b8.2')
km('4.13', 7, 'subject-skill',
   ('critical and constructive engagement with topical discussions on social injustices and social policy reform nationally and '
    'internationally'),
   [], 'engaging with current reform debates',
   'critical, constructive engagement with current debates on injustice and policy reform at home and abroad',
   'Which current reform debate have you taken part in, and what did you add?', 'qaa/fheq-2024/4.17.b4.1')
km('4.13', 8, 'subject-skill',
   'critical analysis of how related disciplines contribute to Social Policy analyses.',
   [], 'what neighbouring disciplines contribute',
   'critical analysis of what neighbouring disciplines bring to policy analysis',
   'What does economics or sociology add to your analysis that the subject alone would miss?', 'qaa/fheq-2024/4.17.b3')
km('4.14', 1, 'generic-skill', 'capacity to assess and apply quantitative, qualitative or mixed methods research',
   ['assess', 'apply'], 'judging and using research of every kind',
   'the capacity to judge and use quantitative, qualitative or mixed-methods research',
   'Which kind of evidence, numbers or interviews, do you find harder to judge?', 'qaa/fheq-2024/4.17.b2')
km('4.14', 2, 'generic-skill', 'a developed ability to collect data using appropriate quantitative, qualitative or mixed method approaches',
   ['collect', 'using'], 'collecting data by fitting methods',
   'a developed ability to gather data with fitting quantitative, qualitative or mixed approaches',
   'How did you decide how to collect your data?', 'qaa/fheq-2024/4.17.b2')
km('4.14', 3, 'generic-skill', 'understanding and application of the principles of ethical research practice',
   [], 'ethical research practice',
   'understanding and use of the principles of ethical research',
   'What ethical risks does your research carry, and how have you dealt with them?', 'qaa/fheq-2024/4.17.b5')
km('4.14', 4, 'generic-skill',
   ('awareness and appreciation of alternative research methods and the ability to design and undertake an independent dissertation '
    'or research project with appropriate supervision'),
   ['design', 'undertake'], 'research methods and a supervised dissertation (repeated from 4.12)',
   'knowledge of different research methods and the ability to design and carry out an independent, supervised dissertation or project',
   'Which research method would you defend as best for your question, and why?', 'qaa/fheq-2024/4.17.b6',
   after='4.14 Students graduating')
km('4.14', 5, 'generic-skill', 'reflexive capacity to evaluate feedback to improve writing and enhance the quality of argument and analysis',
   ['evaluate', 'improve', 'enhance'], 'using feedback to improve',
   'the reflexive capacity to weigh feedback and use it to improve writing, argument and analysis',
   'What did your last feedback change in how you write?', 'qaa/fheq-2024/4.17.b8.3')
km('4.14', 6, 'generic-skill', 'expertise in scholarly practice, including locating relevant information sources and academic referencing.',
   ['locating'], 'expert scholarly practice',
   'expert scholarly practice, from finding relevant sources to academic referencing',
   'How do you find the most relevant sources for a new topic?', 'qaa/fheq-2024/4.17.b7')
km('4.15', 1, 'generic-skill', 'critical, reflexive and independent approaches to learning',
   [], 'critical, reflexive, independent learning',
   'critical, reflexive and independent ways of learning',
   'How do you direct your own learning now?', 'qaa/fheq-2024/4.17.b8.3')
km('4.15', 2, 'generic-skill',
   'critical evaluation of, and commitment to, creating social value and public service contributing to social wellbeing',
   ['creating', 'contributing'], 'commitment to social value and public service',
   'commitment to public service and to adding social value for wellbeing, with a critical eye on both',
   'What kind of public value do you want your work to create?', 'qaa/fheq-2024/4.17.b8.1')
km('4.15', 3, 'generic-skill',
   'critically reflective identification of learning needs, to enhance professional practice and personal development',
   ['enhance'], 'naming learning needs for growth',
   'critically reflective awareness of what they still need to learn, for professional and personal growth',
   'What do you still need to learn for the work you want to do?', 'qaa/fheq-2024/4.17.b8.3')
km('4.15', 4, 'generic-skill',
   ('evaluation and application of practices of engaging productively and contributing effectively in collaborative, multicultural, '
    'and diverse environments domestically and globally'),
   ['engaging', 'contributing'], 'working well in diverse, multicultural settings',
   'the ability to evaluate and use ways of working productively in collaborative, multicultural and diverse settings at home and abroad',
   'How have you worked across cultures or in a diverse team?', 'qaa/fheq-2024/4.17.b8.2')
km('4.15', 5, 'generic-skill',
   ('awareness of and familiarity with evolving technologies, including generative artificial intelligence tools, their strengths and '
    'limitations, and the ethical implications of their use in research and writing.'),
   [], 'emerging technology and generative AI, ethically',
   'familiarity with emerging technologies, generative AI among them, their strengths, limits and ethical questions in research and writing',
   'Where would you not use generative AI in your research, and why?', 'qaa/fheq-2024/4.17.b5')


# ================================================================== statements from prose (sections 1 to 4)
def aaw_learn(n, force, about, beside, award_note="the honours degree at FHEQ Level 6 (FQHEIS Level 10)"):
    return ("Present this as an expectation of Social Policy students, in %s, for %s: %s. Cite it as %s. Do not call it a regulatory "
            "requirement or a rung of the section 4 standards. Set it beside %s and spine:6." % (force, award_note, about, CITE % n, beside))


def aad_learn(when, ask):
    return ("Raise this when %s. With a student, put it in plain second-person words; with staff, frame it as something the course "
            "should help students reach. Ask: \"%s\" Avoid reading the paragraph aloud or treating it as a graded standard." % (when, ask))


def aaw_prov(n, force, who, about, beside):
    return ("Treat this as a duty, in %s, on %s, not a learner outcome: %s. It holds for Social Policy courses at the levels the "
            "statement covers, not for one level. Cite it as %s. Do not present it as a regulatory requirement or turn it into a task "
            "for the student; set it beside %s." % (force, who, about, CITE % n, beside))


def aad_prov(when, ask):
    return ("Raise this when %s. With the programme team, frame it as practice they plan for and ask \"%s\" Do not put it to a "
            "student as their own duty; a student may only be told what the course should offer them." % (when, ask))


def learner(i, force, verbs, dom, about, para, prac, ben, beside, when, ask, find=None, ty='expectation', n=None):
    k = dict(type=ty, rung='none', force=force, level='fheq:6', appliesTo='Social Policy students', addressee='learner',
             verbs=verbs, about=about, domain=dom, award=HON, para=para, prac=prac, ben=ben,
             aaw=aaw_learn(n or i, force, about, beside), aad=aad_learn(when, ask))
    if find:
        k['find'] = find
    s(i, **k)


def provider(i, force, verbs, about, para, prac, why, who, beside, when, ask, find=None, ty='expectation', n=None):
    k = dict(type=ty, rung='none', force=force, level='none', appliesTo=who, addressee='provider', verbs=verbs, about=about,
             domain='none', award=HON, para=para, prac=prac, ben=('n/a', why),
             aaw=aaw_prov(n or i, force, who, about, beside), aad=aad_prov(when, ask))
    if find:
        k['find'] = find
    s(i, **k)


learner('1.7', 'should', ['understand', 'operates', 'emphasising', 'addressing'], 'understanding', 'policy across levels; subsidiarity',
        'Students should understand how social policy works at local, national and international levels, subsidiarity included: meeting needs at the closest level able to do so.',
        'Teach how social policy works at local, national and international scale, with the principle of subsidiarity, so that students should understand it.',
        'You should understand how social policy works locally, nationally and internationally, including subsidiarity: dealing with needs at the nearest level that can handle them.',
        '1.12, 3.2, 4.7.b2 and qaa/fheq-2024/4.15.b1', 'devolution, local government or international policy come up',
        'Which level of government is best placed to meet the need you are studying, and why?',
        find=('Students should understand how social policy operates across local, national and international levels, including the '
              'principle of subsidiarity, emphasising the importance of addressing social needs at the most immediate level capable of doing so.'))
provider('1.14', 'must', ['recognise', 'shaping'], 'environmental sustainability central to welfare',
         ('The subject must treat environmental sustainability as central to welfare systems and future policy; human-centred views '
          'that ignore ecological limits risk widening inequality, and teaching the tie between wellbeing and planetary health lets '
          'graduates engage critically with climate, energy and resource policy.'),
         ('Build the link between human wellbeing and planetary health into the curriculum: the subject must recognise sustainability '
          'as central to welfare, so that graduates can engage critically with climate, energy and resource policy.'),
         'a requirement on the discipline and its curricula; the student meets it in what is taught',
         'the discipline and those who design its curricula', '1.44 to 1.53, 3.3.b7, 3.3.b20 and std:doc:qaa-advancehe-esd-2021-guidance',
         'a team reviews how sustainability runs through the curriculum',
         'Where does the course connect welfare to ecological limits, beyond a single module?', ty='requirement')
learner('1.17', 'must', ['develop'], 'understanding', 'policy design, implementation, evaluation and theory',
        'Students must come to appreciate how social policies are designed, put into practice and evaluated, and wider theories of how policy is made.',
        'Students must develop an appreciation of how policies are designed, delivered and evaluated, and of policy-making theory; give every route room for it.',
        'You must come to appreciate how social policies are designed, carried out and evaluated, and the wider theories of how policy gets made.',
        '2.2.b5, 3.3.b9, 4.7.b3 and qaa/fheq-2024/4.15.b1', 'a student asks why policy-making theory matters',
        'Could you trace one policy from its design through to how it was evaluated?',
        find=('Consequently, Social Policy students must develop an appreciation of the design, implementation and evaluation of social '
              'policies and broader theories of policy making.'), ty='requirement')
learner('1.20', 'should', ['acknowledge', 'inform'], 'generic-skill', "own and others' values, with research",
        "Because the subject is normative, students should recognise their own values, other people's values and research findings, and let these inform how they understand the subject.",
        "Give students room to name their own values, hear others' and set both against research, as they should in a normative subject.",
        "Because your subject is about values as well as facts, you should recognise your own values, respect other people's and use research to shape your understanding.",
        '1.38, 1.39, 4.8.b3 and qaa/fheq-2024/4.15.b4', "values or politics come up in class or a student's position is challenged",
        'Which of your own values shapes how you see this issue, and what does the research say?')
learner('1.24', 'must', ['consider', 'applied'], 'understanding', 'colonial legacies in analysis',
        ('Analysis in the subject must look beyond history to the legacies and practices that continue; decolonial frameworks should '
         'also be used when analysing internationalised policy, since international funding often rests on colonial ideas and interests.'),
        ('Teach analysis that must take in continuing colonial legacies, and use decolonial frameworks when examining international '
         'policy and the conditions attached to its funding.'),
        ('Your analysis must look at colonial legacies that continue today, not only at history, and you should use decolonial '
         'frameworks when you examine international policy and who funds it.'),
        '1.21 to 1.27, 2.5, 3.3.b2 and qaa/fheq-2024/4.15.b7', 'decolonisation, empire or international aid come up',
        'Whose ideas and interests shaped this international policy, and does their legacy still show?', ty='requirement')
P['1.24']['addressee'] = 'both'
provider('1.27', 'should', ['diversify', 'challenge'], 'teaching that challenges colonial assumptions',
         'Teaching should work to widen student learning with theories, knowledge and analyses that challenge the colonial and neocolonial assumptions long built into the discipline.',
         'Widen reading lists and analyses so that teaching challenges the colonial and neocolonial assumptions in the subject, as it should.',
         'a duty on those who teach the subject', 'those who teach the subject', '1.21 to 1.26, 4.13.b6.masters and theme:edi',
         'a team reviews reading lists or decolonises the curriculum',
         'Which theories on this module come from outside the Global North, and which assumptions do they challenge?',
         find=('Teaching within the discipline should make efforts to diversify student learning through wider theories, knowledge and '
               'analyses which challenge the legacy of colonial and neocolonial assumptions and thinking often embedded within the discipline.'))
provider('1.29', 'should', ['supporting'], 'support for students new to the subject',
         'Since few students meet the subject before university, teaching should support those who have not studied it formally but know its issues from life, the media and public debate.',
         'Plan early teaching for students new to the subject, drawing on what they know from lived experience, the media and public debate.',
         'a duty on teaching staff', 'teaching staff', '1.30, 1.31 and 3.9', 'a team plans first-year teaching or induction',
         'How does first-year teaching build on what students already know from life and the news?',
         find=('Teaching of Social Policy should therefore be mindful of supporting students who may not have formally studied Social Policy '
               'but will have engaged with relevant key issues through lived experience and media coverage and public debates over social issues.'))
provider('1.31', 'should', ['reflect', 'ensure'], 'design for diverse needs; awarding gaps',
         ("Programme, teaching and learning design should take account of students' varied needs; provision should make sure support is "
          "in place and act on awarding gaps, starting from protected characteristics and widening to other groups, aware that students "
          "hold several identities at once."),
         ('Review awarding gaps by protected characteristic and beyond, socio-economic status included, and set support so every group '
          'can engage; this should shape programme and teaching design.'),
         'a duty on those who design and run courses', 'those who design programmes and provision',
         '1.30, 1.32, 3.13.b6 and the Equality Act 2010 the statement cites', 'a team examines awarding gaps or support',
         'Which groups of students are awarded fewer good degrees on this course, and what support is aimed at them?')
provider('1.36', 'should', ['adhere'], 'good EDI practice in design',
         "Programme, teaching and assessment design should follow good practice on equity, diversity and inclusion, such as QAA's advice on inclusive subject communities.",
         "Check programme, teaching and assessment design against recognised EDI guidance, such as QAA's inclusive subject communities advice.",
         'a duty on those who design programmes, teaching and assessment', 'those who design programmes, teaching and assessment',
         "1.35 (the statement's definitions of equity, diversity and inclusion), 1.31 and 3.13", 'a team designs or revalidates a programme',
         'Which EDI guidance did you check this design against, and what changed?')
learner('1.39', 'will', ['reflect', 'understand', 'demonstrate'], 'generic-skill', 'inclusive, reflexive practice',
        ('Graduates will be able to reflect on how inclusive their work is and how their own experience and identity shape their views; '
         'as leaders they understand the value of diversity in teams and how their background affects their decisions, and show equity '
         'and inclusion in working with others.'),
        ('Build reflection on inclusion and positionality into the course so that graduates will be able to examine how their identity '
         'shapes their work and lead diverse teams fairly.'),
        ('You will be able to reflect on how inclusive your work is and how your own background and identity shape your views, and to '
         'work and lead with others fairly and inclusively.'),
        '1.38, 1.20, 4.10.b3 and qaa/fheq-2024/4.15.b9.1', 'a student reflects on placement, group work or their own position',
        'How might your own background have shaped the way you approached this piece of work?', ty='outcome')

ACC = ('the provider', '1.40, 1.43, 3.13 and the Equality Act 2010 duties named in 1.40',
       'a team designs teaching and assessment or a disabled student asks about support')
provider('1.42.b1', 'should', ['integrate', 'engage'], 'varied teaching and assessment modes',
         'Programme design should combine varied teaching modes and assessment types so students engage through many approaches.',
         'Mix teaching modes and assessment types across the programme so that every student finds ways in.',
         'a duty on the provider for accessible teaching', *ACC, 'How many different assessment types does a student meet across the programme?')
provider('1.42.b2', 'should', ['given'], 'clear early information on expectations and support',
         'Students should get clear information from the outset about what is expected and what support exists.',
         'Tell students at the start, clearly, what is expected of them and what support they can use.',
         'a duty on the provider to inform students', *ACC, 'What do students learn in week one about expectations and support?')
provider('1.42.b3', 'should', ['given', 'support'], 'resources and assistive technology for disabled students',
         'Disabled students should have full access to adequate learning resources, assistive technology included, to support their learning.',
         'Make sure disabled students can fully use suitable learning resources and assistive technology for their own learning.',
         'a duty on the provider for accessible resources', *ACC, 'Which assistive technologies can disabled students use with your learning resources?')
provider('1.42.b4', 'should', ['enabling', 'access', 'obtain', 'create'], 'reasonable adjustment in assessment',
         ('Reasonable adjustment in assessment should be available through clearly communicated routes, so students can take '
          'alternative assessments or get extra support for fair opportunities.'),
         "Publish clear routes to reasonable adjustment, alternative assessment and extra support, in line with students' support plans.",
         'a duty on the provider in assessment', *ACC, 'How does a student find out how to request an adjustment to an assessment?',
         find=('For assessments, reasonable adjustment is available to students through clearly communicated channels, enabling students '
               'to access alternative assessments and/or\n\n8\nobtain additional support to create equitable learning opportunities for all.'))
provider('1.43', 'should', ['provided', 'face', 'offered'], 'placement support for disabled students',
         'Where placements are part of the curriculum, disabled students who face barriers to them should get extra support, with other work-based learning offered if needed.',
         'Plan support for disabled students on placements and an alternative form of work-based learning for anyone the placement would exclude.',
         'a duty on the provider where placements are in the curriculum', 'the provider, where placements are in the curriculum',
         '1.42, 1.57 and 3.4', 'a team plans placements', 'What would a disabled student who cannot take this placement do instead?')
provider('1.48', 'should', ['explore', 'shaping'], 'welfare, economy and the environment',
         ('Students should have the chance to explore how welfare provision, with labour markets and the economy, shapes what human '
          'action does to the natural environment, including how welfare may need reform for climate, demographic and technological change.'),
         'Give students room to explore the link between welfare, work, the economy and the environment, and how welfare may need to change for future pressures.',
         'a duty on the course to offer the opportunity', 'the course',
         '1.44 to 1.47, 3.3.b7, 4.7.b4 and std:doc:qaa-advancehe-esd-2021-guidance', 'a team plans sustainability content',
         'Where in the course do students examine how welfare policy affects the environment?')
provider('1.50', 'should', ['given'], 'the Inner Development Goals',
         'Attention should also go to the Inner Development Goals, to help identify, build and communicate the personal skills and qualities that sustainable development needs.',
         'Draw on the Inner Development Goals in planning, so that personal skills for sustainable development are named and built.',
         'a duty on those who design programmes', 'those who design programmes',
         '1.49, 1.51 and std:doc:qaa-advancehe-esd-2021-guidance (the guidance 1.50 also names)', 'a team plans sustainability skills',
         'Which personal skills for sustainable development does the course name and develop?',
         find=('Additionally, attention should be given to the Inner Development Goals: to better identify, understand, develop, integrate '
               'and communicate the personal skills and attributes needed for sustainable development.'))
provider('1.52', 'should', ['investigate', 'debate', 'critique', 'given', 'empower', 'support'], 'critique of sustainability; climate and privilege',
         ('The subject can let students investigate, debate and critique sustainability and its politics; within this, attention should '
          'be given to how climate change deepens privilege by race, gender, wealth and ability, locally to globally, and what it means for welfare services.'),
         'In sustainability teaching, cover how climate change deepens privilege of several kinds and what it means for welfare services.',
         'a duty on those who teach sustainability', 'those who teach sustainability', '1.14, 3.3.b20, 4.13.b6.masters and theme:edi',
         'a team designs teaching on climate and inequality', 'Where do students examine who gains and who loses from climate change?')
learner('1.53', 'should', ['considered', 'graduate', 'engage'], 'generic-skill', 'skills for lifelong policy debate',
        ('Sustainability also bears on learning after the degree: since policy contexts keep changing, students should graduate with '
         'broad skills to join shifting policy debates with critical and analytical thinking.'),
        'Prepare students for learning after the degree: they should leave with broad critical and analytical skills to keep up with changing policy debates.',
        'You should leave your degree with a broad set of critical and analytical skills that let you keep joining policy debates as they change.',
        '1.51, 4.10.b2 and qaa/fheq-2024/4.15.b9.3', 'a student asks how the degree prepares them for later learning or work',
        'How will you keep up with policy debates once you graduate?')
provider('1.56', 'should', ['encourage', 'apply'], 'applying knowledge to work contexts',
         'Opportunities should also encourage students to use what they know of the subject in work settings, through placements, authentic assessment or similar.',
         'Design placements, authentic assessments or similar tasks where students apply the subject to real work settings.',
         'a duty on those who design programmes', 'those who design programmes',
         '1.54 to 1.58, 3.11 and std:doc:qaa-enterprise-2018-guidance', 'a team plans employability or authentic assessment',
         'Which tasks ask students to use the subject in a real or realistic work setting?',
         find=('Opportunities should also encourage students to apply disciplinary knowledge to employment contexts (whether through '
               'placements, authentic assessments or other relevant practices).'))
provider('1.60', 'should', ['provided', 'engage', 'develop'], 'critical engagement with generative AI',
         ("Given generative AI's growing place in work and study, students should be given chances to engage critically with it and "
          "learn to use it ethically, effectively and reflectively at work and, where allowed, in study."),
         'Build in chances for students to use and question generative AI tools, ethically and reflectively, within what your institution allows.',
         'a duty on the course to provide the opportunity', 'the course', '1.61 to 1.66, 3.12, 4.10.b4 and 4.15.b5.masters',
         'a team decides how generative AI enters teaching', 'Where do students get to try generative AI critically, and under what rules?')
provider('1.62.b5', 'should', ['informed', 'encouraged', 'participate'], 'debate on the consequences of generative AI',
         'Students should be told about, and encouraged to join, debate on the ethical, legal, environmental and social effects of generative AI and on policy responses to them.',
         'Bring the ethical, legal, environmental and social effects of generative AI, and policy responses, into class debate.',
         'a duty on the course to inform and involve students', 'the course', '1.60, 1.65 and 3.3.b19',
         'a team plans teaching on AI and society', 'Where do students debate the social and environmental costs of generative AI?')
provider('1.65', 'should', ['adhere', 'taught'], 'institutional AI policy; teaching on risks',
         ("Each institution will have its own generative AI policy that programmes have to follow; within it, students should be taught "
          "the risks, limits and environmental costs of using generative AI."),
         "Within your institution's AI policy, teach students the risks, limits and environmental costs of generative AI use.",
         'a duty on the course to teach the risks', "the course, within its institution's policy", '1.60 to 1.64 and 3.12',
         "a team aligns teaching with the institution's AI policy", 'What do students learn here about the risks and environmental cost of generative AI?')

learner('2.1', 'should', ['designed', 'address'], 'subject-skill', 'the core questions for any social problem',
        'Degrees should be designed so students can put core questions to any social problem: what policy does, how, why, whether it should, to whom and by whom.',
        'Design the course so students can ask of any social problem what policy does, how and why, whether it should, and who acts and who is affected.',
        'Your course should equip you to ask of any social problem what policy does, how and why it does it, whether it should, who it affects and who carries it out.',
        '2.2, 2.3, 4.8.b1 and qaa/fheq-2024/4.15.b7', 'a student asks how to approach a social problem, or a team frames course aims',
        'Take a social problem you care about: what is done, how, why, should it be, to whom and by whom?',
        find=('Degrees in Social Policy should be designed so that students are able to address four fundamental questions in relation to '
              'any social problem: what is done by social policies, how is it done, why has this been done, and whether it should be done, '
              'who it is done to and who is it done by?'))
P['2.1']['addressee'] = 'both'

D22 = ('a design duty on the programme', 'programme designers', '2.1, 2.3, 3.3 and qaa/fheq-2024/4.15.b1',
       'a team designs or reviews a Social Policy programme')
provider('2.2.b1', 'should', [], 'welfare, welfare systems and entitlement',
         'Programme design should focus clearly on the concept of welfare, welfare systems and who is entitled to support.',
         'Give the concept of welfare, welfare systems and entitlement a clear place in the programme.',
         *D22, 'Where does the programme teach the concept of welfare and entitlement directly?')
provider('2.2.b2', 'should', ['directed', 'impacting'], 'policies that bear on welfare',
         'Design should focus on policies aimed at or affecting social welfare, such as social security, health, education and housing.',
         'Cover policies on social security, health, education, housing and similar fields that bear on welfare.',
         *D22, 'Which policy fields does the core curriculum cover?')
provider('2.2.b3', 'should', ['linking'], 'theory tied to empirical enquiry',
         'Design should tie theoretical analysis rigorously to empirical enquiry.',
         'Pair theory with empirical work in modules and assessments.',
         *D22, 'Where do students test a theory against data?')
provider('2.2.b4', 'should', ['inform'], 'values, ideologies and evidence in welfare debate',
         'Design should help students identify and understand the values, ideologies and evidence that shape welfare debates and policy design and delivery.',
         'Teach students to identify the values, ideologies and evidence behind welfare debates and policy.',
         *D22, 'Where do students learn to separate values from evidence in a policy debate?')
provider('2.2.b5', 'should', ['designed', 'influence'], 'knowledge of policy making and evaluation',
         'Design should build academic and practical knowledge of how policies meant to change social conditions are developed, carried out and evaluated.',
         'Build both academic and practical knowledge of policy development, implementation and evaluation.',
         *D22, 'Where do students meet practitioners or practical tasks in policy evaluation?')

D23 = ('2.1, 2.2, 3.3 and qaa/fheq-2024/4.15.b7', 'a student analyses a welfare issue or policy')
learner('2.3.b1', 'should', ['conceived', 'constructed'], 'subject-skill', 'how issues and problems are constructed',
        'Students should be able to identify, apply and critique ideas of how social issues come to be understood and social problems built.',
        'Teach students to identify and critique how social issues are framed and how problems come to be constructed.',
        'You should be able to identify, apply and critique ideas about how social issues come to be seen and problems defined.',
        *D23, 'Who first called this a social problem, and how did that framing shape the response?')
learner('2.3.b2', 'should', ['justified', 'established'], 'subject-skill', 'justifying interventions and provision',
        'Students should be able to identify, apply and critique how interventions are justified and provision set up.',
        'Teach students to examine and critique the reasons given for interventions and how provision is set up.',
        'You should be able to identify and critique how interventions are justified and services set up.',
        *D23, 'What reasons were given for this intervention, and do they hold?')
learner('2.3.b3', 'should', ['assess'], 'subject-skill', 'resourcing, design and effects of interventions',
        'Students should be able to identify, apply and critique how interventions are funded, designed and run, and assess their effects.',
        'Teach students to trace the funding, design and running of interventions and to assess their effects.',
        'You should be able to examine how interventions are funded, designed and run, and judge their effects.',
        *D23, 'Who pays for this intervention, how is it run, and what has it changed?')
learner('2.3.b4', 'should', ['influence', 'adopting', 'gives'], 'subject-skill', 'historical, environmental, global and discriminatory forces; beyond the state',
        'Students should be able to identify, apply and critique the historical, environmental, global and discriminatory forces behind welfare provision, looking beyond the state to other providers.',
        'Teach students to examine the historical, environmental, global and discriminatory forces behind provision, across all sectors and not the state alone.',
        'You should be able to examine the historical, environmental, global and discriminatory forces behind welfare, looking beyond the state to other sources of support.',
        *D23, 'Which actors besides the state provide welfare in your topic, and what history shaped that mix?')

D24 = ('2.1, 4.8.b1, 4.10.b1 and qaa/fheq-2024/4.15.b8', 'a student prepares policy work, briefings or proposals')
learner('2.4.b1', 'should', ['conduct'], 'subject-skill', 'policy analysis in varied settings',
        'Students should have the skills and knowledge to analyse policy in a range of professional settings.',
        'Give students practice in policy analysis for different kinds of professional setting.',
        'You should have the skills and knowledge to analyse policy in many kinds of workplace.',
        *D24, 'Where have you analysed a policy for a real or realistic organisation?')
learner('2.4.b2', 'should', ['communicate'], 'generic-skill', 'communicating research to varied audiences',
        'Students should be able to communicate research and recommendations in formats fit for professional, policy and lay audiences.',
        'Set tasks such as briefings, reports and public pieces so students learn to pitch research to different audiences.',
        'You should be able to share research and recommendations in formats that suit professionals, policy makers and the public.',
        *D24, 'How would you turn your findings into a briefing for a policy maker?')
learner('2.4.b3', 'should', ['develop', 'enhance'], 'subject-skill', 'innovative solutions for welfare',
        'Students should be able to devise new solutions to improve individual or shared welfare.',
        'Leave room in assessment for students to propose and defend new solutions to welfare problems.',
        'You should be able to come up with new solutions that improve welfare for individuals or groups.',
        *D24, 'What new solution would you propose to the problem you studied?')
learner('2.5', 'should', ['include', 'developed'], 'understanding', 'welfare from several sectors across contexts',
        "Students' understanding should include awareness that welfare is provided by several sectors and how provision develops nationally, internationally and globally.",
        'Teach welfare as provided by state, market, voluntary and family sectors, developing at national, international and global scale.',
        'Your understanding should include how welfare comes from several sectors and how it develops in national and global settings.',
        '1.12, 3.3.b11, 4.7.b2 and qaa/fheq-2024/4.15.b1', 'a student focuses only on the state',
        'Besides the state, who provides welfare in the area you are studying?',
        find=('Understanding should include awareness of multi-sectoral nature of providing welfare and how provision is developed in '
              'national, international and global contexts.'))
provider('2.6', 'should', ['embed', 'strengthen', 'navigate'], 'reflective practice and interpersonal skills',
         'Programmes should aim to build in reflective practice and interpersonal skills like communication and conflict resolution, to help students handle complex service delivery and governance.',
         'Build reflective practice, communication and conflict resolution into modules to prepare students for the realities of delivering services.',
         'a design duty on the programme', 'programme teams', '1.10, 3.3.b12 and 4.10.b3',
         'a team plans skills for practice or social administration', 'Where do students practise conflict resolution or reflect on practice?',
         find=("Programmes should aim to embed reflective practice alongside interpersonal skills such as communication and conflict "
               "resolution which will strengthen students' capacity to navigate the complexities of service delivery and governance."))
provider('2.7', 'should', ['integrate'], 'student voice in programme review',
         "Reviews of programme design and provision should take in students' contributions, through evaluations, staff-student meetings and co-production.",
         'Use module evaluations, staff-student meetings and co-production so student views feed into programme review.',
         'a duty on programme teams in review', 'programme teams', '1.34, 2.15 and 2.16', 'a team prepares a programme review',
         "How did students' views reach the last review, and what changed?",
         find='Review of programme design and provision should integrate student contributions.')

s('2.8', type='expectation', rung='none', force='will', level='fheq:6', appliesTo="honours and integrated master's students", addressee='learner',
  verbs=['progress', 'include'], about='progression through the levels to the threshold', domain='none', award=[HON, "integrated master's"],
  para=("A student will move from level to level under each institution's rules, each level building towards the threshold (and any "
        "higher) subject and generic skills; this will usually mean completing and gaining credit for all learning and assessment, "
        "practical parts included."),
  prac=("Plan each level to build towards the threshold skills; students will usually need to pass and earn credit for every part, "
        "practical work included."),
  ben=("You will move up a level at a time under your university's rules, building towards the skills your degree asks for; usually "
       "you will need to pass every part, practical work included."),
  aaw=("Describe this as the expected route, in will, by which an honours student (FHEQ Level 6; FQHEIS Level 10) or an integrated "
       "master's student (FHEQ Level 7; FQHEIS Level 11) progresses towards the threshold standards of 4.7 to 4.10. Cite it as "
       + CITE % '2.8' + ". Do not claim it sets progression rules, which stay with each institution. Set it beside the threshold cells, "
       "the descriptors qaa/fheq-2024/4.10, 4.12, 4.15 and 4.17, and spine:4 to spine:7."),
  aad=("Raise this when a student asks what moving from one year to the next involves, or a team maps credit to levels. Tell a student "
       "in plain words that each year builds towards the skills the degree asks for and that passing every part is usually needed; ask "
       "\"Which parts of this year are you less sure of passing?\" Avoid quoting the institution's regulations as if this statement set them."))
s('2.10', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='undergraduates taking the subject in joint or combined degrees',
  addressee='learner', verbs=['achieve', 'add', 'explore'], about='joint and combined degrees', domain='none', award=HON,
  para=("Undergraduates taking the subject in a joint or combined degree will achieve the core subject and generic skills set out here "
        "and add others from their other subject; they may also explore where the disciplines overlap."),
  prac=("In joint and combined routes, make sure students will reach the core skills of the subject while their other subject adds "
        "its own."),
  ben=("If you study this subject in a joint or combined degree, you will gain its core subject and general skills and add others from "
       "your second subject."),
  aaw=("Present this as the expected outcome, in will, for students taking Social Policy in a joint, combined or major/minor honours "
       "degree at FHEQ Level 6 (FQHEIS Level 10): the core of the skills in 4.7 to 4.10, not every cell. Cite it as " + CITE % '2.10' +
       ". Do not claim that a joint-honours student must meet every cell, or that the statement says which elements are core. Set it "
       "beside 1.2, 4.6 and qaa/fheq-2024/4.15.b1."),
  aad=("Raise this when a joint-honours student or a team designing a combined route asks how much of the standard applies. Explain "
       "plainly that the core subject skills still apply and the other subject adds its own; ask \"Which Social Policy skills does your "
       "route give you the chance to show, and which come from your other subject?\" Avoid suggesting that joint honours is a lesser standard."))
s('2.15', find=('Degree-awarding bodies, and their collaborative partnerships, routinely collect and analyse information and undertake '
                'periodic course review according to their own needs. Considering the student voice will form part of this.'),
  type='expectation', rung='none', force='will', level='none', appliesTo='degree-awarding bodies and their partners', addressee='provider',
  verbs=['collect', 'analyse', 'undertake', 'form'], about='periodic review with the student voice', domain='none', award=HON,
  para='Degree-awarding bodies and their partners gather and analyse information and review courses periodically; the student voice will be part of this.',
  prac='Your periodic course review will take account of what students say, alongside the data you routinely gather and analyse.',
  ben=('n/a', 'a duty on the degree-awarding body in course review'),
  aaw=("Treat this as an expectation, in will, on degree-awarding bodies and their partners: periodic course review takes account of "
       "the student voice. Cite it as " + CITE % '2.15' + ". Do not present it as a student outcome or as a regulatory requirement. Set "
       "it beside 2.7 (student contributions to review), 2.16 (external reviewers) and the external examining system described in 2.17."),
  aad=("Raise this with a programme team preparing a periodic review or answering student feedback. Frame it in practitioner terms and "
       "ask \"How did students' views reach this review, and what changed because of them?\" Do not hand it to a student as a task; it is "
       "the institution's duty, though students can be told their views count."))
s('2.16', type='expectation', rung='none', force='will', level='none', appliesTo='providers', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award=HON,
  para=("Externality is essential to UK quality assurance; providers will use external reviewers in periodic review for an independent "
        "view of proposed changes and to make sure threshold standards are met and content suits the subject."),
  prac=("In periodic review you will bring in external reviewers, for an independent view on proposed changes and a check that "
        "threshold standards are met and content fits the subject."),
  ben=('n/a', 'a duty on the provider in periodic review'),
  aaw=("Present this as an expectation, in will, on providers: external reviewers take part in periodic review to check that the "
       "threshold standards (4.7 to 4.10) are achieved and content suits the subject. Cite it as " + CITE % '2.16' + ". Do not present "
       "it as a learner outcome. Set it beside 2.15, 2.17 and the threshold cells of 4.7 to 4.10."),
  aad=("Raise this when a programme team plans a periodic review or asks who checks its standards. Frame it as practice the team will "
       "follow and ask \"Who is your external reviewer, and which threshold standards will they look at?\" Avoid presenting it to "
       "students as something they must meet."))

learner('3.4', 'must', ['requires', 'engage'], 'subject-skill', 'direct engagement with current debates',
        'The subject requires students to take part directly in current debates and arguments on social policy issues.',
        'Bring live policy debates into teaching so that students engage with them directly, as they must.',
        'You must engage directly with current debates and arguments on social policy issues.',
        '3.8, 2.4 and qaa/fheq-2024/4.15.b3.2', 'a student relies only on textbooks',
        'Which current policy debate have you followed closely this term, and where do you stand?',
        find='Social Policy requires that students directly engage with current debates and arguments surrounding social policy issues.',
        ty='requirement')
provider('3.9', 'should', ['reflected', 'ensure', 'fulfil'], 'inclusive learning and assessment design',
         "Inclusive learning design and assessment methods should reflect every student's needs so all can reach their potential, mature learners and those at higher risk of disadvantage among them.",
         'Design learning and assessment inclusively, with mature learners and students from disadvantaged backgrounds in mind.',
         'a duty on those who design learning and assessment', 'those who design learning and assessment',
         '1.29 to 1.32, 3.13 and theme:edi', 'a team designs learning or assessment',
         'How does this assessment work for a mature student with caring duties?',
         find=('The needs of all students should be reflected in inclusive learning design and assessment methods, to ensure that all '
               'learners can fulfil their potential.'))
provider('3.12', 'must', ['equipped', 'paid', 'ensure', 'investigate'], 'validating independent competence; misconduct',
         ("Graduates should be able to work in teams and use generative AI responsibly, but across a course's assessments care must be "
          "taken that each graduate's own competence is validated; rules on collusion and AI use should be clear where independence is "
          "assessed, and there must be capacity to investigate suspected misconduct."),
         ("Across the assessment diet, keep enough tasks that validate each student's independent competence, state the rules on "
          "collusion and AI clearly, and resource misconduct investigation."),
         'a duty on those who design assessment and on the institution', 'those who design assessment and the institution that resources it',
         '1.60 to 1.66 (which 3.12 itself points to), 3.10, 3.13 and 4.10.b4', 'a team designs assessment in response to generative AI',
         'Which assessments show what a student can do without help, and are the AI rules for them clear?', ty='requirement')
provider('3.13.b6', 'should', ['supported', 'complete'], 'support with competing deadlines',
         'Students should be helped to complete assessments when deadlines compete.',
         'Plan deadlines across modules and support students when they cluster.',
         'a duty on those who schedule and support assessment', 'those who schedule and support assessment',
         "3.13 (its other principles, in 'ought to'), 1.42.b4 and 4.10.b2", 'deadlines bunch or a team plans the assessment calendar',
         'Where do assessment deadlines cluster, and what support is in place then?')
provider('3.17', 'should', ['give', 'ensure', 'identify', 'communicate'], 'feedback on strengths for work',
         'Feedback should also show learners their strengths and, in academic tuition, their progress over time, so they can name and communicate those strengths at work.',
         "Use feedback, and personal tutoring, to name students' strengths and growth so they can describe them to employers.",
         'a duty on those who give feedback; the student meets it in the feedback received', 'those who give feedback',
         '3.16, 4.10 and 4.14.b5.masters', 'a team reviews feedback practice',
         'Does your feedback tell students what they do well in terms they could use in an interview?')

s('4.3', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='providers', addressee='provider',
  verbs=['perform', 'refer'], about='evidence above typical; Annex D', domain='none', award=HON,
  para=("Many graduates will do better than the typical standard; each provider decides how to evidence that and should refer to Annex D "
        "of the Frameworks, which describes the four honours classes (1st, 2.1, 2.2, 3rd)."),
  prac=("To evidence achievement above the typical standard, you should use Annex D of the Frameworks, its descriptions of first, upper "
        "second, lower second and third-class honours, alongside your own method."),
  ben=('n/a', 'a duty on the provider in judging and classifying achievement; the student meets it through marks and class'),
  aaw=("Treat this as a duty, in should, on each provider: to judge achievement above the typical rung it refers to Annex D of the "
       "Frameworks (std:doc:qaa-fheq-2024-framework, qaa/fheq-2024/annex-d/summary/r1/3rd to 1st). Cite it as " + CITE % '4.3' + ". Do "
       "not claim the statement itself sets class boundaries or mark bands. Set it beside 4.2 (the three rungs tied to third, second and "
       "first class), the Annex D bands (SL6 of the FHEQ document) and the band axis of std:ref:uk-assesscriteria."),
  aad=("Raise this when a team writes marking criteria or asks how the rungs relate to degree classes. Frame it for staff: threshold sits "
       "at the third-class line, typical at second class and excellent at first, while Annex D splits the second into 2.2 and 2.1; ask "
       "\"Do your criteria tell a 2.2 from a 2.1 where the typical column does not?\" Avoid telling students that most of them will "
       "exceed the typical standard as if it were a promise."))
s('4.4', type='requirement', rung='none', force='should', level='none', appliesTo='providers that develop competence standards', addressee='provider',
  verbs=['follow'], about='competence standards and EHRC guidance', domain='none', award=HON,
  para=("The minimum threshold standards do not set universal competence standards; a provider that develops competence standards under "
        "the Equality Act 2010 may draw on the statement and PSRB requirements, and should follow the latest Equality and Human Rights "
        "Commission guidance."),
  prac=("The threshold standards are not competence standards; if you set competence standards in a programme specification, inform "
        "them from this statement and any PSRB requirements, and you should follow the current Equality and Human Rights Commission guidance."),
  ben=('n/a', 'a duty on the provider in writing competence standards'),
  aaw=("Treat this as a duty, in should, on any provider that writes competence standards (in the Equality Act 2010 sense) for a Social "
       "Policy programme: follow current Equality and Human Rights Commission guidance. Cite it as " + CITE % '4.4' + ". Do not describe "
       "the threshold cells of 4.7 to 4.10 as competence standards or as universal requirements. Set it beside 4.2, 4.3 and the "
       "accessibility paragraphs 1.40 to 1.43."),
  aad=("Raise this when a programme team is drafting competence standards or a disabled student's adjustment turns on what is truly "
       "required. Frame it for staff and ask \"Is this a genuine competence standard, and have you checked it against the Commission's "
       "current guidance?\" Avoid presenting threshold standards to a student as fixed competences that rule out adjustments."))

TH = {
    '1.29': 'theme:edi', '1.31': 'theme:edi', '1.36': 'theme:edi', '1.39': 'theme:edi',
    '1.42.b1': 'theme:accessibility', '1.42.b2': 'theme:accessibility', '1.42.b3': 'theme:accessibility', '1.42.b4': 'theme:accessibility',
    '1.43': 'theme:accessibility',
    '1.48': 'theme:esd', '1.50': 'theme:esd', '1.52': 'theme:esd', '1.53': 'theme:esd',
    '1.56': 'theme:enterprise',
    '1.60': 'theme:generative-ai', '1.62.b5': 'theme:generative-ai', '1.65': 'theme:generative-ai',
}

S5 = dict(
    levels=[
        dict(id='fheq:4', role='cites', locator='D1, 2.11 (Certificate of Higher Education)'),
        dict(id='fheq:5', role='cites', locator='D1, 2.11 (Diploma of Higher Education)'),
        dict(id='fheq:6', role='cites', locator='D1, 2.8; 4.1; 4.5; 4.6'),
        dict(id='fheq:7', role='cites', locator='D1, 2.8; 4.1'),
        dict(id='fqheis:8', role='cites', locator='D1, 2.11 (as the statement gives it for the CertHE: Part E)'),
        dict(id='fqheis:9', role='cites', locator='D1, 2.11 (DipHE, as stated: Part E); 2.12 (ordinary degree and MA)'),
        dict(id='fqheis:10', role='cites', locator='D1, 2.8; 2.12; 4.1'),
        dict(id='fqheis:11', role='cites', locator='D1, 2.8; 4.1'),
    ],
    crosswalks=[
        dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent',
             basis='stated (D1, 2.8; 4.1: the honours degree at FHEQ Level 6 and FQHEIS Level 10); agrees with FHEQ Table 1'),
        dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent',
             basis="stated (D1, 2.8; 4.1: integrated master's and master's at FHEQ Level 7 and FQHEIS Level 11); agrees with FHEQ 4.17"),
        dict(**{'from': 'fheq:4'}, to='fqheis:8', relation='equivalent',
             basis='stated (D1, 2.11: CertHE at FHEQ Level 4, FQHEIS Level 8); differs from FHEQ Table 1, which puts the CertHE at FQHEIS 7 (Part E)'),
        dict(**{'from': 'fheq:5'}, to='fqheis:9', relation='equivalent',
             basis='stated (D1, 2.11: DipHE at FHEQ Level 5, FQHEIS Level 9); differs from FHEQ Table 1, which puts the DipHE at FQHEIS 8 (Part E)'),
    ],
)

S6 = [
    dict(id='theme:edi', role='carries', carriedIn=['1.6', '1.13', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '1.35', '1.36', '1.37',
                                                    '1.38', '1.39', '1.41', '1.57', '3.9', '3.13', '4.13']),
    dict(id='theme:accessibility', role='carries', carriedIn=['1.40', '1.41', '1.42', '1.43', '1.57', '3.13']),
    dict(id='theme:esd', role='carries', carriedIn=['1.14', '1.44', '1.45', '1.46', '1.47', '1.48', '1.49', '1.50', '1.51', '1.52', '1.53',
                                                    '2.3', '2.5', '3.3', '4.5', '4.7', '4.13']),
    dict(id='theme:enterprise', role='carries', carriedIn=['1.54', '1.55', '1.56', '1.57', '1.58', '1.59', '3.11']),
    dict(id='theme:generative-ai', role='carries', carriedIn=['1.60', '1.61', '1.62', '1.63', '1.64', '1.65', '1.66', '3.3', '3.12', '4.10', '4.15']),
]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-social-policy-2019-benchmarks (not ingested)',
         note='the fourth edition, 2019 minor update; earlier editions 2016, 2007 (Social Policy and Administration) and 2000 (with Social Work), back matter'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D',
         note="the degree classification descriptions for bachelor's degrees with honours (4.3)"),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ Levels 4 to 7 (2.8, 2.11, 4.1, 4.5, 4.6)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS (SCQF) Levels 8 to 11 (2.8, 2.11, 2.12, 4.1)'),
    dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='Education for Sustainable Development guidance (1.50)'),
    dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='Enterprise and Entrepreneurship Education guidance (1.54)'),
    dict(rel='refersTo', target='QAA Quality Code, 2024 update (not ingested)', note='front matter'),
    dict(rel='refersTo', target="QAA Master's Degree Characteristics Statement (not ingested)", note='4.11'),
    dict(rel='refersTo', target='Equality and Human Rights Commission guidance on competence standards (not ingested)', note='4.4'),
    dict(rel='overlaps', target='std:doc:qaa-public-policy-and-public-administration-2025-benchmarks',
         note='inferred: 2.6 names overlaps with Public Policy and Administration'),
]

SB1 = [
    'Examines policy and practice through the lens of human welfare: social need, social justice and how resources are divided and allocated (D1, 1.4 to 1.6).',
    'Both academic and applied: it explains social problems, analyses current interventions and argues for alternatives, bridging theory and practice (D1, 1.4).',
    'Separates the discipline (capitalised) from the practice of the state and other bodies in education, health, care, social security, pensions and housing (D1, 1.3).',
    'Studies welfare well beyond the state: commercial, voluntary and community sectors and families, in mixed economies of welfare (D1, 1.11, 1.12).',
    'Rooted in Social Administration and still attentive to how welfare institutions are governed and run (D1, 1.9; 2.6).',
    'Normative by nature: attends to values, ideology, social divisions and lived experience (D1, 1.6, 1.20, 1.38).',
    "Reckons with its colonial history and the global majority's understandings, while holding that it can never be fully decolonised (D1, 1.21 to 1.27).",
    'Works across local, devolved, national and international levels, including subsidiarity, and treats sustainability as central to welfare (D1, 1.7, 1.14).',
    'Taught in single and joint honours and as modules in wider social science degrees, beside Sociology, Politics, Criminology and Economics (D1, 1.2; 1.59).',
]

SB2 = [
    dict(theme='theme:edi', inThisSubject=("structural discrimination and intersecting disadvantage are subject matter; a strong decolonising strand runs "
                                           "through curriculum and analysis; diverse entrants, awarding gaps, co-construction and the statement's own "
                                           "definitions of equity, diversity and inclusion (D1, 1.13, 1.21 to 1.39); reflexive, inclusive practice is "
                                           "a graduate outcome (1.39) and EDI is a master's skill (4.13)"),
         statements=['1.27', '1.29', '1.31', '1.36', '1.39', '3.9', '3.3.b18', '4.13.b5.masters', '4.13.b6.masters']),
    dict(theme='theme:accessibility', inThisSubject=("anticipatory accessibility under equality law, four areas for inclusive courses, placement "
                                                     "support for disabled students and accessible assessment principles (D1, 1.40 to 1.43, 3.13)"),
         statements=['1.42.b1', '1.42.b2', '1.42.b3', '1.42.b4', '1.43', '3.13.b6']),
    dict(theme='theme:esd', inThisSubject=("sustainability as central to welfare and as eco-social policy, the UN goals as a way in, the Inner "
                                           "Development Goals, and climate change deepening privilege (D1, 1.14, 1.44 to 1.53); the UN goals form a "
                                           "full row of the knowledge table (4.7) and a master's skill (4.13)"),
         statements=['1.14', '1.48', '1.50', '1.52', '1.53', '3.3.b7', '3.3.b20', '4.5.b3', '4.7.b1.typical', '4.7.b4', '4.7.b4.typical',
                     '4.7.b4.excellent', '4.13.b6.masters']),
    dict(theme='theme:enterprise', inThisSubject=("problem solving, creative thinking and real-world experience through placements, volunteering and "
                                                  "authentic assessment, with careers in the public, voluntary and private sectors (D1, 1.54 to 1.59, 3.11)"),
         statements=['1.56', '4.5.b2']),
    dict(theme='theme:generative-ai', inThisSubject=("critical, ethical and reflective use of generative AI, its gains and risks (including colonial "
                                                     "bias and environmental cost), institutional policy and its place in assessment (D1, 1.60 to 1.66, 3.12); "
                                                     "AI is a knowledge area (3.3) and part of the technology skill row (4.10) and a master's skill (4.15)"),
         statements=['1.60', '1.62.b5', '1.65', '3.12', '3.3.b19', '4.10.b4', '4.10.b4.typical', '4.10.b4.excellent', '4.15.b5.masters']),
]

SB3 = dict(
    areas=[
        dict(component='3.2', gloss='policy at local, national, international and global scale; fields from criminal justice to work and labour markets'),
        dict(component='3.3', gloss='five groups of knowledge: welfare systems, policy processes, impacts, concepts and theories, research and policy analysis'),
    ],
    practices=[
        dict(component='3.4', kind='teaching', gloss='lectures, seminars and workshops; placements, visits, volunteering, exchanges and life experience'),
        dict(component='3.5', kind='teaching', gloss='virtual learning, data software, distance and blended learning, MOOCs'),
        dict(component='3.6', kind='learning', gloss='a portfolio of experience that prepares for work'),
        dict(component='3.7', kind='learning', gloss='scheduled, peer, virtual, self-directed and experiential learning'),
        dict(component='3.8', kind='learning', gloss='critical reading, independent research, group work, contact with practitioners and users'),
        dict(component='3.10', kind='assessment', gloss='constructive alignment; assessment that reflects progression'),
        dict(component='3.11', kind='assessment', gloss='authentic assessment recommended'),
        dict(component='3.13', kind='assessment', gloss='accessible, inclusive principles, in ought to'),
        dict(component='3.14', kind='assessment', gloss='indicative types, from essays and exams to policy briefings and podcasts'),
        dict(component='3.15', kind='assessment', gloss='diversity monitored at programme level'),
        dict(component='3.16', kind='assessment', gloss='constructive feedback in many forms'),
    ],
)

SB4 = dict(
    rungs=[
        dict(rung='threshold', leadIn='4.7 to 4.10 (rungs defined in 4.2)', award=HON, items=18),
        dict(rung='typical', leadIn='4.7 to 4.10 (rungs defined in 4.2)', award=HON, items=18),
        dict(rung='excellent', leadIn='4.7 to 4.10 (rungs defined in 4.2)', award=HON, items=19),
        dict(rung='threshold', leadIn="4.12 to 4.15 (master's lists; no rung named)", award=MAS, items=25),
    ],
    rungBases=("4.2: threshold is the minimally acceptable requirement for a third-class honours degree; typical the required attainment "
               "for a second-class degree; excellent the required attainment for a first. 4.6: the honours rungs are successive and "
               "cumulative. The four master's lists (4.12 to 4.15) name no rung and are recorded as threshold for the master's award by "
               "the batch 1 convention (Part E)"),
    outcomeLists=[
        dict(leadIn='3.3', gloss='knowledge areas graduates demonstrate, in five groups (plain present; force describes)', items=33, award=['honours']),
        dict(leadIn='4.5', gloss='honours outcomes in line with the Frameworks (expected to; force describes)', items=4, award=['honours']),
    ],
    outcomes=OUT,
)

SB4A_FULL = []

SB5 = [
    dict(body='Professional, statutory and regulatory bodies (PSRBs), none named',
         says=("statements can support PSRBs in defining academic standards; providers may weigh PSRB requirements; courses with "
               "professional outcomes may need accreditation; competence standards may draw on PSRB requirements (D1, front matter; 2.18; 4.4)"),
         requirements='not yet ingested (Part E)'),
    dict(body='Equality and Human Rights Commission',
         says='providers developing competence standards should follow its most recent guidance (D1, 4.4)',
         requirements='not yet ingested (Part E)'),
    dict(body='Office for Students',
         says='in England benchmark statements are not sector-recognised standards under its regulatory framework (D1, front matter)',
         requirements='not-applicable-by-design: named for status only (Part E)'),
    dict(body='Disabled Students Commission',
         says='its website is the pointer for more on accessibility (D1, 1.40)',
         requirements='not-applicable-by-design: named as a resource (Part E)'),
    dict(body='Advance HE',
         says='co-author with QAA of the Education for Sustainable Development guidance programmes can draw on (D1, 1.50)',
         requirements='std:doc:qaa-advancehe-esd-2021-guidance'),
]

SB6 = dict(
    themes=[
        dict(id='theme:edi', named='Equity, diversity and inclusion', carriedIn=S6[0]['carriedIn'], statements=SB2[0]['statements']),
        dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=S6[1]['carriedIn'], statements=SB2[1]['statements']),
        dict(id='theme:esd', named='Education for sustainable development', carriedIn=S6[2]['carriedIn'], statements=SB2[2]['statements']),
        dict(id='theme:enterprise', named='Employability, entrepreneurship and enterprise education', carriedIn=S6[3]['carriedIn'], statements=SB2[3]['statements']),
        dict(id='theme:generative-ai', named='Generative artificial intelligence', carriedIn=S6[4]['carriedIn'], statements=SB2[4]['statements']),
    ],
    frameworks=[
        dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.8', '2.11', '4.1', '4.3', '4.5', '4.6']),
        dict(framework='scqf', levels=['fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.8', '2.11', '2.12', '4.1']),
    ],
    bodies=[
        dict(body='PSRBs (none named)', citedIn=['front matter', '2.18', '4.4']),
        dict(body='Equality and Human Rights Commission', citedIn=['4.4']),
        dict(body='Office for Students', citedIn=['front matter']),
        dict(body='Disabled Students Commission', citedIn=['1.40']),
        dict(body='Advance HE', citedIn=['1.50']),
    ],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D',
             named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies',
             citedIn=['4.3'], role='descriptions of the four honours classes (1st, 2.1, 2.2, 3rd) for evidence above typical'),
        dict(document='std:doc:qaa-fheq-2024-framework', named='the Frameworks for Higher Education Qualifications of UK Degree Awarding Bodies',
             citedIn=['4.5'], role='the four honours outcomes of 4.5 are set in line with it'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='the QAA and Advance HE Education for Sustainable Development',
             citedIn=['1.50'], role='a resource for curriculum design'),
        dict(document='std:doc:qaa-enterprise-2018-guidance',
             named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers', citedIn=['1.54'],
             role='further guidance on EEE'),
        dict(document='QAA Quality Code, 2024 update (not yet ingested)', named='an update to the Quality Code', citedIn=['front matter'], role='a further reference point'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='QAA Creating Inclusive Subject Communities (not ingested)', named='the QAA resource on Creating Inclusive Subject Communities',
             citedIn=['1.36'], role='an example of good EDI practice'),
        dict(document='QAA Generative artificial intelligence resources (not ingested)', named='Generative artificial intelligence',
             citedIn=['1.66'], role='further guidance on GenAI'),
        dict(document="QAA Master's Degree Characteristics Statement (not ingested)", named="The Master's Degree Characteristics Statement",
             citedIn=['4.11'], role="named in the lead-in to the master's standards"),
        dict(document='UN Sustainable Development Goals (external)', named='The UN Sustainable Development Goals (UN SDGs)',
             citedIn=['1.45', '1.46', '1.47', '4.7'], role='the frame of the sustainability theme and a row of the knowledge table'),
        dict(document='Inner Development Goals (external)', named='the Inner Development Goals', citedIn=['1.50'],
             role='personal skills for sustainable development'),
        dict(document='Equality Act 2010 (law)', named='Equality Act 2010', citedIn=['1.31', '1.40', '4.4'],
             role='protected characteristics, accessibility duties, competence standards'),
        dict(document='Disability Discrimination Act 1995 and SEND (Northern Ireland) Order 2005 (law, Northern Ireland)',
             named='Disability Discrimination Act 1995 and Special Educational Needs and Disability (Northern Ireland) Order 2005',
             citedIn=['1.40'], role='accessibility duties in Northern Ireland'),
    ],
)

B1 = [
    dict(slug='social-policy-discipline', definition='the capitalised name for the academic discipline, set against lower-case social policy, the practice of the state and other bodies in welfare fields (D1, 1.3)',
         beneficiaryDefinition='the subject you study, as distinct from the policies it studies', scopeNote='the statement\'s own convention', category='unknown', practices=['education']),
    dict(slug='equity', definition='giving each person the particular resources and chances they need to reach an equal outcome (D1, 1.35)',
         beneficiaryDefinition='getting what you in particular need to reach the same outcome as others', scopeNote='one of the three EDI terms the statement defines', category='unknown', practices=['education']),
    dict(slug='diversity', definition="recognising and valuing students' differing backgrounds and outlooks (D1, 1.35)",
         beneficiaryDefinition='your background and outlook being recognised and valued', scopeNote='one of the three EDI terms', category='unknown', practices=['education']),
    dict(slug='inclusion', definition='an environment that respects the dignity and humanity of everyone (D1, 1.35)',
         beneficiaryDefinition='a setting where your dignity is respected', scopeNote='one of the three EDI terms', category='unknown', practices=['education']),
    dict(slug='polycrisis', definition='several crises at once, each worsening the others (D1, 1.10, footnote 1)',
         beneficiaryDefinition='several crises happening together and feeding each other', scopeNote='used in the plural', category='unknown', practices=['education']),
    dict(slug='subsidiarity', definition='meeting social needs at the closest level of government able to do so (D1, 1.7)',
         beneficiaryDefinition='dealing with problems at the most local level that can handle them', scopeNote='named as a principle students should understand', category='unknown', practices=['education']),
    dict(slug='authentic-assessment', definition='assessment that mirrors real-world scenarios as closely as an academic setting allows (D1, 1.56; 3.11)',
         beneficiaryDefinition='assessment that copies real work tasks', scopeNote='recommended in 3.11', category='unknown', practices=['education']),
    dict(slug='threshold-standard', definition='the least a student must reach to gain a third-class honours degree (D1, 4.2)',
         beneficiaryDefinition='the least you need to show to gain honours', scopeNote='first column of the 4.7 to 4.10 tables', category='unknown', practices=['education']),
    dict(slug='typical-standard', definition='the attainment required for a second-class honours degree (D1, 4.2)',
         beneficiaryDefinition='what a second-class degree asks of you', scopeNote='second column', category='unknown', practices=['education']),
    dict(slug='excellent-standard', definition='the attainment required for a first-class honours degree (D1, 4.2)',
         beneficiaryDefinition='what a first-class degree asks of you', scopeNote='third column; cumulative on the other two (4.6)', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='social-policy-discipline', form='Social Policy', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
    dict(concept='equity', form='equity', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='diversity', form='diversity', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='inclusion', form='inclusion', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='polycrisis', form='polycrises', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
    dict(concept='subsidiarity', form='subsidiarity', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
    dict(concept='authentic-assessment', form='authentic assessment', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='threshold-standard', form='threshold standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='typical-standard', form='typical standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='excellent-standard', form='excellent standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
]
B4 = [dict(rel='contrasts-with', **{'from': 'threshold-standard'}, to='typical-standard', note='4.2: the first two rungs'),
      dict(rel='contrasts-with', **{'from': 'typical-standard'}, to='excellent-standard', note='4.2 and 4.6: the excellent rung incorporates and extends the others')]
B5 = []

D3 = [
    dict(citation='QAA (2019) Subject Benchmark Statement: Social Policy, fourth edition (minor update)', settles=['S7'], asked='2026-10-03', state='wanted'),
    dict(citation="QAA Master's Degree Characteristics Statement (current edition)", settles=['SB6', 'S7'], asked='2026-10-03', state='wanted'),
]

E = [
    'SB4, pattern (differs from Psychology): one three-column table per block (knowledge and understanding 4.7, subject-specific skills 4.8, generic intellectual skills 4.9, generic transferable skills 4.10), each outcome a row with threshold (3rd class), typical (2nd class) and excellent (1st class) cells. Recorded one record per cell, ids `<n>.b<k>`, `.typical`, `.excellent`, `gradeOf` stated by row (batch 1 convention).',
    'SB4, flattened tables (P3): every table is flattened in the held text, cells running threshold, typical, excellent, row by row, with paragraph breaks falling at irregular points. Placement read from that order and the progression of verbs. Least sure: 4.7 row 1, where the typical cell (in-depth knowledge with sustainability and the UN goals) is not a plain step up from the threshold cell; 4.8 row 3, where the excellent cell ("understand the relevance of and apply") reads weaker than the typical cell ("distinguish ... and critically reflect"), so the two may be swapped; 4.8 row 5, where the threshold cell already asks students to undertake research.',
    'SB4, 4.9 orphan cell (P3): after the research row the held text has one more cell, "Synthesis skills", with no partners. Recorded as an excellent cell on its own row (4.9.b5.excellent, gradeOf none), as its wording reads as first-class work; it may instead belong to the typical column, or the research row may run threshold "data collection with supervisory support", typical "independent research", excellent "synthesis", with the second data collection cell misplaced. Rung counts: threshold 18, typical 18, excellent 19.',
    'S4, force of the table cells: the lead-ins (4.7 to 4.10) say "are expected to possess", outside the five. Threshold cells are `threshold` (4.2 defines the rung as the minimum for a third; forceFrom 4.2). Typical and excellent cells are `must`, from 4.2\'s "describes the required attainment" (the batch 1 convention reads "required" as must; forceFrom 4.2). For Abbott: is "required attainment" for a class must, or should these read as will?',
    "SB4, master's (P3): four lists (4.12 knowledge and understanding, 4.13 subject-specific skills, 4.14 generic intellectual skills, 4.15 generic transferable skills), 25 items, no rung named. Recorded as rung threshold, award master's, level fheq:7, ids `.masters`, by the batch 1 convention; force `describes`, since the lead-ins say \"are expected to possess\" or \"are expected to demonstrate\", outside the five, with no stated minimum.",
    "S4, master's lead-ins (issuer slips): 4.12 calls its list \"generic transferable skills\" though its heading (the 4.7-style block) and content are knowledge and understanding; 4.14 calls its list \"generic transferable skills\" under the heading \"Generic intellectual skills\". Domains set by heading and content: 4.12 knowledge or understanding (4.12.b6 subject-skill), 4.13 subject-skill, 4.14 and 4.15 generic-skill. 4.11 names a \"Master's Degree Characteristics Statement\" as setting out the characteristics; read as the 4.12 to 4.15 lists that follow (D3).",
    "S4, repeated item: 4.12.b6 and 4.14.b4 have identical text (research methods and a supervised dissertation). Both kept as records, each on its own span (4.14.b4 found after its lead-in); for P3 whether one is a duplication slip.",
    'S4, 3.3 (33 items): "Graduates of Social Policy courses in the UK demonstrate knowledge in the following areas", plain present with no modal, in five groups with run-in headings. Recorded as an outcome list, force `describes`, domain knowledge, honours (fheq:6), as earlier runs did for plain-present graduate lists (open point 5). 3.1 says it may be inappropriate to be prescriptive about knowledge. Items 3.3.b8, b14, b21, b26 and b33 cut by `find` to drop the run-in group headings the skeleton attached. 3.3.b12 holds its own "should" (embedding reflective practice); recorded with the list\'s describes. Verbs left empty where an item is a noun phrase with no verb of its own.',
    'S4, 4.5 (4 items): "In line with the Frameworks ..., Social Policy graduates are expected to:", honours outcomes outside the rungs. Recorded as an outcome list, force `describes` ("expected to"), rung none. Their content tracks the FHEQ honours descriptor (qaa/fheq-2024/4.15).',
    'S4, statements taken from prose (in should unless named): 1.7, 1.14 (must), 1.17 (must), 1.20, 1.24 (must, with a should), 1.27, 1.29, 1.31, 1.36, 1.39 (will), 1.42.b1 to b4 (lead-in should), 1.43, 1.48, 1.50, 1.52, 1.53, 1.56, 1.60, 1.62.b5, 1.65, 2.1, 2.2.b1 to b5, 2.3.b1 to b4, 2.4.b1 to b3, 2.5, 2.6, 2.7, 2.8 (will), 2.10 (will), 2.15 (will), 2.16 (will), 3.4 (requires, must), 3.9, 3.12 (must), 3.13.b6, 3.17, 4.3, 4.4. Provider duties carry no student version. Several are cut to their obliging sentence by `find`.',
    'S4, 1.14: "Social policy must recognise ..." is lower case, which by 1.3 means the practice, not the discipline; read as a requirement on the discipline and its curricula, since the paragraph is about what the discipline embeds and what graduates can do. For P3.',
    'S4, 1.65: "Social Policy degrees programmes will have to adhere to" institutional GenAI policy (must-like, outside the five) and "students should be taught" in one paragraph; one record at should.',
    'S4, 2.1: the issuer says "four fundamental questions" and lists six (what, how, why, whether, to whom, by whom). Kept as written.',
    'S4, obliging words outside the five, not taken as statements, for Abbott: 1.32 "This will require programme designs ..." (a consequence of a plain-present aim); 1.51 "it is important that programmes seek to integrate"; 1.57 "need to ensure they are accessible"; 1.62.b4 "students need to be able to critique" (inside a list of risks); 2.9 "It is expected that a student ... would be capable"; 3.1 "ought to remain responsive"; 3.11 "Authentic assessments are recommended"; 3.13 "ought to be accessible and inclusive" (six of its seven principles; the seventh, b6, has its own should and is taken); 3.15 "ought to be evaluated and monitored"; 3.16 "an appreciation ... is expected and discussed". For Abbott: should "ought to" read as should?',
    'S4, plain-present provider norms, not statements (template open point 5): 1.32, 1.33, 1.34, 1.37, 1.38, 1.40 (teaching teams take a proactive approach), 1.41, 1.63 (developers consider carefully), 1.64, 2.13, 2.14, 3.2 (students acquiring insights), 3.4 to 3.8 (methods), 3.10, 3.14, 3.16.',
    'S4, predictive or permissive words not taken: 1.29 "will likely mean"; 1.49 "will likely be working"; 1.57 "programmes will likely offer"; 2.6 "will have several overlaps"; 2.11 "may exit earlier and be eligible" (exit awards); 2.17 "external examiners will be asked"; 2.18 "may also require evaluation and accreditation".',
    'S4, 4.2 defines the rungs ("must attain" for the threshold) and is recorded in SB4 rungBases, not as a statement; 4.6 says the standards are "not a checklist" and the rungs cumulative.',
    'S4, section 1 to 3 learner statements are recorded at honours (fheq:6), the statement\'s main award; several (1.7, 1.17, 1.20, 2.1, 2.3, 2.4) are worded for the subject at any level and may also hold for the master\'s. For P3.',
    'S5, levels (doubt for P3): 2.11 places the CertHE at FQHEIS Level 8 and the DipHE at FQHEIS Level 9. The FHEQ document (Table 1) places them at SCQF 7 and 8. Recorded as stated with the difference noted in S5; the issuer\'s text may be in error (the same slip as the History of Art, Architecture and Design statement, run 0111).',
    "S5, generic skills: every generic-skill record carries fheq:6 (honours) or fheq:7 (master's), both in S5; the framework descriptors each instruction sets them beside are qaa/fheq-2024/4.15 and 4.17 and the Annex D cells (std:doc:qaa-fheq-2024-framework); these pairings are inferred, ours.",
    'SB6: five cross-cutting themes, named in the front matter and each with its own heading in section 1. GenAI uses theme:generative-ai. Decolonisation is a strong strand (1.21 to 1.27, 2.5, 4.13.b6) with no shared theme id; recorded under theme:edi here. For Abbott: a theme:decolonisation id?',
    'SB6: CQFW is not cited. The Social Policy Association appears only in the references and the advisory group history (excluded matter), and the Joint University Council only in the back matter; neither is in SB5.',
    'SB5: the PSRBs are named only as a class; no requirements document can be linked. The EHRC\'s guidance is not yet ingested. The Office for Students is named for status only; the Disabled Students Commission as a resource. Advance HE links to the ingested ESD guidance.',
    'S2, subjects: HECoS 100502 and CAH15-01-03 (social policy) taken as stated: the title names the subject and both codes carry that label. Other codes in statedSubjects are for degrees in which the subject is taught (1.2, 1.59) or neighbouring fields (1.9, 2.6), not the benchmark\'s own scope. International social policy (100645) and welfare policy (100649) sit in the same CAH group and are not named.',
    'S7: the previous edition (2019, fourth edition, minor update) is named in the back matter; earlier advisory groups 2016, 2007 (Social Policy and Administration) and 2000 (Social Policy and Administration and Social Work). Not ingested (D3). The overlap with Public Policy and Public Administration (2.6) is an inferred relation.',
    'S1, licence: the text gives a copyright notice and no re-use terms.',
    'S9: not researched in P1.',
    "Pattern (differs from Psychology): rungs in flattened three-column tables tied explicitly to degree classes (4.2), with an orphan cell; typical and excellent defined as 'required attainment' (must); a 33-item plain-present knowledge list; four master's lists with no rungs; five theme sections before the distinctive features, as in the 2026 revision; a strong decolonising strand; no subject body named outside the back matter.",
]
