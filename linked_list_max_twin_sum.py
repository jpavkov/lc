"""
In a linked list of size n, where n is even, the ith node (0-indexed) 
of the linked list is known as the twin of the (n-1-i)th node, if 
0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 
is the twin of node 2. These are the only nodes with twins for n = 4. 
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum 
twin sum of the linked list.

Example 1:
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 

Example 2:
Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

Example 3:
Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

Constraints:
    The number of nodes in the list is an even integer in the range [2, 10^5].
    1 <= Node.val <= 10^5
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
    def pairSum(self, head: ListNode) -> int:

        # set up variables
        n = 1
        ans = 0

        # count nodes and divide by 2, add 1 (for range)
        curr = head
        while curr:
            curr = curr.next.next
            n += 2
        n = int(n / 2)

        # use stack for first half of node values
        stack = []
        curr = head
        for _ in range(1, n + 1):  # n is an odd number, 1 more than half
            stack.append(curr.val)
            curr = curr.next

        # pair sum for first and second half of linked list
        while curr:
            ans = max(ans, stack.pop() + curr.val)
            curr = curr.next

        return ans


sol = Solution()
ll = LinkedList()


# ex 1:
head = [5, 4, 2, 1]
head = ll.createList(head)
ans = sol.pairSum(head)
print(ans)

# ex 2:
head = [4, 2, 2, 3]
head = ll.createList(head)
ans = sol.pairSum(head)
print(ans)

# ex 3:
head = [1, 100000]
head = ll.createList(head)
ans = sol.pairSum(head)
print(ans)
