"""Part 5 — 实战 / Hands-On (lessons 20–22).

Each lesson is a ``lesson(t)`` function. ``t('中文', 'English')`` wraps every
piece of prose; structure, diagrams and code are written once and shared by
both language renders. All technical claims are grounded in the real
GenericAgent source (README self-evolution, memory/skill_search, the memory
SOPs, frontends/conductor.py, frontends/*app.py, agentmain.py).

Authoring conventions are documented at the top of ``part1.py`` — follow the
same 5-card lesson format (🌍 macro / 🔬 detail / 🧩 analogy / ✅ key /
💡 spark) and the ``.inline`` (prose code) vs ``.mono`` (dense components) rule.
"""

import components as c


def lesson_20(t):
    """自进化机制详解 / The Self-Evolution Mechanism."""
    return (
        '<p class="lead">'
        + t(
            '这是 GenericAgent 与其他框架<strong>本质上的不同</strong>：它不靠预装技能取胜，而是每解决一个新任务，'
            '就把这次的成功路径<strong>结晶成一个可复用的 Skill</strong>。用得越久，技能越多——长成一棵只属于你的技能树。',
            'This is what makes GenericAgent <strong>fundamentally different</strong>: it does not win by preloading '
            'skills, but by <strong>crystallizing each successful path into a reusable Skill</strong> whenever it '
            'solves a new task. The longer you use it, the more skills accumulate — growing a skill tree that is '
            'uniquely yours.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '自进化是一个<strong>闭环</strong>：新任务 → 自主探索（装依赖、写脚本、调试、验证）→ 把成功路径结晶进记忆 → '
            '下次遇到相似任务直接召回。第一次可能要折腾很久，但只要成功，<strong>这份经验就永久留下</strong>，从此一句话搞定。',
            'Self-evolution is a <strong>closed loop</strong>: new task → autonomous exploration (install deps, write '
            'scripts, debug, verify) → crystallize the successful path into memory → directly recall it next time a '
            'similar task appears. The first time may take a lot of fiddling, but once it succeeds, <strong>that '
            'experience stays forever</strong>, and from then on one sentence does it.',
        )
        + '</p></div>'

        + '<h2>' + t('自进化闭环', 'The self-evolution loop') + '</h2>'
        + '<div class="vflow">'
        + '<div class="step"><div class="num">1</div><div class="sc"><h3>'
        + t('新任务', 'New task') + '</h3><p>'
        + t('来了一件它还不会的事。', 'Something it cannot yet do arrives.') + '</p></div></div>'
        + '<div class="step"><div class="num">2</div><div class="sc"><h3>'
        + t('自主探索', 'Autonomous exploration') + '</h3><p>'
        + t('用 code_run 装依赖、写脚本、调试，直到<strong>行动验证成功</strong>。',
            'Use code_run to install deps, write scripts, debug, until <strong>action-verified success</strong>.') + '</p></div></div>'
        + '<div class="step"><div class="num">3</div><div class="sc"><h3>'
        + t('结晶为 Skill', 'Crystallize into a Skill') + '</h3><p>'
        + t('start_long_term_update 把要点写进 L3 SOP，并在 L1 索引登记。',
            'start_long_term_update writes the essentials into an L3 SOP and registers it in the L1 index.') + '</p></div></div>'
        + '<div class="step"><div class="num">4</div><div class="sc"><h3>'
        + t('下次直接召回', 'Direct recall next time') + '</h3><p>'
        + t('相似任务再来，顺着 L1 索引找到 SOP，一步到位。',
            'When a similar task returns, follow the L1 index to the SOP and do it in one shot.') + '</p></div></div>'
        + '</div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('结晶靠第 12 课的 ', 'Crystallization uses lesson 12\'s ')
        + '<span class="inline">start_long_term_update</span>'
        + t('；技能存在 L3（memory/ 下的 *_sop.md），由 L1 索引导航。',
            '; skills live in L3 (the *_sop.md files under memory/), navigated by the L1 index.') + '</li>'
        + '<li>' + t('技能检索见 ', 'Skill retrieval is in ')
        + '<span class="inline">memory/skill_search/</span>'
        + t('（含 SKILL.md 与检索能力），帮 Agent 在技能库里找到该用哪条 SOP。',
            ' (with SKILL.md and a search capability), helping the agent find which SOP to use.') + '</li>'
        + '<li>' + t('两种进阶进化：', 'Two advanced evolutions: ')
        + '<span class="inline">memory/morphling_sop.md</span>'
        + t('（Morphling：抽取目标项目的目标+测例，吸收/复刻其能力）与 ',
            ' (Morphling: extract a target project\'s goals + tests and absorb/replicate its abilities) and ')
        + '<span class="inline">memory/incubator_sop.md</span>'
        + t('（Incubator：把自己复制部署到其他节点，各自带独立记忆）。',
            ' (Incubator: replicate and deploy itself to other nodes, each with independent memory).') + '</li>'
        + '</ul></div>'

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '闭环四步逐步拆解：每一步到底用哪个零件',
            'The four-step loop, step by step: which part runs each step',
            c.qa(t, '🧪 一次完整循环 ↔ 零件对照', 'One full loop mapped to parts',
                 '<table class="t"><tr><th>' + t('步骤', 'Step') + '</th><th>'
                 + t('做什么', 'What happens') + '</th><th>' + t('用到的零件', 'Part used') + '</th></tr>'
                 + '<tr><td>' + t('① 新任务', '① New task') + '</td><td>'
                 + t('来了件它还不会的事', 'something it cannot yet do arrives') + '</td><td class="mono">put_task(...)</td></tr>'
                 + '<tr><td>' + t('② 自主探索', '② Explore') + '</td><td>'
                 + t('装依赖 / 写脚本 / 调试 / 验证', 'install deps / write scripts / debug / verify')
                 + '</td><td class="mono">code_run, file_write</td></tr>'
                 + '<tr><td>' + t('③ 结晶', '③ Crystallize') + '</td><td>'
                 + t('把成功要点写进 L3 SOP，登记 L1 索引', 'write essentials into an L3 SOP, register in the L1 index')
                 + '</td><td class="mono">start_long_term_update</td></tr>'
                 + '<tr><td>' + t('④ 召回', '④ Recall') + '</td><td>'
                 + t('相似任务顺着 L1 找到 SOP', 'a similar task follows L1 to the SOP')
                 + '</td><td class="mono">memory/skill_search/</td></tr></table>')
            + c.qa(t, '⚙️ “结晶”内部怎么走', 'What "crystallize" does internally',
                   '<p>' + t(
                       '结晶不是“把整段对话存下来”，而是<strong>提炼</strong>：用 '
                       '<span class="inline">start_long_term_update</span> 只写下复用必需的要点——脚本路径、关键命令、'
                       '踩过的坑——成为 <span class="inline">memory/</span> 下的一个 <span class="inline">*_sop.md</span>（L3），'
                       '并在 L1 全局索引里登记一行指针。下次靠这行指针就能找回整条 SOP。',
                       'Crystallizing is not "save the whole transcript" — it is <strong>distillation</strong>: '
                       '<span class="inline">start_long_term_update</span> records only what reuse needs — the script '
                       'path, key commands, the pitfalls hit — as one <span class="inline">*_sop.md</span> (L3) under '
                       '<span class="inline">memory/</span>, and registers a one-line pointer in the L1 global index. '
                       'Next time that pointer leads straight back to the whole SOP.') + '</p>')
            + c.qa(t, '⚠️ 无行动，不记忆', 'No action, no memory',
                   '<p>' + t(
                       '步骤③只在步骤②<strong>真正跑通并验证成功</strong>后才触发。没被行动验证过的“想法”不许结晶——'
                       '否则记忆里会沉淀一堆没跑通的假经验，越用越坏。这是 L0 记忆铁律（见 '
                       '<span class="inline">memory/memory_management_sop.md</span>）。',
                       'Step ③ fires only after step ② <strong>actually runs and verifies success</strong>. An '
                       '"idea" never proven by action may not crystallize — otherwise memory fills with un-run, false '
                       'experience that rots with use. This is the L0 memory rule (see '
                       '<span class="inline">memory/memory_management_sop.md</span>).') + '</p>'))
        + c.accordion(t, 2, 'skill_search：在 10 万+ 技能卡里找“该用哪条 SOP”',
            'skill_search: finding "which SOP to use" among 100K+ skill cards',
            c.qa(t, '🧪 最简调用', 'The minimal call',
                 c.codefile('memory/skill_search/SKILL.md', 'search()',
                     "import sys; sys.path.append('../memory/skill_search')\n"
                     "from skill_search import search\n\n"
                     'results = search("python send email")  # '
                     + t('必须用英文查询', 'queries must be in English') + '\n'
                     "for r in results:\n"
                     "    s = r.skill\n"
                     '    print(f"[{r.final_score:.2f}] {s.name} — {s.one_line_summary}")'))
            + c.qa(t, '❓ 为什么必须用英文查询', 'Why queries must be English',
                   '<p>' + t(
                       '据 <span class="inline">SKILL.md</span> 的明确提示：<strong>中文匹配效果极差</strong>，'
                       '所以查询要用英文（如 <span class="inline">"docker deployment"</span>）。技能库是语义检索，'
                       '英文 query 命中的相关度和质量分都更高。',
                       'Per <span class="inline">SKILL.md</span>\'s explicit note: <strong>Chinese matches poorly</strong>, '
                       'so queries should be English (e.g. <span class="inline">"docker deployment"</span>). The library '
                       'is semantic search, and English queries score higher on relevance and quality.') + '</p>')
            + c.qa(t, '⚙️ 返回里有什么、内部怎么走', 'What it returns and how it works',
                   '<p>' + t(
                       '<span class="inline">search(query, env=None, category=None, top_k=10)</span> 返回一组 '
                       '<span class="inline">SearchResult</span>（见 '
                       '<span class="inline">skill_search/engine.py</span>），每条带 '
                       '<span class="mono">final_score / relevance / quality</span> 与一个 '
                       '<span class="inline">SkillIndex</span>（含 <span class="mono">key、one_line_summary、'
                       'category、form、autonomous_safe</span>）。它是个零依赖 API 客户端，默认打到内置地址 '
                       '<span class="mono">http://www.fudankw.cn:58787</span>，可用环境变量 '
                       '<span class="inline">SKILL_SEARCH_API</span> 覆盖。',
                       '<span class="inline">search(query, env=None, category=None, top_k=10)</span> returns a list of '
                       '<span class="inline">SearchResult</span> (see <span class="inline">skill_search/engine.py</span>), '
                       'each carrying <span class="mono">final_score / relevance / quality</span> and a '
                       '<span class="inline">SkillIndex</span> (with <span class="mono">key, one_line_summary, category, '
                       'form, autonomous_safe</span>). It is a zero-dependency API client hitting a built-in default '
                       '<span class="mono">http://www.fudankw.cn:58787</span>, overridable via '
                       '<span class="inline">SKILL_SEARCH_API</span>.') + '</p>')
            + c.qa(t, '🔀 和“把所有技能塞进上下文”对比', 'vs stuffing every skill into context',
                   '<p>' + t(
                       '若把上万条技能全列进 prompt，上下文会爆炸、模型会分心。skill_search 反过来——<strong>按需检索</strong>，'
                       '只把最相关的几条召回，既省 token 又少噪声，正是“做减法”哲学在记忆侧的体现。',
                       'Listing tens of thousands of skills in the prompt would explode context and distract the model. '
                       'skill_search inverts this — <strong>retrieve on demand</strong>, recalling only the few most '
                       'relevant — saving tokens and noise, the "subtract" philosophy applied to memory.') + '</p>'))
        + c.accordion(t, 3, '两种进阶进化：Morphling（吸收）与 Incubator（复制）',
            'Two advanced evolutions: Morphling (absorb) and Incubator (replicate)',
            c.qa(t, '🧪 Morphling 的核心三元组', 'Morphling\'s core triple',
                 '<p>' + t(
                     '据 <span class="inline">memory/morphling_sop.md</span>，Morphling 是项目级能力吸收/替代：给定任意目标项目，'
                     '围绕三元组工作——<strong>目标（Target，它解决什么）、测例（Tests，怎么验证）、行为（Actions，逐组件决定'
                     '调用 / 重写 / 舍弃）</strong>。最终让自身或新产物<strong>在同一测例上达到或超过目标</strong>。',
                     'Per <span class="inline">memory/morphling_sop.md</span>, Morphling is project-level capability '
                     'absorption/replacement: given any target project, work around a triple — <strong>Target (what it '
                     'solves), Tests (how to verify), Actions (per component: call / rewrite / discard)</strong> — until '
                     'oneself or a new product <strong>matches or beats the target on the same tests</strong>.') + '</p>')
            + c.qa(t, '⚙️ Morphling 怎么执行', 'How Morphling executes',
                   '<p>' + t(
                       '“更好”不能靠主观判断，必须落在可测维度（通过率 / 性能 / 成本 / 稳定性 / 易用性）。SOP 还规定它'
                       '<strong>应通过 Goal Hive 执行</strong>（见 <span class="inline">goal_hive_sop</span>）：Master 调度 + '
                       'Worker 并行实现 + 持续验收的长程模式。',
                       '"Better" cannot be subjective — it must land on a measurable axis (pass rate / speed / cost / '
                       'stability / usability). The SOP also mandates it <strong>run via Goal Hive</strong> (see '
                       '<span class="inline">goal_hive_sop</span>): Master scheduling + parallel Workers + continuous '
                       'acceptance, a long-horizon pattern.') + '</p>')
            + c.qa(t, '🧪 Incubator：自我复制到其他节点', 'Incubator: self-replicate to other nodes',
                   '<p>' + t(
                       '据 <span class="inline">memory/incubator_sop.md</span>，Incubator 把 GA 复制部署到任意节点，'
                       '组成一张 agent 网络，<strong>每个节点有独立记忆</strong>，可通过编辑其 '
                       '<span class="inline">memory/</span> 来干预行为。通信走与 subagent 相同的协议：'
                       '<span class="inline">agentmain.py --task {name} --input "..."</span>。',
                       'Per <span class="inline">memory/incubator_sop.md</span>, Incubator replicates and deploys GA to '
                       'any node, forming an agent network where <strong>each node has independent memory</strong>, '
                       'steerable by editing its <span class="inline">memory/</span>. Communication uses the same '
                       'protocol as subagents: <span class="inline">agentmain.py --task {name} --input "..."</span>.') + '</p>')
            + c.qa(t, '⚠️ Incubator 的关键坑点', 'Incubator\'s key pitfall',
                   '<p>' + t(
                       'SOP 明确警告：<strong>不要复制 L1/L2 文件</strong>（<span class="inline">global_mem(_insight).txt</span>），'
                       '它们会在新节点自动初始化；也不要复制 <span class="inline">memory/</span> 下未被 gitignore 白名单的文件。'
                       '否则新节点会带着别人的“私货记忆”出生，污染它本应独立生长的技能树。',
                       'The SOP warns explicitly: <strong>do not copy L1/L2 files</strong> '
                       '(<span class="inline">global_mem(_insight).txt</span>) — they auto-initialize on the new node — '
                       'nor any file under <span class="inline">memory/</span> outside the gitignore whitelist. '
                       'Otherwise the new node is born carrying someone else\'s memory, polluting the skill tree it '
                       'should grow independently.') + '</p>'))
        + c.accordion(t, 4, 'README 自进化表：第一次 vs 之后每次',
            'The README self-evolution table: first time vs every time after',
            c.qa(t, '🧪 三个真实任务', 'Three real tasks',
                 '<table class="t"><tr><th>' + t('你说的一句话', 'What you say') + '</th><th>'
                 + t('第一次', 'First time') + '</th><th>' + t('之后每次', 'After') + '</th></tr>'
                 + '<tr><td>' + t('“读我的微信记录”', '"Read my WeChat messages"') + '</td><td>'
                 + t('装依赖 → 逆向数据库 → 写读取脚本 → 存为 Skill',
                     'install deps → reverse DB → write read script → save Skill') + '</td><td>'
                 + t('一句话直接调用', 'one-line invoke') + '</td></tr>'
                 + '<tr><td>' + t('“监控股票并提醒我”', '"Monitor stocks and alert me"') + '</td><td>'
                 + t('装 mootdx → 构建选股流程 → 配置定时 → 存为 Skill',
                     'install mootdx → build a screening flow → configure cron → save Skill') + '</td><td>'
                 + t('一句话启动', 'one-line start') + '</td></tr>'
                 + '<tr><td>' + t('“用 Gmail 发这个文件”', '"Send this file via Gmail"') + '</td><td>'
                 + t('配置 OAuth → 编写发送脚本 → 存为 Skill',
                     'configure OAuth → write send script → save Skill') + '</td><td>'
                 + t('直接可用', 'ready to use') + '</td></tr></table>')
            + c.qa(t, '❓ 这张表想说明什么', 'What the table is really saying',
                   '<p>' + t(
                       '据 README：“几周后，你的 agent 实例会拥有一棵世界上独一无二的技能树——全部从 3K 行种子代码长出。”'
                       '三行任务跨越完全不同的领域（IM / 金融 / 邮件），却共用<strong>同一个闭环</strong>，说明自进化是'
                       '<strong>通用机制</strong>，而非某个内置功能。',
                       'Per the README: "after a few weeks your agent instance will have a skill tree no one else in the '
                       'world has — all grown from 3K lines of seed code." The three tasks span totally different '
                       'domains (IM / finance / email) yet share <strong>the same loop</strong>, showing self-evolution '
                       'is a <strong>general mechanism</strong>, not one built-in feature.') + '</p>'))

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像一个<strong>会写菜谱的厨师</strong>：第一次做一道新菜，要查资料、试比例、可能翻几次车；一旦做成，他就把'
            '“火候、用量、步骤”写成一张菜谱收进菜谱本。下次再点这道菜，照谱做，又快又稳。日子久了，他的菜谱本<strong>独一无二</strong>——'
            '别的厨师没有。',
            'Like a <strong>chef who writes recipes</strong>: the first time he makes a new dish he researches, tries '
            'ratios, maybe fails a few times; once it works, he writes the "heat, amounts, steps" into a recipe and '
            'files it. Next time the dish is ordered, he cooks from the recipe — fast and reliable. Over time his recipe '
            'book is <strong>one of a kind</strong> — no other chef has it.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('闭环：新任务 → 自主探索 → 结晶为 Skill → 下次召回。',
            'Loop: new task → autonomous exploration → crystallize into a Skill → recall next time.') + '</li>'
        + '<li>' + t('技能存 L3 SOP、由 L1 索引导航、用 skill_search 检索。',
            'Skills live in L3 SOPs, are navigated by the L1 index, and found via skill_search.') + '</li>'
        + '<li>' + t('进阶：Morphling 吸收外部项目能力，Incubator 自我复制部署。',
            'Advanced: Morphling absorbs external project abilities; Incubator self-replicates and deploys.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '自进化把“能力”从<strong>出厂预置</strong>变成了<strong>运行时生长</strong>。这也解释了前面所有设计为何如此克制：'
            '极简的循环、九个原子工具、严格“行动验证”的记忆——都是为了让“探索 → 结晶 → 召回”这个飞轮转得稳、转得久。'
            '于是 3K 行种子代码不是终点，而是<strong>起点</strong>：真正的能力，是你和它一起长出来的。',
            'Self-evolution turns "capability" from <strong>factory-preset</strong> into <strong>grown at '
            'runtime</strong>. This explains why every earlier design is so restrained: the minimal loop, the nine '
            'atomic tools, the strict "action-verified" memory — all to keep the "explore → crystallize → recall" '
            'flywheel spinning steadily and long. So 3K lines of seed code is not the destination but the '
            '<strong>starting point</strong>: the real capability is what you and it grow together.',
        )
        + '</div>'
    )


