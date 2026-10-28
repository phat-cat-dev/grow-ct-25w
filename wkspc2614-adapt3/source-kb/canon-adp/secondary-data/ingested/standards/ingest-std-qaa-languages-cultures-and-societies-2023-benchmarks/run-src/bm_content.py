# Judgement for run 0115, QAA Languages, Cultures and Societies 2023 (std run agent). Keys are S4 ids under
# qaa/languages-cultures-and-societies-2023/. Built by tools/bm_build.py (BM-BRIEF 0.2.3).
HON = "bachelor's with honours"
CITE = 'QAA (2023), Languages, Cultures and Societies Subject Benchmark Statement'

META = dict(
    run='0115', p1='2026-10-03 17:44',
    title='Subject Benchmark Statement Languages, Cultures and Societies',
    heading='Subject Benchmark Statement: Languages, Cultures and Societies (QAA, March 2023)',
    edition='March 2023 (fifth edition)', published='2023-03',
    status='current', supersedes='the fourth edition (2019), revised by QAA from the third (2015); earlier Languages and Related Studies editions 2007 and 2002',
    subjects=[
        dict(scheme='hecos', code='100329', label='modern languages', basis='stated'),
        dict(scheme='cah', code='CAH19-04-09', label='others in language and area studies', basis='inferred'),
        dict(scheme='cah', code='CAH19-04', label='languages and area studies', basis='inferred'),
        dict(scheme='cah', code='CAH19', label='language and area studies', basis='inferred'),
        dict(scheme='hecos', code='101130', label='translation studies', basis='stated'),
        dict(scheme='hecos', code='101118', label='Celtic studies', basis='inferred'),
        dict(scheme='hecos', code='100317', label='British Sign Language studies', basis='inferred'),
    ],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, revision with cross-cutting themes (this statement: fifth edition, March 2023)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what a graduate in Languages, Cultures and Societies (modern and other languages "
                     "studied with their cultures and societies) can do at the end of an honours degree. It states one rung only, the "
                     "threshold, in five groups: language proficiency (towards or at CEFR C1), explicit knowledge of language, "
                     "intercultural awareness and pluricultural competence, subject knowledge and skills and general skills. Reach for "
                     "it when designing, reviewing or describing a languages course or its outcomes. It is not a curriculum, it does not "
                     "set master's standards and it is not a regulatory requirement in England."),
    summary=("Published by QAA in March 2023 as the fifth edition, the statement covers single, joint and combined honours degrees "
             "in languages, cultures and societies across the four UK nations and mentions master's provision without setting "
             "standards for it. It describes the subject and its graduates (1.10, 1.11), the four cross-cutting themes (equality, "
             "diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship), distinctive features "
             "(design, progression, flexibility, partnership, monitoring), content, teaching, immersive placements and assessment, "
             "and threshold standards only, at FHEQ level 6 and FQHEIS level 10, applying to courses where languages make up at "
             "least a third of study in every year. Performance above threshold is left to Annex D of the FHEQ. It names the CEFR "
             "as the proficiency scale and no professional body."),
    authority='reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales (Quality Assessment Framework for Wales) and Scotland (Quality Enhancement Framework); part of the quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)')

