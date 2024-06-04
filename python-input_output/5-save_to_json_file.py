#!/usr/bin/python3
"""
This module for  Save Object to a file task
"""
import json


def save_to_json_file(my_obj, filename):
    """This function that writes an Object to a text file"""
    with open(filename, 'w', encoding="UTF8") as file:
        return file.write(json.dumps(my_obj))
