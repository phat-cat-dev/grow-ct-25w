# Judgement for run 0125, QAA Physics, Astronomy and Astrophysics 2025 (std run agent). Built by tools/bm_build.py.
# Keys are S4 ids under qaa/physics-astronomy-and-astrophysics-2025/. Written fresh from the held text alone.
HON = "bachelor's with honours"
IM = "integrated master's"
CITE = 'QAA, 2025, Physics, Astronomy and Astrophysics Subject Benchmark Statement, para '

META = dict(
    run='0125', p1='2026-10-03 18:22',
    title='Subject Benchmark Statement Physics, Astronomy and Astrophysics',
    heading='Subject Benchmark Statement: Physics, Astronomy and Astrophysics (QAA, April 2025)',
    edition='April 2025 (fourth edition)', published='2025-04',
    status='current',
    supersedes='the previous Physics, Astronomy and Astrophysics statement (its date is not given in the text; the advisory group list names a 2019 minor update: Part E)',
    subjects=[
        dict(scheme='hecos', code='100425', label='physics', basis='stated'),
        dict(scheme='hecos', code='100414', label='astronomy', basis='stated'),
        dict(scheme='hecos', code='100415', label='astrophysics', basis='stated'),
        dict(scheme='cah', code='CAH07-01-01', label='physics', basis='stated'),
        dict(scheme='cah', code='CAH07-01-02', label='astronomy', basis='stated'),
        dict(scheme='cah', code='CAH07-01', label='physics and astronomy', basis='stated'),
        dict(scheme='hecos', code='100426', label='theoretical physics', basis='stated'),
        dict(scheme='hecos', code='101060', label='applied physics', basis='stated'),
        dict(scheme='hecos', code='100416', label='chemical physics', basis='stated'),
        dict(scheme='hecos', code='100949', label='biophysical science', basis='inferred'),
    ],
    awards=[HON, IM], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 onward series with cross-cutting themes (this the fourth edition for the subject)',
    partsB="partial: no glossary in the document; it sends readers to QAA's Glossary; terms it defines in passing",
    agentDefinition=("QAA's UK reference point for what a graduate in Physics, Astronomy or Astrophysics should know and be able to do "
                     "at the end of a bachelor's degree with honours or an integrated master's degree: two threshold lists (subject and "
                     "generic) and a typical list for honours, then a threshold and a typical list for the integrated master's. Reach for "
                     "it when designing, reviewing or describing a physics or astronomy course or its outcomes. It sets no excellent rung, "
                     "is not the Institute of Physics accreditation standard and is not a regulatory requirement in England."),
    summary=("Published by QAA in April 2025 for the sector, the statement describes physics as an empirical, mathematical and "
             "computational science, the purposes of a degree, its distinctive features (design, progression, flexibility, "
             "partnership, review), content, teaching and assessment, then benchmark standards at threshold and typical levels for "
             "the bachelor's degree with honours (FHEQ 6, FQHEIS 10) and the integrated master's (FHEQ 7, FQHEIS 11). It treats five "
             "cross-cutting themes (equity, diversity and inclusion; accessibility and the needs of disabled students; education for "
             "sustainable development; employability, enterprise and entrepreneurship; generative artificial intelligence), sends "
             "providers to Annex D of QAA's Frameworks (2024) for the degree classifications and names the Institute of Physics, "
             "which accredits many courses. Course teams, external examiners and PSRBs use it in design, approval and review."),
    authority='reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; part of current quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter: Relationship to legislation)',
)

S2 = dict(
    governs="what a graduate in Physics, Astronomy or Astrophysics can be expected to know, do and understand at the end of an honours degree or an integrated master's, and the nature of awards in the subject (D1, front matter: About this Statement; 4.1)",
    awards=["bachelor's degrees with honours (BSc)", "integrated master's degrees with honours", "joint, combined and major or minor honours (2.5)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    statedScope='"In this Statement we will therefore use \'Physics\' to refer to all of Physics, Astronomy and Astrophysics." (D1, 1.1)',
    statedSubjects=[
        dict(name='Physics', locator='(D1, title; 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100425', label='physics'), dict(scheme='cah', code='CAH07-01-01', label='physics')]),
        dict(name='Astronomy', locator='(D1, title; 1.1; 1.17)', kind='subject', codes=[dict(scheme='hecos', code='100414', label='astronomy'), dict(scheme='cah', code='CAH07-01-02', label='astronomy')]),
        dict(name='Astrophysics', locator='(D1, title; 1.1; 1.17)', kind='subject', codes=[dict(scheme='hecos', code='100415', label='astrophysics'), dict(scheme='cah', code='CAH07-01-02', label='astronomy')]),
        dict(name='theoretical physics courses', locator='(D1, 1.12)', kind='programme title', codes=[dict(scheme='hecos', code='100426', label='theoretical physics')]),
        dict(name='Applied physics courses', locator='(D1, 1.13)', kind='programme title', codes=[dict(scheme='hecos', code='101060', label='applied physics')]),
        dict(name='joint honours degrees and Physics with a specialism', locator='(D1, 2.1; 1.13)', kind='programme title', codes=[dict(scheme='hecos', code='100425', label='physics')]),
        dict(name='chemical physics, biophysics, or geophysics', locator='(D1, 2.5)', kind='specialism', codes=[dict(scheme='hecos', code='100416', label='chemical physics'), dict(scheme='hecos', code='100949', label='biophysical science')]),
        dict(name='placements in industry, research groups or publicly funded bodies', locator='(D1, 2.2)', kind='programme title', codes=[]),
    ])

SECTIONS = {'1': 'Context and purposes of a Physics, Astronomy or Astrophysics degree', '2': 'Distinctive features of the Physics degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.10', 'What is Physics?'),
       ('1.11', '1.21', 'Purposes and characteristics of a Physics, Astronomy or Astrophysics degree'),
       ('1.22', '1.26', 'Equity, diversity and inclusion'),
       ('1.27', '1.34', 'Accessibility and the needs of disabled students'),
       ('1.35', '1.39', 'Education for sustainable development'),
       ('1.40', '1.46', 'Employability, enterprise and entrepreneurship education'),
       ('1.47', '1.51', 'Generative artificial intelligence'),
       ('2.1', '2.2', 'Design'), ('2.3', '2.6', 'Progression'), ('2.7', '2.10', 'Flexibility'),
       ('2.11', '2.13', 'Partnership'), ('2.14', '2.16', 'Monitoring and review'),
       ('3.2', '3.7', 'Content and teaching'), ('3.8', '3.11', 'Assessment'),
       ('4.1', '4.3', 'Introduction'), ('4.4', '4.4', 'Threshold level: Subject knowledge, understanding and skills'),
       ('4.5', '4.5', 'Threshold level: Generic skills'), ('4.6', '4.6', 'Typical level'), ('4.7', '4.8', "Integrated master's")]

G = {
    '1.1': 'physics studies natural and made systems; the statement uses the one word for all three subjects',
    '1.2': 'big questions about the universe and pressing practical issues; mathematics, experiment and computing',
    '1.3': 'the many disciplines physics feeds',
    '1.4': 'a few key quantities and universal laws explain much; mechanics as the example',
    '1.5': 'idealised mathematical models and approximation, reused across very different systems',
    '1.6': 'computation and machine learning at the centre of the subject',
    '1.7': 'an empirical science: measurement tests theory; instruments spread to other fields',
    '1.8': 'progress through imagination and diverse collaboration',
    '1.9': 'lasting benefits of studying the subject (a descriptive list, not outcomes)',
    '1.10': 'where graduates find work',
    '1.11': 'what the degree develops: deep understanding and a wide set of skills',
    '1.12': 'core plus advanced topics; theoretical courses trade lab work for mathematics and computing',
    '1.13': 'applied, joint and dual honours courses; placements; the integrated master\'s adds depth and research',
    '1.14': 'courses serve future researchers and those wanting a broad education',
    '1.15': 'the fundamental areas every degree covers and principles that cross them (S4)',
    '1.16': 'application areas a degree may include',
    '1.17': 'what astronomy and astrophysics degrees add',
    '1.18': 'recent developments and enough depth to read current research (S4)',
    '1.19': 'what every degree covers in some measure: mathematics, computing, problem solving and more (provider norm, not a statement: Part E)',
    '1.20': 'professional skills graduates will have built (outcome list, S4)',
    '1.21': 'points to the threshold lists in section 4',
    '1.22': 'physics open to all; the Equality Act spirit in culture, curricula and assessment (S4)',
    '1.23': 'a curriculum that reflects who has built the discipline (S4)',
    '1.24': 'inclusive and accessible activities, safe placements, EDI awareness in students (S4)',
    '1.25': 'EDI principles throughout teaching, practice and support (S4)',
    '1.26': 'removing stereotypes and barriers; a shared inclusive culture (S4)',
    '1.27': 'accessible learning and assessment by inclusive design and adjustments (S4)',
    '1.28': 'inclusive design defined',
    '1.29': 'fair entry to courses (S4)',
    '1.30': 'course teams, the Disabled Student Commitment and accessible labs, code and maths (S4)',
    '1.31': 'adaptive technologies fall short for code, maths and diagrams; resources to compensate (S4)',
    '1.32': 'equal access to placements and volunteering (S4)',
    '1.33': 'agreeing individual adjustments with students and support services (S4)',
    '1.34': 'training and resources for course teams (S4)',
    '1.35': 'physics and the UN Sustainable Development Goals',
    '1.36': 'instruments and models that quantify sustainability problems',
    '1.37': 'technologies for energy and climate; examples from ice cores, photocells and LEDs',
    '1.38': 'clear communication to tackle global challenges',
    '1.39': 'embedding the goals in the curriculum through examples, projects and lectures',
    '1.40': 'enterprise, entrepreneurship and employability defined',
    '1.41': 'why enterprise education matters for careers',
    '1.42': 'why employers value physics graduates; growing sectors',
    '1.43': 'helping students articulate the value of their degree (S4)',
    '1.44': 'innovation fields and spinouts',
    '1.45': 'optional entrepreneurial skills, ideally taught through physics',
    '1.46': 'external input from industry, alumni and advisory boards',
    '1.47': 'generative AI: principles rather than rules',
    '1.48': 'preparing students to use generative AI ethically and well (S4)',
    '1.49': 'embrace the technology, aware of its risks (S4)',
    '1.50': 'assessment that acknowledges generative AI (S4)',
    '1.51': 'responsible use, data protection and critique of AI output (S4)',
    '2.1': 'a broad subject with a common core and provider-specific options',
    '2.2': 'placements, credit-bearing or experiential',
    '2.3': 'progression by level towards the threshold; framework levels named',
    '2.4': 'a second-class degree as preparation for postgraduate study',
    '2.5': 'joint and combined degrees reach the core skills and add others (S4)',
    '2.6': 'exit awards at lower levels',
    '2.7': 'course length in the four nations',
    '2.8': 'part-time study and credit',
    '2.9': 'modes and formats of study; micro-credentials and prior learning',
    '2.10': 'foundation years and access routes',
    '2.11': 'partnerships for study abroad and industry',
    '2.12': 'credit from study abroad and calibrating partner marks (S4)',
    '2.13': 'professional placements and their value',
    '2.14': 'internal and external review with the student voice',
    '2.15': 'external examiners and threshold standards',
    '2.16': 'externality and accreditation review by the Institute of Physics',
    '3.1': 'what section 3 covers',
    '3.2': 'a hierarchical, empirical subject and its teaching methods',
    '3.3': 'the mix of methods varies and changes over time',
    '3.4': 'skills developed through physics applications; open-ended lab work at higher levels (S4)',
    '3.5': 'computing skills, generative AI among them',
    '3.6': 'skills valued by quantitative professions',
    '3.7': 'no prescribed methods; inclusive design for outcomes (S4)',
    '3.8': 'assessment aligned to outcomes',
    '3.9': 'the range of assessment methods',
    '3.10': 'matching assessment styles to outcomes',
    '3.11': 'uneven module marks and flexible regulations (S4)',
    '4.1': 'the statement sets threshold and typical standards for honours',
    '4.2': 'most exceed the threshold; Annex D for classifications (S4)',
    '4.3': 'not competence standards; Equality Act and EHRC guidance (S4)',
    '4.4': 'threshold: subject knowledge, understanding and skills (rung list)',
    '4.5': 'threshold: generic skills (rung list)',
    '4.6': "typical honours level (rung list)",
    '4.7': "integrated master's threshold (rung list)",
    '4.8': "integrated master's typical level (rung list)",
}
CTYPE = {'1.15': 'area', '1.16': 'area', '1.17': 'area', '1.19': 'area', '3.2': 'practice', '3.9': 'practice', '3.10': 'practice', '3.4': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='section heading lines (1 to 4)', kind='other: headings, recorded in S3 as sections'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for S7 and SB6'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: back matter, read for S8'),
]

