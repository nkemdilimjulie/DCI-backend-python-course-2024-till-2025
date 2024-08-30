
# Creating lambda function


def addition(a, b):
    return a + b

# print(addition(20, 30))

add_lambda = lambda a, b: a + b

# print(add_lambda(70, 30))

def maxim(x, y):
    if x > y:
        return x
    else:
        return y


maximum = lambda x, y: x if x > y else y

# print(maxim(2, 200))

# print(maximum(3, 300))


# Find the square of a number


square_num = lambda n: n ** 2

# print(square_num(20))


# Concatenate two strings together

'Hello', 'Daniel'

'Hello Daniel'

concate = lambda str1, str2: str1 + ' ' + str2 

concate = lambda str1, str2: f'{str1} {str2}'

# print(concate('Hello', 'Daniel'))



# Find if a number is even


# even_num = lambda x: if x % 2 == 0: True: else False # Syntax error


even_num = lambda x: True if x % 2 == 0 else False

# print(even_num(40)) # True

# print(even_num(1543)) # False


# Find if a number is odd --> Exercise 1



# Reverse a string

# 'Arithmatic' --> 'citamhtirA'


# str_reverse = lambda str1, str2: str2.sort(str1, reverse=True)

# str_reverse = lambda x: sorted(x, reverse=True)

# Output: ['t', 't', 'r', 'm', 'i', 'i', 'h', 'c', 'a', 'A']


# print(str_reverse('Arithmatic', 'Amazon')) # taking 2 arguments

# print(str_reverse('Arithmatic'))

# Output: ['t', 't', 'r', 'm', 'i', 'i', 'h', 'c', 'a', 'A']


# Create a lambda function that will take the first character from a string and place it at the end. # Exercise 2


text_reverse = lambda t: t[::-1]

# print(text_reverse('Arithmatic'))


# lambda function with map


numbers = [1, 2, 3, 4, 5]

# create a lambda function that multiplies any number by 10.

x = lambda y: y*10

mult_ten = lambda n: n*10

# print(mult_ten(8)) # 80

# create a lambda function that multiplies any number by 180. # Exercie 3


# --> [10, 20, 30, 40, 50]

numbers = [1, 2, 3, 4, 5] # --> [10, 20, 30, 40, 50]

empty_list = []

for num in numbers:
    new_val = num * 10
    empty_list.append(new_val)

# print(empty_list)



numbers = [1, 2, 3, 4, 5] # --> [10, 20, 30, 40, 50]

mult_ten = lambda n: n*10

new_numbers = map(mult_ten, numbers)

new_numbers_list = list(new_numbers)

# print(new_numbers_list)



# new_list = list(map(lambda n: n*10, numbers)) 

# print(new_list) # [10, 20, 30, 40, 50]


new_set = set(map(lambda n: n*10, range(5))) 

# print(new_set) # {0, 40, 10, 20, 30}

new_set = set(map(lambda n: n*10, range(1, 6)))  

# print(new_set) # {40, 10, 50, 20, 30}


new_tuple = tuple(map(lambda n: n*10, range(1, 6))) 

# print(new_tuple) # (10, 20, 30, 40, 50)


# Create a list of numbers between 1000 and 2000 using map and lambda function from the following number: range(10, 20) # Exercise 4



# Find the longer text from two given texts using a lambda function.

# 'Race', 'Life is a maze.' --> 'Life is a maze.'


long_text = lambda text_1, text_2: text_1 if len(text_1) > len(text_2) else text_2

# print(long_text('Race', 'Life is a maze.')) # Life is a maze.


# Find the shorter text from two given texts using a lambda function.

# 'Melody', 'A thing of beauty is a joy forever.' --> 'Melody' # Exercise 5





# Capitalize the first character of each elements from a given list of strings using map and lambda function:

# ['maria', 'python', 'atlantic'] --> ['Maria', 'Python', 'Atlantic']


text_list = ['maria', 'python', 'atlantic']

cap_lambda = lambda t: t.capitalize()

new_text_list = list(map(cap_lambda, text_list))

# print(new_text_list) # ['Maria', 'Python', 'Atlantic']

# Uppercase all characters of each elements from a given list of strings using map and lambda function:

# ['maria', 'python', 'atlantic'] --> ['MARIA', 'PYTHON', 'ATLANTIC'] # Exercise 6



# List comprehension


numbers = [1, 2, 3, 4, 5] 

new_numbers = [x for x in numbers]

# print(new_numbers) # [1, 2, 3, 4, 5]


numbers = [1, 2, 3, 4, 5] # --> [10, 20, 30, 40, 50]

new_numbers = [x * 10 for x in numbers]

# print(new_numbers)

# create a list of numbers from a given list with each elements divided by 5.


numbers = [1, 2, 3, 4, 5] 

# new_numbers = [x / 5 for x in numbers]

# print(new_numbers) # [0.2, 0.4, 0.6, 0.8, 1.0]


new_numbers = (x / 5 for x in numbers)

print(tuple(new_numbers)) # (0.2, 0.4, 0.6, 0.8, 1.0)


# Return a list of strings from a given list where the elements are longer than 5 character using list comprehension.

['Laptop', 'Monitor', 'Keyboard', 'cap', 'Headphone', 'home', 'tech', 'Lunch']




# Create a list of dictionary from two given lists using list comprehension.

list_1 = ['name', 'age', 'is_employee']
list_2 = ['Ahmed', 37, 'True']

[{'name': 'Ahmed'}, {'age': 37}, {'is_employee': True}]


