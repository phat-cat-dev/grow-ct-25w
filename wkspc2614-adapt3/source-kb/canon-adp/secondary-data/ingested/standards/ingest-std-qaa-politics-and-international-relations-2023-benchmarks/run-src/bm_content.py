# Judgement for run 0127, QAA Subject Benchmark Statement: Politics and International Relations (March 2023). std run agent.
# Built by tools/bm_build.py (BM-BRIEF 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft).
# Written fresh from the held text alone (benchmark rule 6); frameworks consulted by id only.
import os as _os

_HELD = '/home/claude/wkspc2601-library/txt/qaa-2023-politics-international-relations-subject-benchmark-statement-standard.norm.txt'
_ROOT = '/home/claude/wkspc2601-library/ingested/standards'   # moved to the source library (std N-0119)
_T = open(_HELD if _os.path.exists(_HELD) else _os.path.join(_ROOT, _HELD), encoding='utf-8').read()


def cut(a, b):
    """the held text from the first `a` to the end of the next `b`, exactly."""
    k = _T.find(a)
    e = _T.find(b, k)
    assert k >= 0 and e >= 0, (a, b)
    return _T[k:e + len(b)]


HON = "bachelor's with honours"
MAS = "master's"
SUBJ = 'Politics and International Relations Subject Benchmark Statement'
CITE = 'QAA (2023), ' + SUBJ

META = dict(
    run='0127', p1='2026-10-03 18:24',
    title='Subject Benchmark Statement Politics and International Relations',
    heading='Subject Benchmark Statement: Politics and International Relations (QAA, March 2023)',
    edition='March 2023 (fifth edition)', published='2023-03',
    status='current',
    supersedes='the fourth edition (2019), as the back matter states; not held',
    subjects=[
        dict(scheme='hecos', code='100491', label='politics', basis='stated'),
        dict(scheme='hecos', code='100490', label='international relations', basis='stated'),
        dict(scheme='hecos', code='100489', label='international politics', basis='stated'),
        dict(scheme='hecos', code='101288', label='international studies', basis='stated'),
        dict(scheme='cah', code='CAH15-03-01', label='politics', basis='stated'),
        dict(scheme='cah', code='CAH15-03', label='politics', basis='stated'),
        dict(scheme='hecos', code='100618', label='comparative politics', basis='stated'),
        dict(scheme='hecos', code='100610', label='UK government/parliamentary studies', basis='inferred'),
    ],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, the 2022 onward revisions with cross-cutting themes (fifth edition of this statement, published 8 March 2023)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what an honours graduate in Politics and International Relations should know, "
                     "understand and be able to do at the point of award. It gives one rung only, the threshold, in three lists "
                     "(knowledge and understanding; discipline-specific skills; cognitive abilities and skills) and leaves performance "
                     "above the threshold to Annex D of QAA's Frameworks. Reach for it when designing, reviewing or describing a politics, "
                     "international relations or related course, its outcomes, its assessment or its treatment of the four cross-cutting "
                     "themes. It is not a curriculum and not a regulatory requirement, and it sets no master's standards."),
    summary=("Published by QAA in March 2023 as the fifth edition, the statement describes the discipline (power, governance, conflict "
             "and cooperation, at every scale from local to global), its purposes and distinctive features and the content, teaching "
             "and assessment of an honours degree. It treats four cross-cutting themes: equality, diversity and inclusion; accessibility; "
             "sustainability (education for sustainable development, with the SDGs); and enterprise and entrepreneurship education. "
             "Its benchmark standards are threshold only: 28 items in three lists at 4.3 to 4.5, for the bachelor's degree with honours "
             "at FHEQ level 6 and FQHEIS level 10, with Annex D cited for the classes above the threshold. A further skills list (3.3) "
             "names abilities a course may develop. It names no professional, statutory or regulatory body for the subject; master's "
             "study at FHEQ level 7 is mentioned only as resting on the same principles at a higher level."),
    authority=("reference: a sector reference point, not a regulatory requirement (D1, front matter); not a sector-recognised standard "
               "under the OfS framework in England; a key reference point in Wales and Scotland; part of current quality arrangements "
               "in Northern Ireland (D1, front matter: Relationship to legislation)"))

S2 = dict(
    governs=("what a graduate in Politics and International Relations can be expected to know, do and understand at the end of an "
             "honours degree, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 1.4; 4.1)"),
    awards=["bachelor's degrees with honours, single honours and joint honours where the subject is at least half the curriculum",
            "postgraduate taught degrees (named only: same core principles at a higher level, 1.4)"],
    levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope=('"It primarily addresses single honours courses in Politics and International Relations and joint honours courses in '
                 'which either comprises at least half of the curriculum leading to a degree." (D1, 1.4)'),
    statedSubjects=[
        dict(name='Politics and International Relations', locator='(D1, title; 1.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100491', label='politics'), dict(scheme='hecos', code='100490', label='international relations'),
                    dict(scheme='cah', code='CAH15-03-01', label='politics')]),
        dict(name='Government', locator='(D1, 1.6)', kind='programme title', codes=[]),
        dict(name='International Politics', locator='(D1, 1.6)', kind='programme title', codes=[dict(scheme='hecos', code='100489', label='international politics')]),
        dict(name='International Relations', locator='(D1, 1.6)', kind='programme title', codes=[dict(scheme='hecos', code='100490', label='international relations')]),
        dict(name='International Studies', locator='(D1, 1.6)', kind='programme title', codes=[dict(scheme='hecos', code='101288', label='international studies')]),
        dict(name='Political Studies', locator='(D1, 1.6)', kind='programme title', codes=[dict(scheme='hecos', code='100491', label='politics')]),
        dict(name='Political Science', locator='(D1, 1.6)', kind='programme title', codes=[dict(scheme='hecos', code='100491', label='politics')]),
        dict(name='International Development', locator='(D1, 1.6: may include significant subject content)', kind='programme title',
             codes=[dict(scheme='hecos', code='100488', label='international development')]),
        dict(name='Legislative Studies', locator='(D1, 1.6: may include significant subject content)', kind='programme title',
             codes=[dict(scheme='hecos', code='100610', label='UK government/parliamentary studies')]),
        dict(name='Peace Studies; War Studies', locator='(D1, 1.6: may include significant subject content)', kind='programme title',
             codes=[dict(scheme='hecos', code='100617', label='war and peace studies')]),
        dict(name='comparative politics', locator='(D1, 3.2)', kind='specialism', codes=[dict(scheme='hecos', code='100618', label='comparative politics')]),
        dict(name='public policy and administration', locator='(D1, 3.2)', kind='specialism',
             codes=[dict(scheme='hecos', code='100647', label='public policy'), dict(scheme='hecos', code='100090', label='public administration')]),
        dict(name='feminism, gender studies, queer studies and intersectional approaches', locator='(D1, 3.2)', kind='specialism',
             codes=[dict(scheme='hecos', code='100621', label='gender studies')]),
        dict(name='international aid and development', locator='(D1, 3.2)', kind='specialism', codes=[dict(scheme='hecos', code='100488', label='international development')]),
    ])

SECTIONS = {
    '1': 'Context and purposes of a Politics and International Relations degree',
    '2': 'Distinctive features of a Politics and International Relations degree',
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
}
SUB = [
    ('1.1', '1.4', 'Context and purposes of a Politics and International Relations degree'),
    ('1.5', '1.10', 'Purposes and characteristics of a Politics and International Relations degree'),
    ('1.11', '1.13', 'Equality, diversity and inclusion (EDI)'),
    ('1.14', '1.14', 'Accessibility'),
    ('1.15', '1.18', 'Sustainability'),
    ('1.19', '1.22', 'Enterprise and entrepreneurship education'),
    ('2.1', '2.2', 'Design'),
    ('2.3', '2.5', 'Progression'),
    ('2.6', '2.6', 'Flexibility'),
    ('2.7', '2.9', 'Partnership'),
    ('2.10', '2.12', 'Monitoring and review'),
    ('3.1', '3.1', 'Content, structure and delivery'),
    ('3.2', '3.3', 'Content and skills'),
    ('3.4', '3.11', 'Learning and teaching'),
    ('3.12', '3.16', 'Assessment'),
    ('4.1', '4.2', 'Introduction'),
    ('4.3', '4.3', 'Knowledge and understanding'),
    ('4.4', '4.4', 'Discipline-specific skills'),
    ('4.5', '4.5', 'Cognitive abilities and skills'),
]

