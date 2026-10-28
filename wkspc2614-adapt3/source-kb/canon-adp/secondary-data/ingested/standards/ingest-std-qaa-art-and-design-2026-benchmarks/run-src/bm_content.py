# Judgement fields for run 0088, QAA Art and Design 2026 (std). Keys are S4 ids under qaa/art-and-design-2026/.
# Built by tools/bm_build.py art-and-design-2026 --check. Written fresh from the held text alone (benchmark rule 6).
HON = "bachelor's with honours"
MA = "master's"
IM = "integrated master's"
SID = 'qaa/art-and-design-2026'
CITE = 'QAA, 2026, Art and Design Subject Benchmark Statement'

META = dict(
    run='0088', p1='2026-10-03 16:31',
    title='Subject Benchmark Statement Art and Design',
    heading='Subject Benchmark Statement: Art and Design (QAA, April 2026)',
    edition='April 2026 (fifth edition)', published='2026-04',
    status='current',
    supersedes='the fourth edition, 2019 (a minor update of the 2016 statement) (D1, back matter)',
    subjects=[
        dict(scheme='hecos', code='101361', label='creative arts and design', basis='inferred'),
        dict(scheme='hecos', code='100059', label='fine art', basis='inferred'),
        dict(scheme='hecos', code='100048', label='design', basis='inferred'),
        dict(scheme='cah', code='CAH25-01-01', label='creative arts and design (non-specific)', basis='inferred'),
        dict(scheme='cah', code='CAH25-01-02', label='art', basis='inferred'),
        dict(scheme='cah', code='CAH25-01-03', label='design studies', basis='inferred'),
    ],
    awards=[HON, MA, IM],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2026 revision (fifth edition for Art and Design)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing (front matter; 1.2; 3.31)',
    agentDefinition=("QAA's UK reference point for what a graduate in Art and Design should know, do and understand at the end of an "
                     "honours degree, with a short set of master's outcomes: one table of fourteen attributes, each described at three "
                     "rungs (threshold, typical, excellent), and twelve outcomes master's graduates typically reach. Reach for it when "
                     "designing, reviewing or describing an art or design course, its modules or its outcomes. It is not a curriculum, "
                     "not a professional body's accreditation standard and, in England, not a sector-recognised standard."),
    summary=("Published by QAA in April 2026 as the fifth edition, the statement describes Art and Design as a practice-based, "
             "student-centred subject of making and creative inquiry; sets out five cross-cutting themes (equity, diversity and "
             "inclusion; accessibility and the needs of disabled students; education for sustainable development; employability, "
             "entrepreneurship and enterprise education; generative AI); covers course design, progression, flexibility, "
             "partnership and review, and the content, teaching, assessment and feedback of a course; and gives benchmark "
             "standards as one table (Table 1) of fourteen attributes at threshold, typical and excellent for bachelor's degrees "
             "with honours, a master's list in 4.7 and a note on integrated master's. It points to Annex D of the 2024 Frameworks "
             "for the degree classes, cites the FHEQ and FQHEIS levels, and names PSRBs, two accrediting bodies and three "
             "non-accrediting professional bodies."),
    authority=("reference: a sector-owned reference point, not a regulatory requirement; in England not a sector-recognised "
               "standard under the OfS framework; part of the quality arrangements in Scotland, Wales and Northern Ireland "
               "(D1, front matter: Relationship to legislation)"),
)

S2 = dict(
    governs=("what an Art and Design graduate can be expected to know, do and understand at the end of their studies, and the "
             "nature and characteristics of awards in the subject (D1, front matter: About this Statement; 4.1)"),
    awards=["bachelor's degrees with honours (single honours, joint and combined)", "master's degrees (taught postgraduate)",
            "integrated master's degrees (4.8)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    statedScope=('"This QAA Subject Benchmark Statement for Art and Design defines what can be expected of a graduate in terms '
                 'of what they might know, do and understand at the end of their studies." (D1, front matter: About this Statement)'),
    statedSubjects=[
        dict(name='Art and Design', locator='(D1, title; 1.2)', kind='subject',
             codes=[dict(scheme='hecos', code='101361', label='creative arts and design'),
                    dict(scheme='cah', code='CAH25-01-01', label='creative arts and design (non-specific)')]),
        dict(name='single honours award or part of a broader interdisciplinary degree', locator='(D1, 2.10)', kind='programme title',
             codes=[dict(scheme='hecos', code='101361', label='creative arts and design')]),
        dict(name='combined or joint degree, including major and minor options', locator='(D1, 2.14)', kind='programme title',
             codes=[dict(scheme='hecos', code='101361', label='creative arts and design')]),
        dict(name='product design', locator='(D1, 2.23)', kind='specialism',
             codes=[dict(scheme='hecos', code='100050', label='product design')]),
    ],
)

SECTIONS = {'1': 'Context and purposes of an Art and Design degree', '2': 'Distinctive features of Art and Design',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.3', 'Context and purposes of an Art and Design degree'),
       ('1.4', '1.9', 'Purposes and characteristics of an Art and Design degree'),
       ('1.10', '1.16', 'Equity, diversity and inclusion'),
       ('1.17', '1.24', 'Accessibility and the needs of disabled students'),
       ('1.25', '1.33', 'Education for sustainable development'),
       ('1.34', '1.40', 'Employability, entrepreneurship and enterprise education'),
       ('1.41', '1.50', 'Generative artificial intelligence (GenAI)'),
       ('2.1', '2.11', 'Design'), ('2.12', '2.15', 'Progression'), ('2.16', '2.20', 'Flexibility'),
       ('2.21', '2.23', 'Partnership'), ('2.24', '2.28', 'Monitoring and review'),
       ('3.1', '3.1', 'Content, structure and delivery'), ('3.2', '3.4', 'Content'), ('3.5', '3.16', 'Teaching and learning'),
       ('3.17', '3.17', 'Assessment and feedback'), ('3.18', '3.25', 'Assessment'), ('3.26', '3.32', 'Feedback'),
       ('4.1', '4.3', 'Introduction'), ('4.4', '4.4', 'Undergraduate degrees: threshold, typical and excellent standards'),
       ('4.5', '4.7', 'Postgraduate degrees'), ('4.8', '4.8', "Integrated master's")]

