"""Part 1 — 宏观全景 / The Big Picture (lessons 01–03).

Each lesson is a ``lesson(t)`` function. ``t('中文', 'English')`` wraps every
piece of prose; structure, diagrams and code are written once and shared by
both language renders. All technical claims are grounded in the real
GenericAgent source (README.md, agent_loop.py, llmcore.py, agentmain.py, ga.py).

Authoring conventions (follow these when adding/editing lessons)
----------------------------------------------------------------
5-card lesson format — every completed lesson opens with a ``<p class="lead">``
intro paragraph, then presents these five cards in order (the structural test
``test_completed_lessons_follow_card_format`` enforces their presence):

    1. ``card macro``   🌍 The Big Picture — high-level framing.
    2. ``card detail``  🔬 In the Source   — concrete source-code grounding.
    3. ``card analogy`` 🧩 Analogy         — an everyday-life analogy.
    4. ``card key``     ✅ Key Takeaways   — bullet summary.
    5. ``card spark``   💡 Design Insight  — the "aha" design point.

``.inline`` vs ``.mono`` — pick by CONTEXT, not by content:

    * ``.inline`` (pill with a background) → for inline code / identifiers that
      appear in PROSE: file names, symbols, commands. Example:
      ``<span class="inline">agent_loop.py: agent_runner_loop</span>``.
    * ``.mono`` (monospace, no pill) → ONLY inside dense components where a pill
      would be too heavy: ``table.t`` cells, ``.flow``/``.vflow`` node text, and
      ``.layer .name``.

Any visible words must stay wrapped in ``t('zh','en')``; pure numerals/symbols
(e.g. badge text ``①②③④``) need no translation.
"""


