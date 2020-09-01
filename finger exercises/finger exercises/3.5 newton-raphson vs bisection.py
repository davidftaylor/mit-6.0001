# Finger exercise 3.5 - Newton-Raphson approximation
# Add some code to keep track of number of iterations to find the root
# Use that code as part of a program to compare efficiency of N-R method
# as against bisection search. (N-R should be more efficient)

# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0

epsilon = 0.0001
k = 5865
guess = k/2.0
iters = 0

while abs(guess*guess - k) >= epsilon:
    guess = guess - ((guess**2 - k)/(2*guess))
    iters += 1
print('Square root of', k, 'is about', guess)
print(iters)

iters = 0
high = k
low = 0
guess = (high + low)/2.0

while abs(guess**2 - k) >= epsilon:
    if guess**2 > k:
        high = guess
    else:
        low = guess
    guess = (high + low)/2.0
    iters += 1
if abs(guess**2 - k) <= epsilon:
    print('The square root of', k, 'is', guess)
    print(iters)
else:
    print('Could not find the square root of', k)
    print(iters)
