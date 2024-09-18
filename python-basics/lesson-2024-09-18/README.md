## Yesterday - 2024-09-17

* Sorting Algorithms
    - Quick sort
    - Merge sort
* Exercise


## Today - 2024-09-18

* Searching Algorithms
    - Linear search
    - Binary search
* Exercise


### Searching Algorithms in Python - Linear Search and Binary Search

Searching algorithms are crucial when working with data, as they allow you to efficiently retrieve information. In this lesson, we'll explore two basic searching algorithms: **Linear Search** and **Binary Search**.

### 1. Linear Search
**Linear Search** is a simple algorithm that checks each element in a list sequentially until it finds the target value or reaches the end of the list.

#### Key Characteristics:
- **Time Complexity**: O(n), where `n` is the number of elements in the list (worst-case scenario, it searches through the entire list).
- **Space Complexity**: O(1), as it requires a constant amount of memory.
- **Use Case**: Works on both sorted and unsorted lists.

#### Algorithm Steps:
1. Start from the first element of the list.
2. Compare the current element with the target value.
3. If they match, return the index of the element.
4. If not, move to the next element and repeat the process.
5. If the target is not found by the end of the list, return -1 (or another indication that the element is not present).

```python
# Linear Search

num_list = [30, 7, 100, 88, 14, 3, 55, 21] # target = 88


def linear_search(lst, target):

    for i in range(len(lst)):
        if lst[i] == target:
            return i
    
    return -1


# print(linear_search(num_list, 88)) # 3

print(linear_search(num_list, 200)) # -1
```

### 2. Binary Search
**Binary Search** is a more efficient algorithm that works on **sorted arrays**. It repeatedly divides the search space in half, narrowing down the location of the target.

#### Key Characteristics:
- **Time Complexity**: O(log n), where `n` is the number of elements in the list (due to halving the search space).
- **Space Complexity**: O(1) (for iterative versions) or O(log n) (for recursive versions due to call stack).
- **Use Case**: Requires the list to be sorted in ascending or descending order.

#### Algorithm Steps:
1. Start with two pointers: `low` (beginning of the list) and `high` (end of the list).
2. Find the middle element of the current range.
3. If the middle element matches the target, return its index.
4. If the target is less than the middle element, repeat the search in the lower half (left of the middle).
5. If the target is greater than the middle element, repeat the search in the upper half (right of the middle).
6. If the search space becomes invalid (low > high), return -1 (or another indication that the element is not present).


```python
# Binary Search

num_list = [10, 20, 30, 40, 50, 60, 60, 70, 70, 80, 90, 100] # target = 30

def binary_search(lst, target):   
    low = 0 
    high = len(lst) - 1 
    while low <= high:
        mid = (low + high) // 2  

        if lst[mid] == target:
            return mid
        elif lst[mid] < target: 
            low = mid + 1
        else:
            high = mid - 1 
    
    return -1

print(binary_search(num_list, 70))
```