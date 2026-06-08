"""Integration tests for the build pipeline (registry, build.py, check_links).

Import strategy mirrors the other tests: insert the absolute ``src`` directory
onto ``sys.path`` so ``import shell`` / ``import build`` work like production.
The build writes real files into the repo (committed deliverables); we build
once in ``setUpClass`` and assert against the generated artifacts.
"""

import os
import sys
import tempfile
import unittest

SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, SRC)

import shell  # noqa: E402
import registry  # noqa: E402
import build  # noqa: E402
import check_links  # noqa: E402
import i18n  # noqa: E402

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

    def test_body_bilingual_all_pages(self):
        # Targets lesson BODY content (not just chrome) in a content-agnostic
        # way: render each lesson function through both i18n passes and assert
        # both renders are non-empty AND differ. Differing output proves the
        # lesson actually routed prose through t(...). This holds for the real
        # lessons (01-03) and the remaining stubs (04-23) alike.
        for fname, fn in registry.CONTENT.items():
            zh = fn(i18n.t_zh)
            en = fn(i18n.t_en)
            self.assertTrue(zh.strip(), f"{fname}: empty zh render")
            self.assertTrue(en.strip(), f"{fname}: empty en render")
            self.assertNotEqual(
                zh, en, f"{fname}: zh and en renders identical (missing t(...)?)"
            )

    def test_stale_file_cleanup(self):
        junk = os.path.join(ROOT, "lessons", "99-junk.html")
        with open(junk, "w", encoding="utf-8") as f:
            f.write("<!-- junk -->")
        self.assertTrue(os.path.exists(junk))
        build.build()
        self.assertFalse(os.path.exists(junk), "stale 99-junk.html not removed")
        for p in shell.PAGES:
            self.assertTrue(
                os.path.exists(os.path.join(ROOT, "lessons", p.fname)),
                f"missing lessons/{p.fname} after rebuild",
            )

    def test_stub_render_through_pipeline(self):
        # Verifies a still-stub lesson renders both i18n passes end-to-end
        # through the build pipeline. Lessons 01-03 now carry real content, so
        # this targets a remaining stub page (04-install.html).
        with open(os.path.join(ROOT, "lessons", "04-install.html"), encoding="utf-8") as f:
            html = f.read()
        zh = html.split('<div class="zh">', 1)[1].split('<div class="en">', 1)[0]
        en = html.split('<div class="en">', 1)[1]
        self.assertIn(ZH_PLACEHOLDER, zh)
        self.assertIn(EN_PLACEHOLDER, en)


class TestCheckLinksAnchors(unittest.TestCase):
    """Unit-style tests for anchor-aware check_links.check(root=...)."""

    def _build_site(self, root, index_html, lesson_html):
        os.makedirs(os.path.join(root, "lessons"), exist_ok=True)
        with open(os.path.join(root, "index.html"), "w", encoding="utf-8") as f:
            f.write(index_html)
        with open(os.path.join(root, "lessons", "a.html"), "w", encoding="utf-8") as f:
            f.write(lesson_html)

    def test_anchors_resolve(self):
        with tempfile.TemporaryDirectory() as root:
            self._build_site(
                root,
                index_html=(
                    '<a id="top"></a>'
                    '<a href="#top">self</a>'
                    '<a href="lessons/a.html#sec">cross</a>'
                ),
                lesson_html='<h2 id="sec">Section</h2>',
            )
            checked, broken = check_links.check(root=root)
            self.assertEqual(broken, [], f"unexpected broken: {broken}")
            self.assertGreater(checked, 0)

    def test_anchors_broken(self):
        with tempfile.TemporaryDirectory() as root:
            self._build_site(
                root,
                index_html=(
                    '<a id="top"></a>'
                    '<a href="#missing">bad self</a>'
                    '<a href="lessons/a.html#missing">bad cross</a>'
                ),
                lesson_html='<h2 id="sec">Section</h2>',
            )
            checked, broken = check_links.check(root=root)
            self.assertGreater(len(broken), 0)
            hrefs = {href for _, href, _ in broken}
            self.assertIn("#missing", hrefs)
            self.assertIn("lessons/a.html#missing", hrefs)
            for _, _, reason in broken:
                self.assertIn("missing anchor", reason)

    def test_missing_file_reason(self):
        with tempfile.TemporaryDirectory() as root:
            self._build_site(
                root,
                index_html='<a href="lessons/nope.html">gone</a>',
                lesson_html="<p>ok</p>",
            )
            checked, broken = check_links.check(root=root)
            self.assertTrue(
                any(reason == "missing file" for _, _, reason in broken),
                f"expected a missing-file reason, got {broken}",
            )


if __name__ == "__main__":
    unittest.main()
