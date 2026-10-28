# Judgement for run 0133, QAA Town and Country Planning (April 2024). std run agent, under BM-BRIEF 0.2.3,
# the benchmark template 0.6.0-draft and the standards run layer 0.7.0-draft. Keys are S4 ids under
# qaa/town-and-country-planning-2024/. Our words throughout, except `find` (the issuer's text, to fix a span).
HON = "bachelor's with honours"
MAS = "master's"          # the integrated master's (MPlan, 2.7, 4.10), recorded as master's by the batch 1 convention
T = 'qaa/town-and-country-planning-2024/'
FH = 'qaa/fheq-2024/'
AD = 'qaa/fheq-2024/annex-d/'

def CITE(n):
    return f"Cite it as (QAA, 2024, Town and Country Planning Subject Benchmark Statement, para {n})."

META = dict(
    run='0133', p1='2026-10-03 18:42',
    title='Subject Benchmark Statement Town and Country Planning',
    heading='Subject Benchmark Statement: Town and Country Planning (QAA, April 2024)',
    edition='April 2024 (fifth edition)', published='2024-04',
    status='current', supersedes='the fourth edition, 2019 (D1, back matter)',
    subjects=[
        dict(scheme='hecos', code='100197', label='planning', basis='stated'),
        dict(scheme='hecos', code='100199', label='urban and regional planning', basis='stated'),
        dict(scheme='cah', code='CAH13-01-04', label='planning (urban, rural and regional)', basis='stated'),
        dict(scheme='hecos', code='100593', label='rural planning', basis='inferred'),
    ],
    awards=[HON, MAS], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, fifth edition of this statement (April 2024), with the cross-cutting themes',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    authority='reference: a sector reference point and not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)',
    agentDefinition=("QAA's UK reference point for what a graduate in town and country planning (spatial, urban and regional, "
                     "land-use, city, environmental or community planning) should know and be able to do at the end of an honours "
                     "degree, with three standards (threshold, typical, excellent) and an added list for the integrated master's (MPlan). "
                     "Reach for it when designing, reviewing or describing a planning course or its outcomes. It is not a curriculum, "
                     "not the RTPI's accreditation requirements and not a regulatory requirement in England."),
    summary=("Published by QAA in April 2024 as the fifth edition, the statement covers undergraduate and taught postgraduate planning "
             "courses, with standards for bachelor's degrees with honours (FHEQ level 6, FQHEIS level 10) and integrated master's "
             "degrees (FHEQ level 7, FQHEIS level 11). Its threshold list has 13 items, each tagged by the issuer with one or two of "
             "five themes (knowledge and understanding, cognitive, practical and transferable skills, professional competencies); "
             "the typical and excellent standards are two broad items each, building on the threshold, and the integrated master's "
             "adds four. It treats the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; "
             "enterprise and entrepreneurship), points to Annex D of the qualifications frameworks for the honours classes, names "
             "the RTPI as the body conferring Chartered Town Planner status, and sets out content in five thematic groupings "
             "rather than a prescribed list."))

S2 = dict(
    governs="what a town and country planning graduate can be expected to know, do and understand at the end of an honours degree or an integrated master's, and the nature of planning courses (D1, front matter: About this Statement; 1.7; 1.19; 4.1; 4.10)",
    awards=["bachelor's degrees with honours, single, joint or combined (1.17, 2.3, 2.6)", "integrated master's degrees, MPlan (1.17, 2.7, 4.10)",
            "taught master's, including conversion courses: the statement informs them (1.7, 1.17, 1.19), but section 4's standards are set for the two awards above"],
    levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope='"The Statement addresses Town and Country Planning degree courses at both undergraduate and taught postgraduate levels, as well as helping to inform those designing other degree courses which have a substantial Planning content." (D1, 1.7)',
    statedSubjects=[
        dict(name='Town and Country Planning (Planning as shorthand)', locator='(D1, 1.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100197', label='planning'), dict(scheme='cah', code='CAH13-01-04', label='planning (urban, rural and regional)')]),
        dict(name='Urban and Regional Planning', locator='(D1, 1.1)', kind='programme title',
             codes=[dict(scheme='hecos', code='100199', label='urban and regional planning')]),
        dict(name='Spatial Planning; Land-Use Planning; City Planning; Environmental Planning; Community Planning', locator='(D1, 1.1)', kind='programme title', codes=[]),
        dict(name='Planning combined with Real Estate, Architecture, Design or Geography', locator='(D1, 2.3)', kind='programme title', codes=[]),
        dict(name='specialist master\'s in a particular area of planning', locator='(D1, 1.17)', kind='specialism', codes=[]),
    ])

SECTIONS = {'1': 'Context and purposes of a Town and Country Planning degree',
            '2': 'Distinctive features of the Town and Country Planning degree',
            '3': 'Content, structure and delivery',
            '4': 'Benchmark standards'}
SUB = [('1.10', '1.14', 'Purposes and characteristics of a Town and Country Planning degree'),
       ('1.15', '1.22', 'Characteristics of a Town and Country Planning degree'),
       ('1.23', '1.29', 'Equality, diversity and inclusion'),
       ('1.30', '1.34', 'Accessibility'),
       ('1.35', '1.42', 'Sustainability'),
       ('1.43', '1.47', 'Enterprise and entrepreneurship education'),
       ('2.1', '2.4', 'Design'), ('2.5', '2.11', 'Progression'), ('2.12', '2.15', 'Flexibility'),
       ('2.16', '2.25', 'Partnership'), ('2.26', '2.30', 'Monitoring and review'),
       ('3.1', '3.9', 'Content'), ('3.10', '3.16', 'Teaching and learning'), ('3.17', '3.18', 'Assessment'),
       ('4.1', '4.5', 'Introduction'), ('4.6', '4.7', 'Threshold level'), ('4.8', '4.8', 'Typical level'),
       ('4.9', '4.9', 'Excellent level'), ('4.10', '4.10', "Integrated master's degrees")]

