'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.'''
from collections import deque
# using recursion
def max_depth(self, root):
    if not root:
        return 0
        
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# using BFS and QUEUE
def max_depth1(self, root):
    if not root:
        return 0
    
    level = 0
    q = deque([root])

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1

    return level


# using DFS ans STACK

root = [3,9,20,None,None,15,7]