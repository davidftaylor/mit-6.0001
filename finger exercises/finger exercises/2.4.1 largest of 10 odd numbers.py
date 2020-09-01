counter = 10
odd_max = None
while counter > 0:
    num = int(input("Input a number: "))
    if num % 2 == 1 and (odd_max == None or num > odd_max):
        odd_max = num
    counter = counter - 1
if odd_max % 2 == 1:
    print(str(odd_max) + ' is the largest odd you entered')
else:
    print('No odd numbers were entered.')
