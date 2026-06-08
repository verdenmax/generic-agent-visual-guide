"""Integration tests for the build pipeline (registry, build.py, check_links).

Import strategy mirrors the other tests: insert the absolute ``src`` directory
onto ``sys.path`` so ``import shell`` / ``import build`` work like production.
The build writes real files into the repo (committed deliverables); we build
once in ``setUpClass`` and assert against the generated artifacts.
"""

import os
import sys
import unittest

SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, SRC)

import shell  # noqa: E402
import registry  # noqa: E402
import build  # noqa: E402
import check_links  # noqa: E402

ROOT = build.ROOT
ZH_PLACEHOLDER = "本课内容正在编写中。"
EN_PLACEHOLDER = "This lesson is being written."


class TestBuildPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.written = build.build()

    def test_data_parity(self):
        self.assertEqual(
            set(registry.CONTENT.keys()),
            {p.fname for p in shell.PAGES},
        )

    def test_build_produces_all_files(self):
        self.assertTrue(os.path.exists(os.path.join(ROOT, "index.html")))
        for p in shell.PAGES:
            self.assertTrue(
                os.path.exists(os.path.join(ROOT, "lessons", p.fname)),
                f"missing lessons/{p.fname}",
            )
        self.assertEqual(len(shell.PAGES), 23)
        # 23 lessons + index = 24 written files
        self.assertEqual(len(self.written), 24)

    def test_bilingual_integrity(self):
        for p in shell.PAGES:
            with open(os.path.join(ROOT, "lessons", p.fname), encoding="utf-8") as f:
                html = f.read()
            self.assertIn('class="zh"', html, p.fname)
            self.assertIn('class="en"', html, p.fname)
            self.assertIn('id="langbtn"', html, p.fname)
            self.assertIn("<!DOCTYPE html>", html, p.fname)

    def test_index_integrity(self):
        with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
            html = f.read()
        for p in shell.PAGES:
            self.assertIn(f'href="lessons/{p.fname}"', html)
        self.assertIn('id="langbtn"', html)
        self.assertNotIn(".pdf", html)

    def test_no_dead_links(self):
        checked, broken = check_links.check()
        self.assertEqual(broken, [], f"broken links: {broken}")
        self.assertGreater(checked, 0)

    def test_stub_render_through_pipeline(self):
        with open(os.path.join(ROOT, "lessons", "01-what-is-ga.html"), encoding="utf-8") as f:
            html = f.read()
        zh = html.split('<div class="zh">', 1)[1].split('<div class="en">', 1)[0]
        en = html.split('<div class="en">', 1)[1]
        self.assertIn(ZH_PLACEHOLDER, zh)
        self.assertIn(EN_PLACEHOLDER, en)


if __name__ == "__main__":
    unittest.main()
