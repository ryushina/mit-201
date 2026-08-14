"""Classify a triangle while avoiding unnecessary operations."""

NOT_A_TRIANGLE = "not a triangle"
RIGHT_ANGLED = "right-angled"
OBTUSE_ANGLED = "obtuse-angled"
ACUTE_ANGLED = "acute-angled"


def arrange_with_largest_last(
    x: float, y: float, z: float
) -> tuple[float, float, float]:
    """Return two smaller sides followed by the largest side.

    Only two side-to-side comparisons are needed. The order of the two
    smaller sides is irrelevant to both the triangle inequality and the
    angle classification.
    """

    if x >= y:
        if x >= z:
            return y, z, x
        return x, y, z

    if y >= z:
        return x, z, y
    return x, y, z


def classify_triangle(x: float, y: float, z: float) -> str:
    """Return the triangle type formed by x, y, and z."""

    if x <= 0 or y <= 0 or z <= 0:
        return NOT_A_TRIANGLE

    a, b, c = arrange_with_largest_last(x, y, z)

    smaller_sum = a + b
    if smaller_sum <= c:
        return NOT_A_TRIANGLE

    smaller_squares = a * a + b * b
    largest_square = c * c

    if smaller_squares == largest_square:
        return RIGHT_ANGLED
    if smaller_squares < largest_square:
        return OBTUSE_ANGLED
    return ACUTE_ANGLED


def main() -> None:
    """Run representative classifications."""

    examples = [
        (3, 4, 5),
        (5, 3, 4),
        (2, 3, 4),
        (4, 5, 6),
        (1, 1, 1),
        (1, 2, 3),
        (0, 4, 5),
    ]

    for sides in examples:
        result = classify_triangle(*sides)
        print(f"{str(sides):<12} -> {result}")


if __name__ == "__main__":
    main()
