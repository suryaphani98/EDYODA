# Write a Python program to get the Fibonacci series between 0 to 50.

x=0
y=1

while y<=50:
    x,y = y,x+y
    print("The Fibonacci values :", x)
    

# Write a Python program that accepts a word from the user and reverse it.

name = input("Enter a name:")

print("The Reversed name:",name[::-1])


# Write a Python program to count the number of even and odd numbers from a series of numbers.

l = [1,2,3,4,5,6,7,8,9]

even_count = 0
odd_count = 0

for i in l:
    if i%2 == 0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("The Even NUmber:",even_count)
print("The Even NUmber:",odd_count)