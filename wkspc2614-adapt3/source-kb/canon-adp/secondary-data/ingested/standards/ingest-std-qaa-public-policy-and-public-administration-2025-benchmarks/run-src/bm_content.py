# bm_content.py: judgement for run 0128, QAA Subject Benchmark Statement Public Policy and Public Administration (April 2025). std run agent.
# Read by tools/bm_build.py. Keys of P are S4 ids under qaa/public-policy-and-public-administration-2025/. All text below except `find` spans is ours.
import json as _json, re as _re

_ST = '/home/claude/wkspc2601-library/ingested/standards'   # moved to the source library (std N-0119)
_SLUG = 'public-policy-and-public-administration-2025'
_NORM = open('/home/claude/wkspc2601-library/txt/qaa-2025-public-policy-public-administration-subject-benchmark-standard.norm.txt', encoding='utf-8').read()
_SK = _json.load(open(_ST + '/ingest-std-qaa-' + _SLUG.rsplit('-', 1)[0] + '-2025-benchmarks/run-src/bm-skel.json', encoding='utf-8'))
_CS = {c['number']: (c['start'], c['end']) for c in _SK['components']}
_STEM = {c['number']: (c['stemSpan']['start'], c['stemSpan']['end']) for c in _SK['components'] if c.get('stemSpan')}
_HEADS = ['Purposes and characteristics of a Public Policy and Public Administration degree', 'Equity, diversity and inclusion',
          'Accessibility and the needs of disabled students', 'Education for sustainable development',
          'Employability, entrepreneurship and enterprise education', 'Generative artificial intelligence',
          'Design', 'Progression', 'Flexibility', 'Partnership', 'Monitoring and review', 'Content', 'Teaching and learning',
          'Assessment and feedback', 'Threshold level', 'Excellent level', "Master's"]

def _tidy(t):
    t = t.rstrip()
    t = _re.sub(r'\s*\n\n\d+\s*$', '', t).rstrip()
    t = _re.sub(r'\s*\n\n\d+\n(' + '|'.join(_re.escape(h) for h in _HEADS) + r')$', '', t).rstrip()
    for h in _HEADS:
        if t.endswith(' ' + h) or t.endswith('\n' + h):
            t = t[:-len(h) - 1].rstrip()
            break
    return t

def _para(n):
    a, b = _CS[n]
    return _tidy(_NORM[a:b]), a

def _stem(n):
    a, b = _STEM[n]
    return _NORM[a:b].rstrip(), a

SID = 'qaa/' + _SLUG
HON = "bachelor's with honours"
MAS = "master's"
NA = ('n/a', 'a duty on the course and the people who design and run it, not a standard the student reaches')
CITE = '(QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para %s)'

P = {}
def s(i, find=None, after=None, **k):
    if find is None and i in _CS and '.b' not in i:
        find, after = _para(i)
    if find is not None:
        k['find'] = find; k['after'] = after if after is not None else 0
    P[i] = k

def prov(i, **k):
    d = dict(type='expectation', rung='none', force='will', level='none', appliesTo='Public Policy and Public Administration courses',
             addressee='provider', domain='none', award='none', ben=NA)
    d.update(k); s(i, **d)

def both(i, **k):
    d = dict(type='expectation', rung='none', force='will', level='none', appliesTo='Public Policy and Public Administration courses and their students',
             addressee='both', domain='none', award='none')
    d.update(k); s(i, **d)

def learner(i, **k):
    d = dict(type='expectation', rung='none', force='will', level='none', appliesTo='graduates of the subject',
             addressee='learner', domain='none', award='none')
    d.update(k); s(i, **d)

# =============================================================== section 1: context and purposes
learner('1.10', verbs=['prepare', 'acquire'], about='skills that prepare graduates for many occupations',
  para="The subject gives students skills, knowledge and capabilities for work in democratic or non-democratic settings marked by uncertainty; courses teach strategic problem-solving and how to hold governments to account, and the skills graduates gain will ready them for many occupations, not only careers in the field.",
  prac="Teach strategic problem-solving and accountability so that the skills and attributes graduates gain will fit them for a wide range of jobs, including those outside policy and administration.",
  ben="The skills and qualities you build will prepare you for many kinds of work, whether or not you go on to a career in public policy or administration.",
  aaw="Describe this as an expected outcome (will) of study in the subject: the skills gained prepare graduates for a wide range of occupations. It names no level or award; cite it as " + CITE % '1.10' + ". Do not claim it promises employment or that every graduate enters a policy career. Set it beside 1.23 and 2.14 and the FHEQ employment qualities qaa/fheq-2024/4.15.b9.1.",
  aad="Raise it when a student doubts that the degree leads anywhere but government service. Tell them in plain words that the skills travel widely, and ask: \"Which of your skills would an employer outside government value most?\" Avoid promising a job or reading the paragraph aloud.")
both('1.11', verbs=['encourage', 'evaluate', 'consider'], domain='understanding', about='critical evaluation of policy and public sector performance',
  para="With public sector jobs making up about a fifth of the UK economy and delivery spreading to non-profit and private bodies, investment in public staff matters; degrees will encourage students to evaluate policy critically and to weigh how effective and productive the public sector is.",
  prac="Design learning so that students will critically evaluate policy and judge the effectiveness and productivity of the public sector, given its size and its growing reliance on non-profit and private delivery.",
  ben="You will be encouraged to judge policies critically and to weigh how well and how productively the public sector works.",
  aaw="Describe this as a will-expectation on degrees in the subject: they encourage critical evaluation of policy and of public sector effectiveness and productivity. It holds for all awards in the subject without naming a level; cite it as " + CITE % '1.11' + ". Do not repeat the figure on public sector jobs as current fact without checking it. Set it beside the threshold items 4.5.b3 and 4.5.b5 and the FHEQ descriptor qaa/fheq-2024/4.15.b7.",
  aad="Raise it when a student or teacher discusses what critical study of policy should look like. For a student, ask: \"When you judge a policy, how do you decide whether it worked and was good value?\" Avoid quoting the paragraph's statistic as settled and avoid long readings from the text.")
prov('1.12', type='requirement', force='should', verbs=['recognise', 'guided', 'observe', 'integrate', 'promote'], about='EDI in delivery and curriculum',
  para="Because the subject serves fair policy and just institutions, its activities should be guided by EDI principles: degrees should observe, build in and advance EDI in teaching and curriculum, and equality, equity, diversity and inclusion should run through knowledge, pedagogy, curriculum, assessment and inclusive learning communities.",
  prac="Embed EDI in both what you teach and how you teach it: let it shape the curriculum, pedagogy and assessment, and build a subject community where every student and member of staff belongs.",
  aaw="Describe this as a should-duty on the course, not a student outcome: degrees in the subject observe, integrate and promote EDI in delivery and curriculum. It holds for every award in the subject and names no level; cite it as " + CITE % '1.12' + ". Do not present it as a legal requirement, and do not turn it into a learning outcome for students. Set it beside 1.14 and the shared theme record theme:edi.",
  aad="Raise it with a programme team reviewing curriculum, teaching or assessment for inclusion. Use the practitioner framing and ask: \"Where in the course would a student from an under-represented group see their perspective taught as central?\" Do not put this duty to a student as something they must achieve, and do not read the paragraph out at length.")
prov('1.14', type='requirement', force='should', verbs=['recognise', 'facilitate', 'promote', 'foster'], about='EDI in academic and administrative practice',
  para="EDI should lead academic, teaching and administrative practice in the subject, through inclusive language and through teaching and assessment that acknowledge unequal power, bring in diverse views, advance social justice and create inclusive places to learn.",
  prac="Put EDI first in day-to-day practice: use inclusive language, choose teaching and assessment that address unequal power and invite diverse views and keep learning spaces inclusive.",
  aaw="Describe this as a should-duty on staff practice and processes: EDI principles lead academic, pedagogical and administrative work in the subject. It names no level or award; cite it as " + CITE % '1.14' + ". Do not claim it prescribes particular methods, since it gives examples, not a checklist. Set it beside 1.12 and the assessment practice described in 3.11.",
  aad="Raise it when a teacher or team plans language, teaching activities or assessment. Ask: \"Which of your assessment formats could put a student at a disadvantage, and what would you change?\" Keep it to staff; do not hand it to a student as their duty.")
learner('1.17', verbs=['play', 'shaping'], about="graduates' role in accessible, inclusive services",
  para="Graduates will play a central part in shaping policy and services in fields from health and technology to innovation, finance and crises, going beyond legal compliance to provision that is accessible, inclusive, transparent and effective and lets everyone take part.",
  prac="Prepare students for the part graduates will play in shaping policy and services in areas like health, technology and crisis management, so that they design for full accessibility and participation, not only for legal compliance.",
  ben="You will play a central part in shaping policies and services, in areas such as health, technology and crisis management, and in making them open to everyone, beyond what the law demands.",
  aaw="Describe this as a will-expectation about graduates' future role: shaping policies and services that are fully accessible and inclusive, beyond legal compliance. It sets no level or award; cite it as " + CITE % '1.17' + ". Do not present it as an assessed outcome or a guarantee of career roles. Set it beside the accessibility norms in 1.16 (a plain-present paragraph, Part E) and theme:accessibility.",
  aad="Raise it when a student asks why accessibility matters in a policy course. Tell them plainly that they may design services others depend on, and ask: \"Who could be shut out by the service in your last case study, and how would you fix it?\" Avoid reducing accessibility to legal compliance.")
prov('1.22', type='requirement', force='must', verbs=['provide', 'equip', 'develop', 'progress'], about='links to enterprise and equipping experienced students',
  appliesTo='Public Policy and especially Public Administration degrees, pre- and post-experience',
  para="Because the subject is closely tied to practice, its degrees for students before and after work experience must link content clearly to enterprise and entrepreneurship, and must give students already in the sector the knowledge, behaviours and skills to grow and advance at work.",
  prac="Make the link between content and enterprise explicit, and design for experienced practitioners as well as new entrants: they must leave with what they need to progress in their workplace.",
  aaw="Describe this as a must-duty on degrees in the subject, especially Public Administration: clear links to enterprise and entrepreneurship, and provision that equips sector-experienced students to progress at work. It holds for undergraduate and postgraduate degrees alike; cite it as " + CITE % '1.22, the first of two paragraphs so numbered' + ". Do not claim it obliges a placement or a particular module. Set it beside 1.23, 3.10 and the FHEQ employment qualities qaa/fheq-2024/4.17.b8.1.",
  aad="Raise it with a programme team designing for mixed cohorts of new and experienced students. Ask: \"Where does the course show an experienced public servant how to use what they learn to move on at work?\" Do not present this to a student as their duty.")
