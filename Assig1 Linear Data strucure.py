#question 1

def find(array,summ):
    for i in range(summ):
        for j in range(i, summ):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])


array = [5, 2, 3, 4, 1, 6, 7]
summ = 7
find(array,summ)

#question 2

def reverseList(A):
    print( A[::-1])
	
A = [1, 2, 3, 4, 5, 6]
print(A)
print("Reversed list is")
reverseList(A)

#question 3

def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    concat_str = str1 + str1
    if str2 in concat_str:
        return True
    else:
        return False

str1 = "waterbottle"
str2 = "erbottlewat"
print(is_rotation(str1, str2))  # Output: True

str3 = "hello"
str4 = "world"
print(is_rotation(str3, str4))  # Output: False


#question 4

def first_non_repeated_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None

string1 = "aabbccddeeff"
print(first_non_repeated_char(string1)) 

string2 = "aabbccddee"
print(first_non_repeated_char(string2))

string3 = "abcdefgabc"
print(first_non_repeated_char(string3)) 



#question 5

'''
The Tower of Hanoi is a classic problem in computer science and mathematics that involves moving a stack of discs of different 
sizes from one peg to another, using a third peg as an intermediate. The problem has the following rules:
Only one disc can be moved at a time.
Each move consists of taking the upper disc from one of the stacks and placing it on top of another stack or on an empty peg.
No larger disc may be placed on top of a smaller disc.
Here's a Python program to implement the Tower of Hanoi algorithm recursively:
'''

def tower_of_hanoi(n, source, destination, auxiliary):
    
    if n == 1:
        print(f"Move disc 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disc {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)

tower_of_hanoi(3, 'A', 'C', 'B')

#question 6

'''Infix notation is the standard notation for writing arithmetic expressions in which the operator is placed between the 
operands, such as 2 + 3 or (4 * 5) - 6.

Prefix notation, also called Polish notation, is a way of writing arithmetic expressions in which the operator is placed 
before the operands, such as + 2 3 or - * 4 5 6.

Postfix notation, also called reverse Polish notation, is a way of writing arithmetic expressions in which the operator is 
placed after the operands, such as 2 3 + or 4 5 * 6 -.'''

def postfix_to_prefix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append( operand1 +char+ operand2)
    return stack.pop()

expression = "23+45*-"
print(postfix_to_prefix(expression)) 

#question 7

def prefix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in reversed(expression):
        if char in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"({operand1} {char} {operand2})")
        else:
            stack.append(char)
    return stack.pop()

expression = "*-+23*549"
print(prefix_to_infix(expression))

#question 8

def isbalanced(s):
    while(len(s)!=0):
        s=s.replace('()','')
        s=s.replace('[]','')
        s=s.replace('{}','')
        break
    if(len(s)==0):
        return True
    else:
        return False
s=input("Enter a string of brackets:")
print("Given string is balanced:",isbalanced(s))


#question 9

def reverse_stack(stack):
    if len(stack) == 0:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)
    
def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)


stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)

#question 10

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
            
    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
        
    def get_min(self):
        return self.min_stack[-1]


stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(7)
stack.push(1)
print(stack.get_min())  
stack.pop()
print(stack.get_min())  
