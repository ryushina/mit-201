"""Analyze f(n) = 3n^2 + 8n at the input sizes from the exercise."""

N_VALUES = (1, 10, 50, 100, 150, 200)


def analyze(n: int) -> dict[str, float | int]:
    """Return each term, the total, and each term's percentage share."""
    quadratic = 3 * n**2
    linear = 8 * n
    total = quadratic + linear
    return {
        "n": n,
        "3n^2": quadratic,
        "8n": linear,
        "f(n)": total,
        "%3n^2": quadratic / total * 100,
        "%8n": linear / total * 100,
    }


def main() -> None:
    rows = [analyze(n) for n in N_VALUES]
    assert [row["f(n)"] for row in rows] == [11, 380, 7900, 30800, 68700, 121600]

    print("n      3n^2      8n       f(n)      %3n^2   %8n")
    for row in rows:
        print(
            f'{row["n"]:<6}{row["3n^2"]:<10}{row["8n"]:<9}'
            f'{row["f(n)"]:<10}{row["%3n^2"]:>6.2f}% {row["%8n"]:>6.2f}%'
        )
    print("Asymptotic approximation: 3n^2")
    print("Growth rate: Theta(n^2)")


if __name__ == "__main__":
    main()
