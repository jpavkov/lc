"""
Reverse a given linked list

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [5]
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
0 <= Node.val <= 500
"""
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    while cur:
        if cur.next:
            right = cur.next
        


# Test Code
head = ListNode(val=1)
node = head
for i in range(2, 11):
    node.next = ListNode(i)
    node = node.next

cur = head
while cur:
    print(cur.val)
    cur = cur.next
