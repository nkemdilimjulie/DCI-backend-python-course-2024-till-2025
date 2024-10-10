# Advanced OOP 

### Wednesday - 2024-10-09
- Abstract Based Classes
- [Exercise](https://classroom.github.com/a/EjQfhvF3)

### Today - 2024-10-10
- Polymorphism
- Operator Overloading

### Polymorphism
In Greek

- `Poly` -> `Many`
- `morphism` -> `form`, `shape`, `structure`.

> Many Forms

>> In Python, Polymorphism means the same `function name` can be used with different data types. 

```python
# Here the `print` function is used with string, int, float, list, etc.
print('hello') # 'hello'
print(34) # 34
print(3.4) # 3.4
print([]) # []

# Here, the `len` function is used with different data types
print(len([3,4,5])) # 3
print(len('hello')) # 5
```

#### Application of Polymorphism in real-world situations

Let's take cars for example, We know that all cars have an accelerator pedal and when the driver presses that pedal, they are sending a message let's say 'accelerate' to the car. 

Now, base on the type of car
- Cars with internal combustion engine
- Cars with electric motor 
- Hybrid cars.

Independent of the car used, the same message is sent `accelerate`, and each car handles the message accordingly.

So, with Polymorphism, we can easily adopt a new technology. For example, we could develop a nuclear-powered car. The user interface of the car remains the same. That is, the accelerator pedal and the `accelerate` message sent, but now, a very different mechanism would make the nuclear-powered car go faster.


### Ways to achieve Polymorphism in Python
- Functions and objects
- Inheritance
- Overloading

#### Functions and objects
- Multiple classes have methods with the same name

```python
# Classes
class ListOfBook:
    def __init__(self, *args: str) -> None: # Packing and Unpacking Positional Argument
        self._data: tuple[str] = args
            
    def ls_all(self) -> list[str]:
        return list(self._data)
    

class ListOfStudent:
    def __init__(self, *args: str) -> None:
        self._data: tuple[str] = args
            
    def ls_all(self) -> tuple[str]:
        return self._data
    
    
class ListOfMusic:
    def __init__(self, *args: str) -> None:
        self._date: tuple[str] = args

# Function
def get_list(obj): 
    if hasattr(obj, 'ls_all'):
        return obj.ls_all()
    else:
        raise TypeError('object without "ls_all" method is not supported')

if __name__ '__main__':
    # All objects
    lob = ListOfBook('book1', 'book2', 'book3')
    los = ListOfStudent('student1', 'student2', 'student3')
    lom = ListOfMusic('song1', 'song2', 'song3')

    for obj in [lob, los, lom]:
        print(get_list(obj))

    # Output
        #['book1', 'book2', 'book3']
        #['student1', 'student2', 'student3']
        #NotImplemented   
```

So, we are able to act on a collection of objects, independent of what class each come from.
So, having many objects, wherever they come from is not important. We call the same method from all these objects and each object will react differently depending on what it's designed to do.

#### Polymorphism with Inheritance
Create a base class and move all common attributes and method to the base class.

```python
# Base Class
class ListOfItemBase:
    def __init__(self, *args: str) -> None: # Packing and Unpacking Positional Argument
        self._data: tuple[str] = args
            
    def ls_all(self) -> list[str]:
        return list(self._data)

# Derived Classes
class ListOfBook(ListOfItemBase):
    pass
        
class ListOfStudent(ListOfItemBase):
    pass
    
class ListOfMusic(ListOfItemBase):
    def ls_all(self):
        return NotImplemented # Indicates that the method has not been implemented

if __name__ '__main__':
    # All objects
    lob = ListOfBook('book1', 'book2', 'book3')
    los = ListOfStudent('student1', 'student2', 'student3')
    lom = ListOfMusic('song1', 'song2', 'song3')

    for obj in [lob, los, lom]:
        print(get_list(obj))

    # Output
        #['book1', 'book2', 'book3']
        #('student1', 'student2', 'student3')
```

## Exercise 
Given that we have the objects `dog1`, `dog2`, `cat1`, `cat2`, `bird` which are generated from the classes `Dog`, `Cat` and `Bird`. Given that all these classes inherit an abstract based class `Animal`. 

Base on the example code below, determine what the `abstract method` will be, then;
- Define the abstract method in the abstract based class. 
- Construct all the concrete classes and make the code below to work properly.

```python
pets_list: list[Dog | Cat | Bird] = [dog1, dog2, cat1, cat2, bird]

for pet in pets_list:
    pet.speak() # this should print how the different pet speaks. For example 'bark', 'meow', etc.
```

## Operator Overloading

> It is when an operator can behave different base on the operands

```python
# operand operator operand
2 + 5
```

```python
# The different behaviors here are: `Addition`, and `Concatenation`
2 + 5 # Addition
'hello ' + ' world' # Concatenate
```

Example of Operators in Python: `+`, `-`, `/`, `*`, `//`

Python uses `Magic methods`(`Special methods`, `dunder methods`) to implement Operators.

**Syntax**: 

```python
__<name>__()
```

```python
x = 4
y = 6

x + y # x.__add__(y)
```


## + Operator

- The dunder method that handles the `+` operator comes in three types: 
    - `__add__`
    - `__radd__`
    - `__iadd__`

```python
x = 4
y = 6

x + y # x.__add__(y)
x + 10  # x.__add__(10)
10 + x #  # x.__radd__(10)
x += 10 # x.__iadd__(10)
```

If we define a class `A`, would it support addition???

```python
class A:
    def __init__(self, item: int):
        self._item = item
if __name__ '__main__':
    a1 = A(4)
    a2 = A(5)

    a1 + a2 # Answer will be `No, it won't support`
```

For class `A` to support the addition operator, we must define the `__add__` method

```python
class A:
    def __init__(self, item: int):
        self._item = item
        
    def __add__(self, x):
        if isinstance(x, int):
            return self._item + x
        else:
            return self._item + x._item
        
    def __repr__(self):
        return f'{self._item}'

if __name__ '__main__':
    a1 = A(4)
    a2 = A(5)

    a1 + a2 # Now, it supports and answer will be '9'
```

## Exercise
Solve the exercise below

```python
class A:
    def __init__(self, item: int):
        self._item = item
        
    def __add__(self, x):
        if isinstance(x, int):
            return self._item + x
        else:
            return self._item + x._item
        
    def __repr__(self):
        return f'{self._item}'

if __name__ '__main__':

    a1 = A(12)
    a2 = A(6)

    #TODO:  Investigate the different dunder methods to achieve the following

    # Minus
    print(a1 - a2) # 6
    print(a1 -= 3) # a1 = 3
    print(4 - a1) # 1

    # Multiplication
    print(a1 * a2) # 18
    print(a1 * 3) # 9
    print(3 * a1) # 9
    print(a1 *= 5) # a1 = 15

    # Division
    print(a1 / a2) # 2.5
    print(a1 / 4) # 3.75
    print(a1 /= a2) # a1 = 2.5

    # Comparison
    print(a1 == a2) # False
    print(a1 > a2) # False
    print(a1 < 5) # True
    print(a1 != a2) # True
```