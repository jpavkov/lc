"""
You are given the head of a linked list. Delete the middle 
node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th 
node from the start using 0-based indexing, where ⌊x⌋ denotes 
the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, 
and 2, respectively.
 
Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:

Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:

Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

Constraints:
    The number of nodes in the list is in the range [1, 105].
    1 <= Node.val <= 105
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
    def deleteMiddle(self, head: ListNode) -> ListNode:

        l, r = head, head
        i = 0

        while r.next:
            i += 1
            r = r.next
            if i > 2 and i % 2 == 1:
                l = l.next

        if i == 0:
            return None
        elif i == 1:
            l.next = None
        else:
            l.next = l.next.next

        return head


# setup
sol = Solution()
ll = LinkedList()

# Example 1:
head = ll.createList([1, 3, 4, 7, 1, 2, 6])
ll.printList(head)
head = sol.deleteMiddle(head)
ll.printList(head)

# Example 2:
head = ll.createList([1, 3, 4, 7, 1, 2])
ll.printList(head)
head = sol.deleteMiddle(head)
ll.printList(head)
