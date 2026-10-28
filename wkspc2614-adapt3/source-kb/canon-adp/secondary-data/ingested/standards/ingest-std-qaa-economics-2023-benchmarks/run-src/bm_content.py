# Judgement for run 0102, QAA Economics Subject Benchmark Statement (March 2023), std run agent.
# Keys are S4 ids under qaa/economics-2023/. Built by tools/bm_build.py (brief BM-BRIEF.md 0.2.2).
HON = "bachelor's with honours"
SID = 'qaa/economics-2023/'
CITE = 'QAA (2023) Economics Subject Benchmark Statement'

META = dict(
    run='0102', p1='2026-10-03 17:10',
    title='Subject Benchmark Statement Economics',
    heading='Subject Benchmark Statement: Economics (QAA, March 2023)',
    edition='March 2023 (fifth edition)', published='2023-03',
    status='current',
    supersedes='the fourth edition (2019; not yet ingested): std:doc:qaa-economics-2019-benchmarks',
    subjects=[
        dict(scheme='hecos', code='100450', label='economics', basis='stated'),
        dict(scheme='cah', code='CAH15-02-01', label='economics', basis='stated'),
        dict(scheme='cah', code='CAH15-02', label='economics', basis='stated'),
        dict(scheme='cah', code='CAH15', label='social sciences', basis='stated'),
        dict(scheme='hecos', code='100604', label='econometrics', basis='stated'),
        dict(scheme='hecos', code='101401', label='microeconomics', basis='stated'),
        dict(scheme='hecos', code='101402', label='macroeconomics', basis='stated'),
        dict(scheme='hecos', code='100301', label='economic history', basis='stated'),
        dict(scheme='hecos', code='100452', label='international economics', basis='inferred'),
        dict(scheme='hecos', code='100601', label='economic policy', basis='inferred'),
    ],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, revised series with cross-cutting themes (2022 onward; recall, to check); fifth edition for Economics (D1, back cover)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what an Economics graduate should know, understand and be able to do at the end of a "
                     "bachelor's degree with honours, single or with economics as the major part: three rungs of achievement (threshold, "
                     "typical, excellent) of eight items each, two lists of core abilities and course outcomes, and a few expectations on "
                     "courses. Reach for it when designing, reviewing or describing an economics course or its outcomes. It is not a "
                     "curriculum, not an accreditation standard and not a regulatory requirement in England."),
    summary=("Published by QAA in March 2023 as the fifth edition, the statement describes economics as a social science, the purposes "
             "and distinctive features of a degree, its content, teaching and assessment; it then sets benchmark standards at threshold, typical "
             "and excellent levels for honours degrees (FHEQ level 6, FQHEIS level 10), with the eight items running in parallel across "
             "the three rungs. It adds the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; "
             "enterprise and entrepreneurship education), aligns its core skills with the Advance HE and QAA ESD guidance and the UN SDGs, "
             "and points to Annex D's degree classification descriptions for achievement above threshold. It names no accrediting body; "
             "PSRBs appear only in general terms and the Royal Economic Society as a widening-participation partner."),
    authority='reference: a sector reference point, "not a regulatory requirement" (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)',
)

S2 = dict(
    governs="the knowledge, understanding and skills expected of an Economics graduate on completing an honours degree, the nature of such degrees and the standards at three rungs (D1, front matter: About this Statement; 1.1; 4.1)",
    awards=["bachelor's degrees with honours in Economics, single honours or with Economics as a major component (4.1)",
            "combined, joint or major-minor routes (2.4; rungs not all expected where Economics is a minor component, 4.1)"],
    levels=['fheq:6', 'fqheis:10'],
    statedScope='"This document sets out benchmark standards for undergraduate degrees in Economics." (D1, 1.1)',
    statedSubjects=[
        dict(name='Economics', locator='(D1, title; 1.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100450', label='economics'), dict(scheme='cah', code='CAH15-02-01', label='economics')]),
        dict(name='a single honours degree in Economics and joint degrees where Economics is a major component', locator='(D1, 4.1; 3.1)', kind='programme title',
             codes=[dict(scheme='hecos', code='100450', label='economics')]),
        dict(name='a combined, joint or major-minor route', locator='(D1, 2.4)', kind='programme title',
             codes=[dict(scheme='hecos', code='100450', label='economics')]),
        dict(name='econometrics', locator='(D1, 3.3; 3.5)', kind='specialism', codes=[dict(scheme='hecos', code='100604', label='econometrics')]),
        dict(name='the core fields of micro and macroeconomics', locator='(D1, 1.3; 3.5)', kind='specialism',
             codes=[dict(scheme='hecos', code='101401', label='microeconomics'), dict(scheme='hecos', code='101402', label='macroeconomics')]),
        dict(name='economic history and history of economic thought', locator='(D1, 2.2; 3.6)', kind='specialism',
             codes=[dict(scheme='hecos', code='100301', label='economic history')]),
        dict(name='international macroeconomics and finance; international trade and migration', locator='(D1, 3.5)', kind='specialism',
             codes=[dict(scheme='hecos', code='100452', label='international economics')]),
        dict(name='political economy', locator='(D1, 3.5)', kind='specialism', codes=[dict(scheme='hecos', code='100601', label='economic policy')]),
        dict(name='behavioural, development, environmental, experimental, health, labour, monetary and public economics; growth; industrial organisation', locator='(D1, 3.5)', kind='specialism', codes=[]),
    ])

SECTIONS = {'1': 'Context and purposes of an Economics degree', '2': 'Distinctive features of an Economics degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.1', 'Context and purposes of an Economics degree'),
       ('1.2', '1.6', 'Purposes and characteristics of an Economics degree'),
       ('1.7', '1.9', 'Equality, diversity and inclusion (EDI)'),
       ('1.10', '1.14', 'Accessibility'),
       ('1.15', '1.19', 'Sustainability'),
       ('1.20', '1.26', 'Enterprise and entrepreneurship education'),
       ('2.1', '2.2', 'Design'), ('2.3', '2.5', 'Progression'), ('2.6', '2.6', 'Flexibility'),
       ('2.7', '2.8', 'Partnership'), ('2.9', '2.12', 'Monitoring and review'),
       ('3.1', '3.6', 'Content'), ('3.7', '3.11', 'Teaching and learning'), ('3.12', '3.15', 'Assessment'),
       ('4.1', '4.2', 'Introduction'), ('4.3', '4.3', 'Threshold level'), ('4.4', '4.4', 'Typical level'), ('4.5', '4.5', 'Excellent level')]

