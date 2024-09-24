
# Using context variables

def calculate_total_price(price, tax):
    total_price = price + (price * tax)

    return total_price

product_price = 100
product_tax = 0.1

# print(calculate_total_price(product_price, product_tax))




# Conditional breakpoint

# def find_number(lst, target):

#     for i, num in enumerate(lst):
#         if num == target:
#             y = i
#     else:
#         print('After the for loop.')
#         total = 200
        
#     return -1

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# x = 50

# print(find_number(numbers, x))




def find_number(lst, target):

    for i, num in enumerate(lst):
        if num == target:
            return i
        
    return -1

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = 50

# print(find_number(numbers, x))


# Stack Frames

def outer():
    var_out = 20
    return inner()


def inner():
    var_in = 300
    return 'It is lunch time.'

print(outer())




