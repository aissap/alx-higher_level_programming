#!/usr/bin/python3
"""Defines a json reading function."""
import json


def load_from_json_file(filename):
    """Create an object from json."""
    with open(filename) as file:
        return (json.load(file))