G = {
    '1.1': 'the field studies power, governance, participation, conflict and cooperation worldwide; graduates equipped for careers, citizenship and leading change',
    '1.2': 'the history of the subject in UK universities and the forces that have shaped its courses',
    '1.3': 'a broad, contested field whose rigour, diversity and variety of courses are its strengths',
    '1.4': 'what the statement covers: single and joint honours (subject at least half); taught master\'s on the same principles at a higher level (S4)',
    '1.5': 'courses aim at a broad, structured education building knowledge, intellect and skills',
    '1.6': 'the range of degree titles in and near the field',
    '1.7': 'ways of knowing: description, explanation, normative theory, positive theory and non-universalising approaches',
    '1.8': 'politics: who gets what, when, how, why and where; its central questions',
    '1.9': 'international relations: a world of many polities, states and actors beyond them',
    '1.10': 'quantitative and qualitative research methods and cognate subjects',
    '1.11': 'EDI: the discipline analyses power, privilege and exclusion, including in its own boundaries',
    '1.12': 'EDI: critical, self-reflective learners who examine the discipline\'s colonial and other origins and read marginalised voices',
    '1.13': 'EDI: inclusive learning communities, closing gaps in access, attainment and awarding, partnership with students',
    '1.14': 'accessibility: courses designed for all, gaps reduced, reasonable adjustments in place',
    '1.15': 'sustainability is integral to the subject; definitions from the ESD guidance',
    '1.16': 'ESD to run through the whole course, framed by the SDGs (S4)',
    '1.17': 'teaching and assessment methods for delivering ESD and building community engagement',
    '1.18': 'ESD shows the subject\'s relevance: climate, inequality, technology and misinformation',
    '1.19': 'enterprise education as a key component, cultivating an inquisitive and adaptable mindset',
    '1.20': 'enterprise competencies students develop through their studies',
    '1.21': 'ways to promote enterprise education: placements, simulations, assessment tasks',
    '1.22': 'graduate careers in policy, enterprise, institutions and beyond the discipline',
    '2.1': 'courses as structured pathways; each design sets out outcomes, formats and core content (S4)',
    '2.2': 'regular review of curriculum and resources with students as partners (S4)',
    '2.3': 'progression through the levels towards the threshold; readiness for postgraduate study (S4)',
    '2.4': 'joint, combined and major-minor routes meet the core outcomes (S4)',
    '2.5': 'exit awards, course length across the UK nations, part-time study',
    '2.6': 'flexible modes, formats and micro-credentials',
    '2.7': 'study with partner organisations through placements and internships',
    '2.8': 'partner organisations in curriculum, teaching and assessment',
    '2.9': 'courses offered with other higher education institutions, in the UK and abroad',
    '2.10': 'monitoring and periodic review, with the student voice (S4)',
    '2.11': 'external reviewers in periodic review (S4)',
    '2.12': 'external examiners and the statement\'s part in judging threshold standards',
    '3.1': 'courses build knowledge, understanding, skills and abilities',
    '3.2': 'conceptual and empirical study across a number of seventeen subfields (S4; SB3)',
    '3.3': 'a list of skills a course may develop (S4, outcome list in may)',
    '3.4': 'formats of learning and teaching, in person and online',
    '3.5': 'varied environments and methods support critical evaluation',
    '3.6': 'lectures, from traditional to interactive and flipped',
    '3.7': 'small-group learning and its activities',
    '3.8': 'small-group teaching and staff interaction for feedback and reflection',
    '3.9': 'learning in practice settings with external organisations',
    '3.10': 'independent learning and initiative',
    '3.11': 'access to a wide learning environment and many kinds of source (S4)',
    '3.12': 'assessment and feedback at the centre of course design (S4)',
    '3.13': 'diverse assessment so every student can show their abilities (S4)',
    '3.14': 'examples of assessment types and what each develops',
    '3.15': 'constructive feedback and plural approaches to contested questions (S4)',
    '3.16': 'formative and summative feedback and feedforward (S4)',
    '4.1': 'the standards are the minimum at the award of honours (the threshold, defined)',
    '4.2': 'most students exceed the threshold; Annex D for the classes (S4)',
    '4.3': 'threshold list: knowledge and understanding (S4)',
    '4.4': 'threshold list: discipline-specific skills (S4)',
    '4.5': 'threshold list: cognitive abilities and skills (S4)',
}
CTYPE = {
    '1.8': 'area', '1.9': 'area', '1.10': 'area', '3.2': 'area',
    '1.17': 'practice', '1.21': 'practice',
    '3.4': 'practice', '3.6': 'practice', '3.7': 'practice', '3.8': 'practice', '3.9': 'practice', '3.10': 'practice', '3.11': 'practice',
    '3.12': 'practice', '3.13': 'practice', '3.14': 'practice', '3.15': 'practice', '3.16': 'practice',
}
EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='section headings 1 to 4', heading='the four section heading lines', kind='other: headings, recorded in S3 as sections'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for SB6'),
    dict(number='6', heading='Membership of the Advisory Groups (2023, 2019, 2015, 2007, 2000)', kind='other: back matter, read for S7 (editions)'),
]

P = {}


def s(i, **k):
    P[i] = k


# ------------------------------------------------------------------ agent instruction builders (our words)
def aaw_rung(n, what, beside):
    return (f"Treat this as a threshold standard, the minimum a student should be able to show to be awarded honours in the subject ({what}). "
            f"It holds at FHEQ level 6 (FQHEIS level 10); cite it as {CITE}, para {n}. "
            f"Do not call it a regulatory requirement, a mark of a good degree or a master's expectation. "
            f"Set it beside {beside} and spine:6 in std:ref:uk-framework.")


def aad_rung(when, about, q):
    return (f"Raise this {when}. Speak plainly and in the second person to a student about {about}; with staff, frame it as the floor every graduate should clear. "
            f"Ask: {q} Avoid reading the issuer's list aloud, and never present this minimum as the mark of a good degree, since most students go beyond it.")


def aaw_may(n, what, beside):
    return (f"Treat this as one of the skills the statement says an honours course in the subject may develop ({what}); its force is may, so it is an option and not a condition of the award. "
            f"It sits at FHEQ level 6; cite it as {CITE}, para 3.3, {n}. Do not claim every graduate must show it. Set it beside {beside}.")


def aad_may(about, q):
    return ("Raise this when a student asks which wider skills the course will build, or a team decides which skills its modules develop. "
            f"Speak plainly and in the second person to a student about {about}, as something the course may offer; with staff, frame it as a design choice. "
            f"Ask: {q} Avoid presenting it as a minimum that every student must reach.")


def aaw_prov(n, kind, what, beside):
    return (f"Treat this as {kind} on the course or provider, not an outcome a student must show: {what}. "
            f"It concerns the honours degree at FHEQ level 6; cite it as {CITE}, para {n}. "
            f"Do not describe it as a regulatory requirement, since the statement is a sector reference point. Set it beside {beside}.")


def aad_prov(when, q):
    return (f"Raise this with a programme team or teacher when {when}. Frame it as what the course is expected to do, in the practitioner's terms. "
            f"Ask: {q} Do not put it to a student as a task of theirs: it is a duty on the course.")


SHOULD = "a 'should'"
WILL = "an expectation in 'will'"
REQ = "an obligation the issuer words with 'require' (recorded as must; Part E)"

# ------------------------------------------------------------------ paragraph statements (sections 1 to 4)
s('1.4', find=cut('This Subject Benchmark Statement provides both', 'more substantive content specialism.'),
  type='requirement', rung='none', force='must', level='fheq:7', appliesTo='students on taught postgraduate courses in the subject',
  addressee='learner', verbs=['require', 'demonstrate'], about='a higher level of learning on taught master\'s courses', domain='none', award=MAS,
  para=("The statement describes the discipline and guides the standards expected of honours graduates, chiefly for single honours and for joint honours "
        "where the subject is at least half the curriculum; taught postgraduate degrees at FHEQ level 7 and FQHEIS level 11 rest on the same principles "
        "but require students to show a higher level of learning, usually with more specialist content."),
  prac=("Taught master's courses in the subject share the honours principles, but their students must demonstrate a higher level of learning, "
        "usually with deeper specialist content, at FHEQ level 7 or FQHEIS level 11."),
  ben="If you go on to a taught master's in politics or international relations, you must show a higher level of learning than at honours, usually with more specialised content.",
  aaw=("Treat this as the statement's only word on master's study: taught postgraduate courses at FHEQ level 7 (FQHEIS level 11) must ask students for more than honours, "
       f"usually with more specialist content, though the statement sets no master's standards of its own. Cite it as {CITE}, para 1.4, and do not claim the threshold "
       "lists at 4.3 to 4.5 apply at master's level. For the level itself, set it beside the master's descriptor qaa/fheq-2024/4.17.b1 and spine:7 in std:ref:uk-framework."),
  aad=("Raise this when a student asks how a master's in the subject differs from their degree, or when a team drafts master's outcomes. Tell a student plainly that "
       "a master's builds on the same foundations but expects more depth and specialism; with staff, frame it as a level 7 design question. Ask: which of your honours "
       "outcomes would you now expect to see done with more depth or originality? Avoid implying the statement contains master's standards: it does not."))

s('1.16', find=cut('ESD offers an opportunity to reflect', 'diverse context of ESD.'),
  type='expectation', rung='none', force='should', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['integrated'], about='education for sustainable development across the whole course', domain='none', award=HON,
  para=("Education for sustainable development lets the discipline question its established approaches and should run through degree courses rather than "
        "sit only in specialist modules; a review of curriculum and teaching against the ESD guidance, and the UN SDGs as a frame, can help embed it."),
  prac=("Embed education for sustainable development across the whole course, not only in specialist options; reviewing curriculum and teaching against "
        "the ESD guidance, and using the SDGs as a frame, can show where it should sit."),
  ben=('n/a', 'a duty on the course to embed sustainability; the student meets its effect'),
  aaw=aaw_prov('1.16', SHOULD, 'education for sustainable development should be woven through the whole course, not left to specialist modules',
               'std:doc:qaa-advancehe-esd-2021-guidance and this subject\'s ESD theme in SB2 (theme:esd)'),
  aad=aad_prov('it reviews the curriculum or plans how sustainability appears from year to year',
               'in which core modules, outside any specialist option, does sustainability come up, and how?'))

