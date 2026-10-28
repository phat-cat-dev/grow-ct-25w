# bm_content.py: judgement for run 0096, QAA Subject Benchmark Statement Counselling and Psychotherapy (March 2022). std run agent.
# Read by tools/bm_build.py. Keys of P are S4 ids under qaa/counselling-and-psychotherapy-2022/. All text below except `find` spans is ours.
import json as _json, re as _re

_ST = '/home/claude/wkspc2601-library/ingested/standards'   # moved to the source library (std N-0119)
_NORM = open('/home/claude/wkspc2601-library/txt/qaa-2022-counselling-psychotherapy-subject-benchmark-statement-standard.norm.txt', encoding='utf-8').read()
_SK = _json.load(open(_ST + '/ingest-std-qaa-counselling-and-psychotherapy-2022-benchmarks/run-src/bm-skel.json', encoding='utf-8'))
_CS = {c['number']: (c['start'], c['end']) for c in _SK['components']}
_HEADS = ['Purposes of Counselling and Psychotherapy', 'Equality, diversity and inclusion',
          'Sustainability Developing sustainable development knowledge', 'Developing sustainable development competencies',
          'Developing learning environments to promote sustainable development', 'Employability, enterprise and entrepreneurship education',
          'Personal development', 'Accessibility', 'Progression', 'Flexibility', 'Partnership', 'Monitoring and review', 'Theory',
          'Professional skills practice', 'Professional development', 'Research', 'Teaching and learning', 'Assessment',
          'Understanding people and their experiences', 'The therapist', 'Ethical/legal', 'Boundaries and contracting',
          'The therapeutic relationship', 'Generic skills', 'Typical level (2:2 or 2:1)', 'Excellent level (1st class)',
          'Benchmark standard for master’s degrees Generic skills', 'Benchmark standard for master’s degrees','Threshold level (3rd class) Professional context']

def _tidy(t):
    while True:
        o = t
        t = t.rstrip()
        t = _re.sub(r'\n+\d+$', '', t).rstrip()
        if t.endswith('•'):
            t = t[:-1].rstrip()
        for m in (' Be', ' Do', '\nBe', '\nDo'):
            if t.endswith(m):
                t = t[:-len(m)].rstrip()
        for h in _HEADS:
            if t.endswith(' ' + h) or t.endswith('\n' + h):
                t = t[:-len(h) - 1].rstrip()
        if t == o:
            return t

def _para(n):
    a, b = _CS[n]
    return _tidy(_NORM[a:b]), a

def _cut(n, starts):
    """items of a paragraph by their opening words: each runs to the next item's opening, tidied"""
    a, b = _CS[n]; pos = []; cur = a
    for s in starts:
        p = _NORM.index(s, cur); pos.append(p); cur = p + 1
    assert pos[-1] < b, n
    return [(_tidy(_NORM[p:(pos[k + 1] if k + 1 < len(pos) else b)]), p) for k, p in enumerate(pos)]

HON = "bachelor's with honours"
MA = "master's"
NA = ('n/a', 'a duty on the course and the people who design and run it, not a standard the student reaches')

P = {}
def s(i, find=None, after=None, **k):
    if find is None and i in _CS:
        find, after = _para(i)
    if find is not None:
        k['find'] = find; k['after'] = after if after is not None else 0
    P[i] = k

def prov(i, **k):
    d = dict(type='requirement', rung='none', force='should', level='none', appliesTo='Counselling and Psychotherapy courses',
             addressee='provider', domain='none', award='none', ben=NA)
    d.update(k); s(i, **d)

def both(i, **k):
    d = dict(type='expectation', rung='none', force='should', level='none', appliesTo='Counselling and Psychotherapy courses and their trainees',
             addressee='both', domain='none', award=[HON, MA])
    d.update(k); s(i, **d)

def lrn(i, **k):
    d = dict(type='outcome', rung='none', force='should', level='none', appliesTo='trainees on Counselling and Psychotherapy courses',
             addressee='learner', domain='subject-skill', award=[HON, MA])
    d.update(k); s(i, **d)

# =============================================================== section 1: context and purposes
both('1.4', verbs=['viewed'], domain='understanding', about='therapy settings read in their wider context',
  para="The settings where therapy happens and the services they run, from brief to long-term work with individuals, couples, families, groups or communities, should be understood against their history, culture, economics and politics.",
  prac="Teach the places of practice as shaped by history and by social, economic and political forces, not as neutral venues.",
  ben="You should learn to read any service you work in against its history, culture, economics and politics.",
  q="Pick a service you know: what history and politics shaped the therapy it offers?")
both('1.5', force='must', verbs=['considered', 'assess'], domain='subject-skill', about='choosing a mode of delivery with care',
  para="Each way of delivering therapy, in a room or remotely, live or not, carries its own protocols, risks and benefits; these must be weighed with care to find the right mix for the client, the practitioner's competence and the relationship.",
  prac="Make sure trainees learn to weigh in-person and remote modes against client need, their own competence and the relationship before choosing how to work.",
  ben="Before you choose to work in person or by video, phone or text, you must weigh the risks and benefits for that client and for your own competence.",
  q="How would you decide whether a given client is better seen in person or online?")
both('1.7', force='will', verbs=['incorporate', 'engender'], about='training that joins study, growth and a supervised placement',
  para="Training will join academic study with personal and skills development so that students can complete an assessed, supervised client placement, and it should build the UNESCO key competencies so that graduates keep learning, reflectively and reflexively, across their careers.",
  prac="Design the course so that its academic, personal and skills strands all lead towards a supervised, assessed placement, and plan where the UNESCO sustainability competencies are built.",
  ben="Your course will bring together study, personal growth and skills work to ready you for a supervised placement with clients, and should leave you able to keep learning about yourself and your practice.",
  q="Where in the course do the academic, personal and skills strands meet before placement?")
both('1.8', force='will', verbs=['provide', 'engage'], domain='subject-skill', about='what all training offers and what the competent graduate can do',
  para="Whatever its modality or mode, every course will give chances to engage with the literature, learn research methods, build client skills and grow personally and professionally; the competent graduate will be able to work effectively with clients in a safe, contracted relationship while caring for themselves.",
  prac="Check that the course gives every trainee the literature, research methods, client skills and personal growth, whatever the modality, and that graduates leave able to work safely under contract and look after themselves.",
  ben="Whatever approach you train in, you will meet the research literature, learn how research is done, build skills with clients and grow as a person; by the end you will be able to work well with clients within a safe agreement while looking after yourself.",
  q="Which of these four strands feels thinnest in your training so far?")
prov('1.10', force='describes', verbs=['value', 'incorporate'], about='experiential learning, inclusive content and authentic assessment',
  para="Courses prize experiential learning beside academic results and make room for openness and vulnerability; content tries to keep minority experience in view and to question theory rooted in majority culture; assessment needs to be authentic, accessible and tied to the work of a therapist.",
  prac="Build in experiential learning that allows vulnerability, test the curriculum for majority-culture bias, and make each assessment authentic, accessible and close to real therapeutic work.",
  q="Which assessment on the course is furthest from what a therapist actually does?")
both('1.12', force='will', verbs=['involve'], domain='understanding', about="a reflective view of the profession's sustainable future",
  para="Courses seek to build knowledge of sustainable development in the profession, setting it in its history and culture and inviting critique of its structures and dominant discourses; this will call for a reflective and reflexive attitude that imagines how the profession and its graduates can keep bringing broad benefit to people and society.",
  prac="Invite students to critique the profession's institutions and dominant ideas about mental illness, research and treatment, and to imagine how therapy can grow in ways that benefit individuals, communities and society.",
  ben="You will be asked to look critically at how your profession is organised and talked about, and to think about how it, and you, can keep doing good for people and communities over time.",
  q="What would a more sustainable future for counselling services look like where you live?")
both('1.13', force='describes', verbs=['considered', 'requires'], domain='subject-skill', about='the eight UNESCO sustainability competencies',
  para="All eight UNESCO competencies for sustainability (among them systems, anticipatory, normative and strategic thinking, collaboration, critical thought, self-awareness and joined-up problem-solving) are held to be essential; the qualified therapist needs to use them all in practice, so the learning setting and curriculum need to show them too.",
  prac="Map the eight UNESCO competencies across modules and placement, and make sure the course's own facilities and ways of working model them.",
  ben="You will need to use all eight sustainability competencies, such as systems thinking, collaboration and self-awareness, in your work as a therapist, and your course should let you see and practise them.",
  q="Which of the eight competencies can you already show an example of in your practice?")
both('1.14', force='must', verbs=['require', 'contextualise', 'promote'], about="responsibility for one's own and others' well-being as a developmental aim",
  para="Training needs facilities for adult-centred and experiential learning across digital, individual, group and community settings; courses aim to set theory and practice in their social, economic and political arena and to support employability, and fostering responsibility for one's own and others' psychological well-being must be a developmental aim.",
  prac="Provide spaces for experiential and adult learning across digital, personal, group and community settings, and make students' growing responsibility for their own and others' well-being an explicit aim of the course.",
  ben="Your course must help you grow a sense of responsibility for other people's psychological well-being and for your own.",
  q="How does the course show students that it is building their responsibility for well-being?")
lrn('1.16', verbs=['understand', 'articulate', 'demonstrate'], about='knowing and showing the value of therapeutic skills',
  para="Students should grasp both the commercial and the practical worth of their skills and be able to explain and show them to employers and in plans to work for themselves or set up a private practice; they should also be helped to see their own enterprising capacities and to use them flexibly as contexts change.",
  prac="Give students tasks that make them state the market and practical value of their therapeutic skills, for job applications and for private practice plans, and help them notice their own enterprising strengths.",
  ben="You should be able to explain and show what your skills are worth, both to an employer and in a plan for your own practice, and to notice where you are enterprising.",
  q="How would you describe the value of your skills to an agency that is hiring?")
both('1.22', verbs=['include', 'communicate', 'enhance'], about='digital competency for communication and employability',
  para="Building digital and transferable skills should include using technology to share ideas in creative, innovative and accessible ways that support study and employment.",
  prac="Set tasks in which students use digital tools to present ideas creatively and accessibly, and link them to study success and employability.",
  ben="You should learn to use digital tools to put your ideas across creatively and accessibly, in ways that help your studies and your job prospects.",
  q="Which digital tools will you need for remote client work and for finding work?")
prov('1.23', verbs=['achieved', 'embedded'], about='employability and enterprise in curriculum design',
  para="Building these professional capacities should be central to curriculum design and may run through the whole course; outcomes, activities and authentic assessment for employability and enterprise may sit in dedicated modules and across others.",
  prac="Plan employability and enterprise into the curriculum from the start, through dedicated modules, threads across modules or both, with matching outcomes and authentic assessment.",
  q="Where are employability and enterprise assessed, not just mentioned?")
prov('1.24', force='describes', verbs=['recommended', 'develop'], about='speakers from the profession and contact with agencies',
  para="Bringing in speakers from the profession and alumni is advised; meeting a range of therapists and agencies builds awareness of the working world and can help graduates handle market forces and present themselves ethically.",
  prac="Invite practitioners, agencies and alumni into teaching so that students meet the working world and learn to promote themselves ethically.",
  q="Which voices from practice do students hear before they qualify?")

# =============================================================== section 2: distinctive features
prov('2.1', force='will', verbs=['offer', 'encompass'], about='an integrated curriculum and a supervised placement in every course',
  para="Every course in scope will offer a curriculum joining theory, skills practice, personal and professional development and research, and every professional course will include a supervised placement with clients; teaching and assessment strategies are for each institution to decide.",
  prac="Confirm the course joins the five strands and contains a supervised client placement; the methods are the course team's to choose.",
  q="Where does each of the five strands appear in the course map?")
_PD = [  # 2.2: personal development enables the learner to
 ('take', 'owning one\'s learning', "Personal development should equip the learner to own their learning.", "Make students responsible for planning and reviewing their own learning.", "Your personal development work should help you take charge of your own learning.", "What have you chosen to learn beyond what was set?"),
 ('work', 'safe and ethical client work', "It should help the learner work with clients safely and ethically.", "Link personal development activities to safe, ethical client work.", "It should help you work with clients safely and ethically.", "What in your personal work has made your client work safer?"),
 ('differentiate,develop', 'telling self from client', "It should help the learner tell their own material apart from the client's and grow aware of themselves in relation to others.", "Use process work to help students separate their own reactions from the client's.", "It should help you tell your own feelings apart from your client's and see yourself in relation to others.", "How do you know whether a feeling in session is yours or the client's?"),
 ('acknowledge', 'the self as a resource', "It should help the learner see their own self as a resource in the work.", "Help students explore how they use themselves in therapy.", "It should help you see yourself as a resource in the work.", "How do you use yourself in sessions?"),
 ('be', 'awareness of personal and social identity', "It should make the learner aware of their own personal and social identity.", "Include identity work in personal development groups.", "It should help you become aware of your own personal and social identity.", "Which parts of your identity are most visible to clients?"),
 ('identify,address', 'hidden bias in self and practice', "It should help the learner find and deal with hidden biases and prejudice in themselves and their practice.", "Give students structured ways to surface and tackle implicit bias.", "It should help you find and deal with hidden biases and prejudice in yourself and your work.", "What hidden bias have you found in yourself?"),
 ('develop', 'an accurate view of own competence', "It should give the learner an accurate sense of their own competence.", "Calibrate students' self-assessment against feedback.", "It should give you a true sense of how competent you are.", "Where does your own view of your skill differ from your tutor's?"),
 ('accept,enabling', 'self-acceptance as a base for accepting clients', "It should help the learner accept themselves and so accept the client.", "Make room for self-acceptance work alongside skills training.", "It should help you accept yourself, which helps you accept your clients.", "How does accepting yourself change how you meet clients?"),
 ('recognise,foster,avoid,promote', 'a self-care strategy against burnout', "It should help the learner see why self-care matters and build a strategy that guards against burnout and supports emotional strength.", "Require a self-care plan and review it over the course.", "It should help you build a self-care plan that guards against burnout and keeps you emotionally strong.", "What is in your self-care plan, and do you follow it?"),
 ('be', 'being organised, flexible and resilient', "It should help the learner be organised, adaptable and resilient.", "Use placement demands to build organisation and resilience.", "It should help you become organised, adaptable and resilient.", "How do you recover after a hard week on placement?"),
 ('commit', 'lifelong reflection and reflexivity', "It should lead the learner to commit to building self-awareness through reflection and reflexivity for life.", "Model lifelong reflective practice in teaching and supervision.", "It should lead you to keep building self-awareness through reflection all your working life.", "How will you keep reflecting once the course ends?"),
 ('develop', 'self-awareness in wider context', "It should help the learner see themselves within a whole-person, professional and social context.", "Link personal development to the professional and social setting of practice.", "It should help you see yourself as a whole person within your profession and society.", "How does your place in society shape you as a therapist?"),
 ('be', 'tolerating uncertainty and failure', "It should help the learner cope with uncertainty, ambiguity, risk and failure.", "Let students meet uncertainty safely in experiential work.", "It should help you live with uncertainty, ambiguity, risk and failure.", "How do you respond when you do not know what to do in a session?"),
 ('be', 'sensitivity to personal values', "It should make the learner sensitive to values, including ethical, social, diversity and environmental ones.", "Explore values explicitly, including environmental ones.", "It should make you sensitive to your values, including ethical, social, diversity and environmental ones.", "Which of your values most affects your work?"),
 ('develop,apply', 'enterprising capabilities', "It should help the learner see their own enterprising capacities and apply them flexibly with motivation and discipline.", "Connect personal development to students' enterprising strengths.", "It should help you see your enterprising strengths and use them flexibly.", "Where could your enterprising strengths take your career?"),
]
for _k, (_v, _a, _p, _pr, _b, _q) in enumerate(_PD, 1):
    lrn(f'2.2.b{_k}', verbs=_v.split(','), about=_a, para=_p, prac=_pr, ben=_b, q=_q)
P['2.2.b15'].update(find='develop self -awareness of their own enterprising and entrepreneurial capabilities, as well as the motivation and self-discipline to apply these flexibly in different contexts.', after=0)

_AC = [  # 2.3: the course should strive to ensure equitable access by
 ('being', 'access in person and online', "Courses should be accessible to every student both in person and online.", "Audit both campus and online access for every student."),
 ('ensuring,support', 'resources and technology for each learner', "Courses should make sure students can get the learning resources and technology their own learning needs.", "Check that each student has the resources and devices they need."),
 ('ensuring', 'accessible curriculum and content', "Courses should make the curriculum and its content accessible.", "Review curriculum content for accessibility."),
 ('ensuring', 'an accessible, safe and private space for practice', "Courses should make sure the learning space is accessible, fit for purpose, safe and private enough for practising therapy.", "Check rooms used for skills practice for access, safety and privacy."),
 ('delivering', 'accessible formats', "Courses should offer content in accessible formats.", "Provide materials in accessible formats as standard."),
 ('promoting,offered', 'inclusive design and parity of opportunity', "Courses should actively promote equality, diversity and inclusion in teaching and learning; curriculum design must be inclusive, delivery accessible and learning opportunities equal.", "Make inclusive design, accessible delivery and equal opportunity explicit checks at approval and review."),
 ('including', 'a range of assessment strategies', "Courses should use varied assessment strategies.", "Vary assessment types so that no group is disadvantaged."),
 ('screening', 'checking placements for safety and access', "Courses should check placements for health and safety and for accessibility.", "Screen every placement for safety and accessibility before use."),
 ('remaining', 'barriers such as digital poverty', "Courses should stay alert to barriers such as digital poverty.", "Monitor barriers like lack of devices or data."),
 ('finding,offering,lending,providing', 'practical help for marginalised groups', "Courses should look for ways round access problems that marginalised groups may face, such as bursaries, loaned laptops and data.", "Offer practical support, such as bursaries, laptops and data, where access is at risk."),
]
for _k, (_v, _a, _p, _pr) in enumerate(_AC, 1):
    prov(f'2.3.b{_k}', force='must' if _k == 6 else 'should', verbs=_v.split(','), about=_a, para=_p, prac=_pr,
         q="Which students would struggle to reach this part of the course, and what is done about it?")
