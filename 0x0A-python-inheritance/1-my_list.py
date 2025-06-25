#!/usr/bin/python3

"""Defines an inherited list class MyList."""


class MyList(list):
    """Custom list that inherits from built-in list."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
