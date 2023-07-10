#!/usr/bin/env python3

my_dict = {"Willy": ["Cuban", 57, "Cliffside Park"], "Gloria": ["Puerto Rican", 84, "West New Yorl"], "Jose Manuel": ["Spaniard", 62, "Union City"]}


print(my_dict)

print(my_dict["Willy"])

my_dict["Walter"] = ["Salvadorian", 54, "Bogota"]

print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

## del and .pop removes a Key:Value

del my_dict["Gloria"]

my_dict.pop("Jose Manuel")

print(my_dict)

name = my_dict.get("Joe")

print(name)

name = my_dict.get("Willy")

print(name)
