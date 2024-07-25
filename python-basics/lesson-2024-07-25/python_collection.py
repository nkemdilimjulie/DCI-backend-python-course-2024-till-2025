

devices = ['Phone', 'Laptop', 'Monitor', 'keyboard', 'Mouse']

books = {'Harry Poter', 'Python for Beginners', 'The Tale of Two Cities'}

books_list = list(books)

# print(devices)
# print(books)
# print(books_list)

# print(type(devices))


text = 'We watched The Last of Us yesterday.'

text_list = list(text)

# print(text)
# print(text_list)



devices = ['Phone', 'Laptop', 'Monitor', 'keyboard', 'Mouse']

# single_device = devices[3]

# print(single_device)

# print(devices.index('keyboard'))


# print(devices[2:5])

# print(devices[-1])

# print(devices[::-1])

devices = ['Phone', 'Laptop', 'Monitor', 'keyboard', 'Mouse']

# new_devices = devices[::-1]

# print(new_devices)
# print(devices)
# print(devices.reverse())
# print(devices)


devices = ['Phone', 'Laptop', 'Monitor', 'keyboard', 'Laptop', 'Mouse']

# quantity_laptop = devices.count('Laptop')

# quantity_laptop = devices.count('laptop')

# print(quantity_laptop)


devices = ['Phone', 'Laptop', 'Monitor', 'keyboard', 'Laptop', 'Mouse']


# devices.append('Tablet')

# devices.insert(2, 'Washing machine')

# print(devices)

devices = ['Phone', 'Laptop', 'Monitor', 'keyboard', 'Laptop', 'Mouse']


# print(devices.pop())

# print(devices.pop(3))

# print(devices.remove('Monitor'))

# print(devices)

devices = ['Phone', 'Laptop', 'Monitor', 'Keyboard', 'Laptop', 'Mouse']

books = ['Harry Poter', 'Python for Beginners', 'The Tale of Two Cities']


# devices_books = devices + books

# devices_books = devices.extend(books)

# print(devices_books)
# print(devices)
# print(books)

# print(devices.sort(reverse=True))
# print(devices)


mixed_list = ['Elbe', 'Refrigerator', 2024, 'Statue of Liberty', True, 1012.99, [1, 2, 3], 'Germany']

# print(mixed_list)

# for i in mixed_list:
#     print(i)


# Unpacking

numbers = [1, 2, 3, 4, 5]

# a, b, c, d, e = numbers

# a, b, *rest = numbers

# *rest, d, e = numbers

a, _, c, _, e = numbers

# print(a)
# print(b)
# print(e)

# print(a)
# print(c)
# print(e)
# print(rest)

num = [10, 20, 30]

def addition(a, b, c):
    return a + b + c


print(addition(10, 20, 30))
print(addition(*num))