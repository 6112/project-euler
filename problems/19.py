#!/usr/bin/python3
## SOLVED 20/12/13
## 171

# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

def euler ():
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_offsets = []
    accumulator = 0
    for month in range (12):
        month_offsets.append (accumulator % 7)
        accumulator += month_lengths [month]
    def day_of_week (day, month, year):
        accumulator = day - 1
        accumulator += month_offsets [month - 1]
        accumulator += year + year // 4 - year // 100 + year // 400 + 6
        if is_leap (year):
            accumulator -=1
            if month > 2:
                accumulator += 1
        return accumulator % 7
    sundays = 0
    for year in range (1901, 2001):
        for month in range (1, 13):
            if day_of_week (1, month, year) == 6:
                sundays += 1
    return sundays

def is_leap (year):
    return year % 400 == 0 or (year % 4 == 0 and year % 400 != 0)
