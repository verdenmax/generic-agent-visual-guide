"""Unit tests for the bilingual deep-dive components."""
import os
import sys
import unittest

SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, SRC)

import components as c  # noqa: E402
import i18n  # noqa: E402


class TestComponents(unittest.TestCase):
    def test_qa_bilingual_and_verbatim_body(self):
        zh = c.qa(i18n.t_zh, "问", "Q", "<b>体</b>")
        en = c.qa(i18n.t_en, "问", "Q", "<b>体</b>")
        self.assertIn('<div class="qa">', zh)
        self.assertIn("问", zh)
        self.assertIn("Q", en)
        self.assertIn("<b>体</b>", zh)  # body inserted verbatim, not escaped

    def test_accordion_structure_and_number(self):
        html = c.accordion(i18n.t_zh, 3, "标题", "Title", "<p>x</p>")
        self.assertIn('class="accordion"', html)
        self.assertIn('class="badge-num">3</span>', html)
        self.assertIn("标题", html)
        self.assertIn("<p>x</p>", html)
        self.assertTrue(html.startswith("<details") and html.endswith("</details>"))

    def test_accordion_english_pass(self):
        html = c.accordion(i18n.t_en, 1, "标题", "Title", "<p>x</p>")
        self.assertIn("Title", html)
        self.assertNotIn("标题", html)

    def test_codefile_language_neutral(self):
        html = c.codefile("agent_loop.py", "agent_runner_loop", "code")
        self.assertIn('class="codefile"', html)
        self.assertIn("agent_loop.py", html)
        self.assertIn("agent_runner_loop", html)
        self.assertIn("<pre>code</pre>", html)

    def test_deepdive_heading_bilingual(self):
        self.assertIn("深入源码", c.deepdive_heading(i18n.t_zh))
        self.assertIn("Deep Dive", c.deepdive_heading(i18n.t_en))


if __name__ == "__main__":
    unittest.main()
