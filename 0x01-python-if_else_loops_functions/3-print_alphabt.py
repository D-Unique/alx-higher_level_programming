#!/usr/bin/python3
for i in range(97, 123):
    if i == 71 or i == 65:
        continue
    else:
        print("{:c} ".format(i), end='')
