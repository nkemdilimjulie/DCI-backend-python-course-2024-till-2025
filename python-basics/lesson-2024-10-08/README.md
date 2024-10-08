# Basic OOP 

### Wednesday - 2024-10-02
- Inheritance
- Method Overriding
- Visibility (Access Modifiers)
- [Exercise](https://classroom.github.com/a/wBtJJAw4)


### Today - 2024-10-08
- Method Types
- Access Modifiers
- Getters and Setters (The Pythonic way)
- [Exercise](https://classroom.github.com/a/SYbX1DQS)


## Method Types

> A method is a function defined in a class


### Instance Method

>> Code can be found in `instance_method.py`

> Instance methods are methods that are bound to the object or class instance.

- Instance methods are methods that can be used to access or manipulate the content of an object.
- Instance methods can only be accessible via the object
- In order to be able to manipulate or access an object's content, we need the conventional `self`.
    - Instance methods takes in a compulsory first positional argument.
    
**When To Use?**

- When we want to access or manipulate the object's attributes or methods.

## Class Methods
>> Code can be found in `class_method.py`

> Class methods are methods that are bound to the class and not the object.


- Class methods can be accessed with or without creating the object.
- Class methods have the following properties
    - They are decorated: `@classmethod`
    - Takes in a mandatory first positional argument. Conventionally called; `cls`, stands for `class`.
    
**Example**: Let's build a method that will help us to create a person's object from their year of birth rather than their age.

**When to use?** When we want to create an object of that class from different configurations.

## Static Methods
>> Code can be found in `static_method.py`

> These are methods that are not bound to anything.

- Static methods are created with `@staticmethod`
- static methods done't require any specific first positional argument.
- Static methods can be access via the class and object
- They do not modify or access the object's or class attributes and methods because they are not bound to them.
- Static methods can easily be refactored into a function.

**Why static method**

- Static methods are useful in cases where you have a function, but it makes sense for it to be in the class either for readability or organization purposes.
- It also allows for method overriding. If it is a function, then there is no way to override it. The only way will be to move it into a class, and make it a static method.
- It acts as a helper function.

## Getters and Setters
>> Code can be found in `get_set_method.py`

Getters and Setters are as a result of `Encapsulation and Abstraction`

### Exercise
- Change the `last_name` to be private
- Build a getter method that will return the last name only if that last name was set. Else raise an exception
- Build the setter method  such that it sets the last name only when the name provided is greater than 2 characters. Else raise an exception.

### Self-Study
- How would you define `getters` and `setters` the Pythonic way using the `@property` decorator.

### Exercise after Self-Study
- Transform the `age` to be a protected attribute then
    - By using the Pythonic way, define `getters`, `setters` and even `deleters`  for the protected `age` attribute.
    - Think of conditions you'll like to have in the getters, setters and deleters, then implement them.