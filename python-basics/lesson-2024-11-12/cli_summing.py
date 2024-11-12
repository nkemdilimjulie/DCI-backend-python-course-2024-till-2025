# TODO: Write a command line program that will print the following
# - The number of arguments
# - The name of the python module
# - The sum of all numeric arguments.

""" python cli_summing.py 1 2 3 4
# 5
# cli_summing.py
# 10
"""
import sys

args = sys.argv
number = len(args)
script_name = args[0]
sum_ = 0
for arg in args[1:]:
    sum_ += int(arg)

print(number)
print(script_name)
print(sum_)
