"""Determine whether line segments can form a non-degenerate polygon."""

from collections.abc import Sequence


def can_form_polygon(lengths: Sequence[float]) -> bool:
    """Return whether all supplied segments can form a polygon.

    For positive segment lengths, a non-degenerate polygon exists exactly when
    the longest segment is shorter than the sum of all remaining segments.
    The input sequence is read but never modified.
    """

    if len(lengths) < 3:
        return False

    total_length = 0.0
    longest_length = 0.0

    for length in lengths:
        if length <= 0:
            return False

        total_length += length

        if length > longest_length:
            longest_length = length

    return longest_length < total_length - longest_length


def main() -> None:
    """Run representative valid and invalid examples."""

    examples = [
        [2, 3, 4],
        [1, 1, 1, 1],
        [2, 3, 4, 5, 6],
        [1, 2, 3],
        [1, 1, 1, 3],
        [0, 2, 3],
        [5, 5],
    ]

    for lengths in examples:
        print(f"{str(lengths):<18} -> {can_form_polygon(lengths)}")


if __name__ == "__main__":
    main()
