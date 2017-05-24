"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator():
    """Calculates basic math operations using prefix notation"""
    while True:
        user_input = raw_input('> ')
        tokenized_input = user_input.split(' ')
        if tokenized_input[0] == 'q':
            print 'Goodbye!'
            break
        elif tokenized_input[0] == '+':
            add_function = add(int(tokenized_input[1]), int(tokenized_input[2]))
            print add_function
        elif tokenized_input[0] == '-':
            subtract_function = subtract(int(tokenized_input[1]), int(tokenized_input[2]))
            print subtract_function
        elif tokenized_input[0] == '*':
            multiply_function = multiply(int(tokenized_input[1]), int(tokenized_input[2]))
            print multiply_function
        elif tokenized_input[0] == '/':
            divide_function = divide(int(tokenized_input[1]), int(tokenized_input[2]))
            print divide_function
        elif tokenized_input[0] == 'square':
            square_function = square(int(tokenized_input[1]))
            print square_function
        elif tokenized_input[0] == 'cube':
            cube_function = cube(int(tokenized_input[1]))
            print cube_function
        elif tokenized_input[0] == 'pow':
            power_function = power(int(tokenized_input[1]), int(tokenized_input[2]))
            print power_function
        elif tokenized_input[0] == 'mod':
            mod_function = mod(int(tokenized_input[1]), int(tokenized_input[2]))
            print mod_function

calculator()