learner('1.23', type='outcome', verbs=['understand', 'recognise', 'reflect', 'develop', 'communicate'], domain='generic-skill', level='fheq:6', award=HON,
  about='recognising and communicating enterprise and employability skills',
  para="Graduates understand the worth of the enterprise and employability skills they built during study; courses can deepen that understanding, and students will be able to recognise these skills, reflect on them, develop them and explain them to employers and other stakeholders.",
  prac="Give students repeated chances to name, reflect on and build their enterprise and employability skills, so that graduates will be able to explain them to current and future employers.",
  ben="You will be able to recognise the enterprise and employability skills you have built, reflect on them, keep developing them and explain them clearly to employers.",
  aaw="Describe this as an outcome graduates will be able to show (are able to): recognising, reflecting on, developing and communicating their enterprise and employability skills. Read it at honours, FHEQ level 6 (FQHEIS level 10, spine:6), though the paragraph speaks of graduates generally; cite it as " + CITE % '1.23' + ". Do not claim it is a rung standard, since it sits in the context section. Set it beside the threshold items 4.5.b8 and 4.5.b9, the FHEQ descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D cell qaa/fheq-2024/annex-d/transferable/r4/3rd.",
  aad="Raise it when a student prepares an application, interview or placement, or a team plans employability work. Ask a student: \"Name a skill you built on the course and tell me how you would show an employer you have it.\" Avoid treating it as a graded standard and avoid long quotation.")
prov('1.26', type='requirement', force='must', verbs=['recognise', 'respond'], about='responding to generative AI in teaching and assessment',
  para="As AI reshapes the labour market and work alongside smart machines, degrees in the subject must recognise and respond to the needs of employers and workplaces and to changing teaching, assessment and feedback, so that students study responsibly and with integrity; course developers look past assessment security to bring GenAI into wider learning and authentic assessment.",
  prac="Treat generative AI as a curriculum matter, not only an integrity risk: align with what employers and workplaces need, adapt teaching, assessment and feedback and consider building GenAI into activities and authentic assessment.",
  aaw="Describe this as a must-duty on degrees in the subject: they answer to what employers and workplaces need and to changing teaching, assessment and feedback in the face of generative AI. It names no level or award; cite it as " + CITE % '1.26' + ". Do not claim it bans or mandates any tool, or that it is a student outcome. Set it beside 1.27, 1.28, the assessment practice at 3.12 and theme:generative-ai.",
  aad="Raise it with a team reviewing assessment design or its AI policy. Ask: \"Which of your assessments would still show a student's own judgement if they used GenAI openly?\" Do not turn this course duty into a rule for students.")

# =============================================================== section 2: distinctive features
both('2.4', verbs=['examine', 'emphasise'], about='public and social value in courses',
  para="Courses also study multilevel governance and how structure, systems and agency interact in the public sector, such as the state's part in policy and the experience of frontline staff; they will also stress public and social value as typical of the field, with public service motivation and ethos as common themes.",
  prac="Cover multilevel governance and the interplay of structure, systems and agency, and make public and social value a visible thread, alongside public service motivation and ethos.",
  ben="Your course will give weight to public and social value, and you will look at how governance works across levels and how frontline staff experience the public sector.",
  aaw="Describe this as a will-expectation on courses: they emphasise public and social value, alongside multilevel governance and the interplay of structure, systems and agency. It names no level or award; cite it as " + CITE % '2.4' + ". Do not present the topics named as a required syllabus. Set it beside the content paragraph 3.3 and the master's item 4.7.b11.",
  aad="Raise it when a student or teacher asks what sets the subject apart from management or politics. Ask: \"How would you show the public value of a service, beyond its cost?\" Avoid listing the topics as a checklist.")
both('2.7', verbs=['progress', 'build', 'include'], level='fheq:6', award=HON, about='progression through the honours levels towards the threshold',
  para="Over an honours degree (FHEQ level 6; FQHEIS level 10) students will progress level by level under each institution's rules, each level adding knowledge, expertise and experience towards the threshold subject and generic skills; this will usually mean completing all learning and assessment for credit, practical parts included, and a graduate with a second-class degree or better would be expected to be ready for postgraduate study, though providers set entry rules.",
  prac="Plan each level so that it builds knowledge, expertise and experience towards the threshold subject-specific and generic skills by graduation, with credit earned across all learning and assessment, practical work included.",
  ben="As you move through each year of your honours degree, you will build the knowledge, expertise and experience that lead to the minimum standard by the end, completing all your learning and assessment, practical work included. With a second-class result or higher you would usually be ready for postgraduate study, though each university sets its own entry rules.",
  aaw="Describe this as a will-expectation about progression through an honours degree at FHEQ level 6 (FQHEIS level 10): each level builds towards the threshold standards, normally through credit for all learning and assessment. Cite it as " + CITE % '2.7' + ". Do not claim it sets entry rules for postgraduate study, which it leaves to each provider. Set it beside the threshold list 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the progression threads in std:doc:qaa-fheq-2024-framework, SL4.",
  aad="Raise it when a student asks how earlier years count or whether a 2:2 opens postgraduate study. Explain in plain words that each year builds towards the final standard, and ask: \"What did you learn last year that you now use without thinking?\" Avoid promising postgraduate entry, which each university decides.")
learner('2.8', type='outcome', verbs=['achieve', 'add'], level='fheq:6', award=HON, appliesTo='joint or combined honours students', about='joint and combined degrees',
  para="Undergraduates taking the subject in a joint or combined degree will reach the core of its specific and generic skills and add others from their other subject, and may explore where disciplines overlap.",
  prac="In joint or combined honours, make sure students will still attain the core subject-specific and generic skills of this statement, while the partner subject adds its own.",
  ben="If you study this subject as part of a joint or combined degree, you will gain its core subject and general skills and add others from your second subject.",
  aaw="Describe this as a will-outcome for joint or combined honours students at FHEQ level 6 (FQHEIS level 10): they achieve the core of the subject's specific and generic skills. Cite it as " + CITE % '2.8' + ". Do not claim joint students must meet every item in 4.5, since the paragraph speaks of core elements. Set it beside the threshold list 4.5 and the FHEQ descriptor qaa/fheq-2024/4.15.b1.",
  aad="Raise it when a joint honours student or course team asks how much of the subject must be covered. Ask: \"Which core skills of policy and administration does your half of the degree secure?\" Avoid suggesting that joint students are held to less than the core.")
learner('2.14', verbs=['have', 'become', 'acquired', 'helped', 'understand'], domain='understanding', about='skills for policy, management and leadership across sectors',
  para="Graduates are expected to be equipped to work well as policymakers, managers, leaders and agents of change across public, private and non-profit sectors; public service and public administration are distinct professions whose members can move between policy and administration, and students will be helped to see that services are delivered through multi-agency models where cross-sector working is normal.",
  prac="Build skills for policymaking, management, leadership and change across sectors, and teach that services are delivered by multi-agency partnerships, so that graduates will have what they need to move between policy and administration roles.",
  ben="You will gain the skills to work as a policymaker, manager, leader or change agent in public, private or non-profit organisations, and you will learn how services are delivered by many agencies working together.",
  aaw="Describe this as a will-expectation on graduates: the skills to work as policymakers, managers, leaders and change agents across sectors, with an understanding of multi-agency delivery. It names no level or award; cite it as " + CITE % '2.14' + ". Do not present it as a guarantee of a role or of seniority. Set it beside the master's items 4.7.b15 and 4.7.b16, the threshold item 4.5.b7 and the FHEQ employment qualities qaa/fheq-2024/4.15.b9.2.",
  aad="Raise it when a student is weighing careers in the public, private or non-profit sector. Ask: \"Which agencies would need to work together to deliver the service you know best?\" Avoid implying that the degree alone makes someone a leader.")
prov('2.19', verbs=['form'], appliesTo='degree-awarding bodies and their collaborative partners', about='the student voice in monitoring and review',
  ben=('n/a', 'a duty on the awarding body; students take part in review but do not reach it as a standard'),
  para="Degree-awarding bodies and their partners routinely gather and analyse information and review degrees periodically, and the student voice will form part of this; they use external reference points, this statement among them, and evaluation can include regular review of EDI in the learning community.",
  prac="Include students' views in routine monitoring and periodic review, use external reference points and consider reviewing EDI within the learning community as part of evaluation.",
  aaw="Describe this as a will-expectation on degree-awarding bodies: periodic review of the degree takes the student voice into account. It names no level or award; cite it as " + CITE % '2.19' + ". Do not claim it fixes a review cycle or method. Set it beside 2.20 and theme:edi.",
  aad="Raise it with a programme team planning a periodic review. Ask: \"How will students' views reach the review panel, and what will change as a result?\" Do not present it to a student as an obligation.")
prov('2.20', verbs=['use', 'gain', 'ensure'], appliesTo='higher education providers', about='external reviewers in periodic review',
  para="Externality is a core part of UK quality assurance: providers will use external reviewers in periodic review to bring an outside view of proposed changes, check that threshold standards are met and confirm that content suits the subject.",
  prac="Bring external reviewers into periodic review to test proposed changes, confirm that threshold standards are achieved and check that the content fits the subject.",
  aaw="Describe this as a will-expectation on higher education providers: external reviewers take part in periodic review to secure threshold standards and suitable content. It holds for all awards in the subject; cite it as " + CITE % '2.20' + ". Do not claim it describes the external examiner system, which 2.21 covers. Set it beside 2.19 and the threshold list 4.5.",
  aad="Raise it when a team prepares for periodic review or chooses external reviewers. Ask: \"Who outside the institution will test whether your threshold standards hold?\" Keep it to staff and avoid long readings.")
prov('2.23', verbs=['integrate'], appliesTo='courses with professional or vocational outcomes evaluated by accrediting bodies', about='integrating accreditation requirements',
  para="Courses whose professional or vocational outcomes are evaluated by professional and accrediting bodies will need to build those requirements into how the degree is managed.",
  prac="Where professional or accrediting bodies evaluate the course, build their requirements into degree management from the start.",
  aaw="Describe this as an obligation (will need to) on courses whose professional or vocational outcomes accrediting bodies evaluate: integrate those requirements into degree management. It names no level or award; cite it as " + CITE % '2.23' + ". Do not fold any body's requirements into the statement itself, since they are separate documents. Set it beside 1.25 and the bodies in SB5.",
  aad="Raise it with a team seeking or holding accreditation. Ask: \"Where in your course management do the accrediting body's requirements get checked?\" Do not put this duty to a student.")

# =============================================================== section 3: content, structure and delivery
both('3.2', verbs=['learn', 'work', 'develop'], about='practice-based learning',
  para="Students will usually learn how policy making, public administration and decision making have developed through practice-based learning, working on real problems and building critical skills through approaches such as action learning and reflection and through placements in public and non-governmental bodies.",
  prac="Use practice-based learning: real-world problems and action learning with reflection, plus focused placements in public and non-governmental organisations.",
  ben="You will usually learn through practice: working on real problems, reflecting on what you do and perhaps taking a placement in a public agency or a non-governmental organisation.",
  aaw="Describe this as a will-expectation, qualified by typically, about how students learn in the subject: through practice-based learning, action learning, reflection and placements. It names no level or award; cite it as " + CITE % '3.2' + ". Do not claim it requires every student to take a placement. Set it beside the learning methods at 3.7 and the threshold items 4.5.b5 and 4.5.b9.",
  aad="Raise it when a student asks how the course is taught or a team plans practice-based learning. Ask a student: \"Which real problem have you worked on so far, and what did reflecting on it teach you?\" Avoid presenting placements as guaranteed.")
