#!/usr/bin/python3
"""
This module for Append to a file task
"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text file"""
    with open(filename, 'a', encoding="UTF8") as file:
        return file.write(text)
