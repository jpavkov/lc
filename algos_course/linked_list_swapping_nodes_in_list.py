"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values 
of the kth node from the beginning and the kth node from the 
end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 105
    0 <= Node.val <= 100
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
    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        curr = head
        i = 0

        while curr:
            curr = curr.next
            i += 1

        first = min(0 + k, i - k + 1)
        second = max(0 + k, i - k + 1)

        if first == second:
            return head

        curr = head
        for j in range(1, second + 1):
            if j == first:
                firstNode = curr
            elif j == second:
                secondNode = curr
            curr = curr.next

        firstNode.val, secondNode.val = secondNode.val, firstNode.val

        return head


# create instances of Solution and linkedList
sol = Solution()
ll = LinkedList()

# ex 1: output: 1, 4, 3, 2, 5
nodes = [1, 2, 3, 4, 5]
head = ll.createList(nodes)
k = 2
ll.printList(head)
sol.swapNodes(head, k)
ll.printList(head)
