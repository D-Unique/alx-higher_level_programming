#!/usr/bin/python

for i in range(0, 100):
    if i == 99:
        print(i)
        continue
    if i < 10:
        print("0{}".format(i), end=',')
    else:
        print("{}".format(i), end=',')
