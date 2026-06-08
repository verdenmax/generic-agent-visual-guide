"""Tests for src/shell.py (the bilingual HTML shell).

Import strategy mirrors tests/test_i18n.py: insert the absolute ``src``
directory onto ``sys.path`` so that ``import shell`` works identically to
production (modules in ``src/`` import ``i18n`` / ``shell`` directly).
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import shell  # noqa: E402  (import after sys.path tweak, mirrors production)


class TestPages(unittest.TestCase):
    def test_count_is_23(self):
        self.assertEqual(len(shell.PAGES), 23)

    def test_fnames_unique(self):
        fnames = [p.fname for p in shell.PAGES]
        self.assertEqual(len(fnames), len(set(fnames)))

    def test_first_and_last(self):
        self.assertEqual(shell.PAGES[0].fname, "01-what-is-ga.html")
        self.assertEqual(shell.PAGES[-1].fname, "23-glossary.html")

    def test_every_entry_has_bilingual_title_and_part(self):
        for p in shell.PAGES:
            self.assertTrue(p.title_zh, f"{p.fname} missing title_zh")
            self.assertTrue(p.title_en, f"{p.fname} missing title_en")
            self.assertTrue(p.part_zh, f"{p.fname} missing part_zh")
            self.assertTrue(p.part_en, f"{p.fname} missing part_en")

    def test_namedtuple_fields(self):
        self.assertEqual(
            shell.PAGES[0]._fields,
            ("fname", "title_zh", "title_en", "part_zh", "part_en"),
        )

    def test_subtitles_page_key_parity(self):
        page_fnames = {p.fname for p in shell.PAGES}
        self.assertEqual(set(shell.SUBTITLES.keys()), page_fnames)
        for fname, value in shell.SUBTITLES.items():
            self.assertIsInstance(value, tuple, f"{fname} subtitle not a tuple")
            self.assertEqual(len(value), 2, f"{fname} subtitle not a 2-tuple")
            zh, en = value
            self.assertTrue(zh, f"{fname} missing subtitle zh")
            self.assertTrue(en, f"{fname} missing subtitle en")
            self.assertIsInstance(zh, str, f"{fname} subtitle zh not a str")
            self.assertIsInstance(en, str, f"{fname} subtitle en not a str")


class TestPage(unittest.TestCase):
    def setUp(self):
        self.html = shell.page("01-what-is-ga.html", "XYZCONTENT")

    def test_doctype(self):
        self.assertIn("<!DOCTYPE html>", self.html)

    def test_default_lang_class(self):
        self.assertIn('class="lang-zh"', self.html)

    def test_fouc_script(self):
        self.assertIn("localStorage", self.html)
        self.assertIn("documentElement.className", self.html)
        self.assertIn("galang", self.html)

    def test_bilingual_css_rules(self):
        self.assertIn("html.lang-zh .en", self.html)
        self.assertIn("html.lang-en .zh", self.html)

    def test_toggle_button(self):
        self.assertIn('id="langbtn"', self.html)
        self.assertIn("lang-btn", self.html)

    def test_verbatim_content(self):
        self.assertIn("XYZCONTENT", self.html)

    def test_progress_width(self):
        self.assertIn("width:", self.html)
        self.assertIn("%", self.html)

    def test_title_bilingual(self):
        self.assertIn("GenericAgent 是什么", self.html)
        self.assertIn("What is GenericAgent", self.html)

    def test_chrome_has_both_languages(self):
        self.assertIn('class="zh"', self.html)
        self.assertIn('class="en"', self.html)

    def test_returns_nonempty_str(self):
        self.assertIsInstance(self.html, str)
        self.assertTrue(self.html)

    def test_balanced_html_tags(self):
        self.assertEqual(self.html.count("<html"), 1)
        self.assertEqual(self.html.count("</html>"), 1)


class TestPageNav(unittest.TestCase):
    def test_first_prev_points_home(self):
        html = shell.page("01-what-is-ga.html", "C")
        self.assertIn('href="../index.html"', html)

    def test_last_next_points_home(self):
        html = shell.page("23-glossary.html", "C")
        # the next link on the last lesson returns to the index
        self.assertIn('href="../index.html"', html)

    def test_middle_lesson_siblings(self):
        html = shell.page("08-agent-loop.html", "C")
        self.assertIn('href="07-tools.html"', html)
        self.assertIn('href="09-llmcore.html"', html)

    def test_custom_home_href(self):
        html = shell.page("01-what-is-ga.html", "C", home_href="../start.html")
        self.assertIn('href="../start.html"', html)

    def test_unknown_fname_raises_keyerror(self):
        with self.assertRaises(KeyError):
            shell.page("does-not-exist.html", "X")

    def test_toggle_js_pins_bilingual_button_contract(self):
        html = shell.page("01-what-is-ga.html", "C")
        self.assertIn("'EN'", html)
        self.assertIn("'中'", html)


class TestProgress(unittest.TestCase):
    def test_last_lesson_pct_100(self):
        html = shell.page("23-glossary.html", "C")
        self.assertIn("width:100%", html)

    def test_pct_increases_with_index(self):
        h1 = shell.page("01-what-is-ga.html", "C")
        h12 = shell.page("12-memory-crystallize.html", "C")
        import re

        def pct(h):
            return int(re.search(r"width:(\d+)%", h).group(1))

        self.assertLess(pct(h1), pct(h12))


class TestIndexPage(unittest.TestCase):
    def setUp(self):
        self.html = shell.index_page()

    def test_all_fnames_present(self):
        for p in shell.PAGES:
            self.assertIn(f'href="lessons/{p.fname}"', self.html)

    def test_toggle_button(self):
        self.assertIn('id="langbtn"', self.html)

    def test_search_input(self):
        self.assertIn('id="q"', self.html)

    def test_both_languages_chrome(self):
        self.assertIn('class="zh"', self.html)
        self.assertIn('class="en"', self.html)

    def test_no_pdf_link(self):
        self.assertNotIn(".pdf", self.html)

    def test_custom_prefix(self):
        html = shell.index_page(lesson_prefix="")
        self.assertIn('href="01-what-is-ga.html"', html)

    def test_returns_nonempty_str(self):
        self.assertIsInstance(self.html, str)
        self.assertTrue(self.html)

    def test_balanced_html_tags(self):
        self.assertEqual(self.html.count("<html"), 1)
        self.assertEqual(self.html.count("</html>"), 1)

    def test_fouc_script(self):
        self.assertIn("documentElement.className", self.html)
        self.assertIn("galang", self.html)

    def test_bilingual_css_rules(self):
        self.assertIn("html.lang-zh .en", self.html)
        self.assertIn("html.lang-en .zh", self.html)

    def test_all_six_part_headers_present_in_order(self):
        labels = ["第一部分", "第二部分", "第三部分", "第四部分", "第五部分", "第六部分"]
        for label in labels:
            self.assertIn(label, self.html, f"{label} missing from index_page")
        positions = [self.html.index(label) for label in labels]
        self.assertEqual(
            positions,
            sorted(positions),
            "part headers not in top-to-bottom order",
        )


if __name__ == "__main__":
    unittest.main()
