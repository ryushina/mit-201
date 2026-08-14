"""Instrument the Chapter 1 crazySort algorithm.

The function deliberately follows the structure of the C algorithm from the
presentation. It sorts the supplied list in place and records the cumulative
number of data-item comparisons and exchanges after each outer-loop pass.
"""


def crazy_sort(items: list[int]):
    """Sort items in place and return operation totals plus a trace.

    A comparison is counted immediately before evaluating items[i] > items[j].
    An exchange is one swap of two array elements.

    Returns:
        A tuple containing num_exchanges, num_comparisons, and a list of trace
        rows. Each row contains the outer index, a snapshot of the list,
        cumulative exchanges, and cumulative comparisons.
    """

    num_exchanges = 0
    num_comparisons = 0
    trace = []

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            # Count the comparison whether its result is True or False.
            num_comparisons += 1

            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
                num_exchanges += 1

        trace.append((i, items.copy(), num_exchanges, num_comparisons))

    return num_exchanges, num_comparisons, trace


def print_trace(trace) -> None:
    """Print the recorded outer-loop results as a readable table."""

    print(f"{'i':<3} {'items':<24} {'exchanges':>10} {'comparisons':>12}")
    print("-" * 53)

    for i, items, exchanges, comparisons in trace:
        print(f"{i:<3} {str(items):<24} {exchanges:>10} {comparisons:>12}")


def main() -> None:
    """Run the exercise using the required input from the presentation."""

    items = [3, 2, 4, 5, 2, 0]
    num_exchanges, num_comparisons, trace = crazy_sort(items)

    print_trace(trace)
    print()
    print(f"Sorted array: {items}")
    print(f"Total exchanges: {num_exchanges}")
    print(f"Total comparisons: {num_comparisons}")


if __name__ == "__main__":
    main()
