#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
l_digit = number[-1]
if l_digit > 5:
    print("Last digit of "{}" is "{}" and is greater than 5".format("number","number[-1]"))
if the l_digit == 0:
    print("Last digit of "{}" is "{}" and is 0".format("number","number[-1]"))
if l_digit <6 and !=0:
    print("Last digit of "{}" is {} and is less than 6 and not 0".format("number","number[-1]"))
