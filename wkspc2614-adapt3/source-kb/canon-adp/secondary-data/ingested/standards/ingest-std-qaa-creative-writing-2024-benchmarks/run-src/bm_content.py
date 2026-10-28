# bm_content.py: judgement file for run 0097, QAA Subject Benchmark Statement Creative Writing (April 2024), std.
# Built by tools/bm_build.py creative-writing-2024 (BM-BRIEF 0.2.2; benchmark template 0.6.0-draft; run layer 0.7.0-draft).
# Statements: the rung lists 4.3 (threshold), 4.4 (typical) and 4.5 (excellent), the generic skills 4.6 (should), the
# master's list 4.7 (plain present), the outcome list 2.2 (will) and six obliging or outcome paragraphs (1.20, 1.31, 2.3,
# 2.7, 3.22, 4.2). Records whose skeleton span runs on into a heading or a page number are cut by `find`.

HON = "bachelor's with honours"
MAS = "master's"
SID = 'qaa/creative-writing-2024'
CITE = 'QAA (2024), Creative Writing Subject Benchmark Statement'
KN, UN, SK, GS = 'knowledge', 'understanding', 'subject-skill', 'generic-skill'

META = dict(
  run='0097', p1='2026-10-03 16:53',
  title='Subject Benchmark Statement Creative Writing',
  heading='Subject Benchmark Statement: Creative Writing (QAA, April 2024)',
  edition='April 2024 (third edition)', published='2024-04',
  status='current', supersedes='Subject Benchmark Statement for Creative Writing, second edition (2019), as section 6 names it',
  subjects=[
    dict(scheme='hecos', code='100046', label='creative writing', basis='stated'),
    dict(scheme='cah', code='CAH19-01-05', label='creative writing', basis='stated'),
    dict(scheme='cah', code='CAH19-01', label='English studies', basis='inferred')],
  awards=[HON, MAS], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
  nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
  series='QAA Subject Benchmark Statements, 2024 revision with the cross-cutting themes (third edition of this statement)',
  partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
  agentDefinition=("QAA's UK reference point for what an honours graduate in Creative Writing knows, understands and can do, with a further "
    "list for master's study. Its standards are three rung lists (threshold, typical, excellent), a list of generic skills and a "
    "master's list, beside an outcome list in section 2. Reach for it when designing, reviewing or describing a Creative Writing course, "
    "its modules or its outcomes. It is not a curriculum and not a regulatory requirement in England."),
  summary=("Published by QAA in April 2024 as the third edition, the statement sets out the purposes and characteristics of a Creative "
    "Writing degree, its distinctive features (design, progression, flexibility, partnerships, review) and its content, teaching and "
    "assessment. Its benchmark standards for the bachelor's degree with honours are 13 threshold items, 19 typical items and an "
    "excellent rung of a lead paragraph and 9 items, of which graduates show some. Beside them stand 18 generic skills that graduates "
    "should have and 16 outcomes for master's level. It carries the four cross-cutting themes (equality, diversity and inclusion; accessibility; "
    "sustainability; enterprise and entrepreneurship education) and treats artificial intelligence in content and assessment. It "
    "cites FHEQ Levels 6 and 7 with FQHEIS Levels 10 and 11, and Annex D for the honours classifications; it names UNESCO's ESD "
    "competencies and the Equality Act 2010, but no professional body for the subject."))

S2 = dict(
  governs="what can be expected of a Creative Writing graduate at the end of an honours degree, what master's study adds and what courses in the subject provide",
  awards=[HON, MAS], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
  statedScope='"This document is a QAA Subject Benchmark Statement for Creative Writing that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies." (D1, front matter)',
  statedSubjects=[
    dict(name='Creative Writing', locator='(D1, front matter; 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100046', label='creative writing'), dict(scheme='cah', code='CAH19-01-05', label='creative writing')]),
    dict(name='combined, joint and major-minor degrees with Creative Writing', locator='(D1, 2.7; 3.2; 3.3)', kind='programme title', codes=[]),
    dict(name="integrated master's and master's level Creative Writing degrees", locator="(D1, 2.10; 3.33; 4.7)", kind='programme title', codes=[dict(scheme='hecos', code='100046', label='creative writing')])])

SECTIONS = {'1': 'Context and purposes of a Creative Writing degree', '2': 'Distinctive features of the Creative Writing degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.7', 'Context and purposes of a Creative Writing degree'),
       ('1.8', '1.20', 'Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education'),
       ('1.21', '1.26', 'Equality, diversity and inclusion'), ('1.27', '1.32', 'Accessibility'), ('1.33', '1.38', 'Sustainability'),
       ('1.39', '1.41', 'Enterprise and entrepreneurship education'),
       ('2.1', '2.2', 'Design'), ('2.3', '2.10', 'Progression'), ('2.11', '2.11', 'Flexibility'), ('2.12', '2.13', 'Partnerships'),
       ('2.14', '2.16', 'Monitoring and review'),
       ('3.1', '3.9', 'Content'), ('3.10', '3.21', 'Teaching and learning'), ('3.22', '3.22', 'Assessment'),
       ('3.23', '3.24', 'Formative assessment'), ('3.25', '3.27', 'Summative assessment'), ('3.28', '3.32', 'Assessment criteria'),
       ('3.33', '3.33', 'Postgraduate programmes'),
       ('4.1', '4.2', 'Introduction'), ('4.3', '4.3', 'Threshold level: Subject knowledge, understanding and skills'),
       ('4.4', '4.4', 'Typical level: Subject knowledge, understanding and skills'),
       ('4.5', '4.5', 'Excellent level: Subject knowledge, understanding and skills'), ('4.6', '4.6', 'Generic skills'),
       ('4.7', '4.7', "Master's level")]

G = {
 '1.1': 'imagination and language; the creative industries and careers', '1.2': 'interdisciplinary; own practice; workshops; independence',
 '1.3': 'subject skills and transferable skills; traditions drawn on', '1.4': 'communication, literacy and oracy; peer feedback',
 '1.5': 'research culture; creative writing as research', '1.6': 'research-informed teaching; who teaches the subject',
 '1.7': "skills students gain; then the subject's purposes in higher education (a list of aims)", '1.8': 'an artistic and critical discipline across media',
 '1.9': 'ideas and originality as the focus', '1.10': 'what originality means in the subject (with a list)',
 '1.11': 'research skills and reading', '1.12': 'what reading covers, from games to criticism',
 '1.13': 'creative-critical projects; diverse texts; theory', '1.14': 'literary and media analysis; editing skills',
 '1.15': 'professional, entrepreneurial and social skills', '1.16': 'graduate destinations; creative entrepreneurs',
 '1.17': 'kinds of degree', '1.18': 'partnered with other disciplines', '1.19': 'individual or collaborative assessment',
 '1.20': 'peer feedback and encouraging students to use it', '1.21': 'inclusive learning communities; the Equality Act 2010',
 '1.22': 'inclusive curricula and reading lists', '1.23': 'belonging and critical dialogue',
 '1.24': 'participation plans in the four nations; student support', '1.25': 'external agencies for equality and diversity',
 '1.26': 'inclusive responses through content and pedagogy', '1.27': 'routes of entry; adult returners',
 '1.28': 'open to all; disclosure and adjustments', '1.29': 'entry by portfolio or presentation',
 '1.30': 'accessible materials, spaces and placements (a list of aims)', '1.31': 'workshops and accessibility; preparation required',
 '1.32': 'learning support plans; adaptable approach', '1.33': 'education for sustainable development; UNESCO',
 '1.34': 'human and non-human; UNESCO key competencies', '1.35': 'nature and environmental writing',
 '1.36': 'research and ecological responsibility', '1.37': 'environmental publishing and the more than human',
 '1.38': 'global interdependence; imagining sustainable futures', '1.39': 'enterprise education and careers',
 '1.40': 'a self-determined professional life', '1.41': 'skills the subject builds for enterprise (a list)',
 '2.1': 'what characterises course design (a list)', '2.2': 'what students will do through study (an outcome list)',
 '2.3': 'progression across levels towards the threshold', '2.4': 'year one: workshop practice and reflection',
 '2.5': 'year two: wider research and practice', '2.6': 'final year: major project and employability',
 '2.7': 'joint and combined degrees', '2.8': 'exit awards; course length in the four nations',
 '2.9': 'postgraduate study after a second-class degree', '2.10': "integrated master's degrees",
 '2.11': 'modes of study and micro-credentials', '2.12': 'students, industries and presses as partners',
 '2.13': 'work placements (a list of opportunities)', '2.14': 'monitoring and periodic review',
 '2.15': 'externality in quality assurance', '2.16': 'external examiners and threshold standards',
 '3.1': 'making texts at the centre; varied design', '3.2': 'single honours and combinations',
 '3.3': 'a minor beside subjects outside the arts', '3.4': 'an outline of typical structure',
 '3.5': 'Level 4 content (a list)', '3.6': 'Level 5 content (a list)', '3.7': 'Level 6 content (a list)',
 '3.8': 'community of practice and belonging', '3.9': 'changing content: digital forms and AI',
 '3.10': 'teaching strategies; risk and failure', '3.11': 'staff research and visiting practitioners',
 '3.12': 'preparing for class', '3.13': 'learning environments, on and off campus',
 '3.14': 'scheduled activities; online learning', '3.15': 'skills in action; small-group teaching',
 '3.16': 'collaborative and independent study', '3.17': 'presenting work; steps for accessible workshops (a list)',
 '3.18': 'writing about personal and difficult themes (a list of supports)', '3.19': 'tailored support for chosen specialisms',
 '3.20': 'generative AI in practice and analysis', '3.21': 'portfolio, dissertation or capstone project',
 '3.22': 'formative and summative assessment; accessible assessment', '3.23': 'formative assessment in workshops',
 '3.24': 'written feedback; self-critique', '3.25': 'summative assessment and stated outcomes',
 '3.26': 'forms of submission (a list)', '3.27': 'student-devised assignments', '3.28': 'clear, visible assessment criteria',
 '3.29': 'what criteria may evaluate (a list)', '3.30': 'specific criteria', '3.31': 'assessing workshop contribution',
 '3.32': 'AI and the assessment of originality', '3.33': "master's degrees: aims and professional readiness",
 '4.1': 'minimum, typical and excellent standards for honours', '4.2': 'most exceed the threshold; Annex D',
 '4.3': 'threshold rung (a list)', '4.4': 'typical rung (a list)', '4.5': 'excellent rung: a lead paragraph and a list',
 '4.6': 'generic skills (a list)', '4.7': "master's level outcomes (a list)"}

CTYPE = {k: 'area' for k in ['3.1', '3.5', '3.6', '3.7', '3.8', '3.9', '1.12']}
CTYPE.update({k: 'practice' for k in ['3.10', '3.12', '3.13', '3.14', '3.16', '3.17', '3.18', '3.21', '3.23', '3.24', '3.26', '3.27', '3.28', '3.29', '3.31']})

EXCLUDED = [
  dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2, S7 and SB6'),
  dict(number='1, 2, 3, 4', heading='section heading lines', kind='other: headings, recorded in SECTIONS'),
  dict(number='5', heading='List of references and further resources', kind='other: ten references, read for SB6'),
  dict(number='6', heading='Membership of the Advisory Group (2023, 2019, 2016)', kind='other: authorship history, read for S7 supersedes')]

# ------------------------------------------------------------------ statements
P = {}
def s(i, **k):
    P[i] = k

FW6 = 'the FHEQ level 6 descriptor %s (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)'
FW7 = 'the FHEQ level 7 descriptor %s (shared with FQHEIS level 11; spine:7)'

