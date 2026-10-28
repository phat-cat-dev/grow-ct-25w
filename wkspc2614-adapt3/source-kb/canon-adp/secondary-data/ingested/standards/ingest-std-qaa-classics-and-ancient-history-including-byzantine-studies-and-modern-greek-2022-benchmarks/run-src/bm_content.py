# bm_content.py: run 0093 (std), QAA Subject Benchmark Statement Classics and Ancient History (including Byzantine Studies and Modern Greek), March 2022. Judgement for tools/bm_build.py.
# Templates: standards 0.8.0-draft, benchmark 0.6.0-draft, run layer 0.7.0-draft; brief BM-BRIEF 0.2.1. Our words throughout except FINDS (the issuer's spans).
# Exact statement texts where the skeleton cut wrongly (trailing headings or page numbers); 4.4.b11 occurs twice and is placed with `after`.
FINDS = {
    '1.13.b7': 'an analytical knowledge and ability to understand, read, write (and possibly speak and hear) one or more ancient and modern languages, encompassing a thorough knowledge of grammatical structures, a broad vocabulary and range of appropriate idioms, a sensitive knowledge of register and translation skills.',
    '4.4.b11': 'make effective and appropriate use of digital resources and information technology as a source of information, means of communication and aid to learning.',
    '1.25': '1.25 In general, an inclusive environment for learning also anticipates the varied requirements of learners and aims to ensure that all students have equal access to educational opportunities. Students should be offered learning opportunities that are equally accessible to all , by means of inclusive design wherever possible and by means of reasonable individual adjustments where necessary.',
    '3.12': '3.12 Courses in Modern Greek require proficiency in the modern Greek language and take as their main concern the language, literature, thought and history of the Greek- speaking world since the later Middle Ages.',
    '3.17': '3.17 An honours graduate in the subject area will generally have had the opportunity to experience all or most of the following modes of teaching and learning:',
    '3.20': "3.20 Wherever possible, it is highly desirable that students who wish to do so are given opportunity and encouragement to acquire or improve linguistic skills in Greek (ancient, medieval or modern) and/or Latin (ancient, medieval or early modern) or in another language of the ancient Mediterranean at any stage in their course of study for an honours degree. Differential access to the study of ancient languages before university, and diverse levels of attainment within different jurisdictions, requires the provision of different language pathways within degree courses and, where appropriate, may necessitate implementation of support to enable equivalent levels of attainment among students upon graduation irrespective of their prior linguistic training. The provision of such pathways also means that arrangements should be put in place so that students can access language modules also at a later point in their course. Experience of these languages at any stage in a course may significantly benefit command of other subject-specific abilities and forms of knowledge characteristic of honours graduates in the subject area as well as enhance development of more general abilities, such as the ability to systematise complex datasets or to analyse the logical structure of means of communication. Command of Greek and/or Latin is also an indispensable foundation for research degrees in many fields within the subject area and an invaluable asset for those entering master's degree courses.",
    '3.21': '3.21 A complementary range of skills may be acquired through training in classical or Byzantine art, field archaeology or the kind of artefact studies for which museological expertise is required. For many students there may have been the opportunity to begin study of such subjects at an early point in their honours degree course, with some going on to take more advanced and specialised options as they progress. In other courses this may not necessarily have been the case, and it may therefore be appropriate for students towards the end of their studies to be offered the opportunity to begin study of classical or Byzantine art or to gain experience of field archaeology. Where possible, opportunities to work in museums, galleries and in archaeological companies and units may be made available to students who might benefit from them, whether on an occasional basis or via internships or work experience during university vacations. Training involving direct engagement with landscapes and objects in a range of settings (such as critical walking, site surveys, general observation, drawing, creating video/audio recordings, writing descriptions) develops competencies that prepare students for work in many environments. For any such activities reasonable adjustments will be made.',
    '3.24': '3.24 Assessments should enable students to demonstrate a range of attributes, including autonomy, critical reflection and critical judgement in particular.',
    '4.2': "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd.",
}

HON = "bachelor's with honours"
CITE = 'QAA, 2022, Classics and Ancient History Subject Benchmark Statement'

META = dict(
    run='0093', p1='2026-10-03 16:33',
    title='Subject Benchmark Statement Classics and Ancient History (including Byzantine Studies and Modern Greek)',
    heading='Subject Benchmark Statement: Classics and Ancient History (including Byzantine Studies and Modern Greek) (QAA, March 2022)',
    edition='March 2022 (fifth edition)', published='2022-03',
    status='current',
    supersedes='the fourth edition (2019), named in the advisory group list (D1, section 6); earlier editions 2014, 2007 and 2000',
    subjects=[dict(scheme='hecos', code='100300', label='classical studies', basis='stated'),
              dict(scheme='hecos', code='100298', label='ancient history', basis='stated'),
              dict(scheme='hecos', code='100774', label='Byzantine studies', basis='stated'),
              dict(scheme='hecos', code='101124', label='Latin studies', basis='stated'),
              dict(scheme='hecos', code='101126', label='classical Greek studies', basis='stated'),
              dict(scheme='hecos', code='101440', label='classical art and archaeology', basis='stated'),
              dict(scheme='hecos', code='101129', label='classical reception', basis='inferred'),
              dict(scheme='cah', code='CAH20-01-05', label='classics', basis='stated'),
              dict(scheme='cah', code='CAH20-01-01', label='history', basis='stated'),
              dict(scheme='cah', code='CAH20-01', label='history and archaeology', basis='stated'),
              dict(scheme='hecos', code='100329', label='modern languages', basis='inferred')],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (Classics and Ancient History fifth edition, March 2022)',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("This document records what the QAA's 2022 statement for Classics and Ancient History, with Byzantine Studies and Modern Greek, "
                     "expects of an honours graduate and of the courses that lead there. Read S4 for the standards: section 4 gives three rungs, "
                     "threshold (third class), typical (2:1 or 2:2) and excellent (first class), each a list of examples of evidence, and section 1 adds "
                     "four lists of the knowledge, qualities of mind and abilities a graduate has. Every standard has a practitioner version, a student "
                     "version and two instructions for AI agents who write about it or use it in conversation. The frameworks it cites (FHEQ level 6, "
                     "FQHEIS level 10, Annex D) are pointed to by id and never copied."),
    summary=("Classics and Ancient History (including Byzantine Studies and Modern Greek), bachelor's degree with honours, MA (Hons) in Scotland "
             "(FHEQ level 6; FQHEIS level 10), fifth edition, March 2022. Three rungs are stated, each led by a paragraph naming the class: threshold "
             "(4.3, 10 items), typical (4.4, 11 items) and excellent (4.5, 12 items); the lists run in near parallel, so most outcomes are traced "
             "across all three. Section 1 lists the subject-specific characteristics of graduates (1.13, 7 items), the cognitive attributes (1.14, 7), "
             "the specific abilities (1.15, 8) and the practical capacities (1.16, 7). Fourteen paragraphs oblige or state outcomes: facing the "
             "subject's history of elitism, inclusive and accessible teaching, progression and joint honours, sensitive material, language "
             "requirements of Classics and Modern Greek courses, language pathways, adjustments for field and museum work, assessment and Annex D. "
             "Themes: equality, diversity and inclusion; accessibility; sustainability (education for sustainable development); entrepreneurship and "
             "enterprise education with employability. No professional, statutory or regulatory body accredits the subject; subject associations "
             "and the British Schools at Athens and Rome are named as partners."),
    authority='reference: a sector reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland (D1, front matter)')

S2 = dict(
    governs="what a graduate in Classics and Ancient History, Byzantine Studies or Modern Greek is expected to know, do and understand at the end of an honours degree, and the nature of courses in the subject",
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    statedScope='"This document is a QAA Subject Benchmark Statement for Classics and Ancient History (including Byzantine Studies and Modern Greek) that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies." (D1, front matter); 1.1 names bachelor\'s degrees with honours, including the MA (Hons) in Scotland',
    statedSubjects=[
        dict(name='Classics and Ancient History', locator='(D1, title; 1.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100300', label='classical studies'), dict(scheme='hecos', code='100298', label='ancient history'),
                    dict(scheme='cah', code='CAH20-01-05', label='classics')]),
        dict(name='Byzantine Studies', locator='(D1, title; 1.1; 3.2; 3.11)', kind='subject',
             codes=[dict(scheme='hecos', code='100774', label='Byzantine studies')]),
        dict(name='Modern Greek', locator='(D1, title; 1.1; 3.2; 3.12)', kind='subject', codes=[]),
        dict(name='Classics; Ancient Greek; Latin', locator='(D1, 3.6; 3.7)', kind='programme title',
             codes=[dict(scheme='hecos', code='100300', label='classical studies'), dict(scheme='hecos', code='101126', label='classical Greek studies'),
                    dict(scheme='hecos', code='101124', label='Latin studies')]),
        dict(name='Classical Studies (Classical Civilisation)', locator='(D1, 3.8)', kind='programme title',
             codes=[dict(scheme='hecos', code='100300', label='classical studies')]),
        dict(name='Ancient History', locator='(D1, 3.9)', kind='programme title',
             codes=[dict(scheme='hecos', code='100298', label='ancient history'), dict(scheme='cah', code='CAH20-01-01', label='history')]),
        dict(name='Classical Archaeology', locator='(D1, 3.10)', kind='programme title',
             codes=[dict(scheme='hecos', code='101440', label='classical art and archaeology')]),
        dict(name='Late Antique Studies', locator='(D1, 3.11)', kind='specialism',
             codes=[dict(scheme='hecos', code='100298', label='ancient history')]),
        dict(name='joint and combined honours, such as Latin and Ancient History, Classical Archaeology and Ancient History or liberal arts', locator='(D1, 1.2; 1.3; 2.7; 3.5)', kind='programme title',
             codes=[dict(scheme='hecos', code='100300', label='classical studies')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Classics and Ancient History (including Byzantine Studies and Modern Greek) degree',
            '2': 'Distinctive features of a Classics and Ancient History (including Byzantine Studies and Modern Greek) degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.4', 'Context'), ('1.5', '1.6', 'Purposes of a Classics and Ancient History (including Byzantine Studies and Modern Greek) degree'),
       ('1.7', '1.19', 'Opportunities'),
       ('1.20', '1.21', 'Characteristics of a Classics and Ancient History (including Byzantine Studies and Modern Greek) degree'),
       ('1.22', '1.25', 'Equality, diversity and inclusion'), ('1.26', '1.29', 'Sustainability'),
       ('1.30', '1.31', 'Entrepreneurship and enterprise education'),
       ('2.1', '2.1', 'Design'), ('2.2', '2.3', 'Accessibility'), ('2.4', '2.8', 'Progression'), ('2.9', '2.10', 'Flexibility'),
       ('2.11', '2.12', 'Partnership'), ('2.13', '2.16', 'Monitoring and review'),
       ('3.1', '3.12', 'Content'), ('3.13', '3.14', 'Teaching and learning: Starting point and end point'),
       ('3.15', '3.15', 'Independent learning and acquisition of core and transferable skills'),
       ('3.16', '3.16', 'Modes of teaching and learning'), ('3.17', '3.19', 'Examples of different modes of teaching and learning'),
       ('3.20', '3.20', 'Sub-disciplinary examples: Example 1: language'),
       ('3.21', '3.21', 'Example 2: classical or Byzantine art or field archaeology'),
       ('3.22', '3.22', 'Assessment: Wide variety of assessment methods'),
       ('3.23', '3.24', 'Assessment of general cognitive attributes: general remarks'),
       ('3.25', '3.25', 'Assessment of practical abilities: general remarks'), ('3.26', '3.27', 'Specific forms of summative assessment'),
       ('4.1', '4.2', 'Introduction'), ('4.3', '4.3', 'Threshold level (3rd class)'), ('4.4', '4.4', 'Typical level (2:1 or 2:2)'),
       ('4.5', '4.5', 'Excellent level (1st class)')]

