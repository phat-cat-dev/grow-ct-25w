# bm_content.py: judgement for run 0100, QAA Subject Benchmark Statement: Early Childhood Studies (March 2022), std.
# Read by tools/bm_build.py. Every text field below is our words; the issuer's words reach the document only through
# `source`, cut from the held text by span. The section 4 table is cut cell by cell from the held text here (see CELLS).
import json as _json, os as _os, re as _re

SLUG = 'early-childhood-studies-2022'
_BASE = ''
for _b in ('', '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/'):
    if _os.path.exists(_b + 'stan/core/qaa/benchmarks/' + SLUG + '.norm.txt'):
        _BASE = _b; break
_N = open(_BASE + 'stan/core/qaa/benchmarks/' + SLUG + '.norm.txt', encoding='utf-8').read()
_SK = _json.load(open(_BASE + 'ingest-std-qaa-early-childhood-studies-2022-benchmarks/run-src/bm-skel.json', encoding='utf-8'))
_COMP = {c['number']: c for c in _SK['components']}
_CAND = {c['id'].split('/')[-1]: c['span'] for c in _SK['candidateStatements']}

HON = "bachelor's with honours"
MAS = "master's"
CITE = 'QAA (2022), Early Childhood Studies Subject Benchmark Statement'

META = dict(
    run='0100', p1='2026-10-03 17:17',
    title='Subject Benchmark Statement Early Childhood Studies',
    heading='Subject Benchmark Statement: Early Childhood Studies (QAA, March 2022)',
    edition='March 2022 (fourth edition)', published='2022-03',
    status='current', supersedes='the third edition (2019), as the back matter states; earlier editions 2014 and 2007',
    subjects=[dict(scheme='hecos', code='100457', label='early childhood studies', basis='stated'),
              dict(scheme='cah', code='CAH15-04-02', label='childhood and youth studies', basis='inferred')],
    awards=[HON, MAS], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 revision (fourth edition for this subject)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    authority='reference: a sector reference point, not a regulatory requirement; in England not a sector-recognised standard under the OfS framework; a key reference point in Wales (Quality Assessment Framework for Wales) and Scotland (Quality Enhancement Framework); part of quality requirements in Northern Ireland (D1, front matter: Relationship to legislation and regulation)',
    agentDefinition=('QAA\'s UK reference point for what a graduate in Early Childhood Studies, the interdisciplinary study of children from conception to eight, '
                     'should know and be able to do: its subject-specific and generic skill lists and a four-column table of standards (threshold, typical, excellent '
                     'and postgraduate), each column headed by a degree class. Reach for it when designing, reviewing or describing an early childhood course, its '
                     'outcomes or its placements. It is not a curriculum, not the degrees network\'s graduate practitioner competencies and not a regulatory requirement in England.'),
    summary=('Published by QAA in March 2022 as the fourth edition, the statement sets out the context and purposes of the subject, its distinctive features '
             '(design, accessibility, progression, flexibility, partnership, monitoring and review), its content, skills, teaching, learning and assessment, and '
             'benchmark standards for the bachelor\'s degree with honours at threshold (third class), typical (lower to upper second) and excellent (first) standards, '
             'with a fourth postgraduate column for master\'s study. It carries three cross-cutting themes (equality, diversity and inclusion; education for sustainable '
             'development; entrepreneurship and enterprise education, with employability) and a section on accessibility, cites the FHEQ and FQHEIS at levels 6/10 '
             'and 7/11, and sets the subject beside the Early Childhood Studies Degrees Network and its optional Level 6 graduate practitioner competencies. The held '
             'text also carries the network\'s 2026 competencies document as an appendix, excluded here (Part E).'))

S2 = dict(
    governs=('what an Early Childhood Studies graduate can be expected to know, do and understand at the end of their studies, and the nature and characteristics '
             'of awards in the subject, with standards for honours and postgraduate study (D1, front matter: About this Statement; 1.16; 4.1)'),
    awards=[HON, MAS, 'foundation degrees, top-ups and doctorates named as courses it can apply to (1.6, 2.15, 4.2)'],
    levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope='"T he ECS Subject Benchmark Statement can apply to the full range of degree courses offered within early childhood, which can include foundation degrees; BA (Hons) t op ups as a progression from f oundation degrees; BA (Hons) full or part-time degrees; master’s and doctorate provision." (D1, 1.6)',
    statedSubjects=[
        dict(name='Early Childhood Studies', locator='(D1, title; 1.1; 1.2)', kind='subject',
             codes=[dict(scheme='hecos', code='100457', label='early childhood studies'), dict(scheme='cah', code='CAH15-04-02', label='childhood and youth studies')]),
        dict(name='childhood studies degrees', locator='(D1, 4.2)', kind='programme title',
             codes=[dict(scheme='hecos', code='100456', label='childhood studies')]),
        dict(name='foundation degrees; BA (Hons) top-ups; BA (Hons) full or part-time; master\'s and doctorate provision', locator='(D1, 1.6; 2.15; 4.2)', kind='programme title',
             codes=[dict(scheme='hecos', code='100457', label='early childhood studies')]),
        dict(name='Early Childhood Graduate Practitioner Competencies (Level 6)', locator='(D1, 1.6; 1.18 to 1.20; 2.20; 2.25)', kind='specialism', codes=[]),
    ])

SECTIONS = {'1': 'Context and purposes of an Early Childhood Studies degree', '2': 'Distinctive features of an Early Childhood Studies degree',
            '3': 'Content, teaching, learning and assessment', '4': 'Benchmark standards'}
SUB = [('1.1', '1.6', 'Context'), ('1.7', '1.13', 'Purposes of an Early Childhood Studies degree'),
       ('1.14', '1.22', 'Characteristics of an Early Childhood Studies degree'), ('1.23', '1.26', 'Equality, diversity and inclusion'),
       ('1.27', '1.31', 'Education for sustainable development'), ('1.32', '1.36', 'Entrepreneurship and enterprise education'),
       ('2.1', '2.3', 'Design - defining principles'), ('2.4', '2.10', 'Accessibility'), ('2.11', '2.16', 'Progression'),
       ('2.17', '2.17', 'Flexibility'), ('2.18', '2.20', 'Partnership'), ('2.21', '2.25', 'Monitoring and review'),
       ('3.1', '3.2', 'Content'), ('3.3', '3.3', 'Subject-specific skills'), ('3.4', '3.4', 'Generic skills'),
       ('3.5', '3.11', 'Teaching and learning'), ('3.12', '3.16', 'Assessment'), ('4.1', '4.4', 'Benchmark standards')]

G = {
    '1.1': 'the first degrees in 1992 and the period the field covers', '1.2': 'an established discipline drawing on many fields',
    '1.3': 'graduate careers and further study', '1.4': 'graduates as advocates for children and families',
    '1.5': 'contested knowledge, social justice and sustainability', '1.6': 'the courses the statement can serve; the practitioner competencies',
    '1.7': 'the underlying aim: critical study of research and practice', '1.8': 'social justice, holistic development and play',
    '1.9': 'sociocultural context and holism in course structures', '1.10': 'professionalism and multi-professional practice',
    '1.11': 'students as agents of change', '1.12': 'many perspectives on childhood and rights', '1.13': 'research, enquiry and reflexivity',
    '1.14': 'shared characteristics of courses', '1.15': 'a base for postgraduate study', '1.16': "the standards as the floor for bachelor's and master's graduates",
    '1.17': 'four nations and mapping to national requirements', '1.18': 'the practitioner competencies and network membership',
    '1.19': 'competencies through assessed placements; not expected of every degree', '1.20': "practising in early years settings: the nation's rules",
    '1.21': 'language requirements where English is not the first language', '1.22': 'varied approaches; a range of perspectives',
    '1.23': 'EDI vision: questioning dominant thought', '1.24': 'EDI mission: teaching that challenges dominant knowledge',
    '1.25': 'equitable courses; placements and the age range', '1.26': 'conditions for work-based and placement learning',
    '1.27': 'ESD vision: ecological study of early childhood', '1.28': 'ESD mission: sustainability through holistic development',
    '1.29': 'ESD as an aspirational process', '1.30': 'ESD as curriculum design', '1.31': 'sustainability, citizenship and advocacy in degrees',
    '1.32': 'enterprise vision: challenging inequality, building relationships', '1.33': 'enterprise mission: innovation and social value',
    '1.34': 'research and practice informing each other', '1.35': 'enterprising behaviours and attributes', '1.36': 'opportunities to build enterprise skills',
    '2.1': 'conception to eight and holistic development', '2.2': 'interdisciplinarity and pedagogical approaches', '2.3': 'many perspectives and critical evaluation',
    '2.4': 'inclusive, accessible course design', '2.5': 'entry routes and modes of delivery', '2.6': 'digital inclusion and employability',
    '2.7': 'varied delivery and placement settings', '2.8': 'accessible, varied, authentic assessment', '2.9': 'assessment pitched at the level of study',
    '2.10': 'accessible spaces for reflection and debate', '2.11': 'progression year by year to honours', '2.12': 'joint honours',
    '2.13': "integrated master's, exit awards and Scottish degrees", '2.14': 'design for reflection and balance across disciplines',
    '2.15': 'courses served and doctoral progression', '2.16': 'suites of qualifications and placement design', '2.17': 'flexible modes of study',
    '2.18': 'theory with practice; statutory and regulatory requirements', '2.19': 'partnership across disciplines and places',
    '2.20': 'competencies, openness to applicants and the nations', '2.21': 'monitoring and periodic review', '2.22': 'externality in review',
    '2.23': 'external examining', '2.24': 'what external examiners need', '2.25': 'accreditation and network membership',
    '3.1': 'subject-specific and generic skills defined', '3.2': 'the split between kinds of skill is not sharp',
    '3.3': 'subject-specific skills of an honours graduate', '3.4': 'generic skills of an honours graduate',
    '3.5': 'what teaching and learning are designed to do', '3.6': 'growing self-directed learning', '3.7': 'independent and group study',
    '3.8': 'reflecting on childhood experience, with support', '3.9': 'engagement with practice in teaching and learning',
    '3.10': 'mentoring for assessed professional practice', '3.11': 'culturally responsive, inclusive teaching',
    '3.12': 'assessment tied to objectives; reasonable adjustments', '3.13': 'the range of assessment methods',
    '3.14': 'assessment of practice; inclusive criteria', '3.15': 'assessing professional practice', '3.16': 'range of assessment and depth of feedback',
    '4.1': 'four categories of standard', '4.2': 'how the standards are phrased; who may use them', '4.3': 'every graduate gains a measure of the skills',
    '4.4': 'skills need not be shown one by one; the standards table follows',
}
CTYPE = {'1.2': 'area', '1.9': 'area', '2.1': 'area', '2.2': 'area',
         '2.7': 'practice', '2.8': 'practice', '3.5': 'practice', '3.6': 'practice', '3.7': 'practice', '3.8': 'practice', '3.9': 'practice',
         '3.11': 'practice', '3.12': 'practice', '3.13': 'practice', '3.14': 'practice', '3.15': 'practice'}

EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points', kind='other: front matter, read for S1, S2, SB5 and SB6'),
    dict(number='none', heading='section heading lines (sections 1 to 4)', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter; professional organisations listed (Part E)'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Early Childhood Studies', kind='other: back matter; read for the edition history (S8)'),
    dict(number='Appendix', heading='Appendix: ECSDN Graduate Practitioner Competencies, March 2026', kind="other: another issuer's document appended to the held text (ECSDN, revised March 2026); the skeleton labels it advisory-group membership and a contents listing (Part E)"),
]

# ----------------------------------------------------------------- helpers
P = {}
def s(i, **k):
    P[i] = k

_HEADS = ['Equality, diversity and inclusion Vision', 'Education for sustainable development Vision', 'Entrepreneurship and enterprise education Vision',
          'Purposes of an Early Childhood Studies degree', 'Characteristics of an Early Childhood Studies degree', 'Monitoring and review',
          'Subject-specific skills', 'Teaching and learning', 'Generic skills', 'Accessibility', 'Progression', 'Flexibility', 'Partnership',
          'Assessment', 'Mission', 'Vision']

def _clean(t):
    m = _re.search(r'\s*\n\n\d+\n(?:[A-Z][^\n]{0,60}\n?)?\s*$', t)   # a page number (and a heading after it) at the very end
    if m:
        t = t[:m.start()]
    t = t.rstrip()
    changed = True
    while changed:
        changed = False
        for h in _HEADS:
            if t.endswith(' ' + h):
                t = t[:-len(h) - 1].rstrip(); changed = True
    return t

def trimmed(i):
    """span the statement without page numbers or the next sub-heading caught at its end."""
    sp = _CAND.get(i) or {'start': _COMP[i]['start'], 'end': _COMP[i]['end']}
    raw = _N[sp['start']:sp['end']]
    c = _clean(raw)
    return {} if c == raw else dict(find=c, after=sp['start'])

FW = 'qaa/fheq-2024/'

# ----------------------------------------------------------------- paragraph statements (sections 1 to 4)
def para(i, **k):
    k.update(trimmed(i))
    s(i, **k)

para('1.18', type='expectation', rung='none', force='describes', level='none', appliesTo='institutions offering the graduate practitioner competencies',
     addressee='provider', verbs=['written', 'reviewed'], about='network membership to offer the competencies', domain='none', award='none',
     para="Achieving the Level 6 graduate practitioner competencies is meant to strengthen a graduate early years workforce; the network that writes and reviews them expects any institution offering them to be a member.",
     prac="If your course offers the Level 6 practitioner competencies, the expectation is that your institution belongs to the degrees network that writes and reviews them.",
     ben=('n/a', 'a condition on the institution that offers the competencies'),
     aaw=f"Treat this as a provider expectation, not a student outcome: an institution offering the Level 6 practitioner competencies is expected to belong to the degrees network (the issuer's word is expectation, recorded as describes). Cite it as {CITE}, para 1.18. Do not claim the competencies are required of every degree or that membership is a regulatory condition. Set it beside 1.19, 2.20 and 2.25, reading Level 6 as FHEQ level 6 ({FW}4.15) only by inference.",
     aad="Raise it with a programme team weighing whether to embed the practitioner competencies. Put it as a membership condition on the institution, not a task for students. Ask: is the institution a current member, and how would the competencies be assessed on placement? Avoid presenting it to students as a requirement of their degree.")
para('1.20', type='requirement', rung='none', force='must', level='none', appliesTo='institutions that say the degree permits early years practice',
     addressee='provider', verbs=['indicate', 'ensure', 'comply'], about='compliance where a degree claims to permit early years practice', domain='none', award='none',
     para="Early childhood degrees often let students explore theory and research in practice; where an institution says its degree lets graduates practise in early years settings, it must comply with the requirements of the nation where the student studies.",
     prac="If you advertise that the degree qualifies graduates to practise in early years settings, you must meet the requirements of the UK nation where each student studies.",
     ben=('n/a', 'a duty on the awarding institution'),
     aaw=f"Treat this as a provider duty with the force must: an institution claiming that its degree permits early years practice has to meet the requirements of the student's nation. Cite it as {CITE}, para 1.20. Do not state that every early childhood degree licenses practice, or that one nation's rules apply across the UK. Set it beside 1.17, 1.25 and 2.20.",
     aad="Raise it when a programme team describes the degree as a route into early years practice. Frame it for staff as a compliance check, nation by nation. Ask: which nation's requirements does each cohort fall under, and where is the evidence that the course meets them? Do not put this duty to a student as something they must do.")
