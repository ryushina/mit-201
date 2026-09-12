# Exercise 4: Quadratic Linear and Constant Terms

## Problem

Evaluate `f(n) = 8n^2 + 2000n + 10000` for
`n = 1, 10, 50, 100, 150, 200` and determine its asymptotic complexity or
growth rate.

## Evaluated values

| n | 8n^2 | 2000n | 10000 | f(n) |
|---:|---:|---:|---:|---:|
| 1 | 8 | 2,000 | 10,000 | 12,008 |
| 10 | 800 | 20,000 | 10,000 | 30,800 |
| 50 | 20,000 | 100,000 | 10,000 | 130,000 |
| 100 | 80,000 | 200,000 | 10,000 | 290,000 |
| 150 | 180,000 | 300,000 | 10,000 | 490,000 |
| 200 | 320,000 | 400,000 | 10,000 | 730,000 |

## Percentage contribution

| n | 8n^2 | 2000n | 10000 |
|---:|---:|---:|---:|
| 1 | 0.07% | 16.66% | 83.28% |
| 10 | 2.60% | 64.94% | 32.47% |
| 50 | 15.38% | 76.92% | 7.69% |
| 100 | 27.59% | 68.97% | 3.45% |
| 150 | 36.73% | 61.22% | 2.04% |
| 200 | 43.84% | 54.79% | 1.37% |

## Asymptotic analysis

The supplied values stop before the quadratic term overtakes the linear term.
Solving `8n^2 = 2000n` gives `n = 250`, so the two terms are equal there and
`8n^2` becomes larger for `n > 250`. Asymptotic analysis considers what happens
as `n` continues to increase, which makes the highest-degree term decisive.

- Asymptotic approximation: `8n^2`
- Growth rate: `Theta(n^2)`

## Python implementation

[`quadratic_linear_constant.py`](quadratic_linear_constant.py) calculates every
value and percentage, verifies the totals, identifies the crossover, and prints
the result.
