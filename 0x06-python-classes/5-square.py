#!/usr/bin/python3

''' This file contains the class Square with it Attribute size'''


class Square:

    '''This is a class Square and it has a private Attribute size'''

    def __init__(self, size=0):
        '''inintialing an object with a defult size value of zero'''

        self.__size = size

    @property
    def size(self):
        '''This is a method that gets the value of the private attribute'''
        return self.__size

    @size.setter
    def size(self, value):

        '''This is a method that set the private attribute size'''

        '''
        Args:
            raise:
                typeError: size must be an integer
                valueError: size must be greater than zero
        '''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value <= 0):
            raise ValueError("size must be greater than zero")
        self.__size = value

    def area(self):

        '''This is a method area'''

        return self.__size * self.__size

    def my_print(self):
        '''This is a method my_print'''

        '''
        Args:
            if size is zero return empty line
            else:
                return #
        '''
        if self.__size = 0:
            return ""
        else:
            for (i=self.__size, i=0, --1):
                return self.__size * "#"
