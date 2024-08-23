# Nested loops

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

# for key in daily_tasks.keys():
#     print(daily_tasks[key])

'''
{'Tasks': {'task 1': 'Walk', 'task 2': 'Talk'}}
{'Tasks': {'task 1': 'Sing', 'task 2': 'Dance'}}
'''

# for key in daily_tasks.keys():
#     print(daily_tasks[key])
#     inner_dictionary = daily_tasks[key]

#     for key_2 in inner_dictionary.keys():
#         print(key_2)


'''
{'Tasks': {'task 1': 'Walk', 'task 2': 'Talk'}}
Tasks
{'Tasks': {'task 1': 'Sing', 'task 2': 'Dance'}}
Tasks
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

# for key_1 in daily_tasks.keys():
#     print(f'{key_1}:')
#     inner_dictionary = daily_tasks[key_1]

#     for key_2 in inner_dictionary.keys():
#         print(f'    {key_2}')

'''
day_1:
    Tasks
day_2:
    Tasks
'''


# for key_1 in daily_tasks.keys():
#     print(f'{key_1}:')
#     inner_dictionary = daily_tasks[key_1]

#     for key_2 in inner_dictionary.keys():
#         print(f'    {key_2}:')
#         last_dictionary = inner_dictionary[key_2]

#         for key_3 in last_dictionary.keys():
#             print(f'        {key_3}')


'''
day_1:
    Tasks:
        task 1
        task 2
day_2:
    Tasks:
        task 1
        task 2
'''


# for key_1 in daily_tasks.keys():
#     print(f'{key_1}:')
#     inner_dictionary = daily_tasks[key_1]

#     for key_2 in inner_dictionary.keys():
#         print(f'    {key_2}:')
#         last_dictionary = inner_dictionary[key_2]

#         for key_3 in last_dictionary.keys():
#             print(f'        {last_dictionary[key_3]}')

        
'''
        for value_3 in last_dictionary.values():
            print(f'        {value_3}')'''

'''
day_1:
    Tasks:
        Walk
        Talk
day_2:
    Tasks:
        Sing
        Dance
'''



# for key_1 in daily_tasks.keys():
#     print(f'{key_1}:')
#     inner_dictionary = daily_tasks[key_1]

#     for key_2 in inner_dictionary.keys():
#         print(f'    {key_2}:')
#         last_dictionary = inner_dictionary[key_2]

#         for key_3, value_3 in last_dictionary.items():
#             print(f'        {value_3}')

'''
day_1:
    Tasks:
        Walk
        Talk
day_2:
    Tasks:
        Sing
        Dance
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



# for key_1 in daily_tasks.keys():
#     print(f'{key_1}:')
#     inner_dictionary = daily_tasks[key_1]

#     for key_2 in inner_dictionary.keys():
#         print(f'    {key_2}:')
#         last_dictionary = inner_dictionary[key_2]

#         for key_3, value_3 in last_dictionary.items():
#             print(f'        {key_3}: {value_3}')


'''
day_1:
    Tasks:
        task 1: Walk
        task 2: Talk
day_2:
    Tasks:
        task 1: Sing
        task 2: Dance
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
    },
    'day_3': {
        'Tasks': {
            'task 1': 'Read',
            'task 2': 'Code'
        }
    }
}


# for key_1 in daily_tasks.keys():
#     if key_1 == 'day_3':
#         print(f'{key_1}:')
#         inner_dictionary = daily_tasks[key_1]

#         for key_2 in inner_dictionary.keys():
#             print(f'    {key_2}:')
#             last_dictionary = inner_dictionary[key_2]

#             for key_3, value_3 in last_dictionary.items():
#                 print(f'        {key_3}: {value_3}')

'''
day_1:
    Tasks:
        task 1: Walk
        task 2: Talk
'''


'''
day_3:
    Tasks:
        task 1: Read
        task 2: Code
'''


# for key_1 in daily_tasks.keys():
#     if key_1 == 'day_3':
#         print(f'{key_1}:')
#         inner_dictionary = daily_tasks[key_1]

#         for key_2 in inner_dictionary.keys():
#             print(f'    {key_2}:')
#             last_dictionary = inner_dictionary[key_2]
#         else:
#             print('We are going into the Tasks.')

#             for key_3, value_3 in last_dictionary.items():
#                 print(f'        {key_3}: {value_3}')

# else:
#     print('We are done with all the tasks.')


'''
day_3:
    Tasks:
