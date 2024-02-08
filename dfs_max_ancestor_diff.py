"""
Given the root of a binary tree, find the maximum value v 
for which there exist different nodes a and b where 
v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a 
is equal to b or any child of a is an ancestor of b.
"""

from typing import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.result = 0

        def helper(currentNode, cur_max, cur_min):
            if not currentNode:
                return

            # update result
            self.result = max(self.result,
                              abs(currentNode.val-cur_max),
                              abs(currentNode.val-cur_min))
            
            # update cur_max and cur_min
            cur_max = max(cur_max, currentNode.val)
            cur_min = min(cur_min, currentNode.val)

            # call helper on left and right nodes
            helper(currentNode.left, cur_max, cur_min)
            helper(currentNode.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return self.result


