# bm_content.py: judgement for run 0082, QAA Subject Benchmark Statement Accounting (April 2025). std run agent.
# Read by tools/bm_build.py. Keys of P are S4 ids under qaa/accounting-2025/. All text below except `find` spans is ours.
import json as _json, re as _re

_ST = '/home/claude/wkspc2601-library/ingested/standards'   # moved to the source library (std N-0119)
_NORM = open('/home/claude/wkspc2601-library/txt/qaa-2025-accounting-subject-benchmark-statement-standard.norm.txt', encoding='utf-8').read()
_SK = _json.load(open(_ST + '/ingest-std-qaa-accounting-2025-benchmarks/run-src/bm-skel.json', encoding='utf-8'))
_CS = {c['number']: (c['start'], c['end']) for c in _SK['components']}
_HEADS = ['Purposes and characteristics of an Accounting degree', 'Equality, diversity and inclusion',
          'Accessibility and the needs of disabled students', 'Education for sustainable development',
          'Employability, enterprise and entrepreneurship education', 'Generative artificial intelligence',
          'Progression', 'Flexibility', 'Partnership', 'Monitoring and review',
          'Knowledge, understanding and subject-specific skills', 'Transferable, professional and practice skills',
          'Learning and teaching', 'Assessment', 'Undergraduate awards']

def _tidy(t):
    t = t.rstrip()
    t = _re.sub(r'\s*\n\n\d+\s*$', '', t)
    return t.rstrip()

def _para(n):
    """the paragraph's own text: the skeleton span without a trailing sub-heading or page number"""
    a, b = _CS[n]
    t = _tidy(_NORM[a:b])
    for h in _HEADS:
        if t.endswith(' ' + h):
            t = t[:-len(h) - 1].rstrip()
            break
    return t, a

def _items(markers, end, start):
    """list items by their issuer letters: each from its letter to the next item's letter"""
    pos = []
    for m in markers:
        p = _NORM.index(m, start); pos.append(p); start = p + 1
    e = _NORM.index(end, pos[-1])
    return [(_tidy(_NORM[p:(pos[i + 1] if i + 1 < len(pos) else e)]), p) for i, p in enumerate(pos)]

def _cells(starts, cur):
    out = []
    for s in starts:
        a = _NORM.index(s, cur)
        b = _re.compile(r'\.(?=\s|$)').search(_NORM, a + len(s)).end()
        out.append((_NORM[a:b], a)); cur = b
    return out

HON = "bachelor's with honours"
ADV = "master's (advanced or specialist)"
CONV = "master's (conversion)"
PROF = "master's (professional)"
INT = "integrated master's"
MAS = [ADV, CONV, PROF, INT]
NA = ('n/a', 'a duty on the course and the people who design and run it, not a standard the student reaches')

P = {}
def s(i, find=None, after=None, **k):
    if find is None and i in _CS:
        find, after = _para(i)
    if find is not None:
        k['find'] = find; k['after'] = after if after is not None else 0
    P[i] = k

# provider duty, course-wide
def prov(i, **k):
    d = dict(type='requirement', rung='none', force='should', level='none', appliesTo='Accounting courses',
             addressee='provider', domain='none', award='none', ben=NA)
    d.update(k); s(i, **d)

# a duty on the course with an effect the student meets
def both(i, **k):
    d = dict(type='expectation', rung='none', force='should', level='none', appliesTo='Accounting courses and their students',
             addressee='both', domain='none', award='none')
    d.update(k); s(i, **d)

# =============================================================== section 1: context and purposes
prov('1.2', force='must', level='fheq:6', award=HON, appliesTo='joint Accounting and finance courses',
  verbs=['aligned', 'include'], about='joint Accounting and finance courses',
  para="Courses with a large finance element fall within this statement, single honours finance does not (the Finance statement covers it); a joint Accounting and finance course should draw substantially on both statements and must cover conceptual issues and theory in accounting, accountability, sustainability, uses of accounting outside business, its applied side and higher-order thinking.",
  prac="If you lead a joint Accounting and finance course, align it with both subject statements; it must still give real weight to accounting concepts and theory, accountability, sustainability, non-business uses, practical application and higher-order intellectual skills.",
  q="Which modules carry the conceptual and non-business side of accounting, so that finance content does not crowd it out?")
prov('1.3', level='fheq:6', award=HON, appliesTo='joint honours courses that include Accounting',
  verbs=['applied'], about='Accounting within joint honours with other subjects',
  para="Where Accounting is joined with a related or an unrelated subject, this statement should be used together with the other subject's statement, and the mix should not squeeze out accounting concepts, theory, accountability, sustainability, non-business uses, application or higher-order thinking.",
  prac="In a joint honours design, read this statement beside the partner subject's and check that the balance still leaves room for accounting concepts and theory, accountability, sustainability, non-business uses, application and higher-order thinking.",
  q="When the partner subject takes half the credit, what is left of accounting theory and accountability?")
both('1.4', verbs=['educate', 'understand', 'reflect', 'consider'], domain='understanding', about='the purpose of an Accounting degree',
  para="An Accounting degree should prepare students to understand accounting in its social and economic setting and its part in responsible governance, audit and assurance, as a base for many careers and for ethical citizenship; it should look past profit and capital to accountability for sustainability and welfare, to the many kinds of organisation and stakeholder that use accounting, and to past and current research.",
  prac="Shape the course so that students see accounting as a social and economic practice tied to governance and accountability, across public, charitable, co-operative and private bodies and their stakeholders, not only as the measurement of profit and capital; ground it in foundational and current research.",
  ben="Your course should help you see what accounting does in society and in how organisations are governed, well beyond profit, including its part in sustainability and welfare and in the work of charities, public bodies and campaigns.",
  q="Where in your course do you meet accounting outside the for-profit company, and what did it show you?")
prov('1.5', verbs=['designed', 'meet'], about='designing for students with different aims',
  para="Accounting degrees should be built to serve students who come to them for different reasons: a professional qualification, a route into business, government or other sectors, a wider social interest or the intellectual pursuit itself.",
  prac="Design for a mixed cohort: some students want a professional accountancy route, others business, public-sector or third-sector careers, social understanding or the subject for its own sake; the breadth of perspectives serves them all.",
  q="Which of these student aims does the current design serve least well?")
both('1.6', verbs=['study', 'informed'], domain='understanding', about='accounting systems and the social sciences',
  para="Students study how accounting systems shape and are shaped by theory, people, organisations, technology, markets, society and the environment; that study should draw on social science perspectives, for example politics, sociology, psychology, economics and information systems, with finance covered as the course's nature requires.",
  prac="Bring social science perspectives (economics, information systems, politics, psychology, sociology and others) into the study of how accounting systems are designed, run and validated, and size the finance content to the course type.",
  ben="You will study how accounting systems affect, and are affected by, people, organisations, technology, markets, society and the environment, and your course should draw on ideas from economics, politics, sociology and other social sciences to help you.",
  q="Which social science lens has most changed how you think about an accounting system?")
prov('1.8', type='requirement', force='threshold', verbs=['meet'], about='technical, non-critical content at the expense of breadth',
  para="Pressures from employers, professional bodies, regulators and others can push courses towards technical, uncritical accounting; a degree that does so at the cost of the broader intellectual, social and environmental needs the statement sets out falls short of it.",
  prac="Check the design against accreditation pull: a course that trades the broader intellectual, social and environmental content for narrow technical material does not satisfy this statement, whatever exemptions it earns.",
  q="If an accrediting body's syllabus were removed, what broader content would remain in the course?")
both('1.9', verbs=['prepare', 'deal'], about='preparing for a changing profession',
  para="An Accounting degree should ready students for a future in which standards and practice may change radically within a career, so a mainly technical degree is not enough; alongside current regulation and standards it should build lifelong, self-directed learning and professional, transferable and critical skills.",
  prac="Do not build the course around today's technical rules alone: they will change within your graduates' careers. Teach current frameworks, and build self-directed learning and professional, transferable and critical skills that keep graduates employable long term.",
  ben="Your course should prepare you for a profession whose rules and practices may change a great deal during your career, so it should help you keep learning on your own and build professional, transferable and critical skills, not only today's techniques.",
  q="What will you do when a standard you learned is replaced five years after you graduate?")
both('1.11', verbs=['prepare', 'understand', 'interrogate', 'analyse', 'evaluate'], domain='subject-skill', about='systems that provide data and information',
  para="An Accounting degree should prepare students to understand how systems that provide data and information are designed and run: traditional double-entry bookkeeping and the preparation of statements, wider business systems for non-financial and further financial data (for sustainability, social reporting and compliance), and the analysis and evaluation of structured and unstructured data and the structures that hold it.",
  prac="Cover both the traditional accounting process (double entry, statement preparation) and wider business and data systems, including databases and ERP, so that students can question, analyse and evaluate structured and unstructured data for sustainability, social and compliance reporting.",
  ben="Your course should help you understand how accounting and wider business systems produce data and information, from double-entry bookkeeping to databases and ERP systems, and help you question, analyse and judge both tidy and messy data.",
  q="Can you explain how a transaction travels from a source document to a set of statements, and where non-financial data would sit?")
both('1.13', verbs=['enable', 'develop', 'imagine', 'prepare'], domain='understanding', about='critique of the status quo and other futures for accounting',
  para="Courses need to give students the knowledge, skills and confidence to criticise current accounting, to propose other ways of accounting and organising business in the public interest, and to imagine futures for accounting, sustainability accounting among them; they should not be confined to accounting as it now stands.",
  prac="Plan for critique and imagination: students should question mainstream accounting, consider alternatives in the public interest and the common good, and envisage different futures, with sustainability accounting a central case.",
  ben="Your course should give you the confidence to question accounting as it is done today, to suggest other ways of doing it for the public good and to imagine how it could change, for example in accounting for sustainability.",
  q="What is one accounting practice you think should change, and what would you put in its place?")
prov('1.14', type='requirement', force='threshold', verbs=['meet', 'neglects'], about='conceptual and applied study as a minimum',
  para="Accounting is studied in both its conceptual and its applied aspects, conceptual covering accounting theory and broad social, sustainability, political and economic questions; a degree lacking substantial conceptual study does not reach the minimum, and nor does one that wholly leaves out the applied and technical side.",
  prac="Both halves are a floor, not an option: substantial conceptual study (theory and its social, sustainability, political and economic context) and real applied and technical study. A course missing either does not reach the minimum this statement sets.",
  q="Where does the conceptual strand sit in each year, and could a student avoid it?")
prov('1.15', level='fheq:6', award='degree apprenticeship', appliesTo='Accounting degree apprenticeships', verbs=['judged'],
  about='degree apprenticeships judged the same way',
  para="Apprenticeship degrees should be measured against the same criteria as other Accounting degrees.",
  prac="Hold an Accounting degree apprenticeship to the same expectations as the full-time degree: the work-based route does not lower or narrow them.",
  q="Where would the apprenticeship design differ from the full-time degree, and does any difference narrow the content?")
_m16 = _items(['a Advanced or specialist', 'b Accounting conversion', 'c Professional master', 'd Research master'], '\n1.17', 18768)
s('1.16.b1', find=_m16[0][0], after=_m16[0][1], type='expectation', rung='none', force='describes', level='fheq:7', award=ADV,
  appliesTo='graduates of an advanced or specialist academic master\'s', addressee='learner', verbs=['demonstrate'], domain='knowledge',
  about='the advanced or specialist academic master\'s',
  para="Advanced or specialist master's degrees study one or more main parts of an honours Accounting degree at an advanced theoretical level, sometimes with specialist subjects; their graduates are expected to reach honours-level attainment in those areas, meet extra content needs of the specialism and show independent, self-directed inquiry; entry normally needs a good honours degree mainly or jointly in Accounting.",
  prac="For an advanced or specialist master's, expect honours-level attainment in the areas studied, the extra content the specialism needs and independent, self-directed inquiry; plan for entrants with a good Accounting honours degree.",
  ben="On an advanced or specialist master's in Accounting you are expected to reach at least honours-level attainment in your areas, master the extra content of your specialism and carry out independent inquiry of your own.",
  q="Which part of your honours study does this master's take further, and what will your own inquiry be?")
s('1.16.b2', find=_m16[1][0], after=_m16[1][1], type='expectation', rung='none', force='should', level='fheq:7', award=CONV,
  appliesTo='Accounting conversion master\'s courses', addressee='both', verbs=['secure', 'develop', 'informed', 'demonstrate'], domain='knowledge',
  about='the Accounting conversion master\'s',
  para="Conversion master's degrees let students from other disciplines, or who met accounting in another jurisdiction, gain the essentials of an Accounting honours degree and go further at master's level; they should normally be guided by the standards for a good honours degree, with added master's expectations and independent inquiry; entry normally needs a good honours degree in another subject or equivalent experience.",
  prac="Design a conversion master's from the good-honours expectations upward: secure the core knowledge, understanding and skills of an Accounting honours degree, then extend some topics to master's level and require independent, self-directed inquiry.",
  ben="On a conversion master's you should gain the core of what an Accounting honours graduate knows and can do, then take some topics further and complete an independent inquiry of your own.",
  q="Which core areas of accounting were new to you, and which have you taken beyond the honours level?")
s('1.16.b3', find=_m16[2][0], after=_m16[2][1], type='expectation', rung='none', force='will', level='fheq:7', award=PROF,
  appliesTo='professional master\'s courses in Accounting', addressee='both', verbs=['involve', 'reach', 'extend', 'demonstrate'], domain='subject-skill',
  about='the professional master\'s in Accounting',
  para="Professional master's degrees give professional-level knowledge, skills and critical thinking, with ethical judgement and scepticism in applied settings, for students seeking accreditation and exemptions; they will involve advanced study of main parts of an honours degree focused on high-level application, and their graduates are expected to reach and then extend honours-level attainment and show independent inquiry.",
  prac="A professional master's will study main areas of the honours degree at an advanced level with a strong focus on application, judgement and scepticism; expect graduates to go beyond honours attainment in professional content and to complete independent, self-directed inquiry.",
  ben="On a professional master's you will study key areas of accounting at an advanced level with a strong focus on applying them, and you are expected to go beyond honours level and carry out an independent inquiry of your own.",
  q="How does your independent inquiry connect to the professional work you want to do?")
s('1.17', type='expectation', rung='none', force='should', level='fheq:7', award=MAS, appliesTo="taught master's courses in Accounting",
  addressee='both', verbs=['include'], domain='subject-skill', about="self-directed research-based study at master's level",
  para="Every master's in Accounting should include a substantial piece of self-directed, research-based study, a personal inquiry into theory or into applying theory to a real project or issue, inside organisations or beyond them.",
  prac="Build a substantial self-directed, research-based component into every master's: a personal inquiry into a theoretical question or the application of theory to a real organisational, environmental, work or social issue.",
  ben="Your master's should include a substantial inquiry that you direct yourself, into a theoretical question or into using theory on a real issue inside or outside an organisation.",
  q="What real question or theoretical puzzle would sustain your own inquiry for several months?")
s('1.18', type='expectation', rung='none', force='describes', level='fheq:7', award=INT, appliesTo="integrated master's degrees in Accounting",
  addressee='both', verbs=['include', 'take'], domain='knowledge', about="the integrated master's in Accounting",
  para="Integrated master's degrees usually add a year to the honours degree and are expected to reach the standards for a good honours degree and then those of an advanced or specialist master's, or in some jurisdictions a professional master's, including substantial self-directed research-based inquiry.",
  prac="Plan the integrated master's as good-honours attainment plus a further year that reaches the advanced or specialist (or professional) master's expectations, with a substantial self-directed inquiry.",
  ben="On an integrated master's you are expected to reach a good honours standard and then go on to master's-level work in the final year, including a substantial inquiry of your own.",
  q="What changes in your final year that makes the work master's level rather than more honours study?")

# equality, diversity and inclusion
prov('1.19', verbs=['embedded'], about='EDI built into the discipline and every course',
  para="EDI spans many identity characteristics and forms of difference, beyond legal equality duties and including intersections across students and staff; it should be built meaningfully into the culture and practice of accounting and into every Accounting degree.",
  prac="Embed equality, diversity and inclusion in the culture of the department and in every course, attending to intersecting identities among students and staff, not only to legal duties.",
  q="Where would a student see EDI in the content of a core module, not only in policy?")
prov('1.20', verbs=['draw', 'adopted'], about='principles for an inclusive learning community',
  para="To create an inclusive learning community, providers should draw on established principles and guidance for embedding EDI in the curriculum (enabling potential, belonging, awareness, appreciation of other views, self-reflection), with a conscious, proactive approach in environment, content and teaching.",
  prac="Use published principles for embedding EDI (enabling potential, belonging, awareness, respect for other perspectives, self-reflection) and act on them deliberately in the learning environment, content and teaching strategy.",
  q="Which of these principles shows most clearly in your current teaching, and which least?")
both('1.21', verbs=['designed', 'provide', 'embed'], domain='understanding', about='EDI in the curriculum and in reporting',
  para="Through EDI, accounting education can help organisations tackle inequality (the SDGs on gender equality, decent work, reduced inequalities and strong institutions); the curriculum should build in EDI and continued reflection so students can thrive in a diverse world and act inclusively at work, and should give them an understanding of how reporting and record keeping can address these issues and the means and will to apply EDI in practice.",
  prac="Design EDI into the curriculum with reflective practice, and teach how reporting and record keeping can help address inequality, so that students leave with both the understanding and the tools to act inclusively at work.",
  ben="Your course should help you understand how reporting and record keeping can help tackle inequality, and give you the reflective habits and tools to work inclusively in your career.",
  q="How could an organisation's reports make an inequality visible, or hide it?")
both('1.22', verbs=['equip', 'ensure', 'explore'], domain='understanding', about='diverse content and critique of dominant approaches',
  para="Courses should equip students to build diverse, inclusive workplaces and to see accounting's role in global challenges such as poverty, injustice and inequality; content should be diverse and should examine dominant approaches critically, drawing on perspectives from the Global South, marginalised and local communities, with examples that reflect the cohort and society.",
  prac="Diversify the content: examine dominant approaches critically, show how they can exclude, bring in voices from the Global South and marginalised and local communities, and use cases that reflect your students and wider society.",
  ben="Your course should help you see accounting's part in global problems such as poverty and inequality, question the usual ways of doing it and learn from a wide range of voices and places.",
  q="Whose perspective is missing from the cases you have studied so far?")
prov('1.25', verbs=['designed', 'realise'], about='inclusive design for all backgrounds',
  para="Courses should be designed so that students of every background can reach their potential and feel represented and included whatever their characteristics; learning, teaching and assessment should be inclusive, using varied modes and a broad range of assessment types, with alternatives where needed.",
  prac="Design every part, from mode of study to assessment type, so that students of all backgrounds can succeed and feel represented; offer alternative assessments where they remove disadvantage.",
  q="Which assessment in the course most risks disadvantaging a particular group, and what is the alternative?")
prov('1.28', verbs=['reflect'], about='monitoring and reviewing EDI',
  para="EDI in a course needs continuous monitoring and review, and programme teams should regularly consider how well EDI policies are working and how to improve them, with students as partners where they can.",
  prac="Review EDI in the course regularly, ask how well policies have been put into practice and how to improve them, and involve students in that review.",
  q="When did the team last review how EDI policy shows in practice, and were students part of it?")
# accessibility
prov('1.29', verbs=['anticipate', 'thrive'], about='widening access and anticipating needs',
  para="Courses should commit to widening access and inclusive participation so every student can thrive whatever their background, disability or health; providers should anticipate needs and take responsibility for inclusive learning, teaching and assessment, and with support services will make reasonable adjustments proactively.",
  prac="Anticipate disabled students' needs rather than waiting for requests: take responsibility for inclusive learning, teaching and assessment and work with support services to make reasonable adjustments in advance.",
  q="Which reasonable adjustments could be built into the default design so that no one has to ask?")