_f33, _a33 = _stem('3.3')
both('3.3', find=_f33, after=_a33, verbs=['introduce', 'include', 'develop', 'apply', 'study', 'demonstrate'], about='engagement with governance and policy across contexts',
  para="Degrees introduce the design and running of governments and of the public and voluntary sectors; no sector or institution is essential, but study will include close engagement with questions of governance and policy, applying theories, concepts, values and principles across many contexts; all students study the public sector conceptually and empirically at every tier of government, and typically know a number of the listed subfields.",
  prac="Choose any sectors or institutions, but make sure students engage closely with governance and policy questions, apply theory across contexts from the individual to the global and study the public sector both conceptually and empirically, drawing on several of the listed subfields.",
  ben="You will study how governments and the public and voluntary sectors are designed and run, apply theories and principles to real questions of governance and policy in many settings and get to know several specialist areas of the field.",
  aaw="Describe this as a will-expectation on the content of study: detailed engagement with governance and policy questions, applied across contexts, with the public sector studied conceptually and empirically. It names no level or award; cite it as " + CITE % '3.3' + ", and present the 40 subfields as a menu from which courses draw, not a core list. Do not claim any sector or institution is required. Set it beside the knowledge items 4.5.b1 and 4.6.b1 and the FHEQ descriptor qaa/fheq-2024/4.15.b1.",
  aad="Raise it when a team designs or reviews the curriculum, or a student chooses options. Ask: \"Which subfields does your course cover, and how do they let you compare tiers of government?\" Avoid reading out the full list of subfields.")
prov('3.6', verbs=['ensure', 'reflect'], about='learning environments and digital inclusivity',
  para="Each provider's learning and teaching will reflect its own approach to the subject; methods fit the subject matter, the outcomes and learners' needs, embrace sustainability, inclusion, diversity, accessibility and enterprise, recognise students' prior learning cultures and the global context, and run across many modes; and providers will make digital learning inclusive wherever they can.",
  prac="Fit teaching methods to the content, outcomes and learners, build in sustainability, inclusion, accessibility and enterprise, use a mix of modes and do what you can to make digital learning inclusive for every student.",
  aaw="Describe this as a will-expectation on providers: learning and teaching reflect each provider's approach and, as far as possible, secure digital inclusivity. It names no level or award; cite it as " + CITE % '3.6' + ". Do not claim it prescribes any mode of delivery. Set it beside 3.7, 1.14 and the themes theme:accessibility and theme:esd.",
  aad="Raise it with a teacher or team planning blended, online or hybrid delivery. Ask: \"Which students might struggle to reach your digital materials, and what support do they get?\" Keep it as a staff duty.")
_f37, _a37 = _stem('3.7')
both('3.7', find=_f37, after=_a37, verbs=['experience', 'combine', 'develop', 'advance', 'identify'], about='a range of learning environments and methods',
  para="Students will meet a mix of learning settings, methods and activities that together build cognitive and life skills and knowledge and help them find enterprising answers to social challenges; whatever the mode, learning typically combines several of the listed methods.",
  prac="Offer a varied mix of settings and methods that build cognitive and life skills and enterprising responses to social challenges, drawing on lectures, seminars, case studies, simulations, placements, independent study, practitioner talks and fieldwork.",
  ben="You will learn in many ways, such as lectures, seminars, case studies, simulations, placements, guest talks and field trips, which together build your thinking, your life skills and your ideas for tackling social problems.",
  aaw="Describe this as a will-expectation that students experience varied learning environments and methods, typically a combination drawn from the listed methods. It names no level or award; cite it as " + CITE % '3.7' + ". Do not present the list as compulsory. Set it beside 3.2, 3.6 and theme:enterprise.",
  aad="Raise it when a student asks how they will be taught or a team reviews its mix of methods. Ask: \"Which way of learning has helped you most so far, and which have you not yet tried?\" Avoid reading the method list aloud.")
prov('3.10', verbs=['reflect', 'align', 'promoted', 'linked', 'enables'], about='an assessment strategy aligned with curriculum and outcomes',
  para="Assessment and feedback help students engage deeply and show their understanding, analysis, insight and skills; a course's assessment strategy will mirror the knowledge, skills and understanding in its curriculum and fit its teaching methods, with assessment for and as learning, tied to learning outcomes, showing rising attainment and building employability and professional skills.",
  prac="Align the assessment strategy with the curriculum and teaching, link each task to stated outcomes, use assessment for and as learning and let it show progression and build employability and professional skills.",
  ben=('n/a', "a duty on the course's assessment design; the student meets its effect"),
  aaw="Describe this as a will-expectation on each course's assessment strategy: it reflects the curriculum and aligns with teaching, linked to learning outcomes and progressive attainment. It names no level or award; cite it as " + CITE % '3.10' + ". Do not claim it prescribes assessment types, since 3.12 gives examples only. Set it beside 3.11, 3.12, 3.13 and theme:enterprise.",
  aad="Raise it with a team mapping assessment to outcomes. Ask: \"Which outcome does each assessment test, and where does a student show progress from one level to the next?\" Keep it to staff; do not present it as a student's task.")
both('3.13', verbs=['designed', 'given', 'feed'], about='constructive feedback throughout study',
  para="Feedback is central to learning and helps students see their progress and improve; it will be constructive, consistent and specific, and will come throughout study on formative and summative work so that students can carry it forward; varied methods, from written and spoken comments to technology and peer and self-assessment, support equality and inclusion.",
  prac="Give constructive, consistent and specific feedback on formative and summative work across the course, timed so that students can use it on later tasks and vary its form for a diverse cohort.",
  ben="You will get feedback that is constructive, consistent and specific on both practice and marked work throughout your studies, so that you can use it on your next tasks.",
  aaw="Describe this as a will-expectation on the course: feedback is constructive, consistent and specific, given throughout study on formative and summative work so that students can feed it forward. It names no level or award; cite it as " + CITE % '3.13' + ". Do not claim it fixes turnaround times or formats. Set it beside the items on using feedback, 4.5.b14 and 4.6.b15, and theme:edi.",
  aad="Raise it when a student is unsure what to do with feedback or a team reviews its feedback practice. Ask a student: \"What did your last piece of feedback tell you to do differently next time?\" Avoid suggesting that feedback must take one form.")

# =============================================================== section 4: introduction
prov('4.2', type='requirement', force='should', verbs=['refer', 'perform'], level='fheq:6', award=HON, appliesTo='each higher education provider',
  about='using Annex D for classification',
  para="Most students will perform well above the minimum threshold; each provider decides what evidence shows this and should use Annex D of the 2024 Frameworks, the classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees, which describe the four honours classes and postgraduate outcomes.",
  prac="Decide how your institution evidences performance above threshold, and use Annex D of the 2024 Frameworks, the classification descriptions for honours at FHEQ level 6 and FQHEIS level 10, when setting class boundaries.",
  aaw="Describe this as a should-duty on each provider: when judging achievement above the threshold, refer to the degree classification descriptions in Annex D. It holds for honours at FHEQ level 6 (FQHEIS level 10); cite it as " + CITE % '4.2' + " and point to std:doc:qaa-fheq-2024-framework, Annex D (qaa/fheq-2024/annex-d/...). Do not claim the subject sets its own class descriptors, since it states only threshold and excellent levels. Set it beside 4.5, 4.6 and the classification bands in std:doc:qaa-fheq-2024-framework, SL6.",
  aad="Raise it with a team or external examiner calibrating marks across classes. Ask: \"How do your marking criteria for a 2:1 relate to the Annex D description?\" Do not present classification rules to a student as this subject's own.")
prov('4.3', type='requirement', force='should', verbs=['follow', 'informed'], appliesTo='providers writing competence standards', about='competence standards and EHRC guidance',
  para="The minimum threshold standards are not universal competence standards; a provider that writes competence standards under the Equality Act 2010 into a programme specification may draw on this statement and any PSRB requirements, and should follow the Equality and Human Rights Commission's latest guidance.",
  prac="If you write competence standards (Equality Act 2010) into a programme specification, you may draw on this statement and PSRB requirements, but follow the latest EHRC guidance and do not treat the threshold standards as competence standards.",
  aaw="Describe this as a should-duty on providers that write competence standards: follow the latest guidance of the Equality and Human Rights Commission. It names no level; cite it as " + CITE % '4.3' + ". Do not call the threshold items in 4.5 competence standards. Set it beside 4.5 and theme:edi.",
  aad="Raise it with a team drafting a programme specification that includes competence standards. Ask: \"Which of your requirements are competence standards in the legal sense, and have you checked them against the EHRC guidance?\" Keep it to staff.")