s('2.1', find=cut('Politics and International Relations courses are designed to provide structured', 'attainment of course learning outcomes.'),
  type='expectation', rung='none', force='will', level='fheq:6', appliesTo='course design', addressee='provider',
  verbs=['outline'], about='course design: outcomes, formats and core content', domain='none', award=HON,
  para=("Courses offer structured pathways that build what an honours degree needs and that students can use for good in their own lives and communities; "
        "each course design will set out its learning outcomes and its forms of learning, teaching and assessment, with the content core to those outcomes."),
  prac="Each course's design will state its learning outcomes and its learning, teaching and assessment formats, naming the content that is core to meeting those outcomes.",
  ben=('n/a', 'a duty on course design'),
  aaw=aaw_prov('2.1', WILL, 'each course design will set out its learning outcomes, its learning, teaching and assessment formats and the content core to those outcomes',
               'the threshold lists at 4.3 to 4.5 and qaa/fheq-2024/4.15.i1'),
  aad=aad_prov('it drafts or revalidates a programme specification', 'can each core piece of content be traced to a stated course outcome?'))

s('2.2', find=cut('Politics and International Relations are dynamic areas of study', 'relating to higher education.'),
  type='requirement', rung='none', force='must', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['require', 'reviewed', 'updated'], about='regular review of curriculum and learning resources', domain='none', award=HON,
  para=("Because politics and the discipline both keep changing, curriculum and learning resources must be reviewed and updated regularly, with educators "
        "working with students as partners and co-producers and drawing on pedagogic research."),
  prac=("Review and update the curriculum and learning resources regularly as politics and the discipline change, involving students as partners and "
        "co-producers and drawing on pedagogic research in the subject and in higher education."),
  ben=('n/a', 'a duty on the course to keep its curriculum current'),
  aaw=aaw_prov('2.2', REQ, 'curriculum and learning resources are to be reviewed and updated regularly, with students as partners',
               '2.10 (monitoring and review) and 2.11 (external review)'),
  aad=aad_prov('it plans periodic review or a refresh of reading lists', 'when were the core reading lists last changed, and did students help decide what changed?'))

s('2.3', find=cut('Over the course of a degree with honours', 'achievement at undergraduate level.'),
  type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on the honours degree', addressee='learner',
  verbs=['progress', 'builds'], about='progression through the levels towards the threshold', domain='none', award=HON,
  para=("Over an honours degree (FHEQ level 6; FQHEIS level 10) students will progress level by level under each provider's rules, building towards the "
        "threshold subject-specific and generic skills, usually by gaining credit for all learning and assessment including practical parts; a second-class "
        "degree or above would normally equip a graduate for postgraduate study, though entry is for each provider to decide."),
  prac=("Students will move through the levels of study by the provider's rules, each level building towards the threshold skills in 4.3 to 4.5, usually by "
        "gaining credit for all learning and assessment; a second-class result or better is expected to prepare a graduate for postgraduate study, subject "
        "to each provider's entry rules."),
  ben=("You will move up through the levels of your degree under your university's rules, each year building towards the minimum skills you need by graduation; "
       "with a second-class degree or better you would usually be ready for postgraduate study, though each course sets its own entry rules."),
  aaw=("Treat this as the statement's account of progression: students will build, level by level, towards the threshold skills in 4.3 to 4.5, and a second-class "
       f"honours degree or above is expected to fit them for postgraduate study. It holds for honours at FHEQ level 6 (FQHEIS level 10); cite it as {CITE}, para 2.3. "
       "Do not claim it sets entry rules for postgraduate courses, which it leaves to each provider. Set it beside the level 5 and level 6 descriptors "
       "qaa/fheq-2024/4.12.b1 and qaa/fheq-2024/4.15.b1 and spine:6."),
  aad=("Raise this when a student asks how their years fit together or whether their result will let them go on to postgraduate study. Tell them plainly that each "
       "year builds towards the minimum skills for graduation and that a 2:2 or better usually opens that door, though each course sets its own entry rules. "
       "Ask: which skills from this year will you need next year? Avoid promising admission to any postgraduate course."))

s('2.4', find=cut('Undergraduates studying a combined', 'interdisciplinary study.'),
  type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on joint, combined or major-minor routes', addressee='learner',
  verbs=['achieve', 'add'], about='joint, combined and major-minor routes', domain='none', award=HON,
  para=("Students on combined, joint or major-minor routes will meet the core outcomes for the subject and add others from their other subjects, with further "
        "chances to work across disciplines."),
  prac=("On joint, combined or major-minor routes, students will still achieve the subject's core outcomes and will add outcomes from their other subjects, "
        "exploring where the disciplines meet."),
  ben=("If politics or international relations is one part of a joint or combined degree, you will still meet its core outcomes and gain others from your "
       "other subject, with chances to work across both."),
  aaw=("Treat this as an expectation for joint, combined and major-minor honours routes: students will meet the subject's core outcomes and add those of their "
       f"other subjects. Cite it as {CITE}, para 2.4, read with 1.4, which limits the statement to joint courses where the subject is at least half the curriculum. "
       "Do not claim the core outcomes are optional for joint students. Set it beside the threshold lists at 4.3 to 4.5, qaa/fheq-2024/4.15.b1 and spine:6."),
  aad=("Raise this when a joint or combined honours student asks whether the same subject outcomes apply to them as to single honours students. Answer plainly that "
       "the core subject outcomes still apply and their other subject adds more. Ask: where do your two subjects meet, and have you used that in your work? "
       "Avoid suggesting joint students need only part of the subject's outcomes."))

s('2.10', find=cut('Degree-awarding bodies, and their collaborative', 'inform future course planning.'),
  type='expectation', rung='none', force='will', level='none', appliesTo='degree-awarding bodies and their partners', addressee='provider',
  verbs=['form'], about='the student voice in course monitoring and review', domain='none', award=HON,
  para=("Degree-awarding bodies and their partners gather and analyse information and review courses periodically; the student voice will be part of this, "
        "alongside external reference points such as this statement."),
  prac=("Course monitoring and periodic review will take account of the student voice, alongside data and external reference points such as this statement, "
        "to keep provision in line with sector norms."),
  ben=('n/a', "a duty on the provider's review process"),
  aaw=aaw_prov('2.10', WILL, 'periodic course review will take account of the student voice', '2.2 and 2.11'),
  aad=aad_prov('it plans monitoring or periodic review', "how did students' views change anything in the last review?"))

s('2.11', find=cut('Externality is an essential component', 'appropriate for the subject.'),
  type='expectation', rung='none', force='will', level='none', appliesTo='providers', addressee='provider',
  verbs=['use', 'ensure'], about='external reviewers in periodic review', domain='none', award=HON,
  para=("Externality is essential to UK quality assurance: providers will use external reviewers in periodic review to gain an outside view of proposed changes "
        "and to make sure threshold standards are met and content suits the subject."),
  prac="Periodic review will draw on external reviewers to check proposed changes, confirm threshold standards are achieved and judge whether content is right for the subject.",
  ben=('n/a', 'a duty on the provider'),
  aaw=aaw_prov('2.11', WILL, 'providers will involve external reviewers in periodic review to secure threshold standards and suitable content',
               'the threshold lists at 4.3 to 4.5 and 2.12 (external examining)'),
  aad=aad_prov('it prepares for periodic review', 'which external reviewer will look at the threshold outcomes, and against what?'))

s('3.2', find=cut('Students taking Politics and International Relations courses will study', 'sustainability and environmental politics.'),
  type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['study', 'develop', 'demonstrate'], about='conceptual and empirical study across several subfields', domain='knowledge', award=HON,
  para=("Students will study the discipline's conceptual and empirical sides and, though scope varies by course, will typically develop and show knowledge "
        "and understanding of several of seventeen listed subfields, from area studies to environmental politics."),
  prac=("Every course will cover both conceptual and empirical aspects; students will typically build and demonstrate knowledge of a number of the listed "
        "subfields, not all of them, with the mix left to the course."),
  ben=("You will study both the ideas and the real-world evidence of politics, and you will usually come to know several of its main subfields well, such as "
       "comparative politics, political theory or international security."),
  aaw=("Treat this as an expectation of content: students will study conceptual and empirical aspects and will typically show knowledge of a number of the "
       f"seventeen subfields listed, not all of them. It holds for the honours degree at FHEQ level 6; cite it as {CITE}, para 3.2. Do not claim the list is a "
       "required core or that any one subfield is compulsory. Set it beside 4.3 (threshold knowledge and understanding) and qaa/fheq-2024/4.15.b1."),
  aad=("Raise this when a student asks what the subject covers or which options to choose, or when a team maps its modules. Tell a student plainly that courses "
       "differ and they will usually study several areas in depth rather than all of them. Ask: which subfields does your course give you, and which would you "
       "like more of? Avoid presenting the full list as something every student must cover."))

