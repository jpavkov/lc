"""
82. Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes
that have duplicate numbers, leaving only distinct numbers
from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        curr = head
        while curr:
            print(f"node: {curr}, val: {curr.val}, next: {curr.next}")
            curr = curr.next

        fake = ListNode(-1)
        fake.next = head
        curr = head
        prev = fake

        print(f"node: {fake}, val: {fake.val}, next: {fake.next}")

        while curr:

            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next

        return fake.next


# setup
sol = Solution()
ll = LinkedList()

# head = ll.createList([1, 2, 3, 3, 4, 4, 5])
# head = sol.deleteDuplicates(head)
# ll.printList(head)

# head = ll.createList([1, 1, 2, 3])
# head = sol.deleteDuplicates(head)
# ll.printList(head)

# head = ll.createList([-1, 1, 1, 2, 3])
# head = sol.deleteDuplicates(head)
# ll.printList(head)

head = ll.createList([1, 1])
head = sol.deleteDuplicates(head)
ll.printList(head)
