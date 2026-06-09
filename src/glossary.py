"""Part 6 — 速查 / Reference (lesson 23): glossary + source-file index.

``lesson_23(t)`` is a reference page, not a 5-card tutorial, so it is exempt
from ``test_completed_lessons_follow_card_format``. Term and file rows link to
the lesson that covers them (sibling .html files; links validated by
check_links). ``t('中文', 'English')`` wraps every piece of prose.
"""


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
