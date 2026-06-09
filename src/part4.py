"""Part 4 — 进阶能力 / Advanced Capabilities (lessons 15–19).

Each lesson is a ``lesson(t)`` function. ``t('中文', 'English')`` wraps every
piece of prose; structure, diagrams and code are written once and shared by
both language renders. All technical claims are grounded in the real
GenericAgent source (memory/ui_detect.py, ocr_utils.py, ljqCtrl.py, adb_ui.py,
TMWebDriver.py, simphtml.py, reflect/*).

Authoring conventions are documented at the top of ``part1.py`` — follow the
same 5-card lesson format (🌍 macro / 🔬 detail / 🧩 analogy / ✅ key /
💡 spark) and the ``.inline`` (prose code) vs ``.mono`` (dense components) rule.
"""

def lesson_15(t):
    """计算机控制 · 视觉 / Computer Control · Vision."""
    return (
        '<p class="lead">'
        + t(
            '当一个界面没有 API、也没有可读的 HTML 时，GenericAgent 还能怎么操作它？答案是<strong>用眼睛看</strong>：'
            '截屏 → 识别出屏幕上的图标与文字 → 拿到它们的坐标 → 像人一样点过去。这一课讲 GA 的视觉链路。',
            'When an interface has no API and no readable HTML, how can GenericAgent still operate it? The answer '
            'is <strong>look at it</strong>: screenshot → recognize the icons and text on screen → get their '
            'coordinates → click there like a human. This lesson covers GA\'s vision pipeline.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '视觉链路是一条流水线：<strong>截屏 → 检测 → 定位 → 行动</strong>。检测同时用上 YOLO（找图标这类视觉元素）'
            '和 OCR（认文字），输出一串带坐标的元素。拿到坐标后，就交给下一课的“鼠标键盘”去点、去敲。',
            'The vision pipeline is an assembly line: <strong>capture → detect → locate → act</strong>. Detection '
            'uses both YOLO (to find visual elements like icons) and OCR (to read text), emitting a list of '
            'elements with coordinates. With coordinates in hand, the next lesson\'s "mouse & keyboard" does the '
            'clicking and typing.',
        )
        + '</p></div>'

        + '<h2>' + t('截屏到行动', 'From screenshot to action') + '</h2>'
        + '<div class="flow">'
        + '<div class="node"><div class="nt">' + t('截屏', 'Capture') + '</div>'
        + '<div class="nd">' + t('屏幕 / 窗口图', 'screen / window image') + '</div></div>'
        + '<div class="arrow">→</div>'
        + '<div class="node hl"><div class="nt">' + t('检测', 'Detect') + '</div>'
        + '<div class="nd">YOLO + OCR</div></div>'
        + '<div class="arrow">→</div>'
        + '<div class="node"><div class="nt">' + t('定位', 'Locate') + '</div>'
        + '<div class="nd">' + t('物理坐标 bbox', 'physical bbox') + '</div></div>'
        + '<div class="arrow">→</div>'
        + '<div class="node"><div class="nt">' + t('行动', 'Act') + '</div>'
        + '<div class="nd">' + t('点击 / 输入', 'click / type') + '</div></div>'
        + '</div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('UI 元素检测在 ', 'UI element detection is in ')
        + '<span class="inline">memory/ui_detect.py: detect()</span>'
        + t('（YOLO + RapidOCR），返回 bbox / type（icon|text）/ label / confidence。',
            ' (YOLO + RapidOCR), returning bbox / type (icon|text) / label / confidence.') + '</li>'
        + '<li>' + t('纯文字识别在 ', 'Plain text recognition is in ')
        + '<span class="inline">memory/ocr_utils.py</span>'
        + t('（本地 rapidocr）；远程桌面下用 ', ' (local rapidocr); under remote desktop use ')
        + '<span class="inline">ocr_window(hwnd)</span>'
        + t(' 避免黑屏。', ' to avoid black screenshots.') + '</li>'
        + '<li>' + t('无文字图标可由视觉大模型保底：', 'Iconless elements can fall back to a vision LLM: ')
        + '<span class="inline">memory/vision_api.template.py</span>'
        + t('；整套流程的要点见 ', '; the playbook is in ')
        + '<span class="inline">memory/vision_sop.md</span>' + t('。', '.') + '</li>'
        + '<li>' + t('一个反复强调的坑：截屏分析后<strong>必须用物理坐标</strong>（与 ljqCtrl 一致）。',
            'A repeatedly stressed pitfall: after screenshot analysis you <strong>must use physical '
            'coordinates</strong> (consistent with ljqCtrl).') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像给 Agent 装上一双<strong>眼睛</strong>加一根<strong>会指的手指</strong>：它看一眼屏幕，认出“那个蓝色的'
            '发送按钮在右下角”，然后把手指准确地点到那个像素位置。哪怕这个软件压根没有给程序留接口，它也能照用不误。',
            'Like giving the agent a pair of <strong>eyes</strong> plus a <strong>pointing finger</strong>: it '
            'glances at the screen, recognizes "that blue Send button is at the bottom-right", and lands its finger '
            'precisely on that pixel. Even if the software offers no API for programs at all, it can still use it.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('视觉链路：截屏 → 检测（YOLO+OCR）→ 定位 → 行动。',
            'Vision pipeline: capture → detect (YOLO+OCR) → locate → act.') + '</li>'
        + '<li>' + t('detect() 返回带坐标的元素；无文字图标可用 VLM 保底。',
            'detect() returns elements with coordinates; iconless elements can fall back to a VLM.') + '</li>'
        + '<li>' + t('始终使用物理坐标，远程桌面用 ocr_window 防黑屏。',
            'Always use physical coordinates; use ocr_window under remote desktop to avoid black screens.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '视觉是 GA 的“<strong>万能兜底</strong>”：API、HTML 都失效时，只要屏幕能显示，它就能操作。这把可控范围从'
            '“有接口的软件”一举扩展到“<strong>任何肉眼能用的界面</strong>”——也正因如此，GA 不必为每个 App 预置适配，'
            '看得见，就够了。',
            'Vision is GA\'s "<strong>universal fallback</strong>": when APIs and HTML both fail, as long as the '
            'screen shows something, it can operate. This extends the controllable scope from "software with an API" '
            'to "<strong>any interface a human eye can use</strong>" — which is exactly why GA need not preload an '
            'adapter for every app. If it can see it, that is enough.',
        )
        + '</div>'
    )


