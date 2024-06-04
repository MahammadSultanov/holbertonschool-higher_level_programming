#!/usr/bin/python3
"""
This module for Write to a file task
"""


def write_file(filename="", text=""):
    """This function for writes a string to a text file"""
    with open(filename, 'w', encoding="UTF8") as file:
        return file.write(text)
