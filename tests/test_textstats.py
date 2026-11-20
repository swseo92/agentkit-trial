import unittest

from src.textstats import word_count


class WordCount(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(word_count(""), 0)

    def test_one_word(self):
        self.assertEqual(word_count("hello"), 1)

    def test_several_spaces(self):
        self.assertEqual(word_count("  a   b    c  "), 3)

    def test_newlines_and_tabs(self):
        self.assertEqual(word_count("a\nb\n\nc\td"), 4)


if __name__ == "__main__":
    unittest.main()
