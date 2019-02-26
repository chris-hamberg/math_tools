import itertools

def cartesian(args):
    '''
    ex. A = {1, 2} and B = {2, 3}
    A x B = {(1, 2), (1, 3), (2, 2), (2, 3)}
    - expects a list of lists that represents a list of sets
    - returns a list that represents a set of ordered pairs.
    '''
    if len(args) == 2:
        return list(itertools.product(args[0], args[1]))
    return list(itertools.product(args[0], cartesian(args[1:])))
