# matching  (contrib — source not in this checkout)

Fetched at `adapt install`; documented here from a course example only.

## Live example (from this course)

```json
{
  "_id": "L03-c-42",
  "_parentId": "L03-b-42",
  "_type": "component",
  "_component": "matching",
  "_classes": "slot__L03__check knowledge-check-question",
  "_layout": "full",
  "title": "Formative check: formative or summative",
  "displayTitle": "Sort each of these assessments by whether it is formative or summative.",
  "body": "",
  "instruction": "Choose Formative or Summative for each one, then select Submit.",
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": true
  },
  "ariaQuestion": "Sort each assessment into formative or summative.",
  "_attempts": 2,
  "_shouldDisplayAttempts": true,
  "_questionWeight": 1,
  "_hasItemScoring": false,
  "_canShowModelAnswer": true,
  "_canShowCorrectness": false,
  "_canShowFeedback": true,
  "_canShowMarking": true,
  "_recordInteraction": true,
  "_shouldResetAllAnswers": true,
  "_isRandom": false,
  "_isRandomQuestionOrder": false,
  "_allowOnlyUniqueAnswers": false,
  "placeholder": "Select formative or summative",
  "_isPartOfAssessment": false,
  "_items": [
    {
      "text": "A practice essay your tutor comments on but does not mark",
      "_options": [
        {
          "text": "Formative",
          "_isCorrect": true,
          "_score": 1
        },
        {
          "text": "Summative",
          "_isCorrect": false,
          "_score": 0
        }
      ]
    },
    {
      "text": "A short quiz during term that does not count toward your grade",
      "_options": [
        {
          "text": "Formative",
          "_isCorrect": true,
          "_score": 1
        },
        {
          "text": "Summative",
          "_isCorrect": false,
          "_score": 0
        }
      ]
    },
    {
      "text": "The end-of-module examination",
      "_options": [
        {
          "text": "Formative",
          "_isCorrect": false,
          "_score": 0
        },
        {
          "text": "Summative",
          "_isCorrect": true,
          "_score": 1
        }
      ]
    },
    {
      "text": "The final coursework essay that sets your module grade",
      "_options": [
        {
          "text": "Formative",
          "_isCorrect": false,
          "_score": 0
        },
        {
          "text": "Summative",
          "_isCorrect": true,
          "_score": 1
        }
      ]
    }
  ],
  "_feedback": {
    "title": "",
    "correct": "That's right. Formative assessment is there to help you improve and does not count toward your grade; summative assessment is the task that sets it.",
    "_incorrect": {
      "notFinal": "Not quite. For each one, ask: does this count toward my final grade, or is it there to help me improve first?",
      "final": "The practice essay and the term quiz are formative: they help you improve and do not count. The examination and the final coursework essay are summative: they set your grade. The test is simple - does it count toward the mark, or help you reach it?"
    },
    "_partlyCorrect": {
      "notFinal": "Some of those are right, but not all. Check each one against the question: does it count, or help you improve first?",
      "final": "Formative tasks (the practice essay, the term quiz) help you improve and do not count; summative tasks (the examination, the final coursework essay) set your grade."
    }
  }
}
```
