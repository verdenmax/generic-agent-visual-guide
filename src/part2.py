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

import components as c


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
        + '<div class="step"><div class="num">1</div><div class="sc"><h3>'
        + t('克隆仓库', 'Clone the repo') + '</h3><p class="mono">git clone … &amp;&amp; cd GenericAgent</p></div></div>'
        + '<div class="step"><div class="num">2</div><div class="sc"><h3>'
        + t('建环境', 'Create the env') + '</h3><p class="mono">uv venv</p><p>'
        + t('用 uv 建一个隔离虚拟环境。', 'Create an isolated virtualenv with uv.') + '</p></div></div>'
        + '<div class="step"><div class="num">3</div><div class="sc"><h3>'
        + t('装依赖', 'Install deps') + '</h3><p class="mono">uv pip install -e ".[ui]"</p><p>'
        + t('可编辑安装核心 + UI 依赖（pyproject.toml 里的 [ui] 额外组）。',
            'Editable install of core + UI deps (the [ui] extra in pyproject.toml).') + '</p></div></div>'
        + '<div class="step"><div class="num">4</div><div class="sc"><h3>'
        + t('填 key 并启动', 'Add your key & launch') + '</h3>'
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

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '两条安装路线：一行脚本 vs uv 可编辑安装',
            'Two install paths: one-line installer vs uv editable install',
            c.qa(t, '🧪 两条命令', 'The two commands',
                 '<p>' + t(
                     '一行安装（Linux/macOS，见 docs/installation.md「Method 1」）：',
                     'One-line install (Linux/macOS, see "Method 1" in docs/installation.md):') + '</p>'
                 + c.codefile('docs/installation.md', 'Method 1',
                     'GLOBAL=1 bash -c "$(curl -fsSL '
                     'http://fudankw.cn:9000/files/ga_install.sh)"')
                 + '<p>' + t('开发者可编辑安装（「Method 2」）：', 'Developer editable install ("Method 2"):') + '</p>'
                 + c.codefile('docs/installation.md', 'Method 2',
                     'git clone https://github.com/lsdefine/GenericAgent.git\n'
                     'cd GenericAgent\n'
                     'uv venv\n'
                     'uv pip install -e ".[ui]"\n'
                     'cp mykey_template.py mykey.py\n'
                     'python launch.pyw'))
            + c.qa(t, '⚙️ 一行脚本内部做了什么', 'What the one-line installer does',
                   '<p>' + t(
                       '据 docs/installation.md：它<strong>准备一个隔离运行时</strong>（自带 Python 与 Git）、'
                       '下载 GenericAgent、装上<strong>核心</strong>依赖，并给你一棵可直接运行的本地工程树——'
                       '装完从 <span class="inline">frontends/GenericAgent.exe</span> 或 '
                       '<span class="inline">python launch.pyw</span> 启动即可。注意它只装“核心”，'
                       '而非全部依赖。',
                       'Per docs/installation.md it <strong>prepares an isolated runtime</strong> (its own Python '
                       'and Git), downloads GenericAgent, installs the <strong>core</strong> dependencies, and hands '
                       'you a ready-to-run local project tree — then launch from '
                       '<span class="inline">frontends/GenericAgent.exe</span> or '
                       '<span class="inline">python launch.pyw</span>. Note it installs only the "core", not every '
                       'dependency.') + '</p>')
            + c.qa(t, '🔀 用户路线 vs 开发者路线', 'User path vs developer path',
                   '<table class="t"><tr><th>' + t('维度', 'Aspect') + '</th><th>'
                   + t('一行脚本', 'One-line') + '</th><th>' + t('uv 可编辑', 'uv editable') + '</th></tr>'
                   + '<tr><td>' + t('适合', 'For') + '</td><td>' + t('普通用户', 'regular users')
                   + '</td><td>' + t('读源码 / 改代码', 'reading & changing source') + '</td></tr>'
                   + '<tr><td>Python</td><td>' + t('自带隔离', 'bundled, isolated')
                   + '</td><td>' + t('自己用 uv 建', 'you build it with uv') + '</td></tr>'
                   + '<tr><td>' + t('安装方式', 'Install') + '</td><td>' + t('打包下载', 'packaged download')
                   + '</td><td class="mono">uv pip install -e ".[ui]"</td></tr>'
                   + '<tr><td>' + t('更新', 'Update') + '</td><td>' + t('重跑脚本', 're-run script')
                   + '</td><td class="mono">git pull</td></tr></table>'))
        + c.accordion(t, 2, 'mykey.py 与两种 API 协议：模型怎么配',
            'mykey.py and the two API protocols: how models are configured',
            c.qa(t, '🧪 一个最简配置', 'A minimal config',
                 '<p>' + t(
                     '把 <span class="inline">mykey_template.py</span> 复制成 mykey.py，'
                     '填一个 provider 即可。OpenAI 兼容的最简例子（变量名含 native+oai → NativeOAISession）：',
                     'Copy <span class="inline">mykey_template.py</span> to mykey.py and fill one provider. '
                     'A minimal OpenAI-compatible example (a var name with native+oai → NativeOAISession):') + '</p>'
                 + c.codefile('mykey.py', 'native_oai_config',
                     'native_oai_config = {\n'
                     "    'apikey': 'sk-&lt;your-openai-key&gt;',\n"
                     "    'apibase': 'https://api.openai.com/v1',\n"
                     "    'model': 'gpt-5.4',\n"
                     '}'))
            + c.qa(t, '⚙️ agentmain 如何按变量名路由', 'How agentmain routes by variable name',
                   '<p>' + t(
                       '据 mykey_template.py 顶部说明：<span class="inline">agentmain.py</span> 只扫描'
                       '<strong>变量名同时含 api/config/cookie</strong> 的条目，再按名字里的关键字决定实例化哪个 '
                       'Session 类——',
                       'Per the header of mykey_template.py: <span class="inline">agentmain.py</span> only scans '
                       'entries whose <strong>variable name contains api/config/cookie</strong>, then picks a Session '
                       'class by the keywords in that name —') + '</p>'
                   + '<table class="t"><tr><th>' + t('变量名关键字', 'Name keyword') + '</th><th>'
                   + t('Session 类', 'Session class') + '</th></tr>'
                   + '<tr><td>' + t('native + claude', 'native + claude') + '</td><td class="mono">NativeClaudeSession</td></tr>'
                   + '<tr><td>' + t('native + oai', 'native + oai') + '</td><td class="mono">NativeOAISession</td></tr>'
                   + '<tr><td>' + t('claude（无 native）', 'claude (no native)') + '</td><td class="mono">ClaudeSession</td></tr>'
                   + '<tr><td>' + t('oai（无 native）', 'oai (no native)') + '</td><td class="mono">LLMSession</td></tr>'
                   + '<tr><td>mixin</td><td class="mono">MixinSession</td></tr></table>'
                   + '<p>' + t(
                       '所以命名即配置：<span class="inline">native_claude_xxx</span> 走原生 Claude，'
                       '<span class="inline">native_oai_xxx</span> 走原生 OpenAI。',
                       'So the name is the config: <span class="inline">native_claude_xxx</span> goes native Claude, '
                       '<span class="inline">native_oai_xxx</span> goes native OpenAI.') + '</p>')
            + c.qa(t, '❓ Native 与非 Native 的区别', 'Native vs non-Native',
                   '<p>' + t(
                       '<strong>Native</strong> = 工具调用走 API 文档里的 tool 字段（function calling），'
                       '这是 Claude Code / Codex 的原生方式；被 API tool 字段“训到 overfit”的模型（如 Claude '
                       'Opus/Sonnet）只认这种格式。<strong>非 Native</strong> 把工具描述塞进 text 字段（文本协议），'
                       '兼容性更强但对这类模型效果打折。mykey_template.py 建议新手优先用 '
                       '<span class="inline">native_claude_config</span> / '
                       '<span class="inline">native_oai_config</span>。',
                       '<strong>Native</strong> = tool calls use the API\'s native tool field (function calling), the '
                       'way Claude Code / Codex work; models overfit to that field (e.g. Claude Opus/Sonnet) only '
                       'recognize this format. <strong>Non-Native</strong> stuffs tool descriptions into the text '
                       'field (a text protocol) — more compatible but weaker for such models. mykey_template.py '
                       'recommends beginners prefer <span class="inline">native_claude_config</span> / '
                       '<span class="inline">native_oai_config</span>.') + '</p>')
            + c.qa(t, '🧪 能配哪些模型', 'Which models can be configured',
                   '<p>' + t(
                       '因为 GA 原生说<strong>两种协议</strong>，凡是提供 OpenAI 兼容或 Anthropic Messages 兼容'
                       '端点的家族都能配：GPT 家族、Claude、Kimi、MiniMax、DeepSeek、GLM（智谱 /api/anthropic）、'
                       'Qwen、Gemini（经 OAI 兼容网关）等——mykey_template.py 里对它们各给了注释示例。',
                       'Because GA natively speaks <strong>two protocols</strong>, any family exposing an '
                       'OpenAI-compatible or Anthropic-Messages-compatible endpoint works: GPT family, Claude, Kimi, '
                       'MiniMax, DeepSeek, GLM (Zhipu /api/anthropic), Qwen, Gemini (via an OAI-compatible gateway) '
                       'and more — mykey_template.py ships a commented example for each.') + '</p>'))
        + c.accordion(t, 3, 'Python 3.14 / pywebview 坑，以及 [ui] 额外组',
            'The Python 3.14 / pywebview pitfall, and the [ui] extra',
            c.qa(t, '⚠️ 为什么不能用 3.14', 'Why not 3.14',
                 '<p>' + t(
                     'pyproject.toml 把 <span class="inline">requires-python</span> 钉在 '
                     '<span class="mono">&gt;=3.10,&lt;3.14</span>。docs/installation.md 明确：3.14 与 '
                     '<span class="inline">pywebview</span> 及若干 GA 依赖不兼容；若系统 python 是 3.14，'
                     '改用一行安装脚本，或用 uv 建一个 3.11 / 3.12 环境。',
                     'pyproject.toml pins <span class="inline">requires-python</span> to '
                     '<span class="mono">&gt;=3.10,&lt;3.14</span>. docs/installation.md states plainly: 3.14 is '
                     'incompatible with <span class="inline">pywebview</span> and a few GA deps; if your system '
                     'python is 3.14, use the one-line installer or create a 3.11 / 3.12 env with uv.') + '</p>')
            + c.qa(t, '🧪 [ui] 额外组里有什么', 'What is inside the [ui] extra',
                   '<p>' + t(
                       'pyproject.toml 的 <span class="inline">[project.optional-dependencies]</span> 把 UI 依赖'
                       '单独归到 <span class="inline">ui</span> 组——核心很瘦，UI 是按需加装的：',
                       'In pyproject.toml the <span class="inline">[project.optional-dependencies]</span> group '
                       'isolates UI deps under <span class="inline">ui</span> — the core stays lean, UI is opt-in:') + '</p>'
                   + c.codefile('pyproject.toml', '[ui]',
                       'ui = [\n'
                       '    "streamlit&gt;=1.28",\n'
                       '    "pywebview&gt;=4.0",\n'
                       '    "textual&gt;=0.70",\n'
                       '    "prompt_toolkit&gt;=3.0,&lt;4",\n'
                       '    "rich&gt;=13.0",\n'
                       '    "pillow&gt;=9.0",\n'
                       ']')
                   + '<p>' + t(
                       '所以 <span class="inline">.[ui]</span> 才装上 Streamlit / pywebview / Textual。'
                       'IM 机器人依赖另在 <span class="inline">all-frontends</span> 组，需要哪台机器人才装。',
                       'So <span class="inline">.[ui]</span> is what pulls in Streamlit / pywebview / Textual. IM-bot '
                       'deps live in a separate <span class="inline">all-frontends</span> group, installed only if '
                       'you need a given bot.') + '</p>')
            + c.qa(t, '⚙️ configure_mykey.py 是什么', 'What configure_mykey.py is',
                   '<p>' + t(
                       '不想手改字典，可运行 <span class="inline">python assets/configure_mykey.py</span> '
                       '交互式填写密钥（docs/installation.md「Configure your LLM key」一节列为可选 helper）。'
                       '它只是 mykey.py 的一个引导器，最终落地的仍是那张 *_config 字典。',
                       'If you would rather not hand-edit the dict, run '
                       '<span class="inline">python assets/configure_mykey.py</span> for an interactive key setup '
                       '(listed as an optional helper under "Configure your LLM key" in docs/installation.md). It is '
                       'just a wizard for mykey.py; what it produces is still that *_config dict.') + '</p>'))

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

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '一核多面：chatapp_common 到底共享了什么',
            'One core, many faces: what chatapp_common actually shares',
            c.qa(t, '⚙️ AgentChatMixin 的命令派发', 'AgentChatMixin\'s command dispatch',
                 '<p>' + t(
                     '每个 IM 前端都混入 <span class="inline">chatapp_common.py: AgentChatMixin</span>。'
                     '它的 <span class="inline">handle_command</span> 把 op 取小写后统一分派：'
                     '/help、/stop、/status、/llm、/restore、/continue、/new、/btw、/review——'
                     '各平台只需实现 <span class="inline">send_text</span>，其余共享。',
                     'Every IM frontend mixes in <span class="inline">chatapp_common.py: AgentChatMixin</span>. Its '
                     '<span class="inline">handle_command</span> lowercases op and dispatches uniformly: /help, '
                     '/stop, /status, /llm, /restore, /continue, /new, /btw, /review — each platform only implements '
                     '<span class="inline">send_text</span>, the rest is shared.') + '</p>')
            + c.qa(t, '🧪 共享了哪些通用件', 'Which shared pieces',
                   '<table class="t"><tr><th>' + t('共享件', 'Shared piece') + '</th><th>'
                   + t('作用', 'Role') + '</th></tr>'
                   + '<tr><td class="mono">HELP_COMMANDS</td><td>'
                   + t('统一的命令清单 / 帮助文本', 'the unified command list / help text') + '</td></tr>'
                   + '<tr><td class="mono">run_agent()</td><td>'
                   + t('把用户文本 put_task 进同一套 Agent 循环', 'puts user text into the same agent loop via put_task') + '</td></tr>'
                   + '<tr><td class="mono">split_text() / split_limit</td><td>'
                   + t('长回复按平台限长切分', 'splits long replies to a per-platform length cap') + '</td></tr>'
                   + '<tr><td class="mono">format_restore()</td><td>'
                   + t('/restore：从日志恢复上次对话', '/restore: restore the previous conversation from logs') + '</td></tr>'
                   + '<tr><td class="mono">ensure_single_instance()</td><td>'
                   + t('防止同一前端重复启动', 'prevents launching the same frontend twice') + '</td></tr></table>')
            + c.qa(t, '❓ 为什么能这样解耦', 'Why this decoupling works',
                   '<p>' + t(
                       '因为前端只做<strong>收消息 / 显消息</strong>，干活的永远是 '
                       '<span class="inline">self.agent.put_task(...)</span> 背后那套循环。新增一个平台'
                       '只是写一个薄薄的 <span class="inline">*app.py</span>：混入 Mixin、实现 send_text，'
                       '复用命令与恢复逻辑——这也是“扩展前端”一课能轻松成立的根基。',
                       'Because a frontend only <strong>collects and displays messages</strong>, while the real work '
                       'always runs on the loop behind <span class="inline">self.agent.put_task(...)</span>. Adding a '
                       'platform is just a thin <span class="inline">*app.py</span>: mix in the Mixin, implement '
                       'send_text, reuse the command and restore logic — the foundation that makes the "extend a '
                       'frontend" lesson easy.') + '</p>'))
        + c.accordion(t, 2, '选哪张脸：TUI vs Streamlit vs IM bot vs Conductor',
            'Which face: TUI vs Streamlit vs IM bot vs Conductor',
            c.qa(t, '🔀 三类前端的取舍', 'Trade-offs of three frontend kinds',
                 '<table class="t"><tr><th>' + t('形态', 'Form') + '</th><th>'
                 + t('优势', 'Strength') + '</th><th>' + t('适用场景', 'Best for') + '</th></tr>'
                 + '<tr><td>' + t('终端 UI（Textual）', 'Terminal UI (Textual)') + '</td><td>'
                 + t('键盘驱动 / 多会话 / 实时流式 / 有命令面板',
                     'keyboard-driven / multi-session / live streaming / has the palette') + '</td><td>'
                 + t('开发调试、跑进阶模式', 'dev/debug, running advanced modes') + '</td></tr>'
                 + '<tr><td>Streamlit</td><td>'
                 + t('网页 UI，浏览器可视、易展示', 'web UI, visual in a browser, easy to show') + '</td><td>'
                 + t('演示、桌面端无障碍场景', 'demos, headless-friendly') + '</td></tr>'
                 + '<tr><td>' + t('IM 机器人', 'IM bots') + '</td><td>'
                 + t('随身可达，手机一句话即办', 'reachable anywhere, one phone message') + '</td><td>'
                 + t('日常随手用 / 远程触发', 'everyday access / remote triggering') + '</td></tr></table>')
            + c.qa(t, '⚙️ 平台 → 启动命令', 'Platform → launch command',
                   '<table class="t"><tr><th>' + t('平台', 'Platform') + '</th><th>'
                   + t('命令 / 文件', 'Command / file') + '</th></tr>'
                   + '<tr><td>' + t('终端 UI', 'Terminal UI') + '</td><td class="mono">python frontends/tuiapp_v2.py</td></tr>'
                   + '<tr><td>Streamlit</td><td class="mono">python launch.pyw</td></tr>'
                   + '<tr><td>Telegram</td><td class="mono">python frontends/tgapp.py</td></tr>'
                   + '<tr><td>' + t('微信', 'WeChat') + '</td><td class="mono">python frontends/wechatapp.py</td></tr>'
                   + '<tr><td>' + t('飞书 / Lark', 'Feishu / Lark') + '</td><td class="mono">python frontends/fsapp.py</td></tr>'
                   + '<tr><td>' + t('钉钉', 'DingTalk') + '</td><td class="mono">python frontends/dingtalkapp.py</td></tr>'
                   + '<tr><td>Conductor</td><td class="mono">python frontends/conductor.py</td></tr></table>')
            + c.qa(t, '🧪 Conductor 这张“脸”特别在哪', 'Why Conductor is a special face',
                   '<p>' + t(
                       '<span class="inline">frontends/conductor.py</span> 不是单聊窗口，而是一个 FastAPI 服务'
                       '（默认 127.0.0.1:8900，配 conductor.html）。它在内部起一个主 '
                       '<span class="inline">GenericAgent</span> 并做<strong>多 subagent 编排</strong>，'
                       '所以它既是“前端”也是“调度台”——这也是 /conductor 命令背后调用的入口。',
                       '<span class="inline">frontends/conductor.py</span> is not a single chat window but a FastAPI '
                       'service (default 127.0.0.1:8900, with conductor.html). It spins up a main '
                       '<span class="inline">GenericAgent</span> internally and does '
                       '<strong>multi-subagent orchestration</strong>, so it is both a "frontend" and a "control '
                       'desk" — and the entry the /conductor command invokes.') + '</p>'))

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

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '/continue 恢复在内部到底怎么走',
            'How /continue restore works under the hood',
            c.qa(t, '⚙️ continue_cmd.py 的解析流程', 'The parse pipeline in continue_cmd.py',
                 '<p>' + t(
                     '<span class="inline">frontends/continue_cmd.py</span> 扫描 '
                     '<span class="inline">temp/model_responses/model_responses_*.txt</span>，每个文件即一段会话。'
                     '它用 <span class="inline">_BLOCK_RE</span> 切出 '
                     '<span class="mono">=== Prompt ===</span> / <span class="mono">=== Response ===</span> 块，'
                     '<span class="inline">_pairs()</span> 把它们配成 (prompt, response) 对，'
                     '再交给 <span class="inline">_parse_native_history()</span> 还原成 user/assistant 消息列表注回历史。',
                     '<span class="inline">frontends/continue_cmd.py</span> scans '
                     '<span class="inline">temp/model_responses/model_responses_*.txt</span> — one file per session. '
                     'It splits <span class="mono">=== Prompt ===</span> / <span class="mono">=== Response ===</span> '
                     'blocks with <span class="inline">_BLOCK_RE</span>, pairs them via '
                     '<span class="inline">_pairs()</span>, then <span class="inline">_parse_native_history()</span> '
                     'rebuilds a user/assistant message list to inject back into history.') + '</p>')
            + c.qa(t, '🧪 预览靠什么生成', 'How the preview is built',
                   '<p>' + t(
                       '会话列表里每行的预览，由 <span class="inline">_preview_from_file()</span> 给出：'
                       '它优先取文件尾窗里<strong>最后一个</strong> <span class="inline">&lt;summary&gt;</span>'
                       '（<span class="inline">_SUMMARY_RE</span> 匹配），没有或不干净时退回<strong>最后一条真实用户提问</strong>'
                       '（<span class="inline">_last_user()</span>）。所以一段会话“讲的是什么”，'
                       '主要由模型自己写的 &lt;summary&gt; 决定。',
                       'Each row\'s preview comes from <span class="inline">_preview_from_file()</span>: it prefers '
                       'the <strong>last</strong> <span class="inline">&lt;summary&gt;</span> in the file\'s tail '
                       'window (matched by <span class="inline">_SUMMARY_RE</span>), falling back to the '
                       '<strong>last real user prompt</strong> (<span class="inline">_last_user()</span>) when absent '
                       'or dirty. So what a session "is about" is mostly decided by the &lt;summary&gt; the model '
                       'wrote itself.') + '</p>')
            + c.qa(t, '⚠️ 大日志怎么不卡 UI', 'How huge logs avoid stalling the UI',
                   '<p>' + t(
                       '日志可能有十几 MB。/continue 的搜索框只在每个文件的<strong>头窗</strong>'
                       '（<span class="inline">_GREP_WIN = 1 MB</span>）里做内容 grep，'
                       '预览只读头/尾各 <span class="inline">_PREVIEW_WIN = 32 KB</span>，'
                       '并用 <span class="inline">~/.genericagent/continue_rounds_cache.json</span> 缓存轮数——'
                       '于是再大的历史也能秒开。',
                       'Logs can be tens of MB. The /continue search box greps only the <strong>head window</strong> '
                       '(<span class="inline">_GREP_WIN = 1 MB</span>) of each file, the preview reads just '
                       '<span class="inline">_PREVIEW_WIN = 32 KB</span> at head/tail, and round counts are cached in '
                       '<span class="inline">~/.genericagent/continue_rounds_cache.json</span> — so even a huge '
                       'history opens instantly.') + '</p>')
            + c.qa(t, '🔀 /restore 与 /continue 的区别', '/restore vs /continue',
                   '<p>' + t(
                       '<span class="inline">/restore</span>（chatapp_common 的 format_restore）只恢复<strong>上一次</strong>'
                       '对话上下文；<span class="inline">/continue</span> 则<strong>列出多段</strong>历史会话快照供挑选，'
                       '<span class="inline">/continue n</span> 恢复第 n 个。前者“接着上次”，后者“在历史里翻一个”。',
                       '<span class="inline">/restore</span> (format_restore in chatapp_common) only restores the '
                       '<strong>previous</strong> conversation context; <span class="inline">/continue</span> '
                       '<strong>lists multiple</strong> session snapshots to choose from, and '
                       '<span class="inline">/continue n</span> restores the n-th. The former is "resume last", the '
                       'latter is "pick one out of history".') + '</p>'))
        + c.accordion(t, 2, '进阶命令的本质：把提示词注入对话',
            'What advanced commands really are: injecting a prompt',
            c.qa(t, '⚙️ prompt_for 与 build_*_prompt', 'prompt_for and build_*_prompt',
                 '<p>' + t(
                     '终端面板里的 <span class="inline">PALETTE_ENTRIES</span>（slash_cmds.py）列出 /update、'
                     '/autorun、/morphling、/goal、/hive、/conductor、/scheduler。除 /scheduler 外，'
                     '它们都经 <span class="inline">prompt_for(cmd, args)</span> 映射到一个 '
                     '<span class="inline">build_*_prompt</span> 函数，返回一段系统风格提示词，'
                     '<strong>当作用户输入注入</strong>同一套 Agent 循环——命令本身不含业务逻辑。',
                     'The terminal palette\'s <span class="inline">PALETTE_ENTRIES</span> (slash_cmds.py) lists '
                     '/update, /autorun, /morphling, /goal, /hive, /conductor, /scheduler. Except /scheduler, each is '
                     'mapped by <span class="inline">prompt_for(cmd, args)</span> to a '
                     '<span class="inline">build_*_prompt</span> function that returns a system-style prompt, '
                     '<strong>injected as user input</strong> into the same agent loop — the command itself holds no '
                     'business logic.') + '</p>')
            + c.qa(t, '🧪 build_autorun_prompt 长什么样', 'What build_autorun_prompt looks like',
                   '<p>' + t(
                       '以 /autorun 为例，它注入的提示词只是“让 Agent 先读一个 SOP，再自驱执行”：',
                       'Take /autorun: the prompt it injects just tells the agent to read an SOP first, then self-run:') + '</p>'
                   + c.codefile('frontends/slash_cmds.py', 'build_autorun_prompt',
                       t('请进入「自主探索 / autonomous 模式」：先读 '
                         'memory/autonomous_operation_sop.md。全程自驱，不可逆 / 高风险动作先 ask_user，'
                         '结案给一份简明回执（做了什么 / 产物在哪 / 下一步）。',
                         'Enter "autonomous mode": first read memory/autonomous_operation_sop.md. Self-drive '
                         'throughout; for irreversible / high-risk actions call ask_user first; on finishing, give a '
                         'concise receipt (what was done / where artifacts are / next step).'))
                   + '<p>' + t(
                       '/goal、/hive、/morphling 同理，各自指向 '
                       '<span class="inline">goal_mode_sop.md</span> / '
                       '<span class="inline">goal_hive_sop.md</span> / '
                       '<span class="inline">morphling_sop.md</span>。',
                       '/goal, /hive, /morphling are analogous, each pointing to '
                       '<span class="inline">goal_mode_sop.md</span> / '
                       '<span class="inline">goal_hive_sop.md</span> / '
                       '<span class="inline">morphling_sop.md</span>.') + '</p>')
            + c.qa(t, '🔀 /scheduler 与 /update 的两个例外味道', 'How /scheduler and /update differ',
                   '<p>' + t(
                       '<span class="inline">/scheduler</span> 是<strong>唯一不注入提示词</strong>的命令：它直接读写 '
                       '<span class="inline">sche_tasks/*.json</span> 与既有 scheduler 守护进程，无需 LLM。'
                       '<span class="inline">/update</span> 仍是提示词注入，但它写的是一段“先预览上游提交、'
                       '再保留本地改动地 git pull”的精细编排——真正的 git 工作仍由 Agent 在循环里完成。',
                       '<span class="inline">/scheduler</span> is the <strong>only</strong> command that injects no '
                       'prompt: it reads/writes <span class="inline">sche_tasks/*.json</span> and the existing '
                       'scheduler daemon directly, no LLM. <span class="inline">/update</span> is still a prompt '
                       'injection, but one that orchestrates "preview upstream commits, then git pull while '
                       'preserving local changes" — the actual git work still happens in the agent loop.') + '</p>')
            + c.qa(t, '❓ 为什么这样设计', 'Why design it this way',
                   '<p>' + t(
                       '因为模式即提示词：加一个新模式，往往只是加一个 '
                       '<span class="inline">build_*_prompt</span> 函数与一行 PALETTE_ENTRIES，'
                       '不必改内核。命令只是“触发器”，行为长在 Agent 读到的提示词里——这与“工具少、靠提示词组织行为”的整体哲学一致。',
                       'Because a mode is a prompt: adding a new mode is often just adding a '
                       '<span class="inline">build_*_prompt</span> function plus one PALETTE_ENTRIES row, with no core '
                       'change. The command is only a "trigger"; behavior lives in the prompt the agent reads — '
                       'consistent with the overall philosophy of "few tools, behavior organized by prompts".') + '</p>'))

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

        + c.deepdive_heading(t)
        + c.accordion(t, 1, 'code_run：九个工具里的“元工具”',
            'code_run: the "meta-tool" among the nine',
            c.qa(t, '🧪 script 参数 vs 回复代码块', 'script param vs reply code block',
                 '<p>' + t(
                     'tools_schema.json 写得很清楚：code_run “Prefer python. Multi-call OK, use script param. '
                     'Reply code block is executed if no script arg”。也就是说——<strong>单次</strong>调用建议把代码'
                     '直接放在回复的 ```代码块```（省去字符串转义），<strong>多次</strong>并发调用才用 '
                     '<span class="inline">script</span> 参数。两者互斥。',
                     'tools_schema.json says it plainly: code_run "Prefer python. Multi-call OK, use script param. '
                     'Reply code block is executed if no script arg". That is — for a <strong>single</strong> call, '
                     'put code in a reply ```code block``` (no string escaping); use the '
                     '<span class="inline">script</span> param only for <strong>multiple</strong> concurrent calls. '
                     'The two are mutually exclusive.') + '</p>')
            + c.qa(t, '⚙️ do_code_run 内部', 'Inside do_code_run',
                   '<p>' + t(
                       '<span class="inline">ga.py: do_code_run</span> 先取 '
                       '<span class="inline">args["script"]</span>，没有就用 '
                       '<span class="inline">_extract_code_block(response)</span> 从回复里抠代码块；'
                       '默认 <span class="mono">timeout=60</span>、类型 python。输出有长度上限 '
                       '<span class="mono">maxlen = 10000 // _tool_num</span>（按本轮工具数均分），'
                       '所以 schema 才强调“No hardcoding bulk data”——大数据要落文件读，别塞进代码。',
                       '<span class="inline">ga.py: do_code_run</span> first reads '
                       '<span class="inline">args["script"]</span>, else extracts a code block from the reply via '
                       '<span class="inline">_extract_code_block(response)</span>; defaults to '
                       '<span class="mono">timeout=60</span>, type python. Output is capped at '
                       '<span class="mono">maxlen = 10000 // _tool_num</span> (split across this turn\'s tools), '
                       'which is why the schema stresses "No hardcoding bulk data" — read bulk data from files, do '
                       'not stuff it into code.') + '</p>')
            + c.qa(t, '❓ 为什么它是“元工具”', 'Why it is the "meta-tool"',
                   '<p>' + t(
                       '因为它能执行<strong>任意代码</strong>：运行时装包、调外部 API、写新脚本，'
                       '甚至把一段临时能力固化成永久技能。正是这一个工具，把“只有九件工具”的极简框架变成能'
                       '<strong>自我生长</strong>的系统——其余八个工具都是“感知 / 落盘 / 记忆”的边界，code_run 是“行动”的核心。',
                       'Because it runs <strong>arbitrary code</strong>: install packages, call external APIs, write '
                       'new scripts, even crystallize a temporary capability into a permanent skill at runtime. This '
                       'single tool turns a "only nine tools" framework into a <strong>self-growing</strong> system — '
                       'the other eight are the "perceive / persist / remember" boundary, and code_run is the core of '
                       '"act".') + '</p>'))
        + c.accordion(t, 2, 'file_patch：唯一精确匹配，与它的坑',
            'file_patch: unique exact match, and its gotcha',
            c.qa(t, '🧪 唯一精确匹配规则', 'The unique-exact-match rule',
                 '<p>' + t(
                     'file_patch 的契约是“Replace <strong>unique</strong> old_content with new_content. '
                     '<strong>Exact match</strong> required (whitespace/indentation)”。'
                     '<span class="inline">old_content</span> 必须在文件里<strong>唯一且逐字符（含缩进/空白）匹配</strong>，'
                     '否则拒绝替换——这逼模型先精确读、再精确改。',
                     'file_patch\'s contract is "Replace <strong>unique</strong> old_content with new_content. '
                     '<strong>Exact match</strong> required (whitespace/indentation)". '
                     '<span class="inline">old_content</span> must match <strong>uniquely and byte-for-byte (including '
                     'indentation/whitespace)</strong>, or the replace is rejected — forcing the model to read '
                     'precisely before editing precisely.') + '</p>')
            + c.qa(t, '⚠️ 匹配失败怎么办', 'What to do on a failed match',
                   '<p>' + t(
                       'schema 直接给了药方：“On failure, file_read to recheck”。匹配不到通常是因为上下文不够独特、'
                       '或空白/缩进对不上。正确做法是先 <span class="inline">file_read</span> 拿到最新内容与行号'
                       '（schema：“Read before modify for latest context and line numbers”），再扩大 old_content '
                       '让它唯一。',
                       'The schema prescribes the cure: "On failure, file_read to recheck". A miss usually means the '
                       'context is not unique, or whitespace/indentation differs. The fix is to '
                       '<span class="inline">file_read</span> for the latest content and line numbers (schema: "Read '
                       'before modify for latest context and line numbers"), then widen old_content until it is '
                       'unique.') + '</p>')
            + c.qa(t, '🔀 file_patch vs file_write', 'file_patch vs file_write',
                   '<table class="t"><tr><th></th><th>file_patch</th><th>file_write</th></tr>'
                   + '<tr><td>' + t('用途', 'Use') + '</td><td>' + t('精细局部替换', 'fine local replace')
                   + '</td><td>' + t('大段创建/覆盖/追加', 'large create/overwrite/append') + '</td></tr>'
                   + '<tr><td>' + t('schema 说', 'schema says') + '</td><td>' + t('唯一精确匹配', 'unique exact match')
                   + '</td><td class="mono">HUGE edits ONLY</td></tr>'
                   + '<tr><td>' + t('特性', 'Feature') + '</td><td>'
                   + t('new_content 支持 {{file:..}} 引用', 'new_content supports {{file:..}} refs') + '</td><td>'
                   + t('支持 {{file:path:start:end}} 自动展开', 'supports {{file:path:start:end}} auto-expand') + '</td></tr></table>'
                   + '<p>' + t(
                       '默认改文件用 file_patch；只有整文件大改才动 file_write——这正是 part1 lesson_01 强调的“最小改动”原则在工具层的体现。',
                       'Default to file_patch for edits; reach for file_write only for whole-file rewrites — the '
                       'tool-level echo of the "minimal change" principle stressed in part1 lesson_01.') + '</p>'))
        + c.accordion(t, 3, 'web_scan 与 web_execute_js：优先执行 JS，少扫',
            'web_scan and web_execute_js: prefer execute_js, scan sparingly',
            c.qa(t, '⚙️ 两个工具的参数', 'Params of the two tools',
                 '<table class="t"><tr><th>' + t('工具', 'Tool') + '</th><th>'
                 + t('关键参数', 'Key params') + '</th></tr>'
                 + '<tr><td class="mono">web_scan</td><td class="mono">tabs_only, switch_tab_id, text_only</td></tr>'
                 + '<tr><td class="mono">web_execute_js</td><td class="mono">script, save_to_file, no_monitor, switch_tab_id</td></tr></table>'
                 + '<p>' + t(
                     'web_scan 返回<strong>简化后</strong>的 HTML 与标签页列表（do_web_scan 默认 '
                     '<span class="mono">maxlen=35000//_tool_num</span>），并会移除隐藏/浮动/被遮挡元素；'
                     'web_execute_js 在真实浏览器里跑 JS，可用 '
                     '<span class="inline">save_to_file</span> 把长结果落盘、'
                     '<span class="inline">no_monitor</span> 跳过页面变化监控省 2–3 秒（仅限只读）。',
                     'web_scan returns <strong>simplified</strong> HTML plus the tab list (do_web_scan defaults to '
                     '<span class="mono">maxlen=35000//_tool_num</span>) and strips hidden/floating/covered elements; '
                     'web_execute_js runs JS in a real browser, can dump long results via '
                     '<span class="inline">save_to_file</span> and skip change-monitoring with '
                     '<span class="inline">no_monitor</span> to save 2–3s (reads only).') + '</p>')
            + c.qa(t, '❓ 为什么“优先 execute_js，少 scan”', 'Why "prefer execute_js, scan sparingly"',
                   '<p>' + t(
                       'tools_schema.json 在 web_execute_js 上写着“Act accurately to reduce web_scan calls”，'
                       '在 web_scan 上注明 HTML 已被简化、边栏/浮动元素可能被滤掉。原因有二：scan 返回的简化 HTML '
                       '<strong>体积大、还可能漏内容</strong>；而 execute_js 能<strong>精确</strong>读取/操作 DOM，'
                       '一步到位，既省 token 又更可靠。所以 scan 用来“感知一次”，execute_js 用来“反复操作”。',
                       'tools_schema.json says on web_execute_js "Act accurately to reduce web_scan calls", and notes '
                       'on web_scan that its HTML is simplified and sidebars/floating elements may be filtered out. '
                       'Two reasons: scan\'s simplified HTML is <strong>large and may drop content</strong>, while '
                       'execute_js reads/drives the DOM <strong>precisely</strong> in one shot — saving tokens and '
                       'being more reliable. So scan is for "perceive once", execute_js for "act repeatedly".') + '</p>')
            + c.qa(t, '⚠️ do_web_execute_js 的取码与落盘', 'Code source and save in do_web_execute_js',
                   '<p>' + t(
                       '与 code_run 同构：<span class="inline">do_web_execute_js</span> 先取 '
                       '<span class="inline">args["script"]</span>，没有就抠 ```javascript``` 块；'
                       '若 script 是一个存在的文件路径，会读文件内容当脚本。给了 '
                       '<span class="inline">save_to_file</span> 且有 js_return 时，完整结果写盘、'
                       '回包里只留截断预览——避免长结果撑爆上下文。',
                       'Isomorphic to code_run: <span class="inline">do_web_execute_js</span> reads '
                       '<span class="inline">args["script"]</span>, else extracts a ```javascript``` block; if script '
                       'is an existing file path it loads that file as the script. When '
                       '<span class="inline">save_to_file</span> is set and js_return exists, the full result is '
                       'written to disk and only a truncated preview is returned — keeping long results from blowing '
                       'up the context.') + '</p>'))
        + c.accordion(t, 4, 'update_working_checkpoint：每轮自动注入的工作便签',
            'update_working_checkpoint: the auto-injected working notepad',
            c.qa(t, '⚙️ “每轮自动注入”是什么意思', 'What "auto-injected each turn" means',
                 '<p>' + t(
                     '<span class="inline">do_update_working_checkpoint</span> 把 '
                     '<span class="inline">key_info</span> / <span class="inline">related_sop</span> 写进 '
                     '<span class="inline">self.working</span>，并清零 passed_sessions。'
                     '之后每一轮，<span class="inline">_get_anchor_prompt()</span> 会把这张便签连同近 30 条 '
                     '<span class="mono">[WORKING MEMORY]</span> 历史一起拼进下一条 prompt——'
                     '即使上下文被压缩，关键约束也不丢。',
                     '<span class="inline">do_update_working_checkpoint</span> writes '
                     '<span class="inline">key_info</span> / <span class="inline">related_sop</span> into '
                     '<span class="inline">self.working</span> and resets passed_sessions. Thereafter every turn, '
                     '<span class="inline">_get_anchor_prompt()</span> stitches this notepad plus the recent '
                     '<span class="mono">[WORKING MEMORY]</span> history into the next prompt — so key constraints '
                     'survive even when context is compacted.') + '</p>')
            + c.qa(t, '🧪 何时该调 / 不该调', 'When to call / not call',
                   '<p>' + t(
                       'schema 列出四个时机：(1) 读完 SOP 后存下用户需求与关键约束；(2) 切换子任务或上下文将被刷新前；'
                       '(3) 反复失败后，重读 SOP 并存下新发现；(4) 新任务开始时更新内容、清空旧进度但保留有效约束。'
                       '<strong>不要</strong>在简单 1–2 步任务、或任务已完成时调用——后者该用长期记忆工具。',
                       'The schema lists four moments: (1) after reading an SOP, store user needs and key '
                       'constraints; (2) before switching subtasks or a context flush; (3) after repeated failures, '
                       're-read the SOP and store new findings; (4) on a new task, update content and clear old '
                       'progress while keeping valid constraints. <strong>Do not</strong> call it for simple 1–2 step '
                       'tasks, or once a task is complete — that is the long-term memory tool\'s job.') + '</p>')
            + c.qa(t, '⚠️ key_info 是“替换”不是“追加”', 'key_info replaces, not appends',
                   '<p>' + t(
                       'schema 强调 key_info “<strong>Replaces</strong> current notepad (&lt;200 tokens)”，'
                       '要做<strong>增量式</strong>更新：先回看现有内容，保留仍有效的，再增/删/改。'
                       '便签很小（&lt;200 token），所以只记坑点、用户硬性要求、关键参数/发现，不要写流水账。',
                       'The schema stresses key_info "<strong>Replaces</strong> current notepad (&lt;200 tokens)" and '
                       'should be updated <strong>incrementally</strong>: review what is there, keep what still '
                       'holds, then add/remove/modify. The notepad is tiny (&lt;200 tokens), so record only '
                       'pitfalls, hard user requirements, and key params/findings — not a running log.') + '</p>'))
        + c.accordion(t, 5, 'start_long_term_update：跑完大任务后的“结算”',
            'start_long_term_update: "settling up" after a big task',
            c.qa(t, '⚙️ 它触发的是一段结算流程', 'It triggers a settlement flow',
                 '<p>' + t(
                     '<span class="inline">do_start_long_term_update</span> 不直接写记忆，而是<strong>开启结算</strong>：'
                     '它注入一段“提炼经验”的提示词 + L0 记忆管理 SOP（'
                     '<span class="inline">memory/memory_management_sop.md</span>），让 Agent 自己按 SOP '
                     '把<strong>验证成功且长期有效</strong>的环境事实 / 用户偏好 / 关键步骤，用 file_patch 最小化地写进 L2 / L3。',
                     '<span class="inline">do_start_long_term_update</span> does not write memory directly; it '
                     '<strong>opens a settlement</strong>: it injects a "distill lessons" prompt plus the L0 memory '
                     'management SOP (<span class="inline">memory/memory_management_sop.md</span>), letting the agent '
                     'follow that SOP to write <strong>verified, long-lived</strong> environment facts / user prefs / '
                     'key steps into L2 / L3 with minimal file_patch edits.') + '</p>')
            + c.qa(t, '🧪 何时必须调用', 'When you must call it',
                   '<p>' + t(
                       'schema 明确：“Must call when a task that took <strong>15+ turns</strong> is completed”。'
                       '其余时候是“发现值得记的环境事实 / 用户偏好 / 教训”时调用；'
                       '若记忆已更新、或处于 autonomous 流程中，则跳过。',
                       'The schema is explicit: "Must call when a task that took <strong>15+ turns</strong> is '
                       'completed". Otherwise call it when you discover environment facts / user prefs / lessons worth '
                       'remembering; skip if memory is already updated or you are inside an autonomous flow.') + '</p>')
            + c.qa(t, '❓ 记什么、不记什么', 'What to record, what not to',
                   '<p>' + t(
                       '注入的提示词划了红线：<strong>只记行动验证成功</strong>的信息——环境事实（路径/凭证/配置）、'
                       '复杂任务的关键坑点/前置条件/重要步骤。<strong>禁止</strong>记临时变量、具体推理过程、'
                       '未验证信息、通用常识、能轻松复现的细节。这正呼应 part1 的“自进化”：经验沉淀成 L3 的 *_sop.md，'
                       '同类任务越做越快。',
                       'The injected prompt draws a red line: <strong>record only action-verified</strong> info — '
                       'environment facts (paths/credentials/config) and a complex task\'s key pitfalls/preconditions/'
                       'steps. <strong>Forbidden</strong>: temporary variables, detailed reasoning, unverified info, '
                       'general knowledge, easily reproducible details. This echoes part1\'s "self-evolution": '
                       'experience crystallizes into L3 *_sop.md, so similar tasks get faster over time.') + '</p>'))

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
