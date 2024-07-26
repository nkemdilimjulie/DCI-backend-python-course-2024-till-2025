
# Tuples

# week = tuple()

# weather = ()

week = tuple(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Wednesday'])

weather = ('Sunny', 'Rainy', 'Cloudy', 'Stormy')

# print(week)
# print(weather)

# print(type(weather))

# print(week.index('Friday'))

# print(week.count('Wednesday'))

# print(week[0])

# print(week[0:3])

# print(week[::-1])

# print(week)

text = 'Reality is a subset of imagination.'

text_tuple = tuple(text)

# print(text_tuple)



# Sets

# sports = set()

# hobbies = {'Singing'}


sports = {'Football', 'Hockey', 'Tennis', 'Basketball', 'Swimming', 'Tennis'}

hobbies = {'Singing'}

# print(sports)
# print(hobbies)

# print(type(sports))
# print(type(hobbies))


sports = {'Football', 'Hockey', 'Tennis', 'Basketball', 'Swimming', 'Tennis'}

# print(sports[0])
# print(sports[0:4])

# print(sports.add('Voleyball'))

# activities = sports.copy()

# print(sports.clear())
# print(sports)
# print(activities)


sports = {'Football', 'Hockey', 'Tennis', 'Basketball', 'Swimming', 'Tennis'}


# print(sports.discard('Football'))

# print(sports.pop())
# print(sports.remove('Swimming'))
# print(sports)


# activities = sports.copy()

# sports.clear()

# print(sports)
# print(activities)

# print(sports == activities)

# print(id(sports))

# print(id(activities))


sports = {'Football', 'Hockey', 'Tennis', 'Basketball', 'Swimming', 'Tennis'}

hobbies = {'Singing', 'Dancing', 'Biking', 'Swimming', 'Tennis'}


# print(sports.intersection(hobbies))

# print(sports & hobbies)

# print(sports.union(hobbies))

# print(sports | hobbies)

# print(sports.difference(hobbies))

# print(sports - hobbies)

sports = {'Football', 'Hockey', 'Tennis', 'Basketball', 'Swimming', 'Tennis'}

hobbies = {'Singing', 'Dancing', 'Biking', 'Swimming', 'Tennis'}


# print(sports.symmetric_difference(hobbies))

# print(sports ^ hobbies)

# print(sports.symmetric_difference_update(hobbies))

# print(sports)
# print(hobbies)

sports = {'Football', 'Hockey', 'Tennis', 'Basketball', 'Swimming', 'Tennis'}

hobbies = {'Singing', 'Dancing', 'Biking', 'Swimming', 'Tennis'}

activities = {'Hockey', 'Tennis'}


# print(sports.issubset(hobbies))

# print(sports.issubset(activities))

# print(activities.issubset(sports))

# print(activities.issuperset(sports))

print(sports.issuperset(activities))