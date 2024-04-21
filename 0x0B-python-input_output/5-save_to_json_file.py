#!/usr/bin/python3
'''
contain a funtion that save an object
in a text file using  Json represantation
'''
import json


def save_to_json_file(my_obj, filename):
    '''collect object and file where Json is to be saved

   args:
        my_obj (str,dict,list) : path to python data
        filename :

    return:
        Any : JSON str
    '''

    with open(filename, "w") as f:
        data = json.dump(my_obj, f)
    return data
