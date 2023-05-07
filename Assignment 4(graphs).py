# Breadth First Traversal for a Graph
from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, source):
        visited = [False] * self.n
        queue = deque()

        visited[source] = True
        queue.append(source)

        while queue:
            u = queue.popleft()
            print(u, end=' ')

            for v in self.adj_list[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)

# Example usage
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)

g.bfs(0)

# Depth First Traversal for a Graph
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, source, visited):
        visited[source] = True
        print(source, end=' ')

        for neighbor in self.adj_list[source]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def dfs_traversal(self):
        visited = [False] * self.n

        for vertex in range(self.n):
            if not visited[vertex]:
                self.dfs(vertex, visited)

# Example usage
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)

g.dfs_traversal()

# Count the number of nodes at given level in a tree using BFS
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes_at_level(root, level):
    if not root:
        return 0

    q = deque([(root, 0)])
    count = 0

    while q:
        node, current_level = q.popleft()

        if current_level == level:
            count += 1

        if node.left:
            q.append((node.left, current_level + 1))

        if node.right:
            q.append((node.right, current_level + 1))

    return count
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Count the number of nodes at level 2
print(count_nodes_at_level(root, 2)) 


# Count number of trees in a forest
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def count_trees(self):
        visited = set()
        count = 0

        for v in range(self.vertices):
            if v not in visited:
                self.dfs(v, visited)
                count += 1

        return count

    def dfs(self, v, visited):
        visited.add(v)

        for neighbor in self.adj_list[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
# Create a forest with 5 trees
g = Graph(10)
g.add_edge(0, 1)
g.add_edge(2, 3)
g.add_edge(4, 5)
g.add_edge(6, 7)
g.add_edge(8, 9)

# Count the number of trees in the forest
print(g.count_trees())

# Detect Cycle in a Directed Graph

from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def has_cycle(self):
        visited = set()
        rec_stack = set()

        for v in self.adj_list:
            if self.dfs(v, visited, rec_stack):
                return True

        return False

    def dfs(self, v, visited, rec_stack):
        visited.add(v)
        rec_stack.add(v)

        for neighbor in self.adj_list[v]:
            if neighbor not in visited:
                if self.dfs(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(v)
        return False
# Create a directed graph with a cycle
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)

# Check if the graph has a cycle
print(g.has_cycle())  # Output: True

# Create a directed acyclic graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

# Check if the graph has a cycle
print(g.has_cycle())




####### **Implement n-Queen’s Problem  ######


class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for x in range(n)] for y in range(n)]
        self.solutions = []

    def solve(self):
        self.solve_helper(0)

    def solve_helper(self, col):
        if col == self.n:
            # Found a solution
            solution = []
            for row in range(self.n):
                solution.append("".join(["Q" if self.board[row][col] == 1 else "." for col in range(self.n)]))
            self.solutions.append(solution)
            return True
        else:
            for row in range(self.n):
                if self.is_valid_move(row, col):
                    self.board[row][col] = 1
                    self.solve_helper(col + 1)
                    self.board[row][col] = 0

    def is_valid_move(self, row, col):
        # Check row
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal
        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check lower diagonal
        i = row
        j = col
        while i < self.n and j >= 0:
            if self.board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True
nq = NQueens(4)
nq.solve()
print(nq.solutions)