def lesson_01(t):
    """GenericAgent 是什么 / What is GenericAgent — flagship overview."""
    return (
        '<p class="lead">'
        + t(
            'GenericAgent 是一个<strong>极简、可自我进化</strong>的自主 Agent 框架：核心只有约 '
            '3000 行“种子代码”，却能赋予任意大模型对本地电脑的系统级控制能力——浏览器、终端、'
            '文件、键鼠、屏幕视觉，乃至手机（ADB）。',
            'GenericAgent is a <strong>minimal, self-evolving</strong> autonomous agent '
            'framework. Its core is only about 3,000 lines of "seed code", yet it gives any '
            'LLM system-level control over a local computer — browser, terminal, files, '
            'keyboard/mouse, screen vision, even phones (ADB).',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '大多数“强大”的 Agent 走的是<strong>做加法</strong>的路：预置成百上千个工具、几十万行代码、'
            '动辄 200K–1M 的上下文窗口。GenericAgent 反其道而行，做<strong>减法</strong>。它的设计哲学是一句话——'
            '<strong>“不预设技能，靠进化获得能力。”</strong>',
            'Most "powerful" agents grow by <strong>addition</strong>: hundreds of preloaded '
            'tools, hundreds of thousands of lines of code, and 200K–1M token context windows. '
            'GenericAgent goes the other way — it <strong>subtracts</strong>. Its design '
            'philosophy is a single sentence: <strong>"Don\'t preload skills, evolve them."</strong>',
        )
        + '</p><p>'
        + t(
            '它不试图在出厂时就会一切。每解决一个新任务，它就把这次的执行路径<strong>固化（crystallize）</strong>'
            '成一个可复用的 Skill 写进记忆。用得越久，技能越多，最终长成一棵<strong>只属于你</strong>的技能树。',
            'It does not try to know everything out of the box. Each time it solves a new task, '
            'it <strong>crystallizes</strong> that execution path into a reusable Skill written '
            'into memory. The longer you use it, the more skills accumulate — growing a skill '
            'tree that is <strong>uniquely yours</strong>.',
        )
        + '</p></div>'

        + '<h2>' + t('五根支柱', 'The Five Pillars') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('支柱', 'Pillar') + '</th><th>' + t('含义', 'What it means') + '</th></tr>'
        + '<tr><td>' + t('极简种子', 'Minimal seed')
        + '</td><td>' + t('核心约 3K 行代码，没有复杂依赖，零部署负担。',
                          'About 3K lines of core code, no heavy dependencies, zero deployment overhead.') + '</td></tr>'
        + '<tr><td>' + t('9 个原子工具', '9 atomic tools')
        + '</td><td>' + t('code_run、file_read/write/patch、web_scan、web_execute_js、ask_user 等，组合即可覆盖一切操作。',
                          'code_run, file_read/write/patch, web_scan, web_execute_js, ask_user … combine them to cover any action.') + '</td></tr>'
        + '<tr><td>' + t('~100 行 Agent Loop', '~100-line Agent Loop')
        + '</td><td>' + t('整个自主执行循环就在 agent_loop.py 里，短到能一次读完。',
                          'The entire autonomous loop lives in agent_loop.py — short enough to read in one sitting.') + '</td></tr>'
        + '<tr><td>' + t('自进化技能树', 'Self-evolving skill tree')
        + '</td><td>' + t('把成功经验固化为 Skill，下次同类任务一行直达。',
                          'Crystallizes successful runs into Skills; next similar task is a one-line invoke.') + '</td></tr>'
        + '<tr><td>' + t('分层记忆 + 省 token', 'Layered memory + token-thrifty')
        + '</td><td>' + t('L0–L4 分层记忆，上下文常年保持在 30K 以内。',
                          'L0–L4 layered memory keeps the working context under ~30K tokens.') + '</td></tr>'
        + '</table>'

        + '<h2>' + t('一颗种子如何生长', 'How a seed grows') + '</h2>'
        + '<div class="flow">'
        + '<div class="node"><div class="nt">' + t('种子代码', 'Seed code') + '</div>'
        + '<div class="nd">' + t('~3K 行', '~3K lines') + '</div></div>'
        + '<div class="arrow">→</div>'
        + '<div class="node"><div class="nt">' + t('9 原子工具', '9 atomic tools') + '</div>'
        + '<div class="nd">' + t('与世界交互', 'touch the world') + '</div></div>'
        + '<div class="arrow">→</div>'
        + '<div class="node hl"><div class="nt">' + t('Agent Loop', 'Agent Loop') + '</div>'
        + '<div class="nd">' + t('感知·推理·执行', 'sense · reason · act') + '</div></div>'
        + '<div class="arrow">→</div>'
        + '<div class="node"><div class="nt">' + t('技能树', 'Skill tree') + '</div>'
        + '<div class="nd">' + t('越用越强', 'grows with use') + '</div></div>'
        + '</div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<p>'
        + t(
            '这些都不是宣传话术，全部能在仓库里指认到具体位置：',
            'None of this is marketing — every claim maps to a concrete place in the repo:',
        )
        + '</p><ul>'
        + '<li>' + t('哲学与全景：', 'Philosophy & overview: ')
        + '<span class="inline">README.md</span>'
        + t('（“don\'t preload skills, evolve them”、对比表、自进化机制）。',
            ' ("don\'t preload skills, evolve them", the comparison table, the self-evolution section).') + '</li>'
        + '<li>' + t('约 100 行的循环：', 'The ~100-line loop: ')
        + '<span class="inline">agent_loop.py: agent_runner_loop</span>'
        + t('，搭配 ', ', alongside ')
        + '<span class="inline">BaseHandler.dispatch</span>' + t(' 与 ', ' and ')
        + '<span class="inline">StepOutcome</span>' + t('。', '.') + '</li>'
        + '<li>' + t('9 个原子工具的实现：', 'The 9 atomic tools live as ')
        + '<span class="inline">do_&lt;tool&gt;</span>'
        + t(' 方法，集中在 ', ' methods in ')
        + '<span class="inline">ga.py: GenericAgentHandler</span>'
        + t('（如 ', ' (e.g. ')
        + '<span class="inline">do_code_run</span>, <span class="inline">do_file_read</span>, '
        + '<span class="inline">do_ask_user</span>' + t('）。', ').') + '</li>'
        + '<li>' + t('LLM 内核：', 'The LLM core: ')
        + '<span class="inline">llmcore.py</span>'
        + t('，提供 ', ' provides the ')
        + '<span class="inline">chat(messages, tools)</span>'
        + t(' 客户端与工具调用解析。', ' client and tool-call parsing.') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + '<p>'
        + t(
            '重型 Agent 像一套<strong>全功能瑞士军刀工具箱</strong>：出厂自带几百件工具，沉、贵，但你 99% 用不上。'
            'GenericAgent 更像一个<strong>聪明的新员工</strong>：只带一双手和基本常识来上班，'
            '第一次做某件事会慢慢摸索，但一旦学会就写进自己的笔记本，下次信手拈来——而且这本笔记只属于他。',
            'A heavyweight agent is like a <strong>fully loaded Swiss-army toolbox</strong>: '
            'hundreds of tools out of the box — heavy, costly, and 99% unused. GenericAgent is '
            'more like a <strong>sharp new hire</strong>: it shows up with just two hands and '
            'common sense. The first time it does something it figures it out slowly, but once '
            'learned it writes the recipe in its own notebook — instant next time, and that '
            'notebook is uniquely its own.',
        )
        + '</p></div>'

        + '<h2>' + t('和重型 Agent 的区别', 'How it differs from heavyweight agents') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('维度', 'Dimension') + '</th><th>GenericAgent</th><th>'
        + t('多数重型 Agent', 'Typical heavyweight') + '</th></tr>'
        + '<tr><td>' + t('代码量', 'Codebase') + '</td><td>' + t('~3K 行', '~3K lines')
        + '</td><td>' + t('几十万行', 'hundreds of thousands of lines') + '</td></tr>'
        + '<tr><td>' + t('上下文', 'Context') + '</td><td>' + t('&lt;30K，更省、更准', '&lt;30K — cheaper, less noise')
        + '</td><td>' + t('200K–1M', '200K–1M') + '</td></tr>'
        + '<tr><td>' + t('能力来源', 'Where capability comes from') + '</td><td>'
        + t('运行中自我进化', 'self-evolves at runtime')
        + '</td><td>' + t('出厂预置', 'preloaded at build time') + '</td></tr>'
        + '<tr><td>' + t('跨会话', 'Across sessions') + '</td><td>'
        + t('记忆沉淀，越用越强', 'memory accrues, grows with use')
        + '</td><td>' + t('常常无状态', 'often stateless') + '</td></tr>'
        + '</table>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('GenericAgent = 极简种子 + 9 原子工具 + ~100 行循环 + 自进化记忆。',
                    'GenericAgent = minimal seed + 9 atomic tools + ~100-line loop + self-evolving memory.') + '</li>'
        + '<li>' + t('核心哲学：不预设技能，靠进化获得能力。',
                    'Core philosophy: don\'t preload skills, evolve them.') + '</li>'
        + '<li>' + t('上下文常年 <30K，比动辄百万 token 的方案更省、更准。',
                    'It keeps context under ~30K tokens — cheaper and less error-prone than million-token designs.') + '</li>'
        + '<li>' + t('“少即是多”不是口号，而是可在源码中逐条验证的工程选择。',
                    '"Less is more" is not a slogan here — it is an engineering choice you can verify line by line in the source.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + '<p>'
        + t(
            '最反直觉的一点：<strong>更小的上下文反而带来更高的成功率</strong>。塞进去的无关信息越少，模型被噪声'
            '带偏、产生幻觉的概率就越低。GenericAgent 用分层记忆只把<strong>当下最相关</strong>的内容喂给模型，'
            '于是“省 token”和“更可靠”这两件事在它身上是同一件事。',
            'The most counter-intuitive point: <strong>a smaller context yields a higher success '
            'rate</strong>. The less irrelevant information you stuff in, the less the model is '
            'dragged off course or hallucinates. By using layered memory to feed the model only '
            'what is <strong>most relevant right now</strong>, GenericAgent makes "token-thrifty" '
            'and "more reliable" the very same thing.',
        )
        + '</p></div>'
    )


