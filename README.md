## Description
This project compares the execution speed of Python lists and NumPy arrays using 1 million numbers. The goal is to understand performance differences while performing simple mathematical operations.

## Objective
To analyze how NumPy arrays are faster than Python lists for large-scale computations.

## Technologies Used
- Python
- NumPy
- Time module

## Program Overview
The program creates 1 million numbers using both Python lists and NumPy arrays. It multiplies each value by 2 and measures execution time for both methods.

## Observations
1. NumPy arrays execute operations faster than Python lists.
2. Python lists require looping which increases processing time.
3. NumPy uses vectorized operations making it efficient for large datasets.
