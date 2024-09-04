
# Task 3:


# memory = {'func1': {'args': 'result'}} # --> Final target 

# memory = {} # first step

# memory = {'func': {}} # second step

# memory = {'func': {'args': 'result'}} # third step

# memory = {}

# def cache(func):
#     def wrapper(*args):
#         if func not in memory.keys():
#             memory[func] = {}
#         if args not in memory[func]:
#             print('Calculating')
#             memory[func][args] = func(*args)
#         else:
#             print('Using the cache')
#         return memory[func][args]
#     return wrapper


# def cache(func):
#     memory = {}
#     print(id(memory))
#     def wrapper(*args):
#         if func not in memory.keys():
#             memory[func] = {}
#         if args not in memory[func]:
#             print('Calculating')
#             memory[func][args] = func(*args)
#         else:
#             print('Using the cache')
#         return memory[func][args]
#     return wrapper


# def cache(func):
#     def wrapper(*args, memory = {}):
#         if func not in memory.keys():
#             memory[func] = {}
#         if args not in memory[func]:
#             print('Calculating')
#             memory[func][args] = func(*args)
#         else:
#             print('Using the cache')
#         return memory[func][args]
#     return wrapper


def cache(func):
    def wrapper(*args, memory = {}, **kwargs):
        if func not in memory.keys():
            memory[func] = {}
        if args not in memory[func]:
            print('Calculating')
            memory[func][args] = func(*args, **kwargs)
        else:
            print('Using the cache')
        return memory[func][args]
    return wrapper


@cache
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, 2))
print(sum(3, 2))
print(sum(3, 2))
print(sum(2, 1))

# print(memory)

