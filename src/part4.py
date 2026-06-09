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

import components as c


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

        + c.deepdive_heading(t)

        + c.accordion(t, 1, 'detect() 到底返回什么：四元组结构',
            'What detect() actually returns: the four-field shape',
            c.qa(t, '🧪 返回结构', 'Return shape',
                 c.codefile('memory/ui_detect.py', 'detect() → list[dict]',
                     '<span class="cm"># ' + t('每个元素是一个 dict', 'each element is a dict') + '</span>\n'
                     + '{\n'
                     + '  <span class="st">\'bbox\'</span>: [x1, y1, x2, y2],  <span class="cm"># '
                     + t('物理像素框', 'physical-pixel box') + '</span>\n'
                     + '  <span class="st">\'type\'</span>: <span class="st">\'icon\'</span> | <span class="st">\'text\'</span>,  <span class="cm"># '
                     + t('YOLO 框=icon，OCR 框=text', 'YOLO box = icon, OCR box = text') + '</span>\n'
                     + '  <span class="st">\'label\'</span>: <span class="nb">str</span> | <span class="nb">None</span>,  <span class="cm"># '
                     + t('图标上若无文字则为 None', 'None when an icon carries no text') + '</span>\n'
                     + '  <span class="st">\'confidence\'</span>: <span class="nb">float</span>\n'
                     + '}'))
            + c.qa(t, '⚙️ match 模式怎么走', 'How match mode works',
                   '<p>' + t(
                       '默认 <span class="inline">mode=\'match\'</span>：先跑一次 YOLO 得到图标框，再跑一次<strong>全图 OCR</strong>，'
                       '然后用 <span class="inline">_iou()</span>（交集占 OCR 框面积的比例）把文字“贴”到重叠的图标上当 label；'
                       '没被任何图标匹配上的 OCR 框，单独作为 <span class="mono">type=\'text\'</span> 元素输出。约 1.2s。',
                       'The default <span class="inline">mode=\'match\'</span> runs YOLO once for icon boxes, then a single '
                       '<strong>full-image OCR</strong>, and uses <span class="inline">_iou()</span> (intersection over the '
                       'OCR box\'s area) to "stick" text onto the overlapping icon as its label; any OCR box matched by no '
                       'icon is emitted on its own as a <span class="mono">type=\'text\'</span> element. ~1.2s.') + '</p>')
            + c.qa(t, '🔀 match vs crop', 'match vs crop',
                   '<p>' + t(
                       '<span class="inline">mode=\'crop\'</span> 改为把每个 YOLO 框 crop 出来<strong>垂直拼成一张长图</strong>'
                       '（<span class="inline">_ocr_crops_batch</span>）只 OCR 一次，再按 y 坐标映射回各框——更精确但约 2.3s。'
                       '日常用 match 即可，密集小图标识别不准时再换 crop。',
                       '<span class="inline">mode=\'crop\'</span> instead crops every YOLO box and <strong>stitches them '
                       'vertically into one tall image</strong> (<span class="inline">_ocr_crops_batch</span>), OCRs once, '
                       'and maps results back by y-coordinate — more precise but ~2.3s. Use match day-to-day; switch to crop '
                       'only when dense small icons are misread.') + '</p>'))

        + c.accordion(t, 2, 'OCR 的三个坑：ocr_utils.py',
            'Three OCR pitfalls: ocr_utils.py',
            c.qa(t, '⚠️ conf 与“无文字”', 'conf and "no text"',
                 '<p>' + t(
                     'RapidOCR 有两个反直觉点，写在 <span class="inline">ocr_utils.py</span> 文件头：'
                     '<strong>① 置信度是字符串</strong>（<span class="mono">result[i][2]</span> 是 str 不是 float，'
                     '所以 <span class="inline">_ocr_rapid</span> 里要 <span class="mono">float(r[2])</span> 转换）；'
                     '<strong>② 无文字时返回 None</strong> 而不是空列表，必须先 <span class="mono">if not result</span> 兜底。',
                     'RapidOCR has two counter-intuitive points, documented in the header of '
                     '<span class="inline">ocr_utils.py</span>: <strong>(1) confidence is a string</strong> '
                     '(<span class="mono">result[i][2]</span> is str, not float, so <span class="inline">_ocr_rapid</span> '
                     'must cast it via <span class="mono">float(r[2])</span>); <strong>(2) it returns None, not an empty '
                     'list, when there is no text</strong>, so you must guard with <span class="mono">if not '
                     'result</span> first.') + '</p>')
            + c.qa(t, '⚠️ 远程桌面黑屏', 'Remote-desktop black screen',
                   '<p>' + t(
                       '在 RDP 断开后，<span class="inline">ImageGrab</span> / mss 截到的是<strong>全黑图</strong>。'
                       '解法是 <span class="inline">ocr_window(hwnd)</span>：它用 Win32 的 '
                       '<span class="inline">PrintWindow</span> API 直接抓窗口位图，绕开屏幕缓冲，远程桌面下也能拿到画面。',
                       'After an RDP disconnect, <span class="inline">ImageGrab</span> / mss capture a <strong>fully black '
                       'image</strong>. The fix is <span class="inline">ocr_window(hwnd)</span>: it grabs the window bitmap '
                       'directly through Win32\'s <span class="inline">PrintWindow</span> API, bypassing the screen buffer '
                       'so it still works under remote desktop.') + '</p>')
            + c.qa(t, '🧪 三个入口', 'Three entry points',
                   '<p>' + t(
                       '<span class="inline">ocr_image(img)</span> 认一张图、'
                       '<span class="inline">ocr_screen(bbox)</span> 截屏区域再认、'
                       '<span class="inline">ocr_window(hwnd)</span> 抓窗口再认；三者都返回 '
                       '<span class="mono">{text, lines, details}</span>，details 里带 bbox 与 conf。',
                       '<span class="inline">ocr_image(img)</span> reads one image, '
                       '<span class="inline">ocr_screen(bbox)</span> grabs a screen region then reads, and '
                       '<span class="inline">ocr_window(hwnd)</span> grabs a window then reads; all three return '
                       '<span class="mono">{text, lines, details}</span>, with bbox and conf inside details.') + '</p>'))

        + c.accordion(t, 3, '无文字图标怎么办？物理坐标与 VLM 保底',
            'Iconless elements: physical coordinates and the VLM fallback',
            c.qa(t, '⚠️ label=None 的元素', 'Elements with label=None',
                 '<p>' + t(
                     '纯图标（如一个齿轮、一个箭头）没有文字，<span class="inline">detect()</span> 给它的 '
                     '<span class="mono">label=None</span>。这时无法靠文字定位，可把该 bbox crop 出来交给'
                     '<strong>视觉大模型</strong>识别语义——保底入口是 '
                     '<span class="inline">memory/vision_api.template.py: ask_vision(img, prompt)</span>，'
                     '支持 claude / openai / modelscope 三种后端。',
                     'A pure icon (a gear, an arrow) has no text, so <span class="inline">detect()</span> gives it '
                     '<span class="mono">label=None</span>. You then cannot locate it by text, so crop that bbox and hand '
                     'it to a <strong>vision LLM</strong> for its meaning — the fallback entry is '
                     '<span class="inline">memory/vision_api.template.py: ask_vision(img, prompt)</span>, which supports '
                     'claude / openai / modelscope backends.') + '</p>')
            + c.qa(t, '❓ 为什么必须物理坐标', 'Why physical coordinates are mandatory',
                   '<p>' + t(
                       '高 DPI 屏幕上“逻辑坐标”和“物理像素”不是一回事。截屏分析拿到的是<strong>物理像素</strong>框，'
                       '而点击下一课用的 <span class="inline">ljqCtrl</span> 也按物理坐标算（内部再乘 dpi_scale），'
                       '两端对齐才不会“看到的和点到的错位”。所以 <span class="inline">ui_detect.py</span> 一加载就打印'
                       '“截图分析后必须使用物理坐标”。',
                       'On high-DPI screens, "logical coordinates" and "physical pixels" are not the same. Screenshot '
                       'analysis yields <strong>physical-pixel</strong> boxes, and the next lesson\'s clicking via '
                       '<span class="inline">ljqCtrl</span> also reckons in physical coordinates (multiplying by dpi_scale '
                       'internally) — only when both ends agree does "what you see" line up with "what you click". That is '
                       'why <span class="inline">ui_detect.py</span> prints "after screenshot analysis you must use '
                       'physical coordinates" the moment it loads.') + '</p>')
            + c.qa(t, '⚙️ YOLO 跨进程缓存', 'YOLO cross-process cache',
                   '<p>' + t(
                       '加载 YOLO 权重很慢，所以 <span class="inline">_yolo()</span> 把推理外包给一个常驻 daemon：'
                       '先 ping <span class="mono">127.0.0.1:31876</span>，没起就 Popen 自己 '
                       '<span class="mono">--yolo-daemon</span> 拉起来，之后每次检测走 HTTP 复用已加载的模型；'
                       'daemon 不可用时回退 <span class="inline">_yolo_local</span> 本地推理。',
                       'Loading YOLO weights is slow, so <span class="inline">_yolo()</span> outsources inference to a '
                       'resident daemon: it pings <span class="mono">127.0.0.1:31876</span>, and if nothing answers it '
                       'Popens itself with <span class="mono">--yolo-daemon</span>, after which each detection reuses the '
                       'already-loaded model over HTTP; if the daemon is unavailable it falls back to local inference via '
                       '<span class="inline">_yolo_local</span>.') + '</p>'))

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
        + '<div class="col"><h3>' + t('桌面：鼠标键盘', 'Desktop: mouse & keyboard') + '</h3><p>'
        + t('ljqCtrl 用 Click(x,y)、SetCursorPos、Press("ctrl+v") 等操作，全程<strong>物理坐标</strong>，并提供 DPI 安全的窗口截图。',
            'ljqCtrl uses Click(x,y), SetCursorPos, Press("ctrl+v") and more, all in <strong>physical '
            'coordinates</strong>, plus DPI-safe window capture.') + '</p></div>'
        + '<div class="col"><h3>' + t('移动：ADB 安卓', 'Mobile: ADB Android') + '</h3><p>'
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

        + c.deepdive_heading(t)

        + c.accordion(t, 1, 'ljqCtrl 的核心 API 与 DPI 模型',
            'ljqCtrl\'s core API and DPI model',
            c.qa(t, '🧪 常用动作', 'Common actions',
                 c.codefile('memory/ljqCtrl.py', 'physical-coordinate input',
                     '<span class="cm"># ' + t('全部使用物理坐标', 'all in physical coordinates') + '</span>\n'
                     + 'Click(x, y, check=<span class="nb">True</span>)   <span class="cm"># '
                     + t('移动并左键单击，校验变化', 'move + left-click, verify change') + '</span>\n'
                     + 'SetCursorPos((x, y))         <span class="cm"># ' + t('只移动光标', 'move cursor only') + '</span>\n'
                     + 'Press(<span class="st">\'ctrl+v\'</span>)            <span class="cm"># '
                     + t('组合键', 'key combo') + '</span>\n'
                     + 'obj, ok = FindBlock(<span class="st">\'tpl.png\'</span>)  <span class="cm"># '
                     + t('模板匹配 → 中心物理坐标', 'template match → center phys coords') + '</span>\n'
                     + 'img = GrabWindow(hwnd)       <span class="cm"># ' + t('DPI 安全窗口截图', 'DPI-safe window shot') + '</span>'))
            + c.qa(t, '⚙️ dpi_scale 怎么换算', 'How dpi_scale converts',
                   '<p>' + t(
                       '加载时它用 GDI 的 <span class="mono">DESKTOPHORZRES</span>（物理分辨率）除以 '
                       '<span class="mono">SM_CXSCREEN</span>（逻辑分辨率）算出 <span class="inline">dpi_scale</span>，'
                       '满足 <span class="mono">Logical = Physical × dpi_scale</span>。你传物理坐标，'
                       '<span class="inline">SetCursorPos</span> 内部再乘 dpi_scale 转成系统要的逻辑坐标——所以调用方<strong>永远只想物理坐标</strong>。',
                       'On load it computes <span class="inline">dpi_scale</span> by dividing GDI\'s '
                       '<span class="mono">DESKTOPHORZRES</span> (physical resolution) by <span class="mono">SM_CXSCREEN</span> '
                       '(logical resolution), satisfying <span class="mono">Logical = Physical × dpi_scale</span>. You pass '
                       'physical coordinates and <span class="inline">SetCursorPos</span> multiplies by dpi_scale internally '
                       'to the logical coordinates the OS wants — so callers <strong>only ever think in physical '
                       'coordinates</strong>.') + '</p>')
            + c.qa(t, '⚠️ 严禁 import pyautogui', 'Never import pyautogui',
                   '<p>' + t(
                       '文件头第一行就是大写警告：<strong>禁止在此工具链 import pyautogui</strong>。pyautogui 会改动 win32 的 '
                       'DPI 感知 / 坐标语义，和 ljqCtrl 的物理坐标体系冲突，导致点击全部错位。这是一条硬规矩，不是建议。',
                       'The very first line of the file is an upper-case warning: <strong>do not import pyautogui in this '
                       'toolchain</strong>. pyautogui alters win32\'s DPI awareness / coordinate semantics, clashing with '
                       'ljqCtrl\'s physical-coordinate system and throwing every click off. It is a hard rule, not a '
                       'suggestion.') + '</p>'))

        + c.accordion(t, 2, 'Click(check=True)：点完自动验证',
            'Click(check=True): self-verify after the click',
            c.qa(t, '⚙️ 内部怎么走', 'How it works inside',
                 '<p>' + t(
                     '<span class="inline">Click</span> 默认 <span class="mono">check=True</span>：点击前用 '
                     '<span class="inline">ScreenCapAt(x,y)</span> 抓点击点周边一小块、并记下当前前台窗口；点击后等 0.5s 再抓一次，'
                     '比较两张图<strong>有多少像素变了</strong>，同时检测<strong>前台窗口是否切换</strong>，并打印 '
                     '<span class="mono">[Click check] N/total px changed | fg: ...</span>。',
                     '<span class="inline">Click</span> defaults to <span class="mono">check=True</span>: before clicking it '
                     'grabs a small patch around the point with <span class="inline">ScreenCapAt(x,y)</span> and records the '
                     'current foreground window; after clicking it waits 0.5s, grabs again, compares <strong>how many pixels '
                     'changed</strong>, also checks <strong>whether the foreground window switched</strong>, and prints '
                     '<span class="mono">[Click check] N/total px changed | fg: ...</span>.') + '</p>')
            + c.qa(t, '❓ 为什么要验证', 'Why verify at all',
                   '<p>' + t(
                       '盲点击是自动化最大的不可靠来源——点空了、点偏了、窗口没响应，脚本却以为成功了。把“点击是否真的产生了变化”'
                       '做进 <span class="inline">Click</span> 的返回值，Agent 就能<strong>立刻看出点击有没有生效</strong>，'
                       '失败时换坐标重试，而不是一路错下去。',
                       'Blind clicking is the biggest source of automation flakiness — a miss, an off-by-a-bit, an '
                       'unresponsive window, yet the script assumes success. By baking "did the click actually change '
                       'anything" into <span class="inline">Click</span>\'s return value, the agent can <strong>tell '
                       'immediately whether the click landed</strong> and retry with new coordinates on failure instead of '
                       'compounding the error.') + '</p>'))

        + c.accordion(t, 3, '安卓控制：adb_ui 的 dump 与补盲',
            'Android control: adb_ui\'s dump and gap-filling',
            c.qa(t, '⚙️ u2 优先、native 兜底', 'u2 first, native fallback',
                 '<p>' + t(
                     '<span class="inline">ui()</span> 先试 <span class="inline">_dump_u2()</span>（uiautomator2，'
                     '<strong>不受 idle 限制</strong>，适合美团这种动画密集 App），失败再 '
                     '<span class="inline">_dump_native()</span>（原生 <span class="mono">uiautomator dump</span>，需界面静止）；'
                     '拿到 XML 后 <span class="inline">_parse_xml</span> 解析出每个节点的 text / clickable / '
                     '中心坐标 <span class="mono">(cx,cy)</span>。',
                     '<span class="inline">ui()</span> first tries <span class="inline">_dump_u2()</span> (uiautomator2, '
                     '<strong>not bound by idle state</strong>, good for animation-heavy apps like Meituan), then falls '
                     'back to <span class="inline">_dump_native()</span> (native <span class="mono">uiautomator dump</span>, '
                     'which needs a still UI); from the XML, <span class="inline">_parse_xml</span> extracts each node\'s '
                     'text / clickable / center <span class="mono">(cx,cy)</span>.') + '</p>')
            + c.qa(t, '🧪 点击与节点', 'Tapping and nodes',
                   '<p>' + t(
                       '定位到节点后用 <span class="inline">tap(x,y)</span>（底层 <span class="mono">adb shell input tap</span>）点过去。'
                       '弹窗检测的小技巧也写在文件头：<span class="mono">ui(clickable_only=True, raw=True)</span> 找全屏 '
                       'FrameLayout + 底部小 ImageView（关闭 X）。',
                       'Once a node is located, tap it with <span class="inline">tap(x,y)</span> (backed by '
                       '<span class="mono">adb shell input tap</span>). A popup-detection trick is noted in the file header '
                       'too: <span class="mono">ui(clickable_only=True, raw=True)</span> finds a full-screen FrameLayout plus '
                       'a small bottom ImageView (the close X).') + '</p>')
            + c.qa(t, '⚠️ 已知包名与中文输入', 'Known packages and Chinese input',
                   '<p>' + t(
                       '文件头预存了已知包名（美团外卖 <span class="mono">com.sankuai.meituan.takeoutnew</span>、'
                       '淘宝 <span class="mono">com.taobao.taobao</span>）省去查找。一个坑：<strong>别硬啃 adb 中文输入</strong>，'
                       '搜索框一般直接打拼音/首字母即可；遇到小程序等 dump 不全的界面，再叠加上一课的 '
                       '<span class="inline">ui_detect</span> 视觉补盲。',
                       'The header pre-stores known package names (Meituan delivery '
                       '<span class="mono">com.sankuai.meituan.takeoutnew</span>, Taobao '
                       '<span class="mono">com.taobao.taobao</span>) to skip lookups. One pitfall: <strong>do not fight adb '
                       'Chinese input</strong> — a search box usually accepts pinyin/initials directly; for mini-programs '
                       'and other under-dumped UIs, layer on the previous lesson\'s <span class="inline">ui_detect</span> '
                       'vision to fill the gaps.') + '</p>'))

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

        + c.codefile('ga.py', 'web_execute_js',
            '<span class="kw">def</span> <span class="fn">web_execute_js</span>(script, switch_tab_id=<span class="nb">None</span>, no_monitor=<span class="nb">False</span>):\n'
            '    <span class="kw">global</span> driver\n'
            '    <span class="kw">if</span> driver <span class="kw">is</span> <span class="nb">None</span>: <span class="fn">first_init_driver</span>()            <span class="cm"># ' + t('懒连接你的真实浏览器', 'lazily attach to your real browser') + '</span>\n'
            '    <span class="kw">if</span> switch_tab_id: driver.default_session_id = switch_tab_id\n'
            '    <span class="kw">return</span> simphtml.<span class="fn">execute_js_rich</span>(script, driver, no_monitor=no_monitor)')

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

        + c.deepdive_heading(t)

        + c.accordion(t, 1, 'TMWebDriver：浏览器“连回来”的 WS 桥',
            'TMWebDriver: the WS bridge the browser "connects back" to',
            c.qa(t, '⚙️ 内部怎么走', 'How it works inside',
                 '<p>' + t(
                     '<span class="inline">TMWebDriver()</span> 在本机起一个 WebSocket 服务（默认 '
                     '<span class="mono">127.0.0.1:18765</span>）外加一个 HTTP 长轮询服务。你浏览器里的<strong>用户脚本/扩展</strong>'
                     '作为客户端主动连回来注册成一个 <span class="inline">Session</span>（每个标签页一个），'
                     '之后 <span class="inline">execute_js(code)</span> 把脚本下发到对应标签页执行并回收结果。',
                     '<span class="inline">TMWebDriver()</span> starts a local WebSocket server (default '
                     '<span class="mono">127.0.0.1:18765</span>) plus an HTTP long-poll server. A <strong>userscript/'
                     'extension</strong> inside your browser is the client that connects back and registers as a '
                     '<span class="inline">Session</span> (one per tab); thereafter '
                     '<span class="inline">execute_js(code)</span> ships the script to that tab, runs it, and collects the '
                     'result.') + '</p>')
            + c.qa(t, '❓ 为什么是“浏览器连回来”', 'Why "the browser connects back"',
                   '<p>' + t(
                       '反过来——由代码<strong>启动</strong>一个无头浏览器——就丢了你的登录态、Cookie 和插件。让你<strong>已经登录</strong>'
                       '的真实浏览器主动连上桥，代码就在那个上下文里执行 JS，于是“它看到的页面 = 你看到的页面”，免登录、免验证码。',
                       'The opposite — having code <strong>launch</strong> a headless browser — loses your login state, '
                       'cookies and extensions. By letting your <strong>already-logged-in</strong> real browser connect to '
                       'the bridge, the code runs JS in that very context, so "the page it sees = the page you see" — no '
                       're-login, no captchas.') + '</p>')
            + c.qa(t, '🔀 多协议与远程', 'Multi-protocol and remote',
                   '<p>' + t(
                       '<span class="inline">Session</span> 支持 ws / ext_ws / http 三类客户端，http 走 5 秒长轮询兜底；'
                       '构造时还会探测 <span class="mono">port+1</span> 判断是否 <span class="inline">is_remote</span>，'
                       '是则把命令转发到远端的 <span class="mono">/link</span>，从而支持“控制另一台机器的浏览器”。',
                       'A <span class="inline">Session</span> supports ws / ext_ws / http clients, with http falling back to '
                       'a 5-second long poll; the constructor also probes <span class="mono">port+1</span> to decide '
                       '<span class="inline">is_remote</span>, and if so forwards commands to a remote '
                       '<span class="mono">/link</span> — enabling "drive a browser on another machine".') + '</p>'))

        + c.accordion(t, 2, 'simphtml.get_html：把页面压到能喂进模型',
            'simphtml.get_html: shrinking a page until it fits the model',
            c.qa(t, '🧪 签名与参数', 'Signature and parameters',
                 c.codefile('simphtml.py', 'get_html()',
                     '<span class="kw">def</span> <span class="fn">get_html</span>(driver, cutlist=<span class="nb">False</span>,\n'
                     + '             maxchars=<span class="nb">35000</span>, instruction=<span class="st">\'\'</span>,\n'
                     + '             extra_js=<span class="st">\'\'</span>, text_only=<span class="nb">False</span>):\n'
                     + '    <span class="cm"># ' + t('① 抓主体块 → ② token 优化 → ③ 砍长列表 → ④ 超额截断', 'main block → token-optimize → cut lists → truncate') + '</span>'))
            + c.qa(t, '⚙️ cutlist 砍掉重复列表', 'cutlist trims repeated lists',
                   '<p>' + t(
                       '<span class="mono">cutlist=True</span> 时，先用 <span class="inline">findMainList</span> 找出页面里的'
                       '重复列表（如 50 条商品），对每个长列表<strong>只保留前 3 条</strong>（或命中 instruction 的 6 条），'
                       '其余 <span class="mono">decompose()</span> 删掉并插一条 <span class="mono">[FAKE ELEMENT] N more items hidden</span> 提示。'
                       '50 条变 3 条，token 立省一大截。',
                       'With <span class="mono">cutlist=True</span>, it first finds repeated lists on the page via '
                       '<span class="inline">findMainList</span> (e.g. 50 product rows) and for each long list <strong>keeps '
                       'only the first 3</strong> (or 6 that match instruction), <span class="mono">decompose()</span>s the '
                       'rest and inserts a <span class="mono">[FAKE ELEMENT] N more items hidden</span> hint. 50 rows become '
                       '3 — a big token saving.') + '</p>')
            + c.qa(t, '⚠️ 还会丢掉什么', 'What else gets dropped',
                   '<p>' + t(
                       '在 <span class="inline">optimize_html_for_tokens</span> 阶段，隐藏 / 浮动 / 被遮挡的元素会被剔除——'
                       '它们对模型理解“主体内容”没用却很占字。最后若仍超 <span class="mono">maxchars</span>，'
                       '用 <span class="inline">smart_truncate</span> 按预算就地裁剪。所以 web_scan 看到的是<strong>主体的精简版</strong>，'
                       '边栏/广告/隐藏层往往不在里面。',
                       'During <span class="inline">optimize_html_for_tokens</span>, hidden / floating / covered elements '
                       'are stripped — useless for understanding the "main content" yet costly in characters. If it still '
                       'exceeds <span class="mono">maxchars</span>, <span class="inline">smart_truncate</span> trims in place '
                       'to budget. So web_scan shows a <strong>condensed version of the main body</strong>; sidebars/ads/'
                       'hidden layers are often absent.') + '</p>'))

        + c.accordion(t, 3, 'execute_js_rich 与 ga.py 接线',
            'execute_js_rich and the ga.py wiring',
            c.qa(t, '🧪 富返回值', 'A rich return value',
                 '<p>' + t(
                     '<span class="inline">execute_js_rich(script, driver)</span> 不只回 JS 的返回值，还顺带告诉模型“页面发生了什么”：'
                     '<span class="mono">js_return</span>（脚本结果）、<span class="mono">newTabs</span>（执行期间新开的标签页）、'
                     '<span class="mono">transients</span>（一闪而过的提示）、<span class="mono">diff</span>（DOM 变化量与最显著变化）。',
                     '<span class="inline">execute_js_rich(script, driver)</span> returns not just the JS result but also '
                     'tells the model "what happened to the page": <span class="mono">js_return</span> (the script result), '
                     '<span class="mono">newTabs</span> (tabs opened during execution), <span class="mono">transients</span> '
                     '(flash-by toasts), and <span class="mono">diff</span> (how much the DOM changed and the most '
                     'significant change).') + '</p>')
            + c.qa(t, '⚙️ 变化监控怎么做', 'How change monitoring works',
                   '<p>' + t(
                       '执行前先抓一份 baseline HTML（注入 <span class="inline">temp_monitor_js</span>），执行后再抓一份，'
                       '用 <span class="inline">find_changed_elements</span> 对比得出 DOM 变化量；'
                       '若 0 变化且无瞬时提示无新标签，就回 “页面无明显变化”，提醒模型这步可能没生效。',
                       'It grabs a baseline HTML first (injecting <span class="inline">temp_monitor_js</span>), grabs '
                       'another after execution, and diffs them via <span class="inline">find_changed_elements</span> to '
                       'report a DOM change count; if there were zero changes, no transient toasts and no new tabs, it '
                       'returns "no visible change", warning the model this step may not have taken effect.') + '</p>')
            + c.qa(t, '🔀 两个工具如何接线', 'How the two tools are wired',
                   '<p>' + t(
                       '在 <span class="inline">ga.py</span> 里，<span class="inline">web_scan</span> → '
                       '<span class="mono">simphtml.get_html(driver, cutlist=True, maxchars=35000)</span>，'
                       '<span class="inline">web_execute_js</span> → <span class="mono">simphtml.execute_js_rich(script, driver)</span>，'
                       '外面再包成工具方法 <span class="inline">do_web_scan / do_web_execute_js</span>。'
                       '官方建议<strong>多用 execute_js，少全量 scan</strong>——scan 贵，定点 JS 既准又省。',
                       'In <span class="inline">ga.py</span>, <span class="inline">web_scan</span> → '
                       '<span class="mono">simphtml.get_html(driver, cutlist=True, maxchars=35000)</span>, and '
                       '<span class="inline">web_execute_js</span> → '
                       '<span class="mono">simphtml.execute_js_rich(script, driver)</span>, wrapped as the tool methods '
                       '<span class="inline">do_web_scan / do_web_execute_js</span>. The guidance is to <strong>prefer '
                       'execute_js and scan sparingly</strong> — scan is expensive, targeted JS is both precise and '
                       'cheap.') + '</p>'
                   + c.codefile('simphtml.py / TMWebDriver.py', 'execute_js_rich → driver.execute_js',
                       '<span class="cm"># simphtml.py</span>\n'
                       '<span class="kw">def</span> <span class="fn">execute_js_rich</span>(script, driver, no_monitor=<span class="nb">False</span>):\n'
                       '    response = driver.<span class="fn">execute_js</span>(script)              <span class="cm"># ' + t('下发到真实浏览器标签页', 'ship to the real browser tab') + '</span>\n'
                       '    result = response.get(<span class="st">\'data\'</span>) <span class="kw">or</span> response.get(<span class="st">\'result\'</span>)\n'
                       '    ...                                            <span class="cm"># ' + t('再附 newTabs / transients / diff', 'plus newTabs / transients / diff') + '</span>\n'
                       '\n'
                       '<span class="cm"># TMWebDriver.py</span>\n'
                       '<span class="kw">def</span> <span class="fn">execute_js</span>(self, code, timeout=<span class="nb">15</span>, session_id=<span class="nb">None</span>):\n'
                       '    <span class="kw">if</span> session_id <span class="kw">is</span> <span class="nb">None</span>: session_id = self.default_session_id\n'
                       '    ...                                            <span class="cm"># ' + t('通过 WS/HTTP 把 code 送进对应 tab 执行', 'send code into that tab over WS/HTTP') + '</span>')))

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

        + c.deepdive_heading(t)

        + c.accordion(t, 1, 'reflect 模块的三件套约定',
            'The three-part convention of a reflect module',
            c.qa(t, '🧪 最小骨架', 'The minimal skeleton',
                 c.codefile('reflect/autonomous.py', 'INTERVAL / (init) / check',
                     'INTERVAL = <span class="nb">1800</span>      <span class="cm"># '
                     + t('两次 check 间隔（秒）', 'seconds between checks') + '</span>\n'
                     + 'ONCE = <span class="nb">False</span>\n\n'
                     + '<span class="kw">def</span> <span class="fn">check</span>():\n'
                     + '    <span class="cm"># ' + t('返回字符串=唤醒提示；返回 None=本轮跳过', 'return str = wake prompt; return None = skip') + '</span>\n'
                     + '    <span class="kw">return</span> <span class="st">\'[AUTO]...\'</span>'))
            + c.qa(t, '⚙️ agentmain 怎么驱动', 'How agentmain drives it',
                   '<p>' + t(
                       '用 <span class="inline">agentmain.py --reflect reflect/&lt;module&gt;.py</span> 启动后，主程序动态 import 该模块，'
                       '有 <span class="inline">init(a)</span> 就先调（把 <span class="mono">--key value</span> 风格的额外参数传进去），'
                       '然后进一个循环：每隔 <span class="inline">INTERVAL</span> 秒调一次 <span class="inline">check()</span>，'
                       '返回非空就 <span class="inline">put_task(task, source=\'reflect\')</span> 注入 Agent。',
                       'Launched via <span class="inline">agentmain.py --reflect reflect/&lt;module&gt;.py</span>, the main '
                       'program dynamically imports the module, calls <span class="inline">init(a)</span> first if present '
                       '(passing in extra <span class="mono">--key value</span>-style args), then loops: every '
                       '<span class="inline">INTERVAL</span> seconds it calls <span class="inline">check()</span>, and on a '
                       'non-empty return it injects the agent via '
                       '<span class="inline">put_task(task, source=\'reflect\')</span>.') + '</p>')
            + c.qa(t, '⚙️ 热重载', 'Hot reload',
                   '<p>' + t(
                       'agentmain 记下脚本的 mtime，每轮检查文件是否被改动；改了就 <span class="mono">exec_module</span> 重新加载并再调 init。'
                       '于是你可以<strong>边跑边改</strong>反思逻辑，不必重启 Agent。',
                       'agentmain records the script\'s mtime and checks each round whether the file changed; if so it '
                       '<span class="mono">exec_module</span>s to reload and calls init again. So you can <strong>edit the '
                       'reflection logic while it runs</strong> without restarting the agent.') + '</p>'))

        + c.accordion(t, 2, 'goal_mode：按预算自驱到底',
            'goal_mode: self-drive to the budget\'s end',
            c.qa(t, '⚙️ state 与预算', 'State and budget',
                 '<p>' + t(
                     '<span class="inline">goal_mode.py</span> 的 <span class="inline">INTERVAL=3</span>（跑完立刻再检查）。'
                     '它读 <span class="inline">GOAL_STATE</span> 指向的 json，里面有 <span class="mono">objective</span>、'
                     '<span class="mono">start_time</span>、<span class="mono">budget_seconds</span>、'
                     '<span class="mono">turns_used / max_turns</span>。每轮算出已用/剩余时间，回一段续推提示并把 turn +1。',
                     '<span class="inline">goal_mode.py</span> uses <span class="inline">INTERVAL=3</span> (re-check the '
                     'moment a run finishes). It reads the json pointed to by <span class="inline">GOAL_STATE</span>, '
                     'holding <span class="mono">objective</span>, <span class="mono">start_time</span>, '
                     '<span class="mono">budget_seconds</span> and <span class="mono">turns_used / max_turns</span>. Each '
                     'round it computes elapsed/remaining time, returns a continuation prompt and increments the turn.') + '</p>')
            + c.qa(t, '🧪 两种提示', 'Two prompts',
                   '<p>' + t(
                       '预算未尽返回 <span class="inline">CONTINUATION_PROMPT</span>（“禁止说已完成是否继续，没到预算不准停”）；'
                       '<span class="mono">remaining&lt;=0</span> 或 <span class="mono">turn&gt;max_turns</span> 时返回 '
                       '<span class="inline">BUDGET_LIMIT_PROMPT</span> 做最后一轮收口，再返回 <span class="mono">/exit</span> 结束。',
                       'While budget remains it returns <span class="inline">CONTINUATION_PROMPT</span> ("do not say done/'
                       'continue, do not stop before the budget"); when <span class="mono">remaining&lt;=0</span> or '
                       '<span class="mono">turn&gt;max_turns</span> it returns <span class="inline">BUDGET_LIMIT_PROMPT</span> '
                       'for a final wrap-up round, then returns <span class="mono">/exit</span> to finish.') + '</p>')
            + c.qa(t, '❓ 为什么禁止“提前交付”', 'Why forbid "early delivery"',
                   '<p>' + t(
                       '模型天然倾向于尽快说“做完了”。Goal Mode 反过来逼它<strong>把时间预算花满</strong>：每轮换一个角度'
                       '（测试/边界/性能/安全/美观）持续打磨同一个核心成果，从而把“能用”磨成“好用”。',
                       'Models naturally tend to declare "done" as soon as possible. Goal Mode instead forces them to '
                       '<strong>spend the whole time budget</strong>: each round take a different angle (tests/edge cases/'
                       'performance/security/polish) to keep refining the same core deliverable, turning "works" into '
                       '"works well".') + '</p>'))

        + c.accordion(t, 3, 'scheduler 的端口锁与多模块对比',
            'scheduler\'s port lock and a module comparison',
            c.qa(t, '⚙️ 端口锁防重复启动', 'Port lock prevents double-start',
                 '<p>' + t(
                     '<span class="inline">scheduler.py</span> 在模块顶层 <span class="mono">bind(\'127.0.0.1\', 45762)</span>：'
                     '若已有一个调度器在跑，第二次 bind 会失败让 agentmain 直接崩退，<strong>保证全机只有一个调度器</strong>。'
                     '用 <span class="mono">try: _lock except NameError</span> 守护，热重载时跳过重复绑定。',
                     '<span class="inline">scheduler.py</span> does a module-top <span class="mono">bind(\'127.0.0.1\', '
                     '45762)</span>: if a scheduler is already running, the second bind fails and crashes agentmain out, '
                     '<strong>guaranteeing exactly one scheduler per machine</strong>. A <span class="mono">try: _lock '
                     'except NameError</span> guard skips re-binding on hot reload.') + '</p>')
            + c.qa(t, '🧪 repeat 冷却', 'repeat cooldowns',
                   '<p>' + t(
                       '它扫 <span class="mono">sche_tasks/</span> 下的任务，按 <span class="inline">_parse_cooldown(repeat)</span> '
                       '把 daily/weekly/monthly/<span class="mono">every_2h</span> 等折算成冷却时间（略短于周期防漂移），'
                       '到点未做且在 <span class="mono">DEFAULT_MAX_DELAY</span> 窗口内才触发，做完归档到 '
                       '<span class="mono">sche_tasks/done</span>。',
                       'It scans tasks under <span class="mono">sche_tasks/</span> and uses '
                       '<span class="inline">_parse_cooldown(repeat)</span> to convert daily/weekly/monthly/'
                       '<span class="mono">every_2h</span> into cooldowns (slightly shorter than the period to avoid '
                       'drift); it fires only when due, undone, and within the <span class="mono">DEFAULT_MAX_DELAY</span> '
                       'window, archiving finished runs to <span class="mono">sche_tasks/done</span>.') + '</p>')
            + c.qa(t, '🔀 看板 vs 接单', 'Board vs job-board',
                   '<p>' + t(
                       '<span class="inline">checklist_master.py</span> 轮询一份 <span class="mono">state.json</span>（可挂一个 BBS 做 mapreduce），'
                       '逐项派活；<span class="inline">agent_team_worker.py</span> 则是 worker 端，'
                       '<span class="inline">check()</span> 内预检 BBS（<span class="mono">/posts?limit=10</span>），无新帖返回 None 不唤醒，'
                       '有新帖才回一段“接单—执行—汇报”的提示。BBS 服务本体见 <span class="inline">assets/agent_bbs.py</span>。',
                       '<span class="inline">checklist_master.py</span> polls a <span class="mono">state.json</span> (which '
                       'may attach a BBS for mapreduce) and assigns items; <span class="inline">agent_team_worker.py</span> '
                       'is the worker side, whose <span class="inline">check()</span> pre-checks the BBS '
                       '(<span class="mono">/posts?limit=10</span>), returns None to skip when there is nothing new, and '
                       'only on a new post returns a "claim — execute — report" prompt. The BBS service itself is '
                       '<span class="inline">assets/agent_bbs.py</span>.') + '</p>'))

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
    """长期自治与定时任务 / Long-Horizon Autonomy."""
    return (
        '<p class="lead">'
        + t(
            '把上一课的“反思探针”用到极致，就得到一个能<strong>无人值守、长期运行</strong>的 Agent：你离开后它自己找事做，'
            '到点了它自己执行，盯着一个目标它能跑上几小时甚至几天。这一课讲 GA 的长期自治。',
            'Push the previous lesson\'s "reflection probes" to the extreme and you get an agent that runs '
            '<strong>unattended, for the long haul</strong>: it finds work after you leave, executes on schedule, and '
            'can chase a goal for hours or even days. This lesson covers GA\'s long-horizon autonomy.',
        )
        + '</p>'

        + '<div class="card macro"><div class="tag">🌍 '
        + t('宏观理解', 'The Big Picture') + '</div>'
        + '<p>'
        + t(
            '长期自治 = <strong>触发 + 自驱 + 留痕</strong>。触发可以是“用户离开很久了”或“到点了”；自驱让它读自动化 SOP 持续做事；'
            '留痕则靠分层记忆把每段经历沉淀下来，供以后回溯。这三件事都搭在上一课那套 reflect 探针上。',
            'Long-horizon autonomy = <strong>trigger + self-drive + trace</strong>. The trigger can be "the user has '
            'been away a while" or "it is time"; self-drive has it read an automation SOP and keep working; tracing '
            'relies on layered memory to settle each episode for later recall. All three sit on the previous lesson\'s '
            'reflect probes.',
        )
        + '</p></div>'

        + '<h2>' + t('自治是怎么触发的', 'How autonomy gets triggered') + '</h2>'
        + '<div class="vflow">'
        + '<div class="step"><div class="num">1</div><div class="sc"><h3>'
        + t('探针周期检查', 'Probe checks periodically') + '</h3><p>'
        + t('如 autonomous.py 每隔 30 分钟检查一次。', 'e.g. autonomous.py checks every 30 minutes.') + '</p></div></div>'
        + '<div class="step"><div class="num">2</div><div class="sc"><h3>'
        + t('满足条件 → 唤醒', 'Condition met → wake') + '</h3><p>'
        + t('检测到“用户离开超过 30 分钟”，返回一句自治提示唤醒 Agent。',
            'On detecting "user away for over 30 minutes", it returns an autonomy prompt to wake the agent.') + '</p></div></div>'
        + '<div class="step"><div class="num">3</div><div class="sc"><h3>'
        + t('读 SOP 自驱', 'Read SOP, self-drive') + '</h3><p>'
        + t('Agent 按 autonomous_operation_sop 持续执行自动任务。',
            'The agent keeps running automated tasks per autonomous_operation_sop.') + '</p></div></div>'
        + '<div class="step"><div class="num">4</div><div class="sc"><h3>'
        + t('留痕 / 结算', 'Trace / settle') + '</h3><p>'
        + t('过程写入工作便签，重要经验结晶进长期记忆，会话归入 L4。',
            'Progress goes to the working notepad, key lessons crystallize into long-term memory, sessions archive to L4.') + '</p></div></div>'
        + '</div>'

        + '<div class="card detail"><div class="tag">🔬 '
        + t('源码对应', 'In the Source') + '</div>'
        + '<ul>'
        + '<li>' + t('最简单的自治探针：', 'The simplest autonomy probe: ')
        + '<span class="inline">reflect/autonomous.py</span>'
        + t('（INTERVAL=1800 即 30 分钟，check() 返回 “用户离开超过 30 分钟，请执行自动任务”）。',
            ' (INTERVAL=1800, i.e. 30 minutes; check() returns "the user has been away for over 30 minutes, run '
            'autonomous tasks").') + '</li>'
        + '<li>' + t('定时任务由 ', 'Scheduled tasks are driven by ')
        + '<span class="inline">reflect/scheduler.py</span>'
        + t(' 驱动；玩法记在 ', '; the playbook is in ')
        + '<span class="inline">memory/scheduled_task_sop.md</span>' + t('。', '.') + '</li>'
        + '<li>' + t('自治与监督的规范见 ', 'Autonomy and supervision rules are in ')
        + '<span class="inline">memory/autonomous_operation_sop.md</span>' + t(' 与 ', ' and ')
        + '<span class="inline">memory/supervisor_sop.md</span>'
        + t('；可用 /autorun 进入自主模式（见“斜杠命令”一课）。',
            '; enter autonomous mode with /autorun (see the "slash commands" lesson).') + '</li>'
        + '</ul></div>'

        + c.deepdive_heading(t)

        + c.accordion(t, 1, 'autonomous.py 全文：最小自治探针',
            'autonomous.py in full: the minimal autonomy probe',
            c.qa(t, '🧪 真实源码', 'The real source',
                 c.codefile('reflect/autonomous.py', t('全文（仅 6 行）', 'whole file (just 6 lines)'),
                     '<span class="cm"># reflect/autonomous.py</span>\n'
                     + 'INTERVAL = <span class="nb">1800</span>\n'
                     + 'ONCE = <span class="nb">False</span>\n\n'
                     + '<span class="kw">def</span> <span class="fn">check</span>():\n'
                     + '    <span class="kw">return</span> <span class="st">"[AUTO]🤖 '
                     + t('用户已经离开超过30分钟，作为自主智能体，请阅读自动化sop，执行自动任务。',
                         'User away &gt;30 min — as an autonomous agent, read the automation SOP and run autonomous tasks.')
                     + '"</span>'))
            + c.qa(t, '⚙️ 它“无条件”唤醒？', 'Does it wake unconditionally?',
                   '<p>' + t(
                       '注意：这个 <span class="inline">check()</span> 每次都返回那句提示，本身不判断“用户是否真的离开”。'
                       '真正的“离开 30 分钟”是靠 <span class="inline">INTERVAL=1800</span> 这个节拍体现的——每 30 分钟唤醒一次；'
                       '而“是否该自治”交给 Agent 读 SOP 后自行判断。这正是 GA 的风格：<strong>探针只管节拍，判断交给模型</strong>。',
                       'Note: this <span class="inline">check()</span> returns that prompt every time; it does not itself '
                       'test "is the user really away". The actual "away for 30 minutes" is expressed by the '
                       '<span class="inline">INTERVAL=1800</span> cadence — it wakes once every 30 minutes — while "should '
                       'I act autonomously" is left to the agent after it reads the SOP. Very GA in style: <strong>the probe '
                       'owns the cadence, judgment is left to the model</strong>.') + '</p>')
            + c.qa(t, '🔀 和 scheduler 的分工', 'Division of labor with scheduler',
                   '<p>' + t(
                       '<span class="inline">autonomous.py</span> 管“闲时找事做”（粗节拍、无具体任务）；'
                       '<span class="inline">scheduler.py</span> 管“到点做特定事”（细任务、带 repeat 冷却与归档）。'
                       '两者都是 reflect 探针，一个负责<strong>填满空闲</strong>，一个负责<strong>守住日程</strong>。',
                       '<span class="inline">autonomous.py</span> handles "find work when idle" (coarse cadence, no specific '
                       'task); <span class="inline">scheduler.py</span> handles "do a specific thing on time" (concrete '
                       'tasks, with repeat cooldowns and archiving). Both are reflect probes — one <strong>fills idle '
                       'time</strong>, the other <strong>keeps the schedule</strong>.') + '</p>'))

        + c.accordion(t, 2, '触发 → 自驱 → 留痕的闭环',
            'The trigger → self-drive → trace loop',
            c.qa(t, '⚙️ 一圈怎么转', 'How one cycle turns',
                 '<p>' + t(
                     '① 探针按 <span class="inline">INTERVAL</span> 周期 <span class="inline">check()</span>；'
                     '② 返回提示 → <span class="inline">put_task(source=\'reflect\')</span> 唤醒 Agent；'
                     '③ Agent 读 <span class="inline">autonomous_operation_sop.md</span> 自驱执行；'
                     '④ 过程写工作便签、重要经验结晶进长期记忆、会话归入 L4。下一个 INTERVAL 再转一圈。',
                     '(1) the probe runs <span class="inline">check()</span> on its <span class="inline">INTERVAL</span>; '
                     '(2) a returned prompt wakes the agent via '
                     '<span class="inline">put_task(source=\'reflect\')</span>; (3) the agent reads '
                     '<span class="inline">autonomous_operation_sop.md</span> and self-drives; (4) progress goes to the '
                     'working notepad, key lessons crystallize into long-term memory, the session archives to L4. The next '
                     'INTERVAL turns the loop again.') + '</p>')
            + c.qa(t, '❓ 为什么没有新内核', 'Why there is no new core',
                   '<p>' + t(
                       '“长期自治”听起来很高级，但它没有引入任何新机制——只是把<strong>反思探针（何时动）+ SOP（做什么）+ 分层记忆'
                       '（别忘别重复）</strong>三块旧积木拼起来。这也解释了为什么 3K 行种子能长出复杂行为：靠<strong>组合</strong>，不靠堆叠。',
                       '"Long-horizon autonomy" sounds advanced, yet it introduces no new mechanism — it just snaps together '
                       'three old blocks: <strong>reflection probes (when to act) + SOPs (what to do) + layered memory (do '
                       'not forget or repeat)</strong>. That is why a 3K-line seed can grow complex behavior: by '
                       '<strong>composition</strong>, not accretion.') + '</p>'))

        + c.accordion(t, 3, '三份 SOP 与 /autorun 入口',
            'The three SOPs and the /autorun entry',
            c.qa(t, '🧪 各管什么', 'What each governs',
                 '<table class="t"><tr><th>' + t('文件', 'File') + '</th><th>' + t('职责', 'Role') + '</th></tr>'
                 + '<tr><td class="mono">autonomous_operation_sop.md</td><td>'
                 + t('自治时“做什么、怎么判断该不该做”的总规范。',
                     'the master rules for "what to do and how to judge whether to act" during autonomy.') + '</td></tr>'
                 + '<tr><td class="mono">scheduled_task_sop.md</td><td>'
                 + t('定时任务的写法与 repeat 玩法（配合 scheduler.py）。',
                     'how to author scheduled tasks and repeat styles (paired with scheduler.py).') + '</td></tr>'
                 + '<tr><td class="mono">supervisor_sop.md</td><td>'
                 + t('监督规范：自治跑偏/越界时如何自我约束。',
                     'supervision rules: how to self-restrain when autonomy drifts or oversteps.') + '</td></tr></table>')
            + c.qa(t, '🔀 /autorun vs --reflect', '/autorun vs --reflect',
                   '<p>' + t(
                       '<span class="inline">--reflect reflect/autonomous.py</span> 是<strong>外部进程</strong>挂探针的长跑方式；'
                       '<span class="inline">/autorun</span> 则是会话内一条斜杠命令，让当前 Agent <strong>就地进入自主模式</strong>'
                       '（详见“斜杠命令”一课）。前者适合无人值守的长期部署，后者适合你在对话里临时放手。',
                       '<span class="inline">--reflect reflect/autonomous.py</span> is the long-running way to attach a probe '
                       'as an <strong>external process</strong>; <span class="inline">/autorun</span> is an in-session slash '
                       'command that puts the current agent <strong>into autonomous mode in place</strong> (see the "slash '
                       'commands" lesson). The former suits unattended long-term deployment, the latter suits letting go '
                       'mid-conversation.') + '</p>')
            + c.qa(t, '⚠️ 自治不是放任', 'Autonomy is not a free-for-all',
                   '<p>' + t(
                       '自治模式下 Agent 会真的动手改文件、点界面，所以 <span class="inline">supervisor_sop.md</span> 很关键：'
                       '它划出边界、要求留痕与可回溯，避免“无人时跑偏”。配合分层记忆的 L4 归档，事后能完整复盘每一步。',
                       'In autonomous mode the agent really edits files and clicks UIs, so '
                       '<span class="inline">supervisor_sop.md</span> matters: it draws boundaries and demands traceability, '
                       'preventing "drift while unattended". Together with layered memory\'s L4 archiving, every step can be '
                       'fully reviewed afterward.') + '</p>'))

        + '<div class="card analogy"><div class="tag">🧩 '
        + t('生活类比', 'Analogy') + '</div>'
        + t(
            '像一个<strong>尽职的夜班值守</strong>：你下班走了，它不闲着——按巡检表定时转一圈，发现该处理的就处理，'
            '处理完在交接本上记一笔。第二天你回来，事办了，记录也都在。它不需要你一直盯着，因为“何时该动、该做什么、做完记什么”'
            '早已写进流程。',
            'Like a <strong>conscientious night-shift attendant</strong>: you clock out and leave, but it does not idle '
            '— it makes timed rounds per a checklist, handles whatever needs handling, and jots it in the handover log. '
            'You return the next day to find the work done and the records there. It does not need you watching, because '
            '"when to act, what to do, what to log" is already written into the procedure.',
        )
        + '</div>'

        + '<div class="card key"><div class="tag">✅ '
        + t('关键要点', 'Key Takeaways') + '</div><ul>'
        + '<li>' + t('长期自治 = 触发（离开/到点）+ 自驱（读 SOP）+ 留痕（记忆/L4）。',
            'Long-horizon autonomy = trigger (away/scheduled) + self-drive (read SOP) + trace (memory/L4).') + '</li>'
        + '<li>' + t('autonomous.py 是最小例子；scheduler.py 驱动定时任务。',
            'autonomous.py is the minimal example; scheduler.py drives scheduled tasks.') + '</li>'
        + '<li>' + t('规范见 autonomous_operation_sop / scheduled_task_sop / supervisor_sop。',
            'Rules in autonomous_operation_sop / scheduled_task_sop / supervisor_sop.') + '</li>'
        + '</ul></div>'

        + '<div class="card spark"><div class="tag">💡 '
        + t('设计亮点', 'Design Insight') + '</div>'
        + t(
            '看似高级的“长期自治”，其实没有引入任何新内核——它只是把<strong>反思探针 + 分层记忆 + SOP</strong> 三块旧积木拼起来：'
            '探针负责“何时动”，SOP 负责“做什么”，记忆负责“别忘了、别重复”。GA 的复杂能力几乎都是这样<strong>由简单件组合</strong>而来，'
            '而不是堆叠新机制——这正是“3K 行种子代码”能长出参天大树的秘密。',
            'The seemingly advanced "long-horizon autonomy" introduces no new core — it just snaps together three old '
            'blocks: <strong>reflection probes + layered memory + SOPs</strong>: probes decide "when to act", SOPs decide '
            '"what to do", memory ensures "do not forget, do not repeat". Almost all of GA\'s complex abilities arise this '
            'way, <strong>composed from simple parts</strong> rather than by piling on new mechanisms — the secret to how '
            '"3K lines of seed code" grows into a towering tree.',
        )
        + '</div>'
    )


