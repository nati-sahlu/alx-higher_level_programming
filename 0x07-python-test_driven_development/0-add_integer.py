#!/usr/bin/python3

"""This module defines an integer addition function."""


def add_integer(a, b=98):
    """
    Adds two integers or floats (cast to integers).

    Args:
        a: First number (int or float).
        b: Second number (int or float), default is 98.
    Returns:
        int: The integer addition of and b.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """

    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