G = {
    '1.1': 'the subject amid technological and cultural change', '1.2': "'subject' and 'disciplines' defined",
    '1.3': 'room for providers to weight the subject locally', '1.4': 'breadth of disciplines; practice-based pedagogy',
    '1.5': 'conceiving, testing, making and sharing work', '1.6': 'visual, spatial and sensory languages; wider value',
    '1.7': 'studios, workshops and flexible study modes', '1.8': 'links with other subjects and sectors',
    '1.9': 'graduate resourcefulness and careers', '1.10': 'diverse practices; reflexivity and individual voice',
    '1.11': 'national access and equality policies by nation', '1.12': 'values of an inclusive learning community',
    '1.13': 'legacies of exclusion and how they are countered', '1.14': 'inclusion across the student life cycle',
    '1.15': 'inclusive practice as a source of innovation', '1.16': 'dialogue and co-created curriculum',
    '1.17': 'accessibility as a core value; disabled and neurodiverse students', '1.18': 'open admissions; portfolio entry',
    '1.19': 'reasonable and anticipatory adjustments', '1.20': 'accessible live learning activities',
    '1.21': 'accessible studios; quiet areas', '1.22': 'hybrid learning and its limits for access',
    '1.23': 'making as evidence of learning', '1.24': 'flexible assessment formats',
    '1.25': 'sustainable development and its reference points', '1.26': 'core skills for sustainability; climate literacy',
    '1.27': 'creative pedagogies for linked global challenges', '1.28': 'regenerative creative practice',
    '1.29': 'industry partnerships for sustainability', '1.30': 'working with STEM and other fields on global issues',
    '1.31': 'tools for sustainability awareness', '1.32': 'sustainability, inclusion and ethics in curricula',
    '1.33': 'responsible digital practice', '1.34': 'the value graduates create through careers',
    '1.35': 'technical, entrepreneurial and emotional capacities', '1.36': 'enterprise education and IP-led businesses',
    '1.37': 'agility for changing creative careers', '1.38': 'practice-based and experiential learning',
    '1.39': 'interpersonal and leadership competences', '1.40': 'skills for creative economies (a list of thirteen)',
    '1.41': 'the subject and emerging technologies', '1.42': 'GenAI literacies and ethics',
    '1.43': 'a spectrum of GenAI use; own position', '1.44': 'GenAI as one tool among many',
    '1.45': 'authentic assessment including GenAI', '1.46': 'agency and authorship with GenAI',
    '1.47': 'GenAI and creative labour', '1.48': 'bias in GenAI and cultural visibility',
    '1.49': 'environmental cost of GenAI', '1.50': 'intellectual property and GenAI',
    '2.1': 'a spectrum of practices and theories', '2.2': 'course design models and reference points',
    '2.3': 'disciplinary or flexible curricula', '2.4': 'interdisciplinary and specialist courses',
    '2.5': 'learning through making and change-making', '2.6': 'student-centred experiential learning',
    '2.7': 'live and inquiry-led learning', '2.8': 'varied assessment', '2.9': 'contextual and critical awareness',
    '2.10': 'undergraduate study: single and combined', '2.11': 'diverse postgraduate provision',
    '2.12': 'progression across levels to the threshold', '2.13': 'readiness for postgraduate study',
    '2.14': 'joint and combined degrees', '2.15': 'exit awards', '2.16': 'duration in England, Wales and Northern Ireland',
    '2.17': 'Scottish degrees and levels', '2.18': "integrated master's length and levels", '2.19': 'part-time routes',
    '2.20': 'modes, formats and credit', '2.21': 'validation, franchising and apprenticeships',
    '2.22': 'commercial practice through partnership', '2.23': 'accreditation and professional bodies',
    '2.24': 'monitoring and periodic review', '2.25': 'externality in review', '2.26': 'external examiners in studios',
    '2.27': "external examiners' role and reports", '2.28': 'professional and regulatory accreditation',
    '3.1': 'what the section covers', '3.2': 'curricula responding to change', '3.3': 'four typical areas of study',
    '3.4': 'aims of courses', '3.5': 'range of teaching and learning methods', '3.6': 'studio, lecture and project learning',
    '3.7': 'learning resources and technical staff', '3.8': 'scheduled and independent learning',
    '3.9': 'module outcomes building across levels', '3.10': 'student-centred pedagogy',
    '3.11': 'discursive subject learning', '3.12': 'staff practice, scholarship and CPD',
    '3.13': 'in-person and online delivery', '3.14': 'group work and employability',
    '3.15': 'interdisciplinary collaboration', '3.16': 'industry and enterprise activities',
    '3.17': 'why assessment and feedback matter', '3.18': 'diverse, inclusive assessment',
    '3.19': 'holistic assessment of a submission', '3.20': 'co-designed assessment',
    '3.21': 'assessing process and product', '3.22': 'assessment in professional settings',
    '3.23': 'self and peer assessment', '3.24': 'new forms of assessment; integrity',
    '3.25': 'assessment methods (a list of fourteen)', '3.26': 'feedback as part of learning',
    '3.27': 'continuous feedback', '3.28': 'formal and informal feedback settings', '3.29': 'situational feedback',
    '3.30': 'feedback co-constructed with students', '3.31': "the 'crit' and inclusive review",
    '3.32': 'formats of feedback', '4.1': 'what the standards are', '4.2': 'most exceed threshold; Annex D',
    '4.3': 'competence standards and the Equality Act', '4.4': 'Table 1: fourteen attributes at three rungs',
    '4.5': "master's beyond the honours standards", '4.6': 'kinds of postgraduate course',
    '4.7': "outcomes for master's graduates (a list of twelve)", '4.8': "integrated master's at level 7",
}

CTYPE = {'3.2': 'area', '3.3': 'area', '3.4': 'area',
         '3.5': 'practice', '3.6': 'practice', '3.8': 'practice', '3.10': 'practice', '3.11': 'practice',
         '3.13': 'practice', '3.14': 'practice', '3.15': 'practice', '3.16': 'practice',
         '3.18': 'practice', '3.19': 'practice', '3.20': 'practice', '3.21': 'practice', '3.22': 'practice',
         '3.23': 'practice', '3.24': 'practice', '3.25': 'practice', '3.26': 'practice', '3.27': 'practice',
         '3.28': 'practice', '3.29': 'practice', '3.30': 'practice', '3.31': 'practice', '3.32': 'practice'}

EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and Part B'),
    dict(number='none', heading='section heading lines 1 to 4', kind='other: headings, recorded in S3 as sections'),
    dict(number='5', heading='Membership of the Advisory Group (2026, 2019, 2016, 2008, 2002)', kind='other: back matter, read for S8 and supersedes'),
]

P = {}
def s(i, **k):
    P[i] = k

# ---------------------------------------------------------------- obliging and expected-outcome paragraphs
s('1.19', type='requirement', rung='none', force='must', level='none', appliesTo='higher education providers offering the subject',
  addressee='provider', verbs=['make', 'support', 'ensure', 'required'], about='reasonable and anticipatory adjustments for disabled students',
  domain='none', award='none',
  para=("Under the Equality Act 2010 providers must adjust reasonably so disabled students take a full part in academic life; in this "
        "subject that means flexible materials and structures, adjustments made in advance, and adjustments in group and collaborative work."),
  prac=("Plan adjustments before they are asked for: providers must make reasonable adjustments under the Equality Act 2010, and here that "
        "means briefs shared early, other formats for lectures and content, one-to-one help or specialist kit, and adjustments for group work."),
  ben=('n/a', 'a legal duty on the provider; the student meets its effect, not a standard to reach'),
  aaw=("Describe this as a legal duty on the provider under the Equality Act 2010, carried in the accessibility theme, not as a learning "
       f"outcome or a level-bound standard. Cite it as ({CITE}, para 1.19) and name the Act as the source of the duty. Do not present the "
       "statement itself as the regulation, and do not turn it into a student outcome. Set it beside paras 1.17 to 1.24 and the "
       f"inclusive-assessment practices in 3.18 to 3.20 ({SID}/1.19 is the only obliging record in the theme)."),
  aad=("Raise it with a programme team planning studios, group projects or assessment, or with a teacher asked about a disabled "
       "student's access. Frame it for staff as an anticipatory duty: what is in place before anyone asks. Ask: 'Which adjustments for "
       "group and studio work are ready now, and which wait for a request?' Do not put this duty to a student as something they must show."))

s('2.12', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on an honours or integrated master\'s course',
  addressee='learner', verbs=['progress'], about='progression across levels towards the threshold skills', domain='none', award=[HON, IM],
  para=("An Art and Design student will move from level to level under each institution's rules, each level adding knowledge, expertise "
        "and experience towards meeting the threshold (and any higher) subject and generic skills, usually by passing and gaining credit "
        "for all learning and assessment, practical work included."),
  prac=("Map each level so that it builds towards the threshold skills in Table 1: students will progress level by level under your "
        "regulations, normally by passing and earning credit for every part of the course, practical components included."),
  ben=("You will move up one level at a time, each year adding knowledge, expertise and experience that build towards the subject and "
       "general skills expected at the end; usually that means passing and earning credit for all your learning and assessment, "
       "practical work included."),
  aaw=("Describe this as an expectation of progression (force: will) across an honours degree at FHEQ Level 6 (FQHEIS Level 10) or an "
       f"integrated master's at FHEQ Level 7 (FQHEIS Level 11). Cite it as ({CITE}, para 2.12). Do not claim it fixes progression rules, "
       "which stay with each institution. Set it beside Table 1's threshold cells (for example "
       f"{SID}/4.4.b1) and the FHEQ descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1, with spine:6 and spine:7."),
  aad=("Raise it when a student asks what each year is for or a team is mapping modules across levels. Tell a student plainly that each "
       "level builds towards the skills expected at the end; frame it for staff as a check on level-by-level design. Ask: 'What does "
       "this year add that you will need by the final year?' Avoid presenting the higher rungs as what every student must reach."))

s('2.14', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students taking the subject in a joint or combined degree',
  addressee='learner', verbs=['achieve', 'add'], about='joint and combined degrees', domain='none', award=HON,
  para=("Students who take Art and Design within a joint or combined degree, major and minor included, will reach the core of the subject "
        "and generic skills set out here and will add others from their other subject; they may also work where the disciplines overlap."),
  prac=("In a joint or combined course, students will meet the core subject and generic skills of this statement and add skills from the "
        "partner subject; design the course so the overlap between the two can be explored."),
  ben=("If you study the subject alongside another in a joint or combined degree, you will reach the core subject and general skills "
       "and add others from your second subject, with chances to explore where the two meet."),
  aaw=("Describe this as an expectation (force: will) for joint and combined honours at FHEQ Level 6 (FQHEIS Level 10): the core of the "
       f"subject and generic skills is met, not the whole. Cite it as ({CITE}, para 2.14). Do not claim a joint student meets every cell "
       "of Table 1 in full, or that the statement says which cells are core. Set it beside Table 1 (para 4.4), para 2.10 and the "
       "FHEQ honours descriptor qaa/fheq-2024/4.15.b1."),
  aad=("Raise it with a student on a joint or major and minor route, or a team designing one. Tell the student plainly that they cover "
       "the core of this subject and gain other skills from the second; with staff, ask which cells the course treats as core. Ask: "
       "'Where do your two subjects meet in your own work?' Avoid suggesting the student is held to the full single honours set."))

