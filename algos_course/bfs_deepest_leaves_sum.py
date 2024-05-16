from collections import deque


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def deepestLeavesSum(root) -> int:
    queue = deque([root])

    while queue:
        current_row = len(queue)
        ans = 0

        for _ in range(current_row):
            node = queue.popleft()
            ans += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
    return ans


# root = [1,2,3,4,5,6,7,8,9]
root = TreeNode(1)
root.left = TreeNode(12)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)

print(deepestLeavesSum(root))