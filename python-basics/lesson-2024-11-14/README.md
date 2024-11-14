# Python Basic Tools and Libraries

## Wednesday - 2024-11-13
**NB**: PDF notes on this submodule is in the previous lesson

- Revision of yesterday's exercises
- CLi with argparse
- argparse argument types(positional and optional arguments)
- Adding arguments and options
- Set default values to arguments using;
    - `nargs`
    - `default`
- Add description to our CLI project
- Refactor a minimal CLI with argparse

### Exercise
Modify the code above to achieve the following

#### Ex1: Argument
We should be able to call our program with zero or more arguments. If for example 2 arguments are provided, then the result should look like what the Unix command will display.

#### Ex2: Option
Investigate the unix `ls` command with `ls -h` and select an option of your choice, understand its behavior and implement the same in this program.

#### Ex3: Code Count app
Modify the code count app such that we can 
- Specify the folders and files to check when running the command
- Provide an option to determine if test files should be considered or not. Call it `-t` and `--test`.

```python
python3 -m code_count -t src tests 
```

#### Ex4: From git classroom
- Last question on [Python Introduction argument parsing](https://classroom.github.com/a/EB-95CY_)


## Today - 2024-11-14
- Understanding differences between Scripts and Modules in Python
- The use of `__name__` and the different values it can hold
- Namespaces in Python
    - The Different namespaces in Python and how they differ
    - Demonstrating the `LEGB rule` with `ChainMap` from `collections
- Modular programming and why it is important
- import statements
    - Different ways to import
    - Different ways to run a python script when import is involved
    - Conclusion on the best way to import and run a Python script.

### Exercises
- [Python Basic Tools and Libraries Modules and Import](https://classroom.github.com/a/gk3Lc6uJ)
    - The first part on `modules and imports` is mandatory
    - The second part on `virtual environment` is optional and requires `self-study`