_s30 = _NORM[_SK['components'][[c['number'] for c in _SK['components']].index('1.30')]['stemSpan']['start']:_SK['components'][[c['number'] for c in _SK['components']].index('1.30')]['stemSpan']['end']].rstrip()
prov('1.30', find=_s30, after=33695, verbs=['meet', 'apply'], about='meeting accessibility requirements at every stage',
  para="On accessibility, providers should at the least meet the regulatory requirements, which run from pre-application information to graduation and after; the paragraph then lists practices that may help.",
  prac="Treat the legal accessibility requirements as the minimum across the whole student journey, from information before application to graduation and beyond.",
  q="Where in the student journey, before arrival or after graduation, is accessibility least checked?")
prov('1.31', verbs=['taken', 'respond'], about='proactive inclusive design and attainment gaps',
  para="Learning, teaching and assessment should be designed proactively, including looking into possible attainment gaps, so that inclusivity and flexibility are built in for diverse needs.",
  prac="Investigate attainment gaps and use what you find to build inclusivity and flexibility into teaching and assessment from the start.",
  q="What does the course's attainment data show, and what design change has it prompted?")
prov('1.32', verbs=['aim', 'provide'], about='equal access to placements, study abroad and activities',
  para="Where relevant, accessibility should aim to give all students the same or similar chances of workplace and international learning and of extra-curricular and co-curricular activity.",
  prac="Check that placements, study abroad and extra- and co-curricular activities are open on equal terms to disabled students and others with protected characteristics.",
  q="Could every student in the cohort take up the placement or study abroad option as it is set up now?")
# education for sustainable development
prov('1.33', verbs=['address'], about='sustainability in its broadest sense',
  para="Courses should address sustainability in line with current thinking such as the United Nations', taking sustainable development in its widest sense of welfare and social, environmental and political perspectives, which is wider than ESG disclosure.",
  prac="Treat sustainability broadly, as welfare and social, environmental and political concerns in line with current UN thinking, not only as ESG disclosure.",
  q="Where does the course go beyond ESG reporting in its treatment of sustainability?")
both('1.34', verbs=['provide', 'apply', 'develop'], domain='subject-skill', about='accounting for a sustainable transition',
  para="A degree should give students the capacity to use traditional and emerging accounting practices to support the move to a more sustainable and fairer world, as framed by the SDGs and PRME; to that end it should develop their technical, critical and transferable skills, higher-order thinking, ethics and forward-looking mindsets for steering organisations towards sustainable outcomes.",
  prac="Develop students' ability to apply established and emerging accounting practices to a sustainable, fairer transition, with the technical, critical, transferable, ethical and anticipatory capacities to steer organisations towards sustainable outcomes.",
  ben="Your course should help you use both established and new accounting practices to support a fairer and more sustainable world, and build the skills, ethics and forward thinking to help organisations get there.",
  q="Which accounting practice could you use to help an organisation measure its progress towards a sustainable goal?")
both('1.35', verbs=['exemplify'], domain='understanding', about='accounting as a catalyst for sustainable change',
  para="Courses should show accounting and accountants as leaders of change: making sustainability visible, deciding how organisations' impacts are counted and reported, building in double materiality, valuing assets, increasing transparency and engaging diverse stakeholders.",
  prac="Show students accounting as a driver of change, through cases on making sustainability visible, double materiality, valuation, transparency and stakeholder engagement.",
  ben="Your course should show you how accountants can lead change, for example by making sustainability issues visible, deciding how impacts are counted and reported, and making organisations more transparent.",
  q="Can you give an example where the way something was counted changed how an organisation behaved?")
s('1.36', type='expectation', rung='none', force='should', level='none', award='none', appliesTo='graduates of the subject', addressee='learner',
  verbs=['evaluate'], domain='knowledge', about='accounting theories and practices for sustainable development',
  para="Graduates should know and understand theories and practices of accounting, assurance and accountability that can help achieve sustainable development, and be able to evaluate critically how these or other approaches can lead to more sustainable results.",
  prac="Graduates should know the accounting, assurance and accountability theories and practices relevant to sustainable development and be able to judge critically which approaches produce more sustainable outcomes.",
  ben="You should know the accounting, assurance and accountability ideas and practices that can support sustainable development, and be able to judge critically which ones work better.",
  q="Which assurance practice do you think does most to make sustainability claims trustworthy, and why?")
s('1.38', type='expectation', rung='none', force='should', level='fheq:6', award=HON, appliesTo='graduates of the subject', addressee='learner',
  verbs=['drive', 'lead'], domain='generic-skill', about='leading the sustainability agenda',
  para="Graduates should be capable of driving and leading the sustainability agenda for business and society, above all on the ethics, responsibility and sustainability expectations of accounting accrediting bodies and on EDI, and in growing sustainable entrepreneurial mindsets.",
  prac="Graduates should be able to take a lead on sustainability in organisations and society, meeting accrediting bodies' ethics and sustainability expectations and EDI responsibilities, with an entrepreneurial outlook.",
  ben="You should be able to take the lead on sustainability in organisations and society, acting on the ethical and sustainability expectations of the profession and on equality and inclusion.",
  q="Where have you led, or could you lead, a change towards more sustainable practice?")
both('1.39', verbs=['designed', 'equip', 'support', 'consider'], domain='understanding', about='accounting as a performative social practice',
  para="Courses should be designed to prepare students to help organisations and society move to a more sustainable future, and should treat accounting and accountants as part of changing social, economic, organisational and political practices that bring about real change by making the consequences of decisions transparent.",
  prac="Prepare students to support organisations' sustainability transitions, and teach accounting as a practice that changes what happens by making the consequences of decisions visible.",
  ben="Your course should prepare you to help organisations move towards a sustainable future and show you how accounting changes what happens by making the results of decisions visible.",
  q="How can reporting a number change the decision that produced it?")
prov('1.40', verbs=['reflect'], about='current sustainability priorities in content',
  para="Courses should reflect current and emerging sustainability priorities that are reshaping accounting and assurance, such as net zero, regenerative business models, modern slavery, carbon and greenhouse gas management, plastics and waste, water, sustainable supply chains and new reporting and assurance standards.",
  prac="Keep the content current with sustainability priorities that are changing practice: net zero, carbon and greenhouse gas management, modern slavery, waste and water, supply chains and new sustainability reporting and assurance standards.",
  q="Which of these priorities is absent from the current modules?")
both('1.41', verbs=['prepare', 'understand', 'develop', 'design', 'analyse', 'transform', 'manage'], domain='subject-skill', about='sustainability data in information systems',
  para="A degree should prepare students to understand how information systems can embed sustainability throughout accounting and organisational systems and develop their skill in designing, analysing, transforming and managing sustainability data, including how it sits in data structures and ERP systems and how unstructured data can serve sustainability ends.",
  prac="Teach how sustainability data is built into accounting and organisational systems, including ERP and other data structures, and give students practice in designing, analysing, transforming and managing that data, structured and unstructured.",
  ben="Your course should help you understand how sustainability data is captured in accounting and business systems and build your skill in designing, analysing and managing that data.",
  q="Where would a firm's carbon data live in its systems, and who checks it?")
both('1.42', level='fheq:6', award=HON, verbs=['highlight'], domain='generic-skill', about='critical enquiry on planetary limits',
  para="Courses should stress critical enquiry into planetary boundaries and what sustainability means for growth, well-being and political stability, with students building critical thinking, self-awareness, confidence to raise issues, collaboration, anticipatory and systemic thinking and sound measurement, valuation and communication as a base for further study and lifelong learning.",
  prac="Make critical enquiry into planetary limits central, and through it develop critical, systemic, strategic and anticipatory thinking, self-awareness, collaboration, the confidence to raise issues and skill in measuring, valuing and communicating.",
  ben="Your course should push you to question how sustainability limits affect growth, well-being and politics, and help you think critically and systemically, work with others and speak up about issues.",
  q="When did you last raise an issue that others would rather not hear, and how did you frame it?")
prov('1.43', verbs=['integrate', 'mainstream'], about='sustainability throughout the curriculum',
  para="Courses should weave economic, social and environmental sustainability through the whole curriculum, adding specialist modules on topics such as climate change or biodiversity where suitable.",
  prac="Integrate sustainability across all modules first; add specialist modules (on climate or biodiversity, for example) as a complement, not a substitute.",
  q="If the specialist sustainability module were removed, how much sustainability would remain?")
# employability, enterprise and entrepreneurship
both('1.44', level='fheq:6', award=HON, verbs=['include', 'develop', 'navigate'], domain='generic-skill', about='enterprise and entrepreneurship education',
  para="Enterprise education develops the capacity to generate ideas and the behaviours to realise them, and entrepreneurship applies them to create cultural, social or economic value; including both improves employability, and courses should include them to produce enterprising, flexible and innovative graduates who can handle a changing workplace with confidence and creativity.",
  prac="Include enterprise and entrepreneurship so that students learn to generate ideas and act on them, and leave enterprising, adaptable and innovative enough to handle a changing workplace.",
  ben="Your course should help you come up with ideas and make them happen, so that you can work with confidence, flexibility and creativity in a fast-changing workplace.",
  q="What idea have you taken from a first thought to something real, and what did it take?")
both('1.45', level='fheq:6', award=HON, verbs=['develop', 'generate', 'implement', 'contribute'], domain='generic-skill', about='critical thinkers who can act on ideas',
  para="Courses should make students critical thinkers who can generate and carry out new ideas, to be entrepreneurial (self-employment included) and employable in any sector; enterprise education should add to their cultural, social and economic values and fit them for lifelong learning, a self-directed career and many career paths.",
  prac="Develop critical thinking as the base for generating and carrying out ideas, whether in self-employment or in any sector, and link enterprise education to students' values and lifelong learning.",
  ben="Your course should help you think critically and turn ideas into action, whether you work for yourself or for others, and prepare you to keep learning across many possible careers.",
  q="Which career paths are you keeping open, and what would you need to learn for each?")
both('1.46', level='fheq:6', award=HON, verbs=['develop', 'used'], domain='generic-skill', about='enterprise skills through the core content',
  para="Covering the core principles of the subject should develop enterprise-related skills and attributes, and research-led and research-informed teaching should be used to grow open-mindedness, proactivity, determination, resilience and self-efficacy; enterprise skills should also come through seeing that knowing alternative accounting options supports negotiation, creative problem-solving, judgement, leadership, commercial awareness and business acumen.",
  prac="Use research-led teaching and the subject's core principles to build open-mindedness, proactivity, resilience and self-efficacy, and show how knowing alternative accounting treatments strengthens negotiation, problem-solving, judgement and commercial sense.",
  ben="Your course should help you become open-minded, proactive and resilient, and show you how knowing different accounting options helps you negotiate, solve problems and make sound business judgements.",
  q="When has knowing a second way to account for something helped you argue a case?")
# generative AI
both('1.51', verbs=['include', 'build', 'develop', 'adapt'], domain='subject-skill', about='GenAI in accounting practice',
  para="Courses should cover how GenAI is used in accounting practice, build students' skill with suitable professional GenAI tools and develop critical thinking about the limits and implications of those tools; since AI is already common in practice software, analytics and audit planning, degrees need to keep adapting.",
  prac="Teach where GenAI is used in accounting work, give students hands-on practice with suitable professional tools, and develop their critical view of the tools' limits; review the content often as practice changes.",
  ben="Your course should show you how GenAI is used in accounting work, give you practice with suitable tools and help you think critically about what those tools cannot do.",
  q="Where would you not trust a GenAI tool's output in an audit or tax task, and how would you check it?")
both('1.52', verbs=['develop', 'mitigated'], domain='understanding', about='bias in AI systems',
  para="Because AI learns from existing text and decisions it can spread bias (by gender, race, class or capitalist logic) unless controlled, and the control can itself be biased; providers need to know this, and courses should develop students' understanding of bias and discrimination in AI and how to reduce them.",
  prac="Teach how AI systems can reproduce bias and discrimination, and how that can be reduced; be alert to the same risk in the tools the course itself uses.",
  ben="Your course should help you understand how AI systems can repeat bias and discrimination and what can be done to reduce it.",
  q="How could an AI tool used in credit or audit decisions treat some groups unfairly?")
both('1.53', verbs=['designed', 'include', 'learn', 'link'], about='GenAI in learning and teaching',
  para="Courses should use GenAI to support learning, for example to make teaching more interactive, to provide AI-written answers for students to critique and compare with their own writing, and to support dialogic and experiential learning; students should learn to use technology with integrity, linked to the profession's ethics.",
  prac="Use GenAI for learning on purpose: interactive teaching, critiquing AI-written answers, comparison with students' own work for inner feedback; teach integrity in its use and connect it to professional ethics.",
  ben="Your course should use GenAI to help you learn, for example by asking you to critique AI-written answers and compare them with your own, and help you use such tools honestly and ethically.",
  q="What did comparing your answer with an AI-written one teach you about your own work?")
prov('1.54', verbs=['take', 'design', 'considered'], about='assessment design in the age of GenAI',
  para="GenAI makes it essential to rethink assessment: it can move assessment away from rote and multiple-choice formats towards critical, authentic, case-based and experiential tasks, including assessment of students' grasp of AI in accounting; these points should be weighed in formative and summative assessment alike.",
  prac="Redesign assessment for GenAI: move away from rote and objective formats towards authentic cases, dynamic scenarios and experiential tasks, assess understanding of AI in accounting, and apply this to formative and summative work.",
  q="Which current assessment could a GenAI tool complete unaided, and how would you redesign it?")
prov('1.55', verbs=['employ', 'ensure', 'communicated'], about='academic integrity and GenAI policies',
  para="Providers are responsible for due diligence to keep assessment rigorous and honest despite GenAI: clear, consistently applied integrity and GenAI-aware quality policies, awareness of misuse by students and staff, continuous review, since detection is unreliable, and policies communicated to everyone involved.",
  prac="Put GenAI-aware integrity policies in place, apply them consistently, review them continuously because detection is unreliable, and make sure students and staff know them.",
  q="How are students told what use of GenAI is acceptable in each assessment?")

# =============================================================== section 2: distinctive features
both('2.1', verbs=['designed', 'develop', 'equip', 'understand', 'enable'], domain='understanding', about='design aims of an Accounting degree',
  para="Courses should be designed so students can build a broad, rigorous understanding of accounting in its social and economic setting, make sound and creative judgements on complex problems, understand accounting across kinds of organisation and stakeholder and in issues such as sustainability, EDI and accessibility, and become responsible, ethical citizens.",
  prac="Design for breadth and rigour: accounting in context, sound and creative judgement on complex problems, many kinds of organisation and stakeholder, sustainability, EDI and accessibility, and ethical citizenship.",
  ben="Your course should be designed to give you a broad, rigorous understanding of accounting in society, the ability to make sound judgements on complex problems and the grounding to act as a responsible, ethical citizen.",
  q="Which complex problem have you had to judge without a clear right answer?")
prov('2.2', verbs=['designed', 'include', 'structured', 'integrate'], about='learning objectives aligned to the statement',
  para="Courses should set learning objectives in line with section 3's knowledge, understanding and skills and with sound learning, teaching and assessment principles; institutional structures should shape but not overly limit the design; objectives should join the conceptual and applied and link areas of knowledge, with room to adapt to change in the subject and to technology such as GenAI.",
  prac="Write programme objectives that map to the knowledge, understanding and skills in section 3, join conceptual and applied study and connect areas, and keep the design flexible enough to adapt to new technology.",
  q="Can you show each section 3 area against a programme objective and a module where it is assessed?")
both('2.3', level='fheq:6', award=HON, verbs=['designed', 'develop', 'prepare'], domain='generic-skill', about='higher-order thinking and lifelong learning',
  para="Courses should be designed so students develop the higher-order intellectual skills needed in a changing, increasingly automated society and workplace, and a degree should prepare them for lifelong, self-directed learning.",
  prac="Give priority to higher-order thinking (analysis, evaluation, creativity) over routine tasks that automation will absorb, and build habits of self-directed, lifelong learning.",
  ben="Your course should develop your higher-level thinking, such as analysis, evaluation and creativity, for a workplace where routine tasks are increasingly automated, and prepare you to keep learning on your own.",
  q="Which part of your current work could be automated, and what thinking would still be yours?")
both('2.4', verbs=['designed', 'enable', 'thrive'], about='preparing for many careers',
  para="Courses should be designed so students can succeed in a range of careers, entrepreneurial ventures or academic paths.",
  prac="Keep career routes open: design for employment in many sectors, for entrepreneurship and for academic study, not only for professional accountancy.",
  ben="Your course should prepare you to do well in many kinds of career, in starting something of your own or in further academic study.",
  q="Which route are you leaning towards, and what in the course is preparing you for it?")
prov('2.5', verbs=['designed', 'meet'], about='accreditation not at the expense of breadth',
  para="Many students hope to qualify professionally, but courses should take account of students' wider and changing aims and should not be designed to win PSRB exemptions and accreditation at the cost of the broader aims of section 3.",
  prac="Seek accreditation where it helps students, but do not let exemption requirements drive out the broader design aims; plan for students whose career aims change.",
  q="What would change in the design if accreditation were not a consideration?")
prov('2.6', level='fheq:6', award=HON, appliesTo='joint degrees that include Accounting', verbs=['designed', 'ensure', 'include'],
  about='coverage in joint degrees',
  para="Joint degrees with Accounting should be designed to include most of the statement's knowledge, understanding and skills, with a balance that still keeps conceptual issues, theory, accountability, sustainability, non-business uses, application and higher-order thinking.",
  prac="In a joint degree, cover most of the statement's knowledge and skills and keep the balance from squeezing out conceptual, accountability, sustainability and higher-order content.",
  q="Which areas of section 3 does the joint design leave out, and is that a majority or a minority?")
prov('2.10', force='will', level='fheq:6', award=HON, appliesTo='combined or joint honours with Accounting', verbs=['designed', 'satisfy'],
  about='progression rules in joint honours',
  para="In combined or joint honours, progression requirements will be designed to meet the progression needs of both subjects.",
  prac="Set progression rules for a joint or combined honours route that satisfy both subjects' needs, not only the larger one.",
  q="Can a joint honours student progress without the Accounting prerequisites the next level depends on?")
prov('2.11', verbs=['designed', 'allow', 'reach'], about='progression that allows for individual needs',
  para="Progression should allow for each student's needs and, where it is relevant and feasible, permit reasonable adjustments, so that every student can reach their potential.",
  prac="Build flexibility for individual needs into progression rules, including reasonable adjustments where possible.",
  q="Where do the progression regulations leave no room for an adjustment?")
both('2.12', level='fheq:6', award=HON, verbs=['provide', 'pursuing'], about='honours as a basis for qualification and careers',
  para="An honours degree in Accounting should give a sound base for a professional qualification or other careers, especially in business or finance.",
  prac="Make sure the honours degree gives a sound foundation for professional qualification and for other careers, notably in business and finance.",
  ben="Your honours degree should give you a sound start towards a professional qualification or another career, especially in business or finance.",
  q="Which professional qualification or career are you aiming at, and which parts of the degree count towards it?")
s('2.13', type='expectation', rung='none', force='should', level='fheq:6', award=HON, appliesTo='honours graduates with a second-class degree or higher',
  addressee='learner', verbs=['equipped', 'undertake'], domain='none', about='readiness for postgraduate study',
  para="A student with at least a second-class degree should be ready for postgraduate study in Accounting or a related subject, though entry is for each provider to set; the same principles normally govern progression to the master's year of an integrated master's.",
  prac="Graduates with a second-class degree or better should be ready for postgraduate study in the subject; admissions decisions remain each institution's, and the same principles apply to entering an integrated master's final year.",
  ben="If you gain a second-class degree or higher, you should be ready for postgraduate study in Accounting or a related subject, though each institution sets its own entry rules.",
  q="Is postgraduate study part of your plan, and what class of degree does your target course ask for?")
both('2.14', force='will', level='fheq:6', award='degree apprenticeship', appliesTo='degree apprentices in Accounting', verbs=['apply', 'pass'],
  about='progression on degree apprenticeships',
  para="Similar progression standards will apply to degree apprentices at honours level (FHEQ 6, FQHEIS 10), and apprentices may also need to pass an end-point assessment.",
  prac="Apply the same progression standards to degree apprentices as to other students, and plan for the end-point assessment the apprenticeship may require.",
  ben="As a degree apprentice, the same progression standards will apply to you, and you may also need to pass an end-point assessment to complete the apprenticeship.",
  q="Do you know what your end-point assessment involves and when it falls?")
