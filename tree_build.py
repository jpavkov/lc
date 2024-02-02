## create a class of Node
## create a class of Tree
## create pre, post and mid depth first search

from typing import Optional

class TreeNode:

    def __init__(self, val: int, left: None, right: None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(values: [], index: int=0) -> TreeNode:
    if index < len(values) and values[index] is not None:
        root = TreeNode(values[index], None, None)
    left_node = index * 2 + 1
    right_node = index * 2 + 2
    if values[left_node] is not None:
        root.left = create_tree(values, index = index * 2 + 1)
    if values[right_node] is not None:
        root.right = create_tree(values, index = index * 2 + 2)
        return root
    return None

values = [2, None, 3, None, 4, None, 5, None, 6]
root = create_tree(values)
print(root.val)
print(root.right.val)
print(root.right.right.val)

values = [3, 9, 20, None, None, 15, 7]
root = create_tree(values)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.left.val)
print(root.right.right.val)