def lesson_02(t):
    """项目全景地图 / Project Map."""
    return (
        '<p class="lead">'
        + t(
            '在动手读任何一行代码之前，先建立一张<strong>地图</strong>：仓库里每个文件、每个目录各负责什么。'
            '记住一句话——这整个项目就是一颗约 3000 行的<strong>种子</strong>，其余能力都是它生长出来的。',
            'Before reading a single line, build a <strong>map</strong>: what each file and '
            'directory in the repo is responsible for. Keep one idea in mind — the whole project '
            'is a roughly 3,000-line <strong>seed</strong>, and everything else grows from it.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            'GenericAgent 的代码可以按“离大模型有多近”分成几圈：最内圈是<strong>循环与内核</strong>'
            '（agent_loop.py、llmcore.py），向外是<strong>装配与工具</strong>（agentmain.py、ga.py），'
            '再外是<strong>记忆与反思</strong>（memory/、reflect/），最外圈是<strong>给人用的外壳</strong>'
            '（frontends/、ga_cli/）。读代码时知道自己站在哪一圈，就不会迷路。',
            'GenericAgent\'s code can be read as rings around the LLM. The innermost ring is the '
            '<strong>loop and core</strong> (agent_loop.py, llmcore.py); around it sits '
            '<strong>assembly and tools</strong> (agentmain.py, ga.py); then <strong>memory and '
            'reflection</strong> (memory/, reflect/); and the outermost ring is the '
            '<strong>human-facing shell</strong> (frontends/, ga_cli/). Knowing which ring you '
            'stand in keeps you from getting lost.',
        )
        + '</p></div>'

        + '<h2>' + t('四层结构', 'Four layers') + '</h2>'
        + '<div class="layers">'
        + '<div class="layer l-core"><div class="lh"><span class="badge">①</span>'
        + '<span class="name">agent_loop.py · llmcore.py</span></div>'
        + '<div class="ld">' + t(
            '最内核。agent_loop.py 是约 100 行的自主循环；llmcore.py 是 LLM 客户端，负责 chat、'
            '流式输出与工具调用解析。',
            'The innermost core. agent_loop.py is the ~100-line autonomous loop; llmcore.py is the '
            'LLM client handling chat, streaming, and tool-call parsing.') + '</div></div>'
        + '<div class="layer l-main"><div class="lh"><span class="badge">②</span>'
        + '<span class="name">agentmain.py · ga.py</span></div>'
        + '<div class="ld">' + t(
            '装配层。agentmain.py 把系统提示词、工具 schema、会话与 handler 接到循环上；'
            'ga.py 的 GenericAgentHandler 实现 9 个原子工具的 do_&lt;tool&gt; 方法。',
            'The assembly layer. agentmain.py wires the system prompt, tools schema, session and '
            'handler into the loop; ga.py\'s GenericAgentHandler implements the 9 atomic tools as '
            'do_&lt;tool&gt; methods.') + '</div></div>'
        + '<div class="layer l-part"><div class="lh"><span class="badge">③</span>'
        + '<span class="name">memory/ · reflect/ · plugins/</span></div>'
        + '<div class="ld">' + t(
            '经验层。memory/ 存放分层记忆与各类 SOP（.md 流程文档）；reflect/ 负责编排（如 goal_mode、'
            'scheduler）；plugins/ 通过 hooks 在循环关键点插桩观测。',
            'The experience layer. memory/ holds layered memory and SOPs (.md procedure docs); '
            'reflect/ handles orchestration (e.g. goal_mode, scheduler); plugins/ instruments the '
            'loop at key points via hooks.') + '</div></div>'
        + '<div class="layer l-app"><div class="lh"><span class="badge">④</span>'
        + '<span class="name">frontends/ · ga_cli/ · simphtml.py</span></div>'
        + '<div class="ld">' + t(
            '外壳层。frontends/ 提供桌面端、TUI、各类 IM 机器人；ga_cli/ 是命令行入口；'
            'simphtml.py 是网页 HTML 简化 / token 优化工具——把网页 DOM 压缩成精简内容，'
            '供 web_scan/web_execute_js 工具低成本阅读（被 ga.py 调用）。',
            'The shell layer. frontends/ provides the desktop app, TUI and IM bots; ga_cli/ is the '
            'command-line entry; simphtml.py is a web HTML simplifier / token optimizer that shrinks '
            'a page\'s DOM into compact content so the web_scan/web_execute_js tools can read pages '
            'cheaply (used by ga.py).') + '</div></div>'
        + '</div>'

        + '<h2>' + t('核心文件速查表', 'Core file cheat-sheet') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('文件 / 目录', 'File / Dir') + '</th><th>' + t('职责', 'Responsibility') + '</th></tr>'
        + '<tr><td class="mono">agent_loop.py</td><td>'
        + t('约 100 行的自主执行循环：agent_runner_loop、BaseHandler、StepOutcome。',
            'The ~100-line autonomous loop: agent_runner_loop, BaseHandler, StepOutcome.') + '</td></tr>'
        + '<tr><td class="mono">llmcore.py</td><td>'
        + t('LLM 内核：chat(messages, tools)、流式输出、把模型回复解析成 tool_calls。',
            'The LLM core: chat(messages, tools), streaming, and parsing model replies into tool_calls.') + '</td></tr>'
        + '<tr><td class="mono">agentmain.py</td><td>'
        + t('装配与接线：加载工具 schema、system prompt，调用 agent_runner_loop。',
            'Assembly & wiring: loads the tools schema and system prompt, calls agent_runner_loop.') + '</td></tr>'
        + '<tr><td class="mono">ga.py</td><td>'
        + t('GenericAgentHandler：9 个原子工具的具体实现（do_code_run、do_file_read…）。',
            'GenericAgentHandler: the concrete 9 atomic tools (do_code_run, do_file_read …).') + '</td></tr>'
        + '<tr><td class="mono">simphtml.py</td><td>'
        + t('网页 HTML 简化 / token 优化：把网页 DOM 压缩成精简内容，供 web_scan/web_execute_js 工具低成本阅读（被 ga.py 调用）。',
            'Web HTML simplifier / token optimizer: shrinks a page\'s DOM into compact content so the web_scan/web_execute_js tools can read pages cheaply (used by ga.py).') + '</td></tr>'
        + '<tr><td class="mono">memory/</td><td>'
        + t('分层记忆 L0–L4 与可复用 SOP（如 plan_sop.md、verify_sop.md）。',
            'Layered memory L0–L4 and reusable SOPs (e.g. plan_sop.md, verify_sop.md).') + '</td></tr>'
        + '<tr><td class="mono">reflect/</td><td>'
        + t('编排与自驱：goal_mode.py、scheduler.py、agent_team_worker.py 等。',
            'Orchestration & self-drive: goal_mode.py, scheduler.py, agent_team_worker.py, etc.') + '</td></tr>'
        + '<tr><td class="mono">plugins/</td><td>'
        + t('钩子与观测：hooks.py、langfuse_tracing.py。',
            'Hooks & observability: hooks.py, langfuse_tracing.py.') + '</td></tr>'
        + '<tr><td class="mono">frontends/</td><td>'
        + t('各种界面：桌面端、TUI（tuiapp_v2.py / tui_v3.py）、Telegram/微信等 IM。',
            'User interfaces: desktop app, TUI (tuiapp_v2.py / tui_v3.py), and IM bots (Telegram/WeChat…).') + '</td></tr>'
        + '<tr><td class="mono">ga_cli/</td><td>'
        + t('命令行入口：cli.py、__main__.py。',
            'The command-line entry: cli.py, __main__.py.') + '</td></tr>'
        + '</table>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<p>'
        + t('几条能帮你立刻上手的指认：', 'A few pointers to get you oriented immediately:')
        + '</p><ul>'
        + '<li>' + t('循环的心脏在 ', 'The heart of the loop is ')
        + '<span class="inline">agent_loop.py: agent_runner_loop</span>'
        + t('；它接收 client、system_prompt、handler、tools_schema 等参数。',
            '; it takes client, system_prompt, handler, tools_schema and more.') + '</li>'
        + '<li>' + t('接线发生在 ', 'Wiring happens in ')
        + '<span class="inline">agentmain.py</span>'
        + t('，从 assets/tools_schema*.json 读入工具描述，再 ',
            ', which loads the tool descriptions from assets/tools_schema*.json and then calls ')
        + '<span class="inline">agent_runner_loop(...)</span>' + t('。', '.') + '</li>'
        + '<li>' + t('工具实现都是 ', 'The tools are all ')
        + '<span class="inline">do_&lt;tool&gt;</span>'
        + t(' 方法，集中在 ', ' methods, gathered in ')
        + '<span class="inline">ga.py: GenericAgentHandler</span>'
        + t('，继承自 ', ', subclassing ')
        + '<span class="inline">agent_loop.py: BaseHandler</span>' + t('。', '.') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + '<p>'
        + t(
            '把项目想成一家小餐馆：<span class="inline">agent_loop.py</span> 是后厨的<strong>出餐节奏</strong>，'
            '一道接一道；<span class="inline">llmcore.py</span> 是会做菜的<strong>大厨</strong>；'
            '<span class="inline">ga.py</span> 里的工具是<strong>锅碗刀具</strong>；'
            '<span class="inline">memory/</span> 是大厨积累的<strong>菜谱本</strong>；'
            '而 <span class="inline">frontends/</span> 是<strong>前台与菜单</strong>，顾客只跟它打交道。',
            'Picture a small restaurant: <span class="inline">agent_loop.py</span> is the kitchen\'s '
            '<strong>service rhythm</strong>, plating one dish after another; '
            '<span class="inline">llmcore.py</span> is the <strong>chef</strong> who actually cooks; '
            'the tools in <span class="inline">ga.py</span> are the <strong>pots and knives</strong>; '
            '<span class="inline">memory/</span> is the chef\'s growing <strong>recipe book</strong>; '
            'and <span class="inline">frontends/</span> is the <strong>front desk and menu</strong> '
            'that customers actually talk to.',
        )
        + '</p></div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('整个项目是一颗 ~3K 行的种子；其余能力都是运行中长出来的。',
                    'The whole project is a ~3K-line seed; the rest grows at runtime.') + '</li>'
        + '<li>' + t('按“离大模型多近”分四层：内核 → 装配 → 经验 → 外壳。',
                    'Read it as four rings by distance from the LLM: core → assembly → experience → shell.') + '</li>'
        + '<li>' + t('agent_loop.py 是循环，llmcore.py 是大脑，ga.py 是双手，memory/ 是记忆。',
                    'agent_loop.py is the loop, llmcore.py the brain, ga.py the hands, memory/ the memory.') + '</li>'
        + '<li>' + t('迷路时，先问自己：我现在在哪一层？',
                    'When lost, first ask: which ring am I in right now?') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + '<p>'
        + t(
            '注意 <span class="inline">memory/</span> 里有大量 <strong>.md 文件</strong>（SOP），而不是写死的代码。'
            '这是刻意的：流程用自然语言沉淀，模型可读、可改、可自我扩充，于是“加一个新技能”往往等于“多写一份 .md”，'
            '而不是改框架。<strong>把能力放进记忆，而不是放进代码</strong>，正是它能自我进化的结构性原因。',
            'Notice that <span class="inline">memory/</span> is full of <strong>.md files</strong> '
            '(SOPs) rather than hard-coded logic. This is deliberate: procedures are distilled in '
            'natural language the model can read, edit and extend, so "adding a skill" often means '
            '"writing one more .md", not changing the framework. <strong>Putting capability into '
            'memory rather than into code</strong> is the structural reason it can self-evolve.',
        )
        + '</p></div>'
    )


