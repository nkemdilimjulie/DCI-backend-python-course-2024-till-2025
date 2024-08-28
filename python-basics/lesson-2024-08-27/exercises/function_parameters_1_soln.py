# Task 1

def isOdd(num):
    """Return True if the value is an odd number and False otherwise."""
    return num % 2 != 0

def isEven(num):
    """Return True if the value is an even number and False otherwise."""
    return num % 2 == 0

# Test cases

# print(isOdd(1), isEven(1))
# print(isOdd(-42), isEven(-42))
# print(isOdd(0), isEven(0))


# Task 2

def getParity(value, parity):
    """Return true if the value is of the parity indicated."""
    if parity == 'odd':
        return bool(value % 2)
    elif parity == 'even':
        return not value % 2
    return "Parity indicated is unknown"


# Test cases

# print(getParity(1, 'odd'), getParity(1, 'even'))
# print(getParity(-42, 'odd'), getParity(-42, 'even'))
# print(getParity(0, 'odd'), getParity(0, 'even'))
# print(getParity(-2, 'number'), getParity(-2, 'pair'))


# Task 3
import datetime

def greet(name, date):
    """Return a greeting to the person's name depending on the time of the day."""
    if date.hour < 12:
        return f"Good Morning, {name}!"
    return f"Good Afternoon, {name}!"


# Test cases

# print(greet(name="John", date=datetime.datetime(2021, 5, 7, 11, 59, 59)))
# print(greet(date=datetime.datetime(2021, 5, 7, 12, 0, 1), name="John"))


# Task 4

def sumAll(*lists):
    """Return the maximum number in any of the lists."""
    return sum([sum(l) for l in lists])


# Test cases

test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]

print(sumAll(*test1))
print(sumAll(*test2))


# Task 5

def pig_latin(*texts, suffix='ay', single=False):
    """Pig latin translator.

    For each word:
    - If the word starts with a vowel, add the suffix to the word.
    - If not, move the first letter to the end and add the suffix to the word.
    """
    pig_latin_version = []
    for text in texts:
        words = text.split(" ")
        for word in words:
            first = word[0].lower()
            if first in 'aeiou':
                pig_latin_version.append((word + suffix).capitalize())
            else:
                pig_latin_version.append((word[1:] + first + suffix).capitalize())
    if single:
        return " ".join(pig_latin_version)
    return pig_latin_version


# Test cases

test1_data = ["Word", "Apple"]
test1_config = {}
test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oi"}
test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}

print(pig_latin(*test1_data, **test1_config))
print(pig_latin(*test2_data, **test2_config))
print(pig_latin(*test3_data, **test3_config))