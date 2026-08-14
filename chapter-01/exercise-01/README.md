# Exercise 1: Instrumented Crazy Sort

## Problem

Instrument the supplied crazySort algorithm to count:

- numExchanges: the number of array-element exchanges
- numComparisons: the number of comparisons between array data items

Show the cumulative values after each outer-loop iteration for:

    [3, 2, 4, 5, 2, 0]

The original code compares items[i] with every item to its right. Whenever it
finds a smaller value, it exchanges that value with items[i] immediately.

## Instrumentation rule

The counter is increased before evaluating the condition:

    num_comparisons += 1
    if items[i] > items[j]:
        items[i], items[j] = items[j], items[i]
        num_exchanges += 1

This counts the comparison regardless of whether the condition is true or
false. One swap counts as one exchange, even though the original C code uses
three assignments to perform it.

## Pseudocode

    CRAZY-SORT(items)
        numExchanges = 0
        numComparisons = 0

        FOR i = 0 TO length(items) - 1
            FOR j = i + 1 TO length(items) - 1
                numComparisons = numComparisons + 1

                IF items[i] > items[j]
                    EXCHANGE items[i] AND items[j]
                    numExchanges = numExchanges + 1

            OUTPUT i, items, numExchanges, numComparisons

## Required trace

| Outer index i | Array after the iteration | numExchanges | numComparisons |
|---:|---|---:|---:|
| 0 | [0, 3, 4, 5, 2, 2] | 2 | 5 |
| 1 | [0, 2, 4, 5, 3, 2] | 3 | 9 |
| 2 | [0, 2, 2, 5, 4, 3] | 5 | 12 |
| 3 | [0, 2, 2, 3, 5, 4] | 7 | 14 |
| 4 | [0, 2, 2, 3, 4, 5] | 8 | 15 |
| 5 | [0, 2, 2, 3, 4, 5] | 8 | 15 |

Final result:

    Sorted array: [0, 2, 2, 3, 4, 5]
    Total exchanges: 8
    Total comparisons: 15

For six items, the inner loops always perform:

    5 + 4 + 3 + 2 + 1 + 0 = 15 comparisons

In general, the algorithm performs n(n - 1) / 2 data-item comparisons.

## Question A

### Would i < numItems - 1 produce the same result?

Yes. When i equals numItems - 1, j starts at numItems, so the inner loop has no
iterations. The final array element is already in its correct position.
Removing that empty outer iteration does not change the sorted array, number of
data-item comparisons, or number of exchanges.

It removes one outer-loop iteration and a small amount of loop-control
overhead, so it can be marginally faster. The improvement is constant and does
not change the quadratic time complexity.

## Question B

### Is the algorithm closer to insertion sort or selection sort?

It is closer to selection sort and is commonly described as exchange sort or
interchange sort.

Both this algorithm and selection sort use position i for the next smallest
item and examine the unsorted portion to its right. The difference is how they
exchange values:

- Standard selection sort remembers the position of the smallest remaining
  item and normally performs one exchange after the search.
- This algorithm exchanges immediately every time it finds a value smaller
  than items[i], so it may perform several exchanges during one outer pass.
- Insertion sort instead takes one item and inserts it into the already sorted
  left portion, commonly by shifting larger values.

## Complexity

- Data-item comparisons: exactly n(n - 1) / 2
- Running time: Theta(n squared) in the best, average, and worst cases
- Exchanges: input-dependent; zero for sorted input and as many as
  n(n - 1) / 2
- Core sorting space: O(1) auxiliary space
- Recorded trace space in this implementation: O(n squared), because it saves
  one complete list snapshot after each outer iteration

## Run

    python crazy_sort.py
    python test_crazy_sort.py

From the repository root:

    python chapter-01/exercise-01/crazy_sort.py
    python chapter-01/exercise-01/test_crazy_sort.py
