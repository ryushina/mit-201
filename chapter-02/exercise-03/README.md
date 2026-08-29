# Exercise 3: Pointer and Address Trace

## Statements and results

The statements are applied in order to the presentation's illustrated memory.

| Statement | Data written or read |
|---|---|
| `ptNum = &m;` | `ptNum` stores `8096`, the illustrated address of `m` |
| `amtAddr = &amt;` | `amtAddr` stores `16256`, the address of `amt` |
| `*zAddr = 25;` | `slope` becomes `25` because `zAddr` stores `20492` |
| `k = *numAddr;` | `k` becomes `154` because address `18938` contains `firstnum` |
| `ptDay = zAddr;` | `ptDay` stores `20492` |
| `*ptYr = 1987;` | `years` becomes `1987` because `ptYr` stores `694` |
| `*amtAddr = *numAddr;` | `amt` becomes `154` |

## Python implementation

[`pointer_address_trace.py`](pointer_address_trace.py) represents memory as a
dictionary whose keys are the illustrated addresses. A second dictionary stores
the pointer values. This preserves the pointer relationships without claiming
that Python provides C++-style raw pointers.

Final values: `ptNum = 8096`, `amtAddr = 16256`, `ptDay = 20492`,
`years = 1987`, `amt = 154`, `slope = 25`, and `k = 154`.
