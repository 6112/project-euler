#!/usr/bin/python3
## SOLVED 21/12/13
## 21124

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

MAX_VALUE = 1000

def euler ():
    accumulator = 0
    for number in range (1, MAX_VALUE + 1):
        name = number_name (number)
        name = name.replace ('-', '')
        name = name.replace (' ', '')
        accumulator += len (name)
    return accumulator

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
    if number in number_name_dictionary:
        return number_name_dictionary [number]
    elif number > 10 and number < 20:
        return number_name_dictionary [number - 10] + 'teen'
    elif number >= 20 and number < 100:
        if number // 10 * 10 in number_name_dictionary:
            name = number_name_dictionary [number // 10 * 10]
        else: 
            name = number_name (number // 10) + 'ty'
        if number % 10:
            name += '-' + number_name (number % 10)
        return name
    elif number >= 100 and number < 1000:
        name = number_name (number // 100) + ' hundred'
        if number % 100:
            name += ' and ' + number_name (number % 100)
        return name