# ---- obliging or outcome paragraphs (sections 1 to 4)
s('1.20', type='expectation', rung='none', force='should', level='none', appliesTo='Creative Writing courses', addressee='provider',
  verbs=['encouraged', 'refine'], about='encouraging students to use peer feedback', domain='none', award=HON,
  find="Teaching and learning activities employed by Creative Writing courses will often involve significant opportunities for peer-to-peer feedback. Creative Writing students may be exposed to a range of perspectives when presenting their work. Such collaborative activities can be considered as a key stage in the development of student work. Students should be encouraged to take advantage of these experiences to refine their skills in giving and receiving feedback, in a manner that is both productive and empathetic.",
  para="Peer feedback is a frequent and formative part of teaching in the subject; courses should encourage students to use these occasions to sharpen how they give and take feedback, usefully and with empathy.",
  prac="Build regular peer feedback into teaching and actively encourage students to use it to get better at offering and receiving critique that is both useful and kind.",
  ben=('n/a', "a duty on the course to encourage; the student-facing skill is in 4.4.b16 and 4.6.b16"),
  aaw=f"Treat this as a should-level expectation on the course, not a student outcome: courses should encourage students to use peer feedback to improve how they give and take it. It holds for the honours degree at every stage. Cite it as {CITE}, para 1.20. Do not claim it is a requirement or a graduate standard; set it beside 4.4.b16 and 4.6.b16, which state the feedback skills graduates show, and beside the level 6 descriptor qaa/fheq-2024/4.15.b8.",
  aad="Raise it with a programme team planning workshops or reviewing how feedback is taught. For staff, put it as a design expectation and ask: 'Where in each year do students practise giving feedback, and how do you know they are improving at it?' With a student, do not present it as a rule they must meet; talk instead about the feedback skills in 4.4.b16.")

s('1.31', type='requirement', rung='none', force='must', level='none', appliesTo='Creative Writing courses that use workshops', addressee='provider',
  verbs=['required', 'ensure'], about='extra preparation to make workshops accessible', domain='none', award=HON,
  find="Collaborative and/or peer-led workshops are a common feature of many Creative Writing courses. During these workshops students read a section of their writing in progress to the group. The tutor then invites other workshop participants to provide feedback on the work in progress. There are some important critiques of pedagogical approaches to workshops which are worth considering when designing inclusive learning experiences. While workshops can provide a valuable learning experience, additional preparation is required to ensure that the experience is accessible to all students, including those with physical disabilities, learning disabilities, and neurodivergent and chronic mental health conditions.",
  para="Workshops, where students read work in progress and peers respond, are common and open to critique; to make them accessible to every student, including disabled and neurodivergent students and those with chronic mental health conditions, further preparation is required.",
  prac="Workshops are valuable but not accessible by default: prepare them in advance so that disabled students, neurodivergent students and those with long-term mental health conditions can take full part, and weigh the critiques of the workshop model when designing them.",
  ben=('n/a', 'a duty on the course and its tutors; the student meets its effect, not a standard to reach'),
  aaw=f"Treat this as a requirement on the course under the accessibility theme (the issuer's word is 'required', recorded as must): workshops need further preparation so that every student can take part. It applies to provision for the honours degree, not to a level of attainment. Cite it as {CITE}, para 1.31. Do not present it as a legal duty in its own right or as a student outcome; set it beside 1.30, 3.17 and 3.22 on accessible materials, workshops and assessment.",
  aad="Raise it with tutors or a programme team who run workshops, especially when planning a new module or responding to a student's support plan. Frame it for staff and ask: 'What does a student who cannot read aloud, or who finds the room overwhelming, do in your workshop?' Do not give it to a student as something they must achieve; if a student raises access to workshops, point to the adjustments it implies.")

s('2.3', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on the honours degree', addressee='learner',
  verbs=['progress', 'builds'], about='progression across levels towards the threshold', domain='none', award=HON,
  find="Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10) a Creative Writing student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of knowledge, expertise and experience that builds towards the final achievement of meeting the threshold-level subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components.",
  para="Across the honours degree (FHEQ level 6, FQHEIS level 10) a student will move up through the levels under each institution's rules, each level adding knowledge, expertise and experience towards meeting the threshold subject and generic skills, usually by completing and gaining credit for all learning and assessment.",
  prac="Plan each level so that it builds knowledge, expertise and experience towards the threshold subject-specific and generic skills in 4.3 and 4.6; students will normally progress by completing, and earning credit for, all learning and assessment, practical work included.",
  ben="As you move up through the levels of your degree, you will build knowledge, skill and experience towards the minimum subject and general skills for honours, usually by passing and gaining credit for all your learning and assessment, practical work included.",
  aaw=f"Describe this as the statement's account of progression (force will) through the honours degree, which it places at FHEQ level 6 and FQHEIS level 10. Cite it as {CITE}, para 2.3. Do not claim it sets progression rules, which stay with each institution, or that it fixes what each lower level contains; set it beside 4.3 and 4.6 (the threshold it builds towards), 3.5 to 3.7 (content by level) and spine:4 to spine:6 in std:ref:uk-framework.",
  aad="Raise it when a student or programme team asks how the years of the degree fit together or what each level is for. To a student, say plainly that each year builds towards the minimum skills for the degree; to staff, frame it as a design check on the curriculum map. Ask: 'Which of the threshold skills does each year of your course start, and which does it finish?' Avoid presenting the statement as the source of progression rules.")

s('2.7', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='joint and combined honours students', addressee='learner',
  verbs=['achieve', 'add', 'explore'], about='core skills in joint and combined degrees', domain='none', award=HON,
  find="Undergraduates studying Creative Writing courses as part of a combined or joint degree with other subjects will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the topics covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study.",
  para="Students taking the subject within a joint or combined degree will reach the core of its specific and generic skills, add others from their other subject and may work across the boundary between disciplines.",
  prac="In joint and combined degrees, make sure students will reach the core of the subject-specific and generic skills, let the partner subject add its own and use the overlap for interdisciplinary work.",
  ben="If you study creative writing as part of a joint or combined degree, you will gain the core subject and general skills, add others from your other subject and may explore where the two meet.",
  aaw=f"Describe this as an outcome (force will) for joint and combined honours students: the core of the subject's specific and generic skills, at FHEQ level 6. Cite it as {CITE}, para 2.7. Do not claim that a joint honours student must meet every item in 4.3 to 4.6, since the issuer says core elements only and does not name them; set it beside 4.3, 4.6 and {FW6 % 'qaa/fheq-2024/4.15.b1'}.",
  aad="Raise it when a joint or combined honours student, or a team designing such a course, asks what the writing half must cover. To a student, say that you will gain the core of the subject's skills and add others from your other subject; to staff, ask: 'Which of the threshold items does the writing half carry, and which does the other subject?' Avoid implying that the student must match a single honours student item for item.")

s('3.22', type='requirement', rung='none', force='should', level='none', appliesTo='Creative Writing courses', addressee='provider',
  verbs=['made', 'offered'], about='accessible assessment and clear policies', domain='none', award=HON,
  find="Learning in Creative Writing is supported by both formative and summative forms of assessment. Assessments should be made accessible for all students. Alternative assessments should be offered to meet all students' accessibility needs. Policies around extensions, late submissions and extenuating circumstances should be made clear to all students.",
  para="Learning is supported by formative and summative assessment; assessment should be accessible to every student, alternatives should be offered to meet accessibility needs and the rules on extensions, late work and extenuating circumstances should be clear to all.",
  prac="Make every assessment accessible, offer alternative assessments where a student's access needs call for them and publish the extension, late submission and extenuating circumstances policies in terms every student can find and follow.",
  ben=('n/a', 'a duty on the course; the student meets its effect, not a standard to reach'),
  aaw=f"Treat this as a set of should-level expectations on the course: accessible assessment, alternative assessments for access needs and clear policies on extensions and late work. It applies to provision for the honours degree, not to a level of attainment. Cite it as {CITE}, para 3.22. Do not present it as a student outcome or as a legal duty in itself; set it beside 1.31 and 3.17 on accessible workshops and 3.28 on clear criteria.",
  aad="Raise it with a programme team reviewing assessment or responding to a student's access needs. For staff, frame it as a design and policy check and ask: 'If a student cannot do this assessment as set, what is the alternative and who decides?' With a student who raises an access need or a late submission, point to the course policies it expects; do not give it to them as a standard to meet.")

s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['perform', 'refer'], about='performance above threshold; Annex D', domain='none', award=HON,
  find="The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.",
  para="Most students will do clearly better than the threshold; each provider decides how such achievement is evidenced and should consult Annex D of the qualifications frameworks, which describes the four honours classifications.",
  prac="Expect most students to go well past the threshold; when setting how achievement above it is evidenced and classified, refer to Annex D's descriptions of first, upper second, lower second and third-class honours.",
  ben=('n/a', 'a duty on the provider in judging classification; the student-facing rungs are 4.3 to 4.5'),
  aaw=f"Treat this as a should-level expectation on the provider: in judging achievement above threshold, refer to Annex D of the FHEQ (std:doc:qaa-fheq-2024-framework, Annex D, qaa/fheq-2024/annex-d/summary/r1/1st to 3rd). It holds for the honours degree at FHEQ level 6 and FQHEIS level 10. Cite it as {CITE}, para 4.2. Do not claim that the typical or excellent rungs map one to one onto classes; set it beside 4.3, 4.4 and 4.5.",
  aad="Raise it with a programme team or examiners setting marking criteria or classification rules. Frame it for staff and ask: 'How do your criteria for a first or a 2.1 draw on Annex D and on the typical and excellent rungs?' Avoid telling a student that a rung equals a class; with a student, talk about the rungs themselves.")

# ---- 2.2 outcome list (lead-in: through study of the subject, students will)
AAWO = ("Describe this as an outcome the statement says students will reach through study of the subject (force will), for the honours degree "
        "at FHEQ level 6 and FQHEIS level 10 (level inferred: the list sits under Design, before the levels are named in 2.3): {about}. "
        "Cite it as " + CITE + ", para 2.2, bullet {k}. Do not treat it as a rung of section 4 or as a regulatory requirement; set it beside "
        "{nb} and " + FW6 + ".")
AADO = ("Raise this when {when}. To a student, put it plainly in the second person as something the course will build; to staff, frame it "
        "as an outcome to make visible across modules. Ask: {q} Avoid reading the list aloud or presenting the item as a pass hurdle.")
def k22(k, verbs, about, domain, core, ben, nb, fw, when, q, find=None):
    r = dict(type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of the subject', addressee='learner',
             verbs=verbs, about=about, domain=domain, award=HON,
             para='Through study of the subject, students will reach ' + core + '.',
             prac='Students will, through the course, develop ' + core + '; make it visible in modules and assessment.',
             ben='Through your studies you will ' + ben + '.',
             aaw=AAWO.format(about=about, k=k, nb=nb) % fw, aad=AADO.format(when=when, q=q))
    if find:
        r['find'] = find
    P['2.2.b%d' % k] = r

k22(1, ['practised'], 'the resources of language and story', SK,
    "experienced use of the expressive, imaginative and emotional resources of language and story, structure and form included",
    "become practised in what language and story can do expressively, imaginatively and emotionally, including structure and form",
    '4.4.b6 and 4.3.b5', 'qaa/fheq-2024/4.15.b2', 'a student asks what the course will make them good at',
    "'Which resource of language do you rely on most, and which least?'")
k22(2, ['understand'], 'text, narrative and language as artistic materials', UN,
    "an understanding of text, narrative and language as materials for art, with their past traditions and possible uses",
    "understand text, narrative and language as materials for art, each with its own history and possible uses",
    '4.3.b7 and 4.4.b10', 'qaa/fheq-2024/4.15.b1', 'a student treats language only as a vehicle for content',
    "'If language is your material, what are you shaping in this piece?'")
