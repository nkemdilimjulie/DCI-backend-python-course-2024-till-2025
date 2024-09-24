# algorithmic-thinking-time-complexity
'''
Analyze the time complexity for the following Python code:
'''
################################################################################

# TASK 1 #######################################################################

def find_max(arr):
    max_value = arr[0]      # --> O(1)
    for i in arr:           # --> O(n)
        if i > max_value:   # --> O(1)
            max_value = i   # --> O(1) 
    return max_value            

# time complexity is O(n)

# TASK 2 #######################################################################

def calculate_sum(arr):
    total = 0               # --> O(1)
    for num in arr:         # --> O(n)
        total += num        # --> O(1) 
    return total

# time complexity is O(n)

# TASK 3 #######################################################################

def nested_loops(arr):
    for i in arr:           # --> O(n)
        for j in arr:       # --> O(n*n) --> O(n²)
            print(i, j)     # --> O(1) 

# time complexity is O(n²)


# TASK 4 #######################################################################

def is_sorted(arr):
    for i in range(1, len(arr)):    # --> O(n)
        if arr[i] < arr[i-1]:       # --> O(1)
            return False
    return True

# time complexity is O(n)


# TASK 5 #######################################################################

def generate_pairs(arr):
    pairs = []                              # --> O(1)
    for i in range(len(arr)):               # --> O(n)
        for j in range(i+1, len(arr)):      # --> O(n*n) --> O(n²)
            pairs.append((arr[i], arr[j]))  # --> O(1)
    return pairs

# time complexity is O(n²)

# TASK 6 #######################################################################

def recursive_sum(n):
    if n == 0:                      # --> O(1)
        return 0
    return n + recursive_sum(n - 1) # --> O(1) --> recursion ~> O(n)

# time complexity is O(n)

# TASK 7 #######################################################################

def remove_duplicates(arr):
    unique_elements = []                # --> O(1)
    for num in arr:                     # --> O(n)
        if num not in unique_elements:  
            unique_elements.append(num) # --> O(n*(n-1)/2) --> O(n²)
            print(unique_elements)
    return unique_elements

# time complexity is O(n²). Running through arr and unique_elements, comparing both lists, unique can be (nearly) as long as arr.
# Note:
# Task 7 is often considered as O(n²) complexity because of the if statement checking whether an element is already existing in the appended list and that list can be quite big if the input size is big enough.

# TASK 8 #######################################################################

x = 1               
while x < n:        
    x = x * 10      # logarithmic growth

# While loops with logarithmic growth
# time complexity is O(log n)