We are going into the Tasks.
        task 1: Read
        task 2: Code
We are done with all the tasks.
'''


daily_tasks = [
    {'day_1': {
        'Tasks': {
            'task 1': 'Walk',
            'task 2': 'Talk'
        }
    }},
    {'day_2': {
        'Tasks': {
            'task 1': 'Sing',
            'task 2': 'Dance'
        }
    }},
    {'day_3': {
        'Tasks': {
            'task 1': 'Read',
            'task 2': 'Code'
        }
    }}
]


# for item in daily_tasks:
#     print(item)


'''
{'day_1': {'Tasks': {'task 1': 'Walk', 'task 2': 'Talk'}}}
{'day_2': {'Tasks': {'task 1': 'Sing', 'task 2': 'Dance'}}}
{'day_3': {'Tasks': {'task 1': 'Read', 'task 2': 'Code'}}}
'''



# for item in daily_tasks.keys():
#     print(item)


# for item in daily_tasks:
#     for key_1 in item.keys():
#         print(key_1)

'''
day_1
day_2
day_3
'''


# for item in daily_tasks[0:1]:
#     for key_1 in item.keys():
#         print(key_1)
    
#Output: day_1



products = [
    {'id': 1, 'title': 'Lenovo Thinkpad 14', 'price': 1270, 'color': ['black', 'gray']},
    {'id': 2, 'title': 'iPhone 15 Pro Max', 'price': 1199, 'color': ['oceanblue', 'purple']},
    {'id': 3, 'title': 'T-Shirt', 'price': 22, 'color': ['white', 'green', 'orange']},
    ]


# for item in products:
#     print(item)

'''
{'id': 1, 'title': 'Lenovo Thinkpad 14', 'price': 1270, 'color': ['black', 'gray']}
{'id': 2, 'title': 'iPhone 15 Pro Max', 'price': 1199, 'color': ['oceanblue', 'purple']}
{'id': 3, 'title': 'T-Shirt', 'price': 22, 'color': ['white', 'green', 'orange']}
'''

# for item in products:
#     print(item.keys())


'''
dict_keys(['id', 'title', 'price', 'color'])
dict_keys(['id', 'title', 'price', 'color'])
dict_keys(['id', 'title', 'price', 'color'])'''



products = [
    {'id': 1, 'title': 'Lenovo Thinkpad 14', 'price': 1270, 'color': ['black', 'gray']},
    {'id': 2, 'title': 'iPhone 15 Pro Max', 'price': 1199, 'color': ['oceanblue', 'purple']},
    {'id': 3, 'title': 'T-Shirt', 'price': 22, 'color': ['white', 'green', 'orange']},
    ]


# for item in products:
#     print(item.values())

'''
dict_values([1, 'Lenovo Thinkpad 14', 1270, ['black', 'gray']])
dict_values([2, 'iPhone 15 Pro Max', 1199, ['oceanblue', 'purple']])
dict_values([3, 'T-Shirt', 22, ['white', 'green', 'orange']])'''



# for item in products:
#     print(item['title'])

'''
Lenovo Thinkpad 14
iPhone 15 Pro Max
T-Shirt'''

products = [
    {'id': 1, 'title': 'Lenovo Thinkpad 14', 'price': 1270, 'color': ['black', 'gray']},
    {'id': 2, 'title': 'iPhone 15 Pro Max', 'price': 1199, 'color': ['oceanblue', 'purple']},
    {'id': 3, 'title': 'T-Shirt', 'price': 22, 'color': ['white', 'green', 'orange']},
    ]


# for item in products:
#     print(item['price'])

'''
1270
1199
22'''


# Lenovo Thinkpad 14 1270
# iPhone 15 Pro Max 1199


# for item in products:
#     print(item['title'], item['price'])

'''
Lenovo Thinkpad 14 1270
iPhone 15 Pro Max 1199
T-Shirt 22
'''


products = [
    {'id': 1, 'title': 'Lenovo Thinkpad 14', 'price': 1270, 'color': ['black', 'gray']},
    {'id': 2, 'title': 'iPhone 15 Pro Max', 'price': 1199, 'color': ['oceanblue', 'purple']},
    {'id': 3, 'title': 'T-Shirt', 'price': 22, 'color': ['white', 'green', 'orange']},
    ]


# for item in products:
#     print(f"{item['title']}: {item['price']}")

'''Lenovo Thinkpad 14: 1270
iPhone 15 Pro Max: 1199
T-Shirt: 22'''

# for item in products:
#     print(f"{item["title"]}: {item["price"]}") # error


products = [
    {'id': 1, 'title': 'Lenovo Thinkpad 14', 'price': 1270, 'color': ['black', 'gray']},
    {'id': 2, 'title': 'iPhone 15 Pro Max', 'price': 1199, 'color': ['oceanblue', 'purple']},
    {'id': 3, 'title': 'T-Shirt', 'price': 22, 'color': ['white', 'green', 'orange']},
    ]

# for item in products:
#     print(item['color'])

'''
['black', 'gray']
['oceanblue', 'purple']
['white', 'green', 'orange']
'''

'''
black
gray
oceanblue
purple
..
...'''


products = [
    {'id': 1, 'title': 'Lenovo Thinkpad 14', 'price': 1270, 'color': ['black', 'gray']},
    {'id': 2, 'title': 'iPhone 15 Pro Max', 'price': 1199, 'color': ['oceanblue', 'purple']},
    {'id': 3, 'title': 'T-Shirt', 'price': 22, 'color': ['white', 'green', 'orange']},
    ]

# for item in products:
#     for colr in item['color']:
#         print(colr)

'''
black
gray
oceanblue
purple
white
green
orange
'''


products = [
    {'id': 1, 'title': 'Lenovo Thinkpad 14', 'price': 1270, 'color': ['black', 'gray']},
    {'id': 2, 'title': 'iPhone 15 Pro Max', 'price': 1199, 'color': ['oceanblue', 'purple']},
    {'id': 3, 'title': 'T-Shirt', 'price': 22, 'color': ['white', 'green', 'orange']},
    ]

# ['black', 'gray', 'oceanblue', 'purple', 'white',.....]

# empty_list = []

# for item in products:
#     for colr in item['color']:
#         empty_list.append(colr)


# print(empty_list)

'''['black', 'gray', 'oceanblue', 'purple', 'white', 'green', 'orange']'''

products = [
    {'id': 1, 'title': 'Lenovo Thinkpad 14', 'price': 1270, 'color': ['black', 'gray']},
    {'id': 2, 'title': 'iPhone 15 Pro Max', 'price': 1199, 'color': ['oceanblue', 'black', 'purple']},
    {'id': 3, 'title': 'T-Shirt', 'price': 22, 'color': ['white', 'green', 'orange', 'black']},
    ]

# empty_list = []
# counter = 0

# for item in products:
#     for colr in item['color']:
#         if colr == 'black':
#             counter += 1


# print(f'Total black color: {counter}')

# Total black color: 3


empty_list = []
# counter = 0

# for item in products:
#     for colr in item['color']:
#         if colr == 'black':
#             empty_list.append(colr)


# c = empty_list.count('black')
# c = len(empty_list)

# print(f'Total black color: {c}')

# Total black color: 3


# while loop

'''
1
2
3
4
..
..
'''

numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]

nums = [1, 2, 3]

i = 0

# while i < len(nums):
#     print(nums)
#     i += 1

'''
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]'''



numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]

nums = [1, 2, 3]

i = 0

# while i < len(nums):
#     print(nums[i])
#     i += 1

'''
1
2
3'''

nums = [1022, 200, 3000]

i = 0

# while i < len(nums):
#     print(nums[i])
#     i += 1

'''
1022
200
3000'''


# numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]


# i = 0

# while i < len(numbers):
#     print(numbers[i])
#     i += 1


'''
[1, 2, 3]
[4, 5]
[6, 7, 8]
'''

# numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]


# i = 0

# while i < len(numbers):
#     for n in numbers[i]:
#         print(n)
#     i += 1

'''
1
2
3
4
5
6
7
8'''


numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]

i = 0
j = 0

while i < len(numbers):
    while j < len(numbers[i]):
        print(numbers[i][j])
        j += 1
    j = 0
    i += 1


'''
1
2
3
4
5
6
7
8'''


numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]

i = 0

while i < len(numbers):
    j = 0
    while j < len(numbers[i]):
        print(numbers[i][j])
        j += 1
    i += 1
else:
    print('We are done for today.')

'''
1
2
3
4
5
6
7
8
We are done for today.
'''
