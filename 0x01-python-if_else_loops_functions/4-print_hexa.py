#!/usr/bin/python3
"""Print numbers 0 to 98 in decimal and hexadecimal."""

for i in range(0, 99):
    print("{0} = 0x{1:x}".format(i, i))