prov('2.4', verbs=['consider', 'making', 'ensure'], about='reasonable adjustments and fitness to practise',
  para="Courses should consider reasonable adjustments so that access to learning is fair; they also carry ethical duties to watch students' fitness to practise with clients and to act to protect clients.",
  prac="Set out how reasonable adjustments are decided and how fitness-to-practise concerns are raised and acted on.",
  q="How are adjustments balanced against fitness to practise with clients?")
_PG = [  # 2.5: progression
 ('must', 'be', 'each stage set at the right academic and professional level', "Each stage of a course must match both the academic and the professional level it sits at.", "Check every stage against both its academic level and its professional expectations."),
 ('should', 'offered,complete,confer', 'non-practitioner exit awards', "Students who do not complete every requirement should be offered other exit awards that do not confer practitioner status.", "Provide non-practitioner exit awards and make clear they do not license practice."),
 ('should', 'make,commit,ensure', 'clear progression routes', "Courses should make routes to further study and work clear to students, and work with courses at lower and higher levels to ease progression.", "Publish progression routes and keep links with feeder and onward courses."),
 ('should', 'explored', 'articulation routes elsewhere', "Where an institution cannot offer progression itself, formal articulation routes should be explored.", "Set up articulation agreements where internal progression is missing."),
 ('should', 'progress', 'seamless moves between awards', "Smooth routes should let students move from one award or qualification to the next.", "Remove gaps between awards so that students can move on without repeating learning."),
]
for _k, (_f, _v, _a, _p, _pr) in enumerate(_PG, 1):
    prov(f'2.5.b{_k}', force=_f, verbs=_v.split(','), about=_a, para=_p, prac=_pr, q="What would a student leaving early, or moving on, actually be offered?")
both('2.6', force='describes', verbs=['progress', 'expected'], level='fheq:6', award=HON, domain='none', about='progress across the years towards the threshold',
  appliesTo='students on honours courses in the subject',
  para="Honours students move from year to year under their institution's rules, and each year is expected to build knowledge, expertise and experience towards meeting every threshold skill in the statement; a graduate with a second-class degree or better would be expected to be ready for postgraduate study in the field.",
  prac="Plan what each year adds towards the threshold standards, and tell students what a second-class result or better prepares them for.",
  ben="Each year of your course is expected to build towards the full set of minimum skills you need by the end, and a good second-class degree or better should ready you for postgraduate study.",
  q="What does each year of the course add towards the final standards?")
lrn('2.7', force='will', verbs=['achieve', 'add'], level='fheq:6', award=HON, appliesTo='joint honours undergraduates', about='what joint honours students achieve',
  para="Students on joint honours will reach some of the subject's specific and generic skills and add others from their other subjects.",
  prac="Make clear which subject and generic skills a joint honours route covers and which it leaves to the partner subject.",
  ben="If you study the subject jointly with another, you will gain some of its specific and general skills and add others from your other subject.",
  q="Which of the subject's skills does a joint route leave out?")
_FX = [
 ('offered', 'full-time and part-time study', "Courses may be offered full-time or part-time.", "Consider offering part-time routes alongside full-time ones."),
 ('offered,allowing,convert,start', 'recognition of prior learning', "Courses may offer entry with recognition of prior learning, turning relevant experience into credit; the risk to those without recent higher education experience should be noted, with study support and clear information on costs, timescales and failed modules.", "If you admit with recognition of prior learning, support those it may disadvantage and give clear information on costs, time and failure."),
 ('delivered,take', 'face-to-face, blended or hybrid delivery', "Courses may be delivered in person or in blended or hybrid ways that attend to digital inclusion and sustainability; delivery with no live element is not eligible for professional recognition.", "Keep some live contact in any delivery mode, or the course cannot gain professional recognition."),
]
for _k, (_v, _a, _p, _pr) in enumerate(_FX, 1):
    prov(f'2.9.b{_k}', force='may', verbs=_v.split(','), about=_a, para=_p, prac=_pr, q="Which students does this mode of study open the course to, and who does it shut out?")
P['2.9.b3'].update(find='delivered face to face or using blended or hybrid models which take adequate account of digital inclusion and sustainability; however, modes of delivery with no synchronous content are not eligible for professional recognition.', after=0)
prov('2.10', verbs=['work'], about='a written agreement with placement partners',
  para="Courses work with placement partners and outside stakeholders, and there should be a joint written agreement between supervisors, the course, the placement and the student.",
  prac="Put a written agreement in place for every placement, signed by supervisor, course, placement and student.",
  q="Does every placement have a signed four-way agreement?")
prov('2.11', verbs=['written'], about='alignment with a professional body',
  para="Courses should be designed in line with the requirements of a suitable professional body for their modality.",
  prac="Choose the professional body that fits the modality and align the course with its requirements.",
  q="Which professional body's requirements does the course follow, and why that one?")
_MR = [
 ('influences', 'feedback from students, stakeholders and alumni', "Review should make sure that feedback from students, employers, placements and alumni shapes the curriculum."),
 ('', 'feedback from service users', "Review should draw on feedback from people who use services."),
 ('', 'embedding sustainability education', "Review should check that education for sustainable development runs through the whole curriculum."),
 ('', 'internal moderation', "Review should include internal moderation."),
 ('', 'external examiners or assessors', "Review should include external examiners or assessors."),
 ('', 'institutional internal review', "Review should include the institution's own internal reviews."),
 ('align', 'monitoring against professional body requirements', "Annual monitoring should keep the course in line with professional body requirements."),
 ('', 'minuted communication in the teaching team', "Review should rest on structured, minuted communication within the teaching team."),
 ('', 'national surveys and quality exercises', "Review should take account of external quality exercises and surveys such as the TEF, NSS, PTES and PRES."),
]
for _k, (_v, _a, _p) in enumerate(_MR, 1):
    prov(f'2.16.b{_k}', verbs=[x for x in _v.split(',') if x], about=_a, para=_p,
         prac="Show in the course's monitoring and review cycle where this happens and what changed as a result.",
         q="What changed in the course the last time this source was used?")

# =============================================================== section 3: content, structure and delivery
prov('3.4', force='will', verbs=['provide'], about='the five pillars of the curriculum',
  para="Courses will typically offer an integrated curriculum resting on five pillars: theory, skills practice, personal growth, professional growth and research.",
  prac="Structure the curriculum around the five pillars and show how they connect.",
  q="Which pillar is weakest in the current course design?")
_TR = [  # 3.8: trainings must ensure that trainees are able to demonstrate
 ('explore,resolve,engaging', 'emotional competence and warmth', "Trainees must be able to show fitting emotional competence and warmth, including working through personal issues that the work stirs up.", "Assess emotional competence and warmth in practice, and support students to work through what the work stirs up.", "You must be able to show emotional competence and warmth, and to work through personal issues that therapy work raises in you.", "What has client work stirred up in you, and how did you deal with it?"),
 ('use,responding', 'using personal resources creatively', "Trainees must be able to use their personal and professional resources creatively and flexibly to meet a wide range of clients' needs.", "Look for flexible use of self and skills across different clients.", "You must be able to use your personal and professional resources creatively to meet many kinds of client.", "How did you adapt yourself for a client unlike you?"),
 ('identify,address,seeking', 'personal triggers and how to manage them', "Trainees must be able to spot their own triggers in client work and handle them through self-care, supervision or personal therapy.", "Teach students to name triggers and act on them through supervision or therapy.", "You must be able to spot what triggers you in client work and deal with it through self-care, supervision or your own therapy.", "What triggers you in sessions, and what do you do about it?"),
 ('developed', 'knowing what it is to be a client', "Trainees must be able to show awareness of what being a client is like, gained through supervision, group and experiential work and possibly personal therapy.", "Give students ways to experience the client's position, such as experiential groups or personal therapy.", "You must be able to show that you know what being a client feels like, from group work, supervision or your own therapy.", "What did being on the client side teach you?"),
 ('impact,affected', 'how one\'s own history affects therapy', "Trainees must be able to show awareness of how their past and present experience can affect therapy and be shaped by age, family, culture, disadvantage, gender, race, sexuality and social position.", "Explore students' life experience and identity and how these enter the work.", "You must be able to show that you know how your own life and identity can affect the therapy you offer.", "Which part of your history most often enters the room?"),
 ('make,understand,take,recognising,engaging', 'reflection, supervision and personal support', "Trainees must be able to make reflection on themselves and the relationship central to clinical work, tell their needs from the client's, own their learning and use supervision, development and personal support or therapy as needed.", "Assess reflective practice and the use of supervision and personal support throughout placement.", "You must be able to reflect on yourself and the relationship in all your client work, keep your needs apart from your client's, and use supervision and personal support when you need it.", "How do you keep your own needs out of the client's session?"),
 ('adopting,engage', 'personal responsibility and use of feedback', "Trainees must be able to take personal responsibility and engage constructively with feedback.", "Assess how students respond to and act on feedback.", "You must be able to take responsibility and use feedback well.", "What feedback have you acted on recently?"),
 ('recognising', 'knowing one\'s limits, power and strengths', "Trainees must be able to recognise their own limits, power and strengths.", "Ask students to name their limits, power and strengths with evidence.", "You must be able to recognise your limits, your power and your strengths.", "Where do you hold power with clients without meaning to?"),
 ('developing,strengthening,work', 'creativity, autonomy and proactive working', "Trainees must be able to build practical creativity, flexibility, motivation, autonomy and a proactive way of working.", "Give room for autonomous, creative work in placement and projects.", "You must be able to build creativity, flexibility, motivation and independence, and work proactively.", "When did you take the initiative on placement?"),
 ('', 'professional development', "Trainees must be able to show professional development.", "Track professional development across the course.", "You must be able to show your professional development.", "How have you grown professionally since you started?"),
]
for _k, (_v, _a, _p, _pr, _b, _q) in enumerate(_TR, 1):
    lrn(f'3.8.b{_k}', force='must', verbs=[x for x in _v.split(',') if x], about=_a, para=_p, prac=_pr, ben=_b, q=_q)
P['3.8.b10'].update(find='professional development.', after='developing and strengthening practical creativity')
prov('3.11', force='must', verbs=['offer', 'incorporate'], about='an integrated curriculum with an assessed, supervised placement',
  para="Courses prepare self-reflective, evidence-based and ethical practitioners; every course will offer an integrated curriculum of theory, research, skills training and personal and professional development, and must include an assessed and supervised placement.",
  prac="Make sure the course has an assessed, supervised placement as well as the integrated academic, skills and development strands.",
  q="How is the placement assessed, and by whom?")
prov('3.15', verbs=['equip', 'reflect', 'incorporate'], about='in-person and remote skills and core digital training',
  para="Courses should equip students for in-person practice and can include remote practice; training should match the mode in which students will practise, and every course should include core training in electronic systems for data, literature, resources and communication.",
  prac="Match the training mode to how students will practise on placement and after, and include core digital training whatever the mode.",
  q="Does the way students are trained match the way they will see clients?")
prov('3.16', verbs=['incorporated', 'designed', 'assessed', 'exploring', 'addressing'], about='inclusive teaching by a diverse team',
  para="Inclusive practice by diverse trainers should run through all teaching and learning; activities should be designed authentically for the work, checked in advance for barriers to students with different needs, and staff should be open to tackling equality, diversity and inclusion with all stakeholders.",
  prac="Check every teaching activity for barriers in advance, and raise equality, diversity and inclusion with staff, students and placements alike.",
  q="Which teaching activity was last changed because it excluded someone?")
both('3.17', verbs=['involve', 'define', 'demonstrate'], domain='understanding', about='depth in a modality, its view of people and its heritage',
  para="Courses usually give depth in one or more recognised modalities; this should include understanding that modality's account of human nature and its cultural roots as well as how to use it with clients, and an integrative course should be able to name its parts and show they fit together.",
  prac="Teach the chosen modality's view of human nature and its cultural history as well as its methods; if the course is integrative, set out its components and how they cohere.",
  ben="You should understand how your chosen approach sees human nature and where it comes from culturally, as well as how to use it with clients.",
  q="Where does your approach come from, and whose experience does it reflect?")
both('3.18', force='will', verbs=['modify', 'develop'], domain='understanding', about='respect for other approaches and modality-specific training',
  para="Students need to develop awareness and respect for other therapeutic approaches and other mental health interventions, and course teams will adapt the style, emphasis and make-up of training to the modality and to the relevant professional body's requirements.",
  prac="Shape training to the needs of the modality and the professional body, while making sure students learn to respect other approaches.",
  ben="You need to learn about and respect approaches to therapy and mental health other than your own.",
  q="What do you respect in an approach you would not choose yourself?")
lrn('3.19', domain='knowledge', verbs=['require', 'access', 'evaluate', 'have', 'undertake'], about='research awareness and methods',
  para="Research is a key skill for practitioners; at the least, graduates need enough awareness to use continuing development and to evaluate research in their field, and they should know quantitative, qualitative and mixed methods relevant to practice, usually through at least one small study.",
  prac="Teach the three families of research method, and give each student at least one small study, whether empirical, a systematic case study or a review.",
  ben="You should know the main kinds of research method used in therapy, be able to judge research in your field, and usually carry out at least one small study yourself.",
  q="What small study could you carry out on your own practice?")
prov('3.20', force='will', verbs=['make', 'supported'], about='provision for personal development',
  para="Every course will provide for students' personal development, and should create chances to understand how the therapist's growth and emotional competence affect the relationship, which may include personal therapy or other suitable activities.",
  prac="Build personal development into every course, using groups, journals, residentials or personal therapy as suits the modality.",
  q="What does the course require for personal development, and why that?")
prov('3.21', verbs=['support', 'liaise', 'engage'], about='placements, supervision and their oversight',
  para="Training staff should help students find placements that fit their interests and stage, check placements and supervisors, require regular supervision during client work, consider how supervisors stay reflexive about privilege, power and oppression, and decide how placement feeds into assessment.",
  prac="Vet placements and supervisors, require regular supervision, and set out how placement evidence counts towards assessment.",
  q="How do you know a placement's supervision is good enough?")
prov('3.22', force='must', verbs=['delivered', 'managed', 'ensure'], about='qualified staff and suitable staff to student ratios',
  para="Courses should be run by suitably qualified and experienced staff; because experiential work needs close containment, observation and care, staff to student ratios must suit students' learning needs, and the sector's experience supports ratios no higher than one to sixteen in experiential classes, with a clear rationale in all cases.",
  prac="Set and justify staff to student ratios for experiential work, keeping skills classes small enough for observation and feedback.",
  q="What is the ratio in skills practice sessions, and how is it justified?")
both('3.23', force='will', verbs=['address', 'evaluate'], domain='subject-skill', about='assessing theory and practice competence for the award',
  para="Assessment will cover theory and skills against the course outcomes; in professional training practitioner competence will carry heavy weight and a satisfactory level will be a condition of the award, since the graduate is expected to be ready to practise at once.",
  prac="Weight practitioner competence heavily in assessment and make a satisfactory level a condition of the award.",
  ben="Your assessment will cover both theory and skills, and you will need to reach a satisfactory level of practice competence to get your award.",
  q="What would show that a student is ready to practise the day after the award?")
prov('3.25', verbs=['evaluate'], about='inclusive, authentic assessment and its criteria',
  para="Assessment may be formative or summative, in person or on secure platforms; it should be inclusive and true to the profession while keeping academic standards, and criteria should cover core skills and knowledge and broader professional skills such as risk awareness, teamwork, ethics and judgement.",
  prac="Write criteria that cover core counselling skills and wider professional skills, and make assessments inclusive and authentic.",
  q="Do the criteria assess risk awareness and ethical judgement, or only core skills?")
prov('3.26', verbs=['considered'], about='quality assurance of assessment',
  para="Quality assurance of assessment should be planned into design, moderation and review, with external examiners, critical friends, placements, employers and moderators, to share good practice.",
  prac="Involve external examiners, placements and employers in designing and reviewing assessment.",
  q="Who outside the team has looked at the assessments this year?")
both('3.27', force='must', verbs=['assess', 'assessed', 'approved'], domain='subject-skill', about='readiness assessed before client work',
  para="Assessment should be used formatively to judge readiness for placement and summatively for the award; students must be assessed on skills, knowledge and personal resilience before they are approved to see real clients.",
  prac="Put a formal readiness check on skills, knowledge and resilience before any student sees clients.",
  ben="Before you can work with real clients on placement, you must be assessed on your skills, knowledge and personal resilience.",
  q="What does the course check before a student sees a first client?")

# =============================================================== section 4: introduction and the rung paragraphs
prov('4.2', verbs=['refer'], about='Annex D for achievement above the threshold',
  para="Most students will do much better than the minimum; each institution decides what evidence shows this and should refer to Annex D, which describes the honours degree classes at FHEQ level 6 and FQHEIS level 10.",
  prac="Use Annex D alongside your own marking schemes to judge performance above the threshold.",
  q="How do your marking criteria line up with Annex D's descriptions of each class?")
lrn('4.4', type='expectation', verbs=['practise', 'need'], level='fheq:6', award=HON, domain='none', about='competence in every part of the standard before completion',
  appliesTo='students on practice-facing honours courses',
  para="The standards below are the threshold for honours at FHEQ level 6 or FQHEIS level 10, the least that students on professional courses must know, be and do to practise safely, ethically and effectively; successful students should be competent in every aspect before they complete.",
  prac="Assess every threshold standard before the award; competence in each is expected, not an average across them.",
  ben="By the end of your course you should be competent in every part of the minimum standard for safe, ethical and effective practice, not just most of it.",
  q="Which part of the standard is least well evidenced for this student?")
