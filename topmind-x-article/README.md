# topmind-x-article · X 长文一键发布

[English](./README.en.md) | 中文

把 Markdown 原稿变成"复制 → 粘贴 → 发"的 X 长文（Article）发布包。

## 安装

```bash
npx @topmindspace/tms-skills install topmind-x-article
```

## 用法

```bash
# 1. 原稿转可粘贴纯文本（一键复制的核心）
python3 scripts/md2x.py <原稿>.md --out <包>/X发布稿.txt

# 2. 封面图：用 topmind-cover 生成 1200×675

# 3. 按 references/publish-checklist.md 逐项发布
```

## 转换规则

X Article 编辑器对 markdown 支持弱且不稳定，`md2x.py` 按 `references/x-format.md`
转纯文本：标题→纯文本行、加粗/斜体去标记、链接→`文字（url）`、
图片→`[图N]`（文末附配图清单）、表格→"项：值"列表。

转完必须人工通读一遍。

## 发布

X 长文目前走人工粘贴发布（X Article 编辑器），API 不发长文。
发布后按清单做：首条评论置顶补信息、全文抓回核对。

## 外部依赖

以下技能**不在本仓库**（一般随用户侧 workbuddy 环境提供）。缺失时对应路由能力
不可用，不影响本技能核心流程（原稿转文本、封面、发布清单）：

- `topmind-x`：280 字短推文发布（其 xurl 只覆盖短推文，不发长文）。
- `topmind-capture`：「只想存档不发布」时的收录路由。

## 开发

```bash
python3 scripts/package_skill.py --check   # 发布前校验
python3 scripts/negative_tests.py          # 异常输入测试
```
