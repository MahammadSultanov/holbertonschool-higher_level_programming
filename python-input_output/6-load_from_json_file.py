#!/usr/bin/python3
"""
This module for  Save Object to a file task
"""
import json


def load_from_json_file(filename):
    """This function that writes an Object to a text file"""
    with open(filename, 'r', encoding="UTF8") as file:
        return json.load(file)
