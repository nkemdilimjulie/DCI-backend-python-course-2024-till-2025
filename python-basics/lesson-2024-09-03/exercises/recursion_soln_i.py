# Task 1

def countdown(num):
    if num == 0:
        print(num)
    else:
        print(num)
        countdown(num-1)

# countdown(5)

# Short solution of task 1

def countdown(num):
    print(num)
    if num > 0:
        countdown(num-1)

# countdown(5)


# Task 2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) 

# print(factorial(0))
# print(factorial(1))
# print(factorial(10))


# Task 3

def harmonic_sum(n):
    if n == 0:
        return 0
    else:
        return 1/n + harmonic_sum(n -1)   
    
print(harmonic_sum(7))
print(harmonic_sum(4))  