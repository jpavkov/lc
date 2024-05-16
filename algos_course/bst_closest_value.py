"""
Given the root of a binary search tree and a target value, 
return the value in the BST that is closest to the target. 
If there are multiple answers, print the smallest.

Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
-109 <= target <= 109
"""

from typing import Optional
#from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float):

        def returnInOrder(root):
            if not root:
                return []
            else:
                return returnInOrder(root.left) + [root.val] + returnInOrder(root.right)
        
        order = returnInOrder(root)

        return min(order, key=lambda x: abs(target - x))

# root = [4,2,5,1,3]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

sol = Solution()
print(sol.closestValue(root, 2.51))