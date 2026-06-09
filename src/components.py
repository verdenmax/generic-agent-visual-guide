"""Reusable bilingual HTML building blocks for the deep-dive sections.

These helpers cut the repetitive ``<details>/<summary>/<div class="qa">``
boilerplate when thickening lessons. Each takes the translator ``t`` so all
visible text stays bilingual; ``*_html`` arguments are pre-built HTML strings
(already wrapped in ``t`` by the caller), inserted verbatim. Content is trusted,
author-written HTML — nothing is escaped (consistent with i18n.py).

Class names match the shell's CSS (.accordion/.badge-num/.hint/.acc-body/.qa
/.q/.a/.codefile/.cf-head). See the authoring conventions at the top of part1.py.
"""


def qa(t, q_zh, q_en, a_html):
    """One Q/A block inside an accordion body."""
    return (
        '<div class="qa"><div class="q">' + t(q_zh, q_en) + '</div>'
        '<div class="a">' + a_html + '</div></div>'
    )


def accordion(t, n, title_zh, title_en, body_html,
              hint_zh='点击展开', hint_en='click to expand'):
    """A collapsible deep-dive card: numbered summary + body."""
    return (
        '<details class="accordion"><summary><span class="badge-num">' + str(n)
        + '</span> ' + t(title_zh, title_en)
        + ' <span class="hint">' + t(hint_zh, hint_en) + '</span></summary>'
        '<div class="acc-body">' + body_html + '</div></details>'
    )


def codefile(path, label, code_html):
    """A filename-headed code block. ``path``/``label`` are language-neutral."""
    return (
        '<div class="codefile"><div class="cf-head"><span class="dot"></span>'
        '<span class="path">' + path + '</span>'
        '<span class="ln">' + label + '</span></div>'
        '<pre>' + code_html + '</pre></div>'
    )


def deepdive_heading(t):
    """The standard section heading that precedes a lesson's accordions."""
    return '<h2>🔬 ' + t('深入源码', 'Deep Dive') + '</h2>'
