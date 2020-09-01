x = 111111
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print(numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed to find square root of', x)
else:
    print('The approximate square root of', x, 'is', ans)