G = {
    '1.1': 'scope: honours degrees, Greece and Rome, Byzantium and the Greek-speaking world; a wide, interdisciplinary field',
    '1.2': 'courses differ in focus but share the classical past as their centre',
    '1.3': 'three principles: general, flexible and diverse',
    '1.4': 'the classical world shaped modern cultures, education and ideas, and needs critical reflection',
    '1.5': 'purposes: humanities study for its own sake, personal growth and engaged citizens',
    '1.6': 'a wide platform of transferable skills; a way into many modern disciplines',
    '1.7': 'the breadth of opportunities the subject offers',
    '1.8': 'opportunity: history and its source skills',
    '1.9': 'opportunity: ancient and modern languages and linguistics',
    '1.10': 'opportunity: literature, expression and fragmentary texts',
    '1.11': 'opportunity: philosophy, logic and ethics',
    '1.12': 'opportunity: art, archaeology and material evidence',
    '1.13': 'characteristics of honours graduates: subject-specific knowledge and skills',
    '1.14': 'cognitive attributes the subject fosters',
    '1.15': 'specific abilities behind those qualities of mind',
    '1.16': 'practical capacities, from presenting to placements',
    '1.17': 'employers value the breadth and flexibility of these graduates',
    '1.18': 'kinds of work that prize the subject-specific qualities',
    '1.19': "some careers need a master's qualification",
    '1.20': 'courses teach critical handling of material, written and digital evidence',
    '1.21': 'Greek and Roman societies linked with each other and with wider cultures',
    '1.22': 'facing the subject\'s reputation for elitism and its colonial and racial history',
    '1.23': 'reducing elitism through inclusive teaching and curriculum material',
    '1.24': 'examples: diverse reading lists, decolonising approaches, global reach',
    '1.25': 'equal access through inclusive design and adjustments',
    '1.26': 'the subject offers much to education on sustainability',
    '1.27': 'three principles behind its engagement with sustainability',
    '1.28': 'ancient evidence and four of the UN goals; competences matter more than content',
    '1.29': 'four UNESCO competences where the subject is strong',
    '1.30': 'employability and entrepreneurship have grown in importance',
    '1.31': 'enterprise skills are built into the curriculum though not labelled so',
    '2.1': 'design: balanced modules, choice, core and optional modules, language learning, assessment choice',
    '2.2': 'students arrive with varied backgrounds and routes into the subject',
    '2.3': 'blended teaching, unequal engagement and accessible practice',
    '2.4': 'progression from any starting point; core and optional modules; inclusive peer groups',
    '2.5': 'independent research culminating in a dissertation',
    '2.6': 'year-on-year progress to the threshold; readiness for postgraduate study',
    '2.7': 'joint honours students reach the core skills and add others',
    '2.8': 'exit awards and the four-year Scottish honours degree',
    '2.9': 'flexible entry, low-risk options and pathways for non-traditional students',
    '2.10': 'flexible delivery from in person to fully online',
    '2.11': 'partnerships with associations, the British Schools and learned societies',
    '2.12': 'schools outreach, museums, heritage and digital humanities partners',
    '2.13': 'monitoring and periodic review',
    '2.14': 'external reviewers in periodic review',
    '2.15': 'external examiners and threshold standards',
    '2.16': 'review keeps courses current and engaged with equality issues',
    '3.1': 'content varies; the ancient Mediterranean from Bronze Age to Late Antiquity',
    '3.2': 'what Byzantine Studies and Modern Greek each cover',
    '3.3': 'reception and the history of the discipline itself',
    '3.4': 'sensitive and challenging topics and how teaching treats them',
    '3.5': 'the main honours routes and how students combine them',
    '3.6': 'Classics: both ancient languages required',
    '3.7': 'Ancient Greek and Latin as single-language courses',
    '3.8': 'Classical Studies or Civilisation: the whole culture, languages optional',
    '3.9': 'Ancient History: political, social and economic history and its methods',
    '3.10': 'Classical Archaeology: material culture, art and scientific methods',
    '3.11': 'Late Antique and Byzantine Studies',
    '3.12': 'Modern Greek: language proficiency and the later Greek world',
    '3.13': 'teaching starts from where each student begins',
    '3.14': 'skills training, learning communities and transition support',
    '3.15': 'room to specialise and to try new fields late or early',
    '3.16': 'adjusting the mode of delivery for engagement and adjustments',
    '3.17': 'the range of teaching and learning modes a graduate meets',
    '3.18': 'field-specific arrangements: Modern Greek speaking and year abroad; site and museum contact',
    '3.19': 'extracurricular routes to transferable skills',
    '3.20': 'language learning at any stage and language pathways',
    '3.21': 'art, field archaeology and museum training, with adjustments',
    '3.22': 'varied assessment and three guiding principles',
    '3.23': 'assessing cognitive attributes through the same tasks',
    '3.24': 'assessment allows autonomy, reflection and judgement to show',
    '3.25': 'assessing practical skills, mostly formative',
    '3.26': 'the forms summative assessment takes',
    '3.27': 'variety and choice in assessment',
    '4.1': 'the threshold standards and how graduates differ',
    '4.2': 'most students exceed the threshold; Annex D for degree classes',
    '4.3': 'threshold rung: third class',
    '4.4': 'typical rung: 2:1 or 2:2',
    '4.5': 'excellent rung: first class',
}

CTYPE = {'1.8': 'area', '1.9': 'area', '1.10': 'area', '1.11': 'area', '1.12': 'area', '3.1': 'area', '3.2': 'area', '3.3': 'area',
         '3.6': 'area', '3.7': 'area', '3.8': 'area', '3.9': 'area', '3.10': 'area', '3.11': 'area', '3.12': 'area',
         '2.5': 'practice', '2.10': 'practice', '3.16': 'practice', '3.17': 'practice', '3.18': 'practice', '3.20': 'practice', '3.21': 'practice',
         '3.22': 'practice', '3.23': 'practice', '3.25': 'practice', '3.26': 'practice', '3.27': 'practice'}

EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='Contents', kind='other: contents list'),
    dict(number='1 to 4', heading='section heading lines', kind='other: headings, recorded in S3 as sections'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for SB6'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Classics and Ancient History (including Byzantine Studies and Modern Greek)',
         kind='other: back matter, read for S8 (editions 2000, 2007, 2014, 2019, 2022)'),
]

P = {}
def s(i, **k):
    P[i] = k

# ---- obliging or outcome paragraphs (sections 1 to 4)
s('1.22', type='expectation', rung='none', force='must', level='none', appliesTo='the subject, its departments and the education universities provide',
  addressee='provider', verbs=['engage', 'explain'], about="facing the subject's history of elitism, empire and race", domain='none', award='none',
  para=("Classics and its neighbouring fields have long been seen as elitist and exclusive, a reputation that persists despite recent work to widen "
        "who studies and teaches them and to broaden their scope. The subject must now confront and account for its own past: its ties, positive and "
        "negative, to empire, colonial rule, white supremacy and class are a part of university teaching that cannot be avoided, whether assessed or discussed."),
  prac=("Treat the subject's own history as course content you must address: its connections with empire, colonialism, racial supremacy and class, "
        "good and bad. Decide where this is assessed and where it is opened up for discussion, so that no student leaves without meeting it."),
  ben=('n/a', 'a duty on the subject and its teachers; the student meets its effect through the curriculum'),
  aaw=(f"Describe this as an obligation (must) on the discipline and the teaching universities provide, not an outcome a student is assessed on; it "
       f"sets no level. Cite {CITE}, para 1.22, under its equality, diversity and inclusion heading, and read it with paras 1.23 and 1.24. "
       f"Do not claim it is a legal or regulatory duty, or that it prescribes one way of teaching the topic."),
  aad=("Raise this when a programme team reviews the curriculum for inclusion or a teacher plans how to discuss the reception of Greece and Rome. "
       "Put it to staff as a duty to make the discipline's history part of what is taught. Ask where in the course students meet the links between "
       "Classics, empire and race, and whether that is assessed or discussed; avoid handing this duty to a student or reading the paragraph aloud."))

s('1.23', type='expectation', rung='none', force='describes', level='none', appliesTo='teaching and curriculum in the subject',
  addressee='provider', verbs=['taught', 'achieved', 'addressed', 'acknowledged'], about='inclusive curriculum and teaching against elitism', domain='none', award='none',
  para=("Elitism can show in both the content and the manner of teaching, so work remains to open the subject to wider audiences and make teaching "
        "more inclusive: curriculum material that serves students new to the subject and that features under-represented groups in core teaching. "
        "Teaching can show that the subject's methods use antiquity to explore lasting issues; the ethics of these topics and students' intersecting "
        "identities need to be acknowledged and addressed, especially by linking antiquity with the present."),
  prac=("Design curriculum material for students meeting the subject for the first time and bring under-represented groups into core teaching. Show "
        "that the methods of the subject use antiquity to look at enduring questions, and make room to acknowledge the ethics of the topics and the "
        "ways students' social, economic or political identities may expose them to discrimination."),
  ben=('n/a', 'a duty on the teaching and curriculum; the student meets its effect'),
  aaw=(f"Describe this as a provider expectation on inclusive curriculum and teaching; its obliging words are need to and can, recorded as describes. "
       f"Cite {CITE}, para 1.23, and set it beside paras 1.22, 1.24 and the student-facing items 1.14.b5 and 4.3.b1. Do not claim it fixes "
       f"particular content or applies at a stated level."),
  aad=("Bring this into a programme team's review of core modules, reading lists or induction for students new to the subject. Frame it for staff as "
       "two tasks: material that welcomes beginners and core teaching that features under-represented groups. Ask which core module would change "
       "most if it did both, and how the ethics of a hard topic are opened up; avoid presenting it to a student as something they must do."))

s('1.25', type='requirement', rung='none', force='should', level='none', appliesTo='learning opportunities in the subject',
  addressee='provider', verbs=['offered'], about='equal access by inclusive design and individual adjustments', domain='none', award='none',
  find=FINDS['1.25'],
  para=("An inclusive learning environment plans ahead for learners' varied needs and aims for equal access to education; students should be offered "
        "opportunities that all can reach, through inclusive design wherever it is possible and reasonable individual adjustments where they are needed."),
  prac=("Design learning so that everyone can reach it from the start, and add reasonable individual adjustments only where inclusive design falls short; "
        "plan for varied needs rather than reacting to them."),
  ben=('n/a', 'a duty on the course to offer accessible learning; the student meets its effect'),
  aaw=(f"Describe this as a provider expectation (should) on accessible learning, placed under the equality, diversity and inclusion heading; it "
       f"carries no level. Cite {CITE}, para 1.25, and set it beside the accessibility paragraphs 2.2, 2.3 and 2.10. Do not claim it states a "
       f"statutory equality duty or names the adjustments any student is owed."),
  aad=("Raise this when a programme team plans modules, materials or assessments, or when a teacher considers an adjustment. Frame it for staff as "
       "inclusive design first and individual adjustment second. Ask what in a module still relies on an adjustment that design could remove; avoid "
       "putting the duty to a student or treating adjustments as the whole answer."))

s('2.4', type='requirement', rung='none', force='should', level='none', appliesTo='courses and student-led study groups',
  addressee='provider', verbs=['facilitate', 'taken'], about='progression from any starting point; inclusive student-led groups', domain='none', award=HON,
  para=("Courses support progress whatever a student's starting point, built on the distance from entry to the attributes of an honours graduate: "
        "core modules carry what the award needs, options follow interests, language teaching comes at several levels where possible, and skills "
        "training helps students judge their own skills; peer mentoring and group study help students learn together, and care should be taken that "
        "student-led groups include everyone."),
  prac=("Plan the course around how far each student must travel from entry to graduation: core modules for what the award needs, options for "
        "interests, staged language teaching where you can and skills training with honest feedback on skill levels. Where you run peer mentoring "
        "or student-led groups, make sure they are inclusive."),
  ben=('n/a', 'a design duty on the course, with care for inclusive peer groups; the student meets its effect'),
  aaw=(f"Describe this as a provider expectation on progression design, with one should: that student-led groups be inclusive; it carries no level of "
       f"its own. Cite {CITE}, para 2.4, and set it beside paras 2.6, 3.13 and 3.14. Do not claim it sets entry requirements or that peer schemes are compulsory."),
  aad=("Raise this when a programme team designs core and optional modules, language levels or peer mentoring. Frame it for staff as planning for "
       "different starting points and checking that peer groups do not exclude. Ask how a student with no prior language would progress, and who "
       "checks that student-led groups are inclusive; avoid presenting it to a student as a duty."))

s('2.6', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students on an honours degree in the subject',
  addressee='learner', verbs=['progress', 'meeting'], about='progress year by year towards the threshold and readiness for postgraduate study', domain='none', award=HON,
  para=("Across an honours degree at FHEQ level 6 (FQHEIS level 10), a student will progress from year to year under each institution's rules; each "
        "year is expected to build knowledge, expertise and experience towards meeting the threshold subject-specific and generic skills, and a "
        "graduate is expected to be able and prepared to start postgraduate study in the subject or a related one."),
  prac=("Plan each year so that it adds knowledge, expertise and experience towards the threshold skills in section 4, and so that graduates are ready "
        "to begin postgraduate study in classics, ancient history or a neighbouring discipline."),
  ben=("Each year of your course will build towards the minimum skills an honours degree in the subject asks for, and by the end you are "
       "expected to be ready to go on to postgraduate study in this field or a related one if you choose."),
  aaw=(f"Describe this as an expected outcome (will, with expected) of progression through the honours degree at FHEQ level 6 and FQHEIS level 10. "
       f"Cite {CITE}, para 2.6. Set it beside the threshold list 4.3, the level 6 descriptor qaa/fheq-2024/4.15.b9.3 and spine:6 in std:ref:uk-framework; "
       f"do not claim it fixes what each year must contain or guarantees entry to postgraduate study."),
  aad=("Raise this when a student asks what each year is for or whether the degree prepares them for a master's, or when a team maps progression. "
       "To a student, say plainly that each year builds toward the minimum the degree asks and toward readiness for further study. Ask what the "
       "student can do now that they could not a year ago; avoid treating the threshold as the expected result."))

