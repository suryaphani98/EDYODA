#map ---- applying a function to each function in iterator

#lambda function doesn't have any name

#lambda arguments : expression

num1 = [1,23,45,5]
num2 = [2,4,5]
def square(n1,n2):
    return n1**2+n2**2
result = list(map(square, num1,num2))
print(result)


#filter

def check_even(n):
    if n%2 != 0:
        return True
    return False

nums = [1,2,3,4,5,6,7,8,9,10]

evennum = filter(check_even , nums)
print(list(evennum))



#----------------------------------------------JSON----------------------------------------------------------#

# loads(), load() ----> read the data from json

# deserialization ----> conversion of jsn objects into there python objects (int,dict,list) for that we have load and loads method 

#method to convert single json object to python object (loads)
# to read the data from json file (load)

#dump() , dumps() ----> write data to json

#method to convert python object into a json object (dumps)
#to write the data from json file (dump)









