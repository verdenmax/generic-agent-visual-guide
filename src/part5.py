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
        + '<div class="step"><div class="num">1</div><div class="sc"><h4>'
        + t('新任务', 'New task') + '</h4><p>'
        + t('来了一件它还不会的事。', 'Something it cannot yet do arrives.') + '</p></div></div>'
        + '<div class="step"><div class="num">2</div><div class="sc"><h4>'
        + t('自主探索', 'Autonomous exploration') + '</h4><p>'
        + t('用 code_run 装依赖、写脚本、调试，直到<strong>行动验证成功</strong>。',
            'Use code_run to install deps, write scripts, debug, until <strong>action-verified success</strong>.') + '</p></div></div>'
        + '<div class="step"><div class="num">3</div><div class="sc"><h4>'
        + t('结晶为 Skill', 'Crystallize into a Skill') + '</h4><p>'
        + t('start_long_term_update 把要点写进 L3 SOP，并在 L1 索引登记。',
            'start_long_term_update writes the essentials into an L3 SOP and registers it in the L1 index.') + '</p></div></div>'
        + '<div class="step"><div class="num">4</div><div class="sc"><h4>'
        + t('下次直接召回', 'Direct recall next time') + '</h4><p>'
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
        + '<div class="step"><div class="num">1</div><div class="sc"><h4>'
        + t('记住目标', 'Capture the goal') + '</h4><p>'
        + t('收到任务，先用 update_working_checkpoint 记下“要读微信记录”和关键约束。',
            'On receiving the task, use update_working_checkpoint to note "read WeChat messages" and key constraints.') + '</p></div></div>'
        + '<div class="step"><div class="num">2</div><div class="sc"><h4>'
        + t('探索与试错', 'Explore & iterate') + '</h4><p>'
        + t('用 code_run 装依赖、定位数据库、写读取脚本，失败就读报错再改。',
            'Use code_run to install deps, locate the database, write a read script; on failure, read the error and fix.') + '</p></div></div>'
        + '<div class="step"><div class="num">3</div><div class="sc"><h4>'
        + t('验证成功', 'Verify success') + '</h4><p>'
        + t('真正跑通、读出消息——这一步是“能不能记忆”的前提（无行动，不记忆）。',
            'Actually run it and read out the messages — the prerequisite for "may we remember" (no execution, no memory).') + '</p></div></div>'
        + '<div class="step"><div class="num">4</div><div class="sc"><h4>'
        + t('结晶为技能', 'Crystallize a skill') + '</h4><p>'
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
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


