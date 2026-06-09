"""Part 3 — 内部源码 / Inside the Source (lessons 08–14).

Each lesson is a ``lesson(t)`` function. ``t('中文', 'English')`` wraps every
piece of prose; structure, diagrams and code are written once and shared by
both language renders. All technical claims are grounded in the real
GenericAgent source (agent_loop.py, llmcore.py, ga.py, plugins/, memory/).

Authoring conventions are documented at the top of ``part1.py`` — follow the
same 5-card lesson format (🌍 macro / 🔬 detail / 🧩 analogy / ✅ key /
💡 spark) and the ``.inline`` (prose code) vs ``.mono`` (dense components) rule.
"""

import components as c


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

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '逐行读 while 循环：一轮到底发生了什么',
            'Line by line: what one turn of the while loop actually does',
            c.qa(t, '🧪 真实骨架', 'The real skeleton',
                 c.codefile('agent_loop.py', 'agent_runner_loop',
                     '<span class="kw">while</span> turn &lt; handler.max_turns:\n'
                     '    turn += <span class="nb">1</span>\n'
                     '    <span class="kw">if</span> turn%<span class="nb">10</span> == <span class="nb">0</span>: client.last_tools = <span class="st">\'\'</span>  '
                     '<span class="cm"># ' + t('每10轮重置工具描述', 'reset tool desc every 10 turns') + '</span>\n'
                     '    _hook(<span class="st">\'turn_before\'</span>, locals()); _hook(<span class="st">\'llm_before\'</span>, locals())\n'
                     '    response_gen = client.<span class="fn">chat</span>(messages=messages, tools=tools_schema)\n'
                     '    response = <span class="kw">yield from</span> response_gen\n'
                     '    _hook(<span class="st">\'llm_after\'</span>, locals())\n'
                     '    <span class="cm"># ' + t('…解析 tool_calls，逐个 dispatch…', '…parse tool_calls, dispatch each…') + '</span>\n'
                     '    messages = [{<span class="st">\'role\'</span>: <span class="st">\'user\'</span>, '
                     '<span class="st">\'content\'</span>: next_prompt, <span class="st">\'tool_results\'</span>: tool_results}]'))
            + c.qa(t, '⚙️ 内部怎么走', 'How it flows',
                   '<p>' + t(
                       '一轮 = <strong>一次 client.chat</strong>（拿到 response）→ <strong>解析 tool_calls</strong> → '
                       '<strong>逐个 dispatch 执行</strong>（收集 tool_results / next_prompts / exit_reason）→ '
                       '<strong>turn_end_callback</strong> 拼出 next_prompt → <strong>把新消息塞进 messages</strong>，回到 while 顶部。'
                       '整个函数只有约 65 行，没有任何隐藏状态机。',
                       'One turn = <strong>one client.chat</strong> (get the response) → <strong>parse tool_calls</strong> → '
                       '<strong>dispatch each</strong> (collecting tool_results / next_prompts / exit_reason) → '
                       '<strong>turn_end_callback</strong> builds next_prompt → <strong>stuff the new message into messages</strong> '
                       'and jump back to the top of the while. The whole function is only ~65 lines, with no hidden state machine.') + '</p>')
            + c.qa(t, '❓ 为什么用 yield from', 'Why yield from',
                   '<p>' + t(
                       '<span class="inline">response = yield from client.chat(...)</span> 既能把模型的流式输出<strong>实时透传</strong>给上层（边想边显示），'
                       '又能在生成器结束时用 <span class="inline">return</span> 拿到最终的 response 对象。一行兼顾“流”和“结果”。',
                       '<span class="inline">response = yield from client.chat(...)</span> both <strong>passes the model\'s streaming '
                       'output through</strong> to the caller in real time (show as it thinks) and, when the generator finishes, '
                       'grabs the final response object via <span class="inline">return</span>. One line covers both "stream" and "result".') + '</p>'))
        + c.accordion(t, 2, 'tool_calls 是怎么解析出来的，no_tool 又是什么',
            'How tool_calls are parsed, and what no_tool is',
            c.qa(t, '🧪 解析代码', 'The parsing code',
                 c.codefile('agent_loop.py', 'agent_runner_loop',
                     '<span class="kw">if</span> <span class="kw">not</span> response.tool_calls:\n'
                     '    tool_calls = [{<span class="st">\'tool_name\'</span>: <span class="st">\'no_tool\'</span>, <span class="st">\'args\'</span>: {}}]\n'
                     '<span class="kw">else</span>:\n'
                     '    tool_calls = [{<span class="st">\'tool_name\'</span>: tc.function.name,\n'
                     '                   <span class="st">\'args\'</span>: json.<span class="fn">loads</span>(tc.function.arguments),\n'
                     '                   <span class="st">\'id\'</span>: tc.id}\n'
                     '                  <span class="kw">for</span> tc <span class="kw">in</span> response.tool_calls]'))
            + c.qa(t, '❓ 为什么要造 no_tool', 'Why fabricate no_tool',
                   '<p>' + t(
                       '当模型这一轮<strong>没有调用任何工具</strong>（往往意味着它想直接回答或已经做完），循环不会特判，而是塞一个虚拟的 '
                       '<span class="inline">no_tool</span> 进 tool_calls，统一交给 dispatch。dispatch 里对应 '
                       '<span class="inline">do_no_tool</span>，由它判断是“任务完成”还是“空回复需重试”。'
                       '这样主循环对“有没有工具”始终走同一条代码路径。',
                       'When the model calls <strong>no tool</strong> this turn (often meaning it wants to answer directly or is done), '
                       'the loop does not special-case it — it injects a virtual <span class="inline">no_tool</span> into tool_calls and '
                       'hands it to dispatch like any other. Dispatch maps it to <span class="inline">do_no_tool</span>, which decides '
                       'whether this is "task done" or "blank reply, retry". So the main loop always takes the same code path whether or not a tool was called.') + '</p>'))
        + c.accordion(t, 3, '三种结束：EXITED / CURRENT_TASK_DONE / MAX_TURNS_EXCEEDED',
            'The three endings: EXITED / CURRENT_TASK_DONE / MAX_TURNS_EXCEEDED',
            c.qa(t, '🧪 判定代码', 'The decision code',
                 c.codefile('agent_loop.py', 'agent_runner_loop',
                     '<span class="kw">if</span> outcome.should_exit:\n'
                     '    exit_reason = {<span class="st">\'result\'</span>: <span class="st">\'EXITED\'</span>, <span class="st">\'data\'</span>: outcome.data}; <span class="kw">break</span>\n'
                     '<span class="kw">if</span> <span class="kw">not</span> outcome.next_prompt:\n'
                     '    exit_reason = {<span class="st">\'result\'</span>: <span class="st">\'CURRENT_TASK_DONE\'</span>, <span class="st">\'data\'</span>: outcome.data}; <span class="kw">break</span>\n'
                     '<span class="cm"># ' + t('…循环正常走完 max_turns 轮…', '…loop runs out the max_turns rounds…') + '</span>\n'
                     '<span class="kw">return</span> exit_reason <span class="kw">or</span> {<span class="st">\'result\'</span>: <span class="st">\'MAX_TURNS_EXCEEDED\'</span>}'))
            + c.qa(t, '🔀 三者区别', 'How the three differ',
                   '<table class="t"><tr><th>' + t('结果', 'Result') + '</th><th>' + t('触发条件', 'Trigger')
                   + '</th><th>' + t('含义', 'Meaning') + '</th></tr>'
                   + '<tr><td class="mono">EXITED</td><td>' + t('某工具 should_exit=True', 'a tool sets should_exit=True')
                   + '</td><td>' + t('主动退出（如 ask_user 多次空回）', 'deliberate exit (e.g. repeated blank replies)') + '</td></tr>'
                   + '<tr><td class="mono">CURRENT_TASK_DONE</td><td>' + t('outcome.next_prompt 为空', 'outcome.next_prompt is empty')
                   + '</td><td>' + t('本轮没有下一步提示 = 任务自然结束', 'no next-turn prompt = task naturally finished') + '</td></tr>'
                   + '<tr><td class="mono">MAX_TURNS_EXCEEDED</td><td>' + t('while 跑满 max_turns', 'while exhausts max_turns')
                   + '</td><td>' + t('兜底上限，默认 40 轮', 'the safety cap, default 40 turns') + '</td></tr></table>')
            + c.qa(t, '⚠️ 坑点：next_prompt 为空就等于完成', 'Pitfall: empty next_prompt means done',
                   '<p>' + t(
                       '工具作者要注意：只要返回的 <span class="inline">StepOutcome.next_prompt</span> 是 None/空串，循环就判定 '
                       '<strong>CURRENT_TASK_DONE 并 break</strong>。想让任务继续，必须给一个非空的 next_prompt（哪怕只是 '
                       '<span class="inline">\'\\n\'</span>）。这就是为什么 do_code_run 等工具都用 '
                       '<span class="inline">_get_anchor_prompt()</span> 返回一段非空提示。',
                       'Tool authors beware: if the returned <span class="inline">StepOutcome.next_prompt</span> is None/empty, the loop '
                       'decides <strong>CURRENT_TASK_DONE and breaks</strong>. To keep going you must return a non-empty next_prompt (even '
                       'just <span class="inline">\'\\n\'</span>). That is why tools like do_code_run return a non-empty prompt via '
                       '<span class="inline">_get_anchor_prompt()</span>.') + '</p>'))
        + c.accordion(t, 4, 'messages=[新消息]、turn%10 重置与 max_turns=40',
            'messages=[new message], the turn%10 reset, and max_turns=40',
            c.qa(t, '🧪 关键三行', 'The three key lines',
                 c.codefile('agent_loop.py', 'agent_runner_loop',
                     '<span class="kw">def</span> <span class="fn">agent_runner_loop</span>(client, system_prompt, user_input, handler,\n'
                     '                      tools_schema, max_turns=<span class="nb">40</span>, ...):\n'
                     '    ...\n'
                     '    <span class="kw">if</span> turn%<span class="nb">10</span> == <span class="nb">0</span>: client.last_tools = <span class="st">\'\'</span>\n'
                     '    ...\n'
                     '    <span class="cm"># ' + t('只把新消息带入下一轮，历史由 *Session 维护', 'just new message, history is kept in *Session') + '</span>\n'
                     '    messages = [{<span class="st">\'role\'</span>: <span class="st">\'user\'</span>, '
                     '<span class="st">\'content\'</span>: next_prompt, <span class="st">\'tool_results\'</span>: tool_results}]'))
            + c.qa(t, '⚙️ 三件事各做什么', 'What each line does',
                   '<ul>'
                   + '<li>' + t('<strong>max_turns=40</strong>：默认最多 40 轮，是防止无限循环的硬上限（计划模式会被抬到 100/120）。',
                       '<strong>max_turns=40</strong>: at most 40 turns by default — the hard cap against infinite loops (plan mode raises it to 100/120).') + '</li>'
                   + '<li>' + t('<strong>turn%10==0 → client.last_tools=\'\'</strong>：每 10 轮把“工具库已激活”的缓存清空，强制下一次把完整工具描述再发一遍，防止长跑后模型“忘了”工具协议。',
                       '<strong>turn%10==0 → client.last_tools=\'\'</strong>: every 10 turns it clears the "tools already active" cache, forcing the full tool description to be re-sent so the model does not "forget" the tool protocol over a long run.') + '</li>'
                   + '<li>' + t('<strong>messages=[新消息]</strong>：下一轮 messages 只有这一条新内容，历史完全交给 Session——循环本身几乎无状态。',
                       '<strong>messages=[new message]</strong>: the next turn\'s messages holds only this one new entry; history is entirely delegated to the Session — the loop itself is almost stateless.') + '</li></ul>')
            + c.qa(t, '🔀 对比：把历史塞进 messages 的传统写法', 'vs the classic "stuff history into messages"',
                   '<p>' + t(
                       '很多框架每轮把<strong>全部历史</strong>追加进 messages 再发给模型，messages 越滚越长、循环也越来越难懂。'
                       'GA 反过来：循环只递新消息，<span class="inline">*Session.ask</span> 内部维护 history 并在发送前 trim/compress。'
                       '职责一分为二——循环管“这一轮”，Session 管“省 token 的历史”。',
                       'Many frameworks append the <strong>entire history</strong> into messages each turn before sending, so messages keeps '
                       'growing and the loop gets harder to follow. GA inverts this: the loop passes only the new message, while '
                       '<span class="inline">*Session.ask</span> maintains history internally and trims/compresses it before sending. '
                       'Responsibilities split cleanly — the loop owns "this turn", the Session owns "token-thrifty history".') + '</p>'))

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
    """LLM 内核 llmcore.py / The LLM Core."""
    return (
        '<p class="lead">'
        + t(
            '循环只调用一个方法——<span class="inline">client.chat(messages, tools)</span>。'
            '至于背后是 Claude、GPT，还是 Kimi、DeepSeek；是“原生函数调用”还是“纯文本协议”——'
            '这些差异全被 <span class="inline">llmcore.py</span> 抹平，对外只露出一个统一的、可流式的 chat 接口。',
            'The loop calls just one method — <span class="inline">client.chat(messages, tools)</span>. '
            'Whether the backend is Claude, GPT, Kimi or DeepSeek; whether it does "native function calling" or '
            'a "plain-text protocol" — all those differences are flattened by '
            '<span class="inline">llmcore.py</span>, which exposes one unified, streamable chat interface.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            'llmcore 干两件事：<strong>① 适配</strong>——把各家不同的请求/响应格式翻译成 GA 内部统一的对象；'
            '<strong>② 流式</strong>——一边把模型吐出的字实时显示给你，一边在结束时把回复解析成结构化的 '
            'tool_calls。它原生支持 OpenAI 兼容接口与 Anthropic Claude 原生接口两套协议。',
            'llmcore does two things: <strong>(1) adaptation</strong> — translating each vendor\'s request/'
            'response shapes into GA\'s unified internal objects; and <strong>(2) streaming</strong> — showing '
            'the model\'s tokens live while parsing the finished reply into structured tool_calls. It natively '
            'supports both the OpenAI-compatible and the Anthropic Claude native protocols.',
        )
        + '</p></div>'

        + '<h2>' + t('两种工具协议', 'Two tool protocols') + '</h2>'
        + '<div class="cols">'
        + '<div class="col"><h4>' + t('原生函数调用', 'Native function calling') + '</h4><p>'
        + t('把工具 schema 交给支持 function-calling 的模型 API，直接拿回结构化的 tool_calls。实现见 ',
            'Hand the tools schema to a model API that supports function calling and get structured tool_calls '
            'back directly. See ')
        + '<span class="inline">NativeToolClient</span>' + t('。', '.') + '</p></div>'
        + '<div class="col"><h4>' + t('纯文本协议', 'Plain-text protocol') + '</h4><p>'
        + t('对不支持函数调用的模型，先把工具说明拼进提示词，再从模型的文本回复里把工具调用解析出来。实现见 ',
            'For models without function calling, weave the tool instructions into the prompt, then parse tool '
            'calls out of the model\'s text reply. See ')
        + '<span class="inline">ToolClient</span>' + t('。', '.') + '</p></div>'
        + '</div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('两个客户端：', 'Two clients: ')
        + '<span class="inline">ToolClient</span>' + t('（文本协议）与 ', ' (text protocol) and ')
        + '<span class="inline">NativeToolClient</span>'
        + t('（原生协议），都提供 ', ' (native protocol), both exposing ')
        + '<span class="inline">chat(messages, tools)</span>' + t('。', '.') + '</li>'
        + '<li>' + t('多种会话后端：', 'Several session backends: ')
        + '<span class="inline">ClaudeSession / LLMSession / NativeClaudeSession / NativeOAISession</span>'
        + t('，并由 ', ', aggregated by ')
        + '<span class="inline">MixinSession</span>'
        + t(' 聚合多个后端；通过 ', '; the ')
        + '<span class="inline">api_mode</span>'
        + t(' 在 chat_completions 与 responses 之间切换。',
            ' switches between chat_completions and responses.') + '</li>'
        + '<li>' + t('流式由 SSE 解析器处理（', 'Streaming is handled by SSE parsers (')
        + '<span class="inline">_parse_openai_sse</span>' + t(' / ', ' / ')
        + '<span class="inline">_parse_claude_sse</span>'
        + t('）；不同协议的工具调用统一成 ', '); tool calls from any protocol are normalized into ')
        + '<span class="inline">MockResponse / MockToolCall</span>'
        + t('，所以循环永远只看到同一种 response 对象。',
            ', so the loop always sees the same kind of response object.') + '</li>'
        + '</ul></div>'

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '文本协议 vs 原生协议：两个 chat 的根本差异',
            'Text protocol vs native protocol: the core difference between the two chats',
            c.qa(t, '🧪 ToolClient.chat（文本协议）', 'ToolClient.chat (text protocol)',
                 c.codefile('llmcore.py', 'ToolClient.chat',
                     '<span class="kw">def</span> <span class="fn">chat</span>(self, messages, tools=None):\n'
                     '    full_prompt = self.<span class="fn">_build_protocol_prompt</span>(messages, tools)\n'
                     '    gen = self.backend.<span class="fn">ask</span>(full_prompt)\n'
                     '    raw_text = <span class="st">\'\'</span>\n'
                     '    <span class="kw">for</span> chunk <span class="kw">in</span> gen:\n'
                     '        raw_text += chunk; <span class="kw">yield</span> chunk\n'
                     '    <span class="kw">return</span> self.<span class="fn">_parse_mixed_response</span>(raw_text)'))
            + c.qa(t, '🧪 NativeToolClient.chat（原生协议）', 'NativeToolClient.chat (native protocol)',
                 c.codefile('llmcore.py', 'NativeToolClient.chat',
                     '<span class="kw">def</span> <span class="fn">chat</span>(self, messages, tools=None):\n'
                     '    <span class="kw">if</span> tools: self.backend.tools = tools\n'
                     '    <span class="cm"># ' + t('把 messages 拼成一条 user，含 tool_result 块', 'merge messages into one user msg with tool_result blocks') + '</span>\n'
                     '    merged = {<span class="st">\'role\'</span>: <span class="st">\'user\'</span>, <span class="st">\'content\'</span>: final_content}\n'
                     '    gen = self.backend.<span class="fn">ask</span>(merged)\n'
                     '    <span class="kw">try</span>:\n'
                     '        <span class="kw">while</span> <span class="nb">True</span>: chunk = next(gen); <span class="kw">yield</span> chunk\n'
                     '    <span class="kw">except</span> StopIteration <span class="kw">as</span> e: resp = e.value\n'
                     '    <span class="kw">return</span> resp'))
            + c.qa(t, '🔀 区别在哪', 'Where they differ',
                   '<p>' + t(
                       '<strong>ToolClient</strong>：模型不支持原生 function-calling，于是把工具协议写进<strong>纯文本提示词</strong>'
                       '（<span class="inline">_build_protocol_prompt</span> 注入“交互协议 + Tools JSON”），再用正则从混合文本里<strong>解析</strong>出 '
                       '<span class="inline">&lt;tool_use&gt;</span> 块。'
                       '<strong>NativeToolClient</strong>：模型支持原生工具调用，直接传 content-block，工具调用由 API 原生返回，无需文本解析。'
                       '两者都返回同一种 MockResponse，所以上层循环看不出区别。',
                       '<strong>ToolClient</strong>: the model has no native function-calling, so the tool protocol is written into a '
                       '<strong>plain-text prompt</strong> (<span class="inline">_build_protocol_prompt</span> injects the "interaction '
                       'protocol + Tools JSON"), and <span class="inline">&lt;tool_use&gt;</span> blocks are <strong>regex-parsed</strong> back '
                       'out of the mixed text. <strong>NativeToolClient</strong>: the model supports native tool calls, so it passes '
                       'content-blocks directly and tool calls come back natively, with no text parsing. Both return the same MockResponse, '
                       'so the loop above cannot tell them apart.') + '</p>'))
        + c.accordion(t, 2, '会话后端家族：Claude / OAI / Native，以及 MixinSession 兜底',
            'The session backend family: Claude / OAI / Native, and MixinSession fallback',
            c.qa(t, '🧪 四种会话', 'The four sessions',
                 '<table class="t"><tr><th>' + t('类', 'Class') + '</th><th>' + t('协议 / 端点', 'Protocol / endpoint')
                 + '</th></tr>'
                 + '<tr><td class="mono">ClaudeSession</td><td>' + t('Anthropic messages API（标准 key）', 'Anthropic messages API (standard key)') + '</td></tr>'
                 + '<tr><td class="mono">LLMSession</td><td>' + t('OpenAI 兼容（chat_completions / responses）', 'OpenAI-compatible (chat_completions / responses)') + '</td></tr>'
                 + '<tr><td class="mono">NativeClaudeSession</td><td>' + t('伪装 Claude Code CLI 的原生端点（claude-cli UA + beta headers）', 'native Claude Code CLI endpoint (claude-cli UA + beta headers)') + '</td></tr>'
                 + '<tr><td class="mono">NativeOAISession</td><td>' + t('继承 NativeClaudeSession，但走 OpenAI 流', 'subclasses NativeClaudeSession but uses the OpenAI stream') + '</td></tr></table>')
            + c.qa(t, '🧪 MixinSession 多后端兜底', 'MixinSession multi-backend fallback',
                 c.codefile('llmcore.py', 'MixinSession._raw_ask',
                     '<span class="kw">def</span> <span class="fn">_raw_ask</span>(self, *args, **kwargs):\n'
                     '    base, n = self.<span class="fn">_pick</span>(), len(self._sessions)\n'
                     '    <span class="kw">for</span> attempt <span class="kw">in</span> range(self._retries + <span class="nb">1</span>):\n'
                     '        idx = (base + attempt) % n\n'
                     '        gen = self._orig_raw_asks[idx](*args, **kwargs)\n'
                     '        <span class="cm"># ' + t('出错就轮换到下一个后端，成功后弹回主后端', 'on error rotate to next backend; spring back to primary on success') + '</span>\n'
                     '        ...'))
            + c.qa(t, '❓ 为什么要 Mixin', 'Why Mixin',
                   '<p>' + t(
                       '单个 API 会限流或抖动。<span class="inline">MixinSession</span> 把若干同组（全 Native 或全非 Native）后端串成一条<strong>容错链</strong>：'
                       '主后端失败就轮换到下一个，过了 <span class="inline">spring_back</span> 秒再<strong>弹回</strong>主后端。'
                       '它用 <span class="inline">__getattr__/__setattr__</span> 把属性广播到所有子会话，对上层伪装成“一个会话”。',
                       'A single API can rate-limit or flake. <span class="inline">MixinSession</span> chains several same-group (all-Native or '
                       'all-non-Native) backends into a <strong>fault-tolerant chain</strong>: if the primary fails it rotates to the next, then '
                       '<strong>springs back</strong> to the primary after <span class="inline">spring_back</span> seconds. It broadcasts attributes '
                       'to all sub-sessions via <span class="inline">__getattr__/__setattr__</span>, disguising itself as "one session" to the caller.') + '</p>'))
        + c.accordion(t, 3, 'SSE 解析器与 Mock 归一化：循环为什么永远只看到一种对象',
            'SSE parsers and Mock normalization: why the loop only ever sees one object',
            c.qa(t, '🧪 把流式事件拼成 content_block', 'Assembling stream events into content_blocks',
                 c.codefile('llmcore.py', '_parse_claude_sse',
                     '<span class="kw">elif</span> evt_type == <span class="st">\'content_block_delta\'</span>:\n'
                     '    <span class="kw">if</span> delta.get(<span class="st">\'type\'</span>) == <span class="st">\'text_delta\'</span>:\n'
                     '        current_block[<span class="st">\'text\'</span>] += text; <span class="kw">yield</span> text\n'
                     '    <span class="kw">elif</span> delta.get(<span class="st">\'type\'</span>) == <span class="st">\'input_json_delta\'</span>:\n'
                     '        tool_json_buf += delta.get(<span class="st">\'partial_json\'</span>, <span class="st">\'\'</span>)\n'
                     '<span class="cm"># ' + t('_parse_openai_sse 同理，最终都产出 list[content_block]', '_parse_openai_sse is analogous; both yield list[content_block]') + '</span>'))
            + c.qa(t, '🧪 MockResponse / MockToolCall 归一化', 'MockResponse / MockToolCall normalization',
                 c.codefile('llmcore.py', 'MockResponse / MockToolCall',
                     '<span class="kw">class</span> <span class="fn">MockToolCall</span>:\n'
                     '    <span class="kw">def</span> <span class="fn">__init__</span>(self, name, args, id=<span class="st">\'\'</span>):\n'
                     '        arg_str = json.<span class="fn">dumps</span>(args, ...) <span class="kw">if</span> isinstance(args, (dict, list)) <span class="kw">else</span> (args <span class="kw">or</span> <span class="st">\'{}\'</span>)\n'
                     '        self.function = <span class="fn">MockFunction</span>(name, arg_str); self.id = id\n'
                     '<span class="kw">class</span> <span class="fn">MockResponse</span>:\n'
                     '    <span class="kw">def</span> <span class="fn">__init__</span>(self, thinking, content, tool_calls, raw, stop_reason=<span class="st">\'end_turn\'</span>):\n'
                     '        self.thinking = thinking; self.content = content; self.tool_calls = tool_calls'))
            + c.qa(t, '⚙️ 归一化为什么重要', 'Why normalization matters',
                   '<p>' + t(
                       'Claude 返回 content-block，OpenAI 返回 delta+tool_calls，responses API 又是另一套事件名。'
                       '各解析器先把它们统一成 <span class="inline">list[content_block]</span>，再包成 '
                       '<span class="inline">MockResponse(thinking, content, tool_calls, raw)</span>。'
                       '于是 <span class="inline">agent_loop.py</span> 里 <span class="inline">response.tool_calls</span>、'
                       '<span class="inline">tc.function.name/arguments</span> 这套字段对任意模型都成立——<strong>多协议的复杂性被锁死在 llmcore 内</strong>。',
                       'Claude returns content-blocks, OpenAI returns deltas + tool_calls, and the responses API uses yet another set of event '
                       'names. Each parser first unifies them into <span class="inline">list[content_block]</span>, then wraps them as '
                       '<span class="inline">MockResponse(thinking, content, tool_calls, raw)</span>. So in '
                       '<span class="inline">agent_loop.py</span> the fields <span class="inline">response.tool_calls</span> and '
                       '<span class="inline">tc.function.name/arguments</span> hold for any model — <strong>the multi-protocol complexity is '
                       'sealed inside llmcore</strong>.') + '</p>'))
        + c.accordion(t, 4, 'api_mode：chat_completions 与 responses 的切换点',
            'api_mode: the switch between chat_completions and responses',
            c.qa(t, '🧪 解析为枚举', 'Parsed into an enum',
                 c.codefile('llmcore.py', 'BaseSession.__init__',
                     'mode = str(cfg.get(<span class="st">\'api_mode\'</span>, <span class="st">\'chat_completions\'</span>)).strip().lower().replace(<span class="st">\'-\'</span>, <span class="st">\'_\'</span>)\n'
                     'self.api_mode = <span class="st">\'responses\'</span> <span class="kw">if</span> mode <span class="kw">in</span> (<span class="st">\'responses\'</span>, <span class="st">\'response\'</span>) <span class="kw">else</span> <span class="st">\'chat_completions\'</span>'))
            + c.qa(t, '⚙️ 两种模式怎么影响下游', 'How the two modes affect the rest',
                   '<p>' + t(
                       '<span class="inline">api_mode</span> 一路传到 <span class="inline">_parse_openai_sse</span> 与 '
                       '<span class="inline">_record_usage</span>：',
                       '<span class="inline">api_mode</span> flows all the way to <span class="inline">_parse_openai_sse</span> and '
                       '<span class="inline">_record_usage</span>:') + '</p>'
                   + '<ul><li>' + t('<strong>chat_completions</strong>：读 <span class="inline">choices[0].delta.content / tool_calls</span>，用量字段是 prompt_tokens / completion_tokens。',
                       '<strong>chat_completions</strong>: reads <span class="inline">choices[0].delta.content / tool_calls</span>; usage fields are prompt_tokens / completion_tokens.') + '</li>'
                   + '<li>' + t('<strong>responses</strong>：读 <span class="inline">response.output_text.delta</span> 与 <span class="inline">response.function_call_arguments.delta</span>，用量是 input_tokens / output_tokens（含 cached）。',
                       '<strong>responses</strong>: reads <span class="inline">response.output_text.delta</span> and <span class="inline">response.function_call_arguments.delta</span>; usage is input_tokens / output_tokens (with cached).') + '</li></ul>')
            + c.qa(t, '⚠️ 坑点：配置名会被归一化', 'Pitfall: the config value is normalized',
                   '<p>' + t(
                       '写 <span class="inline">api_mode: "response"</span>（少个 s）或 <span class="inline">"chat-completions"</span>（连字符）都不会报错——'
                       '初始化时会 <span class="inline">strip().lower().replace(\'-\',\'_\')</span> 并把 response/responses 都收敛到 '
                       '<span class="inline">\'responses\'</span>，其余一律当 <span class="inline">\'chat_completions\'</span>。容错，但也意味着拼错的非法值会<strong>静默</strong>落到默认值。',
                       'Writing <span class="inline">api_mode: "response"</span> (missing the s) or <span class="inline">"chat-completions"</span> '
                       '(hyphen) raises no error — init runs <span class="inline">strip().lower().replace(\'-\',\'_\')</span> and folds both '
                       'response/responses to <span class="inline">\'responses\'</span>, treating anything else as '
                       '<span class="inline">\'chat_completions\'</span>. Forgiving — but it also means a mistyped invalid value <strong>silently</strong> '
                       'falls back to the default.') + '</p>'))

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像一个<strong>万能电源适配器</strong>：欧标、美标、英标插头形状各异，适配器统一转成你设备要的那一种。'
            'llmcore 就是模型世界的适配器——无论模型“插头”长什么样，循环拿到的永远是同一个标准接口。',
            'Like a <strong>universal power adapter</strong>: EU, US, UK plugs all look different, and the adapter '
            'converts them to the one your device needs. llmcore is that adapter for the model world — whatever a '
            'model\'s "plug" looks like, the loop always receives the same standard interface.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('对外只有一个统一入口 chat(messages, tools)，屏蔽所有模型差异。',
            'There is one unified entry, chat(messages, tools), hiding all model differences.') + '</li>'
        + '<li>' + t('两种工具协议：原生函数调用（NativeToolClient）与纯文本协议（ToolClient）。',
            'Two tool protocols: native function calling (NativeToolClient) and text protocol (ToolClient).') + '</li>'
        + '<li>' + t('不同协议的回复统一成 MockResponse / MockToolCall，循环无需关心来源。',
            'Replies from any protocol become MockResponse / MockToolCall, so the loop need not care about the source.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '<span class="inline">chat()</span> 是个<strong>生成器</strong>：它一边 yield 流式字符，一边在结束时 '
            'return 解析好的结构化回复。这正是循环里那句 <span class="inline">response = yield from client.chat(...)</span> '
            '能同时拿到“实时输出”和“最终结果”的原因。更妙的是文本协议这条退路——它让<strong>连函数调用都不支持的模型也能用上工具</strong>，'
            '把 GA 的“高兼容性”落到了实处。',
            '<span class="inline">chat()</span> is a <strong>generator</strong>: it yields streaming characters '
            'while returning the parsed, structured reply at the end. That is exactly why the loop\'s '
            '<span class="inline">response = yield from client.chat(...)</span> gets both "live output" and the '
            '"final result". Even better is the text-protocol fallback — it lets <strong>models without function '
            'calling still use tools</strong>, making GA\'s "high compatibility" real.',
        )
        + '</div>'
    )