G = {
    '1.1': 'the field and its many course names', '1.2': 'planning serves what societies value',
    '1.3': 'issues planning is linked to (list)', '1.4': 'contested causes; contexts may change sharply',
    '1.5': 'an inter- and multi-disciplinary subject', '1.6': 'vocational aims; accreditation optional',
    '1.7': 'a broad reference, beyond accreditation outcomes', '1.8': 'international setting and devolved governance',
    '1.9': 'the four cross-cutting themes introduced', '1.10': 'creative proposals amid competing interests',
    '1.11': 'kinds of knowledge and the skills they build', '1.12': 'scholarship, practice and wider skills',
    '1.13': 'agile, curious planners for changing careers', '1.14': 'standards as a broad frame; harm and benefit',
    '1.15': 'planning as the study of managed change', '1.16': 'the academic core: why and how planning is done',
    '1.17': 'forms a degree course may take (list)', '1.18': "one-year master's, placements, apprenticeships",
    '1.19': "section 4 aimed at honours and integrated master's", '1.20': 'scholarship with practice; survey and data',
    '1.21': 'modes of study; fieldwork always included', '1.22': 'a frame for courses, not a method',
    '1.23': 'inclusive curriculum and belonging', '1.24': 'uneven growth and equitable places',
    '1.25': 'inclusion at different spatial scales', '1.26': 'inclusive design and co-creation',
    '1.27': 'principles for embedding inclusivity (list)', '1.28': 'diverse teaching methods and materials',
    '1.29': 'inclusive behaviours to foster (list)', '1.30': 'inclusive design for every learner need',
    '1.31': 'accessible environments and reasonable adjustments', '1.32': 'accessible settings beyond the campus',
    '1.33': 'varied methods; clear expectations', '1.34': 'flexible recruitment; seeing oneself in the curriculum',
    '1.35': 'sustainability throughout; critical view of the SDGs', '1.36': 'sustainability in policy and regulation',
    '1.37': 'sustainability defined broadly, over time and scale', '1.38': 'the four Ps',
    '1.39': 'critical debate on what sustainability means', '1.40': 'tensions between the three pillars',
    '1.41': 'interdisciplinary learning for sustainability', '1.42': 'embedding the SDGs in modules',
    '1.43': 'enterprise education and careers', '1.44': 'entrepreneurship and the values of planning',
    '1.45': 'modules on development business and climate', '1.46': 'enterprise in existing modules; digital tools',
    '1.47': 'case studies, problem-based learning, real projects',
    '2.1': 'theory balanced with practice', '2.2': 'professional bodies shape course design',
    '2.3': 'common features of structure (list)', '2.4': 'distinctive course features (list)',
    '2.5': 'progression towards the honours threshold', '2.6': 'joint and combined degrees',
    '2.7': "the integrated master's (MPlan)", '2.8': 'exit awards and course length by nation',
    '2.9': 'specialising as students progress', '2.10': 'growing complexity, judgement and independence',
    '2.11': 'doctoral study and researcher networks', '2.12': 'flexible structures and modes',
    '2.13': 'delivery modes and learning tools', '2.14': 'part-time, apprenticeship and sandwich routes',
    '2.15': 'accredited outcomes and room to specialise', '2.16': 'partnership at many scales',
    '2.17': 'partnerships with practitioners and employers', '2.18': 'employer input from every sector',
    '2.19': 'community and campaign groups', '2.20': 'kinds of partner contribution; study visits',
    '2.21': 'study abroad partnerships', '2.22': 'placements of varying length',
    '2.23': 'degree apprenticeship partnerships', '2.24': 'ethics and fairness in partnerships',
    '2.25': 'networks and learned societies', '2.26': 'monitoring, review and the student voice',
    '2.27': 'external reviewers in periodic review', '2.28': 'external examiners',
    '2.29': 'practitioners as external examiners', '2.30': 'accreditation review by the professional body',
    '3.1': 'the planner as broker, visionary and advocate', '3.2': 'place-based learning; individual and group work',
    '3.3': 'thematic groupings, not a fixed list; the SDGs', '3.4': 'five themes of content (list)',
    '3.5': 'causes and processes of environmental change', '3.6': 'the practice of planning',
    '3.7': 'debates in planning', '3.8': 'key planning skills', '3.9': 'specialist skills and knowledge',
    '3.10': 'teaching informed by research and practice', '3.11': 'education strategies; lifelong learning',
    '3.12': 'strategies designed with practitioners', '3.13': 'what teaching covers; practitioner input',
    '3.14': 'learning defined; varied approaches', '3.15': 'learning with stakeholders',
    '3.16': 'research skills and the student-led project', '3.17': 'authentic assessment',
    '3.18': 'range of assessment types (list)',
    '4.1': 'the three standards introduced', '4.2': 'most exceed threshold; Annex D',
    '4.3': 'standards apply to all of section 3', '4.4': 'the standards students are expected to reach',
    '4.5': 'the three standards defined', '4.6': 'threshold: five core themes',
    '4.7': 'threshold standards (list)', '4.8': 'typical standard', '4.9': 'excellent standard',
    '4.10': "integrated master's standards",
}
CTYPE = {'3.4': 'area', '3.5': 'area', '3.6': 'area', '3.7': 'area', '3.8': 'area', '3.9': 'area',
         '2.4': 'practice', '3.2': 'practice', '3.13': 'practice', '3.14': 'practice', '3.15': 'practice',
         '3.16': 'practice', '3.17': 'practice', '3.18': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2, S7 and SB6'),
    dict(number='none', heading='section heading lines (1 to 4)', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for SB6 and Part E'),
    dict(number='6', heading='Membership of the Advisory Group (2024, 2019, 2016, 2008, 2002); employer representation; copyright', kind='other: back matter, read for S8 and supersedes'),
]

P = {}
def s(i, **k):
    P[i] = k

# ------------------------------------------------------------ obliging or outcome paragraphs
NA_PROV = ('n/a', 'a duty on the provider; the student meets its effect, not a standard to reach')

s('1.8', type='expectation', rung='none', force='should', level='none', appliesTo='planning courses', addressee='provider',
  verbs=['reflect', 'take'], about='governance differences across nations and abroad', domain='none', award='none',
  para="Planning education reflects global, national and devolved systems of government, and courses should allow for how law, policy, governance and practice differ, to suit their focus, in an increasingly international setting.",
  prac="Courses should take account of how the UK nations and other countries differ in law, policy, governance and practice, as fits the course's focus, and reflect structures at global, national and devolved scales.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) on how a course handles differences between the UK nations and other countries, not as a learning outcome. {CITE('1.8')} Do not present it as a regulatory requirement or as tied to one award or level. Set it beside {T}4.7.b4 on the contexts of planning and {T}4.7.b5 on policy at different scales.",
  aad="Raise it with a programme team when a course recruits from several jurisdictions or teaches one nation's system alone. Put it in practitioner terms: the course should say which systems it covers and how it treats the rest. Ask which jurisdictions the core modules assume, and where students meet the differences. Avoid putting it to a student as something they must do.")

s('1.10', type='expectation', rung='none', force='should', level='none', appliesTo='planning degrees', addressee='both',
  verbs=['seek', 'develop'], about='critical understanding of the contexts of planning', domain='understanding', award='none',
  para="A planning degree should aim to build students' knowledge and critical grasp of the environmental, political, social, economic, legal and governance settings in which planning works, and of how its frameworks change at local, national and international scales.",
  prac="The course should set out to develop students' knowledge and critical understanding of the changing settings of planning, from law, policy and administration to ethics, culture and power, at every scale from local to international.",
  ben="Your course should help you build knowledge and a critical understanding of the political, social, economic, legal, environmental and ethical settings that planning works in, from local to international.",
  aaw=f"Describe this as an expectation (should) of what a planning degree sets out to develop, framed as the course's aim rather than a measured outcome. {CITE('1.10')} Do not present it as a threshold standard or as a regulatory requirement. Set it beside {T}4.7.b4, the threshold item on the contexts of planning, and {FH}4.15.b1 for the honours level of understanding.",
  aad="Raise it when a student asks why the course spends time on law, politics or economics, or when a team reviews how context is taught. With a student, say plainly that the course should help them understand the settings planning works in; with staff, frame it as a design aim. Ask which setting, legal, political or economic, the person finds hardest to read in a real case. Avoid reading the paragraph aloud or treating it as a test the student must pass.")

s('1.12', type='expectation', rung='none', force='should', level='none', appliesTo='planning degrees', addressee='both',
  verbs=['develop', 'placed', 'allowing'], about='wider skills and reflective, reflexive practice', domain='generic-skill', award='none',
  para="Planning degrees offer research and scholarship alongside professional growth and will build wider skills, among them negotiation, leadership, teamwork, communication, independent research and critical reflection; they should stress students becoming reflective and reflexive practitioners who grasp and act on the ethical demands of planning.",
  prac="Courses will develop negotiation, leadership, teamwork, communication, independent research and critical reflection, and should give weight to students growing into reflective and reflexive practitioners alert to the ethics of planning.",
  ben="Your course will help you build skills in negotiating, leading, working in teams, communicating, researching on your own and reflecting critically, and it should help you become a practitioner who questions your own part in planning and its ethics.",
  aaw=f"Describe this as an expectation (will, then should) of the wider skills and reflective practice a planning degree builds, not as one of the rung standards. {CITE('1.12')} Do not present it as a regulatory requirement or as a list a module must cover in full. Set it beside {T}4.7.b10 and {T}4.7.b11, and beside {AD}transferable/r5/3rd for reflection at honours level.",
  aad="Raise it when a student is preparing a reflective account or a team plans skills development across the years. With a student, talk about negotiating, leading, teamwork and reflection in their own experience; with staff, frame it as what the course should foster. Ask when the person last changed their mind about their own role in a planning decision, and why. Avoid presenting the whole list as a checklist every student must already meet.")

s('1.20', type='expectation', rung='none', force='should', level='none', appliesTo='planning courses', addressee='provider',
  verbs=['involve', 'consider', 'develop'], about='scholarship with practice; survey and data analysis', domain='none', award='none',
  para="Courses should normally combine scholarship with putting knowledge and skills to practical use, and should consider varied data sources and methods of analysis, with technology used rigorously and ethically, since planning rests on survey and analysis before plans and decisions; core learning usually comes before specialism.",
  prac="Courses should combine scholarship with practical application, and should teach survey and data analysis from varied sources, using technology with sound method and ethics; core knowledge and skills normally come before a specialism.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) about the balance of scholarship and practice and the teaching of data analysis. {CITE('1.20')} Do not present it as a learning outcome or as fixing a particular order of modules. Set it beside {T}4.7.b12 on research and evidence and {T}3.16 on research skills.",
  aad="Raise it with a programme team reviewing the balance of theory and practice or how survey and data methods are taught. Put it in practitioner terms: what mix of scholarship and application the course offers, and where data analysis is learned. Ask where students first collect and analyse their own data, and how its ethics are taught. Avoid giving it to a student as a duty of theirs.")

s('1.21', type='expectation', rung='none', force='should', level='none', appliesTo='planning courses in every mode', addressee='provider',
  verbs=['offered', 'develop', 'exposed', 'form'], about='interpersonal skills, real places and fieldwork', domain='none', award='none',
  para="Whatever the mode, full or part-time, in person or at a distance, students should get chances to build the interpersonal skills for work across professions and should meet real places in their full complexity; fieldwork, visits to sites and experiential learning should always feature in planning education.",
  prac="However the course is delivered, it should give students chances to develop interpersonal skills for cross-professional teamwork and to encounter real places, and fieldwork, visits and experiential learning should always be included.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) that every planning course, in any mode, includes fieldwork, visits and experiential learning and builds interpersonal skills. {CITE('1.21')} Do not present it as a regulatory requirement or as excusing distance courses from fieldwork. Set it beside {T}2.4 on distinctive features and {T}4.7.b11 on working across disciplines.",
  aad="Raise it when a team plans a distance or part-time route, or when fieldwork is under budget pressure. Put it in practitioner terms: the course should always offer fieldwork and real places, whatever the mode. Ask how a student on the most remote route meets real places and works with other professions. Avoid giving it to a student as something they must arrange.")

s('1.23', type='expectation', rung='none', force='describes', level='none', appliesTo='planning courses and their students', addressee='both',
  verbs=['underpinned', 'challenged', 'promote'], about='an inclusive curriculum and belonging', domain='none', award='none',
  para="Because graduates will practise in diverse societies, a barrier-free, inclusive curriculum is called essential, one that links employability to the careers of diverse groups and builds a learning community; students will be challenged to consider how to strengthen belonging for underrepresented groups.",
  prac="The text calls an inclusive curriculum essential: remove barriers so underrepresented groups can take full part, link employability to diverse students' careers and build a learning community in which students will be challenged to think about belonging.",
  ben="You will be asked to think about how places and professions can help people from underrepresented groups feel they belong, and to learn in a community that welcomes everyone.",
  aaw=f"Describe this as the statement's case for an inclusive curriculum; its word is 'essential', outside the usual modal words, so record it as described and do not turn it into a must. {CITE('1.23')} Do not present it as a regulatory or legal duty. Set it beside {T}1.25, {T}4.7.b7 on working with diverse groups and the theme record theme:edi.",
  aad="Raise it when a team reviews inclusion in the curriculum or a student asks how the course treats diversity. With a student, talk about belonging and about the communities they will plan for; with staff, frame it as a curriculum principle. Ask whose experience is missing from the case studies the course uses. Avoid reading the paragraph aloud or telling a student the course is failing them.")

s('1.25', type='expectation', rung='none', force='will', level='none', appliesTo='students of the subject', addressee='learner',
  verbs=['draw'], about='knowledge of particular groups at every scale', domain='knowledge', award='none',
  para="Students apply an inclusion lens at several spatial scales, from a site to the wider community, and will need to use knowledge particular to certain groups, such as how to remove barriers that keep underrepresented people from green space.",
  prac="Students will need to consider inclusion at different scales and draw on knowledge about particular groups, for example the barriers that people on low incomes, with health conditions or from minority ethnic backgrounds face in reaching green space.",
  ben="You will need to think about inclusion at every scale, from one site to a whole community, and use what is known about particular groups, such as what stops some people using green spaces.",
  aaw=f"Describe this as an expectation (will) that students apply knowledge of particular groups when judging inclusion at different scales. {CITE('1.25')} Do not present it as a threshold standard or as naming every group a course must cover. Set it beside {T}4.7.b7 and {T}4.7.b6, and beside {AD}knowledge/r1/3rd for knowledge at honours level.",
  aad="Raise it when a student is assessing a site or neighbourhood proposal. Put it in plain words and the second person: who might be shut out of this place, and what do you know about why. Ask which groups a proposal the student is working on would serve least well. Avoid lecturing on groups in general or reading the issuer's examples aloud as a fixed list.")

s('1.30', type='expectation', rung='none', force='should', level='none', appliesTo='course design', addressee='provider',
  verbs=['designed', 'recognising', 'taken', 'consider'], about='inclusive design for the full range of learner needs', domain='none', award='none',
  para="Courses should be designed inclusively for the whole range of learner needs, recognising that access differs between groups and people, and care should be taken over how environments, materials, assessment and support affect learners with protected characteristics, neurodivergent learners among them, and from different socio-economic backgrounds.",
  prac="Courses should be designed for the whole range of learner needs: accept that access looks different for different people, and check how environments, materials, assessment and support affect students with protected characteristics or from different socio-economic backgrounds.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) on inclusive course design. {CITE('1.30')} Do not present it as stating the provider's legal duties in full or as a student outcome. Set it beside {T}1.31 and {T}1.32 and the theme record theme:accessibility.",
  aad="Raise it with a programme team at design or review, especially when assessment methods change. Put it in practitioner terms: each part of the design should be checked for who it might exclude. Ask which assessment or setting in the course is hardest for a disabled or low-income student, and what has been done about it. Avoid putting it to a student as their responsibility.")

s('1.31', type='expectation', rung='none', force='should', level='none', appliesTo='learning environments and programmes', addressee='both',
  verbs=['benefit', 'seek', 'ensure'], about='accessible environments, adjustments and resources', domain='none', award='none',
  para="Every learning environment and set of materials should be open to learners with mobility or learning needs or with lived experience of disadvantage; students should receive reasonable adjustments for assessed needs, following national and institutional guidance, and programmes should try to give all students the facilities and resources to learn on and off campus.",
  prac="Learning spaces and materials should be accessible to learners with mobility or learning needs or lived experience of disadvantage; students should receive reasonable adjustments for assessed needs, and the programme should seek to give everyone the resources to learn on and off campus.",
  ben="If you have assessed needs, you should receive reasonable adjustments, and your learning spaces, materials and resources, on campus and off, should be open to you.",
  aaw=f"Describe this as an expectation (should) on accessible environments, adjustments and resources. {CITE('1.31')} Do not present it as a statement of the law on adjustments or as a learning outcome. Set it beside {T}1.30 and {T}1.32 and the theme record theme:accessibility.",
  aad="Raise it when a student mentions a barrier to learning, or a team plans materials or field trips. With a student, say plainly that they should get reasonable adjustments for assessed needs and point them to the service that arranges them; with staff, frame it as a design check. Ask what, if anything, stops the person using the course's spaces, materials or resources. Avoid deciding what adjustment a student needs.")

s('1.32', type='expectation', rung='none', force='should', level='none', appliesTo='all settings of planning teaching', addressee='provider',
  verbs=['taken', 'ensure'], about='accessible settings beyond the classroom', domain='none', award='none',
  para="Planning is taught in many settings, from campus rooms to site visits, field trips, placements, group and live projects and digital learning, and particular care should be taken that each is inclusive and fully accessible, physically, socially and financially.",
  prac="Particular care should be taken that site visits, field trips, placements, group and live projects and digital learning are inclusive and fully accessible, with physical, social and financial barriers all considered.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) that field, placement and digital settings are fully accessible. {CITE('1.32')} Do not present it as a student outcome or as forbidding any particular setting. Set it beside {T}1.21 on fieldwork and {T}1.31.",
  aad="Raise it when a team plans a field trip, placement or live project. Put it in practitioner terms: check the physical, social and financial barriers of each setting. Ask what a field trip costs a student and who might be unable to take part. Avoid giving it to a student as their duty.")

s('1.34', find='1.34 Recruitment to Town and Country Planning courses, including degree apprenticeship routes where appropriate, should be sufficiently flexible to enable learners with non-standard academic backgrounds or from groups underrepresented in higher education to flourish. In keeping with wider goals of diversifying professional practice in the built environment, course content should be designed to ensure that all members of the learning community can see themselves in the curriculum, have opportunities to learn about and from the diverse experiences of others, and are supported to explore the range of future career opportunities available to them.',
  type='expectation', rung='none', force='should', level='none', appliesTo='recruitment and course content', addressee='provider',
  verbs=['enable', 'designed', 'ensure', 'explore'], about='flexible recruitment and a curriculum students see themselves in', domain='none', award='none',
  para="Recruitment, apprenticeship routes included, should be flexible enough for learners from non-standard backgrounds or underrepresented groups to thrive, and content should be designed so that everyone recognises themselves in it, learns from others' varied experiences and is helped to explore future careers.",
  prac="Recruitment should be flexible for learners from non-standard or underrepresented backgrounds, and course content should be designed so that every student can recognise themselves in it, learn from others' experience and explore their career options.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) on flexible recruitment and a curriculum that reflects its students, in the service of a more diverse built environment profession. {CITE('1.34')} Do not present it as an admissions rule or a quota. Set it beside {T}1.23 and {T}2.23 on apprenticeships, and the theme records theme:accessibility and theme:edi.",
  aad="Raise it with a programme team reviewing admissions, case studies or careers support. Put it in practitioner terms: who gets in, who sees themselves in the content and who is helped towards which careers. Ask whether students from non-standard routes progress and find planning jobs as often as others. Avoid presenting it to a student as their responsibility.")

s('1.35', type='expectation', rung='none', force='should', level='none', appliesTo='providers delivering planning degrees', addressee='provider',
  verbs=['underpin', 'engage', 'promote'], about='sustainability and critical thinking on the SDGs', domain='none', award='none',
  para="Sustainability runs through the teaching and content of planning education, and those delivering planning degrees should engage with, and encourage critical thinking about, the UN SDGs, other frameworks and sustainability in general.",
  prac="Weave sustainability through the course: it should engage with the UN SDGs and other frameworks and encourage students to think critically about them and about sustainability in general.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) that a planning degree engages critically with the SDGs and sustainability. {CITE('1.35')} Do not present it as requiring uncritical adoption of the SDGs; the text asks for critical thinking. Set it beside {T}1.42, {T}4.7.b8 and std:doc:qaa-advancehe-esd-2021-guidance.",
  aad="Raise it when a team maps sustainability across modules or a student questions the SDGs. Put it in practitioner terms: the course should both use the goals and invite critique of them. Ask where students are asked to challenge, not only apply, a sustainability framework. Avoid giving it to a student as an obligation.")

s('1.42', find="1.42 Planning courses should consider how to embed approaches to teaching and learning that are linked to the UN SDGs across modules, working towards the SDGs and associated frameworks, including the QAA and Advance HE’s Education for Sustainable Development Guidance. Case studies, practical examples, live projects and placements can be used to embed sustainability practice in learning.",
  type='expectation', rung='none', force='should', level='none', appliesTo='planning courses', addressee='provider',
  verbs=['consider', 'embed', 'linked', 'used'], about='embedding the SDGs across modules', domain='none', award='none',
  para="Courses should consider how to build teaching and learning tied to the UN SDGs into modules, working towards the goals and related frameworks such as the joint ESD guidance, with live projects, placements, case studies and practical examples as means.",
  prac="Courses should consider how to embed SDG-linked teaching and learning across modules, drawing on the joint ESD guidance and using live projects, placements, case studies and practical examples.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should consider) on embedding the SDGs, which leaves the means to the course. {CITE('1.42')} Do not present it as requiring a dedicated sustainability module. Set it beside {T}1.35 and std:doc:qaa-advancehe-esd-2021-guidance, which it names.",
  aad="Raise it when a team reviews modules for sustainability content. Put it in practitioner terms: which modules link to which goals, and through what activities. Ask which live project or placement in the course carries sustainability practice most directly. Avoid presenting it to a student as a duty.")

s('2.6', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of joint or combined degrees', addressee='learner',
  verbs=['achieve', 'add', 'explore'], about='joint and combined honours', domain='none', award=HON,
  para="Students on joint or combined degrees will gain the core subject-specific and generic skills set out in the statement and add others from their second subject, and may explore where the disciplines meet.",
  prac="Joint and combined honours students will reach the core planning skills, specific and generic, and add skills from their other subject, with scope to work where the disciplines overlap.",
  ben="If you study planning with another subject, you will gain the core planning skills, both those particular to planning and the wider ones, add skills from your other subject and can explore where the two meet.",
  aaw=f"Describe this as an expectation (will) for joint and combined honours students at FHEQ level 6: they reach the core planning skills, not every specialist one. {CITE('2.6')} Do not claim that joint honours students meet the full single honours range. Set it beside the threshold list {T}4.7.b1 to {T}4.7.b13 and {FH}4.15.b1.",
  aad="Raise it when a joint honours student worries they are learning less planning than single honours peers, or a team designs a combined route. With a student, say they will gain the core planning skills and others from their second subject; with staff, frame it as what the core must protect. Ask which core planning skills the student's route covers fully, and which it covers lightly. Avoid implying a joint degree is a lesser award.")

s('2.10', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students progressing through the degree', addressee='learner',
  verbs=['demonstrate', 'acknowledge'], about='progression in judgement, independence and theory with practice', domain='subject-skill', award=HON,
  para="As they progress, students' understanding of places grows more complex and critical and takes more account of stakeholders; they will show a growing grasp of the subtlety needed for situated, evidenced judgements on spatial and non-spatial questions, increasing independence in fieldwork and projects and an understanding that planning theory and practice form one continuing cycle of inquiry, reflection and improvement.",
  prac="Plan progression so that students will show more complex and critical understanding of places and stakeholders, finer situated and evidence-based judgement on spatial and non-spatial matters, more independence in fieldwork and projects using primary or secondary data and a sense of theory and practice as one cycle.",
  ben="As you move through your course, you will make more careful judgements about places, grounded in evidence and context, carry out fieldwork and projects more independently and come to see planning theory and practice as one cycle of asking, acting and reflecting.",
  aaw=f"Describe this as an expectation (will) of how students progress across an honours degree towards FHEQ level 6, not as a threshold item. {CITE('2.10')} Do not present the topics it gives as examples (young people and climate change, ageing in place, AI) as required content. Set it beside {T}4.7.b2 and {T}4.7.b12, {FH}4.15.b7 and spine:6.",
  aad="Raise it when a student reflects on how their work has changed between years, or a team plans progression in fieldwork and projects. With a student, ask them to compare an early judgement with a recent one; with staff, frame it as the shape of progression. Ask how much of the student's latest fieldwork they planned themselves. Avoid treating the end of the progression as expected in the first year.")

s('2.27', type='expectation', rung='none', force='will', level='none', appliesTo='providers in periodic review', addressee='provider',
  verbs=['use', 'ensure', 'achieved'], about='external reviewers in periodic review', domain='none', award='none',
  para="Externality is central to UK quality assurance: providers will bring in external reviewers during periodic review for an outside view on proposed changes and to make sure threshold standards are met and content suits the subject.",
  prac="In periodic review, the provider will use external reviewers to give an outside view on changes and to confirm that threshold standards are met and content suits the subject.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (will) about external review in periodic course review. {CITE('2.27')} Do not present it as a regulator's rule or a student outcome. Set it beside {T}2.28 on external examiners and {T}4.2 on evidence of achievement.",
  aad="Raise it with a programme team preparing for periodic review. Put it in practitioner terms: who the external reviewers are and what they are asked to confirm. Ask whether the review panel includes a practitioner as well as an academic. Avoid putting it to a student.")

s('3.12', type='expectation', rung='none', force='should', level='none', appliesTo='learning, teaching and assessment strategies', addressee='provider',
  verbs=['designed', 'combining', 'underpins'], about='teaching designed with practitioners', domain='none', award='none',
  para="To bring theory and practice together, teaching and learning strategies should be designed jointly by planning academics and practitioners, joining theoretical ideas to real-life processes in an inclusive pedagogy centred on the student, with sustainability underpinning every pedagogic choice.",
  prac="Teaching and learning strategies should be designed by academics and practitioners together, linking theory to real-life processes in an inclusive, student-centred way, with sustainability behind every choice.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) that teaching strategies are co-designed with practitioners. {CITE('3.12')} Do not present it as requiring practitioners in every module. Set it beside {T}3.13, {T}3.15 and {T}1.35.",
  aad="Raise it with a programme team reviewing who designs teaching. Put it in practitioner terms: where practitioners shape the strategy, not only deliver guest sessions. Ask which module was last redesigned with a practitioner, and what changed. Avoid giving it to a student as a duty.")

s('3.13', type='expectation', rung='none', force='should', level='none', appliesTo='teaching', addressee='provider',
  verbs=['encourage', 'enabling'], about='practitioner involvement in teaching', domain='none', award='none',
  para="Teaching spans curriculum design, content, assessment, moderation and reflection, and the process, above all the delivery of content, should draw professional practitioners in actively so that real-world problems are tackled.",
  prac="Teaching, especially the delivery of content, should actively involve professional practitioners so that real-world problems are addressed.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) that practitioners take an active part in teaching. {CITE('3.13')} Do not present it as a student outcome. Set it beside {T}3.12 and {T}2.4.",
  aad="Raise it when a team plans guest contributors, live briefs or studio teaching. Put it in practitioner terms: how practitioners bring real problems into the course. Ask which real-world problem from practice the students tackled this year. Avoid putting it to a student as their duty.")

s('3.14', type='expectation', rung='none', force='describes', level='none', appliesTo='teaching approaches', addressee='provider',
  verbs=['used', 'accommodate'], about='varied pedagogies for diverse learners', domain='none', award='none',
  para="Learning is change in a person through new information, understanding, skills, attitudes and behaviour, so varied teaching approaches are called for, suited to different learning styles and to hybrid, analogue and digital modes.",
  prac="Use a variety of teaching approaches to suit different learning styles and hybrid, analogue and digital modes; the text's wording ('are to be used') is obliging but not one of the usual modals.",
  ben=NA_PROV,
  aaw=f"Describe this as the statement's call for varied pedagogy; its wording 'are to be used' is recorded as described, not as must or should. {CITE('3.14')} Do not present it as a regulatory requirement. Set it beside {T}1.33 and {T}3.15.",
  aad="Raise it when a team relies on one teaching format or moves between in-person and online delivery. Put it in practitioner terms: which approaches the course uses for which learners. Ask which students the current mix of formats suits least. Avoid giving it to a student as a duty.")

s('3.15', type='expectation', rung='none', force='should', level='none', appliesTo='learning opportunities', addressee='provider',
  verbs=['involve', 'encouraged'], about='learning with stakeholders', domain='none', award='none',
  para="Learning opportunities should involve students actively with a range of stakeholders and may take in co-creation with academics or practitioners, interdisciplinary work, workplaces, scenario projects, simulations, problem-solving and community participation, alone and in groups; such a mix, which widens understanding of social, attitudinal and physical barriers, should be encouraged.",
  prac="Learning should actively involve stakeholders, through co-creation, interdisciplinary work, workplaces, scenarios, simulations and community participation, individually and in groups, and that mix should be encouraged.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) that learning involves stakeholders, with the forms listed as options (may). {CITE('3.15')} Do not present every listed form as required. Set it beside {T}3.12, {T}2.4 and {T}4.7.b7.",
  aad="Raise it when a team designs projects or simulations. Put it in practitioner terms: which stakeholders students meet, and in what roles. Ask when students last worked with a community group rather than only studying one. Avoid treating the list of forms as a checklist.")

s('3.16', find='3.16 Research skills are an important part of the educational journey across a programme of study. They are also important for Planning practice, given the need to understand the built and natural environments and their socio-economic contexts before considering any interventions. Students can develop their investigative skills to demonstrate independence through a student-led research or design project. They are challenged to think in critical, creative and applied ways and may devise research questions, design and conduct a research methodology, and potentially produce original knowledge which will be important to the discipline. As well as conducting their own project, students will communicate their research to academic and/or professional communities using professional communication skills and methods.',
  type='outcome', rung='none', force='will', level='none', appliesTo='students of the subject', addressee='learner',
  verbs=['communicate', 'develop', 'devise', 'design', 'conduct'], about='research skills and communicating research', domain='subject-skill', award='none',
  para="Research skills matter throughout the course and in practice, since places and their contexts need understanding before any intervention; through a research or design project they lead, students show independence and may frame questions and design a method; they will present their research to academic or professional audiences in a professional manner.",
  prac="Give students a student-led research or design project in which they can frame questions and choose a method; they will communicate their research to academic or professional audiences with professional skills.",
  ben="You will develop research skills, often through a research or design project you lead yourself, and you will present your findings to academic or professional audiences in a professional way.",
  aaw=f"Describe this as an expectation (will) that students communicate their own research to academic or professional audiences; framing questions and producing original knowledge are possibilities (may, potentially), not requirements. {CITE('3.16')} Do not claim that every student produces original knowledge. Set it beside {T}4.7.b12, {T}4.10.b4 and {FH}4.15.b6.",
  aad="Raise it when a student is choosing or planning a dissertation or design project. With a student, talk plainly about their own question, method and who will hear the results; with staff, frame it as what the project should lead to. Ask who outside the university would want to hear the student's findings, and in what form. Avoid suggesting the project must produce new knowledge to pass.")

s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['refer', 'perform'], about='evidence of achievement and Annex D', domain='none', award=HON,
  para="Most students will do considerably better than the minimum threshold; each provider decides what counts as evidence of achievement and should refer to Annex D of the qualifications frameworks, which describes the four honours classifications.",
  prac="Decide your own evidence of achievement, referring as you should to Annex D, which describes the four honours classifications; expect most students to exceed the threshold.",
  ben=NA_PROV,
  aaw=f"Describe this as a provider expectation (should) to refer to Annex D when deciding evidence of achievement for honours classes. {CITE('4.2')} Do not present Annex D as part of this statement or the threshold as the usual result. Set it beside std:doc:qaa-fheq-2024-framework, Annex D ({AD}summary/r1/3rd to {AD}summary/r1/1st) and {T}4.5.",
  aad="Raise it with a programme team aligning marking criteria with honours classes. Put it in practitioner terms: how the course's criteria read against Annex D. Ask how the course tells a 2.1 from a 2.2 in a planning report. Avoid putting it to a student as their duty.")

