import os

from src.count_code import code_counter, count_code_line


def main():
    path = "test.py"

    count = code_counter(path)

    print(f"{path}: {count}")


if __name__ == "__main__":
    main()
