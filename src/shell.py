"""Shared HTML shell (CSS design system + navigation) for the GenericAgent
visual guide.

This module is the single source of truth for the bilingual (中文/English)
page chrome: the CSS design system, the top bar, the language toggle, the
progress bar, the footer navigation, and the index/TOC page.

Bilingual mechanism: the active language is chosen by a CSS class on
``<html>`` — ``html.lang-zh`` shows Chinese and hides English, ``html.lang-en``
does the reverse. Pages default to ``lang-zh`` (no flash for default users) and
an inline ``<head>`` script restores the user's saved choice (``galang`` in
``localStorage``) before the body renders, so there is no flash of the wrong
language. All chrome that differs by language uses :func:`i18n.bi` inline spans.
"""

import base64
from collections import namedtuple

from i18n import bi

# ---- favicon (inline SVG, base64): rounded square, white "GA" on accent ----
_FAVICON_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
    "<rect width='32' height='32' rx='7' fill='#5b4ddb'/>"
    "<text x='16' y='22' font-family='system-ui,sans-serif' font-size='14'"
    " font-weight='700' fill='#fff' text-anchor='middle'>GA</text></svg>"
)
FAVICON = "data:image/svg+xml;base64," + base64.b64encode(_FAVICON_SVG.encode()).decode()

INDEX_FILE = "index.html"

# Bilingual site name, reused across chrome.
SITE_NAME = bi("GenericAgent 图解教程", "GenericAgent Visual Guide")


