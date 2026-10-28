// Build the student-facing benchmark sibling store from all-capabilities.json + the SF rewrites.
// Asserts every capability gets exactly one studentFacing rewrite (no misses, no stray ids).
const fs = require('fs');
const base = JSON.parse(fs.readFileSync(__dirname + '/all-capabilities.json', 'utf8'));

const SF = {
 "academic-writing": {
  "academic-writing/05": "You can read an assessment question before you write, working out its steer and its keywords.",
  "academic-writing/c1": "You can follow the writing cycle to plan and finish a first draft.",
  "academic-writing/06": "You can find and fix errors in your own writing by proofreading and editing it.",
  "academic-writing/02": "You can recognise and structure an essay and other argued pieces of writing.",
  "academic-writing/04": "You can write clear sentences, mostly in the active voice.",
  "academic-writing/03": "You can use the four pillars of good writing to shape and review your own work.",
  "academic-writing/01": "You can recognise how writing conventions change from one subject to another.",
  "academic-writing/c2": "You can bring sources into your writing actively, leading with your own point and using sources to back it.",
  "e3": "You write with an awareness of your subject's conventions and how they shape your voice."
 },
 "ai-technology": {
  "i1": "You can explain what generative AI is, and what it is not.",
  "i2": "You check your assessment guidance before using AI on a task.",
  "i3": "You recognise what AI can't be trusted to do, and think it through yourself first.",
  "ai-technology/03": "You can use AI as a critical friend within a careful workflow, not as a replacement for your own thinking.",
  "d2": "You fact-check what AI produces and are open about where you have used it.",
  "ai-technology/01": "You can decide, with clear reasons, when to use AI and when not to.",
  "ai-technology/02": "You avoid the misconduct risks of generative AI, and never cite it as a source.",
  "ai-technology/06": "You can tell permitted support from an unfair advantage when using technology.",
  "ai-technology/05": "You weigh up the costs and benefits of using AI as a responsible professional, including its wider impact."
 },
 "creativity": {
  "creativity/01": "You can see creativity as a skill you can develop, closely tied to critical thinking.",
  "creativity/02": "You can use open, idea-generating thinking and focused, decision-making thinking at the right stage of a task.",
  "creativity/03": "You can work past creative blocks such as fear of failure and perfectionism.",
  "creativity/07": "You can draw on creativity theory to explain and justify a creative approach.",
  "creativity/04": "You can use structured methods to solve problems creatively.",
  "creativity/05": "You can change your approach when a strategy is not working.",
  "creativity/06": "You can apply creative and enterprising thinking in professional settings.",
  "e2": "You can turn ideas into action even when things are uncertain.",
  "e3": "You own a creative practice, aware of how your own creative process works."
 },
 "criticality": {
  "criticality/02": "You can map the main ideas, authors and debates around a topic, and begin to question them.",
  "criticality/c1": "You think critically about the choices you make when searching, reading and planning your work.",
  "i3": "You treat being critical as a habit you bring to all your study, not something you switch on only for assignments.",
  "criticality/01": "You can tell analysis and evaluation apart, and spot when a task is asking for each.",
  "criticality/03": "You can take a scholarly interpretation apart and weigh up how convincing it is.",
  "criticality/04": "You read a journal article strategically, using its structure and methods to decide what to take from it.",
  "criticality/c2": "You can form a judgement about what matters most and justify it with clear reasons.",
  "criticality/05": "You write critically, pulling sources together and using the vocabulary of your subject.",
  "e3": "You write with authority, aware of how your own position shapes the argument you make."
 },
 "finding-using-sources": {
  "i1": "You can explain how searching for academic sources differs from everyday searching.",
  "finding-using-sources/02": "You can use the library discovery service to find scholarly sources.",
  "finding-using-sources/c1": "You can follow a staged search, starting from your reading list and what you already know.",
  "d1": "You can pull the keywords and their synonyms out of a task.",
  "finding-using-sources/01": "You can plan a search using keywords and Boolean operators (AND, OR, NOT).",
  "d3": "You can refine a search over several rounds, reflecting on the results each time.",
  "finding-using-sources/04": "You can widen a search using citation trails, databases and tools like Google Scholar.",
  "finding-using-sources/03": "You can judge a source on how current, authoritative and relevant it is to your work.",
  "e3": "You can search thoroughly and judge when you have covered the discussion on a topic."
 },
 "presenting": {
  "i1": "You can explain what a presentation is testing, and read its brief.",
  "presenting/c1": "You can build a presentation to a brief, with a hook, a main body and a conclusion.",
  "i3": "You can practise your presentation to time and fix what is not working.",
  "presenting/01": "You can design clear, accessible visual aids, keeping to 'less is more'.",
  "presenting/03": "You can adapt how you present to different formats.",
  "presenting/02": "You can open a presentation in a way that engages people, and manage your own nerves.",
  "presenting/c3": "You can present in professional formats such as a pitch, a conference poster or a viva-style interview.",
  "presenting/04": "You can work in a group, taking a lead and resolving conflict when it arises.",
  "presenting/c2": "You can present and defend an argument in an academic voice, even under questioning."
 },
 "referencing": {
  "referencing/c1": "You can explain why academic work acknowledges where its ideas come from.",
  "referencing/01": "You can write accurate in-text references and a references list in a single, consistent style.",
  "referencing/c2": "You record and organise sources as you find them, so every citation can be traced back.",
  "referencing/02": "You can acknowledge quotation and paraphrase correctly, so you avoid plagiarism.",
  "d2": "You can reference trickier source types accurately.",
  "referencing/c3": "You can use citation to show how widely you have read and how you have engaged with the discussion.",
  "referencing/03": "You uphold honesty and trust in your academic work.",
  "referencing/04": "You act with fairness, respect, responsibility and courage in how you conduct your academic work.",
  "e3": "You carry academic integrity into your identity as a graduate and professional."
 },
 "reflective-practice": {
  "reflective-practice/01": "You can work through a simple cycle: describe what happened, reflect on it, then take action.",
  "reflective-practice/02": "You can balance the positives and the negatives when you reflect on how something went.",
  "i3": "You can notice what went well and what did not in your own work.",
  "reflective-practice/c1": "You can reflect critically on your work, rather than just describing it.",
  "reflective-practice/c2": "You can turn a reflection into a dated action plan.",
  "reflective-practice/04": "You can reflect on your motivation and change learning strategies that are not working.",
  "reflective-practice/c3": "You can choose a fuller reflective model (such as Gibbs, Kolb or Johns) and apply it.",
  "reflective-practice/03": "You can use reflective writing to support your ongoing professional development and lifelong learning.",
  "reflective-practice/c4": "You can examine how your own identity, values and assumptions shape what you notice and judge."
 },
 "researching-research-methods": {
  "i1": "You can explain how a research project differs from an essay.",
  "researching-research-methods/01": "You can set out a research question, its rationale and its aims.",
  "i3": "You can narrow a broad topic down to a question you can actually research.",
  "researching-research-methods/02": "You can structure and write a literature review and a research report.",
  "researching-research-methods/c1": "You can write a research proposal that answers each of its questions.",
  "d3": "You can review the literature critically, placing your own research within it.",
  "researching-research-methods/03": "You can apply research ethics, including informed consent and anonymisation.",
  "researching-research-methods/c2": "You can choose a methodology and methods for a question, and justify them.",
  "researching-research-methods/04": "You can plan and scope a dissertation-length research project."
 },
 "revising-exams": {
  "i1": "You can explain the different forms of exam and what each one asks of you.",
  "i2": "You can make a simple revision plan from the time you have.",
  "revising-exams/01": "You can manage exam nerves and prepare in an organised way.",
  "revising-exams/02": "You can turn passive revision into active techniques.",
  "d2": "You can aim your revision at the gaps in your own knowledge.",
  "d3": "You can keep an eye on your revision and change it when it is not working.",
  "revising-exams/03": "You can use hands-on and role-play techniques to engage more deeply with what you are revising.",
  "revising-exams/04": "You can apply an exam strategy across different question formats and on the day.",
  "e3": "You choose revision techniques by what actually works for you, judged by how well you recall."
 },
 "starting-progressing-succeeding": {
  "i1": "You can explain what it means to excel at university.",
  "starting-progressing-succeeding/c1": "You can recognise and follow the conventions of academic practice.",
  "starting-progressing-succeeding/01": "You can take a growth mindset towards academic challenges.",
  "starting-progressing-succeeding/03": "You can set goals focused on mastery and keep working at them.",
  "starting-progressing-succeeding/02": "You can build your confidence and manage stress and anxiety under pressure.",
  "starting-progressing-succeeding/c2": "You can develop an academic voice and the confidence to own how you work.",
  "starting-progressing-succeeding/04": "You can put into words the strengths you are building for the move from student to graduate.",
  "starting-progressing-succeeding/c3": "You can direct your own learning and development as a lifelong learner.",
  "e3": "You draw your learning together into a confident graduate identity."
 },
 "understanding-learning-assessment-feedback": {
  "understanding-learning-assessment-feedback/01": "You can understand how learning works within a subject's community of scholars.",
  "understanding-learning-assessment-feedback/04": "You can tell formative from summative assessment and engage with their different forms.",
  "understanding-learning-assessment-feedback/02": "You can tell active learning, where you build understanding, from passively receiving information.",
  "understanding-learning-assessment-feedback/03": "You can read learning outcomes and see how activities line up with them.",
  "understanding-learning-assessment-feedback/06": "You can turn feedback into an action plan by reflecting on it.",
  "understanding-learning-assessment-feedback/05": "You can apply cycles of self-regulated learning to your independent study.",
  "understanding-learning-assessment-feedback/c3": "You can adapt to the demands of different types of assessment.",
  "understanding-learning-assessment-feedback/c1": "You can assess your own and others' work against marking criteria.",
  "understanding-learning-assessment-feedback/c2": "You can use feedback, in dialogue with tutors, to keep developing across your degree."
 },
 "work-based-experiential-learning": {
  "work-based-experiential-learning/01": "You can tell apart the different types of practice- and work-based learning.",
  "i2": "You can explain what learning in a real practice setting offers.",
  "i3": "You can set your own learning goals for a placement or practice experience.",
  "work-based-experiential-learning/c1": "You can conduct yourself as a professional in a practice setting.",
  "work-based-experiential-learning/02": "You can make good use of a mentor while on placement.",
  "work-based-experiential-learning/c2": "You can test what you have learned in practice and reflect on how it went.",
  "work-based-experiential-learning/03": "You can apply an experiential learning cycle (such as Kolb's) to work-based learning.",
  "work-based-experiential-learning/04": "You can use professional judgement in a work setting and justify your decisions.",
  "e3": "You reflect on your developing identity as a practitioner."
 }
};