para('1.23', type='expectation', rung='none', force='should', level='none', appliesTo='undergraduate and postgraduate students of the subject',
     addressee='learner', verbs=['interrogate'], about='questioning dominant systems of thought', domain='understanding', award=[HON, MAS],
     para="Undergraduates and postgraduates should keep questioning the language, assumptions and entrenched dominant ways of thinking in ideas of knowledge and power; agency, equal rights and dignity ground social justice, and equality is both an ethical matter and a human right.",
     prac="Students at every level should be helped to keep questioning dominant ways of thinking about knowledge and power, with equality treated as an ethical and human-rights question that underpins anti-oppressive practice.",
     ben="You should keep questioning the language and assumptions of dominant ways of thinking about knowledge and power, and treat equality as a matter of ethics and human rights.",
     aaw=f"Treat this as a should-level expectation of students at undergraduate and postgraduate level, from the equality, diversity and inclusion theme. Cite it as {CITE}, para 1.23. Do not present it as a graded outcome or as a legal duty. Set it beside 1.24, the inequality row of the section 4 table (4.4.b24) and {FW}4.15.b7.",
     aad="Raise it when a student or team discusses whose knowledge a module puts first. With a student, invite them to notice the assumptions in their readings; with staff, ask where the curriculum makes room for that questioning. Ask: whose voices are missing from this topic, and why? Avoid lecturing the student or quoting the paragraph at length.")
para('1.24', type='expectation', rung='none', force='will', level='none', appliesTo='students on courses in the subject and their institutions',
     addressee='both', verbs=['challenged', 'think', 'form'], about='teaching that challenges dominant knowledge; institutional support', domain='none', award=[HON, MAS],
     para="Students at all levels meet teaching that challenges dominant knowledge and gives marginalised voices more room; they will be pushed to think critically and make their own pedagogical judgements with equality in mind, and institutions will show active systems of support.",
     prac="Teaching will challenge dominant knowledge and widen representation; students will be pushed to make their own pedagogical judgements with EDI in mind, and the institution will have proactive, inclusive support in place.",
     ben="You will be stretched to question different realities critically and reach your own judgements about teaching and care, keeping equality and inclusion in view, with support from your institution.",
     aaw=f"Treat this as a will-level expectation that binds teaching and institutional support, from the equality, diversity and inclusion theme, on undergraduate and postgraduate courses. Cite it as {CITE}, para 1.24. Do not describe it as measured attainment at a set level. Set it beside 1.23, 1.25 and 3.11.",
     aad="Raise it when reviewing how a module handles diverse perspectives, or when a student feels unsupported. For a student, say plainly that you can expect to be both challenged and supported; for staff, ask what evidence shows proactive support. Ask: where in this course are marginalised voices represented? Avoid promising a particular support service by name.")
para('1.25', type='requirement', rung='none', force='must', level='none', appliesTo='courses in the subject, their placements and their students',
     addressee='both', verbs=['respect', 'enable', 'comply', 'gaining'], about='equitable courses, critical reflection and placements from birth to eight', domain='none', award=[HON, MAS],
     para="Every degree will be meaningful, fair and grounded in scholarship and practice under social justice, and will respect each student's identity and knowledge; courses should foster personal and theoretical critical reflection across theories, practice from birth to eight and disciplines; placements meant to qualify students for early years practice must comply with each nation's guidance, while students should still gain experience across the age range and across health, social care and education.",
     prac="Courses will be equitable and respect what each student brings, and should build critical reflection across theory, practice from birth to eight and disciplines. Placements that qualify students for early years practice must meet the guidance of the student's nation, and students should still gain experience across ages and across health, social care and education.",
     ben="Your course will respect who you are and what you bring, and should help you reflect critically on theory and practice from birth to eight; you should gain placement experience across that age range and across health, social care and education.",
     aaw=f"Treat this paragraph as mixed in force: will for equitable courses that respect students' identities, should for critical reflection and for experience across birth to eight, and must for placements that qualify students for early years practice, which have to follow each nation's guidance. Cite it as {CITE}, para 1.25. Do not let the must spread to the whole paragraph or claim placements are required of every degree. Set it beside 1.20, 1.26 and 2.16.",
     aad="Raise it when planning placements, or when a student asks why they work outside early years settings. With a student, explain plainly that experience across ages and sectors is part of the design; with staff, check placement assessments against the guidance of the student's nation. Ask: does the placement plan reach the whole birth-to-eight range and more than one sector? Avoid suggesting that every student must take a qualifying placement.")
para('1.26', type='requirement', rung='none', force='must', level='none', appliesTo='courses that offer work-based or placement learning',
     addressee='provider', verbs=['offer', 'develop'], about='conditions for placements', domain='none', award='none',
     para="Where courses offer work-based or placement learning, it must be clearly defined, mentored, monitored, accessible and supervised, so that students learn how theory and practice connect in inclusive work with children and families across disciplines.",
     prac="Any placement or work-based element you offer must be clearly scoped, mentored, monitored, accessible and supervised, so that it teaches the link between theory and inclusive practice.",
     ben=('n/a', 'a duty on the course that offers placements'),
     aaw=f"Treat this as a provider duty with the force must, applying only where a course offers placement or work-based learning. Cite it as {CITE}, para 1.26. Do not claim that every course has to include placements. Set it beside 1.25, 2.16 and 3.10.",
     aad="Raise it when a team designs or reviews placement arrangements. Frame it for staff as five tests each placement has to pass: defined, mentored, monitored, accessible, supervised. Ask: which of the five is weakest in the current placements, and what evidence shows it? Avoid presenting it to students as their duty.")
para('1.31', type='expectation', rung='none', force='should', level='none', appliesTo='degrees in the subject and their graduates',
     addressee='both', verbs=['consider', 'evaluate', 'provide', 'demonstrate'], about='exploring sustainability, social justice and advocacy', domain='none', award=[HON, MAS],
     para="Drawing on the joint QAA and Advance HE sustainability guidance, students weigh the values behind ecological sustainability and can help children and communities grasp them; degrees should offer chances to explore sustainability, social justice, democratic action and advocacy from the personal to the global, so graduates show how ecology and sustainable societies link through social justice.",
     prac="The course should give students chances to explore sustainability, social justice, democratic action and advocacy at personal, professional, community, national and global scales, so that they can show how ecology and social justice connect.",
     ben="You should have chances to explore sustainability, social justice, democracy and advocacy, from your own life to the global scale, and to show how caring for the planet and fairness in society connect.",
     aaw=f"Treat this as a should-level expectation on degrees from the education for sustainable development theme, with a stated graduate result: seeing how ecology and sustainable societies link through social justice. Cite it as {CITE}, para 1.31, with the joint guidance it draws on (std:doc:qaa-advancehe-esd-2021-guidance). Do not present it as a measured threshold or a regulatory rule. Set it beside 1.27 to 1.30 and the rights and sustainability row of the section 4 table (4.4.b6).",
     aad="Raise it when a team maps where sustainability sits in the course, or a student asks why it matters in early years work. With a student, ask plainly how fairness and care for the environment meet in children's lives; with staff, ask where students act on it, not only read about it. Ask: at which scale, from personal to global, does the course give least room? Avoid treating sustainability as an add-on topic.")
para('1.33', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students and graduates of the subject',
     addressee='learner', verbs=['contribute', 'add', 'support'], about='innovation and social value', domain='generic-skill', award=[HON, MAS],
     para="Students and graduates help build a workforce that leads innovation and changes practice, relationships, settings and services; ready for change, they will be well placed to add social, cultural and economic value, and they work together to develop the sector and its standing through exchanging knowledge and practice.",
     prac="Graduates will be well placed to add social, cultural and economic value; course design can build this through leadership, innovation and knowledge exchange with the sector.",
     ben="You will be well placed to add social, cultural and economic value, helping to lead new practice and to raise the standing of early years work.",
     aaw=f"Treat this as a will-level expected outcome for students and graduates from the enterprise theme, not a graded standard. Cite it as {CITE}, para 1.33. Do not claim it sets an employment outcome a course must report. Set it beside 1.32, 1.34 to 1.36 and {FW}4.15.b9.1, with spine:6.",
     aad="Raise it when a student asks what difference their degree can make, or when a team plans enterprise and employability work. With a student, ask plainly where they see themselves adding value; with staff, ask which activities let students lead or innovate. Ask: what change in practice or in a setting could you help bring about? Avoid overpromising careers or pay.")
para('1.35', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='students of the subject',
     addressee='learner', verbs=['developing'], about='enterprising behaviours and attributes', domain='generic-skill', award=HON,
     para="Students should be building behaviours, attributes and competencies suited to early years professions at different levels, such as initiative, reflection, communication, adapting, responsibility, networking, personal effectiveness and managed risk-taking, with values such as open-mindedness, curiosity, self-efficacy and resilience.",
     prac="Students should be building enterprising behaviours (initiative, reflection, communication, adaptability, responsibility, networking, managed risk) and attributes such as curiosity, self-efficacy and resilience; plan where each is practised.",
     ben="You should be building the habits early years work needs, such as taking initiative, reflecting, communicating, adapting, taking responsibility, networking and judging risk, along with curiosity, open-mindedness and resilience.",
     aaw=f"Treat this as a should-level expectation of students from the enterprise theme, set for professional work at different levels rather than one award level. Cite it as {CITE}, para 1.35. Do not claim it lists assessed outcomes or a fixed set of competencies. Set it beside 1.36 and {FW}4.15.b9.1 (initiative and personal responsibility).",
     aad="Raise it in personal tutoring or placement review, when a student reflects on how they work. Ask the student plainly which of these habits they already show and which they want to build. Ask: when did you last take the initiative or manage a risk in practice, and what did you learn? Avoid reading the list as a checklist to tick.")
para('2.1', type='expectation', rung='none', force='should', level='none', appliesTo='degrees in the subject',
     addressee='provider', verbs=['develop', 'ensure'], about='social justice, rights and equality across childhoods', domain='none', award='none',
     para="Courses cover early childhood from conception to eight across many childhoods, a period of all-round development that is more than readiness for school; practitioners need to know how to support every child in their local setting, and degrees should know what social justice, children's rights, culture, equality, diversity and inclusion require and make sure this reaches the development, well-being, participation and learning of all childhoods.",
     prac="Degrees should build in what social justice, children's rights, children's cultures and EDI require, applied to the development, well-being, participation and learning of every childhood from conception to eight.",
     ben=('n/a', 'a requirement on how degrees are designed'),
     aaw=f"Treat this as a should-level design expectation on degrees, which also sets the field's age range at conception to eight and its focus on holistic development. Cite it as {CITE}, para 2.1. Do not narrow the field to school readiness or to the under-fives. Set it beside 1.1, 1.2, 2.2 and the rights and equity row of the section 4 table (4.4.b6).",
     aad="Raise it when a team checks whether the curriculum spans the whole age range and all childhoods. Frame it for staff as a coverage question. Ask: where does the course address children before birth, and from five to eight? Avoid giving this to a student as a duty.")
para('2.4', type='expectation', rung='none', force='will', level='none', appliesTo='course design in the subject',
     addressee='provider', verbs=['ensure', 'consider'], about='creative thinking and accessible teaching and assessment', domain='none', award='none',
     para="Course design will make sure students can think creatively and innovatively, and courses will look for ways to be inclusive and to make teaching and assessment accessible to a diverse community, which may mean decolonising the curriculum and supporting disabled students and others with diverse needs.",
     prac="Your course design will need to show how teaching and assessment are made accessible and inclusive, including support for disabled students and, where fitting, a decolonised curriculum.",
     ben=('n/a', 'a duty on course design'),
     aaw=f"Treat this as a will-level expectation on course design from the accessibility section. Cite it as {CITE}, para 2.4. Do not claim it imposes a specific legal duty or a set method such as decolonising, which the text offers as a possibility. Set it beside 2.8, 2.10 and 3.12.",
     aad="Raise it when a team reviews a module for access or when a student reports a barrier. For staff, ask how a disabled student, or one with other needs, would meet each assessment. Ask: what in this module would stop a student with different needs from taking part fully? Avoid telling the student it is their job to remove the barrier.")
para('2.7', type='expectation', rung='none', force='should', level='none', appliesTo='delivery of degrees in the subject',
     addressee='provider', verbs=['include', 'develop'], about='varied modes of delivery and placement settings', domain='none', award='none',
     para="Content should be delivered in varied ways, such as face to face, online, flipped, group and individual study, simulated classrooms or placements in a broad mix of settings, so that students gain multi- and transdisciplinary experience and understand diverse childhoods and families; nine kinds of setting are given as examples, from social care and health to forest schools and childminders.",
     prac="Plan a mix of delivery modes and of placement or simulated settings across sectors: social care, health, social enterprise, local authority, family support, charities, policy, outdoor learning, early years and schools.",
     ben=('n/a', 'a duty on how the course is delivered'),
     aaw=f"Treat this as a should-level expectation on delivery, with the listed settings as examples, not a required set. Cite it as {CITE}, para 2.7. Do not claim every listed setting has to be used. Set it beside 1.25, 2.16 and 2.19.",
     aad="Raise it when a team plans its mix of teaching modes or placement settings. Ask staff which sectors students meet beyond early years settings. Ask: could a student graduate having seen only one kind of setting? Avoid reading the list of settings as a quota.")
para('2.8', type='expectation', rung='none', force='should', level='none', appliesTo='assessment in the subject',
     addressee='provider', verbs=['reflect', 'include', 'offer'], about='accessible, varied, authentic assessment', domain='none', award='none',
     para="Assessment and dialogue should be accessible and varied so students build the academic and practice skills to understand children, families and communities; where possible tasks should mirror real situations, allow for different learners, permit reasonable adjustments, use assistive technology, offer a range of methods and keep digital skills current.",
     prac="Use varied, accessible assessment, real-world tasks where you can, room for reasonable adjustments and assistive technology, and tasks that keep students' digital skills current (section 3 gives the methods).",
     ben=('n/a', 'a duty on assessment design'),
     aaw=f"Treat this as a should-level expectation on assessment design, joining the accessibility section to employability. Cite it as {CITE}, para 2.8. Do not claim it fixes particular assessment types. Set it beside 2.9, 3.12, 3.13 and 3.14.",
     aad="Raise it when a team reviews an assessment strategy or a student asks for an adjustment. For staff, ask how each task reflects real situations and allows adjustment. Ask: which assessment here would be hardest for a disabled student, and what adjustment is ready? Avoid quoting the paragraph to a student in place of help.")
