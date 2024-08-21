# any(), all() returns True/False


a_list = ['Painting', 2024, True, {'price': 33.99}, 3+5j, 'Mercedes']

# a_list = ['Painting', 2024, '', True, {'price': 33.99}, [],  3+5j, 'Mercedes']



# print(any(a_list))

# print(all(a_list))


another_list = ['', [], False, 0, 'Gardening']

# print(any(another_list))

# print(all(another_list))


# collections module
import collections
import collections as c
import collections as collc

hobbies = ['Photography', 'Traveling', 'Yoga', 'Hiking', 'Cooking',
           'Yoga', 'Reading', 'Fishing', 'Yoga', 'Cooking']

# print(len(hobbies))

# hobbies_counter = collections.Counter(hobbies)

# print(hobbies_counter)

# print(hobbies_counter['Traveling'])
# print(hobbies_counter['Cooking'])

# for item in hobbies_counter:
#     print(item)


# for item in hobbies_counter.keys():
#     print(item)

# for item in hobbies_counter.values():
#     print(item)


# for item in hobbies_counter.items():
#     print(item)


# print(hobbies_counter.items())


import collections as collc

hobbies = ['Photography', 'Traveling', 'Yoga', 'Hiking', 'Cooking',
           'Yoga', 'Reading', 'Fishing', 'Yoga', 'Cooking', 'Cooking']


hobbies_counter = collc.Counter(hobbies)

# print(hobbies_counter.most_common(2))

# print(hobbies_counter.most_common(1))

# print(len(hobbies))

# print(hobbies_counter.total())

# for item in hobbies_counter.most_common():
#     print(item)



profession = collc.Counter(Engineers = 3, Developers = 10, Programmers = 20)

# print(profession)



hobbies = ['Photography', 'Traveling', 'Yoga', 'Hiking', 'Cooking',
           'Yoga', 'Reading', 'Fishing', 'Yoga', 'Cooking', 'Cooking',
           'Photography', 'Photography']

hobbies_counter = collc.Counter(hobbies)

profession = ['Engineers', 'Developers', 'Programmers', 'Testers', 'Photography']

profession_counter = collc.Counter(profession)

# print(profession_counter)

# combine = hobbies_counter + profession_counter # -, &, |, ==

# combine = hobbies_counter - profession_counter # -, &, |, ==

# print(combine)

# print(dict(combine))


# combine = hobbies_counter.update(profession_counter)

reduce = hobbies_counter.subtract(profession_counter)

# print(combine)

# print(reduce)

# print(hobbies_counter)


# OrderedDict()

website_config = {
    'name': 'Python',
    'url': 'https://python.org',
    'office': 'Silicon valley 107',
    'ssl': 'Letsencrypt'
}

od = collc.OrderedDict(website_config)

# print(website_config)
# print(od)

# print(od['name'])

# print(od)

# od.move_to_end('url')

# print(od)

# ChainMap()

# collc.ChainMap


# from datetime import datetime

import datetime

# print(datetime.datetime.now())

# print(datetime.datetime.today())


from zoneinfo import ZoneInfo



# ChainMap()

dictionary_1 = {
    'name': 'Python',
    'url': 'https://python.org',
    'office': 'Silicon valley 107',
    'ssl': 'Letsencrypt'
}

dictionary_2 = {
    'name': 'Regex',
    'url': 'https://regexlearn.com',
    'office': 'California 373',
    'ssl': 'Letsencrypt'
}

import collections

chain_dictionary = collections.ChainMap(dictionary_1, dictionary_2)

# print(chain_dictionary) 

# Output: ChainMap({'name': 'Python', 'url': 'https://python.org', 'office': 'Silicon valley 107', 'ssl': 'Letsencrypt'}, {'name': 'Regex', 'url': 'https://regexlearn.com', 'office': 'California 373', 'ssl': 'Letsencrypt'})

# print(chain_dictionary['name']) # Output: Python


# print(chain_dictionary.maps) 

# Output: [{'name': 'Python', 'url': 'https://python.org', 'office': 'Silicon valley 107', 'ssl': 'Letsencrypt'}, {'name': 'Regex', 'url': 'https://regexlearn.com', 'office': 'California 373', 'ssl': 'Letsencrypt'}]



# print(chain_dictionary.maps[1])

# Output: {'name': 'Regex', 'url': 'https://regexlearn.com', 'office': 'California 373', 'ssl': 'Letsencrypt'}


# print(chain_dictionary.maps[1]['ssl']) # Output: Letsencrypt

# print(dictionary_1['name']) # Output: Python

# [1, 2, 3].extend()


# namedtuple()

coordinate = collc.namedtuple('Location', ['lattitude', 'longitude'])

place = coordinate(34.55, 120.77) # Object/Instance

# print(place) # Output: Location(lattitude=34.55, longitude=120.77)

print(place.lattitude) # Output: 34.55

print(place.longitude) # Output: 120.77

