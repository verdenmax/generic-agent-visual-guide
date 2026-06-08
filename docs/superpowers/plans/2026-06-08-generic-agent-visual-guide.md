# GenericAgent 图解教程 · 实现计划（精简版）

**Goal:** 用无依赖 Python 生成器产出一套中英双语、可客户端切换的 GenericAgent 图解 HTML 教程。

**Architecture:** 内容写在 `src/partN.py`（lesson 函数 `lesson(t)`），`build.py` 套 `shell.py` 外壳生成静态 HTML。双语用 `i18n.py` 的 `t(zh,en)` 单写双渲 + CSS class 切换。

**Tech Stack:** Python 3（仅标准库）、纯静态 HTML/CSS/JS。

参考实现：`~/course/langchain-visual-guide/src/`（shell/build/registry/check_links 可直接借鉴）。

---

## 双语机制（关键）

- `<html class="lang-zh">` 默认中文；`<head>` 内联小脚本读 `localStorage('galang')` 设 `documentElement.className`，避免闪烁。
- CSS：`html.lang-zh .en{display:none}` / `html.lang-en .zh{display:none}`。
- 正文：`render_bilingual(lesson_fn)` 用 `t_zh`/`t_en` 渲染两遍，分别包 `<div class="zh">` / `<div class="en">`。
- 外壳零碎文案（标题/导航/部分名）：`bi(zh,en)` → `<span class="zh">…</span><span class="en">…</span>`。
- 顶栏语言按钮：点击切 `documentElement.className` + 写 `localStorage` + 改按钮文字。

---

## 文件结构

| 文件 | 职责 |
| :-- | :-- |
| `src/i18n.py` | `t_zh`/`t_en`、`bi(zh,en)`、`render_bilingual(fn)` |
| `src/shell.py` | CSS 设计系统、`PAGES`（双语标题/部分）、`page()`、`index_page()`、语言切换 JS |
| `src/part1.py … part6.py` | 各部分课程，每课 `lesson_NN(t)` |
| `src/glossary.py` | 术语表 `lesson_glossary(t)` |
| `src/registry.py` | `CONTENT = {fname: lesson_fn}` |
| `src/build.py` | 遍历 `PAGES` → 写 `index.html` + `lessons/*.html` |
| `src/check_links.py` | 生成站点内部死链检查（借鉴参考项） |
| `tests/test_build.py` | 构建冒烟 + 双语完整性 + 死链 |
| `README.md` `LICENSE` `.gitignore` | 说明 / MIT / 忽略 `__pycache__` |

---

## 任务清单

> 每个任务：写/改代码 → `python build.py` 跑通 → 提交。基础设施任务先写测试。

1. **脚手架** — 建 `src/`、`tests/`、`.gitignore`、`LICENSE(MIT)`、README 骨架。提交。
2. **i18n.py** — 实现 `t_zh`/`t_en`/`bi`/`render_bilingual`；`tests` 验证分支选择与双 div 包裹。
3. **shell.py 外壳** — 移植参考项 CSS + GA 主题色；加双语 CSS 规则、`<head>` 防闪脚本、顶栏语言按钮 + 切换 JS。
4. **shell.py 数据与渲染** — `PAGES`（23 条，含 `fname/title_zh/title_en/part_zh/part_en`）、`page()`（双语外壳+进度条+上下课导航）、`index_page()`（双语目录+搜索）。
5. **registry.py + build.py** — 映射 + 构建；`build()` 断言 `CONTENT` 键与 `PAGES` 一致。
6. **check_links.py + tests** — 死链检查；`tests/test_build.py` 断言：生成 24 个文件、每页含 `.zh` 与 `.en`、零死链。先跑通到“空内容也能 build”。
7. **内容·第一部分（1–3 课）** — 先把 lesson 01 写成完整范例确立模板，再补 2–3。每课结构：🌍宏观 / 🔬源码对应 / 🧩类比 / ✅要点 / 💡亮点。对照真实源码（见 spec 第 5 节映射）。
8. **内容·第二部分（4–7 课）** — 安装启动 / 前端形态 / 斜杠命令 / 九个原子工具。
9. **内容·第三部分（8–14 课）** — Agent Loop / llmcore / Handler 调度 / 分层记忆 / 记忆结晶 / 钩子可观测 / 渲染管线。
10. **内容·第四部分（15–19 课）** — 视觉 / 输入·移动端 / 浏览器注入 / 反思编排 / 长期自治。
11. **内容·第五部分（20–22 课）** — 自进化详解 / 端到端造技能 / 扩展前端。
12. **内容·第六部分（23 课）** — 术语表 + 源文件索引（带跳转锚点）。
13. **收尾** — 全量 `build.py` + `check_links.py` + 测试；完善 README（双语、如何重建、项目结构）。提交。

---

## 验收标准

- `cd src && python build.py` 仅用 Python 3 重建 `index.html` + `lessons/`（24 文件）。
- 每页双语可切换、`file://` 可直接打开、`python check_links.py` 零死链。
- 23 课内容对照 GenericAgent 真实源码（文件 + 符号名）。

**非目标（YAGNI）：** PDF/print、CI/CD、quizzes、第三语言。
