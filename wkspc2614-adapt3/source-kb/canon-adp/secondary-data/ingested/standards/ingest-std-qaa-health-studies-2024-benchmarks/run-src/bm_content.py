# Judgement for run 0109, QAA Subject Benchmark Statement: Health Studies (April 2024). std run agent.
# Brief: tools/BM-BRIEF.md 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft.
# Keys are S4 ids under qaa/health-studies-2024/. Our words everywhere except `source`, which the builder takes from each span.

HON = "bachelor's with honours"
MA = "master's"
SLUG_TITLE = 'Health Studies Subject Benchmark Statement'


def cite(n):
    return f'QAA, 2024, {SLUG_TITLE}, para {n}'


def num(i):
    """the issuer's paragraph and our item number, for citations"""
    if '.b' in i:
        base, k = i.split('.b')
        return f'{base} (item {k})'
    return i


META = dict(
    run='0109', p1='2026-10-03 17:33',
    title='Subject Benchmark Statement Health Studies',
    heading='Subject Benchmark Statement: Health Studies (QAA, April 2024)',
    edition='April 2024 (fifth edition)', published='2024-04',
    status='current',
    supersedes='Subject Benchmark Statement: Health Studies, fourth edition (2019), as the membership section names it',
    subjects=[
        dict(scheme='hecos', code='100473', label='health studies', basis='stated'),
        dict(scheme='cah', code='CAH15-04-03', label='health studies', basis='stated'),
        dict(scheme='cah', code='CAH15-04', label='health and social care', basis='stated'),
        dict(scheme='cah', code='CAH15', label='social sciences', basis='stated'),
        dict(scheme='hecos', code='100476', label='health and social care', basis='inferred'),
    ],
    awards=[HON, MA],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements; Health Studies fifth edition (April 2024), in the revision that adds the cross-cutting themes',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("QAA's UK reference point for what a graduate in Health Studies should know, understand and be able to do at the end of "
                     "an honours degree or a master's degree. Its standards are threshold lists only: subject knowledge and generic skills for "
                     "honours, subject knowledge for master's and a list of what typical master's holders can do. Reach for it when designing, "
                     "approving or reviewing a health studies course or writing its outcomes. It is not a curriculum, not a professional body's "
                     "accreditation standard and not a regulatory requirement in England."),
    summary=("Published by QAA in April 2024 as the fifth edition, the statement describes the subject's context and purposes, its "
             "distinctive features (design, progression, flexibility, partnership, monitoring and review), its content, teaching, "
             "assessment and supervision, then benchmark standards at the threshold for bachelor's degrees with honours (FHEQ level 6, "
             "FQHEIS level 10) and master's degrees (FHEQ level 7, FQHEIS level 11). It states no typical or excellent rung for honours "
             "and points to Annex D of the Frameworks for achievement above the threshold; the master's generic skills are led in with "
             "'Typically'. It carries the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability, "
             "with the eight UNESCO competencies; enterprise and entrepreneurship education) and a passage on generative AI, and names "
             "PSRBs in general and four health bodies a graduate might join."),
    authority=("reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised "
               "standard under the OfS framework; a key reference point in Wales and Scotland; part of quality requirements in Northern "
               "Ireland (D1, front matter: Relationship to legislation)"),
)