k22(3, ['recognise'], 'audience responses to own work', UN,
    "recognition of the many ways audiences respond to and read their work",
    "recognise the many ways readers and audiences may respond to and interpret your work",
    '4.3.b8 and 4.4.b12', 'qaa/fheq-2024/4.15.b4', 'a student is surprised by how readers took a piece',
    "'How did your readers' responses differ from what you intended?'")
k22(4, ['develop'], 'critical insight and capability', UN,
    "growth in critical insight and in the capacity to use it",
    "develop critical insight and the capacity to use it",
    '4.4.b2 and 4.6.b17', 'qaa/fheq-2024/4.15.b7', 'a student asks how critical work fits a creative degree',
    "'What has critical reading shown you about your own writing?'")
k22(5, ['have'], 'responsibility for own work from idea to final draft', GS,
    "ownership of their own work from first idea through development and editing to the last redraft",
    "take responsibility for your own work, from the first idea through development and editing to the last draft",
    '4.6.b1 and 4.7.b2', 'qaa/fheq-2024/4.15.b9.1', 'a student relies on tutors to decide when a piece is finished',
    "'How do you decide a piece is ready?'")
k22(6, ['practised', 'appreciate'], 'editing over successive drafts, alone and with peers', SK,
    "practice in editing work through repeated drafts, on their own and with tutors and other students through peer review, and a grasp of why it matters",
    "practise editing your work over many drafts, on your own and with tutors and classmates, and see why it matters",
    '4.3.b1 and 4.4.b16', 'qaa/fheq-2024/4.15.b2', 'a student wants to submit a first draft',
    "'What changed between your second and third drafts, and who helped?'")
k22(7, ['appreciate'], 'creative and cultural contexts of writing', UN,
    "an appreciation of the many creative and cultural settings in which writing is made and read",
    "appreciate the many creative and cultural settings in which writing is made and read",
    '4.3.b7 and 4.4.b10', 'qaa/fheq-2024/4.15.b1', 'a student considers where their work might be published or performed',
    "'Where does writing like yours get made and read, and who decides?'",
    find='appreciate a wide range of creative and cultural contexts for the production and consumption of writing.')

# ---- rungs: 4.3 threshold, 4.4 typical, 4.5 excellent
R = {
 'threshold': dict(stem='4.3', force='threshold', ff=None, label='threshold',
   para='Will have shown, as the minimum for the honours degree, ', prac='At threshold, every honours graduate will have shown ',
   prac2='; make sure every passing student can evidence it.', ben='As a minimum for your honours degree, you will ',
   aaw=("Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), "
        "here {about}. Cite it as " + CITE + ", para 4.3, bullet {k}. Do not present it as a regulatory requirement or as where most students "
        "end, since 4.2 expects most to do clearly better. Set it beside {nb} and " + FW6 + "."),
   aad=("Raise this when {when}. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; "
        "to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: {q} Avoid reading the issuer's list "
        "aloud or treating this minimum as all a student should aim for.")),
 'typical': dict(stem='4.4', force='will', ff='4.1', label='typical',
   para='Will have shown, at the typical level for the honours degree, ', prac='At the typical level, most honours graduates will have shown ',
   prac2='; design teaching so that most students reach it.', ben='At the typical level for your honours degree, you will ',
   aaw=("Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 "
        "(FQHEIS level 10): {about}. Cite it as " + CITE + ", para 4.4, bullet {k}. Do not claim it is the pass requirement or a regulatory "
        "standard; the threshold list in 4.3 is the minimum. Set it beside {nb}, " + FW6 + " and Annex D's upper second band "
        "(qaa/fheq-2024/annex-d/summary/r1/2.1)."),
   aad=("Raise this when {when}. To a student, put it plainly in the second person as what most people show by the end of the honours degree, "
        "not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: {q} Avoid presenting it as the pass "
        "mark or reading the list aloud.")),
 'excellent': dict(stem='4.5', force='will', ff='4.1', label='excellent',
   para='May be among the qualities, of which graduates at the excellent level will show some: ', prac='At the excellent level, graduates will show some of these qualities; this one is ',
   prac2='; treat it as evidence for the top band, not a requirement.', ben='If you reach the excellent level, this may be one of the qualities you show: you ',
   aaw=("Describe this as one of the excellent-level qualities, of which the strongest honours graduates will show some, at FHEQ level 6 "
        "(FQHEIS level 10): {about}. Cite it as " + CITE + ", para 4.5, bullet {k}. Do not claim every graduate, or every excellent graduate, "
        "shows it, or that it sets a pass requirement. Set it beside {nb} and Annex D's first-class description %s."),
   aad=("Raise this when {when}. To a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; "
        "to staff, frame it as evidence for the top band. Ask: {q} Avoid presenting it as the minimum or as a list to tick off in full.")),
}
def kr(rung, k, verbs, about, domain, core, ben, nb, fw, when, q, find=None):
    d = R[rung]
    r = dict(type=rung, rung=rung, force=d['force'], level='fheq:6', appliesTo='graduates at the %s level' % d['label'],
             addressee='learner', verbs=verbs, about=about, domain=domain, award=HON,
             para=d['para'] + core + '.', prac=d['prac'] + core + d['prac2'], ben=d['ben'] + ben + '.',
             aaw=d['aaw'].format(about=about, k=k, nb=nb) % fw, aad=d['aad'].format(when=when, q=q))
    if d['ff']:
        r['forceFrom'] = d['ff']
    if find:
        r['find'] = find
    P['%s.b%d' % (d['stem'], k)] = r

T, TY, EX = 'threshold', 'typical', 'excellent'
kr(T, 1, ['generate', 'develop'], 'generating work and developing it by revision', SK,
   "the capacity to produce creative writing and improve it through editing and redrafting",
   "produce your own creative writing and improve it by editing and redrafting",
   '4.4.b1 and 4.6.b1', 'qaa/fheq-2024/4.15.b2', 'a student asks what the minimum is for a portfolio or how much redrafting counts',
   "'Which piece have you taken through more than one draft, and what changed between versions?'")
kr(T, 2, ['reflect'], 'reflection on own creative process and outputs', SK,
   "the capacity to think back over how they write and what they produce",
   "think back over how you write and what you produce",
   '4.4.b2, 4.5.b7 and 4.6.b17', 'qaa/fheq-2024/4.15.b7', 'a student is preparing a reflective commentary or learning journal',
   "'What did you learn about your own way of working from your last piece?'")
kr(T, 3, [], 'engagement with own creative interests and influences', SK,
   "active engagement with the interests that drive their writing and with the writers and works that shape it",
   "engage actively with what interests you as a writer and with the writers and works that influence you",
   '4.4.b3 and 4.4.b8', 'qaa/fheq-2024/4.15.b5', 'a student is unsure what to write about or whose work to read',
   "'Which writers or works have shaped your recent writing, and how can you tell?'")
kr(T, 4, [], 'early awareness of craft and narrative techniques', KN,
   "a beginning awareness of a range of craft and storytelling techniques",
   "be starting to recognise a range of craft and storytelling techniques",
   '4.4.b1 and 4.4.b4', 'qaa/fheq-2024/4.15.b1', 'a student asks what technical knowledge the course expects',
   "'Name two techniques you used on purpose in your last piece: what did each do?'")
kr(T, 5, [], 'awareness of the rules and possibilities of written and spoken language', KN,
   "awareness of how written and spoken language works across forms, genres and media, with its rules, its conventions and what it makes possible",
   "know how written and spoken language works across different forms, genres and media, including its rules, its conventions and what it lets you do",
   '4.4.b5 and 2.2.b1', 'qaa/fheq-2024/4.15.b1', 'a student is moving between page, performance and screen forms',
   "'What changes when a piece written for the page is read aloud or adapted for screen?'")
kr(T, 6, ['read', 'respond'], 'reading and responding to published and draft work', SK,
   "the capacity to read published writing and drafts in progress and to respond to them",
   "read both published writing and drafts in progress, and respond to them",
   '4.4.b9', 'qaa/fheq-2024/4.15.b7', 'a student prepares for a workshop or a critical response',
   "'When you read a classmate's draft, what do you look for first?'")
kr(T, 7, [], 'historical and cultural dimensions of language and literature', UN,
   "awareness of the history and culture behind how language is used and literature made, storytelling and changing technologies included",
   "understand the history and culture behind how language is used and literature is made, including storytelling and changing technologies",
   '4.4.b10 and 2.2.b7', 'qaa/fheq-2024/4.15.b1', 'a student asks why historical or contextual reading matters to a writer',
   "'How has a change in technology altered the way stories are told in a form you write in?'")
kr(T, 8, ['communicate', 'using'], 'communicating to diverse audiences across forms and media', SK,
   "the capacity to reach varied audiences through a range of narrative forms, digital tools and media",
   "communicate with different audiences, using a range of narrative forms, digital tools and media",
   '4.4.b13 and 4.5.b2', 'qaa/fheq-2024/4.15.b8', 'a student plans a piece for a particular readership or platform',
   "'Who is this piece for, and what would you change to reach a different audience?'")
kr(T, 9, [], 'awareness of group work skills and inclusivity', GS,
   "awareness of what effective group work needs, with openness and a commitment to inclusion",
   "know what it takes to work well in a group, and be open and committed to including everyone",
   '4.4.b15, 4.6.b13 and 4.6.b14', 'qaa/fheq-2024/4.15.b9.1', 'a student prepares for a workshop or a group project',
   "'What helps a writing group work well for everyone in it?'")
kr(T, 10, [], 'applications of writing skills to careers and enterprise', UN,
   "awareness of how the subject's skills apply in varied settings, careers and enterprises",
   "know how your writing skills can be used in different settings, careers and ventures of your own",
   '4.4.b19 and 4.5.b6', 'qaa/fheq-2024/4.15.b9.3', 'a student asks what the degree leads to',
   "'Which two kinds of work could use the skills you are building, and how?'")
kr(T, 11, [], "the subject's contribution to sustainability", UN,
   "awareness of what creative writing can contribute to sustainability and environmental questions",
   "understand what creative writing can contribute to sustainability and to environmental questions",
   '4.4.b14 and 4.5.b5', 'qaa/fheq-2024/4.15.b1', 'a student is drawn to nature or climate writing, or asks how writing bears on sustainability',
   "'How could a story or poem change how a reader thinks about the environment?'")
kr(T, 12, [], 'forms of prose, poetry, story and drama', KN,
   "an understanding of the forms that prose, poetry, story and drama take",
   "understand the forms of prose, poetry, story and drama",
   '4.4.b4 and 4.3.b4', 'qaa/fheq-2024/4.15.b1', 'a student chooses forms to work in or asks what forms they need to know',
   "'Which form are you least familiar with, and what defines it?'")
kr(T, 13, ['explore', 'engage'], 'exploring a range of genres', SK,
   "the capacity to try out and work within a range of genres, such as memoir, short fiction, crime or fantasy",
   "try out and work in a range of genres, from memoir and short fiction to crime, fantasy or writing for young readers",
   '4.5.b1', 'qaa/fheq-2024/4.15.b2', 'a student has written in one genre only',
   "'Which genre have you not yet tried, and what might it teach you?'")

kr(TY, 1, ['conceptualise', 'generate', 'develop'], 'conceiving and developing original work with many techniques', SK,
   "the capacity to conceive, produce and develop original creative writing, drawing on many editing, presentation, narrative and craft techniques",
   "conceive, produce and develop original writing, drawing on many editing, presentation, storytelling and craft techniques",
   '4.3.b1', 'qaa/fheq-2024/4.15.b2', 'a student wants to know what good, not just passing, work looks like',
   "'Which techniques did you choose for this piece, and why those?'")
