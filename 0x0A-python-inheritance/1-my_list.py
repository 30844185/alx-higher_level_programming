#!/usr/bin/python3
"""
contains the MyList class
""""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
