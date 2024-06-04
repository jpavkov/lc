"""
Given the head of a singly linked list, reverse the list, 
and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [5]
Output: [5]

Example 3:
Input: head = []
Output: []

Example 4:
Input: head = [1,2]
Output: [2,1]

Constraints:
The number of nodes in the list is n.
1 <= n <= 5000
-5000 <= Node.val <= 5000
"""
# Definition for singly-linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev


# create linked list with 10 nodes
for i in range(1, 5):
    if i == 1:
        head = ListNode(i * 10)
        node = head
    else:
        node.next = ListNode(i * 10)
        node = node.next

# print linked list
cur = head
while cur:
    print(cur.val)
    cur = cur.next

# reverse linked list
sol = Solution()
head = sol.reverseList(head)

# print linked list after reversal
cur = head
while cur:
    print(cur.val)
    cur = cur.next
