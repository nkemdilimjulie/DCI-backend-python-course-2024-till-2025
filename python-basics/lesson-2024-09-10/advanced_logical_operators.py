
# XOR 

# a = True

# b = False

# result = (a or b) and not (a and b)

# print(result) # True


'''
-->(True or False) and not (True and False)
--> True and not False
--> True and True
--> True

'''


a = True

b = True

result = (a or b) and not (a and b)

# result = a XOR/&& b

'''
-->(True or True) and not (True and True)
--> True and not True
--> True and False
--> False

'''

# print(result) # False



# NAND


a = True

b = False

result = not (a and b)

'''
--> not (True and False)
--> not False
--> True

'''

# print(result) # True



a = False

b = False

result = not (a and b)

'''
--> not (False and False)
--> not False
--> True

'''

# print(result) # True


a = True

b = True

result = not (a and b) # False

# print(result) # False



# NOR

a = False

b = False


result = not (a or b)

'''
--> not (False or False)
--> not False
--> True
'''

# print(result) # True



a = False

b = True


result = not (a or b)

'''
--> not (False or True)
--> not True
--> False
'''

# print(result) # False


# a NOR b --> True if both of them are False



def nor_func(a, b):
    return not (a or b)


# print(nor_func(False, False)) # True
# print(nor_func(True, True)) # False




# def pump_start(tank_full, is_night):
#     return not (tank_full or is_night)


# print(pump_start(False, False)) # True


# pump_data = {'is_full': False, 'run_time': False}


# def pump_start(tank_full, is_night):
#     return not (tank_full or is_night)


# print(pump_start(pump_data['is_full'], pump_data['run_time'])) # True


pump_data = {'is_full': 'No', 'run_time': 0}


def pump_start(tank_full, is_night):
    # tf = True if tank_full == 'Yes' else False
    tf = False if tank_full == 'No' else True

    # if tank_full == 'No':
    #     tf = False

    rt = bool(is_night)

    return not (tf or rt)


# print(pump_start(pump_data['is_full'], pump_data['run_time'])) # True



pump_data = [
    {'is_full': 'No', 'run_time': 0},
    {'is_full': 'No', 'run_time': 0},
    {'is_full': 'Yes', 'run_time': 1},
    {'is_full': 'No', 'run_time': 0},
    {'is_full': 'Yes', 'run_time': 0},
    ]



pump_data = [
    {'pump_id': 1, 'is_full': 'No', 'run_time': 0},
    {'pump_id': 2, 'is_full': 'No', 'run_time': 0},
    {'pump_id': 3, 'is_full': 'No', 'run_time': 1},
    {'pump_id': 4, 'is_full': 'Yes', 'run_time': 0},
    {'pump_id': 5, 'is_full': 'No', 'run_time': 0},
    ]


pump_data = [
    {'pump_id': 1, 'is_full': 'No', 'run_time': 0, 'day_time': ['morning', 'mid-day', 'evening']},
    {'pump_id': 2, 'is_full': 'Yes', 'run_time': 1, 'day_time': ['morning', 'mid-day', 'evening']},
    {'pump_id': 3, 'is_full': 'No', 'run_time': 0, 'day_time': ['morning', 'mid-day', 'evening']},

    ]



# XNOR

# a = True
# b = True

# result = (a and b) or (not a and not b)

# print(result)



a = False
b = False

result = (a and b) or (not a and not b)

'''
--> (False and False) or (not False and not False)
--> False or (True and True)
--> False or True
--> True
'''

# print(result) # True


a = False
b = True

result = (a and b) or (not a and not b)

# print(result) # False


a = False
b = False

result = (a and b) or not (a or b)

'''
--> (False and False) or not (False or False)
--> False or not False
--> False or True
--> True
'''

# print(result) # False


def circuit_on(switch_1, switch_2):
    return (switch_1 and switch_2) or not (switch_1 or switch_2)


print(circuit_on(True, True))
print(circuit_on(True, False))

