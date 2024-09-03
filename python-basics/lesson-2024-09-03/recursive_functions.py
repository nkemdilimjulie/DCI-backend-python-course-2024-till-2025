
# Recursive Function

'''
def recursive_function(parameters): # Header
    # Base case: Condition to end the recursion
    if base_condition:
        return default_value
    # Recursive case: The function calls itself with a modified argument
    else:
        return recursive_function(modified_parameters)
'''


# Sum up all the numbers until a specific number using recursive function.

# given_number = 10 --> 0 + 1 + 2 + 3,.......+ 10 = 55

# print(sum(range(11))) # 55


def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
    

# print(recursive_sum(30)) # 465

# print(sum(range(31))) # 465

# print(recursive_sum(5))

# print(sum(range(6)))


'''
5 + recursive_sum(4) # first --> Result we are looking for.
    4 + recursive_sum(3) # second
        3 + recursive_sum(2) # third
            2 + recursive_sum(1) # fourth
                1 + recursive_sum(0) # fifth 
                    0 # base case
                1 + 0 = 1 # fifth
            2 + 1 = 3 # fourth
        3 + 3 = 6 # third
    4 + 6 = 10 # second
5 + 10 = 15 # first
'''



# Add all elements from a given list of numbers using recursive function.

numbers = [3, 5, 2, 7] # total: 17


def recursive_addition(lst):
    if lst == []: # len(lst) == 0, not data, not lst
        return 0
    else:
        return lst[0] + recursive_addition(lst[1:])
    

# print(recursive_addition(numbers))

# print(recursive_addition([50, 20, 40]))

'''
3 + recursive_addition([5, 2, 7]) = 17 # Result we are looking for.
    5 + recursive_addition([2, 7]) = 14
        2 + recursive_addition([7]) = 9
            7 + recursive_addition([]) = 7
                0'''

numbers = [3, 5, 2, 7] # total: 17

'''7 + recursive_addition([3, 5, 2]) = 17 # result
    2 + recursive_addition([3, 5]) = 10
        5 + recursive_addition([3]) = 8
            3 + recursive_addition([]) = 3
                0'''



# Reverse a string from a given string using recursive function.

given_text = 'The Last of Us' # --> 'sU fo tsaL ehT' 

def recursive_text(txt):
    if len(txt) == 0:
        return txt
    else:
        return txt[-1] + recursive_text(txt[:-1])
    

# print(recursive_text(given_text))
    


# Reverse a list from a given list using recursive function.

numbers = [3, 5, 2, 7] # --> [7, 2, 5, 3]


def reverse_list(lst):
    if lst == []:
        return lst
    else:
        return [lst[-1]] + reverse_list(lst[:-1])


# print(reverse_list(numbers))



# print(list((3,))) # [3]


# factorial: 3! = 3 * 2 * 1 = 6

# 5! = 5 * 4 * 3 * 2 * 1 = 120


# Create a recusive function to calculate factorial of a number. # Exercise

def factorial(n):




























