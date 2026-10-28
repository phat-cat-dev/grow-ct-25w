# Judgement for run 0120, QAA Mathematics, Statistics and Operational Research (March 2023), std.
# Built by tools/bm_build.py (BM-BRIEF 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft).
# Keys of P are S4 ids under qaa/mathematics-statistics-and-operational-research-2023/.

HON = "bachelor's with honours"
IM = "integrated master's"
TM = "master's"
UG = [HON, IM]
CITE = 'QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para '
NA_PROV = ('n/a', 'a duty on the provider; the student meets its effect, not a standard to reach')


def W(what, force, holds, para, notc, beside):
    """author-agent-written: to an AI agent writing about the standard."""
    return (f"Describe this as {what}; its force is {force}. State that it holds for {holds}. "
            f"Cite it as ({CITE}{para}) and do not claim {notc}. Set it beside {beside}.")


def D(when, put, ask, avoid):
    """author-agent-dialogue: to an AI agent using the standard in conversation."""
    return f"Raise it when {when}. {put} Ask {ask} Avoid {avoid}."


META = dict(
    run='0120', p1='2026-10-03 18:06',
    title='Subject Benchmark Statement Mathematics, Statistics and Operational Research',
    heading='Subject Benchmark Statement: Mathematics, Statistics and Operational Research (QAA, March 2023)',
    edition='March 2023 (fifth edition)', published='2023-03',
    status='current',
    supersedes='the fourth edition (2019), named in the membership pages (D1, section 6); not ingested',
    subjects=[
        dict(scheme='hecos', code='100403', label='mathematics', basis='stated'),
        dict(scheme='hecos', code='100406', label='statistics', basis='stated'),
        dict(scheme='hecos', code='100404', label='operational research', basis='stated'),
        dict(scheme='cah', code='CAH09-01-01', label='mathematics', basis='stated'),
        dict(scheme='cah', code='CAH09-01-03', label='statistics', basis='stated'),
        dict(scheme='cah', code='CAH09-01-02', label='operational research', basis='stated'),
        dict(scheme='cah', code='CAH09-01', label='mathematical sciences', basis='stated'),
        dict(scheme='cah', code='CAH09', label='mathematical sciences', basis='stated'),
        dict(scheme='hecos', code='100405', label='pure mathematics', basis='stated'),
        dict(scheme='hecos', code='101032', label='probability', basis='stated'),
        dict(scheme='hecos', code='100402', label='mathematical modelling', basis='stated'),
        dict(scheme='hecos', code='101034', label='statistical modelling', basis='stated'),
        dict(scheme='hecos', code='101027', label='numerical analysis', basis='stated'),
        dict(scheme='hecos', code='100784', label='history of mathematics', basis='stated'),
        dict(scheme='hecos', code='101028', label='engineering and industrial mathematics', basis='inferred'),
        dict(scheme='hecos', code='100400', label='applied mathematics', basis='inferred'),
    ],
    awards=[HON, IM, TM], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, fifth edition series with cross-cutting themes (2022 onward)',
    partsB='partial: no glossary in the document (it points readers to QAA\'s Glossary); terms it defines in its text',
    agentDefinition=("QAA's UK reference point for what a graduate in mathematics, statistics or operational research (MSOR, "
                     "treated as one field with many combinations) should know and be able to do. It sets threshold standards "
                     "only, one list for the bachelor's degree with honours and one for the integrated master's, adds a list of "
                     "professional standards and a list of general skills, and leaves performance above threshold to Annex D of "
                     "the Frameworks. Reach for it when designing, reviewing or describing an MSOR course, a data science course "
                     "with substantial MSOR content or service teaching that depends on the subject. It is not a curriculum, not "
                     "an accrediting body's standard and not a regulatory requirement in England."),
    summary=("Published by QAA in March 2023 as the fifth edition, the statement covers bachelor's degrees with honours, "
             "integrated master's degrees and, more loosely, taught postgraduate master's degrees in MSOR. It describes the "
             "subject and its three fields, the spectrum from theory-based to practice-based courses, course design, "
             "progression, flexibility, partnership and review, the content, skills, teaching and assessment of a degree, "
             "and benchmark standards at threshold only (4.5 for honours, 4.6 for the integrated master's), with the bases "
             "for judging achievement above threshold (4.8) and a list of professional standards (4.9). It treats the four "
             "cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; enterprise and "
             "entrepreneurship education), refers to Annex D of the Frameworks for classification and names the IMA, RSS, "
             "ORS and IFoA as bodies offering accreditation or professional recognition."),
    authority=("reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a "
               "sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of "
               "current quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)"))

S2 = dict(
    governs=("what can be expected of a graduate in MSOR at the end of a bachelor's degree with honours or an integrated "
             "master's degree, with taught master's degrees developing some or all of those standards, and the nature and "
             "characteristics of awards in the subject (D1, front matter: About this Statement; 2.5; 4.2; 4.7)"),
    awards=[HON, IM, "master's (taught postgraduate, 4.7)", "joint honours and interdisciplinary courses (described, 2.7, 2.13)",
            "integrated degree apprenticeships (academic component, 2.11)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    statedScope=('"For the purposes of this document, the term \'MSOR\' (Mathematics, Statistics and Operational Research) '
                 'should be understood to be more than the disjoint union of its three named elements and instead be '
                 'understood to encompass a wide variety of combinations of the various fields." (D1, 1.1)'),
    statedSubjects=[
        dict(name='Mathematics', locator='(D1, title; 1.3; 1.4)', kind='subject',
             codes=[dict(scheme='hecos', code='100403', label='mathematics'), dict(scheme='cah', code='CAH09-01-01', label='mathematics')]),
        dict(name='Statistics', locator='(D1, title; 1.5; 1.6)', kind='subject',
             codes=[dict(scheme='hecos', code='100406', label='statistics'), dict(scheme='cah', code='CAH09-01-03', label='statistics')]),
        dict(name='Operational research', locator='(D1, title; 1.7; 1.8)', kind='subject',
             codes=[dict(scheme='hecos', code='100404', label='operational research'), dict(scheme='cah', code='CAH09-01-02', label='operational research')]),
        dict(name='probability theory', locator='(D1, 1.5)', kind='specialism', codes=[dict(scheme='hecos', code='101032', label='probability')]),
        dict(name='data science', locator='(D1, 1.1; 1.6; 2.7; 3.6; 4.3)', kind='programme title', codes=[]),
        dict(name="analytics; 'management science'", locator='(D1, 1.8)', kind='programme title', codes=[]),
        dict(name='mathematics for engineering', locator='(D1, 1.9)', kind='specialism',
             codes=[dict(scheme='hecos', code='101028', label='engineering and industrial mathematics')]),
        dict(name='pure mathematics', locator='(D1, 2.4; 3.15)', kind='specialism', codes=[dict(scheme='hecos', code='100405', label='pure mathematics')]),
        dict(name='mathematical and statistical modelling', locator='(D1, 3.18; 3.27)', kind='specialism',
             codes=[dict(scheme='hecos', code='100402', label='mathematical modelling'), dict(scheme='hecos', code='101034', label='statistical modelling')]),
        dict(name='numerical analysis', locator='(D1, 3.39)', kind='specialism', codes=[dict(scheme='hecos', code='101027', label='numerical analysis')]),
        dict(name='history of mathematics; mathematics education', locator='(D1, 3.20)', kind='specialism',
             codes=[dict(scheme='hecos', code='100784', label='history of mathematics')]),
        dict(name="integrated master's (such as MMath); standalone master's (MSc, MRes); conversion master's", locator='(D1, 1.13; 2.4; 2.6)',
             kind='programme title', codes=[dict(scheme='hecos', code='100403', label='mathematics')]),
        dict(name='single honours; joint honours; interdisciplinary degrees', locator='(D1, 1.13; 2.7; 2.13)', kind='programme title', codes=[]),
    ])

SECTIONS = {'1': 'Context and purposes of a Mathematics, Statistics and Operational Research degree',
            '2': 'Distinctive features of MSOR courses',
            '3': 'Content, structure and delivery',
            '4': 'Benchmark standards'}

SUB = [('1.1', '1.10', 'Context and purposes of a Mathematics, Statistics and Operational Research degree'),
       ('1.11', '1.20', 'Purposes and characteristics of an MSOR degree'),
       ('1.21', '1.27', 'Equality, diversity and inclusion'),
       ('1.28', '1.43', 'Accessibility'),
       ('1.44', '1.48', 'Sustainability'),
       ('1.49', '1.60', 'Enterprise and entrepreneurship education'),
       ('2.1', '2.11', 'Design'),
       ('2.12', '2.15', 'Progression'),
       ('2.16', '2.24', 'Flexibility'),
       ('2.25', '2.30', 'Partnership'),
       ('2.31', '2.34', 'Monitoring and review'),
       ('3.1', '3.6', 'Content: Introduction'),
       ('3.7', '3.7', 'Subject-specific knowledge and understanding: General principles'),
       ('3.8', '3.8', 'Methods and techniques'),
       ('3.9', '3.12', 'Areas of Mathematics, Statistics and Operational Research'),
       ('3.13', '3.15', 'Mathematical thinking and logical processes'),
       ('3.16', '3.17', 'Numerical computation'),
       ('3.18', '3.19', 'Modelling'),
       ('3.20', '3.20', 'Related areas'),
       ('3.21', '3.21', 'Depth of study'),
       ('3.22', '3.24', 'Subject-specific skills'),
       ('3.25', '3.27', 'General skills'),
       ('3.28', '3.43', 'Teaching and learning'),
       ('3.44', '3.52', 'Assessment'),
       ('4.1', '4.4', 'Introduction'),
       ('4.5', '4.8', 'Academic standards'),
       ('4.9', '4.10', 'Professional standards')]

