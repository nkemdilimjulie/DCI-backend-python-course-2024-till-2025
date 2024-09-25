## Yesterday - 2024-09-24

* Using context variables in `pdb`
* Using conditional breakpoint to debug Python code
* What is stackframe and how to interpret it
* Exercise


## Today - 2024-09-25

* Concepts of OOP (Object Oriented Programming)
* Overview of the principles of OOP
* Differences between classes and objects
* Class members and instance members
* Attributes and methods in OOP
* Exercise

### Object-Oriented Programming Basics

#### 1. **Understanding Object-Oriented Programming (OOP)**

Object-Oriented Programming (OOP) is a programming paradigm that focuses on using "objects" to model real-world entities or concepts. This approach allows developers to encapsulate data (attributes) and functionality (methods) together in a single structure.


#### Key Features of OOP:
- **Encapsulation**: Bundling data and methods that operate on that data within a class.
- **Inheritance**: Allowing new classes to inherit properties and methods from existing ones.
- **Polymorphism**: Ability to treat different objects in a similar way based on a shared interface.
- **Abstraction**: Hiding complex implementation details and exposing only the necessary parts.

#### **Advantages of OOP**:
1. **Modularity**: OOP encourages writing self-contained objects, making your codebase more modular and easier to manage.
2. **Code Reusability**: Through inheritance and polymorphism, OOP allows code reuse, reducing redundancy.
3. **Scalability**: As programs grow larger, the clear structure of OOP makes it easier to scale and maintain.
4. **Maintainability**: With the modularity provided by OOP, fixing bugs or adding new features becomes easier without affecting the entire system.

#### 3. **Class vs Object: Key Differences**

In OOP, **classes** and **objects** are closely related but distinct concepts.

- **Class**:
  - A class is a blueprint or template for creating objects.
  - It defines the structure and behavior that the objects created from the class will have.
  - Example: Think of a class as a blueprint for a house.


- **Object**:
  - An object is an instance of a class.
  - Objects have states (data) and behaviors (methods) defined by their class.
  - Example: An object is like an actual house built from the blueprint.


### Class Members, Methods, and Attributes

- **Class Members**: These refer to all the variables and methods associated with a class. There are two types:
  1. **Instance Members**: Attributes and methods that belong to an instance (object) of the class.
  2. **Class Members** (or **Static Members**): Attributes and methods that belong to the class itself, not individual objects.

- **Attributes**: These are variables that store data related to a class or an object.
  - **Instance Attributes**: These are specific to an object, meaning each instance of the class has its own values for these attributes.
  - **Class Attributes**: These are shared across all instances of the class.

- **Methods**: These are functions defined inside a class that describe the behaviors of the objects. There are three kinds:
  1. **Instance Methods**: Operate on an instance of the class (i.e., the object).
  2. **Class Methods**: Operate on the class itself, and are usually defined using `@classmethod`.
  3. **Static Methods**: Utility methods that don’t access or modify class or instance data, and are defined using `@staticmethod`.
  








































































































































