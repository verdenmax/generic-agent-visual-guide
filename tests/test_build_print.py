"""Smoke tests for the bilingual print/PDF build (build_print.py)."""
import os
import sys
import unittest
from html.parser import HTMLParser

SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, SRC)

import build_print  # noqa: E402
import shell  # noqa: E402

_VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
         "link", "meta", "param", "source", "track", "wbr"}


def _unbalanced(html):
    class _B(HTMLParser):
        def __init__(self):
            super().__init__()
            self.stack, self.err = [], []

        def handle_starttag(self, tag, attrs):
            if tag not in _VOID:
                self.stack.append(tag)

        def handle_endtag(self, tag):
            if tag in _VOID:
                return
            if not self.stack or self.stack[-1] != tag:
                self.err.append(tag)
            else:
                self.stack.pop()

    p = _B()
    p.feed(html)
    return p.stack, p.err


class TestBuildPrint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.written = build_print.build_print()
        cls.docs = {os.path.basename(p): open(p, encoding="utf-8").read()
                    for p in cls.written}

    def test_two_editions_written(self):
        self.assertEqual(
            set(self.docs), {"print-zh.html", "print-en.html"})

    def test_each_has_all_lessons(self):
        n = len(shell.PAGES)
        for name, html in self.docs.items():
            self.assertEqual(html.count('class="print-lesson"'), n, name)

    def test_accordions_forced_open(self):
        for name, html in self.docs.items():
            self.assertNotIn('<details class="accordion">', html, name)
            self.assertIn('<details class="accordion" open>', html, name)

    def test_language_class_per_file(self):
        self.assertIn('<html class="lang-zh"', self.docs["print-zh.html"])
        self.assertIn('<html class="lang-en"', self.docs["print-en.html"])

    def test_no_interactive_chrome(self):
        # Print editions drop the toggle button and search box.
        for name, html in self.docs.items():
            self.assertNotIn('id="langbtn"', html, name)
            self.assertNotIn('id="q"', html, name)

    def test_balanced(self):
        for name, html in self.docs.items():
            stack, err = _unbalanced(html)
            self.assertEqual(stack, [], f"{name}: unclosed {stack[-3:]}")
            self.assertEqual(err, [], f"{name}: stray {err[:3]}")


if __name__ == "__main__":
    unittest.main()
