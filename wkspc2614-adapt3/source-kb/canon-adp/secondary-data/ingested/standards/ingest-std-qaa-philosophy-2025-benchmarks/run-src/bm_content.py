# bm_content.py: run 0124, QAA Subject Benchmark Statement Philosophy (April 2025), std run agent.
# Judgement only; tools/bm_build.py builds the document and runs the checks. Keys are S4 ids under qaa/philosophy-2025/.
# Written fresh from the held text (benchmark rule 6); levels and descriptor ids from the ingested frameworks.

HON = "bachelor's with honours"
MA = "master's"
AD = 'qaa/fheq-2024/annex-d/'
CITE = 'QAA (2025), Philosophy Subject Benchmark Statement'

META = dict(
    run='0124', p1='2026-10-03 18:26',
    title='Subject Benchmark Statement Philosophy',
    heading='Subject Benchmark Statement: Philosophy (QAA, April 2025)',
    edition='April 2025', published='2025-04',
    status='current',
    supersedes='the previous Philosophy statement (named only as "the previous Subject Benchmark Statement"; 2019 minor update by the advisory group lists: Part E)',
    subjects=[
        dict(scheme='hecos', code='100337', label='philosophy', basis='stated'),
        dict(scheme='cah', code='CAH20-02-01', label='philosophy', basis='stated'),
        dict(scheme='hecos', code='101441', label='metaphysics', basis='stated'),
        dict(scheme='hecos', code='101442', label='epistemology', basis='stated'),
        dict(scheme='hecos', code='100793', label='ethics', basis='stated'),
        dict(scheme='hecos', code='100792', label='social philosophy', basis='stated'),
        dict(scheme='hecos', code='100338', label='philosophy of science', basis='stated'),
        dict(scheme='hecos', code='100791', label='mental philosophy', basis='inferred'),
    ],
    awards=[HON, MA], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, with the cross-cutting themes; this statement\'s fifth edition (D1, back matter)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what a Philosophy graduate knows and can do at the end of a single honours degree, "
                     "with a shorter list for the master's degree. Its core is two rung tables (knowledge and understanding; subject and "
                     "intellectual skills), each row given at threshold, typical and excellent, matched to third, second and first-class "
                     "degrees, plus a list of generic skills. Reach for it when designing, reviewing or describing a philosophy course or its "
                     "outcomes. It is not a curriculum, not a set of competence standards and not a regulatory requirement in England."),
    summary=("Published by QAA in April 2025, the statement describes philosophy as a pluralistic sense-making discipline, sets out the "
             "five cross-cutting themes (equity, diversity and inclusion; accessibility and the needs of disabled students; education for "
             "sustainable development; employability, enterprise and entrepreneurship education; generative artificial intelligence) and "
             "the degree's design, progression and delivery. Its benchmark standards for bachelor's degrees with honours are a knowledge table of "
             "five rows and a skills table of nine rows, each at threshold, typical and excellent, and a list of twelve generic skills; a further "
             "twelve outcomes are given for master's degrees. It cites the FHEQ and the FQHEIS levels, points providers to Annex D of the 2024 Frameworks for "
             "the degree classes and to the 2021 Advance HE and QAA guidance on education for sustainable development. No professional body "
             "accredits the subject; PSRBs are named only in general."),
    authority='reference: a sector reference point, "not a regulatory requirement" (D1, front matter); in England not a sector-recognised standard under the OfS regulatory framework; part of the current quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter: Relationship to legislation)',
)