s('2.24', type='expectation', rung='none', force='will', level='none', appliesTo='degree-awarding bodies and their partners',
  addressee='provider', verbs=['form'], about='student voice in monitoring and review', domain='none', award='none',
  para=("Degree-awarding bodies and their partners collect and analyse information and review courses periodically to their own needs; "
        "taking account of what students say will form part of this, alongside external reference points such as this statement."),
  prac=("In monitoring and periodic review, students' views will form part of the evidence, read with external reference points "
        "including this statement."),
  ben=('n/a', 'a duty on the awarding body in its review process'),
  aaw=(f"Describe this as a provider expectation (force: will) about course review, holding at every level. Cite it as ({CITE}, para 2.24). "
       "Do not present it as a learning outcome or as a regulatory rule. Set it beside para 2.25 (externality, "
       f"{SID}/2.25) and the review role of external examiners in paras 2.26 and 2.27."),
  aad=("Raise it with a programme team preparing a periodic review or annual monitoring. Frame it for staff: how students' views enter "
       "the evidence. Ask: 'Where in the review do students' own accounts change a decision?' Do not give this to a student as a "
       "standard; with a student, at most explain that their views count in review."))

s('2.25', type='expectation', rung='none', force='will', level='none', appliesTo='higher education providers',
  addressee='provider', verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award='none',
  para=("Externality is essential to UK quality assurance: providers will bring in external reviewers in periodic review, for an "
        "independent view of proposed changes and to make sure threshold standards are met and the content suits the subject."),
  prac=("Bring external reviewers into periodic review: they will give an independent view of changes and check that threshold standards "
        "are reached and content fits the subject."),
  ben=('n/a', 'a duty on the provider in periodic review'),
  aaw=(f"Describe this as a provider expectation (force: will) about externality in periodic review. Cite it as ({CITE}, para 2.25). Do "
       "not claim it sets the threshold standards themselves, which are in Table 1. Set it beside para 2.24 "
       f"({SID}/2.24), paras 2.26 and 2.27 on external examiners, and Table 1's threshold cells."),
  aad=("Raise it with a team planning a periodic review or choosing reviewers. Frame it for staff as the independent check on threshold "
       "standards and fit with the subject. Ask: 'Who outside the provider will look at this change, and what will they test it against?' "
       "Do not present it to a student as their responsibility."))

s('4.2', type='requirement', rung='none', force='should', level='fheq:6', appliesTo='higher education providers awarding honours',
  addressee='provider', verbs=['refer'], about='Annex D for evidence of classification', domain='none', award=HON,
  para=("Most students will perform well above the minimum; each provider decides what counts as evidence of that and should consult "
        "Annex D of the 2024 Frameworks, which describes the four honours classes."),
  prac=("Most students will go well beyond threshold. When deciding what evidence shows achievement, providers should use Annex D's "
        "descriptions of the first, upper second, lower second and third classes."),
  ben=('n/a', 'a duty on the provider in classifying degrees'),
  aaw=("Describe this as a provider recommendation (force: should) to use Annex D when judging achievement above threshold, at FHEQ Level "
       f"6 (FQHEIS Level 10) for honours. Cite it as ({CITE}, para 4.2) and Annex D as std:doc:qaa-fheq-2024-framework. Do not map "
       "Table 1's typical or excellent rungs onto a degree class: the statement does not. Set it beside qaa/fheq-2024/annex-d/summary/r1/3rd "
       "and the other Annex D summary rows."),
  aad=("Raise it with a team writing marking criteria or a classification policy. Frame it for staff: the subject's rungs describe "
       "attainment, while Annex D describes the classes. Ask: 'How do your criteria for a 2.1 relate to the typical cells?' Do not put "
       "this to a student as a rule they follow."))

s('4.3', type='requirement', rung='none', force='should', level='none', appliesTo='providers who develop competence standards',
  addressee='provider', verbs=['follow'], about='competence standards and Equality and Human Rights Commission guidance', domain='none',
  award='none',
  para=("Threshold standards are not universal competence standards; a provider that sets competence standards under the Equality Act "
        "2010 may draw on this statement and any PSRB requirements, and should follow the latest guidance from the Equality and Human "
        "Rights Commission."),
  prac=("Do not treat Table 1's threshold as a competence standard. If you write competence standards for a programme specification, "
        "draw on this statement and PSRB requirements and follow the Equality and Human Rights Commission's current guidance."),
  ben=('n/a', 'a duty on the provider in writing competence standards'),
  aaw=("Describe this as a provider recommendation (force: should) about competence standards in the Equality Act 2010 sense, holding "
       f"at any level. Cite it as ({CITE}, para 4.3). Do not call the threshold cells competence standards, and do not claim the "
       "statement sets any. Set it beside para 1.19 "
       f"({SID}/1.19) and Table 1's threshold cells."),
  aad=("Raise it when a team proposes making a skill compulsory for every student or writes a programme specification with competence "
       "standards. Frame it for staff as a caution about inclusion law. Ask: 'Is this a genuine competence standard, and have you read "
       "the current Commission guidance?' Do not present it to a student as a requirement on them."))

s('4.5', type='requirement', rung='none', force='must', level='fheq:7', appliesTo="master's graduates of the subject",
  addressee='learner', verbs=['require', 'meeting'], about="master's understanding beyond the honours standards", domain='understanding',
  award=MA,
  para=("A master's degree calls for greater technical, critical, conceptual and contextual understanding, on top of meeting the honours "
        "standards in Table 1."),
  prac=("Design master's study so that students reach deeper technical, critical, conceptual and contextual understanding, and also meet "
        "the honours standards of Table 1 (read as required, force must)."),
  ben=("At master's level you must reach a deeper technical, critical, conceptual and contextual understanding, while also meeting "
       "everything expected at honours level."),
  aaw=("Describe this as the master's requirement (force: must, from the issuer's 'require') at FHEQ Level 7 (FQHEIS Level 11): honours "
       f"standards plus deeper understanding. Cite it as ({CITE}, para 4.5). Do not claim it applies to honours study or that it is a "
       f"regulatory rule. Set it beside the list in para 4.7 ({SID}/4.7.b1 to 4.7.b12), Table 1, the FHEQ master's descriptor "
       "qaa/fheq-2024/4.17.b1 and spine:7."),
  aad=("Raise it with a master's applicant or student asking how the level differs from their degree, or a team writing level 7 "
       "outcomes. Say plainly to a student that the honours skills are the floor and the master's adds depth in four kinds of "
       "understanding. Ask: 'Which of technical, critical, conceptual or contextual understanding has grown most in your work?' Avoid "
       "reading the master's list out in full."))

# ---------------------------------------------------------------- Table 1: fourteen attributes at three rungs (4.4)
AFTER = 'Table 1. Three levels'
RUNGS = ('threshold', 'typical', 'excellent')
RLEAD = {'threshold': 'At threshold (the minimum for the honours award), the graduate ',
         'typical': 'At the typical rung, the graduate ',
         'excellent': 'At the excellent rung, the graduate '}
PLEAD = {'threshold': 'Threshold descriptor: ', 'typical': 'Typical descriptor: ', 'excellent': 'Excellent descriptor: '}
BLEAD = {'threshold': 'To reach the threshold standard, ', 'typical': 'At the typical standard, ',
         'excellent': 'At the excellent standard, '}
RDESC = {'threshold': 'the threshold standard, the minimum every honours graduate in the subject has shown (force: threshold)',
         'typical': 'a typical-rung descriptor, what most honours graduates show above the minimum (the cell has no modal of its own; force recorded as describes)',
         'excellent': 'an excellent-rung descriptor, an aspiration above the typical (the cell has no modal of its own; force recorded as describes)'}
RFORCE = {'threshold': 'threshold', 'typical': 'describes', 'excellent': 'describes'}