prov('4.14', force='will', verbs=[], about='typical-level criteria left to institutional marking schemes',
  appliesTo='honours courses in the subject',
  para="Criteria for 2:2 and 2:1 performance above the threshold will follow each institution's common or generic undergraduate marking schemes.",
  prac="Use your institution's generic marking scheme for 2:2 and 2:1 work; the statement gives no subject-specific typical standards.",
  q="Does the generic marking scheme say enough about practice competence at 2:2 and 2:1?")
prov('4.15', force='will', verbs=[], about='excellent-level criteria left to institutional marking schemes',
  appliesTo='honours courses in the subject',
  para="Criteria for first-class performance will follow each institution's common or generic undergraduate marking schemes.",
  prac="Use your institution's generic marking scheme for first-class work; the statement gives no subject-specific excellent standards.",
  q="What would first-class practice look like under your scheme?")

# =============================================================== threshold (honours): 4.6 to 4.12, Know, Be, Do
DOM = {'k': 'knowledge', 'u': 'understanding', 's': 'subject-skill', 'g': 'generic-skill'}
KBD = {'K': 'Know', 'B': 'Be', 'D': 'Do'}
THR = {}
THR['4.6'] = [
 ('K', 'Understand how philosophical assumptions', 'u', 'Understand,influence,evaluate', 'philosophical assumptions behind research and practice',
  "Grasp how underlying philosophical positions shape the different approaches to counselling research and practice, and weigh critically what this means for working in teams across disciplines.",
  "Teach the philosophical roots of the main approaches and research paradigms, and ask students to judge what those roots mean for multidisciplinary teamwork.",
  "You understand how the beliefs underneath each approach shape research and practice, and you can judge what that means when you work with other professions.",
  "Which assumptions about people sit underneath the approach you are training in?"),
 ('K', 'Critically evaluate and apply relevant professional codes', 's', 'evaluate,apply', 'professional codes and organisational policies',
  "Judge critically and put into practice the professional codes and organisational policies that govern practice, including those on diversity and equal opportunity.",
  "Have students test professional codes and agency policies against cases, including the parts on diversity and equal opportunity, and then apply them.",
  "You can weigh up the codes and policies that govern your practice, including those on diversity and equality, and use them in real situations.",
  "Which part of your professional code have you had to apply in a real decision?"),
 ('K', 'Be aware of the various impacts', 'k', '', 'government policy and guidance such as NICE',
  "Know how government policy and guidance, such as NICE guidelines, affect counselling services, research, mental health provision more widely and the well-being of clients.",
  "Include current policy and national clinical guidance in the curriculum, and ask students to trace their effects on services, research and clients.",
  "You know how government policy and national guidance, such as NICE guidelines, shape therapy services, research and the care clients receive.",
  "How does a current national guideline affect which therapies clients can get?"),
 ('K', 'Recognise and understand the ways in which power', 'u', 'Recognise,understand,reflect,operate,impact', 'power in relationships, groups and organisations',
  "See and understand how power shows itself in relationships, and reflect on how power dynamics work in groups, organisations and therapy and what they do to outcomes.",
  "Use group work, placement and case material to help students name power dynamics and reflect on their effect on outcomes.",
  "You can spot how power works in relationships, groups, organisations and therapy, and think about how it changes what happens.",
  "Where did you notice power shaping a group or session you were part of?"),
 ('B', 'Reflective of the role, contribution', 's', '', "the profession's place in society",
  "Be reflective about what counselling and psychotherapy do in present-day society, what they add and what pressures they face.",
  "Give students space to debate the profession's role, value and current challenges.",
  "You think carefully about what therapy does for society today and the pressures it faces.",
  "What do you see as the biggest challenge facing the profession now?"),
 ('B', 'Considerate, challenging and reflective', 's', '', "examining one's own values and their effect on therapy",
  "Be thoughtful about, question and reflect on one's own values, beliefs, attitudes and behaviour, and on how they bear on therapeutic work.",
  "Use personal development groups and supervision for students to question their own values and trace their effect on client work.",
  "You question and reflect on your own values, beliefs and habits, and on how they affect your work with clients.",
  "Which of your values has most shaped how you respond to clients?"),
 ('B', 'Able to recognise and act with professional responsibility', 's', 'recognise,act', 'professional responsibility to all parties',
  "Be able to see, and act on, professional responsibility to clients, employers, trainers, the professions and society.",
  "Help students map their duties to each party, and use placement to show them acting on those duties.",
  "You can see where your professional responsibilities lie, to clients, employers, trainers, the profession and society, and you act on them.",
  "When have two of these responsibilities pulled you in different directions?"),
 ('B', 'Open to diversity and embrace difference', 's', 'embrace', "openness to diversity and to every client's rights",
  "Be open to diversity and welcome difference with regard to every client's rights and responsibilities, whatever their characteristics or identity, including but not only those the law protects.",
  "Make openness to difference something students show in practice and reflect on, going beyond the legally protected characteristics.",
  "You are open to and welcome difference in every client, whatever their identity, not only in the ways the law protects.",
  "Which aspects of identity do you find harder to stay open to, and why?"),
 ('D', 'Recognise and work within the social, cultural', 's', 'Recognise,work', 'working within the social and political context',
  "See and work within the social, cultural and political setting of one's own practice and of the profession.",
  "Ask students to locate their placement practice in its social, cultural and political context and show that they work with it.",
  "You work with awareness of the social, cultural and political setting of your practice and of the profession.",
  "How does the community your placement serves shape the work you do there?"),
 ('D', 'Build and sustain professional relationships', 's', 'Build,sustain,work,support,evaluate,contribute', 'collaboration with supervisors and other professionals',
  "Form and keep professional relationships that suit the setting, and work with a supervisor and other professions to support and review client work, the wider practice and the growth of services.",
  "Assess how students collaborate with supervisors and other professionals on placement, including any contribution to how the service develops.",
  "You build and keep working relationships with your supervisor and other professionals, and use them to support your client work and help the service improve.",
  "Who outside therapy have you worked with on a client's behalf, and how did it go?"),
 ('D', 'Critically appraise and evaluate published research', 's', 'appraise,evaluate,apply', 'using research in practice',
  "Judge published counselling research critically and use a thorough, research-based body of knowledge consistently in practice.",
  "Require students to appraise studies and show, in case work, how research informs what they do with clients.",
  "You can judge published research critically and let a sound, research-based understanding guide your work every time.",
  "Which study has changed something you do with clients?"),
 ('D', 'Actively seek to promote equality', 's', 'promote,challenge', 'promoting equality and challenging discrimination',
  "Work actively for equality, diversity and inclusion in practice and confront discrimination and prejudice at professional, organisational and systemic levels.",
  "Look for evidence that students act on equality and challenge prejudice, not only discuss it, on placement and in course life.",
  "You actively promote equality and inclusion in your work and challenge discrimination and prejudice where you meet it, including in organisations.",
  "When have you challenged something unfair in a setting you worked in?"),
 ('D', 'Develop competencies to lead', 's', 'Develop,lead', 'competencies for a self-directed professional life',
  "Build the academic, therapeutic and digital competencies for a fulfilling professional life that one directs oneself.",
  "Help students plan the academic, therapeutic and digital skills they will need to shape their own careers.",
  "You build the academic, therapeutic and digital skills to shape a rewarding career of your own choosing.",
  "What does a rewarding professional life look like for you in five years?"),
 ('D', 'Develop the ability to reasonably adapt', 's', 'Develop,adapt', 'adapting to change and uncertainty',
  "Grow the capacity to adjust sensibly to changing settings and to uncertainty.",
  "Expose students to change, such as a move to remote work, and assess how they adapt.",
  "You can adjust sensibly when your setting changes or when things are uncertain.",
  "How did you cope the last time your placement or plans changed suddenly?"),
]
THR['4.7'] = [
 ('K', 'Understand and engage with multifaceted models', 'u', 'Understand,engage,recognise', 'models of mental distress',
  "Understand and work with many-sided models of mental distress that respect different worldviews and frameworks and the client's own view, across biomedical, psychological, social, political and cultural accounts.",
  "Teach biomedical, psychological, social, political and cultural accounts of distress side by side, with the client's own account at the centre.",
  "You understand several ways of explaining mental distress, from medical to social and cultural, and you keep the client's own view at the centre.",
  "How would a medical account and a social account explain the same client's distress?"),
 ('K', 'Recognise potential limitations of their chosen', 'k', 'Recognise,seek,mitigate', "the limits of one's chosen model",
  "See where one's chosen model may fall short with particular clients and try to reduce those shortfalls where possible.",
  "Ask students to name cases where their core model struggles and say what they would do about it.",
  "You can see where your chosen approach may not fit a particular client and look for ways to make up for that.",
  "With which kind of client does your approach work least well?"),
 ('K', 'Recognise and respect diverse perspectives', 'k', 'Recognise,respect', 'other professional perspectives on mental health',
  "Acknowledge and respect a range of views on mental health, including those of other professions and agencies.",
  "Bring in other professions' views of mental health and ask students to engage with them respectfully.",
  "You recognise and respect other views on mental health, including those of other professions and agencies.",
  "How does a psychiatrist's view of a client differ from yours?"),
 ('K', 'Understand and evaluate the role that mental health', 'u', 'Understand,evaluate,consider,impact', 'the social role of mental health services',
  "Understand and judge what mental health and counselling services do in society, and consider critically how social, political and economic forces affect present-day practice.",
  "Ask students to analyse a service in its policy and economic setting and judge how those forces shape practice.",
  "You understand what therapy services do in society and can think critically about how money, politics and social change shape them.",
  "How has funding shaped the therapy offered where you are on placement?"),
 ('K', 'Understand and critically evaluate the concept of relationship', 'u', 'Understand,evaluate,consider', 'the relationship across theoretical approaches',
  "Understand and critically weigh how different theories treat the relationship, and what follows for skilled client work and for work with other professions.",
  "Compare how several approaches treat the relationship and link each to practice with clients and colleagues.",
  "You understand and can compare how different approaches think about the relationship, and what that means for your work with clients and colleagues.",
  "How does your approach's idea of the relationship shape what you do in a first session?"),
 ('B', 'Open to and appreciative of a range', 's', 'building,maintaining', 'openness to other approaches for good working relationships',
  "Be open to, and value, a range of approaches, so as to build and keep respectful working relationships with colleagues and good alliances with clients.",
  "Encourage students to learn from approaches other than their own and show that openness with peers and clients.",
  "You are open to approaches other than your own, which helps you work well with colleagues and build alliances with clients.",
  "What have you learned from a colleague who works in a different way?"),
 ('B', 'Consciously aware of one', 's', '', "awareness of one's own and unconscious bias",
  "Be consciously aware of one's own biases and alert to unconscious bias linked to context, gender, age, ethnicity, origin, culture, class, ability, sexual orientation, religion and belief.",
  "Use reflective tasks and supervision for students to name their biases and watch for unconscious ones across the full range of identities.",
  "You are aware of your own biases and alert to hidden ones about people's identity, background, ability, sexuality or faith.",
  "Which bias of yours surprised you when you first noticed it?"),
 ('D', 'Draw on a range of research-informed', 's', 'Draw,inform', 'research-informed responses that respect client preference',
  "Use a range of responses, strategies and interventions grounded in research to shape practice that is sensitive to what clients need and prefer.",
  "Teach a repertoire of evidence-based interventions and assess whether students choose among them with the client's needs and wishes in mind.",
  "You use a range of research-based responses and techniques, chosen with care for what each client needs and wants.",
  "How did a client's preference change the intervention you chose?"),
 ('D', 'Use opportunities for reflective practice', 's', 'Use,recognise,demonstrate,monitor', 'using supervision to check bias',
  "Use reflective practice, such as supervision, to notice and show awareness of one's own conscious bias and to check practice for signs of unconscious bias, so that therapy is anti-discriminatory.",
  "Make bias a standing item in supervision and reflective logs, and look for evidence that students act on what they find.",
  "You use supervision and reflection to notice your own bias and check your work for hidden bias, so that your practice treats every client fairly.",
  "What did supervision help you see about your own bias?"),
 ('D', 'Develop self-awareness of own enterprising', 's', 'Develop,apply', 'enterprising capabilities in therapeutic work',
  "Become aware of one's own enterprising capacities in therapeutic work, with the drive and discipline to use them flexibly as contexts change.",
  "Help students identify their own enterprising strengths in therapy settings and plan how to use them.",
  "You know your own enterprising strengths in therapy work and have the drive to use them as situations change.",
  "Where have you shown initiative in setting up or improving a service?"),
 ('D', 'Demonstrate initiative, autonomy', 's', 'Demonstrate', 'initiative, autonomy and responsibility',
  "Show initiative, independence and responsibility.",
  "Assess initiative and independent judgement on placement and in projects.",
  "You show initiative, work independently and take responsibility.",
  "When did you act on your own judgement without waiting to be told?"),
]
THR['4.8'] = [
 ('K', 'Recognise their own personal and professional strengths', 'k', 'Recognise,affect', "one's own strengths and limits",
  "Know one's personal and professional strengths and limits as they bear on practice.",
  "Ask students to assess their own strengths and limits with evidence from practice and feedback.",
  "You know your strengths and limits as a person and as a practitioner, and how they affect your work.",
  "Which limit of yours most needs watching in client work?"),
 ('K', 'Recognise their own self-care needs', 'k', 'Recognise,develop', 'self-care needs and strategies',
  "Know what one needs to look after oneself and build suitable ways of supporting and caring for oneself.",
  "Have students write and review a self-care plan, and check it in supervision.",
  "You know what you need to stay well and have workable ways to look after yourself.",
  "What tells you that you need to step back and look after yourself?"),
 ('K', 'Recognise when it is appropriate to make referrals', 'k', 'Recognise,make', 'when to refer on',
  "Know when referring a client to another service is the right step.",
  "Use case discussion to rehearse referral decisions and the routes available.",
  "You can tell when it is right to refer a client to another service.",
  "What would make you refer a client on rather than keep working with them?"),
 ('B', 'Able to engage with the role of supervision', 's', 'engage,support', 'supervision as central to practice',
  "Be able to use supervision as a core part of practice that supports both the client work and the practitioner's growth.",
  "Make the use of supervision visible in assessment, not only the hours logged.",
  "You use supervision as a central part of your practice, for your clients' sake and for your own growth.",
  "What do you bring to supervision, and what do you hold back?"),
 ('B', 'Able to apply self-supervision skills', 's', 'apply,consider,challenge,impact', 'self-supervision',
  "Be able to supervise oneself, questioning one's values, beliefs, attitudes and behaviour and their effect on the work.",
  "Teach self-supervision methods and ask students to show them in process notes.",
  "You can supervise yourself, questioning your own values and habits and how they affect your work with clients.",
  "How do you check your own reactions between sessions?"),
 ('D', 'Ensure a consistent commitment', 's', 'Ensure', 'commitment to ongoing development and fitness to practise',
  "Keep up a steady commitment to growing personally and professionally, self-awareness and fitness to practise included.",
  "Track personal and professional development through the course and treat fitness to practise as an ongoing matter.",
  "You stay committed to your own development, personal and professional, including your self-awareness and fitness to practise.",
  "What will you do to keep developing once the course ends?"),
 ('D', 'Recognise the need for, and engage with', 's', 'Recognise,engage', 'personal support or therapy',
  "See when one needs personal support or therapy and take it up as fitting.",
  "Make routes to personal therapy and support clear, and help students judge when to use them.",
  "You can tell when you need personal support or therapy and you take it up.",
  "How would you know it was time to seek therapy for yourself?"),
 ('D', 'Make use of supervision to develop', 's', 'Make,develop,enhance,protect', 'supervision for understanding and well-being',
  "Use supervision to deepen understanding of practice and to strengthen and safeguard one's own well-being.",
  "Look for evidence that students use supervision to learn and to protect themselves, not only to report cases.",
  "You use supervision to understand your practice better and to protect your own well-being.",
  "When did supervision help you stay well during difficult work?"),
]
THR['4.9'] = [
 ('K', 'Understand the main ethical and legal contexts', 'u', 'Understand,happen', 'the ethical and legal contexts of practice',
  "Understand the main ethical and legal settings of practice, which means knowing the points that follow.",
  "Cover the ethical and legal ground in the points that follow explicitly and check it in assessment.",
  "You understand the main ethical and legal rules your practice works within.",
  "Which law has the biggest effect on your day-to-day practice?"),
 ('K', 'principles of law as they relate', 'k', 'relate', 'law relevant to practice, including online work',
  "Know the legal principles that bear on practice, such as data protection and child protection, including differences across the UK nations and international law when working online.",
  "Teach the law on data and child protection with its devolved variations and the international issues of online work.",
  "You know the legal principles that affect your practice, such as data and child protection, including how they differ across the UK and abroad when you work online.",
  "What changes legally if your online client lives in another nation?"),
 ('K', 'ethical frameworks or codes of practice', 'k', 'understand', 'ethical frameworks and professional requirements',
  "Know the ethical frameworks, codes and good-practice guidance of professional associations, and the professional requirements, such as for supervision, that relevant bodies set.",
  "Teach the main professional codes and the requirements they set, such as for supervision, and compare them.",
  "You know the ethical codes and guidance of the professional associations and what they require of you, for example in supervision.",
  "What does your professional body require of you in supervision?"),
 ('K', 'agency policies and procedures, where relevant', 'k', '', 'agency policies and procedures',
  "Know, where they apply, the policies and procedures of the agency one works in.",
  "Ask students to learn and use their placement agency's policies.",
  "You know the policies and procedures of the agency you work in.",
  "Which agency policy have you had to follow most often?"),
 ('K', 'changes in legislation, having an awareness', 'k', 'ensure,informed', 'keeping up with changes in law and guidance',
  "Know about changes in the law and where to find current information, so that practice follows the latest ethical and legal guidance.",
  "Teach students where to find updates on law and ethics and how to keep their practice current.",
  "You keep up with changes in law and guidance and know where to look so your practice stays current.",
  "Where would you check for a change in the law that affects you?"),
 ('K', 'the implications of needing to breach confidentiality', 'k', 'shared', 'breaching confidentiality',
  "Know what follows from having to break confidentiality, and be clear what must be disclosed and to whom.",
  "Rehearse confidentiality breaches through cases, with clear lines on what must be passed on and to whom.",
  "You know what it means to have to break confidentiality, and you are clear what you must pass on and to whom.",
  "In what situation would you have to break confidentiality, and who would you tell?"),
 ('K', 'Understand the implications of at least one model', 'u', 'Understand', 'a model of ethical decision-making',
  "Understand what follows from at least one ethical decision-making model suited to counselling and psychotherapy.",
  "Teach at least one decision-making model and have students apply it to dilemmas.",
  "You understand at least one model for making ethical decisions in therapy and can use it.",
  "How would you use a decision-making model on a real dilemma?"),
 ('B', 'Committed to working ethically', 's', 'aligning', 'commitment to ethical principles',
  "Be committed to ethical work, matching practice to justice, integrity, trustworthiness, doing good, avoiding harm and self-care.",
  "Ask students to show how core ethical principles guide their placement decisions.",
  "You are committed to working ethically, guided by justice, integrity, trust, doing good, avoiding harm and caring for yourself.",
  "Which ethical principle do you find hardest to hold to in practice?"),
 ('D', 'Work within a named ethical code', 's', 'Work,reflects', 'working within a named code',
  "Practise under a named ethical code and act with care in line with its principles.",
  "Require students to name the code they work under and show its principles in their decisions.",
  "You work under a named ethical code and act thoughtfully in line with its principles.",
  "Which code do you work under, and how did it shape a recent decision?"),
 ('D', 'Critically analyse, question, and consider', 's', 'analyse,question,consider', 'ethical dilemmas in practice',
  "Analyse, question and think through ethical dilemmas that arise in practice, with a supervisor or other suitable professionals as needed.",
  "Use real or simulated dilemmas and assess how students reason through them with supervisory input.",
  "You can analyse and think through ethical dilemmas that come up in practice, drawing on your supervisor or others when needed.",
  "Tell me about a dilemma you took to supervision."),
 ('D', 'Deliver the counselling/psychotherapy services', 's', 'Deliver', 'safety of client, therapist and setting',
  "Provide therapy with proper attention to the safety of client and therapist and to whether the setting is suitable.",
  "Check placement settings and students' risk practice for the safety of both client and therapist.",
  "You provide therapy with care for your client's safety and your own, and for whether the setting is right.",
  "What do you check about a room or platform before a session?"),
 ('D', 'Apply diligence in record-keeping', 's', 'Apply,play', 'diligent record-keeping',
  "Keep records with diligence, since records matter for the quality and safety of therapy.",
  "Assess the quality of students' notes as part of practice competence.",
  "You keep careful records, knowing they matter for the quality and safety of therapy.",
  "What makes a good session note?"),
 ('D', 'Manage records in accordance with legislation', 's', 'Manage', 'records and the law',
  "Handle records in line with the law, statutory requirements, professional information-governance standards and clients' legal rights.",
  "Teach the legal and governance rules for records, including clients' rights of access.",
  "You handle records in line with the law, professional standards and your clients' legal rights.",
  "What rights does a client have to see their notes?"),
 ('D', 'Manage records appropriately, including', 's', 'Manage,storing,destroying', 'the life cycle of records',
  "Handle records properly across their life: accurate notes on paper or screen, secure storage, timely and purposeful sharing, and secure destruction.",
  "Cover the full record cycle, from writing to secure disposal, and check it on placement.",
  "You handle records properly from start to finish: accurate notes, safe storage, careful sharing and secure disposal.",
  "How long do you keep notes, and how do you dispose of them?"),
 ('D', 'Manage and appropriately respond to the practical', 's', 'Manage,respond', 'demands of online and technology-mediated work',
  "Handle and meet suitably the practical, legal and ethical demands of online therapy and of all communication through technology.",
  "Include online practice in teaching on ethics and law, and assess students' handling of it.",
  "You handle the practical, ethical and legal demands of working online and of any contact with clients through technology.",
  "What extra steps do you take when a session is online?"),
 ('D', 'Work within ethical and legal constraints, contracting', 's', 'Work', 'contracting on confidentiality and data across settings',
  "Work within ethical and legal limits, contracting with clients on confidentiality and data protection in different working environments, including the points that follow.",
  "Teach contracting on confidentiality and data for in-person and remote work, and assess it in practice.",
  "You agree with clients how confidentiality and data protection work in your setting, staying within ethical and legal limits.",
  "How do you explain confidentiality to a new client?"),
 ('D', 'limits to confidentiality, including when', 's', 'working', 'limits to confidentiality, including remotely',
  "Set out the limits of confidentiality, remote work included.",
  "Check that students state confidentiality limits clearly, including for remote work.",
  "You make clear to clients where confidentiality ends, including when you work remotely.",
  "Where does confidentiality end when you work by video?"),
 ('D', 'being able to inform the client', 's', 'inform,achieve', 'helping clients stay safe with data and platforms',
  "Be able to tell clients how to keep safe as to data, platforms, equipment and their physical surroundings.",
  "Give students a checklist for advising clients on safe remote set-ups.",
  "You can tell clients how to stay safe with their data, devices, platform and surroundings.",
  "What would you tell a client about where to sit for an online session?"),
 ('D', 'knowledge of contemporary digital platforms', 'k', '', 'digital platforms, accessibility and security',
  "Know current digital platforms, digital accessibility and suitable technology for the profession, and the limits of their security for remote work.",
  "Review platforms with students for accessibility and security, and keep this current.",
  "You know the main digital platforms and tools for therapy, how accessible they are, and where their security falls short.",
  "What makes one video platform safer than another?"),
 ('D', 'negotiating careful agreement concerning', 's', 'negotiating,communicate', 'agreements on recording sessions',
  "Agree carefully on any recording of sessions by either party, and be able to explain what such recording means.",
  "Include recording in contracting role-plays.",
  "You agree carefully with clients about any recording of sessions and can explain what it means.",
  "What would you say if a client asked to record a session?"),
 ('D', 'discussing data security and privacy', 's', 'discussing', 'data security in remote work',
  "Talk through data security and privacy for remote work, in light of the client's circumstances and any vulnerabilities.",
  "Teach students to tailor privacy discussions to each client's situation.",
  "You talk through data security and privacy with clients you see remotely, taking account of their situation.",
  "Who else might overhear your client at home?"),
 ('D', 'maintaining integrity in the remote therapeutic', 's', 'maintaining,fails', 'when technology fails',
  "Keep the remote relationship intact when the technology breaks down.",
  "Agree with students a plan for dropped connections and rehearse it.",
  "You keep the therapeutic relationship safe and steady when the technology breaks down.",
  "What is your plan if the call drops at a difficult moment?"),
 ('D', 'Apply intuitive decision-making', 's', 'Apply,develop,address', 'creative responses to dilemmas',
  "Use intuitive judgement and find creative, new ways to deal with problems and ethical dilemmas, with integrity and compassion.",
  "Value creative problem-solving in case work, alongside rule-based ethics.",
  "You use your judgement and find creative ways to handle problems and dilemmas, with integrity and compassion.",
  "When has a rule not been enough, and what did you do?"),
]
THR['4.10'] = [
 ('K', 'Understand what constitutes safe, responsive', 'u', 'Understand,constitutes', 'safe boundaries in all professional relationships',
  "Understand what makes boundaries safe, responsive and therapeutic in every relationship: with clients, supervisors, tutors, colleagues and employers.",
  "Teach boundaries across all the relationships of training, not only those with clients.",
  "You understand what safe, responsive boundaries look like with clients, supervisors, tutors, colleagues and employers.",
  "Where are boundaries hardest for you: with clients, tutors or colleagues?"),
 ('K', 'Consider how to recognise boundary breaches', 'k', 'Consider,recognise,maintain,support', 'recognising boundary breaches',
  "Think about how to spot breaches of boundaries so that clear professional limits keep practice safe and effective.",
  "Use cases of breaches, small and large, for students to learn the warning signs.",
  "You think about how to spot when a boundary is crossed, so you can keep clear limits and work safely.",
  "What early signs might tell you a boundary is slipping?"),
 ('K', 'The concept of contracting as part', 'k', 'understand', 'contracting and the therapeutic contract',
  "Know contracting as part of an ethical, professional process and understand what a therapeutic contract is for and what it contains.",
  "Have students draft and critique a therapeutic contract.",
  "You know why contracting matters ethically and what a therapeutic contract is for and should include.",
  "What are the parts of your contract with clients, and why each?"),
 ('K', 'Recognise and understand the complexities of working therapeutically with boundaries', 'u', 'Recognise,understand,ensure', 'responsive boundaries that keep practice safe',
  "Recognise and understand how complex boundary work is, keeping boundaries responsive while making sure practice stays safe and ethical.",
  "Discuss cases where flexibility and firmness pull against each other.",
  "You understand how complicated boundaries can be, and keep them responsive while staying safe and ethical.",
  "When did you bend a boundary, and was it right?"),
 ('K', 'Understand the implications of employment legislation', 'u', 'Understand', 'employment law across sectors',
  "Understand what employment law, policy and guidance mean for providing therapy in voluntary, community, statutory and private settings.",
  "Include employment law and policy in teaching on service settings.",
  "You understand how employment law and policy affect therapy work in voluntary, community, public and private settings.",
  "How does being employed differ from being self-employed for a therapist, in law?"),
 ('K', 'Understand the complexities and potential risks when working with sexual', 'u', 'Understand,use,ensure,avoid', 'sexual dynamics and boundary violations',
  "Understand the complexity and risk of sexual issues and dynamics in therapy and use this to keep boundaries safe and prevent sexual boundary violations.",
  "Teach sexual dynamics in therapy directly, with clear guidance on preventing violations.",
  "You understand the risks when sexual issues or feelings arise in therapy and use that to keep boundaries safe.",
  "How would you handle feelings of attraction in the therapy room?"),
 ('B', 'Aware of the potential challenges', 's', '', 'awareness of challenges in the work',
  "Be aware of the difficulties that may come up in therapeutic work.",
  "Prepare students for common difficulties before placement.",
  "You are aware of the difficulties that can come up in therapy.",
  "What challenge are you least prepared for?"),
 ('B', 'Confident in responding therapeutically', 's', 'responding,maintaining', 'confidence with change while holding boundaries',
  "Be confident in meeting changes and difficulties in the relationship therapeutically while keeping clear boundaries.",
  "Assess how students respond to shifts in the relationship without losing boundaries.",
  "You respond with confidence when the relationship changes or gets difficult, while keeping clear boundaries.",
  "How did you respond when a client tested a boundary?"),
 ('D', 'Set and maintain appropriate professional boundaries', 's', 'Set,maintain', 'boundaries during and after therapy',
  "Set and keep suitable professional boundaries throughout therapy and once it has ended.",
  "Include contact after ending in teaching on boundaries.",
  "You set and keep proper boundaries throughout therapy and after it ends.",
  "What would you do if you met a former client socially?"),
 ('D', 'Work with and make therapeutic use', 's', 'Work,make', 'using the therapeutic contract',
  "Work with the contract's limits and benefits and turn them to therapeutic use.",
  "Ask students to show how they used the contract in the work, not only that they had one.",
  "You use the limits and benefits of your contract with clients as part of the therapy.",
  "When did the contract itself become useful in the work?"),
 ('D', 'Establish and maintain appropriate professional and personal boundaries in online', 's', 'Establish,maintain,ensuring', 'online boundaries with clients',
  "Set and keep fitting personal and professional limits in online relationships with clients or patients, by making sure of the points that follow.",
  "Teach online boundaries, including social media, as part of professional conduct.",
  "You set and keep proper boundaries with clients online, as the points that follow describe.",
  "What would you do if a client found you on social media?"),
 ('D', 'reasonable care is taken to separate', 's', 'taken,separate,maintain', 'separating personal and professional presence online',
  "Take reasonable care to keep one's personal and professional presence on social media apart where mixing them could create harmful dual relationships.",
  "Review students' social media practice as part of professional readiness.",
  "You take care to keep your personal and professional social media apart, so that clients cannot be harmed by a dual relationship.",
  "What can a client see about you online today?"),
 ('D', 'any public, online communication', 's', 'carried', 'public online communication',
  "Make sure any public online communication fits one's own ethical framework or code.",
  "Check students' public posts and profiles against their code.",
  "You make sure anything you post publicly online fits your ethical code.",
  "Does your public profile fit your ethical code?"),
 ('D', 'Establish and maintain a secure frame', 's', 'Establish,maintain', 'a secure frame for the work',
  "Create and keep a secure frame for therapy.",
  "Teach the elements of the frame and assess how students hold it.",
  "You create and hold a secure frame for the work.",
  "What makes up the frame of your sessions?"),
 ('D', 'Negotiate an appropriate therapeutic contract', 's', 'Negotiate,using', 'negotiating the contract',
  "Agree a suitable contract with the client using all the information available.",
  "Assess contracting in recorded or observed practice.",
  "You agree a suitable contract with each client, using everything you know about them.",
  "What information shaped the last contract you agreed?"),
 ('D', 'Recognise and work with breaks and holidays', 's', 'Recognise,work,affect,making', 'breaks, holidays and emergency cover',
  "Recognise and work with breaks and holidays and their effect on the relationship and process, arranging for clients to get support in an emergency.",
  "Teach planning for breaks, including emergency cover for clients.",
  "You plan for breaks and holidays, notice how they affect the work, and make sure clients can get help in an emergency.",
  "How do you prepare a client for your holiday?"),
 ('D', 'Understand the need for and have made', 's', 'Understand,made,communicate', 'arrangements for a sudden ending',
  "Understand why arrangements are needed for one's own sudden or unplanned absence or ending, have made them, and tell the client about them.",
  "Require students to have arrangements in place, such as a clinical will, while on placement.",
  "You have arrangements in place in case you suddenly cannot work, and you tell your clients about them.",
  "Who would contact your clients if you were taken ill tomorrow?"),
 ('D', 'Adapt appropriately to manage different', 's', 'Adapt,manage', 'open-ended and time-limited work',
  "Adjust suitably to different contracted time frames, both open-ended and time-limited.",
  "Give students experience of both time-limited and open-ended work where possible.",
  "You adjust your work to fit both open-ended and time-limited contracts.",
  "How does a six-session limit change the way you work?"),
 ('D', 'Manage contact with external agencies', 's', 'Manage', 'contact with outside agencies',
  "Handle contact with outside agencies and professionals as the client's interest requires.",
  "Teach the protocols for liaising with other agencies, with consent.",
  "You handle contact with outside agencies and professionals in your client's interest.",
  "When would you contact a client's GP, and with whose consent?"),
 ('D', 'Adopt an enquiring, critical awareness', 's', 'Adopt', 'an enquiring, forward-looking stance',
  "Take an enquiring, critical and forward-looking approach to professional challenges, aware of social and therapeutic responsibility.",
  "Encourage students to treat professional problems as questions to explore.",
  "You meet professional challenges with curiosity, a critical eye and a view to the future, mindful of your responsibilities.",
  "What professional question are you curious about right now?"),
]
THR['4.11'] = [
 ('K', 'Understand the concepts and processes of client assessment', 'u', 'Understand', 'client assessment concepts and processes',
  "Understand the ideas and steps of client assessment, as the points that follow set out.",
  "Teach client assessment as a topic in its own right.",
  "You understand what client assessment is and how it is done, as the points that follow set out.",
  "What do you assess in a first meeting with a client?"),
 ('K', 'define and describe the concept', 'k', 'define,describe', 'defining client assessment',
  "Be able to define and explain client assessment.",
  "Ask students to define assessment in the terms of their own model.",
  "You can define and explain what client assessment means.",
  "How would you explain assessment to a new client?"),
 ('K', 'understand different political, philosophical', 'u', 'understand,appraise', 'perspectives on assessment tools and outcome measures',
  "Understand the political, philosophical and theoretical views on assessment tools and outcome measures and judge, from research, what they mean for present-day practice.",
  "Debate outcome measures from several viewpoints, drawing on research.",
  "You understand the arguments about assessment tools and outcome measures and can judge from research what they mean for practice.",
  "What do outcome measures capture, and what do they miss?"),
 ('K', 'critically discuss the contexts in which client', 'u', 'discuss,considering', 'contexts of assessment, law and agency policy',
  "Discuss critically the settings in which assessment takes place, with regard to ethics, law and agency policy.",
  "Compare assessment across settings, with their legal and policy frames.",
  "You can discuss critically where and how assessment happens, with attention to ethics, law and agency rules.",
  "How does assessment differ between your placement and private practice?"),
 ('K', 'demonstrate a working knowledge of at least one approach', 'k', 'demonstrate,discussing,influence', "an assessment approach that fits one's model",
  "Show working knowledge of at least one assessment approach that fits one's core model, and discuss how it shapes the focus and agreed process of the work.",
  "Require students to use and explain an assessment approach consistent with their core model.",
  "You know at least one way of assessing that fits your approach and can explain how it shapes your work with a client.",
  "How does your way of assessing shape what you agree to work on?"),
 ('K', 'understand the risks and challenges experienced', 'u', 'understand', 'suitability for technology-mediated therapy',
  "Understand the risks and difficulties some clients face in being suited to therapy by technology.",
  "Teach screening for remote work.",
  "You understand why some clients may not be suited to therapy online or by phone.",
  "Which clients might you not see online, and why?"),
 ('K', 'understand the risk and protective factors', 'u', 'understand', 'risk and protective factors for client safety',
  "Understand the factors that raise and lower risk to client safety, including self-harm and suicide.",
  "Teach risk and protective factors with current evidence and practice cases.",
  "You understand what raises and lowers a client's risk of harming themselves.",
  "What protective factors would you look for with a client at risk?"),
 ('K', 'understand differences between suicidal ideation', 'u', 'understand,determining', 'thoughts and intent in judging risk',
  "Understand how thinking about suicide differs from intending to act, in judging the level of risk.",
  "Train students to tell thoughts from intent in risk assessment.",
  "You understand the difference between having thoughts of suicide and intending to act, and why it matters for judging risk.",
  "What questions help you tell thoughts apart from intent?"),
 ('K', 'demonstrate a working knowledge of legislative', 'k', 'demonstrate,respond', 'responding to immediate risk',
  "Show working knowledge of the legal, policy or procedural steps for responding to a client at immediate risk.",
  "Rehearse the procedures for immediate risk, including whom to contact.",
  "You know the legal and procedural steps to take when a client is at immediate risk.",
  "What would you do, step by step, if a client was at immediate risk?"),
 ('K', 'Recognise that specific knowledge and skills are required', 'k', 'Recognise,work', 'extra training for particular client groups',
  "Recognise that working with certain client groups and populations needs particular knowledge and skills, and may need more training, above all where competence, capacity, understanding or decision-making are in question.",
  "Signpost specialist training routes and the limits of a generic qualification.",
  "You recognise that some client groups need extra knowledge and training, especially where capacity or understanding is in question.",
  "Which client group would you need more training to work with?"),
 ('K', 'Recognise own competencies in relation', 'k', 'Recognise', "one's own competence across groups and modes",
  "Know one's own competence with particular client groups, approaches, techniques and methods, and with each mode of delivery, remote and in person.",
  "Ask students to map their competence across groups and modes.",
  "You know where your competence lies with different client groups, techniques and ways of delivering therapy.",
  "Where does your competence stop?"),
 ('B', 'Critically aware of the diverse therapeutic perspectives', 's', '', 'perspectives on assessment and formulation',
  "Be critically aware of the different views on assessment and on formulation or conceptualisation, as the points that follow set out.",
  "Present competing views of assessment and formulation.",
  "You are critically aware of the different views on assessment and formulation, as the points that follow set out.",
  "Is formulation helpful or harmful in your approach?"),
 ('B', 'understand arguments for and against', 'u', 'understand', 'arguments for and against formal assessment',
  "Understand the case for and against treating these as formal processes in therapy.",
  "Hold a debate on formal assessment in therapy.",
  "You understand the arguments for and against formal assessment and formulation.",
  "Which side of the argument convinces you more?"),
 ('B', 'critically reflect about how these', 'u', 'reflect,influence', 'how these views shape services and experience',
  "Reflect critically on how these views may shape services and clients' experience.",
  "Ask students to reflect on how assessment practice affects clients.",
  "You reflect critically on how these views shape services and what clients go through.",
  "How might a formal assessment feel from the client's chair?"),
 ('B', 'able to articulate a coherent personal approach', 's', 'articulate,addresses,assessed', 'a personal approach to assessment',
  "Be able to set out a coherent personal approach to counselling that covers how client presentations are assessed and worked with.",
  "Assess a written or spoken account of each student's own approach.",
  "You can set out your own coherent approach, including how you assess and work with what clients bring.",
  "How would you describe your approach in two minutes?"),
 ('B', 'aware of the limitations of one', 's', '', "the limits of one's training in complex work",
  "Be aware of the limits of one's training and experience in judging complex client work and its risks.",
  "Encourage students to name limits early in supervision.",
  "You are aware of where your training and experience fall short in complex or risky work.",
  "What kind of case would you hand on?"),
 ('B', 'knowledgeable about networks of support', 'k', '', 'support and referral networks',
  "Know the networks of support and referral open to clients.",
  "Have students map local support and referral options.",
  "You know the support and referral networks available to your clients.",
  "Where could you refer a client locally?"),
 ('D', 'Understand and be able to discuss the client', 's', 'Understand,discuss,articulate,address', "discussing the client's concerns and how therapy helps",
  "Understand and talk through the client's concerns with them and explain how therapy can help with them.",
  "Assess how students open the work and explain therapy to clients.",
  "You can talk through a client's concerns with them and explain how therapy could help.",
  "How do you explain what therapy can offer?"),
 ('D', 'Determine whether each individual client', 's', 'Determine,engage,make', 'client competence and capacity for the approach',
  "Judge whether each client has the competence and capacity to engage with and use the approach offered, in the setting where it is delivered.",
  "Teach capacity checks within assessment.",
  "You judge whether each client can engage with and use the therapy you offer, in the setting it is offered in.",
  "How would you know a client cannot use what you offer?"),
 ('D', 'Provide a clear explanation of the stated', 's', 'Provide', 'explaining the approach and each role',
  "Explain the approach clearly, including why each party contributes as they do.",
  "Assess the clarity of students' explanations to clients.",
  "You explain your approach clearly, including what you and the client each bring.",
  "What do you tell a client about their part in the work?"),
 ('D', 'Actively seek to work within one', 's', 'seek,work', "staying within one's competence",
  "Make an active effort to stay within one's competence, whatever the client group, approach, technique, method or delivery mode.",
  "Monitor in supervision that students take on only work within their competence.",
  "You make a point of staying within your competence, whatever the client group or way of working.",
  "When did you decline or refer work because it was beyond you?"),
 ('D', 'Competently conduct an episode of therapy', 's', 'conduct,includes', 'conducting an episode of therapy',
  "Carry out an episode of therapy competently and in keeping with a stated approach, including assessment of needs and goals, identifying risk and a coherent plan, as the points that follow set out.",
  "Assess at least one full episode of therapy from assessment through plan to ending.",
  "You can carry out a full episode of therapy in line with your approach, from assessing needs, goals and risk to a clear plan.",
  "Take me through one client's work from first meeting to ending."),
 ('D', 'undertake a comprehensive evaluation', 's', 'undertake', 'evaluating needs and goals',
  "Carry out a thorough evaluation of the client's needs and goals.",
  "Assess the depth of students' needs assessment.",
  "You evaluate thoroughly what each client needs and wants from therapy.",
  "What does this client want from therapy, in their words?"),
 ('D', 'develop a conceptualisation or formulation', 's', 'develop', 'building a formulation',
  "Build a conceptualisation or formulation of what may be going on for the client, drawing on theory and on the work as it unfolds.",
  "Require a written formulation revised as the work proceeds.",
  "You build an understanding of what may be going on for a client, drawing on theory and on the work as it develops.",
  "How has your formulation of this client changed over time?"),
 ('D', 'identify and evaluate presenting risks', 's', 'identify,evaluate', 'identifying presenting risk',
  "Identify and weigh the risks the client presents with.",
  "Assess risk identification in casework.",
  "You identify and weigh any risks a client brings.",
  "What risks did this client bring at the start?"),
 ('D', 'devise and agree a contract', 's', 'devise,agree', 'a contract and plan with review points',
  "Draw up and agree a contract and plan for the work, covering what, how and when, with review points to reassess and decide when the work is done.",
  "Check that plans include review points and a route to ending.",
  "You draw up and agree a plan with each client, covering what you will do, how and when, with points to review it and decide when to finish.",
  "When will you and this client next review the work?"),
 ('D', 'Apply appropriate strategies and interventions', 's', 'Apply', 'interventions for particular populations',
  "Use strategies and interventions suited to the modality with particular client populations and experiences.",
  "Assess how students adapt interventions to particular populations.",
  "You use strategies and techniques suited to your approach and to particular groups of clients.",
  "How did you adapt your work for a particular client group?"),
 ('D', 'Make informed decisions about referral', 's', 'Make', 'referral decisions',
  "Make well-founded decisions about referring clients to suitable agencies.",
  "Review referral decisions in supervision.",
  "You make well-founded decisions about referring clients to other services.",
  "What did you weigh up in your last referral decision?"),
]
THR['4.12'] = [
 ('K', 'Understand the concept of the therapeutic relationship', 'u', 'Understand', 'the relationship across approaches',
  "Understand the therapeutic relationship as several theoretical approaches see it.",
  "Compare accounts of the relationship across approaches.",
  "You understand how different approaches see the therapeutic relationship.",
  "What does your approach say heals in the relationship?"),
 ('K', 'Demonstrate understanding of a range of therapeutic approaches', 'u', 'Demonstrate,help,make,voice', 'approaches and evidence to support client choice',
  "Show understanding of a range of approaches, their theory and the evidence for their effectiveness, so that clients can make informed choices or state preferences that suit their needs.",
  "Teach the evidence base across approaches so that students can support informed client choice.",
  "You understand a range of approaches, their theory and the evidence for them, so you can help clients choose what suits them.",
  "How would you help a client choose between two kinds of therapy?"),
 ('K', 'Understand the theoretical dynamics of power', 'u', 'Understand,affect', 'power, oppression and privilege in the relationship',
  "Understand the theory of power, oppression and privilege and how they may bear on the relationship.",
  "Teach theories of power and privilege and apply them to the therapy room.",
  "You understand how power, oppression and privilege can affect the therapeutic relationship.",
  "Where does privilege show up between you and your clients?"),
 ('B', 'Respectful of difference, for example', 's', 'embracing,respecting,accepting,honouring', 'respect for sexual diversity and difference',
  "Respect difference, for instance by welcoming sexual diversity and respecting and honouring each client's sexual orientation and choices.",
  "Address sexual diversity directly in teaching and in practice assessment.",
  "You respect difference, including welcoming and honouring each client's sexual orientation and choices.",
  "How do you make sure clients of any orientation feel safe with you?"),
 ('B', 'Open to ensuring a saf', 's', 'ensuring,support', "a safe space for identity without imposing one's views",
  "Be willing to provide a safe space for clients to talk honestly about their experience, supporting healthy self-identities without imposing one's own values, views or expectations.",
  "Assess whether students hold their own views back while supporting clients' identities.",
  "You offer a safe space for clients to talk honestly about who they are, without pushing your own values or expectations.",
  "How do you notice when your own views are creeping in?"),
 ('B', 'Competent to work therapeutically and non-defensively', 's', 'work,taking', 'repairing ruptures without defensiveness',
  "Be competent to work therapeutically and without defensiveness in hard situations, taking account of one's own limits when repairing empathic failures and ruptures.",
  "Use recorded sessions to assess how students repair ruptures.",
  "You can work openly and without getting defensive in hard moments, and repair misunderstandings and ruptures with clients.",
  "Tell me about a rupture you repaired."),
 ('D', 'Monitor own bias through', 's', 'Monitor', 'monitoring bias through supervision and therapy',
  "Keep watch on one's own bias through self-supervision, supervision and personal therapy.",
  "Make monitoring bias a routine part of supervision.",
  "You keep watch on your own bias through self-reflection, supervision and your own therapy.",
  "How do you check your bias between sessions?"),
 ('D', 'Identify, reflect on and work openly', 's', 'Identify,reflect,work', 'differences between client and counsellor',
  "Identify, reflect on and work openly with differences of social position, culture and identity between client and counsellor, and their effect on the relationship.",
  "Assess how students name and work with difference in sessions.",
  "You notice, reflect on and talk openly about differences between you and your client and how they affect the work.",
  "When did you raise a difference between you and a client?"),
 ('D', 'Recognise and work with component aspects', 's', 'Recognise,work', 'the parts of the therapeutic alliance',
  "Recognise and work with the parts of the alliance, such as client motivation, commitment to the process and the contract.",
  "Teach the components of the alliance and assess students' work with them.",
  "You recognise and work with what holds the alliance together, such as motivation, commitment and the contract.",
  "What is this client's motivation, and how do you know?"),
 ('D', 'Recognise and take steps to mitigate', 's', 'Recognise,take,mitigate', 'the power imbalance in therapy',
  "Recognise the power imbalance built into the therapy relationship and act to reduce it.",
  "Discuss practical ways to reduce power imbalance.",
  "You recognise the built-in power imbalance in therapy and take steps to reduce it.",
  "What do you do to share power in sessions?"),
 ('D', 'Recognise own conscious and unconscious bias', 's', 'Recognise,demonstrate', 'anti-discriminatory practice',
  "Recognise one's own conscious and unconscious bias and show anti-discriminatory practice in the relationship, respecting every client's rights and responsibilities whatever their background, identity or beliefs.",
  "Assess anti-discriminatory practice directly on placement and in recorded work.",
  "You recognise your own biases and show in your work that you treat every client fairly, whatever their background, identity or beliefs.",
  "What does anti-discriminatory practice look like in your sessions?"),
 ('D', 'Establish and sustain a therapeutic alliance', 's', 'Establish,sustain,respects', 'an alliance that respects client goals',
  "Build and keep an alliance that respects the client's goals and preferred way of working together.",
  "Check that students ask about and honour client preferences.",
  "You build and keep a working alliance that respects what each client wants and how they want to work.",
  "How did you find out how this client likes to work?"),
 ('D', 'Recognise and work therapeutically with difficulties', 's', 'Recognise,work', 'difficulties and ruptures',
  "Notice and work therapeutically with ruptures and other difficulties in the relationship.",
  "Teach rupture and repair with case examples.",
  "You notice and work through difficulties and ruptures in the relationship.",
  "What signals a rupture for you?"),
 ('D', 'Regularly review and work therapeutically', 's', 'review,work', "the client's view of therapist and therapy",
  "Review regularly, and work with, how the client sees the therapist and the therapy.",
  "Encourage routine client feedback within sessions.",
  "You check regularly how your client sees you and the therapy, and work with what they say.",
  "How do you ask clients what they think of the work?"),
 ('D', 'Practise in a way that is transparent', 's', 'Practise', 'transparent, inclusive practice including marketing',
  "Practise openly, inclusively and without discrimination, including in advertising and marketing, following professional body guidance and the law.",
  "Include ethical marketing in teaching on professional practice.",
  "You practise openly and fairly, including in how you advertise, following professional guidance and the law.",
  "Does the way you would advertise your practice include everyone?"),
]
THSUB = {'4.6': 'Professional context', '4.7': 'Understanding people and their experiences', '4.8': 'The therapist', '4.9': 'Ethical/legal',
         '4.10': 'Boundaries and contracting', '4.11': 'Assessment', '4.12': 'The therapeutic relationship', '4.13': 'Generic skills'}
