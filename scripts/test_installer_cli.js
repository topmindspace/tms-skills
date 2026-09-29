#!/usr/bin/env node
/**
 * tms-skills 安装器 CLI 负向测试（零依赖：node 直接可跑）。
 *
 * 覆盖 install/uninstall 新行为的负向分支 + 成功路径回归：
 *   1. install 到已存在的技能目录（无 --force）→ 拒绝，报错含已装版本/--force/卸载提示
 *   2. install --force 到已存在目录 → 成功，摘要含 to:/version:/next: 三行
 *   3. uninstall 缺 skill id → 失败并打印用法
 *   4. uninstall 非法 skill id（路径穿越）→ 拒绝
 *   5. uninstall 未安装的技能 → 失败并提示"Nothing to uninstall"，顺带列出该目录已装技能
 *   6. uninstall 目标存在但不是技能目录（无 SKILL.md）→ 拒绝，目录完好
 *   7. uninstall --to 指到包内技能源 → 拒绝，源目录完好
 *   8. uninstall 正常路径：install → uninstall → 目录消失
 *   9. uninstall 未知选项 → 失败
 *  10. install 未知选项 → 失败
 *
 * 隔离设计：把 bin/tms-skills.js 复制到临时目录，旁边搭假技能树，
 * 最多删 /tmp 下的假目录，绝不碰仓库真技能。
 *
 * 用法：node scripts/test_installer_cli.js
 * 任一失败 → 打印 ✗ 并 exit 1。
 */
'use strict';

const { spawnSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const REPO_BIN = path.resolve(__dirname, '..', 'bin', 'tms-skills.js');
let failures = 0;

function ok(cond, msg) {
  console.log((cond ? '  ✓ ' : '  ✗ ') + msg);
  if (!cond) failures++;
}

function noTraceback(out) {
  return !/Traceback|^\s+at\s/m.test(out);
}

/** 搭隔离环境：<tmp>/bin/tms-skills.js + <tmp>/testskill/SKILL.md（version: 9.9.9） */
function makeEnv() {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'tms-install-cli-'));
  fs.mkdirSync(path.join(tmp, 'bin'), { recursive: true });
  fs.copyFileSync(REPO_BIN, path.join(tmp, 'bin', 'tms-skills.js'));
  const skill = path.join(tmp, 'testskill');
  fs.mkdirSync(skill, { recursive: true });
  fs.writeFileSync(
    path.join(skill, 'SKILL.md'),
    '---\nname: testskill\nversion: 9.9.9\ndescription: fake skill for installer cli tests\n---\n# testskill\n'
  );
  return { tmp, skill, bin: path.join(tmp, 'bin', 'tms-skills.js') };
}

function runCli(env, args, cwd) {
  return spawnSync(process.execPath, [env.bin, ...args], {
    cwd: cwd || env.tmp,
    encoding: 'utf8',
    timeout: 20000,
  });
}

function out(r) {
  return (r.stdout || '') + (r.stderr || '');
}

function destroy(env) {
  fs.rmSync(env.tmp, { recursive: true, force: true });
}

