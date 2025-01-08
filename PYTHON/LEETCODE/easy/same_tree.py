'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.'''

def same_tree(self, p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    
    return (same_tree(p.left, q.left) and same_tree(p.right, q.right))


p = [1,2,3]
q = [1,2,3]

print(same_tree(p, q))