def lesson_21(t):
    """端到端实战：造一个新技能 / End-to-End: Build a Skill."""
    return (
        '<p class="lead">'
        + t(
            '理论讲完了，来走一遍真实流程。以一句“<strong>帮我读一下微信聊天记录</strong>”为例，看 GA 第一次怎么从零摸索，'
            '又怎么把成果<strong>沉淀成一条技能</strong>，让第二次变成一句话的事。',
            'Enough theory — let us walk a real flow. Take "<strong>read my WeChat messages</strong>" as an example, '
            'and watch how GA fumbles from scratch the first time, then <strong>settles the result into a skill</strong> '
            'so the second time becomes a one-liner.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '“造技能”不是单独的功能，而是把前面所有零件<strong>拼起来用一次</strong>：用工具去探索，用记忆去结晶。'
            '关键分水岭就一个——<strong>第一次</strong>（慢，要试错）和<strong>之后每次</strong>（快，直接召回）。',
            '"Building a skill" is not a separate feature; it is <strong>using all the earlier parts together once</strong>: '
            'tools to explore, memory to crystallize. The watershed is a single one — the <strong>first time</strong> '
            '(slow, trial and error) versus <strong>every time after</strong> (fast, direct recall).',
        )
        + '</p></div>'

        + '<h2>' + t('第一次：从零摸索', 'First time: from scratch') + '</h2>'
        + '<div class="vflow">'
        + '<div class="step"><div class="num">1</div><div class="sc"><h3>'
        + t('记住目标', 'Capture the goal') + '</h3><p>'
        + t('收到任务，先用 update_working_checkpoint 记下“要读微信记录”和关键约束。',
            'On receiving the task, use update_working_checkpoint to note "read WeChat messages" and key constraints.') + '</p></div></div>'
        + '<div class="step"><div class="num">2</div><div class="sc"><h3>'
        + t('探索与试错', 'Explore & iterate') + '</h3><p>'
        + t('用 code_run 装依赖、定位数据库、写读取脚本，失败就读报错再改。',
            'Use code_run to install deps, locate the database, write a read script; on failure, read the error and fix.') + '</p></div></div>'
        + '<div class="step"><div class="num">3</div><div class="sc"><h3>'
        + t('验证成功', 'Verify success') + '</h3><p>'
        + t('真正跑通、读出消息——这一步是“能不能记忆”的前提（无行动，不记忆）。',
            'Actually run it and read out the messages — the prerequisite for "may we remember" (no execution, no memory).') + '</p></div></div>'
        + '<div class="step"><div class="num">4</div><div class="sc"><h3>'
        + t('结晶为技能', 'Crystallize a skill') + '</h3><p>'
        + t('start_long_term_update：把脚本路径与关键坑点写成 L3 SOP，在 L1 索引登记一行。',
            'start_long_term_update: write the script path and key pitfalls into an L3 SOP, and register one line in the L1 index.') + '</p></div></div>'
        + '</div>'

        + '<h2>' + t('之后每次：一句话', 'Every time after: one sentence') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('你说的话', 'What you say') + '</th><th>' + t('第一次', 'First time') + '</th>'
        + '<th>' + t('之后每次', 'Every time after') + '</th></tr>'
        + '<tr><td>' + t('“读我的微信记录”', '"Read my WeChat messages"') + '</td>'
        + '<td>' + t('装依赖 → 逆向数据库 → 写读取脚本 → 存为技能', 'install deps → reverse the DB → write a read script → save as a skill') + '</td>'
        + '<td>' + t('一句话直接调用', 'one-line invoke') + '</td></tr>'
        + '<tr><td>' + t('“盯盘并提醒我”', '"Monitor stocks and alert me"') + '</td>'
        + '<td>' + t('装行情库 → 搭选股流程 → 配定时 → 存为技能', 'install a quotes lib → build a screening flow → set up a schedule → save as a skill') + '</td>'
        + '<td>' + t('一句话启动', 'one-line start') + '</td></tr>'
        + '</table>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('用到的工具都来自第 7 课：', 'The tools used are all from lesson 7: ')
        + '<span class="inline">code_run</span>' + t('（探索）、', ' (explore), ')
        + '<span class="inline">file_write / file_patch</span>' + t('（写脚本与 SOP）、',
            ' (write scripts and SOPs), ')
        + '<span class="inline">update_working_checkpoint</span>' + t(' 与 ', ' and ')
        + '<span class="inline">start_long_term_update</span>' + t('（记忆）。', ' (memory).') + '</li>'
        + '<li>' + t('结晶遵循 L0 记忆铁律（', 'Crystallization follows the L0 memory rules (')
        + '<span class="inline">memory/memory_management_sop.md</span>'
        + t('）：只记验证成功的要点，最小化 patch；技能落到 L3（memory/ 下的 *_sop.md）。',
            '): record only verified essentials, patch minimally; the skill lands in L3 (a *_sop.md under memory/).') + '</li>'
        + '<li>' + t('下次靠 ', 'Next time, ')
        + '<span class="inline">memory/skill_search/</span>'
        + t(' 在技能库里找回这条 SOP。', ' finds this SOP back in the skill library.') + '</li>'
        + '</ul></div>'

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '第一次：四步与真实工具一一对应',
            'First time: the four steps mapped to real tools',
            c.qa(t, '🧪 步骤 ↔ 工具 ↔ 记忆层', 'Step ↔ tool ↔ memory layer',
                 '<table class="t"><tr><th>' + t('步骤', 'Step') + '</th><th>'
                 + t('真实工具', 'Real tool') + '</th><th>' + t('落点', 'Lands in') + '</th></tr>'
                 + '<tr><td>' + t('① 记住目标', '① Capture goal') + '</td><td class="mono">update_working_checkpoint</td><td>'
                 + t('工作记忆', 'working memory') + '</td></tr>'
                 + '<tr><td>' + t('② 探索试错', '② Explore & iterate') + '</td><td class="mono">code_run, file_write/file_patch</td><td>'
                 + t('临时脚本', 'scratch scripts') + '</td></tr>'
                 + '<tr><td>' + t('③ 验证成功', '③ Verify success') + '</td><td class="mono">code_run</td><td>'
                 + t('行动结果', 'action result') + '</td></tr>'
                 + '<tr><td>' + t('④ 结晶技能', '④ Crystallize') + '</td><td class="mono">start_long_term_update</td><td>'
                 + t('L3 *_sop.md + L1 索引', 'L3 *_sop.md + L1 index') + '</td></tr></table>')
            + c.qa(t, '⚙️ update_working_checkpoint 和 start_long_term_update 有什么区别',
                   'update_working_checkpoint vs start_long_term_update',
                   '<p>' + t(
                       '前者是<strong>短期工作记忆</strong>：在任务进行中记下“我现在要干嘛、关键约束是什么”，用完即弃；'
                       '后者是<strong>长期结晶</strong>：任务成功后把可复用经验沉淀成 L3 SOP。一个管“当下别走神”，'
                       '一个管“以后还能用”。',
                       'The former is <strong>short-term working memory</strong>: mid-task, note "what I am doing now and '
                       'the key constraints", discarded when done. The latter is <strong>long-term crystallization</strong>: '
                       'after success, settle reusable experience into an L3 SOP. One keeps the agent on-task now; the '
                       'other makes it reusable later.') + '</p>')
            + c.qa(t, '⚠️ 为什么第③步不能省', 'Why step ③ cannot be skipped',
                   '<p>' + t(
                       '“无行动，不记忆”：必须<strong>真的跑通、读出消息</strong>，才允许进入第④步结晶。略过验证直接保存，'
                       '等于把没跑通的脚本当成技能存进去，下次召回反而误事。',
                       '"No action, no memory": the script must <strong>actually run and read out messages</strong> '
                       'before step ④ may crystallize. Skipping verification and saving anyway stores an unproven script '
                       'as a skill — which then misfires on recall.') + '</p>')
            + c.qa(t, '🧪 一个技能落地后长什么样', 'What a crystallized skill actually looks like',
                 c.codefile('assets/global_mem_insight_template.txt', 'L1 ' + t('索引：每条技能一格', 'index: one cell per skill'),
                     'L0(META-SOP): memory_management_sop\n'
                     'L3: memory_cleanup_sop(' + t('记忆整理', 'memory cleanup') + ') | skill_search | ui_detect.py | web_setup_sop\n'
                     '  | autonomous_operation_sop | scheduled_task_sop | vision_sop | adb_ui.py | ...\n'
                     'L4: L4_raw_sessions/ ' + t('历史会话', 'archived sessions'))
                 + c.codefile('memory/memory_cleanup_sop.md', t('一个技能 = 一个 *_sop.md', 'a skill = one *_sop.md'),
                     '# ' + t('记忆整理 SOP', 'Memory-cleanup SOP') + '\n'
                     '## ' + t('核心原则：存在性编码', 'Core principle: existence encoding') + '\n'
                     + t('LLM 自身是压缩器+解码器。L1 只需让它意识到“某类知识存在”，', 'The LLM itself is compressor + decoder. L1 only needs to make it aware "some knowledge exists",') + '\n'
                     + t('它就能通过 tool call 自行取用深层内容。', 'and it fetches the deep content itself via a tool call.'))
                 + '<p>' + t(
                     '所以“造一个技能”落到磁盘上，就是这两样东西：<strong>L3 多一个 <span class="inline">*_sop.md</span></strong> 文件，'
                     '<strong>L1 索引多一格指针</strong>。没有数据库、没有注册表——召回时 skill_search 命中 L1 那一格，再顺指针打开 L3 全文。',
                     'So "building a skill" on disk is exactly these two things: <strong>one more '
                     '<span class="inline">*_sop.md</span> in L3</strong> and <strong>one more pointer cell in the L1 '
                     'index</strong>. No database, no registry — on recall, skill_search hits that L1 cell, then follows '
                     'the pointer to open the full L3 text.') + '</p>'))
        + c.accordion(t, 2, '之后每次：一句话是怎么被召回的',
            'Every time after: how one sentence gets recalled',
            c.qa(t, '⚙️ 召回路径', 'The recall path',
                 '<p>' + t(
                     '你再说“读微信记录”，GA 不再从零探索：先用 '
                     '<span class="inline">memory/skill_search/</span> 语义检索命中那条 SOP，顺着 L1 索引指针打开 L3 的 '
                     '<span class="inline">*_sop.md</span>，照着里面的脚本路径与命令一步到位。',
                     'When you say "read WeChat messages" again, GA no longer explores from scratch: it semantically '
                     'matches the SOP via <span class="inline">memory/skill_search/</span>, follows the L1 index pointer '
                     'to open the L3 <span class="inline">*_sop.md</span>, and executes its script path and commands in '
                     'one shot.') + '</p>')
            + c.qa(t, '🔀 第一次 vs 之后每次', 'First time vs every time after',
                   '<p>' + t(
                       '第一次：装依赖 → 逆向数据库 → 写脚本 → 验证 → 结晶，可能折腾很久；之后每次：一句话直接调用。'
                       '差别不在“模型更聪明了”，而在<strong>经验被留下了</strong>——同类任务越做越快、越做越省。',
                       'First time: install deps → reverse DB → write script → verify → crystallize, possibly a long '
                       'fiddle. After: one-line invoke. The difference is not "a smarter model" but '
                       '<strong>experience kept</strong> — similar tasks get faster and cheaper each time.') + '</p>'))
        + c.accordion(t, 3, '没有新机制：这一课只是把前面零件拼一次',
            'No new mechanism: this lesson just composes earlier parts once',
            c.qa(t, '🧪 每块积木的来源', 'Where each block comes from',
                 '<table class="t"><tr><th>' + t('零件', 'Part') + '</th><th>'
                 + t('来自', 'From') + '</th></tr>'
                 + '<tr><td class="mono">code_run, file_write/file_patch</td><td>' + t('第 7 课（9 原子工具）', 'lesson 7 (the 9 atomic tools)') + '</td></tr>'
                 + '<tr><td class="mono">update_working_checkpoint</td><td>' + t('第 11 课（工作记忆）', 'lesson 11 (working memory)') + '</td></tr>'
                 + '<tr><td class="mono">start_long_term_update</td><td>' + t('第 12 课（长期记忆）', 'lesson 12 (long-term memory)') + '</td></tr>'
                 + '<tr><td>' + t('探索→结晶→召回 闭环', 'explore→crystallize→recall loop') + '</td><td>' + t('第 20 课（自进化）', 'lesson 20 (self-evolution)') + '</td></tr></table>')
            + c.qa(t, '❓ 为什么“没有新东西”反而是优点', 'Why "nothing new" is a strength',
                   '<p>' + t(
                       '正因为每块积木都<strong>小而正交、可自由拼接</strong>，“造技能”才不需要额外发明任何机制。'
                       '与其堆功能，不如把少数几件事做对，再让它们组合长出无穷——这是 GA 最深的设计取向。',
                       'Precisely because every block is <strong>small, orthogonal and freely composable</strong>, '
                       '"building a skill" needs no extra machinery. Rather than piling on features, get a few things '
                       'right and let them combine without end — GA\'s deepest design orientation.') + '</p>')
            + c.qa(t, '⚠️ 常见误解', 'A common misconception',
                   '<p>' + t(
                       '很多人以为“学会新技能”需要装插件、改框架代码。在 GA 里完全不用：技能只是 '
                       '<span class="inline">memory/</span> 下多出来的一个 <span class="inline">*_sop.md</span>，'
                       '加上 L1 索引里多出的一行——种子代码一行没动。',
                       'Many assume "learning a new skill" needs plugins or framework edits. In GA it needs neither: a '
                       'skill is just one more <span class="inline">*_sop.md</span> under '
                       '<span class="inline">memory/</span> plus one more line in the L1 index — the seed code is '
                       'untouched.') + '</p>'))

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像第一次去一个陌生小区送货：你得边问边找、走几条冤枉路；但只要这一趟<strong>真送到了</strong>，你就把'
            '“几号门、哪个单元、门禁密码”记进备忘。第二趟，导航直达，再不绕路。GA 的“造技能”就是把这本送货备忘<strong>自动写下来</strong>。',
            'Like delivering to an unfamiliar neighborhood for the first time: you ask around and take a few wrong turns; '
            'but once this trip <strong>actually succeeds</strong>, you note "which gate, which unit, the door code". The '
            'second trip, navigation takes you straight there. GA\'s "build a skill" simply <strong>writes that delivery '
            'note down automatically</strong>.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('第一次：记目标 → 探索试错 → 验证成功 → 结晶为技能。',
            'First time: capture goal → explore & iterate → verify success → crystallize a skill.') + '</li>'
        + '<li>' + t('之后每次：顺着技能库一句话召回，不再重复试错。',
            'Every time after: recall from the skill library in one sentence, no repeated trial and error.') + '</li>'
        + '<li>' + t('全程没有新机制，只是把工具 + 记忆按自进化闭环用了一遍。',
            'No new mechanism throughout — just tools + memory used once along the self-evolution loop.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '注意这一课<strong>没有引入任何新东西</strong>：工具是第 7 课的、记忆是第 11–12 课的、闭环是第 20 课的。'
            '“造技能”之所以成立，正因为前面每块积木都<strong>小而正交、能自由拼接</strong>。这就是 GenericAgent 最深的设计取向——'
            '与其堆功能，不如把少数几件事做对，然后让它们<strong>互相组合，长出无穷</strong>。',
            'Notice this lesson <strong>introduces nothing new</strong>: the tools are from lesson 7, the memory from '
            'lessons 11–12, the loop from lesson 20. "Build a skill" holds together precisely because every earlier block '
            'is <strong>small, orthogonal and freely composable</strong>. This is GenericAgent\'s deepest design '
            'orientation — rather than piling on features, get a few things right and let them <strong>combine to grow '
            'without end</strong>.',
        )
        + '</div>'
    )