G = {
    '1.1': 'what the statement covers: the subject, typical aims, knowledge and skills, learning and assessment and the three rungs',
    '1.2': 'economics defined: decisions and interaction within institutions and power, allocation of resources, well-being and sustainability (S4 none)',
    '1.3': 'micro and macro, static and dynamic analysis; contested interpretations call for plural perspectives and evidence (S4: the requirement of understanding)',
    '1.4': 'a broad social science linked to many disciplines and core to finance, business and accounting',
    '1.5': 'joint and innovative degrees; employment across sectors; knowing the limits of the tools; responsible citizenship',
    '1.6': 'stem: the core intellectual abilities economists need (six items, S4)',
    '1.7': 'the subject studies discrimination and inequality; teachers should foster an inclusive community and embed EDI (S4), with example actions',
    '1.8': 'evidence-based debate on sensitive EDI questions, held inclusively',
    '1.9': "the profession's narrow make-up and the need for compassionate, inclusive teaching",
    '1.10': 'teaching that answers the needs of the student body through an accessible, inclusive curriculum (S4)',
    '1.11': 'curricula in which a diverse community can recognise itself',
    '1.12': 'blended and online delivery since 2020: chances for inclusion and risks to equal access',
    '1.13': 'digital accessibility of graphs, media, data and software (S4)',
    '1.14': 'digital capability and published examples of accessibility practice',
    '1.15': 'sustainability framed by the UN SDGs and Global Compact, defined and woven into concepts and models',
    '1.16': 'graduates able to face the planetary crisis; critical and creative capacities beyond set tools (S4)',
    '1.17': 'stem: core skills aligned with the ESD guidance competencies and four named SDGs',
    '1.18': 'economics as a basis for sustainable, evidence-informed policy and for communicating it',
    '1.19': 'areas of economics that address environmental limits, valuation, market failure and equity',
    '1.20': 'enterprise and entrepreneurship education: what it is and what it offers students',
    '1.21': 'transferable skills relevant to enterprise',
    '1.22': 'data software and data handling skills of graduates',
    '1.23': 'communicating economics to wide audiences in many media',
    '1.24': 'placements and work experience and the attributes they build',
    '1.25': 'real-world, interdisciplinary application and how theory has changed with policy challenges',
    '1.26': 'enterprise education beyond employment: a self-directed life and civic contribution',
    '2.1': 'broad, rigorous design; a core of methods and tools applied in field modules',
    '2.2': 'mathematics on entry and support (S4); research-led teaching; stem of eight typical course outcomes (S4)',
    '2.3': 'progression through levels to the threshold skills; readiness for postgraduate study',
    '2.4': 'joint and combined routes reach core skills and add others (S4)',
    '2.5': 'exit awards and four-year Scottish honours; part-time routes',
    '2.6': 'mixed modes of delivery, independent learning and varied materials',
    '2.7': 'degree apprenticeships and placements with outside organisations',
    '2.8': 'widening participation with the Royal Economic Society and others',
    '2.9': 'course monitoring and review, with students taking part (S4)',
    '2.10': 'external reviewers in periodic review (S4)',
    '2.11': 'external examiners and how the statement supports them',
    '2.12': 'accreditation of courses with professional outcomes by professional and regulatory bodies',
    '3.1': 'content adapts to the degree; the statement does not prescribe forms of analysis',
    '3.2': 'stem and area: eight key concepts most courses cover (one item obliges, S4)',
    '3.3': 'data, programming and econometric skills on real data (S4)',
    '3.4': 'selecting and applying tools to applied topics and policy as an essential outcome (S4)',
    '3.5': 'stem and area: fourteen common applied fields',
    '3.6': 'economic history and the history of economic thought as context',
    '3.7': 'growing critical facility and independence; a range of teaching methods',
    '3.8': 'interactive, student-centred and blended learning since the pandemic',
    '3.9': 'resources and organisations that support economics teaching',
    '3.10': 'language, mathematics and study-skills support for diverse cohorts (S4)',
    '3.11': 'pluralist and decolonial approaches supporting inclusion',
    '3.12': 'assessment design at module and course level',
    '3.13': 'assessment that builds problem-solving and higher-order reasoning',
    '3.14': 'a range of assessment forms, including authentic and data-based tasks',
    '3.15': 'formative assessment and scaffolded skills development',
    '4.1': 'where the rungs apply (single honours and major joint degrees); typical includes threshold',
    '4.2': 'most students exceed the threshold; providers should use Annex D (S4)',
    '4.3': 'rung lead-in: threshold, eight items',
    '4.4': 'rung lead-in: typical, eight items',
    '4.5': 'rung lead-in: excellent, eight items, shown consistently',
}
CTYPE = {'3.2': 'area', '3.5': 'area', '3.6': 'area',
         '2.6': 'practice', '3.7': 'practice', '3.8': 'practice', '3.9': 'practice', '3.11': 'practice',
         '3.12': 'practice', '3.13': 'practice', '3.14': 'practice', '3.15': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1 and S2'),
    dict(number='none', heading='Contents', kind='contents'),
    dict(number='1 to 4', heading='section heading lines', kind='other: headings, kept as section components'),
    dict(number='5', heading='List of references and further resources', kind='references'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Economics', kind='acknowledgements'),
    dict(number='none', heading='back cover: edition, publication date, membership note, copyright', kind='other: read for S1 and S8'),
]

P = {}
def s(i, **k):
    P[i] = k

# ------------------------------------------------------------------ paragraph statements
s('1.3', find=("Studying economics requires an understanding of how resources are used and how economic and social entities, such as "
               "households, firms, governments and other institutions, behave and interact. This understanding is required at both the "
               "individual (micro) and the aggregate (macro) level as well as with respect to the relationship between the individual and society."),
  type='requirement', rung='none', force='must', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['requires', 'behave', 'interact', 'required'], about='understanding resource use and economic behaviour at micro and macro levels',
  domain='understanding', award=HON,
  para="Studying the subject must rest on understanding how resources are used and how households, firms, governments and other bodies behave and interact, at the level of the single actor, of the whole economy and of the link between person and society.",
  prac="Design the course so that every student builds an understanding of resource use and of how economic actors behave and interact, at both micro and macro level and in how individuals relate to society.",
  ben="You must come to understand how resources are used and how households, firms, governments and other bodies behave and interact, both one by one and across the whole economy.",
  aaw=("Treat this as a requirement of studying the subject (the issuer's word is 'requires', read as must): an understanding of resource use and "
       "economic behaviour at micro and macro levels, for honours at FHEQ level 6. Cite " + CITE + ", para 1.3, and do not present it as a rung item "
       "or a regulatory rule. Set it beside the threshold items qaa/economics-2023/4.3.b1 and 4.3.b2 and the honours descriptor qaa/fheq-2024/4.15.b1."),
  aad=("Raise this when a student is unsure why both microeconomics and macroeconomics are taught, or when a team reviews the core modules. "
       "Explain to a student that you need to grasp both how single actors decide and how the economy behaves as a whole; for staff, frame it as what "
       "the core must secure. Ask \"Can you explain one idea at each level and how the two connect?\" Avoid reciting the paragraph or treating it as a graded rung."))

s('1.7', find=("Economics educators should aim to foster an inclusive learning community and consider how to embed EDI in learning materials "
               "(such as readings, lecture slides, videos, and so on), methods and processes."),
  type='expectation', rung='none', force='should', level='none', appliesTo='teaching staff in economics', addressee='provider',
  verbs=['aim', 'foster', 'consider', 'embed'], about='an inclusive learning community and EDI in materials and methods', domain='none', award='none',
  para="Teachers of economics should work towards an inclusive learning community and think about how to build equality, diversity and inclusion into their materials, methods and processes.",
  prac="Aim to build an inclusive learning community and plan how equality, diversity and inclusion shape your readings, slides, videos, methods and processes; the statement's examples include widening participation, countering under-representation, zero tolerance of harassment, anticipating neurodiverse access and closing awarding gaps.",
  ben=('n/a', 'a duty on teaching staff and the course; the student meets its effect, not a standard to reach'),
  aaw=("Present this as an expectation on teaching staff (should), not on students, about inclusive learning communities and embedding EDI in "
       "materials and methods. Cite " + CITE + ", para 1.7, and do not claim the listed efforts in 1.7's bullets are required: the issuer offers them as "
       "examples. Set it beside the accessibility expectations qaa/economics-2023/1.10 and 1.13 and the EDI discussion in 1.8 and 1.9."),
  aad=("Raise this with a programme team reviewing materials, reading lists or assessment for inclusion. Frame it for staff as an aim to work towards and ask "
       "\"Whose experiences do your readings and examples show?\" and \"Which of the example actions, such as closing awarding gaps, does your course take?\" "
       "Do not give it to a student as something they must do."))

s('1.10', find=("Pedagogic methods for teaching Economics will generally reflect the needs of the student body, with an inclusive curriculum that "
                "prioritises the accessibility, equity, appropriateness and resourcing of learning and teaching resources and materials being key."),
  type='expectation', rung='none', force='will', level='none', appliesTo='teaching in economics', addressee='provider',
  verbs=['reflect', 'prioritises'], about='teaching that answers student needs, with accessible resources', domain='none', award='none',
  para="Teaching methods will generally respond to what the students in a cohort need, with an inclusive curriculum that puts accessible, fair, suitable and properly resourced materials first.",
  prac="Expect your teaching approach to respond to the students you actually have, and make an inclusive curriculum with accessible, equitable, fitting and well-resourced materials a priority.",
  ben=('n/a', 'an expectation on teaching and the curriculum; the student meets its effect'),
  aaw=("Present this as an expectation on teaching (will, generally), not a student outcome: methods respond to student needs and an inclusive, accessible "
       "curriculum is key. Cite " + CITE + ", para 1.10, and do not turn it into a promise of particular adjustments. Set it beside "
       "qaa/economics-2023/1.13 on digital accessibility and qaa/economics-2023/1.7 on inclusion."),
  aad=("Raise this when a team plans materials or delivery, or reviews accessibility after student feedback. For staff, ask \"How do your methods change for "
       "the students in this cohort?\" and \"Which materials are not yet accessible?\" Do not present it to a student as their responsibility."))

s('1.13', find=("As a discipline that utilises graphical and other visual tools, Economics pay attention to digital accessibility of materials which "
                "should include, for example, image descriptions."),
  type='expectation', rung='none', force='should', level='none', appliesTo='economics teaching materials', addressee='provider',
  verbs=['pay', 'include'], about='digital accessibility of visual materials, media and software', domain='none', award='none',
  para="Because economics relies on graphs and other visuals, its digital materials should be accessible, for instance through image descriptions; the paragraph goes on to ask for screen-reader-ready content, captions or transcripts, downloadable formats and accessible alternatives for data, software and coding.",
  prac="Make graphs and other visuals accessible, for example with image descriptions; check that digital content works with screen readers, has captions or transcripts for audio and video, can be downloaded in different formats, and that data, specialist software and coding tasks have accessible alternatives.",
  ben=('n/a', 'a duty on the course and its staff; the student meets its effect'),
  aaw=("Present this as an expectation on the course and its staff (should) for the digital accessibility of graphs, media and specialist software. Cite "
       + CITE + ", para 1.13, and do not claim it sets a legal standard or a student outcome. Set it beside qaa/economics-2023/1.10 and the examples of practice in 1.14."),
  aad=("Raise this when staff prepare slides, graphs, recordings or coding tasks. Ask \"Can a screen-reader user follow your diagrams?\" and \"Is there an "
       "alternative to the specialist software?\" Do not put this duty to a student; a student who meets a barrier can be pointed to the course team."))

s('1.16', find=("Reflecting the UN SDGs and their educational implications, a governing purpose of Economics degrees is that graduates have developed "
                "capacities that enable them to cope with and attempt to create solutions for the planetary crisis of climate change, biodiversity loss, "
                "environmental injustice and potential, consequent instabilities. These problems are fundamentally transdisciplinary and highly dynamic "
                "and are characterised by pervasive uncertainty. As such, they require students to foster critical and creative capacities beyond the "
                "application of existing tools and models."),
  type='requirement', rung='none', force='must', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
  verbs=['developed', 'cope', 'create', 'require', 'foster'], about='capacities to face the planetary crisis', domain='generic-skill', award=HON,
  para="A governing aim of the degree is that graduates can cope with, and try to solve, the planetary crisis (a changing climate, lost biodiversity, environmental injustice and the instability these bring); because such problems cross disciplines, change fast and are deeply uncertain, students must develop critical and creative capacities that go past applying familiar tools and models.",
  prac="Build the course so graduates develop the capacity to cope with and seek solutions to the planetary crisis; these problems must push students past applying familiar tools and models towards critical and creative thinking.",
  ben="You must develop critical and creative abilities that go beyond applying the usual tools and models, so that you can cope with the planetary crisis, such as a changing climate and lost biodiversity, and help find solutions.",
  aaw=("Present this as a requirement the issuer states ('require', read as must) for honours graduates at FHEQ level 6: critical and creative capacities "
       "to address the planetary crisis, beyond applying set tools. Cite " + CITE + ", para 1.16, and do not claim it is a regulatory rule or a rung item. "
       "Set it beside the excellent rung item qaa/economics-2023/4.5.b8, the ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance) and the honours "
       "descriptor qaa/fheq-2024/4.15.b7."),
  aad=("Raise this when a student or team asks how sustainability fits an economics degree. Tell a student plainly that you need to think critically and "
       "creatively about climate and nature problems, not only apply standard models; with staff, ask where the course stretches students past textbook tools. "
       "Ask \"Where have you had to go beyond a standard model to tackle an environmental problem?\" Avoid reading the paragraph aloud or turning it into a topic list."))

s('2.2', find=("Where the degree does not require Maths A Levels for entry, the expectation is that suitable teaching and support is provided within "
               "the degree to ensure that students are able to engage with the more quantitative elements of the course."),
  type='expectation', rung='none', force='describes', level='none', appliesTo='courses admitting students without A level mathematics', addressee='provider',
  verbs=['require', 'provided', 'ensure', 'engage'], about='support for quantitative work where mathematics is not an entry condition', domain='none', award='none',
  para="Where entry does not call for A level mathematics, the issuer expects the degree itself to give suitable teaching and support so that students can take on its quantitative parts.",
  prac="If you admit students without A level mathematics, provide suitable teaching and support within the degree so they can take on its quantitative content.",
  ben=('n/a', 'an expectation on the course; the student meets its effect'),
  aaw=("Present this as an expectation on the course, worded 'the expectation is that' and recorded as describes because the phrase is outside the five "
       "obliging words: where entry asks for no A level mathematics, suitable teaching and support are provided for quantitative work. Cite " + CITE +
       ", para 2.2, and do not claim it creates or forbids a mathematics entry condition. Set it beside the support note qaa/economics-2023/3.10 and the "
       "methods rung item qaa/economics-2023/4.3.b3."),
  aad=("Raise this when a team reviews admissions or first-year support, or when a student without A level mathematics worries about the quantitative modules. "
       "For staff, ask \"What support do students without A level maths get, and when?\"; for a student, explain plainly that the course is expected to help you "
       "build the maths you need. Do not present it to a student as a duty of theirs."))

s('2.4', find=("Undergraduates studying a combined, joint or major-minor route will achieve core elements of the specific and generic skills for the "
               "subject, and will add others according to the subjects covered in joint courses."),
  type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on combined, joint or major-minor routes', addressee='learner',
  verbs=['achieve', 'add'], about='joint and combined routes: the core skills plus others', domain='subject-skill', award=HON,
  para="Students on a combined, joint or major-minor route will gain the core subject-specific and generic skills of economics and will add others from the other subjects they take.",
  prac="On joint or combined routes, plan for students to reach the core subject-specific and generic skills of economics, alongside the skills their other subject adds.",
  ben="If you study economics with another subject, you will gain the core economics skills, both subject-specific and general, and add others from your second subject.",
  aaw=("Present this as an expected outcome (will) for students on combined, joint or major-minor honours routes at FHEQ level 6: core elements of the "
       "subject's skills, with others added by the second subject. Cite " + CITE + ", para 2.4, and do not claim joint students meet every rung item, since "
       "paragraph 4.1 applies the rungs only where economics is a major component. Set it beside the threshold list qaa/economics-2023/4.3.b1 to 4.3.b8."),
  aad=("Raise this when a joint or combined honours student asks whether they are held to the same standards as single honours students. Tell them plainly "
       "that you will build the core economics skills and gain others from your second subject; for staff, frame it as what the joint route must still secure. "
       "Ask \"Which core economics skills does your timetable cover, and where?\" Do not suggest every rung item applies where economics is the minor part."))

s('2.9', find=("Degree-awarding bodies and their collaborative partnerships routinely collect and analyse information and undertake periodic course "
               "review according to their own needs, and students should form part of this monitoring and review process."),
  type='expectation', rung='none', force='should', level='none', appliesTo='degree-awarding bodies and their partners', addressee='provider',
  verbs=['collect', 'analyse', 'undertake', 'form'], about='students taking part in monitoring and review', domain='none', award='none',
  para="Degree-awarding bodies and their partners review courses periodically for their own purposes, and students should take part in that monitoring and review.",
  prac="Include students in course monitoring and periodic review, alongside the information you collect and the external reference points you use.",
  ben=('n/a', 'a duty on the degree-awarding body to involve students; not a standard for the student to reach'),
  aaw=("Present this as an expectation on degree-awarding bodies and their partners (should): students take part in monitoring and periodic review. Cite "
       + CITE + ", para 2.9, and do not claim it sets a review cycle or a student outcome. Set it beside the external review expectation qaa/economics-2023/2.10."),
  aad=("Raise this with a programme team planning annual monitoring or periodic review. Ask \"How do students take part in review, beyond surveys?\" and "
       "\"How are their views reported back?\" Do not present it to a student as an obligation; a student asking how to have a say can be told the course should involve them."))

s('2.10', find=("Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed "
                "changes and ensure threshold standards are achieved and content is appropriate for the subject."),
  type='expectation', rung='none', force='will', level='none', appliesTo='higher education providers', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award='none',
  para="Providers will bring in external reviewers during periodic review to gain an outside view of proposed changes, make sure threshold standards are met and check that content suits the subject.",
  prac="Use external reviewers in periodic review to test proposed changes, confirm that threshold standards are achieved and check that content fits the subject.",
  ben=('n/a', 'a duty on the provider; the student meets its effect'),
  aaw=("Present this as an expected practice of providers (will): external reviewers in periodic review to secure threshold standards and suitable content. "
       "Cite " + CITE + ", para 2.10, and do not claim the statement sets how reviewers are chosen. Set it beside qaa/economics-2023/2.9 and the threshold "
       "list qaa/economics-2023/4.3.b1 to 4.3.b8."),
  aad=("Raise this with a team preparing for periodic review. Ask \"Which external reviewer will look at the proposed changes?\" and \"Which threshold items "
       "will they check?\" Do not raise it with students as a standard they meet."))

s('3.2.b5', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['trained', 'recognise'], about='marginal analysis and its limits', domain='understanding', award=HON,
  para="Economists learn that key decisions often turn on small changes in variables and parameters; students should also know where marginal analysis fails, as with strong threshold effects or discontinuities such as planetary crises.",
  prac="Teach marginal reasoning, and make sure students also learn where it breaks down, for example where threshold effects or sudden discontinuities, such as those in planetary crises, dominate.",
  ben="You should know how decisions often turn on small changes, and also where that way of thinking stops working, such as when sudden tipping points occur.",
  aaw=("Present this as an expectation on students (should) inside the list of key concepts most courses cover: awareness of the limits of marginal analysis, "
       "at FHEQ level 6. Cite " + CITE + ", para 3.2 (the marginal considerations item), and do not claim the rest of 3.2's concept list is required, as it "
       "describes what most courses cover. Set it beside qaa/economics-2023/4.3.b8 (more than one approach) and the honours descriptor qaa/fheq-2024/4.15.b4 "
       "on the limits of knowledge."),
  aad=("Raise this when a student applies marginal reasoning to a problem with tipping points, such as climate or financial crises. Ask \"Would a small change "
       "here have a small effect, or could it tip the system?\" Explain plainly that you should know when the marginal tool stops working; with staff, ask where "
       "the course shows its limits. Avoid presenting the full list of key concepts as a checklist."))

s('3.3', find=("Appropriate data, programming, visualisation and other computing skills required in the modern economics profession will be introduced "
               "within the degree course, with particular attention to the study of causality. These include appropriate mathematical and statistical "
               "methods, including econometrics. Students will have exposure to the use of such techniques on actual economic, financial or social data, "
               "using suitable statistical or econometric software. In addition, students will learn about the nature, sources and uses of both "
               "quantitative and qualitative data and an ability to select and apply appropriate methods that economists might use to analyse such data."),
  type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of the subject and their course', addressee='both',
  verbs=['introduced', 'learn', 'select', 'apply'], about='data, programming and econometric skills on real data', domain='subject-skill', award=HON,
  para="The degree will introduce the data, programming, visualisation and computing skills the profession needs, with stress on causality and on mathematical, statistical and econometric methods; students will use them on real data with suitable software and will learn about the kinds, sources and uses of data and how to choose methods for it.",
  prac="Introduce data, programming, visualisation and computing skills, with mathematical, statistical and econometric methods and a focus on causality; give students practice on actual economic, financial or social data in suitable software, and teach the nature and sources of quantitative and qualitative data and how to choose methods.",
  ben="You will learn data, programming, visualisation and computing skills, including statistics and econometrics, use them on real economic or social data with suitable software, and learn how to choose the right method for the data.",
  aaw=("Present this as an expected outcome and course commitment (will) at FHEQ level 6: data, programming and econometric skills, practised on real data, "
       "with attention to causality. Cite " + CITE + ", para 3.3, and do not name particular software or languages as required, since the statement names none. "
       "Set it beside the methods rung items qaa/economics-2023/4.3.b3, 4.4.b3 and 4.5.b3 and the honours descriptor qaa/fheq-2024/4.15.b2."),
  aad=("Raise this when a student asks why coding or econometrics is in the course, or when staff plan where data skills are taught. Tell a student plainly that "
       "you will learn to work with real data using statistical software, and ask \"Which real dataset have you analysed, and how did you choose the method?\" "
       "For staff, ask where causality is taught. Do not imply a particular package is compulsory."))

s('3.4', type='outcome', rung='none', force='should', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['select', 'apply', 'learn', 'discuss', 'analyse', 'evaluate'], about='choosing and applying economic tools to applied topics and policy',
  domain='subject-skill', award=HON,
  para="An essential outcome is the judgement and skill to choose and use economic tools, principles and reasoning across applied topics, including how economics can shape and interpret economic, social and environmental policy; students should also learn to talk about and analyse government policy and judge how the UK and other economies have performed.",
  prac="Make sure students can choose and apply the right economic tools and reasoning to applied fields and to policy design and evaluation, and that they learn to examine government policy and the performance of economies past and present.",
  ben="You should learn to choose and use the right economic tools and reasoning for real topics, and to examine government policy and how economies, including the UK's, have performed.",
  aaw=("Present this as an essential learning outcome with the force should, at FHEQ level 6: judgement in selecting and applying economic tools to applied "
       "topics and policy. Cite " + CITE + ", para 3.4, and do not claim it fixes which applied fields a course must offer, since 3.5 lists common ones only. "
       "Set it beside the policy rung items qaa/economics-2023/4.3.b5, 4.4.b5 and 4.5.b5, the outcome qaa/economics-2023/2.2.b6 and the honours descriptor qaa/fheq-2024/4.15.b6."),
  aad=("Raise this when a student is choosing which model to use for a real problem or a policy question. Ask \"Why is this the right tool here, and what would "
       "another tool tell you?\" Explain plainly that you should pick tools with judgement, not by habit; with staff, ask where students practise this choice. "
       "Avoid reading the paragraph aloud."))

s('3.10', find=("As the student body in many undergraduate Economics courses can be international and otherwise diverse, course leaders need to think "
                "about specific help for students to deal with language issues, mathematics support (as use of mathematics might be quite different from "
                "the focus in school), and study and exam skills support."),
  type='expectation', rung='none', force='describes', level='none', appliesTo='course leaders', addressee='provider',
  verbs=['think', 'deal'], about='support for language, mathematics and study skills', domain='none', award='none',
  para="Because many cohorts are international and diverse, course leaders need to consider specific help with language, mathematics and study and exam skills, since university economics differs from study at school.",
  prac="Plan specific support for language, mathematics (which may differ from school maths) and study and exam skills, given international and diverse cohorts and the jump from school-level economics.",
  ben=('n/a', 'an expectation on course leaders; the student meets its effect'),
  aaw=("Present this as an expectation on course leaders, worded 'need to' and recorded as describes because the phrase is outside the five obliging words: "
       "specific language, mathematics and study-skills support. Cite " + CITE + ", para 3.10, and do not claim it sets a level of provision. Set it beside "
       "qaa/economics-2023/2.2 (support where maths is not an entry condition) and qaa/economics-2023/1.10."),
  aad=("Raise this with a team planning induction, first-year support or exam preparation. Ask \"What help do students get with mathematics that differs from "
       "school, and with academic English?\" Do not present it to a student as their duty; point a student who is struggling to the support the course should offer."))

s('4.2', find=("The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider "
               "has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification "
               "descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees."),
  type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['perform', 'determining', 'refer'], about='achievement above threshold and the use of Annex D', domain='none', award=HON,
  para="Most students will do much better than the minimum threshold; each provider decides what evidence shows this and should refer to Annex D, which describes the four honours classes.",
  prac="Expect most students to exceed the threshold; set your own way of evidencing achievement above it, and refer to the Annex D descriptions of degree classes when doing so.",
  ben=('n/a', 'a duty on the provider in judging and classifying achievement'),
  aaw=("Present this as two claims: a prediction (will) that most students exceed the threshold, and an expectation on providers (should) to use Annex D when "
       "judging achievement above it. Cite " + CITE + ", para 4.2, and do not equate the typical or excellent rung with a degree class, as the statement makes "
       "no such mapping. Set it beside Annex D in std:doc:qaa-fheq-2024-framework (for example qaa/fheq-2024/annex-d/summary/r1/3rd) and the rung lists 4.3 to 4.5."),
  aad=("Raise this when staff align marking criteria or classification with the rung lists. Ask \"How do your class descriptors use Annex D?\" and \"Where would "
       "a typical graduate's work sit?\" Do not tell a student that the typical rung equals a 2.1 or that the threshold is a target."))

# ------------------------------------------------------------------ 1.6: core abilities economists need (lead-in: "Economists need the ability to:")
def k16(n, verbs, about, domain, para, prac, ben, near, fheq, plain, q, find=None):
    r = dict(type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='economists, and students in training', addressee='learner',
             verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben, forceFrom='1.6',
             aaw=("Describe this as one of the core abilities the statement says economists need (" + about + "); the issuer's word is 'need', recorded as "
                  "describes, so give it no must or should. Cite " + CITE + ", para 1.6, and do not present it as a threshold requirement: for that, use the "
                  "rung item " + near + ". Set it beside the honours descriptor " + fheq + " at spine:6, and note that 1.17 aligns these skills with the ESD guidance's competencies."),
             aad=("Use this when a student or programme team asks what makes the economist's way of working distinctive, here " + about + ". Put it plainly to a "
                  "student: " + plain + "; for staff, ask where the course builds it. Ask \"" + q + "\" Do not call it a pass requirement or read the whole list aloud."))
    if find:
        r['find'] = find
    s('1.6.b%d' % n, **r)

k16(1, ['gather', 'assimilate', 'structure', 'analyse', 'evaluate'], 'gathering evidence and handling data', 'subject-skill',
    "Economists need to gather evidence and to take in, organise, analyse and judge data of both kinds, qualitative and quantitative.",
    "Develop students' ability to collect evidence and then absorb, organise, analyse and weigh both numerical and non-numerical data.",
    "As an economist in training, you need to gather evidence and then organise, analyse and judge both numerical and non-numerical data.",
    'qaa/economics-2023/4.3.b4', 'qaa/fheq-2024/4.15.b7',
    'economists collect evidence and make sense of numbers and words alike', 'What evidence did you gather for your last piece of work, and how did you judge its quality?')
k16(2, ['abstract', 'simplify', 'identify', 'model'], 'abstraction and modelling', 'subject-skill',
    "Economists need to abstract and simplify so as to find and model what lies at the heart of a problem.",
    "Teach students to strip a problem to its essentials through abstraction and simplification, and to model that core.",
    "You need to be able to simplify a messy problem, find what really matters in it and build a model of that.",
    'qaa/economics-2023/4.3.b2', 'qaa/fheq-2024/4.15.b3.1',
    'economists simplify a problem to its core and build a model of it', 'What did you leave out of your model, and why was that safe?')
k16(3, ['analyse', 'reason', 'using'], 'deductive, abductive and inductive reasoning', 'subject-skill',
    "Economists need to analyse and reason in deductive, abductive and inductive ways, drawing on economic tools and on earlier research inside and outside the subject.",
    "Give students practice in deductive, abductive and inductive reasoning with economic tools and with prior research from economics and other fields.",
    "You need to be able to reason in several ways, from theory to case, from cases to general patterns and to the best explanation, using economic tools and existing research.",
    'qaa/economics-2023/4.3.b2', 'qaa/fheq-2024/4.15.b3.1',
    'economists reason from theory, from evidence and towards the best explanation', 'Was your argument built from a theory, from the data or from the most likely explanation?')
k16(4, ['communicate'], 'communicating results to varied audiences', 'generic-skill',
    "Economists need to report their results briefly to many kinds of audience, among them people with no economics background.",
    "Build students' ability to present findings concisely to varied audiences, including people untrained in economics.",
    "You need to be able to explain your results briefly to different audiences, including people who have never studied economics.",
    'qaa/economics-2023/2.2.b8', 'qaa/fheq-2024/4.15.b8',
    'economists explain results briefly to experts and non-experts alike', 'How would you explain your main finding to someone with no economics in one minute?')
k16(5, ['think'], 'the limits of analysis in its wider context', 'understanding',
    "Economists need to think critically about where their analysis stops working within its broader social and economic setting.",
    "Teach students to question the limits of their own analysis within its wider socioeconomic setting.",
    "You need to think critically about what your analysis cannot tell you once it is placed in its wider social and economic setting.",
    'qaa/economics-2023/4.3.b8', 'qaa/fheq-2024/4.15.b4',
    'economists question what their own analysis leaves out', 'What can your analysis not tell us, and why?')
k16(6, ['draw', 'recognise', 'evaluate'], 'policy inference, constraints and evaluation', 'subject-skill',
    "Economists need to draw conclusions for policy, see what may limit putting them into practice and judge policy results against the aims set for them.",
    "Develop students' ability to infer policy implications, identify constraints on implementation and evaluate outcomes against stated objectives.",
    "You need to be able to work out what your analysis means for policy, see what might get in the way of a policy and judge whether it met its aims.",
    'qaa/economics-2023/4.3.b5', 'qaa/fheq-2024/4.15.b7',
    'economists turn analysis into policy advice and judge policies against their aims', 'What would stop this policy working as planned, and how would you know whether it succeeded?',
    find=("draw economic policy inferences, to recognise the potential constraints in their implementation and to evaluate policy outcomes in the "
          "light of stated policy objectives."))

# ------------------------------------------------------------------ 2.2: learning outcomes the typical course is designed to achieve
def k22(n, verbs, about, domain, para, prac, ben, near, fheq, plain, q, find=None):
    r = dict(type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='students on a typical Economics course', addressee='learner',
             verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
             aaw=("Describe this as a learning outcome that the usual Economics course is built to reach (" + about + "); the issuer states no modal, so "
                  "record it as describing usual course design, not a requirement. Cite " + CITE + ", para 2.2, and do not claim every course must adopt it or "
                  "that it is a rung item. Set it beside " + near + " and the honours descriptor " + fheq + "."),
             aad=("Raise this when a student asks what the course is meant to give them, or when a team writes programme outcomes, here " + about + ". Tell a "
                  "student plainly: " + plain + "; for staff, compare it with your own programme outcomes. Ask \"" + q + "\" Avoid presenting it as a minimum "
                  "standard or quoting the list at length."))
    if find:
        r['find'] = find
    s('2.2.b%d' % n, **r)

k22(1, [], 'causality and analytical methods', 'understanding',
    "A course is usually designed so that students critically understand causality and analytical methods, in theory and in empirical work.",
    "Typical course outcome: students critically understand causality and the analytical methods of the subject, both theoretical and empirical.",
    "Your course is usually designed to help you understand, critically, how to establish cause and effect and how economic methods work in theory and with data.",
    'qaa/economics-2023/4.3.b3', 'qaa/fheq-2024/4.15.b2',
    'the course aims to help you see how economists establish cause and effect', 'How would you show that one thing caused another, rather than just moving with it?')
k22(2, ['used'], 'the history of economic ideas and methods', 'knowledge',
    "A course is usually designed so that students appreciate and understand how economic ideas have developed and the different methods economists have used and use now.",
    "Typical course outcome: students understand the history and development of economic thought and the varied methods economists have used and still use.",
    "Your course is usually designed to help you understand how economic ideas grew over time and the different methods economists have used.",
    'qaa/economics-2023/4.3.b6', 'qaa/fheq-2024/4.15.b1',
    'the course aims to show you where economic ideas came from and how methods changed', 'Which earlier idea still shapes the theory you are using now?')
k22(3, ['addressed'], 'historical context and economic history', 'knowledge',
    "A course is usually designed so that students understand the history behind present-day problems that economists tackle, and know economic history as fits the course.",
    "Typical course outcome: students understand the historical background of current economic problems and know economic history as relevant to the course.",
    "Your course is usually designed to help you understand the history behind today's economic problems and to know the economic history that matters for them.",
    'qaa/economics-2023/4.3.b6', 'qaa/fheq-2024/4.15.b1',
    'the course aims to give you the history behind current economic problems', 'What earlier episode helps explain the problem you are studying?')
k22(4, ['apply'], 'applying economic reasoning and tools', 'subject-skill',
    "A course is usually designed so that students can use economic reasoning and tools on applied topics.",
    "Typical course outcome: students apply economic reasoning and tools to applied topics.",
    "Your course is usually designed to help you use economic reasoning and tools on real, applied topics.",
    'qaa/economics-2023/4.3.b5 and qaa/economics-2023/3.4', 'qaa/fheq-2024/4.15.b6',
    'the course aims to have you use economics on real topics', 'Which applied topic have you tackled with an economic tool, and what did it show?')
k22(5, ['evaluate'], 'evaluating policy advice against its methods', 'subject-skill',
    "A course is usually designed so that students can judge critically why policy recommendations differ, in the light of the methods behind them.",
    "Typical course outcome: students critically evaluate differing policy recommendations against their underlying methodologies.",
    "Your course is usually designed to help you judge why experts recommend different policies, by looking at the methods behind each view.",
    'qaa/economics-2023/4.4.b5', 'qaa/fheq-2024/4.15.b7',
    'the course aims to help you see why economists disagree about policy', 'Why do two economists reach different advice on this policy, and whose method do you trust more?')
k22(6, ['discuss', 'analyse', 'evaluate', 'assess'], 'government policy and economic performance', 'subject-skill',
    "A course is usually designed so that students can debate, analyse and judge government policy and assess how the UK, other economies and the world economy perform.",
    "Typical course outcome: students discuss, analyse and evaluate government policy and assess the performance of the UK, other national economies and the global economy.",
    "Your course is usually designed to help you debate and judge government policy and assess how the UK and other economies, and the world economy, are doing.",
    'qaa/economics-2023/3.4 and qaa/economics-2023/4.3.b5', 'qaa/fheq-2024/4.15.b7',
    'the course aims to have you judge policy and how economies perform', 'How would you judge whether the economy is doing well, and by which measures?')
k22(7, ['enable'], 'representing economic ideas and handling data', 'understanding',
    "A course is usually designed so that students understand how economic ideas are expressed in words, graphs, mathematics and econometrics and how these relate, together with suitable techniques for working with and interpreting data.",
    "Typical course outcome: students understand verbal, graphical, mathematical and econometric forms of economic ideas and how they link, and can use suitable techniques to handle and interpret quantitative and qualitative data.",
    "Your course is usually designed to help you express economic ideas in words, graphs, maths and statistics, see how these connect and work with data.",
    'qaa/economics-2023/4.3.b3', 'qaa/fheq-2024/4.15.b2',
    'the course aims to help you move between words, graphs, maths and data', 'Can you state the same idea in a sentence, a graph and an equation?')
k22(8, ['articulate', 'communicate', 'present'], 'presenting arguments to specialist and general audiences', 'generic-skill',
    "A course is usually designed so that students can put their arguments clearly, in speech or other forms, to specialists and non-specialists, including people with other expertise on the question.",
    "Typical course outcome: students articulate, communicate and present arguments verbally or non-verbally to specialist and non-specialist audiences, including experts from other fields.",
    "Your course is usually designed to help you make and present your arguments, spoken or otherwise, to experts and non-experts, including people with other kinds of expertise.",
    'qaa/economics-2023/1.6.b4', 'qaa/fheq-2024/4.15.b8',
    'the course aims to help you argue clearly to any audience', 'Who outside economics would need to hear your argument, and how would you adapt it?',
    find=("An ability to articulate, communicate and present their arguments verbally and/or non-verbally and to both specialist and non-specialist "
          "audiences, who may have other kinds of expertise in relation to the issue at hand."))

# ------------------------------------------------------------------ rungs 4.3 threshold, 4.4 typical, 4.5 excellent
RUNG = {'threshold': '4.3', 'typical': '4.4', 'excellent': '4.5'}
FIND8 = {'threshold': "awareness of the possibility that many economic problems may admit of more than one approach.",
         'typical': ("familiarity with some of the different approaches to addressing economic problems and evidence of a critical awareness of the "
                     "applicability and limits of these approaches in particular contexts.")}
OUT = [  # outcome name, domain, FHEQ descriptor, Annex D row
    ('concepts, principles and tools', 'understanding', 'qaa/fheq-2024/4.15.b1', 'knowledge/r2'),
    ('theories, interpretations and modelling', 'understanding', 'qaa/fheq-2024/4.15.b3.1', 'knowledge/r2'),
    ('quantitative and qualitative methods and computing', 'subject-skill', 'qaa/fheq-2024/4.15.b2', 'practical/r1'),
    ('data and evidence', 'knowledge', 'qaa/fheq-2024/4.15.b7', 'practical/r4'),
    ('economic reasoning applied to policy', 'subject-skill', 'qaa/fheq-2024/4.15.b6', 'cognitive/r2'),
    ('the contexts of economic analysis', 'knowledge', 'qaa/fheq-2024/4.15.b1', 'knowledge/r1'),
    ('specialised areas and research', 'knowledge', 'qaa/fheq-2024/4.15.b3.2', 'cognitive/r1'),
    ('alternative approaches and their limits', 'understanding', 'qaa/fheq-2024/4.15.b4', 'cognitive/r2'),
]

def rid(rung, n):
    return '%s.b%d' % (RUNG[rung], n)

def kr(rung, n, verbs, about, para, prac, ben, plain, q):
    name, domain, fheq, ad = OUT[n - 1]
    th, ty, ex = SID + rid('threshold', n), SID + rid('typical', n), SID + rid('excellent', n)
    if rung == 'threshold':
        force = 'threshold'
        aaw = ("Describe this as a threshold standard on " + about + ": the least an Economics honours graduate at FHEQ level 6 (FQHEIS level 10) should "
               "have shown, not the level most reach. Cite " + CITE + ", para 4.3, and do not present it as a regulatory requirement or as binding where "
               "economics is a minor subject (para 4.1). Set it beside the same outcome higher up, " + ty + " and " + ex + ", the honours descriptor " + fheq +
               ", the Annex D threshold cell qaa/fheq-2024/annex-d/" + ad + "/3rd and spine:6.")
        aad = ("Bring this up when a student or programme team asks what must be shown by graduation on " + about + ". Tell a student in plain words that by "
               "the end " + plain + "; for staff, frame it as the floor that every graduate's assessed work has to evidence. Ask \"" + q + "\" and \"Which piece "
               "of assessed work shows it?\" Avoid reading the list aloud and avoid treating the typical or excellent rung as the minimum.")
    elif rung == 'typical':
        force = 'should'
        aaw = ("Describe this as the typical rung on " + about + ": what most Economics honours graduates at FHEQ level 6 should have shown, above the minimum in "
               + th + ". Cite " + CITE + ", para 4.4, and do not call it a pass requirement or tie it to a degree class, since the statement leaves classes to "
               "Annex D (para 4.2). Set it beside " + th + ", " + ex + " and the honours descriptor " + fheq + " at spine:6.")
        aad = ("Raise this when a student wants to know what a good, ordinary result looks like on " + about + ", or when staff calibrate marking above the "
               "minimum. Tell a student that most people at the end " + plain + ", and make clear that falling short of it is not failing; with staff, use it to "
               "describe the usual graduate. Ask \"" + q + "\" Do not present this rung as the pass standard or quote the issuer's list at length.")
    else:
        force = 'should'
        aaw = ("Describe this as the excellent rung on " + about + ": an aspiration for the strongest Economics honours graduates at FHEQ level 6, shown "
               "consistently. Cite " + CITE + ", para 4.5, and do not present it as required or as the same thing as a first; compare it only loosely with "
               "qaa/fheq-2024/annex-d/" + ad + "/1st. Set it beside " + ty + ", " + th + " and the honours descriptor " + fheq + ".")
        aad = ("Raise this when a strong student asks how to stand out on " + about + ", or when staff describe their best work. Say in plain words that the "
               "very best " + plain + ", and do so consistently; with staff, frame it as an aspiration, not a requirement. Ask \"" + q + "\" Do not treat it as "
               "expected of everyone or read the issuer's wording aloud at length.")
    r = dict(type=rung, rung=rung, force=force, level='fheq:6', appliesTo='graduates at the %s level' % rung, addressee='learner',
             verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben, aaw=aaw, aad=aad, forceFrom=RUNG[rung])
    if n == 8 and rung in FIND8:
        r['find'] = FIND8[rung]
    s(rid(rung, n), **r)

T, Y, X = 'To reach the threshold standard, ', 'At the typical level, ', 'At the excellent level, '

# threshold (4.3): "should have demonstrated"; force threshold (4.2 calls it the minimum)
kr('threshold', 1, [], 'key concepts, principles and tools',
   "At threshold, a graduate should have shown that they understand the main ideas, principles and tools that economists work with.",
   "At threshold, check that every graduate has shown a working grasp of the discipline's main concepts, principles and analytical tools.",
   T + "you should have shown that you understand the main ideas, principles and tools of economics.",
   'you should be able to show you understand the main ideas, principles and tools of economics',
   'Which core idea or tool could you explain and use without notes?')
kr('threshold', 2, [], 'key theories, interpretations and models',
   "At threshold, a graduate should have shown that they understand the main economic theories, the ways they are read and the approaches used to model them.",
   "At threshold, graduates should have shown they understand the principal theories of the subject, how they are interpreted and how economists model them.",
   T + "you should have shown that you understand the main theories in economics, how they are interpreted and how economists build models.",
   'you should understand the main theories, how they are read and how economists build models',
   'Which theory could you explain, and which model goes with it?')
kr('threshold', 3, [], 'quantitative and qualitative methods and computing',
   "At threshold, a graduate should have shown that they understand the numerical and non-numerical methods and computing techniques suited to their course, and see where these apply.",
   "At threshold, graduates should have shown they understand the quantitative, qualitative and computing techniques their course uses and the settings where each fits.",
   T + "you should have shown that you understand the numerical, non-numerical and computing methods your course uses, and when each is the right one.",
   'you should understand the methods and computing techniques your course uses and when each fits',
   'Which method would you choose for this question, and why that one?')
kr('threshold', 4, ['applied'], 'sources and content of economic data and evidence',
   "At threshold, a graduate should have shown that they know where economic data and evidence come from and what they contain, and see which methods could suit analysing them.",
   "At threshold, graduates should have shown they know where economic data and evidence originate and what they hold, and which analytical methods fit them.",
   T + "you should have shown that you know where economic data and evidence come from, what they hold and which methods could be used to analyse them.",
   'you should know where economic data come from and which methods suit them',
   'Where would you find data on this question, and what would you do with it?')
kr('threshold', 5, ['apply'], 'economic reasoning applied to policy',
   "At threshold, a graduate should have shown that they can bring economic reasoning to bear on questions of policy.",
   "At threshold, graduates should have shown they can use economic reasoning on policy questions.",
   T + "you should have shown that you can use economic reasoning on policy questions.",
   'you should be able to use economic reasoning on a policy question',
   'What does economic reasoning say about this policy?')
kr('threshold', 6, ['applied'], 'the contexts in which economic analysis is used',
   "At threshold, a graduate should have shown that they know and are aware of the wider settings (historical, political, institutional, international, social, cultural, environmental) in which particular economic analyses are used.",
   "At threshold, graduates should have shown they know the wider settings, from history and politics to institutions, culture and the environment, in which economic analysis is used.",
   T + "you should have shown that you know the wider settings, such as history, politics, institutions, society, culture and the environment, in which economic analysis is used.",
   'you should know the wider settings in which an economic analysis is used',
   'What in the history, politics or environment around this problem changes your analysis?')
kr('threshold', 7, ['informed'], 'knowledge of specialised areas, partly drawn from research',
   "At threshold, a graduate should have shown knowledge of a suitable number of specialist areas of economics, partly grounded in research.",
   "At threshold, graduates should have shown knowledge of an appropriate range of specialist fields, some of it drawn from research in the subject.",
   T + "you should have shown that you know several specialist areas of economics, partly through research in those areas.",
   'you should know a few specialist areas of economics, some of it through research',
   'Which specialist area do you know best, and which research shaped what you know?')
kr('threshold', 8, ['admit'], 'awareness that problems allow more than one approach',
   "At threshold, a graduate should have shown awareness that many economic problems can be tackled in more than one way.",
   "At threshold, graduates should have shown they recognise that many economic problems can be approached in more than one way.",
   T + "you should have shown that you know many economic problems can be tackled in more than one way.",
   'you should know that many problems can be tackled in more than one way',
   'What other approach could someone take to this problem?')

# typical (4.4): "should have demonstrated"
kr('typical', 1, [], 'systematic grasp of concepts, principles and tools',
   "At the typical level, a graduate should have shown a systematic, well-organised understanding of economic concepts, principles and tools.",
   "At the typical level, graduates should have shown they understand economic concepts, principles and tools as a connected system, not as separate items.",
   Y + "you should have shown that you understand economic ideas, principles and tools as a connected whole.",
   'understand economic ideas, principles and tools as a connected whole',
   'How do the core ideas you have learned fit together?')
kr('typical', 2, [], 'systematic grasp of distinctive theories and models, used competently',
   "At the typical level, a graduate should have shown a systematic understanding of distinctive economic theories, their readings and modelling approaches, and use them competently.",
   "At the typical level, graduates should have shown a systematic grasp of the subject's distinctive theories, interpretations and models and be able to use them competently.",
   Y + "you should have shown a systematic understanding of the distinctive theories and models of economics and that you can use them competently.",
   'understand the distinctive theories and models systematically and use them well',
   'Which model would you choose for this question, and how confident are you using it?')
kr('typical', 3, ['use'], 'proficiency in methods and computing across problems',
   "At the typical level, a graduate should have shown proficiency in quantitative methods and computing and know how to use them well across a range of problems.",
   "At the typical level, graduates should have shown proficiency in quantitative and computing techniques and know how to apply them effectively to varied problems.",
   Y + "you should have shown that you are proficient in quantitative and computing methods and can use them well on different kinds of problem.",
   'are proficient in quantitative and computing methods across different problems',
   'Which technique have you used on more than one kind of problem?')
kr('typical', 4, ['applied'], 'systematic grasp of data, evidence and methods for them',
   "At the typical level, a graduate should have shown a systematic grasp of where economic data and evidence come from, what they contain and which methods suit their analysis.",
   "At the typical level, graduates should have shown a systematic grasp of where economic data and evidence come from, what they contain and which methods suit their analysis.",
   Y + "you should have shown a systematic understanding of economic data and evidence, where they come from and which methods suit them.",
   'understand economic data and evidence systematically, with the methods that suit them',
   'How did you decide which data and which method fitted your question?')
kr('typical', 5, ['apply'], 'applying economic reasoning to policy critically',
   "At the typical level, a graduate should have shown that they know how to bring economic reasoning to policy questions critically.",
   "At the typical level, graduates should have shown they can bring economic reasoning to bear on policy questions critically.",
   Y + "you should have shown that you can use economic reasoning on policy questions critically, not only apply it.",
   'use economic reasoning on policy critically',
   'What are the weaknesses of the economic case for this policy?')
kr('typical', 6, ['applied'], 'systematic grasp of the contexts of economic analysis',
   "At the typical level, a graduate should have shown a systematic grasp of the wider settings (historical, political, institutional, international, social, cultural, environmental) in which particular economic analyses are used.",
   "At the typical level, graduates should have shown a systematic grasp of the wider settings, historical to environmental, in which economic analysis is used.",
   Y + "you should have shown a systematic understanding of the wider settings, such as history, politics, institutions, culture and the environment, in which economic analysis is used.",
   'understand systematically the wider settings in which economic analysis is used',
   'How does the setting of this problem shape what the analysis can say?')
kr('typical', 7, [], 'specialised areas and their research literature',
   "At the typical level, a graduate should have shown knowledge of a suitable number of specialist areas of economics and an appreciation of their research literature.",
   "At the typical level, graduates should have shown knowledge of an appropriate range of specialist fields and an appreciation of the research written in them.",
   Y + "you should have shown that you know several specialist areas of economics and appreciate the research written in them.",
   'know several specialist areas and appreciate their research literature',
   'Which recent study in your specialist area would you recommend, and why?')
kr('typical', 8, ['addressing'], 'different approaches and a critical sense of their limits',
   "At the typical level, a graduate should have shown familiarity with some of the different ways of tackling economic problems and a critical awareness of where each works and where it falls short.",
   "At the typical level, graduates should have shown familiarity with several approaches to economic problems and critical awareness of their applicability and limits in particular settings.",
   Y + "you should have shown that you know several ways to tackle economic problems and can judge critically where each works and where it falls short.",
   'know several approaches and judge critically where each works',
   'Where would this approach stop working, and what would you use instead?')

# excellent (4.5): "should have consistently demonstrated"
kr('excellent', 1, [], 'excellent understanding of concepts, principles and tools',
   "At the excellent level, a graduate should consistently have shown an outstanding understanding of economic concepts, principles and tools.",
   "At the excellent level, graduates should consistently have shown an outstanding grasp of the subject's concepts, principles and tools.",
   X + "you should consistently have shown an outstanding grasp of economic ideas, principles and tools.",
   'show an outstanding grasp of economic ideas, principles and tools',
   'Where could you explain a core idea in a way that goes past the textbook?')
kr('excellent', 2, [], 'excellent grasp of theories and models, used competently in research',
   "At the excellent level, a graduate should consistently have shown an outstanding understanding of distinctive economic theories, their readings and models, used competently in a research setting.",
   "At the excellent level, graduates should consistently have shown an outstanding grasp of distinctive theories, interpretations and models and use them competently in research.",
   X + "you should consistently have shown an outstanding understanding of distinctive theories and models in economics and used them well in your own research.",
   'understand distinctive theories and models outstandingly and use them well in research',
   'How did you use a theory or model in your own research, and what did it let you see?')
kr('excellent', 3, ['use'], 'excellence in methods and computing across problems',
   "At the excellent level, a graduate should consistently have shown excellence in quantitative methods and computing and know how to use them well across a range of problems.",
   "At the excellent level, graduates should consistently have shown excellence in quantitative and computing techniques and know how to apply them effectively to varied problems.",
   X + "you should consistently have shown excellent quantitative and computing skills and used them well on many kinds of problem.",
   'show excellent quantitative and computing skills across many problems',
   'Which hard problem did your methods let you crack?')
kr('excellent', 4, ['applied'], 'excellent grasp of data, evidence and methods for them',
   "At the excellent level, a graduate should consistently have shown an excellent command of where economic data and evidence come from, what they contain and which methods suit their analysis.",
   "At the excellent level, graduates should consistently have shown an excellent command of economic data and evidence and of the methods that suit their analysis.",
   X + "you should consistently have shown an excellent command of economic data and evidence and of the methods that suit them.",
   'command economic data, evidence and their methods excellently',
   'What makes your choice of data and method the strongest one available?')
kr('excellent', 5, ['apply'], 'advanced, critical application of economic reasoning to policy',
   "At the excellent level, a graduate should consistently have shown advanced knowledge of how to bring economic reasoning to policy questions critically.",
   "At the excellent level, graduates should consistently have shown advanced, critical use of economic reasoning on policy issues.",
   X + "you should consistently have shown advanced, critical use of economic reasoning on policy questions.",
   'use economic reasoning on policy with advanced, critical judgement',
   'What would you advise a minister, and what is the strongest objection to your advice?')
kr('excellent', 6, ['applied'], 'excellent grasp of the contexts of economic analysis',
   "At the excellent level, a graduate should consistently have shown an excellent grasp of the wider settings (historical, political, institutional, international, social, cultural, environmental) in which particular economic analyses are used.",
   "At the excellent level, graduates should consistently have shown an excellent grasp of the wider settings, historical to environmental, in which economic analysis is used.",
   X + "you should consistently have shown an excellent understanding of the wider settings in which economic analysis is used, from history and politics to culture and the environment.",
   'understand outstandingly the wider settings in which economic analysis is used',
   'Which part of the wider setting would most change your conclusion?')
kr('excellent', 7, ['embedded'], 'advanced knowledge of specialised areas, set in current research',
   "At the excellent level, a graduate should consistently have shown advanced knowledge of a suitable number of specialist areas, grounded in current research literature.",
   "At the excellent level, graduates should consistently have shown advanced knowledge of an appropriate range of specialist fields, rooted in current research.",
   X + "you should consistently have shown advanced knowledge of several specialist areas of economics, built on current research.",
   'know specialist areas in advanced depth, built on current research',
   'Which current debate in your specialist area could you take a side in, and why?')
kr('excellent', 8, ['addressing', 'demonstrating'], 'excellent judgement across approaches, showing creativity',
   "At the excellent level, a graduate should consistently have shown excellent knowledge of different ways of tackling economic problems and an excellent sense of where each works and where it falls short, using them with creativity and sound judgement in varied settings.",
   "At the excellent level, graduates should consistently have shown excellent knowledge of alternative approaches and their applicability and limits, and creative, well-judged use of them across diverse settings.",
   X + "you should consistently have shown excellent knowledge of different ways to tackle economic problems, where each works and where it fails, and used them creatively and with sound judgement.",
   'choose among approaches creatively and with sound judgement',
   'When did you combine or swap approaches creatively, and what made that the right call?')

# gradeOf: the three rung lists run outcome by outcome in parallel (eight each); inferred, the issuer does not pair them
GRADE = {}
for _n in range(1, 9):
    GRADE['4.4.b%d' % _n] = '4.3.b%d' % _n
    GRADE['4.5.b%d' % _n] = '4.4.b%d' % _n

TH = {'1.7': 'theme:edi', '1.10': 'theme:accessibility', '1.13': 'theme:accessibility', '1.16': 'theme:esd'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.3; 4.2'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.3; 4.2')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent',
                           basis='stated (D1, 2.3: "a degree with honours (FHEQ Level 6; FQHEIS Level 10)"; 4.2)')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.7', '1.8', '1.9', '1.11', '1.12', '2.7', '2.8', '3.10', '3.11']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.7', '1.10', '1.11', '1.12', '1.13', '1.14', '3.11']),
      dict(id='theme:esd', role='carries', carriedIn=['1.2', '1.3', '1.5', '1.15', '1.16', '1.17', '1.18', '1.19', '3.2']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '2.7', '3.7'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-economics-2019-benchmarks (fourth edition, 2019; not yet ingested)',
           note='the back matter names the 2019 fourth edition and the front matter lists key changes from the previous statement'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D',
           note='the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees (4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ level 6 (2.3; 4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS level 10 (2.3; 4.2)'),
      dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note='the Education for Sustainable Development Guidance (Advance HE and QAA, March 2021), with whose learning outcomes the core skills of 1.6 align (1.17)'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance (not yet ingested)', note='front matter'),
      dict(rel='refersTo', target='QAA Glossary (not ingested)', note='front matter')]

