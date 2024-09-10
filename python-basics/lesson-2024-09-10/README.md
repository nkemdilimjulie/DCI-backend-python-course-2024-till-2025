## Friday - 2024-09-06

* Concepts of Boolean logic
* Predicates in Logical expressions
* Truthy and Falsy values and how python interprets 
    non-boolean values
* Logical operators and their precedence
* Exercises


## Today - 2024-09-10

* Interpreting truth tables
* Understanding complex logical operators (XOR, NAND, NOR, XNOR)
* Create complex expressions
* Exercises


### **1. Interpreting Truth Tables**

**What is a Truth Table?**
A truth table is a mathematical table used to determine the output of a logical expression based on all possible input combinations of True (1) or False (0) values. It’s widely used in digital circuits and boolean algebra to understand logical operations.

**Example: Truth Table for AND (`&&`) Operation**

| A (Input 1) | B (Input 2) | A AND B (Output) |
|-------------|-------------|-----------------|
| False       | False       | False           |
| False       | True        | False           |
| True        | False       | False           |
| True        | True        | True            |


### **2. Advanced Logical Operators**

Python’s standard library doesn’t directly support non-native logical operators like XOR, NAND, NOR, and XNOR, but you can implement these using combinations of existing Python operators (`and`, `or`, `not`, etc.).


#### **XOR (Exclusive OR)**
- **Definition:** Returns `True` if one, and only one, of the inputs is True. If both inputs are True or both are False, it returns False.


#### **NAND (Not AND)**
- **Definition:** Returns `True` if at least one of the inputs is False. Only returns `False` if both inputs are True.


#### **NOR (Not OR)**
- **Definition:** Returns `True` if both inputs are False. Otherwise, it returns `False`.


#### **XNOR (Exclusive NOR)**
- **Definition:** Returns `True` if both inputs are the same (either both True or both False).





















































