s('3.11', find=cut('Students should be provided with access', 'in different contexts.'),
  type='expectation', rung='none', force='should', level='none', appliesTo='courses and their students', addressee='both',
  verbs=['provided', 'exposed', 'engage', 'supported'], about='a wide learning environment and many kinds of source', domain='none', award=HON,
  para=("Students should have access to a broad learning environment, from published literature, software and computing to primary sources, archives and data, "
        "and should meet and engage with a wide range of sources, with support to judge their value and significance in context."),
  prac=("Give students access to a wide learning environment (literature, digital tools and software, primary sources, archives, statistical data and more), "
        "expose them to a broad range of sources and support them to evaluate those sources critically in context."),
  ben=("You should have access to a wide range of sources, from books and articles to archives, data and media, and get help to judge how useful and reliable "
       "each is in different settings."),
  aaw=("Treat this as a 'should' on the course, with a part for the student: provide a wide learning environment and a broad range of sources, and support "
       f"students to judge their value in context. Cite it as {CITE}, para 3.11; it is a sector reference point, not a regulatory rule. Do not present its list "
       "of materials as a required reading list. Set it beside 4.4.b5, 4.5.b4 and qaa/fheq-2024/4.15.b5."),
  aad=("Raise this when a student says they rely on one kind of source, or when a team reviews library and data provision. Put it to a student as the range of "
       "material they should be using and the support they can ask for; to staff, as what the course should provide. Ask: which kinds of source have you not yet "
       "used, such as archives, data or official documents? Avoid reading the list of materials aloud."))

s('3.12', find=cut('Assessment and feedback are central to successful', 'performance in subsequent tasks.'),
  type='expectation', rung='none', force='should', level='none', appliesTo='course assessment', addressee='provider',
  verbs=['aim', 'empower'], about='assessment that builds critical self-reflection', domain='none', award=HON,
  para=("Assessment and feedback are central to course design; assessments should aim to help students reflect critically on their learning and abilities, "
        "let them show their understanding and that they have met learning outcomes and can build skills for personal development, employability and citizenship."),
  prac=("Design assessment so that it aims to enable students to reflect critically on their learning and abilities, while letting them show they have met the "
        "course outcomes and building skills for employability and citizenship."),
  ben=('n/a', 'a duty on assessment design; the student-facing side is 4.5.b6'),
  aaw=aaw_prov('3.12', SHOULD, 'assessments should aim to help students reflect critically on their own learning and abilities',
               '4.5.b6 and qaa/fheq-2024/annex-d/transferable/r5/3rd'),
  aad=aad_prov('it designs or reviews an assessment strategy', 'which assessment in the course asks students to reflect on how they learned, not just what?'))

s('3.13', find=cut('In the discipline of Politics and International Relations, a variety', 'what they can do.'),
  type='expectation', rung='none', force='should', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['provide'], about='diverse assessment so every student can show their abilities', domain='none', award=HON,
  para=("Many kinds of assessment are used, and variety matters because it lets students show their full range of abilities; given students' varied "
        "backgrounds, courses should give every student chances to show what they have learned and can do."),
  prac="Use a varied range of assessment so that every student, whatever their educational background, has chances to show what they have learned and can do.",
  ben=('n/a', 'a duty on the course'),
  aaw=aaw_prov('3.13', SHOULD, 'courses should give all students, whatever their background, varied chances to show what they have learned',
               '3.14 (types of assessment) and theme:edi (1.13)'),
  aad=aad_prov('it reviews whether its assessment favours one kind of student', 'could a strong student who struggles with exams still show their ability somewhere in this course?'))

s('3.15', find=cut('Feedback is an essential part of assessment', 'peer and self-assessment.'),
  type='expectation', rung='none', force='should', level='none', appliesTo='courses and their teachers', addressee='provider',
  verbs=['receive', 'acknowledged', 'discussed'], about='constructive feedback and plural approaches to contested questions', domain='none', award=HON,
  para=("Feedback helps students judge their progress and how to improve; students should receive constructive feedback throughout, with attention to "
        "self-reflection and self-criticism, and because core concepts are contested, the range of legitimate approaches to a question should be acknowledged and discussed."),
  prac=("Give constructive feedback throughout the course that builds students' self-reflection and self-criticality, and acknowledge and discuss the range of "
        "legitimate approaches to a question, since the subject's core concepts are contested."),
  ben=('n/a', 'a duty on the course to give feedback; the student-facing side is 4.5.b6'),
  aaw=aaw_prov('3.15', SHOULD, 'students should get constructive feedback throughout, and markers should recognise the several legitimate approaches a contested question allows',
               '3.16 and 4.5.b6'),
  aad=aad_prov('markers or a team discuss feedback practice or how to mark contested questions',
               'does your feedback ever mark down a defensible approach just because it differs from the model answer?'))

s('3.16', find=cut('Feedback should be both formative', 'to help the student develop.'),
  type='expectation', rung='none', force='should', level='none', appliesTo='courses and their teachers', addressee='provider',
  verbs=['focus'], about='formative and summative feedback; feedforward', domain='none', award=HON,
  para=("Feedback should be both formative and summative and should focus on helping students see how to improve their work, for the task and for their wider "
        "skills; formative assessment and feedback work best early, during and after assessment."),
  prac="Provide formative as well as summative feedback, focused on feedforward: how students can improve, both on the task in hand and in their wider skills.",
  ben=('n/a', 'a duty on the course to give feedback'),
  aaw=aaw_prov('3.16', SHOULD, 'feedback should be formative as well as summative and look forward to how students can improve', '3.15 and 4.5.b6'),
  aad=aad_prov('it plans assessment timelines or feedback templates', 'where in each module does a student get feedback before the work that counts?'))

s('4.2', find=cut('Most students will perform significantly better', '2.2 and 3rd.'),
  type='expectation', rung='none', force='should', level='fheq:6', appliesTo='providers classifying honours degrees', addressee='provider',
  verbs=['refer'], about='performance above threshold and the classification descriptions', domain='none', award=HON,
  para=("Most students will do much better than the threshold; each provider sets its own way of evidencing this and should refer to Annex D, which describes "
        "the four honours classes (1st, 2.1, 2.2 and 3rd) for degrees at FHEQ level 6 and FQHEIS level 10."),
  prac="Expect most students to exceed the threshold; judge by how much using your own method, referring to Annex D's descriptions of the four classes of honours degree.",
  ben=('n/a', 'a duty on the provider in classifying degrees'),
  aaw=("Treat this as a 'should' on providers: when judging performance above the threshold, they should refer to Annex D, the degree classification "
       f"descriptions at FHEQ level 6 and FQHEIS level 10. Cite it as {CITE}, para 4.2, and do not claim the statement itself defines what earns a 2.1 or a first. "
       "Set it beside qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st and the bands in std:doc:qaa-fheq-2024-framework SL6."),
  aad=("Raise this when a team writes marking criteria above the pass, or a student asks what makes a better degree. Tell a student that the minimum lists "
       "describe a pass at honours and that most students do better, with the classes described elsewhere; with staff, point to Annex D. Ask: how do your "
       "marking criteria step up from the threshold to a first? Avoid presenting the threshold lists as the standard for a good degree."))

# ------------------------------------------------------------------ 3.3 skills a course may develop (lead-in: "may include the ability to")
W33 = 'the skills a course may develop'


def k33(b, verbs, about, domain, para, prac, ben, what, beside, q, **extra):
    s('3.3.b%d' % b, type='outcome', rung='none', force='may', forceFrom='3.3', level='fheq:6', appliesTo='students on honours courses in the subject',
      addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
      aaw=aaw_may('item b%d' % b, what, beside), aad=aad_may(about, q), **extra)


k33(1, ['collaborate', 'achieve'], 'collaborating towards common goals', 'generic-skill',
    'May include working with others towards shared goals, for instance through group work, projects and presentations.',
    'Courses may develop collaboration towards common goals, for example in group work, group projects and group presentations.',
    'Your course may help you learn to work with others towards shared goals, for example in group projects and presentations.',
    'working with others towards shared goals', '4.5.b3 (the threshold item on teamwork) and qaa/fheq-2024/annex-d/transferable/r2/3rd',
    'what has group work taught you about reaching a shared goal?')
k33(2, ['communicate'], 'communicating for context and audience', 'generic-skill',
    'May include communicating in formats suited to the context and to varied audiences.',
    'Courses may develop communication in formats that fit the context, for a range of audiences.',
    'Your course may help you communicate in ways that suit the setting and the audience.',
    'communicating in formats that fit context and audience', '4.5.b1 and qaa/fheq-2024/4.15.b8',
    'which formats have you used so far, and for whom?')
k33(3, ['construct', 'synthesising', 'exercising'], 'reasoned argument and critical judgement', 'generic-skill',
    'May include building a reasoned case that draws relevant information together and applies critical judgement.',
    'Courses may develop the building of reasoned arguments that synthesise relevant information and apply critical judgement.',
    'Your course may help you build a well-reasoned argument, pulling relevant information together and judging it critically.',
    'building a reasoned case with critical judgement', 'qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r2/3rd',
    'how do you decide what to leave out of an argument?')
k33(4, ['reflect'], 'reflecting on own learning', 'generic-skill',
    "May include critical reflection on one's own learning.",
    'Courses may develop students\' critical reflection on how they learn.',
    'Your course may help you think critically about how you learn.',
    'critical reflection on their own learning', '4.5.b6 and qaa/fheq-2024/annex-d/transferable/r5/3rd',
    'what have you changed about how you study since your first year?')
k33(5, ['identify', 'investigate', 'solve', 'thinking'], 'creative problem solving', 'generic-skill',
    'May include finding, exploring and solving problems through lateral and creative thinking, in practical and theoretical settings.',
    'Courses may develop problem identification, investigation and solution through lateral, creative thinking in practical and theoretical contexts.',
    'Your course may help you spot, explore and solve problems by thinking creatively, both in theory and in practice.',
    'finding and solving problems by lateral, creative thinking', 'qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r3/3rd',
    'can you describe a problem you solved by coming at it from an unexpected angle?')