s('2.7', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='joint honours students in the subject',
  addressee='learner', verbs=['achieve', 'add', 'explore'], about='joint honours reach the core skills and add others', domain='none', award=HON,
  para=("Joint honours students will reach the core of the subject's specific and generic skills and will add others from their second subject, "
        "and may also work in the overlap between the two for further interdisciplinary study."),
  prac=("For joint honours, plan for students to reach the core specific and generic skills of this subject, to gain others from the partner subject "
        "and, where you can, to work across the two."),
  ben=("If you take this subject jointly with another, you will reach its core skills, gain others from your second subject and may get the chance "
       "to explore where the two meet."),
  aaw=(f"Describe this as an expected outcome (will) for joint honours at FHEQ level 6: the core elements of the skills in 1.13 to 1.16 and section 4, "
       f"not all of them. Cite {CITE}, para 2.7, and read it with para 1.3. Do not claim it names which elements count as core; the course decides that."),
  aad=("Raise this when a joint honours student asks which outcomes apply to them, or a team designs a joint route. To a student, explain that they "
       "will reach the core of this subject and gain other skills from their second subject. Ask which skills they expect from each side and where "
       "the two overlap; avoid implying that every list item applies in full."))

s('3.4', type='requirement', rung='none', force='should', level='none', appliesTo='teaching in the subject',
  addressee='provider', verbs=['acknowledge', 'take'], about='teaching sensitive and challenging topics', domain='none', award=HON,
  para=("The subject can bring students into contact with sensitive or difficult topics, such as slavery and violence against particular groups, which "
        "may weigh most on marginalised students who have lived through such things; teaching should recognise the issues the material raises "
        "and allow for how students may react."),
  prac=("When you teach topics such as slavery or violence against groups, name the issues the material raises, expect that some students, above all "
        "those from marginalised groups with lived experience, may react strongly, and plan for that in how you teach."),
  ben=('n/a', 'a duty on teaching; the student meets its effect'),
  aaw=(f"Describe this as an expectation (should) on teaching practice; it sets no level. Cite {CITE}, para 3.4, and set it beside para 3.16 on "
       f"modulating delivery and the equality paragraphs 1.22 to 1.24. Do not claim it restricts what may be taught or requires content warnings in a set form."),
  aad=("Raise this when a teacher plans a session on slavery, violence or other hard material, or a team reviews how such topics are handled. Frame it "
       "for staff as preparing for the material's effect on students. Ask how students are told in advance and what they can do if a session affects "
       "them; avoid placing the duty on a student."))

s('3.6', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='students on courses titled Classics',
  addressee='learner', verbs=['acquire', 'show'], about='proficiency in both ancient Greek and Latin on a Classics course', domain='subject-skill', award=HON,
  para=("A course called Classics generally requires its students to gain and show proficiency in both ancient Greek and Latin, and may make Greek "
        "and Latin literature the main though not the only focus, at least early on."),
  prac=("If the course is titled Classics, require students to become proficient in both ancient Greek and Latin and to show it; you may centre the "
        "early years on the two literatures without making them the only focus."),
  ben=("On a course called Classics you will be required to learn both ancient Greek and Latin and to show that you can use them well."),
  aaw=(f"Describe this as a requirement (required, recorded as must) that defines a course titled Classics, at FHEQ level 6; it does not apply to Classical "
       f"Studies or Ancient History (paras 3.8, 3.9). Cite {CITE}, para 3.6, and set it beside the language item 1.13.b7 and the descriptor qaa/fheq-2024/4.15.b2. "
       f"Do not claim it is a regulatory rule on course titles."),
  aad=("Raise this when a student chooses between Classics, Classical Studies and Ancient History, or a team names a course. To a student, say plainly "
       "that Classics means learning both ancient languages. Ask which language the student has started and how they plan to reach the other; "
       "avoid suggesting the same holds for every course in the subject."))

s('3.12', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='students on Modern Greek courses',
  addressee='learner', verbs=['require', 'take'], about='proficiency in the modern Greek language', domain='subject-skill', award=HON, find=FINDS['3.12'],
  para=("Modern Greek courses require proficiency in the modern language and centre on the writing, ideas, language and past of the "
        "Greek-speaking world from the later Middle Ages onwards."),
  prac=("Build the course so that students become proficient in modern Greek and study the language, writing, ideas and past of the Greek-speaking "
        "world since the late medieval period."),
  ben=("On a Modern Greek course you will be required to become proficient in the language, and you will study the writing, ideas and history of "
       "the Greek-speaking world from the later Middle Ages to now."),
  aaw=(f"Describe this as a requirement (require, recorded as must) that defines a Modern Greek course at FHEQ level 6. Cite {CITE}, para 3.12, and set it "
       f"beside para 3.18 on speaking practice, item 1.13.b7 and the descriptor qaa/fheq-2024/4.15.b2. Do not claim it sets a named proficiency level, "
       f"which the text does not give."),
  aad=("Raise this when a student considers Modern Greek or a team plans its language teaching. To a student, explain that proficiency in the language "
       "is part of the course; to staff, connect it to regular speaking practice. Ask how much speaking practice the student gets each week; avoid "
       "naming a proficiency scale the text does not state."))

s('3.17', type='expectation', rung='none', force='will', level='none', appliesTo='honours graduates and the courses they take',
  addressee='both', verbs=['experience'], about='the range of teaching and learning modes a graduate meets', domain='none', award=HON, find=FINDS['3.17'],
  para=("An honours graduate in the subject will usually have had the chance to meet all or most of a listed range of teaching and learning modes, "
        "from essays, language and source exercises, seminars and lectures to group projects, placements, field and museum work, digital production, "
        "examinations and a dissertation."),
  prac=("Offer most of the listed modes across the course: essays, source, commentary and translation exercises, digital tools, seminars and "
        "lectures, one-to-one contact, group projects, work-based learning, reports, media analysis, work with objects in the field or museums, "
        "podcasts and blogs, exam revision and a dissertation."),
  ben=("Over your course you will usually get the chance to try most of these ways of learning: essays, translation and source exercises, seminars, "
       "lectures, group projects, placements, work with objects, podcasts or blogs, exams and a dissertation."),
  aaw=(f"Describe this as an expectation (will, softened by generally) that graduates have met all or most of a range of teaching and learning modes; "
       f"the list items are recorded as S3 practice, not as statements. Cite {CITE}, para 3.17, and set it beside paras 3.18 and 3.26. Do not claim "
       f"every listed mode is required or that it sets a level."),
  aad=("Raise this when a student asks what kinds of teaching to expect, or a team checks the spread of modes across the course. To a student, describe "
       "the range in plain words; to staff, frame it as coverage across years. Ask which modes the student has not met yet; avoid reading the whole "
       "list aloud or treating each mode as compulsory."))

s('3.20', type='requirement', rung='none', force='should', level='none', appliesTo='courses offering ancient and later languages',
  addressee='provider', verbs=['given', 'put'], about='language learning at any stage through language pathways', domain='none', award=HON, find=FINDS['3.20'],
  para=("Where possible, students who want to should get the chance and encouragement to learn or improve Greek, Latin or another ancient Mediterranean "
        "language at any point in the degree. Unequal access before university calls for several language pathways and, where fitting, support towards "
        "comparable attainment by graduation, and arrangements should let students start language modules later in the course. Such study helps other "
        "skills and is a base for research degrees and an asset for master's study."),
  prac=("Run more than one language pathway so that students with and without prior study can reach comparable attainment, give support where needed, "
        "and arrange things so that a student can begin or resume a language module later in the course, not only in the first year."),
  ben=('n/a', 'a duty on the course to offer language pathways; the student meets its effect'),
  aaw=(f"Describe this as a provider expectation (should) on language provision, with the stronger words highly desirable and requires for pathways; it "
       f"states no level. Cite {CITE}, para 3.20, and set it beside paras 2.4, 2.9, 3.6 and item 1.13.b7. Do not claim every course must teach ancient "
       f"languages; para 3.9 says Ancient History need not."),
  aad=("Raise this when a student without Latin or Greek asks whether they can still learn one, or a team plans language pathways. Frame it for staff as "
       "routes for different starting points and a way in later in the course. Ask at what point a second-year student could start a language; avoid "
       "placing the duty on the student."))

s('3.21', type='requirement', rung='none', force='will', level='none', appliesTo='art, field archaeology and museum training in the subject',
  addressee='provider', verbs=['made'], about='training with objects and sites, with adjustments', domain='none', award=HON, find=FINDS['3.21'],
  para=("Training in Greek, Roman or Byzantine art, in fieldwork or in museum-based study of artefacts adds further skills; students may start it early or, "
        "where that was not possible, be offered it near the end of the course, and museum, gallery or field placements may be made available. Direct work "
        "with landscapes and objects builds skills for many jobs, and reasonable adjustments will be made for any such activity."),
  prac=("Where you offer art, field or museum training, consider a late entry point for students who missed it, open placements where you can, and "
        "make reasonable adjustments for every such activity, from site surveys to drawing and recording."),
  ben=('n/a', 'a duty on the course to make adjustments for practical training; the student meets its effect'),
  aaw=(f"Describe this as a provider commitment (will) that practical training with objects and sites comes with reasonable adjustments; the rest of the "
       f"paragraph is permissive (may). Cite {CITE}, para 3.21, and set it beside para 3.18, item 1.16.b7 and the accessibility paragraph 2.3. Do not "
       f"claim fieldwork or museum work is required of every student."),
  aad=("Raise this when a student asks about fieldwork, museum work or placements, or needs an adjustment to take part. Frame it for staff as access to "
       "practical training. Ask which adjustment would let the student take part and whether a later entry point exists; avoid giving the duty to the "
       "student or promising placements the text leaves to the course."))

s('3.24', type='requirement', rung='none', force='should', level='none', appliesTo='assessment in the subject',
  addressee='provider', verbs=['enable', 'demonstrate'], about='assessment that lets autonomy, reflection and judgement show', domain='none', award=HON, find=FINDS['3.24'],
  para=("Assessment should let students show a range of attributes, above all autonomy, critical reflection and critical judgement."),
  prac=("Design assessments that give students room to show independence, critical reflection and critical judgement, not only recall."),
  ben=('n/a', 'a duty on assessment design; the student meets its effect'),
  aaw=(f"Describe this as an expectation (should) on assessment design; it sets no level. Cite {CITE}, para 3.24, and set it beside items 1.14.b1 to "
       f"1.14.b3 and the Annex D cell qaa/fheq-2024/annex-d/transferable/r5/3rd. Do not claim it prescribes particular assessment methods."),
  aad=("Raise this when a programme team reviews assessments or a validation panel asks how cognitive attributes are tested. Frame it for staff as room "
       "for independence, reflection and judgement in each task. Ask which assessment lets a student show judgement rather than knowledge alone; "
       "avoid giving it to a student as their duty."))

s('4.2', type='requirement', rung='none', force='should', level='fheq:6', appliesTo='honours degree-awarding providers',
  addressee='provider', verbs=['perform', 'refer'], about='using Annex D above the threshold', domain='none', award=HON, find=FINDS['4.2'],
  para=("Most students will do well above the minimum threshold; each provider decides how to evidence this and should refer to Annex D, which describes "
        "the four honours classes (1st, 2:1, 2:2, 3rd) at FHEQ level 6 and FQHEIS level 10."),
  prac=("Judge performance above the threshold by your own method and refer to Annex D's outcome classification descriptions; read them with the typical "
        "and excellent lists in 4.4 and 4.5."),
  ben=('n/a', 'a duty on the awarding body for judging classes above the threshold'),
  aaw=(f"Describe this as a provider expectation (should) to use Annex D for performance above the threshold at FHEQ level 6 and FQHEIS level 10. "
       f"Cite {CITE}, para 4.2, and point to std:doc:qaa-fheq-2024-framework, Annex D (SL6), for example qaa/fheq-2024/annex-d/summary/r1/3rd. "
       f"Do not claim Annex D replaces the subject's own rung lists in 4.3 to 4.5."),
  aad=("Raise this when a team or student asks what separates the degree classes. To staff, explain that the subject lists sit beside Annex D's "
       "descriptions; to a student, say that most people do much better than the minimum. Ask which Annex D descriptions the marking criteria follow; "
       "avoid presenting the threshold as the expected result."))

# ---- section 1 outcome lists: 1.13 characteristics of graduates; 1.14 cognitive attributes; 1.15 specific abilities; 1.16 practical capacities
LISTS = {
    '1.13': ("a subject-specific characteristic of honours graduates, which the course is designed to produce (some or all of the list; not exhaustive)",
             'subject-specific characteristic'),
    '1.14': ("a cognitive attribute that study in the subject fosters in honours graduates", 'cognitive attribute'),
    '1.15': ("one of the specific abilities that the subject's qualities of mind rest on", 'specific ability'),
    '1.16': ("one of the practical capacities an honours graduate in the subject has", 'practical capacity'),
}
AAWL = ("Describe this as {what}; the lead-in has no modal, so it is a description of the graduate (force describes), not a threshold, at FHEQ level 6 "
        "for the honours degree: {about}. Cite " + CITE + ", para {stem} (bullet {k}). Set it beside {nb} and the level 6 descriptor {fw}; do not "
        "claim it is a pass requirement, which section 4 holds, or that every course covers it.")
