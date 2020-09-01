# Finger exercise 3.2: Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g. s = '1.23,2.4,3.123'. Write a program that prints the sum of the
# numbers in s

# For loops section - use for loop(s), presumably
# len, indexing, slicing known

s = '1.23,2.4,3.123'
total = None
for i in range(len(s)):
        if s[i] == ',':
                if total != None:
                        total = total + float(s[last_comma+1:i])
                        last_comma = i
                else:
                        total = float(s[0:i])
                        last_comma = i
        if s[0:i+1] == s:
                total = total + float(s[last_comma+1:i+1])
print(total)