P = {}
def s(i, **k):
    P[i] = k

# ------------------------------------------------------------------ paragraph statements
PROV = ('n/a', 'a duty on the course team or provider; the student meets its effect, not a standard to reach')

def pv(i, force, gist, nb, extra=''):
    """aaw for a provider duty."""
    return (f"Describe paragraph {i} as advice the statement gives to course teams and providers ({force}), {gist}; it binds no student and is not a condition of the award. "
            f"Cite it as ({CITE}{i}). Do not present it as a legal or regulatory duty in its own right, even where it points to legislation{extra}. "
            f"Set it beside {nb}.")

def pd(when, q, avoid='Do not put it to a student as something they must do.'):
    return (f"Raise it with a programme team when {when}. Frame it for staff as what the course should do, and ask: {q} "
            f"{avoid} Summarise rather than reading the paragraph aloud.")

s('1.15', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='all Physics degrees', addressee='both',
  verbs=['cover', 'provide'], about='the fundamental areas and the principles across them', domain='knowledge', award=[HON, IM],
  para="Every physics degree will treat, in some measure, classical mechanics, relativity, quantum physics, electromagnetism, thermodynamics with statistical physics, light and waves and the properties of matter, and will give students a sense of the principles, such as conservation and equilibrium, that run through them.",
  prac="Make sure the curriculum touches each fundamental area (mechanics, relativity, quantum, electromagnetism, thermal and statistical physics, waves and optics, matter) and draws out the principles that cut across them, such as conservation laws and equilibrium.",
  ben="Whatever route you take, your course will introduce you to the core areas of physics, from mechanics and relativity to quantum and thermal physics, and help you see the principles, such as conservation laws, that link them.",
  aaw=f"Describe paragraph 1.15 as the statement's expected common core (will) for every honours and integrated master's degree in the subject, held at FHEQ level 6 and FQHEIS level 10. Cite it as ({CITE}1.15). Do not claim it fixes how much time each area receives, since it says each is covered to some extent. Set it beside 1.16 and 1.17 (application and astronomy topics), 2.1 and the honours descriptor qaa/fheq-2024/4.15.b1.",
  aad="Raise it when a student asks what every physics degree contains or a team checks its core modules. For a student, name the core areas plainly and ask which of them feel secure and which feel thin; for staff, ask where each area and the cross-cutting principles are taught. Do not read out the list of areas at length or suggest that every area is taught to the same depth.")
s('1.18', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='all Physics degrees', addressee='both',
  verbs=['provide', 'cover', 'engage'], about='recent developments and reading current research', domain='knowledge', award=[HON, IM],
  para="Degrees give students a sense of recent advances and will take some core areas far enough for students to work with today's research papers.",
  prac="Take at least some core areas to a level where students can read and use current research literature, and give them a feel for recent advances in the field.",
  ben="Your course will take some core topics far enough that you can read and make sense of current research papers, and will show you recent advances in physics.",
  aaw=f"Describe paragraph 1.18 as an expected outcome (will) of every degree in the subject: depth in some core areas sufficient to read current research, at FHEQ level 6. Cite it as ({CITE}1.18). Do not claim it asks for depth in every area or for original research at honours level. Set it beside 4.6.b8 (research-based materials), 4.7.b3.masters and the honours descriptor qaa/fheq-2024/4.15.b3.2.",
  aad="Raise it when a student wonders why final-year modules lean on journal papers or a team plans advanced options. Ask a student: which recent paper in your area could you explain to a friend? Ask staff which core areas reach research depth. Avoid suggesting the student must master the literature across the whole subject.")

s('1.22', type='expectation', rung='none', force='should', level='none', appliesTo='the discipline, its curricula, teaching and assessment', addressee='provider',
  verbs=['embedded', 'welcomed', 'enabled', 'encouraged'], about='physics open to all; EDI embedded', domain='none', award=[HON, IM],
  para="Physics should be open to everyone through inclusive teaching that reflects students' range of experience and background; that needs EDI principles and the spirit of equality law built into the culture, curricula, teaching and assessment, and every person's contribution should be welcomed and supported.",
  prac="Build equity, diversity and inclusion into the department's culture, curriculum, teaching and assessment, aware of protected characteristics and personal circumstances such as caring or economic disadvantage, so that every student's contribution is welcomed and enabled.",
  ben=PROV,
  aaw=pv('1.22', 'should', 'opening the discipline to all through inclusive culture, curricula, teaching and assessment', '1.23 to 1.26 (the rest of the EDI theme), 1.27 (accessibility) and 4.3', ' (here the Equality Act 2010)'),
  aad=pd('it reviews its culture, curriculum or assessment for inclusion', 'whose experiences and backgrounds does the current curriculum reflect, and whose does it miss?'))
s('1.23', type='expectation', rung='none', force='should', level='none', appliesTo='the Physics curriculum', addressee='provider',
  verbs=['reflect', 'acknowledge', 'learn'], about='a curriculum reflecting the diversity of contributors', domain='none', award=[HON, IM],
  para="The curriculum, taken broadly to include content, delivery, assessment and professional preparation, should show the variety of people and ideas behind the discipline and its uses; as a global endeavour, physics should face its past and learn from it.",
  prac="Show in content and examples the range of people, cultures and ideas that have shaped physics and its applications, and treat the discipline's history honestly as a shared, worldwide enterprise.",
  ben=PROV,
  aaw=pv('1.23', 'should', 'a curriculum that reflects the range of people and ideas behind physics', '1.22, 1.24 and 1.8 (diverse collaboration)'),
  aad=pd('it chooses examples, case studies or reading lists', 'whose work appears in the examples students meet, and what does that tell them about who does physics?'))
s('1.24', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='the Physics curriculum and its students', addressee='both',
  verbs=['provided', 'build', 'accept', 'support'], about='inclusive activities, safe placements and EDI awareness', domain='generic-skill', award=[HON, IM],
  para="Curriculum activities should be inclusive and open to all, with suitable alternatives where they cannot be, and no compulsory or optional element should leave students facing discrimination or danger; placements and field trips need checking for that risk. Students will build an awareness of EDI that lets them support peers and staff and work professionally after graduating.",
  prac="Design every activity to be accessible, offer equivalent alternatives where one cannot be, and check placement and field-trip locations for risk of discrimination; expect students to leave with an awareness of EDI they can use at work.",
  ben="You should be able to take part in every activity on your course, or be offered a fair alternative, without facing discrimination. Along the way you will build an awareness of equity, diversity and inclusion that helps you support others and work professionally.",
  aaw=f"Describe paragraph 1.24 as two things: advice to course teams (should) that every activity be inclusive with fair alternatives, and an expected outcome (will) that students gain EDI awareness, a generic skill at FHEQ level 6. Cite it as ({CITE}1.24). Do not merge the two forces or claim it guarantees every placement is free of risk. Set it beside 1.22, 4.5.b11 (working with diversity in a group) and qaa/fheq-2024/annex-d/transferable/r2/3rd.",
  aad="Raise it with a student worried about a placement, a field trip or being left out, and with a team planning off-site activities. Ask a student: has any part of your course felt closed to you, and what alternative would help? Ask staff how they check a location for risk of discrimination. Avoid placing on the student the duty to secure alternatives; that sits with the course.")
s('1.25', type='expectation', rung='none', force='should', level='none', appliesTo='learning, teaching, practice and support in Physics', addressee='provider',
  verbs=['appear', 'permeate'], about='EDI principles throughout the department', domain='none', award=[HON, IM],
  para="EDI works when everyone has equivalent chances and the same duty to live it out; its principles should run through learning, teaching, practice and support for staff and students alike.",
  prac="Treat EDI as part of every activity, for staff and students alike, rather than as a separate module or policy, and give everyone equivalent opportunities and a shared responsibility for it.",
  ben=PROV,
  aaw=pv('1.25', 'should', 'equity, diversity and inclusion running through all learning, teaching, practice and support', '1.22, 1.26 and qaa/fheq-2024/annex-d/professional/r2/3rd-1st'),
  aad=pd('it asks whether EDI is confined to one place in the course', 'where do students meet EDI outside a single session or policy document?'))
s('1.26', type='expectation', rung='none', force='should', level='none', appliesTo='staff and students in Physics', addressee='both',
  verbs=['taken', 'eradicate', 'remove', 'challenge'], about='removing stereotypes and barriers; shared responsibility', domain='none', award=[HON, IM],
  para="Active steps should be taken against harmful stereotypes and language, barriers to inclusion and the structural disadvantages some groups face, for instance through staff and student partnership in a respectful setting; building an inclusive culture is everyone's responsibility.",
  prac="Act to remove harmful stereotypes, language and barriers, and to challenge structural disadvantage, working in partnership with students; make clear that staff and students share responsibility for an inclusive culture.",
  ben="Everyone in physics, you included, shares responsibility for an inclusive culture: you can help by challenging stereotypes and careless language and by working with staff to remove barriers.",
  aaw=f"Describe paragraph 1.26 as advice (should) to take active steps against stereotypes, barriers and structural disadvantage, with the responsibility for an inclusive culture shared by staff and students. Cite it as ({CITE}1.26). Do not present it as a rule a student can be assessed against or as a legal duty. Set it beside 1.22, 1.25 and 1.24.",
  aad="Raise it when a student or team describes unwelcoming language or a barrier to taking part. For a student, put it plainly as a shared job and ask: what is one thing you or your group could change? For staff, ask how students are brought into removing barriers. Avoid making the student responsible for fixing structural problems on their own.")

s('1.27', type='expectation', rung='none', force='should', level='none', appliesTo='Physics courses', addressee='provider',
  verbs=['offered'], about='accessible learning and assessment', domain='none', award=[HON, IM],
  para="Accessibility means removing needless barriers for people with different needs; students should be given learning and assessment that are equally open to them, through inclusive design where possible and reasonable individual adjustments where needed.",
  prac="Design learning and assessment to be equally accessible from the outset and add reasonable individual adjustments where a student still needs them, so that all can thrive and feel they belong.",
  ben=PROV,
  aaw=pv('1.27', 'should', 'learning and assessment equally accessible through inclusive design first and individual adjustments second', '1.28 (inclusive design defined), 1.30, 1.33 and 3.7', ' (here equality law)'),
  aad=pd('it designs assessment or responds to a request for adjustment', 'which barriers in this module could inclusive design remove for everyone, before any individual adjustment?', 'A student may ask about it; tell them what they can expect, but do not frame it as their task.'))
s('1.29', type='expectation', rung='none', force='should', level='none', appliesTo='entry to Physics courses', addressee='provider',
  verbs=['influenced'], about='fair entry', domain='none', award=[HON, IM],
  para="Admission to physics courses should be fair and free of assumptions, by staff or students, about barriers to learning.",
  prac="Keep admissions fair: decisions should not rest on staff or student assumptions about a candidate's barriers to learning.",
  ben=PROV,
  aaw=pv('1.29', 'should', 'equitable entry unaffected by assumptions about barriers to learning', '1.27, 2.10 (alternative entry routes) and 1.22'),
  aad=pd('it reviews admissions or interview practice', 'what assumptions about a disabled applicant could creep into this decision, and how would we know?'))
s('1.30', type='expectation', rung='none', force='should', level='none', appliesTo='Physics course teams', addressee='provider',
  verbs=['take', 'ensure', 'provided', 'develop', 'given'], about='course teams, the Disabled Student Commitment and accessible delivery', domain='none', award=[HON, IM],
  para="Course teams should use the guidance in the Disabled Student Commitment and make sure every student gets inclusive support and training to reach the knowledge, skills and behaviours the statement sets out; they should attend to accessible communication and especially to laboratories, computing and mathematical and graphical material, and a blend of live and recorded delivery can help.",
  prac="Use the Disabled Student Commitment, check that communications are accessible, and give particular attention to labs, computing work and mathematical or graphical content; consider mixing synchronous and asynchronous delivery for disabled and neurodivergent students.",
  ben=PROV,
  aaw=pv('1.30', 'should', 'using the Disabled Student Commitment and making labs, computing and mathematical content accessible', '1.27, 1.31 (limits of adaptive technology) and 1.33'),
  aad=pd('it plans labs, coding sessions or mathematical materials', 'how would a screen-reader user or a neurodivergent student work through this lab script or problem sheet?'))
s('1.31', type='expectation', rung='none', force='should', level='none', appliesTo='higher education providers', addressee='provider',
  verbs=['provide', 'mitigate'], about='resources where adaptive technology falls short', domain='none', award=[HON, IM],
  para="Adaptive technologies help remove barriers but, as yet, do not serve students well for programming, mathematics and diagrams; providers should supply the resources needed to make up for this.",
  prac="Recognise that current assistive tools handle code, equations and diagrams poorly, and fund the extra support and resources that close the gap.",
  ben=PROV,
  aaw=pv('1.31', 'should', 'resourcing support where assistive technology does not yet cope with code, mathematics and diagrams', '1.30, 1.34 and 1.27'),
  aad=pd('it budgets for accessibility support', 'which parts of the course rely on code, equations or diagrams that assistive tools render badly, and what support fills the gap?'))
