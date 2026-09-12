"""Analyze f(n) = 20n + 200 at the input sizes from the exercise."""

N_VALUES = (1, 10, 50, 100, 150, 200)


def analyze(n: int) -> dict[str, float | int]:
    """Return each term, the total, and each term's percentage share."""
    linear = 20 * n
    constant = 200
    total = linear + constant
    return {
        "n": n,
        "20n": linear,
        "200": constant,
        "f(n)": total,
        "%20n": linear / total * 100,
        "%200": constant / total * 100,
    }


def main() -> None:
    rows = [analyze(n) for n in N_VALUES]
    assert [row["f(n)"] for row in rows] == [220, 400, 1200, 2200, 3200, 4200]

    print("n      20n     200     f(n)    %20n    %200")
    for row in rows:
        print(
            f'{row["n"]:<6}{row["20n"]:<8}{row["200"]:<8}'
            f'{row["f(n)"]:<8}{row["%20n"]:>6.2f}% {row["%200"]:>6.2f}%'
        )
    print("Asymptotic approximation: 20n")
    print("Growth rate: Theta(n)")


if __name__ == "__main__":
    main()
