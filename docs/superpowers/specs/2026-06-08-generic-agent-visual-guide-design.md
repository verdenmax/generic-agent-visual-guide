# GenericAgent 图解教程（Visual Guide）· 设计文档

> 日期：2026-06-08　·　状态：已通过设计评审，待写实现计划
> 镜像参考项目：`~/course/langchain-visual-guide`（verdenmax/langchain-visual-guide）

## 1. 目标与背景

为 [GenericAgent](https://github.com/lsdefine/GenericAgent)（一个 ~3K 行的极简自进化自治 Agent 框架）
制作一套面向**完全新手**的可视化（HTML 图解）教程，既讲**宏观全景**，也拆**源码内部**，
每课对照 **GenericAgent 真实源码（文件 + 符号名）** 核实。

形态、设计系统、构建方式整体**模仿** `langchain-visual-guide`，但有三点关键差异：

1. **中英双语**，页面顶部按钮**客户端切换**（纯静态 HTML，无后端）。
2. 独立仓库，位于 `~/course/generic-agent-visual-guide`。
3. **暂不配置 CI/CD**（无 Pages/PDF 自动化），先本地 `python build.py` 生成 HTML。

### 适用人群
- 完全没接触过 GenericAgent、想从零入门的新手
- 想先建立宏观认知、再深入内部源码的学习者
- 准备阅读 / 调试 / 贡献 GenericAgent 源码的开发者

### 成功标准
- `cd src && python build.py` 在**仅需 Python 3、零第三方依赖**下重建 `index.html` + `lessons/`。
- 每个 lesson 页面：双语可切换、`file://` 直接打开可用、内部导航无死链。
- ~23 课内容覆盖 宏观→用法→源码内部→进阶→实战→速查，源码引用真实可查。
- `python check_links.py` 内部链接零死链。

## 2. 架构总览

沿用参考项「无依赖 Python 生成器 → 静态 HTML」架构：内容写在 `src/` 下的 Python 字符串里，
`build.py` 套上共享外壳（CSS 设计系统 + 导航 + 语言切换 JS）产出最终 HTML。

```
generic-agent-visual-guide/
├── index.html              ← 入口（目录页），从这里开始
├── lessons/                ← ~23 课图解页面（NN-*.html）
│   ├── 01-what-is-ga.html
│   └── … 23-glossary.html
├── src/                    ← 无依赖 Python 生成器（可重建全部 HTML）
│   ├── shell.py            共享外壳：CSS 设计系统、顶栏（进度条+语言切换）、导航、index 页
│   ├── i18n.py             双语助手：t(zh, en) + 双语渲染包装（render_bilingual）
│   ├── part1.py … part6.py 各部分课程内容（lesson 函数，签名 lesson(t)）
│   ├── glossary.py         术语表
│   ├── registry.py         课程文件名 → lesson 函数 的统一映射
│   ├── build.py            站点构建（→ index.html + lessons/）
│   └── check_links.py      内部死链检查
├── README.md               中英双语说明
├── LICENSE                 MIT
└── .gitignore              （忽略 __pycache__ 等）
```

### 与参考项的复用/差异对照
| 方面 | 参考项 langchain-visual-guide | 本项目 |
| :-- | :-- | :-- |
| 生成器架构 | src/ 无依赖 Python | ✅ 沿用 |
| 设计系统/卡片/进度条/导航 | shell.py | ✅ 沿用并微调主题色 |
| 语言 | 纯中文 | ⚠️ 中英双语 + 顶部切换 |
| 翻译机制 | 无 | ⚠️ 新增 i18n.py：`t(zh,en)` 单写双渲 |
| PDF/print 构建 | build_print.py | ❌ 暂不做 |
| CI（deploy.yml/ci.yml） | 有 | ❌ 暂不做 |
| 死链检查 check_links.py | 有 | ✅ 沿用 |

## 3. 双语机制（核心设计）

**方案 A · 翻译函数 `t(zh, en)`，单次编写、双次渲染**（已选定）

每课写成接受翻译器 `t` 的函数，文字处用 `t('中文', 'English')`，结构/图表/代码只写一遍：

```python
def lesson_01(t):
    return f"""
    <h2>{t('GenericAgent 是什么', 'What is GenericAgent')}</h2>
    <p>{t('它是一个极简的自进化 Agent。', 'A minimal self-evolving agent.')}</p>
    """
```

构建时对同一个 lesson 渲染两次，分别注入中/英 `t`，包进两层 `div`：

```html
<div class="lang lang-zh"> …中文渲染… </div>
<div class="lang lang-en" hidden> …英文渲染… </div>
```

顶栏语言按钮通过 JS 给 `<body>` 切换 `lang-zh` / `lang-en` class，CSS 控制两块的显隐，
并用 `localStorage` 记住选择（跨页面保持）。默认显示中文。

**关键约束**：
- `t` 的两个分支必须产生**结构一致**的 HTML（仅文字不同），否则切换时布局会跳。
  → i18n.py 提供 `render_bilingual(lesson_fn)`，内部两次调用并断言两版**顶层结构标签数量一致**（轻量校验，发现明显漂移时报错）。
- 纯客户端、无网络请求；`file://` 与任意静态服务器均可用。
- 进度条、导航文案（上一课/下一课/返回目录）等外壳文案也走 `t`，随 body class 切换。

被否决的备选：
- 方案 B（每课中英各写整份 HTML）：图表/代码复制两遍，维护翻倍。
- 方案 C（逐元素内联 `<span lang>`）：HTML 噪音大、块级元素难处理。

## 4. 页面格式（每课包含）

镜像参考项的「每页包含」，并加入语言切换：

- 顶栏：**进度条** + **语言切换按钮（中 / EN）** + 课程标题
- 🌍 **宏观理解** — 大局观，为什么这样设计
- 🔬 **源码对应** — 指向 GenericAgent 真实源码文件 + 符号名（如 `agent_loop.py: agent_runner_loop`）
- 🧩 **生活类比** — 用日常事物帮助理解抽象概念
- ✅ **关键要点** — 每课小结
- 💡 **设计亮点** — 该课最精妙的设计思想
- 底部：上一课 / 下一课 / 返回目录 导航

**版本锚点**：对照 GenericAgent `main` 分支源码讲解，核验时间记于页脚；源码引用以
「**文件 + 符号名**」为主（不写死行号，避免随上游更新失效）。

## 5. 课程结构（6 部分 · 23 课）

> 每课标注主要对应的真实源码，供写作时核对。

### 第一部分 · 宏观全景
1. **GenericAgent 是什么** — 解决的问题 ·「不预装技能，而是进化」设计哲学 · 与传统 Agent 区别（`README.md`）
2. **项目全景地图** — 目录结构 · 核心文件 · ~3K 行种子代码各模块职责（仓库根目录、`ga.py`、`agentmain.py`）
3. **一次任务的生命周期** — 用户输入 → system prompt → LLM → 工具调用 → 结果回写 → 循环（`agent_loop.py`、`agentmain.py`）

### 第二部分 · 用户视角
4. **安装与启动** — Python 版本要求 · `uv`/pip · `mykey` · `launch.pyw`（`docs/installation*.md`、`mykey_template.py`）
5. **前端形态总览** — 桌面 App / TUI / Streamlit / IM bots / 桌面宠物（`frontends/`）
6. **对话与斜杠命令** — `/new`、`/continue`、其他 slash 命令（`frontends/slash_cmds.py`、`continue_cmd.py`）
7. **九个原子工具** — `code_run` / `file_read` / `file_write` / `file_patch` / `web_scan` / `web_execute_js` / `ask_user` / `update_working_checkpoint` / `start_long_term_update`

### 第三部分 · 内部源码
8. **Agent Loop 核心拆解** — `messages` · turn 循环 · `tool_calls` · `StepOutcome` · `next_prompt`（`agent_loop.py: agent_runner_loop`）
9. **LLM 内核 llmcore.py** — 多模型适配 · 流式 `chat` · tools schema · 工具调用解析（`llmcore.py`）
10. **Handler 与工具调度** — `BaseHandler.dispatch` · `do_*` 方法 · generator 协议（`agent_loop.py: BaseHandler`、`agentmain.py`）
11. **分层记忆系统 L0–L4** — Meta Rules / Insight Index / Global Facts / Skills·SOP / Session Archive（`memory/` 目录、各 `*_sop.md`）
12. **记忆的读写与结晶** — `update_working_checkpoint` · `start_long_term_update` · 进程记忆扫描 · 记忆清理（`memory/procmem_scanner.py`、`memory/checklist_helper.py`、`memory_*_sop.md`）
13. **钩子与可观测性** — `plugins/hooks.py` 触发点（agent/turn/llm/tool before/after）· langfuse 追踪（`plugins/hooks.py`、`plugins/langfuse_tracing.py`）
14. **渲染与展示管线** — `simphtml.py` 终端/前端 Markdown→HTML 展示（`simphtml.py`）

### 第四部分 · 进阶能力
15. **计算机控制 · 视觉** — 截屏 → OCR → 元素定位 → 操作（`memory/vision_api.template.py`、`ocr_utils.py`、`ui_detect.py`、`vision_sop.md`）
16. **输入与移动端** — 鼠标/键盘控制 · ADB 安卓控制（`memory/ljqCtrl.py`、`adb_ui.py`、`ljqCtrl_sop.md`）
17. **浏览器注入与 Web 工具** — 注入真实浏览器（保留登录态）· `web_scan`/`web_execute_js`（`TMWebDriver.py`、`tmwebdriver_sop.md`、`web_setup_sop.md`）
18. **反思与编排** — 目标模式 · 调度器 · 清单主控 · 子代理团队（`reflect/goal_mode.py`、`scheduler.py`、`checklist_master.py`、`agent_team_worker.py`）
19. **长期自治与定时任务** — 自治运行 SOP · 定时任务 · supervisor（`reflect/autonomous.py`、`scheduler.py`、`autonomous_operation_sop.md`、`scheduled_task_sop.md`、`supervisor_sop.md`）

### 第五部分 · 实战
20. **自进化机制详解** — 新任务 → 自主探索 → 结晶为 Skill → 下次直接召回 的完整闭环（`memory/skill_search`、`incubator_sop.md`、`README.md` 自进化章节）
21. **端到端实战：造一个新技能** — 完整示例：从一次性任务到沉淀为可复用 SOP
22. **扩展前端 / 接入新 IM** — conductor 编排 · 新增一个 bot（`frontends/conductor.py`、`frontends/*app.py`）

### 第六部分 · 速查
23. **术语表 + 源文件索引** — 全书术语一句话查 + 点链接跳到对应课 + 核心源文件地图（`glossary.py`）

## 6. 组件职责与接口

| 模块 | 职责 | 关键接口 |
| :-- | :-- | :-- |
| `shell.py` | CSS 设计系统、`<head>` 元信息、顶栏（进度条+语言切换+标题）、上下课导航、index 目录页 | `page(fname, content, …)`、`index_page(…)`、`PAGES`、`PARTS`、语言切换 JS 注入 |
| `i18n.py` | 双语支持 | `t_zh(zh,en)→zh`、`t_en(zh,en)→en`、`render_bilingual(lesson_fn)→html`、外壳文案表 |
| `partN.py` | 课程内容 | 每课一个 `lesson_NN(t)` 函数，返回 HTML 片段 |
| `glossary.py` | 术语表 | `lesson_glossary(t)` |
| `registry.py` | 单一事实源：文件名 → lesson 函数 的有序映射 | `CONTENT = {fname: lesson_fn}` |
| `build.py` | 站点构建 | `build()` → 写 `index.html` + `lessons/*.html` |
| `check_links.py` | 死链检查 | 扫描生成的 HTML，校验内部 `href` 指向存在的文件/锚点 |

**模块边界原则**：内容（partN）与外壳（shell）解耦——改样式只动 `shell.py`，加课只动 `partN.py`+`registry.py`+`shell.PAGES`。`i18n.py` 是内容与外壳共享的纯函数层，无副作用。

## 7. 数据流

```
PAGES (shell.py: 文件名/标题/部分 有序表)
   │
build.py 遍历 PAGES
   │  fname → registry.CONTENT[fname] = lesson_fn
   ▼
i18n.render_bilingual(lesson_fn)
   │  zh = lesson_fn(t_zh) → <div class="lang lang-zh">
   │  en = lesson_fn(t_en) → <div class="lang lang-en" hidden>
   ▼
shell.page(fname, bilingual_content)  套外壳（CSS+顶栏+导航+语言切换 JS）
   ▼
写入 lessons/NN-*.html ；最后写 index.html
```

运行时（浏览器）：语言按钮 → JS 设 `body.class = lang-zh|lang-en` + `localStorage` →
CSS `.lang-en .lang-zh{display:none}` 等规则切换显隐。

## 8. 错误处理与健壮性

- **构建期**：`registry.CONTENT` 的键必须与 `shell.PAGES` 文件名一一对应；`build.py` 启动时断言两者集合相等，缺失/多余即报错退出。
- **双语漂移**：`render_bilingual` 轻量校验中英两版顶层标签数量一致，明显不一致时打印警告（不强制中断，避免误杀合法差异）。
- **死链**：`check_links.py` 作为独立校验脚本，CI 暂不接但保留供本地运行。
- **`file://` 兼容**：不使用任何需要 HTTP 的特性（无 fetch、无外链 JS/CSS、资源内联）。

## 9. 测试策略

> 用户偏好：多测试，加 corner 测试与核心测试，可由独立 subagent 补测。

- **构建冒烟测试**：运行 `build.py`，断言生成了预期数量的 lesson 文件 + `index.html`。
- **双语完整性**：每个生成页面都同时含 `lang-zh` 与 `lang-en` 两个容器；语言切换 JS 与按钮存在。
- **死链测试**：`check_links.py` 对生成站点零死链（含 index→lessons、lesson↔lesson、术语表锚点）。
- **结构一致性 corner**：构造一个中英标签数不一致的样例，验证 `render_bilingual` 校验能发现。
- **`file://` 可用性**：抽查页面不含绝对路径/外链依赖。
- 测试以无依赖的 Python `unittest` 或简单脚本实现，置于 `src/` 或 `tests/`，可独立运行。

## 10. 范围与非目标（YAGNI）

**做**：23 课双语 HTML、生成器、index 目录页、死链检查、README/LICENSE、基础测试。

**暂不做**（明确排除）：
- PDF / `print.html` 构建
- GitHub Actions（Pages 部署、PDF 渲染、防回归 CI）
- 在线搜索、评论、quizzes 交互题（参考项有 quizzes，本期不纳入）
- 多于中/英的第三语言

这些可作为后续迭代，不阻塞本期交付。

## 11. 实现里程碑（概要，详见后续实现计划）

1. 脚手架：目录、`shell.py` 外壳 + 设计系统 + 语言切换、`i18n.py`、`build.py`、`registry.py`、README/LICENSE/.gitignore。
2. 先打通 1–3 课 + index，跑通 `build.py` 与切换，确立模板。
3. 按部分逐批填充 4–23 课，每课对照真实源码核实。
4. `check_links.py` + 测试，本地全量校验。
5. 文档收尾、提交。
