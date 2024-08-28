
# Understanding scope

# Global scope

# global_var = 'This is a global variable.'


# def outer_function():
#     # Enclosing scope

#     enclosing_var = 'This is an enclosing variable.'

#     def inner_function():
#         # Local scope
        
#         local_var = 'This is a local variable.'

#         print(global_var)
#         print(enclosing_var)
#         print(local_var)

#     inner_function()

# outer_function()

'''
This is a global variable.
This is an enclosing variable.
This is a local variable.

'''
# print('##############################')

# print(global_var)
# print(enclosing_var) # NameError: name 'enclosing_var' is not defined.
# print(local_var) # NameError: name 'local_var' is not defined.



global_var = 'This is a global variable.'

# print(global_var)

# global_var = 'This is a modified global variable.'

# print(global_var)

# def outer_function():
#     # Enclosing scope
#     global global_var

#     print(global_var)

#     global enclosing_var

#     enclosing_var = 'This is an enclosing variable.'

#     global_var = 'This is a modified global variable.'

#     print(global_var)

#     def inner_function():
#         # Local scope
        
#         local_var = 'This is a local variable.'

#     inner_function()

# outer_function()


# print(global_var)
# print(enclosing_var)

'''This is a global variable.
This is a global variable.
This is a modified global variable.
This is a modified global variable.
This is an enclosing variable.
'''


# Assigning function to a variable


def square(num):
    return num**2

# print(square(4)) # 16


square_var = square

# print(square_var(5)) # 25

# print(square(10)) # 100


# Function as an argument


def calculate_total_price(price, quantity):
    total_price = price * quantity
    return total_price


def calculate_total_price_with_discount(func, price, quantity, discount):

    total_value = func(price, quantity)

    discount_value =  total_value * (discount / 100)

    return total_value - discount_value


# print(calculate_total_price_with_discount(calculate_total_price, 100, 3, 30))



# Passing arguments in inner function



def get_multiplication(factor):

    def multiply_by_three(num):
        return num * 3
    
    return multiply_by_three(factor)


# print(get_multiplication(100)) # 300




# def get_multiplication(factor):

#     def multiply_by_three(num):
#         return num * factor
    
#     return multiply_by_three


# outer_func = get_multiplication(7)

# print(outer_func) # <function get_multiplication.<locals>.multiply_by_three at 0x761a684467a0>


def get_multiplication(factor):

    def multiply_by_three(num):
        return num * factor
    
    return multiply_by_three


outer_func = get_multiplication(7)

# print(outer_func(100))


# Julie's, example

# def multiply_by_three(num):
#     return num * 3

# def get_multiplication(factor):
#     multi_3 = multiply_by_three(77) 
#     return multiply_by_three(factor)

# print(multiply_by_three(20))



# Keyword arguments


# def greet(name):
#     print(f'Hello {name}, Good morning.')

# greet('Alex') # Hello Alex, Good morning.


def greet(name='Emily'):
    print(f'Hello {name}, Good morning.')


# greet()
# greet('Alex')
# greet(name='Thomas')

'''
Hello Emily, Good morning.
Hello Alex, Good morning.
Hello Thomas, Good morning.
'''


# def greet(name):
#     print(f'Hello {name}, Good morning.')

# # greet() # TypeError: greet() missing 1 required positional argument: 'name'

# greet(name='Michael') # Hello Michael, Good morning.


# def greet(name, age=40):
#     print(f'Hello {name}, Good morning. He is {age} years old.')


# greet(name='Michael') # Hello Michael, Good morning. He is 40 years old.


def greet(name, age=40):
    print(f'Hello {name}, Good morning. He is {age} years old.')


# greet(name='Michael', age=30) # Hello Michael, Good morning. He is 30 years old.


def greet(name, age=40):
    print(f'Hello {name}, Good morning. He is {age} years old.')


# greet('Jordan', age=50) # Hello Jordan, Good morning. He is 50 years old.


def greet(name, age=40, **kwargs):
    print(f'Hello {name}, Good morning. He is {age} years old.')


# greet('Jordan', age=50) # Hello Jordan, Good morning. He is 50 years old.


# def greet(name, age=40, **kwargs):
#     print(f'Hello {name}, Good morning. He is {age} years old.')
#     print('He is studying:')
#     for item in kwargs['subjects']:
#         print(item)


# greet('Jordan', age=50, height=175, weight=70, is_student=True, subjects=['Math', 'Physics', 'Programming'])


def greet(*args, **kwargs):
    print(f"Hello {kwargs['name']}, Good morning. He is {kwargs['age']} years old.")
    print('He is studying:')
    for item in kwargs['subjects']:
        print(item)


# greet(name='Jordan', age=50, height=175, weight=70, is_student=True, subjects=['Math', 'Physics', 'Programming'])

'''
Hello Jordan, Good morning. He is 50 years old.
He is studying:
Math
Physics
Programming
'''


def greet(*args, **kwargs):
    print(f"Hello {kwargs['name']}, Good morning. She is {kwargs['age']} years old.")
    print('She is studying:')
    for item in kwargs['subjects']:
        print(item)


person = {
    'name': 'Paula', 'age': 37, 'is_student': True, 'subjects': ['Design', 'Psychology', 'Marketing']
}

greet(**person)

'''
Hello Paula, Good morning. She is 37 years old.
She is studying:
Design
Psychology
Marketing'''