'''Given the root of a binary tree, invert the tree, and return its root.'''

def invert_tree(root):
    if not root:
        return
    
    temp = root.left
    root.left = root.right
    root.right = temp

    invert_tree(root.left)
    invert_tree(root.right)

    return root

root = [4,2,7,1,3,6,9]

print(invert_tree(root))