const out = {
 "storeId": "pathway-student-facing-benchmarks",
 "note": "Student, practical-facing ('You...') rewrites of each pathway's capability statements, in the universal-reference forBeneficiary register; subject-neutral. Keyed pathway -> capabilityId so they survive rebuilds of catalogue/context/pathway/*.json. First move of the 9->18 benchmark proliferation (rewrite the identified 9; proliferate to 18 later). AGENT-SUGGESTED, pending human review.",
 "register": "second person, plain, practical, one idea, subject-neutral (your subject / a topic / your work)",
 "source": "rewritten from catalogue/context/pathway/<pathway>.json capabilities[].statement",
 "status": "drafted",
 "generated": new Date().toISOString().slice(0, 10),
 "pathways": {}
};

const problems = [];
for (const slug of Object.keys(base)) {
 const caps = base[slug];
 const sfMap = SF[slug] || {};
 const seen = new Set();
 out.pathways[slug] = caps.map(c => {
  if (seen.has(c.id)) problems.push(`${slug}: duplicate id ${c.id}`);
  seen.add(c.id);
  const sf = sfMap[c.id];
  if (!sf) problems.push(`${slug}: MISSING studentFacing for ${c.id}`);
  return { id: c.id, tier: c.tier, fheqLevel: c.L, academic: c.academic || c.statement, studentFacing: sf || null };
 });
 for (const id of Object.keys(sfMap)) {
  if (!caps.find(c => c.id === id)) problems.push(`${slug}: stray SF id ${id} (no such capability)`);
 }
}

const total = Object.values(out.pathways).reduce((a, b) => a + b.length, 0);
const withSF = Object.values(out.pathways).reduce((a, b) => a + b.filter(x => x.studentFacing).length, 0);
console.log(`pathways: ${Object.keys(out.pathways).length}  capabilities: ${total}  with studentFacing: ${withSF}`);
if (problems.length) { console.log('PROBLEMS:\n  ' + problems.join('\n  ')); process.exit(1); }

const dest = __dirname + '/../catalogue/context/pathway-student-facing.json';
fs.writeFileSync(dest, JSON.stringify(out, null, 2) + '\n');
console.log('OK -> catalogue/context/pathway-student-facing.json');
