'''Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.'''
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def  array_to_bst(nums: list) -> TreeNode:
    def helper(l, r):
            if l > r:
                return None
            m = (l+r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)
            return root
    
    return helper(0, len(nums) - 1)

nums = [-10,-3,0,5,9]
print(array_to_bst(nums))

