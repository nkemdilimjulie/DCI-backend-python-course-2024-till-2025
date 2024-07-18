
'''
text = 'Today is Thursday.'

if text.find('Thursday') == -1:
    print('The word is not found.')
else:
    i = text.find('Thursday')
    print('The word is at index', i)

text = 'Today is Thursday.'

index = text.find('Thursday')

if  index == -1:
    print('The word is not found.')
else:
    print('The word is at index', index)

'''


# name = str('Emily')
'''
name = int(float('7.888888'))

name = bool(str(round(float('7.888888'))))

print(name)
'''


text = 'This is a function.'

city = 'Berlin is the capital of Germany.'

# def text_upper(txt, num, data, car_list, post):

# def text_upper(txt, num, *data):

def text_upper(txt, num):
    new_txt = txt.upper()
    new_num = num + 100
    print(new_txt, new_num)



# text_upper('hello world', 24, 'Sunny', 'Cloudy', 'Stormy')

# text_upper('hello world', 24)
# text_upper(text, 77)
# text_upper(city, 11)


# def simple(*args, **kwargs):

# def simple():
#     text = input('Enter your favorite food: ')
#     num = int(input('Enter a number: '))
#     new_num = num +1000

#     full_text = text + ' ' + str(new_num)

#     return full_text

# print(simple())



# name  = 'Alex'

# new_name = name

# print(name*5, sep=' ')

# print((name + ' ')*5)

# print(name + ' 5 ' + str(True))


# def text_convert(name: str):

# def text_convert(name):
#     full_text = str(name) + ' 5 ' + str(True)
#     return full_text


# print(text_convert('Emily'))
# print(text_convert(400))



# String Slicing

# text[start:end:step]

# Normal index -> 0, 1, 2, 3,......22
# Reverse index -> -1, -2, -3, -4,....,-23

text = 'Far across the distance'


# print(text[-200])

# print(text[0:10:3])

# print(text[11])

# print(len(text))
# print(text[-23])

# print(text[-1:-10:-3])

# print(text[::1])
# print(text[::-1])

# print(text[-1:-len(text)-1:-1])
# print(text[-1:-(len(text)+1):-1])

'''
# console.log(text[-0:len(text):-1])

# print(text[-0:len(text):-1])
'''


# strip method


# text = '------Far across the distance and spaces between us------'

# new_text = text.strip('-') + 't'
# new_text = text.lstrip('-') + 't'
# new_text = text.rstrip('-') + 't'

# print(text)
# print(new_text)

# String format

text = 'Lunch time is %s passed until %d.'

new_text = text % ('already', 1310)

print(text)
print(new_text)

'--f--'