def lesson_10(t):
    """Handler 与工具调度 / Handler & Tool Dispatch."""
    return (
        '<p class="lead">'
        + t(
            '模型说“我要调 code_run”，这句话怎么变成真正跑起来的代码？答案是 '
            '<span class="inline">agent_loop.py: BaseHandler.dispatch</span>：它按工具名找到对应的 '
            '<span class="inline">do_&lt;tool&gt;</span> 方法、执行它、并把结果包成 StepOutcome 交回循环。',
            'The model says "I want to call code_run" — how does that sentence become real running code? The '
            'answer is <span class="inline">agent_loop.py: BaseHandler.dispatch</span>: it finds the matching '
            '<span class="inline">do_&lt;tool&gt;</span> method by tool name, runs it, and wraps the result in a '
            'StepOutcome handed back to the loop.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '调度的规则简单到只有一句话：<strong>工具名 ', 'The dispatch rule is one sentence: <strong>tool name ')
        + '<span class="mono">X</span>'
        + t(' → 调用方法 ', ' → call the method ') + '<span class="mono">do_X</span></strong>'
        + t('。所有工具都是 ', '. Every tool is a ')
        + '<span class="inline">do_&lt;tool&gt;</span>'
        + t(' 方法，集中在 ', ' method, gathered in ')
        + '<span class="inline">ga.py: GenericAgentHandler</span>'
        + t('（它继承自 BaseHandler）。想加一个新工具？再加一个 do_ 方法就行，循环一行都不用改。',
            ' (which subclasses BaseHandler). Want a new tool? Add one more do_ method; the loop needs zero changes.',
        )
        + '</p></div>'

        + '<div class="codefile"><div class="cf-head"><span class="dot"></span>'
        + '<span class="path">agent_loop.py</span><span class="ln">BaseHandler.dispatch</span></div>'
        + '<pre>'
        + '<span class="kw">def</span> <span class="fn">dispatch</span>(self, tool_name, args, response, ...):\n'
        + '    method_name = <span class="st">f"do_{tool_name}"</span>\n'
        + '    <span class="kw">if</span> hasattr(self, method_name):\n'
        + '        _hook(<span class="st">\'tool_before\'</span>, locals())\n'
        + '        ret = <span class="kw">yield from</span> try_call_generator(getattr(self, method_name), args, response)\n'
        + '        _hook(<span class="st">\'tool_after\'</span>, locals())\n'
        + '        <span class="kw">return</span> ret  <span class="cm"># ' + t('一个 StepOutcome', 'a StepOutcome') + '</span>\n'
        + '    <span class="kw">else</span>:\n'
        + '        <span class="kw">yield</span> <span class="st">f"' + t('未知工具', 'unknown tool') + ': {tool_name}\\n"</span>\n'
        + '        <span class="kw">return</span> StepOutcome(<span class="nb">None</span>, next_prompt=...)\n'
        + '</pre></div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('每个 do_ 方法都是<strong>生成器</strong>：用 ', 'Each do_ method is a <strong>generator</strong>: it ')
        + '<span class="inline">yield</span>'
        + t(' 实时吐出给用户看的过程，再 ', 's process output for the user in real time, then ')
        + '<span class="inline">return</span>'
        + t(' 一个 StepOutcome 作为结构化结果。',
            's a StepOutcome as the structured result.') + '</li>'
        + '<li>' + t('辅助函数 ', 'The helper ')
        + '<span class="inline">try_call_generator</span>'
        + t(' 同时兼容“普通返回”和“生成器”两种写法，让 do_ 方法可繁可简。',
            ' supports both "plain return" and "generator" styles, so do_ methods can be simple or rich.') + '</li>'
        + '<li>' + t('调度内置两个钩子点 ', 'Dispatch has two built-in hook points, ')
        + '<span class="inline">tool_before</span>' + t(' / ', ' / ')
        + '<span class="inline">tool_after</span>'
        + t('（详见“钩子与可观测性”一课）；未知工具与 bad_json 也在这里兜底处理。',
            ' (see the "Hooks & Observability" lesson); unknown tools and bad_json are also handled here.') + '</li>'
        + '<li>' + t('每轮收尾还会调用 ', 'At the end of each turn it also calls ')
        + '<span class="inline">turn_end_callback</span>'
        + t('，把本轮的 response、工具结果与 next_prompt 串起来。',
            ', stitching this turn\'s response, tool results and next_prompt together.') + '</li>'
        + '</ul></div>'

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '逐行读 dispatch：从工具名到 do_ 方法',
            'Line by line: dispatch, from tool name to do_ method',
            c.qa(t, '🧪 BaseHandler.dispatch 全文', 'The full BaseHandler.dispatch',
                 c.codefile('agent_loop.py', 'BaseHandler.dispatch',
                     '<span class="kw">def</span> <span class="fn">dispatch</span>(self, tool_name, args, response, index=<span class="nb">0</span>, tool_num=<span class="nb">1</span>):\n'
                     '    method_name = f<span class="st">\'do_{tool_name}\'</span>\n'
                     '    <span class="kw">if</span> hasattr(self, method_name):\n'
                     '        args[<span class="st">\'_index\'</span>] = index; args[<span class="st">\'_tool_num\'</span>] = tool_num\n'
                     '        _hook(<span class="st">\'tool_before\'</span>, locals())\n'
                     '        ret = <span class="kw">yield from</span> <span class="fn">try_call_generator</span>(getattr(self, method_name), args, response)\n'
                     '        _hook(<span class="st">\'tool_after\'</span>, locals())\n'
                     '        <span class="kw">return</span> ret\n'
                     '    <span class="kw">elif</span> tool_name == <span class="st">\'bad_json\'</span>:\n'
                     '        <span class="kw">return</span> <span class="fn">StepOutcome</span>(None, next_prompt=args.get(<span class="st">\'msg\'</span>, <span class="st">\'bad_json\'</span>), should_exit=<span class="nb">False</span>)\n'
                     '    <span class="kw">else</span>:\n'
                     '        <span class="kw">yield</span> f<span class="st">\'' + t('未知工具', 'unknown tool') + ': {tool_name}\\n\'</span>\n'
                     '        <span class="kw">return</span> <span class="fn">StepOutcome</span>(None, next_prompt=f<span class="st">\'' + t('未知工具', 'unknown tool') + ' {tool_name}\'</span>, should_exit=<span class="nb">False</span>)'))
            + c.qa(t, '⚙️ 走查一遍', 'A walkthrough',
                   '<p>' + t(
                       '① 用 <span class="inline">f"do_{tool_name}"</span> 拼出方法名；② <span class="inline">hasattr</span> 找得到就执行——'
                       '先注入 <span class="inline">_index/_tool_num</span> 两个内部参数，前后各触发一次 hook，中间用 '
                       '<span class="inline">try_call_generator</span> 调用；③ 找不到方法时，<span class="inline">bad_json</span> 与未知工具各有兜底，'
                       '都返回一个非空 next_prompt 让循环继续而不是崩溃。',
                       '① build the method name with <span class="inline">f"do_{tool_name}"</span>; ② if <span class="inline">hasattr</span> finds it, '
                       'run it — first inject the internal args <span class="inline">_index/_tool_num</span>, fire a hook before and after, and call it '
                       'through <span class="inline">try_call_generator</span>; ③ when no method is found, <span class="inline">bad_json</span> and unknown '
                       'tools each have a fallback, both returning a non-empty next_prompt so the loop continues instead of crashing.') + '</p>')
            + c.qa(t, '⚠️ 坑点：_index / _tool_num 是内部参数', 'Pitfall: _index / _tool_num are internal args',
                   '<p>' + t(
                       'dispatch 会往 args 里塞 <span class="inline">_index</span>（这是本轮第几个工具）和 '
                       '<span class="inline">_tool_num</span>（本轮一共几个工具）。do_ 方法用它们做分流——例如 '
                       '<span class="inline">do_code_run</span> 用 <span class="inline">_tool_num</span> 平分输出长度上限、用 '
                       '<span class="inline">_index&gt;0</span> 决定是否跳过锚点提示。所有以 <span class="inline">_</span> 开头的键在记账与摘要里都会被过滤掉。',
                       'dispatch injects <span class="inline">_index</span> (which tool this is in the turn) and '
                       '<span class="inline">_tool_num</span> (how many tools this turn) into args. do_ methods use them to branch — e.g. '
                       '<span class="inline">do_code_run</span> divides the output-length cap by <span class="inline">_tool_num</span> and uses '
                       '<span class="inline">_index&gt;0</span> to decide whether to skip the anchor prompt. Any key starting with '
                       '<span class="inline">_</span> is filtered out of accounting and summaries.') + '</p>'))
        + c.accordion(t, 2, '“工具即生成器”协议：yield 过程，return StepOutcome',
            'The "tool is a generator" protocol: yield progress, return StepOutcome',
            c.qa(t, '🧪 try_call_generator 兼容两种写法', 'try_call_generator supports both styles',
                 c.codefile('agent_loop.py', 'try_call_generator',
                     '<span class="kw">def</span> <span class="fn">try_call_generator</span>(func, *args, **kwargs):\n'
                     '    ret = func(*args, **kwargs)\n'
                     '    <span class="kw">if</span> hasattr(ret, <span class="st">\'__iter__\'</span>) <span class="kw">and</span> <span class="kw">not</span> isinstance(ret, (str, bytes, dict, list)):\n'
                     '        ret = <span class="kw">yield from</span> ret\n'
                     '    <span class="kw">return</span> ret'))
            + c.qa(t, '🧪 一个真实工具长这样', 'A real tool looks like this',
                 c.codefile('ga.py', 'GenericAgentHandler.do_code_run',
                     '<span class="kw">def</span> <span class="fn">do_code_run</span>(self, args, response):\n'
                     '    ...\n'
                     '    result = <span class="kw">yield from</span> <span class="fn">code_run</span>(code, code_type, timeout, cwd, ...)  <span class="cm"># ' + t('yield 实时输出', 'yield live output') + '</span>\n'
                     '    next_prompt = self.<span class="fn">_get_anchor_prompt</span>(skip=args.get(<span class="st">\'_index\'</span>, <span class="nb">0</span>) &gt; <span class="nb">0</span>)\n'
                     '    <span class="kw">return</span> <span class="fn">StepOutcome</span>(result, next_prompt=next_prompt)  <span class="cm"># ' + t('return 结构化结果', 'return structured result') + '</span>'))
            + c.qa(t, '❓ 为什么用生成器而不是普通函数', 'Why a generator instead of a plain function',
                   '<p>' + t(
                       '一个 do_ 方法要同时做两件事：把执行过程<strong>实时流式</strong>展示给用户（如 code_run 边跑边打印），'
                       '以及把最终结果<strong>结构化</strong>交回循环。生成器天然适配：<span class="inline">yield</span> 负责“过程”，'
                       '<span class="inline">return</span> 负责“结果”。<span class="inline">try_call_generator</span> 还允许简单工具直接 '
                       '<span class="inline">return StepOutcome(...)</span> 不写 yield，繁简自由。',
                       'A do_ method must do two things at once: <strong>stream</strong> its progress to the user in real time (e.g. code_run prints '
                       'as it runs) and hand a <strong>structured</strong> result back to the loop. A generator fits naturally: '
                       '<span class="inline">yield</span> carries the "progress", <span class="inline">return</span> carries the "result". '
                       '<span class="inline">try_call_generator</span> also lets simple tools just <span class="inline">return StepOutcome(...)</span> '
                       'without any yield — rich or simple, your choice.') + '</p>'))
        + c.accordion(t, 3, '兜底处理：bad_json、未知工具与 do_no_tool',
            'Fallbacks: bad_json, unknown tools, and do_no_tool',
            c.qa(t, '⚙️ 三种异常分支', 'Three fallback branches',
                   '<ul>'
                   + '<li>' + t('<strong>bad_json</strong>：模型吐出的 tool_use JSON 解析失败，llmcore 会造一个 <span class="inline">MockToolCall(\'bad_json\', {\'msg\':...})</span>；dispatch 把 msg 当 next_prompt 回灌，让模型重发。',
                       '<strong>bad_json</strong>: when the model\'s tool_use JSON fails to parse, llmcore fabricates a <span class="inline">MockToolCall(\'bad_json\', {\'msg\':...})</span>; dispatch feeds the msg back as next_prompt so the model retries.') + '</li>'
                   + '<li>' + t('<strong>未知工具</strong>：模型调了不存在的工具名，dispatch yield 一句提示并回灌，同时循环把 <span class="inline">client.last_tools</span> 清空（强制重发工具表）。',
                       '<strong>unknown tool</strong>: the model calls a non-existent tool name; dispatch yields a note and feeds it back, while the loop clears <span class="inline">client.last_tools</span> (forcing a re-send of the tool list).') + '</li>'
                   + '<li>' + t('<strong>do_no_tool</strong>：这一轮模型没调任何工具，循环造 no_tool → 走到 <span class="inline">do_no_tool</span>，由它判断是“完成”还是“空回复/截断要重试”。',
                       '<strong>do_no_tool</strong>: the model called no tool this turn; the loop fabricates no_tool → reaches <span class="inline">do_no_tool</span>, which decides "done" vs "blank/truncated, retry".') + '</li></ul>')
            + c.qa(t, '🧪 do_no_tool 的判定', 'do_no_tool decisions',
                 c.codefile('ga.py', 'GenericAgentHandler.do_no_tool',
                     '<span class="kw">def</span> <span class="fn">do_no_tool</span>(self, args, response):\n'
                     '    content = getattr(response, <span class="st">\'content\'</span>, <span class="st">\'\'</span>) <span class="kw">or</span> <span class="st">\'\'</span>\n'
                     '    <span class="kw">if</span> <span class="kw">not</span> response <span class="kw">or</span> (<span class="kw">not</span> content.strip() <span class="kw">and</span> <span class="kw">not</span> thinking.strip()):\n'
                     '        <span class="kw">return</span> self.<span class="fn">_retry_or_exit</span>(<span class="st">\'[System] Blank response, regenerate and tooluse\'</span>)\n'
                     '    <span class="cm"># ' + t('检测“只有一个大代码块却没调工具”等情况…', 'detect "one big code block but no tool call", etc…') + '</span>\n'
                     '    <span class="kw">return</span> <span class="fn">StepOutcome</span>(response, next_prompt=None)  <span class="cm"># ' + t('next_prompt=None ⇒ 任务完成', 'next_prompt=None ⇒ task done') + '</span>'))
            + c.qa(t, '🔀 完成 vs 重试', 'Done vs retry',
                   '<p>' + t(
                       'do_no_tool 是“任务该不该结束”的实际裁判：正常情况返回 '
                       '<span class="inline">StepOutcome(response, next_prompt=None)</span>，循环据此判 CURRENT_TASK_DONE；'
                       '但若发现空回复、流中断、max_tokens 截断，或“一大段代码却没调工具”，它就返回一个<strong>非空</strong> next_prompt 把模型拉回来重试，'
                       '连续 3 次空回复才 <span class="inline">should_exit</span>。',
                       'do_no_tool is the real referee for "should the task end": normally it returns '
                       '<span class="inline">StepOutcome(response, next_prompt=None)</span>, on which the loop decides CURRENT_TASK_DONE; '
                       'but if it spots a blank reply, a broken stream, a max_tokens truncation, or "a big code block but no tool call", it returns a '
                       '<strong>non-empty</strong> next_prompt to pull the model back for a retry, only setting <span class="inline">should_exit</span> '
                       'after 3 blank replies in a row.') + '</p>'))
        + c.accordion(t, 4, 'turn_end_callback：每轮收尾的“缝合”',
            'turn_end_callback: stitching up the end of each turn',
            c.qa(t, '🧪 摘要回填与 DANGER 提示', 'Summary backfill and DANGER nudges',
                 c.codefile('ga.py', 'GenericAgentHandler.turn_end_callback',
                     '<span class="kw">def</span> <span class="fn">turn_end_callback</span>(self, response, tool_calls, tool_results, turn, next_prompt, exit_reason):\n'
                     '    rsumm = re.<span class="fn">search</span>(r<span class="st">\'&lt;summary&gt;(.*?)&lt;/summary&gt;\'</span>, _c, re.DOTALL)\n'
                     '    summary = rsumm.group(<span class="nb">1</span>).strip() <span class="kw">if</span> rsumm <span class="kw">else</span> ...\n'
                     '    self.history_info.<span class="fn">append</span>(f<span class="st">\'[Agent] {summary}\'</span>)\n'
                     '    <span class="kw">if</span> turn % <span class="nb">7</span> == <span class="nb">0</span>: next_prompt += <span class="st">\'...[DANGER] ' + t('禁止无效重试…', 'no pointless retries…') + '\'</span>\n'
                     '    <span class="kw">elif</span> turn % <span class="nb">10</span> == <span class="nb">0</span>: next_prompt += <span class="fn">get_global_memory</span>()\n'
                     '    <span class="kw">return</span> next_prompt'))
            + c.qa(t, '⚙️ 它把哪些东西缝在一起', 'What it stitches together',
                   '<p>' + t(
                       'turn_end_callback 在循环每轮末尾被调用，负责：① 从模型回复里抽 <span class="inline">&lt;summary&gt;</span> 追加进 '
                       '<span class="inline">history_info</span>（供下轮锚点提示回灌）；② 按 turn 周期插入 DANGER 提示或重灌全局记忆；'
                       '③ 计划模式下提醒读 plan.md；④ 消费 master 注入的 keyinfo/intervene。它的返回值就是循环写进下一轮 messages 的 next_prompt。',
                       'turn_end_callback runs at the end of each loop turn and is responsible for: ① extracting <span class="inline">&lt;summary&gt;</span> '
                       'from the model reply and appending it to <span class="inline">history_info</span> (re-injected via the next anchor prompt); '
                       '② inserting DANGER nudges or re-loading global memory on turn cycles; ③ reminding to read plan.md in plan mode; '
                       '④ consuming master-injected keyinfo/intervene. Its return value is exactly the next_prompt the loop writes into the next turn\'s messages.') + '</p>'))

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像公司前台的<strong>总机转接</strong>：你报一个部门名（工具名），总机就把电话接到对应分机（do_ 方法）。'
            '前台不需要懂每个部门怎么干活，只要知道“名字 → 分机”的对应关系；新开一个部门，只要登记一个新分机号即可。',
            'Like a company switchboard <strong>routing a call</strong>: you say a department name (the tool name) '
            'and the operator connects you to the right extension (the do_ method). The operator need not know how '
            'each department works, only the "name → extension" mapping; opening a new department just means '
            'registering one new extension.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('调度规则：工具名 X → 方法 do_X，集中在 GenericAgentHandler。',
            'Dispatch rule: tool name X → method do_X, gathered in GenericAgentHandler.') + '</li>'
        + '<li>' + t('do_ 方法是生成器：yield 过程输出，return 一个 StepOutcome。',
            'do_ methods are generators: yield process output, return a StepOutcome.') + '</li>'
        + '<li>' + t('加工具 = 加一个 do_ 方法；循环与调度无需改动。',
            'Adding a tool = adding a do_ method; the loop and dispatch stay untouched.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '“工具即生成器”是这里最优雅的一招：同一个方法既能<strong>流式展示</strong>执行过程，又能<strong>结构化返回</strong>最终结果，'
            '两件事一次写完。再配上 <span class="inline">f"do_{tool_name}"</span> 的约定式调度，整套工具系统对扩展<strong>开放</strong>、对核心<strong>封闭</strong>——'
            '这正是 GA 能从 9 个工具不断长出新能力的结构基础。',
            '"A tool is a generator" is the most elegant move here: one method both <strong>streams</strong> its '
            'progress and <strong>returns a structured</strong> result — both written at once. Combined with the '
            'convention-based <span class="inline">f"do_{tool_name}"</span> dispatch, the whole tool system is '
            '<strong>open</strong> to extension and <strong>closed</strong> at the core — the structural basis for '
            'GA growing new abilities from just 9 tools.',
        )
        + '</div>'
    )


