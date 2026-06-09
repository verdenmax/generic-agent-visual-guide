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
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_17(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_18(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


def lesson_19(t):
    return f'<p class="lead">{t("本课内容正在编写中。", "This lesson is being written.")}</p>'