# =============================================================== section 4: the rungs
# (key, verbs, about, domain, para, prac, ben tail, FHEQ descriptor, Annex D cell, question)
T = [
 ('b1', [], 'key concepts, theories and current evidence', 'knowledge',
  "Shows knowledge of the subject's main concepts and theories and an awareness of the evidence now available.",
  "show that they know the field's core concepts and theories and are aware of current evidence.",
  "show that you know the main concepts and theories of public policy and administration and are aware of current evidence.",
  'qaa/fheq-2024/4.15.b1', 'knowledge/r2', "Which two theories of the policy process could you explain and use on a current case?"),
 ('b2', ['informed'], 'current problems and new insights near the forefront', 'understanding',
  "Shows knowledge, understanding and awareness of present problems or fresh insights, much of it drawn from or shaped by leading work in the discipline or in professional practice.",
  "show knowledge and understanding of present problems or new insights, much of it shaped by leading research or professional practice.",
  "know and understand today's problems and new thinking in the field, much of it drawn from leading research or practice.",
  'qaa/fheq-2024/4.15.b1', 'knowledge/r1', "What is one live problem in public services that recent research has changed your view of?"),
 ('b3', ['construct', 'synthesising', 'exercising'], 'building an argument with judgement', 'generic-skill',
  "Can build an argument, bringing relevant information together and using judgement.",
  "can build an argument that draws relevant information together and uses judgement.",
  "build an argument that brings together the relevant information and shows your own judgement.",
  'qaa/fheq-2024/4.15.b3.1', 'cognitive/r2', "What is the strongest objection to your argument, and how does your evidence answer it?"),
 ('b4', ['deal', 'making'], 'complex issues and judgement with incomplete data', 'generic-skill',
  "Can handle complex issues in an orderly and inventive way and reach sound judgements when data are incomplete.",
  "can handle complex issues methodically and inventively and judge soundly when information is missing.",
  "handle complex issues methodically and inventively, and reach sound judgements when some of the information is missing.",
  'qaa/fheq-2024/4.15.b7', 'cognitive/r3', "When you had to decide without all the facts, how did you make the gap visible in your reasoning?"),
 ('b5', ['identify', 'investigate', 'solve'], 'problems in practical and theoretical contexts', 'subject-skill',
  "Can find, look into and resolve problems in both practical and theoretical settings.",
  "can find, examine and resolve problems in practical and theoretical settings.",
  "spot, look into and resolve problems, in practice as well as in theory.",
  'qaa/fheq-2024/4.15.b6', 'cognitive/r3', "Can you take a problem from a placement or case and show how theory helped you solve it?"),
 ('b6', ['evaluate', 'apply', 'collecting', 'analysing', 'presenting'], 'approaches to collecting, analysing and presenting data', 'subject-skill',
  "Can judge and use suitable ways of gathering, analysing and presenting relevant data.",
  "can assess and use methods for gathering, analysing and presenting relevant data.",
  "choose and use good ways to gather, analyse and present the data a question needs.",
  'qaa/fheq-2024/4.15.b2', 'practical/r4', "Why did you choose that method of collecting data, and what would another method have shown?"),
 ('b7', ['achieve'], 'collaboration towards shared goals', 'generic-skill',
  "Works with others towards shared aims, for instance in group tasks, projects and presentations.",
  "work with others towards shared aims, for example in group tasks, projects and presentations.",
  "work with others towards shared aims, for example in group work, projects and presentations.",
  'qaa/fheq-2024/4.15.b9.1', 'transferable/r2', "What did you contribute to your last group task, and what would you do differently?"),
 ('b8', [], 'communication in varied formats and for varied audiences', 'generic-skill',
  "Communicates in formats suited to the context and to different audiences.",
  "communicate in formats that suit the context and different audiences.",
  "communicate in forms that suit the setting and the people you are addressing.",
  'qaa/fheq-2024/4.15.b8', 'transferable/r1', "How would you explain the same policy finding to a minister and to a service user?"),
 ('b9', [], 'reflection on own learning', 'generic-skill',
  "Reflects on their own learning.",
  "reflect on their own learning.",
  "think about how you are learning and what that tells you.",
  'qaa/fheq-2024/4.15.b5', 'transferable/r5', "What have you learned about how you learn best?"),
 ('b10', ['working'], 'managing own learning and projects', 'generic-skill',
  "Manages their own learning and projects well, working alone and with others.",
  "manage their own learning and projects well, alone and with others.",
  "manage your own learning and projects well, on your own and with others.",
  'qaa/fheq-2024/4.15.b5 and 4.15.b6', 'transferable/r3', "How do you plan a project so that it is finished on time?"),
 ('b11', ['understand', 'apply'], 'principles of ethical research', 'subject-skill',
  "Can understand and use the principles of ethical research.",
  "can understand and apply the principles of research ethics.",
  "understand the principles of ethical research and put them into practice.",
  'qaa/fheq-2024/4.15.b2', 'professional/r2', "What ethical risks did your last piece of research raise, and how did you handle them?"),
 ('b12', [], 'organising and using evidence from primary and secondary sources', 'subject-skill',
  "Organises and uses evidence, data and information from a range of primary and secondary sources.",
  "organise and use evidence, data and information drawn from varied primary and secondary sources.",
  "organise and use evidence, data and information from many kinds of original and secondary sources.",
  'qaa/fheq-2024/4.15.b5', 'cognitive/r1', "Which primary source did you use most recently, and how did it change your argument?"),
 ('b13', ['understand'], 'personal integrity and the ethics of decisions', 'understanding',
  "Can see why personal integrity matters and is aware of the ethical effects decisions may have.",
  "can see why personal integrity matters and recognise the ethical effects that decisions may have.",
  "understand why personal integrity matters and be aware of the ethical consequences decisions can have.",
  'qaa/fheq-2024/4.15.b9.2', 'professional/r2', "Think of a public decision you studied: who bore its ethical costs, and was that fair?"),
 ('b14', [], 'using constructive feedback', 'generic-skill',
  "Understands and uses constructive feedback.",
  "understand and act on constructive feedback.",
  "understand constructive feedback and act on it.",
  'qaa/fheq-2024/4.15.b5', 'transferable/r3', "Which piece of feedback have you acted on, and what changed as a result?"),
 ('b15', ['select', 'use'], 'communication, information and data tools and software', 'generic-skill',
  "Can choose and use suitable aids and software for communication, information and data analysis.",
  "can choose and use suitable aids and software for communicating, handling information and analysing data.",
  "choose and use the right tools and software for communicating, handling information and analysing data.",
  'qaa/fheq-2024/4.15.b8', 'transferable/r1', "Which software do you use for data analysis, and what can you not yet do with it?"),
]
X = [
 ('b1', 'b1', [], 'consistent, detailed knowledge of concepts, theories, evidence and issues', 'knowledge',
  "Shows consistent and detailed knowledge of the main concepts and theories and awareness of current evidence and issues.",
  "show consistent, detailed knowledge of the core concepts and theories and awareness of current evidence and debates.",
  "show detailed, consistent knowledge of the main concepts and theories and a good grasp of current evidence and debates.",
  'qaa/fheq-2024/4.15.b1', 'knowledge/r2', "Where could you go beyond the textbook account of a theory and show where it breaks down?"),
 ('b2', 'b2', ['informed'], 'systematic, critical awareness of current problems and insights', 'understanding',
  "Shows systematic knowledge and understanding, and a critical awareness, of present problems or new insights, much of it from leading work in the discipline or practice.",
  "show systematic knowledge and a critical awareness of current problems or new insights, much of it from leading research or practice.",
  "show a systematic and critical grasp of today's problems and new thinking in the field, much of it from leading research or practice.",
  'qaa/fheq-2024/4.15.b1', 'knowledge/r1', "Which recent study would you challenge, and on what grounds?"),
 ('b3', 'b7', ['collaborate', 'achieve'], 'sophisticated collaboration towards shared goals', 'generic-skill',
  "Collaborates with others in a sophisticated way to reach shared aims, for instance in group work, projects and presentations.",
  "collaborate skilfully with others towards shared aims, for instance in group work, projects and presentations.",
  "work with others skilfully to reach shared aims, for example in group projects and presentations.",
  'qaa/fheq-2024/4.15.b9.1', 'transferable/r2', "How did you help a group reach a goal it might have missed without you?"),
 ('b4', 'b8', ['communicate'], 'developed communication in varied formats and for varied audiences', 'generic-skill',
  "Communicates with developed skill in formats suited to the context and to varied audiences.",
  "communicate with developed skill in formats suited to the context and the audience.",
  "communicate with real skill in forms that fit the setting and the people you are addressing.",
  'qaa/fheq-2024/4.15.b8', 'transferable/r1', "How did you adapt your last piece of work for an audience outside the university?"),
 ('b5', 'b3', ['construct', 'synthesising', 'exercising'], 'strong reasoned argument with critical judgement', 'generic-skill',
  "Shows a strong capacity to build reasoned arguments, drawing relevant information together and judging critically.",
  "show a strong capacity to build reasoned arguments that draw information together and judge it critically.",
  "build strong, well-reasoned arguments that pull the relevant information together and weigh it critically.",
  'qaa/fheq-2024/4.15.b3.1', 'cognitive/r2', "Where in your argument did you weigh competing evidence, and why did one side win?"),
 ('b6', 'b9', ['reflect'], 'critical reflection on own learning', 'generic-skill',
  "Shows a developed capacity to reflect critically on their own learning.",
  "show a developed capacity to reflect critically on how they learn.",
  "reflect critically and in depth on your own learning.",
  'qaa/fheq-2024/4.15.b5', 'transferable/r5', "What have you changed in how you study because of your own reflection?"),
 ('b7', 'b4', ['making'], 'effective handling of complex issues with incomplete data', 'generic-skill',
  "Handles complex issues effectively, in an orderly and inventive way, reaching sound judgements when data are incomplete.",
  "handle complex issues effectively, methodically and inventively, judging soundly when information is incomplete.",
  "handle complex issues effectively, methodically and creatively, and make sound judgements when information is missing.",
  'qaa/fheq-2024/4.15.b7', 'cognitive/r3', "How did you test the judgement you reached on a complex case with gaps in the data?"),
 ('b8', 'b5', ['identifying', 'investigating', 'solving', 'thinking'], 'confident, creative problem-solving', 'subject-skill',
  "Finds, looks into and resolves problems with confidence, thinking creatively in practical and theoretical settings.",
  "find, examine and resolve problems with confidence, thinking creatively in practice and theory.",
  "find, look into and solve problems with confidence, thinking creatively in practice and in theory.",
  'qaa/fheq-2024/4.15.b6', 'cognitive/r3', "What creative option did you find that others had not considered?"),
 ('b9', 'b6', ['evaluate', 'apply', 'collecting', 'analysing', 'presenting'], 'excellent judgement of data approaches', 'subject-skill',
  "Shows an excellent capacity to judge and use suitable ways of gathering, analysing and presenting data.",
  "show an excellent capacity to assess and use methods for gathering, analysing and presenting data.",
  "judge and use methods for gathering, analysing and presenting data to an excellent standard.",
  'qaa/fheq-2024/4.15.b2', 'practical/r4', "Could you defend your choice of data method to a sceptical expert?"),
 ('b10', 'b10', ['working'], 'timely, critical management of own learning and projects', 'generic-skill',
  "Manages their own learning and projects effectively, on time and critically, alone and with others.",
  "manage their learning and projects effectively, on time and critically, alone and with others.",
  "manage your learning and projects well, on time and with a critical eye, on your own and with others.",
  'qaa/fheq-2024/4.15.b5 and 4.15.b6', 'transferable/r3', "How do you check that a project is still asking the right question as it goes?"),
 ('b11', 'b11', ['understanding', 'applying'], 'clear grasp and use of research ethics', 'subject-skill',
  "Understands and uses the principles of ethical research with clarity.",
  "understand and apply research ethics with clarity.",
  "understand research ethics clearly and apply them with care.",
  'qaa/fheq-2024/4.15.b2', 'professional/r2', "Which ethical judgement in your research was hardest, and how did you resolve it?"),
 ('b12', 'b12', [], 'effective organisation and use of evidence from varied sources', 'subject-skill',
  "Organises and uses evidence, data and information from a range of primary and secondary sources effectively.",
  "organise and use evidence, data and information from varied primary and secondary sources effectively.",
  "organise and use evidence, data and information from many original and secondary sources effectively.",
  'qaa/fheq-2024/4.15.b5', 'cognitive/r1', "How did you bring together sources that disagreed?"),
 ('b13', 'b13', [], 'evident grasp of integrity and the ethics of decisions', 'understanding',
  "Shows a clear understanding of why personal integrity matters and an awareness of the ethical effects decisions may have.",
  "show a clear grasp of why personal integrity matters and of the ethical effects decisions may have.",
  "show a clear grasp of why personal integrity matters and of the ethical consequences of decisions.",
  'qaa/fheq-2024/4.15.b9.2', 'professional/r2', "How would you advise a decision-maker facing a conflict between efficiency and fairness?"),
 ('b14', None, [], 'academic practice and professional behaviour', 'subject-skill',
  "Evaluates analytically, where relevant, how academic practice relates to professional conduct.",
  "evaluate analytically, where relevant, how academic practice relates to professional conduct.",
  "weigh up analytically, where it applies, how academic work relates to how professionals behave.",
  'qaa/fheq-2024/4.15.b9.1', 'professional/r1', "Where do the standards of good academic work and good professional conduct pull in different directions?"),
 ('b15', 'b14', [], 'developed use of constructive feedback', 'generic-skill',
  "Shows a developed understanding and use of constructive feedback.",
  "show a developed understanding and use of constructive feedback.",
  "understand constructive feedback well and use it to improve your work.",
  'qaa/fheq-2024/4.15.b5', 'transferable/r3', "Which feedback have you sought out yourself, and what did you do with it?"),
 ('b16', 'b15', ['select', 'use'], 'strong choice and use of tools and software', 'generic-skill',
  "Shows a strong capacity to choose and use suitable aids and software for communication, information and data analysis.",
  "show a strong capacity to choose and use aids and software for communication, information handling and data analysis.",
  "choose and use the right tools and software for communication, information and data analysis with real skill.",
  'qaa/fheq-2024/4.15.b8', 'transferable/r1', "Which tool did you choose for your last analysis, and why that one?"),
]
M = [
 ('b1', [], 'public sector organisations, their context and management', 'knowledge',
  "Understands systematically and in depth what is known about public sector organisations, their surroundings and how they are run.",
  "a systematic, deep understanding of public sector organisations, their context and their management.",
  "understand public sector organisations, their setting and how they are managed, systematically and in depth.",
  'qaa/fheq-2024/4.17.b1', '4.6.b1', "Which model of public management best explains the organisation you know, and where does it fail?"),
 ('b2', [], 'techniques for investigation, research and evaluation', 'understanding',
  "Understands fully and in detail the techniques for close investigation, research and evaluation, or advanced scholarship, in the field.",
  "a full, detailed understanding of the techniques used for close investigation, research and evaluation, or advanced scholarship, in the field.",
  "understand fully the techniques for detailed investigation, research and evaluation in the field.",
  'qaa/fheq-2024/4.17.b2', '4.6.b9', "Which evaluation technique suits your dissertation question, and why not the alternatives?"),
 ('b3', ['demonstrate'], 'proactive, independent learning', 'generic-skill',
  "Shows a proactive and independent approach to learning.",
  "a proactive, independent approach to learning.",
  "take charge of your learning, proactively and independently.",
  'qaa/fheq-2024/4.17.b6 and 4.17.b7', '4.6.b10', "What have you learned this term that nobody asked you to learn?"),
 ('b4', ['demonstrate'], 'agile, reflexive and innovative learning', 'generic-skill',
  "Shows an agile, reflexive and inventive approach to learning.",
  "an agile, reflexive and inventive approach to learning.",
  "learn in a flexible, reflexive and inventive way.",
  'qaa/fheq-2024/4.17.b7', '4.6.b6', "When did you change your approach mid-way because what you were doing was not working?"),
 ('b5', ['informed'], 'critical awareness of current issues', 'understanding',
  "Is critically and subtly aware of current issues, drawing on research and practice.",
  "a critical, nuanced awareness of current issues, grounded in research and practice.",
  "have a critical, nuanced awareness of current issues, grounded in research and practice.",
  'qaa/fheq-2024/4.17.b1', '4.6.b2', "Which current issue in public policy is most misunderstood, and what does research say about it?"),
 ('b6', ['enable'], 'critically evaluating research and scholarship', 'subject-skill',
  "Has the conceptual competence to evaluate current research and advanced scholarship critically.",
  "the conceptual competence to evaluate current research and advanced scholarship critically.",
  "have the conceptual tools to evaluate current research and advanced scholarship critically.",
  'qaa/fheq-2024/4.17.b4.1', '4.6.b2', "What are the weakest assumptions in the most-cited study you have read?"),
 ('b7', ['taking'], 'applying knowledge to complex situations', 'subject-skill',
  "Applies relevant knowledge to a variety of complex situations, allowing for the field's mixed public, private and non-profit setting.",
  "the ability to apply relevant knowledge to varied complex situations, allowing for the field's hybrid setting.",
  "apply what you know to many complex situations, allowing for the mix of public, private and non-profit settings in the field.",
  'qaa/fheq-2024/4.17.b5', '4.6.b7', "How would your recommendation change if the service were run by a charity instead of a council?"),
 ('b8', ['used', 'create', 'interpret'], 'originality, creativity and entrepreneurship with research techniques', 'subject-skill',
  "Applies knowledge with originality, creativity and entrepreneurship, and understands in practice how established research techniques produce and interpret knowledge.",
  "originality, creativity and entrepreneurship in applying knowledge, and a practical grasp of how established research techniques produce and interpret knowledge.",
  "apply what you know with originality, creativity and enterprise, and understand in practice how research methods create and interpret knowledge.",
  'qaa/fheq-2024/4.17.b3', '4.6.b8', "What is original in your approach, and which established method does it rest on?"),
 ('b9', ['evaluate', 'integrate'], 'integrating theory, practice and experience', 'subject-skill',
  "Can assess and combine theory, practice and experience across many situations.",
  "can assess and combine theory, practice and experience across many situations.",
  "assess and combine theory, practice and experience in many kinds of situation.",
  'qaa/fheq-2024/4.17.b5', '4.6.b14', "Where has your own work experience challenged a theory you were taught?"),
 ('b10', ['advanced'], 'how research and practice extend knowledge', 'understanding',
  "Understands fully how research and practice push forward the limits of knowledge.",
  "a full understanding of how research and practice push forward the limits of knowledge.",
  "understand fully how research and practice push knowledge forward.",
  'qaa/fheq-2024/4.17.b3', '4.6.b2', "Can you name a change in practice that came from research, and one that came the other way?"),
 ('b11', ['acting', 'promoting'], 'public sector values, ethics and integrity', 'understanding',
  "Understands, and is committed to, the values and ethics of public service, and sees why acting with integrity and encouraging it in others matters.",
  "a developed grasp of, and commitment to, the values and ethics of public service, acting with integrity and encouraging it in others.",
  "understand and commit to public sector values and ethics, and act with integrity and encourage it in others.",
  'qaa/fheq-2024/4.17.b8.1', '4.6.b13', "Which public service value would you defend even at a cost to efficiency?"),
 ('b12', ['enhance'], 'professional reflection', 'generic-skill',
  "Has professional reflective capacities that improve professional practice.",
  "professional reflective capacities that improve professional practice.",
  "reflect as a professional in ways that improve your practice.",
  'qaa/fheq-2024/4.17.b7', '4.6.b6', "What has reflecting on your work changed in how you practise?"),
 ('b13', ['impact'], 'effects of policy and administration on societies and the environment', 'understanding',
  "Understands, with nuance, how policy and administration affect societies and the environment.",
  "a nuanced understanding of how policy and administration affect societies and the environment.",
  "understand, with nuance, how policy and administration affect people, societies and the environment.",
  'qaa/fheq-2024/4.17.b1', '4.6.b2', "Who gains and who loses, socially and environmentally, from the policy you know best?"),
 ('b14', ['take'], 'an international and global perspective', 'generic-skill',
  "Can take an international and global view.",
  "can take an international and global view.",
  "look at questions from an international and global point of view.",
  'qaa/fheq-2024/4.17.b5', '4.6.b2', "How has another country tackled the problem you are studying, and could it work here?"),
 ('b15', ['work', 'engage', 'lead'], 'collaborative, diverse working and leadership', 'generic-skill',
  "Can work, engage and lead in collaborative, multicultural and diverse settings at home and abroad.",
  "can work, engage and lead in collaborative, multicultural and diverse settings at home and abroad.",
  "work, engage and lead in collaborative, multicultural and diverse settings, in the UK and internationally.",
  'qaa/fheq-2024/4.17.b8.2', '4.6.b3', "When have you led a group whose members saw the problem very differently?"),
 ('b16', ['negotiate', 'influence'], 'negotiation and influence', 'generic-skill',
  "Can negotiate and influence in professional settings.",
  "can negotiate and influence in professional settings.",
  "negotiate and influence others in professional settings.",
  'qaa/fheq-2024/4.17.b5', '4.6.b4', "How would you persuade a reluctant partner agency to share data?"),
 ('b17', [], 'independent learning for continuing professional development', 'generic-skill',
  "Has the independent learning ability needed for continuing professional development.",
  "the independent learning ability needed for continuing professional development.",
  "have the independent learning ability you need to keep developing professionally.",
  'qaa/fheq-2024/4.17.b8.3', '4.6.b10', "What will you need to learn in the next five years, and how will you learn it?"),
]

