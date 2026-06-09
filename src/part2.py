"""Part 2 — 用户视角 / Using It (lessons 04–07).

Each lesson is a ``lesson(t)`` function. ``t('中文', 'English')`` wraps every
piece of prose; structure, diagrams and code are written once and shared by
both language renders. All technical claims are grounded in the real
GenericAgent source (docs/installation.md, mykey_template.py, pyproject.toml,
frontends/*, ga.py, assets/tools_schema.json).

Authoring conventions are documented at the top of ``part1.py`` — follow the
same 5-card lesson format (🌍 macro / 🔬 detail / 🧩 analogy / ✅ key /
💡 spark) and the ``.inline`` (prose code) vs ``.mono`` (dense components) rule.
"""


def lesson_04(t):
    """安装与启动 / Install & Launch."""
    return (
        '<p class="lead">'
        + t(
            'GenericAgent 的安装非常轻：装好一个隔离的 Python 环境、填一把模型 API key，就能跑起来。'
            '它<strong>故意不预装</strong>一大堆依赖——需要什么能力，交给 Agent 自己在运行时去长。',
            'Installing GenericAgent is light: set up an isolated Python environment, fill in one '
            'model API key, and you are running. It <strong>deliberately avoids</strong> preloading '
            'a pile of dependencies — whatever capability you need, the agent grows it at runtime.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '有两条安装路线。<strong>普通用户</strong>用一行安装脚本，它会自带一个隔离的 Python 和 Git，'
            '再下载一个开箱即用的包；装完直接运行桌面端即可。<strong>开发者</strong>则克隆仓库、用 '
            '<span class="inline">uv</span> 建虚拟环境、可编辑安装，然后填 key 启动——这条路更适合读源码、改代码。',
            'There are two install paths. <strong>Regular users</strong> run a one-line installer that '
            'ships an isolated Python and Git and downloads a ready-to-run package; then just launch '
            'the desktop app. <strong>Developers</strong> clone the repo, create a virtualenv with '
            '<span class="inline">uv</span>, do an editable install, fill in the key and launch — this '
            'path is better for reading and changing the source.',
        )
        + '</p></div>'

        + '<h2>' + t('开发者安装四步', 'Developer install in four steps') + '</h2>'
        + '<div class="vflow">'
        + '<div class="step"><div class="num">1</div><div class="sc"><h4>'
        + t('克隆仓库', 'Clone the repo') + '</h4><p class="mono">git clone … &amp;&amp; cd GenericAgent</p></div></div>'
        + '<div class="step"><div class="num">2</div><div class="sc"><h4>'
        + t('建环境', 'Create the env') + '</h4><p class="mono">uv venv</p><p>'
        + t('用 uv 建一个隔离虚拟环境。', 'Create an isolated virtualenv with uv.') + '</p></div></div>'
        + '<div class="step"><div class="num">3</div><div class="sc"><h4>'
        + t('装依赖', 'Install deps') + '</h4><p class="mono">uv pip install -e ".[ui]"</p><p>'
        + t('可编辑安装核心 + UI 依赖（pyproject.toml 里的 [ui] 额外组）。',
            'Editable install of core + UI deps (the [ui] extra in pyproject.toml).') + '</p></div></div>'
        + '<div class="step"><div class="num">4</div><div class="sc"><h4>'
        + t('填 key 并启动', 'Add your key & launch') + '</h4>'
        + '<p class="mono">cp mykey_template.py mykey.py</p><p class="mono">python launch.pyw</p><p>'
        + t('把模型 API key 填进 mykey.py，然后启动。',
            'Put your model API key into mykey.py, then launch.') + '</p></div></div>'
        + '</div>'

        + '<div class="card warn"><div class="tag">⚠️ '
        + t('Python 版本', 'Python version') + '</div>'
        + '<p>'
        + t(
            '务必使用 <strong>Python 3.11 或 3.12</strong>。<strong>不要用 3.14</strong>——它与 '
            '<span class="inline">pywebview</span> 及若干 GA 依赖不兼容。一行安装脚本自带隔离 Python，'
            '通常无需你手动配 Python。',
            'Use <strong>Python 3.11 or 3.12</strong>. <strong>Do not use 3.14</strong> — it is '
            'incompatible with <span class="inline">pywebview</span> and a few GA dependencies. The '
            'one-line installer ships an isolated Python, so manual Python setup is usually '
            'unnecessary.',
        )
        + '</p></div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('完整安装说明在 ', 'Full install docs live in ')
        + '<span class="inline">docs/installation.md</span>' + t('（中文版 ', ' (Chinese: ')
        + '<span class="inline">docs/installation_zh.md</span>' + t('，新手向 ', ', getting-started: ')
        + '<span class="inline">docs/GETTING_STARTED.md</span>' + t('）。', ').') + '</li>'
        + '<li>' + t('密钥模板是 ', 'The key template is ')
        + '<span class="inline">mykey_template.py</span>'
        + t('；GA 原生支持两种协议：<strong>OpenAI 兼容</strong>接口与 <strong>Anthropic Claude 原生</strong>接口，'
            '因此 GPT / Claude / Kimi / MiniMax / DeepSeek / GLM / Qwen / Gemini 等都能配。',
            '; GA natively speaks two protocols: <strong>OpenAI-compatible</strong> and '
            '<strong>Anthropic Claude native</strong>, so GPT / Claude / Kimi / MiniMax / DeepSeek / '
            'GLM / Qwen / Gemini and others can all be configured.') + '</li>'
        + '<li>' + t('依赖在 ', 'Dependencies are declared in ')
        + '<span class="inline">pyproject.toml</span>'
        + t(' 里声明，UI 相关放在 ', ', with UI extras grouped under ')
        + '<span class="inline">[ui]</span>'
        + t(' 额外组；启动入口是 ', '; the launch entry is ')
        + '<span class="inline">launch.pyw</span>'
        + t('。也可用 ', '. You can also run ')
        + '<span class="inline">python assets/configure_mykey.py</span>'
        + t(' 交互式配置密钥。', ' to configure the key interactively.') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像租一间<strong>毛坯但通水电的厨房</strong>：你先接上水电（Python 环境）、挂上门牌（API key），'
            '就能开火。至于打蛋器、烤箱这些专用工具，等真要做某道菜时，厨师（Agent）自己去买、去装——'
            '而不是开业前先把一整面墙堆满你可能永远用不到的器材。',
            'It is like renting a <strong>bare kitchen with water and power hooked up</strong>: connect '
            'the utilities (the Python env), hang your nameplate (the API key), and you can start '
            'cooking. The specialty tools — the whisk, the oven — are bought and installed by the chef '
            '(the agent) only when a dish actually needs them, instead of cramming a whole wall with '
            'gear you may never use before opening day.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('两条路：用户走一行安装脚本 + 桌面端；开发者走 uv + 可编辑安装。',
            'Two paths: users take the one-line installer + desktop app; developers take uv + editable install.') + '</li>'
        + '<li>' + t('Python 用 3.11 / 3.12，避开 3.14。',
            'Use Python 3.11 / 3.12; avoid 3.14.') + '</li>'
        + '<li>' + t('核心配置只有一处：mykey.py 里的模型 API key。',
            'The only core config is your model API key in mykey.py.') + '</li>'
        + '<li>' + t('启动用 python launch.pyw。', 'Launch with python launch.pyw.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '“装得少”本身就是设计的一部分。GenericAgent 不在安装时穷举所有依赖，而是让 Agent 在执行任务时'
            '<strong>按需自己安装</strong>（通过 code_run）。安装步骤越短，意味着能力不是被“配置”出来的，而是被'
            '<strong>“长”出来的</strong>——这正呼应了它“不预设技能、靠进化获得能力”的核心哲学。',
            'Installing little is itself part of the design. GenericAgent does not enumerate every '
            'dependency at install time; it lets the agent <strong>install what it needs on demand</strong> '
            '(via code_run) while doing a task. A short install means capability is not "configured" but '
            '<strong>grown</strong> — echoing its core philosophy of not preloading skills but evolving them.',
        )
        + '</div>'
    )


