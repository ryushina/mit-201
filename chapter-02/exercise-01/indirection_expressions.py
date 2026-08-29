"""Demonstrate the Python equivalent of reading values through references.

The written answers use C++ dereference syntax such as *xAddr. Python does not
have that operator for ordinary variables; names and container entries already
hold references to objects.
"""

values = {
    "xAddr": 10,
    "yAddr": 20,
    "ptYld": 30,
    "ptMiles": 40.5,
    "mptr": 50,
    "pdate": 2026,
    "distPtr": 60.25,
    "tabPt": "\t",
    "hoursPt": 8,
}


def dereference(reference_name: str):
    """Return the object associated with a simulated reference name."""
    return values[reference_name]


def main() -> None:
    expected = [10, 20, 30, 40.5, 50, 2026, 60.25, "\t", 8]
    actual = [dereference(name) for name in values]
    assert actual == expected

    for name, value in values.items():
        display = "tab character" if value == "\t" else value
        print(f"{name:<8} -> {display}")


if __name__ == "__main__":
    main()