S2 = dict(
    governs="what a Philosophy graduate can be expected to know, do and understand at the end of an honours degree and the nature of awards in the subject, with outcomes for a master's degree (D1, front matter: About this Statement; 4.1; 4.11)",
    awards=["bachelor's degrees with honours, single honours above all (4.5)", "joint and combined honours (2.9, 4.5)", "master's degrees (2.11, 4.11)", "integrated master's (described, 2.7, 2.13)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    doesNot="it does not prescribe teaching, learning or assessment or interpret legislation; it carries no statutory or regulatory requirements; its rungs are not universal competence standards (D1, front matter; 4.3)",
    statedScope='"This QAA Subject Benchmark Statement for Philosophy defines what can be expected of a graduate in terms of what they might know, do and understand at the end of their studies." (D1, front matter: About this Statement)',
    statedSubjects=[
        dict(name='Philosophy', locator='(D1, title; 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100337', label='philosophy'), dict(scheme='cah', code='CAH20-02-01', label='philosophy')]),
        dict(name='logic, metaphysics, epistemology or philosophy of mind', locator='(D1, 3.6; 4.6)', kind='specialism', codes=[dict(scheme='hecos', code='101441', label='metaphysics'), dict(scheme='hecos', code='101442', label='epistemology'), dict(scheme='hecos', code='100791', label='mental philosophy')]),
        dict(name='moral, political or social philosophy', locator='(D1, 3.6; 4.6)', kind='specialism', codes=[dict(scheme='hecos', code='100793', label='ethics'), dict(scheme='hecos', code='100792', label='social philosophy')]),
        dict(name='applied ethics', locator='(D1, 3.3)', kind='specialism', codes=[dict(scheme='hecos', code='100793', label='ethics')]),
        dict(name='aesthetics', locator='(D1, 3.6)', kind='specialism', codes=[]),
        dict(name='history and philosophy of science', locator='(D1, 3.7)', kind='programme title', codes=[dict(scheme='hecos', code='100338', label='philosophy of science')]),
        dict(name='joint programmes with Business Studies, Classical Civilisations, Economics and others', locator='(D1, 1.22)', kind='programme title', codes=[dict(scheme='hecos', code='100337', label='philosophy')]),
        dict(name='Foundation and Liberal Arts programmes that have Philosophy as a part', locator='(D1, 1.22)', kind='programme title', codes=[dict(scheme='hecos', code='100065', label='liberal arts')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Philosophy degree', '2': 'Distinctive features of the Philosophy degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.1', 'Context and purposes of a Philosophy degree'),
       ('1.2', '1.4', 'Purposes and characteristics'),
       ('1.5', '1.8', 'Equity, diversity and inclusion: Enabling potential'),
       ('1.9', '1.10', 'Equity, diversity and inclusion: Nurturing belonging and engagement'),
       ('1.11', '1.11', 'Equity, diversity and inclusion: Increasing awareness and understanding'),
       ('1.12', '1.12', 'Equity, diversity and inclusion: Developing self-reflection'),
       ('1.13', '1.16', 'Accessibility and the needs of disabled students'),
       ('1.17', '1.19', 'Education for sustainable development'),
       ('1.20', '1.27', 'Employability, enterprise and entrepreneurship education'),
       ('1.28', '1.33', 'Generative artificial intelligence'),
       ('2.1', '2.6', 'Design'), ('2.7', '2.12', 'Progression'), ('2.13', '2.14', 'Flexibility'),
       ('2.15', '2.15', 'Partnership'), ('2.16', '2.19', 'Monitoring and review'),
       ('3.1', '3.1', 'Content, structure and delivery'), ('3.2', '3.7', 'Content'),
       ('3.8', '3.9', 'Teaching and learning'),
       ('3.10', '3.11', 'Teaching and learning: Learning in Philosophy is an active process'),
       ('3.12', '3.14', 'Teaching and learning: Learning in Philosophy is progressive'),
       ('3.15', '3.19', 'Assessment'),
       ('4.1', '4.5', 'Introduction'), ('4.6', '4.7', 'Subject-specific knowledge and understanding'),
       ('4.8', '4.9', 'Subject-specific and intellectual skills'), ('4.10', '4.10', 'Generic skills'),
       ('4.11', '4.11', "Master's level")]

G = {
    '1.1': 'philosophy as sense-making that underpins other fields and joins the humanities and the sciences',
    '1.2': 'the large questions and the clarifying, dialogue-building role',
    '1.3': 'fourteen benefits of studying the subject, from analysis to applying it in policy',
    '1.4': 'ten wider social purposes of the degree, from logic training to democratic life',
    '1.5': 'little school-level philosophy, so courses serve beginners and those with a prior qualification',
    '1.6': 'varied materials, flexible activities, asynchronous options and a widening range of assessment',
    '1.7': 'a safe environment for controversial views and attention to opponents',
    '1.8': 'a co-created, inclusive community of enquiry; changing one\'s mind takes time',
    '1.9': 'diversifying a curriculum long dominated by privileged European men',
    '1.10': 'the risk of an adversarial culture; the Equality Act 2010 and the Public Sector Equality Duty',
    '1.11': 'outward-looking comparison of traditions; graduates should be adept at it',
    '1.12': 'plurality, situating one\'s own view, reflective logs',
    '1.13': 'an anticipatory approach to accessibility in three practices',
    '1.14': 'reasonable adjustments so all students feel at home',
    '1.15': 'audio and audiovisual material and library resourcing',
    '1.16': 'disabled students\' insight as a contribution to debate',
    '1.17': 'sustainability defined as a moral attribute of acts and institutions',
    '1.18': 'the UN SDGs and the 2021 ESD guidance as a core resource',
    '1.19': 'two roles: critique of the concept and resources for sustainable living',
    '1.20': 'what employability, enterprise and entrepreneurship education does',
    '1.21': 'clear thinking, logic and argument as employability skills',
    '1.22': 'joint, foundation and liberal arts programmes',
    '1.23': 'placement years, internships and years abroad',
    '1.24': 'assessments that build employability, such as policy briefs',
    '1.25': 'funding and support for social enterprise',
    '1.26': 'leadership strengths of graduates',
    '1.27': 'the sectors graduates enter',
    '1.28': 'GenAI set against the principal skills of the degree',
    '1.29': 'three formative benefits of GenAI',
    '1.30': 'four risks of GenAI to learning',
    '1.31': 'GenAI in assessment: the essay challenge and three opportunities',
    '1.32': 'two assessment risks: integrity and autonomous writing',
    '1.33': 'GenAI as more than a tool: three points of focus',
    '2.1': 'three or four levels of historical, thematic and skills modules',
    '2.2': 'first-year design at FHEQ 4 and FQHEIS 7',
    '2.3': 'second-year design at FHEQ 5 and FQHEIS 8',
    '2.4': 'final-year design at FHEQ 6 and FQHEIS 9 or 10',
    '2.5': 'interdisciplinary learning in joint and combined degrees',
    '2.6': 'philosophers teaching concepts within other disciplines\' accredited degrees',
    '2.7': 'progression through the levels towards the threshold skills',
    '2.8': 'a second or better as readiness for postgraduate study',
    '2.9': 'joint and combined students reach the core skills and add others',
    '2.10': 'early exit with a CertHE or DipHE',
    '2.11': 'the master\'s degree: advanced optional and some compulsory modules',
    '2.12': 'a merit or better as readiness for doctoral study',
    '2.13': 'typical course lengths across the UK nations; part-time credit',
    '2.14': 'modes of delivery and ways of accumulating credit',
    '2.15': 'partnership delivery through validation and franchising',
    '2.16': 'routine monitoring, periodic review and the student voice',
    '2.17': 'external reviewers in periodic review',
    '2.18': 'external examiners and threshold standards',
    '2.19': 'accreditation for courses with professional outcomes',
    '3.1': 'what this section covers',
    '3.2': 'traditions and methods of a pluralistic subject',
    '3.3': 'three typical areas of study',
    '3.4': 'traditions share features and are not to be assumed opposed',
    '3.5': 'study is necessarily selective',
    '3.6': 'five things single honours courses typically include',
    '3.7': 'joint honours, specialist courses and interdisciplinary modules',
    '3.8': 'doing philosophy; balancing knowledge with discussion and response',
    '3.9': 'student-led research, peer exchange and self-direction in every programme',
    '3.10': 'three active modes of learning in any module',
    '3.11': 'formal methods learned through graded exercises',
    '3.12': 'two orderings of progression',
    '3.13': 'two-year cycles; bringing diverse students together',
    '3.14': 'eight typical teaching and learning methods',
    '3.15': 'what the suite of assessments tests',
    '3.16': 'diverse ways of meeting learning outcomes',
    '3.17': 'co-created, reflective assessment and eleven example methods',
    '3.18': 'accessible alternatives and student-proposed assessment',
    '3.19': 'integrity through authentic assessment; transparency with technology',
    '4.1': 'the standards shown at the award of honours',
    '4.2': 'most exceed threshold; providers refer to Annex D',
    '4.3': 'rungs are not competence standards; EHRC guidance',
    '4.4': 'the three rungs defined and matched to degree classes',
    '4.5': 'rungs written for single honours; any module brings some competence',
    '4.6': 'the knowledge and understanding table: five rows at three rungs',
    '4.7': 'higher knowledge rungs include the lower',
    '4.8': 'the subject and intellectual skills table: nine rows at three rungs',
    '4.9': 'higher skill rungs include the lower',
    '4.10': 'twelve generic skills at undergraduate level',
    '4.11': 'twelve outcomes for the master\'s degree',
}

CTYPE = {'3.2': 'area', '3.3': 'area', '3.6': 'area', '3.7': 'area',
         '3.8': 'practice', '3.9': 'practice', '3.10': 'practice', '3.11': 'practice', '3.12': 'practice',
         '3.13': 'practice', '3.14': 'practice', '3.15': 'practice', '3.16': 'practice', '3.17': 'practice',
         '3.18': 'practice', '3.19': 'practice'}

EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2, SB5 and SB6'),
    dict(number='none', heading='Contents', kind='other: table of contents'),
    dict(number='section headings 1 to 4', heading='section heading lines', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for SB6 and Part E'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: back matter, read for S7 (earlier editions) and S1 (publication date)'),
]

P = {}
def s(i, **k):
    P[i] = k

# ------------------------------------------------------------------ statements outside the rung tables
s('1.11', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
  verbs=['comparing', 'assessing'], about='comparing perspectives across cultures and traditions', domain='subject-skill', award=HON,
  para="Philosophical discussion flourishes when it looks outward; teachers bring views from other cultures and traditions into materials and discussion; graduates should be skilled at comparing and judging such views; courses use varied tools so every student is heard.",
  prac="Bring views from other cultures and traditions into materials and discussion, since graduates should be skilled at comparing and judging them; use varied tools and strategies so that every student can speak and contribute.",
  ben="You should become skilled at comparing and weighing up philosophical views from different cultures and traditions.",
  aaw=f"Present this as an expectation (should) in the statement's equity, diversity and inclusion section: honours graduates ought to be skilled at weighing views from other cultures and traditions, at FHEQ level 6 (FQHEIS level 10). Cite it as {CITE}, para 1.11. Do not present it as a rung of the benchmark standards or as a regulatory duty. Set it beside 4.8.b7, 4.8.b1.excellent, theme:edi and the FHEQ descriptor qaa/fheq-2024/4.15.b7.",
  aad="Raise it when a student's reading or essay draws on one tradition only, or when a team reviews how diverse its curriculum is. To a student, say plainly that you should be able to compare and weigh views from different cultures; to staff, frame it as a curriculum and teaching expectation. Ask: Which tradition outside the one you mostly study have you read, and how would it answer your question? Avoid reading the paragraph aloud or treating it as a box to tick.")

s('1.18', type='expectation', rung='none', force='should', level='none', appliesTo='course teams in the subject', addressee='provider',
  verbs=['consulted'], about='the 2021 ESD guidance as a core resource', domain='none', award='none',
  para="The statement follows the UN Sustainable Development Goals and their priorities on climate, ecosystems, oceans, settlements, poverty and inclusion; the subject fits the skills and outcomes of the 2021 Advance HE and QAA guidance on education for sustainable development, which course teams should consult as a core resource.",
  prac="Use the Advance HE and QAA guidance on education for sustainable development (March 2021) as a core resource when you design the course; the subject aligns with its skills and outcomes, read against the UN Sustainable Development Goals.",
  ben=('n/a', 'a duty on the course team to consult a guidance document; the student meets its effect'),
  aaw=f"Present this as a should addressed to course teams: consult the 2021 Advance HE and QAA guidance on education for sustainable development as a core resource; it holds for course design at every level and is not a student outcome. Cite it as {CITE}, para 1.18, and the guidance as std:doc:qaa-advancehe-esd-2021-guidance. Do not claim it makes the guidance mandatory or sets sustainability outcomes of its own. Set it beside theme:esd and beside 1.17 and 1.19 on how the subject treats sustainability.",
  aad="Raise it with a programme team planning or reviewing where sustainability appears in the curriculum, not with a student as a requirement. Frame it for staff as the guidance the statement expects them to work from. Ask: Where in your modules do students analyse the idea of sustainability or test claims made in its name? Avoid reading the list of goals aloud and avoid presenting the guidance as binding.")

s('2.9', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='joint and combined honours students', addressee='learner',
  verbs=['achieve', 'add'], about='joint honours students reach the core skills', domain='subject-skill', award=HON,
  para="Students taking philosophy in a combined or joint degree, major and minor routes included, will reach the core of the subject-specific and generic skills the statement sets out and will add others from their other subject; they may also explore where the disciplines overlap.",
  prac="Joint and combined honours students will achieve the core subject-specific and generic skills of the statement and add skills from their other subject; plan chances for them to work across the overlap.",
  ben="If you study philosophy alongside another subject, you will gain the core philosophical and general skills described here, add skills from your other subject and may explore where the two meet.",
  aaw=f"Present this as an expected outcome (will) for joint and combined honours students: they reach the core of the specific and generic skills, not the whole single honours set, at FHEQ level 6 (FQHEIS level 10). Cite it as {CITE}, para 2.9. Do not claim the rung tables in 4.6 and 4.8 apply in full to joint honours, since 4.5 says they are written for single honours. Set it beside 4.5, the generic skills 4.10.b1 to 4.10.b12 and spine:6.",
  aad="Raise it when a joint honours student asks whether they are held to the same standard as single honours students, or when a joint programme team plans its outcomes. Tell a student plainly that you will be expected to reach the core skills, with breadth added from the other subject; frame it for staff as a question of scope. Ask: Which philosophical skills does your other subject strengthen, and which need more practice? Avoid implying a joint student must cover everything a single honours student does.")

s('2.17', type='expectation', rung='none', force='will', level='none', appliesTo='providers of the subject', addressee='provider',
  verbs=['use', 'ensure'], about='external reviewers in periodic review', domain='none', award='none',
  para="Externality is a core part of UK quality assurance; providers will bring in external reviewers during periodic review for an independent view of planned changes and to confirm that threshold standards are met and the content fits the subject.",
  prac="In periodic review, providers will involve external reviewers, who give an independent view on proposed changes and check that threshold standards are reached and the content suits philosophy.",
  ben=('n/a', 'a duty on the provider in course review'),
  aaw=f"Present this as a provider expectation (will) about periodic course review, not a student outcome and not tied to a level. Cite it as {CITE}, para 2.17. Do not claim it sets the review cycle or the form of external review, which each degree-awarding body decides. Set it beside 2.16 and 2.18 on monitoring and external examining; set it also beside the threshold cells of 4.6 and 4.8, which reviewers check.",
  aad="Raise it with a programme team or quality officer preparing a periodic review, never with a student as something they must do. Frame it as the independent check on threshold standards and on fit to the subject. Ask: Who will act as your external reviewer, and which threshold cells will you ask them to look at? Avoid reading the paragraph aloud or treating it as a regulatory rule.")

s('3.4', type='expectation', rung='none', force='should', level='none', appliesTo='anyone studying or teaching the subject', addressee='both',
  verbs=['assumed', 'engage'], about='traditions not to be assumed opposed', domain='understanding', award='none',
  para="Philosophy has many traditions, each with its own style and concerns, yet all share features such as precision, clarity and self-reflection; it should not be taken for granted that the traditions are at odds or unable to talk to each other.",
  prac="Teach the traditions as distinct but compatible: share their common stress on precision, clarity and self-reflection, and do not assume they are at odds or cannot engage productively.",
  ben="You should not assume that different philosophical traditions are opposed or cannot learn from each other; they share a concern with precision, clarity and self-reflection.",
  aaw=f"Present this as a should addressed to students and staff alike: do not treat philosophy's traditions as opposed or unable to engage; it is a principle for the degree at any level, not a rung. Cite it as {CITE}, para 3.4. Do not claim it requires every course to teach several traditions; 3.6 only values some acquaintance with another. Set it beside 3.2, 3.6 and the open-mindedness row 4.8.b7.",
  aad="Raise it when a student dismisses a whole tradition, analytic, continental or comparative, or when a team debates which traditions to teach. Say plainly to a student that you should not assume the traditions cannot talk to each other; to staff, put it as a design principle. Ask: What does the other tradition do well that yours does not? Avoid taking sides between traditions.")

s('3.8', type='requirement', rung='none', force='must', level='none', appliesTo='teaching and learning in the subject', addressee='provider',
  verbs=['balanced'], about='balancing knowledge with doing philosophy', domain='none', award='none',
  para="Programmes build the skills to do philosophy, not only to study it, so it matters that teaching models philosophical practice; time for gaining knowledge of topics and thinkers must be balanced with time in which students discuss, analyse and work out their own responses.",
  prac="Model the practice of philosophy in teaching: time spent acquiring knowledge of topics and thinkers must be balanced with time in which students discuss, analyse and work out their own responses.",
  ben=('n/a', 'a duty on the course in how teaching is balanced; the student meets its effect'),
  aaw=f"Present this as a must on the provider: teaching has to balance acquiring knowledge of topics and thinkers with students discussing, analysing and responding for themselves; it holds for teaching at every level of the degree. Cite it as {CITE}, para 3.8. Do not turn it into a student outcome or a fixed ratio of contact types. Set it beside 3.9, 3.10 and 3.14 on teaching methods and the reference framework's strand:thinking.",
  aad="Raise it with a programme or module team reviewing a teaching plan, for example one built mostly on lectures. Frame it for staff as the one teaching must in this section. Ask: Where in each week do students argue and respond, not only listen? Avoid giving it to a student as their duty.")

s('3.9', type='expectation', rung='none', force='will', level='none', appliesTo='every programme in the subject', addressee='provider',
  verbs=['incorporate', 'allow'], about='student-led research, peer exchange and self-direction', domain='none', award='none',
  para="Programmes differ in size, so the mix of online and in-person teaching and the range of topics vary; all programmes will nonetheless include some student-led research, chances to exchange ideas with peers and freedom for students to choose the questions they pursue.",
  prac="Whatever its size, every programme will include student-led research, peer exchange of ideas and room for students to direct the questions they pursue.",
  ben=('n/a', 'a duty on the programme; the student meets its effect as research, discussion and choice'),
  aaw=f"Present this as a provider expectation (will) that holds for every philosophy programme whatever its size or mode: some student-led research, peer exchange and self-chosen questions. Cite it as {CITE}, para 3.9. Do not claim it fixes how much research there is or which delivery mode is used. Set it beside 3.8, 3.17 on co-created assessment and the generic skill 4.10.b9.",
  aad="Raise it with a team designing a small or largely online programme, where peer exchange and student-led research are easiest to lose. Frame it for staff as a floor every programme keeps. Ask: Where can students choose their own question, and where do they exchange ideas with peers? Avoid presenting it to students as a task they owe.")

s('3.13', type='expectation', rung='none', force='will', level='none', appliesTo='teaching in the subject', addressee='provider',
  verbs=['involve', 'bringing'], about='bringing students of different backgrounds together', domain='none', award='none',
  para="Many departments teach some subjects in a two-year cycle, with difficulty rising towards the final years; because philosophy draws on diverse thinkers, teaching strategies will involve gathering students from different backgrounds around shared problems, and it is important to offer varied modes of discussion, online or in person.",
  prac="Teaching strategies will bring students from different backgrounds together to work on shared problems; offer several modes and occasions for discussion, online and in person, so everyone can take part.",
  ben=('n/a', 'a duty on the provider in teaching strategy'),
  aaw=f"Present this as a provider expectation (will) about teaching strategy: students of different backgrounds work together on shared problems, with varied modes of discussion; it holds across the degree, not at one level. Cite it as {CITE}, para 3.13. Do not read its 'it is important that' as a must; record it as the issuer's emphasis. Set it beside 1.7, 1.8 and 1.11 on inclusive enquiry and the generic skill 4.10.b10.",
  aad="Raise it with a team planning seminars or group work, especially where some students struggle to take part. Frame it for staff as how teaching is expected to use the range of students' backgrounds. Ask: Which discussion formats do you offer besides live seminars, and who uses them? Avoid presenting it to a student as an obligation.")

L315 = dict(type='expectation', rung='none', force='will', level='none', appliesTo='the assessment suite of every programme', addressee='provider', domain='none', award='none',
            ben=('n/a', 'a duty on the programme in designing assessment'))
def a315(k, verbs, about, x, para, prac, nb):
    s('3.15.b%d' % k, verbs=verbs, about=about, para=para, prac=prac,
      aaw=f"Present this as a provider expectation (will): every programme's assessments test {x}; it holds for assessment across the degree. Cite it as {CITE}, para 3.15, item {k}. Do not claim it names particular assessment methods; 3.17 lists methods as examples only. Set it beside {nb}.",
      aad=f"Raise it when a team maps its assessments, to check that {x} is tested somewhere in each year. Frame it for staff as coverage, not as a list of methods. Ask: Which assessment in your programme tests {x}, and how would a marker see it? Avoid putting it to a student as their duty.",
      **L315)
a315(1, [], 'assessment tests knowledge and understanding', 'knowledge and understanding',
     "Each programme's set of assessments will test students' knowledge and understanding, balanced against their competence in philosophical skills and methods.",
     "Make sure the suite of assessments will test knowledge and understanding, alongside philosophical skills and methods.",
     f"the knowledge rows 4.6.b1 to 4.6.b5 and {AD}knowledge/r1/3rd")
a315(2, ['demonstrating', 'reason'], 'assessment tests argument and analysis', 'argument and analysis',
     "Each programme's assessments will test argument and analysis: reasoning with rigour, critically, creatively and independently.",
     "Make sure the suite of assessments will test argument and analysis, showing rigorous, critical, creative and independent reasoning.",
     f"the argument row 4.8.b4, the generic skill 4.10.b9 and {AD}cognitive/r2/3rd")
a315(3, ['demonstrating', 'communicate'], 'assessment tests presentation', 'presentation',
     "Each programme's assessments will test presentation: getting ideas across clearly, reliably and effectively.",
     "Make sure the suite of assessments will test presentation: clear, reliable and effective communication.",
     f"the explaining row 4.8.b5, the generic skills 4.10.b6 and 4.10.b7 and {AD}transferable/r1/3rd")

s('3.19', type='requirement', rung='none', force='must', level='none', appliesTo='assessment in the subject', addressee='provider',
  verbs=['ensured', 'promoted'], about='transparency where technology is used in assessment', domain='none', award='none',
  para="Authentic assessment, fresh examples and personal experience promote academic integrity, and students respond to others' work rather than report it; any use of technology in assessment must be transparent; self and peer assessment with clear marking criteria support learning.",
  prac="Make any use of technology in assessment transparent, which the paragraph makes a must; promote integrity through authentic tasks and personal examples, and give students self and peer assessment against clear criteria.",
  ben=('n/a', 'a duty on the provider in how assessment uses technology'),
  aaw=f"Present this as a must on the provider: where technologies, which may include generative AI, are used in assessment, their use has to be transparent; it holds for assessment at every level. Cite it as {CITE}, para 3.19. Do not claim the paragraph bans any technology or says who must disclose what; it states only that transparency is required. Set it beside 1.31 and 1.32 on generative AI in assessment, theme:generative-ai and the generic skill 4.10.b11.",
  aad="Raise it when a team writes assessment briefs or a policy on technology, or when a student asks whether they may use a tool in an assignment. To staff, frame it as the one must on technology in assessment; to a student, explain plainly how the course says tools may be used and declared, without making the duty theirs. Ask: Does each assessment brief say which tools are allowed and how their use is shown? Avoid reading the paragraph aloud or inventing rules it does not state.")

s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='providers awarding honours in the subject', addressee='provider',
  verbs=['refer'], about='referring to Annex D for achievement above threshold', domain='none', award=HON,
  para="Most students will go beyond the minimum threshold; each provider decides what counts as evidence of that and should refer to Annex D of the UK degree frameworks, which describes the four main honours classifications.",
  prac="Most students exceed the threshold; the provider decides what evidence shows this and should use Annex D of the 2024 UK degree frameworks, with its descriptions of the 1st, 2.1, 2.2 and 3rd classes.",
  ben=('n/a', 'a duty on the provider in judging classifications'),
  aaw=f"Present this as a should on the provider: when judging achievement above the threshold, refer to Annex D's descriptions of the four honours classes, at FHEQ level 6 (FQHEIS level 10). Cite it as {CITE}, para 4.2, and Annex D as std:doc:qaa-fheq-2024-framework, Annex D. Do not claim the statement sets mark ranges; each provider sets its own method. Set it beside 4.4, which defines the rungs, and the Annex D summary cells {AD}summary/r1/3rd to {AD}summary/r1/1st.",
  aad="Raise it with a team or exam board calibrating degree classifications against the rung tables. Frame it for staff as the cross-check between the subject's rungs and the national class descriptions. Ask: Where does your marking scheme draw on Annex D, and does it agree with the rung definitions in 4.4? Avoid giving this to a student as their responsibility.")

