#!/usr/bin/python3

import sys

num_args = len(sys.argv) - 1 

if num_args == 0:
    print("Number of argument: 0.")
    print(".")
else:
    print("Number of argument{}: {}.".format("s" if num_args > 1 else "", num_args))


    for i, arg in enumerate(sys.argv[1:], start=1):
        print("Argument {}: {}".format(i, arg))
