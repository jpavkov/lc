"""
Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
    The number of nodes in the list is in the range [1, 10^5].
    0 <= Node.val <= 9
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, head=ListNode):
        self.head = head

    def createList(self, inputList: list) -> ListNode:
        for i, num in enumerate(inputList):
            if i == 0:
                head = ListNode(num)
                node = head
            else:
                node.next = ListNode(num)
                node = node.next
        return head

    def printList(self, head: ListNode):
        node = head
        output = ""
        while node:
            output += " " + str(node.val)
            node = node.next

        print(f"list:{output}")


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # 0 or 1 nodes return True
        if head is None or head.next is None:
            return True

        stack = []
        slow, fast = head, head.next
        isEven = False

        while fast:
            stack.append(slow.val)
            slow = slow.next
            if fast.next is None:
                fast = fast.next
                isEven = True
            else:
                fast = fast.next.next

        if not isEven:
            slow = slow.next

        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next

        return True


# setup
ll = LinkedList()
sol = Solution()

# ex 1: output: True
nums = [1, 2, 2, 1]
head = ll.createList(nums)
print(sol.isPalindrome(head))

# ex 2: output: False
nums = [1, 2]
head = ll.createList(nums)
print(sol.isPalindrome(head))

# ex 3: output: True
nums = [1, 2, 1]
head = ll.createList(nums)
print(sol.isPalindrome(head))

# ex 4: output: False
nums = [1, 2, 3]
head = ll.createList(nums)
print(sol.isPalindrome(head))

# ex 5: output: True
head = ListNode()
print(sol.isPalindrome(head))

# ex 6: output: True
head = ListNode([5])
print(sol.isPalindrome(head))

# ex 7: output: True
nums = [5, 4, 3, 2, 1, 2, 3, 4, 5]
head = ll.createList(nums)
print(sol.isPalindrome(head))