AADL = ("Raise this when {when}. To a student, put it plainly in the second person as something the course helps them build; to staff, frame it "
        "as a {kind} to make visible in modules and assessment. Ask {q} Avoid reading the list aloud or turning the item into a separate hurdle.")
def kl(stem, k, verbs, about, domain, para, prac, ben, nb, fw, when, q, find=None):
    what, kind = LISTS[stem]
    r = dict(type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='honours graduates of the subject',
             addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
             aaw=AAWL.format(what=what, about=about, stem=stem, k=k, nb=nb, fw=fw), aad=AADL.format(when=when, kind=kind, q=q))
    if find:
        r['find'] = find
    P['%s.b%d' % (stem, k)] = r

KN, UN, SK, GS = 'knowledge', 'understanding', 'subject-skill', 'generic-skill'

# 1.13
kl('1.13', 1, [], 'understanding another culture and how it differs from ours', UN,
   "Understands a culture other than one's own, through its literature, thought and religion, its history and politics or its art and material remains; engages critically with it and has an informed sense of how it resembles and differs from modern cultures.",
   "Graduates understand another culture through its texts, ideas, history or material remains, engage with it critically and can compare it, with evidence, to modern cultures.",
   "You will understand another culture, through its writing, ideas, history or objects, think critically about it and see how it compares with cultures today.",
   '4.3.b1, 4.4.b1 and 4.5.b1', 'qaa/fheq-2024/4.15.b1', 'a student asks what the course is really about or how ancient study bears on the present',
   'which feature of an ancient culture surprised the student most, and what modern assumption it challenged?')
kl('1.13', 2, [], 'broad, coherent knowledge across complementary fields and themes', KN,
   "Has a broad, coherently framed knowledge of related fields, such as language, literature, philosophy, history, art and archaeology, or of themes that cross them and cross periods, such as environment, gender, race or religion.",
   "Graduates hold a broad, well-organised knowledge of complementary fields or cross-cutting themes, drawn from language, literature, linguistics, philosophy, history, art and archaeology.",
   "You will build a broad, joined-up knowledge of several related fields, such as languages, literature, philosophy, history or archaeology, or of themes like gender or religion that run across them.",
   '1.13.b3 and 4.3.b2', 'qaa/fheq-2024/4.15.b1', 'a student chooses options or wonders how separate modules fit together',
   'which theme links two of the student\'s modules, and what each adds to it?')
kl('1.13', 3, [], 'familiarity with a diverse range of primary materials', KN,
   "Knows and is at ease with a suitably wide range of primary material, from literary, historical and philosophical texts to art objects, archaeological finds, inscriptions and papyri.",
   "Graduates know and are familiar with a fitting, varied range of primary sources: texts, objects, archaeological evidence, inscriptions and papyri.",
   "You will get to know a wide range of original sources, from texts of many kinds to objects, archaeological finds, inscriptions and papyri.",
   '4.3.b2, 4.4.b2 and 4.5.b2', 'qaa/fheq-2024/4.15.b5', 'a student first works directly with inscriptions, papyri or objects',
   'which kind of primary source the student has not yet handled, and how they would approach it?')
kl('1.13', 4, [], 'command of research, textual, historical, digital and language techniques', SK,
   "Commands a range of methods, some or all of: library and bibliographic research, close reading and textual analysis, historical methods for statements and fragmentary evidence, digital humanities and databases, visual analysis, statistics, philosophical argument, analysis of language and translation to or from ancient and modern languages.",
   "Graduates command a selection of the subject's methods: research and bibliography, textual and historical analysis, digital humanities, visual and statistical skills, philosophical argument and translation.",
   "You will learn to use a range of the subject's methods, such as library research, close reading, handling fragmentary evidence, databases and digital tools, visual analysis, statistics, argument and translation.",
   '4.4.b7 and 4.3.b4', 'qaa/fheq-2024/4.15.b2', 'a student plans a project and must choose methods',
   'which two methods the student would combine for their topic, and why those?')
kl('1.13', 5, [], 'viewpoints on interpretation and a variety of critical approaches', UN,
   "Understands a range of positions on questions of interpretation and evaluation and can take various critical approaches to them from across the subject.",
   "Graduates understand differing positions on interpretation and evaluation and can apply several critical approaches from across the subject.",
   "You will understand different views on how to interpret and judge evidence, and be able to use several critical approaches from across the subject.",
   '4.3.b3, 4.4.b3 and 4.5.b3', 'qaa/fheq-2024/4.15.b4', 'a student meets conflicting scholarly readings of the same source',
   'which reading the student finds most persuasive, and what a rival approach would say about it?')
kl('1.13', 6, [], 'independence to research, argue and present', SK,
   "Has the intellectual independence to research classical topics, build clear arguments on them and present results clearly in speech and writing.",
   "Graduates are independent enough to research classical topics, argue clearly from them and present findings well orally and in writing.",
   "You will become independent enough to research a classical topic yourself, build a clear argument and present it well in speech and in writing.",
   '4.3.b4, 4.4.b4 and 4.5.b4', 'qaa/fheq-2024/4.15.b6', 'a student starts a dissertation or independent essay',
   'what the student\'s research question is, and how they will present the answer?')
kl('1.13', 7, [], 'analytical command of one or more ancient or modern languages', SK,
   "Can understand, read and write one or more ancient or modern languages, perhaps also speaking and listening, with analytical knowledge: secure grammar, wide vocabulary and idiom, a feel for register and the skills of translation.",
   "Graduates have an analytical command of one or more ancient and modern languages: grammar, vocabulary, idiom, register and translation, with speaking and listening where relevant.",
   "You will gain an analytical command of at least one ancient or modern language: its grammar, vocabulary, idioms, tone and translation, with speaking and listening where the language allows.",
   'paras 3.6, 3.12 and 3.20', 'qaa/fheq-2024/4.15.b2', 'a student asks how far their language study should go or a team plans language assessment',
   'which part of the language, grammar, vocabulary or register, the student finds hardest to translate?', find=FINDS['1.13.b7'])

# 1.14
kl('1.14', 1, [], 'autonomy and self-direction in study and time', GS,
   "Shows considerable autonomy: self-direction and intellectual initiative in learning and study and in managing the time given to them.",
   "Graduates show marked autonomy, directing their own learning, taking intellectual initiative and managing their study time.",
   "You will become largely self-directed, taking the lead in your own learning and managing your study time.",
   '4.3.b7, 4.4.b8 and 4.5.b9', 'qaa/fheq-2024/4.15.b9.1', 'a student moves from taught classes to independent work',
   'what the student now decides for themselves that a tutor once decided?')
kl('1.14', 2, [], 'critical reflection on one\'s own learning', GS,
   "Can reflect critically on the reach and the limits of what and how one has learned and understood.",
   "Graduates reflect critically on the scope and limits of their own learning and understanding.",
   "You will be able to look critically at what you have learned and how, including where your understanding stops.",
   '4.3.b7 and 3.24', 'qaa/fheq-2024/4.15.b4', 'feedback is returned or a student writes a reflective piece',
   'where the student\'s understanding of a topic ran out, and how they noticed?')
kl('1.14', 3, [], 'critical judgement from evidence and argument', GS,
   "Can judge critically on the strength of evidence and argument.",
   "Graduates exercise critical judgement grounded in evidence and argument.",
   "You will be able to reach critical judgements based on evidence and argument.",
   '4.3.b5, 4.4.b5 and 4.5.b5', 'qaa/fheq-2024/4.15.b7', 'a student must decide between competing interpretations',
   'what evidence would change the student\'s judgement on their current topic?')
kl('1.14', 4, [], 'creativity in developing and communicating ideas', GS,
   "Is creative both in forming ideas and arguments and in putting them across.",
   "Graduates show creativity in developing ideas and arguments and in communicating them.",
   "You will be able to be creative in how you develop ideas and arguments and how you share them.",
   '4.5.b8', 'qaa/fheq-2024/4.15.b3.1', 'a student considers a creative assessment or an unusual argument',
   'which idea of the student\'s own they would most like to develop further?')
kl('1.14', 5, [], 'empathy through the lens of antiquity', GS,
   "Can empathise with people whose circumstances differ from one's own, an empathy that looking through antiquity can foster.",
   "Graduates show empathy with people in circumstances unlike their own, built by viewing others through antiquity.",
   "You will learn to understand and feel for people whose lives differ from yours, using the ancient world as a way of seeing them.",
   '4.3.b1 and 4.3.b9', 'qaa/fheq-2024/4.15.b4', 'a seminar turns to slavery, migration or other lives far from the student\'s own',
   'whose experience in the ancient world the student found hardest to imagine, and why?')
kl('1.14', 6, [], 'historical perspective on current issues', GS,
   "Understands more deeply, through historical perspective, the complex past and present urgency of a range of current issues.",
   "Graduates understand current issues more deeply, seeing their complex history and continuing urgency in historical perspective.",
   "You will understand today's issues more deeply by seeing their long and complex history.",
   'paras 1.23 and 1.29', 'qaa/fheq-2024/4.15.b3.2', 'a seminar or project connects antiquity with a present-day debate',
   'which current issue the student now sees differently because of something ancient?')
kl('1.14', 7, [], 'openness to interdisciplinarity and new methods', GS,
   "Is open to working across disciplines, to drawing on many sources and to new methods.",
   "Graduates are open to interdisciplinary work, eclectic sources and new methods.",
   "You will be open to working across subjects, drawing on varied ideas and trying new methods.",
   '1.15.b6 and 1.13.b2', 'qaa/fheq-2024/4.15.b9.2', 'a student is wary of a method from outside their usual field',
   'which method from another discipline the student would like to try?')

# 1.15
kl('1.15', 1, ['gather', 'organise', 'deploy', 'show'], 'handling evidence and the effects of its absence', GS,
   "Collects, remembers, orders and uses evidence and information and recognises what follows when evidence is missing.",
   "Graduates gather, retain, organise and deploy evidence and are aware of what the gaps in evidence mean.",
   "You will be able to collect, remember, organise and use evidence and see what it means when evidence is missing.",
   '4.3.b2 and 1.13.b4', 'qaa/fheq-2024/4.15.b7', 'a student builds an argument on patchy ancient evidence',
   'what the student\'s argument would look like if one key source were lost?')
kl('1.15', 2, ['extract', 'identify', 'solve'], 'drawing key points from complex information and solving problems', GS,
   "Pulls the essential points out of complex information and recognises and solves the problems that follow.",
   "Graduates extract the essentials from complex information and identify and solve the problems it raises.",
   "You will be able to pick out what matters in complex information and spot and solve the problems it raises.",
   '4.4.b7 and 4.5.b7', 'qaa/fheq-2024/4.15.b9.2', 'a student is overwhelmed by a large body of material',
   'what the three key points of the student\'s material are, and what problem they raise?')
kl('1.15', 3, ['select', 'apply'], 'choosing methods to judge meaning and significance', GS,
   "Chooses and uses suitable methods to assess what information means and why it matters.",
   "Graduates select and apply fitting methods to assess the meaning and significance of information.",
   "You will be able to choose and use the right methods to work out what information means and why it matters.",
   '1.13.b4 and 4.4.b7', 'qaa/fheq-2024/4.15.b2', 'a student plans how to analyse a source or dataset',
   'why the student chose their method, and what it cannot show?')
kl('1.15', 4, ['engage'], 'analytical and evaluative thinking about texts, evidence and arguments', GS,
   "Thinks analytically and evaluatively about texts, evidence, arguments and readings, judging their relevance unaided, choosing between rival theories and reaching judgements from evidence and argument.",
   "Graduates analyse and evaluate texts, evidence, arguments and interpretations, weigh relevance independently, discriminate between theories and judge from evidence.",
   "You will be able to analyse and weigh up texts, evidence and arguments, decide for yourself what is relevant, choose between competing theories and reach your own judgements.",
   '4.3.b5, 4.4.b5 and 4.5.b5', 'qaa/fheq-2024/4.15.b7', 'a student reviews scholarship or compares theories',
   'which theory the student rejected, and on what evidence?')
kl('1.15', 5, ['evaluate'], 'critical evaluation of digital resources on the ancient world', GS,
   "Assesses critically how useful digital resources are for the study of antiquity and how they shape it.",
   "Graduates critically evaluate the usefulness and the influence of digital resources on the study of the ancient world.",
   "You will be able to judge critically how useful digital resources are for studying the ancient world, and how they shape what you find.",
   '4.3.b10 and 1.16.b5', 'qaa/fheq-2024/4.15.b4', 'a student relies on an online database, digitised text or image collection',
   'what the digital resource the student used leaves out, and how they would check it?')
