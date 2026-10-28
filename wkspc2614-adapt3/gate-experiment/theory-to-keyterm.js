#!/usr/bin/env node
// EXPERIMENT — knowledge->component generator: ingested THEORY docs -> reusable
// "glossary objects" -> keyTerm component data objects. Faithful extraction:
// term = title, relatedTerms = aliases, definition = the doc's own "0.1 Agent
// definition", extendedDefinition = "0.2 Summary". No fabrication. Not wired in.
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..');
const DIR = path.join(ROOT, 'source-kb/canon-adp/secondary-data/ingested/theory');

function parse(file) {
  const t = fs.readFileSync(file, 'utf8').replace(/\r/g, ''); // files are CRLF
  const fm = (t.match(/^---\n([\s\S]*?)\n---/) || [, ''])[1];
  const body = t.replace(/^---\n[\s\S]*?\n---/, '');
  const line = re => ((fm.match(re) || [])[1] || '').trim().replace(/^["']|["']$/g, '');
  const title = line(/^title:\s*(.+)$/m);
  const subjectKind = line(/^subjectKind:\s*(.+)$/m);
  const aliases = ((fm.match(/^aliases:\s*\[([^\]]*)\]/m) || [, ''])[1] || '')
    .split(',').map(s => s.trim()).filter(Boolean);
  const section = heading => {
    const re = new RegExp('###\\s*' + heading + '[^\\n]*\\n([\\s\\S]*?)(?=\\n#{2,3}\\s|$)');
    const m = body.match(re);
    if (!m) return '';
    return m[1].split('\n')
      .filter(l => l.trim() && !l.trim().startsWith('<!--') && !l.trim().startsWith('```') && !l.trim().startsWith('|'))
      .join(' ').replace(/\s+/g, ' ').trim();
  };
  return { id: path.basename(file, '.md'), title, subjectKind, aliases,
    definition: section('0\\.1 Agent definition'), extendedDefinition: section('0\\.2 Summary') };
}

// glossary object = the reusable term record (scoped later per page/course/pathway)
const toGlossaryObject = p => ({
  id: p.id, term: p.term, kind: p.subjectKind || 'concept',
  aliases: p.aliases, definition: p.definition, extendedDefinition: p.extendedDefinition,
  source: 'source-kb/.../ingested/theory/' + p.id + '.md'
});
// keyTerm component data object, from a glossary object
const toKeyTerm = g => ({
  _component: 'keyTerm', _id: 'kt-' + g.id.replace(/[^a-z0-9]+/gi, '-').slice(0, 24), _classes: '', _layout: 'full',
  _reveal: true,
  term: g.term,
  _partOfSpeech: g.kind,
  definition: g.definition,
  extendedDefinition: g.extendedDefinition ? '<p>' + g.extendedDefinition + '</p>' : '',
  _relatedTerms: g.aliases.filter(a => a.toLowerCase() !== g.term.toLowerCase()).slice(0, 6)
});

const files = fs.readdirSync(DIR).filter(f => f.endsWith('.md'));
const objects = [];
for (const f of files) {
  const p = parse(path.join(DIR, f));
  if (!p.title || !p.definition) continue;          // only docs with a usable definition
  p.term = (p.aliases[0] && p.aliases[0].length < p.title.length ? cap(p.aliases[0]) : p.title);
  objects.push(toGlossaryObject(p));
}
function cap(s) { return s ? s[0].toUpperCase() + s.slice(1) : s; }

const glossary = { glossaryVersion: '0.1-experiment', scope: 'theory-corpus', count: objects.length, objects };
fs.writeFileSync(path.join(__dirname, 'glossary-objects.json'), JSON.stringify(glossary, null, 2) + '\n');
const keyTerms = objects.slice(0, 3).map(toKeyTerm);
fs.writeFileSync(path.join(__dirname, 'keyterm-samples.json'), JSON.stringify(keyTerms, null, 2) + '\n');

console.log('theory docs scanned:', files.length, '| glossary objects extracted:', objects.length);
console.log('\n=== sample glossary objects ===');
objects.slice(0, 3).forEach(o => console.log('\n• ' + o.term + '  [' + o.kind + ']\n   aliases: ' + o.aliases.join(', ') + '\n   def: ' + (o.definition || '').slice(0, 160) + '...'));
console.log('\nwrote gate-experiment/glossary-objects.json (' + objects.length + ') + keyterm-samples.json (3)');
