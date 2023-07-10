#!/usr/bin/env python3

proto = ["ssh", "http", "https"]

print(proto)
print(proto[1])

"""The take away here is that the list method, list.extend() iterates over whatever it was passed, where each iteration 
   becomes a new entry at the end of the list. This is a great method for combining two lists into a single list. 
   Let's demonstrate that in the next script."""

proto.extend("dns") # this line will add d, n, and s
print(proto)