ITEMKBD = {}
for _n, _rows in THR.items():
    _cuts = _cut(_n, [r[1] for r in _rows])
    for _k, (r, (txt, p)) in enumerate(zip(_rows, _cuts), 1):
        kbd, _st, dm, vb, ab, pa, pr, be, qq = r
        _id = f'{_n}.b{_k}'
        ITEMKBD[_id] = KBD[kbd]
        s(_id, find=txt, after=p, type='threshold', rung='threshold', force='threshold', forceFrom='4.4', level='fheq:6',
          appliesTo='graduates with honours in Counselling and Psychotherapy', addressee='learner',
          verbs=[v for v in vb.split(',') if v], about=ab, domain=DOM[dm], award=HON, para=pa, prac=pr, ben=be, q=qq)

# 4.13 generic skills at honours (threshold section; lead-in "should be able to")
_GS = [
 ('assigned,participating', 'teamwork and discussion', "Carry out allocated tasks in a team and take part in discussion.", "Assess group tasks for each student's own contribution.", "You carry out your share of a team's work and join in discussion.", "What did you contribute to your last group task?", 'qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r3/3rd at spine:6'),
 ('', 'drawing information together from sources', "Gather information and material from different sources.", "Set tasks that need several kinds of source.", "You gather information and material from different sources.", "How do you pull sources together for an essay?", None),
 ('', 'identifying problems and questions', "Pick out problems and questions.", "Ask students to frame questions from cases.", "You pick out problems and questions to pursue.", "What question did your last case raise for you?", 'qaa/fheq-2024/4.15.b7 at spine:6'),
 ('undertake', 'analysing factual information', "Analyse factual information.", "Include data or factual analysis in assessment.", "You analyse factual information.", "What did the facts of a case tell you that your first impression missed?", 'qaa/fheq-2024/4.15.b3.1 at spine:6'),
 ('recognise', "weighing others' arguments", "See the strong and weak points in other people's arguments.", "Use critique of published arguments in seminars.", "You can see the strong and weak points in other people's arguments.", "Whose argument have you questioned recently, and why?", 'qaa/fheq-2024/4.15.b7 at spine:6'),
 ('produce', 'synthesising knowledge on a topic', "Bring together the current state of knowledge on a topic.", "Set literature reviews that require synthesis, not summary.", "You can bring together what is known on a topic.", "What is the current state of knowledge on a topic you care about?", 'qaa/fheq-2024/4.15.b5 at spine:6'),
 ('', 'working independently with guidance', "Work on tasks independently, with guidance.", "Give supervised independent tasks with clear check-ins.", "You can work on tasks on your own, with guidance.", "Which task did you complete mostly on your own?", 'qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/annex-d/transferable/r4/3rd at spine:6'),
 ('make', 'reflecting on progress and using feedback', "Reflect on one's own progress and use the feedback given.", "Ask students to log feedback and what they did with it.", "You reflect on your progress and use the feedback you get.", "What did you change after your last piece of feedback?", 'qaa/fheq-2024/annex-d/transferable/r5/3rd at spine:6'),
 ('express', 'oral and written expression', "Express oneself well in speech and in writing.", "Assess both oral and written communication.", "You express yourself well in speech and in writing.", "Which do you find harder, speaking or writing, and why?", None),
 ('present', 'presenting knowledge or argument clearly', "Put knowledge or an argument across in a way others understand.", "Assess clarity for a non-specialist audience.", "You put knowledge or an argument across so others understand it.", "How would you explain your approach to someone outside the field?", None),
 ('use,collate,analyse,select,present', 'digital literacy', "Use suitable IT to collect, analyse, choose and present information.", "Build digital literacy into assessed tasks.", "You use the right digital tools to collect, analyse, choose and present information.", "Which digital tools do you rely on for study?", 'qaa/fheq-2024/annex-d/transferable/r2/3rd at spine:6'),
 ('make', 'presentations', "Give effective presentations.", "Include assessed presentations.", "You give effective presentations.", "What feedback did your last presentation get?", None),
 ('think,show', 'critical evaluation of theory, modalities and methods', "Think critically and evaluate theoretical concepts, therapeutic modalities and research methods.", "Assess critical evaluation of theory, approaches and methods.", "You think critically about theory, approaches to therapy and research methods.", "What is the weakest point of your favourite approach?", 'qaa/fheq-2024/4.15.b7 at spine:6'),
 ('demonstrate,comprehend', 'grasping new ideas', "Show that one can grasp new ideas or information.", "Introduce unfamiliar material and check understanding.", "You can grasp new ideas or information when they come up.", "What new idea did you have to get to grips with recently?", 'qaa/fheq-2024/4.15.b4 at spine:6'),
 ('demonstrate,recognising,describing', 'recognising and describing material', "Show skill in recognising and describing material.", "Use observation tasks that need accurate description.", "You can recognise and describe material accurately.", "How would you describe what happened in a session without judging it?", None),
 ('demonstrate,describing', 'classifying data', "Show skill in classifying data by describing, sorting and collating it.", "Include tasks that sort and categorise data.", "You can sort, group and describe data.", "How did you organise the data in your last project?", None),
 ('understand', 'health, safety and inclusion at work', "Understand why health and safety and equality, diversity and inclusion matter at work.", "Cover workplace safety and inclusion in preparation for placement.", "You understand why health and safety, equality and inclusion matter at work.", "What safety and inclusion checks does your placement make?", None),
 ('appreciate,engage', 'debates on sustainability, employability and global perspectives', "Value and take part in current debates on global sustainability, employability and global perspectives, including decolonisation and anti-racism.", "Bring debates on sustainability, decolonisation and anti-racism into the curriculum.", "You take part in current debates on sustainability, work and global questions, including decolonisation and anti-racism.", "How does decolonisation bear on the theories you are taught?", None),
 ('appreciate,act', 'acting sustainably', "Value the need to act sustainably.", "Make sustainable practice part of course life and placement.", "You see why you need to act sustainably.", "What could you change to practise more sustainably?", None),
]
for _k, (_v, _a, _p, _pr, _b, _q, _fw) in enumerate(_GS, 1):
    _kw = dict(fw=_fw) if _fw else {}
    s(f'4.13.b{_k}', type='threshold', rung='threshold', force='threshold', forceFrom='4.4', level='fheq:6',
      appliesTo='graduates with honours in Counselling and Psychotherapy', addressee='learner', verbs=[x for x in _v.split(',') if x],
      about=_a, domain='generic-skill', award=HON, para=_p, prac=_pr, ben=_b, q=_q, **_kw)
