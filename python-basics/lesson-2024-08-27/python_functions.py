
# Function definition/structure

# Function with no argument

def greet(): # Header
    '''This is a simple function that greets people.''' # Documentation string (doc string)

    text = 'Hello everyone, good afternoon.' # Body

    return text # return

# Call/Use function

# print(greet()) # Hello everyone, good afternoon.


# Function with argument

# def calculate_total_price(price, quantity): # price, quantity --> parameters
#     '''This function calculates the total price of a product.'''

#     total_price = price * quantity

#     return total_price

# print(calculate_total_price(20, 5)) # 20, 5 --> arguments

# 100


def calculate_total_price(price, quantity): # price, quantity --> parameters
    '''This function calculates the total price of a product.'''

    total_price = price * quantity

    return f'The total price is {total_price}.'

# print(calculate_total_price(20, 5)) # 20, 5 --> arguments


# The total price is 100.




def calculate_area(lenth, width):
    '''Returns the area of a rectangle.'''
    area = lenth * width

    return area


calc_area = calculate_area(10, 2)

# print(calc_area) # 20

# print(calc_area + 100)


# Function retuning multiple values


def get_max_min(num_list):
    '''Returns the maximum and minimum values from a list.'''

    maximum = max(num_list)
    minimum = min(num_list)

    return maximum, minimum


num_max, num_min = get_max_min([30, 100, 70, 20, 77, 80])

# print(num_max) # 100
# print(num_min) # 20

# print(get_max_min([30, 100, 70, 20, 77, 80])) # (100, 20)

numbers = [2034, 300, 450, 1006, 1200, 3, 90, 180]

# print(get_max_min(numbers)) # (2034, 3)


# Input packed/unpacked data


# def claculate_bmi(weight, height, age):
#     '''Returns Body-mass index based on given data.'''

#     bmi_index = (weight / height**2) / 100

#     return bmi_index

# print(claculate_bmi(62, 0.170, 32)) # 21.45328719723183


def claculate_bmi(*args):
    '''Returns Body-mass index based on given data.'''

    bmi_index = (args[0] / args[1]**2) / 100

    return bmi_index

# print(claculate_bmi(62, 0.170, 32)) # 21.45328719723183


data_list = [62, 0.170, 32]

print(claculate_bmi(*data_list)) # 21.45328719723183