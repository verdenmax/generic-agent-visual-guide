"""Part 3 — 内部源码 / Inside the Source (lessons 08–14).

Each lesson is a ``lesson(t)`` function. ``t('中文', 'English')`` wraps every
piece of prose; structure, diagrams and code are written once and shared by
both language renders. All technical claims are grounded in the real
GenericAgent source (agent_loop.py, llmcore.py, ga.py, plugins/, memory/).

Authoring conventions are documented at the top of ``part1.py`` — follow the
same 5-card lesson format (🌍 macro / 🔬 detail / 🧩 analogy / ✅ key /
💡 spark) and the ``.inline`` (prose code) vs ``.mono`` (dense components) rule.
"""


def lesson_08(t):
    """Agent Loop 核心拆解 / The Agent Loop."""
    return (
        '<p class="lead">'
        + t(
            '整个 GenericAgent 的“心跳”就是一个约 100 行的循环——'
            '<span class="inline">agent_loop.py: agent_runner_loop</span>。'
            '它不断地：把消息交给大模型 → 看模型想调哪个工具 → 执行 → 把结果带进下一轮 → 再来一遍，'
            '直到任务完成或退出。读懂这一个函数，就读懂了 GA 的运行方式。',
            'The "heartbeat" of all of GenericAgent is one ~100-line loop — '
            '<span class="inline">agent_loop.py: agent_runner_loop</span>. '
            'It repeatedly: hands messages to the LLM → sees which tool the model wants → runs it → '
            'carries the result into the next round → and goes again, until the task is done or it exits. '
            'Understand this single function and you understand how GA runs.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '很多 Agent 框架把“循环”做得很复杂。GenericAgent 反过来：循环极简，复杂性都推给了大模型和工具。'
            '它的循环是<strong>逐轮（turn）</strong>推进的——每一轮就是“一次模型调用 + 若干次工具执行”，'
            '最多跑 <span class="inline">max_turns</span> 轮（默认 40）。',
            'Many agent frameworks make the "loop" elaborate. GenericAgent does the opposite: the loop is '
            'tiny and pushes complexity onto the model and the tools. It advances <strong>turn by '
            'turn</strong> — one turn is "one model call + zero or more tool runs" — for at most '
            '<span class="inline">max_turns</span> turns (default 40).',
        )
        + '</p></div>'

        + '<h2>' + t('一轮里发生了什么', 'What happens in one turn') + '</h2>'
        + '<div class="vflow">'
        + '<div class="step"><div class="num">1</div><div class="sc"><h4>'
        + t('调用模型', 'Call the model') + '</h4><p>'
        + t('把当前 messages 与工具 schema 交给 ', 'Hand the current messages and tools schema to ')
        + '<span class="mono">client.chat(messages, tools)</span>'
        + t('，流式拿到回复。', ' and stream back the reply.') + '</p></div></div>'
        + '<div class="step"><div class="num">2</div><div class="sc"><h4>'
        + t('解析工具调用', 'Parse tool calls') + '</h4><p>'
        + t('从 ', 'Read ') + '<span class="mono">response.tool_calls</span>'
        + t(' 读出模型想调用的工具与参数；一轮可含多个工具。',
            ' for the tools and arguments the model wants; a turn may contain several.') + '</p></div></div>'
        + '<div class="step"><div class="num">3</div><div class="sc"><h4>'
        + t('逐个执行', 'Run them one by one') + '</h4><p>'
        + t('对每个工具调用 ', 'For each call, invoke ') + '<span class="mono">handler.dispatch(...)</span>'
        + t('，得到一个 ', ', yielding a ') + '<span class="mono">StepOutcome</span>'
        + t('。', '.') + '</p></div></div>'
        + '<div class="step"><div class="num">4</div><div class="sc"><h4>'
        + t('决定下一步', 'Decide what is next') + '</h4><p>'
        + t('收集各工具的 next_prompt 与结果；若有工具要求退出或没有 next_prompt，则结束。',
            'Collect each tool\'s next_prompt and results; if a tool asks to exit, or there is no next_prompt, finish.') + '</p></div></div>'
        + '<div class="step"><div class="num">5</div><div class="sc"><h4>'
        + t('组织下一轮消息', 'Build next-turn messages') + '</h4><p>'
        + t('只把“这一轮的新消息 + 工具结果”作为下一轮输入，历史由 Session 保存。',
            'Pass only "this turn\'s new message + tool results" as the next input; history is kept by the Session.') + '</p></div></div>'
        + '</div>'

        + '<div class="codefile"><div class="cf-head"><span class="dot"></span>'
        + '<span class="path">agent_loop.py</span><span class="ln">agent_runner_loop</span></div>'
        + '<pre>'
        + '<span class="kw">while</span> turn &lt; handler.max_turns:\n'
        + '    turn += <span class="nb">1</span>\n'
        + '    <span class="cm"># ' + t('每 10 轮重置一次工具描述，省 token', 'reset tool descriptions every 10 turns to save tokens') + '</span>\n'
        + '    <span class="kw">if</span> turn % <span class="nb">10</span> == <span class="nb">0</span>: client.last_tools = <span class="st">\'\'</span>\n'
        + '    response = <span class="kw">yield from</span> client.chat(messages, tools_schema)\n'
        + '    tool_calls = [...]  <span class="cm"># ' + t('来自 response.tool_calls', 'from response.tool_calls') + '</span>\n'
        + '    <span class="kw">for</span> tc <span class="kw">in</span> tool_calls:\n'
        + '        outcome = <span class="kw">yield from</span> handler.dispatch(tc.name, tc.args, response)\n'
        + '        <span class="kw">if</span> outcome.should_exit: ...\n'
        + '        <span class="kw">if</span> <span class="kw">not</span> outcome.next_prompt: ...  <span class="cm"># ' + t('任务完成', 'task done') + '</span>\n'
        + '    <span class="cm"># ' + t('只带新消息进下一轮，历史在 Session 里', 'only the new message goes to the next turn; history lives in the Session') + '</span>\n'
        + '    messages = [{<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: next_prompt, <span class="st">"tool_results"</span>: tool_results}]\n'
        + '</pre></div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('入口函数 ', 'The entry function ')
        + '<span class="inline">agent_runner_loop(client, system_prompt, user_input, handler, tools_schema, max_turns=40, ...)</span>'
        + t('，初始 messages 为 [system, user] 两条。',
            ' starts messages as two entries [system, user].') + '</li>'
        + '<li>' + t('每个工具返回一个 ', 'Each tool returns a ')
        + '<span class="inline">StepOutcome(data, next_prompt, should_exit)</span>'
        + t('（dataclass）：data 是给模型看的结果，next_prompt 是下一轮提示，should_exit 表示主动退出。',
            ' (a dataclass): data is the result shown to the model, next_prompt is the next-turn prompt, should_exit means exit on purpose.') + '</li>'
        + '<li>' + t('三种结束：某工具 should_exit → ', 'Three endings: a tool sets should_exit → ')
        + '<span class="inline">EXITED</span>'
        + t('；没有 next_prompt → ', '; no next_prompt → ')
        + '<span class="inline">CURRENT_TASK_DONE</span>'
        + t('；轮数耗尽 → ', '; turns exhausted → ')
        + '<span class="inline">MAX_TURNS_EXCEEDED</span>' + t('。', '.') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像一个照着固定节奏干活的工人：<strong>看一眼现场 → 想该做什么 → 动手做 → 记一笔 → 再看一眼</strong>。'
            '工人本身的“流程”很死板、很短，但因为每一步“想该做什么”交给了聪明的大脑（大模型），'
            '所以这套简单循环能完成非常复杂的任务。',
            'Like a worker following a fixed rhythm: <strong>glance at the scene → think what to do → do it → '
            'jot a note → glance again</strong>. The worker\'s own "procedure" is rigid and short, but because '
            'the "think what to do" step is delegated to a smart brain (the LLM), this simple loop can finish '
            'very complex tasks.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('核心就一个函数 agent_runner_loop，约 100 行，逐轮推进，默认最多 40 轮。',
            'The core is one function, agent_runner_loop (~100 lines), advancing turn by turn, up to 40 turns by default.') + '</li>'
        + '<li>' + t('每轮 = 一次模型调用 + 若干次工具执行；工具返回 StepOutcome。',
            'Each turn = one model call + some tool runs; tools return a StepOutcome.') + '</li>'
        + '<li>' + t('下一轮只带新消息，历史由 Session 维护。',
            'The next turn carries only the new message; the Session maintains history.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '最妙的一行是 <span class="inline">messages = [ 新消息 ]</span>：循环<strong>不把历史塞进 messages</strong>，'
            '每轮只递“这一轮新增的内容”，历史交给 Session 单独管理。这让循环本身几乎无状态、极易理解，'
            '也为后面“把上下文压到 &lt;30K”的 token 效率埋下伏笔——少即是多，从这一行开始。',
            'The cleverest line is <span class="inline">messages = [ new message ]</span>: the loop '
            '<strong>does not stuff history into messages</strong>; each turn passes only "what is new this '
            'turn", leaving history to the Session. This keeps the loop almost stateless and easy to grasp, and '
            'it sets up the later "keep context under 30K" token efficiency — less is more, starting from this '
            'one line.',
        )
        + '</div>'
    )


def lesson_09(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_10(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_11(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_12(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_13(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_14(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'
