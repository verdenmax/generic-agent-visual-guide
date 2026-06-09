"""Part 6 — 速查 / Reference (lesson 23): glossary + source-file index.

``lesson_23(t)`` is a reference page, not a 5-card tutorial, so it is exempt
from ``test_completed_lessons_follow_card_format``. Term and file rows link to
the lesson that covers them (sibling .html files; links validated by
check_links). ``t('中文', 'English')`` wraps every piece of prose.
"""

import components as c



def _term(t, term, zh, en, href, lesson_label):
    """One glossary row: term · bilingual one-liner · link to its lesson."""
    return (
        '<tr><td class="mono">' + term + '</td><td>' + t(zh, en) + '</td>'
        '<td><a href="' + href + '">' + t('第 ', 'L') + lesson_label + t(' 课', '') + '</a></td></tr>'
    )


def lesson_23(t):
    """术语表 + 源文件索引 / Glossary & Source Index."""
    return (
        '<p class="lead">'
        + t(
            '全书的术语速查与源码地图都在这里。每个词条配一句话解释，并链到讲它的那一课；每个核心源文件也标注了职责'
            '与对应课程。看完前面的课，这一页就是你<strong>随时回查</strong>的索引。',
            'The whole guide\'s term lookup and source map live here. Each entry has a one-line explanation and links '
            'to the lesson that covers it; each core source file is annotated with its responsibility and lesson. After '
            'the earlier lessons, this page is your <strong>quick-reference</strong> index.',
        )
        + '</p>'

        + '<h2>' + t('学习路径 / Reading paths', 'Reading paths') + '</h2>'
        + '<div class="cols">'
        + '<div class="col"><h4>' + t('🚀 快速上手', '🚀 Get going') + '</h4><p>'
        + t('只想先用起来：', 'Just want to use it: ')
        + '<a href="01-what-is-ga.html">01</a> → <a href="04-install.html">04</a> → '
        + '<a href="05-frontends.html">05</a> → <a href="06-commands.html">06</a> → '
        + '<a href="07-tools.html">07</a></p></div>'
        + '<div class="col"><h4>' + t('🔬 懂原理', '🔬 Understand internals') + '</h4><p>'
        + t('想读懂源码：', 'Want to read the source: ')
        + '<a href="08-agent-loop.html">08</a> → <a href="09-llmcore.html">09</a> → '
        + '<a href="10-handler-dispatch.html">10</a> → <a href="11-layered-memory.html">11</a> → '
        + '<a href="12-memory-crystallize.html">12</a> → <a href="13-hooks-observability.html">13</a> → '
        + '<a href="14-context-tokens.html">14</a></p></div>'
        + '<div class="col"><h4>' + t('🧬 进阶玩法', '🧬 Go further') + '</h4><p>'
        + t('想玩到底：', 'Want the deep end: ')
        + '<a href="15-vision.html">15</a> → <a href="16-input-mobile.html">16</a> → '
        + '<a href="17-browser.html">17</a> → <a href="18-reflect-orchestration.html">18</a> → '
        + '<a href="19-autonomy.html">19</a> → <a href="20-self-evolution.html">20</a> → '
        + '<a href="21-build-a-skill.html">21</a> → <a href="22-extend-frontend.html">22</a></p></div>'
        + '</div>'

        + '<h2>' + t('术语表', 'Glossary') + '</h2>'

        + '<h3>' + t('核心概念', 'Core concepts') + '</h3>'
        + '<table class="t">'
        + '<tr><th>' + t('术语', 'Term') + '</th><th>' + t('一句话解释', 'One-line meaning') + '</th>'
        + '<th>' + t('对应课', 'Lesson') + '</th></tr>'
        + _term(t, 'agent_runner_loop',
                '约 100 行的自主执行循环，GA 的“心跳”。', 'The ~100-line autonomous loop, GA\'s "heartbeat".',
                '08-agent-loop.html', '08')
        + _term(t, 'StepOutcome',
                '工具返回的结果三元组：data / next_prompt / should_exit。',
                'A tool\'s result triple: data / next_prompt / should_exit.',
                '08-agent-loop.html', '08')
        + _term(t, 'turn',
                '一轮 = 一次模型调用 + 若干次工具执行。', 'A turn = one model call + some tool runs.',
                '08-agent-loop.html', '08')
        + _term(t, 'ToolClient / NativeToolClient',
                'llmcore 的两种客户端：纯文本协议 vs 原生函数调用。',
                'llmcore\'s two clients: text protocol vs native function calling.',
                '09-llmcore.html', '09')
        + _term(t, 'dispatch / do_&lt;tool&gt;',
                '按工具名调用 do_&lt;tool&gt; 方法的调度机制。',
                'Dispatch that calls the do_&lt;tool&gt; method by tool name.',
                '10-handler-dispatch.html', '10')
        + '</table>'

        + '<h3>' + t('工具与能力', 'Tools & capabilities') + '</h3>'
        + '<table class="t">'
        + '<tr><th>' + t('术语', 'Term') + '</th><th>' + t('一句话解释', 'One-line meaning') + '</th>'
        + '<th>' + t('对应课', 'Lesson') + '</th></tr>'
        + _term(t, 'code_run',
                '执行任意代码的“元工具”，自进化的发动机。', 'The "meta-tool" that runs any code; the engine of self-evolution.',
                '07-tools.html', '07')
        + _term(t, 'file_read / write / patch',
                '读 / 写 / 精确修改文件。', 'Read / write / precisely patch files.',
                '07-tools.html', '07')
        + _term(t, 'web_scan / web_execute_js',
                '看简化网页 / 在真实浏览器执行 JS。', 'Read a simplified page / run JS in the real browser.',
                '17-browser.html', '17')
        + _term(t, 'ask_user',
                '遇到决策或卡死时打断任务问用户。', 'Interrupt to ask the user on decisions or blockers.',
                '07-tools.html', '07')
        + _term(t, t('视觉 (ui_detect / OCR)', 'Vision (ui_detect / OCR)'),
                '截屏 → YOLO+OCR 检测 → 物理坐标 → 操作。', 'Screenshot → YOLO+OCR detect → physical coords → act.',
                '15-vision.html', '15')
        + _term(t, 'ljqCtrl / ADB',
                '桌面鼠标键盘 / 安卓设备控制。', 'Desktop mouse-keyboard / Android device control.',
                '16-input-mobile.html', '16')
        + _term(t, 'TMWebDriver / simphtml',
                '真实浏览器注入桥 / 网页 token 化简化。', 'Real-browser injection bridge / page token-simplification.',
                '17-browser.html', '17')
        + '</table>'

        + '<h3>' + t('记忆与进化', 'Memory & evolution') + '</h3>'
        + '<table class="t">'
        + '<tr><th>' + t('术语', 'Term') + '</th><th>' + t('一句话解释', 'One-line meaning') + '</th>'
        + '<th>' + t('对应课', 'Lesson') + '</th></tr>'
        + _term(t, t('分层记忆 L0–L4', 'Layered memory L0–L4'),
                '铁律 / 索引 / 事实 / 技能SOP / 会话归档。', 'Rules / index / facts / skill SOPs / session archive.',
                '11-layered-memory.html', '11')
        + _term(t, 'update_working_checkpoint',
                '短期工作便签，每轮自动注入。', 'Short-term notepad, auto-injected each turn.',
                '12-memory-crystallize.html', '12')
        + _term(t, 'start_long_term_update',
                '把验证成功的经验结晶进长期记忆。', 'Crystallize verified experience into long-term memory.',
                '12-memory-crystallize.html', '12')
        + _term(t, t('钩子 hooks', 'hooks'),
                '循环关键点的发布/订阅事件，零耦合扩展。', 'Pub/sub events at loop key points; zero-coupling extension.',
                '13-hooks-observability.html', '13')
        + _term(t, t('Token 效率', 'Token efficiency'),
                '把上下文压到 &lt;30K：只留当下需要的。', 'Keep context under 30K: keep only what is needed now.',
                '14-context-tokens.html', '14')
        + _term(t, t('reflect / 编排', 'reflect / orchestration'),
                '循环之外的定时探针：goal / scheduler / hive…。', 'Periodic probes outside the loop: goal / scheduler / hive…',
                '18-reflect-orchestration.html', '18')
        + _term(t, t('Skill / 自进化', 'Skill / self-evolution'),
                '把成功路径结晶成可复用技能，越用越强。', 'Crystallize a success path into a reusable skill; stronger with use.',
                '20-self-evolution.html', '20')
        + _term(t, 'Morphling / Incubator',
                '吸收外部项目能力 / 自我复制部署到其他节点。', 'Absorb external project abilities / self-replicate to other nodes.',
                '20-self-evolution.html', '20')
        + '</table>'

        + '<h2>' + t('核心源文件索引', 'Core source-file index') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('文件 / 目录', 'File / Dir') + '</th><th>' + t('职责', 'Responsibility') + '</th>'
        + '<th>' + t('对应课', 'Lesson') + '</th></tr>'
        + '<tr><td class="mono">agent_loop.py</td><td>'
        + t('自主执行循环、BaseHandler、StepOutcome、上下文清洗。',
            'The autonomous loop, BaseHandler, StepOutcome, context cleaning.')
        + '</td><td><a href="08-agent-loop.html">08</a> · <a href="14-context-tokens.html">14</a></td></tr>'
        + '<tr><td class="mono">llmcore.py</td><td>'
        + t('LLM 内核：统一 chat、多协议适配、流式、历史压缩。',
            'The LLM core: unified chat, multi-protocol adaptation, streaming, history compression.')
        + '</td><td><a href="09-llmcore.html">09</a></td></tr>'
        + '<tr><td class="mono">agentmain.py</td><td>'
        + t('装配接线：加载 schema / system prompt，启动循环与 reflect。',
            'Assembly & wiring: load schema / system prompt, start the loop and reflect.')
        + '</td><td><a href="03-task-lifecycle.html">03</a> · <a href="18-reflect-orchestration.html">18</a></td></tr>'
        + '<tr><td class="mono">ga.py</td><td>'
        + t('GenericAgentHandler：9 个原子工具的 do_* 实现。',
            'GenericAgentHandler: the do_* implementations of the 9 atomic tools.')
        + '</td><td><a href="07-tools.html">07</a> · <a href="10-handler-dispatch.html">10</a></td></tr>'
        + '<tr><td class="mono">simphtml.py</td><td>'
        + t('网页 HTML 简化 / token 优化，供 web 工具使用。',
            'Web HTML simplification / token optimization for the web tools.')
        + '</td><td><a href="17-browser.html">17</a></td></tr>'
        + '<tr><td class="mono">TMWebDriver.py</td><td>'
        + t('WebSocket 桥，注入真实浏览器执行 JS。',
            'A WebSocket bridge injecting the real browser to run JS.')
        + '</td><td><a href="17-browser.html">17</a></td></tr>'
        + '<tr><td class="mono">memory/</td><td>'
        + t('分层记忆 L0–L4 与可复用 SOP（技能库）。',
            'Layered memory L0–L4 and reusable SOPs (the skill library).')
        + '</td><td><a href="11-layered-memory.html">11</a> · <a href="12-memory-crystallize.html">12</a></td></tr>'
        + '<tr><td class="mono">reflect/</td><td>'
        + t('编排与自治：goal_mode / scheduler / agent_team / autonomous。',
            'Orchestration & autonomy: goal_mode / scheduler / agent_team / autonomous.')
        + '</td><td><a href="18-reflect-orchestration.html">18</a> · <a href="19-autonomy.html">19</a></td></tr>'
        + '<tr><td class="mono">plugins/</td><td>'
        + t('钩子机制与 langfuse 追踪。', 'The hooks mechanism and langfuse tracing.')
        + '</td><td><a href="13-hooks-observability.html">13</a></td></tr>'
        + '<tr><td class="mono">frontends/</td><td>'
        + t('各类界面与 IM 机器人、conductor 编排。',
            'The UIs and IM bots, plus the conductor orchestrator.')
        + '</td><td><a href="05-frontends.html">05</a> · <a href="22-extend-frontend.html">22</a></td></tr>'
        + '</table>'

        + '<h2>' + t('常见疑问 / FAQ', 'FAQ') + '</h2>'
        + c.accordion(t, 1, '为什么核心只有 ~3K 行也能这么强？',
            'How can a ~3K-line core be this capable?',
            c.qa(t, '一句话', 'In one line',
                 '<p>' + t(
                     '复杂度被外包了：推理交给大模型，扩展交给 <span class="inline">code_run</span>（运行时写代码），'
                     '经验交给分层记忆。框架只提供“循环 + 9 工具 + 记忆”的最小骨架。详见 ',
                     'Complexity is outsourced: reasoning to the LLM, extension to <span class="inline">code_run</span> '
                     '(writing code at runtime), experience to layered memory. The framework only provides a minimal '
                     '"loop + 9 tools + memory" skeleton. See ')
                 + '<a href="01-what-is-ga.html">' + t('第 1 课', 'lesson 01') + '</a> '
                 + t('与', 'and') + ' <a href="20-self-evolution.html">' + t('第 20 课', 'lesson 20') + '</a>' + t('。', '.') + '</p>'))
        + c.accordion(t, 2, '它支持哪些大模型？',
            'Which LLMs does it support?',
            c.qa(t, '两种协议', 'Two protocols',
                 '<p>' + t(
                     'GA 原生支持 <strong>OpenAI 兼容</strong>接口与 <strong>Anthropic Claude 原生</strong>接口，'
                     '因此 GPT / Claude / Kimi / MiniMax / DeepSeek / GLM / Qwen / Gemini 等都能在 '
                     '<span class="inline">mykey.py</span> 里配置。连不支持函数调用的模型，也能用文本协议调工具（见 ',
                     'GA natively speaks the <strong>OpenAI-compatible</strong> and <strong>Anthropic Claude native</strong> '
                     'protocols, so GPT / Claude / Kimi / MiniMax / DeepSeek / GLM / Qwen / Gemini and more can be configured '
                     'in <span class="inline">mykey.py</span>. Even models without function calling can use tools via the '
                     'text protocol (see ')
                 + '<a href="09-llmcore.html">' + t('第 9 课', 'lesson 09') + '</a>' + t('）。', ').') + '</p>'))
        + c.accordion(t, 3, '记忆会不会越记越乱？',
            'Won\'t memory get messier over time?',
            c.qa(t, '靠铁律守住', 'Guarded by iron rules',
                 '<p>' + t(
                     '不会。L0 铁律规定“<strong>无行动，不记忆</strong>”——只有经工具调用验证成功的结论才允许写入；'
                     '并禁止存易变状态、要求最小化 patch。所以记忆库是“越用越准”而非“越用越脏”。详见 ',
                     'No. The L0 rules state "<strong>no execution, no memory</strong>" — only conclusions verified by a '
                     'successful tool call may be written; volatile state is banned and patches must be minimal. So the '
                     'store gets "more accurate", not "dirtier". See ')
                 + '<a href="12-memory-crystallize.html">' + t('第 12 课', 'lesson 12') + '</a>' + t('。', '.') + '</p>'))

        + '<div class="card key"><div class="tag">🏁 '
        + t('读完了', 'You made it') + '</div>'
        + '<p>'
        + t(
            '恭喜你走完整套教程！从“GA 是什么”，到循环、工具、记忆、视觉、浏览器、编排，再到自进化与实战——'
            '你已经握有一张完整的 GenericAgent 源码地图。回到 ',
            'Congratulations on finishing the whole guide! From "what is GA", through the loop, tools, memory, vision, '
            'the browser, orchestration, all the way to self-evolution and hands-on — you now hold a complete map of '
            'the GenericAgent source. Head back to the ')
        + '<a href="../index.html">' + t('目录', 'contents') + '</a>'
        + t(' 可随时重温任意一课。', ' to revisit any lesson anytime.')
        + '</p></div>'
    )
