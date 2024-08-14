
# Unpacking dictionary


person = {
    'name': 'Thomas',
    'age': 30,
    'position': 'Developer'

}


# def introduce(name, age, position):
#     return f'Hello, my name is {name}. I am {age} years old. I am a {position}.'


# print(introduce('Alexander', 28, 'Manager'))
# print(introduce('Elizabeth', 23, 'Desiner'))

# print(introduce(**person))


person_1 = {
    'name': 'Thomas',
    'age': 30,
    'position': 'Developer'

}

person_2 = {
    'name': 'Emily',
    'age': 28,
    'position': 'Marketer'

}

products = {
    'title': 'Laptop',
    'price': 1200,
    'stock': 50
}

weather = {
    'temperature': 22,
    'condition': 'Sunny'
}

all_person_products = {**person_1, **products, **weather}

# print(all_person_products)



# Iterables

# List, Tuple, Set, Dictionary

# len()



activities = ['Walking', 'Running', 'Talking', 'Eating']


# print(len(activities))
# print(len(products))


# enumerate()
# print('Todo list:')

# for i, j in enumerate(activities):   
#     print(f'{i+1}. {j}')


# for i, j in enumerate(activities, 1):   
#     print(f'{i}. {j}')

# for index, activity in enumerate(activities, 1):   
#     print(f'{index}. {activity}')


# for count, activity in enumerate(activities, 1):   
#     print(f'{count}. {activity}')


weather = {
    'temperature': 22,
    'condition': 'Sunny',
    'location': 'Paris'
}

# print('Weather Today:')

# for i in weather:
#     print(i)


# for i in weather.keys():
#     print(i)


# for count, data in enumerate(weather, 1):   
#     print(f'{count}.{data}: {weather[data]}')


# for count, data in enumerate(weather.items(), 1):   
#     print(f'{count}.{data[0]}: {data[1]}')


# for i in weather.items():
#     print(i)


# zip()

# all_products = ['Laptop', 'Phone', 'Monitor', 'Mouse']

all_products = ['Laptop', 'Phone']

all_prices = [1200, 800, 400, 20]


# for product, price in zip(all_products, all_prices):
#     print(f'{product} cost {price} euro.')

# for product, price in zip(all_products, all_prices, strict=True):
#     print(f'{product} cost {price} euro.')



# max, min, sum

all_prices = [1200, 800, 400, 20]


def find_max(data):
    val = max(data)
    return f'The maximum value is {val}.'

# print(find_max(all_prices))


# print(max(all_prices))
# print(min(all_prices))
# print(sum(all_prices))

shopping_cart = {
    'product_1': 1000,
    'product_2': 500,
    'product_3': 50,

}

empty_list = []

for i in shopping_cart.values():
    empty_list.append(i)


# print(sum(empty_list))

# print(sum(shopping_cart.values()))
# print(min(shopping_cart.values()))



# sorted()


all_prices = [1200, 400, 20, 800]




# sorted_prices = sorted(all_prices)

# sorted_prices = sorted(all_prices, reverse=True)

all_prices = [1200, 400, 20, 800]



shopping_cart = {
    'product_2': 1000,
    'product_1': 500,
    'product_3': 50,

}

def sorting_func(data):
    return data[1]


# print(sorting_func(('score', 10, 'goal')))

# print(sorting_func('product_2'))

# sorted_prices = sorted(shopping_cart, key=sorting_func)

# sorted_prices = sorted(shopping_cart.values())

# sorted_prices = sorted(shopping_cart.items(), key=sorting_func)

# print(sorted_prices)


books = {
  'Harry Potter And The Sorcerer\'s Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}


def book_func(x):
    return x[1]


new_books = sorted(books.items(), reverse=True, key=book_func)

print(new_books)








