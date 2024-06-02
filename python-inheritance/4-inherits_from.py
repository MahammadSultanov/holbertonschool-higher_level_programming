#!/usr/bin/python3
"""Module containing inherits_from func"""


def inherits_from(obj, a_class):
    """the object is an instance of a class that inherited
     (directly or indirectly) from the specified class"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return Falsep
