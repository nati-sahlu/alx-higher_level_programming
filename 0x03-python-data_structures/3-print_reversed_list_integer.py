#!/usr/bin/python3
# Function to print all integers of a list in reverse order

def print_reversed_list_integer(my_list=[]):
    if my_list:  # Check if the list is not empty
        for i in reversed(my_list):  # Iterate through the list in reverse
            print("{:d}".format(i))  # Use str.format() to print each integer
