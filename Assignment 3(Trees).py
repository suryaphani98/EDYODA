#1 Implement Binary tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            queue = [self.root]

            while queue:
                node = queue.pop(0)

                if node.left is None:
                    node.left = new_node
                    break
                else:
                    queue.append(node.left)

                if node.right is None:
                    node.right = new_node
                    break
                else:
                    queue.append(node.right)

    def print_tree(self):
        if self.root is None:
            print("Empty tree")
        else:
            queue = [self.root]

            while queue:
                node = queue.pop(0)

                print(node.data, end=' ')

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
tree = BinaryTree()

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

tree.print_tree() 

#2 Find height of a given tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)

        # Return the maximum of the left and right subtree heights
        return 1 + max(left_height, right_height)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(height(root))

#3 Perform Pre-order, Post-order, In-order traversal
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def preorder_traversal(node):
    if node is not None:
        print(node.data, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=' ')
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=' ')
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Pre-order traversal:")
preorder_traversal(root)  # output: 1 2 4 5 3

print("\nIn-order traversal:")
inorder_traversal(root)  # output: 4 2 5 1 3

print("\nPost-order traversal:")
postorder_traversal(root)

#4 Function to print all the leaves in a given binary tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def print_leaves(node):
    if node is not None:
        if node.left is None and node.right is None:
            print(node.data)
        else:
            print_leaves(node.left)
            print_leaves(node.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print_leaves(root)  

#5 Implement BFS (Breath First Search) and DFS (Depth First Search)
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend(graph[vertex] - visited)
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

bfs(graph, 'A')  # output: A B C D E F




def dfs(graph, start):
    visited = set()

    def dfs_recursive(vertex):
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start)
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

dfs(graph, 'A') 

#6 Find sum of all left leaves in a given Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves(root):
    if root is None:
        return 0

    # Check if the left child of the root is a leaf node
    if root.left is not None and root.left.left is None and root.left.right is None:
        left_sum = root.left.val
    else:
        left_sum = 0

    # Recursively calculate the sum of left leaves in the left and right subtrees
    return left_sum + sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)

# Example usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sum_of_left_leaves(root))

#7 Find sum of all nodes of the given perfect binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_height(root):
    """
    Returns the height of a perfect binary tree rooted at the given node
    """
    height = 0
    while root.left is not None:
        height += 1
        root = root.left
    return height

def node_sum(root):
    if root is None:
        return 0

    # Calculate the total number of nodes in the perfect binary tree
    height = get_height(root)
    total_nodes = 2**(height+1) - 1

    # Traverse the tree and add up the values of each node
    stack = [root]
    node_sum = 0
    while stack:
        node = stack.pop()
        node_sum += node.val
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    return node_sum

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(node_sum(root))
#8 Count subtress that sum up to a given value x in a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_subtrees_with_sum_x(root, x):
    def count_subtrees(node):
        nonlocal count
        if node is None:
            return 0

        # Calculate the sum of the left and right subtrees
        left_sum = count_subtrees(node.left)
        right_sum = count_subtrees(node.right)

        # Check if the subtree rooted at the current node sums up to x
        if node.val + left_sum + right_sum == x:
            count += 1

        # Return the sum of the current node and its subtrees
        return node.val + left_sum + right_sum

    count = 0
    count_subtrees(root)
    return count

# Example usage
root = TreeNode(5)
root.left = TreeNode(-10)
root.right = TreeNode(3)
root.left.left = TreeNode(9)
root.left.right = TreeNode(8)
root.right.left = TreeNode(-4)
root.right.right = TreeNode(7)

print(count_subtrees_with_sum_x(root, 7))

#9 Find maximum level sum in Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_level_sum(root):
    if root is None:
        return 0

    queue = [root]
    max_sum = root.val
    while queue:
        level_sum = 0
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            level_sum += node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        if level_sum > max_sum:
            max_sum = level_sum

    return max_sum

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(max_level_sum(root))
#10 Print the nodes at odd levels of a tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_odd_level_nodes(root):
    def traverse(node, level):
        if node is None:
            return

        if level % 2 != 0:
            print(node.val)

        traverse(node.left, level+1)
        traverse(node.right, level+1)

    traverse(root, 1)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print_odd_level_nodes(root)