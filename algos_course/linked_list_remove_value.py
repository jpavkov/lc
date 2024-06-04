"""
Given the head of a linked list and an integer val, remove all 
the nodes of the linked list that has Node.val == val, and 
return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
    The number of nodes in the list is in the range [0, 10^4].
    1 <= Node.val <= 50
    0 <= val <= 50
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, head=ListNode):
        self.head = head

    def createList(self, inputList: list) -> ListNode:
        if len(inputList) == 0:
            return None
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if head is None:
            return head

        while head.val == val:
            if head.next is None:
                return None
            head = head.next

        if head is None:
            return head

        prev = ListNode()
        prev.next = head
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                curr = curr.next
                prev = prev.next

        return head


sol = Solution()
ll = LinkedList()

# ex 1:
head = [1, 2, 6, 3, 4, 5, 6]
head = ll.createList(head)
val = 6
head = sol.removeElements(head, val)
ll.printList(head)

# ex 2:
head = []
head = ll.createList(head)
val = 1
head = sol.removeElements(head, val)
ll.printList(head)

# ex 3:
head = [7, 7, 7, 7]
head = ll.createList(head)
val = 7
head = sol.removeElements(head, val)
ll.printList(head)
