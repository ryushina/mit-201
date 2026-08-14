# Chapter 1: Overview of Data Structures and Algorithms

Chapter 1 introduces the relationship among algorithms, data structures, and
implementation. A program must locate or access data, compute a value, and
store the result. Its total running time therefore depends on both computation
and data access.

## Main ideas from the presentation

- An algorithm defines the method and order of the computation.
- A data structure supports efficient reading and writing of the data items.
- A good solution combines a good method, suitable data structures, and a good
  implementation.
- Hardware improvements have physical limits, while software efficiency is
  strongly affected by the nature of the problem and the chosen algorithm.
- Analytical measurement studies time complexity theoretically.
- Empirical measurement instruments a program to count important operations or
  measures its actual execution time.

Exercise 1 applies empirical measurement. The comparison counter is increased
immediately before the data-item comparison. Placing the counter inside the
true branch would miss every comparison whose result is false.

## Completed exercises

| Exercise | Main concept | Python solution |
|---|---|---|
| 1 | Instrument comparisons and exchanges in a sorting algorithm | [crazy_sort.py](exercise-01/crazy_sort.py) |
| 2 | Apply the generalized polygon inequality | [polygon.py](exercise-02/polygon.py) |
| 3 | Minimize operations while validating and classifying a triangle | [triangle.py](exercise-03/triangle.py) |

The README in each exercise folder contains the pseudocode, results, reasoning,
and complexity analysis.