k33(6, ['demonstrate'], 'appropriate behaviour and academic practice', 'generic-skill',
    'May include showing suitable conduct and sound academic practice.',
    'Courses may develop appropriate conduct and sound academic practice.',
    'Your course may help you behave appropriately and follow good academic practice.',
    'appropriate conduct and sound academic practice', 'qaa/fheq-2024/4.15.b9.1',
    "how do you make sure your use of other people's work is clear and honest?")
k33(7, ['evaluate', 'apply'], 'approaches to political data', 'subject-skill',
    'May include judging and using approaches to collecting, analysing and presenting political data.',
    'Courses may develop the evaluation and use of methods for gathering, analysing and presenting political data.',
    'Your course may help you weigh up and use ways of gathering, analysing and presenting political data.',
    'judging and using methods for political data', '4.4.b4, 4.5.b7 and qaa/fheq-2024/annex-d/practical/r4/3rd',
    'which way of presenting political data have you found most misleading, and why?')
k33(8, ['manage'], 'managing own learning and projects', 'generic-skill',
    "May include managing one's learning and projects effectively, on time and critically, alone and with others.",
    'Courses may develop effective, timely and critical management of learning and projects, individually and collectively.',
    'Your course may help you manage your own learning and projects well and on time, on your own and with others.',
    'managing their own learning and projects', '4.5.b2, 4.4.b7 and qaa/fheq-2024/4.15.b5',
    'how do you keep a long project on track?')
k33(9, ['negotiate', 'influence'], 'negotiating and influencing', 'generic-skill',
    'May include negotiating and influencing others.',
    'Courses may develop negotiation and the ability to influence.',
    'Your course may help you learn to negotiate and to persuade others.',
    'negotiation and influence', 'qaa/fheq-2024/4.15.b8 and 4.5.b1',
    "when have you changed someone's mind, and how?")
k33(10, ['organise', 'deploy'], 'organising evidence from varied sources', 'generic-skill',
    'May include organising and using evidence, data and information drawn from varied primary and secondary sources.',
    'Courses may develop the organisation and use of evidence, data and information from a range of primary and secondary sources.',
    'Your course may help you organise and use evidence, data and information from many kinds of source.',
    'organising and using evidence from varied sources', '4.5.b4 and qaa/fheq-2024/4.15.b5',
    'how do you keep track of evidence from very different sources?')
k33(11, ['understand', 'apply'], 'principles of ethical research', 'subject-skill',
    'May include understanding and applying the principles of ethical research.',
    'Courses may develop understanding and application of ethical research principles.',
    'Your course may help you understand and follow the principles of ethical research.',
    'ethical research principles', '4.4.b3 (the threshold item on research ethics)',
    'what ethical issue did your last piece of research raise?')
k33(12, ['understand', 'use'], 'using constructive feedback', 'generic-skill',
    'May include understanding and acting on constructive feedback.',
    'Courses may develop the ability to understand and act on constructive feedback.',
    'Your course may help you make sense of feedback and act on it.',
    'understanding and acting on feedback', '4.5.b6 and 3.15',
    'which piece of feedback has been most useful to you, and what did you do with it?')
k33(13, ['select', 'use'], 'communication and data tools', 'generic-skill',
    'May include choosing and using suitable aids and software for communication, information and data analysis.',
    'Courses may develop the selection and use of suitable communication, information and data-analysis tools and software.',
    'Your course may help you choose and use the right tools and software for communicating, handling information and analysing data.',
    'choosing and using tools and software', '4.5.b7 and qaa/fheq-2024/annex-d/transferable/r1/3rd',
    'which software do you use for data, and which would you like to learn?')
k33(14, ['work', 'engage'], 'working in diverse environments', 'generic-skill',
    'May include working and taking part in multicultural, diverse settings at home and abroad.',
    'Courses may develop the ability to work and engage in multicultural, diverse settings, in the UK and internationally.',
    'Your course may help you work and take part in diverse, multicultural settings, at home and internationally.',
    'working in diverse, multicultural settings', '4.5.b3 and theme:edi (1.11 to 1.13)',
    'when have you worked with people whose backgrounds differ from yours, and what did you learn?',
    find='work and engage in multicultural, diverse environments domestically and globally.')

# ------------------------------------------------------------------ the threshold rung: 4.3, 4.4, 4.5 ("students at the threshold level should be able to")
BL = 'To reach the threshold standard, '
WHEN = {
    '4.3': 'when a student asks what they should know and understand by graduation, or a team checks module outcomes against the minimum',
    '4.4': 'when a student plans a dissertation or research project, or a team maps its research-skills outcomes',
    '4.5': 'when a student asks which general skills they should leave with, or a team maps its transferable-skill outcomes',
}


def kr(lead, b, verbs, about, domain, para, prac, ben, beside, q, **extra):
    i = '%s.b%d' % (lead, b)
    s(i, type='threshold', rung='threshold', force='should', forceFrom=lead, level='fheq:6', appliesTo='honours graduates at the threshold',
      addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=BL + ben,
      aaw=aaw_rung('%s (item b%d)' % (lead, b), about, beside), aad=aad_rung(WHEN[lead], about, q), **extra)


# 4.3 knowledge and understanding (b2 to b5 are sub-items of b1; b7 to b11 of b6)
kr('4.3', 1, ['demonstrate', 'engage'], 'critical familiarity with the concept of power', 'understanding',
   'Should be able to show familiarity with power as a concept and engage with it critically, across the four aspects listed beneath this item.',
   ('At threshold, graduates should know the concept of power well and handle it critically, covering four aspects: contested knowledge; approaches '
    'to the discipline; its key concepts, theories and methods; and their strengths and weaknesses (4.3.b2 to b5).'),
   'you should know your way around the idea of power and be able to question how it is used and understood.',
   'qaa/fheq-2024/4.15.b1, qaa/fqheis-2024/4.16.b2 and qaa/fheq-2024/annex-d/knowledge/r2/3rd',
   'where in your modules have you had to argue about what power is, rather than just describe who holds it?')
kr('4.3', 2, [], 'contested knowledge and understanding', 'understanding',
   'As part of 4.3.b1: should be able to show that what counts as knowledge and understanding in the subject is open to dispute.',
   'At threshold, graduates should recognise that knowledge and understanding in the discipline are contested, and treat power as part of that contest.',
   'you should understand that what counts as knowledge in politics is itself argued over, and that power shapes those arguments.',
   'qaa/fheq-2024/4.15.b4 and qaa/fqheis-2024/4.16.b3',
   'can you give an example where two scholars disagree about the facts themselves, not only about what they mean?')
kr('4.3', 3, [], 'approaches to studying politics or international relations', 'knowledge',
   'As part of 4.3.b1: should know the main approaches to studying politics or international relations.',
   'At threshold, graduates should know the principal approaches by which politics or international relations is studied, and how each treats power.',
   'you should know the main ways scholars go about studying politics or international relations.',
   'qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r2/3rd',
   'which two approaches to the subject could you compare, and what does each notice about power?')
kr('4.3', 4, [], 'key concepts, theories and methods', 'knowledge',
   'As part of 4.3.b1: should know a range of the central concepts, theories and methods used in the discipline.',
   "At threshold, graduates should command a range of the discipline's central concepts, theories and methods, in politics or in international relations.",
   'you should know a good range of the main ideas, theories and research methods used in your subject.',
   'qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/knowledge/r2/3rd',
   'which concepts, theories and methods could you explain without notes, and which would you still need to look up?')
kr('4.3', 5, [], 'strengths and weaknesses of approaches', 'understanding',
   'As part of 4.3.b1: should be able to weigh what the approaches to the discipline do well and where they fall short.',
   "At threshold, graduates should judge the strengths and limitations of the discipline's approaches, not only describe them.",
   'you should be able to say what each approach to the subject does well and where it falls short.',
   'qaa/fheq-2024/4.15.b4, qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r2/3rd',
   'for an approach you use often, what can it not see?')
kr('4.3', 6, ['engage'], 'critical engagement with the discipline', 'understanding',
   'Should be able to engage critically with politics and international relations as fields, across the five aspects listed beneath this item.',
   ('At threshold, graduates should engage critically with the discipline, including its normative and positive foundations, its vocabulary, '
    'political and international systems, the contexts of political behaviour and the causes of political change (4.3.b7 to b11).'),
   'you should be able to think critically about politics and international relations as subjects, not only learn their content.',
   'qaa/fheq-2024/4.15.b7, qaa/fqheis-2024/4.16.b2 and qaa/fheq-2024/annex-d/cognitive/r2/3rd',
   'where have you questioned a claim made in the core reading, and on what grounds?')
kr('4.3', 7, [], 'normative and positive foundations of political ideas', 'knowledge',
   'As part of 4.3.b6: should be able to engage critically with both the value-based and the explanatory roots of political ideas.',
   'At threshold, graduates should engage critically with political ideas from both their normative (what ought to be) and positive (what is, and why) foundations.',
   'you should be able to question political ideas both as claims about what ought to be and as explanations of what happens.',
   'qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r2/3rd',
   'can you take one political idea and say what it claims ought to happen and what it claims does happen?')
kr('4.3', 8, [], 'the vocabulary of political debate', 'knowledge',
   'As part of 4.3.b6: should be able to use and question the language in which political debate is conducted.',
   'At threshold, graduates should handle the vocabulary of political debate critically, using its terms accurately and noticing how they are contested.',
   'you should be able to use the language of political argument accurately and notice when its terms are being stretched or contested.',
   'qaa/fheq-2024/annex-d/knowledge/r1/3rd and qaa/fheq-2024/4.15.b1',
   'which political terms do people use in different senses, and how do you handle that in your writing?')
