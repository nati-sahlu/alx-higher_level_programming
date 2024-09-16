#!/usr/bin/python3
# Function to delete an item at a specific index in a list

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        return my_list[:idx] + my_list[idx + 1:]
    return my_list