SB1 = [
    "A social science of how individuals and groups decide and interact within institutions, power structures and their wider setting, aiming to inform policy through theory and evidence (D1, 1.2, 1.4).",
    "Its central question is how resources are allocated, distributed and used, and what follows for well-being and sustainability, past, present and future (D1, 1.2).",
    "It works at micro and macro levels and in static and dynamic terms; because interpretations are contested, it studies phenomena through several theoretical lenses and in their historical, political, social and environmental settings (D1, 1.3).",
    "Its characteristic method is abstraction and modelling tested against quantitative and qualitative evidence, with causality to the fore and attention to the limits of its own tools (D1, 1.5, 1.6, 3.3).",
    "It links to politics, geography, history, philosophy, law, data science, psychology and the sciences, and underpins finance, business and accounting (D1, 1.4).",
    "It names its own narrow make-up (a field that remains predominantly white, male and Western) as an EDI challenge (D1, 1.9).",
    "Its graduates enter a wide range of sectors, as professional economists and in other careers (D1, 1.5, 2.1).",
]

SB2 = [dict(theme='theme:edi', inThisSubject="the subject itself studies discrimination and inequality and debates sensitive questions from evidence; it names its narrow make-up and its concentration in selective universities, and asks for inclusive materials, widening participation, zero tolerance of harassment and closing awarding gaps (D1, 1.7 to 1.9; 2.7; 2.8; 3.11)", statements=['1.7']),
       dict(theme='theme:accessibility', inThisSubject="inclusive pedagogy and resources; blended delivery since 2020 and its risks for equal access; digital accessibility of graphs, video, data and specialist software, with sector examples (D1, 1.10 to 1.14; 3.11)", statements=['1.10', '1.13']),
       dict(theme='theme:esd', inThisSubject="headed Sustainability: framed by the UN SDGs and Global Compact, defined in the text and built into concepts and models; graduates able to face the planetary crisis; core skills aligned with the ESD guidance's competencies and with SDGs 8, 9, 10 and 12 (D1, 1.15 to 1.19; 3.2)", statements=['1.16']),
       dict(theme='theme:enterprise', inThisSubject="headed Enterprise and entrepreneurship education: transferable skills for careers, data and software fluency, communicating to wide audiences, placements and degree apprenticeships, and civic as well as career value (D1, 1.20 to 1.26; 2.7)", statements=[])]