kr('4.3', 9, [], 'how political and international systems are built and work', 'knowledge',
   'As part of 4.3.b6: should be able to engage critically with how different political and international systems are built and how they work.',
   'At threshold, graduates should analyse critically how political and international systems differ in structure and in operation.',
   'you should be able to explain and question how different political and international systems are set up and how they work in practice.',
   'qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1',
   'which two systems could you compare, and what difference does their design make?')
kr('4.3', 10, [], 'the contexts of political behaviour', 'knowledge',
   'As part of 4.3.b6: should be able to engage critically with the social, economic, historical and cultural settings in which people act politically.',
   'At threshold, graduates should place political behaviour in its wider settings (social, economic, historical, cultural) and reason critically about how these shape it.',
   'you should be able to explain how society, the economy, history and culture shape the way people behave politically.',
   'qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/3rd',
   'for a political event you know well, which context explains most, and which is easiest to overlook?')
kr('4.3', 11, [], 'explanations of political change', 'understanding',
   'As part of 4.3.b6: should be able to engage critically with explanations of why political change happens.',
   'At threshold, graduates should assess critically the factors offered to explain political change.',
   'you should be able to weigh up different explanations of why politics changes.',
   'qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b2',
   'what would you count as evidence that one factor, rather than another, drove a political change?')
kr('4.3', 12, ['apply'], 'applying concepts, theories and methods in political analysis', 'subject-skill',
   'Should be able to use a variety of concepts, theories and methods to analyse political ideas, actors, institutions and behaviour.',
   'At threshold, graduates should put concepts, theories and methods to work in analysing political ideas, actors, institutions and behaviour, choosing among them.',
   'you should be able to choose and use concepts, theories and methods to analyse political ideas, the people and bodies involved and how they behave.',
   'qaa/fheq-2024/4.15.b2, qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/annex-d/knowledge/r3/3rd',
   'for your last essay, which theory did the work, and why that one?')
kr('4.3', 13, ['examine', 'evaluate'], 'judging interpretations of political issues and events', 'understanding',
   'Should be able to scrutinise and judge competing readings of political issues and events.',
   'At threshold, graduates should examine and evaluate rival interpretations of political issues and events and reach a reasoned view.',
   'you should be able to look at different readings of a political issue or event and judge which holds up best.',
   'qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r2/3rd',
   'when two accounts of an event disagree, how do you decide which to trust?',
   find='examine and evaluate different interpretations of political issues and events.')

# 4.4 discipline-specific skills
kr('4.4', 1, ['identify'], 'choosing a research topic', 'subject-skill',
   'Should be able to pick a topic suitable for research.',
   'At threshold, graduates should be able to settle on a research topic that is workable and worth pursuing.',
   'you should be able to choose a topic that works for a piece of research.',
   'qaa/fheq-2024/4.15.b6, qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b5',
   'what makes your chosen topic researchable in the time and with the sources you have?')
kr('4.4', 2, ['develop', 'evaluate'], 'research questions and hypotheses', 'subject-skill',
   'Should be able to form research questions and hypotheses and judge their quality.',
   'At threshold, graduates should develop research questions and hypotheses and evaluate whether they are clear, answerable and worth testing.',
   'you should be able to write research questions and hypotheses and judge whether they are good ones.',
   'qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/knowledge/r3/3rd',
   'could someone else tell from your research question what evidence would answer it?')
kr('4.4', 3, ['assess', 'analyse'], 'the ethics of research and enquiry', 'subject-skill',
   'Should be able to judge and analyse the ethical consequences of research and enquiry.',
   'At threshold, graduates should weigh and analyse the ethical implications of their own research and enquiry, beyond completing an ethics form.',
   'you should be able to think through the ethical questions your research raises and deal with them.',
   'qaa/fheq-2024/annex-d/practical/r1/3rd and qaa/fheq-2024/4.15.b2',
   'who could be affected by your research, and how have you protected them?')
kr('4.4', 4, ['identify', 'interpret', 'apply'], 'methods of data collection and analysis', 'subject-skill',
   'Should be able to find, understand and use suitable methods for gathering and analysing qualitative or quantitative data, or both.',
   'At threshold, graduates should identify, interpret and apply methods of data collection and analysis fitted to the question, qualitative, quantitative or both.',
   'you should be able to choose, understand and use the right methods to collect and analyse data, whether numbers, words or both.',
   'qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r4/3rd',
   'why did you choose that method over the alternatives, and what would it miss?')
kr('4.4', 5, ['search', 'identify'], 'searching the literature', 'subject-skill',
   'Should be able to search systematically for the literature most relevant to a research topic, from books and reviews to papers and articles, and pick it out.',
   'At threshold, graduates should search the literature methodically and identify the most relevant books, reviews, papers and articles for a topic.',
   'you should be able to search methodically for the most useful books, reviews and articles on your topic.',
   'qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/cognitive/r1/3rd',
   'how would you show someone that you have not missed a key source on your topic?')
kr('4.4', 6, ['review', 'assess', 'engage'], 'critical review of the literature', 'subject-skill',
   "Should be able to review a topic's literature and assess it critically so as to take part in the field's debates, concepts and empirical findings.",
   "At threshold, graduates should read a topic's literature critically and use it to take part in the field's competing debates, concepts and empirical findings.",
   'you should be able to read critically what has been written on a topic and use it to join the debates in your field.',
   'qaa/fheq-2024/4.15.b3.2 and qaa/fheq-2024/annex-d/cognitive/r1/3rd',
   'where does your reading disagree with itself, and where do you stand?')
kr('4.4', 7, ['plan', 'execute', 'present'], 'an independent piece of work', 'subject-skill',
   'Should be able to plan, run and present a self-directed project that shows time management, problem solving, independence and sound interpretation and evaluation of evidence.',
   ('At threshold, graduates should plan, carry out and present a substantial piece of work of their own, showing that they manage time, solve problems, '
    'work on their own and weigh the quality of evidence.'),
   'you should be able to plan, carry out and present a project of your own, managing your time, solving problems as they come and judging how good your evidence is.',
   'qaa/fheq-2024/4.15.b6, qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r3/3rd',
   'what went wrong in your last independent project, and how did you deal with it?')
kr('4.4', 8, ['demonstrate', 'identify', 'apply'], 'theoretical and empirical perspectives', 'subject-skill',
   'Should be able to show awareness of relevant theoretical and empirical perspectives and be able to recognise and use them.',
   'At threshold, graduates should know which theoretical and empirical perspectives bear on a question and be able to pick them out and put them to use.',
   'you should know which theories and bodies of evidence matter for a question and be able to use them.',
   'qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b3.1',
   'for your current topic, which theoretical lens and which body of evidence are you drawing on?',
   find='demonstrate an awareness of relevant theoretical and empirical perspectives and the ability to identify and apply them.')

# 4.5 cognitive abilities and skills
kr('4.5', 1, ['communicate'], 'communicating in varied formats to varied audiences', 'generic-skill',
   'Should be able to communicate well in a range of formats and to different audiences.',
   'At threshold, graduates should communicate effectively in varied formats and adapt to different audiences.',
   'you should be able to get your point across well in different formats and to different kinds of audience.',
   'qaa/fheq-2024/4.15.b8, qaa/fqheis-2024/4.16.b7 and qaa/fheq-2024/annex-d/transferable/r1/3rd',
   'who outside your course have you had to explain political ideas to, and how did you change your approach?')
kr('4.5', 2, ['complete'], 'completing tasks efficiently', 'generic-skill',
   'Should be able to finish tasks efficiently.',
   'At threshold, graduates should complete tasks efficiently, meeting deadlines without loss of quality.',
   'you should be able to get tasks done efficiently.',
   'qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r3/3rd',
   'how do you plan your week when several deadlines fall together?')
kr('4.5', 3, ['work'], 'working independently and in a team', 'generic-skill',
   'Should be able to work both alone and as a member of a team.',
   'At threshold, graduates should work effectively on their own and within a team.',
   'you should be able to work well on your own and with others in a team.',
   'qaa/fheq-2024/annex-d/transferable/r2/3rd and qaa/fheq-2024/annex-d/transferable/r3/3rd',
   'what did you contribute to the last group task, and what did you do alone?')
kr('4.5', 4, ['evaluate', 'use', 'discuss', 'apply'], 'judging sources and using evidence', 'generic-skill',
   'Should be able to judge how accurate and reliable sources are and use that judgement to discuss and apply evidence suitably.',
   'At threshold, graduates should evaluate sources for accuracy and reliability and let that evaluation govern how they discuss and use evidence.',
   'you should be able to check how accurate and reliable a source is and use that check when you discuss and use evidence.',
   'qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r1/3rd',
   'how do you check a source you found on social media before you cite it?')
kr('4.5', 5, ['create', 'produce'], 'producing information and media innovatively', 'generic-skill',
   'Should be able to create and produce information and media in new and inventive ways.',
   'At threshold, graduates should create and produce information and media innovatively, in forms suited to the purpose.',
   'you should be able to make information and media of your own in fresh, inventive ways.',
   'qaa/fheq-2024/annex-d/cognitive/r4/3rd',
   'what have you made, beyond essays, that presented political ideas in a new way?')