def lesson_16(t):
    """输入与移动端 / Input & Mobile (ADB)."""
    return (
        '<p class="lead">'
        + t(
            '上一课让 Agent “看见”，这一课让它“动手”：在电脑上<strong>控制鼠标键盘</strong>，在手机上<strong>通过 '
            'ADB 驱动安卓</strong>。看得见、点得到，GA 对设备的控制闭环才算合上。',
            'The last lesson let the agent "see"; this one lets it "act": on a computer it <strong>controls the '
            'mouse and keyboard</strong>, and on a phone it <strong>drives Android over ADB</strong>. Seeing plus '
            'touching closes GA\'s control loop over a device.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '两条“手”的通路：在桌面端，<span class="inline">ljqCtrl</span> 直接调 Win32 API 移动鼠标、点击、敲键；'
            '在移动端，<span class="inline">adb_ui</span> 用 ADB / uiautomator2 把安卓界面 dump 出来再操作。'
            '它们都和上一课的视觉配合——视觉给坐标，输入去执行。',
            'Two "hand" paths: on the desktop, <span class="inline">ljqCtrl</span> calls Win32 APIs directly to move '
            'the mouse, click and type; on mobile, <span class="inline">adb_ui</span> uses ADB / uiautomator2 to dump '
            'and drive the Android UI. Both pair with the previous lesson\'s vision — vision gives coordinates, input '
            'carries them out.',
        )
        + '</p></div>'

        + '<h2>' + t('两条输入通路', 'Two input paths') + '</h2>'
        + '<div class="cols">'
        + '<div class="col"><h4>' + t('桌面：鼠标键盘', 'Desktop: mouse & keyboard') + '</h4><p>'
        + t('ljqCtrl 用 Click(x,y)、SetCursorPos、Press("ctrl+v") 等操作，全程<strong>物理坐标</strong>，并提供 DPI 安全的窗口截图。',
            'ljqCtrl uses Click(x,y), SetCursorPos, Press("ctrl+v") and more, all in <strong>physical '
            'coordinates</strong>, plus DPI-safe window capture.') + '</p></div>'
        + '<div class="col"><h4>' + t('移动：ADB 安卓', 'Mobile: ADB Android') + '</h4><p>'
        + t('adb_ui 优先用 uiautomator2 dump 界面层级（动画密集的 App 更稳），原生 adb 兜底，必要时配合视觉补盲。',
            'adb_ui prefers uiautomator2 to dump the UI hierarchy (steadier for animation-heavy apps), with native '
            'adb as fallback, aided by vision when needed.') + '</p></div>'
        + '</div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('桌面输入在 ', 'Desktop input is in ')
        + '<span class="inline">memory/ljqCtrl.py</span>'
        + t('（Click / SetCursorPos / Press / FindBlock / GrabWindow，基于 win32api）；要点见 ',
            ' (Click / SetCursorPos / Press / FindBlock / GrabWindow, on win32api); the playbook is ')
        + '<span class="inline">memory/ljqCtrl_sop.md</span>' + t('。', '.') + '</li>'
        + '<li>' + t('一条硬规矩：<strong>始终用物理坐标</strong>，且严禁 import pyautogui（会污染 win32api）。',
            'A hard rule: <strong>always use physical coordinates</strong>, and never import pyautogui (it pollutes '
            'win32api).') + '</li>'
        + '<li>' + t('安卓控制在 ', 'Android control is in ')
        + '<span class="inline">memory/adb_ui.py</span>'
        + t('（u2 优先、原生 adb fallback，dump 配合 ui_detect 补盲）；背景见 ',
            ' (u2 first, native adb fallback, dump combined with ui_detect to fill gaps); background in ')
        + '<span class="inline">memory/computer_use.md</span>' + t('。', '.') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '如果说视觉是“眼睛”，这一课就是“<strong>手</strong>”：电脑上的手是鼠标和键盘，手机上的手是隔空操作的遥控器（ADB）。'
            '眼睛找到“发送按钮在哪”，手负责真的把它按下去——缺一不可。',
            'If vision is the "eyes", this lesson is the "<strong>hands</strong>": on a computer the hand is the mouse '
            'and keyboard; on a phone it is a remote control acting at a distance (ADB). The eyes find "where the Send '
            'button is", the hands actually press it — neither works alone.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('桌面用 ljqCtrl（win32api）做鼠标键盘；移动用 adb_ui（u2/adb）控安卓。',
            'Desktop uses ljqCtrl (win32api) for mouse/keyboard; mobile uses adb_ui (u2/adb) to drive Android.') + '</li>'
        + '<li>' + t('始终物理坐标；桌面端严禁 import pyautogui。',
            'Always physical coordinates; never import pyautogui on the desktop.') + '</li>'
        + '<li>' + t('输入与视觉配合：视觉给坐标，输入去点击/敲键。',
            'Input pairs with vision: vision gives coordinates, input clicks/types.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '把“手”做成<strong>最底层、最通用</strong>的能力，是 GA 强执行力的根。它不依赖某个 App 开放接口，而是回到人类操作设备的'
            '<strong>最小公分母</strong>——点、敲、滑。于是“订杯奶茶”“群发微信”“驱动支付宝”这些任务，本质上都被还原成了'
            '“看一眼 + 点几下”，用同一套手在真实设备上完成。',
            'Making the "hands" the <strong>lowest-level, most general</strong> capability is the root of GA\'s strong '
            'execution. It does not depend on any app exposing an API; it falls back to the <strong>lowest common '
            'denominator</strong> of how humans operate devices — tap, type, swipe. So tasks like "order a milk tea", '
            '"mass-send WeChat", "drive Alipay" all reduce to "glance + a few taps", done by the same hands on real '
            'devices.',
        )
        + '</div>'
    )


