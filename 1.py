#!/usr/bin/python3
## SOLVED 19/12/13
## 233168

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

MAX_VALUE = 1000

def euler ():
    return sum ([n for n in range (0, MAX_VALUE) if n % 5 == 0 or n % 3 == 0])

print (euler ())