_TRIM = {'4.5.b15': ' Excellent level', '4.6.b16': " Master's"}
_SPAN = {c['id'].split('/')[-1]: (c['span']['start'], c['span']['end']) for c in _SK['candidateStatements']}
def _item(i):
    a, b = _SPAN[i]
    t = _NORM[a:b]
    if i in _TRIM and t.endswith(_TRIM[i]):
        return t[:-len(_TRIM[i])], a
    return None, None

LV6 = 'FHEQ level 6 (FQHEIS level 10, spine:6)'
LV7 = 'FHEQ level 7 (FQHEIS level 11, spine:7)'
for k, verbs, about, dom, para, prac, ben, fw, ann, q in T:
    i = '4.5.' + k
    f, a = _item(i)
    xs = [x for x in X if x[1] == k][0][0]
    s(i, find=f, after=a, type='threshold', rung='threshold', force='threshold', level='fheq:6', appliesTo='honours graduates at threshold level',
      addressee='learner', verbs=verbs, about=about, domain=dom, award=HON,
      para='Threshold (the minimum for the award): ' + para,
      prac='At threshold, graduates ' + prac,
      ben='To reach the minimum standard for your honours degree, you will ' + ben,
      aaw=("Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at " + LV6 + ": " + about + ". "
           "Cite it as " + CITE % ('4.5, item ' + k[1:]) + ", and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. "
           "Set it beside the excellent-level item 4.6." + xs + ", the FHEQ descriptor " + fw + " and the Annex D third-class cell qaa/fheq-2024/annex-d/" + ann + ('/3rd-1st' if ann.startswith('professional') else '/3rd') + "."),
      aad=("Raise it when a student or teacher asks what the minimum for an honours degree looks like in " + about + ". "
           "Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"" + q + "\" "
           "Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."))
for k, tk, verbs, about, dom, para, prac, ben, fw, ann, q in X:
    i = '4.6.' + k
    f, a = _item(i)
    nb = ('the threshold item 4.5.' + tk) if tk else 'the threshold list 4.5 (it has no threshold counterpart)'
    s(i, find=f, after=a, type='excellent', rung='excellent', force='will', level='fheq:6', appliesTo='honours graduates at an excellent level',
      addressee='learner', verbs=verbs, about=about, domain=dom, award=HON,
      para='Excellent level (will): ' + para,
      prac='At the excellent level, graduates will ' + prac,
      ben='At an excellent level, you will ' + ben,
      aaw=("Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at " + LV6 + ": " + about + "; it is what the strongest graduates are expected to show, not a minimum. "
           "Cite it as " + CITE % ('4.6, item ' + k[1:]) + ", and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). "
           "Set it beside " + nb + ", the FHEQ descriptor " + fw + " and the Annex D first-class cell qaa/fheq-2024/annex-d/" + ann + ('/3rd-1st' if ann.startswith('professional') else '/1st') + "."),
      aad=("Raise it when a student aims high or a teaching team calibrates top-band work on " + about + ". "
           "Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"" + q + "\" "
           "Do not quote the statement at length, and point a student worried about passing to " + (('4.5.' + tk) if tk else 'the threshold list 4.5') + " instead."))
for k, verbs, about, dom, para, prac, ben, fw, hon, q in M:
    i = '4.7.' + k
    s(i, type='threshold', rung='threshold', force='will', level='fheq:7', appliesTo="master's graduates in the subject",
      addressee='learner', verbs=verbs, about=about, domain=dom, award=MAS,
      para="Master's level (will): " + para,
      prac="At master's level, graduates will show " + prac if not prac.startswith('can ') else "At master's level, graduates will " + prac[4:],
      ben="On a master's in this subject, you will " + ben,
      aaw=("Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at " + LV7 + ": " + about + ". "
           "Cite it as " + CITE % ('4.7, item ' + k[1:]) + ", and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. "
           "Set it beside the FHEQ master's descriptor " + fw + " and, for the step up from honours, " + hon + "."),
      aad=("Raise it with a master's student, or a team designing a master's course, when the talk turns to " + about + ". "
           "Put it in plain words as the step beyond honours that a master's should bring, and ask: \"" + q + "\" "
           "Avoid reading the statement out and avoid applying it to undergraduates."))
