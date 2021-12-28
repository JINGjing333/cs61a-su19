from math import sqrt
from lab04 import *

def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.
    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """ 
    "*** YOUR CODE HERE ***"

    return min(letters, key=lambda x: letters[x])

"""
    return [i[0] for i in d.items() if i[1]==min(d.values())]

    for i in d.items():
        if i[1]==min(d.values()):
            return i[0]
    """

    
    



if __name__ == "__main__":
    letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    print(key_of_min_value(letters))
