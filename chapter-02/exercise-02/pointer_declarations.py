"""Show Python references corresponding to the presentation's C++ pointers."""


def main() -> None:
    # Python variables do not need typed pointer declarations.
    y_addr = 1
    ch_addr = "A"
    pt_yr = 2026
    amt = 125.50
    z = 25
    qp = 3.5
    date_pt = 29
    yld_addr = 8.75

    references = {
        "yAddr": y_addr,
        "chAddr": ch_addr,
        "ptYr": pt_yr,
        "amt": amt,
        "z": z,
        "qp": qp,
        "datePt": date_pt,
        "yldAddr": yld_addr,
    }

    assert isinstance(references["yAddr"], int)
    assert isinstance(references["chAddr"], str)
    assert isinstance(references["ptYr"], int)
    assert isinstance(references["amt"], float)
    assert isinstance(references["z"], int)
    assert isinstance(references["qp"], float)
    assert isinstance(references["datePt"], int)
    assert isinstance(references["yldAddr"], float)

    for name, value in references.items():
        print(f"{name:<8} -> {value!r}")


if __name__ == "__main__":
    main()
