# Square an integer, the hard way

x = input("Enter the integer you would like to square: ")
ans = 0
itersLeft = abs(int(x))
while (itersLeft != 0):
    ans = ans + abs(int(x))
    itersLeft = itersLeft - 1
print(x + '*' + x + ' = ' + str(ans))