# each row: (name, domain, framework ids, Annex D row, master's counterpart, when to raise, question, three cells)
# each cell: (find text, verbs, about, core (third person), ben core (second person))
ROWS = [
    ('Research and inquiry', 'subject-skill', 'qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b5', 'qaa/fheq-2024/annex-d/knowledge/r3', '4.7.b3',
     'a student is starting the research for a project or a team is reviewing how research is taught',
     'Where did the ideas in your last project come from, and how did you gather them?', [
        ('Demonstrates the ability to gather and synthesise information from contextual sources and materials, to generate ideas',
         ['demonstrates', 'gather', 'synthesise', 'generate'], 'gathering sources to generate ideas',
         'collects information from contextual sources and materials and pulls it together to produce ideas',
         'you collect information from the sources and materials around your work and pull it together to come up with ideas'),
        ('Undertakes research employing appropriate methods across a broad spectrum of sources',
         ['undertakes', 'employing'], 'research with fitting methods across many sources',
         'carries out research with fitting methods across a wide range of sources',
         'you research with methods that suit the task, drawing on a wide range of sources'),
        ('Engages critically with diverse sources, synthesising insight and demonstrating how this supports creative development',
         ['engages', 'synthesising', 'demonstrating', 'supports'], 'critical synthesis of sources for creative development',
         'works critically with varied sources, draws insight from them and shows how that insight drives creative development',
         'you work critically with varied sources, draw your own insight from them and show how it moves your creative work forward')]),
    ('Material knowledge', 'knowledge', 'qaa/fheq-2024/4.15.b2', 'qaa/fheq-2024/annex-d/practical/r1', '4.7.b2',
     'a student is choosing materials or processes, or a teacher is planning workshop inductions',
     'Why did you pick these materials, and what did you try before settling on them?', [
        ('Applies use of materials and processes appropriate to context',
         ['applies'], 'materials and processes suited to context',
         'uses materials and processes that suit the context of the work',
         'you use materials and processes that suit the setting of your work'),
        ('Experiments with materials and processes to generate creative ideas',
         ['experiments', 'generate'], 'experimenting with materials to spark ideas',
         'experiments with materials and processes as a way of producing creative ideas',
         'you experiment with materials and processes to spark creative ideas'),
        ('Engages with materials in a purposeful, explorative and imaginative way, applying them confidently to produce creative outcomes',
         ['engages', 'applying', 'produce'], 'purposeful, imaginative and confident use of materials',
         'handles materials with purpose, exploration and imagination, and uses them with confidence to make creative work',
         'you handle materials with purpose and imagination, exploring what they can do and using them confidently in your work')]),
    ('Contextual awareness', 'understanding', 'qaa/fheq-2024/4.15.b1', 'qaa/fheq-2024/annex-d/knowledge/r2', '4.7.b10',
     'a student is placing their work in history or theory, or a team is linking contextual studies to studio modules',
     'Which artists, designers or ideas, past or present, does your work answer to?', [
        ('Recognises key historical and current theoretical and cultural contexts',
         ['recognises'], 'main historical, theoretical and cultural contexts',
         'recognises the main historical contexts of the field and the theoretical and cultural ones that matter now',
         'you recognise the main historical, theoretical and cultural contexts your field sits in, past and present'),
        ('Applies contextual understanding and key factors to shape creative practice',
         ['applies', 'shape'], 'context shaping creative practice',
         'uses an understanding of context and its main factors to shape creative practice',
         'you use what you understand about context to shape your creative practice'),
        ('Integrates contextual understanding, factors and behaviours to support creative ambition',
         ['integrates', 'support'], 'context integrated in support of ambition',
         'brings contextual understanding, its factors and behaviours together in the service of ambitious creative work',
         'you bring your grasp of context fully into your work so that it backs up your creative ambitions')]),
    ('Engagement with contemporary discourse and debate', 'understanding', 'qaa/fheq-2024/4.15.b3.2', 'qaa/fheq-2024/annex-d/cognitive/r1', '4.7.b4',
     'a student is asked about current debates in their field or a team is planning seminars and critical writing',
     'What argument going on in your field right now matters to your work, and where do you stand on it?', [
        ('Identifies current debates and conversation relevant to art, design and cultural production',
         ['identifies'], 'current debates in art, design and culture',
         'identifies the debates and conversations now under way in art, design and cultural production',
         'you can name the debates going on now in art, design and cultural production'),
        ('Engages with relevant debates and ideas to inform thinking, practice and critical reflection',
         ['engages', 'inform'], 'debates feeding thinking and practice',
         'takes part in relevant debates and ideas and lets them feed thinking, practice and critical reflection',
         'you engage with relevant debates and ideas and let them feed your thinking, your practice and your reflection'),
        ('Applies critical understanding of discourse to contribute to current disciplinary dialogues',
         ['applies', 'contribute'], 'contributing to the discipline\'s conversations',
         'brings a critical grasp of the discourse to bear and adds to the conversations the discipline is having now',
         'you use a critical grasp of the discussion in your field to add your own voice to it')]),
    ('Analysis', 'subject-skill', 'qaa/fheq-2024/4.15.b7', 'qaa/fheq-2024/annex-d/cognitive/r2', '4.7.b4',
     'a student is analysing their own or others\' work, or a teacher is setting an analytical task',
     'What does this piece do, and how did your analysis of it change what you made next?', [
        ('Recognises and interprets ideas and practices within cultural, creative and conceptual contexts',
         ['recognises', 'interprets'], 'interpreting ideas and practices in context',
         'recognises and interprets ideas and practices in their cultural, creative and conceptual settings',
         'you recognise and interpret ideas and practices in their cultural, creative and conceptual settings'),
        ('Systematically applies analysis to inform creative practice and decision-making',
         ['applies', 'inform'], 'systematic analysis guiding decisions',
         'analyses systematically and uses the results to guide creative practice and decisions',
         'you analyse systematically and use what you find to guide your creative choices'),
        ('Interrogates and experiments with creative possibilities through analysis and synthesis',
         ['interrogates', 'experiments'], 'questioning and testing creative possibilities',
         'questions and tests creative possibilities by analysing and combining ideas',
         'you question and test creative possibilities by analysing ideas and combining them')]),
    ('Realisation', 'subject-skill', 'qaa/fheq-2024/4.15.b6', 'qaa/fheq-2024/annex-d/practical/r3', '4.7.b5',
     'a student is turning ideas into finished work or a team is planning a final major project',
     'What methods took this from idea to finished piece, and what would you change?', [
        ('Identifies and uses suitable methods to develop and complete creative outcomes',
         ['identifies', 'uses', 'develop', 'complete'], 'methods to develop and finish work',
         'finds and uses suitable methods to develop creative work and see it through to completion',
         'you find and use suitable methods to develop your creative work and finish it'),
        ('Uses effective methods and techniques to realise imaginative creative outcomes',
         ['uses', 'realise'], 'effective methods for imaginative work',
         'uses effective methods and techniques to produce imaginative creative work',
         'you use effective methods and techniques to make imaginative creative work'),
        ('Consolidates and generates understanding to realise imaginative and creative outcomes that express intent and innovative thinking',
         ['consolidates', 'generates', 'realise', 'express'], 'work that conveys intent and new thinking',
         'draws together and builds understanding to make imaginative creative work that conveys clear intent and innovative thinking',
         'you build and draw together your understanding to make imaginative work that shows clear intent and new thinking')]),
    ('Reflection', 'subject-skill', 'qaa/fheq-2024/4.15.b4', 'qaa/fheq-2024/annex-d/transferable/r5', '4.7.b6',
     'a student is writing a reflective statement or process journal, or a teacher is designing reflective assessment',
     'Looking back at this project, what worked, what did not, and what will you do differently?', [
        ('Reflects on creative decisions and outcomes to develop self-reflection and understand strengths and weaknesses',
         ['reflects', 'develop', 'understand'], 'reflecting on decisions, strengths and weaknesses',
         'reflects on creative decisions and results to grow self-awareness and know their own strengths and weaknesses',
         'you look back on your creative decisions and results to understand yourself, your strengths and your weaknesses'),
        ('Critically evaluates the impact of process, development and outcomes',
         ['evaluates'], 'critical evaluation of process and outcomes',
         'judges critically what the process, the development of the work and its results have achieved',
         'you judge critically what your process, development and results have achieved'),
        ('Applies critical evaluation, self- awareness and reflection to improve future work',
         ['applies', 'improve'], 'evaluation used to improve later work',
         'uses critical evaluation, self-awareness and reflection to make later work better',
         'you use critical evaluation, self-awareness and reflection to make your next piece of work better')]),
    ('Awareness of audience and impact', 'understanding', 'qaa/fheq-2024/4.15.b8', 'qaa/fheq-2024/annex-d/transferable/r1', '4.7.b5',
     'a student is planning how work will be shown or a team is setting exhibition or presentation tasks',
     'Who is this work for, and how might they read it differently from you?', [
        ('Recognises how creative work conveys meaning and is open to interpretation',
         ['recognises', 'conveys'], 'how work carries meaning',
         'recognises that creative work carries meaning and can be read in more than one way',
         'you recognise that creative work carries meaning and that people may read it differently'),
        ('Considers audiences when conceiving, developing and presenting outcomes',
         ['considers', 'conceiving', 'developing', 'presenting'], 'audiences throughout the making of work',
         'keeps audiences in mind while conceiving, developing and presenting work',
         'you keep your audiences in mind as you conceive, develop and present your work'),
        ('Communicates work to ensure relevance to diverse audiences or contexts, sensitively demonstrating awareness of complexity and ambiguity',
         ['communicates', 'ensure', 'demonstrating'], 'relevance to diverse audiences; handling ambiguity',
         'communicates work so it speaks to diverse audiences or settings, with a sensitive awareness of complexity and ambiguity',
         'you communicate your work so it speaks to many audiences and settings, handling complexity and ambiguity with care')]),
    ('Independence and management', 'generic-skill', 'qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.15.b9.2', 'qaa/fheq-2024/annex-d/transferable/r3', '4.7.b8',
     'a student is struggling with deadlines or workload, or a team is staging independence across the levels',
     'How did you plan this project, and where did the plan slip?', [
        ('Plans time and tasks to meet deadlines',
         ['plans', 'meet'], 'planning time and tasks for deadlines',
         'plans time and tasks so that deadlines are met',
         'you plan your time and tasks so you meet deadlines'),
        ('Organises time and resources effectively to solve problems and manage projects',
         ['organises', 'solve', 'manage'], 'organising resources to run projects',
         'organises time and resources well to solve problems and run projects',
         'you organise your time and resources well to solve problems and run projects'),
        ('Works independently with initiative and resilience in sometimes uncertain contexts',
         ['works'], 'independent work with initiative and resilience',
         'works alone with initiative and resilience where the setting is at times uncertain',
         'you work on your own, taking the initiative and staying resilient when things are uncertain')]),
    ('Communication', 'generic-skill', 'qaa/fheq-2024/4.15.b8', 'qaa/fheq-2024/annex-d/transferable/r1', '4.7.b5',
     'a student is preparing a pitch, statement or presentation, or a teacher is setting communication tasks',
     'How would you explain this idea to someone who has not seen the work?', [
        ('Describes ideas, intent or experience through appropriate formats',
         ['describes'], 'describing ideas in suitable formats',
         'describes ideas, intentions or experience in formats that suit them',
         'you describe your ideas, intentions or experience in suitable formats'),
        ('Selects and uses appropriate communication methods to develop and share creative ideas effectively',
         ['selects', 'uses', 'develop', 'share'], 'choosing ways to communicate ideas',
         'chooses and uses suitable ways of communicating to develop and share creative ideas well',
         'you choose and use suitable ways of communicating to develop and share your creative ideas well'),
        ('Integrates critical and experimental approaches to purposefully communicate ideas with conviction, coherence and purpose',
         ['integrates', 'communicate'], 'communicating with conviction and coherence',
         'combines critical and experimental approaches to put ideas across with conviction, coherence and purpose',
         'you combine critical and experimental approaches to put your ideas across with conviction and coherence')]),
    ('Ethics and social responsibility', 'generic-skill', 'qaa/fheq-2024/4.15.b9.2', 'qaa/fheq-2024/annex-d/professional/r2/3rd-1st', '4.7.b11',
     'a student is weighing an ethical question in their work or a team is placing ethics and inclusion in the curriculum',
     'Who could be affected by this work, and whose voices are missing from it?', [
        ("Shows awareness of the creative sector's ethical and social responsibilities, and empathy towards others",
         ['shows'], "awareness of the sector's ethical duties; empathy",
         'shows awareness of the ethical and social responsibilities of the creative sector, and empathy for other people',
         "you show you understand the ethical and social responsibilities of the creative sector, and you show empathy for others"),
        ('Engages with ethical principles, inclusivity, access and social considerations in decision-making',
         ['engages'], 'ethics, inclusivity and access in decisions',
         'takes ethical principles, inclusivity, access and social factors into account when deciding',
         'you take ethics, inclusivity, access and social factors into account when you make decisions'),
        ('Applies critical practice to address inequalities of representation in the contexts in which art and design is produced and consumed',
         ['applies', 'address'], 'tackling unequal representation',
         'uses critical practice to tackle unequal representation where art and design are made and consumed',
         'you use critical practice to tackle unequal representation in the places where art and design are made and used')]),
    ('Sustainability literacy', 'generic-skill', 'qaa/fheq-2024/4.15.b9.2', 'qaa/fheq-2024/annex-d/summary/r4', '4.7.b10',
     'a student is choosing materials, production methods or digital tools, or a team is embedding sustainability',
     'What is the environmental and social cost of how you made this, and what would lower it?', [
        ("Evidences an understanding of sustainability and acknowledges the creative sector's role in responding to environmental and social challenges",
         ['evidences', 'acknowledges', 'responding'], "understanding sustainability and the sector's part",
         "shows an understanding of sustainability and accepts the part the creative sector plays in meeting environmental and social challenges",
         'you show you understand sustainability and the part the creative sector plays in meeting environmental and social challenges'),
        ('Actively considers environmental, social and economic sustainability in proposed decisions and production methods',
         ['considers'], 'sustainability in decisions and production',
         'actively weighs environmental, social and economic sustainability in planned decisions and ways of producing work',
         'you actively weigh environmental, social and economic sustainability in your decisions and in how you produce work'),
        ('Integrates sustainability as a core value in creative work, showing awareness of circularity, resource impact and long-term value',
         ['integrates', 'showing'], 'sustainability as a core value',
         'makes sustainability a core value of creative work, aware of circularity, resource use and lasting value',
         'you make sustainability central to your creative work, aware of circularity, resource use and lasting value')]),
    ('Enterprise and entrepreneurship', 'generic-skill', 'qaa/fheq-2024/4.15.b9.1', 'qaa/fheq-2024/annex-d/transferable/r4', '4.7.b7',
     'a student is thinking about exhibiting, selling or publishing, or a team is planning professional practice modules',
     'Where could this work be shown, sold or published, and what would it take to get it there?', [
        ('Recognises the potential for work to be professionally presented',
         ['recognises', 'presented'], 'seeing how work could be presented professionally',
         'sees how work could be presented in a professional way',
         'you see how your work could be presented professionally'),
        ('Develops innovative creative outputs within professional or public contexts',
         ['develops'], 'innovative work in professional or public settings',
         'develops new and inventive creative work in professional or public settings',
         'you develop innovative creative work in professional or public settings'),
        ('Devises opportunities to publicly present, exhibit, commercialise or publish creative outputs',
         ['devises', 'present', 'exhibit', 'commercialise', 'publish'], 'creating chances to exhibit, sell or publish',
         'creates their own openings to present, exhibit, sell or publish creative work in public',
         'you create your own chances to show, exhibit, sell or publish your creative work in public')]),
    ('Employability', 'generic-skill', 'qaa/fheq-2024/4.15.b9.3', 'qaa/fheq-2024/annex-d/transferable/r2', '4.7.b12',
     'a student is planning placements, networks or a career, or a team is reviewing employability provision',
     'What are you good at, what do you need to develop, and who in your field do you already know?', [
        ('Recognises and articulates personal strengths and areas for development, in order to engage in collaboration and establish an awareness of professional networks',
         ['recognises', 'articulates', 'engage', 'establish'], 'own strengths, collaboration and networks',
         'recognises and explains their strengths and development needs so that they can collaborate and become aware of professional networks',
         'you recognise and explain your strengths and what you need to develop, so you can collaborate and get to know professional networks'),
        ('Demonstrates commitment to personal development and to building a professional network',
         ['demonstrates', 'building'], 'commitment to growth and professional contacts',
         'shows they are committed to growing personally and to building professional contacts',
         'you show you are committed to your own growth and to building professional contacts'),
        ('Actively seeks and capitalises on opportunities to build professional networks, demonstrate initiative, adaptability and professionalism',
         ['seeks', 'capitalises', 'build', 'demonstrate'], 'seizing networking chances with initiative',
         'actively looks for and makes the most of chances to grow professional networks, showing initiative, adaptability and professionalism',
         'you actively look for and make the most of chances to grow your professional networks, showing initiative, adaptability and professionalism')]),
]

