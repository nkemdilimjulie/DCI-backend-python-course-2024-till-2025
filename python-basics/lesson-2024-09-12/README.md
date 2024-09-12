## Today - 2024-09-11
   
* What is an algorithm?
* What is algorithmic thinking?
* Algorithms in computer programming 
* Typical algorithms
* Pseudo code


## Today - 2024-09-12

* Algorithmic Analysis
    - Big-O-notation
    - Self study


## Algorithmic Analysis: O-Notation

### 1. **Introduction to Algorithmic Analysis**

Algorithmic analysis is essential in computer science to determine the efficiency of an algorithm, particularly in terms of time and space complexity. One of the most common methods of expressing an algorithm's efficiency is through **Big O notation**, which provides an upper bound on the time or space complexity as the size of the input grows.


### 2. **What is Big O Notation?**

Big O notation describes how the runtime or space requirements of an algorithm grow as the input size increases. It focuses on the worst-case scenario and ignores constant factors or less dominant terms, giving a simplified view of the algorithm’s behavior for large inputs.


### 3. **Common Big O Notations**

Here are the most commonly used notations:

- **O(1)**: Constant time - The algorithm’s runtime does not depend on the input size.

- **O(log n)**: Logarithmic time - The runtime grows logarithmically as the input size increases.

- **O(n)**: Linear time - The runtime grows linearly with the size of the input.

- **O(n log n)**: Log-linear time - Common in efficient sorting algorithms like mergesort.

- **O(n^2)**: Quadratic time - Often occurs with nested loops.

- **O(2^n)**: Exponential time - Occurs in algorithms that solve problems by brute-force approaches, such as recursive algorithms solving the traveling salesman problem.


### 4. **Why is Big O Important?**

- **Predict Performance:** Big O helps developers predict how an algorithm will scale with larger input sizes.
- **Optimize Code:** By understanding the time complexity, you can choose or design algorithms that perform efficiently for your use case.
- **Comparing Algorithms:** Big O allows you to compare the efficiency of different algorithms for the same problem.









































































