para('2.9', type='expectation', rung='none', force='should', level='none', appliesTo='assessment strategies in the subject',
     addressee='provider', verbs=['selected', 'build'], about='assessment pitched at the level of study', domain='none', award='none',
     para="Whatever the assessment strategy, it should match the level of the degree and build on the academic and vocational assessment students met before they joined.",
     prac="Match each assessment to the level of study and build on what students were assessed on before they arrived, academic or vocational.",
     ben=('n/a', 'a duty on assessment design'),
     aaw=f"Treat this as a should-level expectation that assessment is pitched at the level of study. Cite it as {CITE}, para 2.9. Do not claim it sets the level itself; take that from the framework descriptors ({FW}4.15 at level 6). Set it beside 2.8 and 3.16.",
     aad="Raise it when a team checks that tasks grow in demand year by year or serve students from vocational routes. Ask staff how first-year tasks connect with students' earlier qualifications. Ask: is this task harder than last year's in a way the level descriptor would recognise? Avoid treating it as a student duty.")
para('2.10', type='expectation', rung='none', force='should', level='none', appliesTo='physical and digital provision for the subject',
     addressee='provider', verbs=['provide', 'foster'], about='accessible spaces for reflection and debate', domain='none', award='none',
     para="Physical and digital provision should be accessible to all students and give room for reflection and debate in a climate that accepts difference and stays open to critical, research-informed discussion; this helps build a learning community of staff, students and workplace partners.",
     prac="Make physical and online spaces accessible and keep a climate where different views are welcome and debate is critical and research-informed.",
     ben=('n/a', 'a duty on the learning environment'),
     aaw=f"Treat this as a should-level expectation on the learning environment from the accessibility section. Cite it as {CITE}, para 2.10. Do not claim it sets a standard for facilities. Set it beside 2.4 and 2.8.",
     aad="Raise it when a team reviews the learning climate, or a student says their view was not welcome. For staff, ask how disagreement is handled in seminars and online. Ask: would a student with an unpopular view feel safe to voice it here? Avoid dismissing the student's experience.")
para('2.11', type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='honours students of the subject',
     addressee='learner', verbs=['progress', 'meeting', 'undertaking'], about='progress towards all the threshold skills', domain='none', award=HON,
     para="Degrees open many routes into work and study; across an honours degree (FHEQ level 6, FQHEIS level 10) each year is expected to build knowledge, expertise and experience towards meeting every threshold-level subject-specific and generic skill, and a graduate with a second-class degree or above would be expected to be ready for postgraduate study.",
     prac="Plan each year so that knowledge, expertise and experience build towards every threshold skill in the statement by graduation; a lower second or above is expected to equip graduates for postgraduate study.",
     ben="Each year of your honours course builds towards the full set of minimum skills you need at graduation, and with a second-class degree or better you would be expected to be ready for postgraduate study.",
     aaw=f"Treat this as a described expectation (the issuer writes 'it is expected'), not a must: each year builds towards all the threshold skills by the end of the honours degree, at FHEQ level 6 and FQHEIS level 10. Cite it as {CITE}, para 2.11. Do not claim a second-class degree guarantees a postgraduate place. Set it beside the threshold column of the section 4 table and {FW}4.15, with spine:6.",
     aad="Raise it when a student asks how the years fit together or whether they could go on to a master's. With a student, say plainly that each year builds towards the minimum skills for graduation; with staff, ask where each threshold skill first appears. Ask: which of the minimum skills feel least secure for you now? Avoid presenting a second-class degree as a promise of further study.")
para('2.12', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='joint honours students',
     addressee='learner', verbs=['achieve', 'add', 'complement'], about='joint honours', domain='none', award=HON,
     para="Joint honours students will reach some of the subject's specific and generic skills and add others from their other subject; the combination should also support progression to master's or doctoral study.",
     prac="Joint honours graduates will meet part of this subject's skill set alongside their other subject's; design the combination so that it supports progression to postgraduate study.",
     ben="If you study the subject within joint honours, you will gain some of its subject-specific and general skills and add others from your second subject.",
     aaw=f"Treat this as a will-level outcome for joint honours students at FHEQ level 6: they meet part of the subject's skills, not all. Cite it as {CITE}, para 2.12. Do not claim joint honours graduates have to meet every threshold item. Set it beside 4.3, 3.3 and 3.4.",
     aad="Raise it when a joint honours student asks which skills they are expected to show. Say plainly that they will cover part of this subject's skills and add others; with a team, ask which items the joint route covers. Ask: which of this subject's skills does your other subject strengthen? Avoid holding joint honours students to the full single honours list.")
para('2.14', type='expectation', rung='none', force='should', level='none', appliesTo='design of degrees in the subject',
     addressee='provider', verbs=['designed', 'encourage', 'develop', 'take'], about='design for reflection; balance across disciplines', domain='none', award='none',
     para="Degrees should be built to foster critical reflection and engagement with the field and to develop high-quality practice; teaching is expected to be balanced across disciplines rather than centred on one, such as early education, should take account of research debates and changing law and guidance, and should leave students room to move into their chosen careers.",
     prac="Design for critical reflection and high-quality practice, keep teaching balanced across disciplines rather than led by one, follow research debates and changing law and guidance, and leave room for students' career paths.",
     ben=('n/a', 'a requirement on how degrees are designed'),
     aaw=f"Treat this as a should-level design expectation: balance across disciplines, critical reflection and high-quality practice. Cite it as {CITE}, para 2.14. Do not claim a degree may centre on early education alone and still meet it. Set it beside 1.2, 2.2 and 2.16.",
     aad="Raise it when a team reviews the balance of modules across health, social care, education and other fields. Ask staff to count credits by discipline. Ask: does one discipline dominate, and what is lost if it does? Avoid giving it to a student as their duty.")
para('2.15', type='expectation', rung='none', force='should', level='none', appliesTo='courses in the subject',
     addressee='provider', verbs=['apply', 'encourages', 'develop', 'enhance'], about='range of courses served; doctoral progression', domain='none', award='none',
     para="The statement can serve the full range of courses in the field, from top-ups and full or part-time honours to master's; there should be scope to go on to doctoral study, by professional doctorate or PhD, which can advance new knowledge and practice.",
     prac="Show students a route onward to doctoral study (professional doctorate or PhD) from your honours and master's provision.",
     ben=('n/a', 'a requirement on the range of courses offered'),
     aaw=f"Treat this as a should-level expectation that courses leave a path to doctoral study, and as the statement's account of the courses it serves. Cite it as {CITE}, para 2.15. Do not claim it sets doctoral standards; doctoral level is FHEQ level 8 ({FW}4.18), which the statement does not cover. Set it beside 1.6, 2.13 and 4.2.",
     aad="Raise it when a master's team discusses progression or a student asks about a PhD. For staff, ask what research preparation opens the doctoral route. Ask: what would a graduate of this course need to apply for a doctorate? Avoid presenting doctoral entry as assured.")
para('2.16', type='expectation', rung='none', force='should', level='none', appliesTo='suites of qualifications and placement design',
     addressee='provider', verbs=['make', 'shows', 'reflect', 'consider', 'offer'], about='suites of qualifications; placement design', domain='none', award='none',
     para="Where a suite of qualifications is built, it should show how understanding of theory, research, practice, policy and law deepens, EDI and sustainability included; where placements are offered, their design and assessment should take account of what early childhood education and care needs in each UK nation, while giving multi- and transdisciplinary experience beyond early years settings and schools.",
     prac="In a ladder of awards, show how understanding deepens from step to step, including EDI and sustainability; design any placement with each UK nation's requirements in mind but reach beyond early years settings and schools.",
     ben=('n/a', 'a requirement on course and placement design'),
     aaw=f"Treat this as a should-level expectation on suites of linked qualifications and on placement design, carrying both the EDI and the sustainability themes. Cite it as {CITE}, para 2.16. Do not claim it requires every course to offer placements. Set it beside 1.25, 1.26 and 2.7, and the steps {FW}4.12, {FW}4.15 and {FW}4.17 for the levels of a suite.",
     aad="Raise it when a team designs a ladder of awards, for example foundation degree, top-up and master's. Ask staff how each step deepens understanding of EDI and sustainability. Ask: what does a student understand at the top of the suite that they did not at the bottom? Avoid giving it to students as a duty.")
para('2.19', type='expectation', rung='none', force='should', level='none', appliesTo='degrees in the subject',
     addressee='provider', verbs=['strive', 'demonstrate'], about='partnership across disciplines and places', domain='none', award='none',
     para="Partnership with multi- and transdisciplinary practice is central to degrees, foundation degrees, apprenticeships and master's courses, through placements or, where there are none, through employability work; degrees should aim to show the field's multidisciplinary nature through partners from local to international.",
     prac="Build partnerships, local to international and across disciplines, that show students the field's breadth, through placements or other employability work.",
     ben=('n/a', 'a requirement on course partnerships'),
     aaw=f"Treat this as a should-level expectation that courses show the field's multidisciplinary nature through partnerships. Cite it as {CITE}, para 2.19. Do not claim placements are compulsory; the text allows employability work instead. Set it beside 2.7, 2.18 and 2.20.",
     aad="Raise it when a team reviews its partners, or a course without placements plans employability work. Ask staff which partners sit outside early years settings. Ask: which partner gives students a view from health or social care? Avoid treating partnership as only the supply of placements.")
para('2.20', type='requirement', rung='none', force='must', level='none', appliesTo='institutions and applicants to the subject',
     addressee='both', verbs=['make', 'ensure', 'discuss'], about='openness about whether the competencies are offered', domain='none', award='none',
     para="Achieving the Level 6 competencies meets England's Level 3 requirements, with assessed practice, and strengthens a graduate-led workforce; institutions must tell prospective students clearly whether they offer the competencies, which are not expected of every degree, and students should talk through requirements for their home nation with their institution.",
     prac="Tell applicants clearly whether your course offers the graduate practitioner competencies; you must do so for transparency, and students should be able to discuss home-nation differences with you.",
     ben="Before you apply, you can expect to be told whether the course offers the graduate practitioner competencies; you should discuss any requirements for your home nation with your institution.",
     aaw=f"Treat this as a provider duty with the force must (be open with applicants about whether the competencies are offered), with a should for students to discuss home-nation requirements. Cite it as {CITE}, para 2.20. Do not claim the competencies come with every degree or that Level 6 is defined here; read it as FHEQ level 6 ({FW}4.15) by inference, and England's Level 3 as an early years qualification level, not a higher education one. Set it beside 1.18, 1.19 and 2.25.",
     aad="Raise it when an applicant or student asks whether the degree leads to recognised practitioner status. With a student, say plainly whether this course offers the competencies and suggest they check their home nation's rules; with staff, check the published course information. Ask: where does the course tell applicants whether the competencies are included? Avoid implying the competencies come with every degree.")
para('2.22', type='expectation', rung='none', force='will', level='none', appliesTo='institutions reviewing courses in the subject',
     addressee='provider', verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award='none',
     para="Externality is essential to UK quality assurance: institutions will use external reviewers in periodic review to bring an outside view of proposed changes and to make sure threshold standards are met and content suits the subject.",
     prac="Periodic review will draw on external reviewers who look at proposed changes and confirm that threshold standards are met and content fits the subject.",
     ben=('n/a', "a duty on the institution's review process"),
     aaw=f"Treat this as a will-level expectation on institutions' review processes, not on students. Cite it as {CITE}, para 2.22. Do not claim it sets the review procedure, which is each institution's own. Set it beside 2.23, 2.24 and the threshold column of the section 4 table.",
     aad="Raise it when a team prepares for periodic review. Ask staff who the external reviewers are and what they will check. Ask: what evidence will show the reviewers that threshold standards are met? Avoid raising it with students as their concern.")
para('2.24', type='expectation', rung='none', force='should', level='none', appliesTo='external examiners for the subject',
     addressee='provider', verbs=['have', 'ensure'], about="external examiners' knowledge", domain='none', award='none',
     para="External examiners should hold the specialist knowledge to assure course quality and, where relevant, placements and the graduate practitioner competencies; they should be open to varied course designs while knowing the core principles here, the kinds and levels of course and the delivery models.",
     prac="Appoint external examiners with specialist knowledge of the subject and, where relevant, of placements and the practitioner competencies, who know the statement's core principles and the range of course types and delivery.",
     ben=('n/a', 'a duty on those who appoint and brief external examiners'),
     aaw=f"Treat this as a should-level expectation on the appointment and conduct of external examiners. Cite it as {CITE}, para 2.24. Do not claim it sets a formal qualification for examiners. Set it beside 2.22, 2.23 and 2.25.",
     aad="Raise it when a team nominates an external examiner, above all for a course with the practitioner competencies. Ask staff what placement and competency experience the nominee has. Ask: could this examiner judge evidence from practice as well as written work? Avoid involving students in it.")
para('2.25', type='requirement', rung='none', force='must', level='none', appliesTo='institutions offering the graduate practitioner competencies',
     addressee='provider', verbs=['require', 'provides', 'offer'], about='network membership to offer the competencies', domain='none', award='none',
     para="Courses with professional or vocational outcomes may also need evaluation and accreditation by professional and regulatory bodies, usually through visits and reviews of student work; the degrees network advises on the competencies, and an institution must be a current member of it to offer them, embedded or as an extra certificate.",
     prac="Before offering the practitioner competencies, embedded or as an extra certificate, confirm that your institution is a current member of the degrees network: it must be.",
     ben=('n/a', 'a condition on the institution'),
     aaw=f"Treat this as a provider duty with the force must: current membership of the degrees network is a condition of offering the practitioner competencies, embedded or as an extra certificate. Cite it as {CITE}, para 2.25. Do not claim membership is needed to run an early childhood degree at all. Set it beside 1.18 and 2.20, and treat the network's own requirements as a separate document, not yet ingested.",
     aad="Raise it when a team proposes adding the competencies. Frame it for staff as a membership check before any design work. Ask: is the institution a current member, and who keeps the membership up to date? Avoid presenting this to students.")
para('3.6', type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='students of the subject',
     addressee='learner', verbs=['encouraged', 'take', 'supplement'], about='self-directed learning', domain='generic-skill', award=HON,
     para="Teaching moves towards more individual and self-directed learning; students are encouraged to take responsibility for meeting the outcomes and are expected to add to what is taught through their own enquiry and discussion.",
     prac="Shift teaching towards self-directed learning over the course; students are expected to take responsibility for the outcomes and to extend what is taught through their own enquiry.",
     ben="As your course goes on you will do more self-directed learning, and you are expected to take responsibility for reaching the outcomes, adding to what you are taught through your own reading, enquiry and discussion.",
     aaw=f"Treat this as a described expectation of students ('are expected to', recorded as describes) about growing independence across the honours degree. Cite it as {CITE}, para 3.6. Do not present it as a graded outcome. Set it beside 3.4.b17 (autonomous learning), the own-learning row of the section 4 table (4.4.b33) and {FW}4.15.b5.",
     aad="Raise it when a student relies wholly on taught sessions or asks how much independent work is expected. Put it plainly: you are expected to go beyond what is taught. Ask: what did you read or explore this week that no one set you? Avoid making it sound like a rebuke.")
