numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
itersLeft = numXs
while (itersLeft != 0):
    toPrint = toPrint + 'X'
    itersLeft = itersLeft - 1
print(toPrint)
