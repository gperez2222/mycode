#!/usr/bin/env python3

"""Willy Perez
   if, elif, else - A simple program using conditionals to make a decision."""

def main():
    print(find_score())

def find_score():
    score = int(input("Enter your scoring grade: "))
    message = 'Your score is '

    # if input value was higher or equal to 90
    if score >= 90:
        message = message + 'A'
    elif score >= 80 and score < 90:
        message = message + 'B'
    elif score >= 70 and score < 80:
        message = message + 'C'
    elif score >= 60 and score < 70:
        message = message + 'D'
    else:
        message = message + 'F'
    return(message)


""" The next if statement checks the value of __name__ and compares it to the string "__main__".
Python defines a special variable called __name__ that contains a string whose value depends on how the code is being used.

There are two primary ways that you can instruct the Python interpreter to execute or use code:
    You can execute the Python file as a script using the command line.
    You can import the code from one Python file into another file or into the interactive interpreter.

When the if statement evaluates to True, the Python interpreter executes main()."""

if __name__ == "__main__":
    main()
