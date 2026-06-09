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
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_12(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_13(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_14(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'
