## Friday - 2024-09-13

* How to calculate time complexity of an algorithm
* What approaches we can use for calculating time complexity
* Sorting Algorithm:
    - Bubble sort
* Exercise

## Today - 2024-09-17

* Sorting Algorithms
    - Quick sort
    - Merge sort
* Exercise


### Sorting Algorithms in Python - Quick Sort and Merge Sort

### 1. Quick Sort
**Quick Sort** is a divide-and-conquer algorithm. It works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays: elements less than the pivot and elements greater than the pivot. The process is recursively applied to the sub-arrays until the entire list is sorted.

#### Key Characteristics:
- **Time Complexity**: 
  - Best/Average case: O(n log n)
  - Worst case: O(n²) (when the pivot element is the smallest or largest)
- **Space Complexity**: O(log n) for recursive stack space
- **In-place sorting**: Yes (i.e., does not require additional memory for another array)


#### Algorithm Steps:
1. Choose a pivot element from the list.
2. Partition the array into two sub-arrays based on the pivot.
3. Recursively apply the process to the sub-arrays.
4. Combine the sorted sub-arrays to form the final sorted list.

```python
# Quick sort

num_list = [20, 100, 2, 33, 8, 40, 7, 55, 8, 21]


def quick_sort(lst):

    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[len(lst) // 2]

        left_lst = [x for x in lst if x < pivot]
        right_lst = [x for x in lst if x > pivot]
        middle_lst = [x for x in lst if x == pivot]

        return quick_sort(left_lst) + middle_lst + quick_sort(right_lst)


print(f'Original list: {num_list}')
print(f'Sorted list: {quick_sort(num_list)}')
```

### 2. Merge Sort
**Merge Sort** is another divide-and-conquer algorithm. It divides the array into two halves, recursively sorts them, and then merges the two sorted halves.

#### Key Characteristics:
- **Time Complexity**: 
  - Best/Average/Worst case: O(n log n)
- **Space Complexity**: O(n) (due to the use of auxiliary arrays during merging)
- **Stable sorting**: Yes (preserves the relative order of equal elements)

#### Algorithm Steps:
1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the two halves together by comparing elements from both halves and inserting them into a new sorted list.

```python
# Merge sort

num_list = [300, 7, 55, 220, 4, 77, 12, 2, 444, 88]

def merge_sort(lst):

    if len(lst) <= 1:
        return lst
    
    mid_idx = len(lst) // 2

    left_lst = lst[:mid_idx]
    right_lst = lst[mid_idx:]

    left = merge_sort(left_lst)
    right = merge_sort(right_lst)

    return merge(left, right)


def merge(left, right):

    i = 0
    j = 0

    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


print(f'Original list: {num_list}')
print(f'Sorted list: {merge_sort(num_list)}')
```


### Comparison of Quick Sort and Merge Sort

| Criteria             | Quick Sort                        | Merge Sort                        |
|----------------------|-----------------------------------|-----------------------------------|
| Time Complexity       | O(n log n) (Best & Average), O(n²) (Worst) | O(n log n) (all cases)            |
| Space Complexity      | O(log n) (in-place)              | O(n) (requires additional space)  |
| Stability             | Unstable                         | Stable                            |
| Usage                 | Generally faster in practice, especially for arrays | Preferred when stability is required, and when space isn’t an issue |