kr('4.5', 6, ['recognise', 'reflect', 'analyse', 'improve'], 'using feedback to improve own work', 'generic-skill',
   'Should be able to take in and reflect on feedback so as to analyse their own work critically and improve it.',
   'At threshold, graduates should recognise and reflect on feedback and use it to analyse critically and improve their own work.',
   'you should be able to take feedback on board, think about it and use it to judge and improve your own work.',
   'qaa/fheq-2024/annex-d/transferable/r5/3rd and qaa/fheq-2024/annex-d/summary/r3/3rd',
   'what is one change you made to your work because of feedback, and did it help?')
kr('4.5', 7, ['interpret', 'analyse', 'apply', 'present'], 'working with numerical, textual and other data', 'generic-skill',
   'Should be able to interpret, analyse, apply and present data, whether numerical, textual or other.',
   'At threshold, graduates should interpret, analyse, apply and present data of several kinds: numerical, textual and others.',
   'you should be able to make sense of, analyse, use and present data, whether numbers, texts or other kinds.',
   'qaa/fheq-2024/annex-d/practical/r4/3rd and qaa/fheq-2024/annex-d/transferable/r1/3rd',
   'what kinds of data have you analysed so far, and which are you least sure of?')

GRADE = {}   # one rung only: no gradeOf links
TH = {'1.16': 'theme:esd'}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.3; 4.2'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.3; 4.2'),
            dict(id='fheq:7', role='cites', locator='D1, 1.4'),
            dict(id='fqheis:11', role='cites', locator='D1, 1.4'),
            dict(id='spine:6', role='refers', locator='std:ref:uk-framework R2 (inferred: honours at FHEQ 6 and SCQF 10)')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.3: "a degree with honours (FHEQ Level 6; FQHEIS Level 10)"; 4.2)'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 1.4: "Postgraduate taught degrees (FHEQ Level 7 and FQHEIS Level 11)")'),
                dict(**{'from': 'fheq:6'}, to='spine:6', relation='thresholdAt', basis='inferred from std:ref:uk-framework R2 (Part E)')])

S6 = [
    dict(id='theme:edi', role='carries', carriedIn=['1.11', '1.12', '1.13']),
    dict(id='theme:accessibility', role='carries', carriedIn=['1.13', '1.14']),
    dict(id='theme:esd', role='carries', carriedIn=['1.15', '1.16', '1.17', '1.18', '1.19', '3.2']),
    dict(id='theme:enterprise', role='carries', carriedIn=['1.19', '1.20', '1.21', '1.22', '3.12', '3.14']),
]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-politics-and-international-relations-2019-benchmarks (not held)',
         note='the back matter names the fourth edition (2019), revised by QAA for the 2018 Quality Code; earlier editions 2015, 2007 and 2000'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree classification descriptions for FHEQ level 6 and FQHEIS level 10 (4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 6 and 7 (1.4; 2.3; 4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 10 and 11 (1.4; 2.3; 4.2)'),
    dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note='definitions of sustainable development and ESD quoted (1.15); "the QAA guidance" (1.16); reference list'),
    dict(rel='cites', target='std:doc:qaa-enterprise-2018-guidance', note='reference list only'),
    dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance (not ingested)', note='front matter'),
    dict(rel='thresholdAt', target='std:ref:uk-framework, spine:6', note='inferred: the threshold lists sit at the honours step (Part E)'),
]

SB1 = [
    'The field studies power, governance, participation, decision-making, conflict and cooperation at every scale, from local to global (D1, 1.1, 1.3).',
    'Politics asks who gets what, when, how, why and where, around questions of power, justice, legitimacy, sovereignty and security; international relations adds a world split into many polities, states and the actors above, below and beyond them (D1, 1.8, 1.9).',
    'Its ways of knowing combine description, general explanation, normative theory and political philosophy, positive political theory and approaches that reject universal theories, such as historical and postmodern analysis (D1, 1.7).',
    'It uses a wide range of quantitative and qualitative methods and draws on cognate subjects (D1, 1.10).',
    'Its boundaries and names are contested and shifting, and it treats its own history (imperial, colonial, patriarchal and other) as an object of critical study (D1, 1.3, 1.6, 1.11, 1.12).',
    'It prepares graduates for careers, active citizenship and leading change, in policy, enterprise, public institutions and beyond (D1, 1.1, 1.22).',
]

SB2 = [
    dict(theme='theme:edi',
         inThisSubject="the subject's own matter is power, privilege and exclusion; students examine how the discipline was shaped by and helped shape colonialism, patriarchy and racism and read marginalised scholars; course teams build inclusive communities and close gaps in access, attainment and awarding (D1, 1.11 to 1.13)",
         statements=['3.3.b14']),
    dict(theme='theme:accessibility',
         inThisSubject='courses designed to be accessible to all, attainment and experience gaps reduced, reasonable adjustments in place (D1, 1.13, 1.14)',
         statements=[]),
    dict(theme='theme:esd',
         inThisSubject='headed Sustainability in the text: integral to how the subject studies an interconnected world, quoting the ESD guidance, to run through the whole course and framed by the SDGs; climate breakdown, inequality, misinformation; sustainability and environmental politics as a subfield (D1, 1.15 to 1.18, 3.2)',
         statements=['1.16', '3.2']),
    dict(theme='theme:enterprise',
         inThisSubject='a key component of the degree: an inquisitive, adaptable mindset and competencies such as negotiation, influence and evidence-based problem solving, built through placements, simulations and authentic assessment such as policy briefs (D1, 1.19 to 1.22, 3.14)',
         statements=['3.12']),
]