def lesson_17(t):
    """浏览器注入与 Web 工具 / Browser Injection & Web Tools."""
    return (
        '<p class="lead">'
        + t(
            'GenericAgent 操作网页有个杀手锏：它注入你<strong>真实的浏览器</strong>，而不是另起一个干净的无头浏览器。'
            '这意味着你的登录态、Cookie、插件全都在——它看到的就是你看到的那个已登录页面。',
            'GenericAgent has a killer feature for the web: it injects into your <strong>real browser</strong> rather '
            'than spinning up a clean headless one. That means your login state, cookies and extensions are all there '
            '— it sees the very logged-in page you see.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '网页能力只有两个工具：<span class="inline">web_scan</span>（看：拿到一份<strong>简化后</strong>的页面与标签页列表）'
            '和 <span class="inline">web_execute_js</span>（做：在页面里执行 JS）。背后由一个 WebSocket 桥把命令送进真实浏览器，'
            '页面则先被<strong>大幅简化</strong>再交给模型，省 token。',
            'There are only two web tools: <span class="inline">web_scan</span> (look: get a <strong>simplified</strong> '
            'page plus the tab list) and <span class="inline">web_execute_js</span> (do: run JS in the page). Behind '
            'them a WebSocket bridge delivers commands into the real browser, and the page is <strong>heavily '
            'simplified</strong> before reaching the model to save tokens.',
        )
        + '</p></div>'

        + '<div class="codefile"><div class="cf-head"><span class="dot"></span>'
        + '<span class="path">ga.py</span><span class="ln">web tools → simphtml</span></div>'
        + '<pre>'
        + '<span class="kw">import</span> simphtml\n'
        + '<span class="kw">from</span> TMWebDriver <span class="kw">import</span> TMWebDriver\n'
        + 'driver = TMWebDriver()  <span class="cm"># ' + t('连真实浏览器的 WS 桥', 'WS bridge to the real browser') + '</span>\n'
        + '\n'
        + '<span class="cm"># web_scan ' + t('看页面', 'look at the page') + '</span>\n'
        + 'content = simphtml.get_html(driver, cutlist=<span class="nb">True</span>, maxchars=<span class="nb">35000</span>)\n'
        + '\n'
        + '<span class="cm"># web_execute_js ' + t('操作页面', 'act on the page') + '</span>\n'
        + 'result = simphtml.execute_js_rich(script, driver)\n'
        + '</pre></div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('注入桥是 ', 'The injection bridge is ')
        + '<span class="inline">TMWebDriver.py</span>'
        + t('：它跑一个 WebSocket 服务，浏览器侧的客户端连回来，从而在<strong>真实浏览器</strong>里执行 JS、保留登录态。',
            ': it runs a WebSocket server that a browser-side client connects back to, executing JS in the '
            '<strong>real browser</strong> and preserving the login session.') + '</li>'
        + '<li>' + t('页面简化是 ', 'Page simplification is ')
        + '<span class="inline">simphtml.py</span>'
        + t('：get_html 把 DOM 压到约 35000 字、去掉隐藏/浮动/被遮挡元素；execute_js_rich 执行 JS 并回收结果。',
            ': get_html shrinks the DOM to ~35000 chars and drops hidden/floating/covered elements; execute_js_rich '
            'runs JS and collects the result.') + '</li>'
        + '<li>' + t('两个工具的封装在 ', 'The two tools are wrapped in ')
        + '<span class="inline">ga.py: do_web_scan / do_web_execute_js</span>'
        + t('；上手与配置见 ', '; setup and usage in ')
        + '<span class="inline">memory/tmwebdriver_sop.md</span>' + t(' 与 ', ' and ')
        + '<span class="inline">memory/web_setup_sop.md</span>' + t('。', '.') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '别的框架像派来一个<strong>陌生的隐身访客</strong>：每次都开一个全新、没登录的浏览器，进站还得重新登录、过验证。'
            'GA 则像在你<strong>自己已经登录好的浏览器</strong>里多了一只“隔空操作的手”——你已经登进去的网站，它直接就能用。',
            'Other frameworks are like sending a <strong>stranger in incognito</strong>: every time a brand-new, '
            'logged-out browser opens and must re-login and pass checks. GA is more like an extra "remote hand" inside '
            '<strong>your own already-logged-in browser</strong> — the sites you are already signed into, it can use '
            'right away.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('两个工具：web_scan（看简化页面）与 web_execute_js（执行 JS）。',
            'Two tools: web_scan (read a simplified page) and web_execute_js (run JS).') + '</li>'
        + '<li>' + t('TMWebDriver 用 WebSocket 注入真实浏览器，保留登录态。',
            'TMWebDriver injects the real browser over WebSocket, preserving the login session.') + '</li>'
        + '<li>' + t('simphtml 把页面压到约 35K 字，省 token；多用 execute_js，少全量 scan。',
            'simphtml shrinks the page to ~35K chars to save tokens; prefer execute_js, scan sparingly.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '“注入真实浏览器”这一个选择，绕开了无数自动化的老大难：免登录、免验证码、和你看到的页面完全一致。再叠加 simphtml 的'
            '<strong>页面简化</strong>，把动辄上百 KB 的 DOM 压成几十 KB——既看得见，又看得起。这正是第 14 课“token 效率”在网页场景的延伸：'
            '<strong>用真实环境换可靠，用简化换便宜</strong>。',
            'The single choice to "inject the real browser" sidesteps countless automation headaches: no re-login, no '
            'captchas, and a page identical to what you see. Layered with simphtml\'s <strong>page simplification</strong>, '
            'a DOM of hundreds of KB shrinks to tens of KB — visible and affordable at once. This extends lesson 14\'s '
            '"token efficiency" to the web: <strong>trade the real environment for reliability, and simplification for '
            'cost</strong>.',
        )
        + '</div>'
    )


