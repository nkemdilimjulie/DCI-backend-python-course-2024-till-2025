## Yesterday - 2024-09-18

* Searching Algorithms
    - Linear search
    - Binary search
* Exercise

## Today - 2024-09-19

* Introduction to debugging in Python
* Importance of debugging
* How to debug code using `pdb`
* Using an `IDE` to debug Python code
* Exercise

### Debugging in Python

Debugging is a critical process in software development that involves identifying and resolving bugs (errors) in your code. Bugs can be logical errors, runtime errors, or unexpected behavior that causes the program to malfunction. In this lesson, we'll cover the importance of debugging, how to interpret a StackTrace, and how to use debugging tools like **pdb** and an Integrated Development Environment (IDE).

### 1. Understanding Debugging and Its Importance

**Debugging** is the process of finding and resolving defects in a program's code that prevent it from behaving as expected. Without proper debugging, even minor errors can cause a program to fail, leading to inefficient code execution, incorrect results, or system crashes.

#### Importance of Debugging:
- **Improves Code Quality**: By identifying and fixing bugs, debugging ensures that the program works as intended and meets the required standards.
- **Enhances Performance**: Debugging helps to locate performance bottlenecks in your code, optimizing it for speed and resource usage.
- **Minimizes Crashes**: Resolving errors early in the development cycle reduces the chances of the application crashing or causing major problems later.
- **Enhances Developer Understanding**: Debugging deepens the developer’s understanding of how the code behaves under different conditions.


### 2. Interpreting a StackTrace

A **StackTrace** (also called traceback in Python) is a report of the active function calls in a program leading up to an error. It’s an invaluable tool for debugging as it shows the exact sequence of code execution when the error occurred.

#### Example of a StackTrace:
```python
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    result = divide(10, 0)
  File "main.py", line 6, in divide
    return a / b
ZeroDivisionError: division by zero
```

#### How to Read a StackTrace:
1. **Traceback**: Indicates that an error occurred and gives details about where the error happened.
2. **File path and line number**: Shows the specific file and line of code where the error occurred (`main.py, line 10`).
3. **Function calls**: Indicates the function call that led to the error (`divide(10, 0)`).
4. **Error message**: The final line provides the type of error and additional details (`ZeroDivisionError: division by zero`).

#### Practical Use of StackTrace:
The StackTrace guides the developer to the exact location in the code that caused the error, enabling them to fix the issue quickly.

### 3. Using the Python Debugger (pdb)

**pdb** is Python’s built-in debugger. It allows you to set breakpoints, step through code line by line, and inspect variables to track down bugs.

#### Key pdb Commands:
- **`b`**: Set a breakpoint at a specific line. Example: `b 10` sets a breakpoint at line 10.
- **`c`**: Continue execution until the next breakpoint or program termination.
- **`n`**: Execute the next line of code, but don't step into function calls.
- **`s`**: Step into a function call.
- **`q`**: Quit the debugger.
- **`p`**: Print the value of a variable. Example: `p var_name`.

```python
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
```

#### How to Debug with pdb:
1. **Run the program**: Execute your script as normal. When it reaches the `pdb.set_trace()` line, the debugger will pause execution.
2. **Inspect variables**: Use the `p` command to print the values of variables and understand their state.
3. **Step through the code**: Use the `n` or `s` commands to proceed through the code and observe its behavior.
4. **Fix the bug**: Once you've identified the issue, fix it and rerun the program.