kr(TY, 2, [], 'reflective, critically evaluative approach to composition', SK,
   "a reflective approach to writing that includes critical evaluation of their own practice",
   "reflect on how you compose and evaluate your writing practice critically",
   '4.3.b2 and 4.5.b7', 'qaa/fheq-2024/4.15.b7', 'a student writes a critical commentary',
   "'Where does your commentary judge your choices, rather than only describe them?'")
kr(TY, 3, ['explore'], 'relationships between reading and own practice', SK,
   "active exploration of how their reading relates to their own writing",
   "explore actively how what you read relates to what you write",
   '4.3.b3 and 4.4.b8', 'qaa/fheq-2024/4.15.b5', 'a student builds a reading list or writes about influences',
   "'What have you read this term that changed something in your own writing?'")
kr(TY, 4, ['compose'], 'composing a story, poem or prose piece', SK,
   "the capacity to write a story, poem or prose piece that works",
   "write a story, poem or prose piece that works well",
   '4.3.b12', 'qaa/fheq-2024/4.15.b2', 'a student submits a finished piece',
   "'What makes this piece complete, and what would you still change?'")
kr(TY, 5, ['utilise'], 'using the conventions and possibilities of language in emerging media', SK,
   "the capacity to use the conventions of written and spoken language, and what it makes possible, across forms, genres and new media",
   "use the conventions of written and spoken language, and what it makes possible, across forms, genres and new media",
   '4.3.b5', 'qaa/fheq-2024/4.15.b2', 'a student adapts work between page, stage, audio or digital media',
   "'Which convention did you bend on purpose, and what did it gain you?'")
kr(TY, 6, [], 'creative, discerning engagement with what language can do', SK,
   "a creative and discerning engagement with what written and spoken language can do expressively, poetically and in narrative",
   "engage creatively and with discernment with what written and spoken language can do: its expressive, poetic and storytelling power",
   '4.5.b3 and 2.2.b1', 'qaa/fheq-2024/4.15.b7', 'a student works on voice, imagery or sound in their writing',
   "'Which line in your draft does the most work, and how?'")
kr(TY, 7, [], 'independent, disciplined commitment to writing', GS,
   "independent, disciplined commitment to their own writing",
   "commit to your own writing independently and with discipline",
   '4.6.b1 and 4.6.b3', 'qaa/fheq-2024/4.15.b9.1', 'a student struggles with routine or deadlines',
   "'What writing routine do you keep when no deadline is close?'")
kr(TY, 8, [], 'understanding the link between reading and own practice', UN,
   "an understanding of how reading connects to their own writing practice",
   "understand how your reading connects to your own writing",
   '4.4.b3 and 4.3.b3', 'qaa/fheq-2024/4.15.b5', 'a student asks why a writing course asks them to read so much',
   "'How does what you read show up in what you write?'")
kr(TY, 9, ['read', 'respond'], 'critical, creative and practical response to published and draft work', SK,
   "the capacity to read published writing and drafts in progress and to answer them critically, creatively and practically",
   "read published writing and drafts in progress and answer them critically, creatively and practically",
   '4.3.b6 and 4.4.b16', 'qaa/fheq-2024/4.15.b7', 'a student gives workshop feedback or writes a critical response',
   "'What practical change would you suggest to this draft, and why?'")
kr(TY, 10, [], 'historical and socio-cultural dimensions of language and story', UN,
   "an understanding of the history and the social and cultural setting of language use, from older ways of making texts to divergent kinds of story and new digital and media technologies",
   "understand the history and the social and cultural setting of language, from older ways of making texts to different kinds of story and new digital media",
   '4.3.b7 and 2.2.b7', 'qaa/fheq-2024/4.15.b1', 'a student studies the contexts of a form or writes for new media',
   "'How did the way this form was produced in the past shape what it became?'")
kr(TY, 11, ['contextualise'], 'placing own writing in historical, cultural or generic frameworks', SK,
   "the capacity to place their own writing within a given historical, cultural or genre framework",
   "place your own writing within a historical, cultural or genre setting",
   '4.7.b4', 'qaa/fheq-2024/4.15.b3.1', 'a student writes a critical commentary or preface',
   "'Which tradition does your piece belong to, and where does it depart from it?'")
kr(TY, 12, [], 'writing as narrative expression for diverse audiences and purposes', UN,
   "an understanding of writing as a narrative means of expression and communication that serves varied audiences and purposes",
   "understand writing as a way of telling and communicating that serves different audiences and purposes",
   '4.4.b13 and 2.2.b3', 'qaa/fheq-2024/4.15.b8', 'a student asks why audience and purpose matter in creative work',
   "'What is this piece trying to do for its reader?'")
kr(TY, 13, ['communicate', 'using'], 'communicating with diverse audiences across many forms and media', SK,
   "the capacity to communicate with varied audiences through many narrative forms, story skills and media",
   "communicate with different audiences through many narrative forms, storytelling skills and media",
   '4.3.b8 and 4.5.b2', 'qaa/fheq-2024/4.15.b8', 'a student adapts a piece for a new platform or readership',
   "'How would you retell this piece for an audience unlike you?'")
kr(TY, 14, ['explore'], 'imaginative exploration of place, planet and other species', SK,
   "the capacity to explore imaginatively place, planet, climate, habitat, sustainability or the lives of other species",
   "explore in your writing places, the planet, climate, habitats, sustainability or the lives of other species",
   '4.3.b11 and 4.5.b5', 'qaa/fheq-2024/4.15.b6', 'a student takes up nature, place or climate writing',
   "'What does your setting do in the story beyond being a backdrop?'")
kr(TY, 15, ['engage', 'improve'], "engaging with diverse writers to improve own and others' work", GS,
   "the capacity to work well with different voices and varied groups of writers to strengthen their own and others' writing",
   "work well with writers whose voices and backgrounds differ from yours, so that your writing and theirs gets better",
   '4.3.b9 and 4.6.b14', 'qaa/fheq-2024/4.15.b9.1', 'a student works in a mixed workshop group',
   "'Whose perspective in your workshop has most changed your writing?'")
kr(TY, 16, [], 'giving and receiving feedback constructively', GS,
   "skill in taking and giving constructive feedback on their own work and their peers'",
   "give useful feedback to others and take feedback on your own work constructively",
   '4.6.b16, 4.7.b10 and 4.4.b9', 'qaa/fheq-2024/4.15.b8', 'a student is nervous about workshops',
   "'What feedback have you acted on recently, what did you set aside, and why?'")
kr(TY, 17, [], 'co-authoring for a shared vision', SK,
   "co-writing skills and techniques that bring a shared creative vision to life",
   "write with others, using skills and techniques that bring a shared vision to life",
   '4.5.b9 and 4.6.b13', 'qaa/fheq-2024/4.15.b9.1', 'a student joins a collaborative project such as a script or anthology',
   "'How did you and your co-writers settle a disagreement about the piece?'")
kr(TY, 18, ['plan', 'carry'], 'research skills and independent research', SK,
   "awareness of research skills and methods suited to creative writing, and the capacity to plan and conduct their own research",
   "know the research skills and methods that suit creative writing, and plan and carry out research of your own",
   '4.7.b7', 'qaa/fheq-2024/4.15.b6', 'a student plans research for a novel, script or project',
   "'What research does your project need, and how will you gather it?'")
kr(TY, 19, [], 'strategic transferability of writing and story skills', UN,
   "an understanding of how, with strategy, the subject's writing and story skills transfer to varied settings, careers and enterprises",
   "understand how to transfer your writing and storytelling skills, with purpose, to different settings, careers and ventures of your own",
   '4.3.b10 and 4.5.b6', 'qaa/fheq-2024/4.15.b9.3', 'a student plans a career or placement',
   "'How would you describe your story skills to an employer outside publishing?'")

# excellent: the lead paragraph's two sentences, then the list ("some of the following")
s('4.5', type='excellent', rung='excellent', force='will', forceFrom='4.1', level='fheq:6', appliesTo='graduates at the excellent level',
  addressee='learner', verbs=['demonstrate', 'produce'], about='integrating the lower rungs with enterprise and flair', domain=SK, award=HON,
  find="Creative Writing graduates who attain the excellent standard demonstrate the qualities listed above, creatively integrated and combined with independent enterprise and flair to produce work that is ambitious, markedly original in its relation to existing work in its field and searching in its enquiry.",
  para="Will have shown, at the excellent level, the qualities of the lower rungs brought together creatively with independent enterprise and flair, in work that is ambitious, clearly original against what already exists and probing in its enquiry.",
  prac="At the excellent level, graduates will have joined up the threshold and typical qualities creatively, with independent enterprise and flair, producing ambitious work that stands out as original in its field and asks searching questions.",
  ben="At the excellent level, you will bring together everything above with flair and independent enterprise, producing ambitious work that is clearly original next to what already exists and that asks probing questions.",
  aaw=f"Describe this as the excellent rung's defining standard: the threshold and typical qualities, integrated with enterprise and flair, at FHEQ level 6 (FQHEIS level 10) for the honours degree. Cite it as {CITE}, para 4.5. Do not present it as the minimum or as a regulatory requirement; set it beside 4.5.b1 to 4.5.b9, the typical list in 4.4 and Annex D's first-class descriptions (qaa/fheq-2024/annex-d/cognitive/r4/1st, qaa/fheq-2024/annex-d/summary/r1/1st).",
  aad="Raise it when a student or a marking team asks what lifts work above the typical level. To a student, say plainly that excellent work combines everything else with ambition, originality and flair; to staff, frame it as the profile of the top band. Ask: 'Where in this portfolio is the work most ambitious, and what makes it original against its field?' Avoid presenting it as what every student must reach.")
s('4.5.s2', type='excellent', rung='excellent', force='should', level='fheq:6', appliesTo='graduates at the excellent level',
  addressee='learner', verbs=['meet', 'exceed'], about='meeting industry presentation standards', domain=SK, award=HON,
  find="Where an industry presentation standard exists, the writing should meet or exceed this.",
  para="Where the industry has a presentation standard, writing at the excellent level should match or surpass it.",
  prac="At the excellent level, where an industry sets a presentation standard (a script format or a manuscript layout, for instance), the writing should reach or go beyond it.",
  ben="If you aim for the excellent level, and an industry has its own presentation standard, such as a script or manuscript format, your writing should reach or go beyond it.",
  aaw=f"Describe this as a should-level condition on excellent work at FHEQ level 6 (FQHEIS level 10): where an industry presentation standard exists, the writing meets or exceeds it. Cite it as {CITE}, para 4.5 (second sentence). Do not extend it to the threshold or typical rungs, or name a particular industry standard the issuer does not; set it beside 4.6.b2 and Annex D's first-class presentation description (qaa/fheq-2024/annex-d/practical/r4/1st).",
  aad="Raise it when a student prepares a submission package, script or manuscript, or when a team sets criteria for the top band. To a student, say plainly that the best work looks professional by the standards of its industry; to staff, frame it as a check at the excellent level only. Ask: 'Which industry format applies to this piece, and does it meet it?' Avoid treating presentation as a pass requirement.")

kr(EX, 1, ['produce', 'offers'], 'original writing transforming genre', SK,
   "original writing that changes how a genre can be approached",
   "write original work that changes how a genre can be approached",
   '4.3.b13 and 4.5', 'qaa/fheq-2024/annex-d/cognitive/r4/1st', 'a student works within or against genre conventions',
   "'What does your piece do that the genre usually does not?'")
kr(EX, 2, [], 'fluency across narrative forms, story skills and media', SK,
   "fluent command of many narrative forms, story skills and media",
   "move fluently between many narrative forms, storytelling skills and media",
   '4.4.b13 and 4.3.b8', 'qaa/fheq-2024/annex-d/practical/r1/1st', 'a student works confidently across forms',
   "'Which form or medium feels as natural to you as your main one?'")
