# Exercise 3: Triangle Validation and Angle Classification

## Problem

Given line-segment lengths x, y, and z, decide whether they can form a triangle.
If they can, classify the triangle as right-angled, obtuse-angled, or
acute-angled while minimizing arithmetic operations and comparisons of data
items.

## Method

Let c be the largest side and let a and b be the other two sides.

The sides form a non-degenerate triangle only when:

    a + b > c

After the validity test, compare the squares:

    a squared + b squared = c squared  means right-angled
    a squared + b squared < c squared  means obtuse-angled
    a squared + b squared > c squared  means acute-angled

The program does not calculate squares for invalid inputs.

## Optimized pseudocode

    CLASSIFY-TRIANGLE(x, y, z)
        IF x <= 0 OR y <= 0 OR z <= 0
            RETURN "not a triangle"

        IF x >= y
            IF x >= z
                a = y, b = z, c = x
            ELSE
                a = x, b = y, c = z
        ELSE
            IF y >= z
                a = x, b = z, c = y
            ELSE
                a = x, b = y, c = z

        smallerSum = a + b

        IF smallerSum <= c
            RETURN "not a triangle"

        smallerSquares = a * a + b * b
        largestSquare = c * c

        IF smallerSquares = largestSquare
            RETURN "right-angled"
        ELSE IF smallerSquares < largestSquare
            RETURN "obtuse-angled"
        ELSE
            RETURN "acute-angled"

## Why this minimizes operations

The two smaller sides do not need to be sorted relative to each other. The
program only needs to identify the largest side, which takes exactly two
side-to-side comparisons instead of fully sorting all three values.

After positive-input validation, the core work is:

| Stage | Operations |
|---|---|
| Identify the largest side | 2 side-to-side comparisons |
| Test the triangle inequality | 1 addition and 1 comparison |
| Calculate squares for a valid triangle | 3 multiplications and 1 addition |
| Classify the angle | 1 or 2 comparisons |

The sum a + b is calculated once. The three squares are calculated only after
the sides pass the triangle inequality, and none of these values is recomputed.
Input validation can require up to three additional comparisons with zero.

## Examples

| Sides | Result |
|---|---|
| (3, 4, 5) | right-angled |
| (5, 3, 4) | right-angled |
| (2, 3, 4) | obtuse-angled |
| (4, 5, 6) | acute-angled |
| (1, 1, 1) | acute-angled |
| (1, 2, 3) | not a triangle |
| (1, 1, 3) | not a triangle |
| (0, 4, 5) | not a triangle |
| (-3, 4, 5) | not a triangle |

## Complexity

The input always contains exactly three lengths:

- Time: O(1)
- Auxiliary space: O(1)

## Run

    python triangle.py
    python test_triangle.py

From the repository root:

    python chapter-01/exercise-03/triangle.py
    python chapter-01/exercise-03/test_triangle.py
