# bm_content.py: run 0106, QAA Subject Benchmark Statement Finance (April 2025). Judgement file for tools/bm_build.py (BM-BRIEF 0.2.3).
# Exact statement texts where the skeleton span carries a run-in heading, a page number or a page break cut (Part E).
FIND = {
  '1.6' : '1.6 The purpose of a Finance degree is to educate students to enable them to understand the role of finance in business and organisations, thereby providing a sound foundation for a range of careers. Finance as a degree requires students to study both the fundamentals and cutting-edge developments in finance theory and practice. While encompassing numerous significant areas as described in section 3, it typically focuses on two main subject domains.' ,
  '1.15.b1' : "Specialist master's degrees in Finance involve the in-depth and advanced theoretical and conceptual exploration of one or more core components typically covered in a bachelor's Finance degrees. These programmes may also incorporate supplementary specialised subjects within or related to the discipline, such as banking, fintech, data analytics, or specific research specialisms in the field. This type of master's degree in\n\n6\nFinance would be expected to be evaluated against the highest levels of achievement outlined in the Subject Benchmark Statement, alongside additional content criteria pertinent to the degree's specialised focus. Typically, applicants for these programmes are required to hold at least a second-class single or joint honours bachelor's degree in Finance, or higher." ,
  '1.27' : '1.27 There should be monitoring and review of EDI within Finance degree programmes to examine how effective the current EDI policies have been implemented and how they can be further enhanced.' ,
  '1.28' : '1.28 Accessibility is concerned with removing barriers so that learners can achieve learning outcomes equitably. Teaching methods in Finance degree programmes reflect the needs of the student body to ensure that each student can succeed and reach their full potential, regardless of their background, disability, health, or other protected characteristics. Accessibility should, as a minimum, meet regulatory requirements and will apply to all stages of the programme, from providing pre-application information through to graduation and beyond. Many providers have their own general accessibility guidance that provides advice and tools to enhance accessibility at the point of design. Some providers also publish accessibility policies which serve as a useful reference point. People with impairments may face barriers to education and employment in higher education institutions. Providing support and adjustments can remove these barriers and therefore support the development of an inclusive environment; please see examples from Advance HE.' ,
  '1.29.b10' : 'Proactive approaches should be taken in the design of learning and teaching, and assessment, in order to build in inclusivity and avoid creating barriers for students with specific learning difficulties or who are neurodivergent.' ,
  '2.4' : '2.4 Finance degree programmes should prepare students for lifelong and self-directed learning. They should be designed to enable students to thrive in a range of careers in finance, including public, private and the third sector, entrepreneurial and enterprise activities, or further academic pursuits.' ,
  '2.17' : "2.17 Students at master's level should be educated having in mind that the opportunity to conduct research is an important aspect, as some will explore further study opportunities." ,
  '2.21' : '2.21 When structuring flexibility into Finance degrees it is essential to ensure that programmes are coherent and meet the benchmarks in this Statement. Flexibility in Finance degrees may be required to meet EDI obligations and partnership relationships may also offer additional flexibility.' ,
  '3.8' : "3.8 Students on both bachelor's and master's taught programmes in Finance often have diverse backgrounds. Programme directors and course leaders should consider specific help for subject-specific language, mathematical (where appropriate) support, academic writing, as well as study and examination skills support." ,
  '3.14' : "3.14 Where appropriate, the design of teaching and learning activities, together with associated assessment activities, can usefully be informed by current pedagogical developments and research in these areas (including developments in technology). Also, regular reviews must be undertaken to ensure that such activities remain 'fit for purpose' and\n\n22\nup to date in achieving the programme's desired outcomes with respect to this Subject Benchmark Statement." ,
  '4.3' : '4.3 Please note that the minimum threshold, typical and excellent standards are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances, providers should follow the most recent guidance from the Equality and Human Rights Commission .' ,
  '3.2.b13' : 'Knowledge of appropriate programming, data visualisation, AI, and other computing skills required in the modern finance profession will be part of a degree programme. An ability to use such techniques on actual economic, financial or social data using suitable statistical or econometric software. An appreciation of both quantitative\n\n20\nand qualitative data and ability to select appropriate research methods to analyse such data.' ,
  '3.3.b9' : 'working with others (such as through group projects).' ,
  '4.4.b15' : 'assert intellectual independence and critical judgement.' ,
  '4.5.s1' : 'Typical graduates can distinguish themselves from threshold graduates by demonstrating a breadth and depth of knowledge and understanding and showing a clear and critical insight of the Finance discipline.' ,
  '4.5.s2' : 'They will demonstrate a rigorous understanding of Finance theories, paradigms, methods, concepts and principles along with a strong understanding of some specialised topics within the Finance field.' ,
  '4.5.s3' : 'They will possess a sophisticated ability to select and critically appraise a wide range of information, sources, views and knowledge which may be specialised within a sub-discipline of Finance or interdisciplinary in nature and recognise the uncertainty, ambiguity and limits of sources and knowledge.' ,
  '4.5.s4' : 'With a degree of autonomy, they will conduct thorough background investigation, reading, analysis, research, and/or study and solve complex finance problems, applying a wide range of established methodologies accurately.' ,
  '4.5.s5' : 'They will meaningfully select, evaluate, synthesize, discuss, communicate and present different information and results with substantiated arguments and demonstrate thorough and thoughtful interpretation of complex ideas and a high level of creativity and originality throughout their work.' ,
  '4.6.s1' : 'Excellent level graduates can distinguish themselves from threshold and typical graduates by showing exceptional knowledge and understanding of the Finance discipline, significantly beyond the typical level and beyond what has been taught.' ,
  '4.6.s2' : 'They will demonstrate an exceptional knowledge of Finance theories, paradigms, methods, concepts and principles and will have in-depth knowledge of a range of specialised areas within the Finance field.' ,
  '4.6.s3' : 'They will assert intellectual independence and conduct thorough and extensive background investigation, reading, analysis, research, and/or study well beyond the typical range.' ,
  '4.6.s4' : 'They will possess an exceptional ability to critically appraise a wide range of sources, views and knowledge and masterly appreciate the uncertainty, ambiguity and limits of those views, sources and knowledge.' ,
  '4.6.s5' : 'They will show exceptional problem-solving skills and a strong ability for decision-making and for solving complex finance problems, with a high degree of autonomy, justifying and evidencing the use and application of a wide range of established methodologies critically and accurately.' ,
  '4.6.s6' : 'They will proficiently select, evaluate, synthesize, discuss, communicate and present different views, information and results.' ,
  '4.6.s7' : 'They will construct and present substantiated arguments and demonstrate a sophisticated perception and critical insight of complex matters and ideas and an exceptional level of creativity, flair and originality throughout their work.' ,
}

# ---------------------------------------------------------------- run 0106: QAA Finance 2025 (std, S-02)
HON = "bachelor's with honours"
MA = "master's"
L6 = 'FHEQ level 6 (FQHEIS level 10 in Scotland)'
L7 = 'FHEQ level 7 (FQHEIS level 11 in Scotland)'
FH = 'qaa/fheq-2024/'
AD = 'qaa/fheq-2024/annex-d/'

def cite(n):
    return '(QAA, 2025, Finance Subject Benchmark Statement, para %s)' % n

META = dict(
  run='0106', p1='2026-10-03 17:30',
  title='Subject Benchmark Statement Finance',
  heading='Subject Benchmark Statement: Finance (QAA, April 2025)',
  edition='April 2025 (Fourth Edition)', published='2025-04',
  status='current',
  supersedes='the previous Finance statement, named only as "the previous Subject Benchmark Statement" (front matter); the back matter lists advisory groups for 2019 (minor update), 2014-2015 and 2007',
  subjects=[dict(scheme='hecos', code='100107', label='finance', basis='stated'),
            dict(scheme='cah', code='CAH17-01-07', label='finance', basis='stated'),
            dict(scheme='cah', code='CAH17-01', label='business and management', basis='inferred'),
            dict(scheme='cah', code='CAH17', label='business and management', basis='inferred'),
            dict(scheme='hecos', code='100832', label='financial management', basis='stated'),
            dict(scheme='hecos', code='100827', label='banking', basis='stated'),
            dict(scheme='hecos', code='100828', label='investment', basis='stated')],
  awards=[HON, MA, "integrated master's"],
  levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
  nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
  series='QAA Subject Benchmark Statements, 2025 revision with cross-cutting themes (this statement: Fourth Edition, published 10 April 2025, D1 back matter)',
  partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
  agentDefinition=("This document is the structured ingestion of QAA's Subject Benchmark Statement for Finance (April 2025). "
    "Read it to learn what a Finance graduate is expected to know, understand and do: the threshold list for the bachelor's degree with honours (4.4), "
    "the typical and excellent levels written as prose (4.5, 4.6), the subject knowledge and generic skills lists (3.2, 3.3) and the duties it places on courses. "
    "Each statement carries the issuer's text in `source`, our paraphrase, a version for staff and one for students, and two instructions for AI agents. "
    "It is a sector reference point, not a regulation; levels are pointed to in the FHEQ and FQHEIS documents by id."),
  summary=("Finance, as a single, joint or combined bachelor's degree and as specialist, conversion or integrated master's study. "
    "Benchmark standards are given for the bachelor's degree only: a threshold list of 15 items (4.4) and typical and excellent levels as two prose paragraphs, cut here into 5 and 7 sentence records; "
    "master's courses are referred to the statement's highest levels (1.15). Two outcome lists, subject knowledge and skills (13) and cognitive and generic skills (9), sit in section 3. "
    "Cross-cutting themes: equality, diversity and inclusion; accessibility; education for sustainable development; employability, enterprise and entrepreneurship; generative AI. "
    "Frameworks: FHEQ and FQHEIS levels 4 to 7 and 8 to 11, with Annex D for evidence of achievement. Bodies: PSRBs in general and eighteen named professional and learned bodies (2.25, 2.26), the FRC, Advance HE and the EHRC."),
  authority='reference: "not a regulatory requirement"; sector-owned reference points; part of the quality arrangements in Scotland, Wales and Northern Ireland, not sector-recognised standards in England (D1, front matter)',
)

S2 = dict(
  governs="what can be expected of a Finance graduate, at bachelor's and master's level, in knowledge, skills and understanding, with the nature of awards in the subject (D1, front matter; 1.1; 4.1)",
  awards=["bachelor's degrees with honours, single, joint or combined", "specialist master's", "conversion master's", "integrated master's", "exit awards CertHE and DipHE (2.12)"],
  levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7', 'fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'],
  doesNot='it does not prescribe teaching, learning or assessment, does not interpret legislation, carries no statutory or regulatory requirement and does not cover single honours accounting or economics (D1, front matter; 1.5)',
  statedScope='"This Subject Benchmark Statement sets out what is typically expected of successful graduates from bachelor\'s and master\'s level programmes in Finance, or Finance combined with another subject, offered by higher education providers in the UK." (D1, 1.1)',
  statedSubjects=[
    dict(name='Finance', locator='(D1, title; 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100107', label='finance'), dict(scheme='cah', code='CAH17-01-07', label='finance')]),
    dict(name="'finance' or 'financial management'", locator='(D1, 1.3)', kind='programme title', codes=[dict(scheme='hecos', code='100107', label='finance'), dict(scheme='hecos', code='100832', label='financial management')]),
    dict(name='banking', locator='(D1, 1.3)', kind='programme title', codes=[dict(scheme='hecos', code='100827', label='banking')]),
    dict(name='investment', locator='(D1, 1.3)', kind='programme title', codes=[dict(scheme='hecos', code='100828', label='investment')]),
    dict(name='financial services, personal finance, sustainable finance, fintech, finance and data analytics, finance and AI', locator='(D1, 1.3)', kind='programme title', codes=[]),
    dict(name='Finance in a joint degree with accounting, management, economics, business, a modern language, law, engineering, computing, statistics or mathematics', locator='(D1, 1.4; 2.5)', kind='programme title', codes=[dict(scheme='hecos', code='100107', label='finance')]),
    dict(name="specialist master's and conversion master's degrees in Finance", locator='(D1, 1.15)', kind='programme title', codes=[dict(scheme='hecos', code='100107', label='finance')]),
    dict(name="integrated master's degrees in Finance", locator='(D1, 1.17; 2.16)', kind='programme title', codes=[dict(scheme='hecos', code='100107', label='finance')]),
  ])

SECTIONS = {'1': 'Context and purposes of a Finance degree', '2': 'Distinctive features of the Finance degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.5', 'Context and purposes of a Finance degree'),
       ('1.6', '1.17', 'Purposes and characteristics of a Finance degree'),
       ('1.18', '1.27', 'Equality, diversity and inclusion'),
       ('1.28', '1.29', 'Accessibility and the needs of disabled students'),
       ('1.30', '1.36', 'Education for sustainable development'),
       ('1.37', '1.42', 'Employability, enterprise and entrepreneurship education'),
       ('1.43', '1.47', 'Generative artificial intelligence (GenAI) and AI applications in finance'),
       ('2.1', '2.4', 'Introduction'), ('2.5', '2.8', 'Design'), ('2.9', '2.17', 'Progression'),
       ('2.18', '2.21', 'Flexibility'), ('2.22', '2.26', 'Partnership'), ('2.27', '2.30', 'Monitoring and review'),
       ('3.1', '3.1', 'Content, structure and delivery'),
       ('3.2', '3.2', 'Subject-specific knowledge and skills'), ('3.3', '3.3', 'Cognitive abilities and generic skills'),
       ('3.4', '3.8', 'Teaching and learning'), ('3.9', '3.14', 'Assessment'),
       ('4.1', '4.3', 'Introduction'), ('4.4', '4.4', 'Threshold level'), ('4.5', '4.5', 'Typical level'), ('4.6', '4.6', 'Excellent level')]

