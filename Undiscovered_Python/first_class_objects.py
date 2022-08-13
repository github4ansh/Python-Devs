import math
import subprocess


def print_function(func):
    first_num = 2
    second_num = 3
    print(func(first_num, second_num))


def sum_of_two_numbers(*args):
    return f'sum of two numbers {args[0]} and {args[1]} is: {sum(args)}'


first_run = sum_of_two_numbers
print_function(first_run)