s('4.3', type='expectation', rung='none', force='should', level='none', appliesTo='providers that write competence standards', addressee='provider',
  verbs=['follow'], about='competence standards and EHRC guidance', domain='none', award=[HON, MA],
  para="The three rungs, for undergraduate and master's study alike, do not set universal competence standards; a provider that develops competence standards under the Equality Act 2010 may draw on the statement and any PSRB requirements, and should then follow the latest Equality and Human Rights Commission guidance.",
  prac="Do not treat the rungs as competence standards; if you write competence standards into a programme specification under the Equality Act 2010, draw on this statement and any PSRB requirements and follow the latest EHRC guidance.",
  ben=('n/a', 'a duty on the provider in writing competence standards'),
  aaw=f"Present this as a should on the provider: if it writes competence standards in the Equality Act sense, it follows the latest Equality and Human Rights Commission guidance; it holds for undergraduate and master's study. Cite it as {CITE}, para 4.3. Do not claim the rung tables are competence standards or that the statement requires any. Set it beside 4.4, theme:accessibility and 1.13 and 1.14 on anticipatory adjustments.",
  aad="Raise it with a programme team drafting a programme specification or reviewing reasonable adjustments, when someone proposes treating a rung as a fixed competence. Frame it for staff as a caution and a pointer to EHRC guidance. Ask: Is this requirement a genuine competence standard, and have you checked it against the current EHRC guidance? Avoid putting it to a student, and avoid reading the paragraph aloud.")

s('4.5', type='expectation', rung='none', force='describes', level='none', appliesTo='students completing any philosophy module', addressee='learner',
  verbs=['completing', 'have'], about='competence expected from any philosophy module', domain='subject-skill', award='none',
  para="Philosophy is studied in single and joint honours and within modular degrees; the rung descriptions are meant for single honours, and what is expected of students taking less philosophy scales accordingly; anyone completing a philosophy module is expected to have some general philosophical skills and to know the texts and topics in its description.",
  prac="Write the rung descriptions into single honours outcomes; for joint, modular and elective students scale the expectations, but anyone finishing a philosophy module is expected to show some general philosophical skills and knowledge of the module's texts and topics.",
  ben="If you complete any philosophy module, you are expected to have some general philosophical skills and to know the texts and topics the module describes.",
  aaw=f"Present this as an expectation phrased 'expected to', recorded with force describes: anyone who completes a philosophy module has some general philosophical skills and knows the module's listed texts and topics; it holds for any module, not a level. Cite it as {CITE}, para 4.5. Do not claim the rung tables apply in full to joint honours or single modules; the paragraph says they are written for single honours. Set it beside 2.9 and the threshold cells 4.6.b1 and 4.8.b1.",
  aad="Raise it when a student from another subject takes a philosophy module and asks what is expected, or when a team writes outcomes for an elective. Tell a student plainly what you are expected to show at the end of the module; frame it for staff as the floor for any module. Ask: Which texts and topics does the module description name, and which general skill will you practise most? Avoid applying the single honours rungs to them.")

# ------------------------------------------------------------------ the rung tables, 4.6 and 4.8
LEAD = {'4.6': 'Philosophy graduates will demonstrate a knowledge and understanding of:',
        '4.8': 'Philosophy graduates will demonstrate the ability to:'}
TABLE = {'4.6': 'knowledge and understanding', '4.8': 'subject-specific and intellectual skills'}
BAND = {'threshold': '3rd', 'typical': '2.2 and 2.1', 'excellent': '1st'}
BL = {'threshold': 'To reach the threshold standard, ', 'typical': 'To reach the typical standard, ', 'excellent': 'To reach the excellent standard, '}
GRADE = {}
OUT = []

def cell_id(t, k, rung):
    base = '%s.b%d' % (t, k)
    return base if rung == 'threshold' else base + '.' + rung

def row(t, k, label, domain, fw, annex, topic, q, cells, outname):
    ids = {r: cell_id(t, k, r) for r in ('threshold', 'typical', 'excellent')}
    anx = {'threshold': f'{AD}{annex}/3rd', 'typical': f'{AD}{annex}/2.2 and {AD}{annex}/2.1', 'excellent': f'{AD}{annex}/1st'}
    for rung, c in cells.items():
        i = ids[rung]
        others = ' and '.join(ids[r] for r in ('threshold', 'typical', 'excellent') if r != rung)
        s1 = {'threshold': f"Present this as the threshold cell of the '{label}' row in the {TABLE[t]} table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10).",
              'typical': f"Present this as the typical cell of the '{label}' row in the {TABLE[t]} table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line.",
              'excellent': f"Present this as the excellent cell of the '{label}' row in the {TABLE[t]} table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement."}[rung]
        aaw = (s1 + f" Cite it as {CITE}, para {t}, {label} row, {rung} column." +
               " Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5)." +
               f" Set it beside the row's other cells ({others}), the descriptor {fw}, Annex D's {BAND[rung]} cell ({anx[rung]}) and spine:6.")
        open_ = {'threshold': f"Raise it when a student asks what they must show at the least in {topic} to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable.",
                 'typical': f"Raise it when a student wants to move from a pass towards a second-class result in {topic}, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach.",
                 'excellent': f"Raise it with a student aiming for a first in {topic}, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work."}[rung]
        avoid = {'threshold': f" Avoid reading the table aloud; give this one cell and name the typical cell ({ids['typical']}) only as the next step up.",
                 'typical': f" Avoid presenting it as the minimum: the threshold cell ({ids['threshold']}) is the floor.",
                 'excellent': " Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."}[rung]
        aad = open_ + f" Ask: {q[0]} {q[1]}" + avoid
        rec = dict(type=rung, rung=rung, level='fheq:6', appliesTo=f'single honours graduates at the {rung} level', addressee='learner',
                   domain=domain, award=HON, find=c['find'], verbs=c['verbs'], about=c['about'], para=c['para'], prac=c['prac'],
                   ben=BL[rung] + c['ben'], aaw=aaw, aad=aad)
        if c.get('after'):
            rec['after'] = c['after']
        if rung == 'threshold':
            rec['force'] = 'threshold'
            rec['forceFrom'] = '4.4'
        else:
            rec['force'] = 'will'
            rec['forceFrom'] = LEAD[t]
        P[i] = rec
    GRADE[ids['typical']] = ids['threshold'] + '|stated'
    GRADE[ids['excellent']] = ids['typical'] + '|stated'
    OUT.append(dict(outcome=outname, threshold=ids['threshold'], typical=ids['typical'], excellent=ids['excellent'], basis='stated', domain=domain, award=HON))

# ---- 4.6 knowledge and understanding (five rows; the issuer gives no row labels: ours)
row('4.6', 1, 'major philosophers', 'knowledge', 'qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1', 'knowledge/r1', 'reading the major philosophers',
    ("Which philosopher have you read in their own words, rather than through a summary?", "Where do readers disagree about that philosopher, and which reading do you find stronger?"),
    {'threshold': dict(find='The writings of some major philosophers.', verbs=[], about='writings of some major philosophers',
                       para="At threshold, graduates will know and understand the work of a number of major philosophers, as set down in their own texts.",
                       prac="At threshold, graduates will show knowledge and understanding of the texts of several of the great philosophers.",
                       ben="you will know and understand what several major philosophers wrote."),
     'typical': dict(find='The theories and arguments of major philosophers, encountered in their own writings, along with the associated important areas of interpretative controversy.',
                     verbs=['encountered'], about='theories of major philosophers and the disputes over reading them',
                     para="Typically, graduates will know the theories and arguments of major philosophers, met in the original texts, together with the main disputes over how to read them.",
                     prac="At the typical level, graduates will understand major philosophers' theories and arguments from their own texts and the key debates about how those texts are interpreted.",
                     ben="you will know the main theories and arguments of major philosophers from reading them directly, and where scholars disagree about how to read them."),
     'excellent': dict(find='The theories and arguments of major philosophers, the associated important areas of interpretative controversy, plus an original interpretation that demonstrates a close reading of primary texts.',
                       verbs=['demonstrates'], about='an original interpretation from close reading',
                       para="At the excellent level, graduates will know major philosophers' theories, arguments and interpretative disputes and will offer a reading of their own grounded in close study of the original texts.",
                       prac="At the excellent level, graduates will add to knowledge of the theories and the interpretative debates an original interpretation of their own, built on close reading of the primary sources.",
                       ben="you will also put forward your own original reading of the philosophers you study, based on close attention to what they actually wrote.")},
    'major philosophers and their interpretation')

