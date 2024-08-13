

# Dictionary

'''
Key, value pairs
'''

# Creating dictionary

# person = {}

person = {'first_name': 'Alex', 'last_name': 'Simpson', 'age': 28, 'email': 'alex@gmail.com'}

shopping_cart = dict(laptop=1299, smartphone=799, keyboard=30)


# print(person)

# print(type(person))

# print(shopping_cart)

# print(type(shopping_cart))




person = {'first_name': 'Alex', 'last_name': 'Simpson', 'age': 28, 'email': 'alex@gmail.com'}


# print(person['email'])
# print(person['age'])
# print(person)
# person['last_name'] = 'Thompson'
# print(person)


# person['phone_no'] = 123456789

# person['phone_no'] = '+49123456789'

# print(person)

# print(person['phone_no'])


names = ['Alex', 'Emily', 'Thomas']
ages = [22, 19, 23]

person = dict(zip(names, ages))

# print(person)


# Dictionary methods


person = {'first_name': 'Alex', 'last_name': 'Simpson', 'age': 28, 'email': 'alex@gmail.com', 'address': 'South port 34'}

# print(person)
# person.clear()
# print(person)


# user = person.copy()
# print(user)

# print(person.get('email'))
# print(person.get('address', 'North street 27'))


person = {'first_name': 'Alex', 'last_name': 'Simpson', 'age': 28, 'email': 'alex@gmail.com'}


# print(person.pop('last_name'))

# print(person.popitem())

# print(person)

# print(person.keys())

# print(person.values())

# print(person.items())




# names = ['Alex', 'Emily', 'Thomas']
# ages = [22, 19, 23]

# user = dict(zip(names, ages))

person = {'first_name': 'Alex', 'last_name': 'Simpson', 'age': 28, 'email': 'alex@gmail.com'}

user = {'Alex': 22, 'Emily': 19, 'Thomas': 23, 'email': 'alex.bob@gmail.com'}


# print(user.update({'James': 24, 'Elizabeth': 25}))

# print(user)

# person.update(user)

# print(person)

user = {'Alex': 22, 'Emily': 19, 'Thomas': 23, 'email': 'alex.bob@gmail.com'}

# print(user.setdefault('contact'))

# print(user.setdefault('contact', 'via email or whatsapp'))

# print(user)

food_list = ['Pizza', 'Burger', 'Doner', 'Bread', 'Butter']

food_dict = dict.fromkeys(food_list, 'Discount 30%')

food_dict['Burger'] = 'Discount 50%'

# print(food_dict)


# Nested dictionary

person = [
            {
            'name': {
                'first_name': 'Alex',
                'middle_name': '',
                'last_name': 'Thompson'
            },
            'age': 28,
            'email': 'alex@gmail.com',
            'address': {
                'house_no': 44,
                'street_name': 'South port',
                'phone_no': {
                    'country_code': 'DE',
                    'area_code': {
                        '1st': '+49',
                        '2nd': 123
                    },
                    'number': 456789
                }
            }
          },
          {
            'name': {
                'first_name': 'Emily',
                'middle_name': '',
                'last_name': 'Johnson'
            },
            'age': 25,
            'email': ['emily@gmail.com', 'emily@outlook.com', 'emily@yahoo.com'],
            'address': {
                'house_no': 22,
                'street_name': 'North port',
                'phone_no': {
                    'country_code': 'DE',
                    'area_code': {
                        '1st': '+49',
                        '2nd': 123
                    },
                    'number': 987654
                }
            }
          },
          {
            'name': {
                'first_name': 'Thomas',
                'middle_name': '',
                'last_name': 'Johnson'
            },
            'age': 25,
            'email': ['emily@gmail.com', 'emily@outlook.com', 'thomas@yahoo.com'],
            'address': {
                'house_no': 22,
                'street_name': 'North port',
                'phone_no': {
                    'country_code': 'DE',
                    'area_code': {
                        '1st': '+49',
                        '2nd': 123
                    },
                    'number': 987654
                }
            }
          }
        ]


# print(person[2]['email'][2])

# print(person[1]['address']['street_name'])


# print(person['address']['phone_no'])

# print(person['name']['first_name'])
# print(person['address']['phone_no']['area_code']['2nd'])
# print(type(person))


for i in person:
    if i['name']['first_name'] == 'Thomas':
        print(i['email'][2])
        print(person.index(i))

    