# Exercise 3: Constant and Linear Terms

## Problem

Evaluate `f(n) = 600 + 30n` for `n = 1, 10, 50, 100, 150, 200` and determine
its asymptotic complexity or growth rate.

## Evaluated values

| n | 600 | 30n | f(n) |
|---:|---:|---:|---:|
| 1 | 600 | 30 | 630 |
| 10 | 600 | 300 | 900 |
| 50 | 600 | 1,500 | 2,100 |
| 100 | 600 | 3,000 | 3,600 |
| 150 | 600 | 4,500 | 5,100 |
| 200 | 600 | 6,000 | 6,600 |

## Percentage contribution

| n | 600 | 30n |
|---:|---:|---:|
| 1 | 95.24% | 4.76% |
| 10 | 66.67% | 33.33% |
| 50 | 28.57% | 71.43% |
| 100 | 16.67% | 83.33% |
| 150 | 11.76% | 88.24% |
| 200 | 9.09% | 90.91% |

## Asymptotic analysis

The constant dominates only for small inputs. Its percentage falls toward zero
while the linear term controls the long-run growth.

- Asymptotic approximation: `30n`
- Growth rate: `Theta(n)`

## Python implementation

[`constant_plus_linear.py`](constant_plus_linear.py) calculates every value and
percentage, verifies the totals, and prints the result.
