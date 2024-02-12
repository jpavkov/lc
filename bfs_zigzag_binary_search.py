from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root) -> list[list[int]]:
    if not root:
        return []
    
    queue = deque([root])
    ans = []
    left_to_right = True

    while queue:
        current_level = len(queue)
        row_ans = []

        for _ in range(current_level):
            node = queue.popleft()

            if left_to_right:
                row_ans.append(node.val)
            else:
                row_ans.insert(0, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        ans.append(row_ans)
        if left_to_right:
            left_to_right = False
        else:
            left_to_right = True
    
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

print(zigzagLevelOrder(root))

root = TreeNode(1)
print(zigzagLevelOrder(root))