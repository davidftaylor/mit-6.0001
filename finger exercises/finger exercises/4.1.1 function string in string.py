# Finger exercise 4.1.1
# Write a function isIn that accepts two strings as arguments and returns True
# if either string occurs anywhere in the other, and False otherwise.
# (Hint: you might want to use the built-in str operation 'in'.)

def isIn(str1, str2):
    if type(str1) == str and type(str2) == str:
        if str1 in str2 or str2 in str1:
            return True
        else:
            return False
    else:
        return 'One or both types not a string'
