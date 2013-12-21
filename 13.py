#!/usr/bin/python3
## SOLVED 20/12/13
## 5537376230

# Work out the first ten digits of the sum of the following one-hundred 50-digit
# numbers.

from modules.file import *

def euler ():
    return str (sum (flattened_list_from_file ('13.txt'))) [:10]

print (euler ())