def lesson_11(t):
    """分层记忆系统 L0–L4 / Layered Memory (L0–L4)."""
    return (
        '<p class="lead">'
        + t(
            'GenericAgent 的记忆不是一锅粥，而是一座<strong>金字塔</strong>：从最顶上的“铁律”，到一份极简索引、'
            '一个事实库、一摞可复用的 SOP，再到最底层归档的历史会话。层层向下越来越细，向上越来越短。',
            'GenericAgent\'s memory is not one big soup but a <strong>pyramid</strong>: from the "iron rules" at '
            'the top, down to a tiny index, a facts store, a stack of reusable SOPs, and finally archived past '
            'sessions at the bottom. Each layer down is more detailed; each layer up is shorter.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '为什么要分层？因为上下文很贵。GA 让<strong>上层只放“能指向下层的最短指针”</strong>：平时只加载极简的索引，'
            '真需要细节时再顺着指针去读对应的事实或 SOP。这样既不丢信息，又把每次喂给模型的上下文压到最小。',
            'Why layer it? Because context is expensive. GA keeps <strong>upper layers holding only "the shortest '
            'pointer to the layer below"</strong>: normally it loads just the tiny index, and only follows a '
            'pointer to a fact or SOP when detail is actually needed. No information is lost, yet the context fed '
            'to the model each time stays minimal.',
        )
        + '</p></div>'

        + '<h2>' + t('五层记忆', 'Five memory layers') + '</h2>'
        + '<div class="layers">'
        + '<div class="layer l-core"><div class="lh"><span class="badge">L0</span>'
        + '<span class="name">' + t('元规则 / Meta Rules', 'Meta Rules') + '</span></div>'
        + '<div class="ld">' + t(
            '最高优先级的行为铁律——如“无行动，不记忆”“禁止存易变状态”。见 memory/memory_management_sop.md 的核心公理。',
            'Top-priority behavioral rules — e.g. "No execution, no memory", "Do not store volatile state". See the '
            'core axioms in memory/memory_management_sop.md.') + '</div></div>'
        + '<div class="layer l-main"><div class="lh"><span class="badge">L1</span>'
        + '<span class="name">' + t('索引 / Insight Index', 'Insight Index') + '</span></div>'
        + '<div class="ld">' + t(
            '极简导航索引（global_mem_insight.txt，硬约束 ≤ 30 行），只留能定位 L2/L3 的最短标识。',
            'A tiny navigation index (global_mem_insight.txt, hard cap ≤ 30 lines) holding only the shortest '
            'locators into L2/L3.') + '</div></div>'
        + '<div class="layer l-part"><div class="lh"><span class="badge">L2</span>'
        + '<span class="name">' + t('事实库 / Global Facts', 'Global Facts') + '</span></div>'
        + '<div class="ld">' + t(
            '经行动验证的稳定知识（global_mem.txt）：路径、凭证、配置等长期有效的事实。',
            'Action-verified, stable knowledge (global_mem.txt): paths, credentials, configs and other long-lived '
            'facts.') + '</div></div>'
        + '<div class="layer l-app"><div class="lh"><span class="badge">L3</span>'
        + '<span class="name">' + t('技能 / Task Skills · SOPs', 'Task Skills · SOPs') + '</span></div>'
        + '<div class="ld">' + t(
            '可复用的工作流：memory/ 下的一摞 .md / .py（如 plan_sop.md、verify_sop.md）。这是“技能”真正住的地方。',
            'Reusable workflows: a stack of .md / .py under memory/ (e.g. plan_sop.md, verify_sop.md). This is where '
            '"skills" actually live.') + '</div></div>'
        + '<div class="layer l-part"><div class="lh"><span class="badge">L4</span>'
        + '<span class="name">' + t('归档 / Session Archive', 'Session Archive') + '</span></div>'
        + '<div class="ld">' + t(
            '历史会话存档（memory/L4_raw_sessions/），由 reflect/scheduler 自动收集，供长程回溯定位过往上下文。',
            'Archived past sessions (memory/L4_raw_sessions/), auto-collected by reflect/scheduler, for long-horizon '
            'recall of earlier context.') + '</div></div>'
        + '</div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('层级架构与各层职责写在 ', 'The layer architecture and each layer\'s duties are written in ')
        + '<span class="inline">memory/memory_management_sop.md</span>'
        + t('（含 L1→L2→L3→L4 的“指针 → 引用”导航链）。',
            ' (including the "pointer → reference" navigation chain L1→L2→L3→L4).') + '</li>'
        + '<li>' + t('L3 就是 ', 'L3 is the ')
        + '<span class="inline">memory/</span>'
        + t(' 目录本身：里面是一堆 *_sop.md（plan_sop、verify_sop、github_contribution_sop…）。',
            ' directory itself: a pile of *_sop.md files (plan_sop, verify_sop, github_contribution_sop …).') + '</li>'
        + '<li>' + t('L4 在 ', 'L4 lives in ')
        + '<span class="inline">memory/L4_raw_sessions/</span>'
        + t('，由 reflect/scheduler.py 的反射任务自动归集。',
            ', auto-collected by reflection tasks in reflect/scheduler.py.') + '</li>'
        + '</ul></div>'

        + c.deepdive_heading(t)
        + c.accordion(t, 1, 'L0 核心公理：四条最高优先级的铁律',
            'L0 core axioms: the four highest-priority iron rules',
            c.qa(t, '🧪 SOP 原文', 'Straight from the SOP',
                 c.codefile('memory/memory_management_sop.md', '0. ' + t('核心公理', 'Core Axioms'),
                     '<span class="kw">1.</span> ' + t('行动验证原则', 'Action-Verified Only') + ' — '
                     + t('只有“成功的工具调用结果”才能写入 L1/L2/L3。', 'only "successful tool-call results" may be written to L1/L2/L3.') + '\n'
                     '   <span class="cm"># No Execution, No Memory</span>\n'
                     '<span class="kw">2.</span> ' + t('神圣不可删改性', 'Sanctity of Verified Data') + ' — '
                     + t('已验证的配置/避坑指南重构时严禁丢弃，只能压缩或迁移层级。', 'verified config/pitfall notes may never be dropped on refactor — only compress or migrate.') + '\n'
                     '<span class="kw">3.</span> ' + t('禁止存储易变状态', 'No Volatile State') + ' — '
                     + t('时间戳、Session ID、PID、临时绝对路径一律不存。', 'no timestamps, session IDs, PIDs, or transient absolute paths.') + '\n'
                     '<span class="kw">4.</span> ' + t('最小充分指针', 'Minimum Sufficient Pointer') + ' — '
                     + t('上层只留能定位下层的最短标识，多一词即冗余。', 'upper layers keep only the shortest locator for the layer below; one extra word is redundant.')))
            + c.qa(t, '❓ 为什么 L0 是“公理”而不是代码', 'Why L0 is "axioms", not code',
                   '<p>' + t(
                       'L0 不是某个函数，而是一份<strong>给模型读的宪法</strong>。每次结算长期记忆时，'
                       '<span class="inline">do_start_long_term_update</span> 都会把这份 SOP 全文 '
                       '（<span class="inline">file_read(\'./memory/memory_management_sop.md\')</span>）作为工具结果回灌，'
                       '让模型在动手改记忆前先复诵铁律。约束写在数据里、由模型遵守，而不是写死在代码里——这正是“极简种子”的风格。',
                       'L0 is not a function but a <strong>constitution the model reads</strong>. Every long-term settlement, '
                       '<span class="inline">do_start_long_term_update</span> feeds the full SOP text back as a tool result '
                       '(<span class="inline">file_read(\'./memory/memory_management_sop.md\')</span>) so the model recites the iron rules before '
                       'touching memory. The constraints live in data and are honored by the model, not hard-coded — exactly the "minimal seed" style.') + '</p>'))
        + c.accordion(t, 2, 'L1→L2→L3→L4：真实文件与“指针→引用”导航链',
            'L1→L2→L3→L4: the real files and the "pointer → reference" chain',
            c.qa(t, '🧪 层级架构原文', 'The layer architecture, verbatim',
                 c.codefile('memory/memory_management_sop.md', t('记忆层级架构', 'Memory layer architecture'),
                     'L1: global_mem_insight.txt  '
                     '<span class="cm"># ' + t('极简索引层 - 严格 ≤30 行', 'minimal index layer - strictly ≤30 lines') + '</span>\n'
                     '    ↓ ' + t('导航指向', 'navigate to') + ' (Pointer)\n'
                     'L2: global_mem.txt          '
                     '<span class="cm"># ' + t('事实库层 - 现短但会膨胀', 'facts layer - short now, grows over time') + '</span>\n'
                     '    ↓ ' + t('详细引用', 'detailed reference') + ' (Reference)\n'
                     'L3: ../memory/              '
                     '<span class="cm"># ' + t('记录库层 - .md / .py 等', 'record layer - .md / .py files') + '</span>\n'
                     'L4: ../memory/L4_raw_sessions/  '
                     '<span class="cm"># ' + t('历史会话层 - 反射自动收集', 'session-history layer - auto-collected by reflection') + '</span>'))
            + c.qa(t, '🧪 真实落盘的文件', 'The real files on disk',
                 '<table class="t"><tr><th>' + t('层', 'Layer') + '</th><th>' + t('真实路径', 'Real path')
                 + '</th><th>' + t('内容', 'Content') + '</th></tr>'
                 + '<tr><td class="mono">L0</td><td class="mono">memory/memory_management_sop.md</td><td>'
                 + t('核心公理 + 各层职责', 'core axioms + per-layer duties') + '</td></tr>'
                 + '<tr><td class="mono">L1</td><td class="mono">memory/global_mem_insight.txt</td><td>'
                 + t('≤30 行索引（场景词→定位）+ RULES', '≤30-line index (scenario→locator) + RULES') + '</td></tr>'
                 + '<tr><td class="mono">L2</td><td class="mono">memory/global_mem.txt</td><td>'
                 + t('按 ## [SECTION] 组织的环境事实', 'environment facts under ## [SECTION]') + '</td></tr>'
                 + '<tr><td class="mono">L3</td><td class="mono">memory/*_sop.md, *.py</td><td>'
                 + t('plan_sop / verify_sop / keychain.py …', 'plan_sop / verify_sop / keychain.py …') + '</td></tr>'
                 + '<tr><td class="mono">L4</td><td class="mono">memory/L4_raw_sessions/</td><td>'
                 + t('compress_session.py / salient_mining_sop.md', 'compress_session.py / salient_mining_sop.md') + '</td></tr></table>')
            + c.qa(t, '⚙️ 一次导航怎么走', 'How one navigation flows',
                   '<p>' + t(
                       '每轮系统提示里只挂 L1 的 <span class="inline">global_mem_insight.txt</span>（≤30 行）。'
                       '模型看到某个场景关键词 → 顺“指针”决定去读 L2 的某个 <span class="inline">## [SECTION]</span> 拿事实，'
                       '或顺“引用”去 <span class="inline">ls memory/</span> 找对应的 <span class="inline">*_sop.md</span> 读详细步骤，'
                       '更老的上下文才去 L4 翻历史会话。<strong>常驻上下文只有索引，细节按需逐层下钻</strong>。',
                       'Each turn the system prompt only carries L1\'s <span class="inline">global_mem_insight.txt</span> (≤30 lines). '
                       'The model sees a scenario keyword → follows the "pointer" to read a <span class="inline">## [SECTION]</span> of L2 for facts, '
                       'or follows the "reference" to <span class="inline">ls memory/</span> and read the matching <span class="inline">*_sop.md</span> for '
                       'detailed steps; only older context reaches into L4 session history. <strong>Only the index stays resident; detail is drilled into '
                       'layer by layer on demand</strong>.') + '</p>'))
        + c.accordion(t, 3, '“最小充分指针”：为什么 L1 硬卡在 ≤30 行',
            'The "minimum sufficient pointer": why L1 is hard-capped at ≤30 lines',
            c.qa(t, '🧪 同步红线（反例 → 正例）', 'The sync red line (bad → good)',
                 c.codefile('memory/memory_management_sop.md', t('L1 ↔ L2/L3 同步规则', 'L1 ↔ L2/L3 sync rules'),
                     '<span class="cm"># ' + t('L1 只写关键词/名称，禁搬细节', 'L1 holds only keywords/names — never move detail up') + '</span>\n'
                     '❌ sop_name(' + t('场景A', 'caseA') + ':' + t('方法1+方法2+方法3', 'm1+m2+m3') + ')\n'
                     '✅ sop_name(' + t('场景A', 'caseA') + ')\n'
                     '<span class="cm"># ' + t('名字已自解释时连触发词都省略', 'when the name is self-explanatory, drop even the trigger word') + '</span>\n'
                     '❌ discord_slate_sop(' + t('Slate输入框', 'Slate input') + ')\n'
                     '✅ discord_slate_sop'))
            + c.qa(t, '❓ 为什么不把细节都写进索引', 'Why not put detail into the index',
                   '<p>' + t(
                       '索引是<strong>每轮都要进上下文</strong>的；它越胖，每轮越贵、噪声越多。'
                       '“最小充分指针”要求 L1 只回答“<strong>有没有这个能力 + 去哪找</strong>”，绝不回答“怎么做”。'
                       '怎么做属于 L3，用到时才 file_read。把索引压到 ≤30 行，是 GA 在 &lt;30K 上下文里仍“知道很多”的关键技巧。',
                       'The index goes <strong>into context every single turn</strong>; the fatter it is, the costlier and noisier each turn. '
                       'The "minimum sufficient pointer" requires L1 to answer only "<strong>does this capability exist + where to find it</strong>", '
                       'never "how to do it". The how-to belongs to L3 and is file_read only when needed. Squeezing the index to ≤30 lines is the key '
                       'trick that lets GA still "know a lot" within a &lt;30K context.') + '</p>')
            + c.qa(t, '🔀 对比：把一切塞进一个大记忆文件', 'vs cramming everything into one big memory file',
                   '<p>' + t(
                       '若把事实、步骤、历史全堆在一个文件里，每轮都要带着这坨东西，上下文迅速爆炸且充满无关信息。'
                       '分层 + 指针让“记得多”与“每轮只加载一点”不再矛盾——这正是 L0 第 4 条公理的工程兑现。',
                       'If facts, steps and history were all piled into one file, every turn would carry that lump, blowing up context with irrelevant '
                       'information. Layering + pointers makes "remember a lot" and "load only a little each turn" no longer contradictory — the '
                       'engineering payoff of L0\'s 4th axiom.') + '</p>'))

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像一本整理得很好的<strong>活页笔记</strong>：封面写着几条铁律（L0），第一页是目录（L1），'
            '后面是事实速查页（L2），再后面是一篇篇“怎么做某事”的食谱（L3），最后附着一摞旧日记（L4）。'
            '你平时只翻目录，需要时才按页码翻到具体那一篇。',
            'Like a well-organized <strong>loose-leaf notebook</strong>: the cover lists a few iron rules (L0), the '
            'first page is the table of contents (L1), then a facts cheat-sheet (L2), then "how to do X" recipes '
            '(L3), and finally a stack of old diaries (L4). You usually only read the contents page and flip to a '
            'specific recipe by its number when needed.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('五层：L0 铁律 · L1 索引 · L2 事实 · L3 技能/SOP · L4 会话归档。',
            'Five layers: L0 rules · L1 index · L2 facts · L3 skills/SOPs · L4 session archive.') + '</li>'
        + '<li>' + t('上层只放“最短指针”，按需顺着指针读下层细节。',
            'Upper layers hold only "the shortest pointer"; follow it to read lower-layer detail on demand.') + '</li>'
        + '<li>' + t('L3（memory/ 下的 SOP）就是技能真正存放的地方。',
            'L3 (the SOPs under memory/) is where skills actually live.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '分层的精髓是“<strong>最小充分指针</strong>”：每往上一层，只保留刚好够定位下一层的那点信息，多一个词都算冗余。'
            '正因为索引被压到 ≤ 30 行，GA 才能把“我知道很多东西”和“每次只加载一点点”这对矛盾同时满足——'
            '这也是它能在 &lt;30K 上下文里稳定工作的记忆侧根基。',
            'The essence of layering is the "<strong>minimum sufficient pointer</strong>": each layer up keeps just '
            'enough to locate the layer below — one extra word is redundancy. Because the index is squeezed to ≤ 30 '
            'lines, GA can satisfy both "I know a lot" and "I load only a little each time" at once — the memory-side '
            'foundation for working steadily within a &lt;30K context.',
        )
        + '</div>'
    )


