# Exercise 3: Pointer and Address Trace

## Initial memory diagram

| Variable | Address | Initial data |
|---|---:|---:|
| `ptNum` | 500 | blank |
| `amtAddr` | 564 | blank |
| `zAddr` | 8024 | 20492 |
| `numAddr` | 10132 | 18938 |
| `ptDay` | 14862 | blank |
| `ptYr` | 15010 | 694 |
| `years` | 694 | blank |
| `m` | 8096 | blank |
| `amt` | 16256 | blank |
| `firstnum` | 18938 | 154 |
| `slope` | 20492 | blank |
| `k` | 24608 | blank |

## Statements and results

The statements are applied in order.

| Statement | Data written or read |
|---|---|
| `ptNum = &m;` | `ptNum` stores `8096`, the illustrated address of `m` |
| `amtAddr = &amt;` | `amtAddr` stores `16256`, the address of `amt` |
| `*zAddr = 25;` | `slope` becomes `25` because `zAddr` stores `20492` |
| `k = *numAddr;` | `k` becomes `154` because address `18938` contains `firstnum` |
| `ptDay = zAddr;` | `ptDay` stores `20492` |
| `*ptYr = 1987;` | `years` becomes `1987` because `ptYr` stores `694` |
| `*amtAddr = *numAddr;` | `amt` becomes `154` |

## Final data

`ptNum = 8096`, `amtAddr = 16256`, `zAddr = 20492`, `numAddr = 18938`,
`ptDay = 20492`, `ptYr = 694`, `years = 1987`, `amt = 154`, `firstnum = 154`,
`slope = 25`, and `k = 154`.

The numerical addresses above come from the presentation's illustration. A
real C++ program receives actual addresses from the runtime, so the source code
also prints the conceptual illustrated address values separately.
