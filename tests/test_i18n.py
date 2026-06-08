"""Tests for src/i18n.py (the bilingual helper module).

Import strategy:
    Production modules (shell.py, build.py, lessons) live in ``src/`` and import
    ``i18n`` directly (e.g. ``import i18n``) when run from inside ``src/``. To
    mirror that production import while still allowing ``python -m unittest``
    from the repo root, we insert the absolute ``src`` directory onto
    ``sys.path`` and then ``import i18n``. This keeps the import identical to
    production ("import i18n") without requiring an installable package.
"""

import io
import os
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import i18n  # noqa: E402  (import after sys.path tweak, mirrors production)


class TestTranslators(unittest.TestCase):
    def test_t_zh_returns_chinese(self):
        self.assertEqual(i18n.t_zh("中", "en"), "中")

    def test_t_en_returns_english(self):
        self.assertEqual(i18n.t_en("中", "en"), "en")


class TestBi(unittest.TestCase):
    def test_bi_basic(self):
        self.assertEqual(
            i18n.bi("中", "EN"),
            '<span class="zh">中</span><span class="en">EN</span>',
        )

    def test_bi_empty(self):
        self.assertEqual(
            i18n.bi("", ""),
            '<span class="zh"></span><span class="en"></span>',
        )

    def test_bi_no_escaping(self):
        self.assertEqual(
            i18n.bi('<b>&"中"</b>', '<b>&"EN"</b>'),
            '<span class="zh"><b>&"中"</b></span>'
            '<span class="en"><b>&"EN"</b></span>',
        )


class TestRenderBilingual(unittest.TestCase):
    def test_basic(self):
        out = i18n.render_bilingual(lambda t: t("中", "en"))
        self.assertEqual(out, '<div class="zh">中</div><div class="en">en</div>')

    def test_empty(self):
        out = i18n.render_bilingual(lambda t: "")
        self.assertEqual(out, '<div class="zh"></div><div class="en"></div>')

    def test_html_passthrough_no_escaping(self):
        out = i18n.render_bilingual(
            lambda t: f"<h2>{t('<b>标题</b>', '<b>Title</b>')}</h2>"
        )
        self.assertEqual(
            out,
            '<div class="zh"><h2><b>标题</b></h2></div>'
            '<div class="en"><h2><b>Title</b></h2></div>',
        )

    def test_special_chars_verbatim(self):
        out = i18n.render_bilingual(lambda t: t('<&>"a"', "<&>'b'"))
        self.assertEqual(
            out,
            '<div class="zh"><&>"a"</div><div class="en"><&>\'b\'</div>',
        )

    def test_multiple_t_calls(self):
        out = i18n.render_bilingual(lambda t: t("一", "one") + "|" + t("二", "two"))
        self.assertEqual(
            out,
            '<div class="zh">一|二</div><div class="en">one|two</div>',
        )

    def test_zh_before_en_ordering(self):
        out = i18n.render_bilingual(lambda t: t("中", "en"))
        self.assertLess(out.index('class="zh"'), out.index('class="en"'))

    def test_called_exactly_twice(self):
        counter = {"n": 0}

        def lesson(t):
            counter["n"] += 1
            return t("中", "en")

        i18n.render_bilingual(lesson)
        self.assertEqual(counter["n"], 2)

    def test_purity_no_output(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            i18n.render_bilingual(lambda t: t("中", "en"))
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