kr(EX, 3, [], 'innovative use of language', SK,
   "inventive use of language whatever the subject or form",
   "use language inventively, whatever your subject or form",
   '4.4.b6', 'qaa/fheq-2024/annex-d/cognitive/r4/1st', 'a student experiments with style or voice',
   "'Where in this piece does your use of language surprise the reader?'")
kr(EX, 4, ['presents'], 'original responses to inclusion, diversity, accessibility and equality', SK,
   "writing that brings original, meaningful and potentially influential responses to inclusion, diversity, accessibility and equality in society",
   "write in original, meaningful ways that could make a difference to inclusion, diversity, accessibility and equality",
   '4.4.b15 and 4.6.b14', 'qaa/fheq-2024/annex-d/cognitive/r4/1st', 'a student writes about identity, difference or access',
   "'What does your piece let a reader see about inclusion that they might have missed?'")
kr(EX, 5, ['presents', 'explores'], 'transformative writing on sustainability and ecology', SK,
   "writing that shows a transforming awareness of how change can support sustainability, or that opens new ways of seeing how humans, other beings and their habitats relate",
   "write in ways that show how change could support sustainability, or open new ways of seeing how people, other creatures and their habitats relate",
   '4.4.b14 and 4.3.b11', 'qaa/fheq-2024/annex-d/cognitive/r4/1st', "a student's work engages with climate, nature or ecology",
   "'What might a reader see or do differently about the living world after reading this?'")
kr(EX, 6, ['articulates'], 'new spaces for creative and entrepreneurial expression', SK,
   "writing that opens new room for creative and entrepreneurial expression",
   "write in ways that open new room for creative and enterprising expression",
   '4.4.b19 and 4.3.b10', 'qaa/fheq-2024/annex-d/transferable/r4/1st', 'a student develops a new format, venture or publishing idea',
   "'What space for writing does your project create that did not exist before?'")
kr(EX, 7, ['sustain', 'develop'], 'critically impactful, self-reflective, interdisciplinary writing', SK,
   "writing with critical force and self-awareness, deeply reflective, that builds and keeps up critical links between the subject and creative practice in other disciplines",
   "write with critical force and self-awareness, reflecting deeply and linking your writing to creative practice in other disciplines",
   '4.4.b2 and 4.3.b2', 'qaa/fheq-2024/annex-d/transferable/r5/1st', 'a student writes a creative-critical or interdisciplinary piece',
   "'What does your reflection reveal about the piece that the piece alone does not?'")
kr(EX, 8, ['explores', 'uses'], 'diversity of languages and dialects', SK,
   "writing that draws on and explores the wide variety of languages and dialects, giving voice to regional, global and media-specific varieties",
   "draw on and explore many languages and dialects, giving voice to regional, global and media-specific ways of speaking",
   '4.4.b6 and 4.4.b15', 'qaa/fheq-2024/annex-d/practical/r1/1st', 'a student writes in dialect, another language or a mixed idiom',
   "'Why does this voice need its own dialect or language, and how will readers meet it?'")
kr(EX, 9, ['demonstrates'], 'advanced co-production with communities of practice', SK,
   "writing that shows advanced co-production through editing, workshops and collaboration, and work with communities of practice outside the classroom",
   "co-create at an advanced level through editing, workshops and collaboration, working with writing communities outside your classes",
   '4.4.b17 and 4.6.b13', 'qaa/fheq-2024/annex-d/transferable/r2/1st', 'a student leads a group project, anthology or community writing work',
   "'What did the group make that none of you could have made alone?'",
   find="writing that demonstrates advanced co-production skills via editing, workshopping, collaborative, creative and/or engagement with communities of practice beyond the classroom.")

# ---- 4.6 generic skills (lead-in: on graduating with honours, students should be able to)
AAWG = ("Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 "
        "(FQHEIS level 10): {about}. Cite it as " + CITE + ", para 4.6, bullet {k}. Do not claim it is a subject-specific or regulatory "
        "requirement, or that it holds unchanged at master's level. Set it beside {nb} and " + FW6 + ", which it refines.")
AADG = ("Raise this when {when}. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a "
        "transferable skill to build and evidence across modules. Ask: {q} Avoid reading the list aloud or treating it as separate from the writing itself.")
def kg(k, verbs, about, core, ben, nb, fw, when, q, find=None):
    r = dict(type='outcome', rung='none', force='should', level='fheq:6', appliesTo='honours graduates of the subject', addressee='learner',
             verbs=verbs, about=about, domain=GS, award=HON,
             para='On graduating with honours, students should be able to ' + core + '.',
             prac='By graduation, honours students should be able to ' + core + '; give them chances to practise and evidence it.',
             ben='By the time you graduate, you should be able to ' + ben + '.',
             aaw=AAWG.format(about=about, k=k, nb=nb) % fw, aad=AADG.format(when=when, q=q))
    if find:
        r['find'] = find
    P['4.6.b%d' % k] = r

kg(1, ['initiate', 'take'], 'initiative and responsibility for own work',
   "start their own work and answer for it", "start your own work and take responsibility for it",
   '2.2.b5 and 4.7.b2', 'qaa/fheq-2024/4.15.b9.1', 'a student waits to be told what to write',
   "'What project have you started without being asked?'")
kg(2, ['present'], 'professional presentation of information',
   "present information to a professional standard that suits the setting", "present information professionally, in a way that suits the setting",
   '4.5.s2', 'qaa/fheq-2024/4.15.b8', 'a student prepares a submission, pitch or portfolio',
   "'Would an editor or agent take this submission seriously as it stands?'")
kg(3, ['work', 'set', 'manage', 'meet'], 'self-management and independent work',
   "manage themselves, work independently, set goals, handle their workload and keep to deadlines",
   "manage yourself, work on your own, set goals, handle your workload and hit deadlines",
   '4.4.b7 and 4.7.b2', 'qaa/fheq-2024/4.15.b9.1', 'a student is behind or overloaded',
   "'How do you plan your writing time across competing deadlines?'")
kg(4, ['anticipate', 'accommodate', 'negotiate'], 'handling change and ambiguity',
   "foresee and adjust to change, and work through situations that are ambiguous, uncertain or unfamiliar",
   "see change coming, adjust to it and find your way through situations that are unclear, uncertain or new to you",
   '4.6.b15 and 4.7.b2', 'qaa/fheq-2024/4.15.b4', 'a student faces an open or unclear brief',
   "'What did you do the last time a brief was unclear?'")
kg(5, ['identify', 'reflecting'], 'identifying strengths and needs through reflection',
   "identify strengths and development needs by reflecting on their personal growth",
   "reflect on your own development and identify your strengths and what you need to work on",
   '4.3.b2 and 4.6.b17', 'qaa/fheq-2024/4.15.b9.3', 'a student plans personal development or writes a reflective account',
   "'What is one strength you can show evidence for, and one need you are working on?'")
kg(6, ['select', 'employ', 'source', 'navigate', 'retrieve', 'evaluate', 'manipulate', 'manage'], 'information and communication technologies; managing information',
   "choose and use communication and information technologies, and find, sift, judge and manage information from many sources",
   "choose and use digital and communication tools, and find, judge and manage information from many sources",
   '4.4.b18', 'qaa/fheq-2024/4.15.b5', 'a student researches for a project or works with digital platforms',
   "'How do you judge whether a source is reliable enough to use?'")
kg(7, ['produce', 'narrate', 'drawing'], "factual storytelling from own or others' accounts",
   "produce or tell a true story in clear or persuasive language, from their own experience or from other people's accounts",
   "write or tell a true story in clear or persuasive language, using your own experience or what others have told you",
   '4.7.b13', 'qaa/fheq-2024/4.15.b8', 'a student writes memoir, life writing, journalism or creative non-fiction',
   "'Whose account are you telling, and what do you owe them?'")
kg(8, ['work'], 'flexible independent and collaborative work',
   "work adaptably, alone and with others", "work flexibly, on your own and with other people",
   '4.6.b13', 'qaa/fheq-2024/4.15.b9.1', 'a student moves between solo and group tasks',
   "'When do you work best alone, and when with others?'")
kg(9, ['demonstrate', 'use'], 'transferable communication and story skills',
   "show and put to active use many transferable communication and storytelling skills",
   "show and put to active use many transferable communication and storytelling skills",
   '4.6.b10 and 4.6.b12', 'qaa/fheq-2024/4.15.b8', 'a student asks what the degree gives them beyond writing',
   "'Which of your story skills would help in a job that is not about writing?'")
kg(10, ['communicate', 'influence', 'developing', 'constructing', 'presenting'], 'concise, accurate, persuasive communication and argument',
   "put across their own and others' ideas briefly, accurately and persuasively so as to sway opinion, building and presenting arguments suitably",
   "put your own and others' ideas across briefly, accurately and persuasively to change minds, building and presenting arguments in the right way",
   '4.6.b9 and 4.7.b15', 'qaa/fheq-2024/4.15.b3.1', 'a student writes an essay, pitch or argument',
   "'What is your central claim, and what would persuade a sceptical reader?'")
kg(11, ['develop', 'understand', 'listening'], 'active listening',
   "build the skill of listening actively and see why it matters", "build your skill in listening actively and understand why it matters",
   '4.4.b16', 'qaa/fheq-2024/4.15.b8', 'a student takes part in workshops',
   "'What did you hear in the last workshop that you nearly missed?'")
kg(12, ['communicate'], 'communicating across media with awareness of story and language',
   "communicate in varied media with a strong sense of what story, narrative and language are for and how they work",
   "communicate in different media, with a strong sense of how story, narrative and language work and what they are for",
   '4.4.b13 and 4.6.b9', 'qaa/fheq-2024/4.15.b8', 'a student moves a piece into a new medium',
   "'What does story do in this medium that it cannot do on the page?'")
kg(13, ['interact'], 'effective interaction in teams and workshops',
   "work well with others in teams or groups, for instance in collaboration or workshops",
   "work well with others in teams and groups, for example in workshops or joint projects",
   '4.3.b9, 4.4.b17 and 4.7.b14', 'qaa/fheq-2024/4.15.b9.1', 'a student has trouble in a group',
   "'What do you do when a group stalls or disagrees?'")
kg(14, ['demonstrate'], 'understanding equality, diversity and inclusivity',
   "show that they understand equality, diversity and inclusion", "show that you understand equality, diversity and inclusion",
   '4.3.b9, 4.4.b15 and 4.5.b4, and paragraphs 1.21 to 1.24 to which the issuer points', 'qaa/fheq-2024/4.15.b9.1 (no level 6 descriptor names equality; personal responsibility is the nearest)',
   'a student asks how inclusion bears on their writing or workshop conduct',
   "'How does your writing or workshop practice make room for people unlike you?'")
kg(15, ['adapt', 'look'], 'adapting to demands; wider social and commercial effects',
   "adjust to varied demands and tasks and see past the task in hand to its wider setting, including what their work does socially and commercially",
   "adapt to different demands and tasks and look past the immediate job to its wider setting, including the social and commercial impact of what you make",
   '4.6.b4', 'qaa/fheq-2024/4.15.b9.2', 'a student works to a brief or commission',
   "'Who else is affected by this piece once it is published?'")
kg(16, ['appreciate'], 'value of giving and receiving feedback',
   "value giving feedback and receiving it", "value both giving and receiving feedback",
   '4.4.b16 and 4.7.b10', 'qaa/fheq-2024/4.15.b9.3', 'a student resists critique',
   "'What is the most useful feedback you have had, and why did it help?'")
