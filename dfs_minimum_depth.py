from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:
    # current node does not exist
    if root is None:
        return 0

    # no left branch, but right branch
    if root.left is None:
        return minDepth(root.right) + 1
    
    # no right branch, but left branch
    if root.right is None:
        return minDepth(root.left) + 1
    
    # left and right branches
    if root.left and root.right:
        return min(minDepth(root.left), minDepth(root.right)) + 1



# [3,9,20,None,None,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(minDepth(root))

# [2,None,3,None,4,None,5,None,6]
root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
print(minDepth(root))
