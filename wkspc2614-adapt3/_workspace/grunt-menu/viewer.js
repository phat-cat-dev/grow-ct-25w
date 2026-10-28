#!/usr/bin/env node
/**
 * viewer.js — control panel for a Node + Grunt project's build / preview /
 * git workflow.
 *
 * A dependency-free (Node built-ins only) launcher that both EXPLAINS and RUNS
 * the common commands, organised into panels, each command carrying a short
 * patterned alias. When you pick a command that takes a target or flags, a small
 * builder walks you through completing it (choose a project, toggle flags,
 * preview, run).
 *
 *   npm run viewer                open the menu
 *   node <this file> <alias|key>  run one command, e.g. `… viewer.js bb`
 *   node <this file> cr psychology  run with its argument(s)
 *   node <this file> aliases      print the alias reference (+ shell snippet)
 *   node <this file> describe bb  print what a command is and what it runs
 *
 * ALIAS PATTERN — two letters: <panel><action>.
 *   b* = Build & preview  c* = Course workflow  n* = npm  s* = scripts  g* = git
 * So `bb` build, `bd` dev, `cs` status, `cr` rebuild, `ne` export, `gs` status.
 *
 * MODULAR: everything is data in GROUPS below — add a command by adding one
 * entry (give it an alias, a base shell command OR an fn, and optional
 * pick/flags). The menu, numbering, alias dispatch and builder all read from it.
 *
 * SELF-DESCRIBING: every item can report what it does. A curated one-line
 * `desc` shows in the panel; `describe` (menu action `d`) prints the fuller
 * story, read from the HEADER COMMENT of whatever file the command actually
 * runs — a .sh script's leading `#` block, or a .js file's leading jsdoc-style
 * block. Document a script in its own header and the menu picks it up, with
 * nothing to restate here. Shell scripts under SCRIPT_DIRS are discovered on
 * disk the same way, so dropping in a documented .sh adds a menu entry.
 *
 * PORTABLE: no path, project name or course assumption is hardcoded. The repo
 * root is found by walking up to the nearest Gruntfile.js, every command runs
 * from there, and panels whose backing files are absent are dropped. Copy this
 * one file into any Node/Grunt project; the course-workflow panel disappears
 * where there is no courses/ directory, and the build, npm, scripts and git
 * panels keep working.
 */

'use strict';

const fs = require('fs');
const path = require('path');
const readline = require('readline');
const { spawnSync } = require('child_process');

// --- locate the Adapt repo root (dir containing Gruntfile.js) ---
function findRoot(start) {
  let dir = start;
  for (let i = 0; i < 10; i++) {
    if (fs.existsSync(path.join(dir, 'Gruntfile.js'))) return dir;
    const up = path.dirname(dir);
    if (up === dir) break;
    dir = up;
  }
  return start;
}
const ROOT = findRoot(fs.existsSync(path.join(process.cwd(), 'Gruntfile.js')) ? process.cwd() : __dirname);
const COURSES = path.join(ROOT, 'courses');
const GENERATED = path.join(COURSES, '_generated');
const PACKS = path.join(ROOT, 'content', 'context-packs');
const LINK = path.join(ROOT, 'src', 'course');

// How this file is reached from the repo root, so printed usage and the shell
// alias snippet stay correct wherever the file is moved to.
const SELF_REL = path.relative(ROOT, __filename).split(path.sep).join('/');

// Dev-server port, freed before a serve command rather than letting the server
// fail on an address already in use. Grunt's connect config decides the real
// one; --port overrides both.
const PORT = 9001;

// Directories scanned for runnable, self-documenting *.sh scripts. Missing
// directories are skipped, so this list is safe in any project.
const SCRIPT_DIRS = ['_workspace/scripts-sa', 'scripts', 'bin'];

const exists = p => { try { return fs.existsSync(p); } catch { return false; } };

function pkgScripts() {
  try { return JSON.parse(fs.readFileSync(path.join(ROOT, 'package.json'), 'utf8')).scripts || {}; }
  catch { return {}; }
}