def _esc(s):
    """Escape text for HTML element content / titles (& and < and >)."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def head_meta(title, description, og_type="website"):
    """SEO / social meta tags + favicon for a page <head> (zh meta is fine)."""
    t = title.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")
    d = description.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")
    return (
        f'<meta name="description" content="{d}">\n'
        f'<meta name="theme-color" content="#5b4ddb">\n'
        f'<link rel="icon" type="image/svg+xml" href="{FAVICON}">\n'
        f'<meta property="og:type" content="{og_type}">\n'
        f'<meta property="og:site_name" content="GenericAgent 图解教程">\n'
        f'<meta property="og:title" content="{t}">\n'
        f'<meta property="og:description" content="{d}">\n'
        f'<meta name="twitter:card" content="summary">\n'
        f'<meta name="twitter:title" content="{t}">\n'
        f'<meta name="twitter:description" content="{d}">'
    )


# Inline <head> script: set the language class + lang attr BEFORE body render
# (FOUC-free), so the right language shows immediately and a11y/SEO lang is correct.
FOUC_SCRIPT = (
    "var _l=localStorage.getItem('galang')||'zh';"
    "document.documentElement.className='lang-'+_l;"
    "document.documentElement.lang=(_l==='zh')?'zh-CN':'en';"
)

# ---- bilingual page model ----
Page = namedtuple("Page", "fname title_zh title_en part_zh part_en")

_P1_ZH, _P1_EN = "第一部分 · 宏观全景", "Part 1 · The Big Picture"
_P2_ZH, _P2_EN = "第二部分 · 用户视角", "Part 2 · Using It"
_P3_ZH, _P3_EN = "第三部分 · 内部源码", "Part 3 · Inside the Source"
_P4_ZH, _P4_EN = "第四部分 · 进阶能力", "Part 4 · Advanced Capabilities"
_P5_ZH, _P5_EN = "第五部分 · 实战", "Part 5 · Hands-On"
_P6_ZH, _P6_EN = "第六部分 · 速查", "Part 6 · Reference"

PAGES = [
    Page("01-what-is-ga.html", "GenericAgent 是什么", "What is GenericAgent", _P1_ZH, _P1_EN),
    Page("02-project-map.html", "项目全景地图", "Project Map", _P1_ZH, _P1_EN),
    Page("03-task-lifecycle.html", "一次任务的生命周期", "Lifecycle of a Task", _P1_ZH, _P1_EN),
    Page("04-install.html", "安装与启动", "Install & Launch", _P2_ZH, _P2_EN),
    Page("05-frontends.html", "前端形态总览", "Frontends Overview", _P2_ZH, _P2_EN),
    Page("06-commands.html", "对话与斜杠命令", "Chat & Slash Commands", _P2_ZH, _P2_EN),
    Page("07-tools.html", "九个原子工具", "The Nine Atomic Tools", _P2_ZH, _P2_EN),
    Page("08-agent-loop.html", "Agent Loop 核心拆解", "The Agent Loop", _P3_ZH, _P3_EN),
    Page("09-llmcore.html", "LLM 内核 llmcore.py", "The LLM Core", _P3_ZH, _P3_EN),
    Page("10-handler-dispatch.html", "Handler 与工具调度", "Handler & Tool Dispatch", _P3_ZH, _P3_EN),
    Page("11-layered-memory.html", "分层记忆系统 L0–L4", "Layered Memory (L0–L4)", _P3_ZH, _P3_EN),
    Page("12-memory-crystallize.html", "记忆的读写与结晶", "Memory & Crystallization", _P3_ZH, _P3_EN),
    Page("13-hooks-observability.html", "钩子与可观测性", "Hooks & Observability", _P3_ZH, _P3_EN),
    Page("14-context-tokens.html", "上下文工程与 Token 效率", "Context Engineering & Token Efficiency", _P3_ZH, _P3_EN),
    Page("15-vision.html", "计算机控制 · 视觉", "Computer Control · Vision", _P4_ZH, _P4_EN),
    Page("16-input-mobile.html", "输入与移动端", "Input & Mobile (ADB)", _P4_ZH, _P4_EN),
    Page("17-browser.html", "浏览器注入与 Web 工具", "Browser Injection & Web Tools", _P4_ZH, _P4_EN),
    Page("18-reflect-orchestration.html", "反思与编排", "Reflection & Orchestration", _P4_ZH, _P4_EN),
    Page("19-autonomy.html", "长期自治与定时任务", "Long-Horizon Autonomy", _P4_ZH, _P4_EN),
    Page("20-self-evolution.html", "自进化机制详解", "The Self-Evolution Mechanism", _P5_ZH, _P5_EN),
    Page("21-build-a-skill.html", "端到端实战：造一个新技能", "End-to-End: Build a Skill", _P5_ZH, _P5_EN),
    Page("22-extend-frontend.html", "扩展前端 / 接入新 IM", "Extending Frontends", _P5_ZH, _P5_EN),
    Page("23-evaluation.html", "为什么强：定位 · 评测 · 技术报告", "Why It's Strong: Positioning & Evaluation", _P6_ZH, _P6_EN),
    Page("24-glossary.html", "术语表 + 源文件索引", "Glossary & Source Index", _P6_ZH, _P6_EN),
]

# One-line bilingual subtitles for the TOC, keyed by fname → (zh, en).
SUBTITLES = {
    "01-what-is-ga.html": ("解决什么问题 · 核心心智模型", "What it solves · core mental model"),
    "02-project-map.html": ("目录结构 · 模块职责一图看懂", "Directory layout · module responsibilities"),
    "03-task-lifecycle.html": ("从一句指令到结果的完整数据流", "From prompt to result, end to end"),
    "04-install.html": ("依赖 · 配置 · 第一次跑起来", "Dependencies · config · first run"),
    "05-frontends.html": ("CLI / Web / IM 等前端形态", "CLI / Web / IM front-ends"),
    "06-commands.html": ("自然语言对话 + 斜杠命令", "Natural chat plus slash commands"),
    "07-tools.html": ("九个原子工具各司其职", "The nine atomic tools at a glance"),
    "08-agent-loop.html": ("感知 → 决策 → 行动的主循环", "The perceive–decide–act main loop"),
    "09-llmcore.html": ("llmcore.py 如何调用大模型", "How llmcore.py talks to the LLM"),
    "10-handler-dispatch.html": ("解析模型输出 · 分发到工具", "Parse model output · dispatch to tools"),
    "11-layered-memory.html": ("L0–L4 五层记忆各自的角色", "The roles of memory layers L0–L4"),
    "12-memory-crystallize.html": ("记忆的读写、压缩与结晶", "Reading, writing and crystallizing memory"),
    "13-hooks-observability.html": ("钩子机制 · 日志与可观测性", "Hooks · logging and observability"),
    "14-context-tokens.html": ("如何把上下文压到 &lt;30K", "Keeping the context under 30K"),
    "15-vision.html": ("截屏理解 · 视觉驱动控制", "Screenshot understanding · vision control"),
    "16-input-mobile.html": ("键鼠输入 · ADB 操控移动端", "Keyboard/mouse · ADB mobile control"),
    "17-browser.html": ("注入脚本 · 浏览器与 Web 工具", "Script injection · browser & web tools"),
    "18-reflect-orchestration.html": ("自我反思 · 多步任务编排", "Self-reflection · multi-step orchestration"),
    "19-autonomy.html": ("长任务自治 · 定时与触发", "Autonomous long tasks · scheduling"),
    "20-self-evolution.html": ("Agent 如何改进自己", "How the agent improves itself"),
    "21-build-a-skill.html": ("从零造一个新技能的全过程", "Build a brand-new skill from scratch"),
    "22-extend-frontend.html": ("接入新 IM / 自定义前端", "Add a new IM / custom front-end"),
    "23-evaluation.html": ("定位 · 横向对比 · 五维评测 · 论文", "Positioning · comparison · evaluation · paper"),
    "24-glossary.html": ("术语一句话查 + 源文件索引", "One-line glossary + source index"),
}

CSS = r"""
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --bg: #f6f7f9; --panel: #ffffff; --panel-2: #f0f2f5; --ink: #1d2129;
  --muted: #5b6470; --faint: #646b74; --line: #e1e5ea;
  --accent: #5b4ddb; --accent-soft: #ece9fc; --accent-ink: #3a2ea3;
  --blue: #2563eb; --blue-soft: #e7efff; --amber: #b4690e; --amber-soft: #fdf1dd;
  --purple: #7c3aed; --purple-soft: #f0e9ff; --red: #d23f3f; --red-soft: #fbe6e6;
  --code-bg: #0f172a; --code-ink: #e2e8f0; --code-line: #1e293b;
  --shadow: 0 1px 2px rgba(16,24,40,.06), 0 8px 24px rgba(16,24,40,.06);
  --radius: 14px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0e1116; --panel: #161b22; --panel-2: #1c232c; --ink: #e6edf3;
    --muted: #9aa6b2; --faint: #8a96a3; --line: #2a323c;
    --accent: #9d8df3; --accent-soft: #211b46; --accent-ink: #c9c0f8;
    --blue: #6ea8fe; --blue-soft: #16243f; --amber: #e0a44a; --amber-soft: #33270f;
    --purple: #b794f6; --purple-soft: #271a40; --red: #f08080; --red-soft: #3a1a1a;
    --code-bg: #0a0f1a; --code-ink: #d8e2f0; --code-line: #14202f;
    --shadow: 0 1px 2px rgba(0,0,0,.4), 0 10px 30px rgba(0,0,0,.35);
  }
}