kg(17, ['evaluate', 'reflect'], 'critical self-reflection on practice and assumptions',
   "evaluate and reflect on themselves, critically examining their own practices and assumptions",
   "evaluate your work and reflect critically on your own practices and assumptions",
   '4.3.b2, 4.4.b2 and 4.5.b7', 'qaa/fheq-2024/4.15.b7', 'a student writes a reflective commentary',
   "'Which assumption about your writing has your reflection challenged?'")
kg(18, ['exhibit'], 'confidence in life-enhancing skills',
   "show growing confidence in the wider personal skills the subject builds, for example self-expression and self-awareness",
   "grow more confident in the wider personal skills writing builds, such as self-expression and self-awareness",
   '4.7.b16', 'qaa/fheq-2024/4.15.b9.3', 'a student talks about why they write or how the course has changed them',
   "'How has writing changed the way you express yourself outside class?'",
   find='exhibit increased confidence in a wide range of life-enhancing skills related to the subject, such as confidence, expression and self-awareness.')

# ---- 4.7 master's level (lead-in plain present: "students achieving master's level demonstrate")
AAWM = ("Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force "
        "describes), at FHEQ level 7 (FQHEIS level 11): {about}. Cite it as " + CITE + ", para 4.7, bullet {k}. Do not claim it applies to the "
        "honours degree or that the issuer makes it a requirement. Set it beside {nb} and " + FW7 + ".")
AADM = ("Raise this when {when}. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it "
        "as a design aim for the master's course and its final project. Ask: {q} Avoid applying it to undergraduates or reading the list aloud.")
def km(k, verbs, about, domain, core, ben, nb, fw, when, q):
    P['4.7.b%d' % k] = dict(type='outcome', rung='none', force='describes', level='fheq:7', appliesTo="students achieving master's level",
             addressee='learner', verbs=verbs, about=about, domain=domain, award=MAS,
             para="Students achieving master's level show " + core + '.',
             prac="At master's level, students show " + core + '; design the course and its final project so that they can.',
             ben="At master's level, you " + ben + '.',
             aaw=AAWM.format(about=about, k=k, nb=nb) % fw, aad=AADM.format(when=when, q=q))

km(1, ['support'], 'advanced creative skills for a substantial project', SK,
   "advanced creative and imaginative skills that carry the conception, design and making of a substantial creative writing project",
   "use advanced creative and imaginative skill to conceive, design and produce a substantial writing project",
   '4.7.b3 and 4.5', 'qaa/fheq-2024/4.17.b3', "a master's student plans their major project",
   "'What is the core idea of your project, and how will its design serve it?'")
km(2, ['managing', 'writing', 'learning', 'required', 'deliver', 'demonstrates'], 'composite professional skills for a substantial project', GS,
   "combined professional skills, managing themselves and their time, writing independently and learning on their own, needed to complete a substantial project with initiative and sound decisions when things are complex and unpredictable",
   "manage yourself and your time, write independently and learn on your own, so that you can complete a major project, taking the initiative and deciding well when things are complex and unpredictable",
   '4.6.b3 and 4.6.b1', 'qaa/fheq-2024/4.17.b8.2', "a master's student is managing a long project alone",
   "'What decisions have you made on your project without guidance, and how did you make them?'")
km(3, ['complete', 'constitutes'], 'a substantial original piece of writing', SK,
   "the completion of a large creative writing piece, of suitable length or form, that adds something original to its field",
   "finish a large creative writing piece, of fitting length or form, that adds something original to its field",
   '4.7.b1 and 4.7.b4', 'qaa/fheq-2024/4.17.b3', "a master's student asks what the final project must achieve",
   "'What does your project add that is not already in its field?'")
km(4, ['produce', 'relating', 'contextualising', 'illuminating'], 'critical writing on the project and its tradition', SK,
   "a critical piece on how their project arose and was carried out, setting it within a fitting scholarly or creative tradition and making clear what is original in it",
   "write a critical piece on how your project began and developed, place it in a scholarly or creative tradition and show what is original about it",
   '4.4.b11 and 4.7.b3', 'qaa/fheq-2024/4.17.b4.1', "a master's student drafts the critical or reflective part of the project",
   "'Which tradition does your project answer to, and where does it break new ground?'")
km(5, ['identify', 'define', 'resolve'], 'analytical and imaginative problem-solving in a professional project', SK,
   "advanced analytical and imaginative skills for spotting, defining and solving the problems a professional writing project throws up",
   "use advanced analytical and imaginative skills to spot, define and solve the problems your writing project raises",
   '4.7.b2 and 4.7.b9', 'qaa/fheq-2024/4.17.b5', "a master's student is stuck on a structural or practical problem",
   "'How did you define the problem before you tried to solve it?'")
km(6, ['enabling'], 'applied awareness of own process for adaptability', UN,
   "a practical grasp of how they work as writers, what influences them and how they approach writing, so that they adapt skilfully to any creative challenge",
   "know in practice how you work, what influences you and how you approach writing, so you can adapt well to any creative challenge",
   '4.3.b2 and 4.6.b17', 'qaa/fheq-2024/4.17.b6', "a master's student meets an unfamiliar brief or form",
   "'How would you change your usual process for a form you have never tried?'")
km(7, ['carry'], 'independent research for the project', SK,
   "the capacity to conduct their own research to support the project",
   "carry out your own research to support your project",
   '4.4.b18', 'qaa/fheq-2024/4.17.b2', "a master's student plans project research",
   "'What research has changed the direction of your project?'")
km(8, ['support', 'respond', 'form', 'improve'], 'advanced craft, editing and story skills; using feedback', SK,
   "advanced craft, editing and storytelling skills that move the work forward, including acting on feedback from peers and tutors and the confidence to judge for themselves how to make the project better",
   "use advanced craft, editing and storytelling skills to move your work forward, respond to feedback from peers and tutors and trust your own judgement on how to make it better",
   '4.4.b16 and 4.7.b10', 'qaa/fheq-2024/4.17.b6', "a master's student weighs conflicting feedback",
   "'Which feedback did you decide not to follow, and why?'")
km(9, ['engage', 'applying'], "analytical group discussion and problem-solving on peers' work", GS,
   "the capacity to take part in analytical, critical group discussion, bringing problem-solving to bear on other writers' work",
   "take part in analytical, critical group discussion and help solve problems in other writers' work",
   '4.7.b10 and 4.6.b13', 'qaa/fheq-2024/4.17.b5', "a master's student takes part in workshops",
   "'What problem in a peer's draft did you help them solve, and how?'")
km(10, ['give', 'demonstrates', 'exhibiting', 'considering', 'influence'], 'sensitive feedback', GS,
   "the capacity to give feedback with sensitivity, for instance by showing a keen sense of what the writer is aiming for and weighing how varied backgrounds and experiences shape judgements of good writing",
   "give feedback sensitively, showing you grasp what the writer is trying to do and that different backgrounds and experiences shape how people judge good writing",
   '4.4.b16 and 4.6.b16', 'qaa/fheq-2024/4.17.b8.1', "a master's student gives workshop feedback",
   "'What was the writer trying to achieve, and did your feedback start there?'")
km(11, ['adapting', 'considering'], 'adapting style across media; technology as a creative tool', SK,
   "skill in adjusting writing style to varied media and narrative forms, weighing the creative risks and gains of technology as a tool for making and representing",
   "adjust your writing style to different media and narrative forms, and weigh the creative risks and gains of using technology",
   '4.5.b2 and 4.7.b12', 'qaa/fheq-2024/4.17.b3', "a master's student writes for digital or multimedia platforms",
   "'What does this technology add to the work, and what does it risk?'")
km(12, ['evaluate', 'discuss', 'adapt', 'position', 'using', 'develop'], 'positioning work within social challenges, including AI ethics', SK,
   "the capacity to evaluate, discuss, adapt and place their work in relation to wider social challenges such as sustainable development, diversity or the ethics of making work with AI and other new technologies",
   "evaluate, discuss, adapt and place your work in relation to wider social questions such as sustainability, diversity or the ethics of using AI to create",
   '4.4.b14, 4.5.b4 and 4.5.b5', 'qaa/fheq-2024/4.17.b5', "a master's student uses AI tools or writes on social themes",
   "'How would you justify, to a reader, the way you used or avoided AI in this work?'")
km(13, ['transform', 'applying', 'transforms'], 'transforming complex and difficult material into effective writing', SK,
   "the capacity to turn complex cultural material, and sometimes emotionally hard material, observation and experience, into effective creative writing with fitting narrative and literary forms and techniques, for example writing about people and place that changes how readers perceive other beings and their surroundings",
   "turn complex and sometimes emotionally difficult material, observations and experiences into effective writing, using the right narrative and literary forms, for instance writing about people and place that changes how readers see other beings and the world around them",
   '4.4.b14 and 4.5.b5', 'qaa/fheq-2024/4.17.b5', "a master's student writes from difficult personal or cultural material, with the support 3.18 describes in mind",
   "'What craft choices let you handle this material without being overwhelmed by it?'")
km(14, ['demonstrating', 'respond'], 'advanced teamwork in changing cultural industries', GS,
   "advanced teamwork, showing they can respond to fast-moving cultural industries, to professional challenges and to global contexts",
   "work in teams at an advanced level and respond to fast-moving cultural industries, to professional challenges and to global settings",
   '4.6.b13 and 4.4.b17', 'qaa/fheq-2024/4.17.b8.2', "a master's student works on a collaborative or industry project",
   "'How did your team adjust when the brief or the market changed?'")
km(15, ['communicate', 'demonstrated'], 'communicating to specialist and non-specialist audiences', GS,
   "the capacity to communicate well with specialists and non-specialists, shown through advanced writing, speaking and storytelling",
   "communicate well with experts and non-experts through advanced writing, speaking and storytelling",
   '4.6.b10 and 4.6.b12', 'qaa/fheq-2024/4.17.b5', "a master's student presents work publicly or pitches to industry",
   "'How would you explain your project to a funder who has never read poetry?'")
km(16, ['apply', 'improve'], 'writing as a life-enhancing skill for well-being', GS,
   "the capacity to draw on their grasp of how creative writing can enrich lives to help themselves and others gain well-being, confidence, self-expression and self-awareness",
   "use what you understand about writing as a life-enhancing skill to support your own and other people's well-being, confidence and self-expression",
   '4.6.b18', 'qaa/fheq-2024/4.17.b8.1', "a master's student plans community, teaching or well-being work",
   "'Where could your writing skills help other people, and how would you know it helped?'")

# gradeOf: the same outcome one rung below, inferred (the issuer lists each rung separately)
GRADE = {'4.4.b1': '4.3.b1', '4.4.b2': '4.3.b2', '4.4.b9': '4.3.b6', '4.4.b10': '4.3.b7', '4.4.b13': '4.3.b8',
         '4.4.b15': '4.3.b9', '4.4.b19': '4.3.b10',
         '4.5.b2': '4.4.b13', '4.5.b3': '4.4.b6', '4.5.b5': '4.4.b14', '4.5.b7': '4.4.b2', '4.5.b9': '4.4.b17'}
TH = {'1.31': 'theme:accessibility'}