// --- self-description: read a file's leading header comment ---------------
// Returns { summary, body }: the first sentence-ish line, and the whole block.
// Understands a shell `#` block (after any shebang) and a JS /** */ block, the
// two conventions these projects use. No header is not an error; it just means
// a command can only describe itself by the command line it runs.
function headerDoc(file) {
  let src;
  try { src = fs.readFileSync(file, 'utf8'); } catch { return null; }
  const lines = src.split(/\r?\n/);
  let i = 0;
  if (lines[0] && lines[0].startsWith('#!')) i = 1;
  while (lines[i] !== undefined && lines[i].trim() === '') i++;

  const out = [];
  if (lines[i] && lines[i].trim().startsWith('/*')) {
    for (; i < lines.length; i++) {
      const raw = lines[i];
      if (/^\s*\/\*+\s*$/.test(raw)) continue;
      if (raw.includes('*/')) break;
      out.push(raw.replace(/^\s*\/?\*+ ?/, '').trimEnd());
    }
  } else {
    for (; i < lines.length; i++) {
      const raw = lines[i];
      if (!/^\s*#/.test(raw)) break;
      out.push(raw.replace(/^\s*#+ ?/, '').trimEnd());
    }
  }
  while (out.length && out[0].trim() === '') out.shift();
  while (out.length && out[out.length - 1].trim() === '') out.pop();
  if (!out.length) return null;

  // Drop a leading "name.sh — " / "name.js - " restatement from the summary.
  const summary = out[0].replace(/^[\w.-]+\.(?:sh|js|mjs|cjs)\s*[—-]\s*/, '').trim();
  return { summary, body: out.join('\n') };
}

// Which file does a command line actually run? Used to pull that file's header
// as the command's long description. Follows one `npm run <script>` hop.
function cmdTargetFile(base) {
  if (!base) return null;
  let cmd = base;
  const viaNpm = cmd.match(/^npm run ([\w:.-]+)/);
  if (viaNpm) {
    const script = pkgScripts()[viaNpm[1]];
    if (!script) return null;
    cmd = script;
  }
  const node = cmd.match(/node\s+(?:[^\s]*\/)?([^\s]+\.(?:js|mjs|cjs))/);
  if (node) {
    const direct = cmd.match(/node\s+([^\s]+\.(?:js|mjs|cjs))/);
    const p = path.resolve(ROOT, direct[1]);
    return exists(p) ? p : null;
  }
  const shell = cmd.match(/(\.?\/?[\w./-]+\.sh)/);
  if (shell) {
    const p = path.resolve(ROOT, shell[1]);
    return exists(p) ? p : null;
  }
  return null;
}

// --- colours ---
const c = { dim: s => `\x1b[2m${s}\x1b[0m`, bold: s => `\x1b[1m${s}\x1b[0m`,
            cyan: s => `\x1b[36m${s}\x1b[0m`, green: s => `\x1b[32m${s}\x1b[0m`,
            yellow: s => `\x1b[33m${s}\x1b[0m`, red: s => `\x1b[31m${s}\x1b[0m` };

// --- live discovery ---
function dirs(p) {
  try { return fs.readdirSync(p, { withFileTypes: true }).filter(d => d.isDirectory()).map(d => d.name).sort(); }
  catch { return []; }
}
const baseCourses = () => dirs(COURSES).filter(n => n !== '_generated');
const generated = () => dirs(GENERATED);
const packs = () => dirs(PACKS);

function currentTarget() {
  try {
    const l = fs.lstatSync(LINK);
    if (l.isSymbolicLink()) {
      const t = fs.readlinkSync(LINK);
      const resolved = path.resolve(path.dirname(LINK), t);
      return { kind: 'symlink', target: t, resolved, exists: fs.existsSync(resolved) };
    }
    if (l.isDirectory()) return { kind: 'directory (real copy)', target: LINK, resolved: LINK, exists: true };
    return { kind: 'file', target: LINK, resolved: LINK, exists: true };
  } catch { return { kind: 'MISSING', target: null, resolved: null, exists: false }; }
}

// --- run a shell command from repo root, streaming output ---
function sh(cmd) {
  console.log(c.dim(`\n$ ${cmd}\n`));
  const r = spawnSync(cmd, { cwd: ROOT, stdio: 'inherit', shell: true });
  if (r.status !== 0) console.log(c.yellow(`\n(exited with code ${r.status})`));
  return r.status === 0;
}

// --- free the dev-server port -------------------------------------------
// A serve command fails outright if an earlier server still holds the port, so
// the serve items free it first. SIGTERM, then SIGKILL only for what ignores
// it. Needs lsof or fuser; where neither exists this is a no-op and grunt
// reports the clash itself.
function portPids(port) {
  const probe = spawnSync(
    `lsof -ti tcp:${port} 2>/dev/null || fuser -n tcp ${port} 2>/dev/null`,
    { cwd: ROOT, shell: true, encoding: 'utf8' }
  );
  return String(probe.stdout || '').trim().split(/\s+/).filter(Boolean);
}
function freePort(port) {
  const pids = portPids(port);
  if (!pids.length) return;
  console.log(c.yellow(`\n  port ${port} is held by ${pids.join(', ')} — freeing it first`));
  spawnSync(`kill ${pids.join(' ')}`, { cwd: ROOT, shell: true });
  spawnSync('sleep 1', { shell: true });
  const left = portPids(port);
  if (left.length) {
    console.log(c.yellow(`  ${left.join(', ')} ignored SIGTERM — sending SIGKILL`));
    spawnSync(`kill -9 ${left.join(' ')}`, { cwd: ROOT, shell: true });
  }
  console.log(c.green(`  port ${port} free.`));
}

// --- repoint src/course at a path under courses/ ---
function relink(subPathUnderCourses) {
  try { fs.rmSync(LINK, { recursive: true, force: true }); } catch {}
  const rel = path.posix.join('..', 'courses', subPathUnderCourses);
  try { fs.symlinkSync(rel, LINK); console.log(c.green(`\n✓ src/course → ${rel}`)); }
  catch (e) {
    console.log(c.red(`\n✗ could not create symlink (${e.code}). On Windows enable it with:`));
    console.log('   git config --global core.symlinks true   (Dev-Mode / admin shell), or build under WSL.');
  }
}
function mergeAndLink(tier, context) {
  const ok = sh(`node merge-context.js --context=${context} --tier=${tier}`);
  if (ok) relink(`_generated/${tier}-${context}`);
  return ok;
}
const soleTier = () => (baseCourses().length === 1 ? baseCourses()[0] : null);

// --- prompt helpers ---
let rl;
function ensureRl() { if (!rl) rl = readline.createInterface({ input: process.stdin, output: process.stdout }); return rl; }
const ask = q => new Promise(res => ensureRl().question(q, a => res(a.trim())));
async function pick(title, items) {
  if (!items.length) { console.log(c.yellow(`\n(none found: ${title})`)); return null; }
  console.log(`\n${c.bold(title)}`);
  items.forEach((it, i) => console.log(`  ${c.cyan(String(i + 1))}) ${it}`));
  const a = await ask('  choose a number (blank to cancel): ');
  const n = parseInt(a, 10);
  return (n >= 1 && n <= items.length) ? items[n - 1] : null;
}
// toggle a flag list + free-text extras, return a string to append
async function chooseFlags(flags) {
  let chosen = [];
  if (flags && flags.length) {
    console.log(`\n${c.bold('Useful flags')} ${c.dim('(comma-separated numbers, blank for none)')}:`);
    flags.forEach((f, i) => console.log(`  ${c.cyan(String(i + 1))}) ${f.f.padEnd(12)} ${c.dim(f.d)}`));
    const a = await ask('  flags: ');
    chosen = a.split(/[,\s]+/).map(x => parseInt(x, 10)).filter(n => n >= 1 && n <= flags.length).map(n => flags[n - 1].f);
  }
  const custom = await ask('  extra flags (free text, blank for none): ');
  return [...chosen, custom.trim()].filter(Boolean).join(' ');
}
// the builder for a plain shell command: optional project pick, optional flags, preview, run
async function runBase(item, args) {
  let cmd = item.base;
  if (item.freePort) freePort(item.freePort);
  if (args && args.length) { sh(cmd + ' ' + args.join(' ')); return; }   // non-interactive: append args as-is
  if (!item.pick && !(item.flags && item.flags.length)) { sh(cmd); return; }   // nothing to build → run directly (no prompt)
  if (item.pick) {
    const list = item.pick === 'context' ? packs() : item.pick === 'course' ? baseCourses() : [...baseCourses().map(n => 'courses/' + n), ...generated().map(n => '_generated/' + n)];
    const sel = await pick(`${c.bold('Projects available')} (${item.pick}):`, list);
    if (!sel) return console.log(c.yellow('  cancelled.'));
    cmd += ' ' + (item.pickPrefix || '') + sel;
  }
  const extra = await chooseFlags(item.flags);
  if (extra) cmd += ' ' + extra;
  const a = await ask(`\n  run  ${c.green(cmd)}  ? [Y/n] `);
  if (a === '' || /^y/i.test(a)) sh(cmd);
  else console.log(c.yellow('  cancelled.'));
}

// =============================================================================
// PANELS — each item: { alias, name, desc, base|fn, pick?, flags?, freePort?,
// when? }. PANELS is the declaration; GROUPS below is what survives pruning in
// the project it finds itself in (see itemAvailable).
// =============================================================================
const PANELS = [
  { title: 'Build & preview', items: [
    { alias: 'bb', name: 'Build', desc: 'production build into build/ (writes imsmanifest.xml)',
      base: 'npx grunt build', flags: [{ f: '--force', d: 'build a partly-authored shell past check-json' }] },
    { alias: 'bd', name: 'Dev + watch', desc: 'developer build (source maps) + rebuild on save', base: 'npx grunt dev' },
    { alias: 'bs', name: 'Serve', desc: `serve build/ in a browser (frees :${PORT} first)`, base: 'npx grunt server', freePort: PORT },
    { alias: 'bx', name: 'Serve (SCORM)', desc: `serve inside a dummy SCORM harness, to test completion (frees :${PORT} first)`, base: 'npx grunt server-scorm', freePort: PORT },
    { alias: 'bw', name: 'Build + serve', desc: `build then serve in one step (frees :${PORT} first)`, base: 'npx grunt server-build', freePort: PORT },
  ]},
  { title: 'Course workflow', when: () => exists(COURSES), items: [
    { alias: 'cs', name: 'Status', desc: 'which course the build points at, and whether it resolves', fn: cmdStatus },
    { alias: 'cl', name: 'List', desc: 'base courses / generated variants / context packs', fn: cmdList },
    { alias: 'ck', name: 'Link', desc: 'point the build at an existing course (base or generated)', fn: cmdLink },
    { alias: 'cg', name: 'Generate', desc: 'merge a base course + a context pack into a fresh course + link it', fn: cmdGenerate },
    { alias: 'cr', name: 'Rebuild', desc: 'one shot: merge a context → link → grunt build', fn: cmdRebuild },
    { alias: 'cz', name: 'Package SCORM', desc: 'zip build/ into a SCORM package for Moodle', base: 'node package-scorm.js' },
    { alias: 'cf', name: 'References worksheet', desc: 'export every Sources block to an editable link worksheet (import writes links back)', fn: cmdReferences },
  ]},
  { title: 'npm scripts', items: [
    { alias: 'ne', name: 'course-export', desc: 'export the whole course bundle (md/html/yaml/templates)', base: 'npm run course-export' },
    { alias: 'ni', name: 'course-script-import', desc: 'rebuild a course from an edited export script', base: 'npm run course-script-import' },
    { alias: 'nm', name: 'component-map', desc: 'component × palette × patterns map', base: 'npm run component-map' },
    { alias: 'nr', name: 'component-reference', desc: 'per-component learning docs', base: 'npm run component-reference' },
    { alias: 'np', name: 'pk-bundle', desc: 'bundle project-knowledge', base: 'npm run pk-bundle' },
    { alias: 'na', name: 'adapt-install', desc: 'install extensions + reapply vendor patches (never raw adapt install)', base: 'npm run adapt-install' },
    { alias: 'nl', name: 'lint', desc: 'run eslint over the repo', base: 'npm run lint' },
    { alias: 'nt', name: 'test', desc: 'run the test suite', base: 'npm run test' },
    { alias: 'nc', name: 'theme-css dump', desc: 'compile each theme LESS to exports/theme-css/ to read the produced CSS + raw-hex candidates', base: 'npm run theme-css' },
    { alias: 'nx', name: 'other npm scripts', desc: 'pick from every remaining script in package.json', fn: cmdNpmOther },
  ]},
  { title: 'git', items: [
    { alias: 'gs', name: 'Status', desc: 'branch, ahead/behind, and what is changed but uncommitted', base: 'git -c color.ui=always status --short --branch' },
    { alias: 'gd', name: 'Diff', desc: 'unstaged changes, then staged, with no pager', base: 'git --no-pager -c color.ui=always diff --stat && git --no-pager -c color.ui=always diff --stat --staged' },
    { alias: 'gl', name: 'Log', desc: 'last 15 commits, one line each', base: 'git --no-pager -c color.ui=always log --oneline --decorate -15' },
    { alias: 'gc', name: 'Commit', desc: 'stage chosen files and commit with a message you type (never auto-generated)', fn: cmdCommit },
    { alias: 'gu', name: 'Sync', desc: 'fetch origin and merge this branch: never force, never rebase, stop on conflict', fn: cmdSync },
    { alias: 'gp', name: 'Push', desc: 'push this branch to origin, behind a typed confirmation', fn: cmdPush },
  ]},
];

// --- which declared items apply to the project this file is sitting in ----
const npmScriptOf = base => { const m = (base || '').match(/^npm run ([\w:.-]+)/); return m ? m[1] : null; };
const namesAFile = base => /[\w./-]+\.(?:js|mjs|cjs|sh)\b/.test(base || '');
function itemAvailable(it) {
  if (it.when && !it.when()) return false;
  const script = npmScriptOf(it.base);
  if (script) return Boolean(pkgScripts()[script]);          // npm item: only if package.json has it
  if (namesAFile(it.base) && !cmdTargetFile(it.base)) return false;  // names a file that is not there
  return true;
}

// --- shell scripts discovered on disk, described by their own headers -----
// Each *.sh under SCRIPT_DIRS becomes an item. Alias is `s` + the first letter
// of its name that is still free, so adding a script needs no edit here.
function scriptItems(usedAliases) {
  const items = [];
  for (const rel of SCRIPT_DIRS) {
    let names;
    try {
      names = fs.readdirSync(path.join(ROOT, rel)).filter(f => f.endsWith('.sh')).sort();
    } catch { continue; }
    for (const file of names) {
      const abs = path.join(ROOT, rel, file);
      const stem = file.replace(/\.sh$/, '');
      const doc = headerDoc(abs);
      let alias = null;
      for (const ch of stem.replace(/[^a-z]/gi, '').toLowerCase() + '123456789') {
        if (!usedAliases.has('s' + ch)) { alias = 's' + ch; break; }
      }
      if (!alias) continue;
      usedAliases.add(alias);
      items.push({
        alias, name: stem,
        desc: (doc && doc.summary) || `run ${rel}/${file}`,
        base: `./${rel}/${file}`
      });
    }
  }
  return items;
}

const GROUPS = (() => {
  const panels = PANELS
    .filter(g => !g.when || g.when())
    .map(g => ({ title: g.title, items: g.items.filter(itemAvailable) }))
    .filter(g => g.items.length);
  const used = new Set(panels.flatMap(g => g.items.map(it => it.alias)));
  const scripts = scriptItems(used);
  if (scripts.length) panels.push({ title: 'scripts', items: scripts });
  // git last: it is the panel you reach for after the others have run.
  const gitIdx = panels.findIndex(g => g.title === 'git');
  if (gitIdx > -1) panels.push(panels.splice(gitIdx, 1)[0]);
  return panels;
})();

const ALL = GROUPS.flatMap(g => g.items);
const byAlias = Object.fromEntries(ALL.map(it => [it.alias, it]));

// --- course-workflow command implementations ---
async function cmdStatus() {
  const t = currentTarget();
  console.log(`\n  build target (src/course): ${c.bold(t.kind)}`);
  if (t.target) console.log(`  → ${t.target}`);
  if (t.resolved && t.kind === 'symlink')
    console.log(`  resolves to: ${t.resolved}  ${t.exists ? c.green('[exists]') : c.red('[MISSING — generate it or relink]')}`);
}
async function cmdList() {
  console.log(`\n  ${c.bold('Base courses')} ${c.dim('(source of truth — edit here)')}:`);
  baseCourses().forEach(n => console.log('   • ' + n));
  console.log(`\n  ${c.bold('Generated variants')} ${c.dim('(courses/_generated, gitignored, rebuilt)')}:`);
  (generated().length ? generated() : ['(none — run Generate)']).forEach(n => console.log('   • ' + n));
  console.log(`\n  ${c.bold('Context packs')}:`);
  packs().forEach(n => console.log('   • ' + n));
}
async function cmdLink() {
  const choice = await pick('Projects available — point src/course at:',
    [...baseCourses().map(n => `courses/${n}`), ...generated().map(n => `_generated/${n}`)]);
  if (!choice) return console.log(c.yellow('\n  cancelled.'));
  relink(choice.replace(/^courses\//, ''));
}
async function cmdGenerate() {
  const tier = await pick('Projects available (base course):', baseCourses());
  if (!tier) return console.log(c.yellow('\n  cancelled.'));
  const context = await pick('Context pack:', packs());
  if (!context) return console.log(c.yellow('\n  cancelled.'));
  mergeAndLink(tier, context);
}
async function cmdRebuild(args) {
  const context = (args && args[0]) || await pick('Context pack:', packs());
  if (!context) return console.log(c.yellow('\n  cancelled.'));
  const tier = (args && args[1]) || soleTier() || await pick('Projects available (base course):', baseCourses());
  if (!tier) return console.log(c.yellow('\n  cancelled.'));
  if (!mergeAndLink(tier, context)) return;
  // flags builder for the build step (unless non-interactive args were given)
  let buildCmd = 'npx grunt build';
  if (!(args && args.length)) {
    const extra = await chooseFlags([{ f: '--force', d: 'build a partly-authored shell past check-json' }]);
    if (extra) buildCmd += ' ' + extra;
  }
  sh(buildCmd);
}

async function cmdReferences(args) {
  // non-interactive: `cf import` imports, otherwise export
  let mode = (args && args[0]) || null;
  if (!mode) {
    const a = await ask('\n  (e)xport worksheet or (i)mport filled links? [E/i] ');
    mode = /^i/i.test(a) ? 'import' : 'export';
  }
  sh(mode === 'import' ? 'node tools/export-references.js --import' : 'node tools/export-references.js');
}

async function cmdNpmOther() {
  const curated = new Set(ALL.map(it => npmScriptOf(it.base)).filter(Boolean));
  const rest = Object.keys(pkgScripts()).filter(s => !curated.has(s)).sort();
  const sel = await pick('Other scripts in package.json:', rest);
  if (!sel) return console.log(c.yellow('\n  cancelled.'));
  console.log(c.dim(`  ${sel} = ${pkgScripts()[sel]}`));
  sh(`npm run ${sel}`);
}

// --- git ------------------------------------------------------------------
// Capture-mode git, for reading state.
function git(args) {
  const r = spawnSync(`git ${args}`, { cwd: ROOT, shell: true, encoding: 'utf8' });
  return { ok: r.status === 0, out: String(r.stdout || '').trim(), err: String(r.stderr || '').trim() };
}
// Argv-mode git, for anything carrying user input: no shell, so a commit
// message or filename cannot be reinterpreted as shell syntax.
function gitRun(argv) {
  console.log(c.dim(`\n$ git ${argv.join(' ')}\n`));
  const r = spawnSync('git', argv, { cwd: ROOT, stdio: 'inherit' });
  if (r.status !== 0) console.log(c.yellow(`\n(git exited with code ${r.status})`));
  return r.status === 0;
}
const changedFiles = () => git('status --porcelain').out.split('\n').filter(Boolean)
  .map(l => ({ code: l.slice(0, 2), file: l.slice(3).replace(/^.* -> /, '') }));

function currentBranch() {
  const b = git('branch --show-current').out;
  if (!b) console.log(c.red('\n  detached HEAD — no branch to work with.'));
  return b || null;
}

async function cmdCommit() {
  const files = changedFiles();
  if (!files.length) return console.log(c.green('\n  nothing to commit; working tree is clean.'));
  console.log(`\n  ${c.bold('Changed files')}`);
  files.forEach((f, i) => console.log(`  ${c.cyan(String(i + 1))}) ${c.dim(f.code)} ${f.file}`));
  console.log(`  ${c.cyan('a')}) all of them, in one commit`);
  const a = await ask('\n  commit which? (number, or a; blank to cancel): ');
  if (a === '') return console.log(c.yellow('  cancelled.'));

  let targets;
  if (/^a$/i.test(a)) targets = files.map(f => f.file);
  else {
    const n = parseInt(a, 10);
    if (!(n >= 1 && n <= files.length)) return console.log(c.yellow('  not a listed choice; cancelled.'));
    targets = [files[n - 1].file];
  }
  const msg = await ask('  commit message: ');
  if (!msg) return console.log(c.yellow('  empty message; cancelled (a message is never auto-generated).'));
  if (!gitRun(['add', '--', ...targets])) return;
  if (gitRun(['commit', '-m', msg])) console.log(c.green('\n  committed. Not pushed; use gp for that.'));
}

async function cmdSync() {
  const branch = currentBranch();
  if (!branch) return;
  if (changedFiles().length) {
    console.log(c.yellow('\n  working tree is dirty. Commit first (gc); a merge into a dirty tree is how work gets lost.'));
    return sh('git -c color.ui=always status --short');
  }
  if (!git(`ls-remote --exit-code --heads origin ${branch}`).ok)
    return console.log(c.yellow(`\n  '${branch}' is not on origin yet; nothing to fetch. Use gp to publish it.`));
  if (!gitRun(['fetch', 'origin', branch])) return;
  if (!gitRun(['merge', '--no-edit', `origin/${branch}`])) {
    console.log(c.yellow('\n  merge stopped. Resolve the listed files, then:'));
    console.log('    git add <files> && git commit');
    console.log('  or back out with:  git merge --abort');
    return;
  }
  console.log(c.green('\n  up to date with origin.'));
}

async function cmdPush() {
  const branch = currentBranch();
  if (!branch) return;
  const known = git(`ls-remote --exit-code --heads origin ${branch}`).ok;
  const ahead = known ? git(`rev-list --count origin/${branch}..HEAD`).out : null;
  if (known && ahead === '0') return console.log(c.green(`\n  origin/${branch} already has every local commit.`));
  console.log(`\n  about to push ${c.bold(branch)} to origin` +
    (known ? ` (${ahead} commit(s) ahead)` : ' (new branch on origin)'));
  console.log(c.dim('  pushing is deliberate here: type the branch name to confirm.'));
  const a = await ask(`  type '${branch}' to push (anything else cancels): `);
  if (a !== branch) return console.log(c.yellow('  cancelled; nothing pushed.'));
  gitRun(known ? ['push', 'origin', branch] : ['push', '-u', 'origin', branch]);
}

// --- describe one command -------------------------------------------------
function describe(token) {
  const it = byAlias[token] || ALL.find(x => x.name.toLowerCase() === String(token).toLowerCase());
  if (!it) { console.log(c.yellow(`\n  no such command: ${token}`)); return; }
  const panel = GROUPS.find(g => g.items.includes(it));
  console.log(`\n  ${c.bold(it.name)}  ${c.cyan('[' + it.alias + ']')}  ${c.dim(panel ? panel.title : '')}`);
  console.log(`  ${it.desc}`);
  console.log(`\n  ${c.bold('runs')}: ${it.base ? c.green(it.base) : c.green('(built in to this menu)')}`);
  if (it.freePort) console.log(`  ${c.bold('first')}: frees port ${it.freePort} if anything holds it`);
  const target = it.base ? cmdTargetFile(it.base) : null;
  if (target) {
    const rel = path.relative(ROOT, target).split(path.sep).join('/');
    const doc = headerDoc(target);
    console.log(`  ${c.bold('source')}: ${rel}`);
    if (doc) {
      console.log(`\n  ${c.dim('— from the header of ' + rel + ' —')}`);
      doc.body.split('\n').forEach(l => console.log('  ' + c.dim(l)));
    } else {
      console.log(c.dim(`  (${rel} has no header comment to read)`));
    }
  }
}

async function cmdDescribe(args) {
  if (args && args.length) return describe(args[0]);
  const a = await ask('\n  describe which command? (number or alias): ');
  if (!a) return console.log(c.yellow('  cancelled.'));
  const n = parseInt(a, 10);
  describe(n >= 1 && n <= ALL.length ? ALL[n - 1].alias : a);
}

// --- aliases reference (+ shell snippet) ---
function printAliases() {
  console.log(`\n${c.bold('ALIAS REFERENCE')}  ${c.dim('— pattern: <panel><action> (b=build, c=course, n=npm, s=scripts, g=git)')}\n`);
  for (const g of GROUPS) {
    console.log('  ' + c.bold(g.title));
    for (const it of g.items) console.log(`    ${c.cyan(it.alias)}  ${it.name.padEnd(22)} ${c.dim(it.desc)}`);
    console.log('');
  }
  console.log(c.bold('  Shell aliases') + c.dim(' (optional — paste into ~/.zshrc or ~/.bashrc; run from the repo):'));
  console.log('    alias v=\'npm run viewer\'');
  for (const it of ALL) console.log(`    alias ${it.alias}='node ${SELF_REL} ${it.alias}'`);
  console.log('');
}

// --- dispatch one command (interactive runner) ---
async function runItem(it, args) {
  if (it.fn) await it.fn(args || []);
  else await runBase(it, args || []);
}

// --- non-interactive: node <this file> <alias|key> [args...] ---
async function runOnce(token, args) {
  if (token === 'aliases') return printAliases();
  if (token === 'help') return printHelp();
  if (token === 'describe' || token === 'd') return cmdDescribe(args);
  const it = byAlias[token] || ALL.find(x => x.name.toLowerCase() === token.toLowerCase());
  if (!it) { console.error(`Unknown command: ${token}\nAliases: ${ALL.map(x => x.alias).join(', ')}, aliases, describe, help`); process.exit(2); }
  await runItem(it, args);
}

function printHelp() {
  console.log(`\n${c.bold('viewer — help')}  ${c.dim('(' + SELF_REL + ', repo root ' + ROOT + ')')}

Pick a command by its number or its alias. Commands that need a target or flags
walk you through completing them (choose a project, toggle flags, preview, run).
Nothing runs until the previewed command line is confirmed.

${c.bold('d')} describes a command: what it does, the exact line it runs, and the
header comment of the file behind it. Scripts document themselves that way, so
${c.cyan('describe')} is the honest answer to "what does this one do?".

${c.bold('git')} panel: ${c.cyan('gs/gd/gl')} only read. ${c.cyan('gc')} commits files you choose with a
message you type. ${c.cyan('gu')} fetches and merges, never rebases, never forces, and
refuses a dirty tree. ${c.cyan('gp')} pushes only after you type the branch name.
${exists(COURSES) ? `
Course model: edit the ${c.cyan('base course')} (courses/<slug>/) + ${c.cyan('context packs')}
(content/context-packs/<ctx>/). A ${c.cyan('generated')} course (courses/_generated/
<slug>-<ctx>/) is produced from both by merge-context.js — gitignored, rebuilt,
never edited. ${c.cyan('src/course')} is a symlink naming the build target.` : ''}

Run 'aliases' for the full alias table and a paste-ready shell-alias snippet.`);
}

// --- interactive menu ---
async function menu() {
  rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  for (;;) {
    console.log('\n' + c.bold('══ viewer ═══════════════════════════════════════════════'));
    console.log('  project: ' + c.cyan(path.basename(ROOT)) + c.dim(`  (${ROOT})`));
    if (exists(COURSES)) {
      const t = currentTarget();
      console.log('  target:  ' + (t.kind === 'MISSING' ? c.red('none') :
        c.cyan(t.target) + (t.kind === 'symlink' && !t.exists ? c.red('  [unresolved!]') : '')));
    }
    const br = git('branch --show-current').out;
    if (br) {
      const dirty = changedFiles().length;
      console.log('  git:     ' + c.cyan(br) + (dirty ? c.yellow(`  [${dirty} file(s) uncommitted]`) : c.green('  [clean]')));
    }
    let n = 0;
    const index = [];
    for (const g of GROUPS) {
      console.log('\n  ' + c.bold(g.title));
      for (const it of g.items) {
        n++; index.push(it);
        console.log(`   ${c.cyan(String(n).padStart(2))} ${c.cyan('[' + it.alias + ']')} ${c.bold(it.name.padEnd(20))} ${c.dim(it.desc)}`);
      }
    }
    console.log(`\n   ${c.cyan(' d')} ${c.cyan('[d ]')} ${c.bold('describe'.padEnd(20))} ${c.dim('what a command does + the header of the file it runs')}`);
    console.log(`   ${c.cyan(' a')} ${c.cyan('[a ]')} ${c.bold('aliases'.padEnd(20))} ${c.dim('full alias table + shell snippet')}`);
    console.log(`   ${c.cyan(' h')} ${c.cyan('[h ]')} ${c.bold('help'.padEnd(20))} ${c.dim('how the model + builder work')}`);
    console.log(`   ${c.cyan(' 0')} ${c.cyan('[q ]')} ${c.bold('quit'.padEnd(20))} ${c.dim('exit')}`);
    const a = await ask('\n  > ');
    if (a === '0' || /^q/i.test(a)) break;
    if (a === 'a' || a === 'aliases') { printAliases(); continue; }
    if (a === 'h' || a === 'help') { printHelp(); continue; }
    if (a === 'd' || a === 'describe') { await cmdDescribe([]); continue; }
    if (/^d\s+\S+/.test(a)) { describe(a.replace(/^d\s+/, '')); continue; }
    let it = byAlias[a];
    if (!it) { const num = parseInt(a, 10); if (num >= 1 && num <= index.length) it = index[num - 1]; }
    if (!it) { console.log(c.yellow('  pick a number or an alias from the list.')); continue; }
    try { await runItem(it, []); } catch (e) { console.log(c.red('  error: ' + e.message)); }
  }
  rl.close();
  console.log('bye.');
}

(async () => {
  const [token, ...args] = process.argv.slice(2);
  if (token) { await runOnce(token, args); if (rl) rl.close(); }
  else await menu();
})();