def lesson_05(t):
    """前端形态总览 / Frontends Overview."""
    return (
        '<p class="lead">'
        + t(
            '同一个 Agent 内核，可以套上很多张“脸”：桌面应用、终端 UI、Streamlit 网页，还有 Telegram、微信、'
            'QQ、飞书、企业微信、钉钉等一票 IM 机器人，甚至一只趴在桌面的桌宠。',
            'One agent core can wear many faces: a desktop app, a terminal UI, a Streamlit web page, and '
            'a whole set of IM bots — Telegram, WeChat, QQ, Feishu/Lark, WeCom, DingTalk — plus a desktop '
            'pet that sits on your screen.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '前端只负责<strong>收消息、显消息</strong>，真正干活的永远是同一套 Agent 循环。所以换界面不换大脑：'
            '你可以在终端里调试，也可以从微信发一句话让它办事，背后跑的是同一个 GenericAgent。',
            'A frontend only <strong>collects and displays messages</strong>; the real work always runs on '
            'the same agent loop. So you switch the face, not the brain: debug it in a terminal, or send it '
            'a WeChat message to get something done — the same GenericAgent runs behind both.',
        )
        + '</p></div>'

        + '<h2>' + t('前端一览表', 'Frontends at a glance') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('形态', 'Form') + '</th><th>' + t('启动命令 / 文件', 'Command / file') + '</th>'
        + '<th>' + t('说明', 'Notes') + '</th></tr>'
        + '<tr><td>' + t('桌面应用', 'Desktop app') + '</td><td class="mono">frontends/GenericAgent.exe</td><td>'
        + t('一行安装后双击即用（Windows）。', 'Double-click after the one-line install (Windows).') + '</td></tr>'
        + '<tr><td>' + t('终端 UI', 'Terminal UI') + '</td><td class="mono">frontends/tuiapp_v2.py</td><td>'
        + t('基于 Textual，键盘驱动，支持多会话与实时流式（另有 tui_v3.py）。',
            'Textual-based, keyboard-driven, multi-session and live streaming (also tui_v3.py).') + '</td></tr>'
        + '<tr><td>Streamlit</td><td class="mono">launch.pyw</td><td>'
        + t('网页 UI（stapp.py / stapp2.py）。', 'Web UI (stapp.py / stapp2.py).') + '</td></tr>'
        + '<tr><td>Telegram</td><td class="mono">frontends/tgapp.py</td><td>'
        + t('Telegram 机器人。', 'Telegram bot.') + '</td></tr>'
        + '<tr><td>' + t('微信', 'WeChat') + '</td><td class="mono">frontends/wechatapp.py</td><td>'
        + t('微信机器人。', 'WeChat bot.') + '</td></tr>'
        + '<tr><td>QQ</td><td class="mono">frontends/qqapp.py</td><td>' + t('QQ 机器人。', 'QQ bot.') + '</td></tr>'
        + '<tr><td>' + t('飞书 / Lark', 'Feishu / Lark') + '</td><td class="mono">frontends/fsapp.py</td><td>'
        + t('飞书机器人。', 'Feishu/Lark bot.') + '</td></tr>'
        + '<tr><td>' + t('企业微信', 'WeCom') + '</td><td class="mono">frontends/wecomapp.py</td><td>'
        + t('企业微信机器人。', 'WeCom bot.') + '</td></tr>'
        + '<tr><td>' + t('钉钉', 'DingTalk') + '</td><td class="mono">frontends/dingtalkapp.py</td><td>'
        + t('钉钉机器人。', 'DingTalk bot.') + '</td></tr>'
        + '<tr><td>' + t('桌面宠物', 'Desktop pet') + '</td><td class="mono">frontends/desktop_pet.pyw</td><td>'
        + t('趴在桌面的伴随式入口（另有 desktop_pet_v2.pyw）。',
            'A companion entry that sits on the desktop (also desktop_pet_v2.pyw).') + '</td></tr>'
        + '<tr><td>Conductor</td><td class="mono">frontends/conductor.py</td><td>'
        + t('多 subagent 编排入口。', 'A multi-subagent orchestration entry.') + '</td></tr>'
        + '</table>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('所有界面都在 ', 'All UIs live under ')
        + '<span class="inline">frontends/</span>'
        + t(' 目录下，按平台分文件（每个 *app.py 对应一个平台）。',
            ', one file per platform (each *app.py maps to a platform).') + '</li>'
        + '<li>' + t('共享逻辑集中在 ', 'Shared logic is centralized in ')
        + '<span class="inline">frontends/chatapp_common.py</span>'
        + t('，它处理通用的消息收发与 /new、/continue 等命令。',
            ', which handles common message I/O and commands like /new and /continue.') + '</li>'
        + '<li>' + t('两版终端 UI ', 'The two TUIs ')
        + '<span class="inline">tuiapp_v2.py</span>' + t(' 与 ', ' and ')
        + '<span class="inline">tui_v3.py</span>'
        + t(' 共用同一套命令面板（见 slash_cmds.py 的 PALETTE_ENTRIES）。',
            ' share one command palette (see PALETTE_ENTRIES in slash_cmds.py).') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '就像一台发动机配不同的<strong>仪表盘</strong>：方向盘、手机 App、语音助手都能开同一辆车。'
            '你选哪块仪表盘，取决于此刻坐在哪——在工位就用终端，在路上就用微信，发动机始终是同一台。',
            'Like one engine behind different <strong>dashboards</strong>: a steering wheel, a phone app, '
            'or a voice assistant can all drive the same car. Which dashboard you pick depends on where you '
            'are right now — the terminal at your desk, WeChat on the go — while the engine stays the same.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('前端只管界面，内核永远是同一套 Agent 循环。',
            'Frontends only handle the interface; the core is always the same agent loop.') + '</li>'
        + '<li>' + t('开发调试优先用 TUI（tuiapp_v2.py）或 Streamlit（launch.pyw）。',
            'For dev/debug, prefer the TUI (tuiapp_v2.py) or Streamlit (launch.pyw).') + '</li>'
        + '<li>' + t('要随手可用，就接一个 IM 机器人（Telegram / 微信 / 飞书…）。',
            'For everyday access, wire up an IM bot (Telegram / WeChat / Feishu …).') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '把<strong>界面</strong>与<strong>循环</strong>彻底解耦，是 GenericAgent 能“到处都是”的关键。'
            '因为内核不关心消息从哪来、显示到哪去，新增一个平台只需写一个薄薄的适配层（一个 *app.py），'
            '复用同一套 chatapp_common 与命令逻辑——这也是后面“扩展前端”那一课能轻松成立的根基。',
            'Cleanly decoupling the <strong>interface</strong> from the <strong>loop</strong> is what lets '
            'GenericAgent be "everywhere". Because the core does not care where a message comes from or where '
            'it is shown, adding a platform only needs a thin adapter (one *app.py) reusing the same '
            'chatapp_common and command logic — the very foundation that makes the later "extend a frontend" '
            'lesson easy.',
        )
        + '</div>'
    )