para('3.8', type='requirement', rung='none', force='must', level='none', appliesTo='teaching in the subject',
     addressee='provider', verbs=['support'], about='supported reflection on one\'s own childhood', domain='none', award='none',
     para="Teaching values personal, theoretical, cultural and practice experience; there is a requirement to support students as they reflect on their own childhoods and on time in early years settings and link these to theory, building cultural competence, and emotional support is essential where such reflection is painful.",
     prac="You must support students in reflecting on their own childhoods and on practice experience and relating these to theory, and plan emotional support for when this reflection is painful.",
     ben=('n/a', 'a duty on teaching staff; the student meets its effect'),
     aaw=f"Treat this as a provider duty: the issuer's word is requirement, recorded as must. Cite it as {CITE}, para 3.8. Do not claim students must disclose personal history. Set it beside 3.5, 3.9 and 3.11.",
     aad="Raise it when a module asks students to reflect on their own childhoods. With staff, ask what emotional support is in place before the task is set. Ask: what will happen if a student finds this reflection distressing? Avoid pressing a student to share more than they choose.")
para('3.12', type='expectation', rung='none', force='should', level='none', appliesTo='assessment in the subject',
     addressee='provider', verbs=['made'], about='reasonable adjustments in assessment', domain='none', award='none',
     para="Assessment methods are tied to the learning objectives and let students show theoretical, subject-specific and generic skills and how they connect; reasonable adjustments should be made for disabled students where needed.",
     prac="Tie each assessment to its objectives, and make reasonable adjustments for disabled students where they need them.",
     ben=('n/a', 'a duty on assessment design'),
     aaw=f"Treat this as a should-level expectation that assessment makes reasonable adjustments, alongside the link between methods and objectives. Cite it as {CITE}, para 3.12. Do not claim it replaces duties under equality law, which it does not name. Set it beside 2.4, 2.8 and 3.4.b10.",
     aad="Raise it when a disabled student asks about an assessment or a team reviews its adjustments process. For staff, ask how adjustments are agreed before the deadline. Ask: does the adjusted task still let the student show the same outcome? Avoid making the student argue for what should already be in place.")
para('3.14', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='students taking the graduate practitioner competencies',
     addressee='both', verbs=['assessed', 'completing', 'encouraged', 'anticipate', 'develop'], about='assessment of practice for the competencies', domain='none', award=HON,
     para="Students may be assessed on their practice in health, social care and early years settings, and this is required for those completing the graduate practitioner competencies; varied, innovative assessment is encouraged, and criteria are explicit, inclusive and expect critical thinking to grow over time.",
     prac="If students are taking the practitioner competencies, their practice must be assessed in settings; for others, practice assessment is optional. Keep criteria explicit and inclusive and expect critical thinking to grow year on year.",
     ben="If you take the graduate practitioner competencies, your practice in settings must be assessed; you can expect clear, inclusive criteria that look for your critical thinking to grow.",
     aaw=f"Treat this as a conditional must: assessment of practice in settings is required only for students taking the graduate practitioner competencies. Cite it as {CITE}, para 3.14. Do not claim every student has to be assessed in practice. Set it beside 1.19, 2.20 and 3.15.",
     aad="Raise it when a student chooses whether to take the competencies, or a team designs practice assessment. With a student, say plainly that taking the competencies means assessed practice; with staff, ask how practice evidence is gathered and judged. Ask: are you planning to take the competencies, and do you know how your practice will be assessed? Avoid suggesting practice assessment is compulsory for everyone.")
para('3.16', type='expectation', rung='none', force='should', level='none', appliesTo='assessment feedback in the subject',
     addressee='provider', verbs=['designed', 'demonstrate', 'allow', 'reflect', 'inform'], about='depth of feedback', domain='none', award='none',
     para="The range of assessment lets students show varied skills and growing independence; feedback and feed-forward should be deep enough for students to reflect on what they achieved and shape their next steps.",
     prac="Give feedback and feed-forward with enough depth for students to reflect on their results and plan what to do next.",
     ben=('n/a', 'a duty on those who give feedback'),
     aaw=f"Treat this as a should-level expectation on the depth of assessment feedback. Cite it as {CITE}, para 3.16. Do not claim it sets turnaround times or a feedback format. Set it beside 2.9, 3.12 and the own-learning row of the section 4 table (4.4.b33).",
     aad="Raise it when a student says feedback did not help them improve, or a team reviews its feedback practice. For staff, ask whether feedback names next steps. Ask: what would you do differently next time, based on this feedback? Avoid defending the feedback before hearing the student out.")
para('4.3', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='all graduates of the subject',
     addressee='learner', verbs=['acquire', 'demonstrated', 'exhibited', 'vary'], about='every graduate gains a measure of the skills', domain='none', award=HON,
     para="All graduates of the subject should gain a measure of the skills the discipline needs, as the standards set out, though how many skills they show and how well will differ between single honours, joint honours and modules within a wider degree.",
     prac="Every graduate should gain a measure of the subject's skills; expect the range and degree to differ between single honours, joint honours and modules taken within another degree.",
     ben="You should gain a measure of the skills the subject calls for; how many you show, and how strongly, will depend on whether you study it as single honours, joint honours or modules within another degree.",
     aaw=f"Treat this as a should-level expectation that every graduate gains a measure of the subject's skills, with range and degree varying by route. Cite it as {CITE}, para 4.3. Do not claim joint or minor routes must meet every item in the table. Set it beside 2.12, 4.4 and the threshold column of the table.",
     aad="Raise it when a joint honours student or a minor-route team asks how much of the table applies. Put it plainly: you will gain some of each skill, to a degree that depends on your route. Ask: which skills does your route leave thin? Avoid holding a minor-route student to single honours expectations.")

# ----------------------------------------------------------------- 1.36: opportunities to develop (lead-in: "Students are to be provided opportunities to develop:")
L136 = [
    (1, ['identifying'], 'intuitive professional decisions and spotting opportunities', "confidence in intuitive professional decisions and in spotting opportunities",
     'a student hesitates to make decisions in practice', 'When did you trust your own judgement in practice, and how did it turn out?'),
    (2, [], 'creative problem-solving', 'creative problem-solving', 'a team plans problem-based tasks', 'What problem did you solve in a way no one had suggested?'),
    (3, [], 'innovative and strategic thinking', 'innovative, strategic thinking', 'a student plans change in a setting', 'What would you change about this setting if you were planning five years ahead?'),
    (4, [], 'negotiation, communication and critical digital literacy', 'negotiation and communication, critical digital literacy among them', 'a student weighs online sources or negotiates in practice', 'How do you check whether online information can be trusted?'),
    (5, [], 'leadership', 'leadership', 'a student is offered a chance to lead', 'Where have you had a chance to lead, and what did you learn?'),
    (6, ['develop'], 'collaborative relationships built on respect', 'collaboration among children, colleagues, employers and students that builds knowledge and trust through mutual respect', 'a team plans work with employers or children', 'Who outside your course have you learned alongside?'),
    (7, ['support'], 'open-mindedness and responsive shared learning', 'open-mindedness that values varied capabilities and knowledge and supports responsive, interdependent learning together', 'a student meets views or abilities unlike their own', "When did someone's different experience change your mind?"),
    (8, [], 'respect for each person\'s uniqueness', "recognition of, and respect for, each person's uniqueness and what they bring", 'a team reviews how inclusive its groups are', 'How does this course show it values what each person brings?'),
]
for n, vb, ab, core, when, q in L136:
    s(f'1.36.b{n}', type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='students and postgraduates of the subject',
      addressee='both', verbs=vb, about=ab, domain='generic-skill', award=[HON, MAS], forceFrom='1.36',
      para=f"Students are to be given chances to develop {core}.",
      prac=f"Build in opportunities for students to develop {core}.",
      ben=f"Your course is meant to give you chances to develop {core}.",
      aaw=f"Treat this as a provider expectation from the enterprise theme (worded 'are to be provided', recorded as describes, not must): opportunities for students and postgraduates to develop {ab}. Cite it as {CITE}, para 1.36. Do not claim it is a graduate outcome with a set level or a regulatory duty. Set it beside 1.35, the generic skills in 3.4 and {FW}4.15.b9.1.",
      aad=f"Raise it when {when}. With a student, say plainly that the course should give them room to build this; with staff, ask where these opportunities sit in the course. Ask: {q} Avoid turning it into a test the student must pass.")
P['1.36.b8'].update(find='recognition and respect of the uniqueness of each individual and the value they bring.', after=_CAND['1.36.b8']['start'])

# ----------------------------------------------------------------- 3.3 subject-specific skills and 3.4 generic skills
# lead-in (3.3, 3.4): "an ECS graduate is expected to be able to:"; recorded as will (Part E).
def outcome(i, kind, vb, ab, dom, core, row, fw, when, q, **extra):
    head = '3.3' if kind == 'subject' else '3.4'
    s(i, type='outcome', rung='none', force='will', level='fheq:6', appliesTo='honours graduates of the subject', addressee='learner',
      verbs=vb, about=ab, domain=dom, award=HON,
      para=f"Will be able to {core.replace('{own}', 'their own')}.",
      prac=f"Honours graduates in the subject will be able to {core.replace('{own}', 'their own')}.",
      ben=f"You will be able to {core.replace('{own}', 'your own')}.",
      aaw=(f"Treat this as an outcome the statement expects of every honours graduate in early childhood studies (force will), at FHEQ level 6 and FQHEIS level 10: {ab}. "
           f"Cite it as {CITE}, para {head} ({'subject-specific' if kind == 'subject' else 'generic'} skills). "
           f"Do not present it as a regulatory requirement or as a graded standard; the graded forms are in the section 4 table. Set it beside {row} and {FW}{fw}, with spine:6."),
      aad=(f"Raise it when {when}. With a student, put it in plain second-person terms as something you will be able to do by graduation; with a programme team, ask where it is taught and assessed. "
           f"Ask: {q} Avoid reading the list aloud or treating each item as needing its own module."), **extra)

