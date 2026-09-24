#!/usr/bin/env node
/**
 * tms-skills — TopMindspace agent skills installer
 *
 * Usage (GitHub is the primary install source — npm publish is optional):
 *   npx github:topmindspace/tms-skills list
 *   npx github:topmindspace/tms-skills install top-ppt-html
 *   npx github:topmindspace/tms-skills install top-ppt-html --to ./skills-out
 *   npx @topmindspace/tms-skills install top-ppt-html   # only after npm publish
 */
'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
// Skills live at repo root (one directory per skill with SKILL.md).
const INFRA_DIRS = new Set(['bin', 'docs', 'scripts', 'node_modules', 'dist', 'release-assets']);

function die(msg, code = 1) {
  console.error(msg);
  process.exit(code);
}

function skillDir(skillId) {
  return path.join(ROOT, skillId);
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
  const candidates = [
    path.join(process.cwd(), '.agents', 'skills'),
    path.join(process.cwd(), '.claude', 'skills'),
    path.join(process.cwd(), '.mimocode', 'skills'),
    path.join(process.env.HOME || process.env.USERPROFILE || '', '.claude', 'skills'),
    path.join(process.env.HOME || process.env.USERPROFILE || '', '.agents', 'skills'),
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

function install(skillId, targetRoot) {
  const src = skillDir(skillId);
  if (!fs.existsSync(path.join(src, 'SKILL.md'))) {
    die(`Skill not found: ${skillId}\nAvailable: ${listSkillIds().join(', ') || '(none)'}`);
  }
  const dest = path.join(targetRoot, skillId);
  fs.mkdirSync(targetRoot, { recursive: true });
  if (fs.existsSync(dest)) {
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

function usage() {
  console.log(`tms-skills — install TopMindspace agent skills

Usage:
  tms-skills list
  tms-skills install <skill-id> [--to <dir>]
  tms-skills help

Examples:
  npx github:topmindspace/tms-skills list
  npx github:topmindspace/tms-skills install top-ppt-html
  npx github:topmindspace/tms-skills install top-ppt-html --to ./.agents/skills

  # Optional npm package (only after @topmindspace/tms-skills is published):
  npx @topmindspace/tms-skills install top-ppt-html
`);
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
      die('Missing skill id.\n\n' + usage());
    }
    let to = null;
    for (let i = 2; i < args.length; i++) {
      if (args[i] === '--to' || args[i] === '-t') {
        to = args[++i];
        if (!to) die('Option --to requires a directory path.');
      }
    }
    const targetRoot = to ? path.resolve(to) : resolveDefaultTarget();
    install(skillId, targetRoot);
    return;
  }

  die(`Unknown command: ${cmd}\n\n` + usage());
}

main(process.argv);
