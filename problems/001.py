# encoding=utf-8
## SOLVED 2013/12/19
## 233168

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

HIGHEST_VALUE = 1000

def euler ():
    # construct the list of relevant numbers
    numbers = (n for n in range (HIGHEST_VALUE) if n % 5 == 0 or n % 3 == 0)
    # return the sum
    return sum (numbers)