# ------------------------------------------------------------------ levels, themes, relations
S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.3'), dict(id='fqheis:10', role='cites', locator='D1, 2.3'),
                  dict(id='fheq:7', role='cites', locator="D1, 2.10 (integrated master's); 4.7 (master's level, framework not named there)"),
                  dict(id='fqheis:11', role='cites', locator="D1, 2.10"),
                  dict(id='fheq:4', role='mentions', locator='D1, 3.5 ("At Level 4": framework not named; inferred FHEQ, Part E)'),
                  dict(id='fheq:5', role='mentions', locator='D1, 3.6 ("At Level 5": framework not named; inferred FHEQ, Part E)')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.3: "FHEQ Level 6; FQHEIS Level 10" for the degree with honours); matches std:doc:qaa-fheq-2024-framework Table 1'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.10: \"FHEQ Level 7; FQHEIS Level 11\" for the integrated master's); matches std:doc:qaa-fheq-2024-framework S5 (shared descriptor 4.17)")])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '3.5', '3.6', '3.18', '3.19', '4.3', '4.4', '4.5', '4.6', '4.7']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '3.17', '3.18', '3.19', '3.22', '4.5']),
      dict(id='theme:esd', role='carries', carriedIn=['1.33', '1.34', '1.35', '1.36', '1.37', '1.38', '3.19', '4.3', '4.4', '4.5', '4.7']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.15', '1.16', '1.39', '1.40', '1.41', '2.6', '3.19', '4.3', '4.4', '4.5']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['3.9', '3.20', '3.26', '3.32', '4.7'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-creative-writing-2019-benchmarks (not ingested)', note='section 6 names the second edition (2019) and the original (2016); the closing line names this the third edition (D1, section 6)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the four honours classifications, for achievement above threshold (D1, 4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ Levels 6 and 7 (D1, 2.3, 2.10)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS Levels 10 and 11 (D1, 2.3, 2.10)'),
      dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='listed in section 5; the sustainability paragraphs cite UNESCO (2017) directly (1.33, 1.34)'),
      dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='listed in section 5, behind the enterprise paragraphs (1.39 to 1.41)'),
      dict(rel='refersTo', target='QAA Quality Code for Higher Education and its Advice and Guidance (not ingested)', note='front matter; section 5')]

# ------------------------------------------------------------------ the variant's sections
SB1 = [
  "An artistic and critical discipline centred on imagination, curiosity and the power of language, whose focus is generating ideas and expressing originality through literary, poetic or narrative forms (D1, 1.1, 1.8, 1.9).",
  "Making texts sits at the centre: students develop their own creative practice and methods, drafting and redrafting, across many genres, forms and media, from print to performance, screen, audio, games and new forms (D1, 1.2, 1.8, 3.1).",
  "Originality is understood as emerging from the writer's own cultural, literary and personal contexts in dialogue with existing forms, influences and techniques (D1, 1.10).",
  "Learning is collaborative and workshop-based, with peer and tutor feedback at its heart, alongside independent study (D1, 1.2, 1.4, 1.20, 3.17, 3.23).",
  "Reading is broad and includes craft, criticism, theory and other media; projects may be creative-critical, and creative writing is itself a form of research (D1, 1.5, 1.11 to 1.13).",
  "Highly interdisciplinary: studied alone or in many combinations, drawing on literature, drama, poetics, mythology, folklore, rhetoric and more (D1, 1.2, 1.3, 1.18, 3.2, 3.3).",
  "Strongly tied to the creative industries and wider careers, and to well-being and personal confidence in self-expression (D1, 1.1, 1.7, 1.16)."]
SB2 = [
  dict(theme='theme:edi', inThisSubject="inclusive learning communities and reading lists in line with the Equality Act 2010, belonging, participation plans in the four nations, external agencies tackling inequality in publishing and students defining their own canon of forms and voices; graduates show understanding of equality and engage with diverse writers and voices (D1, 1.21 to 1.26, 3.18, 3.19, 4.6)", statements=['4.3.b9', '4.4.b15', '4.5.b4', '4.5.b8', '4.6.b14', '4.7.b10', '4.7.b12']),
  dict(theme='theme:accessibility', inThisSubject="many routes of entry, portfolio or presentation in place of written entry tests, accessible materials and spaces, prepared and adapted workshops, support for writing about personal themes and accessible assessment with alternatives (D1, 1.27 to 1.32, 3.17, 3.18, 3.22)", statements=['1.31', '3.22', '4.5.b4']),
  dict(theme='theme:esd', inThisSubject="nature and environmental writing, the human and the more than human, ecological thinking through story and UNESCO's key competencies (critical, self-aware and anticipatory thinking); the rungs move from awareness to imaginative exploration to transformative writing on sustainability (D1, 1.33 to 1.38, 4.3, 4.4, 4.5, 4.7)", statements=['4.3.b11', '4.4.b14', '4.5.b5', '4.7.b12', '4.7.b13']),
  dict(theme='theme:enterprise', inThisSubject="careers in the creative industries and beyond, creative entrepreneurship, writing to commission and to briefs, with a list of enterprise skills the subject builds; the rungs move from awareness of applications to strategic transfer to new spaces for entrepreneurial expression (D1, 1.15, 1.16, 1.39 to 1.41, 4.3, 4.4, 4.5)", statements=['4.3.b10', '4.4.b19', '4.5.b6', '4.6.b15']),
  dict(theme='theme:generative-ai', inThisSubject="AI as content and tool: courses explore its limits and possibilities, analyse its effect on creative industries and use it to develop material with transparency; submissions may engage with AI; assessment of originality and methods may need to change; master's students weigh the ethics of using AI (D1, 3.9, 3.20, 3.26, 3.32, 4.7)", statements=['4.7.b12'])]
SB3 = dict(
  areas=[dict(component='1.12', gloss='reading: traditional and contemporary models, games, audio, podcasts, criticism and theory'),
         dict(component='3.1', gloss='making texts in literary, poetic, narrative and multimodal forms'),
         dict(component='3.5', gloss='Level 4: habits of writing, principal forms, reader and audience, language and contexts'),
         dict(component='3.6', gloss='Level 5: craft techniques, reflective practice, reading and practice, context and diversity'),
         dict(component='3.7', gloss='Level 6: advanced modules, extended project, languages and dialects, research practices, live briefs'),
         dict(component='3.8', gloss='a community of practice and individual and collective voices'),
         dict(component='3.9', gloss='digital, multi-platform and multimodal forms, games, graphic novels and AI')],
  practices=[dict(component='3.10', kind='teaching', gloss='direct instruction, discussion of student work, experiment, risk-taking and failure'),
             dict(component='3.12', kind='learning', gloss='preparatory exercises, prompts and pieces for feedback'),
             dict(component='3.13', kind='teaching', gloss='lectures, seminars and workshops; in person, online, hybrid, on site'),
             dict(component='3.14', kind='teaching', gloss='seminars, small workshops, tutorials, supervision, online activity'),
             dict(component='3.16', kind='learning', gloss='collaborative and independent study with reflection'),
             dict(component='3.17', kind='teaching', gloss='presenting work in writing rooms and workshops, with accessible practice'),
             dict(component='3.18', kind='teaching', gloss='support for writing on personal and difficult themes'),
             dict(component='3.21', kind='assessment', gloss='portfolio, dissertation or capstone research project'),
             dict(component='3.23', kind='assessment', gloss='formative assessment through workshops and self-critique'),
             dict(component='3.24', kind='assessment', gloss='written feedback on work in progress'),
             dict(component='3.26', kind='assessment', gloss='forms of submission, from novel extracts and scripts to pitches and collaborative projects'),
             dict(component='3.27', kind='assessment', gloss='students devising assignments and criteria with tutors'),
             dict(component='3.28', kind='assessment', gloss='clear, shared criteria used in peer and self-evaluation'),
             dict(component='3.29', kind='assessment', gloss='what criteria may evaluate, from originality to engagement with feedback'),
             dict(component='3.31', kind='assessment', gloss='assessing workshop facilitation and contribution')])
OUTCOMES = [
  dict(outcome='generating and developing work', threshold='4.3.b1', typical='4.4.b1', excellent='none', basis='inferred', domain=SK, award=HON),
  dict(outcome='reflection on own practice', threshold='4.3.b2', typical='4.4.b2', excellent='4.5.b7', basis='inferred', domain=SK, award=HON),
  dict(outcome='reading and responding to work', threshold='4.3.b6', typical='4.4.b9', excellent='none', basis='inferred', domain=SK, award=HON),
  dict(outcome='historical and cultural dimensions of language', threshold='4.3.b7', typical='4.4.b10', excellent='none', basis='inferred', domain=UN, award=HON),
  dict(outcome='communicating with diverse audiences across forms and media', threshold='4.3.b8', typical='4.4.b13', excellent='4.5.b2', basis='inferred', domain=SK, award=HON),
  dict(outcome='inclusive work with others', threshold='4.3.b9', typical='4.4.b15', excellent='none', basis='inferred', domain=GS, award=HON),
  dict(outcome='transferring skills to careers and enterprise', threshold='4.3.b10', typical='4.4.b19', excellent='none', basis='inferred', domain=UN, award=HON),
  dict(outcome='what language can do', threshold='none', typical='4.4.b6', excellent='4.5.b3', basis='inferred', domain=SK, award=HON),
  dict(outcome='place, planet and other species', threshold='none', typical='4.4.b14', excellent='4.5.b5', basis='inferred', domain=SK, award=HON),
  dict(outcome='co-writing and co-production', threshold='none', typical='4.4.b17', excellent='4.5.b9', basis='inferred', domain=SK, award=HON)]
SB4 = dict(
  rungs=[dict(rung='threshold', leadIn='4.3', award=HON, items=13),
         dict(rung='typical', leadIn='4.4', award=HON, items=19),
         dict(rung='excellent', leadIn='4.5', award=HON, items=11)],
  rungBases=("4.1: the statement sets minimum, typical and excellent standards that students will have demonstrated at the award of honours; "
             "4.2: most students do significantly better than the threshold, judged by each provider with Annex D; 4.5: the excellent rung is a "
             "lead paragraph (two records: the integrating standard, and a should on industry presentation standards) and a list of which "
             "excellent graduates show some; 4.6: generic skills, outside the rungs; 4.7: master's level, outside the rungs"),
  outcomeLists=[dict(leadIn='2.2', gloss='what students will do through study of the subject', items=7, award=[HON]),
                dict(leadIn='4.6', gloss='generic skills honours graduates should be able to show', items=18, award=[HON]),
                dict(leadIn='4.7', gloss="what students achieving master's level show (plain present; force describes)", items=16, award=[MAS])],
  outcomes=OUTCOMES)
SB4A_FULL = []
SB5 = [
  dict(body='professional, statutory and regulatory bodies (PSRBs), unnamed', says='the statement supports them on academic standards, and their requirements are a further reference point in course design (D1, front matter)', requirements='not-applicable-by-design: no body named (Part E)'),
  dict(body='Office for Students (regulator, England)', says="under its regulatory framework the statements are not sector-recognised standards in England (D1, front matter)", requirements='not yet ingested (Part E)')]
