class MathematicalError(ValueError, TypeError):
    pass


def multiply(x, y):  # x = {'3': 5}
    try:
        if isinstance(x, str):
            x = int(x)  # ValueError
        if isinstance(y, str):
            y = int(y)  # ValueError
        return x * y  # TypeError
    except (TypeError, ValueError):
        raise MathematicalError("Not supported types or values")