# the lead-in's own first sentence: three outcomes outside the list
_f47 = _NORM[_CS['4.7'][0]:_NORM.index('They will also have extended', _CS['4.7'][0])].rstrip()
s('4.7', find=_f47, after=_CS['4.7'][0], type='threshold', rung='threshold', force='will', forceFrom='They will also have extended their knowledge', level='fheq:7', appliesTo="master's graduates in the subject",
  addressee='learner', verbs=['demonstrate'], about='specialist command and independent project work', domain='subject-skill', award=MAS,
  para="Master's graduates in the subject are expected to show graduate outcomes, command of at least one specialist area and independence in project work.",
  prac="At master's level, graduates will show graduate outcomes, command of at least one specialist area and independent project-based work.",
  ben="On a master's in this subject, you will show that you command at least one specialist area and can carry out project work independently.",
  aaw=("Describe this as the lead outcome for a master's in Public Policy or Public Administration, read at " + LV7 + ": graduate outcomes, specialist command and independence in project work. "
       "Cite it as " + CITE % '4.7' + ", and do not claim the statement names a master's level or sets merit or distinction standards. "
       "Set it beside the list items 4.7.b1 to 4.7.b17 and the FHEQ master's descriptors qaa/fheq-2024/4.17.b1 and 4.17.b6."),
  aad=("Raise it when a master's student plans a dissertation or a team scopes specialist pathways. "
       "Ask: \"Which specialist area will your project show you command, and which decisions in it are yours alone?\" "
       "Avoid treating independence as working without supervision, and avoid reading the paragraph out."))

# gradeOf: the same outcome one rung below (no typical rung: excellent links to threshold), inferred by content
GRADE = {'4.6.' + k: '4.5.' + tk for k, tk, *_ in X if tk}

# =============================================================== document-level records
_SUBJ = [dict(scheme='hecos', code='100647', label='public policy', basis='stated'),
         dict(scheme='hecos', code='100090', label='public administration', basis='stated'),
         dict(scheme='cah', code='CAH15-01-03', label='social policy', basis='inferred'),
         dict(scheme='cah', code='CAH15-03-01', label='politics', basis='inferred'),
         dict(scheme='hecos', code='100091', label='public services', basis='inferred')]
META = dict(
    run='0128', p1='2026-10-03 18:24',
    title='Subject Benchmark Statement Public Policy and Public Administration',
    heading='Subject Benchmark Statement: Public Policy and Public Administration (QAA, April 2025)',
    edition='April 2025 (first edition)', published='2025-04',
    status='current', supersedes='none: the statement calls itself new (front matter) and first edition (back matter)',
    subjects=_SUBJ,
    awards=[HON, MAS], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2025 series with five cross-cutting themes (first edition, published 10 April 2025)',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("QAA's UK reference point for what a graduate in Public Policy or Public Administration should know, understand and be able to do, at honours and at master's level. "
                     "Reach for it when designing, approving, reviewing or describing a course in either subject, or one that teaches them inside economics, politics, social policy or management. "
                     "Its honours standards come at two levels, threshold and excellent, with no typical level; its master's standards are one list. "
                     "It is not a regulatory requirement, not a competence standard and not a classification scheme, which it leaves to Annex D."),
    summary=("A new statement, published by QAA on 10 April 2025, covering Public Policy and Public Administration as linked but distinct subjects: policy as the study of what shapes government decisions, "
             "administration as how policy is formed and carried out. It sets the purposes of the degrees, five cross-cutting themes (equity, diversity and inclusion; accessibility; education for sustainable development; "
             "employability, entrepreneurship and enterprise; generative AI), distinctive features of design, progression, flexibility, partnership and review, 40 typical subfields and the teaching, learning and assessment used, "
             "and standards in three lists: a threshold list (15 items) and an excellent list (16) for honours, and a master's list (17 items under a lead-in). "
             "It names the Chartered Management Institute and three public administration accreditors (ICAPA, EAPAA, NASPAA) as routes to accreditation, and points to Annex D for classification."),
    authority=("reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; "
               "part of the quality arrangements in Scotland, Wales and Northern Ireland (D1, Relationship to legislation)"))

S2 = dict(
    governs="what can be expected of a graduate in Public Policy and/or Public Administration, at honours and master's level, and the nature of degrees in the two subjects (D1, front matter; 1.1; 4.1)",
    awards=["bachelor's degrees with honours, including joint and combined honours (2.7, 2.8)", "master's degrees, including MPA, MPP, MSc and executive MA or MSc (1.4, 2.11, 4.7)",
            "relevant to foundation degrees, with no standards set at their level (1.4)"],
    levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    howUsed=['design', 'approval', 'review', 'other: external examining (front matter, 2.21); PSRBs (front matter); prospective students, employers and scholars (front matter)'],
    statedScope='"This Subject Benchmark Statement sets out the context and purposes of degrees in Public Policy and in Public Administration, which are linked and at the same time distinct areas of study." (D1, 1.1)',
    statedSubjects=[
        dict(name='Public Policy', locator='(D1, title; 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100647', label='public policy')]),
        dict(name='Public Administration', locator='(D1, title; 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100090', label='public administration')]),
        dict(name='Master of Public Administration (MPA)', locator='(D1, 2.11)', kind='programme title', codes=[dict(scheme='hecos', code='100090', label='public administration')]),
        dict(name='Master of Public Policy (MPP)', locator='(D1, 2.11)', kind='programme title', codes=[dict(scheme='hecos', code='100647', label='public policy')]),
        dict(name='Police Leadership and Management; Healthcare Management; Local Government Management', locator='(D1, 1.4)', kind='programme title', codes=[]),
        dict(name='economics, finance, politics, public ethics, political geography, planning, urban studies, social policy, sociology, management, law and business', locator='(D1, 1.3)',
             kind='subject', codes=[dict(scheme='hecos', code='100491', label='politics'), dict(scheme='hecos', code='100502', label='social policy')])])

SECTIONS = {'1': 'Context and purposes of a Public Policy and Public Administration degree', '2': 'Distinctive features of Public Policy and Public Administration degrees',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.8', 'Context and purposes of a Public Policy and Public Administration degree'),
       ('1.9', '1.11', 'Purposes and characteristics of a Public Policy and Public Administration degree'),
       ('1.12', '1.14', 'Equity, diversity and inclusion'), ('1.15', '1.17', 'Accessibility and the needs of disabled students'),
       ('1.18', '1.19', 'Education for sustainable development'), ('1.20', '1.25', 'Employability, entrepreneurship and enterprise education'),
       ('1.26', '1.28', 'Generative artificial intelligence'),
       ('2.1', '2.5', 'Design'), ('2.6', '2.14', 'Progression'), ('2.15', '2.16', 'Flexibility'), ('2.17', '2.18', 'Partnership'), ('2.19', '2.23', 'Monitoring and review'),
       ('3.1', '3.2', 'Content, structure and delivery'), ('3.3', '3.5', 'Content'), ('3.6', '3.9', 'Teaching and learning'), ('3.10', '3.13', 'Assessment and feedback'),
       ('4.1', '4.4', 'Introduction'), ('4.5', '4.5', 'Threshold level'), ('4.6', '4.6', 'Excellent level'), ('4.7', '4.7', "Master's")]

G = {
 '1.1': 'policy and administration as linked, distinct subjects', '1.2': 'what the courses investigate and develop', '1.3': 'taught across many host disciplines',
 '1.4': 'degree types the statement serves', '1.5': 'governmental decisions, resources and levels of enquiry', '1.6': 'the policy cycle and fairness at its core',
 '1.7': 'principles of good public decision-making', '1.8': 'interdisciplinarity, co-design and collaboration', '1.9': 'seven purposes of the degree',
 '1.10': 'skills for uncertain settings and many jobs', '1.11': 'public sector scale and critical evaluation', '1.12': 'EDI in delivery and curriculum (should)',
 '1.13': 'curricula that champion EDI', '1.14': 'EDI in academic and administrative practice (should)', '1.15': 'accessibility in degree design',
 '1.16': 'reasonable adjustments and equal access', '1.17': "graduates' part in accessible services", '1.18': 'the subject and sustainable development',
 '1.19': 'pedagogies for ESD', '1.20': 'responsibilities of public roles; enterprise education', '1.21': 'what enterprise education can do (nine claims)',
 '1.22': 'links to enterprise; experienced students (must)', '1.23': 'graduates recognise and convey enterprise skills', '1.24': 'work with employers and stakeholders',
 '1.25': 'professional accreditation routes', '1.22-2': 'cross-sector skills and changing employer needs (second 1.22)', '1.26': 'responding to generative AI (must)',
 '1.27': 'responsible GenAI education', '1.28': 'ethical use of technology',
 '2.1': 'multidisciplinary study and career readiness', '2.2': 'integrating policy with administration', '2.3': 'skills and themes courses promote',
 '2.4': 'multilevel governance and public value', '2.5': 'practitioner teaching', '2.6': 'undergraduate provision across the UK',
 '2.7': 'progression through an honours degree', '2.8': 'joint and combined degrees', '2.9': 'exit awards', '2.10': 'degree length across the nations',
 '2.11': "master's provision and cohorts", '2.12': "integrated master's", '2.13': 'postgraduate entry', '2.14': 'graduates as policymakers and leaders',
 '2.15': 'flexible learning for working students', '2.16': 'forms of flexible learning; CPD accreditation', '2.17': 'what partnerships create',
 '2.18': 'partners and cross-sector collaboration', '2.19': 'monitoring, review and the student voice', '2.20': 'external reviewers',
 '2.21': 'external examiners', '2.22': 'advisory boards', '2.23': 'integrating accreditation requirements',
 '3.1': 'purpose of the section', '3.2': 'practice-based learning', '3.3': 'governance content and 40 typical subfields', '3.4': 'policy and administration emphases compared',
 '3.5': 'transferable capacities; vocational and theoretical range', '3.6': 'teaching environments and digital inclusion', '3.7': 'learning methods (eight kinds)',
 '3.8': 'learning environments, resources and digital literacy', '3.9': 'research-led teaching and practitioner input', '3.10': 'assessment strategy and its alignment',
 '3.11': 'plural assessment and adjustments', '3.12': 'five kinds of assessment', '3.13': 'feedback',
 '4.1': 'what the standards set out', '4.2': 'performance above threshold; Annex D', '4.3': 'threshold standards are not competence standards',
 '4.4': 'scope and use of the standards', '4.5': 'threshold list for honours (15 items)', '4.6': 'excellent list for honours (16 items)', '4.7': "master's lead-in and list (17 items)"}

CTYPE = {'3.3': 'area', '3.4': 'area', '3.5': 'area', '3.2': 'practice', '3.6': 'practice', '3.7': 'practice', '3.8': 'practice', '3.9': 'practice',
         '3.10': 'practice', '3.11': 'practice', '3.12': 'practice', '3.13': 'practice'}

EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='section heading lines 1 to 4', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for SB6 shared documents'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: back matter, read for S8 (first edition, 10 April 2025)')]