s('4.4', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['achieve', 'demonstrate', 'apply'], about='the standards students are expected to reach', domain='none', award=HON,
  para="Students are expected to reach these standards in a planning degree and should show that they understand them and can apply them as fits their work.",
  prac="Students should show that they understand the standards and can apply them as fits; these are the standards a planning degree expects them to reach.",
  ben="You are expected to reach these standards in your degree, and you should be able to show you understand them and can put them to use where they apply.",
  aaw=f"Describe this as an expectation (should) that students understand and can apply the section 4 standards. {CITE('4.4')} Do not present it as a further standard in its own right. Set it beside the threshold list {T}4.7.b1 to {T}4.7.b13 and {T}4.5.",
  aad="Raise it when a student asks what the course expects of them by graduation. With a student, say plainly that they should understand the standards and be able to use them; with staff, frame it as the purpose of sharing the standards with students. Ask which of the standards the student could show evidence for today. Avoid reading the whole of section 4 aloud.")

# ------------------------------------------------------------ threshold (4.6 lead-in, 4.7 list)
def aaw_t(n, beside):
    return (f"Describe this as a threshold standard: the minimum a graduate must show to gain a bachelor's degree with honours in planning, at FHEQ level 6 (FQHEIS level 10). "
            f"{CITE(n)} Do not present it as a regulatory requirement, as the typical or excellent standard or as the integrated master's standard. Set it beside {beside}.")