row('4.6', 2, 'theoretical philosophy', 'knowledge', 'qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1', 'knowledge/r1', 'logic, metaphysics, epistemology or philosophy of mind',
    ("Which theory in this area could you explain and defend now?", "How does it compare with a rival view you have studied?"),
    {'threshold': dict(find='Some central theories and arguments in the fields of logic, metaphysics, epistemology or philosophy of mind, broadly understood.',
                       verbs=[], about='core theories in logic, metaphysics, epistemology or mind',
                       para="At threshold, graduates will know some core theories and arguments from logic, epistemology, metaphysics or the philosophy of mind, each taken in a wide sense.",
                       prac="At threshold, graduates will understand some of the principal theories and arguments in theoretical philosophy: logic, epistemology, metaphysics or the philosophy of mind.",
                       ben="you will know some of the main theories and arguments about logic, knowledge, reality or the mind."),
     'typical': dict(find='More of the central theories and arguments in the fields of logic, metaphysics, epistemology or philosophy of mind, broadly understood.',
                     verbs=[], about='more of the core theories in theoretical philosophy',
                     para="Typically, graduates will know a wider share of the core theories and arguments in logic, epistemology, metaphysics or the philosophy of mind.",
                     prac="At the typical level, graduates will understand more of the principal theories and arguments in theoretical philosophy than the threshold asks.",
                     ben="you will know more of the main theories and arguments about logic, knowledge, reality or the mind."),
     'excellent': dict(find='Many of the theories and arguments in the fields of logic, metaphysics, epistemology or philosophy of mind, broadly understood, in a systematic, extensive and comparative way, demonstrating knowledge that may\n\nbe beyond what has been taught.',
                       verbs=['demonstrating'], about='systematic, comparative command of theoretical philosophy',
                       para="At the excellent level, graduates will know many theories and arguments in logic, epistemology, metaphysics or the philosophy of mind, systematically, widely and by comparison, possibly reaching past what they were taught.",
                       prac="At the excellent level, graduates will command many theories and arguments in theoretical philosophy, compare them systematically and may show knowledge beyond the taught curriculum.",
                       ben="you will know many theories and arguments about logic, knowledge, reality or the mind, compare them carefully and often go beyond what your course covered.")},
    'theoretical philosophy')

row('4.6', 3, 'practical philosophy', 'knowledge', 'qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1', 'knowledge/r1', 'moral, political or social philosophy',
    ("Which theory in ethics, politics or society could you set out and test against an objection?", "Where does it stand against the main alternative you have met?"),
    {'threshold': dict(find='Some central theories and arguments in the fields of moral, political or social philosophy, broadly understood.',
                       verbs=[], about='core theories in moral, political or social philosophy',
                       para="At threshold, graduates will know some core theories and arguments in ethics, political philosophy or social philosophy, each in a wide sense.",
                       prac="At threshold, graduates will understand some principal theories and arguments in practical philosophy: moral, political or social.",
                       ben="you will know some of the main theories and arguments about ethics, politics or society."),
     'typical': dict(find='More of the central theories and arguments in the fields of moral, political or social philosophy, broadly understood.',
                     verbs=[], about='more of the core theories in practical philosophy',
                     para="Typically, graduates will know a wider share of the core theories and arguments in ethics, political philosophy or social philosophy.",
                     prac="At the typical level, graduates will understand more of the principal theories and arguments in practical philosophy than the threshold asks.",
                     ben="you will know more of the main theories and arguments about ethics, politics or society."),
     'excellent': dict(find='Many of the theories and arguments in the fields of moral, political or social philosophy, broadly understood, in a systematic, extensive and comparative way, demonstrating knowledge that may be beyond what has been taught.',
                       verbs=['demonstrating'], about='systematic, comparative command of practical philosophy',
                       para="At the excellent level, graduates will know many theories and arguments in ethics, political or social philosophy, systematically, widely and by comparison, possibly reaching past what they were taught.",
                       prac="At the excellent level, graduates will command many theories and arguments in practical philosophy, compare them systematically and may show knowledge beyond the taught curriculum.",
                       ben="you will know many theories and arguments about ethics, politics or society, compare them carefully and often go beyond what your course covered.")},
    'practical philosophy')

row('4.6', 4, 'techniques of reasoning', 'understanding', 'qaa/fheq-2024/4.15.b2 and qaa/fqheis-2024/4.16.b4', 'knowledge/r2', 'the methods of philosophical reasoning',
    ("Which reasoning technique, such as a counterexample, a reductio or a thought experiment, do you use most confidently?", "What is one criticism of a philosophical method you rely on?"),
    {'threshold': dict(find='A limited range of techniques in philosophical reasoning.', verbs=[], about='a few techniques of philosophical reasoning',
                       para="At threshold, graduates will know a narrow set of methods of philosophical reasoning.",
                       prac="At threshold, graduates will understand a small number of techniques of philosophical reasoning.",
                       ben="you will know a few of the methods philosophers use to reason."),
     'typical': dict(find='A broader range of techniques of philosophical reasoning, and of the philosophical critiques of philosophical methodologies.',
                     verbs=[], about='wider techniques and critiques of method',
                     para="Typically, graduates will know a wider set of reasoning techniques and the philosophical criticisms made of philosophy's own methods.",
                     prac="At the typical level, graduates will understand a wider range of reasoning techniques and how philosophers have criticised the discipline's methods.",
                     ben="you will know more reasoning methods and how philosophers have questioned the methods of philosophy itself."),
     'excellent': dict(find='An extensive range of techniques of philosophical reasoning, and of the philosophical critiques of, and debates around, philosophical methodologies.',
                       verbs=[], about='an extensive repertoire and the debates over method',
                       para="At the excellent level, graduates will know a wide array of reasoning techniques together with the critiques of, and debates over, philosophical method.",
                       prac="At the excellent level, graduates will understand an extensive repertoire of reasoning techniques and the critiques and debates surrounding philosophical method.",
                       ben="you will know a wide range of reasoning methods and the arguments about how philosophy should be done.")},
    'techniques of reasoning and critiques of method')

row('4.6', 5, 'current debates', 'knowledge', 'qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.15.b3.2 and qaa/fqheis-2024/4.16.b2', 'knowledge/r1', "today's philosophical debates",
    ("Which live debate in philosophy today could you summarise, with the positions taken?", "What do you think of it, and on what reading is that view based?"),
    {'threshold': dict(find='Some of the major issues currently at the frontiers of philosophical debate and research.', verbs=[], about='some leading current issues',
                       para="At threshold, graduates will know some of the leading open questions in present-day philosophical debate and research.",
                       prac="At threshold, graduates will be aware of some major issues in current philosophical research.",
                       ben="you will know some of the big questions philosophers are debating and researching now."),
     'typical': dict(find='Many of the major issues currently at the frontiers of philosophical debate and research and their critical assessment.', verbs=[], about='many current issues, critically assessed',
                     para="Typically, graduates will know many of the leading current questions in philosophy and will be able to assess them critically.",
                     prac="At the typical level, graduates will know many major issues in current research and assess them critically.",
                     ben="you will know many of the big questions in current philosophy and be able to judge them critically."),
     'excellent': dict(find='Many of the major issues currently at the frontiers of philosophical debate and research and their critical assessment based on a close reading of the primary text, demonstrating knowledge that may\n\nbe beyond what has been taught.',
                       verbs=['demonstrating'], about='current issues assessed from close reading, beyond the taught',
                       para="At the excellent level, graduates will know and critically assess many leading current questions, working from close reading of the primary literature and possibly beyond what was taught.",
                       prac="At the excellent level, graduates will assess many current research issues critically from close reading of primary sources, often reaching past the taught material.",
                       ben="you will judge many current debates critically from your own close reading of the original texts, often going beyond your course.")},
    'current debates in philosophy')

# ---- 4.8 subject-specific and intellectual skills (nine rows; row labels are the issuer's)
row('4.8', 1, 'Selecting readings', 'subject-skill', 'qaa/fheq-2024/4.15.b5', 'cognitive/r1', 'choosing and using sources',
    ("How did you choose the sources for your last essay, and which came from outside the reading list?", "What did you make of the strongest source, rather than only report it?"),
    {'threshold': dict(find='Select and comment on readings and primary sources.', verbs=['select', 'comment'], about='choosing and commenting on readings',
                       para="At threshold, graduates will choose readings and primary sources and comment on them.",
                       prac="At threshold, graduates will select readings and primary texts and offer comment on them.",
                       ben="you will pick suitable readings and original sources and say something useful about them."),
     'typical': dict(find='Select, comment and evaluate readings and primary sources, sometimes beyond the set range.', verbs=['select', 'comment', 'evaluate'], about='evaluating readings, sometimes beyond the list',
                     para="Typically, graduates will choose, comment on and evaluate readings and primary sources, at times going past the set list.",
                     prac="At the typical level, graduates will select, comment on and evaluate readings and primary texts, sometimes from outside the reading list.",
                     ben="you will choose, comment on and assess readings and original sources, sometimes going beyond your reading list."),
     'excellent': dict(find='Critically evaluate and synthesise a broad range of readings and primary sources, drawing on relevant material which may come from a range of different subdisciplines or traditions within Philosophy or from other disciplines.',
                       verbs=['evaluate', 'synthesise', 'drawing'], about='synthesising wide reading across fields',
                       para="At the excellent level, graduates will critically evaluate and bring together a wide body of readings and primary sources, drawing in material from other branches or traditions of philosophy or from other subjects.",
                       prac="At the excellent level, graduates will critically evaluate and synthesise wide reading, using relevant work from other subfields, other traditions or other disciplines.",
                       ben="you will critically assess and pull together a wide range of reading, including relevant work from other parts of philosophy or other subjects.")},
    'selecting readings')

row('4.8', 2, 'Interpreting texts', 'subject-skill', 'qaa/fheq-2024/4.15.b7', 'cognitive/r2', 'reading and interpreting texts',
    ("How does the context in which a text was written change how you read it?", "Can you set out the argument of a passage step by step and say where it is weakest?"),
    {'threshold': dict(find='Understand the importance of interpretation of texts.', verbs=['understand'], about='why interpretation matters',
                       para="At threshold, graduates will understand why interpreting texts matters.",
                       prac="At threshold, graduates will grasp why textual interpretation matters in philosophy.",
                       ben="you will understand why the way you interpret a text matters."),
     'typical': dict(find='Read carefully and interpret texts drawn from a variety of ages and/or traditions with a sensitivity to context, plus identify textually based arguments and subject their structure and implications to rigorous assessment.',
                     verbs=['read', 'interpret', 'identify'], about='contextual reading and rigorous assessment of textual arguments',
                     para="Typically, graduates will read and interpret texts from different periods or traditions with attention to context, pick out the arguments in them and test their structure and consequences rigorously.",
                     prac="At the typical level, graduates will interpret texts from various periods or traditions in context, identify their arguments and rigorously assess how those arguments are built and what follows from them.",
                     ben="you will read texts from different times and traditions carefully and in context, find the arguments in them and test how they work and what follows."),
     'excellent': dict(find='Draw sophisticated interpretations across various eras and traditions, and critically examine their underpinnings and broader philosophical implications with exceptional clarity and insight.',
                       verbs=['draw', 'examine'], about='sophisticated interpretation across eras and traditions',
                       para="At the excellent level, graduates will draw sophisticated readings across periods and traditions and critically examine their foundations and wider philosophical consequences with great clarity and insight.",
                       prac="At the excellent level, graduates will produce sophisticated interpretations spanning periods and traditions and examine critically what they rest on and imply, with exceptional clarity.",
                       ben="you will offer sophisticated readings across periods and traditions and examine clearly and insightfully what they rest on and what they imply.")},
    'interpreting texts')

row('4.8', 3, 'Terminology', 'subject-skill', 'qaa/fheq-2024/4.15.b8', 'transferable/r1', 'philosophical vocabulary',
    ("Which technical term in your current topic do you find hardest to use exactly?", "Could you define it in a sentence and give an example of its misuse?"),
    {'threshold': dict(find='Use philosophical terminology accurately.', verbs=['use'], about='accurate use of terms',
                       para="At threshold, graduates will use the technical vocabulary of philosophy correctly.",
                       prac="At threshold, graduates will use philosophical terms accurately.",
                       ben="you will use philosophical terms correctly."),
     'typical': dict(find='Use philosophical terminology precisely, including some specialised terminology.', verbs=['use'], about='precise use, some specialist terms',
                     para="Typically, graduates will use philosophical vocabulary with precision, some specialist terms included.",
                     prac="At the typical level, graduates will use philosophical terms precisely, including some specialist ones.",
                     ben="you will use philosophical terms precisely, including some specialist ones."),
     'excellent': dict(find='Use generic and specialised philosophical terminology precisely and, where appropriate,\n\nintroduce new philosophical terminology.', verbs=['use', 'introduce'], about='precise use and new terms where apt',
                       para="At the excellent level, graduates will use general and specialist philosophical vocabulary precisely and, where it helps, coin new terms.",
                       prac="At the excellent level, graduates will handle both general and specialist terms precisely and introduce new terms where the argument needs them.",
                       ben="you will use general and specialist terms precisely and, when it helps your argument, introduce new terms of your own.")},
    'terminology')

