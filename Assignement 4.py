#1 Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

nums = 10
result =lambda x:x+25

print(result(nums))

#2 Write a Python program to triple all numbers of a given list of integers. Use Python map.

nums1 = [1,2,3,4,5,6,7,8]
result1 = list(map(lambda x:x+x+x,nums1))

print(result1)

#3 Write a Python program to square the elements of a list using map() function.

nums2 = [4, 5, 2, 9]

def square(num):
    return num**2

squares = list(map(square , nums2))
print(squares)



