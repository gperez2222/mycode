#!/usr/bin/env python3

#Author: RZFeeser RZFeeser@alta3.com

"""Script to search for a pattern match"""

# used to walk the system
import os 

# for regex pattern matching
import fnmatch 

EXCLUDE = ["/usr", "/home", "/var"] ## Don't search in these locations

def find(pattern, path):

    """search through filesystem based on given path location"""

    result = []
    for root, dirs, files in os.walk(path, topdown=True):

        # if the root matches the exclude list
        if root in EXCLUDE: 

            # remove the directory list for this iteration
            dirs[:] = [] 

            # remove the file list for this iteration
            files[:] = [] 

        # always perform the nested loop, but it maybe empty
        for name in files: 

            # if match
            if fnmatch.fnmatch(name, pattern): 

                # add to our list
                result.append(os.path.join(root, name)) 

    return result # return the list

def main():

    """runtime code"""

    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    lookwhere = input("What is the path in which I should search? ")

    # call function
    print("Results: ", find(lookfor, lookwhere)) 

main()