SB3 = dict(
    areas=[dict(component='1.8', gloss='politics: government and society, the allocation of values and resources'),
           dict(component='1.9', gloss='international relations: states and actors beyond them, governance without government'),
           dict(component='1.10', gloss='research strategies and methods, quantitative and qualitative'),
           dict(component='3.2', gloss='seventeen subfields, from area studies and comparative politics to political economy, political theory and environmental politics; courses cover a number of them')],
    practices=[dict(component='1.17', kind='teaching', gloss='methods for delivering ESD: problem-based learning, simulations, crisis games, field trips, placements'),
               dict(component='1.21', kind='learning', gloss='enterprise education through placements, work-like learning, role-play and group projects'),
               dict(component='3.4', kind='teaching', gloss='seminars, workshops, computer labs; in person, online or both'),
               dict(component='3.6', kind='teaching', gloss='lectures, traditional, interactive or flipped'),
               dict(component='3.7', kind='learning', gloss='small-group work: debates, role-play, crisis games, peer teaching'),
               dict(component='3.8', kind='teaching', gloss='small-group teaching and staff contact for feedback'),
               dict(component='3.9', kind='learning', gloss='learning in practice settings with external organisations'),
               dict(component='3.10', kind='learning', gloss='independent learning, directed, guided and extracurricular'),
               dict(component='3.11', kind='learning', gloss='a wide learning environment: literature, software, archives, data, media'),
               dict(component='3.12', kind='assessment', gloss='assessment at the centre of design, for reflection and to show outcomes met'),
               dict(component='3.13', kind='assessment', gloss='a diverse range of assessment for every student'),
               dict(component='3.14', kind='assessment', gloss='essays and exams, authentic tasks such as briefing papers and simulations, research projects, data reports, presentations, reflective reports'),
               dict(component='3.15', kind='assessment', gloss='constructive feedback; plural approaches to contested questions'),
               dict(component='3.16', kind='assessment', gloss='formative and summative feedback, feedforward')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.3; 4.4; 4.5', award=HON, items=28)],
    rungBases=('Threshold only. 4.1 defines the standards as the minimum a student will have shown at the award of honours; 4.2 says most students do '
               'significantly better and hands the classes above the threshold to Annex D. No typical or excellent lists: 4.3 (knowledge and understanding, '
               '13 items, two of them headings of indented sub-lists), 4.4 (discipline-specific skills, 8) and 4.5 (cognitive abilities and skills, 7), '
               'each with the lead-in "students at the threshold level should be able to".'),
    outcomeLists=[dict(leadIn='3.3', gloss='skills a course may develop (force may)', items=14, award=[HON])],
    outcomes=[])

SB4A_FULL = []

SB5 = [
    dict(body='professional, statutory and regulatory bodies (PSRBs), none named',
         says='the statement supports PSRBs with the academic standards expected of students, and providers may weigh PSRB requirements as further reference points; it names no PSRB for the subject (D1, front matter)',
         requirements='not-applicable: no body named (Part E)'),
    dict(body='Office for Students',
         says="in England the statement is not a sector-recognised standard under the OfS regulatory framework (D1, front matter)",
         requirements='not yet ingested (Part E)'),
]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion (EDI)', carriedIn=['1.11', '1.12', '1.13'], statements=['3.3.b14']),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['1.13', '1.14'], statements=[]),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.15', '1.16', '1.17', '1.18', '1.19', '3.2'], statements=['1.16', '3.2']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)',
                 carriedIn=['1.19', '1.20', '1.21', '1.22', '3.12', '3.14'], statements=['3.12'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['1.4', '2.3', '4.2']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['1.4', '2.3', '4.2'])],
    bodies=[dict(body='PSRBs (generic, none named)', citedIn=['front matter']),
            dict(body='Office for Students', citedIn=['front matter'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees',
             citedIn=['4.2'], role='the four honours classes above the threshold'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named="QAA and Advance HE's Education for Sustainable Development Guidance, 2021",
             citedIn=['1.15', '1.16', 'back matter: references'], role='definitions of sustainable development and ESD; curriculum review'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='QAA (2018) Enterprise and Entrepreneurship Education',
             citedIn=['back matter: references'], role='further reading for the enterprise theme'),
        dict(document='QAA Quality Code, Advice and Guidance (not yet ingested: Part E)', named='Advice and Guidance to support the Quality Code',
             citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
        dict(document="QAA Glossary (not ingested)", named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='UN Sustainable Development Goals (external)', named='The United Nations Sustainable Development Goals (SDGs)',
             citedIn=['1.16', 'back matter: references'], role='a frame for the curriculum under ESD'),
    ])

B1 = [
    dict(slug='threshold-standard', definition='the least a student will have shown when awarded the honours degree (D1, 4.1)',
         beneficiaryDefinition='the minimum you need to show to be awarded your degree', scopeNote='the only rung stated; most students go beyond it (4.2)',
         category='unknown', practices=['education']),
    dict(slug='education-for-sustainable-development', definition='building curriculum structures and subject content that support and enact sustainable development, as the ESD guidance defines it (D1, 1.15)',
         beneficiaryDefinition='learning that helps you understand and act on sustainability through your subject', scopeNote='abbreviated ESD; quoted from QAA and Advance HE 2021',
         category='unknown', practices=['education']),
    dict(slug='enterprise-and-entrepreneurship-education', definition='education that builds the behaviours, attributes and competencies for active, enterprising citizenship and graduate careers (D1, 1.19)',
         beneficiaryDefinition='learning that builds the mindset and skills to make things happen in work and society', scopeNote='abbreviated EED',
         category='unknown', practices=['education']),
    dict(slug='feedforward', definition='feedback aimed at how a student can improve future work, on the task and in wider skills (D1, 3.16)',
         beneficiaryDefinition='feedback that tells you how to do better next time', scopeNote='set beside formative and summative feedback',
         category='unknown', practices=['education']),
    dict(slug='anarchy-international', definition='in international relations, the absence of a government over states at international or global level (D1, 1.9)',
         beneficiaryDefinition='the idea that no world government sits above states', scopeNote='a disciplinary term, not disorder',
         category='unknown', practices=['politics']),
    dict(slug='positive-political-theory', definition='explanatory theory of the general mechanisms that steer how individuals and institutions behave as they allocate values and resources (D1, 1.7)',
         beneficiaryDefinition='theory that explains how politics works, rather than how it ought to', scopeNote='also called explanatory political theory; contrasted with normative theory',
         category='unknown', practices=['politics']),
    dict(slug='normative-theory', definition='the study of the political values of society and the international order, historically and analytically (D1, 1.7)',
         beneficiaryDefinition='theory about how politics ought to be', scopeNote='with political philosophy', category='unknown', practices=['politics']),
]
B2A = [
    dict(concept='threshold-standard', form='minimum threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='education-for-sustainable-development', form='Education for Sustainable Development', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='education-for-sustainable-development', form='ESD', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
    dict(concept='enterprise-and-entrepreneurship-education', form='Enterprise and entrepreneurship education', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='enterprise-and-entrepreneurship-education', form='EED', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
    dict(concept='feedforward', form='feedforward', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='anarchy-international', form='anarchy', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
    dict(concept='positive-political-theory', form='Positive political theory', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
    dict(concept='positive-political-theory', form='explanatory political theory', lang='en', partOfSpeech='noun-phrase', termStatus='admitted', register='discipline-specific'),
    dict(concept='normative-theory', form='Normative theory', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
]
B4 = [dict(rel='contrasts-with', **{'from': 'positive-political-theory'}, to='normative-theory', note='1.7 sets them side by side')]
B5 = []
D3 = [dict(citation='QAA, Subject Benchmark Statement: Politics and International Relations, fourth edition (2019)', settles=['S7', 'S8'],
           asked='2026-10-03', state='wanted')]

E = [
    'SB4, pattern: threshold only, no typical or excellent lists (unlike Psychology); the classes above the threshold are left to Annex D (4.2). SB4 `outcomes` is empty since no outcome can be traced across rungs.',
    'SB4, pattern: three threshold lists (4.3, 4.4, 4.5) under one lead-in wording, "students at the threshold level should be able to", with sub-headings Knowledge and understanding, Discipline-specific skills, Cognitive abilities and skills. Force recorded as the lead-in\'s own word, should (Psychology: will); 4.1 frames the lists as the minimum for the award.',
    'S4, pattern: 4.3 nests two indented sub-lists (b2 to b5 under b1; b7 to b11 under b6). The skeleton\'s flat ids are kept, one record per item; each sub-item is read with its parent\'s verb ("demonstrate a familiarity and engage critically with", "engage critically with") and carries no verb of its own, so its `verbs` is empty. For P3: whether sub-items should take ids such as 4.3.b1.1.',
    'S3, skeleton cuts corrected: 4.3.b13, 4.4.b8 and 3.3.b14 ran on into the next heading ("Discipline-specific skills", "Cognitive abilities and skills", "Learning and teaching"); each is re-cut with `find`. Paragraph statements are cut without their paragraph number and without trailing headings (1.4, 2.2, 3.11, 4.2 ran on into a heading).',
    'S4, domain: 4.3.b12 (apply concepts, theories and methods) is recorded as subject-skill though the issuer lists it under Knowledge and understanding; 4.5 is headed "Cognitive abilities and skills" but its items are recorded as generic-skill, the issuer\'s own split (2.3: "subject-specific and generic skills"). For P3.',
    'S4, outcome list 3.3: "may include the ability to", a list of skills a course may develop; taken as 14 outcome records with force may, not as requirements. For Abbott: whether a may-list counts as a standard under D-std-0002 (a).',
    'S4, 3.2: the subfield list is taken as one statement (students "will typically develop and demonstrate" knowledge of "a number of" the subfields); its 17 items are not cut as statements, since none is required on its own, and are read as an SB3 area.',
    'S4, force outside the five: "require" in 1.4 (postgraduate taught degrees "require students to demonstrate higher levels of learning") and 2.2 (changes "require that curriculum and learning resources are regularly reviewed") recorded as must. For Abbott.',
    'S4, "requires" in 1.12 and 1.13 ("This requires engagement with ...", "This requires working in partnership ...") states what an aim entails, not a duty: not taken as statements. For Abbott.',
    'S4, "need" in 1.18 ("Students need the skillsets to decode ...") and "essential" in 2.11 (taken through its "will") and 3.8: obliging words outside the five; 1.18 and 3.8 not taken as statements. For Abbott.',
    'S4, plain-present provider norms not taken as statements (template open point 5): 1.13 and 1.14 ("Courses are designed ...", "Course teams put in place additional reasonable adjustments"), 2.6, 3.1, 3.10.',
    'S4, predictive "will" not taken: 2.7 ("will be defined by providers"), 2.12 ("external examiners will be asked"), 3.4 ("will develop over time"), 3.9 ("will be most beneficial"), 4.1 (the threshold defined; recorded in SB4 rungBases).',
    'S4, master\'s: the statement sets no master\'s standards; 1.4 alone names taught postgraduate degrees (FHEQ 7, FQHEIS 11), recorded as one requirement with award master\'s. awardsCovered and levelsCovered keep honours only (fheq:6, fqheis:10); fheq:7 and fqheis:11 are in S5 as cited.',
    'S4a, 3.11: addressee both (a provision duty with a part for the student, "engage with a wide range of sources"); it keeps a student version.',
    'S2, codes: "Government" (1.6) has no HECoS term; "Legislative Studies" is placed at 100610 UK government/parliamentary studies, inferred, and 100610 enters front matter as inferred. "Political Studies" and "Political Science" are placed at 100491 politics. Peace and War Studies, International Development and Legislative Studies are titles the statement says "may also include" the subject, not titles it covers.',
    'S2, codes: CAH15-03-01 and CAH15-03 (politics) recorded as stated, by name; CAH15 (social sciences) not entered.',
    'S5, S7: the crosswalk fheq:6 to spine:6 and the relation thresholdAt spine:6 are inferred from std:ref:uk-framework R2; the issuer states only FHEQ 6 with FQHEIS 10 and FHEQ 7 with FQHEIS 11.',
    'SB5: no PSRB is named for the subject; PSRBs appear only generically in the front matter. The Office for Students is named once in the front matter; its framework is not ingested.',
    'SB6: the skeleton\'s cross-cutting hits were one paragraph early (it read each theme heading, which sits at the end of the paragraph before, as part of that paragraph: 1.10 for EDI, 1.13 for accessibility, 1.14 for sustainability, 1.18 for enterprise, 2.6 for PSRBs); corrected from the held text. CQFW is not cited.',
    'SB6, themes: 1.19 names "ethical and sustainable thinking" inside the enterprise theme and 3.2 lists "sustainability and environmental politics"; both are tagged to theme:esd. 3.12 ("employability and citizenship") and 3.14 (assessment "aimed at enhancing their employability") are tagged to theme:enterprise. 3.3.b14 (diverse environments) is listed under theme:edi in SB2 and SB6 though its paragraph is not a theme paragraph (TH left untagged).',
    'S1, licence: the text gives a copyright notice and no re-use terms; QAA\'s terms for holding and chunking are to check.',
    'S7, S8: the fourth edition (2019) is named in the back matter as revised to align with the 2018 Quality Code; it is not held (D3).',
    'S9: not researched in P1.',
    'Pattern: no generative AI section; no "very good" rung; no master\'s column or list; no rung tables.',
]