TH = {'1.12': 'theme:edi', '1.14': 'theme:edi', '1.17': 'theme:accessibility', '1.22': 'theme:enterprise', '1.23': 'theme:enterprise', '1.26': 'theme:generative-ai'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.7; 4.2 (honours); 4.5 and 4.6 read as level 6'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.7; 4.2'),
                  dict(id='fheq:7', role='cites', locator="D1, 2.12 (integrated master's); 4.7 read as level 7 (inferred for taught master's)"),
                  dict(id='fqheis:11', role='cites', locator='D1, 2.12'),
                  dict(id='fheq:4', role='cites', locator='D1, 2.9 (CertHE exit award)'), dict(id='fqheis:8', role='cites', locator='D1, 2.9'),
                  dict(id='fheq:5', role='cites', locator='D1, 2.9 (DipHE exit award)'), dict(id='fqheis:9', role='cites', locator='D1, 2.9')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.7: honours at FHEQ Level 6, FQHEIS Level 10; 4.2)'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.12: integrated master's at FHEQ Level 7, FQHEIS Level 11)"),
                      dict(**{'from': 'fheq:4'}, to='fqheis:8', relation='equivalent', basis='stated (D1, 2.9: CertHE at FHEQ Level 4, FQHEIS Level 8)'),
                      dict(**{'from': 'fheq:5'}, to='fqheis:9', relation='equivalent', basis='stated (D1, 2.9: DipHE at FHEQ Level 5, FQHEIS Level 9)'),
                      dict(**{'from': '4.5 threshold'}, to='Annex D 3rd (pass or threshold)', relation='thresholdAt', basis='inferred: 4.2 ties performance above the minimum threshold to Annex D; the statement does not map its levels to classes'),
                      dict(**{'from': 'fheq:6, fheq:7'}, to='spine:6, spine:7', relation='levelEquivalent', basis='inferred from std:ref:uk-framework R2')])

_EDI = ['front matter', '1.6', '1.12', '1.13', '1.14', '1.15', '1.16', '1.17', '1.21', '2.15', '2.19', '2.22', '3.3', '3.6', '3.8', '3.11', '3.13', '4.3', '4.7']
_ACC = ['front matter', '1.6', '1.15', '1.16', '1.17', '3.6', '3.11']
_ESD = ['front matter', '1.6', '1.18', '1.19', '2.22', '3.3', '3.6']
_EEE = ['front matter', '1.19', '1.20', '1.21', '1.22', '1.22 (second)', '1.23', '1.24', '1.25', '1.26', '2.22', '3.5', '3.6', '3.7', '3.10', '3.12', '4.7']
_GAI = ['front matter', '1.26', '1.27', '1.28', '3.8', '3.12']
S6 = [dict(id='theme:edi', role='carries', carriedIn=_EDI), dict(id='theme:accessibility', role='carries', carriedIn=_ACC),
      dict(id='theme:esd', role='carries', carriedIn=_ESD), dict(id='theme:enterprise', role='carries', carriedIn=_EEE),
      dict(id='theme:generative-ai', role='carries', carriedIn=_GAI)]

S7 = [dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the classification descriptions providers should refer to for performance above threshold (4.2)'),
      dict(rel='cites', target='std:doc:qaa-fheq-2024-framework', note='FHEQ levels 4 to 7 named (2.7, 2.9, 2.12, 4.2); the 2024 Frameworks in the references'),
      dict(rel='cites', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS levels 8 to 11 named (2.7, 2.9, 2.12, 4.2)'),
      dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note="its definitions of sustainable development and ESD are quoted (1.18)"),
      dict(rel='cites', target='std:doc:qaa-enterprise-2018-guidance', note='listed in the references (back matter)'),
      dict(rel='refersTo', target="QAA (2020) Characteristics Statement: Master's Degree (not ingested)", note='listed in the references only'),
      dict(rel='relatedTo', target='std:ref:uk-framework', note='spine:6 and spine:7 for the honours and master\'s lists (inferred)')]

SB1 = ['Public Policy and Public Administration are joined but separate: policy studies what shapes the decisions of governments and regulators, administration studies how policy is formed and put into effect (D1, 1.1).',
       'The subjects study systems, processes, governance and management of public decisions at every tier of government, in democratic and non-democratic states, including the effects of decisions on citizens (D1, 1.2, 1.5, 3.3).',
       'They are taught in many host disciplines, among them economics, politics, social policy, sociology, planning, management, law and business (D1, 1.3).',
       'Study follows the policy cycle from problem definition and agenda-setting through design, transfer, instruments and implementation to evaluation, using several theories and comparisons across sectors and systems (D1, 1.6, 2.2).',
       'Fairness and social justice are central, including the UK public sector equality duty, and principles such as legality, accountability, proportionality and impartiality frame the judgement of public bodies (D1, 1.6, 1.7).',
       'The subjects are interdisciplinary, join theory with practice and stress effectiveness, efficiency and equity in service design, with co-design, co-production and collaboration between agencies (D1, 1.8, 2.1, 2.3).',
       'Public and social value, public service motivation and ethos are characteristic themes; courses are often taught with practitioners and use real cases (D1, 2.4, 2.5, 2.17, 2.18).',
       'Most provision is postgraduate (MSc, MPA, MPP), with pre- and post-experience cohorts; undergraduate Public Administration degrees are few, and public sector content is common in foundation degrees (D1, 2.6, 2.11).']

SB2 = [dict(theme='theme:edi', inThisSubject='equity is part of the subject matter: fair policy, just institutions and the public sector equality duty; EDI in curriculum, pedagogy and assessment, voices of subjugated groups, inclusive feedback and advisory input (D1, 1.6, 1.12 to 1.14, 3.13)',
            statements=['1.12', '1.14', '3.13', '4.3', '4.7.b15']),
       dict(theme='theme:accessibility', inThisSubject='graduates will design accessible services beyond legal compliance; courses make reasonable adjustments, accessible spaces, resources, visits and careers support, and digital inclusion (D1, 1.15 to 1.17, 3.6, 3.11)',
            statements=['1.17', '3.6']),
       dict(theme='theme:esd', inThisSubject='the subject equips future public managers and policymakers to realise the sustainable development goals; ESD pedagogies and UNESCO learning objectives; SDGs among the subfields (D1, 1.18, 1.19, 3.3)',
            statements=['3.3', '3.6', '4.7.b13']),
       dict(theme='theme:enterprise', inThisSubject='named employability, entrepreneurship and enterprise education (EEE): practice links required for pre- and post-experience students, graduates able to articulate their skills, employer work and accreditation routes (D1, 1.20 to 1.25, 3.10)',
            statements=['1.22', '1.23', '3.7', '3.10', '4.7.b8']),
       dict(theme='theme:generative-ai', inThisSubject='degrees must respond to an AI-shaped labour market and changing assessment; ethical, responsible use of GenAI, including in authentic assessment (D1, 1.26 to 1.28, 3.8, 3.12)',
            statements=['1.26'])]

SB3 = dict(areas=[dict(component='3.3', gloss='governance and policy across contexts; 40 typical subfields from administrative law to voluntary sector administration, of which courses cover a number'),
                  dict(component='3.4', gloss='policy degrees lean to the policy cycle and evaluation, administration degrees to leadership, management, project management and finance'),
                  dict(component='3.5', gloss='transferable cognitive, behavioural and affective capacities; vocational to theoretical range')],
           practices=[dict(component='3.2', kind='learning', gloss='practice-based learning, action learning, reflection and placements'),
                      dict(component='3.6', kind='teaching', gloss='methods fitted to content and learners; many modes; digital inclusion'),
                      dict(component='3.7', kind='learning', gloss='lectures, seminars, cases, simulations, work-based learning, independent study, practitioner talks, fieldwork'),
                      dict(component='3.8', kind='learning', gloss='diverse sources and digital tools, with support for critical and ethical use, GenAI included'),
                      dict(component='3.9', kind='teaching', gloss='research-led teaching and practitioner co-creation'),
                      dict(component='3.10', kind='assessment', gloss='strategy aligned with curriculum and outcomes; assessment for and as learning'),
                      dict(component='3.11', kind='assessment', gloss='plural assessment, workload and reasonable adjustments'),
                      dict(component='3.12', kind='assessment', gloss='five kinds: critical analysis, communication, independent research, authentic practice tasks, reflection'),
                      dict(component='3.13', kind='assessment', gloss='constructive, consistent and specific feedback throughout')])

_outs = [dict(outcome=tab[2], threshold='4.5.' + tab[1], typical='none', excellent='4.6.' + tab[0], basis='inferred', domain=tab[4], award=HON) for tab in X if tab[1]]
_outs.append(dict(outcome='academic practice and professional behaviour', threshold='none', typical='none', excellent='4.6.b14', basis='inferred', domain='subject-skill', award=HON))
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.5', award=HON, items=sum(1 for i in P if i.startswith('4.5.')), label='Threshold level'),
           dict(rung='typical', leadIn='none', award=HON, items=0, label='not stated'),
           dict(rung='excellent', leadIn='4.6', award=HON, items=sum(1 for i in P if i.startswith('4.6.')), label='Excellent level'),
           dict(rung='threshold', leadIn='4.7', award=MAS, items=sum(1 for i in P if i == '4.7' or i.startswith('4.7.')), label="Master's (no rung named; recorded as threshold by convention)")],
    rungBases=("4.5 and 4.6 are separate lists for honours graduates at threshold and at an excellent level of attainment; there is no typical list. 4.2 calls the threshold the minimum and refers classification to Annex D. "
               "4.7 is one master's list under a lead-in whose first sentence names three outcomes of its own (recorded as 4.7). 4.4: the standards are not a checklist and carry no weighting."),
    outcomeLists=[],
    outcomes=_outs)
SB4A_FULL = []