row('4.8', 4, 'Formulating arguments', 'subject-skill', 'qaa/fheq-2024/4.15.b3.1', 'cognitive/r2', 'building and defending arguments',
    ("What is the strongest objection to your main argument, and how do you answer it?", "Does your conclusion claim more than your premises support?"),
    {'threshold': dict(find='Present an argument, showing an awareness of the nature of sound arguments.', verbs=['present', 'showing'], about='presenting an argument, aware of soundness',
                       para="At threshold, graduates will put forward an argument and show they know what makes an argument sound.",
                       prac="At threshold, graduates will present an argument and show awareness of what soundness requires.",
                       ben="you will make an argument and show that you know what makes an argument sound."),
     'typical': dict(find='Formulate arguments carefully and scrupulously, drawing only warranted conclusions and predict\n\npossible objections and defend the arguments against them.',
                     verbs=['formulate', 'drawing', 'predict', 'defend'], about='careful arguments that anticipate objections',
                     para="Typically, graduates will build arguments with care, draw only conclusions the premises support, anticipate objections and defend against them.",
                     prac="At the typical level, graduates will formulate arguments scrupulously, draw only justified conclusions, foresee objections and answer them.",
                     ben="you will build arguments carefully, claim only what your reasons support, foresee objections and answer them."),
     'excellent': dict(find='Formulate sophisticated, nuanced arguments with precision and rigour, drawing well-justified conclusions based on sound reasoning and a comprehensive understanding of relevant concepts and theories that exhibit depth, clarity and an acute awareness of the\n\ncomplexities and implications involved.',
                       verbs=['formulate', 'drawing', 'exhibit'], about='sophisticated, rigorous and nuanced argument',
                       para="At the excellent level, graduates will construct subtle arguments precisely and rigorously, reaching well-supported conclusions from sound reasoning and a full grasp of the relevant concepts and theories, with depth, clarity and keen awareness of complexity and consequence.",
                       prac="At the excellent level, graduates will produce precise, rigorous and nuanced arguments whose well-justified conclusions rest on sound reasoning and thorough command of the concepts and theories, aware of their complexities and implications.",
                       ben="you will build subtle, precise and rigorous arguments, reach well-supported conclusions and show a deep, clear sense of the complications and consequences involved.")},
    'formulating arguments')

row('4.8', 5, 'Explaining', 'subject-skill', 'qaa/fheq-2024/4.15.b8', 'transferable/r1', 'explaining ideas',
    ("Could you explain your essay's central idea to someone who has never studied philosophy?", "Which example best shows what you mean, and where does it mislead?"),
    {'threshold': dict(find='Explain complex matters and ideas.', verbs=['explain'], about='explaining complex matters',
                       para="At threshold, graduates will explain complicated matters and ideas.",
                       prac="At threshold, graduates will explain complex issues and ideas.",
                       ben="you will explain complicated ideas."),
     'typical': dict(find='Clearly explain complex matters and ideas, and appropriately simplify complex matters and ideas and illustrate them with helpful examples.',
                     verbs=['explain', 'simplify', 'illustrate'], about='clear explanation, apt simplification and examples',
                     para="Typically, graduates will explain complex matters and ideas clearly, simplify them where fitting and illustrate them with useful examples.",
                     prac="At the typical level, graduates will explain complex ideas clearly, simplify them appropriately and illustrate them with good examples.",
                     ben="you will explain complex ideas clearly, simplify them when that helps and use good examples."),
     'excellent': dict(find='Tailor explanations to diverse audiences without oversimplification.', verbs=['tailor'], about='explanations fitted to varied audiences',
                       para="At the excellent level, graduates will adapt their explanations to different audiences without oversimplifying.",
                       prac="At the excellent level, graduates will fit explanations to varied audiences while avoiding oversimplification.",
                       ben="you will adjust your explanations to suit different audiences without making the ideas too simple.")},
    'explaining')

row('4.8', 6, 'Originality', 'subject-skill', 'qaa/fqheis-2024/4.16.b6 (some originality at Scottish honours; the FHEQ asks for originality only from qaa/fheq-2024/4.17.b3)', 'cognitive/r4', 'original thinking',
    ("What in your last piece of work was your own contribution rather than a report of others' views?", "How would you push that idea further?"),
    {'threshold': dict(find='Display some limited originality.', verbs=['display'], about='a little originality',
                       para="At threshold, graduates will show a little originality.",
                       prac="At threshold, graduates will show some modest originality.",
                       ben="you will show some ideas of your own."),
     'typical': dict(find='Develop some original ideas and arguments.', verbs=['develop'], about='some original ideas and arguments',
                     para="Typically, graduates will work out some ideas and arguments of their own.",
                     prac="At the typical level, graduates will develop some original ideas and arguments.",
                     ben="you will develop some ideas and arguments of your own."),
     'excellent': dict(find='Develop in depth original and plausible lines of argument.', verbs=['develop'], about='original, plausible lines of argument in depth',
                       para="At the excellent level, graduates will work out original and plausible lines of argument in depth.",
                       prac="At the excellent level, graduates will develop original, plausible lines of argument in depth.",
                       ben="you will develop original and convincing lines of argument in depth.")},
    'originality')

row('4.8', 7, 'Open-mindedness', 'subject-skill', 'qaa/fheq-2024/4.15.b4', 'cognitive/r2', 'weighing views you do not hold',
    ("What is the best argument against a view you hold?", "When did an argument last change your mind?"),
    {'threshold': dict(find='Identify the strengths and weaknesses of arguments on both sides of a philosophical\n\nquestion.', verbs=['identify'], about='strengths and weaknesses on both sides',
                       para="At threshold, graduates will pick out what is strong and weak in the arguments on each side of a philosophical question.",
                       prac="At threshold, graduates will identify strengths and weaknesses in arguments on both sides of a question.",
                       ben="you will spot the strong and weak points in the arguments on each side of a philosophical question."),
     'typical': dict(find='Review unfamiliar ideas with an open mind and a willingness to change\n\nmind when appropriate.', verbs=['review'], about='open review of unfamiliar ideas',
                     para="Typically, graduates will consider unfamiliar ideas openly and be ready to change their minds when that is warranted.",
                     prac="At the typical level, graduates will review unfamiliar ideas openly and change their minds where appropriate.",
                     ben="you will consider new ideas with an open mind and be willing to change your view when you should."),
     'excellent': dict(find='Suspend judgement and approach novel perspectives with an open and inquisitive mindset, coupled with the intellectual honesty to revise firmly held convictions when warranted.',
                       verbs=['suspend', 'approach', 'revise'], about='suspending judgement and revising firm views',
                       para="At the excellent level, graduates will hold back judgement, meet new perspectives with open curiosity and have the honesty to revise even firm convictions when the case requires it.",
                       prac="At the excellent level, graduates will suspend judgement, approach new perspectives with curiosity and honestly revise strongly held views where warranted.",
                       ben="you will hold off judging, explore new perspectives with curiosity and honestly change even firmly held beliefs when the arguments call for it.")},
    'open-mindedness')

row('4.8', 8, 'Interdisciplinarity', 'subject-skill', 'qaa/fheq-2024/4.15.b6', 'knowledge/r1', 'links between philosophy and other subjects',
    ("Which other subject has your philosophical work drawn on, or could it help?", "What philosophical assumption have you noticed in work from another field?"),
    {'threshold': dict(find='Identify some of the ways in which philosophical work can inform, and be informed\n\nby, work in other disciplines.', verbs=['identify', 'inform'], about='two-way links with other disciplines',
                       para="At threshold, graduates will name some ways philosophy and other disciplines can shape each other.",
                       prac="At threshold, graduates will identify some ways in which philosophy feeds into, and draws on, other disciplines.",
                       ben="you will point to some ways philosophy and other subjects learn from each other."),
     'typical': dict(find='Describe and explain some of the ways in which philosophical work can inform, and be informed by, work in\n\nother disciplines.', verbs=['describe', 'explain', 'inform'], about='describing and explaining those links',
                     para="Typically, graduates will describe and explain some ways philosophy and other disciplines shape each other.",
                     prac="At the typical level, graduates will describe and explain some of the two-way links between philosophy and other disciplines.",
                     ben="you will describe and explain some ways philosophy and other subjects learn from each other."),
     'excellent': dict(find='Describe, explain and critique philosophical doctrines in non- philosophical work, and\n\nto see the relevance of non-philosophical ideas\n\nand research for philosophical debates.',
                       verbs=['describe', 'explain', 'critique', 'see'], about='critiquing philosophy in other fields and the reverse',
                       para="At the excellent level, graduates will describe, explain and critique the philosophical assumptions at work in other fields and see how ideas and research from outside philosophy bear on its debates.",
                       prac="At the excellent level, graduates will analyse and critique philosophical doctrines embedded in work from other disciplines and recognise what outside ideas and research contribute to philosophical debate.",
                       ben="you will find and critique the philosophical ideas inside work from other subjects, and see how research from those subjects matters to philosophical debates.")},
    'interdisciplinarity')

row('4.8', 9, 'Applications', 'subject-skill', 'qaa/fheq-2024/4.15.b6', 'practical/r1', 'using philosophy in everyday life',
    ("Where in everyday life, at work or in the news, could your philosophy make a difference?", "How would you use it on a real ethical dilemma?"),
    {'threshold': dict(find='State some of the ways in which philosophical work can engage with the concerns of ordinary life.', verbs=['state', 'engage'], about='naming links to ordinary life',
                       para="At threshold, graduates will say how philosophy can bear on some everyday concerns.",
                       prac="At threshold, graduates will state some ways philosophy connects with ordinary life.",
                       ben="you will say how philosophy can connect with some everyday concerns."),
     'typical': dict(find='Describe and explain some of the ways in which philosophical work can engage with the concerns of ordinary life.', verbs=['describe', 'explain', 'engage'], about='explaining links to ordinary life',
                     para="Typically, graduates will describe and explain some ways philosophy bears on everyday concerns.",
                     prac="At the typical level, graduates will describe and explain some connections between philosophy and ordinary life.",
                     ben="you will describe and explain some ways philosophy connects with everyday concerns."),
     'excellent': dict(find="Exhibit a nuanced grasp of philosophy's relevance to everyday lived experiences, applying philosophical insights to illuminate and address real-world complexities and ethical dilemmas.",
                       verbs=['exhibit', 'applying', 'illuminate', 'address'], about='applying philosophy to real problems and dilemmas',
                       para="At the excellent level, graduates will show a subtle understanding of how philosophy matters to lived experience, using its insights to clarify and tackle real-world complexity and ethical dilemmas.",
                       prac="At the excellent level, graduates will apply philosophical insight with nuance to everyday experience, shedding light on real problems and ethical dilemmas and helping to address them.",
                       ben="you will show a subtle grasp of how philosophy matters to daily life and use it to shed light on real problems and ethical dilemmas.")},
    'applications')

# ------------------------------------------------------------------ 4.10 generic skills (undergraduate; no rungs)
def gen(k, verbs, about, para, prac, ben, fw, annex, strand, topic, q):
    s('4.10.b%d' % k, type='outcome', rung='none', force='will', level='fheq:6', appliesTo='undergraduate graduates of the subject', addressee='learner',
      verbs=verbs, about=about, domain='generic-skill', award=HON, para=para, prac=prac, ben=ben,
      aaw=(f"Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10)."
           f" Cite it as {CITE}, para 4.10, item {k}."
           " Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent."
           f" Set it beside the descriptor {fw}, Annex D's {AD}{annex} and the reference framework's {strand} at spine:6."),
      aad=(f"Bring it up when a student or a team is discussing {topic}, for example in personal tutoring, before a placement or in a review of transferable skills."
           " Put it plainly, in the second person to a student and as a programme outcome to staff."
           f" Ask: {q[0]} {q[1]}"
           " Avoid reading the whole list aloud; take one skill at a time."))

gen(1, ['identify'], 'spotting issues and problems',
    "Will be able to recognise the issues, questions and problems a topic raises.",
    "Graduates will identify the issues, questions and problems a topic raises.",
    "You will be able to spot the issues, questions and problems a topic raises.",
    'qaa/fheq-2024/4.15.b7', 'cognitive/r3/3rd', 'strand:thinking', 'how to frame a question',
    ("What is the real question behind the task you have been set?", "Which problems does it raise that are not yet answered?"))
