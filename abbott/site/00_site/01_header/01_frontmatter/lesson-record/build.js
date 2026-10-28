/* build.js
   Makes the view model the template expects and renders lesson-record.example.html.
     npm install handlebars
     node build.js [sample.json] [out.html]
   In grow-ct the same view model is what growMeta.js would hand to the partial.
   Nothing here is needed at runtime: the template itself is plain Handlebars. */
const fs = require('fs');
const path = require('path');
const Handlebars = require('handlebars');

const dir = __dirname;
const input = path.resolve(process.argv[2] || path.join(dir, 'lesson-record.sample.json'));
const output = path.resolve(process.argv[3] || path.join(dir, 'lesson-record.example.html'));
const { record, course } = JSON.parse(fs.readFileSync(input, 'utf8'));

const served = new Set((record.alignment || {}).course_outcome_ids || []);
const n = (a) => (a || []).length;

const vm = Object.assign({}, record, {
  course: Object.assign({}, course, {
    outcomes: (course.outcomes || []).map((o) => Object.assign({ aligned: served.has(o.id) }, o))
  }),
  position: `Lesson ${record.sequence}${course.lesson_count ? ' of ' + course.lesson_count : ''}`,
  summaries: {
    inherited: `${course.language}, ${course.learner_pitch} pitch`,
    scope: (record.scope || {}).focus || '',
    co: `${served.size} of ${n(course.outcomes)} served by this lesson`,
    lo: `${n(record.learning_outcomes)} lesson outcomes`,
    act: `${n(record.activities)} activities`,
    assessment: `${(record.assessment || {}).purpose || 'none'}, covers ${n((record.assessment || {}).lesson_outcome_ids)} outcomes`,
    prereq: record.estimated_duration_minutes ? `${record.estimated_duration_minutes} minutes` : 'No duration set',
    lifecycle: `v${record.version}, ${record.status}, owned by ${record.owner}`,
    review: `Academic review ${(record.review || {}).academic_status || 'pending'}`,
    opening: (record.frontmatter || {}).eyebrow || 'Before you begin'
  }
});

const template = Handlebars.compile(fs.readFileSync(path.join(dir, 'lesson-record.hbs'), 'utf8'));
const body = template(vm);

const page = `<!doctype html>
<html lang="${record.language || 'en-GB'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${Handlebars.escapeExpression(record.title)} · lesson record</title>
<link rel="stylesheet" href="lesson-record.skin.css">
<link rel="stylesheet" href="lesson-record.inspect.css">
</head>
<body>
${body}
<script src="lesson-record.inspect.js"></script>
</body>
</html>
`;
fs.writeFileSync(output, page);
console.log('wrote', output);
