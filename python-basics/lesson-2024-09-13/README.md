## Yesterday - 2024-09-12

* Algorithmic Analysis
    - Big-O-notation
    - Self study


## Today - 2024-09-13

* How to calculate time complexity of an algorithm
* What approaches we can use for calculating time complexity
* Sorting Algorithm:
    - Bubble sort
* Exercise

### 1. **Introduction to Time Complexity**

Time complexity is a measure of how the runtime of an algorithm increases as the size of the input grows. It gives us an understanding of how scalable an algorithm is and helps us compare the efficiency of different algorithms. Calculating the time complexity of an algorithm involves analyzing the number of operations the algorithm performs relative to the size of its input.

### 2. **Steps to Calculate Time Complexity**

Here’s a general approach to calculating time complexity for most algorithms:

#### Step 1: **Identify the input size**
- Let the size of the input be represented by `n`.

- The input size is the primary factor that influences the runtime. In most problems, this refers to the number of elements in an array or the length of a string.

#### Step 2: **Count the number of basic operations**
- Basic operations are the most frequent, non-trivial operations executed by the algorithm, such as comparisons, arithmetic operations, or array accesses.
- Focus on the loops and recursive calls, as these contribute significantly to the number of operations.

#### Step 3: **Determine the growth of operations**
- Analyze how the number of operations grows as the input size increases.
- For each loop or recursion, understand how the number of iterations is related to `n`.

#### Step 4: **Simplify the expression**
- Only the most significant term is kept in Big O notation (e.g., O(n^2), O(n log n)). Disregard constants and less dominant terms.

### 1. **Sorting Algorithms**

Sorting algorithms are essential for organizing data in a specific order. Sorting can be done in various ways, and different sorting algorithms have different time complexities and use cases. The objective of a sorting algorithm is to rearrange a list or array of items in ascending or descending order based on comparison operations.

### 2. **What is Bubble Sort?**

**Bubble Sort** is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The algorithm continues to pass through the list until it is sorted.














































































































































































