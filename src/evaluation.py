"""Part 6 — 速查 / Reference (lesson 23): positioning, evaluation & the paper.

``lesson_23(t)`` steps back from "how it works" to "why it's strong": the
density-first positioning, a head-to-head comparison, the five evaluation
dimensions, and the technical report. Following the guide's contract every
real excerpt is paired with a source explanation. All numbers are grounded in
the real GenericAgent repo (line counts measured) and README.md.
``t('中文', 'English')`` wraps every piece of prose.
"""

import components as c


def lesson_23(t):
    """为什么强：定位 · 评测 · 技术报告 / Why it's strong: positioning, evaluation, paper."""
    return (
        '<p class="lead">'
        + t(
            '前面 22 课讲的都是“它<strong>怎么</strong>工作”。这一课换个视角，回答“它<strong>到底好在哪、凭什么</strong>”：'
            'GenericAgent 的核心赌注、与主流 Agent 的横向对比、五维评测，以及背后的技术报告。',
            'The first 22 lessons were all about <strong>how</strong> it works. This one steps back to answer '
            '<strong>why it is strong, and on what basis</strong>: GenericAgent\'s core bet, a head-to-head comparison '
            'with mainstream agents, the five evaluation dimensions, and the technical report behind it all.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            'GenericAgent 押的是一个反直觉的赌注——<strong>信息密度最大化</strong>：用<strong>更少</strong>的代码与上下文，'
            '换<strong>更高</strong>的成功率与更低的成本。别的框架靠“堆功能、堆上下文”取胜，GA 反其道而行：'
            '核心约 3K 行、上下文常压在 &lt;30K。少不是妥协，而是一条<strong>不同的路</strong>——'
            '噪声更少、幻觉更少、可控性更强，还能<strong>自我生长</strong>。',
            'GenericAgent makes a counter-intuitive bet — <strong>maximize information density</strong>: trade '
            '<strong>less</strong> code and context for <strong>higher</strong> success and lower cost. Where other '
            'frameworks win by piling on features and context, GA does the opposite: a ~3K-line core with context '
            'usually kept under 30K. "Less" is not a compromise but a <strong>different road</strong> — less noise, '
            'fewer hallucinations, more control, and the ability to <strong>grow itself</strong>.',
        )
        + '</p></div>'

        + '<h2>' + t('“极简”不是口号：真实行数', 'Minimal is not a slogan: the real line counts') + '</h2>'
        + '<p>' + t(
            'README 说核心“约 3K 行、Agent Loop 约 100 行”。这不是宣传话术——直接 <span class="inline">wc -l</span> 数一下五个'
            '核心文件就知道：合计 <strong>2977 行</strong>，主循环 <span class="inline">agent_loop.py</span> 只有 133 行。',
            'The README says the core is "~3K lines, with a ~100-line Agent Loop." That is not marketing — just run '
            '<span class="inline">wc -l</span> on the five core files: <strong>2977 lines</strong> total, and the main '
            'loop in <span class="inline">agent_loop.py</span> is only 133 lines.') + '</p>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码佐证：核心五文件的真实行数', 'In the Source: real line counts of the five core files') + '</div>'
        + c.codefile('$ wc -l', t('GenericAgent 核心文件', 'GenericAgent core files'),
            '<span class="nb">133</span> agent_loop.py      <span class="cm"># ' + t('主循环：感知→决策→行动', 'main loop: perceive → decide → act') + '</span>\n'
            '<span class="nb">1068</span> llmcore.py        <span class="cm"># ' + t('LLM 内核：多模型 + 流式 + 历史压缩', 'LLM core: multi-model + streaming + history compaction') + '</span>\n'
            '<span class="nb">595</span> ga.py              <span class="cm"># ' + t('九个 do_&lt;tool&gt; 工具实现', 'the nine do_&lt;tool&gt; handlers') + '</span>\n'
            '<span class="nb">873</span> simphtml.py        <span class="cm"># ' + t('网页简化 + JS 注入', 'web simplification + JS injection') + '</span>\n'
            '<span class="nb">308</span> agentmain.py       <span class="cm"># ' + t('启动装配 + reflect 守护', 'startup assembly + reflect watchdog') + '</span>\n'
            '<span class="nb">2977</span> total             <span class="cm"># ' + t('≈ 3K 行（对比 OpenClaw ~53 万行）', '≈ 3K lines (vs OpenClaw ~530K)') + '</span>')
        + '<p>' + t(
            '<strong>源码说明</strong>：这五个文件就是整套“种子代码”。行数少带来三个直接好处——'
            '① <strong>可读</strong>：一个人几天就能读懂全貌；② <strong>可控</strong>：没有层层抽象，行为可预测、好调试；'
            '③ <strong>可自举</strong>：框架小到能用自己的九个工具维护自己（README 的“作者从未打开过终端”正源于此）。'
            '“密度优先”在这里第一次落到可量化的证据上。',
            '<strong>Source note</strong>: these five files <em>are</em> the entire "seed code". Few lines buy three '
            'direct wins — ① <strong>readable</strong>: one person can grasp the whole thing in a few days; '
            '② <strong>controllable</strong>: no layers of abstraction, so behaviour is predictable and easy to debug; '
            '③ <strong>self-bootstrapping</strong>: the framework is small enough to maintain itself with its own nine '
            'tools (the README\'s "the author never opened a terminal" comes straight from this). "Density first" here '
            'gets its first quantifiable evidence.') + '</p></div>'

        + '<h2>' + t('横向对比：少即是多', 'Head-to-head: less is more') + '</h2>'
        + '<table class="t"><tr><th>' + t('维度', 'Dimension') + '</th>'
        + '<th>GenericAgent</th><th>OpenClaw</th><th>Claude Code</th></tr>'
        + '<tr><td>' + t('代码量', 'Codebase') + '</td><td class="mono">' + t('~3K 行', '~3K lines') + '</td>'
        + '<td class="mono">~530,000</td><td class="mono">' + t('（大）', '(large)') + '</td></tr>'
        + '<tr><td>' + t('部署', 'Deployment') + '</td><td>pip + API Key</td>'
        + '<td>' + t('多服务编排', 'multi-service') + '</td><td>' + t('CLI + 订阅', 'CLI + subscription') + '</td></tr>'
        + '<tr><td>' + t('浏览器控制', 'Browser') + '</td><td>' + t('真实浏览器（保登录）', 'real browser (login kept)') + '</td>'
        + '<td>' + t('沙箱 / 无头', 'sandbox / headless') + '</td><td>' + t('靠 MCP 插件', 'via MCP plugin') + '</td></tr>'
        + '<tr><td>' + t('系统控制', 'OS control') + '</td><td>' + t('键鼠 · 视觉 · ADB', 'kbd/mouse · vision · ADB') + '</td>'
        + '<td>' + t('多智能体委派', 'multi-agent delegation') + '</td><td>' + t('文件 + 终端', 'files + terminal') + '</td></tr>'
        + '<tr><td>' + t('自进化', 'Self-evolution') + '</td><td>' + t('自主长技能', 'autonomous skill growth') + '</td>'
        + '<td>' + t('插件生态', 'plugin ecosystem') + '</td><td>' + t('会话间无状态', 'stateless between sessions') + '</td></tr></table>'
        + '<p>' + t(
            '同一张表，<strong>每一格都能落到前面某一课的真实代码</strong>——这正是下面第 2 个手风琴要展开的“对比项 → 源码”映射。',
            'Every cell in this table <strong>maps to real code from an earlier lesson</strong> — which is exactly the '
            '"claim → source" mapping unpacked in deep-dive #2 below.') + '</p>'

        + '<h2>' + t('五维评测', 'Five evaluation dimensions') + '</h2>'
        + '<table class="t"><tr><th>#</th><th>' + t('维度', 'Dimension') + '</th><th>' + t('基准', 'Benchmarks') + '</th></tr>'
        + '<tr><td>1</td><td>' + t('任务完成 & Token 效率', 'Task completion & token efficiency') + '</td>'
        + '<td class="mono">SOP-Bench · Lifelong AgentBench · RealFin</td></tr>'
        + '<tr><td>2</td><td>' + t('工具使用效率', 'Tool-use efficiency') + '</td>'
        + '<td class="mono">' + t('11 简单 + 5 长程任务', '11 simple + 5 long-horizon') + '</td></tr>'
        + '<tr><td>3</td><td>' + t('记忆系统有效性', 'Memory-system effectiveness') + '</td>'
        + '<td class="mono">SOP-Bench · LoCoMo · ' + t('20 技能压测', '20-skill stress') + '</td></tr>'
        + '<tr><td>4</td><td>' + t('自进化能力', 'Self-evolution') + '</td>'
        + '<td class="mono">' + t('9 轮 LangChain 纵向 · 8 任务跨任务', '9-round LangChain · 8-task cross-task') + '</td></tr>'
        + '<tr><td>5</td><td>' + t('网页浏览能力', 'Web browsing') + '</td>'
        + '<td class="mono">WebCanvas · BrowseComp-ZH · ' + t('22 自定义', '22 custom') + '</td></tr></table>'
        + '<p>' + t(
            '基线对手是 <strong>Claude Code · OpenAI CodeX · OpenClaw</strong>，统一在 Sonnet 4.6 / Opus 4.6 / GPT-5.4 / '
            'MiniMax M2.7 等底座上对比。',
            'Baselines are <strong>Claude Code · OpenAI CodeX · OpenClaw</strong>, compared on shared backbones '
            '(Sonnet 4.6 / Opus 4.6 / GPT-5.4 / MiniMax M2.7).') + '</p>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            'GA 像一家<strong>米其林一星小馆</strong>：菜单很短、食材精选、每道菜都打磨到位；大而全的框架像<strong>大型连锁</strong>：'
            '菜单几百页，样样有、但样样平。不是“做不出更多”，而是<strong>主动把少数几样做到极致</strong>——评测领先正是这种取舍的回报。',
            'GA is like a <strong>one-Michelin-star bistro</strong>: a short menu, hand-picked ingredients, every dish '
            'polished. A do-everything framework is the <strong>big chain</strong>: a 300-page menu where everything '
            'exists but nothing shines. It is not that GA "can\'t do more" — it deliberately <strong>perfects a '
            'few things</strong>, and the evaluation lead is the payoff of that trade-off.',
        )
        + '</div>'

        + c.deepdive_heading(t)

        + c.accordion(t, 1, '极简的量化证据：3K 行怎么自洽',
            'Minimal, quantified: how 3K lines hold together',
            c.qa(t, '🧪 这 3K 行都在干嘛', 'What the 3K lines actually do',
                 '<p>' + t(
                     '把 2977 行拆开看，没有一行是“框架自重”：<span class="inline">agent_loop.py</span>（133）是循环骨架，'
                     '<span class="inline">ga.py</span>（595）是九个工具的实现，<span class="inline">llmcore.py</span>（1068）'
                     '管多模型与历史压缩，<span class="inline">simphtml.py</span>（873）管网页简化与注入，'
                     '<span class="inline">agentmain.py</span>（308）管启动装配。能力不是写死在框架里的，而是运行时用 '
                     '<span class="inline">code_run</span> <strong>长出来</strong>的。',
                     'Break the 2977 lines down and none is "framework overhead": <span class="inline">agent_loop.py</span> '
                     '(133) is the loop skeleton, <span class="inline">ga.py</span> (595) implements the nine tools, '
                     '<span class="inline">llmcore.py</span> (1068) handles multi-model + history compaction, '
                     '<span class="inline">simphtml.py</span> (873) does web simplification + injection, and '
                     '<span class="inline">agentmain.py</span> (308) wires up startup. Capabilities are not baked into the '
                     'framework — they are <strong>grown</strong> at runtime via <span class="inline">code_run</span>.') + '</p>')
            + c.qa(t, '❓ 为什么“小”能换来“强”', 'Why "small" buys "strong"',
                   '<p>' + t(
                       '上下文越小，信号越纯：模型每轮看到的几乎全是当前任务相关内容，少了噪声就少了跑偏与幻觉。这与第 14 课的 '
                       '<span class="inline">llmcore.py: trim_messages_history</span> 是同一枚硬币的两面——'
                       '<strong>代码密度</strong>让框架可控，<strong>上下文密度</strong>让推理可靠。',
                       'The smaller the context, the purer the signal: almost everything the model sees each turn is '
                       'relevant to the current task, and less noise means less drift and fewer hallucinations. This is '
                       'two sides of one coin with lesson 14\'s <span class="inline">llmcore.py: trim_messages_history</span> '
                       '— <strong>code density</strong> keeps the framework controllable, <strong>context density</strong> '
                       'keeps reasoning reliable.') + '</p>'))

        + c.accordion(t, 2, '对比表的每一格 → 真实源码',
            'Every comparison cell → real source',
            c.qa(t, '🧪 claim ↔ 实现它的真实符号', 'Each claim mapped to the real symbol that implements it',
                 '<table class="t"><tr><th>' + t('对比项', 'Claim') + '</th><th>' + t('GA 的真实实现', 'GA\'s real implementation') + '</th><th>' + t('在哪一课', 'Lesson') + '</th></tr>'
                 + '<tr><td>' + t('真实浏览器', 'real browser') + '</td><td class="mono">ga.py: web_execute_js → TMWebDriver.execute_js</td><td>17</td></tr>'
                 + '<tr><td>' + t('自进化', 'self-evolution') + '</td><td class="mono">ga.py: do_start_long_term_update</td><td>12 · 20</td></tr>'
                 + '<tr><td>' + t('Token 高效', 'token efficient') + '</td><td class="mono">llmcore.py: trim_messages_history</td><td>14</td></tr>'
                 + '<tr><td>' + t('九个工具直接控制系统', '9 tools, direct control') + '</td><td class="mono">agent_loop.py: BaseHandler.dispatch</td><td>07 · 10</td></tr>'
                 + '<tr><td>' + t('极简代码量', 'minimal codebase') + '</td><td class="mono">5 files · 2977 lines</td><td>01 · ' + t('本课', 'here') + '</td></tr></table>')
            + c.qa(t, '⚙️ 源码说明：为什么这张映射很关键', 'Source note: why this mapping matters',
                   '<p>' + t(
                       '横向对比最容易沦为“宣传话术”——每一格都<strong>能指到一段真实代码</strong>，对比才站得住脚。'
                       '比如“真实浏览器（保登录）”不是形容词，而是 <span class="inline">web_execute_js</span> 把脚本经 '
                       'WebSocket 桥送进你<strong>已登录</strong>的浏览器（第 17 课逐行看过）；“自进化”落地为 '
                       '<span class="inline">do_start_long_term_update</span> 把成功路径结晶成 L3 <span class="inline">*_sop.md</span>。'
                       '对比表与源码<strong>一一对账</strong>，是这套教程“可验证”原则在“定位”层的延伸。',
                       'A comparison table easily degrades into marketing — it only holds up when every cell '
                       '<strong>points at real code</strong>. "Real browser (login kept)" is not an adjective but '
                       '<span class="inline">web_execute_js</span> shipping the script over a WebSocket bridge into your '
                       '<strong>already-logged-in</strong> browser (read line-by-line in lesson 17); "self-evolution" '
                       'lands as <span class="inline">do_start_long_term_update</span> crystallizing the successful path '
                       'into an L3 <span class="inline">*_sop.md</span>. Reconciling each claim against the source is this '
                       'guide\'s "verifiable" principle, extended to the positioning layer.') + '</p>'))

        + c.accordion(t, 3, '技术报告：arXiv 上的论文',
            'The technical report: the paper on arXiv',
            c.qa(t, '🧪 论文核心', 'The paper in one line',
                 '<p>' + t(
                     '论文题为《<strong>GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual '
                     'Information Density Maximization</strong>》（arXiv <span class="mono">2604.17091</span>）。'
                     '标题本身就是这一课的论点：<strong>用“上下文信息密度最大化”同时换来 token 高效与自进化</strong>。',
                     'The paper is titled "<strong>GenericAgent: A Token-Efficient Self-Evolving LLM Agent via '
                     'Contextual Information Density Maximization</strong>" (arXiv <span class="mono">2604.17091</span>). '
                     'The title <em>is</em> this lesson\'s thesis: <strong>maximizing contextual information density buys '
                     'both token efficiency and self-evolution at once</strong>.') + '</p>')
            + c.qa(t, '⚙️ 怎么读这些评测结论', 'How to read the evaluation results',
                   '<p>' + t(
                       '两张关键图：<strong>工具效率雷达图</strong>显示 GA 在 token / 请求数 / 工具调用三条轴上全面领先，同时'
                       '保住四类任务的质量；<strong>跨任务收敛图</strong>显示 GA 第 2、3 次执行<strong>收敛到稳定低成本区</strong>'
                       '（经验留下了），而 OpenClaw 没有这种收敛。复现数据与完整结果在配套仓库 '
                       '<span class="inline">JinyiHan99/GA-Technical-Report</span>。',
                       'Two key figures: the <strong>tool-efficiency radar</strong> shows GA leading on token / request / '
                       'tool-call axes while preserving quality across four task types; the <strong>cross-task '
                       'convergence</strong> plot shows GA\'s 2nd and 3rd runs <strong>converging to a stable low-cost '
                       'regime</strong> (experience is kept), while OpenClaw shows no such convergence. Reproduction data '
                       'and full results live in the companion repo '
                       '<span class="inline">JinyiHan99/GA-Technical-Report</span>.') + '</p>'))

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('核心约 3K 行（实测 2977）、主循环 133 行——“极简”可量化、可佐证。',
            'The core is ~3K lines (measured 2977), the main loop 133 — "minimal" is quantifiable and verifiable.') + '</li>'
        + '<li>' + t('对比表每一格都能指向真实源码：真实浏览器、自进化、Token 高效各有其符号。',
            'Every comparison cell points to real source: real browser, self-evolution, token efficiency each have a symbol.') + '</li>'
        + '<li>' + t('五维评测对标 Claude Code / CodeX / OpenClaw；技术报告见 arXiv 2604.17091。',
            'Five evaluation dimensions vs Claude Code / CodeX / OpenClaw; the report is arXiv 2604.17091.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '把整套项目串起来的，是<strong>同一个赌注</strong>：信息密度最大化。它一次解释了四件事——'
            '<strong>极简</strong>（代码密度）、<strong>Token 高效</strong>（上下文密度）、<strong>自进化</strong>'
            '（把经验压成最高密度的 SOP）、以及<strong>评测领先</strong>（同样的 token 做更多事）。'
            '密度不只是省钱的手段，更是 GA 的<strong>护城河</strong>：当别人靠加法变强，GA 靠减法变强。',
            'One <strong>single bet</strong> ties the whole project together: maximize information density. It explains '
            'four things at once — <strong>minimalism</strong> (code density), <strong>token efficiency</strong> '
            '(context density), <strong>self-evolution</strong> (compressing experience into the densest possible SOPs), '
            'and the <strong>evaluation lead</strong> (more done per token). Density is not just a cost-saving trick but '
            'GA\'s <strong>moat</strong>: where others grow stronger by adding, GA grows stronger by subtracting.',
        )
        + '</div>'
    )
