# 内容加深 / Depth Enhancement · 实现计划（精简版）

**Goal:** 在不改架构/双语机制/23 课结构的前提下，把每课加厚到"极致详尽"——5 卡主线 + 折叠深挖 accordion + 真实源码摘录 + 更多图表。

**Spec:** `docs/superpowers/specs/2026-06-09-depth-enhancement-design.md`

**分支:** feat/build-guide（继续）。**执行:** 一课一课改 → build → check_links → 测试 → leak/标签检查 → 提交。

---

## 每课加厚清单（统一模板）
1. 加厚 lead / macro / detail 正文（讲透 为什么/从哪来/怎么对比）。
2. 新增 `<h2>🔬 深入源码 / Deep Dive</h2>` 区，置于 detail 卡后、analogy 前，含 **≥2 个** `.accordion`（内部源码课 3–5 个），每个用 `.qa` 小块（🧪示例 ❓为什么 ⚙️内部 ⚠️坑点 🔀对比）。
3. 内部源码课多放真实 `.codefile` 摘录（文件+符号，`…` 省略）。
4. 按需补 flow/vflow/layers/cols/table.t 图表。
5. 每个可见字符串走 `t(zh,en)`；保留 5 卡。

## 任务（按部分逐课）
1. **测试加固**：在 tests 增加"每个非术语表课 ≥2 个 `.accordion`"的结构测试 + 可选 HTML 标签平衡测试。先让它对当前内容**预期失败/跳过**，加厚后转绿。
2. **Part 1 加厚**（01–03）逐课。
3. **Part 2 加厚**（04–07）逐课。
4. **Part 3 加厚**（08–14）逐课，源码摘录最密集。
5. **Part 4 加厚**（15–19）逐课。
6. **Part 5 加厚**（20–22）逐课。
7. **Part 6**（23 术语表）：酌情扩充词条/源文件行；豁免 5 卡与 accordion 数量要求。
8. **收尾**：全量 build + check_links + 测试；更新 README 徽章（如需）。

## 每课验收
- build 出 24 文件；check_links 零死链（新增 accordion 内链/锚点也要对）。
- 该课 EN 渲染无中文；含 zh+en 容器与 langbtn；5 卡齐全；≥2 个 accordion；HTML 平衡。
- `python -m unittest discover tests` 全绿。

## 非目标
不拆页、不加 PDF/CI、不改课程数与导航、不加第三方依赖、不重做设计系统。