def lesson_12(t):
    """记忆的读写与结晶 / Memory Read/Write & Crystallization."""
    return (
        '<p class="lead">'
        + t(
            '分好层只是“书架”，还得有人往上面记东西。GenericAgent 用<strong>两个记忆工具</strong>完成读写：'
            '一个是任务进行中的“工作便签”，一个是任务收尾时的“长期记忆结算”。前者防遗忘，后者把经验<strong>结晶</strong>成技能。',
            'Layering is just the "bookshelf"; something still has to write onto it. GenericAgent reads and writes '
            'memory with <strong>two memory tools</strong>: a "working notepad" during a task, and a "long-term '
            'memory settlement" when a task wraps up. The first prevents forgetting; the second '
            '<strong>crystallizes</strong> experience into skills.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '<strong>短期</strong>：<span class="inline">update_working_checkpoint</span> 把“用户要什么、关键约束”写进一个'
            '便签，之后每轮自动注入，防止长任务跑着跑着把目标跑丢。<strong>长期</strong>：'
            '<span class="inline">start_long_term_update</span> 在任务完成后启动“结算”，把<strong>经过行动验证</strong>的'
            '环境事实/用户偏好/踩坑经验，最小化地写进 L1/L2/L3。',
            '<strong>Short-term</strong>: <span class="inline">update_working_checkpoint</span> writes "what the user '
            'wants and the key constraints" onto a notepad that is auto-injected every turn, so a long task does not '
            'lose its goal along the way. <strong>Long-term</strong>: <span class="inline">start_long_term_update</span> '
            'kicks off a "settlement" after a task, writing <strong>action-verified</strong> environment facts, user '
            'preferences and hard-won lessons minimally into L1/L2/L3.',
        )
        + '</p></div>'

        + '<h2>' + t('从干活到记住', 'From doing to remembering') + '</h2>'
        + '<div class="flow">'
        + '<div class="node"><div class="nt">' + t('开始任务', 'Start task') + '</div>'
        + '<div class="nd">' + t('读 SOP', 'read SOP') + '</div></div>'
        + '<div class="arrow">→</div>'
        + '<div class="node hl"><div class="nt">update_working_checkpoint</div>'
        + '<div class="nd">' + t('记住目标与约束', 'capture goal & constraints') + '</div></div>'
        + '<div class="arrow">→</div>'
        + '<div class="node"><div class="nt">' + t('执行 / 验证', 'execute / verify') + '</div>'
        + '<div class="nd">' + t('每轮自动注入便签', 'notepad injected each turn') + '</div></div>'
        + '<div class="arrow">→</div>'
        + '<div class="node hl"><div class="nt">start_long_term_update</div>'
        + '<div class="nd">' + t('结晶进 L1/L2/L3', 'crystallize into L1/L2/L3') + '</div></div>'
        + '</div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('短期便签：', 'Short-term notepad: ')
        + '<span class="inline">ga.py: do_update_working_checkpoint</span>'
        + t(' 把 key_info / related_sop 写进 self.working，再由“锚点提示”每轮回灌给模型。',
            ' writes key_info / related_sop into self.working, then re-injects it via an "anchor prompt" each turn.') + '</li>'
        + '<li>' + t('长期结算：', 'Long-term settlement: ')
        + '<span class="inline">ga.py: do_start_long_term_update</span>'
        + t(' 注入一段提炼提示词，引导用 file_patch 最小化更新 L2 事实、同步 L1 索引、必要时精简 L3 SOP。',
            ' injects a distillation prompt that guides minimal file_patch updates to L2 facts, syncs the L1 index, '
            'and trims an L3 SOP when needed.') + '</li>'
        + '<li>' + t('结算受 L0 铁律约束：', 'Settlement obeys the L0 iron rules: ')
        + '<span class="inline">memory/memory_management_sop.md</span>'
        + t('——只记“行动验证成功”的信息，禁存易变状态，能不改就不 overwrite、宁愿少量 patch。',
            ' — only record "action-verified" info, never store volatile state, avoid overwrite and prefer small '
            'patches.') + '</li>'
        + '</ul></div>'

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '短期便签：do_update_working_checkpoint 与每轮回灌的锚点',
            'Short-term notepad: do_update_working_checkpoint and the anchor re-injected each turn',
            c.qa(t, '🧪 工具本体', 'The tool itself',
                 c.codefile('ga.py', 'GenericAgentHandler.do_update_working_checkpoint',
                     '<span class="kw">def</span> <span class="fn">do_update_working_checkpoint</span>(self, args, response):\n'
                     '    key_info = args.get(<span class="st">\'key_info\'</span>, <span class="st">\'\'</span>)\n'
                     '    related_sop = args.get(<span class="st">\'related_sop\'</span>, <span class="st">\'\'</span>)\n'
                     '    <span class="kw">if</span> <span class="st">\'key_info\'</span> <span class="kw">in</span> args: self.working[<span class="st">\'key_info\'</span>] = key_info\n'
                     '    <span class="kw">if</span> <span class="st">\'related_sop\'</span> <span class="kw">in</span> args: self.working[<span class="st">\'related_sop\'</span>] = related_sop\n'
                     '    <span class="kw">yield</span> <span class="st">\'[Info] Updated key_info and related_sop.\\n\'</span>\n'
                     '    next_prompt = self.<span class="fn">_get_anchor_prompt</span>(skip=args.get(<span class="st">\'_index\'</span>, <span class="nb">0</span>) &gt; <span class="nb">0</span>)\n'
                     '    <span class="kw">return</span> <span class="fn">StepOutcome</span>({<span class="st">\'result\'</span>: <span class="st">\'working key_info updated\'</span>}, next_prompt=next_prompt)'))
            + c.qa(t, '🧪 锚点提示如何回灌', 'How the anchor prompt re-injects it',
                 c.codefile('ga.py', 'GenericAgentHandler._get_anchor_prompt',
                     '<span class="kw">def</span> <span class="fn">_get_anchor_prompt</span>(self, skip=<span class="nb">False</span>):\n'
                     '    <span class="kw">if</span> skip: <span class="kw">return</span> <span class="st">\'\\n\'</span>\n'
                     '    prompt = f<span class="st">\'\\n### [WORKING MEMORY]\\n{earlier}&lt;history&gt;\\n{h_str}\\n&lt;/history&gt;\'</span>\n'
                     '    <span class="kw">if</span> self.working.get(<span class="st">\'key_info\'</span>):\n'
                     '        prompt += f<span class="st">\'\\n&lt;key_info&gt;{self.working.get(...)}&lt;/key_info&gt;\'</span>\n'
                     '    <span class="kw">return</span> prompt'))
            + c.qa(t, '⚙️ 为什么叫“便签”', 'Why a "notepad"',
                   '<p>' + t(
                       'checkpoint 把 key_info / related_sop 写进 <span class="inline">self.working</span>（一个普通 dict，进程级、不落盘）。'
                       '此后每个工具收尾都调 <span class="inline">_get_anchor_prompt()</span>，把 working memory 连同最近历史拼进 next_prompt——'
                       '于是这条“便签”<strong>每轮都被重新贴到模型眼前</strong>，长任务也不会忘掉当前重点。任务一结束，self.working 随之消失。',
                       'checkpoint writes key_info / related_sop into <span class="inline">self.working</span> (a plain dict, process-level, never '
                       'persisted). Afterwards every tool\'s wrap-up calls <span class="inline">_get_anchor_prompt()</span>, splicing the working memory '
                       'plus recent history into next_prompt — so this "note" is <strong>re-posted in front of the model every turn</strong>, and even '
                       'long tasks do not forget the current focus. When the task ends, self.working vanishes with it.') + '</p>'))
        + c.accordion(t, 2, '长期结晶：do_start_long_term_update 的蒸馏提示词',
            'Long-term crystallization: the distillation prompt of do_start_long_term_update',
            c.qa(t, '🧪 注入的蒸馏提示', 'The injected distillation prompt',
                 c.codefile('ga.py', 'GenericAgentHandler.do_start_long_term_update',
                     '<span class="kw">def</span> <span class="fn">do_start_long_term_update</span>(self, args, response):\n'
                     '    prompt = <span class="st">\'\'\'### [' + t('总结提炼经验', 'Distill experience') + '] ...\n'
                     '- ' + t('环境事实（路径/凭证/配置）', 'environment facts (paths/creds/config)') + ' → file_patch ' + t('更新 L2，同步 L1', 'update L2, sync L1') + '\n'
                     '- ' + t('复杂任务经验（关键坑点/前置条件）', 'complex-task experience (pitfalls/preconditions)') + ' → L3 ' + t('精简 SOP', 'trimmed SOP') + '\n'
                     '\'\'\'</span> + <span class="fn">get_global_memory</span>()\n'
                     '    path = <span class="st">\'./memory/memory_management_sop.md\'</span>\n'
                     '    result = <span class="st">\'This is L0:\\n\'</span> + <span class="fn">file_read</span>(path, show_linenos=<span class="nb">False</span>)\n'
                     '    <span class="kw">return</span> <span class="fn">StepOutcome</span>(result, next_prompt=prompt)'))
            + c.qa(t, '⚙️ 结晶的三个动作', 'The three crystallization actions',
                   '<p>' + t(
                       '这个工具本身<strong>不写记忆</strong>，它只是“开启结算”：把 L0 全文作为工具结果回灌，并附上一段蒸馏提示词，'
                       '引导模型自己用普通文件工具完成三件事——① 环境事实用 <span class="inline">file_patch</span> 最小更新 L2、同步 L1 索引；'
                       '② 复杂任务经验写成 L3 的精简 SOP；③ 无新增内容就跳过。真正动手改文件的是模型，不是这段代码。',
                       'The tool itself <strong>writes no memory</strong>; it just "opens the settlement": it feeds the full L0 back as a tool result '
                       'with a distillation prompt, guiding the model to do three things with ordinary file tools — ① minimally update L2 facts via '
                       '<span class="inline">file_patch</span> and sync the L1 index; ② write complex-task experience as a trimmed L3 SOP; ③ skip if there '
                       'is nothing new. The model, not this code, actually edits the files.') + '</p>')
            + c.qa(t, '🔀 checkpoint vs long_term_update', 'checkpoint vs long_term_update',
                   '<table class="t"><tr><th></th><th>' + t('短期便签', 'Notepad') + '</th><th>' + t('长期结晶', 'Crystallize') + '</th></tr>'
                   + '<tr><td>' + t('存哪', 'Where') + '</td><td class="mono">self.working</td><td class="mono">memory/*.txt,*.md</td></tr>'
                   + '<tr><td>' + t('生命期', 'Lifetime') + '</td><td>' + t('单个任务内', 'within one task') + '</td><td>' + t('跨会话永久', 'across sessions, permanent') + '</td></tr>'
                   + '<tr><td>' + t('触发', 'Trigger') + '</td><td>' + t('任务开始/中途', 'task start / midway') + '</td><td>' + t('任务完成后', 'after task completion') + '</td></tr>'
                   + '<tr><td>' + t('落盘', 'Persisted') + '</td><td>' + t('否', 'no') + '</td><td>' + t('是（最小 patch）', 'yes (minimal patch)') + '</td></tr></table>'))
        + c.accordion(t, 3, 'L0 铁律如何守住结晶质量',
            'How the L0 iron rules guard crystallization quality',
            c.qa(t, '🧪 蒸馏提示里的禁止项', 'The "forbidden" list in the distillation prompt',
                 c.codefile('ga.py', 'do_start_long_term_update (prompt)',
                     '<span class="cm"># ' + t('如果没有经验证的、未来能用上的信息，忽略本次调用！', 'If there is no verified, future-useful info, ignore this call!') + '</span>\n'
                     '<span class="cm"># ' + t('只能提取行动验证成功的信息', 'Only extract action-verified info') + '</span>\n'
                     '<span class="kw">' + t('禁止', 'Forbidden') + '</span>: ' + t('临时变量 / 具体推理过程 / 未验证信息 / 通用常识 / 只是做了但没验证的信息',
                         'temp vars / reasoning traces / unverified info / general knowledge / things done but not verified') + '\n'
                     '<span class="cm"># ' + t('先 file_read 看现有 → 判断类型 → 最小化更新 → 无新内容跳过', 'file_read first → classify → minimal update → skip if nothing new') + '</span>'))
            + c.qa(t, '❓ 为什么“无行动不记忆”如此重要', 'Why "no execution, no memory" matters so much',
                   '<p>' + t(
                       '模型的“固有知识”和“推理猜测”可能是错的，一旦当事实写进记忆，下次会被当真，错误会<strong>复利累积</strong>。'
                       'L0 第 1 条强制：只有工具调用<strong>真正成功</strong>的结论才配结晶。这条铁律把记忆库守成“越用越准”而不是“越用越脏”，'
                       '是自进化技能树能被反复信任的根基。',
                       'A model\'s "inherent knowledge" and "reasoning guesses" can be wrong; once written as facts they are taken as true next time, '
                       'and errors <strong>compound</strong>. L0 rule 1 enforces: only conclusions from <strong>genuinely successful</strong> tool calls '
                       'deserve to crystallize. This iron rule keeps the store "more accurate the more you use it" rather than "dirtier" — the foundation '
                       'that makes the self-evolving skill tree repeatedly trustworthy.') + '</p>')
            + c.qa(t, '⚠️ 坑点：改记忆要“宁可不改”', 'Pitfall: when editing memory, "rather not edit"',
                   '<p>' + t(
                       'L0 第 2 条明确：“记忆修改时请极度小心，尽量不要 overwrite 或 code run，只能少量 patch，改不动宁愿不改。”'
                       '所以结晶时优先 <span class="inline">file_read</span> 看现有内容，再用 <span class="inline">file_patch</span> 做最小局部修改，'
                       '严禁用 code_run 批量重写整个记忆文件——那样极易误删已验证的避坑信息。',
                       'L0 rule 2 is explicit: "edit memory with extreme care, avoid overwrite or code_run, only small patches, and rather not edit if you '
                       'cannot." So crystallization prefers <span class="inline">file_read</span> to see existing content, then a minimal local '
                       '<span class="inline">file_patch</span>; never bulk-rewrite the whole memory file with code_run — that easily deletes already-verified '
                       'pitfall notes.') + '</p>'))

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像做实验时<strong>手边的草稿纸 + 事后的实验记录本</strong>：草稿纸（工作便签）随手记当前要点，做完一组就擦；'
            '只有<strong>真正验证成功</strong>的结论，才郑重地誊进永久的记录本（长期记忆）。没验证过的猜测，绝不入册。',
            'Like doing experiments with a <strong>scratch pad at hand plus a lab notebook afterward</strong>: the '
            'scratch pad (working notepad) jots current points and gets wiped after each batch; only conclusions that '
            'were <strong>actually verified</strong> are carefully transcribed into the permanent notebook (long-term '
            'memory). Unverified guesses never make it in.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('两个记忆工具：working_checkpoint（短期、每轮注入）与 start_long_term_update（长期结晶）。',
            'Two memory tools: working_checkpoint (short-term, injected each turn) and start_long_term_update (long-term crystallization).') + '</li>'
        + '<li>' + t('铁律：无行动，不记忆——只结晶经过验证的信息。',
            'The iron rule: no execution, no memory — only crystallize verified information.') + '</li>'
        + '<li>' + t('写记忆要最小化：优先小 patch，禁存易变状态。',
            'Write memory minimally: prefer small patches, never store volatile state.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '“<strong>无行动，不记忆</strong>”这条铁律，是 GA 记忆可信的关键。模型的“固有知识”“推理猜测”一律不准当事实写入——'
            '只有工具调用真正成功的结论才配结晶成技能。正是这条原则，把记忆库守成了“越用越准”而不是“越用越脏”，'
            '也让后面“自进化”长出的技能树根基扎实、可被反复信任。',
            'The iron rule "<strong>no execution, no memory</strong>" is what makes GA\'s memory trustworthy. A '
            'model\'s "inherent knowledge" and "reasoning guesses" may never be written as facts — only conclusions '
            'from genuinely successful tool calls deserve to crystallize into skills. This very principle keeps the '
            'memory store "more accurate the more you use it" rather than "dirtier", giving the later "self-evolution" '
            'skill tree a solid, repeatedly trustworthy foundation.',
        )
        + '</div>'
    )


