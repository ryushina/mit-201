# Exercise 2: Testing Whether Segments Can Form a Polygon

## Problem

Given an array containing the lengths of n line segments, determine whether all
the segments can form a non-degenerate polygon, such as a quadrilateral for
n = 4 or a pentagon for n = 5.

## Polygon inequality

Positive line segments can form a polygon exactly when the longest segment is
strictly shorter than the sum of all the other segments:

    longest < total - longest

Only the longest segment needs to be tested. If the longest segment satisfies
the inequality, every shorter segment also satisfies it because all lengths are
positive.

Equality is rejected. If the longest segment equals the sum of all the others,
the segments collapse into a straight line instead of enclosing an area. This
is a degenerate polygon.

## Pseudocode

    CAN-FORM-POLYGON(lengths)
        IF length(lengths) < 3
            RETURN false

        total = 0
        longest = 0

        FOR each length IN lengths
            IF length <= 0
                RETURN false

            total = total + length

            IF length > longest
                longest = length

        RETURN longest < total - longest

The method finds the total and longest length during the same traversal. It
does not sort or modify the input.

## Examples

| Lengths | Result | Reason |
|---|---:|---|
| [2, 3, 4] | True | 4 < 2 + 3 |
| [1, 1, 1, 1] | True | 1 < 1 + 1 + 1 |
| [2, 3, 4, 5, 6] | True | 6 < 2 + 3 + 4 + 5 |
| [1, 2, 3] | False | Equality produces a straight line |
| [1, 1, 1, 3] | False | 3 equals the sum of the other segments |
| [0, 2, 3] | False | A segment cannot have zero length |
| [-1, 2, 3] | False | Lengths must be positive |
| [5, 5] | False | A polygon requires at least three segments |

## Complexity

- Time: O(n), using one traversal
- Auxiliary space: O(1)
- Input modification: none

## Run

    python polygon.py
    python test_polygon.py

From the repository root:

    python chapter-01/exercise-02/polygon.py
    python chapter-01/exercise-02/test_polygon.py