SB3 = dict(
    areas=[dict(component='3.2', gloss='eight key concepts: opportunity cost and scarcity; incentives and biases; strategic thinking; expectations and shocks; marginal considerations; equilibrium and dynamics; mutual gains, conflict and power; markets and market failure'),
           dict(component='3.5', gloss='fourteen common applied fields beside the core micro, macro and econometrics, from behavioural to public economics'),
           dict(component='3.6', gloss='economic history and the history of economic thought, embedded or taught separately')],
    practices=[dict(component='2.6', kind='learning', gloss='mixed distance, online and in-person delivery; independent and peer learning; varied materials including code and policy briefs'),
               dict(component='3.7', kind='teaching', gloss='lectures, seminars, tutorials, workshops, peer and project-based learning, experiments, games, technology-enabled and experiential learning, practitioners'),
               dict(component='3.8', kind='learning', gloss='interactive, student-centred and blended learning since the pandemic'),
               dict(component='3.9', kind='teaching', gloss='subject teaching networks and general teaching centres as resources'),
               dict(component='3.11', kind='teaching', gloss='pluralist and decolonial approaches'),
               dict(component='3.12', kind='assessment', gloss='course-level analysis of assessment design'),
               dict(component='3.13', kind='assessment', gloss='assessment that builds problem-solving and higher-order reasoning'),
               dict(component='3.14', kind='assessment', gloss='closed and open-book exams, projects, essays, multimedia, group and policy-brief tasks; authentic, data-based assessment'),
               dict(component='3.15', kind='assessment', gloss='formative assessment, feedback and scaffolded skills development')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.3', award=HON, items=8),
           dict(rung='typical', leadIn='4.4', award=HON, items=8),
           dict(rung='excellent', leadIn='4.5', award=HON, items=8)],
    rungBases="4.1: the rungs apply to single honours and to joint degrees where economics is a major part, not in full where it is a minor part; reaching typical implies threshold. 4.2: most students exceed the threshold; achievement above it is judged by each provider with Annex D. 4.5 adds 'consistently'.",
    outcomeLists=[dict(leadIn='1.6', gloss='core intellectual abilities economists need (lead-in uses need, recorded as describes)', items=6, award=['honours']),
                  dict(leadIn='2.2', gloss='learning outcomes the typical course is designed to achieve (no modal)', items=8, award=['honours'])],
    outcomes=[dict(outcome=o[0], threshold='4.3.b%d' % n, typical='4.4.b%d' % n, excellent='4.5.b%d' % n, basis='inferred', domain=o[1], award=HON)
              for n, o in enumerate(OUT, 1)])