/* ---- bilingual language switch (driven by html.lang-* class) ---- */
html.lang-zh .en { display: none !important; }
html.lang-en .zh { display: none !important; }

html { scroll-behavior: smooth; overflow-x: hidden; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC",
    "PingFang SC", "Microsoft YaHei", system-ui, sans-serif;
  background: var(--bg); color: var(--ink); line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); text-decoration: none; }
code, .mono { font-family: "SF Mono", "JetBrains Mono", "Fira Code", ui-monospace, Menlo, Consolas, monospace; overflow-wrap: break-word; }

/* ---- top progress bar ---- */
.topbar {
  position: sticky; top: 0; z-index: 50; background: var(--panel);
  border-bottom: 1px solid var(--line); backdrop-filter: blur(8px);
}
.topbar-inner {
  max-width: 960px; margin: 0 auto; padding: .7rem 1.25rem;
  display: flex; align-items: center; justify-content: space-between; gap: 1rem;
}
.topbar .home { font-size: .82rem; color: var(--muted); font-weight: 600; display:flex; gap:.5rem; align-items:center; }
.topbar .home b { color: var(--accent); }
.topbar .pill { font-size: .72rem; color: var(--muted); background: var(--panel-2);
  padding: .2rem .6rem; border-radius: 999px; border: 1px solid var(--line); white-space: nowrap; }
.topbar .spacer { margin-left: auto; }

/* ---- language toggle pill button ---- */
.lang-btn { font-size: .72rem; font-weight: 700; color: var(--muted); background: var(--panel-2);
  padding: .25rem .7rem; border-radius: 999px; border: 1px solid var(--line); cursor: pointer;
  white-space: nowrap; transition: .15s; font-family: inherit; }
.lang-btn:hover { border-color: var(--accent); color: var(--accent); }

.progress { height: 3px; background: var(--panel-2); }
.progress > span { display: block; height: 100%; background: linear-gradient(90deg, var(--accent), var(--blue)); }

.wrap { max-width: 820px; margin: 0 auto; padding: 2.4rem 1.25rem 5rem; }

/* ---- hero ---- */
.hero { margin-bottom: 2rem; }
.hero .part { font-size: .76rem; letter-spacing: .08em; text-transform: uppercase;
  color: var(--accent); font-weight: 700; margin-bottom: .55rem; }
.hero h1 { font-size: 2.05rem; line-height: 1.2; letter-spacing: -.01em; font-weight: 750; }
.hero .lead { margin-top: .9rem; font-size: 1.06rem; color: var(--muted); }

h2 { font-size: 1.32rem; margin: 2.4rem 0 .9rem; letter-spacing: -.01em;
  display: flex; align-items: center; gap: .55rem; }
h2::before { content: ""; width: 4px; height: 1.05em; background: var(--accent); border-radius: 3px; display: inline-block; }
h3 { font-size: 1.05rem; margin: 1.4rem 0 .5rem; }
p { margin: .7rem 0; }
ul, ol { margin: .6rem 0 .6rem 1.3rem; }
li { margin: .3rem 0; }
strong { color: var(--ink); font-weight: 680; }
.inline { background: var(--panel-2); border: 1px solid var(--line); border-radius: 6px;
  padding: .08em .4em; font-size: .9em; color: var(--accent-ink); }