S2 = dict(
    governs='what a graduate of an honours degree in languages, cultures and societies knows, understands and can do at threshold and the features, content, teaching and assessment of such degrees',
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    statedScope='"This Subject Benchmark Statement refers to the provision of undergraduate and postgraduate degrees in Languages, Cultures and Societies (LCS) in the four nations of the UK." (D1, 1.1); the standards apply to courses in which languages are at least one-third of study and studied in every year (D1, 4.5)',
    statedSubjects=[
        dict(name='Languages, Cultures and Societies (LCS)', locator='(D1, 1.1; 1.5)', kind='subject', codes=[dict(scheme='hecos', code='100329', label='modern languages')]),
        dict(name='Modern Languages', locator='(D1, 4.6)', kind='programme title', codes=[dict(scheme='hecos', code='100329', label='modern languages')]),
        dict(name='translation and interpreting', locator='(D1, 1.4; 2.2)', kind='specialism', codes=[dict(scheme='hecos', code='101130', label='translation studies')]),
        dict(name='Celtic languages', locator='(D1, 1.8)', kind='specialism', codes=[dict(scheme='hecos', code='101118', label='Celtic studies')]),
        dict(name='sign languages', locator='(D1, 1.14; 4.11)', kind='specialism', codes=[dict(scheme='hecos', code='100317', label='British Sign Language studies')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Languages, Cultures and Societies degree',
            '2': 'Distinctive features of a Languages, Cultures and Societies degree',
            '3': 'Content, structure and delivery',
            '4': 'Benchmark standards'}
SUB = [('1.1', '1.6', 'Context'), ('1.7', '1.11', 'Purposes and characteristics of a Languages, Cultures and Societies degree'),
       ('1.12', '1.18', 'Equality, diversity and inclusion'), ('1.19', '1.21', 'Accessibility'), ('1.22', '1.25', 'Sustainability'),
       ('1.26', '1.32', 'Enterprise and entrepreneurship education'),
       ('2.1', '2.7', 'Design'), ('2.8', '2.11', 'Progression'), ('2.12', '2.14', 'Flexibility'), ('2.15', '2.17', 'Partnership'),
       ('2.18', '2.20', 'Monitoring and review'),
       ('3.1', '3.2', 'Content'), ('3.3', '3.4', 'Subject-specific content'), ('3.5', '3.6', 'Generic, transferable and employability content'),
       ('3.7', '3.7', 'Teaching and learning'), ('3.8', '3.13', 'Characteristics of the study of Languages, Cultures and Societies'),
       ('3.14', '3.15', 'Teaching and learning methods'), ('3.16', '3.19', 'International and national immersive placements'),
       ('3.20', '3.20', 'Assessment'), ('3.21', '3.25', 'Assessment of language proficiency'), ('3.26', '3.26', 'Assessment of subject-related studies'),
       ('4.1', '4.9', 'Introduction'), ('4.10', '4.11', 'Standard of achievement at threshold level: Language proficiency'),
       ('4.12', '4.12', 'Explicit knowledge of language'), ('4.13', '4.14', 'Intercultural awareness and pluricultural competence'),
       ('4.15', '4.15', 'Subject-specific knowledge and skills'), ('4.16', '4.16', 'General and transferable skills')]

G = {
    '1.1': 'scope: degrees of every pattern across the UK, honours and master\'s',
    '1.2': 'honours assumed; context holds for exit awards too',
    '1.3': 'elective language study elsewhere gains some of the same skills',
    '1.4': 'professional master\'s, chiefly translation and interpreting; interdisciplinary topics',
    '1.5': 'how the subject is organised within institutions varies',
    '1.6': 'overlap with English and Linguistics; TESOL left out',
    '1.7': 'core: communicative proficiency plus study of language, culture and society',
    '1.8': 'immersive learning and the year abroad as typical features',
    '1.9': 'value to the UK economy and society; graduate careers',
    '1.10': 'profile of the typical graduate (outcome list)',
    '1.11': 'capabilities shared with other SHAPE subjects (outcome list)',
    '1.12': 'outward-looking, inclusive learning environments',
    '1.13': 'varied teaching, assessment and delivery to widen access',
    '1.14': 'minority, sign, heritage and constructed languages; language rights',
    '1.15': 'injustice, colonialism and inclusive curriculum choices',
    '1.16': 'against native-speakerism; proficiency measured by a framework',
    '1.17': 'linguistic diversity beyond a single standard form',
    '1.18': 'placements, diversity and student well-being abroad',
    '1.19': 'uneven school provision; supporting varied prior learning',
    '1.20': 'beginners and heritage speakers; languages open to everyone',
    '1.21': 'barriers to placements abroad and alternative immersion',
    '1.22': 'sustainability through equality, peace and justice themes',
    '1.23': 'the four UN goals the subject engages most',
    '1.24': 'nature, climate and finding common ground across cultures',
    '1.25': 'the carbon cost of travel for placements',
    '1.26': 'what enterprise education adds for careers',
    '1.27': 'enterprise attributes graduates show',
    '1.28': 'placements build entrepreneurial attributes',
    '1.29': 'students as sensitive communicators and mediators at work',
    '1.30': 'applied linguistics and sociolinguistics as workplace assets',
    '1.31': 'cultural and digital literacy; working with machine translation',
    '1.32': 'enterprise beyond employment; pointer to QAA guidance',
    '2.1': 'undergraduate study: proficiency plus engagement with cultures; teaching medium',
    '2.2': 'postgraduate depth, autonomy and professional skills',
    '2.3': 'analysis of historical and current material; joint degrees with SHAPE subjects',
    '2.4': 'combinations with STEM subjects',
    '2.5': 'intercultural and transnational by nature',
    '2.6': 'varied ways of bringing out intercultural dimensions',
    '2.7': 'diversity of voices against Anglophone dominance',
    '2.8': 'progression toward the threshold; second-class degrees and further study',
    '2.9': 'joint and combined honours students',
    '2.10': 'exit awards, integrated master\'s and part-time routes',
    '2.11': 'what shapes progression; its consistent features',
    '2.12': 'study modes and levels of language modules',
    '2.13': 'language components in other subjects\' degrees',
    '2.14': 'digital platforms and flipped teaching for flexibility',
    '2.15': 'work placements and internships',
    '2.16': 'civic and community partnerships',
    '2.17': 'exchange agreements; employer projects at master\'s level',
    '2.18': 'monitoring and periodic review',
    '2.19': 'external reviewers in periodic review',
    '2.20': 'external examiners, one per language',
    '3.1': 'content varies; single and joint honours coverage',
    '3.2': 'content as a framework; designers stay open to change',
    '3.3': 'subject content: proficiency, awareness, culture and society',
    '3.4': 'the subject-specific skills courses develop',
    '3.5': 'the distinctive education languages give',
    '3.6': 'communicative, transactional and problem-solving skills',
    '3.7': 'methods listed in no order of priority',
    '3.8': 'what shapes teaching methods',
    '3.9': 'intensive language learning; beginners need more contact',
    '3.10': 'contact with proficient users and authentic material',
    '3.11': 'language as a gateway to culture and society',
    '3.12': 'learning technology and online resources',
    '3.13': 'learner autonomy and guided independent study',
    '3.14': 'methods for developing language skills',
    '3.15': 'methods for studying cultures and societies',
    '3.16': 'residence in a target-language country',
    '3.17': 'how placements vary and are supported',
    '3.18': 'what immersive placements typically do',
    '3.19': 'other routes when residence abroad is not possible',
    '3.20': 'inclusive principles of assessment design',
    '3.21': 'feedback and a wide range of assessment types',
    '3.22': 'the four skill areas assessed for proficiency',
    '3.23': 'forms of proficiency assessment',
    '3.24': 'further forms at master\'s level',
    '3.25': 'assessing in the target language',
    '3.26': 'assessment of cultural, linguistic and social study',
    '4.1': 'standards are the minimum for the honours award',
    '4.2': 'most exceed threshold; Annex D for the classes',
    '4.3': 'the CEFR for judging proficiency',
    '4.4': 'specifications cite the CEFR or other scales such as HSK',
    '4.5': 'where the standards apply: a third of study, every year',
    '4.6': 'award titles such degrees carry',
    '4.7': 'smaller language share: not every element expected',
    '4.8': 'no set curriculum; read with course documentation',
    '4.9': 'what shapes course objectives and outcomes',
    '4.10': 'threshold: language proficiency, towards or at C1',
    '4.11': 'when C1 is out of reach; B2 as the usual alternative',
    '4.12': 'threshold: explicit knowledge of language',
    '4.13': 'threshold: knowledge of cultures and societies',
    '4.14': 'threshold: intercultural skills (continues 4.13)',
    '4.15': 'threshold: subject-specific knowledge and skills',
    '4.16': 'threshold: general and transferable skills',
}
CTYPE = {'3.3': 'area', '3.4': 'area', '3.5': 'area', '3.6': 'area',
         '3.8': 'practice', '3.9': 'practice', '3.10': 'practice', '3.11': 'practice', '3.12': 'practice', '3.13': 'practice',
         '3.14': 'practice', '3.15': 'practice', '3.16': 'practice', '3.17': 'practice', '3.18': 'practice', '3.19': 'practice',
         '3.20': 'practice', '3.21': 'practice', '3.22': 'practice', '3.23': 'practice', '3.24': 'practice', '3.25': 'practice', '3.26': 'practice'}
EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1 and S2'),
    dict(number='section headings', heading='section heading lines 1 to 4', kind='other: headings, recorded in S3 as sections'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for SB6 and S7'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Languages, Cultures and Societies', kind='other: membership lists, read for SB5 and S8'),
    dict(number='none', heading='closing page: edition, publication date and copyright', kind='other: read for S1 and S8'),
]

P = {}
def s(i, **k): P[i] = k

FW6 = 'the FHEQ honours descriptor'

# ------------------------------------------------------------------ helpers for the agent instructions
def aaw_out(i, what, nb, force_note):
    return (f"Describe this as {force_note}: {what}. Hold it at honours level (FHEQ level 6, FQHEIS level 10) and cite it as {CITE}, para {i}. "
            f"Do not claim it is a minimum every graduate meets, a regulatory requirement or a standard for master's study. "
            f"Set it beside {nb} and the shared step spine:6.")

def aad_out(when, q):
    return (f"Bring this up when {when}. Put it to a student in plain words, as a picture of what people who finish the degree often show, "
            f"and to staff as the issuer's profile of the subject's graduates. Ask: {q} "
            f"Avoid reading the issuer's list aloud or treating it as a pass condition.")

def aaw_thr(i, what, nb, extra=''):
    return (f"Describe this as a threshold outcome, the minimum every honours graduate in the subject has shown by the award: {what}. "
            f"It holds at FHEQ level 6 and FQHEIS level 10 for a bachelor's degree with honours where languages are at least a third of study in every year; cite it as {CITE}, para {i}. "
            f"Do not present it as a regulatory requirement, as typical or excellent performance or as a master's standard{extra}. "
            f"Set it beside {nb}, and point to Annex D (qaa/fheq-2024/annex-d) for the classes above the minimum.")

def aad_thr(when, q):
    return (f"Raise this when {when}. Tell a student, in the second person and plain words, that this is the floor everyone reaches by the end of the degree, and frame it for staff as a threshold outcome their assessment has to evidence. "
            f"Ask: {q} "
            f"Avoid reciting the issuer's wording at length or suggesting that meeting it signals a high classification.")

# ------------------------------------------------------------------ 1.10 the typical graduate (outcome list; lead-in has no modal)
L110 = dict(type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='graduates of the subject', addressee='learner', award=HON)
def k110(n, **k): s('1.10.b%d' % n, **L110, **k)
k110(1, verbs=['have'], about='high proficiency in the studied languages', domain='subject-skill',
     para='Graduates typically reach a high level in the language or languages studied, strong in producing, receiving, interacting and mediating, so they communicate in them with confidence and subtlety.',
     prac='The usual graduate profile includes a high command of each studied language across all four modes (production, reception, interaction, mediation), enough to communicate with assurance and finesse.',
     ben='You are likely to finish this degree highly capable in your languages: confident speaking, writing, listening, reading and mediating between them.',
     aaw=aaw_out('1.10, item 1', 'a typical graduate has a high command of the studied languages across all four modes', 'the threshold proficiency list (4.10.b1 to 4.10.b5), which asks less', 'a descriptive profile of the usual graduate, carrying no modal'),
     aad=aad_out('a student asks how good their language will be by the end, or a team describes graduate attributes', 'Which of the four modes feels strongest for you now, and which needs the most work?'))
k110(2, verbs=['are', 'deal'], about='context, variation and ambiguity in communication', domain='understanding',
     para='Graduates typically understand the wider setting of communication, notice how usage varies and why it matters and can handle uncertainty and ambiguity when communicating.',
     prac='Graduates usually read communication in its context, are alert to variation in usage and its meaning and cope with uncertain or ambiguous exchanges.',
     ben='You are likely to become alert to how the setting shapes what people say, to notice shifts in usage and what they signal and to cope when meaning is unclear.',
     aaw=aaw_out('1.10, item 2', 'awareness of context and variation and the ability to manage ambiguity', '4.12.b2 and 4.14.b5 at threshold and qaa/fheq-2024/4.15.b4 on uncertainty', 'a descriptive profile of the usual graduate'),
     aad=aad_out('a student finds real conversations less tidy than the classroom, or staff discuss intercultural outcomes', 'When did a conversation last leave you unsure what was meant, and what did you do?'))
k110(3, verbs=['are', 'acquire'], about='awareness of language technologies', domain='subject-skill',
     para='Graduates typically know about relevant language technologies, such as translation tools, language software and corpora, and some become skilled with them.',
     prac='Graduates usually know the relevant language technologies (computer-assisted translation, processing and learning software, online corpora) and some gain competence in them.',
     ben='You are likely to learn about the tools that support language work, such as translation software and online corpora, and you may become skilled with some of them.',
     aaw=aaw_out('1.10, item 3', 'awareness of language technologies, with competence for some', '4.16.b2 at threshold and 1.31 on machine translation', 'a descriptive profile of the usual graduate, which itself says only some gain competence'),
     aad=aad_out('a student asks whether translation tools matter for their career, or a team plans digital content', 'Which language tools have you tried, and do you trust their output?'))
k110(4, verbs=['have', 'see', 'understand', 'value'], about='open mindset and multiple perspectives', domain='generic-skill',
     para='Graduates typically have an open outlook and can view the world as others do, so they understand and value more than one perspective.',
     prac='The usual graduate is open-minded and able to take other people\'s viewpoints, valuing a plurality of perspectives.',
     ben='You are likely to grow more open-minded, able to see things as other people see them and to value views unlike your own.',
     aaw=aaw_out('1.10, item 4', 'an open mindset and the capacity to take and value other perspectives', '4.14.b1 at threshold', 'a descriptive profile of the usual graduate'),
     aad=aad_out('a student reflects on how study abroad or contact with another culture changed them', 'Can you name a view you understand better now than when you started?'))
k110(5, verbs=['appreciate', 'analyse', 'interpret'], about='interpreting diverse cultural forms', domain='subject-skill',
     para='Graduates typically appreciate, analyse and critically interpret a wide range of cultural forms, products and practices, from local and national cultures to high, popular, material and digital culture and everyday customs.',
     prac='Graduates usually analyse and interpret critically a broad span of culture: community to national, high to popular, material and digital and the habits of daily life.',
     ben='You are likely to be able to appreciate and critically interpret many kinds of culture, from literature and film to everyday habits, local traditions and digital media.',
     aaw=aaw_out('1.10, item 5', 'critical interpretation of a wide range of cultural forms and practices', '4.15.b2 at threshold and qaa/fheq-2024/4.15.b7', 'a descriptive profile of the usual graduate'),
     aad=aad_out('a student asks what the culture side of the degree builds, or a team maps cultural modules', 'Which cultural form do you find easiest to analyse, and which least?'))
k110(6, verbs=['understand', 'mediate', 'analyse', 'compare'], about='ideas and events across boundaries', domain='subject-skill',
     para='Graduates typically grasp, mediate and compare ideas and happenings that cross national, cultural or linguistic borders, such as relations between countries past and present and analyse them.',
     prac='Graduates usually work with ideas and events that cross borders of nation, culture or language, understanding, mediating, analysing and comparing them, for instance relations between states.',
     ben='You are likely to be able to explain, compare and mediate ideas and events that cross borders of country, culture or language, such as how two nations relate.',
     aaw=aaw_out('1.10, item 6', 'understanding and comparing ideas and events that cross borders', '4.15.b5 and 4.14.b6 at threshold', 'a descriptive profile of the usual graduate'),
     aad=aad_out('a student links their languages to international affairs or careers in diplomacy', 'What cross-border issue could you explain from two sides?'))
k110(7, verbs=['address'], about='comparative work across languages and cultures', domain='subject-skill',
     para='Graduates typically tackle questions comparatively across languages, cultures and societies, transnationally or with attention to regional and minoritised ones.',
     prac='Graduates usually approach problems comparatively across languages and cultures, at transnational scale or with attention to regional and minoritised communities.',
     ben='You are likely to learn to approach questions by comparing languages, cultures and societies, including regional and minority ones, not only national ones.',
     aaw=aaw_out('1.10, item 7', 'comparative work across languages and cultures, including minoritised ones', '4.13.b3 at threshold', 'a descriptive profile of the usual graduate'),
     aad=aad_out('a student plans a comparative project or a team designs comparative modules', 'Which two communities could you compare, and what would the comparison show?'))
k110(8, verbs=['are', 'possess', 'facilitate'], about='mobility through language and intercultural skill', domain='generic-skill',
     para='Graduates typically have the intercultural skills and language ability to move and work internationally, especially when the degree included a placement abroad.',
     prac='Graduates are usually equipped for international mobility by their language and intercultural skills, most of all where an international placement was part of the degree.',
     ben='You are likely to leave with the language and intercultural skills to live and work in other countries, especially if you spend time abroad during your studies.',
     aaw=aaw_out('1.10, item 8', 'readiness for international mobility', '1.18 and 3.16 on placements', 'a descriptive profile of the usual graduate, hedged by the issuer as likely'),
     aad=aad_out('a student weighs a year abroad or asks about working overseas', 'Where could you see yourself working, and what would you need to manage there?'))

# ------------------------------------------------------------------ 1.11 capabilities shared with SHAPE subjects (outcome list; lead-in has no modal)
L111 = dict(type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='graduates of the subject', addressee='learner', award=HON, domain='generic-skill')
def k111(n, **k): s('1.11.b%d' % n, **L111, **k)
def aaw111(n, what, nb):
    return aaw_out('1.11, item %d' % n, what + ', one of the capabilities shared with other SHAPE subjects', nb, 'part of a descriptive list of general capabilities')
k111(1, verbs=['work', 'engaging', 'reflecting'], about='independent work using supervision and feedback',
     para='Graduates develop the capacity to work on their own while using supervision and guidance, reflecting on progress and acting on feedback.',
     prac='Graduates develop independent working that still draws on supervision, with reflection on progress and use of feedback.',
     ben='You will build the habit of working on your own while still using guidance, thinking about your progress and acting on feedback.',
     aaw=aaw111(1, 'independent work that uses guidance and feedback', '4.16.b7 at threshold and qaa/fheq-2024/4.15.b5'),
     aad=aad_out('a student struggles with feedback or with working alone', 'What did you change after your last piece of feedback?'))
k111(2, verbs=['work'], about='teamwork',
     para='Graduates develop as effective collaborators within a team.',
     prac='Graduates develop effective collaboration as team members.',
     ben='You will learn to be a useful, effective member of a team.',
     aaw=aaw111(2, 'effective teamwork', '4.16.b8 at threshold and qaa/fheq-2024/annex-d/transferable/r2/3rd'),
     aad=aad_out('a student faces group work or asks what employers look for', 'What role do you usually take in a group, and does it help the team?'))
k111(3, verbs=['demonstrate', 'managing'], about='initiative and self-management',
     para='Graduates develop initiative, self-discipline and self-direction, for instance in managing their time well.',
     prac='Graduates develop initiative and self-direction, including efficient management of their own time.',
     ben='You will grow in taking the initiative and organising yourself, including managing your time well.',
     aaw=aaw111(3, 'initiative, self-discipline and time management', '4.16.b7 at threshold and qaa/fheq-2024/4.15.b9.1'),
     aad=aad_out('a student is overwhelmed by deadlines or planning a placement', 'How do you plan your week when several deadlines meet?'))
k111(4, verbs=['demonstrate', 'gathering', 'organising', 'deploying'], about='handling evidence and information',
     para='Graduates develop sound ways of collecting, ordering and using a range of evidence, data and information.',
     prac='Graduates develop appropriate methods for collecting, structuring and using varied evidence, data and information.',
     ben='You will learn good ways to find, organise and use evidence, data and information of many kinds.',
     aaw=aaw111(4, 'gathering and using evidence and information', '4.16.b1 at threshold and qaa/fheq-2024/annex-d/cognitive/r1/3rd'),
     aad=aad_out('a student starts a research task or essay', 'How do you keep track of your sources and decide which to use?'))
k111(5, verbs=['show', 'consider', 'solve'], about='analysis and problem-solving',
     para='Graduates develop analytical ability, a questioning habit and the capacity to work through problems, including those without one right answer.',
     prac='Graduates develop analysis, a questioning disposition and problem-solving, including for open problems with no single answer.',
     ben='You will become more analytical and questioning, able to work through problems, even ones with no single right answer.',
     aaw=aaw111(5, 'analysis, questioning and problem-solving', '4.16.b3 at threshold and qaa/fheq-2024/4.15.b7'),
     aad=aad_out('a student meets an open question with no clear answer', 'How do you decide between two reasonable answers?'))
k111(6, verbs=['demonstrate', 'shape'], about='conceptual grasp and argument',
     para='Graduates develop a grasp of concepts and the ability to build arguments.',
     prac='Graduates develop conceptual understanding and skill in constructing argument.',
     ben='You will get better at grasping ideas and building a case of your own.',
     aaw=aaw111(6, 'conceptual grasp and argument', '4.16.b5 at threshold and qaa/fheq-2024/4.15.b3.1'),
     aad=aad_out('a student plans an essay or presentation', 'What is the one claim your essay is trying to prove?'))
k111(7, verbs=['exhibit'], about='clear structured communication',
     para='Graduates develop structure, coherence and clarity in verbal and non-verbal communication.',
     prac='Graduates develop well-structured, coherent and clear communication, verbal and non-verbal.',
     ben='You will learn to communicate clearly and in an organised way, in words and in other ways.',
     aaw=aaw111(7, 'clear, coherent communication', '4.16.b4 at threshold and qaa/fheq-2024/4.15.b8'),
     aad=aad_out('a student prepares to present or receives feedback on clarity', 'Could a listener sum up your main point after one hearing?'))
k111(8, verbs=['show', 'recognise'], about='intellectual integrity and independence',
     para='Graduates develop intellectual integrity, maturity and independence, including spotting where others\' arguments are strong or weak.',
     prac='Graduates develop intellectual integrity and independence of mind, including judging the strengths and flaws in others\' reasoning.',
     ben='You will grow in intellectual honesty and independence, and get better at seeing where other people\'s arguments hold up or fall down.',
     aaw=aaw111(8, 'intellectual integrity and judging others\' arguments', '4.16.b8 at threshold and qaa/fheq-2024/4.15.b7'),
     aad=aad_out('a student reviews a peer\'s work or a critic\'s argument', 'Where is the weakest step in the argument you are reading?'))
k111(9, verbs=['exhibit'], about='imagination and creativity',
     para='Graduates develop imaginative insight and creativity.',
     prac='Graduates develop imaginative insight and creative ability.',
     ben='You will develop your imagination and creativity.',
     aaw=aaw111(9, 'imaginative insight and creativity', 'qaa/fheq-2024/annex-d/cognitive/r4/3rd'),
     aad=aad_out('a student considers creative or reflective assessment options', 'What piece of work let you be most inventive?'))
k111(10, verbs=['show'], about='academic integrity and research ethics',
     para='Graduates develop awareness of academic integrity and of the ethical duties of anyone doing research.',
     prac='Graduates develop awareness of academic integrity and the ethical obligations of researchers.',
     ben='You will understand academic honesty and the ethical duties you take on when you do research.',
     aaw=aaw111(10, 'awareness of academic integrity and research ethics', '4.16.b9 at threshold'),
     aad=aad_out('a student asks about referencing, translation tools or research with people', 'When might using a source or tool cross the line into someone else\'s work?'))
k111(11, verbs=['demonstrate'], about='digital literacy',
     para='Graduates develop digital literacy.',
     prac='Graduates develop digital literacy skills.',
     ben='You will become confident and capable with digital tools and information.',
     aaw=aaw111(11, 'digital literacy', '4.16.b2 at threshold and qaa/fheq-2024/annex-d/transferable/r1/3rd'),
     aad=aad_out('a student asks which digital skills the degree builds', 'Which digital tools do you use for your languages, and how well?'))
k111(12, verbs=['appreciate', 'engage'], about='global sustainability debates', find='appreciate and engage in contemporary debates relating to global sustainability and global perspectives.',
     para='Graduates develop an appreciation of, and take part in, current debates on global sustainability and global perspectives.',
     prac='Graduates develop engagement with present-day debates on global sustainability and on global viewpoints.',
     ben='You will take part in current debates about sustainability and the world seen from many places.',
     aaw=aaw111(12, 'engagement with debates on global sustainability', 'the sustainability theme (1.22 to 1.25) and 4.15.b5 at threshold'),
     aad=aad_out('a student connects their languages to climate or global justice questions', 'Which sustainability debate looks different in the language you study?'))

# ------------------------------------------------------------------ enterprise paragraphs with graduate outcomes ("are able to")
s('1.27', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
  verbs=['challenged', 'recognise', 'mediate', 'display', 'adapt', 'confront'], about='enterprise attributes from engaging other cultures', domain='generic-skill', award=HON,
  para='Because every student must engage with languages and cultures not their own, graduates will be curious and open, able to recognise and manage their own bias and will show enterprise attributes such as agility, flexibility, critical thinking, emotional literacy and digital skill; they will be able to adapt and keep learning, and facing uncertainty and failure builds resilience and initiative.',
  prac='Engaging with other languages and cultures is the means; the expected result is graduates who will be curious, aware of their own bias, agile and critical, emotionally and digitally literate, able to adapt and keep learning and resilient after facing risk and failure.',
  ben='Working with languages and cultures unlike your own will make you more curious and open, help you notice your own bias and build flexibility, critical thinking, emotional awareness and digital skill; you will be able to adapt, keep learning and bounce back from setbacks.',
  aaw=(f"Describe this as an expected graduate outcome stated with 'are able to' inside the enterprise and entrepreneurship theme: curiosity, managing one's own bias, adaptability and resilience. "
       f"Hold it at honours (FHEQ level 6, FQHEIS level 10) and cite it as {CITE}, para 1.27. Do not present it as one of the threshold outcomes in section 4 or as a regulatory requirement. "
       f"Set it beside 1.11.b3 and 4.14.b2, the descriptor items qaa/fheq-2024/4.15.b9.1 and 4.15.b9.2 and the QAA enterprise guidance (std:doc:qaa-enterprise-2018-guidance)."),
  aad=("Raise this when a student asks how a languages degree helps with work or enterprise, or a team plans employability content. "
       "Put it to a student as qualities that living between languages tends to build, and to staff as an outcome to make visible in teaching and placements. "
       "Ask: When did working in another language make you change your plan, and what did you learn? Avoid presenting these traits as a checklist a student fails if they lack one."))
s('1.29', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['have', 'operate'], about='sensitive communication and mediation at work', domain='subject-skill', award=HON,
  para='Students have a refined understanding of language and communication in real and virtual settings, notice the cultural and contextual factors shaping usage and through intercultural awareness and mediation will be able to work as sensitive communicators, negotiators and influencers in varied professional settings.',
  prac='Students build a refined grasp of real-world communication, including online, and of how culture and context shape usage; the expected result is that they will be able to act as sensitive communicators, negotiators and influencers at work.',
  ben='You will understand how language works in real and online settings and how culture and context shape it, and you will be able to communicate, negotiate and influence with sensitivity in many kinds of job.',
  aaw=(f"Describe this as an expected outcome for students, stated with 'are able to' within the enterprise theme: intercultural communication, negotiation and influence at work. "
       f"Hold it at honours (FHEQ level 6, FQHEIS level 10) and cite it as {CITE}, para 1.29. Do not claim it is a threshold standard or that it promises a particular career. "
       f"Set it beside 4.14.b3 and 4.14.b6 at threshold and the descriptor item qaa/fheq-2024/4.15.b8."),
  aad=("Bring this up when a student asks how their language skills translate into professional roles. "
       "Put it to a student plainly as the professional value of reading context and mediating between people, and to staff as a link between language teaching and employability. "
       "Ask: In what situation have you had to adjust how you spoke to suit the person or setting? Avoid overstating it as a guarantee of negotiating or leadership roles."))
s('1.31', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
  verbs=['are', 'navigate', 'analyse', 'acquire', 'provide', 'reviewing', 'enhancing'], about='cultural and digital literacy, collaboration, machine translation', domain='generic-skill', award=HON,
  para='Graduates are culturally and digitally literate and will be able to find their way through and analyse language, culture and society in a connected, technology-heavy world; they gain collaborative skills across backgrounds, can lead by bringing sensitivity to language into work and work well with technology such as by revising machine translation output.',
  prac='The expected result is graduates who will be able to analyse language and culture in a digitally connected world, collaborate across linguistic, cultural and disciplinary lines, lead through attention to language and work productively with technology, for instance post-editing machine translation.',
  ben='You will become culturally and digitally literate, able to make sense of language and culture in a connected world, work well with people from many backgrounds and use technology wisely, for example by checking and improving machine translations.',
  aaw=(f"Describe this as an expected graduate outcome stated with 'are able to' within the enterprise theme: cultural and digital literacy, cross-boundary collaboration and productive use of language technology, including post-editing machine translation. "
       f"Hold it at honours (FHEQ level 6, FQHEIS level 10) and cite it as {CITE}, para 1.31. Do not present it as a threshold standard or claim the issuer sets rules on generative AI here. "
       f"Set it beside 1.10.b3, 4.16.b2 and 4.16.b8 at threshold and qaa/fheq-2024/annex-d/transferable/r1/3rd."),
  aad=("Raise this when a student asks whether translation technology makes their skills redundant, or staff plan digital and teamwork content. "
       "Put it to a student as the value of judging and improving what machines produce, and to staff as a reason to teach post-editing and collaboration explicitly. "
       "Ask: How would you check a machine translation before you relied on it? Avoid suggesting that technology use replaces developing proficiency of their own."))

# ------------------------------------------------------------------ obliging or "will" paragraphs in sections 2 to 4
s('2.9', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='undergraduates on joint or combined degrees', addressee='learner',
  verbs=['achieve', 'add', 'explore'], about='joint and combined honours students', domain='subject-skill', award=HON,
  para='Undergraduates taking the subject within a joint or combined degree will reach the core of the specific and general skills set out, will gain others from their other subject or subjects and may explore where the subjects overlap.',
  prac='For joint and combined honours, students will achieve the core of the subject-specific and generic skills and will add others from the partner subject; the overlap offers room for interdisciplinary work.',
  ben='If you study languages alongside another subject, you will gain the core language and general skills, add others from your second subject and may explore where the two meet.',
  aaw=(f"Describe this as an expectation, stated with 'will', that joint and combined honours students reach the core of the subject's specific and generic skills, not every element. "
       f"It holds at FHEQ level 6 and FQHEIS level 10; cite it as {CITE}, para 2.9. Do not claim joint honours students meet the whole threshold list in 4.10 to 4.16, nor that the issuer defines which elements are core. "
       f"Set it beside 4.5 and 4.7 on the share of language study and 3.1 on content coverage."),
  aad=("Raise this when a joint honours student or programme team asks how much of the subject's standards apply to them. "
       "Explain to a student that they will build the core skills and add others from the second subject; to staff, that course documentation should make the core explicit. "
       "Ask: Which skills does your other subject add, and where do the two overlap? Avoid implying joint honours students fall short of single honours ones."))
s('2.19', type='expectation', rung='none', force='will', level='none', appliesTo='higher education providers', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award=HON,
  para='Providers will involve external reviewers in periodic review to get an outside view on changes and to make sure threshold standards are met and content suits the subject; externality is essential to UK quality assurance.',
  prac='In periodic review you will use external reviewers, both for an outside view on proposed changes and to confirm threshold standards are achieved and content fits the subject.',
  ben=('n/a', 'a duty on the provider in course review; the student meets its effect, not a standard to reach'),
  aaw=(f"Describe this as a provider expectation, stated with 'will', that periodic review uses external reviewers to confirm threshold standards and subject content. "
       f"It concerns review of honours provision, not a student outcome; cite it as {CITE}, para 2.19. Do not turn it into a learning outcome or claim it sets the review procedure. "
       f"Set it beside 2.18 and 2.20 on monitoring and external examining, and the threshold lists 4.10 to 4.16 that reviewers check."),
  aad=("Raise this with a programme team preparing for periodic review or appointing external reviewers. "
       "Frame it for staff as what the review has to show an outsider: that threshold standards are met and content fits the subject. "
       "Ask: Which external reviewer would see your language provision with fresh eyes, and what evidence of threshold standards will you give them? Avoid putting this to a student as something they must do."))
s('3.2', type='expectation', rung='none', force='describes', level='none', appliesTo='curriculum designers', addressee='provider',
  find='3.2 The content described in this section is intended as a framework for use by curriculum designers, rather than as a list of topics or skills that must be covered. Given the rapidly changing nature of languages and language uses, the evidence base for additional language learning and teaching, technological developments in language learning and use, and the reasons for learning and using languages, it is essential that curriculum designers remain open to new ideas for the content and design of their courses.',
  verbs=['remain'], about='content as a framework; designers stay open to change', domain='none', award=HON,
  para='The content section is a framework for designers, not a list that has to be covered; because languages, evidence, technology and motives for learning keep changing, designers are told it is essential to stay open to new content and design.',
  prac='Treat the content section as a framework rather than a syllabus, and keep your course content and design open to change as languages, the evidence base, technology and learners\' reasons for study move on.',
  ben=('n/a', 'addressed to curriculum designers, not a standard the student reaches'),
  aaw=(f"Describe this as guidance to curriculum designers, worded as 'essential' (outside the five force words, so recorded as describes), that the content section is a framework and courses should stay open to change. "
       f"It concerns honours course design; cite it as {CITE}, para 3.2. Do not claim the issuer lists required topics: it says the reverse, with 'must' negated. "
       f"Set it beside 3.3 and 3.4 on content and 4.8 on reading the standards with course documentation."),
  aad=("Raise this when a programme team treats the content section as a checklist or debates adding new content such as language technology. "
       "Frame it for staff as freedom and a duty to keep content current. "
       "Ask: What has changed in how your languages are used or learned since the course was last designed? Avoid presenting it to students or as a list to tick off."))
s('3.13', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  find='3.13 LCS courses explicitly require a measure of learner autonomy and responsibility for the development of linguistic proficiency through independent study. Guided independent study and research enable students to develop ideas beyond the classroom in a structured learning environment. They may be guided and developed alongside and beyond structured learning.',
  verbs=['require', 'enable', 'develop'], about='learner autonomy in developing proficiency', domain='generic-skill', award=HON,
  para='Courses require students to take some autonomy and responsibility for building their proficiency by studying on their own; guided self-study and research let ideas grow beyond the classroom in a structured setting.',
  prac='Your course requires students to take a share of responsibility for their own language development through independent study, supported by guided independent study and research within a structured environment.',
  ben='You must take some responsibility for your own language progress through independent study; guided study and research help you develop ideas beyond the classroom.',
  aaw=(f"Describe this as a requirement on students (the issuer says courses 'require' it, recorded as must): a measure of autonomy and responsibility for their own proficiency through independent study. "
       f"It applies through the honours course and refines the descriptor item on managing one's own learning (qaa/fheq-2024/4.15.b5) at FHEQ level 6; cite it as {CITE}, para 3.13. Do not claim it sets hours or a proportion of independent study. "
       f"Set it beside 1.11.b1 and 4.16.b7 at threshold and qaa/fheq-2024/annex-d/transferable/r3/3rd."),
  aad=("Raise this when a student relies wholly on class time or asks how to improve between lessons. "
       "Put it to a student as their own share of the work: progress in a language depends on what they do outside class. "
       "Ask: What do you do each week, outside class, to build your language, and is it enough? Avoid making it sound like the student is left without support."))
s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='readers judging achievement above threshold', addressee='provider',
  verbs=['perform', 'refer'], about='Annex D for achievement above threshold', domain='none', award=HON,
  para='Most students will perform well above the threshold; providers set their own evidence for this, and readers should refer to Annex D, which sets out the four honours classes for degrees at FHEQ level 6 and its Scottish equivalent, FQHEIS level 10.',
  prac='Expect most students to exceed the threshold; judge the higher classes by your own institutional method and refer to Annex D, which describes first, upper second, lower second and third class outcomes.',
  ben=('n/a', 'an instruction to readers judging classification, chiefly staff'),
  aaw=(f"Describe this as an instruction, stated with 'should', to refer to Annex D (qaa/fheq-2024/annex-d) for achievement above the threshold, because the statement sets no typical or excellent rung. "
       f"It holds for honours at FHEQ level 6 and FQHEIS level 10; cite it as {CITE}, para 4.2 (the issuer cites Annex D as QAA 2019, now within the FHEQ 2024). Do not invent typical or excellent standards for this subject. "
       f"Set it beside 4.1 and the classification bands in the FHEQ document (SL6, qaa/fheq-2024/annex-d/summary/r1/3rd and the bands above it)."),
  aad=("Raise this when staff ask how to describe a 2.1 or first in this subject, or a student asks what a good degree looks like. "
       "Frame it for staff as the route to classification descriptions; for a student, explain that the subject sets a minimum and the classes above it are described generically. "
       "Ask: What would distinguish an upper second from a lower second in your module's tasks? Avoid presenting the threshold lists as the description of a good degree."))
s('4.8', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='readers of the standards and course teams', addressee='provider',
  verbs=['prescribe', 'read'], about='standards read with course documentation', domain='none', award=HON,
  para='The standards set no curriculum; courses may weight the skills and knowledge differently or leave some out, so the standards must be read together with each course\'s documentation of its outcomes.',
  prac='The standards are not a curriculum: your course may weight the areas differently or omit some, so the standards must be read alongside your course documentation, which has to state its outcomes clearly.',
  ben=('n/a', 'an instruction to readers of the standards, chiefly course teams'),
  aaw=(f"Describe this as a requirement, stated with 'must', that the threshold standards are read with each course's own documentation, since courses may weight or omit areas. "
       f"It governs use of the honours standards at FHEQ level 6; cite it as {CITE}, para 4.8. Do not claim every course must teach every element of 4.10 to 4.16. "
       f"Set it beside 4.5, 4.7 and 4.9 on what shapes outcomes."),
  aad=("Raise this when a programme team maps its outcomes to the standards or an external examiner asks why an element is absent. "
       "Frame it for staff as the need for clear course documentation that explains the weighting. "
       "Ask: Where does your course documentation say which areas carry more or less weight, and why? Avoid giving this to a student as an obligation of theirs."))

# ------------------------------------------------------------------ threshold rung (4.10 to 4.16); 4.1 defines the rung as the minimum for the award
LT = dict(type='threshold', rung='threshold', force='threshold', level='fheq:6', appliesTo='graduates at the threshold', addressee='learner', award=HON)
def kt(i, **k): s(i, **LT, **k)
TB = 'By the end of your degree, as a minimum, '

# 4.10 language proficiency (towards or at CEFR C1)
C1 = '; the issuer allows "working towards" C1, depending on starting point'
kt('4.10.b1', verbs=['understand', 'recognise'], about='reading and listening to demanding long texts', domain='subject-skill',
   para='At threshold, will be able to follow a broad range of long, demanding texts and pick up what they imply as well as say, working towards or at CEFR C1.',
   prac='At threshold, graduates will be able to comprehend a wide variety of challenging, extended texts and grasp implicit meaning, working towards or at CEFR C1.',
   ben=TB + 'you will be able to understand long, challenging texts of many kinds and pick up meanings that are implied rather than stated.',
   aaw=aaw_thr('4.10, item 1', 'comprehension of long, demanding texts including implicit meaning, towards or at CEFR C1', '4.11 for cases where C1 is out of reach and qaa/fheq-2024/4.15.b1', C1),
   aad=aad_thr('a student asks what level of reading or listening they need by the end', 'Can you read a long article in your language and say what it hints at as well as what it states?'))
kt('4.10.b2', verbs=['express'], about='fluent spontaneous expression', domain='subject-skill',
   para='At threshold, will be able to speak and write fluently and spontaneously without obvious searching for words, towards or at CEFR C1.',
   prac='At threshold, graduates will be able to express themselves fluently and spontaneously, rarely needing to search for words.',
   ben=TB + 'you will be able to express yourself fluently and on the spot, without often having to hunt for the right words.',
   aaw=aaw_thr('4.10, item 2', 'fluent, spontaneous expression, towards or at CEFR C1', '4.10.b3, 4.16.b4 and qaa/fheq-2024/4.15.b8', C1),
   aad=aad_thr('a student worries about speaking without preparation', 'In an unplanned conversation, how often do you stop to search for a word?'))
kt('4.10.b3', verbs=['use'], about='flexible use across social, academic and work purposes', domain='subject-skill',
   para='At threshold, will be able to use the language flexibly and well for social, academic and professional ends.',
   prac='At threshold, graduates will be able to deploy the language flexibly and effectively across social, academic and professional settings.',
   ben=TB + 'you will be able to use your language flexibly and well in social life, in study and at work.',
   aaw=aaw_thr('4.10, item 3', 'flexible, effective use of the language across social, academic and professional purposes', '4.10.b2 and qaa/fheq-2024/4.15.b8', C1),
   aad=aad_thr('a student asks whether classroom language is enough for work or study abroad', 'Which setting, social, academic or work, do you find hardest to manage in the language?'))
kt('4.10.b4', verbs=['produce', 'showing'], about='clear, well-structured detailed writing', domain='subject-skill',
   para='At threshold, will be able to write clear, well-organised, detailed text on complex topics, with controlled use of structure, linking words and cohesion.',
   prac='At threshold, graduates will be able to produce clear, detailed, well-organised text on complex topics, controlling organisation, connectors and cohesion.',
   ben=TB + 'you will be able to write clear, well-organised, detailed pieces on complex topics, linking your ideas smoothly.',
   aaw=aaw_thr('4.10, item 4', 'clear, structured, detailed writing on complex subjects', '4.16.b6 and qaa/fheq-2024/4.15.b8', C1),
   aad=aad_thr('a student gets feedback on organisation or cohesion in written work', 'How do you signal to a reader how one paragraph links to the next?'))
kt('4.10.b5', verbs=['translate', 'capturing'], about='translating complex texts from the target language', domain='subject-skill',
   para='At threshold, will be able to translate complex texts on many general and specialist subjects out of the target language, conveying nuance and implication.',
   prac='At threshold, graduates will be able to translate complex general and specialist texts from the target language, rendering nuance and implication.',
   ben=TB + 'you will be able to translate complex texts on general and specialist topics out of the language you study, keeping their nuances and implications.',
   aaw=aaw_thr('4.10, item 5', 'translation of complex texts from the target language, keeping nuance', '4.15.b4 on mediation and qaa/fheq-2024/4.15.b2', C1 + '; the item names translation from, not into, the target language'),
   aad=aad_thr('a student prepares for translation assessment or asks about translation careers', 'When you translate, how do you check you have kept the tone and what is implied?'))

# 4.12 explicit knowledge of language
kt('4.12.b1', verbs=[], about='structures, registers and varieties of the language', domain='knowledge',
   para='At threshold, will show some knowledge and an aware understanding of how each studied language is structured and of its registers and varieties.',
   prac='At threshold, graduates will show awareness and some knowledge of the structure, the registers and the varieties of each studied language.',
   ben=TB + 'you will know about the structure of your language, its registers from formal to informal and its different varieties.',
   aaw=aaw_thr('4.12, item 1', 'awareness and some knowledge of the language\'s structures, registers and varieties', '4.12.b2 and qaa/fheq-2024/4.15.b1'),
   aad=aad_thr('a student asks why grammar or register is taught explicitly', 'Can you explain why a sentence would sound wrong in a formal letter but fine in a chat?'))
kt('4.12.b2', verbs=['encountered', 'used'], about='sociolinguistic contexts of registers and varieties', domain='understanding',
   para='At threshold, will show awareness, understanding and some knowledge of the social settings in which different registers and varieties are met and used.',
   prac='At threshold, graduates will show awareness and some knowledge of the sociolinguistic settings where registers and varieties occur.',
   ben=TB + 'you will understand the social settings where different registers and varieties of your language are heard and used.',
   aaw=aaw_thr('4.12, item 2', 'awareness and some knowledge of where registers and varieties occur socially', '4.12.b1, 4.14.b3 and qaa/fheq-2024/4.15.b1'),
   aad=aad_thr('a student meets a dialect or register they were not taught', 'Where would you expect to hear this variety, and who uses it?'))
kt('4.12.b3', verbs=['required', 'analyse'], about='linguistic principles for analysing the language', domain='understanding',
   find='the linguistic principles required to analyse the language(s) of study.',
   para='At threshold, will show awareness, understanding and some knowledge of the linguistic principles needed to analyse the language or languages studied.',
   prac='At threshold, graduates will show awareness and some knowledge of the linguistic principles used to analyse each studied language.',
   ben=TB + 'you will know the basic principles of linguistics you need to analyse how your language works.',
   aaw=aaw_thr('4.12, item 3', 'awareness and some knowledge of the linguistic principles for analysing the language', '4.12.b1 and qaa/fheq-2024/4.15.b2'),
   aad=aad_thr('a student asks why linguistics appears in a languages degree', 'Could you describe one pattern in your language using a linguistic term?'))

# 4.13 knowledge of cultures and societies, with 4.14 continuing the same lead-in
kt('4.13.b1', verbs=['enhanced'], about='knowledge of one or more cultures and societies', domain='knowledge',
   para='At threshold, will show knowledge and understanding of at least one culture and society, usually deepened by residence abroad or another immersive experience.',
   prac='At threshold, graduates will show knowledge and understanding of one or more cultures and societies, typically deepened by residence or an alternative immersive experience.',
   ben=TB + 'you will know and understand at least one culture and society linked to your language, usually deepened by time spent there or another immersive experience.',
   aaw=aaw_thr('4.13, item 1', 'knowledge of one or more cultures and societies, usually deepened by immersion', '1.21 and 3.19 on alternatives to residence abroad and qaa/fheq-2024/4.15.b1', '; residence abroad is typical, not required'),
   aad=aad_thr('a student cannot go abroad and asks whether that affects their degree', 'What have you learned about the culture through immersion, whether abroad or at home?'))
kt('4.13.b2', verbs=[], about='sociocultural and sociolinguistic norms in other cultures', domain='understanding',
   para='At threshold, will show awareness, understanding and knowledge of differing sociocultural and sociolinguistic perspectives and norms in other cultures and societies.',
   prac='At threshold, graduates will show knowledge and understanding of the varied sociocultural and sociolinguistic norms and viewpoints within other societies.',
   ben=TB + 'you will understand that other societies have their own social and language norms and that views differ within them too.',
   aaw=aaw_thr('4.13, item 2', 'knowledge of sociocultural and sociolinguistic norms and perspectives in other societies', '4.14.b3 and qaa/fheq-2024/4.15.b1'),
   aad=aad_thr('a student is surprised by a social norm abroad', 'What norm surprised you, and how do people within that culture disagree about it?'))
kt('4.13.b3', verbs=[], about='comparing other cultures with one\'s own', domain='understanding',
   para='At threshold, will show awareness, understanding and knowledge of how those cultures and societies resemble and differ from their own.',
   prac='At threshold, graduates will show understanding of the likenesses and differences between the cultures studied and their own.',
   ben=TB + 'you will be able to say how the cultures you study are like and unlike your own.',
   aaw=aaw_thr('4.13, item 3', 'knowledge of likeness and difference between studied cultures and one\'s own', '1.10.b7 and 4.14.b2'),
   aad=aad_thr('a student reflects on a placement or compares cultures in an essay', 'What is one way the culture you study is closer to yours than you expected?'))
FF = dict(forceFrom='4.13')
kt('4.14.b1', **FF, verbs=['deal', 'show'], about='respect for cultural diversity and difference', domain='subject-skill',
   para='At threshold, will be able to handle cultural diversity and difference with sensitivity and respect, open to varied perspectives and worldviews.',
   prac='At threshold, graduates will be able to engage sensitively and respectfully with cultural diversity and difference, showing openness to other worldviews.',
   ben=TB + 'you will be able to treat cultural differences with sensitivity and respect, staying open to other ways of seeing the world.',
   aaw=aaw_thr('4.14, item 1', 'sensitive, respectful engagement with cultural diversity', '1.10.b4 and qaa/fheq-2024/4.15.b9.1', '; 4.14 continues the 4.13 threshold lead-in'),
   aad=aad_thr('a student finds a cultural difference uncomfortable', 'What helped you stay open when a view clashed with your own?'))
kt('4.14.b2', **FF, verbs=['describe', 'evaluate', 'showing'], about='evaluating viewpoints and implicit values', domain='subject-skill',
   para='At threshold, will be able to describe and assess the views and practices of their own and other groups, aware of the hidden values behind judgements and prejudice.',
   prac='At threshold, graduates will be able to describe and judge the views and customs of their own social group and of others, aware of the implicit values beneath judgement and prejudice.',
   ben=TB + 'you will be able to describe and assess how your own group and others think and behave, and notice the hidden values behind judgements and prejudice.',
   aaw=aaw_thr('4.14, item 2', 'evaluating viewpoints and practices with awareness of implicit values', '4.13.b3 and qaa/fheq-2024/4.15.b7'),
   aad=aad_thr('a student discusses stereotypes or their own assumptions', 'Which assumption of your own did study or contact with another culture make you notice?'))
kt('4.14.b3', **FF, verbs=['identify', 'reflect', 'adjust'], about='adapting to sociolinguistic and pragmatic conventions', domain='subject-skill',
   para='At threshold, will be able to spot where sociolinguistic and pragmatic conventions differ, think about those differences and adapt their own communication.',
   prac='At threshold, graduates will be able to identify and reflect on differing sociolinguistic and pragmatic conventions and adapt how they communicate.',
   ben=TB + 'you will be able to notice when the social rules of talking differ, think about them and change how you communicate to fit.',
   aaw=aaw_thr('4.14, item 3', 'noticing and adapting to sociolinguistic and pragmatic conventions', '4.12.b2 and qaa/fheq-2024/4.15.b8'),
   aad=aad_thr('a student had a misunderstanding over politeness or directness', 'What did you change about how you spoke after that misunderstanding?'))
kt('4.14.b4', **FF, verbs=['explain', 'interpret', 'discuss'], about='discussing culture drawing on encounters and media', domain='subject-skill',
   para='At threshold, will be able to explain, interpret and discuss aspects of culture and its practices, drawing on intercultural encounters, reading, film, social media and the like.',
   prac='At threshold, graduates will be able to explain, interpret and discuss culture and cultural practice with reference to encounters, texts, film and social media.',
   ben=TB + 'you will be able to explain and discuss aspects of a culture using what you have met in person, read, watched or seen online.',
   aaw=aaw_thr('4.14, item 4', 'explaining and discussing culture with reference to encounters and media', '4.15.b2 and qaa/fheq-2024/4.15.b8'),
   aad=aad_thr('a student plans a presentation or reflective piece on culture', 'Which encounter or text best shows the cultural point you want to make?'))
kt('4.14.b5', **FF, verbs=['deal'], about='handling ambiguity across cultures', domain='subject-skill',
   para='At threshold, will be able to cope with ambiguity in communication across cultures.',
   prac='At threshold, graduates will be able to manage ambiguity in cross-cultural communication.',
   ben=TB + 'you will be able to cope when communication between cultures is unclear.',
   aaw=aaw_thr('4.14, item 5', 'handling ambiguity in cross-cultural communication', '1.10.b2 and the descriptor item qaa/fheq-2024/4.15.b4'),
   aad=aad_thr('a student is unsettled by uncertain meaning in another culture', 'When meaning was unclear, how did you check or clarify it?'))
kt('4.14.b6', **FF, verbs=['act', 'helping', 'interpreting', 'managing'], about='acting as an intercultural mediator', domain='subject-skill',
   find='act effectively as intercultural mediators, helping to maintain positive interaction by interpreting different perspectives and managing ambiguity.',
   para='At threshold, will be able to mediate effectively between cultures, keeping interaction positive by explaining differing views and handling ambiguity.',
   prac='At threshold, graduates will be able to mediate effectively between cultures, sustaining positive exchange by interpreting perspectives and managing ambiguity.',
   ben=TB + 'you will be able to act as a go-between for people from different cultures, keeping things positive by explaining each side\'s view and handling uncertainty.',
   aaw=aaw_thr('4.14, item 6', 'effective intercultural mediation', '4.15.b4, 1.29 and qaa/fheq-2024/4.15.b8'),
   aad=aad_thr('a student describes helping two people understand each other', 'What did you do to keep that exchange positive when the two sides misread each other?'))

# 4.15 subject-specific knowledge and skills
kt('4.15.b1', verbs=['demonstrate'], about='knowledge of the target societies', domain='knowledge',
   para='At threshold, will be able to show that they know and understand at least one area of the target societies, such as their literature, culture, linguistic setting, history, politics, geography or social and economic make-up.',
   prac='At threshold, graduates will be able to demonstrate knowledge and understanding of at least one aspect of the target societies: literature, culture, language setting, history, politics, geography or social and economic structure.',
   ben=TB + 'you will be able to show what you know about at least one area of the places where your language is spoken: literature, culture, history, politics, geography, society or economy.',
   aaw=aaw_thr('4.15, item 1', 'knowledge of one or more aspects of the target-language societies', '4.13.b1 and the descriptor item qaa/fheq-2024/4.15.b1', '; one aspect suffices, not all of those listed'),
   aad=aad_thr('a student asks how much content knowledge the degree expects', 'Which aspect of the society you study could you explain in depth?'))
kt('4.15.b2', verbs=['deploy', 'analyse', 'interpret'], about='critical methods for cultural materials', domain='subject-skill',
   para='At threshold, will be able to use a range of critical methods to analyse and interpret varied cultural materials, media and forms of communication.',
   prac='At threshold, graduates will be able to deploy several critical methods when analysing and interpreting a variety of cultural materials and media.',
   ben=TB + 'you will be able to use different critical approaches to analyse and interpret many kinds of cultural material and media.',
   aaw=aaw_thr('4.15, item 2', 'using critical methodologies on cultural materials and media', '1.10.b5 and qaa/fheq-2024/4.15.b2'),
   aad=aad_thr('a student plans a cultural analysis or chooses a theoretical approach', 'Which critical approach would you choose for this text, and why that one?'))
kt('4.15.b3', verbs=['account', 'exploited'], about='how language and image work in context', domain='subject-skill',
   para='At threshold, will be able to explain how words, images and other modes of communication are put to use in particular social and cultural settings and for particular ends.',
   prac='At threshold, graduates will be able to account for the ways language, images and other modes are exploited in given social and cultural contexts and for given purposes.',
   ben=TB + 'you will be able to explain how words, images and other forms of communication are used to particular effect in particular settings.',
   aaw=aaw_thr('4.15, item 3', 'accounting for how language and image are used in context and for purposes', '4.15.b2 and qaa/fheq-2024/4.15.b7'),
   aad=aad_thr('a student analyses an advert, speech or film', 'What effect is this image or phrase trying to have, and on whom?'))
kt('4.15.b4', verbs=['mediate', 'demonstrating'], about='mediating between languages', domain='subject-skill',
   para='At threshold, will be able to mediate between languages, showing cultural and plurilingual competence.',
   prac='At threshold, graduates will be able to mediate between languages with cultural and plurilingual competence.',
   ben=TB + 'you will be able to mediate between languages, showing you understand the cultures and can move between several languages.',
   aaw=aaw_thr('4.15, item 4', 'mediation between languages with cultural and plurilingual competence', '4.10.b5, 4.14.b6 and qaa/fheq-2024/4.15.b8'),
   aad=aad_thr('a student prepares for interpreting or mediation tasks', 'When you mediate, what do you change besides the words?'))
kt('4.15.b5', verbs=['contribute', 'drawing'], about='contributing to current debates', domain='subject-skill',
   find='contribute to contemporary debates by drawing on historical, comparative and global perspectives.',
   para='At threshold, will be able to take part in current debates, bringing historical, comparative and global perspectives to them.',
   prac='At threshold, graduates will be able to contribute to present-day debates using historical, comparative and global perspectives.',
   ben=TB + 'you will be able to join current debates, bringing in history, comparison and a global view.',
   aaw=aaw_thr('4.15, item 5', 'contributing to current debates from historical, comparative and global perspectives', '1.11.b12 and the descriptor item qaa/fheq-2024/4.15.b3.1'),
   aad=aad_thr('a student wants to connect their study to news or public debate', 'What would a historical or comparative view add to this current debate?'))

# 4.16 general and transferable skills (generic skills; each refines the FHEQ level 6 descriptor)
kt('4.16.b1', domain='generic-skill', verbs=['gather', 'process', 'evaluate'], about='evidence from sources in several languages',
   para='At threshold, will be able to collect, handle and assess evidence and information from varied sources in different languages.',
   prac='At threshold, graduates will be able to gather, process and evaluate evidence from a range of sources across languages.',
   ben=TB + 'you will be able to find, work through and judge evidence and information from many sources, in more than one language.',
   aaw=aaw_thr('4.16, item 1', 'gathering and evaluating evidence from sources in several languages (a generic skill refining FHEQ level 6)', '1.11.b4, qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/cognitive/r1/3rd'),
   aad=aad_thr('a student starts research using sources in the target language', 'How many of your sources are in the language you study, and how do you judge them?'))
kt('4.16.b2', domain='generic-skill', verbs=['make'], about='digital resources and information technology',
   para='At threshold, will be able to use digital resources and information technology appropriately to find information, communicate and support learning.',
   prac='At threshold, graduates will be able to make appropriate use of digital resources and IT for information, communication and learning.',
   ben=TB + 'you will be able to use digital resources and technology well to find information, communicate and help you learn.',
   aaw=aaw_thr('4.16, item 2', 'appropriate use of digital resources and IT (a generic skill refining FHEQ level 6)', '1.11.b11, 1.31 and qaa/fheq-2024/annex-d/transferable/r1/3rd'),
   aad=aad_thr('a student asks which digital skills matter or how to use online tools responsibly', 'Which digital resource helps your learning most, and how do you check it is reliable?'))
kt('4.16.b3', domain='generic-skill', verbs=['identify', 'analyse', 'work'], about='problem analysis and resolution',
   para='At threshold, will be able to recognise and analyse problems and move towards resolving them.',
   prac='At threshold, graduates will be able to identify and analyse problems and work towards solutions.',
   ben=TB + 'you will be able to spot and analyse problems and work towards solving them.',
   aaw=aaw_thr('4.16, item 3', 'identifying, analysing and working towards resolving problems (a generic skill refining FHEQ level 6)', '1.11.b5, qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r3/3rd'),
   aad=aad_thr('a student is stuck on a task or a placement problem', 'What exactly is the problem, and what is one step towards solving it?'))
kt('4.16.b4', domain='generic-skill', verbs=['communicate'], about='communicating information and arguments',
   para='At threshold, will be able to convey information, ideas and arguments in speech and writing and by non-verbal means.',
   prac='At threshold, graduates will be able to communicate information, ideas and arguments verbally and non-verbally.',
   ben=TB + 'you will be able to put across information, ideas and arguments in words and in other ways.',
   aaw=aaw_thr('4.16, item 4', 'communicating information, ideas and arguments (a generic skill refining FHEQ level 6)', '1.11.b7 and the descriptor item qaa/fheq-2024/4.15.b8'),
   aad=aad_thr('a student prepares a presentation or poster', 'How will your audience know your main argument within the first minute?'))
kt('4.16.b5', domain='generic-skill', verbs=['conduct', 'organise', 'conceptualise', 'formulate'], about='independent research and written argument',
   para='At threshold, will be able to carry out independent research, organise relevant material and develop ideas into a fitting written argument or response.',
   prac='At threshold, graduates will be able to conduct independent research, organise relevant material and conceptualise ideas into an appropriate written argument.',
   ben=TB + 'you will be able to research a topic on your own, organise what you find and shape your ideas into a sound written argument.',
   aaw=aaw_thr('4.16, item 5', 'independent research leading to a written argument (a generic skill refining FHEQ level 6)', '1.11.b6, qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/4.15.b6'),
   aad=aad_thr('a student begins a dissertation or extended essay', 'How will you turn your notes into a single argument?'))
kt('4.16.b6', domain='generic-skill', verbs=['present', 'demonstrates'], about='presenting formal written work',
   para='At threshold, will be able to present formal written work with careful attention to effective language, referencing and layout.',
   prac='At threshold, graduates will be able to present formal writing that shows attention to effective language, referencing and layout.',
   ben=TB + 'you will be able to present formal written work that is well written, properly referenced and well laid out.',
   aaw=aaw_thr('4.16, item 6', 'presenting formal written work with care for language, referencing and layout (a generic skill refining FHEQ level 6)', '4.10.b4 and qaa/fheq-2024/4.15.b8'),
   aad=aad_thr('a student receives feedback on presentation or referencing', 'What do you check before you submit a formal piece of writing?'))
kt('4.16.b7', domain='generic-skill', verbs=['demonstrate', 'learn', 'manage'], about='independent learning and time management',
   para='At threshold, will be able to show that they learn independently and manage their time well.',
   prac='At threshold, graduates will be able to demonstrate independent learning and effective time management.',
   ben=TB + 'you will be able to show that you can learn on your own and manage your time well.',
   aaw=aaw_thr('4.16, item 7', 'independent learning and time management (a generic skill refining FHEQ level 6)', '3.13, 1.11.b3, qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/transferable/r3/3rd'),
   aad=aad_thr('a student falls behind or plans independent study', 'How do you plan your independent study time, and does the plan hold?'))
kt('4.16.b8', domain='generic-skill', verbs=['work', 'framing', 'deciding', 'responding'], about='collaborative teamwork',
   para='At threshold, will be able to work in a team, framing joint tasks by agreeing aims, processes and steps, building ideas and solutions together and answering the strong and weak points of other arguments constructively.',
   prac='At threshold, graduates will be able to work as team members, framing shared tasks (aims, processes, steps), jointly building ideas and solutions and giving constructive responses to others\' arguments.',
   ben=TB + 'you will be able to work in a team: agreeing what you are aiming for and how, building ideas together and responding fairly to the strong and weak points in others\' arguments.',
   aaw=aaw_thr('4.16, item 8', 'collaborative teamwork that frames tasks and responds constructively (a generic skill refining FHEQ level 6)', '1.11.b2 and qaa/fheq-2024/annex-d/transferable/r2/3rd'),
   aad=aad_thr('a student is in a group project or a dispute within a group', 'How did your group agree its aims and steps, and how did you handle disagreement?'))
kt('4.16.b9', domain='generic-skill', verbs=['understand', 'apply'], about='academic integrity and ethics in their own work',
   para='At threshold, will be able to understand what academic integrity and ethics require and apply them to their own work, especially in reusing other people\'s research and writing.',
   prac='At threshold, graduates will be able to understand and apply academic integrity and ethics in their own work, notably when reusing others\' research and writing.',
   ben=TB + 'you will understand academic honesty and research ethics and apply them in your own work, especially whenever you use other people\'s research or writing.',
   aaw=aaw_thr('4.16, item 9', 'understanding and applying academic integrity and ethics (a generic skill refining FHEQ level 6)', '1.11.b10 and qaa/fheq-2024/4.15.b9.1', '; it does not rule on translation tools or generative AI'),
   aad=aad_thr('a student asks about referencing, translation software or reusing their own work', 'If you used a translation tool or someone else\'s idea, how would you acknowledge it?'))

GRADE = {}
TH = {'1.27': 'theme:enterprise', '1.29': 'theme:enterprise', '1.31': 'theme:enterprise', '1.11.b12': 'theme:esd'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.8; 4.2; 4.10'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.8; 4.2; 4.10 (as "FHEQIS Level 10")'),
                  dict(id='fheq:7', role='cites', locator='D1, 2.10 (integrated master\'s)'),
                  dict(id='fqheis:11', role='cites', locator='D1, 2.10 (integrated master\'s)')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.8; 4.10: degree with honours at FHEQ Level 6, FQHEIS Level 10); matches the FHEQ Table 1 (std:doc:qaa-fheq-2024-framework)'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.10: integrated master\'s); matches FHEQ 4.17 shared descriptor'),
                      dict(**{'from': 'fheq:6'}, to='spine:6', relation='equivalent', basis='inferred from the reference framework R2 (std:ref:uk-framework)')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.12', '1.13', '1.14', '1.15', '1.16', '1.17', '1.18', '3.20']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.13', '1.19', '1.20', '1.21', '3.20']),
      dict(id='theme:esd', role='carries', carriedIn=['1.11', '1.22', '1.23', '1.24', '1.25']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.26', '1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '3.21'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-languages-cultures-and-societies-2019-benchmarks (not yet ingested)', note='the closing page calls this the fifth edition; section 6 records the fourth (2019), third (2015) and, as Languages and Related Studies, 2007 and 2002'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree classification descriptions for FHEQ Level 6 and FQHEIS Level 10, cited as QAA 2019 (4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 6 and 7 (2.8, 2.10, 4.10)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 10 and 11 (2.8, 2.10, 4.2, 4.10)'),
      dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='QAA enterprise and entrepreneurship guidance (1.32; section 5)'),
      dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='Education for Sustainable Development Guidance, in the reference list only (section 5)'),
      dict(rel='refersTo', target='CEFR, Council of Europe 2020 (not ingested; Part E)', note='the proficiency scale for the threshold: C1, with B2 as the usual alternative (1.16, 4.3, 4.4, 4.10, 4.11)'),
      dict(rel='overlaps', target='std:doc:qaa-english-2023-benchmarks', note='shares common ground with English (1.6); inferred'),
      dict(rel='overlaps', target='std:doc:qaa-linguistics-2023-benchmarks', note='shares common ground with Linguistics, which covers TESOL (1.6); inferred'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance (not yet ingested)', note='front matter')]
S8 = {'published': '2023-03', 'lastReviewed': 'none-stated', 'reviewCycle': 'none-stated',
      'consultation': 'an advisory group of 22 named members drawn from universities, the Chartered Institute of Linguists and QAA, with GCHQ representatives (D1, section 6)', 'replacedBy': 'none'}

SB1 = [
    'The subject joins communicative proficiency in one or more languages with study of their linguistics, cultures and societies from many disciplinary angles; the languages range from global to regional, indigenous and minoritised, past and present (D1, 1.7).',
    'Immersive learning, physical or digital, in the target language and culture is a defining feature, often a year abroad, valued for language, cultural understanding and intercultural competence (D1, 1.8, 3.16).',
    'It is intercultural and transnational by nature: ideas and events crossing borders, relations between countries, the effect of communities abroad on identities at home (D1, 2.5, 2.6).',
    'Most students learn a language they do not yet command fully, and the language of study may also be a teaching medium, a gateway to the study of culture and society (D1, 2.1, 3.11).',
    'It draws critical methods from the humanities and social sciences and combines readily with other SHAPE subjects and with STEM (D1, 1.11, 2.3, 2.4, 3.11).',
    'It sets itself against Anglophone hegemony and native-speakerism, measuring proficiency by a framework such as the CEFR (D1, 1.16, 2.7).',
    'Language learning is intensive, needs regular contact with proficient users and authentic material and asks for learner autonomy (D1, 3.9, 3.10, 3.13).',
    'Graduates go on to many sectors, from diplomacy and policy to translation, education, media and business (D1, 1.9).',
]
SB2 = [
    dict(theme='theme:edi', inThisSubject='an outward-looking subject that values multilingualism, minority, sign and heritage languages, linguistic diversity beyond one standard form and rejects native-speakerism; it asks students to examine colonial and other injustices and prepares them for intolerance abroad (D1, 1.12 to 1.18)', statements=[]),
    dict(theme='theme:accessibility', inThisSubject='uneven access to languages before university, so courses take beginners and heritage speakers; barriers to placements abroad (money, visas, caring, disability) met by reasonable accommodation or other immersion; alternatives to live oral assessment (D1, 1.13, 1.19 to 1.21, 3.20)', statements=[]),
    dict(theme='theme:esd', inThisSubject='headed Sustainability: international perspectives on equality, peace and justice, four named UN goals (4, 5, 10, 16), climate and nature compared across cultures and the carbon cost of travel for placements (D1, 1.11, 1.22 to 1.25)', statements=['1.11.b12']),
    dict(theme='theme:enterprise', inThisSubject='curiosity, adaptability and resilience from engaging other cultures; placements as enterprise learning; graduates as sensitive communicators, collaborators and users of language technology; employability through varied assessment (D1, 1.26 to 1.32, 3.21)', statements=['1.27', '1.29', '1.31']),
]
SB3 = dict(
    areas=[dict(component='3.3', gloss='proficiency, linguistic and intercultural awareness, language and society, cultures and societies of the language'),
           dict(component='3.4', gloss='eight subject-specific skills from proficiency and mediation to comparative analysis and language technology'),
           dict(component='3.5', gloss='receiving, producing, interacting and mediating in the language; sensitivity to difference'),
           dict(component='3.6', gloss='creative, transactional and problem-solving communication skills')],
    practices=[dict(component='3.9', kind='teaching', gloss='intensive contact hours, more for beginners'),
               dict(component='3.10', kind='learning', gloss='contact with proficient users and authentic material'),
               dict(component='3.12', kind='learning', gloss='learning technology and online resources'),
               dict(component='3.13', kind='learning', gloss='learner autonomy and guided independent study'),
               dict(component='3.14', kind='teaching', gloss='methods for language skills: authentic material, explicit grammar, feedback, four skills, linguistic analysis, translation'),
               dict(component='3.15', kind='teaching', gloss='methods for culture and society: directed study, commentary, seminars, group work, dissertation'),
               dict(component='3.16', kind='learning', gloss='residence in a target-language country'),
               dict(component='3.18', kind='learning', gloss='what placements typically achieve'),
               dict(component='3.19', kind='learning', gloss='alternatives to residence abroad'),
               dict(component='3.20', kind='assessment', gloss='inclusive design; alternatives to live oral exams'),
               dict(component='3.22', kind='assessment', gloss='receptive, productive, interactive and mediation skills'),
               dict(component='3.23', kind='assessment', gloss='seventeen forms of proficiency assessment'),
               dict(component='3.24', kind='assessment', gloss='master\'s forms: dissertations, annotated translation, posters'),
               dict(component='3.25', kind='assessment', gloss='assessing in the target language'),
               dict(component='3.26', kind='assessment', gloss='nine forms for cultural, linguistic and social study')])
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.10; 4.12; 4.13 (continued by 4.14); 4.15; 4.16', award=HON, items=31),
           dict(rung='typical', leadIn='none', award=HON, items=0),
           dict(rung='excellent', leadIn='none', award=HON, items=0)],
    rungBases='4.1: the standards are the minimum a student will have shown at the honours award; 4.2: most students perform well above it, judged by each provider with Annex D. 4.5: the standards apply where languages are at least a third of study and studied in every year; 4.7: with a smaller share, not every element is expected. 4.11: where CEFR C1 is out of reach, B2 is the usual outcome.',
    outcomeLists=[dict(leadIn='1.10', gloss='profile of the typical graduate (no modal)', items=8, award=[HON]),
                  dict(leadIn='1.11', gloss='capabilities shared with SHAPE subjects (no modal)', items=12, award=[HON])],
    outcomes=[])
