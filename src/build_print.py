"""Build single-page print editions for PDF export (one per language).

The interactive site shows one language at a time via a toggle; a PDF cannot
toggle, so we bake each language into its own continuous document:

    print-zh.html   (<html class="lang-zh">)
    print-en.html   (<html class="lang-en">)

Both share the SAME bilingual body (every lesson rendered via
``i18n.render_bilingual``); the ``<html>`` language class decides which half the
shell's CSS shows. All deep-dive ``<details class="accordion">`` are forced open
(``open`` attribute) and extra print CSS expands them, drops interactive chrome
(top bar, nav, toggle, search), and inserts a page break before each lesson.

A headless browser then renders each file to a PDF (see the deploy workflow).

Usage:
    cd src && python build_print.py        # writes ../print-zh.html and ../print-en.html
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

import shell  # noqa: E402
import i18n  # noqa: E402
from i18n import bi  # noqa: E402
from registry import CONTENT  # noqa: E402

PRINT_CSS = """
/* ---- print edition overrides ---- */
.topbar, .footnav, .lang-btn, .toc-search { display: none !important; }
.wrap { max-width: 760px; padding-top: 1rem; }
/* force every deep-dive accordion open and styled as a normal block */
details.accordion > summary { list-style: none; cursor: default; }
details.accordion > summary::after { display: none !important; }
details.accordion > summary .hint { display: none !important; }
details.accordion > .acc-body { display: block !important; }
/* one lesson per page */
.print-lesson { page-break-before: always; }
.print-lesson:first-of-type { page-break-before: avoid; }
.print-lesson > .lesson-head { margin: 0 0 .6rem; padding-bottom: .5rem;
  border-bottom: 2px solid var(--accent); }
.print-lesson > .lesson-head .pt { font-size: .72rem; letter-spacing: .06em;
  text-transform: uppercase; color: var(--accent); font-weight: 700; }
.print-lesson > .lesson-head h1 { font-size: 1.7rem; line-height: 1.2; margin-top: .2rem; }
.print-cover { text-align: center; padding: 3rem 0 1rem; }
.print-cover h1 { font-size: 2.3rem; line-height: 1.2; }
.print-cover .sub { color: var(--muted); margin-top: .8rem; font-size: 1.02rem; }
.print-cover .meta { color: var(--faint); margin-top: 1.2rem; font-size: .82rem; }
@media print {
  a { color: inherit; text-decoration: none; }
  .card, .codefile, .flow, .vflow, .layer, .col, table.t, .accordion {
    break-inside: avoid; }
  pre, .codefile pre { white-space: pre-wrap; word-break: break-word; }
}
"""


def _body():
    """Build the shared bilingual print body (cover + all lessons)."""
    parts = [
        '<div class="print-cover">',
        "<h1>" + bi("GenericAgent 图解教程", "GenericAgent Visual Guide") + "</h1>",
        '<p class="sub">'
        + bi("从零理解一个极简自进化 Agent 框架", "Understand a minimal, self-evolving agent framework from zero")
        + "</p>",
        '<p class="meta">'
        + bi(
            f"共 {len(shell.PAGES)} 课 · 对照 GenericAgent 真实源码",
            f"{len(shell.PAGES)} lessons · grounded in the real GenericAgent source",
        )
        + "</p>",
        "</div>",
    ]
    for idx, p in enumerate(shell.PAGES):
        content = i18n.render_bilingual(CONTENT[p.fname])
        content = content.replace(
            '<details class="accordion">', '<details class="accordion" open>'
        )
        head = (
            '<div class="lesson-head"><div class="pt">'
            + bi(p.part_zh, p.part_en)
            + "</div><h1>"
            + f"{idx + 1:02d} · "
            + bi(p.title_zh, p.title_en)
            + "</h1></div>"
        )
        parts.append(f'<section class="print-lesson">{head}{content}</section>')
    return "\n".join(parts)


def _doc(lang, body):
    lang_attr = "zh-CN" if lang == "zh" else "en"
    title = "GenericAgent 图解教程 · Visual Guide"
    return f"""<!DOCTYPE html>
<html class="lang-{lang}" lang="{lang_attr}"><head>
<meta charset="utf-8">
<title>{title}</title>
<style>{shell.CSS}{PRINT_CSS}</style>
</head><body>
<div class="wrap">
{body}
</div>
</body></html>"""


def build_print():
    body = _body()
    written = []
    for lang in ("zh", "en"):
        path = os.path.join(ROOT, f"print-{lang}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(_doc(lang, body))
        written.append(path)
    return written


if __name__ == "__main__":
    done = build_print()
    print("✓ built", len(done), "print editions:")
    for f in done:
        print("  -", os.path.relpath(f, ROOT))
