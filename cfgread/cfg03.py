#!/usr/bin/env python3

## create file object in "r"ead mode

cnt = 0
newconfiglist = []

with open("vlanconfig.cfg", "r") as configfile:

    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

    for line in configlist:
        nline = line.strip("\n")
        print(nline)
        if "vlan" in nline:
            cnt += 1
        newconfiglist.append(nline)

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
#print(configlist)
print("The number of lines: ", len(configlist))
print("The number of lines: ", len(newconfiglist))
print(f"Total lines in the file: {cnt}")
print(newconfiglist)

