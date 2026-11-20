import unittest

from src.cli_args import parse


class ParseTest(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(parse([]), {"upper": False, "count": False, "text": ""})

    def test_flags_and_text(self):
        self.assertEqual(
            parse(["--upper", "hello", "world", "--count"]),
            {"upper": True, "count": True, "text": "hello world"},
        )

    def test_unknown_flag(self):
        with self.assertRaises(ValueError):
            parse(["--nope"])


if __name__ == "__main__":
    unittest.main()
