""" Asks the user to enter a number "x"
    Asks the user to enter a number "y"
    Prints out the number "x" raised to the power "y"
    Prints out the log (base 2) of "x" """

import numpy

x = float(input('Enter a number to be the base: '))
y = float(input('Enter a number to be the power: '))
print(x)
print(y)
print(x**y)
log = numpy.log2(x)
print(log)