#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase"""
    result = ""
    for c in str:
        result += "{:c}".format(ord(c) - 32 if 97 <= ord(c) <= 122 else ord(c))
    print(result)