S2 = dict(
    governs=("what a Health Studies graduate can be expected to know, do and understand at the end of an honours degree or a master's "
             "degree, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 4.1)"),
    awards=["bachelor's degrees with honours", "master's degrees", "integrated master's (described, 2.15)",
            "postgraduate certificates and diplomas (reference point only, 4.6)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    statedScope='"The term Health Studies throughout this document includes physical and mental health, well-being, and the study of ill health (illness) and disease." (D1, 1.2)',
    statedSubjects=[
        dict(name='Health Studies', locator='(D1, title; 1.1; 1.2)', kind='subject',
             codes=[dict(scheme='hecos', code='100473', label='health studies'), dict(scheme='cah', code='CAH15-04-03', label='health studies')]),
        dict(name='multidisciplinary or joint courses of study, such as Health Studies with exercise or physical activity', locator='(D1, 1.8)',
             kind='programme title', codes=[dict(scheme='hecos', code='100473', label='health studies')]),
        dict(name='combined or joint degree', locator='(D1, 2.13)', kind='programme title',
             codes=[dict(scheme='hecos', code='100473', label='health studies')]),
        dict(name="Integrated master's degrees", locator='(D1, 2.15)', kind='programme title',
             codes=[dict(scheme='hecos', code='100473', label='health studies')]),
        dict(name='Apprenticeship degrees', locator='(D1, 2.22)', kind='programme title',
             codes=[dict(scheme='hecos', code='100473', label='health studies')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Health Studies degree', '2': 'Distinctive features of the Health Studies degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.8', 'Context and purposes of a Health Studies degree'),
       ('1.9', '1.16', 'Purposes and characteristics of a Health Studies degree'),
       ('1.17', '1.23', 'Equality, diversity and inclusion'),
       ('1.24', '1.26', 'Accessibility'),
       ('1.27', '1.30', 'Sustainability'),
       ('1.31', '1.32', 'Developing sustainable development competencies'),
       ('1.33', '1.34', 'Developing learning environments to promote sustainable development'),
       ('1.35', '1.49', 'Enterprise and entrepreneurship education'),
       ('2.1', '2.9', 'Design'), ('2.10', '2.15', 'Progression'), ('2.16', '2.18', 'Flexibility'),
       ('2.19', '2.22', 'Partnership'), ('2.23', '2.30', 'Monitoring and review'),
       ('3.1', '3.2', 'Content'), ('3.3', '3.6', 'Teaching and learning'), ('3.7', '3.10', 'Assessment'),
       ('3.11', '3.12', 'Supervision'),
       ('4.1', '4.3', 'Introduction'),
       ('4.4', '4.4', 'Threshold level: Subject knowledge, understanding and skills'),
       ('4.5', '4.5', 'Threshold level: Generic skills'),
       ('4.6', '4.6', "Benchmark standards for master's degrees"),
       ('4.7', '4.7', "Benchmark standards for master's degrees: Subject knowledge, understanding and skills"),
       ('4.8', '4.8', "Benchmark standards for master's degrees: Generic skills")]

G = {
    '1.1': 'the subject spans daily life across the life-course and many communities',
    '1.2': 'a broad field: physical and mental health, illness, care; wide employment',
    '1.3': 'it draws on many disciplines and keeps growing',
    '1.4': 'what shapes health, from policy to personal experience',
    '1.5': 'aim: critical study of health, its education and promotion; integrated care',
    '1.6': 'local to global contexts; research across disciplines; independent learners',
    '1.7': 'many titles and pathways; content from conceptual to vocational',
    '1.8': 'use beside other statements for joint courses; contrasting views',
    '1.9': 'meanings of health; no agreed definition; not the study of illness',
    '1.10': 'common themes: health as human experience; reflective, critical evaluation',
    '1.11': 'aim: students as agents of change',
    '1.12': 'research-based courses; critical reflection; research ethics',
    '1.13': 'stakeholders in course work; employability skills',
    '1.14': 'choosing a mix of disciplines; experience of care sectors',
    '1.15': 'courses with a professional focus; working with professions and users',
    '1.16': 'the disciplines and subject areas it draws on',
    '1.17': 'EDI: identity characteristics and intersectionality, embedded in the subject',
    '1.18': 'an inclusive learning community; a proactive approach to EDI',
    '1.19': 'why it is taught: EDI, inequality and the SDGs',
    '1.20': 'what is taught: organisations and EDI; the legal duty; diverse content',
    '1.21': 'how it is taught: inclusive design and modes of study',
    '1.22': 'examples of EDI in practice',
    '1.23': 'EDI as continuing review with students',
    '1.24': 'accessibility of every course requirement and what it may cover',
    '1.25': 'designing out barriers in advance',
    '1.26': 'equal access to workplace and international learning; digital access',
    '1.27': 'sustainability and planetary health; ESD defined; the SDGs',
    '1.28': 'ESD and the link between health, equality and environment',
    '1.29': 'weighing sustainability values; graduates as agents of change',
    '1.30': 'the person in context; critique of professional systems',
    '1.31': 'the eight UNESCO sustainability competencies',
    '1.32': 'competencies built into curricula',
    '1.33': 'facilities for self-directed adult learners',
    '1.34': 'teaching methods for ESD; authentic, interdisciplinary learning',
    '1.35': 'EEE and careers; placements and employer links',
    '1.36': 'EEE beyond employment',
    '1.37': 'knowing and showing the worth of one\'s skills',
    '1.38': 'what an entrepreneurial mindset in health means',
    '1.39': 'EEE for an ethical career, employed or self-employed',
    '1.40': 'enterprising behaviours',
    '1.41': 'enterprising attributes',
    '1.42': 'competencies for employed or self-employed practice',
    '1.43': 'ethical digital competence',
    '1.44': 'professional skills across the curriculum; dedicated modules',
    '1.45': 'external speakers and practitioners',
    '1.46': 'assignments that build business skills',
    '1.47': 'work with placement providers and employers',
    '1.48': 'placements as a bridge to an enterprising mindset',
    '1.49': 'career pathways and confidence',
    '2.1': 'multidisciplinary course design; other statements may apply',
    '2.2': 'focus varies; place health in context; partnerships in design',
    '2.3': 'design resting on frameworks and standards',
    '2.4': 'EDI throughout the experience; further considerations',
    '2.5': 'diverse patients\' needs; decolonising the curriculum',
    '2.6': 'plural ways of knowing, cultural safety, global health',
    '2.7': 'ESD in curriculum design',
    '2.8': 'employability and enterprise in design; placements',
    '2.9': 'registers and professional bodies graduates may join',
    '2.10': 'progression through the honours levels',
    '2.11': 'from structured study to autonomy; progression strategies',
    '2.12': 'readiness for postgraduate study',
    '2.13': 'joint and combined degrees',
    '2.14': 'length of study, early exits and part-time routes',
    '2.15': "integrated master's degrees",
    '2.16': 'flexible learning and delivery',
    '2.17': 'flexible formats, modes and entry points',
    '2.18': 'flexible design and review',
    '2.19': 'stakeholders as partners and what partnership brings',
    '2.20': 'aims for stakeholder involvement; regulatory alignment',
    '2.21': 'employer engagement and work-related learning',
    '2.22': 'apprenticeship degrees',
    '2.23': 'routine monitoring and periodic review',
    '2.24': 'external reviewers and threshold standards',
    '2.25': 'external examiners',
    '2.26': 'PSRB accreditation',
    '2.27': 'external reference points; uses of monitoring',
    '2.28': 'what monitoring and review support',
    '2.29': 'stakeholders in quality monitoring',
    '2.30': 'advisory boards and employer panels',
    '3.1': 'content and delivery for reflective, critical study',
    '3.2': 'flexible settings; specialising in a broad field',
    '3.3': 'blended, inclusive teaching strategies',
    '3.4': 'critical evaluation to build problem-solving and creativity',
    '3.5': 'scheduled activities and learning approaches',
    '3.6': 'the list does not prescribe',
    '3.7': 'assessment strategy, adjustments and generative AI',
    '3.8': 'assessment methods',
    '3.9': 'feedback: qualities, timing, feed-in and feed-forward',
    '3.10': 'what feedback should do',
    '3.11': 'the role of supervision',
    '3.12': 'what supervision needs',
    '4.1': "the standards are minimum thresholds for honours and master's",
    '4.2': 'most go beyond the threshold; Annex D for classes',
    '4.3': 'levels 6 and 7 thresholds as the minimum for an award',
    '4.4': 'threshold subject knowledge, understanding and skills (honours)',
    '4.5': 'threshold generic skills (honours)',
    '4.6': "master's standards as a level 7 reference point",
    '4.7': "master's subject knowledge",
    '4.8': "master's generic skills of typical holders",
}

CTYPE = {'1.10': 'area', '1.16': 'area', '3.1': 'area', '3.2': 'area',
         '1.34': 'practice', '3.3': 'practice', '3.5': 'practice', '3.7': 'practice', '3.8': 'practice',
         '3.9': 'practice', '3.10': 'practice', '3.11': 'practice', '3.12': 'practice'}

EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and S7'),
    dict(number='section headings 1 to 4', heading='section heading lines', kind='other: not document substance'),
    dict(number='5', heading='List of references and further resources', kind='other: bibliography, read for S7 and D3'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: names, read for supersedes and S8 only'),
]

P = {}


def s(i, **k):
    P[i] = k


# ------------------------------------------------------------------ agent-instruction builders (our words)
FORCE_WORDS = {
    'must': "stated with 'must', the statement's firmest word",
    'should': "stated with 'should': a firm recommendation that leaves room for the provider's judgement",
    'will': "stated with 'will': what the subject community expects to happen",
}


def pv_aaw(i, force, beside, extra=''):
    return (f"Describe this as a duty on the course team or provider, {FORCE_WORDS[force]}; it sets no outcome a student must show and "
            f"carries no level. Cite it as {cite(num(i))}. Do not present it as a statutory or regulatory requirement{extra}. "
            f"Set it beside {beside}.")


def pv_aad(when, q):
    return (f"Raise it with a programme team or reviewer when {when}. Frame it for staff as a check on course design or review and ask: {q} "
            f"Do not hand it to a student as their task or quote the paragraph at length.")


def pv(i, force, about, verbs, para, prac, when, q, beside, find=None, extra='', **k):
    rec = dict(type='expectation' if force in ('will',) else 'requirement', rung='none', force=force, level='none',
               appliesTo=k.pop('appliesTo', 'Health Studies courses and the teams who run them'), addressee='provider',
               verbs=verbs, about=about, domain='none', award=k.pop('award', [HON, MA]), para=para, prac=prac,
               ben=('n/a', k.pop('why', 'a duty on the course team or provider; the student meets its effect, not a standard to reach')),
               aaw=pv_aaw(i, force, beside, extra), aad=pv_aad(when, q))
    if find:
        rec['find'] = find
    rec.update(k)
    s(i, **rec)


# threshold honours: lead-in "should be able to"; force threshold from 4.3 (the minimum for an award)
ANNEX = {'r1': 'annex-d/summary/r1/3rd', 'r2': 'annex-d/summary/r2/3rd', 'r3': 'annex-d/summary/r3/3rd', 'r4': 'annex-d/summary/r4/3rd'}


def th(i, verbs, about, domain, x, y, q, fh, nb, row='r1', find=None):
    generic = domain == 'generic-skill'
    kind = 'a threshold generic skill' if generic else 'a threshold outcome in subject knowledge, understanding or skills'
    rec = dict(type='threshold', rung='threshold', force='threshold', forceFrom='4.3', level='fheq:6',
               appliesTo='honours graduates in the subject', addressee='learner', verbs=verbs, about=about, domain=domain, award=HON,
               para=f'As a minimum for honours, a graduate should be able to {x}.',
               prac=f'Teach and assess the course so that every honours graduate can {x}; this belongs to the minimum, not to the higher classes.',
               ben=f'As a minimum for your honours degree, you should be able to {y}.',
               aaw=(f"Present this as {kind} for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate "
                    f"in the subject should show it, so it is the floor and not a mark of distinction. Cite it as {cite(num(i))}. "
                    f"Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. "
                    f"Set it beside {nb}, the honours descriptor item qaa/fheq-2024/{fh}, Annex D's third-class column "
                    f"(qaa/fheq-2024/{ANNEX[row]}) and spine:6."),
               aad=(f"Bring it up when a student asks what an honours graduate must manage on {about}, or when a programme team checks "
                    f"module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; "
                    f"with staff, ask where the course teaches and assesses it. Ask: {q} Avoid reading the issuer's list aloud, and do "
                    f"not treat higher achievement as what the minimum demands."))
    if find:
        rec['find'] = find
    s(i, **rec)


def tm(i, verbs, about, domain, x, y, q, fh, nb, find=None):
    rec = dict(type='threshold', rung='threshold', force='threshold', forceFrom='4.3', level='fheq:7',
               appliesTo="master's graduates in the subject", addressee='learner', verbs=verbs, about=about, domain=domain, award=MA,
               para=f"As a minimum for a master's award, a graduate should be able to {x}.",
               prac=f"Design and assess the master's course so that every graduate can {x}; this is the level 7 floor.",
               ben=f"As a minimum for your master's degree, you should be able to {y}.",
               aaw=(f"Present this as a threshold outcome for the master's degree at FHEQ level 7 (FQHEIS level 11); para 4.6 also makes "
                    f"the master's lists a reference point for postgraduate certificates and diplomas. Cite it as {cite(num(i))}. "
                    f"Do not claim it as an honours outcome or a regulatory requirement, and note that the issuer's wording follows the "
                    f"FHEQ master's descriptor closely. Set it beside {nb}, qaa/fheq-2024/{fh} and spine:7."),
               aad=(f"Raise it when a master's student or team asks what the degree must show on {about}. Speak to a student in the "
                    f"second person about the minimum for the award; with staff, ask which module assesses it at level 7. Ask: {q} "
                    f"Avoid reciting the descriptor and do not present it as an honours expectation."))
    if find:
        rec['find'] = find
    s(i, **rec)


def ty(i, verbs, about, x, y, q, fh, nb):
    s(i, type='typical', rung='typical', force='will', level='fheq:7', appliesTo="typical holders of a master's qualification in the subject",
      addressee='learner', verbs=verbs, about=about, domain='generic-skill', award=MA,
      para=f"A typical holder of a master's qualification will be able to show that they can {x}.",
      prac=f"Expect most master's graduates to {x}, and give them chances to show it; it describes typical holders, above the 4.7 minimum.",
      ben=f"By the end of a master's, you will typically be able to {y}.",
      aaw=(f"Present this as a typical expectation of master's holders at FHEQ level 7 (FQHEIS level 11), led in with 'Typically' and "
           f"'will': it describes most graduates, not the minimum every graduate must reach. Cite it as {cite(num(i))}. Do not write it "
           f"into a programme as a pass condition, and do not claim it for honours. Set it beside {nb}, qaa/fheq-2024/{fh} and spine:7."),
      aad=(f"Bring it up when a master's student wants to know what a strong, typical graduate can do on {about}, or when staff plan "
           f"stretch in a module. Speak to a student in the second person; with staff, frame it as what most of the cohort should "
           f"reach. Ask: {q} Do not present it as the minimum for the award."))


def oc(i, verbs, about, x, y, q, strand, fh, find=None):
    rec = dict(type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students and graduates of the subject',
               addressee='learner', verbs=verbs, about=about, domain='generic-skill', award=HON,
               para=f'Students of the subject can {x}.',
               prac=f'Give students chances to {x}, and show where the course builds this competence.',
               ben=f'You will be able to {y}.',
               aaw=(f"Present this as one of the eight UNESCO sustainability competencies (2017) that the statement names as valuable for "
                    f"every graduate in the subject; it is an outcome without a rung, read here at honours (FHEQ level 6), which the text "
                    f"does not state. Cite it as {cite(num(i))}, crediting UNESCO for the competence. Do not present it as a threshold "
                    f"standard from section 4. Set it beside 1.32, 2.7, {strand}, qaa/fheq-2024/{fh} and spine:6."),
               aad=(f"Raise it when a student or team discusses sustainability and health, or plans an ESD activity. Use plain words, "
                    f"second person for a student, and ask: {q} Avoid lecturing on the UNESCO framework and do not treat the competence "
                    f"as a pass condition."))
    if find:
        rec['find'] = find
    s(i, **rec)


# ================================================================== section 1
pv('1.13', 'will', 'stakeholders in course work', ['envisaged', 'engaged'],
   para='Students, patients, the public, community agencies, voluntary services and employers will take part in planning, building, running and evaluating courses.',
   prac='Bring students, patients and the public, voluntary services and employers into each stage of the course, from planning through to evaluation.',
   when='a team plans a new course or a periodic review',
   q='Which stakeholders took part in the last revision, and at what stage?',
   beside='2.19, 2.20 and 2.29',
   find='It is envisaged that in the process of planning, development, delivery and evaluation of courses, relevant stakeholders such as students, patients and the public, agencies and individuals, voluntary services and employers will be engaged.')

pv('1.21', 'should', 'inclusive course design', ['designed', 'enable', 'realise', 'feel'],
   para='Courses should be built so that every student can reach their potential and feel represented and included, whatever their background, faith, ethnicity, disability, gender identity or sexuality.',
   prac='Design the course so each student can reach their potential and sees themselves represented and included, whatever their ethnicity, faith, gender identity, sexuality, disability or class.',
   when='a team designs or revises modules, modes of study or assessment',
   q='Which students might not see themselves in this module\'s content or modes of study?',
   beside='1.22, 1.23 and 2.4',
   find='Courses in Health Studies should be designed to enable students to realise their potential, and feel represented and included, regardless of their race/ethnicity, religion, gender identity, sexual orientation, disability or social background (s ee paragraph 2.4).')

pv('1.23', 'must', 'regular review of EDI with students', ['reflect', 'work'],
   para='Course teams must keep reviewing how to strengthen equality, diversity and inclusion and, where they can, do it in partnership with students.',
   prac='Review at set points how the course can do more on equality, diversity and inclusion, and involve students in the review where possible.',
   when='a team plans its annual review or a course change',
   q='When did the team last review its EDI practice, and were students part of it?',
   beside='1.21, 2.4 and 2.28.b1',
   find='Course teams must regularly reflect upon how EDI can be further enhanced and, where possible, work in partnership with students in doing so (see paragraph 2.2 - relating to course design).')

pv('1.24', 'should', 'accessibility at every stage', ['meet', 'apply'],
   para='Accessibility should at least satisfy regulatory requirements and will cover every stage of the course, from information before application to graduation and after.',
   prac='Treat regulatory accessibility requirements as the minimum and plan accessibility for each stage, from pre-application information to graduation and beyond.',
   when='a team reviews accessibility from admissions information through to graduation',
   q='Which stage of the course has had the least attention to accessibility?',
   beside='1.25, 1.26 and 3.7.b2',
   find='Accessibility should, as a minimum, meet regulatory requirements and will apply to all stages of the course, from providing pre-application information through to graduation and beyond (see paragraph 2.4 relating to course design).')

pv('1.27', 'should', 'the SDGs across the curriculum', ['integrated'],
   para='Understanding the UN Sustainable Development Goals is central to this vision, and where it fits the goals should run through the whole curriculum.',
   prac='Where appropriate, weave the Sustainable Development Goals through the curriculum as a whole rather than confining them to one module.',
   when='a team maps sustainability across a course',
   q='Which of the Goals does the curriculum touch, and in which modules?',
   beside='1.31.b1 to 1.31.b8, 2.7 and the ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance)',
   find='An understanding of the United Nation’s Sustainable Development Goals (SDGs) is essential to this vision and, where appropriate, the SDGs should be integrated holistically across the curriculum.')

# UNESCO sustainability competencies (1.31): an outcome list, "students can" / "are able to"
oc('1.31.b1', ['recognise', 'understand', 'analyse', 'consider', 'deal'], 'systems thinking',
   x='see how levels and units in health relate, analyse complex systems across domains and scales and cope with uncertainty',
   y='see how the parts and levels of health systems connect, analyse complex systems and cope with uncertainty',
   q='Can you map the parts of a health system involved in one problem you studied?', strand='strand:thinking', fh='4.15.b4')
oc('1.31.b2', ['understand', 'evaluate', 'create', 'apply', 'assess', 'deal'], 'anticipatory thinking',
   x='weigh possible futures, form their own visions of what is to come, use the precautionary principle, judge the effects of actions and handle risk and change',
   y='weigh up possible futures, form your own vision, act with care where effects are uncertain, judge the results of actions and handle risk and change',
   q='What future health risk in your area worries you, and what would you do about it now?', strand='strand:thinking', fh='4.15.b4')
oc('1.31.b3', ['understand', 'reflect', 'negotiate', 'set'], 'normative thinking',
   x='reflect on the norms and values behind actions, work through the values of sustainable development with others and set goals where interests clash and knowledge is uncertain in health',
   y='reflect on the norms and values behind what people do, work through sustainability values with others and set goals when interests clash and knowledge is uncertain',
   q='Which values clash in a health decision you know, and how would you set a goal between them?', strand='strand:thinking', fh='4.15.b7')
oc('1.31.b4', ['develop', 'implement', 'further'], 'strategic thinking',
   x='devise and carry out new actions that advance sustainable development locally and beyond',
   y='plan and carry out new actions that move sustainable development forward, near home and further away',
   q='What practical step towards sustainability could you lead in a health setting?', strand='strand:application', fh='4.15.b6')
oc('1.31.b5', ['work', 'learn', 'understand', 'respect', 'deal', 'facilitate'], 'collaborative practice',
   x="work and learn with people inside and outside their institution, respect others' needs and views, handle conflict in groups and support shared problem-solving",
   y='work and learn with people inside and outside your institution, respect their needs and views, handle conflict in a group and help others solve problems together',
   q='How did your last group handle disagreement, and what part did you play?', strand='strand:communication', fh='4.15.b9.1',
   find='Collaborative practice - Health Studies students can work together and learn from others, including peers and others inside and outside of their institution, understand\n\n9\nand respect the needs, perspectives and actions of others in the field, deal with conflicts in a group and facilitate collaborative and participatory problem-solving')
oc('1.31.b6', ['question', 'reflect', 'take'], 'critical thinking for sustainability',
   x='question accepted norms, practices and opinions, examine their own values and actions and take a stance in the debate on sustainable development',
   y='question accepted ideas and practices, look hard at your own values and take a position in debates about sustainable development',
   q='Where do you stand on one sustainability debate in health, and what shaped your view?', strand='strand:thinking', fh='4.15.b7')
oc('1.31.b7', ['reflect', 'consider', 'evaluate', 'motivate'], 'self-awareness',
   x='reflect on their own values, perceptions, actions, feelings and desires, consider their part in local and global society and keep judging and driving their own actions',
   y='reflect on your values, actions and feelings, think about your part in your community and the wider world and keep checking and driving your own actions',
   q="What part do you want to play in your community's health, and what keeps you going?", strand='strand:autonomy', fh='4.15.b9.3')
oc('1.31.b8', ['apply', 'develop', 'utilise', 'solve'], 'integrated problem-solving',
   x='use several problem-solving frameworks on complex sustainability problems in health, devise workable, inclusive and fair solutions and draw on the right competences to resolve them',
   y='use different problem-solving approaches on complex sustainability problems in health and work out solutions that are workable, inclusive and fair',
   q='Which framework did you use on your last complex problem, and was the result fair to everyone affected?', strand='strand:application', fh='4.15.b3.1')

pv('1.32', 'must', 'sustainability competencies in curricula', ['requires'],
   para="The subject's learning environment needs the sustainability competencies built into, and visible in, its curricula and learning resources.",
   prac='Build the eight sustainability competencies into the curriculum and learning resources and make them visible there.',
   when='a team audits its curriculum for sustainability',
   q='Where in the curriculum does each of the eight competencies appear?',
   beside='1.31.b1 to 1.31.b8 and 2.7',
   extra="; the text says 'requires', which this record reads as must (Part E)",
   find='The learning environment for Health Studies therefore requires these competencies to be integral and exemplified within course curricula and learning resources.')

pv('1.33', 'must', 'facilities for self-directed adult learners', ['requires', 'support'],
   para='The subject needs facilities that support study and experiential training for adults who direct their own learning.',
   prac='Provide facilities for study and experiential training that suit self-directed adult learners, across digital, individual, group and community settings.',
   when='a team plans learning spaces, placements or online resources',
   q='Do the facilities serve learners who direct their own study, on and off campus?',
   beside='1.34 and 2.16',
   extra="; the text says 'requires', which this record reads as must (Part E)",
   find='Health Studies requires facilities that support learning and experiential training for adults who are self-directed learners.')

s('1.37', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['understand', 'articulate', 'demonstrate', 'encouraged', 'develop', 'apply'], about='knowing and showing the worth of one\'s skills',
  domain='generic-skill', award=HON,
  find='Health Studies students should understand the commercial as well as practical value of their skillsets and be able to articulate and demonstrate them to potential employers and in plans for self-employment or private practice. They should also be encouraged to develop self-awareness of their own enterprising and entrepreneurial capabilities in the health sector, as well as the motivation and self-discipline to apply these flexibly in different ways and in changing contexts.',
  para="Students should grasp the commercial and practical worth of their skills, be able to explain and show them to employers or in plans to work for themselves; they should also be encouraged to know their own enterprising strengths in health and use them flexibly.",
  prac="Help students learn what their skills are worth commercially and in practice, rehearse presenting them to employers and in self-employment plans and reflect on their enterprising strengths in the health sector.",
  ben="You should understand what your skills are worth, commercially and in practice, and be able to explain and show them to employers or in a plan to work for yourself; you should also be helped to recognise your own enterprising strengths in health.",
  aaw=("Present this as a 'should' expectation of students, set in the enterprise and entrepreneurship section; it is a generic skill read "
       "at honours (FHEQ level 6), a level the paragraph does not state. Cite it as " + cite('1.37') + ". Do not present it as a threshold "
       "standard, since the section 4 lists hold the threshold. Set it beside 1.38, 4.5.b19, qaa/fheq-2024/4.15.b9.1 and spine:6."),
  aad=("Raise it when a student talks about careers, placements or self-employment, or when a team plans employability teaching. Ask a "
       "student which of their skills an employer would pay for and how they would prove it; ask staff where students practise "
       "presenting their skills. Do not treat it as a pass requirement or read the paragraph aloud."))

s('1.43', type='expectation', rung='none', force='should', level='none', appliesTo='the curriculum and students of the subject', addressee='both',
  verbs=['include', 'using', 'communicate', 'enhance'], about='ethical digital communication', domain='generic-skill', award=[HON, MA],
  find='Developing digital competency and transferable skills in Health Studies should include using digital technology ethically to communicate ideas creatively, innovatively and accessibly, in order to enhance academic success in the field, as well as employability.',
  para='Building digital competence and transferable skills should involve using digital technology ethically to share ideas in creative, original and accessible ways, for academic success and for employability.',
  prac="Include the ethical use of digital technology for creative, original and accessible communication in the course's work on digital and transferable skills.",
  ben='Your course should help you use digital technology ethically to share ideas in creative, original and accessible ways, for your studies and your career.',
  aaw=("Present this as a 'should' on how the course builds digital and transferable skills, read for honours and master's alike; it "
       "names no level. Cite it as " + cite('1.43') + ". Do not present it as a standalone threshold outcome or a regulatory duty. "
       "Set it beside 4.5.b13, 4.5.b14 and qaa/fheq-2024/4.15.b8."),
  aad=("Raise it when a team plans digital skills teaching or a student asks how to present work online responsibly. With staff, ask "
       "where students practise ethical, accessible digital communication; with a student, ask which digital format they would choose "
       "for a health message and how they would make it accessible. Do not read the paragraph aloud or treat it as a pass condition."))
P['1.43']['level'] = 'fheq:6'

# ================================================================== section 2
pv('2.1', 'should', 'multidisciplinary course design', ['given'],
   para='Because the subject is broad, course design should give proper thought to how several disciplines are combined.',
   prac='Think through how the course combines its disciplines; 1.16 lists those the subject draws on.',
   when='a team designs a new course or a joint award',
   q='Which disciplines does the course draw on, and how are they joined rather than set side by side?',
   beside='1.16, 2.2 and 2.13',
   find='Given that Health Studies courses cover a broad subject area (see paragraph 1.16 for the academic disciplines and subject areas that Health Studies draws on), due consideration should be given to the nature of multidisciplinary course design.')

pv('2.3', 'will', 'design resting on frameworks and standards', ['underpinned', 'communicate'],
   para='Course design will rest on national qualifications frameworks and sector-recognised standards, so that what an award represents is clear to stakeholders and service users.',
   prac='Ground the design in the national qualifications frameworks and sector-recognised standards and use them to show stakeholders and service users what the award stands for.',
   when='a team writes a programme specification or maps outcomes to levels',
   q='Which framework level descriptor does each exit award map to?',
   beside='4.3, 4.6 and the FHEQ (std:doc:qaa-fheq-2024-framework, S5)',
   find='The design of Health Studies courses will be underpinned by national qualifications frameworks and sector recognised standards to communicate the achievements and attributes represented by Health Studies awards to various stakeholders and service users.')

pv('2.4', 'should', 'EDI throughout the student experience', ['integrate', 'ensure', 'participate', 'complete'],
   para='Course teams should build the dimensions of equality, diversity and inclusion from section 1 into every part of the educational experience, so that all students have an equal chance to take part and finish.',
   prac='Build the EDI dimensions set out in section 1 into all parts of the student experience so every student has an equal chance to take part and finish.',
   when='a team reviews the student experience for equal opportunity',
   q='Where do students disengage or leave early, and does it differ between groups?',
   beside='1.21, 1.22 and 1.23',
   find='Course teams should integrate the dimensions of EDI as outlined in section 1 within all aspects of the educational experience to ensure that students have an equal opportunity to participate in and complete the course.')

pv('2.5', 'should', "learning about diverse patients' needs", ['given', 'gain'],
   para="Students should have the chance to learn what patients from varied social, cultural and ethnic backgrounds need; the statement takes this wording from the GMC's standards for medical education.",
   prac='Give students the chance to learn what patients from varied social, cultural and ethnic backgrounds need; decolonising the curriculum is one route the paragraph offers.',
   when='a team plans content on patient diversity or on decolonising the curriculum',
   q='Where do students meet the needs of patients from backgrounds unlike their own?',
   beside="2.4, 2.6 and the GMC's Promoting Excellence (2015; not yet ingested)",
   why='a duty on the course to give the opportunity; the student meets its effect',
   find='Students should be given ‘the opportunity to gain knowledge and understanding of the needs of patients from diverse social, cultural and ethnic backgrounds’ (GMC, 2015, p33).')

s('2.10', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='honours students of the subject', addressee='learner',
  verbs=['progress', 'develop', 'expected'], about='progression through the honours levels', domain='none', award=HON,
  para=("Across an honours degree at FHEQ level 6 (FQHEIS level 10), students will move up level by level, starting from basic subject "
        "knowledge and taking on more depth, challenge, complexity and autonomy, until they meet the threshold subject-specific and generic "
        "skills; this usually means passing all learning and assessment, practical parts included."),
  prac=("Plan each level so that knowledge, understanding, skills, behaviours and values build towards the section 4 threshold, with depth, "
        "challenge and autonomy rising from one level to the next, and credit for all components, practical ones too."),
  ben="You will start with the basics of the subject and take on more depth, challenge and independence at each level, building towards the minimum skills you need to graduate.",
  aaw=("Present this as an expectation ('will') about how students progress through an honours degree, with the honours level stated "
       "as FHEQ level 6 and FQHEIS level 10. Cite it as " + cite('2.10') + ". Do not treat it as an outcome in itself or as a rule on "
       "credit; the outcomes are in 4.4 and 4.5. Set it beside 2.11, 4.3, the level descriptors qaa/fheq-2024/4.10, 4.12 and 4.15, "
       "and spine:4 to spine:6."),
  aad=("Raise it when a student asks how the levels of the degree differ, or when a team plans the step up between years. With a "
       "student, explain in plain words that each year asks for more depth and independence, and ask what they now do on their own that "
       "they could not do last year. Do not read out the paragraph or suggest that the final threshold applies in the first year."))

s('2.11', type='expectation', rung='none', force='will', level='none', appliesTo='undergraduate students of the subject', addressee='learner',
  verbs=['move', 'manage', 'take'], about='from structured study to autonomy', domain='none', award=HON,
  find='Students will move gradually from highly structured, directed study which scaffolds learning and supports their transition to higher education, into a more autonomous position where they manage and take responsibility for their own learning.',
  para='Students will move step by step from closely guided, structured study that eases their entry to higher education to a more independent position in which they run their own learning.',
  prac='Plan for a gradual shift from tightly structured, directed study in the first year to students managing and owning their learning by the end.',
  ben='You will move gradually from closely guided study, which helps you settle in, to managing and taking charge of your own learning.',
  aaw=("Present this as an expectation ('will') about the shift towards autonomous learning over the degree; it names no level. Cite it "
       "as " + cite('2.11') + ". Do not present it as a threshold outcome. Set it beside 2.10, 2.11.b1 to 2.11.b4, 4.5.b8 and "
       "qaa/fheq-2024/4.15.b5."),
  aad=("Raise it when a student finds the change to independent study hard, or when a team plans transition support. In plain words, "
       "ask a student which parts of their learning they now plan for themselves and where they still need structure. Do not imply "
       "that needing support early on is a failing."))

for k, verbs, about, para, prac, q in [
    (1, ['recognise'], 'prior experience and transition',
     "Strategies for progression should take account of students' varied prior experience and of how hard the move into higher education can be.",
     "Make progression strategies allow for students' different prior experience and for the challenges of transition.",
     'How does the course find out what experience each student brings?'),
    (2, ['allow', 'achieve', 'realise'], 'every student reaching their potential',
     'They should let every student reach their potential and ambitions, whatever their background or reasons for choosing the subject.',
     "Check that progression support lets every student reach their potential, whatever their background or motive for study.",
     'Do progression rates differ by background, and what is the course doing about it?'),
    (3, ['support'], 'academic and personal development',
     'They should support academic and personal growth as well as learning in the subject itself.',
     'Support academic and personal development alongside subject learning, for example through tutoring and skills provision.',
     'Where does the course support personal development, not only subject learning?'),
    (4, ['matched'], 'fit with outcomes at each level',
     "They should fit the course's learning outcomes or competences at each level of study.",
     'Align progression strategies with the learning outcomes or competences set for each level.',
     'Which outcomes does the progression support at each level aim at?'),
]:
    pv(f'2.11.b{k}', 'should', about, verbs, para=para, prac=prac,
       when='a team plans progression and transition support', q=q,
       beside='2.10, 2.11 and the level descriptors qaa/fheq-2024/4.10, 4.12 and 4.15')

s('2.13', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='undergraduates on combined or joint degrees', addressee='learner',
  verbs=['achieve', 'add', 'explore'], about='joint and combined degrees', domain='none', award=HON,
  para="Undergraduates who take the subject in a combined or joint degree will reach the core of this statement's specific and generic skills and add others from their other subject; they may also explore where the disciplines overlap.",
  prac="In joint and combined awards, make sure students reach the core subject-specific and generic skills here, and let the other subject add its own.",
  ben='If you study health as part of a joint or combined degree, you will reach the core subject and general skills described here and add others from your other subject.',
  aaw=("Present this as an expectation ('will') for honours students on joint or combined degrees at FHEQ level 6: they reach the core "
       "of 4.4 and 4.5, not every item. Cite it as " + cite('2.13') + ". Do not claim that joint students meet the full lists, or that "
       "the paragraph defines which items are core. Set it beside 2.1, 4.4, 4.5 and qaa/fheq-2024/4.15."),
  aad=("Raise it when a joint-honours student asks what they must cover in health, or when two departments plan a combined award. Ask a "
       "student which health skills they have built so far and what their other subject adds. Do not tell a joint student they must meet "
       "every item of the single-honours lists."))

pv('2.16', 'will', 'varied delivery methods', ['offered'],
   para='Courses will offer a varied range of delivery methods suited to the student, the material and how it is assessed.',
   prac='Offer a varied range of delivery methods chosen to suit students, the content and its assessment.',
   when='a team chooses delivery modes or reviews flexibility',
   q='Does the mix of delivery modes suit the students actually enrolled?',
   beside='2.17, 3.3 and 3.5',
   find='The range of delivery methods offered through Health Studies courses will be diverse and appropriate for the needs of the student, the taught material and their assessments.')

pv('2.18', 'will', 'flexible design and review', ['allow', 'address', 'considering'],
   para='Course design and review will be flexible enough for teams to meet the needs of students, industry and society while taking account of what external governing or accrediting bodies require.',
   prac='Keep design and review flexible so the team can respond to students, industry and society and to changes from governing or accrediting bodies.',
   when='a course faces an accrediting body or new industry needs',
   q='Can the course change quickly enough when an accrediting body changes its requirements?',
   beside='2.16, 2.20 and 2.26',
   find='Course design and review will be sufficiently flexible to allow course teams to address the needs of students, industry and society while considering requirements raised by external governing or accrediting bodies.')

pv('2.19', 'will', 'stakeholders as partners', ['envisaged', 'engaged'],
   para='Stakeholders will be brought in as partners in planning, developing, delivering and evaluating courses.',
   prac='Engage relevant stakeholders as partners across the life of the course, at a depth of partnership that suits the context, from consultation to co-delivery.',
   when='a team sets up partnership with employers, service users or students',
   q='At what depth are stakeholders involved now: consulted, co-creating or co-delivering?',
   beside='1.13, 2.20 and 2.29',
   find='It is envisaged that relevant stakeholders will be engaged as partners in the process of planning, development, delivery and evaluation of courses.')

pv('2.20', 'should', 'alignment with the regulatory body', ['written'],
   para='Where it applies, courses should be written to align with the relevant regulatory body.',
   prac='Where a regulatory body is relevant, write the course in line with its requirements.',
   when='a course leads to a regulated or professional role',
   q='Which regulatory body, if any, does this course need to align with?',
   beside='2.18, 2.26 and 3.10.b6',
   find='Where relevant, courses should be written in alignment with the relevant regulatory body.')

pv('2.22', 'will', 'support for apprentices', ['ensure', 'given', 'achieve'],
   para='Employers and providers will make sure apprentices get the support they need to reach professional or occupational competence.',
   prac='Agree with employers how apprentices are supported to reach professional or occupational competence and who coordinates that support.',
   when='a team designs or reviews an apprenticeship degree',
   q='Who coordinates support for each apprentice between employer and university?',
   beside="3.11 and QAA's Higher Education Apprenticeships Characteristics Statement (not yet ingested)",
   appliesTo='employers and providers of apprenticeship degrees',
   find='Employers and higher education providers will ensure apprentices are given the support necessary to achieve professional and/or occupational competence.')

pv('2.23', 'will', 'the student voice in review', ['considering', 'form'],
   para='Course review will take account of what students say.',
   prac='Include the student voice in routine monitoring and in periodic course review.',
   when='a team plans periodic review',
   q='How does student feedback reach the review, and what changed because of it?',
   beside='2.20, 2.27 and 2.29',
   find='Considering the student voice will form part of this.')

pv('2.24', 'will', 'external reviewers in periodic review', ['use', 'gain', 'ensure'],
   para='Providers will bring external reviewers into periodic review for an outside view of proposed changes, to confirm that threshold standards are met and content suits the subject.',
   prac='Use external reviewers in periodic review to test proposed changes, confirm the threshold standards are met and check the content fits the subject.',
   when='a team prepares for periodic review',
   q='Who is the external reviewer, and what will they check against the threshold standards?',
   beside='2.25, 2.27 and 4.3',
   find='Providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.')

pv('2.27', 'will', 'external reference points in review', ['considered', 'ensure'],
   para='Review will weigh a range of external reference points, this statement among them, so that provision matches the norms of the health sector.',
   prac='Name the external reference points the review uses, this statement among them, and check provision against health sector norms.',
   when='a team chooses the reference points for review',
   q='Which external reference points does the review use besides this statement?',
   beside='2.23, 2.24 and 2.28.b1 to 2.28.b10',
   find='A range of external reference points, including this Subject Benchmark Statement, will be considered to ensure that higher education provision aligns with health sector norms.')

for k, verbs, about, para, prac, q in [
    (1, ['reviewing'], 'an inclusive, aligned curriculum',
     'Monitoring and review will support an inclusive curriculum by checking that the planned, delivered and achieved curriculum line up.',
     'Use review to compare what the curriculum intends, what is delivered and what students achieve, with inclusion in view.',
     'Where do the planned and the achieved curriculum part company, and for whom?'),
    (2, ['incorporates'], 'a responsive curriculum',
     'They will support a curriculum that responds to change and takes in feedback from key stakeholders.',
     'Feed stakeholder feedback into the curriculum through each review cycle.',
     'What did the last cycle change in response to stakeholders?'),
    (3, ['embedding'], 'institutional goals and sector practice',
     "They will support embedding the institution's goals and the sector's best practice across the curriculum.",
     "Check through review that institutional goals and sector good practice reach every part of the curriculum.",
     'Which institutional goal is least visible in the curriculum?'),
    (4, ['meet'], 'standards meeting the qualifications framework',
     'They will support academic standards that satisfy the relevant national qualifications framework.',
     'Use review to confirm that academic standards meet the relevant national qualifications framework.',
     'How does the review confirm each award meets its framework level?'),
    (5, [], 'moderation',
     'They will support moderation, inside the institution and from outside it.',
     'Run internal and external moderation as part of monitoring and review.',
     'How are marks moderated, and what did the last external moderation find?'),
    (6, [], 'internal reviews',
     "They will support the institution's own internal reviews.",
     "Link course monitoring to the institution's internal review process.",
     'When is the next internal review, and what evidence will it use?'),
    (7, ['align'], 'annual monitoring and professional bodies',
     'They will support annual monitoring, internal or external, in line with what professional bodies require.',
     'Align annual monitoring, internal or external, with professional body requirements.',
     "Which professional body's requirements does annual monitoring check?"),
    (8, [], 'open communication',
     'They will support open communication within teaching teams and with stakeholder partners.',
     'Keep communication open inside the teaching team and with stakeholder partners through the review cycle.',
     'How do stakeholder partners hear what the review found?'),
    (9, [], 'consumer law compliance',
     'They will support compliance with the requirements of the Competitions and Markets Authority.',
     'Check through review that course information and terms meet Competitions and Markets Authority requirements.',
     'When were course information and terms last checked for consumer law?'),
    (10, [], 'feedback from external quality exercises',
     'They will support use of feedback from external quality exercises such as the TEF, the NSS, PTES and PRES.',
     'Use results from the TEF, the NSS, PTES and PRES in monitoring and review.',
     'What did the latest survey results show, and what has the team done about them?'),
]:
    pv(f'2.28.b{k}', 'will', about, verbs, para=para, prac=prac,
       when='a team plans or audits its monitoring and review cycle', q=q, beside='2.27, 2.29 and 2.24')

# ================================================================== section 3
pv('3.3', 'will', 'specified, culturally aware teaching strategies', ['specified', 'consider'],
   para='Teaching and learning strategies will be set out clearly in the course and will take account of the different learning and teaching cultures students bring.',
   prac='State the teaching and learning strategies clearly in the course documents and allow for the learning cultures students arrive with.',
   when='a team writes or revises its teaching and learning strategy',
   q='Where are the teaching strategies stated, and how do they allow for students\' earlier learning cultures?',
   beside='3.4, 3.5 and 2.16',
   find='The learning and teaching strategies will be clearly specified within the course of study, and will consider the diverse learning and teaching cultures that students may have experienced.')

pv('3.4', 'should', 'critical evaluation to build skills', ['engage', 'develop'],
   para="Courses should use critical evaluation and analysis to build students' skills in problem-solving, judging solutions, deciding and creativity.",
   prac='Build critical evaluation and analysis into teaching so students develop problem-solving, judgement of solutions, decision-making and creativity.',
   when='a team plans teaching activities for higher-order skills',
   q='Which activities ask students to judge solutions and decide, not only to describe?',
   beside='4.4.b3, 4.5.b4 and 4.5.b6')

pv('3.7.b1', 'will', 'formative and summative assessment', ['reflect', 'support'],
   para='Assessment will be formative and summative, and a range of methods will track progression through the course and support graduate outcomes.',
   prac='Use both formative and summative assessment, and a range of methods that show progression and support graduate outcomes.',
   when='a team designs an assessment strategy',
   q='Where does formative assessment come before each summative task?',
   beside='3.8, 3.9.b1 and 2.10',
   find='Assessment will be both\n\n20\nformative and summative. A range of assessment methods will reflect progression within the course of study and support graduate outcomes.')

pv('3.7.b2', 'should', 'reasonable adjustments in assessment', ['implemented', 'support'],
   para="Reasonable adjustments are needed and should fit the curriculum's demands; sliding scales can help make assessment inclusive.",
   prac='Make reasonable adjustments to assessment that fit what the curriculum demands, and consider sliding scales for inclusive assessment.',
   when='a team sets or reviews assessment adjustments',
   q='How are adjustments decided, and do they keep to what the module must assess?',
   beside='1.24, 2.4.b8 and 3.10.b3',
   find='Reasonable adjustments are necessary and should be appropriate to the demands of the curriculum, and sliding scales can be implemented to support inclusive assessment (see paragraphs 1.24-1.26).')

pv('3.7.b3', 'should', 'generative AI in teaching and assessment', ['consider', 'incorporated'],
   para='Teaching staff should decide how far generative AI tools enter their teaching, learning and assessment.',
   prac='Decide, and state, how far generative AI tools are part of teaching, learning and assessment on the course.',
   when='a team sets its position on generative AI',
   q='What does each module tell students about using generative AI?',
   beside='3.7.b4, 3.8 and 4.5.b14',
   appliesTo='teaching staff on the course',
   find='Educators should consider the extent to which generative artificial intelligence (AI) tools are incorporated into their teaching, learning and assessment strategies.')

s('3.7.b4', type='requirement', rung='none', force='must', level='none', appliesTo='teaching staff and students', addressee='both',
  verbs=['remain', 'exercising'], about='the limits and risks of AI', domain='generic-skill', award=[HON, MA],
  find='However, both educators and students must remain cognisant of the limitations and risks involved, with a view to exercising responsible and ethical practices.',
  para='Staff and students alike must stay aware of the limits and risks of AI tools so that their use stays responsible and ethical.',
  prac='Make sure staff and students know the limits and risks of the AI tools in use, and set out what responsible, ethical use looks like.',
  ben='You must stay aware of the limits and risks of AI tools and use them responsibly and ethically.',
  aaw=("Present this as a 'must' that binds staff and students alike: awareness of the limits and risks of AI tools, for responsible and "
       "ethical use; it names no level and is read here for honours and master's. Cite it as " + cite('3.7, the sentence on AI risks') + ". "
       "Do not present it as a ban on AI or as a regulatory rule. Set it beside 3.7.b3, 4.5.b14 and qaa/fheq-2024/4.15.b4."),
  aad=("Raise it whenever a student or teacher plans to use an AI tool for learning, assessment or marking. Ask a student what the tool "
       "could get wrong in their task and how they would check it; ask staff how the course explains those risks. Do not present AI as "
       "forbidden, and do not read the paragraph aloud."))
P['3.7.b4']['level'] = 'fheq:6'

pv('3.9.b1', 'will', 'qualities of good feedback', [],
   para='Good feedback will be personal to the student, clear, empowering, manageable and aimed at development.',
   prac='Write feedback that is personal, clear, empowering, manageable and points to next steps.',
   when='a team reviews its feedback practice',
   q='Would a student know what to do next after reading this feedback?',
   beside='3.9.b2, 3.9.b3 and 3.10.b1 to 3.10.b6',
   find='Effective feedback will be personal, individual, understandable, empowering, manageable and developmental.')

pv('3.9.b2', 'should', 'timely feedback that supports reflection', ['accompanied', 'allow'],
   para='Feedback should be prompt, tied to the assessment brief and backed by help in interpreting it, and should give students room to reflect on their academic and professional growth.',
   prac='Return feedback promptly, link it to the brief, offer help in reading it and leave students room to reflect on their development.',
   when='a team sets feedback turnaround or support',
   q='How soon does feedback arrive, and who helps students make sense of it?',
   beside='3.9.b1, 3.10.b5 and 4.5.b9',
   find='It should be timely, relevant to the assessment brief and accompanied by access to interpretative support/advice. Feedback should allow students the opportunity for supportive reflection on their academic and professional development.')

pv('3.9.b3', 'will', 'feedback arrangements known in advance', ['made'],
   para='Students will be told beforehand what feedback each task brings, how much and when.',
   prac='Publish the nature, amount and timing of feedback for each assessment before the task is set.',
   when='a team writes assessment briefs',
   q='Does each brief say what feedback will come, and when?',
   beside='3.9.b1, 3.9.b2 and 3.10.b2',
   find='The nature, extent and timing of feedback for each assessment task will be made clear in advance.')

for k, verbs, about, para, prac, q, find in [
    (1, ['be'], 'valid, reliable, consistent feedback', 'Feedback should be sound, dependable and even across markers.',
     'Check that feedback is valid, reliable and consistent across markers and modules.', 'How does the team check that markers give consistent feedback?', None),
    (2, ['be'], 'clear and available feedback', 'Feedback should be clear and easy for students to get hold of.',
     'Make feedback clear and easy to find.', 'Where do students find their feedback, and can they read it easily?', None),
    (3, ['take'], 'accessibility and EDI in feedback', 'Feedback should allow for accessibility and equality, diversity and inclusion, such as particular learning needs.',
     'Adapt feedback to accessibility needs and EDI, such as specific learning needs.', 'How is feedback adapted for students with specific learning needs?', None),
    (4, ['be', 'relate'], 'feedback tied to outcomes', "Feedback should be part of the course and plainly linked to its learning outcomes.",
     'Link feedback to the learning outcomes and make it part of the course design.', 'Does the feedback name the outcome it addresses?', None),
    (5, ['give', 'validate'], 'confirming knowledge', 'Feedback should let students confirm what they know and understand.',
     'Use feedback to let students confirm their knowledge and understanding.', 'Does the feedback tell students what they have got right, not only what to fix?', None),
    (6, ['align'], 'progression and PSRB requirements', 'Feedback should fit the rules on progression and any PSRB requirements that apply.',
     'Align feedback with progression rules and with PSRB requirements where they apply.', 'Which PSRB requirements, if any, shape feedback on this course?',
     'align with progression and PSRB requirements as necessary.'),
]:
    pv(f'3.10.b{k}', 'should', about, verbs, para=para, prac=prac,
       when='a team reviews its feedback policy', q=q, beside='3.9.b1 to 3.9.b3 and 3.10', find=find)

pv('3.11', 'will', 'supervision shaped in partnership', ['developed', 'allowing', 'contextualise', 'make'],
   para='Supervision will be shaped jointly by teaching staff, employers and workplace supervisors, helping students put learning in context and contribute to health in professional settings.',
   prac='Develop the supervision role with employers and workplace supervisors so students can place their learning in context and contribute in practice.',
   when='a team sets up placements or work-based supervision',
   q='Who agreed the supervision arrangements, and does each party know its role?',
   beside='3.12.b1 to 3.12.b7 and 2.22',
   find='The role of supervision will be developed in partnership with educators, employers, and work-based supervisors, allowing students to contextualise their learning and make a positive contribution to health in the professional context.')

for k, verbs, about, para, prac, q in [
    (1, ['understanding'], 'preparing supervisors', 'Supervision must take account of preparing supervisors to understand varied learning styles and how students are assessed.',
     'Prepare supervisors on varied learning styles and on the assessments students face.', 'How are new supervisors prepared before they take a student?'),
    (2, ['influenced', 'enhance'], 'collaborative supervision', 'It must take account of a collaborative approach that local or contextual practice can shape to improve learning.',
     'Use a collaborative approach to supervision that can adapt to local practice.', 'How does supervision adapt to the practice setting?'),
    (3, ['setting'], 'objectives and action plans', 'It must take account of setting objectives, tracking progress and planning actions with students.',
     'Set objectives, monitor progress and plan actions with each student.', 'Does each student have objectives and an action plan agreed with their supervisor?'),
    (4, [], 'a learning culture', 'It must take account of promoting a culture of learning in the organisation.',
     'Promote a culture of learning in the host organisation.', 'What does the host organisation do to support learning?'),
    (5, [], 'advocacy and coaching', 'It must take account of advocating for and coaching students.',
     'Make advocacy for, and coaching of, students part of the supervisor role.', 'Who speaks up for the student if a placement goes wrong?'),
    (6, ['providing', 'build'], 'critical reflection on earlier learning', 'It must take account of chances for critical reflection that build on earlier learning.',
     'Give students structured chances for critical reflection that draw on what they already know.', 'When do students reflect with their supervisor, and on what?'),
    (7, [], 'three-way supervision', 'It must take account of three-way supervision involving the industry or healthcare sector.',
     'Arrange three-way supervision between student, course and the industry or healthcare setting.', 'Is the workplace a full party to supervision, with the student and the course?'),
]:
    pv(f'3.12.b{k}', 'must', about, verbs, para=para, prac=prac,
       when='a team designs supervision for placements or practice', q=q, beside='3.11 and 3.12',
       extra="; the lead-in says 'requires consideration of', which this record reads as must (Part E)")

# ================================================================== section 4
pv('4.2', 'should', 'Annex D for achievement above the threshold', ['refer'],
   para='Each provider decides what counts as evidence of achievement above the threshold and should refer to Annex D of the Frameworks for Higher Education Qualifications.',
   prac="Use Annex D's classification descriptions when deciding what evidence shows achievement above the threshold; the statement gives no rungs above it.",
   when='a team writes classification criteria or marking descriptors',
   q='How do the course\'s classification criteria use Annex D?',
   beside='4.3, qaa/fheq-2024/annex-d/summary and std:ref:uk-assesscriteria (band axis)',
   appliesTo='higher education providers',
   find='Each higher education provider has the autonomy in determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies.')

s('4.3', type='requirement', rung='none', force='must', level=['fheq:6', 'fheq:7'], appliesTo="students seeking an honours or master's award",
  addressee='learner', verbs=['describe', 'demonstrate'], about='the threshold as the minimum for an award', domain='none', award=[HON, MA],
  find='The undergraduate minimum threshold Level 6 and the postgraduate minimum threshold Level 7 describe the minimum acceptable level of achievement that a student must demonstrate to be eligible for an award.',
  para='The threshold at level 6 for undergraduates and at level 7 for postgraduates marks the least a student must show to be eligible for an award.',
  prac="Treat the section 4 threshold lists as what every student must show for the award: level 6 for honours, level 7 for master's.",
  ben="To be awarded your degree, you must show at least the threshold level: level 6 for an undergraduate degree, level 7 for a master's.",
  aaw=("Present this as the 'must' that defines the threshold: the minimum a student shows to be eligible for an honours award (level 6) "
       "or a master's award (level 7). Cite it as " + cite('4.3') + ". Do not claim it sets a pass mark or classifications; those rest "
       "with the provider and Annex D (4.2). Set it beside 4.4, 4.5, 4.7, qaa/fheq-2024/4.15, qaa/fheq-2024/4.17 and "
       "qaa/fheq-2024/annex-d/summary/r1/3rd."),
  aad=("Raise it when a student asks what they must achieve to graduate, or when a team debates whether an outcome is essential. Tell a "
       "student plainly that the threshold lists are the minimum for the award, and ask which items they feel least sure of. Do not "
       "confuse the threshold with a class of degree or read the lists aloud."))

pv('4.6', 'should', "master's standards as a level 7 reference point", ['used'],
   para="These master's standards should also act as a reference point for other qualifications at FHEQ level 7 and FQHEIS level 11, such as postgraduate certificates and diplomas.",
   prac="Use the master's lists as a reference point when designing postgraduate certificates and diplomas in the subject.",
   when="a team designs a postgraduate certificate or diploma in health",
   q="Which master's outcomes does the shorter award draw on, and which does it leave out?",
   beside='4.7, 4.8 and qaa/fheq-2024/4.17.i2',
   appliesTo='postgraduate qualifications at level 7 in the subject', award=[MA, 'postgraduate certificate', 'postgraduate diploma'],
   find='This qualification descriptor should also be used as a reference point for other qualifications at Level 7 of the FHEQ and Level 11 on the FQHEIS, including postgraduate certificates and postgraduate diplomas.')
P['4.6']['level'] = 'fheq:7'

# ---- 4.4 threshold: subject knowledge, understanding and skills (honours)
th('4.4.b1', ['apply', 'integrate'], 'applying and joining theory across settings', 'subject-skill',
   x='use their knowledge across linked settings and bring together the theories behind the subject on physical, psychosocial and mental well-being',
   y='use what you know across connected settings and combine the theories behind health on body, mind and social well-being',
   q='Which piece of work shows you combining more than one theory to explain a health question?', fh='4.15.b3.1', nb='4.4.b4 and 4.4.b18')
th('4.4.b2', ['demonstrate'], 'the breadth of the subject in real problems', 'knowledge',
   x='show they grasp how wide the subject is by using it on practical problems',
   y='show how wide the field of health is by using it to tackle practical problems',
   q='Can you name a real problem you worked on and the parts of the subject you drew on?', fh='4.15.b1', nb='4.4.b1 and 4.4.b7')
th('4.4.b3', ['adopt', 'evaluate', 'problem-solve'], 'judging issues from several viewpoints', 'subject-skill',
   x='take more than one viewpoint when judging and resolving issues that arise in health settings',
   y='look at health issues from several viewpoints when you judge them and work out what to do',
   q='When you last analysed a health issue, which viewpoints did you weigh and which did you leave out?', fh='4.15.b7', nb='4.4.b16 and 4.5.b4', row='r4')
th('4.4.b4', ['synthesise', 'create'], 'joining specialist knowledge for new solutions', 'subject-skill',
   x="combine specialist and linked knowledge from the subject's many disciplines to devise new answers to health problems",
   y='draw together knowledge from the different disciplines in health to come up with new answers to health problems',
   q='Where have you joined ideas from two disciplines to propose something new?', fh='4.15.b3.1', nb='4.4.b1 and 4.4.b18', row='r4')
th('4.4.b5', ['synthesise', 'integrate', 'inform'], 'evidence with national policy and guidance', 'subject-skill',
   x='join research evidence with relevant national policy and guidance and use the result to shape the subject',
   y='connect research evidence with national health policy and guidance',
   q='Which national policy or guideline have you tested against the evidence, and what did you find?', fh='4.15.b1', nb='4.4.b13')
th('4.4.b6', ['understand', 'reflects'], 'health in a global, mobile world', 'understanding',
   x='understand health globally, allowing for the way travel, migration and displacement move populations',
   y='understand health in a global way, including how travel, migration and displacement move people around',
   q='How does population movement change the health question you are studying?', fh='4.15.b1', nb='4.4.b16')
th('4.4.b7', ['understand'], 'the many dimensions of health', 'understanding',
   x='understand that health has physical, mental and social sides that shift over time, and know the challenges it faces now',
   y='understand that health covers body, mind and social life, changes over time and faces current challenges',
   q='Which current health challenge can you explain from its physical, mental and social sides?', fh='4.15.b1', nb='4.4.b2')
th('4.4.b8', ['demonstrate'], 'theories of causality in health', 'knowledge',
   x='show understanding of several theories of what causes health and ill health',
   y='explain several theories of what makes people healthy or ill',
   q='Which two theories of the causes of ill health can you compare, and where do they disagree?', fh='4.15.b1', nb='4.4.b14')
th('4.4.b9', ['describe'], 'reasons given for health interventions', 'knowledge',
   x='set out a variety of theoretical and professional reasons offered for health interventions',
   y='explain the different theoretical and professional reasons people give for health interventions',
   q='For one intervention you know, what reasons were given for it, and by whom?', fh='4.15.b3.2', nb='4.4.b10')
th('4.4.b10', ['collate', 'analyse', 'present'], 'evidence on health promotion and autonomy', 'subject-skill',
   x='gather, analyse and report evidence on how health promotion helps people make their own life choices',
   y='gather, analyse and present evidence on how health promotion helps people make their own choices',
   q='What evidence have you gathered on a health promotion campaign, and how did you present it?', fh='4.15.b6', nb='4.4.b9')
th('4.4.b11', ['describe'], 'individuals and institutions shaping health', 'knowledge',
   x='explain how individuals and institutions each shape health status',
   y='explain how both individuals and institutions affect how healthy people are',
   q='In a case you know, what did individuals do and what did institutions do to change health?', fh='4.15.b1', nb='4.4.b13')
th('4.4.b12', ['appreciate'], 'varied experiences and values of health', 'understanding',
   x='recognise that people experience and value health in many different ways',
   y='recognise that people, you included, experience and value health in different ways',
   q='How might someone from a different background see the health issue you are working on?', fh='4.15.b4', nb='4.4.b15')
th('4.4.b13', ['compare', 'contrast'], 'healthcare systems and policy', 'subject-skill',
   x='compare different healthcare systems and the policy-making behind them',
   y='compare healthcare systems and the policies that shape them',
   q='Which two healthcare systems could you compare, and on what points?', fh='4.15.b7', nb='4.4.b5', row='r4')
th('4.4.b14', ['demonstrate'], 'theoretical debates in the subject', 'knowledge',
   x="show they know a variety of the subject's theoretical debates",
   y='show you know the main theoretical debates in your subject',
   q='Which theoretical debate in the subject could you sum up for a fellow student?', fh='4.15.b3.1', nb='4.4.b8')
th('4.4.b15', ['demonstrate'], 'ethics and values in health', 'understanding',
   x='show an informed grasp of ethical viewpoints and of the many values people attach to health and to well-being of body and mind',
   y='show you understand ethical viewpoints and the range of values people hold about health and well-being',
   q='Which ethical question in your area divides people, and what values sit on each side?', fh='4.15.b4', nb='4.4.b12 and 4.5.b20')
th('4.4.b16', ['discuss', 'evaluate'], 'health inequalities and population interventions', 'subject-skill',
   x='discuss inequalities in health between populations and judge how well population-wide action narrows health gaps in diverse ethnic communities',
   y='discuss health inequalities between groups and judge how well population-wide action narrows them in diverse ethnic communities',
   q='Which intervention aimed at a health gap have you assessed, and what did it achieve?', fh='4.15.b7', nb='4.4.b19', row='r4')
th('4.4.b17', ['appreciate'], 'why research matters', 'understanding',
   x='recognise why research matters to the subject',
   y='recognise why research matters in the study of health',
   q='How has a research finding changed what you think about a health question?', fh='4.15.b3.2', nb='4.4.b21')
th('4.4.b18', ['apply', 'drawing', 'reflect'], 'working across disciplinary lines', 'subject-skill',
   x='cross traditional subject lines, using knowledge from other disciplines to think about health issues',
   y='cross the lines between subjects, using ideas from other disciplines to think about health issues',
   q='Which other discipline has helped you most with a health issue, and how?', fh='4.15.b6', nb='4.4.b4')
th('4.4.b19', ['demonstrate'], 'integrated analysis with EDI principles', 'subject-skill',
   x='analyse health issues across diverse populations in a joined-up way that takes account of equality, diversity and inclusion',
   y='analyse health issues across diverse groups in a joined-up way, with equality, diversity and inclusion in mind',
   q='In your last analysis, how did you check that it held for different groups?', fh='4.15.b7', nb='4.4.b16 and 4.5.b18', row='r4')
th('4.4.b20', ['demonstrate'], 'social and psychological sides of public health messages', 'understanding',
   x='show they understand why social and psychological factors decide whether public health messages succeed',
   y='show you understand why social and psychological factors decide whether public health messages work',
   q='Think of a public health message: why did it work, or fail, with its audience?', fh='4.15.b8', nb='4.5.b11')
th('4.4.b21', ['consider'], 'current questions in health research', 'understanding',
   x='weigh current questions and arguments in health research and debate',
   y='think through current questions and arguments in health research',
   q='Which current debate in health research do you follow, and where do you stand?', fh='4.15.b3.2', nb='4.4.b17')
th('4.4.b22', ['analyse', 'demonstrate'], 'epidemiology and surveillance', 'subject-skill',
   x='analyse the epidemiology and effects of communicable and non-communicable disease and show how regional, national and global surveillance systems collect health data',
   y='analyse how communicable and non-communicable diseases spread and affect people, and understand how surveillance systems at regional, national and global level collect health data',
   q='Which surveillance data have you used, and what did they tell you about a disease?', fh='4.15.b2', nb='4.4.b8',
   find='analyse the impact and epidemiology of communicable and non-communicable diseases and demonstrate understanding of the role of surveillance systems available regionally, nationally and globally in gathering health data.')

# ---- 4.5 threshold: generic skills (honours)
GS = [
    (1, ['operate'], 'working in complex settings', 'work well in varied, complex work or practice settings that show the many sides of the subject',
     'work well in different complex work or practice settings across health', 'Which placement or work setting has tested you most, and how did you cope?', '4.15.b9.2', '4.5.b8', 'r2'),
    (2, ['work', 'taking'], 'teamwork and shared responsibility', "work in a team and accept responsibility for their own and the group's results",
     "work in a team and take responsibility for your own part and for the group's results", 'In your last group task, what were you responsible for, and how did the group do?', '4.15.b9.1', '4.5.b1', 'r2'),
    (3, ['bring'], 'drawing information together', 'assemble information and material from several sources across typical areas of the subject',
     'pull together information from several sources across the main areas of health', 'For your last assignment, how many kinds of source did you combine?', '4.15.b5', '4.5.b7', 'r1'),
    (4, ['identify', 'propose'], 'problems and possible solutions', 'spot problems and suggest possible solutions where that fits',
     'spot problems and suggest ways to solve them', 'What problem have you spotted recently, and what did you suggest?', '4.15.b7', '4.4.b3', 'r4'),
    (5, ['analyse'], 'analysing facts', 'analyse factual information',
     'analyse factual information', 'Which facts or data have you analysed this term, and what did you conclude?', '4.15.b7', '4.5.b17', 'r4'),
    (6, ['recognise'], "judging others' arguments", "see where other people's arguments are strong and where they are weak",
     "see where other people's arguments are strong and where they fall short", 'Which argument in your reading did you find weakest, and why?', '4.15.b7', '4.4.b14', 'r4'),
    (7, ['produce'], 'summing up current knowledge with guidance', 'with guidance, write a synthesis of what is known on a given subject or topic',
     'with guidance, write a summary that brings together what is known on a topic', 'Have you written a review of what is known on a topic, and how much help did you need?', '4.15.b5', '4.5.b3', 'r1'),
    (8, ['undertake'], 'working independently', 'carry out tasks on their own',
     'carry out tasks on your own', 'Which piece of work have you done with little or no direction?', '4.15.b9.1', '4.5.b2', 'r2'),
    (9, ['reflect', 'act'], 'reflection and acting on feedback', 'reflect critically on their own progress and use feedback from different sources',
     'reflect critically on your progress and act on feedback from different people', 'What feedback have you acted on recently, and what changed as a result?', '4.15.b9.3', '3.10.b5', 'r3'),
    (10, ['express'], 'clear communication in several modes', 'communicate clearly in modes suited to the situation: spoken, non-verbal and digital',
     'communicate clearly in ways that suit the situation, in speech, body language and digital media', 'Which modes of communication have you used in assessed work so far?', '4.15.b8', '4.5.b12', 'r1'),
    (11, ['recognise'], 'communication for health promotion and EDI', 'recognise how spoken and non-verbal communication help promote health, and apply equality, diversity and inclusion principles across every channel',
     'recognise how spoken and unspoken communication can promote health, and keep your communication inclusive in every channel', 'How would you adapt a health message so it reaches and respects different groups?', '4.15.b8', '4.4.b20', 'r1'),
    (12, ['present'], 'making knowledge understandable', 'put knowledge or an argument across so that others can follow it',
     'put across what you know, or an argument, so that others can follow it', 'Who outside your course could follow your last piece of work, and how do you know?', '4.15.b8', '4.5.b10', 'r1'),
    (13, ['use', 'collate', 'analyse', 'select', 'present'], 'IT and digital literacy', 'use suitable IT to gather, analyse, choose and present information, showing digital literacy',
     'use suitable digital tools to gather, analyse, choose and present information', 'Which digital tools do you use to handle information, and how confident are you with them?', '4.15.b2', '4.5.b14 and 1.43', 'r1'),
    (14, ['appreciate'], 'AI and technology in health', 'recognise what AI and other technologies do in health',
     'recognise what artificial intelligence and other technologies do in health', 'Where have you seen AI used in health, and what were its limits?', '4.15.b4', '3.7.b3 and 3.7.b4', 'r1'),
    (15, ['demonstrate'], 'listening and comprehension', 'show they can listen to and understand new ideas or information',
     'show you can listen to and make sense of new ideas or information', 'When did you last change your mind after hearing a new idea?', '4.15.b5', '4.5.b12', 'r3'),
    (16, ['demonstrate'], 'identifying and describing material', 'show skill in identifying and describing material',
     'show you can identify and describe material accurately', 'Can you describe a source you used in a few accurate sentences?', '4.15.b3.2', '4.5.b17', 'r1'),
    (17, ['demonstrate'], 'handling data', 'show skill in describing, sorting and gathering data',
     'show you can describe, sort and gather data', 'How did you organise the data in your last project?', '4.15.b6', '4.5.b5', 'r1'),
    (18, ['understand'], 'health and safety and EDI at work', 'understand why health and safety and equality, diversity and inclusiveness matter at work',
     'understand why health and safety and equality, diversity and inclusion matter in the workplace', 'What would you check first on health and safety and on inclusion in a new workplace?', '4.15.b9.1', '4.4.b19', 'r2'),
    (19, ['appreciate', 'engage'], 'debates on sustainability and employability', 'understand and take part in current debates on global sustainability and employability',
     'follow and take part in current debates on global sustainability and on work', 'Which debate on sustainability and health have you joined, and what did you argue?', '4.15.b9.3', '1.31.b6 and 1.37', 'r2'),
    (20, ['apply'], 'ethics and professional codes', 'bring a thorough grasp of ethical questions and professional conduct codes to their work in the subject',
     'apply a thorough grasp of ethics and professional codes of conduct in your work', 'Which professional code applies to the work you want to do, and what does it ask of you?', '4.15.b9.3', '4.4.b15', 'r2'),
]
for k, verbs, about, x, y, q, fh, nb, row in GS:
    th(f'4.5.b{k}', verbs, about, 'generic-skill', x=x, y=y, q=q, fh=fh, nb=nb, row=row,
       find='apply an in-depth awareness of ethical issues and professional codes of conduct in Health Studies.' if k == 20 else None)

# ---- 4.7 master's threshold: subject knowledge
tm('4.7.b1', ['informed'], 'systematic understanding and critical awareness', 'knowledge',
   x='show a systematic grasp of the field and a critical, up-to-date sense of today\'s health problems and fresh insights, much of it drawn from or at the leading edge of their discipline or practice',
   y='show a systematic grasp of your field and a critical sense of today\'s health problems and fresh insights, much of it at or near the leading edge',
   q='Which current problem in your field could you explain at the level of the latest research?', fh='4.17.b1', nb='4.7.b2 and 4.4.b2')
tm('4.7.b2', [], 'research techniques', 'understanding',
   x='show full understanding of the techniques that suit their own research or advanced study',
   y='show you fully understand the techniques that fit your own research or advanced study',
   q='Which methods suit your own research question, and why those rather than others?', fh='4.17.b2', nb='4.7.b3')
tm('4.7.b3', ['used', 'create', 'interpret'], 'originality and how research makes knowledge', 'understanding',
   x='apply knowledge with originality and understand in practice how established research techniques produce and interpret knowledge in the discipline',
   y='apply what you know in original ways and understand how research methods build and interpret knowledge in your field',
   q='Where in your work have you applied knowledge in a way your sources did not?', fh='4.17.b3', nb='4.7.b2 and 4.8.b3')
tm('4.7.b4', ['enables', 'evaluate', 'develop', 'propose'], 'critical evaluation of research and methods', 'understanding',
   x='hold a conceptual understanding that lets them critique current research, advanced scholarship and methods, form critiques and, where fitting, put forward new hypotheses',
   y='understand ideas well enough to critique current research and its methods and, where it fits, suggest new hypotheses',
   q='Which study in your area would you challenge, and what hypothesis would you test instead?', fh='4.17.b4.1', nb='4.7.b1 and 4.4.b21',
   find='a conceptual understanding that enables the student to critically evaluate current research and advanced scholarship in the discipline, to evaluate methodologies, to develop critiques and, where appropriate, to propose new hypotheses.')

# ---- 4.8 master's: "Typically, holders ... will be able to demonstrate skills that show"
ty('4.8.b1', ['deal', 'manage'], 'complex issues and uncertainty',
   x='handle complex health issues systematically and creatively and manage uncertainty in a changing field',
   y='handle complex health issues in a systematic and creative way and cope with uncertainty in a changing field',
   q='Which complex health issue have you worked through, and how did you handle what was unknown?', fh='4.17.b5', nb='4.8.b2 and 4.5.b1')
ty('4.8.b2', ['make', 'communicate'], 'judgement with incomplete data',
   x='make sound judgements when health data are incomplete and explain their conclusions clearly to specialists and non-specialists',
   y='make sound judgements when the health data are incomplete, and explain your conclusions clearly to experts and non-experts',
   q='When did you last decide something without all the data, and how did you explain it?', fh='4.17.b5', nb='4.8.b1 and 4.5.b12')
ty('4.8.b3', ['tackling', 'solving', 'act', 'planning', 'implementing'], 'self-direction and autonomy',
   x='direct themselves, solve problems with originality and act on their own in planning and carrying out tasks at professional level',
   y='direct yourself, solve problems with originality and plan and carry out tasks on your own at a professional level',
   q='Which task have you planned and carried through entirely on your own?', fh='4.17.b6', nb='4.7.b3 and 4.5.b8')
ty('4.8.b4', [], 'continuing to advance knowledge and skills',
   x='keep advancing their knowledge and understanding and build new skills to a higher level',
   y='keep extending what you know and building new skills to a higher level',
   q='What new skill are you building now, and how will you know it has reached a higher level?', fh='4.17.b7', nb='4.8.b6')
ty('4.8.b5', [], 'initiative and decisions in complex situations',
   x='take initiative and personal responsibility and make decisions in complex, unpredictable situations, professional ones included',
   y='take the initiative, take responsibility and make decisions in complex, unpredictable situations, including at work',
   q='Describe a time you had to decide something while the situation kept changing.', fh='4.17.b8.2', nb='4.8.b3 and 4.5.b1')
ty('4.8.b6', ['required', 'demonstrating'], 'independent learning for professional development',
   x='learn independently in the way continuing professional development needs',
   y='learn independently in the way that continuing professional development needs',
   q='How will you plan your own learning once no course sets it for you?', fh='4.17.b8.3', nb='4.8.b4 and 4.5.b9')

GRADE = {}   # no rung pairs: honours has only a threshold rung; the master's typical list (4.8) is generic skills, its threshold list (4.7) is knowledge
TH = {'1.21': 'theme:edi', '1.23': 'theme:edi', '2.4': 'theme:edi', '2.5': 'theme:edi',
      '1.24': 'theme:accessibility',
      '1.27': 'theme:esd', '1.32': 'theme:esd', '1.33': 'theme:esd',
      '1.37': 'theme:enterprise', '1.43': 'theme:enterprise'}
for _k in range(1, 9):
    TH[f'1.31.b{_k}'] = 'theme:esd'

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.10; 4.3 (as Level 6)'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.10'),
            dict(id='fheq:7', role='cites', locator='D1, 2.15; 4.6; 4.3 (as Level 7)'),
            dict(id='fqheis:11', role='cites', locator='D1, 2.15; 4.6'),
            dict(id='spine:6', role='refers (inferred)', locator='std:ref:uk-framework R2, R8: the step for honours standards'),
            dict(id='spine:7', role='refers (inferred)', locator="std:ref:uk-framework R2, R8: the step for master's standards")],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.10: a degree with honours (FHEQ Level 6; FQHEIS Level 10))'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.15 integrated master's; 4.6 Level 7 of the FHEQ and Level 11 on the FQHEIS)")])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23', '2.4', '2.5', '2.6', '2.28', '2.30', '3.7', '3.10', '4.4', '4.5']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.21', '1.22', '1.24', '1.25', '1.26', '2.4', '2.16', '2.17', '2.21', '3.7', '3.10']),
      dict(id='theme:esd', role='carries', carriedIn=['1.16', '1.19', '1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '2.7', '2.17', '2.19', '2.30', '4.5']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.35', '1.36', '1.37', '1.38', '1.39', '1.40', '1.41', '1.42', '1.43', '1.44', '1.45', '1.46', '1.47', '1.48', '1.49', '2.8']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['3.7', '3.8', '4.5'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-health-studies-2019-benchmarks (not yet ingested)', note='the fourth edition, 2019, named in section 6; earlier editions 2016, 2007 and 2002'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the classification descriptions, for evidence above the threshold (4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note="levels 6 and 7 (2.10, 2.15, 4.6); the master's lists 4.7 and 4.8 follow descriptor 4.17 closely"),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 10 and 11 (2.10, 2.15, 4.6)'),
      dict(rel='themeReference', target='std:doc:qaa-advancehe-esd-2021-guidance', note='definitions of sustainable development and ESD (1.27)'),
      dict(rel='refersTo', target="QAA Higher Education Apprenticeships Characteristics Statement, 2022 (not yet ingested)", note='2.22'),
      dict(rel='refersTo', target='QAA, Creating Inclusive Subject Learning Communities, 2021 (not yet ingested)', note='2.28.b1'),
      dict(rel='refersTo', target='GMC, Promoting Excellence: standards for medical education and training, 2015 (not yet ingested)', note='quoted in 2.5'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance; QAA Glossary (not yet ingested)', note='front matter'),
      dict(rel='readWith', target='other QAA Subject Benchmark Statements', note='for multidisciplinary and joint courses (1.8, 2.1)')]

S8 = dict(published='2024-04', lastReviewed='none-stated', reviewCycle='none-stated',
          consultation='none-stated; an advisory group of 17 members is listed (section 6)', replacedBy='none')

SB1 = [
    'The study of health across the life-course in individuals, families, communities and populations, from local to global, taking in physical and mental health, well-being, illness, rehabilitation and palliative care (D1, 1.1, 1.2, 1.6).',
    'Health is treated as more than the absence of disease and has no single agreed definition; studying it is not the same as studying illness or training to care for the sick (D1, 1.9).',
    'Multidisciplinary and interdisciplinary: it draws on over 30 disciplines, from epidemiology and public health to sociology, law and ethics, and courses choose their own mix (D1, 1.3, 1.14, 1.16, 2.1, 2.2).',
    'Reflective and reflexive critical evaluation of health and how it is represented sits at its centre (D1, 1.10, 1.12).',
    'An integrated, interprofessional care approach, with patients, service users and carers as partners (D1, 1.5, 1.11).',
    'Research-based, with attention to research ethics and to how research informs clinical practice and its governance (D1, 1.6, 1.12).',
    'Courses range from conceptual to applied and vocational, some shaped by professional standards; the aim is to make students agents of change (D1, 1.7, 1.11, 1.15, 1.29).',
]

SB2 = [dict(theme='theme:edi',
            inThisSubject='treated as part of the culture of the subject, set out as why, what and how it is taught; health inequalities, decolonising the curriculum, culturally safe care and the legal duty against discrimination (D1, 1.17 to 1.23, 2.4 to 2.6)',
            statements=['1.21', '1.23', '2.4', '2.5', '3.10.b3', '4.4.b16', '4.4.b19', '4.5.b11', '4.5.b18']),
       dict(theme='theme:accessibility',
            inThisSubject='every course requirement open to every student from pre-application to graduation; alternative assessments, reasonable adjustments, digital access and equal access to placements and international learning (D1, 1.24 to 1.26, 2.17, 3.7)',
            statements=['1.24', '3.7.b2', '3.10.b3']),
       dict(theme='theme:esd',
            inThisSubject='headed Sustainability: planetary health and the link between sustainability, equity and health; the SDGs across the curriculum; the eight UNESCO competencies as outcomes; problem-based and interprofessional ESD teaching (D1, 1.27 to 1.34, 2.7)',
            statements=['1.27', '1.31.b1', '1.31.b2', '1.31.b3', '1.31.b4', '1.31.b5', '1.31.b6', '1.31.b7', '1.31.b8', '1.32', '1.33', '4.5.b19']),
       dict(theme='theme:enterprise',
            inThisSubject='enterprise and entrepreneurship for employed and self-employed health careers: an entrepreneurial mindset, placements, external speakers and business-focused assignments (D1, 1.35 to 1.49, 2.8)',
            statements=['1.37', '1.43', '4.5.b19']),
       dict(theme='theme:generative-ai',
            inThisSubject='not a section of its own: one passage on how far generative AI enters teaching, learning and assessment and on staying alert to its limits; AI tools among assessment methods; the role of AI in health among the generic skills (D1, 3.7, 3.8, 4.5)',
            statements=['3.7.b3', '3.7.b4', '4.5.b14'])]

SB3 = dict(
    areas=[dict(component='1.10', gloss='common themes: health as human experience in its contexts; reflective and critical evaluation of health and its representations'),
           dict(component='1.16', gloss='32 contributing disciplines and subject areas, from allied health, epidemiology and public health to sociology, social policy and social work'),
           dict(component='3.1', gloss='content for reflective, critical study of health, well-being and illness'),
           dict(component='3.2', gloss='specialising within a broad field; integration with social care')],
    practices=[dict(component='1.34', kind='teaching', gloss='ESD methods: problem-based and interprofessional learning, simulations, field trips, placements'),
               dict(component='3.3', kind='teaching', gloss='blended, communicative and inclusive strategies; synchronous and asynchronous'),
               dict(component='3.5', kind='learning', gloss='lectures, seminars, labs, case-based patient-led seminars, tutorials; peer, self-directed, work-based and inter-professional learning'),
               dict(component='3.7', kind='assessment', gloss='formative and summative; inclusive; reasonable adjustments; generative AI'),
               dict(component='3.8', kind='assessment', gloss='essays, online resources, presentations, projects, examinations, portfolios, work-based and practical assessment'),
               dict(component='3.9', kind='assessment', gloss='feedback qualities and timing; feed-in, feed-forward and feedback'),
               dict(component='3.10', kind='assessment', gloss='six things feedback should do'),
               dict(component='3.11', kind='learning', gloss='supervision in practice, developed with employers'),
               dict(component='3.12', kind='learning', gloss='what supervision needs: preparation, objectives, coaching, tripartite arrangements')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.4; 4.5 (defined as the minimum in 4.1 and 4.3)', award=HON, items=42),
           dict(rung='threshold', leadIn='4.7 (defined as the minimum in 4.3)', award=MA, items=4),
           dict(rung='typical', leadIn="4.8 ('Typically, holders ... will be able to')", award=MA, items=6),
           dict(rung='excellent', leadIn='none', award='none', items=0)],
    rungBases=("threshold 46 records in all (honours 4.4: 22, 4.5: 20; master's 4.7: 4); typical 6 (master's 4.8); no typical or "
               "excellent rung for honours: 4.2 leaves achievement above the threshold to the provider and Annex D"),
    outcomeLists=[dict(leadIn='1.31', gloss='the eight UNESCO sustainability competencies, as what students can do', items=8, award=['honours (inferred)'])],
    outcomes=[])

SB4A_FULL = []

SB5 = [dict(body='professional, statutory and regulatory bodies (PSRBs), unnamed',
            says='may evaluate and accredit courses with professional or vocational outcomes; courses align with a relevant regulatory body where one applies; feedback and monitoring align with their requirements (D1, 2.18, 2.20, 2.26, 2.28, 3.10)',
            requirements='not yet ingested (Part E)'),
       dict(body='Academy for Healthcare Science', says='one of the registers or bodies graduates might join (D1, 2.9)', requirements='not yet ingested (Part E)'),
       dict(body='Faculty of Public Health', says='one of the bodies graduates might join (D1, 2.9)', requirements='not yet ingested (Part E)'),
       dict(body='Royal Society of Public Health', says='one of the bodies graduates might join; named so in the text (D1, 2.9)', requirements='not yet ingested (Part E)'),
       dict(body='Institute of Health Promotion and Education', says='one of the bodies graduates might join (D1, 2.9)', requirements='not yet ingested (Part E)'),
       dict(body='General Medical Council (GMC)', says="its 2015 standards for medical education are quoted on learning the needs of diverse patients (D1, 2.5)", requirements='not yet ingested (Part E)'),
       dict(body='Competitions and Markets Authority (CMA)', says='monitoring and review support compliance with its requirements (D1, 2.28)', requirements='not yet ingested (Part E)'),
       dict(body='Advance HE', says='co-issuer of the ESD guidance; its term for an inclusive environment in curriculum design (D1, 1.27, 2.4)', requirements='std:doc:qaa-advancehe-esd-2021-guidance'),
       dict(body='UNESCO', says='source of the eight sustainability competencies (D1, 1.31)', requirements='not yet ingested (Part E)')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion (EDI)', carriedIn=S6[0]['carriedIn'], statements=SB2[0]['statements']),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=S6[1]['carriedIn'], statements=SB2[1]['statements']),
            dict(id='theme:esd', named='Sustainability; Education for Sustainable Development (ESD)', carriedIn=S6[2]['carriedIn'], statements=SB2[2]['statements']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (EEE); front matter: employability, entrepreneurship and enterprise education', carriedIn=S6[3]['carriedIn'], statements=SB2[3]['statements']),
            dict(id='theme:generative-ai', named='generative artificial intelligence (AI) tools', carriedIn=S6[4]['carriedIn'], statements=SB2[4]['statements'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.10', '2.15', '4.2', '4.6']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.10', '2.15', '4.2', '4.6']),
                dict(framework='other: national qualifications frameworks, unnamed', levels=[], citedIn=['2.3', '2.28'])],
    bodies=[dict(body='PSRBs (unnamed)', citedIn=['2.18', '2.20', '2.26', '2.28', '3.10']),
            dict(body='Academy for Healthcare Science', citedIn=['2.9']),
            dict(body='Faculty of Public Health', citedIn=['2.9']),
            dict(body='Royal Society of Public Health', citedIn=['2.9']),
            dict(body='Institute of Health Promotion and Education', citedIn=['2.9']),
            dict(body='General Medical Council', citedIn=['2.5']),
            dict(body='Competitions and Markets Authority', citedIn=['2.28']),
            dict(body='Advance HE', citedIn=['1.27', '2.4']),
            dict(body='UNESCO', citedIn=['1.31'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies',
             citedIn=['4.2'], role='descriptions of the four honours classifications, for evidence of achievement above the threshold'),
        dict(document='std:doc:qaa-fheq-2024-framework', named='FHEQ', citedIn=['2.10', '2.15', '4.6'], role='levels 6 and 7'),
        dict(document='std:doc:qaa-fqheis-2024-framework', named='FQHEIS', citedIn=['2.10', '2.15', '4.6'], role='levels 10 and 11'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named="QAA and Advance HE's Education for Sustainable Development Guidance, 2021",
             citedIn=['1.27'], role='definitions of sustainable development and ESD'),
        dict(document='not yet ingested: listed in Part E', named="QAA's Higher Education Apprenticeships Characteristics Statement", citedIn=['2.22'], role='describes apprenticeship degrees'),
        dict(document='not yet ingested: listed in Part E', named='QAA, 2021, p11 (Creating Inclusive Subject Learning Communities, by the reference list)', citedIn=['2.28'], role='intended, implemented and attained curriculum'),
        dict(document='other QAA Subject Benchmark Statements', named='other relevant Subject Benchmark Statements', citedIn=['1.8', '2.1'], role='for multidisciplinary and joint courses')])

B1 = [dict(slug='health', definition='wholeness and physical and mental well-being, carrying senses of contentment, equity and justice, and going beyond freedom from disease; it has no single agreed definition (D1, 1.9)',
           beneficiaryDefinition='health means more than not being ill: being well in body and mind, and living fairly', scopeNote='studying health is set apart from studying illness or training in care', category='unknown', practices=['health']),
      dict(slug='reflective-and-reflexive-self-awareness', definition='reflective awareness notices one\'s own biases and preferences; reflexive awareness asks how one\'s own history and culture shape dealings with others (D1, 1.10)',
           beneficiaryDefinition='being reflective means noticing your own biases; being reflexive means seeing how your background shapes how you treat others', scopeNote='the two are linked and complementary', category='unknown', practices=['health', 'education']),
      dict(slug='equality-diversity-and-inclusion', definition='a wide set of identity characteristics, with attention to intersectionality, embedded in the culture and practice of the subject (D1, 1.17)',
           beneficiaryDefinition='fair treatment and a sense of belonging for everyone, whatever their identity', scopeNote='abbreviated EDI', category='unknown', practices=['education']),
      dict(slug='accessibility', definition='whether every requirement of a course, however met, can be understood and completed by all students (D1, 1.24)',
           beneficiaryDefinition='whether you can understand and complete everything the course asks of you', scopeNote='at least the regulatory minimum; every stage of the course', category='unknown', practices=['education']),
      dict(slug='education-for-sustainable-development', definition="building curriculum structures and content that support and enact sustainable development, as QAA and Advance HE's 2021 guidance defines it (D1, 1.27)",
           beneficiaryDefinition='learning that helps you work towards a fairer, more sustainable world', scopeNote='abbreviated ESD', category='unknown', practices=['education']),
      dict(slug='enterprise-and-entrepreneurship-education', definition='education for the behaviours, attributes and competencies that support successful and self-determined careers (D1, 1.35, 1.36)',
           beneficiaryDefinition='learning that builds the enterprising qualities you need for your career, employed or self-employed', scopeNote='abbreviated EEE', category='unknown', practices=['education']),
      dict(slug='apprenticeship-degree', definition='a degree that combines taught study with work-based learning, the workplace being the main source of learning (D1, 2.22)',
           beneficiaryDefinition='a degree you take mostly through your job, with study alongside', scopeNote='QAA describes these further in a separate statement', category='unknown', practices=['education'])]

B2A = [dict(concept='equality-diversity-and-inclusion', form='Equality, diversity and inclusion (EDI)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='education-for-sustainable-development', form='Education for Sustainable Development (ESD)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='enterprise-and-entrepreneurship-education', form='Enterprise and entrepreneurship education (EEE)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='reflective-and-reflexive-self-awareness', form='reflexive self-awareness', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='apprenticeship-degree', form='Apprenticeship degrees', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []
B5 = []

D3 = [dict(source='Subject Benchmark Statement: Health Studies, fourth edition (QAA, 2019)', why='the superseded edition, for supersedes and change analysis'),
      dict(source="QAA Higher Education Apprenticeships Characteristics Statement (2022)", why='cited at 2.22'),
      dict(source='QAA, Creating Inclusive Subject Learning Communities (2021)', why='cited at 2.28 as QAA, 2021'),
      dict(source='GMC, Promoting Excellence: standards for medical education and training (2015)', why='quoted at 2.5'),
      dict(source='UNESCO, Education for Sustainable Development Goals: learning objectives (2017)', why='source of the eight competencies at 1.31')]

E = [
    'Rungs: honours has a threshold rung only (4.4 subject, 4.5 generic); no typical or excellent rung. 4.2 leaves achievement above the threshold to the provider and Annex D. Differs from Psychology, which states three rungs.',
    "Master's: the statement covers master's degrees with their own lists (4.7 subject knowledge, 4.8 generic skills); recorded as award master's, level fheq:7. They have their own paragraph numbers, so no `.masters` suffix is needed.",
    "4.8 lead-in reads 'Typically, holders of a qualification in Health Studies will be able to demonstrate skills that show': recorded as rung typical with force will, after the FHEQ's split between threshold outcomes and what typical holders can do (std:doc:qaa-fheq-2024-framework, SL5). Alternative reading for P3: the threshold generic skills for master's, parallel to 4.5. Doubtful cut.",
    "4.7 and 4.8 restate the FHEQ master's descriptor (qaa/fheq-2024/4.17.b1 to 4.17.b8.3) almost word for word, with 'health' added; 4.6 calls them 'This qualification descriptor'.",
    "Threshold force: the 4.4, 4.5 and 4.7 lead-ins say 'should be able to'; recorded force threshold with forceFrom 4.3, which defines the threshold as the minimum a student 'must demonstrate to be eligible for an award' (brief convention).",
    'No gradeOf links: the only typical list (4.8, generic skills, master\'s) has no threshold list of the same domain and award below it (4.7 is knowledge and understanding). SB4 outcomes left empty.',
    "Outcome list 1.31: the UNESCO competencies, items in 'can' or 'are able to'; recorded rung none, award honours and level fheq:6 inferred (the paragraph names no award).",
    "1.31.b5: the skeleton cut the item at the page break after 'understand'; re-cut with find to the item's end, page number 9 included in the span.",
    "Skeleton spans with a glued heading re-cut with find: 3.10.b6 ('Supervision'), 4.4.b22 ('Generic skills'), 4.5.b20 (the master's heading), 4.7.b4 ('Generic skills').",
    "Paragraph statements cut to their obliging sentence with find (1.13, 1.21, 1.23, 1.24, 1.27, 1.32, 1.33, 1.37, 1.43, 2.1, 2.3, 2.4, 2.5, 2.11, 2.16, 2.18 to 2.24, 2.27, 3.3, 3.11, 4.2, 4.3, 4.6). 2.10 and 2.13 take the whole paragraph; 3.4 takes the skeleton's span.",
    "3.7 and 3.9 hold several modals; each obliging sentence is its own record, numbered 3.7.b1 to 3.7.b4 and 3.9.b1 to 3.9.b3. These are sentence records, not list items: for P3.",
    "Obliging words outside the five: 'requires' (1.32, 1.33) and 'requires consideration of' (3.12 lead-in) recorded as must; 'essential' (1.12 critical reflection, 1.27 the SDGs, 2.24 externality, 3.9 feedback) and 'it will be important' (2.2) not recorded as statements: for Abbott.",
    "'Will want to' (2.20 first sentence, 2.21) and 'would be expected' (2.12) read as soft and not recorded as statements: for Abbott.",
    "Not statements, by the brief: plain-present provider norms (for example 1.20 'courses ensure', 1.29, 2.23 'routinely collect', 3.1, 3.2); 1.3 'students are required to draw on a wide variety of subject disciplines' read as a description of the subject's breadth; 1.11 aims ('being given the opportunity to'); 1.28 and 1.30 'will' about what awareness or reflection does; 1.35 'It will prepare' (a prediction about EEE); 2.19 and 2.27 list items (what partnership and monitoring help to do); 2.25 external examiners' duties.",
    "Not statements: the 'may include' lists (1.22, 1.24.b1 to b4, 2.4.b1 to b12, 2.6, 2.17, 3.5, 3.8) and the entrepreneurial mindset list (1.38).",
    "2.28.b1 to b10 recorded as provider expectations under the lead-in 'will support and enable'.",
    "2.11.b1 to b4 recorded as provider duties under 'should be reinforced by strategies that'.",
    "Generic-skill records outside section 4 (1.37, 1.43, 3.7.b4, 1.31.b1 to b8) carry level fheq:6 inferred, so that SB-4 holds; the paragraphs name no level.",
    "4.3 carries level [fheq:6, fheq:7] as a list: it states both thresholds.",
    'Theme generative AI: no section of its own; tagged from 3.7, 3.8 and 4.5 under theme:generative-ai.',
    "Theme names: front matter lists 'employability, entrepreneurship and enterprise education'; the section is headed 'Enterprise and entrepreneurship education'. Sustainability is headed 'Sustainability' and names ESD.",
    'Bodies: the statement names four bodies a graduate might join (2.9), quotes the GMC (2.5) and names the CMA (2.28); none is a professional body that accredits the subject, and PSRBs are named only in general. Requirements not ingested.',
    'Advance HE and UNESCO recorded in SB5 and SB6 though neither is a PSRB: Advance HE co-issues the ESD guidance; UNESCO is the source of the competencies.',
    "'Royal Society of Public Health' as the text names it (recall: the body styles itself Royal Society for Public Health; to check).",
    "Shared QAA documents not yet ingested: Higher Education Apprenticeships Characteristics Statement (2.22); Creating Inclusive Subject Learning Communities (2.28, cited as QAA, 2021, p11); the Quality Code's Advice and Guidance and the Glossary (front matter). QAA's Enterprise and Entrepreneurship Education (std:doc:qaa-enterprise-2018-guidance) appears only in the reference list, so it is not in SB6.",
    'Subjects: hecos 100473 health studies stated by title; CAH15-04-03 and its parents by the HECoS mapping; hecos 100476 health and social care inferred (related code; social care named in 1.16 and 3.2), held back until P3 confirms it.',
    'Supersedes: the fourth edition (2019) from section 6, which is excluded matter read only for this; no date of the previous edition appears in the front matter.',
    "1.21 source keeps the extraction's '(s ee paragraph 2.4)' as held.",
    "Levels 4 and 5 (CertHE and DipHE exits, 2.14) are named as awards but not as levels; not recorded in S5.",
    'S9 commentary not researched in P1.',
]