G = {
 '1.1': 'scope: bachelor\'s and master\'s Finance, conceptual and applied',
 '1.2': 'what finance covers, traditional and emerging fields',
 '1.3': 'typical course titles and related titles',
 '1.4': 'Finance in joint degrees; balance of theory and practice',
 '1.5': 'accounting and economics: their own statements',
 '1.6': 'purpose of the degree; two main domains',
 '1.7': 'markets and institutions; investment and corporate finance; newer areas',
 '1.8': 'perspectives on finance; ethical and social awareness',
 '1.9': 'careers the degree leads to',
 '1.10': 'sectors graduates work in',
 '1.11': 'work across national borders',
 '1.12': 'why students choose Finance',
 '1.13': 'wider aims, the SDGs, computational and higher skills',
 '1.14': 'apprenticeships and placement-year courses',
 '1.15': "two kinds of master's: specialist and conversion",
 '1.16': "master's: taught study and self-directed research",
 '1.17': "integrated master's: typical honours then master's level",
 '1.18': 'what EDI covers; embedding it in the discipline',
 '1.19': 'principles for an inclusive learning community',
 '1.20': 'inequality in finance and access to it',
 '1.21': 'finance education and the SDGs on inequality',
 '1.22': 'widening participation; an environment where all thrive',
 '1.23': 'inclusive teaching modes and assessment',
 '1.24': 'ways to embed EDI in learning and resources',
 '1.25': 'EDI topics a Finance degree can explore',
 '1.26': 'digital delivery, AI and their effect on EDI',
 '1.27': 'monitoring and reviewing EDI in courses',
 '1.28': 'accessibility: removing barriers, regulatory minimum',
 '1.29': 'inclusive design: examples for accessible courses',
 '1.30': 'sustainable finance and its guiding frameworks',
 '1.31': 'environmental, social and governance factors and the SDGs',
 '1.32': 'sustainability practice and its limits in finance',
 '1.33': 'sustainable solutions across disciplines',
 '1.34': 'ESD competencies and sustainable decision making',
 '1.35': 'core competencies for sustainable futures',
 '1.36': 'ESG disclosure, environmental assets, tools',
 '1.37': 'what enterprise and entrepreneurship education does',
 '1.38': 'EED and employability; transferable skills',
 '1.39': 'software and data skills',
 '1.40': 'placements, simulations and industry engagement',
 '1.41': 'entrepreneurship beyond employment; wider context',
 '1.42': 'experiential learning and awareness of industry change',
 '1.43': 'what GenAI is and its uses in finance',
 '1.44': 'AI change and its effect on the profession',
 '1.45': 'learning to use AI and judge its limits',
 '1.46': 'teaching and assessment adapt to AI',
 '1.47': 'integrity with AI; following current guidance',
 '2.1': 'markets, instruments and institutions studied',
 '2.2': 'learning objectives, perspectives, design flexibility',
 '2.3': 'accounting knowledge needed; joint degrees',
 '2.4': 'lifelong learning and range of careers',
 '2.5': "undergraduate and master's course designs",
 '2.6': "bachelor's designed to section 4's outcomes",
 '2.7': "variation among master's courses",
 '2.8': 'integrating knowledge for work and society',
 '2.9': 'progression through levels to the rungs',
 '2.10': "readiness for master's study",
 '2.11': 'joint degree students and the core skills',
 '2.12': 'exit awards: CertHE and DipHE',
 '2.13': 'placement or study abroad',
 '2.14': "full master's: credit, dissertation, empirical work",
 '2.15': 'postgraduate certificates and diplomas',
 '2.16': "integrated master's: duration and level 7 study",
 '2.17': "research in master's education",
 '2.18': 'course length across the UK nations',
 '2.19': "length of master's courses",
 '2.20': 'modes of learning and credit routes',
 '2.21': 'flexibility kept coherent; EDI duties',
 '2.22': 'validation, franchising and apprenticeships',
 '2.23': 'kinds of partnership',
 '2.24': 'PSRB recognition and professional frameworks',
 '2.25': 'networks and learned societies',
 '2.26': 'advanced standing with professional bodies',
 '2.27': 'monitoring and periodic review',
 '2.28': 'external review, employers and professional bodies',
 '2.29': 'external examiners',
 '2.30': 'advisory boards',
 '3.1': 'how to read the outcome lists and examples',
 '3.2': "subject knowledge and skills at bachelor's completion",
 '3.3': "cognitive and generic skills at bachelor's completion",
 '3.4': "each course's choice of activities",
 '3.5': 'what shapes teaching and learning design',
 '3.6': 'active learning and the methods used',
 '3.7': 'blended delivery and academic integrity',
 '3.8': 'support for students from diverse backgrounds',
 '3.9': 'a balanced mix of assessment',
 '3.10': 'formative and summative balance',
 '3.11': 'reliability of assessment; programme-level review',
 '3.12': 'problem-solving and authentic assessment',
 '3.13': 'range of assessment formats, data-oriented tasks',
 '3.14': 'informed design and regular review',
 '4.1': 'the three levels set for the bachelor\'s award',
 '4.2': 'most exceed the minimum; Annex D for evidence',
 '4.3': 'not competence standards; Equality Act guidance',
 '4.4': 'threshold list for the bachelor\'s graduate',
 '4.5': 'the typical level, in prose',
 '4.6': 'the excellent level, in prose',
}
CTYPE = {'1.2': 'area', '1.7': 'area', '2.1': 'area', '2.3': 'area',
         '3.5': 'practice', '3.6': 'practice', '3.7': 'practice', '3.8': 'practice',
         '3.9': 'practice', '3.10': 'practice', '3.12': 'practice', '3.13': 'practice'}
EXCLUDED = [
  dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2 and S7'),
  dict(number='none', heading='Contents', kind='other: table of contents'),
  dict(number='1, 2, 3, 4', heading='section headings', kind='other: headings, recorded as section components'),
  dict(number='5', heading='List of references and further resources', kind='other: references, read for SB6 and D3'),
  dict(number='6', heading='Membership of the Advisory Group', kind='other: membership lists (2025, 2019, 2014-2015, 2007) and the copyright notice'),
]

P = {}
def s(i, **k):
    if i in FIND:
        k['find'] = FIND[i]
    P[i] = k

# ---------------------------------------------------------------- aaw and aad builders (our words; each record supplies its specifics)
def aaw(n, what, place, notclaim, beside):
    return ('Describe this as %s. %s Cite it as %s. Do not claim %s; set it beside %s.' % (what, place, cite(n), notclaim, beside))

def aad(when, how, ask, avoid):
    return 'Raise it when %s. %s Ask: "%s" Avoid %s.' % (when, how, ask, avoid)

STUDENT = 'Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show.'
STAFF = 'Put it to the programme team as a design or review duty in their own terms.'
NOSTUDENT = 'reading the paragraph aloud and handing this duty to a student as if it were theirs'
PLACE6 = 'Place it at %s, for the bachelor\'s degree with honours.' % L6

# ---------------------------------------------------------------- section 1 to 4 statements outside the rung and outcome lists
s('1.4', type='expectation', rung='none', force='should', level='none', appliesTo='joint and combined Finance degrees', addressee='provider',
  verbs=['used', 'maintained'], about='joint degrees read with the partner subject\'s statement', domain='none', award=HON,
  para='Where Finance is one half of a joint degree, the statement should be read together with the statements for the other discipline, keeping the balance of theory and application intact.',
  prac='For a joint or combined award, read this statement alongside the partner subject\'s statement, and check that the Finance part keeps its scope, depth and balance of theory and practice.',
  ben=('n/a', 'a duty on those who design joint courses'),
  aaw=aaw('1.4', 'guidance that should shape joint and combined Finance courses, addressed to course designers', 'Apply it to joint honours at bachelor\'s level.', 'that it sets learning outcomes for students or that it overrides the partner subject\'s statement', 'the other subject\'s statement and paragraph 2.11 on what joint degree students achieve'),
  aad=aad('a team is designing or reviewing a joint or combined award with Finance', STAFF, 'Which statement did you use for the other half, and where would theory or application be thin?', NOSTUDENT))
s('1.6', type='requirement', rung='none', force='must', level='none', appliesTo='students of Finance', addressee='learner',
  verbs=['educate', 'study', 'focuses'], about='fundamentals and new developments in theory and practice', domain='knowledge', award=[HON, MA],
  para='A Finance degree aims to help students understand what finance does in business and organisations, as a base for many careers; it requires study of both the foundations and the newest work in finance theory and practice.',
  prac='Build the curriculum so that students study both the established foundations and current advances in finance theory and practice, organised around two main subject domains.',
  ben='Studying finance means learning both its established foundations and its newest ideas, in theory and in practice, so that you understand what finance does in organisations.',
  aaw=aaw('1.6', 'a requirement the subject places on every Finance student: to study both foundations and new developments', 'Treat it as holding for bachelor\'s and master\'s study alike, without a level of its own.', 'that it is an assessed outcome or a regulatory rule', 'paragraph 1.7 (the two domains) and the threshold item 4.4.b1'),
  aad=aad('a student asks what a Finance degree is for or why new topics keep entering the course', STUDENT, 'Which parts of your course feel like foundations and which feel like current developments?', 'reading the text aloud at length and treating it as a graded standard'))
s('1.7', type='requirement', rung='none', force='must', level='none', appliesTo='students of Finance', addressee='learner',
  verbs=['requires', 'understand', 'expected'], about='the two core domains and contemporary areas', domain='understanding', award=[HON, MA],
  para='Students must understand two domains: how markets, banks, exchanges and institutions are designed and work, with the roles of governments and individuals; and investment, value, corporate finance, securities analysis, risk and international financial management. They are also expected to understand newer areas such as climate and sustainable finance, fintech, AI and data analytics, alternative investments and global uncertainty.',
  prac='Cover both core domains, financial markets and institutions, and investment and corporate finance, and add contemporary areas such as sustainable finance, fintech, AI and alternative investments; the newer areas are expected, the core domains required.',
  ben='You will need to understand how financial markets and institutions work and the principles of investment, value, corporate finance and risk; you are also expected to understand newer areas such as sustainable finance, fintech and AI.',
  aaw=aaw('1.7', 'what the subject requires students to understand (the two core domains) and what it also expects (contemporary areas, given as examples)', 'Treat it as holding for bachelor\'s and master\'s study, without a level of its own.', 'that the listed contemporary areas are compulsory topics, since the text says they may include others', 'the subject knowledge list 3.2.b1 to 3.2.b12 and threshold items 4.4.b5 and 4.4.b6'),
  aad=aad('a student or a module team asks what core content a Finance course must cover', 'With a student use plain words and the second person; with staff separate the required domains from the expected newer areas.', 'Which of the two core domains do you feel more secure in, and which newer area have you met so far?', 'reciting the lists and presenting the example areas as a fixed syllabus'))
s('1.8', type='expectation', rung='none', force='will', level='none', appliesTo='students of Finance', addressee='learner',
  verbs=['become'], about='awareness of the ethical and social side of finance', domain='understanding', award=[HON, MA],
  para='Finance can be studied from behavioural, ethical, economic, sustainable and statistical angles; students will at least become conscious of the ethical and social sides of financial activity and systems, as well as the economic ones.',
  prac='Whatever the angle a course takes, make sure every student will come away conscious of the ethical and social sides of financial activity, not only the economic one.',
  ben='Whatever your route through the subject, you will become aware of the ethical and social side of financial activity and systems, not only the economics.',
  aaw=aaw('1.8', 'a minimum expected outcome, in "will", for every Finance student', 'Read it at the level of the award the student is taking; it names no level.', 'that it requires a separate ethics module', 'threshold item 4.4.b4 (governance and ethics) and the level 6 descriptor %s4.15.b7' % FH),
  aad=aad('a student treats finance as purely technical or asks why ethics appears in the course', STUDENT, 'Can you name one financial decision you studied where the ethical or social effect mattered as much as the return?', 'lecturing and treating awareness as if it were a graded rung'))
s('1.15.b1', type='expectation', rung='none', force='describes', level='fheq:7', appliesTo="specialist master's degrees in Finance", addressee='provider',
  verbs=['involve', 'expected', 'evaluated', 'required'], about="specialist master's judged against the highest levels", domain='none', award=MA,
  para="Specialist master's courses go deeper into one or more core bachelor's components and may add related specialisms; they would be expected to be judged against the statement's highest levels of achievement plus content criteria for their focus, and usually admit holders of at least a second-class Finance degree.",
  prac="Judge a specialist master's in Finance against the excellent level (4.6) and against extra content criteria for its specialism; entry is usually a second-class Finance honours degree or above.",
  ben=('n/a', 'a statement about how a course is evaluated and who it admits'),
  aaw=aaw('1.15.b1', 'how the statement would expect a specialist master\'s to be evaluated: against its highest levels, the excellent rung', 'Place the award at %s.' % L7, 'that the statement sets master\'s rungs of its own or that this wording ("would be expected") is a requirement', 'the excellent level 4.6.s1 to 4.6.s7 and the master\'s descriptor %s4.17.b1' % FH),
  aad=aad("a team designs or reviews a specialist master's in Finance", STAFF, 'Which excellent-level sentences does your programme specification reach, and what content criteria does your specialism add?', 'telling a student that the excellent rung is the pass mark for a master\'s'))
s('1.18', type='expectation', rung='none', force='should', level='none', appliesTo='Finance courses and the discipline', addressee='provider',
  verbs=['embedded', 'reflect'], about='EDI embedded in the culture and practice of Finance', domain='none', award='none',
  para='Equality, diversity and inclusion take in many identity characteristics and their intersections; EDI should be built meaningfully into the culture and practice of the discipline and every Finance course, which also reflect industry EDI codes where suitable.',
  prac='Embed EDI meaningfully in the culture, practice and curriculum of every Finance course, and refer to industry EDI codes where they apply.',
  ben=('n/a', 'a duty on the course and the discipline'),
  aaw=aaw('1.18', 'an expectation, in "should", on Finance courses to embed EDI', 'It holds for every award and has no level.', 'that it sets a student outcome or a legal duty beyond the equality duties it mentions', 'paragraphs 1.22 to 1.27 and the theme record theme:edi'),
  aad=aad('a team reviews a programme for inclusion or an EDI audit is due', STAFF, 'Where in the curriculum and its culture is EDI visible to students, and where is it only a policy?', NOSTUDENT))