def lesson_22(t):
    """扩展前端 / 接入新 IM / Extending Frontends."""
    return (
        '<p class="lead">'
        + t(
            '还记得第 5 课说的“前端只是脸、内核是同一套循环”吗？这一课就把它落到代码：要接入一个新平台，'
            '你只需写一层<strong>薄薄的适配器</strong>，把平台的收发消息接到 GA 的内核上——其余一律复用。',
            'Remember lesson 5\'s "the frontend is just a face; the core is the same loop"? This lesson puts that into '
            'code: to add a new platform, you only write a <strong>thin adapter</strong> connecting the platform\'s '
            'message I/O to GA\'s core — everything else is reused.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '每个前端文件做的事都一样：<strong>① 把平台收到的消息喂给 GA 内核；② 把 GA 的输出发回平台。</strong>'
            '通用的命令处理、消息装配都集中在 chatapp_common 里复用。需要让<strong>多个 Agent 协作</strong>时，'
            '还有一个 conductor 做编排。',
            'Every frontend file does the same thing: <strong>(1) feed messages the platform receives into GA\'s core; '
            '(2) send GA\'s output back to the platform.</strong> Shared command handling and message assembly live in '
            'chatapp_common for reuse. When you need <strong>multiple agents to collaborate</strong>, there is also a '
            'conductor for orchestration.',
        )
        + '</p></div>'

        + '<h2>' + t('接入一个新平台', 'Wiring a new platform') + '</h2>'
        + '<div class="vflow">'
        + '<div class="step"><div class="num">1</div><div class="sc"><h3>'
        + t('接内核', 'Connect the core') + '</h3><p class="mono">from agentmain import GenericAgent</p><p>'
        + t('每个 frontends/*app.py 都从这里拿到同一套 Agent 入口。',
            'Every frontends/*app.py gets the same agent entry from here.') + '</p></div></div>'
        + '<div class="step"><div class="num">2</div><div class="sc"><h3>'
        + t('复用通用逻辑', 'Reuse common logic') + '</h3><p>'
        + t('命令（/new、/continue 等）与消息装配走 chatapp_common，不必重写。',
            'Commands (/new, /continue …) and message assembly go through chatapp_common; no rewriting.') + '</p></div></div>'
        + '<div class="step"><div class="num">3</div><div class="sc"><h3>'
        + t('写平台 I/O', 'Write platform I/O') + '</h3><p>'
        + t('只剩平台特有的收发：监听消息 → 交给内核 → 把回复发回去。',
            'Only platform-specific I/O remains: listen for messages → hand to the core → send the reply back.') + '</p></div></div>'
        + '</div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('现成范例：', 'Ready examples: ')
        + '<span class="inline">frontends/tgapp.py · wechatapp.py · fsapp.py</span>'
        + t(' 等，每个都是“接内核 + 平台 I/O”的薄适配器。',
            ' and more, each a thin "core + platform I/O" adapter.') + '</li>'
        + '<li>' + t('共享逻辑在 ', 'Shared logic is in ')
        + '<span class="inline">frontends/chatapp_common.py</span>'
        + t('（命令清单、/new、/continue 的处理都在这里）。',
            ' (the command list and the handling of /new, /continue live here).') + '</li>'
        + '<li>' + t('多 Agent 编排在 ', 'Multi-agent orchestration is in ')
        + '<span class="inline">frontends/conductor.py</span>'
        + t('（FastAPI + WebSocket，import GenericAgent 来管理多个实例；可用 /conductor 触发）。',
            ' (FastAPI + WebSocket, importing GenericAgent to manage multiple instances; triggerable via /conductor).') + '</li>'
        + '</ul></div>'

        + c.deepdive_heading(t)
        + c.accordion(t, 1, '薄适配器骨架：一个最小前端长什么样',
            'A thin-adapter skeleton: what a minimal frontend looks like',
            c.qa(t, '🧪 最小适配器骨架', 'A minimal adapter skeleton',
                 c.codefile('frontends/myapp.py', 'skeleton',
                     'from agentmain import GeneraticAgent   # '
                     + t('GenericAgent 的别名', 'alias of GenericAgent') + '\n'
                     'agent = GeneraticAgent()\n\n'
                     'def on_platform_message(chat_id, text):\n'
                     '    dq = agent.put_task(text, source="myapp")   # '
                     + t('① 喂给内核', '(1) feed the core') + '\n'
                     '    while True:\n'
                     '        item = dq.get()\n'
                     '        if "done" in item:\n'
                     '            send_back(chat_id, item["done"])     # '
                     + t('② 发回平台', '(2) send back to platform') + '\n'
                     '            break'))
            + c.qa(t, '⚙️ put_task → done 内部怎么走', 'How put_task → done works inside',
                   '<p>' + t(
                       '内核交互只有一条主线：<span class="inline">agent.put_task(text, source=...)</span> 返回一个显示队列 '
                       '<span class="mono">dq</span>，前端循环 <span class="mono">dq.get()</span> 取流式输出，遇到带 '
                       '<span class="mono">"done"</span> 的项就是最终回复。<span class="inline">chatapp_common.py</span> 里的 '
                       '<span class="inline">AgentChatMixin.run_agent</span> 正是这个循环的标准实现（含 ping 保活）。',
                       'Core interaction has one main line: <span class="inline">agent.put_task(text, source=...)</span> '
                       'returns a display queue <span class="mono">dq</span>; the frontend loops '
                       '<span class="mono">dq.get()</span> for streamed output, and an item carrying '
                       '<span class="mono">"done"</span> is the final reply. '
                       '<span class="inline">AgentChatMixin.run_agent</span> in '
                       '<span class="inline">chatapp_common.py</span> is exactly this loop (with keep-alive pings).') + '</p>')
            + c.qa(t, '❓ 为什么类名有两种写法', 'Why two class spellings exist',
                   '<p>' + t(
                       '规范类名是 <span class="inline">GenericAgent</span>；<span class="inline">agentmain.py</span> 里有一行 '
                       '<span class="inline">GeneraticAgent = GenericAgent</span> 别名，于是大多数 '
                       '<span class="inline">frontends/*app.py</span>（tgapp / wechatapp / fsapp …）写的是 '
                       '<span class="inline">from agentmain import GeneraticAgent</span>，而 '
                       '<span class="inline">conductor.py</span> 用规范名 <span class="inline">GenericAgent</span>。两者等价。',
                       'The canonical class is <span class="inline">GenericAgent</span>; '
                       '<span class="inline">agentmain.py</span> has a line '
                       '<span class="inline">GeneraticAgent = GenericAgent</span>, so most '
                       '<span class="inline">frontends/*app.py</span> (tgapp / wechatapp / fsapp …) write '
                       '<span class="inline">from agentmain import GeneraticAgent</span>, while '
                       '<span class="inline">conductor.py</span> uses the canonical '
                       '<span class="inline">GenericAgent</span>. They are equivalent.') + '</p>'))
        + c.accordion(t, 2, 'chatapp_common 到底复用了什么',
            'What chatapp_common actually reuses for you',
            c.qa(t, '🧪 开箱即用的零件清单', 'Out-of-the-box parts',
                 '<table class="t"><tr><th>' + t('零件', 'Part') + '</th><th>'
                 + t('作用', 'Role') + '</th></tr>'
                 + '<tr><td class="mono">AgentChatMixin</td><td>'
                 + t('命令分发 + run_agent 循环', 'command dispatch + the run_agent loop') + '</td></tr>'
                 + '<tr><td class="mono">HELP_COMMANDS</td><td>'
                 + t('统一命令清单（/help /status /stop /new …）', 'unified command list (/help /status /stop /new …)') + '</td></tr>'
                 + '<tr><td class="mono">clean_reply / split_text</td><td>'
                 + t('清洗标签、按长度切分消息', 'strip tags, split messages by length') + '</td></tr>'
                 + '<tr><td class="mono">extract_files / FILE_HINT</td><td>'
                 + t('从回复里取出 [FILE:...] 附件', 'pull [FILE:...] attachments from replies') + '</td></tr>'
                 + '<tr><td class="mono">format_restore / require_runtime</td><td>'
                 + t('恢复历史、单实例守护', 'restore history, single-instance guard') + '</td></tr></table>')
            + c.qa(t, '⚙️ 命令是怎么分发的', 'How commands are dispatched',
                   '<p>' + t(
                       '<span class="inline">AgentChatMixin.handle_command</span> 统一解析斜杠命令：'
                       '<span class="inline">/stop</span> 调 <span class="inline">agent.abort()</span>、'
                       '<span class="inline">/new</span> 重置对话、<span class="inline">/continue</span> 列出可恢复会话、'
                       '<span class="inline">/btw</span> 临时插问、<span class="inline">/review</span> 走代码审查——'
                       '前端<strong>一行都不用重写</strong>，只要继承这个 Mixin。',
                       '<span class="inline">AgentChatMixin.handle_command</span> parses slash commands centrally: '
                       '<span class="inline">/stop</span> calls <span class="inline">agent.abort()</span>, '
                       '<span class="inline">/new</span> resets the conversation, '
                       '<span class="inline">/continue</span> lists resumable sessions, '
                       '<span class="inline">/btw</span> asks a side question, '
                       '<span class="inline">/review</span> runs code review — the frontend '
                       '<strong>rewrites none of it</strong>, it just inherits the Mixin.') + '</p>')
            + c.qa(t, '🔀 真实范例对比', 'Real examples compared',
                   '<p>' + t(
                       '<span class="inline">tgapp.py</span>（Telegram）、<span class="inline">wechatapp.py</span>（微信）、'
                       '<span class="inline">fsapp.py</span>（飞书）做的都是同一件事：import 内核、复用 '
                       '<span class="inline">chatapp_common</span>、只写各自平台的收发 I/O。差异全在最外圈的平台 SDK，'
                       '内核与命令逻辑完全共享。',
                       '<span class="inline">tgapp.py</span> (Telegram), <span class="inline">wechatapp.py</span> (WeChat) '
                       'and <span class="inline">fsapp.py</span> (Feishu) all do the same thing: import the core, reuse '
                       '<span class="inline">chatapp_common</span>, and write only their own platform I/O. All difference '
                       'sits in the outermost platform SDK; core and command logic are fully shared.') + '</p>'))
        + c.accordion(t, 3, 'conductor.py：让多个 GA 实例协作',
            'conductor.py: making multiple GA instances collaborate',
            c.qa(t, '🧪 它是什么', 'What it is',
                 '<p>' + t(
                     '<span class="inline">frontends/conductor.py</span> 是一个 FastAPI + WebSocket 服务（'
                     '<span class="inline">from agentmain import GenericAgent</span>，默认跑在 '
                     '<span class="mono">127.0.0.1:8900</span>）。它有一个<strong>总管</strong> '
                     '<span class="inline">Conductor</span>（自己也是一个 GenericAgent），外加一个 '
                     '<span class="inline">SubagentPool</span> 管理若干子 agent 实例。',
                     '<span class="inline">frontends/conductor.py</span> is a FastAPI + WebSocket service '
                     '(<span class="inline">from agentmain import GenericAgent</span>, default '
                     '<span class="mono">127.0.0.1:8900</span>). It has a <strong>master</strong> '
                     '<span class="inline">Conductor</span> (itself a GenericAgent) plus a '
                     '<span class="inline">SubagentPool</span> managing several sub-agent instances.') + '</p>')
            + c.qa(t, '⚙️ 多实例怎么起、怎么通信', 'How instances start and talk',
                   '<p>' + t(
                       '<span class="inline">SubagentPool.start_subagent(prompt)</span> 每次 '
                       '<span class="inline">GenericAgent()</span> 新建一个实例、起一个 runner 线程，再 '
                       '<span class="inline">put_task</span> 派活；运行进度通过 <span class="inline">/ws</span> WebSocket '
                       '广播到前端 <span class="inline">conductor.html</span>。REST 面板有 '
                       '<span class="mono">/subagent、/chat、/approval</span> 等。',
                       '<span class="inline">SubagentPool.start_subagent(prompt)</span> creates a fresh '
                       '<span class="inline">GenericAgent()</span> each time, spins a runner thread, then '
                       '<span class="inline">put_task</span>s the work; progress is broadcast to the front-end '
                       '<span class="inline">conductor.html</span> over the <span class="inline">/ws</span> WebSocket. '
                       'REST endpoints include <span class="mono">/subagent, /chat, /approval</span>.') + '</p>')
            + c.qa(t, '⚠️ 每个子 agent 都是独立实例', 'Each sub-agent is an independent instance',
                   '<p>' + t(
                       '注意 <span class="inline">SubagentPool</span> 里每个 <span class="inline">SubAgentState</span> '
                       '都持有<strong>自己的 GenericAgent 对象</strong>，互不共享运行态——这与 Incubator“每节点独立记忆”'
                       '的理念一致：协作靠消息传递，而不是共享内存，避免一个 agent 的状态污染另一个。',
                       'Note each <span class="inline">SubAgentState</span> in '
                       '<span class="inline">SubagentPool</span> holds <strong>its own GenericAgent object</strong>, '
                       'sharing no runtime state — consistent with Incubator\'s "independent memory per node": '
                       'collaboration is by message passing, not shared memory, so one agent\'s state cannot pollute '
                       'another\'s.') + '</p>'))

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像给同一台游戏主机配一个新手柄：主机（内核）和游戏（能力）都不用动，你只要做一个<strong>转接头</strong>，'
            '把新手柄的按键信号翻译成主机认识的格式。接微信、接钉钉，都是在做这种“转接头”，工作量小得惊人。',
            'Like adding a new controller to the same game console: the console (core) and games (capabilities) stay '
            'untouched; you only make an <strong>adapter</strong> that translates the new controller\'s button signals '
            'into a format the console understands. Wiring WeChat or DingTalk is exactly making such an "adapter" — '
            'surprisingly little work.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('接新平台 = 写一个薄适配器：from agentmain import GenericAgent + 平台 I/O。',
            'A new platform = a thin adapter: from agentmain import GenericAgent + platform I/O.') + '</li>'
        + '<li>' + t('命令与消息装配复用 chatapp_common，不必重写。',
            'Commands and message assembly reuse chatapp_common; no rewriting.') + '</li>'
        + '<li>' + t('要多 Agent 协作，用 conductor.py 编排（/conductor）。',
            'For multi-agent collaboration, orchestrate with conductor.py (/conductor).') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '“接一个新前端只要几十行”，是第 5 课<strong>界面/内核解耦</strong>结出的果。因为内核对“消息从哪来”一无所知，'
            '前端就退化成纯粹的 I/O 转接——平台再多，内核一行都不用改。这正是好边界的价值：<strong>改动被牢牢锁在最外圈</strong>，'
            '核心始终稳如磐石。',
            '"A new frontend in a few dozen lines" is the fruit of lesson 5\'s <strong>interface/core decoupling</strong>. '
            'Because the core knows nothing about "where a message comes from", a frontend degenerates into pure I/O '
            'adaptation — no matter how many platforms, the core changes not a line. This is the value of good '
            'boundaries: <strong>change is locked into the outermost ring</strong>, while the core stays rock-solid.',
        )
        + '</div>'
    )