s('1.32', type='expectation', rung='none', force='should', level='none', appliesTo='extracurricular opportunities', addressee='provider',
  verbs=['made', 'ensure'], about='equal access to placements and volunteering', domain='none', award=[HON, IM],
  para="Every practical effort should be made so that placements, volunteering and similar extras are equally open to all, given that some students face added hurdles and hidden costs.",
  prac="Widen access to placements, volunteering and other extras by anticipating the hidden costs and extra hurdles some students face.",
  ben=PROV,
  aaw=pv('1.32', 'should', 'equal access to placements, volunteering and similar opportunities', '2.2, 2.13 (placements) and 1.27'),
  aad=pd('it advertises placements or volunteering', 'what hidden costs or hurdles might stop some students taking this up, and what can the course do about them?'))
s('1.33', type='expectation', rung='none', force='should', level='none', appliesTo='Physics course teams', addressee='provider',
  verbs=['engage', 'discuss', 'implement'], about='agreeing individual adjustments', domain='none', award=[HON, IM],
  para="Physics course teams should work with students and student support services to agree and put in place reasonable individual adjustments where they are needed.",
  prac="Agree reasonable adjustments with the student and the support service together, and see that they are carried through in teaching and assessment.",
  ben=PROV,
  aaw=pv('1.33', 'should', 'agreeing reasonable individual adjustments with students and support services', '1.27, 1.30 and 1.34'),
  aad=pd('a student needs an adjustment', 'who speaks with the student and the support service, and how is the agreed adjustment checked in practice?', 'With a student, say plainly that the course should talk this through with them; do not make it their task.'))
s('1.34', type='expectation', rung='none', force='should', level='none', appliesTo='higher education providers', addressee='provider',
  verbs=['ensure', 'implement'], about='training and resources for course teams', domain='none', award=[HON, IM],
  para="Providers should see that physics course teams have the training and resources to put accessibility into practice.",
  prac="Give course teams the training and resources they need to deliver accessibility in practice, not only in policy.",
  ben=PROV,
  aaw=pv('1.34', 'should', 'training and resourcing course teams to make accessibility work in practice', '1.30, 1.31 and 1.33'),
  aad=pd('it reviews staff development', 'what training has the team had in accessible teaching of laboratory and mathematical work?'))

s('1.43', type='expectation', rung='none', force='should', level='none', appliesTo='Physics course teams', addressee='provider',
  verbs=['engage', 'help', 'understand', 'articulate'], about='helping students articulate the value of their degree', domain='none', award=[HON, IM],
  para="Physics course teams should work with students and careers advisers so that students grasp and can put into words what their degree has given them and how it connects with work-based learning or graduate jobs.",
  prac="Work with careers advisers to help students recognise and express the skills, knowledge and behaviours they have gained and link them to work-based learning and graduate roles.",
  ben=PROV,
  aaw=pv('1.43', 'should', 'working with careers advisers so students can explain the value of what they have learned', '4.4.b9 (the threshold outcome it supports), 1.40 to 1.42 and qaa/fheq-2024/4.15.b9.3'),
  aad=pd('it plans careers input or personal tutoring', 'where in the course do students practise explaining their skills to an employer?', 'With a student, turn it into the related outcome at 4.4.b9 rather than a duty on them.'))
s('1.48', type='expectation', rung='none', force='describes', level='none', appliesTo='students and the curriculum', addressee='provider',
  verbs=['prepared', 'use', 'develop'], about='guided preparation to use generative AI', domain='none', award=[HON, IM],
  para="Machine learning and AI already serve physics in data processing and modelling, and generative AI can raise productivity; students need preparing to use it in study and work, which calls for careful guidance, training and practice inside the curriculum so they develop ethical and effective habits.",
  prac="Build guidance, training and practice in generative AI into the curriculum so students learn to use it ethically and effectively for study and later work.",
  ben=PROV,
  aaw=f"Describe paragraph 1.48 as the statement's view that students need guided preparation in generative AI within the curriculum; its obliging word is 'need', outside the five, so record its force as descriptive and do not raise it to must or should. Cite it as ({CITE}1.48). Do not claim it requires any particular tool or policy. Set it beside 1.49 to 1.51, 3.5 and 4.5.b9 (digital technology).",
  aad=pd('it decides how generative AI appears in teaching', 'where do students practise using AI tools under guidance, and how do they learn when not to?', 'With a student, talk about the guidance they can expect; do not treat it as a rule they have broken or met.'))
s('1.49', type='expectation', rung='none', force='should', level='none', appliesTo='the Physics degree and its outcomes', addressee='provider',
  verbs=['embraced', 'maintaining'], about='embracing generative AI with awareness of risk', domain='none', award=[HON, IM],
  para="Generative AI produces text, images, code and more, which changes the skills a physics graduate needs and so the skills, activities and outcomes of the degree; like earlier technologies, it should be embraced with an eye on its risks and limits.",
  prac="Revisit skills, activities and learning outcomes in light of generative AI, adopting it where it helps while teaching its risks and limitations.",
  ben=PROV,
  aaw=pv('1.49', 'should', 'adopting generative AI in the degree while keeping its risks and limits in view', '1.48, 1.50 and 1.51'),
  aad=pd('it reviews outcomes or activities that generative AI now affects', 'which learning outcome has AI changed most, and what risk do students need to understand?'))
s('1.50', type='expectation', rung='none', force='should', level='none', appliesTo='assessment in Physics', addressee='provider',
  verbs=['recognise', 'develop', 'equip', 'welcomed'], about='assessment that acknowledges generative AI', domain='none', award=[HON, IM],
  para="AI tools prompt assessment designs that take generative AI into account; assessments that see its potential in physics, build students' critical thinking and prepare them to solve complex problems creatively should be welcomed.",
  prac="Design some assessments that openly use generative AI, testing critical thinking and creative problem solving rather than simply banning the tools.",
  ben=PROV,
  aaw=pv('1.50', 'should', 'welcoming assessment that recognises generative AI and builds critical, creative problem solving', '1.51, 3.9 (critical use of AI outputs as an assessment method) and 3.10'),
  aad=pd('it designs or revises assessments', 'in which assessment could students use AI openly and be judged on how critically they handle it?'))
s('1.51', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='students and those who train them', addressee='both',
  verbs=['use', 'taken', 'ensure', 'trained', 'critique'], about='responsible use and critique of generative AI', domain='generic-skill', award=[HON, IM],
  para="Students should use generative AI responsibly, sustainably, ethically and safely, keeping sensitive data out of public view with data protection and intellectual property in mind, and should be trained to question AI output for accuracy, relevance and bias.",
  prac="Teach responsible, ethical and safe use of generative AI, including data protection and intellectual property, and train students to check AI output for accuracy, relevance and bias.",
  ben="You should use generative AI responsibly, ethically and safely, never feeding it sensitive data, and you should check what it gives you for accuracy, relevance and bias.",
  aaw=f"Describe paragraph 1.51 as advice (should) addressed both to students, on responsible use of generative AI, and to courses, on training them to critique its output; treat the critique as a generic skill at FHEQ level 6. Cite it as ({CITE}1.51). Do not claim it bans generative AI or sets a legal standard beyond data protection law. Set it beside 1.48, 1.50, 4.5.b9 and qaa/fheq-2024/annex-d/transferable/r1/3rd.",
  aad="Raise it when a student uses or plans to use an AI tool for code, writing or data, or a team sets AI rules. Ask a student: what did you check before trusting that output, and did any of the data you gave it need protecting? Ask staff where students are trained to critique AI output. Avoid moralising or reading the paragraph aloud; keep it practical.")

s('2.5', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on combined or joint degrees', addressee='learner',
  verbs=['achieve', 'add', 'explore'], about='joint and combined degrees and the core skills', domain='subject-skill', award=HON,
  para="Students taking physics, astronomy or astrophysics within a combined or joint degree will reach the core of the subject-specific and generic skills set out here and add others from their other subject, with room for interdisciplinary work such as chemical physics or biophysics.",
  prac="On joint, combined and major or minor routes, make sure students still reach the core subject and generic skills, and use the overlap with the other subject for interdisciplinary study.",
  ben="If you study physics alongside another subject, you will still gain the core physics and general skills, add skills from your other subject and may find interesting ground where the two meet.",
  aaw=f"Describe paragraph 2.5 as an expected outcome (will) for joint and combined honours students: the core of the threshold lists at FHEQ level 6, plus skills from the other subject. Cite it as ({CITE}2.5). Do not claim joint students must meet every item of 4.4 and 4.5 in full; the statement says core elements. Set it beside 4.4, 4.5, 1.13 and the honours descriptor qaa/fheq-2024/4.15.b1.",
  aad="Raise it when a joint honours student asks whether they count as a physicist or a team designs a combined route. Ask a student: which core physics skills feel strongest, and where does your other subject add something? Ask staff which items of the threshold lists the joint route secures. Avoid implying the joint route is a lesser award.")
s('2.12', type='expectation', rung='none', force='should', level='none', appliesTo='study abroad and partner marks', addressee='provider',
  verbs=['calibrated', 'ensure'], about='credit from study abroad and calibrating partner marks', domain='none', award=[HON, IM],
  para="Credit for time abroad follows its length and the home provider's rules and counts towards progression; where a partner's marks feed the final classification they should be carefully calibrated to match the awarding institution.",
  prac="Set credit for study abroad by duration and home regulations, and calibrate partner marks with care before they count towards the classification.",
  ben=PROV,
  aaw=pv('2.12', 'should', 'calibrating marks earned with a partner before they count towards the classification', '2.11, 2.13 and 4.2 (Annex D)'),
  aad=pd('it approves a study-abroad partnership or converts partner marks', 'how are this partner\'s marks mapped onto the home scale, and who checks the mapping?', 'With a student going abroad, explain how credit will count; do not make calibration their task.'))
s('3.4', type='expectation', rung='none', force='should', level='none', appliesTo='skills development in Physics courses', addressee='provider',
  verbs=['developed'], about='skills taught through physics applications', domain='none', award=[HON, IM],
  para="Skills work covers both generic and subject skills, which should be developed through physics applications where appropriate; progress across levels may show, for example in laboratory and observing work growing more open-ended with tougher reporting standards.",
  prac="Teach generic skills through physics contexts where it makes sense, and let laboratory and observational work become more open-ended, with stricter reporting expectations, as students advance.",
  ben=PROV,
  aaw=pv('3.4', 'should', 'developing generic and subject skills through physics applications, with lab work growing more open-ended', '4.5 (generic skills), 4.4.b4, 4.6.b5 and spine:6'),
  aad=pd('it maps skills across years', 'how does laboratory work become more open-ended from first year to final year?'))
s('3.7', type='expectation', rung='none', force='should', level='none', appliesTo='course design', addressee='provider',
  verbs=['paid', 'ensure', 'support'], about='teaching methods that support outcomes and inclusion', domain='none', award=[HON, IM],
  para="The statement does not dictate teaching methods; providers pick methods that engage, motivate and stretch students while delivering outcomes, and in design attention should go to methods that support the outcomes and are inclusive and accessible to all.",
  prac="Choose teaching methods freely, but check in design that each supports the learning outcomes and is inclusive and accessible to every student.",
  ben=PROV,
  aaw=pv('3.7', 'should', 'checking in design that teaching methods support the outcomes and are inclusive and accessible', '3.2, 1.27 and 1.28'),
  aad=pd('it designs or reviews a module', 'how does each teaching method serve an outcome, and who might it leave out?'))
s('3.11', type='expectation', rung='none', force='describes', level='none', appliesTo='assessment regulations', addressee='provider',
  verbs=['take', 'allowing', 'judge'], about='flexible regulations for uneven module marks', domain='none', award=[HON, IM],
  para="A student's marks can vary widely between modules in a quantitative subject, and those near the bottom of the range may fail some modules yet meet the course outcomes overall; regulations need enough flexibility to let examiners judge overall performance against all outcomes.",
  prac="Write assessment regulations that let examiners judge a student's overall performance against all outcomes, since problem-heavy modules often produce marks across the whole range.",
  ben=PROV,
  aaw=f"Describe paragraph 3.11 as the statement's view that regulations need flexibility for uneven marks in a quantitative subject; its obliging word is 'need', outside the five, so record the force as descriptive. Cite it as ({CITE}3.11). Do not claim it permits failed modules to be ignored or overrides a provider's regulations. Set it beside 3.10, 4.2 and qaa/fheq-2024/annex-d/summary/r1/3rd.",
  aad=pd('an exam board meets a student who failed a module but did well overall', 'do our regulations let the board weigh this student\'s whole profile against the course outcomes?', 'Do not promise a student that a failed module will be overlooked.'))