s('1.22', type='requirement', rung='none', force='must', level='none', appliesTo='Finance educators', addressee='provider',
  verbs=['create', 'thrive'], about='an environment where every student can thrive', domain='none', award='none',
  para='Students from varied backgrounds come to Finance; whatever the combination taught, those who teach it must create an environment in which all students can thrive and feel represented and included, starting with widening participation.',
  prac='Create a learning environment where every student can thrive and feels represented and included, and support widening participation to limit the effect of economic disadvantage.',
  ben=('n/a', 'a duty on those who teach'),
  aaw=aaw('1.22', 'a requirement, in "must", on those who teach Finance', 'It holds at every level.', 'that it sets a student outcome', 'paragraph 1.18 and the theme record theme:edi'),
  aad=aad('teaching staff discuss belonging, attainment gaps or widening participation', STAFF, 'Which groups of students feel least represented in your examples and case studies?', NOSTUDENT))
s('1.23', type='expectation', rung='none', force='should', level='none', appliesTo='Finance assessment design', addressee='provider',
  verbs=['designed'], about='inclusive assessment and alternatives', domain='none', award='none',
  para='Teaching and assessment in Finance should reflect EDI principles; varied teaching modes can be used, and assessment should be as inclusive as possible, for instance by offering alternative types, timings or modes where suitable.',
  prac='Design assessment to be as inclusive as possible: offer alternatives in type, duration and mode where suitable, such as a written task for a presentation or extra exam time.',
  ben=('n/a', 'a duty on the course; a student meets its effect as alternative assessment'),
  aaw=aaw('1.23', 'an expectation, in "should", on assessment design', 'It holds at every level.', 'that students have a right to any one listed alternative', 'paragraph 1.29.b8 on accessible assessment and Annex D, %s' % 'std:doc:qaa-fheq-2024-framework'),
  aad=aad('an assessment strategy is being written or reviewed', STAFF, 'Which assessments could take a different form without changing what they test?', NOSTUDENT))
s('1.24.b1', type='requirement', rung='none', force='must', level='none', appliesTo='learning environments', addressee='provider',
  verbs=['flexible', 'reflect'], about='flexible environments that reflect diversity', domain='none', award='none',
  para='Physical and online learning environments must be adaptable and mirror the diversity of the students.',
  prac='Make physical and virtual learning spaces flexible and reflective of the students who use them.',
  ben=('n/a', 'a duty on the course and its spaces'),
  aaw=aaw('1.24', 'a requirement, in "must", on learning environments, given as one example of embedding EDI', 'It holds at every level.', 'that it is a student outcome', 'the other items of 1.24 and paragraph 1.29.b3 on safe learning spaces'),
  aad=aad('a team reviews its rooms, virtual learning environment or timetable', STAFF, 'Who finds your learning spaces hardest to use, and why?', NOSTUDENT))
s('1.24.b2', type='expectation', rung='none', force='should', level='none', appliesTo='teaching and assessment materials', addressee='provider',
  verbs=['reflected', 'ensure'], about='diverse perspectives in materials', domain='none', award='none',
  para='Teaching and assessment materials, readings and case studies included, should carry varied perspectives so that no student\'s background puts them at a disadvantage.',
  prac='Choose readings, cases and assessment materials that carry varied perspectives, so that no student is disadvantaged by background.',
  ben=('n/a', 'a duty on those who choose materials'),
  aaw=aaw('1.24', 'an expectation, in "should", on teaching and assessment materials', 'It holds at every level.', 'that every reading list must meet a quota', 'paragraph 1.29.b2 on materials reflecting the cohort'),
  aad=aad('a module team refreshes its reading list or case studies', STAFF, 'Whose markets, firms and households appear in your cases, and whose are missing?', NOSTUDENT))
s('1.24.b3', type='requirement', rung='none', force='must', level='none', appliesTo='Finance teaching', addressee='provider',
  verbs=['necessary'], about='the hidden curriculum and the language of finance', domain='none', award='none',
  para='The hidden curriculum needs attention, above all the specialist language of finance, so that it does not get in the way of learning.',
  prac='Attend to the hidden curriculum, especially the jargon of finance, so that unspoken expectations and terms do not block learning.',
  ben=('n/a', 'a duty on those who teach'),
  aaw=aaw('1.24', 'a requirement read from "is necessary", on attention to the hidden curriculum', 'It holds at every level.', 'that the issuer used "must" here: the force is our reading (Part E)', 'paragraph 1.29.b4 and QAA\'s guide on the hidden curriculum (not yet ingested)'),
  aad=aad('students struggle with finance terms or unstated expectations', STAFF, 'Which terms do you use in week one that students have never been taught?', NOSTUDENT))
s('1.24.b7', type='requirement', rung='none', force='must', level='none', appliesTo='placements, work experience and visits', addressee='provider',
  verbs=['offered'], about='equal access to placements and visits', domain='none', award='none',
  para='Where a Finance course offers a placement, work experience or industry visit, equality of access for all students must be considered.',
  prac='When you offer placements, work experience or industry visits, consider whether every student can take them up on equal terms.',
  ben=('n/a', 'a duty on the course'),
  aaw=aaw('1.24', 'a requirement, in "must", on access to placements and visits', 'It holds at every level.', 'that the statement requires every course to offer a placement', 'paragraph 1.29.b5 on equal opportunities for placements'),
  aad=aad('a team plans placements or industry visits', STAFF, 'Which students could not take up this placement, and what would let them?', NOSTUDENT))
s('1.27', type='expectation', rung='none', force='should', level='none', appliesTo='Finance courses', addressee='provider',
  verbs=['examine', 'enhanced'], about='monitoring and review of EDI', domain='none', award='none',
  para='Finance courses should monitor and review EDI to see how well current policies work and how to improve them.',
  prac='Monitor and review how well your EDI policies are working in the programme, and plan improvements.',
  ben=('n/a', 'a duty on the course'),
  aaw=aaw('1.27', 'an expectation, in "should", on course monitoring', 'It holds at every level.', 'that it sets a reporting format', 'paragraphs 2.27 to 2.30 on monitoring and review'),
  aad=aad('an annual or periodic review is being prepared', STAFF, 'What evidence shows your EDI measures are working, and what would you change?', NOSTUDENT))
s('1.28', type='expectation', rung='none', force='should', level='none', appliesTo='Finance courses', addressee='provider',
  verbs=['meet', 'apply'], about='accessibility at every stage, regulatory minimum', domain='none', award='none',
  para='Accessibility means removing barriers so that learners can reach outcomes fairly; it should at least meet regulatory requirements and will apply at every stage, from pre-application information to graduation and after.',
  prac='Meet the regulatory requirements for accessibility as a minimum and apply them at every stage, from pre-application information to after graduation; draw on institutional guidance and support.',
  ben=('n/a', 'a duty on the course; a student meets its effect'),
  aaw=aaw('1.28', 'an expectation, in "should", that accessibility meets regulation as a minimum, applying at every stage', 'It holds at every level.', 'that it restates the law in detail', 'paragraph 1.29\'s examples and the theme record theme:accessibility'),
  aad=aad('a team designs or reviews a course for accessibility', STAFF, 'Where in the student journey, from applying to graduating, is access weakest?', NOSTUDENT))
s('1.29.b4', type='expectation', rung='none', force='should', level='none', appliesTo='software and data resources', addressee='provider',
  verbs=['accessible', 'considered'], about='accessible databases, simulations and software', domain='none', award='none',
  para='Databases, simulation tools and software should be usable by every student, for example through remote access or quiet spaces; accessibility counts when choosing them, and class materials take account of the hidden curriculum.',
  prac='Make databases, trading simulations and software accessible to all, for example by remote access or low-stimulation spaces, and weigh accessibility when you choose them.',
  ben=('n/a', 'a duty on the course and its resources'),
  aaw=aaw('1.29', 'an expectation, in "should", on accessible data and software resources', 'It holds at every level.', 'that it names products or standards', 'threshold item 4.4.b8 (statistical analysis with software) and 1.24.b3'),
  aad=aad('a team buys or renews data terminals, simulations or software', STAFF, 'Can a student who cannot reach the trading room use these tools?', NOSTUDENT))
s('1.29.b5', type='expectation', rung='none', force='should', level='none', appliesTo='placements and wider opportunities', addressee='provider',
  verbs=['available'], about='the same opportunities for every student', domain='none', award='none',
  para='Placements, internships, international learning and extracurricular activities should be open to every student whatever their background, disability or other protected characteristic.',
  prac='Open placements, internships, international and extracurricular opportunities to every student on equal terms.',
  ben=('n/a', 'a duty on the course'),
  aaw=aaw('1.29', 'an expectation, in "should", that wider opportunities are open to all', 'It holds at every level.', 'that every course must offer each opportunity named', 'item 1.24.b7'),
  aad=aad('a team reviews who takes up placements or study abroad', STAFF, 'Which groups take up these opportunities least, and why?', NOSTUDENT))
s('1.29.b7', type='expectation', rung='none', force='should', level='none', appliesTo='Finance courses', addressee='provider',
  verbs=['taken', 'lessen'], about='barriers to attendance and achievement', domain='none', award='none',
  para='Courses should take account of what keeps students from attending or achieving, such as caring duties and digital poverty, and act where they can to reduce it.',
  prac='Identify barriers such as caring responsibilities and digital poverty and take what steps you can to reduce their effect on learning.',
  ben=('n/a', 'a duty on the course'),
  aaw=aaw('1.29', 'an expectation, in "should", on reducing barriers to attendance and achievement', 'It holds at every level.', 'that it obliges any single remedy', 'items 1.29.b4 and 1.29.b5'),
  aad=aad('a team looks at attendance or attainment data', STAFF, 'What stops some students from attending, and what could the course change?', NOSTUDENT))
s('1.29.b8', type='expectation', rung='none', force='should', level='none', appliesTo='assessment methods', addressee='provider',
  verbs=['consider', 'demonstrated'], about='accessible assessment of outcomes', domain='none', award='none',
  para='Assessment in Finance should take accessibility into account; outcomes can often be shown another way through alternative assessment.',
  prac='Check each assessment for accessibility and, where needed, let students show the same outcome another way.',
  ben=('n/a', 'a duty on assessment design'),
  aaw=aaw('1.29', 'an expectation, in "should", on accessible assessment', 'It holds at every level.', 'that alternatives change the outcome being tested', 'paragraph 1.23'),
  aad=aad('an assessment is being redesigned', STAFF, 'Could this outcome be shown in another way without lowering the standard?', NOSTUDENT))
s('1.29.b9', type='expectation', rung='none', force='should', level='none', appliesTo='Finance programmes', addressee='provider',
  verbs=['made'], about='universal design and assessment choice', domain='none', award='none',
  para='Courses should consider universal design for learning and build choice of assessment into Finance programmes.',
  prac='Consider universal design for learning and build assessment choice into the programme.',
  ben=('n/a', 'a duty on course design'),
  aaw=aaw('1.29', 'an expectation, in "should", to consider universal design and assessment choice', 'It holds at every level.', 'that it requires choice in every assessment', 'item 1.29.b8 and item 1.29.b10'),
  aad=aad('a programme is being designed or revalidated', STAFF, 'Where could students choose how they show an outcome?', NOSTUDENT))
s('1.29.b10', type='expectation', rung='none', force='should', level='none', appliesTo='learning, teaching and assessment design', addressee='provider',
  verbs=['taken', 'build', 'avoid'], about='proactive inclusive design for neurodivergent students', domain='none', award='none',
  para='Learning, teaching and assessment should be designed ahead of time to include everyone and to avoid barriers for neurodivergent students and those with specific learning difficulties.',
  prac='Design learning, teaching and assessment in advance to include neurodivergent students and those with specific learning difficulties, rather than adjusting later.',
  ben=('n/a', 'a duty on course design'),
  aaw=aaw('1.29', 'an expectation, in "should", for proactive inclusive design', 'It holds at every level.', 'that individual adjustments are no longer needed', 'item 1.24 (access for neurodivergent community members) and item 1.29.b9'),
  aad=aad('a team designs a new module or assessment', STAFF, 'What would a neurodivergent student find hardest here, and can you remove it now?', NOSTUDENT))
s('1.33', type='expectation', rung='none', force='should', level='none', appliesTo='students of Finance', addressee='learner',
  verbs=['viewed', 'foster', 'understand'], about='sustainable solutions as part of wider efforts', domain='understanding', award=[HON, MA],
  para='Finance degrees aim to equip students to devise sustainable solutions for a stable financial system; these should be seen as one part of efforts across disciplines on climate, nature, pollution, inequality and uncertainty, which call for critical and creative skills that cross subject boundaries.',
  prac='Teach sustainable financial solutions as one part of work across disciplines on climate, nature loss and inequality, and build the critical and creative skills that cross subject lines.',
  ben='You should see the sustainable solutions you work on in finance as one part of a wider effort across many disciplines, and build critical and creative skills that cross subject lines.',
  aaw=aaw('1.33', 'an expectation, in "should", about how students frame sustainable financial solutions', 'Read it at the award the student is taking; it names no level.', 'that it requires an interdisciplinary module', 'threshold item 4.4.b11, item 3.2.b12 and the theme record theme:esd'),
  aad=aad('a student works on a sustainability problem in finance', STUDENT, 'Which other discipline would you need to talk to for this problem to be solved well?', 'reading the text aloud and presenting it as an assessed rung'))
s('1.34', type='expectation', rung='none', force='should', level='none', appliesTo="bachelor's and master's Finance degrees", addressee='provider',
  verbs=['align', 'develop', 'prioritise'], about='competencies for sustainable decisions and disclosure', domain='none', award=[HON, MA],
  para='The core skills of Finance degrees match the ESD guidance\'s outcomes, among them systems, anticipatory, strategic and critical thinking and integrated problem-solving; Finance degrees should develop capacities that put sustainable decisions and disclosure first.',
  prac='Develop capacities and competencies that put sustainable decision making and disclosure first, using the ESD guidance\'s competencies as a reference.',
  ben=('n/a', 'a duty on course design; the student-facing outcome is 4.4.b11'),
  aaw=aaw('1.34', 'an expectation, in "should", on course design for sustainability', 'It holds for bachelor\'s and master\'s degrees.', 'that the ESD guidance is mandatory', 'the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance and threshold item 4.4.b11'),
  aad=aad('a team maps its programme to sustainability or the ESD guidance', STAFF, 'Where does a student make a sustainable decision or disclosure judgement in your programme?', NOSTUDENT))
