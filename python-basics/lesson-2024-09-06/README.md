## Yesterday - 2024-09-05

* Using built-in `__name__` variable
* Fixing circular import
* Warehouse project collections
* Warehouse project Functions (continue)


## Today - 2024-09-06

* Concepts of Boolean logic
* Predicates in Logical expressions
* Truthy and Falsy values and how python interprets 
    non-boolean values
* Logical operators and their precedence
* Exercises


## 1. Understanding Boolean Logic

**Boolean Logic** deals with values that are either **True** or **False**. This is important when making decisions in code. Python has built-in support for Boolean values and logical operations, allowing you to create conditions that control the flow of your program.

### Key Boolean Operators:
- **AND** (`and`): Returns `True` if both conditions are `True`.
- **OR** (`or`): Returns `True` if at least one condition is `True`.
- **NOT** (`not`): Negates a Boolean value, i.e., `True` becomes `False` and vice versa.

### Operator Precedence:
- **NOT** has the highest precedence, followed by **AND**, and then **OR**.
- You can use parentheses `()` to group conditions and override the default precedence.

## 2. Understanding the Concept of Predicates

A **predicate** is a function or expression that returns a Boolean value (`True` or `False`). Predicates are widely used in filtering data, condition checking, and decision-making processes.

## Identifying Truthy and Falsy Values

In Python, any value can be used in a boolean context (such as an `if` statement). However, not all values are strictly `True` or `False`. Python evaluates them as either **Truthy** or **Falsy** based on their value.

- **Truthy** values are treated as `True` in a boolean context.
- **Falsy** values are treated as `False` in a boolean context.


### Common Falsy Values:

- `None`
- `False`
- `0` (for integers or floats)
- Empty sequences or collections (e.g., `[]`, `{}`, `()`, `''`)
- Objects of zero length (e.g., `len("") == 0`)
- Objects with a `__bool__()` method that returns `False`

### Common Truthy Values:
Everything that is not falsy is considered **truthy**.

- Non-zero numbers (e.g., `1`, `-5`, `3.14`)
- Non-empty collections (e.g., `[1, 2, 3]`, `{'key': 'value'}`)
- Non-empty strings (e.g., `"Hello"`, `' '`)


### Truth Table for Logical Operators:

| A     | B     | `A and B` | `A or B` | `not A` |
|-------|-------|-----------|----------|---------|
| True  | True  | True      | True     | False   |
| True  | False | False     | True     | False   |
| False | True  | False     | True     | True    |
| False | False | False     | False    | True    |


### Operator Precedence

Just like mathematical operators, logical operators in Python follow a certain **precedence** (or order of evaluation). This is important when you combine multiple conditions in a single expression.

1. **NOT** has the highest precedence.
2. **AND** has the next highest precedence.
3. **OR** has the lowest precedence.


### Using Parentheses to Override Precedence:

You can use parentheses to group logical expressions and control the order in which they're evaluated.

## 3. Short-Circuiting in Boolean Logic:

Python uses **short-circuit evaluation** in boolean expressions:
- For the `AND` operator, if the first condition is `False`, the entire expression is `False`, and Python doesn't evaluate the second condition.
- For the `OR` operator, if the first condition is `True`, Python returns `True` without checking the second condition.


































































































