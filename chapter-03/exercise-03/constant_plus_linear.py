"""Analyze f(n) = 600 + 30n at the input sizes from the exercise."""

N_VALUES = (1, 10, 50, 100, 150, 200)


def analyze(n: int) -> dict[str, float | int]:
    """Return each term, the total, and each term's percentage share."""
    constant = 600
    linear = 30 * n
    total = constant + linear
    return {
        "n": n,
        "600": constant,
        "30n": linear,
        "f(n)": total,
        "%600": constant / total * 100,
        "%30n": linear / total * 100,
    }


def main() -> None:
    rows = [analyze(n) for n in N_VALUES]
    assert [row["f(n)"] for row in rows] == [630, 900, 2100, 3600, 5100, 6600]

    print("n      600     30n      f(n)    %600    %30n")
    for row in rows:
        print(
            f'{row["n"]:<6}{row["600"]:<8}{row["30n"]:<9}'
            f'{row["f(n)"]:<8}{row["%600"]:>6.2f}% {row["%30n"]:>6.2f}%'
        )
    print("Asymptotic approximation: 30n")
    print("Growth rate: Theta(n)")


if __name__ == "__main__":
    main()
