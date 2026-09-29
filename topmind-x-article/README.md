# topmind-x-article · X 长文一键发布

[English](./README.en.md) | 中文

把 Markdown 原稿变成"复制 → 粘贴 → 发"的 X 长文（Article）发布包。

- 版本：**v0.1.0**（与 `@topmindspace/tms-skills@0.3.7` 同 tag）

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
转纯文本：标题→纯文本行、分隔线→空行、加粗/斜体/行内代码去标记、链接→`文字（url）`、
图片→`[图N]`（文末附配图清单）、表格→"项：值"列表、引用去 `>`、`\\` 转义还原。

转完必须人工通读一遍。

## 最小示例

输入（10 行 markdown）：

```markdown
# Manus 2.0 发布了

**从零重建**的 Agent，新增了 Cue 个人助手。

![发布会现场](cover.png)

| Token 消耗 | -23.2% |
| 耗时 | -28.2% |

详见[官方博客](https://manus.im/blog)。
```

`python3 scripts/md2x.py 原稿.md --out X发布稿.txt` 得到：

```
Manus 2.0 发布了

从零重建的 Agent，新增了 Cue 个人助手。

[图1]

Token 消耗：-23.2%
耗时：-28.2%

详见官方博客（https://manus.im/blog）。

—— 配图清单 ——
[图1] 发布会现场
```

复制 `X发布稿.txt` 全文 → 粘贴进 X Article 编辑器 → 按 `[图N]` 顺序上传配图 → 发布。

## 发布

X 长文目前走人工粘贴发布（X Article 编辑器），API 不发长文。
发布后按清单做：首条评论置顶补信息、全文抓回核对。

## 外部依赖

以下技能**不在本仓库**（一般随用户侧 workbuddy 环境提供）。缺失时对应路由能力
不可用，不影响本技能核心流程（原稿转文本、封面、发布清单）：

- `topmind-x`：280 字短推文发布（xurl 只覆盖短推文，不发长文）。
- `topmind-capture`：「只想存档不发布」时的收录路由。

## 开发

```bash
python3 scripts/package_skill.py --check   # 发布前校验
python3 scripts/negative_tests.py          # 异常输入测试
```