def lesson_13(t):
    """钩子与可观测性 / Hooks & Observability."""
    return (
        '<p class="lead">'
        + t(
            '想知道每一轮花了多少 token、想给某个工具加一道审计、想接入追踪系统——又不想去改那 100 行核心循环？'
            'GenericAgent 用一套<strong>钩子（hooks）</strong>解决：循环在每个关键时刻“喊一嗓子”，插件们各自接住。',
            'Want to know how many tokens each turn cost, add an audit to a tool, or wire in a tracing system — '
            'without touching the 100-line core loop? GenericAgent solves it with <strong>hooks</strong>: the loop '
            '"calls out" at every key moment, and plugins catch the calls.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '钩子是一种<strong>发布 / 订阅</strong>机制：核心循环在固定的时间点触发事件（agent / turn / llm / tool 的 '
            'before / after），任何插件都能注册回调来“收听”。核心代码完全不知道有谁在听——这就是“零耦合扩展”。',
            'Hooks are a <strong>publish/subscribe</strong> mechanism: the core loop fires events at fixed points '
            '(the before/after of agent / turn / llm / tool), and any plugin can register a callback to "listen". '
            'The core has no idea who is listening — that is "zero-coupling extension".',
        )
        + '</p></div>'

        + '<div class="codefile"><div class="cf-head"><span class="dot"></span>'
        + '<span class="path">plugins/hooks.py</span><span class="ln">register / trigger</span></div>'
        + '<pre>'
        + '<span class="cm"># ' + t('插件侧：注册一个回调', 'plugin side: register a callback') + '</span>\n'
        + '<span class="kw">@hooks.register</span>(<span class="st">\'llm_after\'</span>)\n'
        + '<span class="kw">def</span> <span class="fn">on_llm_after</span>(ctx):\n'
        + '    ...  <span class="cm"># ' + t('读 ctx，可返回修改后的 ctx', 'read ctx, may return a modified ctx') + '</span>\n'
        + '\n'
        + '<span class="cm"># ' + t('核心侧：循环在关键点触发事件', 'core side: the loop fires events at key points') + '</span>\n'
        + 'trigger(<span class="st">\'llm_after\'</span>, ctx)  <span class="cm"># ' + t('在 agent_loop.py 里写作 _hook(...)', 'written as _hook(...) inside agent_loop.py') + '</span>\n'
        + '</pre></div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('机制在 ', 'The mechanism is in ')
        + '<span class="inline">plugins/hooks.py</span>'
        + t('：register(event) 装饰器登记回调，trigger(event, ctx) 依次调用；',
            ': the register(event) decorator registers a callback, trigger(event, ctx) calls them in turn;') + '</li>'
        + '<li>' + t('循环里成对触发这些事件：', 'The loop fires these events in pairs: ')
        + '<span class="inline">agent_before/after · turn_before/after · llm_before/after · tool_before/after</span>'
        + t('（见 agent_loop.py 里的 _hook 调用与 dispatch）。',
            ' (see the _hook calls in agent_loop.py and dispatch).') + '</li>'
        + '<li>' + t('插件自动发现：', 'Plugins are auto-discovered: ')
        + '<span class="inline">discover_and_load</span>'
        + t(' 扫描 plugins/ 目录加载模块；', ' scans the plugins/ directory and loads modules; ')
        + '<span class="inline">plugins/langfuse_tracing.py</span>'
        + t(' 就是个现成例子——它注册到上述事件，做调用追踪与 token 用量统计。',
            ' is a ready example — it registers on those events to do call tracing and token-usage accounting.') + '</li>'
        + '</ul></div>'

        + c.deepdive_heading(t)
        + c.accordion(t, 1, 'register / trigger：发布-订阅的全部实现',
            'register / trigger: the entire pub-sub implementation',
            c.qa(t, '🧪 注册表 + 装饰器 + 触发', 'Registry + decorator + trigger',
                 c.codefile('plugins/hooks.py', 'register / trigger',
                     '_registry = {}  <span class="cm"># ' + t('event_name -&gt; [callback, ...]', 'event_name -&gt; [callback, ...]') + '</span>\n\n'
                     '<span class="kw">def</span> <span class="fn">register</span>(event):\n'
                     '    <span class="kw">def</span> <span class="fn">decorator</span>(fn):\n'
                     '        _registry.setdefault(event, []).<span class="fn">append</span>(fn); <span class="kw">return</span> fn\n'
                     '    <span class="kw">return</span> decorator\n\n'
                     '<span class="kw">def</span> <span class="fn">trigger</span>(event, ctx: dict):\n'
                     '    <span class="kw">for</span> fn <span class="kw">in</span> _registry.get(event, []):\n'
                     '        <span class="kw">try</span>:\n'
                     '            r = fn(ctx)\n'
                     '            <span class="kw">if</span> isinstance(r, dict): ctx = r  <span class="cm"># ' + t('回调可返回修改后的 ctx', 'callback may return a modified ctx') + '</span>\n'
                     '        <span class="kw">except</span> Exception <span class="kw">as</span> e:\n'
                     '            sys.stderr.<span class="fn">write</span>(f<span class="st">\'[hooks] {event} callback error: {e}\\n\'</span>)\n'
                     '    <span class="kw">return</span> ctx'))
            + c.qa(t, '❓ 回调返回 dict 意味着什么', 'What returning a dict means',
                   '<p>' + t(
                       '<span class="inline">trigger</span> 不只是“通知”，它还能<strong>改写上下文</strong>：若某回调返回一个 dict，'
                       '该 dict 就成为后续回调（以及触发点）看到的新 ctx。这让钩子既能做只读的观测（追踪、计时），'
                       '也能做轻度干预（改 messages、注入提示）。回调里抛异常会被 try 兜住并打到 stderr，<strong>绝不波及主循环</strong>。',
                       '<span class="inline">trigger</span> is not just "notify" — it can <strong>rewrite context</strong>: if a callback returns a dict, '
                       'that dict becomes the new ctx seen by later callbacks (and the trigger site). This lets hooks do read-only observation (tracing, '
                       'timing) or light intervention (edit messages, inject prompts). An exception in a callback is caught by the try and printed to '
                       'stderr, <strong>never disturbing the main loop</strong>.') + '</p>'))
        + c.accordion(t, 2, '八个事件：在 agent_loop.py 里何时被 _hook 触发',
            'The eight events: when _hook fires them in agent_loop.py',
            c.qa(t, '🧪 触发点', 'The trigger sites',
                 c.codefile('agent_loop.py', t('循环内的 _hook 调用', '_hook calls inside the loop'),
                     '_hook(<span class="st">\'agent_before\'</span>, locals())   <span class="cm"># ' + t('循环开始前', 'before the loop') + '</span>\n'
                     '<span class="kw">while</span> turn &lt; handler.max_turns:\n'
                     '    _hook(<span class="st">\'turn_before\'</span>, locals())\n'
                     '    _hook(<span class="st">\'llm_before\'</span>, locals())\n'
                     '    response = <span class="kw">yield from</span> client.<span class="fn">chat</span>(...)\n'
                     '    _hook(<span class="st">\'llm_after\'</span>, locals())\n'
                     '    <span class="cm"># ' + t('dispatch 内: tool_before / tool_after', 'inside dispatch: tool_before / tool_after') + '</span>\n'
                     '    _hook(<span class="st">\'turn_after\'</span>, locals())\n'
                     '_hook(<span class="st">\'agent_after\'</span>, locals())  <span class="cm"># ' + t('循环结束后', 'after the loop') + '</span>'))
            + c.qa(t, '⚙️ 四对成对事件', 'Four paired events',
                   '<table class="t"><tr><th>' + t('事件对', 'Event pair') + '</th><th>' + t('包住什么', 'Wraps what') + '</th><th>' + t('ctx 里有', 'ctx carries') + '</th></tr>'
                   + '<tr><td class="mono">agent_before/after</td><td>' + t('整个任务', 'the whole task') + '</td><td class="mono">user_input / exit_reason</td></tr>'
                   + '<tr><td class="mono">turn_before/after</td><td>' + t('单轮', 'one turn') + '</td><td class="mono">turn / messages</td></tr>'
                   + '<tr><td class="mono">llm_before/after</td><td>' + t('一次模型调用', 'one model call') + '</td><td class="mono">messages / response</td></tr>'
                   + '<tr><td class="mono">tool_before/after</td><td>' + t('一次工具执行（dispatch 内）', 'one tool run (in dispatch)') + '</td><td class="mono">tool_name / args / ret</td></tr></table>')
            + c.qa(t, '🧪 ImportError 的优雅降级', 'Graceful fallback on ImportError',
                 c.codefile('agent_loop.py', t('文件顶部', 'top of file'),
                     '<span class="kw">try</span>: <span class="kw">from</span> plugins.hooks <span class="kw">import</span> trigger <span class="kw">as</span> _hook\n'
                     '<span class="kw">except</span> ImportError: _hook = <span class="kw">lambda</span> *a, **k: None'))
            )
        + c.accordion(t, 3, '自动发现与一个真实插件：langfuse_tracing',
            'Auto-discovery and a real plugin: langfuse_tracing',
            c.qa(t, '🧪 discover_and_load', 'discover_and_load',
                 c.codefile('plugins/hooks.py', 'discover_and_load',
                     '<span class="kw">def</span> <span class="fn">discover_and_load</span>(plugin_dir=None):\n'
                     '    ...\n'
                     '    <span class="kw">for</span> fn <span class="kw">in</span> sorted(os.<span class="fn">listdir</span>(plugin_dir)):\n'
                     '        <span class="kw">if</span> fn.startswith(<span class="st">\'_\'</span>) <span class="kw">or</span> <span class="kw">not</span> fn.endswith(<span class="st">\'.py\'</span>): <span class="kw">continue</span>\n'
                     '        <span class="fn">load</span>(fn[:-<span class="nb">3</span>])  <span class="cm"># ' + t('import 即触发 register', 'importing triggers register') + '</span>'))
            + c.qa(t, '🧪 插件如何挂上事件', 'How the plugin hangs onto events',
                 c.codefile('plugins/langfuse_tracing.py', '@hooks.register',
                     '<span class="nb">@hooks.register</span>(<span class="st">\'agent_before\'</span>)\n'
                     '<span class="kw">def</span> <span class="fn">_on_agent_before</span>(ctx):\n'
                     '    _tls.trace_obs = _lf.<span class="fn">start_observation</span>(name=<span class="st">\'agent.task\'</span>, as_type=<span class="st">\'agent\'</span>,\n'
                     '        input={<span class="st">\'user_input\'</span>: ctx.get(<span class="st">\'user_input\'</span>, <span class="st">\'\'</span>)})\n\n'
                     '<span class="nb">@hooks.register</span>(<span class="st">\'tool_before\'</span>)\n'
                     '<span class="kw">def</span> <span class="fn">_on_tool_before</span>(ctx):\n'
                     '    name = ctx.get(<span class="st">\'tool_name\'</span>, <span class="st">\'?\'</span>)\n'
                     '    _tls.tstack.<span class="fn">append</span>(_lf.<span class="fn">start_observation</span>(name=name, as_type=<span class="st">\'tool\'</span>, input=args))'))
            + c.qa(t, '⚙️ 零侵入的可观测性', 'Zero-intrusion observability',
                   '<p>' + t(
                       '<span class="inline">langfuse_tracing.py</span> 在 import 时若发现 mykey 里有 langfuse_config 就自激活，'
                       '并用 <span class="inline">@hooks.register</span> 挂到 agent/llm/tool 三对事件上，把每次任务/模型调用/工具执行变成一条 trace span。'
                       '核心循环对此<strong>一无所知</strong>——删掉这个插件，agent 照常运行。这就是钩子机制“对扩展开放、对核心封闭”的兑现。',
                       '<span class="inline">langfuse_tracing.py</span> self-activates on import if mykey has a langfuse_config, hanging onto the '
                       'agent/llm/tool event pairs via <span class="inline">@hooks.register</span> to turn each task/model-call/tool-run into a trace span. '
                       'The core loop <strong>knows nothing</strong> about it — delete the plugin and the agent runs just the same. That is the hook '
                       'mechanism delivering "open to extension, closed at the core".') + '</p>'))

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像生产线上的<strong>质检探头</strong>：流水线该怎么走还怎么走，你只是在“上料前 / 下料后”这些节点装上探头，'
            '需要时取数、记录、甚至微调一下零件。要不要装、装几个，都不影响流水线本身的运转。',
            'Like <strong>inspection probes</strong> on an assembly line: the line runs exactly as before; you merely '
            'clamp probes onto nodes like "before loading / after unloading" to read data, log, or even tweak a part '
            'when needed. Whether you add probes, and how many, does not affect how the line itself runs.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('钩子 = 发布/订阅；核心循环触发事件，插件注册回调收听。',
            'Hooks = pub/sub; the core loop fires events, plugins register callbacks to listen.') + '</li>'
        + '<li>' + t('八个事件：agent / turn / llm / tool 的 before / after。',
            'Eight events: the before / after of agent / turn / llm / tool.') + '</li>'
        + '<li>' + t('plugins/ 目录自动加载；langfuse_tracing.py 是现成的追踪插件。',
            'The plugins/ directory is auto-loaded; langfuse_tracing.py is a ready-made tracing plugin.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '钩子回调<strong>可以返回一个修改后的 ctx</strong>——所以它不只是“旁观”，还能“改写”流经的上下文。'
            '这让可观测性与轻量扩展用<strong>同一套机制</strong>实现：既能默默记账，也能在不动核心的前提下调整行为。'
            '核心循环始终只有 100 行，能力却能从外面一层层叠加上去。',
            'A hook callback <strong>can return a modified ctx</strong> — so it does more than "observe"; it can '
            '"rewrite" the context flowing through. This lets observability and lightweight extension share <strong>one '
            'mechanism</strong>: quietly keep accounts, or adjust behavior without touching the core. The core loop '
            'stays 100 lines, yet capabilities can be layered on from the outside.',
        )
        + '</div>'
    )


