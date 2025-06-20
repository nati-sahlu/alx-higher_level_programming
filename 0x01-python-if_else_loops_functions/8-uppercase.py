#!/usr/bin/python3
def to_upper(char):
    if ord(char) > 96 and ord(char) < 123:
        return (ord(character) - 32)
    else:
        return chr(ord(character))


def uppercase(str):
    uppercase = ""
    for char in str:
        uppercase += to_upper(char)
    print(uppercase)