s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['refer'], about='Annex D for performance above threshold', domain='none', award=HON,
  para="Most students do far better than the minimum; each provider decides how to evidence that and should refer to Annex D of the qualifications frameworks, which describes the four honours classifications.",
  prac="Use Annex D's descriptions of the first, upper second, lower second and third to judge and evidence performance above the threshold.",
  ben=PROV,
  aaw=pv('4.2', 'should', 'referring to Annex D of the Frameworks (2024) to evidence achievement above the threshold', '4.1, the 4.4 and 4.6 rungs and qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st'),
  aad=pd('it writes marking criteria or classification rules', 'how do our criteria for a first or an upper second draw on Annex D, and do they go beyond the threshold lists?', 'With a student, explain that most graduates go well beyond the threshold; do not treat the threshold as the target.'))
s('4.3', type='expectation', rung='none', force='should', level='none', appliesTo='providers developing competence standards', addressee='provider',
  verbs=['follow', 'informed'], about='not competence standards; EHRC guidance', domain='none', award=[HON, IM],
  para="The rung standards at both honours and integrated master's level are not universal competence standards; a provider that sets competence standards under the Equality Act 2010 may draw on this statement and PSRB requirements and should follow the latest guidance from the Equality and Human Rights Commission.",
  prac="Do not treat the rung lists as competence standards; if you write competence standards into a programme specification, draw on them and any PSRB requirements and follow current Equality and Human Rights Commission guidance.",
  ben=PROV,
  aaw=pv('4.3', 'should', 'following current Equality and Human Rights Commission guidance when competence standards are set, since the rungs are not competence standards', '4.1, 4.4 to 4.8, 1.22 and SB5 (bodies)', ' (here the Equality Act 2010)'),
  aad=pd('it writes competence standards or reviews them for disabled students', 'which items here are genuine competence standards, and have we checked them against current EHRC guidance?'))

# ------------------------------------------------------------------ outcome list 1.20 (lead-in: graduates will have developed)
def a120(i, about, fd, nb):
    return (f"Describe 1.20.b{i} as an expected outcome (will) of every degree in the subject, a professional skill ({about}) held at FHEQ level 6 for honours and carried into the integrated master's. "
            f"Cite it as ({CITE}1.20). Do not present it as one of the threshold rungs in section 4 or as a professional body requirement. Set it beside {nb} and {fd}.")
def d120(when, q):
    return (f"Raise it when {when}. For a student, put it in plain second-person terms and ask: {q} For staff, ask where the course builds and checks this skill. "
            "Avoid reading the list aloud or treating it as an assessed threshold.")