G = {
    '1.1': 'MSOR as more than its three parts; overlap and interdisciplinary provision such as data science',
    '1.2': 'why each field is described in turn',
    '1.3': 'mathematics: origins in practical problems, then generalisation and abstraction',
    '1.4': 'mathematics today: deduction from assumptions about concepts or models',
    '1.5': 'statistics and probability: data under random variation, and their history',
    '1.6': 'statistics today: models, data science and explaining results to non-experts',
    '1.7': 'operational research: wartime origins; optimisation to problem structuring',
    '1.8': 'analytics and management science at the edge of the scope',
    '1.9': 'the subject beyond STEM and as service teaching',
    '1.10': 'theory-based and practice-based course styles; every graduate a practitioner (S4)',
    '1.11': 'abstract and applied purposes, blurred in practice',
    '1.12': 'each provider shapes its own courses',
    '1.13': "course configurations: foundation years, honours, integrated and taught master's, placements",
    '1.14': 'academic and transferable skills, further study and careers',
    '1.15': 'abstract reasoning and accuracy throughout; time to consolidate',
    '1.16': 'uneven attainment across modules is normal',
    '1.17': 'cumulative subject with strict prerequisites',
    '1.18': 'further study, employability and careers information',
    '1.19': 'economic and social value of the mathematical sciences',
    '1.20': 'professional recognition by the IMA, RSS, ORS and IFoA',
    '1.21': 'why EDI matters for the subject',
    '1.22': 'diverse student backgrounds and inclusive support',
    '1.23': 'EDI in curriculum, processes and monitoring (S4)',
    '1.24': 'provider commitment to EDI; Athena SWAN; the LMS Good Practice Scheme',
    '1.25': 'decolonising the curriculum; reviewing practice for equity (S4)',
    '1.26': 'role models, gender imbalance and inclusive material',
    '1.27': 'examples of EDI good practice in seven areas',
    '1.28': 'anticipating needs; institutional support for staff (S4)',
    '1.29': 'barriers to participation at course and module level (S4)',
    '1.30': 'embedding accessibility so adjustments are rarely needed (S4)',
    '1.31': 'reasonable adjustments and specialist disability services',
    '1.32': 'embedded accessibility helps many groups',
    '1.33': 'well-curated courses (S4)',
    '1.34': 'subject features needing attention: notation, board work, non-linear argument, diagrams',
    '1.35': 'specialist technology removing barriers',
    '1.36': 'mainstream assistive tools fail mathematical content; responses (S4: the provider item)',
    '1.37': 'online and captured content; capture, captions and visibility (S4)',
    '1.38': 'support workers need subject terminology (S4)',
    '1.39': 'rare activities such as fieldwork; advice from other subjects',
    '1.40': 'flexible pedagogy and accessible notes',
    '1.41': 'unwritten course norms made explicit',
    '1.42': 'removing irrelevant barriers in assessment (S4)',
    '1.43': 'community resources for accessible courses',
    '1.44': 'the subject and the UN goals; social mobility',
    '1.45': 'real-world examples link the subject to sustainability',
    '1.46': 'ways to teach sustainability in the degree',
    '1.47': 'examples of methods applied to sustainability',
    '1.48': 'revisiting sustainability; innovation encouraged',
    '1.49': 'enterprise education and careers',
    '1.50': 'employability embedded in courses (S4)',
    '1.51': 'enterprise defined',
    '1.52': 'entrepreneurship defined',
    '1.53': 'enterprise and entrepreneurship education defined',
    '1.54': 'problem-solving and related enterprise competencies',
    '1.55': 'projects and group work; preparing students for group work (S4)',
    '1.56': 'problem-based learning, resilience and adaptability',
    '1.57': 'client projects and authentic assessment with employers',
    '1.58': 'employer and alumni events',
    '1.59': 'placements and entrepreneurial skills',
    '1.60': 'graduates explain their enterprise and employability growth (S4)',
    '2.1': 'theory-based and practice-based styles defined',
    '2.2': 'a spectrum of emphases, read from the curriculum not the title',
    '2.3': 'routes into undergraduate study and entry qualifications',
    '2.4': "routes into taught master's: conversion and specialist",
    '2.5': "bachelor's and integrated master's levels; what bachelor's degrees give (S4)",
    '2.6': "integrated master's and standalone master's courses",
    '2.7': 'joint honours and interdisciplinary degrees',
    '2.8': 'learning outside the institution: placements, schools, study abroad',
    '2.9': 'placement periods and credit; integrating credit-bearing placements (S4)',
    '2.10': 'shared core and later specialisation',
    '2.11': 'integrated degree apprenticeships (S4)',
    '2.12': 'progression to threshold; second-class degrees and postgraduate study (S4)',
    '2.13': 'joint and interdisciplinary students gain each subject\'s core skills (S4)',
    '2.14': "integrated master's adds a year",
    '2.15': 'exit awards; four-year Scottish honours; part-time study',
    '2.16': 'progressive learning supports flexibility',
    '2.17': 'a shared core eases transfer',
    '2.18': 'optional modules and guidance on choosing (S4)',
    '2.19': 'prerequisites limit flexibility and credit transfer',
    '2.20': 'routes to Qualified Teacher Status in England',
    '2.21': 'flexible education for access and social mobility',
    '2.22': 'flexible assessment, credit and recruitment',
    '2.23': 'flexible delivery modes and study patterns',
    '2.24': "courses flexible to change and to learners' needs (S4)",
    '2.25': 'academic and professional partnerships',
    '2.26': 'academic partnerships and advanced standing',
    '2.27': 'industry partnerships, placements and projects',
    '2.28': 'what placements involve',
    '2.29': 'employer demand for sandwich placements',
    '2.30': 'benefits of work with employers; oversight of delivery partners (S4)',
    '2.31': 'monitoring and periodic review',
    '2.32': 'external reviewers in periodic review',
    '2.33': 'external examiners and threshold standards',
    '2.34': 'accreditation by professional bodies',
    '3.1': 'a broad area with wide-ranging expectations',
    '3.2': 'subject knowledge varies at higher levels; that variety not restricted (S4)',
    '3.3': 'foundations mostly early, not only early',
    '3.4': 'no comprehensive content list, by design',
    '3.5': 'general skills: numeracy, computing and modelling (S4)',
    '3.6': 'data science and data-related careers',
    '3.7': 'methods and techniques; at least one application area',
    '3.8': 'common ground: calculus, linear algebra, probability and statistics',
    '3.9': 'knowledge of a range of areas (S4)',
    '3.10': 'mathematics courses: example topics',
    '3.11': 'statistics courses: example topics; using a statistical package (S4)',
    '3.12': 'operational research courses: application fields',
    '3.13': 'assumptions, their validity and their ethics',
    '3.14': 'generalisation, abstraction, proof and problem-solving',
    '3.15': 'axiomatic approaches and modelling',
    '3.16': 'numerical approximation and its pitfalls',
    '3.17': 'programming and specialist software (S4)',
    '3.18': 'modelling expected of all graduates (S4)',
    '3.19': 'modelling techniques, validation and communication',
    '3.20': 'related content: history, education, careers',
    '3.21': 'depth of study and course titles',
    '3.22': 'subject-specific skills for later use',
    '3.23': 'a problem-based subject',
    '3.24': 'branch skills: mathematics, statistics, operational research',
    '3.25': 'general skills and transfer between contexts',
    '3.26': 'general skills expected of all graduates (S4)',
    '3.27': 'summary of graduate attributes',
    '3.28': 'choosing teaching approaches (S4)',
    '3.29': 'lectures, tutorials, laboratories and active learning',
    '3.30': 'advance materials, practice exercises and open problems',
    '3.31': 'revisiting topics in a cumulative subject',
    '3.32': 'peer learning and spaces for it (S4)',
    '3.33': 'extra support and mathematics support services',
    '3.34': 'shared responsibility for independent learners (S4)',
    '3.35': 'equipping students to learn on their own (S4)',
    '3.36': 'study skills, scholarly habits and time to consolidate (S4)',
    '3.37': 'teaching spaces and boards',
    '3.38': 'technology in teaching, including automated feedback',
    '3.39': 'computing across the course; programming and software (S4)',
    '3.40': 'learning materials',
    '3.41': 'bespoke resources kept up to date',
    '3.42': 'staff training and professional development (S4)',
    '3.43': 'engaging with quality assurance (S4)',
    '3.44': 'what assessment sets out to establish',
    '3.45': 'wider abilities summative assessment may test',
    '3.46': 'formative feedback',
    '3.47': 'general characteristics as outcomes; EDI in assessment design (S4)',
    '3.48': 'varied methods; accessible and inclusive assessment (S4)',
    '3.49': 'practice matched to assessment formats',
    '3.50': 'professional judgement in marking',
    '3.51': 'controlled conditions and academic integrity',
    '3.52': 'full mark range; uneven module results; whole-course judgement',
    '4.1': 'standards stated in general terms',
    '4.2': "threshold standards for honours, integrated and taught master's; met overall",
    '4.3': 'a reference point for data science and joint courses',
    '4.4': "above-threshold performance, Annex D and master's outcomes (S4)",
    '4.5': "threshold for the bachelor's degree with honours (S4)",
    '4.6': "threshold for the integrated master's degree (S4)",
    '4.7': "taught master's develop some or all standards (S4)",
    '4.8': 'bases on which achievement above threshold shows',
    '4.9': 'professional standards (S4)',
    '4.10': "master's level: deeper experience and independence (S4)",
}

CTYPE = {'3.8': 'area', '3.9': 'area', '3.10': 'area', '3.11': 'area', '3.12': 'area', '3.13': 'area', '3.14': 'area',
         '3.16': 'area', '3.17': 'area', '3.18': 'area', '3.19': 'area', '3.20': 'area', '3.21': 'area',
         '3.28': 'practice', '3.29': 'practice', '3.30': 'practice', '3.31': 'practice', '3.32': 'practice', '3.33': 'practice',
         '3.36': 'practice', '3.37': 'practice', '3.38': 'practice', '3.46': 'practice', '3.48': 'practice', '3.50': 'practice',
         '3.51': 'practice', '3.52': 'practice'}

EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='section heading lines (1 to 4)', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for SB6'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Mathematics, Statistics and Operational Research',
         kind='other: membership and edition history, read for S1 and S7 (fifth edition, published 8 March 2023)'),
]

P = {}


def s(i, **k):
    P[i] = k


PROV = dict(rung='none', addressee='provider', level='none', domain='none', ben=NA_PROV)

# ======================================================================== section 1
s('1.10', type='expectation', force='should', appliesTo='courses of every style, theory-based to practice-based',
  award=[HON, IM, TM], verbs=['take', 'ensure', 'identify'], about='every graduate able to identify as a practitioner', **PROV,
  para="Whatever the style of course, from theory-based to practice-based, providers should act so that every graduate can see themselves fully as a professional practitioner of the subject.",
  prac="Whether your course leans to theory or to practice, you should plan it so every graduate leaves able to identify fully as a professional practitioner in mathematics, statistics or operational research.",
  aaw=W("a provider expectation about professional identity across the spectrum of course styles", "should, a duty on the provider rather than an outcome a student shows",
        "bachelor's, integrated master's and taught master's courses alike, at no single level", "1.10",
        "that it sets a graded outcome or that it is a regulatory requirement", "2.1 and 2.2 on course styles and the professional standards in 4.9.b1 to 4.9.b8"),
  aad=D("a programme team asks whether a practice-based or interdisciplinary course prepares graduates to call themselves practitioners",
        "Frame it for staff as a design aim, in plain words.", "how would a graduate of this course describe their professional identity, and where is that built?",
        "presenting it to a student as a test to pass or fail"))

s('1.23', type='expectation', force='should', appliesTo='curricula, processes and monitoring', award=[HON, IM, TM],
  verbs=['permeate', 'reflect', 'ensure', 'monitored'], about='EDI through curriculum, processes and monitoring', **PROV,
  para="Equality, diversity and inclusion should run through the curriculum and the whole learning experience; providers should examine curricula and processes, delivery, admissions and assessment among them, so no group is disadvantaged, and should monitor engagement and achievement by group and act on the results.",
  prac="You should build EDI into the curriculum and every part of the student experience, review delivery, admissions and assessment for their effects on particular groups, and monitor engagement and attainment by group so you can act for equity.",
  aaw=W("a provider expectation on equality, diversity and inclusion in curriculum, processes and monitoring", "should, a duty on the provider",
        "all MSOR courses, at no single level", "1.23", "that it states a legal duty or describes a student outcome",
        "1.25 (review of practice for equity), the examples in 1.27 and the assessment statements 3.47 and 3.48"),
  aad=D("staff review a curriculum, an admissions policy or attainment data broken down by group", "Put it to the team as a question of who the present design may leave out.",
        "which groups' attainment do you monitor, and what changed the last time a gap appeared?", "giving it to a student as something they must do, or reading the issuer's wording aloud"))

s('1.25', type='expectation', force='should', appliesTo='curricula and practice', award=[HON, IM, TM],
  verbs=['review'], about='decolonising the curriculum; equity review', **PROV,
  para="Decolonising the curriculum is a live question for the subject; without dropping core content, provision might reflect the troubled settings some contributions came from and the gatekeeping around knowledge, and providers should review their practices with equity as the explicit focus, as 1.23 sets out.",
  prac="Keep core content, but reflect openly on the discipline's history, including contributions from contexts now seen as problematic and long-standing gatekeeping; you should review your practices with equity as the explicit focus.",
  aaw=W("a provider expectation to review practice for equity, set in the debate on decolonising the curriculum", "should for the review; the reflection on history around it is advisory (might)",
        "all MSOR courses", "1.25", "that it asks for core content to be cut or censored", "1.23, which it points back to, and the curriculum examples in 1.27"),
  aad=D("a teacher asks how to handle the history of figures linked to eugenics or other harms, or how to widen the examples used",
        "Use the practitioner framing: keep the mathematics, widen the story told about it.", "where do your modules tell the history of their methods, and whose work appears in them?",
        "treating it as a demand to remove content, or putting the duty to a student"))

s('1.28', type='expectation', force='should', appliesTo='providers and their institutions', award=[HON, IM, TM],
  verbs=['anticipate', 'ensure', 'support', 'overcome'], about='anticipatory accessibility and support for subject staff', **PROV,
  para="For an accessible course, providers should foresee what learners will need and meet it in advance, and institutions should help subject staff past the barriers peculiar to the subject, which can add much to the time spent making materials accessible.",
  prac="You should anticipate learners' needs and meet them before they are raised; your institution should give MSOR staff support (specialist staff, training, policy that allows for mathematical content, suitable tools) to overcome barriers the subject brings.",
  aaw=W("a provider expectation on anticipatory accessibility and on support for subject staff", "should, a duty on the provider and its institution",
        "all MSOR courses", "1.28", "that it is a student outcome or that it restates the law", "1.30 (embedding accessibility) and 1.34 to 1.36 (the subject's own barriers)"),
  aad=D("staff say that accessible notes with dense notation take too long, or an institution writes accessibility policy",
        "Frame it for staff as support the institution owes them, not only work they owe students.", "what help do staff get to make mathematical content accessible, and where does it fall short?",
        "putting the duty to a student or reading the text aloud at length"))

s('1.29', type='expectation', force='should', appliesTo='course and module design', award=[HON, IM, TM],
  verbs=['consider', 'empower'], about='barriers to participation at course and module level', **PROV,
  para="Providers should think through the barriers that stop students taking a full part in their education and academic communities, at course level and inside modules, so accessibility is handled coherently and consistently.",
  prac="You should consider the barriers to full participation both across the course and within each module, so the approach to accessibility is one coherent, consistent whole.",
  aaw=W("a provider expectation to plan accessibility at both course and module level", "should, a duty on the provider", "all MSOR courses", "1.29",
        "that module-level fixes alone meet it", "1.28 and 1.33 (well-curated courses)"),
  aad=D("a module leader plans accessibility alone, or a review finds modules handling it in different ways", "Frame it for staff as joining up module practice into one course approach.",
        "do students meet the same accessibility arrangements in every module, and who checks?", "treating it as something a student must arrange"))

s('1.30', type='expectation', force='describes', appliesTo='providers', award=[HON, IM, TM],
  verbs=['anticipate', 'embedding', 'minimises', 'eliminates'], about='embedding accessibility so adjustments are rarely needed', **PROV,
  para="It is essential that providers foresee disabled students' subject-specific digital, physical and teaching needs and build accessibility in, so that reasonable adjustments are needed as little as possible or not at all.",
  prac="It is essential that you anticipate the digital, physical and pedagogical accessibility needs disabled students have in this subject, and embed accessibility so individual adjustments are rarely or never needed.",
  aaw=W("a provider duty worded as imperative, recorded as describes and read as close to must (Part E)", "the strongest the statement uses outside its modal verbs",
        "all MSOR courses", "1.30", "that it replaces the legal duty to make reasonable adjustments", "1.31 (reasonable adjustments) and 1.32 (who embedded accessibility helps)"),
  aad=D("a team relies on individual adjustments rather than accessible design", "Frame it for staff as moving work from reaction to design.",
        "how many adjustments did you make last year that accessible design would have removed?", "putting the duty to a student or softening its strength"))

s('1.33', type='expectation', force='should', appliesTo='course curation', award=[HON, IM, TM],
  verbs=['seek', 'ensure'], about='well-curated courses', **PROV,
  para="Providers should aim for well-curated courses, which help every student's mental health and lighten the administrative and cognitive load on disabled students, through clear communication of learning opportunities, well-spaced assessment and extra support when new ideas first appear.",
  prac="You should curate the course well: communicate learning opportunities clearly, space assessments sensibly and give particular support when a concept or skill first appears.",
  aaw=W("a provider expectation that courses be well curated", "should, a duty on the provider", "all MSOR courses", "1.33",
        "that it sets a standard for students", "1.32 (embedded accessibility) and 3.36 (time to consolidate)"),
  aad=D("students report bunched deadlines or confusing course information", "Frame it for staff as course housekeeping that helps everyone.",
        "where do assessment deadlines cluster, and how do students first hear about each learning opportunity?", "giving it to a student as their task"))

