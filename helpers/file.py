import re

def list_from_file (file_name, separator = '\\s+', convert_to = int):
    """Returns a 2-D list which contains the content of a file, with lines
    corresponding to sublists and elements being converted with function
    convert_to.

    separator is used (as a regexp) as a separator for each element."""
    array = []
    with open (file_name) as data_file:
        for line in data_file:
            line = line.strip ()
            tokens = re.split (separator, line)
            tokens = [convert_to (token) for token in tokens]
            array.append (tokens)
    return array

def flattened_list_from_file (file_name, separator = '\\s+', convert_to = int):
    """Returns list_from_file as a 1-D list instead of a 2-D list (useful when
    each row has only 1 element anyways)."""
    array = list_from_file (file_name, separator, convert_to)
    array = [element for row in array for element in row]
    return array
