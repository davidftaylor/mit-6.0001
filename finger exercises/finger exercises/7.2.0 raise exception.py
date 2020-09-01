def findAnEven(L):
    """ Assumes L is a list of integers
        Returns the first even number in L
        Raises ValueError if L does not contain an even number """
    
    for integer in L:
        if integer % 2 == 0:
                return integer
                break
        else:
            if integer == L[-1]:
                raise ValueError('No even numbers in list')