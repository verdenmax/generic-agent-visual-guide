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
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_18(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_19(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


