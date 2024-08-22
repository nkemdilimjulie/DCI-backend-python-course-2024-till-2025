
# Iterable, Iterator, Iteration, iter()


animals = ['Panda', 'Fox', 'Kangaroo', 'Lion', 'Cat', 'Dog'] # Iterable


animals_iterator = iter(animals)


# print(animals) # ['Panda', 'Fox', 'Kangaroo', 'Lion', 'Cat', 'Dog']
# print(animals_iterator) # <list_iterator object at 0x7204f8857c70>


# for item in animals_iterator:
#     print(item)

# Output: 
'''Panda
Fox
Kangaroo
Lion
Cat
Dog'''



animals = ['Panda', 'Fox', 'Kangaroo', 'Lion', 'Cat', 'Dog'] # Iterable


animals_iterator = iter(animals) # Iterator


# print(next(animals_iterator)) # Iteration
# print(next(animals_iterator)) # Iteration
# print(next(animals_iterator))
# print(next(animals_iterator))
# print(next(animals_iterator))
# print(next(animals_iterator)) # Iteration
# print(next(animals_iterator)) # Iteration



# For loop


numbers_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for item in numbers_list:
#     print(item)

# Output:
'''
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
'''


numbers_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]

# for outer_item in numbers_list:
#     for inner_item in outer_item:
#         if inner_item == 5:
#             continue
#         print(inner_item)

    

daily_tasks = {
    'day_1': 'Task 1',
    'day_2': 'Task 2',
    'day_3': 'Task 3',
}

# for key in daily_tasks:
#     print(key)

# Output:

'''
day_1
day_2
day_3
'''


# for key in daily_tasks.keys():
#     print(key)

# Output:

'''
day_1
day_2
day_3
'''


# for value in daily_tasks.values():
#     print(value)


# Output
'''
Task 1
Task 2
Task 3
'''


daily_tasks = {
    'day_1': 'Task 1',
    'day_2': 'Task 2',
    'day_3': 'Task 3',
}


# for item in daily_tasks.items():
#     print(item)

# Output:

'''('day_1', 'Task 1')
('day_2', 'Task 2')
('day_3', 'Task 3')'''


# for item in daily_tasks.items():
#     print(item[0])

'''
day_1
day_2
day_3
'''

# for item in daily_tasks.items():
#     print(item[1])

'''
Task 1
Task 2
Task 3'''


daily_tasks = {
    'day_1': 'Task 1',
    'day_2': 'Task 2',
    'day_3': 'Task 3',
}

# for key, value in daily_tasks.items():
#     print(key, value)

'''
day_1 Task 1
day_2 Task 2
day_3 Task 3'''


# for key, value in daily_tasks.items():
#     print(key + '---->' + value)


'''
day_1---->Task 1
day_2---->Task 2
day_3---->Task 3
'''



daily_tasks = {
    'day_1': {
        'Tasks': {
            'task 1': 'Walk',
            'task 2': 'Talk'
        }
    },
    'day_2': {
        'Tasks': {
            'task 1': 'Sing',
            'task 2': 'Dance'
        }
    }
}

# for item in daily_tasks:
#     print(item)

'''
day_1
day_2'''

daily_tasks = {
    'day_1': {
        'Tasks': {
            'task 1': 'Walk',
            'task 2': 'Talk'
        }
    },
    'day_2': {
        'Tasks': {
            'task 1': 'Sing',
            'task 2': 'Dance'
        }
    }
}

# for item in daily_tasks.values():
#     print(item)


'''
{'Tasks': {'task 1': 'Walk', 'task 2': 'Talk'}}
{'Tasks': {'task 1': 'Sing', 'task 2': 'Dance'}}
'''

# Zoye's solution:

for val in daily_tasks.values():
    for v in val.values():
        for task in v.values():
            print(task)


'''
Walk
Talk
Sing
Dance
'''