def rid(n, rung):
    return f'4.4.b{n}' if rung == 'threshold' else f'4.4.b{n}.{rung}'

GRADE = {}
OUT = []
for n, (name, dom, fw, ad, ma, when, qn, cells) in enumerate(ROWS, 1):
    for rung, (find, verbs, about, core, bcore) in zip(RUNGS, cells):
        i = rid(n, rung)
        nb = {'threshold': f'the typical cell {SID}/{rid(n, "typical")}',
              'typical': f'the threshold cell {SID}/{rid(n, "threshold")} and the excellent cell {SID}/{rid(n, "excellent")}',
              'excellent': f'the typical cell {SID}/{rid(n, "typical")}'}[rung]
        adx = (f"Annex D's third-class description {ad}" + ('' if ad.endswith('3rd-1st') else '/3rd')) if rung == 'threshold' else \
              (f'Annex D row {ad} for comparison only, since the statement ties no rung to a degree class')
        notmin = ('and do not equate it with any one degree class' if rung == 'threshold'
                  else 'and never present it as the pass requirement')
        avoid = ('' if rung == 'threshold' else ', and do not present this cell as the minimum a student must reach')
        s(i, find=find, after=AFTER, type=rung, rung=rung, force=RFORCE[rung], level='fheq:6',
          appliesTo=f'honours graduates at the {rung} rung', addressee='learner', verbs=verbs, about=about, domain=dom, award=HON,
          para=PLEAD[rung] + core[0].upper() + core[1:] + f' ({name}).',
          prac=RLEAD[rung] + core + '; set and assess level 6 work so that this can be seen.',
          ben=BLEAD[rung] + bcore + '.',
          aaw=(f"Describe this as {RDESC[rung]} for '{name}' in Table 1, at FHEQ Level 6 (FQHEIS Level 10) for a bachelor's degree "
               f"with honours. Cite it as ({CITE}, para 4.4, Table 1: {name}, {rung} column). Do not call it a regulatory requirement "
               f"or apply it to master's study, where para 4.7 ({SID}/{ma}) holds the nearest outcome, {notmin}. Set it beside {nb}, "
               f"the FHEQ honours descriptor {fw}, spine:6 and {adx}."),
          aad=(f"Bring this up when {when}. With a student, put it in plain second-person words about their own work; with staff, "
               f"frame it as what level 6 work in this area lets a graduate show at the {rung} rung. Ask: '{qn}' Do not read the table "
               f"out at length{avoid}."))
    GRADE[rid(n, 'typical')] = rid(n, 'threshold') + '|stated'
    GRADE[rid(n, 'excellent')] = rid(n, 'typical') + '|stated'
    OUT.append(dict(outcome=name[0].lower() + name[1:], threshold=rid(n, 'threshold'), typical=rid(n, 'typical'),
                    excellent=rid(n, 'excellent'), basis='stated', domain=dom, award=HON))

