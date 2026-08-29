# Exercise 1: Indirection Expressions

## Problem

Using the indirection operator, write expressions for the variables pointed to
by `xAddr`, `yAddr`, `ptYld`, `ptMiles`, `mptr`, `pdate`, `distPtr`,
`tabPt`, and `hoursPt`.

## Answers

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

The `*` operator dereferences a pointer and accesses the value stored at the
address contained in that pointer.

## Source

[`indirection_expressions.cpp`](indirection_expressions.cpp) declares suitable
variables and pointers, dereferences each pointer, and verifies the result with
assertions.
