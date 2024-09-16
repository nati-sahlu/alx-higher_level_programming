#!/usr/bin/python3
# Function to check divisibility by 2 for each element in a list

def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]
