# Exercise 1: Indirection Expressions

## Required written answers

| Item | Expression |
|---|---|
| Variable pointed to by `xAddr` | `*xAddr` |
| Variable whose address is in `yAddr` | `*yAddr` |
| Variable pointed to by `ptYld` | `*ptYld` |
| Variable pointed to by `ptMiles` | `*ptMiles` |
| Variable pointed to by `mptr` | `*mptr` |
| Variable whose address is in `pdate` | `*pdate` |
| Variable pointed to by `distPtr` | `*distPtr` |
| Variable pointed to by `tabPt` | `*tabPt` |
| Variable whose address is in `hoursPt` | `*hoursPt` |

These are C++ pointer expressions required by the presentation.

## Python implementation

Python variables are object references and do not use a normal dereference
operator. [`indirection_expressions.py`](indirection_expressions.py) stores
the simulated references in a dictionary and accesses each value by its
reference name. Assertions verify all results.