gen(2, ['identify', 'acquire'], 'finding and filling gaps in knowledge',
    "Will be able to see where their own knowledge falls short and learn what is missing.",
    "Graduates will identify gaps in what they know and acquire the knowledge to fill them.",
    "You will be able to see what you do not yet know and go and learn it.",
    'qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/4.15.b5', 'transferable/r3/3rd', 'strand:autonomy', 'gaps in what someone knows',
    ("What do you still need to find out before you can answer this?", "Where will you go to learn it?"))
gen(3, ['understand', 'analyse'], 'analysing knowledge and information',
    "Will be able to grasp and break down knowledge and information.",
    "Graduates will understand and analyse the knowledge and information they meet.",
    "You will be able to understand and analyse the knowledge and information you come across.",
    'qaa/fheq-2024/4.15.b7', 'cognitive/r2/3rd', 'strand:thinking', 'making sense of sources and data',
    ("What are the key claims in this source, and what supports them?", "Which piece of information here would you trust least, and why?"))
gen(4, ['synthesise'], 'synthesising the state of knowledge',
    "Will be able to draw together what is known on a given topic.",
    "Graduates will synthesise the current state of knowledge on a topic.",
    "You will be able to pull together what is currently known about a topic.",
    'qaa/fheq-2024/4.15.b6', 'knowledge/r3/3rd', 'strand:thinking', 'summing up a field',
    ("Could you sum up where the debate on your topic now stands in a paragraph?", "Which sources would you need to bring together to do that?"))
gen(5, ['apply', 'provide'], 'reaching evidenced conclusions',
    "Will be able to use knowledge and understanding to reach conclusions backed by evidence.",
    "Graduates will apply knowledge and understanding to reach conclusions supported by evidence.",
    "You will be able to use what you know to reach conclusions backed by evidence.",
    'qaa/fheq-2024/4.15.b7', 'cognitive/r3/3rd', 'strand:application', 'drawing conclusions',
    ("What evidence or reasons support your conclusion?", "What would make you change it?"))
gen(6, ['communicate'], 'communicating in speech or other forms',
    "Will be able to communicate well and fittingly, in speech or by other means.",
    "Graduates will communicate effectively and appropriately, verbally, non-verbally or both.",
    "You will be able to communicate well and appropriately, in speech or in other forms.",
    'qaa/fheq-2024/4.15.b8', 'transferable/r1/3rd', 'strand:communication', 'communication',
    ("Which form of communication, spoken, written or visual, do you find hardest?", "How could you practise it on your course?"))
gen(7, ['present'], 'presenting knowledge or arguments to others',
    "Will be able to set out knowledge or an argument so that others can follow it.",
    "Graduates will present knowledge or an argument in a form others can understand.",
    "You will be able to set out what you know, or an argument, so other people can follow it.",
    'qaa/fheq-2024/4.15.b8', 'transferable/r1/3rd', 'strand:communication', 'presenting work',
    ("Could a classmate follow your argument without asking you questions?", "Where would they get lost?"))
gen(8, ['engage', 'collate', 'analyse', 'select', 'present'], 'critical use of digital technology',
    "Will be able to use a range of digital technologies critically to gather, analyse, choose and present information.",
    "Graduates will engage critically with varied digital tools to collate, analyse, select and present information.",
    "You will be able to use different digital tools critically to gather, analyse, choose and present information.",
    'qaa/fheq-2024/4.15.b8', 'transferable/r1/3rd', 'strand:application', 'digital tools',
    ("Which digital tools do you use to find and organise sources, and how do you check what they give you?", "Where might a tool, generative AI included, be misleading you?"))
gen(9, ['assert', 'undertaking', 'conducting', 'demonstrating'], 'intellectual independence',
    "Will be able to show intellectual independence: working alone with suitable guidance and support, researching on their own initiative and judging critically.",
    "Graduates will assert intellectual independence by working independently with fitting guidance, carrying out self-directed research and exercising critical judgement.",
    "You will be able to think for yourself: work on your own with the right support, carry out your own research and make critical judgements.",
    'qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/4.15.b9.1', 'transferable/r3/3rd', 'strand:autonomy', 'independent study',
    ("Which part of your last project did you direct yourself?", "Where did you need guidance, and could you manage it alone next time?"))
gen(10, ['work', 'undertaking', 'participating'], 'collaboration in groups and discussion',
    "Will be able to work with others, in a group or team or by taking part in discussion.",
    "Graduates will work collaboratively, through group or team work, discussion or both.",
    "You will be able to work with others, in a group or team or by joining in discussions.",
    'qaa/fheq-2024/4.15.b9.1', 'transferable/r2/3rd', 'strand:communication', 'group work and discussion',
    ("What did you contribute to the last group task or seminar discussion?", "How did you respond when someone disagreed with you?"))
gen(11, ['reflect'], 'reflecting on progress and academic integrity',
    "Will be able to reflect on how they are progressing, academic integrity included.",
    "Graduates will reflect on their own progress, including matters of academic integrity.",
    "You will be able to reflect on your own progress, including how you keep your work honest and properly referenced.",
    'qaa/fheq-2024/4.15.b5', 'transferable/r5/3rd', 'strand:autonomy', 'progress and academic integrity',
    ("What has improved most in your work this year, and what has not?", "How do you make sure your use of sources and tools keeps the work your own?"))
gen(12, ['identify', 'examine'], 'examining underlying values and ethics',
    "Will be able to recognise and examine the values and ethics beneath culture and society and in their own lives.",
    "Graduates will identify and examine the values and ethics underlying culture, society and personal life.",
    "You will be able to recognise and question the values and ethics behind culture, society and your own life.",
    'qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/4.15.b9.2', 'summary/r1/3rd', 'strand:thinking', 'values in culture, society and one\'s own life',
    ("Which value is doing the work in this policy or practice?", "Do you hold it yourself, and why?"))

# ------------------------------------------------------------------ 4.11 master's list (another award, recorded as its threshold: batch 1 convention)
def mas(k, find, verbs, domain, about, para, prac, ben, fw, nb, topic, q):
    s('4.11.b%d.masters' % k, find=find, type='threshold', rung='threshold', force='will', level='fheq:7', appliesTo="holders of a master's degree in the subject",
      addressee='learner', verbs=verbs, about=about, domain=domain, award=MA, para=para, prac=prac, ben=ben,
      aaw=(f"Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold."
           f" Cite it as {CITE}, para 4.11, item {k}."
           " Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs."
           f" Set it beside the descriptor {fw}, spine:7 and, for the step up from honours, {nb}."),
      aad=(f"Raise it with a master's student or a master's programme team when {topic} comes up, for example in dissertation supervision or programme review."
           " Use plain words: the second person for a student, a programme outcome for staff."
           f" Ask: {q[0]} {q[1]}"
           " Avoid holding an undergraduate to it, and do not read the list aloud."))

mas(1, 'a sophisticated and comprehensive understanding of key concepts, theories, issues and debates within the discipline of Philosophy, informed by familiarity with current research and advanced scholarship',
    ['informed'], 'understanding', 'comprehensive understanding informed by current research',
    "Will show a sophisticated, thorough understanding of the discipline's key concepts, theories, issues and debates, shaped by current research and advanced scholarship.",
    "Master's graduates will understand the key concepts, theories, issues and debates of philosophy in a sophisticated and comprehensive way, shaped by current research.",
    "You will understand the main concepts, theories, issues and debates in philosophy in depth and breadth, shaped by current research.",
    'qaa/fheq-2024/4.17.b1', '4.6.b5.excellent', 'the depth of their grasp of the discipline',
    ("Which current debate in your area could you map, with its main positions and recent contributions?", "How has recent research changed your view of it?"))
mas(2, 'knowledge of appropriate research methods and employment of appropriate research skills',
    [], 'subject-skill', 'research methods and skills',
    "Will show knowledge of suitable research methods and use fitting research skills.",
    "Master's graduates will know which research methods suit their work and will apply the research skills it needs.",
    "You will know which research methods suit your work and use the research skills it calls for.",
    'qaa/fheq-2024/4.17.b2', '4.10.b9', 'research method',
    ("What method does your dissertation use, and why that one?", "Which research skill do you most need to strengthen?"))
mas(3, 'the ability to formulate, evaluate and critically analyse complex philosophical arguments, texts, positions and problems at an advanced level using rigorous philosophical methods',
    ['formulate', 'evaluate', 'analyse', 'using'], 'subject-skill', 'advanced analysis of arguments and texts',
    "Will be able to construct, assess and critically analyse demanding arguments, texts, positions and problems in philosophy at an advanced standard, with rigorous method.",
    "Master's graduates will construct, evaluate and critically analyse demanding philosophical arguments, texts and problems at an advanced standard, with rigorous method.",
    "You will be able to build, assess and critically analyse difficult philosophical arguments, texts and problems at an advanced level, using rigorous methods.",
    'qaa/fheq-2024/4.17.b4.1 and qaa/fheq-2024/4.17.b4.2', '4.8.b4.excellent', 'the rigour of their analysis',
    ("Which argument in your field have you analysed most rigorously, and what method did you use?", "Where does your analysis still rely on an assumption you have not defended?"))
mas(4, 'expertise in one or more specialised areas or philosophical traditions through in-depth study and research',
    [], 'knowledge', 'specialist expertise',
    "Will show expertise in at least one specialist area or tradition, gained through deep study and research.",
    "Master's graduates will have expert knowledge of one or more specialist areas or traditions from in-depth study and research.",
    "You will become expert in one or more specialist areas or traditions of philosophy through deep study and research.",
    'qaa/fheq-2024/4.17.b1', '4.6.b1.excellent', 'specialisation',
    ("Which area or tradition would you call your specialism now?", "What have you read in it that a non-specialist would not know?"))
mas(5, 'the capacity to conceptualise, design and execute a sustained philosophical research project that contributes to the field',
    ['conceptualise', 'design', 'execute', 'contributes'], 'subject-skill', 'a sustained research project',
    "Will show the capacity to conceive, plan and carry out a sustained piece of philosophical research that adds to the field.",
    "Master's graduates will conceive, design and complete a substantial philosophical research project that makes a contribution to the field.",
    "You will be able to plan, design and complete a substantial philosophical research project that adds something to your field.",
    'qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b6', '4.10.b9 (and not spine:8: do not claim a doctoral contribution)', 'the dissertation or research project',
    ("What will your research project add that is not already in the literature?", "Is its scope realistic for the time you have?"))
mas(6, 'highly developed skills in rational and logical analysis, interpretation of complex ideas, and construction of sophisticated arguments and lines of reasoning',
    [], 'subject-skill', 'advanced analysis, interpretation and argument',
    "Will show well-developed skill in rational and logical analysis, in interpreting complex ideas and in building sophisticated arguments and chains of reasoning.",
    "Master's graduates will analyse rationally and logically, interpret complex ideas and construct sophisticated reasoning at a highly developed level.",
    "You will be highly skilled at logical analysis, at interpreting complex ideas and at building sophisticated arguments.",
    'qaa/fheq-2024/4.17.b5', '4.8.b4.excellent and 4.8.b2.excellent', 'the quality of their reasoning',
    ("Which step in your argument would a logician press you on?", "How would you restate the hardest idea in your topic in your own terms?"))
mas(7, 'an appreciation of the broader significance and implications of philosophical ideas in relation to other disciplinary perspectives and real-world contexts',
    [], 'understanding', 'wider significance of philosophical ideas',
    "Will show an appreciation of what philosophical ideas mean beyond philosophy, for other disciplines and for real situations.",
    "Master's graduates will appreciate the wider significance of philosophical ideas for other disciplines and for real-world settings.",
    "You will understand why philosophical ideas matter beyond philosophy, for other subjects and in real situations.",
    'qaa/fheq-2024/4.17.b3', '4.8.b8.excellent and 4.8.b9.excellent', 'why their work matters beyond philosophy',
    ("Who outside philosophy should care about your research, and why?", "What would change in practice if your conclusion were accepted?"))
mas(8, 'advanced skills in philosophical writing and verbal and/or non-verbal presentation to effectively communicate complex ideas to specialist and non-specialist audiences',
    ['communicate'], 'generic-skill', 'communicating complex ideas to all audiences',
    "Will show advanced writing and presentation skills, spoken or otherwise, that convey complex ideas well to specialists and non-specialists.",
    "Master's graduates will write and present at an advanced level, conveying complex ideas effectively to specialist and general audiences.",
    "You will write and present at an advanced level, getting complex ideas across to experts and non-experts.",
    'qaa/fheq-2024/4.17.b5', '4.8.b5.excellent', 'writing and presenting',
    ("Could you present your research in five minutes to a non-specialist audience?", "What would you leave out, and what must stay?"))
