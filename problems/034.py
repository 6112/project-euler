# encoding=utf-8
## SOLVED 2013/12/24
## 40730

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

MAX = 362881

def euler ():
    accumulator = 0
    for number in range (3, MAX):
        if is_valid (number):
            accumulator += number
    return accumulator

def is_valid (number):
    sum_of_digit_factorials = sum (factorial (int (c)) for c in str (number))
    return number == sum_of_digit_factorials

def factorial (n):
    accumulator = 1
    for i in range (2, n + 1):
        accumulator *= i
    return accumulator
