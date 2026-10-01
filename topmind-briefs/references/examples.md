# 示例 · 干货短文（按真实帖子校准）

## 例 1：数据榜单型（@ArtificialAnlys 原文结构）

原文模式：先抛一个反直觉判断 → 甩基准 → 给最扎眼的数字 → 图证明。

```
Restricting offensive without blocking defensive is difficult...

On CyberGym-E2E-AA, some frontier models are safety blocked on 85%+ of tasks.

The good news: with GPT-6 Luna or MiMo-V2.6-Pro, ~100 bug hunts in a 1M+ line
codebase for ~$20 — up to 100x cheaper per task than Grok 4.7.

[图：上下两张柱状图——任务解决率 vs 单任务成本]
```

结构拆解：
1. 判断句开头（一句话观点）
2. 基准是什么（一句话）
3. 最扎眼的数字（85%+、~$20、100x）
4. 图：解决率和成本两张图并置

## 例 2：榜单速报型（@arena 原文结构）

```
Big news: Gemini 4 Argon (High) just landed #1 in Text Arena with 1525 pts,
and #8 in Code Arena: WebDev with 1679 pts!

Blended $8/MToken — the most cost efficient model on the Pareto frontier.

#1 in Coding, Hard Prompts, Instruction Following, Longer Query, Creative Writing.
+20 pts above #2 Claude Opus 4.6 (High); leap from #11 (Gemini 3.8 Flash).

[图：Text Arena + Code Arena 排行榜截图各一张]
```

结构拆解：
1. "Big news:" + 排名 + 分数（开头即全部关键信息）
2. 价格/性价比（一句话）
3. 细分维度展开（列表）
4. 纵向对比（比上次、比第二名）
5. 图：排行榜实拍

## 例 3：论文解读型（@RulinShao 原文结构）

```
‼️The Bitter Lesson for context management: Giving LMs unrestricted control
over their context beats human-designed SOTA!

Introducing 🩵Context Language Models (CLMs)🩵
- Natively manage their own context
- Treat context as a file
- Learn policies in CLM weights, no harness

[图：论文信息图——架构示意 + 四组结果曲线]
```

结构拆解：
1. 加粗判断（"Bitter Lesson"式标题党，但后面有真东西）
2. "Introducing X" + 3 条 bullet（每条 ≤10 词）
3. 图：论文原图（架构 + 结果）

## 例 4：机制讲解型（@akshay_pachaar 原文结构）

```
Jev for RAG, clearly explained!

Hybrid search gives you a shortlist. It does not decide which passages
contain evidence. That missing judgment is where Jev fits.

→ Retrieve wide
[一句话机制]

→ Judge every candidate together
[一句话机制]

→ Let code apply the threshold
[一句话机制]

To summarise:
- Retrieval finds the candidates.
- Jev decides what deserves context.
- The LLM writes the grounded answer.

[视频：RAG 流程架构动画]
```

结构拆解：
1. 标题句（"X, clearly explained!"）
2. 痛点（一句话：现有方案缺什么）
3. 机制分步（→ 标记，每步一句话）
4. "To summarise:" 三行收束
5. 媒体：流程图/动画 + 文章链接

---

## 公众号版改写示例（例 1 → 公众号）

```markdown
# 跑 100 次漏洞挖掘只要 $20：CyberGym-E2E-AA 基准实测

> 想防住攻击又不误伤防御，太难了——前沿模型在 85%+ 的任务上被安全拦截直接拒绝回答。

- 基准：CyberGym-E2E-AA，测从漏洞发现到补丁的全链路防御能力
- 拦截率：部分前沿模型 85%+ 任务被安全机制拦掉
- 成本：GPT-6 Luna / MiMo-V2.6-Pro 跑 ~100 次 bug hunt 约 $20，
  单任务成本比 Grok 4.7 便宜 up to 100 倍

![CyberGym-E2E-AA：任务解决率 vs 单任务成本](图)

来源：Artificial Analysis
```

改写要点：X 版英文直发；公众号版加一句中文背景（"这是什么基准"），
数字保留英文原样，结论不变。

---

## 反例（不要这样写）

❌ "众所周知，AI 发展日新月异。最近，Google 发布了一款新模型，
   引起了广泛关注。值得一提的是，这款模型在多个基准上表现出色…"
   → 铺垫三段，结论藏在最后，没有具体数字。

❌ "大幅提升""显著改善""表现优异"
   → 没有数据的形容词，删掉或换成数字。