kl('1.15', 6, ['engage'], 'lateral thinking across fields', GS,
   "Thinks laterally, linking ideas and information creatively across different fields of study.",
   "Graduates engage in lateral thinking, making creative links between ideas and information from different fields.",
   "You will be able to think sideways, making creative links between ideas from different fields.",
   '1.14.b7 and 4.5.b8', 'qaa/fheq-2024/4.15.b3.1', 'a student is stuck on a problem within one field',
   'what an idea from another of the student\'s modules would add to their problem?')
kl('1.15', 7, ['marshal'], 'clear, coherent and concise argument in speech and writing', GS,
   "Marshals arguments clearly, coherently and briefly, in speech and in writing.",
   "Graduates marshal arguments with clarity, coherence and concision, orally and in writing.",
   "You will be able to put arguments together clearly, coherently and concisely, in speech and in writing.",
   '4.3.b4, 4.4.b4 and 4.5.b4', 'qaa/fheq-2024/4.15.b8', 'a student plans an essay or presentation',
   'how the student would state their argument in two sentences?')
kl('1.15', 8, ['display'], 'critical appreciation of literature, art and other evidence', GS,
   "Shows critical appreciation and judgement of literature and art and of other written and material evidence.",
   "Graduates display critical appreciation and judgement of literature, art and other written and material evidence.",
   "You will be able to appreciate and judge literature, art and other written and material evidence critically.",
   '1.13.b3 and 4.3.b2', 'qaa/fheq-2024/4.15.b7', 'a student writes on a poem, a sculpture or an inscription',
   'what makes the work the student is discussing effective, and what limits it?')

# 1.16
kl('1.16', 1, ['present', 'relating', 'making'], 'clear oral presentation for an audience, with adjustments', GS,
   "Presents material orally, clearly and effectively, with audio-visual aids where useful, linked to the audience's concerns, with reasonable adjustments where needed.",
   "Graduates present orally with clarity and effect, using aids where apt, addressing the audience's concerns and making reasonable adjustments.",
   "You will be able to give a clear, effective talk, using visual or audio aids where they help, shaped for your audience, with adjustments where needed.",
   '4.3.b4 and 4.4.b4', 'qaa/fheq-2024/4.15.b8', 'a student prepares an assessed presentation',
   'who the student\'s audience is and what they need from the talk?')
kl('1.16', 2, ['present'], 'clear written presentation, referencing and layout', GS,
   "Presents material in writing with discernment and clarity of language, professional referencing and a clear, effective layout, including tables, diagrams or photographs where fitting.",
   "Graduates present written material with discerning, lucid language, professional referencing and clear layout, using tables, diagrams or images where apt.",
   "You will be able to write clearly and with care, reference sources properly and lay out your work well, with tables, diagrams or images where they help.",
   '4.3.b6, 4.4.b6 and 4.5.b6', 'qaa/fheq-2024/4.15.b8', 'feedback on writing, referencing or presentation comes back',
   'which part of the student\'s written work, language, referencing or layout, most needs attention?')
kl('1.16', 3, ['work'], 'creative, flexible work alone and with others', GS,
   "Works creatively and adaptably, both alone and with others.",
   "Graduates work creatively and flexibly, independently and collaboratively.",
   "You will be able to work creatively and adapt, both on your own and with other people.",
   '4.3.b8, 4.4.b9 and 4.5.b10', 'qaa/fheq-2024/annex-d/transferable/r2/3rd', 'a student meets a group project',
   'what role the student took in their last group task and what they would change?')
kl('1.16', 4, ['organise', 'conduct', 'write', 'think', 'meet'], 'organising work, studying alone, working under pressure and meeting deadlines', GS,
   "Organises their own work, studies independently, writes and thinks under pressure and meets deadlines.",
   "Graduates organise their work, study independently, write and think under pressure and meet deadlines.",
   "You will be able to organise your own work, study on your own, write and think under pressure and hit deadlines.",
   '4.3.b7, 4.4.b8 and 4.5.b9', 'qaa/fheq-2024/annex-d/transferable/r3/3rd', 'a student juggles several deadlines or prepares for timed assessment',
   'how the student plans the week before a deadline?')
kl('1.16', 5, ['make', 'collect', 'evaluate', 'organise', 'present', 'employ'], 'effective use of digital resources at every stage', GS,
   "Uses digital resources and information technology well and fittingly throughout their work: collecting and assessing digitised data, using electronic texts and databases, virtual learning environments, presenting arguments, text and images digitally, communicating in varied formats and following safety and security practice.",
   "Graduates use digital resources and IT effectively at every stage: digitised data, electronic texts and databases, virtual learning environments, digital presentation, varied media and safe, secure practice.",
   "You will be able to use digital tools well at every stage of your work: finding and judging digital data, using online texts and databases, presenting your work digitally and keeping safe and secure online.",
   '4.3.b10, 4.4.b11 and 4.5.b12', 'qaa/fheq-2024/annex-d/transferable/r1/3rd', 'a student chooses tools for research or for presenting work',
   'which digital tool the student relies on most and how they check what it gives them?')
kl('1.16', 6, ['cope', 'read', 'interpret'], 'reading sources critically with regard to provenance', GS,
   "Meets central challenges of the modern world by reading a wide range of sources critically, minding their provenance, and by interpreting and synthesising them while taking nothing for granted.",
   "Graduates read many sources critically with attention to provenance, interpret and synthesise them and question what they are told.",
   "You will be able to read many kinds of sources critically, ask where they come from and pull them together without taking anything on trust.",
   '1.15.b1 and 4.3.b2', 'qaa/fheq-2024/4.15.b5', 'a student meets a source of uncertain origin, ancient or modern',
   'where the student\'s last source came from and how that affects its value?')
kl('1.16', 7, ['function'], 'working in vocational settings through placements', GS,
   "Can operate in a range of work settings, through placements with organisations such as charities, galleries, museums, archaeological companies, libraries and archives within the course.",
   "Graduates function in varied vocational settings, through course placements with charities, galleries, museums, archaeological companies, libraries or archives.",
   "You will be able to work in a range of settings, through placements with organisations such as museums, galleries, charities, archaeology firms, libraries or archives.",
   'paras 2.12 and 3.21', 'qaa/fheq-2024/4.15.b9.1', 'careers, placements or employability come up',
   'which kind of organisation the student would like a placement with and what they would bring?')

# ---- section 4 rungs: 4.3 threshold (third class), 4.4 typical (2:1 or 2:2), 4.5 excellent (first class)
# lead-ins: "Honours graduates of a ... level of attainment ... will have demonstrated ... Evidence of proficiency will have been provided if, for example, a graduate has ... demonstrated an ability to:"
RUNG = {
    'threshold': dict(stem='4.3', cls='third class', ad='3rd', word='a threshold standard: the least an honours graduate (third class) will have shown',
                      student="part of the minimum you will need to show by graduation for an honours degree",
                      staff="a threshold every assessment route must let a student show"),
    'typical': dict(stem='4.4', cls='2:1 or 2:2', ad='2', word='a typical-level standard: what an honours graduate at 2:1 or 2:2 will have shown, above the threshold',
                    student="what a good, typical honours result (a 2:1 or 2:2) looks like, not the minimum",
                    staff="the typical level your marking criteria for 2:1 and 2:2 should recognise"),
    'excellent': dict(stem='4.5', cls='first class', ad='1st', word='an excellent-level standard: what a first-class honours graduate will have shown',
                      student="what a first-class result looks like, an aspiration well above the minimum",
                      staff="the excellent level your first-class criteria should recognise"),
}
AAWR = ("Describe this as {word}, at FHEQ level 6 (FQHEIS level 10) for the bachelor's degree with honours; it concerns {about}, and the issuer offers "
        "the list as examples of evidence. Cite " + CITE + ", para {stem} (bullet {k}). Set it beside {nb}, the level 6 descriptor {fw} and the "
        "Annex D cell {adid}; do not claim it is a regulatory rule or a standard at another level.")
AADR = ("Raise this when {when}. To a student, put it plainly in the second person as {student}; to staff, frame it as {staff}. Ask {q} Avoid "
        "reading the list aloud{avoid}.")
AVOID = {'threshold': ' or treating this minimum as the result most students reach',
         'typical': ' or presenting this typical level as the minimum to pass',
         'excellent': ' or presenting this first-class level as the minimum or the norm'}
def kr(rung, k, verbs, about, domain, para, prac, ben, nb, fw, adrow, when, q, find=None, after=None):
    R = RUNG[rung]
    r = dict(type=rung, rung=rung, force='will', level='fheq:6', appliesTo='honours graduates in the subject (%s)' % R['cls'],
             addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
             aaw=AAWR.format(word=R['word'], about=about, stem=R['stem'], k=k, nb=nb, fw=fw, adid='qaa/fheq-2024/annex-d/%s/%s' % (adrow, R['ad'])),
             aad=AADR.format(when=when, student=R['student'], staff=R['staff'], q=q, avoid=AVOID[rung]))
    if find:
        r['find'] = find
    if after:
        r['after'] = after
    P['%s.b%d' % (R['stem'], k)] = r

# threshold 4.3
kr('threshold', 1, ['understand'], 'key features of another culture and cultural difference', UN,
   "Understands the main features of another culture and is alert to cultural difference.",
   "At threshold, graduates grasp the chief features of another culture and show sensitivity to difference between cultures.",
   "By graduation you will have shown that you understand the main features of another culture and are alert to how cultures differ.",
   '4.4.b1 and 1.13.b1', 'qaa/fheq-2024/4.15.b1', 'knowledge/r2', 'a student asks what the minimum is in knowing the ancient world',
   'which feature of the culture the student studies they could explain to a newcomer?')
kr('threshold', 2, ['demonstrate', 'used'], 'familiarity with written and material sources and combining evidence', KN,
   "Knows a range of textual and material sources and understands how to use them together with other kinds of evidence.",
   "At threshold, graduates know a range of textual and material sources and understand how they combine with other evidence.",
   "By graduation you will have shown that you know a range of written sources and objects and understand how to use them alongside other evidence.",
   '4.4.b2 and 1.13.b3', 'qaa/fheq-2024/4.15.b5', 'knowledge/r1', 'a student works mainly from one kind of source',
   'which other kind of evidence would test the student\'s main source?')
kr('threshold', 3, ['understand'], 'viewpoints on interpretation and evaluation', UN,
   "Understands a range of positions on problems of interpretation and evaluation.",
   "At threshold, graduates understand several positions on questions of interpretation and evaluation.",
   "By graduation you will have shown that you understand several different views on how evidence is interpreted and judged.",
   '4.4.b3 and 1.13.b5', 'qaa/fheq-2024/4.15.b4', 'cognitive/r2', 'a student meets scholars who disagree',
   'what two scholars on the student\'s topic disagree about, and why?')
kr('threshold', 4, ['research', 'formulate', 'present'], 'researching, arguing and presenting orally and in writing', SK,
   "Researches topics, builds arguments and presents them in speech and writing.",
   "At threshold, graduates research a topic, form an argument and present it orally and in writing.",
   "By graduation you will have shown that you can research a topic, build an argument and present it both in speech and in writing.",
   '4.4.b4 and 1.13.b6', 'qaa/fheq-2024/4.15.b6', 'knowledge/r3', 'a student starts an essay, presentation or project',
   'what the student\'s argument is and what research it rests on?')
kr('threshold', 5, ['engage', 'forming'], 'observational, analytical and evaluative thinking to a threshold level', SK,
   "Thinks observantly, analytically and evaluatively, to a threshold level, about evidence, arguments and readings, and reaches judgements from evidence and argument.",
   "At threshold, graduates observe, analyse and evaluate evidence, arguments and interpretations at a basic level and judge from evidence and argument.",
   "By graduation you will have shown that you can look at, analyse and weigh up evidence and arguments, at least at a basic level, and reach a judgement from them.",
   '4.4.b5 and 1.15.b4', 'qaa/fheq-2024/4.15.b7', 'cognitive/r1', 'a student summarises sources without judging them',
   'what the student concludes from their evidence, and how sure they are?')
kr('threshold', 6, ['present'], 'written presentation to a threshold standard', GS,
   "Presents written material to a threshold standard, with attention to effective language, referencing and layout.",
   "At threshold, graduates present written work at a basic standard, attending to language, referencing and layout.",
   "By graduation you will have shown that you can present written work to at least a basic standard, taking care over language, references and layout.",
   '4.4.b6 and 1.16.b2', 'qaa/fheq-2024/4.15.b8', 'transferable/r1', 'feedback criticises a student\'s written presentation',
   'which of language, referencing or layout the student will fix first?')
kr('threshold', 7, ['work', 'employing', 'reflect'], 'relative independence, time management and reflection on progress', GS,
   "Works with some independence and intellectual initiative, manages time so that set tasks are finished on time, and reflects on progress.",
   "At threshold, graduates work with relative independence and initiative, manage time to complete set tasks on time and reflect on their progress.",
   "By graduation you will have shown that you can work fairly independently, take some initiative, manage your time so that tasks are done on time and reflect on how you are doing.",
   '4.4.b8 and 1.14.b1', 'qaa/fheq-2024/4.15.b9.1', 'transferable/r3', 'a student misses deadlines or relies heavily on guidance',
   'what the student would change in how they plan their time?')
