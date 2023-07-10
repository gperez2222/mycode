#!/usr/bin/env python3

my_list = ["Willy", 2 , 3.14, [5, 3, "mango"]]

print(my_list[3][2][:3])

name = "Willy"

print(name[0:3])

other_list = ["Joe", "Jim", "Larry", "Gus"]

other_list2 = ["Brad"]

new_list = other_list + other_list2

## Method is a function that is associate with a data type (CLASS)

## .extend is used to iterate through the data type and append it 
## while .append will take the item and append it

new_list.append("Dan")

print(new_list)

