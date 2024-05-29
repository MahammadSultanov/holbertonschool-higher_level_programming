#!/usr/bin/python3
"""Modul for adding two integers"""

def add_integer(a, b=98):
    """This function adds two integers"""
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, int):
        b = int(b)
    return int(a+b)