SS = [
    ('3.3.b1', ['consider'], 'disciplinary perspectives on childhood', 'understanding',
     'reflect on how psychology, sociology, health, history, education and philosophy each shape the way babies, young children and childhood are understood', '4.4.b13', '4.15.b1',
     'a student struggles to see why the course draws on so many disciplines', 'Which discipline shapes your own view of childhood most, and what does another one add?'),
    ('3.3.b2', ['apply', 'recognising'], 'many perspectives on early childhood issues', 'subject-skill',
     'bring several perspectives to early childhood questions, aware that the field uses varied methods, theories, evidence and applications', '4.4.b11', '4.15.b3.1',
     'a student analyses an issue from one angle only', 'How would someone from health or social care read this issue differently?'),
    ('3.3.b3', ['use'], 'observation with reasonable adjustments', 'subject-skill',
     "observe and analyse aspects of babies' and young children's lives, with reasonable adjustments for accessibility where needed", '4.4.b18', '4.15.b2',
     'a student prepares to observe on placement or needs an adjustment to do so', 'What adjustment, if any, would help you observe and record well?'),
    ('3.3.b4', ['integrate', 'recognise'], 'integrating perspectives', 'subject-skill',
     "combine ideas and findings from the field's many perspectives and see how each treats an issue in its own way", '4.4.b11', '4.15.b3.1',
     "a student's essay lists views without bringing them together", 'Where do these perspectives agree, and where do they pull apart?'),
    ('3.3.b5', ['critique'], 'critiquing theory, practice and research', 'subject-skill',
     "critique constructively the theory, practice and research on children's development, well-being, participation and learning across diverse childhoods", '4.4.b12', '4.15.b3.2',
     'a student accepts a theory or study without question', 'What would a critic of this study say, and how fair would that be?'),
    ('3.3.b6', ['demonstrate'], 'skills for pedagogical approaches', 'knowledge',
     'show knowledge and awareness of the skills that different pedagogical approaches call for', '4.4.b17', '4.15.b1',
     'a student plans an activity with children', 'Which approach are you using, and what skill does it ask of you?'),
    ('3.3.b7', [], 'relationships with and between children', 'subject-skill',
     'understand how deep and strong relationships need to be with individual babies and children and with groups, and how to help children build relationships with each other', '4.4.b17', '4.15.b6',
     'a student reflects on relationships in a setting', 'How did you help two children build a relationship with each other?'),
    ('3.3.b8', [], 'respectful relationships with adults', 'subject-skill',
     'build and encourage relationships of mutual respect with families, colleagues, other professionals and communities', '4.4.b22', '4.15.b9.1',
     'a student works with parents or other professionals', "What did you do to earn a family's trust?"),
    ('3.3.b9', ['evaluate', 'develop'], 'own pedagogical values', 'subject-skill',
     'evaluate and develop {own} values about teaching and care', '4.4.b7', '4.15.b5',
     'a student is asked what they believe about how young children learn', 'Which value guides your practice most, and where did it come from?'),
    ('3.3.b10', ['reflect'], 'the natural environment and the outdoors', 'understanding',
     'reflect on why the natural world and time outdoors matter for how all young children and their families grow, develop, know and understand', '4.4.b6', '4.15.b1',
     'a team plans outdoor learning or a student questions its value', 'What did a child learn outdoors that they could not have learned inside?'),
    ('3.3.b11', ['explore', 'examine', 'evaluate'], 'policies, institutions and agencies', 'subject-skill',
     "explore, examine and judge critically the cultural, historical and current features of policies, institutions and agencies, local to global, and what they mean for children's development and for ideas of childhood", '4.4.b15', '4.15.b7',
     'a student studies a policy or an agency', 'How has this policy changed over time, and whose idea of childhood does it carry?'),
    ('3.3.b12', ['demonstrate'], 'the pedagogy of play', 'understanding',
     'show a strong grasp of the pedagogy of play as several disciplines see it', '4.4.b19', '4.15.b1',
     'a student plans or reviews play-based learning', 'What does play look like from a health or psychology view, not only an education one?'),
    ('3.3.b13', ['plan', 'implement'], 'planning creative learning', 'subject-skill',
     "plan, and where fitting carry out, curriculum, assessment, evaluation and improvement of creative learning, with regard to children's health and emotional well-being", '4.4.b21', '4.15.b6',
     'a student plans a learning experience', "How does your plan look after children's emotional well-being as well as their learning?"),
    ('3.3.b14', ['lead', 'support', 'work', 'demonstrate'], 'leading and teamwork', 'subject-skill',
     'lead, support and collaborate with others and understand effective teamwork with parents, carers and other professionals', '4.4.b25', '4.15.b9.1',
     'a student takes on a group or team role', 'What did you do to help the team work well with a parent or another professional?'),
    ('3.3.b15', ['demonstrate', 'plan', 'implement'], 'health, protection and safety', 'subject-skill',
     'understand how to plan for, and where fitting deliver, the protection, safety, health and well-being of children and the conditions in which they thrive', '4.4.b21', '4.15.b6',
     'safeguarding or health promotion comes up in a module or on placement', 'What conditions in this setting help children flourish, and what would you change?'),
    ('3.3.b16', ['produce'], 'arguing for better joint practice', 'subject-skill',
     'build critical arguments for improving multiagency and multi-professional practice for babies and young children', '4.4.b23', '4.15.b8',
     'a student studies a case where agencies did not work together', 'What one change would most improve how these agencies work together, and what is your evidence?'),
    ('3.3.b17', ['use'], 'observation and analysis', 'subject-skill',
     "observe and analyse aspects of babies' and young children's lives", '4.4.b18', '4.15.b2',
     'a student writes up an observation', 'What did you notice, and how do you know it was not just your assumption?'),
    ('3.3.b18', ['reflect'], 'the ethics of studying children', 'subject-skill',
     'reflect on the ethics of studying babies, young children, their families and communities', '4.4.b28', '4.15.b4',
     'a student plans research or observation with children', 'How will you know a young child is happy to take part?'),
    ('3.3.b19', ['generate', 'explore'], 'hypotheses and research questions', 'subject-skill',
     'form and test out hypotheses and research questions on early childhood, seen in its ecological context', '4.4.b26', '4.15.b7',
     'a student begins a research project', 'What exactly do you want to find out, and why does it matter for children?'),
    ('3.3.b20', ['involving', 'analyse'], 'ethical empirical study and analysis', 'subject-skill',
     'carry out ethical empirical studies with varied data collection, observation of early childhood in its ecological context among them, and analyse the data', '4.4.b27', '4.15.b6',
     'a student designs data collection', 'Which methods suit your question, and how will you keep them ethical?'),
    ('3.3.b21', ['present', 'evaluate'], 'presenting and evaluating findings', 'subject-skill',
     'present and judge research findings on early childhood', '4.4.b27', '4.15.b8',
     'a student prepares to share research results', 'How strong are your findings, and who needs to hear them?'),
    ('3.3.b22', ['demonstrate'], "interrelated contexts in children's lives", 'understanding',
     'understand critically how political, economic, cultural and ideological contexts, from local to global, act on one another in the lives of children, families and communities', '4.4.b14', '4.15.b1',
     "a student analyses a child's or family's circumstances", "How do money, politics and culture shape this family's choices?"),
    ('3.3.b23', ['recognise', 'challenge', 'embrace'], 'challenging inequality', 'subject-skill',
     'recognise and challenge inequality in society and take an anti-bias approach', '4.4.b24', '4.15.b9.2',
     'a student meets bias in materials or practice', 'Where have you seen bias in a setting, and how might you challenge it?'),
    ('3.3.b24', ['recognise', 'give', 'act'], 'agency, voice and advocacy', 'subject-skill',
     "recognise children's agency, help their voices be heard and, where fitting, advocate for babies, young children, families and communities", '4.4.b20', '4.15.b9.1',
     "a student considers how children take part in decisions", "When did a child's view change what you did?"),
]
GS = [
    ('3.4.b1', ['present'], 'presenting information', 'present information in suitable forms, online or offline, with a sense of audience', '4.4.b30', '4.15.b8',
     'a student prepares a presentation or poster', 'Who is your audience, and what do they need first?'),
    ('3.4.b2', ['demonstrate', 'develop'], 'empathy and guarding against burnout', 'show empathy and active listening and develop ways to guard against burnout from emotional labour', '4.4.b32', '4.15.b9.1',
     'a student finds placement emotionally demanding', 'What helps you recover after an emotionally heavy day?'),
    ('3.4.b3', ['offer', 'justify'], 'arguing a view from theory', 'give and defend an informed view, drawing on a range of theoretical positions', '4.4.b30', '4.15.b3.1',
     'a student writes an argued essay', 'What is your view, and which theory supports it best?'),
    ('3.4.b4', ['comprehend', 'use'], 'using data', 'understand data and use it well', '4.4.b9', '4.15.b2',
     'a student meets statistics in a report', 'What does this figure tell you, and what does it leave out?'),
    ('3.4.b5', ['communicate', 'reflect'], 'communicating and reflecting on views', "communicate with others and reflect on {own} and others' skills, beliefs, understanding and views", '4.4.b32', '4.15.b8',
     'a student reviews group work', 'What did you learn about your own beliefs from someone who disagreed?'),
    ('3.4.b6', ['generate', 'define', 'refine', 'make'], 'framing questions and judging', 'frame and sharpen questions and judge critically', '4.4.b26', '4.15.b7',
     "a student's question is too broad", 'How could you narrow this question so that it can be answered?'),
    ('3.4.b7', ['reflect', 'evaluate'], 'reaching supported conclusions', 'weigh different perspectives critically and reach well-supported conclusions', '4.4.b30', '4.15.b7',
     "a student's conclusion goes beyond the evidence", 'Which perspective does your conclusion rest on, and what would change it?'),
    ('3.4.b8', ['access', 'retrieve', 'organise', 'use', 'evaluate'], 'finding and judging sources', 'find, retrieve, organise and use varied information sources, primary sources among them, and judge critically how relevant they are', '4.4.b31', '4.15.b5',
     'a student starts a literature search', 'Why is this source the right one for your question?'),
    ('3.4.b9', ['engage'], 'uncertainty in knowledge', 'engage with research and practice and with the uncertainty of knowledge still being built', '4.4.b12', '4.15.b4',
     'a student is unsettled that research disagrees', 'What would you do in practice when the research does not agree?'),
    ('3.4.b10', ['use', 'converse', 'debate', 'negotiate', 'persuade', 'challenge'], 'communicating to debate and persuade', "use communication skills to talk, debate, negotiate, persuade and challenge others' ideas, with reasonable adjustments for disabled students where needed", '4.4.b30', '4.15.b8',
     'a student prepares for a debate or a hard conversation on placement', "How would you challenge a colleague's idea respectfully?"),
    ('3.4.b11', ['have'], 'leading and collaborating', 'lead and collaborate with others with insight and confidence', '4.4.b25', '4.15.b9.1',
     'a student takes a lead in a group task', 'What did you do as a leader that helped the group?'),
    ('3.4.b12', ['shape', 'form'], 'context and interpersonal factors', 'be alert to contextual and interpersonal factors, seeing how complex influences shape behaviour and interaction and give rise to problems and conflict', '4.4.b14', '4.15.b9.2',
     'conflict arises in a group or a setting', 'What lay behind this conflict, beyond the people involved?'),
    ('3.4.b13', ['enhancing', 'maximise'], 'cooperation', 'see the value of cooperation in making individual skills more effective', '4.4.b22', '4.15.b9.1',
     'a student prefers to work alone', 'What could the group do that you could not do alone?'),
    ('3.4.b14', ['write'], 'writing for different purposes', 'write for varied purposes, such as persuading, explaining, describing, evaluating, recounting, summarising and hypothesising', '4.4.b30', '4.15.b8',
     'a student plans a written task', 'What is this piece of writing for, and does its form fit that purpose?'),
    ('3.4.b15', ['engage'], 'critical evaluation and analysis', 'evaluate and analyse critically', '4.4.b12', '4.15.b7',
     "a student's work describes more than it analyses", 'What is your own judgement here, beyond the description?'),
    ('3.4.b16', ['use', 'reflect'], 'digital technology and social media', 'use digital technology and social media appropriately in different contexts and reflect on that use', '4.4.b34', '4.15.b9.3',
     'a student uses social media in study or on placement', 'How would a family feel about the way you used that platform?'),
    ('3.4.b17', ['become', 'develop'], 'autonomy and resilience', 'become a learner who works autonomously, growing in independence, resilience, responsibility and pragmatism', '4.4.b33', '4.15.b5',
     'a student asks how to study more independently', 'What did you decide about your learning this week without being told?'),
]
for i, vb, ab, dom, core, row, fw, when, q in SS:
    outcome(i, 'subject', vb, ab, dom, core, row, fw, when, q)
for i, vb, ab, core, row, fw, when, q in GS:
    outcome(i, 'generic', vb, ab, 'generic-skill', core, row, fw, when, q)
# skeleton corrections: 3.3.b11 runs across a page break; 3.3.b24 and 3.4.b17 caught the next heading
_b11 = _CAND['3.3.b11']['start']
_e11 = _N.index('concept of childhood more widely', _b11) + len('concept of childhood more widely')
P['3.3.b11'].update(find=_N[_b11:_e11], after=_b11)
P['3.3.b24'].update(find='recognise agency, give voice to and, where appropriate, act as an advocate for babies, young children, families and communities.', after=_CAND['3.3.b24']['start'])
P['3.4.b17'].update(find='become more independent, resilient, responsible and pragmatic and develop as an autonomous learner.', after=_CAND['3.4.b17']['start'])
for _i in ('3.3.b7', '3.3.b8'):
    P[_i]['forceFrom'] = '3.3'

