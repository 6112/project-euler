def permutations (tokens):
    """Used as an iterator for all the permutations of a sequence.""" 
    if not tokens:
        yield []
        return
    for index, first in enumerate (tokens):
        rest = tokens [: index] + tokens [index + 1:]
        for permutation in permutations (rest):
            yield [first] + permutation