s('1.41', type='expectation', rung='none', force='should', level='none', appliesTo='graduates of the subject', addressee='learner',
  verbs=['provides', 'appreciation'], about='the wider context of finance skills', domain='understanding', award=[HON, MA],
  para='Entrepreneurship education helps students build a rewarding, self-directed working life that adds social, cultural and economic value; Finance graduates should appreciate the wider setting in which they apply their skills, including sustainability, climate finance and nature and biodiversity finance.',
  prac='Graduates should appreciate where their skills are used, including sustainability, climate finance and biodiversity finance; build this into enterprise education.',
  ben='You should come to appreciate the wider setting for your finance skills, including sustainability, climate finance and finance for nature and biodiversity.',
  aaw=aaw('1.41', 'an expectation, in "should", that graduates appreciate the wider context of their skills', 'Read it at the award the student is taking.', 'that it makes entrepreneurship compulsory', 'threshold item 4.4.b11 and the theme records theme:enterprise and theme:esd'),
  aad=aad('a student talks about careers or the purpose of their finance skills', STUDENT, 'Where might your finance skills add value beyond profit in a job you would like?', 'presenting it as a graded outcome and lecturing on values'))
s('2.2', type='expectation', rung='none', force='should', level='none', appliesTo='Finance courses and their students', addressee='both',
  verbs=['designed', 'develop', 'evaluate'], about='critical thinking and the ethical and regulatory side of finance', domain='subject-skill', award=[HON, MA],
  para='Finance courses align learning objectives with section 4 and should be designed so that students can build critical thinking and apply judgement to finance problems; design flexibility is needed for AI, fintech and digital assets, and students should be able to judge the ethical, sustainability and regulatory sides of financial activity, not only how institutions work or how products are priced.',
  prac='Design objectives that integrate concept and application and let students develop critical thinking and judgement; students should be able to evaluate the ethical, sustainability and regulatory dimensions of finance, beyond pricing and functions.',
  ben='You should be able to judge the ethical, sustainability and regulatory side of financial activity, not only how institutions work or how products are priced, and use critical thinking on finance problems.',
  aaw=aaw('2.2', 'an expectation, in "should", with two parts: course design for critical thinking, and a student ability to evaluate ethical, sustainability and regulatory dimensions', 'Read it with the bachelor\'s threshold at %s.' % L6, 'that design flexibility for AI is a requirement on students', 'threshold items 4.4.b4 and 4.4.b10 and the level 6 descriptor %s4.15.b7' % FH),
  aad=aad('a student only describes how a product works, or a team reviews learning objectives', 'With a student use the second person and plain words; with staff, separate the design duty from the student ability.', 'Beyond how it is priced, what are the ethical and regulatory questions about this product?', 'reading the paragraph aloud and turning the design duty into a student task'))
s('2.3', type='requirement', rung='none', force='must', level='none', appliesTo='students of Finance', addressee='learner',
  verbs=['required'], about='a reasonable knowledge of accounting', domain='knowledge', award=[HON, MA],
  para='Deep accounting knowledge is not required, but a reasonable knowledge of accounting principles, the regulation of financial reporting, what financial statements contain and how accounting information informs decisions is required; joint degrees with Finance include most of the statement\'s knowledge and skills.',
  prac='Teach enough accounting for a reasonable command of its principles, financial reporting regulation, the content of financial statements and using accounting information for decisions; depth beyond that depends on the programme.',
  ben='You do not need deep accounting, but you are required to know the principles of accounting, how financial reporting is regulated, what financial statements contain and how accounting information supports decisions.',
  aaw=aaw('2.3', 'a requirement, read from "is required", for reasonable accounting knowledge', 'Read it with the bachelor\'s award at %s.' % L6, 'that the degree must teach accounting in depth', 'item 3.2.b8 on financial statements and the Accounting statement std:doc:qaa-accounting-2025-benchmarks'),
  aad=aad('a student without an accounting background worries about the accounting content', STUDENT, 'Could you read a set of financial statements and say what they tell a decision maker?', 'implying that deep accounting is required'))
s('2.4', type='expectation', rung='none', force='should', level='none', appliesTo='Finance courses', addressee='provider',
  verbs=['prepare', 'designed', 'thrive'], about='lifelong learning and a range of careers', domain='none', award=[HON, MA],
  para='Finance courses should ready students for self-directed learning throughout life and be designed so that they can flourish in many finance careers across sectors, in enterprise or in further study.',
  prac='Design the programme to prepare students for self-directed, lifelong learning and for careers across public, private and third sectors, enterprise or further study.',
  ben=('n/a', 'a duty on course design'),
  aaw=aaw('2.4', 'an expectation, in "should", on course design for lifelong learning and careers', 'Read it for bachelor\'s and master\'s courses.', 'that it guarantees employment', 'the level 6 descriptor %s4.15.b9.3 and the theme record theme:enterprise' % FH),
  aad=aad('a team reviews employability or independent learning in its programme', STAFF, 'Where does the programme hand responsibility for learning to the student?', NOSTUDENT))
s('2.11', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='joint and combined degree undergraduates', addressee='learner',
  verbs=['achieve', 'add', 'explore'], about='core skills in a joint degree', domain='subject-skill', award=HON,
  para='Undergraduates taking Finance within a joint or combined degree will achieve the core of the specific and generic skills in the statement, add others from their other subject and may explore where the disciplines overlap.',
  prac='Make sure joint and combined students will achieve the core specific and generic skills, then add the other subject\'s skills and room for interdisciplinary work.',
  ben='If you study finance as part of a joint degree, you will gain its core subject and general skills, add skills from your other subject and can explore where the two meet.',
  aaw=aaw('2.11', 'an expected outcome, in "will", for joint and combined degree students', PLACE6, 'that joint students must meet every item a single honours student does', 'paragraph 1.4, item 2.3 and the threshold list 4.4.b1 to 4.4.b15'),
  aad=aad('a joint honours student asks how much finance they must master', STUDENT, 'Which core finance skills do you already use in your other subject?', 'presenting the full single honours list as their minimum'))
s('2.14', type='expectation', rung='none', force='should', level='fheq:7', appliesTo="full master's degrees", addressee='both',
  verbs=['comprise', 'work', 'include'], about="the master's project or dissertation and empirical work", domain='subject-skill', award=MA,
  para="A full master's usually carries 180 credits over one full-time year; after the taught part, students normally complete a self-directed project or dissertation that ideally should include empirical work, though applied projects or extra taught units may take its place.",
  prac="Plan the master's around about 180 credits with a self-directed project or dissertation that ideally should include empirical work; live briefs, internships or extra taught units are accepted variants.",
  ben="On a full master's you will usually finish with your own project or dissertation, ideally one that should include empirical work you carry out yourself.",
  aaw=aaw('2.14', 'an expectation, softened by "ideally should", that the master\'s dissertation includes empirical work', 'Place it at %s.' % L7, 'that a dissertation is compulsory, since the text accepts taught alternatives', 'the master\'s descriptor %s4.17.b2 and the FHEQ credit table in std:doc:qaa-fheq-2024-framework, S5' % FH),
  aad=aad("a master's student plans a dissertation or a team designs the project stage", 'With a student use the second person and plain words; with staff, name the accepted alternatives.', 'What data will your project use, and how will you collect or obtain it?', 'presenting empirical work as an absolute rule'))
s('2.17', type='expectation', rung='none', force='should', level='fheq:7', appliesTo="master's teaching", addressee='provider',
  verbs=['educated'], about="research as part of master's education", domain='none', award=MA,
  para="Master's students should be taught with research in mind as an important part of their study, since some will go on to further study.",
  prac="Treat research as a central part of master's teaching, since some students will continue to doctoral study.",
  ben=('n/a', 'a duty on how the course is taught'),
  aaw=aaw('2.17', 'an expectation, in "should", that master\'s teaching keeps research in view', 'Place it at %s.' % L7, 'that every master\'s student must do original research', 'item 2.14 and the master\'s descriptor %s4.17.b3' % FH),
  aad=aad("a team designs a master's curriculum", STAFF, 'Where do your master\'s students meet research methods before the dissertation?', NOSTUDENT))
s('2.20', type='expectation', rung='none', force='should', level='none', appliesTo='Finance degrees', addressee='provider',
  verbs=['offered', 'suit'], about='a variety of learning modes', domain='none', award='none',
  para='Courses support learning and are inclusive; Finance degrees should be offered in several modes with assessment that suits students\' needs, which may include on-campus, online, hybrid, block or part-time study and credit from micro-credentials or prior learning.',
  prac='Offer the degree in a variety of learning modes, with assessment suited to students\' needs, and consider credit routes such as micro-credentials and recognition of prior learning.',
  ben=('n/a', 'a duty on how the course is offered'),
  aaw=aaw('2.20', 'an expectation, in "should", on modes of study and assessment', 'It holds at every level.', 'that every mode listed must be offered', 'item 2.21 and paragraph 1.23'),
  aad=aad('a team considers part-time, online or block delivery', STAFF, 'Which students can your current mode of delivery not reach?', NOSTUDENT))
s('2.21', type='requirement', rung='none', force='must', level='none', appliesTo='flexible Finance degrees', addressee='provider',
  verbs=['ensure', 'meet', 'required'], about='flexibility kept coherent and on standard', domain='none', award='none',
  para='When flexibility is built into Finance degrees, it is essential that programmes stay coherent and meet the statement\'s standards; flexibility may be needed to meet EDI obligations, and partnerships can add more.',
  prac='However flexible the structure, keep the programme coherent and meeting this statement\'s standards; flexibility may also be how you meet EDI obligations.',
  ben=('n/a', 'a duty on course design'),
  aaw=aaw('2.21', 'a requirement read from "it is essential", that flexible programmes stay coherent and meet the statement', 'It holds at every level.', 'that the issuer used "must": the force is our reading (Part E)', 'item 2.20 and the threshold list 4.4.b1 to 4.4.b15'),
  aad=aad('a team adds flexible routes, credit transfer or micro-credentials', STAFF, 'Does a student on the most flexible route still meet every threshold item?', NOSTUDENT))
s('3.4', type='requirement', rung='none', force='will', level='none', appliesTo='higher education providers offering Finance', addressee='provider',
  verbs=['select', 'demonstrate', 'achieve'], about="the provider's choice of activities and showing they work", domain='none', award='none',
  para='Each provider is responsible for choosing teaching, learning and assessment suited to its degree\'s aims, and will be able to show how those activities let students reach the subject knowledge and skills and the generic skills in section 3.',
  prac='Choose your own mix of teaching, learning and assessment, and be ready to show how it enables students to reach the outcomes in 3.2 and 3.3.',
  ben=('n/a', 'a duty on the provider'),
  aaw=aaw('3.4', 'a provider responsibility, with the expectation in "will" that it can show its activities work', 'It holds at every level.', 'that the statement prescribes methods', 'the outcome lists 3.2.b1 to 3.2.b13 and 3.3.b1 to 3.3.b9'),
  aad=aad('a team prepares a programme specification or review', STAFF, 'For each outcome in 3.2 and 3.3, which activity lets students reach it?', NOSTUDENT))
s('3.7', type='requirement', rung='none', force='must', level='none', appliesTo='blended learning', addressee='provider',
  verbs=['maintain', 'needs'], about='blended learning and academic integrity', domain='none', award='none',
  para='Blended delivery mixing online and in-person work can be used and adds flexibility but can weaken engagement; learning and assessment supported by technology needs fresh approaches that also address integrity, and blended learning must maintain academic integrity.',
  prac='If you use blended learning, keep students engaged and make sure the approach maintains academic integrity, designing technology-supported assessment with integrity in mind.',
  ben=('n/a', 'a duty on course delivery'),
  aaw=aaw('3.7', 'a requirement, in "must", that blended learning maintains academic integrity', 'It holds at every level.', 'that blended learning is required', 'paragraphs 1.46 and 1.47 on AI and integrity'),
  aad=aad('a team moves teaching or assessment online', STAFF, 'How will you know the work submitted online is the student\'s own?', NOSTUDENT))
s('3.8', type='expectation', rung='none', force='should', level='none', appliesTo='programme directors and course leaders', addressee='provider',
  verbs=['consider'], about='support for language, mathematics, writing and study skills', domain='none', award=[HON, MA],
  para='Finance students at both levels often come from varied backgrounds; programme directors and course leaders should consider targeted help with subject language, mathematics where needed, academic writing and study and exam skills.',
  prac='Consider targeted support in subject-specific language, mathematics where relevant, academic writing and study and examination skills for a diverse cohort.',
  ben=('n/a', 'a duty on programme leaders; a student meets its effect as support'),
  aaw=aaw('3.8', 'an expectation, in "should", on programme leaders to consider academic support', 'It holds for bachelor\'s and master\'s taught programmes.', 'that a particular support service is required', 'item 1.24.b3 on the language of finance'),
  aad=aad('a team sees students struggling with maths, writing or finance terms', STAFF, 'Which support could you build into the modules rather than leave to a central service?', NOSTUDENT))
s('3.14', type='requirement', rung='none', force='must', level='none', appliesTo='teaching, learning and assessment activities', addressee='provider',
  verbs=['informed', 'undertaken', 'ensure'], about='regular review of activities', domain='none', award='none',
  para='Teaching and assessment design can draw on current pedagogical research and technology; regular reviews must be carried out so that the activities stay fit for purpose and current for the programme\'s outcomes.',
  prac='Review teaching, learning and assessment regularly so that it stays fit for purpose and current, drawing on pedagogical research and new technology.',
  ben=('n/a', 'a duty on the course'),
  aaw=aaw('3.14', 'a requirement, in "must", for regular review of activities', 'It holds at every level.', 'that it sets a review cycle', 'paragraphs 2.27 to 2.29 on monitoring, review and external examining'),
  aad=aad('a periodic review or module evaluation is due', STAFF, 'When did you last change an activity because evidence showed it was not working?', NOSTUDENT))
s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['refer', 'determining'], about='Annex D for evidence of achievement', domain='none', award=HON,
  para='Most students are likely to go well beyond the threshold; each provider sets how to evidence achievement and should consult Annex D of the Frameworks for more guidance.',
  prac='Decide what evidence shows achievement at each level and use Annex D, the degree classification descriptions, as your guide.',
  ben=('n/a', 'a duty on the provider in judging achievement'),
  aaw=aaw('4.2', 'an expectation, in "should", that providers refer to Annex D when judging evidence of achievement', PLACE6, 'that Annex D bands map one to one onto threshold, typical and excellent', 'the Annex D records %ssummary/r1/3rd to %ssummary/r1/1st and the rungs 4.4, 4.5 and 4.6' % (AD, AD)),
  aad=aad('a team writes marking criteria or classifies degrees', STAFF, 'How do your marking criteria use Annex D, and where do they part from it?', NOSTUDENT))
