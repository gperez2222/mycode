#!/usr/bin/env python3

import re

# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

## Had to make the list global
operators = ["+","-","*","/"]

def main():
    calc1 = 0.0
    calc2 = 0.0
    operation = ""
    while calc1 != "q" and calc2 != "q":

            print("\nWhat is the first operator? Or, enter q to quit: ", end="")
            calc1 = raw_input()
            if calc1 == "q":
                print(f"Exiting ..\n")
                break
     
            print("\nWhat is the second operator? Or, enter q to quit: ", end="")
            calc2 = raw_input()
            if calc2 == "q":
                print(f"Exiting ..\n")
                break
    
            print(f"Enter an operation to perform on the two operators {operators}: ", end="")
            operation = raw_input()

            if operation in operators and calc1 != "q" and calc2 != "q":
                    arithmath(float(calc1),str(operation),float(calc2))

def arithmath(calc1,operation,calc2):

    if operation == '+':
        total = float(calc1) + float(calc2)
        print(f"\n {str(calc1)}  {operation}  {str(calc2)}  = {total}")
    elif operation == '-':
        total = float(calc1) - float(calc2)
        print(f"\n {str(calc1)}  {operation}  {str(calc2)}  = {total}")
    elif operation == '*':
        total = float(calc1) * float(calc2)
        print(f"\n {str(calc1)}  {operation}  {str(calc2)}  = {total}")
    elif operation == '/':
        total = float(calc1) / float(calc2)
        print(f"\n {str(calc1)}  {operation}  {str(calc2)}  = {total}")
    else:
        print("\n Not a valid entry. Restarting...")

    return None

def isfloat(value):
    # regular expression pattern to match valid float value
    pattern = r"^[-+]?[0-9]*\.?[0-9]+$"

    # Use re.match to check if the string matches the string pattern in value and returns a value object if there is a regular expression match, else None
    checkformatch = re.match(pattern, value)

    # Convert the match object to a boolean value and will eeturn True if there is a match, else False
    return bool(checkformatch)

def raw_input():
    value = input()

    if value.isalpha():
        return "q"
    elif value.isdigit() or isfloat(value):
        return float(value)
    elif value in operators:
        return value
    else: 
        return "q"

""" Script starts here"""

if __name__ == "__main__":
    main()
