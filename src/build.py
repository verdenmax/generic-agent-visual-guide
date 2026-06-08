"""Build the static GenericAgent visual guide site into the project root.

Layout: ``ROOT/index.html`` and ``ROOT/lessons/NN-*.html``. Each lesson is
rendered bilingually via :func:`i18n.render_bilingual` and wrapped in the
shared HTML shell from :mod:`shell`.

Usage:
    cd src && python build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LESSONS_DIR = os.path.join(ROOT, "lessons")

sys.path.insert(0, HERE)

import shell
import i18n
from registry import CONTENT


def build():
    """Render every page to disk and return the written relative paths."""
    expected = {p.fname for p in shell.PAGES}
    have = set(CONTENT.keys())
    if have != expected:
        missing = sorted(expected - have)
        extra = sorted(have - expected)
        raise AssertionError(
            "registry.CONTENT does not match shell.PAGES — "
            f"missing: {missing}; extra: {extra}"
        )

    os.makedirs(LESSONS_DIR, exist_ok=True)
    written = []

    for p in shell.PAGES:
        content = i18n.render_bilingual(CONTENT[p.fname])
        html = shell.page(p.fname, content)
        out = os.path.join(LESSONS_DIR, p.fname)
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        written.append(os.path.relpath(out, ROOT))

    index_out = os.path.join(ROOT, "index.html")
    with open(index_out, "w", encoding="utf-8") as f:
        f.write(shell.index_page(lesson_prefix="lessons/"))
    written.append(os.path.relpath(index_out, ROOT))

    return written


if __name__ == "__main__":
    paths = build()
    print(f"✓ built {len(paths)} files:")
    for rel in paths:
        print(f"  {rel}")
