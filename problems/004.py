# encoding=utf-8
## SOLVED 19/12/13
## 906609

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers

def euler ():
    # accumulator for the highest palindrome found so far
    highest_palindrome = 0
    # for each (a,b) pair
    for a in range (100, 1000):
        for b in range (a, 1000):
            product = a * b
            # if the product is a palindromic number
            if str (product) == str (product) [::-1]:
                # set the highest found so far to the higher of the two
                highest_palindrome = max (highest_palindrome, product)
    # return the highest palindrome found
    return highest_palindrome