# flexibility
prov('2.16', verbs=['respond', 'anticipate', 'address'], about='adaptable and flexible courses',
  para="Courses need to adapt to, and anticipate, advances in the subject and related fields and the needs of graduates and employers, and should be flexible enough to serve learners, the profession, wider stakeholders and external bodies' requirements.",
  prac="Review and adapt the course as the subject and employers' needs change, and keep it flexible enough to meet learners', the profession's and external bodies' needs.",
  q="What changed in the course after the last major development in the profession?")
prov('2.17', verbs=['designed', 'offered', 'achieve'], about='inclusive flexibility of mode and length',
  para="Courses should be planned with inclusion in mind and may vary learning mode and assessment to suit students; flexibility can come from length (a placement or study abroad year), mode (full or part-time, in person or distance), entry criteria and assessment.",
  prac="Design for inclusivity through options in length, mode, entry criteria and assessment, such as placement years, part-time and distance study.",
  q="Which mode or length option would most widen who can study the course?")
# partnership
prov('2.23', verbs=['applied', 'ensure', 'met', 'designed'], about='standards across partnership delivery',
  para="Degree-awarding bodies may deliver with partners; the statement should be applied so the standards are met across the whole partnership course, and courses designed with partners should not be built for PSRB exemption and accreditation at the cost of the broader aims.",
  prac="Apply the statement across the whole of a partnership course so that the standards hold everywhere, and do not let a partner's accreditation aims narrow the design.",
  q="How do you check that the standards are met in the partner's delivery, not only in your own?")
prov('2.26', verbs=['meet', 'designed', 'reflect'], about='PSRBs as partners, not prescribers',
  para="PSRBs, above all the professional accountancy bodies, can be important partners in design and courses may reflect their recognition requirements, but every Accounting degree should meet this statement's standards rather than have its content set by PSRB accreditation.",
  prac="Work with professional bodies, but measure the course against this statement's standards first; accreditation requirements do not replace them.",
  q="Where does an accreditation requirement now set content that the statement would weigh differently?")
# monitoring and review
prov('2.28', verbs=['draw', 'ensure', 'aligns'], about='external reference points in review',
  para="Monitoring and regular review are central to quality; degree-awarding bodies should use a range of external reference points, relevant subject statements among them, to keep provision in line with sector norms, through annual and periodic review with external input.",
  prac="Use external reference points, this statement included, in annual monitoring and periodic review, with external experts or advisers, to keep the course in line with the sector.",
  q="Which external reference points did the last periodic review use?")
prov('2.31', verbs=['ensure', 'embedded', 'reflected'], about='monitoring the cross-cutting themes',
  para="Monitoring and evaluation should check that sustainable development, EDI, accessibility, enterprise and entrepreneurship and GenAI run through the curriculum and show in learning, teaching and assessment design.",
  prac="Use monitoring and review to check that the five themes are present across the curriculum and in teaching and assessment, not in one module only.",
  q="Where does each of the five themes appear in assessment, not only in content?")
prov('2.32', verbs=['play'], about='the statement in external examining',
  para="External examiners help keep standards consistent across the sector by commenting on assessment, marking, modules and outcomes, and reporting yearly; this statement and others, especially their standards, should have a central place in their evaluation and advice.",
  prac="Ask external examiners to judge the course and its outcomes against this statement's standards, and use their reports in review.",
  q="Did the last examiner's report refer to the subject standards, and what changed as a result?")
prov('2.33', verbs=['provide'], about='informing students about professional routes',
  para="Courses aligned with PSRBs face extra monitoring by those bodies for exemption and accreditation, through visits and desk reviews; providers should tell prospective and current students about their routes to a professional qualification.",
  prac="Give prospective and current students clear information about how the course leads to professional qualification and which exemptions it carries.",
  q="Where can a prospective student find the exemptions the course gives?")

# =============================================================== section 3: content, structure and delivery
prov('3.2', verbs=['reflect', 'shaped'], about='content shaped by section 1 and the themes',
  para="Course content should follow section 1's principles, be shaped mainly by the purposes and characteristics subsection and reflect the cross-cutting themes.",
  prac="Derive the content from section 1's purposes and characteristics and carry the cross-cutting themes into it.",
  q="Which purposes in section 1 have no clear home in the current content?")
both('3.3', verbs=['include', 'encourage', 'build', 'imagine', 'instil'], domain='understanding', about='the public interest role of accounting',
  para="Courses should give real weight to accounting's public interest role and accountability, society's present and future needs and critique of current accounting, encouraging students to imagine other futures; degrees need to instil responsibility and readiness for change, grounded in ethics.",
  prac="Give substantial time to the public interest and accountability, to critique of current accounting and to imagining alternatives, and build an ethical sense of responsibility and anticipation of change.",
  ben="Your course should give real weight to accounting's role in the public interest, encourage you to question how it is done now and help you imagine other ways, with a sense of ethical responsibility.",
  q="Whose interest does a particular accounting rule serve, and whose does it overlook?")
both('3.4', verbs=['foster', 'based', 'reflect'], domain='understanding', about='critical, socially grounded study',
  para="Courses should encourage critical discussion of accounting and accountability in their social and economic setting, rest on social science perspectives, and look past profit and capital to accountability for sustainability, welfare and social, environmental and political concerns.",
  prac="Teach accounting critically and in context, drawing on the social sciences and treating accountability for sustainability, welfare and social concerns as core.",
  ben="Your course should get you discussing accounting critically in its social and economic setting and looking beyond profit to sustainability, welfare and social concerns.",
  q="What would an account of the same organisation look like from a community's point of view rather than an investor's?")
both('3.5', verbs=['based', 'include'], domain='subject-skill', about='accounting across many kinds of organisation',
  para="Courses rest on accounting as a main form of information and control in many organisations (public, charitable, co-operative, social enterprise, campaigning and for-profit) and should include applying accounting knowledge, skills and critique to a range of them.",
  prac="Give students practice in applying accounting knowledge, skills and critique to public, charitable, co-operative, social enterprise and campaigning bodies as well as companies.",
  ben="Your course should give you practice in using and questioning accounting in many kinds of organisation, from charities and public bodies to co-operatives and companies.",
  q="How would the accounts of a charity tell a different story from those of a company of the same size?")
prov('3.6', verbs=['include'], about='conceptual and applied aspects',
  para="Courses should cover both the conceptual and theoretical and the applied sides of accounting.",
  prac="Include both conceptual and theoretical study and applied study in every course.",
  q="What share of assessment credit goes to conceptual and theoretical work?")
both('3.8', verbs=['prepare', 'learn', 'apply', 'guide', 'include'], domain='subject-skill', about='accounting beyond numbers in a complex world',
  para="Courses should not be only about numbers or money, since accounting deals with accountability and much non-financial information; they should prepare students to learn from accounting's history and to apply their knowledge and skills to guide organisations through modern complexity, including sustainability, stakeholder expectations, social and welfare issues and questions with no settled answer.",
  prac="Go beyond financial numbers: teach accounting's history, its non-financial reporting and its role in sustainability, stakeholder expectations and social issues, and give students practice in guiding organisations through ambiguous problems.",
  ben="Your course should show you that accounting is about more than numbers and money, and prepare you to use what you learn to guide organisations through complex social, sustainability and ethical questions.",
  q="What non-financial information would you need to judge how well an organisation is doing?")
both('3.9', verbs=['incorporate', 'understand', 'apply'], domain='subject-skill', about='core accounting-specific skills',
  para="Courses should build in subject-specific skills so students understand accounting knowledge and can apply it in practice, including recording and summarising transactions, preparing financial statements, analysing operations (decisions, performance, control, budgets, discounted cash flow) and financial analysis and projection.",
  prac="Make sure students practise recording and summarising transactions, preparing financial statements, analysing operations (decision analysis, performance measurement, budgeting, discounted cash flow) and analysing ratios, risks and projections.",
  ben="Your course should build your practical accounting skills: recording transactions, preparing financial statements, analysing how a business performs and projecting its finances.",
  q="Could you prepare a set of statements from a trial balance and explain what the ratios show?")
_s310 = _NORM[70689:_NORM.index('a Accountability, responsibility', 70689)].rstrip()
prov('3.10', find=_s310, after=70689, verbs=['include', 'developed', 'recognised'], about='the broad areas of knowledge, integrated',
  para="Courses should cover all of the broad areas listed, in varying combinations and with overlap; each area should include theory, current practice, regulation, current debate and application in complex settings with evidence-based judgement, in local, national and global contexts, developed to rising levels and taught as connected parts of accounting rather than separate silos, with their links to the themes recognised.",
  prac="Cover every listed area, each with theory, practice, regulation, debate and application in local, national and global contexts; teach them as linked parts of accounting, build them up across the years, and show how the themes cut across them.",
  q="Which two areas are most often taught in isolation from each other, and how could they be linked?")
_m310 = _items(['a Accountability, responsibility', 'b Business, social', 'c Ethics:', 'd Organisational governance', 'e Information for effective',
                'f Systems, processes', 'g The regulatory', 'h Audit and assurance:', 'i Taxation:', 'j Uncertainty and risk',
                'k Data analytics and statistics:', 'l Financial markets'], '\n3.11', 70689)
def a310(n, **k):
    t, a = _m310[n - 1]
    d = dict(type='expectation', rung='none', force='should', level='none', award='none', appliesTo='Accounting courses and their students',
             addressee='both')
    d.update(k); s('3.10.b%d' % n, find=t, after=a, **d)
a310(1, verbs=['equip', 'recognise', 'make', 'provide'], domain='understanding', about='area a: accountability, responsibility and trust',
  para="Area a: accounting helps organisations create sustainable value ethically, and accountants carry a duty to communicate openly and reliably to many stakeholders; a course should equip students to see this position of trust, judge well and give assurance, advice and leadership.",
  prac="Teach the position of trust accountants hold and give students practice in judgement, assurance, advice and leadership that honours it.",
  ben="Your course should help you see the trust placed in accountants and build your ability to judge well and to give assurance, advice and leadership.",
  q="What would losing that trust cost a client, and what would it cost the profession?")
a310(2, verbs=['consider', 'demonstrate'], domain='knowledge', about='area b: the business, social and economic environment',
  para="Area b: a course should look at the business, social and economic setting, and graduates should show they know how that environment affects organisations, and organisations it, locally to internationally, across environmental, cultural, ethical, legal, tax, political, social and technological factors.",
  prac="Cover the environment organisations work in and their effect on it, at local, national and international scale, across environmental, cultural, ethical, legal, tax, political, social and digital factors.",
  ben="You should be able to show that you understand how the business, economic and social environment shapes organisations, and how organisations shape it in turn.",
  q="How has a recent legal, technological or environmental change altered the way a firm you know operates?")
a310(3, verbs=['included', 'integrated', 'apply', 'navigate', 'make'], domain='subject-skill', about='area c: ethics',
  para="Area c: ethics means spotting dilemmas, understanding their effects, judging and acting well, for organisations and society and for accounting in particular; both should be taught, woven through the degree so students can apply professional scepticism, handle complex moral situations and decide in the public interest.",
  prac="Weave ethics through the whole degree, general and accounting-specific, so students practise scepticism, work through hard moral cases and decide in the public interest.",
  ben="Ethics should run through your whole course, helping you spot dilemmas, apply professional scepticism and make decisions that serve the public interest.",
  q="Describe a case where the rules allowed something you still judged to be wrong.")
a310(4, verbs=['ensure', 'apply'], domain='knowledge', about='area d: organisational governance and corporate reporting',
  para="Area d: reporting covers preparing, analysing and interpreting all reports to stakeholders, financial and non-financial; a course should make sure graduates can apply the laws, regulations and standards with sound recording skills, know accounting's role in governance (groups included) and know current theory and research so they can judge practice critically.",
  prac="Teach the full range of reports, financial and non-financial, the laws and standards that govern them, recording skills, accounting's governance role and current research, so that graduates can evaluate practice critically.",
  ben="You should be able to apply the laws, regulations and standards for reporting, understand accounting's part in how organisations are governed and use current research to judge reporting practice.",
  q="Which report beyond the financial statements would you read first to judge a company's governance, and why?")
a310(5, verbs=['equip', 'develop', 'implement', 'operate', 'monitor', 'formulate'], domain='subject-skill', about='area e: information for decision-making',
  para="Area e: providing timely, relevant financial and non-financial information for planning, performance, control and strategy, including decision methods, communication to decision-makers and strategic management accounting; a course should equip students to build and run performance measurement systems and KPIs, set and track budgets, apply costing and valuation, solve problems with incomplete or ambiguous data, anticipate risks and use technology and analytics.",
  prac="Give students practice in performance measurement systems and KPIs, budgeting, costing and valuation, communicating to decision-makers and solving problems with incomplete data, using analytics and current technology.",
  ben="Your course should prepare you to design and run performance measures, build and monitor budgets, apply costing and valuation, and make sound recommendations even when the data is incomplete.",
  q="If a key figure in your budget were missing, how would you still reach a recommendation?")
a310(6, verbs=['include', 'understand', 'interrogate', 'analyse'], domain='subject-skill', about='area f: systems, processes and data structures',
  para="Area f: data and its processing are central, so courses need to cover how systems that supply data are designed, run and controlled, both traditional bookkeeping, ledgers and statements and wider systems for non-financial data, with graduates able to question, analyse and work with structured and unstructured data and the structures that hold it.",
  prac="Cover double entry, ledgers and statement production alongside wider data systems, databases and ERP, and give students practice with structured and unstructured data.",
  ben="Your course should help you understand how accounting and wider data systems work, from ledgers to databases, and build your skill in working with both tidy and messy data.",
  q="What controls would you look for in a system before relying on its data?")
a310(7, force='describes', verbs=['understand', 'interpreting', 'applying'], domain='knowledge', about='area g: the regulatory environment',
  para="Area g: the rules and norms governing accounting, the profession and accountable organisations in every sector, which let graduates see why financial system integrity and governance matter, covering governance codes, sustainability reporting rules, tax law and ethics, sustainability reporting and EDI.",
  prac="Teach the regulation of accounting, the profession and organisations in all sectors, including governance codes, sustainability reporting rules and tax law, and how ethics and equality enter regulation.",
  ben="Your course should help you understand the rules that govern accounting and organisations, from governance codes to sustainability reporting and tax law, and why they matter.",
  q="Which regulation affecting accounting has changed most recently, and why was it changed?")
a310(8, verbs=['designed', 'instil', 'prepare', 'deliver', 'foster', 'navigate'], domain='subject-skill', about='area h: audit and assurance',
  para="Area h: courses should give students the knowledge to prepare for, and deliver, good audit and assurance that strengthens trust and transparency in financial and non-financial reporting, centred on scepticism, critical thinking, the public interest and professional judgement, and should firmly promote professional ethics so graduates can handle audit practice and standards confidently.",
  prac="Teach audit and assurance with professional scepticism, critical thinking and public interest responsibility at the centre, for financial and non-financial reporting, and stress professional ethics throughout.",
  ben="Your course should prepare you to carry out good audit and assurance work, with professional scepticism, sound judgement and a clear sense of the public interest.",
  q="What would make you sceptical of a figure a client's finance director assures you is correct?")
a310(9, verbs=['equip', 'navigate', 'champion', 'support', 'foster', 'encompass', 'include'], domain='knowledge', about='area i: taxation',
  para="Area i: it is essential that courses equip students to handle the principles and complexity of tax and its social and economic purposes, the ethics and law of compliance and avoidance, and should promote transparency and the integrity of tax systems; at the least they should cover the main UK taxes, including income tax, National Insurance, capital gains, inheritance, corporation tax and VAT.",
  prac="Cover tax principles, purposes and ethics, the consequences of non-compliance and illicit practice, and at minimum the main UK taxes (income tax, National Insurance, capital gains, inheritance, corporation tax and VAT).",
  ben="Your course should help you understand how tax works and why, the ethics and law around it and, at the least, the main UK taxes such as income tax, National Insurance, corporation tax and VAT.",
  q="Where would you draw the line between legitimate tax planning and aggressive avoidance?")
a310(10, verbs=['prepare', 'navigate', 'ensure', 'differentiate', 'apply', 'advise'], domain='subject-skill', about='area j: uncertainty and risk management',
  para="Area j: courses should prepare graduates for the complexity of organisational settings, with knowledge of risk and uncertainty and how they differ, of protecting assets and compliance, and of management and mitigation, so they can apply techniques such as risk appetite, scenario planning, game theory, decision trees and forecasting and advise on the data to use.",
  prac="Teach the difference between risk and uncertainty and give students practice with risk appetite, scenario planning, decision trees, forecasting and the data those models need.",
  ben="Your course should help you tell risk from uncertainty, use tools such as scenario planning, decision trees and forecasting, and advise on the right data for them.",
  q="Give an example of uncertainty that no probability could capture, and how you would plan for it.")
a310(11, verbs=['include'], domain='subject-skill', about='area k: data analytics and statistics',
  para="Area k: analytics and statistics inform decisions and help in reading research; they allow large datasets to be interpreted, hypotheses tested and anomalies and trends found, with coding, search, AI and machine learning increasingly relevant; courses should include knowledge and applied skill in a range of these, with critical interpretation of results.",
  prac="Give students applied practice in analytics and statistics (hypothesis testing, anomaly detection and trend analysis, with some coding and machine learning), with critical reading of results and of research papers.",
  ben="Your course should give you practical skills in data analytics and statistics, and help you read the results, and the research that uses them, critically.",
  q="What would make you doubt an anomaly that an analytics tool has flagged?")
a310(12, force='will', verbs=['include'], domain='knowledge', about='area l: financial markets and institutions',
  para="Area l: knowledge of financial markets and institutions is essential because accounting is central to how markets work; coverage depends on the degree, but at minimum a course is expected to include the time value of money, sources of finance, capital markets and instruments, project and corporate finance, stock exchanges, asset pricing, alternative, behavioural and personal finance and ethics in finance, with further topics optional.",
  prac="At minimum cover time value of money, sources of corporate finance, capital markets, project and corporate finance, asset pricing, behavioural and personal finance and ethics in finance; add further finance topics to suit the course.",
  ben="Your course will cover the essentials of financial markets and institutions, such as the time value of money, sources of finance, capital markets, asset pricing and ethics in finance.",
  q="How would a change in interest rates move the value of a project you have appraised?")
prov('3.12', verbs=['reflect'], about='skills shaped by section 1',
  para="The skills asked of a student completing the degree should follow the broad principles of section 1.",
  prac="Derive the skills the course develops from section 1's principles.",
  q="Which section 1 principle is least visible in the skills the course assesses?")
s('3.13', type='outcome', rung='none', force='should', level='fheq:6', award=HON, appliesTo='students of the subject', addressee='learner',
  verbs=['develop', 'demonstrate', 'apply', 'operationalise', 'act'], domain='generic-skill', about='skills that put knowledge into action',
  para="Students should develop skills to show, apply and put into practice their knowledge and understanding, technical accounting skills included, to stay alert to context and the themes, and to act ethically.",
  prac="Students should build skills that turn their knowledge into practice, technical skills included, while staying aware of context and the themes and acting ethically.",
  ben="You should develop the skills to show and use what you know in practice, including technical accounting skills, while keeping the wider context in view and acting ethically.",
  q="Where have you had to use what you know in a real or realistic setting, and what did that demand?")
_m315 = _items(['m Communication:', 'n Collaboration:', 'o Self-efficacy', 'p Critical thinking and scepticism:', 'q Problem solving',
                'r Data analysis:', 's Systems thinking:', 't Digital literacy:', 'u Numeracy:', 'v Entrepreneurialism:',
                'w Cultural awareness:', 'x Research:'], 'Learning and teaching\n3.16', 85773)
def k315(n, **k):
    t, a = _m315[n - 1]
    d = dict(type='outcome', rung='none', force='describes', level='fheq:6', award=HON, appliesTo='graduates of the subject',
             addressee='learner', domain='generic-skill')
    d.update(k); s('3.15.b%d' % n, find=t, after=a, **d)