L120 = dict(type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject', addressee='learner', award=[HON, IM])
def k120(i, **k):
    s('1.20.b%d' % i, **L120, **k)
k120(1, verbs=['approach'], about='flexible approach to new problems', domain='generic-skill',
     para="Will be able to tackle unfamiliar problems with flexibility and adaptability.",
     prac="Graduates will be able to meet unfamiliar problems flexibly and adapt their approach.",
     ben="You will be able to tackle problems you have not met before, adapting your approach as you go.",
     aaw=a120(1, 'meeting new problems flexibly', 'qaa/fheq-2024/4.15.b9.2', '4.5.b1 and 4.6.b3'),
     aad=d120('a student feels stuck on an unfamiliar problem or a team designs open-ended tasks', 'what did you try first, and what did you change when it did not work?'))
k120(2, verbs=[], about='communicating complex data and ideas to fit the audience', domain='generic-skill',
     para="Will communicate complex data and ideas clearly, choosing media that suit the content and the audience.",
     prac="Graduates will communicate complex data and ideas clearly, matching the medium to the content and to who is listening.",
     ben="You will be able to explain complex data and ideas clearly, picking the format that suits your material and your audience.",
     aaw=a120(2, 'clear communication of complex material to suit the audience', 'qaa/fheq-2024/4.15.b8', '4.4.b8, 4.5.b6 and 4.6.b7'),
     aad=d120('a student prepares a talk, poster or report', 'who is your audience, and what will they need from your figures?'))
k120(3, verbs=['work'], about='working alone and in teams', domain='generic-skill',
     para="Will be able to work both independently and as part of a team.",
     prac="Graduates will work effectively on their own and in teams.",
     ben="You will be able to work well both on your own and as part of a team.",
     aaw=a120(3, 'working individually and in teams', 'qaa/fheq-2024/annex-d/transferable/r2/3rd', '4.5.b11 and 4.5.b10'),
     aad=d120('a student reflects on group work or a team plans team projects', 'what did you contribute to the group, and what did you do better alone?'))
k120(4, verbs=[], about='managing time and deadlines', domain='generic-skill',
     para="Will manage time and meet deadlines.",
     prac="Graduates will manage their time and deadlines.",
     ben="You will be able to manage your time and meet your deadlines.",
     aaw=a120(4, 'time and deadline management', 'qaa/fheq-2024/annex-d/transferable/r3/3rd', '4.5.b10'),
     aad=d120('a student struggles with workload or a team spaces deadlines', 'how do you plan your week when three deadlines fall together?'))
k120(5, verbs=[], about='critical analysis of own and others\' work', domain='generic-skill',
     para="Will analyse critically both their own work and the work of others.",
     prac="Graduates will critically analyse their own work and that of others.",
     ben="You will be able to assess your own work and other people's work critically.",
     aaw=a120(5, 'critical analysis of one\'s own and others\' work', 'qaa/fheq-2024/4.15.b7', '4.5.b3 and 4.6.b4'),
     aad=d120('a student reviews a peer\'s report or receives feedback', 'what is the weakest point in this piece of work, and how would you fix it?'))
k120(6, verbs=['identify'], about='spotting ethical issues in one\'s work', domain='generic-skill',
     para="Will be able to recognise the ethical questions their work may raise.",
     prac="Graduates will be able to identify potential ethical issues in their own work.",
     ben="You will be able to spot the ethical questions your own work might raise.",
     aaw=a120(6, 'identifying ethical issues in one\'s own work', 'qaa/fheq-2024/annex-d/professional/r2/3rd-1st', '1.20.b7 and 1.51'),
     aad=d120('a student plans a project with data, people or AI tools', 'who could be affected by this work, and how?'))
k120(7, verbs=['fabricate', 'falsify', 'misrepresent', 'commit', 'recognise'], about='research integrity and honest limits', domain='understanding',
     para="Will understand that fabricating, falsifying or misrepresenting data or plagiarising is unethical in science; the statement adds that a professional physicist should be impartial and truthful in all their work and recognise the limits of their methods, calculations and knowledge.",
     prac="Graduates will understand that fabrication, falsification, misrepresentation and plagiarism are scientific misconduct, and will see that a professional physicist should be objective and honest about the limits of methods and knowledge.",
     ben="You will understand that inventing, altering or misreporting data or plagiarising is scientific misconduct, and that a professional physicist should be objective, honest and open about the limits of their methods and knowledge.",
     aaw=a120(7, 'research integrity and honesty about limits', 'qaa/fheq-2024/4.15.b4', '1.20.b6, 4.4.b7 and 1.51'),
     aad=d120('a student is tempted to tidy awkward data or asks about referencing', 'what would you report if your result disagreed with theory?'))
k120(8, verbs=[], about='safe working environments', domain='understanding',
     para="Will understand what makes a working environment safe.",
     prac="Graduates will understand what a safe working environment requires.",
     ben="You will understand what it takes to keep a workplace or laboratory safe.",
     aaw=a120(8, 'understanding of safe working', 'qaa/fheq-2024/annex-d/professional/r2/3rd-1st', '4.4.b4 (safe use of apparatus)'),
     aad=d120('a student starts lab work or a placement', 'what are the main hazards in this lab, and who would you tell about a problem?'))
k120(9, verbs=[], about='environmental and sustainability issues', domain='understanding',
     para="Will appreciate environmental and sustainability questions.",
     prac="Graduates will appreciate environmental and sustainability issues.",
     ben="You will understand environmental and sustainability issues and why they matter in physics.",
     aaw=a120(9, 'an appreciation of environmental and sustainability issues', 'spine:6', '1.35 to 1.39 (the sustainability theme)'),
     aad=d120('a student asks how physics connects to climate or energy', 'which part of your course connects most clearly to a sustainability problem?'))
k120(10, verbs=['include'], about='knowledge of professional practice', domain='knowledge',
     para="Will know about professional practice, for instance business awareness, project management, entrepreneurship and intellectual property.",
     prac="Graduates will know about professional practice, such as business awareness, project management, entrepreneurship and intellectual property.",
     ben="You will know how professional work in physics runs, from business and project management to entrepreneurship and intellectual property.",
     aaw=a120(10, 'knowledge of professional practice', 'qaa/fheq-2024/4.15.b9.3', '4.6.b9 and 1.40 to 1.46'),
     aad=d120('a student considers industry, a start-up or a placement', 'what do you know about how a physics company protects its ideas?'))

# ------------------------------------------------------------------ rungs
def a_rung(i, para_no, kind, about, fd, nb):
    if kind == 'th':
        head = (f"Describe {i} as part of the threshold the bachelor's degree with honours requires (FHEQ level 6, FQHEIS level 10), "
                f"the minimum the statement sets: {about}.")
        no = "Do not present it as the standard most graduates reach, since the statement expects most to exceed it, or as a regulatory requirement."
    elif kind == 'ty':
        head = (f"Describe {i} as the typical level for the bachelor's degree with honours (FHEQ level 6), what most graduates reach above the threshold: {about}.")
        no = "Do not present it as a minimum for the award or as an excellent rung, which the statement does not set."
    elif kind == 'mth':
        head = (f"Describe {i} as part of the threshold the integrated master's degree with honours requires (FHEQ level 7, FQHEIS level 11), "
                f"on top of the typical honours level: {about}.")
        no = "Do not apply it to the bachelor's degree or to a taught master's course, which the statement does not cover."
    else:
        head = (f"Describe {i} as the typical level for the integrated master's degree with honours (FHEQ level 7), above its threshold: {about}.")
        no = "Do not present it as the minimum for the integrated master's or apply it to the bachelor's degree."
    return f"{head} Cite it as ({CITE}{para_no}). {no} Set it beside {nb} and {fd}."

def d_rung(kind, when, q):
    frame = {'th': 'as something you should be able to do by graduation, the minimum',
             'ty': 'as what most graduates show, not a minimum',
             'mth': "as the minimum for the integrated master's",
             'mty': "as what most integrated master's graduates show, not a minimum"}[kind]
    avoid = {'th': 'Avoid reading the list aloud or treating this minimum as the goal.',
             'ty': 'Avoid presenting this typical level as the minimum to pass.',
             'mth': 'Avoid reading the list aloud or applying it to a bachelor\'s student.',
             'mty': "Avoid presenting this typical level as the minimum for the master's."}[kind]
    return (f"Raise it when {when}. Put it to a student in plain words, {frame}, and ask: {q} "
            f"With staff, ask where the course teaches and assesses it. {avoid}")

# 4.4 threshold: subject knowledge, understanding and skills
T44 = dict(type='threshold', rung='threshold', force='threshold', forceFrom='4.1', level='fheq:6', appliesTo='honours graduates at the threshold',
           addressee='learner', award=HON)
def k44(i, **k):
    s('4.4.b%d' % i, **T44, **k)
BT = 'By the time you graduate with honours, you should be able to '
k44(1, verbs=['understand', 'apply'], about='basic physical laws and principles', domain='understanding',
    para="Should be able to grasp and use the basic laws and principles of physics.",
    prac="At threshold, honours graduates should understand the basic laws and principles of physics and apply them.",
    ben=BT + "understand the basic laws and principles of physics and put them to use.",
    aaw=a_rung('4.4.b1', '4.4', 'th', 'understanding and using the basic laws and principles of physics', 'qaa/fheq-2024/4.15.b1 (with qaa/fqheis-2024/4.16.b1)', '4.4.b2 and 1.15'),
    aad=d_rung('th', 'a student doubts their grasp of the fundamentals', 'which basic law could you explain and use on a problem today without notes?'))
k44(2, verbs=['identify', 'use'], about='choosing laws for simple problems', domain='subject-skill',
    para="Should be able to pick out and use the laws and principles that bear on simple problems.",
    prac="At threshold, honours graduates should identify which physical laws and principles apply to a simple problem and use them.",
    ben=BT + "work out which physical laws apply to a straightforward problem and use them.",
    aaw=a_rung('4.4.b2', '4.4', 'th', 'selecting and using relevant laws on simple problems', 'qaa/fheq-2024/4.15.b3.1', '4.4.b3 and the typical item 4.6.b1'),
    aad=d_rung('th', 'a student can recall laws but not pick the right one', 'faced with this problem, how did you decide which principle to start from?'))
k44(3, verbs=['solve', 'using'], about='solving problems with mathematical and physical techniques', domain='subject-skill',
    para="Should be able to work physics problems through with fitting mathematical and physical methods.",
    prac="At threshold, honours graduates should solve physics problems using suitable mathematical and physical techniques.",
    ben=BT + "solve physics problems with the right mathematical and physical methods.",
    aaw=a_rung('4.4.b3', '4.4', 'th', 'problem solving with suitable mathematical and physical techniques', 'qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/cognitive/r3/3rd', '4.6.b2 (its typical counterpart) and 1.19'),
    aad=d_rung('th', 'a student struggles with problem sheets', 'where does a solution usually go wrong for you, the physics or the mathematics?'))
k44(4, verbs=['execute', 'analyse'], about='carrying out experiments safely', domain='subject-skill',
    para="Should be able, on an experimental course, to carry out an experiment, analyse its results and understand how to use basic apparatus safely.",
    prac="At threshold, honours graduates on experimental courses should run an experiment, analyse its results and use basic apparatus safely.",
    ben=BT + "run an experiment and analyse what it shows, using basic equipment safely, if your course includes lab work.",
    aaw=a_rung('4.4.b4', '4.4', 'th', 'executing and analysing an experiment with safe use of basic apparatus, on experimental courses only', 'qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r1/3rd', '4.6.b5 (its typical counterpart), 1.20.b8 and 1.12 (theoretical courses)'),
    aad=d_rung('th', 'a student prepares for lab work or asks about a theory-only route', 'in your last experiment, what did you check before trusting your results?'))
k44(5, verbs=['use'], about='software for data, simulation and information', domain='subject-skill',
    para="Should be able to use suitable software competently to analyse data, simulate physical systems and find information.",
    prac="At threshold, honours graduates should use suitable software packages or systems competently for data analysis, simulation and information retrieval.",
    ben=BT + "use the right software confidently to analyse data, simulate physical systems and find information.",
    aaw=a_rung('4.4.b5', '4.4', 'th', 'competent use of software for data analysis, simulation and finding information', 'qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/transferable/r1/3rd', '4.6.b6, 4.5.b9 and 3.5'),
    aad=d_rung('th', 'a student talks about coding or data tools', 'which software do you reach for to analyse or simulate, and what can you not yet do with it?'))
k44(6, verbs=['undertake', 'present', 'interpret'], about='handling data numerically and graphically', domain='subject-skill',
    para="Should be able to manipulate data numerically and show and read information in graphs.",
    prac="At threshold, honours graduates should handle data numerically and present and interpret information graphically.",
    ben=BT + "work with data numerically and present and read information in graphs.",
    aaw=a_rung('4.4.b6', '4.4', 'th', 'numerical handling of data and graphical presentation and interpretation', 'qaa/fheq-2024/annex-d/practical/r4/3rd', '4.4.b7 and 4.5.b8'),
    aad=d_rung('th', 'a student prepares figures or a data analysis', 'what does this graph tell a reader at a glance?'))
k44(7, verbs=['perform', 'analyse'], about='investigation with uncertainty and limits', domain='subject-skill',
    para="Should be able to carry out an investigation and analyse its results, including judging their uncertainty or limitations.",
    prac="At threshold, honours graduates should conduct an investigation and analyse its results, evaluating their uncertainty or limitations.",
    ben=BT + "carry out an investigation, analyse what you find and judge how uncertain or limited your results are.",
    aaw=a_rung('4.4.b7', '4.4', 'th', 'carrying out an investigation and analysing results with their uncertainty and limits', 'qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/4.15.b6', '4.6.b4 (its typical counterpart) and 1.20.b7'),
    aad=d_rung('th', 'a student writes up a project or lab report', 'how sure are you of this result, and what limits it?'))
k44(8, verbs=['communicate'], about='communicating scientific information to audiences', domain='subject-skill',
    para="Should be able to convey scientific information to varied audiences, usually through visualisations, reports or presentations.",
    prac="At threshold, honours graduates should communicate scientific information for a range of audiences through visuals, reports or presentations.",
    ben=BT + "explain scientific information to different audiences through figures, reports or talks.",
    aaw=a_rung('4.4.b8', '4.4', 'th', 'communicating scientific information for several audiences', 'qaa/fheq-2024/4.15.b8', '4.6.b7 (its typical counterpart), 4.5.b6 and 1.20.b2'),
    aad=d_rung('th', 'a student prepares a report, talk or poster', 'how would you change this for a non-specialist audience?'))
k44(9, verbs=['articulate'], about='articulating the value of the degree', domain='generic-skill',
    para="Should be able to explain the worth of the skills, knowledge and behaviours their degree has given them.",
    prac="At threshold, honours graduates should articulate the value of what their physics degree has developed in them.",
    ben=BT + "explain clearly what your degree has given you in skills, knowledge and behaviours, for example to an employer.",
    aaw=a_rung('4.4.b9', '4.4', 'th', 'explaining the value of what the degree has developed, a generic skill', 'qaa/fheq-2024/4.15.b9.3 and qaa/fheq-2024/annex-d/transferable/r5/3rd', '1.43 (the course duty that supports it) and 1.20.b10'),
    aad=d_rung('th', 'a student prepares a CV, application or interview', 'which three skills from your degree would you lead with, and what evidence do you have?'))

# 4.5 threshold: generic skills
T45 = dict(T44, domain='generic-skill')
def k45(i, **k):
    s('4.5.b%d' % i, **T45, **k)
BG = 'By graduation, as a general skill, you should be able to '
k45(1, verbs=['identify'], about='identifying issues and problems',
    para="Should be able to recognise issues, questions and problems.", prac="At threshold, honours graduates should identify issues, questions and problems.",
    ben=BG + "spot the issues, questions and problems in a situation.",
    aaw=a_rung('4.5.b1', '4.5', 'th', 'identifying issues, questions and problems, a generic skill', 'qaa/fheq-2024/4.15.b7', '4.5.b3 and 1.20.b1'),
    aad=d_rung('th', 'a student begins a project or open problem', 'what exactly is the question here?'))
k45(2, verbs=['identify', 'acquire'], about='closing gaps in one\'s own knowledge',
    para="Should be able to find gaps in their own knowledge and fill them.", prac="At threshold, honours graduates should identify gaps in their knowledge and acquire what they need.",
    ben=BG + "notice what you do not yet know and go and learn it.",
    aaw=a_rung('4.5.b2', '4.5', 'th', 'finding and filling gaps in one\'s own knowledge', 'qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/transferable/r3/3rd', '4.5.b10 and 4.6.b8'),
    aad=d_rung('th', 'a student meets a topic they have not covered', 'what do you need to learn for this, and where will you find it?'))
k45(3, verbs=['analyse', 'interpret'], about='analysing and interpreting information',
    para="Should be able to analyse and make sense of information.", prac="At threshold, honours graduates should analyse and interpret information.",
    ben=BG + "analyse information and work out what it means.",
    aaw=a_rung('4.5.b3', '4.5', 'th', 'analysis and interpretation of information', 'qaa/fheq-2024/4.15.b7', '4.5.b8 and 4.4.b6'),
    aad=d_rung('th', 'a student reads a source or dataset', 'what does this information show, and what does it not show?'))
k45(4, verbs=['synthesise'], about='synthesising knowledge on a topic',
    para="Should be able to pull together what is known about a given topic.", prac="At threshold, honours graduates should synthesise the current state of knowledge on a topic.",
    ben=BG + "bring together what is known on a topic into a clear overview.",
    aaw=a_rung('4.5.b4', '4.5', 'th', 'synthesising what is known on a topic', 'qaa/fheq-2024/4.15.b3.2 and qaa/fheq-2024/annex-d/cognitive/r1/3rd', '4.6.b8 and 1.18'),
    aad=d_rung('th', 'a student writes a literature review or project introduction', 'what are the two or three main things known on this topic, and where do sources disagree?'))
k45(5, verbs=['apply', 'provide'], about='evidenced conclusions',
    para="Should be able to use their knowledge and understanding to reach conclusions backed by evidence.", prac="At threshold, honours graduates should apply knowledge and understanding to reach evidenced conclusions.",
    ben=BG + "use what you know to reach conclusions you can back with evidence.",
    aaw=a_rung('4.5.b5', '4.5', 'th', 'reaching conclusions supported by evidence', 'qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r2/3rd', '4.4.b7 and 4.6.b4'),
    aad=d_rung('th', 'a student drafts a conclusion', 'which evidence supports this conclusion most strongly?'))
k45(6, verbs=['communicate'], about='effective, fitting communication',
    para="Should be able to communicate well and in a way that fits the situation.", prac="At threshold, honours graduates should communicate effectively and appropriately.",
    ben=BG + "communicate well and in a way that suits the situation.",
    aaw=a_rung('4.5.b6', '4.5', 'th', 'effective and appropriate communication, a generic skill', 'qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/3rd', '4.4.b8 and 4.5.b7'),
    aad=d_rung('th', 'a student prepares any written or spoken work', 'who will read or hear this, and what tone suits them?'))
k45(7, verbs=['present'], about='presenting knowledge or argument clearly',
    para="Should be able to set out knowledge or an argument so that others can follow it.", prac="At threshold, honours graduates should present knowledge or an argument comprehensibly to others.",
    ben=BG + "set out what you know or an argument so others can follow it.",
    aaw=a_rung('4.5.b7', '4.5', 'th', 'presenting knowledge or argument so others can follow it', 'qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/cognitive/r2/3rd', '4.5.b6 and 4.4.b8'),
    aad=d_rung('th', 'a student plans an essay, talk or viva', 'could someone outside physics follow your argument step by step?'))
k45(8, verbs=['work'], about='working with qualitative and quantitative data',
    para="Should be able to handle many kinds of data, qualitative and quantitative empirical data among them.", prac="At threshold, honours graduates should work with a range of data, both qualitative and quantitative.",
    ben=BG + "work with many kinds of data, numerical and descriptive.",
    aaw=a_rung('4.5.b8', '4.5', 'th', 'working with a range of qualitative and quantitative data', 'qaa/fheq-2024/annex-d/transferable/r1/3rd', '4.4.b6 and 4.5.b3'),
    aad=d_rung('th', 'a student meets non-numerical evidence, such as interview or survey data', 'how would you handle evidence here that is not a number?'))
k45(9, verbs=['engage', 'collate', 'analyse', 'select', 'present'], about='critical use of digital technology',
    para="Should be able to use varied digital technologies critically to gather, analyse, choose and present information.", prac="At threshold, honours graduates should engage critically with varied digital technologies to collate, analyse, select and present information.",
    ben=BG + "use a range of digital tools critically to gather, analyse, choose and present information.",
    aaw=a_rung('4.5.b9', '4.5', 'th', 'critical engagement with digital technology for information', 'qaa/fheq-2024/annex-d/transferable/r1/3rd', '4.4.b5 and 1.51 (generative AI)'),
    aad=d_rung('th', 'a student relies on a digital tool or AI output', 'how do you know this tool gave you something reliable?'))
k45(10, verbs=['assert', 'undertaking', 'conducting', 'demonstrating'], about='intellectual independence',
    para="Should be able to show intellectual independence: working alone with suitable guidance, carrying out self-directed research and exercising critical judgement.", prac="At threshold, honours graduates should show intellectual independence, working independently with guidance, doing self-directed research and judging critically.",
    ben=BG + "show independent thinking: working on your own with the right guidance, doing your own research and judging critically.",
    aaw=a_rung('4.5.b10', '4.5', 'th', 'intellectual independence with guidance', 'qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r3/3rd', '4.5.b2, 4.7.b2.masters and 1.20.b3'),
    aad=d_rung('th', 'a student moves into a project or dissertation', 'what decisions in this project did you make yourself, and where did you seek guidance?'))
s('4.5.b11', **T45, find='work collaboratively, including undertaking work in a group or team and/or participating in discussions, showing an appreciation for diversity within the group.',
  verbs=['work', 'undertaking', 'participating', 'showing'], about='collaboration that values diversity',
  para="Should be able to work with others, in groups, teams or discussion, valuing the diversity of the group.", prac="At threshold, honours graduates should collaborate in groups, teams or discussion and appreciate the group's diversity.",
  ben=BG + "work with others in groups or discussions and value the different people in the group.",
  aaw=a_rung('4.5.b11', '4.5', 'th', 'collaboration that appreciates diversity', 'qaa/fheq-2024/annex-d/transferable/r2/3rd', '1.20.b3 and 1.24 (EDI awareness)'),
  aad=d_rung('th', 'a student reflects on team projects or group tension', 'how did the different backgrounds in your group help the work?'))

# 4.6 typical, bachelor's with honours (lead-in: has demonstrated ... in addition, competence in)
TY = dict(type='typical', rung='typical', force='will', forceFrom='4.1', level='fheq:6', appliesTo='honours graduates at the typical level',
          addressee='learner', award=HON)
def k46(i, **k):
    s('4.6.b%d' % i, **TY, **k)
BY = 'At the typical level for an honours degree, you will have shown '
k46(1, verbs=[], about='applying principles across diverse areas', domain='subject-skill',
    para="Will have shown competence in applying physical principles across varied areas of physics.",
    prac="At the typical level, honours graduates will have applied physical principles competently across diverse areas of physics.",
    ben=BY + "you can apply physical principles across many different areas of physics.",
    aaw=a_rung('4.6.b1', '4.6', 'ty', 'applying physical principles across diverse areas', 'qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/annex-d/knowledge/r2/2.1', '4.4.b2 (the threshold item it grades) and 4.8.b1.masters'),
    aad=d_rung('ty', 'a student wants to move beyond the minimum', 'which principle have you used in two very different areas of physics?'))
k46(2, verbs=['selecting', 'using'], about='choosing techniques to solve problems', domain='subject-skill',
    para="Will have shown competence in solving physics problems by choosing and using fitting mathematical and physical techniques.",
    prac="At the typical level, honours graduates will have solved problems by choosing for themselves, and then using, suitable mathematical and physical techniques.",
    ben=BY + "you can solve physics problems by choosing the right mathematical and physical methods yourself.",
    aaw=a_rung('4.6.b2', '4.6', 'ty', 'selecting as well as using techniques to solve problems', 'qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/cognitive/r3/2.1', '4.4.b3 (the threshold item it grades)'),
    aad=d_rung('ty', 'a student can follow worked methods but not choose them', 'why did you pick this method over another?'))
k46(3, verbs=['making', 'solving'], about='making approximations', domain='subject-skill',
    para="Will have shown competence in making suitable approximations when solving problems.",
    prac="At the typical level, honours graduates will have made appropriate approximations when solving problems.",
    ben=BY + "you can make sensible approximations when solving problems.",
    aaw=a_rung('4.6.b3', '4.6', 'ty', 'making appropriate approximations', 'qaa/fheq-2024/4.15.b4', '1.5 (models and approximation) and 1.19 (estimation)'),
    aad=d_rung('ty', 'a student is unsure when an approximation is safe', 'what did you neglect here, and how would you check it was safe to do so?'))
k46(4, verbs=['setting'], about='critical analysis and context of results', domain='subject-skill',
    para="Will have shown competence in analysing experimental or investigative results critically, judging their conceptual and statistical significance and placing them in context against expectations, models or published data.",
    prac="At the typical level, honours graduates will have critically analysed results, evaluated their conceptual and statistical significance and compared them with expected outcomes, models or published data.",
    ben=BY + "you can analyse your results critically, judge how significant they are and compare them with theory, models or published work.",
    aaw=a_rung('4.6.b4', '4.6', 'ty', 'critical analysis of results, their significance and their context', 'qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/practical/r4/2.1', '4.4.b7 (the threshold item it grades) and 4.8.b7.masters'),
    aad=d_rung('ty', 'a student writes the discussion of a report', 'how does your result compare with theory or published data, and is the difference significant?'))
k46(5, verbs=[], about='designing and running experiments', domain='subject-skill',
    para="Will have shown competence, on an experimental course, in designing and carrying out experiments.",
    prac="At the typical level, honours graduates on experimental courses will have designed and executed experiments.",
    ben=BY + "you can design and carry out your own experiments, if your course includes lab work.",
    aaw=a_rung('4.6.b5', '4.6', 'ty', 'designing as well as executing experiments, on experimental courses only', 'qaa/fheq-2024/4.15.b6', '4.4.b4 (the threshold item it grades) and 3.4'),
    aad=d_rung('ty', 'a student moves from scripted to open lab work', 'what would you change in this experiment if you designed it from scratch?'))
k46(6, verbs=['model'], about='mathematical and computational modelling', domain='subject-skill',
    para="Will have shown competence in using mathematical and computational techniques and analysis to model how physical systems behave.",
    prac="At the typical level, honours graduates will have modelled physical behaviour with mathematical and computational techniques.",
    ben=BY + "you can build mathematical and computer models of how physical systems behave.",
    aaw=a_rung('4.6.b6', '4.6', 'ty', 'modelling physical behaviour mathematically and computationally', 'qaa/fheq-2024/4.15.b2', '4.4.b5 (the threshold item it grades, a weaker match) and 1.6'),
    aad=d_rung('ty', 'a student works on simulation or modelling', 'what does your model leave out, and does it matter?'))
k46(7, verbs=[], about='clear communication to different audiences', domain='subject-skill',
    para="Will have shown competence in communicating scientific information clearly and accurately to different audiences.",
    prac="At the typical level, honours graduates will have communicated scientific information clearly and accurately to varied audiences.",
    ben=BY + "you can explain science clearly and accurately to different audiences.",
    aaw=a_rung('4.6.b7', '4.6', 'ty', 'clear and accurate communication to different audiences', 'qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/transferable/r1/2.1', '4.4.b8 (the threshold item it grades) and 4.8.b7.masters'),
    aad=d_rung('ty', 'a student prepares outreach or a final presentation', 'how would you check that your audience understood you correctly?'))
k46(8, verbs=[], about='managing and using research-based materials', domain='subject-skill',
    para="Will have shown competence in managing and using research-based materials.",
    prac="At the typical level, honours graduates will have managed and used research-based materials competently.",
    ben=BY + "you can find, organise and use research papers and other research-based sources.",
    aaw=a_rung('4.6.b8', '4.6', 'ty', 'managing and using research-based materials', 'qaa/fheq-2024/4.15.b5', '1.18, 4.5.b4 and 4.7.b3.masters'),
    aad=d_rung('ty', 'a student starts a literature search', 'how do you keep track of the papers you read and decide which to rely on?'))
s('4.6.b9', **TY, find='where appropriate, an appreciation of topics related to enterprise and entrepreneurship\n- for example, with design thinking, innovation, project and risk management, business and financial awareness, and commercialisation.',
  verbs=[], about='enterprise and entrepreneurship', domain='understanding',
  para="Will have shown, where appropriate, an appreciation of enterprise and entrepreneurship, such as design thinking, innovation, managing projects and risk, business and finance and bringing products to market.",
  prac="At the typical level and where the course offers it, honours graduates will have an appreciation of enterprise and entrepreneurship topics, from design thinking and innovation to risk, business, finance and commercialisation.",
  ben=BY + "an understanding of enterprise and entrepreneurship, such as design thinking, innovation and turning ideas into products, where your course covers it.",
  aaw=a_rung('4.6.b9', '4.6', 'ty', 'an appreciation of enterprise and entrepreneurship where appropriate', 'qaa/fheq-2024/4.15.b9.1', '1.20.b10, 1.40 to 1.46 (the enterprise theme)'),
  aad=d_rung('ty', 'a student is curious about start-ups or commercial physics', 'how could an idea from your project become a product or service?'))

# 4.7 integrated master's threshold (lead-in: will also have); another award, not another rung
MT = dict(type='threshold', rung='threshold', force='threshold', forceFrom='4.3', level='fheq:7', appliesTo="integrated master's graduates at the threshold",
          addressee='learner', award=IM)
BM = "To reach the minimum for an integrated master's, you will also have "
s('4.7.b1.masters', **MT, find='a working knowledge of a variety of experimental, mathematical and/or computational techniques applicable to current research or applications in Physics',
  verbs=[], about='techniques used in current research', domain='subject-skill',
  para="Will also have a working command of a range of experimental, mathematical or computational techniques used in current physics research or applications.",
  prac="At the integrated master's threshold, graduates will have working knowledge of varied experimental, mathematical or computational techniques used in current research or applications.",
  ben=BM + "a working command of several experimental, mathematical or computing techniques used in current physics research.",
  aaw=a_rung('4.7.b1.masters', '4.7', 'mth', 'working knowledge of techniques used in current research', 'qaa/fheq-2024/4.17.b2 and spine:7', '4.8.b5.masters (its typical counterpart) and the honours typical list 4.6'),
  aad=d_rung('mth', 'an integrated master\'s student chooses project methods', 'which research technique could you use without step-by-step help?'))
s('4.7.b2.masters', **MT, find='undertaken an extended investigation',
  verbs=['undertaken'], about='an extended investigation', domain='subject-skill',
  para="Will also have carried out an extended investigation.",
  prac="At the integrated master's threshold, graduates will have completed an extended investigation.",
  ben=BM + "completed an extended investigation of your own.",
  aaw=a_rung('4.7.b2.masters', '4.7', 'mth', 'having completed an extended investigation', 'qaa/fheq-2024/4.17.b6', '4.8.b4.masters (its typical counterpart) and 1.13'),
  aad=d_rung('mth', 'a student plans the master\'s project', 'how will this investigation be longer and deeper than your bachelor\'s-level work?'))
s('4.7.b3.masters', **MT, find='encountered research-level material.',
  verbs=['encountered'], about='research-level material', domain='knowledge',
  para="Will also have met material at research level.",
  prac="At the integrated master's threshold, graduates will have engaged with research-level material.",
  ben=BM + "worked with material at the level of current research.",
  aaw=a_rung('4.7.b3.masters', '4.7', 'mth', 'having met research-level material', 'qaa/fheq-2024/4.17.b1', '4.8.b2.masters, 4.8.b8.masters and 1.18'),
  aad=d_rung('mth', 'a student first reads research papers in depth', 'which research-level paper have you worked through, and what did you take from it?'))

# 4.8 integrated master's typical (lead-in: has demonstrated ... in addition an ability to)
MY = dict(type='typical', rung='typical', force='will', forceFrom='4.7', level='fheq:7', appliesTo="integrated master's graduates at the typical level",
          addressee='learner', award=IM)
BMY = "At the typical integrated master's level, you will be able to "
def k48(i, find, **k):
    s('4.8.b%d.masters' % i, **MY, find=find, **k)
k48(1, 'apply fundamental laws and principles to a variety of areas in Physics, some of which are at (or are informed by) the forefront of the discipline',
    verbs=['apply'], about='applying laws to areas at the forefront', domain='subject-skill',
    para="Will be able to apply fundamental laws and principles across several areas of physics, some at or informed by the forefront.",
    prac="At the integrated master's typical level, graduates will apply fundamental laws and principles to varied areas, some at or near the forefront.",
    ben=BMY + "apply the fundamental laws of physics to several areas, including some at the leading edge.",
    aaw=a_rung('4.8.b1.masters', '4.8', 'mty', 'applying fundamental laws to areas at or near the forefront', 'qaa/fheq-2024/4.17.b1', '4.6.b1 and 4.8.b2.masters'),
    aad=d_rung('mty', 'a student connects coursework to current research', 'which leading-edge area can you analyse with the laws you already know?'))
k48(2, 'apply relevant, recent, research to current questions in Physics',
    verbs=['apply'], about='applying recent research to current questions', domain='subject-skill',
    para="Will be able to bring recent, relevant research to bear on current questions in physics.",
    prac="At the integrated master's typical level, graduates will apply relevant recent research to current questions.",
    ben=BMY + "use recent research to tackle open questions in physics.",
    aaw=a_rung('4.8.b2.masters', '4.8', 'mty', 'applying recent research to current questions', 'qaa/fheq-2024/4.17.b4.1', '4.7.b3.masters and 4.8.b8.masters'),
    aad=d_rung('mty', 'a student frames a research question', 'which recent result changes how you would approach this question?'))
k48(3, 'interpret and contextualise mathematical descriptions of physical phenomena',
    verbs=['interpret', 'contextualise'], about='interpreting mathematical descriptions', domain='understanding',
    para="Will be able to interpret mathematical descriptions of physical phenomena and set them in context.",
    prac="At the integrated master's typical level, graduates will interpret and contextualise mathematical descriptions of physical phenomena.",
    ben=BMY + "read the mathematics behind a physical phenomenon and explain what it means and where it fits.",
    aaw=a_rung('4.8.b3.masters', '4.8', 'mty', 'interpreting and contextualising mathematical descriptions', 'qaa/fheq-2024/4.17.b3', '4.6.b6 and 1.5'),
    aad=d_rung('mty', 'a student can manipulate equations but not explain them', 'what does each term in this equation mean physically?'))
k48(4, 'plan and execute an open-ended extended research project or investigation, demonstrating some originality',
    verbs=['plan', 'execute', 'demonstrating'], about='an open-ended research project with originality', domain='subject-skill',
    para="Will be able to plan and carry out an open-ended, extended research project or investigation that shows some originality.",
    prac="At the integrated master's typical level, graduates will plan and carry out an open-ended extended research project showing some originality.",
    ben=BMY + "plan and run an open-ended research project of your own that shows some original thinking.",
    aaw=a_rung('4.8.b4.masters', '4.8', 'mty', 'planning and executing an open-ended project with some originality', 'qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b3', '4.7.b2.masters (the threshold item it grades)'),
    aad=d_rung('mty', 'a student scopes the master\'s project', 'what part of this project is your own idea?'))
k48(5, 'show the competent use of specialised equipment or research grade software or methods',
    verbs=['show'], about='specialised equipment and research-grade tools', domain='subject-skill',
    para="Will be able to use specialised equipment or research-grade software or methods competently.",
    prac="At the integrated master's typical level, graduates will use specialised equipment or research-grade software or methods competently.",
    ben=BMY + "use specialist equipment or research-grade software and methods with confidence.",
    aaw=a_rung('4.8.b5.masters', '4.8', 'mty', 'confident handling of specialist instruments or research-grade codes and methods', 'qaa/fheq-2024/4.17.b2', '4.7.b1.masters (the threshold item it grades)'),
    aad=d_rung('mty', 'a student learns a research instrument or code base', 'which research tool can you now use without supervision?'))
k48(6, 'master new techniques in a theoretical, computational or experimental context',
    verbs=['master'], about='mastering new techniques', domain='subject-skill',
    para="Will be able to learn new theoretical, computational or experimental techniques thoroughly.",
    prac="At the integrated master's typical level, graduates will master new techniques in theoretical, computational or experimental work.",
    ben=BMY + "pick up and master new theoretical, computing or lab techniques.",
    aaw=a_rung('4.8.b6.masters', '4.8', 'mty', 'mastering new techniques', 'qaa/fheq-2024/4.17.b7', '4.5.b2 and 4.8.b5.masters'),
    aad=d_rung('mty', 'a student must learn a method not taught in class', 'how did you learn the last new technique you needed?'))
k48(7, 'communicate complex scientific ideas, including the concise, accurate and informative conclusions of an experiment, investigation or project',
    verbs=['communicate'], about='communicating complex ideas and conclusions', domain='subject-skill',
    para="Will be able to convey complex scientific ideas, including brief, precise and informative conclusions from an experiment, investigation or project.",
    prac="At the integrated master's typical level, graduates will communicate complex ideas and give concise, accurate conclusions from their work.",
    ben=BMY + "explain complex scientific ideas and give short, accurate and useful conclusions from your work.",
    aaw=a_rung('4.8.b7.masters', '4.8', 'mty', 'communicating complex ideas and concise conclusions', 'qaa/fheq-2024/4.17.b5', '4.6.b7 and 4.6.b4'),
    aad=d_rung('mty', 'a student writes an abstract or final talk', 'can you state your main conclusion in two sentences?'))
k48(8, 'demonstrate an understanding of scientific research and propose realistic suggestions as to how it may progress further.',
    verbs=['demonstrate', 'propose'], about='understanding research and how it may progress', domain='understanding',
    para="Will be able to show an understanding of scientific research and suggest realistic next steps for it.",
    prac="At the integrated master's typical level, graduates will understand scientific research and propose realistic ways it could progress.",
    ben=BMY + "show you understand how research works and suggest realistic next steps for it.",
    aaw=a_rung('4.8.b8.masters', '4.8', 'mty', 'understanding research and proposing how it may progress', 'qaa/fheq-2024/4.17.b4.2', '4.8.b2.masters and 4.7.b3.masters'),
    aad=d_rung('mty', 'a student ends a project or plans further study', 'what would you do next if you had another year on this work?'))

# gradeOf: same outcome one rung below, same domain and award; inferred (the lists are not paired)
GRADE = {'4.6.b1': '4.4.b2', '4.6.b2': '4.4.b3', '4.6.b4': '4.4.b7', '4.6.b5': '4.4.b4', '4.6.b6': '4.4.b5', '4.6.b7': '4.4.b8',
         '4.8.b4.masters': '4.7.b2.masters', '4.8.b5.masters': '4.7.b1.masters'}

TH = {'1.22': 'theme:edi', '1.23': 'theme:edi', '1.24': 'theme:edi', '1.25': 'theme:edi', '1.26': 'theme:edi',
      '1.27': 'theme:accessibility', '1.29': 'theme:accessibility', '1.30': 'theme:accessibility', '1.31': 'theme:accessibility',
      '1.32': 'theme:accessibility', '1.33': 'theme:accessibility', '1.34': 'theme:accessibility',
      '1.43': 'theme:enterprise',
      '1.48': 'theme:generative-ai', '1.49': 'theme:generative-ai', '1.50': 'theme:generative-ai', '1.51': 'theme:generative-ai'}

S5 = dict(levels=[
    dict(id='fheq:6', role='cites', locator='D1, 2.3'), dict(id='fheq:7', role='cites', locator='D1, 2.3'),
    dict(id='fqheis:10', role='cites', locator='D1, 2.3'), dict(id='fqheis:11', role='cites', locator='D1, 2.3'),
    dict(id='fheq:4', role='cites', locator='D1, 2.6 (exit award)'), dict(id='fheq:5', role='cites', locator='D1, 2.6 (exit award)'),
    dict(id='fqheis:8', role='cites', locator='D1, 2.6 (stated for the CertHE; the frameworks place it at fqheis:7: Part E)'),
    dict(id='fqheis:9', role='cites', locator='D1, 2.6 (stated for the DipHE; the frameworks place it at fqheis:8: Part E)'),
    dict(id='spine:6', role='reads-against', locator='std:ref:uk-framework R2, R8 (inferred)'),
    dict(id='spine:7', role='reads-against', locator='std:ref:uk-framework R2, R8 (inferred)')],
    crosswalks=[
        dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis="stated (D1, 2.3: the standard undergraduate degree with honours); agrees with std:doc:qaa-fheq-2024-framework Table 1"),
        dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.3: the integrated master's); agrees with std:doc:qaa-fheq-2024-framework Table 1"),
        dict(**{'from': 'fheq:4'}, to='fqheis:8', relation='equivalent', basis='stated (D1, 2.6, CertHE); conflicts with std:doc:qaa-fheq-2024-framework Table 1 (CertHE at SCQF 7): Part E'),
        dict(**{'from': 'fheq:5'}, to='fqheis:9', relation='equivalent', basis='stated (D1, 2.6, DipHE); conflicts with std:doc:qaa-fheq-2024-framework Table 1 (DipHE at SCQF 8): Part E')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.22', '1.23', '1.24', '1.25', '1.26']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.24', '1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '3.7', '3.8']),
      dict(id='theme:esd', role='carries', carriedIn=['1.2', '1.20', '1.35', '1.36', '1.37', '1.38', '1.39']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.14', '1.20', '1.40', '1.41', '1.42', '1.43', '1.44', '1.45', '1.46', '3.10', '4.6']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['1.47', '1.48', '1.49', '1.50', '1.51', '3.5', '3.9'])]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-physics-astronomy-and-astrophysics-<previous year>-benchmarks (not yet ingested)', note='the front matter names key changes from the previous statement without its date; the advisory group list names a 2019 minor update: Part E'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the four honours classifications, for achievement above the threshold (4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note="levels 4 to 7 named in 2.3 and 2.6; the Frameworks document named in 2.3 and 4.2"),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 8 to 11 named in 2.3 and 2.6'),
    dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='listed in the references (section 5); the ESD theme 1.35 to 1.39'),
    dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='listed in the references (section 5); the enterprise theme 1.40 to 1.46'),
    dict(rel='refersTo', target='QAA Quality Code 2024 (not yet ingested)', note='front matter; references'),
    dict(rel='refersTo', target='Institute of Physics accreditation requirements (not yet ingested)', note='2.16'),
    dict(rel='refersTo', target='Disabled Student Commitment (not yet ingested)', note='1.30'),
]

