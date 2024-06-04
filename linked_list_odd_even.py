"""
Given the head of a singly linked list, group all the nodes 
with odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, 
and so on.

Note that the relative order inside both the even and odd groups 
should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) 
time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
    The number of nodes in the linked list is in the range [0, 10^4].
    -106 <= Node.val <= 106
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return head

        odd_head = head
        even_head = head.next
        prev = None

        odd = head
        even = head.next

        while even:
            if even.next:
                odd.next = even.next
                odd = odd.next
                # if odd.next:
                #     prev = even
            even.next = odd.next

            # if even.next:
            #     odd.next = even.next
            # else:
            #     prev = odd
            # if odd.next:
            #     even.next = odd.next.next
            # odd = odd.next
            # if even.next is None:
            #     prev = even
            # even = even.next

        odd.next = even_head

        # curr = even_head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # if prev:
        #     odd.next = even_head
        # else:
        #     odd.next = even_head

        return head


sol = Solution()
ll = LinkedList()


# ex 1: Output: [1,3,5,2,4]
head = [1, 2, 3, 4, 5]
head = ll.createList(head)
head = sol.oddEvenList(head)
ll.printList(head)

# ex 1b: Output: [1,3,5,2,4,6]
head = [1, 2, 3, 4, 5, 6]
head = ll.createList(head)
head = sol.oddEvenList(head)
ll.printList(head)

# ex 2: Output: [2,3,6,7,1,5,4]
head = [2, 1, 3, 5, 6, 4, 7]
head = ll.createList(head)
head = sol.oddEvenList(head)
ll.printList(head)

# ex 3: Output: [2]
head = [2]
head = ll.createList(head)
head = sol.oddEvenList(head)
ll.printList(head)

# ex 4: Output: [2, 3]
head = [2, 3]
head = ll.createList(head)
head = sol.oddEvenList(head)
ll.printList(head)

# ex 5: output: []
head = ListNode(None)
head = sol.oddEvenList(head)
ll.printList(head)