def lesson_18(t):
    """反思与编排 / Reflection & Orchestration."""
    return (
        '<p class="lead">'
        + t(
            '前面的循环是“你说一句、它做一段”。但要让 Agent <strong>自己持续推进</strong>、按目标自驱、甚至多个 worker 协作，'
            '就需要一层<strong>反思（reflect）</strong>机制：在循环之外，定时“探一探、推一把”。',
            'The loop so far is "you say something, it does a chunk". But to make the agent <strong>keep going on its '
            'own</strong>, self-drive toward a goal, or even have multiple workers collaborate, you need a layer of '
            '<strong>reflection</strong>: outside the loop, periodically "check and nudge".',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            'reflect/ 下的每个模块都是一个<strong>可插拔的定时探针</strong>：它有自己的检查间隔，每隔一段时间运行 '
            '<span class="inline">check()</span>——如果发现“该干活了”，就<strong>返回一段提示词去唤醒 Agent</strong>，'
            '否则返回 None 保持安静。不同模块对应不同的编排玩法。',
            'Each module under reflect/ is a <strong>pluggable periodic probe</strong>: it has its own check interval and '
            'runs <span class="inline">check()</span> every so often — if it finds "time to act", it <strong>returns a '
            'prompt that wakes the agent</strong>, otherwise it returns None and stays quiet. Different modules map to '
            'different orchestration styles.',
        )
        + '</p></div>'

        + '<h2>' + t('几种编排模块', 'A few orchestration modules') + '</h2>'
        + '<table class="t">'
        + '<tr><th>' + t('模块', 'Module') + '</th><th>' + t('玩法', 'Style') + '</th></tr>'
        + '<tr><td class="mono">goal_mode.py</td><td>'
        + t('目标模式：按一份 state 持续自驱，直到预算耗尽。',
            'Goal mode: keep self-driving from a state file until the budget runs out.') + '</td></tr>'
        + '<tr><td class="mono">scheduler.py</td><td>'
        + t('调度器：类 cron 的定时任务（带端口锁防重复启动）。',
            'Scheduler: cron-like timed tasks (with a port lock to prevent double-start).') + '</td></tr>'
        + '<tr><td class="mono">checklist_master.py</td><td>'
        + t('清单主控：轮询一个清单/看板，逐项推进。',
            'Checklist master: poll a checklist/board and advance items one by one.') + '</td></tr>'
        + '<tr><td class="mono">agent_team_worker.py</td><td>'
        + t('团队 worker：从共享 BBS 接单，多 Agent 协作。',
            'Team worker: pick up jobs from a shared BBS for multi-agent collaboration.') + '</td></tr>'
        + '</table>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('反思模块由 ', 'Reflection modules are launched by ')
        + '<span class="inline">agentmain.py --reflect reflect/&lt;module&gt;.py</span>'
        + t(' 启动；每个模块约定有 INTERVAL、init(a)、check() 三样东西。',
            '; each module conventionally has INTERVAL, init(a) and check().') + '</li>'
        + '<li>' + t('check() 的返回值就是“唤醒提示”：',
            'The return value of check() is the "wake prompt": ')
        + t('返回字符串 → 注入并唤醒 Agent；返回 None → 本次跳过。',
            'return a string → inject and wake the agent; return None → skip this round.') + '</li>'
        + '<li>' + t('goal_mode 读 ', 'goal_mode reads ')
        + '<span class="inline">GOAL_STATE</span>'
        + t(' 指定的 state json；scheduler 用一个端口锁（127.0.0.1:45762）防止重复启动；agent_team_worker 预检 BBS（见 assets/agent_bbs.py）。',
            ' a state json pointed to by GOAL_STATE; scheduler uses a port lock (127.0.0.1:45762) to prevent '
            'double-start; agent_team_worker pre-checks a BBS (see assets/agent_bbs.py).') + '</li>'
        + '</ul></div>'

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像给一个埋头干活的工人配了几位<strong>不同的工头</strong>：目标工头盯着“这件事没做完就别停”，'
            '排班工头按点喊“到时间了，去做那件事”，看板工头盯着任务清单逐条派活，接单工头则去公告栏揽活。'
            '工人（Agent 循环）还是那个工人，是工头们决定了他<strong>何时、为何</strong>再次动起来。',
            'Like giving a heads-down worker several <strong>different foremen</strong>: the goal foreman insists "do '
            'not stop until this is done", the scheduling foreman calls "it is time, go do that", the board foreman '
            'assigns items off a checklist, and the job-board foreman picks up postings. The worker (the agent loop) is '
            'the same worker; the foremen decide <strong>when and why</strong> he starts moving again.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('reflect/ 模块是循环之外的定时探针，用 check() 决定是否唤醒 Agent。',
            'reflect/ modules are periodic probes outside the loop; check() decides whether to wake the agent.') + '</li>'
        + '<li>' + t('四种玩法：目标自驱、定时调度、清单主控、团队接单。',
            'Four styles: goal self-drive, timed scheduling, checklist master, team job-board.') + '</li>'
        + '<li>' + t('用 agentmain.py --reflect 启动；约定 INTERVAL / init / check。',
            'Launched via agentmain.py --reflect; the convention is INTERVAL / init / check.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '编排没有被塞进核心循环，而是抽成一层<strong>统一约定的探针</strong>：所有花样——自驱、定时、看板、协作——都被归一成同一个问题'
            '“<span class="inline">check() 这次要不要唤醒、用什么提示唤醒</span>”。于是“加一种新编排”=“写一个新 reflect 模块”，'
            '内核依旧是那 100 行。复杂的多 Agent 行为，由简单的探针<strong>组合</strong>而成。',
            'Orchestration is not stuffed into the core loop but abstracted into a layer of <strong>uniformly-agreed '
            'probes</strong>: every style — self-drive, scheduling, boards, collaboration — reduces to the same question, '
            '"<span class="inline">should check() wake it this time, and with what prompt</span>". So "add a new '
            'orchestration" = "write a new reflect module", while the core stays 100 lines. Complex multi-agent behavior '
            'is <strong>composed</strong> from simple probes.',
        )
        + '</div>'
    )


def lesson_19(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


