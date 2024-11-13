# sys.argv
import sys
from pathlib import Path

# import os


args = sys.argv

if len(args) == 1:
    path = Path(".")

elif len(args) == 2:
    path = Path(args[1])

for item in path.iterdir():
    # item = ./src/tests/.test_add.py
    if not item.name.startswith("."):
        print(item.name, end="\t")