/* ---- callout cards ---- */
.card { border-radius: var(--radius); padding: 1.05rem 1.2rem; margin: 1.2rem 0;
  border: 1px solid var(--line); background: var(--panel); box-shadow: var(--shadow); }
.card .tag { font-size: .72rem; font-weight: 700; letter-spacing: .04em; text-transform: uppercase;
  display: inline-flex; align-items: center; gap: .4rem; margin-bottom: .5rem; }
.card.macro { border-left: 4px solid var(--blue); }
.card.macro .tag { color: var(--blue); }
.card.detail { border-left: 4px solid var(--purple); }
.card.detail .tag { color: var(--purple); }
.card.analogy { border-left: 4px solid var(--amber); background: var(--amber-soft); }
.card.analogy .tag { color: var(--amber); }
.card.key { border-left: 4px solid var(--accent); background: var(--accent-soft); }
.card.key .tag { color: var(--accent-ink); }
.card.warn { border-left: 4px solid var(--red); background: var(--red-soft); }
.card.warn .tag { color: var(--red); }
.card.spark { border-left: 4px solid #e0a000;
  background: linear-gradient(100deg, rgba(224,160,0,.12), transparent 70%); }
.card.spark .tag { color: #c98a00; }
@media (prefers-color-scheme: dark) { .card.spark .tag { color: #f0c050; } }

/* ---- code file callout ---- */
.codefile { margin: 1.2rem 0; border-radius: 12px; overflow: hidden; border: 1px solid var(--line);
  box-shadow: var(--shadow); }
.codefile .cf-head { display: flex; align-items: center; gap: .55rem; padding: .5rem .85rem;
  background: var(--panel-2); border-bottom: 1px solid var(--line); font-size: .8rem; }
.codefile .cf-head .dot { width: 9px; height: 9px; border-radius: 50%; background: var(--accent); flex-shrink:0; }
.codefile .cf-head .path { font-family: ui-monospace, monospace; color: var(--ink); font-weight: 600; }
.codefile .cf-head .ln { margin-left: auto; color: var(--faint); font-size: .72rem; }
.codefile pre { background: var(--code-bg); color: var(--code-ink); padding: .9rem 1rem;
  overflow-x: auto; font-size: .82rem; line-height: 1.6; }
.codefile pre .cm { color: #7d8aa3; }
.codefile pre .kw { color: #c792ea; }
.codefile pre .fn { color: #82aaff; }
.codefile pre .st { color: #c3e88d; }
.codefile pre .nb { color: #f78c6c; }

pre.code { background: var(--code-bg); color: var(--code-ink); padding: .9rem 1rem; border-radius: 12px;
  overflow-x: auto; font-size: .83rem; line-height: 1.6; margin: 1.1rem 0; box-shadow: var(--shadow); }
pre.code .cm { color: #7d8aa3; } pre.code .kw { color: #c792ea; }
pre.code .fn { color: #82aaff; } pre.code .st { color: #c3e88d; } pre.code .nb { color: #f78c6c; }

/* ---- collapsible accordion (details/summary) ---- */
.accordion { border: 1px solid var(--line); border-radius: 12px; background: var(--panel);
  margin: .7rem 0; box-shadow: var(--shadow); overflow: hidden; }
.accordion > summary { cursor: pointer; padding: .85rem 1.1rem; font-weight: 650; font-size: .96rem;
  list-style: none; display: flex; align-items: center; gap: .6rem; user-select: none; }
.accordion > summary::-webkit-details-marker { display: none; }
.accordion > summary::after { content: "▶"; font-size: .68rem; color: var(--accent);
  margin-left: auto; transition: transform .15s ease; }
.accordion[open] > summary::after { transform: rotate(90deg); }
.accordion > summary:hover { background: var(--panel-2); }
.accordion[open] > summary { border-bottom: 1px solid var(--line); }
.accordion .badge-num { background: var(--accent-soft); color: var(--accent-ink);
  width: 1.6rem; height: 1.6rem; border-radius: 7px; display: inline-flex; align-items: center;
  justify-content: center; font-size: .82rem; font-weight: 700; flex-shrink: 0; }
.accordion .hint { font-size: .72rem; color: var(--faint); font-weight: 400; }
.acc-body { padding: .9rem 1.1rem 1.1rem; }
.acc-intro { color: var(--muted); font-size: .9rem; margin: .2rem 0 .4rem; }
.qa { margin: 1rem 0; }
.qa:first-child { margin-top: .3rem; }
.qa .q { font-weight: 680; font-size: .9rem; display: flex; gap: .45rem; align-items: center; margin-bottom: .3rem; }
.qa .a { color: var(--muted); font-size: .9rem; }
.qa .a strong { color: var(--ink); }
.qa pre.code { margin: .5rem 0 0; font-size: .78rem; }

/* ---- flow diagram ---- */
.flow { display: flex; align-items: stretch; gap: 0; flex-wrap: wrap; margin: 1.3rem 0;
  background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius);
  padding: 1.2rem 1rem; box-shadow: var(--shadow); }
.flow .node { flex: 1 1 0; min-width: 110px; text-align: center; padding: .7rem .5rem;
  border-radius: 10px; background: var(--panel-2); border: 1px solid var(--line); }
.flow .node .nt { font-weight: 700; font-size: .92rem; }
.flow .node .nd { font-size: .76rem; color: var(--muted); margin-top: .2rem; }
.flow .node.hl { background: var(--accent-soft); border-color: var(--accent); }
.flow .arrow { align-self: center; color: var(--faint); font-size: 1.3rem; padding: 0 .35rem; }

/* vertical flow */
.vflow { margin: 1.3rem 0; }
.vflow .step { display: flex; gap: .9rem; position: relative; padding-bottom: 1.1rem; }
.vflow .step:not(:last-child)::before { content:""; position:absolute; left: 15px; top: 34px; bottom: -2px;
  width: 2px; background: var(--line); }
.vflow .num { width: 32px; height: 32px; border-radius: 50%; background: var(--accent); color: #fff;
  display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: .85rem; flex-shrink: 0; z-index:1; }
.vflow .sc h3 { margin: .25rem 0 .2rem; font-size: 1rem; }
.vflow .sc p { margin: .15rem 0; font-size: .92rem; color: var(--muted); }
.vflow .sc .mono { font-size: .8rem; color: var(--accent-ink); }

/* layered architecture */
.layers { margin: 1.3rem 0; display: flex; flex-direction: column; gap: .55rem; }
.layer { border-radius: 12px; padding: .85rem 1.1rem; border: 1px solid var(--line); background: var(--panel);
  box-shadow: var(--shadow); }
.layer .lh { display: flex; align-items: center; gap: .6rem; }
.layer .lh .badge { font-size: .7rem; font-weight: 700; padding: .12rem .5rem; border-radius: 999px; }
.layer .lh .name { font-weight: 700; font-family: ui-monospace, monospace; }
.layer .ld { font-size: .85rem; color: var(--muted); margin-top: .35rem; }
.layer.l-core { border-left: 4px solid var(--accent); } .layer.l-core .badge { background: var(--accent-soft); color: var(--accent-ink); }
.layer.l-main { border-left: 4px solid var(--blue); } .layer.l-main .badge { background: var(--blue-soft); color: var(--blue); }
.layer.l-part { border-left: 4px solid var(--purple); } .layer.l-part .badge { background: var(--purple-soft); color: var(--purple); }
.layer.l-app { border-left: 4px solid var(--amber); } .layer.l-app .badge { background: var(--amber-soft); color: var(--amber); }

/* two-column compare */
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.2rem 0; }
@media (max-width: 640px) { .cols { grid-template-columns: 1fr; } }
.col { background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 1rem 1.1rem; box-shadow: var(--shadow); min-width: 0; }
.col h3 { margin: 0 0 .4rem; font-size: .95rem; }

table.t { width: 100%; border-collapse: collapse; margin: 1.1rem 0; font-size: .9rem;
  background: var(--panel); border-radius: 12px; overflow: hidden; box-shadow: var(--shadow); }
table.t th, table.t td { padding: .6rem .8rem; text-align: left; border-bottom: 1px solid var(--line); }
table.t th { background: var(--panel-2); font-size: .8rem; letter-spacing: .02em; }
table.t tr:last-child td { border-bottom: none; }
table.t td.mono, table.t td .mono { font-family: ui-monospace, monospace; font-size: .82rem; color: var(--accent-ink); }
@media (max-width: 640px) {
  /* Wide multi-column tables: scroll within their own box instead of
     forcing page-level horizontal overflow (which clipped right columns). */
  table.t { display: block; overflow-x: auto; -webkit-overflow-scrolling: touch; }
  table.t th, table.t td { padding: .5rem .6rem; }
}
.selftest { margin: 2.2rem 0 0; border-top: 2px dashed var(--line); padding-top: 1.2rem; }
.selftest > h2 { margin-top: .2rem; }
.quiz { background: var(--panel); border: 1px solid var(--line); border-left: 4px solid var(--blue);
  border-radius: 12px; padding: .9rem 1.1rem; margin: 1rem 0; box-shadow: var(--shadow); }
.quiz .qn { font-weight: 650; }
.quiz ol.opts { list-style: upper-alpha; margin: .55rem 0 .6rem 1.5rem; padding: 0; }
.quiz ol.opts li { margin: .3rem 0; padding-left: .15rem; }
.quiz details.accordion { margin: .5rem 0 0; }
.selftest code { font-family: ui-monospace, monospace; font-size: .9em; color: var(--accent-ink);
  background: var(--accent-soft); padding: 0 .28em; border-radius: 4px; }

/* footer nav */
.footnav { display: flex; justify-content: space-between; gap: 1rem; margin-top: 3rem;
  padding-top: 1.4rem; border-top: 1px solid var(--line); }
.footnav a { flex: 1; padding: .85rem 1.1rem; border-radius: 12px; border: 1px solid var(--line);
  background: var(--panel); box-shadow: var(--shadow); transition: .15s; }
.footnav a:hover { border-color: var(--accent); transform: translateY(-1px); }
.footnav a.next { text-align: right; }
.footnav .dir { font-size: .72rem; color: var(--faint); text-transform: uppercase; letter-spacing: .05em; }
.footnav .ttl { font-weight: 700; color: var(--ink); margin-top: .15rem; }
.footnav a.disabled { opacity: .35; pointer-events: none; }

/* index page */
.toc { display: grid; gap: .7rem; margin-top: 1.6rem; }
.toc-part { font-size: .78rem; font-weight: 700; letter-spacing: .05em; text-transform: uppercase;
  color: var(--accent); margin: 1.4rem 0 .2rem; }
.toc a { display: flex; align-items: center; gap: .9rem; padding: .85rem 1.05rem; border-radius: 12px;
  background: var(--panel); border: 1px solid var(--line); box-shadow: var(--shadow); transition: .15s; }
.toc a:hover { border-color: var(--accent); transform: translateX(3px); }
.toc .n { width: 30px; height: 30px; border-radius: 8px; background: var(--accent-soft); color: var(--accent-ink);
  display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: .85rem; flex-shrink: 0; }
.toc .tt { font-weight: 650; color: var(--ink); }
.toc .ts { font-size: .8rem; color: var(--muted); margin-left: auto; text-align: right; }
.toc-search { position: relative; margin: 1.6rem 0 -.4rem; }
.toc-search input { width: 100%; box-sizing: border-box; padding: .75rem 2.8rem .75rem 1rem;
  border-radius: 12px; border: 1px solid var(--line); background: var(--panel); color: var(--ink);
  font-size: .98rem; box-shadow: var(--shadow); }
.toc-search input:focus { outline: none; border-color: var(--accent); }
.toc-search .qcount { position: absolute; right: 1rem; top: 50%; transform: translateY(-50%);
  color: var(--faint); font-size: .8rem; pointer-events: none; }
.toc a.hide, .toc .toc-part.hide { display: none; }
.toc-empty { display: none; color: var(--muted); padding: 1rem; text-align: center; }
.toc-empty.show { display: block; }
.hero.index h1 { font-size: 2.3rem; }
.legend { display:flex; gap:1.2rem; flex-wrap:wrap; margin-top:1rem; font-size:.8rem; color:var(--muted); }
.legend span { display:flex; align-items:center; gap:.4rem; }
.legend i { width:12px; height:12px; border-radius:3px; display:inline-block; }
.pdf-row { display:flex; gap:.6rem; flex-wrap:wrap; margin-top:1.1rem; }
.pdf-btn { display:inline-flex; align-items:center; gap:.4rem; padding:.55rem 1.1rem;
  background:var(--accent); color:#fff; border-radius:10px; font-size:.9rem; font-weight:650;
  box-shadow:var(--shadow); transition:.15s; }
.pdf-btn:hover { background:var(--accent-ink); transform:translateY(-1px); }
"""

SEARCH_JS = """
(function(){
  var q=document.getElementById('q'); if(!q) return;
  var toc=document.querySelector('.toc');
  var empty=document.getElementById('tocempty');
  var count=document.getElementById('qcount');
  var links=[].slice.call(toc.querySelectorAll('a'));
  var heads=[].slice.call(toc.querySelectorAll('.toc-part'));
  links.forEach(function(a){ a.setAttribute('data-s',(a.textContent||'').toLowerCase()); });
  function run(){
    var t=(q.value||'').toLowerCase().trim(), n=0;
    links.forEach(function(a){
      var hit=!t||a.getAttribute('data-s').indexOf(t)>=0;
      a.classList.toggle('hide',!hit); if(hit)n++;
    });
    heads.forEach(function(h){
      var el=h.nextElementSibling, any=false;
      while(el && !el.classList.contains('toc-part')){
        if(el.tagName==='A' && !el.classList.contains('hide')){any=true;break;}
        el=el.nextElementSibling;
      }
      h.classList.toggle('hide',!any);
    });
    empty.classList.toggle('show', !!t && n===0);
    count.textContent = t ? String(n) : '';
  }
  q.addEventListener('input',run);
})();
"""

# Language toggle: flip html class, persist, and keep the button showing the
# OTHER language (so it reads "EN" while zh, "中" while en).
LANG_JS = """
(function(){
  function cur(){ return (localStorage.getItem('galang')||'zh'); }
  function apply(){
    var l=cur();
    document.documentElement.className='lang-'+l;
    document.documentElement.lang=(l==='zh')?'zh-CN':'en';
    var btn=document.getElementById('langbtn'); if(btn) btn.textContent=(l==='zh')?'EN':'\u4e2d';
    var q=document.getElementById('q');
    if(q){ var p=q.getAttribute(l==='zh'?'data-ph-zh':'data-ph-en'); if(p) q.placeholder=p; }
  }
  apply();
  var btn=document.getElementById('langbtn');
  if(btn) btn.addEventListener('click',function(){
    localStorage.setItem('galang', cur()==='zh'?'en':'zh');
    apply();
  });
})();
"""


def _lang_button():
    return '<button class="lang-btn" id="langbtn" type="button" aria-label="切换语言 / Toggle language">EN</button>'


def page(fname, content, home_href="../index.html"):
    """Wrap already-bilingual lesson ``content`` in the full HTML shell.

    ``home_href`` is the link back to the index (defaults to ``"../index.html"``
    because lesson pages live in a ``lessons/`` subdirectory). Sibling lesson
    links always use bare filenames, so lessons must share one directory. All
    navigation uses plain relative ``href`` links (no ``data-nav``).
    """
    try:
        idx = next(i for i, p in enumerate(PAGES) if p.fname == fname)
    except StopIteration:
        raise KeyError(f"{fname!r} not in PAGES") from None
    p = PAGES[idx]
    total = len(PAGES)
    pct = round((idx + 1) / total * 100)
    num = f"{idx + 1:02d}"

    title_bi = bi(p.title_zh, p.title_en)
    part_bi = bi(p.part_zh, p.part_en)

    if idx > 0:
        prev = PAGES[idx - 1]
        prev_link = (
            f'<a class="prev" href="{prev.fname}">'
            f'<div class="dir">{bi("← 上一课", "← Prev")}</div>'
            f'<div class="ttl">{bi(prev.title_zh, prev.title_en)}</div></a>'
        )
    else:
        prev_link = (
            f'<a class="prev" href="{home_href}">'
            f'<div class="dir">{bi("← 返回", "← Back")}</div>'
            f'<div class="ttl">{bi("目录", "Contents")}</div></a>'
        )

    if idx + 1 < total:
        nxt = PAGES[idx + 1]
        next_link = (
            f'<a class="next" href="{nxt.fname}">'
            f'<div class="dir">{bi("下一课 →", "Next →")}</div>'
            f'<div class="ttl">{bi(nxt.title_zh, nxt.title_en)}</div></a>'
        )
    else:
        next_link = (
            f'<a class="next" href="{home_href}">'
            f'<div class="dir">{bi("完成 →", "Done →")}</div>'
            f'<div class="ttl">{bi("返回目录", "Back to contents")}</div></a>'
        )

    page_title = f"{num} · {p.title_zh} / {p.title_en} — GenericAgent 图解教程"
    meta = head_meta(
        page_title,
        f"{p.part_zh}｜{p.title_zh}：面向新手的 GenericAgent 图解教程，配真实源码对应与设计亮点。",
        og_type="article",
    )

    return f"""<!DOCTYPE html>
<html class="lang-zh" lang="zh-CN"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>{FOUC_SCRIPT}</script>
<title>{_esc(page_title)}</title>
{meta}
<style>{CSS}</style>
</head><body>
<header class="topbar">
  <div class="topbar-inner">
    <a class="home" href="{home_href}">📘 {SITE_NAME} · <b>{bi("目录", "Contents")}</b></a>
    <span class="pill">{part_bi}</span>
    <span class="pill">{num} / {total:02d}</span>
    <span class="spacer"></span>
    {_lang_button()}
  </div>
  <div class="progress"><span style="width:{pct}%"></span></div>
</header>
<main class="wrap">
  <div class="hero">
    <div class="part">{part_bi}</div>
    <h1>{title_bi}</h1>
  </div>
  {content}
  <nav class="footnav" aria-label="课程导航 / Lesson navigation">{prev_link}{next_link}</nav>
</main>
<script>{LANG_JS}</script>
</body></html>"""


def index_page(lesson_prefix="lessons/"):
    """Return the complete bilingual index/TOC HTML document."""
    order = []
    parts = {}
    for i, p in enumerate(PAGES):
        key = (p.part_zh, p.part_en)
        if key not in parts:
            parts[key] = []
            order.append(key)
        parts[key].append((i + 1, p))

    blocks = []
    for key in order:
        part_zh, part_en = key
        blocks.append(f'<div class="toc-part">{bi(part_zh, part_en)}</div>')
        for num, p in parts[key]:
            sub_zh, sub_en = SUBTITLES.get(p.fname, ("", ""))
            blocks.append(
                f'<a href="{lesson_prefix}{p.fname}"><span class="n">{num:02d}</span>'
                f'<span class="tt">{bi(p.title_zh, p.title_en)}</span>'
                f'<span class="ts">{bi(sub_zh, sub_en)}</span></a>'
            )
    toc = "\n".join(blocks)

    page_title = "GenericAgent 图解教程 · GenericAgent Visual Guide"
    meta = head_meta(
        page_title,
        "从零理解整个 GenericAgent 项目的双语图解教程：宏观全景、用户视角、内部源码、进阶能力、实战与速查。",
        og_type="website",
    )

    lead = bi(
        "这套教程带你<strong>层层深入</strong> GenericAgent：先建立<strong>宏观全景</strong>，"
        "再从<strong>用户视角</strong>上手，然后深入<strong>内部源码</strong>，"
        "接着掌握<strong>进阶能力</strong>，最后用<strong>实战</strong>把所有零件拼起来。每一课都配真实源码对应。",
        "This guide takes you <strong>layer by layer</strong> through GenericAgent: first the "
        "<strong>big picture</strong>, then <strong>using it</strong>, then deep into the "
        "<strong>source</strong>, then its <strong>advanced capabilities</strong>, and finally "
        "<strong>hands-on</strong> projects that wire it all together. Every lesson maps to real source.",
    )
    anchor = bi(
        '📌 对照 GenericAgent <strong><span class="mono">main</span></strong> 源码讲解 · '
        '引用以「文件 + 符号名」为主（行号会随上游更新而变）',
        '📌 Based on the GenericAgent <strong><span class="mono">main</span></strong> source · '
        "references cite file + symbol name (line numbers drift with upstream)",
    )

    return f"""<!DOCTYPE html>
<html class="lang-zh" lang="zh-CN"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>{FOUC_SCRIPT}</script>
<title>{_esc(page_title)}</title>
{meta}
<style>{CSS}</style>
</head><body>
<header class="topbar">
  <div class="topbar-inner">
    <span class="home">📘 {SITE_NAME}</span>
    <span class="pill">{bi(f"共 {len(PAGES)} 课 · {len(order)} 个部分", f"{len(PAGES)} lessons · {len(order)} parts")}</span>
    <span class="spacer"></span>
    {_lang_button()}
  </div>
  <div class="progress"><span style="width:100%"></span></div>
</header>
<main class="wrap">
  <div class="hero index">
    <div class="part">{bi("从零开始 · 面向完全新手", "From scratch · for total beginners")}</div>
    <h1>{bi("用图解理解整个 GenericAgent", "Understand all of GenericAgent, visually")}</h1>
    <p class="lead">{lead}</p>
    <div class="legend">
      <span><i style="background:var(--blue)"></i>{bi("宏观", "Macro")}</span>
      <span><i style="background:var(--purple)"></i>{bi("源码", "Source")}</span>
      <span><i style="background:var(--amber)"></i>{bi("类比", "Analogy")}</span>
      <span><i style="background:var(--accent)"></i>{bi("要点", "Key points")}</span>
    </div>
    <p style="margin:.9rem 0 0;color:var(--faint);font-size:.8rem">{anchor}</p>
    <div class="pdf-row">
      <span class="zh"><a class="pdf-btn" href="generic-agent-visual-guide-zh.pdf">📄 下载 PDF（中文）</a></span>
      <span class="en"><a class="pdf-btn" href="generic-agent-visual-guide-en.pdf">📄 Download PDF (English)</a></span>
    </div>
  </div>
  <div class="toc-search">
    <input id="q" type="search" data-ph-zh="🔎 搜索课程：标题 / 关键词" data-ph-en="🔎 Search lessons: title / keyword" placeholder="🔎 搜索课程：标题 / 关键词" autocomplete="off" aria-label="搜索课程 / Search lessons">
    <span class="qcount" id="qcount"></span>
  </div>
  <nav class="toc" aria-label="课程目录 / Lesson contents">{toc}</nav>
  <div class="toc-empty" id="tocempty">{bi("没有匹配的课程，换个关键词试试。", "No matching lessons — try another keyword.")}</div>
</main>
<script>{LANG_JS}</script>
<script>{SEARCH_JS}</script>
</body></html>"""