# ---------------------------------------------------------------- 4.7 master's outcomes (lead-in: are typically able to)
MROWS = [
    (['apply'], 'systematic, rigorous use of knowledge in outcomes', 'subject-skill', 'qaa/fheq-2024/4.17.b3', '4.4.b3',
     'apply theoretical, practical, technical and contextual knowledge with system and rigour as creative, academic or professional work develops',
     'bring theory, practice, technique and context to your work with rigour and method, whether the result is creative, academic or professional',
     'a student is shaping a major project or a team is writing level 7 project outcomes',
     'Which kinds of knowledge does this project lean on, and how do you test that you have used them rigorously?'),
    (['apply', 'expand', 'introduce'], 'inventive use of materials', 'subject-skill', 'qaa/fheq-2024/4.17.b3', '4.4.b2',
     'use materials widely and inventively, extending how things are made and bringing new approaches into creative practice',
     'use materials widely and inventively, pushing how things are made and bringing new approaches into your practice',
     'a student is pushing a material or process further or a team is planning studio and workshop access at level 7',
     'What have you done with this material that you had not seen done before?'),
    (['develop', 'apply', 'support'], 'methods for advanced inquiry', 'subject-skill', 'qaa/fheq-2024/4.17.b2', '4.4.b1',
     'build and use methods and methodologies systematically to carry advanced inquiry',
     'build and use research methods and methodologies systematically to carry advanced inquiry',
     'a student is designing the method for a research-led project or a team is planning research training',
     'Why is this the right method for your question, and what would another method show?'),
    (['analyse', 'inform'], 'critical analysis to advance practice', 'subject-skill', 'qaa/fheq-2024/4.17.b4.1', '4.4.b5',
     'analyse research, iteration and contextual factors critically and thoroughly so that practice moves forward',
     'analyse research, your iterations and the context of your work critically and thoroughly, so your practice moves forward',
     'a student is reviewing iterations of their work or a team is setting critical writing at level 7',
     'What did your analysis of the last round of work change in the next?'),
    (['realise'], 'realising work in complex, unpredictable settings', 'subject-skill', 'qaa/fheq-2024/4.17.b5 and qaa/fheq-2024/4.17.b8.2', '4.4.b6',
     'realise practice, research, ideas and knowledge to a professional standard in visual, spoken or written form across varied, complex and unpredictable settings',
     'bring practice, research, ideas and knowledge to a professional finish in visual, spoken or written form, in varied, complex and unpredictable settings',
     'a student is preparing work for a public or professional setting or a team is designing a final show or viva',
     'Which form suits this work best, and how will it hold up in a setting you do not control?'),
    (['undertake', 'support'], 'systematic critical reflection', 'generic-skill', 'qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b7', '4.4.b7',
     'reflect critically on practice in a systematic and purposeful way, supporting intellectual growth and innovation',
     'reflect critically on your practice in a planned, purposeful way that helps you grow and innovate',
     'a student is writing a reflective account or a team is assessing reflection at level 7',
     'What is your method for reflecting, and what has it led you to change?'),
    (['apply'], 'professional working methods in complex situations', 'generic-skill', 'qaa/fheq-2024/4.17.b8.2', '4.4.b13',
     'use professional working methods with confidence across a range of complex situations',
     'use professional ways of working with confidence in a range of complex situations',
     'a student is on a placement or live brief or a team is planning professional practice at level 7',
     'In your last complex brief, which professional methods held up and which did not?'),
    (['deploy', 'support', 'enable'], 'flexible, agile working', 'generic-skill', 'qaa/fheq-2024/4.17.b5', '4.4.b9',
     'use flexible and agile methods of working to move projects on and take a creative approach to problems',
     'work flexibly and with agility to move projects on and take a creative approach to problems',
     'a project has changed course or a team is planning collaborative or live work',
     'When the brief changed, how did you adapt your way of working?'),
    (['situate', 'interrogating'], 'ethically situated practice', 'understanding', 'qaa/fheq-2024/4.17.b1', '4.4.b11',
     'place practice in a clearly defined, critically informed context and question how it relates to ethical working practices, responsibilities and implications',
     'place your practice in a clear, critically informed context and question its ethics, responsibilities and consequences',
     'a student is framing a major project or a team is placing ethics in level 7 study',
     'What context does your practice belong to, and what ethical questions does that raise?'),
    (['interpret'], 'knowledge read in sensitive context', 'understanding', 'qaa/fheq-2024/4.17.b1', '4.4.b3',
     'interpret knowledge within a clearly bounded context that is alert to cultural, environmental, social and political matters',
     'interpret knowledge within a clearly bounded context, alert to cultural, environmental, social and political matters',
     'a student is building the context for a thesis or project or a team is planning critical studies at level 7',
     'Which cultural, environmental, social or political factors shape how your work should be read?'),
    (['apply', 'centre', 'responding'], 'equity and inclusion in creative strategy', 'subject-skill', 'qaa/fheq-2024/4.17.b8.1', '4.4.b11',
     'use creative strategies that put equity and inclusion at their centre, answering structural injustice through design or artistic intervention',
     'use creative strategies built around equity and inclusion, answering structural injustice through design or art',
     'a student is working on a project about injustice or a team is embedding equity in level 7 briefs',
     'What injustice does this work respond to, and who shaped the response with you?'),
    (['apply', 'realise', 'contribute'], 'collaboration and leadership for change', 'generic-skill', 'qaa/fheq-2024/4.17.b8.1', '4.4.b14',
     'work collaboratively with initiative, responsiveness and leadership to reach shared goals and add to positive change',
     'work with others, taking the initiative, responding and leading, to reach shared goals and make a positive difference',
     'a student is leading or joining a team project or a team is assessing collaboration at level 7',
     'What part did you play in the group, and what changed because of it?'),
]
for k, (verbs, about, dom, fw, hon, core, bcore, when, qn) in enumerate(MROWS, 1):
    s(f'4.7.b{k}', type='outcome', rung='none', force='will', level='fheq:7', appliesTo="master's graduates of the subject",
      addressee='learner', verbs=verbs, about=about, domain=dom, award=MA,
      para="Master's graduates are typically able to " + core + '.',
      prac="Master's graduates will typically be able to " + core + '; give level 7 modules and the major project room for this.',
      ben='By the end of a master\'s, you will typically be able to ' + bcore + '.',
      aaw=(f"Describe this as one of the outcomes master's graduates are typically able to show (force: will, framed by the issuer as "
           f"typical), at FHEQ Level 7 (FQHEIS Level 11), resting on the honours standards (para 4.5). Cite it as ({CITE}, para 4.7, "
           f"item {k}). Do not present it as a regulatory requirement, a pass threshold or an honours-level outcome. Set it beside the "
           f"FHEQ master's descriptor {fw}, spine:7, para 4.5 ({SID}/4.5) and the honours row {SID}/{hon}."),
      aad=(f"Raise it when {when}. With a master's student, say it plainly in the second person; with a programme team, frame it as "
           f"what level 7 study gives room to show. Ask: '{qn}' Avoid reading the whole list aloud and avoid treating it as a pass rule."))

TH = {'1.19': 'theme:accessibility'}

