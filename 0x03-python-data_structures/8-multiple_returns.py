#!/usr/bin/python3
# Function to return the length of a string and its first character

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