# ----------------------------------------------------------------- section 4 table: four columns per row
# Rows in the issuer's order; each row: id, domain, about, the cell-start phrases (threshold, typical, excellent, postgraduate),
# our cores (verb phrases after "will"), the FHEQ level 6 item, the Annex D row, the FHEQ level 7 item, when to raise it, a question.
RUNGS = ['threshold', 'typical', 'excellent', 'postgraduate']
ROWS = [
    ('b1', 'knowledge', 'the conceptual foundations of the field',
     ['understand the conceptual underpinnings of e arly', 'understand the conceptual underpinnings of e arly', 'understand critically the conceptual', 'detailed and accurate knowledge and understanding, showing'],
     ['understand the core ideas on which early childhood studies is built as a field',
      "understand those core ideas together with where the field came from, how it grew and where it falls short",
      "understand critically the field's founding ideas, its origins, growth and limits",
      "show detailed, accurate and critically engaged knowledge of the field's founding ideas, origins, growth and limits"],
     '4.15.b1', 'knowledge/r2', '4.17.b1', 'a student asks what holds the field together', 'What idea sits at the centre of early childhood studies for you, and where did it come from?'),
    ('b2', 'knowledge', 'babies, young children and diverse childhoods through many disciplines',
     ['have a basic understanding of babies', 'demonstrate systematic knowledge and critical understanding of babies', 'demonstrate in-depth, systematic knowledge and consistently critical understanding of babies', 'well-developed critical engagement with theoretical knowledge'],
     ['have a basic grasp of babies, young children and the many forms childhood takes, at home and worldwide, through the disciplines that study them, from psychology and sociology to law, politics and economics',
      'know babies, young children and diverse childhoods systematically and understand them critically, at home and worldwide, through every disciplinary lens the field uses',
      'know babies, young children and diverse childhoods in depth and systematically, and understand them with consistent criticality, through every lens the field uses',
      'engage critically with theory and understand babies, young children and diverse childhoods with consistent criticality through every lens the field uses'],
     '4.15.b1', 'knowledge/r1', '4.17.b1', 'a student writes about childhood from one discipline only', 'Which lens, such as decolonising or economic, have you used least, and what would it show?'),
    ('b3', 'knowledge', "the field's areas of interest and how they connect",
     ['demonstrate knowledge and understanding of the areas of interest', 'demonstrate systematic knowledge and critical understanding of the areas', 'demonstrate in-depth, systematic knowledge and consistently critical understanding of the areas', 'detailed and accurate knowledge and consistently critical engagement with the areas'],
     ['know and understand the areas of interest that feed early childhood studies across its core skills areas, and how they connect',
      'know those areas systematically and understand them and their connections critically',
      'know those areas in depth and systematically and understand them and their connections with consistent criticality',
      'show detailed, accurate knowledge of those areas and engage with them and their connections consistently and critically'],
     '4.15.b1', 'knowledge/r1', '4.17.b1', 'a team maps modules to the field\'s areas of interest', 'How does what you learned in one module change how you read another?'),
    ('b4', 'knowledge', 'policy and provision for children and families',
     ['understanding of local, national and global policy', 'a systematic knowledge and critical understanding of local', 'in-depth, systematic knowledge and significant critical', 'detailed and accurate systematic knowledge and consistently critical engagement with local'],
     ['understand local, national and global policy and the provision it makes for young children, babies, their families and communities',
      'know that policy and provision systematically and understand it critically',
      'know that policy and provision in depth and systematically, with marked critical understanding',
      'show detailed, accurate and systematic knowledge of that policy and provision and engage with it consistently and critically'],
     '4.15.b1', 'knowledge/r1', '4.17.b1', 'a student studies a policy that affects young children', 'How does this policy reach a child at home, and who decides how it is applied?'),
    ('b5', 'knowledge', 'working across professions, agencies and cultures',
     ['understanding of multi- professional', 'a working knowledge of the importance of', 'a critical working knowledge of the importance of', 'a well-developed critical engagement with the importance'],
     ['understand how working across professions, agencies and cultures can make life better for babies, young children, their families and communities',
      'have a working knowledge of why such joint working matters and of the challenges and limits it meets',
      'have a critical working knowledge of why such joint working matters and of its challenges and limits',
      'engage critically and in depth with the value, challenges and limits of such joint working'],
     '4.15.b1', 'knowledge/r2', '4.17.b1', 'a student meets health, social care and education staff working on one case', 'What made this joint work succeed or stall?'),
    ('b6', 'knowledge', 'rights, diversity, equity, justice, sustainability and inclusion in practice',
     ['awareness of issues in relation to human rights', 'a good knowledge of issues', 'excellent knowledge of issues', 'Synthesizing of knowledge'],
     ['be aware of issues of equity, diversity, inclusion, human rights, social justice and sustainability when working with babies, young children, families and communities',
      'have a good knowledge of those issues', 'have excellent knowledge of those issues',
      'synthesise knowledge and understanding of those issues in ways that lead to original thinking'],
     '4.15.b4', 'knowledge/r2', '4.17.b1', 'a student or team considers fairness, rights or sustainability in a setting', 'Which of these issues did you notice in your last placement, and what did you do?'),
    ('b7', 'knowledge', 'pedagogical approaches and values',
     ['knowledge and understanding of pedagogical approaches for working', 'a working knowledge and understanding of pedagogical approaches/values', 'a critical working knowledge and understanding of pedagogical', 'detailed and accurate knowledge and understanding showing critical engagement with the pedagogical'],
     ['know and understand pedagogical approaches for work with babies, young children, families and communities',
      'have a working knowledge and understanding of those approaches and the values behind them',
      'have a critical working knowledge and understanding of those approaches and values',
      'show detailed, accurate and critically engaged knowledge of those approaches and values'],
     '4.15.b1', 'knowledge/r2', '4.17.b1', 'a student compares ways of working with young children', 'Which approach fits your values best, and what are its limits?'),
    ('b8', 'understanding', "ethics, economics, politics, culture and ideology in children's lives",
     ['demonstrate a critical understanding of the links', 'demonstrate a well-developed critical understanding of the links', 'have a highly developed critical understanding of the links', 'have an excellent critical engagement with the links'],
     ['understand critically how ethics, economics, politics, culture and ideology connect in the lives of young children, babies and their families and communities',
      'understand those connections critically, in a well-developed way', 'understand those connections critically, to a highly developed degree',
      'engage with those connections critically, to an excellent degree'],
     '4.15.b1', 'knowledge/r2', '4.17.b1', "a student explains a family's situation by one factor alone", 'How do money, politics and belief combine in this family\'s situation?'),
    ('b9', 'knowledge', 'methods for systematic study and research',
     ['knowledge of the methods required', 'a good working knowledge of the methods', 'excellent and explicit working knowledge', 'a critically reflexive evaluation of the methods'],
     ['know the methods needed to study and research children and childhood systematically', 'have a good working knowledge of those methods',
      'have an excellent and explicit working knowledge of those methods', 'evaluate those methods critically and reflexively'],
     '4.15.b2', 'knowledge/r3', '4.17.b2', 'a student chooses a research method', 'Why is this method right for studying children, and what would it miss?'),
    ('b10', 'subject-skill', 'reasoning about theory, policy, practice and evidence',
     ['reason clearly, and demonstrate', 'reason clearly, understand the role', 'have a high-level ability to reason clearly', 'have an excellent ability to reason clearly'],
     ['reason clearly and show how theory, policy, practice and evidence relate',
      'reason clearly, understand what theory, policy, practice and evidence each contribute, and judge arguments in the field critically',
      'reason clearly to a high level, understand the part played by theory, policy, practice and evidence, and judge arguments in the field critically',
      'reason clearly to an excellent level, engage critically with the part played by theory, policy, practice and evidence, and judge arguments in the field critically'],
     '4.15.b3.1', 'cognitive/r2', '4.17.b5', 'a student argues from opinion rather than evidence', 'What evidence and which policy support this point, and does practice bear it out?'),
    ('b11', 'subject-skill', 'taking up theoretical perspectives',
     ['be able to adopt a range of theoretical perspectives', 'be able to adopt a range of theoretical perspectives', 'have a high-level ability to adopt multiple', 'have an excellent ability to adopt multiple'],
     ['take up a range of theoretical perspectives on diverse childhoods', 'take up a range of such perspectives and analyse systematically how they relate',
      'take up many perspectives on early childhood to a high level and analyse systematically how they relate',
      'take up many perspectives on early childhood to an excellent level and analyse critically how they relate'],
     '4.15.b7', 'cognitive/r2', '4.17.b4.1', 'a student uses one theory for everything', 'How would a second theory explain the same behaviour?'),
    ('b12', 'subject-skill', 'critiquing theory, practice and research',
     ['constructively critique theories, practice and research in the area', 'analyse and constructively critique', 'have a high-level ability to analyse and constructively', 'have an excellent ability to critically analyse and constructively'],
     ['critique theory, practice and research in the field constructively', 'analyse theory, practice and research in the field and critique them constructively',
      'analyse and constructively critique theory, practice and research to a high level',
      'analyse critically and critique constructively theory, practice and research, to an excellent level'],
     '4.15.b3.2', 'cognitive/r1', '4.17.b4.1', 'a student summarises research without judging it', 'What is the strongest and the weakest point of this study?'),
    ('b13', 'subject-skill', 'reflecting on disciplinary perspectives',
     ['reflect upon a range of psychological', 'have a well-developed ability to reflect upon a range', 'have a high-level ability to reflect upon a range', 'have an excellent ability to critically reflect upon a range'],
     ['reflect on the many disciplinary perspectives on babies, young children and childhood and how each shapes understanding, from local to global',
      'reflect on those perspectives and how they shape understanding, in a well-developed way',
      'reflect on those perspectives and how they shape understanding, to a high level',
      'reflect critically on those perspectives and how they shape understanding, to an excellent level'],
     '4.15.b7', 'cognitive/r2', '4.17.b4.1', 'a student wonders why the course mixes so many disciplines', 'How does a legal view of childhood differ from a psychological one?'),
    ('b14', 'subject-skill', "contexts in young children's lives",
     ['explore critically the interrelationship between', 'have a well-developed ability to explore critically', 'have a highly developed ability to explore critically', 'have an excellent ability to explore critically'],
     ['explore critically how political, economic, cultural and ideological contexts bear on one another in the lives of babies and young children',
      'explore those interrelations critically, with well-developed ability', 'explore those interrelations critically, with highly developed ability',
      'explore those interrelations critically, with excellent ability'],
     '4.15.b7', 'cognitive/r2', '4.17.b5', "a student analyses the wider forces in a child's life", 'Which context, political, economic, cultural or ideological, matters most here, and why?'),
    ('b15', 'subject-skill', 'policies, institutions and agencies',
     ['explore, examine and evaluate the significance', 'critically explore, examine and evaluate', 'have a high-level ability to explore, examine', 'have an excellent ability to critically explore, examine'],
     ['explore, examine and judge why the cultural, historical and present-day features of policies, institutions and agencies matter for babies, young children and childhood',
      'explore, examine and judge those features critically', 'explore, examine and judge those features to a high level',
      'explore, examine and judge those features critically, to an excellent level'],
     '4.15.b7', 'cognitive/r1', '4.17.b4.1', 'a student studies an agency or a policy', 'What does the history of this agency tell you about how it treats children now?'),
    ('b16', 'subject-skill', 'competing constructions of childhood',
     ['evaluate competing positions in relation to', 'analyse and evaluate competing positions with regards', 'have a high-level ability to analyse and evaluate competing', 'have an excellent ability to critically analyse and evaluate competing'],
     ['weigh competing views of how babies, young children and childhood are constructed by subjects, social agents, time, place and culture',
      'analyse and weigh competing views of how childhood is socially constructed across time, place and culture',
      'analyse and weigh those competing views to a high level', 'analyse critically and weigh those competing views, to an excellent level'],
     '4.15.b7', 'cognitive/r2', '4.17.b5', 'a student takes one idea of childhood for granted', 'How would childhood have been understood in another time or place?'),
    ('b17', 'subject-skill', 'skills for relational pedagogy',
     ['demonstrate knowledge and awareness of the skills needed for different relational', 'have a well-developed knowledge and awareness', 'have a high-level knowledge and awareness', 'have an excellent knowledge and awareness'],
     ['know and be aware of the skills that relational pedagogical approaches call for', 'have well-developed knowledge and awareness of those skills',
      'have high-level knowledge and awareness of those skills', 'have excellent knowledge and awareness of those skills'],
     '4.15.b6', 'practical/r1', '4.17.b3', 'a student reflects on building relationships with children', 'Which relational skill do you rely on most, and which needs work?'),
    ('b18', 'subject-skill', 'observation and analysis',
     ['use skills of observation and analysis', 'use developed skills of observation', 'have highly developed skills of observation', 'have excellent skills of observation'],
     ["observe and analyse parts of babies' and young children's lives", 'observe and analyse those lives with developed skill',
      'observe and analyse those lives with highly developed skill', 'observe and analyse those lives with excellent skill'],
     '4.15.b2', 'practical/r1', '4.17.b2', 'a student writes up an observation', 'What did you see, and what are you reading into it?'),
    ('b19', 'subject-skill', 'patterns in play, behaviour and experience',
     ['identify meaningful patterns', 'identify meaningful patterns', 'have a high-level ability to identify meaningful', 'have an excellent ability to identify meaningful'],
     ['spot meaningful patterns in play, behaviour and experience', 'spot such patterns and judge what they mean',
      'spot such patterns and judge what they mean, to a high level', 'spot such patterns and judge critically what they mean, to an excellent level'],
     '4.15.b7', 'practical/r4', '4.17.b5', 'a student reviews notes on children\'s play', 'What pattern runs through these observations, and what might it mean?'),
    ('b20', 'subject-skill', 'attunement and advocacy',
     ['demonstrate the ability to be attuned', 'have a well-developed ability to be attuned', 'have a highly developed ability to be attuned', 'have an excellent ability to be attuned'],
     ['attune to the views of babies, young children, families and communities and, where fitting, speak up for them',
      'attune to and, where fitting, advocate for babies, young children, families and communities, with well-developed ability',
      'attune to and, where fitting, advocate for babies, young children, families and communities, with highly developed ability',
      'attune to and, where fitting, advocate for babies, young children, families and communities, with excellent ability'],
     '4.15.b9.1', 'professional/r1', '4.17.b8.1', "a student considers how to represent a child's view", "When did you speak up for a child or family, and what did you base it on?"),
    ('b21', 'subject-skill', 'planning for holistic development, health, protection and safety',
     ['demonstrate the ability to plan for, and where appropriate implement, meet', 'have a well-developed ability to plan for, and where appropriate implement, meet', 'have a highly developed ability to plan for, and where appropriate implement, meet', 'have an excellent ability to plan for, and where appropriate implement, meet'],
     ['plan for, and where fitting put in place, provision that protects children, keeps them safe and healthy, supports their all-round development and well-being, and creates the conditions for them to flourish',
      "plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with well-developed ability",
      "plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with highly developed ability",
      "plan and, where fitting, put in place provision for children's all-round development, health, well-being, protection and safety, with excellent ability"],
     '4.15.b6', 'practical/r1', '4.17.b3', 'a student plans provision in a setting', "How does your plan keep children safe while letting them flourish?"),
    ('b22', 'subject-skill', 'collaboration with parents, carers and other stakeholders',
     ['demonstrate the ability to plan for, and where appropriate implement, effective', 'have a well-developed ability to plan for, and where appropriate implement, effective', 'have a highly developed ability to plan for, and where appropriate implement, effective', 'have an excellent ability to plan for, and where appropriate implement, effective'],
     ['plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders',
      'plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with well-developed ability',
      'plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with highly developed ability',
      'plan for, and where fitting carry through, effective joint work with parents, carers and other stakeholders, with excellent ability'],
     '4.15.b9.2', 'transferable/r2', '4.17.b8.2', 'a student plans work with families', 'How will you involve parents and carers from the start, not only at the end?'),
    ('b23', 'subject-skill', 'arguing for better joint professional practice',
     ['produce critical arguments for improvements', 'have a well-developed ability to produce', 'have a highly developed ability to produce', 'have an excellent ability to produce'],
     ['build critical arguments for improving multiagency, multi-professional and inter-professional practice for babies and young children',
      'build such arguments with well-developed ability', 'build such arguments with highly developed ability', 'build such arguments with excellent ability'],
     '4.15.b8', 'cognitive/r2', '4.17.b5', 'a student reviews a case where professionals did not work well together', 'What would you change in how these professionals work together, and why?'),
    ('b24', 'subject-skill', 'challenging inequality',
     ['demonstrate the ability to recognise and challenge', 'have a well-developed ability to recognise', 'have a highly developed ability to recognise', 'have an excellent ability to recognise'],
     ['recognise and challenge inequality and injustice in society and take up anti-bias, anti-oppressive approaches',
      'recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with well-developed ability',
      'recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with highly developed ability',
      'recognise and challenge inequality and injustice and take up anti-bias, anti-oppressive approaches, with excellent ability'],
     '4.15.b9.2', 'professional/r1', '4.17.b8.2', 'a student meets bias or exclusion in practice', 'What inequality did you notice, and what could you do about it?'),
    ('b25', 'subject-skill', 'leadership for transformational change',
     ['demonstrate the ability to lead, mentor', 'have a well-developed ability to lead', 'have a highly developed ability to lead', 'have professional confidence and an excellent ability'],
     ['lead, mentor, facilitate and collaborate with others to bring about transformational change',
      'lead, mentor, facilitate and collaborate with others to bring about transformational change, with well-developed ability',
      'lead, mentor, facilitate and collaborate with others to bring about transformational change, with highly developed ability',
      'show professional confidence and lead, mentor, facilitate and collaborate with others to an excellent level to bring about transformational change'],
     '4.15.b9.1', 'transferable/r4', '4.17.b8.1', 'a student leads or mentors others', 'What change did you help others make, and how did you support them?'),
    ('b26', 'subject-skill', 'research questions and research competence',
     ['pose and operationalise research questions', 'pose, operationalise and critique research questions', 'have a highly developed ability to pose', 'have an excellent ability to pose'],
     ['pose research questions about early childhood, put them into operation, and show research competence through practical and theoretical work',
      'pose, operationalise and critique research questions on early childhood and show research competence in practice and in theory',
      'pose, operationalise and critique research questions with highly developed ability, showing a good level of research competence',
      'pose, operationalise and critique research questions with excellent ability, showing highly developed research competence'],
     '4.15.b7', 'practical/r2', '4.17.b4.2', 'a student frames a research question', 'How would you turn this question into something you can measure or observe?'),
    ('b27', 'subject-skill', 'the supervised research project',
     ['initiate, design, conduct and report an empirically', 'competently initiate', 'initiate, design, conduct and report an early childhood research project under appropriate supervision with', 'independently initiate'],
     ['start, design, carry out and report a supervised empirical research project on early childhood',
      'start, design, carry out and report such a project competently, recognising what it implies and where it falls short in theory, practice and method',
      'carry out the whole project, from start to report, with a high degree of competence, recognising with highly developed ability what it implies and where it falls short',
      'carry out the whole project independently with supervision, showing high competence and reflexive engagement with what it implies and where it falls short'],
     '4.15.b6', 'practical/r2', '4.17.b6', 'a student plans or writes up their project', 'What are the limits of your project, and how do they affect what you can claim?'),
    ('b28', 'subject-skill', 'the ethics of studying children',
     ['reflect upon the ethics of studying', 'have a well-developed ability to reflect upon the ethics', 'have a high-level ability to reflect upon the ethics', 'have an excellent ability to reflect upon the ethics'],
     ['reflect on the ethics of studying babies, young children, families and communities',
      'reflect on those ethics with well-developed ability', 'reflect on those ethics with high-level ability', 'reflect on those ethics with excellent ability'],
     '4.15.b4', 'transferable/r5', '4.17.b5', 'a student plans to study children or families', 'How will you protect the children and families you study?'),
    ('b29', 'subject-skill', 'ethical principles in the research project',
     ['be aware of ethical principles', 'be aware of the complexity of ethical principles and issues, and demonstrate', 'be aware of the complexity of ethical principles and issues, and apply', 'well-considered reflexive engagement'],
     ['know the ethical principles involved and show this in personal study, above all the research project',
      'be aware of how complex ethical principles and issues are and show this in personal study, above all the research project',
      'be aware of that complexity and apply it in personal study, above all the research project',
      'engage reflexively and with care with that complexity and synthesise it in personal study, above all the research project'],
     '4.15.b6', 'professional/r2', '4.17.b6', 'a student prepares an ethics application', 'Which ethical issue in your project is hardest, and how will you handle it?'),
    ('b30', 'generic-skill', 'arguing a point of view from theory',
     ['present a range of theoretical positions', 'present a wide range of theoretical positions', 'present a wide range of theoretical positions', 'detailed and accurate knowledge of a wide range'],
     ['set out a range of theoretical positions and give and defend a point of view',
      'set out a wide range of positions and give and defend a well-informed view',
      'set out a wide range of positions and give and defend a well-informed and insightful view',
      'know a wide range of positions in accurate detail and articulate and defend a well-informed, insightful view'],
     '4.15.b8', 'cognitive/r2', '4.17.b5', 'a student presents an argument', 'What is your position, and which theory would challenge it?'),
    ('b31', 'generic-skill', 'using sources of information',
     ['use a range of sources of information', 'use a range of sources of information critically', 'use a wide range of sources', 'engage with a wide range of sources'],
     ['draw on a range of information sources', 'draw on a range of information sources critically',
      'draw on a wide range of information sources critically and with insight', 'engage critically and with insight with a wide range of information sources'],
     '4.15.b5', 'cognitive/r1', '4.17.b4.1', 'a student builds a reading list', 'Why do you trust this source, and what would make you doubt it?'),
    ('b32', 'generic-skill', 'listening and reflecting on skills and views',
     ['listen carefully to others and reflect upon', 'listen carefully to others and critically reflect', 'listen carefully to others and reflect critically and insightfully', 'listen carefully to others and reflect critically and analytically'],
     ["listen carefully and reflect on {own} and others' skills and views", "listen carefully and reflect critically on {own} and others' skills and views",
      "listen carefully and reflect critically and with insight on {own} and others' skills and views", "listen carefully and reflect critically and analytically on {own} and others' skills and views"],
     '4.15.b8', 'transferable/r5', '4.17.b8.3', 'a student reviews feedback from peers', 'What did you learn from someone whose view differed from yours?'),
    ('b33', 'generic-skill', 'managing own learning',
     ['recognise the need to assess', 'be able to take charge', 'show sophistication in taking charge', 'evidence sophistication in leading'],
     ['see that {own} skills need assessing and reflect on them to guide later learning',
      'take charge of {own} learning and weigh up {own} strengths and weaknesses to guide later learning',
      'take charge of {own} learning with sophistication, reflecting reflexively on {own} strengths and weaknesses for later learning',
      'lead {own} learning with sophistication, evaluating {own} strengths and weaknesses reflexively for later learning'],
     '4.15.b5', 'transferable/r3', '4.17.b8.3', 'a student plans how to improve', 'What is your strongest skill now, and which one will you work on next?'),
    ('b34', 'generic-skill', 'digital technologies and literacies',
     ['have the ability to use digital', 'be confident in the use of digital', 'show sophistication in the use of digital', 'critically and professionally engage with digital'],
     ['use digital technologies and literacies appropriately in learning, across settings, to improve provision for children',
      'use digital technologies and literacies appropriately and with confidence in learning, across settings, to improve provision for children',
      'use digital technologies and literacies with sophistication in learning, across settings, to improve provision for children',
      'engage critically, professionally and with sophistication with digital technologies and literacies in learning, across settings, to improve provision for children'],
     '4.15.b9.3', 'transferable/r1', '4.17.b7', 'a student uses digital tools with children or in study', 'How did a digital tool improve, or get in the way of, what you offered children?'),
]

