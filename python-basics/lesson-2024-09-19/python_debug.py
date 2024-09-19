
# Debugging in Python 

def divide(a, b):
    return a / b

# print(divide(10, 0)) # ZeroDivisionError: division by zero
# print(divide(10, 5)) # 2


def calculate_average(numbers):
    total = 0
    import pdb; pdb.set_trace()
    for i in numbers:
        total += i
    
    breakpoint()
    average = total / len(numbers)

    return average

num_list = [10, 50, 20, 70, 30, 40]

print(calculate_average(num_list))