k315(1, verbs=['including'], about='skill m: communication',
  para="Skill m: presenting quantitative and qualitative data, analysis and argument to suit different audiences and stakeholders, in spoken, written, visual and other forms and media.",
  prac="Graduates are expected to communicate data, analysis and argument effectively to different audiences, in speech, writing, visuals and varied media.",
  ben="You are expected to present numbers, analysis and arguments clearly to different audiences, in speech, writing, visuals and other media.",
  q="How would you explain the same result to a board, a regulator and a community group?")
k315(2, verbs=['enable'], about='skill n: collaboration',
  para="Skill n: listening, negotiating, persuading and communicating so as to work across boundaries, influence and collaborate inclusively and lead, including emotionally intelligent teamwork and work with other organisations and stakeholders.",
  prac="Graduates are expected to collaborate inclusively and with emotional intelligence in teams and across organisations, using listening, negotiation and persuasion, and to show leadership.",
  ben="You are expected to work well with others: listening, negotiating, persuading and leading, inclusively and with emotional intelligence, in teams and with other organisations.",
  q="What did you change in how you worked after a team project went badly?")
k315(3, verbs=['including'], about='skill o: self-efficacy and lifelong learning',
  para="Skill o: belief in and ability to act on one's own capacity, with reflection and commitment to independent action, tied to self-managed lifelong learning: owning one's development and the results of one's actions, ethical decisions, resilience and prioritising.",
  prac="Graduates are expected to show self-efficacy: confidence in their own ability, reflection, independent action, ownership of their development, resilience and the ability to prioritise.",
  ben="You are expected to believe in and act on your own ability, reflect on your progress, take charge of your own learning and of the results of your actions, and bounce back from setbacks.",
  q="What is the next thing you need to learn, and how will you go about it without being told to?")
k315(4, verbs=['including'], about='skill p: critical thinking and scepticism',
  para="Skill p: critical and reflective evaluation of evidence, argument, theory and research, including judgement under uncertainty and ambiguity, scepticism as applied critical thinking, the nature of rationality, reflection and an ethical, activist stance.",
  prac="Graduates are expected to evaluate evidence, arguments, theory and research critically, judge under uncertainty, apply scepticism and take an ethical stance.",
  ben="You are expected to weigh evidence, arguments and research critically, make judgements when things are uncertain, apply professional scepticism and take an ethical stand.",
  q="What evidence would change your mind about a conclusion you hold firmly?")
k315(5, verbs=['analysing', 'selecting'], about='skill q: problem solving and reasoning',
  para="Skill q: analysing data and information in structured and messy situations to find a problem's likely causes, weighing alternative actions with ethical reasoning, and choosing ethical and sustainable solutions.",
  prac="Graduates are expected to diagnose problems from data in structured and unstructured situations, compare options with ethical reasoning and choose ethical, sustainable solutions.",
  ben="You are expected to work out the likely causes of a problem from the data, compare possible actions, including their ethics, and choose solutions that are ethical and sustainable.",
  q="What were the other options you rejected for your last recommendation, and why?")
k315(6, verbs=['including', 'consider'], about='skill r: data analysis',
  para="Skill r: identifying, collecting and checking data from referenced sources in varied forms, then filtering, evaluating and interpreting it to reach reasoned conclusions, including for complex real problems with incomplete data and unclear aims, and presenting findings suitably, visualisations included.",
  prac="Graduates are expected to source, verify, filter, evaluate and interpret data, reach reasoned conclusions on messy real problems and present findings to suit the audience, using visualisation where it helps.",
  ben="You are expected to find, check and interpret data from different sources, draw reasoned conclusions even when the data is incomplete, and present what you find in a form your audience can use.",
  q="How did you check the reliability of the data behind your last conclusion?")
k315(7, verbs=['provides', 'includes'], about='skill s: systems thinking',
  para="Skill s: seeing processes as interconnected systems and understanding the structures beneath complex situations, such as accounting and control systems, including analysing, designing, running, communicating, evaluating and improving systems that supply data, and managing risk, error, fraud and cyber threats, resilience, sustainability and assurance.",
  prac="Graduates are expected to think in systems: analyse, design, evaluate and improve the systems that supply data for reporting and decisions, including their controls against error, fraud and cyber risk.",
  ben="You are expected to see how processes connect as systems and to help analyse, design and improve the systems that produce data, including controls against error, fraud and cyber attack.",
  q="If one control in a purchasing system failed, what else in the system would be affected?")
k315(8, verbs=['including', 'use', 'evaluate'], about='skill t: digital literacy',
  para="Skill t: using and evaluating sources and contexts of data, handling and communicating it in all forms, with attention to storage, control and cyber security, and using and assessing current technologies such as spreadsheets, databases and AI as they emerge.",
  prac="Graduates are expected to handle, communicate and secure data in all forms and to use and evaluate spreadsheets, databases, AI and new technologies as they arrive.",
  ben="You are expected to handle and share data in all its forms, keep it secure and use and judge tools such as spreadsheets, databases and AI as new ones appear.",
  q="Which new tool have you learned recently, and how did you judge whether it was reliable?")
k315(9, verbs=['use', 'manipulate', 'evaluate', 'estimate', 'model'], about='skill u: numeracy',
  para="Skill u: applying quantitative skills to work with data and to estimate, evaluate and model business problems, functions and phenomena.",
  prac="Graduates are expected to use quantitative skills to manipulate data and to evaluate, estimate and model business problems.",
  ben="You are expected to use number skills to work with data and to evaluate, estimate and model business problems.",
  q="How would you estimate a figure quickly to check whether a model's output is plausible?")
k315(10, verbs=['including', 'demonstrating'], about='skill v: entrepreneurialism',
  para="Skill v: commercial awareness and business acumen, shown through innovation, creativity, flexibility, regard for the public interest and enterprise skills.",
  prac="Graduates are expected to show commercial awareness, business acumen, innovation, creativity and flexibility, with regard to the public interest and enterprise skills.",
  ben="You are expected to show commercial awareness and business sense, with creativity, flexibility and new ideas, while keeping the public interest in mind.",
  q="What opportunity have you spotted that others missed, and what would it take to act on it?")
k315(11, verbs=['appreciate'], about='skill w: cultural awareness',
  para="Skill w: appreciating cultural differences and their possible effects on the discipline, on study and on organisations; where a course includes work or study abroad, ability in another language matters too.",
  prac="Graduates are expected to appreciate cultural differences and how they affect the discipline, study and organisations; on courses with time abroad, foreign language ability also matters.",
  ben="You are expected to appreciate cultural differences and how they can shape accounting, study and organisations; if your course includes time abroad, another language helps too.",
  q="How might a cultural difference change how a set of accounts is read?")
k315(12, verbs=['undertake', 'reach'], about='skill x: research',
  para="Skill x: combining earlier skills to carry out a systematic, robust investigation that reaches an informed conclusion on an issue: engaging critically with literature, finding credible sources, framing questions, analysing, managing the project and presenting findings clearly, to add knowledge or drive change.",
  prac="Graduates are expected to plan and complete a systematic investigation: critical use of literature, credible sources, focused questions, analysis, project management and clear reporting of findings.",
  ben="You are expected to carry out a careful, systematic investigation of your own: read critically, find credible sources, ask good questions, analyse, manage the project and present clear findings.",
  q="What question would you most like to investigate, and how would you know your sources were credible?")
# learning and teaching
prov('3.16', force='will', verbs=['designed', 'allow', 'develop'], about='learning and teaching strategy',
  para="Learning and teaching strategies will be designed so students build conceptual and applied knowledge, higher-order thinking, technical accounting skills and relevant professional and transferable skills.",
  prac="Design the learning and teaching strategy to develop conceptual and applied knowledge, higher-order thinking, technical skills and professional and transferable skills together.",
  q="Which of these four strands gets the least teaching time?")
prov('3.17', force='will', verbs=['designed', 'consider', 'promote'], about='constructive alignment and balance',
  para="Methods will be designed so activities align with intended outcomes, and teaching should be coherent with assessment, balance conceptual and applied study and encourage continuous learning and enquiry, giving students an appetite for lifelong learning.",
  prac="Align activities with intended outcomes and with assessment, balance conceptual and applied work and encourage continuing enquiry and lifelong learning.",
  q="For one module, can you trace each outcome to an activity and an assessment?")
both('3.18', verbs=['designed', 'support'], about='employability and responsible citizenship',
  para="Learning and teaching should be designed to build skills, competencies, attitudes and experiences that help students become employable professionals and responsible citizens; some courses allow or require a placement for applying learning outside.",
  prac="Design teaching to build employability and civic responsibility together; where possible offer placements where students apply their learning.",
  ben="Your course should help you build the skills, attitudes and experience to become an employable professional and a responsible citizen, sometimes through a placement.",
  q="What experience outside the classroom would most help your career plans?")
prov('3.19', verbs=['adopted', 'result', 'inform', 'encourage'], about='pedagogy for deep learning',
  para="Teaching may draw on critical, dialogic, reflexive, collaborative and constructivist approaches, alone or mixed; whatever is chosen should lead to deep learning, in which students think critically about new concepts, rather than rote learning, and should guide assessment choices and intellectual growth.",
  prac="Choose pedagogies (dialogic, critical, reflexive, constructivist, collaborative) that produce deep rather than rote learning, and let them shape assessment.",
  q="Which teaching session most reliably produces deep rather than surface learning, and why?")
prov('3.20', verbs=['encouraged', 'designed'], about='diverse and active teaching approaches',
  para="A range of approaches should be encouraged within and across modules, from lectures, seminars, workshops and tutorials to blended, active and innovative learning; digital technologies matter because practice uses them, and approaches should be designed for engagement and active participation.",
  prac="Mix lectures, seminars, workshops, tutorials, blended and active learning, use the digital tools practice uses, and design for student engagement.",
  q="What share of contact time asks students to do something rather than listen?")
prov('3.22', force='will', verbs=['prepare', 'understand', 'design'], about='digital technologies in teaching',
  para="Because a degree should prepare students to understand data systems, it will very probably be necessary to build suitable digital technology into teaching: cloud accounting packages, data cleaning and analytics tools, spreadsheets, AI including GenAI and emerging technology.",
  prac="Build current digital tools into teaching: cloud accounting packages, data preparation and analytics tools, spreadsheets and AI, refreshed as practice changes.",
  q="Which software that graduates will meet at work do they never use on the course?")
both('3.23', verbs=['recognising', 'address', 'provide'], about='inclusive, accessible and culturally aware teaching',
  para="Learning and teaching should be inclusive and accessible by design and, ideally, should address the varied cultures and learning settings students come from, helping them move into a critical learning environment and learn from others about the global context.",
  prac="Design teaching to be inclusive and accessible, and help students from varied educational cultures adjust to critical learning and learn from one another.",
  ben="Your course should be inclusive and accessible, and help you adjust if you are used to a different way of learning, and learn from classmates with other backgrounds.",
  q="What was hardest to adjust to in how you are taught here, compared with before?")
prov('3.24', verbs=['encouraged', 'reflect', 'enhance'], about='research-informed and practice-informed teaching',
  para="Teaching, research and professional practice interact in the learning setting, and teaching should be research-informed or research-led; staff should be encouraged to draw on their professional and academic experience so teaching reflects current developments.",
  prac="Keep teaching research-informed or research-led, and draw on staff's professional and academic experience to reflect current developments.",
  q="Where does current research or practice experience show up in a core module?")
prov('3.25', verbs=['adapt', 'considered', 'receive'], about='responsive strategy and staff development',
  para="Teaching design can usefully draw on pedagogic research; strategies should adapt to business and regulatory change and technology, and teaching staff are expected to have access to professional development and suitable training.",
  prac="Update strategies for business, regulatory and technological change, use pedagogic research and give teaching staff professional development and training.",
  q="What training have staff had in the last year on new technology for teaching?")
prov('3.26', verbs=['monitored', 'reviewed', 'ensure'], about='reviewing learning and teaching',
  para="The strategy, structures and approaches for teaching should be kept under continual review for quality and currency.",
  prac="Review the learning and teaching strategy continually, through the monitoring and review cycle, for quality and currency.",
  q="What did the last review of teaching approaches change?")
# assessment
prov('3.27', verbs=['assessing'], about='robust summative assessment',
  para="Summative assessment should be robust and rigorous in measuring students' attainment of the statement's knowledge, understanding and skills as built into the course's learning outcomes.",
  prac="Make summative assessment robust and rigorous against the knowledge, understanding and skills in the statement as written into the outcomes.",
  q="Which programme outcome is assessed least rigorously?")
prov('3.28', verbs=['include', 'designed', 'enhance', 'encourage'], about='formative assessment and feedback',
  para="Alongside summative assessment, courses should include varied formative assessment and feedback, designed to enrich the learning setting and promote active, independent learning.",
  prac="Provide a range of formative assessments and feedback that encourage active, independent learning.",
  q="How many formative opportunities does a student get before the first summative task?")
prov('3.29', verbs=['balanced', 'support', 'enable', 'demonstrate'], about='a balanced and inclusive portfolio',
  para="The assessment portfolio across the degree should be balanced, with a fitting range of methods, so that it is inclusive, flexible and innovative, supports learning and lets students show rising attainment.",
  prac="Balance assessment methods across the degree so the scheme is inclusive, flexible and innovative and shows progression.",
  q="Is any single method used so often that it advantages one group of students?")
prov('3.30', verbs=['ensure', 'achieved', 'avoid'], about='no route around critical elements',
  para="Across the degree, assessment should make sure all required knowledge and skills are achieved, including the discursive, conceptual and critical, and should not let students avoid them by concentrating on routine, calculative and technical work.",
  prac="Weight and structure assessment so students cannot pass by focusing on calculation and technique alone; the discursive and critical elements must be unavoidable.",
  q="Could a student pass the degree with almost no essay or critical writing?")
prov('3.31', verbs=['designed', 'avoid', 'include'], about='assessing depth, not rote learning',
  para="Assessment should test depth of learning and skill, avoiding designs that let students pass through rote or surface learning such as objective tests; modules should include substantial critical assessment, authentic cases and technical questions set in dynamic scenarios, and any multiple choice should be designed not to reward uncritical learning.",
  prac="Design out rote learning: include substantial critical, authentic and case-based assessment, embed technical questions in dynamic scenarios and use multiple choice only where it is designed not to reward surface learning.",
  q="What proportion of marks in core modules comes from objective tests?")
both('3.32', verbs=['designed', 'operated', 'equip', 'include'], domain='generic-skill', level='fheq:6', award=HON, about='assessment for independent, lifelong learners',
  para="The assessment strategy should be designed and run to make students independent, self-directed lifelong learners and critical thinkers, with feedback that helps their future learning.",
  prac="Design assessment and feedback to develop independent, self-directed and critical learners, with feedback aimed at the next task.",
  ben="Your assessments and feedback should help you become an independent, critical learner who keeps learning after graduation.",
  q="How have you used feedback from one assessment in the next?")
prov('3.33', verbs=['designed', 'undermine', 'demonstrate'], about='inclusive assessment and reasonable adjustments',
  para="Assessment should be inclusive for EDI and accessibility, with reasonable adjustments where suitable that leave the assessment's nature, scope and outcomes intact; overall it should let students show what they have achieved.",
  prac="Make assessment inclusive and accessible, with reasonable adjustments that keep the assessment's purpose and the outcomes intact.",
  q="Which adjustment request last tested whether an assessment's purpose could be kept?")
both('3.34', verbs=['designed', 'facilitate', 'contribute'], about='assessment as dialogue and feedback',
  para="Summative and formative assessment should support dialogues of learning that help students learn and become lifelong learners; feedback can take many forms, including students comparing their work with exemplars, peers' work, GenAI outputs or theory, and feedback schemes should be timely and usable.",
  prac="Design assessment as dialogue: use exemplars, peer work and GenAI outputs for students to compare against their own, and give timely feedback they can act on.",
  ben="Your assessments should help you learn through dialogue, for example by comparing your work with examples, classmates' work or AI outputs, and you should get feedback in time to use it.",
  q="Which comparison has taught you most about the quality of your own work?")
prov('3.35', verbs=['clear', 'given'], about='clear assessment schemes and workload',
  para="Each module's assessment scheme should be clear to students at its start, and programme schemes should take account of timing and total workload.",
  prac="Publish each module's assessment scheme at the start and plan the timing and total assessment load across the programme.",
  q="Where do deadlines across modules cluster in the same week?")
prov('3.36', verbs=['communicated', 'related'], about='timely, indicative assessment criteria',
  para="Assessment criteria should be communicated to students in good time, normally before they start work on the task; rubrics should normally be indicative and linked to learning outcomes rather than prescriptive.",
  prac="Give students the criteria before they begin each task, using indicative rubrics linked to module and programme outcomes rather than detailed marking schedules.",
  q="When do students first see the criteria for the main assessment in each module?")
both('3.39', verbs=['taken', 'given', 'provided'], about='fair team and group assessment',
  para="Group assessment can suit collaborative skills; where it is used, grades should fairly reflect individuals' attainment, the balance with individual work should be weighed, and students should get guidance on running teams.",
  prac="Where you assess group work, make grades reflect individual contributions, balance it with individual work and teach students how to manage teams.",
  ben="Where you are assessed as a group, your grade should fairly reflect your own contribution, and you should get guidance on how to run a team.",
  q="How was your individual contribution recognised in your last group assessment?")
prov('3.41', verbs=['managed', 'provided', 'contribute'], about='safeguards for peer assessment',
  para="Peer discussion and review can aid learning, but it should be well managed with safeguards so no one is disadvantaged, especially for EDI reasons; students should normally have guidance or training, and peer ratings should not normally count towards summative marks without strong protection and academic input.",
  prac="Manage peer review with safeguards and training; keep peer ratings out of summative marks unless strong protections and academic oversight are in place.",
  q="Do peer ratings count anywhere in summative marks, and what protects students who might be marked down unfairly?")
prov('3.42', verbs=['take', 'design', 'taken'], about='GenAI and assessment design',
  para="Widespread GenAI means assessment design must account for AI, but it also allows designs closer to the statement's aims, such as critical, authentic, case-based and experiential tasks and assessment of students' grasp of AI in accounting; these points should apply to formative and summative work.",
  prac="Rework assessment for GenAI: authentic cases, dynamic scenarios, experiential tasks and assessment of students' understanding of AI in accounting, in formative and summative work.",
  q="Which assessments has the team redesigned since GenAI tools became common?")
prov('3.43', verbs=['ensure', 'communicated', 'reminded'], about='GenAI policies communicated to all',
  para="When designing assessment for GenAI, modules should keep integrity and GenAI control policies under continuous review, since AI content is hard to detect; policies, including acceptable use, should be clear to all staff and students, and students should be reminded of the highest ethical and professional standards.",
  prac="Review GenAI and integrity policies continuously, state acceptable use clearly to staff and students, and remind students of the profession's ethical standards.",
  q="Is acceptable GenAI use stated for each assessment, and do staff apply it the same way?")

# =============================================================== section 4: benchmark standards (paragraphs)
prov('4.2', verbs=['follow'], about='competence standards and EHRC guidance',
  para="The standards at each level are not universal competence standards; a provider developing competence standards under the Equality Act 2010 may draw on the statement and PSRB requirements and should then follow the Equality and Human Rights Commission's latest guidance.",
  prac="Do not read the standards as competence standards; if you write competence standards, use the statement and PSRB requirements and follow current EHRC guidance.",
  q="Has the course defined competence standards, and were they checked against current EHRC guidance?")
prov('4.4', verbs=['interpreted', 'applied', 'recognising'], about='interpreting the standards',
  para="Most students are expected to do much better than the threshold; the standards should be read and applied with the understanding that each provider decides what evidence each class of degree needs.",
  prac="Apply the standards as a guide, not a mark scheme: your institution sets the evidence each class needs, and most students should exceed the threshold.",
  q="How do the institution's class descriptors line up with the four levels in Table 1?")