SB4A_FULL = []

SB5 = [dict(body='professional, statutory and regulatory bodies (PSRBs), none named',
            says='the statement supports PSRBs with the academic standards expected (front matter); courses with professional or vocational outcomes may need their evaluation and accreditation, by site visit and desk review (D1, 2.12)',
            requirements='not-applicable-by-design: no body is named (Part E)'),
       dict(body='Royal Economic Society',
            says='a partner with providers in widening-participation work, which also lets current students work with it (D1, 2.8)',
            requirements='not-applicable-by-design: named as a partner, not as an accrediting body (Part E)')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion (EDI)', carriedIn=['1.7', '1.8', '1.9', '1.11', '1.12', '2.7', '2.8', '3.10', '3.11'], statements=[SID + '1.7']),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['1.7', '1.10', '1.11', '1.12', '1.13', '1.14', '3.11'], statements=[SID + '1.10', SID + '1.13']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.2', '1.3', '1.5', '1.15', '1.16', '1.17', '1.18', '1.19', '3.2'], statements=[SID + '1.16']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (EED) (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '2.7', '3.7'], statements=[])],
    frameworks=[dict(framework='fheq', levels=['fheq:6'], citedIn=['2.3', '4.2']),
                dict(framework='scqf', levels=['fqheis:10'], citedIn=['2.3', '4.2'])],
    bodies=[dict(body='professional, statutory and regulatory bodies (unnamed)', citedIn=['front matter', '2.12']),
            dict(body='Royal Economic Society', citedIn=['2.8'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='descriptions of the four honours classes (1st, 2.1, 2.2, 3rd), to which providers should refer when evidencing achievement above threshold'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development Guidance produced by Advance HE and QAA (March 2021)', citedIn=['1.17'], role='its learning outcomes and competencies align with the core skills of 1.6'),
        dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='UN Sustainable Development Goals (external)', named='UN Sustainable Development Goals (SDGs)', citedIn=['1.15', '1.16', '1.17'], role='frame of the sustainability theme; SDGs 8, 9, 10 and 12 named'),
        dict(document='UN Global Compact (external)', named='UN Global Compact', citedIn=['1.15'], role='standard-setting in human rights, labour, environment and anti-corruption, reflected in the discipline'),
        dict(document='Equality Act 2010 (law)', named='the Equality Act 2010', citedIn=['1.7'], role='protected characteristics, as a floor that inclusion goes beyond'),
        dict(document='Jisc (2020) Steps to improve your institution\'s digital accessibility (external)', named='Steps to improve your institution’s digital accessibility', citedIn=['1.14'], role='example of digital accessibility guidance'),
        dict(document='The Open University (2022) Accessibility Statement (external)', named='accessibility statements such as that produced by The Open University', citedIn=['1.14'], role='example of a provider accessibility statement'),
    ])

