"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest 
path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # If the current node is a leaf, return 1
        if not root.left and not root.right:
            return 1

        # Calculate the depth of the left and right subtrees
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # If one of the subtrees is empty, consider the depth of the other subtree
        if left_depth == 0 or right_depth == 0:
            return max(left_depth, right_depth) + 1

        # If both subtrees are non-empty, return the minimum depth
        return min(left_depth, right_depth) + 1

def create_tree(values: List[Optional[int]], index: int = 0) -> Optional[TreeNode]:
    if index < len(values):
        # Create a node for the current value
        current_value = values[index]
        if current_value is not None:
            current_node = TreeNode(current_value)
            # Recursively create left and right children
            current_node.left = create_tree(values, 2 * index + 1)
            current_node.right = create_tree(values, 2 * index + 2)
            return current_node

    return None

# Example usage:
values = [2, None, 3, None, 4, None, 5, None, 6]
root = create_tree(values)

solution = Solution()
result = solution.minDepth(root)
print("Minimum Depth:", result)





