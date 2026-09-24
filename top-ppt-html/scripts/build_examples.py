#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TopPPT HTML · 三模式示例矩阵生成器（主题：AI 智能体发展研究）
用法:
    python scripts/build_examples.py

从 assets/templates/ 三份模式独立模板生成示例矩阵到 assets/examples/：
  presentation × business-blue / apple-mono / brand-red ——《AI 智能体：从工具到同事》（light）
  research     × mckinsey / deep-teal / warm-sand / indigo-violet ——《2026 AI 智能体发展研究报告》（light）
  architecture × graphite-dark / spectrum        ——《企业智能体平台总体架构》
（v8.3 起 9 示例覆盖全部 9 套风格；同一模式的多风格示例共用同一内容包——风格与内容正交的示范）内容包按
__TOPPPT_CONTENT__ 标记整体替换（非正则碎替，防静默截断），REPORT_MODEL 同步注入。
presentation 样例覆盖 comparison / kpi / donut / quote / cards 页型，
     research 样例覆盖 comparison / donut（起另覆盖 6 类复杂信息图页型 +
     gantt/rose/candlestick 三类形状通道图表；29 种页型与 36 种图表的回归覆盖靠三模式合计）。
architecture 模板出厂 data-theme="dark"（石墨深灰深色优先）——graphite 示例
     保持 dark、spectrum 示例切回 light（ex['theme'] 控制，html 标签整体断言）；
     REPORT_MODEL 同步写 theme 字段（PPTX 按 model.theme 导出亮/暗版，
     graphite 架构示例的 PPTX 即为深色版——回归覆盖双主题）。