SB4A_FULL = []
SB5 = [dict(body='professional, statutory and regulatory bodies (PSRBs), none named', says='the statement supports PSRBs with the academic standards expected and their requirements may be other reference points; no body is named in the body of the text (D1, front matter)', requirements='not-applicable: no body named'),
       dict(body='Office for Students', says='in England these statements are not sector-recognised standards under its regulatory framework (D1, front matter)', requirements='not yet ingested (Part E)')]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.12', '1.13', '1.14', '1.15', '1.16', '1.17', '1.18', '3.20'], statements=[]),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['1.13', '1.19', '1.20', '1.21', '3.20'], statements=[]),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.11', '1.22', '1.23', '1.24', '1.25'], statements=['1.11.b12']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.26', '1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '3.21'], statements=['1.27', '1.29', '1.31'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.8', '2.10', '4.2', '4.10']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.8', '2.10', '4.2', '4.10']),
                dict(framework='other: CEFR (Council of Europe 2020), levels C1 Proficient User and B2 Independent User; no shared level id (Part E)', levels=[], citedIn=['1.16', '4.3', '4.4', '4.10', '4.11']),
                dict(framework='other: HSK proficiency test for Mandarin Chinese, named as an example (Part E)', levels=[], citedIn=['4.4'])],
    bodies=[dict(body='PSRBs, unnamed', citedIn=['front matter']),
            dict(body='Office for Students', citedIn=['front matter'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees (QAA 2019)', citedIn=['4.2'], role='describes the four honours classes, standing in for the typical and excellent rungs the statement does not set'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='the QAA enterprise and entrepreneurship guidance', citedIn=['1.32', 'section 5'], role='further reading on the enterprise theme'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='QAA and Advance HE (2021) Education for Sustainable Development Guidance', citedIn=['section 5'], role='reference list only'),
        dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='UN Sustainable Development Goals (external)', named="the UN's sustainable development goals", citedIn=['1.22', '1.23', 'section 5'], role='the frame of the sustainability theme; goals 4, 5, 10 and 16 named'),
        dict(document='CEFR (external; Part E)', named='Common European Framework of Reference for Languages: Learning, Teaching, Assessment (Council of Europe 2020)', citedIn=['1.16', '4.3', '4.10', '4.11', 'section 5'], role='the proficiency scale behind the threshold'),
        dict(document='British Academy reports (external)', named='Born Global (2016); Towards a national languages strategy (2020); SHAPE', citedIn=['1.9', '1.11', 'section 5'], role='evidence of the subject\'s value; the SHAPE grouping')])
