# Permutation & Combinatorics Toolkit

This Python project provides tools for exploring permutations and elementary combinatorics. It includes:

- Inversion Set Calculator
- h-Inversion Set Calculator (inversions within sliding windows)
- Combinatorics Problem Generator (for practice and testing)

---

## Requirements

- Python 3.7+

---

## Inversion Set Calculator

Calculates the number of permutations with a given inversion set, defined as a set of pairs (i, j) in a permutation such that i < j and π(i) > π(j).

### Usage:
$ python inversion.py
Enter the value of n (length of permutation): 5
Enter the inversion set: [(1,2), (3,4)]
Number of permutations with the given inversion set: 1

---

## h-Inversion Set Calculator

Finds the number of permutations with the given h-inversion set, defined as a set of pairs (i, j) where i < j ≤ i + h(i) and π(i) > π(j). Here, h is a Hessenberg Function. It also calculates the number of such permutations using the h-inversion polynomial from my combinatorics research project. 

### Usage:
$ python h_inversion.py
Enter the value of n (length of permutation): 5
Enter the inversion set: [(1,2), (3,4)]
(2, 1, 4, 3, 5)
(3, 1, 4, 2, 5)
Number of permutations with the given inversion set: 2
With Polynomial: 2

---

## Combinatorics Problem Generator

Generates random problems such as:

- Counting permutations and combinations
- Derangement counts
- Inclusion-exclusion challenges

### Example output:
How many ways can you choose 3 people out of 7?
Answer: 35

How many derangements of 4 elements exist?
Answer: 9