def aad_t(when, q):
    return (f"Raise it when {when}. With a student, say in plain words and the second person what they need to show at the minimum; with staff, frame it as what every graduate must reach. "
            f"Ask {q} Avoid reading the item aloud at length or treating the typical or excellent standards as the minimum.")

BT = "To reach the minimum for your honours degree, "
def th(i, **k):
    s('4.7.b%d' % i, type='threshold', rung='threshold', force='threshold', forceFrom='4.6', level='fheq:6',
      appliesTo='graduates at the threshold standard', addressee='learner', award=HON, **k)

th(1, verbs=[], about='interlinked interventions and environments', domain='understanding',
   para="At threshold, graduates understand how planning interventions connect with one another and how they act on built and natural environments.",
   prac="At the minimum, graduates grasp that planning interventions are interlinked and affect both built and natural environments.",
   ben=BT + "you will understand how planning interventions link together and how they affect built and natural environments.",
   aaw=aaw_t('4.7', f"{T}4.8.b1 and {T}4.9.b1, {FH}4.15.b1 and {AD}knowledge/r1/3rd"),
   aad=aad_t("a student asks what joined-up thinking about interventions means, or a team maps a first module on the environment", "can the person trace how one intervention they have studied changed both the built and the natural environment?"))
th(2, verbs=['identify', 'resolve'], about='solving problems with planning tools and processes', domain='subject-skill',
   para="At threshold, graduates can find and settle problems using the tools and processes of planning.",
   prac="At the minimum, graduates identify problems and resolve them with planning tools and processes.",
   ben=BT + "you will be able to spot problems and resolve them with planning's tools and processes.",
   aaw=aaw_t('4.7', f"{T}4.8.b2, {FH}4.15.b7 and {AD}cognitive/r3/3rd"),
   aad=aad_t("a student is working on a problem-based or live project, or a team writes a studio brief", "which planning tool or process did the person use on the last problem they tackled, and why that one?"))
