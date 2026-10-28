window.TrickleExamples = [
  {
    "version": 1,
    "id": "project-rescue",
    "title": "The project that changed overnight",
    "intro": "A deadline, incomplete evidence and a team waiting for a decision. Follow the consequences through three decisions and a final commitment.",
    "start": "opening",
    "nodes": [
      {
        "id": "opening",
        "type": "continue",
        "title": "The situation",
        "body": "It is Monday. Your team has four days to deliver a learning prototype. A key source has changed and your first design may no longer fit.",
        "button": "Step into the scenario",
        "next": "decision-1"
      },
      {
        "id": "decision-1",
        "type": "choice",
        "title": "Choose your first move",
        "body": "What do you do before the team starts building?",
        "choices": [
          {
            "label": "Check the changed evidence",
            "next": "consequence-1-a"
          },
          {
            "label": "Keep building from the old brief",
            "next": "consequence-1-b"
          }
        ]
      },
      {
        "id": "consequence-1-a",
        "type": "auto",
        "title": "What happens next / decision 1",
        "body": "You uncover a requirement that the old brief missed. The team has less building time, but a clearer target.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-1"
      },
      {
        "id": "consequence-1-b",
        "type": "auto",
        "title": "What happens next / decision 1",
        "body": "The first screen looks polished. A reviewer then points out that it solves yesterday's problem. Rework is now part of the plan.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-1"
      },
      {
        "id": "reflection-1",
        "type": "continue",
        "title": "Pause and reflect / 1",
        "body": "Notice what your decision made possible and what it left unresolved.",
        "prompt": "Why did you choose this route?",
        "button": "Make the next decision",
        "next": "decision-2"
      },
      {
        "id": "decision-2",
        "type": "choice",
        "title": "Set the scope",
        "body": "You cannot complete every feature by Friday. What will you protect?",
        "choices": [
          {
            "label": "One complete learning journey",
            "next": "consequence-2-a"
          },
          {
            "label": "A sample of every feature",
            "next": "consequence-2-b"
          }
        ]
      },
      {
        "id": "consequence-2-a",
        "type": "auto",
        "title": "What happens next / decision 2",
        "body": "You choose a smaller end-to-end experience with a clear outcome. Several attractive extras move to a later release.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-2"
      },
      {
        "id": "consequence-2-b",
        "type": "auto",
        "title": "What happens next / decision 2",
        "body": "The breadth makes the concept easy to discuss, but several routes stop at placeholders. You must explain that limit in the review.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-2"
      },
      {
        "id": "reflection-2",
        "type": "continue",
        "title": "Pause and reflect / 2",
        "body": "Notice what your decision made possible and what it left unresolved.",
        "prompt": "Why did you choose this route?",
        "button": "Make the next decision",
        "next": "decision-3"
      },
      {
        "id": "decision-3",
        "type": "choice",
        "title": "Respond to the trial",
        "body": "Two learners misunderstand the instruction. The stakeholder wants more decoration. What comes first?",
        "choices": [
          {
            "label": "Rewrite and retest the instruction",
            "next": "consequence-3-a"
          },
          {
            "label": "Add the requested decoration first",
            "next": "consequence-3-b"
          }
        ]
      },
      {
        "id": "consequence-3-a",
        "type": "auto",
        "title": "What happens next / decision 3",
        "body": "A quick trial shows that learners can now start independently. You record the visual request for the next iteration.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-3"
      },
      {
        "id": "consequence-3-b",
        "type": "auto",
        "title": "What happens next / decision 3",
        "body": "The stakeholder likes the new look. The instruction is still unclear, so the team must explicitly flag that learning risk.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-3"
      },
      {
        "id": "reflection-3",
        "type": "continue",
        "title": "Pause and reflect / 3",
        "body": "Notice what your decision made possible and what it left unresolved.",
        "prompt": "Why did you choose this route?",
        "button": "Review the outcome",
        "next": "outcome"
      },
      {
        "id": "outcome",
        "type": "ending",
        "title": "Your route, your explanation",
        "body": "Your route is ready to discuss. Compare the consequences of your decisions: evidence, scope and learning clarity. This scenario records a route, not a right-answer score.",
        "prompt": "What would you keep or change next time?"
      }
    ]
  },
  {
    "version": 1,
    "id": "source-detective",
    "title": "Can we trust this claim?",
    "intro": "Trace an attractive claim from a shared message to an evidence-based response. Three decisions, multiple consequences and space to reflect.",
    "start": "opening",
    "nodes": [
      {
        "id": "opening",
        "type": "continue",
        "title": "The situation",
        "body": "A colleague shares a striking statistic and asks you to use it in tomorrow's workshop. There is no source in the message.",
        "button": "Step into the scenario",
        "next": "decision-1"
      },
      {
        "id": "decision-1",
        "type": "choice",
        "title": "Find the origin",
        "body": "What do you investigate first?",
        "choices": [
          {
            "label": "Locate the original report",
            "next": "consequence-1-a"
          },
          {
            "label": "Use the most repeated version",
            "next": "consequence-1-b"
          }
        ]
      },
      {
        "id": "consequence-1-a",
        "type": "auto",
        "title": "What happens next / decision 1",
        "body": "The original report describes a small local sample. The headline in the message removed that context.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-1"
      },
      {
        "id": "consequence-1-b",
        "type": "auto",
        "title": "What happens next / decision 1",
        "body": "Several sites repeat the same number. Their agreement looks reassuring until you notice that they all cite one unsourced post.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-1"
      },
      {
        "id": "reflection-1",
        "type": "continue",
        "title": "Pause and reflect / 1",
        "body": "Notice what your decision made possible and what it left unresolved.",
        "prompt": "Why did you choose this route?",
        "button": "Make the next decision",
        "next": "decision-2"
      },
      {
        "id": "decision-2",
        "type": "choice",
        "title": "Compare the evidence",
        "body": "A second report gives a different result. How do you respond?",
        "choices": [
          {
            "label": "Compare methods and populations",
            "next": "consequence-2-a"
          },
          {
            "label": "Choose the more dramatic result",
            "next": "consequence-2-b"
          }
        ]
      },
      {
        "id": "consequence-2-a",
        "type": "auto",
        "title": "What happens next / decision 2",
        "body": "The reports measure different outcomes in different groups. You can explain why their numbers should not be treated as direct opposites.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-2"
      },
      {
        "id": "consequence-2-b",
        "type": "auto",
        "title": "What happens next / decision 2",
        "body": "Your slide has a strong opening, but a participant asks whether the samples are comparable. Your notes do not yet answer that question.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-2"
      },
      {
        "id": "reflection-2",
        "type": "continue",
        "title": "Pause and reflect / 2",
        "body": "Notice what your decision made possible and what it left unresolved.",
        "prompt": "Why did you choose this route?",
        "button": "Make the next decision",
        "next": "decision-3"
      },
      {
        "id": "decision-3",
        "type": "choice",
        "title": "Communicate uncertainty",
        "body": "How will you present the evidence?",
        "choices": [
          {
            "label": "State the limits and cite the source",
            "next": "consequence-3-a"
          },
          {
            "label": "Present the number as a universal fact",
            "next": "consequence-3-b"
          }
        ]
      },
      {
        "id": "consequence-3-a",
        "type": "auto",
        "title": "What happens next / decision 3",
        "body": "You distinguish what the evidence suggests from what it cannot establish. Participants have a source they can inspect.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-3"
      },
      {
        "id": "consequence-3-b",
        "type": "auto",
        "title": "What happens next / decision 3",
        "body": "The message is simple, but stronger than the evidence. You need a correction before using it as learning material.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-3"
      },
      {
        "id": "reflection-3",
        "type": "continue",
        "title": "Pause and reflect / 3",
        "body": "Notice what your decision made possible and what it left unresolved.",
        "prompt": "Why did you choose this route?",
        "button": "Review the outcome",
        "next": "outcome"
      },
      {
        "id": "outcome",
        "type": "ending",
        "title": "Your route, your explanation",
        "body": "Write the claim you would now feel comfortable sharing. Include its source, limits and a question that remains open.",
        "prompt": "What would you keep or change next time?"
      }
    ]
  },
  {
    "version": 1,
    "id": "support-conversation",
    "title": "A learner has gone quiet",
    "intro": "Practise a supportive conversation without pretending to diagnose another person. Follow several layers of choices and consequences.",
    "start": "opening",
    "nodes": [
      {
        "id": "opening",
        "type": "continue",
        "title": "The situation",
        "body": "A learner who usually contributes has missed two activities. You do not know why. You have a chance to offer support.",
        "button": "Step into the scenario",
        "next": "decision-1"
      },
      {
        "id": "decision-1",
        "type": "choice",
        "title": "Open the conversation",
        "body": "How do you make first contact?",
        "choices": [
          {
            "label": "Send a private, non-judgmental invitation",
            "next": "consequence-1-a"
          },
          {
            "label": "Ask for an explanation in the group",
            "next": "consequence-1-b"
          }
        ]
      },
      {
        "id": "consequence-1-a",
        "type": "auto",
        "title": "What happens next / decision 1",
        "body": "The learner can choose whether and how to respond. You explain what support is available without making assumptions.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-1"
      },
      {
        "id": "consequence-1-b",
        "type": "auto",
        "title": "What happens next / decision 1",
        "body": "The learner receives attention they did not request. You will need to move the conversation to a private channel and acknowledge that choice.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-1"
      },
      {
        "id": "reflection-1",
        "type": "continue",
        "title": "Pause and reflect / 1",
        "body": "Notice what your decision made possible and what it left unresolved.",
        "prompt": "Why did you choose this route?",
        "button": "Make the next decision",
        "next": "decision-2"
      },
      {
        "id": "decision-2",
        "type": "choice",
        "title": "Listen before planning",
        "body": "The learner says the workload feels difficult. What next?",
        "choices": [
          {
            "label": "Ask which part is hardest to access",
            "next": "consequence-2-a"
          },
          {
            "label": "Offer your usual solution immediately",
            "next": "consequence-2-b"
          }
        ]
      },
      {
        "id": "consequence-2-a",
        "type": "auto",
        "title": "What happens next / decision 2",
        "body": "They describe a specific barrier. You can discuss adjustments to the activity rather than guessing at the cause.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-2"
      },
      {
        "id": "consequence-2-b",
        "type": "auto",
        "title": "What happens next / decision 2",
        "body": "Your suggestion may help, but you have not checked the barrier. You pause and ask whether it fits their situation.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-2"
      },
      {
        "id": "reflection-2",
        "type": "continue",
        "title": "Pause and reflect / 2",
        "body": "Notice what your decision made possible and what it left unresolved.",
        "prompt": "Why did you choose this route?",
        "button": "Make the next decision",
        "next": "decision-3"
      },
      {
        "id": "decision-3",
        "type": "choice",
        "title": "Agree a next step",
        "body": "How will the conversation finish?",
        "choices": [
          {
            "label": "Agree one achievable step and a check-in",
            "next": "consequence-3-a"
          },
          {
            "label": "Leave the plan open-ended",
            "next": "consequence-3-b"
          }
        ]
      },
      {
        "id": "consequence-3-a",
        "type": "auto",
        "title": "What happens next / decision 3",
        "body": "The learner chooses a manageable action. You both know when to check whether the arrangement helped.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-3"
      },
      {
        "id": "consequence-3-b",
        "type": "auto",
        "title": "What happens next / decision 3",
        "body": "There is room for flexibility, but no shared next action. You offer to agree a smaller, clearer step when the learner is ready.",
        "delayMs": 1800,
        "button": "Consider the next step",
        "next": "reflection-3"
      },
      {
        "id": "reflection-3",
        "type": "continue",
        "title": "Pause and reflect / 3",
        "body": "Notice what your decision made possible and what it left unresolved.",
        "prompt": "Why did you choose this route?",
        "button": "Review the outcome",
        "next": "outcome"
      },
      {
        "id": "outcome",
        "type": "ending",
        "title": "Your route, your explanation",
        "body": "Reflect on privacy, listening and learner agency. This is a practice conversation, not clinical advice or a substitute for your organisation's support procedures.",
        "prompt": "What would you keep or change next time?"
      }
    ]
  },
  {
    "version": 1,
    "id": "team-conversation",
    "title": "The meeting before the deadline",
    "intro": "Learning goal: practise evidence-based, respectful disagreement under pressure. For individual or group use. Before each choice, note your instinct; after an outcome, compare it with another route.",
    "start": "arrival",
    "nodes": [
      {
        "id": "arrival",
        "type": "continue",
        "title": "Ten minutes before the review",
        "body": "You coordinate a small project team. Sam has found an accessibility barrier in the prototype. Alex says there is no time to change anything. Your role is to agree a credible next step without hiding the barrier.",
        "next": "opening",
        "button": "Join the meeting"
      },
      {
        "id": "opening",
        "type": "choice",
        "title": "How do you open the discussion?",
        "body": "Alex interrupts Sam: \"We already agreed this design.\" The room goes quiet.",
        "prompt": "Write your first instinct before choosing.",
        "choices": [
          {
            "label": "Make space for Sam to demonstrate the barrier",
            "next": "demonstration"
          },
          {
            "label": "Take the disagreement out of the meeting",
            "next": "private-talk"
          }
        ]
      },
      {
        "id": "demonstration",
        "type": "auto",
        "title": "A barrier everyone can see",
        "body": "Sam shows that the keyboard cannot reach the final action. Alex acknowledges the problem but worries that a large change would break other screens.",
        "delayMs": 1800,
        "next": "scope"
      },
      {
        "id": "scope",
        "type": "choice",
        "title": "What change will you propose?",
        "body": "The team can test a narrow fix today, or postpone this interaction and explain why.",
        "choices": [
          {
            "label": "Try a narrow keyboard fix with a test",
            "next": "trial"
          },
          {
            "label": "Remove the interaction from this release",
            "next": "alternative"
          }
        ]
      },
      {
        "id": "trial",
        "type": "auto",
        "title": "The first test is promising",
        "body": "The final action is reachable. Sam asks to check focus visibility and the order of controls before declaring the whole interaction accessible.",
        "delayMs": 1800,
        "next": "verification"
      },
      {
        "id": "verification",
        "type": "choice",
        "title": "What counts as ready?",
        "body": "You have time for one more focused check before the review.",
        "choices": [
          {
            "label": "Run the check and describe the limits honestly",
            "next": "test-notes"
          },
          {
            "label": "Call the interaction fully accessible now",
            "next": "overclaim"
          }
        ]
      },
      {
        "id": "test-notes",
        "type": "continue",
        "title": "A clear record",
        "body": "The focused check finds one confusing focus indicator. You fix it and record what was tested, what was not, and who will review next.",
        "prompt": "What evidence supports your recommendation?",
        "next": "review-choice"
      },
      {
        "id": "review-choice",
        "type": "choice",
        "title": "Lead the review",
        "body": "The reviewer asks why the design changed so late.",
        "choices": [
          {
            "label": "Explain the barrier, fix, checks and remaining limits",
            "next": "shared-plan"
          },
          {
            "label": "Describe the change as cosmetic",
            "next": "overclaim"
          }
        ]
      },
      {
        "id": "alternative",
        "type": "continue",
        "title": "A smaller release",
        "body": "The team can offer the same learning content as a straightforward reading activity. It loses the interaction but avoids publishing a known keyboard barrier.",
        "next": "alternative-check"
      },
      {
        "id": "alternative-check",
        "type": "choice",
        "title": "Check the replacement",
        "body": "The replacement needs a clear purpose and a quick access check too.",
        "choices": [
          {
            "label": "Test the replacement and record the deferred feature",
            "next": "scoped-release"
          },
          {
            "label": "Assume simple content needs no checking",
            "next": "unchecked"
          }
        ]
      },
      {
        "id": "private-talk",
        "type": "continue",
        "title": "The conversation becomes quieter",
        "body": "Alex is less defensive in private. Sam is no longer present to demonstrate the issue. You still need evidence, not a decision based only on who speaks most confidently.",
        "next": "private-choice"
      },
      {
        "id": "private-choice",
        "type": "choice",
        "title": "Rebuild a shared view",
        "body": "How will you bring the concern back into the plan?",
        "choices": [
          {
            "label": "Invite Sam to show the barrier with the whole team",
            "next": "demonstration"
          },
          {
            "label": "Let Alex decide whether the concern matters",
            "next": "deferred-voice"
          }
        ]
      },
      {
        "id": "deferred-voice",
        "type": "auto",
        "title": "The original plan continues",
        "body": "The concern is treated as a preference rather than an access barrier. Sam sends a written example so it is not lost.",
        "delayMs": 1800,
        "next": "last-chance"
      },
      {
        "id": "last-chance",
        "type": "choice",
        "title": "The written example arrives",
        "body": "The review has not begun. There is still time to make the issue visible.",
        "choices": [
          {
            "label": "Return to the evidence and agree a limited response",
            "next": "scope"
          },
          {
            "label": "Leave the issue out of the review",
            "next": "unchecked"
          }
        ]
      },
      {
        "id": "shared-plan",
        "type": "ending",
        "title": "Outcome / a shared, evidence-led plan",
        "body": "The team can explain its decisions and remaining uncertainty. Sam and Alex both have clear next actions. Debrief: which choice helped the team disagree constructively?",
        "prompt": "What would you transfer to a real meeting?"
      },
      {
        "id": "scoped-release",
        "type": "ending",
        "title": "Outcome / a deliberate smaller release",
        "body": "The team releases a checked alternative and names the deferred interaction. This is a different strategy, not an automatic failure. Debrief: what learning value was retained, and what was lost?",
        "prompt": "When would a smaller release be appropriate?"
      },
      {
        "id": "overclaim",
        "type": "ending",
        "title": "Outcome / confidence beyond the evidence",
        "body": "The review receives a stronger claim than the tests support. The next task is to correct that claim and agree further checks. Debrief: what would an honest description have said?",
        "prompt": "Rewrite the claim using only the evidence you have."
      },
      {
        "id": "unchecked",
        "type": "ending",
        "title": "Outcome / an unresolved barrier",
        "body": "The plan goes forward without a clear check or visible record of the issue. A learner may still be blocked. Debrief: identify an earlier opportunity to change this route.",
        "prompt": "Which earlier decision would you revisit, and why?"
      }
    ]
  }
];
