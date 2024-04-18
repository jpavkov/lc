"""
Given the head of a singly linked list and two integers 
left and right where left <= right, reverse the nodes 
of the list from position left to position right, 
and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""

# Definition for singly-linked list.


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
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head.next == None or left == right:
            return head

        prev = None
        curr = head
        i = 1
        while i < left:
            prev = curr
            curr = curr.next
            i += 1

        leftStop = prev
        rightStop = curr

        while i <= right:  # and curr.next:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            i += 1

        if leftStop:
            leftStop.next = prev
        else:
            head = prev
        rightStop.next = curr

        return head

    # recursive approach
    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

    #     left, right = head, head
    #     stop = False

    #     def recurseAndReverse(right, m, n):
    #         nonlocal left, stop
    #         if n == 1:
    #             return
    #         right = right.next
    #         if m > 1:
    #             left = left.next
    #         recurseAndReverse(right, m - 1, n - 1)
    #         if left in (right, right.next):
    #             stop = True
    #         if not stop:
    #             left.val, right.val = right.val, left.val
    #             left = left.next

    #     recurseAndReverse(right, m, n)
    #     return head


# create instances of Solution and linkedList
sol = Solution()
ll = LinkedList()

# ex 1: output: 1, 4, 3, 2, 5
nodes = [1, 2, 3, 4, 5]
head = ll.createList(nodes)
ll.printList(head)  # print list
left = 2
right = 4
head = sol.reverseBetween(head, left, right)
ll.printList(head)

# # ex 2: output: 5
# nodes = [5]
# head = ll.createList(nodes)
# ll.printList(head)  # print list
# left = 1
# right = 1
# head = sol.reverseBetween(head, left, right)
# ll.printList(head)

# # ex 3: output: 5, 4, 3
# nodes = [5, 4, 3]
# head = ll.createList(nodes)
# ll.printList(head)  # print list
# left = 2
# right = 2
# head = sol.reverseBetween(head, left, right)
# ll.printList(head)

# # ex 4: output: 5, 3, 4
# nodes = [5, 4, 3]
# head = ll.createList(nodes)
# ll.printList(head)  # print list
# left = 2
# right = 3
# head = sol.reverseBetween(head, left, right)
# ll.printList(head)

# ex 5: output: 4, 5, 3
nodes = [5, 4, 3]
head = ll.createList(nodes)
ll.printList(head)  # print list
left = 1
right = 2
head = sol.reverseBetween(head, left, right)
ll.printList(head)

# ex 6: output: 4, 5, 3
nodes = [5, 4]
head = ll.createList(nodes)
ll.printList(head)  # print list
left = 1
right = 2
head = sol.reverseBetween(head, left, right)
ll.printList(head)