th(3, verbs=['relate'], about='planning theory and its link to practice', domain='knowledge',
   para="At threshold, graduates know the theories of planning and the case made for its role in society, and how best to link theory to practice.",
   prac="At the minimum, graduates know planning theory, why planning exists and how theory bears on practice.",
   ben=BT + "you will know the main theories of planning, why societies plan and how theory connects to what planners do.",
   aaw=aaw_t('4.7', f"{T}4.7.b10, {FH}4.15.b1 and {AD}knowledge/r2/3rd"),
   aad=aad_t("a student finds theory remote from practice, or a team reviews a theory module", "for one theory of planning, what case does it make, and how would it change what a planner does?"))
th(4, verbs=['act'], about='the contexts and actors of planning', domain='knowledge',
   para="At threshold, graduates know the legal, political, economic, social and institutional settings of planning, the relative power of those involved and how planners can act within them.",
   prac="At the minimum, graduates know the legal, political, economic, social and institutional contexts of planning, who holds power in them and how planners can work within them.",
   ben=BT + "you will know the legal, political, economic, social and institutional settings planning works in, who holds power there and how planners can act.",
   aaw=aaw_t('4.7', f"{T}4.7.b5 and {T}1.10, {FH}4.15.b1 and {AD}knowledge/r1/3rd"),
   aad=aad_t("a student asks why the same proposal fares differently in different places, or a team plans teaching on governance", "who held most power in a planning decision the person has studied, and what room did the planner have?"))
th(5, verbs=['framing', 'made', 'shape'], about='policy and how it is made', domain='knowledge',
   para="At threshold, graduates know what policy is, how it frames action at different scales, how planning policy comes about and how far it can shape outcomes.",
   prac="At the minimum, graduates know how policy frames action across scales, how planning policy is made and what it can achieve.",
   ben=BT + "you will know how planning policy is made, how it guides action at different scales and how much difference it can make.",
   aaw=aaw_t('4.7', f"{T}4.7.b4, {FH}4.15.b1 and {AD}knowledge/r1/3rd"),
   aad=aad_t("a student is writing about a local plan or national policy, or a team plans a policy module", "how was a policy the person has studied made, and what difference did it make on the ground?"))
th(6, verbs=['making', 'consider'], about='sustainable, inclusive places; design and finance', domain='understanding',
   para="At threshold, graduates understand planning's part in creating sustainable and inclusive places, what design and finance add to that and why the needs of different groups count.",
   prac="At the minimum, graduates understand how planning, with design and finance, makes sustainable and inclusive places for different groups.",
   ben=BT + "you will understand how planning, helped by design and finance, creates places that are sustainable and work for different groups of people.",
   aaw=aaw_t('4.7', f"{T}4.7.b7 and {T}4.7.b8, {AD}knowledge/r1/3rd, and the theme records theme:esd and theme:edi"),
   aad=aad_t("a student works on a design or development project, or a team reviews how sustainability and inclusion run through the course", "in a scheme the person has studied, how did design and finance help or hinder a place that works for different groups?"))
th(7, verbs=['work'], about='planning, communities and diverse groups', domain='understanding',
   para="At threshold, graduates understand how planning relates to communities and affects people and places, and how to work well with varied groups.",
   prac="At the minimum, graduates understand planning's relationship with communities and its effects, and how to work with diverse groups.",
   ben=BT + "you will understand how planning affects people and places and how to work well with the many different groups in a community.",
   aaw=aaw_t('4.7', f"{T}4.7.b6 and {T}1.25, and {AD}transferable/r2/3rd"),
   aad=aad_t("a student prepares for consultation or community engagement work", "whose voices were missing from an engagement exercise the person has seen, and how would they reach them?"))
th(8, verbs=['tackle', 'meeting'], about='planning, climate and biodiversity', domain='knowledge',
   para="At threshold, graduates know how planning can address the climate and biodiversity crises, for instance through infrastructure that helps reach climate goals.",
   prac="At the minimum, graduates know what planning can do about climate change and biodiversity loss, including through infrastructure.",
   ben=BT + "you will know how planning can help deal with climate change and the loss of nature, for example through the infrastructure it plans.",
   aaw=aaw_t('4.7', f"{T}4.7.b6 and {T}1.35, std:doc:qaa-advancehe-esd-2021-guidance and {AD}knowledge/r1/3rd"),
   aad=aad_t("a student studies climate adaptation, green infrastructure or nature recovery", "what could a plan the person knows do differently to cut emissions or restore nature?"))
th(9, verbs=['carried'], about='technology and digital settings in planning', domain='subject-skill',
   para="At threshold, graduates can use technology in planning and appreciate the digital settings in which planning now takes place.",
   prac="At the minimum, graduates use planning technology and understand the digital environments planning works in.",
   ben=BT + "you will be able to use technology in planning and understand the digital settings planning now works in.",
   aaw=aaw_t('4.7', f"{AD}practical/r1/3rd and {AD}transferable/r1/3rd"),
   aad=aad_t("a student learns mapping, digital engagement or other planning software, or a team reviews digital skills", "which digital tools has the person used in planning work, and where did those tools help or mislead?"))
th(10, verbs=['upholding'], about='values, ethics and the profession', domain='understanding',
   para="At threshold, graduates understand why values and ethics matter to planning practice and the profession's part in upholding them.",
   prac="At the minimum, graduates understand the place of values and ethics in planning and the profession's role in keeping them.",
   ben=BT + "you will understand why values and ethics matter in planning and how the profession keeps to them.",
   aaw=aaw_t('4.7', f"{T}1.12 and {T}4.10.b2, and {AD}professional/r2/3rd-1st"),
   aad=aad_t("a student meets an ethical dilemma in a project or placement, or a team plans teaching on professional ethics", "what would the person do if a client's interest clashed with the public interest in a scheme?"))
th(11, verbs=['working'], about='working across disciplines and professions', domain='generic-skill',
   para="At threshold, graduates understand how planning relates to other professions and disciplines and why working well across their boundaries matters.",
   prac="At the minimum, graduates understand planning's ties to other fields and the value of effective work across disciplines.",
   ben=BT + "you will understand how planning connects with other professions and why working well with them matters.",
   aaw=aaw_t('4.7', f"{T}4.10.b3, {AD}transferable/r2/3rd, {FH}4.15.b9.2 and spine:6"),
   aad=aad_t("a student works with architecture, surveying or engineering students, or a team plans an interdisciplinary project", "what did another profession bring to a project the person worked on that planning could not?"))
th(12, verbs=['drawing'], about='research, evidence and weighing alternatives', domain='subject-skill',
   para="At threshold, graduates understand why research matters to good planning, use evidence from varied sources and judge alternative policies and arguments.",
   prac="At the minimum, graduates value research in planning, use evidence from a range of sources and evaluate competing policies and arguments.",
   ben=BT + "you will understand why research matters in planning, use evidence from many sources and weigh up different policies and arguments.",
   aaw=aaw_t('4.7', f"{T}4.10.b4 and {T}3.16, {FH}4.15.b3.2, {FH}4.15.b5 and {AD}knowledge/r3/3rd"),
   aad=aad_t("a student plans a dissertation or an evidence base, or a team reviews research teaching", "what evidence would change the person's mind about the policy option they favour?"))
th(13, find='the ability to effectively communicate through written, graphic, numerical and digital means (PS/TS).',
   verbs=['communicate'], about='communicating in written, graphic, numerical and digital forms', domain='generic-skill',
   para="At threshold, graduates communicate well in writing, graphics, numbers and digital media.",
   prac="At the minimum, graduates communicate effectively in writing, visually, numerically and digitally.",
   ben=BT + "you will be able to get your ideas across clearly in writing, drawings and graphics, numbers and digital media.",
   aaw=aaw_t('4.7', f"{FH}4.15.b8, {AD}transferable/r1/3rd and {AD}practical/r4/3rd"),
   aad=aad_t("a student prepares a report, plan, presentation or poster", "which of writing, graphics, numbers and digital media does the person find hardest, and what would strengthen it?"))

