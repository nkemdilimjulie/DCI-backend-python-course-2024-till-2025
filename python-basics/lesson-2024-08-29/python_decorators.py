
# Creating simple decorators


# def decorator(func):
#     def wrapper():
#         print(f'Sky is the limit.')
#         func()
#         print(f'Oceans are below the Earth.')
#     return wrapper


# def display_text():
#     print(f'Mountains are on the ground.')


# display_text() # Mountains are on the ground.


# def decorator(func):
#     def wrapper():
#         print(f'Sky is the limit.')
#         print(f'Oceans are below the Earth.')
#         return func()
#     return wrapper


# def display_text():
#     return (f'Mountains are on the ground.')


# new_text = decorator(display_text)

# print(new_text())

# display_new_text = decorator(display_text()) # does not work

# print(display_new_text()) # does not work


def decorator(func):
    def wrapper():
        print(f'Sky is the limit.')
        func()
        print(f'Oceans are below the Earth.')
     
    return wrapper


def display_text():
    print(f'Mountains are on the ground.')


new_text = decorator(display_text)

# print(new_text())

# new_text()

'''
Sky is the limit.
Mountains are on the ground.
Oceans are below the Earth.
None
'''


# def decorator(func):
#     def wrapper():
#         print(f'Sky is the limit.')
#         func()
#         print(f'Oceans are below the Earth.')
     
#     return wrapper

# @decorator
# def display_text():
#     print(f'Mountains are on the ground.')


# display_text()


'''
Sky is the limit.
Mountains are on the ground.
Oceans are below the Earth.
'''

def apply_decorator(func):
    def wrapper():
        print(f'Sky is the limit.')
        func()
        print(f'Oceans are below the Earth.')
     
    return wrapper

@apply_decorator
def display_text():
    print(f'Mountains are on the ground.')


# print(display_text())

# display_text()

'''
Sky is the limit.
Mountains are on the ground.
Oceans are below the Earth.
'''

def apply_decorator(func):
    def wrapper(which, where):
        print(f'Sky is the limit.')
        func(which, where)
        print(f'Oceans are below the Earth.')
     
    return wrapper

@apply_decorator
def display_text(which, where):
    print(f'Mountains are on the ground. {which} is the tallest mountain. It is situated in {where}.')


# display_text('Everest', 'Nepal')

'''
Sky is the limit.
Mountains are on the ground. Everest is the tallest mountain. It is situated in Nepal.
Oceans are below the Earth.
'''


# def apply_decorator(func):
#     def wrapper(*args):
#         print(f'Sky is the limit.')
#         func(*args)
#         print(f'Oceans are below the Earth.')
     
#     return wrapper

# @apply_decorator
# def display_text(which, where):
#     print(f'Mountains are on the ground. {which} is the tallest mountain. It is situated in {where}.')


# display_text('Everest', 'Nepal')

'''
Sky is the limit.
Mountains are on the ground. Everest is the tallest mountain. It is situated in Nepal.
Oceans are below the Earth.
'''

def apply_decorator(func):
    def wrapper(*args, who):
        print(f'Sky is the limit.')
        func(*args, who)
        print(f'Oceans are below the Earth.')
     
    return wrapper

@apply_decorator
def display_text(which, where, who='Edmund Hillary'):
    print(f'Mountains are on the ground. {which} is the tallest mountain. It is situated in {where}. {who} is the first human to climb on top of it.')


# display_text('Everest', 'Nepal', who='Tenzing Norgay')

'''
Sky is the limit.
Mountains are on the ground. Everest is the tallest mountain. It is situated in Nepal. Tenzing Norgay is the first human to climb on top of it.
Oceans are below the Earth.
'''


def apply_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Sky is the limit.')
        func(*args, **kwargs)
        print(f'Oceans are below the Earth.')
     
    return wrapper

@apply_decorator
def display_text(which, where, who='Edmund Hillary'):
    print(f'Mountains are on the ground. {which} is the tallest mountain. It is situated in {where}. {who} is the first human to climb on top of it.')


# display_text('Everest', 'Nepal', who='Tenzing Norgay')

'''
Sky is the limit.
Mountains are on the ground. Everest is the tallest mountain. It is situated in Nepal. Tenzing Norgay is the first human to climb on top of it.
Oceans are below the Earth.'''


def apply_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Sky is the limit.')
        func(*args, **kwargs)
        print(f'Oceans are below the Earth.')
     
    return wrapper


def display_text(which, where, who='Edmund Hillary'):
    print(f'Mountains are on the ground. {which} is the tallest mountain. It is situated in {where}. {who} is the first human to climb on top of it.')


# apply_decorator()

# display_text('Everest', 'Nepal', who='Tenzing Norgay')

# apply_decorator(display_text)('Everest', 'Nepal', who='Tenzing Norgay') # Christian

# display_text()

# Zoje's example

next_text = apply_decorator(display_text)

# next_text('Everest', 'Nepal', who='Tenzing Norgay')

'''
Sky is the limit.
Mountains are on the ground. Everest is the tallest mountain. It is situated in Nepal. Tenzing Norgay is the first human to climb on top of it.
Oceans are below the Earth.
'''


# def apply_discount(func):
#     def wrapper(*args, **kwargs):
#         total_price = func(*args, **kwargs)

#         return total_price - 70
    
#     return wrapper


# @apply_discount
# def calculate_total_price(price, quantity):
#     return price * quantity

# print(calculate_total_price(100, 3)) # 230



# def apply_discount(func):
#     def wrapper(*args, **kwargs):
#         total_price = func(*args, **kwargs)

#         return total_price - args[2]
    
#     return wrapper


# @apply_discount
# def calculate_total_price(price, quantity, discount):
#     return price * quantity

# print(calculate_total_price(100, 3, 70)) # 230


# def apply_discount(discount):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             total_price = func(*args, **kwargs)

#             return total_price - discount
        
#         return wrapper
#     return decorator
    

# @apply_discount(30)
# def calculate_total_price(price, quantity):
#     return price * quantity

# print(calculate_total_price(100, 3)) # 270


def apply_discount(discount, tax):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_price = func(*args, **kwargs)

            return total_price - discount + tax
        
        return wrapper
    return decorator
    

@apply_discount(30, 50)
def calculate_total_price(price, quantity):
    return price * quantity

# print(calculate_total_price(100, 3)) # 320


# def text_upper(func):
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)

#         return text.upper()
#     return wrapper



# def greet():
#     return f'weLcoMe to pyThoN deCorAtoRs.'


# print(greet()) # weLcoMe to pyThoN deCorAtoRs.



def text_upper(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)

        return text.upper()
    return wrapper


def text_lower(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)

        return text.lower()
    return wrapper


# @text_capitalize # Execute third
@text_upper # Execute second
@text_lower # Execute first
def greet():
    return f'weLcoMe to pyThoN deCorAtoRs.'


print(greet()) # WELCOME TO PYTHON DECORATORS.
