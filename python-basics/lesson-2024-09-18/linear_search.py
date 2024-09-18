
# Linear Search

num_list = [30, 7, 100, 88, 14, 3, 55, 21] # target = 88


def linear_search(lst, target):

    for i in range(len(lst)):
        if lst[i] == target:
            return i
    
    return -1


# print(linear_search(num_list, 88)) # 3

print(linear_search(num_list, 200)) # -1

# Exercise 1.

# Find the minimum and maximum elements in a list using linear search.

num_list = [30, 7, 100, 88, 14, 3, 55, 21]

# Output:
'''
3, 100

Minimum: 3 and Maximum: 100
'''



