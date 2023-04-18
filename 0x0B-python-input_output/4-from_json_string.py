#!/usr/bin/python3
"""
contain the JSON string function
"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string
    Args:
        my_str: JSON representation
    Raises:
        Exception: when the string can't be decoded
    """
    return json.loads(my_str)
