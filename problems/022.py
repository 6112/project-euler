# encoding=utf-8
## SOLVED 23/12/13
## 871198282

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.

# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import helpers.file as fileutils

def euler ():
    # read the names from the file
    names = fileutils.flattened_list_from_file ('data/022.txt', separator = ',',
      convert_to = str)
    # remove the quotes surrounding the name
    names = [name.replace ('"', '') for name in names]
    # sort the names alphabetically
    names.sort ()
    # accumulator for the total of the name scores
    accumulator = 0
    for index, name in enumerate (names):
        # calculate the name score
        score = sum (ord (letter) - ord ('A') + 1 for letter in name)
        score *= (index + 1)
        # add the score to the accumulator
        accumulator += score
    # return the accumulator
    return accumulator