mas(9, 'the ability to engage in sustained philosophical dialogue, debate and collaborative inquiry',
    ['engage'], 'subject-skill', 'sustained dialogue and collaborative inquiry',
    "Will show the ability to take part in long philosophical dialogue, debate and shared inquiry.",
    "Master's graduates will sustain philosophical dialogue, debate and collaborative inquiry.",
    "You will be able to keep up philosophical discussion, debate and shared inquiry with others over time.",
    'qaa/fheq-2024/4.17.b5', '4.10.b10', 'seminars and debate',
    ("How do you keep a disagreement in a seminar productive?", "What did you learn from the last debate in which you changed position?"))
mas(10, 'a reflective understanding of the nature of Philosophy as a discipline, its methods, presuppositions, and its relationship to other forms of inquiry',
    [], 'understanding', "philosophy's nature, methods and presuppositions",
    "Will show a reflective grasp of what philosophy is as a discipline, its methods and assumptions, and how it relates to other kinds of inquiry.",
    "Master's graduates will reflect on the nature of philosophy, its methods and presuppositions and its relation to other inquiry.",
    "You will understand, reflectively, what philosophy is, how it works, what it assumes and how it relates to other kinds of inquiry.",
    'qaa/fheq-2024/4.17.b4.2', '4.6.b4.excellent', 'what philosophy is and how it works',
    ("What does your own approach to philosophy assume?", "How is it different from the way another discipline would tackle your question?"))
mas(11, 'ethical reasoning skills and an appreciation of the moral dimensions of philosophical problems and the role of Philosophy in addressing ethical, social and political issues',
    ['addressing'], 'subject-skill', "ethical reasoning and philosophy's social role",
    "Will show skill in ethical reasoning and an appreciation of the moral side of philosophical problems and of philosophy's part in tackling ethical, social and political issues.",
    "Master's graduates will reason ethically and appreciate both the moral dimensions of philosophical problems and philosophy's role in ethical, social and political questions.",
    "You will reason well about ethics and see the moral side of philosophical problems and how philosophy can help with ethical, social and political issues.",
    'qaa/fheq-2024/4.17.b5', '4.10.b12', 'ethics and public questions',
    ("What moral question does your research raise, even if it is not about ethics?", "How could philosophy help with a social or political issue you care about?"))
mas(12, 'independent learning and research skills to identify, evaluate and synthesise relevant sources and continue their philosophical development.',
    ['identify', 'evaluate', 'synthesise', 'continue'], 'generic-skill', 'independent learning and continuing development',
    "Will show the independent learning and research skills to find, assess and combine relevant sources and to keep developing as a philosopher.",
    "Master's graduates will learn and research independently, identifying, evaluating and synthesising sources and continuing their philosophical development.",
    "You will be able to learn and research on your own, finding, assessing and combining sources, and keep growing as a philosopher.",
    'qaa/fheq-2024/4.17.b7 and qaa/fheq-2024/4.17.b8.3', '4.10.b9', 'learning after the course',
    ("How will you keep doing philosophy after the course ends?", "How do you now find and judge sources without a reading list?"))

TH = {'1.11': 'theme:edi', '1.18': 'theme:esd'}

