# Chapter 3: Asymptotic Analysis

This chapter follows the presentation `Chapter-3-Asymptotic-Analysis`. The
exercise evaluates each function at `n = 1, 10, 50, 100, 150, 200`, compares
the percentage contribution of its terms, and identifies the term that controls
its growth as `n` becomes large.

## Completed exercises

| Exercise | Function | Asymptotic approximation | Growth rate |
|---|---|---|---|
| [1](exercise-01/README.md) | `20n + 200` | `20n` | `Theta(n)` |
| [2](exercise-02/README.md) | `3n^2 + 8n` | `3n^2` | `Theta(n^2)` |
| [3](exercise-03/README.md) | `600 + 30n` | `30n` | `Theta(n)` |
| [4](exercise-04/README.md) | `8n^2 + 2000n + 10000` | `8n^2` | `Theta(n^2)` |

The asymptotic approximation keeps the highest-degree term and drops constant
multipliers only when naming the complexity class. `Theta` gives a tight growth
bound. The same functions are also in `O` and `Omega` of their listed classes.

Exercise 4 illustrates an important distinction. At the supplied values up to
`n = 200`, the linear term `2000n` still has the largest percentage. The
quadratic term equals it at `n = 250` and dominates for larger inputs, so the
asymptotic growth rate is still `Theta(n^2)`.

## Run

```bash
python chapter-03/exercise-01/linear_plus_constant.py
python chapter-03/exercise-02/quadratic_plus_linear.py
python chapter-03/exercise-03/constant_plus_linear.py
python chapter-03/exercise-04/quadratic_linear_constant.py
```
