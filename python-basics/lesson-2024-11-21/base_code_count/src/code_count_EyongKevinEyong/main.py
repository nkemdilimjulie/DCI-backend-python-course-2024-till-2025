import argparse
from pathlib import Path

from .count_code import code_counter
from .version import __version__


def main():
    parser = argparse.ArgumentParser(
        description="Count code statements in python files"
    )

    parser.add_argument("paths", nargs="*", default=["."])
    parser.add_argument(
        "-a", "--all", action="store_true", help="list all, including hidden"
    )
    parser.add_argument(
        "-v", "--version", action="store_true", help="version of the program"
    )

    args = parser.parse_args()

    if args.version:
        print("Version: ", __version__)

    for path in args.paths:
        abs_path = Path.cwd() / path

        count = code_counter(abs_path)
        print(f"{path}: {count}")


if __name__ == "__main__":
    main()

# 8
