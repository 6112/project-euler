#!/usr/bin/python

from sys import argv
from importlib import import_module

def main ():
    if len (argv) <= 1:
        print ('Must supply a problem number.')
        return
    try:
        int (argv [1])
    except ValueError:
        print (argv [1] + ' is not a valid integer.')
        return
    if int (argv [1]) <= 0:
        print (argv [1] + ' is not greater than or equal to one.')
    try:
        module = import_module ('problems.' + argv [1])
    except ImportError as error:
        print ('No solution for problem #' + argv [1] + '.')
        return
    if not module.euler:
        print ('Solution for problem #' + argv [1] + ' is invalid.')
        return
    result = module.euler ()
    print (result)

if __name__ == '__main__':
    main ()
