import os

from src.count_code import code_counter


def main():
    path = "src"

    count = code_counter(path)

    print(f"{path}: {count}")


if __name__ == "__main__":
    main()

# 8