# =============================================================== Table 1: honours rungs (paragraph 4.5)
_T1 = _cells([
  "Basic knowledge and understanding of the critical", "Some ability to integrate theoretical", "Solid knowledge and understanding of the critical",
  "Good ability to integrate theoretical", "Very good knowledge and understanding of the critical", "Very good ability to integrate theoretical",
  "Excellent knowledge and understanding of the critical", "Excellent ability to integrate theoretical",
  "Basic knowledge and understanding of substantially", "Able to demonstrate some ability to integrate", "Solid knowledge and understanding of substantially",
  "Able to demonstrate a good level of integration", "Very good knowledge and critical understanding of substantially", "Able to demonstrate a very good level",
  "Excellent knowledge and critical understanding at an advanced", "Able to demonstrate an excellent ability to integrate",
  "Sufficient levels of proficiency", "Able to demonstrate some ability to select", "Good levels of proficiency", "Able to demonstrate good ability to select",
  "Very good levels of proficiency", "Able to demonstrate very good ability to select", "Excellent levels of proficiency", "Able to demonstrate excellent ability to select",
  "Basic ability to apply", "Good ability to apply", "Very good ability to apply", "Excellent ability to apply"], _NORM.index('Table 1: On graduating'))
RUNGS = ['threshold', 'typical', 'very-good', 'excellent']
CLASS = {'threshold': 'third-class or pass', 'typical': 'lower second (2:2)', 'very-good': 'upper second (2:1)', 'excellent': 'first-class'}
BAND = {'threshold': '3rd', 'typical': '2.2', 'very-good': '2.1', 'excellent': '1st'}
LEAD = {'threshold': 'For a third or a pass, at the least, ', 'typical': 'For a lower second (2:2), at the least, ',
        'very-good': 'For an upper second (2:1), at the least, ', 'excellent': 'For a first, at the least, '}
ROW = {}   # S4 id -> (row key, rung)
def t1(n, rung, rowk, **k):
    t, a = _T1[n - 1]
    i = '4.5.b%d' % n; ROW[i] = (rowk, rung)
    d = dict(type=rung, rung=rung, force='threshold', level='fheq:6', award=HON, appliesTo='honours graduates at the %s level' % rung,
             addressee='learner')
    d.update(k); d['ben'] = LEAD[rung] + d['ben']
    s(i, find=t, after=a, **d)

# row 1: critical, ethical and contextual knowledge and understanding
t1(1, 'threshold', 'r1a', verbs=[], domain='knowledge', about='critical, ethical and contextual knowledge',
   para="A basic grasp of why accounting matters critically, ethically and in context.",
   prac="At threshold, graduates have a basic grasp of accounting's critical, ethical and contextual significance.",
   ben="you need a basic grasp of why accounting matters ethically, critically and in its wider setting.",
   q="Can you say in a few sentences why accounting is more than a technical exercise?")
t1(2, 'threshold', 'r1b', verbs=['integrate'], domain='understanding', about='bringing theory into discussion of public and organisational issues',
   para="Some capacity to bring theory, concepts and debate into discussion of public and organisational questions from several social, economic, accountability and sustainability angles.",
   prac="At threshold, graduates show some capacity to draw theory and debate into discussion of public and organisational questions from several perspectives.",
   ben="you need some ability to bring theories and debates into a discussion of public or organisational questions, looking at them from more than one angle.",
   q="Which theory have you used to make sense of a real organisational issue?")
t1(3, 'typical', 'r1a', verbs=[], domain='knowledge', about='critical, ethical and contextual knowledge',
   para="A solid grasp of accounting's critical, ethical and contextual significance.",
   prac="At the typical level, graduates have a solid grasp of accounting's critical, ethical and contextual significance.",
   ben="you need a solid grasp of why accounting matters ethically, critically and in its wider setting.",
   q="Where does your understanding of accounting's wider importance feel secure, and where thin?")
t1(4, 'typical', 'r1b', verbs=['integrate'], domain='understanding', about='bringing theory into critical discussion of public and organisational issues',
   para="A good capacity to bring theory, concepts and debate into critical discussion of public and organisational questions from several perspectives.",
   prac="At the typical level, graduates bring theory and debate well into critical discussion of public and organisational questions from several perspectives.",
   ben="you need to bring theories and debates well into a critical discussion of public or organisational questions from several angles.",
   q="In your last essay, did the theory drive the argument or decorate it?")
t1(5, 'very-good', 'r1a', verbs=[], domain='knowledge', about='critical, ethical and contextual knowledge',
   para="A very good grasp of accounting's critical, ethical and contextual significance.",
   prac="At the very good level, graduates have a very good grasp of accounting's critical, ethical and contextual significance.",
   ben="you need a very good grasp of why accounting matters ethically, critically and in its wider setting.",
   q="Can you explain an ethical tension in accounting and the context that creates it?")
t1(6, 'very-good', 'r1b', verbs=['integrate'], domain='understanding', about='bringing theory into critical discussion of public and organisational issues',
   para="A very good capacity to bring theory and debate into critical discussion of public and organisational questions across a wide range of perspectives, joined up and synthesised.",
   prac="At the very good level, graduates integrate theory and debate into critical discussion across a wide range of perspectives, in a joined-up, synthesised way.",
   ben="you need to bring theories and debates into critical discussion from a wide range of angles and pull them together into one coherent view.",
   q="How did you reconcile two perspectives that pulled in different directions?")
t1(7, 'excellent', 'r1a', verbs=[], domain='knowledge', about='critical, ethical and contextual knowledge',
   para="An excellent grasp of accounting's critical, ethical and contextual significance.",
   prac="At the excellent level, graduates have an excellent grasp of accounting's critical, ethical and contextual significance.",
   ben="you need an excellent grasp of why accounting matters ethically, critically and in its wider setting.",
   q="What would you teach a first-year student about why accounting matters beyond the numbers?")
t1(8, 'excellent', 'r1b', verbs=['integrate'], domain='understanding', about='bringing theory into critical discussion of public and organisational issues',
   para="An excellent capacity to weave theory and debate into critical discussion of public and organisational questions across a wide range of perspectives, fully synthesised.",
   prac="At the excellent level, graduates weave theory and debate into critical discussion across a wide range of perspectives with full synthesis.",
   ben="you need to weave theories and debates into critical discussion from a wide range of angles, synthesising them into a well-integrated argument.",
   q="Where did your synthesis produce a view that none of your sources held on its own?")
# row 2: subject-specific knowledge, understanding and skills
t1(9, 'threshold', 'r2a', verbs=[], domain='knowledge', about='knowledge across the broad areas',
   para="Basic knowledge of nearly all the broad areas of accounting.",
   prac="At threshold, graduates have basic knowledge and understanding of almost all the broad areas in 3.10.",
   ben="you need a basic knowledge of nearly all the main areas of accounting.",
   q="Which of the broad areas of accounting would you be least confident to explain?")
t1(10, 'threshold', 'r2b', verbs=['demonstrate', 'integrate'], domain='understanding', about='integrating knowledge across the areas',
   para="Shows some capacity to connect knowledge across the broad areas.",
   prac="At threshold, graduates show some ability to connect knowledge across the broad areas.",
   ben="you need to show some ability to connect what you know across the main areas of accounting.",
   q="Can you link something from audit to something from management accounting?")
t1(11, 'typical', 'r2a', verbs=[], domain='knowledge', about='knowledge across the broad areas',
   para="Solid knowledge of nearly all the broad areas and a basic grasp of the rest.",
   prac="At the typical level, graduates have solid knowledge of almost all the broad areas and basic understanding of the remainder.",
   ben="you need a solid knowledge of nearly all the main areas of accounting and a basic grasp of the rest.",
   q="Which areas feel solid for you, and which only basic?")
t1(12, 'typical', 'r2b', verbs=['demonstrate'], domain='understanding', about='integrating knowledge across the areas',
   para="Shows good integration of knowledge across the broad areas.",
   prac="At the typical level, graduates show good integration of knowledge across the broad areas.",
   ben="you need to show that you connect what you know across the main areas of accounting well.",
   q="Where did knowledge from one area change your answer in another?")
t1(13, 'very-good', 'r2a', verbs=[], domain='knowledge', about='knowledge across the broad areas',
   para="Very good, critical knowledge of nearly all the broad areas and a solid grasp of the rest.",
   prac="At the very good level, graduates have very good knowledge and critical understanding of almost all broad areas and solid understanding of the rest.",
   ben="you need very good, critical knowledge of nearly all the main areas of accounting and a solid grasp of the rest.",
   q="In which area could you criticise the standard approach, not only describe it?")
t1(14, 'very-good', 'r2b', verbs=['demonstrate'], domain='understanding', about='integrating knowledge across the areas',
   para="Shows very good integration of knowledge across the broad areas.",
   prac="At the very good level, graduates show very good integration of knowledge across the broad areas.",
   ben="you need to show that you connect what you know across the main areas of accounting very well.",
   q="How would a tax decision ripple through reporting, audit and risk?")
t1(15, 'excellent', 'r2a', verbs=[], domain='knowledge', about='knowledge across the broad areas',
   para="Excellent, critical and advanced knowledge of nearly all the broad areas and a very good grasp of the rest.",
   prac="At the excellent level, graduates have excellent, advanced critical knowledge of almost all broad areas and very good understanding of the remainder.",
   ben="you need excellent, advanced and critical knowledge of nearly all the main areas of accounting and a very good grasp of the rest.",
   q="Which area could you discuss at the level of current research?")
t1(16, 'excellent', 'r2b', verbs=['demonstrate', 'integrate'], domain='understanding', about='integrating knowledge across the areas',
   para="Shows excellent integration of knowledge across every broad area.",
   prac="At the excellent level, graduates integrate knowledge excellently across all the broad areas.",
   ben="you need to show that you connect what you know across all the main areas of accounting excellently.",
   q="Can you build one case that draws on five or more areas at once?")
# row 3: transferable, professional and practice skills and higher-order skills
t1(17, 'threshold', 'r3a', verbs=['perform', 'applying'], domain='generic-skill', about='proficiency in transferable and professional skills',
   para="Adequate proficiency in most of the skills in 3.14 and 3.15, used adequately on simple, well-defined problems.",
   prac="At threshold, graduates are adequately proficient in most of the listed skills and use them adequately on straightforward, structured problems.",
   ben="you need to be reasonably skilled in most of the transferable and professional skills and use them adequately on simple, well-defined problems.",
   q="Which of the listed skills could you not yet use on your own?")
t1(18, 'threshold', 'r3b', verbs=['demonstrate', 'select', 'consider', 'evaluate', 'synthesise', 'construct'], domain='generic-skill', about='building arguments from knowledge',
   para="Shows some capacity to choose, weigh, comment on and combine knowledge into sound arguments.",
   prac="At threshold, graduates show some ability to select, evaluate and synthesise knowledge into valid arguments.",
   ben="you need to show some ability to choose, weigh up and combine what you know into a sound argument.",
   q="What makes an argument valid rather than just plausible?")
t1(19, 'typical', 'r3a', verbs=['perform', 'applying'], domain='generic-skill', about='proficiency in transferable and professional skills',
   para="Good proficiency in nearly all the skills, used critically and well on moderately complex, partly structured problems.",
   prac="At the typical level, graduates are proficient in almost all the skills and apply them critically and well to moderately complex, partly structured problems.",
   ben="you need good skill in nearly all the transferable and professional skills and use them critically on moderately complex problems that are not fully defined.",
   q="How did you handle a problem whose brief left key details open?")
t1(20, 'typical', 'r3b', verbs=['demonstrate', 'select', 'consider', 'evaluate', 'synthesise', 'construct'], domain='generic-skill', about='building arguments from knowledge',
   para="Shows good capacity to choose, weigh, comment on and combine knowledge into strong arguments.",
   prac="At the typical level, graduates show good ability to select, evaluate and synthesise knowledge into strong arguments.",
   ben="you need to show that you can choose, weigh up and combine what you know into strong arguments.",
   q="What would make your last argument stronger?")
t1(21, 'very-good', 'r3a', verbs=['perform', 'applying'], domain='generic-skill', about='proficiency in transferable and professional skills',
   para="Very good proficiency in nearly all the skills, applied critically and in combination to complex, unstructured problems.",
   prac="At the very good level, graduates are very proficient in almost all the skills and apply them critically and together to complex, unstructured problems.",
   ben="you need very good skill in nearly all the transferable and professional skills and use them together, critically, on complex problems without a set structure.",
   q="When did you use several skills together to crack a messy problem?")
t1(22, 'very-good', 'r3b', verbs=['demonstrate', 'select', 'consider', 'evaluate', 'synthesise', 'construct'], domain='generic-skill', about='building arguments from knowledge',
   para="Shows very good capacity to choose, weigh, comment on and combine knowledge into strong and creative arguments.",
   prac="At the very good level, graduates select, evaluate and synthesise knowledge very well into strong, creative arguments.",
   ben="you need to show that you can choose, weigh up and combine what you know into strong and original arguments.",
   q="Where did you make an argument that surprised your reader?")
t1(23, 'excellent', 'r3a', verbs=['perform', 'applying'], domain='generic-skill', about='proficiency in transferable and professional skills',
   para="Excellent proficiency in nearly all the skills, applied critically and in combination to complex, unstructured and open-ended problems.",
   prac="At the excellent level, graduates are excellently proficient in almost all the skills and apply them critically and together to complex, unstructured and unbounded problems.",
   ben="you need excellent skill in nearly all the transferable and professional skills and use them together, critically, on complex, open-ended problems with no clear edges.",
   q="How did you decide where to draw the boundary of a problem that had none?")
t1(24, 'excellent', 'r3b', verbs=['demonstrate', 'select', 'consider', 'evaluate', 'synthesise', 'construct'], domain='generic-skill', about='building arguments from knowledge',
   para="Shows excellent capacity to choose, weigh, comment on and combine knowledge into strong and creative arguments.",
   prac="At the excellent level, graduates select, evaluate and synthesise knowledge excellently into strong, creative arguments.",
   ben="you need to show excellent skill in choosing, weighing up and combining what you know into strong and original arguments.",
   q="What is the most original argument you have made, and how did you test it?")
# row 4: application of knowledge and understanding
t1(25, 'threshold', 'r4', verbs=['apply'], domain='subject-skill', about='applying accounting to problems in many organisations',
   para="A basic capacity to apply accounting knowledge, with a range of skills and critique, to simple, well-defined problems in various kinds of organisation.",
   prac="At threshold, graduates apply accounting knowledge with a range of skills and critique to straightforward, structured problems across organisation types.",
   ben="you need to be able to apply what you know about accounting, with some critical thought, to simple, well-defined problems in different kinds of organisation.",
   q="Can you solve a standard problem and say what its answer leaves out?")
t1(26, 'typical', 'r4', verbs=['apply'], domain='subject-skill', about='applying accounting to problems in many organisations',
   para="A good capacity to apply accounting knowledge, drawing on a broad set of skills and critical thought, on moderately complex, partly structured problems in various organisations.",
   prac="At the typical level, graduates apply accounting knowledge well, drawing on a broad set of skills and critical thought, on moderately complex, partly structured problems.",
   ben="you need to apply what you know about accounting well, with a broad range of skills and critical thought, to moderately complex problems that are not fully defined.",
   q="What judgement did you have to make where the problem did not tell you what to do?")
t1(27, 'very-good', 'r4', verbs=['apply'], domain='subject-skill', about='applying accounting to problems in many organisations',
   para="A very good capacity to apply accounting knowledge, drawing on a wide set of skills and critical thought, on complex, unstructured problems in various organisations.",
   prac="At the very good level, graduates apply accounting knowledge very well, drawing on a wide set of skills and critical thought, on complex, unstructured problems.",
   ben="you need to apply what you know about accounting very well, with a wide range of skills and critical thought, to complex problems without a set structure.",
   q="How did you structure a complex case before analysing it?")
t1(28, 'excellent', 'r4', verbs=['apply'], domain='subject-skill', about='applying accounting to problems in many organisations',
   para="An excellent capacity to apply accounting knowledge, drawing on a wide set of skills and critical thought, on complex, unstructured and open-ended problems in various organisations.",
   prac="At the excellent level, graduates apply accounting knowledge excellently, drawing on a wide set of skills and critical thought, on complex, unstructured and unbounded problems.",
   ben="you need to apply what you know about accounting excellently, with a wide range of skills and critical thought, to complex, open-ended problems.",
   q="Where did you show judgement on a problem with several defensible answers?")

# =============================================================== Table 2: master's threshold (paragraph 4.7)
_T2 = _cells([
  "Specialist and sophisticated knowledge and understanding of the critical", "Ability to integrate theoretical and conceptual issues and debates into critical",
  "Comprehensive knowledge and understanding of the critical", "Ability to integrate theoretical and conceptual issues and debates within sound",
  "Comprehensive knowledge and understanding of the critical", "Ability to integrate theoretical and conceptual issues and debates within critical",
  "In addition to reaching the benchmark",
  "Specialist and sophisticated knowledge and critical understanding", "Ability to demonstrate informed and insightful integration",
  "Comprehensive knowledge and understanding of substantially", "Ability to demonstrate informed and insightful integration",
  "Comprehensive and advanced knowledge", "Ability to demonstrate informed and insightful integration",
  "Very good levels of proficiency", "Ability to demonstrate capacity to select", "Very good levels of proficiency", "Ability to demonstrate capacity to select",
  "Very good levels of proficiency", "Ability to demonstrate capacity to select", "In addition to reaching the benchmark",
  "Ability to apply specialised", "Ability to apply knowledge and understanding of accounting in an informed",
  "Ability to apply knowledge and understanding of accounting in an informed",
  "Convincing evidence of achievement", "Convincing evidence of achievement", "Convincing evidence of achievement", "Convincing evidence of achievement"],
  _NORM.index("Table 2: Master's degree benchmark"))
MLEAD = {ADV: "On an advanced or specialist master's, as a minimum, ", CONV: "On a conversion master's, as a minimum, ",
         PROF: "On a professional master's, as a minimum, ", INT: "On an integrated master's, as a minimum, "}
def t2(n, award, rowk, **k):
    t, a = _T2[n - 1]
    i = '4.7.b%d' % n; ROW[i] = (rowk, 'threshold')
    d = dict(type='threshold', rung='threshold', force='threshold', level='fheq:7', award=award, appliesTo='graduates of the %s' % award,
             addressee='learner')
    d.update(k); d['ben'] = MLEAD[award] + d['ben']
    s(i, find=t, after=a, **d)
t2(1, ADV, 'm1a', verbs=[], domain='knowledge', about="specialist critical, ethical and contextual knowledge",
   para="Specialist, sophisticated knowledge of accounting's critical, ethical and contextual significance.",
   prac="Advanced or specialist master's graduates hold specialist and sophisticated knowledge of accounting's critical, ethical and contextual significance.",
   ben="you need specialist, sophisticated knowledge of why accounting matters ethically, critically and in context.",
   q="How does your specialism change the ethical questions accounting raises?")
t2(2, ADV, 'm1b', verbs=['integrate'], domain='understanding', about="integrating theory into critical discussion, by specialism",
   para="The capacity to integrate theory and debate into critical discussion of public or organisational questions, drawing on suitable perspectives, very well synthesised and fitted to the specialism.",
   prac="Advanced or specialist master's graduates integrate theory and debate into critical discussion with a high degree of synthesis suited to their specialism.",
   ben="you need to bring theory and debate into critical discussion of public or organisational issues, pulling perspectives together in a way that suits your specialism.",
   q="Which debate in your specialism is still unresolved, and where do you stand?")
t2(3, CONV, 'm1a', verbs=[], domain='knowledge', about="comprehensive critical, ethical and contextual knowledge",
   para="Comprehensive knowledge of accounting's critical, ethical and contextual significance.",
   prac="Conversion master's graduates hold comprehensive knowledge of accounting's critical, ethical and contextual significance.",
   ben="you need comprehensive knowledge of why accounting matters ethically, critically and in context.",
   q="What did you assume about accounting before the course that you now see differently?")
t2(4, CONV, 'm1b', verbs=['integrate'], domain='understanding', about="integrating theory into sound critical discussion",
   para="The capacity to integrate theory and debate into sound critical discussion of public and organisational questions from a range of perspectives.",
   prac="Conversion master's graduates integrate theory and debate into sound critical discussion of public and organisational questions from several perspectives.",
   ben="you need to bring theory and debate into a sound critical discussion of public and organisational questions from several angles.",
   q="Which perspective from your first discipline helps you criticise accounting?")
