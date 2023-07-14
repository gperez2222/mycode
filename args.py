#!/usr/bin/env python3

import sys

def display_args():
    for i in range(1, len(sys.argv)):
        print(f"value: {sys.argv[i]}")
        #print('argument:', i, 'value:', sys.argv[i])

def main():
    display_args()

main()