P['4.13.b19'].update(find='appreciate the need to act in a sustainable manner.', after=81154)
for _k in range(1, 20):
    ITEMKBD[f'4.13.b{_k}'] = 'Generic skills'

# master's threshold: 4.16, 4.17
_M16 = [
 ('understand,advanced', 'understanding', 'how research advances knowledge', "Understand how research moves knowledge forward.", "Teach how knowledge in the field is built through research.", "You understand how research moves knowledge in your field forward.", "How has research changed practice in your field in the last decade?", 'qaa/fheq-2024/4.17.b3 at spine:7'),
 ('identify', 'knowledge', 'the boundaries of knowledge', "Identify where current knowledge ends.", "Ask students to locate the edges of knowledge on their topic.", "You can tell where current knowledge ends.", "Where does what is known about your topic run out?", 'qaa/fheq-2024/4.17.b1 at spine:7'),
 ('create', 'subject-skill', 'new insight in the field', "Create new insight in the field.", "Value original insight in assessment.", "You create new insight in your field.", "What new insight has your work produced?", 'qaa/fheq-2024/4.17.b3 at spine:7'),
 ('develop', 'generic-skill', 'self-directed higher-level development', "Build higher-level skills by directing one's own academic and professional growth.", "Give students room to direct their own development.", "You build higher-level skills by directing your own academic and professional development.", "What are you developing on your own initiative?", 'qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b8.3 at spine:7'),
 ('demonstrate,extends', 'knowledge', 'a systematic, research-informed knowledge base', "Holders of the award must show systematic understanding and critical awareness of topics informed by research at the forefront of counselling and psychotherapy.", "Assess systematic, critical command of current research across the key topics.", "You must show a systematic, critical grasp of topics shaped by the newest research in your field.", "Which topic could you speak on at the forefront of current research?", 'qaa/fheq-2024/4.17.b1 at spine:7'),
]
for _k, (_v, _d, _a, _p, _pr, _b, _q, _fw) in enumerate(_M16, 1):
    s(f'4.16.b{_k}', type='threshold', rung='threshold', force='must' if _k == 5 else 'threshold', forceFrom='4.17', level='fheq:7',
      appliesTo="holders of a master's degree in Counselling and Psychotherapy", addressee='learner', verbs=_v.split(','), about=_a,
      domain=_d, award=MA, para=_p, prac=_pr, ben=_b, q=_q, fw=_fw)