def lesson_03(t):
    """一次任务的生命周期 / Lifecycle of a Task."""
    return (
        '<p class="lead">'
        + t(
            '从你按下回车的那一刻，到 GenericAgent 说“任务完成”，中间发生了什么？这一课把<strong>一次任务的完整'
            '生命周期</strong>拆开看——它本质上就是一个会循环的对话：问大模型 → 大模型想调哪个工具 → 执行工具 → '
            '把结果喂回去 → 再问，直到收尾。',
            'From the moment you hit enter to the moment GenericAgent says "done", what actually '
            'happens? This lesson opens up the <strong>full lifecycle of one task</strong>. At heart '
            'it is a looping conversation: ask the LLM → the LLM picks a tool → run the tool → feed '
            'the result back → ask again, until it wraps up.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '整个生命周期就是一个 <strong>while 循环</strong>，最多跑 max_turns 轮（默认 40）。每一轮叫一个'
            '<strong>turn</strong>：把当前 messages 发给大模型，拿到回复；如果回复里有工具调用，就执行它们，'
            '把结果拼成下一轮的 messages；如果没有工具要调、或某个工具说“该退出了”，循环就结束。',
            'The whole lifecycle is one <strong>while loop</strong> that runs at most max_turns times '
            '(default 40). Each pass is a <strong>turn</strong>: send the current messages to the LLM '
            'and get a reply; if the reply contains tool calls, run them and assemble their results '
            'into the next turn\'s messages; if there is no tool to call — or a tool says "time to '
            'exit" — the loop ends.',
        )
        + '</p></div>'

        + '<h2>' + t('一次任务，分步走', 'One task, step by step') + '</h2>'
        + '<div class="vflow">'
        + '<div class="step"><div class="num">1</div><div class="sc">'
        + '<h4>' + t('用户输入', 'User input') + '</h4>'
        + '<p>' + t('你的请求作为 user_input 进入循环。',
                   'Your request enters the loop as user_input.') + '</p></div></div>'
        + '<div class="step"><div class="num">2</div><div class="sc">'
        + '<h4>' + t('组装初始 messages', 'Assemble initial messages') + '</h4>'
        + '<p>' + t('循环先拼出 ', 'The loop builds ')
        + '<span class="mono">[{system_prompt}, {user_input}]</span>'
        + t(' 作为对话起点。', ' as the conversation\'s starting point.') + '</p></div></div>'
        + '<div class="step"><div class="num">3</div><div class="sc">'
        + '<h4>' + t('调用大模型', 'Call the LLM') + '</h4>'
        + '<p>'
        + '<span class="mono">client.chat(messages, tools=tools_schema)</span>'
        + t(' 返回一个 response，里面可能带 ', ' returns a response that may carry ')
        + '<span class="mono">response.tool_calls</span>' + t('。', '.') + '</p></div></div>'
        + '<div class="step"><div class="num">4</div><div class="sc">'
        + '<h4>' + t('解析工具调用', 'Parse tool calls') + '</h4>'
        + '<p>' + t('每个 tool_call 解析出 tool_name 和 args；如果模型没调任何工具，记为 no_tool。',
                   'Each tool_call yields a tool_name and args; if the model called nothing, it is recorded as no_tool.') + '</p></div></div>'
        + '<div class="step"><div class="num">5</div><div class="sc">'
        + '<h4>' + t('派发并执行工具', 'Dispatch & run the tool') + '</h4>'
        + '<p>'
        + '<span class="mono">handler.dispatch(tool_name, args, ...)</span>'
        + t(' 找到对应的 ', ' finds the matching ')
        + '<span class="mono">do_&lt;tool&gt;</span>'
        + t(' 方法并运行（如 do_code_run、do_file_read）。',
            ' method and runs it (e.g. do_code_run, do_file_read).') + '</p></div></div>'
        + '<div class="step"><div class="num">6</div><div class="sc">'
        + '<h4>' + t('返回 StepOutcome', 'Return a StepOutcome') + '</h4>'
        + '<p>' + t('每个工具返回 ', 'Each tool returns a ')
        + '<span class="mono">StepOutcome(data, next_prompt, should_exit)</span>'
        + t('：data 是结果，next_prompt 是下一轮要对模型说的话，should_exit 决定是否收尾。',
            ': data is the result, next_prompt is what to tell the model next turn, should_exit decides whether to wrap up.') + '</p></div></div>'
        + '<div class="step"><div class="num">7</div><div class="sc">'
        + '<h4>' + t('结果写回 messages', 'Results flow into messages') + '</h4>'
        + '<p>' + t('工具的 data 收进 tool_results，next_prompt 合成下一轮唯一的新 user 消息；历史由 Session 维护。',
                   'Tool data collects into tool_results; the next_prompts merge into the single new user message; history is kept by the Session.') + '</p></div></div>'
        + '<div class="step"><div class="num">8</div><div class="sc">'
        + '<h4>' + t('循环，直到收尾', 'Loop until done') + '</h4>'
        + '<p>' + t('没有 next_prompt、有工具 should_exit、或达到 max_turns，循环结束并返回 exit_reason。',
                   'When there is no next_prompt, a tool signals should_exit, or max_turns is hit, the loop ends and returns an exit_reason.') + '</p></div></div>'
        + '</div>'

        + '<h2>' + t('循环的骨架', 'The skeleton of the loop') + '</h2>'
        + '<div class="codefile"><div class="cf-head"><span class="dot"></span>'
        + '<span class="path">agent_loop.py</span><span class="ln">agent_runner_loop</span></div>'
        + '<pre>'
        + '<span class="kw">while</span> turn &lt; handler.max_turns:\n'
        + '    turn += <span class="nb">1</span>\n'
        + '    response = <span class="kw">yield from</span> client.<span class="fn">chat</span>('
        + 'messages=messages, tools=tools_schema)\n\n'
        + '    <span class="cm"># ' + t('没调工具就记为 no_tool', 'no tool call -&gt; no_tool') + '</span>\n'
        + '    tool_calls = [{<span class="st">\'tool_name\'</span>: tc.function.name, '
        + '<span class="st">\'args\'</span>: json.<span class="fn">loads</span>(tc.function.arguments)}\n'
        + '                  <span class="kw">for</span> tc <span class="kw">in</span> response.tool_calls]\n\n'
        + '    <span class="kw">for</span> tc <span class="kw">in</span> tool_calls:\n'
        + '        outcome = <span class="kw">yield from</span> handler.<span class="fn">dispatch</span>('
        + 'tc[<span class="st">\'tool_name\'</span>], tc[<span class="st">\'args\'</span>], response)\n'
        + '        <span class="kw">if</span> outcome.should_exit: ...        '
        + '<span class="cm"># EXITED</span>\n'
        + '        <span class="kw">if</span> <span class="kw">not</span> outcome.next_prompt: ...   '
        + '<span class="cm"># CURRENT_TASK_DONE</span>\n'
        + '        tool_results.<span class="fn">append</span>(...)\n\n'
        + '    <span class="cm"># ' + t('只把新消息带入下一轮，历史由 Session 保存', 'only the new message goes to the next turn; history is kept by Session') + '</span>\n'
        + '    messages = [{<span class="st">\'role\'</span>: <span class="st">\'user\'</span>, '
        + '<span class="st">\'content\'</span>: next_prompt, '
        + '<span class="st">\'tool_results\'</span>: tool_results}]\n'
        + '</pre></div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<p>'
        + t('每一步都能在源码里指认到：', 'Every step maps to a concrete spot in the source:')
        + '</p><ul>'
        + '<li>' + t('循环本体：', 'The loop itself: ')
        + '<span class="inline">agent_loop.py: agent_runner_loop</span>'
        + t('，初始 messages 就是 system_prompt + user_input。',
            '; the initial messages are system_prompt + user_input.') + '</li>'
        + '<li>' + t('工具派发：', 'Tool dispatch: ')
        + '<span class="inline">agent_loop.py: BaseHandler.dispatch</span>'
        + t('，用 ', ' looks up ')
        + '<span class="inline">do_&lt;tool&gt;</span>'
        + t(' 找到并执行对应方法（实现见 ', ' and runs it (implementations in ')
        + '<span class="inline">ga.py: GenericAgentHandler</span>' + t('）。', ').') + '</li>'
        + '<li>' + t('每步的结果契约：', 'The per-step contract: ')
        + '<span class="inline">agent_loop.py: StepOutcome</span>'
        + t('，三个字段 data / next_prompt / should_exit 决定循环何去何从。',
            ' — its three fields data / next_prompt / should_exit decide where the loop goes.') + '</li>'
        + '<li>' + t('模型与工具调用：', 'Model & tool calls: ')
        + '<span class="inline">llmcore.py: chat</span>'
        + t(' 返回的 response 带 ', ' returns a response carrying ')
        + '<span class="inline">response.tool_calls</span>'
        + t('，由循环逐个解析执行。', ', which the loop parses and runs one by one.') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + '<p>'
        + t(
            '像一位<strong>主厨（大模型）和一名助手（循环）</strong>配合做菜。助手报一遍现状（messages），'
            '主厨说“去把洋葱切了”（tool_call）；助手照做（do_&lt;tool&gt;），把切好的洋葱和一句“切好了，下一步？”'
            '（StepOutcome 的 data + next_prompt）端回去；主厨再下一道指令。'
            '直到主厨说“齐活，上菜”（should_exit）——这一桌就完成了。',
            'Think of a <strong>head chef (the LLM) and an assistant (the loop)</strong> cooking '
            'together. The assistant recaps the situation (messages); the chef says "go dice the '
            'onions" (a tool_call); the assistant does it (do_&lt;tool&gt;) and brings back the diced '
            'onions plus "done, what next?" (a StepOutcome\'s data + next_prompt); the chef issues '
            'the next instruction. When the chef finally says "that\'s it, plate it up" '
            '(should_exit), the dish is complete.',
        )
        + '</p></div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('一次任务 = 一个 while 循环，每轮一个 turn，最多 max_turns（默认 40）。',
                    'A task = one while loop; each pass is a turn, up to max_turns (default 40).') + '</li>'
        + '<li>' + t('单轮节奏：chat → tool_calls → dispatch → do_&lt;tool&gt; → StepOutcome → 写回 messages。',
                    'Per-turn rhythm: chat → tool_calls → dispatch → do_&lt;tool&gt; → StepOutcome → back into messages.') + '</li>'
        + '<li>' + t('StepOutcome 三字段是循环的“方向盘”：data、next_prompt、should_exit。',
                    'StepOutcome\'s three fields are the loop\'s steering wheel: data, next_prompt, should_exit.') + '</li>'
        + '<li>' + t('结束有三种：should_exit、没有 next_prompt（任务完成）、达到 max_turns。',
                    'Three ways to end: should_exit, no next_prompt (task done), or hitting max_turns.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + '<p>'
        + t(
            '注意那一行 <span class="inline">messages = [{...新消息...}]</span>：每轮只往下传<strong>一条新消息</strong>，'
            '而不是把越滚越长的历史整段重发。完整历史交给 Session 维护，循环只搬运“这一步的增量”。'
            '正是这个小设计，让上下文长期保持在 30K 以内——省 token、少噪声、更稳定，全都源于此。',
            'Notice the line <span class="inline">messages = [{...new message...}]</span>: each turn '
            'passes only <strong>one new message</strong> downward, instead of re-sending an '
            'ever-growing transcript. The full history is kept by the Session, and the loop carries '
            'just "the delta of this step". This small choice is exactly what keeps the context under '
            '~30K — token-thrifty, low-noise and more stable, all from here.',
        )
        + '</p></div>'
    )
