#!/usr/bin/python3
"""Exploring imports"""

import file1

def main():
    file1.main()
    print("I am file2, and the value of __name__ is: ", __name__)

if __name__ == "__main__":
    main()
