# encoding=utf-8
## SOLVED 20/12/13
## 5537376230

# Work out the first ten digits of the sum of the following one-hundred 50-digit
# numbers.

import modules.file as fileutils

def euler ():
    # read the file
    numbers = fileutils.flattened_list_from_file ('data/013.txt')
    # return the first ten digits of the sum of the numbers
    return str (sum (numbers)) [:10]