def lesson_14(t):
    """上下文工程与 Token 效率 / Context Engineering & Token Efficiency."""
    return (
        '<p class="lead">'
        + t(
            '别的 Agent 动辄吞下 200K–1M 的上下文，GenericAgent 却把自己控制在 <strong>&lt;30K</strong> 以内。'
            '上下文小，不只是省钱——更意味着<strong>噪声更少、幻觉更少、成功率更高</strong>。这一课看 GA 是怎么做到的。',
            'Other agents swallow 200K–1M tokens of context; GenericAgent keeps itself under <strong>&lt;30K</strong>. '
            'A small context is not just cheaper — it means <strong>less noise, fewer hallucinations, and a higher '
            'success rate</strong>. This lesson shows how GA pulls it off.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            'GA 的省 token 不是某一个开关，而是一整套“<strong>只留当下需要的</strong>”的习惯：历史不堆进 messages、'
            '展示给模型的内容会被压缩、长长的工具参数会被精简、工具描述每隔几轮重置一次。再加上分层记忆与工作便签托底，'
            '“忘掉原始历史”反而不丢关键信息。',
            'GA\'s token thrift is not a single switch but a whole set of "<strong>keep only what is needed now</strong>" '
            'habits: history is not piled into messages, content shown to the model is compacted, long tool arguments '
            'are trimmed, and tool descriptions reset every few turns. Backed by layered memory and the working '
            'notepad, "forgetting raw history" loses nothing essential.',
        )
        + '</p></div>'

        + '<h2>' + t('几招压上下文', 'A few ways to shrink context') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('手段', 'Technique') + '</th><th>' + t('做什么', 'What it does') + '</th>'
        + '<th>' + t('在哪', 'Where') + '</th></tr>'
        + '<tr><td>' + t('只带新消息', 'Only the new message') + '</td><td>'
        + t('每轮 messages 只放本轮新增内容，历史交给 Session。',
            'Each turn\'s messages hold only what is new; history goes to the Session.')
        + '</td><td class="mono">agent_loop.py</td></tr>'
        + '<tr><td>' + t('压缩展示内容', 'Compact the display') + '</td><td>'
        + t('把大代码块缩成预览、去掉 file_content/tool 标签、合并空行。',
            'Shrink big code blocks to a preview, strip file_content/tool tags, collapse blank lines.')
        + '</td><td class="mono">_clean_content</td></tr>'
        + '<tr><td>' + t('精简工具参数', 'Trim tool args') + '</td><td>'
        + t('在日志/展示里把冗长参数压短（如只留文件名）。',
            'Shorten verbose args in logs/display (e.g. keep just the file name).')
        + '</td><td class="mono">_compact_tool_args</td></tr>'
        + '<tr><td>' + t('周期性重置', 'Periodic reset') + '</td><td>'
        + t('每 10 轮清空一次工具描述，避免重复占位。',
            'Clear the tool descriptions every 10 turns to avoid repeated bulk.')
        + '</td><td class="mono">turn % 10 == 0</td></tr>'
        + '<tr><td>' + t('压缩历史标签', 'Compress history') + '</td><td>'
        + t('对较旧的消息做标签压缩 / 截断，保留最近若干轮。',
            'Tag-compress / truncate older messages, keeping the most recent turns.')
        + '</td><td class="mono">compress_history_tags</td></tr>'
        + '</table>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('展示压缩在 ', 'Display compaction is in ')
        + '<span class="inline">agent_loop.py: _clean_content</span>'
        + t('：超过 6 行的代码块只留前 5 行 + “(N lines)”，并清掉 &lt;file_content&gt; / &lt;tool_use&gt; 等标签。',
            ': code blocks over 6 lines keep the first 5 + "(N lines)", and &lt;file_content&gt; / &lt;tool_use&gt; '
            'tags are stripped.') + '</li>'
        + '<li>' + t('参数精简在 ', 'Argument trimming is in ')
        + '<span class="inline">agent_loop.py: _compact_tool_args</span>'
        + t('（如把 path 只显示 basename，超长则截断）。',
            ' (e.g. show only the basename of path, truncate when over-long).') + '</li>'
        + '<li>' + t('工具描述的周期重置：', 'Periodic tool-desc reset: ')
        + '<span class="inline">if turn % 10 == 0: client.last_tools = \'\'</span>'
        + t('，在循环里。', ', in the loop.') + '</li>'
        + '<li>' + t('历史侧压缩在 ', 'History-side compression is in ')
        + '<span class="inline">llmcore.py: compress_history_tags / trim_messages_history</span>'
        + t('（保留最近若干轮，压缩/截断更早的内容）。',
            ' (keep the latest turns, compress/truncate earlier content).') + '</li>'
        + '</ul></div>'

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '_clean_content：把展示内容“缩骨”',
            '_clean_content: shrinking what gets displayed',
            c.qa(t, '🧪 真实实现', 'The real implementation',
                 c.codefile('agent_loop.py', '_clean_content',
                     '<span class="kw">def</span> <span class="fn">_clean_content</span>(text):\n'
                     '    <span class="kw">def</span> <span class="fn">_shrink_code</span>(m):\n'
                     '        body = [l <span class="kw">for</span> l <span class="kw">in</span> lines[<span class="nb">1</span>:-<span class="nb">1</span>] <span class="kw">if</span> l.strip()]\n'
                     '        <span class="kw">if</span> len(body) &lt;= <span class="nb">6</span>: <span class="kw">return</span> m.group(<span class="nb">0</span>)\n'
                     '        preview = <span class="st">\'\\n\'</span>.<span class="fn">join</span>(body[:<span class="nb">5</span>])\n'
                     '        <span class="kw">return</span> f<span class="st">\'```{lang}\\n{preview}\\n  ... ({len(body)} lines)\\n```\'</span>\n'
                     '    text = re.<span class="fn">sub</span>(r<span class="st">\'```[\\s\\S]*?```\'</span>, _shrink_code, text)\n'
                     '    <span class="kw">for</span> p <span class="kw">in</span> [r<span class="st">\'&lt;file_content&gt;[\\s\\S]*?&lt;/file_content&gt;\'</span>,\n'
                     '              r<span class="st">\'&lt;tool_(?:use|call)&gt;[\\s\\S]*?&lt;/tool_(?:use|call)&gt;\'</span>, r<span class="st">\'(\\r?\\n){3,}\'</span>]:\n'
                     '        text = re.<span class="fn">sub</span>(p, ..., text)\n'
                     '    <span class="kw">return</span> text.strip()'))
            + c.qa(t, '⚙️ 三步缩骨', 'Three shrinking steps',
                   '<p>' + t(
                       '① 任何代码块若<strong>非空行超过 6 行</strong>，只留前 5 行再加一句 <span class="inline">... (N lines)</span>；'
                       '② 删掉 <span class="inline">&lt;file_content&gt;</span> 与 <span class="inline">&lt;tool_use|tool_call&gt;</span> 整块；'
                       '③ 三个以上连续换行压成两个。注意它只用于 <strong>verbose=False</strong> 的展示路径，目的是让终端输出干净、不刷屏。',
                       '① any code block whose <strong>non-empty lines exceed 6</strong> keeps only the first 5 plus a '
                       '<span class="inline">... (N lines)</span> line; ② strip whole <span class="inline">&lt;file_content&gt;</span> and '
                       '<span class="inline">&lt;tool_use|tool_call&gt;</span> blocks; ③ collapse 3+ consecutive newlines into two. Note it only runs on the '
                       '<strong>verbose=False</strong> display path, to keep terminal output clean and unflooded.') + '</p>'))
        + c.accordion(t, 2, '_compact_tool_args：参数也要瘦身',
            '_compact_tool_args: trimming the args too',
            c.qa(t, '🧪 真实实现', 'The real implementation',
                 c.codefile('agent_loop.py', '_compact_tool_args',
                     '<span class="kw">def</span> <span class="fn">_compact_tool_args</span>(name, args):\n'
                     '    a = {k: v <span class="kw">for</span> k, v <span class="kw">in</span> args.items() <span class="kw">if</span> k != <span class="st">\'_index\'</span>}\n'
                     '    <span class="kw">for</span> k <span class="kw">in</span> (<span class="st">\'path\'</span>,):\n'
                     '        <span class="kw">if</span> k <span class="kw">in</span> a: a[k] = os.path.<span class="fn">basename</span>(a[k])\n'
                     '    <span class="kw">if</span> name == <span class="st">\'update_working_checkpoint\'</span>:\n'
                     '        s = a.get(<span class="st">\'key_info\'</span>, <span class="st">\'\'</span>); <span class="kw">return</span> (s[:<span class="nb">60</span>]+<span class="st">\'...\'</span>) <span class="kw">if</span> len(s)&gt;<span class="nb">60</span> <span class="kw">else</span> s\n'
                     '    s = json.<span class="fn">dumps</span>(a, ensure_ascii=<span class="nb">False</span>)\n'
                     '    <span class="kw">return</span> (s[:<span class="nb">120</span>]+<span class="st">\'...\'</span>) <span class="kw">if</span> len(s)&gt;<span class="nb">120</span> <span class="kw">else</span> s'))
            + c.qa(t, '⚙️ 为什么要精简参数显示', 'Why compact the arg display',
                   '<p>' + t(
                       '工具参数里常有长绝对路径、整段脚本。展示时 <span class="inline">_compact_tool_args</span> 把 <span class="inline">path</span> 只留 basename、'
                       '整体 JSON 超 120 字就截断，并对 <span class="inline">update_working_checkpoint</span>、<span class="inline">ask_user</span> 等做专门精简。'
                       '它服务于 <span class="inline">verbose=False</span> 下 <span class="inline">🛠️ name(args)</span> 这一行——既能一眼看清在调什么，又不把屏幕撑爆。',
                       'Tool args often hold long absolute paths or whole scripts. For display, <span class="inline">_compact_tool_args</span> keeps only the '
                       'basename of <span class="inline">path</span>, truncates the overall JSON past 120 chars, and special-cases tools like '
                       '<span class="inline">update_working_checkpoint</span> and <span class="inline">ask_user</span>. It serves the '
                       '<span class="inline">🛠️ name(args)</span> line under <span class="inline">verbose=False</span> — readable at a glance without blowing up the screen.') + '</p>')
            + c.qa(t, '⚠️ 坑点：只是显示层，不改实际参数', 'Pitfall: display-only, not the real args',
                   '<p>' + t(
                       '<span class="inline">_clean_content</span> 与 <span class="inline">_compact_tool_args</span> 都只影响<strong>给人看的输出</strong>，'
                       '不会改写真正发给工具的 args，也不改发给模型的历史。真正省 token 的“历史压缩”在 llmcore 那一侧（下一个折叠）。'
                       '别把这两者误当成上下文压缩——它们是“终端整洁术”。',
                       'Both <span class="inline">_clean_content</span> and <span class="inline">_compact_tool_args</span> affect only the '
                       '<strong>human-facing output</strong>; they never rewrite the real args passed to a tool, nor the history sent to the model. The '
                       'real token-saving "history compression" lives on the llmcore side (next accordion). Do not mistake these two for context '
                       'compression — they are the "tidy-terminal" art.') + '</p>'))
        + c.accordion(t, 3, '历史侧才是真省 token：compress_history_tags / trim_messages_history',
            'The real token saver is history-side: compress_history_tags / trim_messages_history',
            c.qa(t, '🧪 周期压缩旧消息', 'Periodically compress older messages',
                 c.codefile('llmcore.py', 'compress_history_tags',
                     '<span class="kw">def</span> <span class="fn">compress_history_tags</span>(messages, keep_recent=<span class="nb">10</span>, max_len=<span class="nb">800</span>, force=<span class="nb">False</span>, interval=<span class="nb">5</span>):\n'
                     '    <span class="kw">if</span> compress_history_tags._cd % interval != <span class="nb">0</span>: <span class="kw">return</span> messages\n'
                     '    <span class="kw">for</span> i, msg <span class="kw">in</span> enumerate(messages):\n'
                     '        <span class="kw">if</span> i &gt;= len(messages) - keep_recent: <span class="kw">break</span>  <span class="cm"># ' + t('最近若干轮不动', 'leave the latest turns untouched') + '</span>\n'
                     '        <span class="cm"># ' + t('把 &lt;thinking&gt;/&lt;tool_use&gt;/&lt;tool_result&gt; 等标签内容截断', 'truncate content inside thinking/tool_use/tool_result tags') + '</span>'))
            + c.qa(t, '🧪 超额就丢最老的', 'Drop the oldest when over budget',
                 c.codefile('llmcore.py', 'trim_messages_history',
                     '<span class="kw">def</span> <span class="fn">trim_messages_history</span>(history, sess):\n'
                     '    cap = sess.context_win * <span class="nb">3</span>\n'
                     '    <span class="fn">compress_history_tags</span>(history, interval=...)\n'
                     '    <span class="kw">if</span> <span class="fn">cost</span>() &lt;= cap: <span class="kw">return</span>\n'
                     '    <span class="fn">compress_history_tags</span>(history, keep_recent=<span class="nb">4</span>, force=<span class="nb">True</span>)\n'
                     '    <span class="kw">while</span> len(history) &gt; <span class="nb">9</span> <span class="kw">and</span> <span class="fn">cost</span>() &gt; target:\n'
                     '        history.<span class="fn">pop</span>(<span class="nb">0</span>)  <span class="cm"># ' + t('从最老的开始丢', 'drop from the oldest') + '</span>'))
            + c.qa(t, '⚙️ 两段式策略', 'A two-stage strategy',
                   '<p>' + t(
                       '每次 <span class="inline">*Session.ask</span> 发请求前都会调 <span class="inline">trim_messages_history</span>：'
                       '先<strong>轻压</strong>——周期性把较老消息里的 thinking/tool 标签内容截短（保留最近 ~10 轮）；'
                       '若仍超过 <span class="inline">context_win*3</span> 字符的硬上限，再<strong>强压</strong>（keep_recent=4）并从最老消息开始 pop，'
                       '直到降到目标线。这才是把上下文常年压在 &lt;30K 的真正机制。',
                       'Before every <span class="inline">*Session.ask</span> request, <span class="inline">trim_messages_history</span> runs: first a '
                       '<strong>light pass</strong> — periodically truncating thinking/tool-tag content in older messages (keeping the latest ~10 turns); '
                       'if still over the hard cap of <span class="inline">context_win*3</span> chars, a <strong>hard pass</strong> (keep_recent=4) plus '
                       'popping from the oldest message until it drops below the target. This is the real mechanism keeping context under ~30K.') + '</p>')
            + c.qa(t, '🔀 展示压缩 vs 历史压缩', 'Display compaction vs history compression',
                   '<table class="t"><tr><th></th><th>' + t('展示压缩', 'Display') + '</th><th>' + t('历史压缩', 'History') + '</th></tr>'
                   + '<tr><td>' + t('在哪', 'Where') + '</td><td class="mono">agent_loop.py</td><td class="mono">llmcore.py</td></tr>'
                   + '<tr><td>' + t('影响', 'Affects') + '</td><td>' + t('终端输出', 'terminal output') + '</td><td>' + t('发给模型的 messages', 'messages sent to model') + '</td></tr>'
                   + '<tr><td>' + t('省 token？', 'Saves tokens?') + '</td><td>' + t('否', 'no') + '</td><td>' + t('是', 'yes') + '</td></tr></table>'))

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像一张<strong>整洁的工作台</strong>：手边只摆当前这道工序要用的零件，做完就归档进抽屉；台面永远清爽，'
            '找东西又快又不容易拿错。GA 的上下文管理就是这种“桌面整洁术”——不是记得少，而是<strong>只把该上桌的摆上桌</strong>。',
            'Like a <strong>tidy workbench</strong>: only the parts for the current step sit at hand, and finished ones '
            'are filed into drawers; the surface stays clean, so you find things fast and rarely grab the wrong one. '
            'GA\'s context management is exactly this "tidy-desk" art — not remembering less, but <strong>putting only '
            'what belongs on the desk, on the desk</strong>.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('目标：把上下文压到 &lt;30K——更少噪声、更少幻觉、更低成本。',
            'Goal: keep context under 30K — less noise, fewer hallucinations, lower cost.') + '</li>'
        + '<li>' + t('组合拳：只带新消息 + _clean_content + _compact_tool_args + 周期重置 + 历史压缩。',
            'A combo: only-new-message + _clean_content + _compact_tool_args + periodic reset + history compression.') + '</li>'
        + '<li>' + t('分层记忆 + 工作便签兜底，所以“忘掉原始历史”不丢关键信息。',
            'Layered memory + the working notepad backstop it, so "forgetting raw history" loses nothing essential.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '小上下文不是<strong>妥协</strong>，而是 GenericAgent 主动选择的<strong>特性</strong>。它敢于“忘掉”原始历史，'
            '靠的是前几课的两块基石：<strong>分层记忆</strong>把该长期留的沉淀到 L1–L4，<strong>工作便签</strong>把当下该记的每轮回灌。'
            '于是上下文越小、信号越纯、越不容易跑偏——长任务反而更稳。这正是 GA “少即是多”哲学在运行时最直接的体现。',
            'A small context is not a <strong>compromise</strong> but a <strong>feature</strong> GenericAgent chooses. '
            'It dares to "forget" raw history thanks to two foundations from earlier lessons: <strong>layered '
            'memory</strong> settles what should persist into L1–L4, and the <strong>working notepad</strong> re-injects '
            'what matters now each turn. So the smaller the context, the purer the signal and the less it drifts — long '
            'tasks become more stable, not less. This is GA\'s "less is more" philosophy at its most direct, at runtime.',
        )
        + '</div>'
    )