B1 = [dict(slug='sustainability', definition='present and future states, backed by strategies and operations aimed at social goals, centred on preserving resources, upholding human rights and fair labour relations, and reaching equitable welfare (D1, 1.15)', beneficiaryDefinition='meeting needs now and later while protecting resources, rights and fairness', scopeNote='the statement says it goes beyond climate change', category='unknown', practices=['education']),
      dict(slug='enterprise-and-entrepreneurship-education', definition='education that builds behaviours, attributes and competencies likely to support successful careers and readiness for change, often through placements and external links (D1, 1.20)', beneficiaryDefinition='learning that prepares you to create opportunities and adapt at work', scopeNote='abbreviated EED; front matter groups it with employability', category='unknown', practices=['education']),
      dict(slug='authentic-assessment', definition='assessment whose tasks mirror activities in the wider world, workplaces included, used for applied skills (D1, 3.14)', beneficiaryDefinition='tasks like the ones economists do at work', scopeNote='research projects and data-based tasks are the examples', category='unknown', practices=['education']),
      dict(slug='monitoring-and-evaluation', definition='periodic assessment of a course, internal or external, drawing on current and past monitoring to understand achievement or plan the course (D1, 2.9)', scopeNote='students should take part (2.9)', category='unknown', practices=['education']),
      dict(slug='threshold-standard', definition='the minimum standard of achievement for the award, which most students exceed (D1, 4.2, 4.3)', scopeNote='with typical and excellent above it (4.4, 4.5)', category='unknown', practices=['education'])]
