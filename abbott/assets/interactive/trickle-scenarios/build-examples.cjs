const fs = require('node:fs');
const path = require('node:path');
const { validate } = require('./scenario.js');
const definitions = [
  {
    id: 'project-rescue', title: 'The project that changed overnight',
    intro: 'A deadline, incomplete evidence and a team waiting for a decision. Follow the consequences through three decisions and a final commitment.',
    opening: 'It is Monday. Your team has four days to deliver a learning prototype. A key source has changed and your first design may no longer fit.',
    decisions: [
      ['Choose your first move', 'What do you do before the team starts building?', 'Check the changed evidence', 'You uncover a requirement that the old brief missed. The team has less building time, but a clearer target.', 'Keep building from the old brief', 'The first screen looks polished. A reviewer then points out that it solves yesterday\'s problem. Rework is now part of the plan.'],
      ['Set the scope', 'You cannot complete every feature by Friday. What will you protect?', 'One complete learning journey', 'You choose a smaller end-to-end experience with a clear outcome. Several attractive extras move to a later release.', 'A sample of every feature', 'The breadth makes the concept easy to discuss, but several routes stop at placeholders. You must explain that limit in the review.'],
      ['Respond to the trial', 'Two learners misunderstand the instruction. The stakeholder wants more decoration. What comes first?', 'Rewrite and retest the instruction', 'A quick trial shows that learners can now start independently. You record the visual request for the next iteration.', 'Add the requested decoration first', 'The stakeholder likes the new look. The instruction is still unclear, so the team must explicitly flag that learning risk.'],
    ],
    ending: 'Your route is ready to discuss. Compare the consequences of your decisions: evidence, scope and learning clarity. This scenario records a route, not a right-answer score.',
  },
  {
    id: 'source-detective', title: 'Can we trust this claim?',
    intro: 'Trace an attractive claim from a shared message to an evidence-based response. Three decisions, multiple consequences and space to reflect.',
    opening: 'A colleague shares a striking statistic and asks you to use it in tomorrow\'s workshop. There is no source in the message.',
    decisions: [
      ['Find the origin', 'What do you investigate first?', 'Locate the original report', 'The original report describes a small local sample. The headline in the message removed that context.', 'Use the most repeated version', 'Several sites repeat the same number. Their agreement looks reassuring until you notice that they all cite one unsourced post.'],
      ['Compare the evidence', 'A second report gives a different result. How do you respond?', 'Compare methods and populations', 'The reports measure different outcomes in different groups. You can explain why their numbers should not be treated as direct opposites.', 'Choose the more dramatic result', 'Your slide has a strong opening, but a participant asks whether the samples are comparable. Your notes do not yet answer that question.'],
      ['Communicate uncertainty', 'How will you present the evidence?', 'State the limits and cite the source', 'You distinguish what the evidence suggests from what it cannot establish. Participants have a source they can inspect.', 'Present the number as a universal fact', 'The message is simple, but stronger than the evidence. You need a correction before using it as learning material.'],
    ],
    ending: 'Write the claim you would now feel comfortable sharing. Include its source, limits and a question that remains open.',
  },
  {
    id: 'support-conversation', title: 'A learner has gone quiet',
    intro: 'Practise a supportive conversation without pretending to diagnose another person. Follow several layers of choices and consequences.',
    opening: 'A learner who usually contributes has missed two activities. You do not know why. You have a chance to offer support.',
    decisions: [
      ['Open the conversation', 'How do you make first contact?', 'Send a private, non-judgmental invitation', 'The learner can choose whether and how to respond. You explain what support is available without making assumptions.', 'Ask for an explanation in the group', 'The learner receives attention they did not request. You will need to move the conversation to a private channel and acknowledge that choice.'],
      ['Listen before planning', 'The learner says the workload feels difficult. What next?', 'Ask which part is hardest to access', 'They describe a specific barrier. You can discuss adjustments to the activity rather than guessing at the cause.', 'Offer your usual solution immediately', 'Your suggestion may help, but you have not checked the barrier. You pause and ask whether it fits their situation.'],
      ['Agree a next step', 'How will the conversation finish?', 'Agree one achievable step and a check-in', 'The learner chooses a manageable action. You both know when to check whether the arrangement helped.', 'Leave the plan open-ended', 'There is room for flexibility, but no shared next action. You offer to agree a smaller, clearer step when the learner is ready.'],
    ],
    ending: 'Reflect on privacy, listening and learner agency. This is a practice conversation, not clinical advice or a substitute for your organisation\'s support procedures.',
  },
];
function create(def) {
  const nodes = [
    { id: 'opening', type: 'continue', title: 'The situation', body: def.opening, button: 'Step into the scenario', next: 'decision-1' },
  ];
  def.decisions.forEach(([title, body, a, consequenceA, b, consequenceB], index) => {
    const n = index + 1;
    nodes.push(
      { id: `decision-${n}`, type: 'choice', title, body, choices: [{ label: a, next: `consequence-${n}-a` }, { label: b, next: `consequence-${n}-b` }] },
      ...[['a', consequenceA], ['b', consequenceB]].map(([branch, consequence]) => ({
        id: `consequence-${n}-${branch}`, type: 'auto', title: `What happens next / decision ${n}`, body: consequence,
        delayMs: 1800, button: 'Consider the next step', next: `reflection-${n}`,
      })),
      { id: `reflection-${n}`, type: 'continue', title: `Pause and reflect / ${n}`, body: 'Notice what your decision made possible and what it left unresolved.', prompt: 'Why did you choose this route?',
        button: n === 3 ? 'Review the outcome' : 'Make the next decision', next: n === 3 ? 'outcome' : `decision-${n + 1}` },
    );
  });
  nodes.push({ id: 'outcome', type: 'ending', title: 'Your route, your explanation', body: def.ending, prompt: 'What would you keep or change next time?' });
  return { version: 1, id: def.id, title: def.title, intro: def.intro, start: 'opening', nodes };
}
const examples = definitions.map(create);
examples.push({
  version: 1, id: 'team-conversation', title: 'The meeting before the deadline',
  intro: 'Learning goal: practise evidence-based, respectful disagreement under pressure. For individual or group use. Before each choice, note your instinct; after an outcome, compare it with another route.',
  start: 'arrival',
  nodes: [
    { id: 'arrival', type: 'continue', title: 'Ten minutes before the review', body: 'You coordinate a small project team. Sam has found an accessibility barrier in the prototype. Alex says there is no time to change anything. Your role is to agree a credible next step without hiding the barrier.', next: 'opening', button: 'Join the meeting' },
    { id: 'opening', type: 'choice', title: 'How do you open the discussion?', body: 'Alex interrupts Sam: "We already agreed this design." The room goes quiet.', prompt: 'Write your first instinct before choosing.',
      choices: [{ label: 'Make space for Sam to demonstrate the barrier', next: 'demonstration' }, { label: 'Take the disagreement out of the meeting', next: 'private-talk' }] },
    { id: 'demonstration', type: 'auto', title: 'A barrier everyone can see', body: 'Sam shows that the keyboard cannot reach the final action. Alex acknowledges the problem but worries that a large change would break other screens.', delayMs: 1800, next: 'scope' },
    { id: 'scope', type: 'choice', title: 'What change will you propose?', body: 'The team can test a narrow fix today, or postpone this interaction and explain why.',
      choices: [{ label: 'Try a narrow keyboard fix with a test', next: 'trial' }, { label: 'Remove the interaction from this release', next: 'alternative' }] },
    { id: 'trial', type: 'auto', title: 'The first test is promising', body: 'The final action is reachable. Sam asks to check focus visibility and the order of controls before declaring the whole interaction accessible.', delayMs: 1800, next: 'verification' },
    { id: 'verification', type: 'choice', title: 'What counts as ready?', body: 'You have time for one more focused check before the review.',
      choices: [{ label: 'Run the check and describe the limits honestly', next: 'test-notes' }, { label: 'Call the interaction fully accessible now', next: 'overclaim' }] },
    { id: 'test-notes', type: 'continue', title: 'A clear record', body: 'The focused check finds one confusing focus indicator. You fix it and record what was tested, what was not, and who will review next.', prompt: 'What evidence supports your recommendation?', next: 'review-choice' },
    { id: 'review-choice', type: 'choice', title: 'Lead the review', body: 'The reviewer asks why the design changed so late.',
      choices: [{ label: 'Explain the barrier, fix, checks and remaining limits', next: 'shared-plan' }, { label: 'Describe the change as cosmetic', next: 'overclaim' }] },
    { id: 'alternative', type: 'continue', title: 'A smaller release', body: 'The team can offer the same learning content as a straightforward reading activity. It loses the interaction but avoids publishing a known keyboard barrier.', next: 'alternative-check' },
    { id: 'alternative-check', type: 'choice', title: 'Check the replacement', body: 'The replacement needs a clear purpose and a quick access check too.',
      choices: [{ label: 'Test the replacement and record the deferred feature', next: 'scoped-release' }, { label: 'Assume simple content needs no checking', next: 'unchecked' }] },
    { id: 'private-talk', type: 'continue', title: 'The conversation becomes quieter', body: 'Alex is less defensive in private. Sam is no longer present to demonstrate the issue. You still need evidence, not a decision based only on who speaks most confidently.', next: 'private-choice' },
    { id: 'private-choice', type: 'choice', title: 'Rebuild a shared view', body: 'How will you bring the concern back into the plan?',
      choices: [{ label: 'Invite Sam to show the barrier with the whole team', next: 'demonstration' }, { label: 'Let Alex decide whether the concern matters', next: 'deferred-voice' }] },
    { id: 'deferred-voice', type: 'auto', title: 'The original plan continues', body: 'The concern is treated as a preference rather than an access barrier. Sam sends a written example so it is not lost.', delayMs: 1800, next: 'last-chance' },
    { id: 'last-chance', type: 'choice', title: 'The written example arrives', body: 'The review has not begun. There is still time to make the issue visible.',
      choices: [{ label: 'Return to the evidence and agree a limited response', next: 'scope' }, { label: 'Leave the issue out of the review', next: 'unchecked' }] },
    { id: 'shared-plan', type: 'ending', title: 'Outcome / a shared, evidence-led plan', body: 'The team can explain its decisions and remaining uncertainty. Sam and Alex both have clear next actions. Debrief: which choice helped the team disagree constructively?', prompt: 'What would you transfer to a real meeting?' },
    { id: 'scoped-release', type: 'ending', title: 'Outcome / a deliberate smaller release', body: 'The team releases a checked alternative and names the deferred interaction. This is a different strategy, not an automatic failure. Debrief: what learning value was retained, and what was lost?', prompt: 'When would a smaller release be appropriate?' },
    { id: 'overclaim', type: 'ending', title: 'Outcome / confidence beyond the evidence', body: 'The review receives a stronger claim than the tests support. The next task is to correct that claim and agree further checks. Debrief: what would an honest description have said?', prompt: 'Rewrite the claim using only the evidence you have.' },
    { id: 'unchecked', type: 'ending', title: 'Outcome / an unresolved barrier', body: 'The plan goes forward without a clear check or visible record of the issue. A learner may still be blocked. Debrief: identify an earlier opportunity to change this route.', prompt: 'Which earlier decision would you revisit, and why?' },
  ],
});
examples.forEach(example => {
  validate(example);
  fs.writeFileSync(path.join(__dirname, `${example.id}.json`), JSON.stringify(example, null, 2) + '\n');
});
const template = JSON.parse(JSON.stringify(examples[0]));
template.id = 'your-scenario';
template.title = 'Your scenario title';
template.intro = 'Replace this with the audience, context and learning intention.';
template.nodes.forEach(node => {
  node.title = `[Write ${node.type} title: ${node.id}]`;
  node.body = '[Write a specific situation, consequence or reflection here. Keep route IDs and replace all placeholder text.]';
  if (node.choices) node.choices.forEach((choice, index) => { choice.label = `[Write option ${index + 1}]`; });
  if (node.prompt) node.prompt = '[Write a reflection prompt]';
});
validate(template);
fs.writeFileSync(path.join(__dirname, 'scenario-template.json'), JSON.stringify(template, null, 2) + '\n');
fs.writeFileSync(path.join(__dirname, 'examples.js'), `window.TrickleExamples = ${JSON.stringify(examples, null, 2)};\n`);
console.log('Built four scenarios, including divergent endings and 11-card routes, plus a fill-in JSON template.');