s('4.3', type='expectation', rung='none', force='should', level='none', appliesTo='providers developing competence standards', addressee='provider',
  verbs=['follow', 'informed'], about='competence standards and Equality Act guidance', domain='none', award='none',
  para='The three levels are not universal competence standards; a provider that sets competence standards under the Equality Act 2010 may draw on the statement and PSRB requirements, and should follow the latest guidance from the Equality and Human Rights Commission.',
  prac='Do not treat the threshold, typical and excellent levels as competence standards; if you write competence standards under the Equality Act 2010, follow the EHRC\'s latest guidance.',
  ben=('n/a', 'a duty on the provider'),
  aaw=aaw('4.3', 'an expectation, in "should", on providers that set competence standards', 'It holds at every level.', 'that the rungs are competence standards in the Equality Act\'s sense', 'the rungs 4.4 to 4.6 and SB5\'s record of the EHRC'),
  aad=aad('a team writes competence standards or handles a reasonable adjustment request', STAFF, 'Which of your requirements is a true competence standard, and which is only the usual way of assessing it?', NOSTUDENT))

# ---------------------------------------------------------------- 3.2 subject-specific knowledge and skills (lead-in: a student is generally expected to have)
def k32(i, about, domain, verbs, para, prac, ben, ask, fw, th):
    s('3.2.b%d' % i, type='outcome', rung='none', force='describes', level='fheq:6', appliesTo="bachelor's graduates of the subject",
      addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
      aaw=aaw('3.2', 'an outcome the statement generally expects of a bachelor\'s Finance graduate (%s), listed outside the rungs' % about, PLACE6,
              'that it is a threshold the award requires, or that its examples in brackets are a set syllabus', 'threshold item %s and the level 6 descriptor %s%s' % (th, FH, fw)),
      aad=aad('a student or team asks what a Finance graduate should know about %s' % about, STUDENT, ask,
              'reciting the examples and treating the item as a rung'))
k32(1, 'the contexts finance operates in', 'knowledge', ['appreciation', 'knowledge'],
    'A grasp of the settings finance works in, with knowledge of the institutional framework needed to understand how markets and institutions function, such as economic, ethical, legal, political, regulatory, social and tax settings.',
    'Graduates are generally expected to know the economic, legal, regulatory, social and tax settings of finance and the institutional framework of markets and firms.',
    'You are expected to understand the settings finance works in, from law and regulation to tax, and how they shape markets and institutions.',
    'Which rule or institution most shapes the market you know best?', '4.15.b1', '4.4.b3')
k32(2, 'major theories and tools of finance', 'knowledge', ['knowledge', 'relevance', 'application'],
    'Knowledge of finance\'s main theoretical tools and theories and how they bear on theoretical and practical problems, for example arbitrage, portfolio theory, asset pricing, cost of capital, derivatives, behavioural finance and climate finance.',
    'Graduates are generally expected to know the main theories and tools of finance and how to apply them to theoretical and practical problems.',
    'You are expected to know the main theories and tools of finance, such as portfolio theory and asset pricing, and how to use them on real problems.',
    'Pick one theory you have studied: what real problem does it help you solve?', '4.15.b1', '4.4.b1')
k32(3, 'theory and empirical testing', 'understanding', ['understanding', 'appraisal', 'recognition'],
    'An understanding of how finance theory relates to empirical testing, used to appraise the evidence in at least one major area, recognising how tests and theory are limited and change over time.',
    'Graduates are generally expected to relate finance theory to empirical tests and to appraise the evidence in at least one major area, aware of its limits.',
    'You are expected to understand how finance theories are tested against data, and to weigh up the evidence in at least one area while seeing its limits.',
    'In one area, what does the evidence support, and where does it fall short?', '4.15.b4', '4.4.b9')
k32(4, 'interpreting financial data', 'subject-skill', ['interpret', 'manipulate', 'conduct'],
    'An ability to interpret financial data from firms, households, national sources and markets, analysing it with statistical tools in spreadsheets or econometric software, possibly running statistical and econometric tests, and critiquing results and their assumptions.',
    'Graduates are generally expected to interpret and analyse financial data with spreadsheets and statistical software, and to critique the results and their assumptions.',
    'You are expected to read and analyse financial data with spreadsheets or statistical software, and to question your results and the assumptions behind them.',
    'What assumption behind your last analysis would most change the result if it were wrong?', '4.15.b2', '4.4.b8')
k32(5, 'financing arrangements and governance', 'understanding', ['understanding', 'appreciation', 'assess'],
    'An understanding of how firms and other organisations are financed and governed, and how theory and evidence together can judge whether those arrangements are effective and efficient.',
    'Graduates are generally expected to understand financing and governance structures and to judge their effectiveness using theory and evidence.',
    'You are expected to understand how organisations raise money and are governed, and to judge how well those arrangements work.',
    'How would you judge whether a firm\'s capital structure serves it well?', '4.15.b1', '4.4.b4')
k32(6, 'personal financial management and investment', 'understanding', ['understanding'],
    'An understanding of what shapes how individuals manage money and invest, and the opportunities open to them, such as risk attitudes, portfolio choice, pensions, tax on savings and currency risk.',
    'Graduates are generally expected to understand what drives the financial and investment behaviour of individuals and their options.',
    'You are expected to understand what shapes how people save, invest and manage money, from risk attitudes to pensions and tax.',
    'What would you tell a friend about the trade-off between risk and return in their savings?', '4.15.b1', '4.4.b6')
k32(7, 'financial services in the economy', 'understanding', ['understanding', 'appreciation', 'employed'],
    'An understanding of financial service activity in the economy and what changes it, and of how theory and evidence, such as information asymmetry or market efficiency, help explain it.',
    'Graduates are generally expected to understand financial services and their change over time, using theory and evidence to explain them.',
    'You are expected to understand how financial services such as banking, insurance and pensions work and change, and how theory helps explain them.',
    'Which idea, such as moral hazard, best explains a problem in a financial service you use?', '4.15.b1', '4.4.b5')
k32(8, 'financial statements and reporting limits', 'subject-skill', ['understand', 'appreciation'],
    'Able to read financial statements, with a fair awareness of where financial reporting and disclosure fall short, for example accrual versus cash accounting and discretionary practices.',
    'Graduates are generally expected to read financial statements and to recognise the limits of reporting and disclosure.',
    'You are expected to read financial statements and see where reporting and disclosure can mislead or leave gaps.',
    'What can a set of accounts not tell you about a company?', '4.15.b2', '4.4.b7')
k32(9, 'regulation in the finance sector', 'understanding', ['understanding'],
    'An understanding of how regulation in finance is organised, why it exists, what it asks of firms and markets, how it differs across industries and economies, and what it means for practitioners\' professionalism.',
    'Graduates are generally expected to understand the reasons for, reach and effect of financial regulation and its implications for professional practice.',
    'You are expected to understand why finance is regulated, what rules firms and markets face and what that means for how you work as a professional.',
    'Why does this part of finance need regulating, and what would happen without it?', '4.15.b1', '4.4.b5')
k32(10, 'technology, AI and GenAI in finance', 'subject-skill', ['assess'],
    'An ability to judge how technologies, including digital tools, AI and GenAI, make new ways of delivering financial services possible and affect markets and investment, in areas such as payments, lending, fraud detection and compliance.',
    'Graduates are generally expected to assess the role of digital technology, AI and GenAI in financial services, markets and investment.',
    'You are expected to judge how digital technology, AI and generative AI are changing financial services, markets and investment.',
    'Where has AI improved a financial service, and where has it added a new risk?', '4.15.b7', '4.4.b12')
k32(11, 'personal finance and financial literacy', 'understanding', ['understand', 'identify', 'appreciate'],
    'An ability to understand personal finance and see how financial literacy and capability are built, and to value widening access to finance through mainstream and alternative channels.',
    'Graduates are generally expected to understand personal finance and financial capability and to value wider access to finance.',
    'You are expected to understand personal finance, how people become financially capable, and why wider access to finance matters.',
    'Who lacks access to mainstream finance in your area, and what fills the gap?', '4.15.b1', '4.4.b2')
k32(12, 'finance and climate and environmental risk', 'understanding', ['understand'],
    'An ability to understand what the finance sector does about climate change and other environmental risks, and how green and climate finance, nature and biodiversity finance and sustainable products have grown.',
    'Graduates are generally expected to understand finance\'s role in climate and environmental risk and the growth of green and sustainable finance.',
    'You are expected to understand how finance responds to climate change and environmental risk, and how green and sustainable finance products work.',
    'How would climate risk change the value of an asset you have studied?', '4.15.b1', '4.4.b11')
k32(13, 'programming, data and research methods', 'subject-skill', ['use', 'select', 'analyse'],
    'Knowledge of the programming, data visualisation, AI and computing skills the profession needs, the ability to apply them to real data in statistical or econometric software, and a grasp of quantitative and qualitative data with the choice of fitting research methods.',
    'Graduates are generally expected to use programming, visualisation and AI tools on real data and to choose suitable quantitative or qualitative methods.',
    'You are expected to use programming, data visualisation and AI tools on real data, and to choose the right research methods for the data you have.',
    'Which tool or language would you choose for this data, and why?', '4.15.b2', '4.4.b8')

# ---------------------------------------------------------------- 3.3 cognitive abilities and generic skills (same lead-in)
def k33(i, about, verbs, para, prac, ben, ask, fw, th):
    s('3.3.b%d' % i, type='outcome', rung='none', force='describes', level='fheq:6', appliesTo="bachelor's graduates of the subject",
      addressee='learner', verbs=verbs, about=about, domain='generic-skill', award=HON, para=para, prac=prac, ben=ben,
      aaw=aaw('3.3', 'a generic skill the statement generally expects of a bachelor\'s Finance graduate (%s), listed outside the rungs' % about, PLACE6 + ' As a generic skill, it refines that level.',
              'that it is a threshold the award requires or that it is particular to finance', 'threshold item %s and the level 6 descriptor %s%s' % (th, FH, fw)),
      aad=aad('a student reflects on transferable skills or prepares for a job application', STUDENT, ask,
              'treating the skill as a rung and reading the list aloud'))
k33(1, 'critical evaluation', ['evaluation'],
    'Weighing arguments and evidence critically.', 'Graduates are generally expected to evaluate arguments and evidence critically.',
    'You are expected to weigh up arguments and evidence critically.', 'What is the weakest point in the argument you found most convincing?', '4.15.b7', '4.4.b15')
k33(2, 'independent learning', ['learning'],
    'Learning on one\'s own initiative and managing one\'s own study.', 'Graduates are generally expected to learn independently and manage their own learning.',
    'You are expected to learn on your own initiative and manage your own study.', 'What have you learned recently that no one set for you?', '4.15.b5', '4.4.b15')
k33(3, 'analysing data and drawing conclusions', ['analysis', 'drawing'],
    'Analysing, filtering and judging data, and drawing reasoned conclusions about structured and, to a lesser degree, unstructured problems from given data or data the student gathers.',
    'Graduates are generally expected to analyse and filter data and reach reasoned conclusions on structured and some unstructured problems.',
    'You are expected to analyse and sift data, whether given or gathered yourself, and reach reasoned conclusions, mostly on well-defined problems.',
    'How did you decide which data to leave out of your analysis?', '4.15.b7', '4.4.b7')
k33(4, 'finding and managing data from many sources', ['location', 'extraction', 'management'],
    'Locating, extracting, managing and analysing data from several sources, acknowledging and referencing them.',
    'Graduates are generally expected to locate, extract, manage and analyse data from several sources, with proper referencing.',
    'You are expected to find, extract and manage data from different sources and reference them properly.', 'Where did your data come from, and how would someone else find it?', '4.15.b5', '4.4.b7')
k33(5, 'numeracy', ['processing', 'analysis', 'appreciation'],
    'Numeracy, including handling and analysing financial and other numbers and grasping statistical and econometric ideas at a suitable level.',
    'Graduates are generally expected to be numerate, processing financial data and grasping statistical and econometric concepts.',
    'You are expected to be confident with numbers, analysing financial data and understanding the statistics behind it.', 'Which statistical idea do you use most, and could you explain it to a non-specialist?', '4.15.b2', '4.4.b8')
k33(6, 'research tools for policy', ['selection', 'application', 'design'],
    'Choosing and using research tools to design, steer and interpret financial, social and environmental policy.',
    'Graduates are generally expected to select and apply research tools to design and interpret financial, social and environmental policies.',
    'You are expected to choose and use research tools to shape and interpret policies in finance, society and the environment.', 'Which research tool would show whether a policy is working?', '4.15.b6', '4.4.b10')
k33(7, 'technology for financial information', ['using'],
    'Using technology to gather, analyse and communicate financial information.',
    'Graduates are generally expected to use technology to acquire, analyse and communicate financial information.',
    'You are expected to use technology to gather, analyse and share financial information.', 'Which software do you rely on most, and what does it not do well?', '4.15.b2', '4.4.b8')
k33(8, 'communication to an audience', ['communication', 'presenting'],
    'Communicating quantitative and qualitative information with analysis and argument in a form suited to the audience, spoken, non-verbal and written.',
    'Graduates are generally expected to communicate numerical and qualitative analysis and argument in forms that suit the audience.',
    'You are expected to present numbers and ideas, with your analysis and argument, in a way that suits your audience, in speech and in writing.', 'Who was the audience for your last presentation, and what did you change for them?', '4.15.b8', '4.4.b13')
k33(9, 'working with others', ['working'],
    'Working with others, for instance in group projects.', 'Graduates are generally expected to work well with others, for example in group projects.',
    'You are expected to work well with others, for example on group projects.', 'What did you contribute to your last group project, and what would you do differently?', '4.15.b9.1', '4.4.b14')