kr('threshold', 8, ['work', 'perform'], 'effective work in a group', GS,
   "Works well with others to carry out set tasks in a group.",
   "At threshold, graduates work effectively with others on assigned group tasks.",
   "By graduation you will have shown that you can work well with others on tasks set for a group.",
   '4.4.b9 and 1.16.b3', 'qaa/fheq-2024/4.15.b9.1', 'transferable/r2', 'a student meets a group task or a group dispute',
   'what the student contributed to their last group task?')
kr('threshold', 9, ['demonstrate', 'modify'], "respect for others' views and willingness to change position", GS,
   "Respects other people's views and can change position when that is justified.",
   "At threshold, graduates respect others' views and can modify their position where warranted.",
   "By graduation you will have shown that you can show respect for other people's views and be ready to change your mind when there is good reason.",
   '4.4.b10 and 1.14.b5', 'qaa/fheq-2024/4.15.b4', 'transferable/r5', 'a seminar becomes heated or a student holds a view firmly',
   'when the student last changed their mind, and what persuaded them?')
kr('threshold', 10, ['make'], 'suitable use of digital resources and IT', GS,
   "Uses digital resources and IT suitably to find information, communicate and support learning.",
   "At threshold, graduates make appropriate use of digital resources and IT for information, communication and learning.",
   "By graduation you will have shown that you can use digital resources and technology sensibly to find information, communicate and help you learn.",
   '4.4.b11 and 1.16.b5', 'qaa/fheq-2024/4.15.b8', 'transferable/r1', 'a student relies on one digital tool or avoids them',
   'which digital resource helps the student learn most, and which they have not tried?')

# typical 4.4
kr('typical', 1, ['understand'], 'a range of features of another culture and cultural difference', UN,
   "Understands a range of features of another culture and is alert to cultural difference.",
   "At typical level, graduates understand a range of a culture's features and show sensitivity to cultural difference.",
   "For a typical good result you show that you grasp several features of a culture other than your own and are alert to how cultures differ.",
   '4.3.b1 and 4.5.b1', 'qaa/fheq-2024/4.15.b1', 'knowledge/r2', 'a student wants to move beyond the minimum in their cultural knowledge',
   'which further aspects of the culture the student could bring into their work?')
kr('typical', 2, ['demonstrate', 'used'], 'a diverse set of sources and broad understanding of combining evidence', KN,
   "Is familiar with a varied set of written and material sources and broadly understands how to use them with other evidence.",
   "At typical level, graduates know a diverse set of textual and material sources and broadly understand how to combine them with other evidence.",
   "For a typical good result you know a varied set of written sources and objects and broadly understand how to use them with other evidence.",
   '4.3.b2 and 4.5.b2', 'qaa/fheq-2024/4.15.b5', 'knowledge/r1', 'a student asks how to strengthen their use of sources',
   'which source type the student could add to widen their evidence?')
kr('typical', 3, ['understand', 'adopt'], 'a broad range of viewpoints and several critical approaches', UN,
   "Understands a broad range of positions on interpretation and evaluation and uses a variety of critical approaches to them.",
   "At typical level, graduates understand a broad range of interpretive positions and adopt several critical approaches.",
   "For a typical good result you understand many views on interpreting and judging evidence and can use several critical approaches.",
   '4.3.b3 and 4.5.b3', 'qaa/fheq-2024/4.15.b4', 'cognitive/r2', 'a student uses only one approach to a text or problem',
   'which other approach the student could apply and what it would show?')
kr('typical', 4, ['research', 'formulate', 'present'], 'research to a high standard with solid, lucid argument', SK,
   "Researches to a high standard, builds sound arguments and presents them lucidly in speech and writing.",
   "At typical level, graduates research well, form solid arguments and present them lucidly orally and in writing.",
   "For a typical good result you research to a high standard, build solid arguments and present them clearly in speech and writing.",
   '4.3.b4 and 4.5.b4', 'qaa/fheq-2024/4.15.b6', 'knowledge/r3', 'a student aims to move from a basic to a good essay',
   'where the student\'s argument is weakest and what research would shore it up?')
kr('typical', 5, ['engage', 'forming'], 'observational, analytical and evaluative thinking with sound judgement', SK,
   "Thinks observantly, analytically and evaluatively about evidence, arguments and readings, and reaches sound judgements from them.",
   "At typical level, graduates analyse and evaluate evidence, arguments and interpretations and form sound judgements.",
   "For a typical good result you analyse and weigh up evidence and arguments carefully and reach sound judgements.",
   '4.3.b5 and 4.5.b5', 'qaa/fheq-2024/4.15.b7', 'cognitive/r1', 'a student wants to sharpen their judgement in essays',
   'how the student tested their judgement against the strongest counter-evidence?')
kr('typical', 6, ['present'], 'written presentation to a good standard', GS,
   "Presents written material to a good standard, with discerning, lucid language, professional referencing and clear, effective layout.",
   "At typical level, graduates present written work well, with discerning and lucid language, professional referencing and clear layout.",
   "For a typical good result your written work is well presented, with clear, careful language, professional references and a clear layout.",
   '4.3.b6 and 4.5.b6', 'qaa/fheq-2024/4.15.b8', 'transferable/r1', 'a student asks how to lift the presentation of their writing',
   'which convention of professional referencing the student is least sure of?')
kr('typical', 7, ['extract', 'identify', 'solve'], 'drawing key points from complex information and solving problems with a range of methods', GS,
   "Draws key points from complex information and recognises and solves the problems it raises, using a range of methods.",
   "At typical level, graduates draw the main points out of complex information, then spot and solve the problems it raises with a range of methodologies.",
   "For a typical good result you can pick out what matters in complex information and spot and solve problems using a range of methods.",
   '4.5.b7 and 1.15.b2', 'qaa/fheq-2024/4.15.b3.1', 'cognitive/r3', 'a student faces a large or tangled body of material',
   'which method the student would use first on their material, and which second?')
kr('typical', 8, ['work', 'employing', 'reflect'], 'a high degree of independence, effective time management and reflection', GS,
   "Works with a high degree of independence and initiative, manages time well so tasks are finished on time, and reflects on progress.",
   "At typical level, graduates work with a high degree of independence and initiative, manage time effectively and reflect on progress.",
   "For a typical good result you work largely on your own initiative, manage your time well so tasks are finished on time, and reflect on your progress.",
   '4.3.b7 and 4.5.b9', 'qaa/fheq-2024/4.15.b9.1', 'transferable/r3', 'a student moves into independent project work',
   'what the student decides alone now and where they still seek guidance?')
kr('typical', 9, ['work', 'perform'], 'creative, flexible group work', GS,
   "Works creatively and adaptably with others on set group tasks.",
   "At typical level, graduates work creatively and flexibly with others on assigned group tasks.",
   "For a typical good result you work creatively and adaptably with others on group tasks.",
   '4.3.b8 and 4.5.b10', 'qaa/fheq-2024/4.15.b9.1', 'transferable/r2', 'a student\'s group work goes smoothly but without ideas',
   'what creative contribution the student made to their group, and how the group adapted?')
kr('typical', 10, ['demonstrate', 'reflect', 'modify'], "respect for others' views with critical reflection and change of position", GS,
   "Respects other people's views, reflects critically and changes position when that is justified.",
   "At typical level, graduates respect others' views and can reflect critically and modify their position where warranted.",
   "For a typical good result you respect other people's views, think critically about them and change your mind when there is good reason.",
   '4.3.b9 and 4.5.b11', 'qaa/fheq-2024/4.15.b4', 'transferable/r5', 'a student debates a contested reading',
   'which argument from a classmate made the student rethink, and how?')
kr('typical', 11, ['make'], 'effective and suitable use of digital resources and IT', GS,
   "Uses digital resources and IT effectively and suitably to find information, communicate and support learning.",
   "At typical level, graduates use digital resources and IT effectively and fittingly for information, communication and learning.",
   "For a typical good result you use digital resources and technology well to find information, communicate and support your learning.",
   '4.3.b10 and 4.5.b12', 'qaa/fheq-2024/4.15.b8', 'transferable/r1', 'a student plans the digital side of a project',
   'how the student checks the reliability of digital sources they use?',
   find=FINDS['4.4.b11'], after='4.4 Honours graduates of a typical level')

# excellent 4.5
kr('excellent', 1, ['understand'], 'wide understanding of another culture and cultural difference', UN,
   "Understands many features of a culture other than their own and is alert to cultural difference.",
   "At excellent level, graduates understand a wide range of a culture's features and show sensitivity to cultural difference.",
   "For a first-class result you show that you understand a wide range of features of another culture and are alert to how cultures differ.",
   '4.4.b1 and 1.13.b1', 'qaa/fheq-2024/4.15.b1', 'knowledge/r2', 'a student aims for a first and asks what breadth that needs',
   'how widely the student\'s work ranges across the culture they study?')
kr('excellent', 2, ['demonstrate', 'used'], 'a wide, diverse set of sources and deep understanding of combining evidence', KN,
   "Is familiar with a wide, varied set of written and material sources and understands deeply how to use them with other evidence.",
   "At excellent level, graduates know a wide and diverse set of sources and understand in depth how to combine them with other evidence.",
   "For a first-class result you know a wide and varied set of written sources and objects and understand in depth how to use them with other evidence.",
   '4.4.b2 and 1.13.b3', 'qaa/fheq-2024/4.15.b5', 'knowledge/r1', 'a student aims for a first in source-based work',
   'where combining two kinds of evidence changed the student\'s conclusion?')
kr('excellent', 3, ['understand', 'adopt'], 'complex viewpoints and a wide variety of critical approaches', UN,
   "Understands a broad range of sometimes complex positions on interpretation and evaluation and uses a wide variety of critical approaches.",
   "At excellent level, graduates understand a broad, sometimes complex range of positions and adopt a wide variety of critical approaches.",
   "For a first-class result you understand a broad range of views, some of them complex, and use a wide variety of critical approaches.",
   '4.4.b3 and 1.13.b5', 'qaa/fheq-2024/4.15.b4', 'cognitive/r2', 'a student handles a contested problem well and wants to go further',
   'which complex position the student could set against their own?')
kr('excellent', 4, ['research', 'formulate', 'present'], 'excellent research with cogent, nuanced argument', SK,
   "Researches to an excellent standard, builds cogent and nuanced arguments and presents them lucidly in speech and writing.",
   "At excellent level, graduates research excellently, form cogent and nuanced arguments and present them lucidly orally and in writing.",
   "For a first-class result you research to an excellent standard, build convincing and subtle arguments and present them clearly in speech and writing.",
   '4.4.b4 and 1.13.b6', 'qaa/fheq-2024/4.15.b6', 'knowledge/r3', 'a student plans a dissertation aiming high',
   'where the student\'s argument shows nuance, and where it is still blunt?')
kr('excellent', 5, ['engage', 'forming'], 'high-standard thinking with sound and sometimes original judgement', SK,
   "Thinks observantly, analytically and evaluatively to a high standard about evidence, arguments and readings, reaching sound and at times original judgements.",
   "At excellent level, graduates analyse and evaluate to a high standard and form sound, sometimes original judgements.",
   "For a first-class result you analyse and weigh up evidence and arguments to a high standard and reach sound, sometimes original judgements.",
   '4.4.b5 and 1.15.b4', 'qaa/fheq-2024/4.15.b7', 'cognitive/r1', 'a student asks what originality means at undergraduate level',
   'which judgement in the student\'s work is their own rather than a scholar\'s?')
kr('excellent', 6, ['present'], 'written presentation to a high standard', GS,
   "Presents written material to a high standard, with discerning, lucid language, professional referencing and clear, effective layout.",
   "At excellent level, graduates present written work to a high standard with discerning, lucid language, professional referencing and clear layout.",
   "For a first-class result your written work is presented to a high standard, with clear, careful language, professional references and a clear layout.",
   '4.4.b6 and 1.16.b2', 'qaa/fheq-2024/4.15.b8', 'transferable/r1', 'a student polishes a dissertation or final essay',
   'what the student would change to make their prose clearer?')
kr('excellent', 7, ['extract', 'identify', 'solve'], 'key points and nuance from complex information; problems solved with a wide range of methods', GS,
   "Draws both key points and nuance from complex information and recognises and solves the problems it raises with a wide range of methods.",
   "At excellent level, graduates extract key elements and nuance from complex information and solve problems with a wide range of methodologies.",
   "For a first-class result you pick out both what matters and the finer points in complex information and solve problems using a wide range of methods.",
   '4.4.b7 and 1.15.b2', 'qaa/fheq-2024/4.15.b3.1', 'cognitive/r3', 'a student handles complex material well and wants more depth',
   'what nuance in the material the student\'s first reading missed?')
kr('excellent', 8, ['display'], 'creativity and originality in problem-solving and communicating ideas', GS,
   "Shows creativity and originality in solving problems and in developing and communicating ideas and arguments.",
   "At excellent level, graduates display creativity and originality in problem-solving and in developing and communicating ideas.",
   "For a first-class result you show creativity and originality in solving problems and in developing and sharing ideas.",
   '1.14.b4 and 1.15.b6', 'qaa/fheq-2024/4.15.b3.1', 'cognitive/r4', 'a student asks what lifts work into the first-class range',
   'what the student has tried in their work that nobody asked them to?')