SB5 = [dict(body='professional, statutory and regulatory bodies (PSRBs)', says='the statement can support their definitions of academic standards; their requirements are among the reference points providers use and may inform competence standards (D1, front matter, 4.3)', requirements='not yet ingested (Part E)'),
       dict(body='Chartered Management Institute (CMI)', says='a professional accreditation providers may combine with degrees (D1, 1.25)', requirements='not yet ingested (Part E)'),
       dict(body='International Commission on the Accreditation of Public Administration and Training (ICAPA)', says='a route to additional academic accreditation (D1, 1.25)', requirements='not yet ingested (Part E)'),
       dict(body='European Association for Public Administration Accreditation (EAPAA)', says='a route to additional academic accreditation (D1, 1.25)', requirements='not yet ingested (Part E)'),
       dict(body='Network of Schools of Public Policy, Affairs and Administration (NASPAA)', says='a route to additional academic accreditation (D1, 1.25)', requirements='not yet ingested (Part E)'),
       dict(body='professional and accrediting bodies (generic)', says='where they evaluate professional or vocational outcomes, courses build their requirements into degree management; degrees may be accredited for CPD; course teams may engage with professional bodies (D1, 2.16, 2.23, 3.9)', requirements='not yet ingested (Part E)'),
       dict(body='Equality and Human Rights Commission', says='providers writing competence standards should follow its latest guidance (D1, 4.3)', requirements='not-applicable-by-design: guidance, not course requirements'),
       dict(body='Office for Students', says='in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)', requirements='not-applicable-by-design')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equity, diversity and inclusion (EDI)', carriedIn=_EDI, statements=[SID + '/' + x for x in SB2[0]['statements']]),
            dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=_ACC, statements=[SID + '/' + x for x in SB2[1]['statements']]),
            dict(id='theme:esd', named='Education for sustainable development (ESD)', carriedIn=_ESD, statements=[SID + '/' + x for x in SB2[2]['statements']]),
            dict(id='theme:enterprise', named='Employability, entrepreneurship and enterprise education (EEE)', carriedIn=_EEE, statements=[SID + '/' + x for x in SB2[3]['statements']]),
            dict(id='theme:generative-ai', named='Generative artificial intelligence (Gen AI)', carriedIn=_GAI, statements=[SID + '/' + x for x in SB2[4]['statements']])],
    frameworks=[dict(framework='fheq', levels=['fheq:4', 'fheq:5', 'fheq:6', 'fheq:7'], citedIn=['2.7', '2.9', '2.12', '4.2']),
                dict(framework='scqf', levels=['fqheis:8', 'fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.7', '2.9', '2.12', '4.2'])],
    bodies=[dict(body='PSRBs (generic)', citedIn=['front matter', '4.3']),
            dict(body='Chartered Management Institute (CMI)', citedIn=['1.25', 'back matter: references']),
            dict(body='ICAPA', citedIn=['1.25', 'back matter: references']), dict(body='EAPAA', citedIn=['1.25', 'back matter: references']),
            dict(body='NASPAA', citedIn=['1.25', 'back matter: references']),
            dict(body='professional and accrediting bodies (generic)', citedIn=['2.16', '2.23', '3.9']),
            dict(body='Equality and Human Rights Commission', citedIn=['4.3']), dict(body='Office for Students', citedIn=['front matter'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D of The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2'], role='the classification descriptions for performance above threshold'),
        dict(document='std:doc:qaa-fheq-2024-framework', named='The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies (2024)', citedIn=['4.2', 'back matter: references'], role='FHEQ and FQHEIS levels'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named="QAA and Advance HE's Education for Sustainable Development Guidance (2021)", citedIn=['1.18', 'back matter: references'], role='definitions of sustainable development and ESD; curriculum review'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (2018)', citedIn=['back matter: references'], role='the enterprise theme'),
        dict(document='QAA Creating Inclusive Subject Communities (2021) (not ingested: Part E)', named='Creating Inclusive Subject Communities: New QAA Advice', citedIn=['1.12', 'back matter: references'], role='EDI resource'),
        dict(document="QAA Characteristics Statement: Master's Degree (2020) (not ingested: Part E)", named="Characteristics Statement: Master's Degree", citedIn=['back matter: references'], role="background to the master's list"),
        dict(document='QAA Quality Code 2024 (not ingested)', named='the Quality Code (2024 update)', citedIn=['front matter'], role='sector reference point'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='QAA Academic integrity (not ingested)', named='Academic integrity', citedIn=['back matter: references'], role='integrity, read with the GenAI theme'),
        dict(document='UN Sustainable Development Goals (external)', named='United Nations Sustainable Development Goals (SDGs)', citedIn=['1.18', '3.3', 'back matter: references'], role='frame for ESD'),
        dict(document='UNESCO (2017) Education for Sustainable Development Goals: Learning Objectives (external)', named="UNESCO's ESD Learning Objectives", citedIn=['1.19', 'back matter: references'], role='learning objectives for ESD pedagogy'),
        dict(document='World Economic Forum (2023) Future of Jobs Report (external)', named='World Economic Forum Future Jobs Report (2023)', citedIn=['1.22 (second)', 'back matter: references'], role='changing employer priorities'),
        dict(document='Equality Act 2010 (law)', named='Equality Act 2010', citedIn=['4.3'], role='defines competence standards'),
        dict(document='public sector equality duty (law)', named='public sector equality duty (PSED)', citedIn=['1.6', 'back matter: references (Government Equalities Office)'], role='UK duty framing EDI in the subject')])

B1 = [dict(slug='employability-entrepreneurship-and-enterprise-education', definition='the cross-cutting theme, shortened to EEE, that builds the capacities students need for careers and for adding social, cultural and economic value (D1, 1.20, 1.21)',
           beneficiaryDefinition='learning that prepares you for work and for creating value of your own', scopeNote='the statement lists nine benefits it can bring (1.21)', category='unknown', practices=['education']),
      dict(slug='education-for-sustainable-development', definition="building curricula and subject content that support sustainable development, as the statement takes it from the 2021 ESD guidance (D1, 1.18)",
           beneficiaryDefinition='learning that helps you tackle social, environmental and economic problems for the future', scopeNote='sustainable development itself is defined there as an ongoing, aspirational process (1.18)', category='unknown', practices=['education']),
      dict(slug='public-sector-equality-duty', definition='the UK duty on public bodies, shortened to PSED, named as the immediate setting for equality in the subject (D1, 1.6)',
           beneficiaryDefinition='the legal duty on public bodies to consider equality', scopeNote='detailed in the Government Equalities Office guidance in the references', category='unknown', practices=['public administration'])]
B2A = [dict(concept='employability-entrepreneurship-and-enterprise-education', form='employability, entrepreneurship and enterprise education (EEE)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='education-for-sustainable-development', form='Education for Sustainable Development (ESD)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='public-sector-equality-duty', form='public sector equality duty (PSED)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]

D3 = [dict(citation='QAA (2021) Creating Inclusive Subject Communities: New QAA Advice', settles=['SB6'], asked='2026-10-03', state='not held'),
      dict(citation="QAA (2020) Characteristics Statement: Master's Degree", settles=['SB6', 'S5'], asked='2026-10-03', state='not held'),
      dict(citation='The requirements of CMI, ICAPA, EAPAA and NASPAA', settles=['SB5'], asked='2026-10-03', state='not held')]

E = [
 "Rungs: two for honours, threshold (4.5, 15 items) and excellent (4.6, 16 items); no typical rung. Pattern differs from Psychology (three rungs).",
 "Master's: one list (4.7, 17 items) under a lead-in with no rung named; recorded as rung threshold, award master's, level fheq:7 by convention. Ids kept as the issuer's 4.7.b<k> (unique, own paragraph) rather than the .masters suffix, which the convention gives for shared table spans. The level is inferred: 4.7 names no level; 2.12 states FHEQ 7 / FQHEIS 11 only for integrated master's.",
 "4.7's lead-in first sentence states three outcomes of its own (graduate outcomes, specialist command, independence in project work): recorded as statement 4.7 (find on that sentence), counted in the master's rung (18 records). Its force word is 'are expected to' (outside the five); recorded as will from the lead-in's second sentence (forceFrom 4.7). For P3.",
 "Lead-in wording new against Psychology: 'are expected to be able to demonstrate' (4.5, 4.6) and 'are expected to demonstrate ... They will also have extended' (4.7). 'Expected to' is outside the five force words: threshold items take force threshold (4.2 and 4.3 call these the minimum threshold standards); excellent items take will (from 'able to'); master's items will.",
 "gradeOf (inferred, by content, not position): 15 excellent items link to the threshold item below (no typical rung, so excellent links straight to threshold): 4.6.b1-4.5.b1, b2-b2, b3-b7, b4-b8, b5-b3, b6-b9, b7-b4, b8-b5, b9-b6, b10-b10, b11-b11, b12-b12, b13-b13, b15-b14, b16-b15. 4.6.b14 (academic practice and professional behaviour) has no threshold counterpart. All for P3.",
 "Duplicate numbering: the issuer numbers two paragraphs 1.22 (the second, after 1.25, on cross-sector skills); the skeleton keys it 1.22-2. Statement 1.22 is the first; the second is a plain-present paragraph, not a statement.",
 "Statements cut: 23 paragraph records (must 2: 1.22, 1.26; should 4: 1.12, 1.14, 4.2, 4.3; will 17) plus 49 rung records = 72. 3.3 and 3.7 are recorded on their stems (find); their list items are SB3 areas and practices, not statements.",
 "Not statements (D-std-0002 (a); template open point 5), listed for Abbott's P3 on plain-present provider norms: 1.13, 1.15, 1.16, 1.20, 1.22 (second), 3.8, 3.11, 3.12 (assessments courses include) and the 'can' and 'may' paragraphs 1.24, 1.25, 1.27, 1.28, 2.1, 2.9, 2.16, 2.17, 2.18, 2.22. 1.22 (second) and 1.20 state graduate or student outcomes in the plain present ('graduates recognise and demonstrate these skills'): a doubtful exclusion.",
 "Not statements, doubtful: 1.9 (seven purposes of the degree, 'to develop', no modal: an intended-outcomes list in all but form); 1.21 (nine things EEE 'can' do: claims about the theme, cut by the skeleton as candidates, dropped); 1.4 (degree types); 2.21 and 3.4, 3.5 ('will' used descriptively of typical practice); 4.1 (introduction to the rungs, 'will' framing).",
 "Included on 'will' with weak standard content, for P3: 1.10 and 1.17 (predictions about graduates' careers), 2.19 (student voice 'will form part of' review), 3.2 ('will typically learn').",
 "2.23 'will need to' integrate accrediting bodies' requirements: an obliging phrase outside the five; force recorded as will (the issuer's own modal); nearest meaning must. For Abbott.",
 "2.7 'it is expected that each level would see ...' and 'it would be expected that a student ... would be capable of': obliging wording outside the five, under the paragraph's will; recorded as will.",
 "1.23 speaks of graduates generally (1.20 names undergraduate and postgraduate students); recorded at honours, fheq:6 (inferred) so the generic skill carries a level.",
 "Codes: hecos 100647 public policy and 100090 public administration match the subject names the statement gives (stated). CAH15-01-03 (social policy) and CAH15-03-01 (politics) are the CAH parents of those codes, inferred; hecos 100091 public services inferred from the subject's focus on public service delivery (1.2, 2.1). All inferred codes held back for P3.",
 "Foundation degrees: 1.4 says the statement is relevant to them and 2.6 notes public sector content in foundation degrees, but no standard is set at fheq:5; awardsCovered lists honours and master's only.",
 "Exit awards (2.9: CertHE at FHEQ 4 / FQHEIS 8; DipHE at FHEQ 5 / FQHEIS 9) recorded in S5 as cited levels and crosswalks; no standards at those levels.",
 "Theme id: generative AI recorded as theme:generative-ai (batch convention). The front matter names five themes; EEE is the issuer's name for the enterprise theme (theme:enterprise).",
 "Annex D thresholdAt link (S5): inferred; the statement does not map threshold or excellent to classes. Agent instructions point threshold items to Annex D 3rd cells and excellent items to 1st cells, by our reading of content (std:doc:qaa-fheq-2024-framework).",
 "Verbs: several rung items are noun phrases with no verb in their span (for example 4.5.b1, 4.5.b8, 4.6.b12); their verbs list is empty, as the check requires each verb to be in the span.",
 "Bodies: CMI, ICAPA, EAPAA and NASPAA (1.25) are named as accreditation routes; their requirements are not ingested (D3). The Local Government Association appears only as an advisory group member's affiliation (back matter), not recorded.",
 "References name EAPAA as 'EAPPA' (back matter typo); recorded as EAPAA, the body's name in 1.25.",
 "CQFW: not named in the statement; not cited in SB6. Levels checked against the FHEQ (4.15, 4.17, Annex D), FQHEIS (4.16) and the reference framework (R2 spine, R8).",
 "S9 commentary not researched in P1.",
]