SB1 = [
    'The study of natural phenomena and made systems by observation, understanding and prediction; astronomy and astrophysics share its core and apply it to astrophysical systems (D1, 1.1, 1.17).',
    'It explains much with little: a few key quantities, such as energy and momentum, and universal laws that hold well beyond physics (D1, 1.4).',
    'It works through idealised mathematical models and approximation, and models often transfer between very different systems (D1, 1.5).',
    'Computation and, increasingly, machine learning are central to modelling and data analysis (D1, 1.6).',
    'It is empirical: measurement tests theory and new instruments open new fields and spread to other sciences (D1, 1.7).',
    'It is hierarchical, lending itself to ordered, cumulative learning, and it feeds many neighbouring disciplines (D1, 1.3, 3.2).',
    'Progress rests on imagination and collaboration across cultures and sub-fields (D1, 1.8).',
    "Degrees share a common core with provider-specific options; the integrated master's adds research depth and extended project work (D1, 1.13, 2.1).",
]
SB2 = [
    dict(theme='theme:edi', inThisSubject='named Equity, diversity and inclusion: physics open to all, a curriculum that reflects who built the discipline, safe placements and field trips and a culture all share in building (D1, 1.22 to 1.26)',
         statements=['1.22', '1.23', '1.24', '1.25', '1.26']),
    dict(theme='theme:accessibility', inThisSubject='named Accessibility and the needs of disabled students: inclusive design first, then adjustments; the Disabled Student Commitment; the particular difficulty of making code, mathematics and diagrams accessible; equal access to placements (D1, 1.27 to 1.34; 3.7)',
         statements=['1.27', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '3.7']),
    dict(theme='theme:esd', inThisSubject="physics' part in the UN goals through instruments, models and technologies for energy and climate, with examples from ice cores to LEDs; sustainability embedded through problems, projects and lectures (D1, 1.35 to 1.39); graduates appreciate sustainability issues (1.20)",
         statements=['1.20.b9']),
    dict(theme='theme:enterprise', inThisSubject="enterprise, entrepreneurship and employability defined; physics' innovation fields and spinouts; careers advisers help students articulate their degree's value; enterprise topics at the typical honours level (D1, 1.40 to 1.46; 4.6)",
         statements=['1.43', '1.20.b10', '4.6.b9']),
    dict(theme='theme:generative-ai', inThisSubject='guiding principles rather than rules: guided practice in the curriculum, assessment that recognises AI, responsible use and critique of output; AI also appears among computing skills and assessment methods (D1, 1.47 to 1.51; 3.5; 3.9)',
         statements=['1.48', '1.49', '1.50', '1.51']),
]
SB3 = dict(areas=[
    dict(component='1.15', gloss='the fundamental areas: mechanics, relativity, quantum, electromagnetism, thermal and statistical physics, light and waves, matter'),
    dict(component='1.16', gloss='application areas such as astrophysics, condensed matter, medical, nuclear and particle physics, optics and plasmas'),
    dict(component='1.17', gloss='astronomy and astrophysics topics: cosmology, stars and galaxies, planetary systems, high-energy phenomena'),
    dict(component='1.19', gloss='what all degrees cover in some measure: mathematics, computing, problem solving, estimation, experiment planning, project management, data analysis')],
    practices=[
        dict(component='3.2', kind='teaching', gloss='lectures with problem classes, flipped classes, tutorials, labs, observing, projects, team work, placements'),
        dict(component='3.4', kind='learning', gloss='skills through physics applications; lab work more open-ended at higher levels'),
        dict(component='3.9', kind='assessment', gloss='exams and tests, adaptive testing, lab books, projects, posters, vivas, critical use of AI output, reflection, peer and self-assessment'),
        dict(component='3.10', kind='assessment', gloss='assessment styles matched to outcomes')])
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.4', award=HON, items=9),
           dict(rung='threshold', leadIn='4.5', award=HON, items=11),
           dict(rung='typical', leadIn='4.6', award=HON, items=9),
           dict(rung='threshold', leadIn='4.7', award=IM, items=3),
           dict(rung='typical', leadIn='4.8', award=IM, items=8),
           dict(rung='excellent', leadIn='none', award='none stated', items=0)],
    rungBases='4.1 sets minimum threshold and typical standards only; 4.2 leaves achievement above threshold to Annex D. Threshold is split into subject (4.4) and generic (4.5) lists; each typical list and the master\'s threshold build on the rung below by an explicit "in addition".',
    outcomeLists=[dict(leadIn='1.20', gloss='professional skills graduates will have developed', items=10, award=['honours', "integrated master's"])],
    outcomes=[
        dict(outcome='applying principles to problems and areas', threshold='4.4.b2', typical='4.6.b1', excellent='none', basis='inferred', domain='subject-skill', award=HON),
        dict(outcome='solving problems with techniques', threshold='4.4.b3', typical='4.6.b2', excellent='none', basis='inferred', domain='subject-skill', award=HON),
        dict(outcome='analysing results of investigations', threshold='4.4.b7', typical='4.6.b4', excellent='none', basis='inferred', domain='subject-skill', award=HON),
        dict(outcome='experiments', threshold='4.4.b4', typical='4.6.b5', excellent='none', basis='inferred', domain='subject-skill', award=HON),
        dict(outcome='computation and modelling', threshold='4.4.b5', typical='4.6.b6', excellent='none', basis='inferred', domain='subject-skill', award=HON),
        dict(outcome='communicating science', threshold='4.4.b8', typical='4.6.b7', excellent='none', basis='inferred', domain='subject-skill', award=HON),
        dict(outcome='extended investigation and research project', threshold='4.7.b2.masters', typical='4.8.b4.masters', excellent='none', basis='inferred', domain='subject-skill', award=IM),
        dict(outcome='research techniques and tools', threshold='4.7.b1.masters', typical='4.8.b5.masters', excellent='none', basis='inferred', domain='subject-skill', award=IM)])
