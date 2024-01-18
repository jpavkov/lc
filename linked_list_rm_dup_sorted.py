"""
Given the head of a sorted linked list, delete all duplicates such 
that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    # x = head.val
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            # reassign cur.next to cur.next.next
            cur.next = cur.next.next
        cur = cur.next


head = ListNode(val=1)
node = head
for i in range(2, 11):
    if i % 2 == 0:
        node.next = ListNode(i - 1)
    else:
        node.next = ListNode(i)
    node = node.next

# check out list before
node = head
while node:
    print(node.val)
    node = node.next

# run deleteDuplicates
deleteDuplicates(head)

# check out list after
node = head
while node:
    print(node.val)
    node = node.next
