from pathlib import Path

current_file = Path(__file__)

print(current_file)
print(current_file.resolve())
print(current_file.resolve().parent)
print(current_file.resolve().parent.parent)