# ------------------------------------------------------------------ S5 to S7
S5 = dict(
    levels=[dict(id='fheq:4', role='cites', locator='D1, 2.2; 2.10'),
            dict(id='fheq:5', role='cites', locator='D1, 2.3; 2.10'),
            dict(id='fheq:6', role='cites', locator='D1, 2.4; 2.7'),
            dict(id='fheq:7', role='cites', locator='D1, 2.7; 2.11'),
            dict(id='fqheis:7', role='cites', locator='D1, 2.2'),
            dict(id='fqheis:8', role='cites', locator='D1, 2.3; 2.10'),
            dict(id='fqheis:9', role='cites', locator='D1, 2.4; 2.7; 2.10'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.4; 2.7'),
            dict(id='fqheis:11', role='cites', locator='D1, 2.7; 2.11'),
            dict(id='spine:6', role='inferred: the honours rungs and generic skills', locator='std:ref:uk-framework R2, R8'),
            dict(id='spine:7', role="inferred: the master's list", locator='std:ref:uk-framework R2, R8')],
    crosswalks=[dict(**{'from': 'fheq:4'}, to='fqheis:7', relation='equivalent', basis='stated (D1, 2.2: first year); agrees with std:doc:qaa-fheq-2024-framework Table 1'),
                dict(**{'from': 'fheq:5'}, to='fqheis:8', relation='equivalent', basis='stated (D1, 2.3: second year); agrees with Table 1'),
                dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.4; 2.7: "FQHEIS Levels 9/10"); Table 1 puts honours at fqheis:10, other bachelor\'s at fqheis:9'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.7; 2.11); shared descriptor qaa/fheq-2024/4.17'),
                dict(**{'from': 'fheq:4'}, to='fqheis:8', relation='as-stated, conflicting', basis='stated (D1, 2.10: CertHE); Table 1 gives the CertHE fqheis:7: Part E'),
                dict(**{'from': 'fheq:5'}, to='fqheis:9', relation='as-stated, conflicting', basis='stated (D1, 2.10: DipHE); Table 1 gives the DipHE fqheis:8: Part E')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['front matter', '1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '1.12', '1.31', '3.13']),
      dict(id='theme:accessibility', role='carries', carriedIn=['front matter', '1.13', '1.14', '1.15', '1.16', '3.18']),
      dict(id='theme:esd', role='carries', carriedIn=['front matter', '1.17', '1.18', '1.19', '2.6']),
      dict(id='theme:enterprise', role='carries', carriedIn=['front matter', '1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['front matter', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-philosophy-2019-benchmarks (not held)', note='the text names only "the previous Subject Benchmark Statement"; the 2019 minor update is read from the advisory group lists: Part E'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='4.2: providers should refer to it; 4.4 matches the rungs to the 3rd, 2nd and 1st classes'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 4 to 7 (2.2 to 2.4, 2.7, 2.10, 2.11)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note="levels 7 to 11 as the statement gives them (2.2 to 2.4, 2.7, 2.10, 2.11); 2.10's pairings conflict with the FHEQ's Table 1: Part E"),
      dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='1.18: to be consulted as a core resource'),
      dict(rel='refersTo', target='QAA Quality Code, 2024 update (not yet ingested)', note='front matter'),
      dict(rel='refersTo', target='Equality Act 2010 and the Public Sector Equality Duty (law)', note='1.10, 4.3')]

# ------------------------------------------------------------------ SB1 to SB6
SB1 = ["Concerned with how we make sense of the world, of ourselves and of our relations; seen as underpinning the other disciplines and as sitting where the humanities and the social and natural sciences meet (D1, 1.1).",
       "Asks the large questions of knowledge, value, existence, morality and social life, with a clarifying role that supports constructive dialogue (D1, 1.2).",
       "Pluralistic: analytic, continental and comparative traditions, world philosophies among them, with methods from formal and logical analysis to hermeneutics, conceptual engineering and phenomenology; the traditions share precision, clarity and self-reflection (D1, 3.2, 3.4).",
       "Learned by doing: students practise philosophy rather than only study a body of knowledge, through reading, discussion and presentation, and formal methods through graded exercises (D1, 3.8, 3.10, 3.11).",
       "Seeks a safe space for controversial and uncomfortable views, voiced with care and met constructively, and a community of enquiry that values every member (D1, 1.7, 1.8, 1.10).",
       "Acknowledges a past canon dominated by privileged European men and treats diversifying the curriculum as imperative (D1, 1.9).",
       "Often studied jointly with other subjects, and taught by philosophers inside other disciplines' accredited degrees (D1, 1.22, 2.5, 2.6)."]

SB2 = [dict(theme='theme:edi', inThisSubject="named Equity, diversity and inclusion: limited access to the subject before university; varied materials, activities and assessment; a safe but challenging space for controversial views; diversifying a narrow Western canon; the Equality Act 2010 and the Public Sector Equality Duty; outward-looking comparison of traditions; reflective logs (D1, 1.5 to 1.12); assessment variety as an EDI gain from GenAI (D1, 1.31); bringing diverse students together (D1, 3.13)", statements=['1.11']),
       dict(theme='theme:accessibility', inThisSubject="named Accessibility and the needs of disabled students: an anticipatory approach after the Disabled Students Commission report (clear expectations, care that asynchronous materials and automated captions do not create new barriers, multiple means of engagement); reasonable adjustments; audio and audiovisual resources; the insight disabled students bring to debate (D1, 1.13 to 1.16); alternative assessments (D1, 3.18)", statements=[]),
       dict(theme='theme:esd', inThisSubject="named Education for sustainable development: sustainability defined as a moral attribute of acts, processes and institutions; the UN SDGs and the 2021 Advance HE and QAA guidance; philosophy as critique of the concept and as a resource for exposing false sustainability claims (D1, 1.17 to 1.19); sustainability among the concepts other professions' degrees teach (D1, 2.6)", statements=['1.18']),
       dict(theme='theme:enterprise', inThisSubject="named Employability, enterprise and entrepreneurship education: clear thinking, logic and argument as employability skills; joint programmes, placements and years abroad; assessments such as policy briefs; support for social enterprise; leadership strengths; the sectors graduates enter (D1, 1.20 to 1.27)", statements=[]),
       dict(theme='theme:generative-ai', inThisSubject="named Generative artificial intelligence: weighed against the degree's principal skills; formative benefits (critiquing outputs, an interlocutor, help for reticent students); risks to reading, analysis and originality; a challenge to essay-based assessment and integrity; GenAI as a philosophical topic in its own right (D1, 1.28 to 1.33)", statements=[])]

SB3 = dict(
    areas=[dict(component='3.2', gloss='traditions (analytic, continental, comparative, world) and methods (formal, logical, textual, conceptual engineering, hermeneutic, phenomenological)'),
           dict(component='3.3', gloss='general philosophy; philosophy of particular practices such as language, science, law and the arts; collaborative work on questions underlying other disciplines'),
           dict(component='3.6', gloss='single honours: major philosophers in their own texts; theoretical philosophy; aesthetics, moral, political and social philosophy; contemporary challenges; current research issues'),
           dict(component='3.7', gloss='joint honours and specialist courses; history, theoretical and practical philosophy; interdisciplinary modules')],
    practices=[dict(component='3.8', kind='teaching', gloss='model the practice of philosophy; balance knowledge with discussion and response'),
               dict(component='3.9', kind='learning', gloss='student-led research, peer exchange and self-chosen questions'),
               dict(component='3.10', kind='learning', gloss='own reading, discussion and presentation with feedback in every module'),
               dict(component='3.11', kind='learning', gloss='formal methods learned through graded exercises, with computer-assisted logic'),
               dict(component='3.12', kind='learning', gloss='incremental progression from supported to independent study'),
               dict(component='3.13', kind='teaching', gloss='two-year cycles; diverse students on shared problems; varied discussion modes'),
               dict(component='3.14', kind='teaching', gloss='lectures, tutorials, seminars, self-directed study, guided reading with essays, dissertation, online resources, student-led groups'),
               dict(component='3.15', kind='assessment', gloss='the suite tests knowledge and understanding, argument and analysis, presentation'),
               dict(component='3.16', kind='assessment', gloss='diverse ways of meeting outcomes'),
               dict(component='3.17', kind='assessment', gloss='co-created and reflective assessment; essays to curated events and logic exercises'),
               dict(component='3.18', kind='assessment', gloss='accessible alternatives; students propose formats and questions'),
               dict(component='3.19', kind='assessment', gloss='integrity through authenticity; transparency with technology; self and peer assessment')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.4', tables=['4.6', '4.8'], award=HON, items=14),
           dict(rung='typical', leadIn='4.4', tables=['4.6', '4.8'], award=HON, items=14),
           dict(rung='excellent', leadIn='4.4', tables=['4.6', '4.8'], award=HON, items=14),
           dict(rung='threshold', leadIn='4.11', tables=[], award=MA, items=12, note="the master's list, recorded as that award's threshold (batch 1 convention); no typical or excellent master's rungs")],
    rungBases="4.4 defines the rungs: threshold the minimum acceptable for an honours graduate, matched to a third; typical what most reach, a second; excellent the best, a first. 4.6 and 4.8 are tables listing each outcome once per row under the three rung columns, so each row's cells are paired by the issuer; 4.7 and 4.9 state that the higher rungs include the lower. 4.5: the rungs are written for single honours.",
    outcomeLists=[dict(leadIn='4.10', gloss='generic skills at undergraduate level, no rungs', items=12, award=[HON]),
                  dict(leadIn='4.11', gloss="outcomes for the master's degree, recorded in rungs as the master's threshold", items=12, award=[MA])],
    outcomes=OUT)

SB4A_FULL = []

SB5 = [dict(body='Professional, statutory and regulatory bodies (PSRBs), none named for the subject',
            says="the statement can support PSRBs' definitions of academic standards (front matter); many accredited degrees in other disciplines require philosophical concepts such as ethics, risk and sustainability (D1, 2.6); courses with professional outcomes may need PSRB accreditation (D1, 2.19); competence standards may draw on PSRB requirements (D1, 4.3)",
            requirements='not-applicable: no body is named for philosophy (Part E)'),
       dict(body='Office for Students', says='in England, benchmark statements are not sector-recognised standards under its regulatory framework (D1, front matter)', requirements='not yet ingested (Part E)'),
       dict(body='Equality and Human Rights Commission', says='providers that write competence standards should follow its most recent guidance (D1, 4.3)', requirements='not yet ingested (Part E; D3)'),
       dict(body='Disabled Students Commission', says='its Annual Report 2021-22 informs the anticipatory approach to accessibility (D1, 1.13)', requirements='not-applicable: a report, not requirements (Part E)')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equity, diversity and inclusion (front matter: equity, diversity, and inclusion)', carriedIn=['front matter', '1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '1.12', '1.31', '3.13'], statements=['1.11']),
            dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=['front matter', '1.13', '1.14', '1.15', '1.16', '3.18'], statements=[]),
            dict(id='theme:esd', named='Education for sustainable development', carriedIn=['front matter', '1.17', '1.18', '1.19', '2.6'], statements=['1.18']),
            dict(id='theme:enterprise', named='Employability, enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['front matter', '1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27'], statements=[]),
            dict(id='theme:generative-ai', named='Generative artificial intelligence (GenAI)', carriedIn=['front matter', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33'], statements=[])],
    frameworks=[dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.2', '2.3', '2.4', '2.7', '2.10', '2.11', '4.2']),
                dict(framework='scqf', levels=['fqheis:7', 'fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.2', '2.3', '2.4', '2.7', '2.10', '2.11'])],
    bodies=[dict(body='PSRBs (unnamed)', citedIn=['front matter', '2.6', '2.19', '4.3']),
            dict(body='Office for Students', citedIn=['front matter']),
            dict(body='Equality and Human Rights Commission', citedIn=['4.3']),
            dict(body='Disabled Students Commission', citedIn=['1.13']),
            dict(body='Advance HE (co-author of the ESD guidance)', citedIn=['1.18'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2'], role='descriptions of the four honours classes (1st, 2.1, 2.2, 3rd), for evidence of achievement above threshold; 4.4 matches the rungs to them'),
                     dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development Guidance produced by Advance HE and QAA (March 2021)', citedIn=['1.18'], role='a core resource for the sustainability theme'),
                     dict(document='QAA Quality Code, 2024 update (not yet ingested: Part E)', named='the Quality Code', citedIn=['front matter'], role='a further reference point'),
                     dict(document="QAA Glossary (not ingested)", named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
                     dict(document='UN Sustainable Development Goals (external)', named='UN Sustainable Development Goals (SDGs)', citedIn=['1.18'], role='the priorities the sustainability theme follows'),
                     dict(document='Equality Act 2010 (law)', named='Equality Act 2010', citedIn=['1.10', '4.3'], role='prohibitions guiding inclusive teaching; the definition of competence standards'),
                     dict(document='Public Sector Equality Duty (law)', named='Public Sector Equality Duty', citedIn=['1.10'], role='fostering good relations between students'),
                     dict(document='Disabled Students Commission Annual Report 2021-22 (external)', named='Disabled Students Commission Annual Report 2021-22', citedIn=['1.13'], role='grounds the anticipatory approach to accessibility'),
                     dict(document='EHRC guidance on competence standards (not identified: D3)', named='the most recent guidance from the Equality and Human Rights Commission', citedIn=['4.3'], role='what providers follow when writing competence standards')])

# ------------------------------------------------------------------ Part B
B1 = [dict(slug='threshold-standard', definition='the lowest standard acceptable for an honours graduate in the subject, matched to a third-class degree (D1, 4.4)', beneficiaryDefinition='the least you need to show to gain an honours degree', scopeNote='the first column of 4.6 and 4.8', category='unknown', practices=['education']),
      dict(slug='typical-standard', definition='the standard most honours graduates reach, matched to a second-class degree (D1, 4.4)', beneficiaryDefinition='what most students show by the end of the degree', scopeNote='the second column of 4.6 and 4.8', category='unknown', practices=['education']),
      dict(slug='excellent-standard', definition='the standard of the strongest honours graduates, matched to a first-class degree (D1, 4.4)', beneficiaryDefinition='what the strongest students show', scopeNote='the third column of 4.6 and 4.8', category='unknown', practices=['education']),
      dict(slug='sustainability', definition='a quality, worthy of moral praise, of acts, processes or institutions that achieve their ends without harming the prospects of living things (D1, 1.17)', scopeNote='the sense the statement uses for its ESD theme', category='unknown', practices=['education']),
      dict(slug='generative-artificial-intelligence', definition='AI that generates text or images, abbreviated GenAI; more than a tool, since it changes its users and their relation to ideas (D1, 1.28, 1.31, 1.33)', category='unknown', practices=['education']),
      dict(slug='psrb', definition='professional, statutory and regulatory bodies (D1, front matter)', category='unknown', practices=['education']),
      dict(slug='competence-standard', definition='a standard in the sense of the Equality Act 2010; the rungs are not meant as universal ones (D1, 4.3)', category='unknown', practices=['education'])]
B2A = [dict(concept='threshold-standard', form='Threshold', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='minimum threshold', lang='en', partOfSpeech='noun-phrase', termStatus='admitted', register='formal'),
       dict(concept='typical-standard', form='Typical', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='excellent-standard', form='Excellent', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='sustainability', form='sustainability', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='generative-artificial-intelligence', form='generative artificial intelligence', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='generative-artificial-intelligence', form='GenAI', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
       dict(concept='psrb', form='PSRBs', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='competence-standard', form='competence standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []
B5 = []

D3 = [dict(citation='Equality and Human Rights Commission, the most recent guidance on competence standards (named in 4.3, not identified)', settles=['SB5', 'SB6'], asked='2026-10-03', state='wanted'),
      dict(citation='QAA (2024) the Quality Code, the update named in the front matter', settles=['SB6', 'S7'], asked='2026-10-03', state='wanted')]

# ------------------------------------------------------------------ Part E
E = [
    "SB4, rung shape: two tables (4.6 knowledge and understanding, five rows; 4.8 subject-specific and intellectual skills, nine rows), each row given once under three column heads, Threshold (3rd), Typical (2nd), Excellent (1st); recorded one S4 record per rung on each cell's span (batch 1 convention). The rungs are defined once, in 4.4, not by lead-ins above lists: a new shape against Psychology.",
    "SB4, gradeOf: every typical and excellent cell links to the cell to its left in the same row, basis stated (the issuer pairs the cells by row; 4.7 and 4.9 add that the higher rungs include the lower). No inferred link.",
    "SB4, flattened tables: 4.6 and 4.8 are flattened in the held text, cells running row by row, threshold, typical, excellent. Placements read with some doubt, for P3: 4.6 row 1 (the threshold cell 'The writings of some major philosophers.' runs straight into the typical cell); 4.8 row 5, Explaining (the excellent cell 'Tailor explanations...' sits after a paragraph break); 4.8 rows 7 and 8 (cells broken across lines). 4.6 rows carry no labels: the row names in SB4 are ours.",
    "SB4, force: threshold cells take force `threshold` with forceFrom 4.4, where the issuer defines the threshold as the minimum for the award; typical and excellent cells take 'will' from the table lead-ins in 4.6 and 4.8 (forceFrom gives the lead-in text).",
    "SB4, the master's list (4.11) is an outcome list for another award, recorded as rung threshold, award master's, level fheq:7, id suffix .masters (batch 1 convention). The issuer gives no master's rungs, though 4.3 speaks of threshold, typical and excellent standards 'for undergraduate and master's level'.",
    "SB4, 4.10 generic skills: an outcome list at undergraduate level with no rung lead-in; recorded rung none, level fheq:6. 2.7 calls the generic skills 'threshold-level': for P3, whether they should carry rung threshold.",
    "S3, std-prep: the skeleton read 4.4's three definition bullets as threshold items because the bullets name the rungs; they define the rungs and are not statements. The skeleton found no typical or excellent items (the tables are flattened).",
    "S3, std-prep: the skeleton's component spans end with the next sub-heading (for example 1.1 ends 'Purposes and characteristics'; 1.4 ends 'Equity, diversity and inclusion Enabling potential'); the cut is the issuer's numbering and is kept; headings are in SUB.",
    "S4, not taken as statements (descriptive, for P3): 1.2 ('students will ask, and attempt to answer'); 1.3 (fourteen benefits of study, 'provides ... the ability to', plain present); 1.4 (ten social purposes); 1.26 (graduates 'are ready' for leadership, plain present); 2.11 (master's students 'will complete' modules: curricular); 2.16 ('will form part' of review); 4.1 (the standards 'a student will have demonstrated': framing for the tables); 4.7 and 4.9 (rung inclusion, recorded in rungBases).",
    "S4, plain-present provider norms (template open point 5), not statements: 1.6, 1.7, 1.10, 1.13 (three anticipatory practices), 1.14, 1.15, 3.3, 3.6, 3.10, 3.12, 3.14, 3.17, 3.18.",
    "S4, obliging words outside the five: 'it is expected that' (2.7, 2.8, 2.12) and 'expected to' (4.5); 'it is important that' (3.8, 3.13); 'is imperative' (1.9); 'is encouraged' (1.12). 4.5 is taken as a statement with force describes; the others are not statements, or their force sits beside a stated must, should or will. For Abbott: should 'expected to' read as should?",
    "S4, 3.19: 'transparency must be ensured' is passive and names no duty-holder; recorded as a provider duty (addressee provider). For P3: whether students share it.",
    "S4, 3.15: the stem's 'will test for' gives three provider records (3.15.b1 to b3); the stem's first sentence ('will balance the need to test...') is folded into 3.15.b1's paraphrase.",
    "S4, 1.11 and 1.18: one sentence in each paragraph obliges (should); the record's span is the whole numbered paragraph, as the issuer numbers it.",
    "S5, crosswalks: 2.10 pairs the CertHE with FQHEIS Level 8 and the DipHE with FQHEIS Level 9; the FHEQ's Table 1 (std:doc:qaa-fheq-2024-framework, S5) gives FQHEIS 7 and 8. Recorded as stated and conflicting; likely an issuer error. 2.4 and 2.7 give honours as 'FQHEIS Levels 9/10'; Table 1 puts honours at 10 and other bachelor's at 9.",
    "S5, levels: spine:6 and spine:7 are inferred from the reference framework (std:ref:uk-framework R2), not stated. CQFW is not cited by the statement.",
    "S2 and front matter, codes: HECoS 100791 'mental philosophy' entered for 'philosophy of mind' as inferred; no HECoS term for logic, aesthetics or political philosophy. Liberal arts (100065) is in statedSubjects only, as a programme the subject may be part of.",
    "S1, S8: 'Fifth edition Published - 10 April 2025' with copyright 2024; published recorded as 2025-04. The previous statement is named only as 'the previous Subject Benchmark Statement'; the advisory group lists name a 2019 minor update and 2015, 2007 and 2000 editions (recall-free: read from the back matter).",
    "S1, licence: the text gives a copyright notice and no re-use terms.",
    "SB5: no professional body accredits philosophy; PSRBs appear only in general. The Office for Students, the EHRC and the Disabled Students Commission are named; their requirements are not ingested. Advance HE is named only as co-author of the ESD guidance (SB6).",
    "SB6, themes: the statement names five cross-cutting themes, generative AI the fifth (theme:generative-ai, batch 1 convention). EDI is named 'Equity', not 'Equality'. 1.4 (diverse cultures) and 1.33.b3 (diversity in assessment) touch EDI without naming it and are not tagged.",
    "SB6, back matter: the references list (excluded matter) names the BPA and SWIP report on women in philosophy, the Diversity Reading List, QAA's advice on inclusive subject learning communities and the SOAS decolonising philosophy toolkit; not ingested.",
    "S9: not researched in P1.",
    "Patterns against Psychology: rung tables, not lists; rungs defined in 4.4 with class equivalents; a master's list as the last subsection; generic skills as a separate list at undergraduate level; a fifth theme (generative AI); no PSRB; rungs written for single honours only (4.5).",
]
