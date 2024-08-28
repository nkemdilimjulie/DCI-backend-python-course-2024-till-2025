## Yesterday - 2024-08-27

* Try & Except 
* Function definition/benefits
* Create function/structure
* Input arguments/return values
* Call/use function
* Exercises

## Today - 2024-08-28

* Understanding scope
* Reference a function
* Assign function to a variable
* Using function as argument
* Exercises


### **1. Understanding Scope in Python**

#### **What Is Scope?**
Scope refers to the region in a Python program where a variable is accessible. It defines the visibility and lifetime of variables, and Python has different levels of scope to manage variable accessibility.

#### **Types of Scopes:**
1. **Local Scope:**
   - Variables declared inside a function are in the local scope.
   - These variables are only accessible within the function.

2. **Enclosing Scope:**
   - Refers to the scope of a nested function. If a function is defined within another function, the outer function’s variables are in the enclosing scope.

3. **Global Scope:**
   - Variables declared outside of any function are in the global scope.
   - These variables can be accessed throughout the module.

4. **Built-in Scope:**
   - This is the outermost scope that includes built-in functions and variables in Python, like `print()`, `len()`, etc.