s('1.36.b1', type='expectation', force='should', appliesTo='providers', award=[HON, IM, TM],
  verbs=['acknowledge', 'providing'], about='extra resources where assistive technology fails', **PROV,
  para="Because mainstream assistive technology handles mathematical content poorly, providers should recognise the subject's particular needs and supply extra resources that mostly text-based subjects may not need.",
  prac="You should recognise that common assistive tools (screen readers, captioning, learning platforms) often fail on mathematical content, and fund the extra resources needed to close that gap.",
  aaw=W("a provider expectation to resource the gap left by mainstream assistive technology", "should, a duty on the provider", "all MSOR courses", "1.36, first item",
        "that the other two items of 1.36 carry the same force", "1.35 (specialist technology) and 1.28 (support for staff)"),
  aad=D("a team assumes the institution's standard captioning or screen reader is enough for mathematical material", "Frame it for staff as a budget and planning question.",
        "which tools fail on your notation today, and what would replace them?", "putting the duty to a student"))

s('1.37', type='requirement', force='must', appliesTo='captured, online and in-person delivery', award=[HON, IM, TM],
  verbs=['increase', 'capture', 'ensure'], about='capture, captions and visibility', **PROV,
  para="Online, hybrid or blended elements and captured sessions can widen access; suitable technology must be in place to capture live written work and caption it accurately, and in the room boards and displays must be visible.",
  prac="Where you capture or caption sessions, the technology must record extended written working and caption it accurately; in physical rooms, boards and displays must be visible to everyone.",
  aaw=W("a provider requirement, worded 'is required' and 'is essential', on capture technology, captions and visibility", "must, a duty on the provider",
        "all MSOR courses", "1.37", "that it requires any one delivery mode", "1.40 (flexible pedagogy) and 3.37 (teaching spaces)"),
  aad=D("a team plans recorded lectures with board work, or chooses rooms", "Frame it for staff as a minimum for any captured or in-person session.",
        "can a student watching the recording read every line of working, and are the captions accurate for symbols?", "putting the requirement to a student"))

s('1.38', type='requirement', force='describes', appliesTo='those in support roles', award=[HON, IM, TM],
  verbs=['need'], about='support workers knowing subject terminology', **PROV,
  para="Scribes, notetakers, readers, communication support workers and others in support roles need to know the subject's terms and symbols, because a small change in a symbol can alter the meaning entirely.",
  prac="Those who support disabled students (scribes, notetakers, readers, communication support workers) need training in MSOR terminology and notation, since one wrong symbol can change what is meant.",
  aaw=W("a requirement on support arrangements, worded 'need to' and recorded as describes (Part E)", "an obligation outside the modal verbs, read as close to should",
        "all MSOR courses", "1.38", "that it sets a standard for students", "1.34 (special notation) and 1.31 (reasonable adjustments)"),
  aad=D("a disability service assigns support workers to MSOR students", "Frame it for staff as a training and matching question.",
        "do the support workers your students rely on read mathematical notation confidently?", "putting it to a student as their responsibility"))

s('1.42', type='expectation', force='should', appliesTo='assessment design', award=[HON, IM, TM],
  verbs=['anticipate', 'remove'], about='removing irrelevant barriers in assessment', **PROV,
  para="Assessment design should foresee and remove barriers unrelated to what is being measured, such as heavy interpretation of material, distracting images or unfamiliar context, customs or colloquial language.",
  prac="When designing assessments you should anticipate and strip out barriers that have nothing to do with the knowledge or skill measured: needless reading load, distracting imagery, unfamiliar cultural context or idiom.",
  aaw=W("a provider expectation on accessible assessment design", "should, a duty on whoever designs assessment", "all MSOR assessment", "1.42",
        "that it lowers the standard assessed", "3.47 and 3.48 (assessment design and EDI) and the threshold lists 4.5 and 4.6"),
  aad=D("a teacher drafts or reviews an exam paper or coursework brief", "Frame it for staff as a check that each question tests only what it means to.",
        "what in this question would slow a student who knows the mathematics perfectly well?", "suggesting the standard itself should fall"))

s('1.50', type='expectation', force='should', appliesTo='courses', award=[HON, IM, TM],
  verbs=['embedded'], about='employability embedded in the course', **PROV,
  para="Helping students into work is an essential part of the degree; students own their career development and other services help, but employability skills should be built into the course, enterprise and entrepreneurship education included.",
  prac="Students carry personal responsibility for their careers and central services help, but you should embed employability skills in the course itself, through enterprise and entrepreneurship education among other means.",
  aaw=W("a provider expectation to embed employability in the course", "should, a duty on the provider; the student's own responsibility is noted beside it",
        "all MSOR courses", "1.50", "that careers services alone meet it", "1.53 (enterprise education defined), 1.60 and the professional standards 4.9.b1 to 4.9.b8"),
  aad=D("a team treats careers work as something outside the curriculum", "Frame it for staff as course design, not an add-on.",
        "where in the modules do students build and recognise employability skills?", "putting the provider's duty to a student"))

s('1.55', type='expectation', force='should', appliesTo='group work and projects', award=[HON, IM, TM],
  verbs=['supported', 'foster'], about='preparing students for group work', **PROV,
  para="Projects and dissertations build reflection, responsibility and supervised risk-taking, and group modules build influencing, leadership, negotiation and communication; before group work, students should be supported to understand how working with others differs from working alone and how good groups behave.",
  prac="Before any group task you should help students understand how collaborative work differs from individual work, how groups are managed and what good group behaviour looks like; projects, group modules and work with large data sets then build enterprise skills.",
  aaw=W("a provider expectation to prepare students for group work, set among enterprise competencies", "should, a duty on the provider",
        "all MSOR courses", "1.55", "that every module must include group work", "4.9.b3 (working in groups) and 3.26.b9 (collaboration)"),
  aad=D("a team plans assessed group work or students complain about group dynamics", "Frame it for staff as preparation students need before the task begins.",
        "what do students learn about working in a group before the group task starts?", "giving the duty to a student"))

s('1.60', type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
  award=UG, domain='generic-skill', verbs=['reflect', 'understand', 'articulate', 'build'], about='explaining enterprise and employability development',
  para="To build on these skills later in work or study, graduates need to be able to reflect on, understand and explain how their degree let them develop enterprise, entrepreneurship and wider employability skills.",
  prac="Graduates need to be able to reflect on and explain how the course developed their enterprise and employability skills; give them chances to practise saying so.",
  ben="To make the most of your skills in a job or further study, you need to be able to reflect on, understand and explain how your degree helped you develop enterprising and employability skills.",
  aaw=W("a learner expectation worded 'need to', recorded as describes (Part E)", "an expectation, not a threshold requirement",
        "graduates of honours and integrated master's courses, read at fheq:6 beside qaa/fheq-2024/4.15.b9.3", "1.60",
        "that it is a condition of the award", "4.9.b8 (self-learning and reflection) and qaa/fheq-2024/annex-d/transferable/r5/3rd"),
  aad=D("a student prepares for applications or interviews, or a tutor plans reflective work", "Put it to a student in the second person: you will need to say what your degree taught you beyond the mathematics.",
        "what have you done on your course that shows enterprise, and how would you describe it to an employer?", "presenting it as something examined for the degree"))

# ======================================================================== section 2
s('2.5', type='expectation', force='should', appliesTo="bachelor's degrees with honours", award=HON,
  verbs=['provide', 'prepare'], about="what a bachelor's degree should give students", rung='none', addressee='provider', level='fheq:6', domain='none', ben=NA_PROV,
  para="Undergraduates may take a bachelor's degree with honours (FHEQ 6, FQHEIS 10) or an integrated master's with honours (FHEQ 7, FQHEIS 11), each with its own outcomes; bachelor's degrees should give students subject knowledge, understanding and skills and wider transferable skills that equip them for many careers.",
  prac="Your bachelor's course should equip students with the knowledge, understanding and skills of the subject and with transferable skills that open a wide range of careers; integrated master's courses carry their own higher outcomes.",
  aaw=W("a provider expectation on what a bachelor's degree should give students, with the stated level crosswalk", "should, a duty on the provider",
        "the bachelor's degree with honours at fheq:6 and fqheis:10", "2.5", "that it sets the integrated master's outcomes", "4.5 (the honours threshold) and qaa/fheq-2024/4.15.b1 to 4.15.b9.3"),
  aad=D("a team writes the aims of a bachelor's programme", "Frame it for staff as the two halves every bachelor's aim needs: subject and transferable.",
        "which aims cover the subject itself and which cover the skills that carry into any career?", "putting the provider's duty to a student"))

s('2.9', type='expectation', force='should', appliesTo='credit-bearing placements', award=UG,
  verbs=['integrated', 'relate', 'use'], about='integrating credit-bearing placements', **{k: v for k, v in PROV.items()},
  para="Bachelor's and integrated master's degrees may include study away from the institution, with credit set by the workload; where a placement carries credit it should be built into the programme so students can link the experience to their academic study.",
  prac="If a placement earns credit, you should integrate it into the programme so students connect what they did and learned there with their academic work.",
  aaw=W("a provider expectation on credit-bearing placements", "should, a duty on the provider", "bachelor's and integrated master's courses that carry placement credit", "2.9",
        "that placements are required", "2.8 (learning outside the institution) and 2.27 (industry partnerships)"),
  aad=D("a team designs a placement year or decides whether it carries credit", "Frame it for staff as joining the placement to the taught programme.",
        "how will students bring what they learn on placement back into their modules?", "giving the duty to a student"))

s('2.11', type='expectation', force='should', appliesTo='integrated degree apprenticeships', award=UG,
  verbs=['follow'], about='apprenticeships follow this statement', **PROV,
  para="The academic part of an integrated degree apprenticeship in the subject should follow this statement's guidance; degree apprenticeships are described more fully in QAA's Characteristics Statement on apprenticeships.",
  prac="If you run an integrated degree apprenticeship in MSOR, its academic component should follow the guidance of this statement, read with the Characteristics Statement for apprenticeships.",
  aaw=W("a provider expectation that apprenticeships meet the statement's guidance", "should, a duty on the provider", "the academic component of integrated degree apprenticeships", "2.11",
        "that it covers the work-based component", "the Characteristics Statement for Higher Education in Apprenticeships (not yet ingested) and 4.5"),
  aad=D("a team designs or reviews a degree apprenticeship in data science or mathematics", "Frame it for staff as the academic floor the apprenticeship shares with other degrees.",
        "does the academic component reach the same threshold as your bachelor's degree?", "giving the duty to an apprentice"))

s('2.12', type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='undergraduates progressing through their course', addressee='learner',
  award=UG, domain='none', verbs=['progress', 'meeting'], about='progression towards threshold; readiness for postgraduate study',
  para="Students move up the levels of a bachelor's or integrated master's under their institution's rules; each level is expected to build towards reaching at least the threshold subject-specific and generic skills by the end, and a student with a second-class degree or better is expected to be ready for postgraduate study.",
  prac="Plan each level so it builds towards at least the threshold standards by the end; a graduate with a second-class degree or better is expected to be ready for postgraduate study, though each course sets its own entry rules.",
  ben="As you move from one year to the next, each stage builds you towards at least the threshold level of subject and general skills by the end; with a second-class degree or better you can expect to be ready for postgraduate study, though each course sets its own entry rules.",
  aaw=W("a progression expectation worded 'it is expected that', recorded as describes (Part E)", "an expectation, not a rule for progression decisions",
        "bachelor's degrees with honours (fheq:6, fqheis:10) and integrated master's (fheq:7, fqheis:11)", "2.12",
        "that a second-class degree guarantees postgraduate entry", "4.5 and 4.6 (the thresholds) and the progression thread in the FHEQ's SL4"),
  aad=D("a student asks whether they are on track, or whether a 2.2 opens postgraduate study", "Put it to a student in plain words: each year should move you towards the threshold.",
        "which threshold skills do you feel secure in now, and which still need work?", "promising postgraduate entry or treating the threshold as the whole aim"))

s('2.13', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='joint honours and interdisciplinary undergraduates', addressee='learner',
  award=UG, domain='subject-skill', verbs=['achieve'], about='core skills of each subject in a combination',
  para="Students on joint honours or interdisciplinary courses will reach the core of the specific and general skills of each subject they combine.",
  prac="Joint honours and interdisciplinary students will reach the core subject-specific and generic skills of each subject; make sure the MSOR half delivers its core.",
  ben="If you study MSOR jointly with another subject, or on an interdisciplinary course, you will gain the core subject and general skills of each subject you combine.",
  aaw=W("an expected outcome for joint and interdisciplinary students", "will, an expected outcome",
        "joint honours and interdisciplinary undergraduates, at fheq:6", "2.13", "that joint students meet the whole single honours list",
        "2.7 (joint honours described), 4.3 (data science and joint courses) and 4.5"),
  aad=D("a joint honours student asks what they are expected to master in MSOR", "Put it to a student in the second person: you will cover the core, not everything a single honours student covers.",
        "which parts of the MSOR core does your course include, and where do they sit?", "presenting the full single honours list as their minimum"))

s('2.18', type='expectation', force='should', appliesTo='option choices', award=UG,
  verbs=['have', 'select', 'made'], about='optional modules and guidance', **PROV,
  para="Students should have some freedom to choose optional modules that suit their interests, and suitable advice on those choices should be available.",
  prac="You should offer students some optional modules matched to their interests and give them proper guidance on choosing among them.",
  aaw=W("a provider expectation on optional modules and guidance", "should, a duty on the provider", "undergraduate MSOR courses", "2.18",
        "that it overrides prerequisite structures", "2.19 (prerequisites limit flexibility)"),
  aad=D("a team reviews its option structure or advising", "Frame it for staff as choice with guidance.",
        "how do students find out what each option leads to before they choose?", "telling a student they are entitled to any option"))

