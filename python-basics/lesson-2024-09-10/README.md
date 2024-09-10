## Friday - 2024-09-06

* Concepts of Boolean logic
* Predicates in Logical expressions
* Truthy and Falsy values and how python interprets 
    non-boolean values
* Logical operators and their precedence
* Exercises


## Today - 2024-09-10

* Interpreting truth tables
* Understanding complex logical operators (XOR, NAND, NOR, XNOR)
* Create complex expressions
* Exercises


### **1. Interpreting Truth Tables**

**What is a Truth Table?**
A truth table is a mathematical table used to determine the output of a logical expression based on all possible input combinations of True (1) or False (0) values. It’s widely used in digital circuits and boolean algebra to understand logical operations.

**Example: Truth Table for AND (`&&`) Operation**

| A (Input 1) | B (Input 2) | A AND B (Output) |
|-------------|-------------|-----------------|
| False       | False       | False           |
| False       | True        | False           |
| True        | False       | False           |
| True        | True        | True            |


### **2. Advanced Logical Operators**

Python’s standard library doesn’t directly support non-native logical operators like XOR, NAND, NOR, and XNOR, but you can implement these using combinations of existing Python operators (`and`, `or`, `not`, etc.).


#### **XOR (Exclusive OR)**
- **Definition:** Returns `True` if one, and only one, of the inputs is True. If both inputs are True or both are False, it returns False.

```python
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
```


#### **NAND (Not AND)**
- **Definition:** Returns `True` if at least one of the inputs is False. Only returns `False` if both inputs are True.

```python
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
```

#### **NOR (Not OR)**
- **Definition:** Returns `True` if both inputs are False. Otherwise, it returns `False`.

```python
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
```

#### **XNOR (Exclusive NOR)**
- **Definition:** Returns `True` if both inputs are the same (either both True or both False).

```python
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

# print(result) # True


def circuit_on(switch_1, switch_2):
    return (switch_1 and switch_2) or not (switch_1 or switch_2)


print(circuit_on(True, True)) # True
print(circuit_on(False, False)) # True
print(circuit_on(True, False)) # False
```


















































