# ---------------------------------------------------------------- 4.4 threshold (lead-in: a student graduating with a Finance bachelor's degree will be able to)
def kt(i, about, domain, verbs, para, prac, ben, ask, fw, ad):
    s('4.4.b%d' % i, type='threshold', rung='threshold', force='threshold', forceFrom='4.1', level='fheq:6', appliesTo="graduates at the threshold level",
      addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
      aaw=aaw('4.4', 'a threshold outcome, the minimum the bachelor\'s degree with honours in Finance requires (%s)' % about, PLACE6,
              'that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master\'s', 'the typical and excellent levels 4.5 and 4.6, the level 6 descriptor %s%s and Annex D\'s third-class cell %s%s' % (FH, fw, AD, ad)),
      aad=aad('a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes', STUDENT + ' Make clear this is the minimum.', ask,
              'reading the list aloud and implying that the threshold is what most students reach'))
kt(1, 'depth of knowledge of core concepts', 'knowledge', ['demonstrate'],
   'Will show a depth of knowledge of finance\'s main concepts, theories and tools.', 'At threshold, graduates will show deep knowledge of finance\'s main concepts, theories and tools.',
   'To pass, you will show solid knowledge of the main ideas, theories and tools of finance.', 'Which core idea in finance could you explain without notes?', '4.15.b1', 'knowledge/r1/3rd')
kt(2, 'applying knowledge to finance problems', 'subject-skill', ['apply'],
   'Will apply what they know to finance problems that matter to people, firms, institutions and society.', 'At threshold, graduates will apply their knowledge to finance problems facing individuals, companies, institutions and society.',
   'To pass, you will use what you know to tackle finance problems for people, firms, institutions and society.', 'What finance problem have you solved where the answer mattered to someone?', '4.15.b3.1', 'cognitive/r3/3rd')
kt(3, 'the environments finance operates in', 'understanding', ['demonstrate'],
   'Will show they understand the settings of finance: institutional, economic, political, regulatory and social.', 'At threshold, graduates will understand the institutional, economic, political, regulatory and social environments of finance.',
   'To pass, you will understand the institutions, economics, politics, regulation and society that finance works within.', 'How does regulation change what a bank can do?', '4.15.b1', 'knowledge/r2/3rd')
kt(4, 'governance and ethics in decisions', 'understanding', ['recognise'],
   'Will recognise how much sound governance and ethics matter in financial decisions.', 'At threshold, graduates will recognise that reliable governance and ethical considerations are fundamental to financial decisions.',
   'To pass, you will recognise why good governance and ethics matter in financial decisions.', 'When would you refuse a profitable decision on ethical grounds?', '4.15.b7', 'knowledge/r2/3rd')
kt(5, 'markets, their regulation and products', 'understanding', ['understand'],
   'Will understand how financial markets work and are regulated and supervised, with some of what they trade.', 'At threshold, graduates will understand how financial markets operate and are regulated and supervised, with some of their products.',
   'To pass, you will understand how financial markets work and are regulated, and some of the products traded in them.', 'Who supervises the market you know best, and what do they watch for?', '4.15.b1', 'knowledge/r1/3rd')
kt(6, 'valuation, securities and portfolios', 'understanding', ['understand'],
   'Will understand the basics of valuing assets, analysing securities and managing portfolios.', 'At threshold, graduates will understand the basics of valuation, security analysis and portfolio management.',
   'To pass, you will understand the basics of valuing assets, analysing securities and managing a portfolio.', 'How would you put a value on a share you have never seen before?', '4.15.b2', 'knowledge/r2/3rd')
kt(7, 'handling financial and economic data', 'subject-skill', ['collect', 'manage', 'synthesise', 'interpret'],
   'Will gather, organise, combine and make sense of financial, accounting and economic data.', 'At threshold, graduates will collect, manage, combine and interpret financial, accounting and economic data.',
   'To pass, you will gather, organise, combine and make sense of financial, accounting and economic data.', 'Where would you find the data for this question, and how would you check it?', '4.15.b2', 'practical/r4/3rd')
kt(8, 'straightforward statistical analysis with software', 'subject-skill', ['execute'],
   'Will carry out simple statistical analyses of financial data in software.', 'At threshold, graduates will execute straightforward statistical analyses of financial data with software packages.',
   'To pass, you will run simple statistical analyses of financial data using software.', 'Which analysis would you run first on this data set, and in which package?', '4.15.b2', 'practical/r2/3rd')
kt(9, 'limits of theory and evidence', 'subject-skill', ['assess'],
   'Will judge the importance, problems and limits of finance theories and the evidence behind them.', 'At threshold, graduates will assess how far finance theories and their evidence matter, and their problems and limits.',
   'To pass, you will judge how far finance theories and their evidence hold up, and where they fall short.', 'Which theory you studied does the evidence support least well?', '4.15.b4', 'cognitive/r1/3rd')
kt(10, 'theory and evidence guiding policy and practice', 'understanding', ['demonstrate', 'guide'],
   'Will show a critical understanding of how theory and evidence in finance can inform policy and practice.', 'At threshold, graduates will critically appreciate how finance theory and empirical evidence can guide policy and practice.',
   'To pass, you will show you understand, critically, how finance theory and evidence can shape policy and practice.', 'Name a policy that finance research changed, and say whether it should have.', '4.15.b3.2', 'cognitive/r2/3rd')
kt(11, 'finance as a lever for sustainable outcomes', 'understanding', ['understand', 'achieve'],
   'Will understand why finance is a key means of reaching sustainable outcomes for society and the planet.', 'At threshold, graduates will understand finance as a key lever for sustainable outcomes for society and the planet.',
   'To pass, you will understand how finance can drive sustainable outcomes for people and the planet.', 'Where could finance do most to cut emissions or protect nature?', '4.15.b1', 'knowledge/r2/3rd')
kt(12, 'the effect of fintech on financial services', 'understanding', ['understand', 'exerts'],
   'Will understand how fintech changes financial services through AI, blockchain and digital payments.', 'At threshold, graduates will understand the impact of fintech innovations such as AI, blockchain and digital payments on financial services.',
   'To pass, you will understand how fintech, such as AI, blockchain and digital payments, is changing financial services.', 'Which fintech innovation has most changed how you use money?', '4.15.b1', 'knowledge/r1/3rd')
kt(13, 'summarising and communicating to varied audiences', 'generic-skill', ['distil', 'summarise', 'communicating'],
   'Will condense financial knowledge and information and convey it well, orally and in writing, to varied audiences.', 'At threshold, graduates will distil financial information and communicate it effectively, spoken and written, to diverse audiences.',
   'To pass, you will boil down financial information and explain it well, in speech and writing, to different audiences.', 'How would you explain this result to a client with no finance background?', '4.15.b8', 'transferable/r1/3rd')
kt(14, 'collaboration and leadership in teams', 'generic-skill', ['demonstrate', 'working'],
   'Will show they can collaborate and lead by working well in finance and cross-disciplinary teams.', 'At threshold, graduates will show collaborative and leadership skills in finance and interdisciplinary teams.',
   'To pass, you will show you can work with others and lead, in finance teams and mixed-discipline teams.', 'When did you last take the lead in a team, and what happened?', '4.15.b9.1', 'transferable/r2/3rd')
kt(15, 'intellectual independence and critical judgement', 'generic-skill', ['assert'],
   'Will show independent thought and critical judgement.', 'At threshold, graduates will assert intellectual independence and critical judgement.',
   'To pass, you will think for yourself and judge critically.', 'Where in your work did you reach a view that differed from your sources?', '4.15.b7', 'transferable/r3/3rd')

# ---------------------------------------------------------------- 4.5 typical and 4.6 excellent: prose paragraphs, cut by sentence (Part E)
def kr(rung, k, about, domain, verbs, para, prac, ben, ask, beside):
    n = '4.5' if rung == 'typical' else '4.6'
    word = 'a typical-level expectation, in "will", above the threshold' if rung == 'typical' else 'an excellent-level expectation, in "will", the highest level the statement describes'
    s('%s.s%d' % (n, k), type=rung, rung=rung, force='will', level='fheq:6', appliesTo='graduates at the %s level' % rung,
      addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
      aaw=aaw(n, '%s (%s)' % (word, about), PLACE6, 'that it is the minimum for the award, or that %s' % ('it equals an upper second' if rung == 'typical' else 'it equals a first or a master\'s standard'), beside),
      aad=aad('a student asks how to move beyond a pass, or a team sets criteria above the threshold', STUDENT + ' Say it describes a higher level, not what is needed to pass.', ask,
              'presenting this as the minimum and reading the paragraph aloud'))
kr('typical', 1, 'breadth, depth and critical insight', 'knowledge', ['distinguish', 'demonstrating', 'showing'],
   'Graduates at the typical level stand out from those at threshold by the breadth and depth of what they know and understand and by clear, critical insight into finance.',
   'At the typical level, graduates show breadth and depth of knowledge and a clear, critical insight into the discipline, beyond the threshold.',
   'To go beyond a pass, you will show broad and deep knowledge and a clear, critical view of finance as a discipline.',
   'What do you understand about finance now that you could not have argued in your first year?',
   'the threshold list 4.4, Annex D\'s upper-second cell %sknowledge/r1/2.1 for reading only, and %s4.15.b1' % (AD, FH))
kr('typical', 2, 'rigorous theory and some specialised topics', 'knowledge', ['demonstrate'],
   'Will show a rigorous grasp of the theories, paradigms, methods, concepts and principles of finance, and a strong grasp of some specialised topics.',
   'At the typical level, graduates will show rigorous understanding of finance theory and method and strong understanding of some specialist topics.',
   'To go beyond a pass, you will show a rigorous grasp of finance theory and method and know some specialist topics well.',
   'Which specialist topic do you know well enough to teach a classmate?',
   'threshold item 4.4.b1, excellent 4.6.s2 and %sknowledge/r2/2.1' % AD)
kr('typical', 3, 'critical appraisal of sources and their limits', 'subject-skill', ['possess', 'select', 'appraise', 'recognise'],
   'Will have a sophisticated ability to choose many kinds of information, sources, views and knowledge and appraise them critically, specialised or interdisciplinary, recognising their uncertainty, ambiguity and limits.',
   'At the typical level, graduates will select and critically appraise a wide range of sources, specialist or interdisciplinary, and recognise their uncertainty and limits.',
   'To go beyond a pass, you will choose and critically weigh many kinds of sources and views, and see where they are uncertain or limited.',
   'Which of your sources disagree, and how did you decide between them?',
   'threshold item 4.4.b9, excellent 4.6.s4, %s4.15.b4 and %scognitive/r1/2.1' % (FH, AD))
kr('typical', 4, 'investigation and solving complex problems', 'subject-skill', ['conduct', 'solve', 'applying'],
   'With some autonomy, will carry out thorough investigation, reading, analysis and research and solve complex finance problems, using a wide range of established methods accurately.',
   'At the typical level, graduates will investigate thoroughly with some autonomy and solve complex finance problems with established methods, accurately.',
   'To go beyond a pass, you will research thoroughly with some independence and solve complex finance problems using a wide range of methods accurately.',
   'Which complex problem did you solve mostly on your own, and which method did you choose?',
   'threshold item 4.4.b2, excellent 4.6.s3 and 4.6.s5, %s4.15.b6 and %scognitive/r3/2.1' % (FH, AD))
kr('typical', 5, 'synthesis, argument and originality in communication', 'generic-skill', ['select', 'evaluate', 'synthesize', 'communicate', 'present', 'demonstrate'],
   'Will select, evaluate, synthesise, discuss and present information and results with well-supported arguments, interpreting complex ideas thoroughly and showing a high degree of creativity and originality.',
   'At the typical level, graduates will synthesise and present information and results with supported arguments, interpret complex ideas thoroughly and show creativity and originality.',
   'To go beyond a pass, you will pull information together, argue from evidence, explain complex ideas carefully and show creativity and original thought in your work.',
   'Where in your recent work did you make an argument nobody gave you?',
   'threshold item 4.4.b13, excellent 4.6.s6 and 4.6.s7, %s4.15.b8 and %scognitive/r4/2.1' % (FH, AD))
kr('excellent', 1, 'exceptional knowledge beyond the taught', 'knowledge', ['distinguish', 'showing'],
   'Graduates at the excellent level stand out from those at threshold and typical levels by exceptional knowledge and understanding of finance, well past the typical and past what was taught.',
   'At the excellent level, graduates show exceptional knowledge and understanding of finance, well beyond the typical level and beyond what was taught.',
   'At the highest level, you will show exceptional knowledge and understanding of finance, going well past what you were taught.',
   'What have you read or worked out that goes beyond your course?',
   'typical 4.5.s1, %sknowledge/r1/1st for reading only, and the master\'s descriptor %s4.17.b1' % (AD, FH))
kr('excellent', 2, 'exceptional theory and in-depth specialist knowledge', 'knowledge', ['demonstrate', 'have'],
   'Will show exceptional command of the theories, paradigms, methods, concepts and principles of finance and deep knowledge of several specialised areas.',
   'At the excellent level, graduates will show exceptional command of finance theory and method and in-depth knowledge of several specialist areas.',
   'At the highest level, you will show exceptional command of finance theory and method and know several specialist areas in depth.',
   'In which specialist areas could you hold your own with a practitioner?',
   'typical 4.5.s2, %sknowledge/r2/1st and %s4.15.b1' % (AD, FH))
kr('excellent', 3, 'independent, extensive investigation', 'subject-skill', ['assert', 'conduct'],
   'Will think independently and carry out thorough, extensive investigation, reading, analysis and research well past the typical range.',
   'At the excellent level, graduates will work with intellectual independence and investigate thoroughly and extensively, well beyond the typical range.',
   'At the highest level, you will think independently and research thoroughly and widely, well beyond what most students do.',
   'What question did you pursue further than the assignment asked?',
   'typical 4.5.s4, threshold item 4.4.b15 and %sknowledge/r3/1st' % AD)
kr('excellent', 4, 'exceptional critical appraisal', 'subject-skill', ['possess', 'appraise', 'appreciate'],
   'Will have an exceptional ability to appraise many sources, views and knowledge critically and a masterly sense of their uncertainty, ambiguity and limits.',
   'At the excellent level, graduates will critically appraise a wide range of sources with exceptional skill and show a masterly grasp of their uncertainty and limits.',
   'At the highest level, you will weigh up a wide range of sources with exceptional skill and show a masterly sense of what they cannot tell you.',
   'Where does the evidence you rely on most stop being trustworthy?',
   'typical 4.5.s3, %scognitive/r1/1st and %s4.15.b4' % (AD, FH))
