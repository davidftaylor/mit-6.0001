# examine if odd then check relative sizes or vice versa?
x = 7
y = 8
z = 9
if x % 2 == 1 and y % 2 == 1 and z % 2 == 1:
	if x > y and x > z:
		print('x is the largest odd')
	elif y > z:
		print('y is the largest odd')
	else:
		print('z is the largest odd')
elif x % 2 == 0 and y % 2 == 1 and z % 2 == 1:
	if y > z:
		print('y is the largest odd')
	else:
		print('z is the largest odd')
elif x % 2 == 1 and y % 2 == 0 and z % 2 == 1:
	if x > z:
		print('x is the largest odd')
	else:
		print('z is the largest odd')
elif x % 2 == 1 and y % 2 == 1 and z % 2 == 0:
	if x > y:
		print('x is the largest odd')
	else:
		print('y is the largest odd')
elif x % 2 == 1:
	print('x is the largest odd')
elif y % 2 == 1:
	print('y is the largest odd')
elif z % 2 == 1:
	print('z is the largest odd')
