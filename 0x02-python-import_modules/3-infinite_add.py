#!/usr/bin/python3

import sys

arguments = [int(arg) for arg in sys.argv[1:]]

result = sum(arguments)

print(result)