s('2.24', type='expectation', force='should', appliesTo='courses', award=[HON, IM, TM],
  verbs=['respond', 'anticipate', 'take', 'make'], about='courses flexible to change and to learners', **PROV,
  para="Courses should be flexible enough to respond to, and anticipate, change in the subject, its links with other disciplines and the needs of graduates and employers, and should take account of learners' needs, making reasonable adjustments where required.",
  prac="You should keep the course flexible enough to anticipate and respond to change in the discipline, in neighbouring fields and in what graduates and employers need, and make reasonable adjustments for learners as required.",
  aaw=W("a provider expectation on course flexibility and reasonable adjustments", "should, a duty on the provider", "all MSOR courses", "2.24",
        "that it is the legal duty itself", "2.21 to 2.23 (flexible approaches) and 1.31 (reasonable adjustments)"),
  aad=D("a periodic review asks how the course keeps current", "Frame it for staff as a review question about change.",
        "what has changed in the subject or in employers' needs since the course was last revised?", "giving the duty to a student"))

s('2.30', type='expectation', force='should', appliesTo='delivery partners', award=[HON, IM, TM],
  verbs=['develop', 'ensure', 'meet'], about='oversight of partners in delivery', **PROV,
  para="Work with employers brings students many benefits and can shape the curriculum; where partners take part in delivering a degree, providers should set up oversight so the partners meet each relevant safeguard, quality standard and expectation.",
  prac="Where employers or other partners help deliver the degree (degree apprenticeships, for example), you should set up oversight so they meet the relevant safeguards, quality standards and expectations.",
  aaw=W("a provider expectation to oversee partners in delivery", "should, a duty on the provider", "courses delivered with partners", "2.30",
        "that employer involvement is required", "2.27 (industry partnerships) and 2.11 (apprenticeships)"),
  aad=D("a team plans delivery with an employer", "Frame it for staff as governance the partnership needs.",
        "who checks that the partner's part of delivery meets your standards?", "giving the duty to a student"))

# ======================================================================== section 3
s('3.2', type='requirement', force='must', appliesTo='subject-specific knowledge at higher levels', award=[HON, IM, TM],
  verbs=['restricted', 'welcomed'], about='variety of advanced subject knowledge', rung='none', addressee='provider', level='none', domain='none',
  ben=('n/a', 'a constraint on how courses and this statement are applied, not an outcome for the student'),
  para="Courses build subject-specific knowledge and skills; at higher levels these differ between graduates by what each pursued, and this variety, natural to the subject, is welcome and must not be limited at all, though a core shared by all graduates can be seen.",
  prac="Graduates' advanced subject knowledge and skills will differ with the areas they chose; you must not restrict that diversity, though all graduates still share an identifiable core.",
  aaw=W("a requirement that the variety of advanced subject knowledge is not restricted", "must, a constraint on design and on how the statement is used",
        "all MSOR courses", "3.2", "that the statement sets a common advanced syllabus", "3.4 (no comprehensive content list) and 3.8 (the common ground)"),
  aad=D("someone uses the statement to argue for a fixed advanced syllabus", "Frame it for staff as protection for diverse specialisation.",
        "what core does every graduate share, and where may they rightly differ?", "putting the constraint to a student"))

s('3.5', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject', addressee='learner', award=UG,
  domain='generic-skill', verbs=['produce'], about='numeracy, computing and modelling as general skills',
  para="Courses will also produce graduates with well-developed general skills; plainly they should be highly numerate, and most will be competent with computing and modelling applications.",
  prac="Your graduates will have strong general skills: they should be highly numerate, and most will handle computing and modelling applications competently.",
  ben="You will also develop strong general skills: you will be highly numerate and, like most of your peers, able to use computing and modelling with confidence.",
  aaw=W("an expected outcome on general skills", "will, an expected outcome (with should for numeracy)", "graduates at fheq:6, beside qaa/fheq-2024/4.15.b2 and spine:6",
        "3.5", "that every graduate is a modelling specialist", "3.26.b6 (numeracy), 3.26.b7 (software) and qaa/fheq-2024/annex-d/transferable/r1/3rd"),
  aad=D("a student wonders what they gain beyond the mathematics itself", "Put it to a student in the second person, naming numeracy, computing and modelling.",
        "where have you used computing or modelling on your course so far?", "presenting high numeracy as optional"))

s('3.9', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject', addressee='learner', award=UG,
  domain='knowledge', verbs=['develop', 'have'], about='knowledge of a range of areas',
  para="Courses will give graduates knowledge of a range of areas of the subject, with understanding of how results are derived and applied that matches where the course sits between practice-based and theory-based.",
  prac="Graduates will know a range of MSOR areas; the depth to which they understand derivations and applications will follow your course's place between theory and practice.",
  ben="You will know a range of areas across mathematics, statistics and operational research, understanding how results are derived and applied to the depth your course's balance of theory and practice calls for.",
  aaw=W("an expected knowledge outcome", "will, an expected outcome", "graduates at fheq:6, beside qaa/fheq-2024/4.15.b1",
        "3.9", "that every course covers the same areas to the same depth", "3.8 (common ground), 3.10 to 3.12 (areas by field) and 4.5.b1"),
  aad=D("a student asks why their course is more applied or more theoretical than a friend's", "Put it to a student in plain words: breadth is expected, depth follows the course style.",
        "which areas have you met so far, and how far does your course ask you to derive results?", "treating one course's depth as the minimum for all"))

s('3.11', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of statistics courses', addressee='learner', award=UG,
  domain='subject-skill', verbs=['use'], about='using a statistical package',
  para="Statistics courses give graduates core mathematics and several major statistical areas, such as inference, likelihood, linear modelling, time series, stochastic processes, exploratory work and analytics; graduates are able to analyse data with a statistical package.",
  prac="Statistics graduates will be able to analyse data with a statistical package, on a base of core mathematics and major statistical topics.",
  ben="If you study statistics, you will be able to use a statistical software package to analyse data, building on core mathematics and major areas of statistics.",
  aaw=W("an expected skill outcome for statistics courses", "will (worded 'are able to')", "graduates of statistics courses at fheq:6", "3.11",
        "that it applies to every MSOR course", "3.17 (programming and software), 4.5.b7 and 3.26.b7"),
  aad=D("a statistics student asks what software skill is expected", "Put it to a student in the second person.",
        "which package have you used to analyse a real data set from start to finish?", "suggesting a particular package is required"))

s('3.17', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject', addressee='learner', award=UG,
  domain='subject-skill', verbs=['have'], about='programming and specialist software',
  para="Courses give graduates some knowledge of programming for computation; since computation and software are central to data analysis at work, graduates will be familiar with at least one programming language, will have used specialist software on the problems in hand and, where feasible, will know how its algorithms work.",
  prac="Graduates will know at least one programming language and will have used specialist software on real problems; where you can, teach the algorithms behind it.",
  ben="You will know at least one programming language, will have used specialist software on real problems and, where you can, will understand the algorithms behind it.",
  aaw=W("an expected outcome on programming and software", "will, an expected outcome", "graduates at fheq:6", "3.17",
        "that a named language is required", "4.5.b7 (the honours threshold item), 4.6.b7 and 3.39"),
  aad=D("a student asks how much programming they need", "Put it to a student in the second person: at least one language, used on real problems.",
        "which language are you most at ease in, and what problem have you solved with it?", "naming a language as compulsory"))

s('3.18', type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='all graduates of the subject', addressee='learner', award=UG,
  domain='understanding', verbs=['have'], about='knowledge of modelling',
  para="Mathematical and statistical modelling represents processes abstractly; every graduate is expected to know and understand something of modelling, usually through problems from at least one application area.",
  prac="Every graduate is expected to have some knowledge and understanding of modelling, usually met through at least one application area; plan where the course teaches it.",
  ben="You can expect to come away with some knowledge and understanding of mathematical and statistical modelling, usually through problems from at least one area of application.",
  aaw=W("an expectation worded 'are expected to', recorded as describes (Part E)", "an expectation of all graduates", "graduates at fheq:6", "3.18",
        "that deep modelling expertise is expected of all", "3.19 (modelling techniques) and 3.27"),
  aad=D("a student on a theory-based course asks whether modelling matters to them", "Put it to a student in plain words: some modelling is expected of everyone.",
        "where have you built or used a model, and what did it leave out?", "presenting it as a specialist requirement"))

# 3.26 general skills (lead-in: general skills to be expected of all graduates)
L326 = dict(type='outcome', rung='none', force='describes', forceFrom='3.26', level='fheq:6', appliesTo='all graduates of the subject',
            addressee='learner', award=UG, domain='generic-skill')
A326 = ("a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says "
        "'are to be expected of' (Part E)")


def k326(n, verbs, about, para, prac, ben, beside, when, ask):
    s('3.26.b%d' % n, verbs=verbs, about=about, para=para, prac=prac, ben=ben, **L326,
      aaw=W(A326, "an expectation, developed to different extents on different courses", "graduates at fheq:6", '3.26, item %d' % n,
            "that every course develops it to the same degree", beside),
      aad=D(when, "Put it to a student in the second person and plain words.", ask, "treating it as examined on its own or as a threshold the award turns on"))


k326(1, ['learn'], 'study skills and independent learning',
     "Expected of all graduates: study skills, above all learning on one's own.",
     "Graduates are expected to have good study skills, especially independent learning; build these in from the start.",
     "You can expect to develop good study skills, above all the ability to learn on your own.",
     "qaa/fheq-2024/4.15.b5 and 3.36", "a student struggles to study between classes", "how do you work through new material when no one has explained it yet?")
k326(2, ['work', 'pursuing'], 'persistent independent problem-solving',
     "Expected of all graduates: working alone with patience and persistence until a problem is solved.",
     "Graduates are expected to work on their own with patience and persistence, seeing problems through to the end.",
     "You can expect to become able to work on your own with patience and persistence, seeing a problem through to its end.",
     "qaa/fheq-2024/4.15.b9.1 and 4.6.b8", "a student gives up early on long problems", "what do you do when a problem has not given way after an hour?")
k326(3, [], 'managing processes and deadlines',
     "Expected of all graduates: managing processes and deadlines efficiently.",
     "Graduates are expected to manage their processes and deadlines efficiently; give them practice with real schedules.",
     "You can expect to learn to manage your work and deadlines efficiently.",
     "qaa/fheq-2024/annex-d/transferable/r3/3rd", "a student keeps missing deadlines", "how do you plan your week when several deadlines fall close together?")
k326(4, ['displaying', 'address'], 'adaptability to new problems',
     "Expected of all graduates: adaptability, especially readiness to take on new problems from unfamiliar areas.",
     "Graduates are expected to be adaptable, ready to tackle new problems from new areas.",
     "You can expect to become adaptable, ready to take on new problems from areas you have not met before.",
     "qaa/fheq-2024/4.15.b9.2 and 4.9.b2", "a student is anxious about unfamiliar problem types", "when did you last tackle a problem from an area you had not studied?")
k326(5, ['transfer', 'assess', 'approach'], 'transferring knowledge and analytical approach',
     "Expected of all graduates: carrying knowledge from one setting to another, judging problems logically and tackling them analytically.",
     "Graduates are expected to transfer knowledge between contexts and to assess and approach problems logically and analytically.",
     "You can expect to learn to take what you know into new settings and to judge and tackle problems logically.",
     "qaa/fheq-2024/4.15.b7, 3.25 and 4.5.b5", "a student cannot see how a technique applies outside its module", "where else could you use the method you learned this term?")
k326(6, [], 'numeracy',
     "Expected of all graduates: highly developed numeracy, at ease with numerical ideas and arguments at every stage of work.",
     "Graduates are expected to be highly numerate and fully comfortable with numerical concepts and arguments throughout their work.",
     "You can expect to become highly numerate and fully at ease with numbers and numerical arguments in everything you do.",
     "qaa/fheq-2024/annex-d/transferable/r1/3rd and 3.5", "a student doubts the value of numeracy beyond exams", "where do you check whether a numerical answer is sensible?")
k326(7, ['apply'], 'using specialist software',
     "Expected of all graduates: using specialist software appropriately.",
     "Graduates are expected to apply specialist software appropriately; give them practice choosing the right tool.",
     "You can expect to learn to use specialist software well and for the right jobs.",
     "4.5.b7, 3.17 and qaa/fheq-2024/4.15.b2", "a student asks which software skills count", "how do you decide which software to use for a task?")
k326(8, ['obtain', 'referred'], 'IT skills and sourcing information',
     "Expected of all graduates: IT skills and finding information from varied sources, always citing them properly.",
     "Graduates are expected to have IT skills and to gather information from many sources, referencing each one properly.",
     "You can expect to develop IT skills and to find information from many sources, always citing them properly.",
     "4.9.b5 and qaa/fheq-2024/annex-d/knowledge/r3/3rd", "a student is unsure how to reference sources in a technical report", "how do you record where each piece of information came from?")
k326(9, ['working', 'building'], 'collaboration',
     "Expected of all graduates: working with others and building on their work.",
     "Graduates are expected to collaborate and build on others' work.",
     "You can expect to learn to work with others and build on what they have done.",
     "4.9.b3, 1.55 and qaa/fheq-2024/annex-d/transferable/r2/3rd", "a student prefers to work alone", "what did you add to the last piece of work you did with others?")
k326(10, ['communicate'], 'communicating results',
     "Expected of all graduates: communication, verbal and non-verbal, and presenting results clearly in several forms such as reports, talks and posters.",
     "Graduates are expected to communicate verbally and non-verbally and to present results clearly in reports, presentations and posters.",
     "You can expect to learn to communicate in speech and in writing, presenting results clearly in reports, talks and posters.",
     "4.5.b6, 4.9.b4 and qaa/fheq-2024/4.15.b8", "a student prepares a report or presentation", "who is your audience, and what must they take away?")
k326(11, ['handling'], 'ethical issues, personal data and impact',
     "Expected of all graduates: knowledge of ethical issues, including care with personal data and the effects of the subject when applied.",
     "Graduates are expected to know the ethical issues of the field, including sensitive handling of personal data and the impact of applying MSOR.",
     "You can expect to understand the ethical issues in your field, including care with personal data and the effects of applying mathematics.",
     "4.9.b6, 4.9.b7 and 3.13", "a student works with personal data or a model with social effects", "who could be affected by this analysis, and how?")

