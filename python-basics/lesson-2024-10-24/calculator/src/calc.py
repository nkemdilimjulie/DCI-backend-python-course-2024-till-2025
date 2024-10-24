class MathematicalError(ValueError, TypeError):
    pass


class NotBinaryError(ValueError):
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


class BinaryConverter:
    def __init__(self):
        self.accepted_binary = "01"

    def convert_to_decimal(self, binary: str):
        try:
            return int(binary, base=2)
        except ValueError:
            raise NotBinaryError


def addition(*args):
    total = 0
    for value in args:
        total += value
    return total


def multiply_2(numb1, numb2):
    total = 0
    for _ in range(numb2):
        total = addition(total, numb1)
    return total


def ask_username():
    name = input("Enter your name: ")
    return name