改动模板/内容包后重跑本脚本，再用 validate_report / extract_model / build_pptx /
validate_pptx --model 全链路回归。
"""
import json
import re
import sys
from pathlib import Path

# Windows GBK 控制台兜底：强制 UTF-8 输出
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
TPL = ROOT / 'assets' / 'templates'
OUT = ROOT / 'assets' / 'examples'

CONTENT_RE = re.compile(r'<!-- __TOPPPT_CONTENT_START__ -->[\s\S]*?<!-- __TOPPPT_CONTENT_END__ -->')
MODEL_RE = re.compile(r'window\.REPORT_MODEL = \{[\s\S]*?\};')  # 非贪婪：只匹配模型块本身

DATE = '2026-09-09'

# ══════════════════════════════════════════════════════════════════════════
#  内容包 · 演示汇报（presentation）《AI 智能体：从工具到同事》
# ══════════════════════════════════════════════════════════════════════════
P_CONTENT = '''<!-- ══ Hero（16:9 满屏页） ══ -->
<section class="band band--fit">
  <div class="wrap">
    <div class="grid g-hero" style="gap:clamp(32px,4vw,72px)">
      <div class="stack gap-5 rv">
        <div class="row row-wrap">
          <span class="chip chip--accent">2026 · 演示汇报</span>
          <span class="chip chip--line">年度研究</span>
        </div>
        <h1 class="t-display">AI 智能体<br>从工具到同事</h1>
        <p class="t-lead" style="max-width:620px">2026 年，软件不再只是被使用，而是开始自主完成工作。</p>
        <div class="row row-wrap" style="gap:var(--sp-3)">
          <a class="btn btn--primary" href="#agenda">开始阅读</a>
          <a class="btn btn--ghost" href="#refs">参考资料</a>
        </div>
        <div class="row row-wrap" style="gap:var(--sp-6);margin-top:var(--sp-3)">
          <div>
            <div class="t-metric" style="color:var(--accent)">61%</div>
            <div class="t-xs" style="margin-top:4px">企业试点率<a class="cite" href="#ref-1">[1]</a></div>
          </div>
          <div>
            <div class="t-metric">18<span style="font-size:.45em"> %</span></div>
            <div class="t-xs" style="margin-top:4px">规模化运行占比<a class="cite" href="#ref-2">[2]</a></div>
          </div>
        </div>
      </div>
      <div class="g-hero__visual rv">
        <div class="fig">
          <div class="fig__cap">2025 企业智能体试点率</div>
          <svg class="chart" data-chart="donut" viewBox="0 0 140 140" style="width:180px;margin-inline:auto">
            <circle cx="70" cy="70" r="54" class="f-none s-bds" stroke-width="15"/>
            <circle data-sweep data-circ="339.3" data-p="0.61" cx="70" cy="70" r="54" class="f-none s-acc"
                    stroke-width="15" stroke-dasharray="207 132.3" stroke-linecap="round"
                    transform="rotate(-90 70 70)"><title>试点率 61%</title></circle>
            <text x="70" y="68" text-anchor="middle" class="f-txt" font-size="26" font-weight="600"
                  data-count="61" data-suffix="%">61%</text>
            <text x="70" y="88" text-anchor="middle" class="f-txt3" font-size="11">已进入试点</text>
          </svg>
          <div class="row" style="justify-content:center;gap:var(--sp-4);margin-top:var(--sp-4)">
            <span class="chip chip--accent">试点及以上 61%</span>
            <span class="chip">观望 39%</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ══ Agenda 大纲页（第二页） ══ -->
<section class="band band--tint" id="agenda">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">Agenda</div>
      <h2 class="t-h1 shead__title">报告大纲</h2>
      <p class="t-lead shead__desc">三章加参考资料，从范式到落地。点击任意条目跳转。</p>
    </div>
    <ol class="agenda rv">
      <li class="agenda__i"><a class="agenda__a" href="#s1">
        <span class="agenda__n">01</span>
        <span><span class="agenda__t">范式跃迁</span>
          <div class="agenda__d">从 Chatbot 到 Autonomous Agent</div></span>
        <span class="agenda__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a></li>
      <li class="agenda__i"><a class="agenda__a" href="#s2">
        <span class="agenda__n">02</span>
        <span><span class="agenda__t">形态与边界</span>
          <div class="agenda__d">三类形态与能力边界</div></span>
        <span class="agenda__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a></li>
      <li class="agenda__i"><a class="agenda__a" href="#s3">
        <span class="agenda__n">03</span>
        <span><span class="agenda__t">落地路径</span>
          <div class="agenda__d">采纳率四季度爬升</div></span>
        <span class="agenda__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a></li>
      <li class="agenda__i"><a class="agenda__a" href="#refs">
        <span class="agenda__n">04</span>
        <span><span class="agenda__t">参考资料</span>
          <div class="agenda__d">数据来源与口径说明</div></span>
        <span class="agenda__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a></li>
    </ol>
  </div>
</section>

<!-- ══ 章节一（要点卡） ══ -->
<section class="band" id="s1">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">01 · 范式跃迁</div>
      <h2 class="t-h1 shead__title">范式跃迁：智能体的本质是目标驱动的自主执行</h2>
      <p class="t-lead shead__desc">范式为什么现在发生：成本、能力、生态三线交汇。</p>
    </div>
    <div class="grid g-3 rv">
      <div class="card">
        <div class="card__hd">
          <div class="card__ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 9h6v6H9z"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg></div>
          <h3 class="t-h3">从工具到同事</h3>
        </div>
        <ul class="ul">
          <li><strong>执行者换位。</strong>人从执行者变成目标设定者与审核者。</li>
          <li><strong>闭环标志。</strong>给目标即可闭环，过程自主。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card__hd">
          <div class="card__ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 7l-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/></svg></div>
          <h3 class="t-h3">试点率过六成</h3>
        </div>
        <ul class="ul">
          <li><strong>2025 基线。</strong>61% 企业已进入试点<a class="cite" href="#ref-1">[1]</a>。</li>
          <li><strong>规模化不足两成。</strong>分水岭在治理与集成<a class="cite" href="#ref-2">[2]</a>。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card__hd">
          <div class="card__ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg></div>
          <h3 class="t-h3">护栏先行</h3>
        </div>
        <ul class="ul">
          <li><strong>权限与审计。</strong>智能体操作全程留痕。</li>
          <li><strong>回退机制。</strong>高风险动作必须有人工确认。</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ══ 章节二（表格） ══ -->
<section class="band" id="s2">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">02 · 形态与边界</div>
      <h2 class="t-h1 shead__title">三类形态能力边界分明，同事级智能体尚在早期</h2>
    </div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th style="width:20%">能力</th><th style="width:40%">2026 现状</th><th>跃迁目标</th></tr></thead>
        <tbody>
          <tr><td class="k">任务自主性</td><td>单点工具为主，人逐步驱动</td>
              <td><strong>目标驱动，端到端</strong><a class="cite" href="#ref-1">[1]</a></td></tr>
          <tr><td class="k">工具生态</td><td>连接数少、缺乏统一编排</td>
              <td><strong>统一编排，千级工具</strong></td></tr>
          <tr><td class="k">记忆与规划</td><td>会话级记忆，无长期规划</td>
              <td><strong>任务级记忆，多步规划</strong></td></tr>
          <tr><td class="k">安全治理</td><td>事后审计、无回退</td>
              <td><strong>护栏内运行，全程可回退</strong><a class="cite" href="#ref-2">[2]</a></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ══ 章节三（图表 + 解读） ══ -->
<section class="band" id="s3">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">03 · 落地路径</div>
      <h2 class="t-h1 shead__title">企业智能体采纳率：四个季度四步走至 60%</h2>
      <p class="t-lead shead__desc">采纳率曲线的三个拐点分别由什么驱动。</p>
    </div>
    <div class="grid g-side rv" style="align-items:center">
      <div class="fig">
        <div class="fig__cap">企业智能体采纳率（试点及以上，%）</div>
        <svg class="chart" data-chart="bar" viewBox="0 0 560 220">
          <line x1="46" y1="170" x2="540" y2="170" class="s-bds" stroke-width="1"/>
          <rect data-anim="grow" x="60"  y="131" width="58" height="39"  rx="6" class="f-s3"/>
          <rect data-anim="grow" x="188" y="92"  width="58" height="78"  rx="6" class="f-s3"/>
          <rect data-anim="grow" x="316" y="60"  width="58" height="110" rx="6" class="f-acc"/>
          <rect data-anim="grow" x="444" y="53"  width="58" height="117" rx="6" class="f-acc"/>
          <text data-anim="fade" x="89"  y="192" text-anchor="middle" class="f-txt3" font-size="11">2026Q3</text>
          <text data-anim="fade" x="217" y="192" text-anchor="middle" class="f-txt3" font-size="11">Q4</text>
          <text data-anim="fade" x="345" y="192" text-anchor="middle" class="f-txt3" font-size="11">2027Q1</text>
          <text data-anim="fade" x="473" y="192" text-anchor="middle" class="f-txt3" font-size="11">Q2</text>
        </svg>
      </div>
      <div class="stack gap-4">
        <h3 class="t-h3">怎么读这张图</h3>
        <ul class="ul">
          <li><strong>试点先行。</strong>六成企业已越过 PoC<a class="cite" href="#ref-1">[1]</a>。</li>
          <li><strong>规模化受阻。</strong>瓶颈在治理与集成，不在模型<a class="cite" href="#ref-2">[2]</a>。</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ══ 章节四（对比页 comparison） ══ -->
<section class="band" id="s4">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">03 · 落地路径</div>
      <h2 class="t-h1 shead__title">从试点到规模化：两条路径的分野</h2>
    </div>
    <div class="grid g-half rv">
      <div class="card">
        <h3 class="t-h3">堆场景路径 · 现状</h3>
        <ul class="ul">
          <li><strong>接入慢。</strong>每场景重复对接工具与权限。</li>
          <li><strong>治理弱。</strong>事后审计，回退靠人工。</li>
          <li><strong>易回退。</strong>23 家中 19 家半年内退回试点<a class="cite" href="#ref-2">[2]</a>。</li>
        </ul>
      </div>
      <div class="card" style="background:var(--accent-soft);border-color:transparent">
        <h3 class="t-h3" style="color:var(--accent)">平台化路径 · 目标</h3>
        <ul class="ul">
          <li><strong>接入快。</strong>统一编排，接入成本降一个量级。</li>
          <li><strong>治理内嵌。</strong>权限、审计、回退进平台层。</li>
          <li><strong>可放量。</strong>先行 9 家全部穿越分水岭<a class="cite" href="#ref-2">[2]</a>。</li>
        </ul>
      </div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">结论</span>
      <span class="sowhat__v">平台化不是可选项，而是规模化穿越分水岭的唯一共同路径。</span>
    </div>
  </div>
</section>

<!-- ══ 章节五（大数指标页 kpi） ══ -->
<section class="band" id="s5">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">04 · 落地路径</div>
      <h2 class="t-h1 shead__title">六成企业已越过 PoC，规模化不足两成</h2>
    </div>
    <div class="grid g-side rv" style="align-items:center">
      <div class="stack gap-3">
        <div class="t-metric" style="color:var(--accent);font-size:clamp(56px,7vh,76px)">61%</div>
        <div class="t-h3">2025 企业智能体试点率</div>
        <div class="t-sm" style="color:var(--accent);font-weight:600">▲ +6pt vs 2024</div>
      </div>
      <div class="grid g-3">
        <div class="metric">
          <div class="metric__v t-metric">18<small>%</small></div>
          <div class="metric__k">规模化运行占比</div>
          <div class="metric__n">3 个以上场景稳定运行<a class="cite" href="#ref-2">[2]</a></div>
        </div>
        <div class="metric">
          <div class="metric__v t-metric">9<small> 家</small></div>
          <div class="metric__k">规模化成功企业</div>
          <div class="metric__n">全部先建平台层</div>
        </div>
        <div class="metric">
          <div class="metric__v t-metric">60<small>%</small></div>
          <div class="metric__k">2027Q2 采纳率目标</div>
          <div class="metric__n">四个季度四步走</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ══ 章节六（环形图页 donut） ══ -->
<section class="band" id="s6">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">04 · 落地路径</div>
      <h2 class="t-h1 shead__title">试点企业分布：过六成跨越 PoC</h2>
    </div>
    <div class="grid g-side rv" style="align-items:center">
      <div class="fig">
        <div class="fig__cap">2025 企业智能体成熟度分布（%）</div>
        <svg class="chart" data-chart="donut" viewBox="0 0 150 150" style="width:200px;margin-inline:auto">
          <circle cx="75" cy="75" r="54" class="f-none s-bds" stroke-width="26"/>
          <circle cx="75" cy="75" r="54" class="f-acc" stroke-width="26"
                  stroke-dasharray="61.1 278.2" transform="rotate(-90 75 75)"><title>已规模化 18%</title></circle>
          <circle cx="75" cy="75" r="54" class="f-accs" stroke-width="26"
                  stroke-dasharray="145.9 193.4" transform="rotate(-25.2 75 75)"><title>试点中 43%</title></circle>
          <circle cx="75" cy="75" r="54" class="f-s2" stroke-width="26"
                  stroke-dasharray="132.3 207" transform="rotate(129.6 75 75)"><title>观望 39%</title></circle>
          <text x="75" y="72" text-anchor="middle" class="f-txt" font-size="22" font-weight="600">100%</text>
          <text x="75" y="92" text-anchor="middle" class="f-txt3" font-size="10">企业占比</text>
        </svg>
      </div>
      <div class="stack gap-3">
        <div class="row" style="gap:var(--sp-4)">
          <span class="chip chip--accent">已规模化 18%</span>
          <span class="chip">试点中 43%</span>
          <span class="chip chip--line">观望 39%</span>
        </div>
        <ul class="ul">
          <li><strong>规模化仍是少数。</strong>18% 企业进入 3 场景以上稳定运行<a class="cite" href="#ref-2">[2]</a>。</li>
          <li><strong>观望盘最大。</strong>工具链与治理成熟后向试点迁移。</li>
        </ul>
      </div>
    </div>
    <div class="t-xs" style="margin-top:var(--sp-4);color:var(--text-3)">口径：试点及以上 = 61%；N=42 深度访谈 + 行业抽样<a class="cite" href="#ref-1">[1]</a></div>
  </div>
</section>

<!-- ══ 章节七（步骤条页 steps） ══ -->
<section class="band" id="s7">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">05 · 落地节奏</div>
      <h2 class="t-h1 shead__title">四步走：从单场景试点到平台化放量</h2>
    </div>
    <div class="steps rv">
      <div class="step">
        <div class="step__n">01</div>
        <div class="step__t">选场景</div>
        <div class="step__d">客服 / 研发 / 数据三类高价值场景先跑通</div>
      </div>
      <div class="step">
        <div class="step__n">02</div>
        <div class="step__t">建平台</div>
        <div class="step__d">三层解耦 + 统一编排，接入成本降一个量级</div>
      </div>
      <div class="step step--a">
        <div class="step__n">03</div>
        <div class="step__t">立治理</div>
        <div class="step__d">权限、审计、回退进平台层，高风险动作人工确认</div>
      </div>
      <div class="step">
        <div class="step__n">04</div>
        <div class="step__t">放量复制</div>
        <div class="step__d">同一套护栏复制到新场景，无需重建</div>
      </div>
    </div>
    <div class="t-xs" style="margin-top:var(--sp-5);color:var(--text-3)">口径：先行 9 家规模化企业的共同路径<a class="cite" href="#ref-2">[2]</a></div>
  </div>
</section>

<!-- ══ 章节八（达成对比页 bullet） ══ -->
<section class="band" id="s8">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">06 · 目标对照</div>
      <h2 class="t-h1 shead__title">四项能力对照目标：治理与集成缺口最大</h2>
    </div>
    <div class="bul rv" style="--bul-label:minmax(0,2.4fr)">
      <div class="bul__row">
        <div class="bul__k">场景覆盖</div>
        <div class="bul__track"><div class="bul__fill" style="width:61%"></div>
          <div class="bul__tgt" style="left:80%"></div></div>
        <div class="bul__v"><b>61%</b> / 80%</div>
      </div>
      <div class="bul__row bul__row--warn">
        <div class="bul__k">治理就绪</div>
        <div class="bul__track"><div class="bul__fill" style="width:34%"></div>
          <div class="bul__tgt" style="left:75%"></div></div>
        <div class="bul__v"><b>34%</b> / 75%</div>
      </div>
      <div class="bul__row bul__row--warn">
        <div class="bul__k">工具集成</div>
        <div class="bul__track"><div class="bul__fill" style="width:42%"></div>
          <div class="bul__tgt" style="left:70%"></div></div>
        <div class="bul__v"><b>42%</b> / 70%</div>
      </div>
      <div class="bul__row">
        <div class="bul__k">规模化运行</div>
        <div class="bul__track"><div class="bul__fill" style="width:18%"></div>
          <div class="bul__tgt" style="left:60%"></div></div>
        <div class="bul__v"><b>18%</b> / 60%</div>
      </div>
    </div>
    <div class="t-xs" style="margin-top:var(--sp-5);color:var(--text-3)">口径：能力就绪度 = 自评「已具备且稳定运行」的企业占比；目标取 2027Q2<a class="cite" href="#ref-2">[2]</a></div>
  </div>
</section>

<!-- ══ 章节八b（卡片网格 cards · 路标图标） ══ -->
<section class="band" id="s-cards">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">06 · 能力地图</div>
      <h2 class="t-h1 shead__title">平台化三件套：编排、记忆、治理缺一不可</h2>
    </div>
    <div class="grid g-3 rv">
      <div class="card">
        <div class="card__hd">
          <div class="card__ico">01</div>
          <h3 class="t-h3">统一编排</h3>
        </div>
        <ul class="ul">
          <li><strong>工具连接。</strong>千级工具统一注册与调用。</li>
          <li><strong>任务拆解。</strong>多步规划与失败重试。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card__hd">
          <div class="card__ico">02</div>
          <h3 class="t-h3">长期记忆</h3>
        </div>
        <ul class="ul">
          <li><strong>任务记忆。</strong>跨会话保留目标与进度。</li>
          <li><strong>偏好学习。</strong>组织口径与风格沉淀。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card__hd">
          <div class="card__ico">03</div>
          <h3 class="t-h3">护栏治理</h3>
        </div>
        <ul class="ul">
          <li><strong>权限分级。</strong>高风险动作人工确认。</li>
          <li><strong>全程可回退。</strong>审计与回滚内嵌平台层。</li>
        </ul>
      </div>
    </div>
    <div class="t-xs" style="margin-top:var(--sp-4);color:var(--text-3)">口径：先行 9 家规模化企业的共同能力底座<a class="cite" href="#ref-2">[2]</a></div>
  </div>
</section>

<!-- ══ 素材图片页（image 页型 · full 版心全宽 3:1 + 配图占位） ══ -->
<section class="band" id="s-photo">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">07 · 场景实拍</div>
      <h2 class="t-h1 shead__title">客服智能体工作台：会话、工具调用与人工接管同屏</h2>
    </div>
    <figure class="media media--r3-1 media--ph rv">
      <div class="media__ph">
        <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="m3 18 5-5 4 3.4 3-2.6 6 5.2"/></svg>
        <b>配图占位</b>
        <span>建议 2400×800px · 3:1 · 替换 image.src 即可</span>
      </div>
    </figure>
    <p class="media__src">图 1：客服智能体工作台（占位示例；交付前替换为真实截图，版式与比例已锁定）<a class="cite" href="#ref-2">[2]</a></p>
  </div>
</section>

<!-- ══ 金句页（quote 页型 · 节奏休止 · 全文 1–2 处） ══ -->
<section class="band band--accent band--fit" id="quote-1">
  <div class="wrap">
    <div class="shead shead--center rv">
      <div class="t-eyebrow">03 · 关键判断</div>
      <h2 class="t-h1 shead__title">规模化瓶颈不在模型，而在治理与集成</h2>
      <div style="font-size:clamp(40px,4.6vh,56px);font-weight:700;color:var(--accent);line-height:1;margin-top:var(--sp-4)">「</div>
      <p class="t-lead" style="max-width:860px;margin-inline:auto;color:var(--text);font-size:clamp(18px,2.2vh,22px);font-weight:600">穿越分水岭的钥匙是平台化，不是更大的模型。</p>
      <p class="t-sm" style="margin-top:var(--sp-4);color:var(--accent-text)">—— 企业智能体发展调研 · 42 家深度访谈</p>
    </div>
  </div>
</section>

<!-- ══ 深色收尾章 ══ -->
<section class="band band--accent band--fit" id="next">
  <div class="wrap">
    <div class="shead shead--center rv">
      <div class="t-eyebrow">下一步</div>
      <h2 class="t-h1 shead__title">让智能体真正干活起来</h2>
      <p class="t-lead shead__desc">三步走的行动清单。</p>
    </div>
    <div class="grid g-3 rv">
      <div class="card">
        <h3 class="t-h3" style="margin-bottom:var(--sp-2)">选场景</h3>
        <p class="t-body">
          客服 / 研发 / 数据三类高价值场景。</p>
      </div>
      <div class="card">
        <h3 class="t-h3" style="margin-bottom:var(--sp-2)">建平台</h3>
        <p class="t-body">
          三层解耦 + 统一编排 + 护栏。</p>
      </div>
      <div class="card">
        <h3 class="t-h3" style="margin-bottom:var(--sp-2)">立治理</h3>
        <p class="t-body">
          权限、审计、回退全闭环。</p>
      </div>
    </div>
    <div class="row" style="justify-content:center;gap:var(--sp-3);
         margin-top:clamp(28px,3.4vh,44px);flex-wrap:wrap">
      <a class="btn btn--primary" href="#s1">返回查看</a>
      <a class="btn btn--ghost" href="#refs"
         style="border-color:color-mix(in srgb,var(--text-inv) 30%,transparent)">
        参考资料</a>
    </div>
  </div>
</section>

<!-- ══ 参考资料 ══ -->
<section class="band band--tint" id="refs">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">参考资料</div>
      <h2 class="t-h1 shead__title">数据来源与口径说明</h2>
    </div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th style="width:6%">编号</th><th style="width:26%">来源</th>
          <th style="width:14%">时间</th><th>口径说明</th></tr></thead>
        <tbody>
          <tr id="ref-1"><td class="k">[1]</td>
            <td><a class="ref-link" href="https://example.com/gartner-agentic-ai" target="_blank" rel="noopener">Gartner：Agentic AI 技术成熟度曲线
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><path d="M15 3h6v6M10 14 21 3"/></svg></a></td>
            <td>2026-06</td><td>试点率 / 采纳率 / 形态成熟度判定</td></tr>
          <tr id="ref-2"><td class="k">[2]</td><td>企业智能体发展调研（内部，N=42）</td>
            <td>2026-08</td><td>规模化占比与访谈结论，2026-07 至 2026-08</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ══ 页脚 ══ -->
<footer class="foot">
  <div class="wrap foot__in">
    <div class="brand">
      <div class="brand__mark">AI</div>
      <div class="brand__txt">
        <div class="brand__title">AI 智能体发展研究</div>
        <div class="brand__sub">2026 · 年度报告</div>
      </div>
    </div>
    <div class="t-xs">内部资料 · 请勿外传</div>
  </div>
</footer>'''

P_MODEL = {
    "mode": "presentation", "style": "business-blue",
    "title": "AI 智能体：从工具到同事",
    "subtitle": "从工具到同事 · 台上宣讲版",
    "meta": "宣讲材料 · " + DATE,
    "agenda": [
        ["01", "范式跃迁", "从 Chatbot 到 Autonomous Agent"],
        ["02", "形态与边界", "三类形态与能力边界"],
        ["03", "落地路径", "采纳率四季度爬升"],
        ["04", "参考资料", "数据来源与口径说明"],
    ],
    "sections": [
        {"type": "points", "eyebrow": "01 · 范式跃迁", "title": "范式跃迁：智能体的本质是目标驱动的自主执行",
         "points": [["从工具到同事", "人从执行者变成目标设定者与审核者"],
                    ["试点率过六成", "61% 企业已进入试点，规模化不足两成"],
                    ["护栏先行", "权限与审计内嵌，高风险动作人工确认"]],
         "metrics": [["61%", "2025 企业试点率[1]"], ["18%", "规模化运行占比[2]"]]},
        {"type": "table", "eyebrow": "02 · 形态与边界", "title": "三类形态能力边界分明，同事级智能体尚在早期",
         "table": {"head": ["能力", "2026 现状", "跃迁目标"],
                   "rows": [["任务自主性", "单点工具为主，人逐步驱动", "目标驱动，端到端"],
                            ["工具生态", "连接数少、缺乏统一编排", "统一编排，千级工具"],
                            ["记忆与规划", "会话级记忆，无长期规划", "任务级记忆，多步规划"],
                            ["安全治理", "事后审计、无回退", "护栏内运行，全程可回退"]]}},
        {"type": "bar", "eyebrow": "03 · 落地路径", "title": "企业智能体采纳率：四个季度四步走至 60%",
         "chart": {"labels": ["2026Q3", "Q4", "2027Q1", "Q2"], "values": [30, 45, 55, 60], "max": 100, "unit": "%"},
         "note": "口径：试点及以上的企业占比[1]"},
        {"type": "comparison", "eyebrow": "03 · 落地路径", "title": "从试点到规模化：两条路径的分野",
         "left": {"title": "堆场景路径 · 现状",
                  "points": [["接入慢", "每场景重复对接工具与权限"],
                             ["治理弱", "事后审计，回退靠人工"],
                             ["易回退", "23 家中 19 家半年内退回试点"]]},
         "right": {"title": "平台化路径 · 目标",
                   "points": [["接入快", "统一编排，接入成本降一个量级"],
                              ["治理内嵌", "权限、审计、回退进平台层"],
                              ["可放量", "先行 9 家全部穿越分水岭"]]},
         "verdict": "平台化不是可选项，而是规模化穿越分水岭的唯一共同路径。"},
        {"type": "kpi", "eyebrow": "04 · 落地路径", "title": "六成企业已越过 PoC，规模化不足两成",
         "hero": ["61%", "2025 企业智能体试点率", "+6pt vs 2024"],
         "metrics": [["18%", "规模化运行占比，3 场景以上"],
                     ["9 家", "规模化成功企业，全部先建平台层"],
                     ["60%", "2027Q2 采纳率目标"]]},
        {"type": "donut", "eyebrow": "04 · 落地路径", "title": "试点企业分布：过六成跨越 PoC",
         "chart": {"labels": ["已规模化", "试点中", "观望"], "values": [18, 43, 39],
                   "unit": "%", "centerLabel": "企业占比"},
         "note": "口径：试点及以上 = 61%；N=42 深度访谈 + 行业抽样[1]"},
        {"type": "quote", "eyebrow": "03 · 关键判断", "title": "规模化瓶颈不在模型，而在治理与集成",
         "quote": "穿越分水岭的钥匙是平台化，不是更大的模型。",
         "author": "企业智能体发展调研 · 42 家深度访谈"},
        {"type": "steps", "eyebrow": "05 · 落地节奏", "title": "四步走：从单场景试点到平台化放量",
         "steps": [["选场景", "客服 / 研发 / 数据三类高价值场景先跑通"],
                   ["建平台", "三层解耦 + 统一编排，接入成本降一个量级"],
                   {"t": "立治理", "d": "权限、审计、回退进平台层，高风险动作人工确认", "accent": True},
                   ["放量复制", "同一套护栏复制到新场景，无需重建"]],
         "footnote": "口径：先行 9 家规模化企业的共同路径[2]"},
        {"type": "bullet", "eyebrow": "06 · 目标对照", "title": "四项能力对照目标：治理与集成缺口最大",
         "items": [["场景覆盖", 61, 80], ["治理就绪", 34, 75], ["工具集成", 42, 70], ["规模化运行", 18, 60]],
         "unit": "%", "max": 100,
         "footnote": "口径：能力就绪度 = 自评「已具备且稳定运行」的企业占比；目标取 2027Q2[2]"},
        {"type": "cards", "eyebrow": "06 · 能力地图", "title": "平台化三件套：编排、记忆、治理缺一不可",
         "cards": [
           {"title": "统一编排", "points": ["工具连接：千级工具统一注册与调用", "任务拆解：多步规划与失败重试"]},
           {"title": "长期记忆", "points": ["任务记忆：跨会话保留目标与进度", "偏好学习：组织口径与风格沉淀"]},
           {"title": "护栏治理", "points": ["权限分级：高风险动作人工确认", "全程可回退：审计与回滚内嵌平台层"]},
         ],
         "columns": 3,
         "footnote": "口径：先行 9 家规模化企业的共同能力底座[2]"},
        {"type": "image", "eyebrow": "07 · 场景实拍",
         "title": "客服智能体工作台：会话、工具调用与人工接管同屏",
         "image": {"placeholder": True, "layout": "full",
                   "caption": "图 1：客服智能体工作台（占位示例；交付前替换为真实截图）",
                   "hint": "建议 2400×800px（3:1）真实截图；把 image.placeholder 改为 image.src 即可"}},
    ],
    "closing": {"title": "让智能体真正干活起来",
                "points": [["选场景", "客服 / 研发 / 数据三类高价值场景"],
                           ["建平台", "三层解耦 + 统一编排 + 护栏"],
                           ["立治理", "权限、审计、回退全闭环"]]},
}

# ══════════════════════════════════════════════════════════════════════════
#  内容包 · 研究报告（research）《2026 AI 智能体发展研究报告》
# ══════════════════════════════════════════════════════════════════════════
R_CONTENT = '''<!-- ══ 封面页（研究版：紧凑单列，结论前置） ══ -->
<section class="band band--fit">
  <div class="wrap">
    <div class="stack gap-5 rv" style="max-width:880px">
      <div class="row row-wrap" style="gap:var(--sp-3)">
        <span class="chip chip--accent">研究报告</span>
        <span class="chip chip--line">2026 · 年度</span>
      </div>
      <h1 class="t-display">2026 AI 智能体<br>规模化前夜</h1>
      <p class="t-lead" style="max-width:720px">六成企业已在试点，规模化运行不足两成——分水岭已经出现，治理与集成才是真正的门槛。</p>
      <div class="row row-wrap" style="gap:var(--sp-6)">
        <div>
          <div class="t-metric" style="color:var(--accent)">61%</div>
          <div class="t-xs" style="margin-top:4px">2025 企业试点率<a class="cite" href="#ref-1">[1]</a></div>
        </div>
        <div>
          <div class="t-metric">18%</div>
          <div class="t-xs" style="margin-top:4px">规模化运行占比<a class="cite" href="#ref-2">[2]</a></div>
        </div>
        <div>
          <div class="t-metric">42</div>
          <div class="t-xs" style="margin-top:4px">深度访谈样本（家）</div>
        </div>
      </div>
      <div class="t-xs" style="color:var(--text-3)">内部研究资料 · ''' + DATE + ''' · 覆盖金融 / 制造 / 互联网，2026-07 至 2026-08 访谈</div>
    </div>
  </div>
</section>

<!-- ══ Agenda（研究模式 12–25 页；双列） ══ -->
<section class="band band--tint" id="agenda">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">Agenda</div>
      <h2 class="t-h1 shead__title">报告大纲</h2>
      <p class="t-lead shead__desc">五章加参考资料，从范式到放量顺序。点击任意条目跳转。</p>
    </div>
    <ol class="agenda agenda--2col rv">
      <li class="agenda__i"><a class="agenda__a" href="#s1">
        <span class="agenda__n">01</span>
        <span><span class="agenda__t">范式与分水岭</span>
          <div class="agenda__d">从 Chatbot 到 Autonomous Agent</div></span>
        <span class="agenda__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a></li>
      <li class="agenda__i"><a class="agenda__a" href="#s2">
        <span class="agenda__n">02</span>
        <span><span class="agenda__t">形态与边界</span>
          <div class="agenda__d">三类形态与能力边界</div></span>
        <span class="agenda__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a></li>
      <li class="agenda__i"><a class="agenda__a" href="#s3">
        <span class="agenda__n">03</span>
        <span><span class="agenda__t">域间差异</span>
          <div class="agenda__d">试点率的行业分化与互证</div></span>
        <span class="agenda__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a></li>
      <li class="agenda__i"><a class="agenda__a" href="#s5">
        <span class="agenda__n">04</span>
        <span><span class="agenda__t">落地路径</span>
          <div class="agenda__d">平台化先行四步走</div></span>
        <span class="agenda__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a></li>
      <li class="agenda__i"><a class="agenda__a" href="#s7">
        <span class="agenda__n">05</span>
        <span><span class="agenda__t">风险与治理</span>
          <div class="agenda__d">三重门槛与优先级矩阵</div></span>
        <span class="agenda__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a></li>
      <li class="agenda__i"><a class="agenda__a" href="#refs">
        <span class="agenda__n">06</span>
        <span><span class="agenda__t">参考资料</span>
          <div class="agenda__d">数据来源与口径说明</div></span>
        <span class="agenda__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
      </a></li>
    </ol>
  </div>
</section>

<!-- ══ R1 论证页：范式与分水岭 ══ -->
<section class="band" id="s1">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">01 · 范式与分水岭</div>
      <h2 class="t-h1 shead__title">六成企业试点卡在治理与集成——规模化分水岭已经出现</h2>
    </div>
    <div class="cols-2 rv">
      <p class="t-body"><strong>发现。</strong>2025 年全球企业智能体试点率 61%，规模化运行仅 18%，两者相差 43 个百分点<a class="cite" href="#ref-1">[1]</a>。</p>
      <p class="t-body"><strong>证据。</strong>42 家深度访谈企业中，37 家把「权限不清、系统难接」列为放弃规模化的首因<a class="cite" href="#ref-2">[2]</a>。</p>
      <p class="t-body"><strong>含义。</strong>瓶颈不在模型能力，而在治理、权限与系统集成——继续堆参数无助于穿越分水岭。</p>
      <p class="t-body"><strong>推论。</strong>平台化先行：统一编排与护栏到位后，场景再分层放量，顺序反了会被治理拖死。</p>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">先建平台与护栏，再放场景——顺序反了会被治理拖死。</span>
    </div>
    <div class="footnote">注：试点率 = 已进入试点及以上的企业占比；规模化 = 3 个以上场景稳定运行。来源见
      <a class="cite" href="#ref-1">[1]</a><a class="cite" href="#ref-2">[2]</a>。</div>
  </div>
</section>

<!-- ══ R3 密表页：形态与边界 ══ -->
<section class="band" id="s2">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">02 · 形态与边界</div>
      <h2 class="t-h1 shead__title">三类形态能力边界分明，同事级智能体尚在早期</h2>
    </div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th style="width:14%">形态</th><th style="width:26%">自主性</th><th style="width:24%">工具生态</th><th style="width:16%">成熟度</th><th>结论</th></tr></thead>
        <tbody>
          <tr><td class="k">助理级</td><td>单轮任务，人逐步驱动</td><td>少量插件</td><td>规模可用</td>
              <td><strong>当前主力</strong><a class="cite" href="#ref-1">[1]</a></td></tr>
          <tr><td class="k">流程级</td><td>固定流程多步执行</td><td>数十工具编排</td><td>试点爬坡</td>
              <td><strong>2026 焦点</strong></td></tr>
          <tr><td class="k">同事级</td><td>目标驱动，端到端</td><td>千级工具生态</td><td><span class="tbd">早期验证</span></td>
              <td><strong>三年后</strong><a class="cite" href="#ref-2">[2]</a></td></tr>
        </tbody>
      </table>
    </div>
    <div class="footnote">注：形态判定口径见参考资料 [1]；同事级判定基于访谈专家评分（N=42）。</div>
    <!-- 待核实标注（accent 强调色）：无法核实的判断用 .tbd 内联标色 + .flagbar 清单收口，提示二次确认 -->
    <div class="flagbar rv">
      <div class="flagbar__hd">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></svg>
        待核实 · 需二次确认
      </div>
      <ul>
        <li>同事级成熟度评分口径待与业务方确认，正式版请替换 <span class="tbd">xx%</span></li>
        <li>「三年后」时间窗来自访谈主观判断，需以官方路线图数据复核</li>
      </ul>
    </div>
  </div>
</section>

<!-- ══ R2 Exhibit 页：域间差异 ══ -->
<section class="band" id="s3">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">03 · 域间差异</div>
      <h2 class="t-h1 shead__title">客服域一马当先，研发域势能最大——域间分化明显</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 1</span>
        <span class="exhibit__t">各业务域智能体试点率对比</span>
      </div>
      <svg class="chart" data-chart="hbar" viewBox="0 0 520 210">
        <text x="0" y="18" class="f-txt2" font-size="12">客服</text>
        <rect x="80" y="7" width="360" height="15" rx="7.5" class="f-s2"/>
        <rect x="80" y="7" width="259" height="15" rx="7.5" class="f-acc"/>
        <text x="450" y="19" text-anchor="end" class="f-txt" font-size="12" font-weight="600">72%</text>
        <text x="0" y="63" class="f-txt2" font-size="12">财务</text>
        <rect x="80" y="52" width="360" height="15" rx="7.5" class="f-s2"/>
        <rect x="80" y="52" width="205" height="15" rx="7.5" class="f-acc"/>
        <text x="450" y="64" text-anchor="end" class="f-txt" font-size="12" font-weight="600">57%</text>
        <text x="0" y="108" class="f-txt2" font-size="12">营销</text>
        <rect x="80" y="97" width="360" height="15" rx="7.5" class="f-s2"/>
        <rect x="80" y="97" width="173" height="15" rx="7.5" class="f-acc"/>
        <text x="450" y="109" text-anchor="end" class="f-txt" font-size="12" font-weight="600">48%</text>
        <text x="0" y="153" class="f-txt2" font-size="12">研发</text>
        <rect x="80" y="142" width="360" height="15" rx="7.5" class="f-s2"/>
        <rect x="80" y="142" width="137" height="15" rx="7.5" class="f-acc"/>
        <text x="450" y="154" text-anchor="end" class="f-txt" font-size="12" font-weight="600">38%</text>
      </svg>
      <div class="exhibit__src">来源：企业智能体发展调研，2026-08；试点率 = 已进入试点及以上的企业占比</div>
    </div>
    <ul class="ul ul--ico rv" style="margin-top:var(--sp-5)">
      <li>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 7l-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/></svg>
        <strong>客服领跑。</strong>流程标准、容错高，天然适配智能体。
      </li>
      <li>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3"/></svg>
        <strong>研发垫底但增速最快。</strong>工具链补齐后弹性最大<a class="cite" href="#ref-2">[2]</a>。
      </li>
    </ul>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">研发域渗透最浅但势能最大，工具链成熟后有望一年内反超客服域。</span>
    </div>
  </div>
</section>

<!-- ══ R7 半表半图页：域间互证 ══ -->
<section class="band" id="s4">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">03 · 域间差异</div>
      <h2 class="t-h1 shead__title">试点率与增幅互证：研发域一年内有望反超</h2>
    </div>
    <div class="grid g-half rv">
      <div class="tbl-wrap">
        <table>
          <thead><tr><th style="width:30%">业务域</th><th>试点率</th><th>同比增幅</th></tr></thead>
          <tbody>
            <tr><td class="k">客服</td><td class="num">72%</td><td><strong>+9pt</strong></td></tr>
            <tr><td class="k">财务</td><td class="num">57%</td><td><strong>+11pt</strong></td></tr>
            <tr><td class="k">营销</td><td class="num">48%</td><td><strong>+13pt</strong></td></tr>
            <tr><td class="k">研发</td><td class="num">38%</td><td><strong>+15pt</strong></td></tr>
          </tbody>
        </table>
      </div>
      <div class="exhibit">
        <div class="exhibit__hd">
          <span class="exhibit__no">Exhibit 2</span>
          <span class="exhibit__t">各域试点率同比增幅（百分点）</span>
        </div>
        <svg class="chart" data-chart="bar" viewBox="0 0 480 190">
          <line x1="60" y1="150" x2="430" y2="150" class="s-bds" stroke-width="1"/>
          <rect data-anim="grow" x="90"  y="88" width="56" height="62"  rx="5" class="f-s3"/>
          <rect data-anim="grow" x="180" y="74" width="56" height="76"  rx="5" class="f-s3"/>
          <rect data-anim="grow" x="270" y="61" width="56" height="89"  rx="5" class="f-acc"/>
          <rect data-anim="grow" x="360" y="47" width="56" height="103" rx="5" class="f-acc"/>
          <text data-anim="fade" x="118" y="80" text-anchor="middle" class="f-txt3" font-size="11">+9pt</text>
          <text data-anim="fade" x="208" y="66" text-anchor="middle" class="f-txt3" font-size="11">+11pt</text>
          <text data-anim="fade" x="298" y="53" text-anchor="middle" class="f-txt3" font-size="11">+13pt</text>
          <text data-anim="fade" x="388" y="39" text-anchor="middle" class="f-txt" font-size="11" font-weight="600">+15pt</text>
          <text x="118" y="172" text-anchor="middle" class="f-txt3" font-size="11">客服</text>
          <text x="208" y="172" text-anchor="middle" class="f-txt3" font-size="11">财务</text>
          <text x="298" y="172" text-anchor="middle" class="f-txt3" font-size="11">营销</text>
          <text x="388" y="172" text-anchor="middle" class="f-txt3" font-size="11">研发</text>
        </svg>
        <div class="exhibit__src">来源：企业智能体发展调研，2026-07 与 2025-07 两期对比</div>
      </div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">增幅与基数负相关，研发域工具链补齐后将进入陡峭爬坡段。</span>
    </div>
  </div>
</section>

<!-- ══ 对比页（comparison）：两条路径结局分野 ══ -->
<section class="band" id="scmp">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">04 · 落地路径</div>
      <h2 class="t-h1 shead__title">堆场景与平台化两条路径的结局分野</h2>
    </div>
    <div class="grid g-half rv">
      <div class="card">
        <h3 class="t-h3">堆场景路径（n=23）</h3>
        <ul class="ul">
          <li><strong>接入慢。</strong>每场景重复对接，平均 11 周上线。</li>
          <li><strong>治理弱。</strong>事后审计，回退靠人工。</li>
          <li><strong>结局。</strong>19 家半年内退回试点<a class="cite" href="#ref-2">[2]</a>。</li>
        </ul>
      </div>
      <div class="card" style="background:var(--accent-soft);border-color:transparent">
        <h3 class="t-h3" style="color:var(--accent)">平台化路径（n=9）</h3>
        <ul class="ul">
          <li><strong>接入快。</strong>统一编排，平均 3 周上线。</li>
          <li><strong>治理内嵌。</strong>权限、审计、回退进平台层。</li>
          <li><strong>结局。</strong>全部穿越分水岭进入放量<a class="cite" href="#ref-2">[2]</a>。</li>
        </ul>
      </div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">平台化把场景接入周期从 11 周压到 3 周，是穿越分水岭的唯一共同路径。</span>
    </div>
  </div>
</section>

<!-- ══ 环形图页（donut）：规模化企业行业分布 ══ -->
<section class="band" id="sdonut">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">04 · 落地路径</div>
      <h2 class="t-h1 shead__title">规模化企业行业分布：制造与金融领跑</h2>
    </div>
    <div class="grid g-side rv" style="align-items:center">
      <div class="fig">
        <div class="fig__cap">9 家规模化企业的行业构成（家）</div>
        <svg class="chart" data-chart="donut" viewBox="0 0 150 150" style="width:190px;margin-inline:auto">
          <circle cx="75" cy="75" r="54" class="f-none s-bds" stroke-width="26"/>
          <circle cx="75" cy="75" r="54" class="f-acc" stroke-width="26"
                  stroke-dasharray="113.1 226.2" transform="rotate(-90 75 75)"><title>制造 3 家</title></circle>
          <circle cx="75" cy="75" r="54" class="f-accs" stroke-width="26"
                  stroke-dasharray="75.4 263.9" transform="rotate(30 75 75)"><title>金融 2 家</title></circle>
          <circle cx="75" cy="75" r="54" class="f-s2" stroke-width="26"
                  stroke-dasharray="150.8 188.5" transform="rotate(110 75 75)"><title>互联网及其他 4 家</title></circle>
          <text x="75" y="72" text-anchor="middle" class="f-txt" font-size="22" font-weight="600">9</text>
          <text x="75" y="92" text-anchor="middle" class="f-txt3" font-size="10">家</text>
        </svg>
      </div>
      <div class="stack gap-3">
        <div class="row" style="gap:var(--sp-4)">
          <span class="chip chip--accent">制造 3</span>
          <span class="chip">金融 2</span>
          <span class="chip chip--line">互联网及其他 4</span>
        </div>
        <ul class="ul">
          <li><strong>制造领跑。</strong>流程标准、容错高，最先穿越分水岭。</li>
          <li><strong>金融紧随。</strong>合规要求倒逼治理内嵌平台层。</li>
        </ul>
      </div>
    </div>
    <div class="footnote">注：行业构成基于 9 家规模化成功企业（N=42 访谈样本）<a class="cite" href="#ref-2">[2]</a>。</div>
  </div>
</section>

<!-- ══ R4 指标带页：落地基线（节奏休止） ══ -->
<section class="band" id="s5">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">04 · 落地路径</div>
      <h2 class="t-h1 shead__title">四组基线数字勾勒出规模化落地现状</h2>
    </div>
    <div class="grid g-4 rv">
      <div class="metric">
        <svg class="metric__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3"/></svg>
        <div class="metric__v t-metric">61<small>%</small></div>
        <div class="metric__k">企业试点率</div>
        <div class="metric__n">2025 年基线<a class="cite" href="#ref-1">[1]</a></div>
      </div>
      <div class="metric">
        <svg class="metric__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 7l-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/></svg>
        <div class="metric__v t-metric">18<small>%</small></div>
        <div class="metric__k">规模化占比</div>
        <div class="metric__n">3 个以上场景稳定运行<a class="cite" href="#ref-2">[2]</a></div>
      </div>
      <div class="metric metric--warn">
        <div class="metric__v t-metric">9<small> 家</small></div>
        <div class="metric__k">规模化成功企业</div>
        <div class="metric__n">全部先建平台层</div>
      </div>
      <div class="metric">
        <div class="metric__v t-metric">60<small>%</small></div>
        <div class="metric__k">2027Q2 采纳率目标</div>
        <div class="metric__n">四个季度四步走</div>
      </div>
    </div>
  </div>
</section>

<!-- ══ R5 分栏证据页：平台化路径 ══ -->
<section class="band" id="s6">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">04 · 落地路径</div>
      <h2 class="t-h1 shead__title">平台化先行是穿越分水岭的共同路径</h2>
    </div>
    <div class="grid g-side rv">
      <div class="cols-2">
        <p class="t-body"><strong>路径。</strong>访谈中规模化成功的 9 家企业，全部先建平台层再放场景。</p>
        <p class="t-body"><strong>机制。</strong>统一编排把工具、记忆、权限收敛到一处，场景接入成本下降一个量级。</p>
        <p class="t-body"><strong>反例。</strong>跳过平台直接堆场景的企业，23 家中 19 家在半年内回退试点<a class="cite" href="#ref-2">[2]</a>。</p>
      </div>
      <div class="exhibit">
        <div class="exhibit__hd">
          <span class="exhibit__no">Exhibit 3</span>
          <span class="exhibit__t">采纳率爬坡：四个季度四步走</span>
        </div>
        <svg class="chart" data-chart="bar" viewBox="0 0 520 200">
          <line x1="40" y1="160" x2="500" y2="160" class="s-bds" stroke-width="1"/>
          <rect data-anim="grow" x="70"  y="120" width="56" height="40"  rx="6" class="f-s3"/>
          <rect data-anim="grow" x="190" y="92"  width="56" height="68"  rx="6" class="f-s3"/>
          <rect data-anim="grow" x="310" y="60"  width="56" height="100" rx="6" class="f-acc"/>
          <rect data-anim="grow" x="430" y="48"  width="56" height="112" rx="6" class="f-acc"/>
          <text data-anim="fade" x="98"  y="180" text-anchor="middle" class="f-txt3" font-size="11">2026Q3</text>
          <text data-anim="fade" x="218" y="180" text-anchor="middle" class="f-txt3" font-size="11">Q4</text>
          <text data-anim="fade" x="338" y="180" text-anchor="middle" class="f-txt3" font-size="11">2027Q1</text>
          <text data-anim="fade" x="458" y="180" text-anchor="middle" class="f-txt3" font-size="11">Q2</text>
        </svg>
        <div class="exhibit__src">来源：企业智能体发展调研，2026-08；口径 = 试点及以上企业占比</div>
      </div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">平台层的投入在四个季度内由采纳率爬坡兑回，不是纯成本。</span>
    </div>
  </div>
</section>

<!-- ══ R6 三栏证据页：三重门槛 ══ -->
<section class="band" id="s7">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">05 · 风险与治理</div>
      <h2 class="t-h1 shead__title">规模化三重门槛：技术可控、组织就绪、经济可行</h2>
    </div>
    <div class="cols-3 rv">
      <p class="t-body"><strong>技术可控。</strong>幻觉率与工具调用成功率决定场景上限，需评测门禁。</p>
      <p class="t-body"><strong>组织就绪。</strong>流程负责人须会拆任务、定验收；缺位的场景一律降级试点。</p>
      <p class="t-body"><strong>经济可行。</strong>单任务成本须低于人工基线 30% 以上，否则不可放量。</p>
      <p class="t-body"><strong>佐证。</strong>成功企业的共同做法是按三重门槛给场景分级放量。</p>
      <p class="t-body"><strong>顺序。</strong>先算经济账再上技术平台——多数失败案例顺序相反。</p>
      <p class="t-body"><strong>结论。</strong>三门槛齐备的场景不足两成，分级放量是唯一理性路径。</p>
    </div>
    <div class="footnote">注：三重门槛口径来自访谈编码（N=42），编码一致性 Kappa=0.81。</div>
  </div>
</section>

<!-- ══ R8 矩阵图页：放量顺序 ══ -->
<section class="band" id="s8">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">05 · 风险与治理</div>
      <h2 class="t-h1 shead__title">高价值低难度场景优先——矩阵给出放量顺序</h2>
    </div>
    <div class="matrix rv">
      <div class="matrix__grid" style="--mx-cols:3">
        <div></div>
        <div class="matrix__h">实施难度 · 低</div>
        <div class="matrix__h">实施难度 · 中</div>
        <div class="matrix__h">实施难度 · 高</div>
        <div class="matrix__rh">业务价值 · 高</div>
        <div class="matrix__c matrix__c--a"><b>客服问数</b>首批放量</div>
        <div class="matrix__c"><b>研发副驾</b>二批放量</div>
        <div class="matrix__c"><b>端到端交付</b>暂缓</div>
        <div class="matrix__rh">业务价值 · 中</div>
        <div class="matrix__c"><b>知识检索</b>常规推进</div>
        <div class="matrix__c"><b>经营预警</b>常规推进</div>
        <div class="matrix__c matrix__c--a"><b>自主决策</b>护栏试点</div>
      </div>
      <div class="matrix__note">图例：强调单元 = 优先投入项；其余按季度节奏推进。价值 / 难度评分口径见参考资料 [2]。</div>
    </div>
  </div>
</section>

<!-- ══ 热力矩阵页（heatmap）：行业 × 能力就绪度 ══ -->
<section class="band" id="s9">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">06 · 行业对标</div>
      <h2 class="t-h1 shead__title">行业就绪度差异显著——金融客服先行，制造研发滞后</h2>
    </div>
    <div class="heat rv">
      <div class="heat__grid" style="--heat-cols:5;--heat-label:132px">
        <div></div>
        <div class="heat__h">客服</div>
        <div class="heat__h">研发</div>
        <div class="heat__h">营销</div>
        <div class="heat__h">供应链</div>
        <div class="heat__h">财务</div>
        <div class="heat__rh">金融</div>
        <div class="heat__c heat__c--3">78<small>高</small></div>
        <div class="heat__c heat__c--1">46<small>中</small></div>
        <div class="heat__c heat__c--2">63<small>中高</small></div>
        <div class="heat__c">38<small>低</small></div>
        <div class="heat__c heat__c--2">61<small>中高</small></div>
        <div class="heat__rh">制造</div>
        <div class="heat__c heat__c--1">44<small>中</small></div>
        <div class="heat__c">29<small>低</small></div>
        <div class="heat__c">33<small>低</small></div>
        <div class="heat__c heat__c--2">57<small>中高</small></div>
        <div class="heat__c">31<small>低</small></div>
        <div class="heat__rh">互联网</div>
        <div class="heat__c heat__c--2">71<small>中高</small></div>
        <div class="heat__c heat__c--3">82<small>高</small></div>
        <div class="heat__c heat__c--2">68<small>中高</small></div>
        <div class="heat__c heat__c--1">49<small>中</small></div>
        <div class="heat__c heat__c--1">52<small>中</small></div>
      </div>
      <div class="heat__legend">
        <span>就绪度</span>
        <span class="heat__sw" style="background:var(--surface-1)"></span>
        <span class="heat__sw" style="background:var(--accent-soft)"></span>
        <span class="heat__sw" style="background:var(--accent-soft-2)"></span>
        <span class="heat__sw" style="background:var(--accent)"></span>
        <span>低 → 高（单位：分）</span>
      </div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">金融客服与互联网研发是两个可复制样板，制造研发域需先补工具链再谈放量。</span>
    </div>
    <div class="footnote">注：就绪度 = 场景 × 行业维度的能力自评加权得分（0–100），N=42 深度访谈 + 行业抽样<a class="cite" href="#ref-2">[2]</a>。</div>
  </div>
</section>

<!-- ══ 金字塔页（pyramid）：价值兑现的四级台阶 ══ -->
<section class="band" id="s10">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">07 · 价值阶梯</div>
      <h2 class="t-h1 shead__title">价值兑现四级台阶：越往上，组织变革成本越高</h2>
    </div>
    <div class="pyr rv">
      <div class="pyr__lvl" style="--w:42%">
        <div class="pyr__t">自主决策</div>
        <div class="pyr__d">自动执行</div>
      </div>
      <div class="pyr__lvl" style="--w:62%">
        <div class="pyr__t">端到端交付</div>
        <div class="pyr__d">跨系统串联多步任务，交付质量可回退</div>
      </div>
      <div class="pyr__lvl pyr__lvl--a" style="--w:82%">
        <div class="pyr__t">副驾协同</div>
        <div class="pyr__d">人机分工明确，效率提升可度量（当前主力）</div>
      </div>
      <div class="pyr__lvl" style="--w:100%">
        <div class="pyr__t">问答与检索</div>
        <div class="pyr__d">知识问答、找数问数，替换成本最低</div>
      </div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">当前主力仍在第二级：把副驾协同做厚，比抢跑自主决策更能兑现价值。</span>
    </div>
    <div class="footnote">注：台阶高度不代表难度，仅表示覆盖范围；accent 层为当前主力形态<a class="cite" href="#ref-1">[1]</a>。</div>
  </div>
</section>

<!-- ══ 原生图表技巧：瀑布图（增减归因） ══ -->
<section class="band" id="s18">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">03 · 域间差异</div>
      <h2 class="t-h1 shead__title">试点率增长归因：工具链补齐贡献过半</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 4</span>
        <span class="exhibit__t">试点率从 2025 基线到 2026 现值的增量归因（百分点）</span>
      </div>
      <svg class="chart" data-chart="waterfall" viewBox="0 0 900 300">
        <line x1="60" y1="250" x2="860" y2="250" class="s-bd"/>
        <rect x="100" y="92" width="70" height="158" class="f-acc"/>
        <text x="135" y="82" text-anchor="middle" class="f-txt" font-size="12" font-weight="600">38pt</text>
        <text x="135" y="272" text-anchor="middle" class="f-txt2" font-size="11">2025 基线</text>
        <rect x="230" y="54" width="70" height="38" class="f-acc"/>
        <text x="265" y="44" text-anchor="middle" class="f-txt" font-size="12" font-weight="600">+9pt</text>
        <text x="265" y="272" text-anchor="middle" class="f-txt2" font-size="11">工具链</text>
        <rect x="360" y="29" width="70" height="25" class="f-acc"/>
        <text x="395" y="19" text-anchor="middle" class="f-txt" font-size="12" font-weight="600">+6pt</text>
        <text x="395" y="272" text-anchor="middle" class="f-txt2" font-size="11">流程改造</text>
        <rect x="490" y="29" width="70" height="13" class="f-s3"/>
        <text x="525" y="19" text-anchor="middle" class="f-txt" font-size="12" font-weight="600">-3pt</text>
        <text x="525" y="272" text-anchor="middle" class="f-txt2" font-size="11">治理</text>
        <rect x="620" y="33" width="70" height="8" class="f-acc"/>
        <text x="655" y="23" text-anchor="middle" class="f-txt" font-size="12" font-weight="600">+2pt</text>
        <text x="655" y="272" text-anchor="middle" class="f-txt2" font-size="11">组织</text>
        <rect x="750" y="33" width="70" height="217" class="f-acc"/>
        <text x="785" y="23" text-anchor="middle" class="f-txt" font-size="12" font-weight="600">52pt</text>
        <text x="785" y="272" text-anchor="middle" class="f-txt2" font-size="11">2026 现值</text>
      </svg>
      <div class="exhibit__src">来源：企业智能体发展调研，2026-08；单位为百分点（pt），按增量归因分解</div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">九个百分点增量里工具链补齐贡献最大、治理不足拖累 3pt——补齐工具链的边际收益最高。</span>
    </div>
    <div class="footnote">注：归因分解基于 42 家访谈企业的自报增量与编码结果，合计等于两期试点率之差。</div>
  </div>
</section>

<!-- ══ 信息图页：桑基图（流向与流量） ══ -->
<section class="band" id="s19">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">04 · 落地路径</div>
      <h2 class="t-h1 shead__title">线索转化流向：初筛环节流失占比近六成</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 5</span>
        <span class="exhibit__t">线索转化流向（带宽 ∝ 流量 · 单位：条）</span>
      </div>
      <svg class="chart" data-chart="sankey" viewBox="0 0 900 300">
        <g class="f-s2" opacity=".85">
          <path d="M140,40 C400,40 460,40 620,40 L620,74 C460,74 400,74 140,74 Z"/>
          <path d="M140,80 C400,80 460,150 620,150 L620,176 C460,176 400,110 140,110 Z"/>
        </g>
        <g class="f-s3" opacity=".85">
          <path d="M140,116 C400,116 460,210 620,210 L620,244 C460,244 400,150 140,150 Z"/>
        </g>
        <g class="f-s1" opacity=".85">
          <path d="M620,40 C740,40 780,60 830,60 L830,150 C780,150 740,74 620,74 Z"/>
        </g>
        <g class="f-acc">
          <rect x="120" y="34" width="18" height="118"/>
          <rect x="620" y="34" width="18" height="216"/>
          <rect x="830" y="52" width="18" height="104"/>
        </g>
        <g class="f-txt2" font-size="12" font-weight="600">
          <text x="112" y="98" text-anchor="end">线索</text>
          <text x="648" y="70">初筛</text>
          <text x="856" y="110">签约</text>
        </g>
        <g class="f-txt3" font-size="11" text-anchor="middle">
          <text x="380" y="52">1,000</text><text x="380" y="122">420</text><text x="380" y="196">580</text>
        </g>
      </svg>
      <div class="exhibit__src">来源：企业智能体发展调研，2026-08；单位：条，自然月去重线索</div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">初筛环节流失 580 条、占全链路 58%——先修初筛判定规则，比加大线索投放更快见效。</span>
    </div>
    <div class="footnote">注：流带宽度按流量线性编码，明细数据随页附数据表（PPTX 演讲者备注或页内表格）。</div>
  </div>
</section>

<!-- ══ 信息图页：树图（面积编码） ══ -->
<section class="band" id="s20">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">06 · 行业对标</div>
      <h2 class="t-h1 shead__title">规模化企业行业构成：制造与金融合计过半</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 6</span>
        <span class="exhibit__t">9 家规模化成功企业的行业构成（面积 ∝ 家数）</span>
      </div>
      <svg class="chart" data-chart="treemap" viewBox="0 0 900 300">
        <rect x="1" y="1" width="470" height="298" class="f-acc"/>
        <text x="20" y="34" class="t-on-inv" font-size="15" font-weight="600">制造 3 家</text>
        <text x="20" y="58" class="t-on-inv" font-size="12">33%</text>
        <rect x="475" y="1" width="310" height="298" class="f-s2"/>
        <text x="494" y="34" class="f-txt" font-size="14" font-weight="600">金融 2 家</text>
        <rect x="789" y="1" width="110" height="298" class="f-s3"/>
        <text x="800" y="28" class="f-txt" font-size="12">互联网 2 家</text>
      </svg>
      <div class="exhibit__src">注：行业构成基于 9 家规模化成功企业（N=42 访谈样本），能源与医疗各 1 家合并显示</div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">制造与金融合计 5 家、占 55%——共同点是流程标准、容错边界清晰，可直接复制。</span>
    </div>
    <div class="footnote">注：面积与家数严格成比例；小于 2 家的行业合并为「其他」以保证可读性。</div>
  </div>
</section>

<!-- ══ 信息图页：箱线图（分布对比） ══ -->
<section class="band" id="s11">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">05 · 风险与治理</div>
      <h2 class="t-h1 shead__title">各域就绪度分布：金融客服中位最高、离散最小</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 7</span>
        <span class="exhibit__t">四类场景就绪度分布（箱体 = Q1–Q3，中线 = 中位，须 = 极值）</span>
      </div>
      <svg class="chart" data-chart="boxplot" viewBox="0 0 900 300">
        <line x1="70" y1="250" x2="860" y2="250" class="s-bd"/>
        <g class="s-txt3" stroke-width="1.5">
          <line x1="180" y1="42" x2="180" y2="228"/><line x1="150" y1="42" x2="210" y2="42"/>
          <line x1="150" y1="228" x2="210" y2="228"/>
        </g>
        <rect x="140" y="66" width="80" height="110" class="f-s2 s-acc"/>
        <line x1="140" y1="100" x2="220" y2="100" class="s-acc" stroke-width="3"/>
        <text x="180" y="272" class="f-txt2" font-size="12" text-anchor="middle">金融客服</text>
        <text x="180" y="92" class="f-acc" font-size="12" font-weight="600" text-anchor="middle">81</text>
        <g class="s-txt3" stroke-width="1.5">
          <line x1="400" y1="86" x2="400" y2="222"/><line x1="370" y1="86" x2="430" y2="86"/>
          <line x1="370" y1="222" x2="430" y2="222"/>
        </g>
        <rect x="360" y="120" width="80" height="76" class="f-s2 s-acc"/>
        <line x1="360" y1="152" x2="440" y2="152" class="s-acc" stroke-width="3"/>
        <text x="400" y="272" class="f-txt2" font-size="12" text-anchor="middle">制造研发</text>
        <text x="400" y="144" class="f-acc" font-size="12" font-weight="600" text-anchor="middle">49</text>
        <g class="s-txt3" stroke-width="1.5">
          <line x1="620" y1="62" x2="620" y2="212"/><line x1="590" y1="62" x2="650" y2="62"/>
          <line x1="590" y1="212" x2="650" y2="212"/>
        </g>
        <rect x="580" y="94" width="80" height="90" class="f-s2 s-acc"/>
        <line x1="580" y1="130" x2="660" y2="130" class="s-acc" stroke-width="3"/>
        <text x="620" y="272" class="f-txt2" font-size="12" text-anchor="middle">互联网营销</text>
        <text x="620" y="122" class="f-acc" font-size="12" font-weight="600" text-anchor="middle">62</text>
      </svg>
      <div class="exhibit__src">注：就绪度 = 场景 × 行业维度的能力自评加权得分（0–100），N=42 深度访谈</div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">金融客服中位 81 分且四分位区间最窄——标准化程度高的场景，就绪度稳定且可复制。</span>
    </div>
    <div class="footnote">注：分布基于各场景 8–12 个样本点；能源财务组样本最少（n=8），区间仅供参考。</div>
  </div>
</section>

<!-- ══ 信息图页：关系网络（节点-边拓扑） ══ -->
<section class="band" id="s12">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">05 · 风险与治理</div>
      <h2 class="t-h1 shead__title">平台组件依赖拓扑：编排层为单点枢纽</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 8</span>
        <span class="exhibit__t">平台五组件依赖关系（节点大小 ∝ 连接度）</span>
      </div>
      <svg class="chart" data-chart="network" viewBox="0 0 900 300">
        <g class="s-bd" stroke-width="1.2">
          <line x1="450" y1="60" x2="180" y2="190"/><line x1="450" y1="60" x2="450" y2="240"/>
          <line x1="450" y1="60" x2="720" y2="190"/><line x1="180" y1="190" x2="450" y2="240"/>
          <line x1="720" y1="190" x2="450" y2="240"/>
        </g>
        <circle cx="450" cy="60" r="34" class="f-acc"/>
        <text x="450" y="64" class="t-on-inv" font-size="12" text-anchor="middle">统一编排</text>
        <circle cx="180" cy="190" r="24" class="f-acc"/>
        <text x="180" y="194" class="t-on-inv" font-size="11" text-anchor="middle">工具网关</text>
        <circle cx="720" cy="190" r="24" class="f-acc"/>
        <text x="720" y="194" class="t-on-inv" font-size="11" text-anchor="middle">权限中心</text>
        <circle cx="450" cy="240" r="20" class="f-s3"/>
        <text x="450" y="244" class="f-txt" font-size="11" text-anchor="middle">审计日志</text>
      </svg>
      <div class="exhibit__src">注：依赖关系取自 9 家规模化企业的平台架构文档（2026-08）</div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">编排层连接度最高——它一旦不可用，工具、记忆、权限三条链路同时中断，须优先做冗余。</span>
    </div>
    <div class="footnote">注：布局为确定性环形排布（同输入必同输出），不使用随机力导向。</div>
  </div>
</section>

<!-- ══ 信息图页：马赛克图（双重编码） ══ -->
<section class="band" id="s13">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">04 · 落地路径</div>
      <h2 class="t-h1 shead__title">渠道结构演变：线上占比三年提升 21 个百分点</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 9</span>
        <span class="exhibit__t">渠道结构演变（列宽 ∝ 总规模，列高 = 构成占比）</span>
      </div>
      <svg class="chart" data-chart="marimekko" viewBox="0 0 900 300">
        <rect x="70" y="40" width="180" height="90" class="f-acc"/>
        <rect x="70" y="130" width="180" height="110" class="f-s2"/>
        <text x="160" y="90" class="t-on-inv" font-size="12" text-anchor="middle">40%</text>
        <text x="160" y="190" class="f-txt" font-size="12" text-anchor="middle">60%</text>
        <text x="160" y="262" class="f-txt" font-size="12" font-weight="600" text-anchor="middle">2023</text>
        <rect x="256" y="34" width="234" height="117" class="f-acc"/>
        <rect x="256" y="151" width="234" height="89" class="f-s2"/>
        <text x="373" y="90" class="t-on-inv" font-size="12" text-anchor="middle">52%</text>
        <text x="373" y="200" class="f-txt" font-size="12" text-anchor="middle">48%</text>
        <text x="373" y="262" class="f-txt" font-size="12" font-weight="600" text-anchor="middle">2024</text>
        <rect x="496" y="28" width="297" height="141" class="f-acc"/>
        <rect x="496" y="169" width="297" height="71" class="f-s2"/>
        <text x="644" y="90" class="t-on-inv" font-size="12" text-anchor="middle">61%</text>
        <text x="644" y="210" class="f-txt" font-size="12" text-anchor="middle">39%</text>
        <text x="644" y="262" class="f-txt" font-size="12" font-weight="600" text-anchor="middle">2025</text>
        <rect x="70" y="278" width="12" height="12" class="f-acc"/>
        <text x="88" y="288" class="f-txt2" font-size="11">线上</text>
        <rect x="140" y="278" width="12" height="12" class="f-s2"/>
        <text x="158" y="288" class="f-txt2" font-size="11">线下</text>
      </svg>
      <div class="exhibit__src">注：列宽 ∝ 当年总规模（2023 = 100），列高 = 渠道构成占比</div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">总量三年增长 65%，线上占比从 40% 升到 61%——线上承载能力已成为规模化的前置条件。</span>
    </div>
    <div class="footnote">注：双重编码缺一不可——只画占比会丢掉规模差异，只画规模会丢掉结构变化。</div>
  </div>
</section>

<!-- ══ 信息图页：流带图（构成演变） ══ -->
<section class="band" id="s14">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">07 · 价值阶梯</div>
      <h2 class="t-h1 shead__title">价值兑现结构演变：副驾协同持续做厚</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 10</span>
        <span class="exhibit__t">价值兑现结构演变（基线居中 · 带宽 ∝ 场景数）</span>
      </div>
      <svg class="chart" data-chart="streamgraph" viewBox="0 0 900 300">
        <path class="f-acc" opacity=".9"
          d="M60,118 C220,106 380,86 540,72 C660,62 780,56 860,54 L860,94 C780,98 660,108 540,122 C380,138 220,150 60,158 Z"/>
        <path class="f-s2" opacity=".9"
          d="M60,158 C220,150 380,138 540,122 C660,108 780,98 860,94 L860,130 C780,136 660,148 540,162 C380,178 220,188 60,194 Z"/>
        <path class="f-s3" opacity=".9"
          d="M60,194 C220,188 380,178 540,162 C660,148 780,136 860,130 L860,194 C780,202 660,212 540,224 C380,238 220,246 60,250 Z"/>
        <g class="f-txt2" font-size="11" text-anchor="middle">
          <text x="60" y="284">2023</text><text x="260" y="284">2024</text>
          <text x="460" y="284">2025</text><text x="660" y="284">2026</text><text x="860" y="284">2027</text>
        </g>
      </svg>
      <div class="exhibit__src">注：占比为各形态场景数占当年总量；带宽 ∝ 场景数，基线居中展开</div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">问答检索的占比从 52% 降到 18%，价值重心持续向副驾协同与端到端交付迁移。</span>
    </div>
    <div class="footnote">注：带边界上下分别采样（≥24 点），不使用预设形状替代曲线语义。</div>
  </div>
</section>

<!-- ══ 形状通道图表：甘特（排期；回归覆盖 shapeGantt 的 start/span 计算） ══ -->
<section class="band" id="s15">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">01 · 范式与分水岭</div>
      <h2 class="t-h1 shead__title">实施排期：四阶段串行推进共 18 周</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 11</span>
        <span class="exhibit__t">四阶段实施排期（条形长度 = 时长，起点 = 阶段起始周）</span>
      </div>
      <svg class="chart" data-chart="gantt" viewBox="0 0 900 220">
        <text x="0" y="34" class="f-txt2" font-size="12">调研</text>
        <rect x="90" y="20" width="760" height="20" rx="10" class="f-s2"/>
        <rect x="90" y="20" width="127" height="20" rx="10" class="f-acc"/>
        <text x="890" y="35" text-anchor="end" class="f-txt" font-size="12" font-weight="600">3 周</text>
        <text x="0" y="84" class="f-txt2" font-size="12">设计</text>
        <rect x="90" y="70" width="760" height="20" rx="10" class="f-s2"/>
        <rect x="217" y="70" width="169" height="20" rx="10" class="f-acc"/>
        <text x="890" y="85" text-anchor="end" class="f-txt" font-size="12" font-weight="600">4 周</text>
        <text x="0" y="134" class="f-txt2" font-size="12">开发</text>
        <rect x="90" y="120" width="760" height="20" rx="10" class="f-s2"/>
        <rect x="386" y="120" width="338" height="20" rx="10" class="f-acc"/>
        <text x="890" y="135" text-anchor="end" class="f-txt" font-size="12" font-weight="600">8 周</text>
        <text x="0" y="184" class="f-txt2" font-size="12">试点</text>
        <rect x="90" y="170" width="760" height="20" rx="10" class="f-s2"/>
        <rect x="724" y="170" width="126" height="20" rx="10" class="f-acc"/>
        <text x="890" y="185" text-anchor="end" class="f-txt" font-size="12" font-weight="600">3 周</text>
      </svg>
      <div class="exhibit__src">来源：项目排期基线，2026-08；时间轴跨度 = 各阶段「起点 + 时长」最大值（18 周）</div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">开发阶段独占 8 周、占总工期 44%——压缩工期的杠杆在开发，不在调研与设计。</span>
    </div>
    <div class="footnote">注：条形长度按周线性编码，起点为阶段起始周；「起点 + 时长」最大值决定时间轴跨度。</div>
  </div>
</section>

<!-- ══ 形状通道图表：玫瑰图（回归覆盖 shapeRose 的扇区采样） ══ -->
<section class="band" id="s16">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">05 · 风险与治理</div>
      <h2 class="t-h1 shead__title">能力半径：技术可控一枝独秀</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 12</span>
        <span class="exhibit__t">五维能力半径（扇区半径 ∝ 得分 · 单位：分）</span>
      </div>
      <svg class="chart" data-chart="rose" viewBox="0 0 220 220" style="width:210px;margin-inline:auto">
        <path class="f-acc" d="M110,110 L110,35.4 A74.6,74.6 0 0,1 179.2,82.1 Z"/>
        <path class="f-s2" d="M110,110 L169.6,90.6 A62.7,62.7 0 0,1 150.3,158.0 Z"/>
        <path class="f-s3" d="M110,110 L144.4,157.3 A58.5,58.5 0 0,1 79.0,159.6 Z"/>
        <path class="f-s4" d="M110,110 L81.0,150.0 A49.4,49.4 0 0,1 62.1,98.0 Z"/>
        <path class="f-s2" d="M110,110 L47.0,89.5 A66.2,66.2 0 0,1 105.4,43.9 Z"/>
        <circle cx="110" cy="110" r="6" class="f-s3"/>
      </svg>
      <div class="t-xs" style="text-align:center;color:var(--text-3);margin-top:var(--sp-2)">
        技术可控 78 分 · 合规完备 66 分 · 组织就绪 61 分 · 数据就绪 55 分 · 经济可行 42 分
      </div>
      <div class="exhibit__src">注：扇区半径按得分线性映射（0–100 分）；每扇区 ≥16 段采样，不使用预设形状替代曲线语义</div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">技术可控 78 分领先 36 分，而经济可行 42 分垫底——能力建设的短板不在技术，在算得过来账。</span>
    </div>
    <div class="footnote">注：五维得分来自 42 家访谈企业的能力自评加权（0–100 分），维度定义见参考资料 [1]。</div>
  </div>
</section>

<!-- ══ 形状通道图表：K 线（回归覆盖 shapeCandlestick 与 appendix→inline 数据表） ══ -->
<section class="band" id="s17">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">06 · 行业对标</div>
      <h2 class="t-h1 shead__title">八期评分波动：区间震荡后温和上行</h2>
    </div>
    <div class="exhibit rv">
      <div class="exhibit__hd">
        <span class="exhibit__no">Exhibit 13</span>
        <span class="exhibit__t">八期就绪度评分波动（实体 = 开收，须 = 高低 · 单位：分）</span>
      </div>
      <svg class="chart" data-chart="candlestick" viewBox="0 0 900 240">
        <line x1="30" y1="200" x2="870" y2="200" class="s-bd"/>
        <g class="s-txt3" stroke-width="2">
          <line x1="53" y1="86" x2="53" y2="200"/><line x1="158" y1="67" x2="158" y2="143"/>
          <line x1="263" y1="96" x2="263" y2="186"/><line x1="368" y1="120" x2="368" y2="172"/>
          <line x1="473" y1="44" x2="473" y2="153"/><line x1="578" y1="30" x2="578" y2="96"/>
          <line x1="683" y1="53" x2="683" y2="120"/><line x1="788" y1="20" x2="788" y2="115"/>
        </g>
        <g class="f-acc">
          <rect x="40" y="105" width="26" height="67"/><rect x="355" y="134" width="26" height="24"/>
          <rect x="460" y="58" width="26" height="76"/><rect x="775" y="34" width="26" height="71"/>
        </g>
        <g class="f-s3">
          <rect x="145" y="105" width="26" height="19"/><rect x="250" y="124" width="26" height="33"/>
          <rect x="565" y="58" width="26" height="24"/><rect x="670" y="82" width="26" height="24"/>
        </g>
        <g class="f-txt3" font-size="11" text-anchor="middle">
          <text x="53" y="218">1</text><text x="158" y="218">2</text><text x="263" y="218">3</text>
          <text x="368" y="218">4</text><text x="473" y="218">5</text><text x="578" y="218">6</text>
          <text x="683" y="218">7</text><text x="788" y="218">8</text>
        </g>
      </svg>
      <div class="exhibit__src">来源：季度就绪度评分序列，2025Q1–2026Q4；单位：分（0–100）</div>
    </div>
    <div class="sowhat rv">
      <span class="sowhat__k">So what</span>
      <span class="sowhat__v">八期振幅收窄后连拉两根阳线——就绪度进入温和上行段，治理投入开始显效。</span>
    </div>
    <div class="footnote">注：上涨用 accent 实体、下跌用中性色实体（不引入红绿第二色相）；明细数据随页附数据表。</div>
  </div>
</section>

<!-- ══ 素材图片页（image 页型 · grid 多图网格 + 配图占位） ══ -->
<section class="band" id="s-photos">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">08 · 现场素材</div>
      <h2 class="t-h1 shead__title">三家样板企业的产线现场：同一套护栏，不同业务形态</h2>
      <p class="t-lead shead__desc">四张现场照并排互证；无图时先出等比例占位，交付前替换 src 即可。</p>
    </div>
    <div class="media-grid media-grid--4 rv">
      <figure class="media media--r4-3 media--ph">
        <div class="media__ph">
          <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="m3 18 5-5 4 3.4 3-2.6 6 5.2"/></svg>
          <b>配图占位</b>
        </div>
        <figcaption class="media__cap--below">制造 · 质检工位</figcaption>
      </figure>
      <figure class="media media--r4-3 media--ph">
        <div class="media__ph">
          <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="m3 18 5-5 4 3.4 3-2.6 6 5.2"/></svg>
          <b>配图占位</b>
        </div>
        <figcaption class="media__cap--below">金融 · 风控坐席</figcaption>
      </figure>
      <figure class="media media--r4-3 media--ph">
        <div class="media__ph">
          <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="m3 18 5-5 4 3.4 3-2.6 6 5.2"/></svg>
          <b>配图占位</b>
        </div>
        <figcaption class="media__cap--below">互联网 · 研发流水线</figcaption>
      </figure>
      <figure class="media media--r4-3 media--ph">
        <div class="media__ph">
          <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="m3 18 5-5 4 3.4 3-2.6 6 5.2"/></svg>
          <b>配图占位</b>
        </div>
        <figcaption class="media__cap--below">制造 · 设备巡检</figcaption>
      </figure>
    </div>
    <p class="media__src">图 2–5：现场素材占位（建议 900×675px · 4:3；替换 image.items[].src 即可）<a class="cite" href="#ref-2">[2]</a></p>
  </div>
</section>

<!-- ══ 结论页（深色收尾） ══ -->
<section class="band band--accent band--fit" id="next">
  <div class="wrap">
    <div class="shead shead--center rv">
      <div class="t-eyebrow">结论</div>
      <h2 class="t-h1 shead__title">平台化穿越分水岭，分级放量兑现价值</h2>
      <p class="t-lead shead__desc">三条核心结论的浓缩陈述。</p>
    </div>
    <div class="grid g-3 rv">
      <div class="card">
        <h3 class="t-h3" style="margin-bottom:var(--sp-2)">平台先行</h3>
        <p class="t-body">
          统一编排与护栏到位，场景再分层放量。</p>
      </div>
      <div class="card">
        <h3 class="t-h3" style="margin-bottom:var(--sp-2)">场景分级</h3>
        <p class="t-body">
          三重门槛齐备的场景优先，不足两成。</p>
      </div>
      <div class="card">
        <h3 class="t-h3" style="margin-bottom:var(--sp-2)">治理闭环</h3>
        <p class="t-body">
          权限、审计、回退全链路内嵌平台层。</p>
      </div>
    </div>
    <div class="row" style="justify-content:center;gap:var(--sp-3);
         margin-top:clamp(28px,3.4vh,44px);flex-wrap:wrap">
      <a class="btn btn--primary" href="#s1">返回阅读</a>
      <a class="btn btn--ghost" href="#refs"
         style="border-color:color-mix(in srgb,var(--text-inv) 30%,transparent)">
        参考资料</a>
    </div>
  </div>
</section>

<!-- ══ 参考资料 ══ -->
<section class="band band--tint" id="refs">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">参考资料</div>
      <h2 class="t-h1 shead__title">数据来源与口径说明</h2>
    </div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th style="width:6%">编号</th><th style="width:26%">来源</th>
          <th style="width:14%">时间</th><th>口径说明</th></tr></thead>
        <tbody>
          <tr id="ref-1"><td class="k">[1]</td>
            <td><a class="ref-link" href="https://example.com/gartner-agentic-ai" target="_blank" rel="noopener">Gartner：Agentic AI 技术成熟度曲线
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><path d="M15 3h6v6M10 14 21 3"/></svg></a></td>
            <td>2026-06</td><td>试点率 / 采纳率 / 形态成熟度判定</td></tr>
          <tr id="ref-2"><td class="k">[2]</td><td>企业智能体发展调研（内部，N=42）</td>
            <td>2026-08</td><td>域间数据 / 规模化占比 / 访谈结论，2026-07 至 2026-08</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ══ 页脚 ══ -->
<footer class="foot">
  <div class="wrap foot__in">
    <div class="brand">
      <div class="brand__mark">AI</div>
      <div class="brand__txt">
        <div class="brand__title">2026 AI 智能体发展研究报告</div>
        <div class="brand__sub">研究报告 · ''' + DATE + '''</div>
      </div>
    </div>
    <div class="t-xs">内部研究资料 · 请勿外传</div>
  </div>
</footer>'''

R_MODEL = {
    "mode": "research", "style": "mckinsey",
    "title": "2026 AI 智能体发展研究报告",
    "subtitle": "规模化前夜的治理与集成研究",
    "meta": "内部研究资料 · " + DATE,
    "agenda": [
        ["01", "范式与分水岭", "从 Chatbot 到 Autonomous Agent"],
        ["02", "形态与边界", "三类形态与能力边界"],
        ["03", "域间差异", "试点率的行业分化与互证"],
        ["04", "落地路径", "平台化先行四步走"],
        ["05", "风险与治理", "三重门槛与优先级矩阵"],
        ["06", "参考资料", "数据来源与口径说明"],
    ],
    "sections": [
        {"type": "twocol", "eyebrow": "01 · 范式与分水岭",
         "title": "六成企业试点卡在治理与集成——规模化分水岭已经出现",
         "paragraphs": [["发现", "2025 年全球企业智能体试点率 61%，规模化运行仅 18%，相差 43 个百分点。"],
                        ["证据", "42 家深度访谈企业中，37 家把「权限不清、系统难接」列为放弃规模化的首因。"],
                        ["含义", "瓶颈不在模型能力，而在治理、权限与系统集成。"],
                        ["推论", "平台化先行：统一编排与护栏到位后，场景再分层放量。"]],
         "soWhat": "先建平台与护栏，再放场景——顺序反了会被治理拖死。",
         "footnote": "注：试点率 = 已进入试点及以上的企业占比；规模化 = 3 个以上场景稳定运行。"},
        {"type": "table", "eyebrow": "02 · 形态与边界",
         "title": "三类形态能力边界分明，同事级智能体尚在早期",
         "table": {"head": ["形态", "自主性", "工具生态", "成熟度", "结论"],
                   "rows": [["助理级", "单轮任务，人逐步驱动", "少量插件", "规模可用", "当前主力"],
                            ["流程级", "固定流程多步执行", "数十工具编排", "试点爬坡", "2026 焦点"],
                            ["同事级", "目标驱动，端到端", "千级工具生态", "早期验证", "三年后"]]},
         "flags": ["同事级成熟度评分口径待确认，正式版请替换 xx%",
                   "「三年后」时间窗来自访谈主观判断，需以官方路线图数据复核"],
         "footnote": "注：形态判定口径见参考资料 [1]；同事级判定基于访谈专家评分（N=42）。"},
        {"type": "exhibit", "eyebrow": "03 · 域间差异",
         "title": "客服域一马当先，研发域势能最大——域间分化明显",
         "exhibitNo": "Exhibit 1",
         "chart": {"type": "hbar", "labels": ["客服", "财务", "营销", "研发"],
                   "values": [72, 57, 48, 38], "max": 100, "unit": "%"},
         "soWhat": "研发域渗透最浅但势能最大，工具链成熟后有望一年内反超客服域。",
         "footnote": "来源：企业智能体发展调研，2026-08；试点率 = 已进入试点及以上的企业占比"},
        {"type": "halftable", "eyebrow": "03 · 域间差异",
         "title": "试点率与增幅互证：研发域一年内有望反超",
         "table": {"head": ["业务域", "试点率", "同比增幅"],
                   "rows": [["客服", "72%", "+9pt"], ["财务", "57%", "+11pt"],
                            ["营销", "48%", "+13pt"], ["研发", "38%", "+15pt"]]},
         "chart": {"type": "bar", "labels": ["客服", "财务", "营销", "研发"],
                   "values": [9, 11, 13, 15], "max": 16, "unit": "pt"},
         "soWhat": "增幅与基数负相关，研发域工具链补齐后将进入陡峭爬坡段。"},
        {"type": "comparison", "eyebrow": "04 · 落地路径",
         "title": "堆场景与平台化两条路径的结局分野",
         "left": {"title": "堆场景路径（n=23）",
                  "points": [["接入慢", "每场景重复对接，平均 11 周上线"],
                             ["治理弱", "事后审计，回退靠人工"],
                             ["结局", "19 家半年内退回试点"]]},
         "right": {"title": "平台化路径（n=9）",
                   "points": [["接入快", "统一编排，平均 3 周上线"],
                              ["治理内嵌", "权限、审计、回退进平台层"],
                              ["结局", "全部穿越分水岭进入放量"]]},
         "soWhat": "平台化把场景接入周期从 11 周压到 3 周，是穿越分水岭的唯一共同路径。"},
        {"type": "donut", "eyebrow": "04 · 落地路径",
         "title": "规模化企业行业分布：制造与金融领跑",
         "chart": {"labels": ["制造", "金融", "互联网及其他"], "values": [3, 2, 4], "centerLabel": "家"},
         "note": "注：行业构成基于 9 家规模化成功企业（N=42 访谈样本）。"},
        {"type": "metrics", "eyebrow": "04 · 落地路径",
         "title": "四组基线数字勾勒出规模化落地现状",
         "metrics": [["61%", "企业试点率，2025 年基线"], ["18%", "规模化占比，3 场景以上"],
                     ["9 家", "规模化成功企业，全部先建平台层"], ["60%", "2027Q2 采纳率目标"]]},
        {"type": "split", "eyebrow": "04 · 落地路径",
         "title": "平台化先行是穿越分水岭的共同路径",
         "left": {"points": [["路径", "规模化成功的 9 家企业全部先建平台层再放场景。"],
                             ["机制", "统一编排收敛工具、记忆、权限，接入成本降一个量级。"],
                             ["反例", "跳过平台直接堆场景，23 家中 19 家半年内回退试点。"]]},
         "right": {"type": "bar", "cap": "采纳率爬坡（%）",
                   "labels": ["2026Q3", "Q4", "2027Q1", "Q2"], "values": [30, 45, 55, 60], "max": 100},
         "soWhat": "平台层的投入在四个季度内由采纳率爬坡兑回，不是纯成本。"},
        {"type": "threecol", "eyebrow": "05 · 风险与治理",
         "title": "规模化三重门槛：技术可控、组织就绪、经济可行",
         "paragraphs": [["技术可控", "幻觉率与工具调用成功率决定场景上限，需评测门禁。"],
                        ["组织就绪", "流程负责人须会拆任务、定验收；缺位场景一律降级试点。"],
                        ["经济可行", "单任务成本须低于人工基线 30% 以上，否则不可放量。"],
                        ["佐证", "成功企业按三重门槛给场景分级放量。"],
                        ["顺序", "先算经济账再上技术平台——多数失败案例顺序相反。"],
                        ["结论", "三门槛齐备的场景不足两成，分级放量是唯一理性路径。"]],
         "footnote": "注：三重门槛口径来自访谈编码（N=42），编码一致性 Kappa=0.81。"},
        {"type": "matrix", "eyebrow": "05 · 风险与治理",
         "title": "高价值低难度场景优先——矩阵给出放量顺序",
         "rowHeads": ["业务价值 · 高", "业务价值 · 中"],
         "colHeads": ["实施难度 · 低", "实施难度 · 中", "实施难度 · 高"],
         "cells": [[{"t": "客服问数：首批放量", "accent": True},
                    {"t": "研发副驾：二批放量", "accent": False},
                    {"t": "端到端交付：暂缓", "accent": False}],
                   [{"t": "知识检索：常规推进", "accent": False},
                    {"t": "经营预警：常规推进", "accent": False},
                    {"t": "自主决策：护栏试点", "accent": True}]]},
        {"type": "heatmap", "eyebrow": "06 · 行业对标",
         "title": "行业就绪度差异显著——金融客服先行，制造研发滞后",
         "rowHeads": ["金融", "制造", "互联网"],
         "colHeads": ["客服", "研发", "营销", "供应链", "财务"],
         "cells": [[78, 46, 63, 38, 61], [44, 29, 33, 57, 31], [71, 82, 68, 49, 52]],
         "unit": "", "scaleLabel": ["低", "高"],
         "soWhat": "金融客服与互联网研发是两个可复制样板，制造研发域需先补工具链再谈放量。",
         "footnote": "注：就绪度 = 场景 × 行业维度的能力自评加权得分（0–100），N=42 深度访谈 + 行业抽样[2]。"},
        {"type": "pyramid", "eyebrow": "07 · 价值阶梯",
         "title": "价值兑现四级台阶：越往上，组织变革成本越高",
         "levels": [["自主决策", "自动执行"],
                    ["端到端交付", "跨系统串联多步任务，交付质量可回退"],
                    {"t": "副驾协同", "d": "人机分工明确，效率提升可度量（当前主力）", "accent": True},
                    ["问答与检索", "知识问答、找数问数，替换成本最低"]],
         "soWhat": "当前主力仍在第二级：把副驾协同做厚，比抢跑自主决策更能兑现价值。",
         "footnote": "注：台阶高度不代表难度，仅表示覆盖范围；accent 层为当前主力形态[1]。"},
        # ── 原生图表技巧（waterfall）+ 六类复杂信息图页型 ──
        {"type": "bar", "eyebrow": "03 · 域间差异", "exhibitNo": "Exhibit 4",
         "title": "试点率增长归因：工具链补齐贡献过半",
         "chart": {"type": "waterfall",
                   "labels": ["2025 基线", "工具链", "流程改造", "治理", "组织", "2026 现值"],
                   "values": [38, 9, 6, -3, 2, 52], "unit": "pt"},
         "soWhat": "九个百分点增量里工具链补齐贡献最大、治理不足拖累 3pt——补齐工具链的边际收益最高。",
         "footnote": "来源：企业智能体发展调研，2026-08；单位为百分点（pt），按增量归因分解"},
        {"type": "sankey", "eyebrow": "04 · 落地路径", "exhibitNo": "Exhibit 5",
         "title": "线索转化流向：初筛环节流失占比近六成",
         "unit": "条",
         "flows": [["线索", "初筛", 1000], ["初筛", "商机", 420], ["商机", "报价", 260],
                   ["报价", "签约", 120], ["初筛", "流失", 580], ["商机", "流失", 160]],
         "chart": {"dataTable": "inline"},
         "soWhat": "初筛环节流失 580 条、占全链路 58%——先修初筛判定规则，比加大线索投放更快见效。",
         "footnote": "来源：企业智能体发展调研，2026-08；单位：条，自然月去重线索"},
        {"type": "treemap", "eyebrow": "06 · 行业对标", "exhibitNo": "Exhibit 6",
         "title": "规模化企业行业构成：制造与金融合计过半",
         "unit": "家",
         "items": [["制造", 3], ["金融", 2], ["互联网", 2], ["能源", 1], ["医疗", 1]],
         "soWhat": "制造与金融合计 5 家、占 55%——共同点是流程标准、容错边界清晰，可直接复制。",
         "footnote": "注：行业构成基于 9 家规模化成功企业（N=42 访谈样本）"},
        {"type": "boxplot", "eyebrow": "05 · 风险与治理", "exhibitNo": "Exhibit 7",
         "title": "各域就绪度分布：金融客服中位最高、离散最小",
         "unit": "分",
         "groups": [["金融客服", 62, 74, 81, 86, 93], ["制造研发", 31, 42, 49, 57, 68],
                    ["互联网营销", 44, 55, 62, 70, 79]],
         "soWhat": "金融客服中位 81 分且四分位区间最窄——标准化程度高的场景，就绪度稳定且可复制。",
         "footnote": "注：就绪度 = 场景 × 行业维度的能力自评加权得分（0–100），N=42 深度访谈"},
        {"type": "network", "eyebrow": "05 · 风险与治理", "exhibitNo": "Exhibit 8",
         "title": "平台组件依赖拓扑：编排层为单点枢纽",
         "nodes": [["n1", "统一编排"], ["n2", "工具网关"], ["n3", "记忆库"],
                   ["n4", "权限中心"], ["n5", "审计日志"]],
         "edges": [["n1", "n2"], ["n1", "n3"], ["n1", "n4"], ["n2", "n5"], ["n3", "n5"], ["n4", "n5"]],
         "soWhat": "编排层连接度最高——它一旦不可用，工具、记忆、权限三条链路同时中断，须优先做冗余。",
         "footnote": "注：依赖关系取自 9 家规模化企业的平台架构文档（2026-08）"},
        {"type": "marimekko", "eyebrow": "04 · 落地路径", "exhibitNo": "Exhibit 9",
         "title": "渠道结构演变：线上占比三年提升 21 个百分点",
         "unit": "%",
         "cols": [["2023", 100], ["2024", 130], ["2025", 165]],
         "cells": [[40, 60], [52, 48], [61, 39]],
         "legend": ["线上", "线下"],
         "soWhat": "总量三年增长 65%，线上占比从 40% 升到 61%——线上承载能力已成为规模化的前置条件。",
         "footnote": "注：列宽 ∝ 当年总规模，列高 = 渠道构成占比"},
        {"type": "streamgraph", "eyebrow": "07 · 价值阶梯", "exhibitNo": "Exhibit 10",
         "title": "价值兑现结构演变：副驾协同持续做厚",
         "labels": ["2023", "2024", "2025", "2026", "2027"],
         "series": [{"name": "问答检索", "values": [52, 44, 34, 26, 18]},
                    {"name": "副驾协同", "values": [30, 34, 36, 40, 44]},
                    {"name": "端到端交付", "values": [18, 22, 30, 34, 38]}],
         "soWhat": "问答检索的占比从 52% 降到 18%，价值重心持续向副驾协同与端到端交付迁移。",
         "footnote": "注：占比为各形态场景数占当年总量；带宽 ∝ 场景数"},
        # ── 形状通道图表（chart.type 承载；永久回归覆盖 gantt / rose / candlestick）──
        {"type": "bar", "eyebrow": "01 · 范式与分水岭", "exhibitNo": "Exhibit 11",
         "title": "实施排期：四阶段串行推进共 18 周",
         "chart": {"type": "gantt", "labels": ["调研", "设计", "开发", "试点"],
                   "values": [3, 4, 8, 3], "start": [0, 3, 7, 15], "unit": "周"},
         "soWhat": "开发阶段独占 8 周、占总工期 44%——压缩工期的杠杆在开发，不在调研与设计。",
         "footnote": "来源：项目排期基线，2026-08；时间轴跨度 = 各阶段「起点 + 时长」最大值（18 周）"},
        {"type": "bar", "eyebrow": "05 · 风险与治理", "exhibitNo": "Exhibit 12",
         "title": "能力半径：技术可控一枝独秀",
         "chart": {"type": "rose", "labels": ["技术可控", "合规完备", "组织就绪", "数据就绪", "经济可行"],
                   "values": [78, 66, 61, 55, 42], "max": 100, "unit": "分"},
         "soWhat": "技术可控 78 分领先 36 分，而经济可行 42 分垫底——能力建设的短板不在技术，在算得过来账。",
         "footnote": "注：五维得分来自 42 家访谈企业的能力自评加权（0–100 分），维度定义见参考资料 [1]"},
        {"type": "bar", "eyebrow": "06 · 行业对标", "exhibitNo": "Exhibit 13",
         "title": "八期评分波动：区间震荡后温和上行",
         "chart": {"type": "candlestick", "labels": ["1", "2", "3", "4", "5", "6", "7", "8"],
                   "values": [[44, 62, 38, 58], [58, 66, 50, 54], [54, 60, 41, 47], [47, 55, 44, 52],
                              [52, 71, 48, 68], [68, 74, 60, 63], [63, 69, 55, 58], [58, 76, 56, 73]],
                   "unit": "分"},
         "soWhat": "八期振幅收窄后连拉两根阳线——就绪度进入温和上行段，治理投入开始显效。",
         "footnote": "来源：季度就绪度评分序列，2025Q1–2026Q4；单位：分（0–100）"},
        {"type": "image", "eyebrow": "08 · 现场素材",
         "title": "三家样板企业的产线现场：同一套护栏，不同业务形态",
         "lead": "四张现场照并排互证；无图时先出等比例占位，交付前替换 src 即可。",
         "image": {"layout": "grid", "fit": "cover",
                   "items": [{"placeholder": True, "caption": "制造 · 质检工位"},
                             {"placeholder": True, "caption": "金融 · 风控坐席"},
                             {"placeholder": True, "caption": "互联网 · 研发流水线"},
                             {"placeholder": True, "caption": "制造 · 设备巡检"}],
                   "caption": "图 2–5：现场素材占位（建议 900×675px · 4:3）"},
         "footnote": "来源：企业走访现场素材，2026-07 至 2026-08[2]"},
    ],
    "closing": {"title": "平台化穿越分水岭，分级放量兑现价值",
                "points": [["平台先行", "统一编排与护栏到位，场景再分层放量。"],
                           ["场景分级", "三重门槛齐备的场景优先，不足两成。"],
                           ["治理闭环", "权限、审计、回退全链路内嵌平台层。"]]},
}

# ══════════════════════════════════════════════════════════════════════════
#  内容包 · 信息架构图（architecture）《企业智能体平台总体架构》
# ══════════════════════════════════════════════════════════════════════════
A_CONTENT = '''<!-- ══ 封面页（架构版） ══ -->
<section class="band band--fit">
  <div class="wrap">
    <div class="stack gap-5 rv" style="max-width:920px">
      <div class="row row-wrap" style="gap:var(--sp-3)">
        <span class="chip chip--accent">方案架构</span>
        <span class="chip chip--line">评审版</span>
      </div>
      <h1 class="t-display">企业智能体平台<br>三层解耦架构</h1>
      <p class="t-lead" style="max-width:680px">模型、编排、应用三层解耦，统一护栏内让智能体安全地干活。</p>
      <div class="row row-wrap" style="gap:var(--sp-4)">
        <span class="chip">分层 × 3</span>
        <span class="chip">核心节点 × 8</span>
        <span class="chip">内部资料 · ''' + DATE + '''</span>
      </div>
    </div>
  </div>
</section>

<!-- ══ A1 分层带页（图为王） ══ -->
<section class="band band--fit" id="arch1">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">01 · 总体架构</div>
      <h2 class="t-h1 shead__title">三层解耦：模型、编排、应用各司其职</h2>
    </div>
    <div class="arch rv">
      <div class="arch__layer arch__layer--focus">
        <div class="arch__lname">应用层</div>
        <div class="arch__nodes">
          <div class="arch__node arch__node--accent"><div class="arch__nt">智能客服</div><div class="arch__nd">7×24 自主应答</div></div>
          <div class="arch__node"><div class="arch__nt">研发副驾</div><div class="arch__nd">代码与知识库操作</div></div>
          <div class="arch__node"><div class="arch__nt">数据管家</div><div class="arch__nd">口径自动核验</div></div>
        </div>
      </div>
      <div class="arch__conn"><svg width="16" height="20" viewBox="0 0 16 20" fill="none"
        stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M8 1v14M3 11l5 5 5-5"/></svg></div>
      <div class="arch__layer">
        <div class="arch__lname">编排层</div>
        <div class="arch__nodes">
          <div class="arch__node"><div class="arch__nt">任务规划</div><div class="arch__nd">目标拆解与分派</div></div>
          <div class="arch__node"><div class="arch__nt">工具调度</div><div class="arch__nd">千级工具统一注册</div></div>
          <div class="arch__node"><div class="arch__nt">记忆检索</div><div class="arch__nd">任务级长期记忆</div></div>
        </div>
      </div>
      <div class="arch__conn"><svg width="16" height="20" viewBox="0 0 16 20" fill="none"
        stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M8 1v14M3 11l5 5 5-5"/></svg></div>
      <div class="arch__layer">
        <div class="arch__lname">模型层</div>
        <div class="arch__nodes">
          <div class="arch__node"><div class="arch__nt">多模型接入</div><div class="arch__nd">按场景路由</div></div>
          <div class="arch__node"><div class="arch__nt">统一网关</div><div class="arch__nd">配额与降级</div></div>
        </div>
      </div>
    </div>
    <div class="arch__legend rv">
      <span class="chip chip--accent">当前建设焦点</span>
      <span class="chip">已有能力</span>
    </div>
    <div class="t-xs rv" style="margin-top:var(--sp-3);color:var(--text-3)">分层与命名依据 <a class="cite" href="#ref-1">[1]</a></div>
  </div>
</section>

<!-- ══ A2 泳道页 ══ -->
<section class="band band--fit" id="arch2">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">02 · 协作流程</div>
      <h2 class="t-h1 shead__title">一次任务请求的五步闭环</h2>
    </div>
    <div class="stack rv">
      <div class="lane">
        <div class="lane__hd">业务方</div>
        <div class="lane__body">
          <span class="lane__step">下达目标</span><span class="lane__arr" aria-hidden="true"></span>
          <span class="lane__step">拆任务</span><span class="lane__arr" aria-hidden="true"></span>
          <span class="lane__step lane__step--a">人审核</span>
        </div>
      </div>
      <div class="lane">
        <div class="lane__hd">编排层</div>
        <div class="lane__body">
          <span class="lane__step lane__step--a">规划校验</span><span class="lane__arr" aria-hidden="true"></span>
          <span class="lane__step">工具调用</span><span class="lane__arr" aria-hidden="true"></span>
          <span class="lane__step">全程留痕</span>
        </div>
      </div>
      <div class="lane">
        <div class="lane__hd">执行层</div>
        <div class="lane__body">
          <span class="lane__step">调用模型</span><span class="lane__arr" aria-hidden="true"></span>
          <span class="lane__step">产出结果</span><span class="lane__arr" aria-hidden="true"></span>
          <span class="lane__step">回写记忆</span>
        </div>
      </div>
    </div>
    <div class="arch__legend rv">
      <span class="chip chip--accent">关键步骤</span>
      <span class="chip">常规步骤</span>
    </div>
  </div>
</section>

<!-- ══ A3 管线页（全宽 SVG） ══ -->
<section class="band band--fit" id="arch3">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">03 · 端到端链路</div>
      <h2 class="t-h1 shead__title">请求到交付：五段管线全程可审计</h2>
    </div>
    <figure class="fig fig--full rv">
      <svg class="chart" data-chart="gantt" viewBox="0 0 900 240" style="width:100%">
        <rect data-anim="fade" x="20"  y="80" width="150" height="52" rx="10" class="f-acc"/>
        <text x="95" y="103" text-anchor="middle" class="t-on-inv" font-size="14" font-weight="600">受理</text>
        <text x="95" y="122" text-anchor="middle" class="t-on-inv" font-size="11">目标与约束</text>
        <path d="M170 106 L200 106" class="s-txt3" stroke-width="2" stroke-dasharray="4 4"/>
        <polygon points="200,101 210,106 200,111" class="f-txt3"/>
        <rect data-anim="fade" x="210" y="80" width="150" height="52" rx="10" class="f-s2"/>
        <text x="285" y="103" text-anchor="middle" class="f-txt" font-size="14" font-weight="600">规划</text>
        <text x="285" y="122" text-anchor="middle" class="f-txt3" font-size="11">任务拆解</text>
        <path d="M360 106 L390 106" class="s-txt3" stroke-width="2" stroke-dasharray="4 4"/>
        <polygon points="390,101 400,106 390,111" class="f-txt3"/>
        <rect data-anim="fade" x="400" y="80" width="150" height="52" rx="10" class="f-s2"/>
        <text x="475" y="103" text-anchor="middle" class="f-txt" font-size="14" font-weight="600">执行</text>
        <text x="475" y="122" text-anchor="middle" class="f-txt3" font-size="11">工具调用</text>
        <path d="M550 106 L580 106" class="s-txt3" stroke-width="2" stroke-dasharray="4 4"/>
        <polygon points="580,101 590,106 580,111" class="f-txt3"/>
        <rect data-anim="fade" x="590" y="80" width="150" height="52" rx="10" class="f-s2"/>
        <text x="665" y="103" text-anchor="middle" class="f-txt" font-size="14" font-weight="600">核验</text>
        <text x="665" y="122" text-anchor="middle" class="f-txt3" font-size="11">护栏与审计</text>
        <path d="M740 106 L770 106" class="s-txt3" stroke-width="2" stroke-dasharray="4 4"/>
        <polygon points="770,101 780,106 770,111" class="f-txt3"/>
        <rect data-anim="fade" x="780" y="80" width="100" height="52" rx="10" class="f-acc"/>
        <text x="830" y="103" text-anchor="middle" class="t-on-inv" font-size="14" font-weight="600">交付</text>
        <text x="830" y="122" text-anchor="middle" class="t-on-inv" font-size="11">回写记忆</text>
      </svg>
      <figcaption class="fig__cap" style="margin-top:var(--sp-4)">数据全链路：五段管线，每段留痕可回溯</figcaption>
    </figure>
  </div>
</section>

<!-- ══ 金字塔页（pyramid）：平台建设的三级递进 ══ -->
<section class="band band--fit" id="arch4">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">04 · 建设递进</div>
      <h2 class="t-h1 shead__title">三级递进：先接得进来，再管得住，最后放得开</h2>
    </div>
    <div class="pyr rv">
      <div class="pyr__lvl" style="--w:46%">
        <div class="pyr__t">放得开</div>
        <div class="pyr__d">自动执行</div>
      </div>
      <div class="pyr__lvl pyr__lvl--a" style="--w:72%">
        <div class="pyr__t">管得住</div>
        <div class="pyr__d">权限、审计、回退内嵌平台层（当前焦点）</div>
      </div>
      <div class="pyr__lvl" style="--w:100%">
        <div class="pyr__t">接得进来</div>
        <div class="pyr__d">统一编排收敛工具、记忆与模型接入</div>
      </div>
    </div>
    <div class="t-xs rv" style="margin-top:var(--sp-5);color:var(--text-3)">递进依据：节点命名与分层口径见 <a class="cite" href="#ref-1">[1]</a></div>
  </div>
</section>

<!-- ══ 收尾页（极简） ══ -->
<section class="band band--accent band--fit" id="next">
  <div class="wrap">
    <div class="shead shead--center rv">
      <div class="t-eyebrow">结论</div>
      <h2 class="t-h1 shead__title">让智能体在护栏内真正干活</h2>
      <p class="t-lead shead__desc">三层解耦 + 统一编排 + 全程审计。</p>
    </div>
    <div class="row row-wrap rv" style="justify-content:center;gap:var(--sp-4);margin-top:var(--sp-5)">
      <span class="chip chip--accent">三层解耦</span>
      <span class="chip" style="background:color-mix(in srgb,var(--surface) 10%,transparent)">统一护栏</span>
      <span class="chip" style="background:color-mix(in srgb,var(--surface) 10%,transparent)">全程留痕</span>
    </div>
    <div class="row" style="justify-content:center;gap:var(--sp-3);margin-top:clamp(28px,3.4vh,44px)">
      <a class="btn btn--primary" href="#arch1">返回看图</a>
    </div>
  </div>
</section>

<!-- ══ 参考资料 ══ -->
<section class="band band--tint" id="refs">
  <div class="wrap">
    <div class="shead rv">
      <div class="t-eyebrow">参考资料</div>
      <h2 class="t-h1 shead__title">依据与口径说明</h2>
    </div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th style="width:6%">编号</th><th style="width:26%">来源</th>
          <th style="width:14%">时间</th><th>口径说明</th></tr></thead>
        <tbody>
          <tr id="ref-1"><td class="k">[1]</td>
            <td><a class="ref-link" href="https://example.com/agent-platform-whitepaper" target="_blank" rel="noopener">企业智能体平台架构白皮书（内部）
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><path d="M15 3h6v6M10 14 21 3"/></svg></a></td>
            <td>2026-08</td><td>分层与节点命名依据</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ══ 页脚 ══ -->
<footer class="foot">
  <div class="wrap foot__in">
    <div class="brand">
      <div class="brand__mark">AI</div>
      <div class="brand__txt">
        <div class="brand__title">企业智能体平台总体架构</div>
        <div class="brand__sub">方案架构 · ''' + DATE + '''</div>
      </div>
    </div>
    <div class="t-xs">内部资料 · 请勿外传</div>
  </div>
</footer>'''

A_MODEL = {
    "mode": "architecture", "style": "graphite-dark",
    "title": "企业智能体平台总体架构",
    "subtitle": "三层解耦 · 统一护栏",
    "meta": "方案评审材料 · " + DATE,
    "sections": [
        {"type": "diagram", "eyebrow": "01 · 总体架构", "title": "三层解耦：模型、编排、应用各司其职",
         "layers": [["应用层", [{"t": "智能客服", "d": "7×24 自主应答", "accent": True},
                                {"t": "研发副驾", "d": "代码与知识库操作"},
                                {"t": "数据管家", "d": "口径自动核验"}], "focus"],
                    ["编排层", [{"t": "任务规划", "d": "目标拆解与分派"},
                                {"t": "工具调度", "d": "千级工具统一注册"},
                                {"t": "记忆检索", "d": "任务级长期记忆"}]],
                    ["模型层", [{"t": "多模型接入", "d": "按场景路由"},
                                {"t": "统一网关", "d": "配额与降级"}]]],
         "legend": ["当前建设焦点", "已有能力"]},
        {"type": "lane", "eyebrow": "02 · 协作流程", "title": "一次任务请求的五步闭环",
         "lanes": [["业务方", ["下达目标", "拆任务", {"t": "人审核", "accent": True}]],
                   ["编排层", [{"t": "规划校验", "accent": True}, "工具调用", "全程留痕"]],
                   ["执行层", ["调用模型", "产出结果", "回写记忆"]]]},
        {"type": "lane", "eyebrow": "03 · 端到端链路", "title": "请求到交付：五段管线全程可审计",
         "lanes": [["数据流", [{"t": "受理", "accent": True}, "规划", "执行", "核验", {"t": "交付", "accent": True}]]]},
        {"type": "pyramid", "eyebrow": "04 · 建设递进", "title": "三级递进：先接得进来，再管得住，最后放得开",
         "levels": [["放得开", "自动执行"],
                    {"t": "管得住", "d": "权限、审计、回退内嵌平台层（当前焦点）", "accent": True},
                    ["接得进来", "统一编排收敛工具、记忆与模型接入"]],
         "footnote": "递进依据：节点命名与分层口径见[1]"},
    ],
    "closing": {"title": "让智能体在护栏内真正干活",
                "points": [["三层解耦", "模型 / 编排 / 应用各司其职"],
                           ["统一护栏", "权限与审计内嵌每一层"],
                           ["全程留痕", "每段管线可回溯可回退"]]},
}

# ══════════════════════════════════════════════════════════════════════════
#  示例矩阵定义
# ══════════════════════════════════════════════════════════════════════════
EXAMPLES = [
    # presentation × 2
    dict(mode='presentation', style='business-blue',
         fname=f'{DATE}-presentation-business-blue.html',
         title_tag='AI 智能体：从工具到同事 · TopPPT HTML 演示模式样例',
         nav_swaps=[('>章节一</a>', '>范式跃迁</a>'), ('>章节二</a>', '>形态边界</a>')],
         content=P_CONTENT, model=P_MODEL,
         probes=['id="agenda"', 'data-chart="donut"', 'data-chart="bar"', 'class="cite"',
                 'class="steps', 'class="bul', 'band--accent',
                 'class="media media--r3-1 media--ph', 'class="media__ph']),
    dict(mode='presentation', style='apple-mono',
         fname=f'{DATE}-presentation-apple-mono.html',
         title_tag='AI 智能体：从工具到同事 · TopPPT HTML 演示模式样例（优雅黑白）',
         nav_swaps=[('>章节一</a>', '>范式跃迁</a>'), ('>章节二</a>', '>形态边界</a>')],
         content=P_CONTENT, model=P_MODEL,
         probes=['id="agenda"', 'data-chart="donut"', 'data-chart="bar"', 'class="cite"',
                 'class="steps', 'class="bul', 'band--accent',
                 'class="media media--r3-1 media--ph', 'class="media__ph']),
    dict(mode='presentation', style='brand-red',
         fname=f'{DATE}-presentation-brand-red.html',
         title_tag='AI 智能体：从工具到同事 · TopPPT HTML 演示模式样例（品牌红）',
         nav_swaps=[('>章节一</a>', '>范式跃迁</a>'), ('>章节二</a>', '>形态边界</a>')],
         content=P_CONTENT, model=P_MODEL,
         probes=['id="agenda"', 'data-chart="donut"', 'data-chart="bar"', 'class="cite"',
                 'class="steps', 'class="bul', 'band--accent',
                 'class="media media--r3-1 media--ph', 'class="media__ph']),
    # research × 3
    dict(mode='research', style='mckinsey',
         fname=f'{DATE}-research-mckinsey.html',
         title_tag='2026 AI 智能体发展研究报告 · TopPPT HTML 研究模式样例',
         nav_swaps=[('>章节一</a>', '>范式分水岭</a>'), ('>章节二</a>', '>形态边界</a>')],
         content=R_CONTENT, model=R_MODEL,
         probes=['class="exhibit__no"', 'class="cols-2', 'class="cols-3', 'g-half',
                 'class="matrix__grid"', 'class="sowhat', 'id="refs"',
                 'class="heat', 'class="pyr', 'class="flagbar', 'class="tbd', 'band--accent',
                 'data-chart="waterfall"', 'data-chart="sankey"', 'data-chart="treemap"',
                 'data-chart="boxplot"', 'data-chart="network"', 'data-chart="marimekko"',
                 'data-chart="streamgraph"', 'data-chart="gantt"', 'data-chart="rose"',
                 'data-chart="candlestick"',
                 'class="media-grid media-grid--4', 'class="media media--r4-3 media--ph']),
    dict(mode='research', style='deep-teal',
         fname=f'{DATE}-research-deep-teal.html',
         title_tag='2026 AI 智能体发展研究报告 · TopPPT HTML 研究模式样例（墨绿）',
         nav_swaps=[('>章节一</a>', '>范式分水岭</a>'), ('>章节二</a>', '>形态边界</a>')],
         content=R_CONTENT, model=R_MODEL,
         probes=['class="exhibit__no"', 'class="cols-2', 'class="cols-3', 'g-half',
                 'class="matrix__grid"', 'class="sowhat', 'id="refs"',
                 'class="heat', 'class="pyr', 'class="flagbar', 'class="tbd', 'band--accent',
                 'data-chart="waterfall"', 'data-chart="sankey"', 'data-chart="treemap"',
                 'data-chart="boxplot"', 'data-chart="network"', 'data-chart="marimekko"',
                 'data-chart="streamgraph"', 'data-chart="gantt"', 'data-chart="rose"',
                 'data-chart="candlestick"',
                 'class="media-grid media-grid--4', 'class="media media--r4-3 media--ph']),
    dict(mode='research', style='warm-sand',
         fname=f'{DATE}-research-warm-sand.html',
         title_tag='2026 AI 智能体发展研究报告 · TopPPT HTML 研究模式样例（暖沙金）',
         nav_swaps=[('>章节一</a>', '>范式分水岭</a>'), ('>章节二</a>', '>形态边界</a>')],
         content=R_CONTENT, model=R_MODEL,
         probes=['class="exhibit__no"', 'class="cols-2', 'class="cols-3', 'g-half',
                 'class="matrix__grid"', 'class="sowhat', 'id="refs"',
                 'class="heat', 'class="pyr', 'class="flagbar', 'class="tbd', 'band--accent',
                 'data-chart="waterfall"', 'data-chart="sankey"', 'data-chart="treemap"',
                 'data-chart="boxplot"', 'data-chart="network"', 'data-chart="marimekko"',
                 'data-chart="streamgraph"', 'data-chart="gantt"', 'data-chart="rose"',
                 'data-chart="candlestick"',
                 'class="media-grid media-grid--4', 'class="media media--r4-3 media--ph']),
    dict(mode='research', style='indigo-violet',
         fname=f'{DATE}-research-indigo-violet.html',
         title_tag='2026 AI 智能体发展研究报告 · TopPPT HTML 研究模式样例（靛紫）',
         nav_swaps=[('>章节一</a>', '>范式分水岭</a>'), ('>章节二</a>', '>形态边界</a>')],
         content=R_CONTENT, model=R_MODEL,
         probes=['class="exhibit__no"', 'class="cols-2', 'class="cols-3', 'g-half',
                 'class="matrix__grid"', 'class="sowhat', 'id="refs"',
                 'class="heat', 'class="pyr', 'class="flagbar', 'class="tbd', 'band--accent',
                 'data-chart="waterfall"', 'data-chart="sankey"', 'data-chart="treemap"',
                 'data-chart="boxplot"', 'data-chart="network"', 'data-chart="marimekko"',
                 'data-chart="streamgraph"', 'data-chart="gantt"', 'data-chart="rose"',
                 'data-chart="candlestick"',
                 'class="media-grid media-grid--4', 'class="media media--r4-3 media--ph']),
    # architecture × 2（graphite 出厂 dark · 深色优先；spectrum light）
    dict(mode='architecture', style='graphite-dark', theme='dark',
         fname=f'{DATE}-architecture-graphite-dark.html',
         title_tag='企业智能体平台总体架构 · TopPPT HTML 架构模式样例（石墨深灰 · 深色优先）',
         nav_swaps=[],
         content=A_CONTENT, model=A_MODEL,
         probes=['class="arch__layer', 'class="lane__step', 'data-chart="gantt"', 'id="refs"',
                 'class="pyr', 'band--accent',
                 'data-mode="architecture" data-style="graphite-dark" data-theme="dark"']),
    dict(mode='architecture', style='spectrum', theme='light',
         fname=f'{DATE}-architecture-spectrum.html',
         title_tag='企业智能体平台总体架构 · TopPPT HTML 架构模式样例（彩色）',
         nav_swaps=[],
         content=A_CONTENT, model=A_MODEL,
         probes=['class="arch__layer', 'class="lane__step', 'data-chart="gantt"', 'id="refs"',
                 'class="pyr', 'band--accent',
                 'data-mode="architecture" data-style="spectrum" data-theme="light"']),
]

TPL_DEFAULT_STYLE = {'presentation': 'business-blue', 'research': 'mckinsey',
                     'architecture': 'graphite-dark'}
TPL_TITLE_TAG = {'presentation': '报告标题', 'research': '研究报告标题', 'architecture': '架构标题'}
TPL_BRAND = {
    'presentation': [('主标题', 'AI 智能体发展研究'), ('副标题 / 专题名', '从工具到同事')],
    'research': [('报告标题', 'AI 智能体发展研究'), ('研究报告 · 专题名', '2026 年度研究报告')],
    'architecture': [('架构标题', '智能体平台架构'), ('方案架构 · 专题名', '三层解耦 · 统一护栏')],
}


def build(ex):
    mode, style, fname = ex['mode'], ex['style'], ex['fname']
    tpl_path = TPL / f'{mode}.html'
    t = tpl_path.read_text(encoding='utf-8')

    # 风格 / 标题 / 品牌 / 导航（均为首次出现替换；html 标签在各标记块之前）
    t = t.replace(f'data-style="{TPL_DEFAULT_STYLE[mode]}"', f'data-style="{style}"', 1)
    # 主题（architecture 模板出厂 dark；ex['theme'] 指定该示例的实际出厂主题）
    theme = ex.get('theme')
    if theme:
        t = re.sub(r'(<html[^>]*data-theme=")[^"]*(")', r'\g<1>' + theme + r'\g<2>', t, count=1)
        assert f'data-mode="{mode}" data-style="{style}" data-theme="{theme}"' in t, \
            f'{fname}: 主题注入失败（期望 {theme}）'
    t = t.replace(f'<title>{TPL_TITLE_TAG[mode]}</title>', f'<title>{ex["title_tag"]}</title>', 1)
    for old, new in TPL_BRAND[mode]:
        t = t.replace(f'>{old}</div>', f'>{new}</div>', 1)
    for old, new in ex['nav_swaps']:
        t = t.replace(old, new, 1)

    # 内容区整体替换（非贪婪 + 前置存在断言，防静默截断）
    assert CONTENT_RE.search(t), f'{tpl_path.name} 缺少 __TOPPPT_CONTENT__ 标记'
    t = CONTENT_RE.sub('<!-- __TOPPPT_CONTENT_START__ -->\n' + ex['content'] +
                       '\n<!-- __TOPPPT_CONTENT_END__ -->', t, count=1)
    for probe in ex['probes']:
        assert probe in t, f'{fname}: 内容注入后缺少关键组件 {probe}'

    # 模型注入（与正文同步；严格 JSON）
    assert MODEL_RE.search(t), f'{tpl_path.name} 缺少 REPORT_MODEL 块'
    model = dict(ex['model'])
    model['style'] = style
    model['theme'] = ex.get('theme', 'light')   # 模型与页面 data-theme 同步（PPTX 按此导出亮/暗版）
    t = MODEL_RE.sub('window.REPORT_MODEL = ' +
                     json.dumps(model, ensure_ascii=False, indent=2) + ';', t, count=1)
    # 注入后完整性断言：模型 mode 与 data-mode 一致 + 预览运行时 API 未被截断
    assert f'"mode": "{mode}"' in t and f'data-mode="{mode}"' in t, f'{fname}: mode 不一致'
    assert 'g.TopPptHtml = api' in t and 'function slidesXml' in t, f'{fname}: 预览运行时缺失'

    (OUT / fname).write_text(t, encoding='utf-8')
    print(f'written: {fname}  {len(t)} chars  ({mode} x {style})')


def main():
    OUT.mkdir(exist_ok=True)
    for ex in EXAMPLES:
        build(ex)
    print(f'完成：三模式示例矩阵（AI 智能体主题，{len(EXAMPLES)} 个）已刷新到 {OUT}')
    print('下一步回归：validate_report -> extract_model -> build_pptx -> validate_pptx --strict --model')


if __name__ == '__main__':
    main()