s('3.28', type='expectation', force='should', appliesTo='choice of teaching approach', award=[HON, IM, TM],
  verbs=['choose', 'evaluated', 'given'], about='choosing teaching approaches', **PROV,
  para="Teaching and learning methods vary with course style, content, the learners' level and route and the resources at hand; providers should choose carefully after weighing many pedagogies, expecting to mix approaches even within one module while keeping the student's experience coherent across the course.",
  prac="You should choose teaching approaches deliberately, after weighing a wide range of pedagogies; expect to combine several, even in one module, but keep the student's experience coherent from start to finish.",
  aaw=W("a provider expectation on choosing teaching approaches", "should, a duty on the provider", "all MSOR courses", "3.28",
        "that any one method is required", "3.29 to 3.31 (methods in use) and the PSF dimensions only where staff practice is the subject"),
  aad=D("a teaching team plans or reviews a module's delivery", "Frame it for staff as a choice to justify.",
        "why this mix of methods, and does it hang together with the rest of the course?", "giving the duty to a student"))

s('3.32', type='expectation', force='should', appliesTo='peer learning', award=[HON, IM, TM],
  verbs=['ensure', 'promote', 'encourage'], about='peer learning and spaces for it', **PROV,
  para="Practice and repetition suit collaborative learning, and peer learning, in class or student-led, enriches each learner; providers should make formal and informal spaces available for group work and should promote peer learning in ways consistent with good academic practice, so students learn from others without compromising integrity.",
  prac="You should provide formal and informal spaces for group study and actively encourage peer learning, guided by good academic practice, so students learn from one another while keeping their work their own.",
  aaw=W("a provider expectation on peer learning and space for it", "should, a duty on the provider", "all MSOR courses", "3.32",
        "that collaboration on assessed work is permitted", "3.51 (integrity) and 3.26.b9 (collaboration)"),
  aad=D("staff plan study spaces or worry about collusion", "Frame it for staff as encouraging collaboration with clear integrity rules.",
        "where can students work together, and do they know where shared work ends and their own begins?", "giving the duty to a student"))

s('3.34', type='expectation', force='should', appliesTo='developing independent learners', award=[HON, IM, TM],
  verbs=['acknowledge', 'developing', 'recognising'], about='shared responsibility for independent learners', **PROV,
  para="Providers should accept that they share with students the responsibility for turning them into independent scholars and practitioners, which includes the scaffolding, confidence-building and opportunities students need to become effective independent learners.",
  prac="You should treat the growth of students into independent scholars as a responsibility you share with them, and supply the scaffolding, confidence-building and chances to practise that independent learning needs.",
  aaw=W("a provider expectation of shared responsibility for independent learning", "should, a duty on the provider", "all MSOR courses", "3.34",
        "that students carry it alone", "3.35, 3.36 and qaa/fheq-2024/4.15.b5"),
  aad=D("staff say students should simply be independent", "Frame it for staff as shared work with scaffolding.",
        "what scaffolding do first-year students get, and when is it withdrawn?", "giving the duty to a student"))

s('3.35', type='expectation', force='should', appliesTo='discipline skills for independent learning', award=[HON, IM, TM],
  verbs=['prioritise', 'equipping', 'recognise'], about='equipping students to learn on their own', **PROV,
  para="Students need a large base of knowledge and practised skill before they can tackle harder problems alone, especially in abstract areas; providers should put first the discipline skills that let students learn the subject independently, recognising that this enriches the provision.",
  prac="You should give priority to equipping students with the discipline skills to learn MSOR content on their own, since much knowledge and practice must come before they can tackle advanced problems independently.",
  aaw=W("a provider expectation to prioritise discipline skills for independent learning", "should, a duty on the provider", "all MSOR courses", "3.35",
        "that independence is expected from the start", "3.34 and 4.6.b8 (independent work at integrated master's)"),
  aad=D("a team debates how much to scaffold advanced material", "Frame it for staff as an investment that pays back later.",
        "which discipline skills do students need before they can learn a new topic on their own?", "giving the duty to a student"))

s('3.36', type='expectation', force='should', appliesTo='study skills and scheduling', award=[HON, IM, TM],
  verbs=['assist', 'model', 'explain', 'encouraged', 'timetable', 'schedule'], about='study skills, scholarly habits and consolidation time', **PROV,
  para="Providers should help students build study skills; tutors should model and explain the worth of work outside timetabled hours, such as reading ahead, checking arguments and independent practice; scholarly habits like experimenting with ideas and attempting incomplete solutions should be encouraged; and teaching and assessment should be timed to leave room to consolidate.",
  prac="You should develop students' study skills, model the value of independent work outside class (reading ahead, checking proofs, practising problems and code), encourage exploratory scholarship and schedule teaching and assessment so students have time to consolidate.",
  aaw=W("a provider expectation on study skills, scholarly habits and scheduling", "should, a duty on the provider and its tutors", "all MSOR courses", "3.36",
        "that it fixes hours of study", "3.26.b1 (study skills), 1.33 (well-curated courses) and 1.15"),
  aad=D("a tutor plans independent study or a team sets the assessment calendar", "Frame it for staff as modelling and timing.",
        "what do you show students about working outside class, and is there time between topics to consolidate?", "giving the duty to a student"))

s('3.39', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='students of the subject', addressee='both', award=UG,
  domain='subject-skill', verbs=['develop', 'encounter', 'use'], about='computational thinking and programming',
  para="Computing runs through the subject, concentrated in modules or spread across a course; students develop computational thinking, should meet one programming language or more and may draw on specialist software such as computer algebra, numerical and statistical packages and optimisation software, beside spreadsheets, graphics and typesetting tools.",
  prac="Students should meet at least one programming language and develop computational thinking; decide whether computing sits in dedicated modules or runs through the course, and which specialist tools students use.",
  ben="During your course you should meet at least one programming language and develop computational thinking, and you may use specialist software such as computer algebra, statistical packages or optimisation tools.",
  aaw=W("an expectation on computing in teaching and learning", "should for meeting a programming language; may for specialist software", "students at fheq:6",
        "3.39", "that every tool listed is required", "3.17, 4.5.b7 and 3.26.b7"),
  aad=D("a student or team asks how much computing the course should include", "Put it to a student in the second person; to staff, frame it as a placement decision.",
        "where in the course do students write code, and on what kind of problem?", "presenting the example tools as a required list"))

s('3.42', type='expectation', force='should', appliesTo='staff development', award=[HON, IM, TM],
  verbs=['support', 'ensure', 'engage'], about='staff training and professional development', **PROV,
  para="Teaching keeps changing and innovation should be evaluated and shared; providers should support new staff to train in ways suited to the discipline and should ensure postgraduate tutors receive enough discipline-relevant training, and every member of staff carries a responsibility to keep developing professionally.",
  prac="You should give new MSOR staff discipline-appropriate training and make sure postgraduate tutors are properly trained for their role; every member of staff is responsible for their own continuing professional development.",
  aaw=W("a provider expectation on staff training, with a staff responsibility for development", "should for the provider; 'responsibility' for staff (Part E)",
        "all MSOR courses", "3.42", "that it sets a student standard", "the PSF 2023 dimensions (std:doc:advancehe-psf-dimensions-2023-framework), since this is about teaching practice"),
  aad=D("a department plans induction for new lecturers or postgraduate tutors", "Frame it for staff as discipline-specific development.",
        "what training in teaching mathematics did your postgraduate tutors receive before their first class?", "giving the duty to a student"))

s('3.43', type='expectation', force='should', appliesTo='quality assurance', award=[HON, IM, TM],
  verbs=['engage', 'maintain', 'enhance'], about='engaging with quality assurance', **PROV,
  para="Providers should take part in quality assurance processes, local, statutory or tied to accreditation, to keep up and improve the quality of their provision.",
  prac="You should engage with quality assurance (your institution's own processes, statutory ones tied to degree awarding powers and those of accrediting bodies) to maintain and enhance provision.",
  aaw=W("a provider expectation to engage with quality assurance", "should, a duty on the provider", "all MSOR courses", "3.43",
        "that the statement is itself a quality assurance requirement", "2.31 to 2.34 (monitoring, review and accreditation)"),
  aad=D("a team prepares for review or accreditation", "Frame it for staff as continuous improvement.",
        "which quality processes touch this course, and what did the last one change?", "giving the duty to a student"))

s('3.47', type='expectation', force='should', appliesTo='assessment design', award=[HON, IM, TM],
  verbs=['consider', 'demonstrate'], about='general characteristics as outcomes; EDI in assessment design', **PROV,
  para="The subject's general characteristics, such as precision with symbols, spatial awareness, pattern recognition, complex logical reasoning, proof and clear expression, can serve as intended outcomes of every course, and some assessments will test them; assessment design should take account of the equality, diversity and inclusion issues set out in 1.27.",
  prac="Treat the discipline's general characteristics (symbolic precision, spatial awareness, pattern-spotting, logical agility, proof and clarity) as outcomes some assessments test, and you should design assessment with the EDI points of 1.27 in mind.",
  aaw=W("a provider expectation on assessment design, with the subject's general characteristics as outcomes", "should, a duty on whoever designs assessment",
        "all MSOR assessment", "3.47", "that each characteristic is a separate threshold item", "1.27, 3.48 and 4.5"),
  aad=D("a team maps assessments to outcomes or reviews them for inclusion", "Frame it for staff as two checks: what the assessment tests and who it may disadvantage.",
        "which assessment tests proof or clarity of expression, and how would a student from a different background experience it?", "giving the duty to a student"))

s('3.48', type='expectation', force='should', appliesTo='assessment design', award=[HON, IM, TM],
  verbs=['designed', 'taking'], about='accessible and inclusive assessment', **PROV,
  para="Assessment may use many methods suited to context and purpose, since learners show different aptitudes in different formats, with automatic online marking common for formative work; every assessment, invigilated examinations included, should be designed with accessibility and equality, diversity and inclusion in mind.",
  prac="Use a range of assessment methods, since students perform differently across formats; you should design every assessment, traditional exams included, with accessibility and EDI considered from the start.",
  aaw=W("a provider expectation on accessible and inclusive assessment", "should, a duty on whoever designs assessment", "all MSOR assessment", "3.48",
        "that examinations are exempt", "1.42 (removing barriers) and 3.47"),
  aad=D("a team reviews its assessment mix or an exam format", "Frame it for staff as design from the start, not adjustment later.",
        "how did accessibility and inclusion shape this exam before any adjustment was asked for?", "giving the duty to a student"))

# ======================================================================== section 4
s('4.4', type='expectation', force='should', appliesTo='judging achievement above threshold', award=[HON, IM, TM],
  verbs=['perform', 'refer', 'build'], about='Annex D for performance above threshold; master\'s outcomes', rung='none', addressee='provider', level='fheq:6', domain='none',
  ben=('n/a', 'a duty on the provider in judging and evidencing achievement'),
  para="Most students will do much better than the minimum threshold; each provider decides how to evidence this and should refer to Annex D's descriptions of the four honours classifications; master's graduates build on the level 6 and 10 outcomes, in more depth in a specialist area, to the outcomes the Frameworks set for their level.",
  prac="To judge achievement above the threshold you should use Annex D of the Frameworks (the descriptions of first, upper second, lower second and third-class honours) with your own method of evidence; for master's awards use the Frameworks' level 7 and 11 outcomes.",
  aaw=W("a provider expectation to use Annex D for performance above threshold", "should, a duty on the provider", "honours at fheq:6 and fqheis:10, with master's at fheq:7 and fqheis:11",
        "4.4", "that the statement itself defines classification bands", "qaa/fheq-2024/annex-d/summary/r1/3rd to r1/1st, the FHEQ's SL6 and 4.8 (the bases above threshold)"),
  aad=D("a team writes marking criteria or classification descriptors", "Frame it for staff as where to look once the threshold is met.",
        "how do your criteria for a 2.1 or a first relate to Annex D?", "giving the duty to a student or treating the threshold as the expected level"))

# 4.5 threshold, bachelor's degree with honours
L45 = dict(type='threshold', rung='threshold', force='should', forceFrom='4.5', level='fheq:6', appliesTo="graduates at the honours threshold",
           addressee='learner', award=HON)
BL45 = "To reach the minimum standard for an honours degree, you should be able to show "


def k45(n, verbs, about, domain, para, prac, ben, fw, ask, extra=''):
    s('4.5.b%d' % n, verbs=verbs, about=about, domain=domain, para=para, prac=prac, ben=BL45 + ben, **L45,
      aaw=W("a threshold standard the honours award requires, met overall rather than item by item (4.2)", "should, the issuer's word in the lead-in",
            "the bachelor's degree with honours at fheq:6 and fqheis:10", '4.5, item %d' % n, "that it describes typical or good performance, or that it holds at master's level",
            "4.6.b%d (the integrated master's threshold)%s and %s" % (n, extra, fw)),
      aad=D("a student asks what the minimum is for an honours degree, or a team checks a programme's outcomes", "Put it to a student in the second person as the floor, not the target; to staff, as the outcome every graduate must reach.",
            ask, "presenting it as what most students achieve, or reading the issuer's list aloud"))


k45(1, ['comprehend'], 'core body of knowledge and basic language', 'knowledge',
    "Should be able to show a reasonable grasp of the basic knowledge of the course, normally calculus, linear algebra and probability and statistics, and to follow the discipline's basic language.",
    "At threshold, graduates should be able to show a reasonable understanding of the course's core knowledge (usually calculus, linear algebra and probability and statistics) and of the subject's basic language.",
    "a reasonable understanding of the core of your course (usually calculus, linear algebra and probability and statistics) and follow the basic language of the subject.",
    "qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/3rd", "which parts of calculus, linear algebra and probability feel secure, and which do not?")
k45(2, ['solve'], 'calculation, manipulation and solving set problems', 'subject-skill',
    "Should be able to show reasonable skill at calculating and manipulating within that core, and some ability to solve problems set inside it.",
    "At threshold, graduates should be able to show reasonable skill in calculation and manipulation within the core and some capability to solve problems framed in it.",
    "reasonable skill at calculating and manipulating within that core knowledge, and some ability to solve problems set within it.",
    "qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r2/3rd", "can you carry a routine calculation through without slips, and solve a standard problem unaided?")
