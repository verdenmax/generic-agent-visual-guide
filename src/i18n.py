"""Bilingual (中文/English) helpers for the generic-agent visual guide.

Lessons are authored as ``lesson(t)`` functions where ``t`` is a translator:
the author writes ``t('中文文本', 'English text')`` for every piece of prose.
The build renders each lesson twice — once with :func:`t_zh`, once with
:func:`t_en` — and :func:`render_bilingual` wraps the two renders in
``<div class="zh">…</div>`` and ``<div class="en">…</div>``.

Content is trusted, already-formatted HTML; nothing is escaped — all strings
pass through verbatim.
"""


def t_zh(zh, en):
    """Translator for the Chinese render pass; returns ``zh`` verbatim."""
    return zh


def t_en(zh, en):
    """Translator for the English render pass; returns ``en`` verbatim."""
    return en


def bi(zh, en):
    """Return inline bilingual chrome markup; no escaping, verbatim."""
    return '<span class="zh">' + zh + '</span><span class="en">' + en + '</span>'


def render_bilingual(lesson_fn):
    """Render ``lesson_fn`` twice (zh first, then en) and wrap in divs."""
    zh_html = lesson_fn(t_zh)
    en_html = lesson_fn(t_en)
    return '<div class="zh">' + zh_html + '</div><div class="en">' + en_html + '</div>'
