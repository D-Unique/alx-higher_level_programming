#!/usr/bin/python3
'''contains a function that returns a JSON string
from a python object'''

import JSON


def from_json_string(my_str):
    '''this method take in a python object'''

    data = json.loads(my_str)
    return data
