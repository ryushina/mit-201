# Exercise 2: Quadratic and Linear Terms

## Problem

Evaluate `f(n) = 3n^2 + 8n` for `n = 1, 10, 50, 100, 150, 200` and determine
its asymptotic complexity or growth rate.

## Evaluated values

| n | 3n^2 | 8n | f(n) |
|---:|---:|---:|---:|
| 1 | 3 | 8 | 11 |
| 10 | 300 | 80 | 380 |
| 50 | 7,500 | 400 | 7,900 |
| 100 | 30,000 | 800 | 30,800 |
| 150 | 67,500 | 1,200 | 68,700 |
| 200 | 120,000 | 1,600 | 121,600 |

## Percentage contribution

| n | 3n^2 | 8n |
|---:|---:|---:|
| 1 | 27.27% | 72.73% |
| 10 | 78.95% | 21.05% |
| 50 | 94.94% | 5.06% |
| 100 | 97.40% | 2.60% |
| 150 | 98.25% | 1.75% |
| 200 | 98.68% | 1.32% |

## Asymptotic analysis

The quadratic term quickly approaches the entire value of the function. The
linear term becomes negligible by comparison.

- Asymptotic approximation: `3n^2`
- Growth rate: `Theta(n^2)`

## Python implementation

[`quadratic_plus_linear.py`](quadratic_plus_linear.py) calculates every value
and percentage, verifies the totals, and prints the result.
