#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lnum = number % 10
else:
    lnum = number % -10

if lnum > 5:
    print(f"Last digit of {number} is {lnum} and is greater than 5")
if lnum == 0:
    print(f"Last digit of {number} is {lnum} and is 0")
if lnum < 6 and lnum != 0:
    print(f"Last digit of {number} is {lnum} and is less than 6 and not 0")
