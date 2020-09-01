def factI(n):
    """ Assumes n and int > 0
        Returns n! """
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

def factR(n):
    """ Assumes n an int > 0
        Returns n! """
    if n == 1:
        return n
    else:
        return n*factR(n - 1)
