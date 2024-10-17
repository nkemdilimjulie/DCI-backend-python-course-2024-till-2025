# Advanced OOP - Design Patterns

### Tuesday - 2024-10-15
- Building the Dice Game

### Today - 2024-10-16
- Design Patterns
- Properties of design patterns
- Taxonomy of Design patterns
- Categories of design pattern
- Case: Singleton
- [Exercises](https://classroom.github.com/a/TlG5EJ8R)

# Design Patterns
> Instead of code reuse, with patterns we get experience reuse

## Properties of design pattern
- They are language-independent.
- They are time-tested, well-proven and well-known and many experts in the software industry agree with them.
- They introduce a clever way to solving problems
- They are dynamic, meaning new design patterns are been discovered now and then.
- They are highly customizable
- They are solutions to known issues.

## Taxonomy of Design Pattern

### Snippet 
This is usually code in some programming language for a specific purpose

### Design
A design is a code snippet that solve a specific problem

### Pattern
This is a design that is well-proven, time-tested, scalable.

### Definition

Design Patterns are time-tested, well-proven development paradigms or code that offers a clever, structured approach to solving common programming problem

## Design Pattern Categories
### Creational Pattern
Design patterns in this category governs the creation of objects of a class.

### Structural Pattern 
Design patterns in this category governs the assembling of objects and classes into larger structures for flexibility and efficiency

### Behavioral Pattern
Design patterns in this category governs the effective communication and the assignment of responsibilities between objects.

## Creational Pattern
### Singleton Pattern
> It provides a mechanism to have one and only one object of a given class.

#### Use Cases
- In databases, you want to have only one instance of the database to write to that database for data consistency.
- In your country, you will always have one and only one valid ID

```python
class A:
    pass 

a1 = A()
a2 = A()
a3 = A()

print(a1) # <__main__.A object at 0x110936910>
print(a2) # <__main__.A object at 0x110937650>
print(a3) # <__main__.A object at 0x110937310>

# compare identity 
print(a1 is a2)  # False
# compares value
print(a2 == a3)  # False

# Recommended. use id()
id(a1) == id(a2) == id(a3)
```

### Dunder methods to understand
- `__init__`: Object initialization (initialize object's attributes)
- `__new__`: Class Instantiation (create objects)

#### Focusing on `__new__` only

```python
class OnlyOne(object):
    # class attribute
    __instance = None 

    def __new__(cls): # It is by definition a class method
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

obj1 = OnlyOne()
obj2 = OnlyOne()
id(obj1) == id(obj2) # True
```

## Focusing on `__new__` and `__init__`

```python
class OnlyOne(object):
    # class attribute
    __instance = None 

    def __new__(cls, x): # It is by definition a class method
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    def __init__(self, x):
        self.x = x

obj1 = OnlyOne(1)
obj2 = OnlyOne(0)
id(obj1) == id(obj2) # True

# Our singleton maintains the last argument passed to the class.
print(obj1.x) # 0
print(obj2.x) # 0
```

## Maintian the object and it's attribute's value

```python
class OnlyOne(object):
    # class attribute
    __instance = None 

    def __new__(cls, x): # It is by definition a class method
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__new_init(x)

        return cls.__instance
    
    def __new_init(self, x):
        self.x = x

ob1 = OnlyOne(1)
ob2 = OnlyOne(0)
# Now, the very first argument passed to the class is maintained.
print(ob1.x) # 1
print(ob2.x) # 1
```

## Singleton and Metaclass

- `__call__`
    - `__new__`
    - `__init__`

### Create our singleton metaclass 
- A class is a metaclass if it inherits `type`.
- A metaclass can't be instantiated, it can only be used as a metaclass.
- To transform a class into a singleton, we just assign that singleton metaclass to the `metaclass` attribute of the class.

```python
# How do we create a metaclass
# Just inherit 'type'
class MetaSingleton(type):
    __instance = None 

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance
```

```python
# assign our new singleton metaclass to the 'metaclass' parameter
class OnlyOne(metaclass=MetaSingleton):
    def __init__(self, x):
        self.x = x
```

```python
obj1 = OnlyOne(4)
obj2 = OnlyOne(0)

id(obj1) == id(obj2) # True

# The metaclass singleton maintains the first argument
print(obj1.x) # 4
print(obj2.x) # 4
```
