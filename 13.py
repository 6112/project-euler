#!/usr/bin/python3
## SOLVED 20/12/13
## 5537376230

# Work out the first ten digits of the sum of the following one-hundred 50-digit
# numbers.

def euler ():
    accumulator = 0
    with open ('13.txt') as numbers_file:
        for line in numbers_file:
            line = line.strip ()
            number = int (line [:12])
            accumulator += number
    return str (accumulator) [:10]

print (euler ())
