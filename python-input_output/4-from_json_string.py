#!/usr/bin/python3
"""
This module for From JSON string to Object task
"""
import json


def from_json_string(my_str):
    """This function that returns an object"""
    return json.loads(my_str)