t2(5, PROF, 'm1a', verbs=['applied'], domain='knowledge', about="comprehensive knowledge, as applied in practice",
   para="Comprehensive knowledge of accounting's critical, ethical and contextual significance, above all in practice.",
   prac="Professional master's graduates hold comprehensive knowledge of accounting's critical, ethical and contextual significance, especially as practised.",
   ben="you need comprehensive knowledge of why accounting matters ethically, critically and in context, especially in professional practice.",
   q="Where in practice have you seen an ethical judgement that the rules did not settle?")
t2(6, PROF, 'm1b', verbs=['integrate'], domain='understanding', about="integrating theory into discussion of professional practice",
   para="The capacity to integrate theory and debate into critical discussion of professional, public and organisational questions, especially practice, from suitable perspectives, joined up and synthesised.",
   prac="Professional master's graduates integrate theory and debate into critical, synthesised discussion of professional and organisational practice.",
   ben="you need to bring theory and debate into a critical, joined-up discussion of professional and organisational practice.",
   q="Which theory best explains a practice you have seen at work?")
t2(7, INT, 'm1i', verbs=[], domain='knowledge', about="honours standards plus master's standards, combined",
   para="Reaching the typical or very good honours level of Table 1 and then the advanced or specialist master's level, or the higher levels of the professional master's, as the table sets out.",
   prac="Integrated master's graduates reach the typical or very good honours standard and then the advanced or specialist (or professional) master's standard set out in Table 2.",
   ben="you need to reach at least a lower or upper second honours level and then the level of an advanced, specialist or professional master's.",
   q="Which master's type does your final year most resemble, and does your work reach its level?")
t2(8, ADV, 'm2a', verbs=[], domain='knowledge', about="specialist knowledge across or within the broad areas",
   para="Specialist, sophisticated and critical knowledge at an advanced level, either broadly across the areas of accounting or deeply in some, possibly with a further area inside or outside accounting.",
   prac="Advanced or specialist master's graduates hold advanced, critical knowledge across many broad areas or in depth in a subset, perhaps with another subject.",
   ben="you need specialist, advanced and critical knowledge, either across many areas of accounting or in real depth in a few.",
   q="Is your master's broad or deep, and how would an employer see that?")
t2(9, ADV, 'm2b', verbs=['demonstrate'], domain='understanding', about="sophisticated integration across the areas studied",
   para="Shows informed, insightful and sophisticated integration of knowledge across the areas studied.",
   prac="Advanced or specialist master's graduates integrate knowledge across their areas of study with insight and sophistication.",
   ben="you need to connect what you know across your areas of study in an informed, insightful and sophisticated way.",
   q="Where did connecting two of your areas give you an insight neither gave alone?")
t2(10, CONV, 'm2a', verbs=[], domain='knowledge', about="comprehensive knowledge of the broad areas",
   para="Comprehensive knowledge of nearly all the broad areas and a basic grasp of the rest.",
   prac="Conversion master's graduates hold comprehensive knowledge of almost all broad areas and basic understanding of the remainder.",
   ben="you need comprehensive knowledge of nearly all the main areas of accounting and a basic grasp of the rest.",
   q="Which of the broad areas would you most want more time on?")
t2(11, CONV, 'm2b', verbs=['demonstrate'], domain='understanding', about="insightful integration across the broad areas",
   para="Shows informed and insightful integration of knowledge across the broad areas.",
   prac="Conversion master's graduates integrate knowledge across the broad areas with insight.",
   ben="you need to connect what you know across the main areas of accounting in an informed, insightful way.",
   q="How does a decision in one area of accounting show up in another?")
t2(12, PROF, 'm2a', verbs=[], domain='knowledge', about="comprehensive, advanced knowledge of the broad areas",
   para="Comprehensive, advanced and critical knowledge of nearly all the broad areas and a solid grasp of the rest.",
   prac="Professional master's graduates hold comprehensive, advanced critical knowledge of almost all broad areas and solid understanding of the rest.",
   ben="you need comprehensive, advanced and critical knowledge of nearly all the main areas of accounting and a solid grasp of the rest.",
   q="Where would your knowledge be tested hardest in a professional examination?")
t2(13, PROF, 'm2b', verbs=['demonstrate'], domain='understanding', about="integration across the areas for professional practice",
   para="Shows informed, insightful integration of knowledge across the broad areas, especially for professional and organisational practice.",
   prac="Professional master's graduates integrate knowledge across the broad areas with insight, particularly for professional and organisational practice.",
   ben="you need to connect what you know across the main areas of accounting with insight, especially in professional practice.",
   q="Which client problem would draw on several areas of accounting at once?")
t2(14, ADV, 'm3a', verbs=['perform', 'applying'], domain='generic-skill', about="proficiency in transferable and professional skills",
   para="Very good proficiency in nearly all the skills, applied critically and in combination to complex, unstructured and open-ended problems.",
   prac="Advanced or specialist master's graduates apply nearly all the skills very well, critically and together, to complex, unstructured and unbounded problems.",
   ben="you need very good skill in nearly all the transferable and professional skills, used together and critically on complex, open-ended problems.",
   q="Which open-ended problem in your specialism have you tackled from scratch?")
t2(15, ADV, 'm3b', verbs=['demonstrate', 'select', 'consider', 'evaluate', 'synthesise', 'construct'], domain='generic-skill', about="arguments from specialised, advanced knowledge",
   para="Shows the capacity to choose, weigh, comment on and combine specialised, advanced knowledge into strong and creative arguments.",
   prac="Advanced or specialist master's graduates select, evaluate and synthesise specialised, advanced knowledge into strong, creative arguments.",
   ben="you need to choose, weigh up and combine specialised, advanced knowledge into strong and original arguments.",
   q="What is the strongest original argument in your dissertation plan?")
t2(16, CONV, 'm3a', verbs=['perform', 'applying'], domain='generic-skill', about="proficiency in transferable and professional skills",
   para="Very good proficiency in nearly all the skills, applied critically and well to moderately complex, unstructured problems.",
   prac="Conversion master's graduates apply nearly all the skills very well and critically to moderately complex, unstructured problems.",
   ben="you need very good skill in nearly all the transferable and professional skills, used critically on moderately complex problems without a set structure.",
   q="Which skill from your earlier degree has carried over best into accounting?")
t2(17, CONV, 'm3b', verbs=['demonstrate', 'select', 'consider', 'evaluate', 'synthesise', 'construct'], domain='generic-skill', about="building strong arguments",
   para="Shows the capacity to choose, weigh, comment on and combine knowledge into strong arguments.",
   prac="Conversion master's graduates select, evaluate and synthesise knowledge into strong arguments.",
   ben="you need to choose, weigh up and combine what you know into strong arguments.",
   q="How do you decide which evidence to leave out of an argument?")
t2(18, PROF, 'm3a', verbs=['perform', 'applying'], domain='generic-skill', about="proficiency in skills, with a practice emphasis",
   para="Very good proficiency in nearly all the skills, applied critically and in combination to complex, unstructured problems, usually with a practice focus.",
   prac="Professional master's graduates apply nearly all the skills very well, critically and together, to complex, unstructured problems, typically practice-based.",
   ben="you need very good skill in nearly all the transferable and professional skills, used together and critically on complex practical problems.",
   q="Which practical problem from work tested your skills most?")
t2(19, PROF, 'm3b', verbs=['demonstrate', 'select', 'consider', 'evaluate', 'synthesise', 'construct'], domain='generic-skill', about="arguments for professional practice",
   para="Shows the capacity to choose, weigh, comment on and combine knowledge into strong and creative arguments, especially for professional or organisational practice.",
   prac="Professional master's graduates select, evaluate and synthesise knowledge into strong, creative arguments about professional and organisational practice.",
   ben="you need to choose, weigh up and combine what you know into strong and original arguments about professional practice.",
   q="How would you persuade a sceptical partner to change a firm's practice?")
t2(20, INT, 'm3i', verbs=[], domain='generic-skill', about="honours skills plus master's skills, combined",
   para="For skills, reaching the typical or very good honours level of Table 1 and then the advanced or specialist master's level, or the higher professional master's level, as the table sets out.",
   prac="Integrated master's graduates reach the typical or very good honours skills standard and then the advanced or specialist (or professional) master's standard.",
   ben="your skills need to reach at least a lower or upper second honours level and then the level of an advanced, specialist or professional master's.",
   q="Which skill has grown most between your honours years and your master's year?")
t2(21, ADV, 'm4', verbs=['apply'], domain='subject-skill', about="sophisticated application to open-ended problems",
   para="The capacity to apply specialised, advanced knowledge with sophistication and insight, drawing on a wide set of skills and critical thought, on complex, unstructured and open-ended problems in various organisations, fitted to the degree's focus.",
   prac="Advanced or specialist master's graduates apply specialised, advanced knowledge with sophistication to complex, unstructured and unbounded problems, as the degree's focus requires.",
   ben="you need to apply specialised, advanced knowledge with insight and a wide range of skills to complex, open-ended problems in different organisations.",
   q="Where has your specialist knowledge solved a problem that general knowledge could not?")
t2(22, CONV, 'm4', verbs=['apply'], domain='subject-skill', about="informed application to moderately complex problems",
   para="The capacity to apply accounting knowledge with insight, drawing on a broad set of skills and critical thought, on moderately complex, unstructured problems in various organisations.",
   prac="Conversion master's graduates apply accounting knowledge with insight and a broad range of skills to moderately complex, unstructured problems.",
   ben="you need to apply what you know about accounting with insight and a broad range of skills to moderately complex problems without a set structure.",
   q="Which kind of organisation's accounting problem do you now feel able to tackle?")
t2(23, PROF, 'm4', verbs=['apply'], domain='subject-skill', about="informed application to practical, professional problems",
   para="The capacity to apply accounting knowledge with insight, drawing on a wide set of skills and critical thought, on complex, unstructured problems, especially practical and professional ones, in various organisations.",
   prac="Professional master's graduates apply accounting knowledge with insight and a wide range of skills to complex, unstructured problems, particularly practical and professional ones.",
   ben="you need to apply what you know about accounting with insight and a wide range of skills to complex practical and professional problems.",
   q="Which professional problem would you choose to show this to an employer?")
t2(24, ADV, 'm5', verbs=[], domain='subject-skill', about="the self-directed research project, specialist",
   para="Persuasive evidence of completing a substantial, self-directed research study at an advanced level in the specialism: a personal inquiry, driven by curiosity, into theory or into applying theory to a real issue.",
   prac="Advanced or specialist master's graduates give convincing evidence of a substantial, self-directed, advanced research study in their specialism, theoretical or applied.",
   ben="you need to show convincingly that you have completed a substantial research inquiry of your own, at an advanced level in your specialism.",
   q="What makes your research question worth a substantial study?")
t2(25, CONV, 'm5', verbs=[], domain='subject-skill', about="the self-directed research project",
   para="Persuasive evidence of completing a substantial, self-directed research study: a personal inquiry, driven by curiosity, into theory or into applying theory to a real issue.",
   prac="Conversion master's graduates give convincing evidence of a substantial, self-directed research study, theoretical or applied.",
   ben="you need to show convincingly that you have completed a substantial research inquiry of your own, into theory or a real issue.",
   q="How will your inquiry bring together your earlier discipline and accounting?")
t2(26, PROF, 'm5', verbs=['applying'], domain='subject-skill', about="the self-directed project, applied to practice",
   para="Persuasive evidence of completing a substantial, self-directed study, usually showing high achievement in applying knowledge to a practical or real project, perhaps linked to field or work-based learning.",
   prac="Professional master's graduates give convincing evidence of a substantial, self-directed study that applies knowledge to a practical project, often work-based.",
   ben="you need to show convincingly that you have completed a substantial study of your own that applies what you know to a real, practical project.",
   q="Which workplace issue would make the best practical project?")
t2(27, INT, 'm5', verbs=[], domain='subject-skill', about="the self-directed study in an integrated master's",
   para="Persuasive evidence of completing a substantial, self-directed study suited to the nature of the integrated master's.",
   prac="Integrated master's graduates give convincing evidence of a substantial, self-directed study suited to the degree.",
   ben="you need to show convincingly that you have completed a substantial study of your own, suited to your integrated master's.",
   q="How does your final-year study go beyond your honours dissertation or project?")

# =============================================================== gradeOf (same outcome, one rung below), inferred
GRADE = {}
for _r in range(3):
    for _k in (1, 2):
        b = _r * 8 + _k
        GRADE['4.5.b%d' % (b + 2)] = '4.5.b%d' % b
        GRADE['4.5.b%d' % (b + 4)] = '4.5.b%d' % (b + 2)
        GRADE['4.5.b%d' % (b + 6)] = '4.5.b%d' % (b + 4)
GRADE.update({'4.5.b26': '4.5.b25', '4.5.b27': '4.5.b26', '4.5.b28': '4.5.b27'})

# =============================================================== agent instructions (aaw, aad): our words, composed per record
CITE = '(QAA, 2025, Accounting Subject Benchmark Statement, %s)'
LEVELS = {'fheq:6': 'FHEQ level 6 (FQHEIS level 10)', 'fheq:7': 'FHEQ level 7 (FQHEIS level 11)'}
FW = {('fheq:6', 'knowledge'): 'qaa/fheq-2024/4.15.b1 at spine:6', ('fheq:6', 'understanding'): 'qaa/fheq-2024/4.15.b4 at spine:6',
      ('fheq:6', 'subject-skill'): 'qaa/fheq-2024/4.15.b2 at spine:6', ('fheq:6', 'generic-skill'): 'qaa/fheq-2024/4.15.b9.2 at spine:6',
      ('fheq:6', 'none'): 'qaa/fheq-2024/4.15.b1 at spine:6',
      ('fheq:7', 'knowledge'): 'qaa/fheq-2024/4.17.b1 at spine:7', ('fheq:7', 'understanding'): 'qaa/fheq-2024/4.17.b3 at spine:7',
      ('fheq:7', 'subject-skill'): 'qaa/fheq-2024/4.17.b5 at spine:7', ('fheq:7', 'generic-skill'): 'qaa/fheq-2024/4.17.b6 at spine:7',
      ('fheq:7', 'none'): 'qaa/fheq-2024/4.17.b1 at spine:7'}
FW_ROW = {'r1a': 'qaa/fheq-2024/4.15.b1', 'r1b': 'qaa/fheq-2024/4.15.b7', 'r2a': 'qaa/fheq-2024/4.15.b1', 'r2b': 'qaa/fheq-2024/4.15.b3.1',
          'r3a': 'qaa/fheq-2024/4.15.b8 and 4.15.b9.2', 'r3b': 'qaa/fheq-2024/4.15.b7', 'r4': 'qaa/fheq-2024/4.15.b3.1',
          'm1a': 'qaa/fheq-2024/4.17.b1', 'm1b': 'qaa/fheq-2024/4.17.b5', 'm1i': 'qaa/fheq-2024/4.15.b1 and 4.17.b1',
          'm2a': 'qaa/fheq-2024/4.17.b1', 'm2b': 'qaa/fheq-2024/4.17.b3', 'm3a': 'qaa/fheq-2024/4.17.b5 and 4.17.b8.2',
          'm3b': 'qaa/fheq-2024/4.17.b4.1', 'm3i': 'qaa/fheq-2024/4.15.b9.2 and 4.17.b6', 'm4': 'qaa/fheq-2024/4.17.b3',
          'm5': 'qaa/fheq-2024/4.17.b2 and 4.17.b6'}
ANNEX = {'r1a': 'knowledge/r2', 'r1b': 'cognitive/r2', 'r2a': 'knowledge/r1', 'r2b': 'knowledge/r2', 'r3a': 'transferable/r1',
         'r3b': 'cognitive/r2', 'r4': 'cognitive/r3'}
# honours cells a master's row builds on (typical and very good, Table 1)
HONROW = {'m1a': ('4.5.b3', '4.5.b5'), 'm1b': ('4.5.b4', '4.5.b6'), 'm1i': ('4.5.b3', '4.5.b5'), 'm2a': ('4.5.b11', '4.5.b13'),
          'm2b': ('4.5.b12', '4.5.b14'), 'm3a': ('4.5.b19', '4.5.b21'), 'm3b': ('4.5.b20', '4.5.b22'), 'm3i': ('4.5.b19', '4.5.b21'),
          'm4': ('4.5.b26', '4.5.b27'), 'm5': ('1.17', '3.15.b12')}
FORCEW = {'should': 'an expectation worded with "should"', 'must': 'a requirement worded with "must"', 'will': 'an expected feature worded with "will"',
          'threshold': 'a minimum condition', 'describes': 'an expected outcome stated without one of the five obliging words (force recorded as describes)'}
SID = 'qaa/accounting-2025/'

def _order(i):
    base, _, b = i.partition('.b')
    return tuple(int(x) for x in base.split('.')) + ((int(b),) if b else (0,))
_IDS = sorted(P, key=_order)

def _loc(i):
    if i.startswith('4.5.b'):
        return 'para 4.5, Table 1'
    if i.startswith('4.7.b'):
        return 'para 4.7, Table 2'
    if i.startswith('3.10.b'):
        return 'para 3.10, area %s' % 'abcdefghijkl'[int(i.split('.b')[1]) - 1]
    if i.startswith('3.15.b'):
        return 'para 3.15, skill %s' % 'mnopqrstuvwx'[int(i.split('.b')[1]) - 1]
    if i.startswith('1.16.b'):
        return 'para 1.16, type %s' % 'abcd'[int(i.split('.b')[1]) - 1]
    return 'para ' + i

def _awd(r):
    aw = r['award']
    if isinstance(aw, list):
        return "every taught master's type (advanced or specialist, conversion, professional and integrated)"
    return {'none': 'any Accounting degree the statement covers', HON: "the bachelor's degree with honours", ADV: "the advanced or specialist master's",
            CONV: "the Accounting conversion master's", PROF: "the professional master's", INT: "the integrated master's",
            'degree apprenticeship': 'the Accounting degree apprenticeship'}.get(aw, 'the ' + aw)

def _nb(i):
    k = _IDS.index(i); sec = i.split('.')[0]
    near = [x for x in (_IDS[k - 1] if k else None, _IDS[k + 1] if k + 1 < len(_IDS) else None) if x and x.split('.')[0] == sec and not x.startswith(('4.5.b', '4.7.b'))]
    return ' and '.join(SID + x for x in near) or 'the statement\'s section %s' % sec

for _i in _IDS:
    r = P[_i]
    if r.get('aaw') and r.get('aad'):
        continue
    q = r.get('q', 'Where does the course show this, and what evidence would you point to?')
    cite = CITE % _loc(_i)
    lv = LEVELS.get(r['level'], 'the level of the award it is applied to')
    if _i in ROW:
        rowk, rung = ROW[_i]
        if _i.startswith('4.5.b'):
            below = GRADE.get(_i); above = next((x for x, y in GRADE.items() if y == _i), None)
            pair = ' and '.join(SID + x for x in (below, above) if x)
            r['aaw'] = (f"Write about this as the {rung.replace('-', ' ')} level of Table 1, the least a graduate shows for {'an' if rung == 'very-good' else 'a'} {CLASS[rung]} honours degree in Accounting at {lv}: {r['about']}. "
                        f"Cite it as {cite}. Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. "
                        f"Set it beside {pair}, the Annex D band qaa/fheq-2024/annex-d/{ANNEX[rowk]}/{BAND[rung]} and the descriptor {FW_ROW[rowk]} at spine:6.")
            avoid = ('Make clear that this is the floor for any honours award, not the target.' if rung == 'threshold'
                     else 'Never present this level as what is needed simply to pass.')
            r['aad'] = (f"Raise it when a student asks what {CLASS[rung]} work looks like in {r['about']}, or when markers calibrate between classes. "
                        f"Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. "
                        f"Ask: {q} {avoid}")
        else:
            hb = ' and '.join(SID + x for x in HONROW[rowk])
            r['aaw'] = (f"Write about this as the threshold standard for {_awd(r)} at {lv}: {r['about']}. "
                        f"Cite it as {cite}. Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. "
                        f"Set it beside {hb}, which it builds on, and the master's descriptor {FW_ROW[rowk]} at spine:7.")
            r['aad'] = (f"Raise it when a master's student or course team asks what the minimum looks like for {r['about']}. "
                        f"Put it in plain words to a student, and to staff as the floor the award type sets. "
                        f"Ask: {q} Do not read the table cell aloud at length or apply another master's type's column.")
        continue
    fw = FW.get((r['level'], r['domain']), 'the honours and master\'s descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7')
    if r['addressee'] == 'provider':
        r['aaw'] = (f"Write about this as {FORCEW[r['force']]} on the course and its team, on {r['about']}, holding for {_awd(r)}. "
                    f"Cite it as {cite}. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. "
                    f"Set it beside {_nb(_i)}, and where it shapes outcomes beside {fw}.")
        r['aad'] = (f"Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to {r['about']}. "
                    f"Frame it for staff as {FORCEW[r['force']]}, and ask: {q} "
                    f"Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve.")
    else:
        r['aaw'] = (f"Write about this as {FORCEW[r['force']]} for {_awd(r)}, at {lv}, on {r['about']}. "
                    f"Cite it as {cite}. Do not claim it is a regulatory requirement or that it sets the standard at another level. "
                    f"Set it beside {_nb(_i)} and the framework descriptor {fw}.")
        r['aad'] = (f"Bring it up when a student asks about {r['about']}, or when staff check a module or outcome against it. "
                    f"Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as {FORCEW[r['force']]}. "
                    f"Ask: {q} Avoid long quotation of the issuer's text.")