P['4.16.b4'].update(find='develop higher level skills through self-directed academic and professional development.', after=83127)
P['4.16.b5'].update(find='At this level, award holders must demonstrate a knowledge base that extends to a systematic understanding and critical awareness of topics which are informed by research at the forefront of the discipline of counselling/psychotherapy.', after=83127)
_M17 = [
 ('carried', 'generic-skill', 'independent, original critical analysis', "Discuss and analyse complex concepts critically, working independently and with some originality.", "Assess independent, original critical analysis of complex ideas.", "You discuss and analyse complex ideas critically, on your own and with some originality.", "Where has your own thinking gone beyond what you were taught?", 'qaa/fheq-2024/4.17.b6 at spine:7'),
 ('inform,influence,underpin', 'knowledge', 'the history, culture and philosophy of the field', "Be critically aware of the history of ideas, culture, philosophy and social and political theory behind the field's development and one's own approach.", "Teach the intellectual history of therapy and link it to each student's approach.", "You understand critically where the field's ideas came from and how they underpin your own approach.", "Which ideas from history shape your approach most?", 'qaa/fheq-2024/4.17.b1 at spine:7'),
 ('conceptualising,formulating', 'subject-skill', 'formulating work with long-term mental health issues', "Conceptualise or formulate ways of working with clients whose mental health problems are chronic and lasting.", "Include chronic and enduring presentations in case teaching.", "You can work out ways of working with clients who have long-lasting mental health problems.", "How would your formulation change for a client with a long-term condition?", 'qaa/fheq-2024/4.17.b5 at spine:7'),
 ('', 'understanding', 'discourses of diagnosis and psychopathology', "Understand critically the language and discourses of diagnosis, psychopathology and mental disorder.", "Examine diagnostic language critically in teaching.", "You understand critically how diagnosis and mental disorder are talked about.", "What does a diagnostic label do to the way a client is seen?", 'qaa/fheq-2024/4.17.b4.1 at spine:7'),
 ('communicating,reduce', 'subject-skill', 'speaking about discriminatory harm and power', "Speak about the harm done by discriminatory practice and work to reduce insensitivity to power differences in services, training and supervision.", "Assess how students address discrimination and power across services, training and supervision.", "You speak up about the harm discrimination causes and work to reduce blindness to power in services, training and supervision.", "Where have you named a power difference others had missed?", 'qaa/fheq-2024/4.17.b8.2 at spine:7'),
 ('shape,work', 'understanding', 'unconscious processes and ruptures', "Understand critically how processes outside awareness in client and therapist may shape perception and the work, and work therapeutically with ruptures that arise.", "Teach processes outside awareness and their part in ruptures, with case material.", "You understand how processes outside awareness in you and your client shape the work, and you work with ruptures when they happen.", "What might be going on outside awareness in a stuck piece of work?", 'qaa/fheq-2024/4.17.b5 at spine:7'),
 ('integrating', 'subject-skill', 'bringing diversity research into practice', "Bring theory and research on diversity and equality into clinical practice.", "Look for diversity research in students' clinical reasoning.", "You bring theory and research on diversity and equality into your clinical work.", "Which piece of research on diversity has changed your practice?", 'qaa/fheq-2024/4.17.b3 at spine:7'),
 ('utilising,contribute,improving', 'subject-skill', 'audit and evaluation to improve therapy', "Use audit and evaluation methods to help improve the process and outcomes of therapy.", "Include a service audit or evaluation task.", "You use audit and evaluation to help improve how therapy is done and what it achieves.", "What would you audit in your service first?", 'qaa/fheq-2024/4.17.b2 at spine:7'),
 ('developing,planning,implementing,evaluating', 'subject-skill', 'a substantial research study', "Design, plan, carry out and evaluate a substantial empirical study or systematic review that answers a relevant question and adds to knowledge in the field.", "Supervise a substantial study through each stage, from question to evaluation.", "You design, carry out and evaluate a substantial research study that answers a real question and adds to what is known.", "What question will your research study answer, and why does it matter?", 'qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b3 at spine:7'),
 ('work', 'subject-skill', 'reflexive use of self for in-depth work', "Use reflexivity, self-awareness and the self therapeutically to work in depth in the relationship and process.", "Assess depth of reflexive work in recorded sessions and supervision.", "You use reflexivity, self-awareness and yourself to work in depth with clients.", "How do you use yourself to deepen the work?", 'qaa/fheq-2024/4.17.b6 at spine:7'),
 ('facilitating,containing,emerge', 'subject-skill', 'holding intense emotion', "Facilitate or contain intense emotion in a highly charged encounter.", "Prepare students to hold strong emotion, with supervision close at hand.", "You can stay with and contain strong emotion when a session becomes highly charged.", "How do you stay steady when a client's feelings are overwhelming?", 'qaa/fheq-2024/4.17.b8.2 at spine:7'),
]
for _k, (_v, _d, _a, _p, _pr, _b, _q, _fw) in enumerate(_M17, 1):
    s(f'4.17.b{_k}', type='threshold', rung='threshold', force='threshold', forceFrom='4.17', level='fheq:7',
      appliesTo="holders of a master's degree in Counselling and Psychotherapy", addressee='learner', verbs=[x for x in _v.split(',') if x],
      about=_a, domain=_d, award=MA, para=_p, prac=_pr, ben=_b, q=_q, fw=_fw)
for _k in range(1, 6): ITEMKBD[f'4.16.b{_k}'] = "Benchmark standard for master's degrees"
for _k in range(1, 12): ITEMKBD[f'4.17.b{_k}'] = "Benchmark standard for master's degrees"

GRADE = {}

# =============================================================== agent instructions (ours)
SID = 'qaa/counselling-and-psychotherapy-2022/'
CITE = '(QAA, 2022, Counselling and Psychotherapy Subject Benchmark Statement, %s)'
FW = {('fheq:6', 'knowledge'): 'qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r1/3rd',
      ('fheq:6', 'understanding'): 'qaa/fheq-2024/4.15.b4 (qaa/fqheis-2024/4.16.b2) at spine:6, with qaa/fheq-2024/annex-d/knowledge/r2/3rd',
      ('fheq:6', 'subject-skill'): 'qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2) at spine:6, with qaa/fheq-2024/annex-d/professional/r1/3rd-1st',
      ('fheq:6', 'generic-skill'): 'qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) at spine:6, with qaa/fheq-2024/annex-d/transferable/r2/3rd',
      ('fheq:6', 'none'): 'qaa/fheq-2024/4.15.b1 at spine:6',
      ('fheq:7', 'knowledge'): 'qaa/fheq-2024/4.17.b1 at spine:7', ('fheq:7', 'understanding'): 'qaa/fheq-2024/4.17.b3 at spine:7',
      ('fheq:7', 'subject-skill'): 'qaa/fheq-2024/4.17.b5 at spine:7', ('fheq:7', 'generic-skill'): 'qaa/fheq-2024/4.17.b6 at spine:7'}
FORCEW = {'should': 'an expectation worded with "should"', 'must': 'a requirement worded with "must"', 'will': 'an expected feature worded with "will"',
          'may': 'an option worded with "may"', 'threshold': 'a minimum the award requires',
          'describes': 'an expectation stated without one of the five obliging words (force recorded as describes)'}

def _order(i):
    base, _, b = i.partition('.b')
    return tuple(int(x) for x in base.split('.')) + ((int(b),) if b else (0,))
_IDS = sorted(P, key=_order)

def _loc(i):
    base, _, b = i.partition('.b')
    if not b:
        return 'para ' + i
    if i in ITEMKBD and base in THSUB and base != '4.13':
        return f'para {base}, {THSUB[base]}, under {ITEMKBD[i]}'
    return f'para {base}, bullet {b}'

def _nb(i):
    base = i.partition('.b')[0]; k = _IDS.index(i)
    near = [x for x in (_IDS[k - 1] if k else None, _IDS[k + 1] if k + 1 < len(_IDS) else None) if x and x.partition('.b')[0] == base]
    return ' and '.join(SID + x for x in near) or "the statement's section %s" % i.split('.')[0]

def _awd(r):
    aw = r['award']
    if isinstance(aw, list):
        return "both the honours degree and the master's degree"
    return {'none': 'any Counselling and Psychotherapy course the statement covers', HON: 'the honours degree', MA: "the master's degree"}[aw]

for _i in _IDS:
    r = P[_i]
    q = r.pop('q', "What would you point to as evidence that this is met?")
    fwo = r.pop('fw', None)
    cite = CITE % _loc(_i)
    fw = fwo or FW.get((r['level'], r['domain']), 'the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6 and the master\'s descriptor qaa/fheq-2024/4.17.b1 at spine:7')
    if r['rung'] == 'threshold' and r['level'] == 'fheq:6':
        r['aaw'] = (f"Write about this as one of the threshold standards for the honours degree in Counselling and Psychotherapy at FHEQ level 6 (FQHEIS level 10), "
                    f"listed under {ITEMKBD[_i]}: the minimum every graduate meets on {r['about']}. Cite it as {cite}. "
                    f"Do not call it a regulatory or accreditation requirement, a description of 2:1 or first-class work, or a standard for the master's degree. "
                    f"Set it beside {_nb(_i)} and the descriptor {fw}.")
        r['aad'] = (f"Raise it when a student asks what they must be able to show on {r['about']} by the end of training, or when staff check a module, placement or portfolio against it. "
                    f"Put it to a student plainly, as 'you', and as the floor for the award; to staff, as a minimum the course has to evidence for every graduate. "
                    f"Ask: {q} Do not read the issuer's text aloud at length or suggest that meeting it earns more than a pass.")
    elif r['rung'] == 'threshold':
        r['aaw'] = (f"Write about this as part of the threshold for the master's degree in Counselling and Psychotherapy at FHEQ level 7 (FQHEIS level 11), on {r['about']}; "
                    f"it is {FORCEW[r['force']]}. Cite it as {cite}. Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for the honours degree. "
                    f"Set it beside {_nb(_i)}, the honours threshold in paras 4.6 to 4.13 that it builds on, and the descriptor {fw}.")
        r['aad'] = (f"Raise it when a master's student or course team asks what the minimum looks like for {r['about']}. "
                    f"Put it plainly to a student, as 'you'; to staff, as the floor the master's award sets. "
                    f"Ask: {q} Do not read the issuer's list aloud at length or present it as the honours standard.")
    elif r['addressee'] == 'provider':
        r['aaw'] = (f"Write about this as {FORCEW[r['force']]} on the course and its team, on {r['about']}, holding for {_awd(r)}. "
                    f"Cite it as {cite}. Do not present it as a regulatory or accreditation requirement, and do not turn it into an outcome a student must show. "
                    f"Set it beside {_nb(_i)}, and where it shapes outcomes beside {fw}.")
        r['aad'] = (f"Raise it with a programme team or teacher who is designing, reviewing or defending how the course handles {r['about']}. "
                    f"Frame it for staff as {FORCEW[r['force']]}, and ask: {q} "
                    f"Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve.")
    else:
        r['aaw'] = (f"Write about this as {FORCEW[r['force']]} for {_awd(r)}, on {r['about']}; it sits outside the rung lists of section 4. "
                    f"Cite it as {cite}. Do not claim it is a regulatory requirement or part of the threshold standard itself. "
                    f"Set it beside {_nb(_i)} and the framework descriptor {fw}.")
        r['aad'] = (f"Bring it up when a student or a course team asks about {r['about']}. "
                    f"Tell a student in plain words, as 'you', what it means for their training; for staff, frame it as {FORCEW[r['force']]}. "
                    f"Ask: {q} Avoid long quotation of the issuer's text.")