# ------------------------------------------------------------ typical (4.8) and excellent (4.9)
def aaw_r(rung, n, beside):
    what = {'typical': "a typical standard: what most honours graduates in planning reach, beyond the threshold; an expectation, not a requirement",
            'excellent': "an excellent standard: what the strongest honours graduates in planning show, beyond the typical; an aspiration, not a requirement"}[rung]
    return (f"Describe this as {what}, at FHEQ level 6 (FQHEIS level 10). {CITE(n)} "
            f"Do not present it as the minimum for the award or as a regulatory requirement. Set it beside {beside}.")

def aad_r(rung, when, q):
    return (f"Raise it when {when}. With a student, put it in plain words and the second person as what {'most graduates reach' if rung == 'typical' else 'the best work shows'}; with staff, frame it as the level above {'the threshold' if rung == 'typical' else 'the typical'}. "
            f"Ask {q} Avoid presenting it as the minimum a student must reach.")

s('4.8.b1', type='typical', rung='typical', force='will', level='fheq:6', appliesTo='graduates at the typical standard', addressee='learner', award=HON,
  verbs=[], about='going beyond the threshold across the core themes', domain='knowledge',
  para="At the typical standard, graduates meet every threshold criterion and will also go further than the minimum in what they know and understand, in thinking and practical skills and in professional competence.",
  prac="Typical graduates will meet all threshold criteria and go further in knowledge, cognitive and practical skills and professional competence.",
  ben="To reach the standard most students reach, you will meet every minimum criterion and go further in what you know, how you think, your practical skills and your professional competence.",
  aaw=aaw_r('typical', '4.8', f"the threshold list {T}4.7.b1 to {T}4.7.b13, {T}4.9.b1, and {AD}knowledge/r1/2.2 and {AD}knowledge/r1/2.1"),
  aad=aad_r('typical', "a student asks what a good degree looks like beyond a pass, or a team writes criteria for the middle classes", "where in one recent piece of work did the person go further than simply meeting the criteria?"))
s('4.8.b2', find='some critical discernment, insight, initiative, creativity and autonomy through effective and appropriate application of the criteria.',
  type='typical', rung='typical', force='will', level='fheq:6', appliesTo='graduates at the typical standard', addressee='learner', award=HON,
  verbs=[], about='some critical judgement, initiative, creativity and autonomy', domain='generic-skill',
  para="At the typical standard, graduates will also show some critical judgement, insight, initiative, creativity and independence in applying the criteria well and fittingly.",
  prac="Typical graduates will show some critical discernment, insight, initiative, creativity and autonomy in how they apply the criteria.",
  ben="To reach the standard most students reach, you will show some critical judgement, insight, initiative, creativity and independence in how you apply what you have learned.",
  aaw=aaw_r('typical', '4.8', f"{T}4.9.b2, {FH}4.15.b9.1, {AD}cognitive/r4/2.2 and {AD}transferable/r4/2.2"),
  aad=aad_r('typical', "a student wants to move from competent to good work", "where did the person take the initiative or try a creative approach in their last project?"))
s('4.9.b1', type='excellent', rung='excellent', force='will', forceFrom='4.1', level='fheq:6', appliesTo='graduates at the excellent standard', addressee='learner', award=HON,
  verbs=['listed'], about='excellence across all criteria', domain='knowledge',
  para="At the excellent standard, graduates, having met the threshold and typical standards, understand and apply every criterion and will have taken their knowledge, thinking, practical skills and professional competence further than the typical level, to an excellent degree.",
  prac="Excellent graduates will understand and apply all the criteria and develop knowledge, cognitive and practical skills and professional competence to an excellent level, beyond the typical.",
  ben="To reach the highest standard, you will understand and use every criterion and take your knowledge, thinking, practical skills and professional competence well beyond the usual level.",
  aaw=aaw_r('excellent', '4.9', f"{T}4.8.b1, {AD}knowledge/r1/1st and {AD}cognitive/r1/1st"),
  aad=aad_r('excellent', "a student aims for a first or asks what marks out the best work", "which criterion does the person's strongest work already exceed, and which holds them back?"))
s('4.9.b2', type='excellent', rung='excellent', force='will', forceFrom='4.1', level='fheq:6', appliesTo='graduates at the excellent standard', addressee='learner', award=HON,
  verbs=[], about='excellent critical judgement, insight, creativity and autonomy', domain='generic-skill',
  para="At the excellent standard, graduates apply the criteria fluently and with sophistication and will show excellent critical judgement, insight, creativity and independence.",
  prac="Excellent graduates will apply the criteria fluently and with sophistication, and their critical discernment, insight, creativity and autonomy will be of a high order.",
  ben="To reach the highest standard, you will apply what you have learned fluently and with sophistication, showing outstanding critical judgement, insight, creativity and independence.",
  aaw=aaw_r('excellent', '4.9', f"{T}4.8.b2, {AD}cognitive/r4/1st, {AD}cognitive/r3/1st and {AD}transferable/r3/1st"),
  aad=aad_r('excellent', "a student is ready to stretch beyond good work, or a team writes criteria for a first", "where has the person made an independent judgement that went beyond what they were taught?"))

# ------------------------------------------------------------ integrated master's (4.10)
def aaw_m(beside):
    return ("Describe this as an added standard for the integrated master's in planning (MPlan) at FHEQ level 7 (FQHEIS level 11): graduates will show it on top of the typical bachelor's standard. "
            f"{CITE('4.10')} Do not present it as a regulatory requirement, as a standard for one-year taught master's courses or as part of the bachelor's standards. Set it beside {beside}.")

def aad_m(when, q):
    return (f"Raise it when {when}. With a student, say in plain words and the second person what the extra master's year should add; with staff, frame it as what lifts the award above the honours degree. "
            f"Ask {q} Avoid treating it as expected of bachelor's students.")

def ma(i, **k):
    s('4.10.b%d' % i, type='threshold', rung='threshold', force='will', level='fheq:7',
      appliesTo="graduates of integrated master's degrees", addressee='learner', award=MAS, **k)

ma(1, verbs=[], about='in-depth specialist knowledge', domain='knowledge',
   para="Integrated master's graduates will, beyond the typical bachelor's standard, show deep knowledge of at least one specialist field of planning activity and practice.",
   prac="Integrated master's graduates will show in-depth knowledge of at least one specialist field of planning activity and practice.",
   ben="On an integrated master's, you will build deep knowledge of at least one specialist area of planning and its practice.",
   aaw=aaw_m(f"{T}3.9 and {T}4.8.b1, {FH}4.17.b1 and spine:7"),
   aad=aad_m("a student chooses a specialism in the master's year", "which specialist area does the person want to know in depth, and what would show that depth?"))
ma(2, verbs=[], about='professional working, roles, ethics and values', domain='understanding',
   para="Integrated master's graduates will show a good grasp of how professionals work and the roles and responsibilities they hold, along with professional ethics and values.",
   prac="Integrated master's graduates will understand well how planners work and the roles and responsibilities they hold, along with the ethics and values of the profession.",
   ben="On an integrated master's, you will gain a good understanding of how planners work and the roles and responsibilities they carry, along with the ethics and values of the profession.",
   aaw=aaw_m(f"{T}4.7.b10, {FH}4.17.b8.1 and {AD}professional/r1/3rd-1st"),
   aad=aad_m("a student prepares for placement or professional membership", "what responsibilities would the person carry in a first planning post, and which ethical tension would they expect to meet?"))
ma(3, verbs=['undertaking', 'working'], about='professionalism in assignments and group work', domain='generic-skill',
   para="Integrated master's graduates will show a high level of professionalism in carrying out assignments and in group work.",
   prac="Integrated master's graduates will work with a high degree of professionalism on assignments and in groups.",
   ben="On an integrated master's, you will handle assignments and group work with a high level of professionalism.",
   aaw=aaw_m(f"{T}4.7.b11, {FH}4.17.b6 and {FH}4.17.b8.2"),
   aad=aad_m("a group project runs into difficulty or a team designs master's-level group work", "what would a client notice about how the person's group worked?"))
ma(4, verbs=['conduct'], about='data and independent research', domain='subject-skill',
   para="Integrated master's graduates will use data collection and analysis effectively and be able to carry out independent research in planning.",
   prac="Integrated master's graduates will collect and analyse data effectively and conduct independent research in planning studies.",
   ben="On an integrated master's, you will collect and analyse data effectively and carry out your own research in planning.",
   aaw=aaw_m(f"{T}4.7.b12 and {T}3.16, {FH}4.17.b2 and {FH}4.17.b4.2"),
   aad=aad_m("a student plans the master's dissertation", "what data will the person collect, and how will they know their analysis is sound?"))

# gradeOf: the typical and excellent items are two broad items each, in the same order; content plainly matches
GRADE = {'4.9.b1': '4.8.b1', '4.9.b2': '4.8.b2'}

