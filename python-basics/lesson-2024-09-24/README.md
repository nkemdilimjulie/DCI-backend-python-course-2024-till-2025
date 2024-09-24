## Thursday - 2024-09-19

* Introduction to debugging in Python
* Importance of debugging
* How to debug code using `pdb`
* Using an `IDE` to debug Python code
* Exercise

## Today - 2024-09-24

* Using context variables in `pdb`
* Using conditional breakpoint to debug Python code
* What is stackframe and how to interpret it
* Exercise


### Conditional Breakpoints

**Conditional breakpoints** pause the program only when a certain condition is met, unlike regular breakpoints that always pause the execution. This is particularly useful when debugging loops or handling complex data structures where the issue only arises under specific conditions.

```bash
b <line_number>, <condition>
# or
b <file_name>:<line_number>, <condition>

```

Example (debug.py):
```python
def find_number(lst, target):

    for i, num in enumerate(lst):
        if num == target:
            return i
        
    return -1

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = 50

print(find_number(numbers, x))
```
```bash
b debug.py:33, num == 70
```

### Understanding Stack Frames and How to Inspect Them

A **stack frame** represents the state of a function (or method) at a specific point during its execution. Each function call creates a new stack frame, and when an error occurs or debugging is paused, you can inspect the current stack frame and those of previous calls to trace the flow of execution.

#### What is a Stack Frame?
- Every time a function is called, it is added to the **call stack**, which keeps track of active function calls.
- A **stack frame** contains information like local variables, arguments passed to the function, and the location in the code where the function was called.
- When a function completes execution, its stack frame is removed from the call stack.

```python
# Stack Frames

def outer():
    var_out = 20
    return inner()


def inner():
    var_in = 300
    return 'It is lunch time.'

print(outer())
```


In this case:
- The `outer()` function is called first, creating a stack frame for `outer`.
- Then, `inner()` is called from `outer()`, creating a new stack frame for `inner`.
- After `inner()` completes, its frame is popped from the stack, and control returns to `outer()`.

#### Inspecting Stack Frames in `pdb`:

- **Where (w)**: Shows the current position in the stack.
- **Up (u)**: Move up one frame (to the caller function).
- **Down (d)**: Move down one frame (to the callee function).