kr('excellent', 9, ['work', 'employing', 'reflect'], 'considerable independence, effective time management and reflection', GS,
   "Works with considerable independence and initiative, manages time well so tasks are finished on time, and reflects on progress.",
   "At excellent level, graduates work with considerable independence and initiative, manage time effectively and reflect on progress.",
   "For a first-class result you work with real independence and initiative, manage your time well and reflect on your progress.",
   '4.4.b8 and 1.14.b1', 'qaa/fheq-2024/4.15.b9.1', 'transferable/r3', 'a student leads their own project',
   'what the student has decided about their project without being prompted?')
kr('excellent', 10, ['work', 'perform'], 'creative, flexible group work', GS,
   "Works creatively and adaptably with others on set group tasks.",
   "At excellent level, graduates work creatively and flexibly with others on assigned group tasks.",
   "For a first-class result you work creatively and adaptably with others on group tasks.",
   '4.4.b9 and 1.16.b3', 'qaa/fheq-2024/4.15.b9.1', 'transferable/r2', 'a student leads or shapes a group project',
   'how the student helped the group adapt when a plan failed?')
kr('excellent', 11, ['demonstrate', 'reflect', 'modify'], "respect for others' views with enhanced critical reflection", GS,
   "Respects other people's views and has a stronger capacity to reflect critically and change position when justified.",
   "At excellent level, graduates respect others' views with an enhanced capacity to reflect critically and modify their position.",
   "For a first-class result you respect other people's views and are especially able to think critically about them and change your mind for good reason.",
   '4.4.b10 and 1.14.b2', 'qaa/fheq-2024/4.15.b4', 'transferable/r5', 'a student debates or reviews peer work',
   'how the student weighed a view they first disagreed with?')
kr('excellent', 12, ['make'], 'effective and suitable use of digital resources and IT', GS,
   "Uses digital resources and IT effectively and suitably to find information, communicate and support learning.",
   "At excellent level, graduates use digital resources and IT effectively and fittingly for information, communication and learning.",
   "For a first-class result you use digital resources and technology well to find information, communicate and support your learning.",
   '4.4.b11 and 1.16.b5', 'qaa/fheq-2024/4.15.b8', 'transferable/r1', 'a student uses digital tools in an ambitious project',
   'what the student\'s digital method adds that a traditional one would not?')

for _r in P.values():
    _r.pop('themes', None)

# same outcome one rung below (inferred: the issuer gives three lists in near-parallel order but does not pair them)
GRADE = {}
_T2 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 8: 7, 9: 8, 10: 9, 11: 10}           # typical bullet: threshold bullet
_E2 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 9: 8, 10: 9, 11: 10, 12: 11}   # excellent bullet: typical bullet
for _t, _l in _T2.items():
    GRADE['4.4.b%d' % _t] = '4.3.b%d' % _l
for _e, _l in _E2.items():
    GRADE['4.5.b%d' % _e] = '4.4.b%d' % _l

