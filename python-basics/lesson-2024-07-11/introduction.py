
# print('Hello Python!', 'Welcome to Python module.', 2024, sep=' ', end='\n')


name = 'Roger Federer'

age_1 = 34

Age_2 = 42

age_3 = 50

"""
print(name)
print(age_1)
print(Age_2)
"""

'''This is a comment
This is multi line comment
Comments are continuing'''

"""
This is a comment
This is multi-line comment
Comments are continuing
These are called docstrings
"""


# camel case naming
personAgeHeight = '28 and 172 cm'

# pascal case naming
PersonAgeHeight = '28 and 172 cm'

# snake case naming
person_age_height = '28 and 172 cm' # This is a line comment

# print(person_age_height)


# x, y, z = 'green', 'blue', 'yellow'

# print(y)


x = y = z = 'magenta'

# print(z)
# print(x)


color_1 = 'green'
color_2 = 'purple'
# print(color_2)

# swap
color_1, color_2 = color_2, color_1

# print(color_2)



# Data types in Python



"""
string, integer, float, boolean, complex, None 
"""

first_name = 'Thomas'

age = 22

weight = 65.7

is_student = True

complex_num = 5+7j

temperature = None


# print(isinstance(age, int))

# print(isinstance(complex_num, complex))


# print('Is age an integer?:', isinstance(age, int))




# print(type(first_name))
# print(type(weight))
# print(type(temperature))



# user input

# sport = input('What is your favorite sport? ')

# print('I see, your favorite sport is', sport)

# print(type(sport))


# number = int(input('Enter a number: '))

# real_number = int(number)

# print(type(number))


# Math operators


"""addition(+), subtraction(-), multiplication(*), division(/), modulus(%), floor division(//)"""


# num1 = 120
# num2 = 80

# result = num1 / num2

# print(result)


# complex_number = <real_part> + <complex_part>j

# num1 = 4+7j
# num2 = 3+2j

# result = num1 - num2

# print(result)



num1 = 20
num2 = 6

# result = num1 % num2

result = num1 // num2

# print(result)



maximum_num = max(44, 35, 127, 500, 3, 77, 222)

minimum_num = min(44, -35, 127, 500, 3, -77, 222)

# print(minimum_num)


# number = -2550

# abs_num = abs(5-25) # -20

# abs_num = abs(4-3j)

# print(abs_num)



# number = round(12.8527845, 2)

# print(number)

# number = pow(3, 7) # 3^7 = 3 * 3 * 3 * 3 * 3 * 3 * 3

# print(number)


import math

# number = math.pi

# print(number)


# number = math.sqrt(49)

# print(number)


# number = math.ceil(435.0375)

number = math.floor(10.45)

print(number)