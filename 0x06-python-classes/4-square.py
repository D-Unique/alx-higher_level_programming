#!/usr/bin/python3

''' This file contains the class Square with it Attribute size'''


class Square:

    '''This is a class Square and it has a private Attribute size'''

    def __init__(self, size=0):
        '''inintialing an object with a defult size value of zero'''

        self.size = size

        @property
        def get_size(self):
            '''This is a method that gets the value of the private attribute'''
            return self.__size

        @value.setter
        def size_setter(self, value):

            '''This is a method that set the private attribute size'''

            '''
            Args:
                raise:
                    typeError: size must be an integer
                    valueError: size must be greater than zero
            '''

            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif (size <= 0):
                raise ValueError("size must be greater than zero")
        self.__size = value

    def area(self):
        '''This is a method area'''
        return self.__size * self.__size
