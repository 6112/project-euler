# encoding=utf-8
## SOLVED 2013/12/21
## 21124

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

import re

MAX = 1000

def euler ():
    # accumulator for the number of letters used
    accumulator = 0
    # for each number in the given range
    for number in range (1, MAX + 1):
        # get the number's name
        name = number_name (number)
        # remove the whitespace and dashes
        name = re.sub ('\\s|-', '', name)
        # add the length of the anme to the number of letters used
        accumulator += len (name)
    # return the number of letters used
    return accumulator

# used for direct access to some number names
number_name_dictionary = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    15: 'fifteen',
    18: 'eighteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    80: 'eighty',
    1000: 'one thousand'
}

def number_name (number):
    """Return the full name, in letters, of a given number.

    Args:
        number: number whose name should be returned.
    Returns:
        the full name of that number (twenty-three, one hundred and two...), as
        a string.
    Raises:
        ValueError: if number is not between 0 and 1000.
    """
    if not isinstance (number, int):
        raise TypeError ("number is not an integer")
    elif number < 0 or number > 1000:
        raise ValueError ("number out of range (must be between 0 and 1000)")
    elif number in number_name_dictionary:
        # return directly if it's simply a dictionary lookup -- used for
        # exceptions and small numbers
        return number_name_dictionary [number]
    elif number > 10 and number < 20:
        # sixteen, nineteen...
        return number_name_dictionary [number - 10] + 'teen'
    elif number >= 20 and number < 100:
        # twenty-three, forty-nine...
        if number // 10 * 10 in number_name_dictionary:
            # exceptions for the tens: twenty, forty, fifty...
            name = number_name_dictionary [number // 10 * 10]
        else: 
            # regular tens: sixty, seventy...
            name = number_name (number // 10) + 'ty'
        if number % 10:
            # if has a non-zero unit, add a dash, then the name of the units
            # (twenty-three, ninety-eight...)
            name += '-' + number_name (number % 10)
        return name
    elif number >= 100 and number < 1000:
        # nine hundred, two hundred...
        name = number_name (number // 100) + ' hundred'
        # if has tens or units
        if number % 100:
            # add 'and ...', as in four hundred and ninety-eight
            name += ' and ' + number_name (number % 100)
        return name
