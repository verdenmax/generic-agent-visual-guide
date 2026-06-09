# GenericAgent 图解教程 · 内容加深 / Depth Enhancement · 设计文档

> 日期：2026-06-09　·　状态：已通过设计评审　·　分支：feat/build-guide
> 背景：23 课已完成但每课偏薄（~2.4–3.7K 字）。目标：极致详尽地加厚，对标参考项 langchain-visual-guide 的深度。

## 1. 目标

在<strong>不改变</strong>现有架构、双语机制、6 部分 23 课结构的前提下，把每一课<strong>显著加厚</strong>到"极致详尽"：
保留 5 卡主线作为可扫读的脊柱，用可折叠的深挖 accordion + 更多真实源码摘录 + 更多图表叠加深度。深度"按需展开"，页面不至于变成长墙。

成功标准：
- 每课（术语表除外）在原 5 卡之上新增「深入源码 / Deep Dive」区，含 **≥2 个**（内部源码课建议 3–5 个）`.accordion` 深挖卡。
- 内部源码课（Part 3/4）新增真实 `.codefile` 源码摘录（文件+符号，`…` 省略，对照真实代码）。
- 仍：每个可见字符串走 `t(zh,en)`；EN 渲染无中文泄漏；HTML 标签平衡；`check_links` 零死链；全测试通过。
- 体量大致达到参考项级别（每课显著变长，无硬性字数）。

## 2. 每课深挖模板（在现有 5 卡之上叠加）

现有顺序：lead → 🌍macro → （图/表）→ 🔬detail → 🧩analogy → ✅key → 💡spark。加深后插入/扩充：

1. **更厚的 lead / macro / detail 正文**：把"为什么这么设计、它从哪来、和别的做法比"讲透。
2. **新增「深入源码 / Deep Dive」区**（置于 detail 卡之后、analogy 之前）：
   `<h2>🔬 深入源码 / Deep Dive</h2>` + 2–5 个 accordion。每个 accordion 用 `.qa` 小块组织，按需选取：
   - 🧪 **示例 / 代码 (Example / Code)** — 真实片段或最小可懂示例
   - ❓ **为什么这样设计 (Why)** — 设计动机、约束
   - ⚙️ **内部怎么走 (Under the hood)** — 调用链 / 数据流
   - ⚠️ **坑点 (Gotchas)** — 真实注释里的坑、边界
   - 🔀 **其他方案 / 对比 (Alternatives)** — 和传统做法对照
3. **更多真实源码摘录**：内部源码课多放 `.codefile`（标注 文件+符号）。
4. **更多图表**：flow / vflow / layers / cols / table.t，按需补充。
5. 5 卡保留；内容可同步加厚。

accordion 结构范式（每个可见字符串仍走 `t()`）：
```html
<details class="accordion"><summary><span class="badge-num">1</span> 标题 <span class="hint">点击展开</span></summary>
  <div class="acc-body">
    <div class="qa"><div class="q">🧪 示例</div><div class="a">…</div></div>
    <div class="qa"><div class="q">❓ 为什么</div><div class="a">…</div></div>
  </div>
</details>
```
所用 CSS 类（`.accordion/.summary/.badge-num/.hint/.acc-body/.qa/.q/.a/.codefile`）均已在 shell.py 中样式化，无需改 shell。

## 3. 各课深挖侧重（指引，非穷举）

- **Part 1（1–3）**：1 加"加法 vs 减法"对比、与 Claude Code/OpenManus 对照深挖；2 各模块职责深挖 + 行数地图；3 逐轮数据流 accordion + 真实 loop 摘录。
- **Part 2（4–7）**：4 两种安装路线/协议深挖 + mykey 字段；5 各前端取舍 + chatapp_common 复用；6 /continue 恢复内部 + 命令即提示词；7 每个工具一条 accordion（参数、坑、何时用）。
- **Part 3（8–14）**：源码最密集。8 agent_runner_loop 逐段；9 文本协议 vs 原生、SSE、Mock 归一；10 dispatch/generator 协议/try_call_generator；11 各层文件与指针链；12 两工具内部 + L0 铁律；13 八事件 + langfuse；14 _clean_content/_compact_tool_args/compress_history 逐个摘录。多放 `.codefile`。
- **Part 4（15–19）**：15 detect 返回结构/VLM 保底/坑；16 物理坐标/pyautogui 禁忌/u2 vs adb；17 TMWebDriver WS 桥/simphtml 简化/登录态；18 reflect 约定 check()/四种模块；19 触发-自驱-留痕闭环 + autonomous.py 摘录。
- **Part 5（20–22）**：20 闭环每步深挖 + Morphling/Incubator；21 第一次 vs 之后逐步 + 真实工具链；22 适配器最小骨架 + conductor。
- **Part 6（23 术语表）**：保持参考页性质，可酌情扩充词条/源文件行；**豁免** 5 卡与 accordion 数量要求。

## 4. 测试

新增/保留（stdlib unittest）：
- **新增**：每个非术语表课 `.accordion` 出现 **≥2 次**（深度结构测试，随加厚自动覆盖）。
- 保留：5 卡格式（术语表豁免）、EN 无中文泄漏、每课含 zh+en 容器与 langbtn、`build` 24 文件、`check_links` 零死链（含锚点）、HTML 标签平衡（可加一个解析平衡测试）。

## 5. 执行方式

- 仍在 `feat/build-guide` 分支；按用户偏好<strong>一课一课</strong>加厚：改对应 lesson 函数 → build → check_links → 测试 → leak/平衡检查 → 提交。
- 不改 shell.py / i18n.py / build.py / check_links.py（除非深度测试需要小改 tests）。
- 顺序：Part 1 → 6，逐课推进，用户可随时抽查。

## 6. 非目标（YAGNI）

不拆分页面、不加 PDF/CI、不改导航与课程数量、不引入第三方依赖、不重做设计系统。