# =============================================================== front matter and sections
META = dict(
    run='0082', p1='2026-10-03 16:21',
    title='Subject Benchmark Statement Accounting', heading='Subject Benchmark Statement: Accounting (QAA, April 2025)',
    edition='April 2025 (fifth edition)', published='2025-04',
    status='current', supersedes='the Accounting statement of 2019 (a minor update of 2016 and earlier editions; dates from the advisory group lists, back matter)',
    subjects=[dict(scheme='hecos', code='100105', label='accounting', basis='stated'),
              dict(scheme='hecos', code='100104', label='accountancy', basis='stated'),
              dict(scheme='cah', code='CAH17-01-08', label='accounting', basis='stated'),
              dict(scheme='hecos', code='100831', label='taxation', basis='stated'),
              dict(scheme='hecos', code='100840', label='audit management', basis='inferred'),
              dict(scheme='hecos', code='100836', label='management accountancy', basis='inferred'),
              dict(scheme='hecos', code='100107', label='finance', basis='inferred')],
    awards=[HON, ADV, CONV, PROF, INT], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, fifth edition series with cross-cutting themes (published 10 April 2025)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what an Accounting graduate should know, understand and be able to do, for the honours degree and for four kinds of taught master's "
                     "(advanced or specialist, conversion, professional, integrated). Reach for it when designing, approving, reviewing or describing an Accounting course, its outcomes "
                     "or its classification boundaries. Its honours standards run on four levels (threshold, typical, very good, excellent), one per degree class; its master's standards are "
                     "threshold only. It is not a regulatory requirement, not an accrediting body's syllabus and not a mark scheme."),
    summary=("Published by QAA on 10 April 2025, the statement covers Accounting and Accounting with another subject at undergraduate and master's levels, including Accounting with a "
             "significant finance element but not single honours finance. It sets the subject's purposes (accounting as social, economic and governance practice, beyond profit), five "
             "cross-cutting themes (EDI, accessibility, education for sustainable development, employability with enterprise and entrepreneurship, and generative AI), the distinctive "
             "features of design, progression, flexibility, partnership and review, twelve broad areas of knowledge and twelve graduate skills, and standards in two tables: Table 1 "
             "for honours at four levels tied to degree classes and to Annex D, and Table 2 for the threshold of four master's types. It names the PSRBs (the accountancy institutes in "
             "Appendix 1) as partners whose accreditation must not narrow the degree."),
    authority='reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; part of quality arrangements in Scotland, Wales and Northern Ireland (D1, Relationship to legislation)')

S2 = dict(
    governs="what can be expected of a graduate in Accounting, or Accounting with another subject, at honours and taught master's level, and the nature of awards in the subject (D1, front matter; 1.1; 4.1)",
    awards=["bachelor's degrees with honours, including joint honours and degree apprenticeships (1.3, 1.15, 2.14)", ADV, CONV, PROF, INT],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    howUsed=['design', 'approval', 'review', 'other: external examining (2.32); PSRBs (front matter); prospective students and employers (front matter)'],
    doesNot="it does not prescribe teaching, learning or assessment, interpret legislation or carry statutory or regulatory requirements; it does not cover single honours finance (1.2) or research master's programmes (1.16 d) (D1, front matter)",
    statedScope='"The purpose of this Statement is to articulate what is to be expected of successful graduates in Accounting, or Accounting with another subject, at undergraduate and master\'s levels." (D1, 1.1)',
    statedSubjects=[
        dict(name='Accounting', locator='(D1, title; 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100105', label='accounting'), dict(scheme='cah', code='CAH17-01-08', label='accounting')]),
        dict(name='Accountancy', locator='(D1, 1.1)', kind='programme title', codes=[dict(scheme='hecos', code='100104', label='accountancy')]),
        dict(name='Accounting and Finance', locator='(D1, 1.1; 1.2)', kind='programme title', codes=[dict(scheme='hecos', code='100105', label='accounting'), dict(scheme='hecos', code='100107', label='finance')]),
        dict(name='Accounting and Financial Management', locator='(D1, 1.1)', kind='programme title', codes=[dict(scheme='hecos', code='100105', label='accounting'), dict(scheme='hecos', code='100832', label='financial management')]),
        dict(name='Accounting and Data Analytics', locator='(D1, 1.1)', kind='programme title', codes=[dict(scheme='hecos', code='100105', label='accounting')]),
        dict(name='Accounting and Business Analysis', locator='(D1, 1.1)', kind='programme title', codes=[dict(scheme='hecos', code='100105', label='accounting')]),
        dict(name='Accounting and Sustainability', locator='(D1, 1.1)', kind='programme title', codes=[dict(scheme='hecos', code='100105', label='accounting')]),
        dict(name='Audit and assurance', locator='(D1, 3.10 h)', kind='specialism', codes=[dict(scheme='hecos', code='100840', label='audit management')]),
        dict(name='Taxation', locator='(D1, 3.10 i)', kind='specialism', codes=[dict(scheme='hecos', code='100831', label='taxation')]),
        dict(name='strategic management accounting', locator='(D1, 3.10 e)', kind='specialism', codes=[dict(scheme='hecos', code='100836', label='management accountancy')]),
        dict(name='sustainability accounting, carbon accounting, forensic accounting, data analytics', locator='(D1, 1.16 a)', kind='specialism', codes=[])])

SECTIONS = {'1': 'Context and purposes of an Accounting degree', '2': 'Distinctive features of the Accounting degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark Standards'}
SUB = [('1.1', '1.3', 'Context and purposes of an Accounting degree'), ('1.4', '1.18', 'Purposes and characteristics of an Accounting degree'),
       ('1.19', '1.28', 'Equality, diversity and inclusion'), ('1.29', '1.32', 'Accessibility and the needs of disabled students'),
       ('1.33', '1.43', 'Education for sustainable development'), ('1.44', '1.48', 'Employability, enterprise and entrepreneurship education'),
       ('1.49', '1.55', 'Generative artificial intelligence'), ('2.1', '2.6', 'Design'), ('2.7', '2.15', 'Progression'), ('2.16', '2.22', 'Flexibility'),
       ('2.23', '2.27', 'Partnership'), ('2.28', '2.33', 'Monitoring and review'), ('3.1', '3.1', 'Content, structure and delivery'),
       ('3.2', '3.11', 'Knowledge, understanding and subject-specific skills'), ('3.12', '3.15', 'Transferable, professional and practice skills'),
       ('3.16', '3.26', 'Learning and teaching'), ('3.27', '3.43', 'Assessment'), ('4.1', '4.2', 'Introduction'), ('4.3', '4.5', 'Undergraduate awards'),
       ('4.6', '4.8', "Master's awards")]

G = {
 '1.1': 'purpose of the statement; typical course titles', '1.2': 'finance content; joint Accounting and finance', '1.3': 'Accounting in joint honours',
 '1.4': 'purpose: accounting in society and governance', '1.5': 'students study for different reasons', '1.6': 'accounting systems and the social sciences',
 '1.7': 'the contested space between academy and PSRBs', '1.8': 'technical focus at the cost of breadth falls short', '1.9': 'preparing for a changing future',
 '1.10': 'judgement under uncertainty at the core', '1.11': 'systems that provide data and information', '1.12': 'automation and AI raise the bar for thinking',
 '1.13': 'critique of the status quo; other futures', '1.14': 'conceptual and applied study as a minimum', '1.15': 'apprenticeship degrees judged alike',
 '1.16': "four master's types (a to d)", '1.17': "self-directed research in every master's", '1.18': "the integrated master's",
 '1.19': 'EDI defined; embedded everywhere', '1.20': 'principles for an inclusive community', '1.21': 'EDI, the SDGs and reporting',
 '1.22': 'diverse content and critique', '1.23': 'examples of diversifying content', '1.24': 'EDI by area of content',
 '1.25': 'inclusive design and assessment', '1.26': 'inclusive pedagogies', '1.27': 'institutional EDI support', '1.28': 'monitoring EDI',
 '1.29': 'widening access; anticipating needs', '1.30': 'accessibility requirements and practices', '1.31': 'proactive design; attainment gaps',
 '1.32': 'equal access to placements and activities', '1.33': 'sustainability in its broad sense', '1.34': 'accounting for a sustainable transition',
 '1.35': 'accounting as catalyst for change', '1.36': 'graduate knowledge for sustainable development', '1.37': 'ethical responsibility in how one accounts',
 '1.38': 'leading the sustainability agenda', '1.39': 'accounting as performative practice', '1.40': 'current sustainability priorities',
 '1.41': 'sustainability data in systems', '1.42': 'critical enquiry on planetary limits', '1.43': 'sustainability throughout the curriculum',
 '1.44': 'enterprise and entrepreneurship defined', '1.45': 'critical thinkers who act on ideas', '1.46': 'enterprise skills through core content',
 '1.47': 'experiential approaches to enterprise', '1.48': 'co-creating enterprise curricula', '1.49': 'GenAI defined; five areas of impact',
 '1.50': 'automation raises the value of judgement', '1.51': 'GenAI in practice and skills', '1.52': 'bias in AI', '1.53': 'GenAI for learning',
 '1.54': 'GenAI and assessment design', '1.55': 'integrity policies for GenAI',
 '2.1': 'design aims', '2.2': 'objectives aligned to section 3', '2.3': 'higher-order skills and lifelong learning', '2.4': 'many career routes',
 '2.5': 'accreditation not at the cost of breadth', '2.6': 'coverage in joint degrees', '2.7': 'progressive attainment through levels',
 '2.8': 'prerequisites and credit', '2.9': 'typical length by nation', '2.10': 'joint honours progression', '2.11': 'progression and individual needs',
 '2.12': 'honours as a basis for careers', '2.13': 'readiness for postgraduate study', '2.14': 'degree apprenticeship progression',
 '2.15': 'exit awards', '2.16': 'adaptable courses', '2.17': 'inclusive flexibility of mode', '2.18': 'options and micro-credentials',
 '2.19': 'multiple learning modes', '2.20': 'flexible assessment for EDI', '2.21': 'coherence within flexibility', '2.22': 'partnership as flexibility',
 '2.23': 'standards across partnerships', '2.24': 'examples of partnership', '2.25': 'strategic and structural partnerships',
 '2.26': 'PSRBs as partners', '2.27': 'networks and learned societies', '2.28': 'external reference points in review', '2.29': 'externality',
 '2.30': 'advisory boards', '2.31': 'monitoring the themes', '2.32': 'external examining', '2.33': 'PSRB monitoring; informing students',
 '3.1': 'courses map the areas to modules', '3.2': 'content follows section 1', '3.3': 'public interest role', '3.4': 'critical, social science grounding',
 '3.5': 'many kinds of organisation', '3.6': 'conceptual and applied', '3.7': 'why rules exist and their critique', '3.8': 'beyond numbers',
 '3.9': 'core accounting-specific skills', '3.10': 'twelve broad areas of knowledge (a to l)', '3.11': 'optional modules',
 '3.12': 'skills follow section 1', '3.13': 'skills that put knowledge to work', '3.14': 'skills used together; where subject skills sit',
 '3.15': 'twelve graduate skills (m to x)', '3.16': 'learning and teaching strategy', '3.17': 'alignment and balance', '3.18': 'employability and citizenship',
 '3.19': 'pedagogies for deep learning', '3.20': 'varied, active approaches', '3.21': 'innovative methods', '3.22': 'digital technologies in teaching',
 '3.23': 'inclusive, accessible teaching', '3.24': 'research and practice in teaching', '3.25': 'responsive strategy; staff development',
 '3.26': 'reviewing teaching', '3.27': 'robust summative assessment', '3.28': 'formative assessment', '3.29': 'balanced portfolio',
 '3.30': 'no avoiding critical elements', '3.31': 'depth, not rote', '3.32': 'assessment for independent learners', '3.33': 'inclusive assessment',
 '3.34': 'assessment as dialogue', '3.35': 'clear schemes and workload', '3.36': 'timely criteria and rubrics', '3.37': 'typical assessment methods',
 '3.38': 'individual or group modes', '3.39': 'fair group assessment', '3.40': 'synchronous and asynchronous assessment', '3.41': 'peer assessment safeguards',
 '3.42': 'GenAI and assessment', '3.43': 'GenAI policies communicated',
 '4.1': 'what the standards set out', '4.2': 'not competence standards', '4.3': 'four levels and their classes', '4.4': 'most exceed the threshold',
 '4.5': 'Table 1: honours standards by level', '4.6': "basis of the master's standards", '4.7': "Table 2: master's types and standards",
 '4.8': "master's classifications left to institutions; Table 2 follows"}
CTYPE = {'3.9': 'area', '3.10': 'area', '3.15': 'area', '1.16': 'stem', '1.23': 'stem', '1.24': 'stem', '1.30': 'stem', '2.24': 'stem', '3.37': 'stem',
         '4.3': 'stem', '3.19': 'practice', '3.20': 'practice', '3.21': 'practice', '3.22': 'practice', '3.28': 'practice', '3.31': 'practice',
         '3.34': 'practice', '3.37': 'practice', '3.39': 'practice', '3.41': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='section heading lines 1 to 4', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for SB6 shared documents'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: back matter, read for S8 (earlier editions 2019, 2014, 2007, 2000)'),
    dict(number='7', heading='Appendices', kind='other: back matter, read for SB5 (Appendix 1 PSRBs) and SB6 (Appendix 2 learned societies)')]

TH = {}
for _i in ('1.19', '1.20', '1.21', '1.22', '1.25', '1.28'): TH[_i] = 'theme:edi'
for _i in ('1.29', '1.30', '1.31', '1.32'): TH[_i] = 'theme:accessibility'
for _i in ('1.33', '1.34', '1.35', '1.36', '1.38', '1.39', '1.40', '1.41', '1.42', '1.43'): TH[_i] = 'theme:esd'
for _i in ('1.44', '1.45', '1.46'): TH[_i] = 'theme:enterprise'
for _i in ('1.51', '1.52', '1.53', '1.54', '1.55'): TH[_i] = 'theme:genai'

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.7; 2.14; Table 1 (honours)'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.7; 2.14'),
                  dict(id='fheq:7', role='cites', locator="D1, 2.7; 2.13 (integrated master's); Table 2 read as master's (inferred for the taught master's types)"),
                  dict(id='fqheis:11', role='cites', locator='D1, 2.7; 2.13')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis="stated (D1, 2.7; 2.14: honours at FHEQ Level 6, FQHEIS Level 10)"),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.7; 2.13: integrated master's at FHEQ Level 7, FQHEIS Level 11)"),
                      dict(**{'from': 'Table 1 levels'}, to='Annex D classes', relation='thresholdAt', basis='stated (D1, 4.3: threshold = 3rd or pass, typical = 2:2, very good = 2:1, excellent = 1st)')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['front matter', '1.19', '1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28', '1.38', '2.1', '2.20', '2.24', '2.30', '2.31', '3.10', '3.15', '3.23', '3.29', '3.33', '3.41']),
      dict(id='theme:accessibility', role='carries', carriedIn=['front matter', '1.29', '1.30', '1.31', '1.32', '2.1', '2.19', '2.31', '3.23', '3.33']),
      dict(id='theme:esd', role='carries', carriedIn=['front matter', '1.1', '1.2', '1.3', '1.4', '1.11', '1.13', '1.14', '1.16', '1.21', '1.33', '1.34', '1.35', '1.36', '1.38', '1.39', '1.40', '1.41', '1.42', '1.43', '2.1', '2.6', '2.24', '2.31', '3.4', '3.8', '3.10', '3.15', '4.5', '4.8']),
      dict(id='theme:enterprise', role='carries', carriedIn=['front matter', '1.38', '1.44', '1.45', '1.46', '1.47', '1.48', '2.4', '2.31', '3.15']),
      dict(id='theme:genai', role='carries', carriedIn=['front matter', '1.12', '1.23', '1.49', '1.50', '1.51', '1.52', '1.53', '1.54', '1.55', '2.2', '2.31', '3.10', '3.15', '3.22', '3.34', '3.42', '3.43'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-accounting-2019-benchmarks (not held)', note='the 2025 statement lists key changes from the previous one; advisory groups are named for 2019 (minor update), 2014, 2007 and 2000 (back matter)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='4.3: the honours levels are informed by Annex D\'s four classification descriptions; cited as QAA (2024a) in the references'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 6 and 7 (2.7, 2.13, 2.14)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 10 and 11 (2.7, 2.13, 2.14)'),
      dict(rel='readWith', target='std:doc:qaa-finance-2025-benchmarks (not yet ingested)', note='1.2 and 3.10 l: single honours finance and the content of finance topics are in the Finance statement; joint courses draw on both'),
      dict(rel='refersTo', target="QAA Master's Degree Characteristics Statement (not ingested)", note="4.6: the master's standards are informed by it"),
      dict(rel='refersTo', target='QAA Quality Code (2024), Advice and Guidance: Partnerships (not ingested)', note='front matter; 2.23'),
      dict(rel='refersTo', target='QAA Characteristics Statement: Micro-credentials (2022) (not ingested)', note='2.18'),
      dict(rel='themeReference', target='std:doc:qaa-enterprise-2018-guidance', note='listed in the references (back matter); the enterprise theme, 1.44 to 1.48'),
      dict(rel='themeReference', target='std:doc:qaa-advancehe-esd-2021-guidance', note='listed in the references (back matter); the sustainability theme, 1.33 to 1.43'),
      dict(rel='refersTo', target='PSRB accreditation requirements (Appendix 1 bodies; not yet ingested)', note='1.7, 2.5, 2.26, 2.33')]
S8 = dict(published='2025-04', lastReviewed='none-stated', reviewCycle='none-stated',
          consultation='none-stated; the advisory group includes PSRB and employer representatives (back matter)', replacedBy='none')

SB1 = ['Accounting is studied as a social, economic and governance practice, a main form of information and control in every kind of organisation, not only as the measurement of profit and capital (D1, 1.4, 3.4, 3.5).',
       'It joins the conceptual (theory and its social, sustainability, political and economic context) and the applied and technical; both are a floor (D1, 1.14, 3.6).',
       'Judgement under uncertainty, ethics, professional scepticism and integrity in weighing evidence are at its core (D1, 1.10, 3.10 c, 3.10 h).',
       'It sits in a contested space between academic study and the accountancy bodies\' professional requirements; the statement, not accreditation, sets the degree (D1, 1.7, 1.8, 2.5, 2.26).',
       'Data and the systems that produce it are central, from double entry to ERP, analytics and AI (D1, 1.11, 3.10 f, 3.10 k).',
       'It looks forward: critical of current accounting, imagining other futures, sustainability accounting foremost, and preparing for rules that change within a career (D1, 1.9, 1.13, 3.3, 3.7).',
       "Master's study comes in four taught types (advanced or specialist, conversion, professional, integrated), each with self-directed research-based inquiry; research master's are outside the statement (D1, 1.16, 1.17, 1.18)."]

SB2 = [dict(theme='theme:edi', inThisSubject='diverse and decolonised content, critique of dominant approaches, EDI applied area by area (governance, reporting, decisions, tax, audit, finance, economics), inclusive assessment and safeguards in peer marking (D1, 1.19 to 1.28, 3.41)',
            statements=['1.19', '1.20', '1.21', '1.22', '1.25', '1.28', '3.41']),
       dict(theme='theme:accessibility', inThisSubject='legal requirements as the minimum across the student journey, anticipatory adjustments, attainment gap investigation, equal access to placements and abroad study (D1, 1.29 to 1.32, 3.33)',
            statements=['1.29', '1.30', '1.31', '1.32', '3.33']),
       dict(theme='theme:esd', inThisSubject='sustainability in its broadest sense, wider than ESG disclosure; accounting as catalyst for change (double materiality, net zero, modern slavery, carbon), sustainability data in systems, and graduates able to lead the agenda (D1, 1.33 to 1.43, 3.10 g)',
            statements=['1.33', '1.34', '1.35', '1.36', '1.38', '1.39', '1.40', '1.41', '1.42', '1.43']),
       dict(theme='theme:enterprise', inThisSubject='enterprise and entrepreneurship as employability and personal development, built through the core content and research-led teaching, and graduate entrepreneurialism with regard to the public interest (D1, 1.44 to 1.48, 3.15 v)',
            statements=['1.44', '1.45', '1.46', '3.15.b10']),
       dict(theme='theme:genai', inThisSubject='a fifth theme of its own: GenAI in accounting practice, bias in AI, GenAI for learning and the redesign of assessment and integrity policy (D1, 1.49 to 1.55, 3.42, 3.43)',
            statements=['1.51', '1.52', '1.53', '1.54', '1.55', '3.42', '3.43'])]

SB3 = dict(areas=[dict(component='3.9', gloss='core accounting-specific skills: recording, statements, operational and financial analysis'),
                  dict(component='3.10', gloss='twelve broad areas a to l: accountability and trust; environment; ethics; governance and reporting; decision information; systems and data; regulation; audit and assurance; taxation; uncertainty and risk; analytics and statistics; financial markets'),
                  dict(component='3.15', gloss='twelve graduate skills m to x: communication; collaboration; self-efficacy; critical thinking; problem solving; data analysis; systems thinking; digital literacy; numeracy; entrepreneurialism; cultural awareness; research')],
           practices=[dict(component='3.19', kind='teaching', gloss='dialogic, critical, reflexive, constructivist and collaborative pedagogies for deep learning'),
                      dict(component='3.20', kind='teaching', gloss='lectures, seminars, workshops, tutorials, blended and active learning'),
                      dict(component='3.21', kind='learning', gloss='games, simulations, authentic and experiential learning, cases, role play, practitioners'),
                      dict(component='3.22', kind='learning', gloss='cloud accounting, analytics tools, spreadsheets, AI'),
                      dict(component='3.28', kind='assessment', gloss='formative assessment and feedback'),
                      dict(component='3.31', kind='assessment', gloss='critical, authentic, case-based assessment; limits on multiple choice'),
                      dict(component='3.34', kind='assessment', gloss='dialogues of learning; inner feedback by comparison'),
                      dict(component='3.37', kind='assessment', gloss='fifteen typical methods, from examinations to capstone projects'),
                      dict(component='3.39', kind='assessment', gloss='team and group assessment'),
                      dict(component='3.41', kind='assessment', gloss='peer discussion and review with safeguards')])

_OUT = [('critical, ethical and contextual knowledge', 1, 'knowledge'), ('theory in critical discussion', 2, 'understanding'),
        ('knowledge across the broad areas', 9, 'knowledge'), ('integration across the areas', 10, 'understanding'),
        ('transferable and professional skills', 17, 'generic-skill'), ('building arguments', 18, 'generic-skill'),
        ('application to problems', 25, 'subject-skill')]
_outs = []
for name, b, dom in _OUT:
    step = 1 if b == 25 else 2
    ids = ['4.5.b%d' % (b + step * j) for j in range(4)]
    _outs.append(dict(outcome=name, threshold=ids[0], typical=ids[1], veryGood=SID + ids[2], excellent=ids[3], basis='inferred', domain=dom, award=HON))
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.5', award=HON, items=7, label='Threshold (3rd or pass)'),
           dict(rung='typical', leadIn='4.5', award=HON, items=7, label='Typical (2:2)'),
           dict(rung='very-good', leadIn='4.5', award=HON, items=7, label='Very good (2:1)'),
           dict(rung='excellent', leadIn='4.5', award=HON, items=7, label='Excellent (1st)'),
           dict(rung='threshold', leadIn='4.7', award=MAS, items=27, label="Table 2: Master's degree benchmark standards (threshold level)")],
    rungBases="4.3 defines each honours level as the least shown by every graduate in its class (threshold 3rd or pass, typical 2:2, very good 2:1, excellent 1st), informed by Annex D; 4.5 names four bases of difference: depth of mastery, breadth of mastery, integration of mastery and mastery of application; higher levels include all lower ones. Table 2 sets threshold only for four master's types; merit and distinction are left to institutions (4.8).",
    outcomeLists=[dict(leadIn='3.15', gloss='twelve graduate skills on completing the degree (m to x)', items=12, award=[HON]),
                  dict(leadIn='3.10', gloss='twelve broad areas of knowledge, understanding and in situ skills courses include (a to l)', items=12, award=['all Accounting degrees'])],
    outcomes=_outs)