# =============================================================== front matter and sections
META = dict(
    run='0096', p1='2026-10-03 16:58',
    title='Subject Benchmark Statement Counselling and Psychotherapy', heading='Subject Benchmark Statement: Counselling and Psychotherapy (QAA, March 2022)',
    edition='March 2022 (second edition)', published='2022-03',
    status='current', supersedes='the first Counselling and Psychotherapy statement (2013), named only through its advisory group list (section 6); the front matter lists the key changes',
    subjects=[dict(scheme='hecos', code='100495', label='counselling', basis='stated'),
              dict(scheme='hecos', code='100254', label='psychotherapy', basis='stated'),
              dict(scheme='cah', code='CAH02-06-07', label='counselling, psychotherapy and occupational therapy', basis='stated')],
    awards=[HON, MA], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 revision series with cross-cutting themes (published 30 March 2022)',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("QAA's UK reference point for what a graduate in Counselling and Psychotherapy should know, be and do, for the honours degree and the master's degree. "
                     "Reach for it when designing, approving, reviewing or describing a counselling or psychotherapy course, its placement, its outcomes or its assessment. "
                     "Its honours standards are a threshold only, set out under Know, Be and Do across seven practice areas plus generic skills, with higher classes left to institutional marking schemes and Annex D; "
                     "its master's standards add a further threshold. It favours no single modality, is not a regulatory requirement and does not replace a professional body's accreditation standards."),
    summary=("Published by QAA on 30 March 2022 as the second edition, the statement covers bachelor's degrees with honours and master's degrees in Counselling and Psychotherapy, written to suit any core modality. "
             "It sets the subject's context and purposes (alleviating psychological distress through collaborative, reflective and reflexive practice in many settings), "
             "four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability, framed by the eight UNESCO competencies; and employability, enterprise and entrepreneurship), "
             "the distinctive features of personal development, progression, flexibility, partnership and review, a curriculum on five pillars (theory, professional skills practice, personal and professional development, research) "
             "with a mandatory assessed and supervised placement, and benchmark standards: an honours threshold in seven practice areas under Know, Be and Do plus nineteen generic skills, "
             "typical and excellent levels left to institutional marking schemes and Annex D, and a master's threshold. It notes there is no single PSRB and lists the PSA's accredited registers."),
    authority='reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland and part of quality requirements in Northern Ireland (D1, Relationship to legislation and regulation)')

S2 = dict(
    governs="what can be expected of a graduate in Counselling and Psychotherapy, in what they know, do and understand, and the nature of awards in the subject (D1, front matter; 4.1; 4.4)",
    awards=["bachelor's degrees with honours, including joint honours (2.6, 2.7)", "master's degrees (2.8, 4.16, 4.17)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    howUsed=['design', 'approval', 'review', 'other: external examining (2.15); PSRBs, prospective students and employers (front matter); earlier awards at Levels 4 and 5 may use it as a reference (3.1)'],
    doesNot="it favours no theoretical approach and addresses generic work rather than specific conditions; it is not a national curriculum, does not prescribe teaching, learning or assessment and carries no statutory or regulatory requirement; other related awards have their own standards (D1, front matter)",
    statedScope='"This Subject Benchmark Statement refers to bachelor\'s degrees with honours and master\'s degrees in Counselling and Psychotherapy." (D1, front matter)',
    statedSubjects=[
        dict(name='Counselling and Psychotherapy', locator='(D1, title; front matter)', kind='subject',
             codes=[dict(scheme='hecos', code='100495', label='counselling'), dict(scheme='hecos', code='100254', label='psychotherapy'),
                    dict(scheme='cah', code='CAH02-06-07', label='counselling, psychotherapy and occupational therapy')]),
        dict(name='gestalt, person-centred, cognitive behavioural therapy, psychodynamic, integrative', locator='(D1, 1.8)', kind='specialism', codes=[]),
        dict(name='Joint honours with Counselling and Psychotherapy', locator='(D1, 2.7)', kind='programme title', codes=[dict(scheme='hecos', code='100495', label='counselling')])])

SECTIONS = {'1': 'Context and purposes of a Counselling and Psychotherapy degree', '2': 'Distinctive features of a Counselling and Psychotherapy degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.6', 'Context'), ('1.7', '1.8', 'Purposes of Counselling and Psychotherapy'), ('1.9', '1.11', 'Equality, diversity and inclusion'),
       ('1.12', '1.12', 'Sustainability: Developing sustainable development knowledge'), ('1.13', '1.13', 'Sustainability: Developing sustainable development competencies'),
       ('1.14', '1.14', 'Sustainability: Developing learning environments to promote sustainable development'),
       ('1.15', '1.28', 'Employability, enterprise and entrepreneurship education'), ('2.1', '2.1', 'Distinctive features of a Counselling and Psychotherapy degree'),
       ('2.2', '2.2', 'Personal development'), ('2.3', '2.4', 'Accessibility'), ('2.5', '2.8', 'Progression'), ('2.9', '2.9', 'Flexibility'),
       ('2.10', '2.12', 'Partnership'), ('2.13', '2.16', 'Monitoring and review'), ('3.1', '3.4', 'Content'), ('3.5', '3.6', 'Content: Theory'),
       ('3.7', '3.7', 'Content: Professional skills practice'), ('3.8', '3.8', 'Content: Personal development'), ('3.9', '3.9', 'Content: Professional development'),
       ('3.10', '3.10', 'Content: Research'), ('3.11', '3.22', 'Teaching and learning'), ('3.23', '3.28', 'Assessment'), ('4.1', '4.5', 'Introduction'),
       ('4.6', '4.6', 'Threshold level (3rd class): Professional context'), ('4.7', '4.7', 'Threshold level (3rd class): Understanding people and their experiences'),
       ('4.8', '4.8', 'Threshold level (3rd class): The therapist'), ('4.9', '4.9', 'Threshold level (3rd class): Ethical/legal'),
       ('4.10', '4.10', 'Threshold level (3rd class): Boundaries and contracting'), ('4.11', '4.11', 'Threshold level (3rd class): Assessment'),
       ('4.12', '4.12', 'Threshold level (3rd class): The therapeutic relationship'), ('4.13', '4.13', 'Threshold level (3rd class): Generic skills'),
       ('4.14', '4.14', 'Typical level (2:2 or 2:1)'), ('4.15', '4.15', 'Excellent level (1st class)'), ('4.16', '4.17', "Benchmark standard for master's degrees")]

G = {
 '1.1': 'what counsellors and psychotherapists do', '1.2': 'courses prepare reflective, reflexive practitioners', '1.3': 'settings of client work',
 '1.4': 'forms of service, read in context', '1.5': 'modalities and modes of delivery', '1.6': 'engagement with the therapeutic community; ethics; UNESCO',
 '1.7': 'purposes of training; reflective and reflexive self-awareness', '1.8': 'modalities, common training content, career routes, no single PSRB',
 '1.9': 'inclusive training and diverse staff', '1.10': 'experiential learning; inclusive content and assessment', '1.11': 'open educators and accessible curricula',
 '1.12': 'sustainable development knowledge in the profession', '1.13': 'the eight UNESCO competencies', '1.14': 'learning environments for sustainable development',
 '1.15': 'growth in demand and posts', '1.16': 'knowing and showing the value of skills', '1.17': 'what an entrepreneurial mindset involves',
 '1.18': 'purpose of EEEE', '1.19': 'enterprise behaviours', '1.20': 'enterprise attributes', '1.21': 'competencies for employed or self-employed work',
 '1.22': 'digital competency', '1.23': 'employability in curriculum design', '1.24': 'speakers from the profession', '1.25': 'assignments that build business skills',
 '1.26': 'initiatives with external partners', '1.27': 'supervised placement as the base of professional skills', '1.28': 'career pathways and confidence',
 '2.1': 'integrated curriculum and supervised placement', '2.2': 'what personal development enables', '2.3': 'equitable access, ten ways',
 '2.4': 'reasonable adjustments; fitness to practise', '2.5': 'progression: five considerations', '2.6': 'honours progression year to year',
 '2.7': 'joint honours', '2.8': "master's degrees and exit awards", '2.9': 'flexible modes of delivery', '2.10': 'placement partnership agreements',
 '2.11': 'alignment with a professional body', '2.12': 'partnership with students', '2.13': 'monitoring and review by awarding bodies',
 '2.14': 'externality in review', '2.15': 'external examining', '2.16': 'what monitoring and review should cover',
 '3.1': 'where training is offered; related qualifications', '3.2': 'aim of training', '3.3': 'eleven areas of knowledge',
 '3.4': 'the five pillars', '3.5': 'common and modality-specific knowledge', '3.6': 'range of approaches; modality-neutral wording',
 '3.7': 'ten elements of skills practice', '3.8': 'what trainees must show in personal development', '3.9': 'eleven elements of professional development',
 '3.10': 'five elements of research', '3.11': 'integrated curriculum; placement required', '3.12': 'core methods of training',
 '3.13': 'experiential learning activities', '3.14': 'independent learners and practitioners', '3.15': 'in-person and remote training; digital core',
 '3.16': 'inclusive teaching by diverse trainers', '3.17': 'depth in a modality; integrative coherence', '3.18': 'teaching models; respect for other approaches',
 '3.19': 'research skills and a small study', '3.20': 'personal development provision', '3.21': 'placements and supervision',
 '3.22': 'staffing and ratios for experiential work', '3.23': 'assessment of theory and competence', '3.24': 'typical assessment methods',
 '3.25': 'inclusive, authentic assessment criteria', '3.26': 'quality assurance of assessment', '3.27': 'readiness before client work',
 '3.28': 'placements in assessment and outcomes', '4.1': 'standards are the minimum threshold', '4.2': 'most do better; Annex D',
 '4.3': 'a complex, changing landscape', '4.4': 'threshold at level 6 or 10; competent in all aspects', '4.5': 'standards framed as know, be and do',
 '4.6': 'threshold: professional context', '4.7': 'threshold: understanding people', '4.8': 'threshold: the therapist', '4.9': 'threshold: ethical and legal',
 '4.10': 'threshold: boundaries and contracting', '4.11': 'threshold: client assessment', '4.12': 'threshold: the therapeutic relationship',
 '4.13': 'threshold: nineteen generic skills', '4.14': 'typical level left to marking schemes', '4.15': 'excellent level left to marking schemes',
 '4.16': "master's: further critical and conceptual understanding", '4.17': "master's: eleven further threshold statements"}
CTYPE = {'3.3': 'area', '3.4': 'area', '3.5': 'area', '3.6': 'area', '3.7': 'area', '3.9': 'area', '3.10': 'area',
         '1.3': 'stem', '1.13': 'stem', '1.17': 'stem',
         '3.12': 'practice', '3.13': 'practice', '3.15': 'practice', '3.19': 'practice', '3.20': 'practice', '3.21': 'practice', '3.22': 'practice',
         '3.23': 'practice', '3.24': 'practice', '3.25': 'practice', '3.27': 'practice',
         '4.6': 'stem', '4.7': 'stem', '4.8': 'stem', '4.9': 'stem', '4.10': 'stem', '4.11': 'stem', '4.12': 'stem'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points', kind='other: front matter, read for S1, S2 and S8'),
    dict(number='none', heading='section heading lines 1 to 4', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for SB5 and SB6 (the PSA accredited registers)'),
    dict(number='6', heading='Membership of the Advisory Groups', kind='other: back matter, read for S8 (the 2013 first edition)')]

TH = {}
TH['1.10'] = 'theme:edi'
for _i in ('1.12', '1.13', '1.14'): TH[_i] = 'theme:esd'
for _i in ('1.16', '1.22', '1.23', '1.24'): TH[_i] = 'theme:enterprise'
for _k in range(1, 11): TH[f'2.3.b{_k}'] = 'theme:accessibility'
TH['2.4'] = 'theme:accessibility'

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.6; 4.2 (title of Annex D); 4.4'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.6; 4.2 (title of Annex D); 4.4'),
            dict(id='fheq:7', role='cites', locator="D1, 2.8 (master's degrees)"),
            dict(id='fqheis:11', role='cites', locator="D1, 2.8 (master's degrees)"),
            dict(id='spine:6', role='refers', locator='std:ref:uk-framework R2 and R8 (inferred: Part E)'),
            dict(id='spine:7', role='refers', locator='std:ref:uk-framework R2 and R8 (inferred: Part E)')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.6: "FHEQ Level 6; FQHEIS Level 10"; 4.4; 4.2, the title of Annex D)'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.8: "FHEQ Level 7; FQHEIS Level 11")'),
                dict(**{'from': 'fheq:6'}, to='spine:6', relation='equivalent', basis='inferred from std:ref:uk-framework R2 (Part E)'),
                dict(**{'from': 'fheq:7'}, to='spine:7', relation='equivalent', basis='inferred from std:ref:uk-framework R2 (Part E)')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.6', '1.9', '1.10', '1.11', '2.3', '3.3', '3.9', '3.10', '3.16', '4.3', '4.6', '4.7', '4.12', '4.13', '4.17']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.10', '1.11', '1.22', '2.3', '2.4', '3.18', '4.9']),
      dict(id='theme:esd', role='carries', carriedIn=['1.6', '1.7', '1.12', '1.13', '1.14', '2.9', '2.16', '3.3', '4.3', '4.13']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28', '2.2', '2.12', '3.3', '4.3', '4.7'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-counselling-and-psychotherapy-2013-benchmarks (not yet ingested)', note='the first edition (2013), named in section 6; the front matter lists the key changes'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees, for performance above the threshold (4.2); SL6'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 6 and 7 (2.6, 2.8, 4.4)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 10 and 11 (2.6, 2.8, 4.4)'),
      dict(rel='refersTo', target='std:doc:welsh-government-cqfw-2009-framework', note='named in 3.1 for earlier vocational awards in Wales; no level cited'),
      dict(rel='thresholdAt', target='std:ref:uk-framework, spine:6 and spine:7', note='inferred: the honours threshold at spine:6, the master\'s threshold at spine:7 (Part E)'),
      dict(rel='readWith', target='std:doc:qaa-psychology-2023-benchmarks; std:doc:qaa-health-studies-2024-benchmarks; std:doc:qaa-social-work-2026-benchmarks; std:doc:qaa-education-studies-2025-benchmarks', note='1.8: providers may refer to the statements for allied professions (medicine, health sciences, nursing, social work, education, psychology); editions as held, which may differ from those of 2022 (Part E)'),
      dict(rel='refersTo', target='UNESCO (2017) key competencies for sustainability (not yet ingested: Part E)', note='1.6, 1.7, 1.13'),
      dict(rel='refersTo', target='PSA accredited registers and the professional bodies holding them (not yet ingested: Part E)', note='1.8; section 5')]
S8 = {'published': '2022-03', 'lastReviewed': 'none-stated', 'reviewCycle': 'none-stated', 'consultation': 'none-stated (advisory group of 2022 listed in section 6)',
      'previousEditions': '2013 (first edition, advisory group in section 6)', 'replacedBy': 'none'}

SB1 = ['counsellors and psychotherapists work to ease psychological distress and help clients build self-awareness, insight, skill and confidence to live more effectively (D1, 1.1)',
       'training forms knowledgeable, self-reflective and reflexive practitioners committed to lifelong development and professional standards, working safely, ethically and effectively while keeping well themselves (D1, 1.2, 2.1)',
       'practice happens in many settings, from private practice and agencies to schools, prisons, faith communities, businesses, charities and the NHS, with individuals, couples, families, groups and communities, in person or remotely (D1, 1.3 to 1.5)',
       'reflective self-awareness (of one\'s biases and preferences) and reflexive self-awareness (of how one\'s history and culture shape interaction) are both central and are distinguished (D1, 1.7)',
       'the statement favours no modality; courses vary by modality (such as gestalt, person-centred, CBT, psychodynamic, integrative) and mode, but all join literature, research, client skills and personal and professional growth (D1, front matter; 1.8; 3.6)',
       'there is no single PSRB; courses align with differing professional standards that may lead to accreditation and registration (D1, 1.8)',
       'the curriculum rests on five pillars, theory, professional skills practice, personal development, professional development and research, and every professional course includes an assessed, supervised placement (D1, 2.1, 3.4, 3.11)',
       'experiential work needs close containment, small groups and suitable staff to student ratios (D1, 3.22)',
       'the threshold standards are framed as what a graduate needs to know, be and do to practise safely, ethically and effectively (D1, 4.4, 4.5)']
SB2 = [dict(theme='theme:edi', inThisSubject='inclusive training as an ethical duty to safeguard students and clients; diverse trainers for diverse clients; content that questions majority-culture theory; anti-discriminatory practice, awareness of bias and of power and privilege in the relationship (D1, 1.6, 1.9 to 1.11, 3.16, 4.6, 4.7, 4.12)',
            statements=['1.10', '2.3.b6', '3.16', '4.6.b8', '4.6.b12', '4.7.b7', '4.7.b9', '4.12.b3', '4.12.b4', '4.12.b8', '4.12.b11', '4.13.b17', '4.17.b5', '4.17.b7']),
       dict(theme='theme:accessibility', inThisSubject='headed Accessibility in section 2: access in person and online, safe and private practice spaces, accessible formats, placement screening, digital poverty and practical help such as bursaries and laptops; reasonable adjustments with fitness to practise; digital accessibility in remote work (D1, 2.3, 2.4, 4.9)',
            statements=['2.3.b1', '2.3.b2', '2.3.b3', '2.3.b4', '2.3.b5', '2.3.b6', '2.3.b7', '2.3.b8', '2.3.b9', '2.3.b10', '2.4', '4.9.b19']),
       dict(theme='theme:esd', inThisSubject='headed Sustainability: sustainable development knowledge of the profession and its future, the eight UNESCO competencies held essential for practitioners, learning environments that foster responsibility for well-being; ESD embedded across the curriculum and monitored (D1, 1.6, 1.7, 1.12 to 1.14, 2.16, 4.13)',
            statements=['1.7', '1.12', '1.13', '1.14', '2.16.b3', '4.13.b18', '4.13.b19']),
       dict(theme='theme:enterprise', inThisSubject='headed Employability, enterprise and entrepreneurship education: growth in paid, voluntary and private practice; knowing the value of one\'s skills; an entrepreneurial mindset; placements as a bridge to service provision; enterprising capability in the threshold standards (D1, 1.15 to 1.28, 2.2, 4.7)',
            statements=['1.16', '1.22', '1.23', '1.24', '2.2.b15', '4.6.b13', '4.7.b10'])]
