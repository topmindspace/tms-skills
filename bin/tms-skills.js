#!/usr/bin/env node
/**
 * tms-skills — TopMindspace agent skills installer
 *
 * Recommended channel (when published): npm @topmindspace/tms-skills
 * GitHub npx remains available for HEAD / offline clone.
 *
 * Usage:
 *   npx @topmindspace/tms-skills list
 *   npx @topmindspace/tms-skills install top-ppt-html
 *   npx @topmindspace/tms-skills install top-ppt-html --to ./skills-out
 *   npx @topmindspace/tms-skills install top-ppt-html --force
 *   npx github:topmindspace/tms-skills install top-ppt-html   # follow repo HEAD
 */
'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
// Skills live at repo root (one directory per skill with SKILL.md).
const INFRA_DIRS = new Set(['bin', 'docs', 'scripts', 'node_modules', 'dist', 'release-assets']);
const SKILL_ID_RE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

function die(msg, code = 1) {
  console.error(msg);
  process.exit(code);
}

function skillDir(skillId) {
  return path.join(ROOT, skillId);
}

function assertSkillId(skillId) {
  if (!skillId || typeof skillId !== 'string') {
    die('Missing skill id.\n\n' + usageText());
  }
  if (
    skillId.includes('..') ||
    skillId.includes('/') ||
    skillId.includes('\\') ||
    path.isAbsolute(skillId) ||
    !SKILL_ID_RE.test(skillId)
  ) {
    die(
      `Invalid skill id: ${JSON.stringify(skillId)}\n` +
        'Skill ids must match ^[a-z0-9]+(?:-[a-z0-9]+)*$ (no paths, dots, or slashes).'
    );
  }
}

function listSkillIds() {
  return fs
    .readdirSync(ROOT, { withFileTypes: true })
    .filter((d) => d.isDirectory() && !INFRA_DIRS.has(d.name) && !d.name.startsWith('.'))
    .filter((d) => fs.existsSync(path.join(ROOT, d.name, 'SKILL.md')))
    .map((d) => d.name)
    .sort();
}

function readSkillMeta(skillId) {
  const skillPath = skillDir(skillId);
  const skillMd = path.join(skillPath, 'SKILL.md');
  if (!fs.existsSync(skillMd)) return { id: skillId, description: '' };
  const text = fs.readFileSync(skillMd, 'utf8');
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return { id: skillId, description: '' };
  const desc = (m[1].match(/^description:\s*"(.*)"\s*$/m) || m[1].match(/^description:\s*(.+)\s*$/m) || [])[1] || '';
  return { id: skillId, description: String(desc).slice(0, 120) };
}

function resolveDefaultTarget() {
  const home = process.env.HOME || process.env.USERPROFILE || '';
  const candidates = [
    path.join(process.cwd(), '.agents', 'skills'),
    path.join(process.cwd(), '.claude', 'skills'),
    path.join(process.cwd(), '.cursor', 'skills'),
    path.join(process.cwd(), '.codex', 'skills'),
    path.join(process.cwd(), '.mimocode', 'skills'),
    path.join(home, '.claude', 'skills'),
    path.join(home, '.agents', 'skills'),
    path.join(home, '.cursor', 'skills'),
    path.join(home, '.codex', 'skills'),
  ];
  for (const dir of candidates) {
    if (dir && fs.existsSync(path.dirname(dir))) {
      return dir;
    }
  }
  return path.join(process.cwd(), '.agents', 'skills');
}

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, entry.name);
    const d = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === 'node_modules' || entry.name === 'dist' || entry.name === '__pycache__') continue;
      copyDir(s, d);
    } else if (entry.isFile()) {
      if (entry.name.endsWith('.pyc')) continue;
      fs.copyFileSync(s, d);
    }
  }
}

function install(skillId, targetRoot, { force = false } = {}) {
  assertSkillId(skillId);
  const src = skillDir(skillId);
  if (!fs.existsSync(path.join(src, 'SKILL.md'))) {
    die(`Skill not found: ${skillId}\nAvailable: ${listSkillIds().join(', ') || '(none)'}`);
  }
  const dest = path.join(targetRoot, skillId);
  fs.mkdirSync(targetRoot, { recursive: true });
  if (fs.existsSync(dest)) {
    if (!force) {
      die(
        `Destination already exists: ${dest}\n` +
          'Refusing to overwrite. Pass --force (or -f) to replace.'
      );
    }
    fs.rmSync(dest, { recursive: true, force: true });
  }
  copyDir(src, dest);
  console.log(`Installed ${skillId}`);
  console.log(`  from ${src}`);
  console.log(`  to   ${dest}`);
  console.log('');
  console.log('Optional (PPTX export only):');
  console.log(`  cd "${dest}" && npm install`);
}

function usageText() {
  return `tms-skills — install TopMindspace agent skills

Usage:
  tms-skills list
  tms-skills install <skill-id> [--to <dir>] [--force|-f]
  tms-skills help

Examples (npm recommended when published):
  npx @topmindspace/tms-skills list
  npx @topmindspace/tms-skills install top-ppt-html
  npx @topmindspace/tms-skills install top-ppt-html --to ./.agents/skills
  npx @topmindspace/tms-skills install top-ppt-html --force

  # Follow repo HEAD:
  npx github:topmindspace/tms-skills install top-ppt-html
`;
}

function usage() {
  console.log(usageText());
}

function main(argv) {
  const args = argv.slice(2);
  const cmd = args[0];

  if (!cmd || cmd === 'help' || cmd === '--help' || cmd === '-h') {
    usage();
    return;
  }

  if (cmd === 'list' || cmd === 'ls') {
    const ids = listSkillIds();
    if (!ids.length) {
      console.log('No skills found in package.');
      return;
    }
    for (const id of ids) {
      const meta = readSkillMeta(id);
      console.log(`${id}`);
      if (meta.description) console.log(`  ${meta.description}…`);
    }
    return;
  }

  if (cmd === 'install') {
    const skillId = args[1];
    if (!skillId || skillId.startsWith('-')) {
      die('Missing skill id.\n\n' + usageText());
    }
    let to = null;
    let force = false;
    for (let i = 2; i < args.length; i++) {
      if (args[i] === '--to' || args[i] === '-t') {
        to = args[++i];
        if (!to) die('Option --to requires a directory path.');
      } else if (args[i] === '--force' || args[i] === '-f') {
        force = true;
      } else {
        die(`Unknown option: ${args[i]}\n\n` + usageText());
      }
    }
    const targetRoot = to ? path.resolve(to) : resolveDefaultTarget();
    install(skillId, targetRoot, { force });
    return;
  }

  die(`Unknown command: ${cmd}\n\n` + usageText());
}

main(process.argv);
