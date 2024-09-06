
# Boolean Logic

# AND, OR, NOT

# age = 23

# has_license = True

# if age > 18 and has_license == True:    # True and True --> True
#     print('You are allowed to drive.')


age = 23

has_license = False

if age > 18 and has_license == True:    # True and False --> False
    print('You are allowed to drive.') # no output



# 'hello' == 'hello' --> True

# False == False -->  True 

# False == 'Fantastic' -->  False 


raining = False

umbrella = True

# if raining == False or umbrella == True:   # False == False -->  True                       ,True or True --> True
#     print('You can go outside.') # You can go outside.


# if raining or umbrella:    # False or True --> True
#     print('You can go outside.') # You can go outside.


# if True or False:                   # --> True
#     print('This will be True.')


if False or False:                   # --> False
    print('This will be False.')



# print(False or True) # --> True

# print(False or False) # --> False



# raining = False

# umbrella = True


# if raining or umbrella:    # False or True --> True
#     print('You can go outside.') # You can go outside.




# print(True) # True

# print(not True) # False


is_student = False
# is_student == False

if is_student:  # False
    print('Go to the field and play with your friends.') # no output


# if not is_student:  # not False --> True
#     print('You need to pay the full price.')


# if not is_student == 'Myself':  # not False --> True
#     print('You need to pay the full price.')



# age = 10

# parent_permission = True


# if age >= 16 or (age >= 12 and parent_permission):  # False or (False and True) --> False or False --> False

#     print('You can skydive.') # no output




# age = 10

# parent_permission = True


# if age >= 16 or age >= 12 and parent_permission:   # False or False and True --> False or False --> False
#     print('You can skydive.') # no output


# age = 14

# parent_permission = True


# # False or True and True --> False or True --> True

# if age >= 16 or age >= 12 and parent_permission:
#     print('You can skydive.') # You can skydive.



age = 14

parent_permission = True


# False or True and False --> False or False --> False

if age >= 16 or age >= 12 and not parent_permission:
    print('You can skydive.') 

# Output: does not print.



temperature = 25

humidity = 50

condition = 'cloudy'


# True and True and False --> True and False --> False

# if temperature >= 20 and humidity >= 30 and condition == 'windy':
#     print('There is a storm coming soon.') # no output


# True and True or False --> True or False --> True

# if temperature >= 20 and humidity >= 30 or condition == 'windy':
#     print('There is a storm coming soon.') # There is a storm coming soon.


temperature = 25

humidity = 50

condition = 'cloudy'

wind_speed = 37

# True and (False or False) --> True and False --> False

# if temperature >= 20 and (humidity <= 30 or condition == 'windy'):
#     print('There is a storm coming soon.') # no output


# True and (False or False) and not False --> True and (False or False) and True --> 

# -->  True and False and True --> True and False --> False

if temperature >= 20 and (humidity <= 30 or condition == 'windy') and not wind_speed == 50:
    print('There is a storm coming soon.') # no output



# Short-ciruiting


def watch_sports():
    print('Watching sports is my favorite activity in the weekends.')
    return True


def is_weekend():
    print('Today is Saturday.')
    return False

# watch_sports() and is_weekend()   # True and False --> False
# Output: both

# is_weekend() and watch_sports() # False and True --> False
# Output: both


# watch_sports() or is_weekend() # True or 'no need to execute' --> True

# Output: first only

if watch_sports() and not is_weekend(): # True and not False --> True and True --> True
    print('It is time for a lunch!')

# Output: all

'''
Watching sports is my favorite activity in the weekends.
Today is Saturday.
It is time for a lunch!
'''