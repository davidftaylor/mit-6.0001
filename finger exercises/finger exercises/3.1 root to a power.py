# Finger exercise 3.1: Write a program that asks the user to enter an integer
# and prints two integers, root and pwr, such that 1 < pwr < 6 and root**pwr
# is equal to the integer entered by the user. If no such pair of integers
# exists, it should print a message to that effect.

x = int(input('Enter an integer: '))
pwr = 1
root = 0
while root < abs(x):
    pwr = pwr + 1
    if pwr == 6 and root**pwr != abs(x):
        root = root + 1
        pwr = 0
    if root**pwr == abs(x):
        break
if root**pwr == abs(x):
    if x < 0:
        root = -root
    print(x, 'can be represented as', root, 'to the power of', str(pwr) + '.')
else:
    print('Your integer cannot be represented as another integer \
raised to any power between 1 and 6.')
