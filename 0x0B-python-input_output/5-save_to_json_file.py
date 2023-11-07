#!/usr/bin/python3
"""Defines a json writing function."""
import json

def save_to_json_file(my_obj, filename):
    """Write an object to a text file using json."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
