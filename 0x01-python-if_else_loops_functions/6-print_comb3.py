#!/usr/bin/python3

for i in range(0, 9):
    for j in range(i, 10):
        if i == j:
            continue
        print("{0}{1}".format(i, j), end=' ')