B2A = [dict(concept='sustainability', form='sustainability', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='enterprise-and-entrepreneurship-education', form='enterprise and entrepreneurship education', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='enterprise-and-entrepreneurship-education', form='EED', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
       dict(concept='authentic-assessment', form='authentic assessment', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='monitoring-and-evaluation', form='monitoring and evaluation', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='threshold level', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='minimum threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='admitted', register='formal')]
B4 = []; B5 = []
D3 = []

E = [
    "SB4, rungs: three rung lists of eight items each (4.3 threshold, 4.4 typical, 4.5 excellent) with lead-ins in 'should have demonstrated' (Psychology's are in 'will'); 4.5 adds 'consistently'. Threshold items take force `threshold` because 4.2 calls the threshold the minimum; typical and excellent items take the lead-in's `should` (forceFrom 4.4, 4.5).",
    "SB4, gradeOf: unlike Psychology, the three lists run plainly in parallel item by item (concepts; theories; methods; data; policy; contexts; specialised areas; approaches), differing in qualifiers (key, systematic, excellent, advanced). All 16 links (4.4.b1 to b8 to 4.3.b1 to b8; 4.5.b1 to b8 to 4.4.b1 to b8) are inferred: the issuer does not pair them. 4.1 says typical implies threshold. For Abbott at P3: whether the parallel wording makes them `stated`.",
    "SB4, domains: the rung items are noun phrases completing the lead-in's 'demonstrated', so many records carry no verb of their own (verbs: []); none of the 24 is a generic skill. The method items (b3) mix understanding (threshold) with proficiency (typical, excellent); kept as subject-skill across the rungs so the gradeOf links share a domain.",
    "S3, std-prep: the skeleton marked 2.2's eight items as the typical rung because the lead-in says 'The typical Economics course'; they are an outcome list of the usual course design, not a rung (SB4 outcomeLists). Lesson for the script: 'typical' qualifying a course is not a rung lead-in.",
    "S3, std-prep: five spans ran on into the next sub-heading (1.6.b6 'Equality, diversity and inclusion (EDI)', 2.2.b8 'Progression', 4.2 'Threshold level', 4.3.b8 'Typical level', 4.4.b8 'Excellent level'); each was cut back with `find`. The theme candidate hits 1.6 (edi), 1.9 (accessibility), 1.14 (esd) and 1.19 (enterprise) came from the same spill-over and were dropped from SB6 where the paragraph does not otherwise carry the theme.",
    "S4, outcome lists with no listed modal: 1.6 ('Economists need the ability to:'; 'need' outside the five, recorded as describes, forceFrom 1.6) and 2.2 ('The typical Economics course is designed to achieve the following learning outcomes'; plain present, recorded as describes). Taken as statements because they are outcome lists and 1.17 calls 1.6 'the core skills provided by all Economics courses'. For Abbott at P3: keep as statements, and with what force?",
    "S4, force outside the five, recorded as describes: 'the expectation is that' (2.2, provider support where maths is not required on entry); 'need to' (3.10, course leaders' support for language, mathematics and study skills). For Abbott: should these read as should?",
    "S4, 'requires' read as must (brief 0.2.2): 1.3 ('Studying economics requires an understanding ...'; 'required at both the individual (micro) and the aggregate (macro) level') and 1.16 ('they require students to foster critical and creative capacities'). Not taken as statements despite the word: 2.1 ('a core of required modules' describes most courses), 2.2 ('may or may not require a mathematics qualification for admission'), 2.3 (postgraduate entry 'may require specified levels'), 2.12 ('may also require evaluation and accreditation': conditional, about PSRBs) and the front matter's 'regulatory requirements'.",
    "S4, not taken (predictive or descriptive 'will', or plain present): 2.3 ('will typically progress'; 'it is expected that each level would see' attainment building to the threshold skills: 'expected' outside the five); 2.11 (external examiners 'will be asked'); 1.22 and 1.23 (graduates 'are familiar' with software, 'are trained' in communicating); 4.1 (minor-subject students 'are not expected to attain all of these benchmarks').",
    "S4, plain-present provider norms (template open point 5), not statements: 3.2's key concepts 'most Economics courses cover' (seven of eight items; only 3.2.b5, with 'should', is a statement), 3.5's applied fields (may cover), 3.6, 3.7 ('is designed to encourage'), 3.12 to 3.15 on assessment.",
    "S4, 1.7: the obliging sentence (educators 'should aim to foster an inclusive learning community') is the statement; its five bullets are examples ('such efforts might include') and are not statements. The paragraph says 'Economics educators': the provider-facing word, kept in our versions as teachers and staff.",
    "S4, 1.13: the issuer's text reads 'Economics pay attention' (a grammatical slip, kept in source); the statement is cut at the first sentence ('should include ... image descriptions'); the rest of the paragraph ('needs to be suitable', 'needs consideration') is summarised in the paraphrase, 'needs to' being outside the five.",
    "S4, 4.2 holds two forces: a prediction ('will perform significantly better than the minimum threshold standards') and the provider's 'should refer to Annex D'; recorded as should, addressee provider.",
    "S1, front matter: the issuer's template placeholder '[SUBJECT]' is left unfilled in 'About this Statement' ('a QAA Subject Benchmark Statement for [SUBJECT]'); kept in the held text.",
    "S2, awards: honours only (FHEQ 6, FQHEIS 10, stated in 2.3 and 4.2); exit awards (CertHE, DipHE, Pass degree) are mentioned in 2.5 but given no standards. No master's level.",
    "Front matter subjects, inferred: hecos 100452 international economics (from 3.5's international macroeconomics and finance, and international trade and migration) and hecos 100601 economic policy (from 3.5's political economy, a non-preferred term of 100601, and 1.2's policy aim). For P3. CAH15 social sciences is taken as stated from 1.4 ('Economics is a social science'). Specialisms with no HECoS term of their own (behavioural, development, environmental, experimental, health, labour, monetary, public economics; growth; industrial organisation) are listed without codes.",
    "SB5: no professional, statutory or regulatory body is named; PSRBs appear only in general (front matter, 2.12). The Royal Economic Society (2.8) is a widening-participation partner, not an accreditor. Other organisations named, not bodies in SB5's sense: the Bank of England and economic consultancies as degree-apprenticeship and placement partners (2.7); the Economics Network, the Centre for Teaching and Learning Economics and Advance HE as teaching resources (3.9; section 5); Jisc and The Open University as accessibility examples (1.14); the United Nations (1.15 to 1.17).",
    "SB6, frameworks: FHEQ level 6 and FQHEIS level 10 cited in 2.3 and 4.2; CQFW not cited. The front matter also names the OfS regulatory framework (England), the Quality Assessment Framework for Wales and the Quality Enhancement Framework (Scotland): regulatory arrangements, excluded front matter, not qualification frameworks.",
    "SB6, themes: EDI is also carried by 1.11 (curricula a diverse community can see itself in) and 1.12 (diverse and inclusive teaching), both under the Accessibility heading; accessibility by 1.7's bullet on neurodiverse access; esd by 1.5 (the climate crisis among contemporary problems) and 3.2 (planetary crises, environmental degradation, sustainability as an evaluative criterion); enterprise by 2.7 (an employability angle) and 3.7 (learning organised to support employability). Generative AI is not treated (1.4 names Data Science and Artificial Intelligence only as linked subjects).",
    "SB6, sharedDocuments: Annex D is cited by name without a year (4.2); resolved to the ingested FHEQ 2024 document, Annex D. The ESD guidance (1.17) resolves to std:doc:qaa-advancehe-esd-2021-guidance.",
    "Patterns that differ from Psychology: rung lead-ins in 'should have demonstrated' rather than 'will'; eight parallel items per rung; no master's or conversion award; no named PSRB; an outcome list in 'need' (1.6) and one with no modal (2.2); 'Economics educators' named in the text; sub-headings run on to the end of the preceding paragraph in the held text; section 4 has no separate list of subject-specific and generic skills, so generic skills appear only in 1.6.b4, 2.2.b8 and 1.16.",
    "Levels: all learner statements at fheq:6, honours, read from 2.3 (FHEQ Level 6; FQHEIS Level 10) and checked against std:doc:qaa-fheq-2024-framework S5 and SL1 (4.15) and std:doc:qaa-fqheis-2024-framework (4.16); spine:6 from std:ref:uk-framework R2 and R8. The FHEQ descriptor and Annex D cells each aaw names (4.15.b1 to b9.3; annex-d/<strand>/<row>/3rd and /1st) are our pointing, inferred.",
    "S7, supersedes: the text names the fourth edition (2019) and says the 2023 statement revises it; its id std:doc:qaa-economics-2019-benchmarks is ours and not yet ingested.",
    "S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are to check (template open point 3).",
    "S9: not researched in P1.",
]
