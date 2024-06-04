#!/usr/bin/python3
"""
This module for Read file task
"""


def read_file(filename=""):
    """This function read file from filename var"""
    with open(filename, 'r', encoding="UTF8") as file:
        print(file.read())
        file.close()