SB4A_FULL = []
SB5 = [
    dict(body='Institute of Physics', says='many physics, astronomy and astrophysics degrees go through its accreditation review (D1, 2.16); it is represented on the advisory group (back matter)', requirements='not yet ingested (Part E)'),
    dict(body='Equality and Human Rights Commission', says='providers setting competence standards should follow its latest guidance (D1, 4.3)', requirements='not yet ingested (Part E)'),
    dict(body='professional, statutory and regulatory bodies (PSRBs), unnamed', says='the statement can support their reading of academic standards; their requirements are among the reference points providers weigh and can inform competence standards (D1, front matter; 4.3)', requirements='not-applicable-by-design'),
    dict(body='Office for Students', says='in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)', requirements='not-applicable-by-design'),
]
SB6 = dict(
    themes=[
        dict(id='theme:edi', named='Equity, diversity and inclusion', carriedIn=['front matter', '1.22', '1.23', '1.24', '1.25', '1.26'], statements=['1.22', '1.23', '1.24', '1.25', '1.26']),
        dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=['front matter', '1.24', '1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '3.7', '3.8'], statements=['1.27', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '3.7']),
        dict(id='theme:esd', named='Education for sustainable development', carriedIn=['front matter', '1.2', '1.20', '1.35', '1.36', '1.37', '1.38', '1.39', 'section 5'], statements=['1.20.b9']),
        dict(id='theme:enterprise', named='Employability, enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education; 1.14: Employment, enterprise and entrepreneurship)', carriedIn=['front matter', '1.14', '1.20', '1.40', '1.41', '1.42', '1.43', '1.44', '1.45', '1.46', '3.10', '4.6', 'section 5'], statements=['1.43', '1.20.b10', '4.6.b9']),
        dict(id='theme:generative-ai', named='Generative artificial intelligence', carriedIn=['front matter', '1.47', '1.48', '1.49', '1.50', '1.51', '3.5', '3.9'], statements=['1.48', '1.49', '1.50', '1.51'])],
    frameworks=[
        dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.3', '2.6']),
        dict(framework='scqf', levels=['fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.3', '2.6'])],
    bodies=[dict(body='Institute of Physics', citedIn=['2.16']),
            dict(body='Equality and Human Rights Commission', citedIn=['4.3']),
            dict(body='PSRBs (unnamed)', citedIn=['front matter', '4.3']),
            dict(body='Office for Students', citedIn=['front matter'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2'], role='common descriptions of the four honours classifications, for achievement above the threshold'),
        dict(document='std:doc:qaa-fheq-2024-framework', named='The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['2.3', '4.2', 'section 5'], role='defines the levels of qualifications'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development Guidance (Advance HE and QAA, 2021)', citedIn=['section 5'], role='reference for the ESD theme'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (QAA, 2018)', citedIn=['section 5'], role='reference for the enterprise theme'),
        dict(document='QAA Quality Code 2024 (not yet ingested)', named='the Quality Code (2024 update)', citedIn=['front matter', 'section 5'], role='companion reference point for using the statement'),
        dict(document="QAA Glossary (not ingested)", named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='UN Sustainable Development Goals (external)', named='United Nations Sustainable Development Goals (UN SDGs)', citedIn=['1.35', '1.36', '1.37', '1.39'], role='frame of the sustainability theme'),
        dict(document='Equality Act 2010 (law)', named='the Equality Act', citedIn=['1.22', '4.3'], role='EDI principles; competence standards'),
        dict(document='Disabled Student Commitment (not yet ingested)', named='the Disabled Student Commitment', citedIn=['1.30'], role='guidance on legislative principles for disabled students'),
        dict(document='General Data Protection Regulation (law)', named='the General Data Protection Regulation', citedIn=['1.51'], role='a risk in using generative AI')])

B1 = [
    dict(slug='inclusive-design', definition='a process that anticipates every student\'s needs in designing, delivering and assessing the curriculum and in all processes touching students from entry to graduation, so all can take full part (D1, 1.28)', beneficiaryDefinition='designing a course so that everyone can take part from the start, without needing to ask', scopeNote='set beside reasonable individual adjustments (1.27)', category='unknown', practices=['education']),
    dict(slug='accessibility', definition='enabling access for people with differing needs by removing needless barriers to learning and assessment (D1, 1.27)', scopeNote='the theme heading adds the needs of disabled students', category='unknown', practices=['education']),
    dict(slug='enterprise', definition='generating new ideas and turning them into practical action, drawing on creativity, innovation, adaptability, problem solving, communication and reflection (D1, 1.40)', scopeNote='paired with entrepreneurship and employability', category='unknown', practices=['education']),
    dict(slug='entrepreneurship', definition='acting on new ideas and opportunities to create cultural, social or economic value (D1, 1.40)', scopeNote='', category='unknown', practices=['education']),
    dict(slug='employability', definition='the mix of skills, knowledge and behaviours that makes a person likelier to gain work and succeed in a career (D1, 1.40)', scopeNote='', category='unknown', practices=['education']),
    dict(slug='threshold-standard', definition='the minimum standard a student will have shown on being awarded the honours degree (D1, 4.1, 4.2)', scopeNote="with the typical level above it (4.6); the integrated master's has its own threshold and typical levels (4.7, 4.8)", category='unknown', practices=['education']),
]
B2A = [
    dict(concept='inclusive-design', form='inclusive design', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='accessibility', form='accessibility', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='enterprise', form='enterprise', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='entrepreneurship', form='entrepreneurship', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='employability', form='employability', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='threshold-standard', form='minimum threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='threshold-standard', form='threshold level', lang='en', partOfSpeech='noun-phrase', termStatus='admitted', register='formal'),
]
B4 = [dict(rel='contrasts-with', **{'from': 'inclusive-design'}, to='reasonable individual adjustments', note='1.27: inclusive design wherever possible, adjustments where necessary')]
B5 = []
D3 = [
    dict(citation='Institute of Physics, degree accreditation framework (current edition)', settles=['SB5', 'S7'], asked='2026-10-03', state='wanted'),
    dict(citation='Disabled Students\' Commission, Disabled Student Commitment', settles=['S7', 'SB6'], asked='2026-10-03', state='wanted'),
    dict(citation='QAA (2024) The UK Quality Code for Higher Education', settles=['S7', 'SB6'], asked='2026-10-03', state='wanted'),
]

E = [
    "S4, rungs: no excellent rung. 4.1 sets out minimum threshold and typical standards only and 4.2 sends providers to Annex D for performance above threshold; SB4 records excellent with items 0.",
    "S4, rungs: the threshold is two lists, subject knowledge, understanding and skills (4.4, 9) and generic skills (4.5, 11), both under one heading; Psychology has one. Rung totals: threshold 23 (20 honours, 3 integrated master's), typical 17 (9 honours, 8 integrated master's).",
    "S4, force: the threshold lead-ins say 'students should be able to' (4.4, 4.5); recorded as force threshold, since 4.1 and 4.3 define these lists as the minimum for the award (forceFrom 4.1, 4.3). For Abbott: keep threshold or record the lead-in's should.",
    "S4, force: the typical lead-ins (4.6, 4.8) carry no modal ('has demonstrated'); force will taken from 4.1 ('will have demonstrated') for 4.6 and from 4.7 ('will also have') for 4.8.",
    "S4, integrated master's: a separate award, not a rung (BM-BRIEF convention). 4.7 and 4.8 recorded as threshold and typical with award integrated master's, level fheq:7, ids with suffix .masters (found by text); the brief's award value is master's: integrated master's kept as the issuer's award, for P3.",
    "S4, rung lead-ins: a new pattern for the typical and master's lists, which each build on the rung below explicitly ('has demonstrated the capabilities and skills of the threshold honours degree level and, in addition'); 4.7's master's threshold builds on the honours typical level, not the honours threshold.",
    "S3, skeleton: 4.5.b11's span ran into the 'Typical level' heading; cut back by find. 4.6.b10 ('- for example, with design thinking...') is a wrapped clause of 4.6.b9, not an item; merged into 4.6.b9 by find (typical honours list has 9 items, not 10).",
    "S3, skeleton: the script read 4.7 as the only threshold lead-in (it names 'threshold level') and missed 4.4 and 4.5, whose lead-ins say 'on graduating ... should be able to' under the heading 'Threshold level'.",
    "SB4, gradeOf: every link is inferred (the lists are not paired). Plain content matches: 4.6.b1 to 4.4.b2, 4.6.b2 to 4.4.b3, 4.6.b4 to 4.4.b7, 4.6.b5 to 4.4.b4, 4.6.b7 to 4.4.b8, 4.8.b4.masters to 4.7.b2.masters, 4.8.b5.masters to 4.7.b1.masters. Weaker: 4.6.b6 (modelling) to 4.4.b5 (software for simulation). 4.6.b3, b8 and b9 and 4.8.b1 to b3 and b6 to b8 have no counterpart below.",
    "SB4, domains: 4.4.b8 (communicating scientific information) and its typical and master's counterparts are recorded as subject-skill because the issuer lists it under subject skills; 4.4.b9 (articulating the value of the degree) is recorded as generic-skill though it sits in the same list. For P3.",
    "S4, D-std-0002 (a): 1.20 is an outcome list ('graduates will have developed'), taken as 10 statements; 1.20.b7 holds a second sentence with should ('A professional physicist should be objective...') inside the item, kept as one record with the lead-in's will.",
    "S4, provider norms not taken as statements (template open point 5): 1.19 ('All Physics degrees cover to some extent', 7 items), 3.2 teaching methods and 3.9 assessment methods ('may include', 'typically used'), 3.10 ('will typically employ'), 1.14 and 1.45 (predictive or hedged will), 1.9 (benefits of study, descriptive).",
    "S4, obliging words outside the five: 'need to' (1.48 'Students need to be prepared', 3.11 'Assessment regulations need to be flexible') recorded with force describes; 'it is expected that' (2.3) and 'it would be expected that' (2.4) not taken as statements; 'are responsible for' (1.26, inside a should paragraph). For Abbott: should 'need to' read as should?",
    "S4, mixed force: 1.24 carries should (curriculum, provider) and will (students build EDI awareness); recorded as should, addressee both, with the will outcome in the versions. 1.51 is addressed to students (should) as well as to trainers.",
    "S5, crosswalk: 2.6 places the CertHE at FQHEIS level 8 and the DipHE at FQHEIS level 9; the Frameworks (std:doc:qaa-fheq-2024-framework Table 1; std:doc:qaa-fqheis-2024-framework 4.11, 4.13) place them at SCQF 7 and 8. Recorded as stated, flagged here: an issuer error to confirm at P3.",
    "S5, levels: spine:6 and spine:7 (std:ref:uk-framework R2, R8) are inferred reading aids for the agent instructions, not cited by the statement.",
    "S2 and front matter: biophysical science (100949) is inferred for the text's 'biophysics' (2.5; 1.3); geophysics (2.5) has no HECoS term under physics and is not coded. Inferred codes are held back from lookups until P3.",
    "S7 and S0.2: the previous statement's date is not given; the text calls this the fourth edition, and the advisory groups listed are those of 2025, 2019 (minor update), 2008 and 2002 (recall to check: the previous edition is the 2019 minor update).",
    "SB6, themes: 4.5.b11 ('appreciation for diversity within the group') touches EDI without naming it; not tagged. 1.14 names 'the section on Employment, enterprise and entrepreneurship', a different heading from 1.40's.",
    "SB6: the front matter's five cross-cutting themes include generative artificial intelligence, recorded as theme:generative-ai (BM-BRIEF convention).",
    "SB5: the Institute of Physics' accreditation requirements and the EHRC guidance are not yet ingested (D3). The Office for Students appears only in the front matter.",
    "S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are to check (template open point 3).",
    "S9: not researched in P1.",
]
