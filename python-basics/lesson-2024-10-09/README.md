# Advanced OOP 

### Tuesday - 2024-10-08
- Method Types
- Access Modifiers
- Getters and Setters (The Pythonic way)
- [Exercise](https://classroom.github.com/a/SYbX1DQS)


### Today - 2024-10-09
- Abstract Based Classes
- [Exercise](https://classroom.github.com/a/EjQfhvF3)

#### Self-Study
- Polymorphism
- Operator Overloading

## Abstract Based Classes
The class `Vehicle` is a parent class that contain methods common to all vehicles.

The class `Car` is a child class that inherit the parent class.

```python
# Parent class

class Vehicle:
    def horse_power(self) -> str:
        ... # Eclipsis
        
    def wheels_count(self) -> int:
        ...
        
    def cylinder_count(self) -> int:
        ...
    
# Child class

class Car(Vehicle):
    def horse_power(self) -> str:
        return '200hp'
    
    def wheels_count(self) -> int:
        return 4
    
    def cylinder_count(self) -> int:
        return 2

if __name__ == '__main__':
    vehicle = Vehicle()
    vehicle.horse_power()
```

We want to prevent the creation of objects from the Vehicle class.

### How to build an abstract based class?
We have import `ABC` and `abstractmethod` from `abc`.
- `ABC` -> It should be inherited
- `abstractmethod` -> It should be used as a decorator, and it will transform a method into an abstract method.

**NB**: What makes a class an abstract based class?????

- It has to inherit the `ABC`
- It needs to have at least one abstract method

> Abstract methods are methods that do not provide implementation of their own.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def horse_power(self) -> str:
        ...
        
    @abstractmethod
    def wheels_count(self) -> int:
        ...
        
    @abstractmethod
    def cylinder_count(self) -> int:
        ...

if __name__ == '__main__':
    vehicle = Vehicle()

# output
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[11], line 1
# ----> 1 vehicle = Vehicle()

# TypeError: Can't instantiate abstract class Vehicle with abstract methods cylinder_count, horse_power, wheels_count
```

If a class inherit the abstract based class

```python
# Child class
class Car(Vehicle):
    pass
```
- It also inherits the `ABC` by default. We can verify with `mro`

```python
Car.__mro__ # (__main__.Car, __main__.Vehicle, abc.ABC, object)
```

- It also inherit all the abstract methods from the parent. We can verify with `dir`

```python
# This should display all the methods of this class
dir(Car)
```

#### Concrete Class
> A concrete class is a class that inherit an abstract based class, but overrides all the parent's abstract methods.

> A concrete class is a subclass that inherit an abstract based class, but doesn't have any abstract method.

```python
# Child class

# Concrete Class
class Car(Vehicle):
    def horse_power(self) -> str:
        return '200hp'
    
    def wheels_count(self) -> int:
        return 4
    
    def cylinder_count(self) -> int:
        return 2

if __name__ == '__main__':
    BMW = Car() # instantiation is now possible.
```

## Abstract Methods with Parameters
When overriding an abstract method that has parameters, we may nor may not provide those parameters and Python will still work fine. This is because;

> If it walks and quacks like duck, then it is a duck

Let's define the `drive` method below.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def horse_power(self) -> str:
        ...
        
    @abstractmethod
    def wheels_count(self) -> int:
        ...
        
    @abstractmethod
    def cylinder_count(self) -> int:
        ...
        
    @abstractmethod
    def drive(self, distance: int) -> str:
        return f'Drive {distance} km'

# Child class
# Concrete Class
class Car(Vehicle):
    def horse_power(self) -> str:
        return '200hp'
    
    def wheels_count(self) -> int:
        return 4
    
    def cylinder_count(self) -> int:
        return 2
    
    def drive(self) -> str:
        # If you want to call the parent method, then you have to provide arguments for all parameters
        return super().drive(40)

if __name__ == '__main__':
    car = Car()
    car.drive() # Drive 40 km
```

## Property
> A method is a property if it can be called without the parenthesis

- It must be decorated with `property`.

```python
class T:
    @property
    def test(self):
        return 1

if __name__ == '__main__':
    obj = T()
    # since it is a property, we don't need the parenthesis
    obj.test # 1
```

## Abstract Property

> When combining the `@abstractmethod` with any other decorators, make sure the `@abstractmethod` decorator is closest to the method.

Let's define the abstract property `year`

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def horse_power(self) -> str:
        ...
        
    @abstractmethod
    def wheels_count(self) -> int:
        ...
        
    @abstractmethod
    def cylinder_count(self) -> int:
        ...
        
    @abstractmethod
    def drive(self, distance: int) -> str:
        return f'Drive {distance} km'
    
    @property
    @abstractmethod
    def year(self) -> int:
        ...
```

**NB**: How do we override an abstract property?????
- We can override with a method (**Not Logical**)
- We can override with a property
- We can override with a class attribute.

#### Override with a property

```python
# Child class

# Concrete Class
class Car(Vehicle):
    def horse_power(self) -> str:
        return '200hp'
    
    def wheels_count(self) -> int:
        return 4
    
    def cylinder_count(self) -> int:
        return 2
    
    def drive(self) -> str:
        # If you want to call the parent method, then you have to provide arguments for all parameters
        return super().drive(40)
    
    @property
    def year(self) -> int:
        return 2024

if __name__ == '__main__':
    car =Car()
    car.year # 2024
```

#### Override with a class attribute
```python
# Child class

# Concrete Class
class Car(Vehicle):
    year = 2024
    
    def horse_power(self) -> str:
        return '200hp'
    
    def wheels_count(self) -> int:
        return 4
    
    def cylinder_count(self) -> int:
        return 2
    
    def drive(self) -> str:
        # If you want to call the parent method, then you have to provide arguments for all parameters
        return super().drive(40)

if __name__ == '__main__':
    car =Car()
    car.year # 2024
```

### Self-study
Create abstract method that are also
- Static methods
- Class methods


## Summary

#### Abstract class
> It is a class that inherit `ABC` and have at least one `abstract method`. And `can't be instantiated`

#### Abstract Method
> An abstract method is a method that doesn't contain implementation of it self, and it is defined with the `@abstractmethod` decorator.

#### Concrete Method
> It is a subclass that inherit an abstract based class, and provides implementation of all abstract methods.

## Exercise

- Create an abstract based class called `Bank`, with the following abstract methods
    - loan
    - debit

- You should also provide the the abstract property `credit`
- Create at least one `concrete` class that will inherit the `Bank`. The name of the concrete class should be any local bank in your area.
- Provide implementation of each of the abstract methods and properties by simply printing if the bank provide the respective services. For example. In the `load` method, we will print `Loan service available`.

### Solution

```python
from abc import ABC, abstractmethod
# Abstract class: Bank
class Bank(ABC):
    @abstractmethod
    def loan(self):
        ...
        
    @abstractmethod
    def debit(self):
        ...
        
    @property
    @abstractmethod
    def credit(self):
        ...
    
# Concrete class: Local bank
class UBA(Bank):
    #credit = 'Credit service Unavailable'
    
    def loan(self):
        print('Loan service available')
    
    def debit(self):
        print('Debit service available')
        
    @property
    def credit(self):
        print('Credit service Unavailable')

if __name__ == '__main__':
    bank = UBA()
    print(bank.credit) # Credit service Unavailable
    print(bank.loan()) # Loan service available

    print(bank.debit()) # Debit service available
```

## Bonus

At times we don't know if a class is an abstract based class or a concrete class.

- Check the class with `dir()`. For example `dir(Bank)` and check the first attribute `__abstractmethods__`
- if this attribute is an empty frozenset, then it is `Concrete Class`

```python
UBA.__abstractmethods__ # frozenset()
```

- If this attribute is not an empty frozenset, then it is an `Abstract Based Class`.
```python
Bank.__abstractmethods__ # frozenset({'credit', 'debit', 'loan'})
```

## Self-study
- Polymorphism
- Operator Overloading

