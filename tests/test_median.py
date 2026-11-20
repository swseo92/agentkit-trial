import unittest

from src.median import median


class Median(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_single(self):
        self.assertEqual(median([5]), 5)

    def test_unsorted_odd(self):
        self.assertEqual(median([9, 1, 5, 7, 3]), 5)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            median([])


if __name__ == "__main__":
    unittest.main()
