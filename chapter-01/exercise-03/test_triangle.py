"""Tests for the operation-conscious triangle classifier."""

import unittest

from triangle import (
    ACUTE_ANGLED,
    NOT_A_TRIANGLE,
    OBTUSE_ANGLED,
    RIGHT_ANGLED,
    arrange_with_largest_last,
    classify_triangle,
)


class TriangleTests(unittest.TestCase):
    """Verify validity and angle classifications."""

    def test_right_triangle(self) -> None:
        self.assertEqual(classify_triangle(3, 4, 5), RIGHT_ANGLED)

    def test_right_triangle_with_largest_first(self) -> None:
        self.assertEqual(classify_triangle(5, 3, 4), RIGHT_ANGLED)

    def test_all_positions_can_contain_largest_side(self) -> None:
        self.assertEqual(classify_triangle(4, 5, 3), RIGHT_ANGLED)
        self.assertEqual(classify_triangle(4, 3, 5), RIGHT_ANGLED)

    def test_obtuse_triangle(self) -> None:
        self.assertEqual(classify_triangle(2, 3, 4), OBTUSE_ANGLED)

    def test_acute_triangles(self) -> None:
        self.assertEqual(classify_triangle(4, 5, 6), ACUTE_ANGLED)
        self.assertEqual(classify_triangle(1, 1, 1), ACUTE_ANGLED)

    def test_degenerate_triangles(self) -> None:
        self.assertEqual(classify_triangle(1, 2, 3), NOT_A_TRIANGLE)
        self.assertEqual(classify_triangle(1, 1, 3), NOT_A_TRIANGLE)

    def test_nonpositive_lengths(self) -> None:
        self.assertEqual(classify_triangle(0, 4, 5), NOT_A_TRIANGLE)
        self.assertEqual(classify_triangle(-3, 4, 5), NOT_A_TRIANGLE)

    def test_largest_side_helper(self) -> None:
        for sides in [(5, 3, 4), (3, 5, 4), (3, 4, 5), (5, 5, 3)]:
            a, b, c = arrange_with_largest_last(*sides)
            self.assertEqual(c, max(sides))
            self.assertCountEqual((a, b, c), sides)


if __name__ == "__main__":
    unittest.main()
