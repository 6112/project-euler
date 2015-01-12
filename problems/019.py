# encoding=utf-8
## SOLVED 2013/12/20
## 171

# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

def euler ():
    # array of lengths of months
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # values to add to day-of-the-week accumulator for each month index
    month_offsets = []
    # accumulator for month offsets
    accumulator = 0
    for month in range (12):
        month_offsets.append (accumulator % 7)
        accumulator += month_lengths [month]
    def day_of_week (day, month, year):
        # accumulator for day-of-the-week
        # 6 is Sunday, 0 is Monday, 1 is Tuesday...
        accumulator = day - 1
        # account for the month
        accumulator += month_offsets [month - 1]
        # account for the year
        accumulator += year + year // 4 - year // 100 + year // 400 + 6
        # adjust if the year is leap, and the month is January of February
        if is_leap (year):
            accumulator -=1
            if month > 2:
                accumulator += 1
        # return the day of the week between 0 and 6, with 0 being Monday
        return accumulator % 7
    # number of Sundays on the first of the month
    sunday_count = 0
    # for each year from 1901 to 2000
    for year in range (1901, 2001):
        # for each month  in that year
        for month in range (1, 13):
            # if the first of the month is a Sunday
            if day_of_week (1, month, year) == 6:
                # add a Sunday
                sunday_count += 1
    # return the number of Sundays on the first of the month
    return sunday_count

def is_leap (year):
    """Returns True iff the given year number represents a leap year."""
    return year % 400 == 0 or (year % 4 == 0 and year % 400 != 0)