TH = {'1.22': 'theme:edi', '1.23': 'theme:edi', '1.25': 'theme:edi'}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.6; 4.2'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.6; 4.2'),
            dict(id='fheq:4', role='names', locator='D1, 2.8 (Certificate of Higher Education as an exit award; level read from the FHEQ, inferred: Part E)'),
            dict(id='fheq:5', role='names', locator='D1, 2.8 (Diploma of Higher Education as an exit award; level read from the FHEQ, inferred: Part E)'),
            dict(id='fheq:7', role='names', locator="D1, 1.19; 3.20 (master's study after the degree; no standards stated; inferred: Part E)"),
            dict(id='spine:6', role='refers', locator='std:ref:uk-framework R2 and R8 (inferred: Part E)')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.6: "FHEQ Level 6; FQHEIS Level 10"; 4.2, the title of Annex D)'),
                dict(**{'from': 'fheq:6'}, to='spine:6', relation='sameStep', basis='inferred from std:ref:uk-framework R2 (Part E)')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.22', '1.23', '1.24', '1.25', '2.4', '2.16', '3.4', '3.14']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.3', '1.16', '1.25', '2.1', '2.2', '2.3', '2.9', '2.10', '3.13', '3.16', '3.21', '3.22']),
      dict(id='theme:esd', role='carries', carriedIn=['1.26', '1.27', '1.28', '1.29']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.17', '1.18', '1.30', '1.31', '2.12'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-classics-and-ancient-history-including-byzantine-studies-and-modern-greek-2019-benchmarks (not yet ingested)',
           note='the fourth edition (2019), named in section 6; the front matter lists key changes'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees (4.2); SL6'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='level 6 (2.6, 4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='level 10 (2.6, 4.2)'),
      dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note='quoted on what ESD is (1.27); listed in section 5'),
      dict(rel='refersTo', target="UNESCO, Education for Sustainable Development: Towards Achieving the Sustainable Development Goals (not ingested: Part E)", note='the eight key competences (1.29)'),
      dict(rel='refersTo', target='UN Sustainable Development Goals (external)', note='goals 5, 10, 11 and 16 named (1.27, 1.28)'),
      dict(rel='readWith', target='the Subject Benchmark Statements of partner subjects in joint honours (collection)', note='2.7; 3.5'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance; QAA Glossary', note='front matter')]

SB1 = [
    'The study of ancient Greece and Rome from the late Bronze Age to Late Antiquity, of Byzantium from 324 to 1453 CE and of the Greek-speaking world from the late medieval period on, widening to other ancient cultures and to reception in every period (D1, 1.1, 3.1, 3.2, 3.3).',
    'Interdisciplinary by nature: art, archaeology, history, language and linguistics, literature, philology, philosophy, law, science, medicine and reception, studied in varying mixes (D1, 1.1, 1.20).',
    'Several routes into the classical: Classics with both ancient languages, single-language Greek or Latin, Classical Studies, Ancient History, Classical Archaeology, Modern Greek and Late Antique and Byzantine Studies (D1, 1.2, 3.5 to 3.12).',
    'Languages are central but not universal: Classics and Modern Greek require proficiency, other routes offer languages at several entry points (D1, 2.1, 3.6, 3.9, 3.12, 3.20).',
    'Critical handling of fragmentary, varied evidence, material, written and digital, is its characteristic method (D1, 1.20, 1.13).',
    'It sees Greek and Roman societies as linked with each other and with the wider Mediterranean and beyond, through influence, conflict and borrowing (D1, 1.21, 1.24).',
    "A self-critical discipline: it confronts its reputation for elitism and its ties to empire, colonialism, race and class (D1, 1.4, 1.22 to 1.24).",
    'A liberal, non-vocational tradition that nonetheless builds a broad platform of transferable skills valued by employers (D1, 1.5, 1.6, 1.17, 1.31).',
]

SB2 = [dict(theme='theme:edi', inThisSubject='the subject confronts its elitist reputation and its links with imperialism, colonialism, white supremacy and class; it calls for inclusive curricula, diverse reading lists, decolonising approaches, inclusive peer groups and care with sensitive topics such as slavery (D1, 1.22 to 1.25, 2.4, 3.4, 3.14)',
            statements=['1.22', '1.23', '1.25', '2.4', '3.4', '1.14.b5']),
       dict(theme='theme:accessibility', inThisSubject='headed Accessibility in the text: students arrive by varied routes, including popular culture and online platforms; blended and online delivery, captioning and recording, low-risk options, language pathways and adjustments for fieldwork and assessment (D1, 2.1 to 2.3, 2.9, 2.10, 3.16, 3.21, 3.22)',
            statements=['1.25', '3.21', '3.20', '1.16.b1']),
       dict(theme='theme:esd', inThisSubject='headed Sustainability in the text: dialogue with antiquity puts modern values such as growth and consumerism in perspective; ancient evidence bears on four UN goals; the subject builds four UNESCO competences: systems thinking, critical thinking, collaboration and integrated problem-solving (D1, 1.26 to 1.29)',
            statements=[]),
       dict(theme='theme:enterprise', inThisSubject='headed Entrepreneurship and enterprise education, with employability: not labelled as such but built into the curriculum through problem-solving, creative thinking and project-based assessment; careers advice, placements and work schemes (D1, 1.17, 1.18, 1.30, 1.31, 2.12)',
            statements=['1.16.b7', '1.14.b4'])]

SB3 = dict(
    areas=[dict(component='1.8', gloss='history and historical method'),
           dict(component='1.9', gloss='ancient and modern languages and linguistics'),
           dict(component='1.10', gloss='literature, textual transmission, epigraphy and papyrology'),
           dict(component='1.11', gloss='ancient philosophy and science'),
           dict(component='1.12', gloss='art, architecture, archaeology and material culture'),
           dict(component='3.1', gloss='the ancient Mediterranean, centred on Greece and Rome'),
           dict(component='3.2', gloss='Byzantine Studies and Modern Greek defined'),
           dict(component='3.3', gloss='reception and the history of the discipline'),
           dict(component='3.6', gloss='Classics: Greek and Latin languages and literature'),
           dict(component='3.7', gloss='Ancient Greek or Latin as single-language routes'),
           dict(component='3.8', gloss='Classical Studies or Civilisation'),
           dict(component='3.9', gloss='Ancient History'),
           dict(component='3.10', gloss='Classical Archaeology'),
           dict(component='3.11', gloss='Late Antique and Byzantine Studies'),
           dict(component='3.12', gloss='Modern Greek language, literature and history')],
    practices=[dict(component='2.5', kind='learning', gloss='independent research ending in a supervised dissertation'),
               dict(component='2.10', kind='teaching', gloss='blended delivery from in person to fully online'),
               dict(component='3.16', kind='teaching', gloss='modulating delivery for sensitive material and adjustments'),
               dict(component='3.17', kind='learning', gloss='essays, language and source exercises, digital skills, seminars, lectures, group projects, placements, media, museum work, podcasts, blogs, revision, dissertation'),
               dict(component='3.18', kind='learning', gloss='speaking practice and a year abroad in Modern Greek; study tours, museum visits and fieldwork'),
               dict(component='3.20', kind='learning', gloss='language pathways from any starting point'),
               dict(component='3.21', kind='learning', gloss='art, field archaeology and museum training and placements'),
               dict(component='3.22', kind='assessment', gloss='varied assessment on three principles: outcomes, formative and summative, inclusive'),
               dict(component='3.23', kind='assessment', gloss='cognitive attributes assessed through essays and exercises; Modern Greek oral assessment'),
               dict(component='3.25', kind='assessment', gloss='practical skills, mainly formative; language certification'),
               dict(component='3.26', kind='assessment', gloss='unseen, open-book and in-class tests, coursework, dissertations, presentations, discussion, orals, creative responses'),
               dict(component='3.27', kind='assessment', gloss='variety and choice of assessment to remove barriers')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.3 (under the heading Threshold level (3rd class))', award=HON, items=10),
           dict(rung='typical', leadIn='4.4 (under the heading Typical level (2:1 or 2:2))', award=HON, items=11),
           dict(rung='excellent', leadIn='4.5 (under the heading Excellent level (1st class))', award=HON, items=12)],
    rungBases='each rung is tied to a degree class in its heading and lead-in (third; 2:1 or 2:2; first); the items are given as examples of evidence of proficiency ("for example"); 4.1 calls the threshold the minimum and 4.2 sends providers to Annex D for the classes',
    outcomeLists=[dict(leadIn='1.13', gloss='subject-specific characteristics of honours graduates (some or all; not exhaustive)', items=7, award=['honours']),
                  dict(leadIn='1.14', gloss='cognitive attributes fostered by study in the subject', items=7, award=['honours']),
                  dict(leadIn='1.15', gloss='specific abilities the qualities of mind presuppose', items=8, award=['honours']),
                  dict(leadIn='1.16', gloss='additional practical capacities', items=7, award=['honours'])],
    outcomes=[dict(outcome='another culture and cultural difference', threshold='4.3.b1', typical='4.4.b1', excellent='4.5.b1', basis='inferred', domain='understanding', award=HON),
              dict(outcome='written and material sources combined with other evidence', threshold='4.3.b2', typical='4.4.b2', excellent='4.5.b2', basis='inferred', domain='knowledge', award=HON),
              dict(outcome='viewpoints on interpretation and critical approaches', threshold='4.3.b3', typical='4.4.b3', excellent='4.5.b3', basis='inferred', domain='understanding', award=HON),
              dict(outcome='research, argument and presentation', threshold='4.3.b4', typical='4.4.b4', excellent='4.5.b4', basis='inferred', domain='subject-skill', award=HON),
              dict(outcome='observational, analytical and evaluative thinking', threshold='4.3.b5', typical='4.4.b5', excellent='4.5.b5', basis='inferred', domain='subject-skill', award=HON),
              dict(outcome='written presentation', threshold='4.3.b6', typical='4.4.b6', excellent='4.5.b6', basis='inferred', domain='generic-skill', award=HON),
              dict(outcome='complex information and problem-solving', threshold='none', typical='4.4.b7', excellent='4.5.b7', basis='inferred', domain='generic-skill', award=HON),
              dict(outcome='creativity and originality', threshold='none', typical='none', excellent='4.5.b8', basis='inferred', domain='generic-skill', award=HON),
              dict(outcome='independence, time management and reflection', threshold='4.3.b7', typical='4.4.b8', excellent='4.5.b9', basis='inferred', domain='generic-skill', award=HON),
              dict(outcome='group work', threshold='4.3.b8', typical='4.4.b9', excellent='4.5.b10', basis='inferred', domain='generic-skill', award=HON),
              dict(outcome="respect for others' views and change of position", threshold='4.3.b9', typical='4.4.b10', excellent='4.5.b11', basis='inferred', domain='generic-skill', award=HON),
              dict(outcome='digital resources and IT', threshold='4.3.b10', typical='4.4.b11', excellent='4.5.b12', basis='inferred', domain='generic-skill', award=HON)])

SB4A_FULL = []

SB5 = [dict(body='Classical Association; Classics for All', says='no subject association is closely linked to curricula, but many departments and students gain from these two, which connect them with schools and younger learners (D1, 2.11)', requirements='not applicable: partners, not professional, statutory or regulatory bodies (Part E)'),
       dict(body='British School at Athens; British School at Rome', says='link university teachers as researchers and offer some students the chance to study Greek and Roman remains on site, notably through summer schools (D1, 2.11)', requirements='not applicable: partners (Part E)'),
       dict(body='Societies for the Promotion of Hellenic and Roman Studies', says='provide library resources, internships, prizes, grants and awards for student projects (D1, 2.11)', requirements='not applicable: partners (Part E)'),
       dict(body='professional, statutory and regulatory bodies (unnamed)', says='the statement gives them the academic standards expected of students; their requirements may be another reference point (D1, front matter)', requirements='not applicable: no body accredits the subject (Part E)')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.22', '1.23', '1.24', '1.25', '2.4', '2.16', '3.4', '3.14'],
                 statements=['1.22', '1.23', '1.25', '2.4', '3.4', '1.14.b5']),
            dict(id='theme:accessibility', named='Accessibility', carriedIn=['1.3', '1.16', '1.25', '2.1', '2.2', '2.3', '2.9', '2.10', '3.13', '3.16', '3.21', '3.22'],
                 statements=['1.25', '3.20', '3.21', '1.16.b1']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.26', '1.27', '1.28', '1.29'],
                 statements=[]),
            dict(id='theme:enterprise', named='Entrepreneurship and enterprise education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.17', '1.18', '1.30', '1.31', '2.12'],
                 statements=['1.16.b7', '1.14.b4'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6'], citedIn=['2.6', '4.2']),
                dict(framework='scqf', levels=['fqheis:10'], citedIn=['2.6', '4.2'])],
    bodies=[dict(body='Classical Association', citedIn=['2.11']),
            dict(body='Classics for All', citedIn=['2.11']),
            dict(body='British School at Athens', citedIn=['2.11']),
            dict(body='British School at Rome', citedIn=['2.11']),
            dict(body='Societies for the Promotion of Hellenic/Roman Studies', citedIn=['2.11']),
            dict(body='professional, statutory and regulatory bodies (PSRBs; unnamed)', citedIn=['front matter'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='the four honours classes, read beside the rung lists'),
                     dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development Guidance (QAA and Advance HE, 2021)', citedIn=['1.27', '5'], role='defines ESD, quoted in the sustainability principles'),
                     dict(document='UNESCO, Education for Sustainable Development: Towards Achieving the Sustainable Development Goals (not ingested: Part E)', named='The UNESCO global framework', citedIn=['1.29'], role='the eight key competences for sustainability'),
                     dict(document='UN Sustainable Development Goals (external)', named="the UN's sustainable development goals", citedIn=['1.27', '1.28'], role='goals 5, 10, 11 and 16 as material for reflection'),
                     dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
                     dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms')])

B1 = [dict(slug='byzantine-studies', definition='the branch of the subject that studies late antique and medieval Byzantium and Constantinople, from its refounding in 324 CE to 1453 CE (D1, 3.2)',
           beneficiaryDefinition='the study of the eastern Roman, Greek-speaking empire centred on Constantinople', scopeNote='includes literature, theology, culture, history, archaeology and art history (3.11)', category='unknown', practices=['classics']),
      dict(slug='modern-greek', definition='the study of the Greek-speaking world, its diaspora included, from the late medieval period onwards (D1, 3.2)',
           beneficiaryDefinition='the study of the Greek language and the Greek-speaking world from the later Middle Ages to today', scopeNote='courses require proficiency in the language (3.12)', category='unknown', practices=['classics', 'languages']),
      dict(slug='classics', definition='a course in which students must become proficient in both ancient Greek and Latin, often centred at first on their literatures (D1, 3.6)',
           beneficiaryDefinition='a degree that teaches both ancient Greek and Latin', scopeNote='narrower than the subject area, which the statement also calls Classics and Ancient History', category='unknown', practices=['classics']),
      dict(slug='classical-studies', definition='a course giving a broad understanding of Greco-Roman culture as a whole, with languages optional; also called Classical Civilisation (D1, 3.8)',
           beneficiaryDefinition='a degree on the whole culture of ancient Greece and Rome, where learning the languages is optional', scopeNote='', category='unknown', practices=['classics']),
      dict(slug='gobbet', definition='a short critical commentary on a passage or item, used as an exercise (D1, 3.17)',
           beneficiaryDefinition='a short commentary on an extract from a source', scopeNote='', category='unknown', practices=['classics'])]
B2A = [dict(concept='byzantine-studies', form="Byzantine Studies", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='modern-greek', form='Modern Greek', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='classics', form='Classics', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='classical-studies', form='Classical Studies', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='classical-studies', form='Classical Civilisation', lang='en', partOfSpeech='noun-phrase', termStatus='admitted', register='formal'),
       dict(concept='gobbet', form='gobbets', lang='en', partOfSpeech='noun', termStatus='preferred', register='informal')]
B4 = []; B5 = []

D3 = [dict(source='UNESCO, Education for Sustainable Development: Towards Achieving the Sustainable Development Goals (2017)', why='the eight key competences the statement maps the subject against (1.29; SB6)', status='wanted')]

E = [
    'Rungs: three, each a lead-in naming the degree class in its heading and text: threshold (4.3, third class, 10 items), typical (4.4, 2:1 or 2:2, 11 items) and excellent (4.5, first class, 12 items). Unlike Psychology, the rungs are tied to classes and the lists run in near-parallel order, so most outcomes are traced across all three.',
    'Lead-in wording: "Honours graduates of a ... level of attainment ... will have demonstrated ... Evidence of proficiency will have been provided if, for example, a graduate has ... demonstrated an ability to"; recorded as force will. The items are offered as examples of evidence, not a closed list; the threshold lead-in also asks only for proficiency "to some degree" in "the majority of the attributes listed". New lead-in wording against Psychology.',
    'gradeOf links, all inferred (the issuer does not pair the items): 4.4.b1 to b6 from 4.3.b1 to b6; 4.4.b8 to b11 from 4.3.b7 to b10; 4.5.b1 to b7 from 4.4.b1 to b7; 4.5.b9 to b12 from 4.4.b8 to b11. Unlinked: 4.4.b7 (extract key elements and solve problems) first appears at typical; 4.5.b8 (creativity and originality) only at excellent. 4.4.b9 and 4.5.b10 are word for word the same (group work), as are 4.4.b11 and 4.5.b12 (digital resources); kept as issued, and 4.4.b11 is cut with `find` and `after` because its text occurs twice.',
    'Section 1 outcome lists recorded as statements (type outcome, rung none): 1.13 (graduate characteristics, "some or all", 7), 1.14 (cognitive attributes, 7), 1.15 (specific abilities, 8), 1.16 (practical capacities, 7). Their lead-ins have no modal ("designed to produce honours graduates who have", "include", "namely to", "namely the ability to"), so force is describes; 3.23 and 3.25 treat 1.13 to 1.16 as assessable outcomes. P3 to confirm they belong in S4.',
    'Not cut as statements: the opportunity lists 1.8 to 1.12 ("Such study promotes", "enables students to"), which describe what optional study may offer; the employment list 1.18; the ESD principles 1.27 and competences 1.29 (1.27.b3 and 1.29.b1 to b3 use will or should of education in general); the summative assessment forms 3.26 and assessment principles 3.22; 4.1, which frames the rungs ("will have demonstrated"; "Graduates will have acquired most or a majority").',
    'Provider practice described with will, not cut (as run 0085): 2.13 ("They will draw on a range of external reference points") and 2.14 ("providers will use external reviewers"), 2.15 (external examiners "will be asked").',
    'Plain-present provider norms not cut (benchmark template open point 5, for P3): 2.1 ("Courses are structured to ensure"), 2.2 ("Courses aim to build"), 2.3 ("all modes ... are underpinned by a concern for accessibility"), 2.9, 2.10, 3.13, 3.14 ("Higher education providers ensure suitable skills training, and teachers ensure"), 3.22 ("It is for higher education providers to decide"; "courses include elements of both formative and summative assessment").',
    'Obliging words outside the five, for Abbott: 1.23 "need to be addressed and acknowledged" (recorded as describes); 2.6 "it is expected" and "it would be expected" (recorded with will, its own modal); 3.3 "It is desirable"; 3.18 "is indispensable" and "highly desirable" (not cut); 3.20 "highly desirable" and "requires the provision of different language pathways" (recorded at should, its own modal); 3.6 "are required" and 3.12 "require" recorded as must (required is must, brief).',
    '3.17 is recorded as its stem only (will, softened by "generally"); its 21 list items (essays, exercises, seminars, placements and others) are S3 practice content, as run 0085 did for 2.20.',
    '3.21 is recorded at will for its last sentence ("reasonable adjustments will be made"); the rest of the paragraph is permissive (may).',
    '1.22, 1.23 and 1.25 address the discipline and its teaching rather than the student; recorded with addressee provider and the student version not applicable.',
    'Skeleton corrections: 1.13.b7 carried the sub-heading "General abilities, transferable skills and qualities of mind" and 4.4.b11 carried "Excellent level (1st class)"; recut with `find`. Paragraph spans for 1.25, 3.12, 3.20, 3.21, 3.24 and 4.2 carried a following heading or page number; recut to the paragraph text. The held text at 1.17 reads "Byzantine Studies Modern Greek" without "and"; kept as held.',
    'Held-text extraction faults: broken words such as "successf ul", "f irst", "staf f", "m ay", "f orms" and "in-c lass"; no recorded verb depends on them.',
    'Inferred codes: HECoS 101129 (classical reception), from the stress on reception in 1.1, 1.4 and 3.3; HECoS 100329 (modern languages) for Modern Greek, as the HESA store holds no Modern Greek term (P3 to confirm or replace). Codes marked stated match subject or course names the text gives (Classics, Ancient History, Byzantine Studies, Latin, Ancient Greek, Classical Studies, Classical Archaeology); the text gives no codes itself.',
    'Levels inferred: fheq:4 and fheq:5 from the exit awards named in 2.8 (Certificate and Diploma of Higher Education); fheq:7 from the mentions of master\'s study (1.19, 3.20), with no standards stated; fheq:6 to spine:6 from std:ref:uk-framework R2. The MA (Hons) in Scotland (1.1) and the four-year Scottish honours degree (2.8) fall under fqheis:10.',
    'Theme note: no theme sentence is itself a statement except 1.22, 1.23 and 1.25 (equality, diversity and inclusion). The sustainability paragraphs 1.26 to 1.29 carry no standard, so theme:esd has no statements; the theme shows in outcomes only indirectly (1.14.b6 historical perspective on current issues). No generative AI section.',
    'SB5: no professional, statutory or regulatory body accredits the subject; the front matter names PSRBs only in general. The bodies in 2.11 (Classical Association, Classics for All, the British Schools at Athens and Rome, the Hellenic and Roman Societies) are partners and subject associations, recorded for completeness; no requirements document applies.',
    'SB6: the front matter also names the Office for Students regulatory framework, the Quality Assessment Framework for Wales and the Quality Enhancement Framework (Scotland); excluded matter and not qualification frameworks, so not in SB6 frameworks. Section 6 names the Disabled Students\' Commission and the Council of University Classical Departments as contributors; excluded matter, not recorded as bodies.',
    'CQFW: not cited by the statement; not used.',
    'Section order and headings: section 1 has an "Opportunities" sub-section (1.7 to 1.19) holding the graduate lists that Psychology places in its own section; section 3 has sub-disciplinary examples (language; art and field archaeology). Filled by function.',
    'Supersedes: the 2019 fourth edition is named only in the advisory group list (section 6), with the 2014, 2007 and 2000 editions; the fifth edition was published 30 March 2022.',
    'Licence: QAA copyright notice only; re-use terms not stated in the text.',
]
