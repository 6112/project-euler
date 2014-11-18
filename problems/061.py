# encoding=utf-8
## SOLVED 18/11/14
## 28684

from math import sqrt

def euler():
    # functions used to check the type of a number
    predicates = [is_triangle, is_square, is_pentagonal, is_hexagonal,
            is_heptagonal, is_octagonal]
    for left in range(10, 100):
        # try to construct a chain from this initial left-part for the number
        c = chain([], left, predicates)
        # if it worked, return the sum
        if c:
            return sum(c)

def chain(xs, left, predicates):
    # `xs` is the constructed list
    # `left` is the left part of the current number
    # `predicates` is the list of predicates that aren't already verified by 
    #     numbers in `xs`
    if predicates == []:
        # `xs` has the right number of elements, return it
        return xs 
    rights = range(10, 100)
    if len(predicates) == 1:
      # if there is only one number left to guess, the right part of this
      # number must be the left part of the first number
      rights = [int(xs[0] / 100)]
    for right in rights:
        # construct the current number as "${left}${right}"
        n = left * 100 + right
        # no duplicates in `xs`
        if n in xs: 
            continue
        # check each predicate on the constructed number (n)
        for predicate in predicates:
            if predicate(n):
                # remove the verified predicate from the list of predicates
                new_predicates = list(predicates)
                new_predicates.remove(predicate)
                # try to advance recursively
                c = chain(xs + [n], right, new_predicates)
                # if it worked, return the returned value
                if c:
                    return c
    # failed to construct it
    return None

def is_triangle(k):
    n1 = (-1 + sqrt(1 + 8 * k)) / 2
    return int(n1) == n1# or int(n2) == n2

def is_square(k):
    return int(sqrt(k)) == sqrt(k)

def is_pentagonal(k):
    n1 = (1 + sqrt(1 + 24 * k)) / 6
    return int(n1) == n1# or int(n2) == n2

def is_hexagonal(k):
    n1 = (0.5 + sqrt(0.25 + 2 * k)) / 2
    return int(n1) == n1# or int(n2) == n2

def is_heptagonal(k):
    n1 = (3 + sqrt(9 + 40 * k)) / 10
    return int(n1) == n1# or int(n2) == n2

def is_octagonal(k):
    n1 = (2 + sqrt(4 + 12 * k)) / 6
    return int(n1) == n1# or int(n2) == n2
