

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def bfs(root):
    queue = deque([root])
    depth = 0

    while queue:
        nodes_in_row = len(queue)
        depth += 1

        for _ in range(nodes_in_row):

            node = queue.popleft()
            print(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


# root = [1,2,3,4,5,6,7,8,9]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)

depth = bfs(root)

print('There are {} rows in the tree', depth)