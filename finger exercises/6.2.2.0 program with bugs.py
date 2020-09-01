def isPal(x):
    """ Assumes x is a list
        Returns True if the list is a palindrome; False otherwise """

    temp = x[:]
    temp.reverse()
    print(temp, x)
    if temp == x:
        return True
    else:
        return False

def silly(n):
    """ Assumes n is an int > 0
        Gets n inputs from user
        Prints 'Yes' if the sequence of inputs forms a palindrome;
            'No' otherwise """
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')