def lesson_06(t):
    """对话与斜杠命令 / Chat & Slash Commands."""
    return (
        '<p class="lead">'
        + t(
            '大部分时间你只是<strong>用大白话</strong>跟 GenericAgent 说要干嘛。少数时候，你需要管理会话或切换'
            '运行模式——这就是<strong>斜杠命令</strong>的用武之地，最常用的是 /new 和 /continue。',
            'Most of the time you just talk to GenericAgent in <strong>plain language</strong>. Occasionally '
            'you need to manage a session or switch run modes — that is where <strong>slash commands</strong> '
            'come in, the most common being /new and /continue.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '斜杠命令分两类：一类管<strong>会话</strong>（开新对话、恢复旧对话），任何前端都有；另一类是'
            '<strong>高级模式开关</strong>（自治、目标模式、多 worker 协作等），主要在终端 UI 的命令面板里。',
            'Slash commands come in two kinds: ones that manage the <strong>session</strong> (start fresh, '
            'restore an old conversation), available in every frontend; and <strong>advanced mode switches</strong> '
            '(autonomous, goal mode, multi-worker collaboration), mainly in the terminal UI command palette.',
        )
        + '</p></div>'

        + '<h2>' + t('常用会话命令', 'Everyday session commands') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('命令', 'Command') + '</th><th>' + t('作用', 'What it does') + '</th></tr>'
        + '<tr><td class="mono">/new</td><td>'
        + t('开启新对话，清空当前上下文。', 'Start a fresh conversation and clear the current context.') + '</td></tr>'
        + '<tr><td class="mono">/continue</td><td>'
        + t('列出可恢复的历史会话快照。', 'List recoverable conversation snapshots.') + '</td></tr>'
        + '<tr><td class="mono">/continue [n]</td><td>'
        + t('恢复第 n 个会话快照。', 'Restore the n-th conversation snapshot.') + '</td></tr>'
        + '</table>'

        + '<h2>' + t('进阶模式命令（终端面板）', 'Advanced mode commands (terminal palette)') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('命令', 'Command') + '</th><th>' + t('作用', 'What it does') + '</th></tr>'
        + '<tr><td class="mono">/autorun [seed]</td><td>'
        + t('进入 autonomous_operation 自主模式。', 'Enter the autonomous_operation self-run mode.') + '</td></tr>'
        + '<tr><td class="mono">/goal [goal]</td><td>'
        + t('进入 Goal 目标模式（需 condition 约束）。', 'Enter Goal mode (requires a condition constraint).') + '</td></tr>'
        + '<tr><td class="mono">/hive [target]</td><td>'
        + t('进入 Hive 多 worker 协作模式。', 'Enter Hive multi-worker collaboration mode.') + '</td></tr>'
        + '<tr><td class="mono">/conductor [task]</td><td>'
        + t('调用 conductor.py 做多 subagent 编排。', 'Invoke conductor.py for multi-subagent orchestration.') + '</td></tr>'
        + '<tr><td class="mono">/scheduler</td><td>'
        + t('启停 reflect 定时任务（由 reflect/scheduler.py 驱动）。',
            'Start/stop reflect scheduled tasks (driven by reflect/scheduler.py).') + '</td></tr>'
        + '<tr><td class="mono">/morphling [target]</td><td>'
        + t('启用 Morphling 蒸馏 / 吞噬外部技能。', 'Enable Morphling to distill / absorb external skills.') + '</td></tr>'
        + '<tr><td class="mono">/update [note]</td><td>'
        + t('git pull 更新 GA 仓库并报告影响面。', 'git pull to update the GA repo and report the impact.') + '</td></tr>'
        + '</table>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('/new 与 /continue 的派发在 ', '/new and /continue are dispatched in ')
        + '<span class="inline">frontends/chatapp_common.py</span>'
        + t('（命令清单 USER_COMMANDS、分支 op == "/new" / "/continue"）。',
            ' (the USER_COMMANDS list and the op == "/new" / "/continue" branches).') + '</li>'
        + '<li>' + t('恢复逻辑在 ', 'Restore logic lives in ')
        + '<span class="inline">frontends/continue_cmd.py</span>'
        + t('，它从 temp/model_responses 下的日志解析出历次 Prompt/Response 对与 &lt;summary&gt; 摘要，再列出可恢复会话。',
            ', which parses past Prompt/Response pairs and &lt;summary&gt; snippets from the logs under '
            'temp/model_responses and lists recoverable sessions.') + '</li>'
        + '<li>' + t('进阶命令的清单与提示词构造在 ', 'The advanced commands and their prompt builders are in ')
        + '<span class="inline">frontends/slash_cmds.py</span>'
        + t('（PALETTE_ENTRIES 表 + prompt_for / build_*_prompt 函数）。',
            ' (the PALETTE_ENTRIES table + the prompt_for / build_*_prompt functions).') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '斜杠命令像聊天框里的<strong>快捷指令</strong>：平时你正常聊天，偶尔输入一个“/”开头的口令，'
            '就能让助手切换状态——/new 像“清桌重开”，/continue 像“接着上次那盘继续下”。',
            'Slash commands are like <strong>shortcuts in a chat box</strong>: you chat normally, and now and '
            'then type a "/"-prefixed keyword to flip the assistant\'s state — /new is "clear the table and '
            'start over", /continue is "pick up the previous game where we left off".',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('记三个就够用：/new 清空重开、/continue 看历史、/continue n 恢复第 n 个。',
            'Three are enough for daily use: /new to reset, /continue to list history, /continue n to restore the n-th.') + '</li>'
        + '<li>' + t('进阶命令（/autorun、/goal、/hive…）主要在终端 UI 的命令面板里。',
            'Advanced commands (/autorun, /goal, /hive …) live mainly in the terminal UI palette.') + '</li>'
        + '<li>' + t('历史会话存在 temp/model_responses 的日志里，可随时恢复。',
            'Past sessions are stored as logs under temp/model_responses and can be restored anytime.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '许多进阶命令并不是“硬编码的功能”，而是<strong>把一段精心写好的提示词注入对话</strong>'
            '（看 slash_cmds.py 里的 build_*_prompt）。命令只是模式的“触发器”，真正的行为仍由 Agent 读提示词后自己执行——'
            '所以加一个新模式，往往只是加一个提示词构造函数，而不必改内核。',
            'Many advanced commands are not "hard-coded features" but <strong>inject a carefully written '
            'prompt into the conversation</strong> (see the build_*_prompt functions in slash_cmds.py). The '
            'command is just a "trigger" for a mode; the real behavior is still carried out by the agent after '
            'it reads the prompt — so adding a new mode is often just adding a prompt builder, with no change to '
            'the core.',
        )
        + '</div>'
    )


