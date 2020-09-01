# 3.3 - What must be changed so that the code will work for finding an
# approximation to the cube root of both negative and positive numbers?
# (Hint: think about changing 'low' so that the answer lies within the range
# being searched)

##x = 0
##epsilon = 0.01
##numGuesses = 0
##low = min(x, -1.0)
##high = max(1.0, x)
##ans = (high + low)/2.0
##while abs(ans**3 - x) >= epsilon:
##    print('low =', low, 'high =', high, 'ans =', ans)
##    numGuesses += 1
##    if ans**3 < x:
##        low = ans
##    else:
##        high = ans
##    ans = (high + low)/2.0
##print('numGuesses =', numGuesses)
##print(ans, 'is close to cube root of', x)

x = .5
epsilon = 0.01
numGuesses = 0
low = 0
high = x
ans = (high + low)/2.0
if x < 0:
    low = x
    high = 0
if -1 < x < 1:
    if x < 0:
        low = -1
    if x > 0:
        high = 1
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to cube root of', x)
