# encoding=utf-8
## SOLVED 24/12/13
## 45228

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

from modules.sequence import *

def euler ():
    products_cache = {}
    accumulator = 0
    for permutation in permutations ('123456789'):
        permutation = ''.join (permutation)
        products = valid_products (permutation)
        for product in products:
            if not product in products_cache:
                accumulator += product
                products_cache [product] = True
    return accumulator

def valid_products (permutation):
    products = []
    for split_1 in range (1, 5):
        for split_2 in (5 - split_1, 4 - split_1):
            if split_2 > 0:
                split_2 += split_1
                multiplicand = int (permutation [: split_1])
                multiplier = int (permutation [split_1 : split_2])
                product = int (permutation [split_2 :])
                if multiplicand * multiplier == product:
                    products.append (product)
    return products
