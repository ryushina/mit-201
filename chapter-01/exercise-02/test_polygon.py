"""Tests for the polygon inequality solution."""

import unittest

from polygon import can_form_polygon


class PolygonTests(unittest.TestCase):
    """Verify valid polygons, degenerate cases, and invalid input."""

    def test_valid_triangle(self) -> None:
        self.assertTrue(can_form_polygon([2, 3, 4]))

    def test_valid_quadrilateral(self) -> None:
        self.assertTrue(can_form_polygon([1, 1, 1, 1]))

    def test_valid_pentagon(self) -> None:
        self.assertTrue(can_form_polygon([2, 3, 4, 5, 6]))

    def test_degenerate_triangle(self) -> None:
        self.assertFalse(can_form_polygon([1, 2, 3]))

    def test_longest_segment_is_too_long(self) -> None:
        self.assertFalse(can_form_polygon([1, 1, 1, 3]))

    def test_zero_length(self) -> None:
        self.assertFalse(can_form_polygon([0, 2, 3]))

    def test_negative_length(self) -> None:
        self.assertFalse(can_form_polygon([-1, 2, 3]))

    def test_too_few_segments(self) -> None:
        self.assertFalse(can_form_polygon([5, 5]))
        self.assertFalse(can_form_polygon([]))

    def test_input_is_not_modified(self) -> None:
        lengths = [5, 2, 4, 3]
        original = lengths.copy()

        can_form_polygon(lengths)

        self.assertEqual(lengths, original)


if __name__ == "__main__":
    unittest.main()
