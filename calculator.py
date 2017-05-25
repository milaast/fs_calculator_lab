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
        tokenized_input = user_input.split()

            # for item in tokenized_input[1:]:
            #     int(item) and append it to original tokenized_input

        sliced_ti = int(tokenized_input[1:])
            # make each item on the list its own thing?? Assign each
            #to a different variable???
        tokenized_input[1:].append(sliced_ti)

        if tokenized_input[0] == 'q':
            print 'Goodbye!'
            break

        elif tokenized_input[0] == '+':
            add_function = add(tokenized_input[1], tokenized_input[2])
            print add_function

        elif tokenized_input[0] == '-':
            subtract_function = subtract(tokenized_input[1], tokenized_input[2])
            print subtract_function

        elif tokenized_input[0] == '*':
            multiply_function = multiply(tokenized_input[1], tokenized_input[2])
            print multiply_function

        elif tokenized_input[0] == '/':
            divide_function = divide(tokenized_input[1], tokenized_input[2])
            print divide_function

        elif tokenized_input[0] == 'square':
            square_function = square(tokenized_input[1])
            print square_function

        elif tokenized_input[0] == 'cube':
            cube_function = cube(tokenized_input[1])
            print cube_function

        elif tokenized_input[0] == 'pow':
            power_function = power(tokenized_input[1], tokenized_input[2])
            print power_function

        elif tokenized_input[0] == 'mod':
            mod_function = mod(tokenized_input[1], tokenized_input[2])
            print mod_function

calculator()