B1 = [dict(slug='immersive-learning', definition='a physical placement or a digital space in which the student works mainly in the target language and culture (D1, 1.8)', beneficiaryDefinition='time, in person or online, when you live and work mostly in the language you are learning', scopeNote='includes the year abroad and in-country or virtual alternatives (1.21, 3.19)', category='unknown', practices=['education']),
      dict(slug='year-abroad', definition='a full academic year of placement in a target-language setting (D1, 1.8)', beneficiaryDefinition='a year spent studying or working in a country where your language is used', scopeNote='one form of immersive placement', category='unknown', practices=['education']),
      dict(slug='native-speakerism', definition='an exclusionary assumption that ties language ability to ethnicity or nationality instead of measured proficiency (D1, 1.16)', beneficiaryDefinition='the mistaken idea that only people born into a language can be truly good at it', scopeNote='rejected in favour of framework-based measures such as the CEFR', category='unknown', practices=['education']),
      dict(slug='shape-subjects', definition='the social sciences, humanities and arts grouped as Social Sciences, Humanities and the Arts for People and the Economy (D1, 1.11)', beneficiaryDefinition='the arts, humanities and social science subjects taken as one group', scopeNote='the British Academy\'s grouping (section 5)', category='unknown', practices=['education']),
      dict(slug='threshold-standard', definition='the minimum a student will have shown when awarded the honours degree (D1, 4.1)', beneficiaryDefinition='the minimum you must reach to be awarded the degree', scopeNote='the only rung this statement sets; higher achievement is left to Annex D (4.2)', category='unknown', practices=['education'])]
