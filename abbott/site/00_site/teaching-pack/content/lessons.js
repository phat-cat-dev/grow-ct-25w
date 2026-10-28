/* Authored lesson content. The build adds: key ideas (from skos/concepts.json),
   concept links and sources. Everything else about a lesson is written here. */
const C = 'course-teaching-meta';
const L = (n) => `lesson-teaching-meta-0${n}`;

module.exports = [
/* ------------------------------------------------------------------ 1 */
{
  record: {
    id: L(1), sequence: 1, title: 'Teaching as a connected cycle',
    summary: 'See the four processes under every session and how evidence travels from one to the next.',
    scope: {
      focus: 'The map of the course: four processes and the evidence that links them.',
      in_scope: ['Planning, delivering, evaluating and reflecting as separate processes', 'Evidence as the link between them'],
      out_of_scope: ['Detailed planning or assessment methods, which later lessons cover']
    },
    alignment: { course_outcome_ids: ['CO1'] },
    prerequisites: { knowledge: ['You have taught, or will soon teach, at least one session.'], required_lesson_ids: [] },
    learning_outcomes: [
      { id: 'LO1', statement: 'Describe planning, delivering and evaluating as three linked processes, with reflection running through them.', course_outcome_ids: ['CO1'], evidence: 'You write one sentence on what each process does.' },
      { id: 'LO2', statement: 'Sort a teaching decision into the process it belongs to.', course_outcome_ids: ['CO1'], evidence: 'You sort ten decisions and explain any you found hard.' },
      { id: 'LO3', statement: 'Name the evidence one process hands to the next.', course_outcome_ids: ['CO1'], evidence: 'You trace one decision around the cycle.' }
    ],
    estimated_duration_minutes: 15,
    materials_required: ['A session you teach or will teach soon'],
    activities: [
      { id: 'ACT1', purpose: 'Practise telling planning, delivering and evaluating decisions apart.', lesson_outcome_ids: ['LO1', 'LO2'] },
      { id: 'ACT2', purpose: 'Trace one decision around the whole cycle to see what evidence connects the stages.', lesson_outcome_ids: ['LO3'] },
      { id: 'ACT3', purpose: 'List the evidence you will have after your next session.', lesson_outcome_ids: ['LO3'] }
    ],
    assessment: { purpose: 'formative', lesson_outcome_ids: ['LO1', 'LO2', 'LO3'] },
    frontmatter: {
      eyebrow: 'Lesson 1',
      body: 'Most of what makes a session work happens before and after you stand up to teach. In this lesson you will map the processes under a session and see how evidence links them.'
    }
  },
  intro: [
    'When people describe teaching they usually describe the session: the talking, the activities, the questions. That is the visible part. Under it sit four processes. You plan what learners should achieve. You deliver a session that gets them there. You evaluate what they learned and how well your teaching helped. Reflection runs through all three, and it decides what you change.',
    'These are meta-processes because they sit above any particular technique. A technique such as a think-pair-share is one move. The processes tell you when to use it, how to tell whether it worked and what to do next.',
    'The link between the stages is evidence. Planning sets what counts as evidence. Delivery produces it. Evaluation interprets it. Reflection turns the interpretation into a change. If a stage produces no evidence, the next stage has nothing to work with.'
  ],
  activities: {
    ACT1: 'Here are ten decisions. Sort each into planning, delivering or evaluating. (1) Choosing to start with a recap question. (2) Spotting that half the group is stuck and re-explaining. (3) Deciding learners will draft a search strategy as the final task. (4) Reading exit tickets after the session. (5) Splitting a long demonstration into two parts before the day. (6) Asking a colleague to observe you. (7) Moving on early because the check showed everyone understood. (8) Writing the outcome. (9) Comparing learner drafts with the success criteria. (10) Deciding what to do if the activity overruns. Note any you could place in two stages. Decisions 6 and 10 are the awkward ones, and the awkwardness is the point: the stages overlap.',
    ACT2: 'Pick one decision from your own practice, such as how you open a session. Write down, in order: what you planned and why; what you saw when you delivered it; what evidence you could point to afterwards; how you judged it; and what you would change. If you cannot fill a step, mark it. That gap is where the cycle breaks for you.',
    ACT3: 'Think of your next session. List three pieces of evidence you will have at the end, such as answers, questions or work produced. Beside each, write what it will tell you. If the list is empty or vague, you have found something to plan in lesson 2.'
  },
  checks: [
    'Which process would you call on when you notice, mid-session, that a group is confused?',
    'Why is evidence described as the link between the stages?',
    'Name one technique you use and say which process tells you when to use it.'
  ],
  practice: 'Choose the session you will use for your portfolio. Write its title and date at the top of a new document and add the heading Evidence I expect to have.'
},
/* ------------------------------------------------------------------ 2 */
{
  record: {
    id: L(2), sequence: 2, title: 'Planning backwards',
    summary: 'Start from the outcome and the evidence, then choose the activity.',
    scope: {
      focus: 'Writing outcomes, deciding evidence and checking alignment.',
      in_scope: ['Observable outcomes', 'Choosing evidence before activities', 'Alignment checks', 'Finding out what learners already know'],
      out_of_scope: ['Programme-level curriculum design', 'Writing assessment tasks in full']
    },
    alignment: { course_outcome_ids: ['CO2'] },
    prerequisites: { knowledge: [], required_lesson_ids: [L(1)] },
    learning_outcomes: [
      { id: 'LO1', statement: 'Write a learning outcome that names an action a learner performs and you could observe.', course_outcome_ids: ['CO2'], evidence: 'You rewrite three weak outcomes.' },
      { id: 'LO2', statement: 'Decide what evidence would show the outcome has been met before you choose activities.', course_outcome_ids: ['CO2'], evidence: 'You complete a three-step backward design for one topic.' },
      { id: 'LO3', statement: 'Check a plan for alignment between outcome, activity and evidence.', course_outcome_ids: ['CO2'], evidence: 'You fill in an alignment table and mark any mismatch.' }
    ],
    estimated_duration_minutes: 20,
    materials_required: ['The session you chose for your portfolio'],
    activities: [
      { id: 'ACT1', purpose: 'Rewrite unobservable outcomes as observable ones.', lesson_outcome_ids: ['LO1'] },
      { id: 'ACT2', purpose: 'Plan one topic in three backward steps.', lesson_outcome_ids: ['LO2'] },
      { id: 'ACT3', purpose: 'Test a plan for alignment and find out what learners already know.', lesson_outcome_ids: ['LO3'] }
    ],
    assessment: { purpose: 'formative', lesson_outcome_ids: ['LO1', 'LO2', 'LO3'] },
    frontmatter: {
      eyebrow: 'Lesson 2',
      body: 'A plan that starts from an activity can be busy and still miss the point. In this lesson you will start from the outcome and the evidence, and choose the activity last.'
    }
  },
  intro: [
    'It is natural to plan by topic: what shall I cover on Thursday? Backward design asks a different first question: what should learners be able to do afterwards, and how will I know? Once you can answer both, the activity almost chooses itself, because you need one that gets learners practising the thing you will look for.',
    'The test of a plan is alignment. Take each activity and each check and ask which outcome it serves. A task that asks learners to list when the outcome says evaluate will not produce the evidence you need, and that is a fault in the design, not in the learners.',
    'Planning also needs a starting point. What learners already know, including what they believe wrongly, decides where you begin and how much support to build in.'
  ],
  activities: {
    ACT1: 'Rewrite these so that a learner action is visible. (a) Understand how to reference. (b) Know what a database is. (c) Appreciate the importance of peer review. For each, ask: what would a learner do that I could see? A possible rewrite of (a) is Reference a journal article correctly in a short paragraph using the department style. Check that your verbs sit at the level you intend. The cognitive taxonomy gives you a ladder from remembering to creating.',
    ACT2: 'Take one topic from your session. Step 1: write the outcome. Step 2: write what a learner would produce that shows it, and what a good version looks like. Step 3: only now list the activities that would let learners practise producing it. Notice whether the activity you first thought of survived.',
    ACT3: 'Draw a table with three columns: outcome, activity, evidence. Fill one row per activity. Mark any row where the activity does not lead to the evidence, or where the evidence does not show the outcome. Then write two questions you could ask learners before the session to find out what they already know, and say what answer would change your plan.'
  },
  checks: [
    'Why is understand a weak verb in an outcome?',
    'In backward design, when do you choose the activity, and why then?',
    'A plan has an outcome of critique sources and an activity of list sources. What is the fault and how would you fix it?'
  ],
  practice: 'Write the outcome and the evidence for your portfolio session. Add the alignment table beneath them.'
},
/* ------------------------------------------------------------------ 3 */
{
  record: {
    id: L(3), sequence: 3, title: 'Designing the session',
    summary: 'Sequence the session, manage load, plan support and remove barriers.',
    scope: {
      focus: 'Turning an aligned plan into a session structure.',
      in_scope: ['Sequencing', 'Cognitive load', 'Scaffolding and its removal', 'Active tasks', 'Barriers and alternatives'],
      out_of_scope: ['Technology choices', 'Room layout']
    },
    alignment: { course_outcome_ids: ['CO2'] },
    prerequisites: { knowledge: [], required_lesson_ids: [L(2)] },
    learning_outcomes: [
      { id: 'LO1', statement: 'Sequence a session into stages that each build on the one before.', course_outcome_ids: ['CO2'], evidence: 'You write a timed outline with the purpose of each stage.' },
      { id: 'LO2', statement: 'Reduce the new material in a stage to what working memory can hold.', course_outcome_ids: ['CO2'], evidence: 'You split one overloaded stage into smaller parts.' },
      { id: 'LO3', statement: 'Plan a scaffold and say when it will be withdrawn.', course_outcome_ids: ['CO2'], evidence: 'You write a three-attempt scaffold plan.' },
      { id: 'LO4', statement: 'Identify one barrier in your plan and offer an alternative route to the same outcome.', course_outcome_ids: ['CO2'], evidence: 'You name a barrier and write an alternative.' }
    ],
    estimated_duration_minutes: 25,
    materials_required: ['The aligned plan from lesson 2'],
    activities: [
      { id: 'ACT1', purpose: 'Build a timed outline and test its sequence.', lesson_outcome_ids: ['LO1', 'LO2'] },
      { id: 'ACT2', purpose: 'Plan support that fades.', lesson_outcome_ids: ['LO3'] },
      { id: 'ACT3', purpose: 'Look for barriers and plan alternatives.', lesson_outcome_ids: ['LO4'] }
    ],
    assessment: { purpose: 'formative', lesson_outcome_ids: ['LO1', 'LO2', 'LO3', 'LO4'] },
    frontmatter: {
      eyebrow: 'Lesson 3',
      body: 'An aligned plan still needs a shape. In this lesson you will order the session, keep the load manageable, plan support that fades and look for barriers before they appear.'
    }
  },
  intro: [
    'A session is a sequence, and a sequence is a hypothesis: if learners do this first, they will be ready for that next. A common and well-supported pattern is a short review, a small amount of new material, guided practice and then practice on their own. What matters is that each stage earns the next.',
    'Learners can only hold a few new things at once. If you present too much, or present it confusingly, nothing is left over for learning. Cut or split before you add support.',
    'Support helps when it is temporary. Plan how it will go: a model, then a partial model, then nothing. And plan for variation. Ask where a barrier could arise for a learner who reads slowly, joins late, works in a second language or cannot see the screen, and offer more than one route to the same outcome.'
  ],
  activities: {
    ACT1: 'Write your session as a timed outline with five or six stages. Beside each stage write its purpose in a few words, such as recall last week, introduce one idea, practise with help. Then mark the stage with the most new material and ask whether a learner could hold all of it. If not, split it and put a short practice task between the parts.',
    ACT2: 'Choose one task learners will do. Write a three-attempt plan: what help they get on the first attempt, what they get on the second and what they get on the third. The third should be nothing. If you cannot remove the help, ask whether the task is too hard for this group or whether the help is doing the thinking for them.',
    ACT3: 'Read your outline as three different learners: one who arrives knowing little, one who works slowly and one who uses a screen reader or captions. Where would each get stuck? Pick the most likely barrier and write an alternative route that still reaches the same outcome. Check that the alternative asks for the same thinking, not an easier version.'
  },
  checks: [
    'Why is a session sequence described as a hypothesis?',
    'What is the first thing to try when a stage has too much new material?',
    'What makes a scaffold temporary in practice?'
  ],
  practice: 'Add the timed outline, the scaffold plan and one barrier with its alternative to your portfolio document.'
},
/* ------------------------------------------------------------------ 4 */
{
  record: {
    id: L(4), sequence: 4, title: 'Delivering and adapting',
    summary: 'Check understanding as you teach and change course when the evidence says so.',
    scope: {
      focus: 'The delivery moves that produce evidence and the decisions that use it.',
      in_scope: ['Explaining', 'Questions', 'Checks that reach every learner', 'Retrieval', 'Changing the plan during teaching', 'Climate and pacing'],
      out_of_scope: ['Presentation skills and voice work', 'Managing disruptive behaviour']
    },
    alignment: { course_outcome_ids: ['CO3'] },
    prerequisites: { knowledge: [], required_lesson_ids: [L(3)] },
    learning_outcomes: [
      { id: 'LO1', statement: 'Choose a check that reaches every learner at a set point in a session.', course_outcome_ids: ['CO3'], evidence: 'You place two checks in your outline and name the method.' },
      { id: 'LO2', statement: 'Write a question that shows what learners think and not only whether they are right.', course_outcome_ids: ['CO3'], evidence: 'You rewrite three questions.' },
      { id: 'LO3', statement: 'State in advance what you will do if a check shows the group has not understood.', course_outcome_ids: ['CO3'], evidence: 'You write an if-then plan for each check.' },
      { id: 'LO4', statement: 'Describe one routine that makes it likely learners will contribute.', course_outcome_ids: ['CO3'], evidence: 'You write the routine and what you will say to a wrong answer.' }
    ],
    estimated_duration_minutes: 25,
    materials_required: ['The timed outline from lesson 3'],
    activities: [
      { id: 'ACT1', purpose: 'Place checks and write if-then responses.', lesson_outcome_ids: ['LO1', 'LO3'] },
      { id: 'ACT2', purpose: 'Improve questions so they reveal thinking.', lesson_outcome_ids: ['LO2'] },
      { id: 'ACT3', purpose: 'Plan climate routines and protect the closing check.', lesson_outcome_ids: ['LO4'] }
    ],
    assessment: { purpose: 'formative', lesson_outcome_ids: ['LO1', 'LO2', 'LO3', 'LO4'] },
    frontmatter: {
      eyebrow: 'Lesson 4',
      body: 'A plan is a set of intentions. Delivery is where you find out what happened. In this lesson you will build checks into your session and decide in advance how you will respond.'
    }
  },
  intro: [
    'The plan tells you what you hope will happen. Delivery tells you what is happening. The gap between them is the most useful information a teacher has, and you only see it if you build in ways of looking.',
    'Quiet does not mean understood. A check works when it reaches every learner: a quick written answer, a hand signal, a one-question poll. Asking whether there are any questions reaches only the confident few. Decide where the checks go, and decide what you will do with each possible result.',
    'Questions also do two jobs. They can test whether a learner knows an answer, and they can find out what the learner thinks. The second job tells you more. Add a learning climate in which a wrong answer is useful data and you will keep getting honest evidence. Finally, protect the ending. If time is short, cut the middle and keep the closing check.'
  ],
  activities: {
    ACT1: 'Open your outline from lesson 3. Place two checks at the points where a misunderstanding would hurt most. For each, name the method and make sure it reaches every learner. Then write an if-then line: if most learners get it, I will move on to X; if fewer than half get it, I will do Y; if the group splits, I will do Z. Y might be a second worked example. Z might be pairing learners who got it with those who did not.',
    ACT2: 'Rewrite each question so it shows thinking. (a) Is this a good source? becomes What makes this source more or less reliable than the last one? (b) Does everyone understand? becomes Write one sentence explaining this step to a colleague. (c) What is a keyword? becomes Which keyword would you try first for this question, and why? Notice that each rewrite asks for reasons and not only for a label.',
    ACT3: 'Write one routine that makes contribution likely, such as everyone writing before anyone speaks. Then write the exact words you will say when a learner gives a wrong answer so that the answer becomes useful. Finally mark in your outline which stage you would cut if you ran ten minutes late, and confirm that the closing check stays.'
  },
  checks: [
    'Why does asking whether there are any questions give weak evidence?',
    'What is the difference between a question that tests and one that probes?',
    'What do you decide in advance so that a check changes what you do?'
  ],
  practice: 'Add the two checks and their if-then lines to your portfolio. After you teach the session, note which check you used and what you changed because of it.'
},
/* ------------------------------------------------------------------ 5 */
{
  record: {
    id: L(5), sequence: 5, title: 'Evaluating learning and teaching',
    summary: 'Judge what was learned and how well the teaching helped, using more than impressions.',
    scope: {
      focus: 'Using evidence, criteria and feedback to judge learning, then using wider sources to judge teaching.',
      in_scope: ['Formative and summative purposes', 'Criteria', 'Feedback', 'Evaluating a session', 'Peer observation'],
      out_of_scope: ['Designing a full assessment strategy for a module', 'Moderation and marking policy']
    },
    alignment: { course_outcome_ids: ['CO4'] },
    prerequisites: { knowledge: [], required_lesson_ids: [L(4)] },
    learning_outcomes: [
      { id: 'LO1', statement: 'Tell formative and summative purposes apart and say which a given task serves.', course_outcome_ids: ['CO4'], evidence: 'You classify five tasks and justify each.' },
      { id: 'LO2', statement: 'Write criteria that a learner could use to judge their own work.', course_outcome_ids: ['CO4'], evidence: 'You write three criteria in plain language.' },
      { id: 'LO3', statement: 'Give feedback that names the gap and points to the next step.', course_outcome_ids: ['CO4'], evidence: 'You rewrite a comment so a learner can act on it.' },
      { id: 'LO4', statement: 'Gather evidence about a session from learners and one other source.', course_outcome_ids: ['CO4'], evidence: 'You plan a short evaluation with two sources.' }
    ],
    estimated_duration_minutes: 25,
    materials_required: ['Learner work or exit answers from your session, if you have taught it'],
    activities: [
      { id: 'ACT1', purpose: 'Classify tasks by purpose.', lesson_outcome_ids: ['LO1'] },
      { id: 'ACT2', purpose: 'Write criteria and rewrite feedback.', lesson_outcome_ids: ['LO2', 'LO3'] },
      { id: 'ACT3', purpose: 'Plan an evaluation of your own session.', lesson_outcome_ids: ['LO4'] }
    ],
    assessment: { purpose: 'formative', lesson_outcome_ids: ['LO1', 'LO2', 'LO3', 'LO4'] },
    frontmatter: {
      eyebrow: 'Lesson 5',
      body: 'Evaluation answers two questions: what did learners learn, and how well did your teaching help? In this lesson you will practise both and plan how to gather evidence for your own session.'
    }
  },
  intro: [
    'Assessment is not only something that happens at the end. The same piece of evidence can serve two purposes. When you use it to change the teaching or to help the learner while there is still time, it is formative. When you use it to judge what has been achieved at the end, it is summative. The test is what you do with it.',
    'Criteria tell learners what good looks like. Share them before the task and write them in words a learner can use. Feedback then closes the gap between where the learner is and where the criteria point. Useful feedback answers three questions: where am I going, how am I doing and where next. A comment the learner cannot act on is commentary.',
    'Evaluating your teaching is the other half. Use what learners produced, not only how they felt about the session. Add a second source, such as a colleague who watches for one thing you chose in advance. Description comes first. Judgement comes after.'
  ],
  activities: {
    ACT1: 'Classify each task as mainly formative or summative, and say what you would do with the result. (a) A one-question poll mid-session. (b) A marked essay at the end of a module. (c) Exit tickets. (d) A draft with comments before submission. (e) A final quiz that counts toward the grade. Then pick one summative task and describe how you could make a formative version of it for learners to try first.',
    ACT2: 'Write three criteria for the outcome you set in lesson 2. Use plain words and describe quality, for example Each claim has a source that a reader could find. Then rewrite this comment so a learner can act on it: Needs more depth. A rewrite might read Your first two points are clear. The third has no evidence. Add one source and one sentence saying what it shows.',
    ACT3: 'Plan how you will evaluate your portfolio session. Choose two sources: one of learner evidence, such as exit answers measured against your criteria, and one other, such as a colleague observing a focus you choose, for example how many learners answered each question. Write the focus, the method and the date. Decide what result would lead you to change your plan.'
  },
  checks: [
    'What makes an assessment formative in practice?',
    'What three questions should feedback answer?',
    'Why is learner satisfaction a weak basis on its own for judging your teaching?'
  ],
  practice: 'Add your criteria and your evaluation plan to the portfolio. When the session has run, add the evidence you gathered.'
},
/* ------------------------------------------------------------------ 6 */
{
  record: {
    id: L(6), sequence: 6, title: 'Closing the loop',
    summary: 'Reflect with a structured cycle and turn the result into a change to your next plan.',
    scope: {
      focus: 'Reflection in and after a session and a written action that feeds the next plan.',
      in_scope: ['Reflection during and after teaching', 'Two reflective cycles', 'Writing a decision', 'Connecting the four processes'],
      out_of_scope: ['Reflective writing for accreditation portfolios']
    },
    alignment: { course_outcome_ids: ['CO1', 'CO5'] },
    prerequisites: { knowledge: [], required_lesson_ids: [L(5)] },
    learning_outcomes: [
      { id: 'LO1', statement: 'Reflect on a session using a structured cycle.', course_outcome_ids: ['CO5'], evidence: 'You complete the cycle for your portfolio session.' },
      { id: 'LO2', statement: 'Write a reflection that keeps description separate from interpretation.', course_outcome_ids: ['CO5'], evidence: 'You mark which sentences describe and which interpret.' },
      { id: 'LO3', statement: 'Name one specific change to your next plan and the evidence that prompted it.', course_outcome_ids: ['CO5'], evidence: 'You write one dated action.' },
      { id: 'LO4', statement: 'Explain how your change touches planning, delivering and evaluating.', course_outcome_ids: ['CO1'], evidence: 'You write three sentences, one for each process.' }
    ],
    estimated_duration_minutes: 20,
    materials_required: ['Your portfolio document, including the evaluation'],
    activities: [
      { id: 'ACT1', purpose: 'Work through a reflective cycle on your session.', lesson_outcome_ids: ['LO1', 'LO2'] },
      { id: 'ACT2', purpose: 'Turn the reflection into one dated action.', lesson_outcome_ids: ['LO3'] },
      { id: 'ACT3', purpose: 'Trace the change across the whole cycle.', lesson_outcome_ids: ['LO4'] }
    ],
    assessment: { purpose: 'formative', lesson_outcome_ids: ['LO1', 'LO2', 'LO3', 'LO4'] },
    frontmatter: {
      eyebrow: 'Lesson 6',
      body: 'Reflection is the step that closes the loop. In this lesson you will use a structured cycle on your own session and end with one specific change to your next plan.'
    }
  },
  intro: [
    'Reflection happens at two speeds. In the moment, you notice that something is not working and change course. Afterwards, you step back and ask what happened and why. Both depend on having clear intentions to compare against, which is why the earlier lessons asked you to write outcomes and checks first.',
    'A reflective cycle gives the afterwards kind some structure. Kolb describes a loop of experience, observation, concept and experiment. Gibbs offers six prompts: description, feelings, evaluation, analysis, conclusion and action plan. Either works if you keep description apart from judgement and finish with a decision.',
    'The decision is what closes the loop. A good one is small, specific and tied to evidence: not be clearer, but add a one-sentence summary check after the second demonstration because six of twelve exit answers missed the key step.'
  ],
  activities: {
    ACT1: 'Use the Gibbs prompts on your portfolio session. Write a few sentences for each: what happened, what you felt, what went well and less well, why, what else you could have done and what you will do. When you finish, read it back and mark each sentence D for description or I for interpretation. If the description section contains judgements, move them to the evaluation.',
    ACT2: 'Write one change to your next plan. It must name what you will change, where in the session, and the evidence that prompted it. Add a date by which you will make the change. If you wrote more than one change, keep the one with the strongest evidence.',
    ACT3: 'Write three sentences about your change. One says how it alters your planning, for example a new outcome or check. One says how it alters your delivery. One says how you will know whether it worked. Then look back at lesson 1 and update the cycle you traced there.'
  },
  checks: [
    'What is the difference between reflection-in-action and reflection-on-action?',
    'Why must a reflection end with a decision?',
    'Why do the Gibbs prompts put description before evaluation?'
  ],
  practice: 'Finish your portfolio. It should now hold the plan, the alignment table, the outline, the checks, the criteria, the evidence, the evaluation, the reflection and one dated action.'
}
];
