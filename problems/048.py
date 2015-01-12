#encoding=utf-8
## SOLVED 2014/04/10
## 9110846700

# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

MAX = 1000

def euler():
    # accumulator for the sum
    accumulator = 0
    # for each number from 1 to 1000
    for n in range(1, MAX + 1):
        # add the exponent to the accumulator
        accumulator += quick_exponent_with_mod(n, n, 10 ** 10)
        accumulator %= 10 ** 10
    # return the accumulator
    return accumulator
    
def quick_exponent_with_mod(base, power, modulo):
    """Compute quickly the exponent within a given modulo range.

    Will apply a modulo with the specified base at every iteration of the
    exponentiation algorithm, making sure the result is in the given range."""
    # 'powers' will be a list of the base with powers of two applied, i.e.:
    # with base==3, powers==[3, 3^2, 3^4, 3^8, 3^16, ...]
    powers = [base]
    # for each power of two
    i = 2
    while i <= power:
        # compute base^(2^i) and add it to the list
        powers.append((powers[-1] * powers[-1]) % modulo)
        # next power of two
        i *= 2
    # list of booleans corresponding to which powers of two to include to make
    # up the whole exponent
    powers_to_include = list(bool(int(digit)) for digit in bin(power)[2:][::-1])
    # accumulator for the product
    accumulator = 1
    # for each factor==base^(2^index)
    for index, factor in enumerate(powers):
        # if this power should be included
        if powers_to_include[index]:
            # multiply and apply modulo
            accumulator *= factor
            accumulator %= modulo
    # return the product accumulator
    return accumulator