k45(3, ['showing', 'demonstrating'], 'applying concepts with justified choice of method', 'subject-skill',
    "Should be able to show concepts and principles applied in well-defined settings, with judgement in choosing and using tools and techniques and a justification of the methods used.",
    "At threshold, graduates should be able to apply concepts and principles in well-defined contexts, choose and use tools and techniques with judgement and justify their methods.",
    "that you can apply ideas and principles in clearly defined situations, choose and use tools and techniques sensibly and explain why your method fits.",
    "qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/annex-d/cognitive/r3/3rd", "why did you choose this method, and what would make another one better?")
k45(4, ['reasoning', 'identifying'], 'logical reasoning, assumptions and conclusions', 'subject-skill',
    "Should be able to show reasoning by logical argument, naming the assumptions made and the conclusions reached.",
    "At threshold, graduates should be able to reason through logical arguments, identifying the assumptions they rest on and the conclusions they reach.",
    "that you can reason with logical arguments, saying which assumptions you made and what conclusions follow.",
    "qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r2/3rd", "what did you assume at the start of that argument, and what exactly did you conclude?")
k45(5, ['comprehending', 'formulating', 'obtaining', 'drawing'], 'formulating and solving problems; valid inferences', 'subject-skill',
    "Should be able to show reasonable skill at understanding problems, putting them in mathematical form, solving them by suitable methods and drawing valid inferences.",
    "At threshold, graduates should be able to show reasonable skill in understanding a problem, formulating it mathematically, solving it by suitable methods and drawing valid inferences.",
    "reasonable skill at understanding a problem, writing it in mathematical form, solving it by a suitable method and drawing sound conclusions from the answer.",
    "qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r3/3rd", "how did you turn the problem in words into mathematics, and what does your answer tell you?")
k45(6, ['communicate', 'acknowledging'], 'communicating arguments and uncertainty', 'generic-skill',
    "Should be able to show logical arguments, evidence and conclusions communicated with reasonable accuracy and clarity, admitting the uncertainty of conclusions where fitting.",
    "At threshold, graduates should be able to communicate arguments, evidence and conclusions reasonably accurately and clearly, acknowledging uncertainty in conclusions where relevant.",
    "that you can explain arguments, evidence and conclusions reasonably accurately and clearly, saying how uncertain a conclusion is where that matters.",
    "qaa/fheq-2024/4.15.b8, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/transferable/r1/3rd", "how sure are you of that conclusion, and how would you say so in your report?", ', 3.26.b10')
k45(7, [], 'a programming language and MSOR technology', 'subject-skill',
    "Should be able to show they know one programming language or more and can use other suitable technology for the subject competently.",
    "At threshold, graduates should be able to show they know one programming language or more and use other suitable MSOR technology competently.",
    "that you know at least one programming language and can use other suitable mathematical software competently.",
    "qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r1/3rd", "which language and which tools could you use tomorrow on a new problem?", ', 3.17')

# 4.6 threshold, integrated master's degree
L46 = dict(type='threshold', rung='threshold', force='should', forceFrom='4.6', level='fheq:7', appliesTo="graduates at the integrated master's threshold",
           addressee='learner', award=IM)
BL46 = "To reach the minimum standard for an integrated master's degree, you should be able to show "


def k46(n, verbs, about, domain, para, prac, ben, fw, ask, below=True):
    side = ("4.5.b%d (the honours threshold it builds on) and %s" % (n, fw)) if below else ("the honours threshold list 4.5 (no matching item) and %s" % fw)
    s('4.6.b%d' % n, verbs=verbs, about=about, domain=domain, para=para, prac=prac, ben=BL46 + ben, **L46,
      aaw=W("a threshold standard the integrated master's award requires, met overall rather than item by item (4.2)", "should, the issuer's word in the lead-in",
            "the integrated master's degree at fheq:7 and fqheis:11", '4.6, item %d' % n, "that it holds for the bachelor's degree or that it is a typical rung", side),
      aad=D("an integrated master's student asks what the final-year minimum is, or a team sets level 7 outcomes", "Put it to a student in the second person as the floor for the master's award; to staff, as the level 7 outcome every graduate must reach.",
            ask, "presenting it as the honours minimum, or reading the issuer's list aloud"))


k46(1, [], 'main body of knowledge with advanced topics', 'knowledge',
    "Should be able to show a good grasp of the main knowledge of the course, some advanced topics included.",
    "At the integrated master's threshold, graduates should be able to show a good understanding of the course's main body of knowledge, including some advanced topics.",
    "a good understanding of the main knowledge of your course, including some advanced topics.",
    "qaa/fheq-2024/4.17.b1", "which advanced topics could you explain to a fellow student?")
k46(2, ['solving'], 'calculation and advanced problems', 'subject-skill',
    "Should be able to show good skill at calculating and manipulating the material and the capacity to solve advanced problems framed within it.",
    "At the integrated master's threshold, graduates should be able to show good skill in calculation and manipulation and be capable of solving advanced problems in the material.",
    "good skill at calculating and manipulating the material, and that you can solve advanced problems set within it.",
    "qaa/fheq-2024/4.17.b2", "what is the hardest problem you have solved unaided this year?")
k46(3, ['showing', 'demonstrating'], 'applying a range of concepts in loosely defined settings', 'subject-skill',
    "Should be able to show a range of concepts and principles applied in loosely defined settings, with good judgement in choosing and using tools and techniques and a justification of the methods used.",
    "At the integrated master's threshold, graduates should be able to apply a range of concepts in loosely defined contexts, with good judgement in choosing tools and a justification of methods.",
    "that you can apply a range of ideas in loosely defined situations, choosing tools and techniques with good judgement and explaining why your methods fit.",
    "qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b5", "how did you decide what the problem was before choosing a method?")
k46(4, ['developing', 'evaluating'], 'building and evaluating logical arguments', 'subject-skill',
    "Should be able to show good capability in building and judging logical arguments.",
    "At the integrated master's threshold, graduates should be able to show good capability in developing and evaluating logical arguments.",
    "that you can build logical arguments of your own and judge other people's well.",
    "qaa/fheq-2024/4.17.b4.1", "where does this published argument depend on an assumption it does not state?")
k46(5, ['comprehending', 'formulating', 'obtaining', 'drawing'], 'formulating and solving problems; valid inferences', 'subject-skill',
    "Should be able to show good skill at understanding problems, putting them in mathematical form, solving them by suitable methods and drawing valid inferences.",
    "At the integrated master's threshold, graduates should be able to show good skill in understanding, formulating and solving problems by suitable methods and drawing valid inferences.",
    "good skill at understanding a problem, writing it in mathematical form, solving it by a suitable method and drawing sound conclusions.",
    "qaa/fheq-2024/4.17.b5", "what would change in your conclusion if the problem were stated slightly differently?")
k46(6, ['acknowledging'], 'confident communication and uncertainty', 'generic-skill',
    "Should be able to show confident, effective communication of logical arguments, evidence and conclusions, accurate and clear, admitting uncertainty where fitting.",
    "At the integrated master's threshold, graduates should be able to communicate arguments, evidence and conclusions confidently, accurately and clearly, acknowledging uncertainty where relevant.",
    "that you can explain arguments, evidence and conclusions with confidence, accuracy and clarity, saying how uncertain they are where that matters.",
    "qaa/fheq-2024/4.17.b5 and spine:7", "how would you present this result to an audience that does not share your notation?")
k46(7, [], 'a programming language and MSOR technology', 'subject-skill',
    "Should be able to show they know one programming language or more and can use other suitable technology for the subject competently.",
    "At the integrated master's threshold, graduates should be able to show they know one programming language or more and use other suitable MSOR technology competently.",
    "that you know at least one programming language and can use other suitable mathematical software competently.",
    "qaa/fheq-2024/4.17.b2", "which tools did your project rely on, and could you have built any part yourself?")
k46(8, ['work', 'understand'], 'independent work and knowing when to seek help', 'generic-skill',
    "Should be able to show competent, independent working, awareness of one's own strengths and an understanding of when help is needed.",
    "At the integrated master's threshold, graduates should be able to work competently and independently, know their own strengths and recognise when they need help.",
    "that you can work competently on your own, know your strengths and recognise when you need to ask for help.",
    "qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b8.3", "when did you last decide to ask for help, and was it the right moment?", below=False)
k46(9, ['planning', 'conducting'], 'an advanced project', 'subject-skill',
    "Should be able to show competence in planning and carrying out an advanced project in mathematics, statistics, operational research or a related area.",
    "At the integrated master's threshold, graduates should be able to plan and carry out an advanced project competently, in one of the three fields or a neighbouring area.",
    "that you can plan and carry out an advanced project in mathematics, statistics, operational research or a related area.",
    "qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b6", "how did you plan your project, and what did you change when the plan met the problem?", below=False)

s('4.7', type='expectation', rung='none', force='will', level='fheq:7', appliesTo="taught postgraduate master's courses", addressee='both', award=TM,
  domain='none', verbs=['develop'], about="taught master's and the listed standards",
  para="Taught postgraduate master's courses will build some or all of the standards above, depending on the course, which may specialise within one part of the subject or combine it with another discipline.",
  prac="A taught master's will develop some or all of the threshold standards in 4.5 and 4.6, depending on whether it specialises within MSOR or combines it with another discipline; state which apply.",
  ben="On a taught master's course you will develop some or all of these standards, depending on whether your course specialises within the subject or combines it with another field.",
  aaw=W("an expectation that taught master's courses develop some or all of the listed standards", "will, an expectation varying by course",
        "taught postgraduate master's degrees at fheq:7 and fqheis:11", "4.7", "that every taught master's must meet the whole integrated master's list",
        "4.6.b1 to 4.6.b9, 4.10 and qaa/fheq-2024/4.17.b1 to 4.17.b8.3"),
  aad=D("a conversion or specialist master's team writes its outcomes, or a student asks what the statement expects of them", "Frame it for staff as a selection to justify; for a student, plainly and in the second person.",
        "which of the threshold standards does your course develop, and which does it leave aside?", "presenting the full integrated master's list as every taught master's minimum"))

# 4.9 professional standards (lead-in: graduates should be expected to)
L49 = dict(type='outcome', rung='none', force='should', forceFrom='4.9', level='fheq:6', appliesTo='graduates of the subject', addressee='learner', award=UG)


def k49(n, verbs, about, domain, para, prac, ben, fw, ask):
    s('4.9.b%d' % n, verbs=verbs, about=about, domain=domain, para=para, prac=prac, ben=ben, **L49,
      aaw=W("a professional standard expected of graduates, listed beside the academic thresholds", "should, the lead-in's word; not stated as a threshold",
            "graduates of honours and integrated master's courses, read at fheq:6 (4.10 deepens it at master's level)", '4.9, item %d' % n,
            "that it is a professional body's accreditation requirement", fw),
      aad=D("a student asks what employers or professional settings will expect, or a team maps transferable skills", "Put it to a student in the second person and plain words; to staff, as an outcome to build into modules.",
            ask, "presenting it as a pass or fail threshold, or reading the issuer's list aloud"))


k49(1, ['synthesize'], 'synthesising across branches', 'subject-skill',
    "Graduates should be expected to bring together information from different branches of the subject.",
    "Graduates should be able to synthesise information drawn from different branches of MSOR; design tasks that cross module boundaries.",
    "You should be able to bring together ideas and results from different branches of the subject.",
    "3.25 (transfer between contexts) and qaa/fheq-2024/4.15.b7", "when did you last use a result from one module to crack a problem in another?")
k49(2, ['apply'], 'critical thinking and problem-solving', 'generic-skill',
    "Graduates should be expected to use critical thinking and problem-solving on problems from within the subject and from other disciplines or applications.",
    "Graduates should apply critical thinking and problem-solving to problems from MSOR and from other disciplines and applications.",
    "You should be able to think critically and solve problems, both within the subject and in other fields where it is applied.",
    "3.26.b5 and qaa/fheq-2024/annex-d/summary/r4/3rd", "what problem from outside mathematics have you tackled with mathematical tools?")
k49(3, ['work', 'achieve'], 'working alone or in a group to an aim', 'generic-skill',
    "Graduates should be expected to work effectively alone or in a group towards a set aim.",
    "Graduates should work effectively on their own or in a group to achieve a specific aim.",
    "You should be able to work well on your own or as part of a group to reach a shared goal.",
    "3.26.b9, 1.55 and qaa/fheq-2024/annex-d/transferable/r2/3rd", "what did you contribute to your last group task, and what would you do differently?")
k49(4, ['communicate'], 'communicating to specialist and non-specialist audiences', 'generic-skill',
    "Graduates should be expected to communicate accurately and clearly, verbally or non-verbally, in varied formats, possibly to specialist and non-specialist audiences.",
    "Graduates should communicate accurately and clearly, spoken and written, in a variety of formats, which may include specialist and non-specialist audiences.",
    "You should be able to communicate accurately and clearly, in speech and writing and in different formats, to specialists and non-specialists alike.",
    "4.5.b6, 3.26.b10 and qaa/fheq-2024/4.15.b8", "how would you explain your last result to someone with no mathematics beyond school?")
k49(5, ['possess', 'select', 'employ', 'support'], 'digital capability', 'generic-skill',
    "Graduates should be expected to have digital capabilities: finding information and judging its reliability, using general IT and choosing and using digital tools that support mathematical thinking, reasoning and communication.",
    "Graduates should have digital capabilities: retrieving information and checking its reliability, general IT, and selecting digital tools to support mathematical reasoning and communication.",
    "You should be confident with digital tools: finding information and checking whether it can be trusted, everyday IT, and choosing software that helps you think, reason and communicate mathematically.",
    "3.26.b8 and qaa/fheq-2024/annex-d/transferable/r1/3rd", "how do you check whether a source or a piece of software output can be trusted?")
