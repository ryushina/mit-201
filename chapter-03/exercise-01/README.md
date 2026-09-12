# Exercise 1: Linear Term and Constant

## Problem

Evaluate `f(n) = 20n + 200` for `n = 1, 10, 50, 100, 150, 200` and determine
its asymptotic complexity or growth rate.

## Evaluated values

| n | 20n | 200 | f(n) |
|---:|---:|---:|---:|
| 1 | 20 | 200 | 220 |
| 10 | 200 | 200 | 400 |
| 50 | 1,000 | 200 | 1,200 |
| 100 | 2,000 | 200 | 2,200 |
| 150 | 3,000 | 200 | 3,200 |
| 200 | 4,000 | 200 | 4,200 |

## Percentage contribution

| n | 20n | 200 |
|---:|---:|---:|
| 1 | 9.09% | 90.91% |
| 10 | 50.00% | 50.00% |
| 50 | 83.33% | 16.67% |
| 100 | 90.91% | 9.09% |
| 150 | 93.75% | 6.25% |
| 200 | 95.24% | 4.76% |

## Asymptotic analysis

The constant contributes a smaller percentage as `n` increases. The linear
term controls the long-run growth.

- Asymptotic approximation: `20n`
- Growth rate: `Theta(n)`

## Python implementation

[`linear_plus_constant.py`](linear_plus_constant.py) calculates every value and
percentage, verifies the required totals with assertions, and prints the result.
