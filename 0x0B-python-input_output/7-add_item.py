#!/usr/bin/python3
'''
This is a scipt that load object from a json file
and then collect arg from cmd and store in a file
'''
import sys

if __name__ == "__main__":
    load_from_json_file = __import__(6-load_from_json_file).load_from_json_file
    save_to_json_file = __import__(5-save_to_json_file).save_to_json_file
    '''import the function'''
    argument = sys.argv[1:]
    try:
        items = load_from_json_file(add_item.json)
    except FileNotFoundError:
        input_0 = []
    input_0.extend(argument)
    '''get the list of argument from the cmd except the script name'''
    save_to_json_file(input_0, add_item.json)
