#!/usr/bin/python3
'''
contain a funtion that save an object 
in a text file using  Json represantation
'''
import json


def save_to_json_file(my_obj, filename):
    with open("filename","w") as f:
        json.dump(my_obj, f, indent=2)
    return f