function main() {
  if (!fs.existsSync(REPO_BIN)) {
    console.error('找不到安装器：' + REPO_BIN);
    process.exit(1);
  }

  // 1. install 到已存在目录（无 --force）→ 拒绝：报已装版本，要求 --force
  {
    const env = makeEnv();
    try {
      const destRoot = path.join(env.tmp, 'out');
      const destSkill = path.join(destRoot, 'testskill');
      fs.mkdirSync(destSkill, { recursive: true });
      fs.writeFileSync(
        path.join(destSkill, 'SKILL.md'),
        '---\nname: testskill\nversion: 1.0.0\n---\n# stale copy\n'
      );
      fs.writeFileSync(path.join(destSkill, 'stale.txt'), 'stale');
      const r = runCli(env, ['install', 'testskill', '--to', destRoot]);
      const o = out(r);
      ok(r.status !== 0, 'case1: 已存在目录无 --force 被拒绝（exit 非 0）');
      ok(/installed version:\s*1\.0\.0/.test(o), 'case1: 报错含已装版本号 1.0.0');
      ok(/--force/.test(o), 'case1: 报错提示 --force');
      ok(/uninstall/.test(o), 'case1: 报错提示可先 uninstall');
      ok(noTraceback(o), 'case1: 无 Traceback/堆栈');
      ok(fs.existsSync(path.join(destSkill, 'stale.txt')), 'case1: 旧目录未被改动');
    } finally {
      destroy(env);
    }
  }

  // 2. install --force → 成功，摘要三行齐全
  {
    const env = makeEnv();
    try {
      const destRoot = path.join(env.tmp, 'out');
      const destSkill = path.join(destRoot, 'testskill');
      fs.mkdirSync(destSkill, { recursive: true });
      fs.writeFileSync(path.join(destSkill, 'stale.txt'), 'stale');
      const r = runCli(env, ['install', 'testskill', '--to', destRoot, '--force']);
      const o = out(r);
      ok(r.status === 0, 'case2: --force 安装 exit 0');
      ok(/^\s*to:\s*\S+/m.test(o), 'case2: 摘要有 to: 行（装到哪里）');
      ok(/^\s*version:\s*skill 9\.9\.9/m.test(o), 'case2: 摘要有 version: 行（含技能版本）');
      ok(/^\s*next:\s*\S+/m.test(o), 'case2: 摘要有 next: 行（下一步）');
      ok(!fs.existsSync(path.join(destSkill, 'stale.txt')), 'case2: 旧目标被清空覆盖');
    } finally {
      destroy(env);
    }
  }

  // 3. uninstall 缺 skill id
  {
    const env = makeEnv();
    try {
      const r = runCli(env, ['uninstall']);
      const o = out(r);
      ok(r.status !== 0, 'case3: uninstall 缺 skill id（exit 非 0）');
      ok(/Missing skill id/.test(o) && noTraceback(o), 'case3: 提示缺 id 且无 Traceback');
    } finally {
      destroy(env);
    }
  }

  // 4. uninstall 非法 skill id（路径穿越）
  {
    const env = makeEnv();
    try {
      const r = runCli(env, ['uninstall', '../evil', '--to', path.join(env.tmp, 'out')]);
      const o = out(r);
      ok(r.status !== 0, 'case4: 非法 skill id 被拒绝（exit 非 0）');
      ok(/Invalid skill id/.test(o) && noTraceback(o), 'case4: 报错友好无 Traceback');
    } finally {
      destroy(env);
    }
  }

  // 5. uninstall 未安装的技能 → 干净报错，并列出该目录已装技能
  {
    const env = makeEnv();
    try {
      const destRoot = path.join(env.tmp, 'out');
      const other = path.join(destRoot, 'otherskill');
      fs.mkdirSync(other, { recursive: true });
      fs.writeFileSync(path.join(other, 'SKILL.md'), '---\nname: otherskill\nversion: 2.0.0\n---\n');
      const r = runCli(env, ['uninstall', 'testskill', '--to', destRoot]);
      const o = out(r);
      ok(r.status !== 0, 'case5: 未安装技能 exit 非 0');
      ok(/Nothing to uninstall/.test(o), 'case5: 报错说明未安装');
      ok(/installed here: otherskill/.test(o), 'case5: 列出该目录已装技能');
      ok(noTraceback(o), 'case5: 无 Traceback');
    } finally {
      destroy(env);
    }
  }

  // 6. uninstall 目标存在但不是技能目录 → 拒绝，目录完好
  {
    const env = makeEnv();
    try {
      const destRoot = path.join(env.tmp, 'out');
      const destSkill = path.join(destRoot, 'testskill');
      fs.mkdirSync(destSkill, { recursive: true });
      fs.writeFileSync(path.join(destSkill, 'notes.txt'), 'user data');
      const r = runCli(env, ['uninstall', 'testskill', '--to', destRoot]);
      const o = out(r);
      ok(r.status !== 0, 'case6: 非技能目录被拒绝删除（exit 非 0）');
      ok(/not a skill directory/.test(o), 'case6: 报错说明原因');
      ok(fs.existsSync(path.join(destSkill, 'notes.txt')), 'case6: 用户目录完好');
      ok(noTraceback(o), 'case6: 无 Traceback');
    } finally {
      destroy(env);
    }
  }

  // 7. uninstall --to 指到包内（dest == 技能源目录）→ 拒绝，源完好
  {
    const env = makeEnv();
    try {
      const r = runCli(env, ['uninstall', 'testskill', '--to', env.tmp]); // dest == src
      const o = out(r);
      ok(r.status !== 0, 'case7: --to 指到技能源目录被拒绝（exit 非 0）');
      ok(fs.existsSync(path.join(env.skill, 'SKILL.md')), 'case7: 源目录未被删除');
      ok(/own directory tree|Refusing/i.test(o), 'case7: 报错友好无 Traceback');
    } finally {
      destroy(env);
    }
  }

  // 8. 正常路径：install → uninstall → 目录消失
  {
    const env = makeEnv();
    try {
      const destRoot = path.join(env.tmp, 'out');
      const destSkill = path.join(destRoot, 'testskill');
      let r = runCli(env, ['install', 'testskill', '--to', destRoot]);
      ok(r.status === 0, 'case8: install 成功');
      r = runCli(env, ['uninstall', 'testskill', '--to', destRoot]);
      const o = out(r);
      ok(r.status === 0, 'case8: uninstall exit 0');
      ok(/Uninstalled testskill/.test(o), 'case8: 打印卸载确认');
      ok(!fs.existsSync(destSkill), 'case8: 技能目录已删除');
      ok(fs.existsSync(destRoot), 'case8: 目标根目录保留（只删技能目录）');
    } finally {
      destroy(env);
    }
  }

  // 9. uninstall 未知选项
  {
    const env = makeEnv();
    try {
      const r = runCli(env, ['uninstall', 'testskill', '--bogus']);
      ok(r.status !== 0, 'case9: uninstall 未知选项 exit 非 0');
      ok(noTraceback(out(r)), 'case9: 无 Traceback');
    } finally {
      destroy(env);
    }
  }

  // 10. install 未知选项
  {
    const env = makeEnv();
    try {
      const r = runCli(env, ['install', 'testskill', '--bogus']);
      ok(r.status !== 0, 'case10: install 未知选项 exit 非 0');
      ok(noTraceback(out(r)), 'case10: 无 Traceback');
    } finally {
      destroy(env);
    }
  }

  console.log(failures ? `\n[test_installer_cli] ${failures} 项失败` : '\n[test_installer_cli] 全部通过');
  process.exit(failures ? 1 : 0);
}

main();
