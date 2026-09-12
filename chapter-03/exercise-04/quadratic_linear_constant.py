"""Analyze f(n) = 8n^2 + 2000n + 10000 at the exercise input sizes."""

N_VALUES = (1, 10, 50, 100, 150, 200)


def analyze(n: int) -> dict[str, float | int]:
    """Return each term, the total, and each term's percentage share."""
    quadratic = 8 * n**2
    linear = 2000 * n
    constant = 10_000
    total = quadratic + linear + constant
    return {
        "n": n,
        "8n^2": quadratic,
        "2000n": linear,
        "10000": constant,
        "f(n)": total,
        "%8n^2": quadratic / total * 100,
        "%2000n": linear / total * 100,
        "%10000": constant / total * 100,
    }


def main() -> None:
    rows = [analyze(n) for n in N_VALUES]
    assert [row["f(n)"] for row in rows] == [
        12008,
        30800,
        130000,
        290000,
        490000,
        730000,
    ]

    print("n      8n^2      2000n     10000     f(n)       %8n^2  %2000n %10000")
    for row in rows:
        print(
            f'{row["n"]:<6}{row["8n^2"]:<10}{row["2000n"]:<10}'
            f'{row["10000"]:<10}{row["f(n)"]:<11}'
            f'{row["%8n^2"]:>6.2f}% {row["%2000n"]:>6.2f}% {row["%10000"]:>6.2f}%'
        )
    print("At n = 250, 8n^2 and 2000n are equal.")
    print("Asymptotic approximation: 8n^2")
    print("Growth rate: Theta(n^2)")


if __name__ == "__main__":
    main()
