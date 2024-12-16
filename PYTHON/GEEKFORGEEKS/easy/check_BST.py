'''Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.'''

def is_BST(root):
    def valid(root, left, right):
            if not root:
                return True
            if not (left < root.data and root.data < right):
                return False
                
            return (valid(root.left,left,root.data) and valid(root.right,root.data,right))
                
    return valid(root, float("-inf"), float("+inf"))