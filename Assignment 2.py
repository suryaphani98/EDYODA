# 1 Delete the elements in an linked list whose sum is equal to zero
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_zero_sum(head):
    # create a hashmap to store cumulative sum and its corresponding node
    hashmap = {}
    dummy = Node(0)
    dummy.next = head
    curr = dummy
    cum_sum = 0
    
    while curr:
        cum_sum += curr.val
        if cum_sum in hashmap:
            # remove nodes between current node and node with same cumulative sum
            remove_node = hashmap[cum_sum].next
            cum_remove = cum_sum + remove_node.val
            while cum_remove != cum_sum:
                del hashmap[cum_remove]
                remove_node = remove_node.next
                cum_remove += remove_node.val
            hashmap[cum_sum].next = curr.next
        else:
            hashmap[cum_sum] = curr
        curr = curr.next
        
    return dummy.next
# create a linked list with sum zero
head = Node(3)
head.next = Node(4)
head.next.next = Node(-7)
head.next.next.next = Node(3)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(-4)
head.next.next.next.next.next.next = Node(-2)

# delete nodes with sum zero
new_head = delete_zero_sum(head)

# print the new linked list
curr = new_head
while curr:
    print(curr.val, end=' ')
    curr = curr.next


#2  Reverse a linked list in groups of given size
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_groups(head, k):
    # reverse the first group of size k
    curr = head
    prev = None
    next = None
    count = 0
    while curr and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
    
    # recursively reverse remaining nodes
    if next:
        head.next = reverse_groups(next, k)
    
    return prev
# create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# reverse in groups of size 2
new_head = reverse_groups(head, 2)

# print the new linked list
curr = new_head
while curr:
    print(curr.val, end=' ')
    curr = curr.next



# 3 Merge a linked list into another linked list at alternate positions.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_alternate(head1, head2):
    curr1 = head1
    curr2 = head2
    prev1 = None
    
    while curr1 and curr2:
        # insert node of second list after node of first list
        next1 = curr1.next
        curr1.next = curr2
        prev1 = curr2
        curr2 = curr2.next
        prev1.next = next1
        curr1 = next1
    
    return head1
# create the first linked list
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)

# create the second linked list
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)

# merge at alternate positions
new_head = merge_alternate(head1, head2)

# print the new linked list
curr = new_head
while curr:
    print(curr.val, end=' ')
    curr = curr.next



#4  In an array, Count Pairs with given sum
def count_pairs_with_sum(arr, target_sum):
    freq = {}
    count = 0
    
    # count frequency of each element in the array
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    
    # count pairs with given sum
    for x in arr:
        diff = target_sum - x
        if diff in freq:
            count += freq[diff]
            if x == diff:
                count -= 1
    
    return count // 2
arr = [1, 5, 7, -1, 5]
target_sum = 6
count = count_pairs_with_sum(arr, target_sum)
print(count)

#5 Find duplicates in an array
def find_duplicates(arr):
    freq = {}
    duplicates = []
    
    # count frequency of each element in the array
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    
    # find duplicates
    for x in arr:
        if freq[x] > 1 and x not in duplicates:
            duplicates.append(x)
    
    return duplicates
arr = [1, 2, 3, 1, 4, 2, 5]
duplicates = find_duplicates(arr)
print(duplicates)

#6 Find the Kth largest and Kth smallest number in an array
def kth_smallest_largest_sort(arr, k):
    # find kth smallest number
    arr.sort()
    kth_smallest = arr[k-1]
    
    # find kth largest number
    arr.sort(reverse=True)
    kth_largest = arr[k-1]
    
    return kth_smallest, kth_largest
arr = [5, 3, 9, 1, 7]
k = 3
kth_smallest, kth_largest = kth_smallest_largest_sort(arr, k)
print(kth_smallest)  # output: 5
print(kth_largest)   # output: 5

import heapq

def kth_smallest_largest_heap(arr, k):
    # find kth largest number
    min_heap = arr[:k]
    heapq.heapify(min_heap)
    for x in arr[k:]:
        if x > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, x)
    kth_largest = min_heap[0]
    
    # find kth smallest number
    max_heap = [-x for x in arr[:k]]
    heapq.heapify(max_heap)
    for x in arr[k:]:
        if x < -max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -x)
    kth_smallest = -max_heap[0]
    
    return kth_smallest, kth_largest

#7 Move all the negative elements to one side of the array
def move_negatives(arr):
    n = len(arr)
    i, j = 0, n-1
    
    while i < j:
        # find the first negative element from the left
        while i < n and arr[i] >= 0:
            i += 1
        
        # find the first positive element from the right
        while j >= 0 and arr[j] < 0:
            j -= 1
        
        if i < j:
            # swap elements at positions i and j
            arr[i], arr[j] = arr[j], arr[i]
    
    return arr
arr = [5, -2, 3, -1, 8, -4, 7]
print(move_negatives(arr))

#8 Reverse a string using a stack data structure
def reverse_string(string):
    stack = []
    # push all characters onto the stack
    for char in string:
        stack.append(char)
    
    reversed_string = ''
    # pop all characters from the stack to get the reversed string
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string
string = 'Hello, world!'
print(reverse_string(string))

#9 Evaluate a postfix expression using stack
def evaluate_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for char in expression:
        if char.isdigit():
            # if the character is a digit, push it onto the stack as an integer
            stack.append(int(char))
        elif char in operators:
            # if the character is an operator, pop two operands from the stack,
            # perform the corresponding operation, and push the result back onto the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)
            elif char == '^':
                stack.append(operand1 ** operand2)

    # the final element on the stack is the result of the expression
    return stack[-1]
expression = '23*54*+9-'
print(evaluate_postfix(expression))

#10 Implement a queue using the stack data structure
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        # push the element onto the first stack
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            # if the second stack is empty, pop all elements from the first stack
            # and push them onto the second stack
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            # if both stacks are empty, return None
            return None

        # pop the top element from the second stack and return it
        return self.stack2.pop()
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # output: 1
print(queue.dequeue())  # output: 2
queue.enqueue(4)
print(queue.dequeue())  # output: 3
print(queue.dequeue())  # output: 4
print(queue.dequeue())  # output: None