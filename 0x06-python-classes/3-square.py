#!/usr/bin/python3

''' The file contains a class Square with a size attribute. '''


class Square:

    '''
    This is a class Square that contains a size attribute.

    Args:
        size(int): holds the size of the square.
    '''

    def __init__(self, size=0):

        '''Initializing the object and giving size a default value = 0'''

        '''
        raise:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            '''This is a method that takes the argument self'''
            return self.size * self.size
