#!/usr/bin/python3
"""Defines string-to-json function."""
import json


def to_json_string(my_obj):
    """Return the json of a string object."""
    return (json.dumps(my_obj))