SB6 = dict(
  themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '3.5', '3.6', '3.18', '3.19', '4.3', '4.4', '4.5', '4.6', '4.7'], statements=['4.3.b9', '4.4.b15', '4.5.b4', '4.5.b8', '4.6.b14', '4.7.b10', '4.7.b12']),
          dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '3.17', '3.18', '3.19', '3.22', '4.5'], statements=['1.31', '3.22', '4.5.b4']),
          dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.33', '1.34', '1.35', '1.36', '1.37', '1.38', '3.19', '4.3', '4.4', '4.5', '4.7'], statements=['4.3.b11', '4.4.b14', '4.5.b5', '4.7.b12', '4.7.b13']),
          dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.15', '1.16', '1.39', '1.40', '1.41', '2.6', '3.19', '4.3', '4.4', '4.5'], statements=['4.3.b10', '4.4.b19', '4.5.b6', '4.6.b15']),
          dict(id='theme:generative-ai', named='artificial intelligence (AI); generative AI', carriedIn=['3.9', '3.20', '3.26', '3.32', '4.7'], statements=['4.7.b12'])],
  frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.3', '2.10', '4.2']),
              dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.3', '2.10'])],
  bodies=[dict(body='PSRBs (unnamed)', citedIn=['front matter']),
          dict(body='Office for Students (regulator, England)', citedIn=['front matter']),
          dict(body='UCAS (admissions; disclosure of disability)', citedIn=['1.28']),
          dict(body='UNESCO (source of the ESD definition and key competencies)', citedIn=['1.33', '1.34'])],
  sharedDocuments=[
    dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2', '5'], role='descriptions of the four honours classifications (1st, 2.1, 2.2, 3rd), for achievement above threshold'),
    dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='QAA and Advance HE (2021) Education for Sustainable Development Guidance', citedIn=['5'], role='listed reference behind the sustainability paragraphs'),
    dict(document='std:doc:qaa-enterprise-2018-guidance', named='QAA (2018) Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers', citedIn=['5'], role='listed reference behind the enterprise paragraphs'),
    dict(document='UNESCO (2017) Education for Sustainable Development Goals: Learning Objectives (external, not ingested)', named="UNESCO, 2017; UNESCO's Key Competencies for Sustainable Development", citedIn=['1.33', '1.34', '5'], role='definition of ESD and the key competencies the subject develops'),
    dict(document='Equality Act 2010 (legislation, not ingested)', named='the Equality Act 2010', citedIn=['1.21', '5'], role='the principles that texts and community-building align with'),
    dict(document='Research Excellence Framework (external, not ingested)', named='the Research Excellence Framework', citedIn=['1.5'], role='acknowledges creative writing as research'),
    dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code for Higher Education; The UK Quality Code for Higher Education', citedIn=['front matter', '5'], role='course design, teaching, external expertise, monitoring'),
    dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter', '5'], role='explains unfamiliar terms'),
    dict(document='Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland); Quality Enhancement Review (Wales) (not ingested)', named='the same', citedIn=['front matter', '5'], role='where the statement is a key reference point'),
    dict(document="Access and Participation Plans (England); Enhancement-led Institutional Review (Scotland); Access to Success Strategy (Northern Ireland); Strategic Equality Plan (Wales) (not ingested)", named='the same', citedIn=['1.24'], role='institution-level routes to wider participation')])

B1 = [
  dict(slug='threshold-standard', definition='the minimum a student will have demonstrated to be awarded the honours degree (D1, 4.1, 4.3)', beneficiaryDefinition='the least you must have shown by the end of your honours degree', scopeNote='the list in 4.3', category='unknown', practices=['education']),
  dict(slug='typical-standard', definition='what most honours graduates will have demonstrated, above the threshold (D1, 4.1, 4.4)', beneficiaryDefinition='what most people show by the end of the degree', scopeNote='the list in 4.4', category='unknown', practices=['education']),
  dict(slug='excellent-standard', definition='the lower rungs integrated with enterprise and flair, with some of a further list of qualities (D1, 4.1, 4.5)', beneficiaryDefinition='what the strongest work shows, beyond the typical', scopeNote='graduates show some, not all, of the list', category='unknown', practices=['education']),
  dict(slug='originality', definition="writing that reflects the writer's own cultural, literary and personal contexts, reached gradually by joining individual expression with existing forms and techniques (D1, 1.10)", beneficiaryDefinition='work only you could have written, made from your own contexts in dialogue with what exists', category='unknown', practices=['education']),
  dict(slug='workshop', definition='a collaborative or peer-led session where students read work in progress and peers, invited by the tutor, respond (D1, 1.31, 3.17)', beneficiaryDefinition='a class where you share a draft and others give feedback', scopeNote='also writing rooms', category='unknown', practices=['education']),
  dict(slug='creative-critical', definition='a project whose creative text also makes a critical or theoretical argument or explores process, method and technique (D1, 1.13)', category='unknown', practices=['education'])]
B2A = [
  dict(concept='threshold-standard', form='threshold standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='typical-standard', form='typical standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='excellent-standard', form='excellent standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
  dict(concept='originality', form='Originality', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
  dict(concept='workshop', form='workshops', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
  dict(concept='creative-critical', form='creative-critical', lang='en', partOfSpeech='adjective', termStatus='preferred', register='discipline-specific')]
B4 = []; B5 = []
D3 = []

E = [
  "SB4, rung shape: three lists with lead-ins naming the rung, as in Psychology (4.3 threshold 13, 4.4 typical 19, 4.5 excellent 9), but the excellent lead-in 4.5 says graduates show 'some of the following', so no excellent item is expected of every excellent graduate. The lead paragraph of 4.5 is itself recorded as two excellent statements (4.5: the integrating standard; 4.5.s2: the industry presentation standard, 'should'), so the excellent rung counts 11 records.",
  "S4, id 4.5.s2: our id for 4.5's second sentence, which carries its own 'should'; it is not the issuer's numbering and the builder sorts it after the numbered records.",
  "S4, force: threshold items take `threshold` from 4.1 ('minimum ... standards that students will have demonstrated'); typical and excellent items, whose lead-ins have no modal ('demonstrate'), take `will` from 4.1 by `forceFrom`. Generic skills (4.6) take `should` from their lead-in. For Abbott at P3.",
  "S4, 4.7 master's level: the lead-in is plain present ('students achieving master's level demonstrate'), and 4.1's 'will' covers the honours degree only, so the 16 items are recorded with force `describes`. For Abbott: read as will? Their level is recorded as fheq:7 from 2.10 (integrated master's, 'FHEQ Level 7; FQHEIS Level 11'); 4.7 names no framework and 3.33 speaks of master's degrees generally.",
  "S4, 2.2: an outcome list in 'will' under Design ('Through study of the subject, Creative Writing students will'); recorded as 7 outcome items at fheq:6, the level inferred from 2.3.",
  "S4, paragraphs taken as statements: 1.20 (should, a provider expectation in the last sentence; the paragraph is the record), 1.31 ('required', recorded as must), 2.3 (will, with 'it is expected that'), 2.7 (will), 3.22 (should), 4.2 (should).",
  "S4, not taken as statements (D-std-0002 (a)): the purposes list after 1.7 and the list in 1.10 (aims and descriptions, no modal; 1.10's 'will always exhibit innovation' describes originality); 1.11 ('will involve', descriptive); 1.41 (skills the subject 'enables', no outcome lead-in); 2.1 (design characteristics); 2.4 and 2.5 ('will seek', 'will introduce', 'may be expected': predictive or hedged); 2.9 ('it would be expected', 'would be capable': outside the five words); 3.14 ('will usually'); 3.32 ('will need to consider', a forecast for the discipline); 3.33 ('the added expectation that graduates are prepared': plain present, outside the five words).",
  "S4, plain-present provider norms not recorded as statements (template open point 5): 1.21 (texts 'are selected to act in alignment' with the Equality Act 2010), 1.30 (course designers and tutors 'consider accessibility'; 'they aim to ensure' a list of five), 2.14 to 2.16 (review, externality, examiners), 3.25 (outcomes and criteria 'are clearly articulated'), 3.28 (criteria 'are as clear, itemised and transparent as possible'), 3.30 ('care is taken'). 1.32's 'an adaptable approach may be required' is hedged by may and not taken.",
  "S4, skeleton corrections by `find`: 1.20, 2.2.b7, 2.3, 3.22, 4.2, 4.5.b9 and 4.6.b18, whose skeleton spans ran on into the next heading or a page number; 1.31 and 2.7 cut without their paragraph numbers. 4.5 is cut as its first sentence and 4.5.s2 as its second; the lead-in's last sentence stays with the stem.",
  "S4, gradeOf: 12 links, all inferred (the issuer lists each rung separately and pairs nothing): 4.4.b1, b2, b9, b10, b13, b15, b19 to the threshold list; 4.5.b2, b3, b5, b7, b9 to the typical list. Less plain matches, for P3: 4.4.b15 to 4.3.b9 (inclusive group work against engaging diverse writers), 4.5.b3 to 4.4.b6 (inventive language against creative engagement with language), 4.5.b7 to 4.4.b2 (reflection; the excellent item adds interdisciplinary connection).",
  "S4, gradeOf not drawn where the content matches but the domain shifts from awareness to use, since a link must keep its domain: 4.4.b5 (using language conventions) against 4.3.b5 (awareness of them, knowledge); 4.4.b14 (exploring place and planet) against 4.3.b11 (awareness of the subject's contribution to sustainability, understanding). The outcomes 'what language can do', 'place, planet and other species' and 'co-writing' start at the typical rung.",
  "S4, domain: our reading, not stated. Awareness items are knowledge where they concern techniques or language rules (4.3.b4, b5, b12) and understanding where they concern contexts and applications (4.3.b7, b10, b11). 4.3.b9 (awareness of group-work skills) is generic-skill. 4.4.b1 says 'original Creative Writing skills', read as original writing.",
  "S4, 4.6.b14 points to 'paragraphs 1.21-1.24' (the EDI paragraphs); a reference, not cut (DPN-1). 4.6.b14 has no matching FHEQ level 6 descriptor; its aaw points to personal responsibility (4.15.b9.1) as the nearest.",
  "S4, verbs: noun-phrase items (4.3.b3 to b5, b7, b9 to b12; 4.4.b2, b6 to b8, b10, b12, b16, b17, b19; 4.5.b2, b3) give no action verb, so `verbs` is empty; 4.6.b3's 'self-manage' and 4.6.b9 to 4.7 items' auxiliaries are left out.",
  "S3: the purposes list (16 bullets) belongs to the heading 'Purposes of Creative Writing in higher education' after 1.7 and is held in the skeleton's component 1.7; the heading 'Characteristics of Creative Writing in higher education' follows it, before 1.8. Sub-heading ranges in SUB are ours, from the heading lines.",
  "S5 and SB6, frameworks: FHEQ by name in 2.3, 2.10 and 4.2 (Frameworks, Annex D); FQHEIS in 2.3 and 2.10. 3.5 to 3.7 say 'Level 4', 'Level 5' and 'Level 6' without naming a framework: read as FHEQ levels (inferred) and recorded in S5 as mentions only. CQFW is not cited. 'Scottish Highers' (1.27) and the four-year Scottish honours degree (2.8) name no framework.",
  "SB5 and SB6, bodies: no professional body for the subject is named; PSRBs appear only generically (front matter). The Office for Students is named as England's regulator. UCAS (1.28) and UNESCO (1.33, 1.34) are named organisations, not PSRBs; listed in SB6 only.",
  "SB6, themes: the generative AI material (3.9, 3.20, 3.26 bullet 12, 3.32, 4.7.b12) is recorded as theme:generative-ai by the batch 1 convention; the issuer has no AI section of its own. TH tags in S4 only 1.31, the one statement inside a theme's own paragraphs; SB2 and SB6 list the statements elsewhere that carry a theme.",
  "SB6, shared documents: the ESD guidance (2021) and the enterprise guidance (2018) are cited only in section 5 (excluded matter); the body text cites UNESCO (2017) directly. citedIn '5' marks the reference list.",
  "S2, subjects: HECoS 100046 and CAH19-01-05 are the subject's own name ('creative writing'), entered as stated; CAH19-01 (English studies), the CAH2 group above it, is inferred. Scriptwriting (100729) and poetry writing (100730), in the same CAH3 group, are not named as subjects and are not entered.",
  "S7, supersedes: section 6 names the 2019 second edition and the 2016 original; this is the third edition (April 2024). The 2023 advisory group is the one that wrote this edition.",
  "Patterns differing from Psychology: an excellent lead-in that asks for 'some of' its list and carries a 'should' of its own (industry presentation standard); generic skills as a separate should-list (4.6); a master's list in plain present (4.7); an outcome list in section 2 (2.2) rather than section 3; lead-ins with no modal ('demonstrate'); a generative AI strand across content and assessment; no professional body.",
  "S9: not researched in P1.",
  "S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are still to check."]
