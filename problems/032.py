# encoding=utf-8
## SOLVED 24/12/13
## 45228

def euler ():
    products_cache = {}
    accumulator = 0
    n = 0
#    found = False
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

#    for split_index_1 in range (1, len (permutation) - 1):
#        for split_index_2 in range (split_index_1 + 1, len (permutation)):
#            multiplicand = int (permutation [: split_index_1])
#            multiplier = int (permutation [split_index_1 : split_index_2])
#            product = int (permutation [split_index_2 :])
#            if multiplicand * multiplier == product:
#                return product

    return None

def permutations (tokens):
    if not tokens:
        yield []
        return
    for index, first in enumerate (tokens):
        rest = tokens [: index] + tokens [index + 1:]
        for permutation in permutations (rest):
            yield [first] + permutation
