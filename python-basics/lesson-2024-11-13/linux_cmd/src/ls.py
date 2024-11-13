import argparse
from pathlib import Path

# Create argument parser object
parser = argparse.ArgumentParser(description="list content of a directory")

# Add arguments or options to the parser object
# nargs = *, +, ?
parser.add_argument("path", nargs="?", default=".")
parser.add_argument("-a", "--all", action="store_true")

# Access arguments or options
args = parser.parse_args()

## Access specific arguments
path = Path(args.path)

# Add CLI login
if not path.exists():
    print("No such file or directory")
    exit(1)
# TODO: Add the current(.) and parent directory(..)
for entry in path.iterdir():
    item = entry.name
    # TODO: Check if the short option holds the boolean value
    if args.all:
        print(item, end="\t")
    else:
        if not item.startswith("."):
            print(item, end="\t")
else:
    print("")
