# Python Basic Tools and Libraries

## Tuesday - 2024-11-12
- Python Command Line Interface
    - Advantages and Disadvantages of CLI
    - CLI vs GUI
    - The sys module
    - Understanding Commands, Subcommands, Paramters(Arguments, Options)
    - Build a minimal CLI 
        - Creating a short program similar to the `ls` Linux command
### Exercises
- [Python Introduction argument parsing](https://classroom.github.com/a/EB-95CY_)
    - The first question is on `sys.argv` **To this**
    - The second question is on `getopt()`, **Self-study**
    - The second question is on `argparse`: **Skip this**
- Work on all `TODOs` of the Minimal CLI application

## Today - 2024-11-13
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