def lesson_07(t):
    """九个原子工具 / The Nine Atomic Tools."""
    return (
        '<p class="lead">'
        + t(
            'GenericAgent 只给大模型<strong>九个原子工具</strong>。就是这九件“最小够用”的工具，构成了它与外部世界'
            '交互的全部基础能力——代码、文件、网页、问人、记忆，五类齐活。',
            'GenericAgent gives the model just <strong>nine atomic tools</strong>. These nine "minimal but '
            'sufficient" tools form the entire foundation for interacting with the outside world — code, files, '
            'web, asking the human, and memory: five categories in all.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '别的框架靠“工具多”取胜，GenericAgent 靠“工具少而通用”取胜。九个工具是<strong>正交</strong>的：每个负责一类'
            '最基本的动作，复杂能力不是再加新工具，而是用 <span class="inline">code_run</span> 写代码<strong>临时造</strong>出来。',
            'Other frameworks win by having many tools; GenericAgent wins by having few, general ones. The nine '
            'tools are <strong>orthogonal</strong>: each owns one basic kind of action, and complex capabilities '
            'are not added as new tools but <strong>improvised</strong> by writing code with '
            '<span class="inline">code_run</span>.',
        )
        + '</p></div>'

        + '<h2>' + t('九个原子工具', 'The nine atomic tools') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('类别', 'Category') + '</th><th>' + t('工具', 'Tool') + '</th>'
        + '<th>' + t('作用', 'What it does') + '</th></tr>'
        + '<tr><td rowspan="4">' + t('代码 / 文件', 'Code / File') + '</td>'
        + '<td class="mono">code_run</td><td>'
        + t('执行任意代码（首选 Python，也可 PowerShell）。', 'Run arbitrary code (Python preferred, also PowerShell).') + '</td></tr>'
        + '<tr><td class="mono">file_read</td><td>'
        + t('读文件（改前先读，拿到最新内容与行号）。', 'Read a file (read before editing, to get latest content and line numbers).') + '</td></tr>'
        + '<tr><td class="mono">file_patch</td><td>'
        + t('精确替换：把唯一匹配的旧内容换成新内容。', 'Precise replace: swap a uniquely matching old chunk for new content.') + '</td></tr>'
        + '<tr><td class="mono">file_write</td><td>'
        + t('创建 / 覆盖 / 追加文件（仅用于大段写入）。', 'Create / overwrite / append a file (for large writes only).') + '</td></tr>'
        + '<tr><td rowspan="2">' + t('网页', 'Web') + '</td>'
        + '<td class="mono">web_scan</td><td>'
        + t('感知网页：拿到简化 HTML 与标签页列表。', 'Perceive the web: get simplified HTML and the tab list.') + '</td></tr>'
        + '<tr><td class="mono">web_execute_js</td><td>'
        + t('在真实浏览器里执行 JS 来操作网页。', 'Execute JS in a real browser to drive the page.') + '</td></tr>'
        + '<tr><td>' + t('问人', 'Human') + '</td>'
        + '<td class="mono">ask_user</td><td>'
        + t('遇到决策 / 缺信息 / 卡死时打断任务问用户。', 'Interrupt to ask the user on decisions, missing info, or blockers.') + '</td></tr>'
        + '<tr><td rowspan="2">' + t('记忆', 'Memory') + '</td>'
        + '<td class="mono">update_working_checkpoint</td><td>'
        + t('短期工作便签，每轮自动注入，防长任务丢信息。', 'A short-term working notepad, auto-injected each turn to prevent info loss in long tasks.') + '</td></tr>'
        + '<tr><td class="mono">start_long_term_update</td><td>'
        + t('启动长期记忆蒸馏，沉淀值得记住的经验。', 'Start distilling long-term memory to crystallize lessons worth remembering.') + '</td></tr>'
        + '</table>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('九个工具的实现都是 ', 'All nine tools are implemented as ')
        + '<span class="inline">do_&lt;tool&gt;</span>'
        + t(' 方法，集中在 ', ' methods, gathered in ')
        + '<span class="inline">ga.py: GenericAgentHandler</span>'
        + t('（如 do_code_run、do_file_read、do_web_scan、do_ask_user、do_update_working_checkpoint…）。',
            ' (e.g. do_code_run, do_file_read, do_web_scan, do_ask_user, do_update_working_checkpoint …).') + '</li>'
        + '<li>' + t('工具的“说明书”（名字、描述、参数）在 ', 'The tool "manuals" (names, descriptions, params) are in ')
        + '<span class="inline">assets/tools_schema.json</span>'
        + t('（中文版 ', ' (Chinese: ')
        + '<span class="inline">assets/tools_schema_cn.json</span>'
        + t('），由 agentmain.py 读入后交给循环。',
            '), loaded by agentmain.py and handed to the loop.') + '</li>'
        + '<li>' + t('几个值得记的参数：code_run 用 ', 'A few params worth knowing: code_run takes ')
        + '<span class="inline">script</span>'
        + t('；file_patch 用 ', '; file_patch takes ')
        + '<span class="inline">old_content / new_content</span>'
        + t('（要求唯一精确匹配）；ask_user 可带 ', ' (requires a unique exact match); ask_user can carry ')
        + '<span class="inline">candidates</span>'
        + t(' 候选项。', ' candidate options.') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像一把<strong>瑞士军刀</strong>：刀片不多，但每一片都通用。真碰到拧不动的特殊螺丝，你不会指望军刀上凭空多出一个'
            '专用旋具——而是用刀片这种“通用件”现做一个。GenericAgent 的 code_run 就是那把能“现做工具的刀片”。',
            'Like a <strong>Swiss Army knife</strong>: few blades, but each is general. When you hit an oddly '
            'shaped screw, you do not expect a dedicated driver to appear out of nowhere — you improvise one using '
            'the general blades. GenericAgent\'s code_run is exactly that "blade that makes other tools on the spot".',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('九个工具五类：代码 / 文件（4）、网页（2）、问人（1）、记忆（2）。',
            'Nine tools in five groups: code/file (4), web (2), human (1), memory (2).') + '</li>'
        + '<li>' + t('它们正交、最小够用；复杂能力靠 code_run 现场组合。',
            'They are orthogonal and minimal; complex capability is composed on the fly via code_run.') + '</li>'
        + '<li>' + t('实现看 ga.py 的 do_* 方法，描述看 assets/tools_schema.json。',
            'See ga.py do_* methods for implementations and assets/tools_schema.json for descriptions.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            'code_run 是九个工具里的<strong>“元工具”</strong>：因为它能执行任意代码，就能在运行时装包、调外部 API、写新脚本，'
            '甚至把一段临时能力固化成永久工具。正是这一个工具，把“只有九件工具”的极简框架，变成了一个能<strong>自我生长</strong>的系统——'
            '这也是后面“自进化机制”那一课的伏笔。',
            'code_run is the <strong>"meta-tool"</strong> among the nine: because it runs arbitrary code, it can '
            'install packages, call external APIs, write new scripts, even crystallize a temporary capability into a '
            'permanent tool at runtime. This single tool turns a "only nine tools" minimal framework into a system '
            'that can <strong>grow itself</strong> — foreshadowing the later "self-evolution" lesson.',
        )
        + '</div>'
    )
