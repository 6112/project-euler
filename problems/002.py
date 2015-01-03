# encoding=utf-8
## SOLVED 2013/12/19
## 4613732

# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

HIGHEST_VALUE = 4000000

def euler ():
    # previous and current fibonacci sequence numbers
    previous_number = 0
    current_number = 1
    # sum accumulator
    accumulator = 0
    # for each fibonacci number until HIGHEST_VALUE
    while current_number < HIGHEST_VALUE:
        # add to the sum if it's an even number
        if current_number % 2 == 0:
            accumulator += current_number
        previous_number += current_number
        current_number, previous_number = previous_number, current_number
    # return the sum
    return accumulator