S5 = dict(
    levels=[dict(id='fheq:4', role='cites', locator='D1, 2.15'), dict(id='fheq:5', role='cites', locator='D1, 2.15'),
            dict(id='fheq:6', role='cites', locator='D1, 2.12; 2.16; 2.18'), dict(id='fheq:7', role='cites', locator='D1, 2.12; 2.18; 4.8'),
            dict(id='fqheis:7', role='cites', locator='D1, 2.15'), dict(id='fqheis:8', role='cites', locator='D1, 2.15'),
            dict(id='fqheis:9', role='cites', locator='D1, 2.17'), dict(id='fqheis:10', role='cites', locator='D1, 2.12; 2.17; 2.18'),
            dict(id='fqheis:11', role='cites', locator='D1, 2.12; 2.18; 4.8'),
            dict(id='spine:6', role='refers', locator='std:ref:uk-framework, R2 and R8 (inferred: Table 1 and the generic skills sit at this step)'),
            dict(id='spine:7', role='refers', locator="std:ref:uk-framework, R2 and R8 (inferred: the master's outcomes in 4.7)")],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.12; 2.18: honours degree, FHEQ Level 6, FQHEIS Level 10)'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.12; 2.18; 4.8: integrated master's)"),
                dict(**{'from': 'fheq:4'}, to='fqheis:7', relation='equivalent', basis='stated (D1, 2.15: Certificate of Higher Education)'),
                dict(**{'from': 'fheq:5'}, to='fqheis:8', relation='equivalent', basis='stated (D1, 2.15: Diploma of Higher Education)')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.10', '1.11', '1.12', '1.13', '1.14', '1.15', '1.16', '1.19', '1.21', '1.32', '1.38', '1.40', '3.17', '3.18', '3.19', '4.3', '4.4', '4.7']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23', '1.24', '3.13', '3.20', '4.4']),
      dict(id='theme:esd', role='carries', carriedIn=['1.6', '1.25', '1.26', '1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '1.49', '4.4']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.9', '1.29', '1.34', '1.35', '1.36', '1.37', '1.38', '1.39', '1.40', '3.14', '3.16', '4.4']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['1.33', '1.37', '1.41', '1.42', '1.43', '1.44', '1.45', '1.46', '1.47', '1.48', '1.49', '1.50'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-art-and-design-2019-benchmarks (not yet ingested)', note='the fourth edition, 2019, a minor update of 2016 (D1, back matter): Part E'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree classification descriptions for honours, named in 4.2'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ Levels 4 to 7 (2.12, 2.15, 2.16, 2.18, 4.8)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS/SCQF Levels 7 to 11 (2.12, 2.15, 2.17, 2.18, 4.8)'),
      dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note='Education for Sustainable Development (QAA and Advance HE, 2021), 1.26'),
      dict(rel='refersTo', target='QAA Quality Code 2024 and QAA Glossary (not yet ingested)', note='front matter'),
      dict(rel='refersTo', target='PSRB requirements: Institution of Engineering Designers; Chartered Society of Designers (not yet ingested)', note='2.23; Part E'),
      dict(rel='relatedTo', target='std:doc:qaa-history-of-art-architecture-and-design-2026-benchmarks', note='inferred: a neighbouring subject in the same series; not named in the text')]

SB1 = ['A broad subject of many disciplines, practice-based and student-centred, in which making and creative inquiry are both how students learn and how they show their learning (D1, 1.4, 2.5, 2.6).',
       'Its practices conceive, test, make and share work that shapes visual and material culture, drawing on visual, spatial and sensory languages (D1, 1.5, 1.6).',
       'Studios and workshops shape learning; flexible and online modes now sit beside them (D1, 1.7, 2.10, 3.13).',
       'It is increasingly interdisciplinary, crossing into the humanities, business, engineering, computing, health and the built environment (D1, 1.8, 2.1, 2.4, 3.15).',
       'Contextual and critical study (history, theory, discourse) runs through practice rather than beside it (D1, 2.9, 3.3, 3.11).',
       'Assessment looks at process as well as product, often holistically, with feedback through reviews or crits (D1, 2.8, 3.19, 3.21, 3.31).',
       'Live briefs, exhibitions, placements and partnerships tie learning to creative careers (D1, 1.38, 2.7, 2.22, 3.16).']

SB2 = [dict(theme='theme:edi', inThisSubject='headed equity, diversity and inclusion: diverse practices and student voices as a driver of creativity, decolonial attention to the subject\'s knowledge traditions, studio culture as an inclusive community, inclusive assessment; at the rungs, ethics and unequal representation; at master\'s, equity-centred creative strategy (D1, 1.10 to 1.16; 3.17 to 3.19; 4.4; 4.7)',
            statements=['4.4.b11', '4.4.b11.typical', '4.4.b11.excellent', '4.7.b11']),
       dict(theme='theme:accessibility', inThisSubject='the Equality Act duty of reasonable and anticipatory adjustment applied to studios, live projects, group work, hybrid learning and flexible assessment formats, with making itself accepted as evidence (D1, 1.17 to 1.24; 3.13; 3.20)',
            statements=['1.19', '4.4.b11.typical']),
       dict(theme='theme:esd', inThisSubject='sustainability as an ethical frame for creative practice: regenerative design, circularity, responsible digital practice and the cost of GenAI, with a sustainability literacy row in Table 1 (D1, 1.25 to 1.33; 1.49; 4.4)',
            statements=['4.4.b12', '4.4.b12.typical', '4.4.b12.excellent', '4.7.b10']),
       dict(theme='theme:enterprise', inThisSubject='named employability, entrepreneurship and enterprise education: resilient, self-employed and IP-led creative careers, live projects and placements, a skills list in 1.40, and two rows of Table 1 (D1, 1.34 to 1.40; 3.16; 4.4)',
            statements=['4.4.b13', '4.4.b13.typical', '4.4.b13.excellent', '4.4.b14', '4.4.b14.typical', '4.4.b14.excellent', '4.7.b7', '4.7.b12']),
       dict(theme='theme:generative-ai', inThisSubject='GenAI as one tool in creative workflows: a spectrum from automation to refusal, students taking their own position, authentic assessment with process documentation, bias and cultural visibility, environmental cost and intellectual property (D1, 1.41 to 1.50)',
            statements=[])]

SB3 = dict(
    areas=[dict(component='3.3', gloss='four typical areas: art and design practices; historical, theoretical and critical studies; research-led practice and methods; professional skills development'),
           dict(component='3.2', gloss='curricula answering technology, planetary concerns, global views and industry change'),
           dict(component='3.4', gloss='aims: independent thinking, creative innovation, professional engagement')],
    practices=[dict(component='3.5', kind='teaching', gloss='studio learning, workshops, tutorials, reviews, peer learning, study visits, lectures, seminars'),
               dict(component='3.6', kind='teaching', gloss='studio, lecture and project-based teaching and what each develops'),
               dict(component='3.8', kind='learning', gloss='scheduled and independent learning, becoming more self-directed'),
               dict(component='3.11', kind='learning', gloss='discursive learning with texts, discussion and presentation'),
               dict(component='3.14', kind='learning', gloss='group work and projects'),
               dict(component='3.15', kind='learning', gloss='interdisciplinary collaborative projects'),
               dict(component='3.16', kind='teaching', gloss='industry, enterprise and employability activities; placements; competitions'),
               dict(component='3.21', kind='assessment', gloss='assessing both process and product'),
               dict(component='3.23', kind='assessment', gloss='self and peer assessment'),
               dict(component='3.25', kind='assessment', gloss='fourteen methods, from portfolios and exhibitions to pitches, sketchbooks and timed practicals'),
               dict(component='3.27', kind='assessment', gloss='continuous formative feedback'),
               dict(component='3.31', kind='assessment', gloss='the crit, or review, run inclusively')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.4', award=HON, items=14),
           dict(rung='typical', leadIn='4.4', award=HON, items=14),
           dict(rung='excellent', leadIn='4.4', award=HON, items=14)],
    rungBases='4.1 frames the three as minimum (threshold), typical and excellent standards shown at the honours award; 4.2 says most students exceed threshold and points to Annex D; 4.4 says the descriptors build on each other incrementally and gives Table 1, fourteen attributes in two groups (subject knowledge and understanding; professional and transferable skills), each with a threshold, typical and excellent cell',
    outcomeLists=[dict(leadIn='4.7', gloss="master's graduates are typically able to", items=12, award=[MA])],
    outcomes=OUT)

SB4A_FULL = []