B2A = [dict(concept='immersive-learning', form='immersive learning', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='year-abroad', form='year abroad', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='informal'),
       dict(concept='native-speakerism', form='native-speakerism', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
       dict(concept='shape-subjects', form='SHAPE', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='minimum threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []; B5 = []
D3 = [dict(citation='Council of Europe (2020) Common European Framework of Reference for Languages: Learning, Teaching, Assessment, Companion Volume', settles=['SB6', 'S7', 'S4 4.10 and 4.11 levels'], asked='2026-10-03', state='wanted')]

E = [
    'SB4, rungs: threshold only. Five lead-ins (4.10, 4.12, 4.13, 4.15, 4.16) under one heading, "Standard of achievement at threshold level"; 4.14 ("They are also able to") continues 4.13 and is recorded as threshold with forceFrom 4.13. No typical or excellent lists: 4.2 sends readers to Annex D for the classes above. No gradeOf links.',
    'S4, force: threshold items take force threshold, since 4.1 defines the standards as the minimum for the honours award; lead-in wordings differ ("are able to", "demonstrate awareness, understanding and some knowledge of", "demonstrate competence in").',
    'S4, 4.10: the lead-in sets proficiency as "working towards or operating at level C1 of the CEFR", depending on starting point; 4.11 allows B2 as the usual outcome where C1 is not achievable (no placement, distant languages for European students, oral cultures, sign languages). 4.11 is not taken as a statement: its "typical outcome" is not the typical rung, and "expected to reach" is outside the five force words. For Abbott.',
    'S5: 4.10 writes "FHEQIS Level 10", the issuer\'s slip for FQHEIS; recorded as fqheis:10.',
    'S5, SB6: the CEFR (C1, B2) and HSK are proficiency scales with no shared level id; recorded by name only. Whether CEFR levels should become shared ids (for languages benchmarks and others) is for Abbott.',
    'S4, outcome lists in section 1: 1.10 ("Graduates of LCS degrees typically:") and 1.11 ("LCS graduates also develop ... the ability to:") have no modal in the lead-in; recorded as outcome lists, force describes. Their "typically" is a graduate profile, not the typical rung. For Abbott at P3: are these statements or descriptive components?',
    'S4, paragraphs with "are able to" in the enterprise section (1.27, 1.29, 1.31) taken as outcome statements, force will; 1.30 ("Where students have the opportunity ... they are able to apply") left as a component because its outcome depends on an optional study route; 1.3 (elective language students "will also ... develop some of the skills") left out as it concerns students of other subjects.',
    'S4, hedged "will": "will typically" and "will normally" read as descriptions, not standards: 3.1 (single honours graduates "will normally experience all of the content"), 3.3 ("will typically include"), 3.9, 3.18 (placements "will typically" do five things), 2.20 (external examiners "will be asked"); 1.25 ("will increasingly require reflection") is predictive. Not statements. 2.9 and 2.19 use plain "will" and are taken. For Abbott.',
    'S4, obliging words outside the five: 3.2 "it is essential that curriculum designers remain open" (taken, force describes; its "must" is negated: "rather than ... that must be covered"); 3.21 "an essential element" and 3.20 "Fundamental to the design of assessment" (descriptive, not taken); 2.8 "it is expected that each level would see ..." and "it would be expected that a student ... would be capable of ... postgraduate study" (not taken, as in Psychology 3.27). For Abbott.',
    'S4, 3.13: "courses explicitly require a measure of learner autonomy" recorded as must (required is must), addressed to the learner; domain generic-skill at fheq:6 though it applies through the course.',
    'S4, plain-present provider norms not taken (template open point 5): 2.11 (progression features), 3.4 (eight subject-specific skills that "courses develop"), 3.14, 3.15, 3.22, 3.23, 3.24, 3.26 (methods and forms of assessment), 4.5 and 4.9. 3.4 is the subject\'s skills list in all but form; for Abbott whether it should be an outcome list.',
    'S4, 1.20: the skeleton flagged "should" in "the belief that languages should be for all"; a stated value, not an obligation. Not taken.',
    'S4, domains: provider statements 2.19, 3.2, 4.2 and 4.8 carry domain none (no learner outcome); 2.9 carries subject-skill though it covers both specific and generic skills.',
    'S4, skeleton spans: 1.11.b12, 3.2, 3.13, 4.12.b3, 4.14.b6 and 4.15.b5 trimmed with find, because the skeleton ran each span into the next sub-heading.',
    'S3: the skeleton\'s cross-cutting hits sit one paragraph early in places (for example EDI at 1.11, where the heading ends 1.11\'s span); themes judged from the text.',
    'S2, subjects: the text names no HECoS or CAH codes. modern languages (100329) is entered as stated from "Modern Languages" (4.6) and translation studies (101130) from "translation and interpreting" (1.4); CAH19-04-09, CAH19-04 and CAH19 are inferred parents; Celtic studies (101118) and British Sign Language studies (100317) are inferred from the mention of Celtic languages (1.8) and sign languages (1.14, 4.11). All inferred codes held back until P3.',
    'S2, awards: the statement covers master\'s provision (1.1, 1.4, 2.2, 3.24) and names integrated master\'s at FHEQ 7 / FQHEIS 11 (2.10) but sets no master\'s standards; awardsCovered is honours only. In Scotland the honours degree is a Master of Arts (1.1), still at FQHEIS 10.',
    'SB5: no professional body is named in the body of the text; the Chartered Institute of Linguists and GCHQ appear only among advisory group members (section 6). The Office for Students\' framework is not yet ingested.',
    'SB6: the ESD guidance and the UN goals and CEFR also appear in section 5, which is excluded matter; listed with "section 5" in citedIn.',
    'Generative AI: not named; 1.31 (reviewing machine translation output) and 3.23 (post-editing translations produced by language technology tools) touch language technology only, so no theme:generative-ai tag.',
    'S1, licence: the text gives a copyright notice and no re-use terms; QAA\'s terms for holding and chunking are to check.',
    'S9: not researched in P1.',
    'Patterns differing from Psychology: threshold only, with no typical or excellent lists; the threshold split under five sub-headings with differing lead-in wordings and one continuation (4.14); proficiency stated against an external scale (CEFR C1, B2 fallback); the standards limited to courses with at least a third of language study (4.5); no PSRB; outcome lists in section 1 with no modal; master\'s provision described without standards.',
]