kr('excellent', 5, 'exceptional problem-solving and decisions', 'subject-skill', ['show', 'solving', 'justifying', 'evidencing'],
   'Will show exceptional problem-solving and strong decision-making on complex finance problems, working largely autonomously, justifying and evidencing the critical and accurate use of a wide range of established methods.',
   'At the excellent level, graduates will solve complex finance problems exceptionally well and largely autonomously, justifying their choice and use of methods critically and accurately.',
   'At the highest level, you will solve complex finance problems exceptionally well and largely on your own, and justify the methods you chose.',
   'Why did you choose that method over the alternatives, and what would change your mind?',
   'typical 4.5.s4, threshold item 4.4.b2, %scognitive/r3/1st and the master\'s descriptor %s4.17.b5' % (AD, FH))
kr('excellent', 6, 'proficient synthesis and presentation', 'generic-skill', ['select', 'evaluate', 'synthesize', 'communicate', 'present'],
   'Will proficiently select, evaluate, synthesise, discuss and present views, information and results.',
   'At the excellent level, graduates will proficiently select, evaluate, synthesise and present views, information and results.',
   'At the highest level, you will select, weigh, combine and present views, information and results with real skill.',
   'How did you decide what to leave out of your presentation?',
   'typical 4.5.s5, threshold item 4.4.b13 and %stransferable/r1/1st' % AD)
kr('excellent', 7, 'substantiated argument, insight and originality', 'generic-skill', ['construct', 'present', 'demonstrate'],
   'Will build and present well-supported arguments and show sophisticated perception, critical insight into complex matters and exceptional creativity, flair and originality.',
   'At the excellent level, graduates will build supported arguments with sophisticated insight into complex matters and show exceptional creativity and originality.',
   'At the highest level, you will build strong, evidenced arguments, see deeply into complex matters and show exceptional creativity and originality.',
   'What is the most original point in your recent work, and how did you support it?',
   'typical 4.5.s5, %scognitive/r4/1st and %scognitive/r2/1st' % (AD, AD))

# gradeOf: same outcome one rung below, inferred (the issuer pairs nothing; typical and excellent are prose)
GRADE = {'4.5.s2': '4.4.b1', '4.5.s3': '4.4.b9', '4.5.s4': '4.4.b2', '4.5.s5': '4.4.b13',
         '4.6.s1': '4.5.s1', '4.6.s2': '4.5.s2', '4.6.s3': '4.5.s4', '4.6.s4': '4.5.s3',
         '4.6.s5': '4.5.s4', '4.6.s6': '4.5.s5', '4.6.s7': '4.5.s5'}

TH = {'1.18': 'theme:edi', '1.22': 'theme:edi', '1.23': 'theme:edi', '1.24.b1': 'theme:edi', '1.24.b2': 'theme:edi',
      '1.24.b3': 'theme:edi', '1.24.b7': 'theme:edi', '1.27': 'theme:edi',
      '1.28': 'theme:accessibility', '1.29.b4': 'theme:accessibility', '1.29.b5': 'theme:accessibility',
      '1.29.b7': 'theme:accessibility', '1.29.b8': 'theme:accessibility', '1.29.b9': 'theme:accessibility', '1.29.b10': 'theme:accessibility',
      '1.33': 'theme:esd', '1.34': 'theme:esd', '1.41': 'theme:enterprise'}

S5 = dict(levels=[
    dict(id='fheq:4', role='cites', locator='D1, 2.12'), dict(id='fheq:5', role='cites', locator='D1, 2.12'),
    dict(id='fheq:6', role='cites', locator='D1, 2.9'), dict(id='fheq:7', role='cites', locator='D1, 2.9; 2.14; 2.15; 2.16'),
    dict(id='fqheis:8', role='cites', locator='D1, 2.12'), dict(id='fqheis:9', role='cites', locator='D1, 2.12'),
    dict(id='fqheis:10', role='cites', locator='D1, 2.9'), dict(id='fqheis:11', role='cites', locator='D1, 2.9; 2.14; 2.16'),
    dict(id='spine:6', role='inferred', locator="the bachelor's rungs, by std:ref:uk-framework R2"),
    dict(id='spine:7', role='inferred', locator="master's awards, by std:ref:uk-framework R2")],
  crosswalks=[
    dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis="stated (D1, 2.9: bachelor's degree with honours); agrees with std:doc:qaa-fheq-2024-framework Table 1"),
    dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.9; 2.14; 2.16: integrated and full master's); agrees with Table 1"),
    dict(**{'from': 'fheq:4'}, to='fqheis:8', relation='equivalent', basis='stated (D1, 2.12: CertHE); conflicts with Table 1, which places CertHE at FQHEIS 7 (Part E)'),
    dict(**{'from': 'fheq:5'}, to='fqheis:9', relation='equivalent', basis='stated (D1, 2.12: DipHE); conflicts with Table 1, which places DipHE at FQHEIS 8 (Part E)')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.13', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '2.21', '2.30', '3.2']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.28', '1.29']),
      dict(id='theme:esd', role='carries', carriedIn=['1.13', '1.21', '1.30', '1.31', '1.32', '1.33', '1.34', '1.35', '1.36', '1.41', '2.2', '3.2', '4.4']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.37', '1.38', '1.40', '1.41', '1.42', '2.4']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['1.43', '1.44', '1.45', '1.46', '1.47', '3.2'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-finance-2019-benchmarks (not yet ingested)', note='the text names "the previous Subject Benchmark Statement" without a date; 2019 (minor update) is the latest earlier advisory group in the back matter (Part E)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='evidence of achievement against the rungs (4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 4 to 7 and master\'s credit (2.9, 2.12, 2.14 to 2.16)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 8 to 11 (2.9, 2.12, 2.14, 2.16)'),
      dict(rel='readWith', target='std:doc:qaa-accounting-2025-benchmarks', note='joint degrees and single honours accounting (1.4, 1.5)'),
      dict(rel='readWith', target='std:doc:qaa-economics-2023-benchmarks', note='joint degrees and single honours economics (1.4, 1.5)'),
      dict(rel='themeReference', target='std:doc:qaa-advancehe-esd-2021-guidance', note='the ESD guidance\'s learning outcomes (1.34)'),
      dict(rel='themeReference', target='std:doc:qaa-enterprise-2018-guidance', note='QAA\'s enterprise and entrepreneurship guidance (1.37; edition inferred, Part E)'),
      dict(rel='refersTo', target="QAA Characteristics Statements: Master's Degree; Micro-credentials (not yet ingested)", note='2.14; 2.26'),
      dict(rel='refersTo', target='QAA, Unpacking your Hidden Curriculum: Guide for Educators (2022; not yet ingested)', note='1.24'),
      dict(rel='refersTo', target='PSRB requirements (not yet ingested)', note='2.24, 2.26, 2.28, 4.3; bodies in SB5')]

SB1 = [
  'Finance studies national and international financial markets and how they interact with households, firms, the third sector, institutions and governments; it is global, central to decisions and always changing (D1, 1.2).',
  'It joins conceptual study, the theory, with applied study, empirical methods and theory in practice, and keeps both in balance, also in joint degrees (D1, 1.1, 1.4, 2.2).',
  'Two core domains: markets, banks and institutions; and investment, value, corporate finance, securities, risk and international financial management, with newer areas such as sustainable finance, fintech and AI (D1, 1.6, 1.7).',
  'It is approached from behavioural, ethical, economic, sustainable and statistical or mathematical angles, with the ethical and social side always present (D1, 1.8, 2.2).',
  'It draws on accounting and economics but needs only a reasonable knowledge of accounting (D1, 1.5, 2.3).',
  'It is data driven: statistical and econometric work, programming and AI tools are part of the degree (D1, 1.39, 3.2, 3.13).',
  'Professional bodies give advanced standing and accreditation, especially for specialist master\'s courses (D1, 2.24 to 2.26).',
]
SB2 = [
  dict(theme='theme:edi', inThisSubject='finance itself carries inequality: access to finance, discrimination in credit, pay gaps and a sector short of diversity are topics to study, alongside an inclusive learning environment, inclusive assessment and attention to the language of finance (D1, 1.18 to 1.27)',
       statements=['1.18', '1.22', '1.23', '1.24.b1', '1.24.b2', '1.24.b3', '1.24.b7', '1.27']),
  dict(theme='theme:accessibility', inThisSubject='accessible data terminals, trading simulations and software, equal access to placements and proactive design for neurodivergent students (D1, 1.28, 1.29)',
       statements=['1.28', '1.29.b4', '1.29.b5', '1.29.b7', '1.29.b8', '1.29.b9', '1.29.b10']),
  dict(theme='theme:esd', inThisSubject='sustainable finance defined through ESG factors; climate, nature and biodiversity finance, ESG disclosure and the SDGs; finance as a lever for sustainable outcomes, also at threshold (D1, 1.30 to 1.36; 4.4)',
       statements=['1.33', '1.34', '1.41', '2.2', '3.2.b12', '4.4.b11']),
  dict(theme='theme:enterprise', inThisSubject='employability through trading simulations, investment competitions, placements, guest practitioners and incubators; transferable skills sought by the finance sector (D1, 1.37 to 1.42)',
       statements=['1.41', '2.4']),
  dict(theme='theme:generative-ai', inThisSubject='AI and GenAI as subject matter (payments, lending, fraud detection, algorithmic trading), as tools students learn to use and critique, and as a matter for assessment design and integrity (D1, 1.43 to 1.47; 3.2)',
       statements=['3.2.b10', '4.4.b12']),
]
SB3 = dict(
  areas=[dict(component='1.2', gloss='traditional areas (banking, corporate, personal, public finance, investment, risk) and emerging ones (climate, green, biodiversity finance, fintech, AI)'),
         dict(component='1.7', gloss='the two core domains and contemporary areas; the knowledge outcomes are in 3.2'),
         dict(component='2.1', gloss='global capital, commodity, currency, fixed income and derivatives markets and the institutions in them'),
         dict(component='2.3', gloss='a reasonable knowledge of accounting')],
  practices=[dict(component='3.5', kind='teaching', gloss='what shapes the design of activities: balance of theory and application, research, the student body, mode'),
             dict(component='3.6', kind='learning', gloss='active learning: lectures, seminars, workshops, peer and project-based learning, trading simulations, placements'),
             dict(component='3.7', kind='teaching', gloss='blended delivery with academic integrity'),
             dict(component='3.8', kind='learning', gloss='support in subject language, maths, writing and study skills'),
             dict(component='3.9', kind='assessment', gloss='a balanced mix testing concept, application and generic skills'),
             dict(component='3.10', kind='assessment', gloss='formative and summative balance; feedback and feed forward'),
             dict(component='3.12', kind='assessment', gloss='authentic assessment for problem-solving and reasoning'),
             dict(component='3.13', kind='assessment', gloss='closed and open book exams, projects, essays, group and data-oriented tasks')])
SB4 = dict(
  rungs=[dict(rung='threshold', leadIn='4.4', award=HON, items=15),
         dict(rung='typical', leadIn='4.5', award=HON, items=5),
         dict(rung='excellent', leadIn='4.6', award=HON, items=7)],
  rungBases='4.1: the three levels are the standards a student will have shown at the award of a bachelor\'s degree; 4.4 is a list after a "will be able to" lead-in under "Threshold level"; 4.5 and 4.6 are prose paragraphs under "Typical level" and "Excellent level", cut here by sentence; 1.15 points specialist master\'s to the highest levels',
  outcomeLists=[dict(leadIn='3.2', gloss="subject-specific knowledge and skills on completing a bachelor's", items=13, award=['honours']),
                dict(leadIn='3.3', gloss="cognitive abilities and generic skills on completing a bachelor's", items=9, award=['honours'])],
  outcomes=[
    dict(outcome='breadth, depth and insight', threshold='none', typical='4.5.s1', excellent='4.6.s1', basis='inferred', domain='knowledge', award=HON),
    dict(outcome='knowledge of theory and specialist topics', threshold='4.4.b1', typical='4.5.s2', excellent='4.6.s2', basis='inferred', domain='knowledge', award=HON),
    dict(outcome='appraising sources and their limits', threshold='4.4.b9', typical='4.5.s3', excellent='4.6.s4', basis='inferred', domain='subject-skill', award=HON),
    dict(outcome='investigation and research', threshold='none', typical='4.5.s4', excellent='4.6.s3', basis='inferred', domain='subject-skill', award=HON),
    dict(outcome='solving finance problems', threshold='4.4.b2', typical='4.5.s4', excellent='4.6.s5', basis='inferred', domain='subject-skill', award=HON),
    dict(outcome='synthesising and communicating', threshold='4.4.b13', typical='4.5.s5', excellent='4.6.s6', basis='inferred', domain='generic-skill', award=HON),
    dict(outcome='argument, insight and originality', threshold='none', typical='4.5.s5', excellent='4.6.s7', basis='inferred', domain='generic-skill', award=HON)])