SB5 = [dict(body='professional, statutory and regulatory bodies (PSRBs), as a class', says='consulted in course design where relevant; may accredit courses through review of curriculum, facilities, staffing, assessment and partnerships; their requirements inform competence standards (D1, front matter; 2.2; 2.23; 2.28; 4.3)', requirements='not yet ingested (Part E)'),
       dict(body='Institution of Engineering Designers', says='an industry-led skills body that accredits courses, for example in product design (D1, 2.23)', requirements='not yet ingested (Part E)'),
       dict(body='Chartered Society of Designers', says='an industry-led skills body that accredits courses (D1, 2.23)', requirements='not yet ingested (Part E)'),
       dict(body='The Association of Photographers', says='a professional body that does not accredit; affiliated courses gain industry insight and opportunities (D1, 2.23)', requirements='not yet ingested (Part E)'),
       dict(body='the Association of Illustrators', says='a professional body that does not accredit; affiliation gives access to insight and opportunities (D1, 2.23)', requirements='not yet ingested (Part E)'),
       dict(body='Interior Educators', says='a professional body that does not accredit; affiliation gives access to insight and opportunities (D1, 2.23)', requirements='not yet ingested (Part E)')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equity, diversity and inclusion (EDI)', carriedIn=S6[0]['carriedIn'], statements=SB2[0]['statements']),
            dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=S6[1]['carriedIn'], statements=SB2[1]['statements']),
            dict(id='theme:esd', named='Education for sustainable development (ESD)', carriedIn=S6[2]['carriedIn'], statements=SB2[2]['statements']),
            dict(id='theme:enterprise', named='Employability, entrepreneurship and enterprise education (EEE)', carriedIn=S6[3]['carriedIn'], statements=SB2[3]['statements']),
            dict(id='theme:generative-ai', named='Generative artificial intelligence (GenAI)', carriedIn=S6[4]['carriedIn'], statements=[])],
    frameworks=[dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.12', '2.15', '2.16', '2.18', '4.2', '4.8']),
                dict(framework='scqf', levels=['fqheis:7', 'fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.12', '2.15', '2.17', '2.18', '4.8'])],
    bodies=[dict(body='PSRBs', citedIn=['2.2', '2.23', '2.28', '4.3']),
            dict(body='Institution of Engineering Designers', citedIn=['2.23']),
            dict(body='Chartered Society of Designers', citedIn=['2.23']),
            dict(body='The Association of Photographers', citedIn=['2.23']),
            dict(body='the Association of Illustrators', citedIn=['2.23']),
            dict(body='Interior Educators', citedIn=['2.23'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2'], role='descriptions of the four honours classes, for evidence of achievement above threshold'),
                     dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development (QAA and Advance HE, 2021)', citedIn=['1.26'], role='learning outcomes for sustainability'),
                     dict(document='not yet ingested: listed in Part E', named='Quality Code (2024 update); QAA Glossary', citedIn=['front matter'], role='companion reference points'),
                     dict(document='not yet ingested: listed in Part E', named='Equality Act 2010', citedIn=['1.10', '1.19', '4.3'], role='legal basis for EDI, adjustments and competence standards')])

B1 = [dict(slug='discipline-art-and-design', definition="a distinct area of activity within the subject of Art and Design, some still evolving; the statement keeps 'subject' for Art and Design as a whole (D1, 1.2)",
           beneficiaryDefinition='one of the separate areas of art and design you might specialise in, such as illustration or product design', scopeNote='used throughout for specialisms', category='unknown', practices=['art and design']),
      dict(slug='course', definition='an approved pathway of study giving a coherent learning experience that normally leads to a qualification; used interchangeably with programme (D1, front matter)',
           beneficiaryDefinition='the whole set of study you sign up for that leads to your award', scopeNote='also called programme', category='unknown', practices=['education']),
      dict(slug='module', definition='a self-contained, formally structured unit of study with its own learning outcomes and assessment criteria; used interchangeably with unit (D1, front matter)',
           beneficiaryDefinition='one self-contained block of your course with its own outcomes and assessment', scopeNote='also called unit', category='unknown', practices=['education']),
      dict(slug='review-crit', definition="the studio practice of critical discussion of student work, historically the 'crit'; some providers now say 'review' because of associations with power imbalance (D1, 3.31)",
           beneficiaryDefinition='a session where your work is discussed critically with tutors, peers or outside guests', scopeNote='crit, critique and review name the same practice', category='unknown', practices=['art and design'])]
B2A = [dict(concept='discipline-art-and-design', form='disciplines', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='course', form='course', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='course', form='programme', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
       dict(concept='module', form='module', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='module', form='unit', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
       dict(concept='review-crit', form='review', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='review-crit', form='Crit', lang='en', partOfSpeech='noun', termStatus='deprecated', register='informal')]
B4 = []; B5 = []
D3 = [dict(title='Subject Benchmark Statement: Art and Design (QAA, 2019, fourth edition)', why='the superseded edition, for supersedes and a comparison of the standards')]

E = [
    'Skeleton: bm-skel.json was absent from run-src at the start of run 0088; generated with tools/std_prep.py art-and-design-2026 (no judgement fields). Its rung counts were 0 because Table 1 is linearised into paragraph 4.4.',
    'Pattern (differs from Psychology): the rungs are one table (Table 1, in 4.4) of fourteen attributes, each with a threshold, typical and excellent cell, in two groups (subject knowledge and understanding; professional and transferable skills). Recorded per the batch-1 table convention: ids 4.4.b<n>, 4.4.b<n>.typical, 4.4.b<n>.excellent; each cell has its own span (cut by `find`), since every cell carries its own wording.',
    'gradeOf for all 28 typical and excellent cells is stated (the issuer pairs the cells in one row), not inferred.',
    'Force on the rungs: the cells carry no modal. The threshold cells take force threshold (4.1, "minimum (threshold)"); the typical and excellent cells are recorded as describes. 4.1\'s "will have demonstrated" covers all three, but sits too far from the cells for the builder\'s force check; for Abbott: whether typical and excellent should read will, as in Psychology.',
    "Pattern: no master's rungs; 4.7 is a list of twelve outcomes with the lead-in \"are typically able to\" (recorded as rung none, force will, award master's, fheq:7). The word 'typically' may mark it as a typical-level list; for Abbott.",
    "4.5: \"Master's level degrees require\" recorded as force must (required is must, batch-1 convention); for Abbott.",
    '4.8: integrated master\'s "meets FHEQ Level 7/FQHEIS Level 11 standards", plain present with no modal: not a statement; S3 component only.',
    'Plain-present provider norms (not statements, template open point 5): 1.10 and 1.16 (courses aim, enable); 1.21 (studios designed or adapted to be accessible); 1.45 (courses use authentic assessments including GenAI); 2.18 (integrated master\'s designed to meet the descriptors in full); 3.7 (students are able to access resources: a provision, not an outcome); 3.16 (courses include industry activities); 4.6 (postgraduate courses include all three elements).',
    'Obliging words outside the five, left as components: 1.14 and 1.38 ("essential"); 1.37 ("there is a need for graduates", "Graduates ... require"); 1.39 ("are essential professional competencies"); 3.18 ("requiring diverse and inclusive modes of assessment"); 2.13 ("it would be expected", "may require"). Recorded as describes in effect (no statement); for Abbott.',
    '2.27: "They will consider" describes the external examiner\'s role, an actor neither learner nor provider; not cut as a statement. 2.24 and 2.25 were cut as provider expectations (will).',
    '1.40: a list of thirteen skills under "Art and Design education provides opportunities for students to develop ... The skills include"; a provision list, not an outcome list ("are able to"), so not cut; the skeleton\'s 1.40.b1 to b13 are left as candidates. For Abbott: it reads like an employability outcome list.',
    '3.3 and 3.25 lists (areas of study; assessment methods) are descriptive, recorded in SB3, not cut.',
    'Section headings run on at the end of the paragraph before them in the held text (1.9, 1.16, 1.24, 1.33, 1.40.b13, 2.11, 2.15, 2.20, 2.23, 2.28, 3.1, 3.4, 3.16, 3.17, 3.25.b14); the skeleton\'s theme hits on those headings (1.9 EDI, 1.24 ESD, 1.33 enterprise) are not counted in SB6 unless the paragraph also treats the theme.',
    'SB6: the theme names in the front matter (key changes list) are excluded matter. 3.13 and 3.20 (accessibility) and 3.14 and 3.16 (employability) carry the theme by cross-reference ("see Accessibility, paragraphs 1.17-1.24"); the numbers after "paragraphs" are references, not statements (DPN-1).',
    'Generative AI is a cross-cutting theme here (theme:generative-ai, 1.41 to 1.50; also named in 1.33 and 1.37); no statement is cut from it.',
    'Theme name variant: the statement says "Equity, diversity and inclusion", not equality; mapped to theme:edi.',
    'Levels: 1.18 names "Level 3 qualifications" (entry, outside the HE frameworks; RQF or CQFW not named): not recorded in S5.',
    'CQFW is not cited. FQHEIS is cited as "SCQF/FQHEIS" (2.17, 2.18) and as FQHEIS (2.12, 2.15, 4.8); FHEQ also in 4.2 as the Frameworks document.',
    'Inferred codes, held back from lookup until P3: hecos 101361 creative arts and design, 100059 fine art, 100048 design; cah CAH25-01-01, CAH25-01-02, CAH25-01-03. The text names the subject "Art and Design" but no code; 100050 product design is a specialism named in 2.23 (statedSubjects only).',
    'S5: spine:6 and spine:7 are inferred from the reference framework (R2, R8); generic-skill records carry fheq:6 (Table 1) or fheq:7 (4.7).',
    'Bodies: the PSRBs and five named bodies (2.23) have no ingested requirements; named but not bodies of the subject: Office for Students (front matter), Equality and Human Rights Commission (4.3), Design Council (1.25), UNESCO (1.26), Advance HE (1.26), DCMS and Arts Council England (1.35).',
    'Shared documents not ingested: QAA Quality Code 2024 and Glossary (front matter); Equality Act 2010 (1.10, 1.19, 4.3); UN Sustainable Development Goals and the Design Council\'s Skills for Planet (1.25); UNESCO key competencies for sustainability (1.26); national access plans by nation (1.11).',
    'Table 1 cell text has stray spaces from extraction ("self- awareness"); sources keep the held text as it is.',
    'supersedes: the fourth edition (2019) is named in back matter only; its document id is a placeholder.',
    'S9 commentary not researched in P1.',
]
