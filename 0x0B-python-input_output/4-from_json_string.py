#!/usr/bin/python3
"""Defines json-to-object."""
import json


def from_json_string(my_str):
    """Return the representation of a json string.
    """
    return (json.loads(my_str))
