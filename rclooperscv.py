#!/usr/bin/env python3
"""RZFeeser@alta3.com | Alta3 Research
   Using the CSV library to work with CSV data."""

import csv

with open("csv_users.txt", "r") as csvfile:
    #counter to create unique file names
    i = 0

    for row in csv.reader(csvfile):
        i = i + 1 # increase i by 1 (to create unique admin.rc file names)
        filename = f"admin.rc{i}"

        with open(filename, "w") as rcfile:
            # use the standard library print function to print our data
            # out to the open file open rcfile (open in write mode)
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)

print("admin.rc files created")
