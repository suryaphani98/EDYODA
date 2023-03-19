#1  Write a Python function to sum all the numbers in a list.

def reverse(string):
    string = string[::-1]
    return string
s1="1234abcd"
print(reverse(s1))

#2 Write a Python program to reverse a string.

def sum(num):
    total = 0
    for x in num:
        total = total + x
    return total
s2 = (8, 2, 3, 0, 7)
print(sum(s2))

#3 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def string_test(s):
    uppercase = 0
    lowercase = 0
    for c in s:
        if c.isupper():
            uppercase = uppercase + 1
        elif c.islower():
            lowercase = lowercase + 1
        else: 
            pass
    print("The Original String :",s)
    print("The UPPER CASE letters :",uppercase)
    print("The lowe case letters :",lowercase)
s = "The quick Brow Fox"
string_test(s)