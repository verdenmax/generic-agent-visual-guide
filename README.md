# GenericAgent 图解教程 · Visual Guide

> 一套面向**完全新手**的双语（中文 / English）可视化（HTML 图解）教程，带你从零理解
> [GenericAgent](https://github.com/lsdefine/GenericAgent)——一个 ~3K 行的极简自进化自主 Agent 框架。
>
> A bilingual (中文 / English) illustrated HTML guide that takes a complete beginner from zero to
> understanding [GenericAgent](https://github.com/lsdefine/GenericAgent) — a ~3K-line minimal,
> self-evolving autonomous agent framework.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Lessons](https://img.shields.io/badge/lessons-23-blue.svg)
![Parts](https://img.shields.io/badge/parts-6-9cf.svg)
![Built with](https://img.shields.io/badge/built%20with-Python%203-3776AB.svg?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)
![Docs](https://img.shields.io/badge/docs-%E4%B8%AD%E6%96%87%20%2F%20EN-orange.svg)

本教程**对照 GenericAgent 真实源码核实**，源码引用以「**文件 + 符号名**」为主（不写死行号，避免随上游更新失效）。
All technical claims are **verified against the real GenericAgent source**, cited by **file + symbol name**
(no hard-coded line numbers, which drift as upstream changes).

---

## 🌐 双语 / Bilingual

每个页面都内嵌中英两份内容，顶栏的**语言切换按钮**（中 / EN）即时切换，纯静态、无后端，选择记忆在
`localStorage`。
Every page embeds both languages; the **language toggle** (中 / EN) in the top bar switches instantly —
pure static, no backend, with the choice remembered in `localStorage`.

## 🚀 如何阅读 / How to read

直接用浏览器打开 **`index.html`** 即可（支持 `file://` 直接打开）。
Just open **`index.html`** in a browser (works via `file://`).

```bash
# 可选：用任意静态服务器本地预览 / Optional: preview with any static server
python -m http.server 8000   # → http://localhost:8000/
```

## 📚 教程结构（6 部分 · 23 课）/ Structure (6 parts · 23 lessons)

**第一部分 · 宏观全景 / The Big Picture**
1. GenericAgent 是什么 / What is GenericAgent
2. 项目全景地图 / Project Map
3. 一次任务的生命周期 / Lifecycle of a Task

**第二部分 · 用户视角 / Using It**
4. 安装与启动 / Install & Launch
5. 前端形态总览 / Frontends Overview
6. 对话与斜杠命令 / Chat & Slash Commands
7. 九个原子工具 / The Nine Atomic Tools

**第三部分 · 内部源码 / Inside the Source**
8. Agent Loop 核心拆解 / The Agent Loop
9. LLM 内核 llmcore.py / The LLM Core
10. Handler 与工具调度 / Handler & Tool Dispatch
11. 分层记忆系统 L0–L4 / Layered Memory (L0–L4)
12. 记忆的读写与结晶 / Memory Read/Write & Crystallization
13. 钩子与可观测性 / Hooks & Observability
14. 上下文工程与 Token 效率 / Context Engineering & Token Efficiency

**第四部分 · 进阶能力 / Advanced Capabilities**
15. 计算机控制 · 视觉 / Computer Control · Vision
16. 输入与移动端 / Input & Mobile (ADB)
17. 浏览器注入与 Web 工具 / Browser Injection & Web Tools
18. 反思与编排 / Reflection & Orchestration
19. 长期自治与定时任务 / Long-Horizon Autonomy

**第五部分 · 实战 / Hands-On**
20. 自进化机制详解 / The Self-Evolution Mechanism
21. 端到端实战：造一个新技能 / End-to-End: Build a Skill
22. 扩展前端 / 接入新 IM / Extending Frontends

**第六部分 · 速查 / Reference**
23. 术语表 + 源文件索引 / Glossary & Source Index

## 🎨 每页包含 / On every page

- 🌍 **宏观理解 / The Big Picture** — 为什么这样设计 / why it is designed this way
- 🔬 **源码对应 / In the Source** — 指向真实源码文件 + 符号名 / real file + symbol names
- 🧩 **生活类比 / Analogy** — 用日常事物帮助理解 / an everyday analogy
- ✅ **关键要点 / Key Takeaways** — 每课小结 / a short summary
- 💡 **设计亮点 / Design Insight** — 该课最精妙的设计思想 / the "aha" design point
- 顶部进度条 + 语言切换 + 上一课 / 下一课导航 / progress bar + language toggle + prev/next nav

## 📁 项目结构 / Structure

```
generic-agent-visual-guide/
├── index.html              ← 入口（目录页）/ entry (table of contents)
├── lessons/                ← 23 课图解页面 / the 23 lesson pages
│   ├── 01-what-is-ga.html
│   └── … 23-glossary.html
├── src/                    ← 无依赖 Python 生成器 / no-dependency Python generators
│   ├── shell.py            共享外壳：CSS 设计系统 / 导航 / 语言切换 / index 页
│   ├── i18n.py             双语助手 t(zh,en) / render_bilingual
│   ├── part1.py … part5.py 各部分课程内容 / lesson content
│   ├── glossary.py         术语表 + 源文件索引 / glossary + source index
│   ├── registry.py         文件名 → 课程函数 映射 / filename → lesson map
│   ├── build.py            站点构建 / site build
│   └── check_links.py      内部死链 + 锚点检查 / internal link & anchor check
├── tests/                  ← Python unittest（构建 / 双语 / 死链）
├── README.md  LICENSE  .gitignore
```

## 🛠️ 重新生成 / Rebuild

所有 HTML 由 `src/` 下的生成器产出，**仅需 Python 3、零第三方依赖**。
All HTML is produced by the generators in `src/`, needing **only Python 3, zero third-party deps**.

```bash
cd src
python build.py          # 生成 index.html + lessons/ / build the site
python check_links.py    # 校验内部链接与锚点 / verify internal links & anchors
```

页面之间用相对链接互联，整体可直接拷贝、部署到任意静态服务器或 GitHub Pages。
Pages are interlinked with relative links, so the whole site can be copied to any static host or GitHub Pages.

## ✅ 测试 / Tests

```bash
python -m unittest discover tests   # 构建冒烟 · 双语完整性 · 死链 · 卡片格式
```

## 📄 许可 / License

本项目以 [MIT License](./LICENSE) 开源。
This project is open-sourced under the [MIT License](./LICENSE).

GenericAgent 为其作者的项目，相关名称与商标归其所有，详见
[官方仓库](https://github.com/lsdefine/GenericAgent)。本教程为独立的第三方学习材料，与官方无隶属关系。
GenericAgent belongs to its authors; related names and trademarks are theirs — see the
[official repo](https://github.com/lsdefine/GenericAgent). This guide is an independent, third-party
learning resource with no official affiliation.