# cut the cells from the held text: each cell runs from its start phrase to the next cell's, less page furniture and repeated row heads
_T0 = _N.index('Threshold Standard (3rd class degree)')
_TEND = _N.index('5 List of references and further resources', _T0)
_starts = []
_cur = _T0
for _r in ROWS:
    for _ph in _r[3]:
        _p = _N.index(_ph, _cur)
        _starts.append(_p); _cur = _p + 1
_NOISE = _re.compile(r'(\s*(This includes:|Subject knowledge|Subject-specific skills|Generic skills))+\s*$')
CELLS = []
for _k, _p in enumerate(_starts):
    _e = _starts[_k + 1] if _k + 1 < len(_starts) else _TEND
    _t = _N[_p:_e]
    _m = _re.search(r'\n\n\d+\n', _t)
    if _m:
        _t = _t[:_m.start()]
    _t = _NOISE.sub('', _t).rstrip()
    CELLS.append((_p, _t))

VERBS = ['understand', 'demonstrate', 'reason', 'adopt', 'analyse', 'critique', 'reflect', 'consider', 'explore', 'examine', 'evaluate', 'use', 'identify',
         'plan', 'implement', 'meet', 'promote', 'produce', 'recognise', 'challenge', 'embrace', 'lead', 'mentor', 'facilitate', 'work', 'pose',
         'operationalise', 'initiate', 'design', 'conduct', 'report', 'apply', 'synthesise', 'present', 'offer', 'justify', 'engage', 'listen', 'assess',
         'take', 'show', 'evidence', 'articulate', 'act', 'enhance', 'support', 'interrelate', 'Synthesizing']
RLAB = {'threshold': 'Threshold Standard (3rd class degree)', 'typical': 'Typical Standard (2nd class lower to 2nd class upper)',
        'excellent': 'Excellent Standard (1st class)', 'postgraduate': 'Postgraduate level'}
PARA = {'threshold': 'As the minimum for an honours award, the graduate will ', 'typical': 'At the typical standard, the honours graduate will ',
        'excellent': 'At the excellent standard, the honours graduate will ', 'postgraduate': "At the postgraduate standard, the master's student will "}
PRAC = {'threshold': ('Every honours graduate will, at the minimum, ', '; teaching and assessment need to give each student the chance to show this.'),
        'typical': ('At the typical standard, honours graduates will ', '; marking criteria can use this to tell typical work from the threshold in the same row.'),
        'excellent': ('At the excellent standard, honours graduates will ', '; marking criteria can use this to describe first-class work.'),
        'postgraduate': ("At the postgraduate standard, master's students will ", "; use it when setting master's outcomes, not undergraduate ones.")}
BL = {'threshold': 'To reach the minimum standard for an honours degree, ', 'typical': 'At the typical standard, which most students reach, ',
      'excellent': 'At the excellent standard, for first-class work, ', 'postgraduate': "On a master's course, at the postgraduate standard, "}
DESC = {'threshold': 'the threshold, the minimum an honours graduate has to show (third-class level),',
        'typical': 'the typical standard, what most honours graduates are expected to reach (lower to upper second class),',
        'excellent': 'the excellent standard, expected of the highest achievers (first class),',
        'postgraduate': "the postgraduate standard, for master's study,"}
LEV = {'threshold': ('the bachelor\'s degree with honours', 'FHEQ level 6 (FQHEIS level 10)'), 'typical': ('the bachelor\'s degree with honours', 'FHEQ level 6 (FQHEIS level 10)'),
       'excellent': ('the bachelor\'s degree with honours', 'FHEQ level 6 (FQHEIS level 10)'), 'postgraduate': ("the master's degree", 'FHEQ level 7 (FQHEIS level 11)')}
NOT = {'threshold': 'Do not present it as a legal or regulatory requirement, or as the standard for any award other than the honours degree.',
       'typical': 'Do not present it as the minimum: the threshold cell in the same row is the floor.',
       'excellent': 'Do not present it as the minimum or as expected of every student: it describes first-class work.',
       'postgraduate': "Do not apply it to undergraduate work or present it as a regulatory requirement for master's awards."}
RNOTE = {'threshold': ' as the floor every honours graduate reaches', 'typical': ' as what most students reach, not the minimum',
         'excellent': ' as what first-class work looks like, never as the minimum', 'postgraduate': ", and only with master's students"}
AVOID = {'threshold': ' or treating the floor as the goal', 'typical': ' or presenting this column as the pass standard',
         'excellent': ' or presenting this column as the pass standard', 'postgraduate': ' or using it to judge undergraduate work'}
BAND = {'threshold': ['3rd'], 'typical': ['2.2', '2.1'], 'excellent': ['1st']}
RSUF = {'threshold': '', 'typical': '.typical', 'excellent': '.excellent', 'postgraduate': '.masters'}   # std, 18:50: the master's column is another award, not a rung (BM-BRIEF 0.2.3)
ROWNAME = {}
GRADE = {}
OUTCOMES = []
_ci = 0
for (rid, dom, ab, phs, cores, fw6, adr, fw7, when, q) in ROWS:
    base = '4.4.' + rid
    ROWNAME[base] = ab
    ids = [base + RSUF[r] for r in RUNGS]
    for k, r in enumerate(RUNGS):
        i = ids[k]
        start, text = CELLS[_ci]; _ci += 1
        core = cores[k]
        c_they = core.replace('{own}', 'their own')
        c_you = core.replace('{own}', 'your own')
        others = ', '.join(x for x in ids if x != i)
        if r == 'postgraduate':
            fwref = f'{FW}{fw7} and spine:7'
        else:
            fwref = f'{FW}{fw6}, ' + ' and '.join(f'{FW}annex-d/{adr}/{b}' for b in BAND[r]) + ', with spine:6'
        aw, lv = LEV[r]
        vb = [v for v in VERBS if _re.search(r'\b' + _re.escape(v.lower()) + r'\b', text.lower())]
        s(i, find=text, after=start,
          type=('threshold' if r == 'postgraduate' else r), rung=('threshold' if r == 'postgraduate' else r), force='threshold' if r == 'threshold' else 'will', forceFrom='4.2',
          level='fheq:7' if r == 'postgraduate' else 'fheq:6',
          appliesTo=('master\'s students in the subject' if r == 'postgraduate' else f'honours graduates at the {r} standard'),
          addressee='learner', verbs=vb, about=ab, domain=dom, award=MAS if r == 'postgraduate' else HON,
          para=f'{PARA[r]}{c_they}.',
          prac=f'{PRAC[r][0]}{c_they}{PRAC[r][1]}',
          ben=f'{BL[r]}you will {c_you}.',
          aaw=(f"Treat this as {DESC[r]} for {aw} at {lv}, in the row on {ab}. "
               f"Cite it as {CITE}, section 4, benchmark standards table, the {r} column of the row on {ab}. "
               f"{NOT[r]} Set it beside the other cells of the row ({others}) and {fwref}."),
          aad=(f"Raise it when {when}. With a student, say it plainly in the second person{RNOTE[r]}; with staff, frame it as what a module and its assessment have to let students show. "
               f"Ask: {q} Avoid reading the table cell aloud{AVOID[r]}."))
    GRADE[ids[1]] = ids[0] + '|stated'
    GRADE[ids[2]] = ids[1] + '|stated'
    OUTCOMES.append(dict(outcome=ab, threshold=ids[0], typical=ids[1], excellent=ids[2],
                         masters='qaa/early-childhood-studies-2022/' + ids[3], basis='stated', domain=dom, award=HON))

# ----------------------------------------------------------------- themes, levels, relations
TH = {'1.23': 'theme:edi', '1.24': 'theme:edi', '1.25': 'theme:edi', '1.26': 'theme:edi', '1.31': 'theme:esd', '1.33': 'theme:enterprise', '1.35': 'theme:enterprise',
      '2.4': 'theme:accessibility', '2.7': 'theme:accessibility', '2.8': 'theme:accessibility', '2.9': 'theme:accessibility', '2.10': 'theme:accessibility'}
