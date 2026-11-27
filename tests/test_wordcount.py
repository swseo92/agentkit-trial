"""wordcount: 빈 입력, 한 줄, 여러 줄(한글 포함)."""
import io
import unittest
from contextlib import redirect_stdout
from unittest import mock

from src import wordcount


def run(text, *args):
    out = io.StringIO()
    with mock.patch("sys.stdin", io.StringIO(text)), redirect_stdout(out):
        wordcount.main(args)
    return out.getvalue()


class WordCount(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(run(""), "0 0 0\n")

    def test_one_line(self):
        self.assertEqual(run("hello world\n"), "1 2 12\n")

    def test_several_lines_with_korean(self):
        self.assertEqual(run("안녕 세상\nhello\n하나 둘 셋\n"), "3 6 19\n")

    def test_chars_only(self):
        self.assertEqual(run("ab\ncd\n", "--chars-only"), "6\n")


if __name__ == "__main__":
    unittest.main()
