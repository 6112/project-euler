#!/usr/bin/python3
## SOLVED 20/12/13
## 76576500

from modules.prime import *

def euler ():
    i = 1
    triangle = 1
    while True:
        if divisor_count (triangle) > 500:
            return triangle
        i += 1
        triangle += i

print (euler ())
