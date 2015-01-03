# encoding=utf-8
## SOLVED 2013/12/19
## 25164150

# The sum of the squares of the first ten natural numbers is, 
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is, 
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

HIGHEST_NUMBER = 100

def euler ():
    # list of numbers to use
    numbers = range (1, HIGHEST_NUMBER + 1)
    # sum of the squares of each number
    sum_of_squares = sum ([x * x for x in numbers])
    # square of the sum of those numbers
    square_of_sum = sum (numbers) ** 2
    # return the difference of the two
    return square_of_sum - sum_of_squares