TH = {'1.23': 'theme:edi', '1.25': 'theme:edi', '1.30': 'theme:accessibility', '1.31': 'theme:accessibility',
      '1.32': 'theme:accessibility', '1.34': 'theme:accessibility', '1.35': 'theme:esd', '1.42': 'theme:esd'}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.5'), dict(id='fqheis:10', role='cites', locator='D1, 2.5'),
            dict(id='fheq:7', role='cites', locator='D1, 2.7'), dict(id='fqheis:11', role='cites', locator='D1, 2.7'),
            dict(id='fheq:4', role='inferred', locator="D1, 2.8: CertHE named as an exit award; level from std:doc:qaa-fheq-2024-framework, Table 1 (Part E)"),
            dict(id='fheq:5', role='inferred', locator="D1, 2.8: DipHE named as an exit award; level from std:doc:qaa-fheq-2024-framework, Table 1 (Part E)"),
            dict(id='spine:6', role='inferred', locator='std:ref:uk-framework R2, for the honours standards'),
            dict(id='spine:7', role='inferred', locator="std:ref:uk-framework R2, for the integrated master's standards")],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.5: "FHEQ Level 6; FQHEIS Level 10", for the degree with honours)'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.7, for the integrated master\'s); the shared descriptor per std:doc:qaa-fheq-2024-framework S5')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['front matter', '1.9', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28', '1.29', '1.34', '2.23', '4.7']),
      dict(id='theme:accessibility', role='carries', carriedIn=['front matter', '1.9', '1.27', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '3.6']),
      dict(id='theme:esd', role='carries', carriedIn=['front matter', '1.9', '1.35', '1.36', '1.37', '1.38', '1.39', '1.40', '1.41', '1.42', '3.3', '3.12', '4.7']),
      dict(id='theme:enterprise', role='carries', carriedIn=['front matter', '1.9', '1.43', '1.44', '1.45', '1.46', '1.47'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-town-and-country-planning-2019-benchmarks (not held)', note='the fourth edition, 2019; this is the fifth (D1, back matter)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree classification descriptions (4.2); FHEQ levels 6 and 7 (2.5, 2.7)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS levels 10 and 11 (2.5, 2.7)'),
      dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='named at 1.42'),
      dict(rel='readWith', target='std:doc:qaa-housing-studies-2022-benchmarks', note='front matter: other relevant statements to reference'),
      dict(rel='readWith', target='std:doc:qaa-land-construction-real-estate-and-surveying-2024-benchmarks', note='front matter: other relevant statements to reference'),
      dict(rel='refersTo', target='RTPI learning outcomes for initial planning education and accreditation (not yet ingested: Part E)', note='2.2, 2.15, 2.30'),
      dict(rel='refersTo', target='Chartered Town Planner Degree Apprenticeship Standard (not yet ingested: Part E)', note='1.18, 2.23'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance (not yet ingested)', note='front matter')]

SB1 = [
    'Planning is the study of how societies plan, design, manage and regulate change in built and natural environments, and of why and how they intervene and with what effects (D1, 1.15, 1.16).',
    'Its academic core is the rationale for planning and how it is practised, taking in land and property markets, design and place-making, ecology and geography (D1, 1.16).',
    'It is inter- and multi-disciplinary and holistic, drawing on the social sciences and on environmental and design disciplines (D1, 1.5, 1.11).',
    'It is about positive action: creative proposals reached through analysis, public participation and cooperation among competing interests (D1, 1.10).',
    'It is vocational and often professionally accredited, though it need not be; the RTPI alone confers Chartered Town Planner status in the UK (D1, front matter, 1.6, 2.2).',
    'Learning is place-based and real-world: fieldwork, site visits, live projects and practitioners in the curriculum (D1, 1.21, 2.4, 3.2).',
    'Theory and practice form one continuing cycle, and the planner works as broker, visionary and advocate (D1, 2.10, 3.1).',
    'Planning is devolved across the four UK nations, which share values and knowledge through professional and academic networks (D1, front matter, 1.8).',
]

SB2 = [
    dict(theme='theme:edi', inThisSubject='planners shape equitable places for diverse societies, so the curriculum is inclusive, builds belonging for underrepresented groups and uses knowledge of particular groups at every spatial scale (D1, 1.23 to 1.29)',
         statements=['1.23', '1.25', '4.7.b6', '4.7.b7']),
    dict(theme='theme:accessibility', inThisSubject='inclusive design for every learner need, reasonable adjustments and accessible field trips, placements and live projects, physically, socially and financially; flexible recruitment (D1, 1.30 to 1.34)',
         statements=['1.30', '1.31', '1.32', '1.34']),
    dict(theme='theme:esd', inThisSubject='headed Sustainability: it underpins all of planning education; critical debate on its meaning, the four Ps, tensions between the pillars and the SDGs embedded across modules (D1, 1.35 to 1.42, 3.3, 3.12)',
         statements=['1.35', '1.42', '4.7.b6', '4.7.b8']),
    dict(theme='theme:enterprise', inThisSubject='enterprise linked to the values of planning and place-based leadership; modules on development business, land markets and climate enterprise; real-world projects with local authorities and communities (D1, 1.43 to 1.47)',
         statements=[]),
]

SB3 = dict(
    areas=[dict(component='3.4', gloss='five thematic groupings of content, described as non-prescriptive (3.3)'),
           dict(component='3.5', gloss='causes and processes of change: socio-economic, political, land markets, environmental change, built and natural interaction'),
           dict(component='3.6', gloss='practice of planning: impacts, institutions and law, plan-making, design, delivery and viability, ethics, digital technology including generative AI'),
           dict(component='3.7', gloss='debates in planning: history of thought, theory, state and market, ethics, power, scale'),
           dict(component='3.8', gloss='key planning skills: data, appraisal, problem-solving, numeracy, design, presentation, negotiation, digital planning, teamwork'),
           dict(component='3.9', gloss="specialist knowledge and skills; usual in the integrated master's")],
    practices=[dict(component='2.4', kind='teaching', gloss='practitioners and community groups in the curriculum, placements, field visits, live projects, varied assessment, specialist software'),
               dict(component='3.2', kind='learning', gloss='place-based learning through site visits and field study; individual and group work'),
               dict(component='3.13', kind='teaching', gloss='practitioners actively involved in delivery'),
               dict(component='3.14', kind='learning', gloss='varied approaches for hybrid, analogue and digital modes'),
               dict(component='3.15', kind='learning', gloss='co-creation, scenarios, simulations, community participation'),
               dict(component='3.16', kind='learning', gloss='student-led research or design project'),
               dict(component='3.17', kind='assessment', gloss='authentic assessment reflecting professional pathways'),
               dict(component='3.18', kind='assessment', gloss='essays, design projects, examinations, graphics, portfolios, presentations, placement reports, role-play such as mock committees')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.6', award=HON, items=13),
           dict(rung='typical', leadIn='4.8', award=HON, items=2),
           dict(rung='excellent', leadIn='4.9', award=HON, items=2),
           dict(rung='threshold', leadIn='4.10', award=MAS, items=4)],
    rungBases="4.5 defines the three: threshold, the minimum for an honours degree; typical, the attainment of most honours graduates; excellent, competencies and skills at an enhanced level. The typical and excellent items build on the whole threshold list rather than restating it item by item. 4.10's list is added to the bachelor's typical standard for the integrated master's (recorded as threshold for master's, batch 1 convention).",
    outcomeLists=[],
    outcomes=[dict(outcome='development beyond the threshold across the core themes', threshold='none', typical='4.8.b1', excellent='4.9.b1', basis='inferred', domain='knowledge', award=HON),
              dict(outcome='critical judgement, creativity and autonomy', threshold='none', typical='4.8.b2', excellent='4.9.b2', basis='inferred', domain='generic-skill', award=HON)])
SB4A_FULL = []

SB5 = [dict(body='Royal Town Planning Institute (RTPI)', says='uniquely confers Chartered Town Planner status in the UK; its learning outcomes for initial planning education often shape course design; it accredits courses with scrutiny and annual review; it supports early career researchers; its accredited schools meet in the Planning Schools Forum (D1, front matter, 2.2, 2.11, 2.25, 2.30)',
            requirements='not yet ingested (Part E)'),
       dict(body='Royal Institute of British Architects (RIBA)', says='named as a professional body of an aligned discipline and an informal partner to planning education (D1, 2.25)',
            requirements='not yet ingested (Part E): named only as a partner'),
       dict(body='Royal Institution of Chartered Surveyors (RICS)', says='named as a professional body of an aligned discipline and an informal partner to planning education (D1, 2.25)',
            requirements='not yet ingested (Part E): named only as a partner')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['front matter', '1.9', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28', '1.29', '1.34', '2.23', '4.7'], statements=['1.23', '1.25', '4.7.b6', '4.7.b7']),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['front matter', '1.9', '1.27', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '3.6'], statements=['1.30', '1.31', '1.32', '1.34']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development; 1.9: education for sustainability)', carriedIn=['front matter', '1.9', '1.35', '1.36', '1.37', '1.38', '1.39', '1.40', '1.41', '1.42', '3.3', '3.12', '4.7'], statements=['1.35', '1.42', '4.7.b6', '4.7.b8']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education; 1.9: employability and education)', carriedIn=['front matter', '1.9', '1.43', '1.44', '1.45', '1.46', '1.47'], statements=[])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.5', '2.7']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.5', '2.7'])],
    bodies=[dict(body='Royal Town Planning Institute', citedIn=['front matter', '2.2', '2.11', '2.25', '2.30']),
            dict(body='Urban Studies Foundation', citedIn=['2.11']),
            dict(body='Planning Schools Forum', citedIn=['2.25']),
            dict(body='Association of European Schools of Planning', citedIn=['2.25']),
            dict(body='Town and Country Planning Association', citedIn=['2.25']),
            dict(body='Regional Studies Association', citedIn=['2.25']),
            dict(body='Commonwealth Association of Planners', citedIn=['2.25']),
            dict(body='Royal Institute of British Architects', citedIn=['2.25']),
            dict(body='Royal Institution of Chartered Surveyors', citedIn=['2.25'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2'], role='descriptions of the four honours classifications, to which providers should refer when deciding evidence of achievement'),
                     dict(document='std:doc:qaa-fheq-2024-framework and std:doc:qaa-fqheis-2024-framework', named='FHEQ Level 6 and 7; FQHEIS Level 10 and 11', citedIn=['2.5', '2.7'], role='levels of the honours degree and the integrated master\'s'),
                     dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named="the QAA and Advance HE's Education for Sustainable Development Guidance", citedIn=['1.42'], role='a framework for embedding the SDGs'),
                     dict(document='UN Sustainable Development Goals (external)', named='UN Sustainable Development Goals (SDGs)', citedIn=['1.35', '1.42', '3.3'], role='the frame of the sustainability theme and of content design'),
                     dict(document='std:doc:qaa-housing-studies-2022-benchmarks; std:doc:qaa-land-construction-real-estate-and-surveying-2024-benchmarks', named='Housing Studies; Land, Construction, Real Estate and Surveying', citedIn=['front matter'], role='other statements to reference'),
                     dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
                     dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
                     dict(document='Chartered Town Planner Degree Apprenticeship Standard (not yet ingested: Part E)', named='Chartered Town Planner Degree Apprenticeship Standard', citedIn=['1.18', '2.23'], role='the apprenticeship route in England')])

B1 = [dict(slug='town-and-country-planning', definition='the name used for the field and, shortened to Planning, for the range of closely related courses under other titles such as spatial, urban and regional or community planning (D1, 1.1)',
           beneficiaryDefinition='the subject you study, whatever your course is called', scopeNote='the statement uses Planning throughout as shorthand', category='unknown', practices=['education']),
      dict(slug='inclusivity', definition='an approach that builds an educational setting free of barriers, in which underrepresented groups can take full part (D1, 1.23)',
           beneficiaryDefinition='learning set up so that nothing stops anyone taking full part', scopeNote='the basis of the inclusive curriculum (1.23 to 1.29)', category='unknown', practices=['education']),
      dict(slug='four-ps', definition='the four concerns planning is often said to balance: people, place, prosperity in more than the economic sense, and the planet (D1, 1.38)',
           beneficiaryDefinition='people, place, prosperity and planet', scopeNote='framed under sustainability', category='unknown', practices=['education', 'planning']),
      dict(slug='threshold-standard', definition='the minimum needed for an honours degree (D1, 4.5)', scopeNote='with typical and excellent above it', category='unknown', practices=['education']),
      dict(slug='typical-standard', definition='the attainment most honours graduates reach (D1, 4.5)', scopeNote='builds on the threshold (4.8)', category='unknown', practices=['education']),
      dict(slug='excellent-standard', definition='competencies and skills at an enhanced level (D1, 4.5)', scopeNote='builds on the typical (4.9)', category='unknown', practices=['education']),
      dict(slug='integrated-masters-planning', definition='a four-year full-time (or longer part-time) integrated master\'s in planning at FHEQ level 7, FQHEIS level 11 (D1, 2.7)',
           beneficiaryDefinition='a degree that runs undergraduate and master\'s study together', scopeNote='often called the MPlan; standards in 4.10', category='unknown', practices=['education']),
      dict(slug='learning', definition='change in a person brought about by gaining information, understanding, skills, attitudes and behaviour (D1, 3.14)', scopeNote='the basis for varied pedagogy', category='unknown', practices=['education'])]

B2A = [dict(concept='town-and-country-planning', form='Town and Country Planning', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='town-and-country-planning', form='Planning', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
       dict(concept='inclusivity', form='inclusivity', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='four-ps', form="four 'Ps'", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
       dict(concept='threshold-standard', form='threshold standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='typical-standard', form='typical standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='excellent-standard', form='excellent standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='integrated-masters-planning', form='MPlan', lang='en', partOfSpeech='noun', termStatus='admitted', register='discipline-specific'),
       dict(concept='learning', form='learning', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal')]
B4 = [dict(rel='broader', **{'from': 'excellent-standard'}, to='typical-standard', note='4.9: in addition to the threshold and typical standards'),
      dict(rel='broader', **{'from': 'typical-standard'}, to='threshold-standard', note='4.8: in addition to the threshold criteria')]
B5 = []

D3 = [dict(source="RTPI learning outcomes for initial planning education and its accreditation policy", why='the requirements of the body named in SB5; cited at 2.2, 2.15 and 2.30', tier='primary'),
      dict(source='Chartered Town Planner Degree Apprenticeship Standard (Institute for Apprenticeships and Technical Education)', why='the apprenticeship route named at 1.18 and 2.23', tier='primary')]

E = [
    'Rungs: three rungs, defined in 4.5 and listed at 4.6 and 4.7 (threshold, 13 items), 4.8 (typical, 2) and 4.9 (excellent, 2); 4.10 adds 4 items for the integrated master\'s. Differs from Psychology: the typical and excellent standards are two broad items each that build on the whole threshold list, not parallel lists.',
    'Skeleton corrections: 4.5.b1 to b3 were marked threshold rung items; they are the definitions of the three rungs (rungBases), not statements. 4.9.b1 and b2 were marked threshold; they are excellent. 4.10.b1 to b4 were marked typical; they are the integrated master\'s list.',
    "Integrated master's (4.10): its lead-in sets the baseline at the bachelor's typical standard, not the threshold, then adds four items. Recorded as rung threshold, award master's (meaning the integrated master's, MPlan, 2.7), level fheq:7 stated (2.7), by the batch 1 convention; for P3 whether a rung value should say it starts from typical.",
    '4.6.b1 to b5 are the five core themes for standards (KU, CS, PS, TS, PC), labels, not statements. Each 4.7 item carries the issuer\'s theme codes; the five map one to one onto Annex D\'s knowledge, cognitive, practical, transferable and professional categories, so each aaw points to the Annex D 3rd cells. Our domain for each item is read from its codes and content (inferred): KU as knowledge or understanding, CS and PS as subject-skill, TS as generic-skill, PC by content (4.7.b10 understanding, 4.7.b11 generic-skill).',
    'Threshold items are noun phrases completing the 4.7 lead-in; several items (4.7.b1, 4.8.b1, 4.8.b2, 4.9.b2, 4.10.b1, 4.10.b2) have no verb of their own, so verbs is empty.',
    'Threshold force is threshold, from 4.6 ("the minimum requirement") and 4.5; forceFrom 4.6. The excellent lead-in 4.9 has no modal ("excellent graduates also demonstrate"): force will taken from 4.1 ("will have demonstrated"), forceFrom 4.1, for P3. The integrated master\'s lead-in has "will" and "can be expected to": recorded will.',
    'gradeOf, inferred: 4.9.b1 to 4.8.b1 and 4.9.b2 to 4.8.b2 (content plainly matches, same order); no typical item links to a single threshold item. 4.9.b2 drops "initiative", which 4.8.b2 has; 4.9.b1 says "beyond the typical threshold", read as beyond the typical standard.',
    'Domain for the aggregate items is a forced single choice: 4.8.b1 and 4.9.b1 knowledge (they span all the core themes), 4.8.b2 and 4.9.b2 generic-skill.',
    'Section 3\'s lists (3.5 to 3.8, 38 items) are in the plain present ("Planning students demonstrate ... knowledge and understanding of"), with 3.8 "might include"; 3.3 says they are thematic groupings, not a prescriptive list. Recorded as SB3 areas, not statements; 4.3 says the standards apply to all of them. For P3 alongside template open point 5.',
    'Obliging words outside the five, for Abbott: "it is essential" (1.23, recorded as a describes statement; 2.27, recorded will from its own "will"); "are to be used" (3.14, describes); "needs to be", "requires" (1.25 first sentence, 1.26); "need to" (1.14, of planners; 1.25 "will need to", recorded will); "have to meet" (2.15, accredited courses); "it is important" (1.33, 2.24, 3.17); "it is expected that", "would be expected" (2.5, 4.4); "would be anticipated", "will need to adapt" (3.18). Only 1.23, 1.25, 2.27, 3.14 and 4.4 are taken as statements.',
    'Plain-present provider norms not taken as statements (template open point 5): 1.22, 1.28, 2.1, 2.3, 2.12, 2.13, 2.26, 3.10, 3.11 (for example "Education strategies incorporate ...").',
    'Mixed modals in one paragraph, recorded by the main obliging word: 1.12 (will and should: should), 1.21 (may, should, will: should), 3.15 (should, may: should), 3.16 (can, may, will: will), 4.2 (will, should: should).',
    'Front matter "consideration should be given to referencing other relevant Subject Benchmark Statements" and "Joint courses ... should also note" are in excluded matter; not statements; recorded as readWith in S7.',
    '1.9 names the themes as "education for sustainability" and "employability and education"; the second appears to mean enterprise and entrepreneurship education (the front matter names "employability, entrepreneurship and enterprise education"); tagged theme:enterprise, for P3.',
    'Generative AI and AI are mentioned (1.46, 2.10, 3.6, 3.8, 3.18) but there is no generative AI section, so theme:generative-ai is not used.',
    'Statements with a student version though addressed partly to the provider (addressee both): 1.10, 1.12, 1.23, 1.31.',
    'Codes: hecos 100197 planning, hecos 100199 urban and regional planning and cah CAH13-01-04 are stated (1.1 names Town and Country Planning and Urban and Regional Planning). hecos 100593 rural planning is inferred (the "country" in the title; not named) and held back from any lookup until P3. Spatial, land-use, city, environmental and community planning (1.1) have no HECoS term of their own.',
    'Frameworks: FHEQ and FQHEIS are cited at 2.5 and 2.7 only; CQFW is not cited. The front matter names the Quality Assessment Framework for Wales, the Quality Enhancement Framework (Scotland) and the OfS regulatory framework: quality frameworks, not qualification frameworks. S5 fheq:4 and fheq:5 are inferred from 2.8\'s exit awards (CertHE, DipHE) by the FHEQ\'s Table 1; spine:6 and spine:7 from the reference framework\'s R2.',
    'Bodies: the RTPI\'s requirements (learning outcomes for initial planning education, accreditation) are not yet ingested (D3). RIBA and RICS are named only as aligned partners (2.25); their requirements are out of scope. The Planning Officers Society appears only in the Advisory Group list (excluded).',
    'Shared documents: the Chartered Town Planner Degree Apprenticeship Standard (1.18, 2.23) is not ingested (D3). QAA\'s 2018 Enterprise and Entrepreneurship Education guidance (std:doc:qaa-enterprise-2018-guidance) is in the reference list (section 5, excluded) but not cited in the body, so it is not in SB6.',
    '1.35 "(see also section 3)" and 1.47 "As noted in section 3" are references, not statements (DPN-1).',
    'supersedes: the back matter says this is the fifth edition (April 2024) and names the fourth (2019); the 2019 statement is not held.',
    'Patterns that differ from Psychology: rung items carry the issuer\'s theme codes; typical and excellent are two broad items each; no "are able to" outcome lists; an integrated master\'s add-on list; the excellent lead-in has no modal.',
]
