import unittest

from src.slug import slugify


class Slugify(unittest.TestCase):
    def test_runs_of_non_alphanumerics_become_one_dash(self):
        self.assertEqual(slugify("Hello,  World!"), "hello-world")

    def test_no_leading_or_trailing_dash(self):
        self.assertEqual(slugify("  --Hi--  "), "hi")

    def test_empty(self):
        self.assertEqual(slugify("!!!"), "")

    def test_digits_kept(self):
        self.assertEqual(slugify("A1 b2"), "a1-b2")
