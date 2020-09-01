def sumDigits(s):
    """ Assumes s is a string
        Returns the sum of the decimal digits in s
            For example, if s is 'a2b3c' it returns 5 """
    sum = 0
    for char in s:
        try:
            sum += int(char)
        except ValueError:
            continue
    return sum