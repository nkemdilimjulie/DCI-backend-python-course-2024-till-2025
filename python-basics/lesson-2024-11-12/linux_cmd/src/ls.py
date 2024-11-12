import sys

# import os
from pathlib import Path

# python linux_cmd/src/ls.py
# When we run the program without an argument, the current working directory is considered.
# if len(sys.argv) == 1:
#     path = Path('.') # Path.cwd()
path = Path(".")

# python linux_cmd/src/ls.py src
# When an argument(directory) is given, it will list all contents of that directory

# TODO: Modify to handle multiple arguments.
if len(sys.argv) == 2:
    path = Path(sys.argv[1])  # Path.cwd() / sys.argv[1]

# TODO: Check if it is a directory, if not, print an error message.

for entry in path.iterdir():
    item = entry.name
    # We will exclude hidden files and folders by default.
    if not item.startswith("."):
        # TODO: Print three items per column
        print(entry, end=" ")

else:
    print("")