SB4A_FULL = []
SB5 = [
  dict(body='professional, statutory and regulatory bodies (PSRBs), in general', says='courses may meet PSRB requirements for recognition, which can embed a professional standards framework; PSRBs take part in review and may accredit; their requirements may inform competence standards (D1, 2.24, 2.28, 4.3)', requirements='not yet ingested (Part E)'),
  dict(body='AACSB; Association of Corporate Treasurers (ACT); British Accounting and Finance Association (BAFA); Chartered Banker Institute (CBI); CFA Institute; Chartered Institute for Securities and Investment (CISI); EFMD; Financial Management Association (FMA); GARP; PRMIA', says='networks, professional and learned bodies that course teams may engage with for good practice and development (D1, 2.25)', requirements='not yet ingested (Part E)'),
  dict(body='CFA; CISI; Chartered Banker Institute; ICAEW; ICAS; ACT; GARP; AICPA-CIMA', says='bodies whose exams or qualifications some courses give advanced standing or accelerated progression towards, mainly specialist master\'s (D1, 2.26)', requirements='not yet ingested (Part E)'),
  dict(body='Financial Reporting Council (FRC)', says='its UK Corporate Governance Code (2024) on board diversity, inclusion and equal opportunity is an EDI topic for study (D1, 1.25)', requirements='not yet ingested (Part E)'),
  dict(body='Equality and Human Rights Commission', says='providers setting competence standards should follow its latest guidance (D1, 4.3)', requirements='not yet ingested (Part E)'),
  dict(body='Advance HE', says='source of examples of support and adjustments for disabled students, and co-author of the ESD guidance (D1, 1.28, 1.34)', requirements='std:doc:qaa-advancehe-esd-2021-guidance (for the ESD guidance)'),
]
SB6 = dict(
  themes=[dict(id='theme:edi', named='Equality, diversity and inclusion (front matter: equity, diversity and inclusion)', carriedIn=S6[0]['carriedIn'], statements=SB2[0]['statements']),
          dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=['1.28', '1.29'], statements=SB2[1]['statements']),
          dict(id='theme:esd', named='Education for sustainable development', carriedIn=S6[2]['carriedIn'], statements=SB2[2]['statements']),
          dict(id='theme:enterprise', named='Employability, enterprise and entrepreneurship education', carriedIn=S6[3]['carriedIn'], statements=SB2[3]['statements']),
          dict(id='theme:generative-ai', named='Generative artificial intelligence (GenAI) and AI applications in finance', carriedIn=S6[4]['carriedIn'], statements=SB2[4]['statements'])],
  frameworks=[dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.9', '2.12', '2.14', '2.15', '2.16']),
              dict(framework='scqf', named='FQHEIS', levels=['fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.9', '2.12', '2.14', '2.16'])],
  bodies=[dict(body='PSRBs', citedIn=['2.24', '2.28', '4.3']),
          dict(body='AACSB, BAFA, EFMD, FMA, PRMIA', citedIn=['2.25']),
          dict(body='ACT, Chartered Banker Institute, CFA Institute, CISI, GARP', citedIn=['2.25', '2.26']),
          dict(body='ICAEW, ICAS, AICPA-CIMA', citedIn=['2.26']),
          dict(body='Financial Reporting Council', citedIn=['1.25']),
          dict(body='Equality and Human Rights Commission', citedIn=['4.3']),
          dict(body='Advance HE', citedIn=['1.28', '1.34'])],
  sharedDocuments=[
    dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2'], role='guidance on evidence of achievement against the rungs'),
    dict(document='std:doc:qaa-fheq-2024-framework', named='the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['2.14'], role="master's credit and level"),
    dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development Guidance developed by Advance HE and QAA', citedIn=['1.34'], role='learning outcomes the core skills align with'),
    dict(document='std:doc:qaa-enterprise-2018-guidance', named='guidance on Enterprise and Entrepreneurship Education', citedIn=['1.37'], role='guidance providers may find helpful (edition inferred, Part E)'),
    dict(document="not yet ingested: listed in Part E", named="the Characteristics Statement: Master's Degree", citedIn=['2.14'], role="master's structure"),
    dict(document='not yet ingested: listed in Part E', named='the Characteristics Statement on Micro-Credentials', citedIn=['2.26'], role='level 7 micro-credits'),
    dict(document='not yet ingested: listed in Part E', named='Unpacking your Hidden Curriculum: Guide for educators', citedIn=['1.24'], role='an example for attending to the hidden curriculum'),
    dict(document='not yet ingested: listed in Part E', named='the latest guidance from QAA (on generative AI)', citedIn=['1.47'], role='due diligence on AI and integrity'),
    dict(document='std:doc:qaa-accounting-2025-benchmarks; std:doc:qaa-economics-2023-benchmarks', named='the Subject Benchmark Statements for Accounting and Economics', citedIn=['1.5'], role='cover single honours accounting and economics; joint degrees align with both')])

B1 = [
  dict(slug='sustainable-finance', definition='finance decisions (investing, lending, risk, insurance, disclosure) that weigh environmental, social and governance factors for long-term sustainable activity (D1, 1.30)', beneficiaryDefinition='finance that takes account of environmental, social and governance effects, not only returns', scopeNote='the definition the statement gives for its ESD section', category='unknown', practices=['education']),
  dict(slug='generative-ai', definition='large language model systems that use deep learning to imitate creativity and produce new content from prompts (D1, 1.43)', beneficiaryDefinition='AI tools that write or create new content when you give them a prompt', scopeNote='the statement treats AI more broadly beside it', category='unknown', practices=['education']),
  dict(slug='enterprise-and-entrepreneurship-education', definition='education that builds behaviours, attributes and competencies for successful careers and changing settings (D1, 1.37)', beneficiaryDefinition='learning that builds the enterprising skills and mindset that help in any career', scopeNote='abbreviated EED', category='unknown', practices=['education']),
  dict(slug='accessibility', definition='removing barriers so that learners can reach outcomes fairly (D1, 1.28)', beneficiaryDefinition='making sure nothing in the course stops you from reaching its outcomes', scopeNote='with a regulatory minimum', category='unknown', practices=['education']),
  dict(slug='hidden-curriculum', definition='the unstated expectations of how students behave (D1, 1.29)', beneficiaryDefinition='the unwritten rules of studying that nobody spells out', scopeNote='also the language of finance (1.24)', category='unknown', practices=['education']),
  dict(slug='alternative-investments', definition='investments that seek market inefficiencies through unusual assets and strategies, such as hedge funds, private equity, private credit and real assets (D1, 1.7)', scopeNote='given as a contemporary area', category='unknown', practices=['finance']),
  dict(slug='conversion-masters', definition="a master's for students whose first degree is not in Finance or who studied it in another jurisdiction (D1, 1.15)", scopeNote="beside the specialist master's", category='unknown', practices=['education']),
  dict(slug='threshold-standard', definition="the minimum a student will have shown on being awarded a bachelor's degree in Finance (D1, 4.1, 4.4)", scopeNote='with typical and excellent above it (4.5, 4.6)', category='unknown', practices=['education']),
]
B2A = [
  dict(concept='sustainable-finance', form='sustainable finance', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
  dict(concept='generative-ai', form='Generative artificial intelligence', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='generative-ai', form='GenAI', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
  dict(concept='enterprise-and-entrepreneurship-education', form='Enterprise and entrepreneurship education', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='enterprise-and-entrepreneurship-education', form='EED', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
  dict(concept='accessibility', form='Accessibility', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
  dict(concept='hidden-curriculum', form='hidden curriculum', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='alternative-investments', form='alternative investments', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
  dict(concept='conversion-masters', form="Finance conversion master's degrees", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='threshold-standard', form='minimum threshold', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
]
B4 = [dict(rel='contrasts-with', **{'from': 'conversion-masters'}, to="specialist master's (1.15)", note="the two kinds of master's the statement names")]
B5 = []
D3 = [dict(title="QAA Characteristics Statement: Master's Degree", why='cited in 2.14'),
      dict(title='QAA Characteristics Statement: Micro-credentials', why='cited in 2.26'),
      dict(title='QAA (2022) Unpacking your Hidden Curriculum: Guide for Educators', why='cited in 1.24'),
      dict(title="QAA guidance on generative AI (the latest, as 1.47 asks)", why='cited in 1.47'),
      dict(title='Finance Subject Benchmark Statement, previous edition (2019)', why='S7 supersedes and the key changes the front matter names')]

E = [
  'Pattern (new rung shape): threshold is a list (4.4, 15 items, lead-in "will be able to"); typical (4.5) and excellent (4.6) are prose paragraphs of "will" sentences. Cut here one record per sentence, with our ids 4.5.s1 to 4.5.s5 and 4.6.s1 to 4.6.s7 (the issuer\'s paragraph number plus sentence). The alternative, one record per paragraph, is for Abbott at P3. The builder leaves the sub-heading out of `headingPath` for these ids, since it reads only numeric ids (a tool point for std).',
  'Pattern: the threshold lead-in names no rung; the sub-heading "Threshold level" and 4.1\'s "minimum threshold" make it the rung. Threshold items take force `threshold` (4.1 defines it as the minimum for the award), with forceFrom 4.1; typical and excellent sentences keep "will" (their first sentences use "can distinguish themselves").',
  'Pattern: benchmark standards are for the bachelor\'s degree only; master\'s awards have no rungs of their own, and 1.15 says a specialist master\'s would be expected to be judged against the highest levels (recorded as 1.15.b1, force `describes`).',
  'Pattern: integrated master\'s (1.17) take the typical honours standard then master\'s level in their specialism: a plain-present norm, not taken as a statement.',
  'Force, words outside the five: 3.2 and 3.3 lead in "is generally expected to have" (all 22 items recorded as `describes`; for Abbott: should "generally expected" read as `will` or `should`?); 1.15.b1 "would be expected to be evaluated" (`describes`); 1.24.b3 "is necessary" read as `must`; 2.21 "it is essential to ensure" read as `must`; 1.6 and 1.7 "requires students to" and 2.3 "is required" read as `must`; 3.4 "It is the responsibility of each higher education provider" with "will be able to demonstrate" (taken as `will`).',
  'Not taken as statements, for P3: plain-present provider norms 1.13, 1.17, 1.29.b1, b2, b3 and b6 (under the lead-in "This will go beyond compliance ... to include, for example"), 1.30, 1.36, 1.45, 1.46, 1.47, 2.6, 2.8, 2.27; plain-present graduate descriptions 1.33 (last sentence), 1.39, 1.42 ("Finance graduates have an awareness"); predictive or descriptive "will" 1.14, 1.26 ("An EDI approach ... will take cognisance"), 1.29 lead-in, 2.10, 2.18, 4.1; predictive "should help" 1.35; "will need to adapt" 1.44; "it is expected that each level would see" 2.9; "It is not intended that degree programmes should include all the examples" 3.1 (negated); "is an essential component" 2.28; "it is important that" 1.19, 1.23 (first sentence), 1.36.',
  'S4: 1.24.b4 to b6 and 1.25.b1 to b8 follow "could include" or "including, but not limited to" lead-ins: examples, not statements. 1.7.b1 to b3 are kept inside the 1.7 record (examples of contemporary areas). 1.9 and 1.10 list careers and sectors: not statements.',
  'Skeleton corrections (`find` used): 4.4.b15, 3.3.b9, 1.29.b10, 2.4, 2.17, 2.21, 3.8 and 4.3 carried the next run-in heading; 1.15.b1 and 3.2.b13 were cut at a page break; 1.6, 1.28 and 3.14 trimmed of a trailing page number. The skeleton\'s rung counts (0, 0, 0) were wrong: the rungs are 15, 5 and 7.',
  'Skeleton theme hits corrected: 1.17 (EDI), 1.27 (accessibility), 1.29 (ESD) and 1.36 (enterprise) were heading run-ins of the next section, not content; 1.35 ("financial accessibility and inclusion") and 1.44 ("more accessible") use the words in another sense; 1.38 and 2.20 carry no EDI content. 2.20 and 1.2 dropped for the same reason. Added: generative AI (1.43 to 1.47, 3.2.b10), not in the skeleton.',
  'SB4 gradeOf, all inferred (the issuer pairs nothing): 4.5.s2 to 4.4.b1, 4.5.s3 to 4.4.b9, 4.5.s4 to 4.4.b2, 4.5.s5 to 4.4.b13; 4.6.s1 to 4.5.s1, 4.6.s2 to 4.5.s2, 4.6.s3 to 4.5.s4, 4.6.s4 to 4.5.s3, 4.6.s5 to 4.5.s4, 4.6.s6 to 4.5.s5, 4.6.s7 to 4.5.s5. Two excellent sentences share one typical sentence twice (4.5.s4 and 4.5.s5); weaker matches: 4.5.s4 to 4.4.b2 (investigation is not in the threshold item) and 4.6.s7 to 4.5.s5. 4.5.s1 has no threshold match; 4.4.b3 to b8, b10 to b12, b14 and b15 have no typical match.',
  'S5, crosswalk conflict: 2.12 places the CertHE at FHEQ 4 and FQHEIS 8 and the DipHE at FHEQ 5 and FQHEIS 9; the FHEQ document\'s Table 1 (std:doc:qaa-fheq-2024-framework, S5) places them at SCQF 7 and SCQF 8. Recorded as stated; for Abbott at P3 (an issuer error, recall: likely).',
  'S5: spine:6 and spine:7 are inferred from the reference framework R2, not stated.',
  'Subjects: hecos 100107 and cah CAH17-01-07 (finance) and the titles in 1.3 (financial management 100832, banking 100827, investment 100828) are stated by name; CAH17-01 and CAH17 (business and management) are inferred from the CAH hierarchy, held back until P3. No HECoS term found for fintech, personal finance, financial services or sustainable finance.',
  'S7: the previous statement is named only as "the previous Subject Benchmark Statement"; 2019 is read from the back matter\'s advisory group list (minor update) and is inferred.',
  'S7, SB6: the enterprise guidance is cited without a date (1.37); std:doc:qaa-enterprise-2018-guidance is our inference (recall).',
  'SB6, front matter: names the EDI theme "equity, diversity and inclusion" and the enterprise theme "employability, entrepreneurship and enterprise education"; the section headings use "Equality" and "Employability, enterprise and entrepreneurship education". Front matter is excluded matter, so cited by section only.',
  'SB6, not tagged as bodies or shared QAA documents (outside QAA, named once): the UN SDGs (1.13, 1.21, 1.30, 1.31, 1.32), OECD Principles of Corporate Governance, Principles of Responsible Investment, Principles for Responsible Banking, Principles for Sustainable Insurance and the UK net zero legislation (1.30), the Financial Stability Task Force (1.36), the Russell Group Principles on generative AI (1.47), the Equality Act 2010 (4.3), the Office for Students (front matter), the Quality Code and QAA Glossary (front matter).',
  'SB5: the issuer writes "Chartered Institute of Management Accountants (AICPA-CIMA)" and "CFA Institute (Chartered Financial Analyst)"; kept as given. None of the bodies\' requirements is ingested.',
  'S1, licence: the text gives a copyright notice and no re-use terms; QAA\'s terms for holding and chunking are to check.',
  'S9: not researched in P1.',
  'Levels: generic-skill records (3.3, 4.4.b13 to b15, 4.5.s5, 4.6.s6, 4.6.s7) refine fheq:6, which is in S5.',
  'Provider duties (28 records) have no student version; their `aad` addresses the programme team only.',
]
