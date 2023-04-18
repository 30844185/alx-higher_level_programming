#!/usr/bin/python3
"""
contain the JSON string
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    Args:
        my_obj: object
    Raises:
        Exception: when the object can't be encoded
    """
    return json.dumps(my_obj)