SB3 = dict(
    areas=[dict(component='3.3', gloss='eleven areas of knowledge, from philosophy of human nature to mental health systems, framed by epistemic justice'),
           dict(component='3.4', gloss='the five pillars of the curriculum'),
           dict(component='3.5', gloss='theory: knowledge common to all orientations and knowledge proper to each'),
           dict(component='3.6', gloss='theory: a range of approaches and their evidence; modality-neutral wording'),
           dict(component='3.7', gloss='professional skills practice: ten elements from relationship building to digital delivery'),
           dict(component='3.9', gloss='professional development: eleven elements from ethics to supervision'),
           dict(component='3.10', gloss='research: five elements from appraisal to formal projects')],
    practices=[dict(component='3.12', kind='teaching', gloss='core methods: seminars, skills practice, research workshops, development activities, supervised placement'),
               dict(component='3.13', kind='learning', gloss='experiential activities: modelling, group practice, projects, peer learning, case forums, presentations'),
               dict(component='3.15', kind='teaching', gloss='in-person and remote training matched to the mode of practice; core digital training'),
               dict(component='3.19', kind='learning', gloss='research skills and at least one small-scale study'),
               dict(component='3.20', kind='learning', gloss='personal development through groups, journals, residentials or personal therapy'),
               dict(component='3.21', kind='learning', gloss='placements with regular supervision, vetted by the course'),
               dict(component='3.22', kind='teaching', gloss='qualified staff and small experiential groups, ratios normally not above one to sixteen'),
               dict(component='3.23', kind='assessment', gloss='theory and competence assessed; competence a condition of the award'),
               dict(component='3.24', kind='assessment', gloss='typical methods, from essays and portfolios to annotated transcripts and client formulations'),
               dict(component='3.25', kind='assessment', gloss='formative and summative, inclusive and authentic; criteria include professional skills'),
               dict(component='3.27', kind='assessment', gloss='readiness assessed before client work')])

_cnt = lambda rung, award: sum(1 for x in P.values() if x['rung'] == rung and x['award'] == award)
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.6 to 4.13 under the heading Threshold level (3rd class); 4.4 sets them as minimum expectations', award=HON, items=_cnt('threshold', HON)),
           dict(rung='typical', leadIn='4.14 (heading Typical level (2:2 or 2:1); no items)', award=HON, items=_cnt('typical', HON)),
           dict(rung='excellent', leadIn='4.15 (heading Excellent level (1st class); no items)', award=HON, items=_cnt('excellent', HON)),
           dict(rung='threshold', leadIn="4.16 and 4.17 under the heading Benchmark standard for master's degrees", award=MA, items=_cnt('threshold', MA))],
    rungBases="4.1 and 4.4: the standards are the minimum threshold for honours at FHEQ level 6 or FQHEIS level 10; 4.2: most students do significantly better, judged by each institution with reference to Annex D; 4.14 and 4.15: typical (2:2 or 2:1) and excellent (1st) criteria follow each institution's generic marking schemes; 4.17: the master's statements describe its threshold",
    outcomeLists=[dict(leadIn='2.2', gloss='what personal development should enable the learner to do', items=15, award=[HON, MA]),
                  dict(leadIn='3.8', gloss='what trainings must ensure trainees can demonstrate in personal development', items=10, award=[HON, MA])],
    outcomes=[])
SB4A_FULL = []

_REG = ['Association of Child Psychotherapists', 'Association of Christian Counsellors', 'British Association for Counselling & Psychotherapy',
        'British Psychoanalytic Council', 'COSCA (Counselling & Psychotherapy in Scotland)', 'Human Givens Institute', 'National Counselling Society',
        'National Hypnotherapy Society', 'UK Association for Humanistic Psychology Practitioners', 'UK Council for Psychotherapy']
SB5 = [dict(body='professional, statutory and regulatory bodies (PSRBs), none named as the single body', says='there is no single PSRB for counselling and psychotherapy; courses may align with differing standards that can lead to accreditation and registration (D1, 1.8)', requirements='not yet ingested (Part E)'),
       dict(body='the relevant professional body (by modality), unnamed', says='courses should be written in line with a suitable professional body\'s requirements; monitoring aligns with them; training follows them; graduates practise in line with professional body guidance (D1, 2.11, 2.16, 3.18, 3.21, 4.12)', requirements='not yet ingested (Part E)'),
       dict(body='Professional Standards Authority (PSA)', says='approves the accredited registers whose holders are listed in section 5 (D1, section 5)', requirements='not yet ingested (Part E)'),
       dict(body='National Institute for Health and Clinical Excellence (NICE)', says='its guidelines are an example of government policy and recommendations whose effects graduates should know (D1, 4.6)', requirements='not yet ingested (Part E)')] + \
      [dict(body=b, says='holds a register accredited by the PSA, listed in the references (D1, section 5)', requirements='not yet ingested (Part E)') for b in _REG]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.6', '1.9', '1.10', '1.11', '2.3', '3.3', '3.9', '3.10', '3.16', '4.3', '4.6', '4.7', '4.12', '4.13', '4.17'],
                 statements=SB2[0]['statements']),
            dict(id='theme:accessibility', named='Accessibility', carriedIn=['1.10', '1.11', '1.22', '2.3', '2.4', '3.18', '4.9'], statements=SB2[1]['statements']),
            dict(id='theme:esd', named='Sustainability (front matter and 2.16: education for sustainable development)', carriedIn=['1.6', '1.7', '1.12', '1.13', '1.14', '2.9', '2.16', '3.3', '4.3', '4.13'],
                 statements=SB2[2]['statements']),
            dict(id='theme:enterprise', named='Employability, enterprise and entrepreneurship education (EEEE)', carriedIn=['1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.27', '1.28', '2.2', '2.12', '3.3', '4.3', '4.7'],
                 statements=SB2[3]['statements'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.6', '2.8', '4.2', '4.4']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.6', '2.8', '3.1', '4.2', '4.4']),
                dict(framework='cqfw', levels=[], citedIn=['3.1']),
                dict(framework='other: Regulated Qualifications Framework (RQF), England and Northern Ireland', levels=[], citedIn=['3.1'])],
    bodies=[dict(body='PSRBs (no single body)', citedIn=['1.8']),
            dict(body='the relevant professional body, unnamed', citedIn=['2.11', '2.16', '3.18', '3.21', '4.12']),
            dict(body='National Institute for Health and Clinical Excellence (NICE)', citedIn=['4.6']),
            dict(body='Professional Standards Authority (PSA)', citedIn=['section 5 (back matter)'])] +
           [dict(body=b, citedIn=['section 5 (back matter)']) for b in _REG],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='how institutions judge achievement above the threshold, by the four honours classes'),
                     dict(document='not yet ingested: listed in Part E', named='Subject Benchmark Statements for these various professions (medicine, health sciences, nursing, social work, education, psychology)', citedIn=['1.8'], role='reading for collaboration with allied professions'),
                     dict(document='not yet ingested: listed in Part E', named='UNESCO, 2017 (the key competencies for sustainability)', citedIn=['1.6', '1.7', '1.13'], role='the eight competencies held essential for practitioners'),
                     dict(document='not yet ingested: listed in Part E', named='Teaching Excellence Framework (TEF), National Student Survey (NSS), PTES and PRES', citedIn=['2.16'], role='external exercises whose feedback monitoring should draw on')])

B1 = [dict(slug='reflective-self-awareness', definition="awareness of one's own biases and preferences (D1, 1.7)", beneficiaryDefinition='noticing your own biases and preferences', scopeNote='paired with reflexive self-awareness; the two overlap and complement each other', category='unknown', practices=['counselling', 'psychotherapy']),
      dict(slug='reflexive-self-awareness', definition="awareness of how one's own history and culture shape the way one relates to others (D1, 1.7)", beneficiaryDefinition='seeing how your own past and culture affect how you relate to people', scopeNote='paired with reflective self-awareness', category='unknown', practices=['counselling', 'psychotherapy']),
      dict(slug='suicidal-ideation', definition='thoughts of suicide, set apart from intent in judging risk (D1, 4.11)', beneficiaryDefinition='having thoughts of suicide', scopeNote='contrasted with suicidal intent', category='unknown', practices=['counselling', 'psychotherapy']),
      dict(slug='suicidal-intent', definition='an intention to act on thoughts of suicide (D1, 4.11)', beneficiaryDefinition='intending to act on thoughts of suicide', scopeNote='contrasted with suicidal ideation', category='unknown', practices=['counselling', 'psychotherapy']),
      dict(slug='eeee', definition='employability, enterprise and entrepreneurship education, which builds the behaviours, attributes and competencies for a career, employed or self-employed (D1, 1.18 to 1.21)', beneficiaryDefinition='learning that prepares you for work and for running your own practice', scopeNote='the statement abbreviates it EEEE', category='unknown', practices=['education']),
      dict(slug='experts-by-experience', definition='people who use services, whose feedback informs course review (D1, 2.16)', beneficiaryDefinition='people with lived experience of using services', scopeNote='', category='unknown', practices=['counselling', 'psychotherapy'])]
B2A = [dict(concept='reflective-self-awareness', form='Reflective self-awareness', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='reflexive-self-awareness', form='reflexive self-awareness', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='suicidal-ideation', form='suicidal ideation', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='suicidal-intent', form='suicidal intent', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='eeee', form='EEEE', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='experts-by-experience', form='Experts by Experience', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []; B5 = []

D3 = [dict(source='the professional bodies\' accreditation standards (such as BACP and UKCP) and the PSA accredited registers standards', why='the bodies named in 1.8 and section 5 (SB5)', status='wanted'),
      dict(source='UNESCO (2017), the key competencies for sustainability', why='cited in 1.6, 1.7 and 1.13 (SB6)', status='wanted'),
      dict(source='Subject Benchmark Statement: Counselling and Psychotherapy (2013, first edition)', why='superseded edition (S7)', status='wanted')]

E = [
    "Rungs: the honours standards are threshold only. Section 4 lists threshold items under seven practice headings (4.6 to 4.12) and generic skills (4.13); 'Typical level (2:2 or 2:1)' (4.14) and 'Excellent level (1st class)' (4.15) are headings with no items, deferring to each institution's generic marking schemes, and 4.2 points to Annex D. SB4 records typical and excellent with items 0, `outcomes` is empty and no gradeOf link is drawn. Differs from Psychology (three listed rungs).",
    "New rung shape: each threshold paragraph 4.6 to 4.12 opens 'The graduate will have the relevant professional knowledge, abilities and skills to:' and then runs unbulleted sentences under the in-line markers Know, Be and Do. Each sentence is cut as its own record (<n>.b<k> in text order, our numbering within the issuer's paragraph); where a sentence introduces bullets (4.9, 4.10, 4.11), the lead sentence and each bullet are separate records, except 4.10.b1, whose bullets are single nouns (clients, supervisors, tutors, colleagues, employers) and stay in its span. The Know, Be or Do marker is recorded in the agent instructions' locator, not in the span.",
    "Domain for Know, Be, Do: Know sentences are knowledge, or understanding where the verb is understand or evaluate; Be sentences (professional attributes such as 'Reflective of', 'Open to', 'Committed to') and Do sentences are recorded as subject-skill. P3 to confirm Be as subject-skill rather than a domain of its own.",
    "Force of threshold items: recorded as threshold (brief convention: the issuer defines the rung as the minimum, 4.1 and 4.4), with forceFrom 4.4; the lead-in's own modal is will ('will have'). 4.13's lead-in is 'should be able to' but sits under the threshold heading, so it too is recorded as threshold; P3 to confirm should against threshold for 4.13.",
    "Master's: 4.16 (stem 'requires additional critical and conceptual understanding that enables students to', four items) and 4.17 ('The following additional statements describe the threshold level of competence', eleven items, 'will be capable of') are recorded as rung threshold, award master's, level fheq:7, force threshold with forceFrom 4.17. Skeleton correction: 4.16.b4 held both the fourth bullet (marked '-' not a bullet sign) and the closing sentence; recut so that 4.16.b4 is the bullet and 4.16.b5 is the closing sentence ('award holders must demonstrate'), force must; 4.16.b5 is not a bullet in the issuer's text.",
    "Skeleton corrections: 2.2.b15, 2.9.b3, 3.8.b10 and 4.13.b19 carried the next sub-heading (Accessibility, Partnership, Professional development, Typical level); recut with `find`. The skeleton's 4.9, 4.10 and 4.11 bullet cuts (b5 of 4.9 ran over 1,600 characters across many sentences) are replaced by the sentence cut above. Paragraph spans for paragraph records are tidied of trailing sub-headings and page numbers.",
    "Skeleton false hits: 3.24 was flagged as a typical rung lead-in ('Typically, courses of study ...'); its list is assessment methods ('can include') and is an S3 practice, not statements. 4.16 and 4.17 were flagged threshold correctly. The skeleton's typical count (12) is therefore wrong; the true honours rung counts are threshold only.",
    "Outcome lists outside section 4: 2.2 (personal development 'should underpin ... to enable the learner to', 15 items, force should) and 3.8 ('Trainings must ensure that trainees are able to demonstrate', 10 items, force must), recorded as type outcome, rung none. New lead-in wordings against Psychology.",
    "Lists not cut as statements, with reasons: 1.3 (settings, 'may occur'), 1.13 bullets (names of the eight UNESCO competencies; the paragraph is one record), 1.17 (what an entrepreneurial mindset 'means becoming', a definition), 3.3 (areas of knowledge, plain present 'ensures that graduates have'), 3.7, 3.9 and 3.10 ('incorporates the following', content), 3.12 and 3.13 (training methods), 3.24 (assessment methods, 'can include'). 3.3, 3.9 and 3.10 read close to outcomes; P3 to confirm they are content, not standards.",
    "Obliging words outside the five, recorded as describes for Abbott: 1.10 ('Assessments need to be authentic'), 1.13 ('requires practical operation of all the competencies'; read as must, but the builder's force pattern knows only 'require' and 'required'), 1.24 ('is recommended'), 2.6 ('it is expected', 'would be expected'). Also noted, inside records with another force: 3.18 ('it is essential that students develop'), 3.19 ('graduates require sufficient awareness'), 3.21 ('should be required').",
    "Plain-present provider norms not cut (benchmark template open point 5, for P3): 1.2 ('Courses ... prepare students'), 1.9, 1.11 (strive, encouraged), 2.4 second sentence ('courses include ethical responsibilities for monitoring student fitness to practice', kept inside the 2.4 record), 2.12, 2.13 to 2.15 (institutional practice with will), 3.5, 3.6 ('A typical course of study will offer'), 3.14, 3.28. 1.25 ('will help students develop') and 1.26 to 1.28 describe benefits, not standards.",
    "Mixed modals within one record: 1.7 (will and should) recorded at will; 1.14 (aim and must) at must; 2.3.b6 holds must inside a should list, recorded at must; 3.11 (will and must) at must; 3.22 (should and must) at must; 3.27 (should and must) at must; 2.9 items take 'may' from the lead-in 'may be', though the stem opens with 'should consider'.",
    "Broken words in the held text (extraction spacing: 'perf orm', 'bri ng', 'identi fy', 'undert ake', 're flect', 'wri ting', 'arg ument', 'materi al', 'categori sing', 'collati ng', 'contempora ry', 'relati ng', 'saf e', 'staf f', 'successf ul', 'self -awareness') mean some verbs cannot be listed as they appear: 4.13.b2, b3, b7 list none; 4.13.b1 lists 'assigned' and 'participating'. Spans keep the text as held.",
    "The 2.2 list repeats 1.17's mindset items (self-organised, tolerant of uncertainty, sensitive to personal values) and 4.7.b10 repeats 1.16's wording on enterprising capabilities; each is kept where the issuer places it. 3.9 and 4.8 share wording on strengths, limitations and self-care, and 3.8.b6 and 4.8.b7 on personal support; kept as issued.",
    "The statement names sexual dynamics, suicide risk and self-harm as professional knowledge (4.10.b6, 4.11.b7 to b9); the versions keep these at the level of practice competence.",
    "Inferred: the crosswalks fheq:6 to spine:6 and fheq:7 to spine:7 are read from std:ref:uk-framework R2. The S7 readWith targets are the editions held now (Psychology 2023, Health Studies 2024, Social Work 2026, Education Studies 2025), not those current in 2022; medicine and nursing have no matching statement held.",
    "Subjects: HECoS 100495 (counselling), 100254 (psychotherapy) and CAH02-06-07 are recorded as stated because the title names both subjects; the statement names no code. Joint honours (2.7) carries no partner code.",
    "SB5 and SB6: the ten bodies holding PSA accredited registers and the PSA itself are named only in section 5 (back matter, otherwise excluded); recorded so the bodies can be read across, with citedIn 'section 5 (back matter)'. BACP and UKCP also appear in the 2022 advisory group. No body's requirements are ingested (D3).",
    "SB6: the front matter also names the OfS regulatory framework, the Quality Assessment Framework for Wales, the Quality Enhancement Framework (Scotland), the Quality Code's Advice and Guidance and QAA's Glossary; these are excluded matter and not level frameworks, so they are not in SB6. 2.16.b9 names the TEF, NSS, PTES and PRES, recorded as a shared document entry not yet ingested. CQFW and the RQF are named in 3.1 for earlier vocational awards, with no level.",
    "Levels: the threshold standards (4.4) apply to 'practice-facing courses' and 'students on professional courses'; it is not stated how a non-practice honours route (if any) relates to them. 2.8 mentions exit awards (Postgraduate Certificate or Diploma) with no standards.",
    "Section order: section 1 holds the cross-cutting themes (EDI, Sustainability, EEEE); section 2 holds Personal development, Accessibility, Progression, Flexibility, Partnership, Monitoring and review; section 3 Content is subdivided by the five pillars; filled by function.",
    "Supersedes: the 2013 first edition is named only in the advisory group list (section 6); the back matter says 'Second edition, Published 30 March 2022'.",
    "Licence: QAA copyright notice only; re-use terms not stated in the text.",
]
