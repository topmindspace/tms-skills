#!/usr/bin/env node
/**
 * Sync package.json "files" so every discovered skill directory is listed.
 * Keeps shipping skill dirs on npm without hard-coding a single skill id.
 *
 * Usage: node scripts/sync_npm_files.js [--check]
 *   --check  exit 1 if files is out of sync (CI)
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { discoverSkills, ROOT } = require('./discover_skills');

const PKG_PATH = path.join(ROOT, 'package.json');
const BASE_FILES = ['bin', 'README.md', 'LICENSE', 'CHANGELOG.md'];

function desiredFiles(skills) {
  return [...BASE_FILES, ...skills];
}

function sync({ checkOnly }) {
  const pkg = JSON.parse(fs.readFileSync(PKG_PATH, 'utf8'));
  const skills = discoverSkills();
  const next = desiredFiles(skills);
  const cur = Array.isArray(pkg.files) ? pkg.files : [];
  const same =
    cur.length === next.length && cur.every((v, i) => v === next[i]);

  if (same) {
    console.log(`files already in sync (${skills.length} skill(s)): ${next.join(', ')}`);
    return 0;
  }

  if (checkOnly) {
    console.error('package.json "files" out of sync with discovered skills.');
    console.error(`  current:  ${JSON.stringify(cur)}`);
    console.error(`  expected: ${JSON.stringify(next)}`);
    console.error('Run: npm run sync:files');
    return 1;
  }

  pkg.files = next;
  fs.writeFileSync(PKG_PATH, JSON.stringify(pkg, null, 2) + '\n', 'utf8');
  console.log(`updated files: ${next.join(', ')}`);
  return 0;
}

const checkOnly = process.argv.includes('--check');
process.exit(sync({ checkOnly }));
