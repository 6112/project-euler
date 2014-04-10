#encoding=utf-8
## SOLVED 10/04/14
## 16695334890

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
# the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

def euler():
    # accumulator for the sum of these special pandigitals, final answer
    accumulator = 0
    for pandigital in generate_valid_pandigitals():
        accumulator += list_to_int(pandigital)
    return accumulator

def list_to_int(digits):
    """Converts a list of integers corresponding to digits to a number.

    e.g.:
        list_to_int([4, 9, 2]) == 492.

    Args:
        digits: list of integers, which are the digits of the number."""
    # start at 0
    accumulator = 0
    for digit in digits:
        # move the previous digits to the left
        accumulator *= 10
        # append this digit
        accumulator += int(digit)
    # return the number
    return accumulator

def generate_valid_pandigitals():
    """Yields all the pandigitals that fit the criterion in the question."""
    # set of available digits (each from 0 to 9)
    digits = set(range(0, 10))
    # for each possibility for first, second, and third digit
    for first_digit in digits:
        first_available_digits = set(digits)
        first_available_digits.remove(first_digit)
        for second_digit in first_available_digits:
            second_available_digits = set(first_available_digits)
            second_available_digits.remove(second_digit)
            for third_digit in second_available_digits:
                third_available_digits = set(second_available_digits)
                third_available_digits.remove(third_digit)
                # for each pandigital with those starting digits
                for pandigital in pandigitals_helper(
                        [second_digit, third_digit], # last 2 digits
                        [2, 3, 5, 7, 11, 13, 17], # divisions to use, in order
                        third_available_digits):
                    # yield the whole pandigital 'list' to the main function
                    yield [first_digit, second_digit, third_digit] + pandigital

def pandigitals_helper (pair, divisors, available):
    """Used as a helper for generate_valid_pandigitals(), do not use directly.

    Selects the next possible digit that validates the next division and
    'yields' it recursively.

    Args:
        pair: 2-element list containing the previous two digits.
        divisors: list containing the divisors that should be satisfied for
        the rest of the digits, in order.
        available: set containing the available digits for generating a number
        that is still pandigital."""
    # the current divisor to use
    divisor = divisors[0]
    # for each possible digit combination
    for last_digit in available:
        # if that combination is a multiple of the divisor, recurse
        if (pair[0] * 100 + pair[1] * 10 + last_digit) % divisor == 0:
            # if this is the last digit
            if len(divisors) == 1:
                # yield a list of the last digit only
                yield [last_digit]
            else:
                # for each possible combination for the rest of the digits
                for pandigital in pandigitals_helper(
                        [pair[1], last_digit], # last 2 digits
                        divisors[1:], # divisions to use, in order
                        available - {last_digit} # digits still available
                        ):
                    # yield the last digit followed by the rest
                    yield [last_digit] + pandigital
