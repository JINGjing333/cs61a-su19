def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54

    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    
    if n == 1:
        return term(1)
    else:
        return term(n) + term(n-1)



if __name__ == "__main__":
    print(summation(9, lambda x: x +))