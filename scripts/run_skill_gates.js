#!/usr/bin/env node
/**
 * Run a gate command across all discovered skills.
 *
 * Usage:
 *   node scripts/run_skill_gates.js check
 *   node scripts/run_skill_gates.js audit
 *   node scripts/run_skill_gates.js package
 *   node scripts/run_skill_gates.js install
 */
'use strict';

const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const { discoverSkills, ROOT } = require('./discover_skills');

const PY = process.env.PYTHON || 'python3';

function run(cmd, args, opts = {}) {
  const r = spawnSync(cmd, args, { stdio: 'inherit', cwd: opts.cwd || ROOT, shell: false });
  if (r.error) throw r.error;
  if (r.status !== 0) process.exit(r.status || 1);
}

function hasScript(skillDir, name) {
  return fs.existsSync(path.join(skillDir, 'scripts', name));
}

function main() {
  const mode = process.argv[2];
  const skills = discoverSkills();
  if (!skills.length) {
    console.error('No skills discovered.');
    process.exit(1);
  }
  console.log(`skills: ${skills.join(', ')}`);

  for (const id of skills) {
    const skillDir = path.join(ROOT, id);
    console.log(`\n=== ${mode}: ${id} ===`);

    if (mode === 'check') {
      if (!hasScript(skillDir, 'package_skill.py')) {
        console.log(`skip ${id}: no package_skill.py`);
        continue;
      }
      run(PY, ['scripts/package_skill.py', '--check'], { cwd: skillDir });
    } else if (mode === 'audit') {
      for (const s of ['audit_styles.py', 'audit_docs.py', 'audit_skill.py', 'audit_css.py']) {
        if (!hasScript(skillDir, s)) {
          console.error(`missing ${id}/scripts/${s}`);
          process.exit(1);
        }
        run(PY, [`scripts/${s}`], { cwd: skillDir });
      }
    } else if (mode === 'package') {
      if (!hasScript(skillDir, 'package_skill.py')) {
        console.log(`skip ${id}: no package_skill.py`);
        continue;
      }
      run(PY, ['scripts/package_skill.py'], { cwd: skillDir });
    } else if (mode === 'install') {
      const lock = path.join(skillDir, 'package-lock.json');
      const pkg = path.join(skillDir, 'package.json');
      if (!fs.existsSync(pkg)) {
        console.log(`skip ${id}: no package.json`);
        continue;
      }
      if (fs.existsSync(lock)) {
        run('npm', ['ci', '--omit=dev'], { cwd: skillDir });
      } else {
        run('npm', ['install', '--omit=dev'], { cwd: skillDir });
      }
    } else {
      console.error(`Unknown mode: ${mode}`);
      process.exit(1);
    }
  }
}

main();
