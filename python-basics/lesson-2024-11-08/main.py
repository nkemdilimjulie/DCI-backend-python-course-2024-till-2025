from pathlib import Path

current_file = Path(__file__)
dir_of_current_file = current_file.resolve().parent
print(dir_of_current_file)
