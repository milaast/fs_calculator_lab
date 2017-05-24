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

calculator()
