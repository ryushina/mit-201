"""Simulate the presentation's pointer-and-address memory diagram in Python."""

ADDRESSES = {
    "ptNum": 500,
    "amtAddr": 564,
    "zAddr": 8024,
    "numAddr": 10132,
    "ptDay": 14862,
    "ptYr": 15010,
    "years": 694,
    "m": 8096,
    "amt": 16256,
    "firstnum": 18938,
    "slope": 20492,
    "k": 24608,
}


def run_trace() -> tuple[dict[int, int | None], dict[str, int]]:
    """Apply the seven statements using dictionaries as simulated memory."""
    memory: dict[int, int | None] = {
        694: None,
        8096: None,
        16256: None,
        18938: 154,
        20492: None,
        24608: None,
    }
    pointers = {
        "ptNum": 0,
        "amtAddr": 0,
        "zAddr": 20492,
        "numAddr": 18938,
        "ptDay": 0,
        "ptYr": 694,
    }

    pointers["ptNum"] = ADDRESSES["m"]
    pointers["amtAddr"] = ADDRESSES["amt"]
    memory[pointers["zAddr"]] = 25
    memory[ADDRESSES["k"]] = memory[pointers["numAddr"]]
    pointers["ptDay"] = pointers["zAddr"]
    memory[pointers["ptYr"]] = 1987
    memory[pointers["amtAddr"]] = memory[pointers["numAddr"]]

    return memory, pointers


def main() -> None:
    memory, pointers = run_trace()

    assert pointers["ptNum"] == 8096
    assert pointers["amtAddr"] == 16256
    assert pointers["ptDay"] == 20492
    assert memory[694] == 1987
    assert memory[16256] == 154
    assert memory[20492] == 25
    assert memory[24608] == 154

    final_data = {
        **pointers,
        "years": memory[694],
        "m": memory[8096],
        "amt": memory[16256],
        "firstnum": memory[18938],
        "slope": memory[20492],
        "k": memory[24608],
    }
    for name, value in final_data.items():
        print(f"{name:<9} = {value}")


if __name__ == "__main__":
    main()
