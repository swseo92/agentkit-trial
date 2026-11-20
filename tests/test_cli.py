import unittest

from src.cli import run


class RunTest(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(run(["--upper", "hi", "there"]), "HI THERE")

    def test_count(self):
        self.assertEqual(run(["--count", "a", "b", "c"]), "3")

    def test_plain(self):
        self.assertEqual(run(["hi"]), "hi")


if __name__ == "__main__":
    unittest.main()
