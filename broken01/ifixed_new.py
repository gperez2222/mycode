#!/usr/bin/env python3

import re

# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

min=3
calc1 = 0.0
calc2 = 0.0
operation = ""
operators = ["+","-","*","/"]

def main():
    math_input()

def arithmath(calc1,operation,calc2):

    if operation == '+':
        total = calc1 + calc2
        print(f"\n {str(calc1)}  {operation}  {str(calc2)}  = {total}")
    elif operation == '-':
        total = calc1 - calc2
        print(f"\n {str(calc1)}  {operation}  {str(calc2)}  = {total}")
    elif operation == '*':
        total = calc1 * calc2
        print(f"\n {str(calc1)}  {operation}  {str(calc2)}  = {total}")
    elif operation == '/':
        total = calc1 / calc2
        print(f"\n {str(calc1)}  {operation}  {str(calc2)}  = {total}")
    else:
        print("\n Not a valid entry. Restarting...")

def raw_input():
    value = input()
    #if re.match(r'^[A-z]+', value):

    if value.isalpha():
        return "q"
    elif value.isdigit():
        return float(value)
    elif value in operators:
        return value
    else: 
        return "q"

#def math_input():

while (calc1 != "q" and calc2 != "q"):

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

            if operation in operators and calc1 != "q" and calc2 != "q" and min >= 3:
                    arithmath(float(calc1),str(operation),float(calc2))

""" Script starts here"""

#main()