SB4A_FULL = []

_APP1 = [('Association of Chartered Certified Accountants (ACCA)', ['appendix 1', 'back matter: advisory group']),
         ('Association of International Accountants (AIA)', ['appendix 1']), ('Chartered Accountants Ireland (CAI)', ['appendix 1', 'back matter: advisory group']),
         ('Chartered Institute of Public Finance and Accountancy (CIPFA)', ['appendix 1']), ('AICPA & CIMA', ['appendix 1']),
         ('Financial Reporting Council (FRC)', ['appendix 1']), ('IFRS Foundation', ['appendix 1']),
         ('Institute of Chartered Accountants in England and Wales (ICAEW)', ['appendix 1', 'back matter: advisory group']),
         ('Institute of Chartered Accountants of Scotland (ICAS)', ['appendix 1', 'back matter: advisory group']),
         ('Institute of Financial Accountants (IFA)', ['appendix 1']), ('International Federation of Accountants (IFAC)', ['appendix 1']),
         ('Association of Accounting Technicians (AAT)', ['appendix 1']), ('Accounting Technicians Ireland (ATI)', ['appendix 1'])]
SB5 = [dict(body='professional, statutory and regulatory bodies (PSRBs), chiefly the accountancy bodies',
            says='potential partners in design whose accreditation and exemptions many students seek; degrees sit in a contested space with them; courses must not be built for exemptions at the cost of broader aims and should meet the statement rather than PSRB-prescribed content; they monitor accredited courses; their requirements may inform competence standards (D1, front matter, 1.7, 1.8, 1.16 c, 1.38, 1.48, 2.5, 2.16, 2.23, 2.26, 2.33, 3.43, 4.2)',
            requirements='not yet ingested (Part E)')]
SB5 += [dict(body=b, says='listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)', requirements='not yet ingested (Part E)') for b, _ in _APP1]
SB5 += [dict(body='Equality and Human Rights Commission', says='providers writing competence standards should follow its latest guidance (D1, 4.2)', requirements='not-applicable-by-design: guidance, not course requirements'),
        dict(body='Office for Students', says='in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)', requirements='not-applicable-by-design')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion (front matter: equity, diversity, and inclusion)', carriedIn=S6[0]['carriedIn'],
                 statements=[SID + x for x in SB2[0]['statements']]),
            dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=S6[1]['carriedIn'],
                 statements=[SID + x for x in SB2[1]['statements']]),
            dict(id='theme:esd', named='Education for sustainable development', carriedIn=S6[2]['carriedIn'],
                 statements=[SID + x for x in SB2[2]['statements']]),
            dict(id='theme:enterprise', named='Employability, enterprise and entrepreneurship education', carriedIn=S6[3]['carriedIn'],
                 statements=[SID + x for x in SB2[3]['statements']]),
            dict(id='theme:genai', named='Generative artificial intelligence (new theme id: Part E)', carriedIn=S6[4]['carriedIn'],
                 statements=[SID + x for x in SB2[4]['statements']])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.7', '2.13', '2.14', '4.3']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.7', '2.13', '2.14'])],
    bodies=[dict(body='PSRBs (generic)', citedIn=['front matter', '1.7', '1.8', '1.16', '1.38', '1.48', '2.5', '2.16', '2.23', '2.26', '2.33', '3.43', '4.2', '4.8'])] +
           [dict(body=b, citedIn=c) for b, c in _APP1] +
           [dict(body='Equality and Human Rights Commission', citedIn=['4.2']), dict(body='Office for Students', citedIn=['front matter'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.3', 'back matter: references'], role='the four classification descriptions the honours levels are informed by'),
        dict(document='std:doc:qaa-finance-2025-benchmarks (not yet ingested: Part E)', named='Subject Benchmark Statement for Finance', citedIn=['1.2', '3.10'], role='covers single honours finance and details finance topics'),
        dict(document="QAA Master's Degree Characteristics Statement (not ingested: Part E)", named="QAA Master's Degree Characteristics Statement", citedIn=['4.6'], role="informs the master's standards"),
        dict(document='QAA Quality Code 2024 (not ingested)', named='Quality Code; UK Quality Code, Advice and Guidance: Partnerships', citedIn=['front matter', '2.23'], role='sector reference point; partnership guidance'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='QAA Characteristics Statement: Micro-credentials (2022) (not ingested)', named='micro-credentials (QAA, 2022)', citedIn=['2.18'], role='flexible credit options'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (2018)', citedIn=['back matter: references'], role='the enterprise theme'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development Guidance (QAA and Advance HE, 2021)', citedIn=['back matter: references'], role='the sustainability theme'),
        dict(document='QAA advice on Generative AI (2023) (not ingested)', named='Maintaining quality and standards in the ChatGPT era', citedIn=['back matter: references'], role='the GenAI theme'),
        dict(document='UN Sustainable Development Goals (external)', named='UN Sustainable Development Goals', citedIn=['1.21', '1.24', '1.33', '1.34'], role='frame for EDI and sustainability'),
        dict(document='UN Principles of Responsible Management Education (external)', named='UN Principles of Responsible Management Education (PRME)', citedIn=['1.34', 'appendix 2'], role='frame for sustainability'),
        dict(document='Equality Act 2010 (law)', named='Equality Act 2010', citedIn=['4.2'], role='defines competence standards')])

B1 = [dict(slug='enterprise-and-entrepreneurship-education', definition="developing students' capacity to generate ideas and the behaviours, attributes and competencies to realise them (D1, 1.44)", beneficiaryDefinition='learning to come up with ideas and make them happen', scopeNote='entrepreneurship is the applying of these to create cultural, social or economic value (1.44)', category='unknown', practices=['education']),
      dict(slug='generative-ai', definition='AI algorithms that produce content from prompts, built on a probability model of their training data (D1, 1.49)', beneficiaryDefinition='AI tools that write or make content when you ask them', scopeNote='the fifth cross-cutting theme', category='unknown', practices=['education', 'accounting']),
      dict(slug='self-efficacy', definition="the ability to act and belief in one's own ability, with reflection and commitment to independent action (D1, 3.15 o)", beneficiaryDefinition='believing you can do something and acting on it', scopeNote='tied to self-managed lifelong learning', category='unknown', practices=['education']),
      dict(slug='systems-thinking', definition='a way of seeing processes as interconnected systems and understanding the structures beneath complex situations (D1, 3.15 s)', beneficiaryDefinition='seeing how the parts of a process connect', scopeNote='applied to accounting and control systems', category='unknown', practices=['accounting']),
      dict(slug='conceptual-study', definition='theoretical accounting with its social, sustainability, political and economic considerations (D1, 1.14)', beneficiaryDefinition='the theory and wider context of accounting, as against its techniques', scopeNote='with applied study, a minimum for the degree', category='unknown', practices=['accounting']),
      dict(slug='straightforward-and-structured-problem', definition='a bounded problem whose key data and methods are well known, mainly quantitative and fairly certain (D1, Table 1 note)', beneficiaryDefinition='a problem with clear edges, known methods and mostly numerical data', scopeNote='higher levels deal with less bounded, more ambiguous, judgement-based problems', category='unknown', practices=['education']),
      dict(slug='honours-achievement-levels', definition='four levels, each the least shown by every graduate in a degree class: threshold (3rd or pass), typical (2:2), very good (2:1), excellent (1st) (D1, 4.3)', beneficiaryDefinition='what you need at the least for each class of honours degree', scopeNote='very good is a fourth level beyond the three most statements use', category='unknown', practices=['education'])]
B2A = [dict(concept='enterprise-and-entrepreneurship-education', form='enterprise and entrepreneurship education', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='generative-ai', form='Generative AI', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='generative-ai', form='GenAI', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
       dict(concept='self-efficacy', form='self-efficacy', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
       dict(concept='systems-thinking', form='systems thinking', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='conceptual-study', form='conceptual', lang='en', partOfSpeech='adjective', termStatus='preferred', register='discipline-specific'),
       dict(concept='straightforward-and-structured-problem', form='straightforward and structured', lang='en', partOfSpeech='adjective', termStatus='preferred', register='formal'),
       dict(concept='honours-achievement-levels', form='Very good', lang='en', partOfSpeech='adjective', termStatus='preferred', register='formal')]
B4 = [dict(rel='contrasts-with', **{'from': 'straightforward-and-structured-problem'}, to='honours-achievement-levels', note='Table 1 note: the higher levels deal with less bounded, more uncertain problems')]
B5 = []
D3 = [dict(citation='QAA (2025) Subject Benchmark Statement: Finance', settles=['SB6', 'S7'], asked='2026-10-03', state='held by stan, not yet ingested (S-02)'),
      dict(citation="QAA Master's Degree Characteristics Statement", settles=['SB6', 'S7', 'S5'], asked='2026-10-03', state='wanted')]

E = [
 'SB4, rungs: four honours levels, not three: threshold (3rd or pass), typical (2:2), very good (2:1), excellent (1st) (4.3). `very-good` is recorded as a rung value the template does not yet list (threshold, typical, excellent, none): for a template ruling. SB4 `outcomes` carries it as `veryGood`.',
 'SB4, shape: the honours standards are one table (Table 1, 4.5) of four categories by four levels; three categories hold two sentences per cell, recorded as two S4 records each (a knowledge sentence and an ability sentence), so seven outcomes at four levels (28 records, 4.5.b1 to b28 in reading order). Table 2 (4.7; it follows 4.8 in the text) gives master\'s standards at threshold only for four master\'s types (27 records, 4.7.b1 to b27).',
 'SB4, gradeOf: Table 1 pairs each cell with the next level in the same row, so each link (21) is plain; the builder writes `basis: inferred` throughout. Candidate for `stated` at P3. Master\'s cells take no gradeOf: Table 2 has threshold only.',
 'S4, force: every table cell takes force `threshold`, since 4.3 defines each level as "the minimum to be achieved by all graduates" in its class and Table 2 is headed "(threshold level)"; the Table 1 caption also says graduates "will have achieved" these.',
 'S4, force: "is/are expected to" is not one of the five obliging words. 3.15 m to x ("a graduate is expected to have acquired skills"), 1.16 a and 1.18 are recorded as `describes` and treated as statements, as is 3.10 g, which has no modal of its own and whose lead-in "should" is too far away for the script check to see. For Abbott: should "expected to" read as `should` or `will`?',
 'S4, force: paragraphs obliging only in words outside the five were not taken as statements: 1.37 ("need to appreciate"), 2.21 and 2.29 ("essential"), 3.7 ("need to include", "is necessary"); 1.10, 1.12, 1.47, 1.48 ("might consider"), 2.7, 2.8, 2.9, 2.15, 2.18 to 2.20, 2.22, 2.24, 2.25, 2.27, 2.30, 3.1, 3.11, 3.14, 3.21, 3.38, 3.40, 4.1, 4.3, 4.6 and 4.8 are descriptive, permissive or introductory and are S3 components only.',
 'S4, list items not taken: the bullets of 1.23 ("could"), 1.24 ("might"), 1.30 ("may include"), 2.24 ("examples include") and 3.37 ("typically include") are examples under non-obliging lead-ins; the skeleton offered them as candidates. 1.30\'s own lead-in obliges and is one record (its stem). 4.3\'s four bullets are the definitions of the levels (SB4 `rungBases`), not rung items, though the skeleton marked them threshold.',
 'S4, ids: list items use the builder\'s `.b<n>` form for the issuer\'s letters: 1.16.b1 to b3 = types a to c (d, research master\'s, is out of scope and not a statement); 3.10.b1 to b12 = areas a to l; 3.15.b1 to b12 = skills m to x. The 3.10 stem is its own record.',
 'S4, 1.2: "should be aligned ... and must include": force recorded as `must`, which governs the content clause.',
 'S4, 3.10 i: "It is essential that ... equip" and "should": force `should`; "at a minimum" names the UK taxes.',
 'S4, 3.22: "it is highly likely that it will be necessary": force `will`, hedged in the issuer\'s own words.',
 'S4, levels: statements addressed to "graduates" in sections 1 to 3 with a generic-skill domain (1.38, 1.42, 1.44 to 1.46, 2.3, 3.13, 3.32, 3.15 m to x) are recorded at fheq:6 for the honours degree; they also bear on master\'s graduates. Course-wide provider duties carry level none.',
 'S4, spans: the skeleton\'s paragraph spans run on into the next sub-heading (for example 1.18 ends with "Equality, diversity and inclusion"); records here use `find` with the paragraph text alone. Page numbers inside a span (3.10 c, i, j; 3.15 r) are part of the held text and stay in `source`.',
 'S4, 1.46: the held text breaks a reference across lines ("paragraphs 1.4,\\n1.46 and 3.16-3.26"); the second "1.46" is a reference (DPN-1), not a new paragraph; the skeleton kept 1.46 whole.',
 'S6, SB6: a fifth cross-cutting theme, generative artificial intelligence, has no shared theme id; `theme:genai` is proposed here and needs adding to the shared list.',
 'S6: the front matter names the EDI theme "equity, diversity, and inclusion" and section 1 "Equality, diversity and inclusion"; the same theme.',
 'S2, subjects: HECoS 100105 accounting, 100104 accountancy, CAH17-01-08 and 100831 taxation are named by the text; 100840 audit management, 100836 management accountancy and 100107 finance are inferred (finance only for joint courses; single honours finance is out of scope, 1.2) and wait for P3.',
 'S5: the statement cites FHEQ Level 7 and FQHEIS Level 11 only for the integrated master\'s (2.7, 2.13); fheq:7 for the other master\'s types is inferred from the frameworks (std:doc:qaa-fheq-2024-framework S5, Table 1).',
 'S5, CQFW: not named; Wales appears only for course length (2.9).',
 'SB5: Appendix 1 lists 13 bodies; the AICPA & CIMA entry spells out its parent bodies. 2.23 writes "PRSBs", the issuer\'s typo for PSRBs. Appendix 2\'s learned associations (BAFA, IAFA, EAA, AAA and others; CABS listed twice) are not PSRBs and are not recorded in SB5.',
 'SB5: none of the PSRBs\' own requirements is ingested.',
 'S7, S8: the previous statement\'s date is not given in the body; the back matter names advisory groups for 2019 (minor update), 2014, 2007 and 2000, and the cover note says "Fifth Edition Published - 10 April 2025". supersedes points to a 2019 statement not held.',
 'Patterns against Psychology: four honours levels with a very good (2:1) level; standards given as tables, not lists; master\'s standards for four types at threshold only; a fifth theme (GenAI); course-design duties in "should" dominate sections 1 to 3, so most statements are provider duties (student version not applicable); outcome lists use "is expected to have acquired" rather than "are able to".',
 'S1, licence: the text gives a copyright notice and no re-use terms; QAA\'s terms for holding are to check.',
 'S9: not researched in P1.']