for _n in range(1, 9):
    TH[f'1.36.b{_n}'] = 'theme:enterprise'

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.11'), dict(id='fqheis:10', role='cites', locator='D1, 2.11'),
                  dict(id='fheq:7', role='cites', locator='D1, 2.13'), dict(id='fqheis:11', role='cites', locator='D1, 2.13'),
                  dict(id='fheq:6', role='infers', locator='D1, 1.6; 1.18; 1.19; 2.20: "Level 6" of the practitioner competencies, framework not named (Part E)'),
                  dict(id='spine:6', role='infers', locator='std:ref:uk-framework R2, for the honours columns'),
                  dict(id='spine:7', role='infers', locator='std:ref:uk-framework R2, for the postgraduate column')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.11: "FHEQ Level 6; FQHEIS L evel 10" for a degree with honours)'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.13: integrated master\'s at "FHEQ Level 7; FQHEIS Level 11")'),
                      dict(**{'from': 'rung:threshold'}, to='band:3rd (qaa/fheq-2024/annex-d)', relation='labelled-as', basis='stated in the table head ("3rd class degree"); the link to Annex D is inferred (Part E)'),
                      dict(**{'from': 'rung:typical'}, to='band:2.2 to band:2.1 (qaa/fheq-2024/annex-d)', relation='labelled-as', basis='stated in the table head ("2nd class lower to 2nd class upper"); the link to Annex D is inferred (Part E)'),
                      dict(**{'from': 'rung:excellent'}, to='band:1st (qaa/fheq-2024/annex-d)', relation='labelled-as', basis='stated in the table head ("1st class"); the link to Annex D is inferred (Part E)')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.4', '1.5', '1.23', '1.24', '1.25', '1.26', '2.1', '2.16', '3.11', '3.14', '4.4']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.26', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '3.3', '3.4', '3.12']),
      dict(id='theme:esd', role='carries', carriedIn=['1.5', '1.8', '1.27', '1.28', '1.29', '1.30', '1.31', '2.16', '4.4']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.32', '1.33', '1.34', '1.35', '1.36', '2.6', '2.8', '2.19', '2.20'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-early-childhood-studies-2019-benchmarks (not yet ingested)', note='the back matter names the third edition, 2019; earlier editions 2014 and 2007'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ levels 6 and 7 (2.11, 2.13); the table heads label the rungs by degree class, the classes Annex D describes (inferred)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS levels 10 and 11 (2.11, 2.13)'),
      dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note="1.31: the definitions in 1.29 and 1.30 come from QAA's and Advance HE's ESD guidance"),
      dict(rel='refersTo', target='ECSDN Early Childhood Graduate Practitioner Competencies (not yet ingested; Part E)', note='1.6, 1.18 to 1.20, 2.20, 2.25, 3.14; the held text carries the March 2026 revision as an appendix'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance; QAA Glossary (not ingested)', note='front matter')]

# ----------------------------------------------------------------- SB sections
SB1 = ['An interdisciplinary, multi-professional field, first offered as degrees in 1992, that studies children from conception to eight and educates those who work with them and their families (D1, 1.1, 1.2, 2.1).',
       'It draws on health, education, social work, psychology, sociology, philosophy, history, cultural, legal and political studies, economics and neuroscience (D1, 1.2).',
       'Holism is its organising idea: development, well-being, participation and learning seen together and in context, with play central (D1, 1.8, 1.9, 2.1, 2.2).',
       'It speaks of many childhoods, not one, and treats childhood as contested and changing, read locally, nationally and globally (D1, 1.5, 1.12, 2.3).',
       'It is committed to social justice, children\'s rights and advocacy, and asks graduates to act as agents of change (D1, 1.4, 1.8, 1.11, 1.32).',
       'Theory and practice are linked throughout; placements are common but optional, and the Level 6 practitioner competencies are an optional route (D1, 1.19, 2.18, 2.20).',
       'Research, enquiry and reflexivity run through it, including ethical study of young children (D1, 1.13, 3.3).']
SB2 = [dict(theme='theme:edi', inThisSubject='framed as vision and mission: questioning dominant thought, anti-oppressive knowledge and practice, room for marginalised voices, respect for each student\'s identity, inclusive placements; the table carries rights, equity and anti-bias rows (D1, 1.23 to 1.26; 4.4)',
            statements=['1.23', '1.24', '1.25', '1.26', '3.3.b23', '4.4.b6', '4.4.b24']),
       dict(theme='theme:accessibility', inThisSubject='a section of its own under distinctive features: inclusive design, routes and modes of study, digital inclusion, accessible assessment with reasonable adjustments and assistive technology, accessible spaces; adjustments also in the skill lists (D1, 2.4 to 2.10; 3.3; 3.4; 3.12)',
            statements=['2.4', '2.7', '2.8', '2.9', '2.10', '3.12', '3.3.b3', '3.4.b10']),
       dict(theme='theme:esd', inThisSubject='headed Education for sustainable development: an ecological study of early childhood, sustainability through holistic development and equity, the two ESD definitions from the joint guidance, the child as a responsible citizen of the world (D1, 1.27 to 1.31); sustainability also a lens and a rights row in the table (4.4)',
            statements=['1.31', '2.16', '3.3.b10', '4.4.b2', '4.4.b6']),
       dict(theme='theme:enterprise', inThisSubject='headed Entrepreneurship and enterprise education (front matter: with employability): advocacy against inequality, innovation and social value, research and practice informing each other, enterprising behaviours and a list of opportunities to develop them (D1, 1.32 to 1.36); employability through digital inclusion, authentic assessment and partnership (2.6, 2.8, 2.19, 2.20)',
            statements=['1.33', '1.35', '1.36.b1', '1.36.b2', '1.36.b3', '1.36.b4', '1.36.b5', '1.36.b6', '1.36.b7', '1.36.b8'])]
SB3 = dict(areas=[dict(component='1.2', gloss='the contributing disciplines, from health and education to law, economics and neuroscience'),
                  dict(component='1.9', gloss='sociocultural context, family and community, play, environment, economic distribution, stress, risk, policy and law'),
                  dict(component='2.1', gloss='conception to eight, holistic development, children\'s rights, culture and EDI across many childhoods'),
                  dict(component='2.2', gloss='families, development, well-being, participation and learning; safeguarding law; pedagogical approaches')],
           practices=[dict(component='2.7', kind='teaching', gloss='face to face, online, flipped, group and individual study, simulation and placements across sectors'),
                      dict(component='3.5', kind='teaching', gloss='courses designed for ethical awareness, digital literacy, self-assessment and access to support'),
                      dict(component='3.6', kind='learning', gloss='more self-directed learning over time'),
                      dict(component='3.7', kind='learning', gloss='independent and group study through reflection, analysis, enquiry, synthesis, evaluation'),
                      dict(component='3.8', kind='teaching', gloss='supported reflection on one\'s own childhood and practice, with emotional support'),
                      dict(component='3.9', kind='learning', gloss='engagement with practice: curriculum planning, health and safety, co-production'),
                      dict(component='3.11', kind='teaching', gloss='culturally responsive, inclusive and active learning, from guided to independent'),
                      dict(component='2.8', kind='assessment', gloss='accessible, varied, real-world assessment with adjustments and digital skills'),
                      dict(component='3.12', kind='assessment', gloss='methods tied to objectives; reasonable adjustments'),
                      dict(component='3.13', kind='assessment', gloss='eighteen example methods, from examinations to vivas and dissertations'),
                      dict(component='3.14', kind='assessment', gloss='assessment of practice, required for the competencies; explicit, inclusive criteria'),
                      dict(component='3.15', kind='assessment', gloss='assessing professional practice by reflection, discussion, portfolios and observation')])
SB4 = dict(rungs=[dict(rung='threshold', leadIn='4.1', award=HON, items=34), dict(rung='typical', leadIn='4.1', award=HON, items=34),
                  dict(rung='excellent', leadIn='4.1', award=HON, items=34), dict(rung='threshold', leadIn='4.1', award=MAS, items=34)],
           rungBases=('4.1 defines four categories: threshold as the minimum to graduate with a single honours degree, typical, excellent, and postgraduate '
                      '(advanced scholarship); 4.2: the same areas at each level, typical more securely shown than threshold, excellent a high level of '
                      'proficiency. One table lists each outcome once per row under four column heads, the honours columns labelled 3rd, 2nd lower to 2nd upper, and 1st class.'),
           outcomeLists=[dict(leadIn='3.3', gloss='subject-specific skills at graduation', items=24, award=['honours']),
                         dict(leadIn='3.4', gloss='generic skills at graduation', items=17, award=['honours']),
                         dict(leadIn='1.36', gloss='opportunities to develop enterprise skills (provider expectation)', items=8, award=['honours', "master's"])],
           outcomes=OUTCOMES)
SB4A_FULL = []
SB5 = [dict(body='Early Childhood Studies Degrees Network (ECSDN)', says='writes and reviews the Level 6 graduate practitioner competencies and advises on them; institutions offering the competencies are expected (1.18) and required (2.25) to be current members (D1, 1.18, 2.25; section 5)',
            requirements='not yet ingested (Part E)'),
       dict(body='professional, statutory and regulatory bodies (none named)', says='may set requirements beside the statement and may evaluate and accredit courses with professional outcomes; some degrees let students meet statutory or regulatory requirements (D1, front matter; 2.18; 2.25; 3.10; 3.15)',
            requirements='not-applicable-by-design: no body is named'),
       dict(body='Office for Students', says="its regulatory framework does not treat the statement as a sector-recognised standard in England (D1, front matter)",
            requirements='not yet ingested (Part E)')]
SB6 = dict(themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.4', '1.5', '1.23', '1.24', '1.25', '1.26', '2.1', '2.16', '3.11', '3.14', '4.4'],
                        statements=['qaa/early-childhood-studies-2022/' + x for x in ['1.23', '1.24', '1.25', '1.26', '3.3.b23', '4.4.b6', '4.4.b24']]),
                   dict(id='theme:accessibility', named='Accessibility', carriedIn=['1.26', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '2.10', '3.3', '3.4', '3.12'],
                        statements=['qaa/early-childhood-studies-2022/' + x for x in ['2.4', '2.7', '2.8', '2.9', '2.10', '3.12', '3.3.b3', '3.4.b10']]),
                   dict(id='theme:esd', named='Education for sustainable development', carriedIn=['1.5', '1.8', '1.27', '1.28', '1.29', '1.30', '1.31', '2.16', '4.4'],
                        statements=['qaa/early-childhood-studies-2022/' + x for x in ['1.31', '2.16', '3.3.b10', '4.4.b2', '4.4.b6']]),
                   dict(id='theme:enterprise', named='Entrepreneurship and enterprise education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.32', '1.33', '1.34', '1.35', '1.36', '2.6', '2.8', '2.19', '2.20'],
                        statements=['qaa/early-childhood-studies-2022/' + x for x in ['1.33', '1.35'] + [f'1.36.b{n}' for n in range(1, 9)]])],
           frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.11', '2.13']),
                       dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.11', '2.13']),
                       dict(framework='other: "Level 6" of the practitioner competencies, framework not named; read as fheq:6 (inferred)', levels=['fheq:6'], citedIn=['1.6', '1.18', '1.19', '2.20']),
                       dict(framework="other: England's early years Level 3 (a staff qualification level, not a higher education framework)", levels=[], citedIn=['2.20'])],
           bodies=[dict(body='Early Childhood Studies Degrees Network', citedIn=['1.18', '2.25']),
                   dict(body='professional, statutory and regulatory bodies (generic)', citedIn=['front matter', '2.18', '2.25', '3.10', '3.15']),
                   dict(body='Office for Students', citedIn=['front matter'])],
           sharedDocuments=[dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named="QAA’s and Advance HE’s Education for Sustainable Development Guidance Principles", citedIn=['1.31'], role='source of the two ESD definitions in 1.29 and 1.30'),
                            dict(document='std:doc:qaa-fheq-2024-framework, Annex D (not cited by name)', named='the degree classes in the table heads: 3rd class; 2nd class lower to 2nd class upper; 1st class', citedIn=['4.4'], role='labels each honours rung by class; the link to the classification descriptions is inferred (Part E)'),
                            dict(document='ECSDN Early Childhood Graduate Practitioner Competencies (not yet ingested: listed in Part E)', named='Appendix 1: Early Childhood Graduate Practitioner Competencies', citedIn=['1.19', '2.20'], role='the optional Level 6 practice route'),
                            dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, learning and teaching, external expertise, monitoring'),
                            dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms')])

# ----------------------------------------------------------------- Part B
B1 = [dict(slug='early-childhood', definition='the period from conception to eight, including perinatal health, in which development is shaped by environment and people; more than preparation for school (D1, 1.1, 2.1)',
           beneficiaryDefinition='the years from before birth to age eight', scopeNote='the field takes in global definitions, including the first 1001 days', category='unknown', practices=['education', 'health', 'social care']),
      dict(slug='multiple-childhoods', definition='the many forms childhood takes across cultures, societies and places, studied in the plural rather than as one norm (D1, 1.5, 1.7, 2.1)',
           beneficiaryDefinition='the different ways children grow up around the world', scopeNote='used throughout the statement and its table', category='unknown', practices=['education']),
      dict(slug='threshold-standard', definition='the minimum standard needed to graduate with a single honours degree in the subject, labelled third class in the table (D1, 4.1; 1.16; 4.4)',
           beneficiaryDefinition='the least you need to show to pass an honours degree', scopeNote='honours only', category='unknown', practices=['education']),
      dict(slug='typical-standard', definition='what a typical student is expected to attain, labelled lower to upper second class (D1, 4.1; 4.4)',
           beneficiaryDefinition='what most students reach', scopeNote='honours only', category='unknown', practices=['education']),
      dict(slug='excellent-standard', definition='what the highest-attaining student is expected to achieve, labelled first class (D1, 4.1; 4.4)',
           beneficiaryDefinition='the level of first-class work', scopeNote='honours only', category='unknown', practices=['education']),
      dict(slug='postgraduate-standard', definition='what students achieve who show advanced scholarship and understand how research advances knowledge (D1, 4.1)',
           beneficiaryDefinition="what master's study asks of you", scopeNote="a fourth column in the table, for master's study", category='unknown', practices=['education']),
      dict(slug='education-for-sustainable-development', definition='both an aspirational, continuing process of tackling social, environmental and economic concerns and the building of curricula that support sustainable development (D1, 1.29, 1.30)',
           beneficiaryDefinition='learning that helps make the world fairer and more sustainable', scopeNote='definitions taken from the joint QAA and Advance HE guidance (1.31)', category='unknown', practices=['education']),
      dict(slug='subject-specific-and-generic-skills', definition='skills tied to subject knowledge or integral to the degree, set against transferable skills less tied to the subject; the split is called artificial (D1, 3.1, 3.2)',
           beneficiaryDefinition='skills for this subject and skills you can use anywhere', scopeNote='3.3 and 3.4 list them', category='unknown', practices=['education'])]
B2A = [dict(concept='early-childhood', form='early childhood', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='multiple-childhoods', form='multiple childhoods', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='typical-standard', form='typical standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='excellent-standard', form='excellent standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='postgraduate-standard', form='postgraduate standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='education-for-sustainable-development', form='Education for Sustainable Development (ESD)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='subject-specific-and-generic-skills', form='subject-specific skills; generic skills', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []; B5 = []
D3 = [dict(title='ECSDN, Early Childhood Graduate Practitioner Competencies (revised March 2026)', why='the optional Level 6 route the statement cites (1.19, 2.20); held only as an appendix inside this text; wanted as its own standards document', status='wanted'),
      dict(title='QAA Subject Benchmark Statement: Early Childhood Studies, third edition (2019)', why='the edition this one supersedes, for the change comparison', status='wanted')]

E = [
    "Held text: stan's text carries, after QAA's back matter, the ECSDN's Graduate Practitioner Competencies revised March 2026 (contents line 'Appendix: ECSDN Graduate Practitioner Competencies, March 2026'), four years after the statement's publication; excluded here as another issuer's document. The skeleton labels it 'membership of the advisory group' and a 'contents listing'. For Abbott: was the QAA PDF itself updated with this appendix, and should the competencies be ingested as their own document (D3)?",
    'New rung shape: one table with four columns, threshold (3rd class), typical (2nd lower to 2nd upper), excellent (1st) and postgraduate. The fourth (postgraduate) column is recorded as rung `threshold` for another award, master\'s at fheq:7, with the id suffix `.masters` (std, 18:50, BM-BRIEF 0.2.3: a master\'s column is another award, not a rung); its force stays `will`, from 4.2.',
    'Rung ids follow the batch 1 convention: the threshold cell is 4.4.b<n> (the table sits after 4.4, unnumbered), the others 4.4.b<n>.typical, .excellent and .masters; 34 rows, 136 cell records. The cells are cut from the held text by bm_content.py (CELLS), not by the skeleton, which held the whole table inside 4.4.',
    'gradeOf: typical to threshold and excellent to typical in each row are `stated` (the issuer pairs the cells in one row); the postgraduate cells carry no gradeOf, being for another award; SB4 outcomes list them under `postgraduate`.',
    'The typical rung spans two degree classes (lower and upper second); the honours rungs are labelled by class in the table heads, but the statement does not cite Annex D: the link to qaa/fheq-2024/annex-d is inferred (S5, SB6).',
    'Force: the honours threshold cells are `threshold` (4.1 defines the rung as the minimum to graduate); typical, excellent and postgraduate cells take 4.2\'s "is expected to be able to demonstrate", recorded as will with forceFrom 4.2. The lead-in of 3.3 and 3.4 is also "is expected to be able to", recorded as will. For Abbott: is "expected to be able to" will?',
    'Obliging words outside the five: 1.18 "an expectation" (describes); 1.36 "are to be provided" (describes, 8 items); 2.11 "it is expected" (describes); 3.6 "are expected to" (describes); 3.8 "There is a requirement" and 3.14 "This is a requirement" (must, by the batch 1 convention); 2.1 "need to"; 1.17, 1.22, 2.6 "It is important" (not recorded as statements).',
    'Mixed modals in one paragraph, recorded at the strongest with each sentence\'s own modal kept in the paraphrase: 1.25 (will, should, must), 2.20 (must, should), 1.31 and 2.12 (will, should).',
    'Plain-present or descriptive paragraphs not recorded as statements: 3.5 (courses are generally designed to ..., 5 items), 3.7, 3.9, 3.11, 3.15 and 2.21, 2.23 (what review and external examiners typically do); 3.13 lists assessment methods with "may" and is a practice component, not a statement; 1.19 and 2.20\'s "This will enable" describe the competencies\' effect.',
    'Skeleton corrections: 3.3.b6 has two sub-items (3.3.b7, 3.3.b8, marked "-" in the text), kept as their own records under the lead-in 3.3 (forceFrom), with no verbs; 3.3.b11 runs across a page break (its span holds the page number 15); 3.3.b20 holds two items run together ("... ecological context analyse data ..."); 3.3.b24 and 3.4.b17 trimmed of the next sub-heading; paragraph spans trimmed of the sub-headings and page numbers caught at their ends (1.23, 1.26, 1.31, 2.10, 2.16, 2.20, 2.25, 3.6, 3.16).',
    'Table cells cut short by the page layout: on page 21 the excellent and postgraduate cells of the policy row (4.4.b4.excellent, 4.4.b4.postgraduate) continue after the page head, so their spans end at "and provision" and "and provision for"; the remainder ("for babies, young children, families and communities") is outside the span.',
    '3.3.b3 and 3.3.b17 are near repeats (observation and analysis, the first with reasonable adjustments); both recorded.',
    'Levels: "Level 6" of the practitioner competencies (1.6, 1.18, 1.19, 2.20) names no framework; read as fheq:6 (inferred). "Level 3 requirements in England" (2.20) is an early years staff qualification level, not a higher education framework level; not mapped.',
    "Codes: hecos 100457 'early childhood studies' matches the statement's subject name (stated); CAH15-04-02 'childhood and youth studies' is the HECoS code's CAH3 parent, inferred; 'childhood studies degrees' (4.2) given hecos 100456 in statedSubjects only.",
    'Awards: the statement can apply to foundation degrees, top-ups, honours, master\'s and doctorates (1.6, 2.15, 4.2) but states standards only for honours and postgraduate (master\'s) study; awardsCovered lists those two.',
    'Section 5 lists professional organisations (SEFDEY, BECERA, EECERA, Early Childhood Forum, UNICEF, UKCHRC) as resources; excluded matter, not recorded as bodies in SB5.',
    "Patterns that differ from Psychology: a single four-column table rather than separate rung lists; a postgraduate column; rungs labelled by degree class; three cross-cutting themes framed as 'Vision' and 'Mission' with accessibility as its own section under distinctive features; a sector network (ECSDN) and an optional Level 6 practice route in place of a PSRB; no Annex D citation.",
    'S9 commentary not researched in P1.',
]