k49(6, ['work'], 'professional and legal frameworks, EDI and sustainability', 'generic-skill',
    "Graduates should be expected to be aware that work must sit within professional and legal frameworks, data security, EDI and sustainability among them, each in the subject's setting.",
    "Graduates should be aware of the need to keep their work inside professional and legal frameworks, such as those on data security, EDI and sustainability, as they bear on MSOR.",
    "You should be aware that your work has to fit professional and legal rules, including data security, equality, diversity and inclusion and sustainability, as they apply to mathematics.",
    "3.26.b11, qaa/fheq-2024/annex-d/professional/r2/3rd-1st and the theme statements 1.23 and 1.44 to 1.48", "which legal or professional rules applied to the data in your last project?")
k49(7, ['maintain'], 'ethical standards and wider implications', 'generic-skill',
    "Graduates should be expected to keep to suitable ethical standards and be aware of the wider consequences of their work.",
    "Graduates should keep to suitable ethical standards and stay alert to the wider consequences of what they do.",
    "You should keep to sound ethical standards and think about the wider effects of your work.",
    "3.26.b11, 3.13 and qaa/fheq-2024/annex-d/professional/r2/3rd-1st", "who might be affected by how your model is used, and how?")
k49(8, ['initiate', 'monitor'], 'self-directed learning and reflection', 'generic-skill',
    "Graduates should be expected to start their own learning and to check and adjust their plans of work in the light of reflection and feedback.",
    "Graduates should be able to initiate self-learning and monitor and adjust their own work plans in response to reflection and feedback.",
    "You should be able to start learning on your own and to check and adjust your plans as you reflect and receive feedback.",
    "3.26.b1, qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/transferable/r5/3rd", "what did you change in how you work after your last piece of feedback?")

s('4.10', type='expectation', rung='none', force='will', level='fheq:7', appliesTo="students at master's level", addressee='learner', award=[IM, TM],
  domain='generic-skill', verbs=['had'], about="deeper professional skills and independence at master's level",
  para="Master's-level students will have had deeper or broader experience of part of the professional skills listed, more experience of working independently and extra chances to devise new and creative approaches to non-standard problems.",
  prac="At master's level, graduates will have had deeper or broader experience of some of the 4.9 skills, more independent work and more chances to find creative approaches to non-standard problems; plan where these come.",
  ben="At master's level you will have gone deeper or wider in some of these professional skills, worked more independently and had more chances to find new, creative ways into unusual problems.",
  aaw=W("an expectation of deeper professional skill and independence at master's level", "will, an expected outcome", "integrated and taught master's degrees at fheq:7 and fqheis:11",
        "4.10", "that every 4.9 skill is deepened", "4.9.b1 to 4.9.b8, 4.6.b8 and qaa/fheq-2024/4.17.b6"),
  aad=D("a master's student asks how their skills should differ from a bachelor's graduate's", "Put it to a student in the second person: depth in some skills, more independence, more creativity.",
        "which professional skills have you taken further this year, and on what non-standard problem?", "presenting it as deepening every skill"))

GRADE = {}
TH = {'1.23': 'theme:edi', '1.25': 'theme:edi',
      '1.28': 'theme:accessibility', '1.29': 'theme:accessibility', '1.30': 'theme:accessibility', '1.33': 'theme:accessibility',
      '1.36.b1': 'theme:accessibility', '1.37': 'theme:accessibility', '1.38': 'theme:accessibility', '1.42': 'theme:accessibility',
      '1.50': 'theme:enterprise', '1.55': 'theme:enterprise', '1.60': 'theme:enterprise',
      '3.47': 'theme:edi', '3.48': 'theme:accessibility, theme:edi', '4.9.b6': 'theme:edi, theme:esd'}

S5 = dict(levels=[
    dict(id='fheq:6', role='cites', locator='D1, 2.5; 2.12; 4.4', descriptor='std:doc:qaa-fheq-2024-framework: qaa/fheq-2024/4.15.*', spine='spine:6'),
    dict(id='fheq:7', role='cites', locator='D1, 2.5; 2.12; 2.14', descriptor='std:doc:qaa-fheq-2024-framework: qaa/fheq-2024/4.17.*', spine='spine:7'),
    dict(id='fqheis:10', role='cites', locator='D1, 2.5; 2.12; 4.4', descriptor='std:doc:qaa-fqheis-2024-framework: 4.16', spine='spine:6'),
    dict(id='fqheis:11', role='cites', locator='D1, 2.5; 2.12; 2.14', descriptor='std:doc:qaa-fheq-2024-framework: qaa/fheq-2024/4.17.* (shared)', spine='spine:7')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis="stated (D1, 2.5; 2.12: \"FHEQ Level 6; FQHEIS Level 10\" for the bachelor's degree with honours; 4.4 \"Levels 6/10\")"),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.5; 2.12; 2.14: \"FHEQ Level 7; FQHEIS Level 11\" for the integrated master's)")])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.46', '3.47', '3.48', '4.9']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '1.35', '1.36', '1.37',
                                                                 '1.38', '1.39', '1.40', '1.41', '1.42', '1.43', '2.24', '3.30', '3.48']),
      dict(id='theme:esd', role='carries', carriedIn=['1.44', '1.45', '1.46', '1.47', '1.48', '4.9']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.49', '1.50', '1.51', '1.52', '1.53', '1.54', '1.55', '1.56', '1.57', '1.58', '1.59', '1.60', '2.30', '3.26'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-mathematics-statistics-and-operational-research-2019-benchmarks (not yet ingested)',
           note='the fifth edition (2023); the fourth was published in 2019 (D1, section 6)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D',
           note='the degree classification descriptions for FHEQ level 6 and FQHEIS level 10, cited as QAA 2019 (4.4; section 5)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note="levels 6 and 7 (2.5, 2.12, 2.14, 4.4); the Frameworks for master's outcomes (4.4)"),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 10 and 11 (2.5, 2.12, 2.14, 4.4)'),
      dict(rel='themeReference', target='std:doc:qaa-advancehe-esd-2021-guidance', note='Education for Sustainable Development Guidance (1.46)'),
      dict(rel='themeReference', target='std:doc:qaa-enterprise-2018-guidance', note="QAA's enterprise and entrepreneurship guidance (1.49; section 5)"),
      dict(rel='refersTo', target='QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested)', note='2.11'),
      dict(rel='refersTo', target='QAA Contracting to Cheat in Higher Education, third edition (not yet ingested)', note='3.51'),
      dict(rel='refersTo', target='IMA, RSS and IFoA accreditation requirements (not yet ingested)', note='1.20, 2.34')]

SB1 = ["MSOR is treated as one body of knowledge and skill, wider than its three fields and often combined with others, as in data science (D1, 1.1, 1.2)",
       "Mathematics draws conclusions by strict deduction from assumptions, and owes its reach to generalisation and abstraction (D1, 1.3, 1.4)",
       "Statistics handles data under random variation on a base of probability, and explaining results to non-experts is central to it (D1, 1.5, 1.6)",
       "Operational research spans heavily mathematical optimisation and rigorous non-mathematical problem structuring, in support of decisions (D1, 1.7, 1.8)",
       "Courses run along a spectrum from theory-based to practice-based, each emphasis equally valued and read from the curriculum, not the title (D1, 1.10, 2.1, 2.2)",
       "The subject is cumulative, with strict prerequisites; accuracy with symbols and numbers matters; uneven attainment across modules is normal (D1, 1.15 to 1.17, 3.52)",
       "It is widely taught to non-specialists as service teaching (D1, 1.9)",
       "Dense notation, board-based argument and diagrams shape both teaching and accessibility (D1, 1.34, 3.29, 3.37)"]

SB2 = [dict(theme='theme:edi', inThisSubject="the subject names its gender imbalance, awarding gaps and a curriculum centred on white Western men, and debates decolonising its history (eugenics, enslaved labour, fascist links) without cutting core content; inclusion also reaches data collection and analysis (D1, 1.21 to 1.27)",
            statements=['1.23', '1.25', '3.47', '3.48', '4.9.b6']),
       dict(theme='theme:accessibility', inThisSubject="mathematical notation, board work, non-linear argument and diagrams defeat mainstream assistive technology, so the subject asks for specialist tools, trained support workers and staff support to embed accessibility (D1, 1.28 to 1.43)",
            statements=['1.28', '1.29', '1.30', '1.33', '1.36.b1', '1.37', '1.38', '1.42', '3.48']),
       dict(theme='theme:esd', inThisSubject="headed Sustainability in the text: models for climate, epidemics, transport and health serve the UN goals; projects, modules and case studies carry it, along with the ethics of computing's footprint (D1, 1.44 to 1.48)",
            statements=['4.9.b6']),
       dict(theme='theme:enterprise', inThisSubject="problem-solving is the core enterprise competency; projects, group work, data-heavy modules, client projects and placements build it, and graduates must be able to say how (D1, 1.49 to 1.60)",
            statements=['1.50', '1.55', '1.60'])]

SB3 = dict(
    areas=[dict(component='3.8', gloss='common ground for all courses: calculus, linear algebra, probability and statistics'),
           dict(component='3.9', gloss='a range of areas, depth set by the course\'s place on the theory to practice spectrum'),
           dict(component='3.10', gloss='mathematics: algebra, analysis, geometry, number theory, differential equations, mechanics, mathematical physics'),
           dict(component='3.11', gloss='statistics: exploratory analysis, inference, likelihood, linear models, stochastic processes, time series, analytics'),
           dict(component='3.12', gloss='operational research: healthcare, transport, logistics, planning, manufacturing, retail'),
           dict(component='3.13', gloss='assumptions and their validity'),
           dict(component='3.14', gloss='generalisation, abstraction and proof'),
           dict(component='3.16', gloss='numerical approximation'),
           dict(component='3.17', gloss='programming and specialist software'),
           dict(component='3.18', gloss='mathematical and statistical modelling'),
           dict(component='3.19', gloss='modelling techniques, validation and interpretation'),
           dict(component='3.20', gloss='related content: history of mathematics, mathematics education, careers'),
           dict(component='3.21', gloss='depth in particular areas')],
    practices=[dict(component='3.28', kind='teaching', gloss='a deliberate mix of pedagogies, coherent across the course'),
               dict(component='3.29', kind='teaching', gloss='lectures, tutorials, computer laboratories, active and flipped learning'),
               dict(component='3.30', kind='learning', gloss='advance materials, practice exercises and open problems'),
               dict(component='3.31', kind='teaching', gloss='revisiting topics in a cumulative subject'),
               dict(component='3.32', kind='learning', gloss='peer learning, formal and informal'),
               dict(component='3.33', kind='learning', gloss='additional support and mathematics support services'),
               dict(component='3.36', kind='learning', gloss='study skills and independent practice'),
               dict(component='3.37', kind='teaching', gloss='teaching spaces and board space'),
               dict(component='3.38', kind='teaching', gloss='technology, including automated feedback'),
               dict(component='3.39', kind='learning', gloss='computing, programming and specialist software'),
               dict(component='1.46', kind='teaching', gloss='sustainability through projects, modules, case studies and problems'),
               dict(component='1.56', kind='learning', gloss='problem-based learning'),
               dict(component='1.57', kind='assessment', gloss='client projects and authentic outputs such as posters and client reports'),
               dict(component='3.44', kind='assessment', gloss='what assessment establishes against section 4'),
               dict(component='3.46', kind='assessment', gloss='formative feedback'),
               dict(component='3.48', kind='assessment', gloss='varied methods; automated online marking; accessible and inclusive design'),
               dict(component='3.50', kind='assessment', gloss='professional judgement in marking'),
               dict(component='3.51', kind='assessment', gloss='controlled conditions and integrity'),
               dict(component='3.52', kind='assessment', gloss='the full mark range and whole-course judgement')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.5', award=HON, items=7),
           dict(rung='threshold', leadIn='4.6', award=IM, items=9)],
    rungBases=("4.8: performance above threshold may show in depth of understanding, breadth of knowledge, the support needed for an extended task, "
               "the complexity of problems solved or modelled, creative solutions to unfamiliar problems, constructing and presenting argument or proof, "
               "and facility with calculation; 4.4 points to Annex D for the classification bands. No typical or excellent rung is stated."),
    outcomeLists=[dict(leadIn='3.26', gloss='general skills expected of all graduates', items=11, award=['honours', "integrated master's"]),
                  dict(leadIn='4.9', gloss='professional standards', items=8, award=['honours', "integrated master's"])],
    outcomes=[])

SB4A_FULL = []

