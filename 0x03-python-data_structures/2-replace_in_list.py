#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ This function replaces an element of
    my_list at a specific position indicated by idx
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
