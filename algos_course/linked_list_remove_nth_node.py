"""
Given the head of a linked list, remove the nth node 
from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if head.next == None:
            return None

        l, r = head, head
        i = 1
        while r.next:
            i += 1
            r = r.next
            if i - n > 1:
                l = l.next

        print(f"l.val: {l.val}, r.val: {r.val}, i: {i}")

        if n == 1:
            l.next = None
        elif n == i:
            return l.next
        else:
            l.next = l.next.next

        return head


# setup
sol = Solution()
ll = LinkedList()

# Example 1:
head = ll.createList([1, 2, 3, 4, 5])
n = 2
ll.printList(head)
head = sol.removeNthFromEnd(head, n)
ll.printList(head)

# Example 2:
head = ll.createList([1])
n = 1
ll.printList(head)
head = sol.removeNthFromEnd(head, n)
ll.printList(head)

# Example 3:
head = ll.createList([1, 2])
n = 1
ll.printList(head)
head = sol.removeNthFromEnd(head, n)
ll.printList(head)

# Example 4:
head = ll.createList([1, 2])
n = 2
ll.printList(head)
head = sol.removeNthFromEnd(head, n)
ll.printList(head)
