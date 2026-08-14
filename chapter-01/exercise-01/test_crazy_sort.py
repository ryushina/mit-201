"""Tests for the instrumented crazy-sort algorithm."""

import unittest

from crazy_sort import crazy_sort


class CrazySortTests(unittest.TestCase):
    """Verify sorting, totals, and per-iteration instrumentation."""

    def test_required_input_and_trace(self) -> None:
        items = [3, 2, 4, 5, 2, 0]
        exchanges, comparisons, trace = crazy_sort(items)

        expected_trace = [
            (0, [0, 3, 4, 5, 2, 2], 2, 5),
            (1, [0, 2, 4, 5, 3, 2], 3, 9),
            (2, [0, 2, 2, 5, 4, 3], 5, 12),
            (3, [0, 2, 2, 3, 5, 4], 7, 14),
            (4, [0, 2, 2, 3, 4, 5], 8, 15),
            (5, [0, 2, 2, 3, 4, 5], 8, 15),
        ]

        self.assertEqual(items, [0, 2, 2, 3, 4, 5])
        self.assertEqual(exchanges, 8)
        self.assertEqual(comparisons, 15)
        self.assertEqual(trace, expected_trace)

    def test_already_sorted(self) -> None:
        items = [1, 2, 3, 4]
        exchanges, comparisons, _ = crazy_sort(items)

        self.assertEqual(items, [1, 2, 3, 4])
        self.assertEqual(exchanges, 0)
        self.assertEqual(comparisons, 6)

    def test_reverse_sorted(self) -> None:
        items = [5, 4, 3, 2, 1]
        exchanges, comparisons, _ = crazy_sort(items)

        self.assertEqual(items, [1, 2, 3, 4, 5])
        self.assertEqual(exchanges, 10)
        self.assertEqual(comparisons, 10)

    def test_duplicates(self) -> None:
        items = [3, 1, 3, 1]
        _, comparisons, _ = crazy_sort(items)

        self.assertEqual(items, [1, 1, 3, 3])
        self.assertEqual(comparisons, 6)

    def test_empty_list(self) -> None:
        items = []
        exchanges, comparisons, trace = crazy_sort(items)

        self.assertEqual(items, [])
        self.assertEqual((exchanges, comparisons), (0, 0))
        self.assertEqual(trace, [])

    def test_one_item(self) -> None:
        items = [42]
        exchanges, comparisons, trace = crazy_sort(items)

        self.assertEqual(items, [42])
        self.assertEqual((exchanges, comparisons), (0, 0))
        self.assertEqual(trace, [(0, [42], 0, 0)])


if __name__ == "__main__":
    unittest.main()