SB5 = [dict(body='Institute of Mathematics and its Applications (IMA)',
            says='accredits courses meeting its requirements for graduates to reach Chartered Mathematician status; runs individual professional recognition (D1, 1.20)',
            requirements='not yet ingested (Part E)'),
       dict(body='Royal Statistical Society (RSS)',
            says='accredits courses meeting its requirements for Graduate Statistician status and individual modules in statistical literacy (the RSS Quality Mark); runs individual recognition (D1, 1.20)',
            requirements='not yet ingested (Part E)'),
       dict(body='Operational Research Society (ORS)', says='runs individual professional recognition schemes (D1, 1.20)',
            requirements='not yet ingested (Part E)'),
       dict(body='Institute and Faculty of Actuaries (IFoA)', says='accredits courses and modules, giving students exemption from some of its examinations (D1, 1.20)',
            requirements='not yet ingested (Part E)'),
       dict(body='London Mathematical Society (LMS)',
            says='runs a Good Practice Scheme for women\'s careers in the subject, to which many providers work, and publishes Mathematics and Accessibility resources (D1, 1.24, 1.43)',
            requirements='not-applicable-by-design: a learned society, not an accrediting body here (Part E)'),
       dict(body='professional bodies that accredit MSOR courses (unnamed)', says='accreditation carries each body\'s own requirements; quality processes include those tied to accreditation (D1, 2.34, 3.43)',
            requirements='not yet ingested (Part E)')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.46', '3.47', '3.48', '4.9'],
                 statements=['1.23', '1.25', '3.47', '3.48', '4.9.b6']),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)',
                 carriedIn=['1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '1.35', '1.36', '1.37', '1.38', '1.39', '1.40', '1.41', '1.42', '1.43', '2.24', '3.30', '3.48'],
                 statements=['1.28', '1.29', '1.30', '1.33', '1.36.b1', '1.37', '1.38', '1.42', '3.48']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.44', '1.45', '1.46', '1.47', '1.48', '4.9'],
                 statements=['4.9.b6']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)',
                 carriedIn=['1.49', '1.50', '1.51', '1.52', '1.53', '1.54', '1.55', '1.56', '1.57', '1.58', '1.59', '1.60', '2.30', '3.26'],
                 statements=['1.50', '1.55', '1.60'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.5', '2.12', '2.14', '4.4']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.5', '2.12', '2.14', '4.4'])],
    bodies=[dict(body='Institute of Mathematics and its Applications', citedIn=['1.20']),
            dict(body='Royal Statistical Society', citedIn=['1.20']),
            dict(body='Operational Research Society', citedIn=['1.20']),
            dict(body='Institute and Faculty of Actuaries', citedIn=['1.20']),
            dict(body='London Mathematical Society', citedIn=['1.24', '1.43']),
            dict(body='professional bodies (accrediting, unnamed)', citedIn=['2.34', '3.43'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees',
             citedIn=['4.4'], role='descriptions of the four honours classifications (1st, 2.1, 2.2, 3rd), used for performance above threshold'),
        dict(document='std:doc:qaa-fheq-2024-framework; std:doc:qaa-fqheis-2024-framework', named='Frameworks for Higher Education Qualifications',
             citedIn=['4.4'], role="the outcomes for master's level"),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development Guidance produced by QAA and Advance HE',
             citedIn=['1.46'], role='pedagogic approaches for sustainability'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named="QAA's guidance (enterprise and entrepreneurship education)",
             citedIn=['1.49'], role='the frame for enterprise education'),
        dict(document='QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested: Part E)', named='Characteristics Statement for Higher Education in Apprenticeships',
             citedIn=['2.11'], role='the characteristics of degree apprenticeships'),
        dict(document='QAA Contracting to Cheat in Higher Education (not yet ingested: Part E)', named="QAA's guidance Contracting to Cheat in Higher Education",
             citedIn=['3.51'], role='academic integrity under controlled conditions'),
        dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'],
             role='course design, teaching, external expertise, monitoring'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='UN Sustainable Development Goals (external)', named="the UN's Sustainable Development Goals", citedIn=['1.44', '1.45'], role='the frame of the sustainability theme'),
        dict(document='reports on the value of the mathematical sciences (external)', named='Measuring the Economic Benefits of Mathematical Science Research in the UK (2012); The Era of Mathematics (2018)',
             citedIn=['1.19'], role="evidence of the subject's economic contribution"),
        dict(document='Council for the Mathematical Sciences report (external)', named='The Mathematical Sciences People Pipeline (2015)', citedIn=['1.26'], role='demographic imbalance data'),
        dict(document='LMS resources (external)', named='Good Practice Scheme; Mathematics and Accessibility', citedIn=['1.24', '1.43'], role='EDI and accessibility practice'),
        dict(document='Athena SWAN (external award scheme)', named='Athena SWAN awards', citedIn=['1.24'], role='evidence of commitment to EDI'),
        dict(document='Maths Careers website (external)', named='Maths Careers website', citedIn=['1.18'], role='careers information')])

B1 = [dict(slug='msor', definition='mathematics, statistics and operational research taken together as one field, with the many combinations of its parts (D1, 1.1, 1.2)',
           beneficiaryDefinition='the three subjects, and their mixtures, treated as one subject area', scopeNote='used throughout; wider than the three fields side by side', category='unknown', practices=['education']),
      dict(slug='theory-based-course', definition='a course concerned chiefly with how theory yields general propositions and then methods to apply (D1, 1.10, 2.1)',
           scopeNote='one end of a spectrum; most courses mix both styles (2.2)', category='unknown', practices=['education']),
      dict(slug='practice-based-course', definition='a course concerned chiefly with understanding and applying results, methods and techniques in varied settings (D1, 1.10, 2.1)',
           scopeNote='the other end of the spectrum', category='unknown', practices=['education']),
      dict(slug='enterprise', definition='generating ideas and putting them to work in practical situations during a project or undertaking (D1, 1.51)',
           scopeNote='generic, involving creativity and problem-solving', category='unknown', practices=['education']),
      dict(slug='entrepreneurship', definition='using enterprise behaviours, attributes and competencies to create cultural, social or economic value (D1, 1.52)',
           scopeNote='may, but need not, lead to a new venture', category='unknown', practices=['education']),
      dict(slug='enterprise-and-entrepreneurship-education', definition='developing students so they can better generate and evaluate ideas and widen the behaviours needed to carry them out (D1, 1.53)',
           scopeNote='one of the cross-cutting themes', category='unknown', practices=['education']),
      dict(slug='threshold-level', definition='the minimum standard of competence the statement sets for an award, met overall rather than item by item (D1, 4.2, 4.4, 4.5, 4.6)',
           beneficiaryDefinition='the minimum you need to show to gain the award', scopeNote='set for honours and for the integrated master\'s', category='unknown', practices=['education']),
      dict(slug='conversion-masters', definition='a taught master\'s course letting graduates of other subjects retrain in the field (D1, 1.13, 2.4)',
           scopeNote='often in data science and statistics', category='unknown', practices=['education']),
      dict(slug='well-curated-course', definition='a course with clearly communicated learning opportunities, well-spaced assessment and extra support when concepts first appear (D1, 1.33)',
           scopeNote='part of the accessibility theme', category='unknown', practices=['education'])]

B2A = [dict(concept='msor', form='MSOR', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
       dict(concept='msor', form='Mathematics, Statistics and Operational Research', lang='en', partOfSpeech='noun-phrase', termStatus='admitted', register='formal'),
       dict(concept='theory-based-course', form='theory-based courses', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='practice-based-course', form='practice-based courses', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='enterprise', form='Enterprise', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='entrepreneurship', form='Entrepreneurship', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='enterprise-and-entrepreneurship-education', form='Enterprise and entrepreneurship education', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='threshold-level', form='threshold level', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='conversion-masters', form='conversion master\'s', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='well-curated-course', form='well curated', lang='en', partOfSpeech='adjective-phrase', termStatus='preferred', register='formal')]

B4 = [dict(rel='contrasts-with', **{'from': 'theory-based-course'}, to='practice-based-course', note='ends of one spectrum; most courses mix both (2.2)'),
      dict(rel='related', **{'from': 'enterprise'}, to='entrepreneurship', note='entrepreneurship applies enterprise to value creation (1.52)'),
      dict(rel='broader', **{'from': 'enterprise-and-entrepreneurship-education'}, to='enterprise', note='1.53')]
B5 = []

D3 = [dict(citation='QAA (2019) Characteristics Statement: Higher Education in Apprenticeships', settles=['SB6', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='QAA (2022) Contracting to Cheat in Higher Education: How to address Essay Mills and Contract Cheating, third edition', settles=['SB6', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='QAA (2019) Subject Benchmark Statement: Mathematics, Statistics and Operational Research, fourth edition', settles=['S7'], asked='2026-10-03', state='wanted')]

E = [
    "SB4, rungs: the statement sets threshold standards only, two lists for two awards: 4.5 for the bachelor's degree with honours (7 items) and 4.6 for the integrated master's (9 items). No typical or excellent rung is stated; 4.8 lists the bases on which performance above threshold shows (SB4 `rungBases`), and 4.4 hands classification to Annex D. Differs from Psychology, which states three rungs.",
    "S4, skeleton correction: std_prep read 4.8's seven bullets as threshold items because the lead-in names 'threshold'; they are the bases for judging performance above threshold ('may be demonstrated through'), not statements. Recorded in `rungBases` and as an S3 component.",
    "S4, skeleton correction: std_prep gave 4.6's items rung threshold with no award; they are the integrated master's threshold, recorded with award integrated master's and level fheq:7 under their own skeleton ids (4.6.b1 to 4.6.b9), not with the `.masters` suffix, since 4.6 is a separate list with its own spans.",
    "S4, 4.5 and 4.6 force: the lead-ins read 'should be able to demonstrate'; force is recorded as should, the issuer's word, not threshold, though 4.2 and 4.4 define these lists as the minimum for the award. For Abbott: should a threshold lead-in in 'should' take force threshold?",
    "S4, 4.2: the standards are to be met 'in an overall sense, not necessarily in respect of each and every criterion listed'; every 4.5 and 4.6 author-agent-written field says so. A new pattern against Psychology.",
    "SB4, cross-award parallels (inferred, not `gradeOf`, since both lists are threshold): 4.6.b1 to 4.6.b7 follow 4.5.b1 to 4.5.b7 in order, raising 'reasonable' to 'good' and 'well-defined' to 'loosely defined'; 4.5.b4 (reasoning) and 4.6.b4 (developing and evaluating arguments) are the loosest match; 4.6.b8 (independent work) and 4.6.b9 (advanced project) have no honours counterpart.",
    "S4, 4.9 professional standards: a list headed 'Professional standards' beside the academic standards, with lead-in 'graduates should be expected to'; recorded as an outcome list (rung none, force should), not a rung, and read at fheq:6 for both undergraduate awards, with 4.10 adding the master's deepening. Whether it is a threshold is not stated.",
    "S4, 3.26 general skills: the lead-in 'are to be expected of all MSOR graduates' is outside the five obliging words; its eleven items are recorded with force describes (forceFrom 3.26). For Abbott: read as should?",
    "S4, obliging words outside the five, each recorded with force describes: 1.30 'it is imperative that' (read as close to must); 1.38 'need to'; 1.60 'need to be able to'; 2.12 'it is expected that'; 3.18 'are expected to'; 3.26 'are to be expected of'. 1.37 'is required' is recorded as must, by the convention. 1.50 'personal responsibility' (students) and 3.42 'responsibility' (staff) sit in paragraphs already taken as should statements.",
    "S4, not taken as statements (impersonal obligation or a consequence of practice; for Abbott): 1.21 'it is important that'; 1.26 'There is a need for'; 1.41 'All students will benefit from' explicit instruction; 2.32 'Providers will use external reviewers'; 3.38 technology 'is widespread and expected'; 3.41 staff 'need to routinely update materials'; 1.36.b2 staff 'will require' specialist support and 1.36.b3 'are likely to need'.",
    "S4, plain-present provider norms and outcomes (template open point 5; not statements): section 3's 'Courses develop graduates who have ...' paragraphs (3.2 first sentences, 3.7, 3.10, 3.12 to 3.14, 3.16, 3.19, 3.21), 3.22 and 3.24's branch skills ('have skills', 'may have skills'), 3.25 and 3.27. They carry much of the subject's knowledge content; only the paragraphs with 'will', 'are able to' or 'expected' (3.5, 3.9, 3.11, 3.17, 3.18) are statements. For Abbott at P3: this subject leans on plain present more than Psychology does.",
    "S4, list items not taken: 1.13 and 1.20 (descriptive), 1.27 ('good practice here could include', 23 items), 1.34, 1.46 ('might include'), 1.47 (examples), 2.22 and 2.23 ('it is beneficial'), 3.39.b1 to b5 and 3.40 (examples of software and materials), 3.44 and 3.45 (what assessment establishes or could establish).",
    "S4, 1.1 'should be understood' defines the scope term MSOR; not an obligation on anyone, so not a statement.",
    "S4, 4.4 mixes a provider 'should' (refer to Annex D) with a student 'will' (master's graduates build on levels 6 and 10); recorded as one provider statement, the master's sentence carried in its paraphrase.",
    "S4, 4.7: taught master's 'will develop some or all of the standards listed above'; recorded as an expectation for both learner and course, award master's, with no list of its own.",
    "S4, verbs: 3.26.b3, 3.26.b6, 4.5.b7, 4.6.b1 and 4.6.b7 are noun phrases with no verb of their own; their verbs fields are empty.",
    "S4, domain: provider duties and 2.12, 4.4 and 4.7 take domain none, as Psychology's requirements do; SB-4 asks for one of the four values on every benchmark standard. For P3.",
    "S4, themes: 2.24 (reasonable adjustments), 2.30 and 3.26 (employability) carry a theme in SB6 without naming its heading; their S4 records are not theme-tagged, since tags are what the paragraph names.",
    "S6 and SB6, std_prep correction: the skeleton's theme hits on 1.20 (EDI), 1.43 (sustainability) and 1.48 (enterprise) come from the next heading caught at the end of each span; 1.43 carries accessibility only.",
    "S5 and SB6: 2.3 names 'Level 4' (foundation years preparing for 'Level 4 study') with no framework named; not recorded as a level (inferred fheq:4).",
    "S5: integrated master's crosswalk fheq:7 to fqheis:11 stated in 2.5, 2.12 and 2.14; the FHEQ's Table 1 agrees (std:doc:qaa-fheq-2024-framework, S5).",
    "SB6, sharedDocuments: the statement cites Annex D as QAA 2019; it is now held in the Frameworks 2024 (std:doc:qaa-fheq-2024-framework, Annex D).",
    "SB5: the IMA, RSS, ORS and IFoA requirements are not yet ingested; the LMS is a learned society, recorded with requirements not-applicable-by-design. The OfS appears only in the front matter (England's regulatory framework) and is not listed as a body.",
    "S2 and front matter, codes: no HECoS term for data science, analytics or management science; mathematics for engineering mapped to 101028 engineering and industrial mathematics (inferred); applied mathematics 100400 inferred from 'applications of mathematics' (3.8, 3.24). Both inferred codes held back from lookups until P3.",
    "S2: 1.8 says courses titled 'management science', often with little mathematics, might not fall wholly within the statement; 1.9 says the statement is directly relevant to service courses such as mathematics for engineering; 4.3 makes it a reference point for data science and joint courses.",
    "Pattern: the master's level appears as its own award list (4.6) and a separate taught master's paragraph (4.7, 4.10), not as a column. Section 4 splits into Academic standards (4.5 to 4.8) and Professional standards (4.9, 4.10), a heading not met in Psychology.",
    "Pattern: S4 records for 4.9 carry `award` honours and integrated master's but a single `level` fheq:6; 4.10 is recorded at fheq:7.",
    "S1, licence: copyright notice only; QAA's terms for holding and chunking are to check (template open point 3).",
    "S9: not researched in P1.",
]
